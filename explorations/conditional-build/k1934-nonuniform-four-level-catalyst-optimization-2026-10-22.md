---
title: "K1934: Unequal weights improve thermal catalyst return"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite quantum models; analytic proof with internal controls, no native GU or novelty claim
scripts:
  - tests/channel-swings/k1934_nonuniform_four_level_catalyst_optimization.py
  - tests/channel-swings/k1934_nonuniform_four_level_catalyst_optimization_probe.py
---

# K1934: Unequal weights improve thermal catalyst return

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
result: exact fixed-protocol preparation and all-unitary fixed-support return optima
carrier: four-state system, four-level thermal bath, finite nondegenerate ladder catalyst LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace and worst-case half trace distance ON=product_input
real_structure: complex adjoint; coherent preparations reduced by time covariance
grading: additive energy shells; no particle chirality
action_owner: repository-construction -- conserving shell isometries, then all-unitary two-site bound
target: supplied extreme Schur channel and catalyst marginal return MAP-TYPE=intertwiner
```

## 1. Result and exact scope

[K1932](k1932-four-level-bath-catalyst-return-2026-10-22.md) gives a sharp
return bound for a FIXED UNIFORM preparation. Unequal weights improve it.
Keep its four-level bath, positive common spacing Delta, inverse temperature
beta, t=exp(-beta Delta) in(0,1), catalyst dimension d=2N+5, and occupied
levels S={3,5,...,2N+1}. Keep its boundary-repaired full shell unitaries.
Define

    u=t^2, L=1/(1+u), H=u/(1+u), z=1+2u,
    s_i=z^(i-1)/(sum_(k=0)^(N-1) z^k),  i=1,...,N.

The exact full four-state Schur channel has worst-case marginal return

    r_N = 1/[2 sum_(k=0)^(N-1) z^(-k)]
        = u z^(N-1)/(z^N-1).                                    (1)

This is the minimum over ALL preparations supported on S for the FIXED
unitary protocol, including coherent preparations by K1933. For N=2 it is
also the minimum over ALL conserving joint unitaries and all preparations
on those same two levels (section5). Section6 solves the all-unitary problem
for EVERY N on this fixed support, and improves (1) once an interior root
beats the endpoint. No optimum over arbitrary support sets, spectra, bath
sizes or approximate channels is claimed.

At t=1/2,N=2, weights(2/5,3/5) give r=3/10, improving the uniform7/20.
At N=3 they are(4,6,9)/19 and r=9/38; N=5 gives81/422.
For fixed t,

    r_N -> u/(1+2u) < u/(1+u),                                 (2)

strictly improving the old protocol's uniform-weight limit. This remains a
positive limit for a fixed four-level bath and temperature. It does not prove
that the GLOBAL fixed-bath optimum has a positive limit.

## 2. The same full complex channel, changed probabilities

Reuse K1932 section5's explicit conserving shell unitaries, including the
one-occupied-column boundary repair. On each occupied column alpha,
U_j alpha has common Gram <v_k,v_j>, for
v1=(1,0), v2=(0,1), v3=(1,1)/sqrt2, v4=(1,i)/sqrt2.
Any convex choice of diagonal weights therefore implements all16 complex
matrix units exactly. No basis-population shortcut or phase-insensitive
channel test is used. A controlled U and arbitrary diagonal H_S preserve
total energy; its unused columns complete a genuine unitary.

For j=1,2,4 the squared pair coefficients are(1/2,1/2); for j=3 they
are(1,0). Writing c for the first coefficient, direct transport gives the
output probabilities ON S for any probability vector s:

    p'_i=c L s_i+(1-c)L s_(i+1), i<N,
    p'_N=c s_N.                                                (3)

For N=1 only the last formula applies. Output outside S has nonnegative
probability and no initial mass. Thus half trace distance is exactly

    r_c(s)=sum_i (s_i-p'_i)_+.                                 (4)

The partial trace over S removes input-control coherences. Convexity gives
r(s)=max(r_(1/2)(s),r_1(s)), attained by a basis input. This is a statement
about the catalyst MARGINAL for all system inputs, including reductions of
entangled inputs, not a product-return statement.

For the geometric s, all i<N deficits at c=1/2 vanish, because
(1-L/2)s_i=(L/2)s_(i+1). The terminal deficit is s_N/2=r_N.
At c=1, r_1=H(1-s_N)<=s_N/2. Indeed
s_N>=1-z^(-1)=2u/(1+2u)>2u/(1+3u)=2H/(1+2H).
This proves achievability of(1).

## 3. Exact dual: global preparation optimum for this protocol

Let T be the substochastic matrix in(3) at c=1/2 and M=I-T.
M has diagonal1-L/2 except the last entry1/2, and superdiagonal-L/2.
Its inverse is entrywise nonnegative. Put w^T=1^T M^-1. Explicitly,

    w_i=[1/(1-L/2)] sum_(k=0)^(i-1) z^(-k),  i<N,
    w_N=2 sum_(k=0)^(N-1) z^(-k).

All w_i>0 and w_i<w_N for i<N. For arbitrary normalized nonnegative s,
d=M s may contain negative entries, but

    1=w^T d <= w_N sum_i (d_i)_+ = w_N r_(1/2)(s).

Hence r(s)>=r_(1/2)(s)>=1/w_N=r_N. The geometric preparation attains
it. Equality forces d_i=0 for i<N and d_N>0, so the DIAGONAL optimizer
is unique. No uniqueness of coherent optimizers is asserted.
Equivalently f=w/w_N is a physical diagonal effect (0<f_i<=1), with
f^T M=r_N 1^T; it is an exact rational dual certificate.

K1933 applies with fixed U and fixed spectral support S: any coherent
preparation realizing the target has a pinched preparation realizing it with
no larger return. Thus it cannot beat this diagonal minimum. Merely
pinching a measurement outcome would not prove that optimization reduction.
For N>1, the uniform vector has positive nonterminal deficits and therefore
strictly fails the equality condition, proving strict improvement without
relying on sampled temperatures.

## 4. Resource consumers and honest limits

Let Z_N=sum_(k=0)^(N-1) z^k and K=sum_k k z^k/Z_N.
The occupied energy is Delta(3+2k), so

    E_A=Delta(3+2K),  S(sigma)=log Z_N-K log z,
    D_relative(sigma||tau_A)=beta Delta(3+2K)-log Z_N+K log z+log Z_A,
    Z_A=sum_(n=0)^(2N+4) t^n.                                  (5)

As N grows at fixed t, N-1-K ->1/(z-1). Consequently mean energy grows
as Delta[2N+1-2/(z-1)], up to a vanishing correction. The limiting
preparation entropy is log[z/(z-1)]+log z/(z-1), finite. Preparation
relative entropy and energy grow while return approaches the positive(2).
This is a changed resource tradeoff, not a preparation algorithm or total
work cost. At finite N and t->0, r_N->1/(2N); the exactly zero-temperature
bath is a different rank-deficient model, not covered by the exact proof.
At t->1 the continuous formula gives z->3 and limiting return1/3, but the
main theorem assumes strictly positive beta Delta. The limits are explicitly
separated. The previous growing-bath construction remains the proved route
to vanishing return at fixed positive spacing/temperature.

## 5. Released successor: all-unitary optimum on two occupied sites

Set N=2, S={3,5}. Allow ANY conserving joint unitary implementing the
same exact extreme channel and ANY initial coherent state supported on S.
K1933 reduces the latter to diag(x,1-x). For the fixed system input
rho12=(|1><1|+|2><2|)/2, extreme-Gram dilation implies every occupied
energy shell with initial eigenvalues lambda_a has output eigenvalues
lambda_a/2, each repeated twice. This is the K1932 section5 argument,
using exact population preservation, extremality and conservation on the
populated subspace; it does not assume a globally controlled unitary.

The two lower boundary shells have only the low site populated, and the two
upper boundary shells only the high site. Summing their bath weights gives
Lx and H(1-x). In the two interior shells, corresponding initial eigenvalues
are proportional to L(1-x) and Hx. Each physical catalyst-site projector has
rank ONE in a shell, so its output expectation is at most the largest shell
eigenvalue. Therefore final probabilities a,b at the two original sites obey

    a <= [Lx+max(L(1-x),Hx)]/2,
    b <= [H(1-x)+max(L(1-x),Hx)]/2.                             (6)

Measurement contractivity gives r>= (x-a)_+ +(1-x-b)_+ already at rho12.
For x<=L, the maximum in(6) is L(1-x), and thus

    r >= (x-L/2)_+ +(1-x)/2 >= 1/2-L/4.

For x>=L, the maximum is Hx, yielding

    r >= x/2 +(1-x-H/2)_+ >= 1/2-H/4 >= 1/2-L/4.

The breakpoints are0,L/2,L,1-H/2,1; these inequalities hold on whole
intervals, not only enumerated points. Thus

    inf_(sigma supported on S,U) r = (1+2u)/[4(1+u)],           (7)

attained by x=L/2 and the protocol above. This settles the two-site
all-unitary problem, not the arbitrary-support/global fixed-bath problem.
Coherence inside a larger degenerate eigenspace would need separate treatment;
these ladder energies are nondegenerate.

A hostile shortcut fails: the UNWEIGHTED total escaped-support bound alone
can be weaker than(7). At t=1/2,x=1/10 it is3/20<3/10. The separate
site deficits in(6) recover the required bound. This is why the earlier
uniform support proof cannot simply be applied to arbitrary weights.

## 6. Full fixed-support solution: orient the shells toward an interior peak

The fixed-protocol answer(1) is not the general answer even on the SAME S.
Set q=L/(2-L)=1/(1+2u), p=H/(2-H)=u/(2+u). For a+b=N-1 define

    Z_(a,b)=1+sum_(k=1)^a q^k+sum_(k=1)^b p^k.

Then the exact minimum over ALL preparations supported on S and ALL
conserving unitaries implementing the target is

    R_N = 1/[2 max_(a+b=N-1) Z_(a,b)].                         (8)

The optimizer has a peak at site a+1, with probabilities proportional to
q^a,...,q,1,p,...,p^b. Coherent preparations cannot improve it by K1933.
At t=1/2,N=7, a=5,b=1 gives243/1384, strictly below the endpoint729/4118.
Thus the generalization was actually tested and changes the best construction.

**Universal lower bound.** For any diagonal s, generalize(6): set
m_0=L s_1, m_N=H s_N and
m_i=max(L s_(i+1),H s_i), 1<=i<N. Rank-one physical-site projectors and
the duplicated shell spectrum give p'_i<=(m_(i-1)+m_i)/2 for the fixed
rho12 input, regardless of the exact conserving implementation. Choose an
orientation of each interior edge according to the maximizing term in m_i.
This defines a nonnegative substochastic matrix T: if m_i=L s_(i+1),
column i+1 sends L/2 to itself and its left neighbor; if m_i=H s_i,
column i sends H/2 to itself and its right neighbor. Boundary columns
add L/2 at site1 and H/2 at siteN. Then

    r >= sum_i ([(I-T)s]_i)_+.

Each undirected edge points only one way. Ignoring self loops, the directed
line is acyclic, so in topological order T is triangular with diagonal at
most1/2. Hence M=I-T has nonnegative inverse and w^T=1^T M^-1 is finite.
As before 1=w^T M s <= (max_i w_i) sum_i([M s]_i)_+.

The exact bound on the column sums is

    w_i <= 2[1+sum_(k=1)^(i-1) q^k+sum_(k=1)^(N-i) p^k].       (9)

Here is a direct derivation, independent of a matrix search. Regard w_i as
the expected number of visits before killing for the substochastic walk
started at i. An edge once crossed cannot be crossed back: it has only
one direction. Each reachable arm is consequently a single outward path.
On a left-going arm, a non-root vertex has only its L/2 self-loop and
L/2 onward transition, yielding the recurrence
w=2/(2-L)+q w_next. A right-going arm gives2/(2-H)+p w_next.
If an arm stops before the endpoint, its terminal vertex has no outgoing
edge and reward1. Extending the arm to the endpoint and adding the terminal
boundary self-loop only increases its reward. If the initial vertex lacks
one outward arm, adding that arm increases its self-survival and adds
nonnegative future reward; vertices on the new arm were previously
unreachable, so reversing their former inward edges removes no old path.
The maximal walk from i therefore has BOTH arms directed outward all the
way to the boundaries. At its root the self-loop is(L+H)/2=1/2; substituting
the two finite geometric recurrences gives exactly the right side of(9).
This also handles endpoint roots and N=1. Equations(9) and normalization
prove the lower bound(8) for every orientation, including ties and zeros.

**Attainment by full unitaries.** Choose a maximizing root and outward
orientation. In every interior shell choose the occupied input column with
larger thermal weight: left of the root this is the low-bath column;
right of the root it is the high-bath column. Map this heavy column's Wv_j
into the TWO occupied-support output positions, ordering its original
position first. Map the light column's Wv_j into the two complementary
positions. Complete each pair with its orthogonal companion on the two
unoccupied input columns. This is a full shell unitary with the same complex
Gram for BOTH occupied input columns. Boundaries use the K1932 repair.
All entries remain in the same energy shell.

For the displayed q/p preparation, the chosen heavy column really is
heavier: L>=Hq on left edges and H>=Lp on right edges. For c=1/2,
M s vanishes away from the root and equals s_root/2 there. Thus return is
s_root/2=R_N. For c=1, the heavy column stays at its original site, so

    r_1=H sum_(left) s_i + L sum_(right) s_i
       =s_root/2 [1-L q^a-H p^b] <=s_root/2.

All four basis controls therefore have return at most R_N, and the fixed
rho12 input attains it. This supplies the matching all-input upper bound.
Correlations are allowed; no product return or exact reuse is inferred.

**Optimal root and asymptotic resource consequence.** Maximizing Z amounts
to taking the largest N-1 entries from the two decreasing sequences
q,q^2,... and p,p^2,...; each choice automatically takes a prefix. A root
moves when the next q or p power changes order. At fixed0<t<1 both prefix
lengths grow without bound, hence

    R_N -> 1/[2(1+q/(1-q)+p/(1-p))] = L H = u/(1+u)^2.          (10)

This is the GLOBAL limit for this fixed consecutive-odd support family,
not for arbitrary spectra or support patterns. It is1/4 at the continuous
t->1 limit and tends to0 as t->0; finite positive t gives a strict floor.
The normalized two-sided geometric profile has finite limiting entropy and
finite mean displacement from its root. The root itself moves to higher
energy as N increases: a/(N-1) tends to log(p)/(log(p)+log(q)), from balancing
q^(a+1) and p^(b+1). Thus the fixed-support limiting optimum again consumes
unbounded catalyst mean energy and preparation free energy. Exact finite
costs are obtained by E_A=Delta sum_i(2i+1)s_i and
D=beta E_A+sum_i s_i log s_i+log Z_A. No optimal-energy claim follows.

The orientation relaxation was first checked with exact small linear programs;
the universal proof above replaces that exploratory enumeration. Durable
controls independently reconstruct the acyclic reward recurrences for all
orientations through N=8 and three rational temperatures. The producer
constructs full complex shell unitaries at the optimizing roots, including
the N=7 interior-root improvement. These finite controls support, rather
than extend, the proved scope.

## 7. Evidence, prior work and remaining questions

Exact producer controls reconstruct the full shell output for three rational
temperatures and N=1,2,3,5, all complex Gram coefficients, normalized outputs,
transport, dual and the two-site piecewise bound. The independent fraction
probe reconstructs the transpose recurrence without importing the matrix
inverse, tests arbitrary weights, and checks every analytic two-site segment
endpoint. Green baselines precede faults in weights, dual, phase, pairing and root placement;
report/pin tests are separately reporting consistency, not mathematical proof.
Run both frontmatter scripts with Python3/SymPy1.14.0; producer --write
refreshes the report. Universal claims rely on sections 2–6. No external
expert, formal proof or novelty is asserted. Symmetry and catalytic resource
background: [Lostaglio et al.](https://arxiv.org/abs/1410.4572),
[Ng et al.](https://arxiv.org/abs/1405.3039),
[vom Ende](https://arxiv.org/abs/2207.11189).

The next global problem is now classical preparations plus shell isometries:
K1933 removes energy coherence and section6 now handles all interior routing
on this consecutive-odd support. Changing the occupied SUPPORT pattern or
Hamiltonian changes the shell graph and needs a new certificate. The
fixed-protocol M^-1 dual alone was insufficient; the all-orientation bound
is the necessary additional proof. Approximate-channel and energy-constrained
optima also remain separate. Native full20/K-C/domain/accessibility and scalar finite-T cuts remain
independent contenders. SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b/AC-F1,
source claims, ledger and canon are unchanged. No GU prediction is supplied.
