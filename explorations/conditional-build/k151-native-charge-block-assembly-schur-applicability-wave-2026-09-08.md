---
title: "K151 native charge-block assembly and Schur-applicability wave"
status: active_research
doc_type: conditional_native_hard_core_finite_regulator_charge_block_symmetry_and_schur_applicability_result
created: 2026-09-08
date: 2026-09-08
claim_ceiling: exact repository-owned finite-regulator assembly and applicability theorem for the equal-coupling two-edge native hard-core signed point control: canonical exterior-algebra occupation bases give exact rational matrices in every conserved two-charge sector, signed flavor swap exactly intertwines exchanged sectors while two-flavor particle-hole complement fails to preserve the native carrier, and the bare point tail violates K150's bounded off-diagonal hypothesis so native lower enclosure must use a form-level route; no numerical native spectrum, complete threshold or Gram margins, full-Fock scattering, NESS/current, physical selector, source/GU action, Born derivation, prediction or confirmation follows
manifest: lab/process/k151-native-charge-block-assembly-schur-applicability-wave.json
probe: tests/channel-swings/k151_native_charge_block_assembly_schur_applicability_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K151 native charge-block assembly and Schur-applicability wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet keeps K148's equal-coupling two-edge corner, positive
particle/hole polarization, `m=1`, self-energy `1/4`, `W=0` and hard-core
three-state impurity. It serializes the exact algebraic finite-regulator
charge blocks and decides whether their raw omitted-mode coupling can satisfy
K150's continuum bounded-block hypothesis. A cutoff matrix is not the native
singular-IBC spectrum.

```gu-typed-objects
result: exact finite-mode native-C3 charge-block matrices and signed flavor intertwiners, plus a proof that the bare point tail is not a cutoff-uniform bounded Schur block and therefore requires the predeclared form-level lower-certificate route
carrier: the hard-core subspace n1*n2=0 of Lambda(C2_impurity direct-sum C^(4M)_bath), decomposed by (q1,q2), with M finite regulator modes and eventual K139 singular-IBC form limit LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive exterior-Fock Hilbert pairing at finite M; native continuum meaning belongs to K139's closed semibounded boundary form, not the raw matrix sequence ON=repository_signed_point_control
real_structure: canonical CAR adjoint in one global orbital order; flavor swap is a signed exterior permutation, while simultaneous impurity particle-hole complement leaves the native C3 subspace
grading: q_i=n_i+N_(i,+)-N_(i,-), hard-core n1*n2=0 and combined exterior parity
action_owner: repository-construction -- regulator, finite mode data, graph, polarization, extension, couplings, state and probability interface are not selected by Weinstein's source or a GU action
target: charge-block serialization, exact symmetry transport and K150 bounded-Schur applicability decision MAP-TYPE=intertwiner
```

## Inline preflight bookend

K150 supplied a trustworthy exact rational certificate only after an
operator-specific proof provides `D>=d` and `||B||^2<=beta^2`. Its next
condition proposed assembling those inputs for K148's native corner. Before
doing so, one must distinguish three matrices: a finite bare regulator, a
conforming matrix of the transformed boundary form, and the full singular IBC
operator. Only the second can become a native Ritz upper input, and only a
cutoff-uniform full-block estimate can become K150's `beta^2`.

Mechanism retrieval found K139's resolvent-dressed Neumann chart, K146's
one-flavor Nambu interaction, K148's hard-core compression, K149's monotone
penalty/form convergence and K150's bounded Schur contract. It found no
serialized two-charge occupation basis, exact signed flavor intertwiner or
proof that a raw low/tail split is Hilbert bounded. No correction entry
supersedes those inputs.

The route census covered exterior-Fock occupation bases, Jordan--Wigner/CAR
signs, charge-block Jacobi matrices, finite-`U` Anderson controls, flavor and
particle-hole symmetries, K139 boundary-chart pullback, Schur complements,
Temple bounds, Lehmann--Goerisch enclosures and form residual methods. Exact
block assembly and the ultraviolet norm discriminator were selected because
the latter decides whether K150 is even the right lower-bound interface.

## 1. Exact native-C3 finite-mode charge blocks

Order the finite exterior one-particle orbitals as

```text
d_1,d_2;
(1,+,0),...,(1,+,M-1),(1,-,0),...,(1,-,M-1);
(2,+,0),...,(2,+,M-1),(2,-,0),...,(2,-,M-1).          (1)
```

Canonical wedge order fixes every CAR sign. Retain only bit strings with
`n_1 n_2=0`; their impurity factor is exactly `|0>,|1>,|2>`, not the
auxiliary double state. In a rational finite regulator with energies
`epsilon_j>0` and real coefficients `g_j`, assemble

```text
H_M=sum_(i,j) epsilon_j(N_(i,+,j)+N_(i,-,j))
   +sum_(i,j) g_j[d_i* a_(i,+,j)+a_(i,+,j)* d_i
                  +d_i* a_(i,-,j)*+a_(i,-,j)d_i].     (2)
```

Every term in (2) preserves

```text
q_i=n_i+N_(i,+)-N_(i,-),  i=1,2.                     (3)
```

Enumeration by (3) therefore gives a finite exact symmetric rational matrix
`H_(M,q)` with an auditable occupation label for every row. Restoring the
double state and adding `U n_1n_2` produces the finite-`U` K149 control; its
principal compression to `n_1n_2=0` is exactly (2). This closes the missing
charge/CAR combinatorics, but not the continuum boundary-form entries.

For the one-mode control `epsilon=5/4`, `g=1`, the dimensions and exact
inertias `(negative,zero,positive)` are

```text
q=(0,0): dim 8, inertia (1,0,7)
q=(1,0): dim 7, inertia (1,0,6)
q=(0,1): dim 7, inertia (1,0,6)
q=(1,1): dim 5, inertia (0,0,5).                       (4)
```

Equation (4) is a regulator/sign positive control. It is not a table of native
residual energies and earns no threshold ordering.

## 2. The exact symmetry is flavor swap, not particle-hole complement

Let `S` exchange `d_1<->d_2` and every corresponding particle and hole mode.
On a wedge basis its coefficient is the parity of the induced permutation of
occupied orbitals. Thus the generated matrix `S_q` is signed, not an unsigned
row relabeling. Exact multiplication gives

```text
S_q* S_q=I,
H_(M,(q_2,q_1)) S_q = S_q H_(M,(q_1,q_2))             (5)
```

for equal flavor data. Consequently `(1,0)` and `(0,1)` form one certified
orbit; `(0,0)` is its own representative. These are the two finite-control
representatives to compute first. The tempting simultaneous particle-hole
complement is not a native symmetry: it sends impurity vacuum `|0>` to the
excluded double state `|12>`. The phrase “equal coupling” cannot replace (5),
and no unproved particle-hole relation may reduce the charge census.

## 3. The raw point tail fails K150's bounded-block hypothesis

Let `P_M` retain finitely many momentum modes. Acting from the bath vacuum,
the omitted part of one bare point creation field has norm square

```text
||(1-P_M) a*(delta) Omega||^2
   = sum_(k omitted) |g_k|^2.                          (6)
```

For K139's point form factor the Fourier coefficients do not decay. The
finite-cutoff lower bound in (6) grows linearly with the number of newly
included constant-coefficient modes and diverges in the limit. Hence the raw
low/tail off-diagonal block is not bounded in Hilbert norm, and no finite
sample `beta_M^2` is a cutoff-uniform `beta^2` for K150.

K139 proves something different and essential:

```text
(epsilon+lambda)^-1 delta is in l2,
G_lambda=-(H_0+lambda)^-1 C* is bounded,                (7)
```

so a resolvent-dressed boundary inverse exists. The regular terms after this
domain transform are controlled relative to the free-operator graph. Neither
(7) nor graph-relative boundedness implies that the raw `PH(1-P)` in K150 is
a bounded Hilbert-space operator. Feeding a finite `beta_M` to K150 would
therefore certify the wrong operator.

This is a negative applicability result for one certificate interface, not a
failure of the IBC construction. K150 remains valid whenever its hypotheses
are supplied; the native point model does not supply them in the raw split.

## 4. The honest K149--K150 bridge

The exact assembler has three legitimate uses now:

1. verify charge conservation, hard-core compression, CAR signs and flavor
   orbits at every finite regulator;
2. generate exact finite-`U` and native-C3 algebraic controls whose inertia can
   be checked by K150's exact finite-matrix kernel; and
3. specify row/column identities for a later conforming matrix of K139's
   transformed closed form.

It does not yet generate a native conforming transformed Ritz matrix, a
continuum complement floor or a projection residual. The lower side must now
follow K150's predeclared switch: formulate a Lehmann--Goerisch or equivalent
quadratic-form enclosure on the common K139 boundary domain, or certify the
finite-penalty lower values in K149 directly. The required data are form
matrices, comparison operator, residual functionals in the form dual, and a
proved exterior form gap. A bounded raw `B` is no longer an admissible target.

## Inline postflight bookend

- **Strongest construction:** every finite regulator now has an exact,
  reproducible native-C3 matrix in every conserved two-charge block, with all
  Klein/CAR signs fixed by one exterior ordering.
- **Strongest symmetry result:** signed flavor permutation proves the only
  presently certified charge orbit; simultaneous particle-hole complement
  fails the native-carrier test already on the vacuum.
- **Strongest route discriminator:** the bare point tail has divergent norm,
  so K150's raw bounded-block Schur hypothesis cannot be supplied by cutoff
  sampling or by citing K139's resolvent-dressed chart.
- **Strongest contrary route:** finite-cutoff diagonalization remains useful
  for exact combinatorics and upper/form approximants, but it cannot provide a
  continuum lower bound without the form-level certificate.
- **Strongest overclaim:** “K151 computed the native ground charges or first
  thresholds.” Refused. Equation (4) is a one-mode control only.
- **Weakest reproducibility seam:** the assembler fixes an explicit global
  exterior ordering. Any alternate Klein convention must provide its signed
  unitary conjugacy before matrices are compared entrywise.

The companion probe checks the exact CAR algebra, charge preservation,
hard-core compression, finite-sector dimensions and inertias, signed flavor
intertwiners, particle-hole failure, ultraviolet divergence and claim fences.
It uses a baseline-first hostile mutation harness. No numerical native
spectrum, complete threshold/Gram margins, strict full-Fock Mourre/scattering,
NESS/current, physical/source selection, Born rule, held-out score,
prediction, confirmation, canon, paper, release or public-posture movement
follows.

## Next condition

Construct a form-level lower-enclosure kernel on K139's transformed common
boundary domain. Serialize exact or outward-certified form matrices for the
`q=(0,0)` and `q=(1,0)` representatives, use (5) for `(0,1)`, and prove an
exterior form gap and dual residual bound suitable for a Lehmann--Goerisch or
certified penalty-form inequality. Only after those lower enclosures close may
K149 propagate native cluster projections into threshold order and complete
Gram ranks. Do not seek a cutoff-uniform raw Hilbert coupling norm again.

## Reproduction

```bash
python3 tests/channel-swings/k151_native_charge_block_assembler.py --demo
python3 tests/channel-swings/k151_native_charge_block_assembly_schur_applicability_probe.py
python3 tests/channel-swings/k151_native_charge_block_assembly_schur_applicability_probe.py --selftest
```
