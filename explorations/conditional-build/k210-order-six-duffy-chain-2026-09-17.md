---
title: "K210 order-six exact Duffy chart and fourth-derivative chain"
document_role: active_research
doc_type: conditional_native_K139_K210_order_six_duffy_derivative_chain
created: 2026-09-17
date: 2026-09-17
claim_ceiling: exact common and term-specific Dirichlet stick densities and fourth-order multivariate composition for a smooth interior quotient; no complete signed derivative enclosure, accurate order-six prefix or physical/source result
manifest: lab/process/k210-order-six-duffy-chain.json
solver: tests/channel-swings/k210_order_six_duffy_chain.py
probe: tests/channel-swings/k210_order_six_duffy_chain_probe.py
target_claim: INTERNAL_TARGET:K203_K208_DUFFY_CHAIN_INTERFACE
target_claim_verdict: EXACT_CHART_AND_FOURTH_COMPOSITION__SIGNED_CELL_REMAINDER_OPEN
canon_verdict_change: none
---

# K210 Duffy chart and mixed derivative chain

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY. This is K139/K184's repository-owned
conditional `C3` Fock calculation (`lambda=256`, equal couplings one), not a
source-selected action, physical extension, state, domain or polarization.
The carrier is the hard-core impurity tensor positive particle/hole Fock
space; the pairing is its positive Hilbert pairing for the complete signed
time-Gram output, not SC-META-53's unresolved physical quotient. CAR adjoint
and the real interior Bessel kernels supply the real structure. The grading
retains eighteen coherent signed groups, 234 native entries and 1,864
Leibniz support terms. No change to the operator or signed target is made.

## Exact chart and measures

For thirteen sticks `0<u_j<1`, set `z_j=u_j prod_(i<j)(1-u_i)` for
`j=1,...,13`, and `z_14=prod_(i<=13)(1-u_i)`. The first thirteen
coordinates have a lower-triangular Jacobian, so its positive determinant is
`prod_(j=1)^13 (1-u_j)^(13-j)`. A Dirichlet vector with positive parameters
`beta_1,...,beta_14` consequently has independent beta sticks

```text
u_j ~ Beta(beta_j, sum_(k>j) beta_k),  j=1,...,13.
```

This follows by collecting the powers of each `u_j` and `(1-u_j)` in
`prod z_k^(beta_k-1)` times that Jacobian; no numerical normalization is
substituted. K202's **common** reference has fourteen parameters `1/3`, total
`14/3`; K185's 1,276 **term-specific** allocations have parameters
`1-alpha_i>=1/3`, total **six**. They share the chart, not a Dirichlet law.
The radial Gamma-shape-six factor is separate from both angular totals.
The exact common-stick exponents appear in the manifest. In particular the
last stick has `(u_13)^(-2/3)(1-u_13)^(-2/3)`; all chart weights are
integrable. K185/K188's termwise quotient face/tail bounds cannot be replaced
by K204/K209's common-reference lost mass.

## Full fourth-order chain, not a derivative enclosure

For labelled derivative slots `i_1,...,i_m`, `m<=4`, and an interior smooth
signed quotient `f` on the affine simplex (derivatives tangent to that
simplex), the multivariate chain is

```text
partial_(i_1)...partial_(i_m)(f o z)
 = sum_(set partitions pi of {1,...,m})
     D^|pi|f(z)[partial_(i_B)z : B in pi].
```

The stick chart is multiaffine, so `partial_(i_B)z=0` if a block repeats any
stick index. At order four the numbers of labelled partitions with one,
two, three and four blocks are `1,7,6,1`. In particular a **mixed** fourth
chart derivative generally needs ambient signed `D^1 f`, `D^2 f`, `D^3 f`
and `D^4 f`, not only `D^4 f`. Conversely for four repeats of one stick,
only the four-singleton partition survives: the chart is affine in that
variable and its pure fourth derivative is just `D^4f[(partial_i z)^4]`.

The chart is the distribution of the first success among thirteen Bernoulli
sticks (with the residual event as coordinate fourteen). Differentiating
`r` distinct Bernoulli factors gives a signed product measure of total
variation at most `2^r`; its deterministic pushforward to `z` cannot
increase total variation. Therefore `||partial_B z||_2<=2^|B|` globally,
including chart limits. If `M_k=sup ||D^k f||_2` on the *actual chart-cell
image*, the set-partition formula gives the proof-safe fourth mixed bound
`16(M_1+7M_2+6M_3+M_4)`. For a pure fourth stick derivative, the first
derivative vector is `P(e_i-tail_distribution)`, `0<=P<=1`, hence its
Euclidean norm is at most `sqrt(2)` and the sharper bound is `4 M_4`.
The core preimage is not the whole stick cube: a proposed cell must have its
image inside the positive angular core before substituting core-only `M_k`.
These conservative chart inequalities do not establish any `M_k` for the
complete normalized/coalescent K184 quotient or a useful error allocation.

## Independent control and consequence

The producer checks all 1,276 term-specific beta parameters and exact
finite set partitions, and evaluates five rational fourth partials of a
four-term test polynomial. The independent probe does not import the
producer: it substitutes labelled nilpotent perturbations directly into the
stick chart and extracts the squarefree degree-four coefficient, checks the
densities separately, and catches six hostile manifest changes. This tests
the composition formula on polynomial controls, not the nonpolynomial signed
K184 derivative or novelty. K203's cheaper third-order/28-node and K208's
fourth-order/184-node routes both remain candidates; K209's ambient centered
Taylor coefficient `<0.002930` needs its own uniform ambient fourth bound,
not this generic mixed-chart coefficient. The next calculation should enclose
the complete signed normalized/coalescent jets through the selected order
on core-contained cells, with K185/K188 boundaries and coherent-group
allocation separately composed. The inherited full-domain absolute error
remains `<9.683e-7`; no accurate prefix, K171/K168 action/residual/floor,
K152, source, physics, canon, prediction or confirmation result follows.

Run the solver and independent probe with `_local/cas-venv/bin/python` on
the two `tests/channel-swings/k210_order_six_duffy_chain*.py` files.
