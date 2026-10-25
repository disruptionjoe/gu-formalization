---
title: "K2078: Thermal rigidity at both certificate endpoints"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed-bath conditional mathematics; no wider energy interval, GU verdict or novelty certification
scripts:
  - tests/channel-swings/k2078_thermal_certificate_endpoints.py
  - tests/channel-swings/k2078_thermal_certificate_endpoints_probe.py
---

# K2078: Thermal rigidity at both certificate endpoints

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: endpoint optimizer rigidity and minimum physical dimension
carrier: fixed four-state bath and finite/countable nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: nonnegative populations with exact shell-capacity marginal return ON=declared_bath_catalyst
real_structure: exact real rational population data
grading: occupied resonance components and physical empty shells
action_owner: repository-construction -- inherited thermal shell model
target: equality at certificate intersections MAP-TYPE=intertwiner
```

[Conditional mathematical theorem, internal verification.] K2075's unique occupied
population and minimum physical dimension41 hold on the CLOSED K2074 energy interval,
for every spacing1/2<delta<=1 and finite or countable catalysts. The extra tied
certificates at its two endpoints cannot attain there. These endpoints are certified
line intersections; neither is established as a physical phase transition.

## 1. Question and inherited premises

K2074 proves the optimal value a0-t0 E on its closed interval [Eminus,Eplus], with

    a0=178897536881397/603186054075536,
    t0=4369812550533/603186054075536,
    [Eminus,Eplus] approximately [2.4800787763,2.5075721054].

Use the exact endpoints in the accompanying JSON, never rounded endpoints as proof.
K2075 classifies equality only on the OPEN interval because its strict other-cell
argument does not directly cover the boundary ties. All671 assigned certificate
lines are reused with their historical replacement order. Exact intersections give
contacts{187,188} at Eminus and{187,235} at Eplus, with every other cell strict.
This does not itself give a competing optimizer. In particular K2068's N20 physical
witness remains feasible on the larger chamber approximately[2.4328011574,2.6937763949].

Inherited proof premises include the actual support/deficit-sign polyhedral bank,
its completeness, compulsory physical placement, finite/countable tail transfer,
and K2074's corrected cell188 fourth-terminal coverage. They are pinned reuse, not
proved by the arithmetic count below. This note does not change the source register,
physics ledger or canon, and the bath model is independent mathematics.

## 2. Cell188 cannot attain the left endpoint

Use cell188's own fixed certificate (a188,t188), not the cell187 line. Its retained
support is[1,3,5,7,9,11]. Let A11 be the last retained deficit,

    A11=max(0,p11-max(0,H_last*p_previous-L_last*p11)).

The inherited common-tail weight is theta=69/100. For terminal ratios x_i and
stored exact terminal loss c, the boundary price is

    sum_i reward_i*x_i - c - (theta/2)*min(1,max(0,L_first*x1-H_first)).

Enumerate every permitted single, pair, triple and required fourth-terminal piece.
The shorter triple222 remains with its ordinary final reward a188-17t188; its
extensions2222 and2223 use the fourth Bellman reward. Other triples use their third
Bellman reward. Dropping the shorter prefix or retaining its already-expanded
Bellman reward changes the certificate and fails the probe.

There are1,217 candidate vertices and547 recession directions, including the two
single directions. Recession slacks are strictly positive. The sole maximizing
vertex is2222 with ratios(1/9,1/81,1/729,1/6561), giving

    beta188=3190106874287378039504500555992 /
            123451663601334877512465884841883.

The low boundary is max(0,beta188*p11+theta*A11/2). Of all low bank vertices only57
has zero slack; its normalized retained populations are

    (4374,6561,729,81,9,1)/11755.

On this ray A11=0 and p11>0, so the boundary is positive. Within each actual
piecewise affine subcell, equality forces this vertex, then the unique terminal
maximizer. Every surviving equality branch therefore has positive atoms through19
and state(19,incoming gap2).

The inherited saturated deep cap is(20,2), but a successor of(19,2) has gap at
least2 and cannot reach20. Every cap at energies21 and higher is strict. The exact
state-aware Bellman policy then forces gap2 with ratio1/9 through43. All later
rewards are negative at reachable successor energies and their Bellman values vanish,
so a positive further atom produces strict slack. This uses the additive nonnegative
slack identity of K2075, including its y terms; a zero excess alone would not prove
the population ratio. The initial state19 is covered by the explicit four-terminal
price and is NOT required to satisfy a standalone sharp-cap inequality.

Normalize the resulting necessary equality ray. Its exact mean energy is

    52556574640714848457/21782483947476997435
      approximately2.4127906976744184,

which differs from Eminus. Thus this ray cannot attain the left-endpoint optimum.
Necessity is sufficient for this exclusion; we need not claim this ray is a feasible
optimizer at its own mean energy.

## 3. Cell235 cannot attain the right endpoint

Use its inherited fixed certificate(a235,t235), retained support[1,3,5,7,10,11]
and high placement offset11. The unique zero-slack low bank vertex is35:

    (2484,3726,414,46,2,1)/6673.

The only admissible first gap is3. For G=G(14,3), L=8/15, H=1/15, p=p11 and
A=A11, its exact first-terminal boundary is the maximum of

    0,
    G*p/23,
    (G-1/2)*H*p/L + (1/2+(G-1/2)/L)*A.

At vertex35, A=p and the second piece is strictly largest. Hence p14=p11/23.
The correct Bellman state at14 is incoming gap3, permitting next gap1. Exact
state-aware maximization forces the path

    14 ->15 ->18 ->19 ->22 ->23 ->26 ->27 ->30 ->31 ->34,

with alternating ratios7/29 and1/23. Every visited cap is strict. The sole saturated
cap(16,2) is never reached, and the unique maximizing transitions cannot be changed
without strict Bellman slack. The final state34 has positive reward but every allowed
successor has zero Bellman value and negative ordinary reward, excluding extra atoms.

The normalized necessary equality ray has exact mean energy

    4070219131364914959/1688497548141045800
      approximately2.410556731838924,

which differs from Eplus. The right-endpoint competing cell is therefore excluded.

**Correction during derivation.** A provisional continuation incorrectly initialized
state14 with incoming gap2, producing an even-level path and a different energy.
That calculation was rejected before acceptance. The independent probe mutates the
incoming state back to2 and detects the error. The corrected path above is the only
one used in the manifest and endpoint theorem.

## 4. Other components and countable equality

The exclusions must not be defeated by adding an arbitrarily small high component
at very high energy. The producer and separate raw-bath probe check strict high
retained and wholly erased root margins for each tied certificate. Use high offset
25/2 for188 and the ORIGINAL offset11 for235. For all bank vertices, the high slack is

    R_low-a+t*(E_low+ell)
      -p_last*max(0,max_allowed d K_d*G_(a-t ell,t)(last+d,d)).

Its minimum is strictly positive; so is the erased root margin
1/2-a+t*(n+ell)-K_d*G_(a-t ell,t)(n+d,d) for n>=12. The finite check reaches64;
thereafter the reward is negative, G=0, and the margin increases, proving all roots.
All shifted suffix caps are valid. Exact minima are stored in the manifest.

Every nonzero high component has either positive retained mass or a first positive
atom. The positive margins therefore rule out every such component at equality.
The same nonnegative sum argument works for countably many components. Finite first
moment and finite-support Bellman reward remove the boundary term in the suffix
slack identity, exactly as in K2075. Positive slacks cannot cancel in a countable
mixture. Saturated mean energy and zero low offset remain necessary because t>0.
Thus the incompatible necessary energies in sections2 and3 cannot be repaired by
mixing in a hidden high component or leaving energy unused.

## 5. Closed interval consequence and physical dimension

At either endpoint, only cell187 remains eligible for equality. Its internal strict
high/root/ray/cap margins, low two-vertex cone and exact mass/energy solve from K2075
do not depend on openness of the global certificate interval. Both endpoints lie
strictly inside the positive N20 affine-population chamber. Thus the unique occupied
population measure remains the K2068 affine family on energies1,3,...,39.

All20 populations are strictly positive at both endpoints. Shared bath shells from
each adjacent occupied pair force the physical levels0,...,40. The actual K2068
construction on those41 levels attains the value, so the minimum physical catalyst
dimension remains exactly41. This is not channel uniqueness or a classification of
all optional empty levels. The separate raw-return probe evaluates the endpoint
population/normalization/energy identities and mandatory-shell union directly.

The theorem adds the two endpoints to a previously open equality theorem. It does
NOT extend the optimality interval into a neighborhood, infer a uniform gap from
pointwise nonattainment, or classify the next energy phase. A quantitative improved
certificate for the competing cells, or a new physical witness, is required next.

## 6. Verification and remaining question

The producer reconstructs all671 endpoint comparisons, the1,217/547 terminal census,
low equality contacts, complete high/root margins and exact state-aware necessary
rays. The separate checker reconstructs serialized terminal costs from the bath,
uses a fresh recursive Bellman evaluator and independently checks endpoint witnesses
and physical-shell necessity. Seven genuine faults test shorter-prefix coverage,
incoming-state dependence, tail ratios, last atoms, cap reachability, false endpoint
attainment and physical dimension. These checks support the written proof; they do
not replace inherited continuum/countable geometry or specialist scrutiny.

Independent internal thermal and final proof review are recorded at their actual
scope. No external specialist or proof-assistant certification is claimed. The next
useful thermal test is a stronger quantitative188/235 certificate or a concrete
outside-interval feasible population; the closed endpoints themselves are settled.
