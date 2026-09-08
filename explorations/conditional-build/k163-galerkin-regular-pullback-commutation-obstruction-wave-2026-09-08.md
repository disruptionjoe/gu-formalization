---
title: "K163 Galerkin regular-pullback commutation obstruction wave"
status: active_research
doc_type: conditional_galerkin_regular_pullback_compatibility_obstruction_and_fixed_cylinder_tail_result
created: 2026-09-08
date: 2026-09-08
claim_ceiling: exact repository-owned compatibility obstruction and conditional fixed-cylinder tail interface for the supplied equal-coupling two-edge signed point-Fock control; the free form compresses exactly under physical dyadic refinement, while independently rebuilding the cutoff counterterm and nonlinear regular pullback does not, with exact raw q=(0,0) defect 2/105 in the one-to-two-cell control; K161's five weighted tails bound fixed-cylinder action columns only after a same-family finite anchor and K162 Gram proof are supplied, while the native anchor, complete form-dual residual, coercivity, next-spectrum and left floors remain absent, so no native count, K152 interval, physical/source selection, Born derivation, prediction or confirmation follows
manifest: lab/process/k163-galerkin-regular-pullback-commutation-obstruction-wave.json
solver: tests/channel-swings/k163_galerkin_regular_pullback_commutation_obstruction.py
probe: tests/channel-swings/k163_galerkin_regular_pullback_commutation_obstruction_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K163 Galerkin regular-pullback commutation obstruction wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact remains on
> a repository-supplied positive particle/hole control. It does not identify
> the source-native GU object or select a physical polarization, extension,
> coupling, state, observable or Hamiltonian. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet tests the transfer from K155's independently assembled
finite cutoff matrices to K162's literal common-carrier refinement. It proves
that the free form has the expected Galerkin identity, while rebuilding the
cutoff-dependent counterterm and nonlinear boundary chart at each scale is not
the same operation as compressing one fixed form. It then states the exact
additional premise under which K161's five weighted tails enclose a fixed
cylinder action column. It neither denies the regular K139 operator nor
constructs the missing same-family anchor.

```gu-typed-objects
result: exact failure of independent cutoff-Hamiltonian and nonlinear regular-pullback reconstruction to commute with physical dyadic Galerkin compression, plus a conditional fixed-cylinder five-tail enclosure and fail-closed K152 readiness verdict
carrier: the q=(0,0) hard-core sector of the impurity C3 tensor antisymmetric Fock space over one coarse momentum cell and its two fine children, with physical cell-norm-scaled point couplings and the K162 exterior refinement LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive exterior-Fock Hilbert pairing in unnormalized cell coordinates, with coarse Gram obtained exactly from fine Gram and K161's right spectator-energy weight used only on named cylinder vectors ON=repository_signed_point_control
real_structure: CAR adjoint and exact Q(sqrt(2)) arithmetic; signed flavor transport remains available from K162 but no physical real form or state is selected
grading: conserved incidence charge, coarse versus fine cell level, free linear form versus cutoff counterterm versus nonlinear regular chart, fixed-cylinder column versus complete form-dual norm
action_owner: repository-construction -- cutoff counterterm, extension, polarization, couplings, domain, trial core and state are not selected by Weinstein's source or a GU action
target: decide whether K155/K157 finite matrices are admissible K162 coarse anchors and type the surviving same-family Galerkin route into K152 MAP-TYPE=intertwiner
```

## Inline preflight bookend

K162 made the common carrier literal but left every native regular entry open.
The tempting continuation is to reuse K155's one- and two-mode matrices as
coarse and fine anchors. That is valid only if the operator construction is
compatible with K162 refinement or if its incompatibility is bounded as a
same-family cutoff error. K162's universal congruence is a coordinate law for
one supplied form; it does not say that two independently rebuilt forms are
equal.

Mechanism retrieval found K139's cutoff-dependent endpoint subtraction,
K155's nonlinear inverse chart, K156's normal-ordered limiting object, K158's
failure of the free-operator graph comparison, K161's complete right-weighted
tail and K162's exact exterior refinement. No held artifact checks the
commuting square between independent rediscretization and Galerkin
compression.

The route census compared high-cutoff diagonalization, coefficientwise
quadrature, exact Galerkin compression, boundary-triple/Feshbach
reconstruction, Kato form convergence, generalized Ritz, Schur exterior
floors and Lehmann--Goerisch. The exact commuting-square discriminator comes
first: if the square fails, a large finite spectrum remains a regulator
spectrum. Computation is an exact `Q(sqrt(2))` witness, not a numerical search.

`SC-META-53` remains `UNCERTAIN`; `LT-SM8`, `RA-F1` and `AC-F1` remain
`NEEDS`. The packet supplies no physical state, quotient, family count or
chirality mechanism and moves no source or physics ledger row.

## 1. Physical one-cell-to-two-cell control

Take one coarse cell of width two with unnormalized indicator `chi`, and split
it into unit-width children `chi_1,chi_2`:

```text
chi = chi_1 + chi_2,       ||chi||^2=2,
||chi_1||^2=||chi_2||^2=1.                              (1)
```

Use child free energies `1,3`, so the coarse Galerkin energy is their average
`2`. A constant point form factor couples to a normalized cell with the square
root of its width. Thus the coarse normalized coupling is `sqrt(2)` and the
two fine normalized couplings are `1,1`. Exterior powers of (1), with the CAR
permutation sign, map the complete q=(0,0) hard-core block of dimension `8`
into the fine block of dimension `84`.

In unnormalized coordinates the free quadratic forms obey exactly

```text
A_coarse = J^* A_fine J.                               (2)
```

The solver proves (2) entry by entry in exact `Q(sqrt(2))` arithmetic. This is
the positive control: the physical refinement, Gram and free-energy averaging
are mutually compatible.

## 2. Independent cutoff reconstruction does not commute

At auxiliary shift `lambda=4`, independently constructing the matched
endpoint counterterm gives

```text
c_coarse = 2/(2+4)=1/3,
c_fine   = 1/(1+4)+1/(3+4)=12/35.                     (3)
```

The vacuum endpoint coefficient is twice these values. Galerkin compression
therefore has the exact first raw-form defect

```text
2 c_fine - 2 c_coarse = 24/35 - 2/3 = 2/105.          (4)
```

The nonlinear chart

```text
G=-(H0+lambda)^(-1)C^*,
R=(1-G)^(-*) H (1-G)^(-1)                             (5)
```

also fails the commuting square. The exact 8-by-8 versus 84-by-84 comparison
finds a nonzero vacuum-entry defect after both sides of (5) are evaluated; it
does not infer failure merely from (4).

This is not a contradiction in renormalization. Finite cutoff counterterms
are scale-dependent subtraction data, and K156 defines the regular limiting
form after cancellation. The consequence is narrower and decisive:

```text
independently assembled K155/K157 matrices
    != native K162 Galerkin coarse matrices.           (6)
```

Their exact inertias remain valid regulator controls. A native anchor must
instead be the compression of one fixed limiting regular form, or one
same-family finite approximation accompanied by an outward bound to that
form.

## 3. What K161 supplies on a fixed cylinder

K161 proves

```text
||(W_Lambda-W)(1+S)^(-1)|| <= epsilon_Lambda.          (7)
```

Therefore every named cylinder vector `phi` with spectator-energy bound
`S<=s_phi` satisfies

```text
||(W_Lambda-W)phi||
 <= epsilon_Lambda ||(1+S)phi||
 <= epsilon_Lambda (1+s_phi)||phi||.                  (8)
```

For `s_phi=4`, the complete five-component K161 bounds give

```text
Lambda=4096:  5 epsilon_Lambda = 396385/319488,
Lambda=65536: 5 epsilon_Lambda = 33111485/123076608.  (9)
```

Equation (8) is a genuine Cauchy action-column enclosure once
`W_Lambda phi` is evaluated on the same K162 family. The compiler requires
both that same-family anchor reference and K162's refinement/Gram proof. It
rejects the current chain because K155's two arbitrary modes and K157's
zero-fill matrices satisfy neither requirement.

An action-column norm is not the complete shifted form-dual residual. The
latter is a supremum over the full shifted form domain and still needs an
operator-specific representer or a complete complementary bound. Nor does
(8) supply coercivity, the next distinct spectral floor, or a floor excluding
spectrum below `-5`.

## 4. Consequence for K152

The regular route remains open, but the next data must be assembled in this
order:

1. construct the K139 regular form directly on K162's common carrier;
2. define each finite form matrix by exact compression of that one form, or
   evaluate one same-family cutoff form and carry the complete K161 tail;
3. combine the resulting column enclosure with a complete shifted form-dual
   residual and a positive coercivity floor; and
4. prove the next-distinct and left spectral floors on the same operator,
   preferably by form-level Lehmann--Goerisch if a complete exterior minorant
   cannot be closed.

Only that packet may enter K152. The current native contract remains missing
the same-family regular form, complete residual, coercivity, next-spectrum
floor and native left floor. K162 already supplies the signed charge
intertwiner, but one completed field cannot substitute for the other five.

## Inline postflight bookend

- **Strongest positive control:** the free form, point-coupling cell scaling,
  non-identity Gram and exterior refinement form an exact Galerkin square.
- **Strongest obstruction:** independently rebuilding the endpoint
  counterterm already produces the exact raw defect `2/105`; evaluating the
  complete nonlinear regular pullback also gives a nonzero defect.
- **Strongest surviving route:** K161's complete weighted estimate gives
  explicit fixed-cylinder action-column errors through (8), but only from a
  same-family finite anchor.
- **Strongest overclaim:** “K163 disproves the regular K139 realization.”
  Refused. It rejects one finite-anchor identification, not the limiting
  operator.
- **Strongest contrary result:** K155/K157 finite inertias and exact matrices
  remain valid regulator controls and may become useful after a separate
  same-family approximation theorem.
- **Weakest reproducibility seam:** the cell width, point-coupling square-root
  scaling, unnormalized Gram and CAR exterior signs must travel together;
  dropping any one can create a false commuting square.

No compatible admitted unit remains executable without first constructing the
same-family regular form. The native count and physical/source arcs remain
dependency- and authority-blocked, respectively; no scale-down occurred.

## Next condition

Construct the normal-ordered K139 regular form on K162's dyadic carrier and
serialize one exact same-family Galerkin form matrix. Use (8) with K161's five
tails to enclose its fixed-cylinder columns, then prove the complete shifted
form-dual residual and coercivity. Apply a form-level Lehmann--Goerisch or
complete exterior argument for the next-distinct and below-`-5` floors before
feeding K152. Do not reuse an independently rebuilt cutoff matrix as that
anchor.

## Reproduction

```bash
python3 tests/channel-swings/k163_galerkin_regular_pullback_commutation_obstruction.py --demo
python3 tests/channel-swings/k163_galerkin_regular_pullback_commutation_obstruction_probe.py
python3 tests/channel-swings/k163_galerkin_regular_pullback_commutation_obstruction_probe.py --selftest
```
