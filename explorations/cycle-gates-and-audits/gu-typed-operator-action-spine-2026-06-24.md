---
title: "GU Typed Operator/Action Spine"
date: 2026-06-24
status: exploration/canonical-proposal
doc_type: research_spine
verdict: "CANONICAL_PROPOSAL_NOT_PROOF_GRADE"
owned_path: "explorations/cycle-gates-and-audits/gu-typed-operator-action-spine-2026-06-24.md"
depends_on:
  - "explorations/persona-and-dialectic/persona-review-cross-panel-synthesis-2026-06-24.md"
  - "explorations/vz-evasion/vz-principal-symbol-convention-reconciliation-2026-06-24.md"
  - "explorations/vz-evasion/vz-proof-grade-verification-gate-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/gu-minimal-action-spec-2026-06-24.md"
  - "explorations/misc/ig-dynamics-nonzero-theta-action-gate-2026-06-24.md"
  - "explorations/generation-sector/generation-count-rs-symbol-index-contract-2026-06-24.md"
  - "RESEARCH-STATUS.md"
  - "CANON.md"
---

# GU Typed Operator/Action Spine

## Verdict

This is a canonical proposal for a typed GU operator/action spine. It is not a canon
promotion and not proof-grade closure.

The proposal is deliberately narrow:

```text
Use one typed carrier:
  Y = Met_Lor(X), g_Y = gimmel metric of signature (9,5),
  P -> Y with G = Sp(64), spinor bundle S = S^+ plus S^-,
  section s: X -> Y, connection A, IG data (epsilon,beta), spinor field Psi.

Use one rolled-up first-order 0/1-sector operator:
  D_roll(u,psi) = (d_A^* psi, d_A u + Phi_2(d_A psi)) + Z_A(u,psi).

Keep four symbols separate:
  Phi_2                 zero-order algebraic shiab
  Phi_d := Phi_2 o d_A  first-order differential composite
  Phi_F := Phi_2(F_A otimes -)  zero-order curvature insertion
  F_xi := sigma_1(Phi_d)(xi)    principal-symbol block, not curvature
```

This spine makes the VZ convention coherent if the actual GU operator contains
`Phi_d` with the stated coefficient. It does not prove that Weinstein's written action
or the repo canon forces that operator. The remaining gates stay open:

```text
14D VZ:                 conditionally evaded, not upgraded
RS generation index:    open
exact GR/FLRW action:   open, blocked on IG variation and reductions
Pati-Salam CHSH:        ansatz/control only until GU supplies rho_AB and observables
Type II_1 selector:     open; cardinality-only selectors filtered out
```

## 1. Carrier Spine

### 1.1 Base and fiber

Fixed base:

```text
X = X^4
```

where `X` is a smooth oriented 4-manifold.

Metric bundle:

```text
pi: Y -> X
Y = Met_Lor(X)
Y_x = {Lorentzian metrics on T_x X}
    subset Sym^2(T_x^* X)
dim Y_x = 10
dim Y = 14
```

The total space carries the canonical candidate gimmel metric:

```text
g_Y = horizontal tautological metric
      plus trace-reversed Frobenius metric on vertical fibers
signature(g_Y) = (9,5)
```

This file treats `g_Y` as fixed background geometry. If a primary GU source varies
`g_Y` independently, this spine is incomplete and the action must be enlarged by an
`E_{g_Y}=0` equation.

Vertical and horizontal bundles:

```text
VY = ker(d pi) ~= pi^* Sym^2(T^*X)
HY = chosen tautological/Ehresmann horizontal complement
TY = HY plus VY
```

The `HY plus VY` splitting is carrier data for section pullback and for separating
horizontal spacetime variables from vertical metric-fiber variables. The proof-grade
status of any physical reduction depends on the actual horizontal convention.

### 1.2 Principal, spin, and associated bundles

Gauge group and principal bundle:

```text
G = Sp(64)
P -> Y
ad P = P x_Ad sp(64)
```

Spinor bundle:

```text
Cl(TY,g_Y) has type Cl(9,5) ~= M(64,H)
S = P_Spin x_{Spin(9,5)} H^64
S = S^+ plus S^-
rank_H(S) = 64
rank_H(S^+) = rank_H(S^-) = 32
```

The chirality splitting is used below as a principal-symbol typing convention. Any
`Sp(64)` connection component that mixes this splitting is lower-order in the
principal-symbol calculation, but it is not harmless for a full action. A proof-grade
operator must state whether the physical `A` preserves, mixes, or is projected against
this chirality splitting.

Form-spinor bundles:

```text
E_p^eta = Lambda^p T^*Y otimes S^eta,       eta in {+,-}
Omega^p(Y,S^eta) = Gamma(E_p^eta)
```

For gauge-coupled fields one uses the connection induced by `A` and the spin/gimmel
connection. This note writes it schematically as:

```text
d_A: Omega^p(Y,S^eta) -> Omega^{p+1}(Y,S^eta) + lower-order chirality-mixing terms
d_A^*: Omega^p(Y,S^eta) -> Omega^{p-1}(Y,S^eta) + lower-order chirality-mixing terms
```

The principal part of `d_A` and `d_A^*` preserves the coefficient chirality. Any
connection coefficient, spin-connection, mass, extrinsic, or gauge-mixing contribution
is placed in `Z_A`.

### 1.3 Section pullback

A section

```text
s: X -> Y
pi o s = id_X
```

is the same data as a Lorentzian metric on `X`:

```text
g = s^* g_Y
```

Pullback carrier:

```text
P_s = s^*P -> X
S_s = s^*S
A_s = s^*A
F_s = s^*F_A = F_{A_s}
theta_s = s^*theta
Psi_s = s^*Psi
```

The section also supplies the normal bundle:

```text
N_s = s^*VY ~= Sym^2(T^*X)
```

and, after a soldering/representation map,

```text
j_s: N_s -> ad P_s
```

when an `ad P_s`-valued normal source is needed. The normalization of `j_s` is not
free bookkeeping: the older raw Clifford-trace convention can carry a factor such as
`512`. Any 4D Newton constant or `xi_eff` readout must carry this normalization.

### 1.4 Horizontal-normalized second fundamental form

The action convention in this spine is not the raw graph second fundamental form. It is
the horizontal-normalized form:

```text
B_s := II_s^H in Gamma(Sym^2 T^*X otimes N_s)
```

with defining normalization:

```text
II_s^H = 0
```

for the tautological flat Levi-Civita section.

Equivalently, in a moving-frame linearization:

```text
(II_s^H)_{ab}^{(cd)} = (nabla^g_{e_a} theta_b)^{(cd)}
```

up to the chosen horizontal/reference subtraction. This is a carrier convention, not a
derived physical theorem. If a later primary action uses raw `II_s`, all Schwarzschild,
Kerr, and FLRW reductions must be rerun.

## 2. Independent Variables and Variation Status

This spine distinguishes carrier data, derived fields, and independent variations.

| Object | Type | Status in this spine | Variation rule |
|---|---|---|---|
| `X` | smooth oriented 4-manifold | fixed | not varied |
| `Y = Met_Lor(X)` | metric bundle | fixed carrier | not varied |
| `g_Y` | gimmel metric on `Y` | fixed in baseline | `delta g_Y = 0`; open branch if primary source varies it |
| `P -> Y`, `S -> Y` | principal/spinor bundles | fixed topological carrier | not varied except through fields |
| `Phi_2` | algebraic shiab | fixed natural map | not varied |
| `s: X -> Y` | section, physical metric | dynamical for 4D gates | `delta s` allowed subject to boundary data |
| `A` | `Sp(64)` connection on `P` | dynamical | `delta A` allowed subject to gauge/boundary rule |
| `F_A` | curvature of `A` | derived | varies through `A` |
| `epsilon` | IG/gauge variable | open/constrained | no free variation unless `S_IG` supplied |
| `beta` | IG translation field in `Omega^1(Y,ad P)` | open/constrained | free variation with only `|theta|^2` is forbidden |
| `theta` | `A - Gamma(epsilon) - Ad(epsilon^-1) beta` | derived | varies through `A,epsilon,beta` |
| `Psi` | spinor/form-spinor field | dynamical | `delta Psi` allowed; vacuum branch sets `Psi=0` only after consistency |
| `B_s = II_s^H` | section curvature | derived from `s` | varies through `s` |

The main IG warning is binding:

```text
S_theta = -c_theta/2 int_Y |theta|^2
theta = A - Gamma(epsilon) - Ad(epsilon^-1) beta
```

with freely varied `beta` gives:

```text
E_beta = 0  <=>  theta = 0.
```

Therefore the baseline spine does not permit "free beta plus only a theta norm" as a
nonzero-theta dark-energy branch. One of the following must be supplied:

```text
Branch 1: epsilon,beta fixed/Stueckelberg background data.
Branch 2: epsilon,beta constrained on an A-independent geometric/IG slice.
Branch 3: epsilon,beta dynamical with S_IG-dyn, changing the A-source equation.
```

The conservative candidate branch is Branch 2A:

```text
epsilon,beta constrained by Phi_IG(epsilon,beta,s)=0,
Phi_IG independent of A,
beta not a free auxiliary field,
E_A keeps the form D_A^*F_A = theta after normalization.
```

This is a recommendation, not canon. It must be primary-sourced or geometrically forced.

## 3. Four Distinct Phi Objects

### 3.1 Algebraic shiab `Phi_2`

The algebraic shiab is the zero-order map:

```text
Phi_2^eta: Omega^2(Y,S^eta) -> Omega^1(Y,S^{-eta})
```

with local formula:

```text
(Phi_2(alpha otimes psi))_A = c(i_{e_A} alpha) psi.
```

Here `c` is Clifford multiplication and `i_{e_A}` is interior product. Because
Clifford multiplication by a one-form is odd, this map flips chirality.

Order in `psi`:

```text
0
```

Principal symbol:

```text
none
```

The `ad P`-coupled curvature insertion uses the same contraction pattern after the
chosen representation/soldering of `ad P` into endomorphisms of `S`. Its exact
chirality behavior is part of the representation convention and is treated as
lower-order for `D_roll`.

### 3.2 Differential composite `Phi_d`

Define:

```text
Phi_d^eta := Phi_2^eta o d_A
Phi_d^eta: Omega^1(Y,S^eta) -> Omega^1(Y,S^{-eta})
```

This is first order because `d_A` is first order. Its connection coefficient part is
zero order; the homogeneous order-one part comes from the exterior derivative:

```text
sigma_1(d_A)(xi) psi = xi wedge psi.
```

Thus:

```text
sigma_1(Phi_d^eta)(xi) = F_xi^eta.
```

### 3.3 Curvature insertion `Phi_F`

Define:

```text
Phi_F(A) := Phi_2(F_A otimes -)
```

schematically as a zero-order map on form-spinors:

```text
Phi_F(A): Omega^1(Y,S^eta) -> Omega^1(Y,S^{?})
```

where the target chirality is fixed by the actual `Sp(64)` representation convention.
In the VZ principal-symbol problem with background `A` fixed, `F_A` is a coefficient.
Therefore:

```text
order in psi = 0
sigma_1(Phi_F) = 0
```

If `A` is varied in the action, `F_A` contains derivatives of `A`, but that is not a
derivative of the spinor/RS field in the VZ characteristic problem. `Phi_F` cannot be
used as the source of the VZ `F_xi` block.

### 3.4 Principal-symbol block `F_xi`

`F_xi` is not curvature. It is:

```text
F_xi^eta := sigma_1(Phi_d^eta)(xi)
```

For `psi = e^B otimes psi_B`:

```text
(F_xi psi)_A = xi_A gamma^B psi_B - gamma(xi) psi_A.
```

This uses the wedge convention:

```text
i_{e_A}(xi wedge beta) = xi_A beta - beta_A xi.
```

Typing:

```text
F_xi^eta: T^*Y otimes S^eta -> T^*Y otimes S^{-eta}
```

Order:

```text
homogeneous degree 1 in xi
```

This is the only object among the four that supplies the VZ one-form-to-one-form
principal-symbol block.

## 4. Candidate Rolled-Up First-Order Operator

### 4.1 Domain, codomain, and chirality

For each chirality sign `epsilon in {+,-}`, define:

```text
E_roll^epsilon =
  E_0^epsilon plus E_1^{-epsilon}
  =
  S^epsilon plus (T^*Y otimes S^{-epsilon})

F_roll^epsilon =
  E_0^{-epsilon} plus E_1^epsilon
  =
  S^{-epsilon} plus (T^*Y otimes S^epsilon)
```

The candidate rolled-up operator is:

```text
D_roll^epsilon:
  Gamma(E_roll^epsilon) -> Gamma(F_roll^epsilon)
```

Thus the input pair is:

```text
u   in Omega^0(Y,S^epsilon)
psi in Omega^1(Y,S^{-epsilon})
```

and the output pair is:

```text
scalar output    in Omega^0(Y,S^{-epsilon})
one-form output  in Omega^1(Y,S^epsilon)
```

The operator is odd with respect to the above chirality packaging.

### 4.2 Formula

The candidate formula is:

```text
D_roll^epsilon(u,psi)
  =
  (
    d_A^* psi,
    d_A u + Phi_2(d_A psi)
  )
  + Z_A^epsilon(u,psi).
```

Equivalently:

```text
D_roll^epsilon(u,psi)
  =
  (
    d_A^* psi,
    d_A u + Phi_d^{-epsilon} psi
  )
  + Z_A^epsilon(u,psi).
```

Order:

```text
first order
```

Principal symbol:

```text
sigma_1(D_roll^epsilon)(xi)(u,psi)
  =
  (
    i_xi psi,
    xi otimes u + F_xi psi
  ).
```

This is exactly the principal-symbol convention needed by the VZ E-block files.

### 4.3 Lower-order block `Z_A`

`Z_A^epsilon` is not decoration. It is the mandatory home for every term that does not
belong to the order-one symbol above:

```text
Z_A^epsilon =
  connection coefficient pieces inside d_A and d_A^*
  + spin/gimmel connection terms
  + possible chirality-mixing Sp(64) connection coefficients
  + mass terms
  + gauge-fixing or constraint blocks
  + Phi_F(A) curvature insertion
  + theta/IG terms
  + section-pullback and II_s^H/extrinsic terms
  + fermion-current or background-source terms
  + boundary/APS lower-order data after reduction
```

The VZ principal-symbol computation may ignore `Z_A`. The full dynamical/action problem
may not.

### 4.4 Coefficient warning

The spine uses coefficient `+1` in:

```text
d_A u + Phi_2(d_A psi).
```

A more general operator could contain:

```text
d_A u + lambda_d Phi_2(d_A psi).
```

If `lambda_d = 0`, the current VZ `F_xi` E-block is not the actual operator's E-block.
If `lambda_d != 1`, the numerical E-block coefficients must be rederived. Therefore
proof-grade VZ closure requires the primary operator/action to fix this coefficient and
normalization, not merely to permit the term.

### 4.5 Relation to a full `D_GU`

This file does not assert:

```text
D_GU = D_roll
```

as canon. It asserts the minimum typed convention under which the current VZ symbol
language is coherent:

```text
D_GU has, on the relevant 0/1 sector and at principal-symbol order,
the same first-order block as D_roll.
```

If the actual GU operator has only `Phi_F(A)` and not `Phi_d`, downstream VZ claims
using `F_xi` must be rederived from scratch.

## 5. Candidate Minimal Action Schematic

### 5.1 Action form

The candidate action spine is:

```text
S_GU^spine[s,A,epsilon,beta,Psi]
  =
  S_YM[A]
  + S_DD[A,Psi;D_roll]
  + S_theta[A,epsilon,beta]
  + S_W[s]
  + S_IG[epsilon,beta;s,A]
  + S_cross
  + S_boundary.
```

Baseline terms:

```text
S_YM[A]
  =
  -1/(4 g_A^2) int_Y dvol_gY <F_A,F_A>_sp

S_DD[A,Psi;D_roll]
  =
  int_Y dvol_gY <Psi, D_roll(A) Psi>

S_theta[A,epsilon,beta]
  =
  -c_theta/2 int_Y dvol_gY <theta,theta>_sp

theta
  =
  A - Gamma(epsilon) - Ad(epsilon^-1) beta

S_W[s]
  =
  alpha_W/2 int_X dvol_g |II_s^H|^2
```

`S_IG` is a required open slot, not optional decoration, unless `epsilon,beta` are
declared fixed or constrained non-dynamical data by a primary source.

`S_cross` is the placeholder for primary-sourced cross terms. In the baseline branch,
the following are excluded unless explicitly forced:

```text
bare 4D or 14D R theta^2 term
bare Lambda term
theta * D_A^*F_A term
D_A theta * F_A term
torsion/theta invariants with free coefficients
```

The baseline branch excludes them so the FLRW `xi` gate can test generation by the GU
reduction rather than insertion by hand.

### 5.2 Euler-Lagrange tuple

The minimal variational tuple is:

```text
(E_s, E_A, E_epsilon, E_beta, E_Psi) = 0.
```

Schematic equations:

```text
E_A =
  g_A^-2 D_A^*F_A
  - c_theta theta
  + J_Psi
  + E_A^W
  + E_A^IG
  + E_A^cross
  = 0

E_s =
  delta_s S_W
  + delta_s S_YM
  + delta_s S_DD
  + delta_s S_theta
  + delta_s S_IG
  + delta_s S_cross
  = 0

E_epsilon =
  delta_epsilon(S_theta + S_IG + S_DD + S_cross)
  = 0

E_beta =
  delta_beta(S_theta + S_IG + S_cross)
  = 0

E_Psi =
  D_roll(A) Psi + lower-order adjoint/nonlinear terms
  = 0
```

If `epsilon,beta` are fixed, `E_epsilon,E_beta` are omitted but their background
gauge/Noether cost must be stated. If they are constrained, multiplier equations must be
included. If they are dynamical, the conserved source is generally a total current
`theta_eff`, not bare `theta`.

### 5.3 Variation-status ledger for the action

| Field/block | Baseline status | Allowed only if... | Failure if... |
|---|---|---|---|
| `s` | dynamical | boundary data fixed for GR/FLRW test | exact GR claimed without `E_s=0` |
| `A` | dynamical | gauge/boundary rule stated | `D_A^*F_A=theta` asserted without variation |
| `Psi` | dynamical | vacuum branch proves `Psi=0` consistent | fermion stress silently discarded |
| `epsilon` | open/constrained | primary or geometric IG slice supplied | varied freely with no `S_IG` |
| `beta` | open/constrained | beta variations do not span all `Omega^1(Y,ad P)` unless dynamics present | free beta plus only `|theta|^2` forces `theta=0` |
| `theta` | derived | may be promoted to independent parent variable only with constraint equation | treated as independent and derived simultaneously |
| `II_s^H` | derived from `s` | horizontal normalization fixed | raw `II_s` mixed with normalized one |
| `Phi_d` coefficient | fixed as `+1` in proposal | primary operator/action fixes same normalization | VZ E-block imported with different coefficient |

## 6. What This Spine Supplies and Does Not Supply

### 6.1 Velo-Zwanziger lane

What the spine supplies:

```text
1. A typed first-order operator on the 0/1 sector.
2. Domain/codomain chirality:
   S^epsilon plus T^*Y otimes S^{-epsilon}
   -> S^{-epsilon} plus T^*Y otimes S^epsilon.
3. The principal symbol:
   (u,psi) |-> (i_xi psi, xi otimes u + F_xi psi).
4. Clean separation of Phi_d from Phi_F.
5. A named lower-order block Z_A so curvature/extrinsic terms do not contaminate sigma_1.
```

What remains missing:

```text
1. Proof that the actual GU operator/action contains Phi_d with coefficient +1.
2. Proof-grade Q-sector definition and projectors.
3. Independent derivation of the E-block coefficients 1/14 and 13/98.
4. Symbolic two-sided inverse/kernel proof for all non-null mixed covectors.
5. Subprincipal and full dynamical gates involving II_s^H, constraints, and sources.
```

Status after this spine:

```text
VZ convention coherence: improved
14D VZ evasion: still CONDITIONALLY_EVADED
proof-grade FC-VZ-1: still open
```

### 6.2 RS generation-count index lane

What the spine supplies:

```text
1. The ambient spinor bundle S = S^+ plus S^- with right-H structure.
2. The section-pullback internal coefficient candidate:
   s^*S ~= S(3,1) otimes_R S(6,4).
3. The form-spinor 0/1-sector whose one-form component contains RS-type data.
4. A candidate principal-symbol source for a constrained/gauge-fixed RS complex.
5. A clear warning that raw ranks and the VZ symbol are not the APS/K-theory index.
```

What remains missing:

```text
1. Explicit K3 RS bundles E_RS^+ and E_RS^-.
2. Gamma-trace projectors P_+, P_- and their ranks with H-structure verified.
3. Gauge-fixing or ghost/subtraction complex.
4. Ellipticity certificate for the gauge-fixed symbol or elliptic complex.
5. K-theory class [sigma_RS^gf] in K^0_c(T*K3).
6. Characteristic-class computation, including ch_2(F) or proof it vanishes.
7. APS boundary data if any boundary route is used.
8. A final index computed without using 8, 24, rank_eff=4, or three generations as inputs.
```

Status after this spine:

```text
RS index contract: better typed input
generation count: OPEN
```

### 6.3 Exact GR and FLRW action lane

What the spine supplies:

```text
1. A single action schematic with all independent variables visible.
2. A mandatory IG variation-status fork.
3. The horizontal-normalized section curvature B_s = II_s^H.
4. Section-pullback dictionary for A, F_A, theta, Psi, and S.
5. Explicit exclusion of bare R theta^2 and Lambda in the baseline branch.
6. The EL tuple required before Schwarzschild/Kerr or FLRW can be tested.
```

What remains missing:

```text
1. Primary-source or geometry-forced choice of S_IG / constrained IG slice.
2. Complete E_s,E_A,E_epsilon,E_beta,E_Psi equations.
3. Exact Schwarzschild and Kerr vacuum solutions of the full coupled system.
4. Demonstration that the Willmore residual is canceled internally, not relabeled as matter.
5. FLRW reduction to a canonical scalar B(t).
6. Computation of Z_theta, M_KK, xi_eff, Lambda_eff, and self-interactions.
7. Proof that xi_eff < -0.319, or honest failure if it does not.
```

Status after this spine:

```text
weak-field canon: unchanged
exact nonlinear GR: open
FLRW theta dark energy: open
IG free-beta theta-norm branch: structurally broken
```

### 6.4 Pati-Salam CHSH / observer-finality lane

What the spine supplies:

```text
1. The section-pullback representation carrier:
   S(6,4) -> (4,2,1) plus (4-bar,1,2).
2. Candidate finite local Hilbert spaces:
   H_A = C^4_color otimes C^2_SU(2)_L,
   H_B = C^4_anticolor otimes C^2_SU(2)_R.
3. The operator/action source from which zero modes or two-point functions should be derived.
4. A rule that a Bell state inserted by hand is an ansatz, not GU evidence.
```

What remains missing:

```text
1. GU zero-mode projector, propagator, or two-point kernel.
2. Finite reduction map to rho_AB in End(H_A otimes H_B).
3. Physical vacuum/section symmetry status, including CPT/left-right behavior.
4. GU measurement postulate selecting admissible +/-1 local observables.
5. Computed CHSH value from the derived rho_AB and admissible observables.
6. NAC/locality verification for the same measurement scenario.
```

Status after this spine:

```text
CHSH fixture/control: useful
GU-derived CHSH: open
current Pati-Salam Bell states: ansatz only
```

### 6.5 Type II_1 selector lane

What the spine supplies:

```text
1. The smooth GU data a Type II_1 bridge must preserve or replace:
   (s^*S, D_roll or D_GU, chirality, J/H-structure, Pati-Salam content).
2. A Connes-channel target must be typed against this carrier rather than imported.
3. A warning that equal-trace sector labels are not generation derivations.
4. A concrete anti-smuggling interface:
   fixed Type II_1 data -> exactly the finite-control shadow,
   not K_SM tensor C^n after choosing n.
```

What remains missing:

```text
1. Fixed Type II_1 factor/subfactor/standard-invariant data not parameterized by the answer.
2. Functorial map Phi_CC to finite Connes-Chamseddine data.
3. KO/sign bridge compatible with GU's quaternionic structure.
4. Gauge, Higgs, hypercharge, and one-generation module selection.
5. Obstruction to C_n replacement for n != 3.
6. Anomaly/Freed-Hopkins compatibility of the smooth shadow.
```

Status after this spine:

```text
Type II_1 as host: open/possible
Type II_1 as selector: open
cardinality-only selectors: filtered out as non-explanatory
```

## 7. Hegelian Audit

### 7.1 Steelman

The strongest case for this spine is that the repo's live positive lanes are not mainly
missing isolated calculations. They are missing a single typed carrier object. Once the
carrier is fixed, the downstream gates become well-posed:

```text
VZ asks for sigma_1(D_roll).
RS asks for the constrained/gauge-fixed K-theory symbol built from the same carrier.
4D physics asks for S_GU and its section-pullback EL tuple.
CHSH asks for states and observables derived from the same zero modes/propagator.
Type II_1 asks whether another substrate can reproduce or select the same finite-control data.
```

The steelman is that `D_roll + S_GU^spine` turns a pile of promising reconstructions into
a single falsifiable program.

### 7.2 Antithesis

The strongest objection is that this spine may merely canonicalize a convenient choice.

Specific risks:

```text
1. The actual GU operator may contain Phi_F but not Phi_d.
2. The coefficient of Phi_d may differ from +1.
3. A general Sp(64) connection may not respect the chirality bookkeeping needed above.
4. Free IG variation may kill theta unless a real constraint/dynamics is supplied.
5. The action schematic may omit primary-source terms or include terms GU does not allow.
6. Section pullback may not identify theta_s with II_s^H in the needed sense.
7. Downstream lanes may cite the typed proposal as proof rather than as a gate.
```

If any of these occur, the spine is not false as notation, but it fails as canonical
physics.

### 7.3 Synthesis

Use this spine as a proposal-level gate:

```text
All downstream files may cite the typed objects for consistency.
No downstream file may treat them as proof-grade inputs until the relevant closure
condition is met.
```

The synthesis is not "the program is solved." It is:

```text
The program now has a single object against which positive and negative results can bite.
```

That is valuable because it makes failure sharper. For example:

```text
If D_GU lacks Phi_d, the current VZ E-block is not the actual operator's E-block.
If free beta is real, nonzero theta dies in the bare theta-norm branch.
If the RS complex is non-elliptic, the generation index route fails.
If FLRW reduction gives xi_eff >= -0.319, the DESI-sign theta lane fails.
If GU cannot derive rho_AB and observables, CHSH remains a control.
If Type II_1 only returns equal-trace triples, it is a host, not a selector.
```

### 7.4 Closure and falsification conditions

This spine can be promoted only if the following close without changing the definitions:

```text
C1. Primary operator closure:
    A primary GU operator/action fixes D_GU's 0/1 principal block as D_roll
    with Phi_d coefficient +1 or a stated coefficient whose VZ algebra is redone.

C2. Chirality closure:
    The S^+ / S^- bookkeeping is compatible with the physical Sp(64) representation,
    or all chirality-mixing terms are explicitly lower-order/projected.

C3. IG closure:
    epsilon,beta are fixed, constrained, or dynamical in a way that does not
    accidentally force theta=0 unless theta=0 is intended.

C4. VZ closure:
    The Q-sector E-block and inverse/kernel proof are independently verified for all
    non-null mixed 14D covectors.

C5. RS closure:
    The constrained/gauge-fixed K3 RS symbol class is constructed and indexed without
    forbidden target inputs.

C6. 4D action closure:
    The full EL tuple admits exact Schwarzschild and Kerr vacuum branches, or the
    theory accepts their failure as modified gravity.

C7. FLRW closure:
    The written action reduces to a canonical theta scalar and computes xi_eff, with
    pass/fail against the negative-coupling window.

C8. Measurement closure:
    GU supplies rho_AB and admissible CHSH observables; ansatz Bell states remain controls.

C9. Type II_1 closure:
    A fixed-data selector beats the C_n replacement test and functorially supplies
    finite-control data.
```

Falsification/demotion conditions:

```text
F1. D_GU has no Phi_d term: VZ E-block files no longer compute the actual operator.
F2. Free beta plus only |theta|^2 is the actual action: nonzero theta branch fails.
F3. II_s^H is the wrong section convention: 4D reductions must be redone.
F4. RS gauge-fixed symbol is non-elliptic or background-dependent: generation index stays open or fails.
F5. Exact Schwarzschild/Kerr fail the written vacuum EL tuple: nonlinear GR recovery fails.
F6. FLRW reduction gives no sufficiently negative xi_eff: theta dark-energy lane fails.
F7. GU-derived rho_AB gives CHSH <= 2 for admissible settings: physical CHSH forcing fails.
F8. Type II_1 selector survives only by choosing an n-fold object: selector claim fails.
```

## 8. Bottom Line

This file supplies the typed spine the cross-panel synthesis asked for:

```text
carrier:
  X, Y, g_Y, P, S, section s, pullbacks, II_s^H

operators:
  Phi_2, Phi_d, Phi_F, F_xi, D_roll

action:
  S_GU^spine with explicit variation statuses

downstream contracts:
  VZ, RS index, exact GR/FLRW, CHSH, Type II_1
```

It does not close those contracts. The honest verdict remains:

```text
canonical proposal: yes
proof-grade closure: no
```

The next correct use of this spine is to force every downstream lane to say one of:

```text
we are computing this typed object,
we are computing a deliberately different object,
or the claim is not yet well-defined.
```

## Sources Read

- `explorations/persona-and-dialectic/persona-review-cross-panel-synthesis-2026-06-24.md`
- `explorations/vz-evasion/vz-principal-symbol-convention-reconciliation-2026-06-24.md`
- `explorations/vz-evasion/vz-proof-grade-verification-gate-2026-06-24.md`
- `explorations/cycle-gates-and-audits/gu-minimal-action-spec-2026-06-24.md`
- `explorations/misc/ig-dynamics-nonzero-theta-action-gate-2026-06-24.md`
- `explorations/generation-sector/generation-count-rs-symbol-index-contract-2026-06-24.md`
- `RESEARCH-STATUS.md`
- `CANON.md`
- `canon/shiab-existence-cl95.md`
- `explorations/shiab-operator/sc1-shiab-domain-codomain-2026-06-23.md`
- `explorations/geometry-curvature-emergence/4d-reduction-section-pullback-2026-06-22.md`
- `explorations/cycle-gates-and-audits/gu-action-4d-physics-gate-2026-06-24.md`
- `explorations/time-as-finality-crosswalk/observer-finality-physical-forcing-gate-2026-06-24.md`
- `explorations/time-as-finality-crosswalk/observer-finality-gu-derived-chsh-state-attempt-2026-06-24.md`
- `canon/type-ii1-spectral-sm-checklist.md`
- `explorations/type-ii1-spectral/type-ii1-selector-anti-smuggling-theorem-2026-06-24.md`
- `tests/h3_pati_salam_chsh_correlator.py`
