---
title: "Generation Count RS K3 Symbol-Index Attempt"
date: 2026-06-24
status: exploration
verdict: "OPEN_BACKGROUND_DEPENDENT: the raw constrained K3 RS symbol class is computable and gives an other index in the flat-F branch; the physical gauge-fixed GU RS complex and ch_2(F) are not yet fixed."
depends_on:
  - explorations/persona-and-dialectic/persona-review-cross-panel-synthesis-2026-06-24.md
  - explorations/generation-sector/generation-count-rs-rank-gate-2026-06-24.md
  - explorations/generation-sector/generation-count-rs-symbol-index-contract-2026-06-24.md
  - explorations/generation-sector/generation-count-rs-clifford-projector-computation-2026-06-24.md
  - tests/rs_clifford_projector_model.py
  - tests/rs_symbol_index_contract.py
  - canon/w2-y14-spin-structure.md
  - RESEARCH-STATUS.md
optional_executable:
  - tests/rs_k3_symbol_index_formula_audit.py
---

# Generation Count RS K3 Symbol-Index Attempt

## Verdict

The compact K3 RS gate remains open for the physical GU generation count.

This pass does compute the characteristic-class index for the standard raw
gamma-trace-free Rarita-Schwinger operator on closed K3, twisted by the internal
bundle `F = S(6,4)`. The answer is not a small effective rank. With
`rank_C(F) = 16` and flat/trivial `F`, the raw constrained operator gives

```
ind_C(Q_RS,F) = -608
ind_H(Q_RS,F) = -304       if the right-H structure and connection are verified
```

A commonly used BRST/anomaly-style virtual class for a gauge-fixed massless RS
field, if independently derived for the GU operator, would instead give

```
ind_C(Q_RS,F^BRST) = -672
ind_H(Q_RS,F^BRST) = -336  if the right-H structure and connection are verified
```

Those are honest "other index" outcomes for the simple flat-background symbol
classes. They are not Candidate A or Candidate B. Because the actual GU
gauge-fixed/ghost complex has not been derived, and because `ch_2(F)[K3]` is
unknown for a non-flat Sp(64) background, the final physical decision is:

```
physical constrained/gauge-fixed GU RS index on K3: still open
best status: OPEN_BACKGROUND_DEPENDENT / OPEN_MISSING_SYMBOL_DATA
```

## Surfaces Read

Required files read in this pass:

- `explorations/persona-and-dialectic/persona-review-cross-panel-synthesis-2026-06-24.md`
- `explorations/generation-sector/generation-count-rs-rank-gate-2026-06-24.md`
- `explorations/generation-sector/generation-count-rs-symbol-index-contract-2026-06-24.md`
- `explorations/generation-sector/generation-count-rs-clifford-projector-computation-2026-06-24.md`
- `tests/rs_clifford_projector_model.py`
- `tests/rs_symbol_index_contract.py`
- `canon/w2-y14-spin-structure.md`
- `RESEARCH-STATUS.md`

I also checked the relevant status surfaces in `canon/no-go-class-relative-map.md`
and the older OQ-RK/OQ3 notes for prior RS-index attempts. The key inherited
discipline is:

- K3 is a local compact-model working hypothesis for this gate, not a global
  canon assumption about `X^4`.
- The generation count is still OPEN because the RS analytic index has not been
  derived non-circularly.
- Raw projector ranks such as `416`, `96`, `64`, or `24` are not APS/K-theory
  indices.
- Physical degree-of-freedom counting is not an analytic index theorem.

## Anti-Smuggling Guard

The following are rejected as inputs:

```
ind_H(D_RS) = 8
ind_H(D_GU) = 24
rank_eff = 4
three generations
physical RS degree-of-freedom counting
normalizations chosen after seeing the target
```

They may be compared with a completed independent index only after the symbol
class, ellipticity, H-structure, Chern character, and any APS boundary terms are
known. This note does not use them to choose a formula.

## K3 Inputs

Let `M = K3` be the closed compact Riemannian K3 in the compact-model gate.
No boundary is used in the main computation.

Topological data:

```
Ahat(M) = -sigma(M)/8 = 2
chi(M) = 24
sigma(M) = -16
p1(TM)[M] = 3 sigma(M) = -48
```

For the real cotangent bundle complexification

```
V = T_C^*M
```

we use

```
rank_C(V) = 4
ch_2(V)[M] = p1(TM)[M] = -48
```

This `V` is the complexification of the real cotangent bundle used in the
Clifford symbol. It is not the holomorphic tangent bundle `T^{1,0}K3`; using the
holomorphic Chern character here is a different calculation.

Let the internal coefficient bundle be

```
F = s*(S(6,4))
rank_C(F) = n
rank_H(F) = n/2, if the H-structure is verified
k = ch_2(F)[M]
```

For the GU value, the expected complex rank is `n = 16`. I do not assume
`k = 0`; the flat branch sets `k = 0` only as a separately labeled special case.

## Operator Candidate I Can Defend

The strongest exact local object I can defend from the current files is the
standard gamma-trace-free Rarita-Schwinger operator on closed K3, twisted by
`F`.

Bundles:

```
S^+, S^-             chiral spinor bundles on K3
V^+ = T_C^*M tensor S^+ tensor F
V^- = T_C^*M tensor S^- tensor F
```

Gamma-trace maps:

```
gamma_+ : V^+ -> S^- tensor F
gamma_- : V^- -> S^+ tensor F
```

Gamma-trace-free RS bundles:

```
R^+ = ker(gamma_+)
R^- = ker(gamma_-)
```

Projectors:

```
P_+ : V^+ -> R^+
P_- : V^- -> R^-
```

The prior executable projector model constructs the finite-dimensional
`Cl(4,0)` version of these maps and verifies:

```
P_+^2 = P_+
P_-^2 = P_-
gamma_+ P_+ = 0
gamma_- P_- = 0
```

Raw constrained operator:

```
Q_RS,F : Gamma(R^+) -> Gamma(R^-)
sigma_Q(xi) = P_- (c(xi) tensor 1_F, componentwise on vector-spinors) P_+
```

Chirality:

```
Q_RS,F is the positive-to-negative chiral operator.
Changing this convention flips the sign of the reported index.
```

H-structure:

```
index_H = index_C / 2
```

is allowed only if the right-H structure is globally defined, the connection on
`F` preserves it, and `Q_RS,F` commutes with it. The `Cl(9,5) = M(64,H)` story is
strong evidence for this algebraically, but the K3 pulled-back `F` connection
must still preserve the H-structure. Without that check, only `index_C` is
reported.

Gauge map:

```
g_+(xi) : S^+ tensor F -> R^+
epsilon |-> P_+(xi tensor epsilon)
```

This is the principal gauge direction one would expect for a massless RS field.
However, the already-added projector script checks a sample nonzero covector and
finds that the raw projected symbol does not kill the projected gauge image. In
other words:

```
sigma_Q(xi) g_+(xi) != 0
```

in that finite model. Therefore `Q_RS,F` is an elliptic raw constrained operator,
not yet a gauge complex. A physical gauge quotient or BRST operator requires an
additional symbol-level construction.

## Boundary / APS Assumptions

The calculation below is for closed K3. There is no APS boundary correction.

If a punctured K3, collar, or Lorentzian slab is used instead, the formula must
be replaced by

```
index_APS = bulk_index - (eta(A_RS^gf) + h(A_RS^gf)) / 2
```

where `A_RS^gf` is the boundary operator for the same projected and gauge-fixed
RS complex. The older S^3 spectral-symmetry argument cannot be imported unless
the boundary operator is exactly this one. In this note, `eta` and `h` are not
assumed away.

## Symbol-Class Computation

The Spin(4) representation calculation gives:

```
V tensor S^+ = R^+ plus S^-
V tensor S^- = R^- plus S^+
```

Hence in the representation ring:

```
[R^+] - [R^-]
  = ([V] + 1) ([S^+] - [S^-])
```

Under the spin Thom isomorphism, the raw constrained RS symbol therefore has
coefficient virtual bundle:

```
E_raw = (V + 1) tensor F
```

This is the key non-circular computation. It uses the gamma-trace exact sequence
and the chiral spin Thom class, not physical degree-of-freedom counting.

For comparison, a few nearby virtual classes are:

```
full vector-spinor Dirac:        E_full = V tensor F
raw gamma-trace-free RS:         E_raw  = (V + 1) tensor F
BRST/anomaly-style physical RS:  E_BRST = (V - 1) tensor F   if two spinor ghost complexes are derived
```

The last line is not claimed as the GU physical operator. It is included because
it is a standard-looking gauge-fixed virtual class, but the two spinor
subtractions must be derived from the actual GU gauge fixing before it can be
used.

More generally, if `a` signed spinor ghost complexes are subtracted from the raw
operator, the virtual coefficient is:

```
E(a) = (V + 1 - a) tensor F
```

The value of `a` is not chosen from target numerology.

## Characteristic-Class Formula

For any virtual coefficient

```
E(q) = (V + q) tensor F
```

with integer `q`, the complex index is

```
ind_C(D^{E(q)})
  = integral_M Ahat(TM) ch((V + q) tensor F)
  = (4 + q) n Ahat(M) + n p1(TM)[M] + (4 + q) k
```

On K3 this becomes

```
ind_C(D^{E(q)})
  = (4 + q) n * 2 + n * (-48) + (4 + q) k
  = (-40 + 2q) n + (4 + q) k
```

The three relevant branches are:

```
full vector-spinor Dirac, q = 0:
  ind_C = -40 n + 4 k

raw gamma-trace-free RS, q = +1:
  ind_C = -38 n + 5 k

BRST/anomaly-style physical RS, q = -1:
  ind_C = -42 n + 3 k
```

The ordinary spinor ghost/Dirac complex is:

```
ind_C(D_F) = 2 n + k
```

so the BRST/anomaly-style branch differs from the raw constrained branch by
subtracting two spinor Dirac complexes:

```
(-38 n + 5 k) - 2(2 n + k) = -42 n + 3 k
```

This is a useful consistency check, not a derivation of the GU gauge-fixing
complex.

## Flat-F Special Case

If, and only if, the internal bundle is flat/trivial over K3:

```
n = 16
k = ch_2(F)[K3] = 0
```

then:

```
full vector-spinor Dirac:
  ind_C = -640
  ind_H = -320, if H-linear

raw gamma-trace-free RS:
  ind_C = -608
  ind_H = -304, if H-linear

BRST/anomaly-style physical RS:
  ind_C = -672
  ind_H = -336, if H-linear
```

These are not small effective-rank results. They show that the simple K3
symbol classes currently defensible from the Clifford/gamma-trace data do not
produce Candidate A or Candidate B.

## What Remains Unknown

The physical GU RS index is not computed by this note because the following data
are still missing:

1. The exact gauge-fixed GU RS operator or elliptic BRST complex.
2. A proof that its principal symbol has virtual coefficient `V - 1`, `V + 1`,
   or some other specified class.
3. The H-structure preservation of the pulled-back `F` connection.
4. The value of `k = ch_2(F)[K3]` for the actual Sp(64) / section-pullback
   background.
5. APS boundary data, if the closed K3 model is replaced by a compact
   manifold-with-boundary model.

Because `k` is unknown, even a specified virtual class would generally give a
background-dependent expression:

```
raw constrained branch:        ind_C = -38 n + 5 k
BRST/anomaly-style branch:     ind_C = -42 n + 3 k
generic ghost branch E(a):     ind_C = (-38 - 2a) n + (5 - a) k
```

For `n = 16`, different background values of `k` shift the index. The gate
cannot close until the physical background either fixes `k` or proves `k = 0`.

## Rejections

This pass explicitly rejects the following as proof of the RS index:

- Raw finite-dimensional projector ranks.
- Dividing a desired RS index by `Ahat(K3)`.
- Treating a physical RS degree-of-freedom count as an Atiyah-Singer theorem.
- Choosing the ghost subtraction or Chern class after seeing a desired output.
- Importing the S^3 eta cancellation for a different boundary operator.

## Decision

Decision for the raw constrained elliptic operator `Q_RS,F`:

```
OTHER_INDEX in the flat-F branch
OPEN_BACKGROUND_DEPENDENT if ch_2(F)[K3] is not fixed
```

Decision for the physical constrained/gauge-fixed GU RS operator:

```
STILL_OPEN / OPEN_MISSING_SYMBOL_DATA
```

The compact K3 computation has advanced: it now has explicit symbolic index
formulas for the natural vector-spinor, gamma-trace-free, and BRST-style virtual
classes. But it does not support Candidate A or Candidate B, and it does not
settle the generation count.
