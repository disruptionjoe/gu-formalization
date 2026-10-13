---
title: "K1806--K1810 full-Fisher anchored-score wave"
status: active_research
doc_type: exploration
updated_at: "2026-10-13"
---

# K1806--K1810: an anchored score closes slab two

## Result

The complete slab-two full-Fisher sublevel is excluded at

`T = 31835729061 / 200000000000000000`.

The seven K1796 residual leaves are exactly K1804's closed rectangle

```text
t in [56314519603/1099511627776, 887855469/17179869184]
z in [589/1024, 1185/2048].
```

K1806 fixes `h` to the exact score at K1788's slab-two boundary KKT anchor and
defines

```text
A(theta) = E_theta[s_theta h],
B(theta) = E_theta[h^2].
```

Cauchy gives `J(theta) B(theta) >= A(theta)^2`. In the native mixture
formula, `p_theta s_theta` cancels the varying mixture denominator, while
`B` contains it only linearly. This is the structural reason the witness is
stable when direct interval division of the full Fisher quotient is not.

K1807 integrates normalized parameter jets over 352 exact observation cells
on `[-11,11]`. It expands at the exact rectangle midpoint through degree five
and encloses every normalized sixth derivative over the complete rectangle.
An absolute coefficient bound, deliberately avoiding monotonicity guesses,
proves

```text
A_compact^2 - T B_compact
  > 3.0938112974946452920786941956604271275e-21.
```

K1808 supplies the omitted tails. Positive polynomial-exponential majorants
and the incomplete-Gaussian recurrence give

```text
J_tail < 3.122e-25,
B_tail < 5.627e-23,
|A_tail| <= sqrt(J_tail B_tail) < 4.191e-24.
```

Using the certified compact cap `|A_compact| < 2e-7`, the total tail
perturbation of the cross margin is below `1.064e-29`. Therefore

```text
A_whole^2 - T B_whole
  > 3.0938112868622235862286580499108618303e-21 > 0,
```

and `J(theta)>T` everywhere on the complete closed rectangle. K1796 already
excludes its complement by an exact odd-Hermite Bernstein lower bound. K1809
therefore closes slab two, including all of its residual faces and corners.
Together with K1792, slabs one and two are globally excluded.

## Hostile interpretation checks

- The Cauchy witness is a lower bound, not an equality claim away from the
  anchor.
- K1807 alone is compact-window evidence; K1808 is required for a whole-line
  theorem.
- The threshold result is a finite-strength scalar trial-functional theorem,
  not an unrestricted input law and not source-owned physics.
- Closing slab two does not prove the global optimizer. K1787 isolates one
  local slab-three stationary point, but 78 exact slab-three leaves and their
  exposed geometry remain globally open.

## Next transferable construction

Anchor `h` at K1787's exact slab-three stationary score. Apply the K1807
centered normalized-jet construction leafwise to the 78 K1804 slab-three
leaves, reusing K1808's analytic tail machinery. Uniform closed-leaf value
bounds discharge their faces and vertices automatically. Combine that bank
with a complete interval-Newton/Krawczyk exclusion outside K1787's isolated
box before any global optimizer promotion.
