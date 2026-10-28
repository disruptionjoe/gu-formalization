---
title: "K2205 Real Clifford pencils and singular-safe reconstruction"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact necessary Euler interface and actual nonsolution spectral countercontrol; no general adapter classification
scripts:
  - tests/channel-swings/k2205_ordered_pencil_real_constraints_probe.py
---

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: actual Clifford spectral countercontrol and singular-safe Euler reconstruction
carrier: real Cl77 S128 with auxiliary complex normal S32 and chiral16 halves LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: inherited alternating normal-pencil forms ON=declared_carrier
real_structure: real grade3 w,u and grade7 v with quaternionic paired halves
grading: normal Clifford parity and grade, not observed chiral families
action_owner: repository-construction: fixed normalized K2169 adapter and necessary K2171 Euler equations
target: necessary matrix reconstruction and precise spectrum limits MAP-TYPE=intertwiner
```

# K2205 Real Clifford control and singular-safe ordered-pencil tests

This concerns the fixed K2169 normalized zero-order adapter, full real Cl(7,7) S128 with W(3,1)+N(4,6), and its faithful auxiliary complex normal module32. Normal chirality16+16 is bookkeeping; no observed chiral-family or positive physical pairing is asserted. Existing source-native routing and signature caveats remain. Classification: BRIDGE_OR_SEMANTIC_BOUNDARY; target NONE-NOT-A-KILL. No source, physical quotient, ledger or canon change.

## Inherited, checked structurally

K2202's alternating-primary quotient proof does establish paired Jordan blocks on EACH chiral16 half. K2197 supplies the ordered necessary equations, not sufficient original-ten-row descent. K2195's finite root/trace census uses commutation of its V,T,H and does not transfer to the general case.

## New universal singular-safe test

Write C=5B−A, with A,B the actual ordered K2171 Euler coefficients. K2197 says

    C=4AY,     bar(C)Y=4bar(A),      Y=P^-1 bar(P),
    M Y=N,
    M=[4A;bar(C)],       N=[C;4bar(A)].

Bars remain the tangent-volume sign involution, not reversion. All these coefficient matrices are even, so the stacked equation restricts separately to each normal chiral16 block. M,N there have dimensions32×16. The actual Y is invertible. Consequently

    im M=im N,
    rank[M N]=rankM=rankN.

Already the upper equation gives im C=im A and identical left kernels, so rank[A C]=rankA=rankC. These assertions do not invert A or any individual port. They apply on singular A faces too.

If rankM=16, choose any left inverse L, LM=I. Then the only possible Y is Z=LN. The necessary image test ensures MZ=N. Uniqueness makes Z independent of L. Image equality and full column rank force Z invertible: Zx=0 implies Nx=0 and rankN=16. The solution's Z must then satisfy K2202 paired-Jordan conditions, and its monic degree8 characteristic square root must annihilate it. Failure of any test rejects this candidate. If A is invertible one may simply use Z=A^-1 C/4.

If rankM<16, do not invent a unique Z. Differences of solutions are arbitrary matrices with image in kerM. Equality imM=imN alone is sufficient for *some abstract invertible right factor* Y, by choosing isomorphisms between their equal-dimensional kernels and quotient complements; it does not force an arbitrarily chosen Y to be norm-one. The paired equations nevertheless admit an abstract norm-one completion, proved below. Paired Jordan, the prescribed real Clifford pencil and the original ten rows remain separate tests.

### Released consequence: abstract norm-one completion

Let beta:End(S+) -> End(S-) be the antilinear multiplicative isomorphism
implementing real Clifford bar, with inverse on the opposite half. The full bar squared
on the two-block endomorphism algebra is identity, although its underlying quaternionic map
squares to -I. Thus beta(A+)=bar(A)- and beta(bar(A)+)=A-, likewise C.
If invertible Z+ solves the two stacked equations, applying beta gives

    4bar(A)- beta(Z+)=bar(C)-,    C- beta(Z+)=4A-.

Set Z-=beta(Z+)^-1 and multiply on the RIGHT. Then

    bar(C)- Z-=4bar(A)-,        4A- Z-=C-.

Consequently Y=diag(Z+,Z-) solves the paired Euler system and
bar(Y)=Y^-1. Conversely any such Y yields image equality. Image equality
on ONE chiral block is therefore equivalent to existence of some abstract
even invertible norm-one right factor, even at deficient rank. One must not
choose its halves independently. This closes the abstract reality-completion
step; it does not reconstruct the prescribed odd real grade3/7 pencil,
force paired Jordan blocks, or solve the original ten rows.

For invertible A, the concrete polynomial test is

    det(C−4zA)/det(4A)=det(zI−Z)=q(z)^2,
    deg q=8, q monic, q(Z)=0.

The sign is positive because the chiral dimension16 is even. Retain the annihilator test: a characteristic square alone does not rule out unpaired Jordan blocks. The q(Z)=0 test is necessary but does not by itself imply paired blocks either; full pairing requires the Jordan-size condition or an alternating intertwining form.

This is a general rejection interface and does not classify all real ports. It does not derive a scalar polynomial with coefficient constraints comparable to K2195's quartic/trace closure.

## New actual real-port countercontrol

Use positive n1,...,n4 and negative n5,...,n10. With sorted blades,

    w=n123+n145+2n267+3n389+5n4,6,10,
    u=2n124+3n157+5n268+7n3,9,10+11n456,
    v=I_N w, t=i u, P=7v−15t, bar(P)=7v+15t.

These are actual real grade3 w,u and grade7 v. Both [v,t] and {v,t} are nonzero. The explicit Fock representation is exactly K2202's signature(4,6) representation. Both off-diagonal16×16 P blocks are invertible, with determinants

    3201105361546960165450616548831891456,
    2920066167838837908960494130311827456.

For the odd-parity Y block, its exact characteristic polynomial is q(z)^2. Put d=27955676769824869 and define Q=d q by the descending coefficients

    [27955676769824869,
     215594311518921148,
     735656678328289732,
     1446576020362616836,
     1790520274742798830,
     1428142198979408836,
     717403806735025732,
     207896520846657148,
     26700314216456869].

Exact polynomial gcds give gcd(q,q')=1 and gcd(q,q^#)=1, where

    q^#(z)=z^8 conjugate(q(1/conjugate(z)))/conjugate(q(0)).

Here all q coefficients are real. K2202 reciprocal-conjugate transport gives the opposite chiral characteristic polynomial (q^#)^2. Thus the full32 Y has16 DISTINCT eigenvalues of algebraic multiplicity exactly TWO. Its eigenvalues avoid the unit circle: a unit-modulus root would be shared by q and q^#. By the inherited paired-Jordan theorem and squarefree q, every Jordan block has size1.

This strengthens K2202's ABSTRACT non-fourfold countercontrol to an ACTUAL grade3/7 real-port control. Thus reality, Clifford grades, pencil invertibility and the universal alternating pairing alone cannot yield fourfold full multiplicity or unit-modulus spectrum. This is NOT a counterexample satisfying the Euler filter or original ten rows. Indeed the actual ordered Euler residual 4AY−C has (0,0) entry on the odd block

    (15850252893220743860640−1581983112104607593520 i)
      /27955676769824869,

which is nonzero. The control is explicitly rejected by an inherited necessary all-ten-row contraction.

## Reproduction, limitations and next condition

Run `python tests/channel-swings/k2205_ordered_pencil_real_constraints_probe.py`
with SymPy installed. `--write` regenerates the companion report. One fixed
support is evaluated, with exact rational-Gaussian entries expanded before
characteristic-polynomial computation; no parameter search is claimed.
The probe checks the actual Clifford signature, explicit grade3/7 construction and odd-pencil parity, both
pencil blocks, the degree8 square and annihilator, reciprocal coprimality,
nonzero Euler residual, and abstract singular/deficient-rank reconstruction
fixtures. Baselines precede deliberate matrix, polynomial, image-space and
reality-factor faults. These are exact finite controls supporting the written
universal matrix proof, not proof-assistant or external-expert certification.
The actual-port spectral witness strengthens K2202's abstract witness; it does
not establish an adapter solution. General noncommuting reconstruction still
requires the prescribed pencil, paired Jordan constraints and all ten rows.

The next useful algebraic consumer is the intersection of actual Euler image
equality and the grade-constrained pencil equations. Norm-one completion is
settled abstractly and must not be requeued as an unproved obstruction. A
numerical singular-rank guess is not an exact certificate.
