---
title: "K2522 Redshift drift supplies the weak cosmology input"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or empirical certification
scripts:
  - tests/channel-swings/k2522_redshift_drift_interface_probe.py
---

# K2522 Redshift drift supplies the weak cosmology input

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
result: K2522
carrier: comoving Jordan FLRW sources observed on two nearby past lightcones and K2367 homogeneous metric history LAYER=toy CHIRALITY=N/A
pairing: observer proper-time spectral differences, absolute distances and compact weak windows ON=declared_carrier
real_structure: positive real expansion and real common calibration
grading: measured drift, supplied systematic bands, conditional dynamics and empirical evidence are separate
action_owner: repository-construction -- inherited sourced quadratic metric action with conserved dust and photons
target: drift-to-expansion measurement map and its uncertainty-calibrated weak consumer MAP-TYPE=evaluation
```

## Result and scope

[K2520](k2520-nonlinear-observation-null-2026-11-02.md) needs a controlled first distance derivative. Repeated spectral observations provide a different physical input: redshift drift determines expansion once one shared H0 is fixed. We derive finite-baseline and continuous-band requirements, identify H0 with an absolute distance, and propagate their errors into K2520's actual augmented window matrix. The same fitted K2367 member supplies a numerical drift forecast and an exact local sign control without refitting.

This is a conditional measurement construction, not data analysis or a native GU prediction. SC-COS-50/51/54 ASSERTS and LT-GR2e NEEDS remain unchanged; no bridge to native connection displacement is supplied. The standard drift identity is known; our contribution is its explicit composition with the existing sourced weak test and calibration obligations. No novelty claim is made.

## 1. Two lightcones, one clock

For a fixed comoving emitter and observer in FLRW, radial null propagation gives int_te^to dt/a(t)=chi_s. Differentiate with respect to observer proper time to:

    dte/dto=ae/ao=1/(1+z),   1+z=ao/ae,
    g(z)=dz/dto=(1+z)H0-H(z).                         (1)

The H0 and H(z) are evaluated at the observation and emission epochs on the reference lightcone. Repeated observations follow the SAME source; they do not compare unrelated sources selected at two redshifts. Equation(1) needs metric photon propagation and comoving clocks, not a gravitational equation. It is the standard [Loeb drift relation, Section2](https://arxiv.org/pdf/astro-ph/9802122). The spectroscopic velocity convention is dv/dto=c_light g/(1+z), not c_light g. No present-day instrument sensitivity is inferred from the historical proposal.

In fixed K2367 units, g*=g/H*, h=H/H*, h0=H0/H*, reduced distance chi*=H*chi_phys (c_light=1):

    h(z)=(1+z)h0-g*(z),   r=dchi*/dz=1/h(z)>0.      (2)

This bypasses numerical differentiation of distance data. It does not make peculiar accelerations, spectral calibration, source variability or time standards disappear. [Uzan, Bernardeau and Mellier](https://arxiv.org/abs/0711.1950) derive perturbative acceleration contributions. A physical application must supply their residual error/covariance or a justified joint band; averaging is not by itself a bound. Spatial flatness is required for the distance integral below, as in K2518/K2520; the drift identity alone is more general.

## 2. Finite observations and a continuous-band boundary

For an observer-time interval T, endpoint redshift errors e0,e1, and a justified bound |d²z/dto²|<=M2 on that same source track,

    |(zhat(to+T)-zhat(to))/T-g(to)|
      <=(e0+e1)/T+M2 T/2.                            (3)

For centered observations at to±T/2 and |d³z/dto³|<=M3 the last term is M3 T²/24. Integral Taylor remainders prove both bounds. Add clock, redshift assignment and acceleration/calibration errors explicitly in compatible units. A stochastic version needs simultaneous coverage and correlations, not assumed independent shells.

There is a real baseline tradeoff. If e=e0+e1>0 and M2,M3>0 are constant inputs, the forward bound is minimized at T=sqrt(2e/M2), with minimum sqrt(2eM2). The centered bound is minimized at T=(12e/M3)^(1/3), with minimum 3e/(2T). If e=0 the bound favors the smallest available T; if the relevant derivative bound is zero and e>0 it favors the largest available T; if both vanish the displayed bound is zero. These optima apply only within the time range over which the error inputs hold, and are not observing-time recommendations without those inputs.

A finite redshift sample still needs between-node control. With a separately justified Lipschitz constant Lg for g*(z), node error E and mesh covering radius d, nearest-node reconstruction has error <=E+Lg d (plus Lg times redshift-location error). A smooth polynomial bump zero at all nodes disproves a continuous-band inference without regularity. Thus the new interface removes the distance-derivative burden, not all reconstruction assumptions.

## 3. Released absolute-distance calibration

Use physical units here. A consistent homogeneous drift has g(0)=0; an input band must admit that condition. Given such a drift function g and a candidate q=H0 with (1+u)q-g(u)>0 on [0,z*], one absolute reduced distance C=D_L(z*)/(1+z*) obeys

    F(q)=int_0^z* du/[(1+u)q-g(u)]=C,
    F'(q)=-int_0^z* (1+u)/[(1+u)q-g(u)]² du < 0.    (4)

For z*>0, continuity and an endpoint bracket give existence and strict monotonicity gives uniqueness. For joint bands g-<=g<=g+ and C-<=C<=C+, define F- using g- and F+ using g+. Wherever every denominator is positive, every admissible q satisfies

    F-(q)<=C+,   F+(q)>=C-.                          (5)

These decreasing inequalities give an OUTER interval, not a sufficiency theorem for an arbitrary shared functional error model. Intersect constraints from additional anchors using the same q and band realization; independent per-anchor fits invalidate the shared test. Integration error also needs a bound in a real implementation.

An explicit outer-band algebraic control takes g±=±epsilon(1+z), z*=1, and C±=log(2)/(1∓d), 0<d<1. Equation(5) gives q in [1-d-epsilon,1+d+epsilon] on the positive-denominator domain. The envelope functions themselves need not be attainable physical histories (they do not vanish at z=0); this is not a physically sharp interval assertion. With exact zero drift and C=log(2), q=1. If instead only d_obs=A C is known with free positive A, any q can fit by A=d_obs/F(q). For zero drift all relative-distance ratios are log(1+zi)/log(1+zj), independent of q. Relative candles therefore do not universally identify H0. A laboratory time scale measures physical drift but does not provide the missing absolute distance by itself.

## 4. Actual sourced weak consumer

With s=3log(1+z), write K2520's augmented row in h:

    [ int phi h^(-1/2)/36,
     -int phi h^(-5/2)/216,
     -int phi exp(s)h^(-5/2)/108,
      int (phi_ss+phi_s)h^(3/2) ] ds.                 (6)

Every row annihilates (alpha,rho,q0,1) for an admitted same-coefficient history. Let nominal and all allowed h lie in [a,b], a>0, and eta(s)=(1+z)delta_h0+delta_g*(s). The mean-value theorem bounds the row-sum matrix error by

    int eta [ |phi|/(72a^(3/2))
             +5|phi|/(432a^(7/2))
             +5exp(s)|phi|/(216a^(7/2))
             +(3/2)|phi_ss+phi_s|sqrt(b) ] ds.        (7)

For a square four-window nominal augmented matrix W, ||W^-1||_infinity times the maximum row bound strictly below1 ensures every allowed matrix is invertible. Therefore no shared coefficients solve the weak equations for any allowed history. The common h0 remains ONE nuisance throughout all rows. This imports K2520's perturbation criterion, not a new inverse theorem. It is sufficient, may be very conservative, and is not achieved measurement precision. If h0 has no usable band, testing one nominal value cannot exclude the whole nuisance family.

### Executed sufficient precision for the existing witness

For K2520's coasting nominal h=t², t=exp(s/6) in [1,6/5], use exactly its four windows phi_j=t^(6+j)(t-1)²(6/5-t)². Let Phi_j be the sum of absolute polynomial coefficients times (6/5)^degree for phi_j, and Psi_j the same bound for phi_ss+phi_s. With eta<=1/2 all allowed h lie in [1/2,2]. Since the s interval is at most6/5, each row error is at most B_j eta, where the rational bound is

    B_j=(6/5)[Phi_j/24+5Phi_j/36
              +5(6/5)^6 Phi_j/18+9Psi_j/4].

The probe uses the ACTUAL inherited augmented matrix W and computes

    eta_star=min(1/2, 1/[2||W^-1||_infinity max_j B_j])
            approximately 4.36897624e-19.

This exact rational sufficient tolerance gives a half-margin in the inverse criterion. One split is delta_h0<=eta_star/[2(6/5)²] and uniform delta_g*<=eta_star/2. It tests the full shared-calibration consumer. The very small number exposes a conservative, ill-conditioned certificate; it is NOT a necessary precision, a survey forecast or proof that another choice of windows cannot work. Polynomial coefficient bounds sacrifice cancellations. Rebalancing/orthogonalizing windows and tighter integral bounds may improve it; actual band ownership remains separate.

### Executed follow-through: normalize the same tests and certify cancellations

The first bound wastes polynomial cancellations. We therefore use the SAME four-dimensional test span, not a fresh fit: let A=W^-1 and replace the vector of windows by psi=A phi. At the nominal coasting history the actual augmented integral matrix is exactly I. The probe independently integrates all16 entries to verify this, including the twice-integrated derivative column; it does not only multiply stored matrices.

For each new window and psi_ss+psi_s, set t=1+y/5, 0<=y<=1. If p(y)=sum c_i y^i has degree n, its exact Bernstein coefficients are b_k=sum_(i<=k) c_i binom(k,i)/binom(n,i). The identity p=sum b_k binom(n,k)y^k(1-y)^(n-k) proves |p|<=max|b_k| because these basis weights are nonnegative and sum to1. All eight identities are reconstructed exactly. Use these bounds as Phi and Psi in the same rational B formula.

The sufficient uniform h-error tolerance becomes approximately **3.30264588738e-10**, with an exact rational value and all coefficient banks saved in the report. The matrix perturbation margin remains at most1/2; the h0/drift error split uses this improved eta in the same formula. An invertible row recombination preserves the common-coefficient equations and adds no information; the gain is a sharper certified uncertainty calculation in that test span. It is still a sufficient bound, not an optimal tolerance or an achieved physical accuracy. No coefficient refit, new data, physical unit calibration or observation-systematic bound has been introduced.

## 5. Same-model controls and next physical decision

For K2367's unchanged rounded fit, U_s=p, h=U^(2/3), U0=2, p0=.3175541986. Then g*(0)=0 and

    dg*/dz(0)=U0^(-1/3)(U0-2p0)>0.                  (8)

This exact statement for the declared rounded inputs proves positive drift on some sufficiently small positive interval. The probe also integrates the original U,p system with two methods to z=2.33 and reports drift and dv/d(H*to)/c_light at explicit redshifts. These are floating-point forecasts in H* units, not continuum error-certified signs or physical cm/s predictions. Fitting BAO supplied H* r_d; it did not separately determine H* or r_d.

Identically zero drift on any open redshift interval forces h=h0(1+z), U=h0^(3/2)exp(s/2). K2520's independent-exponential and exact four-window witness already excludes that coasting shape for EVERY constant alpha,rho,q0 after scaling. We reuse it by dependency hash rather than count it as a new theorem. An isolated drift zero is permitted; this is not a no-zero-crossings result.

The remaining physical decision is whether a specified redshift-drift program and calibrated distance anchor provide bands tight enough for (7), with acceleration and interpolation control. No dataset, survey feasibility, empirical falsification, native GU forecast or nonzero-mode/slip access has been supplied. If those bands are too wide, use an explicitly different observation configuration rather than treating the geometric drift identity as an action test by itself.
