---
title: "K2162 Global feedback detector frontier and leading weak-signal gain"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed scalar mode, binary diagonal instrument and reported-outcome real squeezes; vacuum field energy only
scripts:
  - tests/channel-swings/k2162_feedback_detector_frontier_probe.py
---

# K2162 Global feedback detector frontier

> **GU-COMPARATOR-ROUTING: scope before inference.** Conventional comparators bind their
> named models only. No GU source or physical recovery follows without a typed bridge.
> Read `lab/methods/source-native-comparator-routing.md` before transferring a result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2162 attained global variational frontier, certified finite approximation, improved attainable weak-budget slope and exact saturation
carrier: fixed positive scalar Fock vacuum and fixed photon-added signal, binary effects of local oscillator occupation LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and global vacuum energy ON=declared_carrier
real_structure: positive square-root Kraus and one real squeeze per reported outcome
grading: occupation n, not source ambient chirality
action_owner: repository-construction: supplied free Hamiltonian, signal and operation class
target: maximum signal-vacuum detection contrast at fixed vacuum output field-energy budget MAP-TYPE=intertwiner
```

## Result and operation class

[K2160](k2160-outcome-conditioned-squeezing-2026-10-27.md) solved prescribed effects.
This result optimizes the effects too: an attained infinite-dimensional frontier has global
finite conic/grid bounds with explicit energy-budget slack. A constructed weak detector
strictly improves the leading small-budget achievable coefficient; no sharp global asymptote
is asserted. The old threshold certificate becomes the EXACT global saturation budget by a
new necessity argument. These are distinct consequences of the global problem.

Keep precisely K2160's binary diagonal instruments with one deterministic real squeeze per
REPORTED outcome, same smear and photon-added signal, and vacuum field output energy.
Positive roots minimize over countably many hidden diagonal Kraus at prescribed effects in
this class, so restricting to them loses nothing. Hidden-label-dependent feedback, randomly
scheduled squeezes, general Gaussian or arbitrary local channels are different classes.
Preparation, switching, controller stability and reset cost remain unaccounted.
SC-META-53 stays UNCERTAIN; LT-SM8 and LT-GR6b are not discharged by an imported positive free
model. Source, ledger, canon and GU recovery remain unchanged. Related fixed-model inputs:
[K2156](k2156-energy-budget-detector-frontier-2026-10-27.md) and
[K2158](k2158-local-squeezing-detector-energy-2026-10-27.md).

## 1. Compact global variational theorem

Use K2160's constants C=2s E_sum, Rbar=N+1/2, q,X and branch energy
F_r(x)=Atilde(x) R_r-C x T_r+d_r,
Atilde(x)=m2 x²/(2nu)+nu/(2x²).
Every branch optimum belongs to [q,X]. Therefore define
V_fb(B)=max {Delta(e): e in [0,1]^N, x0,x1 in [q,X], sum_r F_r(xr)<=B}.
All moment series converge uniformly, hence energy and contrast are continuous in compact product topology. The nonempty feasible set is compact: constant effects and x0=x1=1 give energy0. Consequently the global optimum is attained. Nondecreasing and right-continuous follow; right continuity uses a compact convergent subnet of optimal detectors for B_j decreasing to B. Do NOT infer concavity or left continuity from this proof.

For each FIXED squeeze pair, sum F is convex in e: all R,d terms are affine, while -C*xr*T_r is a negative positive-weight sum of jointly concave geometric means. Hence the fixed-pair finite optimization is SOCP. Minimizing convex functions over squeeze choices does not by itself establish convexity of optimized energy. No claim here that convexity fails: that requires an actual counterexample.

## 2. Exact constant-tail formulas

Fix M>=1, let e_n=e_M for n>=M, and set a_r(n)=e_n for click and 1-e_n for no-click. Put p_n=(1-z)z^n and tau_n=(1-z)(n+1)z^(n+1/2).

w_r=sum_{n=0}^{M-1}p_n a_r(n)+z^M a_r(M).
M_r=sum_{n=0}^{M-1}n p_n a_r(n)+z^M(M+N)a_r(M).
T_r=sum_{n=0}^{M-1}tau_n sqrt(a_r(n)a_r(n+1))
    +sqrt(z) z^M(M+1+N)a_r(M).
R_r=M_r+w_r/2.
Delta=sum_{n=0}^{M-1}(q_n-p_n)e_n+M(1-z)z^(M-1)e_M.

For fixed x0,x1 introduce nonnegative u_n,v_n with u_n²<=e_n e_(n+1), v_n²<=(1-e_n)(1-e_(n+1)); replace the two geometric means by u_n,v_n in the energy. All their energy coefficients are negative. Thus existence of auxiliaries meeting the budget is equivalent to the actual square-root budget, because maximizing each auxiliary lowers energy and its allowed maximum is the exact square root. The remaining tails are linear. This is exact SOCP equivalence, not relaxation.

## 3. Uniform global finite certification, WITH budget slack

Flatten arbitrary e after index M to its e_M. Let
rw=z^(M+1), rm=z^(M+1)(M+1+N), rt=sqrt(z)z^M(M+1+N),
Amax=m2 X²/(2nu)+nu/(2q²),
epsilon_M=Amax(rm+rw/2)+2 C X rt.
Then uniformly over all effects and compact squeeze pairs,
|E(e,x)-E(flatten_M(e),x)|<=epsilon_M.
Proof: |delta w_click|<=rw, |delta M_click|<=rm; no-click differences are negatives; |delta T_r|<=rt since edges n>=M may change. The total d=sum d_r is the same for all complete effects. Thus the R difference contributes (Atilde(x1)-Atilde(x0))*delta R_click. Both Atilde values are positive and at most Amax, giving the stated bound. This avoids a needless factor and d-tail terms.

For M>=floor(N), contrast changes by at most R_M=(M+1)(1-z)z^M (all q_n-p_n beyond M are nonnegative).

A uniform L-infinity Lipschitz constant in the squeeze pair is
H=(m2 X/nu+nu/q³)(N+1/2)+C s.
Indeed |F_r'|<=(m2 X/nu+nu/q³)R_r+C T_r; sum R=N+1/2 and sum T<=s by two-component Cauchy-Schwarz on each adjacent effect pair.

Take a finite grid in [q,X]^2 with covering radius h in max norm. Let W_M,h(B) be the maximum of the finite SOCP optima at its grid points. This is a subset of the allowed operation class, so
W_M,h(B)<=V_fb(B)<=W_M,h(B+epsilon_M+Hh)+R_M.
The upper inequality follows by flattening and rounding any attained infinite optimizer. Define infeasible finite program values carefully (e.g. -infinity); for upper bound the rounded image proves feasibility at the enlarged budget. Add (1,1) to the grid so W(B) is feasible for every B>=0.

These are rigorous global finite certificates. Numerical solver success is not certification: use actual feasible rational/interval lower witnesses and convex tangent/SOCP dual upper bounds at EVERY grid point; maximum of certified upper bounds is a global grid upper bound. Fixed-pair interior tangent proof is exactly K2156's proof with the changed convex energy. There is no justified same-budget additive vertical error or inherited concavity. Right continuity supplies convergence of the enlarged-budget upper envelopes as M->infinity and h->0.

## 4. New small-budget improvement at leading order

This changes the conclusion of COMMON squeezing: reported-outcome feedback improves the leading square-root coefficient, not merely second-order energy.

Let L=m_-1*m2, H0=(3m1+L)/2, D=E_sum*N/(2N+1), a=(1-z)/z, w_edge,n=(n+1)z^(n+1).
Choose bounded real v_n and t in (0,1), set click e_n=t+epsilon v_n for sufficiently small epsilon. Define
w_v=sum p_n v_n, m_v=sum n p_n v_n,
delta=sum(q_n-p_n)v_n=m_v/N-w_v,
J=sum w_edge,n (v_(n+1)-v_n)^2.
The exact contrast is Delta=epsilon delta.

Geometric-mean expansion, uniform because v bounded and t interior:
sqrt((t+epsilon v_n)(t+epsilon v_(n+1)))
=t+epsilon(v_n+v_(n+1))/2-epsilon²(v_(n+1)-v_n)^2/(8t)+O(epsilon³).
Applying also to complement and summing geometric tails gives the diagonal energy
E_diag=epsilon² E_sum J/[4t(1-t)]+O(epsilon³).

At epsilon0 each branch is proportional to vacuum, so F_click=t A(x), F_noclick=(1-t)A(x), with A from K2158; A'(1)=0, A''(1)=H0. The linear derivative of T_click is
T_v=sqrt(z)/2 [w_v+(1+1/z)m_v].
Using L-m1=4N(N+1)E_sum and m1=nu(2N+1),
(d/depsilon) F_click'(1)|0
=(m2/nu-nu)(m_v+w_v/2)-C T_v
= -E_sum(m_v-N w_v)/(2N+1)=-D delta.
The no-click derivative is +D delta. Consequently the implicit-function theorem yields
x_click=1+epsilon D delta/(t H0)+O(epsilon²),
x_noclick=1-epsilon D delta/((1-t)H0)+O(epsilon²).
The first-order click squeeze can EXPAND; no valid blanket restriction x_r<=1 exists for outcome-dependent feedback.

Minimizing the two scalar branches lowers the energy by
 epsilon² D² delta²/(2H0) * [1/t+1/(1-t)]+O(epsilon³).
Thus exactly
E_fb=epsilon²/[4t(1-t)] * [E_sum J-2D² delta²/H0]+O(epsilon³).

The weighted Cauchy inequality delta=a sum w_edge(vnext-v) gives
J>=delta²/(a² S)=z delta², S=z/(1-z)².
Define
kappa=z E_sum-2D²/H0
=z E_sum * [1-(L-m1)/((2N+1)²(3m1+L))].
Since L-m1=4N(N+1)E_sum>0, (2N+1)²>1 and 3m1+L>L-m1>0, we get 0<kappa<z E_sum. This proves positivity of the quadratic coefficient and the strict leading gain.

Take t=1/2 and v_n=min(n,M)-M/2. This is bounded with constant tail. For S_M=sum_{n=0}^{M-1}w_edge,n,
J=S_M, delta=a S_M,
E_fb/Delta² -> kappa_M=E_sum/(a² S_M)-2D²/H0,
and kappa_M decreases to kappa. For each M, the analytic positive energy curve is increasing near epsilon0 and can be inverted. Therefore
liminf_{B downarrow0} V_fb(B)/sqrt(B)>=1/sqrt(kappa_M),
then taking M->infinity proves >=1/sqrt(kappa).
THIS IS AN ACHIEVABLE LIMINF LOWER BOUND, NOT A SHARP GLOBAL ASYMPTOTE. A matching global upper bound would require additional control of rare branches, vanishing t and high-occupation tails.

Fixture m1=5,L=205/9,N=1/3,z=1/4,E_sum=10:
H0=170/9, D=2, kappa=353/170, old common coefficient energy/Delta²=5/2.
Already M=3 gives S3=27/64, delta3=81/64,
kappa3=45652/20655 <5/2,
E_fb=(308151/87040)epsilon²+O(epsilon³),
Delta=(81/64)epsilon.
The exact effect list is e0=1/2-3epsilon/2, e1=1/2-epsilon/2, e2=1/2+epsilon/2, e_n=1/2+3epsilon/2 for n>=3, valid |epsilon|<=1/3. This provides a concrete four-value finite-tail consumer and exact symbolic probe target. Unlike only optimizing the old threshold again, it proves improvement in the weak-information regime.

## 5. Exact endpoint/saturation consumers

For this endpoint use the positive free Hamiltonian with no one-particle zero modes, so
kerH=C Omega (in particular the massive model and the finite positive-frequency fixture).
V_fb(0)=0: H>=0 and kerH=C Omega imply each branch U_x sqrt(e)Omega is scalar Omega. All Schmidt weights are positive, so U_x sqrt(e)=cI. A nonzero positive sqrt(e) can equal a scalar unitary only when e is constant and U_x scalar, hence x=1. Zero branches are omitted. Therefore no information at zero output field energy.

Noninteger N: maximizing unrestricted contrast forces the unique threshold e_n=1_(n>=k), k=floorN+1. Thus its K2160 sum of branch minima is EXACT global saturation budget, not merely a fixed-effect witness. Threshold moments:
w1=z^k, M1=z^k(k+N), T1=sqrt(z)z^k(k+1+N),
w0=1-w1, M0=N-M1,
T0+T1=s-k(1-z)z^(k-1/2).
In fixture N=1/3, K2160's certified 4.2304967688817322..4 interval is consequently the exact global saturation-budget certificate. The full optimal contrast reaches3/4 iff B is at least that energy. Existing artifact wording fixed-effect-only was correct before the global necessity argument; do not overwrite historical scope.

Integer N=ell: unrestricted maximizers retain only tie e_ell=t free. Saturation is the attained min over t in[0,1] and x0,x1 in[q,X]. Do not inherit the old t=1/2 minimizer without proof. Put p_ell=(1-z)z^ell and tau_n as above:
w1=z^(ell+1)+p_ell*t,
M1=z^(ell+1)(ell+1+N)+ell*p_ell*t,
T1=sqrt(z)z^(ell+1)(ell+2+N)+tau_ell*sqrt(t),
T0=sum_{n=0}^{ell-2}tau_n+tau_(ell-1)*sqrt(1-t).
Empty low sum is0; tau_(ell-1)=tau_ell because z=ell/(ell+1).


## 6. Reproducible nonasymptotic consumer and evidence

Use the four-value M=3 effect above at epsilon=1/100, with rational first-order squeezes
x_click=1+epsilon D delta3/(H0/2) and x_noclick=1-epsilon D delta3/(H0/2).
The companion probe evaluates the ACTUAL infinite constant-tail energy with outward256-bit
arithmetic, not the truncated asymptotic series. It compares against the exact lower bound
g(E0)>=E0-E0^2/L, E0=z E_sum Delta^2. Indeed A(1)=A'(1)=0 and
A''(x)=3m1/(2x^4)+L/2>=L/2, hence A(x)>=L(x-1)^2/4; completing the square
in x E0+A(x) gives this bound. Every common-squeeze detector achieving the contrast has
energy at least g(E0), since E_diag>=E0 and g is increasing. The certified actual feedback
energy is0.00035417563756671290593881063264358 (enclosed in the report), below the rational
common lower bound22036174499511/55029268480000000, approximately0.00040044.
Thus the strict advantage
has a finite-budget witness as well as an asymptotic construction. No numerical optimizer
or uncertified objective value is needed.

Exact symbolic controls derive the weak-effect expansion, branch derivative and common
vacuum Hessian; rational controls pin the finite-tail contrast, truncated edge sums and
saturation certificate. Interval checks test actual energy and tail changes. Altered
moment/feedback/tail inputs must fail real checks after a green baseline. Finite samples
check implementations; global compactness, SOCP equivalence and bounds, endpoint uniqueness
and asymptotic statements rest on the written proofs and independent internal review.
No proof-assistant, external-expert, novelty or remote-CI certification is claimed.

Next resolve whether the weak-budget lower coefficient is globally sharp, including rare
reported branches and occupation tails, or change the resource objective by supplying a
stable autonomous controller with preparation/reset accounting. Finite grid refinement
alone is not another independent scientific endpoint. A same-budget global enclosure needs
certified convex upper bounds at every grid point; this theorem does not pretend such a
full grid has already been run. The integer-N saturation tie remains a compact variational
problem; the earlier nondemolition tie minimizer cannot be imported silently.
