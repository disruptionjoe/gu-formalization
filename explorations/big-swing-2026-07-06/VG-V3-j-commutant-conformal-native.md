---
artifact_type: exploration
status: exploration
created: 2026-07-06
title: "Big swing VG-V3 (T1' executable form): is the conformal chain GU-NATIVE (canonical J) or merely GU-compatible (family)? ANSWER: NEITHER — the commutant scan returns EMPTY, which is STRONGER than the pre-registered family-downgrade. The 10-dim metric fiber Sym^2(R^4) with eta = diag(-1,1,1,1) has Frobenius signature (7,3) and trace-reversed signature (6,4) (transcript 00:43:47 independently re-derived, printed as the route anchor); the even-parity theorem (orthogonal J on R^(p,q) iff p AND q even) is now PROVED + constructively verified, clearing its from-memory flag — (6,4) admits J (residuals ~1e-15, Hermitian signature (3,2)), (7,3) is obstructed (40-start falsification floor 4.000). But NO orthogonal J commutes with GU's own fiber data: unconstrained J's form a 20-dim family, and EACH named datum ALONE empties it — the trace/scale direction (exact parity proof, floor 5.200 >= 2), the SO(3,1) isotropy (commutant = span{P9,P1}, exact floor 10, measured 29.000), the SU(2)+ family action via its SO(3) real image (odd isotypics 3 and 5 force real scalars, floor 28.337 >= 8; the leftover 2-dim trivial isotypic has G-signature (1,1), obstructed by the theorem itself). HONEST OUTCOME: T1' reports NEGATIVE on the EMPTY branch — 'conformal is GU-native' is refuted at the fiber level; any J that builds u(3,2) -> su(2,2) ~ so(4,2) (chain verified at matrix level: dims 25/17/15, rank 3, Killing (8,7)) must BREAK GU's trace split and isotropy to exist."
grade: "exploration / (a) THEOREM (proved both directions + constructive J on (6,4) + 40-start numerical falsification on (7,3) with (6,4) success control); (b) THEOREM for each EMPTY verdict (exact Schur/parity/determinant proofs, scans are corroboration with two positive controls showing the optimizer finds J when J exists); (c) chain verified at matrix level (dimension/rank/Killing-signature invariants; not a constructed isomorphism map); (d) verdict NEGATIVE per pre-registered rule, EMPTY branch. Target-import guard at maximum strictness: {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} never assumed, inserted, or divided by; the 3 in u(3,2) is MEASURED (Hermitian signature of the measured (6,4)); no count statement of any kind is made. Route anchor (the (6,4) fiber signature) reproduced and printed first; the 1792-dim carrier anchors are NOT used because this route lives entirely on the 10-dim fiber (stated in-script)."
depends_on:
  - explorations/persona-and-dialectic/all-persona-tri-theory-combination-steelman-hegelian-2026-07-06.md
  - explorations/big-swing-2026-07-06/SYNTHESIS-CONJECTURE-tri-theory-2026-07-06.md
  - canon/ghost-parity-krein-synthesis.md
  - canon/swing-ghost-parity-no-chiral-selection.md
  - canon/h2-base-index-chirality.md
scripts:
  - tests/big-swing/vg_v3_j_commutant_conformal_native.py
---

# VG-V3: T1' executable form — is the conformal chain GU-native (canonical J) or merely GU-compatible (family)?

**The leg (revised statement, Section 5.3 of the persona doc):** T1' — conformal-native check,
executable form. Theorem-verify the p,q-both-even criterion (from-memory flag cleared by proof);
scan for orthogonal J's commuting with GU's own fiber data; report EMPTY / CANONICAL /
FAMILY. Pre-registered downgrade rule accepted from Panel A: if the commutant is a family,
"conformal is GU-native" degrades to "GU-compatible" and T1' reports negative; if EMPTY, the
conformal attachment is dead at the fiber level.

**Answer in one line:** the scan returns **EMPTY** — not canonical, not even a family. There is no
orthogonal complex structure on the 10-dim metric fiber compatible with GU's own trace split,
SO(3,1) isotropy, or the real image of the SU(2)+ action; each named datum **alone** already
kills it, by exact proof. T1' reports **NEGATIVE**, on the branch stronger than the downgrade rule
anticipated.

All numbers below are printed by `tests/big-swing/vg_v3_j_commutant_conformal_native.py`
(run `python tests/big-swing/vg_v3_j_commutant_conformal_native.py` from repo root; exit 0,
all checks pass).

---

## 0. Arena and anchor (Section 0 of the script)

The fiber is V10 = Sym^2(R^4)\* — symmetric 2-tensors h_{mu nu} over the Lorentzian base with
eta = diag(-1,1,1,1) — carrying two O(3,1)-invariant metrics:

- the Frobenius form **B(h,k) = tr(eta h eta k)**, measured signature **(7,3)**;
- the trace-REVERSED metric **G(h,k) = B(h,k) − (1/2) tr_eta(h) tr_eta(k)**, measured signature
  **(6,4)** — **this is the route's anchor**, and it independently re-derives the transcript's
  (7,3) → (6,4) claim at [00:43:47].

Measured mechanism of the flip: the trace-reversal operator T: h → h − (1/2) eta tr_eta(h) has
eigenvalues (−1 ×1, +1 ×9); the flipped direction is exactly the trace line h = eta, where
B(eta,eta) = +4.000000 and G(eta,eta) = −4.000000. Both forms are so(3,1)-invariant (residuals
0.0e+00). Assembly remark (measured consistency, not import): base (3,1) + fiber (6,4) = **(9,5)**,
matching the repo's Cl(9,5) carrier convention.

**Carrier anchors not used:** the triplet (+96,−96,0), beta_S residual, and rank(Gamma)=128 live on
the 1792-dim carrier; this route never touches it. The script states this explicitly and prints the
(6,4) anchor the route assignment designates instead.

## 1. Section A — the even-parity theorem (from-memory flag CLEARED)

**Theorem.** An orthogonal complex structure J (J² = −I, Jᵀ g J = g) on R^{p,q} exists **iff p and
q are both even**.

**Proof, existence (⇐):** in a pseudo-orthonormal basis, place the 2×2 block j₂ = [[0,−1],[1,0]] in
each of the p/2 positive 2-planes and each of the q/2 negative 2-planes. Verified constructively on
(6,4): the exhibited J0 has ‖J0² + I‖ = 4.18e−16 and ‖J0ᵀ G J0 − G‖ = 1.23e−15.

**Proof, obstruction (⇒):** given such a J, (R^{p+q}, J) is a complex vector space of complex
dimension (p+q)/2, and H(x,y) = g(x,y) + i g(Jx,y) is a Hermitian sesquilinear form on it
(Hermiticity uses exactly Jᵀ g J = g and J² = −I; verified at matrix level, residual 6.0e−16). Its
real part is g. A Hermitian form of complex signature (r,s) has real part of signature (2r,2s).
Hence p = 2r and q = 2s are **both even**. (Auxiliary parity fact used later for odd-dimensional
blocks: on an odd-dim invariant block, det(J²) = det(−I) = −1 but det(J)² ≥ 0 — impossible.)

**Numerical falsification scan** (the check that could fail): minimize
‖J²+I‖²_F + ‖Jᵀ g J − g‖²_F over all of gl(10) with L-BFGS-B (analytic gradient verified against
finite differences):

| signature | starts | min residual | reading |
|---|---|---|---|
| (7,3) | 40 | **4.000e+00** | floor bounded away from 0 — obstructed, as the theorem demands |
| (6,4) CONTROL | 10 | **7.750e−19** | the same scan reaches ~0 when J exists — scan is not theater |

Measured on both the constructed J0 and the independently optimizer-found J on (6,4): the Hermitian
form has signature **(3,2)** (residual 1.1e−09 on the optimizer J) — 2r = p forced, doubling back to
the real (6,4). The 3 here is a **measured** signature count, not an import.

## 2. Section B — the commutant scan (the route's core)

Question: which orthogonal J's commute with GU's **own** named fiber data? Cumulative scan, with
each verdict backed by an exact argument and corroborated by the constrained optimizer:

| step | datum added | commutant dim | verdict | evidence |
|---|---|---|---|---|
| 0 | none | — (tangent dim at J0) | **FAMILY, dim 20** | linearization nullity 20 = dim O(6,4) − dim U(3,2) = 45 − 25 |
| 1 | trace/scale direction (projector P1 onto span(eta)) | 82 = 1² + 9² | **EMPTY** | exact: J preserves the 1-dim trace line, J there is a real scalar c with c² = −1 (impossible); the 9-dim complement is odd-dim (determinant parity). Scan floor 5.200 ≥ predicted 2 |
| 2 | base-vs-vertical split | — | **N/A** | the 4+10 split lives on T(Y14); V10 here IS the vertical summand. Recorded via the (3,1)+(6,4)=(9,5) assembly print |
| 3 | SO(3,1) isotropy (from GL(4,R)/O(3,1)) | **2** | **EMPTY** | commutant = span{P9, P1} exactly (elements verified in span, residuals ≤ 7.5e−16): V10 = 9 ⊕ 1, both real-type, multiplicity-free. J = aP9 + bP1 gives exact J²-floor 9(a²+1)² + (b²+1)² ≥ 10 (grid-verified min 10.000000 at a=b=0); measured joint floor 29.000 |
| 4 | SU(2)+ family action, where it acts on the REAL fiber | 6 (standalone) | **EMPTY** | Lorentzian Hodge-\* on Λ² squares to **−I** (verified; Euclidean control +I), so the SD/ASD split is complex and SU(2)+ acts on real V10 only through its SO(3) rotation image. V10 = 1+1+3+5 under SO(3); the multiplicity-one odd irreps (3 and 5, real type) force J to real scalars there (c² = −1 impossible, floor ≥ 8; measured 28.337); the 2-dim trivial isotypic has G-signature **(1,1)** — both odd, obstructed by the Section-A theorem itself |

Cumulative: adding P1 to step 3 leaves the commutant dim at 2; adding the rotations (step 4) to
steps 1+3 leaves it at 2 (rotations lie inside so(3,1)). **No cumulative step ever returns
CANONICAL; every named datum standalone already returns EMPTY.**

**Controls (the empties are not optimizer theater):**

- rank-2 G-definite projector (complement signature (4,4)): the same constrained scan **finds** J,
  residual 3.971e−19;
- the so(2) generated by J0 itself: scan finds an orthogonal J in its commutant, residual 1.082e−19;
- (7,3)-vs-(6,4) in Section A; Euclidean-vs-Lorentzian Hodge-\* in step 4.

**Exact side-remark (closes a neighboring escape route):** commutant dim 2 certifies that the only
so(3,1)-invariant subspaces of V10 are 0, the trace line, the 9-dim traceless part, and V10. So
there is **no invariant 6-dim subspace at all** — a direct so(4,2) ⊕ so(2,2) vector-split of the
(6,4) fiber is equally non-canonical. The conformal attachment cannot dodge the J-question by
splitting instead.

## 3. Section C — the chain (informational: it hangs off a J the fiber data refuses)

Since the scan returned EMPTY rather than CANONICAL, route part (c) is contingent; it was computed
anyway at matrix level for the record, using the (non-invariant) J0:

- centralizer of J0 in so(6,4): dim **25** = dim u(3,2), with Hermitian signature (3,2) measured in
  Section A; dim so(6,4) = 45 (consistency check passed);
- stabilizer of a G-positive complex line inside u(3,2): dim **17** = 1 + 16 = dim(u(1) ⊕ u(2,2));
- su(2,2) vs so(4,2), both built as explicit nullspace bases: dim **15 = 15**, rank (generic
  centralizer dimension) **3 = 3**, Killing signature **(8,7) = (8,7)**. The exceptional
  isomorphism checks at the invariant level (this is invariant-matching evidence, not a constructed
  isomorphism map; the abstract iso su(2,2) ≅ so(4,2) is standard — from memory — and the matrix
  invariants confirm it here).

So the algebra chain so(6,4) ⊃ u(3,2) ⊃ u(1)+u(2,2) → su(2,2) ~ so(4,2) is real mathematics — but
every J that generates it **breaks GU's own trace split and isotropy** to exist.

## 4. Section D — verdict (pre-registered downgrade rule)

- **(a)** THEOREM: even-parity criterion proved both directions, constructively on (6,4), obstructed
  on (7,3) with a 40-start falsification floor of 4.000. From-memory flag **cleared**.
- **(b)** The commutant scan never returns CANONICAL. Unconstrained J's are a 20-dim family; GU's
  FIRST named fiber datum already empties it, and so does each other named datum standalone.
  **There is no GU-native J: not canonical, not even a family.**
- **(c)** The u(3,2) → su(2,2) ~ so(4,2) chain is verified at matrix level, but is unanchored to GU.
- **(d)** The rule fires on the **EMPTY** branch: the conformal attachment via a canonical J is
  **dead at the fiber level**. T1' reports **NEGATIVE** — stronger than the family-downgrade the
  rule pre-registered. Any complex/conformal structure of this type is not merely one unforced
  choice among a 20-dim family; it is **incompatible** with the fiber's own trace split and
  isotropy. The surviving reading is: *conformal is an import that breaks GU's fiber
  decomposition*, not a structure GU carries.

**What this does and does not gate.** This is an independent fiber-level result about T1' only. It
points in the adverse direction for the whole conformal attachment (T10' soldering and T4'
inherit a weaker premise: whatever they intertwine is now an unforced import), and it sits in the
same territory the separate R4 route (conformal gauge: cure vs inherit the fiber obstruction) is
probing — R4's outcome is **not cited here**; per Section 5.5 of the persona doc it remains the
gate for demoting the Mannheim leg to rejection-level alignment. None of the ten numbered kill
conditions fires from T1' alone; kill condition 8's R4-branch direction is *informed adversely and
independently* by this result.

## 5. Honest gaps

1. **Operationalization of "GU-native".** "Native" was executed as *commuting with the four named
   fiber data*. A weaker demand — J invariant only under a proper subgroup of the isotropy (e.g. at
   a point of reduced symmetry), or J required only to *preserve* rather than commute with the
   trace split — would reopen a family. The named-data list is the route assignment's; the empties
   are theorems **given that list**.
2. **Step 2 is N/A by construction.** The base-vs-vertical split lives on T(Y14) = 4 ⊕ 10; this
   route's arena is the 10-dim vertical summand itself. A 14-dim total-space J-scan (does some J on
   T(Y14) mix base into fiber and evade the fiber-level obstruction?) is a distinct, larger
   computation — related in spirit to what R4 probes at the gauge level; not performed here.
3. **SU(2)+ is engaged only through its SO(3) real image**, because the Lorentzian SD/ASD split is
   complex (Hodge-\*² = −I, verified). A fully complexified treatment (J on the complexified fiber
   commuting with the genuine SU(2)+ action) is out of scope; on the *real* fiber the executed
   version is the only one available, and it is empty.
4. **Section C's exceptional isomorphism** is verified by invariants (dim, rank, Killing signature),
   not by constructing the intertwiner. Sufficient for the informational role it plays here; flagged
   as from-memory standard mathematics confirmed at invariant level.
5. **Scan floors above predictions** (5.200 vs ≥2; 29.000 vs ≥10; 28.337 vs ≥8) are expected: the
   predicted floors bound the J²-term alone, the measured values include the orthogonality residual
   under the commutant constraint. The exact proofs, not the floors, carry the verdicts; the floors
   corroborate.
