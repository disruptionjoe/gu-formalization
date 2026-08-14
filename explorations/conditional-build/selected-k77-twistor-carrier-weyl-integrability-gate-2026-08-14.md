---
artifact_type: exact_flat_twistor_carrier_spin_branching_and_weyl_integrability_result
created: 2026-08-14
status: FLAT_DEVELOPABLE_RANK4_TWISTOR_CARRIER_AND_GRAPH_ADAPTER_CONSTRUCTED__C32_OBSERVATION_BRANCHING_TYPED__STRICT_LORENTZIAN_HOLOMORPHIC_ROUTE_CONFORMALLY_FLAT_SCOPED__EUCLIDEAN_ASD_AND_GENERAL_LORENTZIAN_SUCCESSOR_HORNS_OPEN
source_return: SOURCE_SUPPORTS_COMPLEX_TWISTOR_SPACE_REAL_FORM_SPLIT_AND_EUCLIDEAN_ASD_COMPLEXITY__SOURCE_SILENT_GU_TWISTOR_CONNECTION_PHYSICAL_COHOMOLOGY_AND_DECOHERENCE
ledger_rows: [LT-SM8]
ledger_hypothesis: HYP-TW-COHERENCE-01
registry: lab/process/selected-k77-twistor-carrier-weyl-integrability-gate.json
probe: tests/channel-swings/selected_k77_twistor_carrier_weyl_integrability_gate_probe.py
canon_verdict_change: none
---

# Selected K77 twistor-carrier and Weyl-integrability gate

## Result first

The first missing twistor object now constructs on the flat/developable
observer branch. The settled K77 observation split already owns the two
complex rank-two spacetime Weyl factors. With the conventional dual placement,
they assemble into the complex rank-four local twistor carrier

```text
T_GU = S_L direct-sum S_R*.
```

In a flat affine chart, a complexified spacetime vector is a matrix

```text
X:S_R* -> S_L,
```

and its spacetime point is the graph two-plane

```text
S_X = {(X pi,pi):pi in S_R*} subset T_GU.
```

The quotient chart `q_X(u,v)=u-Xv` kills `S_X`, and differentiating the graph
gives the exact tangent adapter

```text
delta X -> Hom(S_X,T_GU/S_X).
```

The determinant of `X` reproduces the complexified Lorentzian conformal
quadratic form. Thus the earlier carrier/incidence gate passes locally and
exactly. A global map to one fixed `C^4` still requires conformal development,
holonomy control and a conformal-spin marking. On a generic curved base the
natural object is a rank-four local-twistor/tractor bundle, not one globally
fixed vector space.

The curvature gate then produces a real branch split:

- A full holomorphic `CP^1` twistor family on complexified four-space requires
  the relevant Weyl-spinor half to vanish. Lorentzian reality conjugates the
  two Weyl halves, so this strict holomorphic route is conformally-flat on a
  real Lorentzian base. It cannot be GU's universal carrier for generic curved
  physical spacetime.
- In Euclidean signature the two Weyl halves are independent. An ASD metric
  may kill the twistor-obstructing half while retaining nonzero curvature in
  the other. The Euclidean-ASD holomorphic route therefore survives as a
  distinct horn.
- A generic Lorentzian successor must choose and construct a different object:
  a Lorentzian CR twistor space, a conformal local-twistor/tractor connection
  with a curvature-controlled BGG sequence, or an ambitwistor/null-geodesic
  complex. Those are alternatives, not names for an already-built common
  object.

The moving-coherence hypothesis survives, but it is now branched rather than
universal. No physical superposition, positive cohomology or decoherence rate
is derived.

## The `C^32` question is now typed exactly

The two sides of a spacetime point are **not** the two source
`C^(32,32)` Weyl halves.

The exact settled K77 branching is

```text
S_14,+^C = (S_4,+ tensor S_10,+) direct-sum (S_4,- tensor S_10,-),
S_14,-^C = (S_4,+ tensor S_10,-) direct-sum (S_4,- tensor S_10,+).
```

Each tensor product has complex dimension `2*16=32`. There are four such
observation summands. Each complexified real ambient Weyl half has two of
them and total complex dimension 64.

This must remain distinct from the source presentation:

- one individual observation summand is `C^32`;
- one complexified real ambient Weyl half is `C^64=C^32+C^32`;
- one source `C^(32,32)` half is a complex-64 Hermitian object;
- a spacetime point `S_X` is a complex two-plane inside `T_GU=C^4`;
- its quotient `Q_X=T_GU/S_X` is another complex rank-two object.

The dimension-level branching is exact. The complete identification of each
complexified real ambient half with the source's Hermitian `C^(32,32)` object
remains the previously recorded C3b pairing debt. In particular, the slogan
“the two sides of the twistor plane are the two `C^(32,32)` halves” is false.

## What the mixed `4x10` connection does

Let `Gamma_4` and `Gamma_10` denote base and normal chirality. Total ambient
chirality is their product. A mixed spin generator has parity

```text
M_mu,a = gamma_mu gamma_a.
```

It anticommutes with each block chirality and commutes with total chirality:

```text
{M,Gamma_4}=0,
{M,Gamma_10}=0,
[M,Gamma_4 Gamma_10]=0.
```

Therefore the mixed connection preserves each ambient Weyl half while
exchanging its paired `C^32` observation summands:

```text
(++ <-> --) inside S_14,+^C,
(+- <-> -+) inside S_14,-^C.
```

This is the precise representation-theoretic content behind the coherence
idea. Vanishing mixed connection coefficients decouple the paired observation
summands; nonzero coefficients couple them. It still does not establish that
the repo's reference-normalized `II_s^H` is that raw mixed connection, nor
that the mixed **curvature** equals a Willmore density or an experimental
decoherence generator.

## Weyl obstruction computation

For one Weyl half write the completely symmetric curvature spinor as five
coefficients

```text
Psi_0,Psi_1,Psi_2,Psi_3,Psi_4.
```

Two standard curvature tests are kept distinct.

First, the local-twistor-spinor integrability map is

```text
C_Psi:S -> Sym^3(S),
(C_Psi)^k_d = Psi_(k+d),
```

represented by the exact `4x2` Hankel matrix

```text
[Psi_0 Psi_1]
[Psi_1 Psi_2]
[Psi_2 Psi_3]
[Psi_3 Psi_4].
```

The probe gives ranks:

```text
flat:     0, kernel dimension 2;
Petrov N: 1, kernel dimension 1;
generic:  2, kernel dimension 0.
```

Second, the alpha-plane Frobenius obstruction is the binary Weyl quartic on
projective spinors. Evaluation at five distinct projective points has exact
rank five, so vanishing on the full `CP^1` fibre forces every `Psi_k=0`.
The Petrov-N control has an isolated principal line but does not make the full
fibre integrable. This prevents an algebraically special survival from being
misreported as a complete twistor fibration.

These finite controls reproduce the standard Weyl-spinor obstruction rather
than replacing the differential-geometric theorem.

## Three hypothesis horns

### H1 — flat/developable Lorentzian boundary-value horn

Use the exact graph carrier above with the `SU(2,2)` real form. Positive-energy
physics would have to arise as boundary values on the null twistor hypersurface
of holomorphic data on a selected positive domain. This is the route emphasized
in Woit's April 2026 slides. It is viable for flat/conformally-flat geometry,
but does not yet extend to generic GU gravity or supply a positive GU quotient.

### H2 — Euclidean ASD plus reconstruction horn

Use the projective right-spin bundle and an ASD Euclidean observer metric, for
which the twistor almost-complex structure is integrable. This can include
nonflat curved metrics. It then owes the full Osterwalder--Schrader or
hyperfunction boundary-value reconstruction, including the imaginary-time
choice, Lorentzian physical domain, and the relation to the normal `J_N/J10`.
Euclidean integrability alone does not protect Lorentzian superposition.

### H3 — general Lorentzian curved horn

Abandon a global Dolbeault complex on `CP^3` as the universal object. Choose
one of:

- a CR complex on a Lorentzian null-twistor or null-geodesic space;
- the conformal local-twistor/tractor connection and a candidate curved BGG
  sequence whose needed compositions must be checked;
- an ambitwistor construction.

The winning object must be derived from GU's base conformal-spin data, accept
the action-owned mixed connection, reproduce the owned Weyl/Dirac/
Rarita--Schwinger principal symbols, and descend through the actual BV/BFV
boundary problem. Merely renaming the curved carrier “twistor” does not pass.

## Composition with the new BFV result

Since the original seven-gate computation, the repository has constructed:

```text
0 -> so(3,4)_21 -> so(7,7)_91 -> T(Spin(7,7)/SO(3,4))_70 -> 0,
```

and proved the selected-orbit Koszul--Tate resolution proper. It has also
proved the complete fixed-label algebraic BFV master equation.

That does not yet furnish the cohomology needed by the twistor hypothesis.
The actual selected-action endpoint has 30 nonzero independent orbit charges
and lies off the unadorned moment-map zero level. A boundary/Green stationarity
law or a covariant edge cotangent carrier with opposite charge must admit the
endpoint before the physical cohomology and positivity gates can be run.

## Updated decisive sequence

1. **Carrier — local pass.** `T_GU=S_L+S_R*`, graph incidence and tangent
   adapter construct exactly on the flat/developable branch.
2. **Choose the curvature horn.** Conformally-flat Lorentzian, Euclidean ASD
   plus reconstruction, or one specified general-Lorentzian successor.
3. **Lift the action-owned connection.** Include the mixed `4x10` term and
   compute the chosen complex's actual curvature obstruction.
4. **Match operators.** Push or BGG-resolve the complex and compare the whole
   owned Weyl/Dirac/RS symbol matrix, not one isolated cell.
5. **Admit the endpoint.** Derive zero boundary charge or an opposite edge
   moment map, then form the proper BV/BFV cohomology.
6. **Construct reality, domain and positivity.** Supply positive energy,
   closed domain and a positive reduced pairing together.
7. **Only then test coherence physics.** Derive an interaction- and
   observable-dependent functional before using the word decoherence.

## Layer 0 and seven-axis read

| layer | result |
|---|---|
| Layer 0 | `T_GU`, `S_X`, `Q_X`, four `C^32` observation blocks, two source `C^(32,32)` halves, `J_N`, `J10`, action pairing and physical pairing remain separately typed |
| L1 algebra | graph incidence, quotient and tangent adapter exact |
| L2 representation | K77 `2x16` half-spin branching and mixed parity action exact |
| L3 geometry | flat/developable twistor constructor exact; generic Lorentzian holomorphic route obstructed by Weyl curvature; Euclidean ASD survives |
| L4 dynamics | mixed connection is a live coupling; its action-owned coefficient and normalized-II bridge remain open |
| L5 observation | strict Lorentzian route conformally-flat scoped; curved successor not selected |
| L6 physics | KT/BFV algebra advanced, but actual endpoint is off zero; transform and physical cohomology open |
| L7 positivity | no positive reduced pairing or closed physical domain |

## Falsifiers and next move

The universal strict-holomorphic Lorentzian version is already killed outside
the conformally-flat stratum. The larger hypothesis is killed if all three
typed horns fail:

- no action-owned connection lift preserves or closes the chosen complex;
- the resulting complex does not reproduce the owned GU operator symbols;
- endpoint admission requires fitted noncovariant edge data;
- the Lorentzian domain destroys complex cohomology; or
- every reduced pairing remains indefinite or degenerate.

The next bounded move is to choose between H2 and H3 for curved GU gravity.
H1 remains the exact flat positive control. The recommended scientific route
is H3: construct the conformal local-twistor/tractor connection first, because
it exists on a generic curved spin conformal base and makes its Weyl/Cotton
curvature explicit. Compare that curved BGG symbol sequence with the owned GU
operator before attempting a Euclidean reconstruction.

## Reproduction

```text
python3 tests/channel-swings/selected_k77_twistor_carrier_weyl_integrability_gate_probe.py
```

passes `54/54` exact ownership, Layer-0, carrier, incidence, branching, Weyl,
real-form and disposition checks with flat, Petrov-N, generic Lorentzian and
Euclidean-ASD controls.

## References

- R. Penrose and W. Rindler, *Spinors and Space-Time*, Vol. 2, Cambridge
  University Press, 1986.
- M. Atiyah, N. Hitchin and I. Singer, “Self-duality in four-dimensional
  Riemannian geometry,” *Proc. Roy. Soc. Lond. A* 362 (1978), 425--461.
- P. Woit, [Wick Rotating Spinors and Twistors](https://www.math.columbia.edu/~woit/twistorunification/marseille.pdf),
  April 3, 2026, especially the complex-space, real-form, ASD and positive-
  boundary-value split.
- P. Woit, [Notes on Wick Rotation and Chiral Field Theories](https://www.math.columbia.edu/~woit/wordpress/?p=15768),
  July 9, 2026. Woit explicitly marks the interpretation as work in progress;
  the note motivates the conjugation/boundary-value gate but does not close it
  for GU.
- `explorations/resolver-wave-k77a-real-spinor-observation-atomic-particle-crosswalk-2026-08-04.md`.
- `explorations/c3prime-split-commutant-certificates-2026-08-12.md`.
- `explorations/conditional-build/selected-k77-stabilizer-koszul-tate-resolution-gate-2026-08-14.md`.
