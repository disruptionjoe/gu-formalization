---
title: "Prepublish Review Tracker -- Multiplicity Theorem note"
status: active
doc_type: review_tracker
target_paper: papers/multiplicity-theorem-note-2026-06-28.md
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

## CRITICAL -- correctness / logic (block any publication)

### C1 -- The 1664 non-sequitur (the load-bearing logical gap) [R2; severity CRITICAL; status OPEN]
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

### H1 -- The self-dual / odd-vector family-index KILL (decisive) [R1+R2; severity HIGH; status OPEN]
The matter sector is `V (x) S`; the VECTOR index `V` (the 14) carries the family branching. Under
`SO(14) ⊃ SO(10) x SU(2)+` (self-dual), the rank-3 `Lambda^2_+(X^4)` / `su(2)+` adjoint is intrinsic 4d
geometry and rides on an ODD number. **The uncomputed decisive test:** the gamma-traceless branching of
`V (x) S` under `SO(10) x SU(2)+`, tracking whether a clean factor of 3 (or 6) SURVIVES the `Gamma`
projection in the generation multiplicity, or reshuffles into 2s and 4s. If a robust forced 3 survives ->
**KILLS-PAPER (and is a major positive result: GU forces 3).** If it reshuffles away -> the sharp form is
substantially STRENGTHENED. Note: distinct from our CONSTRUCT-05, which tested the self-dual connection
INDEX (=0), not the self-dual SU(2)+ as a FAMILY symmetry giving a branching multiplicity. RUN FIRST.

### H2 -- The Lorentzian-complexification tension (sharpest internal tension) [R2(d); severity HIGH; status OPEN]
In a Lorentzian 4-base, `*^2 = -1` on 2-forms, so `Lambda^2_+` is naturally COMPLEX rank 3 (the `sl(2,C)`
Weyl structure) -- a rank-3 object that appears PRECISELY upon complexification. We claim "the required
complexification = Nguyen's prime-3 import." But if that complexification is the self-dual Weyl structure
of GU's OWN base, the 3 is arguably GU-FORCED, not imported -- which would FLIP "positive reading refuted"
toward "Nguyen's 3 is native," and shift the firewall verdict. **We cannot claim the complexification-3 is
both (i) Nguyen's and (ii) an unforced external import if it is intrinsic to a Lorentzian 4-manifold.**
Resolve explicitly. Coupled to H1.

### H3 -- Non-regular / principal su(2) embeddings (close leg 3) [R1+R2; severity HIGH; status OPEN]
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

## Work plan (priority order)

1. **H1 -- run the kill** (`V (x) S` under `SO(10) x SU(2)+`, does a forced 3 survive `Gamma`?). Decides
   whether the paper survives. Do first.
2. **H2 -- resolve the Lorentzian-complexification tension** (is `Lambda^2_+` rank-3 GU-forced?). Coupled to H1;
   bears directly on the firewall verdict and the Nguyen tie-in.
3. **C1-C5 -- correctness fixes** (separate proven/searched; "3-free" wording; narrow the smoothness claim;
   pin real/complex; fix `M(64,H)`). Apply regardless of H1/H2 outcome.
4. **H3 -- enumerate nilpotent orbits** to close leg 3 (finite, cheap, rigorous).
5. **M1-M3 -- reframe** as a relative multiplicity-functor theorem + the spinor 2-smoothness lemma + the
   families-index theorem statement (or label conjectural).
6. **F1-F5 -- framing**; then decide GU-note vs extracted math.RT note.

Outcome rule: if H1 lands a forced 3, this becomes a positive result (GU forces 3) and the firewall weak
form is itself refuted -- record loudly. If H1 reshuffles away, the sharp form strengthens and we proceed
to the reframe-and-prove track.
