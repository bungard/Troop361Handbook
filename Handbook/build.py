#!/usr/bin/env python3
"""
build.py — Compiles Troop 361 handbook markdown files into a self-contained index.html.

The compiled file works when opened directly in a browser (no local server needed)
and is what gets deployed to GitHub Pages.

Usage:
    python build.py

After running, open index.html directly in any browser.
"""

import json
import os
import re

# Must match the SECTIONS config in index.html
SECTIONS = [
    ("1.1", "Section1-Welcome/1.1-Welcome.md"),
    ("1.2", "Section1-Welcome/1.2-Organization.md"),
    ("1.3", "Section1-Welcome/1.3-ScoutingSpirit.md"),
    ("1.4", "Section1-Welcome/1.4-Organization.md"),
    ("1.5", "Section1-Welcome/1.5-UniformGear.md"),
    ("1.6", "Section1-Welcome/1.6 Safety.md"),
    ("2.1", "Section2-Advancement/2.1-PathToEagle.md"),
    ("2.2", "Section2-Advancement/2.2-Conferences.md"),
    ("2.3", "Section2-Advancement/2.3-MeritBadges.md"),
    ("2.4", "Section2-Advancement/2.4-Awards.md"),
    ("3.1", "Section3-Outdoor/3.1-CampingEssentials.md"),
    ("3.2", "Section3-Outdoor/3.2-LeaveNoTrace.md"),
    ("3.3", "Section3-Outdoor/3.3-OutdoorSkills.md"),
    ("3.4", "Section3-Outdoor/3.4-CampingRules.md"),
    ("4.1", "Section4-Operations/4.1-Meetings.md"),
    ("4.2", "Section4-Operations/4.2-CodeOfConduct.md"),
    ("4.3", "Section4-Operations/4.3-Parents.md"),
    ("4.4", "Section4-Operations/4.4-Appendix.md"),
]

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(SCRIPT_DIR, "index.html")
MARKER_RE  = re.compile(
    r"// BUILD:CACHE_START.*?// BUILD:CACHE_END",
    re.DOTALL,
)

def build():
    # Read all markdown files
    cache = {}
    missing = []
    for section_id, rel_path in SECTIONS:
        abs_path = os.path.join(SCRIPT_DIR, rel_path)
        if os.path.exists(abs_path):
            with open(abs_path, encoding="utf-8") as f:
                cache[section_id] = f.read()
        else:
            missing.append(rel_path)

    if missing:
        print("Warning: missing files (skipped):")
        for p in missing:
            print(f"  {p}")

    # Build replacement block
    cache_json = json.dumps(cache, ensure_ascii=False, indent=2)
    replacement = f"// BUILD:CACHE_START\nconst cache = {cache_json};\n// BUILD:CACHE_END"

    # Inject into index.html
    with open(INDEX_PATH, encoding="utf-8") as f:
        html = f.read()

    if not MARKER_RE.search(html):
        print("Error: BUILD markers not found in index.html")
        return

    compiled = MARKER_RE.sub(replacement, html)

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(compiled)

    print(f"Built index.html — {len(cache)} sections compiled.")
    print("Open index.html in any browser (no server needed).")

if __name__ == "__main__":
    build()
