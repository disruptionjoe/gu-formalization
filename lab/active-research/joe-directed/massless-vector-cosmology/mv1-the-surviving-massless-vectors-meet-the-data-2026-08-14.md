---
artifact_type: exploration
status: exploration
doc_type: phenomenological-exclusion-gate
created: 2026-08-14
work_item: MV-1
channel: massless_vector_cosmology_and_laboratory_bounds
title: "MV-1: the 9 non-SM massless gauge directions PV-2 leaves in k fill out the full Pati-Salam algebra su(4)+su(2)_L+su(2)_R, and NONE of them is a free asymptotic quantum -- all 9 are charged under a confining non-abelian factor, so the naive dark-radiation count is wrong. After the best available SM-preserving adjoint VEV and electroweak breaking, GU-as-declared leaves EXACTLY ONE extra massless gauge boson beyond the SM's nine, and it is the gauged U(1)_{B-L}. Confronted with data it is excluded by ~24 orders of magnitude in the coupling by equivalence-principle tests, and independently at 7-26 sigma by N_eff -- but the N_eff arm is thermal-history-conditional and GU declares no thermal history. This is an EXCLUSION of GU-as-declared, not a recovery of physics, and it converges on the SAME missing object as MJ-2/MJ-5/BD-1."
grade: "EXACT for the counting side: integer Z[i] Clifford construction of so(10) on S+, exact rational Cartan covectors, exact rational adjoint-orbit sweep, exact rational one-loop beta coefficients, exact sympy Rationals for every dark-radiation and running formula, 54/54, exit 0, with five planted controls that fire. EMPIRICAL and explicitly NOT exact for the confrontation side: 18 measured inputs, each carrying a value, an uncertainty and a source, tabulated separately in the probe and never mixed into the certificate. NOT: a thermal history for GU, a cross-section computation, a lattice confinement scale, a Stueckelberg analysis, a statement about SG4, or any claim-status movement."
disposition: NINE_SURVIVORS_COMPLETE_THE_PATI_SALAM_ALGEBRA__ZERO_ARE_FREE_ASYMPTOTIC_QUANTA__NAIVE_DARK_RADIATION_COUNT_REFUTED__EXACTLY_ONE_EXTRA_MASSLESS_BOSON_AT_LAB_ENERGIES_AND_IT_IS_GAUGED_B_MINUS_L__EXCLUDED_BY_24_ORDERS_IN_g_BY_EP_TESTS__N_EFF_ARM_IS_THERMAL_HISTORY_CONDITIONAL__STUECKELBERG_ESCAPE_OPEN_AND_SOURCE_SILENT__SG4_UNTOUCHED
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - lab/active-research/joe-directed/photon-extra-vector-spectrum/pv1-available-orbits-retain-an-extra-massless-vector-2026-08-14.md
  - lab/active-research/joe-directed/photon-extra-vector-spectrum/pv2-observation-cannot-reach-the-extra-vectors-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/mj2-no-native-126-carrier-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/mj5-b-minus-l-exactly-preserved-2026-08-14.md
  - lab/active-research/joe-directed/baryon-number-and-proton-decay/bd1-b-violation-lives-only-in-the-removed-coset-2026-08-14.md
  - lab/active-research/joe-directed/anomaly-cancellation/ac1-rs-content-cannot-obstruct-and-anomalies-cannot-select-2026-08-14.md
  - explorations/conditional-build/cb-a-representation-content-2026-08-05.md
  - canon/gu-forces-field-space-declaration-RESULTS.md
scripts:
  - tests/channel-swings/joe_directed_neff_fifth_force_massless_vector_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `CONVENTIONAL_COMPARATOR`.

# MV-1 — the surviving massless vectors meet the data

## 0. What this is, said first

**This route produces an EXCLUSION, not a recovery of physics.** It contains no
number that could be confirmed by a future measurement. Its entire value is that
the contact with data is fast and hard, and that it names the cheapest object GU
could declare in order to survive. Anyone reading it as "GU predicts something"
has misread it.

It also **refutes one claim it would have been natural to make**: that nine
extra massless gauge bosons give a catastrophic dark-radiation signal. They do
not, because all nine are charged under confining non-abelian factors. The
catastrophe is elsewhere, and it is worse.

---

## 1. Prior art, swept by mechanism and attributed

Swept before computing, by mechanism rather than label, over `*.md`, `*.py`,
`*.yaml`: `N_eff`, `Neff`, `effective number of neutrino species`, `BBN`,
`nucleosynthesis`, `dark radiation`, `extra radiation`, `fifth force`,
`long-range force`, `equivalence principle`, `Eot-Wash`, `Eotvos`,
`torsion balance`, `MICROSCOPE`, `lunar laser`, `Z prime`, `gauged B-L`,
`massless gauge boson`, `massless vector`, `extra massless`, `leptoquark`,
`confinement`, `Planck 2018`, `CMB-S4`.

**Genuinely absent from the repository:** `MICROSCOPE`, `Schlamminger`,
`Touboul`, `Eotvos parameter`, any composition-dependent long-range force, any
`Delta N_eff` *computation*, any confinement-scale estimate for a group other
than `SU(3)`, and any use of `Z'` in a phenomenological-bound sense (the `Z'`
hits are all group-theoretic bookkeeping).

**Present, and attributed:**

| what exists | where | grade there | relation to MV-1 |
|---|---|---|---|
| `Delta N_eff` / dark radiation named as a **potential observable face** of the protected `{q=0}` gapless edge mode, explicitly **bridge-gated**: "a *fiber-symbol* gapless mode descending to a *spacetime* massless field is a further leap", "magnitude unforced, bridge unowned" | `explorations/more-predictions-hunt-2026-07-21.md` (row C, lines 88, 323, 363-371, 474); `explorations/operator-grade-anomaly-banking-2026-07-21.md` (line 302) | proposal-grade, bridge-gated, **never computed** | **Different mechanism entirely.** That route is a topological edge mode whose descent to a spacetime field is unowned. MV-1's massless vectors are ordinary unbroken gauge directions of `k` whose existence is already exact (PV-2). MV-1 does **not** discharge that bridge and claims nothing about it. What MV-1 adds is the first actual `Delta N_eff` *number* in the repository, from a different object |
| The entire in-repo fifth-force literature is the **short-range Stelle-Yukawa** `(1/r)(1 + a e^{-mr})` from the massive spin-2 companion at scale `mu_DW`, checked against Eot-Wash/HUST sub-mm bounds; `alpha = 1/3` at `lambda ~ 45-52 um`; self-falsified at face value | `explorations/wave28/H49-...`, `explorations/wave30/H50-...`, `explorations/wave31/H51-...`, `explorations/track2-conditional-numbers-2026-07-13.md`, `explorations/lost-predictions-recovery-2026-07-21.md` | COMPUTED / ARGUED | **Disjoint mechanism.** That is a *massive scalar/tensor Yukawa in the gravity sector* with a finite range. MV-1 is a *massless vector in the gauge sector* with infinite range and a **composition-dependent** charge. The two use the same experiments and nothing else. MV-1 imports no `mu_DW` number and moves none |
| "Declare the leans and check against Eot-Wash / lunar-laser-ranging / planetary-ephemeris fifth-force bounds. **This is the CHEAPEST possible decisive test**... GU is dead on the bench, no source action required" | `explorations/two-track-perspective-sweep-2026-07-11/E-pragmatic-experimental.md` (lens 5, Q2/Q3; ranked item 2 at line 205ff) | perspective-pass route proposal | **MV-1 executes exactly this instruction, for a different sector than the one proposed.** The lens proposed it for `mu_DW`; MV-1 runs it for the gauge sector, where no postulate is needed because PV-1/PV-2 already fix the object exactly. Credit for the strategy is that lens |
| BBN and the CMB precision arena graded **SILENT / out of scope** for GU; "BBN is entirely out of GU's scope. Inherits LCDM" | `explorations/comparative-tensions-ledger-cosmo-gravity-2026-07-21.md` (lines 47, 82, 98) | comparative ledger | **MV-1 contradicts the scope statement in one direction only.** GU-as-declared is not silent on `N_eff`: an unconfined massless gauge boson in equilibrium is a hard radiation contribution. But see §6 target-claim D — this is *not* a GU prediction, because GU declares no thermal history. The ledger row is **not moved here** |
| **CB-A row A4**: "`so(10)` adjoint `Lambda^2 V_10` = 45, rank **5**. Exactly **2** SM-singlet `(1,1,0)` directions survive — `U(1)_Y` and `U(1)_X`... the extra `U(1)_{B-L}` is **forced by the rank of the carrier, not chosen**" | `explorations/conditional-build/cb-a-representation-content-2026-08-05.md` | EXACT weight-lattice | **The rank theorem is CB-A's, and standard SO(10) model building's.** MV-1 re-derives it as a control and claims **no novelty** for it |
| PV-1 `{13,15,19,25}`; PV-2 `21 = 12 + 9` with `6 LQ + 2 W_R + 1 Z'`; BD-1 `|Delta(B-L)| = 4/3` Pati-Salam typing; MJ-5 `B-L` exact; AC-1 anomaly-free | this channel cluster, 2026-08-14 | EXACT | **All four re-derived here as controls, no novelty claimed.** MV-1's own content begins at §3.2 |
| Standard `SU(4)_C` lore that unbroken Pati-Salam confines leptons, and the `K_L -> mu e` bound on PS leptoquarks | Pati-Salam (1974); named in BD-1 lens L5 | external, imported | Imported. MV-1 supplies the exact `b_0` arithmetic for GU's specific content and derives nothing from the lore |

**External literature that already owns the fifth-force half of this, and must
be credited:** P. Fayet's programme on a long-range force coupled to
`(eps_Q Q + eps_B B + eps_L L) e`, "involving `B-L` in a grand-unified theory,
presumably through `B-L - .61 Q`, inducing effectively a very small repulsive
force between neutrons" — Fayet, Phys. Lett. B (1986) and **PRD 97, 055039
(2018)**, `arXiv:1712.00856`, which derives `|eps_{B-L}| < 0.8 x 10^-24` from the
first MICROSCOPE results. **MV-1 claims no novelty for the bound or for its
derivation.** What is new here is only (i) the exact identification of GU's extra
massless vector *as* that boson from GU's own declared content, and (ii) the
exact demonstration that the `Q`-rotation Fayet notes is available cannot remove
the coupling to neutral matter.

---

## 2. Preflight — six lenses, each proposing a route

Run inline before computing. Each lens had to name a *route*, not an opinion.

**L1 — BBN/CMB cosmologist.** *Route:* do not count degrees of freedom and
multiply. `Delta N_eff` is a **thermal-history** quantity, and the load-bearing
input is the decoupling temperature, not the multiplicity. Compute the two
bracketing histories exactly — decoupled just before `e+e-` annihilation
(`T_X = T_nu`) and still coupled through it (`T_X = T_gamma`) — and derive
`(T_gamma/T_nu)^3 = 11/4` from entropy conservation rather than quoting it.
Then plant the control that decides whether the exclusion is real: run the
**same** formula for a species decoupling above the electroweak scale. If that
lands inside the Planck error bar, the exclusion is a claim about thermal
history and must be labelled as one.

**L2 — fifth-force / equivalence-principle experimentalist.** *Route:* the
question is not "is there an extra force" but "**what charge does it couple
to**". Compute the extra `U(1)`'s charge on the proton, the neutron and the
electron exactly, then on an electrically neutral atom. If that charge is
proportional to `Q`, bulk matter is neutral and there is essentially no bound.
If it is `B-L`, the charge of a neutral atom is the **neutron number**, the force
is composition-dependent, and the Eotvos parameter is the sharpest instrument
physics has. Warned in advance: the extra `U(1)` is only defined up to mixing
with the photon, so the escape must be closed for **every** mixing, not for one
basis choice.

**L3 — collider phenomenologist.** *Route:* expect the collider arm to be the
**weakest** of the three and say so rather than padding. Massless colour-charged
gauge bosons are not a resonance search; there is no peak to look for. The
collider-flavoured bound that does bite on Pati-Salam leptoquarks is
`K_L -> mu e`, and BD-1's lens L5 already warned that a parameter-free ratio
needs the quark-lepton flavour rotation, which the repository grades open.
Record the bound, do not manufacture a ratio.

**L4 — thermal-history specialist.** *Route:* the whole `N_eff` arm turns on
whether these states are ever in equilibrium. Compute `Gamma/H` **symbolically**
and read its temperature dependence. For a massless gauge boson coupled to
relativistic charged matter, `Gamma/H ~ alpha^2 M_Pl/T` *grows* as the universe
cools, so a boson that is ever in equilibrium never leaves. That makes the
escape narrow and quantifiable: name the `alpha` at which decoupling would
occur, and then check whether that `alpha` is compatible with the fifth-force
bound. **If it is not, the fifth force is the load-bearing kill and `N_eff` is
decoration.** This lens supplied the ordering of the whole gate.

**L5 — group-theory counting specialist.** *Route:* count **asymptotic states**,
not algebra directions. The 6 leptoquarks are not matter fields; they are 6 of
the 15 generators of `su(4)`, and if `su(4)` is unbroken the correct question is
whether `SU(4)` confines, not whether a triplet is confined by `SU(3)`. Compute
the one-loop `b_0` for `SU(4)`, `SU(3)` and `SU(2)_R` with GU's content as exact
rationals, and check the difference `b_0(SU(4)) - b_0(SU(3))` — if it is
positive the `SU(4)` strong scale is strictly above `Lambda_QCD` and leptons are
confined. Also: verify the `k` block structure by explicit `32x32` commutators,
not by dimension counting, or the direct-sum claim is unearned.

**L6 — honesty auditor.** *Route:* pre-register the four overclaims available
here. (i) "GU is excluded by cosmology" — the hardest contact is a torsion
balance and the very hardest is the existence of the free electron; cosmology is
the *weakest* of the three arms. (ii) "`Delta N_eff` = 9 x 2 x (4/7) x ..." —
almost certainly wrong, because confined states are not dark radiation; make the
probe test this against itself. (iii) "GU is dead" — canon grades SG4 the open
decider; this is GU-**as-declared**. (iv) Any test that passes because a number
was compared to itself. Plant controls that would *fail* the gate if the physics
were different, in every one of the three arms.

### Cheapest kill-or-switch, recorded before computing

> **If the extra unbroken `U(1)` turns out to be proportional to electric
> charge, the fifth-force arm is dead** — neutral bulk matter would carry no
> charge and the Eotvos bound would evaporate, leaving only the far weaker
> `N_eff` arm. Cost: one exact evaluation of the extra charge on `(p, n, e)`.
> Switch in that case: abandon the long-range arm, and put the whole weight on
> confinement plus `N_eff`.

### One credible contrary route, recorded before computing

> **A Stueckelberg mass.** An *abelian* gauge boson can be made massive with no
> Higgs and no charged scalar at all, by eating a shift-symmetric axionic mode.
> PV-1, MJ-2 and MJ-5 all test the **VEV** route only, and MJ-2's exact
> zero-multiplicity result for the 126 says nothing whatever about a
> Stueckelberg sector. If GU's declared bosonic content contains such a mode,
> the entire gate evaporates and nothing above survives. **MV-1 must compute
> the bound anyway, must state that this escape is open, and must not pretend
> that "no 126" implies "no mass".**

---

## 3. What was computed

`tests/channel-swings/joe_directed_neff_fifth_force_massless_vector_probe.py`,
**54/54 exact checks, exit 0**, on `_local/cas-venv` (sympy 1.14, numpy 2.5.1).

The probe prints **two reports and one certificate**, and the separation is
structural, not editorial:

- **PART I — EXACT.** Integer `Z[i]` Clifford construction of `so(10)` on `S+`
  (Jordan-Wigner, same discipline as MJ-1/MJ-3/BD-1), exact **integer** root
  vectors, exact rational Cartan covectors, an exact rational sweep of the
  adjoint orbit space, exact rational one-loop `b_0`, and exact `sympy`
  Rationals for every dark-radiation and running formula. Numpy is an integer
  array container only. **This is the 54/54.**
- **PART II — EMPIRICAL.** Eighteen measured inputs, each with a value, an
  uncertainty and a source, printed in a separate table. **Nothing in Part II
  enters the certificate, and no comparison in Part II is presented as exact.**
  A structural check enforces that every row carries all three fields.

Five controls are planted, and each would fire if the physics were different:

1. dropping the two colour Cartans from the SM-singlet test wrongly admits the
   six gluon roots — so the singlet criterion is the right one and not a shape
   accident;
2. the 126 weight `(1,1,1,1,1)` **is** an SM singlet with `B-L = -2` exactly, so
   `B-L` does not annihilate it and the orbit test **can** return 12 — it
   returns 13 only because GU-as-declared lacks that carrier;
3. a planted extra `U(1)` whose charge **is** the electric charge gives zero on
   every neutral atom for every mixing, so the escape test passes the escape
   when it should;
4. at `n_g = 6` the `SU(2)_R` factor is **not** asymptotically free, so the
   confinement argument would fail there;
5. the same `Delta N_eff` formula applied to a species decoupling above the
   electroweak scale returns `~0.054`, **inside** the Planck error bar.

---

## 4. Result — the exact counting side

### 4.1 The nine survivors complete the Pati-Salam algebra

> **`k = su(4) (+) su(2)_L (+) su(2)_R`, dimensions `15 + 3 + 3 = 21`, and the
> two blocks commute exactly as `32 x 32` matrices.** The 9 non-SM directions
> PV-2 leaves are not a miscellaneous remainder; together with the SM's 12 they
> are the **complete** unbroken Pati-Salam gauge algebra.

`su(4) = 8` gluons `+ u(1)_{B-L} + 6` leptoquarks. The leptoquarks are exactly
`(3,1)_{±2/3}` with `|Delta(B-L)| = 4/3` (BD-1 replayed); the two `W_R` are
exactly `(1,1)_{±1}` with `Delta(B-L) = 0`; the `Z'` is the `su(2)_R` Cartan
direction orthogonal to `Y` inside `span{T_3R, B-L}`.

### 4.2 THE CORRECTION — none of the nine is free dark radiation

> **Exactly ZERO of the 9 are free asymptotic massless quanta.**

Verified by explicit `32 x 32` commutators, not asserted: every one of the 6
leptoquarks fails to commute with another `su(4)` generator, and every `W_R`
fails to commute with another `su(2)_R` generator. The unbroken algebra
`su(4) + su(2)_L + su(2)_R` has **no abelian factor at all**, and the adjoint of
a simple algebra contains no singlet. With exact rationals,

```
b_0(SU(4)_C) = 44/3 - 4 n_g/3        b_0(SU(3)_C) = 11 - 4 n_g/3
b_0(SU(2)_R) = 22/3 - 4 n_g/3        b_0(SU(4)) - b_0(SU(3)) = 11/3, EXACTLY,
                                     and INDEPENDENT of the generation count
```

so every unbroken non-abelian factor is asymptotically free at `n_g = 3`
(`32/3`, `7`, `10/3`), and since a single unbroken `SU(4)` means
`alpha_4 = alpha_3` **identically**,
`log(Lambda_4/Lambda_3) = (2 pi/alpha)(1/b_3 - 1/b_4) > 0` exactly. **The `SU(4)`
strong scale is strictly above `Lambda_QCD`.**

**Consequence, and it is the reason this section exists:** a naive
"`Delta N_eff` from `9 x 2 = 18` extra degrees of freedom" would have been
**wrong**. Confined states are not dark radiation. That claim is not made here,
and the probe tests the point against itself.

**What replaces it is worse.** Leptons are the fourth colour of a confining
`SU(4)`. Below `Lambda_4` there are no free leptons. **The observation-only stage
is killed at the laboratory bench by the existence of the free electron, with no
cosmology involved at all** — and independently, by Wigner's theorem an exact
unbroken `SU(4)_C` forces `m_e = m_d` and `m_nu = m_u` exactly.

### 4.3 After the available VEV: exactly one extra massless vector, and it is `B-L`

PV-1's sweep, re-derived exactly here over the whole SM-preserving adjoint
direction space: unbroken dimensions `{13, 15, 19, 25}`, minimum 13, and **12
never occurs**. The structural reason, which is CB-A A4's and standard SO(10)
model building's and is claimed as neither's novelty here:

> An adjoint VEV is a Cartan element, so its centralizer contains the **whole**
> rank-5 Cartan. `rank(so(10)) = 5 > 4 = rank(SM)`. **An adjoint VEV cannot
> reduce rank**, so at least one `U(1)` beyond the SM survives at every point of
> the orbit space.

And composed with MJ-5: every SM-preserving adjoint VEV has weight zero, hence
`B-L` charge exactly zero, hence `exp(i theta (B-L))` fixes it. The SM Cartan
has rank 4; adjoining `B-L` gives rank 5. **`u(1)_{B-L}` is a genuinely new
unbroken direction, not a combination of SM generators, for every available
vacuum.** The SM Higgs neutral component has `Q = 0` and `B-L = 0` exactly, so
electroweak breaking preserves it too.

**Caveat on the electroweak step, stated rather than buried.** The Higgs used
here is the *Standard Model's* `(1,2)_{1/2}`, imported. CB-A row E3 proves that
`Lambda^2 V_10` (45) and `Sym^2 V_10` (1+54) — the whole 100-dimensional
rank-two internal tensor class — contain **zero** colour-singlet weak doublets
at any `Y`, so GU's declared bosonic content does not supply that Higgs from
that class. This does not affect the conclusion: **any** `(1,2)_{1/2}` has
`B-L = 0`, and MJ-5 says no SM-singlet with `B-L != 0` exists in either declared
field, so `u(1)_{B-L}` survives whether or not electroweak symmetry breaks at
all. If it does not break, the situation is strictly worse, not better.

> **FINAL COUNT. GU-as-declared leaves `8` gluons `+ 1` photon `+ 1` `B-L`
> boson `= 10` massless gauge bosons at laboratory energies. The Standard Model
> has 9. Exactly one extra, and it is the gauged, unbroken, anomaly-free (AC-1)
> `U(1)_{B-L}`.**

---

## 5. Result — the empirical confrontation

**Everything in this section carries measurement uncertainty and is NOT exact.**
Every input is tabulated in §7. Every conclusion below survives an
order-of-magnitude error in every input; none rests on a quoted digit.

### 5.1 (b) The long-range force — the load-bearing kill

Exact charge structure: proton `B-L = +1`, neutron `B-L = +1`, electron
`B-L = -1`. An electrically neutral atom `(Z, A)` has `Q = 0` exactly and
`B-L = A - Z = N` exactly. **The `B-L` charge of bulk matter is its neutron
number**, so the force is repulsive between all nucleons and composition
dependent, and `N/A` differs on every element pair used in an
equivalence-principle experiment.

**The escape is closed exactly.** The extra `U(1)` is only defined up to adding
a multiple of `Q` (photon kinetic mixing — precisely Fayet's `B-L - .61 Q`). For
**every** rational mixing `c`, `(B-L + c Q)` on a neutral atom is `N + c*0 = N`,
nonzero whenever `N >= 1`. No rotation of the two massless `U(1)`s makes bulk
matter neutral. The planted control confirms the test is not vacuous: an extra
`U(1)` whose charge *is* `Q` gives zero on every neutral atom, for every mixing.

Empirical conversion, with `eta = [alpha_{B-L}/(G m_u^2)] (q/mu)_Earth *
Delta(q/mu)`:

```
Delta(q/mu) for Ti/Pt          = 0.0598          (IUPAC atomic weights)
(q/mu) for Earth               ~ 0.4957 +- 0.01  (composition model)
G m_u^2/(hbar c)               = 5.821e-39       (CODATA 2018)
eta (MICROSCOPE Ti/Pt, final)  = (-1.5 +- 2.7)e-15   (Touboul et al., PRL 129, 121102, 2022)

=>  alpha_{B-L} < 1.1e-51,   g_{B-L} < 1.2e-25   (2 sigma)
```

Cross-checked against the literature: Fayet's published limit from the **first**
MICROSCOPE results is `|eps_{B-L}| < 0.8e-24` in units of `e`, i.e.
`g < 2.4e-25`; the final data are `~4x` better in `eta`, hence `~2x` in `g`. The
independent derivation here and the published limit agree.

What GU-as-declared gives: `g_{B-L}` descends from the `SU(4)` gauge coupling
and runs **logarithmically**. The exact abelian coefficient is
`b(U(1)_{B-L}) = 32 n_g/9 = 32/3` at `n_g = 3`, so
`1/alpha(IR) = 1/alpha(UV) + (b/2 pi) ln(mu_UV/mu_IR)`, linear in `1/alpha`.
Starting anywhere from `alpha_UV = 1/40` to an absurdly weak `1/1000`, and
running from anywhere between `10^3` GeV and `M_Pl` down to the lab, gives
`g_{B-L} ~ 0.1` to `1`.

> **GAP: about `10^24` in the coupling, about `10^48` in `alpha`, at the most
> conservative end of a three-order-of-magnitude range of UV ignorance.** The
> exact running law then says reaching the bound by running would need `~5.6e50`
> e-folds. There is no such scale.

### 5.2 (a) Dark radiation — real, but thermal-history-conditional

The surviving `B-L` boson **is** abelian, unconfined and coupled to every
charged species, so this one genuinely is dark radiation. Derived, not quoted:
entropy conservation with exact rational `g_{*s} = 11/2` before and `2` after
`e+e-` annihilation gives `(T_gamma/T_nu)^3 = 11/4` exactly. Then, for one
massless vector (`g_X = 2`):

```
still coupled through e+e- annihilation :  Delta N_eff = (8/7)(11/4)^(4/3) = 4.4032  exactly
decoupled just before it                :  Delta N_eff = 8/7               = 1.1429  exactly
```

Against `N_eff = 2.99 +- 0.17` (Planck 2018 TT,TE,EE+lowE+lensing+BAO) with the
SM value `3.044 +- 0.002`: a tension of **7.0 sigma to 26.2 sigma** using
Planck's own uncertainty. BBN-only gives the same verdict independently
(`Delta N_eff = -0.10 +- 0.21`, Yeh-Shah-Olive-Fields 2024).

**And here is the honest qualification, which is the most important sentence in
this section.** The same formula applied to a species decoupling above all SM
thresholds (`g_{*s} = 427/4`) gives `Delta N_eff = 0.054`, **inside the Planck
error bar**. So the exclusion comes **entirely** from the claim that this boson
never decouples — not from its existence. That claim is defensible: exactly,
`Gamma/H ~ alpha^2 M_Pl/T`, which *grows* as the universe cools, so a gauge
boson that is ever in equilibrium never leaves; decoupling at `T ~ 1` MeV would
need `alpha_{B-L} <~ 10^{-10}`, eight orders below the gauge value. But it is a
thermal-history claim, and **GU declares no thermal history**. See §6, target
claim D.

### 5.3 (c) The colour-triplet leptoquarks — confined, and the collider arm is weak

Handled carefully rather than assumed, per lens L5. The 6 leptoquarks are **not**
separate matter fields; they are 6 of the 15 generators of `su(4)`. Two regimes,
and both are covered:

- **`SU(4)` unbroken** (observation-only stage): the correct question is whether
  `SU(4)` confines, not whether an `SU(3)` triplet does. It is asymptotically
  free with GU's content (`b_0 = 32/3`), sits well below the conformal-window
  edge (`~12 +- 2` Dirac fundamentals, lattice-informed, **not** exact), and has
  `Lambda_4 > Lambda_QCD` exactly. It confines. Leptons are confined with it —
  §4.2.
- **`SU(4)` broken by the available adjoint VEV**: the leptoquarks are massive
  and leave the massless spectrum entirely. They are then a `K_L -> mu e`
  question, bounded at `B < 4.7e-12` (BNL E871, Ambrose et al., PRL 81, 5734,
  1998), and per BD-1's lens L5 there is **no parameter-free ratio** to predict
  because the quark-lepton flavour rotation is open in this repository. No ratio
  is manufactured here.

**The collider arm is the weakest of the three and is reported as such.** There
is no resonance search for a massless gauge boson.

---

## 6. Hostile review, claim-indexed

Per `explorations/claim-indexed-verdict-doctrine-2026-08-12.md`, every verdict
below is bound to the exact claim it targets.

### Strongest overclaim available: "GU is excluded by cosmology"

Attacked hard, and it fails on three separate counts.

1. **Wrong discipline.** Cosmology is the **weakest** of the three arms. The
   hardest contact is a torsion balance (`10^24` in the coupling), and the very
   hardest is the existence of the free electron. The `N_eff` arm is 7-26 sigma
   but is conditional on a thermal history GU does not declare. Anyone quoting
   this gate as a cosmological exclusion has picked the softest available
   evidence.
2. **Wrong scope.** `canon/gu-forces-field-space-declaration-RESULTS.md`
   establishes SG4 as the **open decider** on field space. Every result here is
   GU-**as-declared**.
3. **Unstated dynamical assumption.** Everything above presumes the surviving
   directions are propagating vector fields with Yang-Mills kinetic terms and
   gauge-strength couplings to the observed fermions. That is the standard
   reading of a gauge structure group; it is **not derived** in this repository
   for GU's connection sector, and it is load-bearing for every number in §5.

**Verdict.** The claim *"GU-as-declared, with observation as the only breaking
mechanism, describes the observed low-energy world"* — **candidate killed**, by
lepton confinement, at the bench. The claim *"GU-as-declared, with observation
plus the best available SM-preserving adjoint VEV plus electroweak breaking,
describes the observed low-energy world"* — **candidate killed**, by
equivalence-principle tests, by `~24` orders of magnitude in the coupling. The
claim *"GU is excluded"* — **NOT-YET-FALSIFIED**: SG4 is open and one declared
object removes both kills at once.

### Strongest contrary construction: a Stueckelberg mass for `U(1)_{B-L}`

This is the real threat to the gate and it was pre-registered in §2. An
**abelian** gauge boson can be given a mass by eating a shift-symmetric axionic
mode, with **no Higgs, no charged scalar, and no 126**. PV-1, MJ-2 and MJ-5
between them test only the VEV route. MJ-2's exact zero multiplicity for the 126
is silent on a Stueckelberg sector. If GU's declared bosonic content contains
such a mode with the right coupling, §5.1 and §5.2 both evaporate completely.

**Verdict on the contrary construction: source-silent, and it is the cheapest
surviving escape.** Not excluded, not supported. Classified **type-missing** in
GU's declared content: no artifact in the repository types a shift-symmetric
sector for the internal gauge algebra. **This is the single most important open
item this gate produces**, and it is the next gate (§8).

### Weakest reproducibility seam

Two, and both are in Part II, never in the certificate.

1. **The Earth composition number** `(q/mu)_Earth ~ 0.4957` is a geochemical
   model input, taken from the EP-test literature and **not certified anywhere
   in this repository**. It enters the `eta -> g_{B-L}` conversion linearly. An
   error of a factor of two moves the bound by a factor of two, against a gap of
   `10^24` — but the seam is real and unowned.
2. **Thermalisation is argued from a scaling, not computed.** `Gamma/H ~
   alpha^2 M_Pl/T` is exact as a scaling; the `O(1)` coefficient is not
   computed, and no cross-section appears anywhere. The conclusion is robust by
   eight orders of magnitude, but the seam is that no Boltzmann equation was
   solved.

### Other classified targets

- *"GU-as-declared predicts `Delta N_eff` between 1.14 and 4.40"* —
  **type-missing**. `Delta N_eff` is not a prediction of GU; it is a consequence
  of bolting a standard thermal history onto GU's spectrum. GU declares no
  reheating temperature and no initial state. Stated as a prediction it would be
  an import wearing GU's name.
- *"Nine extra massless gauge bosons give a catastrophic `Delta N_eff`"* —
  **route killed**, by §4.2, by this artifact, against itself. Confined states
  are not dark radiation.
- *"The extra `U(1)` can be rotated away against the photon"* — **route
  killed**, exactly, §5.1, with a control proving the test can pass.
- *"Proton decay bounds apply to the surviving leptoquarks"* — already **route
  killed** by BD-1; not re-litigated, and no proton-decay bound is imported here.

---

## 7. Claim ceiling

### What is exact

The 54/54 certificate covers, and covers only: the Clifford construction and the
`21/24` split; `k = su(4)+su(2)_L+su(2)_R` by explicit commutators; the
identification and exact rational quantum numbers of the 9 survivors; the
SM-singlet subspace of the adjoint and the `{13,15,19,25}` sweep; the rank
theorem and the `B-L` theorem; the final count `10` vs `9`; that zero of the 9
are free asymptotic quanta; the one-loop `b_0` rationals and
`b_0(SU(4)) - b_0(SU(3)) = 11/3`; the `Lambda_4 > Lambda_3` inequality; the
`B-L` charges of nucleons, the electron and neutral atoms; the closure of the
kinetic-mixing escape; the abelian running law; and the `Delta N_eff` and
`(T_gamma/T_nu)^3 = 11/4` formulas as symbolic identities.

### Every empirical input, with uncertainty and source

| input | value | uncertainty | source |
|---|---|---|---|
| `N_eff` (CMB) | 2.99 | `+-0.17` (68% CL) | Planck 2018 results VI, A&A 641 A6 (2020), TT,TE,EE+lowE+lensing+BAO |
| `N_eff` (SM) | 3.044 | `+-0.002` | Froustey-Pitrou-Volpe JCAP 12(2020)015; Bennett et al. JCAP 04(2021)073 |
| `Delta N_eff` (BBN only) | -0.10 | `+-0.21` (68% CL) | Yeh-Shah-Olive-Fields, JCAP 06(2024)006 |
| `eta` (Ti/Pt) | `-1.5e-15` | `+-2.7e-15` (1 sigma, stat+syst) | Touboul et al. (MICROSCOPE), PRL 129, 121102 (2022) |
| `eta` (Be/Ti) | `0.3e-13` | `+-1.8e-13` | Schlamminger et al. (Eot-Wash), PRL 100, 041101 (2008) |
| `eps_{B-L}` limit | `0.8e-24` (units of `e`) | upper limit, first MICROSCOPE results | Fayet, PRD 97, 055039 (2018), arXiv:1712.00856 |
| `G m_u^2/(hbar c)` | `5.821e-39` | `+-1e-4` relative | CODATA 2018 |
| `alpha_s(M_Z)` | 0.1180 | `+-0.0009` | PDG 2024 |
| `Lambda_QCD^(5)` | 0.21 GeV | `+-0.01` | PDG 2024 |
| `m_e` | 0.51099895 MeV | `+-1.5e-7` | CODATA 2018 |
| `m_d(2 GeV)` | 4.70 MeV | `+-0.07` | PDG 2024 |
| `m_u(2 GeV)` | 2.16 MeV | `+0.49/-0.26` | PDG 2024 |
| `sum m_nu` | `< 0.12` eV | 95% CL | Planck 2018 + BAO |
| Earth `(B-L)/mu` | 0.4957 | `+-0.01` (composition model) | standard geochemical composition, as used in the EP-test literature |
| Ti, Pt `(B-L)/mu` | 0.5404, 0.6002 | `+-1e-5` | IUPAC 2021 standard atomic weights |
| `B(K_L -> mu e)` | `< 4.7e-12` | 90% CL | BNL E871, Ambrose et al., PRL 81, 5734 (1998) |
| `SU(4)` conformal-window edge | `~12` Dirac fundamentals | `+-2`, large theory uncertainty | lattice / Schwinger-Dyson estimates; order of magnitude only |

### Every thermal-history assumption, declared not buried

1. **The universe was once hotter than `~1` MeV** and reached a radiation-
   dominated thermal state including the SM plasma. GU declares no reheating
   temperature; this is imported from standard cosmology.
2. **The `B-L` boson thermalises.** Argued from `Gamma/H ~ alpha^2 M_Pl/T > 1`
   at any temperature below `~alpha^2 M_Pl`, not from a solved Boltzmann
   equation. Decoupling would require `alpha_{B-L} <~ 10^{-10}` at `T ~ 1` MeV.
3. **Its decoupling temperature relative to `e+e-` annihilation is unknown**, and
   the two bracketing cases are reported rather than one being chosen. The true
   value is expected at the coupled end, but that is not computed.
4. **No entropy is injected** between BBN and recombination.
5. **Three generations**, `n_g = 3`, for every `b_0`. The generation count is
   graded open in this repository; the `b_0(SU(4)) - b_0(SU(3)) = 11/3` result
   is deliberately `n_g`-independent so the confinement argument does not depend
   on it.

### Two further imported assumptions, declared

6. **The surviving gauge directions are propagating Yang-Mills fields** with
   canonical kinetic terms and gauge-strength couplings to the observed
   fermions. Standard reading of a structure group; **not derived** here for
   GU's connection sector. Load-bearing for every number in §5.
7. **The electroweak Higgs is imported.** CB-A row E3 excludes the whole
   rank-two internal tensor class as an SM-Higgs parent, so GU's declared
   bosonic content does not supply it. §4.3 shows the `B-L` conclusion is
   independent of whether electroweak symmetry breaks; the `10` vs `9` count is
   not.

### Not claimed

No statement about SG4's undeclared completion. No claim that the 24 `p`
directions are disposed of (PV-2 explicitly leaves that open). No mass matrix.
No cross-section, no lifetime, no branching ratio. No lattice computation of
`Lambda_4`. No Stueckelberg analysis. No claim-status movement, no canon or
ledger change, no `CURRENT-STATE.yaml` or `NEXT-STEPS.md` edit.

---

## 8. Standing, and the single decisive next gate

**Standing.** Composed with PV-1, PV-2, MJ-2, MJ-5, BD-1 and AC-1: GU-as-declared
retains a gauged, unbroken, anomaly-free `U(1)_{B-L}` whose gauge boson is
massless, which no declared mechanism can lift, and which is excluded by
equivalence-principle tests by roughly 24 orders of magnitude in its coupling.
The obstruction is **the same missing object** MJ-2, MJ-5 and BD-1 each found
independently: an SM singlet with `B-L != 0`. This gate is the fourth
independent phenomenological consequence of that single absence, and the first
one that is quantified.

**The single decisive next gate — MV-2.** *Does GU's declared bosonic content
contain a shift-symmetric mode that can Stueckelberg the `U(1)_{B-L}`?* It is
the cheapest thing GU could have that would dissolve this entire gate without
SG4, it is answerable with exactly the MJ-2 machinery (multiplicity of a
specific SM-singlet mode in `eps` and `$`), and it is currently **source-silent
and type-missing**. If the answer is no, this exclusion hardens and the `B-L`
carrier becomes the single most important object in the field-space declaration.
If the answer is yes, MV-1's §5 evaporates and only §4's exact counting
survives.

Selection stays inside this channel. Repository-wide GU priority is unchanged,
the superposition / source-residual workstream is untouched, and no ledger,
canon, or current-state surface moves.
