---
title: "K1828: raw zero-form completion on the fixed corrected K77 graph"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact conditional raw-column compatibility and completion; no source-selected action or physical quotient
---

# Raw southeast freedom needs a companion cell

A raw coefficient supported only in the zero-form-to-zero-form cell does
**not** realize K1826's graph-preserving normalized zero-form map. On the
fixed K1822/K1826 fixture, every nonzero such block B leaks from H640 and
from the corrected E512, with leakage rank exactly rank(B).

There is an immediate exact repair. Add a time-one-form output cell
N=S^-1 gamma0 B in the same input column. This pair normalizes to the
pure zero-form map N, preserves both carriers, and has rank rank(B).
The repair is unique within this two-cell support. It is not selected by
an actual coupled action. Allowing all output cells gives a complete affine
space of corrected-compatible columns with prescribed southeast B, of
real dimension 49,152. This removes an apparent compatibility obstruction
while exposing the unowned companion data precisely.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: exact raw zero-form-column obstruction and complete corrected-compatible completion space
carrier: conditional rational ambient1920 with actual H640 graph and corrected E512 LAYER=toy CHIRALITY=N/A
pairing: coordinate dual for input-column selection only; no barred physical Riesz map ON=frozen_K77_fixture
real_structure: rational Cl(7,7) matrices extended to real coefficients
grading: observed one-form and auxiliary zero-form slots; no physical-state grading
action_owner: repository-construction -- raw K and normalized D0^-1 K distinguished; no selected source action
target: fixed-carrier coefficient descent and affine completion MAP-TYPE=evaluation
```

## 1. Inputs and scope

Reuse [K1822](k1822-k77-rational-corrected-carrier-2026-10-20.md)'s rational
principal fixture and [K1826](k1826-k77-graph-preserving-internal-coefficients-2026-10-20.md)'s actual graph formula. SC-OP-04 ASSERTS candidate operator grammar and SC-OP-05 is UNCERTAIN
about its nonzero southeast rival. That admitted nonzero
southeast grammar does not fix a lower-order coefficient on this conditional
realization. SC-ACT-01/02/06 remain ASSERTS, SC-META-53 remains UNCERTAIN;
RA-F1, AC-F1 and LT-SM8 remain NEEDS. No ledger or canonical status changes.
The August 10 W-graph port results and August 11 unrestricted Euler-image
result concern different carriers; they do not authenticate H640 as a
physical field restriction. This note does not revive that attribution.

Write e_r for the ambient spinor inclusion into one-form slot r and e_nu
for inclusion into the auxiliary slot. Q_nu is its coordinate retraction.
O selects slots (0,7,8,9,nu), and L is the actual lift, OL=I640. The hidden
blocks, r outside {0,7,8,9}, are

```
L_rs=-eta_r gamma_r gamma_s/20,   L_r,nu=0.
Gamma=(eta_s gamma_s)_s,   J=(gamma_s/4)_s,
P=diag(I-J Gamma,I128),   E512=im(P),
S=11 Pplus/24+11 Pminus/12,   T=gamma0 S.
```

Gamma is weighted. The hidden lift uses the unweighted trace. They are
not interchangeable. gamma0^2=I and S is invertible, so T^-1=S^-1 gamma0;
reversing that order is generally wrong.

## 2. Universal obstruction, with its rank

The actual inverse has the two column identities

```
D0^-1 e_nu=-e0,
D0^-1 e0=e0 T+e_nu.                                      (1)
```

For a raw southeast-only K=e_nu B Q_nu, normalized evolution on an input
with auxiliary component u is -e0 B u. Its hidden graph defect is

```
[(I-LO)D0^-1 e_nu B]_r=-eta_r gamma_r gamma0 B/20.        (2)
```

Every prefactor in (2) is invertible, so the entire stacked defect has rank
rank(B): one hidden row already has that rank, and the stack factors through
B. Its corrected observed trace is -gamma0 B, also rank(B).
The input Q_nu is surjective on both H640 and E512, so these are actual
restricted-map defects, not unused column diagnostics. Preservation holds
if and only if B=0. This binds only the fixed graph and raw support, not
all four-field operators, all backgrounds, or the source claim.

## 3. Execute the smallest support repair

For K=(e0 N+e_nu B)Q_nu, (1) gives

```
D0^-1 K=[e0(TN-B)+e_nu N]Q_nu.                          (3)
```

There are no hidden outputs. The hidden lift of its observed time component
vanishes precisely when TN-B=0. Therefore the unique repair in this support
is N=T^-1 B. Its normalized map is e_nu N Q_nu, exactly the class K1826
already showed preserves the graph and corrected image. Its rank is rank(B).
One nonzero block alone fails; adding this one companion block succeeds.
This is minimal in number of additional blocks for this column, not a
uniqueness theorem over every possible support or an action-derived repair.

For example B=T gives N=I; B=T E_ab gives N=E_ab, including rank-one and
nilpotent choices. K1826's joint full M512(R) algebra then remains available
in this raw-completed conditional class. That algebra theorem is reused,
not recomputed or counted as a new physical result. The lower-left barred
return, background stationarity, actual relation and common domain have not
been supplied by setting these coefficients.

## 4. All one-column completions, not just the seed

Let R be an arbitrary 1920-by-128 output column and K=R Q_nu. Corrected
graph preservation is equivalent to

```
R=D0 L W,       W: R128 -> E512.                        (4)
```

There are 512*128=65,536 independent real parameters. The raw southeast
return on W=(psi0,psi7,psi8,psi9,nu) is

```
e_nu^T D0 L W=-psi0+T nu.                               (5)
```

This map from E512 to R128 is surjective, as its restriction to pure nu
is T. Fixing the raw southeast block to B gives the complete parametrization

```
Gamma psi=0,    nu=T^-1(B+psi0),    R=D0 L(psi,nu).        (6)
```

Here psi is any map from R128 to the 384-dimensional ker(Gamma).
Thus each B, including singular B, has an affine space of dimension
384*128=49,152 of completions. Injectivity of D0 L prevents hidden parameter
redundancy. The zero psi choice is the two-cell repair; nonzero psi adds
homogeneous completions. Nothing in this large affine family selects a
barred adjoint, physical mode or source interaction.

## 5. Reproduction and hostile checks

```
sage -python tests/channel-swings/k1828_k77_raw_zero_form_completion.py
sage -python tests/channel-swings/k1828_k77_raw_zero_form_completion_probe.py
```

The full producer reconstructs rational D0, its inverse, the explicit graph
and corrected projector. It checks all hidden blocks, surjectivity, a
nonzero homogeneous completion, and zero, identity, rank-one, nilpotent,
rank-64 and gamma examples. The universal claims follow from (1)-(6),
not from the examples. The independent small-model probe inverts its own
matrix rather than importing the producer, checks a complete matrix basis,
and rejects the normalization-order and wrong-sign repairs. It does not
independently reconstruct the full K1822 ambient fixture. Six reporting
mutations are labelled separately from the mathematical controls.

**Preflight.** Graph elimination outranked another matrix-unit plant:
normalization changes the support before any rank claim is relevant.
The complete raw-column class and its immediate repair were selected together.
Source and variational lenses forbid attributing the conditional repair to
the source's southeast permission. Exact inverse identities replace a large
linear-system search.

**Postflight.** The strongest overclaim is a source-action obstruction or
source-selected repair; neither is asserted. The explicit two-cell repair
is the strongest contrary construction to broadening the southeast-only
failure. The weakest transfer seam is the fixed principal fixture and
unowned pre-variation carrier. All results remain active research, with no
novelty or physical acceptance claim. Full independent reconstruction of
these exact conditional results remains available before any canon review.

Next: intersect (6) with an actually supplied same-background mixed-action
coefficient and its barred return. Selecting an arbitrary element of this
affine space or symmetrizing under a coordinate Euclidean form would not
supply that ownership. A changed graph/background is a different problem.
