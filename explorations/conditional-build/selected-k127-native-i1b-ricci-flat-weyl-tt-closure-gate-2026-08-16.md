---
title: "Selected-K127 native I1B Ricci-flat Weyl stationarity and TT-closure gate"
status: active_research
doc_type: exact_local_stationary_curved_germ_lower_order_tt_compression_and_leakage_gate
created: "2026-08-16"
registry: lab/process/selected-k127-native-i1b-ricci-flat-weyl-tt-closure-gate.json
probe: tests/channel-swings/selected_k127_native_i1b_ricci_flat_weyl_tt_closure_gate_probe.py
grade: "K127 CONSTRUCTS A NEW LOCAL FIXED-BOUNDARY SAME-I1B CURVED STATIONARY GERM FAMILY: T=0 ON ANY RICCI-FLAT HORIZONTAL METRIC TWO-JET. EXACT K77 ARITHMETIC KILLS THE FULL TRANSLATION RESPONSE ON NONZERO WEYL FIXTURES. AFTER K124 NORMALIZATION, A WEYL-ALIGNED COMMON-TRANSVERSE ONE-RADIAL C_T_H_H RESPONSE HAS LOWER OPERATOR 24 K_PERP I2, SO THE THREE FORMAL K125 ENTRIES COLLAPSE TO ONE CURVATURE PARAMETER; BUT STATIONARITY DOES NOT SELECT K_PERP. THIS RESPONSE IS NOT THE PURE TT HESSIAN AT T=0. A SECOND EXACT RICCI-FLAT FIXTURE SENDS BOTH TT POLARIZATIONS OUTSIDE THE SELECTED PLANE WHILE ITS TWO-BY-TWO COMPRESSION VANISHES, PROVING THAT GENERIC WEYL BACKGROUNDS DO NOT CLOSE THE TWO-FIELD TT RESPONSE. THE SYMMETRIC LOWER POTENTIAL DOES NOT CHANGE THE LOCAL GREEN CURRENT. SOURCE-GLOBAL BACKGROUND LEGALITY, TT/CONSTRAINT CLOSURE, A QUADRATIC FLUCTUATION OWNER, GLOBAL DOMAIN, BFV AND SUPERPOSITION REMAIN OPEN K128."
target_claim: K126_NEXT_GATE__SELECT_STATIONARY_CURVED_BACKGROUND_JET_AND_COMPUTE_SAME_I1B_LOWER_ORDER_TT_ENDOMORPHISM_WITH_CARTAN_DOMAIN
target_verdict: LOCAL_RICCI_FLAT_T0_STATIONARY_GERM_FAMILY_EXACT__ALIGNED_ONE_RADIAL_TT_RESPONSE_24_KPERP_I2__NOT_PURE_TT_HESSIAN_AT_T0__KPERP_UNSELECTED__GENERIC_WEYL_LEAKS_OFF_TT__GLOBAL_BACKGROUND_DOMAIN_BFV_OPEN_K128
canon_verdict_change: none
---

# Selected-K127 native I1B Ricci-flat Weyl stationarity and TT-closure gate

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> first-transgression, Ricci-flat metric-jet, spin-Levi-Civita and
> variational-Cartan calculation. Ordinary Higgs/VEV, family-index, chirality,
> anomaly, symmetry-breaking and familiar four-dimensional particle-model
> constructions do not adjudicate it. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

## Result in plain English

K127 finds a real curved stationary input for the local `I1B` calculation,
but it is a family rather than a selected background.

On the native Levi-Civita graph, set augmented torsion `T=0` and take a
four-dimensional horizontal metric two-jet whose curvature is Ricci-flat but
has nonzero Weyl tensor. Then the selected K77 Shiab response vanishes as a
full Clifford-valued object, not merely after radial contraction. At `T=0`
direct `B`, metric-coefficient, pairing, frame and density variations retain
a factor of `T`. In source coordinates `(g,varpi)`, the metric-induced
`delta T` chain term instead pairs with the already-zero translation Euler
row. The result is therefore an exact local bulk stationary germ for
compactly supported or fixed-boundary variations.

This does not pick one Weyl tensor. For an aligned common-transverse family
with transverse sectional curvature

```text
K_perp=R_1212,
```

the Ricci-flat Lichnerowicz correction sends both plus and cross to
`-K_perp` times themselves. Calibrating to K124's principal operator gives

```text
P_t|TT=-12 Box I_2+24 K_perp I_2.                    (1)
```

Thus K125's formal symmetric `[[a,c],[c,b]]` lower block is not three free
entries on this stationary aligned family. It collapses to one scalar
curvature parameter. But every real `K_perp` has an exact algebraic
Ricci-flat metric two-jet, so stationarity alone does not choose its value or
sign.

Equation (1) is the curved completion of K124's trilinear one-radial
`C_t_h_h` response. It is not the pure TT Hessian at the `T=0` stationary
germ. A physical TT fluctuation Hessian requires a selected nonzero radial
background or another quadratic owner.

There is a second obstruction. A generic Ricci-flat Weyl tensor need not
preserve the selected plus/cross plane. K127 constructs an exact stationary
fixture whose compressed two-by-two block is zero while the full curvature
operator sends plus and cross into `13` and `23` metric components. A
symmetric TT compression is therefore not yet a closed two-field pencil.

The honest K127 result is:

```text
local stationary curved germ:       constructed;
aligned one-radial lower response:  one-parameter, 24 K_perp I_2;
value of K_perp:                     unselected;
generic TT invariance:               false;
local Green representative:          unchanged;
source-global background/domain/BFV: open.
```

## 1. Layer-0 packet

| object | exact meaning here | not identified with |
| --- | --- | --- |
| background | one local horizontal metric two-jet with `T=0` | a source-global solution or physical vacuum |
| Ricci-flat | full horizontal Ricci tensor zero | flat Riemann tensor |
| Weyl parameter `K_perp` | `R_1212` in the selected transverse plane | a mass, measured scale or selected datum |
| TT compression | DeWitt projection to plus/cross | proof that the full Hessian preserves that subspace |
| radial-response operator | curved `C_t_h_h` with one `Phi1` leg | the pure TT Hessian at `T=0` |
| fixed-boundary grade | compact support or fixed endpoint variation | global self-adjoint/BFV domain |
| superposition | downstream positive physical cohomology hypothesis | a consequence of a two-mode compression |

K105's current-carrier census is not contradicted. That result exhausted
currently serialized backgrounds eligible for the source-global `VRS-5`
continuation. K127 is a new local metric-jet construction with no global
`B(epsilon)`/`Y=Met(X)` legality or boundary completion.

## 2. Exact stationary Ricci-flat family

Let `E` be a symmetric trace-free three-by-three electric Weyl tensor. The
probe builds

```text
R_0i0j=E_ij,
R_ijkl=-epsilon_ijm epsilon_kln E_mn,
```

with all Riemann symmetries. It verifies the first Bianchi identity, zero
Ricci tensor and zero scalar curvature. The normal-coordinate metric two-jet

```text
g_mn,ab=-(1/3)(R_manb+R_mbna)                         (2)
```

reconstructs the same Riemann tensor exactly, so these are genuine local
metric jets rather than abstract endomorphism fixtures.

After raising the internal curvature indices and embedding into the exact
real `Cl(7,7)` carrier, the selected `comm/symi/symi` Shiab gives

```text
S(F_B)=0                                               (3)
```

on every tested nonzero Ricci-flat member. At `T=0`, equation (3) kills the
entire translation derivative of

```text
I1B=<T,S(F_B+(1/2)D_B T+(1/3)T^2)>+(kappa_1/2)<T,*T>.
```

Direct `B`, metric-coefficient, pairing, frame and density derivatives still
multiply `T` and vanish at the germ. In the source variables `(g,varpi)`, the
metric-induced `delta T` contribution pairs with the zero translation Euler
row from (3). This proves local bulk stationarity. It does not prove a global
section, complete source observation graph, bounded action or physical state.

## 3. Aligned TT compression

Choose

```text
E=diag(K_perp/2,K_perp/2,-K_perp).
```

Then `R_1212=K_perp`, and direct index contraction gives

```text
Riem(H_plus) =-K_perp H_plus,
Riem(H_cross)=-K_perp H_cross.                        (4)
```

K124 fixed the one-radial response normalization as `-12 Box`. The Ricci-flat
Lichnerowicz combination has curvature term `-24 Riem`, so (4) yields (1).
In the unnormalized plus/cross basis the bilinear diagonal is
`48 K_perp`, because each polarization has DeWitt norm two. Crossed entries
vanish.

The conditional radial-response characteristic factor is therefore

```text
det(P_TT-z I_2)=(-12 q^2+24 K_perp-z)^2.              (5)
```

Equation (5) is not a physical spectrum or the pure TT Hessian at `T=0`.
It is the characteristic factor of the one-radial response compression;
`K_perp` is arbitrary at local stationarity, no nonzero radial background is
selected, and no global operator domain has been chosen.

## 4. The planted TT-closure failure

The aligned fixture is deliberately not treated as generic. Set instead

```text
E_13=E_31=1,
all other E_ij=0.
```

This is again exact symmetric trace-free Ricci-flat Weyl curvature and again
has zero full K77 translation response. But its curvature action is

```text
Riem(H_plus)  =-(dx1 odot dx3),
Riem(H_cross) =-(dx2 odot dx3).                       (6)
```

Both outputs are DeWitt-orthogonal to plus/cross. Hence the compressed
two-by-two matrix is zero although the full action is nonzero. This fires the
planted failure:

```text
symmetric two-by-two compression
    does not imply
invariant two-field TT subsystem.                     (7)
```

A unique two-field pencil now requires either a background whose Weyl tensor
preserves the polarization plane or a complete gauge/constraint reduction
that proves the leaked components are removed or solved.

## 5. Cartan and domain result

Any symmetric algebraic lower-order potential `E` cancels from the Lagrange
identity:

```text
<H1,E H2>-<E H1,H2>=0.
```

Therefore K124's covariant principal Green current remains a valid local
representative:

```text
j^mu=-12(<H1,nabla^mu H2>_DW-<nabla^mu H1,H2>_DW).    (8)
```

K127 selects compact-support or fixed-boundary variation only to make the
local bulk stationarity calculation legal. It does not select a global
maximal/minimal operator domain, boundary condition, corner term, BFV charge
or positive physical pairing.

## 6. Twenty-lens synthesis

The reassessment compared four hypotheses:

```text
H_A current evidence selects all three entries of a closed radial-response TT endomorphism;
H_B stationary Ricci-flat geometry reduces the aligned compression to one
    unselected curvature scalar, while generic Weyl curvature leaks off TT;
H_C no curved same-I1B stationary germ exists at current grade;
H_D an arbitrary symmetric 2x2 compression may be used conditionally.
```

| lenses | strongest result |
| --- | --- |
| source criticism, action custody, variational calculus, exact K77 algebra | `H_B` |
| differential geometry, metric-jet realization, representation theory, TT decomposition | `H_B` |
| PDE, Green/Cartan, constraint analysis, domain theory | `H_B` |
| hostile falsification, model selection, identifiability, covariance | `H_B` |
| observation semantics, BV/BFV, superposition strategy, program sequencing | `H_B` |

Vote: `H_A=0`, `H_B=20`, `H_C=0`, `H_D=0`.

Highest conviction is split across two statements rather than the vote alone:

1. **Existence:** nonflat Ricci-flat `T=0` local stationary `I1B` germs are
   exact at fixed-boundary grade.
2. **Nonselection:** neither the Weyl sectional curvature nor TT invariance is
   selected by stationarity.
3. **Structural correction:** the aligned projected lower block is one scalar
   times identity, not three independent entries.
4. **Closure warning:** a projected matrix can hide live off-TT response.

## 7. Reverse scaffold

Retaining Variancer's reverse conditional beginning with the superposition
hypothesis:

```text
S0 superposition hypothesis:
   observable superposition, if GU derives it, lives in positive physical
   cohomology of one source-native linearized theory.

S1 necessary background:
   construct a source/action-stationary curved germ before interpreting modes.

S2 K127 local completion:
   T=0 Ricci-flat fixed-boundary I1B germs exist exactly.

S3 K127 response:
   aligned one-radial TT compression is -12 Box I2+24 K_perp I2;
   generic Weyl curvature leaks outside plus/cross.

S4 K128 closure condition:
   select or derive a source-global Weyl-aligned background, or perform the
   complete metric constraint/gauge reduction and prove what happens to the
   leaked components.

S5 analytic condition:
   choose one common closed Green/Krein domain and boundary representative.

S6 physical condition:
   construct BV-BFV cohomology and a positive conserved pairing.

S7 only then:
   test complex structure, state superposition and the 2D-to-98D attachment.
```

K128 should not fit `K_perp`, import the `I_sc` curvature/VEV horn, or assume
the aligned fixture is generic. Its cheapest exact discriminator is the
source/observation legality and constraint closure of the Ricci-flat Weyl
family.

## K128 successor classification

K128 proves the exact action-degree correction that the present artifact left
open. In native `(g,T)` coordinates, `I1B(g,0)=0` identically, so the pure
metric Hessian at every K127 germ is zero. The actual quadratic fluctuation
operator is coupled, `[[0,A*],[A,C]]`, while this artifact's aligned
`24 K_perp I_2` response is the third derivative `D3[t,h,h]`. Eliminating
distortion gives `-A* C^{-1} A` only after the actual `C`, its kernel/gauge
quotient, boundary adjoint and a common closed domain are selected. K129 owns
that coefficientwise evaluation. K127's stationary family, aligned radial
response and generic Weyl leakage remain unchanged.

No ledger, canon, particle interpretation, phenomenology or GU truth-status
claim changes.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k127_native_i1b_ricci_flat_weyl_tt_closure_gate_probe.py
```
