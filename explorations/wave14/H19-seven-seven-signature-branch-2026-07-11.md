---
title: "H19 (Wave 14) -- THE (7,7) SIGNATURE BRANCH: does adopting Y^14 = Cl(7,7) = M(128,R) DERIVE three generations, or only PERMIT odd? Four questions computed on the actual reps. HEADLINE: ODD-ADMISSIBLE-BUT-NOT-3 (honest). (7,7) lifts a 2-primary VETO; it is structurally INCAPABLE of supplying the 3-primary count (|Hom(Z/8,Z/3)|=1); it is cheap (anomaly/SM/unitarity all survive; only predictivity narrows) but NOT GU-native (under-determined). LIVE-BUT-NON-DERIVING."
artifact_type: exploration
status: exploration
updated_at: "2026-07-11"
wave: 14
verdict: "ODD-ADMISSIBLE, NOT FORCED-3 (Q1, high conf); TRANSFERS-IN-SHAPE / CHANGES-IN-REALITY (Q2, med-high); LOW-COST / LESS-CONSTRAINING (Q3, med-high); NOT-GU-NATIVE (Q4, high). Net: adopting (7,7) is a live-but-non-deriving option -- it dissolves the (9,5) even-parity wall cheaply but neither derives 3 nor is selected by GU. The signature axis L7 lifts a 2-primary parity veto; the generation 3 lives in the orthogonal 3-primary (Z/3) arena that a 2-primary signature datum provably cannot reach (two-arena core B, Lean exit 0). So (7,7) is a NECESSARY PERMISSION, not a SUFFICIENT DERIVATION."
depends_on:
  - "tests/wave14/H19_seven_seven_branch.py"
  - "explorations/wave13/H37-count-nogo-2026-07-11.md"
  - "explorations/seven-axis-count-map-L0-L7-2026-07-11.md"
  - "explorations/sequential-goals-2026-07-09/SG1-signature-carrier-parity-77.md"
  - "explorations/big-swing-2026-07-03/BIG-SWING-signature-9-5-vs-7-7-UNDER-DETERMINED.md"
  - "explorations/big-swing-2026-07-06/VG-V3-j-commutant-conformal-native.md"
  - "canon/no-go-quaternionic-parity-generation-sector.md"
  - "canon/two-arena-rep-theory-core-RESULTS.md"
  - "canon/ghost-parity-krein-synthesis.md"
  - "papers/drafts/Transcript into the impossible.md"
---

# H19 -- THE (7,7) SIGNATURE BRANCH

**Discipline.** H37 (wave 13) proved the generation count is provably located-not-forced on the
built `(9,5) = M(64,H)` structure, and the seven-axis map put `L7 = the signature` as the **sole
live escape axis**: the grading/Z-eta leg is signature-independent, but the Kramers/mod-2 leg (the
`J^2` sign) LIFTS under `(7,7)` (`J^2 = +1`), making an odd rank-3 projector **admissible**. This
swing digs into what actually adopting `Y^14 = Cl(7,7) = M(128,R)` DELIVERS and COSTS, on the four
payoff questions, computed on the reps where possible.

The verdict most at risk is a fabricated **"(7,7) forces 3"** (extraordinary; would reopen the
count). The guard is maximal: no `24/8`, no `chi(K3)`, no fit to 3. A clean *"(7,7) makes odd
admissible but does NOT force 3, and here is the cost"* is a full result -- and it is the honest
one. Reproducible: `python tests/wave14/H19_seven_seven_branch.py` (**exit 0, 11/11 PASS**).

---

> [!CAUTION]
> **CORRECTION filed 2026-08-15 (CH-3) -- the chain this artifact attributes to
> the source. Attribution only: no verdict, computation or reproduction claim in
> this document changes.**
>
> **What this artifact wrote.** Q3b, Q4b and the Q4 summary below asserted the chain as
> `Spin(6,4)` then `Spin(3,2)` then `maximal compact SU(3) x SU(2) x U(1)`, sourced to
> `[00:43:47]-[00:45:00]`, and called it *"Weinstein's own SM chain"* and an *"SM embedding."*
> **Both halves of that are wrong**, and the second is wrong independently of the first.
>
> **1. The nested form is group-theoretically impossible.** `dim so(3,2) = 10 < 12 =
> dim(su(3)+su(2)+u(1))`, so no injective homomorphism exists; and every `so(p,q)` with
> `p+q = 5` is 10-dimensional, so no relabelling of the signature rescues it. Reading the
> `Spin(3,2)` as a commuting factor instead of a containing group fails too: the largest
> centraliser of **any** `Spin(3,2)` in `Spin(6,4)` is `10 < 12`, exhaustive over `so(5,C)`
> module structures on `C^10`.
>
> **2. The source's words.** He says *"s u three comma two"* **twice** at `[00:43:47]` --
> attached to a statement this repository has machine-verified twice (`SU(3)xSU(2)xU(1)` **is**
> the maximal compact of `SU(3,2)`) -- and *"spin three comma two"* **once**, inside the chain
> sentence at `[00:45:00]`. The same speaker turn contains the provable ASR garble *"the maximal
> compact subgroup of spin six comma spin four"*, which names no group at all: a spurious `spin`
> inserted into the same `X comma Y` frame, one clause earlier.
>
> **3. The decided reading, and its provenance.** `Spin(6,4) > SU(3,2) > S(U(3)xU(2))`, decided
> by `lab/active-research/joe-directed/source-chain/sca-right-chain-2026-08-15.md` (SC-A, 85/85)
> on the chain sentence, and by `la7-...-2026-08-15.md` §1.4 on the adjacent sentence. Both
> arrows are constructed: `SU(3,2) < Spin(6,4)` by realifying a Hermitian `(3,2)` form
> (`24 <= 45`), and `S(U(3)xU(2)) < SU(3,2)` as the maximal compact (`12 <= 24`).
>
> **4. It is not a subgroup tower at all, and this is the part that matters here.** The arrows
> are **structure-group reductions of one rank-10 vertical bundle**, not symmetry breakings.
> The source denies the GUT frame outright at `[00:38:09]`: *"There is no grand unification.
> It's just a normal bundle in your ambient space."* He names the operation at `[00:46:40]`:
> *"reduce maximal compact subgroups along the fibers."* So **"SM embedding" was the wrong
> phrase for this object even with the middle term corrected**, and every use of it below should
> be read as *"the reduction chain whose last node is the SM algebra."*
>
> **What this correction does and does not do to Q3/Q4.** Q3b and Q4b are load-bearing on the
> **fibre**, not on the chain: what is computed is that the trace-reversed DeWitt fibre is
> `(6,4)` for both base orientations. The corrected chain lives on that same fibre -- all three
> of its nodes are successive structure groups of it -- so **Q3b's and Q4b's conclusions
> survive, and Q4b's is if anything tighter.** No verdict in this artifact moves, and
> `tests/wave14/H19_seven_seven_branch.py` is unaffected in its assertions: the chain appears
> there only in docstrings and detail strings (lines 49, 60, 327, 362), never in a predicate, so
> its 11/11 stands -- but **those four strings still carry the impossible form and are owed the
> same repair by whoever owns that file** (out of scope for CH-3, which may touch only the
> attribution in this document).
>
> **The correction is not a point in GU's favour.** It removes an impossibility from *this
> repository's account of the source*; it supplies nothing. Reductions are not cheaper than
> breakings here -- the non-compact-to-compact reduction that arrow 2 needs is typed
> `REDUCTION_EXTERNAL` (`explorations/big-swing-2026-07-03/AUDIT-noncompact-compact-reduction-EXTERNAL.md`),
> i.e. the Weyl unitarian trick rather than a GU-forced selection. Q4's verdict `NOT-GU-NATIVE`
> is a **negative** result, so tightening its argument makes GU's under-determination *more*
> firmly established, not less.
>
> Reproduced independently in `tests/channel-swings/joe_directed_ch3_chain_repair.py`.

---

## Q1 -- Does (7,7) force the count to exactly 3, or just odd?

**VERDICT: ODD-ADMISSIBLE, NOT FORCED-3. (high confidence)**

Three legs, all computed:

- **Q1a (the rank is unrestricted).** On `(7,7)` (`J^2 = +1`) a genuine J-commuting orthogonal
  projector exists at **every** odd rank tested -- reachable set `{1, 3, 5, 7}` -- while on `(9,5)`
  (`J^2 = -1`) every one of those targets is Kramers-forced to the next even rank. So `(7,7)` lifts
  the parity obstruction for the **whole** odd ladder; it does **not** single out 3. The admissible
  set is `{1,2,3,4,5,6,7,...}`, not `{3}`.

- **Q1b (the decisive structural kill -- why "forces 3" is impossible, not merely unobserved).**
  The signature is a **2-primary datum**: `p-q mod 8` lives in `Z/8`. The generation count 3 lives
  in the **order-3 arena** of `pi_3^s = Z/24 = Z/8 (+) Z/3` (two-arena core, canon, Lean exit 0).
  Since `|Hom(Z/8, Z/3)| = gcd(8,3) = 1` (only the zero map), **no structural map carries a signature
  (2-primary) datum into the count (3-primary) arena.** By the two-arena "2-primary blindness"
  theorem, a mod-8 signature choice is *structurally incapable* of supplying the prime 3. This is the
  clean adversarial answer: any claim that `(7,7)` *derives* 3 would have to route a 2-primary object
  into the `Z/3` arena, which the coprimality theorem forbids.

- **Q1c (anti-fit control).** The natural GU carrier of a "3" -- the self-dual `SU(2)+` generation
  triplet (multiplicity 3, the `Lambda^2_+` of the 4-base, H1) -- is a **neutral Krein subspace
  `(+96, -96, 0)`** in `(9,5)` **and** `(7,7)` (beta_S pseudo-anti-Hermitian, residual `0.0`).
  A neutral form has net chiral index **0**. So even where the odd rank-3 projector is admissible,
  the triplet's "3" is **vectorlike** (three generations + three mirrors); `(7,7)` removes the
  *prohibition* but supplies **no chiral selector**. The 3 is not derived -- it is exactly as latent,
  and exactly as unselected, as on `(9,5)`.

**So `(7,7)` DERIVES three? No. It PERMITS odd (including 3), and it is provably unable to do more.**
This confirms SG1's qualifier and H37's positive control, and sharpens them with the 2-primary
coprimality reason *why* the permission can never become a derivation.

---

## Q2 -- Does the gravity conditional theorem transfer?

**VERDICT: TRANSFERS IN SHAPE, CHANGES IN REALITY CLASS. (medium-high confidence)**

The gravity arc (H1-H27) -- spin-lift `so(9,5) -> End_H(S)`, gauge group `Sp(32,32;H)`, Krein
`[P,S]=0`, `|II|^2` Stelle gravity, ghost-clear -- was built on the **quaternionic** `M(64,H)`. On
`(7,7) = M(128,R)` the Clifford reality is real. What survives:

- **Q2a (the Krein / `|II|^2` shape transfers -- signature-independent).** `beta_S` (product of
  spacelike gammas) is pseudo-anti-Hermitian for **every** `so(p,q)` generator on **both** signatures
  (residual `0.0` in each). The Krein form `K = eta_V (x) beta_S` therefore exists and is invariant on
  both; the triplet is neutral `(+96,-96)` on both (Q1c). Together with H37's finding that the grading
  leg `{G, O} = 0` is signature-independent, the entire *even-sector* machinery -- Krein positivity,
  the `|II|^2` distortion-square, the ghost-parity structure -- is **signature-independent** and
  carries over unchanged.

- **Q2b (the reality class flips -- the quaternionic gauge group does NOT transfer).** The antilinear
  intertwiner has `J^2 = -1` on `(9,5)` (quaternionic; commutant `= M(64,H)`; gauge group the
  quaternionic real form `Sp(32,32;H)`) and `J^2 = +1` on `(7,7)` (real; commutant `= M(128,R)`; a
  **different real form**, split/real-orthogonal type). So the specific object `Sp(32,32;H)` is
  `(9,5)`-**specific**: on `(7,7)` it is replaced by a real/split analog. Gravity's conditional-theorem
  *shape* (Krein, `|II|^2`, ghost-clear) survives; its quaternionic *gauge-group identity* does not.

**Adversarial: does the gravity transfer secretly assume the (9,5) quaternionic structure?** *Partly,
and exactly where you'd expect.* The Krein/`|II|^2`/grading legs are genuinely signature-independent
(computed). The one place the quaternionic structure is load-bearing is the **gauge group**
`Sp(32,32;H)` -- an `H`-linear object that is meaningless on `M(128,R)`. So the honest statement is:
the gravity *positivity theorem* transfers; the *gauge-group name* is `(9,5)`-specific and must be
restated for the real class. This is a change, not a break.

---

## Q3 -- What does (7,7) cost?

**VERDICT: LOW COST -- and the genuine cost is REDUCED PREDICTIVITY, not a broken sector. (med-high)**

- **Q3a (anomaly-freedom: not broken).** `omega = e_1...e_14` has `omega^2 = +I` in **both** signatures
  (both `q` odd), so the chiral splitting `S = S^+ (+) S^-` exists in either; and the `D=14` anomaly is
  order `Tr F^8` (an even symmetric Casimir), which is reality-class-**blind** (BIG-SWING angle 1).
  Anomaly-free content is admissible in both classes. **No cost.**

- **Q3b (SM reduction chain: survives on the common fiber).** *(Chain attribution CORRECTED
  2026-08-15 -- see the CAUTION block above. This bullet originally wrote the middle node as
  `Spin(3,2)` and called the object an "SM embedding"; both were wrong.)* The source's chain is
  `Spin(6,4) > SU(3,2) > S(U(3)xU(2))` (transcript `[00:43:47]`: "the Standard Model answers the
  question, what is the maximal compact subgroup of `SU(3,2)`", said twice; Pati-Salam
  `= Spin(6) x Spin(4) =` maximal compact of `Spin(6,4)`), and its arrows are **structure-group
  reductions of the rank-10 vertical bundle**, not a subgroup tower -- *"There is no grand
  unification. It's just a normal bundle in your ambient space"* (`[00:38:09]`). The `(6,4)` is the
  **trace-reversed DeWitt fiber**, and it is `(6,4)` for **both** base orientations (mostly-plus AND
  mostly-minus, computed) -- the fiber form is quadratic in `g`, hence `g -> -g` invariant. So the
  entire Pati-Salam reduction rides a fiber **common** to `(9,5)` and `(7,7)`. **No cost.**
  **Did this bullet's conclusion USE the nesting? No.** The computed content is the fiber
  signature; the chain was cited as a passenger. The verdict is a *differential* one -- `(7,7)`
  costs no more here than `(9,5)` -- and it never asserted that GU possesses an SM embedding.
  Under the corrected reading it asserts even less: what rides the fiber is a chain of reductions
  whose second arrow is typed `REDUCTION_EXTERNAL`. (Notably, the reduction chain *requires*
  indefinite internal structure -- the real `(6,4)` fiber and its Hermitian halving `(3,2)`,
  **two** signatures, not the three `(6,4),(3,2),(3,2)` this bullet used to list -- which is
  Weinstein's point that the seventies "wasted ... work because we wanted to avoid indefinite
  signature"; and both total signatures deliver the same indefinite fiber.)

- **Q3c (QM unitarity: same cost as (9,5)).** Both `(9,5)` (`q=5`) and `(7,7)` (`q=7`) have `q > 0`, so
  **both** are Krein spaces, neither is a Hilbert space, and both require the Turok-Bateman ghost-parity
  Born rule for positivity. The triplet is neutral `(+96,-96)` in both. **No differential cost** -- the
  unitarity bill was already paid at `(9,5)`.

- **Q3d (the REAL cost: predictivity narrows).** `(7,7)` *removes* the even-parity constraint without
  *adding* one. On `(9,5)` the admissible generation index is Kramers-restricted to even `{0,2,4,6,...}`;
  on `(7,7)` the full ladder `{1,2,3,4,5,6,7,...}` is admissible. So `(7,7)` is **strictly less
  constraining** -- odd `1,3,5,7` are *all* admissible, not just 3. Adopting `(7,7)` buys the
  admissibility of 3 at the price of also admitting 1, 5, 7: the under-determination **widens**.

**Net cost: essentially none on anomaly / SM / unitarity (all reality-blind or ride the common fiber);
the honest cost is that `(7,7)` is a weaker constraint, not a stronger one.**

---

## Q4 -- Is (7,7) GU-native?

**VERDICT: NOT GU-NATIVE -- it stays an under-determined choice. (high confidence)**

- **Q4a (only the base sign moves the class).** Closed form `p-q = d + d^2/2` with `d = #space - #time`
  in the base: `d = +2` (mostly-plus `(3,1)`) `-> p-q = 4 -> (9,5)/H`; `d = -2` (mostly-minus `(1,3)`)
  `-> p-q = 0 -> (7,7)/R`. The whole H/R decision rests on `sign(d)`.

- **Q4b (no GU-native selector for `sign(d)`).** *(Chain attribution CORRECTED 2026-08-15 -- see the
  CAUTION block above.)* The `(6,4)` fiber -- the only structure common to the two totals -- is
  `g -> -g` invariant, so it carries no `sign(d)` and cannot select. Weinstein's
  `Spin(6,4) > SU(3,2) > S(U(3)xU(2))` chain rides that invariant fiber, so it too is **neutral** on
  the total signature. Only the base pullback (linear in `g`) carries the sign, and the observerse
  (the space of metrics) has no preferred timelike-norm sign. The three candidate levers named in the
  swing all fail to select:
  - *the H19 term linear in `g` carrying the timelike-norm sign* -- the only `sign(d)`-carrier is the
    base pullback, and no GU-native term fixing its sign is exhibited (BIG-SWING angle 4);
  - *the trace-reversed `(6,4)` fiber (VG-V3)* -- `g -> -g` invariant, common to both, selects neither;
  - *Weinstein's `so(6,4) > su(3,2) > s(u(3)+u(2))` chain* -- the internal/fiber chain, common to both
    totals. The transcript's three-family claim rides a **VEV** mechanism (`[00:46:02]`: "decreased VEV
    in the total space taking a Dirac equation into two Weyl equations"), which is a chiral-selection
    story, not a signature selector.

  **Did this bullet's neutrality argument USE the nesting? No -- and the corrected reading makes it
  STRONGER, which is a fact about the argument and not a point for GU.** The neutrality claim needs
  only that the chain's nodes are structure groups of a `g -> -g` invariant fiber. Under the old
  nested reading that was an assertion about a chain that could not exist. Under the decided reading
  it is exact: all three nodes are successive structure groups of the *same* rank-10 `(6,4)` bundle
  (`so(6,4)` is its structure algebra, `su(3,2)` is the stabiliser of a compatible complex structure
  on it, `s(u(3)+u(2))` is the maximal compact of that), so their common neutrality is a theorem about
  one bundle rather than a coincidence across three groups. **The conclusion this tightens is
  `NOT-GU-NATIVE`** -- a negative verdict -- so the tightening increases the confidence that GU does
  not select its own signature.

**So the primary source's own "use indefinite signature" argument is about the INTERNAL structure of
the fiber being indefinite -- the real `(6,4)` form and its Hermitian halving `(3,2)`, both carried by
the same rank-10 normal bundle, common to `(9,5)` and `(7,7)`.** It does **not** supply a
total-signature selector. `(7,7)` stays an under-determined declared choice, exactly as BIG-SWING
concluded.

---

## The re-rank: what the seven-axis map should now say about L7

The seven-axis map called `L7 = the signature` **"the one live escape."** This swing sharpens that to
its honest form:

> **L7 lifts a 2-primary VETO; it does not, and provably cannot, supply the 3-primary count.**

The Kramers/mod-2 leg that `(7,7)` lifts is a **2-primary** obstruction (a parity, `Z/2`). Removing it
is real and necessary -- on `(9,5)` odd is *forbidden*; on `(7,7)` odd is *permitted*. But the
generation 3 lives in the **orthogonal `Z/3` arena**, and by 2-primary blindness (`|Hom(Z/8,Z/3)| = 1`,
Lean-verified) **no signature datum can reach it**. So `L7` is a **necessary permission, not a
sufficient derivation**. The count problem does not collapse onto the signature; it **factors**:

- **the 2-primary factor (L7 / the signature):** does GU permit an odd index? On `(7,7)`, yes. This is
  a mod-8 choice, under-determined, cheap, and *not* where 3 comes from.
- **the 3-primary factor (the `Z/3` arena):** does anything *supply* the prime 3? This is the
  chiral-selection / ghost-parity dynamics / source-action question -- **orthogonal to the signature**,
  and untouched by adopting `(7,7)`.

So `L7` is not the last hinge before 3; it is the hinge that removes the *veto*. Even after winning it
(adopting `(7,7)`), the entire burden of *deriving* 3 remains in the orthogonal `Z/3` arena.

### RE-RANK signal

**`(7,7)` is a LIVE-BUT-NON-DERIVING option -- not the recommended signature, not a dead end.**

- It is **not** "forces 3, cheap" (Q1b: structurally impossible for a 2-primary datum).
- It is **not** a dead end (Q2/Q3: it transfers gravity's shape and costs almost nothing; it genuinely
  dissolves the `(9,5)` even-parity wall).
- It **is** a cheap, non-GU-native choice that *permits* odd without *supplying* 3 and *widens*
  under-determination.

**Recommendation:** do **not** re-rank `(7,7)` up to "recommended signature." Adopting it would trade a
false constraint (the `(9,5)` even-parity wall, which forbids the very count we seek) for *more*
freedom, not *less*. The high-leverage next move is **not** the signature at all.

### The single next object

**The `Z/3`-arena chiral selector -- a ghost-parity-preserving dynamics (the unbuilt source action)
whose ghost parity selects the physical half of each hyperbolic (generation, mirror) pair** -- i.e.
the condition `[P_ghost, S] = 0` of `canon/ghost-parity-krein-synthesis.md`, computed on GU's actual
matter Krein space. This is the object that lives in the arena where 3 can actually originate, and it
is **signature-independent** (the triplet is neutral `(+96,-96)` in both `(9,5)` and `(7,7)`), so it
can and should be attacked **without** first settling the signature. If a secondary signature lever is
wanted, it is a GU-native selector for `sign(d)` (mostly-plus vs mostly-minus) -- but Q4 says the
honest prior is that none exists.

---

## Honest caveats (computed vs argued vs cited)

1. **Freshly computed (exact on the 128 / 1792-dim reps, residuals `0.0`):** the `(7,7)` odd-rank
   `{1,3,5,7}` J-projectors and the `(9,5)` even-forcing; `beta_S` pseudo-anti-Hermiticity on both
   signatures; the triplet Krein signature `(+96,-96)` on both; `omega^2 = +I` on both; the
   trace-reversed DeWitt fiber `(6,4)` for both base orientations; the `J^2` reality flip.
2. **Arithmetic certificate (exact integer):** `|Hom(Z/8,Z/3)| = gcd(8,3) = 1` and `Z/24 = Z/8 (+) Z/3`.
   The *inference* "therefore a signature datum cannot supply 3" rests on the two-arena core's
   2-primary blindness theorem (canon, Lean exit 0), **cited not re-proved** here.
3. **Argued / cited (not independently re-closed):** that `Sp(32,32;H)` is replaced by a real/split
   form on `M(128,R)` is the standard real-Clifford consequence of the `J^2` flip (the flip is
   computed; the group name is not a constructed group). The full spin-lift / `|II|^2` Stelle chain was
   **not** rebuilt on `(7,7)`; the transfer claim rests on the computed `beta_S`/`omega`/grading
   signature-independence plus H37's grading-leg result. The `D=14` `Tr F^8` reality-blindness is
   BIG-SWING angle 1, cited.
4. **No p-hacking.** No `3 / 24 / (24-8)` is imported or fit anywhere. The only place an odd count
   appears is the admissibility ladder `{1,3,5,7}` on `(7,7)` (a signature change), and the triplet's
   3 is shown to be index-**0** (unselected) in both signatures. The prime 3 is never derived; it is
   shown to be structurally *out of reach* of the signature axis.

---

*Filed 2026-07-11. Wave 14, the (7,7) signature-branch swing. Reproducible:
`python tests/wave14/H19_seven_seven_branch.py` (exit 0, 11/11 PASS). Exploration-grade; not promoted
to canon. Adversarially graded: no "forces 3" manufactured (2-primary blindness makes it impossible),
gravity transfer honestly split into signature-independent shape vs `(9,5)`-specific gauge group, no
target imported. Headline: adopting `(7,7)` makes odd ADMISSIBLE but does NOT DERIVE three; it is a
live-but-non-deriving, cheap, non-GU-native choice. `L7` lifts a 2-primary veto; the 3 lives in the
orthogonal `Z/3` arena -- which is the single next object, and it is signature-independent.*
