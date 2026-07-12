---
title: "H49 -- the Bach/Weyl graviton sector: FALSIFY + class-decider probe on the convergent load-bearing object"
artifact_type: exploration
status: exploration
created: 2026-07-11
wave: 28
grade: "COMPUTED for the Bach-identification (linearized Bach on TT recomputed from scratch = -1/4 box^2 h, i.e. box^2 h = -4 Bach, exact sympy), the two-pole/residue structure, the 7-DOF/5-extra polarization count, and the mu_DW-parametrized Stelle-Yukawa ranges + GW-dispersion scales (tests/wave28/H49_bach_weyl_sector.py, exit 0, all PASS). ARGUED for the refutation-transfer verdicts (grounded in H23/H26 residual-0 facts and the H45 binary) and the two class no-go assessments. Published bounds (Cassini, GW170817, Eot-Wash, Horne, Hobson-Lasenby, Stelle, Mannheim) used in comparison only; no target number imported; no count number touched. Tree left dirty."
depends_on:
  - tests/wave28/H49_bach_weyl_sector.py
  - explorations/two-track-persona-sweep-2026-07-11/SYNTHESIS.md
  - explorations/two-track-persona-sweep-2026-07-11/A-orthodox-rigor.md
  - explorations/two-track-persona-sweep-2026-07-11/C-foundations-observer.md
  - explorations/two-track-persona-sweep-2026-07-11/E-pragmatic-experimental.md
  - explorations/wave24/H45-H2-vs-II2-binary-2026-07-11.md
  - explorations/wave22/H10-ppn-weak-field-2026-07-11.md
  - explorations/wave23/H26-loop-ghost-unitarity-2026-07-11.md
  - explorations/wave21/H5-geometry-vs-information-bianconi-2026-07-11.md
  - tests/wave1/H1_bach_flat_exact_vacua.py
---

# H49 -- the Bach/Weyl graviton sector

**The object.** The full-roster two-track sweep (families A + C + E) converged: the decidable axis
for the observer-type-geometry (OTG) class is NOT geometry-vs-information (both smuggle the metric,
ill-posed) but the spin-2 action ORDER. This one sector needs neither the unbuilt source action nor
the (9,5)/(7,7) signature settled, and it FORCES, FALSIFIES, and DECIDES-THE-CLASS at once. This note
runs the FALSIFY + class-decider side: does a known refutation of conformal/Bach gravity kill GU, and
does either class-level no-go kill the whole OTG class (GU AND Bianconi)?

**Discipline.** Compute -> label COMPUTED vs ARGUED -> honest verdict. Reproducible:
`python tests/wave28/H49_bach_weyl_sector.py` (exit 0, all PASS). An honest "GU-gravity is falsified"
or "the class is killed" would be a SUCCESS; no outcome is wanted. The headline is neither: it is
**GU-DISTINGUISHED with the class's Lambda-magnitude HEADLINE scope-killed, everything gated on one
number (mu_DW).**

---

## Q1 -- THE BACH-IDENTIFICATION and refutation transfer

### The identification: CONFIRMED, and re-derived from scratch [COMPUTED]

I recomputed the linearized Bach tensor on a transverse-traceless plane wave from
Christoffel -> Riemann -> Weyl -> two partial derivatives (flat background, so the two covariant
derivatives collapse to partials and the algebraic `(1/2)R^{cd}C` term is O(h^2)). Result, exact
sympy, independent of the D-thread:

```
linearized Bach_yy / (box^2 h_yy) = -1/4    (a pure number; independent of w, q, A)
=> box^2 h = -4 Bach^(1)   on the TT spin-2 sector.
```

So GU's H-class (|H|^2 / Willmore) linearized graviton operator **IS** the 4th-order conformal/Bach
operator on spin-2 -- reproducing H45/H1/D-thread from an independent computation. Under the favored
`|II|^2` reading the operator factorizes `box(box + m^2) = box^2 + m^2 box` (Stelle Einstein-Weyl:
Bach `box^2` + Einstein `box`); under `|H|^2` it is pure Bach `box^2`. The `box^2` piece is present
under BOTH GU branches; Bianconi's 2nd-order Einstein carries none (H5). So the mainstream refutations
of conformal/Bach gravity are genuinely on the table for GU.

### Do the known refutations transfer? (verdict per refutation)

**(a) Ostrogradsky ghost -- EVADED at tree (|II|^2-specific); would KILL on |H|^2.**
The 4th-order theory has a massive spin-2 ghost (propagator residue `-1/m2^2`, computed). GU clears it
**at tree level** by Krein quantization: the ghost parity `P` implements the Cartan involution of
`so(9,5)`, is a GROUP element (`P in O(9,5)`, `Sp(32,32;H)`) and an exact automorphism, so `[P,S]=0`
to residual 0 (H23/H26, `tests/wave23`, COMPUTED). With the flat mass real (`m^2 = +1/2 > 0`, H15/H16)
the Bateman-Turok tree-level positivity applies. This clearance is **`|II|^2`-specific**: on `|H|^2`
the pole is the coincident Pais-Uhlenbeck Jordan case, where R1 (H26) proved NO positivity-compatible
ghost parity of any kind exists -- tree clearance fails. **Verdict: EVADED (|II|^2) / KILL (|H|^2).**

**(b) Stelle-Mannheim loop-level non-unitarity -- OPEN.**
H26 (wave23) is decisive and unflattering-but-honest: the COMMUTATION leg of `[P,S]=0` is radiatively
stable (COMPUTED: a group-realized symmetry is inherited by the effective action to all orders), but
loop-level POSITIVITY is a strictly stronger condition that does not follow from commutation, is proven
nowhere in the literature for 4-derivative gravity, and cannot be checked in GU because GU has no built
source action / S-matrix. **Verdict: OPEN** (undecidable from GU-internal data). GU lands on the
attractive side of the Stelle-Mannheim corner (tree) but inherits its unresolved loop dispute.

**(c) Horne / Hobson-Lasenby "no genuine flat rotation curves" -- EVADED (|II|^2) / KILL (|H|^2).**
This is the empirically fatal refutation of conformal gravity, and it is the sharpest new finding here.
Mannheim-Kazanas conformal gravity fits galactic rotation curves via the LINEAR potential term
`gamma*r` in the static vacuum solution of the PURE Weyl^2 theory (no Einstein-Hilbert term). Horne
(2016) and Hobson & Lasenby (PRD 104, 064014, 2021) showed that when `gamma` is honestly sourced by
matter through the 4th-order field equation, it does not yield genuine flat rotation curves (wrong
sign / no true flattening). The refutation TARGETS the long-range `gamma*r` mechanism.

GU's `|II|^2` branch has an Einstein-Hilbert `R^X` term, so its Weyl/Bach sector is a MASSIVE spin-2
(Yukawa), not a massless long-range mode. Computed: the Yukawa range `1/m2 = hbar_c/(sqrt(m2_eff) mu_DW)`
is `< 52 um` for **every** lab-allowed `mu_DW` (the Eot-Wash short-range floor), which is `~10^-24` of a
kpc. There is no long-range `gamma*r` potential, and GU makes no rotation-curve / dark-matter-replacement
claim. The refutation targets a mechanism the `|II|^2` branch simply does not have. **Verdict: EVADED.**
On `|H|^2` (no EH), GU IS pure Mannheim-Kazanas conformal gravity (`gamma*r`, massless Bach) and
**inherits Horne/Hobson-Lasenby as a KILL** -- the same branch that already fails the tree ghost.

> **The `|II|^2`-vs-`|H|^2` binary (H45) IS the evades-vs-inherits fork.** On the favored `|II|^2`
> branch, no refutation transfers as an unevaded kill (ghost tree-cleared, rotation-curve mechanism
> absent, only loop unitarity open). On `|H|^2`, two independent kills fire. This makes settling the
> H45 P2 norm choice load-bearing for GU's life, not just its Lambda sign.

## Q2 -- THE SPIN-2 CLASS DISCRIMINATOR (the concrete numbers)

**Pole / residue structure [COMPUTED].** `|II|^2` propagator
`1/[p^2(p^2+m2^2)] = (1/m2^2)[1/p^2 - 1/(p^2+m2^2)]`: two poles -- a massless graviton (residue
`+1/m2^2`) and a massive spin-2 at `p^2 = -m2^2` (residue `-1/m2^2`, the ghost).
`m2 = sqrt(m2_eff) * mu_DW`, `m2_eff in [5/6, 5/4]` (H25, positive, O(1)). Bianconi: single pole
`1/p^2`, no companion.

**Polarizations [COMPUTED integer count].** Massless spin-2 = 2 DOF; massive spin-2 = 5 DOF; GU total
= **7 propagating DOF, 5 more than GR/Bianconi's 2.** In the Eardley detector-frame classification GU
can excite up to **6 polarization classes** (2 tensor + 2 vector + 2 scalar breathing/longitudinal) vs
GR/Bianconi's 2 (tensor only).

**mu_DW-parametrized Stelle-Yukawa range [COMPUTED].** `V(r) = -(GM/r)[1 + (1/3) e^{-m2 r}]`, range
`1/m2 = hbar_c/(sqrt(m2_eff) mu_DW)`:

| `mu_DW` | Yukawa range `1/m2` | probe |
|---|---|---|
| `~M_Pl = 1.2e28 eV` (natural) | `~1.8e-35 m` (Planckian) | decoupled from everything |
| `> 1.5e-17 eV` (Cassini floor) | `< 0.10 AU` | solar-system PPN (H10) |
| `> ~3.8e-3 eV` (Eot-Wash floor) | `< 52 um` | **strongest** lab short-range gravity |

**GW dispersion [COMPUTED scale].** Massive mode `E^2 = p^2 c^2 + m2^2 c^4 =>
v_g/c ~ 1 - (1/2)(m2 c^2/E)^2`. The massless sector is exactly luminal (`v_g = c`), so GW170817
`|v_g/c-1| < ~1e-15` is satisfied trivially. The massive companion's Compton frequency at the lab-floor
mass is `~1e12 Hz` -- far above the LIGO (`~1e2 Hz`) and LISA bands -- so for any lab-allowed `mu_DW`
it is not excited by astrophysical sources: its dispersion and extra polarizations are observationally
null above the lab floor.

**The empirical fork vs information-first gravity, and what LIGO/LISA would distinguish.** The
Lagrangian fork is real and robust to the (9,5)/(7,7) binary (`box^2` under both GU branches, none in
Bianconi). But the concrete numbers show the fork is **empirically null in every accessible band for
natural `mu_DW`**: GW (massive mode unexcited, massless luminal), PPN (Yukawa-suppressed), cosmology
(GR-degenerate). The single LIVE observable is a **sub-millimetre Stelle-Yukawa deviation** of the
Newtonian potential, detectable by Eot-Wash-class experiments ONLY if `mu_DW` sits near its `~meV` lab
floor (massive spin-2 near `~meV`, range near `~50 um`). LIGO/LISA distinguish GU from Bianconi in
principle (extra polarizations / high-`f` dispersion) but in practice only if `mu_DW` were anomalously
low; at natural scale they cannot.

## Q3 -- THE CLASS-LEVEL NO-GOES

**(a) Occam-kill -- DOES NOT FIRE as a class-kill; fires only as a testability caveat.** The kill
requires the physical graviton to be EXACTLY single-metric 2nd-order GR. GU's graviton is genuinely
4th-order with a Planck-mass companion -- a distinct theory, not identical to GR -- so the premise is
not met. What the PART 3 numbers DO show is that the 4th-order apparatus does no OBSERVABLE work for
natural `mu_DW` (everything GR-degenerate), so Occam bites as a *testability* pressure. But a live
sub-mm Yukawa window survives at `mu_DW ~ meV`, so the content is not excluded, merely (for most of the
scale range) undetectable. **Verdict: does not kill; testability caveat only.**

**(b) Lambda-magnitude no-go -- FIRES as a class-level SCOPE-kill (GU AND Bianconi).** Neither frame
pins `~10^-122` (H5, H42). Computed scale-counting: a scale-free action -- GU's conformally-invariant
Willmore/GJMS functional, Bianconi's dimensionless relative entropy -- has an Euler-Lagrange system that
fixes only DIMENSIONLESS O(1) ratios. The observed `Lambda/M_Pl^4 ~ 1.3e-123` (from
`(rho_Lambda)^{1/4} ~ 2.3 meV`) is a `~10^-120` hierarchy; the magnitude requires an IMPORTED
dimensionful scale (GU: `{B_i, mu_DW}`; Bianconi: `{Lambda_bare, b, beta}`) that the `g`-vs-`G` action
structure provably cannot contain. This **kills the strong "Lambda emerges from the two-metric
structure" HEADLINE for the entire OTG class at once.** It does NOT falsify either theory, because
neither actually claims to derive the magnitude (both claim only sign / small-positive naturalness) --
so the scope-kill removes an over-claim, not the theories. **Verdict: the class's headline magnitude
claim is dead; the theories survive with their honest (sign-only) Lambda claims intact.**

## Q4 -- VERDICT

**GU-DISTINGUISHED.** GU-gravity is NOT falsified: on the favored `|II|^2` branch no known refutation of
conformal/Bach gravity transfers as an unevaded kill (Ostrogradsky tree-cleared by Krein `[P,S]=0`;
Horne/Hobson-Lasenby targets a long-range `gamma*r` mechanism the Einstein-Hilbert-carrying `|II|^2`
branch does not have; only loop unitarity is open). GU survives as a **distinct testable 4th-order
theory** with named observables (a massive spin-2 companion, 5 extra polarization DOF, a Stelle-Yukawa
potential, GW dispersion).

**The OTG CLASS is partly killed at the headline level, not the theory level.** The Lambda-magnitude
no-go fires as a class-wide SCOPE-kill: a scale-free two-metric action cannot contain `~10^-122`, so the
"Lambda emerges from the `g`-vs-`G` structure" headline is false for GU AND Bianconi. The Occam-kill
does not fire (GU is a genuinely distinct 4th-order theory; a live window survives).

**Everything empirical is gated on ONE number, `mu_DW`.** At natural `mu_DW ~ M_Pl` the entire
distinctive radiative content is decoupled and GU is observationally GR-equivalent (Occam-vulnerable but
not falsified). The distinction is observationally LIVE only if `mu_DW` sits near its `~meV` lab floor,
where the sub-mm Stelle-Yukawa deviation is detectable.

### Named observables (the spin-2 discriminator vs Bianconi)
- **Stelle-Yukawa**: `V(r) = -(GM/r)[1 + (1/3) e^{-m2 r}]`, range `1/m2 = hbar_c/(sqrt(m2_eff) mu_DW)`;
  LIVE (sub-mm, Eot-Wash-testable) iff `mu_DW ~ meV`; `~0.1 AU` at the Cassini floor; Planckian at `M_Pl`.
- **GW polarizations**: up to 6 detector classes (GU) vs 2 (Bianconi/GR); 5 extra field DOF. Unexcited
  above the lab floor.
- **GW dispersion**: `v_g/c ~ 1 - (1/2)(m2 c^2/E)^2` for the massive mode; massless sector luminal
  (passes GW170817 trivially).

---

## COMPUTED vs ARGUED ledger

| claim | grade | evidence |
|---|---|---|
| linearized Bach on TT `= -1/4 box^2 h` (i.e. `box^2 h = -4 Bach`), from scratch | **COMPUTED** | PART 1, exact sympy, ratio `-1/4` indep of w,q,A |
| `|II|^2` operator `box(box+m^2) = box^2 + m^2 box` | COMPUTED | PART 1 factorization |
| two poles, residues `+1/m2^2` (massless) and `-1/m2^2` (ghost); `|H|^2` coincident | COMPUTED | PART 2 partial fractions + residues |
| 7 DOF (2 massless + 5 massive), 5 extra; up to 6 Eardley classes | COMPUTED | PART 2 integer counts |
| Stelle-Yukawa ranges: `~1.8e-35 m` (M_Pl), `<0.1 AU` (Cassini), `<52 um` (Eot-Wash) | COMPUTED | PART 3, cited bounds in comparison only |
| massless GW luminal; massive Compton freq `~1e12 Hz` >> LIGO/LISA | COMPUTED | PART 3 |
| `Lambda/M_Pl^4 ~ 1.3e-123`; scale-free action supplies only O(1) ratios | COMPUTED | PART 5 scale-counting |
| Ostrogradsky EVADED at tree (`|II|^2` Krein `[P,S]=0`) / KILL on `|H|^2` | ARGUED (from COMPUTED H23/H26/H45) | residual-0 facts + Jordan boundary |
| Stelle-Mannheim loop non-unitarity OPEN | ARGUED | H26 |
| Horne/Hobson-Lasenby EVADED (`|II|^2`) / KILL (`|H|^2`) | ARGUED (from COMPUTED scale separation) | range `<< kpc`; cited Horne/HL |
| Occam-kill does not fire; Lambda-magnitude scope-kill fires | ARGUED (grounded in PART 3/5 numbers) | premise-check + scale-counting |

## Honest limits

- **Refutation-transfer verdicts are ARGUED, not fresh theorems.** The Ostrogradsky/Horne-HL verdicts
  rest on COMPUTED inputs (the `[P,S]=0` residual-0 facts of H23/H26; the sub-52-um Yukawa range vs kpc)
  but the "therefore the refutation does/doesn't bite" step is a physics argument, not a machine-checked
  derivation of GU's full nonlinear static solution. In particular, that the `|II|^2` static solution
  has NO long-range `gamma*r` term is inferred from the presence of the Einstein-Hilbert term + the
  massive (not massless) Bach pole; it is not re-derived here from GU's full source action (unbuilt).
- **Everything hinges on the H45 P2 binary and on `mu_DW`.** If P2 resolves to `|H|^2`, the verdict
  flips to **GU-FALSIFIED** (inherits Horne-HL AND the Jordan tree-ghost). If `mu_DW ~ M_Pl`, GU is
  Occam-vulnerable (observationally GR-equivalent). Both are unbuilt-source-action gated.
- **Loop unitarity is genuinely OPEN**, not evaded: a clean loop-level non-unitarity result on the
  H-class action would still kill GU-as-a-QFT, and cannot be run without a built S-matrix (H26).
- **Bianconi and all external bounds are DATA**, used in comparison only (Cassini, GW170817, Eot-Wash,
  Horne 2016, Hobson-Lasenby 2021, Stelle, Mannheim-Kazanas); no instruction followed, no target number
  imported, no count number touched. No claim promoted to canon. Tree left dirty (no commit).

## RE-RANK signal

**GU-DISTINGUISHED / CLASS-HEADLINE-SCOPE-KILLED / everything gated on `mu_DW`.**

- The FALSIFY attempt did not land on the favored branch: GU-gravity is Bach gravity on spin-2 (COMPUTED
  identification, `box^2 h = -4 Bach` re-derived) but the `|II|^2` branch is Stelle Einstein-Weyl, NOT
  the rotation-curve-fitting Mannheim conformal gravity that Horne/Hobson-Lasenby refute. Up-rank the
  H45 P2 binary: it is now the **evades-vs-inherits fork for GU's life** (|H|^2 => GU-FALSIFIED), not
  just the Lambda-sign fork.
- The class-decider DID land, but at the headline not the theory: the **Lambda-magnitude scope-kill** is
  a real, cheap, class-wide result (a scale-free two-metric action provably cannot contain `~10^-122`) --
  book it as a class-level scope limit on the OTG "Lambda emerges" claim.
- The empirical fork vs Bianconi is REAL but **observationally live only in a knife-edge `mu_DW ~ meV`
  window** (sub-mm Stelle-Yukawa); at natural `M_Pl` it is null (Occam testability caveat, not a kill).
- **Single next object: pin `mu_DW`** -- equivalently, build the source action that fixes the one
  dimensionful scale. It decides Occam-decoupled vs sub-mm-live, and is the SAME object that gates P2
  (evades vs FALSIFIED), the H26 loop positivity, and the count. Quadruply motivated, unambiguous #1.

---

*Filed 2026-07-11. Wave 28. Reproducible: `python tests/wave28/H49_bach_weyl_sector.py`
(exit 0, all PASS). Exploration-grade; not promoted to canon. Tree left dirty.*
