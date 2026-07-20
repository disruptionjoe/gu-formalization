---
title: "Channel swing CH-SIG-77 (opening port): the machinery ports clean, the wall stays down, and (7,7) is transcript-compatible -- but the payload count does not drop"
status: active_research
doc_type: exploration
created: 2026-07-19
directed_by: "Joe direct chat, 2026-07-19 (signature competition; CH-SIG-77 opening worker, C11-SIGNATURE-77)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends:
  - explorations/channel-swing-CH-QM-2026-07-19.md
  - explorations/five-leg-swing-2026-07-19.md
inputs:
  - lab/process/construction-space-map.json
  - explorations/channel-swing-CH-GR-2026-07-19.md
  - explorations/channel-swing-CH-COSMO-2026-07-19.md
  - explorations/channel-swing-CH-REC-2026-07-19.md
  - explorations/assembly-archaeology-recovered-parameters-2026-07-19.md
  - canon/no-go-quaternionic-parity-generation-sector.md
  - canon/w2-y14-spin-structure.md
  - canon/shiab-existence-cl95.md
  - canon/no-go-class-relative-map.md
  - explorations/anomaly-and-bordism/n1-signature-audit-y14-clifford-algebra-2026-06-22.md
  - explorations/shiab-operator/n2-shiab-computation-spin77-branching-rules-2026-06-22.md
  - tests/generation-sector/ghost_parity_krein.py
  - tests/generation-sector/signature_77_rerun.py
tests: tests/channel-swings/ch_sig77_port_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# CH-SIG-77 opening port: close-or-kill reconnaissance

Mission (Joe direct chat 2026-07-19): port everything computed tonight to the
(7,7) signature and decide QUICKLY whether this fork is a cheap close, a cheap
kill, or a long road. Everything below is machine-checked in
`tests/channel-swings/ch_sig77_port_probe.py` (exit 0, 23/23 checks) unless
explicitly marked "cited". Signature purity (K6): every computation in the
probe is (7,7); (9,5) facts are cited from receipts, never recomputed; the
one table containing both X4 sign conventions (Section 3) exists to LOCATE
(7,7) and is comparison-grade by construction.

## Verdict up front

**No cheap kill exists.** Every piece of tonight's machinery that was
actually computed -- the QM graded-quotient toy, the GR branch-(a)
cancellation identity, the COSMO magnitude projector, the hyperbolic Krein
pairing -- **ports to (7,7) exactly**, and the parity advantage is real: an
ODD-index Hermitian carrier that is type-consistent with the (7,7) native
antiunitary structure EXISTS on the constraint surface (probe 1e), which the
(9,5) Kramers wall forbids. Moreover (7,7) turns out to be
**transcript-compatible, not GU-adjacent** (Section 3, probe 3f).

But it is **not a free close either**: the payload count does NOT drop
(N stays 5 -- odd is reachable, not forced; probe 1f), the orientation bit's
storage TYPE changes (Section 1c/1g), and the port buys two known debits
(the shiab selector family doubles; the entire ind_H "/8" quaternionic
index arithmetic must be rebuilt as real/KO arithmetic; Section 5).

**Call: CLOSE-PATH (a), with one decisive computation outstanding**
(Section 6). The fork survives its cheapest kill checks and the advantage is
genuine but narrower than hoped: severity and typing, not payload count.

## 1. The class certificate, extended (probe Part 1)

- **1a-1b. Class.** Cl(7,7) relations exact under the repo timelike
  convention T = {4..10}; the CH-QM C3 conjugation J' (factors
  e1 e3 e4 e6 e8 e10 e11 e13) commutes with all 14 generators bit-exactly
  and **J'^2 = +1**: real class M(128,R), no Kramers pairing. This re-runs
  and extends the CH-QM certificate inside the channel.
- **1c. NEW -- the Krein Gram fork.** The ported canonical Gram (the
  convention `tests/generation-sector/ghost_parity_krein.py` already uses
  for its (7,7) branch) is `bS = i * (e_s1...e_s7)`: the bare spacelike
  7-product is ANTI-Hermitian in (7,7) (odd number of factors), so the
  **explicit scalar i is forced**. bS is Hermitian, bS^2 = I,
  so(7,7)-invariant -- and because the scalar i is J'-odd, **bS ANTICOMMUTES
  with J'**: `K(J'x, J'x) = -K(x, x)` (residual 1e-14). **J' flips the Krein
  sign.** This is precisely the C0-control structure of the CH-QM swing --
  "the structure a Krein-sign-discharging orientation would require" --
  realized natively in (7,7). The chirality-twisted alternative
  `bT = e_t1...e_t7` (timelike product, no scalar i; bS/bT = unit * omega)
  is equally Hermitian/involutive/invariant and COMMUTES with J'. Both are
  legitimate so(7,7) Grams; **the port must pin one** (a convention datum,
  not a payload item; (9,5) canon pinned its analog by the per-generator
  -exact beta_S = e0..e8 certificate).
- **1d. Hyperbolic pairing SURVIVES.** Self-dual triplet Krein signature
  (+96, -96) under the canonical (7,7) Gram, re-derived independently inside
  the probe (and matching the standing
  `tests/generation-sector/ghost_parity_krein.py` (7,7) branch).
- **1e. THE PAYOFF CERTIFICATE.** `J'_RS = (id_14 (x) C').conj` squares to
  +1 and preserves the constraint surface. A rank-3 Hermitian carrier built
  from J'-fixed kernel vectors lies ON the constraint surface, IN the
  J'-commutant (J'-defect 1.5e-16), with **signature 3 -- ODD**. Odd index
  is **type-consistent** in (7,7). (9,5) contrast, cited not recomputed:
  the canon quaternionic-parity no-go forces even signature for every
  J_quat-commutant Hermitian carrier; odd carriers there are non-H-linear
  imports (step10/step11, per-generator-exact certificate). **The Kramers
  wall does not reappear in (7,7) under a different name -- this is checked,
  not assumed: no antiunitary in the native structure constrains carrier
  parity under either Gram choice (1g).**
- **1f. HONESTY GUARD -- the cheap-kill candidate that did NOT fire, and
  the advantage that did NOT materialize.** Odd is reachable but NOT
  forced: natural so(7,7) metric connections still give index 0 (all
  tested), and the dimension prime spectrum is still 3-free
  ({128, 14, 1792, 1664} contain no factor 3; matches
  `tests/generation-sector/signature_77_rerun.py`). **The rank/count
  integer import survives the port. Payload N stays 5.** The fork's
  generation advantage is severity and typing (a plain integer under the
  literal-index reading, instead of (9,5)'s choice between a foreign
  non-quaternionic structure or the half-index reading), not count.
- **1g. Sector typing.** Canonical Gram: J' EXCHANGES the two orientation
  sectors (1 +- bS)/2 -- the transmitted bit picks one of two J'-conjugate
  (complex-conjugate) sectors, i.e. **the orientation choice breaks the
  real structure**; resonant with the toy's "the bit chooses which root of
  -1". Chirality-twisted Gram: sectors are J'-invariant and carry a real
  structure inside. Either way, no even-signature constraint survives
  inside a sector: **wall-dissolution is Gram-convention-robust.** The
  (9,5) type annotation "sigma is J_quat-commuting" (CH-QM card A4) does
  NOT port; the (7,7) card must carry the new annotation (Gram-dependent:
  J'-sector-exchanging under the canonical Gram).

## 2. QM graded-quotient toy: SURVIVES VERBATIM (probe Part 2)

The toy (`tests/channel-swings/ch_qm_graded_quotient_toy.py` Parts A-B) is
an abstract 9-dim Krein fixture with **no signature input**; the probe
re-runs it verbatim inside the (7,7) channel and every certificate passes
unchanged: Z/2 register loop-coherent and locally inert (Q4); right
orientation -> positive-definite physical sector, Hermitian descended
dynamics, clean Born rule (Q1/Q2/Q3/Q5/Q6); wrong orientation -> Noether
NON-CLOSURE = gamma (cohomological, primary), 3 negative-norm survivors
under brute grading, regenerating zombie under deletion, retune blocked by
loop-coherent storage. **The orientation mechanism and local inertness
survive; the port is a retyping, not a rebuild.** The retyping is Section
1c/1g: the Z/2 remains well-typed and loop-storable (the register never
touches J), but its type annotation changes -- under the canonical Gram the
bit is real-structure-breaking (C0-typed), which is exactly the structure
that in (9,5) was proven IMPOSSIBLE for the bit to have. Whether that
C0-typing lets the one bit discharge more in (7,7) than it could in (9,5)
is a live question for the full CH-SIG-77 weld, not claimed here.

## 3. GR cancellation identity: SURVIVES EXACTLY, and locates (7,7) on the transcript path (probe Part 3)

Which X4 convention is (7,7)? Computed (probe 3f): the fiber Frobenius
metric on Sym^2(R^4) has signature **(7,3)** and its trace-reversal
**(6,4)** under BOTH X4 sign conventions (both are quadratic in the base
metric, hence blind to g -> -g), while the base pullback flips:

    (3,1) + (6,4) = (9,5)        (1,3) + (6,4) = (7,7)

So **(7,7) sits ON Weinstein's stated (7,3) -> (6,4) trace-reversal path**;
it is the same construction under the mostly-minus X4 convention. The N1
signature audit's "(9,5) is correct" is correct GIVEN its declared (3,1)
base convention (its own line 372); the convention itself is not
transcript-pinned, and `docs/NEXT-FRONTIER-HYPOTHESES.md` H4 already writes
the trace-reversed signature as "(9,5)/(7,7)". Consequences: (i) (7,7) is
**transcript-compatible, not a GU-adjacent deformation**; (ii) since the
two conventions describe the same X4 physics but induce NON-isomorphic
Clifford classes (M(64,H) vs M(128,R)), **the geometry does not pin the
Clifford class -- the class is a discrete datum both signature channels pay
symmetrically** (an even-handedness point for the comparative verdict);
(iii) the fiber signature (6,4) is convention-invariant, so ALL
fiber-group results (Spin(6,4) Pati-Salam chain, fiber module theory) port
untouched.

The identity itself, re-run under eta = diag(+1,-1,-1,-1) with the
correspondingly-signed weak fields (h -> -h): Schwarzschild and Kerr-drag
are harmonic, t1 = 0, Q^TF nonzero, the structural identity
**Q^TF = -[t2]^TF survives**, the cancellation is EXACT at the single
frozen constant **sigma * kappa^2 = 1** (c = 1, same value), and the hard
sign gate survives (sigma = -1 leaves -(1 + kappa^2), no real kappa --
pure algebra, signature-blind). **Nothing in the branch-(a) computation
depends on the (9,5) choice.** DEM-GR-1/2 (the Z/2 sign + frozen kappa)
port unchanged.

## 4. COSMO projector: SURVIVES (probe Part 4)

Under the (7,7)-inducing convention (g -> -g, theta -> -theta): background
magnitude |theta_bar|^2 = alpha^2 + 3 beta^2 unchanged (Frobenius is
quadratic in g^{-1} and theta); projector output still pure helicity-0; the
gauge-shift identity delta|theta|^2 = T * d|theta_bar|^2/dt survives with
spatial-scalar and vector gauge dropping identically; SO(2) helicity
superselection survives (spatial rotation representation theory, which
never sees the signature). The undischarged residue (multi-scalar
helicity-0 mixing, Z_theta) is exactly as in (9,5): C10-dynamics
conditions, not signature-dependent. Part B/C of the COSMO swing (empirical
brackets, sign logic) are data-facing and signature-blind; nothing to port.

## 5. Spin/topology obligations (assessed, NOT computed tonight)

| # | obligation | flag | one-line reason |
|---|---|---|---|
| O1 | W2-01: w2(Y14) = pi* w2(X4) (Y14 spin iff X4 spin) | **PORTS-CLEAN** | mod-2 Stiefel-Whitney arithmetic on the REAL bundle splitting of Sym^2; metric signature never enters w-classes; fiber GL(4,R)/O(3,1) = GL(4,R)/O(1,3) same space |
| O2 | [A-hat(TY14)]_16 anomaly density | **PORTS-CLEAN** | pure rational Pontryagin polynomial of TY14 (`tests/ahat_genus_y14_i16.py` has no signature input; validated on (K3)^4) |
| O3 | (7,3) -> (6,4) fiber trace-reversal / transcript compatibility | **COMPUTED tonight (3f)** | (7,7) = (1,3) + (6,4): same trace-reversal path, opposite X4 sign convention; transcript-compatible, not GU-adjacent |
| O4 | Shiab existence | **PORTS-CLEAN (existence)** | the original N2 computation was literally performed for Spin(7,7)/Cl(7,7) = M(128,R) and later relabeled to (9,5); construction is algebra-independent in form |
| O5 | Shiab SELECTOR (SHIAB-04) | **NEEDS-RECOMPUTE, recorded debit** | the quaternionic/right-H cut that reduced the natural family from real dim 8 to 4 "collapses under a (7,7) alternative -- the real spinor has no J" (SHIAB-04's own words): (7,7) has MORE residual selector freedom, a severity debit |
| O6 | ind_H "/8" generation arithmetic + spin-c exclusion (W2-FC1(2)) | **NEEDS-RECOMPUTE** | ind_H is undefined on a REAL spinor module; the 24/8 = 3 packaging, the Â(K3)=2 doubling role, and the "spin-c breaks H-linearity" exclusion all evaporate in current form and must be rebuilt as real/KO-index arithmetic; note this can cut FAVORABLY (spin-c might rescue non-spin X4 in the real class -- unverified) |
| O7 | C-01 eta(D_Sigma) = 0 mechanism (AZ class CII via C = J_quat * G) | **NEEDS-RECOMPUTE, possibly-fatal to that theorem's port** | the particle-hole symmetry IS J_quat; in the real class the AZ symmetry class changes and "C2 is never an APS index by construction" must be re-derived (the conclusion may survive by another route; the proof does not) |
| O8 | Pin/KO 2-primary structure of the generation apparatus | **NEEDS-RECOMPUTE** | KO periodicity class shifts (p - q: 4 -> 0 mod 8); every divisibility/torsion statement keyed to the H-class changes |
| O9 | Witten class-exit (non-compact fiber) | **PORTS-CLEAN** | exit is via the non-compact fiber GL(4,R)/O(3,1), spin- and signature-independent |
| O10 | Nielsen-Ninomiya net chirality 0 | **PORTS-CLEAN (cited)** | docs H4 already records net chirality 0 "survives into (9,5)/(7,7)" -- flipping signature injects no kinematic 3 |

Nothing on the list is fatal to the fork; O5-O8 are the genuine long-road
tail, and O6+O7 share one root: **the same J_quat that walled off odd
counts in (9,5) was also load-bearing** (in the eta = 0 obstruction, the
spin-c exclusion, and the shiab selector cut). Losing the wall means losing
the wall's work.

## 6. Scorecard vs council round-8 cleanliness criteria, and the verdict

- **Legs that fit:** QM, GR, COSMO port clean (computed). SM: pairing
  survives, odd carrier now type-consistent, chain arithmetic NOT re-run
  (its (9,5) run landed tonight in CH-SM's channel; the (7,7) re-run is the
  outstanding decisive computation).
- **Payload count:** **N(7,7) = 5 -- a TIE with (9,5)**, item for item
  (Z/2 orientation [retyped, 1g] + VEV branch [ports, Sec. 3] + scale +
  subgroup datum [fiber-side, convention-invariant] + rank/count integer
  [survives, 1f]).
- **Forced-import severity:** generations item improves (plain integer,
  literal reading, no foreign structure); shiab selector worsens (O5);
  index arithmetic must be rebuilt (O6-O8). Net: mixed, modestly favorable
  on the payoff channel, unfavorable on the two-primary/selector tail.
- **Kill-test survivals:** all armed cheap kills survived -- no structural
  break anywhere in Parts 1-4; the GR sign gate and the toy's
  wrong-orientation failure mode fire identically.
- **Broken legs:** none found.

**VERDICT: close-path (a), not yet closed.** The machinery ports and the
parity advantage is real; (7,7) is transcript-compatible; nothing broke.
What keeps this from being a full cheap close tonight: the payoff channel
(generations) improved in TYPE but not in COUNT, and the port's true price
sits in the un-recomputed index-arithmetic tail (O5-O8).

**The single most decisive next computation:** the **(7,7) real-index
generation arithmetic** -- rebuild the (9,5) count packaging
(ind_H = 24, count = 24/8 = 3, divisor 8 = rank_H per generation tied to
Cl(9,5) = M(64,H)) in the real class: compute the real/KO divisor for the
(7,7) spinor module, the K3 toy-model index that replaces ind_H, and
whether the count-3 target is (i) forced, (ii) reachable-with-free-integer
(parity with (9,5), fork advantage stays typing-only), or (iii)
UNREACHABLE by real-class divisibility (the fork's remaining cheap-kill
window -- e.g. if real-class arithmetic forces an even or /4 count, the
wall returns through the arithmetic back door). One session, mostly module
theory plus the existing K3 inputs; it is the only computation that can
still cheaply kill the fork, and equally the one that would let CH-SIG-77
claim a genuine payoff over CH-SIG-95 rather than a tie.

## Raw data for the parent

1. **Class/pairing/odd-index certificates:** Cl(7,7) = M(128,R) real class
   (J'^2 = +1, all generators commute bit-exactly); canonical Krein Gram
   requires an explicit scalar i and ANTICOMMUTES with J' (Krein sign
   flips under J'; C0 structure native); chirality-twisted Gram commutes
   (convention fork to pin); triplet pairing (+96, -96) survives;
   ODD-index (signature-3) J'-commutant Hermitian carrier EXISTS on the
   constraint surface (J'-defect 1.5e-16); odd reachable NOT forced
   (connections index 0, spectrum 3-free).
2. **Per-port results:** QM toy SURVIVES verbatim (changed: orientation
   type annotation only); GR identity SURVIVES exactly (sigma*kappa^2 = 1,
   sign gate, Kerr-drag; changed: nothing); COSMO projector SURVIVES
   (changed: nothing).
3. **Obligations:** O1 O2 O4 O9 O10 PORTS-CLEAN; O3 COMPUTED
   (transcript-compatible); O5 O6 O8 NEEDS-RECOMPUTE; O7 NEEDS-RECOMPUTE /
   possibly-fatal-to-that-proof.
4. **Verdict:** close-path (a); decisive next computation = (7,7)
   real-index generation arithmetic (the real-class divisor and count
   packaging; the fork's only remaining cheap-kill window).
5. **Payload count:** N(7,7) = 5, tie with (9,5); advantage is import
   severity and typing on item 5, plus the bit's native C0-typing; debits
   are the shiab selector family doubling and the index-arithmetic rebuild.

## Boundary

All conditional under the standing axiom; toy- and symbol-grade
computations plus module theory; no claim status, canon verdict, scorecard
row, map cell, or public posture moves; no external action. The
(9,5)-vs-(7,7) comparative verdict is the integration barrier's business
(both channels report; verdict-grade signature choice stays Joe-gated) --
nothing here scores CH-SIG-95.
