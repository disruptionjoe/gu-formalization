---
artifact_type: exploration
status: exploration (ADVERSARIAL break-test of the observer-conjecture's sectorial closure in a LARGER interacting model; 5-persona inline team; literature read-only + deterministic test)
created: 2026-07-13
hypothesis: H61 / H61a (the observer-conjecture Krein-TT critical path) -- the sectorial closure (W94) STRESS-TESTED under relaxed assumptions
conjecture: "the source action IS the observer (CONJECTURE-source-action-is-the-observer-2026-07-11.md)"
branch: "The sectorial closure (W94) was established on a FINITE-MODE / mode-DIAGONAL (free, one-loop) TOY. This swing is ADVERSARIAL: RELAX the finite-mode and one-loop assumptions (a genuinely interacting, infinite-mode / continuum region) and TRY TO BREAK the closure. The crucial target is NOT whether a sectorial J can be re-written, but whether THREE things stay SIMULTANEOUSLY true: (P1) every finite REGION has a bounded valid J_O; (P2) the regional constructions cohere on OVERLAPS (net gluing); (P3) NO global bounded J exists. The sharp break-point: a finite spacetime region's algebra is ALREADY type III_1 / infinite rank (Reeh-Schlieder), so if infinite-rank => non-definitizable => no bounded J (W84/W93), P1 might FAIL for a genuine finite region -- putting P1 in direct conflict with P3. Does the mass gap (W97) definitize a finite region despite type III_1, or not?"
title: "BREAKS-AT-1. The sectorial closure does NOT survive the relaxation to a genuine interacting continuum region: it was a FINITE-MODE / mode-DIAGONAL TOY ARTIFACT. (P1) A genuine finite SPACETIME REGION is type III_1 (Reeh-Schlieder; Buchholz-D'Antoni-Fredenhagen) -- it contains the WHOLE UV momentum tower. In a Krein higher-derivative / Pais-Uhlenbeck field the healthy and ghost frequencies DEGENERATE in the UV (Dw(k)=|m1^2-m2^2|/(w1+w2) -> 0 as k -> inf), so ANY non-UV-soft interaction drives the exceptional-point parameter r_k -> 1 over the region's UV modes => the metric conditioning is UNBOUNDED => NO bounded regional J_O. P1 FAILS. (Escape KILLED:) the mass gap protects LOCALITY (position-space decay rate = m_gap, W97 correct) but NOT DEFINITIZABILITY (a momentum-space sup); the UV degeneracy is GAP-INDEPENDENT, so the mass gap does NOT definitize a finite region. (P1-vs-P3 RESOLUTION:) P1 and P3 are MUTUALLY EXCLUSIVE -- FREE => P1 holds but a bounded GLOBAL J exists (P3 FAILS: HORN Q, removable ghost, closure VACUOUS); INTERACTING => no global J (P3 holds: HORN K, genuine firewall) but the SAME UV degeneracy makes every finite region non-definitizable (P1 FAILS). A genuine firewall (P3) FORCES P1 to fail; a definitizable region (P1) forces a removable ghost (P3 fails). No regime has BOTH. (P2, the crux, ALSO breaks:) free/mode-diagonal regions cohere trivially (W94 T3), but interacting region-dependent modular data gives r^{O1} != r^{O2} on shared overlap modes, so J_{O1} and J_{O2} DISAGREE on M(O1 cap O2) and the disagreement DIVERGES in the UV. The three properties do NOT hold simultaneously; the closure holds ONLY on finite-rank Pi_kappa truncations. W94's decisive error: it read the observer's region as a finite-RESOLUTION UV cutoff (finite rank, definitizable) rather than a genuine finite SPACETIME REGION (type III_1, infinite rank); a region is not a cutoff. Two-derivation status: AGREE (D1 momentum/mode computation; D2 AQFT structure + literature). LOAD-BEARING assumption: the interaction is not UV-soft faster than 1/k -- the physical derivative-coupled higher-derivative ghost is not."
grade: "exploration / one adversarial BREAK result at reconstruction/strong-argument grade: in a larger interacting Krein (higher-derivative / Pais-Uhlenbeck) region model, the three simultaneity properties (P1 bounded regional J, P2 overlap coherence, P3 no global J) do NOT hold together; the closure is a finite-mode / mode-diagonal toy artifact. The load-bearing mechanism (UV degeneracy of the Krein doublet => exceptional-point r_k -> 1 over a type-III_1 region's UV modes) is a clean computation; its application to GU is conditional on (i) the higher-derivative Krein-doublet reading of the ghost sector, (ii) a non-UV-soft interaction (the physical derivative ghost coupling), and (iii) HORN K (W87). Encoded in tests/W98_break_sectorial_closure.py (7/7, numpy-only, exit 0). Literature read-only 2026-07-13: Reeh-Schlieder; Connes-Haagerup / Buchholz-D'Antoni-Fredenhagen (bounded regions are type III_1, UV-divergent entanglement intrinsic to the algebra); Bisognano-Wichmann (geometric modular flow wedge-only); interacting double-cone modular conjugation unsolved/non-geometric except free fields (Casini-Huerta); Krejcirik-Siegl (bounded metric, unbounded inverse); Langer (only Pi_kappa definitizable). No canon, RESEARCH-STATUS, CANON, claim-status, verdict, or public-posture change. The conjecture remains a conjecture; H61/H61a remain OPEN, and the sectorial closure is demoted from 'sectorially closed' to 'finite-mode toy artifact that BREAKS-AT-1 in the interacting continuum'."
depends_on:
  - explorations/sectorial-relative-j-2026-07-11.md
  - explorations/cond-ii-finite-resolution-aqft-2026-07-11.md
  - explorations/cond-iii-w54-all-orders-2026-07-11.md
  - explorations/branch3-algebraic-modular-skeleton-2026-07-11.md
  - explorations/branch5-adversarial-nogo-2026-07-11.md
  - explorations/rankN-krein-tt-for-gu-2026-07-11.md
  - explorations/CONJECTURE-source-action-is-the-observer-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - tests/W94_sectorial_j.py
  - tests/W96_cond_ii_aqft.py
  - tests/W97_cond_iii_all_orders.py
  - tests/W84_rankN_krein_tt.py
  - tests/W93_adversarial_nogo.py
scripts:
  - tests/W98_break_sectorial_closure.py
external_refs:
  - "H. Reeh & S. Schlieder, Nuovo Cimento 22 (1961) 1051 -- the vacuum is cyclic and separating for the algebra of every bounded region; the algebra of any open region contains field content of ALL momenta (no UV truncation)."
  - "R. Haag, Local Quantum Physics; D. Buchholz, C. D'Antoni, K. Fredenhagen (Connes-Haagerup) -- the local algebra M(O) of every bounded region in a Poincare-covariant QFT is the unique hyperfinite type III_1 factor; the UV divergence of entanglement is INTRINSIC to the algebra (a finite region is infinite-rank, not a finite-rank cutoff)."
  - "K. Fredenhagen, Comm. Math. Phys. 79 (1981) 141 -- scaling limits of double-cone algebras are non-trivial only if all double-cone algebras are type III_1."
  - "J. J. Bisognano & E. H. Wichmann, J. Math. Phys. 16 (1975) 985; 17 (1976) 303 -- geometric modular flow (boost) and geometric modular conjugation (CRT) proved for the WEDGE only."
  - "H. Casini, M. Huerta et al. -- the modular Hamiltonian of a general (double-cone) region for the vacuum is known only for free / conformal fields; for interacting theories it is non-geometric and unsolved in general (the S-matrix is a relative modular invariant of the interacting-vs-incoming WEDGE net)."
  - "D. Krejcirik & P. Siegl, Phys. Rev. D 86 (2012) 121702 -- bounded metric with UNBOUNDED inverse; the infinite-rank obstruction is a sup-over-all-modes property (the UV tail); real-positive spectrum does not give a bounded boundedly-invertible metric."
  - "H. Langer, spectral functions of definitizable operators in Krein spaces -- Pontryagin Pi_kappa (finite rank) is definitizable (an eta-positive square root exists); general infinite-rank is not."
  - "H. Gottschalk, J. Math. Phys. 43 (2002) 4753 -- Krein Bisognano-Wichmann: the modular FLOW half survives the indefinite metric (does not rescue the conjugation half)."
---

# Break-test: does the sectorial closure survive a genuinely interacting, infinite-mode continuum region?

**Role.** The observer conjecture's sectorial closure (`W94`) proved -- on a **finite-mode / mode-diagonal
(free, one-loop) TOY** -- that the physical firewall realization "closes sectorially" and that the global
`J`'s non-existence "confirms" observer-relativity. `W94` conceded the crux **twice** in its own honesty
register: the toy net "coheres exactly because the modes are diagonal (free); in the full interacting
theory the coherence is `W54`-Result-2-grade (one-loop)," and non-definitizability "is ONLY the `t->inf`
idealization no finite-resolution observer occupies." **This swing is adversarial: relax both assumptions
(a genuinely interacting, infinite-mode / continuum region) and TRY TO BREAK the closure.** An honest
break is as valuable as survival; the goal is to break it, not to manufacture survival.

**The target is not whether a sectorial `J` can be re-written.** It is whether **three** things stay
**SIMULTANEOUSLY** true in the larger model:

- **(P1)** every physically finite **REGION** has a **bounded** valid modular conjugation `J_O`;
- **(P2)** the regional constructions are **mutually coherent on OVERLAPS** (net gluing: isotony,
  locality, Haag-duality compatibility of the per-region `(Delta_O, J_O)`);
- **(P3)** **no** observer-independent **global** bounded `J` exists.

**Answer: BREAKS-AT-1.** The three do **not** hold together for a genuine finite spacetime region under
interactions. The closure was a **finite-mode / mode-diagonal toy artifact**. `P1` fails region-locally
(a finite region is type III_1, its UV modes hit the exceptional point under interaction); `P2` (the crux)
also breaks; `P3` survives **only at `P1`'s expense** (they are mutually exclusive). The mass-gap escape
(`W97`) is **killed**. `W94`'s decisive error was reading the observer's region as a finite-**resolution
UV cutoff** (finite rank, definitizable) rather than a genuine finite **spacetime region** (type III_1,
infinite rank) -- **a region is not a cutoff**.

**Artifacts:** this file + deterministic `tests/W98_break_sectorial_closure.py` (7/7, numpy-only, exit 0).
**Not committed. Not a claim-status change.** Exploration-grade.

---

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Construction used | Load-bearing here |
|---|---|---|
| **The algebra / the region** | GU-native indefinite region `*`-algebra on the Krein space, BUT the decisive fact -- **a finite spacetime region is type III_1 and contains the WHOLE UV momentum tower** -- is a **standard-physics (AQFT)** fact (Reeh-Schlieder; Buchholz-D'Antoni-Fredenhagen). It is decisive here, and it lives on the **standard-physics side**. | `W94`'s "finite-resolution observer" silently swapped a **spacetime region** (type III_1, infinite rank) for a finite-rank **UV cutoff**. Naming this fork **is** the break: a region is not a cutoff, so the finite-rank definitizability escape does not apply to a genuine region. |
| **Ghost clearance** | GU-native **KEEP-AND-GRADE** (Krein indefinite metric), not positive-Hilbert removal. | So the metric/grading **is** the object whose (non-)definitizability decides everything. **FREE** keep-and-grade = clean bounded grading (`eta=diag(+1,-1)`, cond 1) = **HORN Q / removable**; **INTERACTING** keep-and-grade = UV-degenerate = **HORN K / genuine but non-definitizable**. |
| **The modular conjugation `J`** | the antilinear `J = S Delta^{-1/2}`, per region, needing an `eta`-positive `Delta_O^{1/2}` (definitizability). | Its existence is exactly `P1`. Under interaction the region's UV modes are past the exceptional point, so no bounded `Delta_O^{-1/2}` exists -> no `J_O`. |
| **The load-bearing FORK** | **is the observer's region a finite-RESOLUTION UV cutoff (W94's reading -> P1 survives) or a genuine finite SPACETIME REGION (type III_1, all UV modes -> P1 fails under interaction)?** | We **identify** the spacetime-region reading as correct, with reason: Reeh-Schlieder is a theorem, and the AQFT type-III_1 classification is standard. We state cleanly what the cutoff reading would (falsely) buy. |

**The one fork this swing turns on (named, not defaulted):** a spacetime **region** vs a **UV cutoff**.
`W94` needed non-definitizability to be "only at `k=inf`, no finite observer reaches it." But the index
`k` is **momentum**, and a genuine finite spacetime region **already** contains all momenta (Reeh-
Schlieder / type III_1). So the region **realizes the whole tower** -- `W94`'s escape dissolves.

---

## 1. The larger interacting model (built, not gestured at)

**The model.** A Krein higher-derivative / **Pais-Uhlenbeck** field on a finite spatial region. Per
momentum `k` the region carries a **Krein doublet**: a healthy mode `w_1(k) = sqrt(k^2 + m_1^2)` (graded
`eta = +1`) and a **ghost** mode `w_2(k) = sqrt(k^2 + m_2^2)` (graded `eta = -1`). For higher-derivative
gravity `m_1 = 0` (massless graviton) and `m_2 = M_2` (ghost mass = the mass gap). A genuine **interaction**
mixes the graded doublet with strength `g(k)`.

**The UV-degeneracy mechanism (the physics of the break).** The two Krein frequencies **degenerate** in
the UV:
```
   Dw(k) = |w_1(k) - w_2(k)| = |m_1^2 - m_2^2| / (w_1(k) + w_2(k))  ->  0   as  k -> inf,
```
**independent of the mass gap** (`Dw ~ |m_1^2 - m_2^2| / 2k` for any fixed masses). The exceptional-point
parameter of the repo's own W52/W84 metric is then
```
   r_k = g(k) / ( g(k) + Dw(k)/2 ),      cond(eta_+(r_k)) = (1 + r_k)/(1 - r_k),   ||J||-cost = 1/sqrt(1-r_k).
```
- **FREE (`g = 0`):** `r_k = 0` at **every** `k`. The metric is the clean grading `eta = diag(+1,-1)`,
  cond `= 1`, bounded with bounded inverse. The region is **definitizable**, `J_O` bounded -- **and a
  bounded GLOBAL `J` exists too**. (`W98` T1.)
- **INTERACTING (`g > 0`):** as `k -> inf`, `Dw(k) -> 0`, so `r_k -> 1`: the mixing dominates the
  vanishing splitting, the mode approaches the **exceptional (Jordan) point**, and
  `cond(eta_+(r_k)) -> inf`. Over a finite region's UV modes the conditioning is **unbounded**. (`W98` T2.)

**Why this is the physical case.** The higher-derivative (Weyl^2) ghost couples through **derivative**
vertices -- `g(k)` does **not** decay in the UV. Only a coupling `g(k) = o(1/k)` (UV-soft faster than the
splitting) would preserve definitizability (`W98` T7); the physical derivative-coupled ghost is not that.
This is the **load-bearing assumption**, named and boxed as a boolean in the test.

---

## 2. Five-persona team (inline, sequential, single context)

### Persona 1 -- AQFT / modular specialist (build the model; test P1, P2, P3)

**P1 is where it breaks.** In `W94`'s free mode-diagonal toy every mode is definitizable because the
ghost is a clean `-1` grading. The moment (i) the algebra is a genuine finite region -- which is **type
III_1** and contains all UV momenta (Reeh-Schlieder) -- and (ii) the theory interacts, the UV degeneracy
`Dw(k) -> 0` drives `r_k -> 1` over the region's UV tail. The region's `sup_k cond(eta_+(r_k))` is
**unbounded** (`W98` T2: `8890 -> 17779 -> 35557` as the UV reach doubles), so there is **no bounded
`Delta_O^{-1/2}`** and **no bounded `J_O`**. `P1` **fails** for a genuine finite region. `P3` (no global
`J`) is then **automatic but not independent** -- it is the same UV divergence (`W98` T4). `P2` is tested
in Persona 3.

### Persona 2 -- MATH REFEREE (is the break real, or a modelling artifact?)

- **Ruling 1 -- the break is real, not a numerical fudge.** `cond(eta_+(r_k)) = (1+r_k)/(1-r_k)` is the
  repo's own W84/W94 metric-conditioning; `r_k -> 1` is the exceptional-point approach they already use.
  The only new input is that `r_k` is indexed by **momentum** (not RG scale) and that `Dw(k) -> 0` is an
  elementary, gap-independent fact. The conditioning genuinely **grows without bound** under UV extension
  (`W98` T2, robust "doubling" signature, no arbitrary threshold). **The obstruction is genuine.**
- **Ruling 2 -- `W94`'s escape is the load-bearing error.** `W94` graded non-definitizability as a
  `t->inf` RG idealization "no finite-resolution observer occupies." But a finite **spacetime region** is
  **not** a finite-resolution object: by Reeh-Schlieder / the type-III_1 classification it contains the
  **whole** UV tower. So the region **is** the `k->inf` limit, mode-content-wise. The referee rules the
  region-vs-cutoff conflation is the specific defect. **`P1` fails for a genuine region.**
- **Ruling 3 -- the honest grade.** The break is **reconstruction / strong-argument grade**: the
  mechanism is a clean computation, conditional on the higher-derivative Krein-doublet reading, a
  non-UV-soft interaction (physical), and HORN K (`W87`). It is **not** a fully rigorous continuum
  theorem (no more than `W94`'s closure was). But it **removes** `W94`'s survival: the closure does not
  survive relaxation, so its "sectorially closed" grade is **withdrawn**.

### Persona 3 -- ADVERSARY (drive the break: P2 overlap coherence + the P1-vs-P3 type-III tension)

- **P2 (overlap coherence -- THE CRUX) breaks.** In the free mode-diagonal toy the per-region `J`'s
  cohere **trivially** because the `C`-grading is region-independent (`W94` T3: exact nesting). Under
  interactions the per-region modular data is **state- and region-dependent**: the interacting
  double-cone modular conjugation is **unsolved / non-geometric** (only the **wedge**, Bisognano-
  Wichmann, and free fields are geometric -- literature 2026-07-13). A shared overlap mode `k` acquires a
  **region-dependent modular weight** `w_O(k)` (its modular rapidity differs between `O1` and `O2`), so
  the effective mixing `g_O(k) = g w_O(k)` gives **different** exceptional parameters `r^{O1}_k !=
  r^{O2}_k`, hence **different** `Delta_O^{-1/2}` on the **same** overlap mode. `J_{O1}` and `J_{O2}`
  **DISAGREE** on `M(O1 cap O2)`, and the disagreement **diverges in the UV** (`W98` T6: `0.32 -> 10.97
  -> 34.70`). FREE: disagreement `= 0` (cohere). The per-region firewalls do **not** patch into a
  consistent net. (And the overlap is itself type III_1, so no bounded `J` on it exists anyway.)
- **The P1-vs-P3 tension, resolved: they are MUTUALLY EXCLUSIVE.** A finite region is type III_1 =>
  `sup_region cond = sup_global cond` (`W98` T5). Hence **`P1` (region definitizable) <=> a bounded global
  `J` exists <=> NOT `P3`.** Two regimes, no third:
  - **HORN Q (free / removable):** `P1` True, `P3` **False** -- a global `J` exists, the firewall is
    trivial, the closure is **vacuous**.
  - **HORN K (interacting / genuine):** `P3` True, `P1` **False** -- no global `J`, the firewall is
    genuine, but every finite region is non-definitizable (no regional `J`).
  A **genuine** firewall (`P3`) **forces** `P1` to fail; a **definitizable** region (`P1`) forces a
  **removable** ghost (`P3` fails). **There is no regime with `P1` AND `P3`.** The closure, which needs
  **both**, cannot hold.
- **The mass-gap escape (`W97`) is killed.** `W97` is **correct** that the gap protects **locality**
  (position-space correlations decay at rate `= m_gap`). But **definitizability** is a **momentum-space
  sup** over all modes, and the UV degeneracy `Dw(k) -> 0` is **gap-independent** (`W98` T3: the
  conditioning at `k = 5e3` is huge for **every** gap `m_2 in {0.1, ..., 2.0}`). So the mass gap does
  **not** definitize a finite region: it protects the wrong thing. The escape conflates position-space
  decay with momentum-space metric boundedness.

### Persona 4 -- CROSS-CHECKER (second derivation + literature)

**Second derivation (D2), independent of the mode computation.** Purely from AQFT structure:
1. **A finite region is type III_1** (Connes-Haagerup; Buchholz-D'Antoni-Fredenhagen), and its
   entanglement is **UV-divergent as an intrinsic property of the algebra** -- confirmed literature
   2026-07-13. So a finite region is **infinite rank**, not a finite-rank cutoff. This alone triggers the
   `W84`/`W93` infinite-rank obstruction: real-positive spectrum does **not** give a bounded boundedly-
   invertible metric (Krejcirik-Siegl), and general infinite-rank Krein-selfadjoint operators are **not**
   definitizable (Langer -- only `Pi_kappa` is). So even **before** the mode computation, `P1` is in
   jeopardy for a genuine region, and W94's finite-rank `Pi_kappa` existence result does **not** transfer.
2. **The interacting double-cone modular conjugation is not geometric and not solved** (only the wedge is
   Bisognano-Wichmann geometric; interacting `J_O` for a double cone is unknown except free fields --
   confirmed literature). So there is **no** theorem delivering `P2` (overlap coherence) under
   interactions; the free-toy coherence was an artifact of Gaussianity + mode-diagonality.
3. **The flow half survives, the conjugation half does not** (Gottschalk: Krein Bisognano-Wichmann gives
   `Delta^{it}` = boost; but `P1`/`P2` need the **conjugation** `J = S Delta^{-1/2}`, which needs the
   `eta`-positive square root that infinite rank denies). This matches Branch 3 (`W91`) and Branch 5
   (`W93`) exactly: the residual is **definitizability**, and a genuine region is where it bites.

**D1 (mode computation) and D2 (AQFT structure + literature) AGREE:** the closure does not survive to a
genuine interacting continuum region; it holds only on finite-rank truncations.

### Persona 5 -- SYNTHESIZER (the verdict)

See Sections 3-5.

---

## 3. VERDICT: BREAKS-AT-1 (the closure was a finite-mode toy artifact)

| Property | Free / mode-diagonal toy (W94) | Larger interacting continuum region (this swing) | Result |
|---|---|---|---|
| **P1** bounded regional `J_O` | holds (clean grading, `Pi_kappa`) | **FAILS** -- region is type III_1, UV degeneracy `r_k -> 1`, cond unbounded | **BROKEN** |
| **P2** overlap coherence | holds trivially (region-independent `C`-grading, exact nesting) | **FAILS** -- region-dependent modular data, `J_{O1} != J_{O2}` on overlap, UV-divergent | **BROKEN** |
| **P3** no global `J` | holds (RG tower `r -> 1` at `t=inf`) | holds -- but by the **same** UV degeneracy that fails `P1`; not independent | survives only at `P1`'s expense |
| **All three SIMULTANEOUSLY** | asserted (toy) | **NO** | **BREAKS-AT-1** |

**The earned statement.**
> For a genuine finite **spacetime region** (type III_1, infinite rank, containing the whole UV momentum
> tower) in a genuinely **interacting** Krein higher-derivative field, `P1` (a bounded regional `J_O`)
> and `P3` (no bounded global `J`) are **mutually exclusive**: a definitizable region has a **global** `J`
> (removable ghost, HORN Q, closure vacuous), and a genuine firewall (no global `J`, HORN K) has **no**
> bounded regional `J` (the UV modes are past the exceptional point). `P2` (overlap coherence) breaks
> **independently** under interactions (region-dependent, non-geometric modular data). The sectorial
> closure holds **only on finite-rank `Pi_kappa` truncations** -- it is a **finite-mode / mode-diagonal
> TOY ARTIFACT**, and the physical interacting continuum realization does **NOT** close.

**Why this is the honest break, not manufactured.** The break is earned because: (1) `P1` genuinely
fails -- the conditioning is **computed** to diverge over a region's UV modes, using the repo's own
metric; (2) the escape (`W97` mass gap) is **tested and killed** -- the UV degeneracy is gap-independent;
(3) `P1` and `P3` are **computed** to be mutually exclusive (the region's sup equals the global sup
because a region contains all UV modes); (4) `P2` is **computed** to break under region-dependent
interaction. Had the conditioning stayed bounded, or the gap definitized the region, or a regime with
`P1` and `P3` both true existed, the verdict would have been SURVIVES or PARTIAL. It is none of those.

---

## 4. Self-critical pass -- the load-bearing assumption + the one survival window (named, not hidden)

**The single load-bearing assumption:** **the interaction is not UV-soft faster than `1/k`.** If a
coupling `g(k) = o(1/k)` is imposed (mixing dies faster than the frequency splitting), then `r_k -> 0` in
the UV and definitizability is preserved -- `P1` would survive (`W98` T7 verifies a `1/k^2` coupling keeps
the conditioning bounded). **This is the one honest survival window**, and it is **not** the physical
case: the higher-derivative (Weyl^2) ghost couples through **derivative** vertices, so `g(k)` grows rather
than decays. On the physically relevant reading the break is **generic**.

**The construction fork (stated, not defaulted).**
- *Spacetime-region reading (identified as correct, with reason).* Reeh-Schlieder + the type-III_1
  classification (Buchholz-D'Antoni-Fredenhagen) make a finite region **infinite rank / all-UV**. On this
  reading `P1` **fails** under interaction -> **BREAKS-AT-1**.
- *Finite-resolution UV-cutoff reading (W94's, identified as the error).* If the observer's "region" is a
  finite-rank `Pi_kappa` cutoff, everything is definitizable (Langer) and the closure holds -- **but that
  is the toy, not a spacetime region.** The whole point of relaxing the finite-mode assumption is that a
  genuine region is **not** a cutoff. So this reading **is** the assumption the task asked us to relax,
  and relaxing it breaks the closure.

**Could the break be wrong (steelmanning survival)?** The strongest survival case: the observer only ever
**probes** finite energy, so it effectively occupies a finite-rank sub-sector where `J` exists. Rebuttal:
"probing finite energy" is a **state/measurement** statement; the **algebra** of a spacetime region is
still type III_1 and its modular conjugation `J_O` is an object of the **algebra**, not of a bounded-energy
subspace. The firewall `J_O` (the physical realization the conjecture needs) is the region's modular
conjugation, which does not exist boundedly. So the survival case again silently swaps the region for a
cutoff. The break stands.

---

## 5. Confidence grade and what would move it

- **A finite spacetime region is type III_1 / infinite rank / all-UV:** **HIGH** (Reeh-Schlieder;
  Buchholz-D'Antoni-Fredenhagen; standard AQFT).
- **UV degeneracy `Dw(k) -> 0`, gap-independent:** **HIGH** (elementary; `W98` T3).
- **Interacting finite region non-definitizable => `P1` fails (non-UV-soft coupling):** **MEDIUM-HIGH** --
  clean computation on the repo's metric, conditional on the higher-derivative Krein-doublet reading and a
  non-UV-soft (physical, derivative) interaction.
- **Mass-gap escape killed (gap protects locality, not definitizability):** **HIGH** (`W98` T3; the two
  are different quantities; matches `W97`'s own scope).
- **`P1` and `P3` mutually exclusive:** **HIGH** (`W98` T5; region sup = global sup because a region
  contains all UV modes).
- **`P2` (overlap coherence) breaks under interactions:** **MEDIUM-HIGH** -- mechanism (region-dependent,
  non-geometric interacting modular data) is literature-backed; the numeric is a model surrogate, not a
  continuum theorem.
- **VERDICT = BREAKS-AT-1:** **MEDIUM-HIGH** -- the closure does not survive relaxation; it is a
  finite-mode toy artifact. Symmetric in rigor with `W94`'s original closure (both reconstruction /
  strong-argument grade), and it **removes** `W94`'s survival claim.

**What would move it most.** (a) The `W87` deciding computation (full FRG `beta_{f_2^2}`): `f_2^2* = 0`
(HORN K) **confirms** the interacting ghost is genuinely indefinite -> the break stands; `f_2^2* > 0`
(HORN Q) makes the ghost removable -> `P3` fails and the closure is vacuous anyway (still not a genuine
survival). Either FRG outcome is consistent with BREAKS-AT-1. (b) A proof that the physical ghost coupling
is UV-soft faster than `1/k` (would open the one survival window -- but the derivative coupling of Weyl^2
gravity argues against it). (c) A continuum interacting Krein double-cone modular-conjugation theorem
(would be needed for **any** survival of `P1`/`P2`; it does not exist and this swing gives a mechanism for
why it should not).

---

## 6. What this does NOT do

No GU claim-status, `CANON.md`, `RESEARCH-STATUS.md`, verdict, or public-posture change. No external
action; all citations are read-only literature. The conjecture remains a conjecture; H61/H61a remain
**OPEN**. The result of this swing is that the **sectorial closure is demoted** from "sectorially closed
(theorem on the toy + strong argument for GU)" to "**finite-mode / mode-diagonal toy artifact that
BREAKS-AT-1 in the interacting continuum**": for a genuine finite type-III_1 spacetime region under a
non-UV-soft interaction, the bounded regional `J_O` (`P1`) does not exist, overlap coherence (`P2`) breaks,
and `P3` survives only at `P1`'s expense -- the three never hold together. This branch **presents, does
not decide** -- it hands the orchestrator: the larger interacting Krein-doublet model, the three-property
simultaneous break (`W98` T1-T7), the mass-gap escape killed (`W98` T3), the `P1`-vs-`P3` mutual-exclusivity
resolution (`W98` T5), the overlap-coherence break (`W98` T6), and the honest verdict -- **BREAKS-AT-1** --
conditional on the named load-bearing assumption and at honest grade. Reproducible:
`tests/W98_break_sectorial_closure.py` (7/7, exit 0).
