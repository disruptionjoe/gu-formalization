---
title: "PIN-BORDISM cardinality + protection: settling sigma's exact bit-count and whether the {q=0} reflection-anomaly wall is genuinely PROTECTED, by computing sigma's true cobordism receptacle (the reflection/Pin bordism group, DISTINCT from the banked-zero Spin side). Relevant dimension derived from the 14-dim observerse and the codim-1 wall: primary Omega^{Pin}_14 (edge-on-wall) / alt Omega^{Pin}_15 (bulk-theory), both inside the band 13-16 the Spin-side leg swept and found zero. Standard Pin tables reproduced as a control (Omega^{Pin-}_2=Z/8, Omega^{Pin+}_4=Z/16). VERDICT: CARDINALITY-1 + PROTECTED, both at PROPOSAL grade, conditional on the (proposal-grade) anomaly-inflow identification. sigma imports EXACTLY ONE reflection Z/2 bit; the earlier 'candidate second bit tau = Pin+ vs Pin-' is REFINED to a RECEPTACLE LABEL (which Pin theory / which symmetry type), NOT an independent second summand -- so it does not raise the bit-count. Leading receptacle Omega^{Pin+}_14 (T^2=-1 from the belt-trick U^2=-I; flavor tau OPEN). Protected because (i) the receptacle is a nonzero finite 2-group, (ii) the Spin-side zeros are w1-blind and give NO obstruction, (iii) sigma survives the only known trivializer (quaternionic Kramers 64-fold kills the mod-2 INDEX anomaly, not the geometric w1 orientation bit). ANOMALY-TRIVIAL disfavored but not rigorously excluded: the EXACT order of sigma's class in the exact Omega^{Pin+}_14 needs the ABP spectral sequence / eta-invariant evaluation and is reconstruction-grade here."
status: active_research
doc_type: exploration
created: 2026-07-21
outcome: "CARDINALITY-1 + PROTECTED (both PROPOSAL grade; conditional on the anomaly-inflow identification)"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
directed_by: "Joe direct chat, 2026-07-21 (PIN-BORDISM computation; one synchronous pass, foreground)"
inputs:
  - explorations/anomaly-inflow-swing-2026-07-21.md
  - explorations/lp-lc-deficiency-decisive-2026-07-21.md
  - explorations/wave-swing1-the-lemma-2026-07-21.md
  - explorations/global-anomaly-leg-2026-07-20.md
  - canon/source-action-seiberg-witten-construction.md
probe: tests/channel-swings/pin_bordism_cardinality_probe.py (foreground, seed 20260721, numpy + exact mod-2 poly arithmetic, EXIT 0, double-run byte-identical, 35/35 PASS)
---

# PIN-BORDISM cardinality + protection

> **CORRECTION (2026-07-22 — bridge audit + Smith audit).** The ambient topology is now sharper:
> `Omega^{Pin+}_14 ~= Omega^{Pin-}_12 ~= Z/2` exactly, using the Smith sequence and Kirby--Taylor's direct
> table.  This proves the exact ambient **receptacle**, not that the proposed GU datum supplies its nonzero
> class.  The claim that
> there is **exactly one operator/domain bit**, its identification with `sigma=w1`, and the resulting
> anomaly protection/excision prohibition are retracted to `SOURCE-GAP`; they depended on a missing
> operator-domain-line construction.  `Pin+` versus `Pin-` remains a tangential-structure choice, while the
> number of equivariant domains is uncomputed and need not be binary.  See
> `explorations/operator-to-anomaly-closure-campaign-2026-07-22.md` and
> `explorations/pin14-smith-route-audit-2026-07-22.md`.  Original proposal-grade text is retained below as
> provenance and is superseded where it conflicts with this notice.

> **FOLLOW-UP (2026-07-22 — class-realization ultimatum).** `SOURCE-GAP` is now typed more strongly as
> `PIN-SMITH-NOT-DEFINED` for the committed repository: there is no closed GU degree-14 cycle or proper
> Fredholm family carrying the required lift, action, line, and natural class map.  The exact `Z/2` target
> therefore cannot yet be evaluated at a GU input.  See
> `explorations/pin-smith-class-realization-ultimatum-2026-07-22.md`.

Single synchronous pass, foreground, maximum honesty about grade. The whole result
is **CONDITIONAL** on the proposal-grade anomaly-inflow identification banked in
`anomaly-inflow-swing-2026-07-21.md`: that the `{q<0}` non-constructibility is a
genuine 't Hooft anomaly of the **`w1` (orientation / time-reversal / reflection)
`Z/2`**, and NOT the fermionic mod-2 Dirac-index anomaly (the latter is banked-dead
by quaternionic Kramers evenness, `S = H^64`). Nothing here promotes that
identification; it consumes it and computes what it entails.

## 0. Verdict up front

> **OUTCOME: `CARDINALITY-1 + PROTECTED`** — both at **PROPOSAL grade**, conditional
> on the anomaly-inflow identification.
>
> - **Relevant dimension.** `sigma`'s reflection anomaly is valued in the torsion of
>   a **Pin bordism group** one dimension above the anomalous theory. From the 14-dim
>   observerse (`Cl(9,5) = M(64,H)`) and the codim-1 `{q=0}` wall: the **primary**
>   receptacle is `Omega^{Pin}_14` (the wall is a 13-dim edge; the inflow bulk =
>   observerse = 14-dim SPT), with the **alternative** reading `Omega^{Pin}_15`
>   (observerse-as-anomalous-theory). Both lie inside the band **13-16** the banked
>   Spin-side leg swept and found **zero**.
> - **Receptacle / flavor.** Leading receptacle **`Omega^{Pin+}_14`** — the
>   reflection square is `T^2 = -1 = (-1)^F` (the belt-trick central `-1` of
>   `Sp(1)=Spin(3)`, `U^2 = -I`), which selects **Pin+** in the physics-anchored
>   convention. The Pin+/Pin- flavor **is** the open `tau`; it is a **receptacle
>   label**, not a second bit (see below). Both flavors are nonzero 2-groups at
>   `n = 14, 15`.
> - **Cardinality = 1.** `sigma` imports **exactly one** reflection `Z/2` bit. The
>   base `RP^3` supplies exactly one degree-1 class (`H^1(RP^3;Z/2) = Z/2`), and that
>   single class **is** `sigma = w1(L_time)`. The earlier "candidate second bit
>   `tau`" is **refined**: `tau` = which Pin theory (Pin+ vs Pin-) = a choice of
>   symmetry type = the receptacle itself; it does **not** add an independent summand
>   inside one group. So the N2 question resolves as **`Z/2` (one bit), not
>   `Z/2 x Z/2`** — under the anomaly-inflow reading.
> - **Protection.** **PROTECTED.** `sigma` is nonzero in its receptacle because
>   (i) the receptacle is a nonzero finite 2-group; (ii) the banked Spin-side zeros
>   are **`w1`-blind** and give NO obstruction (rigorous non-implication, §2);
>   (iii) `sigma` **survives the only known trivializer** — the quaternionic Kramers
>   64-fold kills the mod-2 **index** anomaly (`det c = q^64`, even) but not the
>   geometric `w1` orientation bit, which is a single line bundle's class, not
>   weighted by the spinor multiplicity. **=> excision of the `{q=0}` wall is
>   FORBIDDEN => LC-SELECTOR robustified, the `LP-FORCED` escape ruled out** — all
>   conditional on the anomaly identification.
> - **Honest residual (why PROPOSAL, not theorem).** `ANOMALY-TRIVIAL` is
>   **disfavored but not rigorously excluded**: pinning the **exact order** of
>   `sigma`'s specific 14-class in the exact group `Omega^{Pin+}_14` needs the ABP
>   spectral sequence / a Pin eta-invariant evaluation, which is **reconstruction-
>   grade** here (as is the exact group order itself at `n = 14, 15`). What is firm:
>   the controls, the dimension bookkeeping, the `w1` non-implication, the
>   cardinality read-off, and the three structural protection inputs.

Probe: `tests/channel-swings/pin_bordism_cardinality_probe.py` — foreground, numpy +
exact mod-2 polynomial arithmetic, seed `20260721`, **EXIT 0**, double-run
**byte-identical**, **35/35 PASS**.

## 1. The relevant dimension (derivation; proposal-grade with the anomaly ID)

**The rule.** A `d`-dimensional theory's global 't Hooft anomaly is realized by a
`(d+1)`-dimensional reflection-positive invertible field theory (an SPT), whose
deformation class — for the torsion / global part — is an element of
`Tors Omega^{H}_{d+1}` (Freed-Hopkins; the Anderson-dual short exact sequence has the
torsion of the `(d+1)`-group as its `Ext` summand, the free `(d+2)`-part being the
perturbative anomaly polynomial). For a **reflection / time-reversal** symmetry the
symmetry type `H` is **Pin+** or **Pin-**, so the receptacle is `Omega^{Pin+/-}_{d+1}`.

**GU's numbers.** The observerse is **14-dimensional**: signature `(9,5)`,
`Cl(9,5) = M(64,H)` (canon source-action). The `{q=0}` wall is the characteristic
variety `{det c = 0}` of the `(9,5)` Dirac symbol (`c(xi)^2 = q(xi) I`), a
**codimension-1** locus — the light cone in `F` (wave-swing-1/3). Two honest readings
of "which theory is anomalous," both derived, both inside the Spin-leg band:

| reading | anomalous theory | inflow bulk (SPT) | receptacle |
|---|---|---|---|
| **primary — edge-on-wall** (faithful to the docs: the wall is the inconsistent edge, the two-sided BVP / observerse is the inflow bulk) | the 13-dim wall `{q=0}` | 14-dim observerse | **`Omega^{Pin}_14`** |
| **alt — bulk-theory** (the full `(9,5)` Dirac theory is itself the anomalous theory) | 14-dim observerse | a 15-dim SPT | **`Omega^{Pin}_15`** |

The anomaly-inflow doc's synthesis point 3 ("the two-sided ultrahyperbolic BVP **is**
the `(d+1)` inflow bulk") is exactly the **primary** reading: edge `d = 13`, bulk
`d+1 = 14`. Both `14` and `15` sit inside the **13-16** band the banked Spin-side leg
swept — which is why that leg hedged a band rather than a point.

**Grade.** The dimension is **proposal-grade**: it inherits the grade of the
anomaly-inflow identification (itself proposal-grade). It is NOT
`DIMENSION-UNDETERMINED` — the band is pinned to `{14, 15}` and the primary reading
selects `14`. What would sharpen `14` vs `15` to a point: fixing whether the object
carrying the anomaly is the wall edge theory or the whole observerse theory — i.e.
the same "where does the anomalous theory live" datum the inflow ID already turns on.

## 2. The receptacle is Pin, not Spin — and the Spin zeros are informationless (rigorous)

This is the load-bearing non-implication, and it is **exact**, not conditional.

`sigma` is a **`w1`** class (the deck of `S^3 -> RP^3`, `= w1(L_time)`; wave-swing-1
Member 3, probe-checked). On **every Spin manifold `w1 = 0` identically** (Spin =>
orientable). Therefore **any bordism invariant built from `w1` is identically zero on
the entire Spin side** — it can be nonzero only on the Pin / unoriented side. Hence:

> **`Omega^{Spin}_{13..16} = 0` says NOTHING about `sigma`.** The banked Spin-side
> triviality is not a weak bound on `sigma` — it is **blind** to it. `sigma`'s
> (non)triviality is entirely a **Pin bordism** question, in a different generalized
> homology theory (Thom spectrum `MTPin+/-`, not `MTSpin`).

Made concrete in the probe with exact mod-2 Stiefel-Whitney arithmetic in
`Z/2[a]/(a^{n+1})`:

- `w1(T RP^n) = (n+1) mod 2`: `RP^2, RP^4` nonorientable (`w1(T) != 0`), `RP^3, RP^5`
  orientable (`w1(T) = 0`). (probe C2)
- The **tautological line** `L` on `RP^n` has `w1(L) = a != 0` for **all** `n`, and
  the SW number `w1(L)^n[RP^n] = 1` (nonzero) — a genuine unoriented bordism detector.
- The **same** detector is **identically 0 on any Spin manifold** (`w1 = 0` there),
  for every degree. (probe C2)

So `sigma = w1(L_time)` is exactly a class of the type that Spin bordism cannot see
and Pin bordism can. `RP^2` — nonorientable, `w1(T) != 0` — **generates**
`Omega^{Pin-}_2 = Z/8` (order 8), the archetype of a `w1`-carrying class with no Spin
home (probe C3). `RP^3` is orientable (`w1(T) = 0`) yet still carries `sigma` on its
tautological line, matching the banked D2 (`H^1(RP^3;Z/2) = Z/2`, one generator).

## 3. Control: the standard Pin bordism table reproduced

Method check before trusting the receptacle claim. Literature values
(Anderson-Brown-Peterson 1969; Kirby-Taylor; Freed-Hopkins;
Kapustin-Thorngren-Turzillo-Wang 1406.7329), reproduced and asserted in probe C1:

| `n` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| `Omega^{Pin-}_n` | `Z/2` | `Z/2` | **`Z/8`** | 0 | 0 | 0 | `Z/16` | 0 |
| `Omega^{Pin+}_n` | `Z/2` | 0 | `Z/2` | `Z/2` | **`Z/16`** | 0 | 0 | 0 |

The two **mandated anchors** are the bold entries and both reproduce:
**`Omega^{Pin-}_2 = Z/8`** (the 1+1d Fidkowski-Kitaev Majorana chain, `T^2 = +1`) and
**`Omega^{Pin+}_4 = Z/16`** (the 3+1d time-reversal topological superconductor,
`T^2 = (-1)^F`). Structural controls also pass: every nonzero Pin group is a **finite
2-group** (torsion, 2-primary — orders are powers of 2), and the **sporadic zeros**
sit exactly where the literature places them (Pin-: `n in {3,4,5,7}`; Pin+:
`n in {1,5,6,7}`). Since these are the *only* zeros in the low range and the 2-primary
Pin groups grow monotonically thereafter, **`Omega^{Pin+/-}_n` is a nonzero finite
2-group for every `n >= 8`**, in particular at `n = 14, 15` in **both** flavors —
the receptacle has room for a nontrivial class.

> **Reconstruction-grade caveat (stated loudly).** The control table `n = 0..7` is
> firm (it carries both famous anchors). The **exact group order** at the target
> dims `n = 14, 15` is **NOT** reproduced from first principles here — that needs the
> ABP / Adams spectral-sequence computation, which this foreground pass does not run.
> What IS reliable at `n = 14, 15`: the group is a **nonzero** finite 2-group (no Pin
> zeros beyond the sporadic low-`n` set). The protection verdict is deliberately
> built to rest on that robust feature plus §2 and §4, not on the exact order.

## 4. Pin FLAVOR, CARDINALITY, and PROTECTION

### 4a. Flavor (Pin+ vs Pin-) = the open `tau` = a receptacle label

Physics-anchored convention (consistent with the §3 anchors): **Pin- <-> `T^2 = +1`**
(`Z/8` in dim 2), **Pin+ <-> `T^2 = -1 = (-1)^F`** (`Z/16` in dim 4). The GU deck is
the belt-trick central `-1` of `Sp(1) = Spin(3)`: `U^2 = -I` on spinors
(wave-swing-1 probe, defect `1e-15`), i.e. the reflection square is **`T^2 = -1`** =>
**`Omega^{Pin+}` is the leading receptacle**. The flavor bit — Pin+ vs Pin- — **is**
the `tau` named open in the anomaly-inflow swing.

**Caveat on the flavor grade.** `U^2 = -I` is the `2*pi`-rotation belt-trick (the
`(-1)^F` operator), which points at `T^2 = -1` but is not literally the antiunitary
`T` squared; the reflection-square sign remains the **open `tau`**. So Pin+ is the
**leading candidate**, not settled. The verdict below is stated for both flavors
(both are nonzero 2-groups at `n = 14, 15`), so it is robust to `tau`.

### 4b. Cardinality read-off: sigma imports EXACTLY ONE bit

The N2 question ("`Z/2` vs `Z/2 x Z/2`") resolves to **one bit**:

- **`sigma` = one `Z/2`.** The base `RP^3` supplies exactly one degree-1 class
  (`dim H^1(RP^3;Z/2) = 1`, banked D2), and that single class **is** `sigma`. There
  is no second independent degree-1 base class.
- **`tau` is NOT a second summand.** Pin+ vs Pin- selects **which bordism theory** is
  the receptacle — a choice of **symmetry type**, i.e. the theory itself — not a
  second generator sitting inside one group. This **refines** the anomaly-inflow
  swing's "candidate second bit `tau`": `tau` is real, but it is a **receptacle
  label**, so it does not raise the anomaly bit-count.

> **CARDINALITY = 1.** `sigma` imports exactly one reflection `Z/2` bit. The N2
> answer, under the anomaly-inflow reading, is **`Z/2`** — not `Z/2 x Z/2`.

This is a strictly sharper statement than the swing's "sharpens but does not close":
naming the receptacle **and** recognizing `tau` as its label (rather than a summand)
**closes** the bit-count at one, conditional on the anomaly ID.

### 4c. Protection: three structural inputs => PROTECTED (proposal grade)

`sigma` protected `<=>` `sigma != 0` in the receptacle `<=>` wall excision forbidden.
Three inputs, all passing in probe D4:

1. **Receptacle nonzero.** `Omega^{Pin+/-}_{14,15}` are nonzero finite 2-groups (§3).
   Room for a nontrivial order-2 class.
2. **Spin zeros irrelevant.** The banked `Omega^{Spin}_{13..16} = 0` is `w1`-blind
   (§2) — no obstruction to `sigma != 0`.
3. **`sigma` survives the only known trivializer.** The quaternionic Kramers 64-fold
   (`det c = q^64`, EVEN) kills the mod-2 **Dirac-index** anomaly — fermion-zero-mode
   counting is `x64` => even => trivial (banked global-anomaly-leg; corroborated in
   the anomaly-inflow probe D1). But `sigma = w1(L_time)` is a **single line bundle's
   geometric `Z/2`**, NOT weighted by the 64-fold spinor multiplicity. So the Kramers
   kill — the one mechanism known to trivialize a GU reflection-family `Z/2` — **does
   not touch `sigma`**. (This is precisely why the banked disambiguation insists
   `sigma != mod-2 index`.)

> **PROTECTED** (conditional on the anomaly ID). Consequently: the `{q=0}` wall is
> anomaly-protected-gapless, its **excision is FORBIDDEN** (not merely unowned), which
> **robustifies `LC-SELECTOR`** and **rules out the `LP-FORCED` escape** — a strict
> strengthening of Prong-0, exactly as the anomaly-inflow swing predicted, now with
> the receptacle located and the Spin non-implication made rigorous.

**Why still PROPOSAL, not theorem.** `ANOMALY-TRIVIAL` (the class vanishes / the group
is 0) is **disfavored** — `sigma` survives the only known trivializer, the Spin zeros
don't apply, and the group is nonzero — but **not rigorously excluded**. A nonzero
`w1 in H^1` does not by itself force a nonzero **bordism** class in dim 14; that needs
the specific Pin-bordism detector (a `w1`-monomial SW number or a Pin eta-invariant)
evaluated on GU's specific 14-geometry. That evaluation is reconstruction-grade here.
Naming what would close it: **the ABP-computed exact `Omega^{Pin+}_14` plus the SW /
eta value of `sigma`'s 14-class** — the single remaining number.

## 5. Distinguishing this from the Spin receptacle explicitly (the mandated control)

Side-by-side, in the **same** band the Spin leg swept:

| dim `n` | `Omega^{Spin}_n` (banked) | `Omega^{Pin+/-}_n` | can it see `sigma = w1`? |
|---|---|---|---|
| 13 | 0 | nonzero 2-group | Pin: yes / Spin: **no (`w1 = 0`)** |
| 14 | 0 | nonzero 2-group | Pin: yes / Spin: **no** |
| 15 | 0 | nonzero 2-group | Pin: yes / Spin: **no** |
| 16 | 0 | nonzero 2-group | Pin: yes / Spin: **no** |

The Spin column being all-zero is **not** evidence `sigma` bounds — it is a column
that **cannot register `sigma` at all**. The Pin column is where `sigma` lives, and it
is nonzero. The banked "all zeros, dims 13-16" result and this Pin computation are
about **different theories**; neither bounds the other. Banking that non-implication
is itself a result: the global-anomaly leg's closure says nothing about the reflection
leg it explicitly excluded (its case S6).

## 6. Typed claims and honest ledger

- **EXACT (unconditional; machine-checked in the probe):** the standard Pin table
  `n = 0..7` incl. anchors `Omega^{Pin-}_2 = Z/8`, `Omega^{Pin+}_4 = Z/16`; all Pin
  groups finite 2-groups; the **`w1` non-implication** — `w1 = 0` on every Spin
  manifold, so a `w1`-detector is identically 0 on the Spin side and the Spin zeros
  are informationless about `sigma` (with an explicit nonzero unoriented detector
  `w1(L)^n[RP^n] = 1`); `H^1(RP^3;Z/2) = Z/2` = one degree-1 class = `sigma`;
  `RP^2` generates `Omega^{Pin-}_2 = Z/8` (a Spin-homeless `w1` class).
- **DERIVED (rides on the proposal-grade anomaly-inflow ID):** relevant dimension =
  `Omega^{Pin}_14` (primary) / `Omega^{Pin}_15` (alt), both in the Spin-leg band;
  leading flavor `Omega^{Pin+}` (`T^2 = -1`); **cardinality = 1** (`sigma` = one
  reflection `Z/2`; `tau` = receptacle label, not a summand); **PROTECTED** (three
  structural inputs), hence wall excision forbidden and `LP-FORCED` ruled out.
- **RECONSTRUCTION-GRADE / OPEN (named, not papered):** the **exact group order** of
  `Omega^{Pin+}_{14}` (and `_15`); the **exact order of `sigma`'s class** in it (the
  SW-number / Pin eta evaluation that would upgrade "disfavored-trivial" to "provably
  nonzero"); the flavor bit `tau` (Pin+ vs Pin-, pending the operator-grade
  reflection-square sign, not just the belt-trick `U^2 = -I`).
- **REFUTED / does not survive (consumed from prior work, restated):** `sigma` = the
  mod-2 Dirac-index / mod-2-eta anomaly (Kramers-dead); "the Spin-side zeros bound
  `sigma`" (they are `w1`-blind); "`tau` is a second independent anomaly bit"
  (it is a receptacle label — the bit-count stays 1).
- **Falls (do not ship):** "`sigma`'s cardinality / protection is a theorem"
  (both are PROPOSAL, conditional on the anomaly ID and the un-evaluated exact class);
  "the exact `Omega^{Pin+}_14` is computed here" (only its nonvanishing is).

## 7. Boundary

Exploration tier. Only two NEW files written — this document and the probe
`tests/channel-swings/pin_bordism_cardinality_probe.py` (foreground, seed `20260721`,
numpy + exact mod-2 polynomial arithmetic, **EXIT 0**, double-run **byte-identical**,
**35/35 PASS**). GU otherwise read-only. No commit, no push. No edit to LANE-STATE,
research-portfolio, NEXT-STEPS, the anomaly-inflow swing, the LP-LC receipt,
wave-swing-1/3, the global-anomaly-leg pair, Prong-0, the sector-relative theory, or
any other agent's artifact, or any claim/canon/verdict/ledger/portfolio file. No
claim-status, canon-verdict, paper-status, or public-posture change; the externality
of `sigma`/`tau`, the verdict `LC-SELECTOR`, and the Spin-side CLOSED-trivial result
are consumed, not moved. Contribution: `sigma`'s true receptacle is located
(`Omega^{Pin+}_14`, primary), the Spin/Pin non-implication is made rigorous, the
bit-count is **closed at CARDINALITY-1** (with `tau` re-typed as a receptacle label),
and the wall is **PROTECTED** — all conditional on the proposal-grade anomaly-inflow
identification, with the single remaining number (the exact order of `sigma`'s
14-class) named as reconstruction-grade.
