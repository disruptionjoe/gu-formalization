---
artifact_type: conditional_build_result
created: 2026-08-07
status: FULL_LINEARIZED_BIANCHI_AND_LABELLED_AMBIENT_NULL_SCREEN_PASS__CURRENT_TOTAL_RAW_UPSILON_GRAPH_FAILS__COUPLED_ALL_GRADE_REPAIR_OPEN
source_return: SOURCE-CONFIRMS__RAW_UPSILON_INCLUDES_SHIAB_CURVATURE_PLUS_KAPPA_T_AND_XI_EQUALS_D_UPSILON_REDUNDANCY__SOURCE-SILENT__LINEARIZED_SUPERCONNECTION_BIANCHI_PROOF_AND_LABELLED_AMBIENT_NULL_SCREEN
ledger: lab/process/conditional-physics-ledger-v0.60.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# K77 total raw-Upsilon and labelled ambient null screen

## Result in plain English

Two construction gates pass, and one more complete test exposes a real missing
piece.

First, the four corrected K77 source columns assemble into complete
superconnection tangents. Their full linearized covariant Bianchi identity
vanishes exactly. The earlier odd-curvature packet alone does not satisfy that
identity; both parity pieces of the source tangent are necessary.

Second, a null covector admits an exact labelled ambient screen without ever
dividing by its zero norm. With a reciprocal null label, the screen has rank
12 and signature `(6,6)`, and the Koszul homotopy round-trips all four
curvature packets. This is an ambient K77 form screen, not the separately
constructed four-dimensional `10 -> 6 -> 2` physical null quotient.

Third, the current graph does **not** intertwine Weinstein's complete raw
source object

\[
  \Upsilon_B=\operatorname{Shiab}(F_A)+\kappa_1 T.
\]

The earlier four-column fit correctly cancels the grade-two curvature target.
But it fitted only that curvature contribution. Restoring the source-required
algebraic `kappa_1 T` term leaves nonzero grade-one and grade-two residuals in
every column. The residual family has exact rank four.

So this is not a failure of Bianchi or of the labelled null screen. It is a
failure of the **current curvature-only graph** to carry the complete source
object. The next construction must solve a coupled all-Clifford-grade graph
including `kappa_1 T` before observation Euler or symplectic descent.

## Layer 0

| phrase | object established | object not established |
| --- | --- | --- |
| covariant Bianchi | `D_* delta F + [delta A,F_*]=0` for the complete superconnection tangent | the source's displayed redundant Euler relation `Xi=D Upsilon` |
| raw `Upsilon` | the algebraic source object `Shiab(F_A)+kappa_1 T` | its derivative, Euler covector or Noether identity |
| curvature fit | exact cancellation in the previously fitted grade-two curvature slice | total raw-`Upsilon` naturality across every Clifford grade |
| ambient null screen | a labelled rank-12 `(6,6)` complement of a null pair in K77 | the four-dimensional metric physical characteristic quotient |
| null homotopy | exact algebraic split after retaining a reciprocal null label | a canonical forgetful quotient independent of that label |
| screen descent | configuration-level form decomposition | Euler, preboundary, presymplectic, BV/BFV or Green-domain reduction |

The source writes both `Upsilon_B=Shiab(F_A)+kappa_1 T` and
`Xi=D Upsilon`, but calls the latter a redundant Euler relation. Curvature
Bianchi, raw-`Upsilon` naturality and that Euler redundancy are therefore kept
as three distinct statements.

## Complete source tangent

The corrected fixed-`epsilon` source tangent contains:

- an odd `Cl1` one-form `beta`, whose `q wedge beta` contribution owns the 28
  principal connection coefficients; and
- an even `Cl2` one-form `alpha`, whose nonzero-background Cartan response
  owns the transverse 117 coefficients.

They are assembled as one superconnection tangent
`delta A=alpha+beta`. The Clifford realization uses

\[
 J^{ab}=-\tfrac12\eta^{aa}\eta^{bb}\gamma_a\gamma_b,
\]

where the minus sign reconciles the source convention
`K(alpha)=[alpha,Phi_1]` with the curvature assembly convention
`[Phi_1,alpha]`. After that single global convention conversion, the odd
endpoint-curvature pieces equal all four unique inverse-Shiab packets
coefficientwise and retain family rank four.

## Full linearized Bianchi theorem

For `A_*=q+T_*`, `F_*=T_* wedge T_*`, and each complete `delta A`, the probe
evaluates

\[
 D_*\delta F + [\delta A,F_*].
\]

All four residuals vanish exactly. A planted calculation retaining only the
previously fitted odd curvature packet is nonzero on every column. Thus the
identity is informative: it requires the parity-complete source tangent and
does not merely certify the old split.

## Total raw-Upsilon obstruction

The graph residual uses the complete linearization

\[
 \delta\Upsilon_B
 = *\,\delta\operatorname{Shiab}(F_A)+\delta T
\]

at the fixed selected frame with `kappa_1=1`. The existing direct graph target
still cancels the grade-two curvature contribution exactly. The complete
residual nevertheless has:

| invariant | exact result |
| --- | ---: |
| four-column family rank | 4 |
| live grade-one coordinates | `14,14,14,14` |
| live grade-two coordinates | `57,34,34,34` |
| zero columns | 0 |

This does not prove that no total graph exists. It kills only the current
curvature-only fit. A lawful repair must solve the coupled grade-one and
grade-two equations without adding an unpriced field or deleting the source's
`kappa_1 T` term.

## Labelled ambient null screen

Choose

\[
 q=(1,1,0,\ldots,0),\qquad
 \ell=(\tfrac12,-\tfrac12,0,\ldots,0),
\]

in the settled `(7,7)` metric. Both are null and `q dot ell=1`. The projector

\[
 P=1-q^\sharp\otimes\ell-\ell^\sharp\otimes q
\]

has rank 12, kills both null legs and restricts to signature `(6,6)`. The
homotopy split

\[
 \omega=q\wedge\iota_{\ell^\sharp}\omega
       +\iota_{\ell^\sharp}(q\wedge\omega)
\]

round-trips every tested inverse-Shiab packet exactly, and every first term is
`q`-closed. No division by `q^2` occurs.

A null rotation produces another reciprocal `ell'` with the same pairing but
changes a held-out split. Hence the screen is not basic after forgetting the
reciprocal label. The v0.59 full labelled reduction can own that label modulo
its central stabilizer, but the label must remain through variation until its
degeneracy is derived.

## Constraint-surplus accounting

| item | result |
| --- | ---: |
| new fields or data | 0 |
| fitted total-graph freedom | not constructed |
| full-Bianchi identities counted as independent constraints | 0 |
| screen homotopy identities counted as independent constraints | 0 |
| current total raw-`Upsilon` residual rank | 4 |
| residue or quotient count change | 0 |
| P1/P2/P3 | unchanged and unused |

The screen depends on already retained labelled reduction data; it is not
booked as a new external datum or physical quotient. Bianchi and the homotopy
formula are identities and add no constraint surplus.

## Lightweight specialist pre-assessment

| lens | decisive question | result |
| --- | --- | --- |
| differential geometry | is the complete connection tangent used? | yes; odd and even source components are assembled together |
| superconnection algebra | does full Bianchi close? | yes on all four columns; odd-only control fails |
| hyperbolic PDE | can the non-null Koszul inverse be used at `q^2=0`? | no; a reciprocal null screen is used instead |
| symplectic geometry | is the screen already a physical phase-space quotient? | no; Euler and preboundary classes are absent |
| representation theory | which grades remain after the total source test? | grades one and two, in a rank-four family |
| source archaeology | what object did Weinstein actually write? | raw `Upsilon` contains both Shiab curvature and `kappa_1 T` |
| Krein/operator theory | is a common positive or closed domain produced? | no |
| exact computation | are the conclusions coefficientwise? | yes; rational/Clifford sparse identities with planted failures |

## Seven-axis disposition

| layer | disposition |
| --- | --- |
| Layer 0 | Bianchi, raw `Upsilon`, `Xi=D Upsilon`, ambient screen and 4D physical quotient separated |
| L1 source | `SOURCE-CONFIRMS` the two-term raw `Upsilon`; source is silent on the repo's Bianchi proof and labelled screen |
| L2 algebra | parity-complete tangent, rank-four defect and null homotopy exact |
| L3 geometry | labelled ambient screen exists; forgetful screen is noncanonical |
| L4 variation | curvature-only fit fails the total raw object; Euler/preboundary open |
| L5 covariance | full linearized superconnection Bianchi exact; total graph naturality fails |
| L6 analytic | no common Green/Krein domain or hyperbolic boundary theorem |
| L7 physics | no Einstein, cosmology, spectrum, positivity or Standard Model recovery claim |

## Progress and next gate

```text
Ledger v0.60 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 2
  - full linearized superconnection Bianchi on all four columns
  - labelled ambient rank-12 null screen without q-squared normalization
frontier_conditions_opened: 1
  - coupled all-grade total raw-Upsilon graph repair
remaining_named_conditions: 2
  - coupled all-grade total raw-Upsilon naturality including kappa_1 T
  - observation Euler/preboundary/symplectic and common-domain descent
```

Next solve the coupled all-grade raw-`Upsilon` graph including the mandatory
`kappa_1 T` term. Only a survivor advances to observation Euler, preboundary
and symplectic descent on the labelled ambient null screen. The exact
executable probe passes `43/43`.
