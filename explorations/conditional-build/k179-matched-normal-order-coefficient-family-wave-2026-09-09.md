---
title: "K179 matched normal-order coefficient-family wave"
document_role: active_research
doc_type: conditional_native_K139_K179_coefficient_complete_matched_exchange_family_result
created: 2026-09-09
date: 2026-09-09
claim_ceiling: exact repository-owned coefficient-family theorem for the K139--K178 equal-coupling two-edge positive particle/hole point control; the fixed K156 matched finite-cutoff normal order determines all 2,958 surviving exchange terms through order twelve, including the operator monomial, Neumann and W signs, contracted-resolvent incidence, output kernel and normalized exterior projection, and an independent finite CAR action checks all six order-two terms; the resulting family passes K178 numerical admission, but no determinant integral, complete action column, residual, complement or flux floor, scalar-center floor, K152 interval, physical/source selection, Born derivation, prediction or confirmation is evaluated
manifest: lab/process/k179-matched-normal-order-coefficient-family-wave.json
solver: tests/channel-swings/k179_matched_normal_order_coefficient_family.py
probe: tests/channel-swings/k179_matched_normal_order_coefficient_family_probe.py
target_claim: INTERNAL_TARGET:K178_MISSING_K156_COEFFICIENT_FAMILY
target_claim_verdict: COEFFICIENT_FAMILY_SERIALIZED__ORDER_TWO_DIRECT_CAR_CHECKED__NUMERICAL_ADMISSION_OPENED
canon_verdict_change: none
---

# K179 matched normal-order coefficient-family wave

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
couplings one, and the three normalized K162 zero-bath seed orbits. This packet
derives the missing coefficient family from that supplied operator. It neither
changes the operator nor chooses a physical extension, state, polarization,
domain or scalar center.

```gu-typed-objects
result: K156's finite-cutoff matched normal order determines a coefficient-complete generator for every K178 older-letter contraction through order twelve; each generated term names the impurity/bath monomial, exact Neumann and W signs, all contracted-energy denominator incidence, integrated output kernel and normalized specieswise exterior projection, and all six order-two terms agree with direct finite CAR action
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space Gamma_-(L2(R;C4)), in q=(0,0),(1,0),(0,1), with the fixed K139 chart and normalized K162 zero-bath seed lines LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive physical Fock Hilbert pairing transported by S=(1-G_256)^-1 to M=S* S; ordered kernels are projected into the normalized specieswise exterior convention before determinant inner products ON=repository_signed_point_control
real_structure: CAR adjoint, momentum conjugation, Hermitian matched finite-cutoff normal ordering and the K168 real flavor-symmetric reference shape
grading: conserved incidence charges, hard-core impurity state, four bath species, bath number, Neumann order, path identity, contraction identity, ordered energy-variable provenance and specieswise permutation parity
action_owner: repository-construction -- K139 fixes C and G, K156 fixes W=(E_R-256)I-X after matched endpoint subtraction, and K177/K178 fix the structural contraction coordinates; no source/GU action selects the physical extension, state, domain, polarization or scalar center
target: close K178's coefficient-data gate without performing the downstream determinant integrals, then expose order two as the first exact numerical evaluation target MAP-TYPE=intertwiner
```

## Inline preflight bookend

K178 proved that the path census and generic determinant representation do not
identify a numerical family. Retrieval against K139 and K156 shows that the
five fields are nevertheless derivable from the fixed operator. The
route-changing issue is sign and normalization, not combinatorics: K177's
`car_sign` is the exact structural CAR sign, but the public structural record
does not also carry the factor `(-1)^n` from
`G^n=[-(H0+256)^-1 C*]^n`.

The route census compared hand completion, direct finite-regulator matrices,
symbolic operator normal ordering, sparse continuum compression, immediate
quadrature and action-column assembly. The selected route is a deterministic
operator-level term generator with a separate finite CAR action at order two.
Hand completion cannot be audited, an independently rebuilt regulator would
violate K163, and quadrature is downstream of the exact signed family.

The source register and v0.263 physics ledger do not move. `SC-META-53`
remains `UNCERTAIN`; `LT-SM8`, `RA-F1` and `AC-F1` remain `NEEDS`.

## 1. Fixed boundary monomials

Write `B_i=|i><0|`. The K139 annihilation half on the two-edge control is

```text
C=sum_i [B_i a_(i,+) + B_i* a_(i,-)],                 (1)
```

with all four bath species mutually CAR-orthogonal. Its adjoint creates the
K177 letters:

```text
0 -> i : a_(i,-)* B_i,       recorded as i-,
i -> 0 : a_(i,+)* B_i*,      recorded as i+.          (2)
```

After the adjacent contraction is removed against the matched endpoint, a
new `i-` can contract only an older `i-`, giving impurity matrix unit
`B_i*B_i=|0><0|`. A new `i+` may contract an older `j+`, giving
`B_j B_i*=|j><i|`. These two cases determine every operator-monomial identity
in the K178 family; no coefficient is selected from a count or fitted value.

## 2. Exact coefficient and the missing Neumann sign

Let `epsilon(gamma,k)` be K177's exact global-CAR sign for path `gamma` and
older position `k`. The structural sign is preserved. The actual order-`n`
input is `G^n phi`, so the older contraction in `X` has coefficient

```text
c_X(gamma,k)=(-1)^n epsilon(gamma,k).                  (3)
```

K156 fixes

```text
C(H0+256)^-1C*=c_N D+X,
W=(E_R-256)I-X.                                       (4)
```

Therefore the exchange contribution to `W G^n phi` is

```text
c_W(gamma,k)=(-1)^(n+1) epsilon(gamma,k).              (5)
```

This narrows one K177 presentation sentence: its structural `car_sign` is not
already the complete `G^n` coefficient. K177's automaton, CAR action,
contraction census and representation theorem remain unchanged.

At order two the six terms have W-sign counts `+1:2` and `-1:4`. A separate
direct finite CAR calculation builds the two-letter state, applies the inner
creation and the outer older-letter contraction without calling K177's
contraction enumerator, and then applies the `W=-X` sign. All six compiled
coefficients agree exactly.

## 3. Contracted-resolvent incidence and output kernel

For an order-`n` path put

```text
D_j=256+sum_(r=1)^j E_r,       E_r=sqrt(1+p_r^2).      (6)
```

The inner exchange creation introduces `p_(n+1)` and the outer resolvent
`D_(n+1)`. If the outer annihilator contracts old position `k`, then the
creation resolvent is `D_k`, the distinguished outer resolvent is `D_(n+1)`,
and every denominator containing the contracted energy is

```text
D_k,D_(k+1),...,D_n,D_(n+1).                           (7)
```

The compiler records (7), not only its two endpoints. The ordered output
kernel on the remaining `n` variables is

```text
c_W (2*pi)^(-(n+2)/2)
  int_R dp_k / [D_1 D_2 ... D_n D_(n+1)].              (8)
```

The exponent counts the `n` path creations, the inner creation and the outer
point annihilation. The integration measure in (8) is `dp_k` because all point
normalizations have already been placed in the prefactor. This convention
reproduces K172's `D_256` normalization at the first-block boundary.

## 4. Exterior normalization

Equation (8) is an ordered coefficient before repeated bath species are
identified. For output multiplicities `m_s`, the compiler applies the
normalized CAR exterior projection

```text
product_s [1/sqrt(m_s!)] sum_(pi in S_(m_s)) sgn(pi) P_pi.  (9)
```

Successive normalized creation operators therefore carry no additional
factorial in the ordered coefficient, and the wedge inner product is exactly
the specieswise determinant used by K177. Each term records its output
species multiplicities and factorials, so later grouping cannot silently
switch to an unnormalized antisymmetrizer.

## 5. Complete generated family and release replay

The executable generates one complete record for each of K178's `2,958`
contractions. `--terms` emits the canonical JSON expansion; the sorted compact
encoding has SHA-256

```text
ee24469ef5c6bb8d606efe1d529b294cbc7097b14adc51df80a51627aa7eb686. (10)
```

Every record now has all five K178 fields, leaving zero unresolved instances.
K178 numerical admission accepts the family. Order one remains empty, order
two has six terms, and order twelve has `1,152` terms.

This opens numerical evaluation; it does not perform it. The terms must first
be combined as a signed sum and then bounded at determinant level so small-time
antisymmetric cancellation is not lost. Until that succeeds, K175's scalar and
diagonal pieces plus K176's tail cannot be assembled into the complete K171
action column. The complete `R_ref` residual, complement or flux floor,
scalar-center floor and K152 interval remain open.

## Hostile result review

- **Strongest overclaim:** “K179 numerically evaluates the exchange prefix.”
  Refused. It identifies the exact family and passes admission; every integral
  remains unevaluated.
- **Strongest sign attack:** omit either `(-1)^n` from `G^n` or the minus in
  `W=-X`. The direct order-two CAR action catches both.
- **Strongest normalization attack:** use an unnormalized alternating sum or
  hide the outer point factor in the measure. The term validator pins both the
  species factorials and `(2*pi)^(-(n+2)/2)`.
- **Strongest contrary route:** a determinant-free sparse K162 compression may
  still be cheaper. K163 requires it to compress this same limiting family
  with a proved error; it cannot replace the operator-derived terms.
- **Weakest analytic seam:** determinant cancellation on coincident simplex
  faces remains uncontrolled. Numerical work must bound the signed family as
  a whole rather than interval each entry independently.

## Inline postflight bookend

The K178 data gate is closed: all `2,958` surviving exchange contributions now
have a deterministic coefficient-complete encoding, exact sign theorem,
denominator incidence, output kernel and normalized exterior convention. The
first nonzero order is independently checked by direct finite CAR action.

The next condition is numerical rather than structural: evaluate the six
order-two terms with determinant-level outward bounds, cross-check them against
a same-family conforming compression, and only then scale the evaluator through
order twelve. Source, ledger, canon, paper, release and public posture remain
unchanged.

## Reproduction

```bash
python3 tests/channel-swings/k179_matched_normal_order_coefficient_family.py --demo
python3 tests/channel-swings/k179_matched_normal_order_coefficient_family.py --terms
python3 tests/channel-swings/k179_matched_normal_order_coefficient_family_probe.py
python3 tests/channel-swings/k179_matched_normal_order_coefficient_family_probe.py --selftest
```

Expected: all exact controls pass and every hostile sign, incidence,
normalization, scope and release mutation is caught.
