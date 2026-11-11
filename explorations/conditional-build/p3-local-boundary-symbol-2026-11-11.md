---
title: "Local boundary data must match the actual chiral symbol"
status: exploration
doc_type: structural-result
created: '2026-11-11'
program_target: P3xdomain_boundary
tier: T2
expected_delta: "Constrain the declared structural boundary category without a full-C decision"
actual_delta: "Constrained: the incoming symbol bundle imposes a signed RS/Weyl balance on classical complex-linear local boundary data; APS data are a different category."
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Local boundary data must match the actual chiral symbol

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: P3xdomain_boundary
tier: T2
expected_delta: Constrain the declared structural boundary category without a full-C decision
actual_delta: Constrained: the incoming symbol bundle imposes a signed RS/Weyl balance on classical complex-linear local boundary data; APS data are a different category.

```gu-typed-objects
result: chiral local boundary symbol balance
carrier: complex chiral spinors and geometric gamma-traceless vector-spinors on a Riemannian spin manifold of even dimension n>=4 LAYER=UNTYPED CHIRALITY=S-FULL-DIRAC
pairing: positive auxiliary spinor Hermitian metric ON=declared_carrier
real_structure: complex-linear symbol category; no K77/K95 real-structure transport
grading: fixed spin chirality; gamma trace reverses it; no physical chirality identification
action_owner: N/A -- structural requirements on symbols, no action construction
target: local boundary symbol realization MAP-TYPE=restriction
```

## 1. Question, source boundary and prior results

The observed chirality and count demands require a well-defined graded domain.
Local bulk equations do not decide whether that domain can be given by local
boundary conditions. We test this implication for the entire structural category
whose elliptic principal symbol is homotopic to a sum of geometric RS and Weyl
symbols, keeping the chiral grading. This is a condition on any putative member
of that category, not a claim that an action in C realizes it.

SC-CHI-01/51 ASSERTS the nonchiral-total/effectively-chiral claims with their
source qualifications; SC-GEN-02/03/54 ASSERTS the native 2+1/graded-extension
claims. An ordinary chiral elliptic index is not their physical observable.
RA-F1, AC-F1 and LT-SM8 remain NEEDS. C already allows APS-type data: nonlocal
boundary conditions do not turn a local bulk action into a nonlocal action.
No source, ledger, class declaration or canon conclusion changes.

The [supported fibre result](p3-metric-fibre-supported-index-2026-11-11.md)
computed supported classes and distinguished raw RS from ghost-subtracted
symbols. The [spectral-family result](p3-equivariant-spectral-sections-2026-11-11.md)
tested global continuous spectral sections. Neither computes the local
incoming-symbol obstruction below. The proof uses classical boundary-symbol
calculus, as presented in [Epstein, §6](https://www.fieldsinstitute.ca/programs/scientific/06-07/ISAAC/epstein.pdf).
The standard RS block decomposition and its elliptic homotopy are also described
in [Bär–Mazzeo, §2 and Remark 2.3](https://link.springer.com/article/10.1007/s00220-021-04030-0).
The following pointwise argument spells out why no Einstein assumption or
numerical index equality is needed for the symbol transfer.

## 2. Actual RS symbol, including its homotopy

Use Hermitian Clifford matrices gamma_i gamma_j+gamma_j gamma_i=2 delta_ij.
On V_C tensor S set G(v)=sum gamma_i v_i, so GG*=nI. Let T=G*/sqrt(n),
P=I-TT*, and C(xi)=I_V tensor gamma(xi). In the trace/ker G decomposition,

    C = [ A  B ]       A=((2-n)/n) gamma(xi),
        [ B* Q ]      Q=P C P restricted to ker G.

These equations follow from sum gamma_i gamma(xi) gamma_i=(2-n)gamma(xi).
Writing q=|xi|² and a=(2-n)/n, C²=qI gives

    A²=a²qI, BB*=(1-a²)qI,
    AB+BQ=0, Q²+B*B=qI.

The nonzero eigenvalues of B*B equal those of BB*, hence Q² is qI on ker B
and a²qI on im B*. For xi nonzero and n>2, both are positive. In particular
Q is elliptic. This also explicitly exhibits why Q is not a Dirac-type
symbol: both q and a²q occur, not a single Clifford square.

Scale the off-diagonal blocks by real t in [0,1]. The square of C_t has zero
off-diagonal blocks and diagonal blocks A²+t²BB* and Q²+t²B*B, bounded below
by a²qI. This is an elliptic symbol homotopy on every punctured cotangent
fibre, not a homotopy through actual actions or through normalized Dirac types.
The trace embedding reverses chirality. Thus the trace block represents
D with opposite grading, whose symbol class is -[D]. Multiplying its symbol
by a nonzero complex scalar does not change that class. Additivity yields

    [C]=[T_C M][D]=-[D]+[Q],
    [Q]=([T_C M]+1)[D].

The +1 is not inferred from the rank of ker G. Ghost subtraction requires its
own complete gauge complex and is not inserted here. Lower-order connections,
curvature, potentials and zero-order couplings do not alter this homotopy.
Principal couplings are covered only when they admit the stated elliptic
homotopy; arbitrary coupled class-C symbols are not classified by this argument.

## 3. Boundary bundle and the exact necessary balance

At a boundary point y, freeze the principal symbol. For each nonzero tangential
covector eta, solve the normal half-line symbol equation and take initial values
of solutions decaying into the interior. This defines the incoming bundle E+
over S*_y(boundary)=S^(n-2). For Q use this actual normal polynomial and its
stable generalized eigenspaces (Riesz projection); do not substitute a Dirac
spectral projector or assume diagonalizability.

A classical complex-linear local elliptic boundary operator has a principal
boundary symbol that restricts to an isomorphism from E+ to the pullback of its
boundary data bundle. At fixed y that target bundle is trivial. Consequently
its reduced K class must vanish. This is a necessary condition; it applies to
finite-order classical local differential boundary operators as well as
zero-order trace subbundle conditions. Boundary systems with additional fields,
real-linear conditions and nonclassical conditions need their own analysis.

For D+ the reduced incoming class is a Bott generator beta in K~^0(S^(n-2))=Z,
up to simultaneous orientation/sign convention. This is the standard
[Clifford/Bott identification of Atiyah–Bott–Shapiro](https://www.maths.ed.ac.uk/~v1ranick/papers/abs.pdf),
not a conclusion inferred only from the dimension-four check. For example in n=4 its Pauli
projector has north/south eigenvectors (1+z,x+iy) and (x-iy,1-z). On the equator
the former equals (x+iy) times the latter; the transition has winding one.
Opposite chiral symbol has -beta. Boundary-symbol formation respects the
elliptic homotopy above, so raw Q+ contributes (n+1)beta at each y.

For a_plus/a_minus raw RS copies and b_plus/b_minus Weyl copies, all untwisted,
the necessary condition is

    kappa=(n+1)(a_plus-a_minus)+(b_plus-b_minus)=0.

For separate twist bundles replace each multiplicity by its total complex rank.
One common ordinary twist of rank r multiplies kappa by r. Nontrivial topology
of that twist may add global obstructions; it cannot erase a nonzero fibre
coefficient. A fixed invertible complex scalar phase also leaves this class
unchanged. This is one structural constraint, not a physical generation formula.

## 4. Executed consequences and repairs

**Metric-fibre end.** Reuse the owned smooth model M=RP3 x D7, boundary RP3 x S6,
with a chosen auxiliary positive spin metric. At every boundary point the
cosphere is S8. A rank-r raw chiral RS block contributes 11r beta. An auxiliary
positive fourteen-dimensional model instead gives 15r beta. Neither statement
converts the source's indefinite K77/K95 operator into an elliptic one. No
extra global K calculation is needed to detect this local obstruction.

**Lower-order repair.** A boundary connection or zeroth-order perturbation
cannot change kappa. It can change actual APS spectra and kernel splitting,
so it is not irrelevant to nonlocal domains. The two assertions concern
different layers of the boundary problem.

**Opposite symbols.** Equal opposite-chirality copies cancel this stable
obstruction. Cancellation alone does not construct an exact boundary rule.
For the genuine doubled Dirac symbol one can explicitly realize a local
elliptic rule: identify the opposite chiral modules by the normal Clifford
map; their adapted tangential symbols become a(eta) and -a(eta). The diagonal
trace subspace {(v,v)} has zero intersection with the incoming space
E+(a) direct-sum E-(a), and both have half the total dimension, so it is
complementing. This rule mixes the original chirality. The finite exact probe
checks this complementing property. No selfadjointness, real-structure,
full-gauge invariance or raw-RS bag rule follows from this Dirac example.

**Grading-preserving rule.** If the trace domain respects the original direct
chiral splitting, complementingness would give a local elliptic condition for
each chiral block. Each retains its own nonzero obstruction. Thus ungraded
cancellation is not a grading-preserving repair. By contrast a pseudodifferential
APS rule has a covector-dependent target, outside the pulled-back-bundle
premise; it is not refuted by this test.

## 5. Released symmetry consequence: rank balance is weaker than module balance

Suppose a compact coefficient symmetry H fixes the boundary point and tangent
covectors and commutes with Clifford action. Replace the multiplicities by
finite unitary H-modules A_plus, A_minus, B_plus, B_minus. Since the action on
the cosphere is trivial, decomposing into H-isotypic summands gives
K_H^0(S^(n-2))=K^0(S^(n-2)) tensor R(H). The reduced incoming class is

    beta tensor V,
    V=(n+1)([A_plus]-[A_minus])+[B_plus]-[B_minus].

An H-equivariant local elliptic boundary map identifies the incoming bundle
with a pulled-back H-bundle; its reduced class is zero. Because the reduced
sphere group is free cyclic, this requires V=0 in the representation ring,
not merely dim V=0. This derivation uses actual coefficient-module
decomposition, not an assumption that a symmetry of the metric preserves the
operator. A geometric gauge group rotating tangent directions is a different
category and is not covered by this factorization.

For n=4 and H=C2, one raw positive RS block with trivial coefficient and five
negative Weyl blocks with sign coefficient have numerical balance5-5=0 but
V=5(1-epsilon). Its nonidentity character is10, so the equivariant obstruction
survives. The exact probe also computes the intertwiner space between the two
five-dimensional coefficient modules: it is zero despite equal dimensions.
Conversely, the explicit doubled-Dirac diagonal complement is H-equivariant
when its two coefficient modules are identified by an equivariant unitary
isomorphism. This constructs that repair only, not a general raw-RS/five-Weyl
repair or an implication that vanishing V suffices globally.

## 6. Verification and remaining transfer

`tests/program-focus/p3_local_boundary_symbol_probe.py` computes actual finite
Clifford/trace/projected symbols, their square spectra, homotopy identities,
normal root generalized spaces, a Bott transition and doubled complement.
Exact matrix controls expose the false Dirac square and test that the explicit
diagonal repair breaks grading. Separate arithmetic accounting records the
n+1 versus n-1 distinction and signed balance; it does not independently prove
the raw symbol class or replace the homotopy. The all-dimension
homotopy and boundary-bundle arguments above are the mathematical proof; finite
probes are independent supporting checks, not a whole-family numerical proof.

A full C decision still needs an inhabited structural category and the actual
native operator, real structure, closed domain, gauge complex and observed
count map. The present result imposes a local-versus-spectral choice on that
category without constructing a gate object. The complementary gauge-domain
analysis is [here](p3-gauge-domain-stabilizer-2026-11-11.md).
