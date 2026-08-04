---
artifact_type: exploration
status: exploration
doc_type: deciding-check-result
created: 2026-08-04
lane: "1"
work_item: DC-H2-RECIPROCITY-AND-THE-ZU-BLOCK-RATIO
title: "DC-H2 executed: does reciprocity (self-adjointness of the source pairing under GU's own Krein/C structure) fix Z_U's (c_b : c_f) block ratio on the A3 configuration? VERDICT: outcome (c) FREE, with the only sharpening that could have bitten shown CIRCULAR. Reciprocity is satisfied identically on the whole (c_b : c_s : c_f) family; the condition is invariant under exactly the blockwise congruence group whose orbits ARE the block ratios. H2 is DEAD as filed and the BLOCKED-ON-A4 statement is CONFIRMED, not weakened."
grade: "EXACT RATIONAL CERTIFICATE / deciding check for a preregistered hypothesis / pre-deposit, J5-gated. Script tests/de-certification/dch2_reciprocity_and_zu_block_ratio.py, 35/35, exit 0, hard asserts with exit coupling, no float on any asserted claim (P-H29 satisfied by construction). Nothing here moves a claim, canon entry, verdict, bar, H59, the count, LANE-STATE, or any fork. The three by-products (a 3-to-1 reduction of the A4 residue; the residue's type as a LENGTH; one VERIFIED_REPO_DISCONNECT between W230's text and W203 KER4) are reported to the register owner, not edited in."
source: "DC-H2 as preregistered in explorations/atlas-derived-external-datum-hypotheses-2026-08-04.md (outcomes FROZEN there, not refitted here); Joe-authorized 2026-08-04."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
kill_conditions_declared_before_computation: true
depends_on:
  - explorations/atlas-derived-external-datum-hypotheses-2026-08-04.md
  - explorations/de-certification-redo-2026-08-03.md
  - explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md
  - explorations/W230-close-a4-derive-w154-2026-07-14.md
  - explorations/unified-source-datum-packet-v0-2026-07-30.md
  - explorations/geometry-curvature-emergence/ii-s-coordinate-formula-2026-06-23.md
  - explorations/gimmel-dewitt-normalization-ledger-2026-07-20.md
  - canon/theta-field-flrw-dark-energy-eos.md
  - lab/process/agent-context-pack.md
scripts:
  - tests/de-certification/dch2_reciprocity_and_zu_block_ratio.py
---

# DC-H2: reciprocity and Z_U's block ratio

H2 (filed 2026-08-04) proposed that the `(c_b : c_f)` block ratio of the
native kinetic term `Z_U = |D_A U|^2` -- the decisive unbuilt object at the
A4 NORM arrow of the W230-to-FLRW composition -- is **fixed by requiring the
source pairing to be reciprocal / self-adjoint**, rather than being
independent data. Its preregistered outcomes are frozen in that file:
(a) uniquely fixed, (b) fixed up to a discrete choice, (c) free.

**Verdict: (c) FREE**, and the only version of the check sharp enough to have
constrained the ratio is **CIRCULAR** in the precise sense set out in Section
5. H2 is dead as filed. The BLOCKED-ON-A4 statement is **confirmed and
strengthened**, not weakened: DC-H2 does not merely fail to unblock A4, it
proves that an entire *class* of conditions cannot unblock it.

## 0. Layer-0 typing (before use; the standing rule)

| Term | Type | Ruling for this artifact |
|---|---|---|
| "the pairing" | **DEFINED HERE, GU-internal** | `<alpha, beta> := int_Y kappa_g(alpha, *_G beta)`: the invariant adjoint pairing `kappa_g` on the internal/frame index, contracted with the Hodge star `*_G` of the gimmel metric `G` on `Y14` on the form index. This is the repo's own written pairing (`unified-source-datum-packet-v0-2026-07-30.md`, which uses the SAME `*_G` in the source coupling `kappa_g(theta, *_G J(Z))` and in the gradient term `kappa_g(P_IG, *_G D_A U)`). **No graphics/neutronics object is imported.** The atlas motivated the question; it licenses nothing. |
| "reciprocity" | **DEFINED HERE (two readings, both run)** | (R1) symmetry of the pairing: `<alpha, beta> = <beta, alpha>`. (R2) self-adjointness of the kinetic operator with respect to that pairing: `<alpha, L beta> = <L alpha, beta>`. Both are run; both are shown blind to the ratio. A third reading (the same `G` must serve pairing, measure and adjoint) is run in Section 6 as the by-product it actually earns. |
| `Z_U` | **HOMONYM (flagged, does not affect the verdict)** | In W203's coefficient ledger `Z_U` names the whole gradient term `\|D_A U\|^2` (row: **NOT BUILT**). In W229 / the recovery-contract fingerprint / the source-datum packet, `Z_U` names the scalar coefficient multiplying it (`Z_U magnitude: normalization_unbuilt`). DC-H2 concerns the ledger sense (the block split), and both senses agree that the object carrying the split is unbuilt. |
| `U` vs `theta` | **IDENTIFICATION, carried not adjudicated** | The packet writes the gradient sector for `U` (`P_IG = Z_U D_A U`); the recovery-contract source law writes `(-Z_U D_A*D_A + c_theta eta) theta = J[Psi]`. The step from one to the other is an identification made upstream, not here. It does not enter any computation below. |
| `(c_b : c_s : c_f)` | **DEFINED (de-certification-redo A4)** | The block coefficients of the kinetic form along the A2/A3 splitting (base-time / base-space / fibre) on the configuration `theta = B(t) Y_1(y)`. |
| "external datum" | **NOT ASSERTED** | Nothing here types anything as an external datum or moves the external ledger. Section 6 reports what *type* of object the A4 residue is; typing is not counting. |

Construction fork (`GEOMETER-VS-PHYSICS-OBJECTS.md`): every object below is
program-native (`Y14`, the gimmel metric `Gcal`, the `(9,5)` frame and its
`(3,1)+(6,4)` split, `kappa_g`, `eta`, `theta`, `J[Psi]`, the fibre normal
Laplacian). The machinery is standard linear algebra that binds any
construction (Schur's lemma; congruence invariance of symmetric forms;
homogeneity degrees). Hygiene: `git status` checked first; nothing under
`tests/channel-swings/pw2*` or the interior campaign's files is touched;
nothing is committed by this agent.

## 1. What "the pairing" is, in GU's own objects (stated up front)

The brief's discipline clause requires this before anything else.

GU's source action pairs a source with a field through one object, written
explicitly in the source-datum packet:

```
S  ...  + int_Y [ kappa_g(P_IG, *_G D_A U) - (1/(2 Z_U)) kappa_g(P_IG, *_G P_IG) ]
       + (1/(2 kappa)) int_Y kappa_g(theta, *_G theta)
       - int_Y kappa_g(theta, *_G J(Z))
```

Two independent structures meet in `kappa_g(., *_G .)`:

- **`kappa_g`**, the invariant pairing on the internal/frame index. This is
  **already forced** and was forced before H2 was written: W203 KER1/KER3
  (reproduced here independently over `Fraction`s as RES1/RES2) show that the
  space of `so(9,5)`-equivariant symmetric kernels on the 14-frame is exactly
  one-dimensional and is generated by the Clifford metric `eta`.
- **`*_G`**, the Hodge star of the gimmel metric `G` on `Y14`. This is the
  factor that contracts the *derivative* index, and it is where a block ratio
  can live at all.

So the honest reading of "the source pairing" is: the internal half is
Schur-forced and carries no free ratio; the form half is `G`, and
`(c_b : c_s : c_f)` **is** `G`'s block structure along the A3 splitting.
That identification is what makes the rest of the check decidable -- and, as
Section 5 shows, also what makes its sharp version circular.

## 2. Preregistration honored

H2's outcomes (a)/(b)/(c) are quoted from the frozen file and machine-tied
(REPO10): a drift in that text fails the script. No outcome was added,
narrowed, or reweighted. The script's decision procedure was fixed before the
computations: impose each reading of reciprocity on the candidate pairing at
the A3 splitting, and report whether the constraint set is a point, a finite
set, or a positive-dimensional family.

## 3. What was computed

`tests/de-certification/dch2_reciprocity_and_zu_block_ratio.py`, 35/35, exit 0,
exact rational arithmetic throughout (`fractions.Fraction`); every decisive
statement is an exact zero or an exact nonzero, never a tolerance.

**[REPO] 11 artifact-text ties.** W203's `Z_U` NOT-BUILT row; W203 KER1 and
KER4; the de-certification ledger's FIRST UNBUILDABLE ARROW and its naming of
`(c_b : c_f)` on the A3 configuration; the gimmel metric's written block form
and its `(3,1)`/`(6,4)` signatures; `lambda_GU = 1/2`; the packet's shared
`*_G`; W230's Gram sentence; H2's frozen outcomes; the canon's `M_KK` line
with `R_s = c/H_0`. Silent drift in any of these fails the run.

**[PAIR] reciprocity reading R1 is an identity.** The residual
`<theta, J> - <J, theta>` is **exactly zero at every block ratio tested**, and
exactly zero for an arbitrary symmetric `G` with no block structure at all
(PAIR1/PAIR2). Positive control: a pairing with a nonzero antisymmetric part
is detected with an exactly nonzero residual (PAIR3), so the instrument is not
vacuous. Structural reason, stated plainly: the source coupling is **linear**
in `theta`, and a block ratio is a property of a **quadratic** form. R1 has no
place to carry `(c_b : c_f)`.

**[SA] reciprocity reading R2 is blind to the ratio, provably.** For any
metric `G` and any form `Q`, `G (G^{-1} Q) = Q` identically, so
`G`-self-adjointness of `L = G^{-1} Q` is **equivalent to `Q = Q^T`** -- a
condition in which `G`, and hence the block ratio, does not appear (SA2). The
residual is exactly zero across the sampled `(c_b, c_s, c_f)` grid (SA1); a
non-symmetric `Q` is detected (SA3, non-vacuity). Decisively: the reciprocity
condition is **exactly invariant under the blockwise congruence group**
`Q -> S^T Q S` with `S` block-diagonal (SA4), and that group **moves the
ratio** (SA5: `c_f/c_b : 1 -> 25/36` on the declared fixture). A condition
invariant under a group cannot fix a coordinate on that group's orbits, and
the block ratios *are* those orbits.

**[RES] exactly how much freedom the A3 configuration leaves.** Exact
nullities of the equivariance constraint on symmetric 14-frame kernels:

| symmetry imposed | nulldim | reading |
|---|---:|---|
| full `so(9,5)` | **1** | W203 KER1 reproduced independently; generator is `eta` (RES2) |
| block-preserving `so(3,1) + so(6,4)` | **2** | one scale per block; the most the A2/A3 split can retain |
| FLRW-adapted `so(3) + so(6,4)` | **3** | exactly `(c_b, c_s, c_f)`, and no more |

This is a small new result in its own right: the three A4 coefficients are
**precisely** the invariants of the A3 configuration's residual symmetry --
there are three, not two and not four. Reciprocity adds **zero** constraints
on top (RES5): it is already satisfied on all of it.

**[SCALE] the residue is a LENGTH, not a number.** Under the fibre dilation
`h -> c h` the gimmel metric's vertical block `V_h` is homogeneous of degree
`-2` with the fibre vector held fixed and degree `0` with it transported along
the ray, while the horizontal block `h(u,v)` is degree `+1` (SCALE1/SCALE2).
The horizontal:vertical ratio therefore changes by exactly `c` (SCALE3): the
written `Gcal((u,k),(v,l)) = h(u,v) + V_h(k,l)` has unit relative coefficient
only *in the chart's units*, and one length-squared is hidden in it. The
ledger's own native pure-trace values (`-4` at `lambda_GU = 1/2`, `-12` at the
DeWitt comparison `lambda = 1`) are reproduced exactly as a control (SCALE0).
The consequence is quantitative: on the A3 configuration at `k = 0`,
`M^2 = (c_f/c_b) lambda_{N,1}` with `(c_f/c_b) = N^2/ell^2`, so `ell = R_s`
gives exactly `M^2 = 8` (canon's `M_KK = 2 sqrt(2) H_0`) while `ell = 2 R_s`
gives `2` and `ell = R_s/2` gives `32` (SCALE4) -- continuously, with no
discrete structure anywhere. Outcome (b) is therefore excluded by the same
computation that excludes (a).

**[COST] the strongest opposite reading, and its price.** See Section 4.

**[CIRC] the circularity ledger.** See Section 5.

## 4. Two-sidedness: the strongest case for the opposite reading

The strongest case that H2 survives is **not** a better reciprocity argument;
it is the observation that a *neighbouring* condition does exactly what H2
wanted. Demand full `so(9,5)` equivariance of the kinetic kernel, not merely
reciprocity. By RES1 that is a uniqueness theorem: the kernel must be
proportional to `eta`, so `(c_b : c_s : c_f)` is forced to `eta`'s own block
ratio and the A4 arrow would close by derivation. Someone wanting H2 to live
would move here, and would be entitled to point out that GU's whole
coefficient-pinning practice (W203) is exactly this move.

**That reading is available, and it is expensive.** Computed exactly (COST1):
if `L` is proportional to `M` -- which is what full equivariance forces, given
that W203 already forces `M ~ eta` by the same Schur argument -- then
`theta(c_kin) = (m^2 M + c_kin L)^{-1} kappa J` stays **exactly parallel** to
`M^{-1} J` for every `c_kin` tested (`0, 1/10, 1, 10, 100`). That is precisely
W230 `[NEC]`'s escape variety, and it destroys the **necessity** half of W230:
"a kinetic term present breaks the identity" becomes false, and with it the
`theta = J <=> c_kin = 0` equivalence on which the A4 lane's COMPLETED-POSIT
verdict rests. The contrast control (COST2) reproduces W230's own result: with
`L` symmetric and *not* proportional to `M`, alignment is exact at `c_kin = 0`
and fails for every `c_kin > 0`.

So the two readings are in tension and cannot both be banked:

- Take equivariance to fix the ratio, and W230's necessity leg goes.
- Keep W230's necessity leg (which requires `L` **not** proportional to `M`),
  and equivariance is *already given up* -- at which point RES3/RES4 say the
  surviving symmetry leaves a 2- or 3-parameter family, and reciprocity, by
  SA1-SA5, cuts none of it.

W230's own text takes the second horn (its `L` is "not proportional to `M`").
That is the live posture, and on it H2's outcome is (c) with no residue.

A second, weaker opposite reading deserves recording: one could ask whether
Krein/C-positivity of the record current (W203 SGN3) constrains the ratio.
It cannot yield (a) or (b) either -- cone-preservation conditions cut out
open regions, not points or finite sets -- and SCALE4 shows the observable
`M^2` varies continuously with the same un-derived scale. This is stated as a
structural expectation, not computed here, and is the honest weakest link in
this artifact's coverage.

## 5. The circularity, named precisely

The brief anticipated this outcome and it is real. The ledger, as asserted in
the script (CIRC1):

| object | status |
|---|---|
| the pairing that must be reciprocal | `int_Y kappa_g(., *_G .)` -- GU-internal, no import |
| what fixes `kappa_g` | Schur on the frame's vector rep; already forced (W203 KER1 = RES1/RES2) |
| what fixes `*_G` | the gimmel metric `G` on `Y14`, block-diagonal `h(u,v) + V_h(k,l)` |
| what `(c_b : c_f)` IS | the horizontal:vertical relative scale of that same `G` |
| what reciprocity constrains | the SYMMETRY of the form, `Q = Q^T`; `G` does not appear |
| **the circularity** | to state a reciprocity condition sharp enough to constrain the ratio, one must first fix the pairing with respect to which adjoints are taken -- i.e. fix `G`'s horizontal:vertical scale -- which **is** the missing A4 object |

Stated as a dichotomy: the version of DC-H2 that does not presuppose its own
answer is an **identity** (PAIR1, SA1: satisfied on the whole family); the
version sharp enough to bite **presupposes the missing object**. Both halves
are full-value negative results, and together they are stronger than either:
they show that no condition of this *type* -- any condition invariant under
blockwise congruence, which includes every symmetry-of-the-pairing and every
self-adjointness demand -- can ever supply `(c_b : c_f)`. What A4 needs is a
**scale**, and scale-blindness is exactly the defining property of the
conditions H2 proposed.

## 6. By-products (reported, not claimed as a fix)

Three things the check earned on the way, none of which rescue H2.

1. **The A4 residue reduces from three coefficients to one scale.** Because
   the SAME `*_G` contracts both the source coupling and the gradient term
   (REPO8), the three coefficients are not three independent data: `c_b` and
   `c_s` are two components of ONE horizontal block (`Gcal_{mu nu} = h_{mu nu}`,
   with the FLRW lapse and scale factor supplying their relation), and `c_f`
   is the vertical block. The residue is exactly **one number**: the
   horizontal:vertical relative scale. This slightly sharpens the
   de-certification ledger's framing (three coefficients) without contradicting
   it, and it is the one genuinely positive thing the reciprocity demand does.
2. **That one number is dimensionful.** SCALE1-SCALE3: it is a length-squared
   (the fibre radius in base units), not a pure number. The only value it has
   anywhere in the repo comes from the canon's `R_s = c/H_0` -- an
   observational identification, carried at reconstruction grade. H44's
   equation is therefore the choice `(c_b : c_f) = 1 : 1` **together with**
   that import (SCALE5); neither factor is derived, and nothing in DC-H2
   certifies either. This is reported to the register owner as a typing
   observation about an already-known residue. It is **not** a new external
   datum claim, and the external ledger is not touched.
3. **One VERIFIED_REPO_DISCONNECT.** W230's text calls W180's Frobenius Gram
   "the fixed equivariant ultralocal Krein kernel", while W203 KER4 proves the
   Gram is NOT equivariant -- reproduced here exactly (COST3: 3 of 13
   consecutive `so(9,5)` generators violate it). W230 is downstream of W203 and
   depends on it. This does not change W230's `[NEC]` conclusion, whose stated
   sufficient hypotheses are only that `L` be SPD and not proportional to `M`,
   but the label "equivariant" on the Gram is wrong and should not be carried
   forward. Reported, not repaired.

## 7. Disposition

**Citable from this artifact:**

1. **DC-H2 outcome (c): FREE.** Reciprocity, in either reading, is satisfied
   identically on the whole `(c_b : c_s : c_f)` family and is exactly
   invariant under the group whose orbits are the block ratios. It fixes the
   ratio neither uniquely nor up to a discrete choice.
2. **H2 is DEAD as filed**, per its own frozen preregistration.
3. **BLOCKED-ON-A4 is CONFIRMED and strengthened.** The blocker is not merely
   still there; an entire class of candidate unblockers is now excluded by an
   exact argument, so future A4 work should not be spent on symmetry- or
   adjointness-type conditions. What A4 needs is a scale.
4. **The A4 residue is exactly one dimensionful number** (the gimmel metric's
   horizontal:vertical scale), not three coefficients.
5. The `so(9,5)` / `so(3,1)+so(6,4)` / `so(3)+so(6,4)` nullities 1 / 2 / 3.

**Not citable / unchanged:** anything about the value of `(c_b : c_f)`; any
movement of M-H13 item (a) (it stays BLOCKED-ON-A4 -- DC-H2's outcome (a) was
the only branch that would have moved it, and it did not fire); the native
record law; C10 or M-H13 register status (register-owned); the `c_kin = 0`
posit's status; the count, H59, any bar, LANE-STATE, or any fork. No external
datum is selected, consumed, typed into the ledger, or changed.

**REPORT to the register owner (no edits made here):** DC-H2 returns (c). The
de-certification ledger's report line -- "item (a) ... is sharpened from
uncertain tension to BLOCKED-ON-A4 with the decisive object named" -- stands
unchanged, with two refinements available: the decisive object is one scale
rather than a three-way split, and the class of conditions that cannot supply
it is now characterized. Separately, the W230-vs-W203 "equivariant Gram"
disconnect (Section 6.3) is offered for the improvement register.

*Filed 2026-08-04. Deciding check for a preregistered hypothesis; outcomes were
frozen before computation and are not refitted. Reproducible:
`PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python -u
tests/de-certification/dch2_reciprocity_and_zu_block_ratio.py` (35/35, exit 0).
Pre-deposit, J5-gated; exploration grade; no canon, claim, verdict, bar, count,
H59, or LANE-STATE movement. The atlas motivated this check; it licensed
nothing, and no graphics/neutronics object appears in any computation.*
