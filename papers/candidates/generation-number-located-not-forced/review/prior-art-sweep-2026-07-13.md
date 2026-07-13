# Prior-Art / Scoop Sweep -- "The Generation Number is Located, Not Forced"

**Target paper:** `papers/candidates/generation-number-located-not-forced/generation-number-located-not-forced-2026-07-11.md`
**Sweep date:** 2026-07-13. Web sweep (arXiv, journals, secondary). NOT committed; review artifact.
**Bottom line:** No scoop of the core theorem (class-wide residual-freedom no-go + the SU(2)_+ equivalence). But
three serious exposure points: (1) the "generation-blind Dai-Freed anomaly" leg is a KNOWN computation
(Davighi-Gripaios-Lohitsiri) the paper does not cite, and it is FALSE in the Spin-Z4 refinement unless scoped;
(2) Wang 2023 (arXiv:2312.14928) derives `N_f in 3Z` -- which EXCLUDES 1 -- under his assumptions, and the paper's
`{1,3}` claim will read as a contradiction unless the assumption-delta is stated; (3) the compactification
literature (generations = |chi|/2) forces the count from manifold data and must be explicitly classified as
"extra input" or a referee kills the no-go's framing in one line.

---

## 1. Citation resolution: "Wan-Wang-Yau"

**RESOLVED.** Three distinct real papers are being conflated across the repo:

- **Wan-Wang (NO Yau), 2019/2020:** Zheyan Wan, Juven Wang, *Beyond Standard Models and Grand Unifications:
  Anomalies, Topological Terms, and Dynamical Constraints via Cobordisms*, JHEP 07 (2020) 062,
  arXiv:1910.14668. (Full cobordism classification for SM/GUT gauge groups.)
- **Wang-Wan-You, 2021/2022:** Juven Wang, Zheyan Wan, Yi-Zhuang You, *Cobordism and Deformation Class of the
  Standard Model*, Phys. Rev. D 106, L041701 (2022), arXiv:2112.14765. (Deformation class as a function of
  `(N_f, n_nuR, p', q)`.)
- **Wan-Wang-Yau (WITH Yau), 2026:** Zheyan Wan, Juven Wang, Shing-Tung Yau, *Fermion Families and Pontryagin
  Class: Topological Field Theory via Colour Symmetry Extension*, arXiv:2605.26202 (May 2026). VERIFIED REAL
  (fetched 2026-07-13). This is the paper the repo's "arXiv:2605.26202" points at, and the correct referent for
  "Wan-Wang-Yau."

**Repo inconsistency to fix:** `explorations/wave33/H6-family-puzzle-theorem-2026-07-11.md` and
`explorations/path3-branchC-cobordism-2026-07-11.md` date "Wan-Wang-Yau" as "2019/2020" -- those beyond-cohomology
`p_1` statements belong to **Wan-Wang arXiv:1910.14668** (no Yau). The 2026 three-author paper is a different,
later result. The target paper itself says only "Wan-Wang-Yau" generically (Sections 1, 2, 7); it must cite
2605.26202 explicitly AND add 1910.14668 where the cobordism classification (not the family result) is meant.

Also relevant, same cluster: Juven Wang, *Family Puzzle, Framing Topology, c_- = 24 and 3(E8)_1 CFTs:
48/16 = 45/15 = 24/8 = 3*, arXiv:2312.14928 (Dec 2023) -- currently cited elsewhere in the repo ("Wang 2023")
but **absent from the target paper**, and it is the single closest published result (see Section 3 below).

---

## 2. Claim-by-claim verdicts

### Claim A: 3-primary LOCATION of the count (paper's characterization of the location prior art)

**Verdict: ADJACENT-FOUND, characterization mostly fair, two precision fixes required.**

- **Garcia-Etxebarria & Montero**, *Dai-Freed anomalies in particle physics*, JHEP 08 (2019) 003,
  arXiv:1808.00009. What they ACTUALLY claim: (i) the SM (and SU(5), Spin(10) GUTs) are anomaly-free under the
  refined Dai-Freed conditions; (ii) **gauged baryon triality (a Z/3, with `Omega^Spin_5(BZ_3) = Z/9`) has a
  Z/9 Dai-Freed anomaly that cancels iff the number of generations is a multiple of 3**; (iii) the
  `Spin-Z4` structure carries the Z/16 constraint. Fix: the paper should state (ii) precisely -- GEM's mod-3
  statement is CONDITIONAL on gauging a discrete symmetry beyond `G_SM` (an instance of the paper's "extra
  input," and strong support for the thesis, but it must be stated as their result, with the condition).
- **Wan-Wang-Yau arXiv:2605.26202** (2026). What they actually claim (fetched): using 5d spin bordism with
  discrete `Z_n` structures and the beyond-group-cohomology `p_1` sector, anomalies cancelable by **symmetry
  extension** (`1 -> Z_{N_c} -> Spin x Z_{N_c N_f} -> Spin x_{Z_2^F} Z_{2N_f} -> 1`), plus the requirements that
  baryons are fermions (`N_c` odd) and missing sterile neutrinos are replaced by a TQFT, single out
  **`N_c = N_f = 3` as the unique case**. They do NOT claim first-principles forcing -- the uniqueness is
  explicitly conditional. This is the paper's thesis instantiated by the adjacent group itself; the paper must
  cite it and name the delta (their added assumptions vs. the paper's minimal first-principles set).
- **Freed-Hopkins**, *Reflection positivity and invertible topological phases*, Geom. Topol. 25 (2021) 1165,
  arXiv:1604.06527. Characterization in Section 7 ("anomaly is a homomorphism, cobordism classification") is
  fair and standard.
- **Nielsen-Ninomiya / Callan-Harvey / Kaplan** (inflow leg): standard, fair. (Nielsen-Ninomiya, Nucl. Phys.
  B185 (1981) 20; Callan-Harvey, Nucl. Phys. B250 (1985) 427; Kaplan, Phys. Lett. B288 (1992) 342.)

### Claim B: "the SM Dai-Freed anomaly is generation-blind"

**Verdict: SCOOPED as a computation (this is a KNOWN result and must be cited as such), plus a scoping bug.**

- **Davighi, Gripaios, Lohitsiri**, *Global anomalies in the Standard Model(s) and Beyond*, JHEP 07 (2020) 232,
  arXiv:1910.11277. They compute `Omega^Spin_5(B(G_SM/Gamma_n))` for `n in {1,2,3,6}` via AHSS: **no global
  anomalies at all for two quotients, none beyond the Witten anomaly for the other two -- and the result holds
  "when the SM fermion content is extended arbitrarily"** (their abstract), a fortiori for any number of
  generations. The paper's Branch C statement "`Omega^Spin_5(BG_SM) (x) Z_(3) = 0`" is a corollary of their
  computed groups. The target paper currently cites GEM and Freed-Hopkins but **not DGL**; presenting
  generation-blindness as a finding of Branch C without citing DGL is the fastest public failure mode found in
  this sweep. GEM 1808.00009 and Wan-Wang 1910.14668 also independently establish SM Dai-Freed anomaly freedom.
- **Scoping bug:** generation-blindness is TRUE for the SM gauge group with plain spin structure, but **FALSE in
  the `Spin x_{Z2} Z4` refinement**: the Z/16 anomaly counts Weyl fermions mod 16, i.e., it is
  generation-SENSITIVE (each 15-Weyl generation contributes 1 mod 16; cancellation ties `N_f` to the number of
  right-handed neutrinos or a TQFT sector -- GEM 1808.00009; Wang-Wen, *Nonperturbative definition of the
  standard model*, Phys. Rev. Research 2, 023356 (2020), arXiv:1809.11171; J. Wang, *Ultra Unification*, Phys.
  Rev. D 103, 105024 (2021), arXiv:2012.15860). The paper must say "generation-blind FOR `G_SM` with spin
  structure; the Z4/B-L refinement is generation-sensitive mod 16 but 2-primary, hence coprime to the 3-primary
  arena" -- which actually STRENGTHENS the 2-vs-3-primary point, but only if stated.

### Claim C: the class-wide no-go ("not forced by first-principles topological selectors")

**Verdict: CLEAR as a theorem (no published statement of this form found), with mandatory boundary-drawing
against four adjacent "3 IS forced (given X)" literatures.**

No one has published "the generation number cannot be derived from anomaly/topological constraints" as a
theorem. Searches for that statement return only folklore ("anomalies cancel generation by generation, so
`N_gen` is unconstrained" -- textbook-level, stated in passing in many reviews) and its CONVERSES. The paper's
novelty (residual-freedom formulation, class-wide over four constructions, exact minimal missing input) stands.
But the no-go coexists with published results that DO force the count given extra structure, and each must be
named as an instance of "extra input" or the no-go reads as false:

1. **Compactification (the big one -- currently unhandled in the paper).** Candelas, Horowitz, Strominger,
   Witten, *Vacuum configurations for superstrings*, Nucl. Phys. B258 (1985) 46: `N_gen = |chi(CY_3)|/2` -- an
   index theorem forces the count once the compactification manifold/bundle is CHOSEN. Likewise Witten's
   Kaluza-Klein index counting (*Fermion quantum numbers in Kaluza-Klein theory*, Shelter Island II, 1983).
   **The paper never mentions this literature.** A referee will say "topology famously DOES determine the
   generation number -- chi/2." The answer is already the paper's thesis (the choice of internal manifold IS the
   non-first-principles extra input; the selector is not canonical), but the paper must SAY it, explicitly, in
   Sections 3 or 7. This is required, not optional.
2. **6d anomaly cancellation:** Dobrescu-Poppitz, *Number of fermion generations derived from anomaly
   cancellation*, Phys. Rev. Lett. 87, 031801 (2001), hep-ph/0102010 -- with SM fields in two universal extra
   dimensions, 6d global anomaly cancellation forces `N_gen = 3` (mod structure). Extra input: 6d spacetime.
   (Bordism-refined follow-up: Davighi-Lohitsiri, *Omega vs. pi, and 6d anomaly cancellation*, JHEP 05 (2021)
   267, arXiv:2012.11693.)
3. **331 models:** `SU(3)_c x SU(3)_L x U(1)_X` anomaly cancellation + asymptotic freedom forces `N_gen = 3`
   (Singer-Valle-Schechter; Pisano-Pleitez, Phys. Rev. D 46 (1992) 410; Frampton, Phys. Rev. Lett. 69 (1992)
   2889). Extra input: enlarged gauge group with inter-generation anomaly cancellation.
4. **Discrete-symmetry Dai-Freed:** GEM's Z/9 baryon triality result (above) and WWY 2605.26202's conditional
   uniqueness. Extra input: gauged discrete symmetry / symmetry-extension requirement.
5. **Precedent for a published generations no-go:** Distler-Garibaldi, *There is no "Theory of Everything"
   inside E8*, Commun. Math. Phys. 298 (2010) 419, arXiv:0905.2658 -- proves 3 generations (even 1, without
   mirrors) cannot embed in E8. Different class (rep-theoretic embedding, not topological selectors), but it is
   the closest published "no-go theorem about the generation number" and should be cited as precedent for the
   genre.

### Claim D: the forced content -- count in `{1, 3}`, 3-primary, ceiling `3 = dim Lambda^2_+`

**Verdict: CLEAR on the specific statement; ADJACENT-FOUND with an apparent-contradiction risk vs Wang 2023.**

- **Juven Wang, arXiv:2312.14928** (Dec 2023): from framed/string bordism `Z_24`, `c_- = 0 mod 24` modular
  invariance, `w1-p1` bordism `Z_3` class, derives **`N_f in 3Z` -- a multiple of 3, which EXCLUDES `N_f = 1`**
  -- under the assumption that families of 16 Weyl fermions are "topologically robust" (his framing/anomaly-free
  conditions). This is the closest published result to the paper's Result 2 and lives in exactly the paper's
  arena (`pi_3^s = Z/24`, 3-Sylow). The paper's `{1,3}` (which ADMITS 1) is not in contradiction -- Wang's
  conclusion needs his robustness/modular-invariance postulates, which are precisely non-first-principles extra
  input by the paper's standard -- but without an explicit sentence naming that delta, a referee will read
  `{1,3}` vs `3Z` as one of the two papers being wrong. Currently 2312.14928 is not cited in the target paper
  at all. **Mandatory addition.**
- The `3 = dim Lambda^2_+(R^4)` ceiling and the oddness-excludes-2 derivation: no prior statement found
  (searches below). CLEAR.

### Claim E: the SU(2)_+ reduction (forcing 3 <=> family bundle = self-dual frame adjoint; spin-flavor
identification not supplied by first principles)

**Verdict: CLEAR on the equivalence theorem; ADJACENT-FOUND on the surrounding idea -- there is a whole
spacetime-flavor-identification literature the paper currently does not engage, and it must.**

- **Nesti-Percacci**: *Graviweak unification*, J. Phys. A 41 (2008) 075405, arXiv:0706.3307 -- identifies the
  (anti-)self-dual `SU(2)` half of the complexified Lorentz algebra with weak isospin `SU(2)_L` (or `SU(2)_R`).
  *Chirality in unified theories of gravity*, Phys. Rev. D 81 (2010) 025010, arXiv:0909.4537 -- embeds gravity +
  SO(10) GUT in SO(3,11), obtaining **one chiral family** from a Majorana-Weyl representation. Directly on
  point: they IDENTIFY a chiral frame `SU(2)` with an internal quantum number **by construction** (isospin, not
  flavor), and they get 1 family, not 3. This is a live example of the paper's C1-type move being POSTULATED
  rather than derived -- exactly the paper's point, and the paper's C1 argument (answer-as-premise) applies to
  them cleanly. The paper should engage them by name: its equivalence theorem explains WHY such constructions
  must insert the identification by hand.
- **Woit**, *Euclidean Twistor Unification*, arXiv:2104.05099: same chiral-frame-`SU(2)`-as-internal-symmetry
  move (one `Spin(4)` factor -> gravity, the other -> weak); Woit explicitly states the framework does NOT
  explain why there are 3 generations. Supports, does not scoop.
- **Spinor family unification** (spacetime-flavor identification postulated at the group level): BenTov-Zee,
  *The Origin of Families and SO(18) Grand Unification*, Phys. Rev. D 93 (2016) 065036, arXiv:1505.04312;
  Wilczek-Reece-et al. lineage *A Model of Comprehensive Unification* (SO(3,11)), Phys. Lett. B 774 (2017),
  arXiv:1706.03116; Mankoc-Borstnik spin-charge-family theory (e.g. arXiv:2108.05718) -- families from enlarged
  spin/Clifford structure. In all of these the spin-flavor identification is an INPUT. No one states, let alone
  proves, the paper's equivalence ("forcing 3 <=> family bundle = `Lambda^2_+` adjoint"). CLEAR on the theorem;
  the related-work section needs one sentence covering this family so the paper cannot be accused of ignoring
  the literature that does what C1 describes.

### Claim F: has "3 generations = dim of self-dual 2-forms / su(2) adjoint" appeared anywhere?

**Verdict: CLEAR.** No hit for generations-as-`Lambda^2_+` in any searched form (self-dual 2-forms, su(2)_+
adjoint, chiral frame triplet as family index). The adjacent "algebraic 3" literature derives 3 from different
structures: 3x3 octonionic Hermitian matrices / SO(8) triality -- Dubois-Violette, *Exceptional quantum geometry
and particle physics*, Nucl. Phys. B 912 (2016) 426, arXiv:1604.01247; Todorov-Dubois-Violette, Int. J. Mod.
Phys. A 33 (2018), arXiv:1806.09450; Boyle, *The Standard Model, the exceptional Jordan algebra, and triality*,
arXiv:2006.16265; Furey-Hughes, *Three generations and a trio of trialities*, arXiv:2409.17948. Distinct
mechanism (triality / J3(O) diagonal, not `Lambda^2_+`); cite one sentence to preempt "octonion people did
this."

---

## 3. Biggest mischaracterization risks, ranked

1. **Generation-blindness presented as the paper's own finding** (Sections 3 and 7). It is a corollary of
   DGL arXiv:1910.11277 (and GEM 1808.00009 / Wan-Wang 1910.14668). Cite as known; claim only the 3-primary
   corollary framing. AND scope it: the `Spin-Z4` Z/16 anomaly is generation-sensitive (2-primary), so
   "generation-blind" without qualification is false as a blanket statement about "the SM Dai-Freed anomaly."
2. **Silence on compactification.** `N_gen = |chi|/2` (Candelas et al. 1985) is the most famous
   topology-determines-generations statement in physics. The no-go MUST classify manifold/bundle choice as
   extra input explicitly, or the abstract's "not forced by first-principles topological selectors" gets
   dismissed on first read.
3. **`{1,3}` vs Wang 2023's `N_f in 3Z`.** Same arena (`Z/24`, 3-primary), opposite-looking conclusions about
   `N_f = 1`. State the assumption delta or it reads as a contradiction with the closest prior work -- which the
   paper does not even cite.
4. **"Wan-Wang-Yau" dating/attribution.** WWY = arXiv:2605.26202 (2026) only; the 2019/2020 beyond-cohomology
   `p_1` results are Wan-Wang 1910.14668. Repo files currently mix these (see Section 1). In the target paper,
   add explicit arXiv numbers.
5. **GEM's mod-3 statement stated unconditionally.** Their `N_gen in 3Z` requires gauging baryon triality --
   state the condition (it is support for, not competition with, the thesis).
6. **Nesti-Percacci non-engagement.** Cannot imply spin-flavor identification is unexamined; it is a
   literature. The paper's contribution is proving the identification is exactly what forcing 3 costs.

---

## 4. Related-work text the paper needs (drop-in sentences)

For Section 7, replacing/extending the current four bullets:

- "Location of the count in the 3-primary / mod-3 arena: Garcia-Etxebarria-Montero (arXiv:1808.00009) show that
  gauging baryon triality yields a Z/9 Dai-Freed anomaly cancelling only for generation numbers divisible by 3;
  Wang (arXiv:2312.14928) derives N_f in 3Z from framed/string-bordism (Z_24) and c_- = 24 modular-invariance
  constraints; Wan-Wang-Yau (arXiv:2605.26202) single out N_c = N_f = 3 as the unique solution given odd colour
  number, a Z_{N_c} colour symmetry extension, and TQFT replacement of missing sterile neutrinos. Each forces
  the count only given a further condition (a gauged discrete symmetry; topological robustness of the 16-Weyl
  family; the extension ansatz) -- instances, in our language, of extra input closing the residual freedom, and
  in particular our {1,3} bound admits the sterile N_f = 1 solution precisely because we do not assume them."
- "Generation-blindness of the SM anomaly: freedom of the four SM gauge-group quotients from global anomalies
  for arbitrary fermion content -- hence for any generation number -- was established by Davighi, Gripaios and
  Lohitsiri (arXiv:1910.11277) via Omega^Spin_5(BG_SM/Gamma_n), and by Garcia-Etxebarria-Montero and Wan-Wang
  (arXiv:1910.14668) in the Dai-Freed/cobordism setting; we use only the 3-primary corollary
  Omega^Spin_5(BG_SM) (x) Z_(3) = 0. In the Spin x_{Z2} Z4 refinement the Z/16 anomaly does count fermions mod
  16 (arXiv:1808.00009; Wang-Wen arXiv:1809.11171) -- a generation-sensitive but 2-primary constraint, coprime
  to the 3-primary arena where the count lives."
- "Topology does force the count once compactification data is chosen: N_gen = |chi|/2 for Calabi-Yau
  compactifications (Candelas-Horowitz-Strominger-Witten, Nucl. Phys. B258 (1985) 46) and Kaluza-Klein index
  counting (Witten 1983). Our no-go is the statement that the choice of internal manifold and bundle is itself
  the non-canonical extra input: no such selector is supplied by first principles. Likewise 6d anomaly
  cancellation (Dobrescu-Poppitz, hep-ph/0102010; Davighi-Lohitsiri, arXiv:2012.11693) and 331-type gauge
  extensions force 3 at the cost of assuming the enlarged arena."
- "Identifying frame chirality with internal quantum numbers has been proposed, not derived: graviweak and
  graviGUT unification identify the self-dual SU(2) with weak isospin and obtain one family from SO(3,11)
  (Nesti-Percacci, arXiv:0706.3307, arXiv:0909.4537; cf. Woit, arXiv:2104.05099, where the generation number is
  explicitly left unexplained), and spinorial family unification posits families inside enlarged spin
  representations (BenTov-Zee, arXiv:1505.04312; arXiv:1706.03116; Mankoc-Borstnik). Our Result 3 explains the
  pattern: forcing 3 is equivalent to such an identification, which is why these constructions must insert it
  as a premise. A precedent for a rigorous no-go about generation embedding is Distler-Garibaldi
  (arXiv:0905.2658) for E8."
- "Algebraic derivations of 3 from 3x3 octonionic / triality structure (Dubois-Violette, arXiv:1604.01247;
  Todorov-Dubois-Violette; Boyle, arXiv:2006.16265; Furey-Hughes, arXiv:2409.17948) select the count from a
  chosen algebra rather than from Lambda^2_+; the algebra choice is again extra input in our sense."

---

## 5. Search trail

Fetched directly (2026-07-13):
- arXiv:1808.00009 abstract page (GEM claims: Z/9 baryon triality -> N_gen in 3Z; SM Dai-Freed anomaly-free).
- arXiv:2112.14765 abstract page (authors Wang-Wan-You confirmed; deformation class w/ (N_f, n_nuR, p', q)).
- arXiv:2605.26202 abstract page (EXISTS; Wan-Wang-Yau, May 2026; conditional uniqueness of N_c = N_f = 3).
- arXiv:1910.11277 abstract page (DGL verbatim abstract; "extended arbitrarily" scope; Omega^Spin_5 via AHSS).

Web searches (all ran, non-empty unless noted):
1. GEM 1808.00009 + generations mod 3 -> confirmed Z/9 result.
2. Davighi Gripaios Lohitsiri Omega^Spin_5 -> 1910.11277 + Wan-Wang 1910.14668 + Wang-Wan-You 2112.14765.
3. Wan Wang Yau cobordism SM -> resolved the three-paper split.
4. Juven Wang "family puzzle" 2312 -> arXiv:2312.14928, N_f in 3Z from Z_24/framing.
5. Nesti Percacci graviGUT SO(3,11) -> 0706.3307, graviGUT one-family result; Woit 2104.05099 surfaced.
6. Distler Garibaldi E8 no-go -> arXiv:0905.2658, CMP 298 (2010) 419.
7. "three generations" + self-dual two-forms / Lambda^2_+ flavor -> **EMPTY for the specific identification**;
   only gauged SU(2)_f flavor-symmetry model-building (unrelated mechanism).
8. "number of generations" anomaly cancellation unconstrained -> folklore confirmations + Dobrescu-Poppitz
   PRL 87, 031801 + 331-model literature (both are "extra input forces 3" instances).
9. Dobrescu Poppitz 6d -> confirmed 3 generations from 6d global anomaly; Davighi-Lohitsiri 2012.11693 refinement.
10. Dubois-Violette Todorov Boyle exceptional Jordan -> triality-based 3; distinct from Lambda^2_+. No scoop.
11. Woit Euclidean twistor + generations -> Woit explicitly does NOT derive 3; supports Claim E's landscape.
12. "spin-flavor" unification from Lorentz/frame group -> BenTov-Zee SO(18) 1505.04312, comprehensive
    unification 1706.03116, Mankoc-Borstnik 2108.05718. All postulate the identification; none prove or forbid
    it. **EMPTY for any published equivalence or no-go of the paper's Result 3 form.**

Not found anywhere (searched, empty): "generation number not forced" as a theorem; "residual freedom" {1,3}
statement; the Schur/adjoint-vs-singlet argument applied to frame SU(2)_+ and family number; any prior
"located, not forced" formalization.

## 6. Per-claim verdict summary

| Paper claim | Verdict |
|---|---|
| Class-wide no-go (Result 1) | CLEAR as theorem; must draw boundary vs CHSW chi/2, Dobrescu-Poppitz, 331, GEM-Z9, WWY-2026 (all "extra-input forces 3") |
| SM Dai-Freed generation-blind | SCOOPED as computation (DGL 1910.11277; GEM; Wan-Wang) -- cite as known; scope out Spin-Z4 Z/16 |
| 3-primary location prior art characterization | FAIR with fixes: GEM's mod-3 is conditional; WWY = 2605.26202 (2026), Wan-Wang = 1910.14668 |
| {1,3} + ceiling 3 = dim Lambda^2_+ (Result 2) | CLEAR; state delta vs Wang 2312.14928 (N_f in 3Z excludes 1 under his assumptions) |
| SU(2)_+ reduction / equivalence (Result 3) | CLEAR on the theorem; engage Nesti-Percacci / Woit / BenTov-Zee as the postulated-identification literature |
| 3 = dim Lambda^2_+ identification anywhere | CLEAR (octonion/triality 3 is a different mechanism; one-line cite) |
