#!/usr/bin/env python3
import os
from pathlib import Path
from urllib.parse import quote

def list_notebooks(root: Path):
    notebooks = []
    for path in root.rglob('*.ipynb'):
        if '.ipynb_checkpoints' in path.parts:
            continue
        notebooks.append(path.relative_to(root))
    notebooks.sort(key=lambda p: [part.lower() for part in p.parts])
    return notebooks

def make_markdown(notebooks):
    lines = ["<!-- BEGIN NOTEBOOK TOC -->", "### 📑 Table des notebooks", ""]
    current_dir = None
    for nb in notebooks:
        folder = nb.parent
        display = nb.name.replace('.ipynb', '').replace('_', ' ')
        link = quote(nb.as_posix())
        if folder == Path('.'):
            lines.append(f"- [{display}](./{link})")
        else:
            if current_dir != folder:
                lines.append(f"- **{folder}/**")
                current_dir = folder
            lines.append(f"  - [{display}](./{link})")
    lines.append("")
    lines.append("*Généré via `python scripts/generate_notebook_toc.py`.*")
    lines.append("<!-- END NOTEBOOK TOC -->")
    return "\n".join(lines)

def update_readme(root: Path):
    readme = root / 'README.md'
    toc = make_markdown(list_notebooks(root))
    text = readme.read_text(encoding='utf-8')
    if '<!-- BEGIN NOTEBOOK TOC -->' in text:
        start = text.index('<!-- BEGIN NOTEBOOK TOC -->')
        end = text.index('<!-- END NOTEBOOK TOC -->') + len('<!-- END NOTEBOOK TOC -->')
        new_text = text[:start] + toc + text[end:]
    else:
        new_text = text.rstrip() + '\n\n' + toc + '\n'
    readme.write_text(new_text, encoding='utf-8')

if __name__ == '__main__':
    update_readme(Path(__file__).resolve().parents[1])
