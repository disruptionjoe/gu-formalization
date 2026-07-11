# Science Advisory Council: the full picture after the conformal-Bach turn (2026-07-11)

A deep pass across the explorations corpus (985 files, scanned by theme) + the UCSD-2025 "Into the Impossible"
transcript (`papers/drafts/Transcript into the impossible.md`) + the 2026-07-11 source-action-narrowing arc,
assessed by a five-archetype council: **Orthodox professor, Heterodox-rigorous professor, Commercial
scientist, Philosopher of science, Wild mathematically-serious frontier scientist.** Council voices are
inline (one worker). Purpose: what are we MISSING when the pieces are put together.

## The pivot everything now turns on

The single biggest thing the corpus has not absorbed: **H-class GU's gravity sector IS conformal (Bach /
fourth-order Weyl) gravity on the spin-2 graviton** (`tests/threads/D_hclass_vs_conformal_gravity.py`:
`box^2 h = -4 Bach^(1)`, exact, differing only in the trace sector). The transcript independently predicts
exactly this: Weinstein says the second-order GU theory is "the SQUARE of the first-order (double copy)" and
that Einstein "anticipates Chern-Simons" via the contraction map -- a fourth-order/squared structure. This is
a **phase change** for how to read the whole program, because a large body of prior verdicts was computed
under two now-questionable premises: (a) the raw `(7,3)` Frobenius fiber form (not the physical
trace-reversed `(6,4)` DeWitt form), and (b) "the source action is an unknown object to be BUILT." A grep
confirms the 2026-07-11 vocabulary (`Bach`, `OQ2-A`, `DeWitt`, `H-class`) has NOT propagated into the older
corpus -- so those verdicts predate the reframe by construction.

**Discipline note (per the E honesty audit):** everything below is a set of HYPOTHESES-TO-TEST, not
established results. The conformal identification is proven only linearized, on spin-2. The "reopenable walls"
are candidates, each with a named decisive test -- not walls that are gone.

---

## The five voices

### Orthodox professor -- "you may have rediscovered a known, largely-refuted theory"
If H-class GU is Bach/conformal gravity, that is not a triumph, it is an EXPOSURE. Fourth-order gravity is
old (Weyl 1918, Stelle 1977, Mannheim) and carries known, unresolved problems: the **Ostrogradsky ghost**
(fourth-order kinetic term -> negative-energy states), a **contested Newtonian limit**, and the
**Horne / Hobson-Lasenby "no genuine flat rotation curves"** objection that conformal gravity has never
cleanly answered (`explorations/big-swing-2026-07-06/VG-SB-conformal-gravity-critical-line.md`). Meanwhile
the dark-energy leg -- previously scored a "YES" -- is now `(w0,wa)=(-0.768,-0.273)`, which NAILS `w0` but sits
**~3-4 sigma from DESI on `wa`** (`tests/threads/C_dark_energy_wz_vs_desi.py`), and its divergence-free
property rests on an **unproven Assumption 3** (`canon/dark-energy-theta-divergence-free.md`, CONDITIONALLY_
RESOLVED). Biggest thing missed: **the program keeps booking identifications as novelty when several of them
import a graveyard of known problems.** Stop calling "located-not-forced" a feature; a hostile referee reads
it as an under-determination you have redefined as a prediction.

### Heterodox-rigorous professor -- "the whole negative spine rides on an unforced signature choice"
The celebrated hard results -- the generation no-go, chirality-dead-by-theorem (net 0), located-not-forced --
all ride on the **unforced `Cl(9,5)=M(64,H)` reconstruction** (Nguyen's criterion-4 risk, still open). And
`explorations/sequential-goals-2026-07-09/SG1-signature-carrier-parity-77.md` shows the no-go is
**SIGNATURE-SPECIFIC**: `(9,5)` has `J^2=-1` (Kramers-even, blocks odd counts), but `(7,7)=M(128,R)` has
`J^2=+1` and exhibits an **odd-rank-3 J-projector**. So on the real `(7,7)` branch the odd generation count is
not under-determined -- it may be FORCED. And the `(7,7)`-vs-`(9,5)` choice is literally the OQ2-A H-class /
II-class binary under another name (`BIG-SWING-signature-9-5-vs-7-7-UNDER-DETERMINED.md`). Biggest thing
missed: **you have been hardening a no-go that an equally-defensible signature dissolves.** The real crux is
rep-canonicity -- WHICH signature is GU-native -- and it decides both the conformal-native question and
whether "3" is located or forced. Also, do not paper over the genuine new tension: the **mod-3 Dai-Freed
arena for SM data is empty** (`Omega^Spin_5(BG_SM) tensor Z_(3) = 0`), which is a prima-facie problem for
"the count lives in an odd-primary boundary invariant." Settle the signature before hardening anything else.

### Commercial scientist -- "you have three cheap decisive tests and keep doing narrowing passes instead"
Ruthless triage. There is exactly ONE test that clears or kills gravity: **ELProjectedGRShadowTheorem** --
does GU admit an exact Schwarzschild/Kerr section (`explorations/geometry-curvature-emergence/exact-
schwarzschild-kerr-el-gate-2026-06-24.md`, currently BLOCKED on the Willmore-only branch). The conformal lens
makes the outcome PREDICTABLE: **Bach gravity admits Schwarzschild as an exact vacuum solution** -- so run it,
it likely CLEARS the wall that has blocked the program for weeks. Second cheap decisive test: **verify the
DESI `(w0,wa)` against arXiv:2503.14738 Table 3 this week.** If it holds at 3-4 sigma, that is a real
FALSIFIABLE prediction -- worth more than ten consistency checks. Third: **ship the family-puzzle paper**
(`explorations/non-lnf-open-frontier-prioritized-2026-07-11.md`), the one GU-INDEPENDENT result ("forces odd
count => nonzero 3-Sylow image") that is credible regardless of whether GU is right. Biggest thing missed:
**the source-action buildbench may be solving a non-problem** -- if H-class GU is a known theory with a known
action (Weyl^2 / Bach), the "supply the missing carrier `L_theta_source`" loop
(`absorbed/gu-source-action/`) is building an object that already exists. Stop building; test.

### Philosopher of science -- "prioritize what can kill you; you're protecting where you should expose"
Two moves need adjudication as science-vs-rescue: **"located-not-forced as a feature"** and **"the
complexification gap as an interface slot"** (Nguyen 3.1, still Column-C-empty in
`explorations/nguyen-gu-critique/nguyen-critique-gap-assessment.md`). Both reframe a FAILURE as a FEATURE, and
the E-audit already caught the Lakatos degenerating signature (the "one remaining object" relocating five
times in a day while nothing is built). BUT -- and this is the healthiest thing in the whole program -- the
**conformal-Bach identification runs the OTHER way**: it is a risky, novelty-REDUCING, falsifiable
identification that EXPOSES GU to refutation (it makes GU inherit conformal gravity's ghost and rotation-curve
problems). That is exactly what a progressive research programme does. Biggest thing missed: **the program
spends its energy protecting the count (feature-framing) when it should spend it exposing the gravity sector
(the identification that can kill it).** And the deepest un-adjudicated question: is GU's **geometry-first
primitive** even right? The information-first / entropic-gravity antithesis (`explorations/persona-and-
dialectic/entropic-gravity-antithesis-information-first-2026-07-07.md`; Bianconi's 2026 entropy action
predicts a small positive Lambda that could MEET GU's theta dark-energy) is a fully-built adversary the
program has never run against the confirmed conformal identification. That specific combination is the single
most important un-run lens.

### Wild frontier mathematician -- "the highest-upside objects are sitting untouched"
Four unexploited objects, each a potential theorem:
1. **The `(6,4)` DeWitt fiber form admits the conformal group `so(4,2)` NATIVELY** (`VG-V3-j-commutant-
   conformal-native.md`: builds `u(3,2) -> su(2,2) ~ so(4,2)`). The old "conformal is not GU-native" kill was
   computed on the raw `(7,3)` form. If the physical `(6,4)` form is canonical, **GU may literally BE a
   conformal field theory on the space of metrics** -- chase it.
2. **SG1's odd-rank-3 projector on `(7,7)`** -- if that is the native signature, the generation count is
   FORCED and the entire "located-not-forced" story INVERTS. This is the single highest-value reopener.
3. **The section functor + causality-required obstruction**: the cross-leg coincidences (shared theta, single
   conjugate SM, `alpha_W <-> f_0`) as naturality squares of one functor (D2), AND the conjecture that the
   missing source action is forced by **VZ-causality** -- removing the ghost reinstates Velo-Zwanziger
   acausality (`explorations/firewall-and-two-geometries/source-action-necessary-conditions-and-causality-
   2026-06-27.md`). If true, the "missing object" is forced by causality, not bookkeeping -- a theorem, not a
   build. Note the transcript flags VZ as THE spin-3/2 risk and hints the escape is "no internal symmetry."
4. **The transcript's explicit generation mechanism**: Weinstein describes three generations as **2+1 with the
   third an "imposter"** from the **Rarita-Schwinger spinor product rule** (`Spin(V+W) = Spin(V) tensor
   Spin(W)` plus an RS cross-term). We have NEVER matched this concrete mechanism against our carrier A/B
   structure. It predicts the third generation reunifies at high energy -- a real, distinguishing claim.
Biggest thing missed: **the program routes effort into narrowing an already-reduced object while the objects
with actual theorem-and-discovery upside (conformal-native `(6,4)`, signature-forced count, causality-forced
action, the RS 2+1 mechanism) sit unexplored.**

---

## Walls that may not be walls (candidates to reopen, each with its decisive test)

These carry BLOCKED/OPEN verdicts issued BEFORE the conformal-Bach turn and on the raw `(7,3)` form. Each is a
hypothesis with a concrete test, not a settled reopening:

| Wall (current verdict) | Why it may not be a wall | Decisive test |
|---|---|---|
| `exact-schwarzschild-kerr-el-gate` (BLOCKED, strong-field fails) | Bach gravity admits Schwarzschild as an EXACT vacuum solution | Run ELProjectedGRShadowTheorem in the conformal/Bach branch |
| `BIG-SWING-CONFORMAL-CLASS-BLOCKED` / `VG-V3-j-commutant` ("conformal not GU-native") | Computed on raw `(7,3)`; the `(6,4)` DeWitt form admits `so(4,2)` natively | Redo the commutant/J-structure on the trace-reversed `(6,4)` form |
| Generation no-go / located-not-forced | Signature-specific; `(7,7)` `J^2=+1` gives an odd-rank-3 projector | Settle rep-canonicity `(9,5)` vs `(7,7)` = the OQ2-A binary |
| Source-action buildbench ("missing carriers") | If H-class GU = a known theory, the action already exists | Check whether Weyl^2/Bach + the fiber/gauge terms IS the S_IG spec |
| Dark-energy "YES" (four-legs scoreboard) | Now `~3-4 sigma` from DESI on `wa` | Verify vs arXiv:2503.14738 Table 3; re-run the theta INT gravity test |

## Genuine tensions the program must NOT paper over (the council is unanimous here)

1. **DESI `~3-4 sigma` on `wa`** -- a real, near-falsifying handle (verify the digits first).
2. **The mod-3 Dai-Freed arena is empty** (`Omega^Spin_5(BG_SM) tensor Z_(3) = 0`) -- challenges "the count is
   an odd-primary boundary invariant."
3. **Divergence-free dark energy rests on unproven Assumption 3** -- the DE leg's foundation is conditional.
4. **Ostrogradsky ghost** -- if H-class GU is Bach gravity, it inherits the fourth-order ghost problem; GU must
   state its position (`explorations/misc/external-quadratic-gravity-obligations-2026-06-30.md`).
5. **Nguyen 3.1 complexification** -- still unrefuted; the "interface slot" re-read is unadjudicated.

## The crux and the highest-leverage moves (council synthesis)

**Everything routes through ONE question the program has been treating as a convention: the native signature
`(9,5)` vs `(7,7)` (= the OQ2-A H-class / II-class binary).** It simultaneously decides (a) whether GU's
gravity is conformal-native on the `(6,4)` form, (b) whether the generation count is forced (`(7,7)`) or
located (`(9,5)`), and (c) which functional fixes `c_W`. It is a REP-CANONICITY question, not a build -- and
it is the one thing that would change the epistemic state (per the E-audit rule: only a forced construction or
a genuine discriminator counts).

Concrete, ranked, mostly-cheap next moves:
1. **Run ELProjectedGRShadowTheorem in the conformal/Bach branch** -- likely clears the gravity wall (cheap,
   decisive; Bach admits Schwarzschild).
2. **Settle rep-canonicity `(9,5)` vs `(7,7)`** -- the crux; decides forced-vs-located count AND
   conformal-nativeness. Redo the `J`-commutant on the `(6,4)` DeWitt form.
3. **Verify DESI `(w0,wa)` vs arXiv:2503.14738 Table 3**, then re-run the theta INT gravity intersection test
   with the corrected Willmore residual -- turns a consistency check into a falsifiable prediction.
4. **Do the full higher-codimension Willmore first variation** (the convergent top task from A/B/D) -- settles
   the H/II binary, signs B's Lambda candidate, tests D's conformal-invariance question. No new object.
5. **Run the information-first / entropic antithesis against the confirmed conformal identification** (Bianconi
   `+Lambda` meets GU theta) -- the un-run lens with the highest reframe potential.
6. **Ship the GU-independent family-puzzle paper** -- credible regardless of GU's fate.

## Grade
Synthesis / advisory. No new computation; the council REORGANIZES existing results + the transcript into a
decision map. The reopenable-walls table is a set of HYPOTHESES with named tests, not established reopenings.
Honest posture (E-audit): the conformal-Bach identification is the healthiest development because it is
falsifiable and novelty-reducing; the located-not-forced "feature" framing is the most at-risk of being an
unfalsifiable rescue and should be re-examined via the signature crux. Feeds WI-068 and NEXT-STEPS.
