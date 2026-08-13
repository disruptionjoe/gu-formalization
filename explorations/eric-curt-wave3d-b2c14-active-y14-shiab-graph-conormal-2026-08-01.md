---
title: "Eric/Curt Wave 3D-B2C14R: the active Shiab has a descended quotient-grade reduction symbol"
status: active_research
doc_type: construction_result
created: 2026-08-01
branch: agent/null-clifford-omega1-repair
run: private orchestration runtime#meta/runs/historical-investigation/run-plan.md
registry: lab/process/eric-curt-wave3d-b2c14-active-y14-shiab-graph-conormal.json
probe: tests/channel-swings/eric_curt_wave3d_b2c14_active_y14_shiab_graph_conormal_probe.py
grade: "B2C14R QUOTIENT-GRADE COEFFICIENT PASS AFTER HOSTILE-REVIEW CORRECTION. The first packet computed an exact nonzero 78-dimensional Spin-stabilizer/lift block and incorrectly called it the reduction tangent. The repaired construction implements h=spin(9,5)=Lambda2 (91 dimensions), g/h with dimension 8165, and the complete 364-dimensional Spin-invariant grade-three quotient slice. All 91 vertical lift directions cancel when u and omega_LC co-move. Conservatively allowing every h-valued LC principal return W_h=T*Y tensor h (1274 dimensions), its active grade-three residual image is zero, while the reference graph has exact rank 364 on the executed owner for tested non-null normals, grade-three-projected lower-bound rank 132 at the tested null normal, and mixed-covector projected lower-bound rank 198. Exact witnesses 3/4 and -3/4 agree with a native 128x128 representation cross-check. The matching grade-three projected Gram block has rank 364 off the tested null cone and zero on it; this is not the all-grade residual Hessian. The quotient-grade moving Shiab derivative is nonzero, but the selected six-slot DM value is exactly zero. The active residual operator is therefore second order along genuine reduction tangents, while the complete all-grade primalizer, induced metric/LC graph, prolonged preboundary potential, characteristic kernel, and domain remain open."
canon_verdict_change: none
---

# B2C14R descended quotient-grade graph coefficient

## Result first

The B2C13 zero/nonzero fork is now closed on a genuine subspace of the
reduction field, but only after correcting the owner.

The first B2C14 draft used bivectors in `Spin(9,5)`. Those are changes of the
local lift, not tangents to the declared field

\[
\epsilon_{\rm red}\in P/H,
\qquad H=\operatorname{Spin}(9,5).
\]

Every control in that first computation passed because it correctly measured
the wrong object. The required hostile specialist review caught the Layer-0
failure before commit.

The repaired construction uses the exact reductive decomposition

\[
\mathfrak g=\mathfrak{sp}(32,32;\mathbb H)
=\underbrace{\Lambda^2}_{\mathfrak h,\ \dim 91}
\oplus
\underbrace{\left(
\Lambda^3\oplus\Lambda^6\oplus\Lambda^7
\oplus\Lambda^{10}\oplus\Lambda^{11}\oplus\Lambda^{14}
\right)}_{\mathfrak m\simeq\mathfrak g/\mathfrak h,\ \dim 8165}.
\]

It executes the complete `364`-dimensional `Lambda3` subspace of
`m`, proves that subspace is invariant under every bivector commutator, and
tests it against the complete `14*C(14,3)=5096` grade-three residual testers.

For a normal covector `xi`, put

\[
\ell_\xi a=\mathscr S_{\rm tr}(\xi\wedge a),
\qquad
C^+_\xi=\frac12(\ell_\xi+\ell_\xi^{\top_{\rm alg}}),
\qquad
C^-_\xi=\frac12(\ell_\xi-\ell_\xi^{\top_{\rm alg}}).
\]

In the real-jet convention used by B2C13,
`sigma(L^!)=-ell^(top_alg)`, so its displayed
`1/2(sigma(L)-sigma(L^!))` graph operator is `C+`. The probe also executes
`C-` separately so the conservative LC-return quotient does not depend on a
transpose-notation convention.

In the declared convention the graph used by B2C13 is the reference variation

\[
\sigma(DB_{\rm rot})(\xi)\chi_{\mathfrak m}
=-\xi\otimes\chi_{\mathfrak m}.
\]

Since `T=A-B_rot`, the fixed-`A` distortion symbol has the opposite sign,

\[
\sigma(DT|_{\delta A=0})(\xi)\chi_{\mathfrak m}
=+\xi\otimes\chi_{\mathfrak m}.
\]

That overall sign does not change any nonzero or rank verdict.

The direct half of `C+_xi` vanishes by `xi wedge xi=0`; its transpose half
survives.

## The descent correction

A local lift `u` represents the same reduction as `u h`. Under that change,
the LC connection moves by

\[
\omega_{\rm LC}\mapsto
h^{-1}\omega_{\rm LC}h+h^{-1}dh.
\]

The probe linearizes this law on all `91` bivector directions and verifies

\[
-\xi\otimes\chi_{\mathfrak h}
+\xi\otimes\chi_{\mathfrak h}=0.
\]

Thus a bare stabilizer coefficient is rejected as a reduction-field tangent.

For a true quotient representative, the as-yet-unbuilt induced LC response
could add an `h`-valued one-form. B2C14R does not assume it is parallel to
`xi`. It allows the conservative full space

\[
W_{\mathfrak h}=T^*Y\otimes\mathfrak h,
\qquad \dim W_{\mathfrak h}=14\cdot91=1274.
\]

The cancellation-proof test is

\[
\boxed{
[C^+_\xi(-\xi\otimes\chi_{\mathfrak m})]\ne0
\quad\text{in}\quad
\mathcal R/A_{\rm graph,\xi}(W_{\mathfrak h}).
}
\]

For every tested normal, the probe evaluates the direct and algebraic-
transpose images of all `1274` basis vectors in `W_h` separately. Each image
has exact grade-three-projected rank zero. Consequently both `C+(W_h)` and
`C-(W_h)` have rank zero, so either equivalent sign package for
`A_graph(W_h)` gives the same quotient. The quotient-grade graph image cannot
be canceled by any possible `h`-valued LC principal return.

## Exact quotient census

| normal | `q(xi)` | projected ranks `(direct,transpose,C+,C-)` on `W_h` | projected joint rank | projected quotient rank | grade-three Gram rank |
| --- | ---: | ---: | ---: | ---: | ---: |
| base spacelike `e0` | 1 | `(0,0,0,0)` | 364 | 364 | 364 |
| base null `e0+e3` | 0 | `(0,0,0,0)` | 132 | 132 | 0 |
| second spacelike `e1` | 1 | `(0,0,0,0)` | 364 | 364 | 364 |
| spacelike sum `e0+e1` | 2 | `(0,0,0,0)` | 364 | 364 | 364 |

The mixed covector polarization

\[
\frac12\left[C_{e_0+e_1}-C_{e_0}-C_{e_1}\right]
\]

has grade-three-projected quotient rank `198` after the same conservative
LC-return quotient. It is a lower bound on the full residual quotient rank.

The first two lexicographic exact coefficients are `3/4` and `-3/4`. The
first coefficient is reproduced as `0.75` by the native `128 x 128` matrix
representation while the owner/output satisfy the right-`H`, Krein-skew, and
`C+` tests. This is a representation cross-check of the same coefficient,
not an independent derivation of the operator.

The grade-three Gram ranks in the last column use the matching grade-three
Hodge/Clifford pairing only. They are useful projected comparators. They are
**not** the complete `K^top R_res K`, its inertia, its radical, or the full
characteristic kernel. Higher active grades remain uncomputed.

## Layer 0

| object | meaning | not identified with |
| --- | --- | --- |
| `u` | local lift | descended field `[u]=epsilon_red` |
| `h=Lambda2` | 91 vertical lift/stabilizer directions | `T(P/H)` |
| `m` | 8165-dimensional reductive complement representing `g/h` | full connection owner `g` |
| executed `Lambda3` | complete 364-dimensional invariant quotient slice | all of `m` |
| `DB_rot` | reference graph `-xi tensor chi` | fixed-`A` `DT=-DB_rot=+xi tensor chi` |
| `A_graph,xi(W_h)` | every conservatively allowed `h`-valued LC principal return; direct, transpose, `C+`, and `C-` projections all tested | only the diagonal `xi tensor h` subspace |
| projected quotient rank | nonzero projected residual class modulo LC returns; exact full owner rank only when it reaches owner dimension | full rank of the active residual symbol in the null and mixed cases |
| grade-three Gram | projected diagnostic block | complete residual Hessian or energy |
| scalar density control | one-dimensional product-rule/Green-sign fixture | full active fourteen-dimensional Green adjoint |

`S_tr` remains a bosonic contraction with an internal `pi_sp` projection. It
is not the spinorial Shiab, and the source does not uniquely select the
repository trace-line adapter.

## Trace reversal and moving data

The exact active Hodge has signature `(9,5)` and degree-two square `-1`. The
raw-Frobenius hostile comparator changes that square to `+1` and changes the
quotient-grade coefficient tensor. It is not Curt's `(7,7)` carrier.

Using a genuine grade-three quotient generator, the derivative moves the
trace gamma, `Phi1`, and `Phi2`. On the deterministic curvature fixture the
projected contribution supports are `(12,9,0)`: the raw `Phi2` derivative is
nonzero, but its selected projected contribution vanishes. The total moving
Shiab derivative remains nonzero.

The selected six-permutation `DM` response is exactly `0`. This corrects the
first stabilizer-owned draft value `-1`; nonzero `DM` responses in the other
quotient grades remain open.

A separate scalar variable-density control now has nonzero endpoint flux:

```text
direct = 107/15
bulk = -223/15
boundary = 22
```

It verifies the density product rule and boundary sign and rejects a frozen
density derivative. It does not construct the full active Green adjoint.

## What is proved

1. The exact vertical lift block cancels under the required G1 descent law.
2. `Lambda3` is a genuine Spin-invariant quotient-tangent subspace.
3. The active graph coefficient is nonzero on that descended subspace.
4. Its grade-three residual class survives modulo every possible
   `T*Y tensor h` LC principal return.
5. Hence the selected active residual operator contains a genuine second
   derivative of `epsilon_red`; active order collapse is killed on this
   subchannel.
6. Null and mixed covectors already have different grade-three-projected
   quotient ranks, providing lower bounds and concrete input for the later
   all-grade characteristic analysis.

## What is not proved

- the coefficient on the remaining quotient grades `6,7,10,11,14`;
- the complete all-grade residual tester/primalizer and Hessian;
- the actual induced metric/ambient LC graph rather than its conservative
  cancellation envelope;
- the full prolonged preboundary potential or its conormal momenta;
- the coupled characteristic kernel, constraints, or closed domain;
- a global `Y14` atlas/descent theorem;
- Einstein, Yang--Mills, Higgs/Yukawa, Standard Model, dark-energy,
  dark-matter, or PP3 recovery.

P1/P2/P3 are unchanged and unused. They supply no quotient tangent, Shiab
selector, symbol, graph coefficient, residual primalizer, conormal pair,
domain, or action term. Curt remains `FORMALLY_SEPARATE_INSIDE_ERIC_LANE`, and
`TG-1 AND TG-2 AND TG-3` remains `NOT_PROMOTED`.

## Source collision

`SOURCE-CONFIRMS`:

- draft p.44 eq.9.4 supplies the completed bosonic
  `T/Shiab/F_B + 1/2 D_B T + 1/3[T,T]` grammar;
- TOE official/local `02:17:07/02:19:17--02:20:33` places displacement from
  a gauge-rotated Levi--Civita connection in the contorsion slot;
- TOE supplies trace-reversed Frobenius and corrects “projection” to
  contraction.

`SOURCE-CORRECTS`:

- none.

`SOURCE-SILENT`:

- the named Shiab in this TOE episode;
- the repository graph sign, owner quotient, trace-line selector, exact
  transpose, and residual pairing;
- the `P/H` tangent realization and the active `(9,5)` quotient-grade map;
- exact ranks, null/mixed behavior, all-grade primalizer, prolongation,
  characteristic kernel, and domain.

`CONSTRUCTION-CORRECTS`:

- a local Spin lift direction is not a reduction tangent;
- direct `xi wedge xi` cancellation is not the full action graph coefficient;
- the stabilizer-owned `DM=-1` does not transfer to the tested quotient-grade
  direction, where the value is `0`.

## Next gate

The next gate is
`ECW3D-B2C15-FULL-QUOTIENT-GRADED-RESIDUAL-PRIMALIZER-AND-INDUCED-LC-GRAPH`:

1. execute every quotient-owner grade against every active residual grade,
   or prove the required cross-grade vanishing theorem;
2. assemble the all-grade residual lowerer/primalizer;
3. derive the actual induced metric/ambient LC graph and complete the active
   reduction--metric graph coefficient;
4. only then compute the full block Hessian, radical, and characteristic
   candidates, distinguishing covector polarization from the owner blocks
   `H_epsilon_epsilon`, `H_epsilon_g`, and `H_gg`;
5. build the complete prolonged preboundary potential only after those maps
   are typed.

The final mixed boson--fermion common-domain replay remains downstream.

## Validation

The executable probe passes:

```text
28 exact + 3 source receipts + 13 type-level + 12 planted = 56 PASS
```

Exact rational arithmetic is used for quotient ranks, witnesses, projected
Gram ranks, and the `DM` response. Source/type rows are receipts and scope
declarations.
