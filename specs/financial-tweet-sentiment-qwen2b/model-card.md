# Model Card

## Model

- Name: `tunedtensor/qwen3.5-2b-financial-sentiment`
- Base model: `Qwen/Qwen3.5-2B`
- Task: financial social-post sentiment extraction
- Output: strict JSON with `sentiment`, `label`, and `rationale`
- Training rows used by trainer: 4,080
- Epochs: 1
- Precision: bf16
- Final training loss: 0.5898758276

Model link:

- [tunedtensor/qwen3.5-2b-financial-sentiment](https://huggingface.co/tunedtensor/qwen3.5-2b-financial-sentiment)

## Intended Use

Use this model as a small classifier for short finance-related tweets, headlines, and market social posts when a downstream system needs a coarse sentiment signal in an inspectable JSON contract.

The core behavior is:

1. Read one finance-related social post.
2. Classify the market signal as `bearish`, `bullish`, or `neutral`.
3. Return the corresponding numeric label, where `0` is bearish, `1` is bullish, and `2` is neutral.
4. Include one short rationale grounded in the post.

## Evaluation

| Metric | Base | Tuned | Delta |
| --- | ---: | ---: | ---: |
| Validation average score | 0.819 | 0.903 | +0.084 |
| Validation pass rate | 79.2% | 86.7% | +7.5 pts |
| Test average score | 0.834 | 0.875 | +0.041 |
| Test pass rate | 80.0% | 85.8% | +5.8 pts |

Output diagnostics:

- Valid JSON: 100%
- Strict JSON: 100%
- Expected schema keys: 100%
- Non-JSON prefix: 0%

## Limitations

This model is trained for coarse sentiment extraction from short market-social text. It is not an investment advisor, trading system, factual market-data source, or risk-management system.

Ambiguous mixed-signal posts may still be difficult, especially when a post contains both a clearly negative primary event and a secondary contrarian or factual framing.
