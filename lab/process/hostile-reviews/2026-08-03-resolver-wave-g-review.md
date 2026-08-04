---
artifact_type: hostile_review
created: 2026-08-03
target: RESOLVER-WAVE-G-Q6-NATIVE-SP-TILTED-SOURCE-PORT-AND-TRANSVERSE-EULER
status: PASS_AFTER_REPAIRS
reviewers:
  - Clifford representation and exact computation
  - source and differential geometry
  - variational PDE and operator theory
meta_charges:
  - summary_outruns_artifact
  - rigorous_work_defends_superseded_object
---

# Hostile review: Resolver Wave G

## Final verdict

`PASS_AFTER_REPAIRS` at the grade

```text
PARTIAL_NATIVE_Q6_AND_LOCAL_TILTED_SCHEMA_CONSTRUCTED
```

The final independent reruns pass:

```text
29 exact + 3 Sage + 6 source + 17 type + 9 planted = 64/64
```

The Wave G scope audit, Python compilation, strict JSON parsing, process/test
inventories, predecessor regressions, and diff checks also pass.

## Review 1: Clifford representation and exact computation

Final verdict: `PASS`.

The reviewer independently confirmed:

- the number-operator eigenvalue on all 16,384 blades;
- native grades, dimensions, and denominator `122880`;
- `q6` identity on 3,003 grade-six blades and annihilation of 5,253 others;
- one-form rank 42,042 and kernel 73,542;
- composite rank 252 and kernel 115,332;
- the Sage `D7` Hom census `0,0,4,0,1,0,0`, including the live grade-ten
  near-miss;
- the native grade-three square-zero mover's K-anti/right-H matrix class,
  finite K-unitarity, exact grade mixing, frozen-projector failure, and moved
  repair;
- fixed coefficient and tensor adjoints remain scoped to fixed pairings.

The reviewer found no summary overreach after repair and no evidence that the
local `q6` subproblem was being defended as the public/global source map.

## Review 2: source and differential geometry

Initial verdict: `MUST-FIX`.

This review found the decisive error in the first draft: separate fixtures
for fixed `q6`, moved `q6`, tilted `T_omega`, and a 2-by-2 frame rule had been
compressed into “local tilted port constructed,” even though no combined
`Psrc(T_omega)` function or naturality test existed.

Required and completed repairs:

1. Demote the verdict, title, report, registry, README, and improvement
   surfaces from a constructed local port to a constructed local schema.
2. Record `local_Psrc=FORMULA_ONLY_UNINSTANTIATED` and
   `combined_Psrc_Tomega_naturality=NOT_TESTED`.
3. Rename the 2-by-2 object `frame_surrogate`; state that it is a `GL(2)`
   transformation fixture, not a Clifford frame or `Theta_Z`.
4. Scope the tilted calculation to a chosen local `A0=0` specialization;
   add exact `tau` homomorphism and semidirect associativity fixtures; leave
   the general `tau_(A0)` bridge open.
5. Replace the false `SOURCE-CORRECTS` identity claim for `epsilon_src` and
   `epsilon_IG` with `SOURCE-SILENT-ON-IDENTITY / LAYER-0-UNCERTAIN`.
6. Replace the circular Wave-F silence matcher with bounded checks against
   enumerated source surfaces and direct Portal locators for the intrinsic
   chimeric split.
7. Correct the final wording: Portal displays the `A0`-dependent covariant
   formula, not the `A0=0` ordinary-derivative specialization.

Final verdict after the 64-check rerun: `PASS_AFTER_REPAIRS`.

## Review 3: variational PDE and operator theory

Final verdict: `PASS`.

The reviewer confirmed that the final packet preserves:

- fixed coefficient/tensor adjoints versus the open global density/Hodge/Krein
  lowerer;
- diagnostic Euler decomposition versus actual restricted-action variation;
- the moving-projector chain term and source-root Green return;
- zero differential order for fixed `q6/Pext` versus open derived
  `Theta_Z` order;
- separate active and transverse Euler equations;
- open Ward identity, Green form, quotient, domain, and both observation and
  no-leakage equations;
- P1/P2/P3 unchanged and unused.

The repaired summary points to the actual combined/public/native/global
construction, so it no longer defends a superseded isolated-projector target.

## Nonblocking evidence notes

- Clifford mixing is exact sparse rational algebra. K/right-H membership and
  K-unitarity of the 128-by-128 mover are finite numerical controls inherited
  from the native matrix realization.
- The executable samples the `Pext` self-adjoint identity while the signed
  formulas establish it generally from `delta=j^times` and the orthogonal
  internal five-form projector.
- Several variational boundary rows are explicit type/scope sentinels, not
  mathematical computations. They are used only to prevent promotion.

## Two meta-charges

`summary_outruns_artifact`: `PASS_AFTER_REPAIRS`. The initial local-port
overclaim was found and removed.

`rigorous_work_defends_superseded_object`: `PASS`. The intrinsic chimeric
split replaces the stale route asking the coarse Clifford plane to invent a
`4+10` flag. The next gate requires the combined local source port and global
bundle/action construction; it does not ask for another isolated `q6` proof.
