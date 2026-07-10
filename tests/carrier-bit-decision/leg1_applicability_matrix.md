# LEG-1: Theorem-applicability matrix — the published spin-3/2 no-go record vs GU's stated commitments

**Leg of:** carrier-bit swing (carrier A = ghost-subtracted gravitino, −42 = 21σ/8, order-3 class (0,0,0);
carrier B = geometric gamma-traceless RS operator, −38 = 19σ/8, order-3 class (0,2,1)/3 NONZERO).
**Runnable checklist:** `LEG-1-applicability-matrix.py` (25/25 asserts, exit 0; exact `Fraction` arithmetic only).
**Grade:** GU-commitments + published-theorem. **Not a verdict.** The formal decider stays SG4 (the unbuilt
source action's quadratic form), per `canon/gamma-traceless-38-adjudication-RESULTS.md`.

## The three questions and their answers

| Question | Answer | Where it comes from |
|---|---|---|
| Q1: Does any published theorem make gauging **MANDATORY** for GU's spin-3/2 as stated? | **NO** | The only forcing theorems (GP-1977, GPvN-1977) each have ≥1 input hypothesis that fails against GU commitments (mass is a modulus; spacetime SUSY rejected). VZ/DW/Buchdahl/HM force background/parameter restrictions, never gauging. |
| Q2: Does any published theorem make gauging **IMPOSSIBLE** for GU? | **NO** | Nothing fetched excludes the graded-IG upstairs gauging channel (steelman S3). The in-repo 343.73 fact kills only the naive ghost-free quotient, and the "343.73 = d² commutator" identification was KILLED in-repo (`canon/source-action-seiberg-witten-construction.md:42`). |
| Q3: Does the ungauged massive vectorlike carrier **escape everything**? | **YES, within a named window** | Massive (GP/GPvN moot) + Einstein backgrounds (Buchdahl/HM satisfied on K3, the adjudicated arena) + the VZ line carrying published non-SUGRA escapes (Deser-Waldron Planck-order windows; Adler RSA; Porrati-Rahman non-minimal couplings). |

**Net:** neither forcing direction closes. What the matrix establishes: carrier A's mechanism is
**unavailable to GU-as-stated but adoptable** (the S3 door); carrier B's index/anomaly density is
**published in both math and physics registers for exactly the field-content shape GU describes**.
The bit **tilts B** at this grade — evidence, not verdict.

## The matrix

Verification tiers: **F** = fetched this session (verbatim), **C** = cached-fetched-verbatim (fetched a prior
leg, re-read this session), **S** = secondary-verbatim (primary unfetched), **U** = unverified-primary.

### Row 1 — Grisaru & Pendleton, Phys. Lett. B 67 (1977) 323 [F]

> "If massless fermions of spin 3/2 have non-vanishing low-energy couplings, the fermions must have
> massless partners of spin 2, and all particles to which the fermions couple must display supersymmetry."
> — abstract, fetched via InspireHEP API this session.

Regime: **massless**, flat 4d, S-matrix soft limit. Forces: massless spin-2 partner + SUSY of all
couplings → supergravity → carrier A's gauged reading.

Hypothesis-by-hypothesis vs GU:
- *massless* — **ESCAPES** generically. Transcript [00:46:02] L158: "because the mass is actually a
  variable"; [00:39:18 block] L128: "It's too massive and you haven't gotten enough energy to see it
  yet"; capstone (`canon/carrier-dirac-mass-capstone-RESULTS.md`): carrier vectorlike, Krein (+96,−96),
  Dirac mass ALLOWED, generically massive.
- *non-vanishing low-energy couplings* — **BITES-IF-MASSLESS**. GU cannot plead decoupling: the
  DEAD-ENDS firewall holds the bare commutator ‖[Π_RS, M_D]‖ = 58.72 nonzero (used here as a PREMISE,
  never as a reduction target). The only escape is via mass.
- *flat 4d S-matrix regime* — **PARTIAL**: GU's arena is 14d Y14/K3-fibered; the 4d effective
  identification where generations are counted is itself unbuilt.

**Row verdict: ESCAPES (generic massive branch); PARTIAL corner named** — an exactly-massless
interacting corner of the "16 flipped chiral" would re-engage the theorem with full force (steelman S2).

### Row 2 — Grisaru, Pendleton & van Nieuwenhuizen, Phys. Rev. D 15 (1977) 996 [F]

> "Kinematical constraints on helicity amplitudes determine the spin-2 and spin-3/2 Born amplitudes
> almost uniquely, and force Born amplitudes involving spin-5/2 fermions to vanish. Global supersymmetry
> is then used to determine the Born amplitudes completely. We suggest that Lorentz invariance, presence
> of only one (dimensional) coupling constant κ, and global supersymmetry lead to a unique locally
> supergauge-invariant theory of spin-2 and spin-3/2 particles." — abstract, fetched via InspireHEP API
> this session. (Full text unfetched/paywalled; abstract-tier.)

Hypothesis-by-hypothesis vs GU:
- *global supersymmetry (INPUT)* — **ESCAPES** as stated: transcript [00:46:02] L158 "We will never find
  space time Susie... Feed it the space of connections." GU's SUSY is on connection space, not a 4d
  spacetime global SUSY input.
- *massless helicity amplitudes* — **ESCAPES** (same mass escape as Row 1).
- *single dimensional coupling / Lorentz invariance* — **PARTIAL**: GU's coupling structure is the
  unbuilt SG4 object.

**Row verdict: ESCAPES at commitments grade; PARTIAL corner named** — if connection-space SUSY descends
to an effective 4d global SUSY, this theorem forces the unique supergravity → carrier A (steelman S3).

### Row 3 — Velo & Zwanziger, Phys. Rev. 186 (1969) 1337 [F; mass hypothesis PARTIAL]

> "The Rarita-Schwinger equation in an external electromagnetic potential is shown to be equivalent to a
> hyperbolic system of partial differential equations supplemented by initial conditions. The wave fronts
> of the classical solutions are calculated and are found to propagate faster than light. Nevertheless,
> for sufficiently weak external potentials, a consistent quantum mechanics and quantum field theory may
> be established. These, however, violate the postulates of special relativity." — abstract, fetched via
> InspireHEP API this session.

**The abstract does not state the mass hypothesis** → marked **PARTIAL**, confirmed via three secondaries:
- nLab "Velo-Zwanziger problem" (fetched this session): fields of "spin higher than 1" in an
  "irreducible massive representation of the Lorentz group" with "minimal coupling to electromagnetism"
  have EOM "which are not hyperbolic"; original refs PR 186:1337, PR 188:2218, NPB 43:389, PRD 9:928.
- Bekaert-Boulanger-Sundell arXiv:1007.0435 §2.5 (cached `bbs-nogo.txt`, verbatim): "the electromagnetic
  interactions exhibit pathologies (such as seemingly superluminal propagation) in Minkowski spacetime
  already for massive spin-3/2 fields."
- Deser-Waldron's framing (Row 4) treats the massive charged field as the VZ-problem carrier.

Forces: **nothing about gauging** — a pathology statement with published **non-supergravity escapes**:
- BBS §2.5 (verbatim): "the interactions between spin-3/2 and electromagnetic fields in gauged
  supergravities are well-known to avoid the Velo–Zwanziger problems" AND non-minimal couplings
  (Porrati-Rahman, BBS refs [61],[62]); also BBS quoting Weinberg (p.244): "The problems reported with
  higher spin have been encountered only for higher-spin particles that have been arbitrarily assumed to
  have only very simple interactions with external fields. No one has shown that the problems persist
  for arbitrary interactions."
- Deser-Waldron dynamical-gravity windows (Row 4).
- Adler RSA: "allowed to consistently gauge the theory beyond the supergravity approach" (PTZ, cached
  verbatim; Row 7).

Vs GU: **PARTIAL-BITES as danger** — GU's carrier is generically massive + coupled, and the author himself
names VZ ([00:41:48] L140: "Vela Zwanziger says that if you have spin three halves matter that is coupled,
to some sort of nontrivial acting group, you have to be very careful"); GU's exemption plea ("if your model
differs by having no internal symmetry groups") is weak since GU retains SU(3)×SU(2)×U(1) content. But
**the forcing-to-A route "consistency forces gauging" is REFUTED at published grade** by the non-SUGRA
escapes. Whether GU's coupling is "minimal" in VZ's sense is undetermined until SG4 — PARTIAL.

### Row 4 — Deser & Waldron, hep-th/0112182 (Nucl. Phys. B 631) [F]

> "We examine the causality and degrees of freedom (DoF) problems encountered by charged, gravitating,
> massive higher spin fields. For spin s=3/2, making the metric dynamical yields improved causality
> bounds. These involve only the mass, the product eM_P of the charge and Planck mass and the
> cosmological constant Λ. ... While propagation is causal in arbitrary E/M backgrounds, the allowed
> mass ranges of parameters are of Planck order." — abstract, fetched from arXiv this session.

Forces: **nothing** — it *opens* a window: massive charged gravitating spin-3/2 is causal **without
supersymmetry**, within Planck-order parameter ranges. **ESCAPES-ENABLING** for the ungauged massive
carrier; kills "massive spin-3/2 is fatally acausal" as a theorem. PARTIAL: the window is Planck-order
parameter ranges, not unconditional — if GU needs a sub-Planckian charged carrier outside the windows,
the shelter narrows.

### Row 5 — Buchdahl 1958 (Nuovo Cimento 10, 96) [S — via HM verbatim restatement]

> "[T]he minimally coupled equations imply R_µν γ^µ ψ^ν = 0, with R_µν denoting the Ricci curvature
> tensor, and this equation can only be satisfied by ψ ≡ 0 unless the spacetime is an Einstein spacetime
> s.t. R_µν is a constant multiple of the metric g_µν." — Hack-Makedonski, cached `hack-makedonski.txt`,
> read this session. (Buchdahl primary unfetched.)

Forces: **background restriction (Einstein), not gauging**. Vs the adjudicated arena: **ESCAPES** — K3 is
Ricci-flat hyperkähler, hence Einstein; carrier B's arena sits *inside* the published consistency window
(Homma-Semmelmann and Bär-Mazzeo study exactly the ungauged RS operator there; RS(K3) = 38 sharp).
Named gap: GU's effective *Lorentzian* backgrounds off-K3 are not certified Einstein.

### Row 6 — Hack & Makedonski, arXiv:1106.6327 (Phys. Lett. B) [C]

> "In this work we analyse whether it is possible to couple a spin 3/2-field to a gravitational field in
> such a way that the resulting quantum theory is consistent on arbitrary gravitational backgrounds. We
> find that this is impossible as all couplings require the background to be an Einstein spacetime for
> consistency." And: "our proof covers both m > 0 and m = 0." And (discussion): "the model is, at best,
> only consistent on Einstein spacetimes." — cached `hack-makedonski.txt`, verbatim, read this session.

Forces (as THEOREM): Einstein background — again a background restriction, **not a gauging requirement**.
The supergravity attribution is **discussion-tier**, quoted honestly for the steelman:

> "This enforces the widespread belief that supergravity theories are the only meaningful models which
> contain spin 3/2 fields as in these models such restrictions of the gravitational background appear
> naturally as on-shell conditions."

**Row verdict: ESCAPES as theorem (K3 Einstein); PARTIAL as discussion** (steelman S5). Named gap: every
consistency no-go here is a *Lorentzian* propagation/quantization statement while the adjudicated indices
are *Riemannian-elliptic* on K3 — that bridge is program semantics (SG4), not a fetched theorem.

### Row 7 — The anomaly-convention pair (answers the swing's anomaly question) [C]

**Gauged-gravitino register (carrier A, −21, −42):**
- Bilal arXiv:0802.0634, eq (11.47) context (cached `bilal.txt`, verbatim): a positive-chirality spin-3/2
  field "is obtained from a positive chirality spin-1/2 field with an extra vector index by subtracting
  the spin-1/2 part"; and "in the cases of interest, the spin-3/2 gravitino is not charged under the
  gauge group and the factor of ch(−F) then is absent in (11.47)."
- HS Remark 3.6 (cached `hs_paper.txt`, verbatim): "In applications of the Rarita-Schwinger operator in
  supergravity and superstring theory, the index of the Rarita-Schwinger operator is calculated as
  ind D_TM − ind D. This is motivated by the necessity of 'discarding zero modes that can be gauged away
  or that violate gauge conditions'. These are 'cancelled by zero modes of the spin 1/2 ghost fields'."
  (quoting Witten [43], p. 252).
- PTZ eq (1.3) (cached `ptz-rsa.txt`, verbatim): "the factor in the anomaly is −21 times larger compared
  to the anomaly for Dirac field."

**Ungauged register (carrier B, −19, −38):**
- HS eq (11) (verbatim): "ind Q = Â(TM)(ch(TM_C) + 1)[M] = ind D_TM + ind D"; Prop 3.1(i): "n = 4:
  ind Q = −19 Â(M) = 19/8 σ(M)" — the ch(T)+1 density published for the **ungauged geometric operator**.
- PTZ conclusion (verbatim): "We have calculated the gravitational chiral anomaly for the extended
  Rarita-Schwinger-Adler model for spin 3/2 fields and found that it is −19 times larger than the
  standard anomaly for spin 1/2." Bookkeeping (verbatim): "−19 = −21 + 2" (eq 5.1); "the factor −21 in
  (1.3) can be obtained as −21 = −20 − 1, where −20 is the 'ghostless' contribution and −1 is the
  contribution of the ghosts. Now, the −19 factor could be obtained by adding the ghostless contribution
  and the contribution of spin 1/2, i.e. −19 = −20 + 1" (eq 5.2).
- The RSA model is spin-3/2 matter with "a nontrivial chirally symmetric interaction with an additional
  spin 1/2 field," which "allowed to consistently gauge the theory beyond the supergravity approach"
  (PTZ intro, verbatim; refs Adler PRD 92 (2015) 085022, PRD 97 (2018) 045014, Adler-Pais PRD 99 (2019)
  095037).

**So the swing's anomaly question is answered YES:** the ch(T)+1 / 19σ/8 density IS published for a
non-gauged spin-3/2 system, in both math and physics registers — and the physics register (RSA) is
structurally the same field-content shape as GU's stated mechanism (transcript [00:39:18] L128: the
spin-1/2 slot enters ADDED, "plus spinners on v, tensor spinners on w. So that's where you get your third
generation of matter from"). Ghost subtraction (−21) remains tied by both sources to gauge conditions and
ghost fields. Named caveats: AGW primary (NPB 234) paywalled — the −21 attribution rides verbatim
secondaries; the −19 rides one paper family (Adler 2015-2019 + PTZ 2022); PTZ's own footnote flags "The
tachyon mode from LLL requires the separate investigation."

## GU's commitments used (all line-verified this session in `papers/drafts/Transcript into the impossible.md`)

- **Matter, not gauge field** (4 independent ways): [00:32:46] L107 (one-form-spinor slot = SM fermion
  content); [00:39:18] L128 (third generation of MATTER); [00:40:27] L131 ("one family of 16 flipped
  chiral spin three halves particles... just the conjugate of the internal symmetry representation");
  [00:41:48] L140 (VZ-exemption plea = ungauged-matter framing). **Negative (grep, this session): 0 hits**
  for "gravitino", "ghost", "gauge fix"; no δψ = Dε ever stated.
- **No spacetime SUSY**: [00:46:02] L158 "We will never find space time Susie... Feed it the space of
  connections. Then the Lorentz group is the gauge group."
- **Mass is a modulus**: [00:46:02] L158 "the mass is actually a variable"; L128 "It's too massive and
  you haven't gotten enough energy to see it yet"; capstone: vectorlike, Dirac mass ALLOWED.
- **Coupled, never decoupled**: DEAD-ENDS acausal-trap firewall (bare ‖[Π_RS, M_D]‖ = 58.72 stays
  nonzero; premise only).
- **Graded-IG upstairs**: [00:49:16] L173 "you take the inhomogeneous gauge group on that group and you
  extend it to through supersymmetry... the entire universe without making any choices" — the live
  unconventional gauging channel (shape tagged gu_derived in
  `explorations/vz-evasion/rs-gu-phys-brst-specification-2026-06-26.md:61-63`; unbuilt in fact).

## Carrier-A steelman ledger (all carried OPEN; the tilt is invalid without them)

- **S1 — massive ≠ ungauged.** A super-Higgsed/Stueckelberg gravitino keeps its local invariance and
  ghost bookkeeping through the Higgsing; the capstone's mass-allowed finding is super-Higgs-compatible;
  the author name-checks the Stueckelberg trick ([00:23:02] L80). A mass term never selects B by itself.
- **S2 — the massless chiral corner.** If any of the "16 flipped chiral" is genuinely massless and
  interacting at tree level in the 4d soft regime, GP-1977 bites with full force → SUSY couplings +
  spin-2 partner → the gauged reading, hence A. Non-mandated by commitments, not excluded either.
- **S3 — the Y14 upstairs gauging (the named GU-native A-door).** The graded-IG odd generators are
  locally parametrized; their τ⁺-twisted action is ε → D_ℵ ε — the gravitino shape. Nothing fetched
  excludes a 14d fibered construction whose odd-IG invariance descends and ghost-subtracts with no
  spacetime SUSY. If SG4 lands there, carrier A stands with the transcript intact, and GPvN's forcing
  becomes available through the descended global SUSY.
- **S4 — anomaly-by-field-content.** PTZ's −19 is a property of Adler's specific model; GU's spin-1/2
  slot has a different origin (RS branching). Which spin-1/2 completes vs cancels is pinned only by the
  unbuilt quadratic form — this steelman collapses into SG4 rather than escaping it.
- **S5 — HM's discussion, hostile reading.** "supergravity theories are the only meaningful models which
  contain spin 3/2 fields" — quotable as evidence that any consistent completion is supergravity-shaped.
  Discussion-tier, carried verbatim.
- **S6 — the VZ guard cuts A's way too.** The Einstein-window escape is background-restricted, and
  DEAD-ENDS forbids the cheap decoupling fix; if the dressed obstruction cannot be tamed without a
  guardian symmetry, the guardian symmetry IS the gauging, and A follows.

## Careful-reader corrections carried (anti-story-shopping)

1. The task brief's "343.73 = gauge-orbit obstruction on Cl(9,5)" is a machine fact ONLY as "RS symbol
   on pure-gauge image norm = 343.73 → annihilated? False" (`rs-gu-phys-brst-specification-2026-06-26.md:113`)
   — it kills the *naive ghost-free quotient*, not gauging; the spec itself: "the machine fact rules out
   the easy subtraction but does not prove a ghost complex is the unique resolution." The
   "343.73 = d² commutator" identification was KILLED (`canon/source-action-seiberg-witten-construction.md:42`).
   Treating 343.73 as a machine refutation of carrier A would be story-shopping.
2. The ghost-parity no-go (`canon/swing-ghost-parity-no-chiral-selection.md:40`) concerns the KREIN
   (Turok-Bateman) ghost parity, not BRST gauge ghosts — it does not bear on gauging availability.
3. No leg computation moves the bare commutator 58.72 or targets any obstruction reduction; the
   58.72 nonvanishing is used only as the anti-decoupling premise in Row 1.
4. Â(K3) = −σ/8 = 2 computed from σ = −16 only; no χ(K3), no Â=3, no /8 manufacture (asserted in script).

## Named risks / what would move the matrix

1. **SG4 resolution either way** — a stabilized action with a local fermionic invariance (spacetime or
   τ-descended) makes A's mechanism available and the tilt evaporates by design; an explicit added
   physical spin-1/2 quadratic term hardens B past this grade.
2. **The massless hypothesis engaging** — proof that GU's 16 must be massless AND interacting in a flat
   4d soft regime lets GP/GPvN force the supergravity coupling structure (→ A).
3. **RSA anchor weakening** — −19 rides one paper family; an inconsistency demonstration or
   regularization-dependence would drop B's physics register to math-only (HS/BM stand regardless).
4. **Verbatim gaps** — GPvN and VZ are abstract/secondary-tier; Buchdahl rides HM; AGW and Duff/
   Christensen-Duff primaries unfetched. A primary-text surprise could shift a row.
5. **The Lorentzian–Riemannian bridge** — all fetched consistency no-gos are Lorentzian; the adjudicated
   indices are Riemannian-elliptic on K3. The identification is program semantics (SG4), not a theorem.
6. **Deser-Waldron window narrowing** — a sub-Planckian charged carrier on non-Einstein effective
   backgrounds would lose the published consistency shelter.

## Sources

- Grisaru & Pendleton, Phys. Lett. B 67 (1977) 323 — InspireHEP API, abstract verbatim, fetched this session.
- Grisaru, Pendleton & van Nieuwenhuizen, Phys. Rev. D 15 (1977) 996 — InspireHEP API, abstract verbatim, fetched this session.
- Velo & Zwanziger, Phys. Rev. 186 (1969) 1337 — InspireHEP API, abstract verbatim, fetched this session.
- Deser & Waldron, hep-th/0112182 — arXiv abstract, verbatim, fetched this session.
- nLab, "Velo-Zwanziger problem" — fetched this session.
- Bekaert, Boulanger & Sundell, arXiv:1007.0435 — cached `bbs-nogo.txt` (fetched prior leg), §2.5 verbatim re-read.
- Hack & Makedonski, arXiv:1106.6327 — cached `hack-makedonski.txt` (fetched prior leg), verbatim re-read.
- Prokhorov, Teryaev & Zakharov, Phys. Rev. D 106 (2022) 025022, arXiv:2202.02168 — cached `ptz-rsa.txt`, verbatim re-read.
- Homma & Semmelmann, arXiv:1804.10602 — cached `symbol-swing/hs_paper.txt`, verbatim re-read (eq (11), Prop 3.1(i), Remark 3.6).
- Bilal, arXiv:0802.0634 — cached `symbol-swing/bilal.txt`, verbatim re-read (eq (11.47) context).
- In-repo: `canon/gamma-traceless-38-adjudication-RESULTS.md`, `canon/carrier-dirac-mass-capstone-RESULTS.md`,
  `canon/swing-ghost-parity-no-chiral-selection.md`, `canon/source-action-seiberg-witten-construction.md`,
  `explorations/vz-evasion/rs-gu-phys-brst-specification-2026-06-26.md`, `absorbed/gu-source-action/DEAD-ENDS.md`,
  `papers/drafts/Transcript into the impossible.md` (all read/grep-verified this session).
- Unfetched primaries (named): Alvarez-Gaumé & Witten NPB 234 (1984); Buchdahl Nuovo Cimento 10 (1958) 96;
  Christensen-Duff / Duff 1982; GPvN and VZ full texts (paywalled).
