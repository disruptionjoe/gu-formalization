---
artifact_type: exploration
status: exploration
doc_type: deciding-check
created: 2026-08-04
work_item: DC-H1
title: "DC-H1: the B5 chirality-orbit signs ARE a path-type holonomy but NOT a framing-type one. The ten special-orbit relative signs are moved by parallel transport around the generator of pi_1(F) = Z/2 (the DeWitt metric-fibre loop), so the datum is a monodromy class and not a stored value. But the orientation character is QUADRATIC in the Clifford lift: it descends to SO, the deck element -I of Spin -> SO has character +1, and the character is invariant under an arbitrary change of trivialization. So the [L^13, SO] reframing freedom acts on the orbit signs through the ZERO homomorphism, P1 is NOT framing-determined, and the external ledger does not reduce. Layer-0: the Z/2 that fires is pi_0 of the Lorentz stabilizer O(3,1) -- the O(1) TIME REFLECTION named in canon Section 7 -- exhibited exactly as the orthochronous character; it is a REFLECTION Z/2, not the spin double-cover Z/2. Same group order, different mechanism: HOMONYM."
grade: "EXACT finite linear algebra (Gaussian-integer Cl(9,5) rep, asserted) plus pure integer combinatorics, in tests/dc-h1/dc_h1_orbit_sign_monodromy_probe.py: 42 hard checks, four preregistered kill conditions, five firing negative controls, exits nonzero on any failure. The -1 loop return is INDEPENDENTLY reproduced here (no import from the full-20 probe) and agrees with the published result. CITED, not re-derived: the reduction of the ten relative phases to ONE common phase (Gamma-naturality plus the 136 written coefficient intertwiners, full20-dewitt-loop-transport-wave-2026-07-30, rerun green 2026-08-04). NOT established: any transfer of the loop from the metric fibre F to the 13-dim link L^13; any packet field, phase, Green form, domain, or operator; any movement of the count."
prereg: explorations/atlas-derived-external-datum-hypotheses-2026-08-04.md
probe: tests/dc-h1/dc_h1_orbit_sign_monodromy_probe.py
kill_conditions_declared_before_computation: true
depends_on:
  - lab/process/CURRENT-RESEARCH-CONTEXT.md
  - explorations/atlas-derived-external-datum-hypotheses-2026-08-04.md
  - canon/boundary-einvariant-and-the-tangential-fork.md
  - explorations/mh7-dim13-restatement-2026-08-03.md
  - explorations/b5-chirality-orientation-audit-2026-07-29.md
  - explorations/b5-phase-sum-forcing-audit-2026-07-29.md
  - explorations/shiab-operator/b5-observer-symbol-multiplicity-matrix-2026-07-24.md
  - explorations/sa-y8-majorana-layer0-and-vertical-krein-weld-2026-07-29.md
  - explorations/full20-dewitt-loop-transport-wave-2026-07-30.md
  - explorations/external-datum-ledger-and-the-2plus1-product-rule-2026-07-29.md
deposit: "pre-deposit; any decisive downstream use is J5-gated"
construction: "program-native throughout per GEOMETER-VS-PHYSICS-OBJECTS.md: the certified B5 observer-symbol matrix, the program-native Krein-dual coflip C_perp = K J_obs, and the actual DeWitt metric fibre GL(4,R)/O(3,1). No positive-Hilbert substitution."
canon_verdict_change: none
outcome: "DC-H1-PARTIAL: PATH-TYPE CONFIRMED, FRAMING MECHANISM FALSIFIED"
---

# DC-H1 — are the B5 chirality-orbit signs a monodromy?

**Preregistered outcome: (c) PARTIAL. No promotion. The external ledger does
not reduce.**

The preregistration in `atlas-derived-external-datum-hypotheses-2026-08-04.md`
§H1 bundled two claims into its outcome (a): that the orbit signs are a
*monodromy*, and that they are therefore *framing-determined*. This check
splits them, because they come apart:

| half of H1 | verdict |
|---|---|
| the sign is a **holonomy of a path class**, not a stored value | **SUPPORTED** (exact; but by a result already in the repository) |
| the sign is moved by the **framing class** (`[L^13, SO]`, via `pi_1(SO(3)) = Z/2`) | **FALSIFIED** (exact; the action is the zero homomorphism) |
| therefore **P1 is framing-determined and the ledger REDUCES** | **DOES NOT FOLLOW** |

The mechanism H1 named — "a `Z/2` monodromy of the spine's double cover
`S^3 -> RP^3`" — **does not transfer**. A different `Z/2` monodromy is
present, and it is a *reflection* `Z/2`, not a *double-cover* `Z/2`. Per the
standing discipline note, the shared group order `|Z/2| = 2` is
number-matching (N13, the weakest class) and is not offered as evidence
anywhere below; every load-bearing statement is a computed mechanism.

---

## 1. (i) What the six orbits are, and what assigns their relative signs

Rebuilt exactly in the probe (Part 1) from the certified 12-label type matrix
of `explorations/shiab-operator/b5-observer-symbol-multiplicity-matrix-2026-07-24.md`,
with the provenance expansion done from scratch rather than cited:

```text
20 slots, 136 ordered nonzero cells, 68 transpose pairs, 68 mirror orbits,
joint orbits under <mirror, transpose>: 29 four-cell + 10 special two-cell.
```

The ten special orbits are exactly the cells `(i, m(i))` fixed by the
composite of mirror and transpose. They split **6 + 4**, and the six are
recovered by name:

```text
S:Lm <-> S:Lp                imGamma:Lm <-> imGamma:Lp    kerGamma:Lm <-> kerGamma:Lp
S:Rm <-> S:Rp                imGamma:Rm <-> imGamma:Rp    kerGamma:Rm <-> kerGamma:Rp
```

i.e. one `L16` and one `R16` `E+/E-` orbit in each of the three provenances
`S`, `imGamma`, `kerGamma` — matching
`b5-phase-sum-forcing-audit-2026-07-29.md` exactly. The remaining four are the
X-sector orbits `X32`, `X23`, `X2T`, `X1T`.

**What assigns their relative signs in the committed ledger: nothing.** The
invariance battery is reproduced (Part 1): the cell set, slot dimensions,
provenance sector, cell multiplicity, and orbit structure are *all* invariant
under global `E+ <-> E-` exchange, while chirality *distinguishes* the two
cells of each of the six. That is the standing verdict
`DISTINGUISHED-NOT-ORIENTED`. The sign assignment is therefore **not a
function of any committed point-datum** — which is the negative half of H1's
question, and it was already established.

Their joint effect is one integer, not ten bits: exhaustive over all `2^10`
assignments, `even = 68 + sum(signs)`, eleven values `58..78` in steps of two.

**Cited, not re-derived here:** the full-20 DeWitt run showed that
`Gamma`-naturality plus the 136 *written* coefficient intertwiners force all
ten relative phases equal, collapsing the `2^10` static freedom to **two
absolute assignments** — one common phase `eps`. (Rerun green 2026-08-04:
`static 1024, coefficient-level 2 absolute`.) So the object DC-H1 must type is
that single bit `eps`.

---

## 2. (ii) Is `eps` a function of a path?

**Yes, exactly.**

### 2a. The loop is the generator of `pi_1(F)`, and this is now exact

`F = GL(4,R)/O(3,1)` is the metric fibre; canon
`boundary-einvariant-and-the-tangential-fork.md` §7 gives its spine
`RP^3 = O(4)/(O(3) x O(1))` with the `Z_2` identified as **the `O(1)` Lorentz
time-reflection**, and records that the retract requires the indefinite base
signature (a Riemannian base gives a contractible cone — no spine, no loop,
nothing below exists).

The full-20 probe's loop is `B_t = ` rotation by `pi t` in the `(x_0, x_3)`
plane, with `h_t = B_t^T eta B_t`. The probe verifies (Part 2), exactly:

- `h_t` has signature `(3,1)` at every sample and `h_1 = h_0 = eta`, while
  `max|h_t - eta| > 1/2` — a genuine non-constant loop **in `F`**;
- the `GL(4,R)`-lift ends at `B_1 = diag(-1,1,1,-1)`, which lies in `O(3,1)`
  with `det = +1` and `(B_1)_{33} < 0` — the **PT / non-orthochronous**
  component;
- the doubled loop lifts to `I`.

From the fibration `O(3,1) -> GL(4,R) -> F`, `pi_1(F) = ker(pi_0 O(3,1) ->
pi_0 GL(4,R)) = {1, PT} = Z/2` (orders asserted: `|pi_0 O(3,1)| = 4`,
`|ker| = 2`). So `[loop]` is **the** nontrivial element. This is a sharpening:
the full-20 run established the transport; it did not identify the loop's
homotopy class.

### 2b. The orientation character, independently reproduced

On an independently built `Cl(9,5)` (Gaussian-integer entries, Clifford defect
`0.00e+00`, signature `(9,5)` asserted), with the program-native coflip
`C_perp = K J_obs` (antilinear involution, defect `0.00e+00`), define

```text
chi(T)  by   T . C_perp . conj(T)^-1  =  chi(T) . C_perp .
```

`chi` is a group homomorphism (verified on 60 random lifts), so it is a
product of per-leg characters:

```text
per-leg chi = [+1,+1,+1,-1 | -1,-1,-1,-1,-1,-1 | +1,+1,+1,+1]
```

The loop's induced 14-leg frame return is *derived* (not hardcoded) from `B_1`
by exact rational arithmetic on the DeWitt frame — it reverses `2` base and
`4` `Sym^2` legs, `3` positive and `3` negative, matching the published
count — and

```text
chi(loop)   = -1        chi(loop^2) = +1 .
```

This reproduces the published central `-1` **without importing it**.

**Consequence.** The single bit `eps` is not a stored value: the `Z/2` local
system of admissible coflips over `F` has holonomy class `w != 0` in
`H^1(F; Z/2)`. There is no global section. *That* is H1's "holonomy, not a
stored value," and it is exact — but note that it was already the content of
the full-20 run of 2026-07-30, so DC-H1 does not earn it, it types it.

*Arithmetic consequence, stated at arithmetic grade only (probe 3b):* under
`C -> -C` the even and breaking subspaces exchange, so the even count `d` maps
to `136 - d`, i.e. `58 <-> 78`. Only the unordered pair is loop-invariant.
Certifying this **on the packet** (rather than as involution arithmetic) is a
named reopener below, not a result here.

---

## 3. (iii) Does the framing class act? Exhibit

**No. The action is the zero homomorphism, and this is the decisive half.**

A change of framing can do exactly two things to a transport:

1. change the reference frame at the basepoint, `(C, T) -> (g C conj(g)^-1,
   g T g^-1)`; and
2. change the homotopy class of the `SO`-development along the loop by
   `[g o gamma] in pi_1(SO) = Z/2`, which multiplies the **Spin lift** by `-1`.

Both are computed, and both leave `chi` fixed.

**(1) is the identity on `chi`.** For *any* invertible `g`,

```text
(gTg^-1) (g C conj(g)^-1) conj(gTg^-1)^-1
   = g (T C conj(T)^-1) conj(g)^-1
   = chi(T) . (g C conj(g)^-1) .
```

Verified numerically on six deterministic-seeded dense `g` (max relative
defect `5.6e-15`).

**(2) cannot be seen at all, because `chi` is quadratic in the lift.**
`T . C . conj(T)^-1` is invariant under `T -> -T`, so `chi` descends to `SO`.
Exhibited two ways in the probe:

- `chi(T) = chi(-T)` on 40 random lifts;
- the **genuine double-cover generator** is built explicitly: for a spacelike
  pair, `(gamma_i gamma_j)^2 = -I` and `exp(pi gamma_i gamma_j) = -I`, i.e.
  the `2pi` rotation is `I` in `SO` and `-I` in `Spin`. Its character is

```text
chi(-I) = +1 .
```

**So the deck transformation of `Spin -> SO` moves no orbit sign.** The
homomorphism `pi_1(SO) = Z/2 -> {orbit signs}` asked for in DC-H1(iii) is the
**zero** homomorphism. Since a reframing `g: L^13 -> SO` can only act through
(1) and (2), the `[L^13, SO]` reframing freedom — M-H7's named open item O4 —
acts trivially on the orbit signs.

There is one more thing worth stating for two-sidedness: the loop's own
Clifford lift satisfies `T^2 = +I` (defect `0.00e+00`). The loop is an
*involution* in `Spin`, not a `2pi` rotation. The double cover is not merely
invisible to `chi`; it is **not engaged by this loop at all**.

### The `Z/2` that IS there, exhibited exactly

Exhaustively over all sixteen diagonal elements of `O(3,1)` (probe Part 5),
`chi` is **constant on each of the four `pi_0(O(3,1))` components** (kill
condition K1: had it not been, the monodromy reading would have died), and

```text
chi(Lambda) = the ORTHOCHRONOUS character of Lambda     (all 16 cases)

  (det, orth) = (+1,+1) -> chi = +1        (+1,-1) -> chi = -1   [= PT = pi_1(F)]
  (det, orth) = (-1,+1) -> chi = +1        (-1,-1) -> chi = -1
```

So `chi` restricted to `pi_1(F) = {1, PT}` is an **isomorphism onto `Z/2`**,
and the `Z/2` it is, is the **time-orientation character** — precisely the
`O(1)` Lorentz time-reflection canon §7 names as the spine's `Z_2`.

---

## 4. Layer-0: three `Z/2`s, two of which are homonyms here

| token | object | mechanism | acts on the orbit signs? |
|---|---|---|---|
| `Z/2` of `pi_1(F)` | `pi_0` of the Lorentz stabilizer `O(3,1)`; the PT / time-reflection component | reflection; `chi` = orthochronous character | **YES**, isomorphically |
| `Z/2` of `pi_1(SO(3))` | the deck group of the spin double cover `S^3 -> RP^3 ~ SO(3)`; the `[L^13, SO]` reframing's only `Z/2` | double cover; deck element `-I in Spin` | **NO** — `chi(-I) = +1` |
| `Z/2` of the `E+/E-` grading | the global chirality exchange on the B5 ledger | representation grading | distinguishes, does not orient |

The first two share a group order and nothing else. **HOMONYM.** The
hypothesis note's own warning fires here exactly as written: the group
coincidence rescues nothing, and the mechanism match — "a binary choice on an
overlap resolved by path-continuation" — is only half-present. Path
continuation: yes. The *double cover* that made the netcode rhyme (quaternion
rotation compression) : no.

---

## 5. Honest scope, and what is NOT established

1. **The loop is in `F`, not on the link.** Everything above lives on the
   10-dim metric fibre. `mh7-dim13-restatement-2026-08-03.md` §5 loss 1 is
   binding: the link is *not* the spine, and no homotopy equivalence of open
   manifolds controls the link's end structure. Transfer would need
   `pi_1(L^9) = pi_1(RP^3) = Z/2` (fine — `S^6` fibre) and then survival
   through `pi_2(X^4) -> pi_1(L^9) -> pi_1(L^13)`, which is `X^4`-dependent
   and **OPEN** (M-H7 gaps O2/O3). Nothing here closes it. Note that the
   framing negative is *robust to* this gap: even if the class transfers,
   `pi_1(SO)` still acts as zero.
2. **The relative-phase collapse is cited.** DC-H1 does not re-derive
   `Gamma`-naturality or the 136 written intertwiners; it reruns them.
3. **`chi` is a statement about `C_perp`, one whole-module construction.** The
   B5 fail-closed packet still lacks normalized 20-slot phases, a Green
   boundary form, a common closed domain, and the nonlinear completion. No
   packet field is frozen here.
4. **`P2`, `P3` untouched.** The `P1/P2` weld is the full-20 result at its own
   grade; the reinstated count datum `P3` is not addressed.
5. **The RS function-space residual, the carrier/signature forks, and the
   compact-vs-Lorentzian fork** are all upstream of this and unmoved.

---

## 6. What this does to the external ledger

**Nothing numeric. The ledger does not reduce.**

```text
before:  D1 = one Z/2 orientation carried jointly by P1 and P2
         D2 = P3, the separate physical chiral-index/count datum
after:   unchanged
```

What changes is a **typing**, and it is worth recording precisely because the
tempting overstatement is nearby:

> `D1` is not a `Z/2` *value* awaiting supply from outside. It is a `Z/2`
> **local system** on the metric fibre whose holonomy class is computed and
> nonzero. Its externality is the externality of a structure with no global
> section — not of a number handed in. But it is **not** determined by, and
> does not vary with, the boundary framing class; so nothing is derived from
> the framing, and no piece leaves the ledger.

Under H1's preregistered outcomes this is exactly **(c) partial**: report the
split, no promotion. Outcome (a)'s consequent fails; outcome (b)'s antecedent
holds (framing-independent) but its consequent ("P1 stays a value-type datum")
is *also* wrong — the datum is path-type. The preregistration's binary was
under-specified, and the honest report is the split, not a nearest-match.

---

## 7. Controls

Four kill conditions were declared in the probe header before computation.

| id | condition | fired? |
|---|---|---|
| K1 | `chi` not constant on a `pi_0(O(3,1))` component => monodromy reading dies | no (constant on all four, exhaustive over 16) |
| K2 | `chi(-T) != chi(T)` => the framing half is LIVE | no (blind on 40 lifts) |
| K3 | the `2pi`-rotation lift is not `-I` => Part 4 is void | no (`-I` exactly, `bivector^2 = -I` exactly) |
| K4 | `chi` constant over leg subsets => every negative is vacuous | no (surjective onto `{+1,-1}`) |

Five negative controls **fired as required**: a different antilinear structure
`gamma_a C_perp` gives `chi = +1` (so `chi` is not hardcoded); a one-sided,
non-reframing move of the coflip destroys the character (6/6 undefined); a
generic non-Clifford lift has no character and raises (6/6); toggling exactly
the seven `chi = -1` legs moves the loop's sign and the seven `chi = +1` legs
do not; and the probe fails closed (a planted `chi(loop) = +1` expectation
exits 1).

42 checks, exit 0. `process_gates/certificate_shape_audit.py` green.

---

## 8. Reopeners, in cost order

1. **Cheapest.** Certify the §2b arithmetic consequence *on the packet*: does
   the nontrivial holonomy make the even/breaking split (`58` vs `78`) a
   non-global function on `F`, and if so what is the invariant statement? This
   is finite linear algebra on objects that already exist.
2. **The transfer.** Is `pi_1(F)`'s class in the image of `pi_1(L^13)`? Needs
   `pi_2(X^4) -> pi_1(L^9)`; hostage to M-H7 O2/O3 and to the `X^4`
   compactness input. Do not attempt before those.
3. **Named, and now sharper.** If the orbit-sign `Z/2` is the *time-orientation*
   character, then the datum's natural home is a time-orientation of the
   Lorentzian base, not a boundary framing. Whether GU's construction supplies
   or requires one is a physics-facing question that has not been asked in
   this form. It is not a claim; it is the cheapest new question this check
   generated.

Nothing in this file moves any claim, canon entry, verdict, bar, H59, the
count, LANE-STATE, or any fork. Pre-deposit; any decisive downstream use is
J5-gated.
