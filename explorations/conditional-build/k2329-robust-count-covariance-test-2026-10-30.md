---
title: "K2329 Robust count covariance and calibrated finite-data witnesses"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no empirical, hardware or native GU acceptance
scripts:
  - tests/channel-swings/k2329_robust_count_covariance_test_probe.py
---

# K2329 Robust count covariance and calibrated finite-data witnesses

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
result: K2329
carrier: finite real Gaussian full-count windows sharing one constrained scalar seed LAYER=toy CHIRALITY=N/A
pairing: positive covariance and Frobenius/operator matrix norms ON=declared_carrier
real_structure: real covariance or complex adjoint as explicitly declared
grading: linear scalar perturbations, sky harmonics and radial spectral templates
action_owner: repository-construction -- K2311 action with K2325 observation and separately supplied seed/noise
target: certified covariance margins and finite-sample discrimination MAP-TYPE=evaluation
```

## Result and scope

[K2327](k2327-constrained-seed-likelihood-2026-10-30.md) supplies exact population covariance cones. This note makes the test robust to certified numerical error and finite Gaussian samples, then removes a bounded-amplitude assumption through a trace-calibrated repair. It also reduces the actual [K2325](k2325-relativistic-count-covariance-2026-10-30.md) full-count operator to radial harmonic kernels, so numerical accuracy has a precise consumer.

This retains the SAME designer dust-scalar model and count operator. Windows, spectral templates, known Gaussian noise and replication structure are supplied. No survey covariance matrix has been evaluated here. Exact matrix fixtures below are controls, not cosmological forecasts. SC-ACT-01/GEO-55/COS-50/51/54 remain ASSERTS; SC-META-53 remains UNCERTAIN. Ledger0.263 LT-GR2e/GR6b/SM8 and native GU verdicts are unchanged. Positive Gaussian probabilities are imported conventional structures. This is a conditional statistical result, without empirical rejection, physical seed selection or novelty.

## Actual harmonic reduction and numerical-error interface

Use real L2-normalized spherical harmonics Y_Lm, L>=2, and real smooth compact-annular weights w_i=F_i(r)Y_Lm(n)/r². Keep K2325's coordinate-event observer. Isotropy and the plane-wave identity yield

    B_i(k)=4pi i^L Y_Lm(khat) b_i(k).

Let j=j_L(kr), with j' and j'' derivatives in its argument. All source transfers below are evaluated at the background emission time eta_o-r. T_v is K2311's Einstein-frame velocity potential: V_r=i k.mu T_v/a_E. Write a=a_E, Hc=a_J'/a_J, A=dot Hc/Hc²+2/(r Hc), W=Phi_J+Psi_J. A dot means conformal partial time, not a derivative along the cone. Direct substitution into K2325(4), before integration by parts, gives

    b_i(k)=integral F_i(r) {
      [T_nJ+dot T_PsiJ/Hc+(1+A)T_PhiJ-2T_PsiJ] j_L(kr)
      -k² T_v/(a Hc) j_L''(kr) -A k T_v/a j_L'(kr)
      +integral_0^r [A(r) dot T_W(s)
          +(2/r+L(L+1)(r-s)/(rs))T_W(s)] j_L(ks) ds
    } dr.                                                     (1)

Indeed the angular integral of i mu exp(ix mu) is the derivative of the plane-wave integral; that of mu² is its negative second derivative. The radial spatial derivative in the redshift-space term does not differentiate the time-dependent transfer. The angular Laplacian contributes -L(L+1), and the count's negative lens integral reverses that sign. Observer scalar/dipole terms vanish at every finite spectral cutoff for L>=2. Near s=0, j_L(ks)=O(s^L), so the displayed1/s kernel is integrable. The inherited P4 estimates justify the weighted covariance limit. No pointwise white-noise observer field is assumed.

For a nonnegative radial template f_l<=C_l P4 (or with a separately proved finite covariance), the common-harmonic covariance is

    (M_l)_ij=16pi² integral_0^infinity f_l(k) k² b_i(k)b_j(k) dk. (2)

Distinct (L,m) sectors have zero cross covariance under isotropic seed and rotationally invariant dynamics; the noise must also be specified if independence is claimed. This is an exact reduction of the actual operator, not the replacement of its transfer by an arbitrary matrix.

For computation absorb the factor4pi and radial measure into a vector-valued L2 space. If an approximation Bhat to B obeys ||B-Bhat||_L2(f)<=eta and ||Bhat||_L2(f)<=K, then

    ||M-Mhat||_F <= 2K eta+eta².                              (3)

Proof: expand BB*−Bhat Bhat*, use ||uv*||F=||u|| ||v|| and Cauchy-Schwarz. A rigorously bounded omitted tail contributes its trace integral as a Frobenius bound. Hence neither positive quadrature weights nor two close meshes establish (3): the ODE transfer, radial quadrature, spectral quadrature and tail each require a bound. Compact spectral templates eliminate the last tail only for that explicitly restricted statistical model. Equation(1) is ready for such integration; this work does not claim it has been performed.

## Robust population witness with bounded powers

Fix known noise N0>0, matrices M_l>=0, powers0<=p_l<=U_l and Sigma=N0+sum p_l M_l. Suppose certified real symmetric approximations obey ||M_l−Mhat_l||F<=eps_l. Fix a symmetric witness H before observing the testing data. Define

    c_l=tr(H Mhat_l)−||H||F eps_l,
    L0=sum_l U_l min(c_l,0),
    V=||N0||op+sum_l U_l (||Mhat_l||op+eps_l).                (4)

Then tr[H(Sigma−N0)]>=L0 and ||Sigma||op<=V. These follow by duality of the Frobenius norm, nonnegative powers and the operator triangle inequality. Mhat need not be PSD; the true matrices do. Uniform bounds over all admitted tracer/response nuisances produce a uniform test; checking one fitted nuisance value does not.

For n independent centered Gaussian readout vectors y_j with common Sigma, use the uncentered second moment Shat=n^-1 sum y_j y_j^T (the mean is known zero). Set Qhat=tr[H(Shat−N0)] and a=sqrt(t/n). A valid one-sided test rejects the declared null family if

    Qhat < L0−r,   r=2V||H||F a+2V||H||op a².               (5)

Its false-rejection probability is at most exp(-t). This is a calibrated statement about the supplied experiment, not measured evidence.

For completeness, diagonalize A_S=Sigma^(1/2) H Sigma^(1/2). For Z=g^T A_S g−tr A_S and |s|<1/(2||A_S||op), the Gaussian integral and power series give

    log E exp(sZ)=sum_i[-s lambda_i−(1/2)log(1−2s lambda_i)]
       <= s²||A_S||F²/(1−2|s| ||A_S||op).

Sum independent copies and apply Chernoff to either sign. Each one-sided deviation exceeds 2||A_S||F sqrt(t/n)+2||A_S||op t/n with probability at most exp(-t). The bounds ||A_S||F<=V||H||F and ||A_S||op<=V||H||op prove(5), including indefinite H. The Gaussian quadratic-form method is established prior art; [Hsu, Kakade and Zhang](https://arxiv.org/abs/1110.2842) give the related PSD/subgaussian theorem. We derive the signed Gaussian form here instead of exporting the PSD theorem to indefinite H without proof.

A supplied alternative with mean witness mu_A<L0 and covariance norm bounded by V_A is rejected with probability at least1−exp(-t_A) whenever

    L0−mu_A > r_null(t)+r_alt(t_A).                          (6)

This quantifies required numerical tolerance and sample size before spending computation on additional digits.

## Executable matrix control and its exact margin

Use N0=I2, null generators v1v1^T,v2v2^T with v1=(0,1), v2=(1,-1), and H=[[0,-1/2],[-1/2,0]]. Allow powers in[0,2] and certified matrix errors eps_l=1/100. Conservative bounds ||H||F<=1, ||H||op=1/2 give L0>=−1/50 and V<=8. Alternative S_A=[[1,1],[1,2]] has mu_A=−1 and ||I+S_A||op<8. At n=10000 and t=t_A=4,

    r_null=r_alt<=202/625,
    L0−mu_A>=49/50 > 404/625.

Thus (5) has type-I error<=e^-4 and power>=1−e^-4 for this exact finite control, even under the declared null matrix uncertainty. No Monte Carlo frequency is used to certify these probabilities. Reversing cross covariance changes the result while keeping both diagonal entries identical; dropping cross terms destroys the distinguishing information.

## Unbounded powers: counterexample and trace-calibrated repair

Without bounded powers, a fixed absolute threshold is invalid. For the null cone generated by I2 and H=diag(1,-1), Sigma=(1+p)I2 gives mean witness0 but fluctuations proportional to1+p. For any fixed negative threshold its lower-tail probability tends to1/2 as p grows, at every fixed positive integer n. This follows from the continuous symmetric difference of independent chi-squares; arbitrary unknown amplitude cannot be hidden in a fixed V.

First obtain a robust dual K with tr(KM_l)>=0 for every admitted true generator. If certified trace lower bounds tau_l>0 are available, (4) supplies one repair:

    rho=max_l max(0,−c_l/tau_l),  K=H+rho I.                 (7)

Then tr(KM_l)>=c_l+rho tau_l>=0 at all amplitudes. Zero generators may be discarded only when proven zero; an interval containing zero supplies no positive tau. The repair may eliminate useful alternative separation, which must be retested. For the control above tau_l=49/50 is valid, rho=1/98 works, and tr(K S_A)=−95/98<0. This survives the repair; a sufficiently large shift would not.

Now powers may be arbitrary nonnegative finite values. Let QK=tr[K(Shat−N0)], T=tr Shat, a=sqrt(t/n)<1/2. Reject if

    QK < −2||K||op (a+a²) T/(1−2a).                         (8)

False rejection is at most2exp(-t). To prove it, write s0=tr Sigma. The signed quadratic-form lower tail is bounded by2s0||K||op(a+a²), since both required norms are at most s0||K||op. For s>=0, the positive-eigenvalue Gaussian integral gives log E exp[-s(T−s0)]<=s²||Sigma||F²/n, using log(1+x)>=x−x²/2 for x>=0. Chernoff yields T>=s0−2||Sigma||F a and hence the positive trace lower-tail bound gives T>=(1−2a)s0 except on probability exp(-t). Combine these two ONE-SIDED events and tr[K(Sigma−N0)]>=0. No independence between T and QK is used. For level alpha choose t=log(2/alpha) and n>4t. This test is conservative, but for any fixed negative alternative witness it is consistent: T tends to finite tr Sigma and its threshold tends to0.

## Data and acceptance boundary

The n vectors must be independent realizations with the stated covariance. Multiple correlated windows on one sky form ONE vector; repeated noise reads of the same sky do not replicate its seed. Full-sky real harmonic components can provide independent Gaussian replicates only when rotational symmetry, identical radial windows/covariance and noise actually justify it. A cut sky, mask or anisotropic noise changes that covariance. Unknown means, Poisson counts, fitted noise and correlated realizations require new calibration. No fictitious10000 skies are inferred from10000 observed objects.

H/K must be frozen independently of testing data. An independent training split is permissible; a finite prespecified bank of J witnesses, with data selecting among them, needs a simultaneous bound (e.g. replace alpha by alpha/J). Continuously optimizing a witness on the test sample invalidates the stated level without additional uniform analysis.

The probe checks exact angular derivative/sign and harmonic normalization controls, matrix-error algebra, robust margins, both calibrations and genuine changed-input faults. The general continuum and probability statements rest on the proofs. Next integrate(1) with certified transfer/window errors and actual allowed spectral/tracer/noise models, or supply real replication before empirical inference. Neither a cone picture nor this calibration invents those inputs.
