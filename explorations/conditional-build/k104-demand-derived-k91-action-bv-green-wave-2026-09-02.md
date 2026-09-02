---
title: "K104 demand-derived K91 action, BV and Green completion"
status: active_research
doc_type: reverse_scaffold_coefficient_complete_action_bv_domain_green_result
created: 2026-09-02
date: 2026-09-02
claim_ceiling: exact repository-owned free real split-l2 action with frozen coefficients, shift gauge, minimal classical abelian BV extension, Euler/Noether identity, Hessian/formal adjoint, maximal closed history realization, common invariant core, retarded/advanced pair, Green form and common-domain boundary spectral family; no authenticated Weinstein source action, GU-native action, nonlinear or quantum BV, curved-spacetime hyperbolicity, local net, state, detector, Born rule, K155 admission, prediction, confirmation or verdict
manifest: lab/process/k104-demand-derived-k91-action-bv-green-wave.json
probe: tests/channel-swings/k104_demand_derived_k91_action_bv_green_probe.py
---

# K104 demand-derived K91 action, BV and Green completion

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

Scope: this packet constructs one complete free action exactly on K91's split
functional carrier. It is demanded backward by the already frozen quotient,
domain and Green conditions. It is not recovered from Weinstein's source and
does not claim that this action describes GU or nature.

```gu-typed-objects
result: one coefficient-complete free real action owns the K91 split quotient, Euler-Noether-BV complex, closed history realization, causal Green pair and model boundary family
carrier: real G and P copies of l2(N), histories in compactly supported smooth rapid sequences, and the quotient of G direct-sum P by G direct-sum zero LAYER=observed CHIRALITY=N/A
pairing: positive real l2 pairing on G and P, history L2 pairing, causal antisymmetric Green form and endpoint Green boundary form ON=repository_owned_action_control
real_structure: coefficientwise real carrier; complex K91 is its complexification, with no Cl(9,5) or Cl(7,7) identification
grading: fields g,p; gauge parameter and ghost c; minimal antifields g-star,p-star,c-star; no source BV-BFV grading
action_owner: repository-construction -- every displayed coefficient and map is frozen in this packet
target: K91 split functional quotient/action/domain/Green completion MAP-TYPE=quotient
```

## Inline preflight bookend

The gate was re-derived from current state after K103. The route-changing lens
census covered real variational calculus, linear gauge systems, Noether
identities, BRST/BV, closed Fourier multipliers, invariant nuclear cores,
hyperbolic Green operators, Peierls forms, endpoint symplectic data, boundary
spectral families and source-custody ceilings. Retrieval found K91's exact
functional complex and causal pair, but no action whose variation produced
them. Earlier K77 conventional action controls bind different finite-rank and
spacetime carriers and are not this object.

The cheapest decisive route is the unique diagonal free quadratic action with
K91's frozen frequencies. A prose template was rejected because it would not
own coefficients or maps. A source-action search was rejected by the active
reverse-scaffold contract: K103 proved the filed root empty, while the K91
downstream demands are sufficient to construct a repository control.

Positive controls fix the split sequence, unit kinetic coefficient, exact
`(n+1)^2` potential, nilpotent shift BRST differential, opposite Green support
and a no-crossing boundary family. Negative controls independently mix the
quotient, alter one potential coefficient, add a mixed Hessian entry, break
BRST nilpotence, leak support, reverse the advanced sign and force a boundary
crossing.

## The frozen action and its variation

Let `G=P=l2(N,R)`, let `Omega e_n=(n+1)e_n`, and retain K91's rapid core

```text
s = intersection_(k>=0) D(Omega^k).
```

For compactly supported histories `g,p in C_c^infinity(R;s)`, set

```text
S(g,p) = 1/2 integral_R (
           <partial_t p, partial_t p> - <Omega p, Omega p>
         ) dt.                                                (1)
```

There are no suppressed coefficients: the kinetic coefficient is `1`, the
mode-`n` potential coefficient is `-(n+1)^2`, and the coefficients of `g` and
every `g-p` mixed term are zero. The shift gauge action is

```text
delta_alpha g = alpha,       delta_alpha p = 0.               (2)
```

Integration by parts on compact support gives

```text
E_g = 0,
E_p = -(partial_t^2 + Omega^2)p = -L p.                       (3)
```

Thus the Noether identity is not a label: `d0^* E=E_g=0`. The
ambient Hessian is `diag(0,-L)` and its gauge radical contains exactly the
displayed `G` direction before any solution-space degeneracy is considered.
On compactly supported rapid histories, `L` is formally self-adjoint for the
real history pairing.

Introduce one odd ghost `c` and define

```text
s_BRST g = c,       s_BRST p = 0,       s_BRST c = 0.         (4)
```

Then `s_BRST^2=0`, and the minimal classical BV action

```text
S_BV = S + integral_R <g*,c> dt                              (5)
```

satisfies the classical master equation: `S` is independent of `g`, the gauge
algebra is abelian and the ghost has zero BRST image. This is a complete
minimal free abelian BV control. It is not a gauge-fixed quantum BV theory,
does not supply a measure and has no source-owned nonlinear algebra.

## Closed realization, Green pair and boundary data

On the real history Hilbert space `L2(R;P)`, Fourier transformation in time
makes `L` multiplication by

```text
Omega^2 - xi^2.                                               (6)
```

The maximal multiplication domain—those transforms for which (6) times the
transform is square integrable—is a closed self-adjoint realization. The
algebraic tensor product of Schwartz time functions with finite sequences is
an invariant core; it sits in `Schwartz(R;s)` and is a core because compact
spectral cutoffs in `xi` and finite mode truncations approximate in the graph
norm. The operator is not claimed positive or boundedly invertible on history
space: its characteristic set is precisely why retarded and advanced inverses,
not a Hilbert inverse, are the relevant objects.

For `f in C_c^infinity(R;s)`, use K91's formulas

```text
(G_ret f)(t) =  integral_(-infinity)^t
                Omega^(-1) sin(Omega(t-u)) f(u) du,

(G_adv f)(t) = -integral_t^(infinity)
                Omega^(-1) sin(Omega(t-u)) f(u) du.           (7)
```

Modewise jump and integration-by-parts arguments give both left and right
test-space identities. Their temporal supports are opposite, and
`E=G_ret-G_adv` is antisymmetric. The variational Green boundary form is

```text
beta_t(p,h) = <p,partial_t h>_R - <partial_t p,h>_R,          (8)
```

whose endpoint difference is the integration-by-parts defect of `L`.

The model boundary family is

```text
B_r = Omega + r I,       0 <= r <= 1,       D(B_r)=D(Omega). (9)
```

It is self-adjoint on one common domain, has gap at least one and spectral flow
zero. This owns a global common-domain boundary spectral family for the model.
It is not a curved-spacetime boundary Dirac operator, APS theorem, families
index or source global object.

## Exact K91 bridge

Realification followed by complexification is identity on the displayed `G`
and `P` coordinates. Consequently the action's gauge map is K91's
`d0(alpha)=(alpha,0)`, the quotient is `q(g,p)=p`, the Euler operator is K91's
`L`, the spatial energy generator is `Omega`, the closed generator domain and
rapid core are unchanged, and the Green pair and boundary form use the same
pairing. All six K103 K91 bridge cells therefore close for this repository
action.

What closes is action ownership for K91 as an internal control. Source
authentication remains zero. The separate K155 test decides whether this same
frozen action reaches the hostile fixture.

## Inline postflight bookend

- **Strongest overclaim:** calling (1) a recovered GU action. Refused: it is
  constructed backward from K91's repository demands and earns no source or
  native certification credit.
- **Strongest contrary construction:** a nonlinear, curved or indefinite
  action may own the same quotient while differing outside K91's tested
  interface. Preserved; K91 does not select (1) uniquely among such extensions.
- **Weakest reproducibility seam:** finite mode checks cannot prove maximal
  multiplier closedness or core density. Those statements use the Fourier
  multiplication theorem and graph-norm cutoff argument above; the probe
  certifies only the exact formulas and fences.

The exact probe passes `24/24`; its baseline-first hostile selftest catches
`22/22` independent mutations. No source, K155, Born, prediction,
confirmation, canon or public-posture state moves.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  tests/channel-swings/k104_demand_derived_k91_action_bv_green_probe.py
PYTHONDONTWRITEBYTECODE=1 python3 \
  tests/channel-swings/k104_demand_derived_k91_action_bv_green_probe.py --selftest
```
