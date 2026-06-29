# Deep-research adversarial-hardening prompt (use alongside the uploaded paper PDF)

Paste the text below into a deep-research / web-enabled model together with the paper
(`located-not-forced-generation-count-2026-06-29.pdf`). It is tuned to this paper's actual risk surface.

---

You are a hostile, meticulous referee **and** a research-integrity auditor for the attached mathematical-physics
paper, "Located, Not Forced," which is about to be posted publicly (arXiv: hep-th primary; math-ph, math.AT
secondary). Your job is to find **every** weakness, error, overclaim, unsupported assertion, and integrity
problem before it goes public. Do **not** praise, summarize approvingly, or soften. Assume the most skeptical
expert reader possible -- including a researcher whose own prior work the paper cites (e.g. Juven Wang). **Use
web search to verify every checkable claim**, and cite the URL for each verification.

**Context you need (and the standard to hold it to).**
- The paper studies the generation-count / chirality structure of a Clifford Rarita--Schwinger sector
  reconstructed from Eric Weinstein's Geometric Unity (GU). It explicitly does **not** claim three generations;
  its thesis is "located, not forced."
- Its entire value proposition is **honesty and grading discipline** (theorem-grade vs computed vs
  reconstruction-grade vs gated vs open). Hold it ruthlessly to that standard: any claim graded above its
  support, any GU-specific step not clearly marked, any "computed fact" dressed as a "theorem," is a defect.
- The theorem-grade, GU-independent core it rests on: (1) a two-primary meta-theorem (no obstruction is an
  odd-prime congruence); (2) a CRT two-arena structure `pi_3^s = Z/24 = Z/8 (+) Z/3`; (3) an index-conservation
  theorem (linear Krein isometries form `U(96,96)`, which is connected, so the net chiral index is constant);
  (4) a class-level structural no-go (no covariant operator forces an odd chiral count -- the antilinear leg is
  a finite adversarial hunt, **not** a closed proof); (5) a located order-3 carrier (`e_R = p_1/48 = 1/12`).

**Attack these, hard. Do not limit yourself to this list -- find new problems too.**

**A. Mathematical correctness of the theorem-grade core.** Re-derive each theorem independently. Are they
actually theorems, or computed-on-a-substrate facts presented as theorems? Specifically: is the
`U(96,96)`-connectedness argument for index conservation valid and complete? Is the CRT two-arena structure
more than a restatement of `gcd(8,3)=1`? Is the structural no-go's antilinear leg honestly hedged as a finite
hunt rather than a proof, and is that hedge consistently maintained everywhere (abstract, contributions,
Section 5, status table, conclusion)? Verify the keystone `e_R = p_1/48 = (p_1/2)/24 = 1/12`: does `p_1/2`
generate `H^4(BSpin; Z)` (so the generator of `pi_3(Spin)` has `p_1 = 2`)? Is `p_1 = 4` correctly the adjoint
charge-1 Dynkin index? Is the class genuinely order-3 in its 3-primary part (note the element 2 in `Z/24` has
order 12)? Is the attribution correct (Kirby--Melvin for the framing/Pontryagin normalization, Adams for the
`e`-invariant arithmetic, the relation `e=p_1/48` stated as the authors' own composite, not quoted)? Check
`Hom(Z/3, Z) = 0` and the relative/equivariant/rank-invariant claim.

**B. Fabrication and citation integrity.** For **every** reference: confirm it exists (find the arXiv ID / DOI),
that authors/date/title are correct, and that the paper's characterization of what it shows is accurate. Flag
any hallucinated arXiv ID, misattribution, mischaracterized result, truncated/altered title, or self-published
source dressed as peer-reviewed. Pay special attention to: the future-dated Wan--Wang--Yau (arXiv:2605.26202);
the self-published Nguyen--Polya "A Response to Geometric Unity" and the Weinstein GU draft (verify the correct
citable form and URL); and whether Wang 2023 (arXiv:2312.14928) -- including its full title containing
`24/8 = 3` -- is accurately and fully represented.

**C. Novelty / prior art.** The paper concedes no novelty for the `Z/24 = Z/8 (+) Z/3` factorization or the use
of `pi_3^s = Z/24` (both Wang's), and claims novelty **only** for: (a) the inverse "disjointness-implies-
blindness" reading -- a 2-primary no-go is arithmetically blind to a 3-primary count, so the count is located
but not forced (Wang *forces* `N_gen in 3Z`; this paper shows a no-go *cannot* force it); (b) the Clifford
Rarita--Schwinger generation embedding; and (c) the Krein / `U(96,96)` index-conservation theorem. Search hard
for prior work that anticipates **any** of these three. Is even the narrowed claim defensible, or is something
still overclaimed? Name the closest precedents and say precisely how (or whether) the paper differs.

**D. Physics and reconstruction.** Is the Clifford-RS / GU reconstruction representation-theoretically and
physically sound? Check the `4+10` split, the `16` of `Spin(10)`, the Pati--Salam `Spin(7,7)` chain, the
Alvarez-Gaum\'e--Witten gravitino-anomaly use, the `K3` reductions, and the anomaly-inflow claims. Are the
GU-specific identifications honestly flagged reconstruction-grade? Is the characterization of GU (the "2+1"
hedge, "effective chirality," the unbuilt matter action) fair to the source, or a strawman?

**E. Load-bearing assumptions.** The "located, not forced" framing presupposes the *torsion-count reading*
(that a count lives as a 3-primary boundary `e`-invariant in `Z/3`), as opposed to a literal *integer-index
reading*, under which the same obstructions would *forbid* an odd count outright. Is this contingency stated
clearly and early enough? Are there other hidden assumptions on which the headline depends?

**F. Internal consistency.** Abstract vs body; the status-of-claims table vs the text; any contradiction; any
place a claim is stronger in one section than the evidence offered in another.

**G. Presentation and submission-readiness.** Is the "does NOT claim three generations" disclaimer and the
motivated-vs-independent distinction unmistakable up front? Any LaTeX issue you can see? Anything that would
draw an arXiv moderation flag, or hand a hostile expert an easy public rebuttal?

**Output.**
1. **Overall verdict**: safe to post publicly as-is, or after what level of fixes? (publishable-as-is /
   minor-fixes / substantive-fixes / not-yet).
2. **Prioritized punch-list**: MUST-FIX (blocks public posting), SHOULD-FIX, NICE-TO-HAVE. For each: quote the
   offending text, state the problem, give the specific fix, and cite your source URL for any factual/literature
   claim.
3. **Fabrication-check section**: list every reference and mark it verified or flagged, with the URL.
4. **The single most damaging objection** a hostile expert could raise, and a judgment on whether the paper
   survives it.

Be specific; quote section/line; cite sources. If a claim cannot be verified, say so and recommend the
conservative fix (soften / caveat / drop). The goal: after addressing your report, the paper cannot be
embarrassed by any expert reader.

---

**Note for the human (Joe):** run this in a deep-research / web-enabled model with the PDF attached. If it
returns MUST-FIX items, bring them back and we apply them before posting -- same loop we have been running. The
paper's computed core (the `tests/` in the repo) is the ground truth for any disputed numeric claim.
