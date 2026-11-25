---
title: Independent chiral wedge weights and observation transport
status: exploration
doc_type: structural-result
created: 2026-11-25
program_target: BET-2PLUS1
tier: T1
review_status: accepted_internal_T1_scoped
result: SCOPED_INTERNAL_NO_GO_FIXED_ADJOINT__WEIGHTED_DENSITY_CLASSIFIED
expected_delta: Complete lower-term observation transport across the owned independent-chiral southeast
  family and classify its existing weighted-adjoint escape.
actual_delta: Complete independent-chiral fixed-adjoint class excluded at H nonzero; weighted-integration-density
  class classified by b=H with all compatible connections. Internal T1 review and conditional Lean core
  pass; no source/GU/matrix verdict.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: CW-SE-FIXED-Q-PAIRED-ADJOINT
class_covered: All nonzero constant real chiral wedge weights in the owned K77 reciprocal southeast family,
  fixed q and LC-normal jets, and every compatible unitary spinor connection; separately its existing
  scalar-density weighted-adjoint extension.
premises:
- Exact autonomy of the contraction-augmented observation q is the tested realization condition; it is
  not proved necessary for effective GU chirality. See lab/sources/source-claim-register.yaml#SC-CHI-04
- Reference normal covariant jets are fixed using Levi-Civita before varying the spinor connection. See
  explorations/conditional-build/source-lower-term-compatibility-2026-11-13.md
- The exterior/form connection, Clifford contraction, uniform Hermitian-Clifford adjoint, and coefficient
  ordering are held fixed. See explorations/conditional-build/source-lower-term-compatibility-2026-11-13.md
- All fourteen unitary spinor connection components are allowed, including chirality-mixing components.
  See lab/sources/source-claim-register.yaml#SC-OP-04
- Weights are constant or LC-parallel in the held T composed with d_A grammar, not parallel for the varied
  connection. See explorations/conditional-build/selected-k77-wedge-shiab-southeast-completion-2026-08-11.md
- No independent new lower-order terms or derivative-of-weight terms are added. See explorations/conditional-build/source-lower-term-compatibility-2026-11-13.md
source_bridge:
  status: conditional
  reason: SC-OP-04/05 authenticate candidate grammar and admit unselected SE rivals; exact off-shell autonomy
    of q and source selection of this paired adjoint are not established necessities for source-effective
    chirality. Source and real-form/domain bridges remain explicit premises.
kill_condition: At nonzero mean curvature no compatible unitary connection cancels the complete normalized
  hidden leakage with the fixed paired adjoint; this kills the named realization class only.
canon_verdict_change: none
matrix_or_ledger_effect: none
target_claim_verdict: Excluded at nonzero H within the declared local realization class; weighted integration-density
  rival survives exactly at b=H.
bears_on: [SC-OP-04, SC-OP-05, SC-CHI-01, SC-CHI-04, SC-GEN-03, SC-GEN-50]
---

# Independent chiral wedge weights and observation transport

> **GU-COMPARATOR-ROUTING — scope before inference.** Read
> `lab/methods/source-native-comparator-routing.md`. This is a class-wide
> conditional operator/observation result, not a GU, class-C, physical-family,
> or emergent-chirality verdict. Its exact observation and fixed-adjoint
> premises are not authenticated as necessary source requirements.
> Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: independent-chiral wedge/SE transport exclusion and complete weighted-adjoint survivor class
carrier: full independent one-form Dirac S128 plus scalar; H4/N10 split and full6S receiver LAYER=ambient+observed BRIDGE=literal-section-plus-gamma-trace CHIRALITY=S-FULL-DIRAC
pairing: one fixed nondegenerate Hermitian Clifford pairing with uniform vector-adjoint sign kappa; optional explicitly changed scalar density ON=declared_carrier
real_structure: actual real K77 principal family complexified for the Hermitian proof; K95 counterpart separately typed, never inferred by porting its reciprocal sign
grading: ambient chirality enters coefficient weights; no physical family or count grading constructed
action_owner: repository-construction -- existing wedge/southeast symbol and source-exterior connection grammar; no source action or gated operator constructed
target: normalized first-order observation intertwining on the stated section/normal-jet prescription MAP-TYPE=intertwiner
```

program_target: BET-2PLUS1
tier: T1
expected_delta: Complete independent-chiral transport and existing density alternative
actual_delta: Scoped whole-family fixed-adjoint exclusion; complete b=H survivor classification; no GU/source/matrix verdict

## Result, novelty, and limit

The earlier scalar-weight obstruction extends to **every independently
chiral member of the already-owned wedge/southeast family**. It allows the
entire compatible unitary spin-connection parent, including connections mixing
ambient chiralities. With the paired adjoint held fixed, the transport equations
are solvable exactly when the section's mean curvature H is zero.

For the existing weighted-adjoint alternative, let b be its normal logarithmic
density gradient. Compatibility holds exactly when **b=H**. This is a necessary
and sufficient normal first-jet condition, not a unique density off the section.
All compatible connection components are characterized below.

New content: ordered independent-chiral proof, direct principal descent/time
inversion for the actual operator, and necessity plus full connection
classification for the density escape. Principal semisimplicity, the scalar
obstruction, the sufficient determinant-density example, time jets and
polarization are prior work.

This exact local transport result does not construct a closed full-14D solution
space, Fredholm domain, physical Hilbert space, observed count, or source-derived
effective decoupling theorem.

## 1. Actual owned symbol and coordinate identification

Let V=H⊕N be a nondegenerate orthogonal split, dim V=n=14, dim H=4,
dim N=m=10. In the actual K77 probe's slot convention, γ_i²=η_i and

```
Γ z = Σ_i γ_i z_i,         (J ψ)_i=η_i γ_i ψ,
c_x = Σ_i x_i γ_i,         i_x z=Σ_i η_i x_i z_i.
```

Thus ΓJ=nI. Expanding the actual off-diagonal wedge entries
`η_a γ_a γ_i γ_b` gives exactly

```
D_x(z,ν) = ( A_w(x) W z + x ν,  -i_x z + c_x E ν ),
A_w(x) = c_x I - x Γ + J(c_x Γ-i_x),
W=w_+P_+ + w_-P_-,        E=ell_+P_+ + ell_-P_-.
```

Terms with a=i, b=i or a=b cancel, matching `wedge(index)` in the owned
probe. The lower-left block is **minus** the metric codifferential symbol.

For comparison with conventional covector components, put F=diag(η_i).
Transport the one-form input/output and covector parameter together:

```
z_cov=F z_raw,   x_cov=F x_raw,   F_total=diag(F,I).
D_cov(Fx)=F_total D_raw(x) F_total^-1.
Γ_cov=(η_i γ_i)_i,    J_cov=(γ_i)_i.
```

Consequently Γ_cov F=Γ_raw, F J_raw=J_cov. With q below,
`q_cov F_total=diag(F_H,I,I) q_raw`. This is a simultaneous coordinate
identification, not a different physical observation. It explains the
eta-on-row versus eta-on-input-column versions of the wedge formula.

The owned completed K77 family has

```
w_+w_- !=0,
12 w_+ ell_- =11,       12 w_- ell_+ =11.
```

The K95 comparator has the opposite reciprocal sign. The transport proof does
not need the reciprocal value: it works for every E in this declared symbol
grammar and hence for the entire previously admitted completion. Other E values
are not newly admitted candidates, and principal propagation verdicts do not
change.

Write M^sharp for exchange of the two chiral coefficients of a weight M, so
γ_i M=M^sharp γ_i. Sharp is **not** an adjoint. The exact ordered membership
in the Nov13 notation is A=W, C=−W, G=−I, L=2A+nC=(2−n)W. All three
necessary factors A,G,L are invertible.

## 2. Direct principal descent and time inverse

Use precisely

```
q(z,ν)=(z_H, Γz, ν),
ker q={z_H=0, Γ_N z_N=0, ν=0}.
```

For x∈H*, hidden z has i_x z=0 and ΓWz=W^sharp Γz=0. Therefore

```
D_x(z,0)=(c_x Wz,0).
```

The output stays normal and Γ_N c_x Wz=−c_x Γ_N Wz=0. Thus the actual D_x
preserves ker q and induces d_x with qD_x=d_xq.

For the actual K77 time t=e^0, η_0=+1, solve D_t(z,ν)=f directly. With
F_spin=Σ_{a≠0}γ_a f_a,

```
ν=f_0,
z_0=γ_0 E f_0-f_ν,
z_a=W^-1[γ_0 f_a + J_a γ_0 F_spin/(n−2)]   (a≠0).
```

The wedge time row vanishes, fixing ν; the scalar row fixes z_0. Set
T=Σ_{a≠0}γ_a Wz_a. The remaining rows read
`f_a=γ_0 Wz_a+J_a γ_0 T`; contraction yields
`F_spin=(n−2)γ_0 T`, proving the inverse for every nonzero pair w_±.

On ker q, D_t=c_t W is invertible and maps that kernel onto itself. Hence d_t
is invertible and

```
q D_t^-1=d_t^-1 q.
```

Vanishing of the complete raw observed lower defect is therefore equivalent
to vanishing of its normalized evolution defect. This says nothing about
pairing descent or whether q is a physical observation.

## 3. Ordered lower response with arbitrary chirality-mixing connections

Hold the geometric prescription and fixed LC-normal jets from
`source-lower-term-compatibility-2026-11-13.md`. Let every K_i be an arbitrary
spinor connection difference satisfying K_i†=−K_i, with γ_i†=κγ_i for a
uniform κ=±1. In particular **[K_i,ambient chirality] need not vanish**.

For hidden z use invariantly raised indices in these formulas:

```
S(z)=Σ_r K^r z_r,
R_i(z)=Σ_r γ^r K_i z_r,
Wsum(z)=Σ_i γ^i R_i(z),
G_h(z)=Σ_μ γ^μ z(II_{μh}),       H=tr_H II.
```

Wsum is distinct from the coefficient weight W. The held grammar is a
coefficient contraction T composed with d_A. Its connection variation is
`V_K=Σ_i D_i diag(K_i)`: the weight acts **after K_i**. The weights are
reference/LC-parallel, not parallel for the varied A; the latter would wrongly
exclude chirality-mixing connections. Replacing T d_A by d_A T is another
operator.

Direct expansion gives

```
(qV_K z)_h      = -W^sharp R_h - W^sharp γ_h(S-Wsum),
(qV_K z)_trace  = (2−n)W(S-Wsum),
(qV_K z)_scalar = -S.                                      (1)
```

For example ΓA_w(x)W=(2−n)W(i_x−c_xΓ); the trace factor is W, not W^sharp.
The calculation only moves weights through Clifford vectors, never through K_i.

The full form/spin LC reference response is

```
(qR_LC z)_h      = -W^sharp G_h + W^sharp γ_h z(H),
(qR_LC z)_trace  = -(2−n)W z(H),
(qR_LC z)_scalar = +z(H).                                  (2)
```

The earlier reference derivation is linear in the natural symbol coefficients;
LC preserves ambient chirality, so its constant weights give these exact left
factors without extra derivative terms. Both form and spin contributions and
the same normal-jet prescription are retained.

Invertibility makes (1)+(2)=0 equivalent to

```
S=z(H),       Wsum=0,       R_h=-G_h.                       (3)
```

The scalar-input SE lower term has no response on ν=0. Its possible indirect
effect through time normalization is already accounted for by principal
descent. No scalar coefficient is silently replacing an independent chiral one.

## 4. Complete unitary normal lemma and exclusion

For a real normal vector B, suppose S=z(B) on ker Γ_N and K_r†=−K_r.
Surjectivity of Γ_N means this condition is equivalent to
K_r=B_r I+Aγ_r for one endomorphism A. Write A=−c(B)+F. Exactly all
solutions are

```
K_r=γ_r c(B)-B_r I+Fγ_r,
Fγ_r+κγ_r F†=0  for every r.                              (4)
```

The forced term is a real Clifford bivector, skew-adjoint for either κ.
This classifies the entire unitary parent, without a Spin or equivariant ansatz.

Its forced response satisfies

```
R_r=-2γ_r z(B)+2c(B)z_r,       W_N=-2(m−2)z(B).
```

The homogeneous F response has R_r^F=−2κF†z_r and
W_N^F=2FΓ_Nz=0. Thus every unitary solution has the same W_N. Symmetry of II
and R_h=−G_h separately give W_H=−z(H). With B=H, (3) therefore forces

```
Wsum=−(2m−3)z(H).                                         (5)
```

For m10 the coefficient is17. The map v ↦ [z ↦ z(v)] on ker Γ_N is injective
for m≥2, including null v. One proof factors a hypothetically vanishing row
v^r I through Γ_N: v^r I=Tγ^r for all frame r. Inverting each non-null frame
generator equates two independently supported Clifford vectors
v^r(γ^r)^−1=v^s(γ^s)^−1. Injectivity of Clifford multiplication forces both
coefficients zero; varying pairs gives v=0. This never divides by v².

Thus (3) is impossible at H≠0. At H=0 the Spin solution

```
K_h^0=(1/2)Σ_μ γ^μ c(II_{hμ}),       K_r=0
```

has R_h=−G_h, S=0 and Wsum=0. The exact fixed-adjoint criterion is therefore
**H=0**, not vanishing of all II. Nonzero traceless II is an explicit survivor.

## 5. Existing weighted adjoint: exact normal jet and complete solutions

The pre-existing rival changes the integration measure by exp(f), retaining the
same fibre Hermitian form and its B-unitary connection class. Its adjoint is
delta_f=delta−i_grad f. Replacing the fibre metric itself by exp(f)B and demanding
connection compatibility with that varying fibre metric changes the equations;
that distinct construction is outside this classification. Let b be its real normal
gradient. With G=−I its added hidden scalar response is **−z(b)**, equivalently
+G z(b). No top/trace response is added. Equations become

```
S=z(H-b),       Wsum=−z(b),       R_h=−G_h.                 (6)
```

Apply (4) with B=H−b. The actual Wsum is necessarily
−z(H)−2(m−2)z(H−b). Equality with −z(b) yields

```
(2m−3)z(H-b)=0 on ker Γ_N.
```

Faithfulness proves **b=H is necessary**. It is sufficient: K_h=K_h^0 and K_r=0
give S=0, W_N=0, W_H=−z(H). This works for every independent chiral weight.

All unitary connection solutions at b=H are precisely

```
K_r=Fγ_r,       Fγ_r+κγ_r F†=0 for every normal r;
K_h=K_h^0+U_h,
U_h†=−U_h,     U_h ∈ Comm(Cl^0(N)).                        (7)
```

Indeed the tangent homogeneous condition is that Γ_N diag(U_h) vanish on
ker Γ_N, equivalently Γ_N diag(U_h)=T_h Γ_N. Componentwise
γ^r U_h=T_h γ^r for every r. Invertibility of frame generators makes this
equivalent to commuting with all even normal Clifford products. Conversely
the commutant condition produces a single T_h and zero homogeneous R_h.
Equation (4) at B=0 is already the complete normal classification.

For H=0, (7) also classifies every fixed-adjoint solution. Separately imposed
real or quaternionic structures intersect this Hermitian solution space; they
cannot enlarge it. The explicit particular Spin solution respects the
corresponding real Clifford structure when that structure is supplied.

The criterion fixes only the normal first jet of log density. Tangential and
higher-normal data remain free for this hidden test alone. If one additionally
requires f to vanish identically on the section to preserve its literal current,
the tangential derivative there is also zero. Pointwise solutions exist without a new
operator/domain construction; a global connection/physical quotient still
requires its actual bundle and domain conditions.

## 6. Existing geometric realization and source ceiling

The same-metric connection reconstruction already proves

```
G_g=y(dx,dx)+K_y(theta_g,theta_g),
K_y(U,V)=tr(y^-1Uy^-1V)-tr(y^-1U)tr(y^-1V)/2,
H=t/2,       K(t,t)=−4.
```

H is nonzero even for flat downstairs geometry. Thus fixed-adjoint transport
is excluded throughout the declared class wherever the stated
Clifford/Hermitian identification with this reconstruction is made.

The K77 code fixes its horizontal sign convention; the displayed geometric
reconstruction and source signature assertion retain their existing K77/K95
ledger distinction. The algebra applies separately to either compatible port.
It proves neither their identification nor the source's choice of real form.

The existing globally defined real scalar on the admitted nondegenerate
metric bundle,

```
f=−(1/2)log|det(g^-1 y)|,
```

has f=0 and grad_N f=t/2=H along the same section. The determinant ratio is
coordinate-invariant and nonzero on the fixed-signature metric bundle, so its
absolute logarithm is smooth there. Its construction is prior work. The new
claim is necessity of its normal jet for every weighted-adjoint escape in this
class, not global uniqueness or source selection of f.

Retain the current distinctions: a bare scalar lower correction at fixed
density preserves its primitive connection derivative; changing paired
density multiplies the ambient current and can require inverse barred-field
transport; multiplying output rows alone changes neither normalized evolution
nor leakage. The universal criterion does not identify these current maps.

SC-OP-04 is candidate-strength four-independent-field grammar. SC-OP-05 admits
but does not select a southeast rival. SC-FER-04/05 and SC-GEN-03/50 give
representation/provenance structure; SC-GEN-52's label uncertainty remains.
The actual imposter's observed gamma-trace landing is unchanged.

SC-CHI-01/04/51/52 concern emergent low-curvature/low-mass chirality, not exact
off-shell q-autonomy. SC-GEN-01 rejects three identical ambient families. No
rank, commutant multiplicity or symmetrizer here becomes a generation count.

**Closed within the stated class:** changing either independent wedge weight, its
reciprocal SE coefficient, or any compatible spin-connection component cannot
evade the fixed-adjoint mean-curvature obstruction. Neighboring coefficients
inside this class need no further enumeration.

**Typed survivor:** the existing weighted-adjoint realization needs b=H and
connections (7), plus its density/bar/current transport, full domain and
source-selection burdens. Other receivers, normal jets, form connections,
additional lower terms, variable weights with derivative terms, and effective
instead of exact decoupling are outside this class. The result does not stop
ordinary work on another eligible discriminator.

LC accounting records this conditional structural result only. No guessed
action variant, source/physics/canon verdict, or matrix status changes. Later
B-lane absorption requires its prescribed rederivation.

## Evidence and internal acceptance

Actual symbol and family:
`tests/channel-swings/selected_k77_wedge_shiab_southeast_completion_probe.py`,
`build_packet`, `wedge`, `symbol`;
`selected-k77-wedge-shiab-southeast-completion-2026-08-11.md`.
K95 contrast:
`../eric-curt-wave3d-b2c4-shiab-family-southeast-completion-2026-08-01.md`.

Reused proofs:
`source-lower-term-compatibility-2026-11-13.md`,
`source-chimeric-trace-compatibility-2026-11-13.md`,
`source-exterior-connection-2026-11-13.md`,
`tests/program-focus/source_exterior_connection_probe.py`.
W06 prior principal coverage:
`exterior-symbol-orbits-conormal-2026-11-25.md`.

Two independent specialist reviewers and a separate hostile source/analytic
reviewer accepted the concrete derivation. This is internal agent review, not
external-human certification. Root executed 61 exact supporting/contrary
controls and the pinned Lean check of five conditional arithmetic/evaluation
theorems, followed by the updated import root. The controls use reduced complex
Clifford representations, including a complex-null evaluation test and a separate
indefinite coordinate test; they do not instantiate the full native128-spinor
geometry. The written universal proof supplies the general/null-vector claims.

[Review and corrections](../../lab/process/hostile-reviews/2026-11-25-chiral-weight-transport-review.md),
[exact evidence](../../lab/process/bet-2plus1-chiral-weight-transport.json),
[probe](../../tests/program-focus/chiral_weight_transport_probe.py),
[conditional formal core](../../Lean/GUFormalization/ChiralWeightTransport.lean).
The Lean core supplies no Clifford/source/domain premise and proves no GU theorem.
