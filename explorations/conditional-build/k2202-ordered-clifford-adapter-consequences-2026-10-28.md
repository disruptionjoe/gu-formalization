---
title: "K2202 Ordered Clifford adapter pencils have paired Jordan blocks"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: necessary spectral and Jordan constraints for the fixed normalized adapter pencil
scripts:
  - tests/channel-swings/k2202_ordered_clifford_adapter_consequences_probe.py
---

# K2202 Ordered Clifford adapter consequences

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2202 universal chiral alternating-pencil and paired-Jordan necessary constraints
carrier: full real Cl77 S128 vector-spinor plus scalar; auxiliary faithful complex normal Cl10 module32 LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic Chevalley bilinear pairing on normal module; no physical Hilbert pairing ON=declared_carrier
real_structure: real Cl46 normal Clifford algebra with quaternionic anti-linear module structure
grading: normal chirality16+16; full physical Dirac carrier retained
action_owner: repository-construction: fixed simple-contraction coupled operator
target: necessary spectrum and Jordan structure of normalized adapter pencil MAP-TYPE=intertwiner
```

## Result and scope

For every nonzero candidate of K2169, the ordered invertible pencil
P=7v-15iu and Y=P^-1 bar(P) has a stronger invariant than a squared
characteristic polynomial: on EACH normal chiral16-dimensional half, every
Jordan block size at every eigenvalue occurs an even number of times.
Neither commutation nor anticommutation of the ports is assumed. This removes
possible generalized-pencil Jordan types, including types with even algebraic
multiplicities that the Pfaffian determinant alone cannot reject.

This is a necessary structure theorem, not a noncommuting class exhaustion,
not a solution of all ten original rows, and not a smaller faithful Clifford
representation. The Chevalley form below belongs to the normal Cl10 module;
it is not the Spin8 pairing or a physical positive pairing. SC-OP-04 ASSERTS
candidate four-field grammar, not these normalized adapters; SC-GEO-55 ASSERTS
rotated-LC displacement, not ordinary torsion. Source/full16cell/full20/K-C,
physical quotient, native2+1/chirality, ledger0.263 and canon remain unchanged.

Here v=I_N w is the real normal grade-seven port and u the real normal
grade-three port. We work on tangent volume eigenvalue +i; the other tangent
half is its conjugate. This is the faithful normal reduction of K2169, not a
replacement of its full real128 carrier.

## 1. The correct normal pairing

Use the faithful complex normal Cl10 module S=Lambda* C5, dimension32, with
even and odd halves S+,S- of dimension16. Its Chevalley pairing is

    B(alpha,beta)=[reverse(alpha) wedge beta]_top.

B is symmetric: the reversal sign in dimension5 is (-1)^(5*4/2)=+1.
It pairs opposite parity because the top degree is odd. Clifford vectors
are self-adjoint for B. Reversion has sign -1 in degrees3 and7, so v,u,P
and bar(P) are B-skew-adjoint. P and bar(P) are odd.

Invertibility of P is K2169's necessary result, not an extra hypothesis
discarding a singular branch. Define, on each half,

    Omega_pm=(B P)|S_pm,    Y_pm=Y|S_pm.

The products BP and B bar(P) preserve parity as bilinear forms and are
alternating. Their restrictions Omega_pm are nondegenerate because P is
invertible and B pairs the two halves nondegenerately. Since

    Omega_pm Y_pm=(B bar(P))|S_pm,
    Y_pm^T Omega_pm=Omega_pm Y_pm,

Y_pm is self-adjoint for an alternating, not positive or Hermitian, form.
It follows immediately that det(zI-Y_pm) is the square of the degree8
monic polynomial Pf(Omega_pm(zI-Y_pm))/Pf(Omega_pm).

## 2. Jordan structure, including nonsemisimple pencils

Generalized eigenspaces at distinct eigenvalues are orthogonal for Omega:
the usual Bezout identity for their relatively prime primary polynomials,
and self-adjointness, prove this without diagonalization. Each primary
space therefore has nondegenerate alternating restriction. On one primary
space let N=Y-lambda I. For k>=1 form

    U_k=ker N^k /(ker N^(k-1)+N ker N^(k+1)),
    b_k([x],[y])=Omega(x,N^(k-1)y).

This form is well-defined and alternating because N is self-adjoint.
Its radical before quotient is exactly the displayed denominator:
the condition N^(k-1)x in (ker N^k)^perp=im N^k gives
x=Nz+a with a in ker N^(k-1), and N^(k+1)z=0 follows from x in ker N^k.
Thus b_k is nondegenerate. The dimension of U_k equals the number of
Jordan blocks of size EXACTLY k. Every such number is even.

In particular, one size2 block and fourteen size1 blocks at the same
eigenvalue on a chiral16 space is impossible, despite total multiplicity16.
Conversely paired size2 blocks are allowed: if J2(lambda) is a Jordan block,
diag(J2(lambda),J2(lambda)^T) is self-adjoint for
[[0,I2],[-I2,0]]. The theorem does not assert semisimplicity.

The monic degree8 Pfaffian polynomial annihilates each chiral block:
at any eigenvalue its exponent is half the total algebraic multiplicity,
at least the largest block size because each size occurs in pairs.
Consequently the full Y has an annihilating polynomial of degree at most16,
the product of the two chiral Pfaffian polynomials. This is an annihilator
bound, not a claim of a faithful16-dimensional representation.

## 3. Reality gives reciprocal-conjugate transport

Real Cl(4,6) has a quaternionic anti-linear module structure J with J^2=-I
commuting with its real Clifford elements. The real normal volume I_N has
square -I. J exchanges its +i and -i eigenspaces, which are the two chiral
halves. Since J fixes real v,u and conjugates i,

    J Y J^-1=bar(Y)=Y^-1.

Thus a size-k Jordan block at lambda in one half is transported to a
size-k block at 1/conjugate(lambda) in the other. All eigenvalues are
nonzero. Nothing here implies unit modulus, a positive metric, or equal
same-eigenvalue multiplicities across halves.

K2195's anticommuting (v,t) sector, where the underlying trivectors obey
[w,u]=0, had a further odd intertwiner commuting with its ratio X=w^-1u
(distinct from the current Y), proving equal same-eigenvalue chiral multiplicities. That
argument must be supplied afresh before claiming full multiplicity four
for the general ordered pencil.

## 4. Abstract control of the inference limit

The following is an ABSTRACT paired-pencil control, not an asserted real
normal3/7 port. Let Omega=diag(J2,...,J2), J2=[[0,1],[-1,0]], with eight
blocks, and D=diag(2I2,3I2,...,9I2). Put

    B=[[0,I16],[I16,0]], C=[[0,I16],[-I16,0]],
    P=[[0,-Omega D],[Omega,0]], bar(P)=C conjugate(P) C^-1.

C followed by conjugation has square -I and exchanges chirality;
BP and B bar(P) are alternating. Direct multiplication gives
Y=diag(D,D^-1), so each full32 eigenvalue has multiplicity exactly TWO.
This proves that the universal paired-pencil properties alone do not
imply fourfold multiplicity. It does NOT prove that a real normal3/7
Clifford port realizes this example, nor disprove a separate stronger
theorem for those ports. No abstract control is promoted into a port.

## Verification and next condition

The probe builds the explicit32-dimensional Fock representation at signature
(4,6), checks the symmetric opposite-chiral pairing, all vector relations,
all120 grade3 and120 grade7 skew-adjoint identities, and the quaternionic
real-structure signs. An actual K2197 genuinely noncommuting port checks
the derived alternating forms and ordered Y identities. Abstract positive,
Jordan, and non-fourfold controls are separately labeled. Actual sign and
matrix faults must fail after a green baseline. These finite controls check
the construction; the quotient-form proof supplies the universal theorem.

Further general noncommuting work must combine these restrictions with
K2197's ordered Euler identities or all ten original rows. Those equations
do not permit simultaneous triangularization of A,B,Y merely because
Y itself has paired Jordan blocks. No class-exhaustion or GU verdict follows.
