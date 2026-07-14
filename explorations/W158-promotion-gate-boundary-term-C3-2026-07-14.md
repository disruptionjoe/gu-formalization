---
artifact_type: exploration
status: exploration (TEAM KEYSTONE-GATE, W158; five personas inline, one worker, no sub-agents; deterministic test with positive controls)
created: 2026-07-14
wave: W158
label: W158
hypothesis: "W154's keystone: the whole coherence-first program reduces to ONE unbuilt object, the promotion-gate BOUNDARY term T4 on the (9,5) q=5 finality frontier, whose variation yields the dark-energy exchange Q, equivalently discharging C3 of the 2026-06-22 divergence-free proof (theta = the Euler-Lagrange derivative of a gauge-invariant action on Y14). BUILD it explicitly on the verified Cl(9,5) rep, machine-check its properties, and answer the sharpest new question W154 left open: does the q=5 Krein-indefinite structure SUPPLY the non-monotone fluctuation that sources the RISE (the z~0.405 crossing), or is the crossing genuinely free?"
title: "W158 -- the promotion-gate boundary term T4 and the C3 discharge. VERDICT: PARTIAL. S_gate is WRITTEN EXPLICITLY on the q=5 frontier and its algebraic properties are machine-checked EXACT: S_gate = oint_frontier n_a J^a with J^a = Re<Psi, K_S e_a Psi>_Krein is a REAL Krein current; J^a transforms as a VECTOR (equivariant/adjoint) -- exactly theta's Section-2 property; S_gate is EXACTLY gauge-invariant under Stab(n) (the frontier little group) and moves under non-stabilizer boosts (a boundary term correctly breaks G -> Stab(n)); its variation delta S_gate/delta Psibar = K_S c(n) Psi is a nonzero frontier current; the Krein grading gives the confirmed-count trace over H_C+ non-negative -> Lambda >= 0. The C3 discharge is PARTIAL: the Noether-second-theorem MECHANISM (gauge-invariant action + equivariant EL current => D*J = 0) is machine-checked, but the IDENTITY J == theta = pi - eps^{-1} B eps rides the inhomogeneous-gauge distortion-sector map the 2026-06-22 proof left open, so C3 is discharged as a MECHANISM, not as the specific-theta identity. The fluctuation-supplies-rise question resolves NEGATIVE at the mean and SHARPENS the obstruction: even with the 5 unconfirmable directions LAGGING the 9 confirmed ones, the Krein difference N_K = 9 f_+ - 5 f_- stays MONOTONE (the 9-weighted un-lagged confirmed sector dominates the flux at every epoch), so the q=5 indefinite grading does NOT convert monotone record accretion into a rise. The rise appears ONLY when a genuine NON-monotone fluctuation is present; its natural HOME is the q=5 unconfirmable sector and its SIGN is forced +, but its existence, amplitude, and epoch are a FREE realization -- so the z~0.405 crossing stays FREE. E1: this is the THIRD consecutive one-object reduction (bulk operator -> covariant operator -> promotion-gate term) and W158 reduces AGAIN (to the confirmed-vs-unconfirmable schedule lag / the frontier fluctuation two-point function) rather than building-closed or obstructing -- so per the E1 rule the chain is DEGENERATING and the build path should be demoted in the rankings."
grade: "exploration / conditional register throughout. Every 'S_gate does X' reads 'under the reverse-engineered conditional structure, X'; nothing asserts GU, that the DESI wiggle is real, or that any decomposition is physical. COMPUTED (deterministic, tests/W158_promotion_gate_boundary_term.py, 26/26, exit 0; positive controls first): PC reproductions -- Gamma Gamma^dag = 14 I (residual 0), Krein anti-self-adjointness Sigma^dag K_S + K_S Sigma = 0 for all 91 generators (residual 0), [rho(J), Pi] = 0 for the full so(9,5) generator incl. a boost (residual 0), (9,5)=(3,1)+(6,4) / q=5, W154's monotone-mean obstruction and F1^F3 compatibility, the everpresent amplitude Lambda ~ 1/sqrt(N_4) ~ H^2; the BUILD -- J^a real (max |Im| 1.8e-15), equivariant vector law delta J^a = <Psi, K_S [e_a, Sigma] Psi> (residual 5.3e-15) with [e_a, Sigma] closing on span(e) (residual 0), gauge-invariance under Stab(n) (residual 7.1e-15) with a non-stabilizer boost moving it (0.80), the frontier variation nonzero with c(n)^2 = eta(n,n) I (residual 0); the C3 Noether input (gauge-orbit variation sums to 1.9e-13); the RISE tests (monotone-in stays monotone-out under the Krein difference; a q=5-sector fluctuation carries a single crossing whose epoch tracks the free peak). CITED (not re-derived): W131 (parallel Pi, nabla K = 0, (9,5), the covariant operator built at symbol level), W150 (the q=5 finality frontier, H_C+ proper maximal positive subspace), W154 (the reverse-engineered S, the T4 localization, the monotone-mean obstruction), W152/W153 (marble/wood), W146 (everpresent-Lambda), W138 (kill battery), the 2026-06-22 divergence-free proof (theta, C1/C2/C3). Per the E1 rule this wave is a CONSTRUCTION with a PARTIAL build: no FIT row moves, no gated number unlocks; H41 stays unbuilt (narrowed: the boundary term is now written with gauge-invariance + EL-current equivariance machine-checked, but it does not DERIVE Q's rise/epoch); H59 stays OPEN; the count stays {1,3}."
construction: "program-native where the objects are GU's (Y14, the record field Psi in carrier B / ker Gamma, the Krein/C-operator structure K_S / Pi / H_C+, the (9,5) split, the q=5 finality frontier); standard-field where the machinery binds any construction (Noether's second theorem, the equivariance->divergence-free argument, the interacting-vacuum decomposition -- PORTED; the everpresent-Lambda law -- PORTED Sorkin/ADGS). Forks named per GEOMETER-VS-PHYSICS-OBJECTS.md; the boundary functional is the geometer's object (a Krein-graded conormal current built from the constant equivariant structures W131 transported), not the physicist's F-analytic vertex."
depends_on:
  - explorations/W154-reverse-engineered-source-action-2026-07-14.md
  - explorations/W131-covariant-operator-y14-2026-07-14.md
  - explorations/W150-substrate-sweep-consensus-crypto-2026-07-14.md
  - explorations/W152-marble-and-wood-source-fix-2026-07-14.md
  - explorations/W146-substrate-sweep-theoretical-physics-2026-07-14.md
  - explorations/W138-issuance-kill-battery-2026-07-14.md
  - explorations/dark-energy-cosmology/dark-energy-divergence-free-proof-2026-06-22.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W158_promotion_gate_boundary_term.py
---

# W158 -- the promotion-gate boundary term T4 and the C3 discharge

Test: `tests/W158_promotion_gate_boundary_term.py` (26/26, exit 0). Deterministic (fixed seed
20260714); the algebra runs on the repo's verified Cl(9,5) = M(64,H) representation via
`gen_sector_bridge`; the cosmological pieces run the same closed-form models W154 used.

Five personas ran inline in one worker, sequentially (no sub-agents): (1) constructive field
theorist, (2) Krein/C-operator specialist, (3) GR/interacting-vacuum theorist, (4) numerical/
symbolic engineer, (5) honesty auditor/E1. The positive controls run first.

## 0. The object, and why this is the keystone

W154 reverse-engineered a single coherent source action `S` (the record field `Psi` fundamental
on Y14, the metric a derived shadow `g[Psi,C]`) and reduced the whole coherence-first program to
ONE unbuilt object: **the promotion-gate boundary term T4** -- a boundary functional on the (9,5)
`q=5` finality frontier whose variation yields the dark-energy exchange `Q`, equivalently
discharging **C3** of the 2026-06-22 divergence-free proof (`theta` = the Euler-Lagrange
derivative of a gauge-invariant action on Y14). Building it would (a) close debit-3 (the source
action's last unbuilt term); (b) turn debit-2 from half-derived to derived (`S` would DERIVE `Q`'s
rise-and-fall, not just its character); (c) supply the genuine reason the replaced cosmological-
constant term is divergence-free (the marble/wood fix, W152/W153).

W154 also sharpened the debit-2 residue to one precise question: the everpresent MEAN
`Lambda = c/sqrt(N)` with monotone `N` gives monotone WITHDRAWAL, so the RISE needs a NON-monotone
fluctuation, and the sharpest target is whether the `q=5` Krein-indefinite directions SUPPLY that
fluctuation. This wave writes T4 explicitly, machine-checks its properties, and answers that
question head-on.

## 1. Persona 1 -- constructive field theorist: S_gate written explicitly

The finality frontier is the measurement-gated `Y14 -> X4` promotion surface: the moving edge
between confirmed records (`H_C+`, the C-positive subspace) and the `q=5` unconfirmable remainder
(W150). Write the promotion-gate boundary term as a conormal Krein current on that frontier:

```
S_gate  =  oint_{frontier}  n_a  J^a ,      J^a  =  Re < Psi , K_S e_a Psi >_Krein
```

where `Psi` is the record field (a spinor section on the RS carrier), `e_a` are the Cl(9,5)
gammas, `K_S = beta_S = e_0 e_1 ... e_8` is the spinor Krein form, and `n` is the frontier
conormal -- a `q=5` (indefinite / negative-eta) direction, because the finality frontier's normal
points into the unconfirmable sector. The variation is a boundary current:

```
delta S_gate / delta Psibar  =  K_S c(n) Psi ,      c(n) = sum_a n_a e_a
```

This is degree-0 in derivatives (a single conormal Clifford contraction, not a bulk kinetic
operator), so it is a genuine codimension-1 frontier flux, not a bulk term. The test confirms the
current is nonzero and that `c(n)^2 = eta(n,n) I` exactly (the conormal is a real frontier
direction; for the indefinite `n` chosen, `eta(n,n) < 0`, a timelike/unconfirmable normal). This
is the exchange current: a record promotes when it crosses the `q=5` frontier, and the promotion
flux across it is `J^a` restricted to the surface -- the `Q^nu` of debit-2 (Persona 3).

The machinery is entirely W125/W131/W150's: the constant equivariant projector `Pi`, the parallel
Krein form (`nabla K = 0`, W131), the `(9,5)` split, the `q=5` frontier (W150). Nothing new is
postulated; the boundary term is assembled from transported constant structures.

## 2. Persona 2 -- Krein/C-operator specialist: gauge-invariance and the sign

The load-bearing property is gauge-invariance, because it is what feeds Noether's second theorem
(the C3 discharge). Three exact facts, machine-checked on the real rep:

- **The Krein current is real (SG1).** `J^a = <Psi, K_S e_a Psi>` has `max |Im| = 1.8e-15`: `K_S e_a`
  is Krein-hermitian, so `J^a` is an admissible real flux density.
- **The current is equivariant -- it transforms as a VECTOR (SG2).** Under a gauge transformation
  `Psi -> Psi + Sigma Psi` (spin generator `Sigma`), using the Krein anti-self-adjointness
  `Sigma^dag K_S + K_S Sigma = 0` (W131 A4, exact 0.0 for all 91 generators),
  `delta J^a = <Psi, K_S [e_a, Sigma] Psi>`, and `[e_a, Sigma]` closes on `span(e)` (residual 0):
  so `J^a` rotates as a frame vector. **This is exactly theta's Section-2 equivariance property**
  (the 2026-06-22 proof: `theta` is an equivariant ad-valued 1-form). The GU-specific content is
  that the Krein grading `K_S` is what makes the current equivariant AND sign-graded.
- **The boundary term is gauge-invariant under Stab(n) (SG3).** `S_gate = n_a J^a` is EXACTLY
  invariant (residual 7.1e-15) under every generator of the little group `Stab(n)` (the `Sigma_ij`
  with `i,j != frontier-index`), and MOVES (0.80) under a non-stabilizer boost that mixes `n` into
  another direction. A boundary term SHOULD break the full group to the stabilizer of its conormal;
  the invariance under `Stab(n)` is the gauge-invariance leg the C3 discharge needs, and the
  breaking under the rest is the correct behaviour of a genuine frontier functional, not a defect.

**The sign that signs Lambda (SG5).** The confirmed count `N = Tr(P_sigma eta_+ P_sigma)` is a
trace over the `H_C+` positive subspace, non-negative by construction, so the everpresent
`Lambda ~ 1/sqrt(N)` is real and positive -- W154's T2 sign pin, reproduced here at the trace
level. `Lambda >= 0` (F3) is a CONSEQUENCE of the Krein grading, not an extra postulate.

## 3. Persona 3 -- GR/interacting-vacuum theorist: the C3 discharge and Q

**The C3 mechanism, machine-checked (C3a/C3b).** The 2026-06-22 proof's cleanest route to
divergence-freedom is C3: if `theta` is the EL derivative of a gauge-invariant action on Y14, then
`D_A* theta = 0` by Noether's second theorem (equivariance -> perpendicularity to gauge orbits ->
codifferential vanishes). For `S_gate`: it is gauge-invariant (SG3), `J` is its EL current (SG4),
and `J` is equivariant/adjoint (SG2). The Noether INPUT is machine-checked here as the gauge-orbit
variation of `S_gate` over `Stab(n)` summing to zero (residual 1.9e-13): the invariance forces the
EL current perpendicular to the gauge orbits, which is the `D*J = 0` mechanism. So the
**divergence-free-for-a-genuine-reason MECHANISM is discharged**: `S_gate`'s exchange current is
divergence-free because `S_gate` is a gauge-invariant action, exactly Weinstein's "equivariance
leads to divergence-free" and the marble/wood fix's genuine reason (W152 Persona 1 route ii).

**What is NOT closed (the honest C3 boundary).** C3 as the 2026-06-22 proof states it requires the
current to BE the specific `theta = pi - eps^{-1} B eps` (distortion minus conjugated potential in
the inhomogeneous gauge group). `S_gate`'s current has theta's equivariance property, but the
identification `J == pi - eps^{-1} B eps` needs the distortion-sector map (which connection `nabla`
is the distortion `pi` of, which potential `B`) -- the same map the 2026-06-22 proof left open at
C1/C2. So **C3 is discharged as a MECHANISM (gauge-invariant action -> Noether II -> divergence-
free, with a concrete gauge-invariant `S_gate`), not as the specific-theta identity.** This is a
real advance over the 2026-06-22 status (which had only the abstract "IF theta is such an EL
derivative"): here a concrete gauge-invariant boundary action with an equivariant EL current is
exhibited. It is honestly short of "theta is THIS action's EL derivative."

**Q and its character.** The exchange current `Q^nu = J^nu|_frontier = <Psi, K_S c(e^nu) Pi Psi>`
inherits the character W154 derived: clock-coupled (it tracks the promotion rate = what `S_gate`
IS), sign-graded (the Krein form makes it change sign), amplitude O(1) in `q_B` (the everpresent
law forces `Lambda ~ H^2`, PC4). The rise-and-fall CHARACTER is carried; the specific epoch is the
subject of Persona 4.

## 4. Persona 4 -- numerical engineer: does the q=5 structure SOURCE the rise?

This is the sharpest new question, and the answer is a clean, sharpening NEGATIVE.

- **RISEa (the mean obstruction, reproduced).** A shared monotone accretion schedule across all 14
  directions gives `Lambda = c/sqrt(N)` monotone -> `Q` monotone withdrawal. W154's obstruction,
  reproduced at the Krein level.
- **RISEb (the KEY new negative result).** Refine `N` into the Krein-graded frontier trace
  `N_K = 9 f_+ - 5 f_-` over the 9 confirmed and 5 unconfirmable directions, and let the
  unconfirmable sector LAG the confirmed one (the natural reading of "permanently harder to
  confirm"). **`N_K` stays MONOTONE increasing**: for `a^3`-type accretion, `9 f_+' = 135 a^2`
  exceeds `5 f_-' = 75 (a-lag)^2` at every epoch (the 9-weighted, un-lagged confirmed sector
  dominates the flux). So a monotone-in, Krein-graded-out flux is STILL sign-definite: **the `q=5`
  indefinite grading does NOT convert monotone record accretion into a rise.** This SHARPENS
  W154: it was plausible the indefinite sector might supply the non-monotonicity for free; the
  computation says it does not.
- **RISEc (where the rise actually lives).** A rise appears ONLY when a genuine NON-monotone
  fluctuation is present. Its natural HOME is the `q=5` unconfirmable sector (a transient in the 5
  indefinite directions), and its SIGN is forced `+` by the Krein grading (Persona 2). But with the
  fluctuation absent the flux is monotone withdrawal (no crossing); with it present, `Q` crosses
  zero once and **the crossing EPOCH tracks the free fluctuation peak** (RISEc3): `S_gate` does not
  pin it. So the `q=5` structure LOCALIZES and SIGNS the fluctuation but does not SOURCE it -- the
  `z ~ 0.405` crossing stays FREE.

`tests/W158_promotion_gate_boundary_term.py`, 26/26, exit 0. Positive controls first (PC1-PC4:
the W131 exact algebra, the `(9,5)`/`q=5` split, W154's obstruction and F1^F3 compatibility, the
everpresent amplitude), then the build (SG1-SG5), the C3 Noether input (C3a/C3b), the rise tests
(RISEa-c), and the E1 count.

## 5. Persona 5 -- honesty auditor / E1: verdict and the degeneration flag

**Build verdict: PARTIAL.** The term is WRITTEN and its algebraic properties are machine-checked
EXACT (real Krein current, equivariant vector transformation, gauge-invariance under `Stab(n)`,
nonzero frontier variation, sign pin). Per the E1 rule, a written-down term whose properties
machine-check is more than a name -- but this one does not machine-check the two properties that
would make it BUILT: (i) that its EL current IS Weinstein's `theta` (C3 is a MECHANISM, not the
identity); (ii) that its variation DERIVES `Q`'s rise/epoch (the rise rides a free fluctuation).
So: **PARTIAL** -- explicitly, PARTIAL-{theta-identity, Q-rise-epoch}.

**C3-discharge verdict: PARTIAL.** The gauge-invariant-action -> Noether-II -> divergence-free
mechanism is discharged with a concrete `S_gate`; the specific-theta identity is not.

**Fluctuation-supplies-rise verdict: NEGATIVE (crossing still free).** The `q=5` grading does not
convert monotone accretion into a rise (RISEb); it localizes and signs the fluctuation, but the
rise's existence, amplitude, and epoch are a free realization (RISEc). This is progress over W154
(the free object is now sharper -- the confirmed-vs-unconfirmable schedule lag / the frontier
fluctuation two-point function -- and its SIGN and HOME are pinned), and it is honestly short of
sourcing the rise.

**E1 one-object-reduction count: THREE, and it reduces AGAIN.** The chain is
`W125` (whole program -> bulk operator on Y14) -> `W131` (bulk operator -> algebraic half BUILT +
the Y14 propagator) -> `W154` (-> the promotion-gate boundary term T4) -> `W158` (T4 written, its
gauge-invariance and EL-current equivariance machine-checked, but reducing AGAIN to the
confirmed-vs-unconfirmable schedule lag / the frontier two-point function). This is the THIRD
consecutive one-object reduction, and W158 neither builds-closed nor obstructs -- it reduces once
more. **Per the E1 rule the chain is DEGENERATING**: the build path (keep-reducing-the-source-
action-to-its-next-term) should be demoted in the rankings, and the next wave should either
BUILD-closed the frontier two-point function (a genuine analytic/statistical object: the fluctuation
correlation that would pin the epoch) or OBSTRUCT it (prove the epoch cannot be pinned by any
gauge-invariant `S_gate`, which would make the crossing PROVABLY free = a DR3-style honest limit),
not name a fourth object.

## 6. What this does NOT do (the honest limits)

- Everything is conditional / exploration grade. Nothing asserts GU, that the DESI wiggle is real
  (W144 fits it as HYPOTHESIS; the DR3 bet is live), or that any decomposition is physical.
- The build is algebraic/symbol-level (the Krein current, its equivariance, gauge-invariance under
  `Stab(n)`, the frontier variation). No global analysis on Y14 (the propagator / two-point
  function on the non-compact frontier) is claimed -- that is precisely the object the rise reduces
  to. The interacting-vacuum decomposition and the everpresent-Lambda law are PORTED and labelled.
- C3 is discharged as a MECHANISM, not as the `theta = pi - eps^{-1} B eps` identity; the
  distortion-sector map (C1/C2 of the 2026-06-22 proof) is untouched.
- W138 battery honored: the built `Q` is a boundary/schedule reading (G4 alive side, not a rate),
  its magnitude routes through the everpresent `Lambda ~ H^2` which relabels de Sitter (G5 bites on
  the magnitude, novelty only from the fluctuation's sign+time-dependence, as W146/W154 recorded);
  no mu_DW identification (G3); no claim to BE the DESI signal beyond hypothesis (G2). No gate is
  newly cleared or newly failed.
- Claim-status: no status moves. H41 stays unbuilt (narrowed: the boundary term is now written
  with gauge-invariance + EL-current equivariance machine-checked, but it does not DERIVE `Q`'s
  rise/epoch, which is what H41 as a Q-deriving dynamical action requires); H59 stays OPEN; the
  count stays {1,3}. No canon / RESEARCH-STATUS / verdict / posture change; no spec FIT row moves.
- Tri-repo gating honored: "record / substrate / promotion / finality / confirmed / unconfirmable"
  are local postulate labels (W136/W150 sense); the issuance concept is owned by temporal-issuance,
  MEASURE by time-as-finality; GU owns the field-equation / boundary-term / Krein math only; no
  cross-repo identity claim. Zero em dashes in paper-facing text.

*Filed 2026-07-14 by Team KEYSTONE-GATE (W158). Five personas inline in one worker (constructive
field theorist, Krein/C-operator specialist, GR/interacting-vacuum theorist, numerical engineer,
honesty auditor/E1); no sub-agents. Reproducible: `python -u tests/W158_promotion_gate_boundary_term.py`
(26/26, exit 0; four positive controls first). Exploration grade; conditional register; no canon
movement; H41 unbuilt; H59 OPEN; the count stays {1,3}. E1: third consecutive one-object reduction,
DEGENERATING -- demote the build path.*
