---
artifact_type: construction_result
created: 2026-08-05
status: SELECTED_BRANCH_GAUSS_HESSIAN_EXACT__FULL_WARD_AND_STRESS_CURRENT_CHAIN_TYPED__COUPLED_DEFECT_KREIN_GREEN_DOMAIN_CLOSED__MASSIVE_PARTNER_OPPOSITE_RESIDUE_CLASSIFIED__FULL_BV_PHYSICAL_COHOMOLOGY_AND_TWO_FIELD_COSMOLOGY_OPEN
lane: "1"
functional_channels: [COMPOSE, SOURCE, BUILD, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR2d, LT-GR3, LT-GR5, LT-GR6]
fork_assumed: SIGNATURE_AMBIENT_K77__SELECTED_NONCYCLIC_BRANCH__CANONICAL_GAUSS_FULL_II__OBSERVED_GLOBALLY_HYPERBOLIC_DEFECT_HORN
source_return: SOURCE-CORRECTS
free_object_delta: "zero fields, data, potentials, projectors, boundary selectors or fitted coefficients; P1/P2/P3 unchanged and unused"
scripts:
  - tests/channel-swings/selected_branch_linearized_totalization_domain_probe.py
  - tests/channel-swings/selected_branch_linearized_totalization_domain_independent.sage
registry: lab/process/selected-branch-linearized-totalization-current-green-domain.json
---

# Selected-branch linearized totalization, current and common defect domain

## Result first

The selected K77 branch is substantially better behaved in the gravitational
sector than its radial result suggested, but its distinct partner is not yet
a positive-state particle.

The previous Hessian

\[
 I''(t_*)=-14\kappa_1
\]

is the invariant radial direction in
`C* tensor Cl1(C)`. Gravitational second-fundamental-form perturbations live in
the different carrier

\[
 \operatorname{Sym}^2H^*\otimes V
 \hookrightarrow H^*\otimes\operatorname{Cl}^2(C).
\]

Differentiating the same selected non-cyclic scalar action directly at
`T*=-(kappa_1/312) Phi1` gives the exact Gauss-sector Hessian

\[
 \boxed{
 H_{T_*}|_{\operatorname{tr}II}
   ={100\over117}\kappa_1 G_{II},\qquad
 H_{T_*}|_{II_0}
   ={124\over117}\kappa_1 G_{II}. }
 \tag{1}
\]

The trace sector has dimension ten and the traceless sector dimension ninety.
The native `II` pairing has inertia `(54,46)`, split as
`(6,4)+(48,42)`. Thus the gravitational Hessian is nondegenerate for
`kappa_1 != 0`, with inertia `(54,46)` for positive `kappa_1` and `(46,54)`
for negative `kappa_1`. Changing the sign does not make the full native sector
positive; but the radial negative mode does **not** automatically make the
Gauss/TT partner tachyonic.

On either observed TT polarization the construction-selected pencil becomes

\[
 P_{TT}(z)=
 \begin{pmatrix}
  \alpha_{II}z&z\\
  z&{124\over117}\kappa_1
 \end{pmatrix},
 \quad
 \det P_{TT}
 =z\left({124\over117}\alpha_{II}\kappa_1-z\right). \tag{2}
\]

It retains one simple massless Einstein pole and one distinct massive GU pole
with

\[
 m_{GU}^2={124\over117}\alpha_{II}\kappa_1. \tag{3}
\]

In the declared `z=m^2` convention the partner is non-tachyonic when
`alpha_II*kappa_1>0`. The two standard `z`-plane residues are exactly
`+1/alpha_II` and `-1/alpha_II`. A positive-Hilbert reading therefore calls
one pole ghostlike. GU's active Krein structure keeps this from being an
automatic algebraic kill, but only a BV/constraint physical cohomology can
show whether the negative-metric partner is absent, paired, confined or
physical.

The same wave closes one analytic domain at the correct grade. Keeping the
coupled `(h,v)` system second order, its kinetic matrix is

\[
 K=\begin{pmatrix}\alpha_{II}&1\\1&0\end{pmatrix},
 \qquad \det K=-1.
\]

Multiplication by `K^-1` converts the operator to a scalar wave principal
symbol plus a smooth constant endomorphism. On the inherited globally
hyperbolic observed defect in harmonic gauge, it is normally hyperbolic and
therefore has advanced/retarded Green operators on the common core
`C_c^infinity`, with spacelike-compact Green images. The operator is
Krein-symmetric because the lower-order endomorphism is `K`-self-adjoint.
This is a common **defect** Krein/Green domain; it is not the ambient
ultrahyperbolic `Y14` domain and does not prove positive energy.

Finally, the action-owner chain is now explicit. At a stationary background,
linearizing the complete even Ward identity gives `R^! H=0`. For a connection
depending on metric/soldering data, the physical metric source is

\[
 \boxed{T_{\rm red}=E_g^{\rm direct}+(D_gA)^!J_A.} \tag{4}
\]

Equation (4), not `J_A` alone and not a literal diagonal `VU`, is the typed
connection-current-to-Hilbert-stress chain. The existing Gauss insertion and
its action adjoint close this formula on the selected `II` sector. The full
metric/coframe derivative of the unified soldered connection and its BV
physical quotient remain open.

## Plain English

We had found a nonzero shape of the GU connection that makes the algebraic
action stationary, but one direction looked upside down. That was real, but
it was not the gravitational direction. The action treats the part of the
connection that bends observed spacetime differently. In the trace and
gravitational-wave sectors its exact curvature is `100/117` and `124/117`
times the original coupling, rather than `-1` times it.

That gives the extra gravitational mode a definite mass formula. It also
exposes the actual hard issue: the Einstein pole and its partner have opposite
residues. In ordinary positive-metric language that is a ghost warning. In
GU's indefinite/Krein language it is a demand to construct the physical-state
quotient, not permission to ignore the sign and not an automatic rejection.

We also no longer need to eliminate the auxiliary field and struggle with a
fourth-order equation. The two fields together form an ordinary second-order
wave system with an indefinite field pairing. That system has a clean
advanced/retarded Green domain on observed globally hyperbolic spacetime.

## 1. Pre-wave record

### Fork and cost if wrong

The active fork is K77, the selected non-cyclic `comm/symi/symi` action, the
canonical full-`II` Gauss placement and the observation-first globally
hyperbolic defect horn. The costly wrong inference would be to transfer the
radial `Cl1` Hessian sign to the gravitational `Cl2` carrier. That would
misclassify the massive partner before its actual restriction was computed.

### Search-space theorem

At the invariant background the stabilizer acts on

\[
 \operatorname{Sym}^2H^*\otimes V
 = (\mathbb R g_H\otimes V)\oplus
   (\operatorname{Sym}^2_0H^*\otimes V).
\]

An invariant Hessian has one scalar on each summand. Two representatives plus
held-out positive/negative normal and off-diagonal controls therefore replace
a 100-by-100 brute-force fit. No coefficient search is performed.

### Free objects

`free_object_delta=0`. The background, action, Gauss embedding, current,
stress, Ward owner and defect domain were already owned. No external datum,
new potential, projector or boundary selector is added.

## 2. Layer 0

| phrase | object here | kept distinct |
| --- | --- | --- |
| radial Hessian | invariant `C* tensor Cl1` branch direction | gravitational Gauss Hessian |
| Gauss Hessian | selected action restricted to `Sym2(H*) tensor V` inside `H* tensor Cl2` | vertical `q` receiver and radial branch |
| Hilbert stress | metric/coframe Euler covector | connection current |
| connection current | connection Euler covector | complete Ward totalization |
| current/stress chain | direct metric block plus adjoint soldering derivative | current-only algebraic map |
| common Green domain | coupled second-order observed defect operator | ambient `Y14` Cauchy theory |
| opposite residue | positive-Hilbert ghost warning | proof of failure in a Krein/BV physical quotient |
| direct source susceptibility | response to a source coupled to the algebraic branch | Weinstein's full two-field curvature/VEV identification |

## 3. Exact selected-branch Hessian

Write the selected action on constant fields as

\[
 I(T)=\left\langle T,{1\over3}\mathscr S(T\wedge T)\right\rangle
 +{\kappa_1\over2}\langle T,*T\rangle .
\]

For perturbations `u,v`, the exact second variation is

\[
\begin{aligned}
H_T(u,v)={1\over3}\{&
 \langle u,\mathscr S(vT+Tv)\rangle
 +\langle v,\mathscr S(uT+Tu)\rangle\\
 &+\langle T,\mathscr S(uv+vu)\rangle\}
 +{\kappa_1\over2}
 (\langle u,*v\rangle+\langle v,*u\rangle).
\end{aligned} \tag{5}
\]

The exact Python evaluator and independent Sage reconstruction agree on:

| carrier | Hessian coefficient relative to native pairing |
| --- | ---: |
| invariant `Cl1` trace/radial | `-kappa_1` |
| `Cl1` symmetric traceless | `15*kappa_1/13` |
| `Cl1` antisymmetric | `41*kappa_1/39` |
| Gauss mean-curvature/trace | `100*kappa_1/117` |
| Gauss traceless `II_0` | `124*kappa_1/117` |

The Gauss results are checked on diagonal and off-diagonal representatives and
on both signs of the `(6,4)` normal metric. Cross terms between trace and
traceless representatives vanish. Doubling `kappa_1` doubles the Hessian,
which catches an accidental unit-coupling specialization.

## 4. Complete Ward and stress/current chain

Let all primitive fields be `q`, their Euler covector `E(q)` and the complete
ordinary gauge generator `R(q)`. Gauge invariance gives

\[
 R(q)^!E(q)=0.
\]

At the selected stationary branch `E(q_*)=0`. Differentiating gives

\[
 R(q_*)^!H_{q_*}=0,\qquad H_{q_*}R(q_*)=0, \tag{6}
\]

where the second identity uses Hessian reciprocity. The exact finite control
has kernel equal to the complete gauge image. Replacing the complete generator
by the connection block alone fails.

For matter and a dependent connection `A(g,...)`, the chain rule gives (4).
At a matter-free stationary background its mixed linearization is

\[
 D_\psi T_{\rm red}
 =H^{\rm direct}_{g\psi}+(D_gA)^!H_{A\psi}. \tag{7}
\]

If the background current is nonzero, derivatives of `D_gA` multiply that
current and must also be retained. The exact finite action control verifies
both directions of (7) and fires when the direct term or soldering derivative
is omitted.

The Gauss insertion's adjoint maps the connection equation to the `II`
equation. It does not by itself equal the ordinary metric Hilbert tensor. Full
closure still requires the actual metric/coframe derivative of the unified
connection, including direct Clifford/coframe variation.

## 5. Common defect Krein/Green domain

On each already-isolated plus/cross polarization, use

\[
 P=K\Box+M,
 \quad K=\begin{pmatrix}\alpha_{II}&1\\1&0\end{pmatrix},
 \quad M=\begin{pmatrix}0&0\\0&{124\over117}\kappa_1\end{pmatrix}.
\]

Because `det K=-1`,

\[
 K^{-1}P=\Box\,1+K^{-1}M. \tag{8}
\]

The principal symbol is the scalar Lorentzian wave symbol on both fields;
`K^-1 M` is lower order and `K`-self-adjoint. Standard Green-hyperbolic
theory therefore supplies unique advanced/retarded Green operators on the
inherited globally hyperbolic defect horn. The common domain is the compact
test core with spacelike-compact Green images, tensored with the exact
harmonic/BV quotient already yielding plus/cross.

Equation (8) is more informative than eliminating `v`: elimination produces a
fourth-order metric equation and hides the ordinary coupled hyperbolic system.
Nothing here constructs a spacelike hypersurface in signature `(7,7)` or a
global ambient boundary-value theory.

## 6. Partner and shift classification

Partial fractions give

\[
 (P^{-1})_{hh}
 ={1\over\alpha_{II}z}
 -{1\over\alpha_{II}(z-m_{GU}^2)}. \tag{9}
\]

So the residues are opposite independently of the coupling magnitudes. The
honest classification is:

- `alpha_II*kappa_1>0`: real positive mass-squared in the declared convention,
  with a negative-residue partner on a positive-Hilbert reading;
- `alpha_II*kappa_1<0`: tachyonic sign as well as opposite residue;
- either sign: the coupled operator remains Green-hyperbolic because mass is
  lower order;
- Krein/BV status: open until the physical cohomology and boundary pairing are
  built.

For a direct source `rho` coupled to the algebraic invariant branch,

\[
 4368t^2+14\kappa_1t+\rho=0,
 \qquad
 \left.{dt\over d\rho}\right|_{t_*}={1\over14\kappa_1}. \tag{10}
\]

Thus this branch alone responds rather than screens. Equation (10) does not
test Weinstein's actual magnitude argument, which identifies the dark-energy
field with a curvature-side field and only claims two problems collapse to
one. That two-field parameter-count and FLRW response remain open.

## 7. Seven axes plus Layer 0

| layer | result | boundary |
| --- | --- | --- |
| Layer 0 | seven carrier/owner/domain distinctions exact | no radial-to-Gauss transfer |
| L1 source | `SOURCE-CORRECTS` literal current/stress and partial-totalization readings | source path remains unfinished |
| L2 algebra | five exact Hessian sectors, Gauss inertia, pole factors/residues | physical quotient open |
| L3 geometry | canonical full-II Gauss carrier retained | full metric/coframe connection derivative open |
| L4 variation | complete stationary-branch Ward linearization and chain-rule stress/current formula | nonlinear full-field BV chain open |
| L5 covariance/BV | full even owner linearizes to a tangent complex | odd/diffeomorphism physical cohomology incomplete |
| L6 analytic | coupled observed operator has one common Krein/Green defect domain | positive energy and ambient domain open |
| L7 physics | mass formula, tachyon sign criterion and opposite residues classified | partner acceptability and cosmology open |

## 8. Constraint and progress accounting

| item | result |
| --- | ---: |
| new fields/data/potentials/projectors | 0 |
| fitted coefficients | 0 |
| Gauss trace/traceless sectors solved | `10+90=100` |
| common observed Green domains added | 1 conditional defect domain |
| positive physical-state quotients built | 0 |
| direct-source screening | no; susceptibility nonzero |
| two-field curvature/VEV magnitude test | open |
| P1/P2/P3 | unchanged and unused |

## 9. Hostile disposition and successor

The hostile review accepts the selected Gauss Hessian and common defect domain
after refusing four promotions: radial sign to gravity, Green to positivity,
Gauss-current adjoint to the whole Hilbert tensor, and direct susceptibility to
a refutation of the two-field dark-energy argument.

Next gate:

```text
CONSTRUCT_SELECTED_BRANCH_FULL_METRIC_COFRAME_SOLDERING_DERIVATIVE_AND_BV_PHYSICAL_COHOMOLOGY_FOR_THE_OPPOSITE_RESIDUE_PARTNER__IN_PARALLEL_BUILD_THE_OBSERVED_TWO_FIELD_CURVATURE_VEV_FLRW_PARAMETER_COUNT_AND_SHIFT_RESPONSE
```

The first half decides whether the massive partner is a physical ghost,
paired Krein mode or constrained state. The second tests Weinstein's
dark-energy claim on its actual two-field terms. Neither may spend P1/P2/P3 or
replace the selected two-pole construction with a pure-GR reflex.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_branch_linearized_totalization_domain_probe.py
DOT_SAGE=/private/tmp/gu-selected-branch-totalization-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/selected_branch_linearized_totalization_domain_independent.sage
```
