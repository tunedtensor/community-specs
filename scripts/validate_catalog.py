#!/usr/bin/env python3
"""Validate the community spec catalog."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SPEC_FILES = ("README.md", "tunedtensor.json", "examples.jsonl")


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        fail(f"{path.relative_to(ROOT)} is not valid JSON: {exc}")


def main() -> None:
    catalog_path = ROOT / "catalog.json"
    catalog = load_json(catalog_path)
    if not isinstance(catalog, dict):
        fail("catalog.json must contain an object")
    if catalog.get("version") != 1:
        fail("catalog.json version must be 1")

    specs = catalog.get("specs")
    if not isinstance(specs, list) or not specs:
        fail("catalog.json must contain a non-empty specs array")

    seen_ids: set[str] = set()
    for index, spec in enumerate(specs):
        if not isinstance(spec, dict):
            fail(f"catalog spec at index {index} must be an object")

        spec_id = spec.get("id")
        if not isinstance(spec_id, str) or not spec_id:
            fail(f"catalog spec at index {index} is missing id")
        if spec_id in seen_ids:
            fail(f"duplicate spec id: {spec_id}")
        seen_ids.add(spec_id)

        path_value = spec.get("path")
        if not isinstance(path_value, str) or not path_value.startswith("specs/"):
            fail(f"{spec_id}: path must start with specs/")

        spec_dir = ROOT / path_value
        if not spec_dir.is_dir():
            fail(f"{spec_id}: path does not exist: {path_value}")

        for filename in REQUIRED_SPEC_FILES:
            if not (spec_dir / filename).is_file():
                fail(f"{spec_id}: missing required file {filename}")

        spec_json = load_json(spec_dir / "tunedtensor.json")
        if not isinstance(spec_json, dict):
            fail(f"{spec_id}: tunedtensor.json must contain an object")
        if spec_json.get("base_model") != spec.get("base_model"):
            fail(f"{spec_id}: catalog base_model does not match tunedtensor.json")

    print(f"validated {len(specs)} catalog spec(s)")


if __name__ == "__main__":
    main()
