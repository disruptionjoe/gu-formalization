---
title: "Pin+ degree-14 Smith-route audit"
status: active_research
doc_type: exploration
lane: "1"
created: 2026-07-22
updated: 2026-07-22
outcome: "PIN14-EXACT-Z2; GU-CLASS-OPEN"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
runnable:
  - tests/channel-swings/pin14_smith_degree_gate.py
---

# Pin+ degree-14 Smith and table audit

## Result

The Smith route is genuinely cheaper than a new Adams-resolution engine, but the earlier description of it
was one step too optimistic.  It does **not** reduce `Omega^{Pin+}_14` to ordinary Spin coefficients alone.
The exact primary-source cofiber sequence and the two vanishing Spin coefficients give

```text
Omega^Spin_14 -> Omega^Pin+_14 -> Omega^Spin_13((BZ/2)_+) -> Omega^Spin_13
      0                    isomorphism                         0
```

and hence

```text
Omega^Pin+_14
  ~= Omega^Spin_13((BZ/2)_+)
  ~= reduced Omega^Spin_13(BZ/2)
  ~= Omega^Pin-_12.
```

The last step is the reduced Smith equivalence
`MTSpin smash BZ/2 ~= Sigma MTPin-`.  Therefore the exact order problem has been lowered by two degrees and
changed flavor; it has not disappeared into the ordinary Spin table.

Anderson--Brown--Peterson's Pin exponent theorem applies in degree `12 = 4 mod 8` and says the degree-12
Pin-minus group has exponent `2` (degree 12 is beyond the exceptional lowest case).  This narrows the group
to a nonzero elementary 2-group.  Kirby--Taylor's direct `Pin+` table closes the remaining multiplicity:
they define `A(n)` to be the number of `Z/2` summands in `M Pin+_n`, give `A(14)=1`, and state that the
other, higher-order summands occur only in dimensions congruent to `0 mod 4`.  Since `14 != 0 mod 4`,

```text
Omega^Pin+_14 ~= Omega^Pin-_12 ~= Z/2.
```

The Smith route and the direct table are independent checks: the former explains the degree/flavor shift and
the latter supplies the missing rank.  The exact ambient bordism group is therefore closed.  This does not
identify the proposed GU datum with its nonzero element.

## Exact derivation and type checks

The four-periodic Smith family is essential.  Its four tangential structures are, in order,

1. `Spin x Z/2`,
2. `Pin-`,
3. `Spin x_{+/-1} Z/4`,
4. `Pin+`.

For the `Pin+` member, the published cofiber sequence is

```text
MTSpin -> MTPin+ -> Sigma MTSpin smash (BZ/2)_+.
```

Taking degree-14 homotopy gives the displayed long exact sequence.  The repository's already-used low-degree
Spin table has `Omega^Spin_13 = Omega^Spin_14 = 0`.  Splitting the disjoint basepoint removes the ordinary
Spin summand, and the published reduced equivalence shifts degree 13 to Pin-minus degree 12.  The runnable
gate checks all three degree shifts and prevents the old “ordinary Spin alone” wording from returning.

## What this does and does not settle

- **Settled:** `Omega^{Pin+}_14 ~= Z/2` exactly.
- **Cross-checked:** the Smith sequence identifies the same group with `Omega^{Pin-}_12`; hence that group is
  also `Z/2` under the cited convention.
- **Not settled:** whether GU supplies a Pin-plus 14-manifold/operator family at all.
- **Not settled:** whether the proposed `sigma` datum maps to a nonzero class.  A nonzero ambient group is not
  a proof that a particular unconstructed class is nonzero.

That last distinction is load-bearing.  This result repairs the ambient topology leg; it cannot repair the
missing operator/domain/line-bundle map.

## Primary evidence

- Debray, Devalapurkar, Krulewski, Liu, Pacheco-Tallaj, and Thorngren,
  [*The Smith Fiber Sequence and Invertible Field Theories*](https://arxiv.org/abs/2405.04649), especially
  the spin four-periodic Smith family, its `Pin+` cofiber sequence, and
  `MTSpin smash BZ/2 ~= Sigma MTPin-`.
- Anderson, Brown, and Peterson,
  [*Pin Cobordism and Related Topics*](https://eudml.org/doc/139415), Commentarii Mathematici Helvetici 44
  (1969), Theorem 5.1 and Corollary 2.1 (the Pin groups and their exponent pattern).
- Kirby and Taylor,
  [*A calculation of Pin+ bordism groups*](https://eudml.org/doc/140204), Commentarii Mathematici Helvetici
  65 (1990), p. 446: the table definition, `A(14)=1`, and the restriction of other summands to degrees
  congruent to zero modulo four.
- Anderson, Brown, and Peterson, *The Structure of the Spin Cobordism Ring*, Annals of Mathematics 86
  (1967), DOI `10.2307/1970690` (the coefficient table used at degrees 13 and 14).

## Receipt

`tests/channel-swings/pin14_smith_degree_gate.py` is deterministic, standard-library only, and returns
`PIN14-EXACT-Z2`.  It is a bookkeeping/type gate, not a replacement for the cited theorems or table.
