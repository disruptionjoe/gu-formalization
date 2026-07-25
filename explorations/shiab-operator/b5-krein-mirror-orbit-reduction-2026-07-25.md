---
title: "B5 Krein-adjoint and mirror reduction: 136 complex cells collapse to an exact 39-orbit phase problem"
status: active_research
doc_type: result
created: 2026-07-25
run_id: RUN-20260725-031112-gu-formalization-progress
lane_id: "1"
work_item: B5-INDEPENDENT-RECONSTRUCTION
code: tests/shiab_b5_krein_mirror_orbit_reduction.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# B5 Krein-adjoint and mirror-orbit reduction

## Result

`B5-KREIN-MIRROR-ORBIT-REDUCTION-COMPLETE`.

The complete 136-cell complexified B5 observer-symbol space has an exact
support reduction under formal-adjoint transpose \(T\) and the declared
normal-chirality mirror support exchange \(M\):

```text
136 ordered complex cells
-> 68 fixed-point-free formal-adjoint edges
-> 39 joint <T,M> orbits
   = 29 four-cell orbits + 10 two-cell orbits.
```

The ten two-cell orbits are exactly the adjoint edges joining one labeled slot
directly to its mirror. They are the only cells fixed by \(TM\). They consist
of:

- two mirror edges in each of the `S`, `imGamma`, and `kerGamma` provenance
  copies; and
- four mirror edges inside `X`.

This closes the algebraic part of the native-adjoint reduction without
choosing a differential or a native phase.

## Construction fork

The computation stays on the program-native fork:

- observer-restricted `(9,5)` Rarita-Schwinger carrier;
- all 20 labeled irreducible slots;
- all three provenance copies;
- the full eight-summand extra block `X`; and
- formal Krein adjoint, not a positive-Hilbert replacement.

It distinguishes three structures that cannot be renamed into one another:

1. \(T\), the support action of formal adjoint;
2. a **linear** normal-chirality coflip; and
3. an **antilinear** real/quaternionic coflip.

The last two yield different coefficient reductions even though their support
permutation is the same.

## Exact orbit theorem

Let \(\mathcal C\) be the 136-dimensional complex coefficient space on the
ordered cells from the complete matrix. The matrix has no diagonal cells, so
\(T\) is fixed-point-free. The declared mirror exchanges every labeled slot,
so \(M\) is also fixed-point-free. They commute.

Formal Krein self-adjointness has the coefficient form

\[
c_{ji}=\epsilon_{ij}\,\overline{c_{ij}},
\qquad |\epsilon_{ij}|=1,
\]

after absorbing the invariant-pairing and symbol-adjoint phase into
\(\epsilon_{ij}\). Each of the 68 transpose edges therefore contributes one
complex parameter, giving a real 136-dimensional adjoint space. This count is
independent of the unfrozen unit phases.

### Linear coflip

For each of the 29 four-cell orbits, the mirror-even and mirror-breaking
subspaces each have real dimension two after formal adjoint. For each of the
ten special two-cell orbits, the mirror action on the complex edge parameter
is an antilinear involution; each parity has real dimension one. Therefore:

```text
linear coflip:
  mirror-even     = 68 real dimensions
  mirror-breaking = 68 real dimensions.
```

The support class does not prefer either parity.

### Antilinear coflip

For each four-cell orbit, both parities again receive two real dimensions. On
a special edge, however, the antilinear coflip and formal adjoint have the
same support exchange. Their product is complex-linear and carries one
normalized phase invariant \(\delta_e\in\{+1,-1\}\). The entire two-real-
dimensional edge belongs to the even sector for \(\delta_e=+1\), or to the
breaking sector for \(\delta_e=-1\).

If \(k\) of the ten special invariants are \(+1\), then:

\[
\dim_\mathbb R\mathcal C_{\rm even}=58+2k,\qquad
\dim_\mathbb R\mathcal C_{\rm break}=78-2k,
\qquad 0\le k\le10.
\]

Thus all \(2^{10}=1024\) assignments collapse to the exact eleven possible
dimension pairs:

```text
(58,78), (60,76), ..., (68,68), ..., (76,60), (78,58).
```

Current owner truth does not select one of these assignments. Reporting only
the symmetric `(68,68)` case would silently choose either the linear coflip
type or five favorable antilinear phase signs.

## Hostile controls

The executable certificate fails or changes its census when:

1. `X` is omitted;
2. the three provenance copies are collapsed;
3. transpose and mirror do not commute;
4. a fixed cell is introduced;
5. linear and antilinear coflips are treated as the same coefficient action;
   or
6. one of the 1024 native phase assignments is silently selected.

The result is reconstructed from the exact matrix code. It does not copy the
target counts `136`, `68`, `39`, `29`, or `10` into the cell enumeration.

## What this does and does not freeze

This Run freezes:

- the adjoint/mirror support group;
- all 39 joint orbits;
- the ten phase-sensitive special edges;
- the real formal-adjoint dimension;
- the linear-coflip parity dimensions; and
- the complete antilinear phase-parametric dimension family.

It does **not** freeze:

1. the phase-normalized invariant pairing on every observer summand;
2. whether the physical coflip is linear or antilinear;
3. the ten antilinear special-edge phase invariants;
4. the formal-adjoint sign of the actual differential expression;
5. the Green boundary form; or
6. a common closed, symmetry-compatible operator domain.

Representation multiplicities cannot select the last two. Existing
repo-local graph-domain work proves that admissible domains can exist after
a Green form is frozen, while also proving that existence does not canonically
select one. Therefore no domain or lower-order term is inferred here.

## Operational outcome

`CONDITIONAL`.

The previous qualitative residual has been reduced to an exact finite
decision surface:

```text
B5-NATIVE-PHASE-AND-DOMAIN-PACKET
```

The smallest next native packet must supply:

```text
slot_pairing_phases
coflip_linearity_and_phases
formal_adjoint_sign
Green boundary form
common closed domain
```

Once those fields are frozen, the certificate can select one admissible real
coefficient space and send the genuine mirror-even and mirror-breaking
classes to symbol exactness. Until then, the existence of 58--78
mirror-breaking real directions is an algebraic availability result, not a
native GU selection or a mirror-obstruction verdict.

No claim, canon verdict, scientific grade, paper state, or public posture
changes.
