---
artifact_type: exploration
status: exploration
created: 2026-07-04
title: "(9,5)-vs-(7,7) decide-tournament: does GU-native structure FORCE the metric signature of Y^14 = Met(X^4), hence J^2 and the C-07 quaternionic-parity wall? HONEST OUTCOME: UNDER_DETERMINED. No GU-native lever fixes p-q mod 8. The shiab, chirality, anomaly-freedom, and the RS anchors are all signature-AGNOSTIC (verified: shiab nonzero in both Cl(9,5)=M(64,H) and Cl(7,7)=M(128,R); omega^2=+I for q=5 and q=7; anchors bare_comm=58.7215/C2=155.3625/ker=1664 byte-identical across signatures). The ONLY mover of p-q across the H/R boundary is the base Lorentzian metric-sign convention -- and the DeWitt/Frobenius fiber form is convention-INDEPENDENT ((6,4) for mostly-plus AND mostly-minus), so mostly-plus (3,1)->(9,5) p-q=4 while the physically-identical mostly-minus (1,3)->(7,7) p-q=0. Signature is a DECLARED CHOICE; canon C-04 CONFIRMED; C-07 wall GENUINELY CONDITIONAL. FORCES_7_7 NOT warranted -- the count does not reopen. No target imported."
grade: "exploration / strong. Four independent GU-native angles (anomaly-freedom, H-structure/shiab, Clifford reconstruction, under-determination adversary) each return UNDER_DETERMINED and survive adversarial scrutiny (gu_native, not imported, sound). Load-bearing computations reproduced independently: fiber form (7,3) raw / (6,4) trace-reversed for every base convention; total (9,5) vs (7,7) from base sign only; closed form p-q=d+d^2/2, d=+-2; eta=[1]*9+[-1]*5 hardcoded, J^2 reads it back (circular). Honest limitation: the 'no GU selector for the base sign' claim is an absence-of-forcing argument, not a proof no selector could exist -- but the burden is on FORCING (9,5), and no forcing is exhibited anywhere in the reconstruction. One reality-sensitive channel (2-primary Witten Z/2) remains OPEN, but it is asymmetric (could EXCLUDE H, never FORCE it), so it cannot flip the verdict toward FORCES_9_5."
depends_on:
  - canon/no-go-quaternionic-parity-generation-sector.md
  - canon/shiab-existence-cl95.md
  - explorations/anomaly-and-bordism/n1-signature-audit-y14-clifford-algebra-2026-06-22.md
  - canon/multiplicity-theorem.md
scripts:
  - scratchpad/verify_fiber.py
  - scratchpad/verify_total.py
  - tests/generation-sector/gen_sector_bridge.py
  - tests/internal-paths/anomaly_sp64.py
---

# (9,5)-vs-(7,7) decide-tournament: is the Y^14 signature FORCED by GU-native structure?

## The swing

The C-07 quaternionic-parity no-go (`canon/no-go-quaternionic-parity-generation-sector.md`) is the
program's structural wall against an odd generation count: given the quaternionic real form
`Cl(9,5) = M(64,H)` (`p-q = 4 mod 8`, antiunitary `J` with `J^2 = -1`), Kramers' theorem forces every
GU-native self-adjoint carrier to have **even** signature, so an odd index such as 3 is obstructed. But
the wall is only as firm as the signature that seeds it. Under the defensible alternative
`Cl(7,7) = M(128,R)` (`p-q = 0 mod 8`, `J^2 = +1`) Kramers does not apply, and an odd real index is
unobstructed. So the decidable, target-free question is:

> **Does GU-native structure FORCE `p-q = 4 mod 8` (H-class, wall holds), FORCE `p-q = 0 mod 8`
> (R-class, wall dissolves, count reopens), or fix neither (declared input, wall conditional)?**

Grade exactly one of FORCES_9_5 / FORCES_7_7 / UNDER_DETERMINED, without importing the answer -- i.e.
without assuming (9,5) to hold the wall or (7,7) to dissolve it, and without using `J_quat`/the
H-structure to derive the signature (`J` is the *consequence* of `p-q=4`, so that move is circular).

**Honest outcome: UNDER_DETERMINED.** No GU-native lever fixes `p-q mod 8`. This confirms canon C-04
("the metric signature 9-5 = 4 is a declared structural INPUT, not a derived invariant") and leaves the
C-07 wall **genuinely conditional** -- neither unconditional nor dissolved. The generation count does
**not** reopen: a FORCES_7_7 verdict is extraordinary and is not met, because (7,7) is *admissible but
not forced*.

---

## Where the signature enters (single point of entry)

Everything downstream inherits the signature from one place: `shiab-existence-cl95.md` Step 1
(lines 29-31), promoted from the N1 signature audit. The chain is:

- `Y^14 = Met(X^4)` = bundle of Lorentzian metrics over spacetime `X^4`.
- Horizontal/base directions carry the tautological base signature `(3,1)`.
- Vertical/fiber directions are `Sym^2(T*_x X^4)` (dim 10) with the trace-reversed Frobenius/DeWitt
  metric = `(6,4)`.
- Total = `(3+6, 1+4) = (9,5)` => `Cl(9,5) = M(64,H)` => `J^2 = -1`.

`p+q = 14` is rigid (`4` base `+ 10` fiber; spinor `2^7 = 128`; `ker(Gamma) = 1664` across all nine
signatures swept). **`J^2` is fixed entirely by `(p-q) mod 8`** via real Clifford / Bott periodicity:
`{4,5,6} -> M(.,H)` quaternionic, `J^2 = -I`; `{0,1,2} -> M(.,R)` real, `J^2 = +I`. So the whole
question reduces to: **what, if anything, GU-native fixes `p-q mod 8`?**

No operator-algebra file re-derives it. `step7_integer_freeness.py` merely reads
`tr(sign(e_a^2)) = 9-5 = 4` back off already-chosen gammas (circular -- exactly what C-04 flags). In
code the class is pinned only by a hardcoded sign vector `eta = [1]*9 + [-1]*5`
(`absorbed/gu-source-action/lib/gu_bridge.py:49`; also `gen_sector_bridge.py`, `signature_sweep_fast.py`).
`shiab-existence-cl95.md` line 70 itself flags the "Signature uncertainty ... `Cl(7,7) = M(128,R)` ...
a defensible parallel."

---

## Four GU-native angles, all signature-AGNOSTIC

Each angle was pushed as its own prove-or-break determination and survived adversarial scrutiny
(GU-native, not imported, sound). All four return UNDER_DETERMINED.

### Angle 1 -- anomaly-freedom / chiral field content

Requiring anomaly-free chiral fermion content does **not** select the reality class.

- `omega = e_1...e_14` has `omega^2 = +I` in BOTH `(9,5)` and `(7,7)` (both `q` odd), so the chiral
  splitting `S = S^+ (+) S^-` exists in either class -- chirality does not privilege H.
- Net chirality `-13 = C(14,0) - C(14,1)` and `dim S = 128 = 2^7` are signature-independent.
- The decisive physics point: the `D=14` perturbative anomaly is order `Tr F^8` (an **even** symmetric
  Casimir), which does **not** vanish for real/pseudoreal reps -- unlike the `D=4` `Tr F^3` (odd cubic
  `d`-symbol) that vanishes for (pseudo)real reps and **would** discriminate reality class. So
  perturbative cancellation is reality-class-blind here.
- `tests/internal-paths/anomaly_sp64.py` (43 asserts, exit 0): the odd-primary Dai-Freed arena
  `Omega^Spin_15(BSp(n))` has **no odd torsion for every `n`** (content-independent); the local `I_16`
  gravitational channel is nonzero only via an *assumed* truncated content and is computed **on** the
  `Sp(64) = H`-commutant `(9,5)` reading (uses it, does not derive it); the reality-sensitive 2-primary
  Witten channel is left OPEN.

Anomaly-freedom is a consistency **filter** *inside* an already-chosen class, not a **selector**
between classes -- it can only render a class inconsistent (exclude it), never single one out. Both
classes admit anomaly-free content, so: **UNDER_DETERMINED.** Note the asymmetry -- if the open
pseudoreal Witten `Z/2` channel ever bit, it would **exclude** H, never **force** it.

### Angle 2 -- H-structure / shiab

GU's fixed H-structure does **not** require the quaternionic class; it is a *consequence* of it.

- The shiab Clifford-contraction is a nonzero, real-linear, equivariant map in BOTH
  `Cl(9,5) = M(64,H)` and `Cl(7,7) = M(128,R)` (n1-audit s7 table: "Shiab exists? Yes/Yes," both
  complexification-free; `shiab-existence-cl95.md` Known Failure Modes: "`Cl(7,7)` ... a different but
  parallel construction"). The construction uses only interior product + Clifford multiplication,
  neither of which references the real form.
- The circularity is explicit: the no-go doc states the `J_quat`-commutant **IS** the standard
  `Cl(9,5) = M(64,H)` isomorphism, and SHIAB-04 says the quaternionic right-`H`/`Sp(64)` cut is
  "contingent on the `(9,5)` signature; under a `(7,7)` alternative the real spinor has no `J` and this
  cut collapses." So `J` is downstream of `p-q=4`; using it to derive `(9,5)` assumes the conclusion.

**Reproduced:** an antilinear `J` commuting with the whole rep has `J^2 = -1` **only** in `(9,5)` and
`J^2 = +1` **only** in `(7,7)`, while the shiab contraction is nonzero in both. The H-structure carries
no forcing power: **UNDER_DETERMINED.**

### Angle 3 -- the Clifford reconstruction and the RS anchors

Is `Cl(9,5) = M(64,H)` a *derived* consequence of GU-native data, or a *chosen* reconstruction? The RS
anchors cannot tell.

- The bridge's advertised fingerprint -- `bare ||[Pi_RS, M_D]|| = 58.7215`, `C2 = 155.3625`,
  `rank(Gamma) = 128`, `ker = 1664` -- is **byte-identical** across `(9,5), (7,7), (10,4), (8,6),
  (5,9), (11,3)`. These are Frobenius norms invariant under the sole real-vs-quaternionic difference
  `G_a -> i*G_a`, so they *provably* cannot separate M(64,H) from M(128,R).
- The class is set only by the hardcoded `eta = [1]*9 + [-1]*5`; `Jsq` reads that same `eta` back into
  `Phi(U) = sum_a eta_a e_a U e_a* / N`, so `J^2` tracks `p-q mod 8` *by construction* and derives
  nothing (the C-04 circularity).

**UNDER_DETERMINED.** The reconstruction does not force the signature -- it hardcodes it.

### Angle 4 -- under-determination adversary (the one lever that moves p-q)

Trying hard to find *any* GU-native forcing, the only structure that moves `p-q` across the H/R
boundary is the **base Lorentzian metric-sign convention** -- and that convention is physically vacuous.

Reproduced numerically (`scratchpad/verify_fiber.py`, `verify_total.py`):

| base | raw Frobenius fiber | trace-reversed fiber | total | p-q mod 8 | class |
|------|--------------------:|---------------------:|------:|----------:|-------|
| (3,1) mostly-plus  | (7,3) | (6,4) | **(9,5)** | 4 | M(64,H), J^2=-1, wall HOLDS |
| (1,3) mostly-minus | (7,3) | (6,4) | **(7,7)** | 0 | M(128,R), J^2=+1, wall DISSOLVES |

The DeWitt/Frobenius fiber form
`B(h,k) = tr(g^-1 h g^-1 k) - 1/2 tr(g^-1 h) tr(g^-1 k)` is **quadratic in `g^-1`**, hence invariant
under `g -> -g`: the fiber signature is `(6,4)` for **both** base orientations. Trace-reversal moves
*within* a class (raw `(7,3)` -> `(10,4)`/`(8,6)`, `p-q = 6`/`2`), **never across** it. Only the base
pullback (linear in `g`) carries the sign. Closed form:

> `p-q = d + d^2/2`, with `d = (#space - #time)` in the base. `d = +2` (mostly-plus) -> `p-q = 4`
> (quaternionic); `d = -2` (mostly-minus) -> `p-q = 0` (real).

So the entire H/R decision -- the decision on which the C-07 wall hinges -- rests on `sign(d)`:
mostly-plus vs mostly-minus. These describe **identical physics** (the textbook `Cl(3,1) = M(4,R)` vs
`Cl(1,3) = M(2,H)` split), and the observerse -- *the space of metrics* -- carries **no preferred
metric-sign / timelike-norm sign** (distinct from time-orientation, which does not fix the convention).
There is no GU-native selector for `sign(d)`. **UNDER_DETERMINED.**

The Weinstein UCSD April 2025 transcript `[00:43:04]` declares only the **fiber** move
`(7,3) -> (6,4)` via trace-reversal on a mostly-plus `(3,1)` base; the total `(9,5)` is the repo's
inference from *adding* `(3,1)`. Some earlier presentations / repo N2 use a split `Spin(7,7)` -- genuine
source non-univocality, not a derivation.

---

## Verdict

**UNDER_DETERMINED.** Four independent GU-native angles -- anomaly-freedom, H-structure/shiab, the
Clifford reconstruction, and the under-determination adversary -- each fail to fix `p-q mod 8`, and each
survives adversarial scrutiny as GU-native and not-imported. The shiab, chirality, anomaly-freedom, and
the RS anchors are all signature-agnostic; the only mover is the base metric-sign convention, which is a
physically vacuous mostly-plus/mostly-minus choice with no GU selector. **Canon C-04 is CONFIRMED:** the
`9-5=4` signature is a declared structural input, not a derived invariant.

**FORCES_7_7 is NOT warranted.** A "count reopens" verdict is extraordinary and requires airtight
GU-native evidence pinning `p-q = 0 mod 8` as a **forced output**. What we have instead is *symmetric*
under-determination: `(7,7)` is admissible but not forced, because mostly-minus is no more GU-native
than mostly-plus. Neither the wall-holds branch nor the wall-dissolves branch is GU-forced.

---

## Implication for the C-07 wall and the count

- **The C-07 wall is GENUINELY CONDITIONAL** -- neither unconditional nor dissolved. As a *conditional*
  it is airtight: given `(9,5)`/H-class, Kramers forces even signature and an odd count is obstructed;
  under `(7,7)`/R-class the pairing does not apply and an odd real index is unobstructed. Its truth-value
  is inherited entirely from a declared convention. The no-go doc's 2026-07-03 signature caveat --
  "forces EVEN is conditional on the `(9,5)`/H-class reconstruction, not signature-universal" -- is
  correct and should stand.
- **The generation count does NOT reopen.** Reopening requires FORCES_7_7, which is not established. The
  count remains where canon already places it: **located, not forced.** No external check is triggered.
- This is a "located, not forced" result: the wall is exactly as firm as the standard `(3,1)`
  mostly-plus base convention -- natural and conventional, but a choice, not a GU-derived invariant.

---

## Next steps

1. **Hunt for a base-convention selector.** Search GU-native structure for anything distinguishing
   mostly-plus `(3,1)` from mostly-minus `(1,3)` beyond time-orientation -- a sign in the observerse
   tautological structure, the Shiab source term, or the RS constraint that is *not* invariant under
   `g -> -g`. This is the only remaining lever; if it carries no sign, UNDER_DETERMINED is final.
2. **Compute the 2-primary Witten / global Dai-Freed anomaly** (the one open, reality-sensitive channel
   in `anomaly_sp64.py`) for GU's actual content. Note its asymmetry: a nonzero pseudoreal `Z/2` anomaly
   would **exclude** H (push toward `(7,7)`/dissolution), never force H. It can only move the verdict in
   the dissolving direction, never toward FORCES_9_5.
3. **Resolve source univocality with the author.** Establish whether `(3,1)` mostly-plus is a
   load-bearing GU commitment or an expository choice (transcript `[00:43:04]` declares only the fiber
   move; the total `(9,5)` is the repo's inference; earlier N2 material uses split `Spin(7,7)`). This
   clarifies which convention canon should declare -- it cannot upgrade the verdict to a GU-native
   forcing.
4. **Hold the line.** Keep the C-07 signature caveat; do not strengthen the no-go to unconditional; keep
   C-04 as the standing stance. Record this decide-tournament as an exploration confirming C-04 by four
   independent GU-native angles.
5. **De-circularize the pipeline.** Flag (do not edit canon) that `gen_sector_bridge` /
   `signature_sweep_fast` compute `J^2` by reading back the hardcoded `eta = [1]*9 + [-1]*5`, so any file
   asserting `J^2 = -1` is asserting the `(9,5)` input, not deriving it -- to keep the circularity from
   being mistaken for a derivation in future audits.

---

## Verifier's note (main-loop review, 2026-07-04)

Synthesis of an 18-agent ultracode decide-tournament (`wf_0607c162-c31`; 1 non-fatal error -- one scope-angle
agent hit the schema retry cap, so scope ran on two of three reads). Main-loop honesty review:

- **Independently re-verified (holds):** the closed form `p-q = d + d^2/2` -- base `d=+2` (mostly-plus (3,1))
  gives `p-q=4` -> `(9,5)`/`M(64,H)`/`J^2=-1`; base `d=-2` (mostly-minus (1,3)) gives `p-q=0` ->
  `(7,7)`/`M(128,R)`/`J^2=+1`. And the **circularity is real**: `eta = [1]*9 + [-1]*5` is hardcoded in
  `tests/generation-sector/gen_sector_bridge.py` (at line ~35; the doc says line 49 -- a minor line-ref slip,
  substance holds), and the Hermitian gammas are built from it, so any `J^2` computed from these gammas is
  **reading back the declared `(9,5)` input, not deriving it**. This is the crux: the signature is an INPUT.
- **The verdict is the right one.** UNDER_DETERMINED, not FORCES_7_7: `(7,7)` is *admissible* but not *forced*
  (mostly-plus is equally valid, physically identical, with no GU-native selector distinguishing the base
  sign). So the count does **not** reopen -- reopening would need a sound GU-native derivation forcing
  `p-q=0 mod 8`, which is not exhibited. This confirms canon **C-04** (signature is a declared input) and the
  existing 2026-07-03 signature caveat on `canon/no-go-quaternionic-parity-generation-sector.md` -- both
  correct, both should stand. **No canon edit made** (the caveat already says exactly this).
- **Honest limitations (as the doc states):** "no GU selector for the base sign" is an absence-of-forcing
  argument, not a proof none could exist -- but the burden is on FORCING `(9,5)`, and none is exhibited
  anywhere. One reality-sensitive channel (the 2-primary Witten/Dai-Freed `Z/2`) stays OPEN, but it is
  asymmetric -- it could EXCLUDE the H-class (tending toward dissolution), never FORCE it -- so it cannot flip
  the verdict toward FORCES_9_5. Scripts were scratchpad-only.

**Bottom line (main-loop concurrence):** UNDER_DETERMINED is right and completes the arc. The C-07 wall is
**genuinely conditional** -- exactly as firm as the standard `(3,1)` mostly-plus convention, which is natural
but is a choice, not a GU-derived invariant. The generation count stays **located, not forced**; it neither
firms to "even" nor reopens to "odd". No target imported.
