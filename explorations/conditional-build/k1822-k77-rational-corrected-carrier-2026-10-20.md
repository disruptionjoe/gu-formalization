---
title: "K1822: exact rational lift of the corrected K77 carrier"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: rational principal-fixture identities only; no functional or physical completion
---

# K1822: the corrected spectral multiplicities now hold over the reals

The declared K435-K439 coefficient fixture has a rational corrected-carrier
operator with eigenvalues `1,-1,1/24,-1/24` and multiplicities
`192,192,64,64`. Its polynomial identities, spectral projectors and ranks are
now certified over the rationals, hence over the reals. They no longer rest
only on agreement at two finite characteristics. This discharges the specific
real-lift premise left conditional in K1821. The selected fixture remains a
conditional principal-symbol model, not a completed source action.

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: rational coefficient certificate for a conditional principal symbol
carrier: K435 rank-1920 real fixture; H640 observed graph; corrected rank-512 subcarrier LAYER=toy CHIRALITY=N/A
pairing: none required for the spectral algebra; no physical pairing supplied ON=principal_fixture
real_structure: QQ matrices extended to R; the selected Cl(7,7) representation
grading: fourteen one-form slots and one zero-form slot; four characteristic eigenspaces
action_owner: repository-construction -- the already declared K435 principal coefficients, not new source-owned interaction coefficients
target: K438 spectral algebra and K1821 factorwise rank premise MAP-TYPE=evaluation
```

## Preflight: the exact question and the cheaper route

K438 serialized exact calculations over GF(1009) and GF(1013). Equality in
those two fields is not a proof of equality over the rationals. K1821 correctly
retained this limitation before applying its factorwise-algebra consequence.
The question here is whether the same rational fixture really has the proposed
quartic and multiplicities. It is not whether a fitted replacement can have
them.

The algebra lens uses a direct time-symbol inverse, small support components
and projector traces instead of a large rational characteristic polynomial.
The verification lens requires direct rational identities and a planted error
invisible at both old primes. The source lens keeps a Lorentzian conditional
fixture distinct from SC-ACT-06's Euclidean ellipticity claim and from a
functional BV/KT physical quotient. The strongest alternative, a newly derived
same-background mixed action jet, would supply stronger physical input but is
not supplied by improving a coefficient certificate.

## 1. Rational construction of the same fixture

The producer independently reconstructs K435's ordered Kronecker Clifford
generators, plus-first signature `(7,7)`, volume element, chirality projectors,
weights `W=P_plus+2 P_minus`, southeast coefficient
`S=11 P_plus/24+11 P_minus/12`, and all used symbol blocks. It imports no
predecessor numerical producer. The primitive formulas and ordering are the
fixture identity; the historical modular digest comparisons below are
additional regression evidence, not the proof of rational identity.

For `D0(x,z)=y`, its first row gives `z=y0`, its final row gives
`x0=gamma0 S y0-yz`, and for `r=1,...,13` set

```
v_r = gamma0 gamma_r y_r,
u_r = gamma_r W x_r.
```

The middle equations read `sum_{c != r, c>0} u_c=v_r`. Summing yields
`sum_c u_c=(sum_c v_c)/12`. Consequently

```
x_r = W^{-1} eta_r gamma_r ((sum_{c=1}^{13} gamma0 gamma_c y_c)/12
                           - gamma0 gamma_r y_r).
```

Both products of this proposed inverse with D0 are checked to be the identity
over QQ. Thus no approximate inversion or inferred modular invertibility is
used. Only the three observed evolutions `E_j=D0^{-1}D_j`, `j=7,8,9`, are
needed.

Apply the eight ordered words `1,E7,E8,E9,E7E8,E7E9,E8E9,E7E8E9` to the
128-column zero-form seed, producing a rational word span V. O restricts to
slots `0,7,8,9,14`. Good reduction of OV at 1009 has rank 640. The producer
records the common denominator and verifies its coprimality with 1009.
A nonzero minor after good reduction proves a nonzero rational minor, so this
is a rigorous lower bound on rational rank, not a finite-field extrapolation.

Take its 640 pivot columns B and invert OB over QQ. The bipartite support
graph splits that inverse into 256 independent blocks of order at most four.
The assembled inverse is checked on both sides. Define `L=B(OB)^{-1}`.
Exact rational checks establish `OL=I`, seed containment, `LOV=V`, and
invariance of `im(L)` under all three observed evolutions. Thus V has rank
exactly 640 and L is precisely the inverse of observation on that H640.
This also proves all longer words stay in the same space.

A proposed shortcut that inferred every hidden slot from one observed
Clifford trace was rejected by the exact E7-invariance test before use.
The final proof uses the actual word-span lift throughout. It does not replace
L by the coordinate inclusion when compressing the action.

## 2. Rational spectral certificate

Use K437's trace and lift on the four observed one-form slots:

```
Gamma = [eta_j gamma_j]_(j=0,7,8,9),
J = [gamma_j/4]^T,
P = diag(I-J Gamma, I_128),
A = P O E7 L P.
```

The exact checks give `Gamma J=I`, `P^2=P`, `tr(P)=512`, `PA=AP=A`,
and

```
576 A^4 - 577 A^2 + P = 0.
```

Here P is the identity on the corrected carrier, not on the full observed
space. Define

```
F = (576 A^2-P)/575,
G = 576(P-A^2)/575,
E_{+1} = (P+A)F/2,       E_{-1} = (P-A)F/2,
E_{+1/24} = (P+24A)G/2,  E_{-1/24} = (P-24A)G/2.
```

Over QQ these four matrices are pairwise orthogonal idempotents summing to P,
satisfy their eigenvalue equations, and have traces `192,192,64,64`.
An idempotent over a characteristic-zero field has rank equal to trace.
Consequently the corrected carrier is the direct sum of exactly those four
eigenspaces. Each is nonzero, so the minimal polynomial is
`(x^2-1)(x^2-1/576)` and the characteristic polynomial is
`(x^2-1)^192 (x^2-1/576)^64`.

The oriented sign operator is also exact:
`Sigma=(601 A-576 A^3)/25`, `Sigma^2=P`. Its incoming/outgoing projectors
have ranks 256 each. These are characteristic subspaces, not physical-state
spaces or a proof of positive norm.

## 3. Consequences and source-data audit

On the real corrected carrier `im(P)`, with identity P, `R[A]` is a
four-dimensional algebra acting by scalars
on the four eigenspaces. Its smallest nonzero idempotent rank is 64. Every
finite sum of base maps tensor polynomials in A has block form
`direct_sum_j B_j tensor I_(d_j)`. Its rank is
`sum_j d_j rank(B_j)`, a multiple of 64. The same divisibility applies to
homology dimensions in complexes formed entirely from these blocks.
K1821's one-mode defect therefore cannot arise within this specified algebra.
This says nothing comparable about the full commutant, arbitrary
nonfactorized couplings or new action data. On the full observed 640-space,
the ordinary unital algebra also sees a zero eigenspace and has dimension
five; that is not the algebra used in the divisibility statement.

Retrieval of K614-K637 prevents treating existing constructions as new input:
the source zero-form seed, moving-varpi graph, polynomial and full-commutant
adapters, ambient and canonical pairings, determinant lines and naturality
ceilings were already examined. K631 distinguishes eight concrete input
types. In particular, the first-action epsilon cross has type
`Q91 -> R1470`; its connection branch does not close the metric Euler equation.
The partial stationary second-action Gram lives on F34, not E512. The
source-owned zero-form inclusion `V128 -> E512` does not provide a nonzero
stationary value or its Riesz return.

The next source construction remains a same-background mixed Hessian or third
action jet with the required variation labels, corrected-carrier map,
stationarity, Riesz return and common domain, or an independently owned
coefficient distinguishing K637's labeled slow seed summands. The rational
lift supplies none of these. SC-ACT-01/02/06 remain ASSERTS and SC-META-53
UNCERTAIN; LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS. No ledger or canon
status moves, and no new physical count or positivity result follows.

## Reproduction and hostile review

From the repository root:

```sh
sage -python tests/channel-swings/k1822_k77_rational_corrected_carrier.py --check
sage -python tests/channel-swings/k1822_k77_rational_corrected_carrier_probe.py
```

The producer recomputes the rational certificate and compares the saved JSON.
All 29 checks pass, including the two computational faults, and a fresh saved
certificate replay passes. The probe imports no producer and compares the inverse
formula with direct exact inversion on four smaller Clifford fixtures. It
also uses independent Lagrange interpolation on a rationally conjugated
five-dimensional model and rejects a Jordan counterfeit.

The full producer plants two computation-level failures: a changed hidden
graph entry preserving `OL=I` fails invariance, and `A+1009*1013*P` has the
same reductions at both historical primes but fails the rational quartic.
Thus the checks distinguish rational evidence from repeated modular agreement.
All eight historical lift/compressed/fast/slow digest comparisons still agree.

The strongest overclaim is to promote a coefficient-level real lift into an
action-derived nonfactorized differential or physical quotient. The strongest
contrary route supplies a new interaction outside `base maps tensor R[A]`.
The weakest remaining reproduction seam is the explicitly fixed primitive
Clifford representation and selected principal coefficients; their physical
ownership is not independently established by these exact calculations.
