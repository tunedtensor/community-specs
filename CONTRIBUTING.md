# Contributing

Thanks for helping build a small, useful library of Tuned Tensor specs.

This repo is intentionally simple. A contribution should make it easier for someone to copy a `tunedtensor.json` file, understand what it does, and adapt it for their own small model.

## Add A Spec

Start from the template:

```bash
cp -R template specs/my-new-spec
```

Then edit:

- `tunedtensor.json` - required
- `dataset-card.md` - optional
- `model-card.md` - optional
- `eval.md` - optional

Only keep the optional cards when they add real context.

## What Makes A Good Spec

A good spec is:

- Narrow: one clear behavior, not a general assistant.
- Inspectable: examples make the input and output contract obvious.
- Runnable: `tt eval -f tunedtensor.json` should pass.
- Honest: limitations and eval gaps are stated plainly.
- Reusable: another person can copy it and adapt it without a lot of setup.

## Before Opening A PR

Run:

```bash
python3 -m json.tool specs/my-new-spec/tunedtensor.json >/dev/null
tt eval -f specs/my-new-spec/tunedtensor.json
```

Check that links to datasets and models are public, if you include them.

## Do Not Commit

- Model weights
- Private datasets
- API keys, tokens, passwords, or `.env` files
- User data or proprietary data you do not have permission to publish

Linked datasets, base models, and fine-tuned models keep their own licenses. Please include license notes when they matter.
