---
title: "K2024: Full odd connection obstruction and a positive-core massive completion"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional exact algebra and observed-subsystem dynamics; no source-selected connection, physical quotient, full-carrier positivity, GU verdict or novelty claim
scripts:
  - tests/channel-swings/k2024_full_odd_connection_compatibility.py
  - tests/channel-swings/k2024_full_odd_connection_compatibility_probe.py
---

# K2024: Full odd connection obstruction and a positive-core massive completion

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: complete392-coefficient obstruction and explicit broader massive formal completion
carrier: K1951 full1920 raw carrier and its fixed invariant128 observed core LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: K2021 full indefinite H and separate inherited positive core P=8I ON=declared_full_and_core_carriers
real_structure: real Cl(7,7) coefficients, complex Fourier solutions
grading: ambient Clifford halves and independent form degree; no observed family count
action_owner: repository-construction -- fixed raw principal symbols, freely constructed zeroth-order blocks
target: common formal adjoint plus positive conservative massive core MAP-TYPE=intertwiner
```

## 1. The result changes the next question

[K2022](k2022-degree-dual-dynamics-boundary-2026-10-24.md) excluded a nonzero
mass in a four-scalar connection class. The present exact census expands that
class to **all392 independent real grade-one and grade-thirteen coefficients**.
Upper-core invariance leaves11 parameters; upper H-adjointness leaves one;
imposing the SAME inherited positive-core conservation leaves zero.
An arbitrary lower return cannot change this upper obstruction.

That is not an obstruction to every formal massive completion. A different,
explicit zeroth-order block construction below satisfies full H-adjointness,
preserves the same128-dimensional core, conserves its positive energy and has
a nonzero spectral gap. A second construction keeps the southeast block ZERO.
Both leave the full1920-dimensional principal Jordan obstruction intact.

The coefficient restriction, not mere formal duality or the zero-southeast
incidence pattern, is therefore load-bearing. Neither construction is a
source-selected connection, a physical constraint, or an interacting quotient.
The useful next source-facing question is whether a source-owned coefficient
or constraint can realize this compatibility, with the same operator and state.

## 2. Frozen objects and the complete connection census

Use the full raw D_k, symmetric invertible H, observed directions0,7,8,9,
core injection Jc, positive form P=8I and three symmetric Clifford generators
C_i from K1951/K1967/K2021. In particular

    D_i Jc = D_0 Jc C_i,    C_i C_j+C_j C_i=2 delta_ij I.

Do not identify this four-direction subsystem with every ambient equation.
Let Gamma be the fourteen-dimensional Clifford volume. The enlarged class is

    Omega_k = sum_a (x_ka gamma_a + y_ka gamma_a Gamma),
    k,a in{0,...,13}, x_ka,y_ka real.                     (1)

The raw upper coefficient is the upper block rows of
sum_k D_k diag(Omega_k,...,Omega_k). There is no isotropy, diagonal-covector
or four-scalar restriction in(1). Other Clifford grades are not included.
For its action on Jc, the top time row determines a unique induced M, since
the corresponding Jc zero-form block is invertible. Every remaining upper
row must equal its row of D_0 Jc M.

The report stores exact rational kernels and full-rank minors with explicit
inverses. Block decomposition is by shared equation support, not a guessed
representation truncation. Each kernel annihilates every original equation.

| Constraint | Rank on current parameters | Surviving dimension |
| --- | ---: | ---: |
| All upper-core invariance equations on392 coefficients |381|11|
| All upper entries of HK-K^T H on that11-space |10|1|
| Joint upper H-adjointness and PM+M^T P=0 on that11-space |11|0|

The extra inherited196 grade-one and four-scalar results are controls and
context, not additional new classifications. The lower return and southeast
block cannot alter the upper-left adjoint defect. This establishes the scoped
zero intersection without guessing the lower map. It does not exclude another
pairing, core, Clifford class or unrestricted matrix coefficient.

## 3. The exact general extension criterion

The subsequent structural test avoids guessing more connections. For ANY
prescribed core endomorphism M, seek an H-self-adjoint full coefficient K with

    K Jc = D_0 Jc M.                                      (2)

Put S=Jc^T H D_0 Jc and Y=H D_0 Jc M. Such K exists if and only if

    S M is symmetric.                                    (3)

Necessity: multiply HK=K^T H on the left and right by Jc^T,Jc and use(2).
For sufficiency choose any left inverse O Jc=I and set

    L=Y O+O^T Y^T-O^T(Jc^T Y)O,    K=H^-1 L.             (4)

When(3) holds, L=L^T and L Jc=Y. No positivity is assumed for H.
For this core, exact reconstruction gives S^T=-S, rank128,
[S,C_i]=0 and diagonal -S^2 with values81/19600 and81/4900.
The old K1967 positive mass fails(3), with rank128 defect. Thus even an
unrestricted lower/block completion cannot realize that PARTICULAR old mass
with this H and this same core. A different mass is a real new branch.

## 4. An explicit conservative gapped mass that passes the criterion

The construction changes M rather than refitting its constraints independently.
Start with elementary real skew matrices X=E_ij-E_ji whose coordinates have
the same positive value s^2 of -S^2. Apply in sequence

    X <- (X-C_i X C_i)/2,  i=1,2,3;
    X <- (X-S X S/s^2)/2.                                (5)

The first three commuting conjugation projections impose anticommutation
with every C_i. The last imposes commutation with S on the specified squared-
frequency block. Since S commutes with the C_i and S^2 commutes with them,
these requirements are compatible; all projections preserve skew symmetry.
The supplied report lists24 nonzero projected elementary matrices, selected
reproducibly with seed20241024. Their SUM N is explicitly stored and satisfies

    N^T=-N,    [N,S]=0,    N C_i+C_i N=0,    rank N=128.
    ||N^-1||_F^2=31872.                                  (6)

These are full exact matrix identities, not probabilistic rank estimates.
The seeded search is only a way to obtain the witness; verification uses its
actual rational entries. Equations(3),(6) give the full formal extension(4).
This first K has11136 nonzero entries and a rank128 southeast block.

The inherited observed-core equation becomes

    partial_t phi+sum_i C_i partial_i phi+N phi=0.         (7)

For compactly supported, decaying or periodic fields on the chosen flat
observed subsystem, its positive energy integral phi^dagger P phi is
conserved. Its Fourier Hamiltonian C dot xi-iN is Hermitian and has square

    |xi|^2 I-N^2 >= (|xi|^2+1/31872) I.                  (8)

Indeed the smallest singular value of N is at least1/||N^-1||_F. This is a
rigorous gap bound, not a claim that all masses are equal or the displayed
bound is sharp. Scaling N by a nonzero real mu scales the squared gap bound
by mu^2. No physical unit or source mass scale has been selected.

## 5. A zero-southeast completion also exists

The first completion's southeast block is a choice, not a necessity. Write
Jc=[X;F], Y=[Y1;Y2], where X is the1792-row vector-spinor part. It has full
column rank; choose Ox X=I using its invertible first128-row block. Set

    B=Ox^T Y2^T,    Z=Y1-B F,
    A=Z Ox+Ox^T Z^T-Ox^T(X^T Z)Ox,
    L0=[[A,B],[B^T,0]],    K0=H^-1 L0.                  (9)

Condition(3) makes X^T Z symmetric: its antisymmetric part is exactly that
of Jc^T Y. Consequently L0=L0^T and L0 Jc=Y. H is block diagonal, so the
southeast block of K0 is zero. The exact11136-entry K0 passes

    HK0=K0^T H,    K0 Jc=D_0 Jc N,    (K-K0)Jc=0.         (10)

This preserves the zero-southeast incidence pattern. It FAILS the raw common
connection tie: infer every Omega_a from the upper-right block and reconstruct
the required raw upper-left coefficient. The first K differs in69888 entries
(witness entry(0,209)=-147/88); K0 differs in70272 entries
(witness entry(0,38)=13/18). Thus neither supplied completion has that form,
even without imposing the392-class basis restriction on the inferred Omega.
The separate checker reconstructs these defects directly from full raw
matrices. No independent barred connection is quietly attributed to the source.

Both completions transport through K2021's supplied density/degree map by
K_q=C^-1 K C. The already proved derivative terms remain mandatory. The
positive core and its observation transport as in K2022; the constant raw
mass is real new data, unlike a pure change of field coordinates. Global
spectral equivalence still requires bounded invertible multipliers and the
transported domain. This does not repair full-carrier principal Jordan growth.

## 6. Verification, contrary cases, and claim ceiling

The producer verifies all392 coefficients and exact ranks381/10/11, then
constructs and checks both full extensions and the gap. A separate checker
uses the original signed-column raw matrices and direct full multiplication,
rather than the producer's factored upper action, to reconstruct the rank
certificates and every kernel, including kernel independence, disjoint
equation blocks and full column coverage. It independently verifies both full extensions,
the old mass's failure, positive conservation, all three anticommutators and
the exact inverse-norm bound, and both raw-connection tie failures. Minor-entry perturbations test algebraic
certification; mass and raw-block perturbations test the actual equations.
Input hashes are provenance evidence, counted separately.

Strongest overclaim: the392-class obstruction excludes every massive formal
completion. Equations(4)--(10) are an explicit contrary construction. Strongest
remaining objection: the positive core is supplied and unselected, the full
carrier remains defective, and both explicit completions fail the raw common connection tie.
Weakest reproducibility seam: confusing a low-dimensional rank with all392
coefficients; the exact minor/kernel certificates and direct matrix replay
address that seam. All checks remain internal and same-author, with no external
specialist or proof-assistant certification.

SC-OP-04 **ASSERTS** candidate four-field grammar; SC-OP-05 remains
**UNCERTAIN** about its unselected southeast rival. SC-META-53 remains
**UNCERTAIN** about physical positivity; SC-META-56 **DISAVOWS** an odd-action
prerequisite. Source register, physics ledger LT-SM8/LT-GR6b and canon are
unchanged. Native2+1, observed chirality, full20, K/C and accessibility,
mirror/full-II, normal jets and interacting physical-state debts remain open.
