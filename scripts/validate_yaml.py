#!/usr/bin/env python3
"""Validate YAML syntax, indentation, and required coursework examples."""
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
YAML_FILES = sorted(
    path for path in ROOT.rglob("*")
    if path.is_file() and path.suffix.lower() in {".yml", ".yaml"}
    and ".git" not in path.parts
)

def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)

if not YAML_FILES:
    fail("No YAML files were found.")

for path in YAML_FILES:
    raw = path.read_text(encoding="utf-8")
    relative = path.relative_to(ROOT)
    if "\t" in raw:
        fail(f"{relative}: tab characters are not allowed.")
    for number, line in enumerate(raw.splitlines(), start=1):
        if line.strip() and not line.lstrip().startswith("#"):
            indentation = len(line) - len(line.lstrip(" "))
            if indentation % 2:
                fail(f"{relative}:{number}: indentation must use multiples of two spaces.")
        if line.rstrip(" \r") != line:
            fail(f"{relative}:{number}: trailing whitespace found.")
    try:
        yaml.load(raw, Loader=yaml.BaseLoader)
    except yaml.YAMLError as exc:
        fail(f"{relative}: invalid YAML: {exc}")

required = {"simple-config.yml", "nested-structure.yml", "workflow-spec.yml"}
present = {path.name for path in YAML_FILES}
missing = required - present
if missing:
    fail(f"Missing required coursework files: {', '.join(sorted(missing))}")

print(f"SUCCESS: {len(YAML_FILES)} YAML files passed syntax and formatting checks.")
for path in YAML_FILES:
    print(f"  - {path.relative_to(ROOT)}")
