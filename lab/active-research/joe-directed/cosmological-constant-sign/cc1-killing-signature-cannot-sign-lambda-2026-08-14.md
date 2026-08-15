---
artifact_type: exploration
status: exploration
doc_type: sign-availability-gate
created: 2026-08-14
work_item: CC-1
channel: cosmological_constant_sign
title: "CC-1: the Killing signature does NOT predict sign(Lambda), and the reason is exact. Every SM-preserving direction in `ad = so(6,4)` lies inside the compact summand `k` (`p` carries no SM singlet at all), so the Killing form is negative definite on the whole available 2-plane, Gram diag(-48,-32) -- but `so(6,4)` admits exactly ONE invariant bilinear form and NO invariant linear functional, so the quadratic order carries exactly one free real constant. What DOES survive without any potential declaration: for EVERY Ad-invariant polynomial potential of degree <= 4, a nonzero VEV that is a radial local minimum LOWERS the vacuum energy strictly, direction-independently. That is the anti-de Sitter direction, opposite to the observed Lambda > 0. Degree <= 4 is the exact boundary: an explicit degree-6 invariant has an SM-preserving critical point with V = +1 and a PSD Hessian. Also killed exactly: the LITERAL reading of SC-COS-01 (`Lambda` = the VEV) is TYPE-MISSING -- no gauge-invariant real number is linear in an ad-valued VEV."
grade: "EXACT: integer matrix Lie algebra, Fraction linear algebra over Q, sympy polynomial identities, and one finite-field rank certificate whose error direction is stated and safe (rank mod p <= rank over Q). 61/61. NOT: a prediction of sign(Lambda), a derivation of dark energy, a magnitude, a statement about SG4's completion, a claim about the observation/section mechanism, a movement of the standing Q2-FREE verdict, or any claim-status movement."
disposition: KILLING_SIGNATURE_DOES_NOT_FIX_SIGN_OF_LAMBDA__ROUTE_KILLED__LITERAL_VEV_READING_TYPE_MISSING__DEGREE_LE_4_SHIFT_IS_STRICTLY_NEGATIVE_AND_DIRECTION_INDEPENDENT__DEGREE_6_ESCAPES__Q2_FREE_INDEPENDENTLY_CORROBORATED
target_claim: SC-COS-01
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - lab/active-research/joe-directed/photon-extra-vector-spectrum/pv2-observation-cannot-reach-the-extra-vectors-2026-08-14.md
  - lab/active-research/joe-directed/photon-extra-vector-spectrum/pv1-available-orbits-retain-an-extra-massless-vector-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/mj3-4-source-vev-channel-and-twenty-lens-hypothesis-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/mj5-b-minus-l-exactly-preserved-2026-08-14.md
  - lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md
  - lab/sources/source-claim-register.yaml
  - explorations/threads/B-omega0-curvature-dark-energy-scoping-and-first-swing-2026-07-11.md
  - explorations/decision-tree-Q2-sector-bit-forced-free-supplied-2026-07-21.md
  - explorations/W211-krein-sign-godel-independent-five-method-synthesis-2026-07-14.md
  - canon/gu-forces-field-space-declaration-RESULTS.md
scripts:
  - tests/channel-swings/joe_directed_lambda_sign_probe.py
---

# CC-1 — the Killing signature does not sign Lambda, and the exact reason why

## 0. Target claim, named before anything is computed

`lab/sources/source-claim-register.yaml` registers two hard-core, `ADHERED`
source claims:

- **`SC-COS-01`** — *"The cosmological constant is actually the Vacuum
  Expectation Value (VEV) of a Field which plays the role of a fundamental
  mass..."*
- **`SC-MAS-03`** — *"Cosmological 'Constant' Lambda <-> Spinless Gauge Field
  <-> Fermion Mass"* (draft-2021 p.62, eq. 12.21)

MJ-4 already killed the **fermion-mass leg** under the direct reading. This
gate takes the **Lambda leg**, and asks the question the channel was opened
for: *does the Killing signature of GU's own gauge algebra, plus the
availability constraints on an SM-preserving vacuum, fix the SIGN of Lambda
without declaring a potential?*

**Answer, up front: no. The route is killed, for a reason that is exact and
that also produces one genuine surviving inequality.**

## 1. Prior art, attributed — none of this is re-claimed

This is the densest prior-art field in the repository and the attribution
matters more here than the result.

| prior art | what it already owns | status here |
|---|---|---|
| `explorations/decision-tree-Q2-sector-bit-forced-free-supplied-2026-07-21.md` | **`Q2-FREE`**: *"The DE sign is a free (discrete, exactly-located, record-welded) parameter"* | **governing.** Nothing below contradicts or re-derives it; CC-1 is an independent corroboration from the gauge-algebra side |
| `explorations/W211-krein-sign-godel-independent-five-method-synthesis-2026-07-14.md` | five independent methods return `RESIDUAL-BIT-STANDS`; *"Symmetry reduction LIBERATES the sign as a free Z/2; it does not force it"* | **governing.** CC-1 finds the same liberation in a different sector |
| `explorations/threads/B-omega0-curvature-dark-energy-scoping-and-first-swing-2026-07-11.md` (B1) | **the idea that a `(6,4)` signature can sign a Lambda contribution**: *"the DeWitt/gimmel metric is indefinite (signature `(6,4)` on the fiber), and its trace-reversal makes the conformal (trace) direction the negative-norm direction ... it fixes the sign of the cosmological constant this term would contribute"* | **prior art for the mechanism idea.** Thread-B works with the DeWitt form on the **vector 10** and the second fundamental form; CC-1 works with the **Killing form on the adjoint 45**. Different objects, same idea-shape. Thread-B owns the idea |
| `explorations/wave24/H45-H2-vs-II2-binary-2026-07-11.md` | *"`\|II\|^2` gives a POSITIVE DeWitt-Lambda leading contribution ... COMPUTED; the net sign is positive at ARGUED grade"* | prior positive-sign claim, conditional on the unbuilt P2 binary. Not touched |
| `W145 / W146 / W152 / W154 / W156` | Krein/C-operator route to `sign(Lambda) = +`, repeatedly self-labelled *"NAMED, not built"* | prior, unbuilt. Not touched |
| `explorations/blockbuster-p1-de-sign-covariance-2026-07-19.md` | `w_DE(z) >= -1` at toy grade, Prediction Packet 1 | prior. Not touched |
| `comparative-tensions-ledger-cosmo-gravity-2026-07-21.md` | `PRED-NORM-RANK = RESOLVED_NO_GO` — the Lambda **magnitude** is a pure import | governing. CC-1 says nothing about magnitude |
| PV-2 (this lane) | `so(6,4) = k(21) (+) p(24)`, Killing negative on `k`, positive on `p`, SM inside `k` | **reused verbatim in construction.** No novelty claimed; the probe re-derives it as a control |
| MJ-4 (this lane) | the 45 is absent from `16 (x) 16`; the fermion-mass leg of `SC-MAS-03` fails under the direct reading | not re-derived |
| `lab/process/paired-curt-eric-gu-axiom-graph.json` `AX-R06` | *"A distortion or spinless gauge-potential VEV may replace a fixed cosmological constant, but it is not automatically the Higgs or a dark-energy prediction"* | this gate is exactly that warning, executed |

**One Layer-0 fork noted and dissolved.** `docs/paper-formalization-candidates.md`
7A puts the spinless field in `eps`, the `(Omega^0, ad)` entry; the source pack
`WGS-05` puts it in `Omega^1(ad)`. Both readings place the VEV in the **same
internal carrier**, `ad = Lambda^2(10) = so(6,4)` — "spinless" is a statement
about 4d Lorentz spin, not about the internal index. Every result below is
indifferent to that fork, which is why it was not adjudicated here.

## 2. Preflight — six lenses, each proposing a route

Run inline, before the computation, each required to *propose a route* rather
than comment.

**(a) General relativist / de Sitter specialist.** A cosmological constant is
a *number multiplying the metric in the field equations*, not a field value.
Route: refuse to compare a Lie-algebra element with `Lambda` until a map
`ad -> R` is exhibited. Ask what invariant maps exist. *This lens produced L2
and is the reason the literal reading got typed rather than assumed.*

**(b) Gauge-theory vacuum-energy specialist.** The vacuum energy is `V` at the
VEV, and `V` is not the kinetic form. Route: compute the space of Ad-invariant
polynomials by degree and see what a *stationarity plus minimality* condition
forces without fixing coefficients. *This lens produced L3 — the one result
that survives.*

**(c) Lie-theory Killing-form specialist.** For a Cartan decomposition the
Killing form is definite on each summand and indefinite overall. Route: the
sign question is therefore entirely a question of *which summand the available
VEVs occupy*. Compute the commutant of the SM exactly and locate it. *This
lens produced L1, and closed the "pick a `p` direction and flip the sign"
escape.*

**(d) Effective-potential / naturalness specialist.** Standard SSB gives
`V_min = -m^4/4 lambda < 0`; a Mexican hat always ends below where it started.
Route: check whether that is an accident of the quartic or a theorem. It is a
theorem, and the boundary is degree 4 exactly. *This lens produced the L4
boundary hunt.*

**(e) Source-fidelity reader.** The 2021 Into the Impossible `01:41:43` locator
records that *which fields acquire VEVs and where* is **not** selected by the
source; Portal/Oxford `02:12:34` records that *"a Euclidean-to-Minkowski sign
may be wrong."* Route: any sign claim attributed to GU is a misattribution
before it is a physics error — the source disclaims sign control in its own
voice. *This lens set the claim ceiling and is why no sign prediction is
issued below.*

**(f) Honesty auditor.** "GU predicts the sign of the cosmological constant"
is the most fundable sentence available in this repository and the most
heavily pre-killed (`Q2-FREE`, W211, two process gates). Route: pre-commit to
publishing the negative, and pre-commit to reporting the shift result *with*
the fact that its sign is the wrong one relative to observation. *Honoured.*

**Cheapest kill-or-switch, pre-stated:** if the SM-preserving subspace of `ad`
turns out to contain any `p` direction, the sign is direction-dependent, the
whole route collapses into "it depends on the vacuum", and the switch is to
the availability question instead. *(It does not — `p` has no SM singlet — so
the route ran.)* A second pre-stated kill: if `so(6,4)` admits more than one
invariant bilinear form, the quadratic order carries several free constants
and there is nothing to say. *(It admits exactly one.)*

**Credible contrary route, pre-stated:** GU is not a 4d renormalisable QFT, so
nothing restricts the potential to degree 4. If a degree-6 Ad-invariant
potential can hold an SM-preserving minimum at positive energy, the one
surviving inequality is conditional rather than structural. *This contrary
route WON — see L4.*

## 3. The swing — four exact results

Probe: `tests/channel-swings/joe_directed_lambda_sign_probe.py`, **61/61**,
exits nonzero on any failure (verified: an induced defect produced exit 1).

### L1 — every available direction sits in the negative summand

Building `su(3)` inside `so(6)` through a complex structure and
`su(2)_L`/`su(2)_R` inside `so(4)`, and computing exact commutants over `Q`:

> The commutant of `su(3) (+) su(2)_L` in `so(6,4)` is **4-dimensional**; the
> commutant of the full Standard Model is **exactly 2-dimensional**; both lie
> **entirely inside `k`**; and **`p` carries no SM singlet at all.**

The 2-plane is `span{J6, R1}` — the `B-L` and `T3R` directions — for **every**
hypercharge normalisation `Y = p J6 + q R1` with `q != 0`, swept and verified.
The check is sensitive: dropping the `T3R` part leaves a 4-dimensional
commutant, not 2. This independently re-verifies CB-A row A4's *"exactly two
SM-singlet directions"* in the noncompact real form and claims no novelty for
it; what is new is the **location**.

The Killing Gram on that plane is exactly

    B|_Z = diag(-48, -32),   B(v,v) = -48 a^2 - 32 b^2

negative definite, and negative definite on the whole 4-dimensional
`su(3)+su(2)_L` commutant too. **So the "choose a `p` direction and flip the
sign" escape does not exist, and the sign of any Killing-built quantity is the
same for every available VEV direction.** Combined with the source's own
admission that VEV selection is unselected (2021 ITI `01:41:43`), this is a
real rigidity: *the unselected freedom is harmless for the sign.*

### L2 — one invariant bilinear form, no invariant linear functional

- `[g,g] = g` (bracket span has rank 45, certified mod `p`), so **`so(6,4)`
  admits no nonzero Ad-invariant linear functional.**
- The space of Ad-invariant bilinear forms on `so(6,4)` is **exactly
  1-dimensional**, realised by the Killing form. Certificate: nullity mod
  `p = 1000003` equals 1; since `rank mod p <= rank over Q`, nullity over `Q`
  is at most 1, and the Killing form realises it exactly (checked as an
  integer identity against all 45 generators) and is nondegenerate.

**Consequence 1 — a claim-indexed kill.** The *literal* reading of `SC-COS-01`
— "`Lambda` **is** the VEV" — is **`TYPE-MISSING`**. A gauge-invariant real
number cannot be extracted linearly from an ad-valued VEV, because no
invariant linear functional exists. The claim needs a quadratic-or-higher map,
which is a *potential*, which `SG4` leaves undeclared.

**Consequence 2.** At quadratic order the vacuum energy is `c * B(v,v)` with
exactly **one** undeclared real constant `c`. Its sign is the sign of the
contribution. So the Killing form reduces the quadratic-order freedom to one
bit — and supplies neither that bit nor a reason to prefer either value.

**This is the precise refutation of the route's core idea.** PV-2's Killing
signature governs the *kinetic* form. The vacuum energy is `V`'s *value*. They
share exactly one object — the unique invariant bilinear form — and sharing it
transmits normalisation, not sign.

### L3 — what DOES survive without a potential: the degree-4 sign lock

Not "nothing". Exactly one strict inequality.

`D5` has no Ad-invariant polynomial of degree 1 or 3 (verified by exhausting
Cartan monomials against the even sign changes in `W(D5)`; degrees 2, 4, 5 have
survivors as positive controls, and `tr(X^3) = 0` identically on `so(6,4)` as
an independent cross-check). Hence every Ad-invariant potential of degree `<= 4`
restricted to a ray is exactly `alpha t^2 + beta t^4`, with no odd term. Then:

> **SIGN LOCK.** For **any** Ad-invariant polynomial potential `V` on `ad` with
> `deg V <= 4`, any nonzero VEV `v*` that is a **radial local minimum**
> satisfies
>
>     V(v*) - V(0) = -alpha^2 / (4 beta) < 0    STRICTLY.
>
> Proof chain, verified symbolically: the critical point is
> `t*^2 = -alpha/(2 beta)`; the radial second derivative there is exactly
> `-4 alpha`, so minimality forces `alpha < 0`; positivity of `t*^2` then
> forces `beta > 0`; the value is `-alpha^2/(4 beta)`.

Verified again by exhaustive rational sweep over quartic potentials
`c1 I2 + c2 I2^2 + c3 I4` and every rational direction in the SM-preserving
plane: **zero violations**, with non-minimum critical points present in the
sweep so the minimality hypothesis is doing real work. The two quartic
invariants `I2^2` and `I4` are genuinely independent on that plane
(`I2 = -6a^2-4b^2`, `I4 = 6a^4+4b^4`), so the lock is not an artifact of a
one-parameter family.

Three things this does and does not say:

1. It is **direction-independent** — no dependence on the unselected VEV
   location, and it does not even require SM preservation (it holds on all of
   `ad`); SM preservation is what makes L1's definiteness statement available.
2. It is a **shift**, not a value. A constant is Ad-invariant, so `V(0)` is a
   free bare cosmological constant. Verified explicitly: sweeping a bare
   constant makes the absolute vacuum energy take both signs while the shift
   stays exactly `-3/2`.
3. Its sign is the **wrong one**. Observed `Lambda > 0`. The source's single
   declared spinless channel, at degree `<= 4`, can only push the vacuum energy
   **down** — the anti-de Sitter direction. It cannot be the *source* of a
   positive `Lambda`; at best it deepens a negative one.

### L4 — degree 4 is the exact boundary, and the contrary route wins

The pre-stated contrary route was that nothing forces degree 4. It is correct.

    V6 = -I2 - (1/4) I2^2 - (1/54) I2^3,    I2(x) = tr(x^2)

is Ad-invariant, and at the SM-preserving point `z1 = J6` (with `I2 = -6`):

- along the `z1` ray it is exactly `6t^2 - 9t^4 + 4t^6`, with `t = 1` critical;
- `dV6/ds` vanishes at `s = -6`, so `z1` is a critical point of `V6` on **all**
  of `g`, not merely radially;
- `d^2 V6/ds^2 = +1/6 > 0` there, so the Hessian on `g` is positive
  semidefinite — **no descent direction anywhere**;
- **`V6(z1) = +1 > 0`.**

A positive vacuum energy at an SM-preserving critical point of an Ad-invariant
potential. So `deg <= 4` is load-bearing, not decoration, and the exact
boundary is set by the degree-5 Pfaffian — which the probe confirms is **not**
identically zero on the available plane (`det(eta v) = a^6 b^4`, so
`Pf ~ a^3 b^2`), so the parity argument underpinning the lock provably stops at
degree 4.

## 4. Hostile review of this swing

**Strongest overclaim available, attacked.** *"GU predicts the sign of the
cosmological constant."* It is available in two directions here — "negative,
by the degree-4 lock" and "the Killing form is definite on everything
available, so the sign is fixed" — and **both are false as stated.** The first
is conditional on three declarations GU does not make (degree `<= 4`, the
identification of `Lambda` with `V`'s value, and no other vacuum-energy
contribution) and constrains only a *shift* against a free bare constant. The
second confuses a definite *form* with a definite *functional*: L2 shows the
form is unique up to one real constant whose sign is exactly the missing bit.
Independently, the repository already holds `Q2-FREE` and W211's unanimous
`RESIDUAL-BIT-STANDS` at proof grade; a claim of forcing here would collide
with them, and CC-1 **agrees with them** rather than challenging them.
Independently again, the source disclaims sign control in its own voice
(Portal/Oxford `02:12:34`, *"a Euclidean-to-Minkowski sign may be wrong"*), so
attributing a sign prediction to GU would be a source misattribution before it
was a physics error.

**Strongest contrary construction.** L4, found and executed rather than
imagined: a degree-6 Ad-invariant potential holding an SM-preserving critical
point at `V = +1` with a positive-semidefinite Hessian. It defeats the
generality of L3. Second contrary construction, not defeated and honestly
open: `V(0)` is free, so even at degree `<= 4` the *observed* `Lambda` can be
positive with the eps-channel shift negative, provided a bare term dominates —
which is precisely the freedom the repository's own
`mission_a_lambda_dark_energy_provenance_audit.py` names
`bare_Lambda_inserted_as_source_derivation`.

**Strongest mistyping risk.** `ad = Lambda^2(10) = so(6,4)` with internal
signature `(6,4)` is inherited from the repository (`Y14 = Met(X4)`,
DeWitt/Frobenius), not established here. If the internal signature were
different, `k` would be a different maximal compact and L1's *location* claim
would have to be recomputed — although L3 and L4 are signature-independent,
since they use only that `so(10, C)` has no degree-1 or degree-3 invariant.
Second mistyping risk: "SM-preserving" is imposed as *commuting with the SM
generators*; if GU's physical SM is embedded differently in `so(6,4)` than the
Pati-Salam chain PV-2 uses, L1's 2-plane changes. The probe reduces this
exposure by proving the result for **every** hypercharge normalisation rather
than one.

**Weakest reproducibility/propagation seam.** The uniqueness of the invariant
bilinear form (L2) is the only step that is not a direct rational
computation — it uses one finite-field rank certificate. The error direction is
stated and safe (`rank mod p <= rank over Q`, so `nullity mod p = 1` bounds
`nullity over Q` by 1) and the Killing form is exhibited over `Z` to realise
the remaining dimension, so the conclusion is exact. But a reader who
mis-recalls the inequality direction would read it as heuristic. Second seam:
the no-degree-1/3-invariant step (L3) uses the Chevalley restriction theorem
as a cited result, with the Weyl-monomial exhaustion done exactly; the cited
step is standard but is a citation, not a computation.

## 5. Classification, in target-native vocabulary

| object | verdict |
|---|---|
| **Route:** "the Killing signature of GU's gauge algebra fixes `sign(Lambda)`" | **ROUTE KILLED.** Exactly one invariant bilinear form and no invariant linear functional; the form transmits normalisation, not sign |
| **Candidate:** literal reading of `SC-COS-01`, `Lambda` **=** the spinless VEV | **CANDIDATE KILLED / TYPE-MISSING.** No Ad-invariant linear functional on `so(6,4)` exists, so the stated identity does not define a gauge-invariant real number |
| **Candidate:** scale reading, `Lambda = V(<eps>)` at degree `<= 4` | **NOT-YET-FALSIFIED, and it delivers the wrong sign.** Shift strictly negative, direction-independent, against an observed `Lambda > 0` |
| **Candidate:** scale reading with `deg V >= 6` | **NOT-YET-FALSIFIED, sign free.** Explicit positive-energy SM-preserving minimum exhibited (L4) |
| The potential `V`, its degree, and `V(0)` | **SOURCE-SILENT.** `SG4` is the open decider (`canon/gu-forces-field-space-declaration-RESULTS.md`); 2021 ITI `01:41:43` records that VEV selection is not source-selected |
| Absolute `sign(Lambda)` in GU | **unchanged: `Q2-FREE`.** CC-1 independently corroborates the standing verdict from the gauge-algebra side; it does not move it |
| Lambda **magnitude** | untouched; `PRED-NORM-RANK = RESOLVED_NO_GO` stands |

## 6. Claim ceiling

**This is not a prediction of `sign(Lambda)`, and it is not a derivation of
dark energy.** It is a statement about how much sign information the declared
algebra can carry, and the answer is: **one strict inequality on a shift, at
degree `<= 4`, and nothing about the absolute value.**

Not established, and deliberately not attempted: any movement of the `Q2-FREE`
verdict; any statement about the observation/section mechanism, which is how
GU actually breaks and which PV-2 shows reaches only `p`; any statement about
`SG4`'s undeclared completion; any Lambda magnitude; any claim about the
*fermion-mass* leg beyond MJ-4's, which is not re-derived; and any comparison
with a cosmological dataset. The internal signature `(6,4)` and the identity
`ad = Lambda^2(10)` are inherited from the repository, not re-established.

## 7. Composed standing of the source's three-way link

With MJ-4 and CC-1 side by side, `SC-MAS-03`'s three-way link now has both
non-cosmological legs typed:

- **fermion-mass leg:** killed exactly under the direct reading (MJ-4 — the 45
  is absent from `16 (x) 16`); the scale reading is untouched.
- **Lambda leg:** the literal reading is type-missing; the scale reading
  survives but, at degree `<= 4`, can only move the vacuum energy in the
  direction *opposite* to the observed sign.

Neither leg is closed at the scale reading, and that is the same unbuilt
object in both cases: the zero-order operator that turns a spinless
gauge-potential VEV into a scale. **That operator, not the algebra, is where
this link lives or dies.**

## 8. Next in-channel gate

**CC-2 — does GU's actual breaking mechanism even reach this sector?** PV-2
established that observation reduces `Spin(6,4)` to its maximal compact and
therefore addresses only the 24 directions of `p`. L1 establishes that every
SM-preserving spinless VEV lies in `k`. So the two mechanisms are disjoint on
this sector, and the honest next question is whether a spinless `eps` VEV is
*dynamically available at all* once the section is chosen — i.e. whether the
observation mechanism leaves the `k`-valued spinless channel free or freezes
it. A negative there would make the entire cosmological channel vacuous in
GU-as-declared, which would be a stronger result than anything above.

Selection stays inside this channel. Repository-wide GU priority is unchanged,
the superposition / source-residual workstream is untouched, and no ledger,
canon, or current-state surface moves.
