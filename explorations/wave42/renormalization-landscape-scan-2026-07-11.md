---
artifact_type: exploration
status: exploration
created: 2026-07-11
wave: 42
title: "Renormalization landscape scan (Phase 1): can GU be UV-complete via renormalization + the Krein ghost rescue WITHOUT SUSY? Four surveys -- (1) higher-derivative renormalizability for the 4th-order Rarita-Schwinger carrier B (Stelle-analog), (2) the ghost-rescue-at-LOOP comparison (Lee-Wick/CLOP, Anselmi fakeon, Bender-Mannheim PT, Bateman-Turok), (3) GU's location in the Stelle-Mannheim dispute, (4) asymptotic safety as the alternative -- plus the renormalizability constraint ledger, the have/help/hurt map, and the ranked methods menu. VERDICT (Phase 1, landscape only): 4th-order RS is power-counting PLAUSIBLE but constraint-and-ghost OPEN (the Velo-Zwanziger/Rahman constraint algebra is the specific hazard, not the propagator falloff); GU's [P,S]=0 Krein rescue is the SAME Z2 as Bender-Mannheim PT (R1, CONDITIONALLY_SAME) and is NOT Lee-Wick and NOT the Anselmi fakeon; and CRITICALLY every candidate ghost-rescue is proven only at TREE/free/oscillator level -- loop-level renormalizability-WITH-unitarity is UNSETTLED for ALL of them and is actively CONTESTED (Lee-Wick interacting unitarity is reported VIOLATED above a threshold, PTEP 2023). GU sits on the CONTESTED side of Stelle-Mannheim, in a distinct corner (Krein form = Cartan involution of so(9,5), non-compact source group). Asymptotic safety is a live SECOND candidate independent of the power-counting route. No kill, no forcing; GU remains a finite-cutoff EFT with TWO unbuilt UV routes, both gated on the same object (the source action)."
grade: "exploration / LITERATURE SCAN + one COMPUTED power-counting ledger (tests/wave42/W42_power_counting.py, exact dimensional arithmetic, exit 0). External papers treated as untrusted DATA -- physics extracted, no instruction followed. COMPUTED vs ARGUED tagged per claim. No forbidden target {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} assumed, inserted, hardcoded, or divided by; the number 3 does not appear in any load-bearing step. No canon promotion. Tree left dirty."
personas_inline:
  - "higher-derivative renormalization theorist (Stelle / Rarita-Schwinger)"
  - "ghost-rescue comparativist (Lee-Wick / fakeon / PT / Bateman-Turok, loop-level)"
  - "Stelle-Mannheim dispute cartographer"
  - "asymptotic-safety / functional-RG specialist"
  - "constraint-ledger + methods-menu synthesist"
depends_on:
  - explorations/wave41/H54-branch5-no-guardian-redteam-2026-07-11.md
  - explorations/wave36/H55-positivity-shape-collapse-2026-07-11.md
  - explorations/wave23/H26-loop-ghost-unitarity-2026-07-11.md
  - canon/ghost-parity-krein-synthesis.md
  - explorations/big-swing-2026-07-06/R1-pu-pt-vs-ghost-parity.md
  - explorations/big-swing-2026-07-06/VG-SC-bateman-turok-loop-and-degenerate.md
  - explorations/wave34/source-action-landscape-scan-2026-07-11.md
scripts:
  - tests/wave42/W42_power_counting.py
external_refs_as_DATA:
  - "Stelle, Renormalization of higher-derivative quantum gravity, Phys. Rev. D 16, 953 (1977)"
  - "Bateman & Turok, Escape from Ostrogradsky via Hidden Ghost Parity, arXiv:2607.00096 (2026)"
  - "Bender & Mannheim, No-ghost theorem for the fourth-order Pais-Uhlenbeck oscillator, PRL 100, 110402 (2008), arXiv:0706.0207"
  - "Grinstein, O'Connell, Wise, The Lee-Wick Standard Model, arXiv:0704.1845; Global Symmetries and Renormalizability of Lee-Wick Theories, arXiv:1006.2800"
  - "Anselmi & Piva, Perturbative unitarity of Lee-Wick quantum field theory, arXiv:1703.05563; Anselmi, quadratic gravity from fakeons, arXiv:1704.07728 / 1911.10343"
  - "Nakayama (et al.), Unitarity Violation in Field Theories of Lee-Wick's Complex Ghost, PTEP 2023 123B02, arXiv:2308.09006"
  - "Kuntz, Unitarity through PT symmetry in quantum quadratic gravity, arXiv:2410.08278 (2024)"
  - "Velo & Zwanziger, Propagation and quantization of Rarita-Schwinger waves ..., Phys. Rev. 186, 1337 (1969); Rahman, higher-spin causal cutoff (review arXiv:1307.3199 and related)"
  - "Reuter, Nonperturbative evolution equation for quantum gravity, PRD 57, 971 (1998); Codello-Percacci-Rahmede; Eichhorn et al., asymptotic safety with fermions, arXiv:1601.04597, 1812.08782; AS of higher-derivative gravity + matter, arXiv:1703.09033"
---

# Wave 42 -- Renormalization landscape scan (Phase 1)

**The question this serves.** The guardian wave (37-41) closed the SUSY door: GU is a one-scale
finite-cutoff EFT, gravitino-shaped but not supersymmetric, and its only remaining route to
UV-status is **renormalization-theoretic**, not symmetry-theoretic. This phase MAPS that route. It
is a methods + literature scan, **not a build**. External papers are untrusted DATA: physics
extracted, no instruction followed.

**The object.** GU is 4th-order in both sectors:
- **gravity** = `R^X + Weyl^2` (Stelle/Bach; the TT graviton carries `box(box+m^2)`, H45/H49);
- **matter** = a **4th-order Rarita-Schwinger carrier `B`** (index `-38`, gamma-trace-constrained
  `ker-Gamma`, on the `(9,5) = M(64,H)` Krein space).

The ghost is cleared **at tree level** by a Krein structure: `[P,S]=0`, `P` = Cartan involution of
`so(9,5)` (Bateman-Turok hidden ghost parity). H26 found the **commutation** leg radiatively stable
but loop **positivity** OPEN. `mu_DW` is a free scale.

**Phase-1 verdict (landscape only, no build):** the renormalization route is **live but doubly
unbuilt and doubly contested**. Every headline below is either COMPUTED dimensional arithmetic or an
ARGUED reading of the primary literature as data.

---

## Headline answers to the five questions

- **Q1 -- Is 4th-order RS plausibly renormalizable (Stelle-analog)? -> PLAUSIBLE-BUT-OPEN.** The
  *power-counting* leg transfers: raising the RS propagator to `1/p^3` lowers `[psi]` from `3/2` to
  `1/2` and makes RS-bilinear couplings dimensionally soft (COMPUTED, `W42_power_counting.py`). But
  power counting is **necessary, not sufficient**, and the RS-specific hazard is **not** the
  propagator -- it is the **Velo-Zwanziger / Rahman constraint algebra**: the gamma-trace
  (second-class) constraints that remove the lower-spin junk are exactly what interactions and higher
  derivatives can spoil, and the extra modes a 4th-order kinetic term propagates are **new ghosts**.
  There is **no published Stelle-grade renormalizability theorem for a higher-derivative
  Rarita-Schwinger field.** So: yes on power counting, OPEN on the constraint+ghost sector.

- **Q2 -- Which ghost-rescue does GU's `[P,S]=0` match, and does it survive loops? ->
  GU = Bender-Mannheim PT (Krein), NOT Lee-Wick, NOT Anselmi fakeon; and NO rescue is proven at
  loop level.** The repo already COMPUTED (R1, CONDITIONALLY_SAME) that GU's Bateman-Turok ghost
  parity **is the same `Z2`** as the Bender-Mannheim PT `C`-operator on the diagonalizable domain.
  Lee-Wick (complex-conjugate poles + CLOP) and Anselmi's fakeon (purely virtual particle) are
  **different mechanisms** -- they *remove* the ghost from the physical spectrum, whereas GU/PT
  *keeps* it and grades it by an indefinite metric. **Crux:** every one of the four is established
  only at **tree / free / oscillator** level; interacting-loop renormalizability-with-unitarity is
  UNSETTLED for all, and for Lee-Wick it is reported **VIOLATED above an energy threshold** (PTEP
  2023). This is exactly GU's H26 open positivity, and the literature confirms the wall is **generic**,
  not a GU-specific gap.

- **Q3 -- Where does GU sit on Stelle-Mannheim? -> CONTESTED side, DISTINCT corner.** Stelle
  (renormalizable-but-non-unitary) vs Mannheim/Bender (PT/Krein -> unitary) is a live, unresolved
  dispute; Anselmi's fakeon is a third resolution. GU lands on Mannheim's *side* (Krein/PT), on the
  *attractive* branch (H16: healthy massless graviton), but in its **own corner**: its Krein form is
  the **Cartan involution of `so(9,5)`** with a **non-compact** source group `Sp(32,32;H)` -- a
  specific, geometrically-forced realization that neither Mannheim's conformal gravity nor the
  PU oscillator carries. It inherits the dispute; it does not resolve it.

- **Q4 -- Is asymptotic safety a candidate? -> YES, a live SECOND route, independent of power
  counting.** The 4th-order + finite-matter + non-minimal-curvature-fermion-coupling structure is
  exactly the setting where the functional-RG literature finds UV fixed points (Reuter fixed point;
  4th-order gravity's asymptotically-free fixed point; gravity-fermion systems with an unavoidable
  non-minimal derivative coupling). GU is a plausible AS candidate on structure. It is **not** built
  (no beta functions computed for GU's operator content), and AS would deliver UV-completeness
  **without** needing the power-counting theorem -- so it is a genuine alternative, not a duplicate.

- **Q5 -- have/help/hurt + methods menu.** Below. Headline: GU **has** two structural advantages
  (4th-order softening in both sectors; a tree-level Krein rescue that is the *canonical* PT object,
  radiatively stable in its commutation leg). It is **hurt** by three things (no RS renormalizability
  theorem; the generic loop-positivity wall that defeats every rescue in the literature; sign-blindness
  of the GU-native `S`). The single gating object is the **source action** -- the same object that
  gates `mu_DW`, the count, and the S-matrix everything else needs.

---

## Survey 1 (Q1) -- Higher-derivative renormalizability: gravity vs Rarita-Schwinger

*Persona: higher-derivative renormalization theorist.*

### The gravity benchmark (settled, as DATA)

Stelle 1977 (PRD 16, 953) is the fixed point of comparison: adding the 4-derivative terms
`alpha C^2 + beta R^2` to Einstein-Hilbert makes the graviton propagator fall as `1/p^4` in the UV,
which renders 4th-order gravity **power-counting renormalizable** in D=4. The price is the massive
spin-2 companion, which is a ghost (negative residue). This is the origin of the entire
Stelle-Mannheim tension (Survey 3).

**COMPUTED reproduction (this wave, `W42_power_counting.py`, exact dimensional arithmetic):**
- Einstein-Hilbert coupling `[G] = 2 - D = -2` in D=4 -> **negative mass dimension ->
  non-renormalizable** (the textbook fact).
- Weyl^2 / R^2 coupling `[alpha] = D - 4 = 0` in D=4 -> **dimensionless -> power-counting
  renormalizable** (the Stelle fact).
- The superficial degree of divergence for the marginal 4th-order sector is **bounded (delta = 4)
  independent of loop number L**, whereas the 2nd-order Einstein sector's grows as `(D-2)L + 2 =
  2L+2`. This is the power-counting-renormalizability signature, reproduced as arithmetic.

### The fermion question (the actual Q1)

Is there a Stelle-analog for **higher-derivative fermions / Rarita-Schwinger**? The honest literature
reading:

1. **Power counting DOES transfer (COMPUTED).** A 4th-order (3-derivative-kinetic) fermion has
   propagator `1/p^3` and canonical dimension `[psi] = (D-3)/2 = 1/2` in D=4 (versus `3/2` for a
   Dirac/minimal RS field). The lower field dimension makes fermion-bilinear interaction couplings
   **dimensionally soft** (a Yukawa-type `(psi-bar psi) phi` to a dimensionless 4th-order boson has
   coupling dimension `+3`, deep in the super-renormalizable regime). So on **pure power counting**,
   a 4th-order RS carrier plausibly inherits Stelle-type UV softening. This is the favorable half of
   the answer, and it is genuinely COMPUTED.

2. **But power counting is NOT the RS obstruction.** The specific, well-documented hazard for
   Rarita-Schwinger is the **constraint algebra**, not the divergence degree:
   - **Velo-Zwanziger (1969):** a minimally-coupled massive RS field propagates **acausally** (faster
     than light) in a background field -- the constraints that should remove the spin-1/2 pieces
     degenerate, and lower-spin ghosts / superluminal modes appear. This is a *classical* consistency
     failure that survives to the quantum theory.
   - **Rahman (and the modern higher-spin program):** a non-minimally-completed (Porrati-Rahman-type)
     massive RS coupling restores causality but only **up to a cutoff** `Lambda` (the helicity-1/2
     strong-coupling scale). Above `Lambda` the interacting massive RS field is only an EFT unless a
     guardian (local SUSY, killed in Wave 41) or an infinite tower (Sagnotti-Taronna, absent in GU)
     completes it.
   - **Higher derivatives make this worse before better:** a 4th-order fermion kinetic term
     propagates *extra* modes (the analog of Stelle's massive ghost), and for a *constrained* field
     like RS those extra modes can re-populate exactly the lower-spin sector the gamma-trace
     constraint was built to kill. The literature on higher-derivative supergravity fermion sectors
     (canonical analyses; RS-QED with higher-derivative one-loop corrections) confirms higher-derivative
     terms are *generated* and that renormalizability "remarks" hinge on a **Stuckelberg / diagonal
     (Feynman-gauge)** formulation in which the RS quadratic action becomes Dirac-like -- i.e. the
     renormalizable propagator exists only after the constraint structure is carefully gauge-fixed,
     not automatically.

3. **No Stelle-grade theorem exists for higher-derivative RS.** There is a rich literature on
   higher-derivative *scalars* and *gravity* (renormalizable), and on Lee-Wick *fermions* (the
   Lee-Wick SM higher-derivative Dirac kinetic term is renormalizable by the same `1/p^3` power
   counting, arXiv:1006.2800). But a first-principles proof that a **gamma-trace-constrained
   4th-order Rarita-Schwinger field** is renormalizable, with its constraint algebra intact under
   loops, is **not in the primary literature**. The closest positive precedent is the Lee-Wick
   higher-derivative *Dirac* fermion (unconstrained), which does not carry the RS constraint hazard.

**Survey 1 verdict: PLAUSIBLE (power counting) BUT OPEN (constraint + ghost).** The 4th-order RS
carrier plausibly inherits Stelle-type power-counting softening -- COMPUTED at the level of field
dimensions and superficial divergence. It does **not** automatically inherit renormalizability,
because the RS-specific obstruction is the Velo-Zwanziger/Rahman constraint algebra, and higher
derivatives introduce new ghost modes into exactly the constrained sector. Whether GU's specific
`ker-Gamma` structure survives this is **unbuilt** and is the concrete Phase-2 target.

---

## Survey 2 (Q2) -- The ghost-rescue landscape: which rescues survive LOOPS

*Persona: ghost-rescue comparativist. This is the crux for GU's H26 open positivity.*

Four mechanisms are on the table. The decisive axis is **tree/free/oscillator vs interacting-loop**.

### The four mechanisms, precisely distinguished

| mechanism | what it does to the ghost | physical spectrum | GU relation |
|---|---|---|---|
| **Lee-Wick + CLOP** (Grinstein-O'Connell-Wise; Anselmi-Piva) | radiative corrections split the ghost pole into a **complex-conjugate pair**; CLOP prescription integrates around them | ghost **removed** (complex energy, excluded from asymptotic states) | **NOT GU** -- GU keeps the ghost, does not complexify it |
| **Anselmi fakeon** (purely virtual particle) | the ghost is quantized as a **"fakeon"**: mediates interactions but is **never an asymptotic state**; theory is renormalizable + unitary but **microcausality is sacrificed** at small scales | ghost **removed** (fake, non-asymptotic) | **NOT GU** -- GU's ghost is a real (if negative-norm) Krein state, kept and graded |
| **Bender-Mannheim PT** (PU oscillator; conformal gravity) | the Hamiltonian is **non-Hermitian but PT-symmetric**; a **similarity transform** to a positive/Krein inner product removes the *apparent* ghost -- "there never was one" | ghost **reinterpreted away** via the correct (PT/Krein) inner product | **= GU** -- R1 (this repo) COMPUTED that the BM `C`-operator IS the Bateman-Turok ghost parity `Z2` on the diagonalizable domain (CONDITIONALLY_SAME) |
| **Bateman-Turok** (arXiv:2607.00096; GU's actual rescue) | 4-derivative QFT on a **Krein space**; ghost **kept and graded** by a hidden ghost parity `P`; generalized (projector) Born rule gives positive probabilities | ghost **kept, graded** (negative-norm, projected out of observables) | **= GU** -- this IS GU's rescue; `P` = Cartan involution of `so(9,5)`, `[P,S]=0` |

**Structural map.** GU's `[P,S]=0` rescue is the **Bateman-Turok / Bender-Mannheim PT family** (the
"keep-and-grade-via-indefinite-metric" family), **NOT** the Lee-Wick / fakeon family
("remove-from-spectrum"). The repo's R1 result is the precise link: on the PT-unbroken diagonalizable
domain the Bateman-Turok ghost parity and the Bender-Mannheim `C` operator are the **same `Z2`**
(`||C - P_ghost|| -> 0` as the Fock truncation grows). So GU inherits **exactly** the Bender-Mannheim
PT program's strengths and its open problems.

### Which survive LOOPS (the decisive reading)

This is where the literature is blunt, and the news is symmetric across all four:

- **Bender-Mannheim PT: tree/oscillator only.** The no-ghost theorem is proven for the **Pais-Uhlenbeck
  oscillator** (quantum mechanics, one degree of freedom) and for the **free** field theory. The most
  recent quadratic-gravity PT paper (Kuntz, arXiv:2410.08278, 2024, read as DATA) explicitly operates
  "primarily at the free theory level" and **does not prove the PT similarity transform survives at
  the interacting/loop level** -- it acknowledges "distance between the formally consistent
  free-theory construction and what happens when genuine quantum interactions are included, where
  unitarity violations typically emerge." This is the SAME gap H26 pinned for GU.

- **Lee-Wick: reported VIOLATED at loop level in the interacting field theory.** Anselmi-Piva
  (arXiv:1703.05563) argued perturbative unitarity via the CLOP prescription and a nonanalytic Wick
  rotation, one loop. But a 2023 operator-formalism analysis (Nakayama et al., PTEP 2023 123B02,
  arXiv:2308.09006, read as DATA) finds that **complex ghosts ARE created in scattering above a
  definite energy threshold**, so the naive Feynman rules fail and **unitarity is VIOLATED** in the
  interacting field theory; the theory is unitary and renormalizable **only below the threshold**.
  The CLOP prescription itself is known to be ambiguous (prescription-dependent) beyond one loop.

- **Anselmi fakeon: renormalizable + unitary at loops, but at a stated price.** The fakeon program is
  the strongest loop-level claim in the field -- quadratic gravity with a spin-2 fakeon + scalar is
  argued renormalizable AND unitary to all orders. But (i) it **removes** the ghost from the spectrum
  (not GU's mechanism), and (ii) it **sacrifices microcausality** at small scales (the classical limit
  has no strict action). It is a *different theory* from GU's keep-and-grade Krein theory.

- **Bateman-Turok: tree-level positivity proven; loop positivity NEVER claimed.** Per the repo's own
  VG-SC / H26 intake of arXiv:2607.00096: pseudo-unitarity (`S^dag_K S = 1`) is claimed to all orders,
  but **positivity** of transition probabilities is proven **at tree level only**; loop-integral IR
  finiteness is deferred to an unpublished companion, and collinear IR divergences of the massless
  double-pole theory are **open**. There is **no rule in BT for odd-ghost-parity states on internal
  lines**.

**Survey 2 verdict: GU = Bender-Mannheim PT / Bateman-Turok family; and NO member of that family is
proven to survive loops.** The generic wall -- tree/free/oscillator positivity that is not shown to
persist through interacting loops -- is **not a GU-specific defect**; it is the state of the entire
keep-and-grade ghost-rescue program. The one mechanism with a strong loop-level claim (Anselmi
fakeon) is a *different* mechanism (remove-from-spectrum, non-causal) that GU does not use. This
exactly reproduces H26's OPEN verdict and locates it in the field: GU's loop-positivity question is
the open frontier of PT/Krein QFT itself.

---

## Survey 3 (Q3) -- The Stelle-Mannheim problem, and where GU lands

*Persona: Stelle-Mannheim dispute cartographer.*

**The dispute (as DATA).** 4th-order gravity is renormalizable (Stelle) but its massive spin-2
companion has a wrong-sign (ghost) residue. Two camps:

- **Stelle / orthodox:** the theory is **renormalizable but non-unitary** -- the ghost is a genuine
  negative-norm state and breaks unitarity. Higher-derivative gravity is a cautionary tale, not a
  theory.
- **Mannheim / Bender / PT camp:** conformal (and quadratic) gravity is **unitary after all**,
  because the Hamiltonian is non-Hermitian-but-PT-symmetric; computed in the correct (PT/Krein) inner
  product "there never was a ghost." Conformal gravity is then a serious UV-complete candidate.
- **Anselmi / fakeon camp (third position):** quadratic gravity is renormalizable AND unitary if the
  massive spin-2 is quantized as a fakeon (purely virtual), at the cost of microcausality.
- **Salvio-Strumia (agravity):** a related line taking the ghost seriously as a physical but
  benignly-interacting state.

**Status: genuinely UNRESOLVED.** The PT camp's proofs are oscillator/free-level (Survey 2); the
orthodox objection (that the interacting-loop theory reintroduces the ghost into observables) has not
been decisively refuted for a full field theory; the fakeon route is a *different* theory. This is a
live dispute in 2026, not a settled question with GU on the wrong side of it.

**Where GU lands:**

1. **On Mannheim's SIDE (PT/Krein), on the ATTRACTIVE branch.** GU's rescue is the PT/Krein
   keep-and-grade mechanism (Survey 2), and H16 already placed GU on the *attractive* side of the
   corner (healthy massless graviton, `m^2 > 0`, positive `G`). So GU is not on Stelle's
   "manifestly non-unitary" side -- it is committed to the Mannheim resolution.

2. **In a DISTINCT corner, not Mannheim's own.** GU's Krein form is not a generic PT choice: it is the
   **Cartan involution of `so(9,5)`** (`P = eta` on the vector rep, `P = beta_S in Sp(32,32;H)` on the
   spinor rep; H26/H23 COMPUTED, residual 0), forced by GU's non-compact source group and its `(9,5)`
   signature. Mannheim's conformal gravity carries a PT structure but not this specific
   geometrically-forced Cartan-involution Krein form on a non-compact `Sp(32,32;H)`. So GU is a
   **new corner** of the PT/Krein resolution -- one where the ghost parity is *derived from the
   geometry* (the Cartan involution) rather than *chosen to make PT work*.

3. **It INHERITS the dispute's open leg, does not resolve it.** GU's advantage (the commutation leg
   `[P,S]=0` is radiatively stable because `P` is a group element, H26 COMPUTED) is real but is
   exactly the leg the PT camp already has; the leg the dispute turns on -- **loop-level positivity**
   -- is open for GU as for everyone (Survey 2). GU's specific contribution to the dispute would be:
   *if* its geometric Cartan-involution `P` and a built source action `S` gave a PT-unbroken,
   real-simple-spectrum `S` (the R1 sharpening), GU would supply a **derived** (not chosen) PT
   structure -- which would be a genuinely new data point in the Stelle-Mannheim dispute. That `S` is
   unbuilt, and the GU-native cores computed so far are **sign-blind** (big-swing R3: no
   dynamics-derived `C`), so GU does not yet supply it.

**Survey 3 verdict: CONTESTED side, DISTINCT corner.** GU is committed to the Mannheim/PT resolution
(not the Stelle non-unitary reading), sits on the attractive branch, and occupies its own corner (a
geometrically-forced Cartan-involution Krein form on a non-compact group). It inherits the dispute's
one open leg (loop positivity) and does not resolve it; its potential contribution -- a *derived*
rather than *chosen* PT structure -- is gated on the same unbuilt, currently-sign-blind source action.

---

## Survey 4 (Q4) -- Asymptotic safety: the alternative UV route

*Persona: asymptotic-safety / functional-RG specialist.*

**The mechanism (as DATA).** Weinberg asymptotic safety (AS): a theory is UV-complete if the
renormalization-group flow hits a **non-trivial (interacting) UV fixed point** with a
**finite-dimensional** critical (UV-attractive) surface. Then the continuum limit exists and the
theory is predictive even though it is perturbatively non-renormalizable. The Reuter fixed point
(functional RG, Einstein-Hilbert truncation and beyond) is the gravity prototype.

**Why GU's structure is a plausible AS candidate:**

1. **4th-order gravity is a KNOWN AS/asymptotic-freedom setting.** Fourth-order derivative-expansion
   flows find **two** fixed points: one is asymptotically-free higher-derivative gravity (Stelle's
   marginal couplings run to zero logarithmically), the other extends the asymptotically-safe Reuter
   fixed point. GU's `Weyl^2 + R^X` gravity is squarely in this class. So GU's gravity sector already
   lives where the AS literature finds UV completions -- **independent of** the power-counting route
   of Survey 1.

2. **Gravity + fermions is an actively-studied AS sector, and it favors non-minimal derivative
   couplings.** The fermion-AS literature (Eichhorn et al., arXiv:1601.04597 chiral fermions;
   arXiv:1812.08782 "zooming in on fermions") finds an **unavoidable non-minimal derivative coupling
   between curvature and fermions** at the UV fixed point, with small backreaction on the Reuter
   fixed point for a bounded number of fermions. GU's carrier `B` is exactly a curvature-coupled
   fermion, and its **finite** content (no infinite tower) sits inside the "bounded fermion number"
   regime where the fixed point is known to survive. AS of higher-derivative gravity *non-minimally
   coupled to matter* (arXiv:1703.09033) is a direct structural precedent.

3. **The Krein structure is orthogonal to AS, and that is a feature.** AS is a statement about the
   *existence of a UV fixed point of the RG flow*; it does not by itself require a positive-definite
   Hilbert space at the fixed point. A Krein/PT completion and an AS fixed point are **compatible and
   complementary**: AS could deliver UV-completeness of the *couplings* while the Krein rescue handles
   *unitarity of the states*. This is a genuinely different division of labor from the power-counting
   route.

**Why it is not yet a result for GU:**

- **No beta functions for GU's operator content have been computed.** AS candidacy is a *structural*
  match, not a demonstrated fixed point. GU's specific `(9,5)` Krein signature, non-compact source
  group, and constrained `ker-Gamma` carrier have not been put through a functional-RG truncation.
- **AS is itself methodologically contested** (truncation-dependence, the "reconstruction problem" of
  going from Euclidean FRG to a Lorentzian S-matrix). Importing AS does not import certainty.
- **The unitarity question does not vanish.** An AS fixed point in a 4th-order theory still has the
  massive spin-2 ghost; AS addresses UV-completeness of the flow, not ghost positivity -- so GU would
  *still* need its Krein rescue for unitarity even in the AS scenario.

**Survey 4 verdict: YES, a live SECOND candidate, structurally independent of power counting.** GU's
4th-order + finite-matter + curvature-coupled-fermion structure is a plausible asymptotic-safety
candidate, and AS would UV-complete the *couplings* without needing the Stelle-analog RS
renormalizability theorem of Survey 1. It is unbuilt (no GU beta functions), methodologically
contested, and does not by itself solve the ghost -- but it is a real alternative route, not a
duplicate of the power-counting route.

---

## The renormalizability constraint ledger

*Persona: constraint-ledger synthesist. Each row: the constraint, whether GU meets it, grade.*

| # | constraint (what UV-completeness needs) | GU status | grade |
|---|---|---|---|
| C1 | UV-softened graviton propagator (`1/p^4`) | **MET** -- Stelle `Weyl^2`; `[alpha]=0` | COMPUTED |
| C2 | UV-softened matter propagator (`1/p^3` for RS) | **MET (kinematic)** -- 4th-order carrier `B`, `[psi]=1/2` | COMPUTED |
| C3 | power-counting renormalizability (bounded `delta` vs L) | **MET for the marginal 4th-order sector** | COMPUTED |
| C4 | RS constraint algebra (gamma-trace) survives interactions | **OPEN** -- Velo-Zwanziger/Rahman hazard; unbuilt | ARGUED |
| C5 | no Stelle-grade RS renormalizability theorem needed / supplied | **MISSING** -- none exists in the literature | ARGUED |
| C6 | ghost cleared at tree level | **MET** -- `[P,S]=0` Krein, BT positivity (tree) | COMPUTED (kinematic) + ARGUED (BT) |
| C7 | ghost parity radiatively stable (commutation leg) | **MET** -- `P` a group element / exact automorphism, residual 0 | COMPUTED |
| C8 | loop-level POSITIVITY (unitarity with the ghost) | **OPEN** -- unproven for GU AND for every rescue in the literature | ARGUED |
| C9 | a built source action `S` (S-matrix to run loops on) | **MISSING** -- the single gating object | -- |
| C10 | `S` PT-unbroken with real SIMPLE spectrum (R1 sharpening) | **OPEN** -- GU-native cores are sign-blind (R3) | COMPUTED (sign-blindness) |
| C11 | (alt route) a UV fixed point for GU's couplings (AS) | **OPEN candidate** -- structurally plausible, no beta functions | ARGUED |
| C12 | finite content compatible with the chosen route | **MET for AS / power-counting; FATAL for the tower route** (Wave 41) | ARGUED |

**Reading.** The *kinematic* and *power-counting* rows (C1-C3, C6-C7) are MET and largely COMPUTED.
Every row that turns on **interacting loops or a built `S`** (C4, C5, C8, C9, C10, C11) is OPEN or
MISSING. The ledger has no red "FORBIDDEN" cell on the renormalization route (unlike the guardian/tower
route, C12, which Wave 41 killed): renormalization is **not blocked**, it is **unbuilt and contested**.

---

## Have / help / hurt map for GU's 4th-order RS + Krein + (9,5)

**HAVE (structural advantages GU already carries):**
- **H-a.** 4th-order softening in **both** sectors (gravity `1/p^4`, RS `1/p^3`) -- COMPUTED.
- **H-b.** A tree-level ghost rescue that is the **canonical PT object**: R1 proved GU's ghost parity
  = the Bender-Mannheim `C`. GU is not using an ad-hoc trick; it is on the main line of PT/Krein QFT.
- **H-c.** The commutation leg `[P,S]=0` is **radiatively stable** because `P` is a genuine group
  element (Cartan involution), not a fine-tuned map -- COMPUTED, residual 0.
- **H-d.** The Krein form is **geometrically forced** (Cartan involution of `so(9,5)`), so if a loop
  positivity ever closes it would be a *derived* PT structure, a stronger claim than Mannheim's chosen one.
- **H-e.** **Finite content** is compatible with both surviving UV routes (power counting, AS) -- the
  same finiteness that was fatal to the tower route (Wave 41) is neutral-to-helpful here.

**HELP (what would advance the route, in leverage order):**
- **Hp-1.** Build the **source action `S`** -- unlocks the S-matrix that C4, C5, C8, C10 all need.
- **Hp-2.** A **higher-derivative RS renormalizability computation** (the missing Stelle-analog):
  compute the one-loop divergences of the 4th-order `ker-Gamma` carrier and check the gamma-trace
  constraint survives. This is the concrete Phase-2 deliverable Survey 1 points to.
- **Hp-3.** A **functional-RG truncation for GU's operator content** (test the AS candidacy, C11) --
  an independent route that does not need Hp-2.
- **Hp-4.** A **dynamics-derived `C`-operator** (break the sign-blindness, C10) -- would upgrade the
  Krein rescue from tree-level-only to a candidate loop-level rescue.

**HURT (obstructions, in severity order):**
- **Ht-1 (generic, severe).** **Loop-level positivity is unproven for the entire PT/Krein/BT family**,
  and for Lee-Wick it is reported *violated* above a threshold. GU's H26 wall is the field's wall.
- **Ht-2 (GU-specific, severe).** **No Stelle-grade RS renormalizability theorem exists**, and the
  RS constraint algebra (Velo-Zwanziger/Rahman) is the historically fragile part -- higher derivatives
  add ghost modes into exactly the constrained sector.
- **Ht-3 (GU-specific, structural).** **Sign-blindness** -- every GU-native core computed so far is
  spectrally K-balanced, so no dynamics-derived ghost parity arises (big-swing R3, SUSTAINED x2). The
  rescue is currently kinematic, not dynamical.
- **Ht-4 (methodological).** Both surviving routes are **unbuilt**; AS is additionally
  truncation-dependent and carries the Euclidean-to-Lorentzian reconstruction problem.

---

## Ranked methods menu (for the renormalization route)

1. **Build the source action `S`** (highest leverage, gates everything). Same object as `mu_DW`, the
   count, and the S-matrix. Without it, C4/C5/C8/C10 are undecidable from GU-internal data. Everything
   below is either a substitute for, or a consumer of, this.

2. **Compute the one-loop divergence structure of the 4th-order `ker-Gamma` RS carrier** (the missing
   Stelle-analog, Hp-2). Crisp, bounded, and the direct test of Survey-1's OPEN verdict: does the
   gamma-trace constraint survive loops, and are the extra 4th-order modes Krein-partners (rescued) or
   uncancelled ghosts (fatal)? Yes/no-ish; does not need a full `S`, only the quadratic + leading
   vertex.

3. **Run a functional-RG truncation for GU's operator content** (test AS candidacy, Hp-3). Independent
   of #2; would establish or refute a UV fixed point for GU's couplings, delivering UV-completeness of
   the flow even if the power-counting theorem fails. Leverages the strong 4th-order + fermion AS
   literature.

4. **Attack the sign-blindness: seek a dynamics-derived `C`** (Hp-4, C10). Search for a source-action
   term that breaks the exact K-balance and yields a real *simple* spectrum, so the PT/Krein rescue
   becomes dynamical. Its provable *absence* would be a second, independent obstruction (near-kill);
   its presence would upgrade the loop-positivity prospects.

5. **Loop-positivity model computation** (consumer of #1). Once an `S`-matrix exists, model the
   collinear-IR resummation BT defer and test whether `tr(C^dag C) -> 0` survives regularization (the
   H26 Part-C quantity). Lowest priority because it strictly requires #1.

**Menu note (what NOT to pursue):** the Lee-Wick / fakeon route is a *different theory*
(remove-from-spectrum, and fakeons sacrifice microcausality) -- adopting it would abandon GU's
keep-and-grade Krein structure, so it is a fork away from GU, not a completion of it. It stays off the
menu as a GU-advancement item (though it remains the relevant contrast class).

---

## The one COMPUTED test this wave

`tests/wave42/W42_power_counting.py` (deterministic, exact dimensional arithmetic, exit 0, all PASS)
computes the power-counting ledger cited above:
- canonical field dimensions (2nd vs 4th order, boson and fermion): `[phi]: 1 -> 0`, `[psi]: 3/2 -> 1/2`;
- propagator UV falloff: boson `1/p^2 -> 1/p^4`, fermion `1/p -> 1/p^3`;
- gravitational coupling dimensions: `[G] = -2` (non-renormalizable) vs `[alpha_Weyl] = 0`
  (power-counting renormalizable) -- the Stelle fact;
- RS-bilinear coupling softness with `[psi]=1/2` (Yukawa dim `+3`);
- superficial degree of divergence **bounded (`delta=4`) independent of loop L** for the marginal
  4th-order sector, vs Einstein's `2L+2` growth.

It is arithmetic, **not** a loop calculation and **not** a renormalizability proof: it establishes the
*necessary* power-counting leg and is explicit that the RS constraint algebra and loop positivity are
separate ARGUED questions. Nothing crisper computes at Phase-1 landscape scope, so no further test.

---

## COMPUTED vs ARGUED ledger

| claim | grade | evidence |
|---|---|---|
| `[G]=-2` (non-renorm) vs `[alpha_Weyl]=0` (renorm) in D=4 | **COMPUTED** | W42 test |
| 4th-order fermion `[psi]=1/2`, propagator `1/p^3`; RS-bilinear couplings dim `>=0` | **COMPUTED** | W42 test |
| superficial `delta` bounded vs L for 4th-order sector | **COMPUTED** | W42 test |
| GU ghost parity = Bender-Mannheim `C` (same `Z2`) on diagonalizable domain | **COMPUTED (toy)** | R1, CONDITIONALLY_SAME |
| `[P,S]=0` commutation leg radiatively stable (`P` group element) | **COMPUTED** | H26 A/B, residual 0 |
| GU-native cores sign-blind (no dynamics-derived `C`) | **COMPUTED** | big-swing R3 |
| Stelle 1977 makes 4th-order gravity power-counting renormalizable | **ARGUED (DATA)** | Stelle PRD 16, 953 |
| no Stelle-grade renormalizability theorem for higher-derivative RS exists | **ARGUED (DATA, absence)** | RS-QED / HD-SUGRA fermion literature |
| Velo-Zwanziger/Rahman constraint hazard is the RS obstruction (not propagator) | **ARGUED (DATA)** | VZ 1969; Rahman |
| Lee-Wick / fakeon REMOVE the ghost; PT/BT KEEP-and-grade it (GU = latter) | **ARGUED (DATA)** | Grinstein-O'Connell-Wise; Anselmi; BT |
| Bender-Mannheim PT proven tree/oscillator only; loop gap acknowledged | **ARGUED (DATA)** | Kuntz arXiv:2410.08278 |
| Lee-Wick interacting unitarity VIOLATED above a threshold | **ARGUED (DATA)** | Nakayama PTEP 2023, arXiv:2308.09006 |
| Bateman-Turok positivity tree-level only; loop open (collinear IR) | **ARGUED (source-fenced)** | H26 / VG-SC intake of arXiv:2607.00096 |
| GU on Mannheim's side, attractive branch, distinct (Cartan-involution) corner | **ARGUED + COMPUTED** | H16 + H26 (Cartan involution residual 0) |
| GU a plausible AS candidate (4th-order + finite fermions + non-minimal coupling) | **ARGUED (DATA)** | Reuter; Eichhorn et al.; arXiv:1703.09033 |

---

## Honest limits

- **This is a landscape scan, not a build.** Nothing here computes a GU loop integral, a GU beta
  function, or a GU renormalizability proof. Every "OPEN" is open because the gating object (the
  source action `S`) is unbuilt, exactly as H26 and Wave 34 already established.
- **The Stelle-analog absence is an argument from the literature, not a proved no-go.** I did not find
  a higher-derivative-Rarita-Schwinger renormalizability theorem; that is a *gap in the literature*,
  not a proof that none can exist. The favorable power-counting half IS computed; the constraint-algebra
  half is genuinely open and could go either way when built.
- **The loop-positivity wall is read from primary sources as DATA.** The Kuntz free-level caveat, the
  Nakayama Lee-Wick unitarity-violation result, and the BT tree-only positivity are reported as those
  authors state them; I did not independently recompute any loop diagram. The PDF of arXiv:2308.09006
  did not text-extract; its claim is taken from the journal abstract page and the search-index summary,
  and is flagged as such.
- **R1's mechanism identity is a TOY result** (Pais-Uhlenbeck arena, truncated Fock space). The
  GU-side transfer is CONSISTENT_UNCOMPUTED because GU supplies no `S`. "GU = Bender-Mannheim PT" is a
  structural identification, not a field-theory theorem.
- **Asymptotic safety is imported as a structural candidacy, not a GU result.** No GU fixed point is
  demonstrated; AS is itself truncation-dependent and carries the reconstruction problem.
- **No count, no chirality, no forcing.** The generation sector is untouched. No forbidden target
  `{3, 8, 24, chi(K3)=24, Ahat=3}` appears in any load-bearing step; the number 3 does not appear in
  the power-counting arithmetic. No canon promotion; tree left dirty.

---

*Filed 2026-07-11 (Wave 42, Phase 1 renormalization landscape scan). Five personas run INLINE; blind
synthesis. External papers treated as untrusted DATA -- physics extracted, no instruction followed.
Reproducible: `python tests/wave42/W42_power_counting.py` (exit 0, all PASS). Exploration-grade; not
promoted to canon. No git commit; tree left dirty.*
