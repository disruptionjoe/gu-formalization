# Release verification — 2026-07-13

Paper: *A Diagonal No-Go for Self-Valuations and an Invariance Classification*

This receipt applies only to the source, PDF, Lean declarations, and dedicated finite check named below. It does not certify the wider GU research repository.

## Mathematical scope audit

The release is a theorem in **Set**. For sets `A` and `B`, a map `T : A × A -> B`, and a fixed-point-free `alpha : B -> B`, it proves pointwise that `d_T(x) = alpha(T(x,x))` differs from every row of `T`; consequently, `T` is not weakly point-surjective. If `A` is nonempty, it separately proves that no `p : A -> B` is pointwise `alpha`-invariant.

The group-action section classifies a valuation as invariant exactly when its image lies in the common fixed-point set. It is an invariance classification, not a selection, forcing, commitment, dynamics, or decidability theorem.

The release explicitly excludes:

- any theorem in an arbitrary category;
- any physical or operator-algebra realization;
- any physical selection mechanism or empirical prediction;
- any canonical residual, preferred valuation, numerical constant, or generation count;
- any claim that the full paper or interpretive group-action section is formalized;
- any claim that the diagonal or invariance ingredients are themselves novel.

The identity and three-grade controls were checked specifically to prevent two invalid inferences:

1. representing one twisted diagonal is not the same as weak point-surjectivity;
2. a fixed grade defeats the fixed-point-free diagonal proof for that action, but does not defeat Cantor–Lawvere non-enumerability when the codomain has at least two elements.

## Lean 4 receipt

Toolchain: `leanprover/lean4:v4.32.0-rc1`, as pinned in `lean-toolchain`.

Command:

```text
lake env lean Lean/GUFormalization/ResidualSelection.lean
```

Result: **PASS**, exit 0, no output, no `sorry`.

The clean deposit package was also tested from an isolated copy with its minimal Lake configuration:

```text
lake -Kjobs=1 build +GUFormalization.ResidualSelection
```

Result: **PASS**. This target-specific command avoids building any broader repository module and is the recommended clean-package command.

Axiom command:

```text
lake env lean Lean/GUFormalization/ResidualSelectionAxioms.lean
```

Result: **PASS**, exit 0. Lean reported no axiom dependencies for:

- `residual_escapes`
- `lawvere_fixed_point`
- `no_closure`
- `no_invariant_valuation`
- `not_fixpoint_free`
- `gu_residual_not_row`
- `gu_no_closure`
- `gu_no_invariant_valuation`

The checked core is function-level over arbitrary Lean types. Its Boolean corollaries use `Bool` negation. The group-action classification, literature discussion, and interpretation are not represented as Lean declarations.

## Dedicated finite-instance receipt

Command:

```text
python tests/W99_theorem_finite_instances.py
```

Result: **PASS**, exit 0. The test exhaustively checked the stated small finite cases, including identity, singleton-codomain, fixed-middle-grade, and fixed-point-free three-cycle controls. This is confirmation only; the proof does not depend on it.

Historical repository tests `W70_path5_D_lawvere.py` and `W73_H62_arena_value_partition.py` also exited 0 during regression checking. They predate this paper, contain broader GU interpretation, and are deliberately excluded from the paper's evidence and deposit package.

## Source and bibliography checks

- Abstract length: 178 words.
- Labels: 16; every reference target exists.
- Bibliography keys: 16; every citation resolves and every bibliography item is cited.
- TeX environment nesting and raw brace balance: valid.
- Author placeholder scan: clear.
- Overclaim scan: the only uses of “force,” “commit,” and “selection” occur in limitations, interpretive disclaimers, or cited titles.

Bibliographic metadata was checked on 2026-07-13 against publisher, journal, author-archive, DOI, or authoritative index records. Verified DOI-bearing entries include Lawvere (`10.1007/BFb0080769`), Kochen–Specker (`10.1512/iumj.1968.17.17004`), Bell (`10.1103/RevModPhys.38.447`), Abramsky–Brandenburger (`10.1088/1367-2630/13/11/113036`), Conway–Kochen (`10.1007/s10701-006-9068-6`), Curie (`10.1051/jphystap:018940030039300`), Earman (`10.1080/0269859042000311299`), Norton (`10.1086/687934`), Breuer (`10.1086/289852`), Szangolies (`10.1007/s10701-018-0221-9`), Abramsky–Zvesper (`10.1016/j.jcss.2014.12.001`), Frauchiger–Renner (`10.1038/s41467-018-05739-8`), and Brukner (`10.3390/e20050350`). The Lawrence preprint identifier was checked as `arXiv:2604.21945`.

The Bell/Kochen–Specker paragraph now distinguishes Bell's Gleason-based route from finite noncolorability constructions and does not describe Bell 1966 as adding a locality assumption.

## PDF receipt

- Compiler: Tectonic 0.16.9, Homebrew macOS arm64 release.
- Result: **PASS**, exit 0, automatic rerun completed.
- Pages: 7, all nonempty by text extraction.
- Final log: no TeX errors, unresolved references, unresolved citations, or overfull boxes.
- Remaining warnings: bibliography-only underfull boxes.
- Visual QA: all seven pages rendered at 120 dpi and inspected; no clipping, overlap, missing glyphs, blank pages, or layout defects.
- PDF metadata: title, author, subject, and keywords present.
- Placeholder scan: no unresolved `??`, `JOE:` marker, or missing-affiliation text.

## SHA-256 source receipt

```text
877A967C22A895BF87071AD593DE33D45A947BB4A3900A91C9597F17E0DC911C  submission/main.tex
B516E5245C2FE55D010BCED2511BC6E79A9C051CA8EDD51591A31BCB5EE8B37D  submission/main.pdf
568FCF13F940FEBB85082277B4C466727BF3A7D50A55D41A7FB277C57F4A966B  submission/reproduction.md
C2D2B87DC390AC354F4ECDA4B16201930518589B821A4C5EAEFDDBE35141988B  observer-value-selection-theorem-2026-07-11.md
D5B25E99E1A3E745DAA4C0224F6EA91039B464A2F5A9331001E22667BCACCA37  Lean/GUFormalization/ResidualSelection.lean
270EC2EE125A3D08C94A8C75BEF7649E5C87E3DEC7D0E1C626CAA98D2894CB48  Lean/GUFormalization/ResidualSelectionAxioms.lean
C459F4B4574DEA9C72D5C5174C25F282801A43273A874C1D8FBD8970D6BDAD48  tests/W99_theorem_finite_instances.py
72681913B978B3F7C2F48229836771F736F6E97D833917726B2263AFBC6108ED  lean-toolchain
```

The PDF hash supersedes the earlier candidate PDF. The LaTeX file is the release source of record.
