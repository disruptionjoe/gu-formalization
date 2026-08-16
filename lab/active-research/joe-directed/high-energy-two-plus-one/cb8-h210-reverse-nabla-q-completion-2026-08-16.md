---
artifact_type: exploration
status: exploration
doc_type: conditional_build_reverse_formal_transpose_completion
created: 2026-08-16
work_item: CB-8B
channel: high_energy_two_plus_one_prediction
target_claim: SC-GEN-53
title: "CB-8B: the reverse of gamma(q_H)d0 forces a nabla-q_H term, and generic normal variation opens a second Z-to-nu zero-order route"
grade: "EXACT local first-jet formal-density-transpose and Green-identity certificate under a declared parallel density, split metric, B-skew real-Cl(7,7) Clifford pairing, and compatible connection. CONDITIONAL on H210 and a typed horizontal q_H horn. The formula, its signs, both ambient halves, null fence, and pure-normal-Z restriction are exact. Global descent, the horn's ownership, an action, a selected density/domain/reality, and identification of source stars with this transpose remain unproved."
disposition: FORMAL_TRANSPOSE_EXACT__NABLA_Q_FORCED__PRINCIPAL_AND_LOWER_SHARE_SIGN__GENERIC_NORMAL_Q_JET_CONTAMINATES_ISOLATED_REVERSE_Z_PORT__PARALLEL_Q_PASSES_LOCALLY__TYPED_PULLBACK_X_PLUS_VERTICAL_PARALLEL_CONNECTION_QUALIFIED__BARE_LINE_AND_UNBRIDGED_X_STAGE_FAIL
canon_verdict_change: none
steering_effect: "Retain gamma(q_H)d0 as a full local forward/reverse candidate only with the explicit reverse lower term. If the reverse H210 coefficient is required to remain the sole zero-order map out of pure-normal Z, impose the exact restriction L_q|_Z=0; nabla_N q_H=0 is a sufficient stronger horn. A generic nonparallel source-Y q_H fails that isolation requirement. Do not absorb L_q into H210, call the source star a proved adjoint, or construct/select q_H."
depends_on:
  - lab/methods/source-native-comparator-routing.md
  - lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he4-path-reprioritization-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb2-h210-equation916-cross-half-composition-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb6-h210-equation916-observed-composition-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb7-forward-reverse-density-duality-composition-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb7-wave-h210-half-duality-reprioritization-2026-08-16.md
  - lab/process/hostile-reviews/2026-08-16-joe-directed-cb7-h210-half-duality-review.md
  - explorations/k77-wave2-q-receiver-trace-adjoint-ward-selection-2026-08-04.md
scripts:
  - tests/channel-swings/joe_directed_cb8_h210_reverse_nabla_q_completion_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — source-native conditional build.** This artifact
> concerns Weinstein's equation-(9.16) four-field grammar, equation-(12.22)
> F/imposter, equation-(11.6) Q/Z, `2+1`, and emergent-chirality claims.
> Ordinary family indices, net-chirality arguments, scalar-Higgs/VEV models,
> conventional `SO(10)` mass mechanisms, and familiar low-energy particle
> models are irrelevant comparators without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md`.
>
> Horns `H210` and `H210-CELL-ADAPTER(q_H)` are assumed. This reverse build
> never constructs or selects `q_H`, an action, a selector, an observer graph,
> a background, a density, a family row, a Pati--Salam reduction, a physical
> quotient, a domain, or a reality map. Bars remain independent fields.
>
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

# CB-8B — reverse `nabla q_H` completion

## Result first

Fix the local conventions stated below. For

```text
A_q = gamma(q_H) o d0 : Omega0(S_epsilon) -> Omega1(S_-epsilon),
```

the exact formal density transpose is

```text
A_q^times alpha
  = div(gamma(q_H) alpha)
  = gamma(q_H) nabla^a alpha_a
      + gamma(nabla^a q_H) alpha_a.                 (1)
```

The second summand is forced. It has the same sign as the principal divergence
term. Under the extra outer minus printed in the reverse-shaped cells of
equation (9.16), both signs reverse together:

```text
-A_q^times alpha
  = -gamma(q_H) nabla^a alpha_a
    -gamma(nabla^a q_H) alpha_a.                    (2)
```

This closes CB-7's local differential-order debt but produces a sharper
custody condition. Under the observer split

```text
T*Y = H* direct-sum N*,
Omega1(S) = (H* tensor S) direct-sum (N* tensor S),
```

the lower term is

```text
L_q(alpha_H + alpha_N)
 = sum_mu gamma(nabla^mu q_H) alpha_mu
   + sum_i  gamma(nabla^i  q_H) alpha_i.             (3)
```

Merely saying that `q_H` is horizontal does **not** delete the second sum. A
horizontal section can vary in normal directions. The exact current-Cl(7,7)
fixture gives an explicit normal first jet for which `L_q` is nonzero on the
pure-normal, normal-gamma-traceless H210 Z port on both ambient halves. Since
the first-jet-to-`Hom(Z,S)` map is linear, its vanishing set is a proper linear
subspace: generic first jets contaminate Z, while special nonzero jets may
still lie in the exact kernel.

Therefore:

- the generic nonparallel source-`Y` horn gives a well-typed formal transpose,
  but its reverse cell has an additional zero-order route from Z to the
  `nu`-half; the isolated reverse H210 coefficient is no longer the sole
  zero-order Z route;
- a fully parallel `q_H` deletes `L_q` and passes the local reverse completion;
- the exact isolation condition is `L_q|_Z=0`;
- the stronger, representation-independent condition `nabla_N q_H=0` is a
  newly stipulated sufficient horn for that isolation and still allows a
  horizontal lower term;
- a pulled-back `X` section is only a qualified route: it also needs a typed
  lift into the source-`Y` horizontal Clifford bundle and a pullback/split
  connection that actually gives `nabla_N q_H=0`.

None of these conditions is derived or selected here. They are reverse-
conditional pass/kill branches.

## 1. Conventions and exact sign derivation

Work locally on `Y` with a pseudo-orthogonal split `TY=H direct-sum N`, where
the exact fixture has signatures `(1,3)` and `(6,4)`. Let:

```text
B(gamma(v)s,t) = -B(s,gamma(v)t),
nabla B = 0,
nabla gamma = gamma nabla,
nabla g = 0,
nabla mu = 0,
d0 psi = e^a tensor nabla_a psi,
d0^times alpha = -nabla^a alpha_a.
```

Here `mu` is a declared local density used only to type the transpose. This
artifact does not construct or select it. Compact support, or deletion of the
local boundary term, is assumed only for the formal integration-by-parts
identity.

Because Clifford multiplication is `B`-skew,

```text
gamma(q_H)^times = -gamma(q_H).
```

Composition reverses under formal transpose:

```text
(gamma(q_H) d0)^times
  = d0^times gamma(q_H)^times
  = (-div)(-gamma(q_H) . )
  = div(gamma(q_H) . ).
```

The compatible-connection Leibniz rule then gives equation (1). If one adopts
the opposite Clifford-pairing convention, both displayed terms acquire the
same common convention sign. Their relative sign cannot change. The source's
outer minus then produces equation (2).

The exact probe checks the coefficientwise Green identity on independent
integer first jets. Omitting `L_q`, or changing only its sign, fails. Thus an
algebraic symbol dual and a full formal density transpose are different:

| object | sees `q_H` | sees `nabla q_H` | current status |
|---|---:|---:|---|
| algebraic symbol dual | yes | no | exact pointwise principal symbol |
| formal density transpose | yes | yes | exact locally under the declared conventions |
| source star in equation (9.16) | source-displayed glyph | source does not expand it | not identified with this construction |
| Hilbert/Krein operator adjoint | would require the full pairing and a common analytic domain | yes | not constructed |
| field reality / barred-field identification | not an operator transpose | not applicable | not imposed; bars remain independent |

A nonparallel density, noncompatible pairing, or non-Clifford connection would
add their own lower-order terms. They are outside this exact convention, not
silently zero in every possible realization.

## 2. Form degree and both ambient halves

The forward and reverse types are, simultaneously,

```text
A branch:
  nu+  in Omega0(S+) --A_q--> zeta- in Omega1(S-),
  zeta- in Omega1(S-) --A_q^times--> nu+ in Omega0(S+);

B branch:
  nu-  in Omega0(S-) --A_q--> zeta+ in Omega1(S+),
  zeta+ in Omega1(S+) --A_q^times--> nu- in Omega0(S-).
```

Both pieces of (1) remove one form index. Both contain one Clifford vector and
therefore flip ambient half. The lower term is zero order in `alpha`, but it
still has reverse form degree `Omega1 -> Omega0`; it is not an endomorphism of
the one-form field and it does not change the CB-7 parity result.

The exact fixture constructs H210 pure-normal Z tensors from source spinors in
both chirality eigenspaces, verifies their internal gamma trace is zero, and
then verifies that a horizontal `nabla_i q_H` produces a nonzero reverse
spinor in the correct opposite half for both tensors.

## 3. Total one-form decomposition and Z custody

The index `a` in (1) runs over the full source `Y`, not merely the four
horizontal directions. For an adapted frame, use `mu` for `H` and `i` for
`N`. Equation (3) follows directly.

The banked H210 forward arrow remains untouched:

```text
M_3 tensor 16+ --r tensor T_H210--> Z_A/144bar- subset N* tensor S-,
bar(M_3) tensor 16bar- --bar(r) tensor bar(T)_H210-->
    Z_B/144+ subset N* tensor S+.
```

But the full reverse of the repaired derivative acts on the same total
one-form field as the reverse H210 coefficient. On a Z input `z=(z_i)`, its
new zero-order piece is

```text
L_q(z) = sum_i gamma(nabla^i q_H) z_i.               (4)
```

There is no general gamma-trace identity forcing (4) to vanish: H210
gamma-tracelessness constrains `sum_i gamma(e^i)z_i`, while (4) contains the
independent coefficient tensor `nabla^i q_H`. The exact probe supplies a
counterexample with `z` still in Z and `nabla_i q_H` still horizontal.

This is **not** a failure of bundle typing. It is a failure of the stronger
claim that the reverse H210 coefficient remains the only zero-order map out of
the isolated internal-Z H210 port. The new route must not be absorbed into or
renamed H210: it depends on the first jet of the separately declared adapter,
not on the H210 `210` coefficient or family row.

The exact condition for zero-order Z isolation is

```text
L_q restricted to Z = 0.                            (5)
```

`nabla_N q_H=0` implies (5). It is sufficient, not proved necessary: special
nonzero normal jets could annihilate the particular Z submodule. Proving a
larger representation-theoretic iff statement would require a complete
intertwiner decomposition not claimed here.

Even under (5), the principal divergence term can act on normal one-form
components. That is the intended first-order reverse derivative, not the new
zero-order contamination diagnosed here.

## 4. Branch classifier

| horn or stage | exact local transpose | lower term | isolated reverse Z zero-order custody | disposition |
|---|---:|---:|---:|---|
| source-`Y`, `nabla q_H=0` | yes | zero | yes | **conditional pass** |
| source-`Y`, nonparallel but `L_q|_Z=0` | yes | horizontal and/or off-Z | yes | **qualified pass** |
| source-`Y`, generic nonparallel | yes | nonzero on total `Omega1` | no in general | **pass as a full transpose; kill as an isolated-H210 reverse completion** |
| `q_H` nowhere non-null | yes | depends on jet | depends on jet | required to inherit pointwise full-rank adapter receipt |
| nonzero null `q_H` | yes as a bundle map | depends on jet | depends on jet | **rank-retention kill** because `gamma(q_H)^2=0` |
| `q_H=0` | derivative repair vanishes | zero at that point if jet also zero | irrelevant | **cell-repair kill** |
| pullback-X with typed source lift and pullback/split connection giving `nabla_N q_H=0` | yes | horizontal only | yes | **qualified pass; bridge is an additional horn** |
| pullback-X without a source-Y Clifford lift | no | not typed | not typed | **stage kill** |
| graph-plane `H_J` section only after observation | not a source-cell map by itself | downstream | downstream | **stage kill unless a prior source-Y lift is separately declared** |

“Parallel” here is a covariant statement for the declared connection, not a
coordinate-constant shortcut. Likewise, the notation “pullback-X” does not by
itself imply vertical parallelism after an arbitrary graph embedding or moving
split.

## 5. A bare line and an untwisted source cell

A line subbundle `L_H subset H` supplies a canonical Clifford morphism

```text
c_L : L_H tensor S -> S,
```

but no canonical section `1 -> L_H`. Without a chosen section, the universal
derivative adapter naturally has a line-dual target:

```text
A_L : S -> L_H* tensor Omega1(S),
(A_L psi)(ell) = gamma(ell) d0 psi.
```

Its transpose can be written using a connection on `L_H`, but it is not the
untwisted reverse operator above. More importantly, the banked H210 term lands
in untwisted `Omega1(S)`. It cannot be added to `A_L` unless H210 is also given
a compatible line-dual lift. That is a new source-slot bridge, not a free
benefit of retaining only the line. The bare-line/untwisted-source-cell branch
therefore remains killed.

## 6. Module custody and source semantics

The lower term does not modify the banked forward zero-order H210 map or the
CB-6 forward order

```text
Z/internal-144 --O_J--> H_J* tensor S
  --Gamma_H,J^intr--> S --kappa_J--> F_corr.
```

It does change the proposed **reverse full-cell** zero-order inventory unless
condition (5) is imposed. No backward `kappa`, observation, or F-shaped chain
is inferred. `M_3`, Z/internal-`144`, and F/imposter remain distinct. The bars
remain independent Berezin fields; equation-(9.16) stars are not promoted to
this formal transpose, an analytic adjoint, or a reality map.

Ordinary Higgs, family-index, net-chirality, anomaly, mass, and low-energy
comparators have no role here without a typed bridge. Both ambient halves and
the source's emergent-chirality interpretation are retained.

## 7. Strict claim ceiling and next discriminator

The strongest warranted statement is:

> Given H210, a typed horizontal `q_H` section on source `Y`, a compatible
> Clifford connection, a parallel density and the declared B-skew pairing,
> the local formal density transpose of `gamma(q_H)d0` is exactly (1). Its
> principal and `nabla q_H` terms both have the reverse source cell's form
> degree and ambient half on both conjugate branches. A generic normal first
> jet of `q_H` gives a nonzero additional zero-order map from the pure-normal
> H210 Z port. Retaining isolated reverse-H210 zero-order custody therefore
> requires `L_q|_Z=0`; `nabla_N q_H=0` is a sufficient stronger horn.

This is not a source extraction or a global operator theorem. There is no
action, no selector, no graph/background construction, no density selection,
no common domain, no reality map, no Hilbert/Krein operator adjoint, no family
row, no reduction, no quotient, no external-datum construction, no mass, no
scale, no threshold, no spectrum, no cancellation theorem, no observable,
and no phenomenology.

No action, selector, density, domain, reality, mass, scale, spectrum, or
observable is constructed.

The integrated CB-8 audit finds no already-admitted source-`Y` or pullback
connection horn that implies `L_q|_Z=0`. Preserve that exact condition as an
externally triggered reopen criterion, not as authorization to search for a
connection or owner. The vertically parallel branch is a coherent local
conditional full-operator type but is over-conditioned and low fertility;
the generic full forward/reverse repair loses isolated H210 custody, while the
banked zero-order CB-6 chain survives unchanged.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 python3 tests/channel-swings/joe_directed_cb8_h210_reverse_nabla_q_completion_probe.py
PYTHONDONTWRITEBYTECODE=1 python3 tests/channel-swings/joe_directed_cb8_h210_reverse_nabla_q_completion_probe.py --selftest
```
