---
title: "K2223 Semibounded controlled detector and exact reset resources"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied nonlocal externally switched stable control and resource accounting; no autonomous apparatus or GU realization
scripts:
  - tests/channel-swings/k2223_stable_detector_resource_realization_probe.py
---

# K2223 Semibounded controlled detector and exact reset resources

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
result: K2223 semibounded pulse realization and record reset resource
carrier: supplied positive scalar Fock space with one record qubit and a separate reset reservoir LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and trace ON=declared_carrier
real_structure: ordinary complex adjoint and real canonical Q,P
grading: occupation number and binary record; no spinor grading
action_owner: repository-construction -- explicitly switched total Hamiltonians
target: same complete detector instrument and its work/purity resource account MAP-TYPE=intertwiner
```

## Result and explicit control assumption

The unique half-contrast instrument in [K2219](k2219-detector-global-capture-2026-10-28.md)
has an exact realization by a sequence of nonnegative self-adjoint TOTAL
Hamiltonians on the same field and one initially pure, degenerate record qubit.
The construction retains all occupations, both reported outcomes and arbitrary
reference systems. It does not truncate the optimized effect.

The essential supplied control is the ability to SWITCH THE TOTAL HAMILTONIAN
from physical free H=dGamma(omega) to the displayed nonlocal controls and back.
Other free drift is turned off during these pulses. This assumption is stronger
than adding a bounded local coupling to a fixed physical H. It supplies external
timing and arbitrary spectral control theta(n_b); it is neither an autonomous
clock nor an implementation by available local matter. Semiboundedness means
each active total generator has a lower bound, not that external control has
been derived or thermodynamic resources are free. The additive compensation
relative to the original free H is itself unbounded below; only the TOTAL
Hamiltonian on each plateau is asserted semibounded.

This closes the mathematical semibounded-control and mean switching-work
questions under that assumption. Exact repeated operation additionally consumes
a pure reset bit. A finite faithful thermal reservoir cannot exactly reset the
record by any unitary; its optimal residual error is computed below. No source
or physical GU claim changes. SC-META-53 remains UNCERTAIN. The older finite-chain
[K2154](k2154-uncompensated-detector-control-2026-10-27.md) retains physical drift
and approximates threshold and soft diagonal instruments without this
outcome-conditioned squeezing, so its result is not
silently replaced by this stronger control model.

## 1. Exact coherent measurement

Use the fixed b mode and real canonical Q,P of
[K2160](k2160-outcome-conditioned-squeezing-2026-10-27.md), [Q,P]=i,
n_b=(Q^2+P^2-1)/2. Write e_n for the click effect, 0<=e_n<=1,
and theta(n)=arcsin(sqrt(e_n)). On field tensor record define

    H_m=theta(n_b) tensor sigma_y + (pi/2) I,   duration 1.

Functional calculus gives 0<=H_m<=pi I. Starting the record in |0>,
exp(-i H_m) maps psi tensor |0>, up to a common phase, to

    sqrt(1-e(n_b)) psi tensor |0> + sqrt(e(n_b)) psi tensor |1>.

This is an exact isometry on the full Fock space, not a finite number-state
approximation. The measurement pulse commutes with n_b and with the complement
mode number n_c. Consequently all moments needed by K2160 remain finite on the
vacuum and the complete field-reference channel is the desired positive-root
instrument once the record is read.

## 2. Squeezing with positive oscillator pulses

For s>0 let h_s=(P^2+s^2 Q^2)/2. Conditionally on coherent record r, use
h_(s_r)/s_r for time pi/2, followed by h_1 for time 3pi/2. Both operators
are positive self-adjoint oscillator Hamiltonians; finite record direct sums
remain so. The Heisenberg quarter-period matrix is

    R_s=[[0,1/s],[-s,0]],
    R_1^3 R_s=diag(s,1/s).

Thus the resulting controlled unitary has U_r^* Q U_r=s_r Q and
U_r^* P U_r=P/s_r, exactly K2160's outcome squeeze. Metaplectic phases may
differ between outcomes and have no effect after record dephasing. The pulse
sequence followed by record readout realizes both Kraus maps U_r sqrt(e_r(n_b))
for all input states and entangled references. It is the same full recorded
instrument whose vacuum field energy K2219 optimizes.

## 3. Domains, stability and switching work

For this vacuum let G=n_b+1/2, <G>_0=N+1/2=5/6 and
K=max_r(s_r,1/s_r)>=1. Measurement preserves the summed <G>. During the first
oscillator pulse the phase-space matrix is

    R_s(t)=[[cos t,sin t/s],[-s sin t,cos t]].

Its operator norm is at most max(s,1/s): write it as an orthogonal rotation
conjugated by diag(1/sqrt(s),sqrt(s)). Therefore as quadratic forms
G_t<=K^2 G before the final unit-frequency rotation, which preserves G.
The complement number is unchanged. The initial two-mode Schmidt state has
finite moments; bounded diagonal measurement preserves their summed occupation-number moments,
and finite squeezing preserves finite quadratic moments. The physical endpoint
H expectation is finite by K2160's finite-moment form-domain argument; no
invariance of span(h,j) under omega is assumed. These statements establish
finite mean energy for the input used in the optimization, not every arbitrary
finite-energy field input without additional mode/domain assumptions.

Each pulse has a self-adjoint unitary evolution on the same Hilbert space,
with its own natural domain. Instantaneous Hamiltonian switches use the state
continuously; we assert common form-finite vacuum evolution, not equality of
all operator domains. Infinite degeneracy of spectator modes during the
switched controls is allowed. No negative unbounded squeeze generator is used.

Define mean switching work at each sudden switch as the expectation of
H_after-H_before in the unchanged state. Within a time-independent pulse its
mean active energy is conserved. Hence the signed sum telescopes:

    W_switch=<H>_out-<H>_in=E_star.

The physical vacuum has zero input energy. Record readout here includes explicitly supplied pinching of the record in its
computational basis. It does not change field mean energy since H acts
trivially on the record. No thermodynamic cost of that readout is asserted. Thus K2219's bracket
for E_star is also the NET mean switching work of THIS supplied protocol.
It is not a universal work lower bound for arbitrary controllers or inputs.

Using 0<=H_m<=pi, h_s/s<=K G and the bound on G above gives the explicit
conservative bound on absolute mean switching works

    sum_switches |<H_after-H_before>|
       <=2pi+2K G0+2K^2 G0+E_star,   G0=5/6.

A more precise formula uses K2160's unnormalized R_r=M_r+w_r/2. The
pre-squeeze number-diagonal branch has <Q^2>=<P^2>=R_r. Put

    B=sum_r R_r(s_r+s_r^-1)/2,
    C=sum_r R_r(s_r^2+s_r^-2)/2.

The four mean switch works are exactly

    pi/2, B-pi/2, C-B, E_star-C,

so their absolute sum is pi/2+|B-pi/2|+|C-B|+|E_star-C|.
The first equality uses <sigma_y>=0 initially and conservation of H_m.
These identities apply to the fixed vacuum input and supplied pulse schedule.
This separates
net work from potentially larger positive and negative exchanges.

The probe now evaluates these quantities for the TRUE K2219 optimizer using
its certified seven-coordinate boxes, squeeze intervals and a complete
geometric tail bounded by3/20<=e_n<=1. It obtains

    0.3045489 < w < 0.3046040,
    0.8383135 < B < 0.8384061,
    0.8534883 < C < 0.8535830,
    2.34055 < sum |mean switch work| < 2.34093.

All four switch signs are certified (+,-,+,-). The net work is the inherited
E_star approximately0.83120400517. Exact rational outward endpoints are in
[the certificate](../../lab/process/k2223-stable-detector-resource-realization.json).
Pi is bounded by the Machin arctangent identity with alternating rational
series. No fitted profile is substituted for the true minimizer and no
occupation tail is discarded. The wider absolute-work interval is adequate
to distinguish the supplied control's total exchanges from its net cost. Preparation of the physical vacuum and pure record, timing,
readout and reservoir renewal remain named external resources.

## 4. Exact reset and sharp finite-reservoir error

After readout the record marginal is rho_R=diag(1-w,w), with 0<w<1 for
the interior K2219 optimizer. It can remain correlated with the field. A fresh
pure degenerate qubit |0>_B permits an exact SWAP: the record resets to |0>,
while B receives its old state AND its correlations with the field. With
zero endpoint Hamiltonians this reset has zero net mean energy change, but
it consumes the purity of one bit; it is not a cyclic thermal reservoir.
Any additional observer copy produced by readout remains outside this reset.
Before pinching the coherent record need not have a diagonal marginal, so the
following diagonal-record formula is not applied to that earlier state.
A positive bounded SWAP generator exists, pi times the antisymmetric projector
for unit duration. Its input and output mean generator energy agree, so its
two switching works cancel, with finite absolute-work bound 2pi.

For contrast, take a finite d-dimensional faithful thermal state tau_B,
initially independent of record and field, and allow ANY unitary on R tensor B,
including arbitrary work input. The local input rho_R tensor tau_B is full
rank2d. Exact pure record output would have rank at most d, impossible under
a unitary. The sharper optimal error probability q of finding the unwanted
record value is

    q_min=sum of the d smallest eigenvalues of rho_R tensor tau_B
         >=d min(w,1-w) lambda_min(tau_B)>0.

Proof: the unwanted-record projector has rank d. Minimizing its expectation
over unitary conjugates is the elementary eigenvalue variational principle;
a permutation of an eigenbasis attains the bound. This includes a sharp
construction, not only the full-rank obstruction. The quantity is reset error
for a fixed marginal, not a universal reset channel norm. It also equals the optimal half trace
distance to |0><0| for this fixed marginal: the unwanted-population measurement
is a lower bound and the diagonal permutation attainer saturates it. Correlations with the
field do not change this marginal argument for local R,B operations.

Example: w=1/3 and bath eigenvalues3/4,1/4 give joint eigenvalues
1/2,1/6,1/4,1/12 and q_min=1/4. Increasing control energy cannot remove this
fixed finite-bath error. In fact the certified TRUE optimizer probability
also lies between1/4 and3/4. Throughout that interval the two smallest joint
eigenvalues for this bath are w/4 and(1-w)/4, so q_min=1/4 for the actual
optimal detector as well. This is a fixed two-level-bath statement, not a
universal error floor across reservoirs. A pure-bit bath has zeros in its spectrum and permits
q_min=0, consistent with SWAP. This resource distinction is related to
[K1916](k1916-bath-preparation-resource-limits-2026-10-21.md)'s support-preparation
account, not a new generic thermodynamic law. No finite-temperature exact
Landauer-cost protocol or repeatable finite bath is claimed.

## Verification and useful continuation

The probe checks the coherent record rotation, exact symbolic symplectic pulse
product, positivity coefficient bounds, finite-work telescoping, explicit SWAP
and the sharp reset spectrum against every finite permutation in a rational
fixture. Baseline-first mutations change rotation normalization, pulse order,
Hamiltonian shift, reset eigenvalue products or the actual geometric tail. These finite controls support
the functional-calculus, domain and variational proofs above; they are not a
proof assistant or external expert review.

Useful next work must relax an EXPLICIT supplied resource: retain physical
free drift with semibounded local controls; price a clock and achievable
spectral coupling; or choose a reservoir renewal/approximate-reset model.
Neither another half-contrast optimum nor another abstract dilation settles
those requirements. Uniform contrast continuation can reuse these pulses
for its finite positive squeezes, but does not make timing or purity free.
Source/full16cells/full20/K-C, native2+1/chirality, physical quotient and the
prior scalar/thermal/cosmology claim ceilings remain unchanged.
