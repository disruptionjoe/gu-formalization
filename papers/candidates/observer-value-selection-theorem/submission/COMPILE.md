# Compile receipt

## Release artifact

- Source: `main.tex`
- PDF: `main.pdf`
- Compiler: Tectonic 0.16.9, Homebrew macOS arm64 release
- Compile date: 2026-07-13
- Pages: 7
- PDF SHA-256: `B516E5245C2FE55D010BCED2511BC6E79A9C051CA8EDD51591A31BCB5EE8B37D`

The release build completed with exit code 0. Tectonic automatically reran TeX to resolve cross-references. The final log contains no TeX errors, undefined references, undefined citations, or overfull boxes. The remaining underfull-box notices occur only in bibliography entries and do not indicate clipped or overlapping content.

All seven pages were rendered to PNG at 120 dpi and visually inspected. No clipping, overlap, missing glyphs, blank pages, or broken line wrapping was found. Text extraction found seven nonempty pages, no unresolved `??`, and no author placeholder. PDF metadata contains the title, author, subject, and keywords.

## Recompile

Tectonic:

```text
tectonic main.tex
```

Or with a standard TeX distribution:

```text
pdflatex main.tex
pdflatex main.tex
```

No BibTeX run is needed because the bibliography is inline. The document uses the `article` class plus `fontenc`, `geometry`, AMS packages, and `hyperref`.

## Release identity

The paper identifies Joe Hernandez as an Independent Researcher and includes `joe@disruptionjoe.com`. No ORCID is asserted. The absence of an ORCID is intentional and is not a placeholder.
