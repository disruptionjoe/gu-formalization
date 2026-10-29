---
title: "K2257 Finite battery capacity for retained detector outputs"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied model theorem only; no source physicalization or canonical verdict
scripts:
  - tests/channel-swings/k2257_finite_battery_service_capacity_probe.py
---

# K2257 Finite battery capacity for retained detector outputs

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2257 Finite battery capacity for retained detector outputs
carrier: K vacuum two-mode oscillator inputs, retained output fields, finite charge battery and zero-charge ancillary memory LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product and trace distance ON=declared_carrier
real_structure: complex conjugation and Hilbert adjoint
grading: nonnegative total oscillator number, not general nonuniform energy
action_owner: repository-construction -- K2253 conserving detector apparatus with no charged replenishment
target: joint service capacity and necessary donor-charge budgets MAP-TYPE=intertwiner
```

## Question and exact physical boundary

[K2253](k2253-full-instrument-reference-reuse-2026-10-29.md) constructs a finite reference for finitely many complete detector calls. It does not claim perpetual catalysis. We test uniform service by retaining all outputs of K vacuum calls to its actual b=(5/3)a1+(4/3)a2* Lüders instrument.

Assume the initial battery has number support0,...,H; all other device memories/ancillas start in nonnegative zero-charge sectors; fresh system inputs are vacuum; every device operation has a dilation commuting with all spectral projections of total number. U(1)-covariance or conservation of the mean alone is insufficient. Old output fields are isolated and retained, with no harvesting/reuse of their charge. External controls may change Hamiltonians only within a conserving dilation and introduce no hidden charged donor. The test strategy simply supplies vacuum and keeps the outputs, so failure already lower-bounds worst-case adaptive service error. A controller that recharges the device changes these hypotheses.

This is a charge-budget result, not a general no-catalysis or asymmetry no-broadcasting theorem. [Åberg](https://arxiv.org/abs/1304.1060) supplies the broader coherence context; it does not supply the bounded retained-output premise used here.

## 1. A support witness for the whole output history

Total number conservation and positivity imply

    support(sum_(i=1)^K N_Oi)<=H                       (1)

for the actual joint output. This remains true with battery coherence, arbitrary internal correlations, adaptive conserving controls and any neutral degeneracy. Number conservation constrains total support, not just expected number. Discarded positive-charge waste can only reduce the available output budget.

The ideal vacuum output distribution from K2253 is

    P(N=0)=337/625,
    P(N=2j)=(162/625)(16/25)^j, j>=1.                  (2)

For the ideal K-fold instrument, outputs are independent on these vacuum inputs. Put Y=N/2, h=floor(H/2), r=16/25, p0=337/625, q=288/625. The probability generating function is

    g(z)=p0+(162/625)rz/(1-rz)
        =(337-112z)/(625-400z).                       (3)

Measuring the effect 1_(sum N>H), zero on every actual output, gives the exact necessary lower bound

    epsilon_K >= T(K,H)
      :=1-sum_(s=0)^h [z^s]g(z)^K.                    (4)

Here epsilon_K uses half trace norm on joint outputs, and therefore lower-bounds the corresponding worst-case complete process distance in that normalization. This is a lower bound on achievable channel/process error, not an asserted exact optimum. It needs neither battery restoration nor a phase-reference approximation theorem. At K=1 it is q r^h; at H=0 it is1-p0^K. Adjacent H=2h and H=2h+1 have the same bound. Every finite H already incurs a strictly positive one-call tail.

For an independent exact coefficient evaluation, condition on the number X of nonzero outputs. X is Binomial(K,q), and Y|Y>0 is positive geometric with success9/25. For s>=1,

    P(sum Y=s)=sum_(x=1)^min(K,s) binom(K,x)p0^(K-x)q^x
                     binom(s-1,x-1)(9/25)^x r^(s-x).  (5)

The zero coefficient is p0^K. This evaluates(4) without truncating the target instrument or treating finite samples as an infinite-tail proof.

## 2. Lifetime, linear capacity and explicit finite consequence

Since sum N>=2X, T(K,H)>=P(X>h). A convenient sharper exponential estimate uses any0<z<1:

    T(K,H)>=max(0,1-z^(-h)g(z)^K).                   (6)

Indeed z^sumY>=z^h on sumY<=h, so Markov's inequality bounds that event. At z=1/2 this is1-2^h(281/425)^K. For K=100,H=20, exact rational comparison gives error>1-10^-14. The full infinite output tail is included; a charge cutoff with a handful of levels cannot sustain this retained-output service.

From(2), mean mu=64/25 and variance v=94336/5625 for N. Cantelli's inequality gives, when mu K>H,

    T(K,H)>=(mu K-H)^2/[v K+(mu K-H)^2].              (7)

Thus epsilon_K<=epsilon<1 requires

    H>=mu K-sqrt(v K epsilon/(1-epsilon)).            (8)

If H>=mu K this necessary bound is automatic. For K=1000 and epsilon<=1/100, (8) implies H>2546 and hence integer H>=2547 (the probe checks the conservative arithmetic). As K increases, any uniform error ceiling below1 requires liminf H_K/K>=64/25. If limsup H_K/K<64/25, error tends to1. A budget above this slope merely removes this obstruction; it does not construct a phase reference, controls or accurate detector. Fixed finite H yields T(K,H)->1 by either(6) or(7).

## 3. Replenishment and restoration tradeoff

If additional prepared charged donors have joint number support at most D, replace H by H+D in(1)--(8). An unbounded-support donor requires its actual tail account; it cannot be replaced by its mean in the support theorem.

A separate mean-budget inequality prices approximate battery return. Suppose initial donors have total mean charge d, battery restoration marginal error delta_B, and field output i has error epsilon_i from the ideal vacuum marginal. For integer J>=1 use F_J=min(N,2J), whose ideal expectation is

    mu_J=(64/25)[1-(16/25)^J].

Bounded-observable duality gives actual output charge at least sum_i(mu_J-2J epsilon_i). Conservation bounds that charge by the battery mean loss plus consumed donor charge; the former is at most H delta_B, the latter at most d. Therefore

    H delta_B+d>=K mu_J-2J sum_i epsilon_i.            (9)

If a joint output-plus-battery restoration comparison against the original battery marginal has error epsilon, delta_B<=epsilon and every epsilon_i<=epsilon, so d>=max(0,K mu_J-(H+2JK)epsilon). This is necessary charge supply, not sufficient coherence renewal. A diagonal donor can carry enough number and still lack the asymmetry needed by the target. Correlations do not defeat(9), but signed-charge ancillas, output recapture, nonvacuum inputs or nonconserving drives change its premises.

The finite capacity result strengthens the one-use restoration witness into an entire retained-output service obstruction. It leaves two substantive engineering successors: a priced charged/coherent replenishment process, or a different service interface that permits output-energy recovery and includes its disturbance in the target. It does not invalidate K2253's finite-use construction with its very large battery.

## Reproduction and scope

Run `python tests/channel-swings/k2257_finite_battery_service_capacity_probe.py`; `--write` refreshes its exact report. Finite exact controls and changed-input faults supplement the written universal proofs, not certify them by sampling. The concrete proof and controls received independent internal specialist review; no Lean, external-expert, novelty or remote-CI certification is claimed.

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 remains UNCERTAIN on the southeast rival; SC-META-53 remains UNCERTAIN on physical positivity. These results concern supplied constructions, not every source-admitted completion. LT-SM8/LT-GR6b/AC-F1 and ledger0.263 remain unchanged. Preserve full16cells/full20/K-C, native2+1/nonchiral, physical quotient and global source-domain debts.
