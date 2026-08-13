---
title: "G3 full variational bicomplex and BV--BFV: coupled Ward closure, a real preboundary packet, and a section-scope correction"
status: active_research
doc_type: construction_result
created: 2026-07-31
branch: agent/weinstein-guided-source-action
run: archived private execution record
specification: lab/specifications/g3-graph-variation-noether-bvbfv-packet-2026-07-31.md
certificate: lab/process/g3-variational-bvbfv-certificate.json
probe: tests/channel-swings/g3_full_variational_bvbfv_probe.py
grade: "G3 SPLIT CONDITIONAL PASS. The selected source-sector action has a graph-complete all-slot bulk derivative, nonzero action-derived preboundary data, an exact coupled first-jet gauge identity, and the ordinary-gauge minimal BV completion required for CME closure through antifield number one. The isolated connection conservation law fails. A required primary-source recheck identifies observation pullback/restriction, not a supplied defect action, as the author-guided four-dimensional route. G4 must build that retract and the domain/polarization; no complete physical BV--BFV theory is claimed."
canon_verdict_change: none
---

# G3 full variational bicomplex and BV--BFV

## Result first

G3 succeeds at the exact level its selected action can own, and it corrects
two overstatements before they can propagate.

First, every actual dependency of the G2 action now has an Euler owner. With

\[
B=A_{\rm LC}(\epsilon_{\rm red},g_{\rm DW}),
\qquad T=A-B,
\]

the source equation is

\[
E_A=E_T^{\rm var},
\]

while the reduction and metric equations receive the formal-transpose return
of the `B`, `T`, Shiab, Hodge, density, trace-line, Krein, and pseudo-musical
responses. There is no independent `B` equation.

Second, gauge conservation is genuinely coupled. In the exact first-jet
fixture, the connection contribution is nonzero off shell and the moving
reduction contribution cancels it:

\[
\langle E_A,-D_A\chi\rangle
+\langle E_\epsilon,\chi\epsilon\rangle
+\text{boundary flux}=0.
\]

So the old shortcut “the connection equation is separately divergence-free”
is false on a nondegenerate control. This is not a failure of gauge
invariance; it is the correct Noether-II structure of a theory with a moving
reference.

Third, the action emits a nonzero thirteen-form preboundary potential and a
nonzero antisymmetric presymplectic current. They are derived from the action,
not guessed as an Atiyah--Bott form. But they are not yet a reduced BFV phase
space: G4 still owes the ultrahyperbolic domain, polarization, and quotient of
the preboundary kernel.

Finally, the ordinary nonabelian gauge sector has the standard minimal BV
completion. Field-antifield terms alone do not close; the ghost-antifield
bracket term is forced. With that term, the coupled Ward identity, gauge
closure, and Jacobi establish the CME through antifield number one at the
bulk algebraic grade.

## Plain English

The action depends on a free connection and on a reference connection built
from the moving geometry. Changing the gauge moves both. If we watch only the
free connection, it looks as though charge is not conserved. When we include
the equation for the moving reference, the two pieces cancel exactly. The
conservation law belongs to the coupled system, not to either piece alone.

Varying the action also leaves a genuine boundary residue. That residue tells
us what the boundary coordinates want to be, but it does not choose which
half are fixed or which solutions are admissible. That is why G4 comes next:
it must turn this preboundary geometry into an actual domain for the
multi-time ambient equations.

There is one important scope correction. G2 chose a source-bulk action and
explicitly left the older matter/defect family out to avoid double counting.
That action simply does not contain the observation section. Its section
derivative is therefore zero by absence.

Before treating this as an Eric-lane failure, we rechecked the verified
Weinstein transcripts. They repeatedly describe building fields and
equations on `Y^14` and pulling them back to `X^4` along a metric section;
they do not supply a delta-supported defect action. So G4's author-guided
task is a pullback/retract and leakage construction. The older N1 defect
action remains a useful repo-originated comparator, but it is not what these
sources instruct us to expect from the bulk action.

## 1. What was varied

The action remains exactly the G2 functional

\[
I_{G2}
=\int_YT\wedge\mathscr S_\epsilon
\left(F_B+\frac12D_BT+\frac13q(T,T)\right)
+\frac{\kappa_1}{2}\int_YT\wedge\flat_1T.
\]

The exact all-slot derivative varies:

- `T` in the leading, derivative, cubic, and pseudo-musical terms;
- `B` in its curvature and covariant derivative;
- the moving native Shiab through the reduction, trace gamma, soldering,
  Hodge star, adjoint projection, Krein dual, and density;
- `flat_1` through the metric/Krein density dual; and
- the first-jet Levi--Civita graph before returning the result to
  `epsilon_red` and `g_DW`.

The rational probe changes all of those slots simultaneously and agrees with
the analytic derivative exactly. Freezing the Shiab response, metric response,
or `delta T=-delta B` graph response is independently rejected.

## 2. The owner equations

At the intermediate `(B,T,S,flat)` level write

\[
\delta I
=\langle E_T,\delta T\rangle
+\langle E_B^\circ,\delta B\rangle
+E_S[\delta S]+E_\flat[\delta\flat]
+\int_{\partial Y}\Theta.
\]

Returning through the graph gives

\[
E_A=E_T,
\]

\[
E_\epsilon
=(D_\epsilon B)^!(E_B^\circ-E_T)
+(D_\epsilon S)^!E_S
+(D_\epsilon\flat)^!E_\flat,
\]

and the analogous metric formula. The complete expression for `E_T` is

\[
E_T
=S(F_B)+\frac12(L+L^!)T+M_\epsilon(T,T)+\kappa_1\flat T.
\]

The G2-killed compressed equation never re-enters.

The formal transposes retain their Green forms. In particular, the
Levi--Civita graph is first order in the metric variation, so its return adds
a second-stage boundary term rather than an algebraic stress tensor alone.

## 3. What the coupled Ward identity decides

The probe includes a gauge parameter with nonzero first jet. It verifies the
full transformations of the two connection jets, the distortion, and the
moving Shiab insertion. The results are:

```text
complete gauge variation                 = 0
connection-owner contribution            != 0
moving-reduction graph contribution       != 0
connection + moving reduction             = 0
```

This directly executes the council's Stueckelberg-shaped kill control. It
rules out isolated off-shell `D_A^!E_A=0` without weakening the coupled gauge
theory.

The same discipline applies to diffeomorphisms. For the natural top-form
action, the weak identity includes the metric and density response and a
boundary term. A frozen-density plant fails exactly.

This source-only identity cannot yet choose among N3's `J_D`, `J_D+J_F`, or
independently soldered current branches. G5 must add a current in common
density-dual types and recompute the joint identity after G4 supplies the
domain-compatible Green/Riesz map.

## 4. Boundary result

The first derivative terms emit

\[
\Theta_{BT}
=\mathcal G_{D_B}(S^!T,\delta B)
+\frac12\mathcal G_{D_B}(S^!T,\delta T),
\]

plus the Green forms generated when `delta B` is returned through the
Levi--Civita/reduction graph. Therefore

\[
\Theta_{G3}\in\Omega^{13,1},
\qquad
\omega_{G3}=\delta_{\mathcal F}\Theta_{G3}
\in\Omega^{13,2}.
\]

The interval comparator proves the Green identity with a nonzero boundary
flux and a nonzero antisymmetric field-space two-form. This is enough to hand
G4 an action-derived preboundary packet.

It is not enough to declare a phase space. The kernel, closed domain,
polarization, corner compatibility, and positive majorant remain open. No
ordinary spacelike hypersurface exists in ambient signature `(9,5)`; G4 must
solve the actual observation/domain problem rather than import a conventional
Cauchy surface.

## 5. Minimal BV result

For the ordinary gauge ghost `c`, the convention-compatible BRST rules are

\[
sA=-D_Ac,
\quad s\epsilon=c\epsilon,
\quad sg=0,
\quad sc=\frac12[c,c].
\]

The minimal action is

\[
S_{\min}
=I_{G2}
+\langle A^+,-D_Ac\rangle
+\langle\epsilon^+,c\epsilon\rangle
+\left\langle c^+,\frac12[c,c]\right\rangle.
\]

The final term is not optional bookkeeping. Although `c+` has antifield
number two, this term is what cancels the master-equation obstruction at
antifield number one. The nonabelian fixture has a nonzero gauge bracket;
omitting the term fails, while closure and Jacobi pass exactly.

This proves only the ordinary gauge-subgroup algebraic/bulk statement. It
does not prove properness, a nonminimal sector, super-IG closure,
diffeomorphism BV closure, matter/RS BV closure, boundary charge closure, or
physical cohomology.

## 6. Observation-pullback/defect correction

The selected G2 action has no `s`, `Z`, defect density, or `s_*` current.
Therefore

\[
E_s^{G2}=0
\]

means “this functional does not see the section.” It does not mean the
section equation is solved. The exact plant adds a nonzero section-dependent
defect and immediately reopens the derivative.

The required primary-source recheck gives the more important positive route:

```text
ambient fields/equations on Y --R_s--> observed fields/equations on X.
```

The exact control now distinguishes this pullback from the opposite-direction
defect pushforward. It also shows that `R_s L_s=1` and even
`R_s D_Y L_s=D_X` do not imply the off-slice condition
`(1-L_s R_s)D_YL_s=0`. G4 must test all three and construct the dual map on
Euler covectors; variation and pullback cannot simply be assumed to commute.

If the later construction uses the N1 defect comparator, it must state a
guidance debit and replacement registry. A viable route is to keep the G2
source bosonic term as the bulk connection/distortion owner while adding only
nonduplicated N1 matter and defect terms. It may not also retain the N1 bulk
Yang--Mills/parent/bridge family without a proved equivalence or replacement
map.

## 7. Datum and constraint surplus

No physical coefficient was added. The graph transposes, preboundary forms,
and ghost bracket are forced by the action and gauge algebra. P1/P2/P3 remain
untouched. Boundary polarization, reduction component, domain, stationary
orbit, physical projections, normalization, and P3 remain unpriced, so the
global surplus is still `UNCOMPUTABLE`.

## 8. Next swing

G4 now has a concrete input rather than a generic request for boundary data:

1. construct an observation lift/retract with `R_s L_s=1`;
2. impose the off-slice leakage test;
3. build a closed Krein domain and positive majorant compatible with
   `Theta_G3` and `omega_G3`;
4. choose or enumerate admissible boundary polarizations without using P1,
   P2, P3, the SM spectrum, or PP3 as a target; and
5. return the Green/pseudo-musical packet G5 needs for the current weld.

This ordering is now a standing Eric-lane rule: when a construction appears
to lack an expected mechanism, first run a timestamped positive/negative
recheck of the verified Weinstein source set, then distinguish “not supplied
by the source” from “supplied but unbuilt” and “computed and killed.” The
receipt for this case is
`lab/sources/g3-weinstein-section-pullback-recheck-2026-07-31.md`.

## Validation and boundary

The new exact probe reports:

```text
G3-FULL-VARIATIONAL-BVBFV:
25 exact checks + 13 planted failures = 38 PASS
```

G1, G2, RB1b, RB1c, RB2, and N3 remain regression dependencies.

No selected domain/polarization, complete defect theory, full BV--BFV
cohomology, source/N1 equivalence, vacuum, Standard Model realization,
anomaly cancellation, index, observed generation count, cosmological
amplitude, or PP3 is claimed.
