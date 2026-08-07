# Selected K77 coupled all-grade raw-Upsilon graph

Status: `UNIQUE CONDITIONAL GRAPH CONSTRUCTED; TARGET NOT DERIVED; EULER OPEN`

## Result

The v0.60 failure was a failure of the **old curvature-only lift**, not an
obstruction to the full source response.  On the already admitted finite K77
source-tangent carrier

\[
  \Omega^1\!\left(\mathrm{Cl}_1\oplus\mathrm{Cl}_2\right),
  \qquad \dim=14(14+91)=1470,
\]

the source-displayed linearized raw-`Upsilon` response at the selected
nonzero-`kappa_1` background is

\[
  R(\delta A)=*\,\operatorname{Shiab}(D_A\delta A)
               +\kappa_1\delta A .
\]

Its exact sparse matrix has:

```text
domain dimension                         1470
finite output coordinate support         4330
output Clifford grades                   1, 2, 5
rank                                     1470
nullity                                     0
cokernel dimension in that support       2860
```

An independent Sage/FLINT sparse matrix over `QQ` reproduces rank `1470` and
nullity zero; it does not reuse the probe's retained-representation echelon
solver.

The domain was declared before the four physical comparator columns were
read.  Each fixed conditional target `-J_2D` lies in the image and therefore
has one unique all-grade preimage.  Their supports are `71,48,48,48`; their
Clifford-grade-one supports are `10,13,13,13`; their grade-two supports are
`61,35,35,35`.  The family has rank four.

For every column, the grade-one and grade-five response cancels internally
and the complete response is exactly the required pure-grade-two target.
Omitting `kappa_1 T` or reversing its sign makes all four columns fail.  A
grade-three output plant is outside the response image.  Thus this is not an
output-space counterterm defined as the negative residual: it is the unique
inverse of an independently declared source response.

The new lifts differ from every v0.60 curvature-only lift.  Their unique
source-tangent corrections cancel the old residuals exactly, satisfy the full
linearized superconnection Bianchi identity, intertwine three independent
K77 signed rotations, and obey the paired three-patch full-labelled-frame
descent law.  Freezing the graph while the labelled frame moves fails.

## Layer 0

| phrase | object established here | object kept distinct |
| --- | --- | --- |
| raw `Upsilon` | source-displayed `Shiab(F_A)+kappa_1T` and its pointwise linear response | `Xi=D Upsilon`, curvature Bianchi and the action Noether identity |
| graph target | the repo's fixed conditional `-J_2D` four-column comparator | a source-quoted transformation law or a derived physical Euler equation |
| graph construction | the unique inverse of `R` on the finite `Cl1+Cl2` tangent | an arbitrary coordinate-wise `-residual` counterterm |
| descent | paired configuration descent with the full labelled reduction | observation-section Euler, preboundary or reduced symplectic descent |
| null carrier | the retained labelled ambient rank-12 screen from v0.60 | the separate four-dimensional `10 -> 6 -> 2` physical quotient |

The source confirms the two terms in raw `Upsilon`.  It is silent on the
conditional `-J_2D` columns and on identifying them with the physical graph.
The result is therefore a **conditional construction**, not a derivation of
the target.

```text
SOURCE-CONFIRMS:
  raw Upsilon is Shiab curvature plus kappa_1 T.

SOURCE-SILENT:
  the conditional -J_2D target and its identification with the physical
  observation graph.
```

## Constraint-surplus accounting

The fixed-target source coefficients have zero freedom because `R` is
injective.  The response occupies a 1,470-dimensional image inside a
4,330-coordinate finite support, so each accepted target satisfies 2,860
cokernel compatibility equations.  These are reported as **target
compatibility codimension**, not inflated into local predictive surplus:
the rank of the equations determining the 1,470 source coefficients is also
1,470, hence the local fitted-parameter surplus is zero.

No new local coefficient, field, functional datum or quotient is introduced.
`P1/P2/P3` remain unchanged and unused.  The result earns construction value
because it removes the all-grade inconsistency without new freedom; it does
not yet earn prediction value because the target is supplied by the
conditional physics map.

## Divergent specialist review

| lens | question | disposition |
| --- | --- | --- |
| differential geometry | is the inverse applied to a connection tangent rather than an output counterterm? | yes |
| superconnection algebra | do the repaired lifts remain derivatives of one endpoint curvature? | yes; full linearized Bianchi vanishes for all four |
| representation theory | are grades and carrier ranks explicit? | yes; input grades 1/2, output support grades 1/2/5, rank 1470 |
| variational PDE | is `-J_2D` being sold as an Euler covector? | no; it remains a conditional comparator |
| hyperbolic PDE | is the ambient null screen promoted to a well-posed domain? | no |
| symplectic geometry | is configuration descent confused with a preboundary or phase-space class? | no; those are the next gate |
| Krein/operator theory | is positivity or a common closed domain inferred? | no |
| source criticism | which half is source-owned? | `R` is source-owned; the four target columns are source-silent |
| exact computation | does an independent engine reproduce the rank? | yes; Sage/FLINT gives rank 1470 and nullity zero; omitted/wrong-sign `kappa` and grade-three plants fail |
| constraint surplus | does uniqueness become prediction? | no; zero coefficient freedom and zero local predictive surplus are both recorded |

## Hostile review

Both mandatory charges fire as useful fences.

1. **Summary outruns artifact:** calling the rank-1,470 map an automorphism of
   the output carrier would be false; it is an injective map into a
   4,330-coordinate support.  Calling the 2,860-dimensional cokernel positive
   fitted surplus would also overstate the calculation.
2. **Defends superseded or mistyped object:** preserving the unique v0.60
   curvature-only lift would rigorously defend the wrong source object.  The
   full two-term response, rather than the old selected curvature inverse, is
   now primary.

The separate hostile-review artifact records the final fences.

## Seven axes and progress

| axis | disposition |
| --- | --- |
| Layer 0 | raw response, conditional target, graph inverse and Euler object separated |
| L1 source | response formula confirmed; target identification source-silent |
| L2 algebra | exact rank 1470, nullity 0, four unique solutions |
| L3 geometry | full labelled-frame transport and three-patch descent pass |
| L4 variation | pointwise response inverse built; observation Euler/preboundary open |
| L5 covariance | three signed-rotation intertwiners and full Bianchi pass |
| L6 analytic | no common Green/Krein domain or hyperbolic theorem |
| L7 physics | no Einstein equation, spectrum, cosmology or Standard Model recovery claim |

```text
Ledger v0.61 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 1
frontier_conditions_opened: 0
remaining_named_conditions: 1
  - observation-section Euler/preboundary/symplectic and common-domain descent
```

Five rows migrate in distance, mapping grade and evidence only: `LT-GR1`,
`LT-GR2b`, `LT-GR3`, `LT-GR5`, `LT-GR6`.  Verdicts, residue, quotient count,
canon and public posture do not move.

## Next gate

Use the unique all-grade graph inside the selected first-order action and vary
the observation section, full labelled reduction, reciprocal null label,
connection and soldering fields together.  Derive the observation Euler
covector and preboundary current before attempting any reduced symplectic,
BV/BFV, Green-domain or physical-spectrum statement.

The executable probe passes `50/50`.
