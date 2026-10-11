# Astronomy Research Paper Assistant

**Status: runnable starter. Real-data portfolio results are still to be built.**

Build the retrieval and evaluation foundation for an evidence-based AI assistant. The first version searches local Markdown documents and returns cited excerpts.

## Run it in five minutes

Requires Python 3.11 or newer. This starter uses only Python's standard library: no dependency installation, API key, or paid service is needed.

1. Click **Code > Download ZIP** on GitHub and extract it.
2. Open the extracted folder containing `run.py`.
3. Click the Windows File Explorer address bar, type `powershell`, and press Enter.
4. Check Python: `python --version`. If Windows does not find it, try `py --version` and substitute `py` in the commands below. If neither works, install Python from [python.org](https://www.python.org/downloads/) and enable the installer option to add Python to PATH.
5. Run:

```powershell
python run.py --question "What is transit depth?"
python run.py --evaluate
```

Then open `reports/generated/context.txt`. Generated files are local outputs and are ignored by Git. The starter's sample results demonstrate the workflow, not research or business findings.

## What works now

- Loads five passages from original educational Markdown notes.
- Ranks passages with a transparent TF-IDF cosine similarity baseline.
- Returns exact excerpts with stable file/paragraph citations.
- Builds a question-and-evidence context file for a later generation stage.
- Evaluates seven hand-written fixture questions with retrieval hit rate and unrelated-query overlap checks.

## First task for you

Create an original note at `examples/documents/your_note.md` about a topic you understand. Separate each paragraph with a blank line. Ask a question using words from your note, then add a row to `evaluation/questions.csv` with the exact citation you expect. Rerun evaluation and inspect `reports/generated/evaluation.json`.

See [START_HERE.md](START_HERE.md) for a guided session and [ROADMAP.md](ROADMAP.md) for the project milestones.

## Validation

```powershell
python -m unittest discover -s tests -v
```

GitHub Actions runs the same tests and demo on Python 3.11. Tests cover selected failure cases and starter behavior; they do not validate scientific conclusions or portfolio readiness.

## Limitations

This is a document retrieval baseline, not an AI-generated answer system. Educational notes are not research papers. The seven questions are a tiny development fixture, not a held-out benchmark. Lexical overlap misses synonyms and can retrieve irrelevant text. Zero overlap is not a reliable answerability detector. No paid API, embeddings, PDF parser, or UI is implemented.

## Sources and method

See [data sources](docs/DATA_SOURCES.md). Keep a development log of decisions and evidence in [docs/LEARNING_LOG.md](docs/LEARNING_LOG.md). No performance or impact claim should be added to a resume until it is supported by work you can reproduce and explain.
