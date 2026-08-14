---
artifact_type: exact_k77_adapted_connection_total_yang_mills_current_and_moving_reduction_variation_result
created: 2026-08-14
status: K77_ADAPTED_CURRENT_DECOMPOSED_EXACTLY__LOCAL_TWISTOR_PROLONGATION_ADAPTER_OPEN__II_ZERO_EQUIVALENCE_FAILS_BOTH_DIRECTIONS__COUPLED_MOVING_REDUCTION_DETOUR_IS_THE_TYPED_SUCCESSOR
source_return: STANDARD_SUBMANIFOLD_AND_GAUSS_MAP_GEOMETRY_DISTINGUISH_WILLMORE_REDUCTION_ENERGY_FROM_CONNECTION_YANG_MILLS__GU_ACTION_CONNECTION_AND_NORMALIZED_ADAPTER_REMAIN_UNOWNED
ledger_rows: [LT-SM8]
ledger_hypothesis: HYP-TW-COHERENCE-01
registry: lab/process/selected-k77-total-twisted-yang-mills-current-gate.json
probe: tests/channel-swings/selected_k77_total_twisted_yang_mills_current_gate_probe.py
canon_verdict_change: none
---

# Selected K77 total twisted Yang--Mills current gate

## Result first

The proposed equivalence

```text
total twisted Yang--Mills  <=>  II_s=0
```

is false in both directions, already at exact local differential-geometric
grade.

The mixed coefficient of the universal K77-typed adapted tangent/normal
connection algebra is the raw second fundamental form. But the Yang--Mills
equation is imposed on the
**curvature** of that connection. Its tangent, mixed and normal blocks are the
Gauss, Codazzi and Ricci curvatures, and its divergence contains all three.
Consequently:

1. `II=0` does not force the diagonal tangent or normal connections to be
   Yang--Mills.
2. A nonzero symmetric `II` can occur inside a flat total adapted connection.
   The exact control is the local connection of a developable/cylindrical
   immersion: its moving frame has nonzero extrinsic curvature while the
   pulled-back flat ambient connection has zero curvature and therefore zero
   Yang--Mills current.

This does not kill the twistor/coherence route. It identifies a Layer-0
collision in the previous formulation. There are two variational objects:

```text
tangent-plane reduction/Gauss field R:
    D_A R measures the mixed coefficient and |D_A R|^2 measures bending;

twistor/normal connection A:
    F_A supplies the detour complex and D_A^*F_A is its obstruction.
```

Their equations are not identical. Varying the reduction energy gives a
harmonic-reduction equation. Varying that same energy with respect to the
connection creates a reduction current `[R,D_A R]`. For the coupled functional

```text
S[A,R] = (1/4)||F_A||^2 + (lambda/2)||D_A R||^2,
```

the connection equation is, up to the declared codifferential sign,

```text
D_A^*F_A = lambda [R,D_A R].
```

Thus an on-shell coupled connection is not generally source-free
Yang--Mills. The ordinary Bach/Yang--Mills detour composition does not close
unless the reduction current vanishes. The correct successor is therefore a
**coupled moving-reduction detour/BV complex**, not a pure connection detour
with `II` renamed as its Yang--Mills current.

The strongest hypothesis becomes:

> GU may couple a moving tangent/normal or complex reduction field to the
> local-twistor connection. The reduction-field energy controls geometric
> bending; the connection curvature controls the detour complex. If the
> action-owned coupled BV differential absorbs the reduction current, admits
> the actual endpoint, and has a positive physical cohomology, that coupled
> cohomology is the remaining plausible geometric home for superposition.

This is a sharper construction target. It is not a quantum-mechanical result
and it yields no decoherence rate.

## 1. Exact structure fingerprint

The finite certificate uses the source-aligned K77 sign matrix explicitly,
without relying on ordered signature-pair notation:

```text
observed tangent signs: (+,-,-,-),
normal signs:           (+,+,+,+,+,+,-,-,-,-),
total signs:            seven plus and seven minus.
```

Along a section, write the adapted metric connection on
`TX direct-sum N_s` as

```text
A_mu = [ a_mu       -b_mu^dagger ]
       [ b_mu        c_mu         ],
```

where

```text
a_mu in so(TX),
c_mu in so(N_s),
b_mu in Hom(TX,N_s),
b_mu^dagger = g_T^{-1} b_mu^T g_N.
```

For the ambient Levi--Civita adapted connection,

```text
(b_mu)^i_nu = B^i_{mu nu}=II^i_{mu nu}
```

and torsion-freeness makes `B^i_{mu nu}` symmetric in `mu,nu`. This is the
repository's canonical-gauge **raw** `II` identification. It is not yet the
horizontal-reference-normalized `II_s^H` used by the candidate section
functional.

The exact probe works at the actual `4+10` dimensions and verifies

```text
A_mu^T G + G A_mu = 0
```

for every coefficient, curvature and current in the generic control.

## 2. Gauss--Codazzi--Ricci curvature is the first separation

For constant local coefficients, enough to certify the algebraic terms, write

```text
F_{mu nu} = [ P_{mu nu}   -Q_{mu nu}^dagger ]
             [ Q_{mu nu}    R_{mu nu}        ].
```

The exact block expansion is

```text
P_{mu nu}
 = F^a_{mu nu}
   - b_mu^dagger b_nu + b_nu^dagger b_mu,

Q_{mu nu}
 = D_mu b_nu - D_nu b_mu,

R_{mu nu}
 = F^c_{mu nu}
   - b_mu b_nu^dagger + b_nu b_mu^dagger.
```

With derivatives restored these are precisely the Gauss, Codazzi and Ricci
blocks. Applying the spin representation preserves the commutator identities,
but does not by itself identify this adapted spin connection with the
Schouten-prolonged local-twistor connection. That adapter remains required.

The key typing fact is already visible:

```text
b = II                    connection coefficient,
Q = D II                  mixed curvature,
D_A^*F_A                  Yang--Mills current.
```

They differ by two differential/algebraic layers. No pointwise substitution
can identify them.

## 3. Complete total current

Let

```text
J_nu = sum_mu epsilon_mu [A_mu,F_{mu nu}]
```

in a local constant frame; ordinary derivatives and connection terms combine
covariantly in the global formula. Then

```text
(J_T)_nu
 = D_a^mu P_{mu nu}
   - b^{mu dagger} Q_{mu nu}
   + Q_{mu nu}^dagger b^mu,

(J_N)_nu
 = D_c^mu R_{mu nu}
   - b^mu Q_{mu nu}^dagger
   + Q_{mu nu} b^{mu dagger},

(J_M)_nu
 = D_{c,a}^mu Q_{mu nu}
   + b^mu P_{mu nu}
   - R_{mu nu} b^mu.
```

The three equations

```text
J_T=0,  J_N=0,  J_M=0
```

are the total Yang--Mills condition. The mixed equation is a covariant
Codazzi-divergence/Simons-type equation with tangent and normal curvature
acting on `II`. It is not `II=0`.

This block result is complementary to the repository's earlier ambient-to-
section formula

```text
s^*(D_A^*F_A)_nu = (D_a^*F_a)_nu + K_nu(A,s),
```

where `K` contains normal derivatives and shape contractions. The present
calculation decomposes the pulled-back adapted connection internally; the
older formula compares fourteen-dimensional divergence with four-dimensional
divergence and retains normal-direction jets. Neither replaces the other.

## 4. Two exact counterexamples

### 4.1 Nonzero `II`, zero total current

Take a single positive tangent and normal axis and set

```text
B^0_{00}=1,
all other B^i_{mu nu}=0.
```

This is symmetric and has positive nonzero quadratic density in the explicit
control. Only `A_0` is nonzero, so all `A_mu` commute:

```text
F_A=0,
D_A^*F_A=0,
II != 0.
```

Geometrically this is the local adapted-frame pattern of a developable or
cylindrical immersion in a flat ambient space. A pulled-back flat ambient
connection stays flat even though its moving tangent plane has nonzero second
fundamental form.

Therefore total Yang--Mills does not imply a totally geodesic section.

### 4.2 Zero `II`, nonzero total current

Set `b_mu=0` and choose two noncommuting tangent connection coefficients. The
exact control returns

```text
II=0,
J_T != 0.
```

A second control sets both `II=0` and the base connection to zero while using
a non-Yang--Mills normal connection:

```text
J_T=0,
J_N != 0.
```

Therefore total geodesicity does not imply total Yang--Mills. At best,
`II=0` removes the mixed contractions and reduces the remaining obligation to
the separate tangent and normal Yang--Mills equations.

## 5. Horizontal normalization is a connection transgression

The repo's operative candidate field is

```text
II_s^H = II_s^raw - II_s^ref.
```

The Yang--Mills current cannot accept that replacement at the coefficient
level while keeping the old curvature. If a purely mixed reference one-form
`K_ref` is subtracted from the connection,

```text
A^H = A-K_ref,
```

then exactly

```text
F(A^H) = F(A) - D_A K_ref + K_ref wedge K_ref.
```

The probe starts with the flat developable control and supplies a second,
noncommuting mixed reference. The normalized connection acquires nonzero
curvature and nonzero Yang--Mills current. Thus

```text
b -> b-b_ref
```

is not an innocent relabeling; it constructs a different connection and a
different detour gate.

Before `II_s^H` can enter the coherence complex, the program must build an
action-owned `A^H`, prove its mixed block is exactly `II_s^H`, and show that
the physical operator and BV differential use that same connection.

## 6. The two Gauss objects

The historical geometry clarifies the collision.

### Tangent-plane Gauss map

For an immersion into flat Euclidean space, the tangent-plane Gauss map

```text
gamma_s : X -> Gr_4(R^14)
```

has differential identified with `II`. Its Dirichlet energy is proportional
to

```text
integral_X |II|^2.
```

Ruh and Vilms identify its tension field with the covariant derivative of the
mean-curvature vector. In their Riemannian Euclidean setting the Gauss map is
harmonic exactly when mean curvature is parallel. This is not the condition
`II=0`, and it is not the Yang--Mills equation for the pulled-back ambient
connection.

The theorem is used here only as a standard positive-control classification.
GU's observed base and K77 carrier are indefinite, so the corresponding
equation is a pseudo-harmonic/wave-map equation and needs its own domain.

### Principal-connection Gauss section

There is another construction in which a principal connection determines a
horizontal distribution in `TP`, hence a Gauss section of a Grassmann bundle
over `P`. In the Riemannian compact/bi-invariant setting, Wood's theorem and
Manabe's extensions relate harmonicity of that connection Gauss section to
the Yang--Mills equation.

That is a different Gauss object. Its differential measures the curvature of
the horizontal distribution; it is not the tangent-plane Gauss map of the
spacetime section. The theorem's Riemannian hypotheses also do not transfer
automatically to noncompact K77.

The two constructions can coexist and may be related by an associated-bundle
functor, but no such GU adapter currently exists.

## 7. Moving reduction field gives the correct coupled equations

Represent the tangent/normal reduction by the involution

```text
R = diag(+I_4,-I_10),
R^2=I.
```

For the adapted connection,

```text
D_A R = [A,R]
      = [ 0             2 b^dagger ]
        [ 2 b           0          ].
```

Hence `D_A R=0 iff b=0` in this raw adapter. This is the exact reduction-field
version of the earlier kernel-zero commutator result. It does not identify `R`
with spinor `J10`, local-twistor multiplication by `i`, or the rolled-carrier
`Jhat`; those require their existing adapters.

Define the reduction energy

```text
E_R[A,R] = (1/2) integral <D_A R,D_A R>.
```

The exact first variations are:

```text
delta_R R=[xi,R]:
    [R,D_A^*D_A R]=0,

delta_A A=alpha:
    delta_A E_R = integral <[R,D_A R],alpha>.
```

Thus the moving reduction carries the connection current

```text
j_R=[R,D_A R].
```

For the coupled functional

```text
S[A,R]=(1/4)||F_A||^2+(lambda/2)||D_A R||^2,
```

the exact finite variation gives, in the probe's codifferential convention,

```text
J_A = lambda j_R.
```

The sign flips if `D_A^*` is defined with the opposite overall sign; the
content does not: curvature divergence is balanced by reduction current.

This is a gauged sigma-model/Yang--Mills--Higgs-shaped system. It gives the
Willmore and twistor pieces distinct jobs:

```text
|D_A R|^2: bending/moving-reduction dynamics,
|F_A|^2: connection/detour dynamics,
j_R: coupling between them.
```

## 8. Consequence for the detour complex

The ordinary Yang--Mills detour identity is

```text
M_A d_A = epsilon(D_A^*F_A).
```

On a coupled solution with nonzero reduction current,

```text
M_A d_A = lambda epsilon(j_R) != 0
```

in general. Therefore the pure connection sequence is not a complex merely
because the **coupled** Euler--Lagrange equations hold.

There are two honest horns:

1. **Source-free/parallel horn.** If `D_A R=0`, then `j_R=0`. The coupled
   connection equation reduces to pure Yang--Mills and the ordinary detour may
   close. This is sufficient but need not be necessary for a larger complex.
2. **Coupled-complex horn.** Enlarge the deformation/BV complex by the moving
   reduction field. Its linearized equation contributes exactly the missing
   current map, potentially converting the failed composition into the next
   component of a mapping-cone or coupled detour complex.

The second horn is now the stronger steelman because the repository already
proved that fixed `J10` fails the active gauge quotient while moving `J10`
transforms covariantly. But the complex must be constructed; the words
“Yang--Mills--Higgs” or “mapping cone” do not supply it.

## 9. Revised coherence hypothesis

The sequence of hypotheses is now:

```text
H0, rejected:
    pointwise complex structure alone is superposition;

H1, rejected as an equivalence:
    II=0 iff total Yang--Mills iff coherence;

H2, current steelman:
    a moving reduction field R/J and a local-twistor connection A form a
    coupled gauge system; superposition, if geometrically represented at all,
    lives in positive physical cohomology of the coupled BV/detour complex;

H3, still speculative:
    an observable loss of that cohomology or its positive pairing produces a
    measurable decoherence law.
```

`II=0` remains a useful special locus. After an action-owned normalized
adapter, it can make the reduction current vanish. It is neither the general
Yang--Mills locus nor a derived physical coherence condition.

## 10. Inefficiency audit

This gate removes four pieces of overhead:

1. **Redundant encoding:** `II`, `D II`, and `D^*F` are no longer treated as
   three names for one obstruction.
2. **Tool-hypothesis mismatch:** Willmore/Gauss-map variation and connection
   Yang--Mills variation are assigned to their actual fields.
3. **Projection-loss accounting:** replacing raw `II` by normalized `II^H`
   now carries the full connection transgression instead of restoring lost
   curvature terms by hand.
4. **Uniqueness-failure cost:** the pure-detour and moving-reduction routes are
   not forced to share one operator before a coupled complex is constructed.

It exposes one larger cost: an ordinary detour complex is insufficient on a
connection sourced by the moving reduction. The BV extension is no longer
optional interpretive machinery; it is the exact algebraic gate.

## 11. Seven-axis disposition

| layer | result |
|---|---|
| Layer 0 | raw `II`, normalized `II^H`, Codazzi curvature, total YM current, tangent Gauss map, connection Gauss section, `R`, `J10`, `Jhat` and local-twistor `i` remain separately typed |
| L1 algebra | exact K77 `4+10` block curvature/current formulas; exact reduction and coupled first variations |
| L2 representation | formulas pass through a Lie-algebra representation, but the local-twistor prolongation and rolled-carrier adapters remain open |
| L3 geometry | `II=0 <=> total YM` fails both ways; Gauss-reduction energy and connection YM energy are distinct |
| L4 dynamics | coupled equation is YM current balanced by reduction current; full action ownership and normalized connection remain open |
| L5 observation | computation uses the observed four directions and explicit K77 signs; no Euclidean continuation is used for the algebra |
| L6 physics | ordinary detour need not close on coupled shell; coupled BV/detour complex is unbuilt |
| L7 positivity | the K77 reduction energy is indefinite; no positive reduced pairing or decoherence functional |

## 12. Decisive next sequence

1. Choose the actual action-owned pair `(A,R)`—ambient adapted connection,
   Schouten-prolonged local-twistor connection, full Sp connection, or an
   explicit coupled adapter—and reject all silent substitutions.
2. Construct the normalized connection `A^H` if the action uses `II_s^H`, and
   verify the complete transgressed curvature and current.
3. Linearize the coupled Euler--Lagrange system in `(delta A,delta R)` together
   with the moving-reduction gauge map.
4. Build its deformation/BV complex and compute the first two compositions.
   Test whether the reduction-current component cancels the ordinary detour
   obstruction on the **coupled** shell.
5. Push the coupled symbol complex through the exact `Pi4 -> ker Gamma14`
   carrier adapter and compare it with the owned rolled GU operator.
6. Only after endpoint admission, a closed Lorentzian domain, positive reduced
   pairing and nontrivial cohomology exist, ask whether the resulting linear
   structure represents physical superposition.

## Reproduction

```text
python3 tests/channel-swings/selected_k77_total_twisted_yang_mills_current_gate_probe.py
```

passes `62/62` exact ownership, Layer-0, signature, adapted-connection,
Gauss--Codazzi--Ricci, total-current, counterexample, normalization,
moving-reduction and first-variation controls.

## References

- E. A. Ruh and J. Vilms, [The tension field of the Gauss
  map](https://doi.org/10.1090/S0002-9947-1970-0259768-5), *Transactions of
  the American Mathematical Society* 149 (1970), 569--573. The imported
  theorem is used only on its Euclidean Riemannian domain.
- H. Manabe, [Harmonic Gauss sections, object inclusion maps and Yang--Mills
  connections](https://doi.org/10.2996/kmj/1138039896), *Kodai Mathematical
  Journal* 17 (1994), 15--37, for the distinct principal-connection Gauss-
  section construction and its Riemannian hypotheses.
- `explorations/geometry-curvature-emergence/codazzi-sp64-bundle-2026-06-23.md`.
- `tests/wave5/H21_theta_equals_II_proof.py`.
- `explorations/conditional-build/selected-k77-j10-bv-green-descent-gate-2026-08-13.md`.
- `explorations/conditional-build/selected-k77-local-twistor-bach-detour-composition-gate-2026-08-14.md`.
