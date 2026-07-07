---
artifact_type: exploration
status: exploration
created: 2026-07-06
title: "R3 (Mannheim/Bender PT swing): can definiteness be DERIVED from GU-native dynamics' own spectral data, curing BIG-SWING-1's imported-definiteness defect? HONEST OUTCOME: NO — BLOCKED, bounded-negative, with one THEOREM-grade sub-result. All six GU-native cores tested on the 192-dim self-dual triplet sector (comp(M_D), comp(Pi M_D Pi) [= identical on W, proved], the SU(2)+ Casimir [exactly scalar], a Weyl^2-shaped quadratic so(9,5)-curvature core, and three mixed-grading variants) are PT-UNBROKEN (fully real spectra, no Jordan blocks, no K-null eigenvectors) — reality itself is special, since random K-self-adjoint controls are PT-BROKEN (90–95 complex pairs) — but EVERY eigenspace of EVERY GU-native core has exactly balanced Krein signature (+m/2, -m/2): the C operator exists yet is NEVER determined by the dynamics. The Mannheim move fails not at spectral reality but at spectral separation: no GU-native core ever splits a hyperbolic (generation, mirror) pair. And a one-line theorem, machine-checked: because chi anticommutes with K (the canon cross-chirality), Re tr(chi Pi_+) = 0 for EVERY admissible C — GU-native, imported, or otherwise. No chiral physical sector; no forbidden target touched."
grade: "exploration / BLOCKED, bounded-negative (Mannheim move measurably unavailable on the tested GU-native cores), containing one THEOREM-grade sub-result (the achirality identity Re tr(chi Pi_+) = 0 for every admissible C, proved in one line from {K, chi} = 0 and machine-corroborated to 1e-14). Anchors reproduced exactly (rank Gamma = 128, ker = 1664, bare 58.7215, C2 155.3625, beta residual 0.0e+00, triplet Krein signature (+96, -96, 0)). Classifier is not a tautology: a non-GU definitizable control returns PT-UNBROKEN with a DERIVED unique C, and random controls return PT-BROKEN. No forbidden target {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} assumed, inserted, hardcoded, or divided by; every count is measured and zero."
depends_on:
  - canon/ghost-parity-krein-synthesis.md
  - explorations/generation-sector/mannheim-conformal-gravity-source-action-intake-2026-07-06.md
  - tests/generation-sector/ghost_parity_krein.py
  - tests/generation-sector/gen_sector_bridge.py
  - tests/generation-sector/step11_gu_native_parity_theorem.py
  - explorations/big-swing-2026-07-03/BIG-SWING-1-source-action-definite-vertical-dirac-BLOCKED.md
scripts:
  - tests/big-swing/cg_r3_pt_phase_gu_cores.py
---

# R3: PT-phase classification of GU-native cores — is definiteness derivable from dynamics?

**The swing.** BIG-SWING-1's Attempt 1 was refuted because definiteness was IMPORTED via a
gauge-breaking compensator section. Bender–Mannheim's central move (the PT resolution of the
Pais–Uhlenbeck ghost, the mechanism behind Mannheim's conformal gravity and the direct ancestor of the
Turok–Bateman ghost parity the canon synthesis is built on) is the exact opposite: definiteness is
DERIVED from the dynamics' own spectral data. If a K-self-adjoint core is in the **PT-UNBROKEN** phase
— real spectrum, diagonalizable, K definite on each eigenspace — then a unique operator `C` exists with
`C^2 = I`, `[C, A] = 0`, `K·C > 0`, and the C-positive subspace is the physical Hilbert space. No
import; the spectrum does the choosing. This swing asks whether that move is **available on GU's own
carrier**: for each GU-native core on the 192-dim self-dual `SU(2)+` generation-triplet sector `W`
(Krein signature `(+96, -96, 0)`, the canon anchor), classify the PT/Krein phase, build `C` where it
exists, test whether it is canonical (derived), and read off whether the C-positive physical sector can
be **chiral**: `tr(chi Pi_+)`.

**Honest outcome: BLOCKED, bounded-negative.** The Mannheim move is measurably **unavailable** on every
GU-native core tested — and the failure mode is sharper and more interesting than the anticipated one.
GU's cores are *not* PT-broken and *not* Jordan-singular; they are all **PT-UNBROKEN with maximally
K-balanced eigenspaces**: every eigenspace of every GU-native core has Krein signature exactly
`(+m/2, -m/2)`. The `C` operator always exists but is **never determined by the dynamics** — the choice
of maximal positive subspace inside each K-hyperbolic eigenspace is exactly the datum the spectrum was
supposed to supply and doesn't. Definiteness cannot be derived; it would still have to be imported,
which is BIG-SWING-1's refuted move. On top of that, a one-line theorem (machine-checked) closes the
chirality door for **every** admissible `C`, not just GU-native ones.

Script: `tests/big-swing/cg_r3_pt_phase_gu_cores.py` (repo root, `python tests/big-swing/cg_r3_pt_phase_gu_cores.py`,
exit 0, runtime a few minutes). Every number below is printed by that script.

---

## Anchors — reproduced before any claim

Bridge signature convention (`eta = +1` for `a = 0..8`, `-1` for `a = 9..13`, the
`gen_sector_bridge.py` convention, so the `M_D` anchors reproduce verbatim); triplet sector built by the
`ghost_parity_krein.py` recipe (self-dual `SU(2)+` on the spacelike base `{0,1,2,3}` inside
`ker(Gamma)`, top Casimir sector):

| anchor | printed | target |
|---|---|---|
| `rank(Gamma)` | **128** | 128 |
| `dim ker(Gamma)` | **1664** | 1664 |
| bare `\|\|[Pi_RS, M_D]\|\|` | **58.7215** | 58.7215 |
| `C2 = \|\|Gamma M_D Pi_RS\|\|` | **155.3625** | 155.3625 |
| `beta_S` pseudo-anti-Hermiticity residual | **0.00e+00** | ~0 |
| triplet sector dim / Casimir top | **192 / 8.0** | 192 |
| triplet Krein signature | **(+96, -96, 0:0)**, min `\|eig B\| = 1.0000` | (+96, -96, 0) |
| `tr(chi\|W)` (vectorlike anchor) | **+4.4e-15** | 0 |
| chirality halves totally K-null | max `\|eig\|` **3.2e-15 / 3.8e-15** | 0 |
| `{K, chi} = 0` (K purely cross-chiral) | **0.00e+00** | 0 |
| `J_quat`: `\|\|U Ubar + I\|\|` | **7.9e-12** (`J^2 = -1`) | 0 |

Compressions to `W` are **Krein-orthogonal**: `comp(A) = B^{-1} W^H K A W` (`B = K|W`), which sends
K-self-adjoint operators to B-self-adjoint operators on `W`; the K-self-adjointness residual
`||BA - (BA)^H||` is printed per core (all `~1e-13`–`1e-12`), never assumed. Globally
`||K M_D - M_D^H K|| = 0.00e+00` and `||[K, Pi_RS]|| = 0.00e+00` (both printed).

---

## The decisive readout table

| core (all K-self-adjoint; residuals printed) | phase | C | `\|\|[C, J]\|\|` | `tr(chi Pi_+)` | `\|\|{C, chi}\|\|` |
|---|---|---|---|---|---|
| 1. `comp(M_D)` — GU default Dirac core | PT-UNBROKEN | **NON-CANONICAL** | 8.7e-11 | **-0.000000** | 1.9e-12 |
| 2. `comp(Pi_RS M_D Pi_RS)` | = core 1 (`\|\|diff\|\| = 5.8e-14`) | = core 1 | – | – | – |
| 3. `comp(SU(2)+ Casimir)` = `8.0000·I` exactly | PT-UNBROKEN | **NON-CANONICAL** (maximally) | 6.7e-12 | **+0.000000** | 6.2e-14 |
| 4. `comp(sum w_ab T_ab^2)` — Weyl²-shaped, seed 7 | PT-UNBROKEN | **NON-CANONICAL** | 6.7e-12 | **+0.000000** | 2.0e-13 |
| 5. mixed `M_D + 0.5·W²` (seed 7) | PT-UNBROKEN | **NON-CANONICAL** | 9.4e-11 | **-0.000000** | 3.7e-11 |
| 5. mixed `M_D + 1.5·W²` (seed 7) | PT-UNBROKEN | **NON-CANONICAL** | 8.7e-11 | **-0.000000** | 4.5e-12 |
| 5. mixed `M_D + 0.5·W²` (seed 8) | PT-UNBROKEN | **NON-CANONICAL** | 9.9e-11 | **-0.000000** | 4.7e-11 |
| C1. random J-commuting K-self-adjoint (2 seeds) | **PT-BROKEN** (92 / 90 complex pairs) | none | – | – | – |
| C2. random non-J K-self-adjoint (2 seeds) | **PT-BROKEN** (94 / 95 complex pairs) | none | – | – | – |
| C3. definitizable `B^{-1}(Y^H Y + 0.1 I)` — NOT GU-native | PT-UNBROKEN | **DERIVED** (unique) | 2.1e+01 | +0.000000 (Im −0.102) | 2.1e+01 |

**GU-native cores that are PT-UNBROKEN with a DERIVED C: 0 of 6. Cores with a chiral physical sector: 0 of 6.**

---

## What is established (machine-checked, with the printed numbers)

**1. GU-native cores are all PT-UNBROKEN — and that reality is itself a measured specialness.** Every
GU-native core has a fully real spectrum (max `|Im lambda|` between `1.8e-14` and `3.5e-13`, at spectral
scales `0.36`–`11.6`), is diagonalizable (geometric multiplicities sum to `192/192` in every case; no
Jordan blocks), and has K-nondegenerate eigenspaces (min `|Gram eig| = 0.1115`, far from zero). This is
NOT generic: random K-self-adjoint cores on the same `(96, 96)` Krein space — even when forced to be
J-commuting — are **PT-BROKEN** with 90–95 complex-conjugate pairs out of 96. GU's kinematic cores sit
squarely inside the PT-unbroken phase, which is a genuine, non-tautological structural fact about them.

**2. But the C operator is never derived: every eigenspace is exactly K-balanced.** The eigenspace
census, per core:

- `comp(M_D)`: two eigenvalues `±0.3606`, each 96-dim, each with K-signature **(+48, -48)**. (Also
  printed: `comp(M_D)^2 = 0.130000·I`, residual `2.9e-12` — the compressed Dirac core is an exact
  two-frequency `±omega` system, `omega = 0.3606`.)
- `comp(SU(2)+ Casimir)`: exactly scalar, `||A − 8.0000·I|| = 9.1e-13`; a single 192-dim eigenspace with
  K-signature **(+96, -96)** — the maximally undetermined case: *every* K-compatible `C` commutes with it.
- Weyl²-shaped core: three eigenvalues `{0.2725, 1.3689, 4.2314}`, each 64-dim, each **(+32, -32)**.
- The three mixed-grading cores: six eigenvalues each, all 32-dim, all **(+16, -16)**. (Printed:
  `||[comp(M_D), comp(W²)]|| = 2.0e-12` — the odd and even GU cores commute, so mixed-core eigenspaces
  are joint `(lambda_1, lambda_4)` sectors.)

In Bender–Mannheim's construction the spectrum is supposed to separate K-positive from K-negative
states; the `C` operator is unique exactly when each eigenspace is K-definite. Here **no GU-native core
ever separates them** — each eigenspace is a direct sum of hyperbolic planes, i.e. the canon's
(generation, mirror) pairing survives inside every eigenspace of every GU-native core. A valid `C`
always exists (built and verified per core: `||C^2 − I|| ≤ 2.9e-11`, `||[C, A]|| ≤ 1.6e-11`,
`min eig(KC) > 0`, values printed), but the choice of maximal positive subspace inside each hyperbolic
eigenspace is free. The **non-uniqueness is demonstrated concretely**: a hyperbolic rotation (`t = 0.6`)
inside an indefinite eigenspace produces a second `C'` passing all three C-conditions
(`||C'^2 − I|| ~ 1e-11`, `||[C', A]|| ~ 1e-11`, `min eig(KC') = 0.0259 > 0`) — an equally valid,
genuinely different physical-sector choice from the same dynamics.

**3. THEOREM (one line, machine-checked): no admissible C yields a net-chiral physical sector.** The
canon fact that `K` is purely cross-chiral (`{K, chi} = 0`, printed `0.00e+00`; each chirality half of
`W` totally null, max `|eig| ~ 3e-15`) forces, for **every** operator `C` with `K·C` Hermitian (which
every Bender–Mannheim / Krein `C` satisfies, `C = K^{-1}H` with `H = KC`):

> `conj(tr(chi C)) = tr(H K^{-1} chi) = −tr(chi K^{-1} H) = −tr(chi C)`,

so `tr(chi C)` is purely imaginary and `Re tr(chi Pi_+) = Re[tr(chi) + tr(chi C)]/2 = 0` identically.
Numeric corroboration on 4 random admissible `H` (seeds 51–54): `Re tr(chi B^{-1}H)` between `0.0` and
`1.1e-14` while `Im` is `O(1)` (`−0.957`, `+1.442`, `−0.106`, `+0.358`). Note what this means honestly:
the `tr(chi Pi_+) = 0` column of the table is **an arena identity, not a GU-core property** — even the
non-GU definitizable control prints real part `+0.000000`. No choice of `C` — GU-native, imported, or
otherwise — makes the C-positive physical sector net-chiral in the Cl(14)-volume trace sense. This is
the C-07 wall speaking PT language, now as a theorem rather than a scan.

**4. The classifier has discriminating power (anti-tautology controls).** The definitizable control
`B^{-1}(Y^H Y + 0.1 I)` (deliberately NOT GU-native — it imports definiteness by construction; that is
its job) returns exactly what the Mannheim cure would look like: PT-UNBROKEN, 192 simple eigenvalues,
**all 192 eigenspaces K-definite, C DERIVED and unique** (`||C^2 − I|| = 3.2e-12`,
`min eig(KC) = 0.209`). And the random controls return PT-BROKEN. So the pipeline can output both "cure
present" and "no structure at all"; the GU-native cores' uniform "PT-unbroken but C-undetermined"
verdict is a property of the cores, not of the method.

**5. Cross-check on the 1664-dim gamma-traceless slice.** `K` on `ker(Gamma)` has signature
`(+832, -832, 0)` (printed); `comp(M_D)` on the slice is K-self-adjoint (residual `2.8e-11`) with fully
real spectrum (max `|Im| = 3.0e-13` at scale `5.489`) — the PT-unbroken-ness of the GU Dirac core is not
a triplet-sector artifact.

**6. Two incidental exact facts** (printed): `comp(Pi_RS M_D Pi_RS) = comp(M_D)` on `W` to `5.8e-14`
(because `W ⊂ ker(Gamma)` and `[K, Pi_RS] = 0` exactly — core 2 is redundant on this arena, a finding,
not an omission); and the so(9,5) quadratic Casimir compresses to `−36.7500·I` (residual `4.2e-12`),
confirming `ker(Gamma)` is so(9,5)-irreducible — which is why a *generic-weight* quadratic core (the
Weyl²-shape) is needed to get a non-scalar curvature-squared symbol at all.

---

## Why each defect candidate is or is not present

- **Imported definiteness (BIG-SWING-1's killer)?** NOT present — and that is the point. Nothing here
  imports a positive metric; the swing *measures whether the dynamics can supply one* and finds it
  cannot. The only definite object in the run is the C3 control, explicitly labeled NOT GU-native and
  used solely as the discriminator.
- **Tautological closure / zero discriminating power (BIG-SWING-1 defects 2–3, R2's forced-parity
  trap)?** NOT present. The classifier returns three different verdicts on three different input
  classes (GU cores: UNBROKEN/NON-CANONICAL; random: BROKEN; definitizable: UNBROKEN/DERIVED). The one
  readout that IS forced — `Re tr(chi Pi_+) = 0` — is explicitly identified as an arena identity,
  proved, and NOT counted as evidence about GU cores.
- **Constants copied from canon?** None. All spectra, signatures, and residuals are computed fresh; the
  canon numbers (128, 1664, 58.7215, 155.3625, (+96, -96, 0)) appear only as reproduced-and-asserted
  anchors.
- **Scripts not persisted?** The single script is on disk at `tests/big-swing/cg_r3_pt_phase_gu_cores.py`
  and runs to exit 0 from the repo root; every number cited here is in its stdout.
- **Forbidden-target import?** The numbers 3, 8, 24 etc. are never assumed, inserted, or divided by.
  The only counts computed are the measured eigenspace signatures (all balanced) and the measured
  `tr(chi Pi_+)` (zero, and proved zero for the real part). Had any core produced a nonzero count it
  would have been labeled "this core forces c", never "GU forces c" (the script prints this discipline
  in its verdict branch).

---

## What this settles, and what it does not

**Settles (this swing).** On GU's verified carrier, the Bender–Mannheim/PT route to definiteness — the
one mechanism in the literature that *derives* rather than imports the physical inner product for
higher-derivative/Krein dynamics, and the stated reason (canon, "plausibly met if GU's source action is
quadratic-gravity-like") for optimism about the ghost-parity condition — **degenerates on every
GU-native core tested**. The failure is precise: GU cores are PT-unbroken (nontrivially — random cores
are not), but their spectra never separate the hyperbolic (generation, mirror) pairs; every eigenspace
is exactly K-balanced `(+m/2, -m/2)`, so the C operator exists but carries exactly as much freedom as
the definiteness one hoped to derive. GU's kinematics sits at the **degenerate-C point** of the PT
phase diagram: not the Jordan/K-null equal-frequency PU singularity the route brief anticipated, but
the adjacent degeneracy where the spectrum is real yet completely sign-blind. The Mannheim move does
not cure BIG-SWING-1's defect; it relocates the same missing datum into "choice of positive subspace
per hyperbolic eigenspace." Additionally, THEOREM-grade: with chirality read as the Cl(14) volume
grading (this repo's standard), `{K, chi} = 0` forces `Re tr(chi Pi_+) = 0` for every admissible `C` —
no PT/Krein quantization of this arena can output a net-chiral physical sector by that readout, no
matter what source action GU eventually builds, as long as the physical sector is selected by a `C`
with `KC` Hermitian.

**Does NOT settle.**
- The core list is finite (M_D, its Pi-dressing, both Casimirs, a generic quadratic curvature symbol,
  three mixed variants, one `xi`). "Every GU-native core has K-balanced eigenspaces" is measured on
  these, not proved for the generated algebra. For chi-**even** cores balance IS a one-line theorem
  (chi preserves each eigenspace and anticommutes with K, so the restricted signature satisfies
  `(p, q) = (q, p)`); for chi-odd and mixed cores it is measured only.
- The chirality readout is the Cl(14) volume trace. The canon's "three chiral generations" hope lives
  one refinement deeper (the `Spin(10)` `16` vs `16bar` split inside the triplet); this swing does not
  test a `16/16bar`-graded readout, and the theorem's scope is exactly the `chi`-trace.
- This classifies finite-dimensional cores (symbols), not GU's actual unbuilt field dynamics; a genuine
  source action could in principle supply a K-separating perturbation. But note what the scatter of
  eigenvalues across cores 4–5 (weights, couplings, seeds — all spectra move, all balances stay
  `(+m/2, -m/2)`) says: the balance is robust across the GU-unfixed modeling freedom we varied.
- Nothing here derives or forbids three generations. The generation-count verdict stays **OPEN**.

**Relation to the canon's open condition.** The canon synthesis left one named condition: does GU's
dynamics realize the ghost parity as a symmetry (`[P_ghost, S] = 0`)? This swing sharpens the cost of
that condition from the PT side: even granting a PT-symmetric (K-self-adjoint, PT-unbroken) dynamics of
the Bender–Mannheim class, the spectral data of GU-native cores does not single out the physical half
of any hyperbolic pair — and the built `C`'s all *anticommute* with chi (`||{C, chi}|| ≤ 4.7e-11` on GU
cores), i.e. every dynamics-compatible `C` we constructed IS a ghost parity in the R2/canon sense
(swapping chirality halves) — which by the theorem is exactly the class that yields an achiral physical
sector. The Turok–Bateman rescue and the achirality of its output are, on this arena, the same fact.

---

## Next steps

1. **Promote the balance to a theorem or find the separating datum.** Prove (or refute by construction)
   that every K-self-adjoint element of GU's J-commuting native algebra, Krein-compressed to `W`, has
   K-balanced eigenspaces. The even case is done (one line, via chi); the odd/mixed case is the open
   lemma. A proof would upgrade this route's BLOCKED to a structural no-go: "the Mannheim move is
   unavailable on GU's carrier, period."
2. **Test the 16/16bar-graded readout.** Build the `Spin(10)` chirality refinement on `W` and re-run
   the trace identity; if the refined grading also anticommutes with `K`, the achirality theorem
   extends and the canon's "three physical chiral generations" reading loses its last trace-level
   readout; if it does not anticommute, that is the first crack worth attacking.
3. **The equal-frequency boundary.** `comp(M_D)^2 = 0.1300·I` is a two-frequency `±omega` PU analog at
   `omega = 0.3606` for the canon `xi`; scan `xi` toward `Q(xi) -> 0` (the null cone) where `omega -> 0`
   and the two clusters merge — the genuine Jordan/K-null PU point. If GU's dynamics prefers null `xi`,
   the kinematics lands exactly ON the singular PT boundary, which would connect this route to R1(d)
   as the brief anticipated.
4. **Feed the result back to the intake.** The Mannheim intake's follow-up question 1 (are Bender–
   Mannheim and Turok–Bateman the same mechanism here?) now has a computed answer on this arena: every
   dynamics-compatible `C` is a ghost parity, and both mechanisms hit the same balanced-eigenspace
   degeneracy. Update the intake's stress-test log accordingly.

**Governance.** Exploration-grade; no canon promotion proposed (the theorem sub-result is a candidate
for later promotion once independently re-derived). Generation-count verdict unchanged (OPEN); a
verdict/status flip pauses for Joe.
