#!/usr/bin/env bash
set -euo pipefail

shopt -s nullglob

specs=(template/tunedtensor.json specs/*/tunedtensor.json)

if [ "${#specs[@]}" -eq 0 ]; then
  echo "No tunedtensor.json files found"
  exit 1
fi

for spec in "${specs[@]}"; do
  echo "Validating ${spec}"
  python3 -m json.tool "${spec}" >/dev/null
  tt eval -f "${spec}"
done
