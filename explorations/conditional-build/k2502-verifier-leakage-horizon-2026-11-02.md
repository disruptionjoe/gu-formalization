---
title: "K2502 Verifier leakage with optimal weak-error horizon scaling"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional supplied-model mathematics; no native GU realization, measured calibration or global stopping frontier"
---

# K2502 Verifier leakage with optimal weak-error horizon scaling

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
result: K2502
carrier: original C108 verifier with finite retained memory E and supported memory subspace E0 LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace or original failure-inclusive expected probability cost ON=declared_carrier
real_structure: complex adjoint for instruments; real probabilities for stopping
grading: original verifier sectors or ordered finite stopping stages
action_owner: repository-construction -- supplied positive instruments and original probability law
target: complete record and untouched-reference error under supported effect preservation MAP-TYPE=evaluation
```

## Result and scope

For the original Q/T verifier, exact preservation of its two effects on a
supported memory subspace gives a complete-record error bound with linear,
rather than quadratic, growth of the coefficient multiplying total leakage.
The coefficient has the sharp weak-leakage limit m-1 for m storage gaps.
This closes the order gap left in K2500. It does not establish exact preservation
from finite calibration data. Both a block-dephased subclass and a general coherent-error extension admit
nonzero effect errors below; the general bound has conservative constants.

Let S=I_H tensor P_E0, and suppose the initial H/E/reference state is supported
on S. At each gap j and every history h in the declared padded adaptive map tree require

    S Phi_jh*(R) S=R_S, R=Q,T,
    0<=S Phi_jh*(I-S)S<=ell_j S, 0<=ell_j<=1.            (1)

The ell_j are worst-history bounds, covering hybrid-reachable histories as well as actual ones. Original tests, their complements, adaptive
record-based choices/stopping, final target bit and exogenous flag law are
unchanged. Flags are independent of the initial carrier/reference and unaltered
by storage; they may correlate across time. Every reused environment belongs
in E; dilation environments below are inaccessible and fresh. No normalized
postselected branch bound is assumed. Trace out H/E at the output.

For m>=2, put N=m-1 and a_j=1-sqrt(1-ell_j). Half trace distance E of the
actual complete record/final-target-bit/untouched-reference output from the
no-storage output satisfies

    E<=min(1, 2 sum_(j<m) a_j
                  +2 sum_(i<j<m) sqrt(ell_i ell_j))
      =min(1, (sum_(j<m) sqrt(ell_j))^2+sum_(j<m) a_j^2)
      <=min(1,m sum_(j<m) ell_j).                        (2)

For m=0 or1, E=0. Last-gap leakage is absent. K2500's sharper ordered bound
E<=sum_j min(1,(sum_(i<j)sqrt(ell_i))^2) remains available at zero effect
error; take the smaller upper bound. In particular its exact m=2 law E<=ell_1
is retained. Equation (2) is not claimed to have the optimal finite-error constant.

All statements are supplied finite positive-Hilbert-space mathematics.
SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b still require native interacting
state, quotient and domain constructions. Source polarities, ledger0.263 and
physical credit are unchanged. No novelty, external-expert, proof-assistant or
hardware certification is claimed.

## 1. Supported intertwining and a transparent comparison

For a Stinespring isometry V of Phi, exact compressed preservation of a
projection R implies (R tensor I)V S=V R S. Indeed the positive defect
D_R*D_R has zero compression, by the identity in K2496. Since Q,T preserve S,
word telescoping gives this identity for their generated algebra. It also holds
with operator coefficients on an untouched reference. The original target P
belongs to that algebra, as K2496 proves.

For j<m, suppress history and set

    A=(S tensor I)V S, L=S V*(I-S)V S,
    H=sqrt(I_S-L), B|S=A H^(-1).                         (3)

For ell<1, H is invertible. A intertwines the algebra, so H commutes with it
and B|S is a supported algebra-intertwining isometry. Extend B to the whole
carrier by mapping S-perp with the identity system action and a fresh,
orthogonal environment tag. This makes B globally transparent to the verifier
algebra, without asserting a physical reset or deployable construction.
The actual V is embedded in the same larger dilation with zero new-tag component.

Write C=(B|S)*V(I-S). Since (B|S)*V is a contraction and its S block is H,

    C C*<=I_S-H^2=L,
    ||C||<=sqrt(ell), ||H-I_S||<=1-sqrt(1-ell)=a.         (4)

At the last gap use B_m|S=V_m S, without compressing its output, and extend
with an orthogonal tag. It still intertwines the algebra, and now

    (B_m|S)* V_m S=I_S, (B_m|S)*V_m(I-S)=0.              (5)

The ideal B process has supported prefixes through the last gap and, by exact
algebra transparency, precisely the no-storage reduced recorded-output law.
Only its last output may leave S. If any earlier ell=1 the coarse capped
bound is already1, so the polar inverse is unnecessary. This handles the
endpoint without a singular inverse or continuity assumption.

## 2. Cross-expectation telescope, including adaptive records

Purify the initial state and dilate every channel and complete instrument.
Keep permanent copies of the classical history so its blocks stay orthogonal;
use controlled direct sums for adaptive choices. Fix an exogenous flag sequence
first and average only after the proof. Let |u> and |v> be actual and ideal
normalized terminal pure states in this common dilation.

For any effect F on the final record, target bit and reference, define

    c_F=<v|F|u>-<v|F|v>.

Telescope the actual ket by replacing suffixes with the ideal B process,
leaving actual prefixes and the supported ideal bra prefixes. Every ideal
suffix pulls F back to an effect X in the original Q/T algebra with reference
coefficients, separately on each history. This is the same algebra closure
used by K2496, not a bound on arbitrary stored-state effects. Intertwining B
moves X through its adjoint. Thus gap j contributes the block row

    <ideal_prefix| X [S B_j* V_j-S] |actual_prefix>.

Equations (4) bound its absolute value by a_j+sqrt(ell_j)*sqrt(p_j), where
p_j is aggregate unnormalized outside mass in the actual prefix. The same
estimate survives the history direct sum by Cauchy-Schwarz: the two complete
prefix norm squares sum to1. No history count or normalization factor appears.
The last gap contributes zero by (5).

The K2500 purified leakage recurrence gives

    sqrt(p_j)<=sum_(i<j) sqrt(ell_i).

Complete Q/T instruments commute with S and preserve aggregate outside mass.
Consequently |c_F|<=K, with

    K=sum_(j<m) a_j+sum_(i<j<m) sqrt(ell_i ell_j).         (6)

The same bound applies to I-F. For D=u-v and d_F=<u|F|u>-<v|F|v>,

    d_F=2 Re(c_F)+<D|F|D> >=-2K,
    d_F=-2 Re(c_(I-F))-<D|(I-F)|D> <=2K.

The second identity uses equal total norms. Supremizing over F proves (2)
in half trace norm, with arbitrary reference dimension. Padding stopped
branches with identities preserves the argument. A raw full-state norm hybrid
would lose this linear leakage conclusion; the two complementary output
effects are essential.

## 3. Released sharp weak-leakage coefficient

If max_(j<m) ell_j<=delta<1, then

    a_j^2=ell_j^2/(1+sqrt(1-ell_j))^2
         <=delta ell_j/(1+sqrt(1-delta))^2.

Cauchy-Schwarz in (2) gives the uniform bound

    E <= [N+delta/(1+sqrt(1-delta))^2] sum_(j<m) ell_j.   (7)

The leading coefficient N=m-1 cannot be reduced. Start in an original A-sector
vector and memory |0>. Perform N memory-only rotations of angle theta, each
followed by deterministic Q tests, then one gap swapping original A and B only
when memory is |1>. The first N gaps have epsilon=0 and ell=sin^2(theta);
the last gap has compressed epsilon=ell=0. Ideal Q always passes, whereas the
actual final failure probability is sin^2(N theta). Therefore

    E / sum ell =sin^2(N theta)/(N sin^2(theta)) -> N.    (8)

This is an actual original-sector construction, not merely a recurrence
saturator. Together (7)--(8) prove sharp asymptotic horizon coefficient m-1
for fixed m as the worst per-gap leakage tends to0. No joint m/delta limit
or exact finite-error supremum is asserted. The effect of intermediate tests
is explicit: they see the unchanged A sector until the final controlled swap.

## 4. Released dephased-output certificate with nonzero errors

Suppose, for j<m and every supported operator X, the actual storage map obeys

    Phi_j(X)=S Phi_j(X)S+(I-S)Phi_j(X)(I-S).              (9)

This is a map-level identity, including reference amplification, not a property
inferred from a finite sample or a new dephasing operation added to deployment.
Allow compressed Q/T effect error epsilon_j at every gap. Then

    E<=min(1,sum_(j<m)ell_j+512 sum_(j<=m)epsilon_j).     (10)

To prove it, repair the outside block by resetting only memory to a fixed state
in E0, leaving H and the untouched reference intact. The inside block is
unchanged. The resulting supported CPTP map Psi preserves every H-observable
expectation of Phi on supported inputs, so its Q/T defect is epsilon_j exactly,
not epsilon_j+ell_j. Under (9), actual and repaired states differ by two
positive equal-trace blocks with orthogonal memory support. Their half trace
distance is exactly the leakage probability p<=ell_j.

Replace gaps1 through m-1 earliest to latest. Inputs to each replaced gap
have supported repaired prefixes; the remaining actual channels contract each
disturbance. Total full-state difference is at most sum_(j<m)ell_j. At the
last gap, reset all memory after Phi_m as a proof device. This cannot change
any subsequent recorded Q/T or target-bit/reference marginal, even if the
last output contains support/outside coherence. Its repaired map also has
compressed effect error epsilon_m. K2496 on all supported repaired maps now
adds512 sum epsilon, proving (10), with adaptive direct sums as before.

At zero effect error the coefficient1 on total leakage is sharp: a dephased
memory leak of probability ell from an A state, followed by an outside-controlled
A/B swap, changes the final Q record by exactly ell. Coherent repeated rotations
violate (9) and exclude extending (10) to arbitrary storage.

For a desired complete-record allowance Delta and N=m-1>=1, sufficient uniform
allocations are ell<=Delta/(2N) and epsilon<=Delta/(1024m).
The three-effect support calibration of K2500 applies to these numerical
bounds; (9) still requires an independently justified channel structure.
With d=108 dim(E0), G covered fixed map classes and confidence1-alpha,
zero systematic bias and observed certified residuals at most half the targets,
Nshots>=2(8d^2-7d)log(6Gd^2/alpha)/min(ell,epsilon)^2 suffices per setting.
There are3Gd^2 settings. This is inverse-square accuracy sampling at fixed
horizon, with improved leakage allocation under the extra structure; it is
not a sample lower bound, experiment or proof of (9). Positive acceptance
margin and independent restarts remain separate consumer assumptions.

## 5. General coherent errors also admit a linear horizon coefficient

The exact-effect argument extends to arbitrary coherent maps with

    ||S[Phi_jh*(R)-R]S||<=epsilon_j, R=Q,T,

and the same supported leakage bounds. No block dephasing is required.
For m>=1, a conservative explicit bound is

    E<=min(1,(3m+5)[sum_(j<m) ell_j+540600 sum_(j<=m) epsilon_j]). (12)

The last leakage is still absent. Take the minimum with K2500 and the exact
and block-dephased bounds when their hypotheses hold. The large error constant
makes (12) useful mainly in leakage-dominated regimes; it is not a calibrated
instrument or an optimal finite-error constant. For m=0, E=0.

### The finite algebra projection

Use the original matrix units e=P,A,B,N,Z,U,U*,Y of K2496, with weight c_e=1
on the four scalar sectors and1/2 on each plane matrix unit. On rectangular
maps X between any amplified representations define

    Pi(X)=sum_e c_e e_out X e_in*.

This is the projection onto algebra intertwiners. The matrix-unit identities
give Pi^2=Pi, the bimodule identity, and sum c_e e e*=sum c_e e*e=I.
Factoring the weighted row and column therefore proves ||Pi(X)||<=||X||,
including arbitrary memory and environment multiplicities.

If ||Q_out X-X Q_in||,||T_out X-X T_in||<=eta, word telescoping and the
explicit K2496 polynomials give the following defect constants:

    P:23/3, Z:50, Y:100, U,U*:25/2,
    A=Q-P-Z:176/3,
    B=T-P-rZ-(1-r)Y-sqrt(r(1-r))(U+U*):341/3,
    N=I-P-Z-Y-A-B:330.

Here1/5<=r<=1/4, r(1-r)>=4/25. Their weighted sum is1195/2<600.
Since X-Pi(X)=sum c_e(X e_in-e_out X)e_in*, we obtain

    ||X-Pi(X)||<=K eta, K=600.                         (13)

The same bound holds for commutators of square input operators.

### Supported polar approximation without exact effects

The projection-defect identity gives
||R_out VS-VS R_S||<=sqrt(epsilon). For j<m set

    W=Pi(S_out VS), D0=S_out VS-W, D=VS-W,
    M=ell+K^2 epsilon.

For the last gap use W=Pi(VS), D=VS-W and M=K^2 epsilon, with no output
support compression. Orthogonality of supported/outside outputs and (13)
give ||D||^2<=M. W intertwines, so also ||R_out D-D R_S||<=sqrt(epsilon).
Put A0=W*W, Z0=W*D. Contractivity gives0<=A0<=I, and

    I=A0+Z0+Z0*+D*D,
    Delta_R=[R_S,Z0]+D*(R_out D-D R_S),
    Pi_in(Z0)=0.

The last identity follows from the bimodule property and Pi(D0)=0; the
outside-supported piece is orthogonal to W. At the last gap Pi(D)=0 directly.
Thus (13) gives

    ||Z0||<=z=K(epsilon+sqrt(epsilon M)),
    ||I-A0||<=tau=M+2z.

When tau<1, B|S=W A0^(-1/2) is an algebra-intertwining isometry,
supported for j<m. Extend it globally with a fresh orthogonal environment tag.
Its overlap and outside row satisfy

    ||(B|S)*VS-I||<=a=1-sqrt(1-tau)+z/sqrt(1-tau),
    ||(B|S)*V(I-S)||<=sqrt(2a).                         (14)

The row bound follows from contraction and
I-HH*<=2||H-I||I for H=(B|S)*VS. Unlike the exact-effect case, the final
row may be nonzero and must be charged. The complete-record/reference
F/complement telescope of section2 therefore gives

    E<=min(1,2 sum_j a_j
       +2 sum_j sqrt(2a_j) min(1,sum_(i<j)sqrt(ell_i))). (15)

Equation (15) requires every tau_j<1; otherwise use a valid coarse bound.

For the globally valid coarse formula (12), Young's inequality gives
z<=ell/2+(K^2+K)epsilon, with ell replaced by0 for the last gap. Set
v=ell+540600 epsilon. Then tau<=2v. If every v<1/4, tau<1/2 and

    a<=tau+2z<=2tau<=4v.

The telescope is bounded by
[8+2sqrt(2)(m-1)]sum v<=(3m+5)sum v. If any v>=1/4, the right side
of (12) before capping is at least2, so the cap1 is valid without constructing
a polar inverse. This covers large errors, m=1 and all endpoint cases.

A concrete comparison avoids advertising the new constants universally. Write
Lsum=sum_(j<m)ell_j and Esum=sum_j epsilon_j. For m>=2 and Lsum>0,
the uncapped bound (12) beats K2500's1024 Esum+513m(m-1)Lsum/2 exactly when

    Esum/Lsum < [513m(m-1)/2-(3m+5)]/[540600(3m+5)-1024]. (16)

The full ordered K2500 certificate must also be compared, not just its coarse
formula. For m=100, ell_j=10^(-8) for j<100 and epsilon_j=10^(-16) for all
100 gaps, its q_j=(j-1)^2*10^(-8)<1 gives

    E_old<=512*10^(-14)+1024*10^(-12)*4950+10^(-8)*328350
          =0.00328856880512,
    E_new<=305*(99*10^(-8)+540600*10^(-14))=0.00030359883.

Thus the new bound genuinely improves the prior ordered certificate for this
explicit residual allocation. These are hypothetical certified allowances,
not measured residuals or a claim that calibration is economical. With
Lsum=0, K2500 is much tighter; always retain the minimum. The improvement
has a specific consumer and regime rather than a universal numerical advantage.

The result concerns the original recorded consumer. It does not imply a
full-state distance linear in leakage or an exact-transparent convex component
inside an arbitrary noisy channel. Trusted finite calibration can target the
strictly positive errors in (12); no exact-zero inference is needed.

## 6. Controls, calibration boundary and next question

Exact rational rotations test the actual channel, supported Q/T effects,
polar identity and complete deterministic record, with entangled-reference
fixtures. Changed inputs test coherent-versus-incoherent accumulation, global versus
supported transparency, finite zero-count inference and treating the complete
state as the recorded output. K2500's average-versus-uniform leakage counterexample
is inherited; it is not counted as a fresh check. The universal reference/adaptive theorem is the
written proof above, independently reviewed; finite fixtures are coverage.

Finite calibration cannot establish epsilon=0 exactly. With nonzero compressed
effect error, use the minimum of (12), K2500 and any applicable subclass bound.
The exact-effect theorem is an endpoint and structural diagnostic, not an
experimental certificate. Rare accepted branches still need K2500's positive
acceptance margin, and renewal costs need independent actual restarts.

Related primary work includes Gao, *Quantum union bounds for sequential
projective measurements*, PRA92,052331 (2015),
[arXiv:1410.5688](https://arxiv.org/abs/1410.5688). Sequential projection
probabilities motivate testing coherent accumulation, but (2) uses the stated
supported-intertwiner argument; arbitrary adaptive storage is not substituted
into that theorem without a bridge. No novelty comparison is claimed.

Next: instantiate trusted calibration/readout inputs for a concrete consumer,
or characterize the finite-error optimum when it changes that consumer. Conservative
constants must not be advertised as a practical improvement for every regime.
Trusted memory/readout implementation and native GU physics remain separate.


[Exact probe](../../tests/channel-swings/k2502_verifier_leakage_horizon_probe.py) and [saved report](../../lab/process/k2502-verifier-leakage-horizon.json).
