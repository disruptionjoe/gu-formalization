---
title: "K1922: A uniform obstruction for energy-conserving thermal channels"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied conditional models only; no native GU, novelty, total work or formal proof
scripts:
  - tests/channel-swings/k1922_energy_conserving_thermal_channel_floor.py
  - tests/channel-swings/k1922_energy_conserving_thermal_channel_floor_probe.py
---

# K1922: A uniform obstruction for energy-conserving thermal channels

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
result: bath-dimension and temperature independent full-channel approximation floor
carrier: four-level system and finite Gibbs bath with product initial state LAYER=toy CHIRALITY=N/A
pairing: positive trace, normalized Choi state and diamond distance ON=finite_tensor_product
real_structure: complex adjoint and positive spectral Gibbs weights
grading: system energy eigenbasis and bath energy shells only
action_owner: repository-construction -- strict conservation of additive system plus bath Hamiltonian
target: approximation of a supplied nonfactorizable Schur channel MAP-TYPE=intertwiner
```

## 1. A restriction that changes the collective conclusion

[K1920](k1920-local-block-thermal-channel-construction-2026-10-22.md) permits
arbitrary driven gates. Impose instead EXACT endpoint conservation
[U,H_S tensor I+I tensor H_B]=0, with H_S diagonal in the target's four
population labels, any finite bath and initial product state X tensor tau,
tau=exp(-beta H_B)/Z. Degeneracies in either Hamiltonian are allowed. No
catalyst, work battery, measurement or external nonthermal ancilla is supplied.
The channel may mix system populations arbitrarily.

Use [K1913](k1913-leakage-robust-bath-bound-2026-10-21.md)'s target C,
B=[-1 -1 sqrt2 0; -1 i 0 sqrt2], H=B*B, delta=6-4sqrt2 and
h0=||H||=4+sqrt2. If t is normalized Choi trace distance and pbar is mean
basis-population leakage, then

    sqrt(t)+sqrt(pbar)>=sqrt(delta/(4h0)).             (1)

Consequently the half-diamond distance epsilon satisfies

    epsilon>=c0=delta/(16h0)>0.0039.                  (2)

The constant is independent of bath dimension, beta, bandwidth and the
number of same-temperature bath cells. This is a valid lower bound, not the
sharp thermal-operation distance. It is stronger than K1913's bound for
this restricted class because there is NO d*lambda_min factor. Taking a
larger or colder Gibbs bath cannot approximate C arbitrarily well while
keeping strict additive-energy conservation.

## 2. Energy shells replace the minimum-eigenvalue estimate

Write A_j=U_jj. The diagonal block of [U,H_S+H_B]=0 is
[A_j,H_B]=0, irrespective of population leakage or H_S degeneracies.
Choose the polar unitary V_j extending A_j=V_j|A_j| separately within each
finite-dimensional bath energy eigenspace. Such an extension exists because
a square block has equal kernel and cokernel dimensions. Thus V_j commutes
with H_B, and K1913's exact contraction estimate still gives

    ||(A_j-V_j)sqrt(tau)||_F^2<=ell_j.                 (3)

On energy shell e of dimension d_e, tau is a scalar and all V_j restrict
to unitaries. K1912's normalized-trace inequality therefore gives

    (1/d_e)Tr_e(sum_l |sum_j B_lj V_j|^2)>=delta.

Multiply by the shell probability q_e=d_e exp(-beta e)/Z and sum. Since
sum q_e=1, the weighted residual is at least delta, with no lower spectral
estimate. The triangle inequality yields

    sqrt(W_A)+sqrt(h0 sum_j ell_j)>=sqrt(delta).

K1913's positive normalized Choi effect QHQ*/h0 gives W_A<=4h0 t.
This proves(1), and t,pbar<=epsilon proves(2). The full off-diagonal system
blocks have not been dropped: their observable leakage appears in(3).
This is why exact population conservation need not be assumed.

The same proof holds for ANY bath state scalar on each H_B eigenspace,
with arbitrary nonnegative shell weights summing to one. It includes the
zero-temperature uniform ground-space limit. A pure ground state in a
DEGENERATE ground space is not that limit unless the ground space is one
dimensional. Arbitrary nonthermal states within a degenerate shell can
supply the missing resource, so [rho,H_B]=0 alone is insufficient.

## 3. Released finite-cell, multi-copy and preparation consequences

A finite sequence of strictly energy-conserving interactions with independent
Gibbs cells at the SAME beta composes into one conserving unitary on the
product bath. Its state is Gibbs for the summed bath Hamiltonian. Bound(2)
survives arbitrary cell count and intermediate population mixing. Different
temperatures generally fail the scalar-total-shell condition and are not
covered by this argument. Equal mean work is not exact conservation.

For N target systems with additive Hamiltonian, a global thermal operation
approximating Phi_C^(tensor N) also has half-diamond error at least c0.
Initialize N-1 systems in their Gibbs states, run the channel and trace them
out. They can be absorbed into the same-temperature bath, and the target
reduction is Phi_C on the remaining system. Channel pre/postprocessing
contracts diamond distance, so(2) applies. This does not establish an
increasing-in-N floor or exclude nonthermal catalysts.

For an initial bath state rho within trace distance r of an admissible
shell-scalar tau, fixing the same conserving U gives channel half-diamond
distance at most r between the two bath preparations: tensoring any purified
input, applying U and partial trace are trace-norm contractions. Therefore

    epsilon(rho)+r>=c0.                              (4)

If the implementation is also within half-diamond eta of that conserving
implementation, epsilon+r+eta>=c0. The eta is an actual channel-distance
hypothesis; a small energy expectation change or commutator is not silently
substituted for it. These are quantitative nonthermal/control requirements,
not total-work lower bounds or a cooling protocol.

## 4. Controls that distinguish the exact hypotheses

A resonant population-mixing test uses H_S=diag(0,1,2,3),
H_B=diag(0,1), tau=diag(3/4,1/4), and a real rotation with cos=3/5,
sin=4/5 on span{|0,1>,|1,0>}, identity elsewhere. It commutes with total
energy but leaks populations: ell_0=4/25, ell_1=12/25 and pbar=4/25.
Direct Kraus/Choi construction verifies W_A/4=Tr[(QHQ*)J], normalized
trace, positivity, shell block commutation and the witness/leakage bound.
It is not a controlled-unitary surrogate.

A second exact test uses a twofold degenerate bath shell with noncommuting
unitaries I,X,Z and a rational rotation inside the shell. The state is
scalar there, so the tracial estimate applies even though the unitaries do
not jointly diagonalize. A simple-spectrum bath instead gives scalar phase
mixtures; that special fact is not asserted for every degenerate bath.

A genuine escape control sets H_S=H_B=0 and supplies a PURE qubit state,
with U_j columns equal to K1903's Gram vectors. It realizes C exactly with
energy conservation, but the Gibbs state of this degenerate H_B is I/2,
not pure. Conversely a nondegenerate pure ground can realize C with the
old arbitrary U_j only by violating conservation. These controls separate
rank, temperature, stationarity and thermal symmetry instead of conflating
them. Input faults remove one resonant unitary entry or alter a Choi index;
a clean baseline must pass before either fault is counted.

For a quantitative escape family, keep H_S=H_B=0 and the same four controlled
qubit unitaries, but prepare rho_q=diag(1-q,q), 0<=q<=1/2. The channel is
(1-q)Phi_C+q R, so its half-diamond error is at most q, while its distance
from the Gibbs state I/2 is exactly1/2-q. No energy conservation is broken;
the resource is nonthermal purity inside a degenerate energy shell. This
supplies an explicit finite realization as q tends to zero. Bound(4) gives
a necessary resource cost and this family a sufficient cost; the gap between
them is open and no sharp purity tradeoff is claimed.

## 5. Known context and claim ceiling

The relation between Schur channels and tracial unitary factorization is
established in [Haagerup and Musat](https://arxiv.org/abs/1009.0778).
The strict-conservation/Gibbs model is the thermal-operation definition used
by [Lostaglio, Korzekwa, Jennings and Rudolph](https://doi.org/10.1103/PhysRevX.5.021001).
We specialize existing tracial-witness and leakage arguments to an explicit
energy-shell obstruction; no novelty claim is made.

The target is covariant under every diagonal H_S and Gibbs preserving,
yet cannot be approximated below(2) by the stated finite thermal operations.
Thus covariance and Gibbs preservation alone do not supply this dilation.
The gap also holds under diamond-norm closure of this finite class by
continuity. It is not a theorem about every infinite-reservoir dynamics,
nonthermal apparatus, correlations, catalytic or measurement-assisted
process. K1920's successful driven construction remains valid and lies
outside the conservation condition. No GU mechanism is excluded.

## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 is UNCERTAIN about
its nonzero southeast rival. SC-MAS-01/SC-CHI-02 ASSERT a stylized curvature
mass toy; SC-META-53 remains UNCERTAIN about indefinite spectra. None selects
the positive Hilbert bath, scalar control or physical units used here.
LT-SM8, LT-GR6b and AC-F1, source-register and canon verdicts remain unchanged.
The full20 raw/barred map, separate K/C, accessible algebra and physical domain
remain distinct constructions. These are independent mathematical results.
Analytic arguments carry universal claims; exact finite probes test identities
and examples, not expert acceptance, empirical prediction or formal proof.
