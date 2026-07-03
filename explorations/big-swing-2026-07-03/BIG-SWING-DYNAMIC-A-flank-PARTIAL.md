---
artifact_type: exploration
status: exploration
created: 2026-07-03
title: "DYNAMIC_A big swing (Branch 2B, the last un-probed flank): does making the RS/IG connection A a genuine dynamical field (D_A Phi_tau != 0) move the generation anomaly onto the tangential base B(Spin(4)-frame) -- where the order-3 e_R=1/12 is GU-FORCED, not K3-imported -- and can that bear on an integer count? HONEST OUTCOME: PARTIAL, trending BLOCKED. DYNAMIC_A is the FIRST genuinely non-BSp(64) flank and the located base does carry e_R=1/12 as a real computed property, but (i) both concrete attempts to show DYNAMIC_A FORCES that base were REFUTED on GU's verified Cl(9,5) carrier -- the actual RS current is parity-symmetric with net self-dual frame charge exactly 0, and the DYNAMIC_A proxy current's forcing signal sign-flips across sections and is indistinguishable from random-operator noise -- and (ii) the count leg is provably DEAD (eta=0 constant, spectral flow 0, the triplet is vectorlike, Hom(Z/3,Z)=0). Base-forcing is plausibly-forcing-but-UNBUILT/refuted-as-demonstrated, gated on the stabilized action GU does not supply; the count is not shown. NO target imported."
grade: "exploration / PARTIAL (trending BLOCKED). The distinguishing achievement is real and target-free: DYNAMIC_A is the only flank where the 3-carrying base is GU-native rather than K3-imported, and the DECOUPLE discriminator correctly separates it from FIXED_ALEPH/BSp(64) in principle. But the affirmative claim -- 'DYNAMIC_A forces the tangential base' -- did NOT survive verification: on the verified carrier the RS current carries net self-dual frame charge 0, the BRST anomaly current is parity-symmetric (self-dual = anti-self-dual to 16 digits, base_forced=BSp(64)), and the only positive proxy signal (net_SD ~0.8 on one seed) sign-flips across sections and sits at the random-noise floor. The count leg is dead by three independent verified facts (homotopy-fixed e_R, vectorlike triplet, Hom(Z/3,Z)=0). Standing: base-forcing NECESSARY-BUT-NOT-SUFFICIENT and unbuilt; count NOT produced."
depends_on:
  - explorations/big-swing-2026-07-03/R2-sm-boundary-mod3-arena-empty.md
  - explorations/big-swing-2026-07-03/R4-two-arena-rep-theory-core.md
  - explorations/big-swing-2026-07-03/R1-rs-operator-residual-and-odd-count-nogo.md
scripts:
  - scratchpad/locator_adversary.py
  - scratchpad/brst_base_reader.py
  - scratchpad/refute_locator.py
  - scratchpad/verify_dynamic_a.py
---

# DYNAMIC_A big swing: does making the RS connection dynamical force the order-3 tangential base, and can that force a count?

**The swing.** Every prior flank of the generation-count program parks the anomaly on Route 2's bordism
target `Omega^Spin_15(BSp(64))`, which is **2-primary / 3-free**: it treats the RS/IG connection `A` as a
**fixed map** into a classifying space and is therefore **blind** to the `Z/3 <= pi_3^s = Z/24` where the
program's CRT split says a count could hide. `DYNAMIC_A` (a.k.a. Branch 2B) is the one logical possibility
that escapes this: if `A` is a **genuine dynamical field** integrated over in the action -- not a fixed
background (`nabla_aleph`) nor gauge-redundant (full-IG) datum -- then the tau constraint
`Phi_tau = beta - beta_0(epsilon,s,A)` obeys `D_A Phi_tau != 0`, the connection equation of motion picks up a
multiplier/source current, and the anomaly **moves off `BSp(64)` onto the tangential base
`B(Spin(4)-frame)`** -- the `RP^3 = L(2;1)` spine of the metric fiber with its self-dual `Lambda^2_+`
framing, where the order-3 class `e_R = p_1/48 = 1/12` is **GU-FORCED by `(S,S)=0`**, not a target-fitted
`chi(K3)=24` import. This is the only flank where the 3-carrying base is native. The home-run prize:
show `DYNAMIC_A` forces that base **and** that this bears on an actual integer count.

**Honest outcome: PARTIAL, trending BLOCKED.** Two things are true and must be held apart.

1. **The arena is real and distinct.** `DYNAMIC_A` is the **first genuinely non-`BSp(64)` flank**. The
   located base `B(Spin(4)-frame)` genuinely carries `e_R = 1/12`, whose additive order in `Q/Z` is `12` and
   whose 3-primary part is `3` -- verified live, computed as a property of the base, never inserted. The
   DECOUPLE discriminator (`co-variance = 0` for a fixed map vs non-zero for a dynamical `A`) is the correct
   test for which base the anomaly lands on, and it does separate `DYNAMIC_A` from `FIXED_ALEPH`/`BSp(64)`
   **in principle**.

2. **But the forcing was refuted, and the count leg is dead.** Both concrete attempts to show `DYNAMIC_A`
   *forces* the tangential base **failed adversarial verification on GU's verified `Cl(9,5) = M(64,H)`
   carrier**, and no attempt produced an integer count. The base-forcing claim is therefore
   **plausibly-forcing-but-UNBUILT** (gated on the stabilized action GU does not supply) and, in its two
   concrete proxy forms, **refuted**. This is `NECESSARY-BUT-NOT-SUFFICIENT` -- and not even shown.

The two grades the program insists on keeping separate:

- **(i) forcing the tangential base** -- *the arena is right; the forcing is unbuilt/refuted-as-demonstrated.*
- **(ii) producing an integer count** -- *dead.* `eta = 0` constant over the whole `A`-loop, spectral flow
  `0`, the located `j=1` triplet is **vectorlike** (net chiral index 0), and `Hom(Z/3,Z) = 0`.

Never conflate "the base carries `e_R = 1/12`" (grade i, necessary, and here only *plausible*) with "the
count is 3" (grade ii, dead).

---

## Certificate 0 -- the load-bearing number theory, verified live and target-free (`verify_dynamic_a.py`)

Before any carrier construction, the arithmetic backbone was reproduced standalone, so the report rests on
computed facts, not asserted ones. All outputs below are from a fresh run (exit 0):

- `e_R = p_1/48 = 1/12` (Kirby-Melvin `p_1 = 4`). **Additive order in `Q/Z` = 12.** **3-primary part of the
  order = 3; 2-primary part = 4.** The `3` is read as the odd part of a computed rational's order -- a
  **locator**, never an inserted or divided-by count.
- `Hom(Z/3, Z) = 0`: the only `a in Z` with `3a = 0` is `a = 0`. So a nonzero class in `Z/3` detects
  information **mod 3** and **cannot equal any integer**. No map bridges the absolute torsion class to a
  count.
- **Negative control:** the charge-`q` Dirac `eta = (2q^2 - 4q + 1)/8` is **2-primary for every integer
  `q`** (`q = -3..4` all give denominator a power of 2). The order-3 burden therefore sits **only** in the
  gravitational framing channel `-p_1/24`; it **cannot leak** from the gauge/Dirac side.
- `pi_3^s = Z/24 = Z/8 (+) Z/3` by CRT (`gcd(8,3)=1`). The `Z/3` summand is where the whole hope lives, and
  it is CRT-disjoint from the 2-primary `Z/8` that carries the Dirac data.

This certificate is clean: it establishes the arena exists and is order-3, and simultaneously proves
(via `Hom(Z/3,Z)=0`) that living in it is **not** the same as producing a count of three. It imports
nothing.

---

## Certificate A -- LocatorTrapAdversary: the forcing signal is section-dependent noise (`locator_adversary.py`, `refute_locator.py`)

**Object.** On GU's verified `Cl(9,5) = M(64,H)` carrier, model the DYNAMIC_A multiplier current as
`J = Q[M(xi), S]Pi` (a structural stand-in for the true `D_A Phi_tau`, which needs the unbuilt
`S_IG^susy`), and ask the DECOUPLE question: does `J` carry a **net self-dual tangent-frame charge**
`net_SD = frame_charge(J, Lambda^2_+) - frame_charge(J, Lambda^2_-)`? A non-zero, robust `net_SD` would mean
`J` couples to the `-p_1/24` gravitational channel -- the **only** route to an order-3 `eta` -- and hence
forces the tangential base, excluding the frame-blind `BSp(64)`.

**What the single-seed run reported (grade-i, weakly positive).** Co-variance `253.77` (dynamical `A`) vs
`0` (fixed map): the DECOUPLE test does distinguish DYNAMIC_A from FIXED_ALEPH. And `net_SD(J) = 0.8079` on
the `rand_herm_0` section vs `net_SD(D_RS) = 0.0000` and a hand-built control `33.94`. Read charitably, this
is a small (~2.4% of the control) tangent-frame charge, i.e. a *plausible* base-forcing signal.

**Why it does not survive (the refutation, reproduced live).** A robustness sweep over many random Hermitian
sections `S` (`refute_locator.py`, exit 0) shows the "signal" is **not a certificate**:

```
net_SD(D_RS)=0.0000   net_SD(Lambda^2_+ ctrl)=33.9411
DECOUPLE sweep, net_SD(J) per S over the A-loop:
  S=rand_herm_0   range=[ 0.4554, 1.6425]  mean= 1.0397   frac_of_ctrl=[1.34%, 4.84%]
  S=rand_herm_1   range=[-6.0935,-4.9327]  mean=-5.5045   frac_of_ctrl=[14.53%,17.95%]
  S=gamma_built   range=[ 0.0000, 0.0000]  mean= 0.0000
Null baseline (random hermitian op, no dynamics): range=[-0.7165, 1.4631] mean=0.4441
```

Three facts kill the forcing claim: (1) **`net_SD(J)` sign-flips** with the section (positive on
`rand_herm_0`, negative on `rand_herm_1`, zero on `gamma_built`) -- there is no consistent self-dual
preference; (2) its magnitude is **indistinguishable from the null baseline** of a generic random operator;
(3) the **actual RS operator** on the verified carrier has `net_SD(D_RS) = 0` **exactly** -- only the
hand-built `Lambda^2_+` control (a datum GU does not supply) carries `33.94`. So the advertised `0.8079` is a
**hand-picked single-seed residual at the noise floor**, not a quantized, `S`-independent, topological
certificate. Co-variance `253.77` is separately **tautological** (varying `xi` trivially varies `J(xi)`).

**And the count leg is dead regardless.** Across every section the net chiral index `eta = 0`, constant over
the entire `A`-loop, and the torsion-free rank home (spectral flow) is also identically `0` -- even under a
chirality-*breaking* current and a purely cross-chirality vectorlike current. There is no integer that is
(a) nonzero, (b) in a rank home, and (c) geometry-co-varying. The `+/-` pairing survives, matching the R1
Dirac-mass wall.

**Verdict:** PARTIAL. Honest as a **locator** (never inserts/divides by 3/8/24/chi/Ahat; keeps grade i and
grade ii on separate ledgers; self-grades PARTIAL and states "necessary-not-sufficient"), but **refuted as a
route to forcing** and **dead as a route to a count**.

---

## Certificate B -- BRST base-reader: the verified carrier's anomaly is parity-symmetric, base = BSp(64) (`brst_base_reader.py`)

**Object.** Read which classifying space the DYNAMIC_A **consistent anomaly** descends from by measuring the
self-dual (`su(2)_+`) vs anti-self-dual (`su(2)_-`) content of the anomaly current on the verified `Cl(9,5)`
data. Transgression from the tangential `B(Spin(4)-frame)` requires a **self-dual-selective** current.

**Result (decisive control 1b, reproduced, exit 0).** The DYNAMIC_A anomaly current on the verified carrier
is **exactly parity-symmetric**: `self-dual su(2)_+ = anti-self-dual su(2)_- = 5.4134583754e-02`, identical
to ~16 digits and statistically `~` a random `so(4)` current (`5.38e-02`). So `self_dual_selective = False`
and **`base_forced = BSp(64)`, NOT the tangential base.** The current stays `ad(Sp(64))`-valued and does
**not** transgress the self-dual `Lambda^2_+` base. The tangential base appears **only** under hand-inserted
**case C** -- a V-acting self-dual frame connection forced into the RS Dirac by hand, ratio `~0.51` --
which is a **convention of the unbuilt (author-disclaimed, quarantined eq 10.10) action**, not GU data.

**Structural root cause (in-repo metatheorem).** `tests/gu-independent/structural_frame_triviality_metatheorem.py`
proves the net-chiral functional `Tr(Gamma . P)` uses spinor chirality `Gamma = id_V (x) gamma` and is
**trace-orthogonal (blind)** to every `so(4)` tangent-frame-charge component. The frame's only `+/-` grading
that the chiral count can see is the Hodge SD/ASD split on `Lambda^2_+` -- which is exactly the
**vectorlike `+96/-96` order-3 carrier** (net chiral index 0). This is why Certificate A's DECOUPLE
"success" (`net_SD != 0`) is precisely the channel that **structurally cannot source a chiral count**, and
why the same run yields `eta = 0`.

**Verdict:** BLOCKED. An honest **self-negative**: the verified carrier's own data does **not** force the
tangential base (it is `ad(Sp(64))`-valued/parity-symmetric); the flip requires a hand-inserted convention;
and no code path maps base -> integer (`integer_count` hard-coded UNBUILT). No target imported.

---

## Mapping onto the five firewall criteria

- **(1) Closed completion exists?** **NO.** The single load-bearing object -- a stabilized `S_IG^susy` on
  `Y14 = Met(X4)` -- does not exist in GU. Eq 10.10 is author-disclaimed ("Caveat Emptor") and
  repo-quarantined (`QUARANTINED_UNDERDEFINED_ZERO_ACCEPTED_RS_RECEIPTS`); the 2021 draft emits no
  action/operator/Noether/BRST rule. Every DYNAMIC_A statement is conditional on this unbuilt object. This
  is **WEAK-form evidence only**, never POSITIVE form.
- **(2) Boundary removable?** N/A here -- there is no closed reconstruction to delete a boundary from; the
  object is missing, not adaptered.
- **(3) Alternative completion reproduces the physics?** Consistent with the standing **Multiplicity
  Theorem**: GU fixes one-generation **structure** (Pati-Salam verified) but not **multiplicity**; the whole
  internal spectrum is `{2,7,13}`-smooth and every metric-connection index is `0`. DYNAMIC_A does not change
  this.
- **(4) Artifact of choices?** The base-flip to `B(Spin(4)-frame)` **is** an artifact of a choice -- of
  "what `A` includes" (case C, a V-acting self-dual connection). This is the standing rep-canonicity caveat
  (the `d_A` notation is ambiguous; `D_A Phi_tau != 0` holds but is **frame-free / isotropic-valued** on the
  verified carrier).
- **(5) Physics survives boundary rejection?** **YES.** SM, QM, and one-generation structure remain
  derivable; DYNAMIC_A is an escape *hatch* for the count, not a load-bearing part of the physics
  derivation. Rejecting it costs nothing already-derived.

**Net firewall standing.** STRONG form is **CONFIRMED DEAD** (criterion 4 landed via the C-07
quaternionic-parity wall being a `(9,5)` H-class artifact). WEAK form **SURVIVES**. DYNAMIC_A is the
**surviving WEAK-form evidence** -- the one flank whose 3-carrying base is GU-forced not K3-imported -- but
it is **itself external in the operative sense**: BLOCKED on the unbuilt action, and its two concrete
forcing attempts are refuted. It is **not** support for the POSITIVE form (GU pins neither the base nor the
value).

---

## The trap, stated sharply for this flank

`e_R = 1/12` **locates** the unique CRT-disjoint `Z/3` arena but **cannot be pushed to an integer 3**, for
three independent verified reasons:

- **(a) Homotopy-fixed.** `e_R = 1/12` is a fact about `pi_3^s`, **identical** for a universe with one
  generation or five; it cannot co-vary with the answer.
- **(b) Vectorlike.** The located `j=1` triplet carries a purely cross-chirality Krein form, net chiral
  index `0` -- it marks the slot without filling it. (Confirmed: `eta = 0`, spectral flow `0`, on every
  section and under chirality-breaking currents.)
- **(c) Algebraic category error.** `Hom(Z/3, Z) = 0` (verified live). A nonzero class in `Z/3` detects
  information **mod 3**; it is not equality to an integer. Contrast `Hom(Z,Z)`: an integer count, if it
  exists, can only live in a **RELATIVE / RANK (torsion-free)** home -- integer-valued by construction yet
  geometry-dependent -- which no toy on this carrier has produced (all yield 2-primary values or 1).

**Forbidden moves not taken:** `ind_H(D_RS) := 8` (target import) and `8/Ahat(K3) = 8/2 = 4`
(`INVALID_TARGET_DIVISION`) were never used; nothing was divided by `3, 8, 24, chi(K3)=24, Ahat, rank_H, 8`.
The `3` appears exactly once, as the odd part of the order of a computed rational.

---

## What this settles, and what it does not

**Settles (this swing).** DYNAMIC_A is the **first genuinely non-`BSp(64)` flank**, and that is a real,
distinct finding: the DECOUPLE discriminator correctly identifies it as the only branch whose anomaly could
land on the order-3 tangential base rather than the 3-free `BSp(64)` target. But the affirmative claim
"DYNAMIC_A **forces** that base" **does not survive verification on GU's verified `Cl(9,5)` data**: the RS
current's net self-dual frame charge is `0`, the BRST anomaly current is parity-symmetric (`base = BSp(64)`),
and the only positive proxy signal sign-flips across sections at the noise floor. The forcing is therefore
**plausibly-forcing-but-UNBUILT** (gated on the stabilized action) and, concretely, **refuted**. The count
leg is **dead** independently (homotopy-fixed, vectorlike, `Hom(Z/3,Z)=0`). So even the best imaginable
near-term outcome is **BASE_FORCED_NOT_A_COUNT**, never a HOME_RUN -- and we are not even at BASE_FORCED,
because the forcing is not shown.

**Does NOT settle (and no target imported).** This neither derives three nor forbids three. It removes one
more *mechanism* by which three could have been forced (a GU-native order-3 anomaly on a dynamical base) from
the "achieved" column, downgrading it to "unbuilt/refuted-as-demonstrated." The number three was never
assumed, inserted, or divided by.

**Where the wall now is.** Two hard gates, in order:
1. **The stabilized `S_IG^susy` on `Y14`** -- the single missing object. Until it exists, `J = Q[M,S]Pi` is
   a proxy and "DYNAMIC_A forces the base" is a proxy statement. This is genuine **incompleteness in
   GU-as-a-theory**, not a formalization gap.
2. Even given the action: the **external null-plane spectral section** to close `C2 = 0` (bare norm
   `155.36`; `s^2 = 0` only for the connection-2-form carrier, KSp carrier fails at `749.16`), **and** a
   **RELATIVE/RANK twisted-RS index** on `Y14` that is integer-valued and geometry-co-varying and reduces
   mod 3 to the `Lambda^2_+` carrier. No such operator or integer exists; the symbol/K-theory route
   (`ind_H = -320/-304/-336`) and the af4 rep-theory route (conditional `ind_H = 8`) currently **disagree**.

**Net verdict.** The generation count stays **OPEN / external-by-structure**. DYNAMIC_A was the one un-probed
escape and the only flank where the 3-carrying base is GU-forced rather than imported -- **but it is itself
external in the operative sense**: BLOCKED on the unbuilt action, its forcing attempts refuted, and even if
built it would be BASE_FORCED_NOT_A_COUNT, not a HOME_RUN. Complementary context: the R2 SM-boundary mod-3
route is a **KILL** (the arena is provably empty: `Omega^Spin_5(B G_SM) (x) Z_(3) = 0`), so DYNAMIC_A does
not overturn any prior result -- it closes the last affirmative hope's near-term door while leaving the
count formally OPEN.

**Not promoted.** Exploration-grade; staged under `explorations/big-swing-2026-07-03/`. Scripts live under
the session scratchpad. The generation-count verdict remains OPEN; no canon, status, or verdict flip.

---

## Verifier's note (main-loop review, 2026-07-03)

Synthesis of a 23-agent ultracode workflow (`wf_9cc93469-ba1`; 1 non-fatal agent error -- one of five design
angles failed its schema retries, so the design panel ran on four). Main-loop honesty review:

- **Independently re-checked (holds):** `e_R = 1/12` has additive order 12 in `Q/Z` with 3-primary part 3
  (a genuine, target-free property of the base -- not an inserted count); `Hom(Z/3, Z) = 0` trivially; and the
  `net_SD(D_RS) = 0` / parity-symmetric finding is consistent with R1's already-established
  `{D_RS, Gamma_15} = 0` (symmetric spectrum). The locator-not-count discipline held: the doc does **not**
  conflate `e_R = 1/12` with a count of three.
- **NOT reproduced (honest gaps, as the doc flags):** the affirmative *base-forcing* attempts were **refuted**
  on the verified carrier (RS current parity-symmetric, `net_SD = 0`; the proxy signal sign-flips across
  sections at the random-noise floor), so base-forcing is asserted-via-proxy and gated on the unbuilt
  stabilized action. The four construction scripts (`scratchpad/*.py`) were written to ephemeral scratchpad and
  **not persisted**, so their affirmative claims are not checkable from disk. The symbol/K-theory `ind_H`
  route (`-320/-304/-336`) and the af4 rep-theory route (`ind_H = 8`) **disagree** and are flagged for
  reconciliation, not resolved.

**Bottom line (main-loop concurrence):** PARTIAL / trending BLOCKED is right. DYNAMIC_A is genuinely the first
non-`BSp(64)` flank and the only one where the order-3 base is GU-native rather than K3-imported -- a real,
target-free distinction. But it does **not** force that base (as demonstrated on the verified carrier), and the
count leg is dead three ways (`e_R` homotopy-fixed, triplet vectorlike, `Hom(Z/3,Z)=0`). Even in the best case
it is BASE_FORCED_NOT_A_COUNT, never a home run. The single gate remains the stabilized RS/IG-sector action --
a genuine incompleteness in GU-as-a-theory (eq 10.10 author-disclaimed), not a formalization gap. Count stays OPEN.
