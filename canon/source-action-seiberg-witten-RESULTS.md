---
title: "Source action build RESULTS: the GU Seiberg-Witten action exists, discharges dark energy conditionally, and is provably orthogonal to the generation count"
status: active
doc_type: result
created: 2026-06-28
grade: "RECONSTRUCTION-GRADE, INCOMPLETE -- no upgrade for GU. Every claim below is computed (numbers from running code on the Cl(9,5) substrate) or graded open. Refutations reported as loudly as confirmations."
method: "12-agent build workflow: 4 construct angles -> moment-map foundation gate -> 4 numerical discharge verifiers (ran python on the substrate) -> adversarial critic (re-ran the numerics) -> synthesis. ~1.58M subagent tokens, 343 tool uses."
depends_on:
  - canon/source-action-seiberg-witten-construction.md
  - canon/two-primary-lemma.md
  - canon/ghost-parity-krein-synthesis.md
  - NEXT-FRONTIER-HYPOTHESES.md
---

# Source action build: results

We built the GU fermionic source action in its own named Seiberg-Witten template and ran the numbers. The
verdict is decisive and honest: **the action exists as a well-defined algebraic object, conditionally
discharges dark energy, and performs NONE of the three jobs it was built for.** This converts "S_IG is
unbuilt" into "S_IG's SW nonlinearity exists, is the unique cross-chirality seesaw source, conditionally
discharges dark energy -- and leaves the chiral count, the selector collapse, the BV master equation, and
the -5376/24 index as named, separated, UNMOVED open frontiers." GU stays reconstruction-grade and
incomplete; the standing quaternionic-parity no-go is hardened, not relieved.

## The object we built (the final action)

The **doubled full-`Lambda^2` GU-Seiberg-Witten source action** on the 4-base `X^4`, with chimeric
vector-spinor `Psi` (the 192-dim `j=1` triplet of `ker(Gamma)` inside `V (x) S`) and IG connection `A`:

```
S = INT_{X^4} [ ||F_A||^2  +  <Psi, D_A Psi>_K  +  |F_A^+ - mu^+(Psi)|^2  +  |F_A^- - mu^-(Psi)|^2 ]
    + S_comp[sigma_c]  +  S_VZ
```

with the load-bearing nonlinearity the moment map `mu = (mu^+, mu^-)`,
`mu^s_k(Psi) = i <Psi, J^s_k Psi>_K` landing in `su(2)_+ (+) su(2)_-`. Euler-Lagrange (the GU monopole
equations): `F_A^+ = mu^+(Psi)`, `F_A^- = mu^-(Psi)`, `D_A Psi = 0`.

The running code forced one correction to the strawman: the coupling must be **doubled** to the full
`Lambda^2` (both `su(2)_+` and `su(2)_-`), because the same Krein bilinear sources both chiralities
comparably (`|mu^-| ~ |mu^+|`). The doubling is substrate-legitimate (`mu^-` is itself a genuine Krein-real,
`su(2)_-`-equivariant moment map, image rank 3) and it removes the need for the hand-imposed self-dual
projector the construction was built to avoid. `S_comp` and `S_VZ` stay in the action graded OPEN.

## What landed (computed-confirmed, survives the adversarial re-run)

- **The substrate is exact.** `Cl(9,5) = M(64,H)`; self-dual `su(2)_+` in `so(9,5)`; the Casimir split
  `ker(Gamma) = 1664 = 640 (j=0) + 832 (j=1/2) + 192 (j=1)`. The 192-dim `j=1` triplet is the pure
  `Spin(10)` generation spinor (16/16bar), vectorlike (96/96).
- **`mu` exists** and is Krein-real (`|Im mu| = 2.8e-14`), `su(2)`-equivariant (finite-rotation intertwiner
  `1.1e-15`), quaternionic-compatible (`J_q^2 = -1`, defect `2.3e-17`), unique as a Hamiltonian moment map
  (multiplicity 1, `su(2)` simple). **Honest flag:** this is EXISTENCE, not selection. Equivariance is an
  automatic rep-theory theorem -- a *conjugate* `su(2)` gives the same machine-precision equivariance
  (`1.17e-12`). Step 1 was structurally unfalsifiable and carries no GU-specific information.
- **Krein gate.** `K`-anti-self-adjointness exact; triplet signature exactly `(+96,-96,0)`; single-chirality
  `mu` vanishes (`1.3e-13`) while cross-chirality fires (`~112`). `mu` IS the seesaw/Majorana cross term,
  and it survives restriction to the maximal physical (K-positive, dim 96) subspace at image rank 3.
- **Discharge A (dark energy / Assumption 3) -- CONDITIONAL.** Each monopole sector
  `|F_A^s - mu^s(Psi)|^2` is separately gauge-invariant under a genuine finite gauge transformation, both
  chiralities (`4.6e-13`, `1.9e-12`), with no hand-imposed projector, and the Dirac-variation current equals
  the moment-map source exactly (`c_k + i mu_k = 0`). So Noether's second theorem gives `D_A^* Theta^s = 0`
  off-shell. **Honest flag:** this reduces to an `Ad`-invariant-norm tautology once `mu`'s automatic
  equivariance is granted; the action form is POSITED, not derived from GU; and the load-bearing
  differential-geometric step `theta = D_A^*(F - mu)` with the base integral is open-by-construction. A is a
  conditional consistency, not a derivation.

## What was refuted (computed-refuted -- the real deliverable)

- **B1: the SW shell does not reduce the gamma-trace obstruction -- it INCREASES it.** On the `j=1` SW
  carrier, per-mode leakage RMS `= 1.4639` and escape fraction `= 0.2054`, versus off-shell `1.0179` and
  `0.1429` -- a **1.44x worse** leakage per mode on the SW surface. The off-shell floor
  `41.52 = C2/sqrt(14)` survives untouched.
- **B2: the `>=8`-real shiab selector is not collapsed toward GU's `(1,0,1,0)`.** By Schur, an
  `su(2)_+`-equivariant shell cannot reduce `dim Hom`; going on-shell only shrinks symmetry to the
  stabilizer, which *enlarges* the admissible family. No movement toward the GU selector; the 3 residual
  real dims survive.
- **C: the seesaw is refuted.** The fold with `mu`'s actual Majorana block gives light eigenvalue scaling
  `~ t^1` (slope 1.000), not seesaw `t^2`. Cause is structural: `mu`'s block is **vectorlike**
  (`||A_++|| = ||A_--|| = 391.027`), so there is no `m^2/M` suppression. The `{+|mu|, 0, -|mu|}` split is
  just the spin-1 `Jz` weight diagram (a trivial rep fact). **The asserted `+8 = ind_H(D_RS)` is NOT
  computed from `mu`.**
- **Sign / magnitude: not repaired, provably untouchable.** `ch2(S_X)[K3] = -5376` exactly; the genuine
  Dirac index `A-hat[(K3)^4] = 16`; the lone `24` is `chi(K3)` surfacing via `2chi + 3sigma = 0` (a
  disguised import). `mu` is degree-2 homogeneous (measured `1.000000`) while `ch2 = (1/8pi^2) INT tr F^F`
  is a degree-0, connection-independent de Rham bundle invariant -- the SW shell selects a connection on a
  *fixed* bundle and **cannot** change `ch2`. The gap `|ch2|/24 = 224x`, sign negative, is identical to what
  the program already had. **The source action is orthogonal to the count.**
- **Foundation overclaim refuted by its own numbers.** "`mu` is supported on the `j=1` triplet carrying the
  16" is false: `mu` also fires on `j=1/2` (median `0.058`) and vanishes only on `j=0`. The restriction to
  the 192-dim `j=1` sector is an imposed modeling choice tied to the generation-count story, not forced by
  where `mu` lives.

## The deepest finding (a hardened no-go)

**The moment map of a Krein isometry provably cannot supply the chiral asymmetry.** Every GU-native operator
commutes with the quaternionic structure `J_quat`, forcing an even index; `mu` is a Krein-real bilinear of a
Krein isometry, so its heavy block is necessarily vectorlike (net chiral index 0). The `2+1` it produces is
a **mass multiplicity, not a chiral anomaly index**. Therefore the chiral `+8` cannot come from the source
action's own nonlinearity. Two honest exits remain, and the construction forces the choice:
(a) import a non-Krein-isometric (symmetry-breaking) chiral/topological ingredient and show it chiralizes
the vectorlike split, or (b) re-read GU's "3 generations" as a vectorlike mass count, not a chiral anomaly
index, and re-derive the headline accordingly. This hardens the standing quaternionic-parity even-index
no-go and converges with `canon/two-primary-lemma.md`.

## What stays open (named, separated, unmoved)

- **Discharge A base-manifold step.** `theta = D_A^*(F_A^s - mu^s)` and `D_A^* theta = 0` need the
  codifferential and the integral over `X^4` -- differential structure absent from the `Cl(9,5)` fibre.
- **BV master equation `(S,S)=0`** does not close on the symbol algebra. The SW compensator commutes with
  `Pi_RS` (`(I-Pi_RS) sigma_c Pi_RS = 0`, obstruction flat at escape `41.52` / `C2 155.36`), and inserting
  the SW Majorana leg into Koszul-Tate breaks nilpotency (`s^2 = 102.9`). The obstruction lives **off** the
  `Cl(9,5)` symbol algebra (the off-symbol `Y14 = Met(X^4)` connection-curvature). BICOMPLEX-01 re-confirmed
  from the SW direction.
- **Over-determination.** Fixing both `F_A^+ = mu^+` and `F_A^- = mu^-` pins the full curvature (stronger
  than standard 4D SW). Whether this leaves a finite-dimensional moduli space or over-determines `A` into
  rigidity is uncomputed.
- **Velo-Zwanziger ledger.** The anti-trap `||[Pi_RS, M_D]|| = 58.72` is held (RS stays coupled), so
  spin-3/2 causality is genuinely at stake. `S_VZ` unbuilt; VZ hyperbolicity is a PDE-symbol statement not
  finite-dimensionally representable on the fixed algebra.
- **Selector collapse to `(1,0,1,0)`** -- untouched; the count may be observer-relative.

## Per-discharge grade card

| Item | Grade |
| --- | --- |
| Substrate (Cl(9,5), Casimir split, Krein signature) | computed-confirmed (exact) |
| `mu` exists, equivariant, Krein-real, quaternionic | computed-confirmed -- but EXISTENCE-not-selection (unfalsifiable) |
| Krein gate (cross-chirality, physical-subspace rank 3) | computed-confirmed |
| A: dark energy / Assumption 3 | PARTIAL / conditional (tautological core; codifferential step open) |
| B1: SW shell reduces the obstruction | computed-REFUTED (1.44x worse) |
| B2: selector collapses to (1,0,1,0) | computed-REFUTED (Schur; no collapse) |
| C: seesaw hierarchy + chiral `+8` | computed-REFUTED (vectorlike, `t^1`, `+8` not computed) |
| Sign/magnitude (-5376 vs 24) | computed-confirmed NEGATIVE (orthogonal, unrepaired) |
| BV master equation `(S,S)=0` | OPEN (off the symbol algebra) |
| Velo-Zwanziger | OPEN (unbuilt; not representable on the fibre) |

## Next computations (the named frontier)

1. **Doubled-monopole deformation complex.** Compute the linearized index / moduli dimension of
   `(F_A^+=mu^+, F_A^-=mu^-, D_A Psi=0)`; decide moduli vs rigidity. If over-determined, test absorbing
   `mu^-` into the Krein Dirac constraint instead of a second monopole term.
2. **Chiral-import test.** Identify the minimal non-Krein-isometric ingredient that could chiralize the
   vectorlike split; if none works, formally re-read "3" as a vectorlike mass count.
3. **BV lift off the symbol algebra.** Lift `sigma_c` to the full `Y14` geometry; test whether any
   non-`Cl(9,5)`-native compensator closes `(S,S)=0`, or ratify BICOMPLEX-01 as a standing no-go.
4. **Global index under the SW shell.** Compute `ch2` with `F_A^+ = mu^+(Psi)` imposed to rigorously confirm
   orthogonality to `-5376` (beyond the degree-homogeneity proxy).
5. **VZ unitarity ledger.** Build the characteristic determinant of the doubled RS operator over `T*X^4` and
   test hyperbolicity.
6. **Selector-dim under the monopole constraint.** Quantify whether any sub-shell collapses the 3 residual
   real dims, or ratify the count as observer-relative.

## Honest bottom line

We did exactly what we set out to do: built the keystone object in its named template and measured it. It is
not a working source action for GU; it is a well-defined algebraic object whose three intended jobs are
refuted or open, with dark energy landing only conditionally. The single most valuable output is the
hardened no-go: **a Krein-isometric source action is structurally orthogonal to the chiral generation
count**, so the count -- if it exists -- requires a symmetry-breaking import or a re-reading as a vectorlike
mass multiplicity. That is a real, GU-independent-flavored result, and it sharpens rather than inflates the
program. (Full numerical output: session task `wir3nolwt`; tests under `tests/source-action/`.)
