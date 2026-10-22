---
title: "K1939: Physical catalyst dimension and the two-support energy frontier"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: independent conditional mathematics; no native GU, novelty, external acceptance or formal proof
scripts:
  - tests/channel-swings/k1939_physical_catalyst_resource_frontier.py
  - tests/channel-swings/k1939_physical_catalyst_resource_frontier_probe.py
---

# K1939: Physical catalyst dimension and the two-support energy frontier

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
result: sharp physical dimension and exact energy-constrained return with at most two occupied energies
carrier: four-state system, four-level Gibbs bath, finite nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace and worst-input half trace norm ON=independent_initial_registers
real_structure: complex adjoint and covariant energy pinching
grading: additive energy shells; no source chirality
action_owner: repository-construction -- exact conserving joint unitary
target: physical dimension and mean-energy constrained full-channel simulation MAP-TYPE=intertwiner
```

## 1. Distinct physical resources

Fix precisely [K1935](k1935-arbitrary-support-thermal-return-2026-10-22.md)'s
extreme four-state Schur channel C_jk=<v_k,v_j>, with
v1=(1,0), v2=(0,1), v3=(1,1)/sqrt2, v4=(1,i)/sqrt2.
The bath energies are b Delta, b=0,1,2,3, and its faithful Gibbs weights
are t^b/Z, 0<t<1. The system Hamiltonian is diagonal, and all registers
start independently. The catalyst spectrum is finite, nondegenerate,
nonnegative and has ground0. Mean energies below are in units Delta.

N means the number of positive diagonal catalyst populations after energy
pinching, D the FULL physical catalyst dimension, and r the worst-system-input
marginal half trace distance. Coherent preparation is permitted: K1933's
covariant pinching comparison preserves energy and does not increase r.
This comparison does not physically dephase a supplied catalyst for free.

Two results follow:

1. Exact implementation with N occupied energies requires D>=2N+1, and
   this minimum is attained for every N.
2. For N<=2, the optimal r under a mean-energy budget E is an explicit
   finite minimum of rational piecewise-linear functions, including optimal
   choices of actual energy separation, offset, preparation and conserving
   unitary. It is not the unrestricted-N energy optimum.

These are different from K1937's occupied-support optimum. Dimension,
occupied support, coherent state rank and energy are not interchangeable.
Neither result establishes product return, reusable catalysis or local control.

## 2. Sharp dimension: count physical shell slack

In a physical bath/catalyst shell e let k_e count all basis states and n_e
count initially occupied states. Extreme-Gram polarization gives
2 n_e<=k_e, as proved in K1935 section2. Summing over ALL shells gives

    8N <= 4D, so D>=2N.

Equality would force equality in every shell. But the lowest total-energy
shell consists solely of bath ground and catalyst ground, so k_0=1 while
2n_0 is either0 or2. Equality is impossible. Therefore D>=2N+1.
This proof uses nondegeneracy and a finite spectrum; it is not continuous
in degeneracy or applicable to an infinite catalyst by dimension counting.

For attainment take A={0,1,...,2N}, with occupied odd levels
S={1,3,...,2N-1}. Every shell has at least twice as many physical positions
as occupied inputs. In the interior two occupied inputs have four positions;
incomplete edge shells have one occupied input and at least two positions.
Assign orthogonal copies of the two-component vectors Wv_j to the occupied
inputs and complete their orthogonal companions on unused input columns,
where W=[[1,1],[1,-1]]/sqrt2. This is a full unitary on EACH actual shell,
not an isometry relying on a hidden pure ancilla. The controlled direct sum
implements every matrix unit of the target channel and conserves energy.
Any positive weights on S work for channel exactness.

For K1937's attaining consecutive-odd rooted weights, choose the same output
pairs as there. Only singleton edge shells change size; their two required
positions remain available. Its all-input return formula and optimum on that
fixed support are preserved, now on D=2N+1 instead of an overpadded ladder.
This does NOT say every globally optimal arbitrary-gap N-site architecture
fits the dimension minimum. The warm-temperature adjacent-gap N=2 example
already needs more shell-completion states than the odd two-site support.

## 3. Exact return at any two-support preparation

Let the two occupied levels be a and a+d, with lower weight x and upper
weight1-x. Resonance requires d in{1,2,3}; nonresonant or d>=4 supports
have the singleton lower bound1/2 and cannot beat a single occupied level.
Set

    L=(1+...+t^(3-d))/Z, H=t^d L,
    h=max(Hx,L(1-x)),
    r_d(x)=([(1+H)x-h]_+ + [(1+L)(1-x)-h]_+)/2.       (1)

This is the SHARP worst-input return, after supplying the necessary empty
shell levels. For the lower bound use rho12=(|1><1|+|2><2|)/2. Its shell
output eigenvalues are each occupied input weight divided by2, repeated
twice. Rank-one support projections therefore give

    a_low <= ((1-H)x+h)/2,
    a_high <= ((1-L)(1-x)+h)/2.

Support measurement bounds trace distance below by the sum of positive
deficits, exactly (1). There is no assumption that a general optimizing
unitary is controlled on unused environment states.

For the upper construction, in each shared shell send the heavier input's
Wv_j to the two occupied-support output positions, its own position first;
send the lighter input to the two empty positions. In singleton shells use
its own position first and an empty one second. Complete the orthogonal
columns. The basis-input first-coordinate probabilities are c_j=1/2,1/2,1,1/2.
At c=1/2 both population bounds above are attained. At c=1, the return is
Hx in the upper-heavy case or L(1-x) in the lower-heavy case. Both are no
larger than (1). For example in the upper-heavy region x<=L/(L+H),

    r_d(x)=(1-x)/2 + [(1+L+H)x-L]_+/2;

split at x=L/(1+L+H) to check Hx<=r_d(x). The reversed case is the same
calculation with L,H and the sites exchanged. Output populations depend
affinely on c, so trace-distance convexity proves the bound throughout
[1/2,1]. Tracing the controlled system removes input coherences. This proves
ALL-input attainment, including arbitrary system states entangled with an
external reference when only the catalyst marginal is tested.

## 4. Minimum offsets and energy-budget algorithm

An occupied lowest level must satisfy a>=1: its bath-ground input needs a
second state in the same shell, necessarily a lower catalyst level by at
least Delta. For gap d, the first shared shell at a+d has two occupied
inputs, so all four bath positions must exist. Its lowest catalyst position
is a+d-3; hence a>=3-d. The exact minimum is therefore

    a_d=max(1,3-d).                                         (2)

A finite full ladder from0 to a_d+d+3 supplies every needed state. Empty
padding has zero preparation weight and does not change mean energy. Thus
(2) is sufficient as well as necessary. With at most two occupied energies,
no exact realization exists at E<1. At E>=1 a pure catalyst at energy1 on
three physical levels has return1/2.

For each d with E>=a_d, minimize (1) on

    x in [max(0,1-(E-a_d)/d),1].                            (3)

The only possible interior breakpoints are

    x_L=L/(1+L+H), x_c=L/(L+H), x_R=(1+L)/(1+L+H).

Evaluate (1) at those in (3), at both endpoints, and include the singleton
value1/2. Their minimum is the GLOBAL optimum over arbitrary finite
nondegenerate spectra, all preparations with at most two occupied energies,
and all conserving implementations in this model. No sampling is used for
this minimization: (1) is piecewise linear and (2) accounts for the energy
origin. Endpoints x=0,1 are singletons; the actual singleton at energy1 is
always available and prevents unnecessary offset cost.

For t=1/2 the exact resource decisions include:

| E | minimum r | an attaining preparation |
|---|---|---|
| 1 | 1/2 | pure occupied level1 |
| 11/10 | 19/40 | levels1,3; weights19/20,1/20 |
| 6/5 | 9/20 | levels1,3; weights9/10,1/10 |
| 8/5 | 9/20 | same preparation, unused energy slack |
| 2 | 7/20 | levels1,3; equal weights |
| 11/5 | 3/10 | levels1,3; weights2/5,3/5 |

A flat section followed by renewed decrease is permitted: fixing at most
two occupied energies is not a convex class under arbitrary flagged mixtures
of implementations. Additional flags or support levels change the problem.
The optimizer explicitly compares all three resonant gaps, including the
warm-temperature adjacent-gap advantage; it does not fix gap2 universally.

## 5. Released physical-dimension return decisions

The dimension theorem and K1937 together imply that for D>=3, with
n=floor((D-1)/2), the best achievable return satisfies

    R_n_global(t) <= r_D(t) <= R_n_odd(t).

The lower is K1937's optimizer over all n-site paths; smaller support cannot
improve it. The upper uses the dimension-minimal odd ladder with its optimal
rooted weights. An extra empty far-separated level embeds an odd-D witness
into even dimension without changing energy conservation or return. These
bounds do not assert equality for general D.

For small dimensions, actual shell completion closes the gap:

- D<3: no exact implementation.
- D=3 or4: r_D=1/2, since N<=1.
- D=5: r_D=R2=(1+2t^2)/(4(1+t^2)).
- D=6: r_D=min(R1,R2), where
  R1=(1+2t+2t^2+2t^3)/(2(1+t)(2+t+2t^2)).

For two occupied energies, gap1 needs the six distinct positions from a-2
through a+3: its three shared shells must all have four physical positions.
Gap3 has four shared-shell positions a through a+3, but the lowest and
highest singleton-input shells require one additional position below a and
one above a+3. Gap2 needs five positions a-1 through a+3, and those already
satisfy every edge shell. These counts are attained by ladders with offsets
2,1,1 for gaps1,2,3 respectively. Gap3's unconstrained optimum is worse than
gap2 (K1935); nonresonance gives1/2. Hence the claims above cover arbitrary
nondegenerate spectra, not just chosen ladders. At t=3/4, D5 has return17/50
while D6 improves to143/434. This is an explicit benefit of an EMPTY physical
level without increasing the two occupied populations.

## 6. Verification, contrary cases and remaining scope

The producer checks full complex Gram matrices, actual edge-shell dimensions,
unitarity, probability, and all-input return at nonoptimal weights. The
separate probe enumerates physical spectra/supports, reconstructs support
bounds directly from bath weights, and compares the finite budget optimizer
against rational preparations. Analytic arguments carry universal scope;
finite enumeration is a hostile control, not its proof. Empty-level removal,
complex-phase conjugation and a wrong return normalization are detected only
after a green baseline. Report/pin controls are separate consistency checks.

Strongest overclaims rejected: unrestricted-N energy optimality, dimension
optimality of every arbitrary-gap return optimizer, physical repeatability,
and continuity through a degenerate spectrum. Weakest seams are ground-energy
offset, incomplete edge shells, and the all-input inequality; all are explicit.
No new source or physics-ledger verdict follows. SC-META-53 remains UNCERTAIN;
LT-SM8/LT-GR6b/AC-F1 still need native paired domain/observable constructions.
[Ng et al.](https://arxiv.org/abs/1405.3039) already study dimension/mean-energy
restrictions on thermal catalysis. The present target-specific resource
calculation is not claimed novel or externally verified. Reproduce with
Python3/SymPy1.14 and both frontmatter scripts; producer --write regenerates
its rational report. No source-register, ledger or canon changes.
