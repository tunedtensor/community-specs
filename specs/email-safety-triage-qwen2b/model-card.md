# Model Card

## Model

- Name: `weijianzhg/email-safety-triage-qwen3.5-2b`
- Base model: `Qwen/Qwen3.5-2B`
- Task: email triage, phishing/spam risk classification, and prompt-attack filtering
- Output: strict JSON
- Training rows: 8,000
- Epochs: 1
- Precision: bf16

Model link:

- [weijianzhg/email-safety-triage-qwen3.5-2b](https://huggingface.co/weijianzhg/email-safety-triage-qwen3.5-2b)

## Intended Use

Use this model as a small local or hosted classifier for email-like content where a downstream system needs inspectable JSON rather than free-form prose.

The core behavior is:

1. Classify operational triage.
2. Detect phishing, spam, and suspicious content.
3. Detect instructions embedded in email bodies that target an AI assistant.
4. Return a constrained JSON object that can be routed or audited.

## Evaluation

| Metric | Base | Tuned | Delta |
| --- | ---: | ---: | ---: |
| Validation average score | 0.528 | 0.856 | +0.328 |
| Validation pass rate | 57.5% | 89.5% | +32.0 pts |
| Test average score | 0.537 | 0.862 | +0.325 |
| Test pass rate | 61.5% | 89.0% | +27.5 pts |

Output diagnostics:

- Valid JSON: 100%
- Strict JSON: 100%
- Expected schema keys: 100%
- Non-JSON prefix: 0%
- Visible reasoning prefix: 0%

## Limitations

This model is trained for structured classification and should not be used as a general assistant. It should be evaluated against the target email distribution before production use.
