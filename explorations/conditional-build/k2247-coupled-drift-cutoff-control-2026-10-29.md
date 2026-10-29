---
title: "K2247 Positive local cutoff cancellation of coupled detector drift"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied mathematics; no source selection or physical recovery
scripts:
  - tests/channel-swings/k2247_coupled_drift_cutoff_control_probe.py
---

# K2247 Positive local cutoff cancellation of coupled detector drift

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2247 Positive local cutoff cancellation of coupled detector drift
carrier: finite bosonic hopping graph with finite record and arbitrary reference LAYER=toy CHIRALITY=N/A
pairing: declared positive product Hilbert norm ON=declared_carrier
real_structure: real raw matrices or complex Hilbert adjoint as specified below
grading: local bosonic occupation and finite classical-record labels
action_owner: repository-construction -- explicitly supplied operator below
target: complete recorded detector channel under coupled drift and finite resources MAP-TYPE=intertwiner
```

## Result and scope

[K2244](k2244-onsite-drift-local-control-2026-10-29.md) retains onsite drift using local phase modulation; coupled drift spreads that modulation. Here bounded positive site/edge controls cancel a specified finite number-preserving hopping drift exactly on a proved reachable cutoff sector. This yields the same complete finite recorded detector, with arbitrary-reference photon-budget error. Control strength grows with the cutoff: there is no arbitrary-small-fixed-cap theorem.

The model is M finite bosonic sites, finite record and arbitrary reference. H0=dGamma(h), h=h*>0, is a supplied finite positive one-particle matrix supported on onsite and graph edges. It is not arbitrary coupled quadrature drift, K2225's full W-squared model, a continuum field, a source-owned GU operator or a restricted laboratory control alphabet. Source claims and ledger0.263 stay unchanged.

## 1. Positive bounded local cancellation

Write H0=sum_e h_e, one onsite/edge number-preserving second-quantized term per e. Let N_e count particles on that support. The one-particle norm c_e bounds

    ||h_e restricted to N_e<=A||<=A c_e.

For example onsite omega_i n_i has c_e=omega_i; hopping J a_i* a_j+conj(J)a_j* a_i has c_e=|J|. Individual hopping terms need not be positive. For integer A>=0 define

    P_e=1_(N_e<=A),
    C_e=P_e(A c_e-h_e)P_e.                         (1)

Then C_e>=0, ||C_e||<=2A c_e, with the same site/edge support. It has finite rank only on that local factor; spectator identities prevent calling it globally finite rank. It commutes with total N. On the total-number subspace N<=A, every P_e is identity, so

    D=H0+sum C_e=lambda I,  lambda=A sum c_e.        (2)

H0 remains present; bounded additive controls produce the cancellation. Globally D>=0 because H0>=0 and C_e>=0, and D is selfadjoint on Dom(H0). Outside N<=A, (2) is not asserted.

## 2. Reachable support supplies the missing exactness proof

For q ideal local unitaries U_j of the K2241 coherent detector, use K2244 polar completion to get local W_j, identity outside local N_j<=R_j. Choose positive spectral logarithms K_j, 0<=K_j<=2pi, exp(-iK_j)=W_j, zero outside that local cutoff. Every partial path exp(-is K_j),0<=s<=1, preserves the local cutoff and fixes its complement.

If input has total N<=B, such a path has total support at most B+R_j: spectators carry at most B, and the changed local occupation is at most R_j. This conservative bound need not be sharp. Fix an input total cutoff L0 and

    A=L0+sum_j R_j.                                (3)

During each gate the ideal finite-gate path stays in total N<=A. Implement the piecewise-constant Hamiltonian H(t)=D+K_j/tau during slot j of duration tau>0. On that exact path D=lambda, so exp(-i lambda t) times the finite-gate path solves the actual full Schrödinger equation. Uniqueness for selfadjoint bounded perturbations proves exact equality for every initial N<=L0 state, including arbitrary reference. There is no Trotter limit, unproved projected-generator convergence, or instantaneous pulse assumption. The scalar phase cancels from the recorded channel; no laboratory-frame phase correction is needed.

This is a solution-path argument, not a claim that N<=A is invariant for every imaginable sequence from every state in that sector. The initial L0 and ordered gate support bounds are essential.

## 3. Complete recorded/reference error

Assume input mean G=N+1<=B0, e.g B0=E/h_min+1 when Tr H0 rho<=E and h_min>0. Zero modes require a separate photon budget. Ideal target-prefix energies obey mean G<=B from K2241's explicit transport estimate; each U_j obeys U_j*G_j U_j<=gamma_j G_j. Choose local L_j<=R_j and delta_j²=gamma_j(L_j+1)/(R_j+1)<1. K2244 gives

    epsilon_gate <=sum_j [delta_j+delta_j²+2sqrt(B/(L_j+1))].

For actual versus finite-gate dynamics, both agree on input P_(N<=L0). On its complement two isometries differ by at most2, so purification gives half trace error<=2sqrt(B0/(L0+1)). The triangle inequality gives

    epsilon_total<=min(1,2sqrt(B0/(L0+1))+epsilon_gate). (4)

The extra initial tail is counted ONCE. Gate errors use ideal-prefix B on the original state; actual prefixes need not obey B. Pinching the record after controlled feedback produces exactly the target complete instrument and contracts error, as in K2241. No unrecorded-only shortcut is used.

The total control obeys

    ||sum C_e+K_j/tau||<=2A sum c_e+2pi/tau.         (5)

Finite rank, precision, static cutoff controls and slot timing remain supplied. Increasing tau makes the gate part small but cannot remove the cancellation cost2A sum c_e. Equation(5) is a sufficient resource bound, not a lower bound for every possible controller.

## 4. Actual energy stays finite, without claiming convergence

Let g=2pi/tau and C=sum C_e. During a constant slot, H=D+K_j/tau is conserved. Since both D and K_j are positive, at any time in that slot

    <D(t)><=<D(start)>+g.

Iteration gives, for input finite H0 energy E,

    <H0(t)><=<D(t)><=E+||C||+qg
                    <=E+2A sum c_e+2pi q/tau.       (6)

The inequalities extend from finite-energy form-domain states by positive spectral approximation. Switches change the Hamiltonian, not the state. This bound avoids K2244's onsite-only per-gate occupation increment: under coupled drift a local gate can replenish particles while drift transports them. It proves finiteness for the actual input, not convergence of output energy as cutoffs grow and not optimal switching work. All controls are bounded, so each Hamiltonian H0 plus its bounded control has domain Dom(H0); the piecewise propagator is well-defined.

## 5. Concrete consumers and a cutoff counterexample

For the two-site h=[[2,1],[1,2]], h_min=1 and sum c_e=5. Use E<=1 so B0=2. K2241's complex-mode fixture has B=5832, q<=12 (the K2244 final onsite phase corrections are unnecessary here), gamma_j<=9. Set

    L0+1=10^8, L_j+1=10^9, R_j+1=9*10^15,
    A=(10^8-1)+12*(9*10^15-1).

Then the initial tail is<3/10000, every delta<=1/1000, and each local tail<1/200. Therefore

    epsilon_total<3/10000+12*(1/1000+1/10^6+1/200)
                 =0.072312<0.1.                  (7)

At tau=1, duration is12, the sufficient control cap is10A+2pi, and actual energy is at most1+10A+24pi. These enormous finite numbers certify existence under a different resource regime, not efficient hardware or a fixed-cap physical implementation.

Why(3) matters: start the same two-site model in vacuum. A local generator K=(I-X) on site1's |0>,|1> subspace is positive, and a pi/2 slot produces a phase-equivalent bit flip; take R=1. With correct A=1, D is scalar along this whole path. With the incorrect A=0, all C_e vanish. H0 K|00> contains a nonzero |01> term; the second-order coefficient of actual evolution differs from the intended local gate. This is actual remote leakage under an insufficient cutoff, not a mutated success assertion.

## 6. The cancellation strength cost is sharp within this local architecture

For one hopping edge with coupling J, its restriction to exactly A bosons has spectrum (2k-A)|J|, k=0,...,A. This follows by diagonalizing its two one-particle modes into energies plus/minus|J| and taking bosonic occupation sums. Any positive edge control that cancels this term to a scalar lambda on the ENTIRE N_e<=A sector must equal lambda I-h_e there. Positivity requires lambda>=A|J|, and its norm on the eigenvector with energy -A|J| is lambda+A|J|>=2A|J|. Equation(1) attains this bound for the edge at lambda=A|J|.

This is a genuine lower bound for positive scalar cancellation by that edge control, not a universal lower bound on all local circuit synthesis. Time-dependent alternative controls, different division among supports, or approximate cancellation can leave this architecture. Merely lengthening gate duration cannot lower its static edge requirement. It explains why cutoff growth cannot silently be used under an arbitrary fixed cap.

## 7. Consequence and remaining work

The selected finite number-preserving coupled drift no longer blocks a bounded positive local existence construction, provided large cutoff-dependent cancellation controls are supplied. This does not remove locality/control-alphabet limitations by pretending interaction-picture conjugation stays local. The canceled model still uses site/edge operators, priced at(5), and the exact reachable-sector proof explains why they work.

Useful successors require a specified restricted control algebra, a fixed strength/precision budget with efficiency or lower bounds, or non-number-preserving/continuum dynamics with independent energy and locality estimates. Existing onsite arbitrary-cap and present coupled cutoff-cost theorems have different hypotheses. Neither implies the other regime for free.

Independent review checks positivity, domains, support through partial gates, reference-tail accounting, complete record, and actual-energy conservation. Exact small Fock fixtures and genuine input faults supplement the universal written proof; no finite check count proves the infinite-dimensional argument or a GU physical bridge.

## Reproduction and evidence kinds

Run `python tests/channel-swings/k2247_coupled_drift_cutoff_control_probe.py`. `--write` refreshes the report; default execution recomputes finite controls and input faults and rejects stale note/code/dependency hashes. Universal proofs are internally reviewed mathematical arguments, distinct from finite controls and reporting integrity. No external-expert, proof-assistant, remote-CI, hardware or novelty certification.
