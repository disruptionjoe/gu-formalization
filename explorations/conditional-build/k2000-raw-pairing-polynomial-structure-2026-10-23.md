---
title: "K2000: Algebraic raw pairings and one-phase fields are excluded"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2000_raw_pairing_polynomial_structure.py
  - tests/channel-swings/k2000_raw_pairing_polynomial_structure_probe.py
---

# K2000: Algebraic raw pairings and one-phase fields are excluded

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
result: full zero-order operator invertibility, algebraic-field obstruction and robust one-phase exclusion
carrier: unchanged raw1920 section and real128 core on14 flat coordinates LAYER=toy CHIRALITY=N/A
pairing: arbitrary real matrix field, symmetric only for the one-phase result ON=raw_spinor_and_vector_spinor
real_structure: fixed real Cl(7,7) coefficients without source bar identification
grading: matrix-entry invariant sectors and polynomial degree, not observed chirality
action_owner: repository-construction -- unchanged raw lower-return equation
target: complete algebraic ansatz class and local one-scalar dependence MAP-TYPE=intertwiner
```

## Result and exact scope

Keep the ACTUAL J_k, Omega_k,T and both signs s=+1,-1 from
[K1976](k1976-general-pairing-transport-2026-10-23.md). The equation is

    B(partial Q)=sum_(k<14) eta_k(partial_k Q)J_k=R_s(Q),
    R_s(Q)=sum_(k<14)eta_k Omega_k^T Q J_k-s Q T.        (1)

The zeroth-order real linear map R_s:Mat128->Mat128 is invertible for
BOTH signs: exact rank16384. Consequently **no nonzero rational matrix
field solves(1) on any nonempty open set**. Polynomial fields of ANY degree
are included. The Newton–Puiseux follow-through below strengthens this to every
nonzero algebraic matrix-field germ. Symmetry, positivity and global boundedness
are not assumed.
This is stronger than the previous failure of the specific quadratic Taylor
field and different from K1982's global PSD growth obstruction.

A distinct result concerns nonpolynomial fields. No C1 symmetric field of
the form Q(x)=F(theta(x)), for one real C1 scalar theta and a C1 symmetric
matrix-valued function F, can solve(1) through Q=I. The exclusion persists
in an explicit matrix-norm neighborhood of I, given below. The phase may be
NONLINEAR and all14 coordinates may occur in it. No invertibility of the
characteristic matrix is assumed.

These are exclusions of construction classes in the fixed conditional raw
model. They do not exclude a genuinely multicoordinate analytic positive
pairing, select the source bar, or settle GU physical positivity. K1979's
positive full first jet and K1976's nonsymmetric analytic solution survive.

## 1. Full zero-order rank from small invariant sectors

Right-compose R with the existing exact inverse of J0. Set

    L_s(Q)=R_s(Q)J0^-1,
    B_k=J_k J0^-1, C=T J0^-1.

Actual sparse reconstruction gives the following entry transitions. Label
matrix rows and columns by seven-bit integers i,j. For coordinate k with
axis-bit b=2^(6-(k mod7)), Omega_k^T changes the row by XOR b.
B_k changes the column by XOR(b XOR64); C changes it by XOR64.
All coefficients are exact rationals, including their chirality dependence.
Therefore every term preserves

    (i XOR j) AND63.

There are64 disjoint invariant sectors, each containing256 entry basis
matrices E_ij, and their union is ALL16384 entries. This is not a symmetric
subspace restriction. The producer constructs every column of each actual
256-dimensional L_s block, checks no entry leaves its sector, and performs
exact elimination modulo the prime1000003. Every block has rank256 for
both signs; all rational denominators are invertible modulo that prime.
A nonzero determinant modulo a prime proves the rational determinant nonzero.
Since J0 is invertible, R_s has the same full rank.

The independent probe reconstructs the earlier raw section with its separate
signed-bit implementation. It constructs the FULL16384-by16384 sparse R_s
map directly, without J0^-1, the sector formula, or the producer's elimination,
and obtains rank16384 at the different prime1000033 for each sign.
This is exact finite-field linear algebra, not a numerical rank threshold.
The stored pivot hashes are reproducibility aids, not the proof of rank.
The finite exact rank calculation is essential evidence; the polynomial and
rational consequences below then hold at every degree without enumerating it.

## 2. Leading degree excludes every rational field

Suppose Q=P/d, where P is a polynomial matrix, d a nonzero real polynomial,
and d is nonzero on a nonempty open subset where(1) holds. A common denominator
exists for any finite collection of rational matrix entries. Multiplying(1)
by d² gives the polynomial identity

    sum_k eta_k[d(partial_k P)-(partial_k d)P]J_k
                 =d R_s(P).                          (2)

An identity on a nonempty real open set is a polynomial identity everywhere.
If P is nonzero of total degree m and d has degree n, the left side has degree
at most m+n-1. The right side has degree EXACTLY m+n: its top homogeneous
part is d_n R_s(P_m). Invertibility of R_s guarantees R_s(P_m) is nonzero,
and a nonzero scalar polynomial cannot annihilate that polynomial matrix.
Contradiction. Thus P=0, proving the full rational-field result.

The argument is local despite using polynomial degrees: it needs neither an
extension of the solution across poles nor any boundedness at infinity.
It permits arbitrary real coefficients and common denominators with any
number of coordinate variables. A Taylor truncation may approximate a solution,
but can NEVER terminate as a nonzero exact solution of this fixed equation.
The following successor addresses algebraic functions. Infinite transcendental
series and general C1 solutions remain outside the conclusion.

## 2a. Released successor: all algebraic germs are excluded

The rational proof has an algebraic extension. A matrix-field germ is called
algebraic here when each entry is algebraic over C(x_0,...,x_13); real algebraic
branches are included by complexification at a nonsingular point. These are
finite algebraic extensions, not arbitrary analytic or formal power series.
Restricting a nonzero local algebraic solution to a generic nonsingular point
retains a nonzero algebraic germ and its differential identity.

Use the generic projective chart x_13=t, x_i=t y_i (i<13). The base field is
C(y_0,...,y_12)(t). Let K be an algebraic closure of C(y_0,...,y_12), and use
z=1/t. The characteristic-zero Newton–Puiseux theorem embeds any finite
algebraic extension of K(z) into a Puiseux series field over K, after selecting
one branch. In particular our finite collection of algebraic entries has a
common denominator of exponents and a finite HIGHEST power of t. Write its
leading matrix term as t^rho Q_rho(y), with nonzero Q_rho over K.

The theorem used here is precisely algebraic closedness of the Puiseux field
over an algebraically closed coefficient field of characteristic zero; see
[Manuel Eberl, Formal Puiseux Series](https://isa-afp.org/entries/Formal_Puiseux_Series.html),
2021. Its hypotheses apply to K. This external formal theorem is not a
formal verification of the present matrix-PDE argument.

In these coordinates the derivations are

    partial_(x_i)=t^-1 partial_(y_i), i<13,
    partial_(x_13)=partial_t-t^-1 sum_(i<13)y_i partial_(y_i).

Each sends a series with highest power rho to one with highest power at
most rho-1. The y derivations act on coefficient field K and extend uniquely
to algebraic extensions in characteristic zero. Coefficientwise differentiation
of the Puiseux series agrees with these extensions: differentiate the minimal
polynomial, whose derivative at its algebraic root is nonzero by separability.
Thus this is a differential-field embedding, not an arbitrary change of branch
that forgets the differential identity.

The derivative side of(1) therefore has highest power at most rho-1, while
the right side has nonzero term t^rho R_s(Q_rho). The rational matrix R_s
remains invertible over K, so that leading coefficient cannot vanish.
Contradiction. No convergence of the Puiseux expansion or physical passage to
infinity is needed: it is an algebraic test of an identity of germs.

This excludes all finite radical and other algebraic closed-form ansatzes,
including nonrational ones with local branch cuts, in the unchanged raw model.
It does not exclude a transcendental convergent matrix series. In particular
K1976's nonsymmetric exponential is outside this class. The leading-degree
proof for rational functions remains useful because it avoids this theorem.
A singular zero-order map would invalidate both arguments; constants in its
kernel are the immediate contrary control. The independent probe additionally
checks the coordinate-derivation formulas at four positive and negative
fractional orders; these are algebraic controls, not a substitute for the
Newton–Puiseux proof.

## 3. A rank14 symmetry discriminator excludes one scalar phase

At a point with Q=I, a one-phase field has derivatives
partial_k Q=xi_k H with H symmetric and xi_k=partial_k theta. Equation(1)
would give H J(xi)=R_s(I), where J(xi)=sum eta_k xi_k J_k.
Necessarily

    J(xi)^T R_s(I)-R_s(I)^T J(xi)=0.                  (3)

This follows by inserting H and its transpose; it remains necessary when
J(xi) is singular. The14 coefficient matrices

    A_k=J_k^T R_s(I)-R_s(I)^T J_k

are linearly independent. The linked report contains14 selected entry slots,
their14-by14 rational matrix M_s and its exact inverse. Direct multiplication
checks that inverse. The eta signs merely rescale the14 unknown xi_k.
Thus(3) forces xi=0, which makes every derivative zero, contradicting the
nonzero R_s(I). Nonlinear theta has no escape at a critical point.
This result concerns dependence through one scalar function; it is not a
count of the number of nonzero coordinate derivatives in a general field.

## 4. Released robust neighborhood and surviving contrary constructions

Use the maximum absolute row-sum matrix norm. For arbitrary symmetric Q,
replace R_s(I) by R_s(Q) in the selected entries of(3), giving M_s(Q).
Let

    C_R=sum_k ||Omega_k^T||_infinity ||J_k||_infinity
                  +||T||_infinity,
    C_A=2 C_R sum_k ||J_k^T||_infinity,
    B_s=||M_s(I)^-1||_infinity,
    delta_s=1/(2 B_s C_A).

Each selected entry perturbation is bounded by
2||J_k^T||_infinity C_R||Q-I||_infinity; summing columns gives
||M_s(Q)-M_s(I)||_infinity<=C_A||Q-I||_infinity.
If ||Q-I||_infinity<=delta_s, the relative inverse perturbation is at most1/2,
so M_s(Q) remains invertible. Equation(3) with Q in place of I forces xi=0,
then R_s(Q)=0 and hence Q=0. Zero is outside this certified neighborhood.
Therefore NO such one-phase solution can pass through it.

- Sign -1: delta_s=3123/2968864.
- Sign 1: delta_s=6833/2968864.

These conservative rational radii are not optimal. By homogeneity the same
result applies to relative neighborhoods of any nonzero scalar multiple cI:
||Q-cI||_infinity<=|c|delta_s. This is not coordinate-invariant under changing
only Q; the frozen coefficients must transform too. It does not exclude all
positive initial matrices elsewhere in the positive cone.

The independent probe contracts K1979's stored full multicoordinate symmetric
jets against the actual J_k and confirms B(H)=R_s(I) for both signs. Thus the
new exclusion cannot be broadened to all positive first jets. K1985's second
jets and its nonzero remaining defect are also consistent with the rational
obstruction: finite compatibility is not termination. K1976's entire
nonsymmetric one-coordinate solution is a contrary control for dropping
symmetry from the one-phase theorem. It is transcendental, consistent with(2).

## 5. Verification and frontier

Producer:128 complete256-dimensional modular rank blocks and two exact14-by14
phase minors/inverses. Separate probe: two full raw rank computations at a
second prime and436 exact phase, inverse, norm and positive-first-jet checks.
Four corrupted mass-sign, coefficient, inverse and radius inputs are rejected
after a green baseline. The degree/Puiseux proofs cover rational/algebraic germs;
finite rank checks do not by themselves prove PDE existence or nonexistence
outside that class. All verification is same-author internal work.

Strongest overclaim: replacing "algebraic" or "one scalar phase near I" with
"every local positive field." The known full jets prevent that inference.
Strongest contrary route is a convergent genuinely multicoordinate analytic
construction with off-diagonal matrix coefficients and a common symmetric
integrability condition. Full matrix-polynomial, rational and algebraic searches are now
eliminated, as are scalar-phase exponentials through identity; neither another
finite jet nor an arbitrary unverified exponential is the missing construction.
The weakest seam is convergence/integrability of that remaining infinite
system on an actual domain.

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 remains UNCERTAIN about
unselected rivals. SC-MAS-01/02 ASSERT scoped stylized mass statements, without
selecting this Q. SC-META-53 remains UNCERTAIN; SC-META-56 DISAVOWS the extra
odd-action prerequisite. LT-SM8/LT-GR6b, source-register and canon verdicts
remain unchanged. No GU falsification, source-selected physical pairing,
external specialist acceptance, formal certification or novelty is claimed.
