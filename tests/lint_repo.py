#!/usr/bin/env python3
"""Lint the plugin folder against the directory's pre-submission rules.

Usage: python3 tests/lint_repo.py [plugin_root]
Exits non-zero if any blocking problem is found.
"""
import json
import os
import re
import sys

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), ".."))
MAX_FILE_BYTES = 256 * 1024
MAX_FILES = 512
SKILL_LINE_CAP = 130
DESC_CAP = 600
TEXT_EXT = {".md", ".json", ".py", ".txt", ".yml", ".yaml", ".csv", ""}
FORBIDDEN = {".DS_Store", "Thumbs.db", "desktop.ini", "__MACOSX"}

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def front_matter(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    fields = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fields[k.strip()] = v.strip().strip('"')
    return fields, text


# manifest
manifest_path = os.path.join(ROOT, ".claude-plugin", "plugin.json")
if not os.path.isfile(manifest_path):
    err("missing .claude-plugin/plugin.json")
else:
    manifest = json.load(open(manifest_path, encoding="utf-8"))
    name = manifest.get("name", "")
    if not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?", name):
        err("plugin name must be lowercase letters, digits and hyphens, up to 64 chars")
    for key in ("description", "author", "version"):
        if not manifest.get(key):
            warn("plugin.json missing " + key)
    if not manifest.get("license") and not os.path.isfile(os.path.join(ROOT, "LICENSE")):
        err("no LICENSE file and no license field")

# readme
readme = os.path.join(ROOT, "README.md")
if not os.path.isfile(readme):
    err("missing README.md")
else:
    body = re.sub(r"```.*?```", "", open(readme, encoding="utf-8").read(), flags=re.S)
    if len(body.split()) < 40:
        err("README has fewer than 40 words outside code blocks")

if os.path.isdir(os.path.join(ROOT, "bin")):
    err("top-level bin/ stops claude.ai and Cowork from installing the plugin")

# files
count = 0
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__")]
    for entry in dirnames + filenames:
        if entry in FORBIDDEN:
            err("forbidden system file: " + os.path.join(dirpath, entry))
    for fn in filenames:
        path = os.path.join(dirpath, fn)
        rel = os.path.relpath(path, ROOT)
        count += 1
        if os.path.islink(path):
            err("symbolic link: " + rel)
            continue
        size = os.path.getsize(path)
        if size > MAX_FILE_BYTES:
            err("file over 256 KiB: " + rel)
        ext = os.path.splitext(fn)[1].lower()
        if ext in (".png", ".jpg", ".jpeg"):
            continue
        if ext not in TEXT_EXT:
            err("non-text file type: " + rel)
            continue
        data = open(path, "rb").read()
        try:
            text = data.decode("ascii")
        except UnicodeDecodeError:
            err("non-ASCII characters: " + rel)
            continue
        if ext == ".md" and (chr(8212) in text or " -- " in text):
            warn("dash used as punctuation: " + rel)
if count > MAX_FILES:
    err("more than 512 files in the plugin (%d)" % count)

# skills
skills_dir = os.path.join(ROOT, "skills")
skill_names = sorted(d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d)))
for skill in skill_names:
    path = os.path.join(skills_dir, skill, "SKILL.md")
    if not os.path.isfile(path):
        err("skill folder without SKILL.md: " + skill)
        continue
    fields, text = front_matter(path)
    if fields is None:
        err("no front matter: skills/%s/SKILL.md" % skill)
        continue
    if fields.get("name") != skill:
        err("skill name does not match folder: " + skill)
    desc = fields.get("description", "")
    if not desc:
        err("skill has no description: " + skill)
    elif len(desc) > DESC_CAP:
        warn("description over %d chars (%d): %s" % (DESC_CAP, len(desc), skill))
    lines = text.count("\n") + 1
    if lines > SKILL_LINE_CAP:
        warn("SKILL.md over %d lines (%d): %s" % (SKILL_LINE_CAP, lines, skill))
    if "## Workflow" not in text or "## Important Notes" not in text:
        warn("missing Workflow or Important Notes section: " + skill)
    for ref in re.findall(r"`(references/[^`]+|assets/[^`]+|scripts/[^`]+)`", text):
        target = os.path.join(skills_dir, skill, ref)
        if "<" in ref or "*" in ref or ref.endswith("/"):
            continue
        if not os.path.exists(target):
            if not any(os.path.exists(os.path.join(skills_dir, other, ref)) for other in skill_names):
                warn("skills/%s refers to missing file %s" % (skill, ref))

# commands
commands_dir = os.path.join(ROOT, "commands")
for fn in sorted(os.listdir(commands_dir)) if os.path.isdir(commands_dir) else []:
    fields, text = front_matter(os.path.join(commands_dir, fn))
    if fields is None or not fields.get("description"):
        err("command without description: " + fn)
    else:
        m = re.search(r"Load the `([^`]+)` skill", text)
        if not m:
            warn("command does not load a skill: " + fn)
        elif m.group(1) not in skill_names:
            err("command %s loads unknown skill %s" % (fn, m.group(1)))

print("Skills: %d   Files: %d" % (len(skill_names), count))
for w in warnings:
    print("WARN  " + w)
for e in errors:
    print("ERROR " + e)
print("RESULT: " + ("FAIL" if errors else "PASS") + " (%d errors, %d warnings)" % (len(errors), len(warnings)))
sys.exit(1 if errors else 0)
