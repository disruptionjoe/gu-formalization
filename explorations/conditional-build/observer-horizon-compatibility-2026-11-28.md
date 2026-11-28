---
title: 'Observation as a horizon: causal-cone and finite-state compatibility'
status: exploration
doc_type: structural-result
created: '2026-11-28'
program_target: X-P1-P2
tier: T1
expected_delta: Test the unbuilt causal/state bridge using the actual metric-fibre representation and printed differential symbol.
actual_delta: Robust Lorentz-natural pointed cones and unrestricted finite-measure value/finite-jet realizations are excluded in the stated categories; weighted stationarity leaves higher variation free.
class_covered: Closed pointed Lorentz-invariant conic subsets of H plus Sym2(Hstar) with a pure horizontal interior vector; separately finite invariant fibre measures retaining all smooth germs of the declared first-order operator.
premises:
- SC-GEO-03 draft p17 supplies Met(X); its section-induced connection metric is the held K95 reconstruction.
- SC-ACT-02 draft p45 eq9.8 supplies an endpoint template; the low-Phi dictionary is a selected realization, not source uniqueness.
- SC-META-52/53 leave physical causal, boundary, state and positivity structures open.
- Existing invariant-measure support and natural-density first-jet theorems are reused, not newly proved here.
source_bridge:
  status: conditional
  reason: Neither a robust ambient cone nor finite invariant L2 state measure with unrestricted normal jets is source-required. These test specified completion mechanisms for H1, not GU itself.
kill_condition: Boost-weight limits contradict pointedness, or the actual operator maps a measure-null smooth field to a nonzero output class; close only the corresponding declared category.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
internal_target: INTERNAL-OBSERVER-HORIZON-COMPLETION
canon_verdict_change: none
---

# What the section supplies, and what it still needs

program_target: X-P1-P2
tier: T1
expected_delta: Decide the stated causal-cone and finite-state compatibility classes.
actual_delta: Scoped cone/lineality and actual operator non-descent results; physical bridge remains open.

**ESTABLISHED:** the same-metric section has timelike mean curvature and admits the required density first jet. These are owned results. They do not by themselves select a causal horizon or an equation-compatible finite state space.

Two new compatibility tests sharpen that gap:

1. A closed pointed cone respecting the actual observed Lorentz action cannot contain a pure horizontal observer velocity in its full fourteen-dimensional interior.
2. The already-classified finite invariant measures can normalize values on a conformal ray, but the actual ambient first-order equation does not act on those value equivalence classes. Retaining any finite number of unrestricted transverse jets still does not close the equation.

Neither excludes all GU* completions. Restricted velocities, a supplied clock/tensor, selected normal-jet relations, different state spaces and nonlocal constructions remain open. No such choice is adopted here.

```gu-typed-objects
result: Observer-horizon compatibility
carrier: H direct-sum Sym2(Hstar); separately actual bosonic one-form Clifford field LAYER=ambient+observed BRIDGE=literal-contraction-only CHIRALITY=N/A
pairing: native trace-reversed metric and auxiliary positive coefficient norms, separately typed ON=declared_carrier
real_structure: K95 normal(6,4), ambient(9,5); source primary-minus real bosonic coefficients; no K77 transfer
grading: Clifford form grades, not fermionic or physical chirality
action_owner: repository-construction -- selected printed low-Phi realization; fixed-reference geometric volume is separate
target: causal cone and state quotient MAP-TYPE=restriction
```

## 1. Source custody, reuse and expected outcomes

SC-GEO-03 **ASSERTS** `Y=Met(X)` (draft p17; dimension14 p55 and rank10 fibre p28). SC-GEO-51 **ASSERTS** the chimeric semi-canonical relation (TOE2025 02:41:57); it does not identify every reconstructed real form. SC-ACT-02 **ASSERTS** the first-order endpoint (draft p45,9.8–9.10). SC-META-52 **UNCERTAIN** acknowledges ultrahyperbolic/boundary debt (01:17:10); SC-META-53 **UNCERTAIN** leaves spectral/physical shielding unresolved (01:22:30). None supplies the tested cone or probability-to-physical-state identification.

The actual metric fibre transforms as symmetric covariant tensors, not ten inert scalars or an exterior-power bundle. The section-induced native K95 metric is distinct from K77. Literal contraction preserves horizontal form components but has not been identified with a gauge-invariant physical observable. No source 2+1 count, Higgs, chirality or mirror-particle conclusion follows.

Reuse, without repeat credit:

- [Native density theorem](natural-density-fibre-volume-2026-11-25.md): `H=t/2`, `K(H,H)=-1`, all required natural first logjets, and infinite smooth invariant full-fibre mass.
- [Singular measure theorem B1](symmetry-restoration-measure-limit-2026-11-25.md): every finite positive Lorentz-invariant fibre measure is supported on `Z_g={a g:a>0}`; every measure on this ray is invariant.
- [Chimeric geometry](source-chimeric-trace-compatibility-2026-11-13.md), [actual printed symbol](printed-equation-jets-and-symbol-2026-11-27.md), and [full-system symbol checks](cw-fullsystem-domain-2026-11-27.md).
- Prior conormal/non-autonomy results already show why restriction need not intertwine derivatives. The new delta is the joint classification with **all surviving finite invariant measures**, actual bosonic coefficients, and the robust nonquadratic cone criterion.

Advance outcomes: a compatible cone or quotient would provide a scoped mathematical survivor. A failed test excludes its quantified category and names the additional datum; it does not make that datum impossible. Source necessity and class-C representativeness remain unproved. Physical state/readout and reference semantics are shared prerequisites of predictive, energy and H1 interpretations.

## 2. Boost-weight obstruction to robust observer causality

Let H be time-oriented Lorentz four-space and `N=Sym²(H*)`. Use the diagonal action of `G=SO⁺(1,3)` on `V=H⊕N`. A **conic** set is invariant under positive rescaling; **pointed** means `C∩(-C)⊂{0}`.

**Theorem C.** No closed, pointed, G-invariant conic subset C has `(h,0)` in its full V-interior, for any h. Convexity is not needed.

**Proof.** Take a boost A_s. Its weights on H are `1,-1,0,0`. A null covector ell can be chosen with dual weight1, so the nonzero symmetric tensor `v=ell⊗ell` has weight2. Interior membership gives `(h,±epsilon v)∈C` for some epsilon>0. Invariance and conicity give

`(exp(-2s) A_s h, ±epsilon v) ∈ C`.

The first component tends to zero as s tends to infinity. Closedness places both `(0,epsilon v)` and its negative in C. Pointedness contradicts v≠0. QED.

This is an actual representation constraint, independent of the DeWitt coefficient. It applies to a K77 proposal only after the same correlated Lorentz representation and cone hypotheses are established; it is not a transfer of metrics or operators. Adding the owned H supplies no new isotropy breaking, since its vertical trace direction is Lorentz-fixed.

**Controls and survivors.** The ordinary four-dimensional future Lorentz cone has timelike interior. On the full V, however,

`C_product = C_H^+ × PSD(H*)`

is a closed convex pointed invariant full-dimensional cone with every pure-horizontal member `(h,0)` on its boundary. It is a genuine counterexample to the stronger false statement that no natural cone exists. It restricts normal motion to one matrix sign; no printed-equation compatibility is established. If an extra future unit clock u is supplied, its compact stabilizer preserves a positive norm on the other thirteen directions. A Lorentz-type cone using that norm puts `(u,0)` in its interior. The resulting covariant **family depending on u** escapes the theorem, at the cost of the added datum; no clock is selected here.

Thus the theorem rejects robust unrestricted local bulk causality from the observing metric alone. A boundary-only observed direction, restricted admissible velocities, additional tensors, nonpointed relation, or nonlocal notion of accessibility changes its premises. The source does not require the rejected combination.

### Sharp price if pointedness is dropped: nine normal directions

There is a stronger statement for **closed convex** conic C, without assuming pointedness. If `(h,0)` is interior, the same limit places both signs of every vertical null square in C. Its lineality space `L=C∩(-C)` is a vector subspace, so it contains their span. That span is exactly

`N0={n∈Sym²(H*):tr(g^-1 n)=0}`, of dimension9.

For an exact spanning control take the six null covectors `(1,±e_i)` and the three `(1,(3/5)e_i+(4/5)e_j)`, i<j. Their nine symmetric squares are tracefree and have rank9 in the ten symmetric coordinates. This proves the whole normal shape subspace is forced into lineality, not merely one special null direction.

The bound is sharp algebraically. Write `n=n0+a g`, with `a=tr(g^-1 n)/4`. The pullback of

`{(h,a): h future, -g(h,h)>=a²}`

to H⊕N is a closed convex Lorentz-invariant cone, has pure horizontal timelike interior, and has lineality exactly N0. It is not the native metric cone or a selected physical construction. If used as an order relation, those nine normal directions have no antisymmetric order distinction until a quotient or additional rule is supplied. This is not a proof that they are gauge or physically unobservable. Identifying causal lineality with a field-state quotient needs its own bridge; the nonzero differential response in §4 makes that bridge consequential.

## 3. Causal barrier and trapped-submanifold limits

Independently of Lorentz covariance, suppose a continuous open future-cone field near a smooth section admits an ambient-interior tangent vector `h∈TS`. In adapted coordinates `S={y=0}`, small velocities `∂_0+w` with both signs of transverse w remain future-directed. For a smooth positive bump phi on `(0,T)`, vanishing at the ends, and sufficiently small epsilon,

`gamma(s)=(s,0,epsilon phi(s)n)`

is future-directed, leaves S and returns later. Shrink the chart and use a compact parameter interval to keep its tangent inside the open cone. The section therefore is not a local one-way causal barrier under this **additional robust-cone premise**. This is separate from Theorem C: a cone in its closed pointed class cannot satisfy that premise. Closedness matters: `int(C_H^+) × N` is an open Lorentz-invariant pointed cone with horizontal interior, but its closure has the whole normal space as lineality. It permits the displayed excursions and is not a counterexample to Theorem C.

A Lorentzian section also cannot be an achronal horizon for a causal relation retaining its timelike tangent curves. A horizon enclosing the section, observer-algebra boundary, or restricted cone can still be meaningful; no such object has been supplied here.

Standard trapped-submanifold results permit arbitrary codimension, so codimension alone is not the correct objection. [Galloway–Senovilla,1005.1249](https://arxiv.org/abs/1005.1249), §2 and its theorems, require a Lorentzian index-one ambient spacetime and spacelike trapped submanifold, with further curvature/global conditions. The tested section is Lorentzian, its ambient has index5, and its normal has index4. Those are substantive missing premises. Timelike H does not supply future orientation, focusing, an event horizon, or a positive observer trace. No novelty claim about standard causal geometry is made.

## 4. Finite invariant normalization versus the actual equation

Let mu be any nonzero finite positive invariant fibre measure. Reuse B1: `supp(mu)⊂Z_g`. This includes atomic and singular-continuous scale laws, not only delta_g. A probability used solely as a geometric average or reference for a reduced action need not be a field-state norm; the following theorem applies only if it is offered for that latter role.

For bundles E,F with auxiliary positive coefficient norms and a first-order smooth operator L, an action of the **same expression** on ordinary `L²(mu)` value classes of all smooth compact germs requires

`[u]=0 ⇒ [Lu]=0`.

If f vanishes on Z, then `L(f beta)|Z=σ_L(df)beta|Z`. A nonzero conormal symbol therefore violates that necessary condition wherever it has nonzero mu-measure. Compact cutoffs make both representatives finite. This is failure of well-definedness before a question of closability; it is not a theorem against every singular state space.

### Binding the native off-diagonal normal

At `y=a g`, use g-orthonormal spatial indices1,2. The symmetric matrix `S=(E12+E21)/sqrt(2)` has trace zero and native K95 square1 at y=g. It is not the negative trace normal. Near a positive ray point define `a(y)=tr(g^-1y)/4` and

`f(y)=sqrt(2) y12/a(y)`.

On Z, f=0 and df is a unit positive transverse conormal for `K_y(U,V)=tr(y^-1Uy^-1V)−(1/2)tr(y^-1U)tr(y^-1V)`. In a native orthonormal frame call it theta4. Choose the horizontal odd hook

`beta=theta1 gamma1 − theta2 gamma2`.

For the actual held principal map `P(xi)beta=Phi(xi wedge beta)`, the authenticated nested-Phi calculation gives

`P(theta4)beta=−2 c(theta4)beta
 =2 theta1 gamma14 −2 theta2 gamma24`.

Both coefficients are real in the tested primary-minus carrier. The first literal horizontal receiver is2; its auxiliary coefficient norm squared is8. Port theta4 is explicitly bound to the actual traceless spatial off-diagonal matrix, not to a trace mode or an arbitrary CW label. The orthonormal identity extends smoothly along every positive scale.

Take `T=chi f beta`, localizing around a support point of mu. Then `[T]=0`, but `[P T]≠0`; continuity bounds its positive output norm below on a positive-mass patch. All smooth zeroth-order terms vanish there. In the affine nonlinear endpoint `R(T)=S+kappa T+P T+Q(T,T)`, compare R(T) with R(0): S cancels and the algebraic terms vanish on support. They cannot repair representative independence. A variable base can be treated locally on `Z={(x,a g_x)}` using the held metric-compatible horizontal lift; no global trivialization is needed.

**Theorem M.** No nonzero finite metric-only Lorentz-covariant measure supplies an ordinary value-only coefficient state quotient that retains all smooth transverse germs of this actual ambient operator and its unchanged output. This covers every scale law, including delta_g. It does not exclude its use as a reduced-action reference, nor a quotient that discards this output, a chosen extension/domain, other symbols, or an actual physical BRST construction.

### Every finite unrestricted jet tower still needs closure

Let `J_Z^r` retain all derivatives through order r along Z. For each finite r≥0 take `T=chi f^(r+1) beta`. Its r-jet vanishes, but the transverse r-jet of L T contains

`(r+1)! P(df)beta ≠0`.

All differentiated lower terms and coefficient derivatives still multiply a vanishing power of f; the leading term is the sole survivor. Thus there is no operator on unrestricted finite r-jet classes intertwining this L. This is a general jet argument with an actual nonzero native conormal coefficient, not an enumeration of r=0..5. The finite probes only calibrate its factorial formula.

Prescribed relations for the next derivatives, an invariant solution domain, an infinite germ, stronger ambient topology, a genuinely tangential operator, or a changed output are potential escapes. The theorem does not say they fail; it shows that **normalization alone does not supply them**. Even an infinite smooth jet need not determine a smooth germ, and no infinite-jet sufficiency is asserted.

## 5. What the one-way density jet actually selects

The owned `grad_N log rho=H` is the fixed-reference weighted-volume stationarity condition, because

`delta ∫_S rho dVol = ∫_S rho [d log rho(nu)−G(H,nu)] dVol`.

It is not a causal flow equation. Keep this geometric functional distinct from a source action or physical energy.

On the trace-normal tube `y=exp(r/2)g`, the held connection metric pulls back to

`G_tube=exp(r/2)g−dr²`.

It has signature(3,2), not a single-time Lorentzian spacetime. The parameter runs over all real r with no finite-r degeneration of this immersion. This is not a full normal-Jacobi/focal-point theorem. The determinant reference `f0=log rho0=−r` cancels the horizontal volume `exp(r)`, leaving constant weighted volume per dr and infinite total radial mass.

All the natural comparison profiles

`log rho_c=f0+c f0²−f0⁴`

have the same value and required first jet at y=g. On the tube the weighted volume is `exp(c r²−r⁴)`, integrable in r for every finite real c and with second derivative2c at zero. This is a singular ray/tube normalization control, not a smooth finite measure on the full fibre, whose boost divergence remains. No profile is adopted.

For a compactly supported graph r=epsilon chi(x), take epsilon sufficiently small that the determinant factor stays positive and the induced signature is unchanged. The exact local weighted density is

`exp(c r²−r⁴) sqrt(1−exp(−r/2) g^-1(dr,dr)) dVol_g`.

Its second variation is `∫[2c chi²−g^-1(dchi,dchi)]dVol_g`. Thus the same first-jet condition leaves the zero-order response arbitrary even among finite radial profiles. Lorentzian variational signs are not quantum ghost or physical stability verdicts. The first-order condition supplies neither a selected restoring coefficient nor a finite equation-compatible bulk state space.

## 6. Three-state synthesis and continuation

| State | Result |
|---|---|
| ESTABLISHED | Native timelike H and global density first jets are reused; boost-weight cone obstruction, actual singular-state non-descent and all-finite-jet extension burden hold under their stated premises. |
| RULED OUT | Robust closed pointed metric-only Lorentz-covariant cone with horizontal interior; finite invariant value/finite-jet state quotient retaining all smooth native transverse germs and outputs. |
| NOT MODELED / UNDETERMINED | Physical causal cone, observer algebra/positive trace, selected state/normal-jet law, source necessity, horizon identification and physical scale. No SOURCE GU or all-C verdict. |

The product cone, extra-clock cones, finite measures as **references rather than state quotients**, selected domains, and nonlocal observation mechanisms remain distinct survivors. No new choice family, prediction, source claim, ledger verdict or action is introduced. Historical candidate10/4/net6/0 is unchanged and is not a count for all GU.

This completes the bounded basic step4 compatibility question without spending further waves repeating pointwise H or measure classification. A new H1 calculation needs a specified cone/domain/observer trace with its physical bridge. The existing sequence proceeds to step5: whether the owned equations actually make Lambda an integration constant; fixed-volume symmetry alone is not that result.

## Verification

[53 exact controls and deterministic replay](../../lab/process/observer-horizon-certificates.json) bind boost weights, the actual matrix-normal/native-Phi port, real coefficients, finite jet controls and trace variation. [Lean finite cores](../../Lean/GUFormalization/ObserverHorizon.lean) check quotient/pointedness implications and finite arithmetic only. Cone-limit topology, measure localization, arbitrary-order jets and geometric variational arguments remain written proofs requiring independent T1 review. Primary literature is comparison evidence, not a GU transfer or novelty certificate.
