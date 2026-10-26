---
title: "K2089: Smooth distributed mode transfer and the readout boundary"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source-state selection, GU verdict or external certification
scripts:
  - tests/channel-swings/k2089_distributed_smooth_transfer.py
  - tests/channel-swings/k2089_distributed_smooth_transfer_probe.py
---

# K2089: Smooth distributed mode transfer and the readout boundary

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: finite-duration distributed transfer with finite final sea energy and explicit instrument debt
carrier: supplied massive complex Dirac1408 CAR on R3 LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: fixed positive Hilbert metric and gauge-invariant quasifree input ON=declared_complex_completion
real_structure: inherited b antiunitary with b squared minus identity and b H b inverse equals minus H
grading: fermion parity, charge and energy signs are separate
action_owner: repository-construction -- imported free massive dynamics and stated operational additions
target: operational state and measurement constraints MAP-TYPE=intertwiner
```

[Conditional mathematical result; accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Scope and inherited evidence

SC-OP-04 ASSERTS candidate four-independent-field operator grammar; SC-OP-05 and
SC-META-53 remain UNCERTAIN; SC-META-56 DISAVOWS an odd-action prerequisite.
These calculations use the supplied positive massive CAR completion, not the source
operator (9.16). LT-SM8/GR6b, source-register, physics-ledger and canon verdicts remain
unchanged. K2021 already supplies local R0/R1; source selection and interacting
observation/action/quotient are still separate. No novelty or external certification
is claimed. The operational demands are reverse-scaffold constraints, not predictions.

## 1. Construct a different continuum primitive

[K2084](k2084-continuum-instrument-limit-2026-10-26.md) rules out a strong limit
of a shrinking-root funnel, while allowing a fixed-radius/distributed repair.
Here construct a distributed mode-transfer primitive using a supplied second
identical Dirac field. This is a genuine continuum evolution, not another finite
mesh endpoint. It does not by itself measure a mode or construct a localized record.

Let the doubled one-particle space be H0 tensor C2_species and free generator
h=H tensor I. Choose a compact initial support K and T>0. Supply Hermitian
V(t,x)=g(t)theta(x) sigma_y, g smooth with compact support inside(0,T), theta
smooth compact, theta=1 on K enlarged by the free propagation radius vT and
a positive margin. The original local Hamiltonian h+V has common domain H1,
unitary evolution U and finite speed v, since the bounded Hermitian zero-order
potential cancels in the density balance. Define endpoint scattering

    S=exp(iTh)U(T,0), A=integral_0^T g(t)dt.

For every spinor f supported in K, uniqueness and finite propagation give

    S(f tensor z)=f tensor exp(-i A sigma_y)z.         (1)

Indeed exp(-i integral_0^t g sigma_y)exp(-itH)f solves the coupled equation
while its support stays in the plateau. At A=pi/2 the species matrix is [[0,-1],[1,0]], an exact signed swap.
Each sign disappears on its individual even algebra. It applies simultaneously to all selected compact modes and
preserves their relative coherence, including K2082's f,bf pair. Physical output
modes are exp(-iTH)f at time T; S is an interaction-picture statement, not an
instantaneous intervention or zero-time transport. Spatial support has not
been concentrated into a shrinking region.

## 2. Finite post-pulse energy in a declared representation

Put the supplied sea Q in BOTH species. A constant unitary species basis
change diagonalizes sigma_y into+1,-1, reducing U to two scalar pulses
+g theta and-g theta. Reuse [K1897](k1897-smooth-pulse-energy-2026-10-21.md),
which builds on [Langmann and Mickelsson](https://arxiv.org/abs/hep-th/9509034):
for a smooth compact spacetime scalar potential, every finite weighted
energy off-block Hilbert-Schmidt moment at the pulse endpoint is finite.
The present H is a finite direct sum of massive rank-four blocks after its
fixed isometry; changing a positive constant propagation speed does not alter
ellipticity, the mass gap, smoothness, localization or symbol-order inequalities.
The two scalar signs and finite multiplicity preserve that result. Explicitly,

    J_r(S)=sum_(sign=+,-) [|| |H|^(r/2) P S_sign Q ||_HS^2
                         +|| |H|^(r/2) Q S_sign P ||_HS^2]<infinity. (2)

These are particle/hole one-particle moments, including final mean excitation
energy r=1. K1897's weighted bound, spatial decay and vanishing endpoint jets
are indispensable; ordinary operator boundedness alone would not prove(2).
The finite-energy endpoint is implemented in the doubled sea representation.
No numerical resource budget, uniform T->0 bound, intermediate-time energy or
total apparatus work is asserted. The mass, field copy and coupling are supplied.
The inherited doubled antiunitary B=b direct-sum b has B V B^-1=-V,
because sigma_y is imaginary; hence B(h+V)B^-1=-(h+V) and the actual
propagator commutes with B. In real coefficients iV is real skew and commutes
with the doubled kinetic structure. This preserves K2058's fixed metric rather
than fitting a new one. A real sigma_x potential would fail this sign test.
An empty apparatus covariance0 would be a different representation/input and
cannot inherit this doubled-sea energy result. The inherited particle-hole CAR symmetry is therefore respected by this
particular pulse; no source selection of it follows.

## 3. Exact finite-mode transfer, with honest apparatus noise

Equation(1) swaps the finite CAR subalgebras of any finite orthonormal set
supported in K. Consequently every even apparatus observable in that subalgebra
after the pulse has the corresponding system expectation before the pulse,
regardless of the apparatus marginal. Correlations with the environment do not
change this algebraic statement. A superposition is transferred coherently;
measuring positions first would not do this. The signed swap acts identically on each even subalgebra, including anomalous
two-creation coherence; a sigma_x swap would instead introduce a quarter-turn
gauge rotation. Even states need not be gauge-invariant: vacuum plus two-particle
coherence detects that difference.

The old apparatus state replaces the system's selected marginal. In the supplied
sea its detector restriction is generally noisy: K2082 gives nu and the paired
click background2nu-nu^2. A swap is therefore destructive state transfer, not a
nondemolition measurement or a fresh pure pointer preparation. Initial thermal
product states also enjoy the algebraic transfer, but(2) is specifically a
sea-excitation statement and is not their infinite-total-energy accounting.

## 4. The exact readout obligation, not an apparatus claim

If one additionally supplies ideal measurement of the collective apparatus
projection E_a and an exact inverse of the transfer, then algebraically

    U_transfer* E_a U_transfer=E_s,
    U_transfer* (1-E_a) U_transfer=1-E_s,             (3)

with the appropriate evolved mode labels or interaction-picture S. Thus a
swap-measure-unswap construction has exactly the desired coarse system Kraus
operators, tensored with identity on the apparatus. This is an IF statement.
The local implementation of E_a and of the physical inverse has not been
constructed. Negating g while retaining the forward drift H does not in general
reverse the complete evolution. No reverse-time control is silently granted.

A useful partial return can nevertheless be constructed. Apply a second opposite-area
smooth pulse with its plateau enlarged to contain all freely evolved selected-mode
supports through the two-pulse duration. The same finite-propagation argument makes
its interaction-picture rotation the inverse on the SELECTED subspace.
Use a common time origin: S_r=exp(i(T+T_r)h)U_r(T+T_r,T)exp(-iTh),
not a locally restarted scattering operator. Both scalar
pulse families still meet the finite-energy endpoint theorem. Their product S_r S_f
is identity on that selected one-particle subspace, but need not be identity on its
orthogonal complement. With the ideal intermediate readout, the full branches are
W_residual E_s,j. W_residual commutes with the selected CAR algebra. Thus the selected
subalgebra has exactly its Lueders instrument while remote/complement observables may
experience residual dynamics. This is an actual selected-mode return control, not a
proof of the whole-system inverse or of the unsupplied collective readout. The physical
output includes the known free evolution throughout; no time reversal is required for
this restricted statement.

A distributed array of local occupation measurements plus the classical particle/hole OR is not
that coarse Lueders instrument. For the actual paired particle/hole effect E=1-(1-n_f)n_bf,
the same-parity states |00>,|11> both lie in the click subspace. A coherent superposition between them survives
coarse projection but is dephased by the individual readouts, even after their
classical labels are discarded. This explicit countercontrol rules out the
simple proposed replacement. It does not exclude every distributed quantum
readout. K2081's causal record bound still applies when one compact record
must collect the result; a parallel transfer alone cannot evade it.

## 5. Consequence and verification

The shrinking-root obstruction is avoided by an actual local, finite-duration,
fixed-spatial-profile evolution with finite final doubled-sea excitation energy.
What remains is a coherent collective readout (or a rigorously approximate one),
its causal collection and inverse-control requirements, and its resource budget.
The finite probe checks species diagonalization, exact coherent transfer at pi/2,
partial-swap apparatus contamination, and coarse/refined instrument difference.
It cannot certify the PDE or weighted symbol theorem; sections1--2 provide those
arguments with explicit reused hypotheses. Compare this remaining readout problem
against source-selected state/observation and the new thermal163/164 certificate;
do not report a completed continuum measurement apparatus.
