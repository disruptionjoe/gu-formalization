---
title: "K2040: Polynomial interaction thresholds from the conserved graph norm"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed classical graph action; no physical parity, quantum positivity or source selection
scripts:
  - tests/channel-swings/k2040_nonlinear_resonance_selection.py
  - tests/channel-swings/k2040_nonlinear_resonance_selection_probe.py
---

# K2040: Polynomial interaction thresholds from the conserved graph norm

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
result: complete polynomial resonance lattice and sharp interaction-degree thresholds
carrier: K2038 fixed real1408 observed graph LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: fixed positive Euclidean graph norm and invertible skew kinetic T ON=declared_graph
real_structure: real commuting classical coordinates, grouped into complex skew-frequency sectors
grading: even polynomial parity, explicitly not Grassmann parity
action_owner: repository-construction -- K2038 reduced action and its full variational extension
target: norm-preserving potential classification and conserved currents MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] In the fixed K2038 action, every even
polynomial potential of degree at most four that conserves the positive graph
norm separately conserves six sector norms. The first possible transfer between
these sectors is degree six. Three paired-sector norms remain separately
conserved for every polynomial of degree below eighty. Degree eighty is the
first possible transfer between those pairs. Both thresholds have explicit
nonzero dynamical witnesses. These restrictions follow from the actual
irrational kinetic frequencies, not from a chosen interaction ansatz.

## 1. Question and fixed object

[K2038](k2038-observed-action-compression-2026-10-24.md) gives

    D u + T^-1 grad V(u)=0,   D=partial_t + sum Cj partial_j,
    T^T=-T,  [T,Cj]=0,  Cj^T=Cj,
    positive norm conservation iff dV_u(T^-1 u)=0.       (1)

This asks what the backward demand for a conserved positive local norm
requires of the potential in that specified realization. It is not a new
GU action selection. Its full variational lift is already owned by K2038.

Use orthogonal skew normal coordinates with T_l=omega_l J_l and J_l acting
as multiplication by i. Let a=(sqrt(641)-19)/2, b=19+a. Then

    a*b=70,  a^2+19a-70=0,
    omega=(1,2,a,2a,b,2b),
    complex dimensions=(288,288,32,32,32,32).            (2)

These are K2038's six distinct positive frequencies. The Cj preserve every
spectral sector and commute with its J_l, since they commute with T. The
complex coordinates are an orthogonal presentation of real commuting fields;
they do not select a complex physical Hilbert space or a Grassmann reduction.

SC-OP-04 ASSERTS the candidate four-independent-field grammar. SC-OP-05 is
UNCERTAIN about a selected southeast rival. SC-META-53 is UNCERTAIN about
physical positivity; SC-META-56 DISAVOWS an odd-action prerequisite. Neither
that disavowal nor the four-field grammar selects this real-even construction.
LT-SM8/LT-GR6b, source register, physics ledger and canon are unchanged.

## 2. Complete integer resonance lattice

For a monomial in complex coordinates and their conjugates let k_l be its
number of unbarred factors minus barred factors in sector l, summed over all
coordinates in that sector. Equation (1) is equivalent, coefficient by
coefficient, to

    sum k_l/omega_l=0.                                (3)

To prove this, the infinitesimal rotation is diagonal on monomials, with
weight proportional to (3). Distinct monomials are linearly independent in
the complexified real polynomial algebra. Real potentials impose conjugate
coefficients, which does not allow a nonzero weight to cancel another
monomial's derivative. This handles arbitrary multiplicities, not just one
coordinate per sector. Constant terms are harmless.

In the rational basis (1,a), the six inverse frequencies are

    (140,0), (70,0), (38,2), (19,1), (0,2), (0,1),

all divided by 140. Irrationality follows from 25^2<641<26^2. Writing
h1=2k1+k2, h2=2k3+k4 and h3=2k5+k6, the two equations are

    70 h1+19 h2=0,  h2+h3=0.

As gcd(70,19)=1, the COMPLETE lattice is

    h1=19r, h2=-70r, h3=70r,   r integer.              (4)

For a monomial of degree d, d>=sum |k_l| and their difference is even.
For fixed 2x+y=h the minimum |x|+|y| is ceil(|h|/2): the triangle
inequality gives the lower bound and taking x nearest h/2 attains it.
Thus a resonance with r!=0 has degree at least

    ceil(19|r|/2)+70|r| >=80.                         (5)

For r=0 the lattice instead consists of

    k=(p,-2p,q,-2q,s,-2s).                            (6)

This classification is all-degree and exact; it does not extrapolate a
finite search.

## 3. Quartic rigidity, the sextic witness, and local currents

Even means V(-u)=V(u), an ordinary sign symmetry of commuting fields.
For r=0, sum |k|=3(|p|+|q|+|s|). A nonzero even-degree monomial has degree
at least six: a minimal cubic resonance is odd and adding balanced factors
changes degree by two. Consequently every even polynomial of degree at most
four satisfying (1) has k=0 in every monomial. It is invariant under six
independent phase rotations. Equivalently its quadratic terms are linear
combinations of within-sector bilinears z_l,i conjugate(z_l,j); its quartic
terms are products of two such bilinears, with the usual reality conditions.
Relations between these generators need not be free. Their count is not the
small scalar control census in the checker.

This does not prohibit quartic interactions: density-density and intra-sector
orientation interactions remain. It prohibits exchange of the six sector
norms. Since the fixed Cj preserve the spectral projectors P_l, every smooth
solution satisfies six separate continuity equations

    partial_t |P_l u|^2 + sum partial_j((P_l u)^T Cj P_l u)=0.  (7)

The potential source is zero because dV(T^-1 P_l u)=0. Integrated charges
are conserved on a periodic domain or with the corresponding vanishing flux.
This is stronger than the total current, but not six physical species.

Sharpness: choose one complex coordinate from sectors 1 and 2 and set

    V6=Re(z1^2 conjugate(z2)^4).

Its k=(2,-4,0,0,0,0) is resonant. For homogeneous flow at z1=1+i, z2=1,
the two norm derivatives are exactly (8,-8); hence the individual charges
really transfer. A merely nonzero polynomial would not prove this. The
probe differentiates the polynomial in real coordinates and uses the actual
inverse frequencies. The odd cubic Re(z1 conjugate(z2)^2) is a control:
it preserves the total norm but violates the stated even-potential condition.

## 4. Accidental pair conservation lasts through degree seventy-nine

Every resonant monomial of degree below eighty has r=0. Therefore V is
invariant under the three independent rotations with weights (2,1) on
sectors (1,2), (3,4), (5,6), respectively. On each pair this is proportional
to T^-1, so each paired Euclidean norm has its own local current by the same
calculation as (7). This is true even when V couples the pairs through
products of invariants. Pairwise invariance is not complete factorization.

The even degree-eighty polynomial

    V80=Re(z1^9 z2 conjugate(z3)^35 z5^35)

has k=(9,1,-35,0,35,0), realizes r=1, and proves the bound sharp. At z1=i
and all other displayed coordinates 1, its three paired norm derivatives are

    (19, -(19+a), a),

which sum to zero and are individually nonzero. Thus the extra three
currents are low-degree consequences, not all-order symmetries. There remain
the two exact torus weight symmetries from (3), but they are different from
three independent paired norms. No source or physical claim is made from
this arithmetic resonance at high degree.

## 5. Homogeneous completeness and its limit

For any globally defined C2 potential on R^1408 satisfying (1), the homogeneous vector field
-T^-1 grad V is locally Lipschitz and tangent to each Euclidean sphere.
Every initial orbit stays in a compact sphere; its vector field and local
Lipschitz constant are bounded on a surrounding compact ball. The local
existence theorem can therefore be continued for all positive and negative
times. This applies in particular to both polynomial witnesses, regardless
of whether V is bounded below on the full vector space.

This finite-dimensional completeness does not control spatial derivatives
of the PDE, establish global PDE existence, or contradict K2038's unbounded
homogeneous tangent amplification. A conserved field norm and stability of
the solution map are separate properties.

## 6. Reproduction, hostile review, and next question

Run the producer and probe listed above. The producer checks the integer
lattice through degree six and the sharp pair cost; the distinct probe uses
exact rational arithmetic in Q[a] and enumerates all scalar exponent tuples
at degrees 2,4,6. It finds 6,21,74 invariant scalar monomials; those are
control counts, not dimensions for the full multiplicities. It differentiates
both transfer witnesses directly. The all-degree proof is (4)-(6), not the
finite census. K2038's full raw compression is pinned reuse, not newly rerun.

Four clean-baseline faults cover a changed frequency, a nonresonant witness,
and two false degree thresholds. The last two check reporting against the
proved thresholds; they are not independent proof of the thresholds.
The strongest counterexample to an all-order pair symmetry is V80 itself.
The strongest scope risk is treating the real one-field reduction as source
fermions; that bridge remains absent. Same-author distinct implementations
and hostile reasoning do not constitute external review, proof-assistant
certification, or a novelty claim.

The next substantial source-facing input is an actual field/parity and
observation bridge. For this fixed mathematical model, a global PDE domain
or the stability of a specified sextic interaction is a substantive next
question. Repeating quartic coefficient searches for sector transfer is
eliminated by the complete lattice argument.
