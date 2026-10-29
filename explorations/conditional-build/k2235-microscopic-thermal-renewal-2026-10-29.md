---
title: "K2235 Microscopic thermal collision renewal"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: finite thermal collision dilation with fresh supplied ancillas and external timing; no closed renewable reservoir, autonomous clock, local field apparatus or GU realization
scripts:
  - tests/channel-swings/k2235_microscopic_thermal_renewal_probe.py
---

# K2235 Microscopic thermal collision renewal

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
result: K2235 finite microscopic Gibbs renewal, exact sampled thermal channel and finite entropy-sink limit
carrier: positive record qubit, N bank qubits, finite fresh Gibbs ancilla train and arbitrary retained reference LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace form ON=declared_carrier
real_structure: ordinary complex adjoint
grading: binary occupation and additive energy
action_owner: repository-construction -- externally timed resonant exchange and supplied independent Gibbs ancillas
target: complete renewal channel, finite ancillary heat/entropy accounting and repeated reset errors MAP-TYPE=intertwiner
```

## Scope and actual increment

Prerequisites: owner instructions, geometer/physics routing T15/T16/T17,
source-native comparator routing, Layer 0, current state, research posture,
verification/contribution rules, standing ledger0.263 and path dependencies.
The object is the positive finite apparatus of K2229/K2232. No identification
with a GU action, physical quotient or native field coupling is supplied.
LT-SM8 remains NEEDS; no source claim, hypothesis vote or ledger grade changes.

K2232 supplies a thermal Markov generator and proves reference-uniform bank
renewal. Here a finite sequence of explicit positive two-qubit Hamiltonians
DERIVES its channel at selected times, prices every fresh ancilla, transfers
its heat into finite outgoing systems, and proves why finite cyclic entropy
sinks cannot support indefinitely repeated erasure. This is established
collision-model mathematics applied to the actual 1701-cell consumer, not a
novel general open-system mechanism. Background: Ciccarello et al.,
[Quantum collision models](https://doi.org/10.1016/j.physrep.2022.01.001).
The statements below have direct proofs and do not rely on a bath-limit claim.

## 1. Resonant exchange gives GAD; partial SWAP does not

Let B and A be qubits with the SAME nonnegative gap E, n=|1><1|,
H0=E(n_B+n_A), and fresh tau_A=diag(1-p,p),
p=(1+exp(beta E))^-1, beta>0. A is independent of BF and every unused
ancilla; B may be arbitrarily correlated with F. Define

    X=|01><10|+|10><01|,
    H(t)=H0+g(t)(I+X),  g(t)>=0,  theta=integral g(t)dt.

I+X has eigenvalues 0,1,1,2, so this TOTAL Hamiltonian is positive.
[H0,X]=0. Dropping only its scalar global phase, its exact propagator is

    exp(-i T H0) U_theta,
    U_theta|00>=|00>, U_theta|11>=|11>,
    U_theta|01>=c|01>-i s|10>,
    U_theta|10>=c|10>-i s|01>,    c=cos(theta), s=sin(theta).

For 0<=theta<=pi/2, tracing A gives the four Kraus operators

    sqrt(1-p) diag(1,c),  -i sqrt(1-p)s |0><1|,
    sqrt(p) diag(c,1),    -i sqrt(p)s |1><0|.

Their adjoint products sum to I. Thus, on arbitrary reference-valued blocks,

    [[A,C],[C*,B]] ->
    [[(1-p)(A+B)+c² D, c C],
     [c C*, p(A+B)-c² D]],  D=pA-(1-p)B,                     (1)

followed by the known free B rotation exp(-iETn). This is precisely K2232's
GAD with eta=c², INCLUDING its sqrt(eta) coherence coefficient. Derivation
by four Kraus operators proves complete-reference validity, not just correct
populations. The bath free rotation disappears under partial trace. The free
B phase is retained, matching the Hamiltonian term in K2232.

For contrast, the superficially similar partial SWAP V=cI-i s S has reduced
channel c²rho+s²tau-i cs[tau,rho]. Its population contraction is also c²,
but its coherence multiplier is c²-i cs(1-2p), not c. Its squared modulus
is c²[c²+s²(1-2p)²], strictly below c² when 0<p<1 and 0<c,s<1.
Even a correcting diagonal unitary cannot remove this extra contraction.
At p=1/2 the multiplier is c². Both full SWAP and full EXCHANGE are exact
replacement channels after tracing a fresh Gibbs ancilla, but their partial
versions are different channels. Do not reuse a partial-SWAP Hamiltonian
while quoting GAD's coherence rate.

## 2. Finite exact sampling, bounded rates and the limiting obstruction

For r fresh ancillas at the same gap, with angles theta_l, independent entry
and no return of spent ancillas, (1) composes exactly with

    a_r=p+eta(a_0-p),    z_r=e^(i E T_total) sqrt(eta) z_0,
    eta=product_l cos²(theta_l).                             (2)

Here z denotes the upper off-diagonal entry; its free phase has the displayed
positive sign. With a chosen step duration Delta and desired kappa>0, take

    theta=arccos(exp(-kappa Delta/2)),
    g(t)=theta f'(t/Delta)/Delta,

where f is K2232's normalized smooth increasing bump integral. Each of the r
sampled times agrees EXACTLY with exp(t L) in K2232. This is not exact
continuous-time semigroup evolution during a collision. In particular smooth
switch-on has theta(t)=o(t) and population derivative zero at the start,
whereas nonstationary semigroup input has nonzero initial population slope.

All chosen positive durations yield finite strength and slope:

    g_peak=theta C1/Delta,   |dot g|<=theta C2/Delta².

The constants C1=max f' and C2=max|f''| are finite. Timing remains externally
supplied. No clock Hamiltonian or battery is inferred from these bounds.

A fixed bounded strength g_max does NOT support the same finite kappa as
Delta tends to zero. Indeed theta<=g_max Delta. For theta<pi/2,

    -2 log cos(theta)=2 integral_0^theta tan u du
                    <=theta² sec²(theta).

Therefore exact matching implies

    kappa <= g_max² Delta sec²(g_max Delta)                  (3)

whenever g_max Delta<pi/2. The right side tends to zero. Conversely matching
at small Delta has theta/sqrt(Delta)->sqrt(kappa); hence g_peak scales as
C1 sqrt(kappa/Delta). This is a restriction on this resonant collision
family, not a universal no-go for continuous reservoirs or autonomous clocks.

## 3. Uniform renewal and same-bank cycles with finite ancillary stock

Applying K2232's block proof to (1) gives

    half-diamond(Phi_j-Tau_j)
      <= d_j=min(1,sqrt(eta_j)/2+max(p_j,1-p_j)eta_j).

Tensor telescoping across the N bank cells gives epsilon_B<=min(1,sum_j d_j).
All old correlations are included in F; unused ancillas must be independent
of this whole BF state. The channel therefore decouples the renewed bank
from the SAME reference marginal, including arbitrary retained detector
history. Knowing only the incoming ancilla marginals does not suffice. For an exact countercontrol at E=0, both marginals of (|01>+i|10>)/sqrt(2) are Gibbs with p=1/2. Exchange with c=3/5,s=4/5 changes the B excitation to (c-s)^2/2=1/50; an independently supplied GAD bath would preserve1/2.

Keep the same N bank cells for M resets, with K2229's final record error q.
Detector maps act on record/reference, never on the bank. The complete retained
output comparison is <=min(1,Mq+(M-1)epsilon_B); include the final renewed
bank by using min(1,M(q+epsilon_B)). These are K2232's hybrid arguments with
its reservoir hypothesis now supplied by the finite circuit, not a new
independence assumption on later detector priors. Additional energy-constrained
detector errors may be added only when their per-cycle energy hypotheses hold.

For the 1701-cell bank, choose r=100 and theta=pi/4 for every cell and step.
Then eta=2^-100 and the EXACT finite construction gives

    epsilon_B <=1701(2^-51+2^-100)<7.554e-13,
    1000(q+epsilon_B)<0.000019306566.

There are 170100 FRESH ancillas per renewal. With 1000 renewals, including the
last, there are 170100000 fresh ancillas plus the 1701 retained bank cells.
Omitting the last renewal consumes 169929900 fresh ancillas. A complete
stock can be prepared initially as a product Gibbs state on this finite
number of qubits, each with its matching bank gap. Reservoir Hilbert dimension
is 2 to the number of stocked qubits; no matrix of that size is needed.
Unused ancillas stay isolated, so intervening bank/reference operations cannot
correlate them before entry. No spent ancilla is silently reused.

At theta=pi/4, Delta=log(2)/kappa, giving total renewal time 100Delta when
1701 disjoint pairs are operated concurrently, or 170100Delta serially.
This supplies finite hardware/time, not a spatial transport or timing model.
Maximum ancilla gap is the inherited E_m<17.762861/beta. All energy-capacity
bounds are finite; e.g. sum E_A<=170100000 E_m with final renewal included.
The actual Gibbs energy is sum p_j E_j for each copy, not this upper bound.

A stronger finite-resource alternative deliberately abandons finite-rate
semigroup interpolation: one full exchange theta=pi/2 per cell gives c=0,
EXACT reference-uniform product-Gibbs replacement with N fresh ancillas.
The retained free B rotation leaves the diagonal output tau_B invariant, so
this statement does not discard a physically relevant phase.
This does not contradict K2232's no-finite-time exact renewal at fixed finite
Markov rate. For M=1000 resets it uses 1699299 fresh ancillas without a final
renewal; adding the initial 1701 bank cells gives 1701000, exactly K2229's
original fresh-bank stock count. Reusing the named bank relocates, and under
weak collisions increases, the consumed fresh-state resource.

## 4. Finite heat, switching work and entropy export

Because X commutes with the whole collision Hamiltonian, <I+X> is conserved
even for arbitrary correlated BA entry. Smooth coupling begins/ends at zero,
so its net switched mean work is exactly

    integral dot g(t)<I+X>dt =0.

For a single-crest pulse the absolute mean exchange is 2g_peak<I+X>, bounded
by 4g_peak for arbitrary entry. With the declared fresh diagonal ancilla,
<X>=0 EVEN WHEN B is correlated with F; hence it is exactly 2g_peak. This
is a supplied-control energy account. It does not price producing the controls,
transporting cells, or constructing a clock.

The pulse preserves H0 exactly. At input population a, the fresh ancilla's
outgoing population is p+(1-c²)(a-p). Thus its mean energy increase is
E(1-c²)(a-p), with either sign allowed. A train yields

    Q_A=E(1-eta)(a-p),
    Q_all=sum_j E_j(1-eta_j)(a_j-p_j),                        (4)

by telescoping. This derives K2232's reservoir heat as actual finite ancillary
energy, with zero renewal net work. Reset work still comes from the original
record gap changes. General cycle balance remains

    W_k=Q_A,k+E_B,after-renewal,k-E_B,before-reset,k.

The same prior warning is essential: actual bank populations b_j give
beta W=w x0+sum b_(j-1)(x_j-x_(j-1))-b_m x_m. The first-cycle narrow w
interval cannot be recycled for arbitrary later detectors. Renewal changes
this expression by at most (2x_m-x0)epsilon_B relative to the actual w.

There is also an EXACT finite-environment refinement of K2232's entropy
balance. Let A denote the entire fresh train in tau_A, and let chi_BFA be
the final joint state. Unitary evolution of rho_BF tensor tau_A gives

    Delta S(B|F)+beta Q_A
      = D(chi_A || tau_A)+I(A:BF)_chi >=0.                   (5)

Proof: S(BFA)_out=S(BF)_in+S(A)_in and F is unchanged, so
Delta S(B|F)+Delta S(A)=I(A:BF)_out. Also
D(chi_A||tau_A)=beta Q_A-Delta S(A). Add these identities.
For an arbitrary infinite-dimensional F, the same identity follows by
conditional entropy defined with the finite BA carriers; all finite-system
entropies and the mutual information with finite A are bounded. Formula (5)
accounts for correlations AMONG ancillas via the joint chi_A and for their
correlations with the retained apparatus. Summing independent binary entropies
would omit those terms. The consumed resource is the fresh product Gibbs
stock: outgoing ancillas store energy, correlations and entropy and are not
certified reusable. No reservoir renewal beyond that finite stock is derived.

## 5. Finite cyclic entropy sinks cannot erase indefinitely

Here is a separate closed-apparatus theorem, not a claim about the open circuit.
Take M independent maximally mixed input record qubits and an initially
independent finite apparatus E of dimension d_E in sigma_E. Include every
clock, battery, bank, sink and retained copy in E. Permit ANY global unitary,
including arbitrary externally prescribed unitary controls. Suppose every
output record is within half trace distance q<=1/2 of |0><0|. Then

    M[log(2)-h(q)] <= S(E_out)-S(sigma_E)
                   <= log(d_E)-S(sigma_E).                  (6)

Proof: each output record has excitation <=q and entropy <=h(q), by
pinching/dephasing and monotonicity of binary entropy on [0,1/2]. Global
entropy conservation and subadditivity give
M log2+S(sigma_E)<=sum S(R_k,out)+S(E_out), which proves (6).
Final correlations do not evade it. An exactly cyclic E marginal is
impossible for any M>0 and q<1/2, even if final correlations are allowed.
A fresh reservoir, accumulating classical memory or changing battery entropy
must be counted in E or explicitly declared an external sink.

If d_E>=2 and E returns within half trace distance epsilon<=1-1/d_E of
sigma_E, the [Audenaert finite-dimensional entropy continuity bound](https://arxiv.org/abs/quant-ph/0610146) gives the stronger necessary bound

    M[log2-h(q)] <= epsilon log(d_E-1)+h(epsilon).            (7)

Thus a tiny nominal marginal-return error alone does not establish an
indefinitely reusable apparatus: dimension enters its entropy capacity.
These inequalities concern unconstrained maximally mixed independent records.
They do not forbid resetting a known pure record, consuming side-information
resources, or exporting records to an excluded sink. The constructed open
ancilla circuit obeys them; it consumes an explicitly growing E.

## 6. Robustness and weakest seams

A fresh independently supplied ancilla rho_A within half trace distance delta
of tau_A changes its collision channel by at most delta in half diamond norm:
append rho_A-tau_A, apply the same unitary and trace. A pulse-angle error
|delta theta| changes it by at most |delta theta|, from unitary Duhamel and
||X||=1. The scalar shift is a global phase and is removed in this comparison.
More generally an actual bounded Hamiltonian perturbation V(t), modulo scalar
identity, contributes at most integral ||V(t)||dt. For L contacts, telescope
these bounds; add their sum to the ideal renewal/repeated-output ceiling.
This prices specified imperfections, not a claim that such preparation or
calibration accuracy is physically available. Correlated incoming stock is
not covered by one-cell marginal delta values.

Strongest overclaim rejected: a finite microscopic circuit closes reservoir,
clock or apparatus renewal. It does not; (5)-(7) identify the missing resource.
Strongest countercontrols: partial SWAP has the wrong coherence; unequal gaps
break energy conservation; a Gibbs-correlated incoming ancilla need not yield
a GAD channel; reusing a spent ancilla is not the fresh-channel composition;
full exchange changes finite-rate interpolation; bounded-strength rapid
collisions cannot maintain fixed kappa. No GU physical map is promoted.

The accompanying exact Gaussian-rational probe tests unitary/Kraus blocks,
reference extension, fresh-versus-reused composition, energy transfer,
positivity spectrum, partial-SWAP coherence, and exact 1701-cell arithmetic.
Genuine input mutations must fail unchanged controls. Universal channel,
entropy, continuity and limiting proofs remain written mathematics, not
finite enumeration, proof-assistant or external-expert certification.


## Reproduction and independent-review handoff

The scientific preflight compared repeating the supplied GAD channel, deriving
a collision dilation, and pursuing a general autonomous clock. The collision
dilation was selected because it changes an actual supplied reservoir premise
and has an explicit finite-resource consumer. The hostile postflight then
challenged the partial-SWAP substitution, continuous-time rate claim, omitted
ancilla stock, correlations and cyclic entropy sink; Sections1--6 state the
resulting corrections and limits. Independent specialist review checked the concrete derivation and wording,
and strengthened the correlated-input countercontrol to an explicit state
with Gibbs marginals. No blocking mathematical finding remained. Internal
review is not external expert or proof-assistant certification.

The source metadata is deliberately narrow: the current standing-ledger pointer
was read and LT-SM8 was checked; no new source claim was adjudicated and no
source-video/transcript reinspection is claimed. K2229 and K2232 are reused
mathematical dependencies. Primary collision-model and entropy-continuity
references support background conventions, not a novelty or physical claim.

Run `python tests/channel-swings/k2235_microscopic_thermal_renewal_probe.py`
for the exact finite controls. Its certificate binds this note, the probe and
the two reused mathematical dependencies by SHA256; default execution must
reject stale certificates and `--write` may refresh them after native review.
Faults change the exchange unitary, relative phase, Gibbs input, resonance,
positive scalar shift, input correlations, spent-ancilla reuse, heat sign or
fresh collision count. None changes an acceptance flag. Matrix-unit controls
exercise every operator of the stated finite reference size; the arbitrary-
reference theorem is the Kraus/block proof, not extrapolation from those tests.
