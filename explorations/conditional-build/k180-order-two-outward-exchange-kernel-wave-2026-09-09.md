---
title: "K180 order-two outward exchange-kernel wave"
document_role: active_research
doc_type: conditional_native_K139_K180_order_two_exchange_kernel_outward_result
created: 2026-09-09
date: 2026-09-09
claim_ceiling: exact repository-owned analytic reduction and certified outward numerical enclosure for all six K179 order-two exchange kernels on the fixed K139--K179 equal-coupling two-edge positive particle/hole point control; every term is one signed copy of a common positive rank-one-species kernel, whose squared norm lies in [6.15966310411619e-8,7.83634164688456e-8], and a same-family midpoint compression lies inside that interval with explicit L2 error; no nontrivial repeated-species determinant above order two, complete action column, residual, complement or flux floor, scalar-center floor, K152 interval, physical/source selection, Born derivation, prediction or confirmation is evaluated
manifest: lab/process/k180-order-two-outward-exchange-kernel-wave.json
solver: tests/channel-swings/k180_order_two_outward_exchange_kernel.py
probe: tests/channel-swings/k180_order_two_outward_exchange_kernel_probe.py
target_claim: INTERNAL_TARGET:K179_ORDER_TWO_DETERMINANT_OUTWARD_GATE
target_claim_verdict: SIX_KERNELS_EVALUATED__OUTWARD_NORM_AND_CONFORMING_ERROR_CERTIFIED__HIGHER_DETERMINANT_GATE_OPEN
canon_verdict_change: none
---

# K180 order-two outward exchange-kernel wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: the fixed K139/K156 hard-core `C3` impurity coupled to four
particle/hole bath species on `L2(R)`, auxiliary chart `lambda=256`, equal
couplings one, and the three normalized K162 zero-bath seed orbits. K180
consumes K179's exact coefficient family without changing the operator,
extension, state, polarization, domain or scalar center.

```gu-typed-objects
result: all six K179 order-two older-letter exchange terms are signed orthogonal copies of one positive two-variable continuum kernel; exact contracted-momentum reduction, monotone dyadic rectangles and an analytic infinite-tail majorant certify its norm, while a same-family piecewise-constant compression carries an explicit L2 error
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space Gamma_-(L2(R;C4)), in q=(0,0),(1,0),(0,1), with the fixed K139 chart and normalized K162 zero-bath seed lines LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive physical Fock Hilbert pairing on the order-two output sector; K179's normalized specieswise exterior convention makes the two output signatures per seed orthogonal ON=repository_signed_point_control
real_structure: CAR adjoint, momentum reflection, Hermitian matched finite-cutoff normal ordering and real positive continuum kernel
grading: conserved incidence charges, hard-core impurity state, bath species, bath number two, K179 path and contraction identity, ordered momentum provenance and specieswise exterior parity
action_owner: repository-construction -- K139 fixes C and G, K156 fixes W=(E_R-256)I-X, and K179 fixes the coefficient-complete six-term order-two family; no source/GU action selects the physical extension, state, domain, polarization or scalar center
target: close the first K179 numerical gate and identify the first genuinely nontrivial determinant successor without claiming the through-order-twelve action column MAP-TYPE=intertwiner
```

## Inline preflight bookend

K179 leaves six signed order-two output kernels. Retrieval against its
canonical generator shows a symmetry stronger than the handoff wording: all
six have the same unsigned scalar kernel, and the two outputs attached to each
seed have different species signatures. Their cross terms therefore vanish in
the Fock pairing. The K177 determinant is only `1x1` in every species at this
order; there is no coincident-face determinant subtraction to lose yet.

The route census compared a direct three-variable cubature, Laplace-simplex
Bessel quadrature, exact contracted-momentum reduction, finite K162
compression and entrywise determinant intervals. The selected route integrates
the contracted momentum exactly, then encloses the remaining common kernel by
monotone rectangles. A separate piecewise-constant compression is conforming
to that same continuum family and carries a cellwise error. This closes order
two without pretending its rank-one determinant structure implements the
higher-order antisymmetric gate.

The source register and v0.263 physics ledger do not move. `SC-META-53`
remains `UNCERTAIN`; `LT-SM8`, `RA-F1` and `AC-F1` remain `NEEDS`.

#### 1. Exact contracted-momentum reduction

Put

```text
E_j=sqrt(1+p_j^2),
D_1=256+E_1,
D_2=256+E_1+E_2,
D_3=256+E_1+E_2+E_3.                         (1)
```

K179's common unsigned order-two kernel before its `(2*pi)^-2` point
normalization is

```text
K(p_2,p_3)=int_R dp_1/(D_1 D_2 D_3).          (2)
```

For `a>1`, define

```text
F(a)=a acosh(a)/sqrt(a^2-1),
J(a,b)=2 [F(b)-F(a)]/(b-a).                    (3)
```

The substitution `p=sinh(x)` and cancellation of the common divergent
constant give

```text
J(a,b)=int_R dp/[(sqrt(1+p^2)+a)(sqrt(1+p^2)+b)]. (4)
```

Partial fractions only between complete positive factors now give the stable
second divided difference

```text
K(p_2,p_3)=
 [J(256,256+E_2)-J(256,256+E_2+E_3)]/E_3.     (5)
```

Equation (2), not cancellation-prone individual heat-kernel entries, proves
that `K` is positive and decreases separately in `|p_2|` and `|p_3|`.

## 2. Finite-domain outward enclosure

The certificate partitions each positive momentum axis from zero to `2^40`
into six equal cells on `[0,1]` and six equal cells on every dyadic octave.
This gives `60,516` positive-quadrant rectangles. On each rectangle,
coordinate monotonicity puts `K` between its upper-left and lower-right corner
values. The implementation evaluates (5) at 50 decimal digits and enlarges
each value by `max(10^-30 |K|,10^-45)`, far above the accumulated correctly
rounded square-root/logarithm operation ulps.

The raw positive-quadrant squared-integral enclosure is

```text
2.4000287361905616e-5
 <= int_[0,2^40]^2 K(p_2,p_3)^2 dp_2 dp_3
 <= 3.0514610466044448e-5.                     (6)
```

Three independent one-dimensional monotone `p_1` sums, including their own
analytic tails, enclose the closed form at `(0,0)`, `(1,2)` and `(100,100)`.
They do not call the divided-difference identity to obtain their bounds.

## 3. Analytic infinite complement

Let `A=256+E_1`. Weighted AM--GM on `D_2=A+E_2` with weight `1/8` on `A`,
and on `D_3=A+E_2+E_3` with weights `(1/64,1/16,59/64)`, yields after dropping
weight products smaller than one

```text
K(p_2,p_3)
 <= (64/9) E_2^(-15/16) E_3^(-59/64).         (7)
```

Indeed the remaining `A` exponent is `73/64`, and

```text
int_R (256+|p|)^(-73/64) dp
 = 2(64/9)256^(-9/64) < 64/9.                 (8)
```

Using `E(p)>=1` on `[0,1]` and `E(p)>=p` after one gives the rational total and
tail bounds

```text
int_0^inf E^(-15/8) dp <= 15/7,
int_0^inf E^(-59/32) dp <= 59/27,
int_(2^40)^inf E^(-15/8) dp <= (8/7)2^-35,
int_(2^40)^inf E^(-59/32) dp <= (32/27)2^-33. (9)
```

The union bound over all four quadrants is
`7.450483260969855e-8` before point normalization. Combining (6)--(9) and
`g=(2*pi)^-2 K` gives the certified single-term result

```text
6.159663104116194e-8 <= ||g||_2^2 <= 7.836341646884551e-8,
2.481866858660269e-4 <= ||g||_2 <= 2.799346646431012e-4. (10)
```

## 4. Same-family conforming compression

On every dyadic rectangle let `g_h` be the constant value of the exact common
kernel at the cell midpoint, with zero continuation beyond the finite box.
This is a same-family finite-dimensional `L2` vector, not a rebuilt cutoff
Hamiltonian. Its squared norm is

```text
||g_h||_2^2=6.918623720176071e-8,               (11)
```

inside (10). If `L_C` and `U_C` are the monotone endpoint bounds on cell `C`,
then

```text
||g-g_h||_2^2
 <= (2*pi)^-4 [4 sum_C |C|(U_C-L_C)^2 + tail]
```

gives

```text
||g-g_h||_2 <= 3.472607606064087e-5.            (12)
```

Thus the independent finite compression agrees with the outward continuum
enclosure and has a proved approximation error; agreement is not inferred
from decimal coincidence.

## 5. Six-term reconstruction and the scale switch

K179's coefficients are `(+,+)` on the vacuum seed and `(-,-)` on each
one-impurity seed. Those signs remain part of the action coordinates. Within
each seed the two outputs have different species signatures, so the squared
exchange-vector norm is exactly `2||g||_2^2` and

```text
3.509889771521663e-4 <= ||X_ex,2 G^2 phi_seed||
                     <= 3.958873993166378e-4.   (13)
```

The determinant-aware scale replay finds the first honest switch immediately
after this gate. None of the six order-two terms repeats an output species.
At order three, four of the eight terms do, so their scalar products require
signed `2x2` heat-kernel determinants. From order five onward every term has a
repeated species. The rank-one order-two evaluator therefore cannot be copied
through order twelve without violating the cancellation requirement.

The next gate is the complete grouped order-three family: evaluate the four
repeated-species terms as whole `2x2` determinants while retaining the four
rank-one terms in the same path-pair basis. Only after that mixed control
agrees should the determinant-simplex engine scale further and feed K171.

## Hostile result review

- **Strongest overclaim:** “K180 evaluates the exchange prefix through order
  twelve.” Refused. It closes exactly order two and proves why order three is
  a new determinant problem.
- **Strongest cancellation attack:** the order-two signs appear to cancel.
  They do not: differently signed terms live on different seed inputs, and
  the two terms within each seed occupy orthogonal species outputs.
- **Strongest numerical attack:** the finite dyadic box omits a slowly
  decaying tail. Equation (7) encloses the complete complement; it is not
  estimated from the last sampled cells.
- **Strongest normalization attack:** omit the four momentum-reflection
  quadrants or one `(2*pi)^-2` point factor. Equations (6)--(10) record both
  explicitly, and the seed norm doubles only after the single-term result.
- **Weakest remaining seam:** higher orders contain same-species determinants
  with coincident-face cancellation. K180 supplies no interval rule for those
  determinants and makes no action-column claim.

## Inline postflight bookend

The K179 first numerical gate closes. All six exact order-two kernels reduce
to one positive continuum function, whose norm and each seedwise two-copy
vector now have outward enclosures. A conforming piecewise-constant vector
agrees inside the enclosure with a proved `L2` error, and direct contracted-
momentum sums check the analytic reduction at three scales.

The attempted through-order-twelve release stops honestly at the first changed
mathematical object: four of the eight order-three terms need nontrivial `2x2`
determinants. The next work is a grouped determinant-simplex order-three
certificate, not a larger rank-one cubature. The complete K171/K168 action
columns, `R_ref` residual, complement or flux floor, scalar-center floor and
K152 interval remain open. Source, ledger, canon, paper, release and public
posture remain unchanged.

## Reproduction

```bash
python3 tests/channel-swings/k180_order_two_outward_exchange_kernel.py --demo
python3 tests/channel-swings/k180_order_two_outward_exchange_kernel.py --quick
python3 tests/channel-swings/k180_order_two_outward_exchange_kernel_probe.py
python3 tests/channel-swings/k180_order_two_outward_exchange_kernel_probe.py --selftest
```

Expected: the full evaluator reproduces the outward and compression
certificates; the probe passes all exact/reporting controls and catches every
hostile scope, determinant, interval and release mutation.
