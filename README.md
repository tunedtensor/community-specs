# Tuned Tensor Community Specs

Free, open-source Tuned Tensor spec files for small specialist language models.

This repository is intentionally simple. Each example is centered on one file:

```text
tunedtensor.json
```

That JSON file is the behavior spec. It contains the task description, system prompt, guidelines, constraints, examples, and base model.

Optional notes can sit beside the spec when they are useful:

- `dataset-card.md`
- `model-card.md`
- `eval.md`

## Template

Start from the simple template:

```bash
cp -R template specs/my-new-spec
```

Then edit `specs/my-new-spec/tunedtensor.json`. The optional cards can be deleted if you do not have a public dataset, model, or eval yet.

## Use A Spec

Copy a spec locally:

```bash
cp specs/email-safety-triage-qwen2b/tunedtensor.json ./tunedtensor.json
tt eval -f tunedtensor.json
```

Then edit the JSON for your own task, examples, labels, or base model.

## Validate Specs

Run the same check used by CI:

```bash
scripts/validate-specs.sh
```

## Add A Spec

Add a folder under `specs/` with:

```text
tunedtensor.json
dataset-card.md
model-card.md
eval.md
```

Only `tunedtensor.json` is required. The notes are helpful when a public dataset, model, or evaluation exists.

Before opening a PR, read [CONTRIBUTING.md](CONTRIBUTING.md). Do not commit model weights, private datasets, API keys, tokens, or `.env` files.

## License

The repository content is licensed under the MIT License unless a file says otherwise. Linked datasets, base models, and fine-tuned models keep their own licenses.
