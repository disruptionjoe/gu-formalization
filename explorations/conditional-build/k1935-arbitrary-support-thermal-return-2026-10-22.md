---
title: "K1935: Global four-level thermal return floor and a finite support transition"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied exact finite quantum model; arbitrary nondegenerate catalyst spectra, no native GU or novelty claim
scripts:
  - tests/channel-swings/k1935_arbitrary_support_thermal_return.py
  - tests/channel-swings/k1935_arbitrary_support_thermal_return_probe.py
---

# K1935: Global four-level thermal return floor

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
result: global fixed-bath catalyst-return infimum and sharp two-occupied-energy support transition
carrier: four-state system, four-level equally spaced thermal bath, arbitrary finite nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace and half trace distance ON=independent_initial_registers
real_structure: complex adjoint and energy pinching
grading: additive energy resonance classes; no source chirality
action_owner: repository-construction -- exact conserving unitary and extreme channel
target: all-input catalyst marginal return and arbitrary-support spectral lower bound MAP-TYPE=intertwiner
```

## 1. Main result and scope

Fix the four-state extreme Schur channel with
v1=(1,0), v2=(0,1), v3=(1,1)/sqrt2, v4=(1,i)/sqrt2,
and C_jk=<v_k,v_j>. The system Hamiltonian is any diagonal H_S.
The bath has energies0,Delta,2Delta,3Delta, Delta>0, and Gibbs weights
t^b/Z with t=exp(-beta Delta) in(0,1), Z=1+t+t^2+t^3.
Allow ANY finite nondegenerate catalyst Hamiltonian, ANY initial catalyst
state, and ANY exactly energy-conserving joint unitary implementing the
full target channel. Initial S,B,A are independent. Define

    r=sup_rhoS (1/2)||sigma'_A(rhoS)-sigma_A||_1.

Then every finite feasible implementation satisfies

    r > t^2/(1+t^2)^2.                                        (1)

The infimum over these implementations EQUALS the right side: the
consecutive-odd constructions in
[K1934](k1934-nonuniform-four-level-catalyst-optimization-2026-10-22.md)
approach it. Thus its formerly fixed-support limit is now the global
fixed-four-level-bath infimum, even over arbitrary nondegenerate spectra.
No finite catalyst attains it. This does not settle approximate channels,
degenerate catalysts, other bath spectra, initially correlated resources,
local control or product catalyst return.

There is also a finite-size surprise. For exactly TWO occupied energy
levels after pinching, adjacent levels beat separation2Delta when
2t^3+t-1>0. At t=3/4, support{3Delta,4Delta} with weights(74/217,143/217)
attains r=143/434<17/50, the separation2Delta optimum. The unchanged global
limit does not mean consecutive-odd support is best at every finite size.

## 2. Shell rank and arbitrary spectrum geometry

K1933 permits pinching the initial catalyst without increasing r, preserving
exactness for this covariant target. Let s_i>0 be its occupied diagonal
energy probabilities. Coherence is not freely erased in a physical protocol;
the reduction proves a feasible comparison preparation with the same U.

The four projectors |v_j><v_j| span Hermitian(2). Exact system population
preservation and extreme-Gram polarization give mutually orthogonal
copies of v_j for each occupied environment eigenvector, as derived in
[K1932 section5](k1932-four-level-bath-catalyst-return-2026-10-22.md).
On an energy shell with k_E physical states and r_E occupied inputs,

    2r_E<=k_E<=4.

For rho12=(|1><1|+|2><2|)/2, the output shell eigenvalues are each initial
positive eigenvalue divided by2 and repeated twice. This statement uses the
PHYSICAL mixed environment and does not suppose globally controlled U on
unused inputs. Conservation preserves these shell copies because the system
population j itself is unchanged on every occupied input.

Split catalyst energies by differences in Delta Z. Only separations dDelta,
d=1,2,3, can share a bath shell. Ordered occupied energies in each class
form path components with edge gaps d_i in{1,2,3}; gaps>=4 disconnect them.
Three occupied energies in a span<=3Delta would violate r_E<=2, hence

    d_i+d_(i+1)>=4.                                           (2)

Missing unoccupied levels may make a proposed support infeasible; retaining
all four potential shell positions is a RELAXATION for the lower bound.
Attainment below deliberately supplies full padded ladders.

Set L_d=(1+t+...+t^(3-d))/Z, H_d=t^d L_d. At site i let
B_i=1-L_(left gap)-H_(right gap), omitting absent-edge terms.
Condition(2) makes the two bath-label subsets disjoint, so B_i>=0.
Each site projector has rank1 per shell. The largest duplicated eigenvalue
therefore gives the componentwise population bound

    a_i <= [B_i s_i
       +max(H_left s_(i-1),L_left s_i)
       +max(H_right s_i,L_right s_(i+1))]/2.                  (3)

The shared-shell ratio is constant t^d; hence summing shell maxima really
gives the displayed L,H coefficients. Different resonance classes remain
separate. Measurement contractivity implies
r>=sum_i(s_i-a_i)_+ at this fixed input alone.

## 3. An orientation certificate, not an assumed optimal protocol

Orient each edge according to the winning term in(3). A right-site winner
contributes L_d/2 to that column's own site and its left neighbor; a left-site
winner contributes H_d/2 to itself and its right neighbor. Add B_i/2 to
the diagonal. Each column sums to at most B_i/2+L_left+H_right
=(1+L_left+H_right)/2<=1. This is a nonnegative substochastic matrix T with diagonal
at most1/2 and an acyclic directed path off the diagonal. Thus M=I-T has
entrywise nonnegative inverse. For w^T=1^T M^-1,

    1=w^T M s <= (max_i w_i) sum_i((M s)_i)_+,
    r >=1/max_i w_i.                                         (4)

For a walk starting at i, an edge pointing back into the reachable component
makes the opposite component unreachable. Reversing it increases the current
endpoint's diagonal survival and adds that formerly unreachable branch;
it removes no path available from i. Repeat outward on each side.
The fully outward rooted orientation therefore bounds w_i from above.
Solving Mx=e_i in that orientation gives root value2. Each step left
multiplies by q_d=L_d/(1+H_d); each step right by p_d=H_d/(1+L_d).
Indeed a non-root left vertex has diagonal(1-H_d)/2 for its incoming gap d,
so its equation is (1+H_d)x/2=L_d x_parent/2; the right case is analogous.
Consequently

    w_i<=2[1+sum_left_prefixes product q_d
              +sum_right_prefixes product p_d].             (5)

This is a lower-bound relaxation for general finite supports. We do NOT
assert its general finite-support bound is always achievable.

## 4. Three-state Bellman bound on every admissible path

Write A=1/(2t^2), B=t^2/2, P=1+t+t^2 and

    D1=1+2t+2t^2+2t^3, D3=1+t+t^2+2t^3,
    E1=2+2t+2t^2+t^3, E3=2+t+t^2+t^3.

Then q1=P/D1, q2=1/(1+2t^2), q3=1/D3, and
p1=tP/E1, p2=t^2/(2+t^2), p3=t^3/E3. Define

    X=q1(1+q3)/(1-q1q3), X3=q3(1+q1)/(1-q1q3),
    Y=p1(1+p3)/(1-p1p3), Y3=p3(1+p1)/(1-p1p3), C=q3(1+A),
    (F1,F2,F3)=(max(A,X), A, max(C,X3)),
    (G1,G2,G3)=(Y, B, Y3).

F bounds left-arm prefix sums conditional on first gap; G bounds right arms.
The admissible next gaps e satisfy d+e>=4. The relations
C<=A, X3<=A and Y3<=B<=Y imply

    F_d>=q_d(1+max_allowed F_e),
    G_d>=p_d(1+max_allowed G_e).                              (6)

For example F2=q2(1+A); F3=q3(1+max(A,X)). For F1, the alternating1,3
fixed point X=q1(1+X3) shows q1(1+C)<=max(A,X), whichever exceeds the
other. G1=p1(1+Y3), G3=p3(1+Y), G2=p2(1+B).
Induction from the empty terminal arm bounds every finite path sum.

At the root the only adjacent-gap pairs are(1,3),(2,2),(2,3),(3,1),
(3,2),(3,3). For all of them

    F_a+G_b<=A+B.                                            (7)

For2/3 pairs use F3<=A and G3<=B. The remaining comparisons are
X+Y3<=A+B, C+Y<=A+B and X3+Y<=A+B. Missing arms obey the same bound
by dropping a positive admissible opposite arm.

Here are explicit certificates, with positive denominators for0<t<1:

    A-X3=(2t^4-t^3+2t^2-t+1)
          /[2t^2(1+t^2)(2t^2+t+1)],
    Y-B=t[(2-t)+2t^2(1-t)+t^4(1-t)]
          /[2(1+t^2)(t^2+t+2)],
    B-Y3=t^2(t^4-t^3+2t^2-t+2)
          /[2(1+t^2)(t^2+t+2)].

The first numerator is (1-t)+t^2(2-t)+2t^4>0;
the third is (2-t)+t^2(2-t)+t^4>0. For C<=A the difference's
numerator is t-t^2+2t^3>0. Moreover

    A+B-X-Y3 = A+B-X3-Y
      =Q/[2t^2(t^2+t+2)(2t^2+t+1)],
    Q=(2-t)+2t^2(1-t)+2t^4(1-t)+t^6(2-t)+2t^8>0,

    A+B-C-Y
      =R/[2t(1+t^2)(t^2+t+2)(2t^3+t^2+t+1)],
    R=(2-t)+t^2(4-t)+t^4(3-2t)+t^6(3-2t)+t^8(4-t)+2t^10>0.

Exact symbolic controls verify these identities; their positive grouped
forms prove the continuum statements. Equations(4)-(7) give

    r>=1/[2(1+A+B)]=t^2/(1+t^2)^2.

Every finite arm is STRICTLY below its positive supersolution: the terminal
zero continuation has positive slack, propagated by positive multipliers.
The finite maximum of all root rewards is strictly below2(1+A+B), proving
(1). The case of a singleton component gives r>=1/2 directly. K1934's
explicit conserving sequence with both rooted arms growing supplies the
matching infimum; it consumes increasing energy. No infinite-dimensional
unitary or limit exchange is required.

## 5. Released finite-size result: sharp optimum on two occupied energies

Take two occupied energies separated by dDelta, d=1,2,3, with all relevant
shells physically filled by unoccupied ladder levels. Put L=L_d,H=H_d.
The two rooted rewards in(5) are2(1+q_d) and2(1+p_d). Since L>H,
q_d>p_d, so every exact implementation obeys

    r>=R_d=(1+H)/[2(1+L+H)].                                 (8)

This bound IS attained, using weights

    (s_low,s_high)=(L,1+H)/(1+L+H).                           (9)

On a shared shell, the high catalyst level's low-bath input is heavier.
Map its Wv_j into the two occupied-support output positions, its original
position first; map the light input's Wv_j to the two complementary positions.
Here W=[[1,1],[1,-1]]/sqrt2. Complete each output pair with its orthogonal
companion on an unused input column. On singleton occupied shells, map
Wv_j to its original position and an empty one, again original first, then
complete to a full shell unitary. All populated column Gram matrices are
C, including their complex phases. Every matrix unit and entangled input
therefore has the correct channel. Each map stays in its own energy shell.

The squared first coordinate of Wv_j is c=(1/2,1/2,1,1/2).
On support, the actual output is

    a_low=c(1-H)s_low+(1-c)L s_high,
    a_high=c s_high.

At c=1/2 the low deficit vanishes and the high deficit equals R_d.
At c=1 return equals Hs_low=HL/(1+L+H)<=R_d, since2HL<=1+H.
Tracing S eliminates control coherences, so the worst-case marginal distance
is R_d for ALL inputs. This does not assert product return or exact reuse.

A gap>=4Delta, or a nonresonant gap, yields disconnected singleton components
and sharp return1/2 when feasible. Gap3 is worse than2 because
D3-(1+2t^2)=t-t^2+2t^3>0. Gap1 beats2 exactly when

    q1>q2 iff t(2t^3+t-1)>0.

The cubic is strictly increasing and has one root in(0,1). Thus the minimum
over ALL arbitrary nondegenerate spectra with exactly two occupied energies
is min(R1,R2), with

    R2=(1+2t^2)/[4(1+t^2)],
    R1=(1+2t+2t^2+2t^3)/[2(1+t)(2+t+2t^2)].

At t=3/4, a catalyst ladder0,...,7 with occupied levels3,4 has
L=148/175,H=111/175, weights(74/217,143/217), and
r=143/434<17/50. This is the explicit improving architecture, not a
numerical optimizer guess. Two occupied energies refers to the diagonal
energy populations after pinching, not the rank of an arbitrary coherent
state. For t=1/2, separation2 remains better.

## 6. Verification, prior work and limits

The proof transfer from physical shell spectrum to constrained paths and
the Bellman bound is the central dependency. Independent exact controls
reconstruct all small admissible path orientations without the symbolic
proof, test a prohibited triple occupancy, and build every complex shell
unitary for the two-site improvement. Mathematical-input faults follow a
green baseline; report/pin faults establish reporting consistency only.
Universal claims rest on sections2-5, not enumeration or check totals.

Known background includes
[Ng et al.](https://arxiv.org/abs/1405.3039) on catalytic resource limits and
[vom Ende](https://arxiv.org/abs/2207.11189) on bath-spectrum resonance.
No novelty, external expert acceptance or formal proof is claimed.
SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b/AC-F1, source, ledger and canon
are unchanged. There is no native GU or physical particle identification.
Approximate channels require a stable replacement for exact rank doubling;
finite support larger than two requires a matching optimization certificate;
degenerate energy levels change the site-projector rank. Those are separate
questions, not extensions already proved by(1).

Run both frontmatter scripts with Python3/SymPy1.14.0. Producer --write
refreshes its JSON. Internal analytic review is distinct from finite exact
computation and from report/digest consistency.
