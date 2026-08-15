---
title: "Eric/Curt Wave 3D-B2C2 parallel: null-Clifford factorization and full-Omega1 completion"
status: active_research
doc_type: construction_result
created: 2026-07-31
work_item: ECW3D-B2C2-PARALLEL-NULL-CLIFFORD-FULL-OMEGA1-COMPLETION
registry: lab/process/eric-curt-wave3d-b2c2-null-clifford-omega1-completion.json
probe: tests/channel-swings/eric_curt_wave3d_b2c2_null_clifford_omega1_completion_probe.py
grade: "EXACT PRINCIPAL-SYMBOL COMPLETION on the source-stated full one-form spinor carrier. The isolated ker-Gamma W131 Jordan sector is exactly the projected-twistor image of null Dirac spinors. Restoring the forced gamma-trace spinor companion reconstructs 1 tensor c(k), removes the rank-128 Jordan remainder, admits the identity positive right-H symmetrizer on the admitted Lorentz section, and retains the rank-512 observed one-form carrier. This is not yet the rolled source action, an off-shell BV complex, an analytic domain, or a generation/index result."
---

# Wave 3D-B2C2 parallel — null-Clifford factorization and full-`Omega1` completion

## Result

The B2B Jordan obstruction is real for the isolated gamma-traceless
Rarita--Schwinger carrier, but it is not present on the source-stated full
spinor-valued one-form carrier.

The target-blind candidate

\[
F(k)=\Pi_{\ker\Gamma}\bigl(k\otimes c(k)\bigr)
\]

was frozen using only the covector `k`, Clifford multiplication `c(k)`, and
the existing gamma-trace projector. It used no characteristic-root
projector, Jordan eigenvector, `|xi|^{-1}`, fitted coefficient, or external
datum. On ten nonzero null covectors it has rank 64, is intrinsically
gamma-traceless, is right-`H` invariant, and is killed by the matching W131
symbol. Only after those tests were frozen was it compared with B2C1's held-
out targets. For every tested direction and both characteristic roots,

\[
\operatorname{im}F(k)
=\text{the held-out rank-64 characteristic-null half},
\]

and the two opposite-root images are disjoint and span the complete rank-128
Jordan image.

This does **not** make the Jordan image gauge. The exact identity is instead
an on-shell Dirac--twistor--RS factorization. With

\[
T(k)=\Pi_{\ker\Gamma}(k\otimes-),\qquad
Q(k)=\Pi_{\ker\Gamma}(1\otimes c(k))\Pi_{\ker\Gamma},
\]

and `n=14`, the probe verifies

\[
F(k)=T(k)c(k),\qquad
Q(k)T(k)=\frac{n-2}{n}T(k)c(k),
\]

so

\[
Q(k)F(k)=\frac{12}{14}q(k)T(k).
\]

It vanishes on the null cone because `q(k)=0`. Off-null and wrong-root
controls fail. Because `F` is quadratic in `k`, it is not the symbol of the
missing ordinary first-order BV arrow without an additional detour or
intermediate-field construction.

## The full-carrier completion

The natural orthogonal splitting is

\[
T^*Y\otimes S=\operatorname{im}\Gamma^\dagger\oplus\ker\Gamma.
\]

Instead of quotienting the defective W131 sector, the second phase restores
the omitted trace-spinor summand and derives every block from the unprojected
one-form Clifford symbol

\[
M(k)=1\otimes c(k).
\]

In the normalized gamma-trace splitting, its tested block form is

\[
U^\dagger M(k)U=
\begin{pmatrix}
-\frac{12}{14}c(k) & B(k)\\
\frac{2}{\sqrt{14}}T(k) & Q(k)
\end{pmatrix},
\]

where `B(k)` is the corresponding derived return block. No block coefficient
was adjusted after seeing the obstruction. The complete matrix satisfies

\[
\bigl(U^\dagger M(k)U\bigr)^2=q(k)I
\]

on base, time, generic section, and generic ambient controls.

On the admitted `(3,1)` section this completion has:

- the identity as a positive simultaneous symmetrizer;
- exact right-`H` compatibility;
- zero Jordan remainder, versus rank 128 and square-zero for isolated
  `ker Gamma`; and
- the full rank-512 observed one-form carrier, rather than a quotient that
  erases it.

A conservative direct sum with the `Omega0(S)` Dirac principal block is also
positive symmetric. That direct sum is a control, not a claim that the
spoken rolled two-by-two operator is block diagonal.

## Layer 0: what changed

The earlier gates asked whether the isolated `ker Gamma` operator could be
repaired by a gauge quotient. That is a valid question about the W131
summand, and their negative answers remain valid. It is not yet the same
question as whether Eric's full fermion carrier is hyperbolic.

| object | this swing's meaning | disposition |
| --- | --- | --- |
| W131 | compressed symbol on `ker Gamma` | defective; B2B retained |
| rank-64 root half | on-shell image `im T(k)c(k)` | explained, not declared gauge |
| full `Omega1(S)` | trace spinor plus `ker Gamma` | exact principal completion |
| BV differential | off-shell nilpotent tangent map | still unbuilt |
| generation/count | observed chiral/index object | not inferred from summands or ranks |
| external datum | P1/P2 orientation and P3 real-`KO` twist | unused; not a projector or symmetrizer |

Thus B2C2A and this result are complementary. B2C2A proves the ordinary
`tau`/BRST complex has the wrong carrier. This swing shows that a quotient
inside that carrier is not the only next move: the source-stated full odd
carrier already contains a forced companion that cures the principal defect.

## Primary-source collision

Leading carrier disposition: `SOURCE-CONFIRMS`.

- The complete TOE ledger's `WG-F01` records
  `Omega^0(Y,S) direct-sum Omega^1(Y,S)` as the fermion carrier.
  **[CN-2 S-TYPING: S-CHIRALITY-UNTYPED]** `S` is unsubscripted; this line does
  not fix which Weyl halves the two slots carry, and nothing below depends on
  fixing them. The same-half reading `S-HALF-SAME` is stated by neither primary
  (`canon/escape-corners-campaign-RESULTS.md`, A2 `REFUTED-AS-FILED`); eq (9.16)
  declares `S-FULL-DIRAC`; the spoken declaration is the opposite-half
  `Omega^0(S+) + Omega^1(S-)`. Fork unresolved here.
- The TOE transcript at `02:28:46--02:31:53` explicitly separates the
  zero-form spinor, Clifford-contracted one-form spinor, and kernel pieces.
- `WG-X01--WG-X04` and the TOE transcript at `02:38:12--02:42:55` describe a
  rolled Dirac--de Rham/RS construction, the shortened
  `0 -> 1 -> 13 -> 14` degree skeleton, and a prospective two-by-two operator.
- The UCSD transcript at `00:32:46--00:36:13` likewise places the full
  zero-form/one-form spinor content in the unified-field arena.

Exact-operator disposition: `SOURCE-SILENT`.

The public source does not supply the full rolled matrix, its middle Shiab
map, signs, coefficients, two-connection dependence, lower-order terms,
domain, or BV law. `b5-middle-source-freeze-2026-07-21.md` already records
that boundary and is retained. Therefore `1 tensor c(k)` is an exact
repo-derived principal completion and a discriminator for the next action;
it is not attributed to Weinstein as the finished rolled operator.

## Seven-axis read

| axis | result |
| --- | --- |
| L1 algebra | exact Clifford/twistor identities and target-blind collision pass |
| L2 representation | gamma-trace splitting and right-`H` invariance pass |
| L3 geometry | tested on the established `(9,5)` carrier and admitted `(3,1)` section; global curved bundle operator open |
| L4 dynamics | positive symmetric principal evolution passes; lower-order action, constraints, and nonlinear propagation open |
| L5 observation | rank-512 section one-form carrier retained; full equation descent open |
| L6 physics | no Higgs/Yukawa/mass/chirality/count recovery claimed |
| L7 empirical | no new phenomenological prediction or fit claimed |

The algebraic block completion has zero fitted parameters. Its mathematical
constraint surplus is therefore positive at the tested principal-symbol
scope. Physical surplus is not computable until the rolled action and its
observation map are written.

## Non-regression and boundary

- B2B remains decisive for isolated `ker Gamma`.
- B2C1's previous projected gauge quotient remains killed.
- B2C2A's ordinary `tau`/BRST carrier mismatch remains decisive.
- P1/P2/P3 remain intact, unused, and identically priced.
- The prior four-dimensional source-action build is not overwritten; this
  result tells it which full fermion carrier must be varied next.
- Curt's literal `(7,7)` carrier remains a separate rival inside the Eric
  lane. `TG-1 AND TG-2 AND TG-3` remains false, so no third lane is promoted.
- No stationarity, BV closure, analytic domain, mass, index, generation
  count, cosmological prediction, or Standard Model recovery is claimed.

The executable probe passes `36 exact + 12 planted = 48` checks.

## Next gate

`ECW3D-B2C3-ROLLED-OMEGA0-OMEGA1-SOURCE-ACTION-AND-SHIAB-MIDDLE-BLOCK`

Construct the actual first-order rolled `Omega0(S) direct-sum Omega1(S)`
source action rather than a quotient of isolated `ker Gamma`. The gate must:

1. derive the `0 -> 1 -> 13 -> 14` middle map, adjoints, signs, and
   coefficients from the source-shaped action grammar;
2. show whether its principal symbol is, contains, or legitimately differs
   from the positive full-carrier completion above;
3. derive the odd Noether/BV differential and curved lower-order closure;
4. couple the previously constructed distortion, connection, Krein pairing,
   zero-order `P0/rho/Y_K/Y_C/C` placement, and observation maps; and
5. retest no-leakage, right-`H`, trace-reversed Frobenius-fibre compatibility,
   analytic domain, and P1/P2/P3 non-regression.

Failure of the source-shaped rolled action to retain the forced companion is
now informative: it must either generate a separate constraint that removes
the Jordan chains without erasing observation, or accept loss of positive
Lorentz-section hyperbolicity at this scope.
