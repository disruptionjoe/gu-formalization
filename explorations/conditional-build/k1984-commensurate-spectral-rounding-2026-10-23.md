---
title: "K1984: Exact spectral lattice reduction and the five-level thermal frontier"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1984_commensurate_spectral_rounding.py
  - tests/channel-swings/k1984_commensurate_spectral_rounding_probe.py
---

# K1984: Exact spectral lattice reduction and the five-level thermal frontier

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
result: conserving protocol preserved by energy rounding, finite exact templates and all-temperature five-level frontier
carrier: finite nondegenerate catalyst, bath energies0,1,2,3 and spacing h=1/m LAYER=toy CHIRALITY=N/A
pairing: positive trace and worst-input catalyst marginal half trace distance ON=independent_initial_registers
real_structure: complex conserving unitaries; arbitrary coherent catalyst preparation
grading: energy shells, not physical chirality
action_owner: repository-construction -- fixed four-state Schur-channel model
target: exact mean-budget optimization with commensurate minimum spectral spacing MAP-TYPE=intertwiner
```

## 1. Round the spectrum without altering the protocol

Keep the exact channel and bath of
[K1981](k1981-wide-spacing-thermal-frontier-2026-10-23.md), but take minimum
adjacent catalyst gap h=1/m, m a positive integer. Ground energy is0,
dimension is finite, and energy is bounded ABOVE by E. The preparation may
be coherent. For any admissible real spectrum e_i define

    q_i=h floor(e_i/h).                                  (1)

The rounded spectrum remains strictly increasing with minimum gap h and
q_0=0; moreover q_i<=e_i. The key is floor translation by an integer:

    e_i+b=e_j+c, b,c in{0,1,2,3}
    implies q_i+b=q_j+c.                                (2)

Therefore EVERY matrix element of the ORIGINAL energy-conserving unitary
still conserves the rounded total energy. Keep the identical unitary,
preparation matrix and bath state in the same labeled bases. The simulated
channel and every reduced-state return error are EXACTLY unchanged, including
coherent preparations and all input states. The catalyst mean energy can only
decrease, since it uses the unchanged nonnegative diagonal populations.
Rounding may create new resonances but cannot remove an old unitary block.
No continuity approximation, perturbative conservation or refitted channel
is involved. This protocol-preserving argument is stronger than comparing
only optimized shell values.

The proof applies to any finite ancillary Hamiltonian whose energy differences
lie in hZ, with the same fixed ancillary state and the relevant commuting
unitary. Here the ancillary range is3. It does not change the bath's Gibbs
weights: only the catalyst Hamiltonian is rounded.

## 2. Finite exact physical templates

On the rounded lattice, replace each adjacent gap larger than3 by3, keeping
all smaller gaps. Each original unitary block spans catalyst-energy differences
of at most3; it never crosses an old gap larger than3. Such a compression
translates each old block rigidly and preserves its conservation. New blocks
may meet; keep their old direct-sum action. Energy only decreases, all gaps
remain at least h, and the final spectrum obeys

    adjacent gaps in{h,2h,...,3}, max energy<=3(d-1).       (3)

Thus for dimension at most d, the exact mean-budget optimum is the minimum
over finitely many ACTUAL physical spectra: at most
sum_(n=1)^d (3m)^(n-1) gap templates. These are not colliding tagged limits.
After the existing energy-pinching reduction, the shell-rank condition and
sharp return formula reduce each template to finitely many population
polytopes and linear pieces. For rational t in(0,1) and rational E, all
coefficients are rational. An optimum is attained by rational populations
on a rational spectrum whenever feasible. This reuses the existing shell
optimization; the new reduction removes real spectral variables while
retaining spacing exactly.

At zeros of a population, drop that occupied direction; the shell-rank
condition only becomes easier. Hence closed population cells remain physical.
Exact-energy equality is different: (1)-(3) lower energy and do not prove
an equivalence for a prescribed mean E. Arbitrary noncommensurate spacing
or off-grid bath differences also require a new argument. Explicit controls
show both failures: rounding a spacing7/10 spectrum on a half-unit lattice
can reduce its gap to1/2; a bath gap3/2 rounded with h=1 can destroy an old
conserving transition. Nearest/upward rounding may increase the energy budget.

## 3. Executed consumer: complete spacing-one, at-most-five-level frontier

For h=1, at most five levels, and every0<t<1, set q=t^2. The finite exact
census covers all120 gap templates with2--5 levels and all nonempty candidate
supports of size at least2. Sixteen two-population cases survive. Only
spectrum{0,1,2,3,4} with support{1,3} has occupied-shell overlap; the other
fifteen supports have energy separation at least4 and optimal return1/2.
No support of size3 or more survives. Pure preparations also have return1/2.
This disproves the initial conjecture that only ONE two-population template
is feasible; only the IMPROVING template is unique.

The finite reduction(1)-(3) proves this exhaustive integer census covers ALL
real spectra with spacing1 in this dimension bound. The minimum occupied
energy is at least1: an occupied e<1 has no distinct partner in its bath0
shell. The four-level spectrum{0,1,2,3}, prepared at1, attains return1/2.
For E<1 the problem is infeasible.

In the improving template let p be the population at1, with1-p at3.
Its mean is3-2p. The sharp shell formula gives, with
A=1/[2(1+q)], B=1/(1+q), C=(2+q)/[2(1+q)],

    R(p)=(1-p)/2                      for0<=p<=A,
         p/2+q/[2(1+q)]              forA<=p<=B,
         C-p/2                        forB<=p<=C,
         p/2                          forC<=p<=1.         (4)

For example, combine the shell maxima into max(qp,1-p), then take the two
positive parts in the return formula. Their zeroes are exactly A and C.
These four affine pieces prove the whole-temperature statement, not a set
of sampled temperatures. Minimize over p>=max(0,(3-E)/2).
Define

    E_c=(1+2q)/(1+q), E_s=(1+4q)/(1+q), E_a=(2+3q)/(1+q).

The COMPLETE optimum is

    F_5,1,t(E)=(3-E)/4                         for1<=E<=E_c,
               (2+q)/[4(1+q)]                forE_c<=E<=E_s,
               (3-E)/4+q/[2(1+q)]            forE_s<=E<=E_a,
               (1+2q)/[4(1+q)]               forE>=E_a.  (5)

All values are attained. Here the dimension allowance is AT MOST5; no
assertion is made for larger dimensions. At t=1/2 the breakpoints are6/5,
8/5,11/5 and the plateau values9/20,3/10. These specialize to the existing
fixed-temperature five-level evidence; their independent reuse is a control,
not a new claim about that already-known special case. Formula(5) extends
it to every0<t<1 and removes a real-spectrum assumption via(1)-(3).
At E=2 and t=1/2 the optimum is7/20, recovering K1981's boundary witness
as optimal in this five-level spacing-one class, not for arbitrary d.

## 4. Validation, hostile review and next boundary

Producer:5416 exact lattice/transition controls,12 actual feasible channel
families, and45 exact temperature/budget frontier controls. Separate probe:
120 exhaustive integer shapes and all candidate supports;117 transition,
energy and piecewise-minimization controls. Four genuine upward-rounding,
level-collision, gap-cap and off-grid-bath faults are rejected after baseline.
The finite census is exhaustive only AFTER the proved real-to-lattice
reduction. Exact finite examples alone would not establish that reduction.

Strongest overclaim: preserving exact energy or arbitrary spacing. Both are
explicitly excluded. Strongest contrary case: newly merged shells; retaining
the original unitary's direct-sum blocks preserves the entire protocol.
Weakest scaling seam: template count is exponential and (5) stops at d=5.
The next substantial question is a matching small-spacing resource bound or
larger-d structural optimization, using lattice reduction where its arithmetic
hypotheses hold. This is independent thermal mathematics; SC-META-53 remains
UNCERTAIN and source, physics ledger and canon do not change. No novelty,
external expert or proof-assistant certification is claimed.
