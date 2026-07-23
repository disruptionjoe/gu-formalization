---
title: "H2 Lean finite core: bounded class-C enumeration and 2-primary closure"
status: review-support
doc_type: review
paper: "located-not-forced-generation-count-2026-06-29"
date: "2026-07-23"
grade: "LEAN-VERIFIED bounded finite deduction from an explicitly encoded, computed carrier census; no claim-status change"
---

# H2 Lean finite core

## Result

H2 now has a default-target Lean module,
`Lean/GUFormalization/LocatedNotForcedFiniteCore.lean`, plus the targeted entrypoint
`tests/located-not-forced/H2_FiniteCore.lean`.

The strongest honest bounded completion obtained is:

1. The computed carrier output is represented by two inequivalent chiral blocks and exact
   finite Schur-matching rules. Lean derives the invariant-space packet
   `2/2/2/2/0`: two linear, two bilinear, two physical split-signature
   sesquilinear, two T-type antilinear, and zero equivariant cross-chirality linear
   block matches.
2. Those matches, together with the seven characteristic/arithmetic rows, form an
   exhaustive finite type with `15 = 2 + 2 + 2 + 2 + 7` generators. Every encoded
   generator maps to one of the seven paper obstruction rows.
3. The finite modulus packet is exactly `[2, 2, 4, 8, 16, 2, 2]`, matching the
   extension engine's composition input. The `8` in the adjoint row is the engine's
   doubled `4k` proxy; the underlying identity `4 ∣ 4k` remains separately proved in
   `LocatedNotForcedLegs.lean`.
4. Product, gcd, and lcm of arbitrary powers of two are proved to be powers of two.
   An inductive theorem then covers every finite expression generated from the class-C
   atoms by those three operations. This replaces the engine's finite pairwise closure
   sweep with a theorem over arbitrary finite composition trees.
5. The existing exact 2-primary identities remain in the dependency:
   Rokhlin/RS bulk arithmetic, adjoint divisibility by four, odd lens-eta numerator
   with denominator `2^3`, spinor non-divisibility by `3`, Kramers mod two, and
   ghost-parity net zero. The targeted H2 test directly reuses representative RS,
   lens-eta, and spinor theorems.
6. `Hom(Z/3, Z) = 0` is now present as a typed Lean theorem for additive maps. The
   program-native order-three torsion carrier and a literal integer-valued generation
   index are distinct types and cannot be silently identified.

No `sorry` or project-defined `axiom` declaration is present. Explicit `#print axioms`
checks report only Lean/mathlib's standard logical dependencies (`propext`,
`Classical.choice`, and `Quot.sound`); the earlier `native_decide` implementation
dependency was removed.

## Construction and grade boundary

The finite model uses the program-native cross-chirality indefinite/Krein construction.
It does not replace it with a positive-Hilbert default. The positive subspace used by the
separate index-nullity theorem remains a subspace inside the indefinite Krein setting,
not a claim that the ambient carrier is positive definite.

The Lean theorem is conditional on the encoded two-block carrier census. It machine-checks
the finite block matching, exhaustive typed list, row assignment, arithmetic identities,
and closure deduction. It does **not** reconstruct the explicit `192`-dimensional
Clifford matrices or prove inside Lean that the physical carrier realizes the two supplied
irreducible blocks. That realization remains computed plus independently rechecked by:

- `tests/enum-completeness/enum_class_c_generators.py`;
- `tests/enum-completeness/verify/indep_check.py`;
- `tests/hardening-pass/enum_route_a_classification.py`.

Accordingly, the result is `LEAN-VERIFIED` for the bounded finite deduction and remains
computed/exact-script grade for carrier faithfulness. It is not an end-to-end symbolic
classification of the physical carrier, and it does not inflate the paper's claim grade.

## Validation

All Lean commands were serialized through the macOS host lock
`/tmp/CapacityOS-locks/lean-build.lock`; no overlapping Lean run was started.

```text
bash /Users/joe/Brain/CapacityOS/repos/private/system-runtime/kernel/run-convention/repo-session-sync.sh start \
  /Users/joe/Brain/CapacityOS/repos/public/gu-formalization
  -> exit 0; branch even with origin

/usr/bin/lockf -t 0 /tmp/CapacityOS-locks/lean-build.lock lake build
  -> exit 0; 8645 jobs; new finite-core module and default entrypoint built
  -> warnings were replayed pre-existing linter warnings in older modules

/usr/bin/lockf -t 0 /tmp/CapacityOS-locks/lean-build.lock \
  lake env lean tests/located-not-forced/H2_FiniteCore.lean
  -> exit 0; all examples elaborate; explicit axiom report contains standard logical
     dependencies only

python3 process_gates/lean_certificate_surface_audit.py
  -> exit 0; 6/6 checks pass
```

## Exact residuals

The following remain open and are not narrowed by this finite Lean core:

- an end-to-end Lean reconstruction of the actual `192`-dimensional
  `Cl(9,5)` Rarita-Schwinger carrier, its split-symmetry action, and the claim that its
  complete invariant Hom spaces are exactly the encoded two-block matches;
- Lean faithfulness for the full class-C characteristic-input list, including the actual
  sector bundle representations, boundary eta data, and inherited ghost grading;
- non-equivariant operators, external backgrounds or spurion VEVs, gauge twists by
  representations outside the sector, and the sharp beyond-class-C examples;
- unrestricted function-space/Fredholm completeness, including APS/end and family-index
  analytic terms;
- the definite `Y14`-fiber pushforward, actual global source action/domain, and the
  true-`Y14` source-action residual.

Therefore this is a bounded class-C finite-core completion, not a universal no-go and not
a closure of the true-`Y14` source-action route. It neither derives nor forbids three
integer-valued generations, changes no scientific verdict, and makes no manuscript,
queue, staging, reviewer, or claim-status edit.
