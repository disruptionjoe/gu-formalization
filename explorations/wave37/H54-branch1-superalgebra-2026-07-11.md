---
title: "H54 branch-1 -- Guardian superalgebra existence for GU's (9,5) / Sp(32,32;H) structure"
date: 2026-07-11
status: exploration
doc_type: exploration
wave: 37
verdict: "PARTIAL. A guardian super-extension EXISTS -- the symplectic-Majorana super-Poincare siso(9,5|N), N EVEN, USp(2N)_R, {Q,Q}=Omega^{ij}(C_- gamma^mu)_{ab} P_mu -- and it is precisely the gravitino-carrying algebra, so a supergravity guardian is ALGEBRAICALLY POSSIBLE. But it is NOT forced by GU's bosonic data: it requires ADDING a new boson/fermion Z/2 + odd generators + a USp(2N)_R that the Cartan involution P=beta_S and the chirality omega (both purely bosonic-sector) do not supply; the SIMPLE / super-CONFORMAL packaging is OBSTRUCTED (D=14 >> Nahm bound 6); and no unique N is singled out by GU's carrier-B. Existence of a super-Poincare is generic to signatures and is NOT 'GU is supergravity'."
test: tests/wave37/H54b1_superalgebra_existence.py   # deterministic, exit 0, 15/15 PASS
depends_on:
  - tests/wave13/H37_count_nogo.py            # the (9,5) J^2=-1 CII quaternionic structure
  - tests/oq_rk1_cl95_explicit_rep.py         # the verified Cl(9,5)=M(64,H) rep
  - explorations/wave8/H23-source-action-construction-2026-07-11.md   # beta_S Cartan involution, Sp(32,32;H)
  - explorations/wave34/source-action-landscape-scan-2026-07-11.md    # the guardian requirement (Rahman cutoff)
blind_to: [branches 2,3,4,5]
---

# H54 branch-1 -- Does GU's (9,5)/Sp(32,32;H) admit a guardian superalgebra?

**Discipline.** Every positive rep-theory claim below is an EXACT matrix identity on the verified
Cl(9,5)=M(64,H) 128-dim complex representation (residuals `0.0e+00`) or an explicit dimension count.
Nothing imported. The two ARGUED legs (Nahm bound, "existence != realization") are flagged. A NO would
have been as valuable as a YES; the honest outcome is **PARTIAL, with the obstruction on the
super-CONFORMAL / uniqueness side, not on super-Poincare existence.**

## The five personas, inline (compressed)

**(1) Lie-superalgebra / Kac theorist.** The question "does so(9,5)+spinor close as a *simple* Lie
superalgebra" is answered by Kac's list. It does not: the super-Poincare siso(9,5|N) is a
semidirect/**inhomogeneous** extension (translations + Lorentz + odd), not simple; no `osp(m|2n)` or
`su(m|n)` packages the *spinor* of so(9,5) as the odd part with `{Q,Q}~P` (osp's odd part is the
*fundamental* of the sp factor, `2n`-dim, not a `so` spinor -- the reps do not match in D=14). So the
right object is `siso(9,5|N)`, and the only question with teeth is whether the **super-conformal**
promotion (a genuinely simple superalgebra with even part the conformal `so(10,6)`) exists. **Nahm
(1978): simple superconformal algebras exist only for spacetime `D <= 6`.** D=14 is far past it. So the
guardian, if present, is a super-*Poincare* (local-SUSY / supergravity), never a super-conformal one.

**(2) Supergravity-algebra specialist.** The gravitino is the gauge field of local super-Poincare, and
the super-Higgs mechanism gives it a mass tied to SUSY breaking. So the branch's YES/NO reduces to:
does a super-Poincare with `{Q,Q}~gamma^mu P_mu` exist for signature (9,5)? Because (9,5) is
**quaternionic** (below), the supercharge is symplectic-Majorana and the R-symmetry is `USp(2N)` --
the D=5/6/7-type story, not the D=4/10/11 Majorana story. Minimal is one Sp(1) doublet (N even). This
is real and standard; a gravitino CAN live here. The catch is that supergravity needs this gauged
*locally* and the mass fixed by super-Higgs -- neither is delivered by the mere existence of the
algebra, and both are exactly the "guardian + mu_DW" data wave 34 named as missing.

**(3) Clifford/spinor rep theorist for (9,5).** Computed on the explicit rep: `p-q = 4 == 4 (mod 8)`
=> quaternionic (CII), antilinear `J^2 = -1` (the *same* structure H37 uses). In the JW basis
`e_a^T = (-1)^a e_a`, from which the two linear charge conjugations are explicit products of gammas:
`C_- = prod_{a odd} e_a` (`eta=-1`, `C_-^T=+C_-`) and `C_+ = prod_{a even} e_a` (`eta=+1`,
`C_+^T=-C_+`). The decisive computation: **`C_- gamma^mu` and `C_+ gamma^mu` are BOTH antisymmetric
for all 14 mu.** Since `{Q_a,Q_b}` is symmetric, a *single* Majorana supercharge cannot carry
`{Q,Q}=(C gamma^mu)P_mu` -- **N=1 super-Poincare is forbidden in (9,5).** The cure is symplectic
doubling: `{Q^i,Q^j}=Omega^{ij}(C_- gamma^mu)P_mu` with the antisymmetric Sp(1) invariant `Omega`;
`Omega (x) (C_- gamma^mu)` is symmetric (verified). So super-Poincare exists **iff N is even**. Weyl
is fine (`omega^2=+I`, 64+64) but Majorana-Weyl is not (`p-q != 0 mod 8`); the minimal object is a
**symplectic-Majorana-Weyl** Sp(1) doublet of 64_C Weyl spinors.

**(4) Non-compact real-form specialist.** GU's gauge arena is the *non-compact* `Sp(32,32;H)` (H23),
`beta_S` signature `(64,64)`. Does the odd part fit? The supercharge sits in the 128 (or its 64_C Weyl
half); `Sp(32,32;H)` acts on exactly that module, and it is dim 8256 -- vast enough to contain a
`USp(2N)_R` factor commuting with the frame `so(9,5)`. So there is no room obstruction: the odd part
fits, and the R-symmetry can be embedded. The non-compactness does *not* forbid the superalgebra (real
forms of super-Poincare exist for indefinite signature); it does mean the SUSY inner product is
Krein/pseudo-unitary, not positive -- the same caveat wave 34 flagged for the positivity bounds. So
non-compactness is a *complication for unitarity*, not a *no-go for existence*.

**(5) Philosopher of science (scout vs claim).** The seductive error here is "super-Poincare exists =>
GU is secretly supergravity." Guard against it: a super-Poincare exists for **essentially every
signature and dimension** (it is an inhomogeneous extension, cheap to write down). Existence of the
*abstract* algebra says nothing about whether GU's *dynamics* gauges it, fixes N, or produces a
propagating gravitino. The load-bearing content is the three *negatives* we can prove -- N=1 forbidden,
super-conformal forbidden, the SUSY Z/2 is not already present as P or omega -- plus the honest
positive that the gravitino-carrying algebra is not obstructed. Verdict must be **PARTIAL**, and the
YES-fragment must be quarantined as "algebraically possible," not "realized."

## The team verdict: PARTIAL

A guardian super-extension **EXISTS** at the algebra level: the symplectic-Majorana super-Poincare
`siso(9,5|N)`, **N even**, R-symmetry `USp(2N)`, with

```
{Q^i_a, Q^j_b} = Omega^{ij} (C_- gamma^mu)_{ab} P_mu
```

closing because antisymmetric `Omega` times antisymmetric `C_- gamma^mu` is symmetric. This is exactly
the algebra whose gauge field is a gravitino, so a **supergravity guardian is algebraically possible**
for GU's (9,5)/Sp(32,32;H) data.

It is **PARTIAL, not YES**, for three computed reasons:

1. **Not forced / not already present.** The super-extension adds a *new* boson/fermion Z/2, odd
   generators, and a `USp(2N)_R`. GU's published bosonic data carries two Z/2's -- the Cartan
   involution `P = beta_S` (rotations +, boosts -; the Krein/ghost parity, H23) and the chirality
   `omega` (the H20 gravity-matter split) -- and **neither is the SUSY grading**: `beta_S != +-omega`
   and `[beta_S, omega] != 0`, and both act *within* the even (bosonic) subalgebra. The guardian Z/2 is
   genuinely new. So "is P secretly the SUSY grading?" -> **No** (Q3).

2. **The simple / super-conformal packaging is obstructed.** No simple Kac superalgebra (`osp`,
   `su(m|n)`) packages so(9,5)+spinor with `{Q,Q}~P`; the super-conformal promotion (even part the
   conformal `so(10,6)`) does not exist because Nahm caps simple superconformal algebras at `D <= 6`
   and here `D=14`. So the guardian can only be the inhomogeneous `siso(9,5|N)` -- a local-SUSY /
   supergravity, never a superconformal CFT dual.

3. **No unique N.** N is even but otherwise unfixed by anything in this branch; GU's carrier-B (index
   -38, order-3) does not single out a specific `siso(9,5|N)`. Matching N to GU's fermion content is a
   separate, unbuilt step.

## COMPUTED vs ARGUED

- **COMPUTED (residual 0 on the verified rep):** quaternionic CII / `J^2=-1`; `e_a^T=(-1)^a e_a`; the
  explicit `C_+`, `C_-`, their symmetries; **both `C gamma^mu` antisymmetric** (the N=1 no-go);
  `Omega (x) (C_- gamma^mu)` symmetric (the N-even closure); `omega^2=+I`, 64+64 Weyl; `beta_S` Cartan
  action (rot +, boost -); `beta_S != +-omega`, `[beta_S,omega] != 0`; `dim so(9,5)=91`.
- **ARGUED:** the Nahm `D<=6` bound (standard classification, dimension-checked here, not re-derived);
  "`Sp(32,32;H)` is large enough to hold `USp(2N)_R`" (dimension argument, not an explicit embedding);
  "a super-Poincare exists for essentially every signature" (structural); "existence != GU realizes it"
  (the load-bearing epistemic caveat).

## Honest limits

- **Existence is not realization.** This branch proves the *target algebra* exists and is
  gravitino-capable; it does **not** show GU's dynamics gauges it, produces a propagating gravitino, or
  fixes the gravitino mass. That is the soldering/guardian question (H23 codim-8165 + `mu_DW`), untouched
  here.
- **No explicit R-symmetry embedding.** I argued `USp(2N)_R` fits inside `Sp(32,32;H)` by dimension; I
  did not construct the commuting `so(9,5) (+) usp(2N)` embedding or verify the odd part transforms
  correctly under both. That is the natural next computation.
- **Krein, not unitary.** The SUSY inner product inherits the indefinite `beta_S` -- `{Q,Q^dag}` is
  Krein-graded, so "positivity of the SUSY algebra" is the same open pseudo-unitary question as
  everywhere else in GU. A super-Poincare that exists as a *complex/graded* algebra need not have a
  unitary rep on a positive Hilbert space.
- **N unfixed.** Even parity of N is proven; the value is not.
- **The rep is finite-dim explicit, not a symbolic proof over the abstract algebra** -- but for these
  finite-dim bilinear-symmetry identities the explicit rep is decisive.

## Branch RE-HYPOTHESIS (blind to other branches)

The N=1 no-go plus the symplectic closure point somewhere specific. **RH-b1:** *GU's guardian, if it
exists, is a symplectic-Majorana `siso(9,5|N)` whose `USp(2N)_R` is not an add-on but is carved from
GU's existing internal structure -- specifically, the quaternionic `M(64,H)` fiber's own
`Sp`-automorphisms already furnish the `Omega^{ij}` that the closure needs.* The `Omega` I used by hand
is exactly an Sp(1) invariant, and GU's spinor module is `H`-linear (`M(64,H)`), so the quaternionic
units `{i,j,k}` acting on the fiber ARE a ready-made `Sp(1)=USp(2)` R-symmetry. If the minimal N=2
R-symmetry is *identical* to the quaternionic structure `J` (the CII `J^2=-1` from H37), then the
supercharge doubling is not new data -- it is the `H`-structure GU already has. That would upgrade the
"NEW Z/2 required" objection: the boson/fermion Z/2 stays new, but the R-symmetry and the symplectic
pairing would be **already present**, making the guardian cheaper than a generic supergravity.

**This is falsifiable:** compute whether the antilinear `J` (H37's `J^2=-1`, tangent-frame charge 0)
commutes with `so(9,5)` and squares/pairs to give exactly the `Omega^{ij}` used in the closure -- i.e.
whether GU's quaternionic fiber-`J` and the SUSY R-symmetry `USp(2)` are the same object. H37 already
found `J` is frame-trivial (charge 0), which is *exactly* the profile of an R-symmetry (it commutes
with the frame `so(9,5)`). That is a strong, specific, checkable lead.

### Ranked next-move

1. **(highest) R-symmetry = quaternionic-J test.** Compute the commutant of `so(9,5)` inside
   `End_H(S)`; check whether it contains `usp(2N)` and whether H37's frame-charge-0 antilinear `J`
   generates the `Omega^{ij}` of the closure. If yes, the guardian's R-symmetry is GU-native (the
   `H`-structure), and only the odd generators + boson/fermion Z/2 are genuinely added. One targeted
   test on the existing rep. **If it fails, the guardian needs imported R-symmetry -- a real cost.**
2. **Explicit `siso(9,5|2)` closure + super-Jacobi.** Build the minimal N=2 super-Poincare generators
   (`P_mu`, `sigma_ab`, `Q^i`) on the rep and verify the super-Jacobi identity numerically, promoting
   "closes" from a bilinear-symmetry check to a full algebra check.
3. **Krein-graded `{Q,Q^dag}` positivity.** Test whether the SUSY algebra admits a positive rep under
   `beta_S`, i.e. whether the guardian is unitary or only Krein-consistent -- this connects directly to
   the ledger-4/8 positivity question and decides whether the guardian actually buys UV-completeness or
   only Krein-hidden consistency.
4. **(lower) N-fixing from carrier-B.** Whether GU's fermion content (index -38, order-3) selects a
   specific N. Needs the fermion sector, so it ranks below the pure-algebra moves.

---

*Filed 2026-07-11, Wave 37, H54 branch-1 (superalgebra existence). Reproducible:
`python tests/wave37/H54b1_superalgebra_existence.py` (exit 0, 15/15 PASS). Exploration-grade; not
promoted to canon. Adversarially graded: no supergravity was manufactured; the honest verdict is
PARTIAL with a computed N=1 no-go, a computed super-conformal no-go (Nahm), and a specific,
falsifiable re-hypothesis that GU's quaternionic fiber may already carry the guardian's R-symmetry.*
