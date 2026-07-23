#!/usr/bin/env python3
"""Build the v2.15 LaTeX/PDF and scoped Zenodo reproducibility package."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path


PAPER_DIR = Path(__file__).resolve().parent
REPO_ROOT = PAPER_DIR.parents[2]
MARKDOWN = PAPER_DIR / "located-not-forced-generation-count-2026-06-29.md"
TEX = PAPER_DIR / "located-not-forced-generation-count-2026-06-29.tex"
PACKAGE = PAPER_DIR / "zenodo-package-v1.0.0"
BUILD = REPO_ROOT / "_local" / "lnf-v215-release-build"
ARCHIVE = PAPER_DIR / "located-not-forced-v1.0.0.zip"
SOURCE_DATE_EPOCH = "1784822400"  # 2026-07-23T16:00:00Z


PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{mathtools}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{xurl}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{listings}
\usepackage{microtype}
\setlength{\emergencystretch}{3em}
\setlength{\parindent}{1.25em}
\setlength{\parskip}{0.25em}
\widowpenalty=10000
\clubpenalty=10000
\brokenpenalty=10000
\newcolumntype{P}[1]{>{\raggedright\arraybackslash}p{#1}}
\lstset{basicstyle=\ttfamily\footnotesize,breaklines=true,columns=fullflexible}

\newtheorem{theorem}{Theorem}
\newtheorem{lemma}{Lemma}
\theoremstyle{remark}
\newtheorem*{remark}{Remark}

\title{Located, Not Forced:\\
A Scoped Two-Primary Audit of a Clifford Rarita--Schwinger Generation Carrier}
\author{Joseph Hernandez\\Independent Researcher\\
\small\texttt{joe@disruptionjoe.com}}
\date{Version 1.0.0 --- July 2026}
\hypersetup{
  pdftitle={Located, Not Forced: A Scoped Two-Primary Audit of a Clifford Rarita-Schwinger Generation Carrier},
  pdfauthor={Joseph Hernandez},
  pdfsubject={A finite-codomain audit of generation structure in a Clifford Rarita-Schwinger carrier},
  pdfkeywords={generation count, chirality, Clifford algebra, Rarita-Schwinger, stable homotopy, bordism, anomaly, Krein}
}

\begin{document}
\maketitle
"""


POSTAMBLE = r"""
\end{document}
"""


UNICODE_TEXT = {
    "\u2013": "--",
    "\u2014": "---",
    "\u2212": "-",
    "\u2018": "`",
    "\u2019": "'",
    "\u201c": "``",
    "\u201d": "''",
    "\u00a0": " ",
    "\u03b7": r"$\eta$",
    "\u03c0": r"$\pi$",
    "\u039b": r"$\Lambda$",
    "\u0394": r"$\Delta$",
    "\u03c7": r"$\chi$",
    "\u03c3": r"$\sigma$",
    "\u03bd": r"$\nu$",
    "\u2124": r"$\mathbb{Z}$",
    "\u211a": r"$\mathbb{Q}$",
    "\u211d": r"$\mathbb{R}$",
    "\u2282": r"$\subset$",
    "\u2283": r"$\supset$",
    "\u2192": r"$\to$",
    "\u2194": r"$\leftrightarrow$",
    "\u00b1": r"$\pm$",
    "\u00d7": r"$\times$",
    "\u2245": r"$\cong$",
    "\u2260": r"$\ne$",
    "\u2264": r"$\le$",
    "\u2265": r"$\ge$",
    "\u221e": r"$\infty$",
    "\u2229": r"$\cap$",
}


def escape_text(value: str) -> str:
    value = value.replace("\\", r"\textbackslash{}")
    value = value.replace("&", r"\&")
    value = value.replace("%", r"\%")
    value = value.replace("$", r"\$")
    value = value.replace("#", r"\#")
    value = value.replace("_", r"\_")
    value = value.replace("{", r"\{")
    value = value.replace("}", r"\}")
    value = value.replace("~", r"\textasciitilde{}")
    value = value.replace("^", r"\textasciicircum{}")
    for source, replacement in UNICODE_TEXT.items():
        value = value.replace(source, replacement)
    value = value.replace("Sections ", "Sections~")
    value = value.replace("Section ", "Section~")
    value = value.replace("Theorem ", "Theorem~")
    return value


def math_code(value: str) -> str:
    value = value.strip()
    if value.startswith(("tests/", "canon/", "papers/", "review/", "Lean/", "lab/")) or value.endswith(
        (".py", ".md", ".json", ".lean", ".tex")
    ):
        return rf"\path{{{value}}}"
    if value in {"numpy", ".tex", "review/", "tests/", "tests/located-not-forced/"}:
        return rf"\texttt{{{escape_text(value)}}}"
    exact = {
        "*^2 = -1": r"$\star^2=-1$",
        "3-primary torsion component -> integer 3": (
            r"$3\text{-primary torsion component}\to\text{integer }3$"
        ),
        "Delta_cap(P) = dim_C(P intersect W_+) - dim_C(P intersect W_-)": (
            r"$\Delta_{\mathrm{cap}}(P)=\dim_{\mathbb C}(P\cap W_+)"
            r"-\dim_{\mathbb C}(P\cap W_-)$"
        ),
        "Delta_cap(P)=0": r"$\Delta_{\mathrm{cap}}(P)=0$",
        "2^floor(m/2)": r"$2^{\lfloor m/2\rfloor}$",
        "2^(k-1)": r"$2^{k-1}$",
        "|Weyl(D7)|": r"$\lvert\mathrm{Weyl}(D_7)\rvert$",
        "integer_is_3 = False": r"\texttt{integer\_is\_3 = False}",
        "{0 (linear net-chiral, vectorlike), 1 (Pati-Salam family-unit normalization), 2 (A-hat(K3))}": (
            r"$\{0\ \text{(linear net-chiral, vectorlike)},\ "
            r"1\ \text{(Pati--Salam family-unit normalization)},\ "
            r"2\ (\widehat A(K3))\}$"
        ),
        "{960, -288, -384, -192, -336, -128, 128, -8, -480, 60}": (
            r"$\{960,\allowbreak -288,\allowbreak -384,\allowbreak -192,"
            r"\allowbreak -336,\allowbreak -128,\allowbreak 128,"
            r"\allowbreak -8,\allowbreak -480,\allowbreak 60\}$"
        ),
    }
    if value in exact:
        return exact[value]
    value = value.replace("\\", "")
    value = re.sub(r"\|\|(.+?)\|\|", r"\\lVert \1 \\rVert", value)
    value = re.sub(r"^\|\|(.+)\|\|$", r"\\lVert \1 \\rVert", value)
    value = value.replace("(+)", r"\oplus")
    value = value.replace("(x)", r"\otimes")
    value = value.replace("<->", r"\leftrightarrow")
    value = value.replace("->", r"\to")
    value = value.replace("==", "=")
    value = value.replace("+/-", r"\pm")
    value = value.replace(" x ", r" \times ")
    value = value.replace(" intersect ", r" \cap ")
    value = re.sub(r"\bmod\b", r"\\bmod", value)
    value = re.sub(r"\bin\b", r"\\in", value)
    value = value.replace("16bar", r"\overline{\mathbf{16}}")
    value = value.replace("3bar", r"\overline{\mathbf{3}}")
    value = value.replace("A-hat", r"\widehat{A}")
    value = re.sub(r"\bpi_", r"\\pi_", value)
    value = re.sub(r"\bLambda", r"\\Lambda", value)
    value = re.sub(r"\beta\b", r"\\eta", value)
    value = re.sub(r"\bDelta\b", r"\\Delta", value)
    value = re.sub(r"\bGamma\b", r"\\Gamma", value)
    value = re.sub(r"\bsigma\b", r"\\sigma", value)
    value = re.sub(r"\bchi\b", r"\\chi", value)
    value = re.sub(r"\bnu_", r"\\nu_", value)
    value = value.replace(" ⊃ ", r" \supset ")
    value = value.replace(" ⊂ ", r" \subset ")
    value = value.replace(" . ", r" \cdot ")
    value = value.replace("*", r"\cdot ")
    return f"${value}$"


def inline(value: str) -> str:
    tokens: list[str] = []

    def hold(rendered: str) -> str:
        token = f"@@TOKEN{len(tokens)}@@"
        tokens.append(rendered)
        return token

    def render_link(match: re.Match[str]) -> str:
        label, url = match.group(1), match.group(2)
        rendered_label = (
            rf"\nolinkurl{{{label}}}"
            if ":" in label or label.startswith("http")
            else escape_text(label)
        )
        return hold(rf"\href{{{url}}}{{{rendered_label}}}")

    value = re.sub(
        r"\[([^\]]+)\]\(((?:[^()]|\([^()]*\))+)\)",
        render_link,
        value,
    )
    value = re.sub(r"`([^`\n]+)`", lambda match: hold(math_code(match.group(1))), value)
    value = re.sub(
        r"\*\*([^*]+)\*\*",
        lambda match: hold(rf"\textbf{{{inline(match.group(1))}}}"),
        value,
    )
    value = re.sub(
        r"(?<!\*)\*([^*\n]+)\*(?!\*)",
        lambda match: hold(rf"\emph{{{inline(match.group(1))}}}"),
        value,
    )
    value = escape_text(value)
    for index in range(len(tokens) - 1, -1, -1):
        rendered = tokens[index]
        value = value.replace(f"@@TOKEN{index}@@", rendered)
    return value


def table_to_latex(rows: list[list[str]]) -> str:
    columns = len(rows[0])
    if columns == 3:
        spec = r"P{0.14\textwidth}P{0.34\textwidth}P{0.43\textwidth}"
    elif columns == 4:
        spec = r"P{0.14\textwidth}P{0.24\textwidth}P{0.24\textwidth}P{0.24\textwidth}"
    else:
        width = max(0.12, 0.88 / columns)
        spec = "".join(rf"P{{{width:.2f}\textwidth}}" for _ in range(columns))
    output = [r"\begin{longtable}{" + spec + "}", r"\toprule"]
    output.append(" & ".join(inline(cell.strip()) for cell in rows[0]) + r" \\")
    output.append(r"\midrule")
    output.append(r"\endfirsthead")
    output.append(r"\toprule")
    output.append(" & ".join(inline(cell.strip()) for cell in rows[0]) + r" \\")
    output.append(r"\midrule")
    output.append(r"\endhead")
    for row in rows[1:]:
        output.append(" & ".join(inline(cell.strip()) for cell in row) + r" \\")
    output.extend([r"\bottomrule", r"\end{longtable}"])
    return "\n".join(output)


def markdown_to_latex(markdown: str) -> str:
    lines = markdown.splitlines()
    output = [PREAMBLE]
    paragraph: list[str] = []
    in_code = False
    code_lines: list[str] = []
    list_kind: str | None = None
    appendix_started = False
    abstract_open = False
    front_box_open = False
    skip_meta = False

    def close_list() -> None:
        nonlocal list_kind
        if list_kind:
            output.append(rf"\end{{{list_kind}}}")
            list_kind = None

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            output.append(inline(" ".join(part.strip() for part in paragraph)))
            output.append("")
            paragraph = []

    index = 0
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()

        if index == 0 and stripped.startswith("# "):
            index += 1
            continue

        if stripped.startswith("```"):
            flush_paragraph()
            close_list()
            if in_code:
                output.append(r"\begin{lstlisting}")
                output.extend(code_lines)
                output.append(r"\end{lstlisting}")
                code_lines = []
                in_code = False
            else:
                in_code = True
            index += 1
            continue
        if in_code:
            code_lines.append(line)
            index += 1
            continue

        if stripped == "---":
            flush_paragraph()
            close_list()
            if abstract_open:
                output.append(r"\end{abstract}")
                abstract_open = False
            index += 1
            continue

        if stripped.startswith("*Canonical "):
            flush_paragraph()
            skip_meta = True
            index += 1
            continue
        if skip_meta:
            if stripped.startswith("## Abstract"):
                skip_meta = False
            else:
                index += 1
                continue

        if stripped == "## Abstract":
            flush_paragraph()
            close_list()
            output.append(r"\begin{abstract}")
            abstract_open = True
            index += 1
            continue

        heading = re.match(r"^##\s+(.+)$", stripped)
        if heading:
            flush_paragraph()
            close_list()
            title = heading.group(1)
            if title.startswith("Appendix"):
                if not appendix_started:
                    output.append(r"\appendix")
                    appendix_started = True
                title = re.sub(r"^Appendix:\s*", "", title)
            title = re.sub(r"^\d+\.\s*", "", title)
            output.append(rf"\section{{{inline(title)}}}")
            index += 1
            continue

        subheading = re.match(r"^###\s+(.+)$", stripped)
        if subheading:
            flush_paragraph()
            close_list()
            output.append(rf"\subsection{{{inline(subheading.group(1))}}}")
            index += 1
            continue

        if stripped.startswith("|") and index + 1 < len(lines):
            flush_paragraph()
            close_list()
            table: list[list[str]] = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                cells = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                    table.append(cells)
                index += 1
            output.append(r"{\small")
            output.append(table_to_latex(table))
            output.append("}")
            continue

        numbered = re.match(r"^(\d+)\.\s+(.+)$", stripped)
        bullet = re.match(r"^[-*]\s+(.+)$", stripped)
        if numbered or bullet:
            flush_paragraph()
            desired = "enumerate" if numbered else "itemize"
            if list_kind != desired:
                close_list()
                output.append(rf"\begin{{{desired}}}[leftmargin=2em]")
                list_kind = desired
            item_text = numbered.group(2) if numbered else bullet.group(1)
            index += 1
            continuation: list[str] = []
            while index < len(lines):
                candidate = lines[index].strip()
                if not candidate:
                    break
                if (
                    re.match(r"^\d+\.\s+", candidate)
                    or re.match(r"^[-*]\s+", candidate)
                    or candidate.startswith(("#", "|", "```", ">"))
                ):
                    break
                continuation.append(candidate)
                index += 1
            if continuation:
                item_text += " " + " ".join(continuation)
            output.append(r"\item " + inline(item_text))
            continue

        if stripped.startswith(">"):
            flush_paragraph()
            close_list()
            quote_lines: list[str] = []
            while index < len(lines) and lines[index].strip().startswith(">"):
                quote_lines.append(lines[index].strip()[1:].strip())
                index += 1
            output.append(r"\begin{quote}")
            output.append(inline(" ".join(quote_lines)))
            output.append(r"\end{quote}")
            continue

        if not stripped:
            flush_paragraph()
            close_list()
            index += 1
            continue

        if index == 1 and not front_box_open:
            front_box_open = True
            front_lines: list[str] = []
            while index < len(lines):
                current = lines[index].strip()
                if current.startswith("*Canonical "):
                    break
                if current:
                    front_lines.append(current)
                index += 1
            output.append(r"\begin{quote}\small\noindent")
            output.append(inline(" ".join(front_lines)))
            output.append(r"\end{quote}")
            continue

        paragraph.append(stripped)
        index += 1

    flush_paragraph()
    close_list()
    if abstract_open:
        output.append(r"\end{abstract}")
    output.append(POSTAMBLE)
    return "\n".join(output)


def render_tex() -> None:
    TEX.write_text(
        "% Generated from the canonical v2.15 Markdown by build_release.py.\n"
        + markdown_to_latex(MARKDOWN.read_text(encoding="utf-8")),
        encoding="utf-8",
    )


def compile_tex(tex_path: Path, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    environment = os.environ.copy()
    environment["SOURCE_DATE_EPOCH"] = SOURCE_DATE_EPOCH
    environment["FORCE_SOURCE_DATE"] = "1"
    subprocess.run(
        [
            "/opt/homebrew/bin/tectonic",
            "-X",
            "compile",
            str(tex_path),
            "--outdir",
            str(output_dir),
            "--keep-logs",
        ],
        cwd=REPO_ROOT,
        env=environment,
        check=True,
    )
    pdf = output_dir / tex_path.with_suffix(".pdf").name
    if not pdf.exists():
        raise FileNotFoundError(pdf)
    return pdf


def compile_pdf() -> Path:
    return compile_tex(TEX, BUILD)


def iter_path_strings(value: object):
    if isinstance(value, dict):
        for item in value.values():
            yield from iter_path_strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from iter_path_strings(item)
    elif isinstance(value, str):
        yield value


def evidence_paths() -> set[Path]:
    sources = [
        PAPER_DIR / "LOAD-BEARING-NUMBERS.json",
        PAPER_DIR / "CLAIM-AND-PREMISE-LEDGER.json",
    ]
    paths: set[Path] = set()
    for source in sources:
        data = json.loads(source.read_text(encoding="utf-8"))
        for candidate in iter_path_strings(data):
            path = REPO_ROOT / candidate
            if path.is_file():
                paths.add(path)
    return paths


def copy_relative(source: Path, destination_root: Path) -> None:
    relative = source.relative_to(REPO_ROOT)
    target = destination_root / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def build_package(pdf: Path, source_commit: str) -> None:
    PACKAGE.mkdir(parents=True, exist_ok=True)
    shutil.copy2(TEX, PACKAGE / "main.tex")
    shutil.copy2(MARKDOWN, PACKAGE / "manuscript-v2.15.md")

    # Compile the actual deposited source name. PDF link destinations and
    # document internals can depend on the TeX job name, so compiling the
    # long repository filename and merely renaming its PDF is not sufficient
    # for a byte-reproducible `main.tex` -> `main.pdf` release.
    package_pdf = compile_tex(PACKAGE / "main.tex", BUILD / "package")
    shutil.copy2(package_pdf, PACKAGE / "main.pdf")

    root_files = {
        PAPER_DIR / "METADATA.md" if (PAPER_DIR / "METADATA.md").exists() else PACKAGE / "METADATA.md",
        PACKAGE / "CITATION.cff",
        PACKAGE / "README.md",
        PACKAGE / "reproduction.md",
        PACKAGE / "requirements.txt",
        PAPER_DIR / "REVIEWER.md",
        PAPER_DIR / "PRIOR-ART-DELTA.md",
        PAPER_DIR / "LOAD-BEARING-NUMBERS.json",
        PAPER_DIR / "CLAIM-AND-PREMISE-LEDGER.json",
        PAPER_DIR / "validate_release_evidence.py",
        PAPER_DIR / "reproduce_all.py",
        REPO_ROOT / "LICENSE-DOCS.md",
        REPO_ROOT / "LICENSE-CODE.md",
        REPO_ROOT / "lakefile.lean",
        REPO_ROOT / "lake-manifest.json",
        REPO_ROOT / "lean-toolchain",
    }
    root_names = {
        PAPER_DIR / "REVIEWER.md": "REVIEWER.md",
        PAPER_DIR / "PRIOR-ART-DELTA.md": "PRIOR-ART-DELTA.md",
        PAPER_DIR / "LOAD-BEARING-NUMBERS.json": "LOAD-BEARING-NUMBERS.json",
        PAPER_DIR / "CLAIM-AND-PREMISE-LEDGER.json": "CLAIM-AND-PREMISE-LEDGER.json",
        PAPER_DIR / "validate_release_evidence.py": "validate_release_evidence.py",
        PAPER_DIR / "reproduce_all.py": "reproduce_all.py",
        REPO_ROOT / "LICENSE-DOCS.md": "LICENSE-DOCS.md",
        REPO_ROOT / "LICENSE-CODE.md": "LICENSE-CODE.md",
        REPO_ROOT / "lakefile.lean": "lakefile.lean",
        REPO_ROOT / "lake-manifest.json": "lake-manifest.json",
        REPO_ROOT / "lean-toolchain": "lean-toolchain",
    }
    for source in sorted(root_files):
        if not source.exists() or source.parent == PACKAGE:
            continue
        shutil.copy2(source, PACKAGE / root_names.get(source, source.name))

    nested = evidence_paths()
    nested.update(
        {
            MARKDOWN,
            PAPER_DIR / "CLAIM-AND-PREMISE-LEDGER.json",
            PAPER_DIR / "reproduce_all.py",
            PAPER_DIR / "review/HQW-LEAD-premise-flag-map-and-gu-dependency-2026-07-14.md",
            REPO_ROOT / "Lean/GUFormalization/LocatedNotForcedLegs.lean",
            REPO_ROOT / "Lean/GUFormalization/LocatedNotForcedFiniteCore.lean",
            REPO_ROOT / "Lean/GUFormalization/R4TwoArena.lean",
            REPO_ROOT / "tests/located-not-forced/H2_FiniteCore.lean",
            REPO_ROOT / "tests/located-not-forced/V15_CodomainSeparatedFiniteCore.lean",
            REPO_ROOT / "tests/located-not-forced/V15_KreinTransversality.lean",
        }
    )
    for source in sorted(nested):
        copy_relative(source, PACKAGE)

    (PACKAGE / "SOURCE-COMMIT.txt").write_text(source_commit + "\n", encoding="utf-8")

    manifest = PACKAGE / "MANIFEST.sha256"
    entries = []
    for path in sorted(PACKAGE.rglob("*")):
        if path.is_file() and path.name not in {"MANIFEST.sha256"}:
            entries.append(f"{sha256(path)}  {path.relative_to(PACKAGE).as_posix()}")
    manifest.write_text("\n".join(entries) + "\n", encoding="utf-8")

    if ARCHIVE.exists():
        ARCHIVE.unlink()
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(PACKAGE.rglob("*")):
            if path.is_file():
                archive.write(path, Path("located-not-forced-v1.0.0") / path.relative_to(PACKAGE))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action",
        choices=("tex", "pdf", "package"),
        help="generate TeX, compile PDF, or build the complete package",
    )
    parser.add_argument("--source-commit", help="immutable source commit for package builds")
    args = parser.parse_args()

    render_tex()
    if args.action == "tex":
        return 0
    pdf = compile_pdf()
    if args.action == "package":
        if not args.source_commit:
            parser.error("--source-commit is required for package")
        build_package(pdf, args.source_commit)
    return 0


if __name__ == "__main__":
    sys.exit(main())
