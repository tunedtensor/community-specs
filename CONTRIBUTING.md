# Contributing

Thank you for helping build a useful public library of small specialist LLM recipes.

## What To Contribute

A contribution can be:

- A behavior spec with examples
- A spec plus a public dataset
- A complete recipe with spec, dataset, model, evals, and serving notes
- A fix to docs, metadata, validation, or templates

Good examples are narrow, measurable, and easy to adapt.

## Add A New Spec

1. Copy `templates/spec-template` into `specs/<your-spec-id>`.
2. Fill in `README.md`, `tunedtensor.json`, `examples.jsonl`, and any schema/eval files that apply.
3. Add an entry to `catalog.json`.
4. Run validation:

```bash
python3 scripts/validate_catalog.py
python3 scripts/validate_spec_examples.py
```

## Required Files

Every spec should include:

- `README.md`
- `tunedtensor.json`
- `examples.jsonl`

Structured-output specs should also include:

- `output.schema.json`

Complete recipes should include:

- `eval.md`
- `runbook.md`
- `model-card.md`
- `dataset-card.md`

## Artifact Rules

- Do not commit model weights.
- Do not commit private data.
- Do not commit API keys, tokens, `.env` files, or credentials.
- Link to public Hugging Face datasets and models when possible.
- Include source attribution and license notes for datasets.

## Review Standard

A strong PR makes it clear:

- What the model should do
- Why a small model is a good fit
- What data was used
- What changed after fine-tuning
- How someone can run or adapt it
- What limitations remain
