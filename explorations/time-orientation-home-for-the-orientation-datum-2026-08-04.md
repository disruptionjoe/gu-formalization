---
artifact_type: exploration
status: exploration
doc_type: deciding-check
created: 2026-08-04
work_item: DC-H1-FOLLOW-ON
title: "DC-H1 follow-on: the orientation datum's home IS a time-orientation of the Lorentzian base, and NOTHING in GU fixes it. CARRIER (exact): the DeWitt loop is a path of Lorentzian metrics on ONE fixed tangent space that returns the SAME metric with the future and past cones exchanged (closed form, no Clifford input); and the orientation character factors over the fourteen gimmel legs as chi = chi_base * chi_fibre with chi_fibre == +1 identically and chi_base == the orthochronous character, exhaustively over O(3,1). The Sym^2 metric-fibre legs contribute NOTHING, for an exhibited parity reason (the only flippable chi=-1 fibre legs are the three purely spatial off-diagonals and they flip in count k(3-k), always even) that is specific to three spatial dimensions. So the datum is a time-orientation of the tautological timelike LINE of X^4 -- not of F, not of Y^14. BUT its nontriviality is FIBREWISE: the loop lies inside one fibre, so the class is not in the image of H^1(X^4;Z/2), and no base-side supply can cancel it. FIXED-vs-PRESUPPOSED: all seven real candidates PRESUPPOSE. W166's record-count mode and the Friedmann first equation are exactly T-EVEN (T exchanges the growing and decaying branches); record accretion and the causal-order route are T-odd only because they import the past cone; CH-REC already types its eps as an import. LAYER-0 PAYLOAD, new: the program's three structures carry three DIFFERENT characters -- sigma_J(J_obs) = det = SPACETIME orientation, sigma_K(K_S = e_0..e_8) = det*orth = SPACE orientation, chi(C_perp = K J_obs) = orth = TIME orientation, with chi = sigma_K * sigma_J -- so any weld of 'the arrow' to a Krein sign must name WHICH. Ledger: UNCHANGED in count; the datum is RELOCATED and BETTER TYPED."
grade: "EXACT throughout, in tests/dc-h1/time_orientation_home_probe.py: 52 hard checks, five preregistered kill conditions, five firing negative controls, exits nonzero on any failure. Part 1 is Fraction arithmetic (the DeWitt supermetric); Part 2 is closed-form sympy with NO Clifford/Krein/coflip/packet input at all; Parts 3-5 are Gaussian-integer Cl(9,5) linear algebra plus integer combinatorics; Part 6 is exact sympy T-parity plus integer bookkeeping over a declared, existence-checked ledger. CITED, not re-derived: DC-H1's identification of chi as the orthochronous character and the reduction of the ten relative phases to one common phase. HARDENED here, not merely cited: DC-H1 ASSERTED the fibre frame's (6,4) signature; this investigation DERIVES it (exact orthogonality, exact norms, and the lambda > 1/4 dependence). NOT established: any transfer of the loop from the metric fibre F to the 13-dim link L^13; any packet field, phase, Green form, domain, or operator; any movement of the count; any identification of this Z/2 with TaF's finality direction."
prereg: explorations/atlas-derived-external-datum-hypotheses-2026-08-04.md
probe: tests/dc-h1/time_orientation_home_probe.py
kill_conditions_declared_before_computation: "K1-K5 declared in the probe docstring before the probe body was written; the outcome space for parts (1) and (2) was fixed from the task statement and the artifacts before any computation. NOT BLIND, stated honestly: reconnaissance values for chi_fibre and the three characters were in hand before this note was drafted. The probe re-derives every load-bearing number independently and fails closed."
depends_on:
  - lab/process/CURRENT-RESEARCH-CONTEXT.md
  - explorations/dc-h1-orbit-signs-monodromy-check-2026-08-04.md
  - explorations/atlas-derived-external-datum-hypotheses-2026-08-04.md
  - explorations/b5-chirality-orientation-audit-2026-07-29.md
  - explorations/external-datum-ledger-and-the-2plus1-product-rule-2026-07-29.md
  - canon/boundary-einvariant-and-the-tangential-fork.md
  - explorations/W166-lens-tachyon-is-the-engine-2026-07-14.md
  - explorations/channel-swing-CH-REC-2026-07-19.md
  - explorations/wave-swing2-the-bit-2026-07-21.md
  - explorations/W151-gr-and-c-emergence-from-records-2026-07-14.md
  - explorations/W154-reverse-engineered-source-action-2026-07-14.md
  - canon/theta-field-flrw-dark-energy-eos.md
  - explorations/mh7-dim13-restatement-2026-08-03.md
  - docs/paper-formalization-candidates.md
deposit: "pre-deposit; any decisive downstream use is J5-gated"
construction: "program-native throughout per GEOMETER-VS-PHYSICS-OBJECTS.md: the actual DeWitt metric fibre GL(4,R)/O(3,1), the DeWitt supermetric on Sym^2(T*X^4), the program-native Krein-dual coflip C_perp = K J_obs with K = K_S = e_0...e_8, and the certified B5 objects by citation. No positive-Hilbert substitution."
canon_verdict_change: none
outcome: "CARRIER = TIME-ORIENTATION OF THE LORENTZIAN BASE (exact); FIXED-vs-PRESUPPOSED = ALL PRESUPPOSE; LEDGER UNCHANGED, DATUM RELOCATED"
---

# Whose time-orientation is it? — the home of GU's orientation datum

**Preregistered outcome space, fixed before computing:** (1) the carrier is
one of {`X^4`, `F`, `Y^14`, a joint object}; (2) the datum is either ALREADY
FIXED by some GU object — in which case the ledger REDUCES — or merely
PRESUPPOSED by all of them, in which case the ledger is unchanged and the
datum is relocated. **Landed:** (1) `X^4`, with a fibrewise twist that neither
of the three simple answers anticipated; (2) all PRESUPPOSE. **The ledger does
not reduce. No promotion.**

Honest provenance note, because the program cares: the reconnaissance
computations that produced §2's numbers were run before this note was drafted,
so the *values* are not blind. What was fixed in advance is the outcome space,
the deciding rule of §3, and the probe's five kill conditions. The probe
re-derives every load-bearing number with hard asserts and fails closed.

---

## 1. What DC-H1 handed forward

DC-H1 (`explorations/dc-h1-orbit-signs-monodromy-check-2026-08-04.md`)
established, exactly:

- the six B5 chirality-orbit relative signs are a **holonomy of a path class**,
  not a stored value;
- the class is moved by the generator of `pi_1(F) = Z/2`, `F = GL(4,R)/O(3,1)`;
- the `Z/2` that fires is the **orthochronous character** of `O(3,1)` — a
  *reflection* `Z/2`, not the spin double cover; the framing route dies through
  the **zero homomorphism**;
- ledger unchanged.

It then named its own cheapest new question, which this note answers: *if the
`Z/2` is the time-orientation character, what is it a time-orientation OF, and
does GU already supply one?*

DC-H1's scope caveat is inherited unchanged and is **not** papered over: the
loop lives in the metric fibre `F`, and transfer to the 13-dim link `L^13` is
hostage to M-H7 gaps O2/O3 (`explorations/mh7-dim13-restatement-2026-08-03.md`
§5 loss 1). Nothing below closes that gap, and §2.6 states exactly which of the
results survive it and which do not.

---

## 2. Part (1) — TYPING: the carrier

### 2.1 The loop, in closed form, with no Clifford algebra at all

This is the load-bearing paragraph, and it uses none of the program's
conventions. Let `B_t` be rotation by `pi t` in the `(x_0, x_3)` plane and
`h_t = B_t^T eta B_t` the DeWitt loop's metric. Set

```text
v_t = (sin(pi t), 0, 0, cos(pi t)).
```

Then, symbolically and exactly (probe Part 2):

```text
B_t^T B_t = I            (so the base point never moves: the loop lies in ONE fibre)
h_t v_t   = -v_t         (v_t is the continuous h_t-timelike eigendirection)
h_t(v_t, v_t) = -1       IDENTICALLY in t          [kill condition K4]
h_1 = h_0 = eta          (the loop closes on the same metric)
v_1 = -v_0               (the ray reverses; the LINE returns)
v_2 = v_0                (order 2)
```

In words: **the DeWitt loop is a path in the space of Lorentzian metrics on a
single fixed tangent space which returns the SAME metric with the future and
past cones EXCHANGED.** That is the entire typing, and it holds independently
of every Clifford, Krein, coflip, packet, signature and normalization
convention in the program. It also reproduces canon
`boundary-einvariant-and-the-tangential-fork.md` §7 constructively: the retract
`F -> RP^3` is `h |-> its timelike line`, `RP^3` is the space of *unoriented*
timelike lines, and the `Z_2` canon names as "the `O(1)` Lorentz
time-reflection" is exactly the choice of a *ray* within that line.

### 2.2 The fibre frame, earned rather than asserted

DC-H1 hardcoded `FIBRE_SIGNATURE = [1]*6 + [-1]*4` for its ten DeWitt columns.
This investigation derives it (probe Part 1, exact `Fraction` arithmetic). With the
DeWitt supermetric

```text
G(E,F) = tr(eta E eta F) - lambda tr(eta E) tr(eta F),
```

the ten columns are **exactly `G`-orthogonal** with norms

```text
+2, +6, +12, +2, +2, +2 | -12, -2, -2, -2      (lambda = 1)
```

i.e. signature `(6,4)`, and the four negative legs are **named**: the
conformal/trace mode (column 6 *is* `eta` itself) and the three space-time
off-diagonals `E_(i,3)`. Columns 0,1,2 are `eta`-traceless diagonal modes. The
split is not free: at `lambda = 1/4` the trace leg is **null**, and at
`lambda = 0` it is positive, so `(6,4)` requires `lambda > 1/4`. This closes a
small assertion in DC-H1's instrument and makes the leg bookkeeping below
non-arbitrary.

### 2.3 The carrier split: the metric fibre contributes NOTHING

The orientation character `chi` of `C_perp = K J_obs` is a homomorphism, so it
factors over the flipped legs of any diagonal `Lambda in O(3,1)` as
`chi = chi_base * chi_fibre`. Exhaustively over all sixteen diagonal elements
(probe Part 3):

```text
chi_fibre(Lambda) = +1      for EVERY Lambda            [kill condition K1]
chi_base(Lambda)  = orth(Lambda)                        (the orthochronous character)
chi(Lambda)       = orth(Lambda)
```

All four `pi_0(O(3,1))` components are represented among the sixteen (K2), and
`chi_base`, `chi_fibre` are each continuous homomorphisms into a discrete
group, so they factor through `pi_0` and the sixteen-element check is
**exhaustive over all of `O(3,1)`**, not merely over its diagonal elements.

The reason is **exhibited, not observed**. The `chi = -1` fibre legs are the
three `eta`-traceless diagonal modes and the three *purely spatial*
off-diagonals. The diagonal modes can never flip (`s_i^2 = +1`). The spatial
off-diagonals flip in count `k(3-k)`, where `k` is the number of flipped
spatial base legs:

```text
k        0   1   2   3
k(3-k)   0   2   2   0        -- even for every k.
```

They always flip **in pairs**, so their contribution cancels. And this is **not
generic**: for an `n`-dimensional spatial slice, `k(n-k)` is odd at `k = 1`
whenever `n` is even. The fibre's blindness to the time-orientation is a
three-spatial-dimension fact, recorded here so it is not later assumed as a
structural generality.

**Carrier verdict.** The datum is carried by the **base Lorentz frame**. It is
a time-orientation of the tautological timelike line of `X^4`, pulled back to
`Y^14`. It is *not* a datum about the metric fibre's own ten directions, and
*not* an independent orientation of `Y^14`.

### 2.4 Three structures, three DIFFERENT orientation characters — the Layer-0 payload

The same exhaustive computation separates the program's own structures (probe
Part 4). Writing `det` and `orth` for the two `pi_0(O(3,1))` invariants:

| object | return character | what that character IS |
|---|---|---|
| `J_obs`, the reality structure | `det` | **SPACETIME** orientation |
| `K_S = e_0...e_8`, the Krein form | `det * orth` | **SPACE** orientation (verified: it is the determinant of the spatial `3x3` block) |
| `C_perp = K J_obs`, the coflip | `orth` | **TIME** orientation |

and `chi = sigma_K * sigma_J` exactly — the elementary identity *spacetime
orientation = space orientation x time orientation*, realized by GU's own
coflip factorization. The three are pairwise distinct (K3).

**Layer-0 consequence, and it is a live caution rather than a decoration:** any
claim that welds "the arrow" to a sign carried by the program's Krein structure
must say **which of the three objects** it attaches to. The Krein *form*'s own
return character is the **space** orientation. Only the antilinear coflip
`K J_obs` carries the time orientation. A weld written against the wrong one of
the three would be a homonym with the right group order — the exact failure
mode DC-H1 already caught once.

### 2.5 A fourth homonym, excluded

The induced 14-frame return has determinant `det(Lambda)^2 = +1` for every
`Lambda in O(3,1)`. So the `Z/2` in play is **not** `Y^14`'s
spacetime-orientation class — consistent with the standing unconditional
theorem `w_1(Y^14) = 0`, and independently reproducing it along fibre loops.
Four `Z/2`s are now separated in this neighbourhood: `pi_1(SO)` (DC-H1: does
not act), `w_1(Y^14)` (trivial), the `E+/E-` grading (distinguishes, does not
orient), and the orthochronous character (acts isomorphically).

### 2.6 The fibrewise twist, and the base-side no-go

The simple reading — "so the datum is an `X^4` datum, go look for it on the
base" — is **wrong**, and the probe says why (Part 5).

The loop lies inside a **single fibre**. Therefore the class restricts
nontrivially to `F_x`. But every class pulled back from the base restricts to
**zero** on every fibre, because the projection of a fibre loop to `X^4` is the
constant path. Hence

```text
w_t  is NOT in the image of  H^1(X^4; Z/2) -> H^1(Y^14; Z/2),
```

and consequently:

> **No base-side time-orientation, however it is supplied, can equal or cancel
> this class on `Y^14`.** The tautological Lorentzian structure on the
> observerse is *never* time-orientable, for *any* `X^4`.

This is the sharpest structural result of the run, and it forks the question
cleanly:

- **On a fixed section** (one chosen metric `g`), the fibre loop is not
  available; the datum is an ordinary time-orientation of `(X^4, g)`, a class
  in `H^1(X^4; Z/2)`, and an `X^4`-side supplier would be admissible in
  principle. Every candidate in §3 lives here.
- **On the observerse `Y^14`** — which is where the B5 packet, the shiab
  operator, `Cl(9,5)` and the ledger item itself live — the obstruction is
  present for every `X^4` and no base-side supply reaches it.

The ledger item is an object of the second kind. That is why §3's answer cannot
be rescued even by a successful base-side supplier.

**Scope, inherited and stated plainly.** Everything above lives on `F` and on
the 14-dim gimmel frame. The link `L^13` is not the spine, and the transfer of
the class to `pi_1(L^13)` needs `pi_2(X^4) -> pi_1(L^9)`, which is `X^4`-
dependent and OPEN (M-H7 O2/O3). §2.1's geometry, §2.3's carrier split, §2.4's
three characters and §2.6's no-go are all statements about `F` and `Y^14` and
are **robust to that gap**; nothing here claims anything about `L^13`.

**Coflip dependence, fenced.** §2.3-2.4 are statements about the program-native
`C_perp = K J_obs` (a different antilinear structure gives a different `chi` —
negative control, fires). §2.1 and §2.6 are not: they are pure Lorentzian
geometry and survive any change of Clifford convention.

### 2.7 Bearing on `wave-swing2`'s IC-3

`explorations/wave-swing2-the-bit-2026-07-21.md` identified `sigma` with
`w_1(L_time)` **and** with the spin double-cover class, correctly noting that
`H^1(RP^3;Z/2)` is one-dimensional so *any* nontrivial `Z/2` is the same class
by pigeonhole, and binding future work with **IC-3**: *do not upgrade the
class-level identity to a claim that geometry alone selects `sigma`.*

This investigation respects IC-3 exactly and resolves the ambiguity it flagged, in the
one direction that pigeonhole could not:

- the **mechanism** is the `L_time` reading. §2.1 exhibits the loop physically
  reversing a future-pointing timelike vector, with no cohomological
  pigeonhole and no Clifford input.
- the **spin/belt-trick** reading is a homonym for this class: DC-H1 showed
  `chi(-I) = +1` and that the loop's own lift satisfies `T^2 = +I`, so the
  double cover is not merely invisible to `chi` but *not engaged*. The
  candidate identity flagged in `wave-swing2` ("Kramers `T^2 = -1` == belt-trick
  `2pi = -1`") therefore gains a negative bearing here: whatever its general
  status, *this* class does not run through it.
- and IC-3 stands: nothing below selects `sigma`. §3 is the reason.

---

## 3. Part (2) — IS IT ALREADY SUPPLIED? The payoff question

### 3.1 The rule, stated before any candidate was classified

> A construction **FIXES** a time-orientation iff its defining law contains a
> **T-odd term** AND it takes **no orientation-valued input**. Otherwise it
> **PRESUPPOSES** one.

Both halves are needed and both do work. A T-*even* law has a time-reversed
solution for every solution: its solution set is `T`-stable, so it selects a
*pair* of directions, never one. A T-*odd* law that is only T-odd because one
of its inputs already carries a direction has assumed what it purports to
supply. The probe applies the rule mechanically, and a **synthetic control**
(`p'' + gamma p' = 0` with `gamma` orientation-free) is classified `FIXES`, so
the empty result below is not vacuous (kill condition K5).

### 3.2 The verdict table

| candidate | law's T-parity | orientation-valued input it takes | verdict |
|---|---|---|---|
| W166 record-count / arrow mode | **EVEN** (exact) | the affine `tau`; the choice of the growing branch | PRESUPPOSES |
| record accretion, `Lambda = c/sqrt(N)` | odd | **the causal past** — `N` is a past-cone integral | PRESUPPOSES |
| theta-sector on an FLRW background | **EVEN** (exact) | an oriented FLRW time; past initial data | PRESUPPOSES |
| causal order (Malament / BLMS) | odd | **the precedence relation**, already directed | PRESUPPOSES |
| the indefinite-base requirement | — | none — but it supplies `O(3,1)`, not `O^{up}(3,1)` | PRESUPPOSES |
| symmetric hyperbolicity SH2 | — | `mu_0`, a time direction, is a *hypothesis* | PRESUPPOSES |
| CH-REC's transmitted `eps` | odd | `eps` itself, typed in-artifact as payload item 1 | PRESUPPOSES |
| SYNTHETIC control (`gamma p'`) | **ODD** | none | **FIXES** |

**All seven real candidates PRESUPPOSE. None fixes.**

### 3.3 The two that look closest, taken seriously

**W166 is the strongest candidate and it does not fix.** W166's structural
claim is solid and is not disputed here: `m_0^2 < 0` in the conformal /
record-count mode is the *same object* as record genesis, because `N ~ e^{4p}`
is monotone in the scale amplitude. But the mode equation `p'' + m_0^2 p = 0`
is **exactly T-even** (probe: `EVEN`, symbolically, for both signs of `m_0^2`),
and its solution space is `{e^{+tau/2}, e^{-tau/2}}` with `tau -> -tau`
**exchanging the two branches** (probe, exact). So "`N` grows" names a
*branch*, not a *direction*; selecting the growing branch is a boundary
condition with respect to an already-oriented `tau`. W166's own dichotomy is
LIVE-vs-DEAD (`m^2 >= 0` gives an oscillatory `p`, no accretion), which is a
genuine and interesting statement — but LIVE-vs-DEAD is not
FORWARD-vs-BACKWARD. W166 itself says so: "*nothing asserts an arrow of time as
fact*", and its honest grade is PLAUSIBLE. The reframe stands; the derivation
does not exist.

The same argument disposes of the FLRW background independently: the Friedmann
first equation contains `adot` only as `adot^2`, so `a(t) -> a(-t)` maps
solutions to solutions (probe, exact). Expansion versus contraction is a
boundary condition. The `theta`-sector's DESI-facing integrations run `z = 3 ->
z = 0` from past initial data — an imposed direction, and the `w_a` sign is
already known to be IC-sensitive.

**Record accretion is T-odd, and that is exactly why it fails.** `Lambda(x) =
c/sqrt(N(x))` with `N` the promoted count *in the causal past* is a genuinely
retarded, time-asymmetric law. But its asymmetry is **imported with the past
cone**. Removing the orientation from the input removes the asymmetry from the
law. This is the case the deciding rule exists for, and being ruthless about it
is the point: a construction that assumes a time-orientation does not derive
it. The same disposes of the Malament/BLMS route — a causal *precedence*
relation is a directed order in its premises, and `W151` never claims
otherwise.

**The indefinite-base requirement is the datum's PRECONDITION, not its
supplier.** Canon §7 makes the Lorentzian signature load-bearing (a Riemannian
base gives a contractible cone: no `RP^3`, no spine, no loop, nothing). But
what it supplies is the *group* `O(3,1)`, which has four components. A
reduction to the orthochronous subgroup is a strictly further datum. The
requirement is what makes the `Z/2` **exist**; it cannot also fix it.

**CH-REC is the closest thing to good news, and it is already booked.**
`channel-swing-CH-REC` establishes that the record direction, the sector
`G`-sign and the vacuum cancellation sign are **one** transmitted orientation
`eps` — "zero new payload items", with the arrow living "in the record law plus
`eps`, not in the propagator", and the sharp accounting identity that
*decoupling* the arrow from the Krein sign would cost **one additional** `Z/2`
import. That is a real and valuable result. It is also, explicitly, an
identification of the arrow with an **import**: `eps` is payload item 1. So
CH-REC does not fix the orientation; it *prices* it, and reports that the price
is already on the ledger.

### 3.4 Two independent reasons the answer cannot be "FIXED"

1. **T-parity** (§3.1-3.3): every candidate law is either T-even or T-odd only
   through an orientation-valued input.
2. **The base-side no-go** (§2.6): even a hypothetical successful base-side
   fixer would produce a class in `H^1(X^4; Z/2)`, whose pullback restricts to
   zero on every metric fibre — and the ledger's class does not. So the two
   objects cannot be equal, and the supply cannot cancel the obstruction.

The second reason is the stronger one, because it does not depend on auditing
any particular candidate. It says the *shape* of a base-side supply is wrong
for the *shape* of this datum, on the carrier where the datum actually lives.

---

## 4. Part (3) — the tri-repo fence

The records / finality **interpretation** is TaF-owned (2026-08-03 typings and
the mailbox response `20260803-taf-response-records-de-typings.md`). This note
observes that fence:

**Stated here, and it is GU-side mathematics only.** A time-orientation is a
reduction of the structure group `O(3,1)` to its orthochronous subgroup,
equivalently a choice of ray in the tautological timelike line; the DeWitt
loop's holonomy exchanges the two rays; the character is `orth`; the coflip's
character is `orth` while the Krein form's is `det*orth` and the reality
structure's is `det`. None of that mentions records, finality, capability, or
issuance.

**NOT stated here, and it may not be inferred.** That this `Z/2` *is* the
finality direction. That the record-accretion direction and this
time-orientation are the same object. Any import of TaF's capability measure.
W166's own tri-repo gate says the same thing from the GU side ("record /
finality / arrow-of-time / capability semantics stay pointers to
temporal-issuance / TaF; GU owns the induced-action math and the mode identity
only"), and this note does not widen it.

**Named as a JOINT item, because the honest finding is that it cannot be
settled GU-side.** Whether GU's orientation datum and TaF's finality direction
are the same object requires a TaF-side statement of what the finality
direction is a direction *of*. GU can now make that question cheap to answer,
because §2.4 supplies a discriminating instrument: there are **three**
candidate characters on the same group and they are pairwise distinct. If TaF's
object attaches to a spacetime-orientation, it is `sigma_J = det`; to a
space-orientation, `sigma_K = det*orth`; to a time-orientation, `chi = orth`.
The joint item is: *TaF names which, or names a fourth; GU checks it against
the exhaustive `pi_0(O(3,1))` table.* Nothing further is asserted.

---

## 5. What this does to the external ledger

**Nothing numeric. The ledger does not reduce.**

```text
before:  D1 = one Z/2 orientation carried jointly by P1 and P2   (P3 = D2 separate)
after:   unchanged  -- three pieces unconditional, two under the conditional
                       P1/P2 weld, exactly as the Wave 1A banner states
```

What changes is a **relocation and a sharper typing**, stated so that the
tempting overstatement is visible and refused:

> `D1` is not a `Z/2` value awaiting supply, and not a boundary-framing
> holonomy (DC-H1 killed that). It is the **time-orientation of the tautological
> timelike line** — `w_1` of the orientation double cover of `L_time` over the
> metric fibre. Its externality is the externality of a structure that is
> obstructed *fibrewise*, on every `X^4`. Nothing in GU fixes it; several
> things presuppose it; and because the obstruction is fibrewise, nothing that
> could be supplied on the base would fix it either.

Three consequences worth booking, none of them a promotion:

1. **The arrow is not a NEW datum.** CH-REC already booked that (zero new
   payload items). This investigation supplies the *mechanism* behind that accounting:
   the character in question is literally the orthochronous character of the
   Lorentz stabilizer. That is a mechanism supply for an existing conditional
   identification, not a reduction.
2. **One datum, many consumers.** The `theta`-sector's integration direction,
   the record-accretion direction, W166's arrow mode, SH2's `mu_0`, and the
   causal-order route are all consumers of *the same kind of* `Z/2`. That they
   are the same *instance* is not established here and must not be assumed —
   but it is now a well-posed, cheap question, and if any two of them used
   opposite instances the program would be inconsistent. That consistency
   condition was not previously named.
3. **A previously unearned framing is now half-earned.** `README.md`'s standing
   `sigma/tau` paragraph calls `sigma` "one `Z/2`, the orientation /
   time-reversal bit". The *time-reversal typing* is now earned at mechanism
   grade for the `D1` piece. The *count* ("exactly two data enter from
   outside") remains over-banked — the ledger is three unconditional / two
   conditional — exactly as
   `explorations/uncontestability-audit-math-spine-2026-07-21.md` §4 already
   flagged. Recorded as a register item; no file is edited here.

---

## 6. Findings, labelled

**`CHEAP_NEW_COMPUTATION` — the carrier split.** `chi_fibre == +1`
identically, with an exhibited parity mechanism and a named dimension
dependence. New; nothing in the repository had decomposed the character over
the base/fibre legs.

**`CHEAP_NEW_COMPUTATION` — the three characters.** `sigma_J = det`,
`sigma_K = det*orth`, `chi = orth`, `chi = sigma_K sigma_J`. New, and it
converts "which `Z/2` does the arrow attach to?" from a rhetorical question
into a decidable one.

**`CHEAP_NEW_COMPUTATION` — the fibrewise no-go.** The tautological Lorentzian
structure on `Y^14` is never time-orientable. New as a statement; it follows
immediately from DC-H1's loop plus the observation that the loop is confined to
one fibre, which no prior artifact drew out.

**Bears on a `VERIFIED_REPO_DISCONNECT` that is already on the books.**
`docs/paper-formalization-candidates.md` §8A records that the paper's §12.2
argues "GU addresses L4 by recovering temporal order from the Observerse, not
assuming it", with "**Repo overlap: None**", while
`canon/six-axis-specification-protocol.md` L4 (causal order) is recorded as not
addressed. This investigation does not discover that gap — it **sharpens it**: for the
*orientation* half specifically, recovery from the observerse is not merely
unbuilt but obstructed, because the obstruction is nonzero on every metric
fibre. Recovering a causal *order* (a conformal structure) is a different and
still-open claim; only the orientation half is addressed here.

**`REFEREE_CONJECTURE` — none offered.** No conjecture is filed by this run.

---

## 7. Controls

Five kill conditions were declared in the probe header before the probe body
was written.

| id | condition | fired? |
|---|---|---|
| K1 | `chi_fibre` not identically `+1` => the base-carrier verdict dies | no (`+1` on all sixteen) |
| K2 | the four `pi_0(O(3,1))` components not all represented => the check is not exhaustive | no (all four present) |
| K3 | `sigma_K == chi` => §2.4's discriminator is empty | no (three pairwise-distinct characters) |
| K4 | `h_t(v_t,v_t)` not identically negative => §2.1's future/past reading is void | no (`= -1` exactly, all `t`) |
| K5 | the synthetic T-odd/no-input control not classified `FIXES` => §3's negative is vacuous | no (classified `FIXES`) |

Five negative controls **fired as required**: a generic non-Clifford lift has
no character and raises (6/6); a different antilinear structure gives a
different `chi` (so `chi` is not a hardcoded constant); deleting the conformal
leg destroys the `(6,4)` signature (so the frame is load-bearing); some
`chi = -1` fibre legs *do* flip (so §2.3's triviality is a cancellation, not a
vacuity); and every artifact cited in §3's ledger is checked to exist on disk
(so the audit cannot drift into fiction).

The probe **fails closed**: a planted `chi_fibre == -1` expectation exits 1
(and, run from outside the checkout, the artifact-existence check fires too —
so §3's ledger really is tied to the repository and not to a comment).

52 checks, exit 0. `process_gates/certificate_shape_audit.py` green, together
with the explorations/tests README-surface, top-level-boundary,
manifest-count, public-path-hygiene and protected-surface-diff gates.

---

## 8. Reopeners, in cost order

1. **Cheapest, and it falls straight out of §2.4.** CH-REC's `eps` — does it
   attach to the *linear* Krein involution or to the *antilinear* coflip
   `C_perp = K J_obs`? The two carry **different characters** (`det*orth`
   versus `orth`). If `eps` attaches to the linear structure, then CH-REC's
   "the arrow is `eps`" welds the arrow to the **space**-orientation character
   and is a Layer-0 error; if it attaches to the coflip, the weld is exact and
   CH-REC's accounting identity gains a mechanism. Finite linear algebra on
   objects that already exist. This is the cheapest new question *this* check
   generated.
2. **The joint item (§4).** TaF names which character, if any, its finality
   direction attaches to; GU checks it against the exhaustive table. Cannot be
   done GU-side.
3. **Consistency of the consumers (§5 item 2).** Are the `theta`-sector's
   integration direction, `N`'s past cone, W166's branch selection and SH2's
   `mu_0` the same *instance* of the `Z/2`, or merely the same *type*? Well
   posed; needs the packet's normalized phases, so it is downstream of the B5
   fail-closed residual.
4. **The transfer, unchanged from DC-H1.** Is `pi_1(F)`'s class in the image of
   `pi_1(L^13)`? Hostage to M-H7 O2/O3. Do not attempt before those.
5. **The section-vs-observerse fork (§2.6).** Which carrier does GU's physics
   actually run on — a chosen metric section, or the full observerse? The
   ledger item lives on the observerse; if some part of the program silently
   works on a section, the obstruction is invisible there and the two usages
   must be separated. Not adjudicated here.

---

Nothing in this file moves any claim, canon entry, verdict, bar, H59, the
count, LANE-STATE, the external-datum ledger, or any fork. The records /
finality interpretation is TaF-owned and is not asserted. Pre-deposit; any
decisive downstream use is J5-gated.
