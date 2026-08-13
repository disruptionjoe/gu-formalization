---
title: "K77 Wave 2 partial: rendered draft-9.16 matrix and formal primalizer templates"
status: active_research
doc_type: exploration
created: 2026-08-04
gate: RENDEZVOUS-ACTION-CURRENT-RIESZ-SUPERIG-WARD
result: "PARTIAL__DRAFT916_SOURCE_MATRIX_AND_FORMAL_PRIMALIZER_TEMPLATES_BUILT__ACTUAL_D916_K77_ASSEMBLY_OPEN"
canon_verdict_change: none
---

# K77 Wave 2 partial: what the draft operator supplies and what remains to be built

## Result first

This swing closes the identity of the 2021 draft's displayed fermion matrix
and builds exact, discriminating templates for the mathematical structures
that a global K77 realization will require. It does **not** yet assemble the
actual sixteen-block K77 operator.

Built at the stated grade:

- a rendered, cell-by-cell transcription of draft equation 9.16;
- the exact K77 Hodge-square signs in degrees `0,1,13,14`;
- a finite exact model of the primalizer needed to turn a density-dual
  operator into an endomorphism before asking for a Krein adjoint;
- the general moving-density, moving-pairing formal-adjoint and Green-density
  identity for a primalized first-order operator;
- a nonconstant three-patch **model** of connection, adjoint, and Green-current
  descent;
- finite algebraic controls showing that K-skewness alone does not force the
  southeast block to vanish; and
- finite one-insertion current and conjugation-covariance controls, plus a
  typed candidate compact-support variational core.

Still open:

- instantiate all sixteen equation-9.16 blocks with the real K77 form
  degrees, Hodge/Shiab coefficients, density, pairings, and
  `rho(epsilon)` transitions;
- construct the actual density-dual primalizer and compute the resulting
  multi-index formal adjoint;
- compare its lower-left quadrant, after the displayed row permutation, with
  the draft's barred/starred entries;
- prove that the actual bosonic and fermionic variations share one core and
  reproduce the already-built `J_D+J_F` and even-IG Ward system on that same
  core; and
- only then admit the Wave-3 observation/provenance incidence census.

The repaired exact probe passes:

```text
7 source + 23 type + 19 exact + 5 planted = 54 PASS.
```

Wave 2 therefore remains `PARTIAL`. This is useful progress: the next gate is
now a concrete blockwise assembly rather than the vague request to "find the
Dirac operator."

## Layer 0: seven nearby objects

| phrase | actual object | present grade |
|---|---|---|
| draft fermion bilinear | the local four-field matrix printed in equation 9.16 | source display |
| density-dual operator | a construction `D916:E -> E!` after a density lift | open actual assembly |
| primalizer | `R:E! -> E`, induced by density, Hodge, and the split pairing | exact finite template; actual K77 map open |
| primalized operator | `D_pr = R D916:E -> E` | open actual assembly |
| formal Krein adjoint | integration-by-parts adjoint of `D_pr` | exact general formula; actual block result open |
| variational core | common boson/fermion test-field space for action/Euler/Ward calculus | candidate typed; common invariance open |
| physical domain | closed, constraint-compatible evolution realization | downstream Wave 5 |

An eighth, separate object is the observed equivariant chiral-family index.
It cannot be read from the three kinematic provenance pieces.

The bars in the draft denote independent classical/Berezin variables. They
do not by themselves identify a field with a Hilbert or Krein adjoint. The
draft's stars are adjoint-shaped source ingredients, not a proof that the
full moving K77 integration-by-parts identity closes.

## Source collision before construction

The identity-grade extraction is
`lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md`.
It records the official PDF hash and the visual page-46 transcription.

| source question | disposition |
|---|---|
| four independent barred/unbarred fields | `SOURCE-STATES` |
| signed four-by-four matrix | `SOURCE-DISPLAYS-CANDIDATE` |
| southeast zero | `SOURCE-DISPLAYS-2021 / REITERATES-PROSPECTIVELY-2025` |
| nonzero southeast map | `SOURCE-ADMITS-UNSPECIFIED-RIVAL` |
| Hodge/Shiab/formal-star ingredients | `SOURCE-DISPLAYS-INGREDIENTS` |
| global density/Krein/reality adjoint | `SOURCE-SILENT` |
| global overlap descent and common domain | `SOURCE-SILENT` |
| three family-shaped pieces | `SOURCE-ASSERTS-WITH-HEDGES` |
| three observed chiral families | `SOURCE-ASSERTS-WITH-HEDGES / DOES-NOT-DERIVE` |

The `rho(epsilon)` factors are a displayed covariance ansatz. They do not by
themselves prove descent under the actual active real-K77 transition group.

## The equation-9.16 display

Let

\[
\mathcal E=\Omega^1(S_+)\oplus\Omega^1(S_-)
\oplus\Omega^0(S_+)\oplus\Omega^0(S_-)
\]

with unbarred order `(zeta+,zeta-,nu+,nu-)`. The displayed row order is
`(bar-zeta-,bar-zeta+,bar-nu-,bar-nu+)`, reflecting an opposite-half pairing.
The rendered source gives

\[
\mathscr D_{916}=
\begin{pmatrix}
*\odot\varpi_{++} & *\odot(d_0+\varpi_{+-})
  & \varpi_{++} & d_0+\varpi_{+-}\\
*\odot(d_0+\varpi_{-+}) & *\odot\varpi_{--}
  & d_0+\varpi_{-+} & \varpi_{--}\\
-\bar\varpi_{++}^{*} & -d_0^{*}-\bar\varpi_{+-}^{*}
  & 0 & 0\\
-d_0^{*}-\bar\varpi_{-+}^{*} & -\bar\varpi_{--}^{*}
  & 0 & 0
\end{pmatrix}.
\]

The source bilinear is schematically

\[
(\bar\zeta_-,\bar\zeta_+,\bar\nu_-,\bar\nu_+)
\rho(\epsilon)\,\mathscr D_{916}\,\rho(\epsilon^{-1})
(\zeta_+,\zeta_-,\nu_+,\nu_-)^T.
\]

Equation 9.18 places an outer Hodge star around the entire three-class Euler
residual. The source display is therefore not simply a square endomorphism
under an unstated positive inner product. A clean construction types the
bilinear first as a density-dual arrow

\[
\mathscr D_{916}:\mathcal E\longrightarrow\mathcal E^!
=\mathcal E^*\otimes\operatorname{Dens}(Y).
\]

## The missing primalizer

Let `flat_(g,B,mu):E -> E!` be induced by the K77 metric, the real split
spinor pairing `B`, the Hodge map, and the density. Define

\[
R_{g,B,\mu}=\flat_{g,B,\mu}^{-1},\qquad
D_{\rm pr}=R_{g,B,\mu}\mathscr D_{916}.
\]

For signature `(7,7)` on a fourteen-manifold,

\[
*^2\big|_{\Omega^p}=(-1)^{p(14-p)+7}.
\]

Consequently:

- degrees `1` and `13` have `*^2=+1`;
- degrees `0` and `14` have `*^2=-1`;
- after a fixed coordinate/density convention, the inverse on
  `Omega13 -> Omega1` has the sign `* B^{-1}`; and
- the inverse on `Omega14 -> Omega0` has the sign `-* B^{-1}`.

The probe verifies both inverse patterns on finite exact coordinate models.
That prevents the zero-form sign from being silently copied from the
one-form sector. It does not instantiate the actual 128-spinor bundle map.

## Formal adjoint and Green-density template

For the **primalized** first-order operator

\[
D_{\rm pr}=A^a\nabla_a+C
\]

with domain pairing `K_E`, codomain pairing `K_F`, and density `mu`, the
formal adjoint template is

\[
D_{\rm pr}^{\times}u
=K_E^{-1}\mu^{-1}
\left[-\nabla_a\!\left(\mu(A^a)^\dagger K_Fu\right)
+\mu C^\dagger K_Fu\right].
\]

The local density identity is

\[
\mu\bigl(\langle u,D_{\rm pr}v\rangle_F
-\langle D_{\rm pr}^{\times}u,v\rangle_E\bigr)
=\partial_a\bigl(\mu u^\dagger K_FA^av\bigr).
\]

The exact fixture uses moving density, pairing, and principal coefficient. A
planted adjoint omitting those derivative corrections leaves a nonzero
interior defect. The probe also extracts the coefficient of independent
symbolic field derivatives from the computed adjoint and compares it with
`-K_E^-1 (A^a)^T K_F`; it no longer compares an expression with itself.

This is a general theorem/template. It becomes evidence about `D916` only
after the actual K77 blocks and primalizer are substituted.

## Model overlap descent, not actual D916 descent

The rational three-patch fixture verifies the familiar associated-bundle
grammar

\[
A_i=h_{ij}A_jh_{ij}^{-1}-(dh_{ij})h_{ij}^{-1}
\]

for nonconstant `O(1,1)` transitions. It checks covariant differentiation,
formal-adjoint naturality, cocycle composition, and Green-current invariance.
A planted pure-conjugation connection fails.

This is deliberately labeled a **model**. It does not construct:

- the atlas of `Y=Met(X)`;
- the actual `rho(epsilon)` transition law;
- the real K77 Hodge/Shiab coefficients; or
- descent of the sixteen-block draft operator.

## Southeast zero: source branch and precise non-result

The displayed candidate has a zero southeast quadrant, and the later TOE
conversation treats that shape prospectively as a seesaw. The draft also
explicitly admits versions with a nontrivial lower-right map.

The probe supplies a discriminating finite algebraic comparator: both a zero
and a particular nonzero southeast block can satisfy the same finite K-skew
relation, while an arbitrary nonzero block fails. Therefore:

```text
proved: algebraic K-skewness alone does not force southeast zero;
not proved: a nonzero block exists with the actual form degrees, gauge
            equivariance, real-K77 structures, and source action.
```

The conditional construction keeps `SE=0` as the strongest displayed source
candidate. It remains a posit, not a uniqueness theorem.

## Action, current, Ward, and core: inherited versus checked here

The predecessor action swing already built the action-first bosonic sector,
the `J_D+J_F` connection variation, pseudo-musical/Riesz ownership, and the
even local-IG Ward architecture. This probe does not recompute those results.

It checks only finite controls:

- cross-pairing a matrix with its Krein adjoint gives a compatible doubled
  Hessian at classical independent-field grade;
- one connection insertion differentiates to one finite current; and
- finite conjugation covariance requires field and operator response.

No graded/Berezin Hessian is claimed. The product

\[
\mathcal F^B_c\times\Gamma_c(\bar{\mathcal E})
\times\Gamma_c(\mathcal E)
\]

is a natural **candidate** variational core because compact support removes
the integrated Green term. It is not yet a proven common core for the actual
bosonic Euler system and the unassembled `D916` realization.

## Curt's family map: exact typing and the next test

The three kinematic pieces are

1. `Omega0(S)`;
2. a chosen splitting image `s_Gamma(im Gamma) subset Omega1(S)`; and
3. `ker Gamma subset Omega1(S)`.

Here `Gamma:Omega1(S)->Omega0(S)`, so `im Gamma` itself does not live in
`Omega1(S)`. A splitting is required to speak of a gamma-trace complement.

The repo contains an exact complexified observer-character result with an
`E+` and an `E-` carrier in each provenance piece, plus the larger residual
carrier. That result has not been ported to the actual real K77 operator and
domain. The source asserts the three-family interpretation with hedges but
does not derive the observed chiral index.

After Wave 2 closes, the cheapest Wave-3 preflight is the exact incidence
census

\[
\operatorname{rank}
\bigl(P_{j,\alpha}\,\sigma_\xi(D_{916})\,P_{i,\beta}\bigr)
\]

for null and non-null `xi`, with provenance and observer projectors. Until
the actual `D916` symbol is assembled, this is a proposed test, not evidence
that Wave 3 has begun.

## Divergent specialist pre-assessment and hostile post-review

Before construction, three nonredundant lenses separated:

1. formal variational core from closed physical evolution domain;
2. source display from global adjoint/domain construction; and
3. provenance pieces from observer characters and physical family index.

After the first implementation, three hostile reviewers independently found
the same error: the summary had promoted exact templates and finite fixtures
to an actual global K77 closure. Their corrections were accepted:

- build the primalizer before the Krein adjoint;
- include the `(7,7)` Hodge signs;
- use a density identity with a partial derivative;
- replace the tautological principal-symbol test;
- label overlap, current, Ward, and southeast checks at their finite/model
  grade;
- repair the gamma-trace typing; and
- revert the campaign from Wave 3 to Wave 2 partial.

The durable review receipt is
`lab/process/hostile-reviews/2026-08-04-k77-wave2-global-draft916-krein-preboundary-review.md`.

## Gate disposition

`RENDEZVOUS-ACTION-CURRENT-RIESZ-SUPERIG-WARD` remains:

```text
PARTIAL__DRAFT916_SOURCE_MATRIX_AND_FORMAL_PRIMALIZER_TEMPLATES_BUILT__ACTUAL_D916_K77_ASSEMBLY_OPEN
```

The next exact construction is:

```text
ACTUAL_DRAFT916_K77_BLOCKWISE_ADJOINT_DESCENT_AND_COMMON_CONNECTION_VARIATION
```

Acceptance requires all of the following on the same actual operator/core:

1. all sixteen K77 blocks and their form degrees;
2. the density-dual lift and primalizer;
3. the complete multi-index formal adjoint;
4. lower-left comparison after the source row permutation;
5. actual `rho(epsilon)` transition/descent;
6. common boson/fermion compact-support core;
7. the inherited `J_D+J_F` connection variation re-derived once; and
8. the even-IG Ward identity with the moving operator response.

The provenance incidence census is retained as `WAVE3_PREFLIGHT`, not as a
reason to advance the campaign now.

## Held-out wall

No actual global `D916` realization, unique Shiab, unique southeast block,
atlas for arbitrary `Y`, Lorentz-section existence theorem, common invariant
core, graded fermion Hessian, closed physical evolution domain,
maximal-dissipative generator, spectrum, vacuum, particle mass, Standard
Model equation, anomaly cancellation, physical chirality, generation count,
P1/P2/P3 use, canon change, lane change, or public-posture change is claimed.

## Successor advance and correction (actual-carrier attempt)

The successor
`explorations/k77-wave2-actual-draft916-k77-blockwise-adjoint-descent-2026-08-04.md`
builds a conditional real-K77 total-graded D916 rival, an exact nonconstant
moving-Clifford/connection descent witness, a nontrivial frozen K77 adjoint and
current direction, and an inverse-trace-weighted Spin-equivariant algebraic
super-IG bracket.

Hostile review also found the exact remaining Layer-0 obstruction: section
11.2 fixes `zeta+/-` and `nu+/-` as ambient half-spinor labels, while the
successful total-grading fit reverses the one-form labels.  With the source
ambient labels, the selected gamma `Phi d` and exterior `d` have opposite
ambient-J parities even though equation 9.16 requires them to share the same
row/input incidence parity.  The successor therefore advances but does not
close Wave 2.  The next build is now
`K77_D916_SOURCE_SIGN_DUALITY_SHIAB_PARITY_RECONCILIATION`, followed by actual
zero-order coefficients, full multi-index adjoint, complete shared-core
connection variation, and full-source-group descent.
