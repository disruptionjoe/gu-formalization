# Compile status and instructions

**Status (honest):** `main.tex` has NOT been compiled to PDF on this machine -- no TeX toolchain is installed (checked: pdflatex, xelatex, latexmk, tectonic, MiKTeX, TeX Live; none present). The file was verified by static checks instead: balanced environments and braces, matched math delimiters, all `\ref` targets labelled, all `\cite` keys present in the bibliography, no exotic packages (only geometry, amsmath, amssymb, amsthm).

## To compile

Any of the following will work; the document is plain `article` class with AMS packages only.

**Option A -- tectonic (single binary, no TeX install):**
```
tectonic main.tex
```

**Option B -- a standard TeX distribution (MiKTeX or TeX Live):**
```
pdflatex main.tex
pdflatex main.tex
```
(Run twice so `\ref` cross-references resolve. No bibtex run is needed -- the bibliography is inline `thebibliography`.)

**Option C -- Overleaf:** upload `main.tex` as the only file of a new project and click Recompile. Default compiler (pdfLaTeX) is fine.

## Expected warnings

- First pass only: undefined references (resolved on the second pass).
- No errors are expected. If a font/encoding warning appears for the accented characters in the bibliography (Gödel, symétrie), it is harmless under pdfLaTeX's default OT1/T1 handling; adding `\usepackage[T1]{fontenc}` silences it.

## Before posting (the %% JOE marker)

`main.tex` contains one placeholder: the `\thanks{}` on the author line, marked `%% JOE: fill in email and affiliation`. Replace "Email and affiliation to be added." with your email and affiliation (or an independent-researcher line) before submitting anywhere.
