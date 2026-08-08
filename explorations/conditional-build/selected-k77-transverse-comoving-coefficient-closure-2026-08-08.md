# Selected K77 transverse comoving coefficient closure

Date: 2026-08-08

Status: exact local construction on the conditional Spin-native selected K77
parent; ledger v0.94 distance migration only

Source return:
`SOURCE-CONFIRMS_RAW_UPSILON_AND_AUGMENTED_TORSION__SOURCE-SILENT_TRANSVERSE_COMOVING_COEFFICIENT_CLOSURE`

## Result in plain English

One large-looking part of the missing metric derivative is not an independent
physical term. When the metric moves, the orthonormal coframe, Clifford
generators, Hodge operator and tautological `Phi` forms must move with it. The
repo had proved this only for one transverse-traceless example. This wave proves
it for all ten metric values and for all six directions transverse to the
diffeomorphism orbit in timelike, spacelike and null symbol classes.

That closes the **coefficient-motion packet** without adding or fitting a
coefficient. It does not make the physical source derivative vanish. The
already constructed principal augmented-torsion response remains rank six in
every causal class. What remains is now smaller and better typed: the component
normal derivatives of augmented torsion and curvature, the complete
Levi-Civita connection derivative beyond its principal symbol, and the
observation/soldering normal jets.

## Construction

Let `G(g)=g direct-sum G_DW(g)` be the fourteen-dimensional gimmel metric and
let `H=D_g G[h]`. For every symmetric base-metric variation `h`, define the
`G`-self-adjoint square-root-gauge coframe lift

```text
A_h = -1/2 G^{-1} H.
```

Then, exactly,

```text
H + A_h^T G + G A_h = 0.
```

Thus the moving frame is an infinitesimal isometry between the neighbouring
Clifford metrics. The Clifford relations are constant in that frame. For the
Hodge operator on every degree used by the displayed Shiab composition,

```text
D_g(*)[H] = * rho_in(A_h^T) - rho_out(A_h^T) *.
```

The certificate checks degrees one, two and fourteen explicitly. The
tautological identity also has zero comoving component derivative,

```text
-A_h Phi1 + Phi1 A_h = 0,
```

and `Phi2=1/2 Phi1 wedge Phi1` follows.

At the selected stationary point,

```text
T* = -(kappa/312) Phi1,
F_A* = T* wedge T*,
Shiab(F_A*) + * kappa T* = 0.
```

The two constituents are separately nonzero. Their fixed-frame target
transports are also nonzero, but they are exact negatives. Therefore the
comoving coefficient derivative of the raw residual cancels coefficientwise.
This is tensor naturality of a zero residual, not a new field equation.

## Exact ranks

| object | timelike | spacelike | null |
|---|---:|---:|---:|
| physical metric transverse projector | 6 | 6 | 6 |
| induced total-metric family | 6 | 6 | 6 |
| canonical comoving coframe family | 6 | 6 | 6 |
| frozen-frame Hodge motion, degree 1 | 6 | 6 | 6 |
| frozen-frame Hodge motion, degree 2 | 6 | 6 | 6 |
| one nonzero constituent's target transport | 6 | 6 | 6 |
| total raw-residual coefficient transport | 0 | 0 | 0 |
| principal augmented-torsion source response | 6 | 6 | 6 |

Across the unrestricted metric fibre, both `h -> H` and `h -> A_h` have rank
ten. The fixed-frame degree-one and degree-two Hodge families also have rank
ten, so the closure is not a zero-input artifact.

## Layer 0

| object | What this wave establishes | What it does not establish |
|---|---|---|
| fixed-coordinate Hodge derivative | nonzero rank-ten family | an independent physical coupling |
| comoving coframe lift | canonical local `G`-self-adjoint representative | a global frame, new epsilon field or observation section |
| coefficient transport of raw `Upsilon` | zero at the selected residual-zero point | complete `D_g Upsilon` |
| principal augmented-torsion derivative | inherited rank-six live response | the lower-order connection/curvature completion |
| pointwise naturality | local coefficient closure | formal adjoint, Green domain, BV/BFV or positivity |

Any other metric-compatible lift differs from `A_h` by a `G`-skew frame gauge.
The square-root gauge fixes a representative; tensor naturality and transport
of the zero residual are independent of that representative. No new dynamical
field is introduced.

## Specialist pre-assessment and hostile post-review

- **Differential geometry:** the result is a natural-bundle statement; the
  fixed-frame derivative and covariant derivative must not be added as two
  owners.
- **Symplectic geometry:** no presymplectic current or reduced phase space is
  produced. The action variation still needs the component-normal field jets.
- **Variational PDE:** the result removes coefficient derivatives from the
  unknown list but leaves the live rank-six principal source response.
- **Real Clifford/Krein:** the proof uses exact real K77 metric compatibility;
  it says nothing about positive energy or a global Krein domain.
- **Complex/path-integral:** no contour, measure, saddle or reflection-positive
  completion follows from finite pointwise naturality.
- **Source criticism:** the raw residual and augmented-torsion arena are
  source-confirmed. The transverse closure is repository-derived.
- **Exact algebra:** Python passes `116/116`; independent Sage passes `13/13`.
- **Constraint accounting:** no free object, residue, quotient, fork or datum
  changes.

The three-charge hostile review accepts the local coefficient closure and
rejects the stronger reading that physical `D_g Upsilon` is now complete. The
summary is intentionally typed as `coefficient packet closed`.

## Frontier delta

Conditions closed: `3`; opened: `0`.

1. all-ten metric-induced comoving coframe/Clifford compatibility;
2. Hodge/Phi naturality on all three transverse sixes;
3. selected raw-residual coefficient target-transport cancellation.

Remaining named conditions: `2`.

1. Construct component-normal `delta T` and `delta F`, the complete
   lower-order Levi-Civita connection derivative, and observation/soldering
   jets; then assemble complete physical `D_g Upsilon` coefficientwise.
2. Construct its formal adjoint, Green concomitant and common analytic/
   symplectic domain.

P1/P2/P3 remain unused. Curt remains formally separate. `TG-1 AND TG-2 AND
TG-3` remains not promoted. No signature, canon, claim-status, public-posture,
Einstein, particle, chirality, generation-count or quantum claim moves.

## Evidence

- `tests/channel-swings/selected_k77_transverse_comoving_coefficient_closure_probe.py`
- `tests/channel-swings/selected_k77_transverse_comoving_coefficient_closure_independent.sage`
- `lab/process/selected-k77-transverse-comoving-coefficient-closure.json`
- `lab/process/hostile-reviews/2026-08-08-selected-k77-transverse-comoving-coefficient-closure-review.md`
