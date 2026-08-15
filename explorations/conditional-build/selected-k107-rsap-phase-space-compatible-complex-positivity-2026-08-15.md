---
title: "Selected-K107 RSAP zero-section compatible-complex and Krein positivity classification"
status: active_research
doc_type: exact_invariant_linear_phase_space_complex_polarization_krein_classification
created: "2026-08-15"
registry: lab/process/selected-k107-rsap-phase-space-compatible-complex-positivity.json
probe: tests/channel-swings/selected_k107_rsap_phase_space_compatible_complex_positivity_probe.py
grade: "INVARIANT COMPATIBLE COMPLEX STRUCTURES AND THE CANONICAL VERTICAL REAL POLARIZATION EXIST, BUT EVERY INVARIANT ASSOCIATED METRIC ON THE ZERO-SECTION 98D PHASE TANGENT HAS SIGNATURE 48|50 OR 50|48; NO INVARIANT LINEAR KREIN OR CONSTRAINT REPAIR IS POSITIVE"
target_claim: K106_NEXT_GATE__AN_INVARIANT_PHASE_SPACE_COMPLEX_POLARIZATION_OR_KREIN_STRUCTURE_PRODUCES_A_POSITIVE_PAIRING_ON_THE_CONDITIONAL_98D_RSAP
target_verdict: NO_AT_ZERO_SECTION_INVARIANT_LINEAR_GRADE__COMPATIBLE_COMPLEX_AND_VERTICAL_POLARIZATION_EXIST_BUT_DO_NOT_REPAIR_SIGNATURE
canon_verdict_change: none
---

# Selected-K107 RSAP zero-section compatible-complex and Krein positivity classification

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> conditional phase-space, BFV and positivity question. Ordinary Higgs/VEV,
> family-index, net-chirality, anomaly, symmetry-breaking and familiar four-
> dimensional gauge-model conclusions do not adjudicate it. Read
> `lab/methods/source-native-comparator-routing.md` before importing any such
> comparator.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: the zero-section tangent of the conditional balanced cotangent space
`T*(G/H_bal)`, after explicitly supplying `R_0`, the balanced zero-level law,
and the right-`H_bal` gauge declaration. The result classifies invariant
linear compatible-complex, real-polarization, Krein-fundamental-symmetry and
linear-subquotient escapes. It is not a theorem about nonlinear BFV
cohomology, non-invariant background-selected sectors, contours, Wick
rotations, boundary domains or nonlocal quantization.

## Result in plain English

Passing from the indefinite `49D` base to its `98D` cotangent phase space does
create the missing algebraic structures—but not positivity.

- Invariant symplectic-compatible complex structures exist. They make the
  phase tangent pseudo-Kähler with signature `48|50` or `50|48`, never
  positive.
- The cotangent bundle has its canonical invariant vertical real
  polarization. That is a genuine positive control: polarization existence
  is not the obstruction. But a real polarization alone supplies neither a
  positive kinetic operator nor the missing physical domain.
- An invariant Krein fundamental symmetry cannot remove the signs because
  every invariant operator acts only on the two-dimensional
  position/momentum multiplicity and leaves the irreducible `24|25` factor
  untouched.
- Every nonzero proper invariant linear subquotient is another copy of that
  `49D` factor and remains indefinite.

Thus the bare conditional phase space has complex and polarization geometry,
but no invariant positive physical pairing. Repeating abstract invariant
linear searches will not produce one. The next admissible input must be a
concrete action-owned non-invariant selector or an explicit boundary,
contour, Wick or constrained domain whose full moving-`R` Noether and BFV
compatibility can actually be tested.

## 1. Carrier and owner fence

K106 identifies the balanced isotropy module

```text
U = R^(3,4) tensor R^(4,3),
dim U=49,                     signature(q)=(24,25),
End_H(U)=R.
```

At a zero-section point of `T*(G/H_bal)`, use `q` to identify `U*=U`. The
phase tangent is

```text
M = U plus U* = R^2 tensor U,
dim M=98,
Omega = K tensor q,           K=[[0,1],[-1,0]].
```

Complete reducibility and the scalar commutant on `U` give

```text
End_H(M)=M_2(R) tensor 1_U.
```

This is still the reverse scaffold. `R_0`, `lambda_h=0`, and the declaration
that right `H_bal` is gauge remain conditional inputs, not source-selected
facts.

## 2. Exact classification of compatible complex structures

Every invariant endomorphism has the form `J=A tensor 1_U`. Write

```text
A = [[a,b],[c,-a]].
```

The conditions `J^2=-1` and symplectic compatibility reduce exactly to

```text
a^2 + b c = -1.
```

So invariant compatible complex structures exist; for example

```text
A_0=[[0,-1],[1,0]].
```

The associated symmetric form is

```text
g_J(z,w)=Omega(z,Jw)=(K A) tensor q.
```

For every solution, `K A` is symmetric with determinant one. It is therefore
positive or negative definite. Tensoring with `q_(24,25)` gives

```text
signature(g_J)=(48,50)  or  (50,48).
```

The complex structure is real and exact, but pseudo-Kähler rather than
positive. This closes the loophole that the symplectic doubling itself might
canonically turn K106's indefinite base into a positive phase-space metric.

## 3. Polarization is present but insufficient

The vertical tangent of any cotangent bundle is a canonical real Lagrangian
polarization and is preserved by cotangent-lifted `G` actions. K107 therefore
does **not** claim that the conditional RSAP lacks a polarization.

At the zero section, every line `ell` in the multiplicity space gives an
`H_bal`-invariant Lagrangian

```text
L_ell = ell tensor U,          ell in RP^1,
```

because a skew form vanishes on a line. The vertical line is distinguished by
the cotangent projection. But each `L_ell` carries the same irreducible
`24|25` representation. Choosing a polarization specifies which variables
are wavefunction coordinates; it does not by itself produce a positive
kinetic form, semibounded generator, self-adjoint domain or positive BFV
cohomology pairing.

## 4. Krein and invariant-constraint controls

On `U`, an invariant fundamental-symmetry candidate must lie in
`End_H(U)=R`, so involutivity leaves only `+1` or `-1`. Multiplying `q` by
either sign merely swaps `(24,25)` and `(25,24)`.

On `M`, an invariant candidate has the form `D tensor 1_U`. Any associated
symmetric form is `B tensor q` for some nonzero two-dimensional symmetric
`B`. Pick one nonzero eigenvalue of `B`; pairing its eigenvector with one
positive and one negative vector of `q` produces opposite signs. No invariant
fundamental symmetry on the phase tangent can therefore positivize the
carrier.

The same representation theory closes the linear-constraint escape. Since
`U` is irreducible and occurs with multiplicity two, invariant phase-tangent
submodules are multiplicity subspaces `L tensor U`. A nonzero proper one has
dimension `49`, and its nonzero quotient is another copy of `U`; neither is
positive. This does not decide nonlinear constraints or ghost cohomology on
an actual stationary background.

## 5. What closes and what remains

Closed at zero-section invariant linear grade:

- symplectic doubling does not yield an invariant positive compatible metric;
- an invariant compatible complex structure exists only with an indefinite
  associated form;
- the canonical vertical polarization exists but does not solve positivity;
- invariant Krein fundamental symmetries cannot remove the `24|25` factor;
  and
- no nonzero invariant linear subquotient is positive.

Retained:

- the conditional `98D` classical symplectic realization and classical BFV;
- the canonical vertical real polarization;
- pseudo-Kähler invariant complex structures;
- non-invariant structures selected by a genuinely new stationary
  background or action term;
- nonlinear BFV/BRST cohomology with a separately proved positive pairing;
- explicit contour/Wick rotations and boundary-defined domains; and
- nonlocal or constrained quantizations at their own declared grades.

No ledger, datum, quotient booking, canon, public posture, particle or
phenomenology claim changes. Reproduce:

```bash
python3 tests/channel-swings/selected_k107_rsap_phase_space_compatible_complex_positivity_probe.py
```

The exact probe reports `39/39`, including a symbolic all-family certificate
for `A^2`, symplectic compatibility, symmetry of `KA`, and
`det(KA)=-(a^2+bc)` before the rational hostile fixtures are evaluated.
