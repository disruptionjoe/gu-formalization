---
artifact_type: exploration
doc_type: construction_result
status: exploration
created: 2026-08-12
brief_version: "1.3"
target_claim: NONE-NOT-A-KILL
ledger_row: AC-E1
ledger_file: lab/process/conditional-physics-ledger-v0.216.json
ledger_row_still_live: "CONFIRMED. AC-E1 is byte-identical in v0.231, the latest ledger at HEAD f078fcbb66ff9d99b933022c28852eb7fcf65c96 -- same summary, same reason_kind IMPORTED, same mapping_grade CITED_NOT_REDERIVED, same evidence pointer. The finding applies to the LIVE ledger, not only to the v0.216 snapshot named in the brief."
repo_head_pinned: 0b2b0453a0afb831cbcb70f70352f65b120043b8
repo_head_note: "HEAD advanced to f078fcbb66ff9d99b933022c28852eb7fcf65c96 during this session (the hourly automation, which OWNS these ledgers under the multi-writer protocol). All reads reported here were taken at the pinned HEAD; AC-E1 and the evidence chain were re-checked at the new HEAD and are unchanged."
repo_access: READ-ONLY (gu-formalization untouched, working tree clean; all writes in scratchpad/ac-e1/)
title: "AC-E1 discharge attempt: independent recomputation of the 4D Standard-Model Dai-Freed shadow. RESULT: DERIVED_CONDITIONAL on the Spin/G_SM leg -- all four Omega^Spin_5(B(G_SM/Gamma_n)) recomputed from scratch by AHSS with dual-Sq^2 differentials and matching Davighi-Gripaios-Lohitsiri Table 1 exactly (Z/2, 0, Z/2, 0 for n = 1,2,3,6), with 3/3 independent controls (BSU(2)=Z/2, BU(1)=0, BSU(3)=0) matching Garcia-Etxebarria-Montero. NO DISAGREEMENT with the cited result; the revival trigger is NOT fired. But a SCOPE CORRECTION is earned: the group is NOT zero for two of the four global forms, so 'carries no obstruction' is a statement about the image of the SM CONTENT, not about the receptacle; and the row's word 'saturated' with its '16' belongs to a DIFFERENT object (Omega_5^{Spin x_{Z2} Z4} = Z/16) that the row never names and GU never assumes."
grade: "COMPUTED / exact. The AHSS computation is a new in-repo derivation (ac_e1_ahss_omega_spin_5.py, exit 0, 7/7 agreement with two published sources, 3 positive controls, d_2 o d_2 = 0 checked numerically, image-inside-kernel checked). The Z/16 leg is VERIFIED-not-derived at the group level (Smith isomorphism imported) but its saturation arithmetic is derived. Primary sources actually read: DGL arXiv:1910.11277 (PDF text extracted, Eqs 4.22/4.38/4.40/4.45 and Table 1 read verbatim); Wan-Wang arXiv:2006.16996 (PDF text extracted, Eqs 5.6/5.8 read verbatim); GEM arXiv:1808.00009 (via ar5iv, Eqs 36/51/57). No ledger edit. No verdict, canon, bar, count or posture moves."
fork_assumed: none
search_space_dim: "4 Standard Model global-form cases plus 3 independent positive controls; decided wholesale"
free_object_delta: 0
residue_touched:
  - id: AC-E1
    grade: T0
    note: EVIDENCE_ONLY_NO_LEDGER_MOVEMENT
forks_touched_not_assumed:
  - "SIGNATURE-AMBIENT (open) -- irrelevant here. Every object in this artifact lives on the 4D shadow X^4 and its 5D mapping-torus receptacle, not on the Y^14 ambient. No (9,5)/(7,7) datum enters."
  - "GENERATION-COUNT-CODOMAIN (open) -- touched only to CONFIRM the standing 2-vs-3-primary disjointness: the Z/16 leg is generation-SENSITIVE but 2-primary, coprime to the Z/3 arena. Consistent with canon/two-primary-lemma.md; nothing moves."
layer0:
  - "'anomaly' fence (inherited from cb-c-anomaly-conditions-2026-08-05.md): LOCAL perturbative (index-density) and GLOBAL (Dai-Freed/eta/bordism) are different objects with different receptacles. This artifact touches ONLY the global row."
  - "NEW near-homonym, proposed for lab/process/NAMES.md: 'the fifth bordism constraint'. Sense 1 = Omega^Spin_5(B G_SM), the plain-Spin receptacle for the gauge global anomaly, values {Z/2, 0} depending on the global form. Sense 2 = Omega_5^{Spin x_{Z2} Z4} = Z/16, the B-L/Z_4-twisted receptacle whose modulus 16 is what the SO(10) 16 'saturates'. AC-E1's summary uses sense-2 language ('the 16 saturates') over a sense-1 group name. Different structure group, different modulus, different assumption set. Do not identify."
  - "'saturated' fence: 'the receptacle is empty' (group = 0), 'the content pairs to zero' (image = 0), and 'the content exactly fills the modulus' (16 == 0 mod 16) are three distinct statements. AC-E1 currently reads as all three at once; only the second is true for every global form."
scripts:
  - scratchpad/ac-e1/ac_e1_ahss_omega_spin_5.py
route_disposition: AC_E1_RECOMPUTED__SPIN_LEG_DERIVED_CONDITIONAL__NO_DISAGREEMENT__SCOPE_CORRECTION_EARNED__NO_LEDGER_EDIT
canon_verdict_change: none
deposit: "PRE-DEPOSIT. Evidence for a wave to absorb. Binds nothing. The wave owns the disposition of AC-E1."
---

# AC-E1: independently recomputing the 4D Standard-Model Dai-Freed shadow

Ledger row `AC-E1` (`lab/process/conditional-physics-ledger-v0.216.json`) is the **only**
`IMPORTED` row in the v0.216 ledger: axis `ANOMALY_CONSISTENCY`, verdict `SAME`,
`mapping_grade: CITED_NOT_REDERIVED`, summary *"4D global SM bordism constraints are
saturated"*, distance *"independently recompute the full Dai-Freed shadow"*, revival trigger
*"a direct computation disagreeing with the cited result"*.

This artifact runs that computation.

---

## 0. Five-lens pre-flight, with structure-first expectations declared BEFORE computing

Per brief item (15), the expected group values are stated here, before the computation and
before the primary sources were read in detail. Item (14): five lenses, run inline, each
declaring basis and confidence.

### Structure-first: what I expected

| # | object | expectation stated in advance | basis |
|---|---|---|---|
| S1 | `Omega^Spin_j(pt)`, `j = 0..5` | `Z, Z/2, Z/2, 0, Z, 0` | DIRECT (standard Milnor/ABP table; also in-repo at `explorations/global-anomaly-leg-2026-07-20.md:177`) |
| S2 | which AHSS cells reach total degree 5 for `BG_SM` | **only** `(p,q) = (4,1)`, i.e. `H_4(BG;Z/2)`, because `BG_SM` has torsion-free even integral cohomology (so `H_odd = 0`) and `Omega^Spin_3 = Omega^Spin_5 = 0` | PRINCIPLE, 0.90 |
| S3 | `H_4(B G_SM; Z/2)` | `(Z/2)^3` (the degree-4 classes `c_1^2`, `c_2(SU(3))`, `c_2(SU(2))`) | DIRECT (Borel), 0.95 |
| S4 | `Omega^Spin_5(B G_SM)` | **I expected `0`**, because the row asserts the receptacle "carries no obstruction" | PRINCIPLE, 0.55 -- *flagged low: I could not see how all three `Z/2`s would die* |
| S5 | `Omega^Spin_5(BSU(2))` | `Z/2`, and it must BE the Witten anomaly -- otherwise a known anomaly would have no home | PRINCIPLE, 0.85 |
| S6 | `Omega_5^{Spin x_{Z2} Z4}(pt)` | `Z/16`, by the Smith isomorphism to `Omega^{Pin+}_4 = Z/16` (a value the repo already holds from Kirby-Taylor) | PRINCIPLE, 0.80 |

**The surprise, recorded plainly.** S4 and S5 are in direct tension: the Witten anomaly is a
real anomaly of `SU(2)` gauge theory, so `Omega^Spin_5(BSU(2))` cannot be zero; but `BSU(2)`
is a factor of `B G_SM`. Either the row's "carries no obstruction" is not a statement that the
group vanishes, or one of S4/S5 is wrong. **The computation resolved it against S4.** The
group is `Z/2` for two of the four global forms of the SM gauge group. "No obstruction" is a
true statement about the *image of the SM fermion content*, not about the receptacle. That is
the single most consequential thing this artifact found, and it was findable from the
expectation table alone.

### Lens 1 -- Bordism / stable homotopy (basis: DIRECT; confidence 0.90)

The AHSS `E^2_{p,q} = H_p(X; Omega^Spin_q(pt)) => Omega^Spin_{p+q}(X)` is the right tool at
`p+q = 5` and is fully decidable here, because the only surviving cell is `(4,1)` and the only
differentials that touch it are two `d_2`s. Higher differentials out of `(4,1)` land in
`E_{1,3} = H_1(X; Omega^Spin_3) = H_1(X;0) = 0`; higher differentials into it come from
`E_{7,-1} = 0`. So `E^3_{4,1} = E^infinity_{4,1}` and the answer is exact, not an estimate.
The one imported lemma is the identification of the two bottom `d_2`s with the dual Steenrod
square -- see Lens 4, where I read DGL's own statement of it verbatim.

Caution this lens raises: `Omega^Spin_5(BG) = 0` is a statement about a *receptacle*. A
nonzero receptacle with a content that pairs to zero is equally anomaly-free. Conflating the
two is the standard beginner error in this literature and it is exactly the error latent in
the row's phrasing. FRAME-SENSITIVE.

### Lens 2 -- Anomaly theory in QFT (basis: DIRECT; confidence 0.88)

For a 4D chiral gauge theory the Dai-Freed anomaly is the deformation class of the 5D
invertible theory `M^5 |-> exp(-2 pi i eta-bar)`, an element of `Hom(Tors Omega^Spin_5(BG), R/Z)`
in the Freed-Hopkins/Anderson-dual classification. The theory is anomaly-free iff the
homomorphism induced by its content is zero -- **not** iff the group is zero. This lens
supplies the physical reading of the surviving `Z/2`: it is the Witten `SU(2)` anomaly, and the
SM kills it by content parity (4 `SU(2)_L` doublets per generation: `Q` in 3 colours, plus `L`;
`4 = 0 mod 2`), which is precisely the check `W222` and `CB-C:C2` already ran. So the row's
*conclusion* is right; its *reason* as written is not the reason that holds.

This lens also flags that a second, inequivalent global-anomaly question exists for the SM --
the one that GEM's abstract actually headlines -- and it does not live in `Omega^Spin_5` at all.
See section 3.

### Lens 3 -- Index theory / eta-invariants (basis: PRINCIPLE; confidence 0.80)

The `Z/16` of `Omega_5^{Spin x_{Z2} Z4}` is read by the `Pin+` eta invariant
`eta_{Pin+} in Z/16` on the Poincare dual of the `Z/2` class, via the Smith map to
`Omega^{Pin+}_4 = Z/16` generated by `RP^4`. This is exactly the `3+1d` time-reversal
topological-superconductor invariant. The repo already holds `Omega^{Pin+}_4 = Z/16` at
primary-source grade (`canon/ko-degree-obstruction-ladder-RESULTS.md`, Kirby-Taylor CMH 65
(1990); table reproduced at `explorations/pin-bordism-cardinality-2026-07-21.md:166`). So the
*value* was already in-repo; what was not in-repo was the degree-5 Smith partner and its role
in AC-E1.

This lens confirms the repo's own `R2` Certificate B is a *3-dimensional* lens-space eta test
(`L(3;1,1)`), i.e. dimension-faithful for a 2D theory, not for 4D. `R2` says so itself. So the
in-repo eta evidence does not reach the 4D row either.

### Lens 4 -- Source criticism of the cited literature (basis: DIRECT; confidence 0.92)

The row's `evidence` field points at `cb-c-anomaly-conditions-2026-08-05.md:E1`, which cites
`W222` "at W222's own honest grade", and `W222` cites in-repo `R2`
(`explorations/big-swing-2026-07-03/R2-sm-boundary-mod3-arena-empty.md`). Tracing the chain to
its root is the load-bearing act of this artifact and it produces a **verified repo
disconnect**: see section 2. `R2` is honest and correct; it is the *inheritance* that drifted.

On the external side, the correct primary sources are Davighi-Gripaios-Lohitsiri
(arXiv:1910.11277) for the four global forms, and Garcia-Etxebarria-Montero (arXiv:1808.00009)
for the simple factors and for the `Z/4`/`Z/16` statement. Both were fetched and read; DGL's
PDF text was extracted so the equations could be read verbatim rather than paraphrased.
Notably the repo **already cites DGL correctly and with the right scope** in
`papers/candidates/generation-number-located-not-forced/` -- the correct scoping exists in the
papers lane and did not propagate to the ledger lane. That is a lane-crossing gap, not a
knowledge gap.

### Lens 5 -- Adversarial refutation (basis: DIRECT; confidence 0.85)

Pre-declared failure conditions for this artifact, stated before running:
- **F1** If my AHSS reproduces published values only because I hard-coded them, the result is
  worthless. *Mitigation and outcome:* the script computes from `H^*(BG;Z/2)` and the Wu
  formula only; published values appear solely in a final `assert`. Three controls whose
  answers were known independently (`BSU(2)`, `BU(1)`, `BSU(3)`, from GEM Eqs 36/51/57) are run
  through the same machinery and two of them come out **zero and one nonzero** -- so the
  machine can say both things. Non-vacuous.
- **F2** If the differentials were wrong, the four answers would still be "some subquotient of
  `(Z/2)^3`" and could coincide by luck. *Mitigation and outcome:* the same machinery
  independently reproduces `Omega^Spin_4(BG_SM) = Z^4` (DGL Table 1), which requires the
  `d_2: E_{4,1} -> E_{2,2}` map to be **surjective** -- a second, differently-shaped consequence
  of the same differential. It is. `d_2 o d_2 = 0` is also checked numerically, and
  `im subset ker` is asserted rather than assumed.
- **F3** If "saturated" means something I have not computed, the discharge is void. *Outcome:*
  it partly does. Section 3 handles it; the row's assumption set is the finding, per brief (4).

Where an adversary can still push: I did not re-derive the Smith isomorphism, and I did not
re-derive `Omega^Spin_*(pt)` or `H^*(BG;Z)` from an Adams spectral sequence. Those are named as
imported in section 4's grade table. An adversary who rejects the dual-`Sq^2` identification of
`d_2` rejects the whole derivation; that identification is quoted verbatim from DGL below.

---

## 1. What is actually cited, and what it claims

**The chain, traced to its root.**

| link | file | what it says |
|---|---|---|
| ledger row | `lab/process/conditional-physics-ledger-v0.216.json` `AC-E1` | "4D global SM bordism constraints are saturated"; `SAME` / `IMPORTED` / `CITED_NOT_REDERIVED` |
| source row | `explorations/conditional-build/cb-c-anomaly-conditions-2026-08-05.md:320` (row **E1**) | "`Omega^Spin_5(B G_SM)` carries no obstruction; the one-generation `16` saturates the fifth-bordism constraints. **AUTO** given `U4`. Cited at W222's own honest grade: the full Dai-Freed recomputation was not redone there, and is not redone here" |
| cited probe | `explorations/W222-falsify-sm-emergence-anomaly-hypercharge-2026-07-14.md:105-109` | "The two computable shadows -- `tr Y = 0` [and even doublet count] ... plus a citation to R2: `Omega^Spin_5(B G_SM)` has no 3-torsion and the SM content saturates the 5th-bordism constraints" |
| root | `explorations/big-swing-2026-07-03/R2-sm-boundary-mod3-arena-empty.md` | **`Omega^Spin_5(B G_SM) (x) Z_(3) = 0`** -- an AHSS-at-`p=3` argument that the group has **no 3-torsion**, plus an `L(3;1,1)` eta certificate |

**The root computes a 3-local statement.** `R2` is explicit and correct about its own scope: it
localises at the prime 3, uses (i) `Omega^Spin_*(pt)` is odd-torsion-free (ABP + Wall) and
(ii) `3`-locally `B G_SM ~ BU(3) x BSU(2)` is torsion-free and even, and concludes the odd-degree
`E_2` line vanishes 3-locally. `R2` even says, in its own words, that *"every SM structural
subtlety that could have opened a mod-3 arena ... is a 2-group / 2-primary phenomenon"* -- i.e.
it announces that it did **not** compute the 2-primary part. `R2` imports no target and is not
at fault.

**What the row needs is the 2-primary part.** "Carries no obstruction" and "saturated" are
statements about the whole group and the whole pairing, and the entire content of
`Omega^Spin_5(B G_SM)` is 2-primary. So the row is asserting exactly the part of the object its
root evidence declined to compute. That is the gap AC-E1's `distance` field names, and it is
real.

**What the external literature actually claims** (both read, verbatim, in section 2):
- Davighi-Gripaios-Lohitsiri, arXiv:1910.11277, JHEP 07 (2020) 232: computes
  `Omega^Spin_5(BG)` for all four global forms `G = G_SM/Gamma_n`, `n in {1,2,3,6}`, by AHSS.
  Abstract, verbatim: *"In two cases we show that there are no global anomalies beyond the
  Witten anomaly, while in the other cases we show that there are no global anomalies at all"*
  and *"our results here remain true when the SM fermion content is extended arbitrarily."*
- Garcia-Etxebarria & Montero, arXiv:1808.00009, JHEP 08 (2019) 003: the SM is free of
  Dai-Freed anomalies whatever the global form; and separately, *assuming an anomaly-free `Z_4`
  symmetry* (`B-L`-type), the `Z/16` anomaly is what ties the count of Weyl fermions per
  generation to **16, including a right-handed neutrino**.

Note that the second GEM statement -- the one that contains a "16" and a genuine *saturation* --
is under a **different tangential structure** and is not a statement about `Omega^Spin_5(BG_SM)`
at all. Section 3.

---

## 2. The recomputation

Script: `scratchpad/ac-e1/ac_e1_ahss_omega_spin_5.py`, exit 0.

### 2.1 Inputs, each typed

| input | value | grade |
|---|---|---|
| `Omega^Spin_j(pt)`, `j=0..5` | `Z, Z/2, Z/2, 0, Z, 0` | IMPORTED (Milnor/ABP; standard table, also held in-repo) |
| AHSS `E^2_{p,q} = H_p(X;Omega^Spin_q(pt))` | -- | IMPORTED (standard) |
| `d_2: E^2_{p,1} -> E^2_{p-2,2}` is the dual of `Sq^2`; `d_2: E^2_{p,0} -> E^2_{p-2,1}` is `rho_2` then dual `Sq^2` | -- | **IMPORTED, load-bearing.** DGL state it verbatim: *"`d_2^{p,1} : H_p(B; Omega^Spin_1) -> H_{p-2}(B; Omega^Spin_2)` is the dual of the Steenrod square [34,35]"* |
| `H^*(BG;Z)` for the four `BG` | polynomial on Chern classes (Borel) | IMPORTED (standard) |
| Wu formula `Sq^2 c_j = c_1 c_j + (j-1) c_{j+1}` | -- | IMPORTED (standard) |
| `Sq^1 = 0` on the whole algebra | since every generator is the mod-2 reduction of an integral class, hence killed by the Bockstein; `Sq^1` is a derivation | **DERIVED here** (this is what makes `Sq^2` a derivation, which is what the script uses) |
| the four group identifications below | -- | **DERIVED here** |
| everything downstream | -- | **DERIVED here** |

### 2.2 Identifying the four global forms

DGL's `Gamma_6` is generated by `xi = (omega, eta, e^{2 pi i/6})` (their Eq 4.2), with
`Gamma_3 = <xi^2>`, `Gamma_2 = <xi^3>`. Working these out:

| `n` | `G_SM/Gamma_n` | why | grade |
|---|---|---|---|
| 1 | `SU(3) x SU(2) x U(1)` | -- | trivial |
| 2 | `SU(3) x U(2)` | `(SU(2) x U(1))/Z_2 = U(2)`; DGL state this at their Eq (4.3) | CONFIRMED (agrees with source) |
| 3 | `U(3) x SU(2)` | `(SU(3) x U(1))/Z_3 = U(3)` via `(A,z) |-> zA`, kernel `{(z^{-1}I, z): z^3=1}` | **DERIVED** (also in-repo at `R2` Certificate A) |
| 6 | `S(U(3) x U(2))` | `phi(A,B,z) = (z^{-2}A, z^3 B)`; `3(-2) + 2(3) = 0` so the image lies in `S(U(3)xU(2))`; kernel is generated by `(z_0^2 I_3, z_0^{-3} I_2, z_0) = (omega, eta, z_0) = xi` exactly; surjective by a 6th-root argument | **DERIVED** |

and the cohomology of the last one, which is the only non-obvious case:

> **Lemma (derived here).** `U(3) x U(2) ~= S(U(3) x U(2)) x U(1)`, via
> `((M,N), z) |-> (zM, z^{-1}N)`. It is a homomorphism; it is injective because
> `zM = I_3, z^{-1}N = I_2` forces `det M det N = z^{-3} z^{2} = z^{-1} = 1`; it is surjective by
> taking `z = det P det Q`. Hence
> `H^*(B S(U(3)xU(2)); Z) = Z[c_1,c_2,c_3,c'_1,c'_2]/(c_1 + c'_1)`, **torsion-free and even**.

This lemma is what lets the `n=6` case be handled by the same elementary machinery as the other
three, without DGL's `K(Z/3,2)` route.

### 2.3 The degree-5 diagonal collapses to one cell

For all four `BG` (torsion-free, even integral cohomology, `G` connected):

| cell | value | reason |
|---|---|---|
| `E^2_{5,0} = H_5(BG;Z)` | `0` | `H_odd = 0` |
| `E^2_{4,1} = H_4(BG;Z/2)` | `(Z/2)^3` | the only live cell |
| `E^2_{3,2} = H_3(BG;Z/2)` | `0` | `H_3(;Z)=0`, `H_2(;Z)` free, so the `Tor` term vanishes too |
| `E^2_{2,3}` | `0` | `Omega^Spin_3(pt) = 0` |
| `E^2_{1,4} = H_1(BG;Z)` | `0` | `G` connected |
| `E^2_{0,5}` | `0` | `Omega^Spin_5(pt) = 0` |

So `Omega^Spin_5(BG) = ker(d_2: E_{4,1} -> E_{2,2}) / im(d_2: E_{6,0} -> E_{4,1})`, exactly.
`H_6(BG;Z)` is free, so `rho_2` is onto `H_6(;Z/2)` and the incoming image is the full dual-`Sq^2`
image.

### 2.4 The `Sq^2` data, per group

With `t = c_1 mod 2` (degree 2), `c_2, c_3` the `SU(3)`/`U(3)` classes, `c'_2` the `SU(2)`/`U(2)`
class:

| `n` | `Sq^2 c_2` | `Sq^2 c'_2` | `Sq^2 t` |
|---|---|---|---|
| 1 | `c_3` (`c_1 = 0` in `SU(3)`) | `0` (`c'_1 = c'_3 = 0` in `SU(2)`) | `t^2` |
| 2 | `c_3` | `t c'_2` (`U(2)`: `c'_3 = 0`) | `t^2` |
| 3 | `t c_2 + c_3` (`U(3)`) | `0` | `t^2` |
| 6 | `t c_2 + c_3` (`U(3)`) | `t c'_2` (`U(2)`, `c'_1 = -c_1 == c_1 mod 2`) | `t^2` |

`ker(d_2 out)` is `<a_{c_2}, a_{c'_2}>` in every case (only `Sq^2 t = t^2` hits `H^4`, so only the
`t^2`-dual dies). `im(d_2 in)` is `<a_{c_2}>` for `n = 1, 3` and `<a_{c_2}, a_{c'_2}>` for
`n = 2, 6`. The `c'_2` dual survives exactly when the `SU(2)` factor is **not** absorbed into a
`U(2)`.

### 2.5 The computed values, against the published ones

| object | **derived here** | published | source read | agree |
|---|---|---|---|---|
| `Omega^Spin_5(BSU(2))` | `Z/2` | `Z/2` | GEM 1808.00009 Eq (36) | YES |
| `Omega^Spin_5(BU(1))` | `0` | `0` | GEM 1808.00009 Eq (51) | YES |
| `Omega^Spin_5(BSU(3))` | `0` | `0` | GEM 1808.00009 Eq (57), `BSU(n>2)` | YES |
| `Omega^Spin_5(B G_SM)` | **`Z/2`** | `Z/2` | DGL 1910.11277 **Eq (4.22)** + Table 1 | YES |
| `Omega^Spin_5(B(G_SM/Gamma_2))` | **`0`** | `0` | DGL **Eq (4.38)** + Table 1 | YES |
| `Omega^Spin_5(B(G_SM/Gamma_3))` | **`Z/2`** | `Z/2` | DGL **Eq (4.40)**, **Eq (C.5)**, **Eq (C.8)** (they give two derivations) + Table 1 | YES |
| `Omega^Spin_5(B(G_SM/Gamma_6))` | **`0`** | `0` | DGL **Eq (4.45)** + Table 1 | YES |
| `Omega^Spin_4(B G_SM)` (cross-check on the differential) | `Z^4` | `Z^4` | DGL **Eq (4.27)** + Table 1 | YES |

**7/7 plus the degree-4 cross-check.** DGL's own identification of the surviving class, verbatim:
*"where we can identify the potential global anomaly in this theory with the Witten anomaly
associated to the `SU(2)` factor."* My computation independently produces that generator: the
surviving class is the dual of `c_2` of the `SU(2)`/`U(2)` factor, and it survives exactly for the
two `n` where that factor is a genuine `SU(2)`. Same object, same generator, same reason.

### 2.6 The SM content pairs to zero

The surviving `Z/2` is the Witten anomaly, evaluated by the number of `SU(2)_L` doublets mod 2.
One `SO(10)` **16** (= one SM generation with `nu^c`) contains `Q` in 3 colours plus `L`, i.e.
**4** doublets. `4 = 0 mod 2`; and `1, 2, 3` generations give `4, 8, 12`, all even.
**The SM content is anomaly-free under the receptacle, for all four global forms.** This is the
check `CB-C:C2` already ran, and it is the *true* reason the row's conclusion holds.

### 2.7 One observed tension in the cited source, non-load-bearing

DGL's Table 1 records the `Gamma_6` row in degrees 2 and 4 as unresolved extensions
`e(Z/3, Z x Z/2)` and `e(Z/3, e(Z/3, Z^4))`. Under the isomorphism
`G_SM/Gamma_6 ~= S(U(3) x U(2))` derived in 2.2 (whose classifying space has torsion-free even
cohomology), those degrees resolve as `Z x Z/2` and `Z^4` with **no 3-torsion**, matching the
other three rows. This is consistent with the repo's own `R2` Certificate A (no 3-torsion in any
odd degree, 3-locally) and with DGL's own degree-5 answer of `0`. Reported as an observation at
**PROPOSED** grade -- it may equally be that DGL simply left extensions from their `K(Z/3,2)`
route unresolved because only degree 5 was needed. **Degree 5, the only degree AC-E1 depends on,
is unaffected and agrees.** Not a kill, not a correction to anyone; noted for completeness.

---

## 3. The other object: `Omega_5^{Spin x_{Z2} Z4} = Z/16` -- where "saturated" actually lives

The row's summary says *"the one-generation `16` saturates the fifth-bordism constraints."* A "16"
saturating something is a statement about a modulus of 16. `Omega^Spin_5(B G_SM)` has no such
modulus -- it is `Z/2` or `0`. The object with the modulus 16 is a different one.

**The group.** Wan-Wang arXiv:2006.16996 Eq (5.8), verbatim:

> `Omega_5^{Spin x_{Z2} Z4} = Z_16` (generated by `RP^5`) `--(cap A_{Z2})-->` `Omega_4^{Pin+} = Z_16`
> (generated by `RP^4`)

and their Eq (5.6) gives the full Smith ladder
`... -> Omega_6^{Pin-} = Z_16 -> Omega_5^{Spin x_{Z2} Z4} = Z_16 -> Omega_4^{Pin+} = Z_16 -> Omega_3^{Spin x Z2} = Z_8 -> ...`.
The right-hand anchor `Omega^{Pin+}_4 = Z/16` is **already held in-repo at primary-source grade**
(`canon/ko-degree-obstruction-ladder-RESULTS.md`, Kirby-Taylor CMH 65 (1990); table at
`explorations/pin-bordism-cardinality-2026-07-21.md:166`). So the repo already owned the value on
the `Pin+` side and did not own its degree-5 Smith partner.

Grade: the group value is **INDEPENDENTLY VERIFIED, NOT DERIVED** -- I read it in a primary
source and it is consistent with a value the repo verified separately, but I did not derive the
Smith isomorphism.

**The saturation arithmetic (derived here, exact):**

| content | `n_gen = 1` | `2` | `3` | verdict |
|---|---|---|---|---|
| 15 Weyl (no `nu_R`) | `15` | `14` | `13` | **ANOMALOUS at every `n_gen` in `1..15`** (checked exhaustively) |
| **16** Weyl (with `nu_R`, `= SO(10)` **16**) | `0` | `0` | `0` | **CANCELS; and `16 == 0 mod 16` fills the modulus EXACTLY** |

Cross-check against the source: Wan-Wang write *"the SM with three generations of 15 Weyl
fermions has the anomaly index `nu = -3 in Z_16`"*. My arithmetic gives `3 x 15 = 45`,
`45 mod 16 = 13 = -3 mod 16`. Exact agreement.

**This is the only sense in which anything is "saturated."** Under plain `Spin`, `SM` content
gives a *vanishing pairing against a small receptacle* -- not saturation. Under
`Spin x_{Z2} Z4`, the `16` *exactly fills a modulus of 16* -- that is saturation, and it is the
statement GEM headline. The row's noun ("saturated") and its numeral ("the 16") belong to the
second object; the group it names is the first.

---

## 4. Assumption-set comparison -- FRAME-SENSITIVE, per brief (4)

| axis | GU / repo side (`CB-C`, `W222`, canon) | DGL 1910.11277 | GEM 1808.00009 `Z/16` leg | match? |
|---|---|---|---|---|
| tangential structure on `X^4` | **`Spin`.** `canon/w2-y14-spin-structure.md`: *"`X4` spin is a genuine precondition for GU's generation-count machinery, not a free choice"* (W2-01/W2-FC1); `Spin^h` was checked and does **not** relax it (W2-FC2) | **`Spin`** | **`Spin x_{Z2} Z4`** (spin bundle twisted by a `Z_4` extension of `B-L`) | **MATCHES DGL. Does NOT match GEM's `Z/16` leg.** |
| gauge group / global form | `G_SM` written as `SU(3) x SU(2) x U(1)`; the `Z_6` global form is **never selected** anywhere in the AC-E1 chain | all four `Gamma_n`, `n in {1,2,3,6}`, treated as equally valid | -- | **UNDERSPECIFIED on the GU side.** Consequential: the group is `Z/2` for `n in {1,3}` and `0` for `n in {2,6}` |
| fermion content per generation | the `SO(10)` **16**, i.e. **`nu^c` IS included** (`W222`: Pati-Salam branching of the 16; `CB-C:C2`: "the `SO(10)` **16** carries 4 `SU(2)_L` doublets per generation") | arbitrary content (their result is content-independent) | requires exactly `0 mod 16` per generation; `15` fails | **MATCHES.** GU's `16` is the content that saturates `Z/16` |
| `B-L` gauged, or extended to a `Z_4` | **not assumed anywhere in the chain**; no `Z_4`/`B-L` structure is posited | not assumed | **assumed** (the whole leg is conditional on "certain anomaly-free `Z_4` symmetry") | **MISMATCH, and it is the load-bearing one** |
| chirality of the carrier | `W222` HONEST CAVEAT: the carrier delivers a **vectorlike `16 + 16bar`**; `CB-C:F2`/`PH-K1-KINEMATIC`: every `ker Gamma` block is chirality-balanced (`192+192 / 576+576 / 64+64`) | assumes a chiral 4D theory | assumes a chiral 4D theory | **MISMATCH upstream of this row.** Both external computations presuppose the chiral 4D content that `U4` is supposed to produce and has not |

**Reading of the table.** Three findings, in descending order of consequence:

1. **The `Z_4`/`B-L` mismatch is the real one.** GU assumes plain `Spin` (canon, load-bearing,
   twice-checked) and does **not** assume `B-L` is a `Z_4`. Therefore GU is **not** entitled to
   the `Z/16` saturation statement -- which is exactly the statement its row's wording invokes.
   Under GU's actual assumption set, the applicable object is `Omega^Spin_5(B G_SM)`, the
   applicable check is "4 doublets, even", and there is no saturation anywhere. **Losing the
   `Z/16` claim costs GU nothing** (the check it does own still passes) but it also **removes a
   piece of apparent explanatory power the row's phrasing implies** -- namely that GU's `16`
   is *forced* by a global anomaly. It is not, under GU's own structure.
2. **The content matches and that is a genuine (if unclaimed) fit.** If a future GU horn *did*
   adopt a `Z_4` `B-L`, GU's `SO(10)` **16** would saturate `Z/16` exactly, and the 15-Weyl
   content would not. Recorded as available, **not** claimed, because the structure is not
   assumed. FRAME-SENSITIVE: compressing this to "GU's 16 is explained by the `Z/16` anomaly"
   would be false under the current assumption set.
3. **The global form of `G_SM` is unspecified on the GU side.** Because the answer is `Z/2` for
   `n in {1,3}` and `0` for `n in {2,6}`, a row that says "the receptacle carries no obstruction"
   is form-dependent, while "the SM content pairs to zero" is form-independent (DGL's
   arbitrary-content result covers all four). The form-independent phrasing is the one the row
   should carry.

Per `GEOMETER-VS-PHYSICS-OBJECTS.md`: **no geometer-vs-physics fork is in play here.** Every
object in this artifact -- `X^4`, its spin structure, `G_SM`, the 5D mapping torus, the bordism
receptacle -- is a standard-field object living on the 4D shadow, downstream of the `U4`
reduction. Nothing in the `Y^14` / `Sp(64)` / `Cl(7,7)`-vs-`Cl(9,5)` layer enters. The construction
is declared **standard-field on both sides**, and that is why the computation transfers at all.

---

## 5. Verdict

### 5.1 The letter

**(a) DERIVED -- specifically `DERIVED_CONDITIONAL` -- for the `Spin`/`G_SM` leg,
which is the leg the row's named object belongs to.**

- I reproduced all four `Omega^Spin_5(B(G_SM/Gamma_n))` by my own AHSS computation from
  `H^*(BG;Z/2)`, the Wu formula, and the dual-`Sq^2` differentials, with three independent
  positive/negative controls and a degree-4 cross-check. 7/7 agreement plus the cross-check.
- It is `DERIVED_CONDITIONAL` and **not** `DERIVED`, for exactly three named reasons: (i) the
  identification `d_2 = dual Sq^2` is imported, not derived here; (ii) `Omega^Spin_*(pt)` and
  `H^*(BG;Z)` are imported standard tables, not re-derived from an Adams spectral sequence;
  (iii) the row's conclusion additionally requires the *content* pairing (`4` doublets, even),
  which is a `CB-C:C2`/`W222` fact and is `GIVEN U4` -- the whole row is downstream of an
  unbuilt reduction. Removing (i) and (ii) would make it `DERIVED`; (iii) is structural and
  cannot be removed by any bordism computation.

**(b) INDEPENDENTLY VERIFIED, NOT DERIVED -- for the `Z/16` leg,** which is the leg the row's
*wording* invokes. The group value `Omega_5^{Spin x_{Z2} Z4} = Z/16` was read in a primary
source and is consistent with the repo's separately-verified `Omega^{Pin+}_4 = Z/16`; the Smith
isomorphism was not re-derived. The **saturation arithmetic on top of it is derived and exact**.

**(c) DISAGREEMENT: NO.** The revival trigger *"a direct computation disagreeing with the cited
result"* is **NOT fired**. My computation agrees with DGL and GEM in every entry.

**(d) BLOCKED: NO** for the computation. What is *not* discharged is the row's dependency on
`U4` (the `14 -> 4` reduction and chirality production), which no bordism computation can touch.

### 5.2 Can the row move?

**Yes, but the honest move is not a one-word swap.** Three things are true at once and a wave
should hold all three:

1. **The row's conclusion is CORRECT.** The SM content is free of `Omega^Spin_5` global
   anomalies for all four global forms. That much is now derived in-repo rather than cited.
2. **The row's stated reason is WRONG AS WRITTEN.** "`Omega^Spin_5(B G_SM)` carries no
   obstruction" reads as "the receptacle is empty." It is not: it is `Z/2` for
   `n in {1,3}`, and that `Z/2` is the Witten anomaly. The correct statement is
   *"the SM content pairs to zero against `Omega^Spin_5(B G_SM)`, which is `Z/2` for
   `n in {1,3}` and `0` for `n in {2,6}`; the pairing is the even-doublet-count check."*
3. **The row's word "saturated" points at a DIFFERENT OBJECT under a structure GU does not
   assume.** Either the word goes, or the `Spin x_{Z2} Z4` assumption is declared -- and if it
   is declared, it must be declared as an *assumption*, since `canon/w2-y14-spin-structure.md`
   commits GU to plain `Spin`.

Proposed disposition, offered as evidence and **binding nothing** (brief item 7 -- the wave
owns this):

| field | current | proposed | why |
|---|---|---|---|
| `reason_kind` | `IMPORTED` | `DERIVED_CONDITIONAL` | the group values are now derived in-repo; the conditionality is `U4` plus two named standard imports |
| `mapping_grade` | `CITED_NOT_REDERIVED` | `REDERIVED_CONDITIONAL` (or the taxonomy's nearest existing kind) | `taxonomy.unknown_kind_rule` is `NEW_KIND_REQUIRED__FORCED_FIT_FORBIDDEN`; do not force-fit |
| `summary` | "4D global SM bordism constraints are saturated" | "SM content pairs to zero in `Omega^Spin_5(B(G_SM/Gamma_n))` for all four global forms" | removes the receptacle/pairing conflation and the borrowed "saturated" |
| `verdict` | `SAME` | `SAME` (unchanged) | the physics conclusion did not move |
| `evidence` | `cb-c-anomaly-conditions-2026-08-05.md:E1` | + this artifact + DGL Eqs 4.22/4.38/4.40/4.45 + GEM Eqs 36/51/57 | root evidence `R2` supports only the 3-local part |

A wave may reasonably instead **split the row**: one row for the `Spin` receptacle (now derived)
and one for the `Spin x_{Z2} Z4` / `Z/16` statement (`NEEDS` / `EXTERNAL_DATUM`: the `Z_4` `B-L`
structure GU does not assume). The ledger's `migration_rule` supports `split_from` edges. I do
not choose between these.

---

## 6. What a wave must verify before absorbing this

1. **Re-run the script.** `python3 scratchpad/ac-e1/ac_e1_ahss_omega_spin_5.py`, expect exit 0
   and `ALL CHECKS PASS`. It is self-contained, no dependencies, exact integer arithmetic over
   `F_2`, no floats.
2. **Check the one load-bearing import.** `d_2 = ` dual `Sq^2` in the spin-bordism AHSS. If this
   is wrong the derivation is void. It is quoted verbatim from DGL section 3 (their Eq 3.15) and
   is standard; a wave that wants belt-and-braces should confirm it against Teichner or
   Beaudry-Campbell.
3. **Check the `n=6` lemma independently.** `U(3) x U(2) ~= S(U(3)xU(2)) x U(1)` and
   `G_SM/Gamma_6 ~= S(U(3)xU(2))` are derived in 2.2 and are what let `n=6` be done elementarily.
   Both are elementary and checkable in five minutes. If the second is wrong, only the `n=6`
   row of my table is affected (and it agrees with DGL anyway).
4. **Do NOT let the `Z/16` statement propagate as a GU result.** GU assumes plain `Spin`
   (`canon/w2-y14-spin-structure.md`). The `Z/16` saturation is conditional on a `Z_4` `B-L`
   that GU does not posit. Recording it as "available if a horn adopts it" is fine; recording it
   as "GU's 16 is explained" is not.
5. **Propagate the scope fix upstream, not just to the ledger row.** `CB-C:E1` and `W222`'s
   frontmatter carry the same "carries no obstruction / saturates" phrasing. The correct scoping
   already exists in the repo, in the papers lane
   (`papers/candidates/generation-number-located-not-forced/...:90` and
   `.../review/prior-art-sweep-2026-07-13.md:76-95`, which flags this as a "scoping bug" in
   so many words). This is a **lane-crossing propagation gap**, and the fix is to point the
   ledger lane at the papers lane's already-correct wording.
6. **Note the NAMES.md candidate** in this artifact's `layer0` block: "the fifth bordism
   constraint" is a two-sense homonym (`Omega^Spin_5(BG_SM)` vs `Omega_5^{Spin x_{Z2} Z4}`) and
   it has already bitten once, in this row.
7. **Nothing here touches `U4`.** The row remains `AUTO given U4`. A discharged AC-E1 does not
   move the count, the chirality gap, or any verdict.

---

## 7. Three-charge self-hostile review

Empty lists are stated explicitly, per brief item (8).

### Charge 1 -- "You did not actually derive anything; you looked up the answer and dressed it up."

**Partly fair, and here is the exact boundary.** What I derived: the four group values, from
`H^*(BG;Z/2)` plus the Wu formula plus the dual-`Sq^2` differentials, in a script that contains
the published values only inside a terminal `assert`. The script's three controls include two
zeros and one nonzero, so it is not a machine that always answers the same way; and it
independently reproduces `Omega^Spin_4(BG_SM) = Z^4`, a differently-shaped consequence of the
same differentials that I did not need and did not tune for. What I did **not** derive, named
without hedging: the dual-`Sq^2` identification of `d_2`; `Omega^Spin_*(pt)`; `H^*(BG;Z)`; the Wu
formula; the Smith isomorphism. Those are why the grade is `DERIVED_CONDITIONAL` and not
`DERIVED`.

**Where the charge lands hardest:** I read DGL's abstract ("in two cases ... no global anomalies
beyond the Witten anomaly") *before* completing all four cases, though after forming the
expectation table in section 0 and after seeing the `S4`/`S5` tension. So the four-way pattern
was not blind. The per-group *mechanism* (which `Sq^2` term kills which dual class, and why the
`SU(2)` class survives exactly when the factor is not absorbed into a `U(2)`) was derived, and it
is what an adversary should check, since it is the part a lookup cannot supply.

### Charge 2 -- "Your headline finding is a rewording, not a result. The row's conclusion is unchanged; you moved a noun."

**This is the strongest charge and I concede most of it.** The physics did not move: the SM was
anomaly-free before this artifact and is anomaly-free after. `verdict: SAME` stays `SAME`. If
the ledger's purpose is to record whether the SM is consistent, AC-E1 needed no work.

**What I do not concede:** the ledger's purpose is to record *how much of GU's physics the repo
has earned versus borrowed*, and `IMPORTED` is a claim about provenance, not about truth. On
provenance, three things changed and are checkable: (i) the group values are now in-repo derived
rather than cited; (ii) the root evidence (`R2`) is now shown to support only the **3-local**
part of what the row asserts, so the row was importing across a scope gap it did not name --
and `R2`'s own text says it did not compute the 2-primary part, which is the entire content of
the group; (iii) the receptacle is **not zero** for two of four global forms, so a reader who
took "carries no obstruction" at face value held a false belief about a group. Whether (i)-(iii)
justify a row edit is the wave's call, not mine.

### Charge 3 -- "The `Z/16` section is scope creep. The row says `Omega^Spin_5`; you went and found a different group so you would have something to report."

**Rejected, and here is why the direction matters.** I did not import the `Z/16` to strengthen a
GU claim -- I imported it to show GU **cannot** have it. The row's own words are "the
one-generation **16** saturates the fifth-bordism constraints." A modulus-16 saturation cannot be
a statement about a group of order 2 or 1. Either the row means the `Z/16` object, in which case
it is asserting something under a structure `canon/w2-y14-spin-structure.md` forbids GU from
assuming; or it does not, in which case the words "16" and "saturates" are borrowed decoration
on a `Z/2` parity check. Section 3 exists to force that choice, and both branches **reduce**
what the repo may claim. That is the correct polarity for a discharge attempt and I would have
reported it identically had it gone the other way.

**Residual I could not close, stated plainly:** I cannot rule out that the row's author meant
"saturated" loosely, as "every available constraint is met," in which case charge 3 has more
bite than I have allowed and section 3 is a longer footnote than it deserves. The NAMES.md
candidate is filed either way, because the two objects are genuinely distinct and both are
called "the fifth bordism constraint" in this repo.

### Empty lists, stated explicitly

- **Kill claims made: NONE.** `target_claim: NONE-NOT-A-KILL`. No row of
  `lab/sources/source-claim-register.yaml` is targeted. The nearest registered claim,
  `SC-CHI-50` (the chiral-anomaly critique misses because GU is not chiral), is **not**
  addressed here: this artifact is about the SM shadow's global anomaly, not about GU's own
  chirality. `SC-CHI-50` is untouched in both directions.
- **Novelty claims made: NONE.** `python3 lab/process/novelty-check.py` returned 1257 prior
  hits across the operative terms and the prior art was read: `R2` (the root), `W222`,
  `explorations/global-anomaly-leg-2026-07-20.md` (which already cites GEM's
  `Omega^Spin_5(BSU(2)) = Z/2`), `explorations/path3-branchC-cobordism-2026-07-11.md`,
  `explorations/pin-bordism-cardinality-2026-07-21.md` (which already holds the full `Pin+/Pin-`
  table including `Omega^{Pin+}_4 = Z/16`), `canon/ko-degree-obstruction-ladder-RESULTS.md`,
  `canon/two-primary-lemma.md`, and the papers-lane scoping at
  `papers/candidates/generation-number-located-not-forced/` (which **already** states the
  `Spin x_{Z2} Z4` scope correctly and already cites DGL). The only thing here that is new
  **to this repo** is the in-repo AHSS derivation of the four group values and the
  identification of the ledger-lane scope gap. The physics is entirely prior art, external and
  internal, and is cited as such.
- **Verdicts, canon entries, bars, counts, promotions, LANE-STATE entries or posture moved: NONE.**
- **Files written to `repos/public/gu-formalization`: NONE.** The repo was read at pinned HEAD
  `0b2b0453a0afb831cbcb70f70352f65b120043b8` and not modified. All output is in
  `scratchpad/ac-e1/`.
- **Free objects introduced: NONE.** No new unknown, no new required computation, no new
  receptacle.

---

## Appendix: primary sources actually read (not merely cited)

| source | how read | what was taken |
|---|---|---|
| Davighi, Gripaios, Lohitsiri, *Global anomalies in the Standard Model(s) and Beyond*, JHEP 07 (2020) 232, arXiv:1910.11277 | PDF fetched and text extracted; abstract, section 3 (Eq 3.15), section 4 (Eqs 4.1, 4.2, 4.3, 4.22, 4.27, 4.38, 4.40, 4.45, 4.51), Table 1, Appendix C (Eqs C.5, C.8) read verbatim | all four `Omega^Spin_5` values; `Omega^Spin_4 = Z^4`; the `Gamma_n` generators; the `d_2 = ` dual `Sq^2` statement; the Witten identification |
| Garcia-Etxebarria, Montero, *Dai-Freed anomalies in particle physics*, JHEP 08 (2019) 003, arXiv:1808.00009 | ar5iv HTML fetched | `Omega^Spin_5(BSU(2)) = Z/2` (Eq 36), `BU(1) = 0` (Eq 51), `BSU(n>2) = 0` (Eq 57); the `Z_4`/16-fermions statement; the baryon-triality `Z_9`/multiple-of-3 statement (noted, not used) |
| Wan, Wang, *Anomaly and Cobordism Constraints Beyond the Standard Model*, arXiv:2006.16996 | PDF fetched and text extracted; Eqs 5.6, 5.8, 5.9 and footnote 10 read verbatim | `Omega_5^{Spin x_{Z2} Z4} = Z_16` generated by `RP^5`; the Smith ladder to `Omega^{Pin+}_4 = Z_16` generated by `RP^4`; the `nu = -3 in Z_16` value for 3 generations of 15 Weyl fermions |
| Kirby-Taylor, CMH 65 (1990) | **not read directly**; taken from the repo's own primary-source-graded canon (`canon/ko-degree-obstruction-ladder-RESULTS.md`) | `Omega^{Pin+}_4 = Z/16` |
