#!/usr/bin/env python3
# ~/macro_index.py
# Scan Klipper macro files under ~/printer_data/config/macros and produce MACRO_INDEX.md

import re
from pathlib import Path
import os
import sys

# Target macros directory (will expand ~ and $HOME)
MACROS_DIR = Path(os.path.expanduser("~/printer_data/config/macros"))
OUT_MD = MACROS_DIR / "MACRO_INDEX.md"

if not MACROS_DIR.exists():
    print(f"Error: macros directory not found: {MACROS_DIR}")
    sys.exit(2)

# Regex patterns (single-line strings)
macro_re = re.compile(r'^\s*\[gcode_macro\s+([A-Za-z0-9_]+)\]\s*$', re.MULTILINE)
desc_re = re.compile(r'^\s*description:\s*(.+)\s*$', re.IGNORECASE | re.MULTILINE)
param_default_re = re.compile(
    r'\{\%\s*set\s+([A-Za-z0-9_]+)\s*=\s*params\.([A-Za-z0-9_]+)\|default\(([^\)]+)\)', re.IGNORECASE)
jinja_param_re = re.compile(r'params\.([A-Za-z0-9_]+)')

results = []

for f in sorted(MACROS_DIR.glob("*.cfg")):
    try:
        text = f.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Warning: could not read {f}: {e}")
        continue

    for m in macro_re.finditer(text):
        name = m.group(1)
        start = m.end()
        next_m = macro_re.search(text, start)
        block = text[start: next_m.start() if next_m else None]

        desc_m = desc_re.search(block)
        desc = desc_m.group(1).strip() if desc_m else ""

        params = {}
        for p in param_default_re.finditer(block):
            param_key = p.group(2)
            default_val = p.group(3).strip()
            params[param_key] = default_val

        params_ref = set(jinja_param_re.findall(block))
        for pr in params_ref:
            if pr not in params:
                params[pr] = None

        results.append({
            "name": name,
            "description": desc,
            "file": f.name,
            "params": params
        })

# Build markdown
md_lines = []
md_lines.append("# Macro index (generated)\n")
md_lines.append("_Auto-generated list of macros found in the macros folder_\n")
by_file = {}
for r in results:
    by_file.setdefault(r["file"], []).append(r)

for file in sorted(by_file):
    md_lines.append(f"## {file}\n")
    for r in by_file[file]:
        param_list = ", ".join([f"{k}={v}" if v is not None else k for k,v in sorted(r["params"].items())]) or "none"
        desc_text = r['description'] if r['description'] else "no description"
        md_lines.append(f"- **{r['name']}** — {desc_text}; **params:** {param_list}\n")
    md_lines.append("\n")

try:
    OUT_MD.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"Wrote macro index to {OUT_MD}")
except Exception as e:
    print(f"Error writing {OUT_MD}: {e}")
    sys.exit(3)
