---
title: "K2504 Five-setting supported verifier calibration with finite confidence"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional supplied-model mathematics; no native GU realization, experimental certification or global stopping optimum"
---

# K2504 Five-setting supported verifier calibration with finite confidence

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
result: K2504
carrier: original C108 Q/T verifier with retained memory E and supported subspace E0 LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace or original failure-inclusive probability cost ON=declared_carrier
real_structure: complex adjoint for effects; real probabilities for stopping
grading: original verifier sectors or finite stopping stages
action_owner: repository-construction -- supplied instruments and original probability law
target: operator-norm effect and leakage bounds from trusted sector-mixture wrong-outcome counts MAP-TYPE=evaluation
```

## Result and scope

The complete-record consumer of K2500/K2502 does not require full process
tomography. Five trusted mixed-state preparation/measurement distributions per
fixed map class suffice to bound its two compressed projection-effect errors
and support leakage. The guarantee includes a finite-confidence rule, explicit
systematic-error floors, and a sharp coherent-rotation obstruction to replacing
the square-root effect bound by a linear wrong-count bound.

Let H=C108, k=dim(E0)>=1, S=I_H tensor P_E0 and d=108k. Storage Phi is CPTP
on the complete retained H/E carrier. Every reusable environment is included
in E; any inaccessible fresh dilation environment is traced out. Q,T are the
original fixed projections, extended by the identity on E. Their supported
ranks are 10k and12k. Initial deployment support, original readout instruments,
exogenous flags and worst-history map-class coverage are supplied premises,
not facts learned by these five tests. No native physical bridge is asserted.

SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b still require the interacting
physical quotient/domain. Source polarities, ledger0.263 and physical credit
are unchanged. This is independent positive-Hilbert-space mathematics, not a
hardware experiment, device-independent test, novelty claim or proof-assistant
certificate.

## 1. Positivity replaces coherent tomography

For any effect 0<=A<=I and orthogonal projection R on a finite carrier, put
D=A-R and B=R(I-A)R+(I-R)A(I-R). Direct multiplication gives

    B-D^2=A-A^2>=0.

The two blocks of B are positive, so

    ||A-R||^2 <= max(||R(I-A)R||,||(I-R)A(I-R)||).       (1)

If R has rank r with 0<r<d, measure the wrong outcome on inputs R/r and
(I-R)/(d-r). The means p_plus,p_minus obey

    epsilon_R=||A-R||
      <=min(1,sqrt(max(r p_plus,(d-r)p_minus))).         (2)

Indeed a positive matrix has largest eigenvalue at most its trace. Zero-rank
blocks may simply be omitted. For A=S Phi*(R) S on the supported carrier,
A is an effect and the target is R_S=SR, because S commutes with Q,T.
Thus (2) applies to the compressed errors used in K2500/K2502; it does not
assume Phi preserves S or commute with either projection.

For the positive leakage effect L=S Phi*(I-S) S, the full uniform input S/d
has leakage mean p_L, and ||L||<=min(1,d p_L). The five settings and ranks are

| Input distribution | Wrong event | Rank used |
|---|---|---:|
| Q_S/(10k) | Q fails | 10k |
| (S-Q_S)/(98k) | Q passes | 98k |
| T_S/(12k) | T fails | 12k |
| (S-T_S)/(96k) | T passes | 96k |
| S/(108k) | output outside S | 108k |

They are five distributions, potentially implemented by randomizing among
many independently trusted basis preparations. They are not five pure states,
nor a reconstruction of the channel. Coherent preparation across all d^2
operator coordinates is unnecessary for this particular upper bound.

## 2. A finite-confidence acceptance rule

Freeze G map classes and all sample counts before sampling. At each setting,
trials are independent fresh-reset Bernoulli trials for one fixed map. Distinct
settings need not be mutually independent. Set beta=alpha/(5G), 0<alpha<1.
For x wrong outcomes in n>=1 trials define u(x,n) by

    sum_(j=0)^x binom(n,j) u^j(1-u)^(n-j)=beta, x<n;
    u(n,n)=1.                                          (3)

The left side is strictly decreasing on(0,1) for x<n. For any true p, the
set of counts with u(X,n)<p is an initial segment whose binomial probability
is at most beta. Hence Pr_p[p>u(X,n)]<=beta, including endpoint cases.
The union bound makes all 5G bounds simultaneous with probability at least
1-alpha. Reusing a covered map at many deployment gaps does not spend alpha
again; the resulting simultaneous operator event already controls each use.

If known preparation half-trace error is eta_p and readout effect operator
error is eta_m, contraction of trace distance and effect duality give an
absolute probability bias at most eta=eta_p+eta_m. Replace each u by
v=min(1,u+eta). Then, on the simultaneous event,

    epsilon_g <= min(1,sqrt(max_i r_i v_gi)),
    ell_g <= min(1,d v_gL),                             (4)

where i ranges over the four projection sectors. These are support-wide
operator bounds, so K2500/K2502's untouched-reference conclusions apply.
Calibration does not have to initialize an entangled reference; the later
reference claim comes from the existing operator theorem, not state sampling.

Fixed-n intervals are not automatically safe under data-dependent stopping,
repeated peeking, after-data choice of map classes or post hoc confidence
allocation. Such designs require separately valid sequential inference.
Unverified preparation/readout bias, drifting maps or untested history classes
are not covered. This is a confidence-qualified certificate, not certain truth.

## 3. Resource reduction and its actual limits

Suppose all wrong counts are zero and systematic biases are zero. With
L=log(5G/alpha), equation(3) gives u=1-exp(-L/n)<=L/n. Sufficient sample counts
for target positive allowances epsilon_star and ell_star are

    n_i=ceil(r_i L/epsilon_star^2),
    n_L=ceil(d L/ell_star),
    total per map <= L(2d/epsilon_star^2+d/ell_star)+5.  (5)

The four sector ranks sum to2d. Thus the zero-count passing certificate has
inverse-square effect accuracy and inverse-linear leakage accuracy, with
linear dimension scaling in trial count and five distributions. It does not
promise zero counts or any passing probability for an arbitrary noisy map.
For nonzero counts use(3), not(5) as if its premise held. A systematic bias
eta_i imposes epsilon_star^2>r_i eta_i for positive statistical slack, and
ell_star>d eta_L; extra shots cannot remove these floors.

A concrete sufficient allocation illustrates the gain without claiming a
practical experiment. Take k=G=1, alpha=1/100, epsilon_star=ell_star=10^-6,
and use log500<7. Choosing n_i=r_i*7*10^12 and n_L=108*7*10^6 gives exactly

    total = 1,512,000,756,000,000 trials.                (6)

This is enormous. Nevertheless, K2500's stated three-effect tomography design
uses3d^2=34992 settings, with per-setting sufficient count
ceil(2(8d^2-7d)log(6Gd^2/alpha)/min(epsilon_star,ell_star)^2). Since
log6998400>15 and8d^2-7d=92556, its prescribed total exceeds

    34992*2*92556*15*10^12,

more than sixty million times(6). This compares two conservative stated
sufficient designs under their respective passing-data assumptions; it is not
a lower bound on all tomography, nor a speed claim about hardware preparation.
The sector design's systematic precision demand can still dominate its cost.

For a genuine recorded-output consumer, reuse one covered map at two gaps.
K2500's ordered bound with epsilon_1=epsilon_2=ell_1=10^-6 gives

    E <=512(2*10^-6)+1024 sqrt(10^-6*10^-6)+10^-6
       =2049/10^6 <1/100.                              (7)

Last-gap leakage is irrelevant to this bound. The generic K2502 bound is
looser for this allocation; take the minimum, not whichever theorem is newer.
If ideal acceptance has s0>=1/2 and bad-and-accepted mass b0=0, (7) bounds
actual conditional bad probability by E/(s0-E)<=2049/497951<1/200.
More generally require E< s0 and E<=(z s0-b0)/(1+z)>0 for tolerance z.
This hypothetical consumer requires the stated ideal margins and deployment
premises. No such experiment or calibrated residual was supplied here.

## 3a. Released pooled-trial confidence protocol

The same five distributions can be sampled through one labeled randomized
protocol. Freeze positive target allowances and put

    c_i=r_i/epsilon_star^2 (four sectors), c_L=d/ell_star,
    W=sum c=2d/epsilon_star^2+d/ell_star.

At each independent fresh trial, draw a label with probability c_i/W and use
that distribution and its stated wrong-event readout. Labels are independent
of the fixed map and its fresh environment; the map must not secretly change
with the label. The pooled wrong-bit probability is p=sum_i(c_i/W)p_i, so

    Wp=sum_(four) r_i p_i/epsilon_star^2+d p_L/ell_star.

All terms are nonnegative. Therefore Wp<=1 implies every bound(2) and the
leakage allowance simultaneously. For G fixed map classes use the single
binomial upper limit U per class at alpha/G. If known setting biases are
eta_i, use eta_eff=sum_i(c_i/W)eta_i. The sufficient acceptance gate is

    W(U+eta_eff)<=1.                                   (7a)

With zero wrong counts and zero bias,
N=ceil(W log(G/alpha)) suffices per map class. This reduces confidence
allocation overhead without changing the five physical input/readout types.
For the example(6), log100<5 gives the explicit sufficient pooled count
1,080,000,540,000,000. The record/postselection consequence(7) is unchanged.

This gate is stronger than checking each allowance individually; it can reject
maps which pass all five individual inequalities. If each of the five
normalized contributions equals1, the separate allowance conditions hold but
Wp=5. Thus pooling is a sufficient zero-count resource alternative, not a
uniformly more powerful or minimax-optimal test. Preserve label-resolved data
if nonzero errors make the separate confidence region more useful. One may
choose a valid predeclared confidence allocation covering both analyses, but
may not silently try both at full alpha and report whichever passes.

The weights are optimal within this particular scalar-domination construction.
For arbitrary positive weights q_i summing to1, the smallest coefficient C
such that c_i p_i<=C sum_j q_j p_j for every nonnegative mean vector is
max_i(c_i/q_i). Its q-weighted average is W, so C>=W, with equality exactly
when q_i=c_i/W. This is not a universal physical calibration optimum: it
ignores physical relations among the five means and richer test designs.

There is also a physical sharp zero-count boundary for the chosen protocol
when an outside-memory direction exists and0<ell_star<1. Rotate one original
A-sector vector and its outside-memory copy, acting identically elsewhere.
The unitary commutes with both Q,T, but its supported leakage effect is
L=t|a,e0><a,e0| with0<t<1. Four projection wrong means are0 and p_L=t/d.
The pooled wrong probability is t/(ell_star W). For t>ell_star the claimed
leakage allowance is false, yet N independent pooled trials are all correct
with probability(1-t/(ell_star W))^N. Taking t down to ell_star proves that
any rule always accepting the all-correct transcript with per-class risk
beta must satisfy (acceptance here includes every realized label sequence
with zero wrong outcomes; label-selective acceptance is excluded)

    N>=log(1/beta)/[-log(1-1/W)].                       (7b)

The exact binomial zero-count rule has precisely this threshold, rounded up
to an integer. Thus it is sharp for that fixed randomized protocol and
all-zero acceptance condition. The elementary N>=W log(1/beta) allocation
is slightly conservative. No lower bound for unrelated experiments follows.

With nonzero eta_eff, set v=1/W-eta_eff. A positive statistical margin
requires v>0; zero-count acceptance follows from
N>=log(G/alpha)/[-log(1-v)], or the simpler
N>=W log(G/alpha)/(1-W eta_eff). Pooling can have a worse combined systematic
floor than separate tests, so its unbiased resource advantage is not universal.
Trivial allowances equal to1 need no test and can be omitted when comparing
efficiency; the nontrivial comparison here uses allowances strictly below1.

Labels must be iid, not deterministic quotas: the confidence probability
averages over label randomization and outcomes. It is not automatically
conditional on the realized label counts. Trusted label weights and fresh fixed-map trials are necessary. Incorrect
weights can starve the one defective sector, and a label-dependent adversary
can defeat inference about the common deployment map. Systematic error enters
as the weighted sum in(7a); pooled trials do not self-calibrate trusted inputs.
This extension requires no new elementary states, experiment or hardware claim.

## 4. Sharpness and restricted identification limits

Choose one original A-sector vector (Q=1,T=0) and one original B-sector vector
(Q=0,T=1), at a fixed supported memory label. Rotate their span by angle theta
and act identically elsewhere. For t=sin^2(theta), both compressed effect
errors are sqrt(t), each of the four sector wrong means is t/r_i, and leakage
is0. Both the square-root conversion and the factor r_i in(2) are attained.
A linear claim epsilon<=max_i r_i p_i would be false. Small average wrong
probability is not small operator error without the square root and ranks.

More generally, on an r-dimensional sector a trusted density rho has least
eigenvalue lambda_min<=1/r. For a positive wrong-effect block B,
tr(rho B)>=lambda_min ||B||. A rank-one block on a least-eigenvalue vector
saturates the conversion; the uniform mixture maximizes lambda_min. This is
minimax optimality only for a single-input positive-block conversion. If
lambda_min=0, arbitrary positive defect on an unseen direction is invisible.
A storage map that changes only an unprepared memory label illustrates this
failure while initialized-memory tests pass. Global memory support and map
coverage remain explicit inputs.

The rotation also gives a restricted sample lower bound. For this lower-bound
experiment, take all trials across settings mutually independent; this is an
allowed subclass of the broader confidence model. For fixed counts
n_i, the all-correct transcript has probability

    P0(t)=product_i (1-t/r_i)^n_i.                       (8)

Suppose a deterministic rule accepts that transcript as certifying
epsilon<=epsilon_star. For every t>epsilon_star^2 it must have P0(t)<=alpha;
otherwise its false-certification risk exceeds alpha on this physical unitary.
Thus sum_i n_i[-log(1-t/r_i)]>=log(1/alpha). As t decreases to epsilon_star^2,
with epsilon_star<1, the total projection-setting count obeys

    sum_i n_i >= log(1/alpha)/[-log(1-epsilon_star^2/(10k))]. (9)

This is asymptotic order k epsilon_star^-2 log(1/alpha) at small epsilon_star,
matching(5)'s dimension/accuracy order for fixed G and these fixed rank ratios.
It is not a universal channel-testing lower bound. It assumes this restricted
five-setting design and acceptance of the all-correct transcript; randomized
acceptance multiplies P0 by the acceptance probability on that transcript.
Untrusted readout, richer coherent probes and entirely different tests fall
outside this comparison.

## 5. Evidence and remaining work

The universal claims follow from the displayed positivity identity, trace
bound, binomial inversion and exact physical counterchannel. Finite symbolic
and rational probes independently exercise nonprojective effects, coherent
rotation, original-sector multiplicities, biased preparations, unseen memory,
confidence coverage, resource counts and the recorded-output consumer.
They are not independent theorem counts or experimental observations.

Exact binomial inversion is the established Clopper-Pearson construction;
[NIST's instrument-confidence report](https://www.govinfo.gov/content/pkg/GOVPUB-C13-477b14161dac9dab920bf2cf1d6d4ac5/pdf/GOVPUB-C13-477b14161dac9dab920bf2cf1d6d4ac5.pdf)
describes its confidence-interval form. The one-sided rule and its coverage
proof are given here, so no new statistical method or novelty is claimed.

A trusted preparation/readout implementation, actual data, stable map classes,
supported initial state and meaningful calibration-to-deployment guarantees
remain missing. The present result removes full tomography as a mathematical
prerequisite for this particular supplied verifier; it supplies none of those
physical inputs. A lower-cost conditional design using richer probe states or
structured noise may change the resource frontier, but requires a new proved
model rather than treating sample counts as realized hardware.


[Exact probe](../../tests/channel-swings/k2504_verifier_sector_calibration_probe.py) and [saved report](../../lab/process/k2504-verifier-sector-calibration.json).
