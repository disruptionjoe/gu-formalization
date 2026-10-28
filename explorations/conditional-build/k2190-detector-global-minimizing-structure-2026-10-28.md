---
title: "K2190 Detector multiplier sign reduction and branch-sign obstructions"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied positive free-field binary diagonal instrument, vacuum output field energy only
scripts:
  - tests/channel-swings/k2190_detector_global_minimizing_structure_probe.py
---

# K2190 Detector multiplier sign reduction and branch-sign obstructions

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2190 minimizing sign reduction and branch-sign counterexamples
carrier: fixed positive scalar Fock vacuum and photon-added signal with binary diagonal local occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and free vacuum output energy ON=declared_carrier
real_structure: positive square-root diagonal Kraus followed by one real squeeze per reported outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction: supplied free Hamiltonian and instrument class
target: finite-budget lower energy envelope and inverse contrast bound MAP-TYPE=intertwiner
```

## Result and scope

At every nonzero-contrast minimizing detector whose two optimizing squeezes
are at most1, the contrast multiplier has strictly positive signed product
eta*d. For positive d, the complementary squeeze is always below1; thus any
remaining nonpositive multiplier must have s1>1>s0 and a precisely bounded
Dirichlet defect. This is a new partial sign theorem, not global monotonicity.

Two exact full-tail counterconstructions eliminate tempting extensions:
individual Q_z can be positive when s_z>1, and it can also be positive when
the branch has NEGATIVE signed contrast. The second yields a positive-contrast
counterexample even to replacement by outcome0, closing the sign-specific
loophole in K2186. All fixed replacement biases fail somewhere on the
positive-contrast domain. These profiles are not minimizers.

Scope is the supplied positive scalar Fock vacuum, photon-added signal,
binary diagonal square-root Kraus instrument and one real squeeze per
reported outcome. Energy means vacuum output FIELD energy, excluding
apparatus, clock, preparation, switching, reset and total work. SC-META-53
remains UNCERTAIN; LT-SM8/LT-GR6b, ledger0.263, source, canon and physical
quotient are unchanged. No joint uniqueness, global saturation, sharper
half-contrast bracket, proof-assistant, external-expert or novelty claim.

## 1. Exact orientation of the unresolved minimizing regime

Use [K2188](k2188-detector-variational-structure-2026-10-28.md):

    p_n=(3/4)4^-n, x_n=p_n e_n, y=p-x, d=sum(3n-1)x_n,
    R(z)=sum(n+1/2)z_n, T(z)=sum(n+1)sqrt(z_n z_(n+1)),
    A(s)=41s^2/6+3/(2s^2), C=40/3,
    H=min_(s1,s0)[R(x)A(s1)+R(y)A(s0)-C(s1T(x)+s0T(y))+35/18],
    Ep(s)=(5/6)A(s)-(2C/3)s+35/18.

Every nonzero branch has unique positive squeeze satisfying
R(z)A'(s_z)=C T(z). For a positive branch define D(z)=DT(z)[p] and
Q_z=Ep(s_z)-Cs_z[D(z)-2/3]. At an interior exact-contrast minimizer,
K2188 proves Q_x=Q_y=H-eta*d, with absolutely convergent derivatives.
For these optimizers 0<|d|<3/4 and all coordinates are strictly interior.

Let D_e=sum(n+1)p_n(sqrt(e_(n+1))-sqrt(e_n))^2 and similarly D_(1-e).
Since R=(5/6)w+d/3, the K2188 Dirichlet identity gives exactly

    T(x)=(4/5)R(x)+(3/20)d-D_e/4,
    T(y)=(4/5)R(y)-(3/20)d-D_(1-e)/4.             (1)

A'(1)=4C/5. Thus if d>0, necessarily s0<1, and

    s1<=1 iff D_e>=3d/5.                         (2)

This holds for any nonzero capped branches, not just minimizers. In
particular both squeezes>=1 is impossible at nonzero contrast.

## 2. A proved positive multiplier region

Define B(s)=A(s)-sA'(s). At optimizing squeezes,

    H=R(x)B(s1)+R(y)B(s0)+35/18, B'(s)=-sA''(s)<0.

Let smax=max(s1,s0)<=1. Since R(x)+R(y)=5/6,

    H >= (5/6)B(smax)+35/18
       = Ep(smax)+(5/6)smax[A'(1)-A'(smax)].       (3)

This is strict relative to Ep(smax) for nonzero contrast: if smax<1,
the last term is positive; if smax=1, the other squeeze is below1 by(1)
and its branch has positive R, making the first inequality strict.
Since D(z)>=2/3 by the ratio arithmetic-geometric mean inequality,
Q_z<=Ep(s_z). Apply this to the branch with smax and use Q=H-eta*d:

    eta*d>0.                                    (4)

For d>0 this proves eta>0 whenever D_e>=3d/5 at the minimizing profile.
Outcome exchange covers negative d. By K2188, eta=F'(d) at differentiable
frontier points. Any remaining failure of the sign must occur specifically
in s1>1>s0 with D_e<3d/5. The theorem does not assert that every minimizing
profile satisfies(2), nor that straddling gives a negative multiplier.

## 3. A positive-squeeze branch can still have Q>0

This counterconstruction prevents completing(3) by asserting Q_z<=0 whenever
s_z>=1. Fix L>=4 and N>=L+1. Put epsilon=4^-N,
a=p_(N+L)=(3/4)epsilon*4^-L, rho=2^(N-L), and define

    e_n=epsilon                         n<N,
    e_n=4^(n-N-L)                       N<=n<N+L,
    e_n=1/4                             n>=N+L.

Thus z_n=p_n e_n is flat on the L-point middle block, with positive
geometric tails and strict caps. Direct infinite sums give

    w=epsilon-epsilon^2+a(L+1/3),
    R=(5/6)epsilon-epsilon^2(N+5/6)
       +a[(L+1/3)N+L^2/2+L/3+5/18],
    d=a[(3L+1)N+(3/2)L(L-1)]-3N epsilon^2,
    T=(2/3)epsilon-2epsilon^2(N+1/3)+2Na/rho
       +a[(L-1/3)N+L^2/2+L/6+2/9],
    D-2/3=[N p_(N-1)/4](rho+rho^-1-2)
           +(1/8)sum_(n=N)^(N+L-2)(n+1)p_n.       (5)

For fixed L and N tending to infinity,
T/R tends to (3L-1)/(3L+1)>4/5. Thus s_z tends to a fixed s*>1,
while D-2/3=O(N2^-N) tends to0, and Q_z tends to Ep(s*)>0.
This is an explicit asymptotic construction, not a formal stationary tail.
The probe additionally certifies a finite L4,N40 witness with 1011/1000<s_z<253/250 and Q_z>1/1000
by exact rational squeeze bracketing. It independently sums the full moments and derivative
rather than trusting(5). No minimizing property is asserted.

## 4. Even a negative-contrast branch can have Q>0

The next plausible shortcut is Q_z<=0 when d(z)<0, because the complement
of a positive-contrast detector has negative contrast. It is also false.
Let r=3/13, a_n=(1-r)r^n, choose integer N=40 and b=3/(100N-33), and set

    z_n=a_n+b*1_(n=N), u=sqrt(1+b/a_N), h=sqrt(r).

This is a positive geometric sequence plus one isolated spike. It has

    w=1+b, R=(83/100)(1+b), d=-(1+b)/100,
    T=h/(1-r)+[N/h+(N+1)h]a_N(u-1),
    D=(2/3)[h+1/(4h)]
      +(1/2){N p_(N-1)[h(u-1)+(u^-1-1)/(4h)]
         +(N+1)p_N[h(u^-1-1)+(u-1)/(4h)]}.        (6)

The geometric baseline is summed to infinity and exactly two edges are
corrected. Scale z by lambda=p_N/[2(a_N+b)]. This makes e_N=1/2;
elsewhere a_n/p_n=(40/39)(12/13)^n and lambda<39/40, so every coordinate
is strictly between0 and p_n. Both squeeze and D,Q are invariant under
positive scaling, and signed contrast remains negative.

The exact probe encloses the positive square roots by rational integer-
square-root bounds and verifies

    9723/10000 < s_z < 6079/6250 <1,
    Q_z > 1/5000.                               (7)

For example the conservative lower bound is greater than0.00025098.
No floating optimizer or finite-tail substitution enters this certificate.
The failure is structural: normalized mean below1/3 does not prohibit a
small distant spike from changing the moment/squeeze relation while its
p-weighted derivative cost is small. As N tends to infinity, the mean
stays33/100, T tends to sqrt39/10, and the derivative perturbation tends
to0 because 1/(4sqrt(r))<1. These limits explain the construction; the
finite certificate(7) is sufficient for its claim.

## 5. Released positive-contrast outcome-zero obstruction

Let y=lambda*z from section4 and x=p-y. Then d(x)=lambda*(1+b)/100>0.
For the beta0 replacement path x_t=(1-t)x, contrast strictly decreases.
The exact full-tail derivative identity of K2186 gives

    H'(0)=Q_y-H.

This derivative is legitimate: away from the one spike, the ratios are
geometric and the complement approaches p, so the derivative series is
absolutely convergent. There are no zero coordinates.
At common squeezes1, H<=C[2/3-T(x)-T(y)]. For 0<=e,f<=1,
sqrt((1-e)(1-f))>=1-e-f (if e+f>1 the right side is nonpositive;
otherwise square and use e+f-(e+f)^2+ef>=0). Summing with weights
(n+1)p_n/2 gives

    H <= C[2/3-T(x)]
       <= C lambda[(5/2)M_z+w_z/2] <1/10000,     (8)

where M_z=(33/100)(1+b). All terms in the last bound are rational.
Combining(7),(8) proves H'(0)>1/10000 at a POSITIVE-contrast profile.
K2186 already gives positive-contrast counterexamples for every fixed
beta>0. The new beta0 witness therefore closes the remaining sign
loophole: every fixed beta in[0,1] fails universal energy descent even
when restricted to d>0. The witness may depend on beta. Neither this
nor section4 contradicts minimizing Q_x=Q_y or proves a frontier failure.

## Verification and remaining question

The written minimizing-sign argument and infinite-tail counterconstructions
are distinct from finite rational/symbolic controls. The probe checks exact
moment identities, monotonic squeeze brackets, outward radical enclosures,
full tails and equation/data faults after a green baseline. Independent
internal review challenges both the analytic proof and the transfer.

Global saturation F=V and joint uniqueness remain open. One sufficient
remaining route is a genuinely PAIRED inequality min(Q_x,Q_y)<=0, which
would imply eta*d>=H>0 at nonzero-contrast minimizers. None of the
single-branch statements refuted above is that paired inequality; no proof
of it is claimed. Alternatively construct or exclude actual minimizing
straddling profiles using the full recurrence/global comparison. Reversible
birth-death smoothing preserves caps/probability and contracts contrast,
but an energy-descent proof for the jointly squeezed objective is unsupplied.
Retain K2182 endpoint theorem, weak-contrast353/170 and K2176 half-contrast
bracket. A complete nonconvex optimizer and physical controller with shared
stable Hamiltonian/preparation/reset costs are separate unfinished work.
