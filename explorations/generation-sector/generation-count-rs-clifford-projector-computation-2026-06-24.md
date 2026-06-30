---
title: "Generation Count RS Clifford/Projector Computation"
date: 2026-06-24
status: exploration
verdict: "ADVANCED_BUT_OPEN: explicit Cl(4,0) matrices, gamma-trace maps, kernel projectors, and a sample raw projected RS symbol were computed. The raw finite ranks are concrete, but they are not the K-theory/APS effective rank and do not decide Candidate A vs Candidate B."
depends_on:
  - explorations/generation-sector/generation-count-rs-rank-gate-2026-06-24.md
  - explorations/generation-sector/generation-count-rs-symbol-index-contract-2026-06-24.md
  - explorations/generation-sector/oq-rk1-rs-rank-first-principles-2026-06-23.md
  - explorations/generation-sector/oq-rk1-cas-matrix-rank-2026-06-23.md
  - explorations/analytic-index-fredholm/oq-rk2-aps-boundary-rs-k3-2026-06-23.md
  - explorations/analytic-index-fredholm/oq-rk2-aps-fc3-fc4-closure-2026-06-23.md
  - explorations/generation-sector/oq-rk2-fc4-k3-holonomy-rank-2026-06-23.md
executable:
  - tests/rs_clifford_projector_model.py
---

# Generation Count RS Clifford/Projector Computation

## Verdict

This pass turns part of the vague "RS projector rank" language into explicit matrices.
It constructs a concrete complex `Cl(4,0)` model for the K3 pulled-back pieces:

```
S_4^+ = C^2
S_4^- = C^2
F = C^16
V_+ = C^4 tensor S_4^+ tensor F = C^128
V_- = C^4 tensor S_4^- tensor F = C^128
G_+ : V_+ -> S_4^- tensor F = C^32
G_- : V_- -> S_4^+ tensor F = C^32
```

The raw gamma-trace kernels have complex rank `96`, and the orthogonal kernel projectors
are explicitly verified. For the sample nonzero covector `xi = (1,2,3,4)`, the raw projected
symbol

```
sigma_RS_raw(xi) = P_- (c(xi) tensor 1_F, componentwise on vector-spinors) P_+
```

is full rank as a map between the raw gamma-trace kernels: `rank_C = 96` on a `96 x 96`
restricted matrix.

This is real computational progress, but it is **not** the RS index. It does not construct
the gauge-fixed physical RS complex, the K-theory symbol class, the right-H conversion
certificate, the Chern character, or the APS/Atiyah-Singer characteristic-class integral.
Therefore the generation-count gate remains **OPEN**.

## Executable Artifact

Run:

```
python tests/rs_clifford_projector_model.py
```

The script also supports:

```
python tests/rs_clifford_projector_model.py --json
```

It is intentionally labeled:

```
RAW_SYMBOL_ONLY / NOT_INDEX_COMPUTATION
```

## Matrix Model

The gamma matrices are Hermitian `4 x 4` complex matrices:

```
gamma_1 = sigma_1 tensor sigma_1
gamma_2 = sigma_1 tensor sigma_2
gamma_3 = sigma_1 tensor sigma_3
gamma_4 = sigma_2 tensor I
```

They satisfy:

```
gamma_i gamma_j + gamma_j gamma_i = 2 delta_ij I
gamma_1 gamma_2 gamma_3 gamma_4 = diag(-1,-1,+1,+1)
chirality^2 = I
chirality gamma_i + gamma_i chirality = 0
```

The positive chiral subspace is the `+1` eigenspace of the chirality matrix, so
`rank_C(S_4^+) = 2`; the negative chiral subspace has the same complex rank.

The gamma-trace maps are assembled as horizontal block matrices:

```
G_+ = [gamma_1^{+->-} gamma_2^{+->-} gamma_3^{+->-} gamma_4^{+->-}]
G_- = [gamma_1^{-->+} gamma_2^{-->+} gamma_3^{-->+} gamma_4^{-->+}]
```

and then tensored with `I_16` for the internal coefficient `F = C^16`.

The kernel projectors are the orthogonal projectors:

```
P = I - G^* (G G^*)^{-1} G
```

This is a pointwise finite-dimensional model of the raw gamma-trace-free vector-spinor
bundle. It is not a gauge quotient and not an elliptic complex.

## Numeric Results

Main output from `python tests/rs_clifford_projector_model.py`:

```
Clifford relations ok: True (max error 0.000e+00)
chirality gamma_1...gamma_4 = [[-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
spinor ranks over C: {'S4': 4, 'S4_plus': 2, 'S4_minus': 2}

base G_+: C^8 -> C^2, rank_C=2, ker_C=6
with F=C^16: C^128 -> C^32, rank_C=32, ker_C=96
```

Projector checks:

```
base_P_plus: rank_C=6, P^2-P=0.000e+00, P-P*=0.000e+00, G P=0.000e+00
base_P_minus: rank_C=6, P^2-P=0.000e+00, P-P*=0.000e+00, G P=0.000e+00
with_F_P_plus: rank_C=96, P^2-P=0.000e+00, P-P*=0.000e+00, G P=0.000e+00
with_F_P_minus: rank_C=96, P^2-P=0.000e+00, P-P*=0.000e+00, G P=0.000e+00
```

The base kernel rank `6` is the complex Spin(4) gamma-trace-free vector-spinor rank
inside `C^4 tensor C^2`. Tensoring by `F=C^16` gives the raw complex rank:

```
6 * 16 = 96.
```

If one merely halves this complex rank as though a compatible right-H structure had already
been proven, one gets `48`, not the candidate effective ranks `4` or `8`. If one externally
imposes an additional internal `C^8` half, the raw rank becomes `48` complex, whose naive
H-halving is `24`. That reproduces the shape of the older "Spin(4)-irreducible refinement"
raw number, but only after adding an extra internal half as input. It is still not the
APS effective rank.

## Raw Projected Symbol

For the sample covector:

```
xi = (1, 2, 3, 4)
|xi| = sqrt(30) = 5.477225575052
```

the restricted base raw symbol is a `6 x 6` matrix with:

```
rank_C = 6
singular values =
  5.477225575052
  5.477225575052
  5.477225575052
  5.477225575052
  2.738612787526
  2.738612787526
```

After tensoring with `F=C^16`, the restricted matrix is `96 x 96` with:

```
rank_C = 96
```

So the sampled raw projected symbol has no pointwise rank defect on the raw gamma-trace
kernels. This is useful: it suggests that the elementary finite matrix obstruction is not
in `G_+`, `G_-`, or the raw projectors. The unresolved issue lies in identifying the correct
physical/gauge-fixed symbol class and its characteristic-class index.

The script also checks a pointwise principal gauge map:

```
epsilon |-> xi tensor epsilon
```

After projection to the raw gamma-trace kernel, this projected gauge image has:

```
rank_C = 32
raw symbol on projected gauge image: rank_C = 32
norm = 73.484692283495
```

Thus the raw projected symbol does **not** quotient or kill gauge directions in this finite
model. Gauge data remain additional structure, not something automatically solved by the
raw projector.

## What This Rules Out

This computation rules out treating the pulled-back raw gamma-trace kernel as a mysterious
rank-`4` or rank-`8` projector. In the explicit complex model with `F=C^16`, the raw answer is:

```
ker_C(G_+ tensor I_F) = 96
ker_C(G_- tensor I_F) = 96
```

Even optimistic H-language does not turn this raw rank into `4` or `8`. A raw rank may be
`96_C`, naively `48_H`, or with an externally imposed internal half `48_C` / naively `24_H`.
None of those is the APS effective rank.

It also rules out blaming the current gap on an absent elementary projector identity. The
orthogonal projectors exist and satisfy:

```
P_+^2 = P_+
P_-^2 = P_-
G_+ P_+ = 0
G_- P_- = 0
```

For the sampled nonzero covector, the raw projected symbol is full rank on the raw kernels.

## What Remains Missing

The true generation-count gate still needs all of the following.

1. A gauge-fixed physical RS operator or an elliptic RS complex, including ghost/subtraction
   terms. The raw gamma-trace-free vector-spinor operator is not enough.
2. A K-theory symbol class for that gauge-fixed operator/complex.
3. A verified right-H structure and a legitimate complex-to-H index conversion. This script
   reports complex ranks only.
4. The Chern character of the actual RS symbol class. In dimension four, the missing term is
   precisely the degree-four data that can make an "effective rank" differ from raw fiber rank.
5. A treatment of `ch_2(F)[K3]`, or a proof that the relevant internal coefficient is flat in
   the needed sense.
6. If APS boundary language is used, the eta and kernel terms for the projected/gauge-fixed
   boundary operator, not merely the raw flat spinor boundary operator.

Until those are supplied, the decision remains:

```
Candidate A: ind_H(D_RS) = 8, rank_eff = 4    OPEN
Candidate B: ind_H(D_RS) = 16, rank_eff = 8   OPEN
```

This computation narrows the problem: the next advance should not be another raw projector
rank. It should be the gauge-fixed/elliptic symbol class and its index density.
