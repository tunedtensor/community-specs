# Dataset Card

## Dataset

- Name: `weijianzhg/email-safety-triage-10k`
- Link: [Hugging Face dataset](https://huggingface.co/datasets/weijianzhg/email-safety-triage-10k)
- Rows: 10,000
- Format: JSONL with `input` and `output` string fields
- SHA-256: `f877ed8155a74cc73a9ecb0e75929e5a12d9a6f0060ce8294cb2ec0832060fb7`

Each output string parses to a JSON object with:

- `triage`
- `priority`
- `risk`
- `should_process`
- `confidence`
- `reason`

## Composition

Risk distribution:

| Risk | Rows |
| --- | ---: |
| none | 4,843 |
| phishing | 2,102 |
| prompt_attack | 1,763 |
| spam | 997 |
| suspicious | 295 |

Triage distribution:

| Triage | Rows |
| --- | ---: |
| ignore | 3,925 |
| review | 3,338 |
| archive | 997 |
| reply | 979 |
| escalate | 761 |

## Sources

The dataset combines permissively licensed upstream datasets with project-generated examples. The dataset license is marked as composite because downstream users should preserve upstream attribution and follow each source dataset's license terms.

## Processing

The build process redacts obvious URLs, email addresses, phone-like identifiers, long numeric identifiers, and common account/invoice/ticket/order IDs. Rows are deduplicated by an input/output fingerprint.

## Limitations

This dataset should not be treated as a complete phishing detector, malware detector, or legal/compliance review set. Redaction is best-effort and should be re-audited before redistribution in stricter environments.
