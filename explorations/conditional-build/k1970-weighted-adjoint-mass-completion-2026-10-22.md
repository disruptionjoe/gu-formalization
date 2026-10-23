---
title: "K1970: The complete chiral-weighted adjoint obstruction"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1970_weighted_adjoint_mass_completion.py
  - tests/channel-swings/k1970_weighted_adjoint_mass_completion_probe.py
---

# K1970: The complete chiral-weighted adjoint obstruction

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
result: exact obstruction for two complete chiral-weighted bilinear-adjoint families and a quantified non-adjoint repair
carrier: K1951 real1920 raw operator and K1967 fixed positive128 core LAYER=toy CHIRALITY=N/A
pairing: inherited H=8I; tested spinor pairings Q=I P or B P ON=fixed_observed_core
real_structure: real Cl(7,7); complex bilinear weights allowed for the obstruction
grading: Clifford volume eigenspaces, not physical chirality
action_owner: repository-construction -- K1967 conditional scalar mass line
target: actual lower raw block compatibility MAP-TYPE=intertwiner
```

## 1. Question and exact result

[K1967](k1967-paired-raw-coefficient-observation-2026-10-22.md) constructs a
nonzero conservative mass on the actual raw core, using an independently supplied
lower return. Its four unweighted bar tests fail. This result decides the entire
chiral-weighted extension of two declared adjoint families, rather than sampling
more weights. It also quantifies the extra freedom needed to remove the obstruction.

Keep its normalized coefficients (a,b,c,d)=(-5301,-594,7559,198)/23168,
Omega_k=eta_k gamma_k(a+c omega) horizontally and
eta_k gamma_k(b+d omega) normally, its injection J and mass M.
Let Pi_+/-=(I+/-omega)/2, P=p_+ Pi_+ + p_- Pi_- with p_+ p_- nonzero.
Test BOTH signs epsilon=+1,-1 in

    barOmega_k=epsilon Q^-1 Omega_k^T Q,
    Q=P  or  Q=B P,       B=gamma_0 ... gamma_6.          (1)

The transpose is the stated coordinate transpose. This is a bilinear adjoint,
not an inferred source Hermitian adjoint, Hodge star or antireal identification.
The conclusion holds even for complex nonzero p_+,p_-, so real positive and
indefinite chiral weights are included.

NO choice in either family produces K1967's required raw lower row. More
precisely its residual has rank at least64, and64 is attained by cancelling
one volume sector. The obstruction therefore cannot be made exactly zero by
an overlooked chiral weight or either sign.

## 2. Reduce infinitely many weights to one invariant product

Let T=-J_0 M be the required lower output. For Q_0=I or B form

    L_0=-sum_k eta_k Q_0^-1 Omega_k^T Q_0 J_k.

Both T and L_0 are monomial128-square matrices. On their OUTPUT volume
sectors the complete matrices satisfy L_0=r_+ Pi_+ T+r_- Pi_- T, with:

|Q_0|r_+|r_-|r_+ r_-|
|---|---|---|---|
|I|-1041/11584|-3303/1448|3438423/16773632|
|B|-2995/2896|-1349/1448|4040255/4193408|

Each Omega_k is odd. Thus conjugating its adjoint by P multiplies an output
plus row by1/q and a minus row by q, where q=p_+/p_-. The actual required
matrix equation becomes

    epsilon r_+/q=1,       epsilon r_- q=1.             (2)

Multiplication requires r_+ r_-=1. Neither exact rational product equals1.
This eliminates the whole nonzero weight space; finite weight samples are
controls only. At q=epsilon r_+ exactly the plus64 rows vanish, while all
minus64 entries remain nonzero. The opposite choice cancels the minus rows.
Otherwise the residual has rank128. The certificate checks all128 raw lower
entries for each family, including their support, not one suggestive entry.

K1967 already proves that the complete upper-preserving four-scalar ansatz has
exactly one conservative mass line for H=8I. Every nonzero point on that line
rescales both T and L_0 equally. Consequently this is an obstruction for the
ENTIRE nonzero conservative line in that ansatz, not just its unit normalization.
The upper196 grade-one obstruction remains a separate reused result.

## 3. Why the second family is the full Spin-invariant bilinear class

The signed tensor gamma matrices obey gamma_k^T B=B gamma_k and B^T=-B.
Hence each spin generator gamma_i gamma_j is skew-adjoint for B.
An invariant bilinear matrix Q must have B^-1 Q commuting with every even
Clifford generator. The real even Cl(7,7) algebra acts as the full matrix
algebra on each of its two inequivalent real64-dimensional half-spinor
modules. A direct dimension proof uses the8192 even Clifford blades: they commute
with omega and are independent under the matrix trace pairing. Every
nonidentity blade has zero trace, by conjugation with an anticommuting gamma;
products of distinct blades reduce to such a blade. Their dimension equals
2 times64 squared, the full block-diagonal algebra dimension. Its commutant
therefore consists of p_+ Pi_+ + p_- Pi_-.
Thus Q=B P is the complete invariant bilinear family on THIS spinor carrier.
B anticommutes with omega; allowing both chiral weights includes the symmetric
and alternating special choices and does not presuppose a positive form.

This representation statement concerns the specified spinor module, not all
possible pairings of the vector-spinor/auxiliary raw1920 carrier, different
connection placements, moving cores or source full20 fields. The coordinate
family Q=P is included separately; it is not called Spin-invariant.

## 4. Released repair and density consequences

If one FREES two output-sector multipliers s_+,s_- rather than using an adjoint,
the unique repair is s_+=1/r_+, s_-=1/r_-. It reproduces every required lower
entry. But s_+s_-=1/(r_+r_-) is not1. The resulting operation is not obtained by conjugating the specified base
adjoint with a single chiral-diagonal P. General bilinear adjoints themselves
need not be involutions unless their forms obey the additional symmetry rule. An equivalent common
rescaling xi followed by a weight would require

    xi^2=16773632/3438423 (coordinate),
    xi^2=4193408/4040255 (Spin-invariant).                (3)

These positive values show exactly how a changed lower coupling could repair
the equation. They do NOT select that coupling or turn a scalar-rescaled
transpose into the same adjoint. A nonunit common rescaling is additional
operator data, not an innocuous common normalization of Q: multiplying Q by
any nonzero scalar cancels in Q^-1 Omega^T Q.

For the same reason a scalar density factor multiplying the pointwise pairing
cannot alter (2), even if that factor varies. A DIFFERENTIAL formal adjoint of
a variable operator has derivative-of-density and derivative-of-pairing terms;
those are a changed lower-order operator and are not excluded by this algebraic
statement. The current test therefore leaves an explicit route: construct the
actual source differential adjoint with its pairing, density and coefficients,
or change the core/coefficient class. It does not manufacture that input.

## 5. Source fidelity, verification and limits

SC-OP-04 ASSERTS a candidate four-field grammar; it does not identify (1) with
the source barred-star operation. SC-OP-05 remains UNCERTAIN about a different
southeast completion. SC-MAS-01 ASSERTS a stylized local mass; SC-MAS-02 ASSERTS
its mass-role reading with an in-some-sense hedge. Neither selects this mixed
grade1/13 line, these pairings or the extra rescaling. SC-META-53 is UNCERTAIN;
LT-SM8/LT-GR6b/AC-F1 and RA-F1 remain NEEDS. No source or ledger verdict moves.
The primary s9 extraction and DS-1 grade inventory retain their limits.

The producer reuses K1967's checked core assembly. The separate probe imports
no producer or predecessor implementation: it reconstructs signed tensor gamma
matrices, raw core injection and both lower matrices from the pinned data.
It verifies256 exact raw entries. Four actual mathematical faults are rejected
after its clean baseline. Fifty producer controls include the invariant-form
identities, exact ratios, residual ranks and free-sector repair. The universal
weight and rank claims follow (2); finite tests do not supply their quantifier.
Internal mathematical review is not an independent expert or proof-assistant
certification. Strongest contrary construction is the explicitly NON-adjoint
repair above; strongest overclaim would identify (1) as the unbuilt source star.
