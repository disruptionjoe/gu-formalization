---
title: "K2002: A differential trace identity excludes every local positive raw pairing"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics on fixed raw coefficients and core; no source pairing identification, GU falsification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2002_clifford_pairing_integrability.py
  - tests/channel-swings/k2002_clifford_pairing_integrability_probe.py
---

# K2002: A differential trace identity excludes every local positive raw pairing

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
result: exact differential trace identity and complete local semidefinite-pairing obstruction
carrier: unchanged raw1920 section and real128 core on14 flat coordinates LAYER=toy CHIRALITY=N/A
pairing: arbitrary real symmetric128 matrix field, including distributional solutions ON=raw_spinor_and_vector_spinor
real_structure: fixed real Cl(7,7) coefficients; no identified source bar or star
grading: Clifford blades and polynomial differential degree, not observed chirality
action_owner: repository-construction -- unchanged raw lower-return equation
target: full multicoordinate symmetric integrability MAP-TYPE=intertwiner
```

## 1. The local positive-pairing question is closed for this fixed model

Keep the actual J_k, Omega_k,T and both signs s=+1,-1 of
[K1976](k1976-general-pairing-transport-2026-10-23.md). Write

    E_s(Q)=sum_(k<14) eta_k(partial_k Q)J_k-R_s(Q),
    R_s(Q)=sum_(k<14)eta_k Omega_k^T Q J_k-s Q T,
    eta_k=+1 for k<7 and -1 otherwise.                         (1)

For EVERY real symmetric matrix-valued distribution Q on ANY open subset of
R14 satisfying E_s(Q)=0, **tr Q=0 as a distribution**. In particular every
continuous positive-semidefinite or negative-semidefinite solution is ZERO.
No local positive-definite or negative-definite solution exists, even with
arbitrary multicoordinate transcendental dependence. This is a local result;
no growth, periodicity, boundary condition, analytic continuation, algebraic
ansatz, or boundedness is assumed.

The proof is an exact constant-coefficient differential identity. For each
sign the report supplies a polynomial matrix Y_s of degree at most4. Its
full14-variable lift gives constant matrices C_alpha such that, for every
symmetric Q,

    tr Q = sum_(|alpha|<=4) <C_alpha, partial^alpha E_s(Q)>_F. (2)

Here <A,B>_F=tr(A^T B). Equation(2), proved coefficientwise below, is valid
in distributions. Thus C1 solutions are covered without assuming their
classical fifth derivatives exist.

This settles the open local symmetric positive question left by K1979,
K1985 and K2000. Their positive first and second jets remain correct: a
necessary low-order jet need not extend to a solution. The existing
nonsymmetric analytic repair also survives. Nonzero symmetric INDEFINITE
solutions survive; section6 supplies an exact example. No source-selected
pairing, physical quotient, action, observed chirality or GU verdict follows.

## 2. The actual raw symbol has a useful right transformation

Let gamma_k be the actual real Clifford generators, V=gamma_0...gamma_13,
and X=J_0^-1 gamma_0. Independently reconstructed raw multiplication proves

    J_k X=eta_k a_k gamma_k,
    T X=-(3I+5V)/4,
    a_k=1 on H={0,7,8,9}; a_k=-4/9 on N={1,...,6,10,...,13}. (3)

These are full128-square matrix identities. The original J_k are not
Clifford generators; multiplying all of them on the RIGHT by the SAME
invertible X is essential. It changes neither the unknown Q nor its symmetry,
and E_s(Q)=0 is equivalent to E_s(Q)X=0. This does not undo the earlier
warning against squaring the untransformed J_k as Clifford matrices.

The transformed equation is

    E'_s(Q)=sum a_k(partial_k Q)gamma_k-R'_s(Q),
    R'_s(Q)=R_s(Q)X
            =sum a_k(u_k+w_k V)gamma_k Q gamma_k
                         +s Q(3I+5V)/4.                    (4)

The exact u,w are the original normalized repair coefficients:
(u,w)=(-5301,7559)/23168 on H and (-594,198)/23168 on N.
Indeed Omega_k^T=(u_k+w_k V)gamma_k, verified against the actual raw
coefficients, not inferred from a conventional replacement.

## 3. A small exact polynomial certificate, then all14 variables

For a covector xi put P(xi)=sum a_k xi_k gamma_k. The decisive identity is

    Sym(Y_s(xi) P(xi)^T - (R'_s)^*(Y_s(xi)))=I.             (5)

The star here means ONLY the algebraic Frobenius adjoint of the constant
matrix-space map R'_s. It is not an integration-by-parts adjoint and creates
no derivative sign. Sym(A)=(A+A^T)/2.

First use representative coordinates p=(xi_0,xi_1,xi_7,xi_10). The32 basis
matrices are the ordered products of gamma0,gamma1,gamma7,gamma10 for masks
0..15, followed by V times those products. All have squared Frobenius norm128
and are mutually orthogonal; twenty are symmetric. The producer constructs
both derivative and zero-order maps from the original raw matrices and solves
318 exact rational coefficient equations in280 unknowns. For each sign it
finds112 nonzero terms of degree at most4. The report stores every rational
coefficient and exponent. The smaller degree2 covariant ansatz is inconsistent;
that is not a claim of globally minimal certificate degree.

This reduced solve alone would not prove(5) against matrices outside the32
basis span. The independent checker closes that seam: it verifies the actual
raw algebraic adjoint and the COMPLETE lifted polynomial matrix identity,
including all nonconstant coefficients. No projected-rank argument is used
to declare the full-space result.

### Polynomial lift without divisions or exceptional covectors

Use three groups G1={1,...,6}, G2={7,8,9}, G3={10,...,13}. For every stored
term, the exponent of p_g has the same parity as occurrence of that group's
representative gamma in its basis blade. Replace each even pair p_g^2 by
sum_(k in Gg) xi_k^2, and each remaining p_g gamma_rep by
sum_(k in Gg)xi_k gamma_k. Keep gamma0 fixed and p0=xi0. This produces an
ordinary polynomial matrix on ALL14 coordinates, of degree at most4;
there is no normalization or division by a group length.

The structural reason is SO(6)xSO(3)xSO(4) covariance. Rotations within each
group lift to conjugation by real Euclidean-orthogonal spin matrices: products
of two same-sign gamma generators are skew under coordinate transpose.
Those conjugations preserve V, transpose, the actual coefficient groups and
R'_s, and rotate each group covector to its representative. This transports
(5) on real nonzero group vectors. Polynomial equality extends across zero
groups and, after complexification, complex null covectors as well.

The checker does not rely on covariance as an unchecked shortcut. It expands
the lift into2308 nonzero exponent/blade terms and1281 distinct monomials for
EACH sign, multiplies in the full Cl(7,7) algebra, and verifies that the
symmetric part in(5) is exactly the constant identity. All other polynomial
coefficients cancel. It verifies all196 actual Clifford relations, the14
raw symbol transforms, the target and connection formulas, and direct raw
adjoint identities on the26 representative blades used per sign. These
checks establish the algebraic representation and adjoint formula applied
by the full14 coefficient calculation.

## 4. Differential consequence and fifth-jet obstruction

Pair(5) with any symmetric constant matrix A. This gives

    <Y_s(xi), A P(xi)-R'_s(A)>_F=tr A.                     (6)

Write Y_s(xi)=sum Y_alpha xi^alpha. Substitute commuting differential
operators for the formal variables. The coefficients are constant, so the
polynomial identity gives

    tr Q=sum <Y_alpha,partial^alpha E'_s(Q)>_F.

Since E'_s=E_s X, set C_alpha=Y_alpha X^T to obtain(2). This substitution
uses the SAME derivative signs as the symbol calculation. Negative signs
occur only when subsequently moving derivatives onto a test function.

At a point, vanishing of the equation and all its derivatives through
order4 forces tr Q at that point to vanish. Thus no symmetric fifth-order
jet with positive-definite value can satisfy those prolonged equations.
This is an actual finite-order compatibility obstruction, not continued
finite-jet survival or an unproved assertion about series convergence.
The exact order4 certificate is sufficient; no minimal prolongation order
is asserted. K1979's full positive first jets and K1985's symmetric second
jets are unaffected and remain useful contrary controls for an earlier-order
or one-point exclusion.

## 5. Released consumers: approximate residuals cannot disappear

For a C5 symmetric Q at a point define
D=max_(|alpha|<=4) ||partial^alpha E_s(Q)||_max-entry. Equation(2) gives

    |tr Q| <= D sum_alpha ||C_alpha||_entrywise1.             (7)

The independent probe computes a rigorous rational upper bound for that sum
by expanding the actual certificate and using the signed-permutation Clifford
basis and the actual X. Through Q=I, it proves the following conservative
strictly positive lower bounds on D:

- s=-1: 52045409004490862975088656552293785 /
  375024620519465193721646406438003220622624.
- s=+1: 132531847896698524186527531685923 /
  2515864733022874332606832864155593435296.

They concern residual derivatives through order4, not merely pointwise
residual amplitude, and are not claimed optimal.

There is also a fixed-domain L2 consequence without controlling high
residual derivatives. For any nonnegative smooth compactly supported scalar
phi, define

    K_phi=sum_alpha (-1)^|alpha| C_alpha partial^alpha phi.

Distributional integration by parts in(2) gives

    integral tr(Q) phi = integral <E_s(Q),K_phi>_F.          (8)

If Q>=mI almost everywhere on supp(phi), m>0, integral phi>0,
and E_s(Q) is represented by an L2 matrix field there, Cauchy--Schwarz gives

    ||E_s(Q)||_L2(supp phi)
       >=128 m integral phi / ||K_phi||_L2 >0.              (9)

The norm is the Frobenius matrix L2 norm. The denominator cannot vanish:
applying(8) to Q=I would contradict integral phi>0. This supplies a genuine
local residual gap on any fixed domain with a chosen test bump, including
weak residual formulations. The constant depends on the bump/domain; no
uniform lower bound over shrinking domains is asserted. The result does
not prohibit positive approximate low-order Taylor fields whose domain or
uncontrolled residual derivatives change.

## 6. Nonzero indefinite and nonsymmetric solutions remain

The conclusion is trace zero, not zero for every symmetric field. For s=+1,
let

    lambda^2=54542565/67094528, lambda>0,
    A0=-3 gamma0 gamma10+V gamma0 gamma10,
    A1=(23168/3267) gamma0,
    Q(x)=exp(lambda x10)(A0+lambda A1).                     (10)

Both A0 and A1 are real symmetric and traceless. The independent probe
checks the two rational raw identities

    -lambda^2 A1 J10=R_+(A0),  -A0 J10=R_+(A1),

which prove(1) exactly. This is a nonzero symmetric traceless field and hence
indefinite. It provides an explicit opposite-scope control, not a positive
pairing or a claim of nondegeneracy. K1976's nonsymmetric analytic transport
is also outside the symmetry hypothesis. A different raw core, coefficients,
principal placement, pairing assignment or source-selected reality structure
remains a different construction; none is ruled out by(2).

## 7. Verification, hostile review and source ceiling

Producer: two complete degree4 rational systems; full raw transformation and
representative invariance checks. Separate checker: complete all14-variable
polynomial identity, actual independent signed-bit reconstruction, raw
adjoint checks, positive first-jet controls, the indefinite exponential,
residual bounds and four genuine mathematical corruptions (certificate,
mass sign, transpose and connection coefficient) rejected after green baseline.
No floating rank, finite sampling or selected-point residual certifies the
universal conclusion. These are internal implementations; the finite exact
certificate and written argument are reproducible but are not a proof-assistant
formalization, external specialist acceptance or novelty evidence.

Preflight tested the actual right transformation before prolonging another
Taylor jet. Clifford/covariance, PDE compatibility, algebraic duality and
positive-cone reasoning changed the route: a constant differential identity
settles the complete local definite class and removes arbitrary higher-jet or
transcendental positive-ansatz searches on this unchanged model. A preliminary
two-coordinate reduction led to the full14 identity; the narrower calculations
are superseded by its explicit certificate, not presented as independent gains.

Strongest overclaim: all symmetric pairings vanish or GU positivity is
falsified. Equation(10) and the absence of a source-selected bar disprove
those inferences. Strongest contrary evidence is the earlier positive first/
second jets; section4 explains exactly why they coexist with this higher
compatibility obstruction. Weakest seam was reduced versus full matrix-space
adjoint and all14-variable lift; the independent full coefficient identity
checks both. No unresolved contradiction was found in the stated scope.

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 is UNCERTAIN about
unselected rivals. SC-MAS-01/02 ASSERT scoped stylized mass claims without
selecting this Q. SC-META-53 remains UNCERTAIN; SC-META-56 DISAVOWS the extra
odd-action prerequisite. LT-SM8/LT-GR6b, source register, physics ledger and
canon verdicts remain unchanged. Further physical work must change or
identify a missing input, such as the source bar/common pairing assignment,
raw core or coefficient realization, rather than continuing a positive
symmetric solve that(2) now excludes under the same assumptions.
