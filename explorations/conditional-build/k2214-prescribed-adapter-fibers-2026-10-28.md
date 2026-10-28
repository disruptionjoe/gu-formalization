---
title: "K2214 Entire prescribed noncommuting adapter fiber excluded"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: INTERNAL-K2214-PRESCRIBED-Y0-ADAPTER
target_claim_verdict: EXCLUDED
claim_ceiling: no real nonsingular normal-grade3/7 port realizing the exact K2205 matrix factor satisfies all ten original rows; no isospectral or general-family exclusion
scripts:
  - tests/channel-swings/k2214_prescribed_adapter_fibers_probe.py
---

# K2214 Entire prescribed noncommuting adapter fiber excluded

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.
Verdict against `INTERNAL-K2214-PRESCRIBED-Y0-ADAPTER`: **excluded**.

```gu-typed-objects
result: complete one-dimensional real reconstruction fiber and its all-row obstruction
carrier: fixed conditional Cl46 normal spinor32 with both chiral16 halves, real grade3/7 ports LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: alternating chiral trace form and real-grade reconstruction ON=declared_carrier
real_structure: quaternionic bar exchanges chiral halves; reconstruction coordinates remain real
grading: normal Clifford grades3 and7; not physical family or observed chirality
action_owner: repository-construction -- fixed normalized ordered adapter equations
target: exact prescribed factor Y0 reconstruction fiber MAP-TYPE=intertwiner
```

## Result

[K2205](k2205-ordered-pencil-real-constraints-2026-10-28.md) constructs an
actual noncommuting real grade3/7 pencil and rejects its original port by a
nonzero Euler residual. This result excludes **every** real nonsingular
normal-grade3/7 port realizing that exact matrix factor Y0, not just the
original witness. It uses [K2208](k2208-grade-constrained-pencil-reconstruction-2026-10-28.md)'s
complete real reconstruction theorem and an exact rank certificate:

    rank_Q E(Y0,+)=rank_R E(Y0,+)=119,
    ker_R E(Y0,+)=R a0,   a0=7w0+15 epsilon u0.         (1)

Every reconstructed port is consequently (w,u)=c(w0,u0), c real nonzero.
Its necessary ordered Euler residual is c² times the known nonzero residual.
Thus the intersection with ALL TEN original equations is empty. No commuting
or anticommuting hypothesis is introduced. Matrices merely similar or
isospectral to Y0 are outside this statement; their Clifford-real-form
position can change the reconstruction kernel.

## 1. Exact input and complete linear fiber

Use K2208's indexed Cl(4,6) matrices, normal volume I_N, chiral index set ix,
B form and epsilon=I_N|ix/i. The coordinates are the120 ordered triples of
{1,...,10}. Let

    w0=123+145+2(267)+3(389)+5(4,6,10),
    u0=2(124)+3(157)+5(268)+7(3,9,10)+11(456),
    v0=I_N w0, t0=i u0,
    P0=7v0-15t0, barP0=7v0+15t0, Y0=P0^-1 barP0.     (2)

Triple labels denote ordered Clifford products, not independent commuting
variables. Both pencil blocks are invertible by the inherited exact fixture.
Phi maps complex grade3 coordinates to alternating16 matrices. For REAL a,
E(Y+)a=0 comprises the real and imaginary parts of the symmetric entries of
Phi(a)Y+, plus the imaginary coordinates of Phi^-1(Phi(a)Y+). These are392
rational rows in120 real unknowns for(2). It follows from K2208 that exactly
these solutions yield real b with Phi(a)Y+=Phi(b), with

    w=(a+b)/14, u=epsilon(a-b)/30.                     (3)

For an actual full real port the opposite chiral half is fixed by the stated
real structure. No half may be deleted from the original equations.

## 2. Finite-field lower rank and exact upper rank

Every entry denominator of E(Y0,+) is invertible modulo the prime1000003.
Take columns0..119 excluding93. Take the ordered rows0..118, replacing the
entry85 by275. The corresponding119-square minor has determinant

    992118 modulo1000003,                             (4)

which is nonzero. A nonzero minor over this finite field proves the same
rational minor is nonzero: rational reduction modulo the prime is legitimate
because no denominator vanishes. Hence rank_Q E>=119. Separately, exact
rational multiplication verifies E a0=0 and a0!=0, proving rank_Q E<=119.
Ranks of a rational matrix agree over Q and R. This proves(1) without assuming
that a numerical singular value or modular nullvector spans the real kernel.

The probe independently reconstructs E and the specified minor; no reported
rank is trusted as input. It also reconstructs b0=7w0-15 epsilon u0 and
checks(3) and the complete32-dimensional original pencil equation. Scaling
linearity then forces every real candidate with this exact Y0 to have the
form c(w0,u0). c=0 is singular and excluded by the original chart condition.

## 3. Ordered Euler obstruction applies to the entire fiber

Write R=v+3t, barR=v-3t and K(X)=sum_j eta_j gamma_j X gamma_j. Preserve
[K2197](k2197-general-ordered-adapter-constraints-2026-10-28.md)'s order:

    A=3K(barR²)+34barR²+36R barR+8barR R-24R²,
    B=184R²+140R barR+184barR R+194barR²
        +24K(barR R)+15K(barR²).

Every solution of all ten original rows obeys their necessary Euler
contraction 4A Y=5B-A. For the actual Y0 one entry of its positive-half
residual is exactly

    (15850252893220743860640
      -1581983112104607593520 i)/27955676769824869 !=0. (5)

A and B are homogeneous degree2 in the ORIGINAL v,t. Keeping Y0 fixed and
scaling the real port by c multiplies the residual by c². For every allowed
c!=0,(5) stays nonzero. Failure of this necessary contraction excludes all-ten
solutions; it is not claimed to replace the all-ten equations for acceptance.
K2211's equivalent degree17 formulation remains valid but has no nonsingular
solution on this fiber. No general noncommuting exclusion follows.

## 4. Semisimple comparison and why reality matters

For a prescribed semisimple chiral16 Y with eight distinct eigenvalues each
of multiplicity2, the complex alternating solutions of ZY=Y^T Z form an
8-dimensional space. In an eigenbasis the alternating form has one2-by2
alternating block per eigenspace and no off-diagonal blocks. A real-grade
reconstruction kernel injects into this space. Real-linearly independent
vectors of a real form are complex-linearly independent; hence its real
dimension is at most8. Additional real-coordinate constraints can shrink it,
as(1) demonstrates. This is a structural upper bound, not an existence
statement and not applicable unchanged to nonsemisimple Y.

Thus prescribed spectral data and norm-one completion do not determine
admissibility: the exact Clifford real form and the ordered Euler rows carry
independent constraints. In particular, complex rescaling is not a new real
port, and a similarity transform cannot be imported without an allowed
Clifford/source transformation.

## Reproduction and remaining question

The exact probe uses the existing SymPy matrix construction, one119-square
modular determinant and exact rational kernel/Euler identities. It tests signed
nonunit rescalings against the original polynomial, not a boolean homogeneity
assertion. Genuine faults duplicate a minor row, corrupt a reconstruction
coefficient, change an Euler coefficient, or violate real-grade coordinates.
Universal reconstruction/homogeneity reasoning, the finite rank certificate,
and inherited actual-pencil evidence are stated separately. No broad nonlinear
search, proof assistant, external-expert certification or novelty is claimed.

This closes the exact Y0 fiber. The next useful adapter question is a genuinely
different prescribed factor/family with original-grade reconstruction and all
ten equations, or a universal noncommuting obstruction. Merely refitting w,u
under this fixed Y0 is now eliminated. Source claims, ledger0.263 and physical
mapping grades remain unchanged.
