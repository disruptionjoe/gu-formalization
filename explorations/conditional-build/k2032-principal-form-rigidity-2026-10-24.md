---
title: "K2032: Full principal-form rigidity and the constant-weight boundary"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed raw principal-form classification and weight/descriptor boundary; no source physical quotient
scripts:
  - tests/channel-swings/k2032_principal_form_rigidity.py
  - tests/channel-swings/k2032_principal_form_rigidity_probe.py
---

# K2032: Full principal-form rigidity and constant weights

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: full principal centralizer, compatible forms and singular-weight nonuniqueness
carrier: real1920 raw K77 and full128 spinor, observed covectors0,7,8,9 LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: arbitrary constant real symmetric full form compatible with all14 raw symbols ON=declared_raw_carrier
real_structure: fixed real Cl(7,7), not a source-selected bar
grading: raw form degree and Clifford halves, not observed physical chirality
action_owner: repository-construction -- fixed zero-southeast principal candidate
target: full formal principal adjoint and well-posedness necessary conditions MAP-TYPE=intertwiner
```

## Result and scope

[Verified conditional algebra.] The common centralizer of all fourteen raw
principal matrices from [K1951](k1951-coordinated-zero-southeast-principal-2026-10-22.md)
is exactly the real scalars. Consequently **every nondegenerate constant real
symmetric full form** making those matrices skew-adjoint is a nonzero scalar
multiple of the inherited H, with inertia(960,960). This closes full-form
retuning for this fixed principal construction, beyond
[K2030](k2030-positive-metric-rescue-2026-10-24.md)'s classification of positive
metrics on its128 core. It is not a positivity theorem for a physical quotient.

A second result eliminates **every constant invertible128-by128 weight W**
in the triple-gamma block, not just diagonal half weights, as a repair of the
principal Jordan defect. Singular W is a genuinely different descriptor system;
we exhibit arbitrary-time, zero-initial-data solutions even after quotienting
its entire algebraic common kernel. A differential gauge equivalence could
remove these examples, but that equivalence and its physical interpretation
have not been supplied by the source.

SC-OP-04 **ASSERTS** candidate four-field grammar; SC-OP-05 remains **UNCERTAIN**
about an unselected southeast rival; SC-META-53 remains **UNCERTAIN** on physical
positivity; SC-META-56 **DISAVOWS** an odd-action prerequisite. These statements,
LT-SM8/LT-GR6b, source register and canon remain unchanged.

## 1. Recovering every raw field slot from principal matrices

Write the raw matrix as Dk=[[Tk W,dk],[-dk*,0]], with
W=(3I-volume)/2=Pplus+2Pminus, eta=(+1 seven times,-1 seven times), and
Tk's(r,c) block eta_r gr gk gc for r!=k, c not in{r,k}. The offdiagonal
blocks are identity spinor maps with the displayed signs. H is block diagonal
with blocks eta_r B on the14 one-form slots and B on the auxiliary slot,
B=g7...g13. K2021's formal identity is Dk^T H+H Dk=0.

Let Qk=eta_k Dk^2. The kth/auxiliary pair has Qk=-I. On the other13 slots,
conjugate by diag(eta_r gr). The block matrix becomes

    (J13-I13) tensor (gk Wbar),  Wbar=(3I+volume)/2,
    (gk Wbar)^2=2 eta_k I.

Since J13-I13 has eigenvalues12 and-1, Qk has only2 and288 on those slots.
Thus, on the full carrier,

    (Qk+I)(Qk-2I)(Qk-288I)=0,
    Ek=(Qk-2I)(Qk-288I)/867=Pk+Paux.                 (1)

The producer checks(1) directly for every k. The separate replay checks all2184
nonzero transverse blocks by signed-bit Clifford arithmetic and the symbolic
13-slot identity, independently of the large-matrix multiplication.

Any matrix commuting with every Dk commutes with Ek. Summing gives
sum Ek=I+13Paux, hence it commutes with Paux and with every Pk.
It is therefore block diagonal. Commutation with dk and -dk* forces all fifteen
spinor blocks to be the **same**128-by128 matrix X.

## 2. The full centralizer and every compatible form

The remaining equations say X commutes with every gr gk gc W on distinct
indices. Choose k,c different from0,j. The ratio of two such invertible blocks is

    (g0 gk gc W)(gj gk gc W)^-1 = eta_j g0 gj.         (2)

These13 even Clifford generators have commutant span(I,volume). This familiar
Clifford conclusion is also certified here without assuming irreducibility:
conjugation by their signed-permutation matrices gives signed equations on all
16384 matrix units. The complete orbit traversal leaves precisely two independent
solutions, the diagonal half projectors. Their span is checked against I,volume.
One invertible odd triple block anticommutes with volume. Commuting with that
block forces the two half scalars equal. The full common centralizer is R I.

For any candidate full symmetric form H', write H'=H X since H is invertible.
Using Dk^T H=-H Dk gives

    Dk^T H'+H'Dk=H[X,Dk].                             (3)

Thus H'=aH, and nondegeneracy is exactly a!=0. This proves completeness even for
forms mixing all1920 coordinates; it is not a block-diagonal ansatz. H has equal
positive/negative inertia because B is a symmetric involution with zero trace.
Both signs of a preserve(960,960).

The consequence for lower-order work is immediate: H'K-K^T H' equals a times
the previously tested defect. No failed raw common-return coefficient becomes
compatible by a different constant full form satisfying the same fourteen
principal equations. K2028's complete coefficient classification and K2030's
positive-core obstruction therefore survive this repair class. We reuse those
certificates rather than recount their grade census as new verification.
A form satisfying only the three observed evolution equations is a different
problem; the present rigidity hypothesis explicitly includes all14 Dk.

## 3. Every invertible constant triple-gamma weight

Now replace W by an arbitrary invertible real128-by128 matrix, with no Clifford
commutation assumption. Put

    S=diag(I14 tensor W^-1,I), R=diag(I14,I_aux tensor W).
    R Dk(W) S=Dk(I), for every k.                     (4)

The offdiagonal identity blocks prove(4) directly. This is a left-right pencil
equivalence, not a congruence preserving the same H. Since D0 is invertible,

    D0(W)^-1 Di(W)=S[D0(I)^-1 Di(I)]S^-1.              (5)

All observed evolution generators are simultaneously similar. The cyclic
auxiliary carrier is transported because S fixes the auxiliary seed. Thus the
640-dimensional carrier, genuine Jordan chains and one-derivative loss from
K1951 persist for every fixed invertible W. A change of the full formal form
under(4) is not a physical positive-energy repair. Noncommuting W controls are
included; restricting the argument to scalar half weights would miss its scope.

For a smooth invertible W(x), equation(4) holds pointwise at principal order.
Leibniz contributes sum Dk(W) partial_k S. The explicit connection correction

    K_W=-sum Dk(W)(partial_k S) S^-1

makes R[sum Dk(W)partial_k+K_W]S exactly sum Dk(I)partial_k.
Omitting this term changes the operator. Local bounded smooth coordinate maps
do not remove the frozen principal Jordan defect; no global equivalence is
asserted without uniform invertibility and the relevant domain. This is a
necessary distinction, not a newly selected source connection.

## 4. Singular weights are constraints, not a successful repair

Let rank W=r and q=128-r>0. At time covector0, the kth/auxiliary pair has rank256.
The transverse13-slot block is Tk(I) times diag(W,...,W); Tk(I) is invertible
by the explicit K1951 inverse at W=I. Therefore

    rank D0(W)=256+13r, dim ker D0(W)=13q.             (6)

Its kernel has nu=0,zeta0=0 and every other zeta_r in ker W. Intersecting with
D7,D8,D9 forces those three slots to vanish as well. Consequently the observed
common algebraic kernel consists exactly of ten unobserved slots in ker W,
with dimension10q. This conclusion holds for arbitrary singular W, not only a
half projector. Both W=0 and a rank64 half projector are explicit controls.

Removing that common kernel still does not give a unique Cauchy problem. For
v!=0 in ker W and any smooth scalar f(t,x7,x8,x9), set

    zeta7=(partial_8 f)v, zeta8=-(partial_7 f)v,
    all other zeta=0, nu=0.                           (7)

All triple-gamma terms vanish because Wv=0; the remaining divergence vanishes
by commuting derivatives and eta7=eta8=-1. Choose f compactly supported in
space and in t>0. Then(7) is a nonzero smooth solution with identically zero
initial data, and it is not in the algebraic common kernel because its observed
slots are nonzero. Thus neither the raw system nor that pointwise quotient
admits a unique evolution on these unconstrained fields.

This is a differential identity, not proof of physical gauge. Locally the
kerW-valued observed one-form enters only by its divergence; variations given
by divergence-free fields leave this equation unchanged. One can **choose** to
quotient such variations, but must define an actual complex, observable and
boundary/domain before interpreting the resulting quotient as physical. Nonzero
lower-order couplings can break this identity and create consistency conditions;
(7) is a theorem of the declared zero-order-free principal system only. A
singular W does not authorize silently deleting a Clifford half of the source's
full Dirac carrier.

## 5. Review and next substantive input

The cheap structural test killed invertible weight tuning, and its released
work classified the previously open full-form class and the singular alternative.
The strongest contrary construction is K2026's conservative gapped extension:
it remains possible after relaxing the raw connection tie. Nothing here excludes
it. The strongest hidden assumption is requiring all14 raw principal adjoints;
observed-only or changed-principal forms are outside this theorem. The weakest
reproducibility seam is centralizer completeness; both implementations traverse
every matrix-unit equation, and the note independently gives the Clifford proof.
Actual offdiagonal, weight, half-scalar, curl-sign and omitted-connection faults
test mathematical conditions after a clean baseline; provenance checks are
reported separately. Internal verification is not external acceptance, formal
proof-assistant certification or a novelty claim.

The next source-adjacent question must genuinely change the symbol/offdiagonal
contraction, supply a differential physical constraint and its action/domain,
or relax the fourteen-formal-adjoint requirement with a typed observation bridge.
Another constant full-form or invertible W search would repeat this result.
