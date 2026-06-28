---
title: "A4/A5: triality and the Adams e-invariant -- the predict-not-name pair"
status: exploration
doc_type: note
created: 2026-06-28
---

# A4/A5: triality (order 3) and the Adams e-invariant (order 24)

The last of the five escape hatches. These are the only routes that would PREDICT the integers 3 and 24
from independent theorems rather than fitting them, and the one route the kinematic-Krein / even-index /
ghost-parity panel is structurally blind to. A4 is a numpy-checkable structural gate; A5 is a
stable-homotopy specialist hand-off.

## A4 -- triality, structural verdict: sharpened negative

**The decisive gate is the commutant dimension.** The generation triplet is the self-dual `su(2)+` inside
`so(4) = su(2)+ (+) su(2)-`, which is the FULL commutant of the gauge group `Spin(10)` in `Spin(14)`
(`dim so(4) = 6`, machine-checked in `leg3_family_embedding_enumeration.py`). Triality is the order-3 outer
automorphism of `Spin(8)`, and `dim so(8) = 28 >> 6`. No `Spin(8)` commutes with `Spin(10)`. So triality, if
present, acts on gauge / representation content (it permutes `8v / 8s / 8c`), NOT on the 3-dimensional
`Lambda^2_+` family triplet that carries the generation multiplicity. The triality "3" (an 8-rep orbit
length) and the generation "3" (the self-dual two-form triplet, in the 6-dim gauge commutant) are different
threes; the commutant dimension forbids identifying them. A triality that normalized `Spin(10)` would
permute the Standard-Model charges WITHIN a generation, not the generations.

**Verdict:** sharpened negative. Triality names an order-3 structure, but it is decoupled by the commutant
from the family triplet, so it does not supply the generation count. (A full numpy scaffold -- build the
order-3 `tau` from the octonion Cayley table, verify `tau^3 = I` and outer-ness, and test whether its
128-spinor lift normalizes the `Spin(10)` generators on the internal indices -- would confirm this; the
structural commutant argument already settles the direction.)

## A5 -- Adams e-invariant, the specialist hand-off

This leg is NOT a numpy run. It is a stable-homotopy-theory question for a specialist:

- **The claim to check.** The third stable homotopy group of spheres is `pi_3^s = Z/24`; the image of the
  J-homomorphism in dimension 3 has order exactly 24; the Adams `e`-invariant is the homotopy-theoretic
  avatar of the APS `eta / rho` invariant (Adams 1966; APS II). If the chirality datum is read as the
  `e`-invariant of the framed-bordism class of the charge-1 self-dual `SU(2)+` twist on the GU end
  `RP^3 = S^3 / Z2`, then the denominator 24 is FORCED by a homotopy theorem, and `24 / 8 = 3` is its
  real-Bott (KO period 8) reduction.
- **What a specialist needs to settle.** (1) Identify the precise framed-bordism class of the self-dual
  `SU(2)+` twist on the lens space `L(2;1) = RP^3`. (2) Compute its `e_R`-invariant in `Z/24`, cross-checked
  against the APS `eta`-finite-sum for the quaternionic-twisted Dirac operator on `L(2;1)`. (3) Decide
  whether the `/8` is INDEPENDENTLY pinned by the real-Bott period / `rank_H(S) = 8`, or whether `24/8 = 3`
  is a coincidence (the canon already flags the unforced `/8` as the weak point; cf. the K3 `ch2 = -5376`
  target-fitting concern).
- **The convergence test.** Are A4's order-3 orbit and A5's framed class the SAME `Lambda^2_+` twist? If
  yes, `24 = 3 x 8` would be structural rather than target-fitted; A4's commutant decoupling currently
  argues they are NOT the same object, which is the honest tension to resolve.

**Forecast:** sharpened negative on both legs (the order-3 of triality is decoupled from the family triplet;
the `/8` of the e-invariant is not independently pinned), with the asymmetric upside that a specialist
confirmation of a forced 24 with a real-Bott `/8` pointing at the self-dual twist would be the one result
that derives the count from a theorem. Status: A4 structural-negative (numpy-confirmable); A5 open,
specialist-gated, the only leg of the whole five-hatch program that could still flip the headline.
