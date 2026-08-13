---
artifact_type: construction_result
created: 2026-08-11
ledger_version: "0.163"
result: UNRESTRICTED_K77_SOUTHEAST_FAMILY_CONSTRUCTED__NONNULL_DETERMINANT_INDEPENDENT_OF_SOUTHEAST__FERMION_ONLY_PRINCIPAL_CONSTRAINT_BV_ROUTE_KILLED__FULL_FIELD_GAUGE_BV_NEXT
grade: "EXACT structural theorem for the selected real-K77 four-field principal operator and every lower-right 128x128 southeast matrix; source-family, full-field BV, nonlinear/domain and physics claims excluded"
canon_verdict_change: none
---

# Unrestricted K77 southeast family and the principal BV-kernel gate

## Plain-English result

The source-admitted lower-right fermion block is now explicit, and it cannot do
the job the bounded-carrier route needed it to do.

For the complete selected real-K77 four-field principal operator, adding any
lower-right `128 x 128` matrix leaves every non-null determinant unchanged.
This is stronger than checking the two-parameter Clifford family or the K95
`11/12` comparator: it holds for every southeast matrix at a fixed non-null
covector.

Consequently no fixed southeast choice can create a nonzero fermion-only gauge
or constraint generator. The null symbol still has an `896`-dimensional right
kernel, but that is a characteristic propagation space: it disappears on the
open set of non-null covectors and therefore is not an off-shell gauge identity
or BV quotient.

The correct successor is the coupled ordinary-gauge complex containing the
connection `varpi`, four independent barred/unbarred fermions, gauge ghost and
action-derived Noether identity. A smaller fermion carrier may reappear only if
that full pre-variation complex derives it. An external datum cannot supply the
missing local Noether identity.

## Layer 0

The following objects were kept separate before computing:

1. source permission for `SE != 0` versus selection of its coefficient;
2. the complete Euler symbol versus a right characteristic kernel;
3. null characteristic modes versus an off-shell gauge generator;
4. a fermion-only principal complex versus the full connection-plus-matter BV
   complex;
5. an action-dual Noether identity versus a physical quotient; and
6. external datum versus local variational closure.

## Construction

Write the complete rolled symbol as

\[
D_0(\xi)=\begin{pmatrix}A(\xi)&B(\xi)\\C(\xi)&0\end{pmatrix}
\]

on `(Omega1(S) direct-sum Omega0(S))`, with total dimension `1920`. The
smallest source-admitted real-K77 Clifford family is

\[
E_{\ell}(\xi)=\gamma(\xi)
   (\ell_+P_+ + \ell_-P_-),
\qquad
D_{\ell}(\xi)=
\begin{pmatrix}A&B\\C&E_{\ell}\end{pmatrix}.
\]

Here `P_+` and `P_-` are complementary real K77 rank-64 projectors. The
coefficients are parameters of the construction, not source-derived values or
external data.

## Exact determinant theorem

For every non-null `xi`, the rolled blocks obey

\[
A(\xi)B(\xi)=0,
\qquad
C(\xi)B(\xi)=-q(\xi)1,
\qquad q(\xi)\ne0.
\]

Let `U` inject the lower `128` equations and `V` project the lower `128`
fields. The explicit solution of `D_0 X=U` is

\[
X=\binom{-B/q}{0},
\qquad VX=0.
\]

Thus the lower-right block of `D_0^{-1}` is exactly zero. For every southeast
matrix `E`, the matrix determinant lemma gives

\[
\det(D_0+UEV)
=\det D_0\,\det(1+EV D_0^{-1}U)
=\det D_0.
\]

The exact finite-field certificate verifies the identities on timelike and
spacelike orbit representatives, each of rank `1920`. The identities are
formal Clifford relations; Spin covariance carries the result over the two
non-null orbit classes in characteristic zero.

This theorem explains rather than contradicts the K95 B2C4 result. A southeast
term can change Jordan structure and hyperbolicity while leaving the non-null
determinant nonzero. Hyperbolicity repair is not gauge reduction.

## Exact fingerprints

| branch | timelike rank | spacelike rank | sampled null rank |
|---|---:|---:|---:|
| `SE=0` | 1920 | 1920 | 1024 |
| K95 `11/12` coflip comparator ported to K77 | 1920 | 1920 | 1024 |

The sampled null right nullity is `896`. It is not common with the non-null
symbols because those are invertible.

## BV/Noether consequence

Suppose a polynomial principal generator `R(xi)` obeyed
`D_ell(xi) R(xi)=0` for every covector at fixed coefficients. On the open
non-null set `D_ell` is invertible, so `R` vanishes there and hence vanishes
identically. The nondegenerate action pairing gives the same conclusion for a
fermion-only left Noether identity.

Therefore the nontrivial fermion-only principal constraint/BV route is killed
for the entire southeast family. This is not a claim that the complete theory
has no gauge symmetry. Ordinary gauge transformations act on `varpi` as well
as matter, and their coupled Noether/BV complex remains to be built from the
source action.

## Hostile-review boundary

- The theorem covers the selected complete K77 upper/lower blocks and any
  southeast matrix. It does not exhaust the source's Shiab family.
- It kills a fermion-only principal gauge generator, not characteristic null
  propagation and not a full-field gauge-BV complex.
- It supplies no closed domain, Green operator, positivity, spectrum, index,
  particle interpretation or count.
- The K95 reciprocal coefficient remains K95-scoped prior art and is only a
  planted comparator here.
- No post-variation projector, P1/P2/P3 datum or new residue coordinate is
  introduced.

## Frontier

```text
headline_delta: none
frontier_conditions_closed: 2
  - smallest source-admitted K77 southeast family is explicitly constructed
  - nontrivial fermion-only principal constraint/BV route is killed wholesale
frontier_conditions_opened: 1
  - coupled varpi plus four-fermion ordinary-gauge Noether/BV complex
remaining_named_conditions: 2
  - full-field off-shell gauge/BV closure from the source action
  - common Green/domain, observation, chirality, index/count and physics rendezvous
```

## Source return and next gate

`SOURCE_CONFIRMS_SOUTHEAST_ZERO_AND_ADMITS_NONZERO_RIVAL__SOURCE_CORRECTS_NONE__SOURCE_SILENT_ON_K77_COEFFICIENT_SELECTION_FERMION_ONLY_BV_AND_FULL_FIELD_BV_DOMAIN`.

Next:

`BUILD_THE_COUPLED_VARPI_PLUS_FOUR_FERMION_ORDINARY_GAUGE_NOETHER_BV_COMPLEX_FROM_THE_SOURCE_ACTION__KEEP_NULL_PROPAGATION_SEPARATE_FROM_GAUGE_AND_DO_NOT_PROJECT_TO_RANK384`.

Probe:
`tests/channel-swings/selected_k77_unrestricted_southeast_bv_kernel_probe.py`.

Machine result:
`lab/process/selected-k77-unrestricted-southeast-bv-kernel.json`.
