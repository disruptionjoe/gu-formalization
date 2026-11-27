---
title: Ricci-flat base curvature in the full ambient source jets
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: X-P1-P2
tier: T2
expected_delta: Determine the first nonzero full ambient LC curvature-source response beyond the same-metric section
actual_delta: All Ricci-flat bases have zero relative value and first normal jet; Schwarzschild has a nonzero second normal source jet
class_covered: All smooth Ricci-flat Lorentz four-metrics with the existing source-guided tautological connection metric and native trace reversal one half; coherent LC reference and comparison identifications fixed
premises:
- source-chimeric-trace-compatibility-2026-11-13.md section1 authenticates the source geometry chain and marks its coordinate completion reconstructed
- shiab-bianchi-companion-class-2026-11-27.md sections5-6 owns the Ricci-Einstein restriction in the declared Clifford convention
- printed-shiab-endpoint-audit-2026-11-27.md retains exact-Euler architecture exclusions
source_bridge:
  status: conditional
  reason: The concrete metric is source-guided, not source-unique; coherent LC curvature is not automatically the independently varied printed B, and source response is not the full endpoint residual
kill_condition: A failure of the full Koszul trace or coherent source transfer cancels that claimed implication; no all-completion or GU exclusion follows from a source jet
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Ricci-flat base curvature in the full ambient source jets

program_target: X-P1-P2
tier: T2
expected_delta: Determine the first nonzero full ambient LC curvature-source response
actual_delta: Ricci-flat first-normal cancellation and Schwarzschild second-normal response

**ESTABLISHED in the declared reconstruction:** relative to the matching
flat-base geometry, the complete ambient Ricci and Einstein sources have zero
value and first normal derivative on every Ricci-flat same-metric section.
Schwarzschild curvature appears at second normal order. This is a class-wide
cancellation followed by an explicit nonzero witness, not a black-hole solution
or a no-lift theorem. No world-novelty claim is made.

```gu-typed-objects
result: Ricci-flat ambient source jets
carrier: TY=H4 plus Sym2(T*X)10 of the source-guided metric bundle LAYER=ambient BRIDGE=coherent-LC-spin-identification-conditional CHIRALITY=N/A
pairing: tautological horizontal y and trace-reversed normal K with lambda=1/2 ON=TY
real_structure: real Lorentz geometry; K95 (-+++) and flipped K77 (+---) separately evaluated; no automatic real-adjoint or Hodge-phase transfer
grading: horizontal/normal tensor blocks, not total/observed physical chirality
action_owner: repository-construction -- existing source-guided metric, no new action or displacement
target: full ambient LC Ricci and its declared Shiab restriction MAP-TYPE=intertwiner
```

## 1. Custody and the tested equation term

[Source chimeric trace](source-chimeric-trace-compatibility-2026-11-13.md) §1
pins draft §§3.1–3.4, printed pp17–22/eqs3.7–3.17; §4/eqs3.39–3.42,
4.4–4.6; §6 pp35–36; §11 p50/eq11.4. It distinguishes chimeric C, a
connection-dependent C-to-TY identification, the downstairs LC connection,
its induced upstairs metric and LC reference, and the independently varied
connection. Its concrete coordinate completion is source-guided, not uniquely
selected by the source.

    theta_g=dy-C(Gamma_g)y dx,
    G_g=y(dx,dx)+K_y(theta_g,theta_g),
    K_y(U,V)=tr(y^-1 U y^-1 V)-tr(y^-1 U)tr(y^-1 V)/2.

The horizontal coefficient is y, not frozen g. Compare curved and flat-base
local tensors using the same y, K_y and coherent horizontal/vertical frame.
This is a local jet comparison, not a diffeomorphism between curved and flat
solutions. The observed section is s_g(x)=(x,g_x); its tangent is horizontal.
The normal deformation y=g+s v is in the metric fibre, not a radial spacetime
derivative or approach to a spacetime horizon.

The [Shiab companion theorem](shiab-bianchi-companion-class-2026-11-27.md)
§§5–6 gives +2G14 for the wedge companion and -2G14 for the held selected map
under its injection convention. A spin-curvature factor1/2 changes that
coefficient; real Clifford/Hodge phases must be transported coherently. This
calculation supplies the LC curvature term only. Equating it to a printed B
requires that declared identification. The selected map does not satisfy the
same-cubic/unit-endpoint premise of the conditional Riemann-silence theorem;
that theorem cannot be used to erase its nonzero Ricci response.

## 2. Full Koszul calculation

### Conventions and blocks

Fix the downstairs torsion-free metric connection ∇=∇g. At a base point use a ∇-normal frame. Lift horizontal fields with
`H_i=partial_i+C(Gamma_i)y`, where `C(A)y=A^T y+yA`; then

```
[H_X,H_Y]^V=Omega_y(X,Y)=R(X,Y)^T y+yR(X,Y).
R(X,Y)=∇_X∇_Y-∇_Y∇_X-∇_[X,Y].
Ric(X,Y)=trace[Z -> R(Z,X)Y].
```

Use vertical symmetric matrices U,V, and K_y as above. Their horizontal extension uses ∇; at the chosen base point the mixed brackets vanish. The fibres are totally geodesic with their own LC connection ∇F. Koszul gives

```
(∇Y_X Y)^H=∇_X Y,
(∇Y_X Y)^V=II_y(X,Y)+(1/2)Omega_y(X,Y),
K_y(II_y(X,Y),U)=-(1/2)U(X,Y),

(∇Y_X U)^H=(∇Y_U X)^H=L_U X,
L_U=(1/2)y^-1 U + A_U,
y(A_U X,Y)=-(1/2)K_y(Omega_y(X,Y),U),
(∇Y_X U)^V=∇_X U,
∇Y_U V=∇F_U V.
```

In particular `(1/2)y^-1U` is y-self-adjoint, whereas A_U is y-skew. All signs follow from the displayed bracket and curvature conventions; reversing Omega requires changing the A sign and mixed formula together.

### Exact Ricci differences from the matching flat-base model

Let `Ric^flat_y` mean the universal flat-base ambient tensor at the same fibre metric y, using the same horizontal/vertical identification. Its horizontal block is `(1/4)y`, as owned by the existing flat-base geometry certificate; its mixed block vanishes. No new value for the vertical universal term is needed here. The exact formulas are

```
RicY(H_X,H_Y)
 = Ricg(X,Y)+(1/4)y(X,Y)
   -(1/2) sum_ij y^ij K_y(Omega_y(X,e_i),Omega_y(Y,e_j)),       (BH1)

RicY(U,V)=Ric^flat_y(U,V)-trace_H(A_U A_V),                    (BH2)

RicY(H_X,U)
 =(1/2) K_y(sum_ij y^ij (∇_i Omega_y)(e_j,X),U).              (BH3)
```

For BH1 the potentially misleading **linear** curvature terms cancel between horizontal and vertical traces. Put
`S_XY=sum_ij y^ij Omega_y(e_i,X)(Y,e_j)`.
The horizontal curvature trace contributes `-(S_XY+S_YX)/4`. The vertical trace contributes the opposite. The useful trace identity is

```
trace_F[U -> Omega_y(X,y^-1 U Y)]
 = trace_H[Z -> y^-1 Omega_y(X,Z)Y]
 = -S_XY.
```

Also `div_F Omega_y(X,Y)=0`: it is a fundamental congruence Killing field of the GL-invariant fibre metric K. The quadratic horizontal and vertical traces contribute `-3/4` and `+1/4` of the Omega norm respectively, yielding `-1/2` in BH1. Thus merely retaining the horizontal trace would incorrectly leave an apparent Riemann-times-v normal response.

For BH2, fibre derivatives of `trace A_U=0` vanish, and the mixed products between the self-adjoint L0 and skew A have zero trace. Only `-trace(A_U A_V)` remains beyond the flat model. For BH3, the horizontal trace differentiates A and the vertical trace vanishes; the stated sign follows from the conventions above.

The independent reviews check these full traces. The connection is exactly the one induced by `theta_g`, and the curvature trace uses the full14-dimensional tangent space.

### Consequence for every Ricci-flat base

Set y=g+s v. Since R is g-skew,

```
Omega_(g+sv)(X,Y)=s C(R(X,Y))v.
```

BH1 and BH2 therefore start at order s² beyond the matching flat tensor. For BH3 write
`D_y R(X)=sum y^ij ∇_i R(e_j,X)`.
Each such weighted sum remains g-skew, so
`sum y^ij ∇_i Omega_y(e_j,X)=C(D_yR(X))(y-g)`.
Contracted Bianchi gives `D_gR=0` for a Ricci-flat base. Thus BH3 also starts at order s². **The full ambient Ricci and scalar source have the same value and first normal jet as the flat-base model for every Ricci-flat g**, under the stated metric and connection hypotheses. This is stronger and cheaper than separate Schwarzschild/Kerr first-jet substitutions.

The exact diagonal second normal derivative of the horizontal difference is

```
d²/ds² [RicY-Ric^flat]_(g+sv)(H_X,H_Y)|s=0
 = -sum_ij g^ij K_g(C(R(X,e_i))v,C(R(Y,e_j))v).                (BH4)
```

Its polarization gives the full bilinear normal Hessian. The normal-normal second derivative is `-2 trace(A_U^(v) A_V^(v))`, where
`g(A_U^(v)X,Y)=-K_g(C(R(X,Y))v,U)/2`.
The mixed second derivative is
`-K_g(C(sum v^ij ∇_iR(e_j,X))v,U)`, with `v^ij=g^ia v_ab g^bj`.
These latter expressions are provided for a complete check; BH4 alone can exhibit a nonzero source.

### Cheapest nonzero Schwarzschild algebraic specialization

In a g-orthonormal frame with `g=diag(-1,1,1,1)`, take the purely electric Petrov-D curvature with boost coefficients
`R(e0,ei)^0_i=R(e0,ei)^i_0=lambda_i`,
`(lambda_1,lambda_2,lambda_3)=(-2rho,rho,rho)` up to a common curvature sign. For Schwarzschild rho is its usual geometric tidal parameter; only rho≠0 matters here. Choose the explicit normal vector `v=e^0 tensor e^0` and `y=g+s v`, |s| small. Then

```
Omega_y(e0,ei)=s lambda_i(E_0i+E_i0),
K_y(Omega_y(e0,ei),Omega_y(e0,ei))
 = -2 s² lambda_i²/(1-s),

[RicY-Ric^flat](H_0,H_0)
 = s² sum_i lambda_i²/(1-s)
 = 6 rho² s²/(1-s),

d²/ds² [RicY-Ric^flat](H_0,H_0)|0=12 rho² !=0.               (BH5)
```

The matrix-entry convention is explicit: `E_0i+E_i0=2 e0⊙ei` if ⊙ includes1/2. No hidden factor2 is being absorbed. Pure conformal normal displacements y=a g instead give Omega=0 and are not a useful witness.

Since the ambient dimension is14, Ricci-to-Einstein trace reversal is invertible (`trace Einstein=-6 scalar`). A nonzero full Ricci difference therefore gives a nonzero Einstein-output difference. The held selected map and positive wedge map have their separately owned nonzero Einstein normalizations, so this establishes a quadratic normal **LC curvature-source** response for both, with their signs/conventions retained. It does not invoke the false same-cubic premise for the selected map.


## 3. Signature and direct Einstein controls

The displayed Schwarzschild expression uses the native geometric K95 port,
g=diag(-1,1,1,1), normal signature(6,4). Set rho≠0 and v00=1. Direct tracing gives

| Port | Delta Ric00 | Delta scalar | Delta Einstein00 |
|---|---|---|---|
| K95, g=(-+++) | 6 rho² s²/(1-s) | -6 rho² s²/(1-s)² | 3 rho² s²/(1-s) |
| Flipped K77, g=(+---), same v00=1 | -6 rho² s²/(1+s) | -6 rho² s²/(1+s)² | -3 rho² s²/(1+s) |

The Ricci second derivatives are respectively +12rho² and -12rho²; Einstein
second derivatives +6rho² and -6rho². This is an explicit tensor calculation
in each metric port, not a transfer of physical Krein/adjoint data. Multiplying
the base metric by -1 leaves its LC connection and algebraic R endomorphisms
unchanged; the horizontal inverse contraction changes the sign/denominator.
It does not derive source K77 from the displayed native blocks.

Conformal fibre deformations y=a g have Omega=0 and give no curvature response.
A general normal direction is essential. Schwarzschild supplies one nonzero
Ricci-flat Petrov-D witness; the all-base first-jet theorem includes Kerr,
but no explicit Kerr second-jet or bulk solution is claimed.

## 4. Verification and proof limits

The exact rational probe compares the **uncontracted horizontal and vertical
Koszul traces** with (BH1), using the ten symmetric coordinates, not sixteen
unconstrained matrix entries. It includes section, nonconformal, shear and
conformal fixtures in both signature ports; raw VV derivative checks; curvature
symmetries/Bianchi; an omitted-vertical-trace false-result control; and direct
scalar/Einstein contractions. Native lambda1/2 is degenerate in base dimension2,
so a two-dimensional native control is explicitly rejected.

For reproducibility, with B_ij=II_ij+Omega_ij/2 and L=L0+A, the raw traces are

    HorizontalHH_ij=Ric_g,ij+tr L_(B_ij)
       -sum_(k,A) B_kj^A (L_EA)_i^k
       -sum_(k,A) Omega_ki^A (L_EA)_j^k,
    VerticalHH_ij=div_F B_ij-sum_(A,k)(L_EA)_j^k B_ik^A,
    div_F B=sum_A(D_EA B)^A+sum_(A,B)F(E_A,E_B)^A B^B,
    F(U,V)=-(U y^-1 V+V y^-1 U)/2.

The difference from the Omega=A=0 traces proves the linear cancellation.
Raw VV is RicF+tr L_(F(U,V))-tr(D_U L_V)-tr(L_U L_V).
These yield (BH1–3); the mixed first-jet claim uses the written contracted
Bianchi proof, not a finite numerical sample. See the linked exact certificate
and two independent review receipts. The serialized probe passed87 grouped checks. No Lean certification or all-domain PDE
claim is made by these finite controls.

## 5. What is and is not decided

- **ESTABLISHED:** full Ricci-flat class value/first-normal blindness; a nonzero
  quadratic normal Schwarzschild LC source response in this reconstruction.
- **RULED OUT by this witness only:** extending that blindness to all normal
  orders for every Ricci-flat base in this fixed geometry. This is not a
  matrix-cell or source-GU kill.
- **NOT MODELED / UNDETERMINED here:** actual Schwarzschild/Kerr completion T,
  the full matched printed endpoint residual, horizon/end conditions, physical
  observable metric selection, and a stable full GU* theory.

SOURCE retains printed equations and source-bridge burdens. GU* wedge response
is a component comparison only; its Bianchi/Einstein behavior does not cure the
owned unchanged-Euler architecture failure. Neither track acquires a new action
or choice family. Budget remains10 choice families/4 obligations/net6/0
source-selected predictions.

The next meaningful test is the **complete matched endpoint residual** at the
same normal order for a specified admissible completion, or a class-level
compatibility condition quantifying its allowed jets. P_gT and Q(T,T) can carry
curvature dependence and cancel a source term. Even transporting unchanged
flat-branch coefficients does not establish that their full residual is
unchanged. No failure of every completion follows from this report.
