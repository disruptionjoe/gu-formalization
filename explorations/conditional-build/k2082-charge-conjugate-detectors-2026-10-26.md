---
title: "K2082: A real-compatible paired particle/hole detector"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no GU verdict, novelty or external certification
scripts:
  - tests/channel-swings/k2082_charge_conjugate_detectors.py
  - tests/channel-swings/k2082_charge_conjugate_detectors_probe.py
---

# K2082: A real-compatible paired particle/hole detector

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
result: single-mode half-noise boundary and invariant paired detector with finite excitation energy
carrier: complexified real1408 massive graph and imported sea CAR LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: fixed Pstar Hilbert metric normalized by its real square root ON=declared_observed_graph
real_structure: K involution and inherited b=-iJ K anti-involution; neither source-selected
grading: energy signs and fermion parity, distinct from source grading
action_owner: repository-construction -- K2058 changed coefficient dynamics and CAR completion
target: charge conjugation, positive click effect and free measurement energy MAP-TYPE=intertwiner
```

## 1. Freeze the actual map before imposing reality

[Conditional mathematical result; accepted after independent internal specialist review. No external or proof-assistant certification.]
K2056 already constructs a local degree-dual successor and proves that demanding
both the positive kinetic coefficient and a SAME-COORDINATE square-plus-one bar
fails. It supplies a square-minus-one anti-involution instead. K2021 already
constructs local R0/R1; the missing input is source selection and a physical bridge,
not existence of any local degree-dual map. Here compose the inherited map with
K2080's detector, without changing that earlier obstruction.

After the real Pstar^(1/2) isometry, K2060's real coefficient form is
H=-i(sum C_j partial_j+mM), m>0, domain H1. Ordinary conjugation K satisfies
KHK=-H. Because K also conjugates i, K U(t) K=U(t), not U(-t).
For normalized f and any pointwise antiunitary C with CHC^-1=-H,

    C P C^-1=Q,  C Q C^-1=P,  nu(Cf)=1-nu(f),         (1)

where P,Q are the positive/negative energy projectors and nu(f)=<f,Qf>.
A normalized C-real mode (even up to phase) has nu=1/2. In fact
|<f,Cf>|<=2sqrt(nu(1-nu)), by splitting both vectors into energy signs and
Cauchy-Schwarz. Thus ||f-Cf||^2>=2-4sqrt(nu(1-nu)). A small-noise mode is not
approximately real in this sense. Conversely a sign-plus antiunitary preserves
P,Q and reverses time;(1) does not apply to it. No sign-free no-go is asserted.

The linear particle-hole CAR automorphism is alpha_C(a(f))=a*(Cf), with
annihilation antilinear. It preserves CAR, support, free dynamics and the sea state,
and sends n_f to I-n_Cf. The different number-preserving conjugate-linear map
must not be substituted: it exchanges the sea with its complement. For C^2=I,
alpha_C is an involution; for C^2=-I its square is fermion parity, hence it is
still involutive on every even observable. A single C-real mode exchanges click
labels. That statement does not exclude invariant multi-mode instruments.

## 2. Paired repair with fixed click label

Choose smooth compact normalized f with f perpendicular to Cf and vanishing
sea cross covariance. Put n=n_f, h=I-n_Cf and

    E=n+h-nh=I-(I-n)(I-h).                            (2)

The two number projections commute. E is an even local projection. If C^2=+I
or-I, alpha_C exchanges n,h and fixes E. The complete binary Lueders instrument
{E,I-E} therefore has fixed outcome labels and commutes with remote even
observables. Both outcomes are kept. It is not identical to resolving n,h
separately and forgetting their records; that refined measurement destroys extra
coherence inside E's range.

An explicit plus-square example uses C=K and f=g tensor v with
v=(e1+i e2)/sqrt2 in an unused real multiplicity pair. Since v perpendicular
bar(v), both ordinary and Q cross products vanish. In the sea the two defect
occupations n,h are independent Bernoulli variables of parameter nu, so

    p_vac=2nu-nu^2.                                   (3)

For the positive-energy electron psi tensor v, put a=<g,psi>. K2080's compact
cutoff construction gives nu<=tau^2 and |a|^2>=1-tau^2. The second defect
occupation stays independent and unchanged, yielding

    p_e=2nu-nu^2+(1-nu)|a|^2,
    1-p_e=(1-nu)(1-nu-|a|^2)<=tau^2.                  (4)

Thus vacuum click <=2tau^2 and false negative <=tau^2 coexist with an invariant
positive click effect. No vacuum subtraction is used. The hole signal is related
by alpha_C. Exact vacuum silence remains unavailable for a nonzero compact f.

## 3. Compose with the actual kinetic anti-involution

K2056/K2058 give b=-iJ K, J=T^-1 Pstar, J real skew orthogonal, J^2=-I, commuting
with C_j and M. Thus b is antiunitary in the same fixed metric, bHb^-1=-H and
b^2=-I. Its absence of nonzero fixed vectors is preserved. Nevertheless

    alpha_b(n_f)=I-n_bf, alpha_b(I-n_bf)=n_(b^2 f)=n_f,

so(2) is invariant. In the real Clifford decomposition R4 tensor R352, J acts
on multiplicity. Choose a real unit vector e and its orthogonal partner Je,
f=g tensor e and bf=-i bar(g) tensor Je. This supplies exactly the diagonal
cross covariance used in(3)--(4). Therefore the detector is compatible with the
inherited positive-kinetic anti-involution, not merely an unrelated K convention.
No new metric is fitted. The source's four independent fields remain independent
until an actual identification is selected. This is not a source-real physical
quotient, source quantization or an evasion of K2056's square-plus-one theorem.

## 4. Coarse measurement energy

Let G>=0 be the imported free sea excitation generator, G Omega=0. For f in H1,
the bounded CAR derivation gives ||[G,n_f]||<=2||Hf||. This follows by the product
rule and ||a(f)||=||f||; it also gives domain preservation on Dom G. The same holds
for Cf because C preserves the graph norm. From(2),

    [G,E]=[G,n](I-h)+(I-n)[G,h],
    ||[G,E]||<=4||Hf||.

For the complete coarse binary channel the vacuum excitation energy is

    E_exc=2<E Omega,G E Omega>
         <=8||Hf|| sqrt(2nu-nu^2)
         <=8sqrt2 ||Hf|| tau.                         (5)

The first equality uses G Omega=0; the bound uses
||E Omega||=sqrt(p_vac) and ||G E Omega||=||[G,E]Omega||.
K2080's smooth cutoff estimate for ||Hf|| applies. At tau<1/500 and
||Hf||<201m/100, a simple rational bound sqrt2<3/2 gives E_exc<603m/12500.
This bounds free postmeasurement excitation, not apparatus work or energy.
K2081's finite-time/readout requirements still apply; algebraic invariance does
not implement the measurement.

## 5. Follow-through: paired causal witness and finite-graph repair

The paired construction does not evade K2081's causal demand. In the explicit
orthogonal multiplicity pair, occupy Cf as a spectator so h=0. Take Alice's
h_A,h'_A and Bob's g_B entirely in f's multiplicity sector. They commute with
n_Cf, and the even Alice swap preserves its occupation. On this invariant finite
mode sector E=n_f. The normal-state witnesses, record difference |alpha|^2 and
channel difference2|alpha|^2|beta|^2 of K2081 therefore apply to E as well. This
is an explicit witness transfer, not an inference from similar-looking effects.
It is still an all-state limitation; it does not exclude accuracy on a prepared
restricted class.

A finite connected graph also admits a coherent coarse apparatus. Choose a leaf
r of a spanning tree. Funnel f to r by K2081's rotations. The transformed Cf is
orthogonal to r, hence lives on the remaining connected tree; funnel it to the
neighbor of r using only that tree. At most(N-1)+(N-2)=2N-3 two-site rotations
suffice. Now E is a two-neighbor occupation/hole OR projection. A local pointer
controlled by that projection, followed by reversal of both funnels, gives the
COARSE Kraus operators E,I-E exactly. Measuring the two occupations separately
would instead give the refined instrument. Forward-plus-reverse mixing takes
at most pi(2N-3)/J, plus phase and two-site pointer times. This is a finite circuit
existence statement; it does not supply a continuum light cone or bounded
continuum resource limit.

## 6. Evidence and next condition

The independent probe uses four explicit CAR modes, filled sea, added electron,
particle-hole automorphism with square parity, exact OR/noise formulas, coarse versus
refined channel comparison, and an excitation-energy control. Six faults change
the hole effect, formulas, antilinear square or energy bound. These finite identities
support the written continuum CAR/domain argument; they are not a source or
proof-assistant certificate. The inherited map and Clifford decomposition are reused
from K2056/58/60 with their exact scope.

SC-OP-04 ASSERTS candidate four-independent-field grammar; OP-05 and META-53 remain
UNCERTAIN; META-56 DISAVOWS an odd-action prerequisite. LT-SM8/GR6b and all source,
physics-ledger and canon verdicts are unchanged. Source selection, interacting
quotient, actual preparation and point-local apparatus remain separate obligations.
The next constructive question is a causal instrument for this paired effect with
uniformly controlled continuum resources; a single-real-mode half-noise slogan is
no longer a candidate exclusion of this repaired detector.
