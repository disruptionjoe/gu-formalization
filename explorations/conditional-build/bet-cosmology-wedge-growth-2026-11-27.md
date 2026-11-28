---
title: Wedge scalar growth is Hubble-scale and reference-dependent
status: exploration
doc_type: structural-result
created: '2026-11-27'
program_target: BET-COSMOLOGY
tier: T2
expected_delta: Quantify growth relative to expansion and assess signed or trace-contour references without adopting a completion
actual_delta: Exact growth-to-Hubble interval, slow-growth moment condition and scalar response correlation; signed reference is a formal scalar-stable countercontrol, while trace-only contour does not supply a finite native reduction
class_covered: Previously reviewed leading local four-dimensional wedge metric action with constant positive finite conformal moments; separately declared signed finite moment functional and holomorphic scale-contour controls
premises:
- explorations/conditional-build/wedge-shiab-einstein-reduction-2026-11-27.md
- explorations/conditional-build/natural-density-fibre-volume-2026-11-25.md
- lab/sources/source-claim-register.yaml#SC-COS-50
- lab/sources/source-claim-register.yaml#SC-COS-51
- lab/sources/source-claim-register.yaml#SC-COS-52
source_bridge:
  status: conditional
  reason: The source asserts an automatic dark-energy identity and adjoint one-form mechanism; it does not select this reduced metric action, reference moments, physical state or cosmological history
kill_condition: A failed coefficient, constraint or normalization transfer withdraws the affected comparison; no bet-wide or source verdict follows
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
matrix_or_ledger_effect: none; LC evidence only
---

# Wedge growth, trace contours and the dark-energy comparison

program_target: BET-COSMOLOGY
tier: T2
expected_delta: Decide whether the admitted scalar growth is necessarily fast and whether the proposed reference prescriptions supply a finite scalar-stable reduction.
actual_delta: Growth is at most0.84970H and can be arbitrarily slow; slowing depends on reference spread, not kappa. Formal signed moments can reverse scalar stability, but trace-only rotation does not resolve the native reduction.

Basis `e10ee88b801ee1fc877936080c68ea84ca872f60`; Joe27y considered within the mandatory LC slot at counter119. This is a bounded application of the accepted wedge theorem, not a fourth wave of branch construction or an LC result imported into the matrix.

| State | Result and ceiling |
|---|---|
| **ESTABLISHED** | The declared positive-reference leading4D model has a nonzero Einstein coefficient, a positive-Lambda de Sitter solution and a real growing scalar mode. Its exact dimensionless growth rate is calculated below. |
| **ESTABLISHED, conditional comparison** | A finite signed reference has a healthy linear scalar mass and positiveLambda in the same formal reduction. This changes the positive-measure premise and does not settle spin2 or full physical stability. |
| **RULED OUT by reused scope** | Trace-only scale rotation with the unchanged invariant real shape domain as a source of finite full-fibre absolute mass. This is not a no-go for general oscillatory or complex-cycle prescriptions. |
| **NOT MODELED / UNDETERMINED** | A finite nativeK95 reduction, K77 action transfer, source-selected reference/state, physical Newton normalization, full nonlinear14D evolution, observed dark-energy w(z), CMB/DESI consistency. |

```gu-typed-objects
result: conditional scalar growth and reference-prescription applicability
carrier: leading reduced Lorentz metric on X4 and separately declared moment functionals on the conformal fibre ray LAYER=observed CHIRALITY=N/A
pairing: native K95 indefinite contractions retained; positive, signed and holomorphic reference functionals kept distinct ON=bosonic_metric_and_fibre_moments
real_structure: real (-+++) metric for growth; explicit complex scale only in contour control; no K77 or W2 transfer
grading: derivative and perturbation order; not physical chirality or generation count
action_owner: repository-construction -- reviewed GU* own-wedge leading metric reduction
target: growth relative to expansion and finite-reference burden MAP-TYPE=contraction
```

> **GU-COMPARATOR-ROUTING:** scalaron, effective-fluid and GHP comparisons bind their named reduced or conventional constructions. They do not identify the source's adjoint one-form with a scalar field or establish the source-native observation/stress map. No prescription below is adopted. [Routing](../../lab/methods/source-native-comparator-routing.md).

## 1. Reuse boundary and source footing

The [accepted reduction](wedge-shiab-einstein-reduction-2026-11-27.md) owns the actual connection-metric cross-term, measure normalization, full scalar metric row and independent FLRW constraints. It gives, for h=1/kappa,

    S4 = integral vol_g [AQ Ric² + (5/2)AQ R² + AR R + A0],
    AQ=h m0/2, AR=-99h m1/4, A0=2115h m2/16,
    m_j=integral a^j dlambda(a), a>0,
    m0>0, m1>0, m1²<=m0m2<infinity.

The positive finite measure is a conditional metric-only reference, not an automatic physics default. Native pseudo-Riemannian volume is positive and infinite; its negative trace contraction is already included. The full14D action, the original fixed regulator, a moving reference and the leading4D action are not interchangeable.

SC-COS-50 is the source's conditional continuing-DESI/automatic-identity statement (TOE2025 02:14:44, continuation02:15:25–02:16:02). SC-COS-51 is its adjoint-one-form replacement at02:22:20–02:23:28. SC-COS-52 is the UCSD2025 seminar at00:02:05, completed00:25:56–00:27:00. Their ASSERTS polarity does not select the moment law, a reduced scalar stress, or its initial data. The source bridge therefore remains conditional.

The native wedge own-action fidelity cost also remains: its corrected equation differs from the printed unit endpoint. The source and GU* tracks are retained separately. No further action is constructed here.

## 2. Exact instability rate relative to expansion

The admitted de Sitter background and scalar equation are

    Lambda=235m2/(88m1), H²=Lambda/3=235m2/(264m1),
    m_s²=-99m1/(34m0),
    deltaR=amplitude exp(r t), r²+3Hr+m_s²=0.

Define the dimensionless moment ratio and mass ratio

    z=m1²/(m0m2), 0<z<=1,
    chi=|m_s²|/H²=(13068/3995)z.

Then the growing root satisfies

    x=r/H=(sqrt(9+4chi)-3)/2,
    0<x<=x_max<0.85,
    x_max=(sqrt(88227/3995)-3)/2 = 0.849699738493... .

The maximum is attained by a single conformal scale (equality in the moment cone). Every rate in the exact interval (0,x_max] occurs because the accepted moment cone is complete. The perturbation e-folding time obeys

    tau_growth/(H^-1) = H/r >=1.17688632195... .

This is a homogeneous long-wavelength linear instability on the specified de Sitter solution. It is not arbitrarily fast high-frequency growth, a finite-loss well-posedness failure, or proof of nonlinear runaway. Conversely a rate of orderH can still change a background substantially over cosmological times; the linear mode does not prove that its endpoint is acceptable.

Neither h nor a common rescaling of the fibre ratio changes x. Large kappa or changing a common dimensional reference cannot slow this instability **relative to H** at this leading order.

### What makes growth slow

Normalize lambda/m0 and let its coefficient of variation satisfy

    CV² = m0m2/m1²-1 = 1/z-1.

For epsilon>0,

    x<=epsilon  iff  z<= (3995/13068)epsilon(epsilon+3)
                iff  CV²>=13068/[3995epsilon(epsilon+3)]-1.

A negative right-hand side is automatically satisfied. Examples:

- x<=0.1 requires z<=24769/261360≈0.09477, hence CV²>=236591/24769≈9.552.
- x<=0.01 requires z<=240499/26136000≈0.009202, hence CV²>=25895501/240499≈107.67.

Thus arbitrary slow growth is possible, but its rate is controlled by an unselected reference-shape quantity. Even m0=m2=1 does not fix it: atoms at t and1/t with weights1/(1+t²) andt²/(1+t²) give m1=2t/(1+t²)→0 as t→0.

A bounded-support condition would be a useful additional discriminator. If a∈[a_min,a_max], K=a_max/a_min, then

    z>=4K/(1+K)².

To prove it, put mu=E[a], q=E[a²]. The pointwise inequality(a-a_min)(a-a_max)<=0 gives q<=(a_min+a_max)mu-a_min a_max. Completing the square gives4a_min a_max q<=(a_min+a_max)²mu². Endpoint weights a_max/(a_min+a_max),a_min/(a_min+a_max) attain equality. There is currently no source-supplied support-width bound; none is imposed.

## 3. What actually evolves: curvature, expansion and the response coefficient

For the same pure growing mode define E=deltaR/(12H²). Reusing the full Friedmann and acceleration constraints gives, to first perturbative order,

    deltaH/H=2E/(x+4),
    w_kin+1 := -2 delta(dotH)/(3H²) = -4xE/[3(x+4)].

This w_kin is a kinematic expansion diagnostic. It is a total-fluid parameter only after a GR-style rewriting, and it is not automatically physical dark-energy w_DE.

The amplitude E can have either sign. Therefore the same growing solution family can move the kinematic quantity to either side of-1. Being close to-1 can mean merely a small initial amplitude; it does not establish slow x or select a cosmological history.

Write b=17AQ/6, f(R)=AR R+bR²+A0, and F=f'(R). The background F0 and perturbation satisfy

    F0=3f'' H²(4-chi),
    deltaF/F0=4E/[(1-x)(x+4)] = 2(deltaH/H)/(1-x),
    w_kin+1=-(1-x)alpha_F/3,
    alpha_F=(1/H)d(deltaF/F0)/dt.

This is a correlated consequence of the specified reduced equations: changing expansion through this mode also changes its f(R)-sector response coefficient. If one **additionally** uses the proxy G_F proportional to1/F, then

    w_kin+1=(1-x) dotG_F/(3H G_F).

The action contains Weyl-squared as well as f(R); F alone is not an authenticated measured Newton constant or complete graviton pole residue. No empirical varying-G bound is applied without that bridge. In the held normalization F0 has signh; h>0 makes it positive in this scalar sector, but does not certify the full physical spectrum.

## 4. Signed and trace-contour tests

### 4a. Trace rotation does not regularize the full native fibre

[Gibbons–Hawking–Perry, NPB138(1978)141–150](https://doi.org/10.1016/0550-3213(78)90161-X) discuss the **Euclidean Einstein-action functional integral**. They rotate the conformal integration contour parallel to the imaginary axis and state one-loop convergence conditional on a positive-action conjecture. Original article text was inspected through its [reproduced primary text](https://www.academia.edu/78754388/Path_integrals_and_the_indefiniteness_of_the_gravitational_action); the publisher endpoint returned403. This is not a theorem giving a finite measure on GU's finite-dimensional Lorentz-metric fibre.

Direct native control: write `y=e^u z` with fixed determinant z. Then `tr(z^-1 dz)=0`, and the vertical metric at lambda=1/2 splits as

`K=-4 du²+tr[(z^-1 dz)²]`.

Rotating only `u=i s` reverses that one trace direction. The real traceless Lorentz-shape sector still has signature(6,3), and its noncompact Lorentz congruence orbits remain. A determinant-one boost preserves u and det z, so the disjoint-boost-translate proof still applies to every nonzero positive invariant smooth shape density on an open shape set. A radial damping factor cannot distinguish these translates. Thus **trace-only rotation with unchanged real shape domain does not produce finite full-fibre absolute mass**.

This reuses `explorations/conditional-build/natural-density-fibre-volume-2026-11-25.md` §5; it does not assert that every complex cycle or oscillatory functional integral diverges. A different shape contour, quotient, oscillatory prescription or noninvariant regulator changes premises and requires its own Jacobian, convergence and covariance proof. The GHP functional variable and this fibre-scale variable are different objects.

### 4b. Signed conformal reference: an explicit scalar-stability countercontrol

Reuse `explorations/conditional-build/wedge-shiab-einstein-reduction-2026-11-27.md` §§2–3,7–8. Extend its linear moment functional, formally, from positive measures on `a>0` to the finite signed reference

`lambda=3 delta_1-2 delta_2`.

Its moments are `(m0,m1,m2)=(1,-1,-5)`; total variation is5. The same constant-coefficient leading reduction gives

`AQ=h/2`, `AR=99h/4`, `A0=-10575h/16`, `beta=5h/4`.

In the fixed `(-+++)`, `R_dS=4Lambda` convention:

`Lambda=-A0/(2AR)=1175/88>0`,

`R0=1175/22`, `H²=1175/264`,

`m_scalar²=AR/(17AQ)=99/34>0`.

Put `f(R)=AR R+(17AQ/6)R²+A0`. Then

`f''=17h/6`, `F0=f'(R0)=11621h/66`.

For h>0, AR, f'' and F0 are all positive; the homogeneous scalar roots have negative real part, since they satisfy `lambda_time²+3H lambda_time+m_scalar²=0`. This is a genuine escape from the **positive-measure scalar-instability theorem**, by violating positivity of the measure. It is not a counterexample within that theorem's class. It supplies no spin2 stability, full ghost clearance, quantum unitarity or source selection.

Normalization cost is substantive: vertical signed mass m0=1, but total fibre-volume factor `N=m2=-5`. The would-be normalized total measure `a² dlambda/N=(-3/5)delta_1+(8/5)delta_2` is still signed, not a probability. Dividing the gravitational action by N flips AR and F0 relative to a fixed matter action; it leaves the vacuum equations unchanged. Conversely leaving the held normalization and h>0 gives the positive f(R)-sector signs above but does not derive physical Newton normalization. The full Weyl-squared sector and matter/current normalization need separate checks. A signed weight is neither a positive classical observer probability nor automatically a consistent quantum integration prescription.

### Signed freedom is a cost, not a selected cure

A second logical countercontrol, lambda=delta1-delta2, has(m0,m1,m2)=(0,-1,-3). It removes both curvature-squared coefficients while retaining AR=99h/4 and Lambda=705/88>0. It is therefore a **formal leading Einstein-plus-Lambda action**, not a positive reference probability or a complete14D construction. Its vertical signed mass is zero; the scalar-mass formula dividing by m0 no longer applies. Higher-h corrections, native field equations, matter normalization and source selection remain untested.

More generally, weights on the three positive points1,2,3 map to(m0,m1,m2) through the Vandermonde matrix with rows(1,1,1),(1,2,3),(1,4,9), determinant2. Arbitrary real moment triples can be obtained if arbitrary signed weights are allowed. This frees the three leading coefficients AQ,AR,A0 (while the internal Ric²:R² ratio remains fixed whenever AQ is nonzero). It shows exactly why choosing a desirable sign is not yet predictive progress. A source-supplied law restricting the weights, or a new falsifiable consequence independent of their selection, is still needed before adoption earns credit.

Finite signed or complex invariant measures of finite total variation do not evade the shape-support statement: their total variation is itself a positive invariant finite measure and therefore has conformal support by the existing theorem. Oscillatory distributions without finite variation are a different class, not silently covered or ruled out.

### 4c. Closed complex-scale control versus open imaginary log scale

Declare only a **formal holomorphic conformal reduction**, analytically continuing the restricted polynomial `a² F_G(ag)=Q_g-(99/2)a R_g+(2115/8)a²`. This chooses the holomorphic volume continuation `a² dVol_g`; an absolute value of a complex determinant is not holomorphic. No full complex metric/spin/Hodge path integral is thereby defined.

On a closed positively oriented circle in C* winding once around0, define

`m_j=(1/(2pi i)) integral a^j da/a`.

Residues give `(m0,m1,m2)=(1,0,0)`. Therefore the leading reduced action retains `(h/2)Q_g` and loses both the Einstein term and the constant term. It does not force a de Sitter scale; pure quadratic constant-curvature vacua are a separate degenerate family. The contour does not pass through a=0, but winding and the chosen holomorphic continuation are extra prescription data. A circle with zero winding gives all three moments zero.

By contrast, the **unweighted open** imaginary log contour `u=u0+i s`, `s in R`, `a=e^u`, has `da/a=i ds`. Its zeroth moment diverges; the higher moments oscillate without an ordinary convergent improper integral. It traverses the same circle repeatedly. A one-period quotient, Cesaro normalization, damping or distributional prescription changes the definition and must be stated. This control does not show that GHP's action-weighted conformal functional integral fails; it shows that merely saying “rotate log scale” does not define these finite moments.


## 5. Cosmological interpretation and data boundary

The result supports **a possible slowly evolving mode of this declared reduced vacuum model**. It does not establish slowly evolving source dark energy or DESI agreement. The [official DESI DR2 index](https://data.desi.lbl.gov/doc/papers/dr2/) lists the [2025 Results II analysis](https://arxiv.org/html/2503.14738v3) and [2026 Results IV update](https://arxiv.org/abs/2607.27410). Their evolving-dark-energy preferences depend on the data combination and cosmological model; the update must not be conflated with the earlier significance range. No numerical likelihood is imported here.

A comparison requires the physical observed metric/time, matter and radiation equations, gravitational normalization, reference/state selection, initial perturbation amplitude, a controlled regime for the leading action and sound-horizon calibration. DESI distances divided by the sound horizon are not direct measurements of deltaR or the vacuum scalar mass. No H(z) history, dark-energy split, crossing history or acoustic calibration has been supplied by this wave. The source's adjoint one-form/current remains a distinct object.

The finite signed witness shows that the scalar sign is not inevitable once positivity is dropped. It does **not** show that a GHP contour gives that signed functional, that full native volume becomes finite, or that the spin2/physical-state problem is solved. The closed scale contour is likewise a formal control and loses the Einstein term. The unchanged-shape trace rotation retains the native absolute-volume burden. These comparisons sharpen required inputs rather than select a repair.

## 6. Choice cost, decision and verification

No reference prescription is adopted. If the signed witness were adopted, it would enter GU* as one new signed-reference structural choice, with at least its selected weights/scales, matter normalization and physical interpretation declared. If a complex contour were adopted, its integration cycle, complex metric/Hodge continuation and convergence prescription would be additional specified data. These costs are alternatives, not summed into W2's historical choice inventory. Neither currently supplies a source-selected prediction.

The existing wedge member remains one declared GU* alternative, and the three-wave wedge budget remains spent. This LC result uses existing geometry and equations; it adds no guessed action or physical state. The bet remains active because neither its CMB/DESI kill criterion nor its success criterion is met. Main-line continuation remains the packet's next uncovered nonlinear-CW mechanism, followed by the retained antilinear/PT, trapped-section and Lambda/comparator tests. A proposal to test an arbitrary next measure is not made the default.

[Probe](../../tests/program-focus/bet_cosmology_wedge_growth_probe.py) and [certificate](../../lab/process/bet-cosmology-wedge-growth-certificates.json) check exact coefficients, rate relation, moment examples, sharp-support algebra, full-mode response correlations, signed normalization, residues and trace/shape split. These37finite checks apply the previously reviewed full-row proof; they do not establish a new14D PDE, physical scalar state, oscillatory path integral or observational fit. No new Lean theorem is claimed; the existing T1 finite growth/sign cores are reused. Independent T2 acceptance is recorded separately.

**Actual delta:** instability is precisely Hubble-scale or slower, with a reference-spread cost and an expansion/response correlation. A signed finite moment control can reverse scalar stability, while trace rotation alone does not provide the native finite reference. No source/ledger/matrix verdict changes; no LC result is absorbed into laneB.
