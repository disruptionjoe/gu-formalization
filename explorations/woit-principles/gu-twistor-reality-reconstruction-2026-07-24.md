---
title: "GU-TWISTOR-REALITY-RECONSTRUCTION: spacetime as a real shadow of incidence geometry"
status: active_research
doc_type: exploration
created: "2026-07-24"
grade: "standard twistor and OS theorems plus exact finite controls; curved and GU transfer remain construction-grade"
terminal_label: TWISTOR-REALITY-KERNEL-BUILT-GU-MAP-OPEN
---

# GU-TWISTOR-REALITY-RECONSTRUCTION

## Outcome

The user's correction is right:

> Starting with Minkowski spacetime and then adding twistor notation hides the
> most useful part of the construction.

The stronger mathematical order is

```text
complex twistor/incidence substrate
        |
        +-- Lorentzian Hermitian real structure --> compactified Minkowski
        |
        +-- Euclidean quaternionic real structure --> HP1 = S4
        |
        +-- complete O(1)+O(1) line family
            + Kodaira deformation --> ASD complex conformal four-geometry
        |
        +-- Schwinger data + OS reflection positivity --> physical Hilbert space
```

Minkowski spacetime is one reconstructed real locus, not the full substrate.
The complex geometry remembers incidence, chirality, conformal structure,
alternative real forms, and a route to curved anti-self-dual geometry that is
not visible if one freezes the Minkowski affine chart at the start.

The flat real-slice/incidence kernel now closes with exact controls, and the
finite OS covariance controls close on their declared spans. This investigation does
not instantiate a curved nonlinear-graviton construction or a full OS field
theory. The GU transfer does not close. The run's terminal disposition is:

```text
TWISTOR-REALITY-KERNEL-BUILT-GU-MAP-OPEN
```

This is more informative than `UNDERDEFINED`. The standard constructor is
well typed, and GU owns several endpoints that a future adapter could target.
Here `MAP-OPEN` is limited to the geometric observer/twistor adapter. What is
missing beyond it includes genuinely source-missing Schwinger/physical-
quotient, deck/operator-line, full carrier, and complete B5 data.

No claim, canon entry, verdict, scientific grade, or public posture moves.

## 1. The common complex substrate

Freeze

```text
T = C^4,
M_C = Gr(2,T),
PT = P(T) = CP^3,
F = {(W,[Z]) : Z in W}.
```

Here:

- `W in M_C` is a complex two-plane;
- its projectivization `P(W)` is a line `CP^1` in `PT`;
- `[Z] in PT` is incident with every `W` containing `Z`;
- `dim_C M_C=4`, `dim_C PT=3`, and `dim_C F=5`.

The tangent at `W` is intrinsically

```text
T_W M_C = Hom(W,T/W).
```

This is the first reason the substrate contains more than a chosen real
spacetime. It is a complex four-dimensional moduli space equipped with a
universal incidence relation. A real metric signature appears only after
additional non-holomorphic data are chosen.

### 1.1 Spacetime deformation from a twistor line

For a projective line `L=CP^1` in `CP^3`, the normal bundle is

```text
N_{L/PT} = O(1) + O(1).
```

Consequently,

```text
H^0(L,N_{L/PT}) = C^4,
H^1(L,N_{L/PT}) = 0.
```

The first equality supplies four complex infinitesimal deformations. The
second says that the flat line has no first obstruction to those deformations.
This is the local deformation-theoretic reason that a complete local moduli
family of these twistor lines is a complex four-manifold.

More is encoded. A section of

```text
O(1) + O(1)
```

is a pair of linear forms on `CP^1`. It has a zero exactly when the associated
`2 x 2` coefficient matrix has zero determinant. Therefore the determinant
null cone is recoverable from the statement that the infinitesimal normal
section vanishes at a point of the line.

Equivalently:

```text
two spacetime points are null separated
<==>
their twistor lines intersect.
```

This is not Minkowski geometry smuggled into twistor notation. Incidence of
curves is the primitive statement; the conformal causal relation is its
spacetime shadow.

## 2. Lorentzian reconstruction

Split `T=U+U`, with `U=C^2`, and freeze the Hermitian form

```text
h((u,v),(u',v')) = u^dagger v' + v^dagger u',

    [ 0  I ]
H = [      ],
    [ I  0 ]
```

of signature `(2,2)`.

The antiholomorphic involution on the Grassmannian is

```text
rho_L(W) = W^{perp_h}.
```

Its fixed locus is the set of maximal `h`-isotropic two-planes:

```text
M_L = {W in Gr(2,T) : h|_W=0}.
```

This is compactified Lorentzian Minkowski spacetime.

### 2.1 The Hermitian big cell

On the chart transverse to the second `C^2`, write

```text
       [ I  ]
B_X =  [    ],
       [ iX ]

W_X = image(B_X).
```

Then

```text
B_X^dagger H B_X = i(X-X^dagger).
```

Thus `W_X` is isotropic exactly when `X` is Hermitian. With Pauli
coordinates,

```text
    [ x0+x3    x1-i x2 ]
X = [                    ],
    [ x1+i x2  x0-x3   ]

det(X) = x0^2-x1^2-x2^2-x3^2.
```

The invariant local causal statement compares two points:

```text
W_X intersects W_Y nontrivially
<==>
det(X-Y)=0.
```

The exact test includes null, timelike, and spacelike controls. `det(X)` is
only the origin-based special case.

Every `P(W_X)` lies in

```text
PN = {[Z] in PT : h(Z,Z)=0}.
```

`PN` is a real five-dimensional CR hypersurface. It is not a holomorphic
quadric. The Hermitian chart is also only the affine big cell; the full fixed
locus includes conformal infinity.

## 3. Euclidean reconstruction

Define the antilinear quaternionic structure

```text
J(z0,z1,z2,z3)
  = (-conj(z1),conj(z0),-conj(z3),conj(z2)).
```

Exactly,

```text
J^2 = -I_T.
```

The Grassmannian involution

```text
rho_E(W)=J(W)
```

has fixed locus

```text
M_E = {W : J(W)=W} = HP^1 = S^4.
```

These are quaternionic lines in `T=C^4=H^2`.

On projective twistor space,

```text
j([Z])=[JZ]
```

squares to the identity because scalar `-1` disappears projectively. It has
no fixed points: if `JZ=lambda Z`, antilinearity would give

```text
-Z=J^2 Z=J(lambda Z)=|lambda|^2 Z,
```

which is impossible for nonzero `Z`.

There are nevertheless invariant projective lines. For every nonzero `Z`,

```text
W_Z = span_C(Z,JZ)
```

is `J`-invariant, and `P(W_Z)` is a fiber of the smooth fibration

```text
CP^1 --> CP^3 --> HP^1=S^4.
```

Distinct Euclidean fibers are disjoint. This differs sharply from the
Lorentzian fixed locus, where intersecting lines encode null separation.

## 4. Three different reality operations

The reconstruction requires three operations that must not be conflated:

| operation | acts on | defining datum | output |
|---|---|---|---|
| `rho_L` | `Gr(2,C^4)` | signature-`(2,2)` Hermitian form `h` | Lorentzian maximal-isotropic real locus |
| `rho_E` / `J` | `Gr(2,C^4)` / `C^4` | quaternionic antilinear map `J^2=-1` | Euclidean `HP^1=S^4` real locus |
| `Theta_OS` | Euclidean fields/observables | reflection, field conjugation, support split, Schwinger data | candidate positive physical form and quotient |

Holomorphic incidence alone selects none of them. In particular:

- `rho_L` is not the quaternionic `J`;
- `J` is not an OS time reflection;
- an OS reflection is not a proof of reflection positivity;
- the Lorentzian positive/null/negative `PT` strata are defined only after
  `h` is fixed.

This is the precise mathematical content behind the intuition that a
Minkowski-only presentation misses the interesting structure.

## 5. The curved/nonlinear swing

The flat `C^4/CP^3` model is only the first kernel. The deeper principle is
the Penrose nonlinear-graviton/Kodaira deformation pattern:

```text
complex threefold Z
+ four-complex-dimensional family {L_x}
+ L_x=CP^1 and N_{L_x/Z}=O(1)+O(1)
------------------------------------------------
complex conformal four-manifold M_C of curves
```

The infinitesimal soldering is the Kodaira-Spencer map

```text
kappa_x:
T_x M_C -> H^0(L_x,N_{L_x/Z}).
```

When it is an isomorphism, the zero locus of a normal section defines the
conformal null cone. This is best described as a **conformal soldering**:
the tangent of the reconstructed spacetime is identified with deformations
of its twistor line.

It does not yet give:

- a metric scale within the conformal class;
- a Cartan tetrad with the GU target type;
- a full non-self-dual gravitational theory;
- a physical state space.

For an oriented Riemannian four-manifold `(X,[g])`, the ordinary twistor
bundle is a `CP^1` bundle, equivalently `P(S_g^+)` after a spin choice. It has
the Atiyah-Hitchin-Singer almost-complex structure. Its integrability
condition is vanishing of the appropriate Weyl half, with the sign depending
on the orientation convention. This names the AHS structure specifically;
the distinct Eells-Salamon almost-complex structure is not being used.

This AHS input is Riemannian. It cannot directly consume GU's admitted
Lorentzian observer metric. Before invoking AHS, the adapter must either
construct and type a Euclidean metric/real form on the observer base, or
choose a separately typed Lorentzian twistor construction. Therefore a
generic GU observer section does not automatically produce a holomorphic
twistor threefold. There are two honest routes:

1. **Observer-first:** first freeze either (a) a Euclidean metric/real-form
   constructor and then build its AHS `CP^1` almost-twistor bundle, or (b) a
   Lorentzian spin/CR twistor construction with its own integrability
   statement. In branch (a), prove the required Weyl-half condition or work
   in an explicitly almost-complex extension.
2. **Substrate-first:** postulate/build `Z` and its line family first,
   reconstruct `(X,[g])`, choose a scale, and only then map the resulting
   metric into `Y=Met(X)`.

The second route is the genuine substrate inversion already demanded by the
repo's Cartan/twistor guardrail. It is also the route that most directly
implements the user's point.

## 6. OS positivity is a dynamical reconstruction layer

Let a scalar Euclidean covariance have a positive spectral representation

```text
C(tau)=integral_0^infinity exp(-E |tau|) dmu(E),
dmu(E) >= 0.
```

For positive times `tau_i`, reflection gives

```text
K_ij=C(tau_i+tau_j).
```

Then

```text
c^dagger K c
 = integral_0^infinity
   |sum_i c_i exp(-E tau_i)|^2 dmu(E)
 >= 0.
```

The new NumPy kernel tests:

- one deterministic positive spectral measure;
- sixteen seeded random positive measures;
- rank bounded by the number of spectral atoms, including quotient ranks one
  and three under the same positive-time geometry;
- a signed spectral atom with a robust negative eigenvalue;
- a `10^-15` rescaling control proving that PSD/rank classification is
  matrix-relative rather than set by an absolute tolerance floor;
- the same reflection matrix in the positive and negative cases.

The last control is decisive. Reflection geometry stays fixed while
positivity changes with the Schwinger data.

The finite test is not the OS theorem. It proves positivity on selected
finite spans for these covariance kernels. Full Wightman reconstruction needs
the other OS axioms and the repaired growth/regularity condition; an
interacting theory needs its own Schwinger-functional argument.

Woit's July 2026 notes make this boundary explicit: the `PT+ / PN / PT-`
boundary-value picture is a proposal, while finding the appropriate twistor
`Theta` is still connected to the unfinished twistor-transform
construction.

## 7. GU interface ledger

### 7.1 What GU already owns

The repository has genuine target objects:

```text
s:X^4 -> Y^14=Met(X),        pi o s = id,
H_{s,x}=ds(T_x X),           dim_R H_{s,x}=4,
N_{s,x}=T_{s(x)}Y/H_{s,x} ~= Sym^2(T_x^*X),  rank_R=10.
```

Under the admitted Lorentzian and horizontal-normalized observer convention,
it also distinguishes:

```text
base/horizontal metric g_s,          signature (3,1),
vertical DeWitt metric,              signature (6,4),
full gimmel metric on Y^14,          signature (9,5).
```

A general distorted section has tangent
`T_a=E_a^H+theta_a^V`; its vertical slope contributes to the full pullback
`s^*gimmel`. Thus `s^*gimmel=g_s` is not being asserted outside the
horizontal-normalized convention.

The bounded Lorentzian carrier audit supplies:

```text
C_+, C_-:             192 complex dimensions each,
K|_{C_+}=K|_{C_-}=0,
physical conjugation: C_+ <-> C_-,
C_cl=C_+ + C_-:       384 complex dimensions,
K signature on C_cl:  (192,192).
```

These are not yet the true function-space carrier on `Y^14`, but they are
strong enough to reject several silent identifications.

### 7.2 Exact adapter ledger

| interface | available endpoint | missing map or theorem | disposition |
|---|---|---|---|
| generic observer twistor geometry | admitted Lorentzian observer plane `H_{s,x}` and metric | either a Euclidean metric/real-form constructor before the Riemannian AHS construction, or a separately typed Lorentzian spin/CR twistor construction; both also need orientation/spin data and route-specific integrability | `UNDERDEFINED` until the route and real form are frozen; then potentially a `CONDITIONAL CONSTRUCTOR` |
| observer to one fixed `Gr(2,C^4)` | conformally flat/developable observer geometry | conformal development plus a conformal-spin trivialization/marking giving one fixed `V_tw=C^4` and `Phi_obs(s,x)=S_x` | conditional branch `MAP-OPEN`; not natural for a generic observer |
| tangent comparison | `H_{s,x} tensor C` and `Hom(S_x,Q_x)` both have complex dimension four | an equivariant `tau_x:H_{s,x} tensor C -> Hom(S_x,Q_x)` after freezing the common `Spin(4,C) ~= SL(2,C) x SL(2,C)` action and its selected Lorentzian or Euclidean real form | `MAP-OPEN`; dimension is not a construction, and no universal `tau_x` is typed before that freeze |
| conformal metric | twistor determinant conformal form and complexified GU base metric `g_s^C` | a determinant-line scale, proof `[det o tau_x]=[g_s^C]`, and a real involution whose fixed locus recovers `[g_s]` | `MAP-OPEN` |
| full gimmel | 4d determinant form versus 14d `(9,5)` base-plus-DeWitt metric | none possible as an equality; only a base embedding plus a separate vertical construction can be typed | direct equality `INCOMPATIBLE` |
| bounded physical-carrier comparison | a named candidate `H^1(PT_U,O(-3))` on an open twistor domain `PT_U`, degree `1` and weight `-3`, versus audited `C_cl` of dimension `384_C` | freeze the spin-`1/2` convention and contour transform `P_{-3}:H^1(PT_U,O(-3))->ker D_{1/2}`, then construct a map from its image into a specified summand of this bounded closure | `MAP-OPEN`; generic “twistor cohomology” is not enough |
| true physical cohomology | desired function-space carrier/quotient and projector `Pi_RS^phys` | differential, domain, construction of `Pi_RS^phys`, quotient, induced form, and observable algebra | `UNDERDEFINED` |
| single Hodge half | holomorphic chirality versus one `192_C` GU half | ordinary physical conjugation already exchanges the halves and each is `K`-null | shortcut `INCOMPATIBLE` |
| geometric real structures | twistor maps `rho_L`, `rho_E`, and `J_tw:C^4->C^4`, versus bounded physical `J_phys:C_cl->C_cl` | a typed comparison/compatibility map between their distinct carriers | `MAP-OPEN` |
| OS reality square | desired `(rho,J_phys,Theta_OS)` square | `Theta_OS` and its lift do not yet exist on the GU field algebra | `UNDERDEFINED` |
| direct OS/GU quotient equality | standard positive Hilbert quotient versus GU Krein keep-and-grade target | none: these are different constructions | silent equality `INCOMPATIBLE` |
| OS-to-GU bridge | the two distinct quotient targets | GU reflection lift, Schwinger functional, positivity/indefinite theorem, null quotient, and comparison map/theorem | `UNDERDEFINED` |
| deck/orientation | proposed external `sigma` | operator/domain family, deck lift, determinant/Pfaffian/orientation line, and classifying map | `UNDERDEFINED` |
| gauge/internal data | twistor `S(U(1)xU(3))` host; GU real `Spin(6,4)`, complex `Spin(10,C)`, compact comparison real form `Spin(10)`, and super-IG | choose exactly one adapter type—bundle embedding, structure-group reduction, or coupling—and construct it | direct equality `INCOMPATIBLE`; adapter `UNDERDEFINED` before that choice |
| internal representation | complex chiral `Spin(6,4)` module `S^+_{6,4} ~= C^16` | restriction to the maximal-compact/Pati-Salam subgroup gives `16=(4,2,1)+(bar 4,1,2)` at representation level | standard representation-level `CONSTRUCTOR`; not yet a gauge-bundle or dynamics result |
| super-IG bracket | `ig=Omega^0(ad P) semidirect Omega^1(ad P)` and desired `beta:Sym^2 Q->Omega^1(ad P)` | canonical odd module `Q`, representation `rho`, bracket `beta`, closure/Jacobi data, and BV/action identities | `UNDERDEFINED` |
| conditional normal-to-adjoint solder | repository candidate `j_s:N_s->ad(P_s)` | its declared bundle, rank, equivariance, and nondegeneracy hypotheses | conditional `CONSTRUCTOR`; not an equation-of-motion result |
| incidence-to-connection solder | Kodaira-Spencer conformal solder and dynamic GU connection `pi` | map from incidence deformation data to `pi`, plus equivariance and domain control | `MAP-OPEN` |
| square-action forcing of solder | existing `||theta||^2=||II||^2` action and proposed requirement that `pi` land in a spin-lift image | H27's variation shows that this action does not supply the needed curvature-linear Palatini mechanism | forcing claim `INCOMPATIBLE` for this action; H27 remains `NOT FORCED` |
| action | partial classical GU action candidates | Euclidean functional/Schwinger hierarchy on the actual carrier, counterterms, and physical observables | `UNDERDEFINED` |
| B5 seed placement | individual native symbol slots in `Hom_H(V tensor W_i,W_j)` | after every `m_ij` and a tangent/cotangent adapter are complete, use the named transform `P_{-3}:H^1(PT_U,O(-3))->ker D_{1/2}` to type the zero-rest-mass operator and place `sigma(D_{1/2})` in one cell | `MAP-OPEN`; a GU “twistor symbol” is not automatically this Penrose-derived differential |
| complete B5 transform | unresolved full symbol matrix and physical complex | complete every `m_ij`, then prove full-matrix, `J/K`, domain, and cohomology compatibility | `UNDERDEFINED` and enumeration-gated |

The current program-native super-IG sketch is not a hidden closure of this
ledger. It still needs a canonical odd module, an equivariant odd bracket,
and BV/action identities.

### 7.3 GU evidence map

The ledger is grounded in the following current repository surfaces:

- observer section, four-plus-ten split, base/vertical metrics:
  `explorations/geometry-curvature-emergence/pc2-met-x4-bundle-formalization-stub-2026-06-22.md:121-209,412-438`
  and
  `explorations/geometry-curvature-emergence/pc2-gauss-y14-curvature-2026-06-23.md:83-98`;
- distorted-section vertical slope and its effect on the pullback:
  `explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md:223-230`;
- conditional normal-to-adjoint solder:
  `explorations/geometry-curvature-emergence/ic1-soldering-map-ns-adps-2026-06-23.md:780-807,1051-1077`;
- physical-signature and `192/384` transfer correction:
  `papers/candidates/located-not-forced/review/V15-1-physical-signature-transfer-audit-2026-07-23.md:18-39,57-141`
  and
  `papers/candidates/located-not-forced/review/V15-4-carrier-faithfulness-packet-2026-07-23.md:35-59`;
- deck/operator-line source gap:
  `explorations/operator-to-anomaly-closure-campaign-2026-07-22.md:136-145,188-205`
  and
  `explorations/sigma-external-z2-claim-dependency-packet-2026-07-23.md:17-90,147-178,207-240`;
- partial super-IG construction:
  `explorations/misc/super-ig-algebra-construction-2026-06-23.md:29-41,85-165,191-238`;
- partial classical source action:
  `explorations/W125-source-action-first-build-2026-07-13.md:46-75,139-155`;
- physical quotient obligation:
  `explorations/research-cycles/hourly-cycle2-rs-physical-quotient-brst-complex-gate-2026-06-24.md:24-111`;
- the unresolved `Pi_RS^phys`/generation versus representation-level split:
  `explorations/W221-falsify-generation-count-structure-2026-07-14.md:64-107`;
- paper-facing internal representation status:
  `docs/paper-formalization-candidates.md:420-436`;
- standard OS quotient versus GU-native reconstruction fork:
  `explorations/woit-principles/woit-os-physical-real-form-gate-2026-07-24.md:204-274`;
- Palatini/GU soldering fork:
  `explorations/wave10/H27-soldering-palatini-2026-07-11.md:48-67,76-165,197-237`;
- B5 symbol cells and unresolved middle:
  `explorations/b5-independent-symbol-class-enumeration-contract-2026-07-23.md:48-86`
  and
  `explorations/b5-middle-source-freeze-2026-07-21.md:39-103`.

## 8. Strongest partial GU constructor

The biggest justified next object is not a global identification

```text
GU = twistor theory.
```

It is a bounded domain freeze followed by an adapter packet.

### `GU-TWISTOR-OBSERVER-DOMAIN-FREEZE`

Before constructing maps, freeze:

1. the flat/developable or curved ASD/almost-complex route;
2. the Lorentzian Hermitian, Euclidean quaternionic, or explicitly related
   pair of real forms;
3. the spin structure and any conformal development/trivialization/marking;
4. the admissible observer objects and equivalences under which naturality is
   required.

This is the bounded executable next target. It does not presuppose categories,
morphisms, or functoriality that have not been defined.

The object obtained after this freeze, if the required maps exist, is called
the **`GU-OBSERVER-TWISTOR-ADAPTER`**.

#### Flat/conformally-flat leg

This leg is not natural for an arbitrary observer section. First require a
locally conformally flat/developable observer conformal structure. A global
map additionally requires compatible development/holonomy and a
conformal-spin trivialization or marking that identifies the flat twistor
tractor with one fixed `V_tw=C^4`. Only on that declared branch construct

```text
Phi_obs:(s,x) -> S_x in Gr(2,V_tw),

tau_x:
H_{s,x} tensor C
  -> Hom(S_x,V_tw/S_x),

lambda_x:
det(V_tw/S_x) tensor det(S_x)^*
  -> C
```

and prove

```text
[lambda_x o det o tau_x] = [g_{s,x}^C],

rho^* fixed real locus -> [g_{s,x}].
```

The equivariance datum is part of the freeze: both sides must carry the same
complex conformal-spin action
`Spin(4,C) ~= SL(2,C) x SL(2,C)`, together with the chosen Lorentzian or
Euclidean real form. Until those actions are fixed, there is no universal
`tau_x`.

This would identify the observer's conformal base geometry with the
incidence-derived conformal geometry. It would not identify the full gimmel
metric. For a generic observer the natural object is instead the fiberwise
twistor bundle from Section 5, not a map into one global fixed
`Gr(2,C^4)`.

#### Curved/substrate-first leg

Construct

```text
(Z,{L_x},rho:Z->Z)
```

with:

```text
L_x=CP^1,
N_{L_x/Z}=O(1)+O(1),
rho antiholomorphic and rho(L_x)=L_{bar x},
kappa_x:T_x M_C -> H^0(L_x,N_{L_x/Z}) an isomorphism
  on the complex moduli space M_C,
```

so that real moduli have invariant lines. Equivalently, after a real slice is
chosen, write
`kappa_x:T_x X tensor_R C -> H^0(L_x,N_{L_x/Z})`. Then reconstruct and mark:

```text
X_rho = real slice of M_C,
iota:X -> X_rho a declared diffeomorphism/marking,
iota^*[g_rho] -> choose scale g -> section s_g:X->Met(X).
```

The adapter succeeds only if the reconstructed conformal class agrees with
the GU observer class and the construction is natural over admissible
observer sections.

#### Physicalization leg

Only after either geometric leg closes, require:

```text
twistor field/cohomology
  -> bounded C_cl comparison,

eventual GU physical cohomology
  through an explicitly constructed Pi_RS^phys
  (separate underdefined target),

rho and J_tw:C^4->C^4
  <-> J_phys:C_cl->C_cl geometric compatibility,

(rho,J_phys,Theta_OS) reality square
  (only after Theta_OS exists),

P_{-3}:H^1(PT_U,O(-3)) -> ker D_{1/2}
  with degree 1, weight -3, and a convention-fixed spin-1/2 transform,
sigma(D_{1/2}) -> one explicit B5 Hom_H cell
     after all required m_ij and a tangent/cotangent adapter are complete,

Schwinger data
  -> positive Hilbert quotient
     or a proved GU-native indefinite reconstruction theorem.
```

This packet gives a real target to the twistor branch without pretending that
incidence alone supplies the action or the physical state space.

## 9. What the swing proves, kills, and opens

### Proves at standard/exact-control grade

- Minkowski and Euclidean compactified four-spaces arise as inequivalent real
  loci of one complex Grassmannian/incidence substrate.
- The Minkowski determinant and null relation arise from maximal isotropy and
  intersection of twistor lines.
- The Euclidean quaternionic action has no fixed projective points but has
  invariant `CP^1` fibers over `S^4`.
- The line normal bundle explains four complex spacetime deformations and
  reconstructs the conformal null cone.
- Positive spectral measures give finite OS-positive Gram matrices; signed
  spectral data can fail while reflection geometry remains unchanged.

### Kills only the shortcuts

- “Minkowski spacetime is the twistor substrate.”
- “One real structure is just another signature convention.”
- “Quaternionic `J`, Lorentzian reality, and OS `Theta` are the same map.”
- “A reflection automatically proves positivity.”
- “The twistor determinant metric is GU's full gimmel metric.”
- “Holomorphic chirality automatically selects one physical `192` half.”
- “The twistor stabilizer is already GU's internal gauge group.”
- “Incidence supplies GU's dynamic soldering connection for free.”

### Opens a sharper route

The new high-information bridge is the conformal/Kodaira-Spencer solder:

```text
observer tangent
<-> deformation of observer twistor line
<-> conformal null structure.
```

It is a more natural twistor-to-GU interface than trying to identify a
standard gauge connection with GU's `pi` directly. It also has a clean
failure mode: no natural line family, failed normal-bundle type, failed
reality locus, failed conformal match, or non-integrable observer twistor
bundle outside the declared almost-complex branch.

## 10. Run-local dependency proposal

This is an information/dependency proposal produced by this run, not a
durable queue movement. Current repository authority remains:

- `B5-INDEPENDENT-RECONSTRUCTION` is the global truth-status research lead;
- the existing OS-Theta packet remains the recorded Woit-derived follow-up;
- the B5 twistor transform cannot execute before the complete `m_ij`
  enumeration and a typed tangent/cotangent adapter;
- H27 is closed at `NOT FORCED`.

Because the OS target is source-blocked while domain selection is executable,
this investigation proposes the following local ordering. It does not edit
`NEXT-STEPS.md`, move a lane, or supersede stewardship.

1. **`GU-TWISTOR-OBSERVER-DOMAIN-FREEZE`** — choose the flat/developable or
   curved ASD/almost-complex route, real form, spin/marking data, and
   naturality domain.
2. **`GU-OBSERVER-TWISTOR-ADAPTER`** — only after that freeze, build or
   obstruct the observer-line, Kodaira-Spencer, reality, and conformal-match
   maps above.
3. **`GU-OS-THETA-ACTION`** — once a GU Euclidean functional/Schwinger packet
   exists, compute the reflection form and its null quotient on the actual
   carrier.
4. **`GU-TWISTOR-B5-FIELD-TRANSFORM`** — freeze
   `P_{-3}:H^1(PT_U,O(-3))->ker D_{1/2}`, then map the resulting
   `sigma(D_{1/2})` into a B5 symbol cell only after every `m_ij` and the
   tangent/cotangent adapter are complete; test `J/K/domain/cohomology`
   compatibility.
5. **H27 wake gate** — do not rerun the closed square-action test. Wake it only
   for a genuinely new curvature-linear source action or a constructed
   Kodaira-Spencer-to-`pi` adapter whose compatibility with the GU variation
   can actually be tested.

## 11. Sources and provenance

Primary and standard mathematical sources:

- Roger Penrose,
  [Twistor Algebra](https://doi.org/10.1063/1.1705200) (1967).
- Roger Penrose,
  [Nonlinear Gravitons and Curved Twistor Theory](https://inspirehep.net/literature/114824)
  (1976).
- M. F. Atiyah, N. J. Hitchin, and I. M. Singer,
  [Self-Duality in Four-Dimensional Riemannian Geometry](https://doi.org/10.1098/rspa.1978.0143)
  (1978).
- J. Bures and V. Soucek,
  [The Penrose Transform for Dirac Equation](https://dml.cz/handle/10338.dmlcz/701517)
  (1993).
- Konrad Osterwalder and Robert Schrader,
  [Axioms for Euclidean Green's Functions II](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-42/issue-3/Axioms-for-Euclidean-Greens-functions-II-with-an-Appendix-by/cmp/1103899050.pdf)
  (1975 repaired reconstruction theorem).
- Peter Woit,
  [Euclidean Twistor Unification](https://arxiv.org/abs/2104.05099)
  and
  [Spacetime is Right-handed](https://arxiv.org/abs/2311.00608).
- Peter Woit,
  [Notes on Wick Rotation and Chiral Field Theories](https://www.math.columbia.edu/~woit/twistorunification/chiralwick-sketch.pdf)
  (preliminary notes, July 2026).

The Theories of Everything transcripts remain discovery aids only. The
load-bearing statements here come from the primary/standard sources, exact
derivations, executable controls, and current GU repository authority.

## 12. Reproduction

```bash
python3 tests/woit-principles/test_twistor_real_slice_reconstruction.py
python3 tests/woit-principles/test_os_reconstruction_kernel.py
python3 tests/woit-principles/test_twistor_grassmannian_kernel.py
python3 tests/woit-principles/test_os_real_form_kernel.py
python3 tests/woit-principles/test_soldering_palatini_kernel.py
python3 tests/wave10/H27_soldering_palatini.py
```
