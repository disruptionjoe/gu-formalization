# LEG-3: UNGAUGED-CONSISTENCY — is carrier B itself consistent as GU matter?

Companion analysis to `LEG-3-ungauged-consistency.py` (64/64 checks, exit 0, this session).
Every quote below is needle-verified against the cached/fetched source by the script.
Grades used: EXACT (machine, sympy rational), VERIFIED (verbatim fetched/cached text),
PARTIAL (hypothesis-match with named gap), BLOCKED (named missing input).

Guards: no repo dynamics touched (bare ||[Pi_RS, M_D]|| = 58.72 untouched — the 4d VZ model
below is the standalone published system, not the repo substrate); no chi(K3), no A-hat=3,
no manufactured /8; carrier-A steelman carried per finding; verdict authority stays SG4.

---

## (i) RIEMANNIAN SIDE — carrier B's home turf is published, unconditional mathematics. VERIFIED.

**The operator is defined with no gauge structure anywhere.** Homma–Semmelmann
(arXiv:1804.10602, Sec. 2): "The operator Q : Γ(S3/2) → Γ(S3/2) with Q = pr_{S3/2} ∘
D_TM|Γ(S3/2) is called Rarita-Schwinger operator." and "In the physics literature a
Rarita-Schwinger field is a section ψ of S3/2 satisfying the equations P∗ψ = 0 and Qψ = 0."
The gamma-trace constraint (S3/2 = ker of Clifford multiplication) is **definitional of the
bundle**, not a gauge-fixing residue. Bär–Mazzeo (arXiv:2003.11255, abstract): "The
Rarita-Schwinger operator is the twisted Dirac operator restricted to 3/2-spinors.
Rarita-Schwinger fields are solutions of this operator which are in addition divergence-free."

**The index side needs no curvature hypothesis at all.** HS Sec. 3 opens: "In this section we
do not have to assume the metric g to be Einstein," and eq (11): "ind Q = Â(TM)(ch(TM_C) +
1)[M] = ind D_TM + ind D" — the ch(T)+1 (carrier-B) bookkeeping is the published index of this
operator on ANY compact even-dim spin manifold. Prop 3.1(i): "n = 4 : ind Q = −19 Â(M) = 19/8
σ(M)."

**K3 specifically is a fully solved, sharp example.** HS Sec. 4.7: "hyperkähler manifolds are
spin, Ricci-flat and Q² coincides with the standard Laplace operator Δ_{S3/2}." HS Example (1)
to Prop 4.6: "n = 2 : then M is a K3 surface and it follows from Proposition 4.6 that
dim ker Q = 2h^{1,1} − 2 = 38. In this case the space of Rarita-Schwinger fields is isomorphic
to two copies of the space of harmonic primitive (1,1)-forms." Bär–Mazzeo Rem 5.3: "This is
sharp; indeed RS(K3) = 38." EXACT coherence check (script A6): (19/8)·σ(K3) = (19/8)(−16) =
−38 = ind Q = −(dim ker Q) — published formula times published signature, reproducing canon's
carrier-B row; nothing manufactured.

**Ghost subtraction is named by the same source as the OTHER convention — supergravity's.**
HS Rem 3.6: physics computes "ind D_TM − ind D" motivated by "discarding zero modes that can
be gauged away or that violate gauge conditions," "cancelled by zero modes of the spin 1/2
ghost fields" (quoting Witten [43] p. 252). So the mathematics literature itself contrasts:
ungauged geometric operator → ch(T)+1 (carrier B); gauged gravitino → ch(T)−1 (carrier A).

**Curved-background consistency window (Lorentzian caveat carried honestly):** Hack–Makedonski
(arXiv:1106.6327, abstract): "We find that this is impossible as all couplings require the
background to be an Einstein spacetime for consistency," restating Buchdahl (Nuovo Cim. 10
(1958) 96): the minimally coupled equations "can only be satisfied by ψ ≡ 0 unless the
spacetime is an Einstein spacetime." K3 is Ricci-flat, hence Einstein: carrier B's Riemannian
arena sits INSIDE the published consistency window. This is a background restriction, not a
gauging requirement.

**Conclusion (i):** carrier B's operator, index density (19σ/8), and K3 kernel are published,
well-defined, unconditional mathematics — VERIFIED at published-theorem grade. Carrier-A note:
none of this selects B; the same sources publish the ghost-subtracted convention for the
gauged reading (HS Rem 3.6). The Riemannian result says B's arithmetic is legitimate, not that
GU's action uses it.

---

## (ii) LORENTZIAN/DYNAMICAL SIDE — what VZ requires, what GU presents, and the exact finite computation.

### What Velo–Zwanziger acausality requires (published hypotheses, verbatim)

- nLab (fetched this session): the problem hits fields which "have spin higher than 1," "are
  in an irreducible massive representation of the Lorentz group," and "have minimal coupling
  to electromagnetism" — then the EOM "tend to have equations of motion which are not
  hyperbolic." Original: Velo–Zwanziger, Phys. Rev. 186 (1969) 1337 (primary paywalled;
  hypotheses ride nLab + the two fetched restatements below — PARTIAL at primary level, but
  double-covered at secondary level).
- Porrati–Rahman (arXiv:0906.1432, fetched full text): "minimal coupling to external
  electromagnetic fields resulted in equations of motion which exhibited faster-than-light
  propagation of signals [4]" and "the original Velo-Zwanziger problem ... manifests itself
  already for constant backgrounds [4]."
- Deser–Pascalutsa–Waldron (hep-th/0003011, fetched full text): "Truncated supergravity
  (l2 = 1/2, l5 = 0) and minimal coupling (l1 = l2 = l5 = 0) have critical field values
  B² = 3m⁴/e² and B² = (3m²/2e)², respectively (the latter being the well known result of
  [5, 6])" — [5] Johnson–Sudarshan 1961, [6] Velo–Zwanziger PR 186, 1337.

So VZ requires: MASSIVE + spin 3/2 + MINIMAL coupling to a nontrivial (EM-type) background.
It does NOT require gauging, and it does not force supergravity by itself.

### The exact finite computation (script Parts B–C, all sympy-exact, 4d Dirac representation)

1. **Free massive ungauged RS is self-constraining matter** (B2): operator calculus with
   [D_μ, D_ν] = ieF_{μν} gives, uniquely (c = ia/2, both mass signs, mass-sign independent):
   D·R + (ia/2) m γ·R = −(e/2) γ^{μνρ}F_{μν}ψ_ρ + (3i/2) m² γ·ψ.
   All second- and first-derivative terms cancel IDENTICALLY. At F = 0 this forces γ·ψ = 0
   exactly — **the free massive ungauged theory enforces carrier B's field space (ker Γ)
   on-shell, with no gauge symmetry anywhere**. Free DOF certificate (B3): exactly 4
   polarizations per energy sign, all gamma-traceless and transverse. EXACT.

2. **Minimal coupling twists the constraint off ker Γ** (B2d): for F ≠ 0, γ·ψ =
   −(ie/3m²)γ^{μνρ}F_{μν}ψ_ρ ≠ 0. GU cannot both couple this sector minimally and keep the
   gamma-traceless field space on-shell. EXACT.

3. **The VZ characteristic degeneracy, reproduced exactly** (C1–C4): jump analysis
   [∂_νψ_ρ] = ξ_νΨ_ρ. At timelike ξ = (1,0,0,0): ker(J1) is EXACTLY the 4-dim longitudinal
   modes Ψ_ρ = ξ_ρ ε, and ker(J1) ∩ ker(Γ) = 0 — **every candidate acausal front carries
   nonzero gamma-trace, i.e. lives outside carrier B's field space**. Null-ξ control: kernel
   jumps to 6 (genuine light-cone characteristics). On a constant magnetic background
   (minimal coupling), the constraint-restricted critical matrix has
   det K(B) = (9/4 m⁴ − e²B²)², with real zeros exactly at **|B| = 3m²/(2e)** — matching
   DPW's verbatim "the well known result of [5, 6]" (= VZ's primary). Full stacked jump
   system: rank 16 subcritical (no timelike front), rank 14 at critical (nonzero timelike
   jump exists). EXACT, matching published.
   Scope honesty: the machine claim is the degeneracy locus of the timelike-normal
   constraint system; the statement that fronts are strictly superluminal already below
   critical field is VZ's published claim (PR verbatim above), not re-derived here.

### Does GU-as-stated present the VZ trigger? Rep-content YES; coupling prescription BLOCKED.

- MASSIVE: canon capstone — "The carrier Dirac mass is ALLOWED, generically massive — not
  forbidden, not protected"; transcript [00:46:02] "because the mass is actually a variable";
  [00:39:18 block] "It's too massive and you haven't gotten enough energy to see it yet."
  Massive branch live. VERIFIED.
- CHARGED under a nontrivially acting group: [00:40:27] the 16 is "just the conjugate of the
  internal symmetry representation" and "Some of these things will be electrically neutral,
  but lots of them won't be." **The author's own escape plea — [00:41:48] "if your model
  differs by having no internal symmetry groups, I have no idea whether it has any kind of a
  Velo Zwanziger problem" — is not available to GU-as-stated: its own spin-3/2 family carries
  internal and electric charge by the author's own description.** VERIFIED (transcript-tier).
- MINIMAL coupling: nowhere stated. This is precisely SG4 (no source action). **BLOCKED —
  named missing input: GU's coupling prescription for the spin-3/2 sector (minimal vs
  non-minimal), which only the unbuilt source action can supply.**

### The published escape fork IS the carrier fork (the leg's sharpest structural finding)

Both published escapes from VZ exist, and they map one-to-one onto the two carriers:

- **Ungauged escape (carrier-B-shaped):** Porrati–Rahman: "We present a Lagrangian for a
  massive, charged spin 3/2 field in a constant external electromagnetic background, which
  correctly propagates only physical degrees of freedom inside the light cone... No
  additional fields or equations besides the spin 3/2 ones are needed to solve the problem."
  Mechanism: "The crucial property of our construction is that the standard
  gamma-tracelessness constraint γ·ψ = 0 is enforced exactly," whereupon the system reduces
  "to a standard, manifestly causal Dirac form." **The published causality-restoring
  structure for ungauged massive charged spin-3/2 is exact enforcement of carrier B's
  defining constraint.** Consistent with the exact computation: acausal fronts are
  longitudinal with nonzero gamma-trace (C1b), so exact γ-tracelessness removes them.
- **Gauged escape (carrier-A-shaped):** N=2 gauged supergravity / dynamical gravity.
  PR: "Causality in this case is due to gravitational back-reaction"; Deser–Waldron
  (hep-th/0112182 abstract, fetched): "For spin s=3/2, making the metric dynamical yields
  improved causality bounds... While propagation is causal in arbitrary E/M backgrounds, the
  allowed mass ranges of parameters are of Planck order."

**Conclusion (ii):** carrier B is NOT fatally acausal as GU matter: the massive ungauged
sector is published-viable (PR construction; DW windows), and its defining constraint is
exactly the published cure. But the viability is conditional: it requires the action to
enforce γ·ψ = 0 exactly (non-minimal couplings — PR), which GU nowhere states. VZ bites the
minimal reading above |B| = 3m²/(2e). Which escape GU takes is the SG4 bit itself.

Carrier-A steelman on (ii), intact: (a) PR's rescue is constant-background only ("Our method
will work for constant backgrounds. While this is a drawback...") — no published ungauged
rescue covers arbitrary backgrounds, while the supergravity escape does (within Planck-order
windows); (b) for fixed sub-Planckian charge, PR verbatim: "the gravitational back-reaction
of spin 3/2 particles much lighter than O(eMPl) is negligible, so they can still propagate
superluminally" — the generic light charged ungauged spin-3/2 remains sick, and the only
fully general published cure is the gauged/gravitating one; (c) if SG4's action is minimal,
the ungauged reading inherits VZ and the consistent completions on record are
supergravity-shaped (Hack–Makedonski discussion: supergravity as "the most prominent
solution"), i.e. carrier A.

---

## (iii) THE MASSLESS-CHIRAL TENSION — "16 flipped chiral" vs the vectorlike carrier. Reading fork; parked on SG4.

Facts in tension (all needle-verified):
- Transcript [00:40:27]: "one family of 16 flipped chiral spin three halves particles."
- Canon capstone: carrier "vectorlike: Krein signature exactly (+96, −96), net chirality 0";
  Dirac mass "ALLOWED, generically massive"; "the massive case decouples to ZERO net chiral
  generations, not three."

Reconciliation options, stated honestly (no computation can pick one):

1. **"Flipped chiral" = internal conjugation (author's own gloss).** The very next sentence
   [00:40:27]: the family "aside from being spin three halves is just the conjugate of the
   internal symmetry representation." On this reading "flipped chiral" names the internal-rep
   flip, not net spacetime chirality — no contradiction with the vectorlike measurement.
   Cheapest reconciliation; transcript-internal; costs nothing.
2. **Chirality as a small-VEV emergent property.** [00:46:02]: "the fermionic extension gives
   you exactly three families of chiral fermions if you have a decreased VEV ... because the
   mass is actually a variable." The vectorlike carrier sits at the generic massive point; the
   chiral appearance is the light limit. Honest cost, from the capstone itself: because the
   carrier is vectorlike, any nonzero mass decouples to ZERO net chiral generations — the
   light-limit chirality is a located modulus, not forced. This reading keeps carrier B but
   concedes the generation count is not protected (already canon).
3. **Genuine spacetime-chiral massless reading — the carrier-A door.** If the 16 is
   spacetime-chiral and massless-interacting at tree level, Grisaru–Pendleton (PLB 67 (1977)
   323, InspireHEP abstract fetched this session, verbatim) bites: "If massless fermions of
   spin 3/2 have non-vanishing low-energy couplings, the fermions must have massless partners
   of spin 2, and all particles to which the fermions couple must display supersymmetry."
   That forces the supergravity coupling structure whose index bookkeeping is the
   ghost-subtracted gravitino — carrier A — and collides with [00:46:02] "We will never find
   space time Susie" unless the SUSY is realized upstairs (the tau/space-of-connections door,
   Design 2's steelman (i)). On this reading the transcript's own words pull toward A.

**Conclusion (iii):** the tension does not resolve toward either carrier. Option 1 dissolves
it verbally (B-compatible), option 2 keeps B at the cost canon already booked (zero net chiral
generations when massive), option 3 is a live A-door. Which option GU's action realizes is,
again, SG4.

---

## BOTTOM LINE OF THE LEG

Carrier B is CONSISTENT as GU matter, at two grades:
- Riemannian/index grade (where the adjudicated −38 actually lives): unconditional,
  published, sharp (HS eq (11), Prop 3.1(i), Prop 4.6 Ex. (1); BM Rem 5.3). VERIFIED + EXACT.
- Lorentzian/dynamical grade: conditionally viable — massive, Einstein-window, and the
  defining gamma-trace constraint is the published causality cure (PR), with the exact finite
  computation reproducing the published VZ critical field |B| = 3m²/(2e) and showing acausal
  fronts are precisely the modes OUTSIDE ker(Γ). PARTIAL: viability requires exact constraint
  enforcement (non-minimal couplings) or neutrality, neither stated by GU; constant
  backgrounds only.

Neither forcing direction closes: "ungauged spin-3/2 is fatally acausal, so gauging (carrier
A) is forced" is REFUTED for the massive sector by PR/DW at published-theorem grade; "carrier
B is unconditionally consistent" is NOT established (coupling prescription BLOCKED on SG4;
the general-background cure on record is the gauged one). The bit stays on SG4 — per canon:
"Selection authority moved to SG4"; "treating that smell as a verdict would be story-shopping."

Named missing inputs (BLOCKED items): (1) GU's spin-3/2 coupling prescription (minimal vs
non-minimal — decides whether VZ bites); (2) VZ primary text (PR 186 paywalled; hypotheses
ride nLab + PR + DPW verbatim secondaries); (3) whether GU's internal symmetry is dynamically
gauged with the 16 minimally charged (rep-content says charged; the coupling is unbuilt).
