---
title: "Selected-K134 native I1B T=0 kappa Hodge fingerprint and Fourier pencil"
status: active_research
doc_type: exact_all_grade_hodge_clifford_mass_fingerprint_fourier_roots_inertia_and_uniform_gap_gate
created: "2026-08-16"
registry: lab/process/selected-k134-native-i1b-t0-kappa-hodge-fingerprint-and-fourier-pencil.json
probe: tests/channel-swings/selected_k134_native_i1b_t0_kappa_hodge_fingerprint_and_fourier_pencil_probe.py
grade: "K134 CONSTRUCTS THE ACTUAL ALL-GRADE KAPPA-ONE HODGE-CLIFFORD MASS FINGERPRINT ON THE COMPLETE 229376-DIMENSIONAL REAL CL(7,7) DISTORTION CARRIER. K IS A REAL GRADE-PRESERVING INVOLUTION WITH TOTAL INERTIA 114688 PLUS AND 114688 MINUS. K134 CORRECTS THE PENCIL TYPE: THE ACTION HESSIAN AT REAL FOURIER FREQUENCY IS I C_1(N)+KAPPA_1 K, NOT THE RAW REAL COEFFICIENT C_1(N)+KAPPA_1 K. THE HERMITIAN TIMELIKE PENCIL HAS NO NONZERO REAL ROOT; THE SPACELIKE PENCIL HAS 27 EXACT ROOT RADII WITH TOTAL MULTIPLICITY 65456 PER SIGN AND AN EXACT 28-INTERVAL INERTIA CENSUS; THE NULL GENERALIZED COEFFICIENT IS NILPOTENT OF INDEX FIVE. FREQUENCY SCALING PUTS A SPACELIKE SINGULAR SHELL AT SOME FREQUENCY FOR EVERY FIXED NONZERO KAPPA_1, WHILE THE NULL INVERSE GROWS THROUGH FOURTH ORDER. THERE IS THEREFORE NO FREQUENCY-UNIFORM FULL-CARRIER INVERSE OR AUTOMATIC ULTRAHYPERBOLIC CLOSED DOMAIN. K135 MUST COMPOSE THE METRIC CURVATURE BLOCK WITH THESE EXACT SINGULAR SHELLS AND CLASSIFY THE COUPLED KERNEL, ADJOINT AND DOMAIN."
target_claim: K133_NEXT_GATE__ACTUAL_ALL_GRADE_K_STRUCTURE_FINGERPRINT_BLOCK_PENCIL_ROOT_INERTIA_AND_DOMAIN_ADMISSIBILITY
target_verdict: K_EXACT_REAL_GRADE_PRESERVING_BALANCED_INVOLUTION__HERMITIAN_FOURIER_PENCIL_TYPED__SPACELIKE_27_RADIUS_SINGULAR_SHELLS_EXACT__NULL_NILPOTENCY_INDEX_FIVE__NO_FREQUENCY_UNIFORM_INVERSE__COUPLED_METRIC_SHELL_GATE_K135
canon_verdict_change: none
---

# Selected-K134 native I1B T=0 kappa Hodge fingerprint and Fourier pencil

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> first-transgression, real `Cl(7,7)`, Hodge--Clifford pairing, mixed-order
> Fourier-symbol and ultrahyperbolic-domain calculation. Ordinary Einstein,
> Higgs/VEV, family-index, chirality, anomaly, symmetry-breaking and familiar
> particle-spectrum constructions do not adjudicate it without an explicit
> typed bridge. Read `lab/methods/source-native-comparator-routing.md` before
> reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

Scope: K134 binds the selected displayed `comm/symi/symi` `I1B` Hessian at
K127's local Ricci-flat `T=0` fixed-boundary germ. It stands on the repository's
settled real `Cl(7,7)` action algebra, not a settlement of the separate open
ambient-signature reconstruction. It does not select `kappa_1`, a source-global
background, a boundary condition, a BFV quotient or physical cohomology.

## Result in plain English

K133 correctly refused to infer roots from the word “nondegenerate.” K134 now
constructs the missing matrix rather than substituting an identity or guessed
signature.

The quadratic action term is

```text
(kappa_1/2)<T,*T>.
```

In the coefficient basis `dx^mu e_A`, its Hessian is diagonal:

```text
K_(mu,A)=eta_mu (e_A^2)_scalar.                       (1)
```

Thus `K` is real, grade preserving, satisfies `K^2=I`, and has total inertia

```text
(n_+,n_-,n_0)=(114688,114688,0).                     (2)
```

It is nondegenerate and indefinite. It is not a positive Hilbert metric or a
freely chosen fundamental symmetry.

The decisive typing correction is that K133's real derivative coefficient is
skew. The formally self-adjoint action Hessian at real Fourier frequency is

```text
H_n(kappa_1)=i C_1(n)+kappa_1 K,                     (3)
```

which is Hermitian. Inertia belongs to (3), not to the nonsymmetric raw
coefficient matrix `C_1(n)+kappa_1 K`. The two pencils have analytically
continued root dispositions:

| causal representative | raw real coefficient pencil | Hermitian Fourier pencil |
| --- | --- | --- |
| timelike | 27 nonzero root radii | no nonzero real root |
| spacelike | no nonzero real root | 27 nonzero root radii |
| null | only zero | only zero; nontrivial nilpotent part |

For a unit spacelike covector, the squared nonzero Fourier root radii and the
algebraic multiplicity of each sign are

```text
1:312, 2:78, 3:286, 4:46487, 5:1287, 6:1716,
7:1716, 8:1287, 9:2002, 10:286, 11:78, 12:13,
13:1, 16:1716, 25:1716, 36:1287, 48:13, 49:715,
64:286, 81:78, 88:78, 100:13, 120:286, 121:1,
144:715, 160:1287, 168:1716.                        (4)
```

The multiplicities sum to `65456`, one half of the nonnull Euler rank. The
zero root has algebraic multiplicity `98464`.

Scaling the spacelike covector by frequency `rho` moves (4) to

```text
kappa_1=plus-or-minus rho sqrt(a).                    (5)
```

For every fixed nonzero `kappa_1`, choosing
`rho=abs(kappa_1)/sqrt(a)` therefore hits a singular shell. The pointwise
generic inverse of K133 cannot be uniform over frequency.

On the null representative, `L=K C_1(n)` has exact power ranks

```text
rank(L,L^2,L^3,L^4,L^5)=122746,65469,8192,4096,0.    (6)
```

So `L` is nilpotent of index five. For nonzero `kappa_1`, the null inverse is
a finite Neumann polynomial reaching `(rho/kappa_1)^4`. Pointwise
invertibility again fails to give a first-order inverse estimate.

## 0. Pre-wave answers

1. **Fork.** This wave stands on settled `REAL-CLIFFORD-FORM = Cl(7,7)` and
   explicitly does not settle `SIGNATURE-AMBIENT`. The applicable chain is
   `PD-SIGNATURE-PARITY`. If the action carrier were instead ported to the
   non-isomorphic `Cl(9,5)` horn, the Hodge signs and all block inertias would
   require recomputation.
2. **Search dimension.** The carrier dimension is `14*2^14=229376`. The
   question is decided wholesale by the exact `56/56/49` invariant causal
   block types with combinatorial multiplicity; no coefficient-by-coefficient
   candidate search is used.
3. **New unowned object.** None. `K` is owned by the written quadratic
   `kappa_1` Hodge term. A closed ultrahyperbolic domain remains unowned and is
   not introduced by the calculation.
4. **What dies or is re-scoped.** K133's “real roots and inertia unknown”
   ceiling is closed for the selected `Cl(7,7)` carrier. Its flat-complex
   obstruction, principal ranks, absence of a distortion gauge owner and
   global-domain ceiling survive. The propagation set is K133, current state,
   roadmap, research status and context.

## 1. Layer-0 and action custody

| object | exact meaning | not identified with |
| --- | --- | --- |
| `K` | Hessian of `<T,*T>/2` in the action pairing | identity matrix, positive norm or fitted mass |
| `C_1(n)` | real skew first-order coefficient | a differential or Hermitian matrix by itself |
| `iC_1(n)+kappa K` | Hermitian frozen-Fourier Hessian | a global closed operator |
| root multiplicity | order in the block determinant | gauge dimension or automatically the kernel dimension |
| balanced inertia | local Krein signature | physical positivity |
| singular shell | fixed-frequency loss of invertibility | a gauge orbit or cohomology class |

For Clifford grade `p`, the `K` block has dimension `14 binomial(14,p)` and
inertia

```text
(7 binomial(14,p), 7 binomial(14,p), 0).             (7)
```

This gives the full all-grade fingerprint and proves that no grade or causal
block may silently replace `K` by a definite identity.

## 2. Exact Fourier inertia

At `kappa_1=0`, the nonnull inertia is
`(65456,65456,98464)` and the null inertia is
`(61373,61373,106630)`. Away from zero, the timelike and null full-carrier
inertias are balanced `(114688,114688,0)` because they have no nonzero real
Fourier roots.

For positive dimensionless `x=kappa_1/rho`, the spacelike inertia between
successive root shells is:

| interval for `x^2` | `(n_+,n_-,n_0)` |
| --- | --- |
| `(0,1)` | `(114682,114694,0)` |
| `(1,2)` | `(114688,114688,0)` |
| `(2,3)` | `(114682,114694,0)` |
| `(3,4)` | `(114676,114700,0)` |
| `(4,5)` | `(114709,114667,0)` |
| `(5,6)` | `(114694,114682,0)` |
| `(6,7)` | `(114674,114702,0)` |
| `(7,8)` | `(114654,114722,0)` |
| `(8,9)` | `(114639,114737,0)` |
| `(9,10)` | `(114639,114737,0)` |
| `(10,11)` | `(114633,114743,0)` |
| `(11,12)` | `(114627,114749,0)` |
| `(12,13)` | `(114626,114750,0)` |
| `(13,16)` | `(114625,114751,0)` |
| `(16,25)` | `(114605,114771,0)` |
| `(25,36)` | `(114625,114751,0)` |
| `(36,48)` | `(114610,114766,0)` |
| `(48,49)` | `(114611,114765,0)` |
| `(49,64)` | `(114626,114750,0)` |
| `(64,81)` | `(114620,114756,0)` |
| `(81,88)` | `(114626,114750,0)` |
| `(88,100)` | `(114632,114744,0)` |
| `(100,120)` | `(114631,114745,0)` |
| `(120,121)` | `(114637,114739,0)` |
| `(121,144)` | `(114638,114738,0)` |
| `(144,160)` | `(114653,114723,0)` |
| `(160,168)` | `(114668,114708,0)` |
| `(168,infinity)` | `(114688,114688,0)` |

For negative `x`, positive and negative inertia swap because
`H(-x)=-conjugate(H(x))`. This is an exact congruence census of the Hermitian
realification, not a floating eigenvalue classification.

## 3. Domain and BV disposition

Three independent facts survive every nonzero `kappa_1`:

1. the lower-order term does not change K132's principal characteristic set;
2. the spacelike family contains exact singular shells at some frequency; and
3. the null inverse has fourth-order frequency growth.

Therefore no fixed nonzero `kappa_1` gives a frequency-uniform inverse on the
complete distortion carrier. This obstructs the naive full Fourier-multiplier
domain. It does not prove that every restricted boundary-value problem is
impossible: a signature-appropriate domain could exclude or control shells,
but that is new analytic data and must be checked against the action Green
form.

The shell kernels are not action-owned distortion gauge. K133's failure of a
distortion complex remains. No KT differential, BFV quotient, positive
cohomology or superposition law follows.

## 4. Reverse scaffold and next gate

```text
R0 superposition, if derived, must live in positive physical cohomology.
R1 K127--K132: local T0 germ, coupled Hessian and all-grade obstruction.
R2 K133: universal nondegenerate pencil claims and flat-complex kill.
R3 K134: actual K fingerprint and correctly typed Fourier pencil.
R4 K134: exact spacelike shells plus null order-four inverse growth.
R5 K135: compose A and A* on every exceptional shell; classify the coupled
   kernel, adjoint Green form and admissible constrained domain.
R6 only after a domain: build KT/BFV reduction and test positivity.
R7 only after positive physical cohomology: revisit superposition.
```

K135 must not treat a determinant multiplicity as gauge, delete singular
frequencies, or import an ordinary one-time Dirac domain. Its cheapest exact
discriminator is whether the metric curvature block `A` pairs nontrivially
with the spacelike shell kernels and the terminal null Jordan chains in the
same invariant basis.

No ledger, canon, public posture, particle, phenomenology or GU truth-status
claim changes. Joe input is not required.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k134_native_i1b_t0_kappa_hodge_fingerprint_and_fourier_pencil_probe.py
```

## K135 successor classification

K135 composes the actual metric curvature block in the same invariant basis.
Only squared radii `4` and `121` meet its image, but all 27 complete coupled
spacelike shells retain nonzero kernel. On the null metric-support packet, all
positive frequency degrees in `-A*C^-1 A` vanish and the remaining metric form
has rank one and radical nine. The analytic restricted-domain and constraint-
propagation problem now routes to K136; do not delete shell frequencies or
rename the retained radical as gauge.
