# Tuned Tensor Community Specs

Free, open-source behavior specs and runnable recipes for small specialist language models.

This repository is for people who want to build, share, and learn from compact LLMs that do one useful job well. Each example is intended to be practical: a behavior spec, example rows, dataset and model links, evaluation notes, and local serving instructions.

Small models are most interesting when the task is narrow, the output contract is clear, and progress is measurable. This library collects those recipes in one place.

## New To Small Model Fine-Tuning?

Start by reading one complete recipe before creating your own. A recipe shows the full path from intent to a working specialist model: define the behavior, collect or link a dataset, evaluate the base model, fine-tune, compare results, and serve the model locally.

You can use these specs even if you are not ready to train anything yet. Clone a recipe, inspect the `tunedtensor.json` behavior spec, try the examples, and change the labels or output schema to match a task you care about.

## Start Here

The first complete recipe is:

- [Email Safety Triage Qwen 2B](specs/email-safety-triage-qwen2b/README.md)

It fine-tunes `Qwen/Qwen3.5-2B` for email triage, phishing/spam risk classification, and prompt-attack filtering. The model returns strict JSON that can be routed or audited by downstream systems.

## What Is A Spec?

A community spec is a small-model recipe with enough context to reproduce, evaluate, or adapt the model.

A strong spec includes:

- A narrow task and target user
- A Tuned Tensor behavior spec
- Clear input and output examples
- A JSON Schema when the output is structured
- Dataset provenance and licensing notes
- Base model and tuned model links
- Before/after evaluation results
- Local serving instructions
- Known limitations

## Contribution Levels

You do not need a finished model to contribute. Contributions can land at three levels:

- **Spec only**: behavior spec, examples, and README.
- **Spec + dataset**: public dataset link or generation script.
- **Full recipe**: spec, dataset, trained model, evals, and runbook.

The library should make it easy for a curious person to clone, run, inspect, and adapt a small model.

## Catalog

The machine-readable index lives in [catalog.json](catalog.json). It is intentionally simple so a website, CLI, or dashboard can render it later.

## Validate Locally

```bash
python3 scripts/validate_catalog.py
python3 scripts/validate_spec_examples.py
```

## Repository Policy

Keep this repo lightweight:

- Do not commit model weights.
- Do not commit private datasets, secrets, tokens, or `.env` files.
- Link to public model and dataset artifacts.
- Preserve upstream dataset attribution and license terms.

## License

The repository content is licensed under the MIT License unless a file says otherwise. Linked datasets, base models, and fine-tuned models keep their own licenses.
