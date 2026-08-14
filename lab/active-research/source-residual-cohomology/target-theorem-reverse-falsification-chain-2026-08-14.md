---
title: "Conversation note: GU superposition target and backwards falsification"
status: active_research
doc_type: research_content_note
created: "2026-08-14"
lane_id: SRC-RES-COH-01
claim_grade: "CONDITIONAL TARGET AND BACKWARDS NECESSARY-CONDITION SKETCH; NO GU PHYSICS THEOREM"
canon_verdict_change: none
---

# GU superposition target theorem and reverse falsification chain

## Result first

The missing full GU solution is too expensive to make the only way to reason
about the hypothesis. A useful conditional strategy is:

```text
forward construction: actual solution -> complex -> physical state space
reverse falsification: proposed physical state space -> necessary conditions
                       -> cheapest structural no-go first
```

The backwards reasoning is logically valid because it tests implications of the
form

```text
target T implies necessary condition N;
not N therefore not T.
```

It is deliberately asymmetric:

```text
failure of N  -> certified kill at the declared scope;
survival of N -> only NOT-YET-FALSIFIED at that scope.
```

Survival never manufactures the missing background, complex, domain or
quantum interpretation.

## The conditional target theorem

Let

```text
Phi_*=(gimel,epsilon,varpi,nu,zeta,...)
```

be a legal Lorentzian GU field configuration satisfying the complete
action-owned total residual and stationary equations. Let

```text
gauge parameters --K--> field perturbations --L_Upsilon--> residual perturbations
```

be the total linearized symmetry/residual complex on one common carrier and
closed domain. The strongest currently useful target is:

> **Conditional GU physical-cohomology target.** The physical first
> cohomology
> `H_phys=ker(L_Upsilon)/closure(im K)` admits an action-derived complex
> structure `J_phys`, a positive nondegenerate Hermitian pairing and
> well-posed unitary Lorentzian evolution. The complex scalar action and
> linear evolution are intrinsic to the GU construction rather than supplied
> by an external quantization step.

In formulas, the target includes

```text
J_phys^2=-1,
<psi,psi>_phys>0 for psi!=0,
U(t) J_phys=J_phys U(t),
<U(t)psi,U(t)phi>_phys=<psi,phi>_phys.
```

Then for physical states `psi_1,psi_2` and complex scalars `a,b`,

```text
a psi_1+b psi_2
```

is again a physical state and evolution preserves the combination. This is
the target sense of intrinsic superposition. It does not yet include a Born
rule, measurement postulate, interacting Fock space or empirical
decoherence law.

## Saved forward chain

```text
F0  actual action-owned GU solution Phi_*
     Upsilon(Phi_*)=0 and every independent Euler row vanishes
      |
F1  total gauge-residual complex on one carrier
     L_Upsilon K=0, reducibility and boundary extension owned
      |
F2  genuine infinitesimal solutions modulo gauge
     H^1=ker L_Upsilon / closure(im K)
      |
F3  common closed Lorentzian domain and well-posed evolution
      |
F4  descended J plus positive nondegenerate physical pairing
      |
F5  intrinsic complex physical Hilbert space
      |
F6  superposition preserved by physical evolution
```

The forward implications are construction burdens, not established arrows.

## Backwards falsification questions

### Endpoint specification

Fix what is being attacked. The endpoint requires an internally supplied
complex scalar structure, physical linear closure and norm-preserving
evolution. A merely complexified classical bundle, a pointwise `J`, or an
externally quantized Hilbert space does not meet the target.

**Kill:** show that every claimed realization imports its complex scalars or
state-space linearity only during ordinary quantization.

### Can `J` descend to the quotient?

For a field-space candidate `J_F`, a sufficient typed test is

```text
L_Upsilon J_F = J_E L_Upsilon,
J_F K = K J_g,
J_F^2=-1.
```

Equivalently, `J_F` must preserve both `ker L_Upsilon` and `im K`; otherwise
`[psi] -> [J_F psi]` depends on the representative and is not a physical
operator.

**Candidate kill:** the proposed `J_F` fails either invariant-subspace test.

**Route kill:** prove that no source/action-admissible `J_F` can satisfy them,
or prove that the candidate exhausted by the no-go is the unique admissible
one. Killing `J_10`, `+/-J` or one twistor polarization alone does not kill
all intrinsic complex structures.

### Can the pairing descend and become positive?

For a candidate pairing `beta` on linearized solutions, require

```text
beta(K eta,v)=0                  for v in ker L_Upsilon,
rad(beta restricted to ker L)=closure(im K),
beta(J_F u,J_F v)=beta(u,v),
beta_phys([u],[u])>0             for [u]!=0.
```

The first two conditions make the quotient pairing well-defined and
nondegenerate; the last two make it positive Hermitian data. A Krein form on
the unreduced carrier is not yet this object.

**Candidate kill:** a negative or null physical direction survives every
declared gauge quotient/polarization for that candidate.

**Route kill:** prove that every action-admissible pairing or fundamental
symmetry has such a surviving direction. One bad polarization is only a
candidate kill.

### Can one common Lorentzian domain carry the maps?

Require dense domains on which `K`, `L_Upsilon`, `J_F`, the pairing and
evolution are simultaneously defined; `L_Upsilon` must be closed or
closable, `J_F` must preserve the domain, Green flux must obey the selected
boundary condition, and the reduced evolution must be well posed.

**Candidate kill:** principal-symbol, boundary-flux or domain incompatibility
that no lower-order correction can repair.

**Route kill:** a theorem covering every admissible domain/background in the
declared class. Failure of one boundary condition does not kill all domains.

### Is the proposed physical cohomology nontrivial and correctly typed?

Conditionally introduce `K` and `L` with the exact source representations and
test

```text
sigma(L)(xi)sigma(K)(xi)=0,
H^1_xi=ker sigma(L)(xi)/im sigma(K)(xi),
```

across timelike, spacelike and null covectors, then include lower-order and
boundary data. A raw symbol quotient, multiplicity or algebraic kernel is not
a physical mode count.

The gauge quotient also needs a topology. If `im K` or the nonlinear gauge
orbits are not closed in the selected solution topology, the naive quotient
can be non-Hausdorff. One must either prove closed image/orbits on the chosen
domain or explicitly use `closure(im K)` and account for the additional lost
classes. This is distinct from operator closedness in the preceding question.

**Candidate kill:** the proposed physical sector is zero, has the wrong
representation, consists entirely of gauge/constraint modes, or has a
non-Hausdorff gauge quotient with no action-owned completion on its declared
carrier.

### Can the total complex be assembled at all?

Test whether the internal, diffeomorphism, fermion, metric/section and
boundary maps share one carrier, bracket/reducibility structure and action
owner. This is where the current rank-25 internal and rank-four physical
diffeomorphism packets must be composed rather than merely juxtaposed.

**Candidate kill:** a representation, order, codomain or semidirect-bracket
obstruction prevents composition for the declared candidate.

### Does the required GU background exist?

Only after cheaper necessary conditions survive do we pay for the complete
background:

```text
Upsilon_B(Phi_*)+Upsilon_F(Phi_*)=0,
all independent Euler rows=0,
all carrier, reality, boundary and domain conditions legal.
```

This is the construction currently named `SR-1B`. A formal zero field or generic finite model is not a
GU solution until its Observerse geometry and owner equations are proved.

## Illustrative finite descent controls

Two exact real-linear quotient controls would distinguish the questions.

1. A four-dimensional candidate with a one-dimensional gauge image and a
   complex structure rotating that gauge vector out of the gauge image. The
   same physical class acquires different `J` images under a change of
   representative, so `J` does not descend.
2. A six-dimensional complex with a two-dimensional gauge image, a
   two-dimensional physical cohomology and compatible complex structures on
   gauge, physical and residual pairs. Its semidefinite carrier pairing has
   radical exactly equal to the gauge image on `ker L` and descends to the
   Euclidean pairing on physical cohomology. Replacing the physical block by
   signature `(1,1)` preserves descent but fails positivity.

These controls would distinguish descent, nondegeneracy and positivity. They
would prove nothing about GU's unassembled total carrier.

## Epistemic discipline

For any backwards result, distinguish four things:

```text
target class:       which J/pairing/operator/background family was tested
quantifier:         one candidate, finite family, or all admissible objects
result:             KILLED or NOT-YET-FALSIFIED
promotion ceiling: what missing lower layer prevents a positive conclusion
```

This strategy may falsify a candidate before `SR-1B`. It may not promote
superposition, physical cohomology, positivity or even background existence.

## Cheapest first question

Start with `J` descent, because it is algebraic and cheapest: test whether the
repo's candidate `J_10`, its two signs, and the base/normal twistor complex
preserve the already-owned candidate kernels and gauge images. Report
candidate-specific failures separately. Only a uniqueness/exhaustion theorem
can turn those failures into a kill of H1-R itself.
