---
title: "Five-Mathematician Panel: unabsorbed learnings, orderings, and unexplored routes"
status: process
doc_type: research-strategy-synthesis
created: 2026-08-03
updated: 2026-08-03
claim_status_change: none
canon_change: none
method: "Five specialist panels (representation theory, topology/index theory, operator/Krein theory, mathematical physics, research strategy), each seeded with the verified findings of the same-day eleven-lens audit (lab/process/eleven-lens-audit-2026-08-03.md), Joe-directed. Charter: Lane 1 — force, falsify, or precisely place. Items marked [verified] were checked by the orchestrator (quote-trail, arithmetic, or run); the rest are panel-asserted with the checking step named. Layer-0 applies throughout: no decomposition below is a count."
---

# Mathematician-panel synthesis

Companion to the audit report. This file is the opportunity map: what the
program has already learned without absorbing, what should be reordered, and
what is unexplored. It changes no claim; every item names its own check.

## 0. The convergent verdict (reached independently by 4 of 5 panels)

**The kinematic/boundary program should lead; the interior source-action
campaign continues as the slow lane under a new acceptance rule.** Reached
independently by the rep-theory, topology, operator-theory, and strategy
panels, with the physicist concurring in weaker form. Load-bearing
sub-findings:

- **Gap (ii) of the boundary bridge IS the interior source action** (strategy
  panel; verified against `canon/final-verdict-generation-count-and-the-open-bridge.md`).
  The two programs are not rivals; they share one blocking dependency. What is
  reallocatable is precise: bridge gaps (i) and (iii), plus the whole
  kinematic layer, are decidable now with installed tools.
- **The RB6/RB7 null verdicts were read inside the finite-difference noise
  band** (numerics lens, mechanism [verified]; RB7's vertical residual is
  exactly 0 and its published numbers are s⁻³ roundoff). New acceptance rule:
  no new interior wave until the previous wave's null is certified with exact
  derivatives; no wave scheduled that cannot move a named gate.
- The interior campaign is NOT quiescent: `agent/null-clifford-omega1-repair`
  was committing the pw2fr campaign at ~1.8 commits/hour on 2026-08-03
  [verified]. The acceptance rule applies to it.

## 1. Top unabsorbed learnings (cross-panel, ranked)

**U1 — Inflow provably cannot be the 2↔3 bridge (a near-theorem split across
two files).** [verified — both quotes verbatim]
`canon/three-generations-locate-not-force-CRT-RESULTS.md:40`: "anomaly inflow
is the sole bridge." `explorations/global-anomaly-leg-2026-07-20.md:252`: "the
spin Dai-Freed ledger has NO 3-primary column in any dimension (spin-bordism
torsion is all 2-primary, Wall+ABP; BSp adds none, Borel)." Together: the sole
bridge cannot carry Z/3 through the spin wall, so route (iii) of the
single-decider program dies as stated, and any count-bridge is forced onto
framed/Pin/String structures — exactly where U3 lives. Cost S (assembly).
Settles: whether the single decider's SPT route is alive. Anchor: N_gen.

**U2 — The generation-fork branching already exists in-repo under a B5
filename.** [verified — slot table at `explorations/shiab-operator/b5-observer-symbol-multiplicity-matrix-2026-07-24.md:77-90`]
The D₂×D₅ decomposition OQ-RK1 has waited on since June is filed: `(3,2,16±)`
is the 4D chiral gravitino with internal multiplicity the 16 of Spin(10) —
the effective RS twist is `S(6,4)^chiral`, rank_C 16. Next: restrict the
existing `J` to the branched slots and determine whether it acts within `16⁺`
or exchanges `16⁺↔16⁻` (numpy on existing fixtures, 4–8 h). Layer-0 fence
(both rep and strategy panels, agreeing with `tests/oq_rk1_e_rs_eff_assembly.py`'s
BLOCKED_NEEDS_SPEC): naming how the H-structure factorizes across the tensor
splitting is itself the deliverable — the branching narrows the fork; whether
it closes it depends on whether equivariance forces the summand
identification. Anchor: N_gen (4-vs-8 candidate fork).

**U3 — The true boundary receptacle is purely 3-primary, and the located-not-
forced theorem is currently proved about a surrogate.** [standard facts;
π₁₃ˢ = Z/3, Im J₁₃ = 0 need in-repo citation]
In dim 13 (the actual link, `RP³×S⁶` fibered over X⁴): the framed receptacle
is Z/3 with no 2-primary part, no String structure needed (the
`leg_tmf_string.py` gate is vacuous for framed bordism), and the e-invariant
is identically zero — the correct detector is the Laures f-invariant
(Bunke–Naumann arXiv:0808.0257 for the index form; zero repo hits). Upgrade
available: "2-primary blindness" becomes "the boundary group cannot express
the interior obstruction's type at all" — the Firewall-Boundary Hypothesis as
a group-theoretic identity. Bunke's universal eta (arXiv:1103.4217) supplies
the eta↔e dictionary canon says doesn't exist, and likely converts bridge gap
(iii) into a clean no-go (an η-derived invariant valued in torsion cannot
equal an integer count since Hom(Z/3,Z)=0). Costs: restatement 1–2 d;
f-invariant program is the one genuine research project (weeks).

**U4 — Bridge gap (i) reduces to one eta-form, with a candidate one-line
vanishing.** [panel derivation; needs referee]
The topology panel computed what the repo only asserted: the spine's normal
bundle is `ν ≅ R ⊕ Sym²(Q*)` (from `Sym²(T*) = Sym²(ℓ*) ⊕ ℓ*⊗Q* ⊕ Sym²(Q*)`),
stably trivial over RP³ and rank 7 > 3, hence trivial — the 13-link is
literally `RP³ × S⁶`. Lichnerowicz kills ker D^{S⁶}, so Bismut–Cheeger applies
with no Dai corrections and the only unknown is η̃; the free R-summand gives a
fiberwise orientation-reversing reflection sending η̃ ↦ −η̃ — candidate
theorem η̃ = 0, closing gap (i) from geometry alone, independent of the source
action. Honest residue: the reflection's compatibility with the chosen spin
structure/horizontal distribution, and the full 7-dim base where Sym²Q* is
twisted. Cost 3–5 d. Anchor: N_gen; gravity (the −p₁/24 inflow channel).

**U5 — The Λ⁵/126 seesaw channel is internal, and the mass story is
assemblable.** [arithmetic verified: 2002 = 252+840+720+180+10; Λ⁵(R¹⁰) = 252
= 126⊕126̄ as Lorentz singlet; canon's own 16×16 = 10+120+126]
Combined with the unwritten SU(4)_c relation `m_D^ν = m_up` at the PS scale:
`m_ν₃ ≈ m_t²/M_R` retrodicts `M_R ≈ 6×10¹⁴ GeV` [arithmetic verified] — a
zero-free-parameter retrodiction once M_PS is fixed, in exactly the
hypercharge-precedent sense of AGENTS.md. Next: branch Λ⁵(V₁₄) under
so(3,1)⊕so(6,4) → Pati-Salam (1 d, signature-blind); write the RG page (S).
Anchor: neutrino masses — the highest value-per-cost physical lug on the
board.

**U6 — The Krein-sign question became a trichotomy, and its input is
computable now.** [W219 quote verified; SGH parallel is lens-supplied,
secondary-source]
Prop 1 + Thm 2 of the structurally-forced draft, applied to the *generated
observable algebra* (not a guessed stabilizer), yield: irreducible+compact ⇒
sign forced (F a singleton); reducible ⇒ the external datum's type and
dimension are COMPUTED by `Σ_λ dim_R(D_λ)a_λb_λ`; non-compact closure ⇒ F = ∅
⇒ deny-Prop-1 ⇒ firewall positivity forced. The operator panel specs the
commutant computation on ker Γ (1664-dim) via the tensor shortcut (1–2 d,
existing fixtures). Either outcome retires the "one externally-owned bit"
framing — the sharpest single available question in the program. Anchor:
measurement-record; bar(b); projected unitarity.

**U7 — The B5 residual is a signature, and three of its five fields may be
derived, not posited.** [panel; structure claims checkable against
`tests/shiab_b5_krein_mirror_orbit_reduction.py`]
The eleven parity-dimension values are the eleven inertia classes (k, 10−k)
of a Hermitian form on the ten mirror edges; each edge sign ε_e is a
Frobenius–Schur-type indicator plausibly forced by Clifford type. Prediction:
(9,5) ⇒ k=0 ⇒ (58,78); (7,7) ⇒ k=10 ⇒ (78,58) — endpoints only. If confirmed
(2–4 d finite rep theory), fields (i)–(iii) of the B5 packet are derived and
the fail-closed contract is satisfiable natively for 3 of 5; fields (iv)–(v)
are exactly what Bär–Ballmann (arXiv:1101.1196) + Bär–Bandara
(arXiv:1906.08581; non-compact boundary arXiv:2401.17784) construct
generically — zero repo citations [grep verified by panel]. This unblocks
B5, OPERATOR-END-PENCIL, and RB8 simultaneously and splits B5 into an
algebraic half (now) and an analytic half (boundary triples). The fail-closed
contract stays; these proposals satisfy it, not weaken it.

**U8 — RB7's own output specifies its missing stabilizer, and its saddle
verdict is convention-charged.** [panel; RB7 quotes consistent with doc]
(a) The runaway lives on the commuting cone where the YM quartic vanishes; a
completion stabilizes iff coercive there — a kernel condition
`ker(D⁰)∩ker(C)∩{commuting cone} = {0}` decidable in days, replacing the
planned term-by-term search. The natural candidate term's kernel is RB7's own
exact mixed Gram (9/32)(I+T_tr). (b) The reported Hessian spectra are plain
second derivatives on a DeWitt-indefinite fiber; only the inertia of
(Hess, G_V) is invariant, and on a negative-definite support the Morse index
is convention-dependent — re-report before treating the saddle as a kill.
(c) Physics reading: an index-2 saddle whose unstable modes change singular
values = the anisotropic (curvature-locked) VEV branch selecting itself — the
one branch that can break Spin(10). Anchor: source action; Cartan 3+1.

**U9 — The DESI shape failure is a structural requirement on the source
action, and the repo owns a candidate mechanism.** [exclusion mechanics
verified by the audit's cosmology lens]
The signal-level exclusion is a shape failure (too little low-z evolution at
the θ★-forced Ωm). The GU-native escape class is a coefficient growing at low
z; `explorations/W187-…` already has `r(N) = κ₀√N` growing by record
accretion — monotone in cosmic time. Connect them: re-solve the background
with r(N(z)), refit θ★, report Δχ²_shape (S–M; pipeline exists). Either the
family exclusion is a truncation artifact, or the record-accretion law is
excluded too — both are informative. Anchor: cosmology.

**U10 — (7,7) as physics, not as an audit.** [panel]
Real class M(128,R): natively Majorana, real index (different divisor), and an
O(p,q)-type Krein form — the exact case where the uniqueness theorem applies
with no shared-irrep escape. (7,7) may FORCE the Krein sign that (9,5) leaves
open; it is also the signature of the verified Pati-Salam chain. One
reality-class ledger table (1–2 d) makes the fork decision-relevant for the
count arithmetic (every dim_H halving restates; some values change, not just
labels). Fix on the way through: `RESEARCH-STATUS.md:376` still says "(9,5)
confirmed RESOLVED."

## 2. The candidate unified vision (physicist panel; stated as a posit)

> GU is an SO(10)-class grand unified theory whose interior is vectorlike,
> even, and gauge-complete (Pati-Salam chain, absolute Y-normalization 5/3
> earned), whose gravity is linear-in-curvature (c_R = 0 at law level), whose
> vacuum sector is everpresent-class (amplitude yes, phase no), whose fermion
> masses come from odd-form VEVs inside the equivariant family (Λ⁵ = the 126),
> whose metric slot can select exactly one breaking chain (Sym²(10) = 1 + 54)
> — and whose chirality, odd generation count, and record/measurement
> structure live on a 13-dimensional boundary whose framed receptacle is
> purely 3-primary, with the Krein sign forced iff the observable algebra is
> irreducible.

Constraint surplus counted at ≈ +14 (≈32 independent computed constraints vs
≈18 declared free parameters), deflating to ≈ +4 under the hostile reading
that books the SO(10) frame as imported — positive across the band, which is
the regime where the orthodox reflex misfires (AGENTS.md). One constraint
FAILED and is recorded as such (the DE signal-level identification). Eight
kill conditions are named in the panel report, the sharpest being: K1 the
fibered reduction lands gauge (3-part zero); K2 the observable algebra is
reducible with shared types (the 4→1 sign collapse evaporates); K3 any
>3σ w(z) < −1 detection; K8 = U1 resolving against a 3-primary bridge with no
framed replacement. Layer-0 fence: nothing here converts a multiplicity into
a count; "count = dim_H" remains a reading with an unpinned divisor.

Distinctive-physics candidates surfaced (posits, surplus to be counted before
pursuit): the M_R ≈ 6×10¹⁴ GeV retrodiction (U5); n–n̄ oscillation rather
than p→e⁺π⁰ as the flagship B-violation (PS-side, D-even, 126 rank-drop);
Z₃ (not Z₂) matter parity if the boundary's 3-primary structure descends —
semi-annihilating dark matter with distinct relic/indirect signatures; a
finite count of exceptional/bistability loci if the boundary Pontryagin index
κ is finite (operator panel O8).

## 3. Ordered queue (strategy panel, corrected)

**Tier 0 — Joe (~40 min):** J1 send the drafted arXiv endorsement email
(`papers/candidates/located-not-forced/ENDORSER-REQUEST-DRAFT.md`, exists,
unsent); J2 `brew install --cask sage` interactively (8 named CAS gates; NOT
OQ-RK1, which is spec-blocked); J3 name the trunk and authorize the merge to
main (CI over 75 commits; ends three-way divergence); J4 authorize seeding
the 4 finished GU-independent assets (good-stable no-go, two-arena core
[Lean-verified], shape-blind c_R, Pati-Salam 19/19 + survey); J5 standing
answer on whether a decisive computation may move bar(b)/H59/count (they are
Joe-gated; without a pre-answer, Tier-1 results cannot land).

**Tier 1 (hours–2 days, decidable now):** exact-derivative certification of
the RB nulls (fork: artifact vs certified-terminal); U1 assembly; U6
commutant computation; U2 J-restriction (with its Layer-0 fence); U5 Λ⁵
branching + the RG/seesaw page; surface repairs per the audit fix packet;
DE-SNe pure-shape leg (cheap, closes a named residual).

**Tier 2 (days–weeks):** U4 η̃ (raced against U3's dim-13 restatement — both
attack gap (i)); U7 B5 signature test then Bär–Ballmann skeleton; U8 kernel
condition then (only if it passes) a stabilized RB7.1; U9 r(N(z)) refit;
U10 (7,7) ledger; Bunke dictionary note; gap (iii) restated via Bunke
(probable no-go).

**Tier 3 (research projects):** the f-invariant program (the one multi-week
item; the correct home of the boundary class); boundary-triple κ(M) of the
Weyl function (the firewall hypothesis as a number — after the Bär–Ballmann
skeleton); Kobayashi discrete-decomposability for (O(9,5), O(3,1)×O(6,4)) +
the minimal-rep null-cone realization (a second exact-math instance of the
firewall).

**Do not schedule (blocked on unbuilt objects):** OQ-RK1's decisive rank
(needs Π_RS^phys spec), B5 packet field selection beyond U7's three,
SRC-TOY-01 rungs 2–5, the pw2fr open-list items — subject to the acceptance
rule above.

## 4. Negative space (strategy panel verdicts)

Probe-worthy: **functorial/TQFT axiomatization of the 13-dim boundary**
(Freed–Teleman shape; the bounded question is whether GU's class map hits the
nontrivial element of the already-derived Ω^{Pin+}₁₄ ≅ Z/2 — if GU's 14d
content is non-anomalous, the firewall has no home); **framed-bordism/tmf
data of the actual link** (NOT spectral geometry — the repo's own 2-primary
lemma proves a spectral computation on L(2;1) cannot see Z/3);
**surplus-guided term search** (only after U7/O-panel work makes surplus
computable — today it has no objective function). Mostly-noise: lattice-Y¹⁴
(inherits Jackiw–Rebbi hosting-not-selection by construction; only relevant
if SRC-TOY rung 2 is built anyway); S-matrix positivity bounds (needs the
unbuilt 4d EFT and a unitarity premise the Krein structure breaks); twistor
methods (the guardrail file exists for a reason; the fork it would probe is
already resolved); deformation quantization (no identified Poisson structure;
the live version is the BV-BFV boundary work already started).

## 5. Efficiency and infrastructure

Compounding, in order: (1) the exact-derivative library (kills the FD-noise
class permanently; drops the W177 floor ~6 decades; converts three floor
verdicts to structural ones); (2) the branching dictionary (one Sage/Racah-
Speiser module discharging FC-IRR/FC-HW/FC-MULT/OQ1/OQ-CG-2 and U2/U5 from
one build — note the D₅ machinery already exists in the B5 file); (3) CI on
working branches + a Python quick-sweep job + a committed baseline receipt;
(4) a derived LANE-STATE (~50-line generator; every stale field is
mechanically derivable; failure mode today is "stale green reads as healthy");
(5) split the live frontier block out of NEXT-STEPS.md (330 KB append-only)
into a small FRONTIER.md. Process finding: the pw2fr campaign's suffix chain
(six levels deep, ~1.8 commits/hour, no claim_status_change fields) is the
North-Star-vs-quick-payoff failure mode in its "wild exploration wearing
exploit clothing" form — the acceptance rule in §0 is the repair.

## 6. Caveats

Panel items not orchestrator-verified are marked and carry their own checking
steps; the three highest-stakes panel derivations (U4's ν-triviality and
reflection lemma, U7's endpoint prediction, U6's expected commutant) are
exactly the ones to referee first — each is also cheap. The audit's stale-
surface findings mean several panel inputs (LANE-STATE, portfolio states)
described a week-old repo; the live pw2fr branch partially supersedes the
"interior blocked" premise, and the §0 verdict was re-derived with that
correction and stands. External-literature attributions (SGH 1992, Bunke,
Bär–Ballmann, Kobayashi–Ørsted, Laures) were live-checked by the panels at
abstract level but should be confirmed against primary texts before any repo
artifact cites them — the repo's own oq3b forensic standard applies.
