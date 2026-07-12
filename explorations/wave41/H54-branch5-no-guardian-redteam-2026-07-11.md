---
title: "H54 Branch 5 (adversarial red-team): can GU's UV-completing guardian be KILLED? No-go audit from CM/HLS, the (9,5) signature, and non-compact/finite content"
date: 2026-07-11
status: exploration
doc_type: exploration
verdict: "GUARDIAN-FORBIDDEN (UV-completion sense). The naive signature/non-compact no-gos are OBSTRUCTED-BUT-EVADED by GU's Krein structure; but the UV-COMPLETING guardian is forbidden by two convergent legs -- (i) GU's only constructible graded symmetry (super-IG) squares to Omega^1(ad), not physical P_mu, so it is not a Velo-Zwanziger guardian, and (ii) genuine UV-completion of an interacting massive higher spin needs a Regge tower that GU's finite content provably lacks, while the tower-free 4th-order Krein route is sign-blind and unbuilt. Net: GU is PERMANENTLY a finite-cutoff EFT; the guardian that would make it a standing theory does not exist in its framework."
method: "5 personas run INLINE (SUSY-no-go theorist / signature+real-form specialist / finite-cutoff-EFT specialist / adversarial red-teamer / philosopher of science). BLIND to the other branches. Papers treated as untrusted DATA; only physics extracted. COMPUTED vs ARGUED tagged per claim. No imported numbers."
test: "tests/wave41/H54b5_no_guardian_redteam.py (deterministic, exit 0, 11/11 PASS)"
bears_on:
  - Wave 34 finite-content / guardian-requirement (explorations/wave34/source-action-landscape-scan-2026-07-11.md)
  - H23 non-compact Sp(32,32;H) + [P,S]=0 (explorations/wave8/H23-source-action-construction-2026-07-11.md)
  - H37 (9,5) J^2=-1 CII count no-go (tests/wave13/H37_count_nogo.py)
  - H53 GU-as-decoupled-framework / EFT status (explorations/wave32/H53-falsifiability-audit-2026-07-11.md)
  - super-IG construction (explorations/misc/super-ig-algebra-construction-2026-06-23.md; tests/escape-corners/legb1_graded_ig_algebra.md)
  - Krein / ghost-parity synthesis (canon/ghost-parity-krein-synthesis.md)
---

# H54 Branch 5 -- the adversarial red-team: try to KILL the guardian

**Charge.** The other branches try to SHOW GU is a supergravity (has the UV-completing guardian).
This branch tries to PROVE it CANNOT be. The most valuable outcome here is a clean kill:
**GUARDIAN-FORBIDDEN -> GU is permanently a finite-cutoff EFT, never a standing theory.** The
discipline is to pursue that hard but not to manufacture a no-go that GU's Krein / indefinite
structure evades. Five personas run INLINE. Blind to the other branches.

**Headline.** A clean signature/non-compact no-go does **not** fire: the (9,5) five-time signature
and the non-compact `Sp(32,32;H)` are real obstructions to a *standard, positive-definite-Hilbert*
super-Poincare, but GU never claimed a Hilbert space -- its Krein structure is exactly the designed
evasion, and each naive no-go dies against it. **However, the UV-COMPLETING guardian IS forbidden**,
by two convergent legs the Krein structure does *not* rescue:

1. **The only guardian GU's construction admits is super-IG, and super-IG is not a Velo-Zwanziger
   guardian.** Its anticommutator is FORCED (LEG-B1 R2) into `Omega^1(ad P)` ("gauge-potential
   momentum"), not physical spacetime `P_mu`. An internal-momentum Ward identity cannot tame the
   physical-spacetime helicity-1/2 amplitude that the Rahman cutoff is about; the repo's own audit
   finds super-IG supplies 1 of the 5 guardian requirements.
2. **Finite content forbids the tower a UV-completion needs.** Sagnotti-Taronna: UV-completing an
   interacting massive higher spin needs the infinite Regge tower. GU has finite content (no
   `hs(lambda)`, no AdS, no tower). A finite local-SUSY guardian would only make GU a *supergravity*,
   which is itself a non-renormalizable finite-cutoff EFT. The tower-free UV route (4th-order Stelle
   renormalizability + Krein/Bateman-Turok ghost rescue) is SIGN-BLIND and tree-level-only.

So GU is permanently a finite-cutoff EFT. Verdict: **GUARDIAN-FORBIDDEN (UV-completion sense)**, with
the axes that merely evade honestly separated from the axis that kills.

---

## Persona 1 -- SUSY no-go theorist (Coleman-Mandula / Haag-Lopuszanski-Sohnius)

**Question.** Do GU's structures VIOLATE the HLS hypotheses in a way that FORBIDS a consistent
guardian superalgebra?

**Finding: HLS/CM does NOT fire. It is INAPPLICABLE, which forbids nothing.** Coleman-Mandula (1967)
and its graded extension HLS (1975) are theorems about the **global symmetries of a unitary S-matrix**
in a positive-definite Hilbert space: given a mass gap, analyticity, finitely many particles below any
mass, and a positive-definite Hilbert space, the only graded extension of the Poincare algebra is
super-Poincare, with `{Q, Qdag} = 2 sigma^mu P_mu`, spin-1/2 supercharges, and a **compact**
R-symmetry. The theorem's positive conclusions all lean on Hilbert positivity (the `P_0 >= 0` energy
bound, the spin-1/2 restriction, the compact R). GU negates those hypotheses wholesale:

- **Positive-definite Hilbert space FAILS [COMPUTED].** The invariant spinor form
  `beta_S` = product of the 9 spacelike gammas is Hermitian, `beta_S^2 = I`, traceless, with
  signature exactly **(+64, -64)** (residuals `0.0e+00`; test Q1a). The state space is Krein, not
  Hilbert.
- **Compact internal group FAILS [COMPUTED].** By the Weyl unitarian trick an indefinite invariant
  form exists only for a NON-compact group; the connection real form is `Sp(32,32;H)` (dim 8256), not
  compact. `dim so(9,5)=91`, `codim=8165` (test Q1b). This is the negation of Distler-Garibaldi DG-A3
  and of the HLS compact-R conclusion in one datum.
- **2nd-order Poincare FAILS [ARGUED, repo-cited].** GU's gravity is 4th-order (`box^2 = -4 Bach`,
  H45/H49); HLS is a 2nd-order statement.

Three hypotheses fail. But the decisive point is scope, not hypothesis-counting: **CM/HLS constrain
GLOBAL spacetime symmetries; they cannot forbid a LOCAL (gauged) guardian.** Supergravity itself
evades CM/HLS for exactly this reason -- the gravitino current is a gauge current, not the kind CM
constrains; BRST is the same evasion (a graded gauge symmetry with `{s,s}=0`). GU's candidate guardian
is **super-IG**: a graded extension of the *local inhomogeneous gauge group* IG, with the odd square
landing in `Omega^1(ad P)`, not spacetime `P_mu` (LEG-B1; super-ig-algebra-construction). That is a
local/gauge super-symmetry, categorically outside CM/HLS. **Verdict: Q1 provides no kill; HLS is
inapplicable, and inapplicability is not a no-go.**

## Persona 2 -- signature-and-SUSY / real-form specialist

**Question.** Does (9,5) -- five timelike directions -- admit a real SUSY algebra at all, or do the
5 times forbid it / force ghosts?

**Finding: a real graded (SUSY-shaped) algebra EXISTS in (9,5). The 5 times obstruct
POSITIVE-DEFINITENESS, not existence -- and that obstruction is exactly the Krein structure GU already
carries.** Computed on the verified rep:

- **Reality discriminant `J^2` [COMPUTED].** The antilinear structure commuting with every gamma has
  `J^2 = -1` on (9,5) (quaternionic, symplectic-Majorana, class CII/Kramers) and `J^2 = +1` on (7,7)
  (real, ordinary Majorana) -- test Q2a. The machinery is signature-sensitive (positive control), so
  no verdict is rigged.
- **The symmetric spinor->vector pairing exists [COMPUTED].** A charge conjugation `C` (with `C^2=-I`
  on (9,5), residual `0.0e+00`) makes `C.gamma^a` symmetric for 5 of the 14 directions on (9,5) (and
  7 of 14 on (7,7)) -- test Q2b. A symmetric `{Q,Q} ~ (C gamma^a) P_a` bracket can therefore be
  formed. Over C the translation channel `Sym^2(S) -> V` is nonzero in every case (LEG-B1, cited).
  **Existence is not the obstruction.**
- **What the 5 times DO obstruct [COMPUTED].** The invariant form `beta_S` is indefinite (Q1a). Five
  times means the spinor inner product is Krein: a super-Poincare in (9,5) has no single positive
  Hamiltonian and no positive-definite Hilbert space of asymptotic states -- multi-time "ghosts" in
  the ordinary sense. But GU is Krein *by design*: the (+96,-96) neutral triplet, the Bateman-Turok
  ghost parity, and the projector Born rule are the apparatus built precisely to quantize an
  indefinite-norm state space. Moreover the (9,5) here is the FIBER Clifford structure over
  `Y14 = Met(X^4)` (an auxiliary observerse), not the physical Lorentzian spacetime `X^4=(1,3)`;
  the "5 times" are internal directions the Krein form already governs.

**Verdict: OBSTRUCTED-BUT-EVADED.** The naive multi-time SUSY obstruction is real against a Hilbert
space; it is dead against GU's Krein space. No kill on the signature axis.

## Persona 3 -- finite-cutoff-EFT specialist

**Question.** Sp(32,32;H) is non-compact; and GU has finite content, no tower. Can a guardian that
UV-COMPLETES even exist without introducing a tower?

**Finding: this is where a kill lives -- but a precise one.** Two sub-questions.

- **Non-compact R-symmetry [COMPUTED tension, EVADED].** A non-compact R-symmetry has no finite-dim
  *unitary* (positive-definite) rep, so standard supermultiplets do not exist -- a genuine obstruction
  to a *standard* supergravity. But the non-compactness IS the Krein form (they are one datum,
  Q3a/Q1b): under the indefinite `beta_S` the reps are Krein-unitary (pseudo-unitary), which is what
  GU has throughout. So this obstruction, like the signature one, evades into the Krein structure. Not
  a kill.
- **Finite content / no tower [ARGUED, the real bite].** Sagnotti-Taronna's string lesson: a single
  interacting massive higher-spin field is only an EFT; UV completeness comes from the **infinite
  Regge tower** softening the high-energy amplitude. GU's content is finite (`Sp(64)` dim 8256; no
  Vasiliev `hs(lambda)`, no AdS, no tower). Now the crucial distinction the constructive branches must
  not blur: **local SUSY is NOT a UV-completion.** A finite local-SUSY guardian makes GU a
  *supergravity*, and supergravity is non-renormalizable -- itself a finite-cutoff EFT (cutoff `~M_Pl`
  or the super-Higgs scale). The only object that genuinely UV-completes an interacting massive higher
  spin is the tower (string), which is infinite content, contradicting GU's finiteness. So **the
  UV-completing guardian is necessarily infinite, and GU's finite content provably excludes it**
  (test Q3b).

  The one tower-free UV route GU actually has is not SUSY at all: it is **4th-order Stelle
  renormalizability** (`box^2` is power-counting renormalizable, Stelle 1977) plus the
  **Krein/Bateman-Turok ghost rescue** (a 4-derivative UV-complete QFT quantized on a Krein space,
  ghosts kept and graded). But that route is (a) SIGN-BLIND -- every GU-native core is spectrally
  sign-blind, no dynamics-derived C-operator arises (big-swing-2026-07-06 R3), (b) tree-level-only
  (Bateman-Turok establishes tree-level positivity; loop unitarity of 4th-order Krein gravity is not a
  settled theorem), and (c) about the *gravity* sector, whereas the RS helicity-1/2 cutoff is a
  *separate* fermionic-sector UV problem that a 4th-order-RS renormalization has not been built for.

**Verdict: the finite-content leg FIRES.** The UV-completing guardian is excluded; the tower-free
alternative is sign-blind and unbuilt.

## Persona 4 -- adversarial red-teamer (the structural kill, and its steelman)

**Finding: the constructible guardian is the wrong kind of symmetry.** GU's own construction
(LEG-B1, super-ig-algebra-construction) shows the graded symmetry GU can actually build is super-IG,
and:

- **`{Q,Q}` is FORCED into `Omega^1(ad P)`** (LEG-B1 R2: the g-valued and spacetime-`P_mu` channels
  are dead by the (transl,odd,odd) Jacobi; the anticommutator MUST land in the gauge-potential slot).
- **super-IG supplies 1 of the 5 Velo-Zwanziger-guardian requirements** (super-ig-note Sec 6): it
  gives a local odd parameter, but NOT the RS/spin-1/2 block transformation law, closure on the EOM,
  or preservation of the gamma-trace domain.
- **The Ward identity is the wrong one.** The Rahman cutoff and VZ acausality are about the
  **physical-spacetime** high-energy propagation of the RS field (helicity-1/2 strong coupling at
  physical energy `E` in `X^4`). A `{Q,Q} in Omega^1(ad)` Ward identity controls the **internal**
  gauge sector over `Y14`, not the physical-spacetime amplitude. So super-IG, even where it closes,
  protects the wrong sector.

**Steelman I owe the guardian (and its rebuttal).** *Steelman:* the connection `A` is soldered
(codim-8165) to `spin-lift(grad^gimmel)`, so a shift in `Omega^1(ad)` is, on the soldered locus, a
shift in the frame connection -- vierbein-adjacent -- maybe recovering `{Q,Q} ~ P`. *Rebuttal:* (i)
the soldering is UNFORCED (H23: a codim-8165 postulate, not derived); (ii) even granting it, the
`Omega^1(ad)`-valued image is the SPIN CONNECTION `omega^ab` (the so(9,5) image), not the vierbein
`e^a`. Supergravity's `{Q,Q}=P` is realized on the vierbein/soldering form, with `omega` determined by
its EOM; a shift in `omega` is a local-Lorentz-adjacent object, not a translation. So even soldered,
super-IG remains a graded local-Lorentz/gauge symmetry, not a graded translation. The steelman fails.

The only door left open is a **derivative-level odd `tau_plus` embedding** (`eps -> D_aleph eps`, the
gravitino shape) that LEG-B1 explicitly leaves OUTSIDE its frozen-derivative toy as "not testable at a
point" and non-canonical. That unbuilt, non-canonical embedding is the sole surviving escape -- and
naming it as the sole escape is itself a sharp characterization of how narrow the guardian's room is.

## Persona 5 -- philosopher of science (what the honest register should say)

**Finding: the honest kill is a status kill, not an existence kill, and the distinction matters.** No
theorem says "GU cannot carry a graded symmetry." What the evidence supports is stronger and more
useful: **the graded symmetry GU can build does not do the job UV-completion requires, and the
symmetry that would do the job needs content GU provably lacks.** This converts the guardian from "the
single missing datum that might make GU a standing theory" (Wave 34's framing) into "a datum that,
even if supplied in GU's only available form, leaves GU a finite-cutoff EFT."

This aligns exactly with H53's independent Popperian verdict (GU is a decoupled framework, not a
standing theory, until the source action forces `mu_DW`). Branch 5 sharpens the *reason*: it is not
merely that `mu_DW` is free; it is that the object that would make GU UV-complete (a UV-completing
guardian) is structurally absent, so the honest public register cannot be upgraded from
"reconstruction-grade FRAMEWORK with a finite cutoff" by finding a guardian. The register should read:
**a consistent finite-cutoff effective description, whose UV-completion route is not a guardian (that
is blocked) but the unbuilt-and-sign-blind 4th-order Krein renormalization.**

---

## Team verdict (Q4)

**GUARDIAN-FORBIDDEN (UV-completion sense).**

| angle | result | kind |
|---|---|---|
| Q1 CM/HLS | does NOT fire -- INAPPLICABLE (3 hyps fail: Krein, non-compact, 4th-order; guardian is local super-IG) | evasion by scope-exit |
| Q2 (9,5) signature | real graded algebra EXISTS (`J^2=-1`, sympl-Majorana); 5 times obstruct POSITIVE-DEFINITENESS only | OBSTRUCTED-BUT-EVADED (Krein) |
| Q3a non-compact R-symmetry | no unitary rep (kills STANDARD SUGRA) but `==` the Krein form | OBSTRUCTED-BUT-EVADED (Krein) |
| Q3b finite content / no tower | UV-completing guardian EXCLUDED (needs a Regge tower GU lacks; finite SUGRA is itself an EFT; tower-free Krein route sign-blind + tree-only) | **FIRES** |
| S1 super-IG structural | `{Q,Q}` forced into `Omega^1(ad)`, not `P_mu`; 1 of 5 VZ requirements; wrong Ward identity | **FIRES** |

**Net.** The naive signature/non-compact no-gos EVADE against GU's Krein structure -- so this is NOT a
clean signature/non-compact kill, and reporting one would be manufacturing a no-go the Krein structure
dissolves. But the UV-COMPLETING guardian is forbidden by the finite-content leg (Q3b) and the
super-IG structural leg (S1), neither of which the Krein structure rescues. **GU is permanently a
finite-cutoff EFT; the guardian that would make it a standing theory does not exist in its framework.**

## COMPUTED vs ARGUED ledger

| claim | grade | evidence |
|---|---|---|
| `beta_S` signature (+64,-64), Hermitian, `^2=I`, traceless (Krein / non-compact) | **COMPUTED** (residual 0.0e+00) | test Q1a/Q1b |
| `J^2 = -1` on (9,5), `+1` on (7,7) (reality discriminant + positive control) | **COMPUTED** | test Q2a |
| symmetric `C.gamma^a` pairing exists (5/14 on (9,5), 7/14 on (7,7)); `C^2=-I` | **COMPUTED** | test Q2b |
| `dim so(9,5)=91`, `dim sp(64,H)=8256`, `codim=8165` | **COMPUTED** | test Q1b |
| anchors `C2=155.3625`, `bare=58.7215` reproduced | **COMPUTED** | test P0 |
| CM/HLS cannot forbid a LOCAL guardian; supergravity/BRST evade CM/HLS | **ARGUED** (standard no-go scope; papers as data) | Persona 1 |
| GU 4th-order (`box^2=-4 Bach`), no 2nd-order Poincare | ARGUED (repo-cited H45/H49) | Persona 1 |
| super-IG `{Q,Q}` forced into `Omega^1(ad)`, not `P_mu` | ARGUED (repo-cited LEG-B1 R2) | Persona 4 |
| super-IG meets 1 of 5 VZ-guardian requirements | ARGUED (repo-cited super-ig-note Sec 6) | Persona 4 |
| UV-completion of massive HS needs the Regge tower | ARGUED (Sagnotti-Taronna, papers as data) | Persona 3 |
| GU has no tower / `hs(lambda)` / AdS; finite content | ARGUED (repo-cited) | Persona 3 |
| local SUSY (SUGRA) is non-renormalizable => a finite-cutoff EFT, not a UV-completion | ARGUED (standard) | Persona 3 |
| tower-free Krein route is sign-blind + tree-level-only | ARGUED (repo-cited big-swing R3; Bateman-Turok tree-level) | Persona 3 |

## Honest limits

- **No absolute impossibility theorem was proved, and I do not claim one.** The kill is
  framework-conditional: it is a kill of the *UV-completing* guardian given (a) GU's stated
  super-IG-only graded structure and (b) GU's finite content. The lone surviving escape -- a
  derivative-level odd `tau_plus` embedding `eps -> D_aleph eps` connecting `Omega^1(ad)` momentum to
  physical translations -- is unbuilt and flagged non-canonical by LEG-B1; if it were built and did
  square to physical `P_mu`, the structural leg (S1) would reopen. I name it as the sole door, not as
  closed.
- **The signature and non-compact axes are EVADED, not killed.** I deliberately did not force a
  signature/non-compact no-go: every naive one dies against the Krein structure (Q1/Q2/Q3a all
  COMPUTED to evade). Reporting a clean signature kill would be manufacturing a no-go the program's
  own Krein apparatus dissolves.
- **The finite-content leg (Q3b) is ARGUED from the literature (Sagnotti-Taronna, SUGRA
  non-renormalizability) read as data, plus the repo's COMPUTED finite dimension count.** It is a
  strong structural argument, not a machine-checked theorem about GU's (unbuilt) source action.
- **The `(9,5)` here is the fiber Clifford structure over `Y14=Met(X^4)`, not physical spacetime.**
  The "5 times" argument is about the internal Krein form; I have not re-derived the physical-spacetime
  `X^4=(1,3)` RS propagation from scratch (the source action is unbuilt -- the same wall as everywhere).
- **All external results (CM, HLS, Sagnotti-Taronna, Rahman, Bateman-Turok, Stelle) are DATA.** No
  target imported; no `3`, `24`, `24-8` fit; `C2=155.3625` unchanged. Tree left dirty; no canon
  movement.

## Branch re-hypothesis (blind) and ranked next-move

**Re-hypothesis.** The guardian question has been mis-framed as "does `Sp(32,32;H)+[P,S]=0` furnish a
local SUSY guardian (yes/no)?" The red-team reframes it: **GU has no UV-completing guardian, because
(i) its constructible graded symmetry (super-IG) squares to internal `Omega^1(ad)` momentum and so is
a graded local-Lorentz/gauge symmetry, not a super-Poincare / VZ guardian, and (ii) UV-completion
needs an infinite tower GU's finite content forbids.** GU's actual and only UV-completion candidate is
therefore NOT a guardian at all but **4th-order Stelle renormalizability + Krein ghost rescue** -- a
route that is currently sign-blind and tree-level-only. The falsifiability keystone (H53's source
action) and the UV keystone are the same object, and its honest status is: finite-cutoff EFT with an
unbuilt, sign-blind UV-completion route that is renormalization-theoretic, not symmetry-theoretic.

**Ranked next-move (blind):**

1. **Decide the super-IG derivative-level embedding (the sole surviving escape).** Build the odd
   `tau_plus` `eps -> D_aleph eps` at derivative level and compute whether its `{Q,Q}` connects to
   physical `P_mu` (reviving a VZ guardian) or stays in `Omega^1(ad)` (confirming the kill). This is
   the one computation that flips S1. Highest leverage: it is a yes/no that closes or reopens the
   structural leg.
2. **Test whether 4th-order-RS is renormalizable-and-Krein-rescued the way 4th-order gravity is.**
   The RS helicity-1/2 cutoff (Rahman) is a *separate* fermionic UV problem from gravity's Stelle
   renormalizability. If a 4-derivative RS operator is power-counting renormalizable with its ghost a
   Krein partner, GU's UV route survives without a guardian; if not, the finite-cutoff verdict hardens.
3. **Make the Krein ghost rescue dynamics-derived (attack the sign-blindness).** The whole tower-free
   route rests on `[P_ghost,S]=0` being a symmetry of the actual dynamics with a real simple spectrum;
   big-swing R3 found it sign-blind at kinematic grade. A source-action-level `S` that breaks the
   K-balance would upgrade the route from tree-level-only to standing; its provable absence would be a
   second, independent kill.

## The honest GU-as-EFT cutoff (since the guardian does not UV-complete)

GU stands as a **finite-cutoff effective description** with cutoff set by the single free scale
`mu_DW` (H53's falsifiability keystone). Precisely:

- **Gravity sector:** 4th-order Stelle with a massive spin-2 companion at `m2 = sqrt(m2_eff) mu_DW`,
  `m2_eff in [5/6, 5/4]` (H25). The 5 extra DOF decouple as `(E/m2)^2` and are unexcited above the
  massive-mode scale; at natural `mu_DW ~ M_Pl` the range is `~1.8e-35 m` (H53). Renormalizable by
  power counting; unitarity contingent on the (sign-blind, tree-level) Krein rescue.
- **RS / fermion sector:** a Porrati-Rahman-type causal massive coupling valid up to the Rahman
  helicity-1/2 cutoff `Lambda`, plausibly `~ mu_DW` (Wave 34; structural link, not computed).
  Guardian-free and (per this branch) guardian-*unavailable*, so the cutoff is not removed -- only the
  numerical value of `Lambda(mu_DW)` remains to be pinned by the unbuilt source action.

So the exact cutoff of GU-as-EFT is `Lambda ~ mu_DW` in both sectors, `mu_DW` free (H53), with no
guardian to push `Lambda -> infinity`. That is the honest fallback: GU is a one-scale finite-cutoff
EFT whose only route past the cutoff is renormalization-theoretic (4th-order Krein), not
symmetry-theoretic (a guardian) -- and that route is unbuilt and sign-blind.

---

*Filed 2026-07-11. Wave 41, Branch 5 (adversarial red-team), blind to the other branches.
Reproducible: `python tests/wave41/H54b5_no_guardian_redteam.py` (exit 0, 11/11 PASS).
Exploration-grade; not promoted to canon. Tree left dirty.*
