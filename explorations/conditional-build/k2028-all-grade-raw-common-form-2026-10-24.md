---
title: "K2028: All-grade raw coefficient classification and the complex repair boundary"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: complete fixed raw contraction, H and128-core coefficient classification; no changed-core, changed-form, interacting or GU-wide conclusion
scripts:
  - tests/channel-swings/k2028_all_grade_raw_common_form.py
  - tests/channel-swings/k2028_all_grade_raw_common_form_probe.py
---

# K2028: All-grade raw coefficient classification and the complex repair boundary

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
result: complete real coefficient obstruction, southeast repair and complex Hermitian scalar/vector classification
carrier: fixed K1951 raw1920 carrier and its invariant128 observed core LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: full indefinite H and inherited positive core P=8I ON=declared_full_and_core_carriers
real_structure: real128 matrices first; explicitly separate complex Hermitian branch breaks entrywise real coefficient condition
grading: Clifford monomial grades and ambient halves, independent of form degree
action_owner: repository-construction -- frozen raw contraction and common coefficient tie
target: joint common-form invariance and positive conservative core dynamics MAP-TYPE=intertwiner
```

## 1. Result and the branch that changes it

[K2024](k2024-full-odd-connection-compatibility-2026-10-24.md) exhausted392
real grade1/13 coefficients. This result allows **every real128-by128
coefficient Omega_k for all14 covector directions**, or229376 scalar
parameters, while retaining the same raw upper contraction, common H and
observed injection J.

Full common-form symmetry of the upper block leaves8388 parameters. Requiring
that upper block to preserve the fixed observed core leaves exactly **one**
parameter. Its induced core matrix has a rank128 positive-energy defect.
Thus conservation of the inherited P=8I forces **every real coefficient to
zero**, without imposing Clifford anticommutation or isotropic dispersion.
The one upper survivor also fails the uniquely H-adjoint lower return when
the southeast block is zero. A nonzero southeast block repairs that full
invariance, but still fails positive-core conservation.

A deliberate change of reality is different. Allow arbitrary complex
coefficients and require Hermitian H-adjointness and Hermitian positive-core
conservation. The real part is still zero; the imaginary part has exactly
**13 real parameters**. Nine directions act trivially on the fixed core.
The four-dimensional image is exactly

    i times span_R { I, C1, C2, C3 }.                   (1)

These are genuine compatible complex coefficients, not a numerical absence
claim. They generate scalar/vector phase and momentum shifts, not an
isotropic mass. No member supplies a globally gapped constant-coefficient
Fourier Hamiltonian on the whole R^3 momentum space.

This is a fixed-construction result, not a falsification of GU or of every
source connection. The explicit complex branch prevents promoting the real
zero-only result to all coefficients. The new real classification prevents
repeating higher-grade real searches under the unchanged conditions.

## 2. Frozen object and structural reduction

Use the original real K77 gamma matrices gamma_k, signatures eta_k, volume
v=gamma_0...gamma_13 and W=(3I-v)/2. Let B=gamma_7...gamma_13. Direct exact
matrix identities give B^T=B, B^2=I and gamma_k^T B=-B gamma_k. Write
X*=B X^T B. The common full form is diag(eta_0 B,...,eta_13 B,B).

For a!=c the raw upper coefficient is

    K_ac = eta_a gamma_a sum_(k!=a,c) gamma_k gamma_c W Omega_k,
    K_aa = 0,                K_a,zero = Omega_a.       (2)

No freely fitted replacement of this contraction is used. Set

    A_k=W Omega_k=eta_k gamma_k Y_k,
    Omega_k=W^-1 eta_k gamma_k Y_k,
    W^-1=(3I+v)/4.                                     (3)

Upper H-self-adjointness is equivalent to

    sum_(k!=a,c) [Y_k* gamma_a gamma_c-gamma_a gamma_c Y_k]=0.
                                                               (4)

Expand Y_k in all16384 ordered Clifford monomials Gamma_I. Their signed
Pauli characters are distinct and trace-orthogonal, hence form a basis of
M128(R). For degree r,

    Gamma_I*=sigma_r Gamma_I,  sigma_r=(-1)^(r(r+1)/2),
    Gamma_I gamma_a gamma_c = chi_I(a,c) gamma_a gamma_c Gamma_I,
    chi_I(a,c)=(-1)^(1_(a in I)+1_(c in I)).

Therefore each monomial sector is an independent14-variable system:

    sum_(k!=a,c) y_k=0 whenever sigma_r chi_I(a,c)=-1.  (5)

A permutation of the index set makes its rank depend only on r. The complete
real table is

| r | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| kernel per monomial |14|1|1|1|1|0|0|1|1|0|0|1|1|1|0|

Weighting by binomial(14,r) gives8388. The report stores each small exact
kernel. This reduction covers all grades before the core calculation, rather
than selecting a successful-looking grade subset.

The standard ordered-monomial construction can also be found in the
[Sage Clifford algebra documentation](https://doc.sagemath.org/html/en/reference/algebras/sage/algebras/clifford_algebra_element.html).
The actual representation, adjoint signs, reduction and ranks here are
checked directly; that reference does not certify them.

## 3. Complete core test and the only real survivor

The frozen K1951 objects obey D_k J=D_0 J C_k in the three observed spatial
directions, with core energy P=8I. The zero-form block F=J_zero is invertible.
In coordinates normalized by F, every gamma and J block is a monomial matrix.
Consequently the8388 columns split into128 disjoint row-permutation blocks,
with at most84 columns each. No dense229376-variable rank search is needed.

For every basis coefficient compute the original upper action KJ. The time
upper block determines the only possible M. Impose the remaining upper
identities KJ=D_0 J M and then PM+M^T P=0. Selected integer minors modulo101
are nonsingular in every block. A nonzero modular determinant of an integer
minor proves nonzero rational, hence real, determinant; this is an exact
rank certificate, not a probabilistic rank estimate. The separate checker
rebuilds all8388 columns through the original D_k(Omega_k J), using a
different ordering and scaling, and checks the corresponding minors also
modulo103. Exact kernels and equation-block coverage prove completeness.

Without the energy equations the upper kernel is one-dimensional. A convenient
normalization has

    Y_k=y_k I,
    y_k=1          for k in {0,7,8,9},
    y_k=198/1043   otherwise.                          (6)

This reproduces the earlier1043/198 scalar ratio as the **entire all-grade
upper survivor**, rather than assuming that scalar ansatz complete. Its
energy defect PM+M^T P has rank128. The complete combined system has rank8388
and zero kernel.

For a fully H-self-adjoint coefficient with zero southeast block, the lower
row is forced to be eta_k B Omega_k^T B. Its action on J differs from the
required lower return by rank128. Thus even without positive energy the
nonzero upper survivor cannot preserve the full core with southeast zero.

There is a concrete admissible repair of this latter condition: the unique
southeast block restoring full core invariance is

    E_SE = -1989/1639 I.                               (7)

It is B-self-adjoint and has rank128. The report and separate raw matrix
replay verify the full return, not just symmetry of(7). Its energy defect
remains rank128. This separates the southeast-zero obstruction from the
stronger positive-core obstruction and respects SC-OP-05's unselected rival.

Allowing an arbitrary southeast block cannot repair positive conservation:
the upper equations already force Omega=0 and M=0. Full invariance then gives
E_SE F=0; invertibility of F forces E_SE=0. No assumption about an isotropic
mass was used in this conclusion.

## 4. Complex Hermitian coefficients: actual repair, limited payoff

For complex Omega=U+iV, Hermitian H-self-adjointness separates into real
H-self-adjoint U and real H-anti-self-adjoint V. Positive-core conservation
similarly requires the real induced matrix skew and the imaginary induced
matrix symmetric in P. The real part is settled by section3.

For V, replace the condition in(5) by sigma_r chi_I(a,c)=+1. The common-form
space has8232 dimensions. Rebuilding the raw upper invariance and symmetric
core conditions gives rank8219, hence dimension13. The forced negative
H-adjoint lower row preserves the core for all13 directions with southeast
zero. Their induced matrices have rank4 as a linear map; its kernel has
dimension9. The report gives the complete13 coefficient directions through
exact kernels, all13 induced matrices and their coordinates in(1).

The separate checker reconstructs every one of the8232 raw columns, verifies
127 disjoint blocks, exact kernel annihilation and full-rank minors, and
checks every full lower-return identity. These are exhausted linear spaces,
not13 examples offered as a classification.

For constant coefficients, the core equation is

    partial_t phi+sum C_j partial_j phi
      + i(a0 I+sum a_j C_j)phi=0.

Its Hermitian Fourier Hamiltonian is

    H(xi)=a0 I+sum C_j(xi_j+a_j),
    eigenvalues a0 +/- |xi+a|.                         (8)

The Clifford identities and trace controls hold on the actual128 core.
The spectrum over all xi in R^3 covers the real line, so there is no global
spectral gap. Equivalently the scalar phase
exp[-i(a0 t+sum a_j x_j)] removes these constant coefficients locally on
R times R^3. On compact domains that phase need not preserve boundary
conditions, so global holonomy is not declared trivial.

Nor can an isotropic mass be hidden in(1): anticommuting with every C_j
forces all a_j=0 by tracing the anticommutators, then a0=0. Nonconstant
coefficients can have nonzero curvature and need a separate domain/dynamics
analysis; neither GU electromagnetism nor a physical gauge selection follows.
Entrywise real coefficients exclude this imaginary branch. The source has
not selected that extra reality restriction here.

### Smooth potentials and the exact remaining consumer

The coefficient equations are pointwise and linear. A fixed right inverse of
the rank4 image map therefore lifts arbitrary smooth real functions a_mu(x)
to compatible imaginary raw coefficients. The nine invisible functions
remain arbitrary and contribute zero to the fixed core equation. No derivative
of those coefficients occurs in the zeroth-order connection action.

For smooth core solutions the exact local identity is

    partial_t(phi^dagger P phi)
      +sum partial_j(phi^dagger P C_j phi)=0.

This is local current conservation; it does not by itself establish a global
closed operator domain. The scalar change phi=exp(-i chi)psi replaces
 a_mu by a_mu-partial_mu chi. Hence the six curvature components
f_mu_nu=partial_mu a_nu-partial_nu a_mu are gauge invariant. Exact polynomial
controls verify this on all six pairs, while the argument holds for arbitrary
smooth coefficients. For instance a_2=B x_1 with B nonzero has f_12=B and
cannot be removed by a scalar phase, unlike the constant coefficients in(8).
This is an actual surviving variable-potential construction, not a mass or a
claim that every compatible coefficient is physically trivial. Its fields,
charge normalization, interacting action and physical interpretation are
supplied, not source-selected. The full carrier's principal Jordan problem
is unchanged.

## 5. Consequences, source boundaries and review

The [K2026 freely completed masses](k2026-compatible-mass-moduli-2026-10-24.md)
remain valid. The new result proves that no nonzero member of their isotropic
mass class comes from this fixed raw common-coefficient construction, even
in the complete complex Hermitian branch. That conclusion uses the original
raw tie; it is not the earlier failure of two sample free completions.

A common invertible change of field coordinates, density or degree duality
cannot evade these pointwise compatibility equations if the operator,
common form, injection and energy are all transported together. Conjugating
a difference of zeroth-order coefficients is injective. Moving-frame
connection terms are part of that coordinate transport, not automatically
an additional mass. Changing H, the contraction, the selected core or the
physical constraints is a different construction, still open for testing.

SC-OP-04 ASSERTS candidate four-field grammar, not this fixed realization's
uniqueness. SC-OP-05 is UNCERTAIN about the unselected southeast rival.
SC-META-53 is UNCERTAIN about physical positivity, and SC-META-56 DISAVOWS
an odd-action prerequisite. LT-SM8/LT-GR6b remain unchanged: no action-owned
physical selector, interacting quotient, global analytic domain or physical
GU result is supplied. The full principal Jordan defect also remains.

Hostile review found two overextensions worth testing directly: southeast
zero is not compulsory, and real-coefficient failure need not extend to
complex Hermitian coefficients. Equations(7),(8) retain those repairs and
show exactly what they buy. The reproducibility risk is missing coefficient
sectors or trusting numerical rank; complete monomial coverage, exact
minors and a separate raw-action reconstruction address it. Four actual
matrix/basis/minor faults and one omitted phase-connection term are rejected
after passing baselines. Provenance
hashes are separate evidence. All checks are same-author internal verification,
not external specialist, proof-assistant or novelty certification.

The next source-facing question must change a load-bearing input or construct
an action-owned stable-core constraint. More real Clifford grades, another
constant complex coefficient, or another free isotropic mass under the same
raw tie would repeat an exhausted question. Full20, K/C, accessibility,
mirror/full-II, normal jets,2+1 and observed chirality remain separate debts.
