---
title: "Two-Sided Quadratic Energy in a Curved I1B Reconstruction"
status: draft
doc_type: overview
created: "2026-10-08"
updated_at: "2026-10-09"
target_claim: NONE-NOT-A-KILL
bears_on: [SC-ACT-06, SC-META-53]
canon_verdict_change: none
---

# Two-Sided Quadratic Energy in a Curved I1B Reconstruction

*Stationary backgrounds, constraint reduction, boundary compatibility, and
 the limits of positivity transfers*

[Read the 28-page PDF](article.pdf) ·
[Editable LaTeX](build/source/main.tex) · [Build receipt](build/receipt.json)

This unpublished research manuscript replaces the October 8 expository
technical note. It presents the selected curved I1B chain through the October 9
real compact-core theorem, including the prior boundary qualification,
imaginary energy proof, corrected flat controls, primary-source analysis,
and the separate quantum/PDE control sequence through K1600. The former
manuscript and its update file are preserved as exact verification-time
[snapshots](../../../lab/process/native-i1b-verification-history.json); they
are no longer parallel current sources.

The central result is two-sided unbounded **classical quadratic energy** on
both certified stationary coupling branches, in both real and imaginary
packets. The real witnesses have zero full metric forcing and satisfy every
finite-order formal compatibility condition of the declared boundary
polarization. The result concerns a selected reconstruction, compact phase
data and formal solution jets. It does not construct global evolution, a
source-selected physical quotient, an interacting quantum Hamiltonian, or a
universal GU no-go. A completion retaining the core and agreeing with its
quadratic energy inherits the obstruction.

Author attribution remains unassigned. This draft does not imply authorship
or endorsement by the people whose work it discusses. It remains in `drafts/`;
compilation is not publication readiness, independent analytic review or canon
promotion. LT-SM8 and LT-GR6b remain NEEDS, INHERITANCE_BRIDGE is undischarged,
and SC-META-53 remains UNCERTAIN.

## Manuscript and evidence

| Editable source | Contents |
| --- | --- |
| [Main file](build/source/main.tex) | Title, abstract, contents and typesetting |
| [Geometry and background](build/source/content.tex) | Exact action conventions, real structure, main theorem, canonical geometry and certified stationary branches |
| [Coupled reduction](build/source/reduction.tex) | Complete mixed operator, even and primary reductions, pure-base Hessian, raw boundary form and rank-five compatibility qualification |
| [Energy proofs](build/source/energy.tex) | Imaginary witnesses, observation non-descent, real reflection character, exact inverse coefficients, compact oscillations and all-order formal boundary compatibility |
| [Controls and source scope](build/source/controls.tex) | Positive pairing classification, flat corrections, Yang–Mills and Witten, scalar/composite donors, and separate cutoff quantum/PDE results |
| [Verification and appendices](build/source/verification.tex) | Evidence limits, exact algebraic branch, all sixteen local probes, five scoped Lean deductions and K1538–K1600 coverage |
| [Bibliography](build/source/references.bib) | Exact inspected primary versions and companion derivations |

The [research map](../../../explorations/nguyen-gu-critique/README.md) links
all scientific owners, receipts and executable checks. The
[corpus manifest](build/research-corpus.json) binds the manuscript sections to
those records and distinguishes substantive results from bookkeeping and
historical evidence. The
[integration receipt](../../../lab/process/native-i1b-corpus-integration.json)
records the successful sixteen-probe replay and named Lean build in the local
research history. The [verification-history index](../../../lab/process/native-i1b-verification-history.json)
preserves the historical text inputs needed by those receipts independently
of the original local commit identifiers.
Their finite computations support identified coefficients; analytic domain,
symmetry and locality arguments retain their separate proof obligations.

The two Clifford implementations are independent implementations of designated
finite calculations, not an outside review of the full theorem. The Lean
module proves only its five conditional deductions. Imported Witten and
other authors' results are credited to their sources; no literature-priority
claim is made here.

## Rebuild

Use Tectonic 0.17.0 with the versioned TeX Live bundle recorded in the
[typesetting receipt](build/receipt.json). With `tectonic` on `PATH`, run
from the repository root:

```bash
(
  set -e
  paper_dir="$PWD/papers/drafts/complex-gauge-unitarity"
  tex_scratch=$(mktemp -d)
  trap 'rm -rf -- "$tex_scratch"' EXIT
  cp "$paper_dir"/build/source/* "$tex_scratch/"
  cd "$tex_scratch"
  SOURCE_DATE_EPOCH=946684800 tectonic --untrusted --only-cached \
    --bundle https://data1.fullyjustified.net/tlextras-2022.0r0.tar \
    -Z deterministic-mode main.tex
  cp main.pdf "$paper_dir/article.pdf"
)
```

Omit `--only-cached` on the first build if the compiler's package cache has
not been populated. The seven LaTeX/BibTeX inputs are self-contained for
typesetting with those dependencies; no repository-specific builder is
required. The generated manuscript PDF is included as a review artifact.
The receipt also records a source ZIP from the earlier local build; that
archive is not needed for this rebuild or included in the contribution.
Exact mathematical reproduction uses the companion repository probes
listed in the manuscript and research map. Compilation does not certify
the analytic arguments or change the draft's publication stage.

## Scope routing

**GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
borders a conventional particle-physics comparator. Any result about a
standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
mass route binds only that named model. It is not evidence for or against
Weinstein's source-native mechanism without an explicit typed bridge. Read
`lab/methods/source-native-comparator-routing.md` and follow its source-native
pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`. This overview is outside the
routing audit's derived artifact scope. The manuscript keeps its selected
I1B action, flat surrogate, ordinary Yang–Mills, Chern–Simons, external scalar,
and repository quantum/PDE controls distinct.

```gu-typed-objects
result: selected curved I1B two-sided quadratic energy in both packets, with local stationary construction and formal boundary compatibility; separate comparator and transfer analysis
carrier: source-phased Clifford one-forms on the canonical metric bundle and a base metric; distinct comparator carriers explicitly declared LAYER=ambient+source-print+toy BRIDGE=declared_I1B_reconstruction_without_comparator_transfer CHIRALITY=N/A
pairing: scalar Clifford trace/Hodge action, reduced symplectic form and quadratic Noether energy; each comparator retains its own pairing ON=each_declared_carrier_and_domain
real_structure: source anti-involution slice and coefficient-conjugation packets; distinct reality conditions for imported models
grading: Clifford grade, time kernel, differential order and finite reflection character; no coefficient rank interpreted as a particle count
action_owner: source-action -- selected comm/symi/symi bosonic I1B; comparator -- separately named external and repository controls
target: quadratic energy on compact reduced phase cores and formal solution jets; physical observation, closed evolution and quantum completion remain open MAP-TYPE=restriction
```
