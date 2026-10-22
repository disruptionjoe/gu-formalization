---
title: "K1936: Bounded energy limits approximate catalyst return"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite positive quantum models; analytic necessary bounds, no optimum or native GU claim
scripts:
  - tests/channel-swings/k1936_bounded_energy_catalyst_return.py
  - tests/channel-swings/k1936_bounded_energy_catalyst_return_probe.py
---

# K1936: Bounded energy limits approximate catalyst return

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
result: dimension-independent mean-energy and return-error inequalities with bounded bath energy transfer
carrier: four-state system, finite Gibbs bath, nondegenerate finite catalyst spectrum e_n >= n Delta LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace, half trace distance and natural-log entropy ON=independent_initial_registers
real_structure: complex adjoint and energy pinching
grading: additive energy, not source chirality
action_owner: repository-construction -- exactly conserving finite unitary
target: exact or approximate supplied extreme Schur channel and binary-input catalyst marginal MAP-TYPE=intertwiner
```

## 1. Bound without catalyst dimension or bandwidth

Use the four-state extreme Schur target of
[K1925](k1925-extreme-channel-information-consumption-2026-10-22.md), with
v1=(1,0), v2=(0,1), v3=(1,1)/sqrt2, v4=(1,i)/sqrt2.
Let the finite bath be Gibbs at beta>0 and have energy bandwidth W.
Let the finite catalyst have nondegenerate ordered energies
0=e0<e1<... with e_n>=n Delta, Delta>0, and initial mean energy at most E.
All dimensions and the catalyst bandwidth may vary. Initial registers are
independent; the joint unitary conserves additive energy exactly, and the
system Hamiltonian is diagonal in the target basis. Initial catalyst
coherence and final correlations are allowed.

For EXACT target realization, let R be half trace distance between the
initial and final catalyst on the SINGLE system input
rho12=(|1><1|+|2><2|)/2. This also lower-bounds any all-input return promise.
Define h(x)=-x ln x-(1-x)ln(1-x), hbar(x)=h(min(x,1/2)), and
g(n)=(n+1)ln(n+1)-n ln n, with continuous endpoint conventions.
Then

    ln2 <= beta min{E,W,2 sqrt(W E R)}
           + hbar(R) + R g((E+W)/(Delta R)).                    (1)

Set the last term to0 at R=0. For fixed finite E,W,beta and Delta>0,
the right side tends to0 as R tends to0. Thus (1) is a strictly positive,
dimension-independent return-error obstruction. It is a necessary bound,
not a sharp optimum or sufficient preparation/control protocol.
K1925's bandwidth/dimension continuity estimate cannot give this conclusion
when both catalyst bandwidth and dimension grow. A mean-energy bound alone
does not give uniform continuity of energy: the bounded transfer W is crucial.

## 2. Reduce to classical energy transport, keeping the physical registers

[K1933](k1933-covariant-catalyst-dephasing-reduction-2026-10-22.md) pinches
the INITIAL catalyst without changing its mean energy, worsening neither
channel error nor return for the invariant rho12 input. Indeed covariance
gives sigma'_bar=D_A(sigma'), so trace-norm contraction applies to their
difference. The pinched initial state p and final state q are diagonal because
the total input is energy invariant and the catalyst is nondegenerate.
Let r=TV(p,q)<=R. No physical dephasing operation or free reset is assumed:
this constructs another feasible preparation with the same unitary.

Exact preservation of each system population input forces that system to
remain in its original pure basis state on the populated environment support.
Consequently each nonzero transition has catalyst energy change bounded by
W, the bath bandwidth. The squared unitary matrix entries and initial
bath/catalyst probabilities give a classical coupling (X,Y) of p,q with
|X-Y|<=W, E[X]<=E, E[Y]<=E+W. This holds even if the unitary is not globally
controlled outside the occupied subspace.

## 3. The bounded-jump energy inequality

For ANY nonnegative coupled X,Y with |X-Y|<=J, E[X]<=E and marginal TV=r,
write x=min(x,L)+(x-L)_+ for L>0. The bounded part differs in expectation
by at most Lr. The one-sided remainder obeys

    (X-L)_+-(Y-L)_+ <= J 1_(X>L).

It is nonpositive when X<=L, so no enlarged tail cutoff is needed.
Markov's inequality therefore gives

    E[X]-E[Y] <= Lr+JE/L.

Optimize L=sqrt(JE/r), taking endpoints by limits, and retain the immediate
bounds from nonnegative Y and bounded jumps:

    E[X]-E[Y] <= min{E,J,2 sqrt(J E r)}.                       (2)

This is an upper bound on energy CONSUMED, not an absolute continuity bound
for arbitrary equal-mean state families. No monotone coupling is needed.
The concrete contrary control p=(1-r)delta0+r delta_(E/r), q=delta0 has
TV=r but loses energy E. Its jump is E/r; it violates a fixed-J hypothesis
as r decreases. Bounding mean energy and invoking a bandwidth estimate with
a silently fixed bandwidth would miss exactly this case.

## 4. Entropy common-part bound and consumption

For diagonal p,q with TV=r in(0,1), write
p=(1-r)c+r a and q=(1-r)c+r b using their common part.
Concavity and the binary mixture entropy upper bound give

    H(q)-H(p) <= h(r)+r[H(b)-H(a)] <= h(r)+r H(b).

The positive residual rb is componentwise bounded by q, so its mean energy
is at most(E+J)/r. Since e_n>=n Delta, its mean index is bounded by
(E+J)/(Delta r). Relative entropy against a geometric distribution gives
H(b)<=g((E+J)/(Delta r)). This holds on every finite spectrum; extending
probabilities by zeros to the infinite ladder only enlarges the entropy bound.
For r=1 use the same bound directly. The argument requires no quantum
positive-part energy inequality, which would be unsafe without commutation.

K1925's exact physical-environment information theorem and Gibbs accounting
on rho12 imply

    ln2 <= beta(E[X]-E[Y])+H(q)-H(p).

Insert (2), use J=W, and pass from r<=R to R: h(r)<=hbar(R), while
x g(A/x) is increasing, since its derivative is ln(1+A/x)>=0. This proves(1).
Keeping the actual diagonal r gives the slightly sharper h(r) expression.
Monotonicity of h itself beyond1/2 is NOT asserted.

## 5. Executed consumers: approximate channels and energy growth

Allow half diamond channel error epsilon and system energy bandwidth W_S.
Pinching still does not increase that error. Population leakage now permits
system energy exchange, so use the universally valid jump
J=W+W_S, NOT W. For K1927's constants set

    delta=sqrt(2 epsilon), eta=min(2,10 delta),
    b=delta+sqrt(eta), L_info=ln2-h(min(1/2,b)),
    a=min(1,2 sqrt(epsilon)),
    G(a)=2a ln4+(1+a)h(a/(1+a)),
    C_epsilon=L_info-G(a)-beta W_S epsilon.

The physical-environment thermal bound of
[K1927](k1927-robust-physical-environment-information-2026-10-22.md)
allows arbitrary population leakage and gives

    C_epsilon <= beta min{E,J,2 sqrt(J E R)}
                 +hbar(R)+R g((E+J)/(Delta R)).                 (3)

A negative left side is vacuous; only a positive C_epsilon constrains return.
Both sides have been derived for the same binary input and actual physical
bath/catalyst. No purified environment is substituted. With fixed resources,
epsilon and R cannot jointly tend to0. This is conservative; no optimal
finite-error exponent or quantitative shell-rank stability is claimed.

For any exact-channel sequence with fixed beta,Delta,W>0 and R_k->0,

    liminf E_k R_k >= (ln2)^2/(4 beta^2 W).                     (4)

If the liminf is finite, pass to a subsequence with E_k R_k bounded. Then
E_k<=C/R_k, so hbar(R_k)+R_k g((E_k+W)/(Delta R_k))->0.
Equation(1), even after dropping the min in favor of the square-root bound,
yields(4). Infinite liminf is trivial. Thus vanishing return would require
at least inverse-error mean-energy growth; this does not prove such a
sequence exists for a fixed bath. In particular K1935 excludes it entirely
for the fixed four-level bath. For epsilon_k->0 the same proof uses J=W+W_S
and (3), giving the corresponding constant with J. If W or W_S varies,
that fixed-resource asymptotic cannot be used.

A certified illustrative case: E=10, W=3, Delta=1, beta=ln2.
Any exact implementation must have R>1/10000. For R<=1/10000,
2sqrt(30R)<11/100, hbar(R)<=R(1-ln R), and
g(n)<=1+ln(1+n). Thus the RHS of(1) is less than
11/100+24/10000<1/2<ln2, using beta=ln2<1, ln10000<10
and ln130001<12.
The script verifies the rational exponential-series witnesses for the log
bounds. This is an intentionally conservative certified example, not a
numerically optimized or attainable return threshold.

## 6. Scope, prior work and hostile review

Mean-energy restrictions on thermal embezzling are established prior work:
[Ng et al., Limits to catalysis](https://arxiv.org/abs/1405.3039).
Energy-constrained entropy continuity is also established:
[Winter](https://arxiv.org/abs/1507.07775).
Here the bounded-jump estimate is explicitly composed with the supplied
full-channel information cost. No novelty claim or complete literature
survey is made. The proof is internal analytic mathematics, not external
expert acceptance or Lean verification.

Countercontrols retain zero gap, high degeneracy, growing bath bandwidth,
unbounded preparation mean energy, and nonconservation as different models.
A bounded mean with an arbitrarily dense spectrum cannot use the geometric
entropy estimate. The existing zero-Hamiltonian embezzlers and growing-bath
constructions do not contradict (1). Neither (1) nor(4) prices total work,
local control synthesis, actual repeated use or product catalyst return.
SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b/AC-F1, source claims, physics
ledger and canon are unchanged. No native GU pairing/action/domain bridge
or physical prediction is supplied.

## Reproduction

Run the two frontmatter scripts with Python3. The producer --write flag
refreshes its JSON. Rational transition/cutoff and coupling controls are
exact finite computations; entropy/log illustrations are floating checks
unless explicitly labeled rational certificates. Universal statements rest
on the proofs above. The separate probe uses independent couplings and
checks real input faults after a green baseline; report equality and script
pins are separately reporting checks.
