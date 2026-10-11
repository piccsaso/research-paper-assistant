# Data sources and assumptions

## Corpus provenance and citation format

The documents under `examples/documents/` are original educational fixture notes written for this project. They are not excerpts from published research and should not be represented as scientific source material. Citation IDs have the form `filename.md:paragraph-N`, counting non-heading blocks separated by blank lines. Editing paragraph order changes IDs: update evaluation labels when you change the corpus.

Use `python run.py --corpus data/documents --question "YOUR_QUESTION"` for your own Markdown documents. Keep downloaded research material in the ignored directory `data/documents/`, with a tracked provenance manifest under `docs/`. Verify permission to redistribute each paper before committing it to GitHub. Public access alone is not blanket permission to republish.

The context file separates the question from document excerpts and says to treat document instructions as untrusted. This wording is a starting point, not a guarantee against prompt injection. A future API integration must enforce its own boundaries and be evaluated. No document content is sent to an external service in this version.
