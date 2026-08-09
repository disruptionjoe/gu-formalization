---
title: "Y14 / X4 systems spec sheet: substrate, projection, and section, specified in distributed-systems vocabulary"
doc_type: orientation
status: baseline
created: 2026-08-09
version: "1.0"
version_policy: |
  1.0 is the FROZEN BASELINE. It is not the best version of this document -- it is the first one, saved
  deliberately so later changes are diffable rather than silent.
  - PATCH (1.0.x): typo, formatting, source-path correction. No content change.
  - MINOR (1.x): add or correct a field; fold a defect fix. Body changes, conclusions do not.
  - MAJOR (x.0): the document says something different than it did. Requires a CHANGELOG rationale.
  Every version appends to the CHANGELOG at the foot of this file. Nothing is edited silently.
known_issues: "See companion issue register (75 items, S1-S4). 1.0 ships with all of them open, by design."
grade: "ORIENTATION DOCUMENT. Produces NO new claim, changes NO verdict, promotes NOTHING. Every field is
  graded [MATH] (quoted from canon/computed source), [ANALOGY] (systems framing, zero physics content), or
  [UNSPECIFIED] (genuinely not determined by the construction). The systems vocabulary is a lens for
  legibility and must never be cited as a result."
layer0_note: "Written under the AGENTS.md Layer-0 precondition. The recurring failure it names -- reading a
  MULTIPLICITY or DECOMPOSITION result as a COUNT result -- is explicitly avoided: this document asserts no
  count anywhere, and Sec 9.3 states the count is not a field in this schema."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
follows:
  - canon/w2-y14-spin-structure.md
  - canon/shiab-existence-cl95.md
  - canon/no-go-class-relative-map.md
  - canon/h2-base-index-chirality.md
  - canon/function-space-index-conservation-RESULTS.md
  - canon/single-decider-integer-index-RESULTS.md
  - canon/schwarzschild-weak-field-rfail.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
raises:
  - "D8 (Met(X4) contractibility type error, canon/no-go-class-relative-map.md) -- filed separately"
  - "D9 (stale CP2 scope tag, same file) -- filed separately"
---

# SPEC: `Y14` / `X4` — substrate, projection, and section

**Audience.** Anyone who needs the shape of the `Y14`/`X4` construction without reading differential
geometry first, and anyone who needs to know which parts of it are determined.

---

## Sec 0 Scope and epistemic status

This models a differential-geometric construction as a distributed system. **That is a lens, not a claim.**
Where this document writes "replica," the underlying object is a section of a fiber bundle, and no physics
follows from the vocabulary.

Every field is graded:

- **`[MATH]`** — computed or proved in the source material, quoted as given
- **`[ANALOGY]`** — systems framing; load-bearing for intuition and nothing else
- **`[UNSPECIFIED]`** — genuinely not determined by the construction

A spec whose unknowns are not marked is a lie. Roughly a third of this document is `UNSPECIFIED`, and that
is the most important thing it communicates.

**Standing hazard.** Per `GEOMETER-VS-PHYSICS-OBJECTS.md`, many objects here have both a standard-physics
construction and a program-native geometric one under the same name. This document names which it is using
wherever the fork is live. Defaulting silently to either side is the failure mode, and Sec 8 D8 records an
instance found in canon during this pass.

---

## Sec 1 System overview

Two spaces and two maps.

`Y14` is a 14-dimensional total space. `X4` is a 4-dimensional space. `Y14` is built *out of* `X4` — it is
the bundle of pointwise **Lorentzian** metrics on `X4`, so a point of `Y14` is a point of `X4` **together
with a choice of how to measure at that point**. `[MATH]`

The relationship is **not** client/server, and that reading must be killed early because it is the obvious
one and it is wrong in a specific way (Sec 3.4). `X4` embeds *into* `Y14` as a submanifold. The observable
world is not a remote view of the substrate — **it is a slice through it**, and the physics comes from how
that slice bends. `[MATH]`

One line: **`Y14` is the state space, `X4` is a section through it, and everything measurable is a property
of the section rather than of the state space.**

**`Y14` is open.** The Lorentzian signature condition is *open* in `Sym^2(T*X4)`, therefore **standard
compact index theorems do not apply.** Every index-theoretic argument in this system inherits this. `[MATH]`

---

## Sec 2 Object inventory

### 2.1 `X4` — the base

| field | value | grade |
|---|---|---|
| type | smooth, oriented 4-manifold | `[MATH]` |
| dimension | 4 | `[MATH]` |
| signature | `(3,1)` [K95 fork] / `(1,3)` [K77, settled for the chimeric metric] | `[MATH]`, fork live |
| compactness | **`[UNSPECIFIED]`** — not fixed by the construction | |
| **spin** | **standing PRECONDITION, not a free structure choice** (W2-FC1). `CP^2` is **excluded** (non-spin). | `[MATH]` |
| spin-c escape | closed: `Y14` is spin-c for any orientable `X4` (`W3(Y14)=pi*W3(X4)=0`), **but** the `U(1)` twist `S (x)_C L^{1/2}` breaks H-linearity and shifts the index off `Ahat(K3)=2`. **Spin-c does not suffice.** | `[MATH]` |

> **Note.** `X4 in K3` is a **local working hypothesis** of specific entries (Freed-Hopkins Option-B; the
> Distler-Garibaldi GU-Chir block), never a global base assumption. Do not import it silently.

### 2.2 `Y14` — the substrate

| field | value | grade |
|---|---|---|
| construction | `Y14 = Met(X4)`, **total** 14-dim space; **not** selected by an exterior dimension count | `[MATH]` |
| dimension | 14 = 4 (base) + 10 (fiber `Sym^2(T*_x X4)`) | `[MATH]` |
| fiber | `GL(4,R)/O(3,1)`, **non-compact**, homotopy type **`RP^3 x R^+`** | `[MATH]` |
| fiber derivation | Gram-Schmidt + Cartan: `F ~= O(4)/(O(3) x O(1)) ~= S^3/Z2 = RP^3`; `RP^3 ~= SO(3)`, parallelizable, `w(RP^3)=1` | `[MATH]` |
| fiber signature | Frobenius `(7,3)`, trace-reversed to `(6,4)` | `[MATH]` |
| ambient signature | `(9,5)` [K95] or `(7,7)` [K77] | `[MATH]`, fork open |
| compactness | **open / noncompact** (see Sec 1) | `[MATH]` |
| ends | **fiber ends, not a boundary.** End is **limit-point / essentially self-adjoint**: **the domain is UNIQUE and FORCED** | `[MATH]` |
| `w1` | `w1(Y14) = 0`, unconditional | `[MATH]` |
| `w2` | `w2(Y14) = pi*w2(X4)` — spin **iff** `X4` spin | `[MATH]` |

> **Correction inherited.** The earlier *unconditional* spin claim was **retracted** (W2-01): the Step 3
> assembly dropped a `w2(V)` term. Independent check: `w2(Sym^2 E) = w1(E)^2` for any rank-4 `E`, so the
> vertical bundle contributes **no** `w2` and the base obstruction survives.

> **Do not let this slide.** Total dimension 14 is **not** selected by an exterior-grading count. The
> `Lambda^1 + Lambda^2 + Lambda^3` reading over a 4-base totals **18**, and there is no natural
> `GL(4)`-equivariant isomorphism `S^2 V* ~= Lambda^2 V* + Lambda^3 V*`. **Two different objects have been
> called "the 14."** Type them separately or coefficients will cross a fork.

### 2.3 Representation layer

| field | value | grade |
|---|---|---|
| Clifford type | `(9-5) mod 8 = 4` => quaternionic => `Cl(9,5) ~= M(64,H)`; `(7,7)` fork gives `M(128,R)`, real | `[MATH]` |
| irreducible module | `S = H^64`, `dim_R = 256`, complex dim `128 = 2^7` | `[MATH]` |
| matter module | `V (x) S`, dim `1792 = 2^8 * 7` | `[MATH]` |
| RS sector | `ker Gamma = 13*128 = 1664 = 2^7 * 13`, signature-independent across all nine signatures | `[MATH]` |
| internal arena | `Sp(32,32;H)` — non-compact real form; **the non-compactness IS the Krein form**, one datum | `[MATH]` |

### 2.4 Cohomology

| field | value | grade |
|---|---|---|
| Serre SS (trivial monodromy) | `H^2(Y14; Z/2) ~= Z/2 + H^1(X4; Z/2) + H^2(X4; Z/2)` | `[MATH]` |
| fiber | `H^2(RP^3; Z) = Z_2` — 2-torsion | `[MATH]` |
| families index over fiber | valued in `Z_2`; **3-free** | `[MATH]` |
| RS boundary eta | on `RP^3 = L(2;1)`, **2-primary** | `[MATH]` |
| bulk characteristic number | `ch2(S_X)[K3] = -5376 = -2^8 * 3 * 7` | `[MATH]` |

> **Read the last row carefully.** `-5376` is **a bulk characteristic number, not yet THE families index** —
> the pushforward over the non-convex `GL(4,R)/O(3,1)` fiber is unbuilt (Sec 9.6). It **is** divisible by 3,
> hence `= 0 mod 3`, which is the **failing** condition: the bar requires `N != 0 mod 3`.

---

## Sec 3 Interfaces

### 3.1 `pi : Y14 -> X4` — projection (the read)
Forgets the metric, keeps the point. Total, surjective, well-defined. No issues. `[MATH]`

### 3.2 `sigma : X4 -> Y14` — section (the write, and the problem)
Assigns each point of `X4` a Lorentzian metric `g(x)`, one point per fiber.
**Contract:** `pi . sigma = id_X4`. Pullbacks: `g_s = s*(G)`, `s*(theta) = II_s`. `[MATH]`

> ### Sec 3.2.1 The contract is weaker than it looks
>
> `pi . sigma = id` guarantees the round-trip. **It does not guarantee `sigma` is unique, and `sigma` is not
> unique.** `[MATH]`
>
> In storage terms: a materialized view with a **non-deterministic refresh**. The view round-trips, so it is
> *consistent*, but the substrate does not determine the view and the view does not determine the substrate.
> **The read path is not a pure function of stored state.** `[ANALOGY]`
>
> **The obstruction is named and computable.** Under `C -> -C` the even/breaking subspaces exchange
> (`58 <-> 78`), giving **a nontrivial holonomy class `w != 0` in `H^1(F; Z/2)` with no global section.**
> `[MATH]` This is a specific `Z/2` class, not a vague under-determination — it is falsifiable and it is the
> right object to attack.

### 3.3 `Phi` — SHIAB operator (lossy transport)

`Phi : Omega^2(Y14) (x) S -> Omega^1(Y14) (x) S`. `[MATH]`

| property | value |
|---|---|
| input width | `dim(Lambda^2 V (x) S) = 91 * dim(S)` |
| output width | `dim(V (x) S) = 14 * dim(S)` |
| compression ratio | **6.5 : 1** |
| injective? | **provably not** — `91 > 14` |
| existence | proved: one natural real-linear `Spin(9,5)`-equivariant Clifford contraction |
| uniqueness | **RESOLVED-NEGATIVE.** Real family dim 16 -> 8 (J-commutation) -> 4 (full `Sp(64)`-equivariance). The written operator is **one point in a 4-dim space; residual freedom 3.** |

> **A lossy codec with a 4-parameter configuration and no selection rule.** Existence was proved;
> injectivity, rank, kernel and uniqueness were **not** in that proof, and the source says so. Treating
> `Phi` as "the" operator silently pins three free parameters.

### 3.4 Where the systems analogy breaks — read before reusing it

`X4` is an **embedded submanifold** of `Y14`, not a remote peer. There is **no transport, no latency, no
serialization, and no network partition in the transport sense.** The partition in this system is in the
*observer-overlap structure*, not in a link. `[MATH]` + `[ANALOGY]`

**Any conclusion that depends on messages taking time is invalid here.**

---

## Sec 4 State, units, and clocks

### 4.1 Two metrics, and conflating them is the classic bug
A base metric on `X4` and a fiber metric-on-metrics (DeWitt/gimmel) on `Y14`, related by an action.
**Different objects, same name.** `[MATH]`

### 4.2 No absolute scale — the system has no wall clock
`mu_DW` is **structurally free, not merely unmeasured**. The scale-covariant geometry fixes only
**dimensionless ratios**; the magnitude is not determined (H24/H25: ratios geometric, magnitude free).
`[MATH]`

> Cleanest systems statement: **this system has logical time, not physical time.** Ratios are ordering
> relations; the magnitude is the missing NTP. Do not expect the geometry to hand you `mu_DW` — it is not
> underspecified in the documentation, it is underspecified in the object. `[ANALOGY]`

### 4.3 No norm on state — only signed pairings
The invariant form is **Krein** (indefinite), not positive-definite. Ghosts are **kept and graded** via
`[P,S] = 0` (`P` = Cartan involution), not removed. This is anti-SUSY: consistency is Krein-graded, not a
positive Hilbert space. `[MATH]`

> **Underappreciated consequence.** You cannot ask "how far apart are these two states." There is no
> positive-definite metric on state, so **distance is not a well-formed query** — only signed pairings are.
> Therefore **you cannot state a convergence criterion.** "Eventually consistent" presupposes a norm in
> which divergence shrinks, and there is none. Any consistency claim about this system must be phrased in
> terms the Krein form can express, or it is not a claim. `[ANALOGY]`

---

## Sec 5 Consistency model

**Classification: AP.** Not by preference — by theorem. `[MATH]` for components, `[ANALOGY]` for the label.

| guarantee | status |
|---|---|
| global **operator** (strong consistency) | **does not exist** |
| global **class** (interface-class descent) | **exists** |
| global **section** | **does not exist** — obstruction is `w != 0` in `H^1(F; Z/2)` |
| genuine partition (overlapping observers disagree) | **present** |

The precise canon statement is: **"a global CLASS exists while no global OPERATOR does"** (W107/W110).
`[MATH]`

> **Citation hazard, recorded.** An earlier draft of this spec attributed operator non-gluing to W94/W98.
> Those are the **Krein/modular observer** waves, not section statements, and **W94's sectorial-closure
> result is retracted** (`VERIFICATION.md`). The AP conclusion survives; the supporting object is
> W107/W110 for class descent and the `H^1(F;Z/2)` holonomy class for sections.

**Tiering** (`[ANALOGY]` framing over `[MATH]` objects): *individual* = per-observer operator content, does
not glue. *Regional* = interface-class content across overlapping observers, descends. *Global* =
section-independent ambient invariants.

---

## Sec 6 Write path — dynamics

The reconciliation equation is the **Gauss identity**, which holds as a tautology for any section:

```
G^X = G^Y_T + Q(B) + E^Psi
```

`G^X` = 4D Einstein tensor on the induced metric `g_s = s*(g)`; `G^Y_T` = tangential projection of the 14D
Einstein tensor; `Q(B)` = extrinsic stress, **quadratic** in the second fundamental form `B = II_s`;
`E^Psi` = gauge-curvature contribution. `[MATH]`

Plain reading: **observable 4D physics = 14D physics restricted to the slice, plus corrections measuring how
the slice bends.**

The gravitational action is `|II|^2`, the full second-fundamental-form norm of the embedding, via
`|II|^2 = |H|^2 - R^X`. **Einstein-Hilbert is induced, not added.** `[MATH]`

> Not a free Lagrangian choice, and it matters: pure conformal `|H|^2` dies against rotation curves, while
> the induced `|II|^2` survives (H49). The dynamics are constrained by the embedding rather than selected by
> the modeler.

---

## Sec 7 Invariants (MUST hold)

1. `pi . sigma = id_X4` — the round-trip. `[MATH]`
2. `dim ker Gamma = 1664` — structural for **any** signature; `Gamma` surjective since every `gamma^a` is invertible. `[MATH]`
3. Krein signature on the generation sector `(+96, -96, 0)`, both chirality halves **totally null** (`~1.8e-14`). `[MATH]`
4. Net chiral asymmetry `= 0` at representation-theory level, all signatures. `[MATH]`
5. `w1(Y14) = 0`; `w2(Y14) = pi*w2(X4)`. `[MATH]`
6. Ghost parity commutes with dynamics: `[P, S] = 0`. `[MATH]` **as a requirement**; not verified for the constructed action.

---

## Sec 8 Known defects

| # | defect | severity |
|---|---|---|
| D1 | `sigma` non-unique — read path not a pure function of state; obstruction `w != 0` in `H^1(F;Z/2)` | **critical, structural** |
| D2 | `Phi` has 3 residual free parameters and no selection rule | **critical** |
| D3 | Two objects named "the 14" (metric total space vs exterior grading; 14 vs 18) | high — type confusion |
| D4 | Two metrics both called "the metric" | high — type confusion |
| D5 | Signature fork `(9,5)`/`(7,7)` open; **any complexified computation is provably incapable of deciding it** — both complexify to `M(128,C)` | high |
| D6 | No declared wire format for signature pairs `(p,q)` vs `(q,p)` | medium — a real bug survived four days on this |
| D7 | Spin structure conditional on `X4`; prior unconditional claim retracted | medium |
| **D8** | **`Met(X4)` asserted contractible in one canon entry, non-contractible in another** | **high — filed separately** |
| **D9** | **Stale scope tag: same file claims Sec 2.1 admits `CP^2`; Sec 2.1 excludes it** | **low — filed separately** |

---

## Sec 9 `[UNSPECIFIED]` — the gap list

**9.1 The selector.** Nothing determines *which* `sigma` is realized. The constructed candidate source
action **exists as a well-defined algebraic object and performed none of the three jobs it was built for.**

**9.2 The boundary object.** The sequencer that would restore global consistency. Named, required by Sec 5,
not built.

**9.3 The count.** The number of matter generations is **not a field in this schema.** Interior contribution
provably even; observed count odd; therefore supplied externally. A foreign key into a registry this system
cannot read. `[MATH]`

**9.4 The scale `mu_DW`.** Structurally free (Sec 4.2). Not a TODO — a property.

**9.5 The APS/end condition.** The end **domain** is unique and forced (Sec 2.2), but the **index** question
is open: on noncompact ends an APS eta/end term **can supply an unpaired chiral contribution**. The full
function-space RS APS + family-index statement is not closed.

**9.6 The families pushforward — the single decider.** The pushforward over the **non-convex**
`GL(4,R)/O(3,1)` fiber is unbuilt. This is the named single-decider computation, and it is why `-5376`
remains a bulk number rather than an index.

---

## Sec 10 Non-goals

- **Not** a positive Hilbert space. Consistency is Krein-graded; do not look for SUSY-style positivity.
- **Not** a closed system. The primary working hypothesis is termination at an interface, and Sec 9 is that
  hypothesis' fingerprint pattern.
- **Not** scale-fixed (Sec 4.2).
- **Not** a derivation of the generation count (Sec 9.3), under any current assumption.
- **Not** a source of citable results. Every `[ANALOGY]` row is framing with zero physics content.

---

## Reviewer's summary

**The state model is exceptionally well-specified.** Dimensions, signatures, algebra type, kernel size,
cohomology, end domain, and the section obstruction are all pinned — several to machine precision, several
stable across the open signature fork. This is a well-typed object.

**The control plane is absent.** Not thin — absent. No selector (9.1), no sequencer (9.2), and the count is
a dangling foreign key (9.3). The read path is not a pure function of state (D1) and the primary transport
is a lossy codec with three unpinned parameters (D2).

**On why it is absent.** The tempting read is unfinished engineering. The better-supported read, after this
pass, is harder: `Y14` is **open**, so compact index theorems do not apply, and the one computation that
would decide the count is a pushforward over a **non-convex** fiber that nobody has built. That is a genuine
analysis problem sitting behind a topological obstruction, not a backlog item.

**Cheapest wins, ranked:** D9 (stale cross-reference, mechanical), D8 (type the two `Met(X4)`s and re-run
the affected elimination), D6 (declare a wire format for signature pairs). None requires an object nobody
has.

---

## Correction record

Kept per house discipline; corrections are folded into the body above and recorded here.

- **E1 (2026-08-09).** Sec 2.2 ends/boundary was filed `[UNSPECIFIED]`. **Corrected:** end is limit-point /
  essentially self-adjoint, **domain UNIQUE and FORCED**. Correction in the system's favor. Index question
  remains open (9.5).
- **E2.** Sec 2.2 fiber understated as "homotopy equivalent to `RP^3`." **Corrected:** non-compact, homotopy
  type `RP^3 x R^+`. The non-compactness is how this datum violates Witten's assumption (1).
- **E3.** `Y14` openness promoted from a table row to Sec 1; compact index theorems do not apply.
- **E4.** Sec 2.1 spin filed as "conditional." **Corrected:** `X4` spin is a standing **precondition**;
  `CP^2` **excluded**; spin-c does not suffice.
- **E5.** Sec 5 cited W94/W98 for operator non-gluing. **Corrected:** those are Krein/modular observer waves,
  **W94's sectorial-closure result is retracted**; the correct objects are W107/W110 (class descent) and the
  `H^1(F;Z/2)` holonomy class (no global section). Conclusion unchanged, support replaced.

---

## CHANGELOG

Every version appends here. Nothing is edited silently.

### 1.0 — 2026-08-09 — frozen baseline
First saved version. Establishes the object inventory (Sec 2), interfaces (Sec 3), state/units/clocks
(Sec 4), consistency model (Sec 5), dynamics (Sec 6), invariants (Sec 7), defect list (Sec 8) and the
`[UNSPECIFIED]` gap list (Sec 9).

Folded before freezing: errata E1-E5 (see Correction record above), raised during a structural-inventory
pass against canon on the same day.

**Ships with 75 known issues open, by design** — see the companion issue register. 1.0 is not the best
version of this document; it is the first one, saved deliberately so every later change is diffable rather
than silent.

Known at freeze time and deferred to later versions:
- the mirror-pair doubling is not modelled (register 12, S1) — MAJOR, lands in 2.0
- the selector is typed as a missing function rather than a `Z2` parity per pair (register 14, S2) — MAJOR, lands in 2.0
- `[ANALOGY]` content is not visually separated from `[MATH]` content (register 6, S1) — MINOR, lands in 1.1
- no staleness/version contract with source files (register 8/17, S1) — MINOR, lands in 1.1
