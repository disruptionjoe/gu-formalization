---
title: "K2058: One positive kinetic metric for the complete compatible dynamics"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional observed graph and changed coefficients only; no source parity, physical quotient or positive Hamiltonian claim
scripts:
  - tests/channel-swings/k2058_universal_positive_dynamics.py
  - tests/channel-swings/k2058_universal_positive_dynamics_probe.py
---

# K2058: One positive kinetic metric for the complete compatible dynamics

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.


```gu-typed-objects
result: simultaneous kinetic and dynamical compatibility, complete universal metric classification and variable-potential propagators
carrier: complexification of actual real1408 observed graph with both ambient64 halves LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: fixed real skew kinetic T and positive Hermitian graph metric P ON=declared_observed_graph
real_structure: independent dual coefficient A conjugation with square minus identity; no nonzero fixed-vector reality
grading: ambient Clifford halves and independent field parity, not family count
action_owner: repository-construction -- K2038 changed coefficient class and K2056 demanded kinetic convention
target: common current, metric classification and bounded-potential L2 propagator MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] The positive metric Pstar=sqrt(-T^2)
from K2056 conserves the dynamics of EVERY generator in K2038's existing
169984-dimensional liftable class, with no refitting. The full compatible
positive-Hermitian anti-involution metric family has six real parameters;
Pstar is its unique real member. The same fixed metrics give unitary L2
propagators for locally time-integrable bounded varying potentials in that
class. Varying the metric itself introduces a defect and needs a declared
additional connection. These results do not supply GU physical positivity.

## 1. Frozen object and distinction from the previous results

[K2038](k2038-observed-action-compression-2026-10-24.md) constructs the real1408
observed graph, its nondegenerate skew kinetic matrix T and symmetric spatial
C_j. They satisfy C_j^2=I, {C_j,C_k}=0 for j!=k and [T,C_j]=0. Its complete
real Euclidean-norm-conserving liftable zero-order class is

    g={N:N^T=-N, [T,N]=0}.

This is the explicitly CHANGED coefficient class, not the raw common-connection
tie excluded by K2036. [K2056](k2056-common-dual-successor-2026-10-25.md)
separately proves that A^T T=iP forces A=-iT^-1 conjugate(P), and that the
antilinear duality b=A conjugation has b^2=-I exactly when

    conjugate(P) T^-1 P=-T.                              (1)

A positive P cannot instead produce b^2=+I on the same coordinates. Independent
dual inverse maps remain possible. Here the new question is simultaneous
compatibility of(1) and the full existing dynamics, followed by its analytic
consequences. Neither predecessor alone supplied that classification.

Source SC-OP-04 ASSERTS candidate four-independent-field grammar; SC-OP-05 is
UNCERTAIN about a southeast rival; SC-META-53 is UNCERTAIN about positivity;
SC-META-56 DISAVOWS an odd-action prerequisite. None selects this metric,
field identification, changed coefficient, parity or physical quotient.
LT-SM8/LT-GR6b and all source/physics/canon verdicts remain unchanged.

## 2. A single fixed metric, no refit across generators

Let Pstar=sqrt(-T^2)>0 and J=T^-1 Pstar. Then J is real skew orthogonal,
J^2=-I and T=-Pstar J. Every matrix commuting with T commutes with Pstar
and J, by the finite-dimensional spectral calculus (or polynomial
interpolation on its distinct eigenvalues). Thus

    [Pstar,C_j]=0, [Pstar,N]=0 for EVERY N in g.

K2056 gives(1) for Pstar. For smooth solutions of

    u_t+sum_j C_j u_xj+Nu=0,

Hermitian positive P with [P,C_j]=0 has current

    rho=u^dagger P u, j_j=u^dagger P C_j u.

For fixed P and real skew N, its divergence is u^dagger[N,P]u. Consequently
Pstar is simultaneously a kinetic anti-involution metric and conserved positive
norm for the whole class. This is a stronger joint statement than independently
fitting a metric to each generator.

## 3. Complete universal positive-Hermitian classification

Set a=(sqrt(641)-19)/2, b=19+a. The six positive skew frequencies of T are
r in{1,2,a,2a,b,2b}; 3<a<7/2 and22<b<45/2 separate them. The associated
real spaces E_r have dimensions(576,576,64,64,64,64). Their J-complex
dimensions are m_r=(288,288,32,32,32,32); their ordinary complexifications
still have complex dimensions2m_r. Each ±i eigenspace of J_r has dimensionm_r.
Do not confuse these two uses of complex dimension.

K2038's real centralizer is direct-sum u(m_r), dimension169984. All positive
Hermitian P satisfying(1) and conserving EVERY N in g are precisely

    P|E_r=r(cosh(theta_r) I+i sinh(theta_r) J_r),
    theta_r in R independently for the six frequencies.                (2)

Proof: conservation is [P,N]=0. The independent central rotation on each
E_r eliminates off-diagonal frequency blocks. Within E_r, its central J_r
first splits the complexification into ±i sectors. Commuting with all diagonal
phase rotations removes off-diagonal coordinate entries in either sector;
commuting with two-coordinate unitary rotations forces equal diagonal values.
Hence the commutant is complex span{I,J_r}. Hermiticity gives
P_r=alpha_r I+i beta_r J_r with alpha,beta real. Positivity is
alpha_r>|beta_r|. Since T_r=-rJ_r, equation(1) reduces to
alpha_r^2-beta_r^2=r^2. Its positive branch is exactly(2).
Conversely every(2) commutes with g and obeys(1). Each C_j preserves the
frequency spaces and commutes with J_r, hence every such P also conserves
all three spatial currents. This completes necessity and sufficiency.

Realness forces beta_r=0. Therefore Pstar is the UNIQUE real positive
universal metric. In fact real positive P, conservation for just the allowed
N=T, and(1) imply P^2=-T^2 and already force that conclusion.

For comparison, with just one fixed N in g, all positive Hermitian metrics
satisfying(1) and conserving it and the spatial matrices can be parameterized

    P=Pstar^(1/2) exp(X) Pstar^(1/2),
    X^dagger=X, conjugate(X)J+JX=0,
    [X,N]=0, [X,C_j]=0.                                (3)

To prove this, let Q=Pstar^(-1/2) P Pstar^(-1/2)>0. Equation(1) becomes
conjugate(Q)JQ=J. Unique Hermitian logarithms transform it into
conjugate(X)J+JX=0 for X=log Q; exponentiation proves the reverse direction.
The dynamical commutators pass through Pstar and functional calculus. Thus(3)
is an exact description rather than a finite ansatz for the fixed-N problem.

## 4. Free massive evolution and its ceiling

K2038's M=I11 tensor(gamma0 gamma1 gamma2 gamma10) is real skew, squares to-I,
commutes with T and anticommutes with each C_j. For N=mu M, mu real, define

    H(p)=sum_j p_j C_j-i mu M.

It is self-adjoint in every fixed metric(2) and
H(p)^2=(|p|^2+mu^2)I. The Fourier multiplier exp(-itH(p)) is unitary.
Its self-adjoint generator on R3 has domain H1: the displayed square gives
the exact graph-norm equivalence. The periodic analogue is the same Fourier
series argument. No arbitrary high-order theorem is needed for this step.
The mass parameter mu remains supplied; this reuses the existing mass.

Positive norm is NOT positive Hamiltonian energy. The eigenvalue signs ±sqrt
remain; no positive-frequency interacting quotient or CAR quantization has
been supplied. An anti-involution has no nonzero fixed-vector reality locus:
bu=u would imply u=b^2u=-u. It is used here as an independent-dual coefficient
map, never imposed as a real-field restriction.

## 5. Released global L2 evolution for varying allowed potentials

Fix ONE metric P in(2). Let N(t,x) be jointly measurable, real skew and
centralize the fixed T almost everywhere, with integral_I ||N(t,.)||_infinity dt
finite on each compact time interval I. On L2(R3,C1408;P), or periodic space,
the constant principal Fourier group U0(t,p)=exp(-it sum p_j C_j) is unitary.
Multiplication by-N(t,x) is bounded skew-adjoint in this same metric.

In the interaction picture B(t)=U0(-t)(-N(t))U0(t), the successive Duhamel
integrals have norm bounded by(integral_I ||N(t)||_infinity dt)^k/k!.
The series converges uniformly in operator norm of its integrated terms on
compact intervals. Its strong integral equation gives uniqueness by the same
iteration; skew-adjointness implies preservation of inner products (first for
step approximants, or directly for absolutely continuous interaction-picture
solutions). Backward evolution is its inverse. There is therefore a unique
strongly continuous TWO-PARAMETER unitary propagator U(t,s), solving the PDE
in the distributional mild sense. Spatially measurable coefficients do not
necessarily preserve H1; no such claim is made. General varying N has no
constant-mass dispersion formula and need not form a one-parameter group.

Two useful consequences hold under the same measurable-potential assumptions.
First, propagation speed is at most one. For unit n, C(n)^2=I and PC(n) is
Hermitian, so |u^dagger PC(n)u|<=u^dagger Pu. The exterior-cone energy
estimate gives speed one for the free group; density extends it to L2.
In the original-picture Dyson series, each term is a time-ordered product of
free propagators and multiplication by N. Multiplication does not enlarge
support, and all free propagation distances sum to |t-s|. The convergent L2
sum preserves that support bound. This requires no derivative of N and is
conditional PDE propagation, not a GU physical causality assertion.

Second, for two admitted potentials N and Ntilde, variation of constants gives

    ||U_N(t,s)-U_Ntilde(t,s)||_P
       <= integral_min(s,t)^max(s,t) ||N-Ntilde||_infinity dt.

Both surrounding propagators are unitary, so no exponential growth factor
appears. Each potential commutes with P, hence its P operator norm equals its
ordinary Euclidean matrix operator norm. This supplies a quantitative
coefficient-approximation bound under the same fixed-metric assumptions.

This is global linear existence under explicit coefficient bounds. It does
not control K2038's nonlinear tangent amplification or arbitrary field-dependent
coefficients. Nor does variable use automatically establish a source-selected
variable action or a global physical bundle/domain.

## 6. Metric variation has an exact defect and a priced repair

For smooth P(t,x)>0 commuting pointwise with C_j, direct differentiation gives

    divergence(rho,j)=u^dagger D_eff u,
    D_eff=P_t+sum_j partial_j(P C_j)-N^dagger P-PN.        (4)

Pointwise membership in(2) cancels the last two terms but not the derivatives.
On E_r, P_r=r exp(i theta_r J_r) gives derivative defect

    D_r=P_r iJ_r(theta_(r,t) I+sum_j theta_(r,xj) C_j).

For all fields to have conserved current without a new coefficient, this
matrix must vanish. Cancel the invertible factor P_r iJ_r first. Each C_j is traceless on E_r: the invertible mass M
preserves E_r and anticommutes with it. Taking trace gives theta_t=0;
squaring the remaining Clifford combination gives sum theta_xj^2=0. Thus
all six theta_r must be constant on a connected patch.

Example: N=0, spatially constant u, theta_r(t)=t and iJ_r u=u. Its density
is r exp(t)|u|^2 although the kinetic condition holds at every point. This is
a local density counterexample; no constant nonzero R3 field is claimed L2.

For a declared CHANGED construction, assume N^dagger P+PN=0 pointwise,
as family(2) supplies. Put D=P_t+sum partial_j(P C_j) and
K=(1/2)P^-1 D. Then K^dagger P+PK=D, so replacing N by N+K repairs(4).
For the family(2), K=(i/2)J_r(theta_t I+sum theta_xj C_j) blockwise. With
S=P^(1/2), the exact identity K=S^-1(partial_t+sum C_j partial_j)S shows
that v=Su removes this connection. K is generally complex and outside the
original real-skew class. The repair is explicit additional data, not silent
survival of the unchanged model. Uniform bounds on S and its inverse would
be needed to identify a fixed ordinary L2 space globally.

## 7. Controls, evidence and adversarial review

On any actual invariant T-plane T=r[[0,1],[-1,0]], take
P=r diag(2,1/2). It obeys(1), but fails to commute with the allowed generator
N=T. Extending by Pstar on the orthogonal complement embeds the counterexample
in the full graph. Thus kinetic compatibility alone does not prove conservation.
Conversely P_r=r(5I/4+3iJ_r/4) is a genuinely complex universal survivor with
eigenvalues2r and r/2. Doubling Pstar gives anti-square-4I, not-I.

The producer checks actual128-spinor gamma factors and the copy-frequency
arithmetic, rational Hermitian kinetic controls and contrary constructions.
It reuses the earlier gamma implementation; the separate probe independently
constructs signed column maps and exact Gaussian-rational/realified matrices.
Raw1920-to1408 compression and generator exhaustiveness are inherited by hash,
not recounted as a new exhaustive matrix calculation. Written proofs supply
universal classification and the analytic domain/propagator statements.

Internal independent construction and root hostile verification check the
strongest overclaim (physical positivity), contrary kinetic-only example,
real/complex dimension distinction, fixed versus varying metrics and analytic
regularity. No external specialist, proof-assistant or novelty acceptance.
Next: actual source-selected independent dual/parity and observed physical
state bridge, or a genuinely different interacting estimate. The unchanged
raw tie remains excluded on its earlier scope; this theorem does not rescue it.
