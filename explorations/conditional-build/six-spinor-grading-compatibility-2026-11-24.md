---
title: 'Scoped exclusion: the six-spinor principal grade conflicts with retained torsion'
status: exploration
doc_type: structural-result
created: '2026-11-24'
program_target: X-P1-P2-P3
tier: T1
expected_delta: Decide the preregistered F16-K95-spectral/R6-Bn0 same-grade extension test
actual_delta: The R6-Bn0 K95 tangential reconstruction has no same-input/output grade descending to its
  full six-spinor observation with horizontal chi_H. Principal equations force a unique parallel receiver
  grade; retained NW torsion gives an injective128-spinor anticommutator witness. This excludes the last
  F16 spectral choice and any hidden-grade or kernel-preserving-shear repair of this same realization.
  The already-held constant chiral-W wrapper preserves the obstruction. It does not exclude source effective
  chirality or class C. Localization native transfer and normal-L2 necessity remain unestablished; its
  short applicability audit is complete without promotion.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: F16-K95-SPECTRAL-R6-BN0-GRADED-EXTENSION
canon_verdict_change: none
target_claim_verdict: EXCLUDED_IN_DECLARED_RECONSTRUCTION
review_status: two specialist reviews plus hostile source review and Lean core
bears_on:
- SC-OP-04
- SC-OP-05
---

# Six-spinor principal grade versus retained exterior torsion

Root exact controls and Lean core pass; independent mathematical and hostile
source review are recorded in the linked review receipt. This is internal Tier1 acceptance at the
named reconstruction scope, not external certification. Base `d1cc9825ef3aaf18f7bf5c515a9e3b8302c53a0b`.
The owner preregistered `six-spinor-grading-scope-2026-11-24.md` before this
calculation. Its exact carrier, operator, pairing and exhaustion boundary
remain in force. No new action, connection or normal jet has been constructed.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.


program_target: X-P1-P2-P3
tier: T1
expected_delta: Decide exact F16-K95-spectral/R6-Bn0 extension, with no whole-class claim
actual_delta: Scoped graded-realization exclusion; unique principal grade has a nonzero retained-torsion defect

```gu-typed-objects
result: No same-field/equation odd grade descending with the prescribed horizontal chirality for R6-Bn0
carrier: raw E1920 to observed full6S rank768 with hidden K1152; actual K95 symmetric-metric normal geometry LAYER=ambient+observed BRIDGE=declared-coherent-jet-observation-quotient CHIRALITY=S-FULL-DIRAC
pairing: inherited K95 skew-sharp law; impossibility holds even without requiring that law ON=declared_carrier
real_structure: full complex K95 spinors, quaternionic reality separately checked at symbol level; K77 not inferred
grading: same input/output zero-order grade, actual observation descent, pi_b G_o=chi_H pi_b; arbitrary lower blocks allowed
action_owner: repository-construction -- stable zero-SE two-channel exterior tangential operator, not selected source action
target: F16-K95-spectral/R6-Bn0 graded extension MAP-TYPE=intertwiner
```

## 1. Exact result and scientific ceiling

For the existing K95, zero-SE, `c0=-a/12`, `a e g != 0`, `B_n=0`,
coherent-normal-jet, density-repaired exterior reconstruction, there is **no
same input/output zeroth-order grading** which preserves the observation
kernel, descends to a six-spinor receiver grade with horizontal output
`pi_b G_o=chi_H pi_b`, and anticommutes with the full tangential operator.

The principal coefficients force a unique observed grade. That grade is
parallel for the already-held coherent connection. Its anticommutator with
the retained NW exterior torsion has a rank128 injective witness. Hence
allowing the grade to vary does not repair the contradiction.

This closes the proposed extension of the last of the sixteen spectral-sign
hidden choices. In fact the observed obstruction is independent of which
hidden grade is chosen, and of a kernel-preserving off-diagonal shear. More
hidden spectral projectors alone cannot repair this same operator/readout.
This is not exhaustion of all source operators, gradings, reductions, or
physical weak-chirality realizations. SC-OP-04/05 retain candidate strength and operator rivals. SC-CHI-01/04/51/52
describe a qualified effective physical split without selecting this exact
operator anticommutation criterion. SC-META-56 separately concerns an
odd-action demand for the graded-group construction; it is not itself a
theorem about fermion-chirality anticommutators.

## 2. Complete six-spinor principal symbol in orthogonal coordinates

Write `H` for Lorentz four-space, `N` for the native trace-reversed normal
ten-space, `S` for the full complex K95 spinor (rank128). Keep raw
`E=(H*+N*) tensor S + S`, rank1920, and the actual augmented observation
`q=(b=P_H zeta,tau=Gamma_Y zeta,nu)`, rank768. Its kernel K has rank1152.
This is not the canonical rank1664 RS carrier with observed4S.

Use `sigma=tau-Gamma_H b`, so the canonical orthogonal lift is
`(b+J_N sigma/m,nu)`, m=10. Put `c=c_H(xi)`, `i=i_xi`, h=4, n=14.
Transforming the existing full symbol, without dropping the independent
trace or scalar, gives

```
D_xi = [ T_H(xi)                    -a xi-c0 J_H c       e xi ]
       [ m c0(i-c Gamma_H)          -(a+m c0)c           0    ]
       [ g i                       0                    0    ],

T_H(xi)=a(c I-xi Gamma_H)+c0 J_H(i-c Gamma_H).
```

All entries are operators on the indicated spinor or one-form-spinor slots.
Only the structural relation c0=-a/12 is fixed, not a numerical action.
The previous symbol result owns its invertible time coefficient and stable
full6S principal behavior; these are inputs, not new credit.

## 3. Principal uniqueness allows arbitrary endomorphism blocks

Horizontal chirality anticommutes with horizontal Clifford multiplication
and commutes with every normal Clifford generator. Thus

```
G_0 = diag(chi_H on b, -chi_H on sigma, -chi_H on nu)
```

anticommutes with every displayed principal coefficient: diagonal Dirac
terms are horizontally odd, while the maps between b and the two scalar
slots have even horizontal Clifford degree and opposite grade signs.

Now allow a completely arbitrary linear receiver endomorphism G_o satisfying
only its prescribed b output. In particular its lower rows may contain
arbitrary endomorphisms of the full128-spinor module, maps from all b
components, and trace/scalar mixing. Set R=G_o-G_0. Its b row is zero.
The b row of `{D_xi,R}=0` is precisely

```
(-a xi-c0 J_H c_xi) R_sigma + e xi R_nu = 0.       (1)
```

Choose a nonnull horizontal xi and a nonnull horizontal output vector v
perpendicular to xi. Evaluating (1) in that output slot yields

```
-c0 c_H(v)c_H(xi) R_sigma = 0.
```

Both Clifford factors are invertible and c0 != 0, so the **entire map**
R_sigma vanishes. Equation (1) then gives R_nu=0 because e != 0 and xi is
nonzero. Therefore `G_o=G_0`. This proves uniqueness before imposing
involution, adjoint, reality, or any scalar-on-spinor ansatz. One time
covector and one perpendicular space slot already suffice.

Since Gamma_H anticommutes with chi_H, the same grade is
`diag(chi_H,-chi_H,-chi_H)` in the original `(b,tau,nu)` coordinates too.

The actual K95 law is `chi_H^sharp=-chi_H`, not self-adjointness in a
positive norm. The canonical orthogonal receiver pairing is block diagonal
in `(b,sigma,nu)`, with nonzero scalar multiples of the spin pairing on its
last two entries. Thus G0 satisfies the inherited skew-sharp law, G0²=I,
and the existing quaternionic relation `C G0=-G0 C`. It is a Krein
anti-isometry; no positive-Hilbert physical symmetry is inferred.

## 4. Retained NW torsion on the same observed carrier

The density repair cancels the SW correction on all one-form inputs. It
does not change the exterior NW term. At B_n=0 that term depends only on b.
Write its contraction before Phi in horizontal/normal form slots as

```
C_H(b)(X) = -sum_r eta_r c_N(n_r) b(S_(n_r) X),
A_II(b)(n) = sum_mu eta_mu c_H(e_mu) b(S_n e_mu),
F(b) = Gamma_N A_II(b).
```

For a non-normalized orthogonal normal frame, eta_r here means its inverse
metric coefficient. Clifford anticommutation and symmetry of the mixed
torsion form give the exact identities

```
Gamma_H C_H(b)=F(b),
Gamma_Y C(b composed T_B)=2 F(b).
```

Consequently, with L=2a+n c0,

```
V_o(b,sigma,nu)
  = (a C_H(b)+c0 J_H F(b), (a+m c0)F(b), 0),

(V_o)_tau(b) = L F(b).                              (2)
```

At the held stable locus, a+m c0=a/6 and L=5a/6. The b output in (2)
commutes with chi_H, whereas F has odd horizontal Clifford degree. Hence
the nonzero observed torsion is **even** for the forced G0, in conflict
with the requested oddness. The following witness proves it is nonzero
on the actual source-reconstructed shape, without a genericity assertion.

## 5. Exact native witness and coordinate check

Take b=J_H psi, meaning b(X)=c_H(X)psi, with sigma=nu=0. This is an
allowed pure-horizontal raw input: its original total trace is tau=h psi.
The shape operators are g-selfadjoint, so contraction cancels their
Clifford bivector part:

```
A_II(J_H psi)(n)
   = sum_mu eta_mu c_H(e_mu)c_H(S_n e_mu)psi
   = tr(S_n)psi
   = <H_mean,n> psi.
```

Thus `F(J_H psi)=c_N(H_mean)psi`. The already-owned native geometry has
`S_n=-(1/2)g^-1 n`, `H_mean=t/2`, `t²=-4`, so H_mean²=-1. Normal
Clifford multiplication by H_mean is invertible. Substitution into the
observed grading defect gives

```
({G0,V_o}(J_H psi,0,0))_sigma
     = -(a/3) chi_H c_N(H_mean)psi,

({G0,V_o}(J_H psi,0,0))_tau
     = -(5a/3) chi_H c_N(H_mean)psi
     = -(5a/6) chi_H c_N(t)psi.                      (3)
```

The different coefficients are required: the total-trace defect also
includes Gamma_H of the b-row defect, since tau=sigma+Gamma_H b. The
exact probe verifies both and this coordinate transport. Each displayed
map is injective on a full128-spinor input because a != 0, chi_H²=I and
c_N(H_mean)²=-I. Hence the complete anticommutator has rank **at least128**
at the point; this is not a claim that its full rank is128.

## 6. Variable grades, hidden freedom, and the precise exclusion

Principal uniqueness is pointwise and forces the same geometric G0 at every
point. The coherent split-preserving metric/spin connection preserves
chi_H, Gamma_H and the split, so nabla'G0=0. Thus the derivative-of-grade
term in `{D_coh,G0}` vanishes; it cannot cancel (3). The contradiction is
a full tangential differential one for the held connection and coherent
normal-jet prescription, not merely a frozen-symbol failure.

More generally suppose a grade G on raw E preserves K and descends through
q to G_o, while the already-repaired operator satisfies qD=D_o q. Then

```
q{G,D}={G_o,D_o}q.
```

Surjectivity of the algebraic receiver implies that full oddness requires
observed oddness. The latter is impossible by (1)–(3), regardless of the
hidden grade A or a kernel-preserving shear into K. This observation prevents
mistakenly scheduling a larger hidden commutant as a repair of the same
obstruction. In particular the surviving A=+chi_H from F16 fails here.

The theorem does **not** require an identification of the full source barred
fields with metric duals. Conversely it does not show that this same
input/output anticommutation is a source obligation. Distinct field and
equation grades, a different observation receiver or kernel, a different NW
completion/connection/jet prescription, a source-selected extra lower term,
or a different physical effective construction change the hypotheses.
Their viability is not established by naming them. K77 requires its own
carrier, pairing and reality; no K95 transfer is made. Global domains,
stationary solutions, family counts and class-C emptiness remain undecided.

## 7. Recorded follow-through: the held constant chiral W does not repair the defect

This corollary was separately scoped in the owner document before its
calculation. It uses only the existing constant wrapper from
`source-symbol-quotient-membership-2026-11-12.md` §7, the same zero-SE
operator and the same retained torsion. It introduces no variable W,
independent chiral weights, current, new action or lower completion.

Let Ω denote the existing ambient spinor chirality, Ω²=I, and put

```
W=(3−Ω)/2,       Wbar=(3+Ω)/2,
W^-1=(3+Ω)/4,   Wbar^-1=(3−Ω)/4.
```

Both are invertible and parallel for the held compatible spin connection.
Clifford contraction obeys `Gamma W=Wbar Gamma`. The wrapped raw operator
has NW `T W`, NE `e d_A`, SW the existing repaired divergence, and zero SE;
T includes the retained exterior torsion term. The already-owned row/field
identity is

```
D_0 = L D_W F^-1,
F=diag(W on zeta,I on nu),   L=diag(I on zeta,W on nu).
```

Parallel W is essential for this differential identity: no derivative of W
has been discarded. These left/right changes are not a unitary similarity
and do not by themselves justify any statement about one common grade.

### Actual observation transport

On the same receiver `(b,sigma=Gamma_N zeta_N,nu)`, the induced maps are

```
F_o=diag(W on b,Wbar on sigma,I on nu),
L_o=diag(I on b,I on sigma,W on nu),
D_0,o=L_o D_W,o F_o^-1.
```

The original total trace tau also transforms by Wbar. Thus reconstructing
the old observations from new fields requires `b_old=W^-1 b_new` and
`tau_old=Wbar^-1 tau_new`, exactly as the prior source-symbol result states.
Using W on both trace and one-form slots would be incorrect.

The ambient chirality Ω commutes with horizontal chirality chi_H. Therefore
both F_o and L_o commute with the uniquely forced receiver grade
`G0=diag(chi_H,−chi_H,−chi_H)`. On the full raw carrier with hidden
A=+chi_H, its normal-form extension uses only chi_H and the even projector
`P_K=I−J_N Gamma_N/10`, so it also commutes with the slotwise W transforms.
No isometry or identification of independent bars has been assumed.

### Do not assume arbitrary grades transport: recheck uniqueness

The wrapped b-row principal blocks are

```
[ T_H W,  (-a xi-c0 J_H c_xi) Wbar,  e xi ].
```

G0 is principal-odd because it commutes with both transformation matrices.
For any competing same-input/output G_o with the fixed horizontal output,
set R=G_o−G0. As before R has zero b row. The perpendicular output of the
principal anticommutator yields

```
-c0 c_H(v)c_H(xi) Wbar R_sigma=0.
```

The extra Wbar is invertible, so R_sigma=0, then R_nu=0. Thus G0 is again
the unique observed principal grade even allowing all spinor endomorphism
blocks and mixing. No inference from a left/right equivalence to arbitrary
same-grade equivalence is needed.

For that forced grade the differential defect transports exactly:

```
{G0,D_W,o}=L_o^-1 {G0,D_0,o} F_o.
```

Use the transported input `b_old=W^-1 J_H psi`, sigma=nu=0. The trace
output of L_o is unchanged, so its defect is exactly the previous
`−(5a/6) chi_H c_N(t)psi`, still injective on128 spinors. Parallelness of
G0 and W preserves the derivative argument. The same quotient obstruction
remains, independently of the hidden sign or a kernel-preserving shear.

**Outcome:** this held constant-W wrapper is not an unresolved repair of
the existing same-grade six-spinor test. Do not schedule it as though the
original obstruction ignored the already-owned weight transport. General
variable wrappers, independent chiral weights, distinct field/equation
grades, and the source's four-field action/current compatibility are not
covered or certified by this corollary. The missing physical-necessity
bridge remains missing.

The probe addition checks the exact native Clifford volume normalization,
W and Wbar inverses, crossed contraction, all four wrapped principal
coefficients, the uniqueness block inverse, row/field identity, full
observed defect transport, and both transported coordinate witnesses.

## Reproducibility and controls

`tests/program-focus/six_spinor_grading_compatibility_probe.py` uses exact rational Clifford words and the
already-owned native normal symmetric-matrix basis. It checks all four
principal coefficients, the invertible perpendicular uniqueness block,
wrong-sign principal failures, native torsion identities, t²=-4, both
coordinate witnesses and exact inverses. Omitting NW torsion is an explicit
false-positive control. No floating rank, selected action, or new large
native matrix elimination is used. The analytic uniqueness proof covers
arbitrary endomorphism blocks and all admitted coefficients, beyond the
probe's rational coefficient control. Root serialized execution: all40 exact controls pass, including the held constant-W observation and defect transport.


## Acceptance and continuation

The [scope](six-spinor-grading-scope-2026-11-24.md) was recorded before
calculation. Two specialist mathematical reviews and a separate hostile
source/domain review support the exclusion. Root serialized the exact probe
and `lake env lean Lean/GUFormalization/SixSpinorGrading.lean`; both pass.
The Lean core checks residual-row annihilation, complete receiver uniqueness,
oddness through a surjective quotient, witness injectivity and the scalar
relations. Geometry, Clifford identities and connection parallelism are
explicit supplied premises, proved in this artifact and checked by exact
controls; the full geometric theorem is not claimed as Lean-formalized.

[Machine receipt](../../lab/process/six-spinor-grading-compatibility.json),
[Lean core](../../Lean/GUFormalization/SixSpinorGrading.lean),
[reviews](../../lab/process/hostile-reviews/2026-11-24-six-spinor-grading-review.md).

All18 matrix cells remain constrained and the joint intersection open.
There is no source/physics-ledger, class-C, canon or prediction change.
The [localization applicability audit](localization-applicability-audit-2026-11-24.md)
found neither promotion premise established. Its prior brief relied on
W175's now-withdrawn native gap; the positive comparison theorem is retained.

The next structural enlargement tests admitted metric normal-connection
extensions with the complete observation and exterior equations. Changing
only hidden sign projectors cannot remove this observed defect. A different
source field/equation transformation or current law is a separate hypothesis,
not automatically a repair or a source requirement to fabricate.
