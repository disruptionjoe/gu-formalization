# Reviewer guide -- one-command reproduction

*Companion to* `located-not-forced-generation-count-2026-06-29.md` *(hardening item H1).*

## The one command

From the repository root:

```
python papers/candidates/located-not-forced/reproduce_all.py
```

Dependencies: `numpy` and `sympy` (both standard). Runtime: a few minutes. The script is
deterministic (seeded) and self-contained -- it copies the verified carrier recipe rather than
importing the test tree, so it runs from a clean checkout with no path setup.

**Exit code 0** iff every load-bearing number in the paper reproduces; **exit 1** otherwise,
with a listed summary of any failures. Each check prints one line:

```
[MATCH]/[FAIL]  <claim> (Section N):  paper = <stated value>,  computed = <value>
```

## What it checks

Every number the paper leans on is **recomputed from first principles or from the carrier**,
then compared against the paper's independently stated value. The comparison target is the
paper's number; the computed value never reads from it.

| # | Load-bearing claim | Section | Paper value |
|---|---|---|---|
| 1 | Carrier Clifford Morita type `Cl(9,5)` | 2, 8 | `M(64,H)` |
| 2 | `rank(Gamma)` of the gamma-trace map | 2 | 128 |
| 3 | `dim ker(Gamma) = (14-1)*128` | 2 | 1664 = 2^7·13 |
| 4 | self-dual su(2)+ content of `ker(Gamma)` | 2, 3 | 640 / 832 / 192 |
| 5 | triplet (j=1) sector dimension | 2 | 192 |
| 6 | triplet Krein signature | 2, 6 | (+96, −96, 0) |
| 7 | `beta_S` pseudo-anti-Hermiticity residual | carrier | ~ 0 |
| 8 | Theorem 2 net chiral index (9,5) & (7,7) | 6 | ~ 0 (cited ~ −2.4e-15) |
| 9 | same-chirality Krein blocks ‖K(+,+)‖=‖K(−,−)‖ | 6 | ~ 0 |
| 10 | antilinear leg: index nullity under re-grading | 6 | 0 |
| 11 | adjoint Dirac index over su(2)±  multiplicity bundle | 4 | 12k (even); diagonal 24k |
| 12 | `pi_3^s = Z/24 = Z/8 ⊕ Z/3`, gcd(8,3)=1 | 5 | 24 = 8·3 |
| 13 | category error `Hom(Z/3,Z)=Hom(Z/24,Z)=0` | 9 | both 0 |
| 14 | located carrier Adams e-invariant `e_R` | 7 | 1/12 (order-3 part) |
| 15 | Pati-Salam `Spin(7,7)` chain → one generation | 8, App | 1 (chain-relative) |
| 16 | forcing-slot backbone (spin-1/2 = 2, spin-3/2 = −42, 256 = 2^8, 16·(−42)+3·ch₂ ≡ 0 mod 3) | 8 | all 2-primary or 1 |
| 17 | located carrier reaches ≤ 2 of 3 forcing properties | 8 | ≤ 2 of 3 |

## The discriminating controls (why this is not a tautology)

A harness that only restated hardcoded numbers would pass trivially -- exactly the "verification
theater" this repository warns against. So **every major check ships a control**: a scrambled or
wrong input that *must* produce a different number (or fail the same predicate). Controls print
inline, tagged `[CONTROL]`. The load-bearing ones:

- **Clifford type.** The same derivation machinery on the wrong signature `Cl(7,7)` yields
  `M(128,R)` -- a different division algebra and size -- so the `M(64,H)` result is
  signature-sensitive, not a constant. (The quaternionic type of `Cl(4,0)` is *measured*: its
  8×8 real commutant is 4-dimensional with every imaginary unit squaring to −1.)
- **Carrier dimensions.** Scrambled (non-self-dual) so(4) generators do **not** give a
  192-dim triplet -- the multiplicity requires the genuine self-dual su(2)+ structure.
- **Krein signature.** Replacing `beta_S` by the identity (wrong Krein metric) breaks the
  (96, 96) split.
- **Theorem 2.** The Euclidean `(14,0)` control is grading-*aligned* and gives `|chi| = 96`,
  proving the index genuinely detects chirality; the ~0 in (9,5)/(7,7) is real cross-chirality
  content, not an automatic zero. A random linear Krein isometry preserves `chi = 0`.
- **Antilinear leg.** A K-*definite* re-grading (not a chirality) escapes to `|chi| = 96` --
  exactly the residual the paper says an escape would require.
- **CRT.** A non-coprime split (`Z/8 ⊕ Z/2`) fails to reconstruct `Z/16` (max element order 8),
  so the 8·3 factorization works only because `gcd(8,3)=1`. And `Hom(Z/3, Z/3) = Z/3 ≠ 0`
  shows the vanishing `Hom(Z/3, Z)=0` is specifically about the torsion-free target.
- **e_R.** The gauge-channel Dirac eta `(2q²−4q+1)/8` is 2-primary for every integer q -- the
  order-3 burden lives only in the gravitational framing channel.
- **Pati-Salam.** The naive B−L-only hypercharge (dropping SU(2)_R) fails to reproduce the
  generation's n-values.
- **Forcing slot.** Replacing the `3·ch₂` coefficient by `1·ch₂` breaks the all-twists
  `≡ 0 mod 3` identity -- the identity is specific to the 2-primary structure, not automatic.

### Target-import guard

The integers `{3, 8, 24}` are **never hardcoded as answers**. `24` is derived as
`denom(B_2/4)` (Adams image-of-J, via sympy Bernoulli); `8` and `3` are its 2-primary and odd
parts, obtained by factoring the derived `24`; the multiplicity `3` is measured from the su(2)+
decomposition and from the order-3 part of `e_R = 1/12`.

## Honest scope

This harness is **internal-tier** in the paper's own three-tier vocabulary. What it does:

- lowers the barrier to external replication -- a referee re-runs every load-bearing number in
  a single pass, from a clean checkout, and sees each next to its paper reference; and
- makes the checks adversarial-by-construction (every one carries a control that must fail on
  a scrambled input).

What it does **not** do:

- it does **not** replace external peer review. Every result remains reproduced *within the
  same AI-directed process that produced it* -- not independently replicated, not peer-reviewed,
  not signed off by a named specialist. The paper's caveat (e) and its three-tier caveat stand
  unchanged.
- it does **not** touch the two genuinely open analytic residuals (the function-space
  APS/end-eta and family-index terms, and the true-`Y14`-bundle computation). Those are gated,
  not closed, and the harness makes no claim about them.
- passing this harness is **not** a claim of three generations. The paper does not claim three;
  no computed quantity in the program equals three, and this harness reproduces exactly that --
  the located-not-forced verdict, including the numbers that show the count is *not* internally
  forced.

The heavier verifications the paper cites (the full class-C enumeration engine, the four-way
forcing-slot toy, the decider's 26 checks, the Lean lane) live under `tests/` and `lab/` and are
referenced from the relevant checks; this script reproduces the load-bearing *numbers*, which is
the barrier H1 targets.
