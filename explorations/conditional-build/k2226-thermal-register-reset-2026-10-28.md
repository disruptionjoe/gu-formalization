---
title: "K2226 Sharp thermal-register reset resources"
status: active_research
doc_type: exploration
created: "2026-10-28"
claim_ceiling: supplied finite thermal register and externally controlled reset; no autonomous apparatus or GU realization
scripts:
  - tests/channel-swings/k2226_thermal_register_reset_probe.py
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
---

# K2226 Sharp thermal-register reset resources

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
result: K2226 exact fixed-marginal and uniform reset errors
carrier: supplied record qubit and N finite thermal bath qubits with arbitrary reference LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace form ON=declared_carrier
real_structure: ordinary complex adjoint
grading: binary occupation and tensor-product bath number
action_owner: repository-construction -- arbitrary collective unitary controls
target: reset marginal and complete replacement channel MAP-TYPE=intertwiner
```

All claims
concern supplied positive finite Hilbert spaces and arbitrary externally
controlled unitaries. No source-native GU construction, source claim, physics
grade, experimental realization, novelty, or total apparatus cost is inferred.

## Route and retrieval

AGENTS.md, GEOMETER-VS-PHYSICS-OBJECTS.md, source-native comparator routing,
the six-axis semantic template and RESEARCH-POSTURE were loaded. The operative
object is the post-readout positive record qubit of K2223, with an independent
finite Gibbs bath. Ordinary complex adjoint, trace pairing, binary occupation
grading, and repository-supplied unitary controls are used. Native indefinite
pairings, full20/K-C, source action, physical units and accessible algebra are
not identified. Relevant routing is T15/T16/T17; particle comparators are not
being tested. The standard notice above bounds all inference.

K2223 proves the correct finite-bath spectral variational theorem: q is the
sum of the smaller half of the joint spectrum, attainable by a permutation.
Its rank obstruction and fixed-marginal trace-distance statement survive this
review. Correlations with the field do not change the local spectrum argument.

Retrieval found K99/K100's odd-prefix majority discrimination of flipped Gibbs
products, including exactly the p=1/4 odd binomial tail below. That scalar
formula is reused, not claimed as new. The consumer here is unitary erasure,
with an explicit exact channel optimum and even-N/fixed-prior distinction.
K1916 prices rank-constrained bath preparation and K1918 studies the entropy
threshold for N-copy extreme correlation channels. Those concern a growing
target rank k^N, while the present target remains one record bit. They do not
already establish this uniform reset optimizer. No novelty claim is made.

## 1. Exact fixed-marginal optimum

Let rho_R=diag(a,b), a=1-w, b=w, 0<w<=1/2. Supply N>=1 independent fresh
qubits tau=diag(1-p,p), 0<p<1/2. There is arbitrary collective unitary access
to R and all N bath qubits; no energy-conservation, locality or circuit-time
constraint is imposed. Each reset receives a fresh N-qubit block. Write

    lambda_k=(1-p)^(N-k) p^k, c_k=binom(N,k).

The spectrum consists of a lambda_k and b lambda_k, each with multiplicity
c_k. Pair (record=0,word x) with (record=1,complement x). Every pair has product
ab[p(1-p)]^N. Exactly one member is below the common square-root threshold;
ties are divided evenly. These lower members are precisely the lower half of
the complete spectrum. Therefore the sharp error is

    q_N(w,p)=sum_(k=0)^N c_k min(a lambda_k, b lambda_(N-k)).       (1)

Equation (1), with rational p,w, is an exact arithmetic formula without any
floating logarithm or boundary ambiguity. The Ky Fan minimum is attained by
assigning all these eigenvalues to the output record-1 subspace.

For the alternate binomial formula let J~Bin(N,p),
L=log[(1-p)/p], t=log(a/b)/L, and
B_N(x)=Pr[J>x]+(1/2)Pr[J=x], with the equality term zero for noninteger x.
Then the same optimum is

    q_N=a B_N((N+t)/2)+b B_N((N-t)/2).                        (2)

The half-tie convention accounts for all boundary degeneracies. For p<w<1/2,
0<t<1, so

    N odd:  q_N=Pr[J>N/2],
    N even: q_N=Pr[J>N/2]+w Pr[J=N/2].                        (3)

For p=1/4, K2223's certified 0.3045489<w<0.3046040 lies strictly in this
regime. Odd-N errors therefore do not depend on the uncertain optimized w.
N=1 gives 1/4; N=2 gives 1/16+3w/8; N=3 gives 5/32.

Faithfulness implies q_N>0 at every finite N. At p=1/2, (1) gives q_N=w:
a completely mixed bath cannot improve this marginal at any N. At p=0, a
pure bath qubit allows exact reset. These are contrary controls, not limits
silently covered by the faithful/nonuniform exponent theorem.

## 2. Exact uniform reset-channel optimum

Define the ideal channel Z(X)=Tr(X)|0><0| and use half-diamond distance,
allowing arbitrary reference systems. Among every unitary on R+B with the
same supplied product Gibbs bath, the exact optimum is

    epsilon_N=Pr[J>N/2]+(1/2)Pr[J=N/2].                      (4)

Lower bound: test the channel on I_R/2. K2223's rank-2^N variational principle
gives the sum of the smallest 2^(N-1) bath eigenvalues; the unwanted-record
measurement lower-bounds trace distance. This sum is exactly (4).

Attainment: by a bath-only permutation place its largest 2^(N-1) eigenvalues
in the 0 sector of one designated bath qubit, the rest in its 1 sector. Its
marginal is sigma=diag(1-epsilon_N,epsilon_N). SWAP that qubit with R. The
resulting record channel is the replacement X -> Tr(X)sigma, including for
entangled inputs. Correlations inside the bath cause no difficulty: the
initial entire bath is independent of input/reference. Half-diamond distance
between these two replacement channels equals half-trace distance between
sigma and |0><0|, namely epsilon_N. No extra pure ancillary bit is used.

For p<w<1/2 and odd N, q_N=epsilon_N. For even N,

    epsilon_N-q_N=(1/2-w) Pr[J=N/2]>0.                       (5)

Thus the fixed optimized record can do better than a universal reset channel
at even N. Do not label q_N a diamond optimum. An independently checked bath
permutation plus SWAP is a concrete full-channel attainer of epsilon_N.

The fixed-marginal permutation also preserves classicality of a post-readout
record in an arbitrary classical-quantum state sum_r |r><r| tensor A_r.
For this family the output is |0><0| tensor C_0+|1><1| tensor C_1, with
C_0+C_1=rho_F, so its joint half-trace distance from |0><0| tensor rho_F is
exactly Tr(C_1)=q_N. This handles the specified correlations but is still a
state-family statement, not uniform channel control for arbitrary inputs.

## 3. Sharp exponent and finite bounds

For any fixed 0<p<1/2 and 0<w<1,

    lim_(N->infinity) -log q_N/N
      =lim -log epsilon_N/N
      =D(1/2 || p)=-log[2 sqrt(p(1-p))].                    (6)

Proof: the thresholds in (2) are N/2+O(1). Binomial type bounds
exp[-N D(k/N||p)]/(N+1) <= Pr[J=k] <= exp[-N D(k/N||p)]
give lower bounds from one included term and upper bounds from at most N+1
terms. Dividing their logarithms by N and taking the boundary to 1/2 proves
(6). The endpoints w=0,1 are excluded because an initially pure record is a
different resource.

A direct finite upper bound follows from min(x,y)<=sqrt(xy) in (1):

    q_N <= sqrt(w(1-w)) [2 sqrt(p(1-p))]^N,
    epsilon_N <= (1/2) [2 sqrt(p(1-p))]^N.                 (7)

For p<w<1/2, set r=2sqrt(p(1-p)). Central-binomial coefficients satisfy
binom(N,floor(N/2))>=2^N/(N+1), so explicit lower bounds are

    even N: q_N>=w r^N/(N+1), epsilon_N>=r^N/[2(N+1)];
    odd N:  q_N=epsilon_N>=sqrt[p/(1-p)] r^N/(N+1).        (8)

These prove the exponent in this regime without asymptotic approximations.
For p=1/4 the exponent is (1/2)log(4/3), about 0.143841 nats/cell.
Equations (7)-(8) are conservative finite bounds; exact rational evaluation
of (3)-(4) provides sharper finite certification.

## 4. Exact rational consumers for the actual detector

For p=1/4, probabilities are integer sums divided by 4^N. Computing with
exact Fractions and K2223's rational w endpoints proves

    N=100: 3.5038e-8 < q_N < 3.5042e-8;
           4.3848e-8 < epsilon_N < 4.3849e-8.
    N=101: 3.2580e-8 < q_N=epsilon_N < 3.2581e-8.

The displayed decimal inequalities are rational comparisons, not rounding
assertions. The lightweight exact probe independently enumerates the
full joint spectrum at small N, checks the explicit uniform channel, and
computes the N=100/101 bounds by exact integer binomial sums. The exact output is [the certificate](../../lab/process/k2226-thermal-register-reset.json).

## 5. Repeatability and renewal

With M uses of the uniform construction and a fresh independent N-cell block
on every use, arbitrary intervening CPTP detector maps obey a hybrid bound
of min(1,M epsilon_N) in half-diamond distance from the ideal M-reset circuit.
This follows by telescoping channel differences and diamond contractivity;
it holds with adaptive classical records and arbitrary references. For an
error target eta, (7) suffices when N>=log[M/(2eta)]/D(1/2||p), rounded up
and at least one. The exact bound can be much sharper. N=101 and M=1000
certify total error below 0.000032581 by a rational comparison.

This uses M*N fresh thermal cells. It does not construct a cyclic finite
reservoir. Compression plus SWAP leaves spent cells correlated and changed;
the old record and its field correlations move into the bath. Resetting them
to independent tau is another physical operation with its own heat sink,
work, timing and control costs. This calculation prices the supply in cell
count and spectral error, not a complete apparatus work budget.

Collective access is essential to the released result. Repeatedly interacting
the record with one fresh qubit, discarding it, and retaining no other memory
cannot cool a qubit below min(initial smaller eigenvalue,p): the two-qubit
Ky Fan optimum is min(q,p). Starting with w>p, this one-cell-only model
plateaus at p even with arbitrary unitary controls. Entangling and retaining
several bath cells accesses a different control class. No claim of an
implementable local circuit, uniform time/strength or energy-conserving
thermal operation is made.

If energy accounting is added with degenerate record and bath Hamiltonian
H_B whose Gibbs state is tau^N, the exact reset identity is

    beta Delta E_B = h(w)-S(rho_R')+I(R:B)' + D(rho_B'||tau^N).

This follows from joint entropy conservation and the Gibbs relative-entropy
identity; initial R and B are independent even when R is correlated with F.
It gives a lower bound beta Delta E_B>=h(w)-h(q_N) for a diagonal attainer.
Calling Delta E_B the reset work additionally requires a specified cyclic
endpoint switching model. The identity does not itself price bath renewal,
observer readout, clocks, control preparation or physical detector creation.

## Hostile review and acceptance limits

Strongest overclaim: exponentially accurate collective erasure proves a
repeatable finite thermal apparatus at negligible total work. It does not.
Finite-N faithfulness, bath consumption, arbitrary global control and the
separate physical/source bridge remain explicit. A second overclaim would
transfer K100's controlled-flip work W_N=N Delta/2 to this different reset
unitary; identical binomial tails do not identify work protocols.

Weakest reproducibility seams: the half-tie rule; parity; sorting the complete
spectrum rather than independently picking lower weights per original
record branch; confusing diagonal-state accuracy with full channel accuracy;
and treating a finite rational computation as the exponent proof. The
separate pairing argument, maximally-mixed converse, explicit replacement
channel construction and analytic type bounds address these seams.

Contrary controls: p=1/2 gives no purification, p=0 gives exact SWAP, even N
separates fixed-prior and uniform optima, one-cell sequential reset plateaus,
and reused spent blocks violate the fresh-product hypothesis. No canon,
source-register, physical ledger, GU hypothesis vote or acceptance changes
follow from these results.

The classical majority compression belongs to established algorithmic cooling; see [Kaye](https://arxiv.org/abs/quant-ph/0703194). The new repository consumer and exact channel comparison above are not a novelty claim.
