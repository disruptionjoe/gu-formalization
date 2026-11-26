---
status: exploration
doc_type: structural-result
created: '2026-11-25'
program_target: LB-CLASS
tier: T2
expected_delta: Replace the formal zero-matter recipe by an actual locally convergent coupled stationary
  branch, or identify the failed symmetry/closure premise.
actual_delta: Full connected-isotropy invariant space has real dimension 216; the exact Euler map closes
  and has an analytic small-inverse-kappa stationary branch. Native induced fermion response and equal-connection
  observation distinction are explicit. No physical/source verdict.
class_covered: The complete connected-affine-invariant local displacement family of the existing W2 K95
  full U64,64 candidate, both Clifford parities. Product regulator and declared correlated base-metric/compact
  field variations. Not all C or all native domains.
premises:
- lab/sources/source-claim-register.yaml#SC-ACT-01
- lab/sources/source-claim-register.yaml#SC-ACT-05
- lab/sources/source-claim-register.yaml#SC-GEO-51
- lab/sources/source-claim-register.yaml#SC-GEO-55
- explorations/conditional-build/source-action-wave2-construction-2026-11-25.md
- explorations/conditional-build/source-action-engineering-wave-2026-11-25.md
source_bridge:
  status: conditional
  reason: The source supplies action ingredients and kappa, but does not select this completion, large-kappa
    regime, product boundary problem or physical observed sector.
kill_condition: Failure would reject only this invariant-reduction route for the fixed candidate. Existence
  does not decide source truth, C membership, kappa1 or the imported boundary/physical receiver.
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
title: 'From formal series to actual local stationary fields: full homogeneous reduction'
---

# From formal series to actual local stationary fields

```yaml
program_target: LB-CLASS
tier: T2
expected_delta: Test exact full invariant reduction and convergent coupled stationarity.
actual_delta: Real216-dimensional full residual closure yields analytic small-h coupled branch; source, physical and matrix verdicts unchanged.
```

## Main finding, in plain language

The recent construction had a recipe that solved the equations order by order, with no guarantee that adding the terms produced a field. This wave finds an exact symmetry reduction: on the flat-base native metric bundle, **all connected-isotropy invariant connection corrections form a 216-dimensional real space**. The full equation, including its previously missed even corrections, stays inside that space. A direct convergence argument therefore turns the formal recipe into **actual smooth stationary fields for sufficiently large positive kappa**. The base metric and zero-matter equations are satisfied too, in the precise local variation problem below.

The new insight is not a new general mathematical theorem. It is that the remaining analytic obstacle can be removed for this candidate vacuum by proving full symmetry closure, without solving a general indefinite PDE or choosing another small ansatz. It gives an actual background on which the next perturbation questions can be asked.

A concrete bridge follows: the curved background generates a calculable zero-order fermion coupling. Its Clifford contraction is 60, but its complete operator mixes slots, so 60 is **not a particle mass prediction**. The original fixed pure-gauge spherical external datum remains incompatible near this branch. Source selection, physical states, the observed2+1 interpretation and the primary kappa=1 normalization remain open.

**Acceptance:** internally reviewed T2 candidate mathematics; three specialists cross-reviewed the concrete sections and root ran 300 exact controls. Native gates are recorded in the evidence. This is not external-expert or proof-assistant certification. **Source necessity:** conditional. **Weakest unproved link to physics:** source-selected completion and an admitted physical state/readout/constraint space. **Class-C representativeness:** unproved; no width witness or matrix status is promoted.

```gu-typed-objects
result: full homogeneous analytic stationary branch and induced fermion response
carrier: actual K95 metric-bundle full Dirac and u64,64 displacement LAYER=ambient+observed BRIDGE=literal_section_contraction CHIRALITY=S-FULL-DIRAC
pairing: original nondegenerate real Krein/form pairing; independent barred rows ON=full_Dirac_field_module
real_structure: complex K95 rank128 with real u64,64; connected Lorentz isotropy and local spin lift
grading: full Clifford even and odd displacement grades; no physical chirality identification
action_owner: repository-construction fixed W2 comm/symi/symi and SEminusonehalf completion
target: full local Euler section and owned equation-row diagnostic MAP-TYPE=contraction
```

> **GU-COMPARATOR-ROUTING — scope before inference.** Read [source-native routing](../../lab/methods/source-native-comparator-routing.md). This is a candidate-level construction, not a conventional Higgs, repeated-three-family or index substitute. Literal contraction, source2+1, fullU, independent bars, K95/K77 separation and non-LC displacement remain explicit.

## A. Exact geometric and analytic reduction

### A1. Actual affine homogeneity

For constant base metric g0 the selected base connection is flat, so in affine coordinates the actual ambient metric is

    G_(x,y)((v,U),(w,V)) = y(v,w)
       + tr(y⁻¹U y⁻¹V) − (1/2)tr(y⁻¹U)tr(y⁻¹V).

The fibre contains nondegenerate symmetric y of signature(3,1). Let the connected oriented affine group act by

    x′=Ax+b,  y′=A⁻ᵀyA⁻¹,
    v′=Av,    U′=A⁻ᵀUA⁻¹,
    A∈GL⁺(4,R).

The horizontal pairing is unchanged. Also `y′⁻¹U′=A(y⁻¹U)A⁻¹`, so both vertical trace terms are unchanged. This is an isometry of the actual K95 metric, including its trace direction. It preserves the flat horizontal connection and the horizontal/vertical decomposition. It is not merely a fibre symmetry with x held fixed.

The action is transitive: translations choose x and congruence chooses any y of the specified inertia. The stabilizer at p=(0,eta) has Lie algebra so(3,1), and group dimension20−6 gives the actual dimension14. For connected isotropy and local spin bookkeeping use the homogeneous cover G/H0, H0=SO⁺(3,1). The theorem only needs a neighborhood of p and can then be restricted to any relatively compact chart. A global equivariant spin bundle on the original un-covered metric space is not silently asserted.

The fixed g0 itself need not be invariant under every affine A. Its **connection** is invariant, and G_g0 and every bosonic coefficient here depend on g0 only through that connection. This is why the larger affine symmetry is available. The actual observation section and the imported boundary fixture need not share it and are not imposed in this reduction.

### A2. Spin/Krein lift and coefficient naturality

An orientation-preserving isometry in the identity component acts on the oriented orthonormal frame bundle. On a contractible patch it lifts to the chosen spin bundle, uniquely up to the central sign. Infinitesimally, the lifts are generated by Clifford bivectors. In the declared K95 representation these are H-skew, so the lift preserves the Krein form of signature(64,64). Conjugation therefore preserves the real Lie algebra u(H).

The central sign acts trivially on End(S) and on u(H). Thus the bosonic displacement representation and the invariant-space construction below do not depend on which of the two local spin lifts is chosen. Globally one may formulate these adjoint/Clifford-valued tensors on the homogeneous associated bundle; an actual spin connection matrix is then read in the admitted local spin chart. This suffices for a local solution of the candidate action.

The required naturality concerns the actual fixed coefficient recipe, not a guessed invariant operator:

- Clifford multiplication intertwines the lifted isometry and its tangent action.
- The forms Φ1(v)=c(v♭) and Φ2(v,w)=[c(v♭),c(w♭)]/2 therefore intertwine.
- Matrix commutator and i times anticommutator commute with conjugation; multiplication by the fixed scalar i does not change this.
- Wedge, metric contraction, oriented Hodge star, trace pairing and volume density commute with the isometry.
- Consequently the actual S0 comm/symi/symi expression, and Φ=*⁻¹S0, intertwine.
- The Levi-Civita spin connection B is natural under isometry; D_B and its local formal adjoint are natural with the same pairing and density. Formal adjoint here means the local Euler differential operator, not a boundary-domain realization.
- Hence the actual S=ΦF_B, K=(ΦD_B+D_B†Φ†)/2, and symmetric algebraic N in W2 are equivariant. The full Euler residual remains u(H)-valued under the same real pairing used to derive it.

For the declared Krein adjoint, gamma_a^sharp=-gamma_a. Bivectors are also skew. If X,Y are skew, [X,Y] and i(XY+YX) are skew; both i factors in the actual Shiab recipe are retained. The real trace/form pairing is nondegenerate, although indefinite. Its real formal adjoints preserve the real coefficient bundles, and the mass Euler term is exactly kappa T. Even if the pairing restricted to E were degenerate, this full-residual argument would still apply: it does not obtain the equations by restricting the action to E.

No restriction to Clifford-compatible displaced connections or to a quaternionic subgroup has been inserted. B is Clifford-compatible, but B+T generally is not. The non-Clifford remainder of the fermion operator remains present if matter is subsequently introduced.

### A3. Complete finite invariant receiver space

Let W=T_p*Y⊗u(H), a real vector space of dimension14×16384. Define

    E = W^(H0).

An element t∈E determines one invariant section T_t by transport from p; isotropy invariance makes the transport well-defined on the homogeneous cover. Conversely an invariant section is determined by its value at p. Thus E is finite-dimensional, and no independent derivatives of an invariant field can be freely selected.

Because the *full* residual operations are equivariant,

    S∈E,  K_E:E→E,  N_E:E×E→E.

These are obtained by applying the actual differential/algebraic operation to the invariant section and evaluating at p. In particular K_E is an ordinary finite linear map despite K being a first-order differential operator on arbitrary fields. The resulting residual vanishes as a full section iff its value in E vanishes. No omitted non-invariant Euler receiver remains: the residual of invariant input is itself invariant.

#### Dimension, with real-form qualification

Complexifying the connected isotropy gives sl2⊕sl2. Its tangent module is

    m_C = V_(1,1) ⊕ V_(2,2) ⊕ V_(0,0),

the4-dimensional vector,9-dimensional traceless symmetric part, and trace line. End(S_C) is the full complex Clifford algebra, hence Λ*m_C as isotropy module. Its even and odd parts each have dimension 8192. Character subtraction gives, in each parity,

    multiplicity(V00)=16,
    multiplicity(V11)=40,
    multiplicity(V22)=52.

Therefore Hom_H(m_C,End(S_C)) has dimension 216, split 108+108 by Clifford parity. The real Lie algebra u(H) is an invariant real form whose complexification is End(S_C); taking invariants commutes with complexification because it is the kernel of real infinitesimal representation matrices. Hence **dim_R E=216**,108 in each parity. This count concerns invariant displacement tensors, not particle families or physical degrees of freedom. The trace line explains equality of the two parity characters. The accompanying probe reconstructs the full exterior weight characters from their irreducible multiplicities, rather than checking only the three quoted numbers.

The existence proof only needs finite dimensionality; it does not depend on explicitly listing 216 basis tensors. The full216-dimensional space avoids the previous failure from retaining only constant odd radial/projector tensors.

### A4. Analytic finite-h existence and explicit symbolic radius

On E the exact normalized connection equation is

    F(h,t)=t+hS+hK_E t+hN_E(t,t)=0.

It is polynomial and its t derivative at (0,0) is the identity. The real analytic implicit-function theorem gives a unique analytic branch through t(0)=0. The following direct majorant also supplies a useful certificate without any unspecified infinite-dimensional inverse.

Choose any norm on E and finite bounds

    s=||S||>0,  k≥||K_E||,  n≥||N_E||_bilinear.

The already-owned formal recurrence is bounded coefficientwise by the nonnegative scalar solution

    m(q)=q(s+k m(q)+n m(q)²),  q≥0.

For n>0,

    r = 1/(k+2√(ns)),
    m(q)=[1−kq−sqrt((1−kq)²−4nsq²)]/(2nq),  0<q<r.

The q=0 value is0. If n=0, use m(q)=sq/(1−kq), with r=1/k; if n=k=0 the branch is simply t=−hS and r=∞. These are bounds in whichever norm was chosen, not actual numerical constants computed for the native216-dimensional system.

For |h|=q<r, the map t↦−h(S+K_Et+N_E(t,t)) maps the closed ball ||t||≤m(q) into itself. Its Lipschitz constant is at most

    q[k+2n m(q)] = 1−sqrt((1−kq)²−4nsq²) < 1.

Thus it has a unique solution in that ball. This is uniqueness within the invariant ball, not uniqueness among arbitrary non-invariant fields or disconnected finite-h branches.

Equivalently, set a1=s and

    a_j=k a_(j−1)+n sum_(u+v=j−1) a_u a_v.

Then ||T_j||≤a_j, and sum a_j q^j=m(q). The native formal series therefore converges absolutely in E for |h|<r. Evaluation E→C^ell(K) on a compact chart K is a bounded linear map for each finite ell, so the section series converges in every C^ell compact seminorm. This supplies smooth local connection solutions and validates termwise differentiation, not merely convergence of point values.

For any q<rho<r, truncation after orderM has the explicit coefficient bound

    ||t(h)−sum_(j=1)^M h^jT_j||
       ≤ m(rho)(q/rho)^(M+1).

The same estimate holds in a C^ell(K) seminorm with its finite evaluation constant. This addresses the previous derivative-growth obstacle precisely inside the homogeneous sector; it provides no unrestricted native PDE estimate.


## B. Exact coupled stationarity and boundary/observation consequences

### B1. Exact base-metric stationarity at each small nonzero h

### The actual dependence on g

The metric bundle has coordinates (x,y), where y is the independent fibre metric value. Its metric is

    G_g = y_mu nu dx^mu dx^nu
          +V_y(dy-C_mu dx^mu, dy-C_nu dx^nu),
    C_mu=Gamma_mu(g)^T y+y Gamma_mu(g),
    V_y(U,V)=tr(y^-1 U y^-1 V)-1/2 tr(y^-1 U)tr(y^-1 V).

The horizontal metric is y, **not an additional explicit g coefficient**. Base g enters through its Levi-Civita connection. The spinor trivialization can be chosen locally from the ambient metric matrix G_g. The Clifford tensors, Phi, Hodge, pairing, density and B[g] then depend on g only through Gamma(g) and finitely many derivatives. Constant H=diag(I64,-I64) in a smooth Krein frame permits holding actual u(64,64) connection coefficients fixed. No K77 or quaternionic replacement is used.

At constant g0,

    delta Gamma^a_mu b = 1/2 g0^ac
        (partial_mu p_cb + partial_b p_cmu - partial_c p_mu b).

There is no undifferentiated-p term: the variation of g^-1 in Gamma multiplies `partial g0=0`. The same property persists after differentiating Gamma or composing the ambient geometric constructions. An additional arbitrary g-dependent frame convention could obscure this fact; it is neither required nor adopted.

### Variational class and proof

Fix a relatively compact product regulator `Omega_x × V_y` with smooth fixed fibre boundary, contained in a nondegenerate metric chart. Take `p=delta g` compactly supported in Omega, with no artificial independent dependence on y. Hold `Ahat(h,y)` fixed in the declared coordinate frame and set fermions/bars to zero. Vary the **original action density**, not an effective action with unexamined boundary terms.

At each fixed nonzero h in the analytic interval its first variation has the finite form

    delta_g L = sum_(1<=|alpha|<=m) C_alpha(h,y) partial_x^alpha p(x).

All coefficients are x-independent because both reference geometry and actual connection are translation invariant. They are smooth and bounded on the compact fibre chart. Integrating in x first gives

    delta_g I[g0,Ahat(h),0,0](p)=0.

There is no interchange of an infinite series and metric variation. No fibre-boundary term has been discarded: the original density is integrated directly, and the compact-x derivative integral vanishes with all y dependence retained. This covers the exact moving B, Clifford/Hodge, pairing and density terms and uses only the permitted base-metric variation.

### Other primitive variations

- Compactly supported arbitrary connection variations in the product region vanish because the full connection Euler residual is zero.
- Zero barred/unbarred fermions solve their bilinear Euler equations and produce zero current.
- In the declared dressed two-frame completion, a compact epsilon variation induces a compact connection variation (including its derivative). Its Euler pairing is zero. This is the candidate's Noether redundancy, not an authentication of every source active symmetry.

**Conclusion:** for each sufficiently small nonzero real h, `(g0,Ahat(h),chi=0,bar chi=0)` is an actual smooth coupled stationary configuration of the chosen local action in this product-regulator variation class. Set kappa=1/h. No statement that the analytic interval reaches h=1 is made.

### B2. Local existence is not a global state/domain

The homogeneous construction may be formulated on a local lifted homogeneous space and then restricted to this product chart. An unresolved global spin lift, complete metric-bundle topology or native boundary does not prevent the local result, but it prevents reporting global existence on the intended physical carrier without a separate proof.

On the compact regulator the fields and action density are smooth and finite. On a whole homogeneous noncompact space the action integral or L2 norm can diverge. A stationary homogeneous field is not a normalizable fermion state. No positive physical pairing, causal evolution, Fredholm observation complex, true-family modes or observed scattering is established.

The connection variations are compactly supported and the boundary traces are those supplied by this branch. Arbitrary boundary variations or the earlier external Bott boundary are not part of this stationarity statement. Base-metric variations extend through the fibre but have compact base support; the direct-density proof is specifically what permits that correlated variation class.

### B3. The boundary mismatch persists on an open C1 neighborhood

The earlier engineering result identifies nonzero tangential curvature of B0 at a horizontal pole p of the coordinate sphere. All vertical directions are tangent there. For traceless symmetric vertical U,V supported on a positive 2×2 block,

    U=diag(1,-1), V=[[0,1],[1,0]],
    R^V(U,V)V=-1/4[[U,V],V]=-U !=0.

The actual spin-LC curvature is nonzero because its action on Clifford vectors recovers that tangent curvature. Choose any fixed real component receiver ell with `m=|ell(F_B0(U,V))|>0`. For A=B0+T,

    F_A=F_B0+D_B0 T+T wedge T.

On a compact neighborhood of p, smooth coefficients and a fixed positive auxiliary coordinate norm give constants C1,C2>=0 such that

    |ell((F_A-F_B0)(U,V))|
         <= C1 ||T||_C1 + C2 ||T||_C1².

If C1+C2>0, take any

    0<delta<min(1, m/[2(C1+C2)]).

Then `||T||_C1<delta` keeps the receiver magnitude at least m/2, so the boundary restriction is not flat. If C1+C2=0 the receiver is unchanged. This is an **open-neighborhood exclusion**, covering arbitrary sufficiently C1-small displacements, not merely invariant fields.

The analytic branch satisfies `||T(h)||_C1->0`, so its boundary is nonflat for every sufficiently small h. It therefore cannot equal or be gauge-equivalent to `U_k^-1 dU_k`, which is tangentially flat, for any k including zero. This is a property of the fixed reference geometry/boundary problem, not a generation-count obstruction. No numerical radius is asserted before C1,C2 and the continuation radius are evaluated. Boundary layers, large displacement, different leading geometry, or a changed external datum remain distinct possibilities.

### B4. Exact equal-connection lemma: bulk scale versus observation

For any two base metrics with the same Levi-Civita connection, `Gamma(g1)=Gamma(g2)`, the displayed ambient metrics agree on the same metric-bundle chart:

    G_g1=G_g2.

Use the same ambient spin trivialization and hold Ahat, fermions, bars, chart domain and boundary/framing structures fixed; recompute the actual observation section from each base metric. Then B, Phi, Clifford/Hodge operators, pairing and density agree, so **the entire candidate ambient functional agrees**, including its fermion term. A simple exact subfamily is

    g2=c g1, c>0 constant,
    Gamma(cg)=Gamma(g).

This is not a local Weyl symmetry: a variable c(x) changes the connection. It is not automatically a physical gauge equivalence either. The source observation sections differ, and

    s_g^*G_g=g

because `dg-Gamma(g)^Tg-g Gamma(g)=0`. In particular `s_cg^*G_cg=cg`, even though the ambient metrics are identical. Thus the ambient functional alone cannot distinguish constant base scales at fixed independent fields, while observation and held external data can. Whether those distinctions are physically equivalent depends on transporting those data, rather than declaring a new gauge freedom.

This exact identity also keeps the new result separate from K2519's failed observation graft: the actual metric bundle retains its tautological rank10 metric receiver. It does not yet provide a normalized physical observable or scale prediction.

### B5. Prior-result scope and what changed

K2519 already supplies full stationary local seeds of a different completion: real Cl(7,7), independent ambient metric, two seven-dimensional space forms and parallel distortion. Its chosen totally geodesic observer fails the rank10 native metric-fibre receiver test. The present action fixes the actual K95 metric-bundle geometry and varies the base g through its lift; neither the old solutions nor their metric scale equations transfer by name.

K2529 uses an inverse-function theorem for a restricted four-coordinate source response around those seeds and explicitly withholds a full native sourced solution. Here the decisive new proof is closure of the **full residual** in the invariant E space for the W2 action, followed by the exact base-metric argument. Do not claim the first homogeneous analytic solution or a new implicit-function theorem.

The substantive upgrade, once the mathematical arc is accepted, is from a formal zero-matter recipe to actual small-h stationary fields of this candidate. It leaves the source action ownership, prescribed external datum, physical states and h=1 questions open. Repeating more formal coefficients is unnecessary; a source-typed matter/observation response or quantitatively controlled continuation would be the next distinct work.


## C. The induced fermion response

### C1. Owned leading connection

Use the actual wave2 normalization `T(h)=h T1+O(h²)` at the flat base, with

`(T1)_a=t_a gamma_a`,

`t_a=21/4` on four horizontal axes and the one normal trace axis,
`t_a=15/4` on the nine normal traceless axes.

These coefficients are real. Gamma_a is H-skew; inserting an extra i would leave the real Lie algebra. Clifford contraction yields

`gamma^a (T1)_a = [5(21/4)+9(15/4)] Id =60 Id`.

That scalar contraction is not the full fermion operator. Since `[T1_a,gamma_b]` is generally nonzero, the generic full-U differential remainder cannot be omitted.

### C2. Full zero-order correction

Differentiate the repaired operator D_rep with respect to its connection. For any a,

`V(a)(zeta,nu)_r,a = gamma^b(a_b zeta_a−a_a zeta_b)+a_a nu`,
`V(a)(zeta,nu)_scalar = eta^a a_a zeta_a−(1/2)gamma^a a_a nu`.

Putting a=T1 and using `gamma^b gamma_a zeta_b=−gamma_a Gamma zeta+2zeta_a` gives

`V(T1)_r,a = (60−2t_a)zeta_a+t_a gamma_a(Gamma zeta+nu)`,
`V(T1)_scalar = Gamma_t zeta−30nu`,

where `Gamma_t zeta=sum_a eta_a t_a gamma_a zeta_a`. Therefore the actual background fermion operator is `D_B+h V(T1)+O(h²)` on every fixed compact chart if the analytic branch is established. This statement is local operator algebra; its interpretation requires an admissible physical domain and states.

### C3. Source-owned imposter/scalar diagnostic

Reuse the owned injection `I psi=(10J_H psi,−4J_N psi)`, Gamma I=0, and independent scalar input nu=phi. The normal trace direction is one of the ten N axes. For the equation-row diagnostic `d_E(r,t)=(Gamma_H r_H/4,t)`,

```
d_E V(T1)(I psi,phi) = [495   21/4] [psi]
                       [ 54    −30] [phi].
```

Indeed `r_H=495 J_H psi+(21/4)J_H phi`; and

`Gamma_t I=10[4(21/4)]−4[(21/4)+9(15/4)]=54`.

The determinant is `−30267/2`, so this diagnostic has full rank256 on the two rank128 input slots. This is distinct from the rank-one horizontal **central-probe** subdiagnostic in the prior engineering wave. There is no contradiction: T1 is a noncentral Clifford-vector connection variation with both horizontal and normal components.

The previous central-horizontal diagnostic kernel `phi=20psi` now produces `(600psi,−546psi)`, not zero. The ambient branch therefore supplies a concrete geometry-forced perturbation that detects that previously special combination. This is not identification of those slots with two physical families or a claim about dark matter.

### C4. The primed operator is not a scalar mass shift

To make the limitation explicit, take pure primed scalar input `(zeta'=0,eta)`. Wave2's inverse map gives `zeta=−J eta/2`, `nu=−6eta`. Directly applying the correction and then the equation-row map R gives

`(R V(T1)F^-1)_oneform,a = (330−12t_a)gamma_a eta`,
`(R V(T1)F^-1)_scalar =720eta`.

The one-form coefficient is267 on horizontal+trace axes and285 on normal traceless axes, both nonzero. Thus even in the repaired Dirac principal coordinates this correction mixes the one-form and scalar slots. Reading60 as a physical universal mass would ignore this explicit coupling, the unequal field/row transforms, the independent bars, and physical-domain questions.


## D. Consequences, novelty and retained burdens

The nonzero S and already-owned nonzero T2 receiver imply that the actual branch is nonzero and contains both Clifford parities for all sufficiently small nonzero h. Its coefficients are exactly the previously constructed recurrence. The grading symmetry gives T(-h)=theta T(h); the zero-matter effective action is odd in h. These are now convergent identities on compact charts. The original action uses kappa=1/h, so h=0 is only the normalized analytic anchor, not a finite-coupling stationary point.

| Question | Result here | Remaining burden |
|---|---|---|
| Do all invariant connection equations fit together? | Yes, exact polynomial map on the complete connected-isotropy216-dimensional real space | Explicit tensor basis/coefficients only needed for quantitative continuation |
| Does the old formal branch converge somewhere? | Yes, nonempty small-h interval with symbolic majorant and compact smooth convergence | Native numeric norms; whether the interval or continued branch reaches h=1 |
| Are the metric and matter equations also satisfied? | Yes, constant base and zero matter under the stated product-regulator variations | Nonzero matter, general backgrounds, physical domains and stability |
| Can the fixed imported pure-gauge boundary be attached nearby? | The existing mismatch persists on an open small-C1 neighborhood | A boundary layer, large displacement or different datum/geometry is a different problem |
| Does geometry affect the fermion operator? | Explicit leading coupling on the full owned slots and a full-rank imposter/scalar diagnostic | Normalized physical states, constraints, observed family embeddings |
| Does the bulk action determine the observing metric scale? | Equal base connections give identical held ambient functional; observation can differ | Physical equivalence and scale depend on the complete observed/external data |

This is not evidence that all GU constraints are jointly satisfiable. It supplies a local stationary background for one source-informed candidate, rather than proving that the candidate is source-required or in class C. It does not evade the observation-domain obstruction: smooth fields can be restricted to the section, but that does not supply a closed physical Hilbert-space readout or a Fredholm complex.

**Literature/context.** The use of homogeneous invariant connections is standard; [Hanusch, A Characterization of Invariant Connections](https://arxiv.org/abs/1310.0318v3) states Wang's transitive classification and generalizes it. The explicit local transport/closure and majorant proofs above carry this result; the paper is not a GU applicability certificate. K2519/K2529 already own different stationary and restricted-response results as distinguished in B5. No external novelty survey or new general theorem is claimed.

## E. Verification and continuation

The probe is `python3 tests/program-focus/source_action_homogeneous_probe.py`. It checks native K95 Clifford/current arithmetic, complete exterior-character reconstruction, exact affine metric and nonconstant metric-jet identities, and reduced polynomial/majorant contrary controls. It does not numerically solve the 216-variable native equation, calculate its norm constants, check Lean, or prove a physical mode spectrum. The written analytic proof and object-sensitive independent review are the evidence for existence.

Verification results and exact reviews are recorded in [machine-readable evidence](../../lab/process/source-action-homogeneous-analytic-vacuum.json) and the [internal review](../../lab/process/hostile-reviews/2026-11-25-source-action-homogeneous-review.md).

The uncovered construction questions are now quantitative continuation within the complete invariant family and admissible perturbations/physical observation around an actual branch. Generic formal-existence work and more coefficients are covered in the declared scope. The [existing packet](../../lab/process/work-packets/source-action-response-discriminators-2026-11-25.md) records those distinctions; ordinary research priorities and governance are unchanged.
