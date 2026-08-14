---
title: "Source-residual cohomology research lane"
status: active_research
doc_type: research_lane_index
created: "2026-08-14"
lane_id: SRC-RES-COH-01
registry: lab/process/source-residual-cohomology-lane.json
claim_grade: "SOURCE-GROUNDED RESEARCH PROGRAM; NO QUANTUM SUPERPOSITION OR PHYSICAL COHOMOLOGY RESULT"
---

# Source-residual cohomology

## Purpose

This repo-native research lane rebases the superposition investigation on the
operator architecture Weinstein actually writes:

```text
first residual:       Upsilon_omega = 0
second action:        I2 = (1/2)<Upsilon_omega,Q_B Upsilon_omega>
second Euler system:  (D Upsilon_omega)^! Q_B Upsilon_omega = 0
proposed complex:     Upsilon_omega is the obstruction to delta_omega^2=0
```

`lane` here means a public GU research workstream. It is not a CapacityOS
service Lane, schedule, priority grant or scientific verdict.

The existing K77 work already owns substantial parts of this floor:

- `SC-ACT-04` and the source-natural fixed-grade `I2B` owner;
- exact selected residual, Hessian, Ward, BV/KT and Spencer packets;
- the exact failure of `II=0 iff D_A^*F_A=0`;
- the local-twistor/Bach--Yang--Mills detour comparator; and
- the absence of a positive physical cohomology.

This lane does not rebuild those results. It constructs the missing maps
between them.

## Working hypothesis

> **H1-R.** If GU derives superposition internally, its first plausible home
> is a positive physical cohomology of the action-owned total-residual
> deformation complex. The moving reduction and local-twistor structures must
> be derived as compatible reductions, prolongations or representations of
> that complex. They are not allowed to replace its action owner.

The mandatory null remains:

> **H0.** GU supplies classical complex-linear geometry while ordinary
> quantization supplies superposition externally.

## Swing sequence

| swing | question | earned result required before continuing | status |
|---|---|---|---|
| `SR-0` | Which operator owns the proposed cohomology and the Yang--Mills-like equation? | Typed separation of source residual square from ordinary Yang--Mills, with exact controls. | **executed** |
| `SR-1` | Does the source gauge map compose with the linearized total residual on an action-owned stationary background? | Construct `K`, `L_Upsilon`; certify `L_Upsilon K=0` on shell and identify reducibility. | queued |
| `SR-2` | Is the second action genuinely the square/factorization of the first layer? | Compare the full Hessian, including the residual-dependent term, with `L_Upsilon^! Q_B L_Upsilon`; identify the exact on-shell condition. | queued |
| `SR-3` | Does Weinstein's rolled Dirac--Rarita--Schwinger operator factor or intertwine with that complex? | Principal and lower-order symbol map on one common carrier/domain. | queued |
| `SR-4` | What exactly decouples into Weyl sectors? | Construct the off-diagonal zero-order mass/VEV block `M(Phi)` and prove the algebraic decoupling criterion `M=0`. | queued |
| `SR-5` | Does curvature dynamically control `M(Phi)`? | Derive, rather than posit, the map from scalar curvature/distortion/VEV to `M`; test low- and high-curvature controls. | queued |
| `SR-6` | Can local twistors carry the source complex and a positive physical state space? | Prolongation/intertwiner, Lorentzian closed domain, endpoint admission and positive pairing. | queued |
| `SR-7` | What would an observer measure after normal-sector reduction? | Derived transition law or memory kernel, reduced channel and coherence observable. | queued |

The dependency order is strict. A later swing may be explored early only as a
clearly typed comparator; it cannot close an earlier gate.

## First result

[`sr0-operator-owner-rebase-2026-08-14.md`](sr0-operator-owner-rebase-2026-08-14.md)
establishes the operator-owner rebase. Ordinary source-free Yang--Mills remains
a useful comparator and a component of the twistor detour, but it is not the
source's printed second equation. The next mathematical swing is `SR-1` on an
action-owned stationary background.

## Claim ceiling

This lane constructs no quantum state space, positive pairing, superposition
law, Born rule, luminous/dark separation, decoherence channel, memory kernel,
particle spectrum or empirical prediction. Weinstein's formulas are source
statements; repository computations decide only the exact objects they model.

