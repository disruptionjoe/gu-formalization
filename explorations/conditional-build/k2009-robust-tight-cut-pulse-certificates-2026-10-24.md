---
title: "K2009: Robust tight-cut and pulse-error certificates"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2009_robust_tight_cut_pulse_certificates.py
  - tests/channel-swings/k2009_robust_tight_cut_pulse_certificates_probe.py
---

# K2009: Robust tight-cut and pulse-error certificates

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
result: quantitative forced-support stability, regional residual bounds and amplitude-aware continuum dual certificates
carrier: actual width9 scalar strip and K1991 tight cuts at the algebraic contact root LAYER=toy CHIRALITY=N/A
pairing: Lebesgue row and column marginals, L1 residuals and real L2 norm ON=actual_characteristic_strip
real_structure: real bounded measurable pulses and bounded dual potentials
grading: forced and three free regions, not source chirality
action_owner: repository-construction -- unchanged scalar transport model
target: honest validation of approximate full-strip and residual-wing constructions MAP-TYPE=intertwiner
```

## 1. What an approximate pulse really certifies

Keep [K1991](k1991-tight-cut-pulse-factorization-2026-10-23.md)'s actual
strip D={-3<=u<=3,u<=z<=u+9}, phase phi, cap M=23/100 and algebraic root
9/20<t<23/50. K1991 proves EXACT factorization at exact marginals and cap.
This note gives quantitative bounds when any of those constraints has error.
It does not construct the global capped wing, repair its marginals, or
replace K2007's exact-feasibility lower bound.

Let v be measurable with |v|<=M+epsilon, epsilon>=0. Its row/column errors are

    e_r(u)=integral v(u,z) dz-2phi(u),
    e_c(z)=integral v(u,z) du,
    eta_r=||e_r||_1, eta_c=||e_c||_1.

Set L=3-t and K=9L-L^2=18-3t-t^2. Define the two cut errors
rho_a=integral_(-3)^a e_r(u)du for a=-t,t, and

    Q=4 epsilon K+|rho_(-t)|+|rho_t|+2 eta_c
      <=4 epsilon K+2 eta_r+2 eta_c.                    (1)

On the forced region F of K1991, write s=+1 or -1 for its forced sign. Then

    ||v-Ms||_(L1(F)) <=Q,
    ||v-Ms||_(L2(F))^2 <=(2M+epsilon)Q.                 (2)

Thus small measured residuals force concentration near the actual saturated
support with an explicit square-root L2 bound. The estimates use integrated
continuum errors, not sampled residuals or averages at a grid's nodes.

## 2. The signed slack identity and the factor of two

For one row cut A_a={u<=a}, let a column have total length ell(z) and cut
length m(z). Let B_a take the cut side with sign +1 when m<=ell/2, and the
complement side with sign -1 otherwise. Its column length is
min(m,ell-m). Put H_a={z:m>ell/2}. Direct subtraction gives

    integral_(B_a) sign_a v
      = integral_(A_a) v - integral_(H_a) e_c(z)dz.

The exact target cut mass is MK, by the actual contact relation. Both cuts
have K=integral min(m,ell-m)dz. Therefore the nonnegative slack satisfies

    integral_(B_a) (M+epsilon-sign_a v)
      =epsilon K-rho_a+integral_(H_a) e_c.              (3)

The pointwise inequality |v-sign_a M|
<=M+epsilon-sign_a v+epsilon gives

    ||v-sign_a M||_(L1(B_a))
      <=2 epsilon K+|rho_a|+eta_c.                     (4)

The two B_a cover F and agree in sign on overlaps. Summing (4) proves (1)
and (2), since |v-Ms|<=2M+epsilon. Double counting an overlap only weakens
the upper bound. Column imbalance cannot be omitted from (3); a constant
pulse on an otherwise balanced two-row column is a direct contrary control.
A cap overshoot is charged twice in (4), once through slack and once through
changing the reference endpoint from M+epsilon back to M.

For completeness, if a cut leaves a shorter row interval of length h<=3,
the left and right triangular column ranges contribute 6h-h^2, and the
middle width3 contributes3h. Hence K=9h-h^2. For a=+-t, h=L. Exact
piecewise-linear column integration in the probe checks this geometry
independently on rational cuts; the contact mass is inherited from K1991.

## 3. Regional residual and cap diagnostics

Replace v by Ms on F, leaving v unchanged on D_L,D_C,D_R, and call the
result v_tilde. This is a diagnostic replacement, not an exact feasible pulse.
It satisfies

    ||v_tilde-v||_1<=Q,
    ||row(v_tilde)-2phi||_1<=eta_r+Q,
    ||column(v_tilde)||_1<=eta_c+Q.                     (5)

After subtracting the exact forced contributions, the SUM of the three
regional row-error L1 norms is at most eta_r+Q, and likewise the sum of
regional column errors is at most eta_c+Q. This uses the disjoint row bands
AND disjoint column ranges in K1991, not an arbitrary partition.
Consequently a supposed full-strip construction with small residuals cannot
hide a large residual-wing error behind changes on the forced support.
It must pay the explicit bound (5). On the free regions the cap is still
M+epsilon. Neither clipping nor K2007's uncapped inverse automatically
preserves both marginals and the original cap.

Equation (3) also detects inconsistency of proposed error budgets. For any
claimed cap C (even C<M), feasibility requires

    (M-C)K <= |rho_a|+eta_c.                            (6)

Thus a measured cap below M is incompatible with certified errors smaller
than this threshold. It is not a new claim about the exact optimal phase.

## 4. Bounded dual potentials price actual constraint errors

Take bounded row potential alpha and column potential beta. Set zeta=alpha+beta,
A=||alpha||_infty, B=||beta||_infty, and

    psi_C(z)= z^2                         if |z|<=C,
              2C|z|-C^2                 otherwise,
    D_M=2 integral alpha(u)2phi(u)du-integral_D psi_M(zeta),
    T=integral_D (|zeta|-M)_+.

D_M is a lower bound on the squared norm for exact M-feasible pulses.
The clipped quadratic conjugate has derivative
partial_C psi_C(z)=2(|z|-C)_+. Thus

    0<=psi_(M+epsilon)(z)-psi_M(z)
       <=2 epsilon (|z|-M)_+.

Fenchel's inequality with the ACTUAL marginals proves

    ||v||_2^2 >= D_M-2A eta_r-2B eta_c-2 epsilon T.      (7)

If D_M is replaced by a certified lower endpoint D_low, the inequality stays
valid. Strong convexity gives a further actual-candidate diagnostic with
w_C=clip(zeta,-C,C):

    ||v-w_C||_2^2
      <=||v||_2^2-D_low+2A eta_r+2B eta_c+2epsilon T.    (8)

This is distance to the specified clipped dual witness. It is NOT distance
to the unknown optimum or to some exactly feasible pulse. If v is exactly
feasible, the ordinary exact feasibility results can be used separately.
Finite L2 potentials without an L-infinity bound do not justify the stated
L1-error prices; either prove boundedness or use a different dual norm.

The report reads K1989's stored 24-row bounded rational witness, recomputes
its actual strip cell areas and its rational D_low, and calculates A,B,T.
It evaluates (7) at explicit cap/row/column error budgets. This is an
actual-model robustness consumer, not a new optimized lower bound. K2007's
stronger 2.361527 regional exact-feasibility lower uses additional exact
regional information and is NOT silently substituted for this global D_low.

## 5. Verification and boundaries

The producer checks exact rational finite-measure cut identities and their
inequalities, all three branches of the conjugate, and actual K1989 geometry
and error prices. The separate probe uses independently coded interval
integration and the pointwise Fenchel identity. Faults change column
balance, cap, potential normalization or triangle area, then must fail an
actual mathematical check after a green baseline. Finite controls verify
formulas and implementation; sections2-4 provide the continuum proof.

Executed producer and full replay:72 rational cut controls,238 pointwise
conjugate/strong-convexity controls and3 actual-witness error budgets. The
separate probe passes72 cut identities,7 continuum geometry integrals and
3 budgets, then rejects4 actual mathematical faults;4 provenance hashes are
separate. At cap, row and column errors each1e-6, the conditional squared-norm
lower is greater than2.34935665865. This number prices the stated errors;
no approximate candidate is asserted to satisfy those budgets.

These bounds resolve a certification question about approximate candidates.
They do not supply a cap-preserving marginal right inverse, convergence
rate for a nonlinear optimizer, or full-wing formula. Same-author internal
checks are not independent specialist or formal acceptance. Source, physics
ledger and canon remain unchanged; the carrier has no GU identification.

Reproduce with `python tests/channel-swings/k2009_robust_tight_cut_pulse_certificates.py --write`,
the same command without `--write`, and
`python tests/channel-swings/k2009_robust_tight_cut_pulse_certificates_probe.py`.
