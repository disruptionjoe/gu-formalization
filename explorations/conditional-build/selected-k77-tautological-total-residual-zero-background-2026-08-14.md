---
artifact_type: exact_background_candidate_totalization_and_legality_gate
created: 2026-08-14
status: LOCAL_FROZEN_FRAME_FIXED_BOUNDARY_TOTAL_RESIDUAL_ZERO_CANDIDATE_SURVIVES__FREE_EDGE_HORN_KILLED__NATIVE_B_EPSILON_Y_LEGALITY_TYPE_MISSING
target_claim: NONE-NOT-A-KILL
source_claims: [SC-ACT-01, SC-ACT-04, SC-ACT-05, SC-ACT-06]
lane_id: SRC-RES-COH-01
revision_basis: fb128b49bcb78eef66ec4822a84ddd28865e0f47
canon_verdict_change: none
ledger_row_changes: none
probe: tests/channel-swings/selected_k77_tautological_total_residual_zero_background_probe.py
registry: lab/process/selected-k77-tautological-total-residual-zero-background.json
source_return: lab/sources/selected-k77-tautological-total-residual-zero-background-source-return-2026-08-14.md
hostile_review: lab/process/hostile-reviews/2026-08-14-selected-k77-tautological-total-residual-zero-background-review.md
---

# Selected K77 tautological total-residual-zero background gate

## Result first

The repository contains a much closer precursor to the missing `SR-1B`
background than the current source-residual audit recorded.  The two exact
tautological branches

```text
B = b_+ Phi1,   T = t_+ Phi1,
B = b_- Phi1,   T = t_- Phi1,

t_+ = (-2+sqrt(3))/208,   b_+ = 1/208-sqrt(3)/312,
t_- = (-2-sqrt(3))/208,   b_- = 1/208+sqrt(3)/312
```

obey, coefficientwise,

```text
Upsilon_B = [312(b+t)^2+t] Phi1 = 0,
metric-volume Euler trace = 624(b^2+bt+t^2/3)+t = 0,
Xi = 2(b+t) Upsilon_B (Phi1 wedge Phi1) = 0.
```

Setting all four independent classical fermion variables and their barred
partners to zero then gives

```text
Upsilon_F = 0,
fermion Euler rows = 0,
fermion connection current = 0,
Upsilon_total = Upsilon_B + Upsilon_F = 0.
```

The bosonic second action is automatically stationary there, and its Hessian
reduces to the Gauss--Newton factorization

```text
H_I2B = L_Upsilon_B^! Q_B L_Upsilon_B.
```

This is a real positive result at **local frozen-frame, compact-support or
fixed-boundary grade**.  It does not yet close `SR-1B`.

Two independent failures prevent promotion:

1. The open-ball construction freezes `Phi1`, Shiab, Hodge, density and
   observation.  It does not construct `B=b Phi1` as the source-owned
   `B(epsilon)` connection on native `Y=Met(X)`, or match its nonzero
   curvature to the distinguished-connection curvature orbit.
2. Both branches carry nonzero endpoint momentum.  The bare action with free
   endpoint variation forces zero momentum and zero moment map, so it excludes
   both branches.  Fixed endpoint data or compactly supported variations make
   the bulk variational statement legal, while boundary-nonvanishing
   transformations remain charged symmetries.

The disposition is therefore

```text
local fixed-boundary total-residual-zero candidate:  SURVIVES
bare free-edge nonzero branch:                       KILLED
native B(epsilon)/Y legality:                        TYPE-MISSING
complete total K,L carrier:                          TYPE-MISSING
SR-1 BACKGROUND-MISSING premise:                     NARROWED, NOT CLOSED
```

## Why this was worth replaying

`SR-1` correctly rejected the nonzero-Krein-null moving-`H_q` critical branch:
that branch has `Upsilon_B != 0` and is not stationary on the full `196` bank.
The tautological branches tested here are different objects.  They predate the
source-residual lane, solve the first residual exactly, and were already shown
to survive the local source-variable first variation.

The audit therefore had to decide whether they supplied the missing
background or merely looked like it.  The exact answer is intermediate:
their algebraic and variational core survives, while their native source
connection and boundary legality remain incomplete.

This packet does not touch the concurrent reverse-`J` gate.  Fixed and moving
complex structures, sign equivalence and mapping-cone descent are independent
questions downstream of a legal total background.

## Current action ownership

The source owns three nearby but distinct objects:

```text
SC-ACT-01:  I1B, whose source-varpi derivative is Upsilon_B;
SC-ACT-04:  I2B = 1/2 <Upsilon_B,Q_B Upsilon_B>;
SC-ACT-05:  Upsilon_total = Upsilon_B + Upsilon_F = 0.
```

The current fixed-natural owner result identifies the source-faithful
fixed-grade `I2B` with the printed endpoint residual square, up to a nonzero
overall scale.  That scale does not change a residual-zero locus.

The source does **not** thereby print a norm square of the total
boson--fermion residual.  This packet consequently proves:

- totalization of the **first-order Euler residual** at zero fermion; and
- automatic stationarity/factorization of the separately owned **bosonic**
  second action.

It does not manufacture a total boson--fermion second action.

## Exact branch calculation

On the frozen tautological family,

```text
R(b,t) = 312(b+t)^2+t,
M(b,t) = 624(b^2+bt+t^2/3)+t.
```

Eliminating `b` gives

```text
97344 t^2 (43264 t^2+832 t+1)=0.
```

The factor `t^2` is the separate zero branch.  The quadratic factor has the
two nonzero roots displayed above.  For each of them:

```text
R=0,
M=0,
b != 0,
t != 0,
b+t != 0.
```

The earlier exact source-variable results supply the following local
composition:

- the complete pointwise source-`varpi` covector vanishes across all
  `14*16384=229376` real `u(64,64)` directions;
- primitive epsilon closes in the bulk through the source-coordinate
  pullback and naturality;
- the ten local metric directions and equation-dual observation preserve the
  zero covector; and
- `Xi=D Upsilon` is redundant at `Upsilon=0`.

These are local functional statements.  They do not prove a global section,
native connection orbit or analytic domain.

## Zero-fermion totalization

The source treats barred and unbarred `nu,zeta` as four independent classical
fields.  Equation 9.16 is bilinear in the barred and unbarred variables, while
equation 9.18 has linear spinor residual classes and a bilinear adjoint-valued
current.  Therefore at

```text
nu=bar_nu=zeta=bar_zeta=0
```

all four fermion Euler rows, every displayed fermion residual class, and the
fermion connection current vanish.  The explicitly admitted nonzero
southeast-block rival is still bilinear and cannot create a zero-field
tadpole.

The executable receipt uses nonzero finite operator blocks as controls.  Its
fermion Hessian is nonzero and a nonzero fermion turns on the linear residual,
so the zero result is structural rather than vacuous.

At this grade,

```text
Upsilon_total = 0 direct-sum 0 = 0.
```

No fermion zero mode, physical cohomology, chirality or particle count is
inferred.

## Variational consequence for the second action

For

```text
I2B = 1/2 <Upsilon_B,Q_B Upsilon_B>,
```

the exact identities are

```text
dI2B = (D Upsilon_B)^! Q_B Upsilon_B,

H_I2B
 = (D Upsilon_B)^! Q_B (D Upsilon_B)
   + <Q_B Upsilon_B,D^2 Upsilon_B>.
```

At either branch the second term vanishes because the residual vector itself
is zero, not merely Krein-null.  The exact nonlinear control in the probe
checks both the on-shell reduction and a nonzero off-shell residual-dependent
term.

This licenses a later bosonic `SR-2` replay only after the background legality
gate closes.  It does not license importing the involutive principal tableau
computed on the different moving-`H_q`/endpoint branch.

## Native `B(epsilon)` and `Y=Met(X)` legality

The source variable is not an arbitrary independent `B`.  It has the form

```text
B(epsilon)=epsilon^-1 Gamma_0 epsilon + epsilon^-1 d epsilon,
T=varpi-B(epsilon),
```

so its curvature must satisfy

```text
F_B = epsilon^-1 F_Gamma0 epsilon.
```

The branch construction instead freezes the moving geometry on a contractible
ball and declares `B=b Phi1`.  Its curvature is nonzero for both branches:
two noncommuting Clifford axes already give

```text
F_01 = b^2 [gamma_0,gamma_1] != 0.
```

Hence the branch cannot be smuggled in as a flat pure-gauge Maurer--Cartan
form.  A curved distinguished connection could still have the required
curvature orbit, but no current receipt constructs the epsilon, proves that
orbit equality, or moves the full native `Phi1`/Shiab/Hodge/density/
observation packet on the branch.

This is `TYPE-MISSING`, not a no-go.  The cheapest next discriminator is the
curvature-orbit equation on the actual distinguished K77 connection, followed
by its first native coefficient jet.  Failure kills these two branches as GU
backgrounds; survival supplies the missing local source tuple.

## Symplectic/BV and boundary disposition

The bulk epsilon equation and endpoint momentum are different variational
objects.  On the branches the exact endpoint coefficient is

```text
p(b,t)=312 t(2b+t) != 0.
```

The existing boundary theorem gives:

```text
free bare endpoint variation:  p_0=p_2=0, hence zero moment map;
fixed endpoint data:            delta g_0=delta g_3=0, momentum unlocked.
```

Thus the nonzero branches fail the first horn and survive the second.  A
generated/Robin graph or compensating edge field remains source-unowned.

For any later `K_total` construction:

- compactly supported or boundary-vanishing gauge parameters may enter the
  bulk gauge image;
- boundary-nonvanishing transformations remain charged symmetries unless an
  explicit BFV edge cancellation is constructed; and
- the rank-25 image, 66 reducibilities and 21-dimensional stabilizer computed
  on other selected fixtures must not be imported.  This branch needs its own
  stabilizer and reducibility calculation.

No presymplectic quotient, BFV phase space or positive reduced pairing is
constructed here.

## PDE/operator scope

The result is a constant-coefficient open-ball solution on a frozen moving
geometry packet.  It supplies neither:

- a Lorentzian closed or closable realization;
- propagation or a Green-hyperbolic complex;
- the source-claimed Euclidean elliptic deformation complex;
- a common domain for `K_total`, `L_total` and the rolled fermion operator;
- positivity, a spectrum or stability.

The next operator gate, if native legality survives, must assemble the
complete bosonic and fermionic linearizations on this branch and test

```text
sigma(L_total)(xi) sigma(K_total)(xi)=0
```

for timelike, spacelike and null covectors.  Euclidean ellipticity requires a
separate source-aligned Euclidean real structure and cannot be inferred from
the Lorentzian K77 fixture.

## Exact assumptions

This scoped survival assumes:

1. the source-aligned real K77 `(7,7)` horn and selected Shiab fixture;
2. the repository normalization in which the branch equations above hold;
3. a contractible local observed patch with frozen `Phi1`, Hodge, density and
   observation coefficients;
4. the source-coordinate pullback `(g,varpi,epsilon)->(g,B,T)`;
5. four independently varied barred/unbarred fermions set to zero;
6. compactly supported variations or fixed endpoint data; and
7. separate ownership of first-order total residual and bosonic `I2B`.

Removing assumption 3 is the next construction.  Removing assumption 6
requires a boundary action or edge completion.

## Outcome-contingent successor

```text
native curvature-orbit and moving-Y gate
├─ passes
│  ├─ assemble K_total,L_total and branch-specific reducibility
│  ├─ replay SR-1 composition
│  ├─ replay bosonic SR-2 factorization and Green concomitant
│  └─ run Lorentzian principal-symbol/domain discriminator
├─ fails
│  └─ kill both tautological branches as GU backgrounds and construct a new
│     residual-first solution on the legal source-connection graph
└─ boundary-only failure
   ├─ retain the local fixed-boundary background
   └─ route the global horn to charged edge completion
```

If zero fermion later acquires a genuine source-owned tadpole, switch to the
already-located nonzero-fermion `Omega0`--gamma-trace saddle.  No such tadpole
exists in the displayed or southeast-nonzero bilinear grammars tested here.

## Claim ceiling and accounting

```text
ledger_row_changes: none
canon_verdict_change: none
residue_or_datum_change: none
quotient_change: none
public_posture_change: none
```

The result constructs no complete GU background, total physical complex,
Euclidean ellipticity, quantum state space, positive cohomology,
superposition law, Born rule, luminous/dark separation, spectrum or empirical
prediction.

## Executable receipt

Run:

```text
PYTHONDONTWRITEBYTECODE=1 _local/cas-venv/bin/python -u \
  tests/channel-swings/selected_k77_tautological_total_residual_zero_background_probe.py
```

The exact SymPy receipt passes `55/55`, including source-owner, branch,
zero-fermion, off-shell Hessian, curvature-orbit, boundary and scope controls.
