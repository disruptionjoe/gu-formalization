---
title: "H54 branch 4 -- reverse-engineer the guardian from GU's cure term: does the forced g=1 ker-Gamma cure INSTANTIATE a known consistent gravitino coupling (de Wit-Freedman / Deser-Zumino / Porrati-Rahman / Vasiliev)?"
date: 2026-07-11
status: exploration
doc_type: exploration
wave: 40
verdict: speculation   # blind branch; NO claim promoted, NO canon/ledger movement
method: "5-persona team run INLINE (supergravity-construction theorist / higher-spin-Vasiliev specialist / Porrati-Rahman cure expert / EFT-matching specialist / philosopher of science). Templates read as DATA. COMPUTED (on the verified Cl(9,5)=M(64,H) rep) vs ARGUED tagged per claim. Blind to sibling branches."
test: tests/wave40/H54b4_cure_guardian_reverse.py   # deterministic, exit 0, all PASS
reads:
  - explorations/wave34/source-action-landscape-scan-2026-07-11.md   # Porrati-Rahman cure template; guardian requirement; Rahman cutoff
  - explorations/wave35/source-action-carve-2026-07-11.md             # the forced g=1 ker-Gamma cure
  - explorations/wave17/H40-terminal-sourceaction-2026-07-11.md       # the cure requirement
  - explorations/firewall-and-two-geometries/source-action-necessary-conditions-and-causality-2026-06-27.md
  - explorations/analytic-index-fredholm/oq-rs3-gu-vasiliev-comparison-2026-06-23.md
---

# H54 branch 4 -- reverse-engineer the guardian from the cure term

The sibling branches (blind to me) ask "does GU have a guardian?". This branch inverts it: **take GU's
SPECIFIC forced cure -- the g=1, full ker-Gamma projection `O = Pi M_D Pi` (Wave 35) -- and ask which known
consistent gravitino coupling its OPERATOR STRUCTURE instantiates, and what guardian would consistency-
complete exactly that structure.** The advantage of the reverse direction: the cure is a concrete operator on
the verified `Cl(9,5) = M(64,H)` rep, so the comparison to the de Wit-Freedman / Deser-Zumino / Porrati-Rahman
/ Vasiliev templates can be made on computed operator signatures, not just prose.

Everything numeric here is reproduced by `tests/wave40/H54b4_cure_guardian_reverse.py` (deterministic, exit 0,
all PASS). Template bits are ARGUED (read from the repo's own literature descriptions in Wave 34 and the
Vasiliev-comparison file); GU-cure's bits are COMPUTED on the rep. Nothing is promoted; no ledger movement.

## The method: five structural axes, one signature per template

I reduced "which consistent coupling is this?" to five yes/no structural axes and computed GU's cure's bits
against them, then scored the four templates.

| Axis | Question | GU cure (COMPUTED) |
|---|---|---|
| **A** field content | does the cure produce a STANDALONE / decoupled massive spin-3/2 (`[Pi, O]=0`)? | **+1 YES** |
| **B** non-minimal vertex | is the correction an `F(background)`-analytic non-minimal vertex (vanishes at `F=0`), not a kinematic projector? | **-1 NO** |
| **C** guardian | is `ker Gamma` realized COHOMOLOGICALLY via a NON-equivariant local gauge symmetry, not a hard equivariant projector? | **-1 NO** |
| **D** finite content | consistent with finite field content (no infinite HS/Regge tower)? | **+1 YES** |
| **E** AdS | does it REQUIRE an AdS / `Lambda<0` background? | **-1 NO** |

**GU-cure signature `(A,B,C,D,E) = (+1, -1, -1, +1, -1)`.** Template signatures (ARGUED):

| Template | A | B | C | D | E | match to GU cure |
|---|---|---|---|---|---|---|
| Porrati-Rahman (non-minimal EFT) | -1 | +1 | -1 | +1 | -1 | **3/5** (differs on A, B) |
| **de Wit-Freedman gravitino** | **+1** | **-1** | **+1** | **+1** | **-1** | **4/5** (differs on **C only**) |
| **Deser-Zumino massive gravitino** | **+1** | **-1** | **+1** | **+1** | **-1** | **4/5** (differs on **C only**) |
| Vasiliev higher-spin vertex | -1 | -1 | +1 | -1 | +1 | **1/5** (excluded) |

The headline falls straight out of the table: **GU's forced cure matches the de Wit-Freedman / Deser-Zumino
gravitino on 4 of 5 axes, and the ONE axis it fails is axis C -- the guardian.** GU's cure is, structurally,
**"a gravitino minus its guardian."**

## The three computed operator facts that set the bits

1. **AXIS A (+1) -- the cure DECOUPLES the RS sector.** The bare minimal symbol has `||[Pi, M_D]|| = 58.72`
   (RS coupled to the spin-1/2 sector). The g=1 cure `O = Pi M_D Pi` satisfies `||[Pi, O]|| = 0` exactly
   (COMPUTED). So the cure converts a coupled RS into a **standalone gamma-traceless massive spin-3/2** -- the
   FIELD CONTENT of a de Wit-Freedman gravitino, NOT the coupled EFT field of Porrati-Rahman. This is the
   crux, and it is the reverse-engineering payoff: *the cure's own algebra tells you it is building a
   gravitino, not a Porrati-Rahman vertex.*

2. **AXIS B (-1) -- the cure is KINEMATIC, not an F-vertex.** The correction `Delta = O - M_D` is EXACTLY a
   pure constraint-projector object, `Delta = -(Pi M_D Q + Q M_D Pi + Q M_D Q)` with `Q = I - Pi` (COMPUTED,
   residual `1e-13`). It carries no background field strength `F` and does not vanish at `F=0` -- it is
   kinematic (built from the Clifford frame). Porrati-Rahman's cure is the opposite: `A^{munurho}(F)`,
   `B^{munu}(F)`, analytic in `F`, vanishing at `F=0`. So GU's cure is **not** a Porrati-Rahman non-minimal
   vertex.

3. **AXIS C (-1) -- the guardian is ABSENT because the projector is EQUIVARIANT.** The cure imposes `ker Gamma`
   with a hard, Spin(9,5)-EQUIVARIANT projector `Pi` (`max ||Gamma J_i - sigma_i Gamma|| = 0`, COMPUTED). That
   is exactly the SHIAB-04 equivariant class the necessary-conditions box (2026-06-27) proved **cannot close
   the complex**; a valid guardian must realize `ker Gamma` cohomologically via a **non-equivariant**
   compensator `sigma_c`. GU's cure as written is the hard-projector configuration the box rejects, so the
   cohomological local-SUSY guardian is NOT instantiated.

A structural report (Q1e): the cure annihilates a 128-dim space (`ker Pi = 14*128 - 1664`, the gamma-trace
directions) -- the would-be gauge orbit a guardian `delta psi = nabla eps` would have to fill.

## Per-persona takes (run INLINE)

**Supergravity-construction theorist (de Wit-Freedman).** The decoupling result (axis A) is decisive from my
seat. A consistent massive gravitino IS a standalone gamma-traceless spin-3/2 whose subsidiary condition
`gamma . psi = 0` is preserved by the gauge algebra, not by hand. GU's cure produces precisely that field
content -- `[Pi, O]=0` is the operator statement that the RS constraint surface is dynamically invariant. But
in genuine SUGRA the constraint is a *consequence* of `delta psi = nabla eps` (a nilpotent local SUSY,
`s^2=0`); here it is imposed by a hard projector. So GU has fabricated the gravitino's kinematics without its
symmetry. My verdict: GU's cure instantiates the de Wit-Freedman field content and is missing exactly the
local SUSY that would make it a genuine gravitino. That missing piece is axis C, and it is non-optional.

**Higher-spin / Vasiliev specialist.** Ruled out from my side, and the reverse construction makes it cleaner
than the forward one. Vasiliev needs (i) an infinite tower (the master field `W` valued in `hs(lambda)`),
(ii) an AdS / `Lambda<0` background, and (iii) an algebra with the right truncations. GU's cure fails all
three: it decouples to a SINGLE standalone spin-3/2 (axis A = "not a tower"), it was built with no `Lambda`
input (axis E), and it lives over quaternionic `M(64,H)`, which `oq-rs3-gu-vasiliev-comparison` shows has no
`hs(lambda)` truncation (FC-3). Vasiliev scores 1/5. There is no truncated or non-standard higher-spin gauging
that a finite `Sp(32,32;H)` realizes in place of SUSY -- the finite content forbids the tower that HS UV-
completeness requires. **The guardian, if any, is local SUSY, not a higher-spin symmetry.**

**Porrati-Rahman / cure-coupling expert.** This is the subtle one, and the reverse direction corrects a naive
read. Wave 34 called Porrati-Rahman "the structural template for the cure term," and at the level of *purpose*
(restore constraint invertibility) that is right. But at the level of *operator structure* GU's cure is NOT a
Porrati-Rahman cure: PR keeps the field coupled and adds an `F`-analytic non-minimal vertex; GU's cure
decouples the field (axis A) and adds a kinematic projector (axis B). PR matches only 3/5. What survives is
the CONSEQUENCE, not the mechanism: a standalone massive spin-3/2 *without* a guardian is exactly the regime
where PR's own follow-up (Rahman 2011) bites -- a finite UV cutoff, strong coupling in the helicity-1/2 mode.
So GU's cure, guardian-free, lands in the Porrati-Rahman-EFT *regime* (finite-cutoff EFT) even though its
operator is not a PR vertex. That is the honest reconciliation of "PR is the template" (Wave 34) with "PR is
not the operator match" (here): PR names GU's UV STATUS, de Wit-Freedman names GU's FIELD CONTENT.

**EFT-matching specialist.** The two readings are not in conflict; they are the two legs of one verdict. Field
content matches the gravitino (4/5, de Wit-Freedman / Deser-Zumino). UV status, with axis C absent, is a
finite-cutoff EFT (Porrati-Rahman regime, Rahman cutoff). Matching says: integrate out above `Lambda` and GU's
cured RS is an EFT of a standalone massive spin-3/2; the only operator that UV-completes it while preserving
`gamma . psi = 0` under evolution is a local-SUSY gauge completion (flip axis C). The scale `mu_DW` (free,
ledger 7) is the natural candidate for that cutoff, but nothing here computes it. Note the internal tension the
carve already flagged: the guardian's required compensator `sigma_c` is NON-equivariant, whereas GU's cure is
equivariant -- so the guardian is not a small deformation of the current cure; it replaces the hard projector
with a gauge orbit.

**Philosopher of science.** Watch the integrity line. "GU's cure IS a de Wit-Freedman gravitino" would be a
manufactured win. What we actually exhibited is narrower and more honest: a 4/5 structural correspondence whose
single failing axis is *precisely* the guardian. That is not a match; it is a diagnosis. "A gravitino minus
its guardian" is falsifiable and modest: it says GU built the kinematics and is missing the symmetry, and it
predicts exactly what a completion must add (a non-equivariant `sigma_c`). Equally, "guardian-free -> Porrati-
Rahman finite-cutoff EFT" is as real a result as a SUSY match would have been -- it is the branch's honest
lower bound, and the required-reading instruction explicitly values it. The reverse construction earns its
keep by turning the guardian question from a search into a single named missing axis.

## Team verdict

**GU's forced g=1 ker-Gamma cure INSTANTIATES the de Wit-Freedman / Deser-Zumino GRAVITINO field content (a
standalone gamma-traceless massive spin-3/2), matching 4 of 5 structural axes, but LACKS the guardian (axis C
-- the cohomological, non-equivariant local SUSY). As written it is therefore a Porrati-Rahman-REGIME finite-
cutoff EFT: a gravitino's kinematics without a gravitino's symmetry = a Velo-Zwanziger / Rahman-exposed
standalone massive RS. The unique UV-completing guardian is a de Wit-Freedman local SUSY (super-IG); its
required signature is a NON-equivariant BRST compensator `sigma_c` that upgrades the hard equivariant projector
`Pi` to a gauge orbit `delta psi = nabla eps`. Vasiliev is excluded (finite content, no AdS, no `hs(lambda)`
truncation over `M(64,H)`).**

The two named templates are not rivals: **de Wit-Freedman names GU's field content; Porrati-Rahman names GU's
UV status.** Both are simultaneously true, and together they say the same thing the forward branches conclude
from the other side -- the guardian is the single missing datum -- but reached from the cure operator itself.

## COMPUTED vs ARGUED

- **COMPUTED (exact, on the verified `Cl(9,5)=M(64,H)` rep):** the anchors `C2=155.3625`, `||[Pi,M_D]||=58.72`,
  `rank(Pi)=1664`; the g=1 cure kills the leakage (`6e-14`); axis A -- the cure DECOUPLES (`||[Pi,O]||=2e-14`
  vs bare `58.72`); axis B -- the correction is a pure constraint-projector object (`||Delta - (-(Pi M_D Q +
  Q M_D Pi + Q M_D Q))|| = 1e-13`); axis C -- `Pi` is Spin(9,5)-equivariant (`max residual = 0`); the
  gauge-orbit dimension (`dim ker Pi = 128`); the match-score bookkeeping (dWF/DZ 4/5, PR 3/5, VAS 1/5) and
  the single separating axis (C).
- **ARGUED (structural / literature read as data):** the template signature bits for PR / dWF / DZ / Vasiliev
  (from Wave 34 + the Vasiliev-comparison file); that a non-equivariant `sigma_c` is the required guardian
  signature (from the necessary-conditions box); that `mu_DW` is the plausible cutoff scale; the identification
  of "guardian-free standalone massive RS" with the Rahman-cutoff EFT regime.

## Honest limits

1. **The five axes are a modeling choice.** The match verdict is only as good as the axis set; a different
   basis of structural questions could shift a bit. The axes were chosen to be the ones separating the four
   templates in the repo's own descriptions, and GU's four load-bearing bits (A, B, C, D) are computed, not
   assigned. But "4/5 match" is a bookkeeping statement over an ARGUED template encoding, not a theorem.
2. **A 4/5 match is a diagnosis, not an instantiation.** I did NOT show GU's cure IS a de Wit-Freedman
   gravitino. I showed it shares the gravitino's field content and differs on exactly the guardian axis. The
   claim is deliberately the weaker, honest one.
3. **No guardian was constructed.** The reverse-engineered guardian (a non-equivariant `sigma_c` upgrading
   `Pi` to a gauge orbit) is named and its signature is pinned, but not built or shown to exist. Whether
   `Sp(32,32;H) + [P,S]=0` actually furnishes such a local SUSY is untouched here -- that is the forward
   question this branch is blind to.
4. **The rep is the finite `Sp(64)`/`Cl(9,5)` model, not the non-compact source-action arena.** All operator
   facts are on the built `M(64,H)` rep; the `Sp(32,32;H)` non-compact real form (where the guardian would
   actually live) is not the object computed on.
5. **"Porrati-Rahman regime" is an argued UV read, not a computed cutoff.** I did not compute a cutoff `Lambda`
   or a helicity-1/2 amplitude; the finite-cutoff-EFT status is inferred from axis C being absent plus the
   Wave 34 Rahman/Sagnotti-Taronna reading, not recomputed.

## Branch re-hypothesis (blind) + ranked next-move

**Re-hypothesis.** GU's cure is not a free-standing new mechanism and not a Porrati-Rahman vertex; it is a
gravitino's KINEMATICS realized by a hard equivariant projector, MISSING only the gravitino's SYMMETRY. The
guardian question therefore has a sharp, computable form: *does there exist a NON-equivariant `sigma_c(xi)`,
outside the Spin(9,5)-equivariant family, such that the off-surface escape `(I-Pi)(M_D + sigma_c)Pi` is
BRST-exact with `s^2=0` -- i.e. that upgrades the hard projector `Pi` to a gauge orbit while keeping the
leakage zero?* If yes, axis C flips and GU's cure IS a de Wit-Freedman gravitino (guardian = local SUSY). If
provably no non-equivariant `sigma_c` closes, GU's cure is permanently the Porrati-Rahman-regime finite-cutoff
EFT. The whole H54 verdict reduces to this one existence question about a single non-equivariant operator.

**Ranked next-moves (highest leverage first):**

1. **Search for the non-equivariant `sigma_c` on the rep (COMPUTED, tractable now).** On the same
   `Cl(9,5)=M(64,H)` rep, parametrize operators OUTSIDE the equivariant family (break the `Gamma J_i = sigma_i
   Gamma` intertwining explicitly) and test whether `(I-Pi)(M_D + sigma_c)Pi = 0` admits a solution with a
   nilpotent `s` (`s^2=0`). This is the exact object the necessary-conditions box named as the "first genuinely
   new degree of freedom" and it is a finite linear-algebra search on machinery already in this test. It
   directly decides the re-hypothesis. Highest leverage.
2. **Compute the gauge-orbit / cohomology dimension (COMPUTED).** The cure annihilates a 128-dim `ker Pi`. Test
   whether that 128-dim space carries a consistent `delta psi = nabla eps` gauge action (does a 128-dim
   spinor-parameter orbit reproduce it?). A match would be positive evidence the gravitino gauge structure is
   latent in the cure; a mismatch bounds it. Cheap.
3. **Price the guardian-free branch (COMPUTED-ish).** If move 1 fails, compute the helicity-1/2 high-energy
   behavior of the cured standalone operator to exhibit the Rahman cutoff explicitly and pin the finite-EFT
   verdict, testing whether `mu_DW` sets `Lambda`. Confirms the Porrati-Rahman-regime leg quantitatively.
4. **Deser-Waldron `(m^2, Lambda)` locus check (ARGUED->COMPUTED).** Independent of the guardian, check whether
   GU's `(m2_eff in [5/6,5/4], c_L=3/8)` point sits on a partial-massless gauge line -- a different way a gauge
   invariance (a weaker guardian) could switch on. Lower priority; orthogonal hedge.

---

*Filed 2026-07-11, Wave 40, H54 branch 4 (blind). Test: `tests/wave40/H54b4_cure_guardian_reverse.py`
(deterministic, exit 0, all PASS). Exploration-grade; no canon or ledger movement. Adversarially framed: the
"de Wit-Freedman match" is exhibited as a 4/5 correspondence with the single failing axis being exactly the
guardian -- a diagnosis, not a manufactured instantiation -- and the "Porrati-Rahman finite-cutoff EFT"
guardian-free verdict is filed as an equally valuable outcome. Tree left dirty; no commit.*
