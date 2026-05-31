#!/usr/bin/env python3
"""Validate spec examples and structured outputs."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        fail(f"{path.relative_to(ROOT)} is not valid JSON: {exc}")


def validate_output_against_schema(output: Any, schema: dict[str, Any], path: Path, line_number: int) -> None:
    required = schema.get("required", [])
    if not isinstance(output, dict):
        fail(f"{path.relative_to(ROOT)}:{line_number}: output must parse to a JSON object")

    for key in required:
        if key not in output:
            fail(f"{path.relative_to(ROOT)}:{line_number}: output missing required key {key}")

    if schema.get("additionalProperties") is False:
        allowed = set(schema.get("properties", {}).keys())
        extra = sorted(set(output.keys()) - allowed)
        if extra:
            fail(f"{path.relative_to(ROOT)}:{line_number}: output has extra keys: {', '.join(extra)}")

    for key, rules in schema.get("properties", {}).items():
        if key not in output or not isinstance(rules, dict):
            continue

        value = output[key]
        expected_type = rules.get("type")
        if expected_type == "string" and not isinstance(value, str):
            fail(f"{path.relative_to(ROOT)}:{line_number}: {key} must be a string")
        if expected_type == "boolean" and not isinstance(value, bool):
            fail(f"{path.relative_to(ROOT)}:{line_number}: {key} must be a boolean")
        if expected_type == "number" and not isinstance(value, (int, float)):
            fail(f"{path.relative_to(ROOT)}:{line_number}: {key} must be a number")

        enum = rules.get("enum")
        if enum and value not in enum:
            fail(f"{path.relative_to(ROOT)}:{line_number}: {key} has value outside enum: {value!r}")

        if expected_type == "number":
            minimum = rules.get("minimum")
            maximum = rules.get("maximum")
            if minimum is not None and value < minimum:
                fail(f"{path.relative_to(ROOT)}:{line_number}: {key} is below minimum")
            if maximum is not None and value > maximum:
                fail(f"{path.relative_to(ROOT)}:{line_number}: {key} is above maximum")


def validate_examples(spec_dir: Path) -> int:
    examples_path = spec_dir / "examples.jsonl"
    schema_path = spec_dir / "output.schema.json"
    schema = load_json(schema_path) if schema_path.exists() else None
    if schema is not None and not isinstance(schema, dict):
        fail(f"{schema_path.relative_to(ROOT)} must contain a JSON object")

    count = 0
    for line_number, raw_line in enumerate(examples_path.read_text().splitlines(), start=1):
        if not raw_line.strip():
            continue
        try:
            example = json.loads(raw_line)
        except json.JSONDecodeError as exc:
            fail(f"{examples_path.relative_to(ROOT)}:{line_number}: invalid JSONL row: {exc}")

        if not isinstance(example, dict):
            fail(f"{examples_path.relative_to(ROOT)}:{line_number}: row must be an object")
        if not isinstance(example.get("input"), str) or not example["input"]:
            fail(f"{examples_path.relative_to(ROOT)}:{line_number}: input must be a non-empty string")
        if not isinstance(example.get("output"), str) or not example["output"]:
            fail(f"{examples_path.relative_to(ROOT)}:{line_number}: output must be a non-empty string")

        try:
            parsed_output = json.loads(example["output"])
        except json.JSONDecodeError as exc:
            fail(f"{examples_path.relative_to(ROOT)}:{line_number}: output string is not valid JSON: {exc}")

        if schema is not None:
            validate_output_against_schema(parsed_output, schema, examples_path, line_number)

        count += 1

    if count == 0:
        fail(f"{examples_path.relative_to(ROOT)} has no examples")
    return count


def main() -> None:
    total = 0
    for spec_dir in sorted((ROOT / "specs").iterdir()):
        if spec_dir.is_dir():
            total += validate_examples(spec_dir)
    print(f"validated {total} example row(s)")


if __name__ == "__main__":
    main()
