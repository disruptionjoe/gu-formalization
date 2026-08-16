---
title: "Selected-K114 RSAP TT alpha normalization-invariant owner gate"
status: superseded_by_k116
doc_type: exact_commutator_invariant_and_structure_preserving_field_redefinition_classification
created: "2026-08-15"
registry: lab/process/selected-k114-rsap-tt-alpha-normalization-invariant-owner-gate.json
probe: tests/channel-swings/selected_k114_rsap_tt_alpha_normalization_invariant_owner_gate_probe.py
grade: "THE K113 alpha_II=1 ZERO-TRANSPORT LOCUS IS NOT A FIELD-NORMALIZATION ARTIFACT. IT IS THE EXACT SIMILARITY-INVARIANT COMMUTING LOCUS OF THE FREE AND INTERACTION DYNAMICS. EVERY LINEAR FIELD CHANGE PRESERVING THE RECORDED FREE-MASS BLOCK, INTERACTION RAY AND KINETIC PENCIL SENDS alpha_II ONLY TO alpha_II OR 2-alpha_II; alpha_II=1 IS A FIXED POINT AND CANNOT BE REACHED FROM alpha_II!=1. THE COEFFICIENT RELATION IS GENUINE BUT REMAINS ACTION-UNSELECTED."
target_claim: K113_NEXT_GATE__alpha_II_ONE_MAY_BE_A_FIELD_NORMALIZATION_RATHER_THAN_A_GENUINE_ACTION_COEFFICIENT_CONDITION
target_verdict: NORMALIZATION_HORN_EXCLUDED__ZERO_TRANSPORT_IS_THE_INVARIANT_FREE_INTERACTION_ALIGNMENT_LOCUS__GENUINE_BUT_ACTION_UNSELECTED
canon_verdict_change: none
---

# Selected-K114 RSAP TT alpha normalization-invariant owner gate

> **K116 FRAME-CONSISTENCY CORRECTION (2026-08-15):** this result is
> superseded in full. The commutator below used raw-frame `K,M0` with an
> eigenmode-frame interaction block. For the consistent action-owned pencil,
> `[L0,L1]=b[[1,0],[-alpha,-1]]`, which has rank two for every `alpha` when
> `b!=0`; no `alpha=1` commuting or zero-transport locus exists.

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> Krein, observed-defect and RSAP/BFV action-owner question. Ordinary
> Higgs/VEV, family-index, net-chirality, anomaly, symmetry-breaking and
> familiar four-dimensional gauge-model conclusions do not adjudicate it.
> Read `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

## Result in plain English

K113 found that the moving TT transport disappears when `alpha_II=1`, but
left open whether that number was only a field convention. It is not.

Split the TT dynamics into its free mass part and its interaction part:

```text
L_0=K^-1 M_0,             L_1=K^-1 vv^T,
K=[[alpha,1],[1,0]],      M_0=[[0,0],[0,b]],      v=(1,1).
```

Their exact commutator is

```text
[L_0,L_1]=b(alpha-1)G,
G=[[-1,0],[alpha,1]].                         (1)
```

For `b!=0`, the two pieces commute if and only if `alpha=1`. Under every
invertible linear field change, both dynamics transform by the same
similarity and their commutator transforms by conjugation. Its vanishing,
rank and similarity class cannot change. Thus `alpha_II=1` means something
coordinate-free: the free and interaction dynamics share fixed spectral
directions. That is exactly why K113's moving spectral connection vanishes.

The strongest structure-preserving redefinition check agrees. If a field
change preserves the free distortion-only mass block, the interaction ray and
the recorded kinetic-pencil form, then it can send

```text
alpha -> alpha              or              alpha -> 2-alpha.       (2)
```

The point `alpha=1` is fixed by both branches. No `alpha!=1` pencil is
equivalent to it. So this is a genuine codimension-one action-coefficient
condition, not a normalization freedom. The repository still has no source or
action equation selecting that condition: `alpha_II` remains the live
coefficient `U7`, with only positivity used in this TT branch.

## 1. Layer-0 owner packet

```text
carrier:       real two-field observed TT fluctuation q
pairing/form:  K(alpha)=[[alpha,1],[1,0]], Krein signature (1,1)
real structure: ordinary real two-component field
grading:       K113 spectral +/- grading C(u)
action owner:  recorded TT quadratic pencil; alpha_II is charged U7
target:        decide whether the alpha_II=1 zero-transport locus is coordinate
               normalization or an invariant action-coefficient relation
assumptions:   b!=0; invertible linear field changes; gapped K113 component
controls:      arbitrary congruence/similarity changes and the narrower
               transformations preserving M_0, the ray Rv and K's normal form
claim ceiling: exact finite-dimensional pencil classification only
```

No standard Higgs, family-index or chirality comparator enters the
calculation.

## 2. The invariant test

Write

```text
M(u)=M_0+u vv^T,
L(u)=L_0+uL_1.
```

Exact multiplication gives

```text
L_0=[[0,b],[0,-alpha b]],
L_1=[[1,1],[1-alpha,1-alpha]],
[L_0,L_1]=b(alpha-1)G.                (3)
```

Because `G^2=I`, `G` is invertible. Hence, for the nonzero free coefficient
`b`,

```text
[L_0,L_1]=0  <=>  alpha=1.            (4)
```

For a field change `q=S r`,

```text
K'=S^T K S,       M_i'=S^T M_i S,
L_i'=(K')^-1 M_i'=S^-1 L_i S,
[L_0',L_1']=S^-1[L_0,L_1]S.           (5)
```

Equation (5) is the decisive point. Even a completely arbitrary invertible
field redefinition cannot turn a noncommuting free/interaction pair into a
commuting pair. It may hide the literal coefficient name `alpha`, but it
cannot create K113's constant spectral grading.

## 3. Full classification inside the recorded TT normalization

Now require more: after an overall nonzero action rescaling, retain all three
recorded structural features.

1. `M_0` has only a lower-right distortion entry.
2. The interaction remains the rank-one ray generated by `v=(1,1)`.
3. The kinetic form remains `K(alpha')=[[alpha',1],[1,0]]`.

Let

```text
S=[[a,c],[d,e]].
```

Preserving the free mass kernel gives `d=0`. Preserving the interaction ray
gives `S^T v=s v`, hence `s=a` and `c=a-e`. The lower-right entry of
`S^TKS` is then

```text
c(alpha c+2e).
```

It vanishes in exactly two branches.

### Branch A: `c=0`

Then `e=a`, and after removing the common action scale,

```text
alpha'=alpha.                          (6)
```

### Branch B: `alpha c+2e=0`

For `alpha!=2`,

```text
e=alpha a/(alpha-2),
c=2a/(2-alpha),
alpha'=2-alpha.                        (7)
```

The other normalized coefficients transform as

```text
b'=alpha b/(2-alpha),
u'=(2-alpha)u/alpha,
alpha'b'=alpha b.                      (8)
```

If positive `alpha'` and a positive overall action scale are retained, Branch
B is admissible only for `0<alpha<2`. This restriction is not needed for the
main conclusion: on every admissible branch,

```text
alpha'=1  <=>  alpha=1.                (9)
```

The structural orbit of `alpha` is therefore at most `{alpha,2-alpha}`. The
zero-transport point is its own fixed orbit.

## 4. What the number means—and what it does not mean

The invariant content is not the naked decimal `1`. It is

```text
free dynamics commutes with interaction dynamics
<=> the spectral eigendirections do not rotate with u
<=> K113 transport is identically trivial.            (10)
```

The fixed TT conventions—unit cross kinetic entry and interaction ray
`v=(1,1)`—write that invariant relation as `alpha_II=1`. Arbitrary coordinates
can obscure that literal equation, but cannot change (10).

This also distinguishes a **genuine condition** from a **selected condition**.
The source/action coefficient census records `alpha_II` and
`beta_0/alpha_II` as the live charged unknown `U7`. The present TT work uses
`alpha_II>0`; it has not derived `alpha_II=1` from an Euler equation, symmetry,
normalization clause or source statement. K114 excludes the convention horn.
It does not promote the surviving coefficient relation to physical truth.

## 5. Reverse-scaffold disposition

```text
alpha_II=1 as removable field normalization:          EXCLUDED
zero transport as invariant free/interaction alignment: EXACT
structure-preserving alpha orbit:                      {alpha,2-alpha}
alpha_II=1 action/source selection:                    NO CURRENT WITNESS
K113 exact Jacobian target for generic alpha:          RETAINED
K112 minimal variational owner:                        RECONSTRUCTION GRADE
boundary/cohomological 2D-to-98D attachment:           OPEN
stationary moving background and closed domain:        OPEN
```

Keep Variancer's reverse classical RSAP/BFV scaffold. The normalization detour
is closed. For generic `alpha_II!=1`, the next useful swing is now a direct
source/action moving-TT Jacobian audit against K113's exact transport. The
alternative reopener is new source geometry or an action equation that
actually selects the commuting locus; a field rescaling is not enough.

## Claim ceiling

This is a repository-derived exact classification of the observed two-field
TT pencil. It is not source-confirmed coefficient selection, a completed
full-action derivation, a stationary solution, a bulk BV master action, a
closed positive quantum domain, a `98D` attachment or physical cohomology. It
does not prove `alpha_II=1`, `H-Q*` or `H0`.

No ledger, datum, quotient booking, canon, public posture, particle,
phenomenology or GU truth-status claim changes. Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k114_rsap_tt_alpha_normalization_invariant_owner_gate_probe.py
```

## Successor closure (K115)

K115 classifies the generic-alpha owner target completely. Every local
invertible moving frame inducing K113 is, up to one constant frame,
`exp((phi-phi0)G)`; the corresponding parallel transport is its inverse. The
moving factor is `K`-orthogonal and determinant one, has fixed `G` eigenlines,
and carries the exact reciprocal stretch fixed by the K113 cross-ratio. For
generic `alpha_II!=1`, that stretch diverges at either simple spectral gap
wall, excluding a bounded invertible same-frame extension but not patched or
singular theories. The current serialized source/action custody supplies no
typed TT map meeting this fingerprint, so the adapter remains reconstruction
grade and requires genuinely new owner evidence.
