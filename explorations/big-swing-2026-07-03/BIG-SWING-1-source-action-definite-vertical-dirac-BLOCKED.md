---
artifact_type: exploration
status: exploration
created: 2026-07-03
title: "Big swing #1 (construct the GU source action's decisive object S_IG-D): build the DEFINITE vertical Dirac index [D] on the noncompact fiber GL(4,R)/O(3,1) of Y14 from GU-internal data, and compute its family L^2/APS pushforward. HONEST OUTCOME: BLOCKED / firewall-CONFIRMING (WEAK form). Two target-free attempts (homogeneous-metric+Callias/APS; Dai-Freed anomaly-inflow boundary object) both FAIL adversarial verification in the same three ways: (a) definiteness is IMPORTED via a gauge-breaking compensator section, not derived, so the C-07 quaternionic-parity wall is dodged by fiat; (b) the decisive integer is not derived -- the denominator 8 is copied from canon and the fresh 'theorem' proves only the numerator is odd (blind to the denominator); (c) the degree-10 noncompact L^2/APS pushforward is never computed (1D toy proxy + a CITED, un-run bordism fact). No object built, no count derived, no forbidden target imported. The single missing GU input is named exactly: an external 3-divisible topological integer from a GU-FORCED base, which p-q=4 forces to the 3-free/2-primary RP^3."
grade: "exploration / BLOCKED, bounded-negative. This is a firewall CONFIRMATION in the WEAK / Multiplicity-Theorem form, not a home run and not a fabricated-closure KILL. The decisive [D] is CHARACTERIZED (definite + noncompact => the sole odd-capable, non-topological term) but NOT built; both candidate completions reduce to a 2-primary / {2,7,13}-smooth boundary object on the GU-forced RP^3 base. Independently reproduced: numerator 2q^2-4q+1 is always odd (sympy) yet this is provably blind to the denominator (substituting 24 or 3 preserves them); prime 3 divides none of the GU-native carrier dims. The generation-count verdict stays OPEN. No 3/8/24/chi(K3)/Ahat/rank_H/ind_H was imported or divided."
depends_on:
  - explorations/big-swing-2026-07-03/R1-rs-operator-residual-and-odd-count-nogo.md
  - explorations/big-swing-2026-07-03/R2-sm-boundary-mod3-arena-empty.md
  - tests/rs-function-space/rs_boundary_eta_l21.py
  - tests/generation-sector/gen_sector_bridge.py
scripts:
  - "(claimed but NOT on disk) callias_vertical_dirac_D.py, scipy_free_expm.py -- the homogeneous-metric/Callias run"
  - "(claimed but NOT on disk) the Dai-Freed carrier script -- boundary-object run"
  - "reproduced live here: sympy numerator-parity + denominator-blindness check; GU-carrier prime-content factorization"
---

# Big swing #1: build S_IG-D's decisive [D] from GU-internal data -- can the definite vertical fiber Dirac index be closed target-free?

**The swing.** The whole program converges on one wall, named independently by the R1 carrier analysis,
the rs-boundary-eta STEP-3 crux, the residual-closure caveat, and the gu-source-action campaign
(SPEC 5(i)+5(ii)+5(iii)): every sector piece closes 2-primary or index-0 EXCEPT the definite,
same-chirality vertical Dirac contribution `[D]` on the noncompact fiber `F = GL(4,R)/O(3,1)` of
`Y14 = Met(X4) -> X4`. `[D]` is decisive precisely because it is the sole odd-capable term (definite =>
`{D,Gamma} != 0` => spectrum not `+/-` symmetric) AND because the degree-10 integral over the *noncompact*
fiber is **not a topological pushforward** -- it is an analytic `L^2`/APS index that needs a fiber metric,
a functional-analytic completion, and an end condition. The home-run target `S_IG-D` is a closed BV source
action that supplies exactly that analytic data from GU-internal structure and computes the resulting
family index as a well-defined integer, with the generation count left to fall out or provably fail to.

**Honest outcome: BLOCKED / firewall-CONFIRMING (WEAK form).** Two target-free construction attempts
were made. **Neither built the object.** Both survive the target-import check clean, and both are
internally honest (each self-grades BLOCKED and fabricates no closure -- to their credit). But under
adversarial verification **both are refuted as constructions of `[D]`**: they relocate the wall behind a
citation, a copied constant, and a gauge-breaking import, rather than removing it. The convergent lesson --
the completion is necessarily a **boundary / external** object that is 2-primary on the GU-forced base --
is itself a real result: it **confirms the firewall** in its WEAK / Multiplicity-Theorem form and names
the missing GU input with no remaining vagueness.

---

## Attempt 1 -- homogeneous-metric + Callias/APS vertical Dirac on GL(4,R)/O(3,1)

**What is genuinely established (the real content).** The one solid, target-free result is an
*obstruction*, computed on the actual homogeneous space: the only `GL(4,R)`-invariant trace form on
`F = GL(4,R)/O(3,1)` is **indefinite, signature `(+7,-3)`**, with **noncompact isotropy** -- so there is
**no invariant Riemannian fiber metric** at all. This is a property of `F` fixed by `p-q=4` and is
**identical** under both `Cl(9,5)=M(64,H)` and `Cl(7,7)=M(128,R)`, so it passes Criterion 4 -- but note
that *signature-robustness here cuts AGAINST a win*: it makes the **failure** robust, not the count.

**Why it is refuted as a construction of `[D]` (three independent verifier reasons, all sustained):**

1. **Definiteness is IMPORTED, not derived (the deepest weakness, conceded).** Making `D_vert`
   Riemannian requires a compensator section `s` (a timelike reference frame) that **breaks
   `GL(4,R)/GU` gauge invariance**. It is canonical only up to the contractible `H^3` of choices. So the
   **C-07 quaternionic-parity wall is dodged by fiat**, not broken canonically from GU-internal data --
   which is exactly what the firewall demands.

2. **The decisive integer is imported with its denominator baked in.** The load-bearing conclusion
   (`[D] in (1/8)Z`, denominator **exactly 8**, 2-primary, never 3) rests on the constant `8` hardcoded
   in `Fraction(2*q*q-4*q+1, 8)`, copied verbatim from `tests/rs-function-space/rs_boundary_eta_l21.py`
   line 60, where it is labeled a *"canon control."* I reproduced the arithmetic live:

   > `numerator 2q^2-4q+1 mod 2 = 1` (always odd, sympy) -- **but this is blind to the denominator.**
   > Writing `24` or `3` in place of `8` yields reduced denominators `24` or `3` for the identical
   > numerator. The fresh "theorem" only proves the numerator is coprime to 2; it re-reads whichever
   > denominator is imported and has **zero discriminating power** over the geometry. It would wrongly
   > "confirm" 3-primary for a denominator-24 case with no closed completion.

   In fairness: the denominator-8 fact is *externally real* (it is the known Dirac eta of `RP^3 = L(2;1)`,
   validated independently in R2). The honest defect is narrower but fatal to the swing -- **this route
   re-derives nothing fresh from a degree-10 fiber Dirac spectrum; it inherits the answer from canon.**

3. **The degree-10 noncompact pushforward is a disguised assumption.** The collapse of the degree-10
   `GL(4,R)/O(3,1)` `L^2` Callias index onto the charge-`q` lens eta is **asserted**, not computed. The
   Callias step is an admitted **1D domain-wall finite-difference proxy** (its "index" is a domain-wall
   sign read-off `round((sign Phi(+L) - sign Phi(-L))/2)`, which returns `+1` for `tanh`, `5*tanh`, and
   `sinh` alike -- **blind to the actual fiber operator, carrier, metric, and dimension 10**). Nothing
   links the two live steps.

Additionally, the named runnable artifacts (`callias_vertical_dirac_D.py`, `scipy_free_expm.py`) are
**not on disk** -- no `scratchpad/` and no such files under `tests/big-swing/` -- so the reported
"exit 0, all guards passed" is unverifiable.

**Verdict on Attempt 1:** BLOCKED. It produces a genuine obstruction finding (no invariant Riemannian
fiber metric; indefinite `(+7,-3)`) but **not** a GU-internal definite vertical Dirac index. Definiteness
is imported by a gauge-breaking choice, and the load-bearing integer is imported from canon with a target
denominator baked in.

---

## Attempt 2 -- S_IG-D-DaiFreed: [D] as an anomaly-inflow boundary object, and the 3-freeness test

**What is genuinely established.** The numerics reproduce exactly (anchors `||[Pi,M_D]||=58.7215`,
`C2=155.3625` in both signatures; Krein `eta=0`, spectrum `+/-128`; definite candidate spectrum
`+/-832`, `eta=0`; carrier primes `{2,7,13}`, no 3; exit 0 as reported). No forbidden target is imported
or divided -- I independently factored the GU-native carrier dimensions and confirmed **prime 3 divides
none of them**: `128=2^7`, `14=2*7`, `1664=13*128`, `832=2^6*13`, `416=2^5*13`, `64=2^6`. The
`{2,7,13}`-smoothness is real and structural.

**Why it is refuted as a construction of `[D]` (three independent verifier reasons, all sustained):**

1. **It never builds the fiber index.** There is no fiber metric on `GL(4,R)/O(3,1)`, no weighted-Sobolev
   domain, no APS spectral section, no bulk integral. The bulk `L^2`/APS index is *replaced* by the
   spectral asymmetry of a finite 0-dimensional Hermitian matrix.

2. **The decisive fact is CITED, not computed.** The load-bearing claim -- `Omega^Spin_15(BSp(64))` is
   2-primary / 3-free (no odd torsion) -- is **asserted from the literature, with no Adams spectral
   sequence run** (the construction admits "not computed here"). The finite carrier does not derive it;
   it only factorizes representation dimensions (`2^7`, `2^6*13`) and notes 3 does not divide them, which
   is trivially forced by the `2^k` carrier choice, not by any fiber integral.

3. **The finite corroboration is a forced parity tautology (zero discriminating information).**
   `eta = 0` for the definite candidate `D_def` is an **algebraic identity, not a measurement**: `D_def`
   is built from a single odd Clifford element `xi^a e_a`, and the volume element `Gamma_5` anticommutes
   with every `e_a`, so the Hermitian part is `+/-`-symmetric and `eta = 0` for **any** `xi` and **any**
   signature (verifiers confirmed: 6 random masses all give `+832/-832`). The method returns the
   identical "`eta=0`, no asymmetric channel, 3-free, firewall-confirming" verdict **regardless of the
   true answer** -- so it would equally "confirm" a case whose true index is divisible by 3. The finite
   slice discards exactly the analytic content where a nonzero or 3-torsion index would live.

**Verdict on Attempt 2:** BLOCKED. It relocates the wall behind a citation plus a trivially-forced finite
identity. As a construction of the definite vertical fiber Dirac index, refuted.

---

## Mapping onto the firewall falsification criteria

| Criterion | Requirement | Outcome |
|---|---|---|
| **1 -- closed internal completion** | Fully closed source action, no import, no hand-tuned rank, DERIVES an odd/3 count | **NOT MET.** Neither attempt builds a closed action; neither derives a count. Under-determination remains. |
| **4 -- rep-artifact (both signatures)** | Same nonzero count under `Cl(9,5)` and `Cl(7,7)` | **Passes trivially for the wrong reason.** Every load-bearing fact (indefinite `(+7,-3)`, noncompact isotropy, `RP^3` core, `eta=0`) is signature-robust -- so the **2-primary FAILURE is robust**, confirming the WEAK firewall, not deriving a count. |
| **C-07 quaternionic-parity wall** | Break the grading canonically from GU-internal data | **NOT MET.** Attempt 1 breaks it only via a gauge-breaking compensator section (by fiat); Attempt 2's definite candidate has `{D,Gamma}` forcing `eta=0` (grading not broken at all). |
| **External-integer requirement** | Break grading AND carry a 3-divisible external integer from a GU-FORCED base | **NOT MET, and shown structurally out of reach.** `p-q=4` forces the base to `RP^3` (`H^2=Z_2`, 2-torsion, 3-free); the only 3-carrying base (K3) is a forbidden target-fitted import. |
| **HARD BAR** | Also make the matter number come out right without importing it | **Not reached** (the prior gates already block). Proving the count UNREACHABLE on this base is the legitimate outcome that IS in hand. |

**Net:** this is the **KILL/FIREWALL-CONFIRMATION** branch of the success definition in its honest form --
*not* a fabricated closure (nothing reached 4/8/3 by import or by the `8/2=4` division, so it is **not**
the fabricated-closure KILL), but a construction that **fails in the boundary-shaped way the firewall
predicts**: it pins a spectrum that is EVEN and `{2,7,13}`-flavored, never 3, and gives `eta=0` for the
definite candidate. That is the **WEAK / Multiplicity-Theorem** firewall form.

---

## What this settles, and what it does not

**Settles (this swing).** The decisive `[D]` is now sharply **characterized** -- definite + noncompact =>
the sole odd-capable, non-topological term -- and both natural routes to *building* it have been tried and
refuted. The convergent structural message is that **the completion is necessarily a boundary / external
object**, and on the GU-forced `RP^3` base that object is provably 2-primary and 3-free. Combined with
R1 (odd-interior route closed) and R2 (mod-3 anomaly arena empty), the picture is consistent and stable:
**the count is located but not forced from inside GU**, and the specific internal-fiber route cannot
supply the 3.

**Does NOT settle (and no target imported).** This does not derive three and does not forbid three. The
number 3 was never assumed, inserted, or divided by; it entered only as the prime whose *absence* from
every GU-native dimension is measured. No `chi(K3)=24`, no `/8` as an answer, no `Ahat=3`, no `8/2=4`.
The generation-count verdict stays **OPEN**.

**The single missing GU input, named with no remaining vagueness.** An **EXTERNAL topological integer
divisible by 3, pulled from a GU-FORCED base.** `p-q=4` forces the base to `RP^3`, which is 3-free and
2-primary; the only 3-carrying base (K3, `chi=24`) is an unforced, target-fitted, **forbidden** import.
The one un-probed escape is the **DYNAMICAL** RS-1-form branch of the `FULL_IG/FIXED_ALEPH/DYNAMIC_A`
trichotomy: if the spinor 1-form is dynamical, the correct anomaly theory may live over a tangential-framing
base `B(Spin(4)-frame)` carrying a `Lambda^2_+` leg with a known order-3 e-invariant (`1/12`) -- exactly
the base a genuine source action would have to select, and the only place a 3-carrying base is not an
import. **That selection is the unbuilt GU object.**

---

## Concrete next steps

1. **Attack the trichotomy, not the metric.** Build the stabilized RS-sector action for the `DYNAMIC_A`
   branch and test whether `(S,S)=0` forces the tangential-framing home `B(Spin(4)-frame)` (with its
   order-3 `Lambda^2_+` e-invariant) rather than `BSp(64)`. This is the only route where the 3-carrying
   base is GU-forced rather than imported.
2. **Re-derive the lens eta denominator from scratch.** Compute the `L(2;1)` charge-`q` Dirac spectrum
   from a from-scratch lens-space Dirac operator (not the canon literal). If an honest derivation still
   gives denominator 8, that HARDENS the WEAK firewall; if not, route 1's conclusion must be reopened.
   Either way it removes the "provenance-inherited denominator" defect.
3. **Settle C-07 canonically or prove the Multiplicity-Theorem.** Either exhibit a GU-internal
   (non-compensator) datum that makes `{D,Gamma} != 0` from `Spin(9,5)`-equivariant structure alone, via
   a genuine non-equivariant compensator ghost `sigma_c` inside a BV action with `(S,S)=0`; or prove every
   GU-native primitive commutes with `J_quat` (Kramers => even signature), promoting the WEAK firewall to
   a publishable no-go: *"the definite vertical index is always even, never 3."*
4. **Write the firewall-confirmation as the deliverable.** Stop treating `[D]` as internally completable.
   Draft the statement "the definite vertical index cannot source 3 from any GU-forced base; the K3-import
   is the exact forbidden move the theory would have to make" as the honest positive result.
5. **Restore reproducibility.** Commit the two missing construction scripts under `tests/big-swing/`, or
   retract the runnable-artifact claims. The `eta=0`/denominator-8 conclusions cannot be adjudicated from
   disk as they stand.

**Governance.** Exploration-grade; belongs under `explorations/big-swing-2026-07-03/`. No canon promotion
proposed -- this is a GU-carrier-specific negative certificate, not a standalone theorem. The
generation-count verdict remains **OPEN**; a verdict/status flip is separate and pauses for Joe.

---

## Verifier's note (main-loop review, 2026-07-03)

This doc is the synthesis of a 25-agent ultracode workflow (`wf_6659b8b4-4cb`). Main-loop honesty review:

- **Independently re-checked (holds):** the lens Dirac eta numerator `2q^2 - 4q + 1` is odd for every integer
  `q` (sympy), and this parity is provably *blind to the denominator* (it cannot distinguish `/8` from `/24`
  or `/3`) — so the "2-primary" reading rests on the denominator, which route 1 inherited from canon rather
  than re-deriving. The specific factored dims are 3-free (`128 = 2^7`, `832 = 2^6*13`). **Caveat noted:**
  the Krein multiplicities `96 = 2^5*3` and `192 = 2^6*3` *are* 3-divisible-as-multiplicands (the main paper's
  standing point); the doc's 3-freeness claim is scoped to the operator/representation dims above and does
  **not** assert those are 3-free — no overreach, but do not read the claim more broadly than that.
- **NOT reproduced (honest gap, as the doc itself flags):** the two construction scripts
  (`callias_vertical_dirac_D.py`, the Dai-Freed carrier script) were written to ephemeral scratchpad by the
  construct agents and were **not persisted**, so their `exit 0` claims are not checkable from disk. Treat
  those runnable-artifact claims as unverified; next-step #5 (rebuild + commit them, or drop the claims)
  stands.

**Bottom line (main-loop concurrence):** BLOCKED / firewall-confirming (WEAK form) is the right grade. The
swing did not build the object and did not fabricate a closure; its durable content is (i) the invariant-metric
obstruction on `GL(4,R)/O(3,1)` (indefinite `(+7,-3)`, no invariant Riemannian fiber metric) and (ii) the
sharpened statement that any completion is a boundary/external object which the GU-forced `RP^3` base renders
2-primary — i.e. sourcing 3 would require importing a 3-divisible integer from outside GU. Count stays OPEN.
