---
title: "G3 graph-complete variation, coupled Noether, and BV--BFV preboundary packet"
status: active_research
doc_type: specification
created: 2026-07-31
branch: agent/weinstein-guided-source-action
run: lab/process/runs/GUH-20260731T144734Z-g3-full-variational-bvbfv/run-plan.md
probe: tests/channel-swings/g3_full_variational_bvbfv_probe.py
grade: "CONDITIONAL SOURCE-SECTOR VARIATIONAL/BV PASS. The G2 action has an all-slot graph-complete bulk derivative, action-derived preboundary data, a coupled first-jet gauge identity, and the ordinary-gauge minimal BV completion required for master-equation closure through antifield number one. A primary-source recheck identifies observation pullback/restriction, not a supplied defect action, as the author-guided four-dimensional route. G4 must construct that retract and select a domain/polarization before later matter/current work."
---

# G3 graph variation, Noether, and BV--BFV packet

## 1. Layer-0 field boundary

The word `full` has two meanings that must not be merged.

| object | G3 meaning | not established |
| --- | --- | --- |
| full source variation | every free field and derived graph arrow in the selected G2 functional | variation of the N1 matter/defect functional that G2 explicitly did not combine with it |
| Euler equation | density-dual covector of the written action | a primal one-form or the G2-killed compressed source |
| Noether identity | joint weak identity for all transforming owners | isolated off-shell connection conservation |
| BV theory | ordinary `Gau(P)` minimal sector on the selected graph fields | super-IG, diffeomorphism, RS/matter, nonminimal, or physical BV theory |
| BFV object | preboundary one-form and its field-space differential | reduced BFV phase space, polarization, or closed boundary domain |
| section response | absent from the selected source-bulk functional | either the author-guided observation pullback or the section equation of the repo-originated N1 defect comparator |

The G2 sentence that the metric and section have “analogous graph terms” is
therefore corrected in scope: the metric does, because `B`, `S_epsilon`,
Hodge, density, trace line, Krein dual, and `flat_1` depend on it. The
observation section does not occur in `I_G2`. Its source-only Euler response
is zero by absence, not by cancellation or symmetry.

The required Eric-lane primary-source recheck is recorded in
`lab/sources/g3-weinstein-section-pullback-recheck-2026-07-31.md`. It finds
that the source-guided route reads ambient fields and equations on `X^4` by
pullback along a metric section. It does not find a supplied
delta-supported defect action. These two uses of a section are `HOMONYM` and
must remain separate.

## 2. Free and derived fields

The selected free source-sector fields are

```text
A             free G-connection
epsilon_red   LC-equipped moving reduction
g_DW          native trace-reversed metric data induced from g_X
```

The derived graph is

```text
B       = A_LC(epsilon_red,g_DW)
T       = A-B
S       = S_tr(epsilon_red,g_DW,K,kappa_g)
flat_1  = density-dual pseudo-musical(epsilon_red,g_DW,K,kappa_g)
```

The observation section `s`, spinor `Z`, N1 parent `U/P_IG`, defect fields,
P1, P2, and P3 are not fields of this selected functional. `A0` remains a
comparator. `B`, `T`, and `S` receive no independent antifields because they
are graph composites.

## 3. Primitive all-slot variation

Set

\[
\mathcal C(B,T)
=F_B+\frac12D_BT+\frac13q(T,T).
\]

Before returning to the owners, its variation is

\[
\begin{aligned}
\delta\mathcal C
={}&D_B\delta B
+\frac12\left(D_B\delta T+[\delta B,T]_{\wedge}\right)
+\frac23q(T,\delta T),
\end{aligned}
\]

where `[delta B,T]_wedge=2q(delta B,T)` in the symmetric-polarization
convention. The complete first variation is

\[
\begin{aligned}
\delta I_{G2}
={}&\int_Y\delta T\wedge\mathscr S(\mathcal C)
+\int_YT\wedge(D\mathscr S)[\delta\epsilon,\delta g](\mathcal C)\\
&+\int_YT\wedge\mathscr S(\delta\mathcal C)\\
&+\frac{\kappa_1}{2}
 D\!\left[\int_YT\wedge\flat_1T\right]
 [\delta T,\delta\epsilon,\delta g].
\end{aligned}
\]

This formula carries the Hodge, density, trace-gamma, adjoint pairing, Krein
dual, projector, and pseudo-musical responses inside `D S` and `D flat_1`.
Freezing either response fails the exact finite derivative.

Define primitive covectors operationally by

\[
\delta I_{G2}
=\langle E_T,\delta T\rangle
+\langle E_B^\circ,\delta B\rangle
+E_{\mathscr S}[\delta\mathscr S]
+E_{\flat}[\delta\flat_1]
+\int_{\partial Y}\Theta_{BT}.
\]

`E_B^circ` is an intermediate partial derivative at fixed `T,S,flat`; it
is not an independently imposed field equation.

The exact `T` covector is the G2 result

\[
E_T
=\mathscr S(F_B)
+\frac12(L+L^!)T
+M_\epsilon(T,T)
+\kappa_1\flat_1T.
\]

The killed expression `S(F_(B+T))+kappa_1 flat_1 T` is not used.

## 4. Graph return to the owners

Because `delta T=delta A-delta B`, the owner-level bulk covectors are

\[
\boxed{E_A=E_T,}
\]

\[
\boxed{
E_{\epsilon}
=(D_\epsilon B)^!(E_B^\circ-E_T)
+(D_\epsilon\mathscr S)^!E_{\mathscr S}
+(D_\epsilon\flat_1)^!E_{\flat},
}
\]

\[
\boxed{
E_g
=(D_g B)^!(E_B^\circ-E_T)
+(D_g\mathscr S)^!E_{\mathscr S}
+(D_g\flat_1)^!E_{\flat}.
}
\]

The exclamation marks are density- and boundary-aware formal transposes. The
LC metric derivative contains the standard Palatini first-jet symbol

\[
\delta\Gamma^a{}_{bc}
=\frac12g^{ad}
(\nabla_bh_{cd}+\nabla_ch_{bd}-\nabla_dh_{bc}),
\]

lifted through the moving Spin reduction. Consequently `(D_g B)^!` emits a
second-stage Green term. The reduction derivative likewise splits into a
gauge-orbit part, fixed by equivariance, and transverse reduction variations
whose global components and domain are passed to G4.

There is no independent equation `E_B=0`. The exact fixture finds the
partial `B` derivative generically nonzero and rejects freezing
`delta T=-delta B`.

## 5. Action-derived preboundary data

The first derivative occurrences give the primary Green potential

\[
\Theta_{BT}(\delta)
=\mathcal G_{D_B}(\mathscr S^!T,\delta B)
+\frac12\mathcal G_{D_B}(\mathscr S^!T,\delta T),
\]

up to the declared graded pairing convention. Returning `delta B` to
`delta epsilon` and `delta g` adds the graph Green forms from
`D_epsilon B` and `D_g B`. Thus

\[
\Theta_{G3}
=\Theta_{BT}+\Theta_{\rm LC,epsilon}+\Theta_{\rm LC,g}
\in\Omega^{13,1}(J^\infty\mathcal F).
\]

The covariant presymplectic current is

\[
\omega_{G3}=\delta_{\mathcal F}\Theta_{G3}
\in\Omega^{13,2}(J^\infty\mathcal F).
\]

The exact interval control retains a nonzero Green flux, constructs a
nonzero antisymmetric field-space two-form, and rejects treating the boundary
term as a bulk zero.

This is a **preboundary** packet. G4 must choose a closed Krein domain and an
admissible polarization, then quotient the kernel of the pulled-back
two-form. A nonzero `omega_G3` alone is not a BFV phase space.

The source-only action has no defect density and therefore emits no
four-dimensional moving-section term or bulk-defect corner. The primary
sources do not make that a failure: their stated route is to build fields and
equations upstairs and pull them back along the metric section. G4 must type
that observation map, including the equation-dual map and the question
whether pullback commutes with variation. The N1 bulk-plus-defect action is a
repo-originated comparator; if a later swing uses it, it needs an explicit
guidance debit and a replacement map preventing double counting.

## 6. Coupled gauge Noether identity

For the G1 convention

\[
\delta_\chi A=-D_A\chi,
\qquad
\delta_\chi\epsilon_{\rm red}=\chi\epsilon_{\rm red},
\qquad
\delta_\chi g_{\rm DW}=0,
\]

equivariance gives

\[
\delta_\chi B=-D_B\chi,
\quad
\delta_\chi T=[\chi,T],
\quad
\delta_\chi\mathscr S=[\chi,\mathscr S],
\quad
\delta_\chi\flat_1=0
\]

in compressed notation. The authoritative weak identity is

\[
\boxed{
\langle E_A,-D_A\chi\rangle
+\langle E_\epsilon,\chi\epsilon_{\rm red}\rangle
+\int_{\partial Y}\Theta_{G3}(R_\chi)=0.
}
\]

After a boundary condition kills or controls the flux, integration by parts
gives the corresponding density-dual Noether-II identity. This is the exact
meaning of conservation in G3.

The finite first-jet control includes nonzero `d chi`. Its isolated
connection contribution is nonzero, while the moving-reduction graph term
cancels it exactly. Therefore an off-shell equation of the form
`D_A^!E_A=0` is false on the tested nondegenerate stratum.

## 7. Diffeomorphism identity

For a vector field `xi`, naturality of the fourteen-form Lagrangian gives

\[
\sum_\phi\langle E_\phi,\mathcal L_\xi\phi\rangle
+d\left(\Theta_{G3}(\mathcal L_\xi\phi)-\iota_\xi\mathcal L_{G2}\right)=0,
\]

where the sum runs over the selected owner fields. The metric and density
responses are mandatory. The exact top-density control verifies
`L_xi(f vol)=d(i_xi f vol)` and rejects the frozen-density expression.

This is a weak source-sector identity. The diffeomorphism ghost, its
semidirect product with `Gau(P)`, defect support motion, and its BV brackets
are not yet constructed.

## 8. Minimal ordinary-gauge BV completion

Let `c` be the ordinary gauge ghost. In the declared left-action convention,
the fundamental vector fields form the corresponding anti-homomorphism and
the BRST rules can be written

\[
sA=-D_Ac,
\qquad
s\epsilon_{\rm red}=c\epsilon_{\rm red},
\qquad
sg_{\rm DW}=0,
\qquad
sc=\frac12[c,c].
\]

The minimal action needed to test the CME through antifield number one is

\[
\boxed{
S_{\min}
=I_{G2}
+\langle A^+,-D_Ac\rangle
+\langle\epsilon^+,c\epsilon\rangle
+\left\langle c^+,\frac12[c,c]\right\rangle.
}
\]

The ghost-antifield term has antifield number two, but is required to cancel
the antifield-number-one closure obstruction. A literal truncation retaining
only field antifields fails for the nonabelian algebra. The exact fixture
verifies the connection and distortion closure laws, a nonzero bracket, and
Jacobi. Together with the coupled Ward identity this establishes the
ordinary-gauge CME through antifield number one at the algebraic/bulk grade.

This does not establish BV properness on stabilizer strata, a nonminimal
sector, boundary BFV charge closure, super-IG, diffeomorphism BV, matter BV,
or physical cohomology.

## 9. G4 and G5 handoff

G4 receives

```text
(E_A,E_epsilon,E_g; Theta_G3,omega_G3;
 gauge/diffeomorphism weak identities;
 native (9,5) Krein/right-H structures)
```

and must construct the observation lift/retract, admissible ultrahyperbolic
polarization, closed boundary domain, preboundary-kernel quotient, and
off-slice leakage test.

G4 must construct and test

```text
R_s L_s = 1,
R_s D_Y L_s = D_X,
(1-L_s R_s) D_Y L_s = 0,
```

plus the dual map on Euler covectors. The exact finite control shows that the
middle identity can pass while the leakage condition fails.

G5 may begin only after G4 returns the observation and
pseudo-musical/Green-domain packet. It must then add the matter current and
recompute the coupled identity. A defect weld is optional comparator work,
not an author-supplied prerequisite. The source-only Ward pass cannot select
`J_D`, `J_D+J_F`, or an independently soldered current because none is
present here.

## 10. Datum and surplus boundary

G3 adds no phenomenological parameter. The Euler transposes,
`Theta_G3`, `omega_G3`, and the ghost bracket are forced by the action and
ordinary gauge algebra. P1/P2/P3 remain unused. Boundary/domain choices,
normalization, reduction component, stationary orbit, physical projections,
and P3 remain unpriced, so constraint surplus remains `UNCOMPUTABLE`.

No stationary vacuum, Standard Model spectrum, Higgs, anomaly cancellation,
index, observed count, cosmological amplitude, or PP3 result is claimed.
