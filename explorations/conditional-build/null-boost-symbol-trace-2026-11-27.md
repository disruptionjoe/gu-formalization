---
title: Null-boost trace obstruction for short equivariant symbol complexes
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: LB-CLASS
tier: T1
expected_delta: Decide whether any coefficient choice or finite middle differential order can make the declared repeated-coefficient four-term symbol complex exact on the native null cone while its end arrows remain first order.
actual_delta: Null-boost covariance and trace additivity force a+c=(n-1)b for scalar homogeneous orders a,b,c. First-order ends in dimension14 require13b=2, excluding every nonnegative integer middle order in the declared class.
class_covered: Four finite-dimensional modules E, Vstar tensor E, Lambda^(n-1)(Vstar) tensor E and Lambda^n(Vstar) tensor E with the same nonzero smooth coefficient representation E, equivariant homogeneous symbol arrows of scalar orders a,b,c, and a real metric-preserving boost scaling a nonzero real null covector. All symbol coefficients are quantified. Componentwise mixed-order filtrations and extra modules are outside the class.
premises:
- lab/sources/source-claim-register.yaml#SC-ACT-06
- lab/sources/source-claim-register.yaml#SC-META-04
- explorations/eric-curt-wave3d-b2c8-source-forked-two-connection-square-euler-map-2026-08-01.md
- lab/process/k276-sc-act-06-euclidean-principal-complex-data-gate.json
- lab/process/k708-sc-act-06-euclidean-dewitt-signature-gate.json
- lab/process/k720-sc-act-06-selected-i1b-euclidean-bosonic-symbol.json
- explorations/conditional-build/k1127-k887-t0-gauge-carrier-correction-2026-10-05.md
- explorations/conditional-build/k1130-k1129-corrected-action-boundary-2026-10-05.md
source_bridge:
  status: conditional
  reason: SC-ACT-06 asserts a reduced elliptic complex for Upsilon=0 but does not authenticate these four modules, their scalar orders or an ambient null-boost stabilizer at a held background. The printed epsilon field and algebraic gauge component cannot be silently removed to obtain this class.
kill_condition: Exactness forces the scalar-order balance. A nonzero balance excludes every symbol choice in the class; in dimension14 with first-order ends no integer middle order can satisfy it.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: INTERNAL-NULL-BOOST-SHORT-SYMBOL-CLASS
target_claim_verdict: Exactness at the real null covector excluded for the declared dimension14 first-order-end class; source necessity unproved.
canon_verdict_change: none
matrix_or_ledger_effect: none
---

# A trace obstruction on the null cone

```yaml
program_target: LB-CLASS
tier: T1
expected_delta: Decide whether any coefficient choice or finite middle differential order can make the declared repeated-coefficient four-term symbol complex exact on the native null cone while its end arrows remain first order.
actual_delta: Null-boost covariance and trace additivity force a+c=(n-1)b for scalar homogeneous orders a,b,c. First-order ends in dimension14 require13b=2, excluding every nonnegative integer middle order in the declared class.
```

## Result first

**No symbol complex in the declared dimension14 class is exact at a real nonzero null covector when its two end arrows are first order. Changing only the finite middle differential order cannot repair it.** The proof quantifies over every coefficient choice and uses an alternating trace, not a selected Shiab matrix or a rank census.

The obstruction is specific to the module pattern, homogeneous orders and boost covariance. Indefinite signature alone does not obstruct elliptic complexes: the full de Rham symbol is exact at every nonzero covector in every signature. The dimension3 short de Rham complex and dimension2 Maxwell complex provide exact controls with the exceptional allowed orders.

| State | Meaning |
|---|---|
| ESTABLISHED by the written proof | Necessary scalar-order balance a+c=(n-1)b; dimension14 exclusion for all nonnegative integer middle orders with first-order ends. Execution and acceptance evidence are separate. |
| RULED OUT | Coefficient tuning, lower-order correction, or a different integer middle order as repairs that preserve every stated module/symmetry/order hypothesis. |
| SURVIVES / OUTSIDE THE CLASS | Full de Rham sequences, different modules or rows, reduced background symmetry, componentwise mixed orders, different end orders, and real covector domains without the tested null ray. |
| UNDETERMINED / NOT MODELED by this test | Necessity of this class for SC-ACT-06, a complete source deformation complex, a global Fredholm realization, physical cohomology or GU falsification. |

```gu-typed-objects
result: coefficient-independent null-symbol exactness obstruction by shifted boost trace
carrier: E to Vstar tensor E to Lambda^(n-1)(Vstar) tensor E to Lambda^n(Vstar) tensor E; same nonzero finite coefficient representation throughout LAYER=ambient CHIRALITY=N/A
pairing: no field pairing or positivity used; a nondegenerate indefinite metric supplies the null boost ON=ambient_tangent_space
real_structure: real null covector and real orthogonal boost; coefficient representations may be real or complex; no K77/K95 adjoint identification
grading: four chain positions with scalar symbol orders; exterior degrees0,1,n-1,n are distinct from source Bose/Fermi grading
action_owner: repository-construction of a structural interpretation test; no action selected or varied
target: exactness of the fixed-covector symbol sequence MAP-TYPE=intertwiner
```

> **GU-COMPARATOR-ROUTING — scope before inference.** Hodge degree identification does not establish a source self-dual complex. The printed gauge, epsilon, metric and independent matter fields cannot be replaced by this four-term template without a typed reduction. [Routing](../../lab/methods/source-native-comparator-routing.md).

## 1. Exact theorem and assumptions

Let V be an oriented real nondegenerate quadratic space of dimension n>=2 with indefinite signature. Let k be a nonzero real null covector. Choose a metric-preserving one-parameter boost g(s) whose covector action satisfies `g(s)k=exp(s)k`. Let E be a nonzero finite-dimensional real or complex smooth representation of that one-parameter group. Full Spin equivariance is sufficient, but only this boost covariance is needed.

Consider

```
C0 = E,
C1 = Vstar tensor E,
C2 = Lambda^(n-1)(Vstar) tensor E,
C3 = Lambda^n(Vstar) tensor E.
```

There are symbol maps p_j(xi):Cj->C(j+1), j=0,1,2, homogeneous in xi of scalar degrees `m0=a`, `m1=b`, `m2=c`. Assume covariance

`p_j(g(s)xi)=rho_(j+1)(g(s)) p_j(xi) rho_j(g(s))^-1`.

The theorem permits arbitrary coefficients satisfying these hypotheses. For principal symbols of local differential operators, a,b,c are nonnegative integers; the trace argument itself works for any differentiable homogeneous degrees. At k, assume the symbols form a complex. If they do not compose to zero, they already fail the complex requirement.

**Theorem.** Exactness of `0 -> C0 -> C1 -> C2 -> C3 -> 0` at k implies

`a+c=(n-1)b`.                                                     (1)

No diagonalizability or semisimplicity of the action on E is required.

**Dimension14 corollary.** For a=c=1, equation(1) is `13b=2`. It has no solution b in the nonnegative integers. Thus every finite local middle order is excluded while these end orders, modules and covariance are held. For a=b=c=1 the trace defect is `(3-n)dim(E)`, so the all-first-order class fails in every n other than3.

## 2. Proof by invariant images and trace additivity

Write B_j for the infinitesimal boost on Cj. Differentiating covariance along the null ray and using homogeneity gives

`B_(j+1) p_j(k)-p_j(k) B_j = m_j p_j(k)`.

Set cumulative shifts `s0=0`, `s1=a`, `s2=a+b`, `s3=a+b+c`, and define `M_j=B_j-s_j I`. Then

`M_(j+1)p_j(k)=p_j(k)M_j`:

the shifted boosts are an endomorphism of the fixed-k complex.

If this finite complex is exact, put `I_j=im p_(j-1)(k)`, with I0=I4=0. Each I_j is M_j-invariant. Exactness gives short exact sequences

`0 -> I_j -> Cj -> I_(j+1) -> 0`.

The quotient action is identified with the action on I_(j+1) through p_j. In any basis adapted to I_j, M_j is block triangular. Its trace is therefore the trace on I_j plus the trace on the quotient. No invariant complement is required. Alternating these identities cancels every image contribution, giving

`tr M0-tr M1+tr M2-tr M3=0`.                         (2)

Let e=dim(E)>0 and r=tr(B_E). A metric-preserving infinitesimal boost has trace0 on V and Vstar. The orientation representation is trivial, and `Lambda^(n-1)(Vstar)` is isomorphic to V tensor the orientation line. Thus

```
tr B0 = tr B3 = r,
tr B1 = tr B2 = n r,
dim C0 = dim C3 = e,
dim C1 = dim C2 = n e.
```

The unshifted traces cancel. Substituting into(2) gives

```
r - (n*r-a*n*e) + (n*r-(a+b)*n*e) - (r-(a+b+c)*e)
  = [a+c-(n-1)b]e.
```

Since the field has characteristic0 and e>0, equation(1) follows. This proves the theorem without eigenvectors, characters or a native matrix construction.

For n14, all first orders and E=End_C(S128), e=16384 and the defect is **-180224**. This is a module/order trace checksum, not a cohomology dimension. The same first-order arithmetic applies to any nonzero finite E; its specific Clifford decomposition cancels from the theorem.

Trace additivity and alternating traces of finite complexes are standard: [Stacks Project, Lemma15.122.1](https://stacks.math.columbia.edu/tag/0GSY) and [Proposition64.10.2](https://stacks.math.columbia.edu/tag/03TI). The invariant-image proof above supplies the exact argument needed here. No world-novelty claim is made.

## 3. Positive controls and exception boundaries

### Dimension3: de Rham, orders1/1/1

For any nonzero k, the full exterior symbol sequence `k wedge` is exact. Choose a vector v with k(v)=1; then

`i_v(k wedge omega)+k wedge i_v(omega)=omega`.

Such a v exists even when k is null; no division by its metric norm occurs. In dimension3 the full de Rham sequence has precisely the four modules above, tensor E, and a=b=c=1 satisfies1+1=(3-1)1. This exact example survives both definite and indefinite signature.

### Dimension2: Maxwell, orders1/2/1

Using metric and orientation identifications, take

```
p0(k)u = k u,
p1(k)alpha = q(k)alpha-k<k,alpha>,
p2(k)alpha = <k,alpha>,
q(k)=<k,k>.
```

The last scalar is identified with the top form, and the arrows act as the identity on E. Their compositions vanish. For nonnull k, p1 has kernel span(k) and image k-perpendicular. For null k in dimension2, nondegeneracy gives `k-perpendicular=span(k)`, and p1 is the nonzero rank-one map `-k<k,.>`. Both middle equalities remain exact; p0 is injective and p2 surjective. The balance is1+1=(2-1)2.

For this Maxwell sequence in n>2, at a null covector both middle cohomology dimensions are n-2 per coefficient direction: ker p1=k-perpendicular has dimension n-1, while im p0=span(k); likewise ker p2/im p1. The dimension2 control is not a higher-dimensional null repair. At nonnull covectors the Maxwell symbol is exact in every dimension; ordinary ellipticity requires every nonzero real covector.

### Full de Rham and positive-definite signature

The full de Rham symbol is exact in every dimension and every metric signature by the same contraction identity. For n>3 it includes extra intermediate exterior modules and lies outside the four-term pattern. Indefinite signature alone therefore does not forbid elliptic complexes.

Positive-definite signature has no nonzero real null covector scaled by a metric-preserving real boost. The theorem does not obstruct ordinary Riemannian elliptic complexes. A complex null covector alone cannot refute real ellipticity. The standard definition tests exactness off the real zero section; see [Atiyah–Singer, The Index of Elliptic Operators I](https://math.uchicago.edu/~shmuel/tom-readings/ASI.pdf). [Branson–Gover's conformal deformation detour complex](https://arxiv.org/abs/math/0605192) is related background with different modules and stated ellipticity in Riemannian signature, not an attribution of this theorem.

## 4. What changes the theorem

Coefficient changes and genuine lower-order terms cannot alter the shifted trace of the same principal symbol profile. In dimension14, changing only b to another nonnegative integer also fails. The general balance is merely necessary: satisfying it does not construct exact symbols or a differential complex.

These changes require a new calculation and are not covered:

* different coefficient representations, extra modules/rows, or a longer complex;
* componentwise Douglis–Nirenberg weights instead of one scalar order per entire arrow;
* different end orders, fractional/nonlocal orders, or an unproved differential reduction;
* extra held background tensors that break the required boost covariance;
* a changed real covector domain that removes this null ray.

A nonnull-only microlocal restriction avoids the tested ray but does not prove ordinary ellipticity on the original manifold. These are necessary escape categories, not sufficient repairs or source selections. The theorem supplies no positive pairing, gauge quotient, closed domain or Green operator.

## 5. Source scope and corrected reuse

SC-ACT-06 asserts at draft p65 summary item x that **Upsilon=0** carries an elliptic deformation complex in Euclidean signature after redundant Euler equations are discarded. SC-META-04 preserves the older-version/Caveat Emptor qualification on §10/eq10.10. Neither provides the complete reduced symbols or a selected row projector.

The [transcribed §10 skeleton](../eric-curt-wave3d-b2c8-source-forked-two-connection-square-euler-map-2026-08-01.md) are

```
Omega0(ad) -> Omega1(ad) + Omega0(ad) -> Omega13(ad),
delta1=(d_A,DL_epsilon),
delta2=(S_omega d_A+kappa1*,
        F_A wedge K_omega(.)-kappa1*d_B).
```

Here the stars denote Hodge operations; the inner K_omega glyph is not an authenticated complete linearization. The extra zero-form field, algebraic epsilon gauge component, moving-contraction glyph and independent matter rows cannot be discarded to obtain this report's module pattern. A Hodge identification does not establish self-duality. Full ambient Spin/boost symmetry at the held background is another premise: additional source structures can leave a smaller stabilizer. K717 already supplies a background-owned positive auxiliary structure with O(4) naturality, so a smaller-symmetry route must not be described as absent.

| Owned result | Retained meaning and limit |
|---|---|
| K276 | Exterior skeleton and row-deletion controls; not the full source complex. |
| K708–K712 | Euclidean base may have native ambient(13,1); indefinite Hodge gauge-fixing and metric-independent exterior exactness are distinct. |
| K128/K129/K132 and K720/K724 | Actual selected I1B Hessian/order/rank defects, with zero-order kappa separated; not an all-coefficient or complete printed-Upsilon theorem. |
| K926–K940 | Connection-only quotient bundle and auxiliary projector calculations. |
| K1126–K1130 | First-order formal-adjoint sign and native T=0 gauge-carrier corrections remain controlling. Radial d-chi connection columns are not native distortion gauge columns. |

The [gauge correction](k1127-k887-t0-gauge-carrier-correction-2026-10-05.md) and [current action boundary](k1130-k1129-corrected-action-boundary-2026-10-05.md) prohibit reusing the90128 connection-only quotient as source-action cohomology. The [recent companion theorem](shiab-bianchi-companion-class-2026-11-27.md) does not authenticate an ordinary exterior redundancy for the complete source system either. Its selected-map obstruction and positive wedge survivor retain their own types.

The new delta is an all-symbol class exclusion, independent of the old selected coefficients, under a **conditional source interpretation**. The weakest link is authentication of these modules, scalar orders and null-boost covariance in one actual reduced source complex. No SC-ACT-06 status, physical2+1/nonchirality claim, action class or GU-wide verdict changes.

## 6. Verification and continuation

[NullSymbolTrace.lean](../../Lean/GUFormalization/NullSymbolTrace.lean) verifies the scalar trace telescope, shifted-trace polynomial identity and integer impossibility13b=2. It does not formalize invariant-image exactness, representations, symbols, the geometric boost or source necessity. The separately owned exact probe provides concrete boost, symbol and exception controls. This report's author ran no local tests or Lean compilation; counts, hashes and independent T1 acceptance are recorded separately.

The decision is to stop searching inside the stated dimension14 first-order-end profile, including higher finite middle orders. A source-facing successor requires an authenticated complete symbol tuple, or proof that a source-owned component necessarily retains this profile under the actual reduction. Guessing a missing action or extra arrows is not that authentication. The older selected ellipticity and source-incompleteness results are consumed, not awarded new credit by repetition.
