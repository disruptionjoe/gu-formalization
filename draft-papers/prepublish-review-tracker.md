---
title: "Prepublish Review Tracker -- Multiplicity Theorem note"
status: active
doc_type: review_tracker
target_paper: draft-papers/multiplicity-theorem-note-2026-06-28.md
created: 2026-06-28
---

# Prepublish Review Tracker

Living catalog of every critique of `multiplicity-theorem-note-2026-06-28.md` (and the underlying
Multiplicity Theorem, `canon/multiplicity-theorem.md`). Discipline: each item is to be RESOLVED, REFUTED,
or shown to KILL the result. We do not defend; we work each down to a verified outcome.

**Status legend:** OPEN (not started) | COMPUTING (kill/fix in progress) | RESOLVED (fixed/closed) |
KILLS-PAPER (a kill landed; the sharp form is dead) | WONTFIX (deliberately out of scope, with reason).

**Sources:** R1 = first adversarial reviewer; R2 = second adversarial reviewer (sharper; found the
load-bearing logical gap); SELF = our own honest-scope admissions.

---

## TOP-LINE FINDING (2026-06-28): the H1 kill LANDED -- the paper's sharp thesis is refuted

Running the reviewer's decisive kill (H1) **broke the central claim.** Verified, machine-checked:
the gamma-traceless RS module `ker(Gamma)` decomposes under the self-dual `SU(2)+` (the rank-3
`Lambda^2_+` of any 4-manifold, GU-forced geometry) as **640 singlets + 416 doublets + 64 TRIPLETS**;
the 64 triplets carry the PURE `Spin(10)` generation spinor (Casimir `-11.25 = 16/16bar` exactly).
So there IS a GU-native branching multiplicity equal to **3** -- the generation sits in an `SU(2)+`
triplet the gamma-trace cannot remove. **"count = 3 iff import the prime 3" and "3 divides no GU-native
branching multiplicity" are FALSE.** (C1 fully vindicated: the 2^7*13 total-dimension fact never
protected the multiplicity.)

But the triplet is **vectorlike in Euclidean (14,0)**: it splits 96/96 by `Spin(14)` chirality (net
chiral asymmetry 0 = 3 generations + 3 mirrors), so this is NOT yet "GU predicts 3 chiral generations."
Scripts: `h1_selfdual_family.py`, `h1b_verify.py`, `h1c_chiral.py`, `h1d_ghostparity.py`.

**Krein / ghost-parity synthesis (2026-06-28), reshapes H2.** The mirror is not a defect: GU's matter
module is a Krein space (indefinite `so(p,q)` metric), and the self-dual triplet is exactly neutral
(`+96/-96`) in every signature -- each generation is bound to its mirror in a hyperbolic (null) pair.
This is Turok-Bateman's ghost-parity setting: a `Z2` ghost parity resolves each pair into 1 physical
generation + 1 ghost. So the chiral selection that was "open (needs an index)" is now sharply specified:
it is a ghost-parity-preserving dynamics. This also yields the first candidate **inside-the-class**
Distler-Garibaldi evasion (a new positivity axis on the six-axis protocol). Full statement + the D-G /
six-axis connection: `canon/ghost-parity-krein-synthesis.md`; test: `tests/generation-sector/
ghost_parity_krein.py`.

**T1a -- kinematic chiralization KILL confirmed (2026-06-28).** The Krein form on the triplet is purely
CROSS-chirality (same-chirality blocks `||K(+,+)|| = ||K(-,-)|| ~ 1e-14`), so every maximal positive-norm
(physical) subspace is exactly 50/50 chirality and its net chirality is `0` (~1e-15), in both `(9,5)` and
`(7,7)`. No ghost parity chiralizes the triplet by KINEMATICS alone -- ghost parity is necessary
(physical-sector selection) but not sufficient (chiral selection). The chirality requires a
symmetry-breaking dynamics or a base-manifold Dirac index. The six-axis candidate's own predicted kill,
machine-confirmed; the central claim's honest boundary is pinned to exactly one open condition. Test:
`tests/generation-sector/t1a_kinematic_chirality_kill.py`.

**Ghost-parity / Kramers chiralization hypothesis -- TESTED and REFUTED (2026-06-28).** Conjecture: the
quaternionic Kramers parity (`J^2 = -1`, the Z2 we earlier dismissed as a "(9,5) artifact") is a
ghost-parity that controls whether the self-dual triplet is vectorlike (quaternionic class) or chiral
(real class). Test: recompute the triplet chirality holding the base `(4,0)` fixed (self-dual `SU(2)+`
identical) and flipping the internal signature to change the spinor-module class -- `(14,0),(10,4)` (QUAT)
vs `(8,6),(11,3),(7,7)` (REAL). RESULT: **net chiral asymmetry = 0 in ALL FIVE** -- the triplet is
robustly vectorlike (96/96) regardless of class. So no algebraic parity (Kramers, and by the
mirror/Nielsen-Ninomiya obstruction any global Z2 that respects gauge + 4d-chirality) can chiralize it.
**Consequence:** a net chiral 3 is an INDEX (analytic/topological), identically 0 at the rep-theory level;
it can only become nonzero through actual base-manifold topology (a Dirac index with instanton/curvature
data). This RELOCATES the open question precisely: the multiplicity-3 *structure* is GU-native (self-dual
triplet); the *chiral projection* that turns vectorlike 3+3bar into 3 net generations is a topological
index datum -- exactly the H2 Lorentzian-base / families-index frontier (and a refined, sharper firewall:
structure internal, chirality is the interface datum). NOTE: this tested the Kramers parity on a Euclidean
base; the genuine BV ghost parity (compensator `sigma_c`) and the Lorentzian base (`sl(2,C)` self-dual,
non-compact) are still untested -- but the obstruction predicts neither chiralizes without an index.

---

## CRITICAL -- correctness / logic (block any publication)

### C1 -- The 1664 non-sequitur (the load-bearing logical gap) [R2; severity CRITICAL; status VINDICATED by H1, 2026-06-28]
`ker(Gamma) = 13*128 = 1664 = 2^7*13` is a statement about a TOTAL MODULE DIMENSION. The theorem needs
3-freeness of a BRANCHING MULTIPLICITY (how many times the one-generation object appears in the
gamma-traceless RS module). **Total-dimension-3-freeness does NOT imply multiplicity-3-freeness.**
Counterexample-by-arithmetic: `1664 = 6*16 + 1568`, `1568 = 2^5*7^2` -- a sub-multiplicity of 3 (or 6)
generations is compatible with a 3-free total. So the rigorous-looking 1664 arithmetic proves the WRONG
proposition; multiplicity-3-freeness rests ENTIRELY on the finite `leg4_branching_multiplicity_search.py`
(evidence-grade). **Fix:** separate the PROVEN (total ker = 2^7*13, signature-universal) from the SEARCHED
(multiplicity 3-freeness); never let the former stand for the latter; demote the sharp "count=3 iff import
prime 3" to explicitly evidence-grade-pending-H1. This is the most important item.

### C2 -- "never an odd prime, in particular never 3" is FALSE [R2; severity CRITICAL; status OPEN]
7 and 13 ARE odd primes and they appear (1664 = 2^7*13; adjoint 91 = 7*13). The intended claim is
"never DIVISIBLE BY 3" / "3-free." Reword every occurrence.

### C3 -- "{2,7,13}-smooth across every GU-native object class" is self-refuting [R2; severity CRITICAL; status OPEN]
Our own `|Weyl(D7)| = 2^10*3^2*5*7` carries 3 and 5. The smoothness set is NOT closed over GU-native
numbers. True claim is the narrower "the ELIGIBLE counting invariants are 3-free." State it narrowly.

### C4 -- Real-vs-complex sloppiness on the load-bearing complexification [R1+R2; severity CRITICAL; status OPEN]
We write `Gamma` surjective onto "C^128" while calling the setup a real `Cl(p,q)`. Since the headline is
"the 3 enters via complexification (Nguyen)," casually complexifying the spinor module is exactly the move
we cannot make uncommented. **Fix:** pin down the module (real `M(128,R)` vs complex rep with real/
quaternionic structure), state precisely where complexification is invoked, and reconcile with the Nguyen
tie-in. Tied to H2.

### C5 -- `M(128,H)` is dimensionally off [R2; severity CRITICAL; status OPEN]
For `p-q = 4,6 mod 8` at `n=14` the algebra is `M(64,H)` on `H^64` (real dim 256, quaternionic dim 64),
NOT "M(128,H)". "128-dim" used uniformly hides a factor of 2. **Fix:** say which module carries the 1664 --
full Dirac `(n-1)*128`, or per-chirality `(n-1)*64 = 832 = 2^6*13` (also 3-free).

---

## HIGH -- open kill threats (must compute before claiming)

### H1 -- The self-dual / odd-vector family-index KILL (decisive) [R1+R2; severity HIGH; status KILLS-PAPER (sharp form), 2026-06-28]
The matter sector is `V (x) S`; the VECTOR index `V` (the 14) carries the family branching. Under
`SO(14) ⊃ SO(10) x SU(2)+` (self-dual), the rank-3 `Lambda^2_+(X^4)` / `su(2)+` adjoint is intrinsic 4d
geometry and rides on an ODD number. **RESULT (verified):** built the self-dual `SU(2)+` generators on
`V (x) S` (genuine su(2): `[J0,J1] = -2 J2`, residual 0; `[J, Pi_RS] = 0` exactly so they preserve
`ker(Gamma)`). `ker(Gamma) = 1664` decomposes as `640` singlets `+ 416` doublets `+ 64` TRIPLETS
(`640*1 + 416*2 + 64*3 = 1664`). The triplet sector (dim 192) carries the PURE `Spin(10)` generation
spinor: `Spin(10)` Casimir `= -11.25` on all 192 states, matching the reference `16/16bar` spinor value
exactly. **=> a GU-native branching multiplicity equal to 3 EXISTS; the sharp claim is dead.** Chirality
check (Euclidean `(14,0)`): the triplet sector is 96/96 by `Spin(14)` chirality, net asymmetry 0 ->
VECTORLIKE (3 generations + 3 mirrors), so not yet a net-chiral-3 prediction. The chiral question passes
to **H2**. Distinct from CONSTRUCT-05 (which tested the self-dual *connection index* = 0, not the self-dual
`SU(2)+` as a *family symmetry*). DONE; conclusion feeds H2.

### H2 -- The Lorentzian-complexification tension (sharpest internal tension) [R2(d); severity HIGH; status DONE 2026-06-28]
**RESOLVED** (workflow, 3-lens adversarially verified; it corrected the anchored reasoning). Headline holds:
the net chiral 3 is NOT GU-internally forced. Split: (multiplicity) the rank-3 self-dual object is honestly
native, including in Lorentzian `sl(2,C)` signature -- complexification STRENGTHENS H1, not a Euclidean
artifact. (count) every GU-native base-index route is EVEN: the real `su(2)+` adjoint gives `4k`, the full
16-dim multiplicity bundle gives `12k`/`12k`/`24k` (self-dual/anti-self-dual/diagonal), robust by a base-side
quaternionic-Kramers parity argument (J^2=-1 from real adjoint x quaternionic S_+, mirrors our internal C-07)
+ Rokhlin. Complexification cannot turn an even index odd (topology lives in the maximal compact SU(2); an
index is Euclidean/elliptic; reality type conserved). **Three anchor corrections:** the generation is a (3,2)
of su(2)+ x su(2)- (NOT "triplet not doublet"); the cheapest odd-3 route is a charge-1 anti-self-dual
instanton in the pseudoreal su(2)- doublet x native triplet-3, plus sub-sector truncation (NOT k=3); even-ness
is a property of the real/adjoint channel, scoped away from the pseudoreal doublet. Nguyen's complexification:
necessary (Z2 reality-breaking to define a chiral split) but INSUFFICIENT (yields even); the import is
relocated + shrunk to "a unit of flux," never "the prime 3." Full result: `canon/h2-base-index-chirality.md`.

### H3 -- Non-regular / principal su(2) embeddings (close leg 3) [R1+R2; severity HIGH; status DONE 2026-06-28]
**CLOSED** for the commutes-with-Spin(10) case. The commutant of Spin(10) in Spin(14) is so(4) = su(2)+ ⊕
su(2)-; its only su(2) subalgebras are self-dual, anti-self-dual, diagonal/vector; su(3) cannot embed
(dim 8 > 6). The 16-multiplicity space decomposes as: self-dual/anti-self-dual -> `2(j=0)+4(j=1/2)+2(j=1)`
(odd piece = TRIPLET 3); diagonal/vector -> `4(j=1/2)+2(j=3/2)` (all even). Odd multiplicity is ALWAYS the
triplet 3, never 5+, and there is no su(3). Self-dual SU(2)+ is the canonical, essentially unique odd
route. Residual: the commutes-with-G_SM-only case (larger commutant, possible horizontal su(3)) is a
bounded next computation. Also closes **M3**: the spinor 2-smoothness lemma is proved (spinor family
factors -> power-of-2 multiplicity -> 3-free; odd 3 only via the non-spinor self-dual Lambda^2_+). Canon:
`canon/leg3-closure-and-spinor-2smoothness.md`; test: `tests/generation-sector/leg3_family_embedding_enumeration.py`.

### H3-orig -- Non-regular / principal su(2) embeddings (original note) [superseded by the DONE entry above]
Our Leg-4 search covered only maximal-rank D5 splits. Non-regular/principal su(2) embeddings are in
bijection with nilpotent orbits, FINITELY classified (Bala-Carter / weighted Dynkin). **Bounded finite
computation:** enumerate nilpotent orbits in the family-symmetry / centralizer algebra; for each, check
whether the induced family rep on the matter module has a GU-forced 3-dim (spin-1) piece. If none ->
leg 3 upgrades to proof-grade; if one -> related to H1, possible kill. The cheapest leg to make rigorous.

---

## MEDIUM -- closure for a strong theorem

### M1 -- Leg 1 (completeness): convert to a relative theorem [R1+R2; severity MEDIUM; status OPEN]
Stop trying to prove open-ended completeness (unprovable; |W(D7)| shows 3s exist, merely ineligible).
Instead DEFINE the generation-counting invariant precisely -- multiplicity `= dim Hom_H(W_gen, Res_H M)`
for matter module `M`, SM-subgroup `H`, plus indices of a specified operator class -- and prove all such
are 3-free FOR THIS module and chain. This is provable and referee-proof, AND it gives the principled rule
that legitimately excludes `|W(D7)|` (an order, not a multiplicity-of-anything). Honest catch: pinning `H`
makes the theorem explicitly "relative to the Pati-Salam chain" (weaker, honest); a different admissible
`H` with SU(2)+ is exactly H1.

### M2 -- Leg 2 (connection index): families/spectral-flow index THEOREM, not sampling [R1+R2; severity MEDIUM; status OPEN]
The single `so(9,5)` certificate is a point evaluation; an index theorem is the integral. Close via either
(i) cohomological `ind = integral of Ahat(vertical) . ch(index bundle)` shown 3-free for all signatures by
curvature/Ahat argument, or (ii) a symmetry-vanishing (PHS/self-duality) theorem forcing the characteristic
form to integrate to 0. Until then this leg is evidence-grade. NOTE: a twisted Dirac with instanton number
3 is NOT covered by "metric so(p,q) connection index = 0," so even a perfect leg 2 does not shut down H1.

### M3 -- Isolate the spinor-factor 2-smoothness LEMMA (positive content) [R2(b); severity MEDIUM; status OPEN]
Clean lemma worth proving and foregrounding: a family/internal space entering as a SPINOR of an internal
`SO(2k)`/`SO(2k+1)` has dimension `2^(...)`, so its multiplicity is a power of 2, hence 3-free. Contrapositive
(the whole game): the ONLY route to an odd multiplicity is a NON-spinor (vector / adjoint / principal-su(2)
/ odd-vector) family index -- which is exactly H1. This converts "we searched spinor branchings" into
"we proved the spinor route is 2-smooth, and identified the only surviving route."

---

## FRAMING / PUBLISHABILITY

### F1 -- "reproduces exactly ONE generation" reads as a prediction [R2; status OPEN]
Lead with "structure fixed, count free," never "predicts one generation," to avoid the vindication we
disclaim.

### F2 -- Retire any phrasing where the 1664 arithmetic IMPLIES the multiplicity result [R1+R2; status OPEN]
Same wound as C1, at the rhetoric level. A referee who sees the non-sequitur distrusts the rest.

### F3 -- Decouple the two contributions; consider a standalone math.RT note [R2; status OPEN]
(1) The reconstruction-grade GU reading caps at commentary. (2) A GU-INDEPENDENT rep-theory core: the n=14
Clifford principal counting invariants are 3-free and WHY (rank-7 accident), plus the M3 lemma. Contribution
(2) survives a hostile referee. Candidate: "On the arithmetic of generation multiplicities in Cl(p,q)
Rarita-Schwinger sectors" (math.RT), GU as a motivating remark. The current note is a strong arXiv/blog
essay; the extracted core is journal-viable.

### F4 -- Decouple GU-dependent and GU-independent claims [R2; status OPEN]
So a referee can accept the rep theory without buying GU.

### F5 -- Spell out WHY the K3 import is unforced [R2; status OPEN]
Currently asserted. And H2 suggests a 3-carrying object (`Lambda^2_+`) may be FORCED by the base even if K3
is not -- so this needs an argument, not an assertion. (Keep the K3 candor: `ch2 = -5376 = -2^8*3*7` carries
a 3; `24/8 = 3` is target-fitting. Reviewers praised this as the most credible part.)

---

## Work plan (priority order) -- REVISED after H1 landed

1. ~~**H1 -- run the kill.**~~ DONE 2026-06-28: KILLS the sharp form. GU-native multiplicity-3 exists
   (self-dual `SU(2)+` triplet of the generation), vectorlike in Euclidean. Sharp thesis is dead.
2. **H2 -- THE decisive computation now.** Does the Lorentzian self-dual structure (`*^2 = -1`,
   `Lambda^2_+` complex rank 3, `sl(2,C)` Weyl = Nguyen's complexification) CHIRALIZE the triplet
   (net chiral count -> 3) or leave it vectorlike? Net-chiral-3 => GU natively forces 3 chiral generations
   (major positive). Vectorlike => GU carries a mirror-paired 3, count still not chirally fixed. This now
   decides the whole verdict. RUN NEXT.
3. **H3 -- nilpotent-orbit enumeration** (close leg 3 / map all odd-multiplicity family embeddings, now
   that one (self-dual `SU(2)+`) is known to give 3). Confirms whether `SU(2)+` is the unique odd-route.
4. **Rewrite = a clean-room FULL re-draft, NOT an edit (Joe, 2026-06-28).** Draft the paper anew from the
   verified canon kernel only (H1, T1a, H3, M3, the Krein/ghost-parity synthesis, H2-pending), so no
   residue of the old note's assumptions (the retired 1664-implies-multiplicity logic, the "import the
   prime 3" framing) leaks through. Both `multiplicity-theorem-note-2026-06-28.md` and
   `generation-sector-no-go-note-2026-06-27.md` get marked SUPERSEDED (banner), not edited. Run as a
   draft -> 3-lens adversarial-verify -> synthesize workflow producing the new note from the canon docs.
   New spine: structure fixed -> native multiplicity-3 (H1) -> vectorlike, kinematically un-chiralizable
   (T1a) -> the chiral count is one missing ingredient (dynamics or base index, per H2) -> Krein /
   ghost-parity / Turok + the D-G positivity-axis candidate. Fold C1-C5 + M1-M3 + F1-F5 in by construction.
   Do NOT start before H2 lands -- the headline depends on H2's outcome.
5. **C1-C5 / M1-M3 / F1-F5** -- apply during the rewrite (C1 already vindicated; the rest still stand as
   precision/framing fixes).

Outcome rule (updated): H1 landed the kill. The remaining fork is entirely H2: chiral 3 (GU predicts three
generations, modulo the complexification) vs vectorlike 3 (native multiplicity present but not chiral).
Either way the OLD sharp "import the prime 3" framing is retired.
