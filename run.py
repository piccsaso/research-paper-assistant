import argparse
import csv
import json
from pathlib import Path
from src.retrieval import read_corpus, retrieve, context_pack

ROOT = Path(__file__).resolve().parent


def evaluate(passages, cases, top_k):
    details = []
    for case in cases:
        matches = retrieve(case['question'], passages, top_k)
        ids = [m['citation'] for m in matches]
        expected = case['expected_citation']
        # Empty citation denotes a deliberately unrelated query.
        hit = expected in ids if expected else not ids
        details.append({'question':case['question'],'expected_citation':expected,
                        'retrieved_citations':ids,'passed':hit,'answerable':bool(expected)})
    answerable = [r for r in details if r['answerable']]
    unrelated = [r for r in details if not r['answerable']]
    return {'top_k':top_k, 'cases':len(details),
            'answerable_hit_rate_at_k':sum(r['passed'] for r in answerable)/len(answerable) if answerable else None,
            'unrelated_zero_overlap_rate':sum(r['passed'] for r in unrelated)/len(unrelated) if unrelated else None,
            'details':details}


def main():
    parser = argparse.ArgumentParser(description='Search local Markdown documents or evaluate the retrieval baseline. No API key required.')
    parser.add_argument('--corpus', type=Path, default=ROOT/'examples'/'documents')
    parser.add_argument('--question')
    parser.add_argument('--evaluate', action='store_true')
    parser.add_argument('--cases',type=Path,default=ROOT/'evaluation'/'questions.csv')
    parser.add_argument('--top-k', type=int, default=3)
    args = parser.parse_args()
    if not args.question and not args.evaluate:
        parser.error('Provide --question or --evaluate')
    if args.top_k < 1:
        parser.error('--top-k must be positive')
    passages = read_corpus(args.corpus)
    out = ROOT/'reports'/'generated'
    out.mkdir(parents=True,exist_ok=True)
    if args.question:
        matches = retrieve(args.question, passages,args.top_k)
        print('RETRIEVED EXCERPTS - not an AI-generated or validated answer')
        for m in matches:
            print(f'\n[{m["citation"]}] relevance={m["score"]:.3f}\n{m["text"]}')
        pack = context_pack(args.question,matches)
        (out/'context.txt').write_text(pack,encoding='utf-8')
        if not matches:
            print('No matching evidence. This is a lexical overlap check, not reliable answerability detection.')
        print('\nSaved reports/generated/context.txt for the future generation stage.')
    if args.evaluate:
        with args.cases.open(newline='',encoding='utf-8') as f:
            cases = list(csv.DictReader(f))
        if not cases or not {'question','expected_citation'}.issubset(cases[0]):
            raise ValueError('Evaluation CSV needs question and expected_citation, plus at least one row.')
        result = evaluate(passages,cases,args.top_k)
        result['corpus'] = str(args.corpus)
        result['limitations'] = 'Tiny educational fixture benchmark. Measures retrieval only, not answer correctness, hallucinations, or robust abstention.'
        (out/'evaluation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
        print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
