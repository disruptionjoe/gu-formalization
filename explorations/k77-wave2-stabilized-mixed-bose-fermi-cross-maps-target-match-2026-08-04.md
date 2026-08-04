# K77 Wave 2: stabilized mixed Bose--Fermi cross maps and target match

Date: 2026-08-04
Gate: `K77_STABILIZED_MIXED_BOSE_FERMI_CROSS_MAPS_AND_TARGET_MATCH`
Verdict: **PARTIAL**

## Outcome

This swing constructed the two raw mixed Bose--Fermi maps directly from one
common action and verified their mixed-Hessian reciprocity both in an exact
finite action and on the actual real K77 one-form operator family. It also
found the decisive Layer-0 boundary: these maps land in Euler-density duals,
so the old `VU/UV` square is not even typed until moving Hodge/Krein/density
primalizers are built.

The direct target match to the later two-connection square is therefore not a
failed numerical fit. It is **ill-typed without a comparison functor** between
two different complexes. The current action-derived mixed family is nonzero
and has coefficient sensitivity rank two, but common-action reciprocity has
coefficient-selection rank zero. The projective surplus remains `-1`.

## Ten-lens preassessment

The lightweight preassessment was carried out before computation:

1. **Differential geometry:** locate every map in field or density-dual bundles
   before composing it.
2. **Representation theory:** require a carrier adapter between the
   two-connection and Bose--Fermi gradings.
3. **Variational bicomplex/BV:** derive cross blocks as mixed Hessians of one
   action.
4. **Hyperbolic PDE:** keep primalizers, Green data and evolution domains
   separate.
5. **Symplectic geometry:** interpret Hessian reciprocity as the local
   variational precursor, not a physical symplectic quotient.
6. **Krein/operator theory:** use density-dual adjoints; do not insert a
   positive Hilbert Riesz map.
7. **Standard Model phenomenology:** do not relabel a mixed cell Yukawa or mass
   before observation and symmetry breaking.
8. **Topology/anomaly:** P1/P2/P3 cannot manufacture analytic primalizers.
9. **Computational algebra:** use exact rational/Clifford witnesses and rank
   controls.
10. **Proof/distributed systems:** propagate the topology correction and its
    reconstruction debt together.

The shared recommendation was action first, followed by explicit dual-to-field
geometry, and only then a target comparison.

## Layer 0: three different block structures

The swing separates:

1. the draft deformation complex `C0 -> C1 -> C2`;
2. the formal endomorphism totalization
   `Delta=[[D,V],[U,F]]` on `B plus F`;
3. the later bosonic two-connection operator `D_AB`.

Equation `10.10` realizes the first, not automatically the second. The
two-connection operator realizes a different internal grading, not
automatically the Bose--Fermi one.

For a common action, the actual raw mixed blocks are

\[
U_{\rm raw}:B\to F^!,\qquad V_{\rm raw}:F\to B^!.
\]

Consequently `V_raw U_raw` and `U_raw V_raw` are ill-typed. The composable
maps would instead be

\[
U=R_FU_{\rm raw}:B\to F,
\qquad
V=R_BV_{\rm raw}:F\to B,
\]

where `R_F` and `R_B` must be constructed from the moving pairings and density.

## 1. Exact common-action construction

The probe uses the finite common action

\[
S(b,z,\bar z)=\tfrac12 b^TKb
+\bar z^T\left(F_0+\sum_i b_iC_i\right)z.
\]

Its complete exact Hessian is symmetric. The two off-diagonal blocks are
nonzero exact transposes, giving both raw cross directions without adding an
independent bridge equation. This is the finite Helmholtz control for the
field-theoretic statement that mixed variations of one scalar action agree.

## 2. Actual real-K77 witness

On the real `Cl(7,7)` carrier, the swing varied the existing left/right
trace-`q` one-form operators in both the tautological-`q` and one actual even
connection direction. With deterministic barred/unbarred fields and their
variations, it checked coefficientwise

\[
\langle\delta\bar\zeta,C_i\zeta\rangle
+\langle\bar\zeta,C_i\delta\zeta\rangle
=
\langle U_i(\zeta,\bar\zeta),(\delta\zeta,\delta\bar\zeta)\rangle
\]

for the left, right and mixed coefficient placements. All identities pass
exactly. The flattened coefficient response has rank two, proving that the
two placements are genuinely distinguished by the mixed Hessian.

This is a **frozen one-form-sector witness**. It is not the complete moving
sixteen-cell Hessian, global associated-bundle descent or a physical source.

## 3. Why target matching stops here

Two exact choices of primalizers applied to the same raw Hessian blocks produce
different bosonic and fermionic up-and-back composites. Therefore neither an
identity primalizer nor a preferred target square can be inferred from raw
mixed-Hessian reciprocity alone.

Likewise, entrywise comparison with

\[
\mathbb D_{A,B}^2=
\begin{pmatrix}F_A-F_B&0\\d_A-d_B&0\end{pmatrix}
\]

would compare the two-connection grading with the Bose--Fermi/Euler grading.
No such identification has been constructed. The missing object is a typed
comparison functor or chain adapter that sends the two-connection complex into
the common Euler complex and respects the selected primalizers.

## Constraint surplus

The action owns both raw blocks, but mixed-Hessian reciprocity holds for every
trace-`q` coefficient. Hence

\[
\text{selection rank}=0,\qquad
\text{surplus}=0-1=-1.
\]

Sensitivity rank two is not selection rank. P1/P2/P3 remain unused; an
external datum cannot manufacture the primalizers or comparison functor.

## What moved

- Equation `10.10` topology: **retyped as a rectangular mixed
  deformation-to-Euler complex**.
- Common-action raw mixed Hessian blocks: **constructed**.
- Actual K77 frozen one-form reciprocity: **verified exactly**.
- Global primalized maps `U,V`: **open**.
- Direct two-connection target match: **ill-typed pending a comparison
  functor**.
- Coefficient surplus: **unchanged at `-1`**.
- P1/P2/P3: **unused**.
- Wave 3: **closed**.
- Observed Yukawa, mass, particles, domain and vacuum: **not claimed**.

## Next gate

`K77_MIXED_HESSIAN_PRIMALIZERS_AND_TWO_CONNECTION_COMPARISON_FUNCTOR`

Construct the moving Hodge/Krein/density pseudo-musicals for the complete
sixteen-cell common Euler system, verify their formal-adjoint and Green
identities, and build the smallest typed chain adapter from the source-bounded
two-connection complex. Only then rerun diagonal and crossed target matching.

## Executable receipt

`tests/channel-swings/k77_wave2_stabilized_mixed_cross_map_probe.py` passes:

```text
11 source + 15 type + 13 exact + 7 planted = 46/46
```
