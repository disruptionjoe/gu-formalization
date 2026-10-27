---
title: "Prediction kickoff: complete source/readout pairing for matter motion and light"
status: exploration
claim_verdict: internally_reviewed_conditional_mathematics
doc_type: conditional_response_result
created: "2026-10-27"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: "INTERNAL_TARGET: shared-source motion/light response from a supplied coupled variational packet"
claim_ceiling: "Exact conditional source, detector, boundary and coupled-response identities; supplied finite nonselection and no-slip controls; no source-selected GU matter action, observation, physical quotient, Green domain, prediction or recovery."
probe: tests/channel-swings/prediction_kickoff_matter_light_probe.py
canon_verdict_change: none
ledger_verdict_change: none
---

# One source does not yet fix the motion/light relation

The new result is a complete response formula. Eliminating an independent
distortion field changes both the source and the detector and leaves a contact
contribution. Keeping only the resulting metric operator can therefore change
the observable. The formula identifies what a GU matter/light packet must
provide before a common-action prediction can be certified.

A fixed reciprocal source/readout pairing implies an exchange identity on a
common symmetric domain. It does not determine the ratio of massive-motion
and light responses. An exact countercontrol keeps the first action's zero
pure-metric Hessian block, the source and both readouts while changing that
ratio. One additional no-slip response equation fixes the normalized ratio
to two. At that endpoint the distortion block is singular although the full
coupled system is invertible; a pseudoinverse elimination can lose an equation.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: complete coupled source/readout reduction, Ward-current dual interface and motion/light nonselection control
carrier: supplied metric variations and independent connection-displacement coordinates; four-dimensional LC/spin algebraic control and finite quotient LAYER=toy CHIRALITY=N/A
pairing: action density dual, including moving density, coframe and matter pairing; real coordinate duals only in finite controls ON=declared_variation_spaces
real_structure: real Lorentzian observed control with eta=(-+++); real finite matrices
grading: metric / independent displacement / gauge; no unconstructed odd BV grading
action_owner: repository-construction -- native I1B structural inputs are inherited separately; conditional matter variation and finite response family are supplied
target: source-conjugate response and two fixed metric readouts MAP-TYPE=evaluation
```

The differential identities below are conditional identities for any supplied
action/observed-field packet of the stated type. The concrete probes use toy
carriers. There is no asserted native-to-toy or native-to-observed bridge.

## 1. Custody: inherited and new content

SC-ACT-01 prints the first bosonic action. SC-GEO-55 identifies displacement
from a gauge-rotated Levi-Civita reference, not ordinary torsion. The source
does not release the completed matter coupling, observation/physical-quotient
bridge or these physical readouts. The unfinished up-and-back remark is an
architectural target, not an identity between connection current and stress.

These predecessor results are reused, not booked again:

- `observed-upback-stress-normal-constraint-vacuum-2026-08-05.md` constructs
  action Hilbert stress and separates it from a literal Hessian square.
- `selected-branch-bv-tt-and-curvature-vev-flrw-2026-08-05.md` supplies the
  metric-reference derivative and direct-plus-adjoint source chain.
- `selected-action-stationary-spin-lc-hessian-2026-08-06.md` already corrects
  coordinate-Christoffel rank ten to symmetric-frame spin-LC rank nine.
  `selected-k77-metric-transverse-augmented-torsion-block-2026-08-08.md`
  already identifies six transverse directions. The dual calculation below
  composes those facts; it is not a new rank-nine claim.
- K128 fixes the native `T=0` Hessian as `[[0,A!],[A,C]]`. K1126--K1130
  withdraw older formal-adjoint and independent-`d chi` native-distortion
  objections. None is revived, and no TT-only second action is substituted.
  Those corrections do not promote the earlier repaired action or selected
  Hessian into the native coupled action or a physical response.
- K1866 already proves its positive-scalar Fourier-slip theorem. No scalar
  mass fit or replay of that theorem occurs.

New content is the source-and-detector reduction with its contact term,
the total-source compensator law, the restricted dual-current certificate,
and the coupled discriminator with a singular-block positive endpoint.
These are conditional mathematics, with no novelty claim.

## 2. Freeze the complete source variation

Use independent variables `y=(g,T,epsilon,s,psi)` and

```text
A=B(g,epsilon)+T,
delta A=Lh+t+D_B chi,       L=D_g B,  chi=epsilon^-1 delta epsilon.
```

The observation section `s` is independent unless a relation `s(g)` is
supplied; such a relation contributes its own chain term. Already observed
Hilbert stress must not be pulled back from the ambient space again.
For a supplied matter density schematically written as

```text
S_m=integral mu(g,s) Re[psi^dagger K(g,s) D(g,A,s) psi],
```

the direct metric variation contains `delta mu`, `delta K`, explicit
coframe/Clifford/operator variation `delta_g D`, and any declared section
and matter-trivialization terms. The connection derivative is separate:

```text
delta S_m=<d,h>+<J_A,Lh+t+D_B chi>+<E_s,delta s>
          +<E_psi,delta psi>+integral_boundary Theta_direct,
j_h=d+L!J_A,                 j_t=J_A.                    (1)
```

Here `d` is the complete direct density-dual covector. Formal `!` includes
integration by parts and its boundary term. Holding independent `T` fixed
does not impose Levi-Civita dynamics on the full connection.

A polynomial control exposes each omission: at `g=T=0`, take `mu=1+g`,
`K=1+2g`, `D=1+3g+A`, `B=4g`, `psi=1`. The complete derivative is
`1+2+3+4=10`, with direct row six and soldering return four. This checks
the chain rule; it is not a GU matter model.

For a field-coordinate change `x=F(y)`, the full Hessian law is

```text
H_y[u,v]=H_x[DF u,DF v]+E_x[D2F(u,v)].                    (2)
```

Only at a stationary background can the last term be dropped.

## 3. Compensator and boundary pairing

Write `G=D_B`. If `L'=L+GX`, the isolated current return changes by
`X!G!J`. The same total source has representatives

```text
d'=d-X!G!J,             d'+L'!J=d+L!J.                   (3)
```

Alternatively a separately justified `G!J=0` makes that isolated return
invariant. This does not follow just from calling `GX` gauge. Direct
Lorentz/coframe, matter-Euler and other-owner terms can participate in the
full Ward identity. An independent current conservation law is not assumed.
Boundary flux remains when the gauge parameter or variation is allowed there.

In the flat spin control use pairing
`(1/2) sum_(mu,a,b) J^(mu ab) delta omega_(mu ab)` with `J` antisymmetric
in `a,b`. The exact Green identity has

```text
(L_s h)_(mu ab)=(partial_b h_(mu a)-partial_a h_(mu b))/2,
(L_s!J)^(mu a)=-partial_b J^((mu a)b)/2,
Theta_s^b=J^(mu ab)h_(mu a)/2.                            (4)
```

Parentheses symmetrize the metric indices with weight one half. Storing
only `a<b` gives the equivalent single-count pairing. The probe constructs
polynomial antisymmetric currents and symmetric metric tensors, including
moving off-diagonal entries, then independently differentiates and integrates
the two sides of (4) and its nonzero boundary term. Its removal by
compact support or fixed boundary data is a domain choice, not a BFV result.

## 4. Restricted Ward-current dual: six receiver directions

For nonzero `q`, suppress the Fourier factor `i` only for symbol ranks.
The coordinate and spin maps are related by the moving coframe term:

```text
(L_Gamma h)^a_(mu b)=eta^(ac)(q_mu h_bc+q_b h_mu c-q_c h_mu b)/2,
(L_s h)_(mu ab)=eta_ac(L_Gamma h)^c_(mu b)-q_mu h_ab/2.
```

Known raw ranks are ten and nine. The spin kernel is `span(q tensor q)`:
its defining equation makes every row of `h` proportional to `q`, and
symmetry makes the proportionality covector proportional to `q` too.
Set

```text
(R xi)_mu nu=q_mu xi_nu+q_nu xi_mu,
(G_s chi)_mu ab=q_mu chi_ab,
(Q xi)_ab=(q_b xi_a-q_a xi_b)/2.
```

Then `L_s R=G_s Q`, with ranks `4,6,3` for `R,G_s,Q`. Moreover
`L_s h in im G_s` iff `h in im R`: in a linear basis with `q=(1,0,0,0)`,
the first condition kills all `h_ij` with `i,j>0`, leaving precisely those
four metric-gauge directions. These all-lowered algebraic formulas require
no division by `q`'s Lorentz norm, so the argument includes null `q`.

Consequently the newly composed dual interface is

```text
rank [L_s G_s]=12,
L_s! : ker G_s! -> ker R! is onto,
dim ker G_s!=18,          rank returned source=6,
dim ker(L_s! restricted to ker G_s!)=12.                  (5)
```

The coordinate control has gauge rank sixteen and joint rank twenty-two,
giving the same receiver dimension. Exact finite checks cover timelike,
spacelike and null representatives, the adapters, squares and dual images.
Equation (5) applies only to the stipulated independently Ward-closed current
sector. It does not place the actual GU current there, identify all ambient
chimeric currents with observed spin currents, or make Ward annihilation
sufficient for physical descent. Equation (3) is the broader source law.

## 5. Eliminate a field with both source and detector

Suppose a paired boundary/domain and a genuine gauge reduction are supplied.
On that common quotient write

```text
H=[[B,A!],[A,C]],       H(h,t)=(j_h,j_t),
readout_r(h,t)=<r_h,h>+<r_t,t>.
```

If `C^-1` exists on the stated symmetric common realization, elimination gives

```text
H_eff=B-A!C^-1A,
j_eff=j_h-A!C^-1j_t,       r_eff=r_h-A!C^-1r_t,
response(r,j)=<r_eff,H_eff^-1j_eff>+<r_t,C^-1j_t>.          (6)
```

The last term is the source-source contact contribution left by elimination;
it need not be spacetime-local when `C^-1` is nonlocal. Substitution in the
quadratic action gives

```text
S_eff[h;j]=<h,H_eff h>/2-<j_eff,h>-<j_t,C^-1j_t>/2.
```

Differentiating with respect to a detector/source amplitude produces both
terms in (6). The probe compares this with the full coupled inverse for
nonzero `j_t,r_t`, planting each omitted term separately.

For a retarded realization set `K_ret=C_ret^-1`. Provided this inverse and
the effective retarded inverse exist on the specified compatible source and
field domains, with the required support conditions, block substitution uses

```text
j_eff=j_h-A! K_ret j_t,
r_eff,left=r_h^T-r_t^T K_ret A,
response_ret(r,j)=r_eff,left (B-A! K_ret A)_ret^-1 j_eff
                 +r_t^T K_ret j_t.                      (7)
```

The detector column is `r_h-A! (K_ret)^! r_t`. It can be called the
advanced-inverse transform only after the adjoint identity
`(K_ret)^! = K_adv` has been proved on the chosen paired domains.
Formal action symmetry then licenses retarded/advanced exchange for the
complete system, if its corresponding operators and domains are also proved:

```text
<r,G_ret j>=<j,G_adv r>.
```

It does not generally license same-retarded exchange. Finite matrix controls
verify the left/right factorization and transpose distinction, not an
ambient GU Green operator. No positivity is inferred from reciprocity.

## 6. Fixed-source discriminator retaining the I1B block shape

This is a supplied finite block-completion class. Matching a necessary I1B
shape does not show its coefficients occur in native GU. No member is
selected as a physical action or potential. Take two metric coordinates
`h=(Phi,Psi)`, two independent displacement coordinates `t`, and

```text
G_a=[[1,a],[a,1]],
H_a=[[0,I],[I,-G_a]],       H_a^-1=[[G_a,I],[I,0]].         (8)
```

`H_a` is real symmetric and invertible for every real `a`. Appending one
pure metric gauge coordinate with zero row/column gives exactly that gauge
radical. It introduces no independent distortion gauge direction. This
finite quotient is explicit, unlike the unconstructed native BV/domain one.

Freeze the source and both readouts:

```text
j=(1,0;0,0),      r_motion=(1,0;0,0),
r_light=(1,1;0,0).
```

Injecting a detector as a source uses the same action-conjugate covector;
the metric observation and its adjoint are fixed. Exact inversion yields

```text
(h,t)=(1,a;1,0),
response_motion=1,        response_light=1+a.              (9)
```

At `a=0` and `a=1/2`, `G_a` is positive definite, exchange reciprocity holds,
and the motion calibration is the same. Light responses are one and three
halves. The full coupled Hessian is indefinite; positive `G_a` is a finite
response property, not a physical-state or stability theorem.

One optional supplied observational interpretation uses the static scalar
metric `ds^2=-(1+2Phi)dt^2+(1-2Psi)dx^2`: normalized timelike and transverse
null metric contractions read `Phi` and `Phi+Psi`. At `q=(0,1,0,0)`, both
the rest vector and a null ray along the third spatial axis pair to zero
with `q`, so these source covectors annihilate metric-gauge variations.
Actual acceleration and deflection require their different derivative and
ray-integral weights. Equation (9) compares normalized responses of one fixed
mode; it is not a rotation curve, deflection angle, measured PPN parameter
or GU observable derivation.

## 7. Constructive positive endpoint

Add the one independent response equation

```text
D h=0,       D=(-1,1),       equivalently Psi=Phi.         (10)
```

On (9) this is `a-1=0`. It selects `a=1` within the supplied family and
fixes normalized light/motion to two. The equation is an explicit extra
restriction, not a consequence of reciprocity or a released GU equation.
For a whole source subspace `S`, the corresponding condition is

```text
(r_light-2r_motion) G_full |S=0.                         (11)
```

Replace two by `c` for a desired ratio `c`. One scalar condition is necessary
and sufficient for this single source; it does not settle other profiles,
frequencies or polarizations.

At `a=1`, `C=-G_1` has rank one, but the full inverse still gives
`(h,t)=(1,1;1,0)`. The `t` equation contains the kernel constraint
`h_1-h_2=0`; the `h` equation fixes both components of `t`. A pseudoinverse
reconstruction `(h,t)=(1,1;1/2,1/2)` loses that last equation and fails
the full residual. Thus the constructive endpoint survives while (6), which
requires invertible `C`, is unavailable.

## 8. Verification, consumers and next calculation

The selftesting probe uses exact rational linear algebra and polynomial
identities. A clean baseline must pass before altered operators/inputs run;
only explicit failed mathematical checks count as catches. Finite checks
support concrete controls; arbitrary-covector and operator statements rest
on the written proofs. No empirical numbers, floating-point nulls, proof
assistant or external certification are used. The final probe passes 106 exact
finite checks and rejects 22 altered-input/operator faults. Independent internal
review accepted the written identities and scope after the spin boundary
control and complete retarded formula were made explicit.

Positive consumer: a native packet supplying the complete source/readout,
quotient/domain and a derived condition such as (11) can fix a shared
dimensionless relation without fitting both observations. The full coupled
formula tests it even with a singular distortion block.

Nonselection consumer: if the complete native packet permits two responses
like (9) after its actual coefficients, source maps and domains are fixed,
it has failed to select that relation. The supplied finite family proves
only insufficiency of the named abstract structural conditions; it does
not prove two GU-admissible completions exist.

The next native calculation must instantiate one coupled `I1B` background
with its complete density/pairing/coframe/section source variation, matter
and light readouts, total Ward/boundary pairing and actual reduced or
constrained inverse; then evaluate (11) on the fixed source space. A scalar
potential, raw LC rank or TT-only `I2B` pencil cannot substitute for this
packet. Source polarities, the physics ledger and canon remain unchanged.

Reproduce from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 tests/channel-swings/prediction_kickoff_matter_light_probe.py --selftest
```
