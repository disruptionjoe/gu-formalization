---
artifact_type: exploration
status: exploration (Objective 2 -- turns the W98 BREAK of the sectorial closure into a clean STRUCTURAL THEOREM with an explicit falsification boundary; 5-persona inline team; reconstruction/strong-argument grade, symmetric with W98/W94)
created: 2026-07-13
hypothesis: H61 / H61a (the observer-conjecture Krein-TT critical path) -- the sectorial closure, having BROKEN under interaction (W98), is restated as an IFF-form NO-GO with the boundary condition X made explicit
conjecture: "the source action IS the observer (CONJECTURE-source-action-is-the-observer-2026-07-11.md)"
objective: "Objective 2 -- convert the W98 break into an externally-legible structural theorem: under assumptions A-D, each finite region admits the required modular object, these cohere as a net, and a bounded global extension exists IFF condition X holds. The honest realization of that success-standard is an IFF-NO-GO, because on a genuine type-III_1 region the regional and global obstructions are the SAME UV event."
title: "IFF-NO-GO THEOREM (sectorial modular conjugation). Under A (Krein higher-derivative doublet), B (coupling profile g(k)), C (region = type III_1 / infinite rank, NOT a finite-rank cutoff), D (mass gap m_gap>0): the healthy/ghost Krein frequencies degenerate in the UV (Dw(k)=|m1^2-m2^2|/(w1+w2)->0, GAP-INDEPENDENT), so the exceptional parameter r_k=g(k)/(g(k)+Dw(k)/2) has UV limit set by the coupling. THEOREM (three legs). (1 NET BICONDITIONAL) a coherent net of BOUNDED regional modular conjugations {J_O} (P1 bounded regional J, P2 overlap coherence) exists IFF the coupling is UV-soft, condition X: g(k)=O(1/k) (cleanly definitized, cond->1, IFF the strict X: g(k)=o(1/k)). (2 MUTUAL-EXCLUSIVITY CORE) on a genuine type-III_1 region (C) the region's sup-conditioning EQUALS the global sup-conditioning, so P1 <=> NOT P3 IDENTICALLY for every coupling; hence the observer-relativity net N=P1^P2^P3 (bounded regional J's, coherent, with NO bounded global extension) is UNSATISFIABLE on a genuine region -- the UV event that a soft coupling removes to grant P1 is the SAME event that grants a bounded global J and kills P3. (3 PHYSICAL COROLLARY / FALSIFICATION BOUNDARY) the physical higher-derivative Weyl^2 ghost couples through DERIVATIVE vertices, so g(k) does NOT decay -- NOT X -- hence not even P1 holds: the physical interacting continuum admits NO bounded regional modular conjugation, and the sectorial closure survives ONLY on finite-rank Pi_kappa truncations (NOT C). TRICHOTOMY: (i) FREE g=0 -> P1 yes, P2 yes, P3 NO (global J exists, ghost removable HORN Q, closure vacuous); (ii) INTERACTING non-UV-soft on type III_1 -> P1 NO, P3 yes, P2 NO (genuine firewall HORN K but no realizable modular object -- THE PHYSICAL CASE); (iii) UV-soft boundary X -> P1 yes, P2 yes, but on type III_1 a bounded global J returns so P3 NO (net extends globally; only on a Pi_kappa CUTOFF can the net lack a global extension). The falsification boundary is X: the whole result flips at g(k)=O(1/k); a proof the physical ghost coupling is UV-soft faster than the splitting would move GU into regime (iii); the derivative coupling of Weyl^2 gravity is the standing reason it does not."
grade: "exploration / reconstruction-strong-argument (symmetric with W98 and W94). The theorem is the HONEST structural form of the break: an IFF-no-go with an explicit falsification boundary X. HIGH: a finite region is type III_1 / all-UV (C; Reeh-Schlieder, Buchholz-D'Antoni-Fredenhagen); UV degeneracy Dw(k)->0 gap-independent (D); the mutual-exclusivity core P1<=>NOT P3 (region sup = global sup on type III_1); the net biconditional as a metric-conditioning computation (the coupling exponent sets the UV limit of r_k). MEDIUM-HIGH: the identification of the physical Weyl^2 coupling as NOT-X (conditional on the higher-derivative Krein-doublet reading of the ghost sector and HORN K / W87); the P2 continuum status (interacting double-cone modular conjugation is unsolved/non-geometric -- the numeric is a model surrogate). Encoded in tests/W100_obj2_sectorial_theorem.py (exit 0). No canon / RESEARCH-STATUS / CANON / claim-status / verdict / posture change. The conjecture remains a conjecture; H61/H61a remain OPEN. This does NOT dress the break as a positive: it states the IFF-NO-GO plainly. A falsification boundary IS a result."
depends_on:
  - explorations/break-sectorial-closure-interacting-2026-07-11.md
  - explorations/sectorial-relative-j-2026-07-11.md
  - explorations/CONJECTURE-source-action-is-the-observer-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - tests/W98_break_sectorial_closure.py
  - tests/W94_sectorial_j.py
  - tests/W87_horn_k_vs_q.py
  - tests/W84_rankN_krein_tt.py
scripts:
  - tests/W100_obj2_sectorial_theorem.py
external_refs:
  - "H. Reeh & S. Schlieder, Nuovo Cimento 22 (1961) 1051 -- the vacuum is cyclic and separating for the algebra of every bounded region; the region's algebra contains field content of ALL momenta (no UV truncation). => assumption C."
  - "R. Haag, Local Quantum Physics; D. Buchholz, C. D'Antoni, K. Fredenhagen -- the local algebra M(O) of every bounded region in a Poincare-covariant QFT is the unique hyperfinite type III_1 factor (infinite rank; a region is not a finite-rank cutoff). => assumption C."
  - "J. J. Bisognano & E. H. Wichmann, J. Math. Phys. 16 (1975) 985; 17 (1976) 303 -- geometric modular conjugation (CRT) proved for the WEDGE only."
  - "H. Casini, M. Huerta et al. -- the interacting double-cone modular conjugation is non-geometric and unsolved in general (only wedge + free fields are geometric). => P2 has no continuum theorem under interaction."
  - "D. Krejcirik & P. Siegl, Phys. Rev. D 86 (2012) 121702 -- bounded metric with UNBOUNDED inverse; the infinite-rank obstruction is a sup-over-all-modes (UV-tail) property."
  - "H. Langer, spectral functions of definitizable operators in Krein spaces -- Pontryagin Pi_kappa (finite rank) is definitizable; general infinite rank is not. => the closure survives only on Pi_kappa (NOT C)."
  - "H. Gottschalk, J. Math. Phys. 43 (2002) 4753 -- Krein Bisognano-Wichmann: the modular FLOW half survives the indefinite metric; the conjugation half (the eta-positive square root) does not."
---

# Objective 2: the sectorial break, restated as an IFF-NO-GO theorem with a falsification boundary

**Posture (honest, up front).** This artifact does **not** manufacture a positive out of the `W98`
break. It converts the break into the clean **structural theorem** it actually is: an **IFF-no-go** with an
explicit **falsification boundary** (condition `X`). A falsification boundary is a legitimate result -- it
tells an external reader exactly which single physical input would flip the verdict, and states plainly
that the physical theory sits on the wrong side of it. The grade is the same as the break it formalizes:
**reconstruction / strong-argument**.

**What the break gave (`W98`).** For a genuine finite spacetime region (type III_1, infinite rank) under a
physical non-UV-soft interaction, the three simultaneity properties do **not** hold together:

- **(P1)** every finite region has a **bounded** regional modular conjugation `J_O`;
- **(P2)** the per-region `(Delta_O, J_O)` are **coherent on overlaps** (a net);
- **(P3)** **no** bounded **global** `J` exists.

The observer-relativity structure the conjecture needs is the conjunction **`N = P1 ^ P2 ^ P3`**: bounded
regional firewalls that cohere into a net and admit **no** observer-independent global extension. `W98`
showed `N` fails. Objective 2 asks: state that failure as a theorem of the success-standard form -- "each
finite region admits the modular object, they cohere, and a bounded global extension exists **IFF**
condition `X`." The **honest realization of that standard is an IFF-no-go**, because on a genuine
type-III_1 region the regional obstruction and the global obstruction are the **same UV event**.

---

## 1. Assumptions A-D (named precisely, forks identified per GEOMETER-VS-PHYSICS-OBJECTS.md)

| | Assumption | Statement | Construction fork / side |
|---|---|---|---|
| **A** | **Mode structure (Krein doublet)** | Higher-derivative / Pais-Uhlenbeck field: per momentum `k`, a healthy mode `w_1(k)=sqrt(k^2+m_1^2)` (grade `eta=+1`) and a ghost `w_2(k)=sqrt(k^2+m_2^2)` (grade `eta=-1`); the repo's exceptional-point metric `eta_+(r_k)`, `cond=(1+r_k)/(1-r_k)`, with `r_k = g(k)/(g(k)+Dw(k)/2)`. | **GU-native** (Krein KEEP-AND-GRADE); the metric IS the object whose definitizability decides `P1`. |
| **B** | **Interaction UV softness** | A coupling profile `g(k) >= 0`. Define **condition `X`** (the boundary): `g(k)` is **UV-soft**. Sharp forms: `g(k)=O(1/k)` gives a **bounded** regional `J` (`P1`); the strict `g(k)=o(1/k)` gives a **cleanly** definitized region (`cond -> 1`). Free is `g=0`, a fortiori `X`. | **GU-native** coupling; the exponent of `g(k)` is the single dial. |
| **C** | **Region type** | The region is a **genuine finite spacetime region = type III_1 / infinite rank** (Reeh-Schlieder; Buchholz-D'Antoni-Fredenhagen): it contains the **whole** UV momentum tower `k -> inf`. It is **NOT** a finite-rank `Pi_kappa` UV cutoff. | **STANDARD-PHYSICS (AQFT)**; decisive, and lives on the standard side. Naming the region-vs-cutoff fork **is** the break: a region is not a cutoff. |
| **D** | **Mass gap** | Ghost mass `m_2 = m_gap > 0` (and `m_1 >= 0`). The gap fixes the **position-space** localization/decay rate (`= m_gap`), **not** any momentum-space sup. | **GU-native / standard**; `W97` is correct about locality, silent about definitizability. |

**Key lemma (UV degeneracy, gap-independent).**
```
   Dw(k) = |w_1(k) - w_2(k)| = |m_1^2 - m_2^2| / (w_1(k) + w_2(k))  ~  |m_1^2 - m_2^2| / (2k)  ->  0   (k -> inf),
```
independent of `m_gap`. Hence the UV limit of `r_k = g(k)/(g(k) + Dw(k)/2)` is fixed **entirely by how
`g(k)` compares to `Dw(k) ~ 1/k`**:
- `g(k)` decays **slower** than `1/k` (incl. constant / growing): `r_k -> 1`, `cond -> inf` -- **non-definitizable**;
- `g(k) ~ c/k` (**marginal**, `O(1/k)` but not `o(1/k)`): `r_k -> c/(c + |m1^2-m2^2|/4) = const < 1`, `cond -> const` -- **bounded but not clean** (a fixed residual);
- `g(k) = o(1/k)` (**condition `X`**): `r_k -> 0`, `cond -> 1` -- **cleanly definitized**.

---

## 2. Five-persona team (inline, sequential, single context)

### Persona 1 -- AQFT / modular specialist (state the three legs)

The observer-relativity net is `N = P1 ^ P2 ^ P3`. On a type-III_1 region (C), a **finite region already
contains all UV modes**, so `sup_{k in region} cond = sup_{k, global} cond`. Therefore, for **every**
coupling,
```
   P1 (bounded regional J_O)  <=>  global metric bounded  <=>  bounded global J exists  <=>  NOT P3.
```
This is the **mutual-exclusivity core**: `P1 <=> NOT P3`, identically. Consequences:
- `P1 ^ P3` is **unsatisfiable** on a genuine region -> `N` is **unsatisfiable** for any coupling.
- The coupling only decides **which** side of the XOR you occupy -- it never buys both.

Leg (1), the **net biconditional**, is then a pure metric-conditioning fact from the key lemma:
`P1 ^ P2` (a coherent net of bounded regional `J`'s) exists **iff** `g` is UV-soft (`O(1/k)` for
boundedness; `o(1/k) = X` for clean `cond->1`).

### Persona 2 -- MATH REFEREE (is the IFF real, and honestly graded?)

- **Ruling 1 -- the biconditional is genuine, both directions.** `(<=)` UV-soft `g` gives `r_k` bounded
  away from 1 (or `->0`), so `sup cond < inf` -- bounded regional `J`; mode-diagonality then coheres them
  (`P2`, free-toy grade). `(=>)` if `g` is **not** `O(1/k)` then `r_k -> 1` and `sup cond = inf` -- **no**
  bounded regional `J` (`P1` fails). So `P1 <=> X`. Verified numerically across coupling profiles
  (`W100` T5): `const -> inf`, `1/sqrt(k) -> inf`, `1/k -> const`, `1/k^2 -> 1`.
- **Ruling 2 -- the no-go core is a theorem-grade structural fact, not a numeric.** `sup_region =
  sup_global` follows from `C` (type III_1, all UV modes) alone; it needs no computation. This is the
  strongest leg.
- **Ruling 3 -- honest grade = reconstruction / strong-argument.** Symmetric with `W98`/`W94`. The two
  conditional inputs are: (a) the higher-derivative Krein-doublet **reading** of the ghost sector (A), and
  (b) the identification of the **physical** Weyl^2 coupling as **not** `X` (leg 3). Both are physics
  readings, not proved continuum theorems. `P2`'s continuum status is a model surrogate (interacting
  double-cone modular conjugation is unsolved). The theorem is not dressed above its evidence.

### Persona 3 -- ADVERSARY (attack the IFF; try to keep `N` alive)

- **Attack: "UV-soft `X` grants `P1` -- so take `X` and keep `P3` too, giving `N`."** **Rebuttal:** on a
  type-III_1 region the same soft coupling that bounds `sup_region` bounds `sup_global` (they are equal),
  so a bounded **global** `J` returns and `P3` **fails**. Under `X`, `N` dies through `P3`, not `P1`. The
  adversary cannot have `P1` and `P3` at once (mutual-exclusivity core). `W100` T6.
- **Attack: "then take a finite-rank `Pi_kappa` cutoff -- there `P1` on each band and `P3` globally can
  both hold."** **Rebuttal:** true, and that is **exactly `W94`'s toy** -- but it **violates C**. A cutoff
  is not a spacetime region; Objective 2's success-standard is about **regions**. Under `NOT C` with a
  **non-soft** coupling the closure does hold (each finite momentum band is bounded, the global tower
  diverges) -- which is precisely why `W98` demoted the closure to a **finite-mode toy artifact**. The
  adversary's survival requires abandoning the region assumption. `W100` T4/T7.
- **Attack: "the physical coupling might be soft."** **Rebuttal:** the higher-derivative (Weyl^2) ghost
  couples through **derivative** vertices -- `g(k)` does **not** decay. This is the **one** honest
  survival window and it is the **falsification boundary** `X`, stated plainly, not hidden. `W100` T8.

### Persona 4 -- CROSS-CHECKER (second derivation; literature)

**D2 (AQFT structure, independent of the mode computation).** (1) A finite region is type III_1 /
infinite rank (Connes-Haagerup; Buchholz-D'Antoni-Fredenhagen) -> `sup_region = sup_global` and the
`W84/W93` infinite-rank obstruction applies (Krejcirik-Siegl: bounded metric, unbounded inverse; Langer:
only `Pi_kappa` definitizable). (2) The interacting double-cone modular conjugation is **not geometric,
not solved** (only wedge Bisognano-Wichmann + free fields) -> there is **no** continuum theorem delivering
`P2` under interaction; the free-toy coherence was a Gaussian/mode-diagonal artifact. (3) The flow half
survives, the conjugation half does not (Gottschalk). **D1 (mode conditioning) and D2 (AQFT + literature)
AGREE**: `N` requires an `eta`-positive square root that a genuine region under non-soft interaction
denies; the whole result pivots on the coupling exponent `X`.

### Persona 5 -- SYNTHESIZER

See Sections 3-4.

---

## 3. The theorem (IFF-form no-go)

> **Theorem (Sectorial modular-conjugation IFF-no-go).** Assume **A** (Krein higher-derivative doublet),
> **B** (coupling profile `g(k)`), **C** (the region is a genuine type-III_1 spacetime region, infinite
> rank / all UV modes -- **not** a finite-rank `Pi_kappa` cutoff), **D** (mass gap `m_gap > 0`). Then:
>
> **(1) Net biconditional.** A coherent net of **bounded** regional modular conjugations `{J_O}`
> (`P1 ^ P2`) exists **IF AND ONLY IF** the interaction is **UV-soft** (condition `X`): `g(k) = O(1/k)`
> for boundedness, `g(k) = o(1/k)` for clean asymptotic definitization (`cond -> 1`). Equivalently,
> **regional definitizability `<=> X`**.
>
> **(2) Mutual-exclusivity core.** Because a type-III_1 region contains the **whole** UV tower,
> `sup_region cond = sup_global cond`, hence `P1 <=> NOT P3` **identically, for every coupling**. Therefore
> the observer-relativity net `N = P1 ^ P2 ^ P3` (bounded coherent regional firewalls with **no** bounded
> global extension) is **UNSATISFIABLE** on a genuine region: the UV event a soft coupling removes to grant
> `P1` is the **same** event that grants a bounded global `J` and kills `P3`.
>
> **(3) Physical corollary / falsification boundary.** The physical higher-derivative **Weyl^2** ghost
> couples through **derivative** vertices, so `g(k)` does **not** decay -- **`NOT X`**. Hence **not even
> `P1`** holds: the physical interacting continuum admits **no** bounded regional modular conjugation. The
> sectorial closure survives **only** on finite-rank `Pi_kappa` truncations (**`NOT C`**) with a non-soft
> coupling -- it is a **finite-mode toy artifact**. The result flips at `X`; a proof that the physical
> ghost coupling is UV-soft faster than the splitting would move GU into regime (iii). The **derivative
> coupling of Weyl^2 gravity is the standing reason it does not** -- this is the explicit falsification
> boundary.

**The trichotomy (the three regimes A-D single out).**

| Regime | Coupling | `P1` (bdd regional `J`) | `P2` (overlap coherence) | `P3` (no global `J`) | `N` | Physics label |
|---|---|---|---|---|---|---|
| **(i) FREE** | `g = 0` | **yes** | yes | **NO** | fails via `P3` | global `J` exists; ghost **removable** (HORN Q); closure **vacuous** |
| **(ii) INTERACTING, non-UV-soft** (`NOT X`) on type III_1 | e.g. `g=const` (physical) | **NO** | **NO** | yes | fails via `P1` | genuine firewall (HORN K) but **no realizable modular object** -- **THE PHYSICAL CASE** |
| **(iii) UV-soft boundary** (`X`) | `g(k)=o(1/k)` | **yes** | yes | **NO** (on type III_1) | fails via `P3` | region cleanly definitized, but a bounded global `J` returns; only on a `Pi_kappa` **cutoff** can the net lack a global extension |

In every regime the observer-relativity net `N` fails -- through `P3` when the coupling is soft enough for
`P1`, through `P1` when the coupling is physical. There is **no** regime with all three, and the physical
theory sits in **(ii)**.

---

## 4. Confidence, falsification boundary, and scope

- **`C`: finite region is type III_1 / all-UV:** **HIGH** (Reeh-Schlieder; Buchholz-D'Antoni-Fredenhagen).
- **`D`-lemma: `Dw(k)->0` gap-independent:** **HIGH** (elementary; `W100` T3).
- **Mutual-exclusivity core `P1 <=> NOT P3`:** **HIGH** (`sup_region = sup_global` from `C`; `W100` T6).
- **Net biconditional `P1 <=> X`:** **HIGH** as a metric-conditioning computation (`W100` T5); the
  coupling exponent sets the UV limit of `r_k` deterministically.
- **Leg 3: physical Weyl^2 coupling is `NOT X`:** **MEDIUM-HIGH** -- conditional on the higher-derivative
  Krein-doublet reading (A) and HORN K (`W87`); it is the derivative-vertex physics, not a proved theorem.
- **`P2` under interaction:** **MEDIUM-HIGH** -- literature says the interacting double-cone conjugation is
  unsolved/non-geometric; the numeric is a model surrogate.
- **THE THEOREM (IFF-no-go):** **MEDIUM-HIGH** -- symmetric in rigor with `W98`/`W94`; it does not exceed
  the break it formalizes, and it **adds** the externally-legible falsification boundary `X`.

**Falsification boundary (`X`), stated plainly.** Everything turns on the single boolean **`g(k) = O(1/k)`
(UV-soft)**. On the wrong side (`NOT X`, the physical derivative-coupled ghost): no bounded regional `J`,
the closure is a toy artifact. What would move it: (a) `W87` FRG `beta_{f_2^2}` -- `f_2^2* = 0` (HORN K)
confirms the genuine indefinite ghost -> the no-go stands; `f_2^2* > 0` (HORN Q) makes the ghost removable
-> `P3` fails and `N` is vacuous anyway. Either FRG outcome keeps `N` dead. (b) A proof the physical ghost
coupling is UV-soft faster than `1/k` -- would move GU into regime (iii) and grant `P1 ^ P2` (but still not
`N`, which dies via `P3` on a type-III_1 region). (c) A continuum interacting Krein double-cone
modular-conjugation theorem -- does not exist; this swing gives a mechanism for why it should not.

**What this does NOT do.** No GU claim-status, `CANON.md`, `RESEARCH-STATUS.md`, verdict, or public-posture
change. No external action; citations are read-only. The conjecture remains a conjecture; H61/H61a remain
**OPEN**. The sectorial closure stays **demoted** (per `W98`) to a finite-mode toy artifact; Objective 2's
contribution is to state that demotion as a **clean IFF-no-go with an explicit falsification boundary**,
not to resurrect a positive. Reproducible: `tests/W100_obj2_sectorial_theorem.py` (exit 0).
