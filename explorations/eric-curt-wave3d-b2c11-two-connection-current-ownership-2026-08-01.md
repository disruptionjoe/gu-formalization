---
title: "Eric/Curt Wave 3D-B2C11 — Two-Connection Current Ownership and Source-Action Selection"
status: active-research
doc_type: exploration
updated_at: "2026-08-01"
---

# Eric/Curt Wave 3D-B2C11 — Two-Connection Current Ownership and Source-Action Selection

## Result

B2C11 resolves the owner-transfer fork opened by B2C10.

The active southeast current cannot be removed by assigning it to a different
connection.  A distortion-dependent term can move the channel between the two
connection equations, and can make one *partial* equation blind to it, but the
complete graph-owned Euler tuple retains it.

Write

\[
C=\frac{A+B}{2},\qquad T=A-B,
\]

so that

\[
A=C+\frac12T,\qquad B=C-\frac12T.
\]

For connection Euler covectors \((J_A,J_B)\), the exact owner transform is

\[
\boxed{
J_C=J_A+J_B,
\qquad
J_T=\frac12(J_A-J_B).
}
\]

If the active extra current is \(K=J_{\bar\nu\nu}\), a general scalar
\(T\)-linear transfer has the B2C10 form

\[
J_A^{\rm extra}=qK,
\qquad
J_B^{\rm extra}=(1-q)K.
\]

Therefore

\[
J_C^{\rm extra}=K,
\qquad
J_T^{\rm extra}=\left(q-\frac12\right)K.
\]

At \(q=1/2\), the distortion current vanishes while the shared current remains
exactly \(K\).  At \(q=1\), the reference-connection current vanishes but the
whole current has moved to the variational connection.  Neither is a
cancellation.

The graph return makes this stronger.  If the second connection is derived as
\(B=B(\epsilon,g)\), then the full owner is

\[
\left(qK,(D_{\epsilon,g}B)^!(1-q)K\right).
\]

Killing its first component forces \(q=0\).  Killing the graph component,
when \((D B)^!K\ne0\), forces \(q=1\).  The two demands are incompatible.  The
actual active \(\mathrm{Cl}(9,5)=M(64,\mathbb H)\) B2C10 witness confirms both
nonvanishings:

```text
||K|| = 54.826107
graph return = 56.43009
fixture-normalized selected-direction proxy q* = 0.51441402
minimum selected-direction two-component proxy residual = 1546.2782
```

The last two numbers combine a four-evaluation current norm with one supplied
graph-direction pairing.  They are a fixture- and normalization-dependent
diagnostic, not an invariant norm of the full graph-owner covector.  The
non-deletion theorem instead uses only the robust facts \(K\ne0\) and one
nonzero graph pairing, which establishes \((D B)^!K\ne0\).  Thus the extra
channel is **transferred but not canceled**.

This fixes its minimal repository source-action role.  Conditional on
selecting the nonzero southeast operator *and retaining the other p.46 terms
and chosen owner maps*, the candidate fermion Euler current is

\[
\boxed{
\Upsilon_F^{\rm candidate}
=\Upsilon_F^{(9.18)}+J_{\bar\nu\nu}.
}
\]

The action variation forces the selected southeast block's current
contribution somewhere in the total connection Euler covector.  The source is
silent on whether the completion is exactly this additive formula or contains
additional cyclic or compensating terms.  The contribution is not a separately
appended matter bridge and not a fourth external datum: it is the derivative of
the same southeast coefficient already present in the selected fermion
operator.  This introduces zero new current coefficients.  Calling it
"conditional surplus one" remains provisional bookkeeping until an
independent operator-to-current comparison or held-out carrier test establishes
the independence of the consistency condition.  A planted unrelated current
is not fit.

The two draft coupling architectures were then realized in a finite
fixed-current/fixed-pairing owner sector.  Let \(I_1^B\) have Euler residual
\(\Upsilon_B\), let \(Q\) be the chosen fixed indefinite rational comparator,
and let \(I_F^{\rm candidate}\) have the candidate current above.  The two
finite actions are

\[
I_{\rm first}=I_1^B+I_F^{\rm candidate},
\]

with equation

\[
\boxed{\Upsilon_B+\Upsilon_F^{\rm candidate}=0,}
\]

and

\[
I_{\rm sourced}
=\frac12\langle\Upsilon_B,Q\Upsilon_B\rangle
-I_F^{\rm candidate},
\]

with equation

\[
\boxed{
(D\Upsilon_B)^TQ\Upsilon_B
=\Upsilon_F^{\rm candidate}.
}
\]

Exact directional differentiation verifies both formulas in that owner
sector, using an algebraic transpose.  The extra active current enters the
first equation additively and the second equation on the right-hand side.  It
cancels in neither.  This does not yet vary the fermion fields, the graph,
\((\epsilon,g)\), the density, or the pairing.  For moving \(Q_B\), variation
also returns a quadratic \((D Q_B)^!\) term; for differential
\(D\Upsilon_B\), integration by parts supplies Green terms and the formal
adjoint depends on the pairing and domain.

The current test does **not** select one of these two architectures.  It
selects the southeast current contribution used in both finite candidates.
Imposing both equations on the same fields adds an independent compatibility
condition: after the first gives \(\Upsilon_B=-\Upsilon_F\), the second adds a
nontrivial eigencondition.  The two equations are inconsistent on the exact
finite fixture, which leaves residual

```text
(-43/8, -25/8)
```

rather than an identity.  The equations must not be summed or silently imposed
simultaneously.

The most source-faithful constructive route now is a staged pair:

1. retain \(I_{\rm ED}=I_1^B+I_F^{\rm candidate}\) as the first
   Einstein--Dirac layer;
2. retain the manuscript-exact bosonic square
   \(I_2^B=\frac12\langle\Upsilon_B,Q_B\Upsilon_B\rangle\) as the separate
   second Yang--Mills--Higgs candidate;
3. keep the draft's second-order-sourced equation as a rival until the active
   \(Q_B\), adjoint, domain, and full \((\epsilon,\varpi)\) variation policy
   decide it.

This is a construction recommendation, not a claim that Weinstein released
the final staged coupling.  It uses his modern two-layer guidance while
respecting the exact 2021 formulas and their unresolved variation domain.

Finally, an abstract finite product-sector Green control was performed.  It
proves only the direct-sum lemma that adding a boson-only square cannot change
a stipulated nonzero fermion restriction on the full unrestricted fermion
trace space; zero-order coefficients do not alter principal Green order.  It
does not import the active B2C5/B2C6B/B2C10 Green matrix and is not a domain
replay.  A Green-Lagrangian fermion subdomain, the active symmetrized Green
form, and source-selected mixed boson--fermion boundary conditions all remain
open.

The probe passes

```text
27 computational exact + 6 source receipts + 34 type-level + 4 planted = 71 PASS
```

P1, P2, and P3 are untouched.

## Layer 0 — what is and is not the same object

| term | object here | not identified with |
|---|---|---|
| partial `varpi` variation | one displayed translation-connection directional derivative | a global declaration of every varied/held-fixed `omega=(epsilon,varpi)` component |
| `A` owner | variational-connection component in a chosen two-connection chart | automatically Weinstein's unreleased modern `A` token |
| `B` owner | reference or graph-derived connection component | automatically the 2021 draft's common `A_omega` |
| shared current | pullback along `delta A=delta B` | distortion current along `delta T` |
| graph current | `(D B)^!J_B` returned to `epsilon,g` owners | a disposable gauge artifact |
| `Upsilon_F` | fermion connection Euler covector | observed Maxwell/Yang--Mills current or Green current |
| `D_omega^* Upsilon_B` | residual derivative, pairing, adjoint, and domain applied to the bosonic Euler residual | a renaming of `Upsilon_B` or `Upsilon_F` |
| `I_2^B` | manuscript bosonic residual square | a total Einstein--Dirac residual square |
| `J_bar-nu-nu` | current derived from the selected southeast operator coefficient | a mass, count, or external datum |

The two most important homonym controls are these:

- vanishing \(J_T\) does not mean vanishing \(J_C\);
- a partial `varpi` derivative does not select the full two-connection
  field-space graph.

## Primary-source collision

### `SOURCE-CONFIRMS`

- Draft equations `(9.18)--(9.20)` give the first-order-total and
  second-order-sourced equations as alternatives.
- Draft equations `(9.11)--(9.15)` give the second action as the **bosonic**
  residual square \(I_2^B=\|\Upsilon_B\|^2\).
- The Section 9.1 action window contains a partial directional variation in
  `varpi`.
- TOE `02:44:06--02:45:13` says the modern two-connection on-shell object has
  not been released.
- TOE `00:41:50--00:43:38` distinguishes an Einstein--Dirac first layer from
  a second Yang--Mills--Higgs Lagrangian/action; ITI/UCSD
  `00:05:43--00:06:32` independently describes a first-order theory and its
  second-order square.

### `SOURCE-CORRECTS`

- The source does not authorize calling the partial `varpi` derivative the
  complete `omega` variation policy.  The existing source-locator audit grades
  that policy `UNDECLARED`.
- The source-exact square is bosonic.  Squaring a total Einstein--Dirac
  residual is a repository completion, not the manuscript formula.
- The second architecture compares the fermion current with an adjointed
  derivative of the bosonic residual.  A raw current-alphabet comparison is a
  Layer-0 error.

### `SOURCE-SILENT`

The checked sources do not provide:

- the owner map for the active nonzero-southeast repair;
- the full varied/held-fixed \((\epsilon,\varpi)\) policy;
- the active right-\(\mathbb H\)/Krein residual pairing \(Q_B\);
- the complete nonlinear \(Y^{14}\) graph transpose;
- a rule coupling or sequencing the two actions at one stationary solution;
- a common Green domain or mixed boson--fermion boundary condition.

Accordingly, the owner theorem and action realizations are repository
constructions.  They constrain any completion but are not presented as the
unreleased Weinstein formula.

## L1 — owner theorem

The owner transform is a cotangent-chain-rule identity, not a convention:

\[
\langle J_A,\delta A\rangle+\langle J_B,\delta B\rangle
=\langle J_C,\delta C\rangle+\langle J_T,\delta T\rangle.
\]

This makes the transfer result coefficient-independent.  Every \(T\)-only
term contributes opposite \(A/B\) currents, hence zero shared current.  It can
change \(J_T\), not \(J_C\).

## L2/L3 — graph return and action closure

Once \(B\) is graph-derived, dropping its return breaks the full variational
problem.  B2C10 already constructed the local reduction tangent and transpose;
B2C11 applies that actual active map to the southeast current and obtains a
nonzero return.  The finite owner model then proves why coefficient fitting
cannot solve the full tuple.

Both finite owner-sector action comparators close under exact differentiation
with a chosen fixed indefinite rational \(Q\) and algebraic transpose.
Replacing that chosen \(Q\) changes the finite gradient; this is not evidence
that positive pairings are inadmissible.  The active action-owned \(Q_B\), its
right-\(\mathbb H\)/Krein origin, moving response, formal adjoint, and domain
remain open.

## L4 — selected construction

The selected construction statement is conditional and precise:

> If the source-admitted nonzero-southeast semisimple operator is retained,
> its active `bar-nu-nu` contribution must occur somewhere in the total
> connection Euler covector with the same coefficient.  The displayed
> additive completion is the minimal repository candidate conditional on
> preserving the other p.46 terms and chosen owner maps; owner transfer cannot
> remove the contribution from the full action.

This selects a current correction, not yet the final coupling architecture.
The recommended next construction is the staged first-order Einstein--Dirac
action plus separate bosonic residual square because it consumes the most
source guidance without imposing the two rival equations simultaneously.

## L5/L6/L7 and boundary

- **L5 quantum:** the current remains on the active right-\(\mathbb H\), Krein,
  and `C+` carrier inherited from B2C10.  No Hilbert space, propagator, or
  quantum measure follows.
- **L6 physics:** no observed Maxwell/Yang--Mills current, Higgs mass, Yukawa
  coefficient, generation count, or cosmological amplitude is claimed.  The
  other GU/SM/GR/QM/cosmology legs are not altered.
- **L7 sourcing:** every source-positive and source-negative boundary has an
  exact local pointer.  Missing owner data is construction debt, not P1/P2/P3.

The trace-reversed Frobenius fibre remains

\[
(3,1)+(6,4)=(9,5),
\]

with \(\mathrm{Cl}(9,5)=M(64,\mathbb H)\).  Curt's literal `(7,7)` carrier
remains `FORMALLY_SEPARATE_INSIDE_ERIC_LANE`.  `TG-1 AND TG-2 AND TG-3`
remains false, so no third lane is promoted.

## Next gate

Run

```text
ECW3D-B2C12-ACTIVE-SOUTHEAST-CURRENT-CONTRIBUTION-AND-STAGED-RESIDUAL-SQUARE-ACTION
```

Construct the active staged packet

\[
(I_1^B,
 I_F^{\rm candidate},
 \Upsilon_{\rm ED};
 Q_B,I_2^B;
 D_{\epsilon,g}B,(D_{\epsilon,g}B)^!),
\]

with the same southeast coefficient appearing in the operator and current,
the full trace-reversed moving pairing, and the complete graph return.  Then
test whether one action-owned \(Q_B\) and one stationary background satisfy
the first-layer and second-layer Ward identities without imposing the rival
Euler equations simultaneously.

Only after that active staged action exists should the full mixed-domain
B2C6B replay attempt source-selected boson--fermion boundary conditions.
