---
title: "K2594 Reciprocal preparation for measures and regularized point inputs"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed nonzero kappa, fixed annulus and compact radial pressure; distributional fields and smooth-versus-measure reciprocity only
scripts:
  - tests/channel-swings/k2594_reciprocal_distributional_response_probe.py
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2594
carrier: compact smooth conserved A radial pressure times finite interior invariant B measures LAYER=toy CHIRALITY=N/A
pairing: actual tensor contraction with invariant density; distinct scalar w2 and TT w5 coefficient densities ON=declared_carrier
real_structure: real order/conjugate-averaged inverse preparation from K2588
grading: source, TT amplitude, six scalar potentials, original metric and compact detector kept distinct
action_owner: repository-construction -- conditional curved-product completion
target: quantified distributional response and smooth detector continuity MAP-TYPE=evaluation
```

# Quantify the differentiated source before admitting a point

## Result, assumptions and prior credit

K2592's NEW real reciprocal preparation admits finite signed B measures supported in a fixed compact subset of the interior annulus. The reconstructed fields, including the original metric, have the conservative bound C0_loc(A;H^-61_loc(B)). Moving or mollifying an interior atom by epsilon gives O(epsilon) in H^-62. A compact smooth conserved detector F=EW consequently has error at most C epsilon ||W||H64. Constants depend on fixed nonzero kappa, the annulus, compact sets, the source's radial norms and the preparation; no uniform kappa limit or numerical constant is asserted.

The full selected coupled equations survive. Reciprocity extends to ONE measure pressure source against ONE smooth compact pressure source. This does not define a pairing of two point sources, a pointwise metric, physical causality, positivity, or a physically selected boundary condition. This is the same conditional curved-product completion, not source-native GU recovery. SC-ACT-01 ASSERTS its action, SC-GEO-03 ASSERTS Met(X), SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita, and SC-META-53 remains UNCERTAIN. Ledger0.263 LT-GR6b/10/11 and LT-SM8 remain unchanged.

Reuse K2586's fixed-annulus base measure estimates, K2588's real symmetric order average, K2590's full cofactor/metric reconstruction and K2592's spectral resultant exclusion and equation-preserving repair. The earlier H^-43 estimate is NOT inherited through the new correction. This note supplies the missing source-derivative estimate and tracks its losses.

## 1. The source-variable kernel estimate

Fix scalar radial eigenvalue sigma and B angular labels. Let k>=1 be the inherited joint frequency scale, comparable to 1+sqrt(sigma)+ell_plus+ell_minus, with fixed dimensional constants absorbed. Let R be K2588's symmetric determinant inverse and K_sigma(x,t) its kernel in invariant B radial density. The five-factor bounds of K2586 give ||K_sigma||infinity<=C k13. A finite order/conjugate average preserves that estimate and kernel symmetry.

The actual determinant is degree five in Y and has nonzero constant leading coefficient. In the Liouville annular coordinate, normalize its tenth-order equation to

    (partial_x^10 + sum_(j<10) b_j(x) partial_x^j) K_sigma(x,t)
         = J(t) delta_t,
    |partial_x^r b_j(x)| <= C_r k^(10-j).

The coefficient estimates follow by expanding the five (Y-y_i) factors: |y_i|<=3sigma/2, each second-order Y has smooth annular coefficients with angular potential O(k²), and its derivatives have the same polynomial scale. No root separation or commuting boundary resolvents is used. The inverse leading coefficient and invariant-density conversion give a smooth bounded J(t) on each fixed interior compact source set.

Distributional integration of the ODE shows that jets zero through eight are continuous and the ninth jet has jump J(t). Jumps of lower-order jets would create higher derivatives of delta absent from the source. For a local interval of size h=c/k containing t, subtract J(t)(x-t)_+^9/9!. Its ninth jump is exactly the required one; the remainder has bounded tenth weak derivative. Taylor interpolation at ten equally spaced nodes and inversion of the fixed Vandermonde matrix give

    ||u^(j)|| <= C_j(h^-j ||u|| + h^(10-j)||u^(10)||), j<10.

Apply this to the jump-subtracted kernel. Substitute the ODE and choose a sufficiently small FIXED c: the factors h^(10-i)k^(10-i)=c^(10-i) absorb all lower derivative terms in the maximum of the scaled derivative norms. The explicit jump subtraction contributes at most C k^(j-9)|J|. Thus

    |partial_x^j K_sigma(x,t)| <= C k^(13+j), 0<=j<=9.       (1)

For j=9 the bound is piecewise/almost everywhere, not continuity across the diagonal. One-sided intervals give the same estimates up to regular annulus endpoints. Symmetry in the invariant pairing transfers (1) to t derivatives. Smooth fixed density conversion does not change frequency exponents. The eighth source derivative is Lipschitz because its weak ninth derivative is bounded; no tenth classical derivative is invoked.

This local ODE argument is the universal estimate. The independent flat fixture |x-t|^9/(2*9!) checks its critical jump and differentiated-source mechanism: its tenth derivative is delta, ninth jump is one, and eight source derivatives give |x-t|/2. It is not the curved Green operator.

## 2. Apply the actual numerator to the source

K2592 computes the actual P_sigma(Y) with Y degree four and total (sigma,Y) degree five. Therefore each term sigma^a Y^b satisfies a+b<=5, b<=4. Its kernel action uses at most eight source derivatives and costs at most k^(2a+2b)<=k10. Define R P delta through P acting in the SOURCE variable of K in the invariant pairing. Applying a measure bound directly to P delta would be wrong: derivatives of delta are not finite measures.

Equation (1) proves

    |(R P delta_t)(x)| <= C k23,
    |(R P delta_t)(x)-(R P delta_t')(x)| <= C k24 |t-t'|. (2)

P R delta has the same k23 pointwise magnitude bound by target derivatives in (1). For source movement we instead use the distributional bound below: continuity estimates commute with a fixed target differential operator. This costs at most eight B derivatives of the inherited R point estimate. We do NOT assume simultaneous mixed derivatives of total order seventeen are classical across the kernel diagonal.

Using K2586's angular point HΩ^-4 bound and moving-point HΩ^-5 bound on the six-dimensional compact angular product, (2) gives R P delta in local H^-27(B), with input radial loss23; point movement is bounded in H^-28 with loss24. Radial and angular frequency powers can be separated by k^n<=C(1+sqrt(sigma))^n(1+ell_plus+ell_minus)^n.

For P R delta use the baseline R estimate with radial loss13 and angular ceiling17. Apply the fixed differential polynomial P: it costs at most radial10 and B8, giving local B ceiling25<=27. Movement costs radial14+10=24 and B ceiling26<=28. Thus BOTH commutator terms share H^-27, and their source differences share H^-28. We assert these local distribution norms, not joint classical kernel regularity after arbitrary mixed derivatives. This avoids an unjustified source/target derivative exchange of total order seventeen across the diagonal.

## 3. Bound the Bezout coefficients and reconstruct

The actual Sylvester map (A,B) -> A P+B d has nine rows, with deg_Y A<=4 and deg_Y B<=3. Every entry has degree at most five in sigma. Each eight-entry term in an adjugate minor has degree at most40. Its determinant is the actual nonzero resultant. K2592 excluded its zeros on the actual scaled spectrum, which lies in [3,10] union [35,infinity). The resultant has degree17 and grows at infinity, so its reciprocal is bounded on those closed sets. Cramer's rule gives

    |coefficient of A_sigma| <= C (1+sigma)^40.             (3)

This intentionally wastes cancellation. A costs at most80 radial Sobolev orders and eight B differential orders. K2592's repair U_new=R chi-A D chi/2 therefore lies in H^-35_loc(B), with radial input loss103; movement lies in H^-36 with loss104. Reserve q=30 radial orders before reconstruction. The inherited full cofactor, potential-to-tensor, metric shift and auxiliary reconstruction consume at most26 differential orders. Hence

    fields in C0_loc(A;H^-61_loc(B)), input chi in Hrad^133;
    point differences in C0_loc(A;H^-62_loc(B)), input chi in Hrad^134. (4)

Radial derivatives retained after the conservative loss26 are sufficient for local continuity in A with the regular-center compatibility already proved in K2586. Compact smooth radial pressure has trace in every Dirichlet operator power; its fixed splitter supplies every required radial Sobolev order. These exponents are upper bounds on loss, not sharp singularity descriptions. Separate angular/radial estimates imply the stated isotropic local negative Sobolev bounds.

All identities hold first on smooth regularizations. Equation(4), continuity of differential operators on distributions, and unchanged reconstruction pass EVERY selected source equation and synchronized source-split identity to the limit. The new preparation is defined by this limiting extension; no old impedance traces are reimposed on its correction.

## 4. Released measure, transport and reciprocity consumers

On a fixed interior compact source set the point-response map is bounded into H^-61 and Lipschitz into H^-62. Integrate it against a finite signed invariant measure mu. Coefficientwise continuity of the eighth kernel jets and dominated angular/radial summation give continuity in H^-61 as well; the quantitative Lipschitz estimate is in H^-62. Thus the map is strongly measurable with separable Hilbert range. Bochner integration in the local Hilbert distribution space gives

    ||h_mu||H^-61 <= C ||mu||TV.

For equal-mass positive measures, integrate the pointwise difference bound against any coupling, then take its infimum:

    ||h_mu-h_nu||H^-62 <= C W1(mu,nu).                      (5)

For signed measures an explicit signed coupling or TV estimate is required; W1 is not silently applied to arbitrary signed measures. A unit nonnegative mollifier supported within epsilon gives W1<=epsilon and the O(epsilon) error. For compact detector F=EW, E is a fixed second-order operator, so

    |<h_mu-h_nu,EW>| <= C W1(mu,nu) ||W||H64.              (6)

In the flat jump fixture, moving delta0 to delta_epsilon changes the differentiated kernel by exactly epsilon/2 for x>epsilon. This executes a sharp nonzero regularization consumer for the source-derivative mechanism; no numerical curved response is claimed.

For a smooth compact pressure source j_s and a measure pressure source j_mu, mollify mu. K2592 gives <j_s,h_mu_eps>=<j_mu_eps,h_s>. The left converges by (4), the right by smoothness of h_s on the source compact set. Thus <j_s,h_mu>=<j_mu,h_s>. This is a useful extension of full pressure reciprocity to a singular source and a smooth observer. It does not pair two distributions. Physical readout and boundary selection remain independent.

## Verification and next condition

The probe computes actual polynomial degrees/Sylvester bounds, checks the reused resultant's root exclusions, verifies weighted formal transposition and the independent tenth-order jump example, and separately labels exponent bookkeeping. The written interpolation/absorption, spectral synthesis and distribution-limit arguments carry the universal claim. No numerical sampling is a proof of those arguments.

Next compare a sharper local singularity calculation or an independently justified boundary/readout with the original preparation's actual boundary defect. Do not requeue finite-measure existence, regularization or smooth-versus-measure reciprocity on this new preparation as absent. Native displacement, physical causality and two-singular-source pairings remain open.

[K2592](k2592-scalar-tensor-boundary-pairing-2026-11-06.md), [K2586](k2586-fixed-annulus-point-response-2026-11-05.md), [probe](../../tests/channel-swings/k2594_reciprocal_distributional_response_probe.py), [report](../../lab/process/k2594-reciprocal-distributional-response.json).

Independent read-only field specialists and a distinct integrated hostile reviewer inspected the mathematical transfers and final candidates. K2594 passes38 supporting checks and7 contrary controls; K2595 passes62 and8. Exact polynomial/jump/interval calculations, reused predecessor certificates and exponent bookkeeping are distinguished from the written continuum kernel, synthesis, convexity and sensitivity proofs. No external-expert, proof-assistant or physical certification is claimed. Final substantive findings: [].
