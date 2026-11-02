---
title: "K2500 Verifier calibration with imperfect memory confinement"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional supplied-model mathematics; no measured calibration, global finite-budget optimum or native GU realization"
---

# K2500 Verifier calibration with imperfect memory confinement

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
result: K2500
carrier: original C108 verifier with finite retained memory E and declared E0 subspace LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace and operator norm ON=declared_carrier
real_structure: complex adjoint
grading: original target/plane/A/B/N sectors and support-complement memory split
action_owner: repository-construction -- supplied positive quantum instruments and exogenous flags
target: restricted leakage and effect calibration to complete record/reference error MAP-TYPE=evaluation
```

## Result and scope

Exact memory confinement is not necessary for a finite verifier certificate.
Uniform leakage and two compressed test-effect errors on a declared memory
subspace suffice. The construction needs access only to that subspace and a
trusted leakage measurement, rather than coherent preparation of all possible
memory states. It handles arbitrary retained correlations and an untouched
reference. This is a sufficient, deliberately coarse certificate, not an
optimal noise bound or an implemented device.

The result extends K2498's exact invariant-support observation and consumes
K2496's original two-projector theorem. It supplies neither the initial support
assumption nor trustworthy future map-class coverage from its own calibration.
SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b retain their native interacting
physical-state, quotient and domain debts. Source polarity, ledger0.263, canon
and physical credit are unchanged. Positive Hilbert space and instruments are
supplied. No mathematical novelty or external certification is claimed.

## 1. Reference-safe supported repair

Let H=C108 carry the original Q,T and target P. Let E be finite and E0 a
nonzero subspace. Write S=I_H tensor P_E0; S is the support projector, distinct
from the verifier's target P. For a CPTP storage map Phi define

    L=S Phi*(I-S) S,                 0<=L<=ell S,
    ||S Phi*(R) S-R_S||<=epsilon,    R=Q tensor I_E,T tensor I_E.

Here R_S is the restriction to S, and 0<=ell,epsilon<=1. These are uniform
operator bounds over all supported inputs, not averages over a calibration
ensemble. Choose any fixed density tau supported on S and define, on supported X,

    Psi(X)=S Phi(X) S+tr[(I-S)Phi(X)] tau.                 (1)

Both summands are completely positive; their traces sum to tr(X). Thus Psi is
a CPTP map into H tensor E0. It is a proof device, not an added physical reset.
For a supported state rho with reference Rf, set sigma=(Phi tensor id)(rho).
Its amplified repair is

    (Psi tensor id)(rho)=S sigma S+tau tensor sigma_Rf,leak,
    sigma_Rf,leak=tr_HE[(I-S)sigma(I-S)].                 (2)

In general sigma_Rf,leak is not ell times the original reference state.
Its trace p is at most ell. To prove the disturbance bound without a channel
continuity assumption, purify sigma. For a pure state with outside mass p,
the difference between its density and its unnormalized S compression has
trace norm sqrt(4p-3p^2)<=2sqrt(p), by its two-dimensional support. Partial
trace contracts trace norm. Adding the positive trace-p replacement in (2)
therefore gives

    1/2 ||sigma-(Psi tensor id)(rho)||_1
       <=sqrt(p)+p/2<=sqrt(ell)+ell/2.                   (3)

This holds for every reference dimension and supported entangled input. Cap
it at1 if desired. A general full stored-state closeness premise is unnecessary.

## 2. Transfer of the two test effects

Every original test commutes with S. Put r_tau=tr(R tau) in[0,1]. Then

    Psi*(R_S)-S Phi*(R) S
      =S Phi*(r_tau(I-S)-(I-S)R(I-S)) S.

The middle operator lies between -(I-S) and I-S. Positivity of Phi* bounds
this difference between -L and L, hence its norm by ell. The repaired map's
Q/T defects are at most epsilon'=min(1,epsilon+ell). K2496 applies to Psi
on H tensor E0 with exactly the same constant512 and original plane parameters.
Neither the repaired map nor Phi is asserted to be close to identity on all
stored states.

## 3. Adaptive finite records and initial-support errors

For n tests, suppose every history-dependent gap map has these bounds, with
values epsilon_jh,ell_jh. Tests, complements, adaptive record-based choices and
stopping are as in K2496. Exogenous flags may correlate across time but remain
independent of the initial carrier/reference and unaltered by storage. No
additional memory observation or feedback is inserted into deployment.
Initially assume support in S, allowing entanglement with the reference. Then
half trace distance between actual and no-storage outputs, consisting of the
complete record, final target bit and reference after tracing H/E, is at most

    E_n=min(1, sum_{j=1}^{n-1} max_h [
       min(1,sqrt(ell_jh)+ell_jh/2)
       +512 min(1,epsilon_jh+ell_jh)]).                  (4)

First compare actual to repaired storage by replacing gaps EARLIEST TO LATEST.
The common preceding maps are then repaired, so the input to the gap being
compared is supported. All subsequent actual adaptive instruments are CPTP
and contract the error. Each classical history block contributes its probability;
the weights sum to1, with no factor counting histories. Replacing in the
opposite order would use (3) on unsupported inputs and is invalid. After this
comparison, apply K2496 to the all-repaired process, replacing its gaps latest
to earliest as in that proof. At each gap both telescopes have the same
all-repaired prefix, hence the same classical history weights. This permits
the maximum of the sum in (4), rather than requiring separate worst-case
maxima for the two terms. Stopping can
be padded with identity gaps. This proves (4).

A supplied initial half-trace-distance bound delta0 to a supported joint
state adds delta0 if the ideal comparator starts in that supported state.
Comparing actual and ideal processes on the same approximately supported
initial state instead adds 2delta0 by two contractions. If only initial outside
probability p0 is supplied, (1)'s replacement argument gives
 delta0<=min(1,sqrt(p0)+p0/2). Do not silently omit the second initial-state
comparison. Exact initial support is the default in (4).

For ideal acceptance s0, ideal accepted bad mass b0 and desired conditional
error z in(0,1), the K2498 consumer uses

    Delta=(z s0-b0)/(1+z)>0.

E_n<=Delta implies actual error at most z and positive acceptance s0-E_n.
The confidence probability of calibration is a separate epistemic statement,
not a new independent error charged at every gap. Renewal costs still require
independent actual restarts and declared prices.

## 4. Three-effect calibration on the smaller support

Let d=108 dim(E0). For each of G fixed covered map classes reconstruct
S Phi*(Q)S, S Phi*(T)S and L using K2498's d^2 complex basis/superposition
preparations, with binary Q,T and support-complement measurements. The
reconstruction norm radius remains

    C_d=sqrt(8d^2-7d),
    radius=C_d(t+eta),
    t=sqrt(log(6Gd^2/alpha)/(2N)).                       (5)

Here each setting has N independent repetitions of the same map with fresh
unretained environment, alpha in(0,1), and eta is a known probability-level
systematic allowance. The union bound now covers 3Gd^2 estimates. On one
simultaneous confidence event, epsilon is bounded by the largest reconstructed
Q/T residual plus radius, and ell by a certified upper bound on ||Lhat|| plus
radius, both capped at1. Nonphysical reconstructed matrices are allowed because
the triangle inequality suffices. Certified operator bounds are required.

Only E0's dimension and coherent preparation are needed in the settings count.
The full E may be any larger finite space; trusted measurement of I-S is still
required. This does not identify a missing dimension or validate the leakage
measurement from its own output. Unknown preparation/readout error, drifting
maps or uncovered histories invalidate this inference.

For m=n-1>=1 and exact initial support, let q=Delta/m and choose

    epsilon_* =q/1536,
    ell_* =min(q^2/9,2q/3075).                          (6)

Then sqrt(ell_*)<=q/3, (512+1/2)ell_*<=q/3, and
512 epsilon_*=q/3; (4)<=Delta. These are sufficient allocations, not optimal.
Suppose observed certified residuals are at most half their respective targets,
eta=0, and put r=min(epsilon_*,ell_*). It suffices that

    N>=2 C_d^2 log(6Gd^2/alpha)/r^2.                    (7)

There are 3Gd^2N map uses, before preparation/readout/reset prices. A nonzero
systematic radius consumes the same allowance and cannot be reduced by shots.
For fixed d,G,alpha and q down to0, this particular construction scales as
q^(-4), since leakage must be O(q^2). This is only an upper bound from this
proof, not an information-theoretic lower bound or a claim of practical cost.

A second route needs less instrumentation if its dimension penalty is acceptable:
for positive L on dimension d, ell=||L||<=tr(L)=d times average leakage on
the maximally mixed supported state. This is a valid conservative conversion;
using the average itself as ell is invalid.

## 5. Contrary controls and the exact claim ceiling

**Coherent leakage.** A unitary maps one supported a to
sqrt(1-ell)a+sqrt(ell)b with b outside support; tau=|a><a| makes the repaired
output |a><a|. Their half trace distance is exactly sqrt(ell). Thus a uniform
O(ell) full-channel repair bound fails. This does NOT establish optimal
square-root scaling for the final Q/T record: the tests commute with S and
may not observe that coherence. In particular memory-only rotations commute
with both tests and can leave the entire verifier record unchanged.

**Average leakage and later return.** Let dim E0=M. Choose one Q-only A vector
a and one supported memory label0. Gap1 swaps |a,0> with |a,out> and fixes
all else. It commutes with Q and T, so compressed epsilon1=0, but its leakage
effect is rank1: average leakage1/(108M), worst-case ell1=1. Gap2 is identity
on S and swaps A with a T-only B vector on the outside memory label. Its
compressed epsilon2=ell2=0. Starting |a,0>, Q tests before and after gap1 pass,
and the final Q test after gap2 fails with certainty; identity storage passes.
This defeats a dimension-independent substitution of average for worst-case
leakage, even with zero compressed effect error. It does not defeat the
factor-d conversion above or the correctly calibrated theorem.

**Reference repair.** Entangle two supported system states with two reference
labels and leak only one system component. The leakage marginal in (2) is
supported on its corresponding reference label, not the original marginal.
A product replacement with the original reference would erase a real correlation.
The exact probe constructs this channel and checks (2) explicitly.

## 6. Released result: linear leakage for fixed-horizon records

The full-channel repair is useful, but its square root is unnecessary for this
record consumer. Let m=n-1 gaps, exact initial support, and epsilon_j,ell_j be
worst-history compressed effect and leakage bounds at gap j. Put

    q_j=min(1,(sum_{i<j} sqrt(ell_i))^2), q_1=0.
    E <= min(1,sum_j[512 epsilon_j+1024 sqrt(epsilon_j q_j)+q_j])
      <= min(1,1024 sum_j epsilon_j
               +[513 m(m-1)/2] sum_j ell_j).                       (7)

These are complete record/target-bit/untouched-reference bounds, with the same
original verifier algebra and exogenous flags as above. They include adaptive
record-based choices and stopping. q_j bounds **aggregate unnormalized** outside
mass across complete histories; it does not bound every normalized accepted
branch. No postselection normalization occurs in this proof.

For a Stinespring isometry V and projection R=Q or T, write
D_R=(R tensor I)V-VR. Compressed effect errors give
||D_R S||<=sqrt(epsilon). For a word W of length L, telescoping through words
that preserve S gives ||D_W S||<=L sqrt(epsilon). The compressed product
identity gives ||S Delta_W S||<=L(L+1)epsilon/2, where
Delta_W=Phi*(W)-W. Also

    S Delta_W = (D_{W*}S)* V.

Consequently the support-to-outside block is at most L sqrt(epsilon).
The operator-valued original-algebra expansion in K2496 now yields, for any
ideal backward record/reference effect X,

    ||S Delta_X S||<=512 epsilon,
    ||S Delta_X(I-S)||<=512 sqrt(epsilon).

The outside diagonal block has norm at most one: Delta_X is a difference of
effects. For a density with outside mass p, positivity gives
||S rho(I-S)||_1<=sqrt(p(1-p)). The absolute expectation defect is therefore
at most 512epsilon+1024sqrt(epsilon p)+p, uniformly with a reference.

For B=Phi*(I-S), 0<=B<=I and SBS<=ell S. Splitting a purified input into
supported/outside parts gives
sqrt(p_next)<=sqrt(ell)sqrt(1-p)+sqrt(p)<=sqrt(ell)+sqrt(p).
Q/T complete instruments commute with S and preserve aggregate outside mass.
Direct sums over classical histories and Cauchy--Schwarz preserve this recurrence
with history-uniform ell_j, including stopped branches. Induction gives p_j<=q_j.
A latest-to-earliest observable hybrid has actual prefixes and ideal suffixes,
so the preceding expectation estimate proves the first bound in (7).
Young's inequality gives 1024sqrt(epsilon q)<=512epsilon+512q.
Finally q_j<=(j-1)sum_{i<j}ell_i, hence
sum_j q_j<=m(m-1)sum_i ell_i/2, proving the second bound.

For m=1, E<=512epsilon_1, independently of leakage. For epsilon_j=0,
E<=sum_j q_j. Uniform ell produces an O(m^3 ell) sufficient estimate;
no optimal horizon coefficient is claimed. Initial support errors can instead
use the separate triangle-inequality allowances above.

### Calibration consumer and a necessary horizon dependence

For desired error Delta in (0,1) and m>=2 put C_m=513m(m-1)/2,

    epsilon*=Delta/(2048m), ell*=Delta/(2m C_m).

The three-effect certificate of Section 4, with all estimated effects plus their
confidence radii below these thresholds, implies E<=Delta. The same sufficient
shot count 2 C_d^2 log(6Gd^2/alpha)/min(epsilon*,ell*)^2 now scales as
Delta^-2 at fixed m,d,G,alpha with zero systematic bias or bias radius
O(Delta), and the observed-residual half-target allowance of Section 4. A fixed
positive systematic bias floor does not permit taking Delta to zero.
This supersedes the inverse-fourth-power sufficient record allocation for that
fixed-horizon consumer. It does not remove trusted leakage readout, covered map
classes, independent repetitions, preparation bias, or dimension/horizon costs.
For m=1 only the compressed Q/T effect targets are needed.

Horizon dependence cannot be discarded. On memory C^2 supported on |0>, use
N memory-only rotations by theta=pi/(2N), then a gap that swaps the original
A/B sectors only on memory |1>. Rotations commute with Q/T, have epsilon=0,
and ell=sin^2(theta); the last gap has compressed epsilon=ell=0. Starting
A tensor |0>, deterministic Q tests do not disturb the rotations. After N
rotations memory is |1>; the conditional swap makes the final Q bit disagree
with ideal storage with probability one. But sum ell=Nsin^2(theta)<=pi^2/(4N)
tends to zero. This defeats any cap-independent constant times sum ell, while
remaining consistent with (7). The deterministic Q sequence is an admissible
unchanged test-choice law. Exact N=2,3,4 fixtures and rational repeated rotations
check the actual channel and aggregate recurrence. Sharpening the horizon
coefficient remains open; this construction supplies a necessary growing cost,
not matching upper and lower coefficients.
In fact any coefficient c_m in E<=c_m sum ell at zero compressed effect error
must satisfy c_m>=1/[N sin^2(pi/(2N))]>=4(m-1)/pi^2, with m=N+1.
The present universal coefficient is O(m^2), against this necessary Omega(m).

The ordered q_j bound never charges last-gap leakage ell_m. With m=2 and
zero compressed effect errors it specializes to E<=ell_1, and that coefficient
is exactly sharp for every ell_1 in [0,1]: rotate memory by theta with
sin^2(theta)=ell_1, then apply the same outside-controlled A/B swap. The final
Q failure probability is exactly ell_1. Thus the two-gap special case is settled;
the general horizon coefficient remains open.


## Verification, related work and next question

Exact small-carrier fixtures embed into the original target/A/B sectors.
They test complete positivity/trace preservation, complex effect reconstruction,
nontrivial leakage-effect transfer, entangled reference repair, coherent and
averaged leakage counterexamples, hybrid support and rational resource budgets.
Universal inequalities rely on the derivations above and independent review;
finite fixtures are coverage, not independent theorem counts.

Leakage and coherent/incoherent distinctions are established topics: Wood and
Gambetta, *Quantification and Characterization of Leakage Errors*, Physical
Review A97,032306(2018), [arXiv:1704.03081](https://arxiv.org/abs/1704.03081);
Wallman, Barnhill and Emerson, *Characterization of Leakage Errors via Randomized
Benchmarking*, New Journal of Physics18,043021(2016),
[arXiv:1412.4126](https://arxiv.org/abs/1412.4126). These references concern
leakage characterization; no claim that the present certificate is novel or
more efficient follows. The present contribution is the explicit supported
repair plus original-verifier consumer under the stated assumptions.

Next: sharpen the fixed-horizon coefficient or supply a trusted resource-calibrated
memory/readout implementation. Linear fixed-horizon record leakage is now
established, while a cap-independent coefficient is excluded. Exact hardware
costs, future stationarity and native physical realization remain unsupplied.


[Exact probe](../../tests/channel-swings/k2500_reachable_memory_leakage_probe.py) and [saved report](../../lab/process/k2500-reachable-memory-leakage.json).
