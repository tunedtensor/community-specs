# Spec Name

One-sentence summary of what this small model does.

## Task

Describe the target behavior, target users, and why this is a good fit for a small specialist model.

## Artifacts

- Behavior spec: `tunedtensor.json`
- Examples: `examples.jsonl`
- Output schema: `output.schema.json`
- Dataset: add public dataset link or describe generation script
- Model: add public model link when available

## Try It

```bash
tt eval -f tunedtensor.json
```

If you have a model artifact:

```bash
tt models serve <model-dir-or-artifact> \
  --spec tunedtensor.json \
  --json-schema output.schema.json \
  --host 127.0.0.1 \
  --port 8000 \
  --temperature 0
```

## Evaluation

Summarize base model and tuned model results. Include enough detail for readers to understand the improvement and remaining failure modes.

## Limitations

Explain where this model is likely to fail and what users should test before production use.
