---
title: "Velo-Zwanziger Fifth-Theorem Canon Entry: Assumption List, Clifford-Module-Non-Sub-Module Evasion, and Explicit Failure Conditions"
date: 2026-06-23
problem_label: "no-go-velo-zwanziger-canon-entry"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# Velo-Zwanziger Fifth-Theorem Canon Entry

## 1. Problem statement

The no-go-class-relative-map (`canon/no-go-class-relative-map.md`) carries five no-go
families: Witten 1981, Nielsen-Ninomiya, Freed-Hopkins, Distler-Garibaldi, and
Velo-Zwanziger (VZ). The first four have settled canon treatments: each has a formal
assumption list, a named forgetful operation, an evasion verdict, and (for DG) a
precision carve-out promoted from structural observation to theorem.

VZ is the fifth and only GU-prediction-specific family. Its analysis chain reached
`EVADED (reconstruction)` at 14D and `VERIFIED` at the 4D principal-symbol level (§18 of
`vz-schur-complement-2026-06-23.md`), but both labels were subsequently corrected: the 14D
verdict to `CONDITIONALLY_EVADED` (VZ-01 circularity flag,
`vz-14d-mixed-covectors-2026-06-23.md`), and the 4D label to `CONDITIONALLY_RESOLVED`
(principal-symbol, flat-gauge computation; subprincipal and curved-gauge open), since the
§18 result is a principal-symbol-only, flat-gauge computation with subprincipal order and
the curved-gauge extension still open.
What the map still lacks is a **formal fifth-theorem VZ canon entry of the same shape as
the other four**: a self-contained statement of (a) the assumptions VZ fixes, (b) the
precise evasion type — the Clifford-module-non-sub-module mechanism — stated as a formal
condition GU satisfies in place of a VZ hypothesis, and (c) explicit failure conditions
that would falsify the evasion.

This file is that entry. It is a **synthesis / no-go-map update**, not an index inflation
or a new computation. It does not re-derive the Schur complement, the §18 4D pullback, or
the F5 Hamiltonian analysis; it states their joint consequence in canon form and binds the
verdict honestly: **14D is reconstruction (CONDITIONALLY_EVADED), 4D is
CONDITIONALLY_RESOLVED (principal-symbol, flat-gauge computation; subprincipal and
curved-gauge open).** The entry does not over-state either leg.

## 2. Established context (what this entry synthesizes)

This entry builds on and cites, without re-deriving:

- `vz1-velo-zwanziger-analysis-2026-06-22.md` — Finding 1 (RS(3,1)⊗S(6,4) carries SM
  charges, so VZ hypothesis H3 fires at 4D and "trivial internal coupling" is false);
  Finding 2 (the evasion lives at 14D via Dirac-DeRham non-decoupling).
- `vz-schur-complement-2026-06-23.md` — the Schur complement symbol
  `S_R(xi) = A - B E^{-1} C`; §8 kernel argument (`ker S_R = 0` for non-null `xi`);
  §17-18 section-pullback 4D preservation; OQ3-V2/V3 RESOLVED, OQ3-V1
  CONDITIONALLY_RESOLVED (computed only in constant-coefficient flat Minkowski gauge,
  curved-section frame-splitting asserted not computed); 4D principal-symbol
  evasion CONDITIONALLY_RESOLVED, NOT VERIFIED; 4D E-block `det = -1/4`).
- `vz-14d-mixed-covectors-2026-06-23.md` — VZ-01 correction: the 14D Schur proof presumes
  `E(xi)` invertible, which it does not independently establish; 14D status is therefore
  `CONDITIONALLY_EVADED`, not `EVADED`. The 4D leg is independently CONDITIONALLY_RESOLVED (the OQ3-V1 flat-gauge limitation; see vz-schur §18).
- `vz-e-block-direct-clifford-2026-06-23.md` — same-session reconstruction-grade direct
  Clifford argument for E-block invertibility; not externally verified.
- `vz-oq1-sr-squared-identity-2026-06-23.md` — the exact matrix identity is
  `A S_R = S_R A = xi2 Id_R`, **not** `S_R^2 = xi2 Id` (the latter is false; `B E^{-2} C != 0`).
- `vz-f5-hamiltonian-subsidiary-propagation-2026-06-23.md` — Dirac-Bergmann analysis:
  the gamma-trace constraint is kinematic, not a dynamical E-L constraint; the classical VZ
  secondary-constraint chain does not initiate (CONDITIONALLY_RESOLVED, four FCs).
- `vz-f6-eft-decoupling-2026-06-23.md` — KK zero-mode sub-bundle inherits the Clifford
  module property; B/C blocks are kinematic (CONDITIONALLY_RESOLVED).
- Pre-loaded context: `Cl(9,5) ≅ M(64,H)`, spinor module `S = H^64`; gauge group `Sp(64)`
  anomaly-free; D_GU has light-cone characteristic cone (Berline-Getzler-Vergne §2.1).

## 3. The fifth-theorem canon entry

The following is the formal entry, written to slot into `no-go-class-relative-map.md` §2.5
as the structured assumption/evasion record. It mirrors the four-part shape of the DG
precision carve-out (§2.4): assumptions → condition GU satisfies instead → forgetful
operation → failure conditions.

---

### 3.1 Statement (as used in the literature)

Velo-Zwanziger 1969 (Phys. Rev. 186:1337; precursor Johnson-Sudarshan 1961): a spin-3/2
(Rarita-Schwinger) field **minimally coupled to a nontrivial external gauge background**
develops acausal propagation — the characteristic determinant of the hyperbolic system
vanishes for some spacelike normal, producing superluminal characteristics, or the
subsidiary conditions that fix the physical DOF count become inconsistent and the Cauchy
problem is ill-posed.

### 3.2 Assumptions (formal list)

VZ fixes the class of theories satisfying **all** of:

- **VZ-H1 (standalone RS field).** Ψ_μ is described by a **standalone** Rarita-Schwinger
  Lagrangian — an independent dynamical spinor-vector field with its own kinetic term and
  its own gamma-trace subsidiary condition `γ^μ Ψ_μ = 0` imposed externally (as a
  Lagrange-multiplier constraint or as a gauge condition).
- **VZ-H2 (minimal coupling).** Coupling is minimal, `∂_μ → D_μ = ∂_μ + A_μ`, with `A_μ`
  valued in a nontrivial Lie-algebra representation of an internal gauge group G.
- **VZ-H3 (nontrivial gauge representation).** The representation of G on Ψ_μ is
  non-singlet.
- **VZ-H4 (background).** Flat or mildly curved background (original theorem).
- **VZ-H5 (no guardian).** No local symmetry principle (local SUSY, higher-spin gauge
  invariance) maintains the subsidiary conditions.

### 3.3 Condition GU satisfies instead of VZ-H1 — the evasion type

**Evasion type: Clifford-module-non-sub-module mechanism.**

GU does **not** evade VZ by exiting H3 (it does not — the RS(3,1)⊗S(6,4) sector carries a
full Pati-Salam generation of SM charges, so H3 fires at 4D; the "trivial internal coupling"
claim is false, `vz1-velo-zwanziger-analysis-2026-06-22.md` Finding 1). Nor does it evade by
supplying a guardian (H5 may hold; GU has no established local SUSY). GU evades by
**violating H1**: there is no standalone RS field to which VZ applies. The formal condition
GU satisfies in place of VZ-H1 is:

> **GU-VZ (Clifford-module non-sub-module).** The RS sector is the gamma-trace kernel
> `R = ker Γ ⊂ E` of the full Clifford module bundle `E` of the single Dirac-type operator
> `D_GU` on `Y^14`, with `Cl(9,5) ≅ M(64,H)` acting on `S = H^64`. Clifford multiplication
> `c(xi)` does **not** preserve `R`: `R` is **not a sub-Clifford-module** of `E`. Equivalently,
> `c(xi) R ⊄ R` — the off-diagonal blocks `B = (c(xi))|_{R→Q}` and `C = (c(xi))|_{Q→R}` are
> generically nonzero (explicit `C` block: `C ψ_R = (χ, (γ(xi)−2)χ)` with `χ = g_Y(xi,ψ_R)`,
> §3.1 of `vz-schur-complement`). The effective RS symbol is the Schur complement
> `S_R(xi) = A − B E^{-1} C`, and the Clifford module identity `c(xi)^2 = g_Y(xi,xi) Id_S`
> propagates through it to give the exact entanglement identity
>
> ```
> A S_R = S_R A = g_Y(xi,xi) Id_R                                    (GU-VZ-ENT)
> ```
>
> (exact, from block-square identities (I) `A^2 + BC = xi2 Id` and (II)/(III) `AB = −BE`,
> `EC = −CA`; `vz-oq1`). Identity (GU-VZ-ENT) is the formal statement that the RS sector
> cannot be detached from the spin-1/2 sector at any energy scale: the coupling is
> **kinematic** (fixed by the Clifford algebra), not dynamical (a choice of Lagrangian).

**Why GU-VZ defeats the VZ mechanism.** VZ's acausality is the statement that the
characteristic cone of the standalone RS operator has spacelike sheets. Under GU-VZ the
effective RS characteristic cone is `{xi : det S_R(xi) = 0}`. The §8 kernel argument shows
`ker S_R(xi) = 0` for all non-null `xi` (i.e. `g_Y(xi,xi) ≠ 0`), so the characteristic cone
is **contained in the null cone** `{g_Y(xi,xi) = 0}`. No spacelike characteristics exist;
VZ acausality cannot arise. The mechanism is **not a guardian symmetry** (no SUSY is
invoked) and **not class-exit by trivial coupling** (H3 fires) — it is non-decoupling: VZ's
H1 is structurally unavailable because `R` is a direct summand of a Clifford module, not a
standalone field.

### 3.4 Forgetful operation

The VZ class is the image of the **minimal-coupling functor**

```
ϕ_mc : (RS field, Clifford-module embedding R ⊂ E, B/C coupling data, guardian) ↦
       (standalone RS field, nontrivial gauge coupling, no guardian)
```

`ϕ_mc` **forgets the Clifford-module embedding** `R ⊂ E` (the data of `B` and `C`) and
treats `R` as an independent matter field. VZ is the statement that the image of `ϕ_mc` is
ill-posed. GU lives in the domain of `ϕ_mc` but not in its image: the embedding datum
`R ⊂ E` is exactly what `ϕ_mc` discards, and it is precisely (GU-VZ-ENT) — the kinematic
entanglement — that carries the causal-cone guarantee. The smooth-bundle shadow forgets the
non-sub-module structure; the relation (a physical spin-3/2 multiplet in the spectrum)
survives the shadow, the mechanism (non-decoupling) does not.

### 3.5 Verdict (bound honestly)

- **14D (full mixed covectors `xi = xi_H + xi_V`): CONDITIONALLY_EVADED, reconstruction
  grade.** The §8 kernel argument establishes `ker S_R^{14D}(xi) = 0` for all non-null 14D
  covectors **conditional on** `E(xi)` being invertible. E-block invertibility has only a
  same-session reconstruction-grade direct Clifford argument
  (`vz-e-block-direct-clifford`), not external verification. This is reconstruction, not
  verified.
- **4D (section pullback to `s(X^4)`): CONDITIONALLY_RESOLVED (principal-symbol, flat-gauge
  computation; subprincipal and curved-gauge open).** OQ3-V1/V2/V3 are resolved at the
  principal-symbol, flat-gauge level (§18): the pulled-back symbol satisfies
  `c_s(η)^2 = g_s(η,η) Id_{E_s}` exactly in flat-gauge coordinates; the 4D E-block is
  invertible (`det = −1/4`); `R_s = ker Γ^{4D}` exactly, with the normal RS components being
  KK scalars, not spin-3/2 fields. The 4D effective RS characteristic cone is the null cone of
  `g_s`; no spacelike characteristics at the principal-symbol level. The subprincipal order and
  the curved-gauge extension are open (see FC-VZ-4).

The honest combined reading: **the checked 4D model has no principal-symbol VZ spacelike
characteristics in the flat-gauge reconstruction, and the 14D origin of that result is
established only at reconstruction grade conditional on E-block invertibility.** The entry
does not claim 14D is verified, does not claim the curved/subprincipal 4D problem is closed,
and does not claim the full dynamical (loop-level, constrained-Hamiltonian) problem is
closed.

### 3.6 Failure conditions (explicit; would falsify the evasion)

The Clifford-module-non-sub-module evasion **fails** — and VZ acausality is reinstated — if
any of the following is established. Each is a specific, checkable mathematical statement.

- **FC-VZ-1 (E-block kernel on the non-null cone).** There exists a 14D covector `xi` with
  `g_Y(xi,xi) ≠ 0` such that `E(xi): Q → Q` has nontrivial kernel. Then the Schur complement
  `S_R = A − B E^{-1} C` is undefined at `xi`, the §8 argument fails at Step 2, and the 14D
  evasion proof collapses. (This is the open VZ-01 precondition; it is the single load-bearing
  gap separating the 14D verdict from `EVADED`.)

- **FC-VZ-2 (standalone GU RS Lagrangian).** There exists a standalone, gauge-invariant,
  dynamically consistent Rarita-Schwinger Lagrangian for the GU spin-3/2 multiplet on `X^4`
  whose field equations are **not** equivalent to the section-restricted `D_GU Ψ = 0`. Then
  GU-VZ is false — VZ-H1 is satisfied after all — and the standard VZ characteristic analysis
  applies to that Lagrangian. (This is FC1 of `vz-f5`; closing it negatively, by proving no
  such Lagrangian exists, is what would upgrade F5 toward RESOLVED.)

- **FC-VZ-3 (first-order gauge-curvature entry into B/C).** The Sp(64) gauge curvature `F_A`
  enters the off-diagonal coupling blocks `B(xi)` or `C(xi)` at **first order in `xi`** (rather
  than at zero order via the Shiab coupling, as currently established). Then `F_A` modifies the
  principal symbol, the cone `{det S_R = 0}` can acquire spacelike sheets, and (GU-VZ-ENT) no
  longer guarantees the null-cone bound. (This is FC2 of `vz-f5`; the Dirac-Bergmann analysis
  finds `F_A` enters only at zero order, but that result is reconstruction grade.)

- **FC-VZ-4 (extrinsic-curvature-sourced spacelike characteristics).** The second fundamental
  form `II_s = s*(θ)` of the section embedding sources an effective first-order term in
  `S_R^{4D}(η)` that produces spacelike characteristics in the 4D effective RS cone. Then the
  4D principal-symbol evasion is overturned at the next (subprincipal) order. (FC3 of
  `vz-f5`; `vz-subprincipal` finds no sub-characteristics, CONDITIONALLY_RESOLVED. This is the
  subprincipal leg the §3.5 4D verdict records as open.)

- **FC-VZ-5 (IR loop corrections drive B/C to zero).** One-loop corrections drive the
  off-diagonal blocks `B`, `C` to zero in the deep infrared, so that `R` decouples into an
  effectively standalone field at low energy. Then a guardian symmetry would be required (OQ2),
  and absent one, VZ would fire in the decoupled IR theory. (This is OQ-RS-2 / F6-loop; the
  structural argument is that B/C are Clifford-algebra-determined and `c(xi)^2 = xi2 Id` is
  loop-exact, but the explicit one-loop B/C computation has not been performed.)

If **none** of FC-VZ-1 … FC-VZ-5 is established, the evasion stands at the grade stated in
§3.5 (14D reconstruction / 4D CONDITIONALLY_RESOLVED at the principal-symbol, flat-gauge
level). Each is a falsification surface, not a current obstruction; none is established as a
structural obstruction as of 2026-06-23.

## 4. Where this sits among the five families (cross-theorem note)

VZ remains the family that **resists the anomaly/cobordism unification** the first three
share (§3.2 of the map): it is a classical Cauchy-well-posedness constraint, not a
topological obstruction. But the GU evasion sharpens a structural parallel with the **DG
carve-out**: in both cases GU exits the no-go not by a clever condition-by-condition dodge
inside the theorem's class, but by **not being an object of the class at all**. DG: GU is
not a single-E8 representation-theoretic object. VZ: GU's RS sector is not a standalone RS
field — it is a non-sub-Clifford-module summand `R ⊂ E`. Both are **category-level / structural
exits**: the forgetful operation (single-E8-adjoint for DG; minimal-coupling for VZ) discards
exactly the datum (bundle/compactification structure for DG; the Clifford-module embedding for
VZ) on which the GU invariant depends. The difference is grade: DG is EVASION-BY-SCOPE-EXIT
(a precision theorem, the generation invariant `ind_H(D_GU)` provably lies outside `DG_E8`),
whereas VZ is CONDITIONALLY_EVADED at 14D (reconstruction) and, after 4D pullback,
CONDITIONALLY_RESOLVED (principal-symbol, flat-gauge computation; subprincipal and
curved-gauge open). The map should not present VZ at DG's grade.

## 5. Result and verdict

**Verdict: CONDITIONALLY_RESOLVED.**

The fifth-theorem VZ canon entry is written: a formal assumption list (VZ-H1…H5), the
condition GU satisfies instead of VZ-H1 (GU-VZ, the Clifford-module-non-sub-module
mechanism, with the exact entanglement identity `A S_R = xi2 Id_R`), the forgetful operation
(minimal-coupling functor `ϕ_mc`), an honestly bound verdict (14D reconstruction
CONDITIONALLY_EVADED / 4D CONDITIONALLY_RESOLVED, principal-symbol, flat-gauge computation;
subprincipal and curved-gauge open), and five explicit failure conditions FC-VZ-1…5.

The verdict is CONDITIONALLY_RESOLVED rather than RESOLVED because the entry's content is
load-bearing on a reconstruction-grade 14D result whose single open precondition (E-block
invertibility on the non-null cone, FC-VZ-1) has only a same-session, externally-unverified
argument; and because the entry deliberately records the 14D leg as reconstruction, not
verified. The synthesis task — producing the canon entry — is complete; the underlying
mathematics it summarizes is not uniformly verified, so the synthesis cannot claim RESOLVED
without over-stating the 14D leg, which the instructions forbid.

**The three (here five) explicit failure conditions that would falsify the result** are
FC-VZ-1 (E-block kernel on non-null cone), FC-VZ-2 (standalone GU RS Lagrangian exists),
FC-VZ-3 (F_A enters B/C at first order), FC-VZ-4 (extrinsic-curvature spacelike
characteristics), and FC-VZ-5 (IR loop decoupling of B/C).

## 6. Open questions

- **FC-VZ-1 closure** is the highest-leverage remaining item: external verification of the
  E-block direct-Clifford argument would upgrade 14D from CONDITIONALLY_EVADED to EVADED.
- **FC-VZ-2 / FC-VZ-5** (no standalone RS Lagrangian; loop-stability of B/C) are the path
  from "principal-symbol evasion" to "full dynamical evasion."
- The entry as written is the synthesis artifact; promoting its §3.1-3.6 text into the body
  of `no-go-class-relative-map.md` §2.5 (replacing the prose with this structured form) is a
  map-edit, recorded in the tracking cascade below but kept conservative — the map's existing
  §2.5 already carries the substance; this file supplies the formal four-part shape and the
  enumerated FC list it lacked.
