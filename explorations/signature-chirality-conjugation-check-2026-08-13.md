---
title: "Signature-dependence of chirality: conjugation flips in Lorentzian, preserves in Euclidean"
status: active_research
doc_type: construction_result
created: 2026-08-13
brief_version: "1.3"
target_claim: NONE-NOT-A-KILL
ledger_rows: [AC-F1, RA-D2, AC-A4, RA-A2, RA-A3]
source_claims: [SC-CHI-01, SC-CHI-50]
canon_verdict_change: none
probe: tests/channel-swings/signature_chirality_conjugation_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `SOURCE_NATIVE_ROUTE`.

# Signature-dependence of chirality

Joe-directed (direct chat, 2026-08-13). Two hypotheses were posed about
whether GU's asserted chirality EMERGENCE has a representation-theoretic
rather than dynamical source. One is confirmed by exact computation; one
is refuted, informatively, by two independent routes.

## H2 — CONFIRMED (exact, this artifact's probe)

**Antilinear conjugation FLIPS chirality in Lorentzian signature and
PRESERVES it in Euclidean signature.**

| signature | `gamma5` normalisation | conjugation acts on chirality |
|---|---|---|
| `Cl(1,3)` | `i * g0g1g2g3` (IMAGINARY) | **FLIPS** |
| `Cl(4,0)` | `g0g1g2g3` (REAL) | **PRESERVES** |

Both admissible conjugation families agree within each signature; the
computation is exact over Gaussian integers on explicit 4x4 gammas with
Clifford relations verified.

**The mechanism is the normalisation.** `gamma5` needs an imaginary
factor in Lorentzian and none in Euclidean; that factor is what changes
sign under conjugation. Equivalently: in Euclidean, `S+` and `S-` are
independent pseudoreal representations with no natural map between them;
in Lorentzian they are complex conjugates of one another.

**Consequence for GU.** A construction that is genuinely VECTORLIKE with
respect to one real form can be genuinely CHIRAL with respect to another,
with NO dynamical input. This is a candidate mechanism for **AC-F1**
(`NEEDS/MISSING_CONSTRUCTION`, "observed four-dimensional chirality
emerges from a balanced bulk") that does not rely on **RA-D2**, whose
stated VEV/mass chirality mechanism is adjudicated
`OVER_DETERMINED/GENUINE_FALSIFICATION`. It is consistent with **AC-A4**
(`SAME/DERIVED`, bulk chirality zero) rather than in tension with it.

**Grade: the signature fact is CONFIRMED and is standard representation
theory** (its novelty is zero; the novelty claimed here is only its
CONNECTION to AC-F1). Whether GU's reduction actually changes real form
in the required way is **PROPOSED and untested** — that is the wave's
question, not this artifact's claim.

## H1 — REFUTED (two independent routes)

Proposed: GU's three open selections — the four-plane, the clock
direction, and `J` from the 20-dimensional family — might be ONE twistor
datum. They are not.

**Route 1 (this probe).** An orthogonal complex structure on `R^(p,q)`
(`J^2 = -I`, `J^T eta J = eta`) exists iff `p` and `q` are BOTH EVEN.
Verified with explicit witnesses:

| space | orthogonal `J` |
|---|---|
| `R^(4,0)` | EXISTS (witness verified) |
| `R^(6,4)` | EXISTS (witness verified) |
| `R^(2,2)` | EXISTS (witness verified) |
| `R^(1,3)` | **NONE** (both odd) |
| `R^(7,7)` | **NONE** (both odd) |

So the twistor sphere does not exist on the observed Lorentzian
four-plane, nor on the ambient.

**Route 2 (independent source reading).** In Woit's construction a
complex structure selects `U(2) subset SO(4)` — it does NOT select a time
direction; `J` and the time-selector are independent data.

**The useful residue.** `O(6,4)/U(3,2)` IS a twistor-type space — on the
FIBRE. So GU's `J`-selection is a fibre-side twistor problem while the
clock direction is a base-side problem where no such structure exists.
**They are structurally different and must not be investigated as one
datum** — the same lesson the sibling-repo reassessment reached from the
continuous/discrete factorisation.

## LAYER-0 WARNING (the error this artifact was written around)

"Complex structure" is a homonym across three objects here:
1. an orthogonal `J` on a VECTOR space `R^(p,q)` — the twistor object;
2. the `J` certified in `explorations/c3prime-split-commutant-certificates-2026-08-12.md`,
   which acts on the SPINOR space `R^128`, not on `R^(7,7)`;
3. Woit's `J` selecting `U(2) subset SO(4)`.
Conflating (1) and (2) is what produced H1. Do not repeat it.

## Verify manifest

- H2 table, both signatures: **CONFIRMED** (exact probe, this artifact).
- `p,q` both-even criterion and witnesses: **CONFIRMED** (exact probe).
- H2's applicability to GU's actual reduction: **PROPOSED**.
- H1 refutation: **CONFIRMED** by two independent routes.
- Correction of record: an earlier run of this probe used
  `omega = g0g1g2g3` (`omega^2 = -I` in `(1,3)`), which is not the
  chirality operator; the H2 leg of that run was invalid and is
  superseded here. Recorded rather than silently fixed.

## Three-charge self-review

**Charge 1 — summary outruns artifact.** The signature fact is textbook;
nothing here is a new theorem. The only new content is the proposed
connection to AC-F1, which is PROPOSED and untested. Any reading of this
as "chirality emergence is solved" outruns it badly.
**Charge 2 — mistyped object.** The homonym above is the live hazard and
is stated in its own section. `J`-on-spinors and `J`-on-vectors are
different objects; the c3prime certificate is untouched by H1's
refutation.
**Charge 3 — downstream.** dissolved: the naive one-datum reading of the
three selections. survives: c3prime's `+/-J10` uniqueness; AC-A4;
RA-D2's falsification. needs-recheck: whether GU's reduction changes real
form in the required way (the wave's question); whether the in-repo
`c(n): S+ -> S-` constructor (filed July 2026, closed "execute when a GU
packet exists") is the right instrument now that the clock gap asks for
exactly that variation.
