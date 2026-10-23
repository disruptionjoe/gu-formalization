---
title: "K1983: Certified continuum evaluation of the optimal pulse iteration"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1983_certified_continuum_pulse_evaluation.py
  - tests/channel-swings/k1983_certified_continuum_pulse_evaluation_probe.py
---

# K1983: Certified continuum evaluation of the optimal pulse iteration

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: exact early-iterate formulas, whole-strip computable error and actual optimal-phase enclosures
carrier: width9 strip D with u in[-3,3], u<=z<=u+9 LAYER=toy CHIRALITY=N/A
pairing: normalized row and column averages and real L2 area norm ON=characteristic_strip
real_structure: real bounded pulses and algebraically specified odd phase
grading: characteristic directions only
action_owner: repository-construction -- fixed scalar model and minimum-norm selection
target: reproducible continuum integral evaluation with certified amplitude and error MAP-TYPE=intertwiner
```

## 1. Actual continuum object, not a finite test marginal

Use [K1980](k1980-constructive-minimum-norm-pulse-2026-10-23.md)'s EXACT
operators P,Q on D, M=23/100, forcing g(u)=2phi_star(u)/9, a=2+epsilon>2,
and v_0=0. The phase is the algebraic optimum established in
[K1974](k1974-scalar-excursion-separation-2026-10-23.md). This result supplies
an implemented, rational evaluator of continuum iterates, including a uniform
error bound valid at ANY point of the strip. It does not make a finite iterate
exactly feasible or certify its phase energy.

Let A(z)=Qg(z), the mean of g on
[max(-3,z-9),min(3,z)]. At the two zero-length tips use the continuous
endpoint value g. Direct application of the projections gives

    v_1=g/a,
    v_2=((a+1)g-A)/a^2,
    v_3=clip_[-M,M](((a^2+a+1)g+PA-(a+2)A)/a^3).         (1)

The first two formulas need NO clipping: |g|<=2/9 and
|v_2|<=2(a+2)/(9a^2)<=2/9<M for a>=2. The v3 formula follows from
Pv2=((a+1)g-PA)/a^2 and Qv2=A/a; clipping remains explicit.
Thus computing the first genuinely clip-capable iterate requires only one
one-dimensional integral of A, not a nested two-dimensional discretization.

## 2. Algebraic phase enclosure and shrinking-column control

The code isolates the unique K1969 quartic root t by exact rational bisection.
It encloses lambda=D(t)/K(t) by rational interval arithmetic. With rational
midpoints t_hat,lambda_hat, use K1969's piecewise polynomial phase formula
exactly at those midpoints. The phase kernel has |kernel|<=1/2 and is
1-Lipschitz in t, including across its moving join. Since lambda<7/100,
if the interval widths are w_t,w_lambda, then

    |g-g_hat| <= d_g=(2/9)(w_lambda/4+7w_t/200).           (2)

The default96 bisections give d_g<10^-27. `configure(bits)` permits further
refinement; the128-bit control verifies shrinkage before restoring the default.
No floating-point root is part of the certificate.

Both the exact phase and its rational surrogate are207/200-Lipschitz.
Therefore g and g_hat are G=23/100-Lipschitz. A normalized moving-interval
average does not blow up at zero length: write it as
integral_0^1 g(l(z)+s(r(z)-l(z))) ds. Both endpoint slopes lie in[0,1],
so A is also G-Lipschitz, including its continuous tip extensions. This
removes the apparent singularity caused by dividing by the column length.

The integral of g_hat is a rational polynomial antiderivative on each piece.
Hence A_hat(z) is evaluated exactly at rational z. A composite midpoint mean
on an interval of length L and a G-Lipschitz integrand has error at most
GL/(4N): integrate G times the distance to each cell midpoint. For PA, L=9.
Clipping is1-Lipschitz, so the implemented third iterate has the uniform bound

    |v3_hat-v3| <= ((a^2+2a+4)d_g+9G/(4N))/a^3.           (3)

This is a whole-strip bound, not an estimate inferred from adjacent grids.
The report contains18 actual phi_star point enclosures for three epsilon
values and128 midpoints, checked against256-midpoint refinements. The
endpoints, asymmetric columns, reflection and amplitude are exercised.
The enclosures bound a finite v3, not the limiting optimal pulse.

## 3. Executed general evaluator and constructive convergence consumer

For any finite k, the code also evaluates the original iteration recursively,
using normalized midpoint means and clipping. If exact v_k has separate
coordinate Lipschitz constants U_k,Z_k, then

    U_0=Z_0=0,
    U_(k+1)=(3U_k+Z_k+G)/a,
    Z_(k+1)=(U_k+3Z_k)/a.                               (4)

P moves the row interval with u; Q moves its column endpoints with z.
Their derivative bounds are respectively U+Z and U+Z. Formula(4) follows
by the triangle inequality and nonexpansive clipping. For k>=4 the uniform
arithmetic/quadrature error obeys

    e_k <= [4e_(k-1)+(9Z_(k-1)+6U_(k-1))/(4N)+d_g]/a,    (5)

starting from(2)-(3). Row width is9 and column width is at most6. The
script executes a coarse k4 example as an implementation control; its large
error bound is recorded honestly, not advertised as accurate pulse data.
All returned approximations obey |v|<=M. Reflection is preserved.

For any fixed k, increase root precision and N until(5) is below a requested
positive tolerance. This terminates because all constants are explicit and
finite, d_g tends to0 and the midpoint terms tend to0. The cost can grow
exponentially with k; this is a correctness construction, not an efficient
large-iteration solver or a claim it was executed at asymptotic k.

Combine with K1980's epsilon_n=1/n^2 and prescribed k_n satisfying
(2/(2+epsilon_n))^k_n<=1/n^2. Evaluate the resulting function to uniform
error<=1/n^2; its L2 error is at most sqrt(54)/n^2. K1980's proved strong
convergence then gives a fully specified computable sequence converging to
the unique minimum-L2 optimal measurable pulse. This removes the missing
certified integral-evaluation procedure, while leaving an effective strong
error-to-limit modulus and practical high-accuracy construction open.
Neither uniform error to a FINITE iterate nor marginal L2 convergence gives
exact plateaux, H1/Dirichlet-energy convergence or smooth optimal attainment.

## 4. Independent checks and remaining boundaries

A separate implementation verifies the polynomial joins and derivative bounds,
the symbolic projection identity(1), and18 continuum reference integrals at
60-digit precision. Its31 mixed controls distinguish exact algebra/derivative
checks from numerical spotchecks. Four actual forcing/column-sign/column-length/
step perturbations fail the continuum comparison after the baseline. The
numerical reference is a bug detector; the proof of(2)-(5) certifies the error.
No numerical agreement is promoted to a continuum theorem.

Strongest overclaim: certified v3 samples called an exactly feasible optimal
pulse. Strongest contrary issue: shrinking columns; normalized parameterization
settles their continuity and Lipschitz bound. Weakest remaining practical seam:
recursive cost and no effective modulus to v_dagger. A faster adaptive solver,
a closed formula, or smooth exact-marginal approximation is separate work.
K1977's no-C1-attainment theorem survives. This is independent scalar
mathematics; SC-META-53 remains UNCERTAIN and source/ledger/canon are unchanged.
