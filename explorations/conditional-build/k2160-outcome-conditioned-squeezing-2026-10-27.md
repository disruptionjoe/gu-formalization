---
title: "K2160 Outcome-conditioned squeezing lowers fixed-effect detector energy"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed-mode diagonal instrument followed by reported-outcome real squeezes; field energy only
scripts:
  - tests/channel-swings/k2160_outcome_conditioned_squeezing_probe.py
---

# K2160 Outcome-conditioned squeezing lowers fixed-effect detector energy

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2160 exact branch energy and optimal feedback at fixed diagonal effects
carrier: positive scalar-field Fock space, fixed real normalized smooth smear and fixed photon-added signal LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product ON=declared_carrier
real_structure: real smear and real local squeezes Q maps to x_r Q, P maps to P/x_r
grading: occupation n_b; no GU ambient grading
action_owner: repository-construction -- supplied positive free Hamiltonian and local instruments
target: fixed-effect output field-energy minimization MAP-TYPE=intertwiner
```

## Result, scope and changed operation

[K2158](k2158-local-squeezing-detector-energy-2026-10-27.md) solved one common squeeze after a
complete diagonal detector. Allow one deterministic real squeeze **per reported outcome**.
The exact fixed-effect **vacuum output field-energy** optimum separates into strictly convex scalar problems with explicit
branch moments. It is no worse than common squeezing and strictly better exactly when the
nonzero branches have different optimal squeezes. A rational unchanged-ROC detector already
beats the previous certified optimum; optimal branch feedback gives a stronger certified bound.

This is an independent positive-free-field construction, not a GU-derived state, recovery,
source verdict or ledger change. SC-META-53 remains UNCERTAIN about indefinite spectra;
LT-SM8 and LT-GR6b are not discharged by supplying a positive free model. The signal, smear,
Hamiltonian and effects are fixed. No arbitrary local-channel or general Gaussian optimum,
controller work, autonomous stability, preparation or reset cost is claimed. References retain
the same outcome statistics, while the output channel changes.

## 1. Fixed model and unnormalized branch data

Use [K2151](k2151-optimal-local-mode-discrimination-2026-10-27.md) and
[K2153](k2153-diagonal-detector-energy-2026-10-27.md): H=dGamma(omega)>=0, real normalized f,
m_j=<f,omega^j f>, nu=sqrt(m1/m_-1), N=(sqrt(m1*m_-1)-1)/2>0,
z=N/(N+1), s=sqrt(N(N+1)), p_n=(1-z)z^n. The physical signal is the SAME a_h†Omega.
The Schmidt pair b,c has vacuum sqrt(1-z) sum_n z^(n/2)|n,n>, with physical modes
h=sqrt(N+1)b-sqrt(N)c† and j=sqrt(N+1)c-sqrt(N)b†. Write E_h=<h,omega h>,
E_j=<j,omega j>, E_sum=E_h+E_j>0. These are one-particle energies, not oscillator labels.

For binary effects e_r(n)>=0, sum_r e_r(n)=1, first use K_r=sqrt(e_r(n_b)). Define

    w_r = sum_n p_n e_r(n),
    M_r = sum_n n p_n e_r(n),       R_r=M_r+w_r/2,
    T_r = (1-z) sum_n (n+1) z^(n+1/2) sqrt(e_r(n)e_r(n+1)).

These are UNNORMALIZED branch moments: w is probability, M is <n_b>=<n_c>, and T=<bc>.
No conditional thermal-state assumption is made. Cauchy-Schwarz on b†psi and c psi gives
0<=T<=sqrt(M(M+w))<=R. All moments are finite since e<=1 and z<1. A zero-probability
branch vanishes identically and is omitted; no division by zero is used.

Apply U_x after the Kraus, U_x†Q U_x=xQ, U_x†P U_x=P/x, x>0. All full-record effects
remain exactly e_r(n_b), including probabilities for reference-entangled inputs.

## 2. Exact branch field energy

The unnormalized vacuum branch energy after squeezing is

    F_r(x)=a_r x²+b_r x^-2-c_r x+d_r,
    a_r=m2 R_r/(2nu),       b_r=nu R_r/2,
    c_r=2s E_sum T_r,
    d_r=E_h[N M_r+(N-1)w_r/2]
         +E_j[(N+1)M_r+N w_r/2].                         (1)

In particular d_r contains the conditional complement contribution and can be negative;
the total F_r is nonnegative because it is an expectation of H>=0.

Derivation independent of the common-squeeze shortcut: set u=(x+x^-1)/2, v=(x-x^-1)/2.
In the branch, <b†b>=<c†c>=M, <bb†>=<cc†>=M+w, <bc>=T real, and <b²>=<c²>=<b†c>=0.
After transforming b to ub+vb†, the physical number and cross moments are

    Hh=(N+1)(u² M+v²(M+w))+N(M+w)-2s u T,
    Hj=(N+1)M+N(u²(M+w)+v² M)-2s u T,
    Hjcross=(2N+1)v T-s u v(2M+w).

Then F=E_h Hh+E_j Hj+2F_hj Hjcross, where

    E_h=(nu+2m1+m2/nu)/(4(N+1)),
    E_j=(nu-2m1+m2/nu)/(4N),
    s F_hj=(nu-m2/nu)/4,       F_hj(2N+1)=-s E_sum.

Substitution gives (1). This uses the finite two-mode energy quadratic form, not an
assumption that span(h,j) is omega invariant. Smooth f and finite moments put the transformed
vectors in the form domain; finite second moments suffice for the quadratic expectation.
Countably many hidden diagonal Kraus labels are controlled by e<=1 and the same moment sums.
With finitely many reported outcomes and finite x_r the summed form energy is finite.

As a consistency check, sum w=1, sum M=N, E=2E_sum(s²-s sum T).
Thus sum F_r(x) equals K2158's xE+A(x). Applying that unconditional identity to EACH branch
is invalid and loses exactly the feedback advantage.

## 3. Exact optimization at prescribed effects

For every nonzero branch a,b>0 and c>=0. F tends to infinity at both endpoints and

    F''(x)=2a+6b/x^4>0.

The unique minimizer solves 2a x^4-c x^3-2b=0. Therefore

    E_feedback(e)=sum_r min_(x>0) F_r(x).                  (2)

This is an exact fixed-effect optimization, not a solved global optimization over e.
Positive-root Kraus remain optimal even among arbitrary complete countable diagonal
implementations of the SAME reported effects, provided each reported outcome uses one common
squeeze across its hidden labels. w,M,d are fixed; the complex adjacent overlap satisfies
Re sum_alpha f_alpha(n)^*f_alpha(n+1)<=sqrt(e(n)e(n+1)). Its coefficient in the energy is
-2s E_sum x<0. Positive square roots saturate all links simultaneously. Optimizing x does
not reverse this pointwise ordering. Outcome refinement with separate feedback is a different
operation class and must be declared.

Strictness against common squeezing follows without guessing an optimizer:

    sum_r min F_r <= min_x sum_r F_r.

Equality holds iff all nonzero branches have the same unique minimizer, equivalently T_r/R_r
is constant across them. Informative effects alone do not establish strictness. Proportional
constant effects are an equality control and produce no measurement information.

A uniform compact interval also follows. Put C=2s E_sum,
q=(nu²/m2)^(1/4), X=max(1,nu(C+nu)/m2). Then every positive-root optimum lies in [q,X].
Indeed F'/R=(m2/nu)x-nu/x³-C T/R is strictly increasing, nonpositive at q and nonnegative
at X. Cauchy inequalities give m2>=m1²>=m1/m_-1=nu², hence q<=1. This gives an actual
bounded certification interval, not a stopping tolerance. Arbitrary effects still require
their infinite moment sums or rigorous tails; compact squeezes alone do not solve that task.

### Certified evaluation for non-finite effect sequences

For w,M truncated through n=J and T through n=J (so e(J+1) is also supplied), geometric
bounds independent of the effect sequence give

    delta_w <= z^(J+1),
    delta_M <= z^(J+1)(J+1+N),
    delta_T <= sqrt(z) z^(J+1)(J+2+N).

Let A=m2 X²/(2nu)+nu/(2q²), D_M=N E_h+(N+1)E_j and
D_w=((N-1)E_h+N E_j)/2. On the compact squeeze interval, the full and truncated
branch energy functions differ uniformly by at most

    A(delta_M+delta_w/2)+C X delta_T+abs(D_M)delta_M+abs(D_w)delta_w.

The minima OVER [q,X] differ by at most the same bound; summing over two branches gives
twice this safe bound. A truncated function's unconstrained minimizer need not lie in the
interval, so the interval restriction is essential. The true optimizer does lie there.
This certifies evaluation for a supplied infinite effect sequence; it does not solve the
variational optimization over all effects or give apparatus cost.

## 4. Exact threshold witness and certified optimum

Keep the earlier spectral fixture W=diag(1,9,4), f=(1,1,0)/sqrt2. Then
m1=5, m_-1=5/9, m2=41, nu=3, N=1/3, z=1/4, s=2/3, E_h=E_j=5.
Use e0=1_{n=0}, e1=1_{n>=1}. The two branches are

    (w0,M0,T0,R0)=(3/4,0,0,3/8),
    (w1,M1,T1,R1)=(1/4,1/3,7/24,11/24),
    F0(x)=(41x²+9x^-2-10)/16,
    F1(x)=(451x²+99x^-2-560x+370)/144.

Both F_r(1)=5/2. Choosing x0=2/3,x1=1 gives exact total 2465/576<4.28.
The common optimum from K2158 is >4.4289859434858, so this is a strict certified
improvement without numerical optimization. All detection probabilities are unchanged:
alpha=1/4, eta=1, equal-prior error=1/8.

The exact no-click optimum is x0=(9/41)^(1/4), F0*=(3sqrt41-5)/8.
The click optimum is the unique positive root of 451x^4-280x^3-99=0.
The companion probe bisects rational derivative signs for BOTH branches and uses a convex
tangent lower bound and feasible-value upper bound. It certifies

    4.2304967688817322 < E_feedback < 4.2304967688817324.

This interval is for the fixed threshold's optimal two real squeezes; it is not the global
energy-optimal detector or a bound on apparatus resource expenditure. K2154's number-preserving
controller estimate does not transfer to these squeezes.

## Evidence and continuation

Exact symbolic checks independently expand physical two-mode moments and branch formula,
recover common squeezing, test strict-convexity and the equality condition; exact rational
branch sums/certificates and changed inputs/equations test the witness. Full-record finite
unitary tests check ordering only; infinite-domain statements are the written argument above.
Independent internal review is required before acceptance; no novelty, external-expert,
proof-assistant or remote-CI claim.

Next compare the energy-budget frontier over effects in this explicitly enlarged class, or
construct an actual stable controller including switching, preparation and reset. A more general
Gaussian map, hidden-label feedback, a different signal or a different region changes the
question. Repeating common-squeeze optimization or assuming conditional thermal covariance
would not answer it.
