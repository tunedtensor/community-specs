# Evaluation

## Setup

- Base model: `Qwen/Qwen3.5-2B`
- Dataset: `zeroshot/twitter-financial-news-sentiment`
- Converted rows in balanced training file: 5,100
- Rows used by trainer: 4,080
- Validation split: 10%
- Test split: 10%
- Epochs: 1
- Precision: bf16
- Max validation eval examples: 120
- Max test eval examples: 120

## Tuned Tensor Run

- TT dataset id: `401f341e-5215-4d7e-b549-f97f1045102e`
- TT behavior spec id: `2f9c1cd3-2b6a-4da0-8fea-875cb929b681`
- TT run id: `61d64e3e-b9a1-48e5-8803-c7c30a4df5a8`
- TT model id: `fd09ae23-1935-48b4-b838-9e563df59b49`
- Hosted model: [tunedtensor/qwen3.5-2b-financial-sentiment](https://huggingface.co/tunedtensor/qwen3.5-2b-financial-sentiment)

## Results

Primary validation eval:

| Metric | Base | Tuned | Delta |
| --- | ---: | ---: | ---: |
| Average score | 0.819 | 0.903 | +0.084 |
| Pass rate | 79.2% | 86.7% | +7.5 pts |

Test eval:

| Metric | Base | Tuned | Delta |
| --- | ---: | ---: | ---: |
| Average score | 0.834 | 0.875 | +0.041 |
| Pass rate | 80.0% | 85.8% | +5.8 pts |

Output diagnostics:

- Valid JSON: 100%
- Strict JSON: 100%
- Expected schema keys: 100%
- Non-JSON prefix: 0%

## Local Smoke Tests

The exported model was downloaded and served locally with Tuned Tensor's OpenAI-compatible runtime. On 20 hand-curated finance/social examples, all 20 responses returned valid JSON with the expected classification.

## Notes

The tuned model improved validation and test scores while preserving the strict JSON contract. Remaining evaluation needs include:

- Larger held-out market-social samples from a different source
- More ambiguous mixed-signal headlines
- Posts containing sarcasm, abbreviations, or ticker-heavy slang
- Time-aware tests where old market news should not be interpreted as current advice
