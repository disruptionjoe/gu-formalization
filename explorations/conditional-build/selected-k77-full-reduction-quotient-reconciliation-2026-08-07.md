---
artifact_type: conditional_build_result
created: 2026-08-07
status: SOURCE_OWNED_FULL_REDUCTION_QUOTIENT_BASIC__HORIZONTAL_PLANE_FORGETFUL_QUOTIENT_FAILS__OBSERVATION_EULER_OPEN
source_return: SOURCE-CORRECTS__FULL_LABELLED_CLIFFORD_REDUCTION_ALREADY_OWNED_BY_SOURCE_EPSILON__SOURCE-SILENT__OBSERVATION_SECTION_AND_PHYSICAL_EULER_DESCENT
ledger: lab/process/conditional-physics-ledger-v0.59.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# K77 full-reduction quotient reconciliation

## Result in plain English

The previous Run proved a real failure, but attached it to a quotient that
forgets too much of the source configuration.

If one remembers only the horizontal four-plane, a normal frame rotation
leaves that plane unchanged while changing all four source lifts. The map is
therefore not basic on that forgetful quotient. That v0.58 theorem remains
exact.

But the repository had already constructed a richer, source-owned object:

\[
 \gamma_\epsilon
 =\operatorname{Ad}(\epsilon^{-1})\gamma_0:
 C\longrightarrow\operatorname{ad}(P_H).
\]

It is a full **labelled** Clifford reduction, dependent on Weinstein's source
`epsilon`, not a newly supplied frame. Its stabilizer inside the complexified
Krein-unitary group is the scalar `U(1)`. That center acts trivially in the
adjoint representation. Consequently the paired object
`(gamma_epsilon,L_epsilon)` is well-defined on the source-owned reduction
orbit even though its image after forgetting `gamma_epsilon` is not.

The alternative suggestion—replace the fitted lift by a block-stabilizer
invariant map—is now closed for the same four targets. The Cartan/Spencer map
has a unique inverse, and that inverse lies outside the exact three-dimensional
invariant Hom span.

This advances the action geometry to total raw-`Upsilon` Bianchi/naturality and
the null screen. It does **not** construct the observation-section pullback,
Euler covector, preboundary current, reduced symplectic class, Green domain or
physical spectrum.

## Layer 0

| phrase | object established | object not established |
| --- | --- | --- |
| source `epsilon` | a gauge transformation/nonlinear sigma field in the source configuration | an observation section `s:X->Y` |
| `gamma_epsilon` | the dependent full labelled Clifford map `Ad(epsilon^-1)gamma_0` | the four-plane after its labels/reduction are forgotten |
| basic quotient | the orbit of paired `(gamma_epsilon,L_epsilon)` modulo the central stabilizer | the horizontal-plane-only quotient killed by v0.58 |
| invariant replacement | no member of the three-map block-invariant Hom span reproduces the targets | a differently typed target or smaller source-selected geometry |
| symplectic descent | none | a basic Euler/preboundary class on the reduced covariant phase space |

This is a Layer-0 correction, not a retraction of the calculation. v0.58 and
the August 5 global-reduction theorem compare different retained objects.

## Repo and source collision

The decisive predecessor is
[`k77-global-chimeric-spin-reduction-and-support-normalization-2026-08-05.md`](k77-global-chimeric-spin-reduction-and-support-normalization-2026-08-05.md).
It proves, on the oriented/time-oriented K77 branch and relative to the
admitted spin structure on `X`, that:

1. `C=Sym2(pi*T*X) plus pi*T*X` has an induced global Spin(7,7) lift;
2. `P_H` is the chimeric-spinor frame extension, not an independent gauge
   bundle;
3. Clifford multiplication supplies `gamma_0:C->ad(P_H)`; and
4. source `epsilon` transports all fourteen labelled Clifford directions.

Its primary-source return was already `SOURCE-CORRECTS`, grounded in the
Portal and TOE passages that construct `P_H`, identify the adjoint with the
Clifford/exterior algebra, and rotate the invariant `Phi` by `epsilon`.
Accordingly v0.58's `SOURCE-SILENT` statement was too broad at this locus. The
source remains silent about the later observation-section and Euler descent.

## Exact stabilizer theorem

The faithful real K77 Clifford module has

\[
 \operatorname{Cl}(7,7)\cong M_{128}(\mathbb R).
\]

The fourteen labelled matrices `gamma_0(c)` generate that full real matrix
algebra. Therefore their real commutant is `R*1`; after complexification the
commutant is `C*1`. Intersecting with `U(64,64)` gives the scalar `U(1)`.
Every element of this stabilizer acts trivially by conjugation on the adjoint
carrier.

Hence, if two representatives `epsilon_1` and `epsilon_2` determine the same
labelled reduction, their ratio is central and they determine the same
adjoint-valued lift. The map

\[
 [\gamma_\epsilon]\longmapsto L_\epsilon
\]

is well-defined on the full-reduction orbit.

An exact rational Spin rotation supplies a noncentral control: it moves
`gamma_1 -> gamma_2`, `gamma_2 -> -gamma_1`, moves the fitted source lift, and
preserves the Spencer and endpoint equations. The central representative
`-1` fixes both.

## Why the v0.58 failure survives

The forgetful map

\[
 (\gamma_\epsilon,L_\epsilon)
 \longmapsto (H,L_\epsilon)
\]

throws away the labelled normal Clifford directions. Its fibre contains the
normal `(4,5)` rotation used by v0.58. That rotation fixes `H` pointwise but
changes the lift with rank four and 80 nonzero entries. Therefore no map on
the horizontal-plane-only quotient pulls back to the fitted lift.

This is useful rather than contradictory: it identifies exactly which source
field must remain in the configuration until Euler and symplectic reduction
decide whether it is gauge, physical, or constrained.

## Invariant replacement is not a second route

The oriented block-stabilizer invariant maps form the exact span of horizontal
metric contraction, normal metric contraction and horizontal volume
contraction. Directly applying the Spencer map to those three families yields
a rank-three target span. Adjoining the actual four K77 targets raises the
rank to four; exact `linsolve` returns `EmptySet`.

Independently, the Spencer inverse round-trips all three invariant families and
the fitted family. Its uniqueness means any lift reproducing the same targets
must equal the fitted `L`, which is not in the invariant span. Thus the
invariant-replacement horn is closed for these targets, not merely unfound.

## Constraint-surplus accounting

| item | result |
| --- | ---: |
| new fields or data | 0 |
| new Clifford-frame coefficients | 0 |
| fitted pointwise coefficient freedom | 0 |
| residual stabilizer | scalar `U(1)` |
| residual stabilizer action on adjoint lift | trivial |
| transport identities counted as independent constraints | 0 |
| block-invariant replacements reproducing the targets | 0 |
| P1/P2/P3 | unchanged and unused |

The full reduction is already dependent on source `epsilon`, so its use does
not add another function-valued datum. The transport equations are
tautological consequences of the orbit construction and are not counted as
surplus. No residue or quotient count is reduced yet because the physical
Euler/BV quotient has not been constructed.

## Lightweight specialist pre-assessment

| lens | decisive question | result |
| --- | --- | --- |
| differential geometry | which reduction is retained? | full labelled Clifford reduction, not merely the horizontal plane |
| principal bundles | what is its stabilizer? | scalar `U(1)` after complexification |
| representation theory | does the stabilizer act on the lift? | its adjoint action is trivial |
| source archaeology | is the reduction added by the repo? | no; source `epsilon` and source-owned `P_H` supply it |
| repo archaeology | was this already constructed? | yes; the August 5 global-reduction result was not composed into v0.58 |
| variational PDE | does configuration descent give field equations? | no; raw residual, null screen and Euler remain open |
| symplectic geometry | is there a reduced presymplectic class? | not until Euler/preboundary basicness and degeneracy are computed |

## Seven-axis disposition

| layer | disposition |
| --- | --- |
| Layer 0 | full labelled reduction, horizontal-plane forgetful image, observation section and symplectic quotient separated |
| L1 source | `SOURCE-CORRECTS` at full-reduction ownership; `SOURCE-SILENT` at observation/Euler descent |
| L2 algebra | centralizer and invariant-Hom obstruction exact |
| L3 geometry | paired full-reduction orbit is basic; forgetful plane quotient fails |
| L4 variation | pointwise endpoint/Spencer equations preserved; total raw residual and Euler open |
| L5 covariance | source-configuration orbit descent exact; physical observation/BV quotient open |
| L6 analytic | null screen, Green domain and trace compatibility open |
| L7 physics | no Einstein, cosmology, spectrum, positivity or Standard Model recovery claim |

## Progress and next gate

```text
Ledger v0.59 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 2
  - source-owned full-reduction ownership/stabilizer basicness
  - block-invariant replacement for the same four targets
frontier_conditions_opened: 0
remaining_named_conditions: 2
  - total raw-Upsilon Bianchi/naturality plus null characteristic screen on
    the full reduction
  - observation Euler/preboundary/symplectic and common-domain descent
```

Next construct total raw-`Upsilon` Bianchi/naturality on the source-owned full
reduction and a null characteristic screen without non-null normalization.
Only a survivor advances to the observation-section Euler, preboundary and
symplectic descent. The exact executable probe passes `38/38`.
