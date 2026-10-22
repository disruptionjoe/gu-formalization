---
title: "K1945: Fixed-energy raw completions and the full observation obstruction"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional exact mathematics; no native GU identification, source selection, novelty or formal proof
scripts:
  - tests/channel-swings/k1945_energy_compatible_raw_columns.py
  - tests/channel-swings/k1945_energy_compatible_raw_columns_probe.py
---

# K1945: Fixed-energy raw completions and the full observation obstruction

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
result: complete fixed-energy raw-column cone and constant full-carrier observation compatibility
carrier: actual corrected K77 real512 with32 real16 blocks and auxiliary real128 LAYER=toy CHIRALITY=N/A
pairing: fixed direct-sum K1832 positive H and independent real dual ON=compressed_conditional_system
real_structure: actual rational Cl(7,7) fixture extended to real fields
grading: one-form and zero-form input slots; no physical cohomology grading
action_owner: repository-construction -- normalized compressed coefficients; not source-owned full20 action
target: raw completion, same-energy dynamics and differential observation MAP-TYPE=intertwiner
```

## Result and scope

The unrestricted raw-column completion of [K1828](k1828-k77-raw-zero-form-completion-2026-10-20.md)
is much less free after the **same** positive energy of
[K1832](k1832-k77-common-energy-form-2026-10-20.md) is imposed. Every dissipative
completion has the form C=H^-1 Q^T Z Q, with Z+Z^T positive semidefinite.
The actual raw southeast map from Z is invertible. A prescribed southeast
block therefore has exactly one possible fixed-energy completion, and it is
admissible only if this matrix inequality holds. Conservation is its skew
subspace, of real dimension8128. No nonzero minimal two-cell completion is
dissipative in this fixed norm.

These completions give actual conditional conservative or contractive PDEs,
but preserving the previous observation adds another independent condition.
With its leading derivative coefficients fixed, a zero-order observation
repair leaves three first-order directions on each real16 block. The FULL
constant-coefficient equations eliminate every nonzero real direction. This
obstruction also holds with arbitrary mixing of all32 copies, by the common
positive functional in section4.1. Special nonconstant solutions remain open.

SC-OP-04 ASSERTS candidate four-independent-field grammar; SC-OP-05 is
UNCERTAIN about a southeast rival. SC-MAS-01 and SC-CHI-02 ASSERT the stylized
curvature-mass toy; SC-META-53 remains UNCERTAIN. None supplies the chosen
positive H, the corrected compression, or an identification of independent
barred fields with their Riesz partners. LT-SM8, LT-GR6b and AC-F1 remain
NEEDS. Source register, physics ledger and canon are unchanged. This pays a
specific compatibility calculation, not the native full20/K-C adapter debt.

## 1. The actual raw map, without a coordinate-transpose shortcut

Use the rational corrected basis from K1824, assembled as an injection
F:R512 -> R640 in the observed coordinates (psi0,psi7,psi8,psi9,nu).
Let Q be its last128 rows, R its raw southeast return, and H the direct sum
of the32 individually normalized K1832 energy matrices. In these precise
bases,

    Q=F_nu, R=-F_0+T Q, T=gamma0 S,
    S=11 Pplus/24+11 Pminus/12,
    N=H^-1 Q^T, M=R N.                                  (1)

K1828's actual ambient lift converts any W:R128 -> R512 into the normalized
one-input-column coefficient C=WQ; the raw southeast block is B=RW.
The certificate reconstructs the full rational fixture, all32 bases, Q,R,H,N
and M. It proves

    rank Q=rank N=rank M=128,
    rank(F_one-form N)=128.                             (2)

The inverse M^-1 exists over Q. In particular R N is NOT T Q N: the Riesz
lift has genuine one-form components. Replacing it with a pure auxiliary
inclusion changes the question. The separate verifier reconstructs T by
binary Clifford indices, checks (1), and proves the ranks modulo1009 after
checking rational identities and invertible denominators. Such a modular
full-rank minor is an exact rational lower-rank certificate.

## 2. Complete conservation and dissipation classification

For the evolution u_t+A_i u_i+C u=0, the fixed energy decreases exactly when
HC+C^T H is positive semidefinite. Suppose C=WQ and let x lie in ker Q.
Then Cx=0 and x^T(HC+C^T H)x=0. A positive semidefinite symmetric matrix
annihilates a vector with zero quadratic value, hence C^T Hx=0. Since Q is
onto, this says W^T Hx=0 for every x in ker Q. Therefore

    im W subset (ker Q)^(perp_H)=im(H^-1 Q^T),
    W=N Z, C=N Z Q.                                    (3)

N is injective, so Z is unique. Conversely

    HC+C^T H=Q^T(Z+Z^T)Q,

which is positive semidefinite exactly when Z+Z^T is. Conservation is exactly
Z^T=-Z, of dimension128*127/2=8128. This proves necessity for the entire
class, not only for sampled skew matrices. It also treats non-self-adjoint
dissipative Z; requiring Z itself to be symmetric would discard valid work.

Combining (1)-(3), a prescribed raw B admits a dissipative completion iff

    M^-1 B+(M^-1 B)^T >=0,                             (4)

and a conservative completion iff this sum is zero. The unique completion
is W=N M^-1 B. The earlier49152-dimensional affine freedom at fixed B has
disappeared inside this energy class. This does not say an unprescribed
source coefficient must obey our chosen norm.

There are explicit nonzero witnesses. Set Z=E01-E10: C has rank2 and is
conservative, B=MZ. Set Z=I128: C has rank128 and is dissipative, B=M.
Both use the actual raw return, not a dimension-matched substitute. The
minimal two-cell completion has pure auxiliary normalized output. By (2)
its intersection with im N is zero, so it is dissipative only when B=0.
Additional output cells genuinely repair this restriction. Noncontractivity
in this fixed energy is not a universal instability or ill-posedness claim.

## 3. Follow-through to a domain and paired derivative action

For constant Z satisfying (4), use R3 or a periodic3-torus, and the SAME
constant principal matrices and H. Fourier transformation gives generators
-i A(xi)-C with nonpositive H-symmetric part. Their exponentials are
contractions, uniformly in xi. Plancherel gives a strongly continuous
contraction semigroup on L2_H and every H^s_H; the natural generator domain
is H1 because the K1832 symbol is uniformly invertible away from zero.
For skew Z it is an isometric group. This is the standard energy method
with an explicit coefficient, not a new theorem of symmetric hyperbolicity.
The local energy identity and |u^T H A(n)u|<=u^T H u preserve speed at most1.
The torus has nondamped constant data in ker Q, of dimension384; no uniform
strict decay of all data is asserted. Spatially varying bounded dissipative
coefficients preserve the energy inequality, but the report's domain theorem
is stated only for the constant case.

For conservative C, P=partial_t+A_i partial_i+C has weighted formal adjoint
P^dagger=-P on compactly supported spacetime tests. The first derivatives
supply the minus sign. The conditional independent-dual action

    S[y,u]=integral y^T H P u

gives Pu=0 and P^dagger y=0, hence the same equation for independent y.
Setting y=u would make the real commuting-field quadratic action a boundary
term; it would NOT reconstruct these Euler equations. Neither this pairing
nor [K1830](k1830-k77-paired-action-nilpotent-completion-2026-10-20.md)'s
finite dual retract is a source-owned barred reality condition. The original
uncompressed derivative operator is not silently replaced by this compression.

## 4. The SAME observation is an independent test

First keep exactly O=T_i partial_i from
[K1836](k1836-k77-differential-dirac-quotient-2026-10-20.md). On each block,
T_i restricted to ker Q is onto R4, and T_i N is invertible. These exact
rank facts hold in all four coordinate types. In the full direct sum, if
T_i C=B_t T_i with C=N Z Q, evaluation on ker Q forces B_t=0; then
T_i N Z=0 forces Z=0. This conclusion allows arbitrary cross-copy Z and B_t.
Thus no nonzero fixed-energy raw-column completion preserves the unchanged
observation. This is not a statement about all possible observation maps.

Test the immediate repair, O=T_i partial_i+S, on ONE real16 block with real4
target. Let Z and B_t be arbitrary skew4-by4, and S arbitrary4-by16. The
first-order equations are

    T_i N Z Q-B_t T_i+S A_i-d_i S=0, d_i=D_i/24.        (5)

They have76 real unknowns and192 equations. The complete rational matrix
has rank73 in every coordinate type. Its three basis triples(C_a,B_a,S_a)
are serialized. First-order survival is not enough: constants must also obey

    S C-B_t S=0.                                      (6)

Write a general triple as sum v_a(C_a,B_a,S_a). In monomial order
(v0^2,v0v1,v0v2,v1^2,v1v2,v2^2), the row space of the actual matrix
coefficients in (6) is EXACTLY the span of

    v0^2, v0v1, v0v2, v1^2+v2^2.                     (7)

Over the REAL field (7) implies v0=v1=v2=0. A complex vector(0,1,i)
satisfies these polynomial equations, so forgetting the real-field premise
would change the result. The independent probe rebuilds (5) rowwise,
certifies rank73 modulo1009 plus a rational three-dimensional kernel, and
recomputes (6)-(7) directly from the stored triples. No solver's declared
ideal or nullity is accepted on its own.

For a common scalar profile f(x_j) multiplying one constant triple, the
remaining derivative coefficient is T_j C-d_j S. Its map on the three
parameters has rank3 for every j and all types. No nonzero triple therefore
works for EVERY such profile. This does not rule out specially coupled
nonconstant functions satisfying their full derivative/quadratic equations,
while section4.1 covers constant cross-copy S. K1840's successful mass profiles use a larger
input-column class and remain valid.

## 4.1. Released successor: all32 copies, without a block-diagonal assumption

The block result alone does not settle arbitrary mixing. We therefore test
all ten unordered pairs of the four coordinate types. For an off-diagonal
pair a,b, fixed-energy conservation forces

    C_ab=N_a Z_ab Q_b, C_ba=-N_b Z_ab^T Q_a,
    B_ba=-B_ab^T,

with arbitrary real4-by4 Z_ab,B_ab and independent4-by16 S_ab,S_ba.
The two directed versions of(5) give384 equations in160 variables. Each
pair has rank156 and a complete four-dimensional rational kernel. This
includes two different copies of the SAME coordinate type. The full32-copy
first-order space consequently has dimension

    32*3 + (32*31/2)*4 =2080.

One cannot infer that all its nonlinear solutions vanish by checking isolated
pairs. Instead construct four linear functionals ell_type on4-by16 diagonal
residuals. The certificate stores them as a4-by64 rational matrix with eight
nonzero entries. It verifies TWO sets of coefficient identities:

* on every diagonal three-parameter family, ell_type(SC-BS) is a diagonal
  quadratic form with strictly positive rational coefficients;
* on every four-parameter pair, ell_a(S_ab C_ba-B_ab S_ba) plus
  ell_b(S_ba C_ab-B_ba S_ab) is likewise a strictly positive diagonal
  quadratic form.

All mixed monomial coefficients are EXACTLY zero. The minimum recorded square
coefficient is1. The first attempted equal-coefficient normalization was
inconsistent; a floating linear feasibility search suggested the eight-entry
support, after which an exact rational system solved it and all124 monomial
constraints were checked. Floating success is not acceptance.

For arbitrary32-copy coefficients, sum ell_type(i) over the diagonal blocks
of SC-BS. Each diagonal block contains its own local term plus one term per
other copy; no three-copy loop occurs in a quadratic diagonal product. Thus
the sum is precisely a positive weighted sum of squares of ALL2080 independent
first-order parameters. If SC-BS=0, every parameter vanishes. Hence

    C=0, B=0, S=0

is the ONLY real constant conservative solution with this fixed leading
observation and one-auxiliary-input-column raw coefficient, allowing arbitrary
cross-copy mixing. The separate verifier rebuilds every cross-copy equation,
checks the rational kernels and independent modular ranks, reconstructs the
quadratic products, and verifies the SAME four functionals on all types.
This finite component certificate proves the full-carrier assertion through
the direct-sum identity; it is not an inference from random mixtures.

The scalar variable-profile test above is not a theorem against all special
nonconstant matrices. Their derivative terms may change the positive-sum
argument. Additional raw INPUT columns also leave the tested class; the known
K1840 mass lifts are such a concrete surviving alternative. This is the next
support-construction question, not a reason to repeat the completed cross-copy
test or to attribute the obstruction to the source's full20 operator.

## 5. Verification and research consequence

Run the two frontmatter scripts with Sage Python; the producer's --write
option regenerates the rational artifact. The producer checks42 new exact
identities and reuses20 fixture checks. The independent probe uses different
row assembly and modular rank witnesses. Five altered mathematical inputs
(Riesz lift, raw return, raw southeast map, observation correction and global positive functional) must
fail assertions after a green baseline; report/pin checks are separate.

Preflight preferred kernel geometry to a full raw matrix search. The strongest
overclaim is a native K/C identification or all-observations exclusion; neither
is asserted. The concrete contrary construction is the nonzero conservative
completion in section2: failure of the two-cell representative is repairable.
The full observation equation then defeats every constant repair in this
conservative class, including arbitrary copy mixing.
The weakest transfer seam is physical ownership, not matrix rank. No external
expert review, formal proof, novelty or canon promotion is claimed.

Next: compare special variable solutions with adding the smallest raw input
support that realizes K1840's known conservative mass lifts. Cross-copy
constant mixing is now covered, not an open successor. A source-selected same-background datum must
still identify the full20 placement, actual barred K/C maps and physical
accessible algebra. The common-energy calculation alone cannot supply them.
Established method context: [Tadmor's energy method](https://www.math.umd.edu/~tadmor/lecture-notes/hyperbolic/node4.html).
