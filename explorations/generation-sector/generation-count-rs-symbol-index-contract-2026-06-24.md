---
title: "Generation Count RS Symbol-Index Contract"
date: 2026-06-24
status: exploration
verdict: "CONTRACT_SPECIFIED: the executable gate is precise, but the RS index remains OPEN until the constrained/gauge-fixed K3 symbol class is computed without using ind_H(D_RS)=8 or rank_eff=4 as input."
depends_on:
  - explorations/generation-sector/generation-count-rs-rank-gate-2026-06-24.md
  - explorations/generation-sector/oq-rk1-rs-rank-first-principles-2026-06-23.md
  - explorations/generation-sector/oq-rk1-cas-matrix-rank-2026-06-23.md
  - explorations/analytic-index-fredholm/oq-rk2-aps-boundary-rs-k3-2026-06-23.md
  - explorations/analytic-index-fredholm/oq-rk2-aps-fc3-fc4-closure-2026-06-23.md
  - explorations/generation-sector/oq-rk2-fc4-k3-holonomy-rank-2026-06-23.md
optional_executable:
  - tests/rs_symbol_index_contract.py
---

# Generation Count RS Symbol-Index Contract

## Verdict

The next gate is now precise but not closed. The generation-count RS leg remains **OPEN**.

The required computation is not another raw RS projector rank. It is:

```
construct the constrained/gauge-fixed RS principal symbol on K3,
construct its K-theory symbol class,
evaluate the Atiyah-Singer/APS index,
then compare the resulting ind_H(D_RS) with Candidate A/B/other.
```

The value `ind_H(D_RS)=8`, the effective rank `rank_H(E_RS^eff)=4`, and the target
generation count `24` are forbidden as inputs. They are allowed only as comparison values
after the independent symbol-index computation is complete.

## Surfaces Read

This contract uses the prior wave note
`explorations/generation-sector/generation-count-rs-rank-gate-2026-06-24.md` as the immediate handoff. It also
uses the OQ-RK chain:

- `oq-rk1-rs-rank-first-principles-2026-06-23.md`
- `oq-rk1-cas-matrix-rank-2026-06-23.md`
- `oq-rk2-aps-boundary-rs-k3-2026-06-23.md`
- `oq-rk2-aps-fc3-fc4-closure-2026-06-23.md`
- `oq-rk2-fc4-k3-holonomy-rank-2026-06-23.md`

Adjacent OQ3b/OQ3c and topological-index files were checked only to align terminology:
`oq3b-rs-index-closed`, `oq3b-rs-index-8`, `oq3b-tau-correction-closure`,
`oq3c-index-additivity`, `oq3c-cross-term-cancellation`,
`ind-top-x4-atiyah-singer`, and `ind-top-eta-s3-aps`.

The strict reading is the previous wave's reading: OQ-RK1/OQ-RK2 do not contain a
non-circular computation of the RS analytic index. They provide useful raw ranks, projector
language, APS scaffolding, and failure conditions, but the symbol class itself is still missing.

## The Object To Compute

Let `M = K3` be the compact Riemannian K3 used in the APS/Atiyah-Singer route. Let
`F = S(6,4)` be the internal GU spinor coefficient bundle after section pullback. The contract
must compute the index of the constrained/gauge-fixed RS operator on `M`:

```
D_RS^gf : Gamma(E_RS^+) -> Gamma(E_RS^-)
```

where `E_RS^pm` are not allowed to be prose names. They must be constructed from explicit
Clifford, projector, and gauge data. The minimum acceptable symbol-level description is:

```
V_+ = T*M tensor S_4^+ tensor F
V_- = T*M tensor S_4^- tensor F

G_+ : V_+ -> S_4^- tensor F          gamma-trace
G_- : V_- -> S_4^+ tensor F          gamma-trace

P_+ : V_+ -> ker(G_+)                gamma-trace projector
P_- : V_- -> ker(G_-)                gamma-trace projector

g_+ : S_4^+ tensor F -> V_+          gauge symbol, epsilon |-> xi tensor epsilon
g_- : S_4^- tensor F -> V_-          opposite chirality gauge symbol, if used

sigma_RS_raw(xi) = P_- (c(xi) tensor 1_F) P_+
```

The raw symbol is not enough if the raw projected vector-spinor operator is not elliptic. The
contract must include one of the following:

1. A gauge-fixed elliptic operator symbol `sigma_RS^gf(xi)` including gauge-fixing blocks.
2. An elliptic RS complex with ghost/subtraction terms and a K-theory class for the complex.

The output must be a K-theory symbol class, for example:

```
[sigma_RS^gf] in K^0_c(T*M)
```

or an equivalent elliptic-complex class. Merely printing raw ranks such as `416`, `96`, `64`,
or `24` does not decide the generation count.

## Exact Inputs

### Topological Inputs

These are fixed and may be hard-coded:

```
Ahat(K3) = 2
chi(K3) = 24
sigma(K3) = -16
p1(TK3)[K3] = 3*sigma = -48
b0 = 1
b2_plus = 3
b2_minus = 19
b4 = 1
```

Required checks:

```
Ahat(K3) = -sigma/8 = 2
p1 = 3*sigma = -48
chi = b0 + b2_plus + b2_minus + b4 = 24
sigma = b2_plus - b2_minus = -16
```

These checks are sanity checks only. They do not compute the RS index.

### Clifford Inputs

The implementation must provide either exact matrices or a symbolic Clifford algebra object
for the K3 base Clifford action:

```
gamma_i gamma_j + gamma_j gamma_i = 2 delta_ij Id,       i,j = 1..4
sigma_4 = gamma_1 gamma_2 gamma_3 gamma_4
sigma_4^2 = +Id
```

It must also provide the right-H structure or an explicitly stated complex-to-H conversion:

```
J^2 = -Id
J commutes with every gamma_i used in the H-linear operator
index_H = index_C / 2      only after the quaternionic structure is verified
```

A full `Cl(9,5)` model may be included for consistency with the GU ambient story. If it is
included, it must verify:

```
omega_9,5^2 = +Id
rank_H(S^+) = rank_H(S^-) = 32
rank_H(ker Gamma^14D | S^+) = 416
```

Those are ambient checks. They still do not decide the K3 RS index.

### Bundle Inputs

The contract must explicitly state the internal coefficient bundle:

```
F = S(6,4)
rank_C(F) = 16
rank_H(F) = 8, if the H-structure is verified
```

The implementation must not silently assume `F` is flat. It must choose one of:

```
flat_F = true, with a proof or explicit trivial connection
```

or

```
ch_2(F)[K3] = symbolic variable or explicit integer
```

If the output depends on `ch_2(F)[K3]`, the gate remains open until the physical Sp(64) /
section-pullback background is fixed.

### Projector Inputs

The implementation must construct:

```
G_+, G_-
P_+, P_-
```

and verify:

```
P_+^2 = P_+
P_-^2 = P_-
G_+ P_+ = 0
G_- P_- = 0
rank(P_+), rank(P_-) printed with units: C-rank and/or H-rank
```

If `P_pm` are orthogonal projectors, the inner product used to construct the adjoints must be
specified. If the projectors are algebraic idempotents but not orthogonal, the Fredholm/APS
domain proof must say why this is sufficient.

### Gauge Inputs

The gauge choice must be explicit. The contract must state one of:

```
computed_object = raw gamma-trace-free vector-spinor operator
```

or

```
computed_object = gauge-fixed physical RS operator
gauge_condition = ...
ghost_or_subtraction_complex = ...
```

For the gauge-fixed route, the symbol class must include the ghost/subtraction contribution.
An acceptable schematic form is:

```
[sigma_RS^gf] =
    [sigma(raw gamma-trace-free vector-spinor)]
  - [sigma(gauge ghost)]
  + [sigma(gauge-fixing block)]
```

but the actual implementation must define the bundles and maps. Omitting gauge data while
claiming to compute the physical constrained RS index invalidates the result.

### Boundary Inputs, If APS Is Used

Closed K3 needs Atiyah-Singer only and has no boundary correction. If the implementation uses
K3 with a collar or K3 minus a ball, it must also provide:

```
A_RS = boundary operator
C_RS = APS/Calderon projector
eta(A_RS)
h(A_RS) = dim ker(A_RS)
```

and the final formula must be:

```
index = bulk_index - (eta(A_RS) + h(A_RS))/2
```

The earlier `eta=0` S^3 arguments can be used as checks only if the boundary operator is the
same projected/gauge-fixed RS boundary operator, not merely the flat spin-1/2 boundary Dirac.

## Exact Outputs

The executable gate must print or serialize the following outputs.

### Algebra Sanity Outputs

```
clifford_relations_ok: true/false
sigma_4_squared: +1 or failure certificate
right_H_structure_ok: true/false
raw_gamma_trace_ranks:
  full_14d_chiral: optional, expected 416 if modeled
  pulled_back_4d_reducible_pre_gauge: optional, expected 96 if that model is used
  spin4_irreducible_refinement: optional, expected 24 if that model is used
```

The report must label these as raw ranks. They are not Candidate A/B decisions.

### Symbol Outputs

```
symbol_class_constructed: true/false
computed_object: raw | gauge_fixed | elliptic_complex
elliptic: true/false
ellipticity_certificate:
  exact determinant/rank polynomial, or exact theorem reference encoded as a named assumption
missing_symbol_data:
  list of missing Clifford/projector/gauge inputs, if any
```

If `elliptic=false`, the APS/Atiyah-Singer route fails as currently stated.

### Characteristic-Class Outputs

```
ch_symbol = explicit degree-0 and degree-4 components
bulk_index_C = integer or symbolic expression
H_structure_verified = true/false
bulk_index_H = bulk_index_C / 2, only if H_structure_verified
eta = integer/rational/symbolic, if APS boundary used
h = integer, if APS boundary used
index_H = final H-linear index, or symbolic expression
depends_on_ch2_F: true/false
```

The characteristic-class expression must expose every normalization. In dimension 4:

```
index_C = < Ahat_4 * ch_0(symbol) + Ahat_0 * ch_2(symbol), [K3] >
```

where `Ahat_4[K3] = 2`. If the computation reduces to `2 * rank` only because `ch_2=0`,
then the proof of `ch_2=0` must be present.

### Decision Outputs

The decision engine must output one of:

```
OPEN_MISSING_SYMBOL_DATA
INVALID_CIRCULAR
NON_ELLIPTIC
OPEN_BACKGROUND_DEPENDENT
COMPLEX_ONLY_H_STRUCTURE_MISSING
CANDIDATE_A
CANDIDATE_B
OTHER_INDEX
```

The output must include the computed final expression and the rule that fired.

## Decision Rules

Let `I = ind_H(D_RS)` be the final independently computed H-linear index.

### Preliminary Rules

1. If the computation uses any forbidden target as input, output:

```
INVALID_CIRCULAR
```

2. If Clifford, projector, gauge, or symbol-class data are missing, output:

```
OPEN_MISSING_SYMBOL_DATA
```

3. If the H-structure or complex-to-H conversion is missing, output:

```
COMPLEX_ONLY_H_STRUCTURE_MISSING
```

and report only `index_C`.

4. If the gauge-fixed symbol or elliptic complex is not elliptic, output:

```
NON_ELLIPTIC
```

5. If the final index depends on an unspecified Chern character or background gauge class,
output:

```
OPEN_BACKGROUND_DEPENDENT
```

and keep the symbolic formula.

### Candidate Rules

Only after all preliminary rules pass:

```
I = 8:
  CANDIDATE_A
  rank_eff_report = I / Ahat(K3) = 4
  total_index_if_spin_half_16_and_additivity = 24
  generation_count_if_8_H_lines_per_generation = 3
```

```
I = 16:
  CANDIDATE_B
  rank_eff_report = I / Ahat(K3) = 8
  total_index_if_spin_half_16_and_additivity = 32
  generation_count_if_8_H_lines_per_generation = 4
```

```
I not in {8, 16}:
  OTHER_INDEX
  total_index_if_spin_half_16_and_additivity = 16 + I
  generation_count_if_8_H_lines_per_generation = (16 + I) / 8
```

If `(16 + I)` is not divisible by `8`, the output must say the current SM-generation
normalization does not yield an integral generation count.

### Boundary Rule

If APS boundary data are used:

```
I = bulk_index_H - (eta + h)/2
```

Then apply the same Candidate A/B/other rules. A nonzero eta or kernel term is not an
automatic failure; it is part of the computed index. It is a failure only if it is assumed
away without computing it for the projected/gauge-fixed RS boundary operator.

## Circularity Guard

The following are forbidden as inputs:

```
ind_H(D_RS) = 8
rank_H(E_RS^eff) = 4
total ind_H(D_GU) = 24
three generations
rank_eff = ind_H(D_RS) / Ahat(K3) when ind_H(D_RS) came from physical generation counting
normalization factors chosen after observing the target value
physical DOF count treated as an analytic index theorem
```

Allowed comparisons after the independent computation:

```
compare I with 8 and 16
report rank_eff = I / 2 as a derived readout
report total = 16 + I, conditional on the existing spin-1/2 and additivity gates
```

Forbidden shortcut examples:

```
8 / Ahat(K3) = 4, therefore ind_H(D_RS) = 8
physical RS chiral half has H-rank 8, therefore analytic index is 8
raw gamma-trace rank 24/96/416 reduces by an unstated normalization to 4
choose a topological expression such as b2_plus + b0 because it equals 4
```

This guard is the main advance over the older OQ-RK attempts.

## Minimal Executable Skeleton

The optional executable skeleton is `tests/rs_symbol_index_contract.py`.

Run it with:

```
python tests/rs_symbol_index_contract.py
```

What it currently checks:

- K3 invariant arithmetic: `Ahat=2`, `p1=3*sigma=-48`, `chi=24`, `sigma=-16`.
- Raw-rank sanity labels: `416`, `96`, and `24` are recorded as raw ranks and are not
  accepted as Candidate A/B evidence.
- Decision-rule behavior for Candidate A, Candidate B, other index values, missing data,
  non-ellipticity, missing H-structure, background dependence, and circular-input invalidation.

What it explicitly does not verify:

- No explicit `Cl(4,0)` or `Cl(9,5)` gamma matrices are present.
- No projectors `P_+`, `P_-` are constructed.
- No gauge-fixed RS symbol or elliptic complex is constructed.
- No K-theory symbol class is computed.
- No Atiyah-Singer or APS RS index is evaluated.

The skeleton's real Clifford/projector/index tests are marked skipped. Passing the skeleton is
therefore a check of the contract logic only, not evidence for Candidate A or Candidate B.

## Acceptance Criteria For A Future Worker

A future worker may claim the gate has advanced past this contract only if they supply an
artifact that:

1. Provides the Clifford, H-structure, projector, gauge, and bundle data named above.
2. Constructs `sigma_RS^gf` or an elliptic RS complex and prints an ellipticity certificate.
3. Computes the K-theory symbol class and characteristic-class formula before comparing with
   `8` or `16`.
4. Carries or proves away all `ch_2(F)` and RS-bundle Chern-character terms.
5. Does not use any forbidden target as input.
6. Emits one of the decision statuses above.

Until then, the correct verdict is:

```
generation count RS analytic index gate: OPEN
contract status: specified and executable as a skeleton
```

