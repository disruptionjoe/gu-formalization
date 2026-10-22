---
title: "K1955: Grade-one connection obstruction and rigidity of the positive carrier"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional exact observed connection algebra; no source-selected full20 placement or physical GU verdict
scripts:
  - tests/channel-swings/k1955_grade_one_connection.py
  - tests/channel-swings/k1955_grade_one_connection_probe.py
---

# K1955: Test the grade-one carrier before calling a connection a mass

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
result: grade-one connection realization and positive-carrier rigidity
carrier: conditional real1920 SE0 fields; fixed cyclic640 and positive128 subspace LAYER=toy CHIRALITY=N/A
pairing: fixed K1951 positive energy, or a pointwise positive symmetrizer for the moving-carrier theorem ON=observed_constant_principal_system
real_structure: real rational Clifford representation of signature seven positive and seven negative
grading: total raw spinor-slot chirality used as algebraic parity, not physical chirality
action_owner: repository-construction -- common grade-one connection coefficient ansatz
target: invariant massive observed dynamics MAP-TYPE=intertwiner
```

## 1. The source-motivated question and its limits

[K1953](k1953-spin-connection-stable-mass-2026-10-22.md) tests Spin(7,7)
bivectors. That is not the grade-one Clifford component specifically named
by SC-MAS-02. The source register **ASSERTS**, with the stated “in some
sense” hedge, that the mass-role field lies in a truly-spinless component
of `Lambda^1 tensor Lambda^1` inside the ad-valued one-forms.
[WGS-05](../../lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md)
preserves that statement alongside the stylized curvature mass of
SC-MAS-01 and the three-way linkage of SC-MAS-03. It explicitly leaves the
full20 placement, K/C reality conditions and equality to the scalar-curvature
bundle map unconstructed.

Accordingly, this note tests a specified **conditional observed grade-one
ansatz**, not a source-selected mass realization. The raw operator and its
stable carrier are the changed all-observed-covector SE0 construction of
[K1951](k1951-coordinated-zero-southeast-principal-2026-10-22.md).
SC-OP-04 ASSERTS a candidate four-field grammar, while SC-OP-05 is UNCERTAIN
about an explicitly admitted but unselected nonzero-SE rival. Neither selects the present principal symbol,
observation, barred maps or positive carrier. SC-META-53 remains UNCERTAIN.
LT-SM8, LT-GR6b and AC-F1 remain NEEDS; no source, physics-ledger or canon
verdict changes.

## 2. All56 real observed grade-one coefficients

Let `A_0=I`, `A_k=D0^{-1}D_k` for `k=7,8,9`, and let
`J: R128 -> R1920` be K1951's actual positive injection. Thus
`A_k J=J C_k`, and `LJ=I` for the declared pivot left inverse L.
Take independently in each observed direction

    Omega_k = sum_(a=0)^13 x_(k,a) gamma_a,
    V(x) = sum_k A_k (I15 tensor Omega_k),
    M(x) = L V(x) J,
    E(x) = V(x) J - J M(x).                            (1)

The same spinor coefficient acts in all14 one-form slots and the auxiliary
slot. This is a56-dimensional real linear class. No claim that it is a
closed Lie algebra, a selected ambient gauge group or the actual full
source connection is needed for the test.

**Exact result:** `E(x)=0` implies `x=0`. The report gives56 selected
entries of E, forming a rational56-by56 matrix B with an explicit inverse.
The independent checker rebuilds the Clifford matrices by signed bit flips,
reconstructs the actual raw coefficients and core, checks the time inverse,
and verifies `B^{-1}B=I`. This proves injectivity for every real x, not a
numerical-rank or random-sampling statement. No mass or energy equation is
needed once invariance fails.

The exact certificate also gives

    ||B^{-1}||_infinity = 185948/495,
    max_selected |E(x)| >= (495/185948) max_(k,a)|x_(k,a)|.  (2)

The norm is tied to these coefficient coordinates and chosen residual
entries. It is not a physical energy norm. The observed trace seed
`Omega_k=eta_k gamma_k`, `k=0,7,8,9`, has an explicit nonzero residual in
the report. This seed is a restricted observed analogue; its failure is
not a calculation of the full ambient source spinless projection.

Since (1) is algebraic with constant J, arbitrary spacetime-dependent real
coefficients obey the same obstruction pointwise, and almost everywhere
for measurable coefficients where the multiplication equation is defined.

## 3. Even and odd connections cannot repair one another here

Write `omega=gamma_0 ... gamma_13` and define the total raw involution

    T = diag(omega,...,omega,-omega),                  (3)

with14 positive one-form slots and one negative auxiliary slot. The raw
D_k anticommute with T: their northwest Clifford terms are odd, while their
identity off-diagonal blocks change the slot sign. The weight W commutes
with omega. Consequently every `A_k=D0^{-1}D_k` commutes with T.
The actual core obeys `TJ=Jt`, `t^2=I`; these identities are checked exactly.

The spinor grade-one actions anticommute with T. Spin bivectors commute with
T, as does K1953's explicitly defined covector-spinor action. Because T
preserves K=im(J), it acts on the raw quotient R1920/K. On maps from K to
that quotient, `F -> T_quot F t` is an involution. The even and odd leakage
maps lie in its opposite eigenspaces. Their sum can vanish only if each
vanishes separately. This reasoning uses the quotient by K, not an
assumption that the pivot projection JL commutes with T.

It follows that the mixed common-spinor class with56 grade-one plus364
Spin-bivector coefficients has injective leakage: all420 coefficients must
vanish. This is an analytic composition of the two exact certificates,
not a newly enumerated420-column rank computation.

For the mixed class using the K1953 tensorial bivector action plus these
spinor grade-one terms, invariance again forces all56 odd coefficients to
zero. Adding the Dirac anticommutation equations then leaves precisely the
five zero-action directions already proved in K1953, with no nonzero mass.
Its conservative internal rotation remains a valid nonmass control; no
claim excludes all tensorial potentials.

## 4. A moving frame cannot move the maximal positive carrier

The remaining qualifier in K1953 about moving subbundles can be narrowed
within the SAME fixed cyclic640 system. Let `J(x)` be a C1 rank128 injection
into that cyclic carrier, invariant under every fixed A_k. Suppose its
restricted principal matrices admit a pointwise common positive symmetrizer;
the symmetrizer may vary with x and need not be the stored H.

K1951 proves the quartic identity
`[A(xi)^2-|xi|^2 I]^2=0` on the cyclic carrier. On a positive symmetrizable
restriction, self-adjointness forces every defect coefficient to vanish.
The invariant common defect kernel is exactly K of dimension128. Thus
`im J(x)` is contained in K and, by dimension, equals K at every point.
Locally `J(x)=J0 G(x)` with G invertible, where J0 is the constant stored
injection. In particular every derivative of J has image in K.

For `partial_t f=sum A_k partial_k f+V f`, substitution `f=J(x)u` gives
the extra lower-order term `sum A_k partial_k J-partial_t J`. That entire
term is tangent to K. Its image in the raw quotient by K is zero, so it
cannot cancel the leakage of VJ. Since G is invertible, zero leakage on
J is equivalent to zero leakage on J0. The grade-one and mixed
common-spinor RAW leakage exclusions therefore survive every such moving
frame and pointwise positive symmetrizer. This does not force every
coordinate zeroth-order coefficient to vanish: derivatives of G can create
pure-frame terms. They describe frame-equivalent dynamics, not a new
connection realization. The tensorial mass classification of section3 is
stated in the fixed frame; changing both principal coordinates and their
frame terms is not a new fixed-principal mass certificate.

This theorem does not classify smaller moving subspaces, other positive
carriers outside the fixed cyclic640, moving principal coefficients,
frequency-dependent reductions or source-owned physical cohomology. It
removes only the apparent freedom to move a maximal positive subbundle
inside this already fixed principal system.

## 5. A quotient without the fixed section still needs its parent

One can ask for a quotient of the cyclic carrier without preserving its
positive section. That is a different demand which does not require
preserving the positive section, and is tested separately. Let `Jc: R640 -> R1920` be the stored cyclic
injection, with blockwise pivot left inverse Lc. Parent preservation requires

    Ec(x) = V(x) Jc - Jc Lc V(x) Jc = 0.               (4)

For the SAME56 grade-one coefficients, (4) has21888 nonzero scalar equation
positions and exact rank56. The report supplies a second56-square minor and
its rational inverse, with `||Bc^{-1}||_infinity=102`. Thus
`max_selected |Ec(x)| >= max|x|/102`.
Thus nonzero grade-one coefficients leave the cyclic parent itself. They
cannot define an endomorphism of its quotient by the512-dimensional defect
radical, even when preservation of the positive section is abandoned.
Testing radical preservation, positive energy and mass after this failure
would be redundant for this class.

The auxiliary seed is T-invariant, and the principal evolutions commute
with T, so the cyclic parent is T-invariant too. The same intrinsic parity
argument applies to maps from H640 to R1920/H640: adding even connection
terms cannot cancel this odd grade-one leakage. Parent preservation still
forces the grade-one coefficients to zero in such a mixture. The remaining
even coefficients require their own quotient test.

Common action in all15 slots is load-bearing. A changed-support term
`A_k P_aux (I15 tensor Omega)`, with P_aux the raw auxiliary-slot projector,
always maps into H640: its intermediate output is in the full auxiliary
seed, and A_k preserves the cyclic span. Such auxiliary-only terms therefore
preserve the cyclic parent. The next section resolves radical preservation
and stable-core dynamics separately. This analytic countercontrol
prevents extending (4) to every grade-one raw placement.

This argument is specific to a quotient whose parent is that fixed H640.
It does not classify maps on a different carrier, quotients directly from
raw1920, or differential/nonlocal observations. Nor does it extend the
quotient-parent exclusion to the even bivector class without a separate
calculation.

## 6. Follow-through: auxiliary-only support does not produce the missing dynamics

Use cyclic coordinates in H640, with radical R512, stable section S and
quotient Q as in K1951. Let F extract the RAW AUXILIARY input from that
carrier. This F is not the raw-time-input return denoted F in K1951's
southeast-cell mass construction. In each stored20-dimensional block it is

    F = (raw auxiliary coordinate rows of the cyclic basis),
    E = (pure auxiliary seed expressed in cyclic coordinates).

The new report independently checks on all32 blocks:

    rank(F R)=4,             rank(F S)=4,
    [E, B1 E, B2 E, B3 E, S] is invertible.              (5)

It gives a right inverse for FR, an inverse for FS, and an inverse of the
last20-by20 matrix. These globalize as surjectivity of `F|R` onto R128,
bijectivity of `F|K`, and a direct sum `H640=U512 direct-sum K128`, where
U is the span of the auxiliary seed and its three first principal images.
Arbitrary cross-copy mixing is covered by these global statements.

### Quotient descent for any auxiliary-input-only coefficient

Any cyclic-valued lower-order coefficient supported on auxiliary input
has the form `V=O F`, with `O: R128 -> H640`. If it preserves the radical,
then `Q O F R=0`. Surjectivity of FR forces `QO=0`. Therefore the induced
coefficient on H640/R512 is exactly ZERO. No mass or energy condition is
needed, and O may be arbitrary, not only grade-one or a connection ansatz.
Nonzero O with image in R may survive, but they act trivially on the quotient.

If such a V also preserves K, then `V S` lies in K while `Q V S=0`.
Since Q restricted to K is invertible, `O F S=0`. Bijectivity of FS forces
`O=0`. Both radical and core preservation are required for this last
statement about unrestricted O. Core preservation alone allows, for example,
nonzero O with image in K.

### Stable-core invariance in the observed connection subclass

For the more specific auxiliary-only connection class,

    O = E Omega_0 + B1 E Omega_7 + B2 E Omega_8 + B3 E Omega_9,  (6)

allow the four Omega matrices to be ARBITRARY real128-by128 matrices,
including cross-copy mixing. This is65536 independent real input coefficients;
no Clifford-grade or ambient gauge-group membership is imposed.
Its image lies in U. If V=OF preserves K, then `OFS` lies in both U and K,
so it is zero by(5). Again FS is invertible, hence O=0. The first512 columns
of the global decomposition matrix are independent, so(6) then forces
EVERY Omega_k=0. Thus this particular auxiliary-only observed connection
class cannot produce any nonzero stable-core coefficient, before asking
whether it is a conservative mass.

This is a structural argument from32 small decomposition identities, not
a65536-parameter matrix census. It resolves the changed-support repair
suggested by the cyclic-parent countercontrol. Other raw support, a different
parent or principal system, and unrestricted algebraic mass lifts remain
distinct possibilities. No source operator, physical quotient or mass
mechanism is identified by this conditional obstruction.

## 7. Verification and next genuine freedoms

The computational evidence consists of two exact56-square leakage inverses,
total-chirality identities, explicit trace-seed residual and96 small
auxiliary-support inverse identities across32 blocks. Four actual
connection faults are tested only after the independent raw baseline passes:
missing coefficient action, wrong Clifford generator, wrong covector and
missing auxiliary-slot action. A separate cyclic-parent observed-covector fault
breaks its own independent certificate. Two additional input faults change
the auxiliary projection and a first-principal image in the support certificate.
Identity and digest faults are separate reporting checks. Variable-coefficient,
mixed-parity, moving-carrier and universal auxiliary-support statements use
the stated analytic arguments. This is internal verification, not external
expert acceptance, novelty or proof-assistant certification.

A different raw invariant carrier, additional Clifford grades, a quotient
with a different parent, unobserved-direction coefficients,
changed principal geometry and the source-admitted nonzero-SE rival remain
possible changed premises. The full source spinless projection, barred
pairing/density, source action and physical observable are still unbuilt.
The K1951 unrestricted algebraic mass lift remains valid; the result above
limits these particular connection realizations of it.
