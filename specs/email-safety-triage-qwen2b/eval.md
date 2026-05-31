# Evaluation

## Setup

- Base model: `Qwen/Qwen3.5-2B`
- Dataset: `weijianzhg/email-safety-triage-10k`
- Train rows: 8,000
- Validation rows: 1,000
- Test rows: 1,000
- Epochs: 1
- Precision: bf16
- Max validation eval examples: 200
- Max test eval examples: 200

## Tuned Tensor Run

- TT dataset id: `00e764e5-5104-42f5-afd6-9773b72a9bdd`
- TT behavior spec id: `cb5f6659-9607-4b40-a29d-8328377d9491`
- TT run id: `be85015a-85b0-4420-a8b6-26d948c7d6b2`
- TT model id: `444c7c69-4907-4d08-a2ef-6ce688678f19`
- Hosted model name: `Qwen3.5-2B-ft-be85015a`

## Results

Primary validation eval:

| Metric | Base | Tuned | Delta |
| --- | ---: | ---: | ---: |
| Average score | 0.528 | 0.856 | +0.328 |
| Pass rate | 57.5% | 89.5% | +32.0 pts |

Test eval:

| Metric | Base | Tuned | Delta |
| --- | ---: | ---: | ---: |
| Average score | 0.537 | 0.862 | +0.325 |
| Pass rate | 61.5% | 89.0% | +27.5 pts |

Output diagnostics:

- Valid JSON: 100%
- Strict JSON: 100%
- Expected schema keys: 100%
- Non-JSON prefix: 0%
- Visible reasoning prefix: 0%

## Notes

The most important gain is reliability under a constrained JSON contract. The tuned model improved task score and pass rate while producing schema-compatible output on capped evals.

Remaining evaluation needs:

- Multilingual email
- HTML email and attachment-derived text
- Organization-specific routing labels
- Subtle business email compromise examples
- Held-out production-like inbox samples
