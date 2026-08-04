# K77 Wave 2: mixed primalizers and two-connection comparison

Date: 2026-08-04
Gate: `K77_MIXED_HESSIAN_PRIMALIZERS_AND_TWO_CONNECTION_COMPARISON_FUNCTOR`
Verdict: **PARTIAL**

## Outcome

This swing closes the algebraic primalizer part of the preceding gate on the
existing admissible real-K77 associated-bundle sector. It constructs the
moving density/Krein pseudo-musicals for the four fermion fields, proves their
inverse-variation and transition-naturality identities, and shows that the
density formulation does not consume the orientation datum P1.

The required primary-source collision also corrected the comparison itself.
Weinstein introduces the unreleased two-connection `D^2` immediately after
the fermionic `0 -> 1 -> 13 -> 14` roll, not as the bosonic half of a
Bose--Fermi totalization. The swing therefore builds the smallest typed
one-way Hodge rolling of that mnemonic and compares it with the released D916
fermion roll. They are not slot-preservingly equal. The full cyclic reverse
arrow and action owner remain unreleased and unbuilt, so the gate stays
partial.

## Ten-lens preassessment

Before computation the swing used ten lightweight specialist lenses:

1. **Differential geometry:** derive the pseudo-musicals from metric, density
   and bundle pairings, not coordinate identities.
2. **Spin representation theory:** use the actual real `Cl(7,7)` carrier and
   cross-chiral split pairing.
3. **Variational/BV:** keep density-dual Euler rows distinct from fields until
   primalized.
4. **Krein operator theory:** prove moving inverse and formal typing before
   discussing a Green domain.
5. **Homological algebra:** reconstruct both arrows before claiming a cyclic
   square or cohomology.
6. **Gauge geometry:** require transition naturality, not merely a pointwise
   matrix inverse.
7. **Hyperbolic PDE:** do not promote algebraic pseudo-musicals to a closed
   physical domain.
8. **Standard Model phenomenology:** emit no seesaw, mass or generation claim
   from the block shape alone.
9. **Exact computation:** use nonorthogonal frame, moving-spin and Hodge-sign
   controls.
10. **Science council/proof systems:** look for a source classification error
    before defending the inherited comparison target.

The shared recommendation was to build the primalizer exactly, then retype
the source target before attempting any equality.

## Layer 0 correction

Three distinct structures must remain separate:

- D916, the released conditional four-field fermion operator;
- the unreleased cyclic two-connection fermion completion or rival;
- common-action mixed Bose--Fermi Hessians, which land in equation duals.

The immediate predecessors accidentally called the second object bosonic.
That classification is retracted here. Consequently the anticipated
tensor-to-spinor central-character test is not a kill: it is a test of the
wrong comparison object and is discarded.

## 1. Actual moving density/Krein primalizers

On the actual real `Cl(7,7)` carrier the split spin form `B` is symmetric,
involutive and cross-chiral. The K77 Hodge-square signs in degrees
`0,1,13,14` are `(-,+,+,-)`. Combining the metric musical, `B`, the absolute
metric density and the source row permutation produces an invertible
four-field pseudo-musical.

For a moving flat map `K(t)` its inverse `R(t)` obeys exactly

\[
\dot R=-R\dot K R.
\]

The probe verifies this in degrees zero and one and checks naturality under a
nonorthogonal determinant-one form-frame change and an actual nonconstant
Spin transition generated inside the real K77 Clifford representation. Once
degrees, metric, split pairing, density and the source row permutation are
fixed, the algebraic primalizer has no free coefficient.

This result is scoped to the admissible associated-bundle/density sector. It
does not construct an arbitrary `Y^14` atlas, an analytic closure, a Green
operator or a physical evolution domain.

### Orientation and P1

The absolute metric volume is a density, so the action-dual construction does
not choose an orientation. P1 is therefore not required here. If one insists
on ordinary top-form Hodge notation, the equivalent expression carries the
orientation line. That optional notation must not be confused with a new
receiving arrow for P1.

## 2. One-way Hodge rolling of the two-connection mnemonic

The smallest typed raw carriers are

\[
C_{\rm even}=\Omega^0(S)\oplus\Omega^{13}(S),\qquad
C_{\rm odd}=\Omega^1(S)\oplus\Omega^{14}(S).
\]

Rolling degrees 13 and 14 with the constructed primalizers gives the one-way
operator

\[
\mathcal D_{A,B}^{\rm one\ way}=
\begin{pmatrix}
d_A&-F_B\\
1&-\delta_B
\end{pmatrix}.
\]

An exact Hodge-sign fixture distinguishes the degree-14 inverse from the
degree-14 star itself. Copying the wrong sign flips the whole lower row, so
the result is not a convention-insensitive scalar toy.

This constructs only the even-to-odd arrow. A cyclic `D^2` requires the
odd-to-even arrow, its degree/connection assignments and the relations under
which the two composites close. The public source does not give those data.

## 3. Comparison with the released D916 roll

In column order `(nu,zeta)` and equation-row order `(zeta,nu)`, the released
conditional D916 roll has the schematic form

\[
\mathcal D_{916}=\begin{pmatrix}
d_A^0&\Phi d_A^1\\
0&-(d_A^0)^\times
\end{pmatrix}.
\]

The two candidates share the top-left connection slot, but the other three
comparisons matter:

| slot | D916 roll | one-way two-connection roll | disposition |
|---|---|---|---|
| northeast | first-order `Phi d_A^1` | zero-order `-F_B` | principal-order mismatch |
| southwest | zero | identity | later rival fills the old zero path |
| southeast | Krein/formal adjoint of `d_A^0` | second connection `-delta_B` | different owner |

Thus slot-preserving equality is killed. This does not kill either fermion
construction, and it does not decide whether the 2025 object replaces,
completes or merely rivals D916. A general non-slot-preserving chain
equivalence remains untested.

## Constraint surplus and status

The primalizer itself has zero free algebraic coefficients once its geometric
owners are fixed. It contributes no equation selecting the surviving
projective trace-`q` coefficient:

\[
\operatorname{rank}_{\rm selection}=0,\qquad
\operatorname{surplus}=0-1=-1.
\]

P1/P2/P3 remain unused. Wave 3 stays closed. No observation map, Yukawa,
particle, generation, mass, vacuum, domain or physical equation is claimed.

## What moved

- Four-field K77 density/Krein primalizer: **constructed algebraically with
  moving and transition checks**.
- P1 requirement for density-dual action: **not required**.
- Two-connection source classification: **corrected to an unreleased
  fermion-cyclic completion/rival**.
- One-way Hodge-rolled two-connection arrow: **constructed**.
- Slot-preserving equality with D916: **killed by typed order and slot
  mismatches**.
- Full cyclic arrow pair/action owner: **open**.
- Trace-`q` coefficient surplus: **unchanged at `-1`**.

## Next gate

`K77_TWO_CONNECTION_CYCLIC_FERMION_FULL_ARROW_PAIR_AND_ACTION_OWNER`

Construct or source-bound the reverse odd-to-even arrow, assign both
connections and Hodge degrees, compute both composites, and determine whether
one scalar action/Helmholtz structure owns the pair. Only then test a general
chain equivalence or precise rival relationship with D916 and return to the
mixed-Hessian Euler totalization.

## Executable receipt

`tests/channel-swings/k77_wave2_mixed_primalizer_comparison_probe.py` passes:

```text
9 source + 19 type + 22 exact + 8 planted = 58/58
```
