---
title: "K177 Laplace-simplex exchange-prefix wave"
document_role: active_research
doc_type: conditional_native_K139_K177_boundary_word_automaton_antisymmetric_kernel_and_laplace_simplex_prefix_result
created: 2026-09-09
date: 2026-09-09
claim_ceiling: exact repository-owned continuum-coordinate result for the K139--K176 equal-coupling two-edge positive particle/hole point control; every K162 vacuum and one-impurity boundary word through order twelve is serialized by a finite hard-core path automaton, every matched older-letter contraction is enumerated with exact CAR sign and fixed-charge verification, the order-one exchange vector is exactly zero, and all remaining Fock scalar products reduce to finite ordered Laplace-simplex integrals of relativistic one-particle heat-kernel determinants, but those integrals, the complete base and reference action columns, M-dual residual, complement or flux floor, scalar-center left floor, K152 interval, physical/source selection, Born derivation, prediction and confirmation remain unevaluated
manifest: lab/process/k177-laplace-simplex-exchange-prefix-wave.json
solver: tests/channel-swings/k177_laplace_simplex_exchange_prefix.py
probe: tests/channel-swings/k177_laplace_simplex_exchange_prefix_probe.py
target_claim: INTERNAL_TARGET:K176_RESOLVED_EXCHANGE_VECTOR_PREFIX
target_claim_verdict: EXACT_CONTINUUM_COORDINATE_AND_INTEGRAL_REDUCTION_COMPLETE__OUTWARD_NUMERICAL_PREFIX_OPEN
canon_verdict_change: none
---

# K177 Laplace-simplex exchange-prefix wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet remains on the repository-supplied K139--K176 hard-core
`C3` impurity coupled to four particle/hole bath species on `L2(R)`, at the
auxiliary chart `lambda=256`. It does not discretize momentum. Its finite
objects are path and contraction labels for exact continuum kernels.

```gu-typed-objects
result: every K162 seed word through order twelve and every K176 matched older-letter contraction has a finite canonical coordinate description; cumulative resolvents admit an ordered Laplace-simplex representation, and antisymmetric Fock inner products reduce specieswise to determinants of the relativistic heat kernel
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space Gamma_-(L2(R;C4)), in q=(0,0),(1,0),(0,1), with the fixed K139 chart and normalized K162 zero-bath seed lines LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive physical Fock Hilbert pairing transported by S=(1-G_256)^-1 to M=S* S; ordered tensors are antisymmetrized within each bath species before any norm or residual is formed ON=repository_signed_point_control
real_structure: CAR adjoint, momentum conjugation, Hermitian matched normal ordering, exact global orbital signs on distinct dummy modes and the K168 real flavor-symmetric reference shape
grading: conserved incidence charges, hard-core impurity state, four bath species, bath-particle number, boundary-word order, Laplace-simplex order and K162 level
action_owner: repository-construction -- K156 owns the matched regular core, K176 owns its all-order exchange tail, and this packet owns only the exact finite-prefix coordinate and integral reduction; no source/GU action selects an extension, state, domain, polarization or scalar center
target: convert the K176 orders-one-through-twelve vector request into exact antisymmetric continuum kernels and a rigorous finite integral family suitable for outward evaluation MAP-TYPE=intertwiner
```

## Inline preflight bookend

K176 proves a tail below `1/250` after order twelve but intentionally leaves
the resolved vector prefix unevaluated. A direct twelve-dimensional momentum
grid is not an admissible native shortcut: K163 already separates independently
rebuilt finite regulators from the K162 common-carrier compression, and a grid
does not preserve exterior antisymmetry or supply an outward continuum error.

The route census compared direct multidimensional quadrature, sparse dyadic
Fock matrices, tensor networks, Slater/determinant coordinates, Schwinger
parameters, Feshbach moments and an obstruction-only close. The boundary-word
automaton followed by a Laplace-simplex transform is exact before numerical
work, exposes all CAR cancellations, and replaces momentum-space tensor
integrals by a reusable one-particle heat kernel. It is the strongest route.

The source register and v0.263 physics ledger do not move. `SC-META-53`
remains `UNCERTAIN`; `LT-SM8`, `RA-F1` and `AC-F1` remain `NEEDS`.

## 1. The complete hard-core seed-word automaton

Write the impurity state as `0`, `1` or `2`, and label the four bath species
by `i+`, `i-`, `i=1,2`. The creation half of the K139 boundary map permits
exactly

```text
0 --i---> i,             i --i+--> 0.                 (1)
```

The first arrow creates a hole of flavor `i` and occupies impurity `i`; the
second creates a particle of the same flavor and empties it. The hard-core
condition forbids any other transition. Every arrow preserves

```text
q_i = n_i + N_(i+) - N_(i-).                          (2)
```

For a vacuum seed, choices occur on odd steps; for a one-impurity seed they
occur after the forced first step. Therefore the exact path counts are

```text
#P_n(Omega)=2^ceil(n/2),
#P_n(d_i*Omega)=2^floor(n/2).                          (3)
```

At order twelve there are `64` paths for each of the three seeds. Across
orders zero through twelve there are `253+190+190=633` path coordinates.
These are coordinate labels, not 633 orthogonal or linearly independent
vectors: paths with the same final impurity and species occupation can
interfere after antisymmetrization.

For a path `gamma=(alpha_1,...,alpha_n)` with momenta `p_1,...,p_n`, let
`epsilon_gamma` be its exact global-CAR sign. Before antisymmetrization its
cumulative-resolvent coefficient is

```text
k_gamma(p_1,...,p_n)
 =epsilon_gamma (2*pi)^(-n/2)
  product_(j=1)^n [256+sum_(r=1)^j omega(p_r)]^(-1),  (4)
omega(p)=sqrt(1+p^2).
```

The native word is `Alt_gamma k_gamma`, where `Alt_gamma` antisymmetrizes
the variables belonging to each identical bath species and leaves different
species in their fixed global order. This fence is essential: an ordered path is not itself a Fock vector.

## 2. Exact matched older-letter contractions

To form `C A^-1 C* G^n phi`, extend each order-`n` path by one fresh bath
mode. Contracting `C` with that fresh mode is the adjacent Wick contraction
K176 identifies with the endpoint counterterm. The compiler removes it before
forming a continuum coefficient. It never subtracts two divergent continuum
vectors.

Every surviving contraction annihilates an older mode. The hard-core
selection rules sharpen the raw `16n` triangle census:

- after `0 -> i` creates `i-`, only an older `i-` can be annihilated;
- after `i -> 0` creates `i+`, any older `j+` can be annihilated, and the
  output impurity is `j`.

The solver realizes every path on distinct dummy modes in the exact global
CAR order, performs the extension and older-mode annihilation, records the
sign, and independently checks the final charge. It finds `2,958` matched
contraction coordinates across all three seeds and orders one through twelve:
`1,158` from `Omega` and `900` from each one-impurity seed. This is before
combining paths that land in the same antisymmetric kernel class.

At order one the list is empty for every seed. Thus

```text
X_ex,1 G phi = 0                                      (5)
```

on all three K162 seed lines. This retrospectively explains why K172's exact
first block contains only the scalar and diagonal multiplier. The genuinely
new exchange-prefix evaluation begins at order two, not order one.

## 3. Ordered Laplace-simplex representation

For positive `a`, `a^-1=int_0^infinity exp(-ta)dt`. Applying this to every
factor of (4) gives `t_1,...,t_n>0`. Put

```text
s_r=t_r+t_(r+1)+...+t_n.                              (6)
```

The Jacobian is one and the positive orthant becomes the ordered simplex
`s_1>s_2>...>s_n>0`. The exponent telescopes exactly:

```text
product_(j=1)^n [256+sum_(r<=j)E_r]^(-1)
 =int_(s_1>...>s_n>0)
    exp[-256 s_1-sum_(r=1)^n E_r s_r] ds.             (7)
```

The executable checks the coefficient incidence for every order one through
twelve. Equation (7) has no discretization, series truncation or stochastic
step. A K176 exchange contraction contributes the second resolvent as one
additional positive Schwinger parameter, so it remains in the same ordered
heat-kernel class.

## 4. Fermionic scalar products become heat-kernel determinants

At fixed simplex variables, (7) is a decomposable tensor of one-particle
functions `exp(-s_r omega)`. Hyperbolic substitution `p=sinh u` gives the
exact one-particle Gram kernel

```text
kappa(t)
 =int_R exp[-t sqrt(1+p^2)] dp/(2*pi)
 =K_1(t)/pi,                                           (8)
```

where `K_1` is the modified Bessel function. There is no extra factor `1/t`.
For `r` particles of one species, the exterior inner product is the Slater
determinant

```text
det[kappa(s_i+r_j)]_(i,j=1)^r.                        (9)
```

Different species factorize. Path pairs with different final impurity or
different species occupation are orthogonal. Hence every Gram, scalar,
diagonal and matched-exchange scalar product in the order-twelve prefix is a
finite sum of ordered-simplex integrals of products of determinants (9), with
the compiler's exact CAR signs. The continuum dimension has not disappeared;
it has been moved into a structured positive-time integral whose one-particle
kernel and antisymmetry are explicit.

## 5. Release replay

K177 closes the exact coordinate problem and one finite prefix component:

1. all 633 boundary-word coordinates through order twelve;
2. all 2,958 matched older-letter contraction coordinates with CAR signs and
   charge checks;
3. the order-one exchange vector, exactly zero; and
4. the reduction of all remaining prefix scalar products to explicit finite
   ordered-simplex heat-kernel determinant integrals.

It does not numerically evaluate those integrals with outward bounds. The
coefficient-complete base action column, its covariance with K168's reference
shape, and the complete `M`-dual residual therefore remain open. K176's
`1/250` tail cannot be added to a prefix whose numerical norm is still
unbounded by a certified interval. The positive complete `M`-orthogonal
complement or flux floor, scalar-center left floor and K152 interval remain
downstream.

The next numerical method must preserve the simplex ordering and determinant
cancellation. A viable certificate can compactify the positive variables,
bound `K_1` and its derivatives by intervals on each box, sum the signed
path-pair integrals by occupation signature, and control the small-time faces
analytically before adding K176's tail. Sparse K162 compression remains the
fallback, but only as a compression of the same kernels with a proved error.

## Hostile result review

- **Strongest overclaim:** “633 paths are 633 basis vectors and therefore the
  continuum prefix is a finite matrix.” Refused; identical species require
  antisymmetrization and the coefficients remain continuum functions.
- **Strongest contrary construction:** a conforming sparse K162 dyadic
  compression may evaluate the same prefix more cheaply. It remains valid if
  it compresses the fixed kernels and carries an outward error; K163 forbids
  substituting an independently rebuilt regulator Hamiltonian.
- **Weakest analytic seam:** determinants of heat kernels have strong
  cancellation near coincident simplex variables. Entrywise interval bounds
  can destroy that cancellation; the next certificate must use determinant-
  level or divided-difference bounds.
- **Weakest reproducibility seam:** the Bessel normalization is
  `K_1(t)/pi`, not `K_1(t)/(pi t)`. The artifact and hostile control pin the
  hyperbolic-substitution normalization explicitly.

## Inline postflight bookend

The finite-prefix task is now finitely and natively specified. Its apparent
twelve-particle brute-force problem reduces to 633 signed path coordinates,
2,958 non-adjacent contraction coordinates, and a finite family of ordered
heat-kernel determinant integrals. Order one closes as zero. Numerical
interval evaluation, action-column assembly and the residual remain honest
open work; no complement, center, physical extension or source claim moved.

## Reproduction

```bash
python3 tests/channel-swings/k177_laplace_simplex_exchange_prefix.py --demo
python3 tests/channel-swings/k177_laplace_simplex_exchange_prefix_probe.py
python3 tests/channel-swings/k177_laplace_simplex_exchange_prefix_probe.py --selftest
```

Expected: `42/42` exact controls and `28/28` hostile mutations caught.
