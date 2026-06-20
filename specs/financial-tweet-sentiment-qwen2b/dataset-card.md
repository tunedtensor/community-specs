# Dataset Card

## Dataset

- Name: `zeroshot/twitter-financial-news-sentiment`
- Link: [Hugging Face dataset](https://huggingface.co/datasets/zeroshot/twitter-financial-news-sentiment)
- License: MIT
- Raw rows inspected: 11,931
- Deduplicated rows: 11,924
- Duplicates removed: 7
- Format after conversion: JSONL with `input` and `output` string fields
- Train SHA-256: `dd2ae1ff7cbb8f4185950566f63885db2d99272603bf43f03d15ae77b2d55580`
- Holdout SHA-256: `b5c1be87e937312de8689f5de968a3ad7aa52c375266b4985f0d967086a418d6`

Each output string parses to a JSON object with:

- `sentiment`
- `label`
- `rationale`

## Composition

The larger balanced training set used for this run contained 5,100 converted rows:

| Sentiment | Rows |
| --- | ---: |
| bearish | 1,700 |
| bullish | 1,700 |
| neutral | 1,700 |

The balanced holdout set contained 180 converted rows:

| Sentiment | Rows |
| --- | ---: |
| bearish | 60 |
| bullish | 60 |
| neutral | 60 |

## Processing

Rows were deduplicated, then C0/C1 control characters were removed except standard whitespace. JSONL was written with ASCII escapes.

Selection used a deterministic shuffle seed of `20260620`: the first 60 examples per class were held out, and the next 1,700 examples per class were used for the larger balanced training file.

## Limitations

The source dataset is useful for short financial-news/social sentiment, but labels are coarse. It should not be treated as a market forecast dataset, trading signal dataset, or comprehensive financial-risk benchmark.
