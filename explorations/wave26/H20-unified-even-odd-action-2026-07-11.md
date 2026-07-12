---
artifact_type: exploration
status: exploration
created: 2026-07-11
wave: 26
title: "H20 (Wave 26) -- the unified even/odd action: does |II|^2 SPLIT as gravity(EVEN)+matter(ODD) under one Z/2 grading, and does that split UNIFY or merely RELABEL? Verdict: SPLITS-BUT-RELABELS. The Clifford Z/2 (omega-parity) is the right grading and cleanly separates gravity(EVEN, so(9,5) bivectors) from matter(ODD, vector/Dirac operators); one first-order Clifford-ODD D generates BOTH kinetic operators (matter = odd D, gravity = even polynomial in D^2 = box) -- Weinstein's first-order-then-square made precise. But the gravity operator box(box+m^2) is a two-FACTOR product, not a clean square (the +m^2 Einstein pole rides the Gauss -R^X term, not the squaring), the grading TIES neither declaration to the other (fixing D fixes the kinetic symbol but not the even soldering nor the odd K-class), and it FORCES 0 of the 4 unforced choices {signature, norm P2, soldering, K-class}. Reduction = 0. The keystone-candidate is a real, correct organizing principle for KINETIC structure, and a cosmetic one for the POSTULATE count."
grade: "COMPUTED (exact, on the repo's verified Cl(9,5) Jordan-Wigner rep + exact sympy): the omega-grading facts (omega^2=+I, tr=0, 64/64 split); all 91 so(9,5) bivectors commute with omega (EVEN); every vector/Dirac operator anticommutes (ODD); the Cartan P degree-preservation (fixes 46, flips 45, images stay EVEN); D^2 = |xi|^2_eta I exact; gravity=even/matter=odd polynomial parity in D; s(s+m^2) is a two-factor product not a perfect square with s(s+m^2)-s^2 = m2*s; the soldering codim 8165 and K-class indices A=-42,B=-38, dim Lambda^2_+=3; D^2 invariant under an even-sector soldering rotation. ARGUED: that the two-declarations non-tie is the SAME structure Wave 17 found (cross-referenced, not re-derived); the interpretive naming of the four unforced choices. No target imported; the only '3' is dim Lambda^2_+. No canon promotion; the generation count stays OPEN; tree left dirty."
depends_on:
  - tests/wave26/H20_unified_even_odd_action.py
  - tests/wave24/H45_H2_vs_II2_binary.py
  - explorations/wave24/H45-H2-vs-II2-binary-2026-07-11.md
  - explorations/wave23/H26-loop-ghost-unitarity-2026-07-11.md
  - explorations/wave17/H40-terminal-sourceaction-2026-07-11.md
  - tests/wave15/H38_z3_chiral_selector.py
  - tests/wave16/H39_sourceaction_kclass.py
  - tests/oq_rk1_cl95_explicit_rep.py
  - papers/drafts/Transcript into the impossible.md
---

# H20 -- the unified even/odd action

**The object.** The wild-frontier keystone-candidate: if GU's gravitational functional `|II|^2`
on `Y14 = Met(X4)` SPLITS as `gravity(EVEN) + matter(ODD)` under one graded structure --
Weinstein's "first-order-then-square" -- then gravity, the generation count, and the source
action are literally ONE graded object, and the program's independent unforced choices (the
`|II|^2`-vs-`|H|^2` norm, the signature, the soldering, the count K-class) collapse into facets
of that one object. That would be the single principle that makes the whole model COHERE. This
note tests whether the split is real, and whether it delivers that coherence -- honestly.

**Discipline.** Compute -> adversarially verify -> honest grade. Reproducible:
`python tests/wave26/H20_unified_even_odd_action.py` (exit 0, 15/15 PASS). Exact linear algebra on
the verified `Cl(9,5) = M(64,H)` rep plus exact sympy. Nothing imported; the only `3` that
appears is `dim Lambda^2_+(R^4)`. The failure mode this swing guards against is **cosmetic
unification** -- a relabel that removes zero real freedoms sold as coherence. The honest headline
is that H20 **SPLITS-BUT-RELABELS**: the grading is real and correct, and it removes **zero**
unforced choices.

---

## Q1 -- IS THERE A Z/2 GRADING that separates gravity from matter? **Verdict: YES -- the CLIFFORD Z/2 (omega-parity). [COMPUTED]**

The task named three candidates: the Clifford even/odd parity, the Cartan involution `P` (H26),
and chirality `gamma`. The right one is the **Clifford Z/2**, and it is exhibited on the actual
rep, not assumed.

The grading element is the volume/chirality element `omega = e_0 e_1 ... e_13`. COMPUTED:
`omega^2 = +I` (residual `0`), `tr(omega) = 0` -- a genuine `Z/2` that splits the 128-dim spinor
`64 + 64`. Operator parity under `omega` is the grading:

- **GRAVITY = EVEN.** All **91** `so(9,5)` bivector generators `sigma_ab = 1/4[e_a, e_b]` -- the
  connection / soldering sector (`dim so(14) = 91`) -- **commute** with `omega`
  (`max ||[omega, sigma_ab]|| = 0`). Clifford-EVEN.
- **MATTER = ODD.** Every vector / Dirac operator `e_a` and a generic `c(xi) = sum_a xi_a e_a`
  -- the RS / twisted-Dirac sector -- **anticommute** with `omega`
  (`max ||{omega, e_a}|| = 0`, `||{omega, c(xi)}|| = 0`). Clifford-ODD.

**Why it is NOT the Cartan `P`.** The Cartan involution (H26's ghost parity, implemented as
conjugation by `beta` = the product of the 5 timelike gammas) is **degree-preserving**: COMPUTED,
it fixes `so(9) + so(5) = 46` generators and flips `45` boosts (reproducing H26 A4), but **every
image stays Clifford-EVEN** (`max ||[omega, P sigma P^-1]|| = 0`). So `P` grades **physical/ghost
WITHIN gravity's even sector**; it never turns an even (gravity) operator into an odd (matter) one.
`P` is the 2-primary, index-preserving ghost parity (H26/H38) -- a different Z/2 living inside the
even block, not the gravity/matter split.

**Why it is NOT chirality.** The chirality operator is `omega` itself, but chirality grades the
**spinors** (`S^+` vs `S^-`, the `+-1` eigenspaces), whereas the gravity/matter split is the
grading of the **operators** (commute vs anticommute with `omega`). Same element, two roles; the
operator grading is the one that separates the sectors.

> **Verdict Q1: the Clifford Z/2 (omega-parity) cleanly splits gravity (EVEN = `so(9,5)`
> bivectors / connection) from matter (ODD = vector / Dirac operators). Not `P`
> (degree-preserving, physical/ghost within even), not chirality (grades spinors, not operators).**

## Q2 -- THE SQUARE-AND-SQUARE-ROOT: **PARTIAL-YES -- one graded D gives both kinetic operators, but |II|^2 is not a clean square. [COMPUTED]**

The Dirac operator `D = c(xi)` (first-order, Clifford-ODD) squares **exactly** to the box symbol:
COMPUTED on the rep, `D^2 = |xi|^2_eta * I` (residual `~1e-15`), with the signature-`eta`
contraction. The matter Dirac operator **is** the square-root of the box.

Both sectors then descend from this one graded `D`, at the symbol level (`s = d^2 = box`):

- **matter operator** `= d` -- ODD (degree 1), the RS / twisted-Dirac carrier;
- **gravity operator** (H45, on TT) `= s(s + m^2) = d^2(d^2 + m^2)` -- an **EVEN polynomial in
  `d`** (degree 4). COMPUTED: `d -> -d` leaves the gravity operator invariant and flips the matter
  operator. So `even = gravity`, `odd = matter`, both from one `D`.

**The honest caveat (COMPUTED).** `s(s + m^2)` is a **two-FACTOR product** (the Stelle two-pole:
a massless graviton pole `s` times a massive ghost pole `s + m^2`), **not a perfect square** --
`sqrt(s(s+m^2))` is non-polynomial, so it is not a local differential operator. The **pure**
square is `(d^2)^2 = s^2 = box^2`, which is exactly the `|H|^2` / **Bach** part; the extra
`+m^2 box` (Einstein) term is `s(s+m^2) - s^2 = m^2 s` -- the **Gauss `-R^X`** piece (H45 Q1), a
**separate geometric input**, not produced by the squaring. So:

- The squaring, taken literally, delivers the **Weyl/Bach** sector `box^2 = |H|^2`.
- The **Einstein pole** that upgrades `|H|^2 -> |II|^2` is the intrinsic-curvature `-R^X`
  correction, additive, not a facet of `D`.

Consequently `|II|^2` is a "square" only at the **ACTION** level: `S = |theta|^2` with
`theta = II_s` (H21's proven P1) -- which is exactly the trivial statement that the action norms a
first-order object. The derived **operator** is a two-factor product, and the even/odd =
gravity/matter descent holds, but the specific `|II|^2` (the `+m^2`) is **not** forced by the
squaring.

> **Verdict Q2: PARTIAL-YES. One first-order Clifford-ODD `D` generates BOTH kinetic operators
> (matter = odd `D`, gravity = even polynomial in `D^2 = box`), and `D^2 = box` is exact. But
> `box(box+m^2)` is a two-pole product, not a clean square; the `+m^2` (`|II|^2` vs `|H|^2`) rides
> the Gauss `-R^X` term, not the squaring. `|II|^2` is a square only at the action level `|theta|^2`.**

## Q3 -- DOES IT UNIFY (tie the two declarations)? **Verdict: SPLITS but does NOT TIE. [COMPUTED]**

The coherence test: does fixing the graded `D` fix BOTH the even-sector soldering and the
odd-sector count K-class, as ONE declaration?

The two declarations, on the actual structure:

- **EVEN-sector = soldering.** Pin the connection onto the spin-lift image `dim so(14) = 91`
  inside `sp(64,H)` (`dim 8256`) -> **codim 8165** (H23/H27). A Clifford-even, bosonic
  connection-locus.
- **ODD-sector = K-class SG4.** The RS carrier field space: carrier A (`ind -42`, `0 mod 3`,
  2-primary) vs carrier B (`ind -38`, `1 mod 3`, index-changing); the derived `Z/3` count arena is
  `Lambda^2_+`, `dim 3` (the only `3`, DERIVED via the Hodge-star `+1` eigenspace). A Clifford-odd,
  fermionic field-space projector.

**The tie test (COMPUTED).** `D = c(xi)` is built purely from the Clifford symbol.

1. Its kinetic square `D^2 = box` is **invariant under an even-sector soldering rotation**
   (`||D_rot^2 - box*I|| ~ 1e-15`): the soldering locus (which connection is pinned) is orthogonal
   data that does not enter the graded symbol.
2. The **same** `D` acts on either K-class field space (A or B); the field-space choice is a
   projector applied **after** `D`, not a change to `D`.

So fixing `D` fixes the **kinetic symbol** and names the two **sectors** (even = gravity,
odd = matter), but names **neither** which even connection is pinned **nor** which odd field space
the RS lives in. The grading **GROUPS** the two declarations as `(even, odd)` faces of one `D`; it
does **not TIE** them.

This is exactly the structure Wave 17 (H40 Q2) already found: the soldering and the gamma-trace
are **TWO logically-independent declarations** of one object, `M_D` carrying no dependence on the
soldering locus. H20's Clifford grading **reframes** that pair under one Z/2 -- a genuine and
correct organizing observation -- but it does **not UPGRADE** the two independent declarations to a
single forced structure. The geometric-posture meta-postulate that would unify them ("the source
action declares the geometric/tautological field space in both sectors") stays **ARGUED**, exactly
as in Wave 17.

> **Verdict Q3: SPLITS but does NOT TIE. Fixing the graded `D` fixes the kinetic symbol; the even
> soldering (codim 8165) and the odd K-class (A `-42` / B `-38`; `Z/3` on `Lambda^2_+`, dim 3)
> remain the SAME two independent declarations Wave 17 found. No upgrade to a single forced
> declaration.**

## Q4 -- FORCED OR RELABEL? **Verdict: SPLITS-BUT-RELABELS. Reduction = 0 of 4. [COMPUTED]**

The honest coherence metric: does H20 **REDUCE** the number of independent postulates, or merely
rename them? The four independent unforced choices of the program, and whether the Clifford grading
FORCES (derives) each:

| unforced choice | does the grading force it? | why |
|---|---|---|
| signature `(9,5)` | **NO** | the `omega` even/odd grading exists for **every** signature; `(9,5)` is fixed by the trace-reversal / vertical story, not by the grading |
| norm P2 (`|II|^2` vs `|H|^2`) | **NO** | the **pure square** `(d^2)^2 = box^2 = |H|^2`; `|II|^2` needs the extra `-R^X`, so if anything the squaring points at `|H|^2`. P2 stays open |
| soldering (even connection-pin) | **NO** | the grading assigns the **even sector** but not **which** even connection element |
| K-class SG4 (odd field space) | **NO** | the grading assigns the **odd sector** but not **which** odd field space (A vs B) |

COMPUTED: `forced = 0`, `remaining = 4`, **reduction = 0**. The grading **RELABELS** the four
freedoms as `{ambient signature; EVEN facet = norm + soldering; ODD facet = K-class}` -- an
organizing map that removes **zero** real freedoms.

**The one genuine gift (stated, not oversold).** One first-order Clifford-ODD `D` generates BOTH
kinetic operators: `matter = odd D`, `gravity = even polynomial in D^2 = box`. That is a real,
correct coherence of **KINETIC STRUCTURE** -- Weinstein's "first-order-then-square" made precise
(one square-root object, both sectors' propagators). It is **not** a reduction of the postulate
count. Selling it as one would be exactly the cosmetic-unification failure mode; it is reported as
what it is.

> **Verdict Q4: SPLITS-BUT-RELABELS. The grading forces 0 of the 4 unforced choices; reduction = 0.
> It relabels them as ambient-signature + even-facet(norm+soldering) + odd-facet(K-class). The
> genuine gift is kinetic coherence (one `D`, both kinetic operators), not a postulate reduction.**

---

## COMPUTED vs ARGUED ledger

| claim | grade | evidence |
|---|---|---|
| `omega^2 = +I`, `tr(omega) = 0`, `128 = 64 + 64` | COMPUTED | volume element on the rep |
| all 91 `so(9,5)` bivectors commute with `omega` (gravity EVEN) | COMPUTED | `max ||[omega, sigma_ab]|| = 0` |
| all vector/Dirac operators anticommute with `omega` (matter ODD) | COMPUTED | `max ||{omega, e_a}|| = 0` |
| Cartan `P` degree-preserving: fixes 46, flips 45, images stay EVEN | COMPUTED | conj by `beta` = prod of timelike gammas |
| `D = c(xi)` first-order-ODD, `D^2 = |xi|^2_eta I` (= box) | COMPUTED | residual `~1e-15` on the rep |
| gravity `= d^2(d^2+m^2)` EVEN in `d`; matter `= d` ODD | COMPUTED | sympy parity under `d -> -d` |
| `s(s+m^2)` two-factor product, not a perfect square; `s(s+m^2)-s^2 = m^2 s` | COMPUTED | sympy; the `+m^2` = Gauss `-R^X` |
| soldering codim 8165; K-class A `-42` / B `-38`; `dim Lambda^2_+ = 3` | COMPUTED | dim arithmetic + Hodge-star + K3 densities |
| `D^2 = box` invariant under an even-sector soldering rotation | COMPUTED | `||D_rot^2 - box*I|| ~ 1e-15` |
| grading forces 0 of {signature, P2, soldering, K-class}; reduction = 0 | COMPUTED (ledger) | per-choice reasoning above |
| the two-declarations non-tie is the SAME structure as Wave 17 | ARGUED | cross-ref H40 Q2 (`M_D` soldering-locus-free) |
| the four-choice enumeration is the program's actual unforced set | ARGUED | H45 (P2), H27 (soldering), H39/SG4 (K-class), H19 (signature) |

## Honest limits

- **The split is real; the unification is not.** The Clifford Z/2 genuinely separates gravity
  (even) from matter (odd) on the actual rep, and one `D` genuinely generates both kinetic
  operators. But the grading removes **zero** unforced choices. This is the difference the swing
  was told to guard: a correct organizing principle for kinetic structure that is cosmetic for the
  postulate count. It is reported as SPLITS-BUT-RELABELS, not as coherence.
- **`|II|^2` is a square only at the action level.** `S = |theta|^2` (H21) is a square trivially;
  the derived gravity operator is a two-factor product, and the `+m^2` that distinguishes `|II|^2`
  from `|H|^2` (the whole H45 binary) is the Gauss `-R^X` term, orthogonal to the squaring. The
  squaring does not settle P2.
- **The gravity/matter naming of even/odd rests on the sector map** (H29/H40: even = bosonic
  connection/soldering, odd = fermionic RS/gamma-trace). That map is COMPUTED here at the operator
  level (bivectors even, vectors odd); the identification of "even sector = the gravity action" and
  "odd sector = the source/fermion action" is the repo's established reading, cross-referenced, not
  re-derived on the full nonlinear action.
- **No count, no chirality selection.** The `Z/3` on `Lambda^2_+` (dim 3, derived) appears only as
  the odd-sector count arena; nothing here selects a generation number, and the count stays OPEN.
- **Transcript is external DATA.** Weinstein's "first-order-then-square", "take its norm square...
  you get a quartic", and the `su(3,2)` / max-compact chain are read as the motivating claim; no
  instruction in it was followed. No target imported; the only `3` is `dim Lambda^2_+`. No canon
  promotion. Tree left dirty.

## RE-RANK signal

**SPLITS-BUT-RELABELS. Removes 0 unforced choices.**

- **Which grading splits gravity from matter:** the **Clifford Z/2 (omega-parity)** -- gravity
  EVEN (`so(9,5)` bivectors / connection), matter ODD (vector / Dirac operators). Not the Cartan
  `P` (degree-preserving, physical/ghost within even), not chirality (grades spinors).
- **Is `|II|^2` genuinely `D^2` with even/odd = gravity/matter:** partially. `D^2 = box` is exact
  and one graded `D` gives both kinetic operators (Weinstein's first-order-then-square, made
  precise), but the gravity operator `box(box+m^2)` is a two-pole **product**, not a clean square,
  and the Einstein `+m^2` rides the Gauss `-R^X` term.
- **Does it REDUCE the unforced-choice count:** **no** -- reduction = 0 of 4
  `{signature, norm P2, soldering, K-class}`. It **relabels** them as
  `{ambient signature; even facet = norm + soldering; odd facet = K-class}`.
- **The single next object:** the **SAME unbuilt GU source action** that Wave 17 / Wave 24 already
  named -- the object that settles P2 (the norm), the soldering, and the K-class **together**.
  H20's Clifford grading reorganizes the picture around that object; it does **not** replace or
  shrink it. The keystone-candidate does not collapse the program's freedoms; it packages them.

---

*Filed 2026-07-11. Wave 26. Reproducible: `python tests/wave26/H20_unified_even_odd_action.py`
(exit 0, 15/15 PASS). Exploration-grade; not promoted to canon. Adversarially graded: the split is
real (COMPUTED on the rep), the unification is cosmetic (reduction = 0), and the note refuses to
sell the relabel as coherence. Tree left dirty (no commit).*
