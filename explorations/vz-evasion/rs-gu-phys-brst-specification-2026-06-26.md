---
title: "RS_GU^phys: BRST Specification and Whether GU Determines the Generation-Count Structure"
date: "2026-06-26"
problem_label: "OQ-RK1 / RS_GU^phys-BRST"
status: exploration
doc_type: frontier_run_artifact
verdict: "BLOCKED_NEEDS_SPEC"
overall_origin: "genuine_gu_gap (with gu_derived skeleton + textbook-import frame)"
rank_H_Pi_E_Pi: "NOT_COMPUTABLE"
single_load_bearing_gap: "stabilized RS/IG-sector action (=> gauge-fixing slice, ghost count q, gamma-trace<->gauge reconciliation)"
gap_kind: "genuine incompleteness in GU-as-a-theory (NOT merely repo-unformalized)"
owned_path: "explorations/vz-evasion/rs-gu-phys-brst-specification-2026-06-26.md"
code:
  - "tests/rs_gu_phys_brst_specification.py"
reuses:
  - "tests/oq_rk1_e_rs_eff_assembly.py"
  - "tests/oq_rk1_cl95_explicit_rep.py"
  - "tests/rs_clifford_projector_model.py"
depends_on:
  - "explorations/generation-sector/oq-rk1-e-rs-eff-specification-2026-06-26.md"
  - "explorations/vz-evasion/af4-tau-rs-gauge-fixing-2026-06-23.md"
  - "explorations/hourly-cycles/hourly-20260625-0502-cycle2-author-manuscript-rs-differential-receipt-gate.md"
  - "explorations/hourly-cycles/hourly-20260626-1302-cycle3-tau-action-field-space-declaration-spec.md"
  - "canon/shiab-existence-cl95.md"
  - "lab/literature/weinstein-ucsd-2025-04-transcript.md"
---

# RS_GU^phys: BRST Specification and Whether GU Determines the Generation Count

## 0. The question and the one-line answer

Assemble `RS_GU^phys` from four justified sub-structure specs (RS gauge symmetry /
`d_RS,-1`; gauge-fixing condition; ghost/BRST complex; elliptic symbol / K-theory
class), then decide whether GU itself **determines** that structure well enough to
make the decisive quaternionic rank computable:

```text
rank_H( Pi_RS . E_+ . Pi_RS )   in M(64,H)      ( 4 => 3 generations, 8 => 4 )
```

**Answer. `RS_GU^phys` is NOT specifiable. The decisive rank is NOT computable
without fabricating the BRST data, which is refused. The BRST structure needed to
predict the generation count is NOT derived from GU's own tau+/inhomogeneous-gauge
source: GU fixes the gauge SYMMETRY, the field content, and that the RS sector is
the generation carrier, but it fixes neither a gauge-fixing slice, nor a stabilized
RS-sector action, nor the ghost-subtraction count `q`, nor the reconciliation of
its own gamma-trace irreducibility constraint with the gauge orbit. The general
spin-3/2 BRST apparatus is a textbook import; the GU-specific data that would make
it concrete is a genuine incompleteness in GU-as-a-theory. Verdict =
BLOCKED_NEEDS_SPEC; overall origin = genuine GU gap (over a gu_derived skeleton in
a textbook frame).**

## 1. Origin classification of the four pieces

Tags: `gu_derived` (fixed by GU's own source: transcript, tau+/IG, Cl(9,5)=M(64,H),
the action), `textbook_import` (standard for ANY spin-3/2 gauge theory, not
GU-specific), `genuine_gu_gap` (GU does not currently determine it).

| # | Piece | Specifiable | gu_derived part | genuine GU gap |
|---|---|---|---|---|
| C1 | RS gauge symmetry / `d_RS,-1` | partially | SHAPE + H-structure: `d_RS,-1 = d_A: Omega^0(/S)->Omega^1(/S)`, `eps |-> D_mu eps`, H-linear via the FORCED `Sp(64)=U(64,H)` connection | pure-RS projection / quotient semantics; an ACCEPTED spinorial differential (only eq 10.10, author-disclaimed); the action-forcing Noether identity |
| C2 | Gauge-fixing condition | **not** | the gauge SYMMETRY to be fixed (IG, SUSY-extended) | **GU picks NONE** ("without making any choices"); upstream the IG action field-space is unselected |
| C3 | Ghost/BRST complex | partially | skeleton + form-degree grading + H-structure (`C^{-1}->C^0->C^1`, ghost a quaternionic 0-form spinor, `d_A^2=0`) | the signed ghost multiplicities / net count `q=1-a`; gauge-fixing; gamma-trace<->`d_A` compatibility; ghost chirality |
| C4 | Elliptic symbol / K-class | partially | the FORM `E(q)=(V+q)F`, `ind_C=(-40+2q)n+(4+q)k`; raw endpoint `E_raw=(V+1)F` elliptic | the physical member `q`; `d_RS,-1`; ellipticity of the gauge-fixed complex; `k=ch_2(F)[K3]`; `Tr_H`; `Y14<->K3` bridge |

Only the **gauge symmetry, the field content, the H-structure, and the closed-form
index family** are GU-derived. Everything that converts the skeleton into a finite,
rank-computable `H^0` (the slice, the action, `q`, the reconciliation) is either a
textbook import in TYPE or a genuine GU gap in VALUE.

## 2. The single load-bearing gap (and why it is upstream of "compute q")

The four gaps collapse to **one** load-bearing object: a **stabilized RS/IG-sector
action**. The dependency is:

```text
stabilized action  =>  is zeta pure-gauge / dynamical / constrained?
                   =>  gauge-fixing slice (or BRST charge)  =>  ghost count q
                   =>  Pi_RS^phys  =>  rank_H(Pi_RS . E_+ . Pi_RS)
```

Without the action it is not even well-posed which fields are gauge and which are
physical, so "compute `q`" is premature. The repo has already established, against
GU's own primary source, that this object is absent:

- **GU's design philosophy is anti-gauge-fixing.** Transcript [00:49:16]: "you take
  the inhomogeneous gauge group on that group and you extend it through
  supersymmetry ... the entire universe **without making any choices**." Retaining
  the full IG as physical content is structurally opposite to picking a slice.
- **GU's 2021 draft was acquired and checked; it does not supply the rule.** The
  author-manuscript RS differential receipt gate
  (`hourly-20260625-0502-cycle2`) verdict: `QUARANTINED_UNDERDEFINED_ZERO_ACCEPTED_RS_RECEIPTS`
  — the manuscript "does not emit a source action, operator, differential, Noether
  identity, or BRST rule that identifies `source.action_or_operator for d_RS,-1`."
  The only candidate, the Section 10 deformation diagram (eq 10.10), is flagged by
  the author himself: "may contain some inconsistencies until it is stabilized.
  Caveat Emptor."
- **The tau-action field space is declared but uninhabited.**
  `hourly-20260626-1302-cycle3` verdict: "declaration uninhabited"; the trichotomy
  `FULL_IG_FREE_BETA / FIXED_ALEPH_GRAPH / DYNAMIC_A_GRAPH` is source-unselected.

## 3. The load-bearing machine fact, re-verified this run in BOTH models

If the pure-gauge image `im(d_A)` were annihilated inside the gamma-trace kernel,
then `R^phys = ker(Gamma)/im(gauge)` would be a clean subspace subtraction and **no
ghost complex would be needed** — the gap would be cosmetic. It is not. Code
`tests/rs_gu_phys_brst_specification.py` rebuilds the gamma-trace kernel projector
`P_+` and the constrained RS symbol, then evaluates the symbol on the projected
pure-gauge image `eps |-> P_+(xi tensor eps)`:

```text
Cl(4,0) x F=C^16 toy : RS symbol on pure-gauge image norm = 73.48   -> annihilated? False
Cl(9,5) = M(64,H) anc: RS symbol on pure-gauge image norm = 343.73  -> annihilated? False
```

The Cl(9,5) anchor check is **new this run** (prior runs only had the Cl(4,0) toy).
Both confirm: `im(d_A)` escapes `ker(Gamma)`. Therefore the physical RS space is
NOT a naive subtraction (that easy case is rigorously ruled out), and **some
nontrivial gauge-fixing apparatus is required** (the naive quotient is obstructed;
the machine fact rules out the easy subtraction but does not prove a ghost complex
is the *unique* resolution) — exactly the object GU does not provide. GU asserts an
"elliptic deformation complex after redundant EL equations are discarded" (draft
p.65) but never constructs it, and supplies no reconciliation of the gamma-trace
constraint with the gauge orbit.

## 4. The honest numbers (none is 4 or 8; 4/8 only via forbidden moves)

With `q` left symbolic and `k` unfixed, every honestly computable surrogate
(target-free):

| quantity | value | trace |
|---|---|---|
| `rank_H(E_+)` on `S=H^64` | 32 | verified |
| raw 14D gamma-trace kernel | 416_H | verified |
| Cl(4,0) `Pi_raw.E_+.Pi_raw` | 96_C = 48_H | verified |
| K3 `ind_H` flat `k=0`, `q=0/+1/-1` | -320 / -304 / -336 | conditional `Tr_H` |

None equals 4 or 8. The values 4 and 8 are reachable ONLY by inserting the desired
index `ind_H(D_RS):=8` (target import) or dividing it by the genus
`rank_eff := 8/Ahat(K3) = 8/2 = 4` (`INVALID_TARGET_DIVISION`). Both are documented
and **refused**. Note also that the symbol/K-theory route (large negatives) and the
af4 rep-theory route (claimed `ind_H(D_RS)=8`, itself only CONDITIONALLY_RESOLVED
with open conditions GF1-GF5 and never reconciled with the §3 obstruction) are
DIFFERENT objects that currently DISAGREE; neither is a GU-forced BRST output.

## 5. Is the gap a genuine incompleteness in GU, or merely repo-unformalized?

This is the decisive judgment. The gap is **layered**, and the load-bearing layer
is a genuine incompleteness in GU-as-a-theory:

- **Layer A — textbook-importable, NOT a genuine gap.** The general spin-3/2 BRST
  apparatus (ghosts, antighosts, Nielsen-Kallosh, a gauge slice) and the fact that
  BRST cohomology is slice-INDEPENDENT. If GU's action were fixed and its gauge
  symmetry were standard, importing any valid slice would close the computation.
  This layer is "not-yet-formalized in the repo," not a hole in GU.
- **Layer B — genuine GU gap.** Two GU-specific features block Layer A from
  closing:
  - **(B1) No stabilized action.** GU does not determine its own RS/IG-sector
    action. Eq 10.10 is author-disclaimed ("Caveat Emptor"); the 2021 draft emits
    no action/operator/differential/Noether/BRST rule for `d_RS,-1`; the field-space
    is unselected. Crucially this is sourced to GU's **own draft** being explicitly
    unstabilized by the author — not to the repo failing to do arithmetic.
  - **(B2) Constraint-vs-symmetry incompatibility.** GU's definitional gamma-trace
    irreducibility (`R = ker Gamma`) and the gauge symmetry are incompatible as a
    naive quotient (§3, machine-verified, norm `!= 0` in both models). GU asserts a
    reconciled elliptic complex but never constructs it; whether the reconciled
    complex is even elliptic is open.

So: the BRST FRAME is a textbook import (Layer A), the SKELETON/H-structure is
gu_derived, but the GU-specific DATA that selects the physical member — the action,
hence `q`, hence the reconciliation — is a **genuine incompleteness in GU-as-a-
theory**. It is not closable by repo formalization alone, because GU's primary
source has been read and does not contain it.

## 6. The exact object that would unblock

```text
RS_GU^phys = (
  STABILIZED RS/IG-sector action S_IG^susy            # the missing root object (B1)
    -> selects: zeta pure-gauge vs dynamical vs constrained
    -> EL/Noether identity delta_2 o d_RS,-1 = 0       # makes d_RS,-1 canonical (C1)
  reconciliation of gamma-trace R=ker(Gamma) with im(d_A)   # (B2), machine-obstructed
  gauge-fixing condition OR BRST charge (signs, degrees)    # (C2/C3)
  ghost-subtraction count a => q = 1 - a                    # (C3) selects E(q)
  sigma_RS^phys(xi) + ellipticity-of-complex certificate    # (C4)
  k = ch_2(F)[K3] ; global Tr_H ; Y14<->K3 bridge           # (C4) numeric closers
)
```

The first field whose absence halts everything is the **stabilized action**; it
cascades to the gauge slice, `q`, and the reconciliation. Supplying it (with a
genuine derivation, not analogy) would make the gate computable. Until then the
decisive `rank_H(Pi_RS . E_+ . Pi_RS)` is genuinely undetermined — the operator
`Pi_RS^phys` does not exist.

## 7. Fabrication self-check (FC4-HOLONOMY-01)

- No BRST/ghost structure was invented to hit rank 4 (3 gen) or rank 8 (4 gen). `q`
  was left FREE; building `Pi_RS^phys` would require choosing it — the refused step.
- The forbidden `8/Ahat(K3)=8/2=4` division and the `ind_H:=8` insertion are
  documented and never executed.
- The machine fact (`im(d_A)` not annihilated in `ker(Gamma)`, norms 73.48 and
  343.73) is reported as an obstruction that BLOCKS the convenient naive quotient —
  i.e. against the easy answer, not for it.
- The af4 "8" was NOT silently adopted; it is flagged as a different,
  conditionally-resolved rep-theory object that disagrees with the symbol route.
- The gu_derived skeleton is reported only at the level GU's source fixes it; the
  author's "Caveat Emptor" on eq 10.10 and the repo's zero-accepted-receipt status
  are preserved, not promoted. The honest deliverable is a precisely located gap.
