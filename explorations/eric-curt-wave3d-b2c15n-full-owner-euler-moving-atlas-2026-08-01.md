---
title: "Eric/Curt Wave 3D-B2C15N: full first-action owner Euler and the background-dependent moving atlas"
status: active_research
doc_type: construction_result
created: 2026-08-01
branch: agent/null-clifford-omega1-repair
run: historical-investigation
registry: lab/process/eric-curt-wave3d-b2c15n-full-owner-euler-moving-atlas.json
probe: tests/channel-swings/eric_curt_wave3d_b2c15n_full_owner_euler_moving_atlas_probe.py
grade: "B2C15N PARTIAL CONSTRUCTION PASS WITH NATIVE BACKGROUND GATE. The first complete exact noncentral finite owner tuple is derived from the written action by independently constructing E_T and E_B and returning E_B-E_T through two moving graph owners. The chain rule, nonzero Green endpoint, and integrated Helmholtz identity pass; omitting E_B gives a nonzero Helmholtz defect. Direct-B/T cancellation lowers both diagonal graph orders but leaves mixed third-order formal-adjoint coefficients +9/-9. A degree-six moving-background interpolation passes two held-out points. The full total-symbol dispersion determinant is irreducible of bidegree (20,8), while the actual Douglis--Nirenberg principal determinant factors into four exact background loci. This proves the moving atlas is action-background dependent and kills promotion of the frozen-Shiab trace atlas before the actual native Y14 background and stabilizer are built. Native coefficientwise right-H/Krein/reality, BV, and domain remain open."
canon_verdict_change: none
---

# B2C15N full owner Euler and moving atlas

## Result first

The main missing variational step is now explicit and executable.

The earlier exact equation `E_T` varied the displacement

\[
T=A-B
\]

while holding the reference connection `B` fixed. That is not the full
equation when `B` itself is the gauge-rotated Levi--Civita graph
`B(epsilon,g)`. B2C15N constructs the independent direct-`B` covector,
subtracts the returned `T` response, and only then dualizes through the graph.
The controlling covector is

\[
R_B:=E_B-E_T.
\]

The returned owner equations are

\[
E_A=E_T,
\qquad
E_\epsilon=C_\epsilon+(D_\epsilon B)^!R_B,
\qquad
E_g=C_g+(D_gB)^!R_B.
\]

Here `C_epsilon` and `C_g` are the direct coefficient returns from the moving
Shiab, density, and lowerer. The exact finite construction includes both graph
owners and a graph whose formal adjoint itself moves.

All pieces are live. Direct differentiation of the pulled-back action equals
the assembled owner tuple plus its nonzero preboundary endpoint. The complete
linearization obeys Helmholtz reciprocity. The tempting tuple obtained by
returning `E_T` alone has exact Helmholtz defect

\[
\frac{279281447}{155195040}\ne0.
\]

This is a construction result, not merely a warning about notation.

## Plain English

We had derived the equation obtained by wiggling the difference between two
connections. But one of those connections is itself built from the metric and
reduction. Wiggling the metric therefore does two things at once: it changes
the difference, and it changes the reference connection. Until both effects
were included, we did not have the actual metric/reduction equation.

They do not simply add. Some leading terms cancel, while different mixed terms
survive. In the exact two-owner model, the third-derivative term disappears on
each owner's diagonal but survives between the two owners with coefficients
`+9` and `-9`. Those opposite signs are required by variational symmetry.

The second result is strategic. The earlier rank atlas described a frozen
piece of the contraction as a function of the wave covector. The full action
operator also depends on the background field and its derivatives. The exact
moving model produces both a total-symbol dispersion determinant and a
Douglis--Nirenberg principal determinant depending jointly on the background
and the wave covector. Two admissible backgrounds give different total-symbol
dispersion polynomials. So the old frozen atlas is useful input, but it is not
the moving action atlas.

## Layer 0: the objects that must not collapse

| object | role | status |
| --- | --- | --- |
| `I1` | written first action | retained |
| `E_T` | partial Euler covector at fixed `B` | constructed previously; retained |
| `E_B` | independent direct-`B` covector at fixed `T` | constructed here |
| `R_B=E_B-E_T` | driver returned through the connection graph | constructed here |
| `Euler_owner(I1)` | full `(A,epsilon,g)` covector | exact finite construction here |
| `Euler(I2_src)` | compact-source residual-square Euler system | distinct |
| `Euler(I2_var)` | exact-variation residual-square Euler system | distinct |

Likewise, the `91` vertical Spin directions used in B2C15M are passive
frame/descent directions. They are not `91` physical epsilon-owner fields.
The owner graph uses quotient reduction motion and the ten physical metric
owners.

The native gauge-rotated Levi--Civita branch also remains separate from the
`A0` comparator. The latter may add the already typed lower-order return
`pr_h[beta_m,chi_m]`; it is not inserted into the native principal symbol.

There is also a source homonym that remains unresolved. In the draft,
`omega=(epsilon,varpi)` and the contraction is written `odot_omega`. The
selected reconstruction in this packet uses
`S=S_(epsilon,g)` and assumes no independent translation/`varpi` derivative.
If `D_varpi odot_omega` is nonzero, additional translation-owner slots must be
added. The source does not type that dependence, so this packet is exact for
the declared selected branch, not claimed as the unique source-literal branch.

## Independent variation

Write

\[
C=F_B+\frac12D_BT+\frac13q(T,T),
\qquad
L=\mathscr S D_B,
\qquad
Q_T(\tau)=\mathscr S q(T,\tau).
\]

With formal adjoints defined by the actual Green identity, the independent
covectors have the form

\[
E_T=
\mathscr S F_B
+\frac12(L+L^!)T
+\frac13\mathscr S q(T,T)
+\frac23Q_T^!T
+\frac\kappa2(\flat+\flat^!)T,
\]

and

\[
E_B=L^!T+Q_T^!T.
\]

Therefore

\[
\boxed{
R_B=
-\mathscr S F_B
+\frac12(L^!-L)T
+\frac13\left(Q_T^!T-\mathscr S q(T,T)\right)
-\frac\kappa2(\flat+\flat^!)T .
}
\]

This formula makes the cancellations visible:

- half of the direct derivative term cancels the returned `T` term;
- the cubic terms leave a cyclicity defect unless the missing cyclic identity
  is actually present;
- the curvature and mass terms survive;
- moving contraction and pairing terms remain separate coefficient covectors.

`D(L^!)` and the six-slot `DM` are not added to this first variation. They
enter when this owner tuple is linearized to form the Hessian.

## Exact two-graph-owner fixture

The B2C13 noncentral rational model is extended to

\[
\begin{aligned}
B={}&(1,-1)z+(1,2)z'
 +(2,1)g+(-1,1)g'\\
&+(1,-2)g z',
\qquad T=a-B,
\end{aligned}
\]

with

\[
\rho=2+z+g,
\quad
S=S_0+zS_z+gS_g,
\quad
H=H_0+gH_g.
\]

The `g z'` term makes the graph map and its formal adjoint genuinely move.
Every quantity is differentiated symbolically over the rationals.

The direct first variation satisfies

\[
\delta I_1
=\int\sum_u\langle E_u,\delta u\rangle
+\left[\Theta_{I_1}\right]_0^1
\]

with exact values

```text
direct   = -530418061 / 166320
bulk     = -162961741 / 166320
boundary = -6628 / 3
```

and `direct = bulk + boundary`.

The owner trace orders are

```text
A0: 1, A1: 1, epsilon: 2, g: 2
```

so both graph owners carry the prolonged preboundary packet.

## Realized orders and the cancellation fork

The prior Douglis--Nirenberg table was deliberately an upper-bound skeleton:

\[
\begin{pmatrix}
1&2&2\\
2&3&3\\
2&3&3
\end{pmatrix}_{(A,\epsilon,g)}.
\]

The exact fixture realizes

\[
\boxed{
\begin{pmatrix}
1&2&2\\
2&2&3\\
2&3&2
\end{pmatrix}.
}
\]

Thus direct-`B`/returned-`T` cancellation lowers the two diagonal graph
blocks, but it does not remove the mixed odd-order blocks. Explicitly,

\[
\sigma_3(H_{\epsilon g})
=\frac12(g-3)(g+z-3)(g+z+2),
\]

and

\[
\sigma_3(H_{g\epsilon})=-\sigma_3(H_{\epsilon g}).
\]

At `z=g=0` these are `+9` and `-9`. Their antisymmetry is the odd-order
formal-adjoint relation demanded by Helmholtz symmetry.

A scalar one-owner model necessarily kills `p^T(S-S^T)p`. It therefore cannot
decide whether the full graph has a third-order block. This was caught by the
specialist pre-pass before the result was recorded.

## Weighted Helmholtz gate

Two independently chosen compactly supported polynomial owner variations give

\[
\int\langle v_2,Hv_1\rangle
=\int\langle v_1,Hv_2\rangle
=\frac{1103763581}{274575840}.
\]

The same test on the hostile `E_T`-only return gives the nonzero defect quoted
above. This is stronger than checking that the direct action differentiates:
it detects a missed owner-return term in the assembled equation.

This exact rational Helmholtz check is not a coefficientwise proof of the
native right-quaternionic, Krein, and charge-reality identities. Those require
the actual native owner coefficient and remain open.

## Moving background/conormal atlas

Let `c` scale the preregistered owner background jet and let `lambda` denote
the one-dimensional conormal. The complete `4 x 4` total-symbol ledger has
entrywise background degrees

\[
\begin{pmatrix}
4&4&5&5\\4&4&5&5\\5&5&6&6\\5&5&6&6
\end{pmatrix}
\]

and conormal degrees

\[
\begin{pmatrix}
0&1&2&2\\1&0&2&2\\2&2&2&3\\2&2&3&2
\end{pmatrix}.
\]

Thus it has:

- maximum entry degree `6` in `c`;
- maximum entry degree `3` in `lambda`;
- all coefficients reconstructed from `c=-3,-2,-1,0,1,2,3`;
- exact held-out agreement at `c=4,5`;
- a planted degree-`7` polynomial that vanishes at every interpolation node
  but is caught at both holdouts.

The unique square maximal minor of the **full total symbol** is irreducible
over `Q` and has bidegrees

\[
(\deg_c,\deg_\lambda)=(20,8).
\]

This is dispersion data, not the weighted principal characteristic
polynomial. With row weights `(0,0,1,1)` and column weights `(1,1,2,2)`, the
actual Douglis--Nirenberg principal determinant is

\[
\boxed{
16(c-3)^2(c+2)^2(3c-1)^2(c+1)^4\lambda^8.
}
\]

The admissible slices `c=0` and `c=1` have different exact total-symbol
dispersion polynomials. At `c=-1`, `rho=2+z+g` vanishes at the frozen point and the support
changes from `16` to `14` matrix entries. That point is an invalid density
chart and is retained as a hostile control, not promoted as physics.

The conclusion is not that the native action has this finite determinant. It
is that a moving action atlas is a relation in **background jet and conormal**.
The frozen `K_fix(xi)` rank theorem cannot determine it by itself.

## Why the negative/null/pure-trace atlas is paused

B2C15M's positive-plus-trace theorem remains valid at its stated frozen-Shiab
scope. B2C15N does not erase it. But before extending that atlas to negative,
nonzero-null, and pure-trace representatives, the complete native owner
background must be specified and its actual stabilizer computed.

If the full background preserves the trace stabilizer, the efficient charts
are still:

1. pure trace;
2. positive trace-orthogonal norm;
3. negative trace-orthogonal norm;
4. nonzero null trace-orthogonal component.

The tags `perpendicular=0` versus `perpendicular nonzero null`, `trace=0`
versus `trace nonzero`, and `q(xi)=0` must remain explicit. If the action
background preserves only a smaller base/fibre or Lorentz-diagonal group,
those four charts must be refined by incidence type. Extending the old atlas
first would assume the very stabilizer the full action may break.

## Source disposition

- `SOURCE-CONFIRMS`: draft p.44 eq.9.4 supplies the written first-action
  grammar.
- `SOURCE-CONFIRMS`: Portal/Oxford `01:43:32--01:45:53` requires an adjustment
  making the curvature-based tensor exact.
- `SOURCE-CONFIRMS`: Portal/Oxford `02:35:10` explicitly calls that completion
  a quadratic eddy tensor.
- `SOURCE-CORRECTS`: TOE `01:36:35--01:36:56` corrects Shiab from projection
  to contraction.
- `SOURCE-CORRECTS`: the compact 2021 residual is not automatically the exact
  Euler covector of the selected noncyclic action.
- `SOURCE-SILENT`: independent `E_B`, the complete owner return, moving graph
  adjoints, realized orders, native background/stabilizer, polynomial loci,
  any independent `D_varpi odot_omega` slot, BV quotient, and domain.
- `WATCH-ONLY`: TOE `02:44:06` describes the modern two-connection `D^2` as
  unreleased; it supplies none of these missing coefficients.

## External datum

P1/P2/P3 are unchanged and unused. Their types do not supply an independent
`E_B`, graph derivative, moving coefficient, action background, stabilizer,
polynomial component, BV differential, or domain.

This does not mean external data can never select a solution after the native
equations exist. It means they cannot replace the local variational map that
defines those equations.

## What remains open

- construct the actual native `Y^14` `E_B` and return it through the quotient
  and ten metric owners on a declared background;
- compute the stabilizer and complete typed support graph of that background;
- verify every native coefficient under right-`H`, Krein, and charge reality;
- only then extend the negative, nonzero-null, and pure-trace polynomial
  charts;
- retain the `A0` lower-filtered comparator separately;
- construct a source-derived tangent/BV differential and an
  observation-descended quotient;
- prolong the native preboundary form and find a common analytic domain.

## Next gate

`ECW3D-B2C15O-NATIVE-Y14-OWNER-BACKGROUND-STABILIZER-AND-TYPED-SUPPORT`:

1. resolve or explicitly branch the possible `D_varpi odot_omega` slot, then
   choose a declared native action background without fitting a desired
   principal result;
2. construct the native `E_B`, `R_B`, `D_epsilon B`, and `D_gB` coefficients;
3. derive the actual stabilizer and typed owner/residual support after all
   cancellations;
4. verify coefficientwise right-`H`, Krein, reality, and weighted Helmholtz;
5. then decide which trace/null charts are genuine orbit charts and compute
   their repeated templates/all-maximal-minor loci.

Curt remains `FORMALLY_SEPARATE_INSIDE_ERIC_LANE`. The conjunctive promotion
gate `TG-1 AND TG-2 AND TG-3` remains `NOT_PROMOTED`.

## Validation

The construction probe passes `22 exact + 6 source receipts + 16 type-level +
13 planted = 57` checks. The planted controls reject omission of `E_B`, an
`E_T`-only Helmholtz-defective tuple, cap-to-realized-order promotion, the
scalar-owner third-order shortcut, unsupported background-free support or
background-free dispersion claims, hidden interpolation degree,
selected-entry dispersion, datum-supplied coefficients, and BV promotion.
