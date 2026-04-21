#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import quote

CATEGORIES = [
    {
        "title": "Fondamentaux Python / NumPy / Pandas",
        "keywords": [
            "first", "numpy", "dummy", "training", "utilization", "implementation",
            "two-dimensional", "creation", "waama", "mtfuji data"
        ]
    },
    {
        "title": "Préparation de données & exploration tabulaire",
        "keywords": [
            "analysis", "cleaning", "property", "home price", "homecredit",
            "credit information", "housing", "data analysis", "data cleaning", "house"
        ]
    },
    {
        "title": "Parcours Sprints & algorithmes classiques",
        "keywords": ["sprint", "binary classification", "iris", "svm", "regression"]
    },
    {
        "title": "Deep learning & vision",
        "keywords": [
            "resnet", "u_net", "faster", "yolo", "simpleconv", "cnn",
            "tensor", "keras", "anchored", "conv", "simpleconv2d", "simpleconv1d", "turing"
        ]
    },
    {
        "title": "Modèles séquentiels & séries temporelles",
        "keywords": ["lstm", "seq2seq", "rnn", "recurrent", "waama"]
    },
    {
        "title": "NLP & compréhension",
        "keywords": ["traitement", "langage", "ecriture", "comprehension", "nlp"]
    },
    {
        "title": "Casse-têtes & mathématiques appliquées",
        "keywords": ["sorori", "fuji", "problème", "problem", "darts", "paper", "échiquier", "chestnut"]
    }
]
DEFAULT_CATEGORY = "Autres notebooks généralistes"


def list_notebooks(root: Path):
    notebooks = []
    for path in root.rglob('*.ipynb'):
        if '.ipynb_checkpoints' in path.parts:
            continue
        notebooks.append(path.relative_to(root))
    notebooks.sort(key=lambda p: [part.lower() for part in p.parts])
    return notebooks


def categorize(nb: Path):
    name = nb.name.lower()
    for category in CATEGORIES:
        if any(keyword.lower() in name for keyword in category["keywords"]):
            return category["title"]
    return DEFAULT_CATEGORY


def make_markdown(notebooks):
    sections = {cat["title"]: [] for cat in CATEGORIES}
    sections[DEFAULT_CATEGORY] = []
    for nb in notebooks:
        cat = categorize(nb)
        sections.setdefault(cat, []).append(nb)
    lines = ["<!-- BEGIN NOTEBOOK TOC -->", "### 📑 Table des notebooks (navigation thématique)", ""]
    ordered_titles = [cat["title"] for cat in CATEGORIES] + [DEFAULT_CATEGORY]
    for title in ordered_titles:
        entries = sections.get(title, [])
        if not entries:
            continue
        lines.append(f"#### {title}")
        lines.append("")
        for nb in entries:
            display = nb.name.replace('.ipynb', '').replace('_', ' ')
            link = quote(nb.as_posix())
            lines.append(f"- [{display}](./{link})")
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
