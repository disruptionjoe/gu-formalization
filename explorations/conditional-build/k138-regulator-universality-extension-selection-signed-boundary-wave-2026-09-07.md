---
title: "K138 regulator universality, extension selection, and signed boundary wave"
status: active_research
doc_type: conditional_matched_regulator_universality_extension_torsor_and_signed_filtration_result
created: 2026-09-07
date: 2026-09-07
claim_ceiling: exact repository-owned finite-circle theorem that matched sharp and Abel point regulators have the same complete positive-energy W_min after their own diagonal endpoint counterterms are used, while the raw counterterms differ by -2(Euler gamma+log 2)D_g; finite Hermitian subtraction changes form an affine extension torsor, full rook symmetry leaves three real parameters and only complete boundary data select W; a natural positive signed-Dirac particle/hole split preserves semibounded free energy and finite-volume Pauli/Coulomb counting but destroys K137's one-way G^5=0 filtration, so no complete signed point limit, physical extension, infinite-volume scattering/NESS, smooth unreduced parent, Weinstein/source/GU owner, Born derivation, prediction or confirmation follows
manifest: lab/process/k138-regulator-universality-extension-selection-signed-boundary-wave.json
probe: tests/channel-swings/k138_regulator_universality_extension_selection_signed_boundary_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K138 regulator universality, extension selection, and signed boundary wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) 126
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> lab/methods/source-native-comparator-routing.md and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet remains on K134--K137's repository-owned finite-circle
point control. It compares two explicit ultraviolet profiles, classifies the
finite extension ambiguity, and tests one declared positive particle/hole
representation of the signed field. It neither supplies a physical
renormalization condition nor proves the signed minimal cutoff converges.

```gu-typed-objects
result: matched sharp and Abel regulators give the same complete positive-energy W_min despite a finite raw counterterm offset; finite Hermitian subtractions form an affine extension torsor, rook symmetry does not choose its origin, and the natural signed particle/hole split loses K137's one-way nilpotent filtration
carrier: C9 tensor C512 tensor Gamma_minus of eighteen positive-dispersion l2(Z) species for regulator comparison; positive particle/hole Fock space over thirty-six l2(Z) species for the signed-boundary test LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: standard positive impurity, Klein and antisymmetric Fock Hilbert pairing; matched graph-resolvent limits and finite-dimensional Hermitian Schur boundary data ON=repository_point_extension_control
real_structure: CAR adjoint and momentum conjugation; particle and hole charges are opposite; W, the finite subtraction F and the Schur boundary matrix are Hermitian
grading: matrix units are even, Klein/CAR fields are odd and defect monomials are even; positive-only singular creation lowers the ordered impurity label, while the natural signed split creates particles and holes in opposite impurity directions
action_owner: repository-construction -- regulator profiles, renormalized boundary coordinate, finite extension, spectral polarization, sea-charge subtraction, defect split, Coulomb interval/domain and state are not selected by Weinstein's source or a GU action
target: matched-regulator universality class, finite-extension selection data, rook-symmetry commutant and signed-polarization filtration boundary MAP-TYPE=not-a-map
```

## Inline preflight bookend

K137 called its finite `W_min` scheme-dependent but did not compare two
regulators. That leaves open two opposite possibilities: an honest regulator
dependence, or a coordinate artifact caused by comparing a regulated coupling
with the wrong counterterm. The decisive comparison must therefore match each
coupling profile to its own vacuum contraction before comparing finite graph
words.

Mechanism retrieval found K132's finite subtraction-scale flow, K135's
Hermitian `W` family, K137's complete rook-graph tail ideal and no prior
matched sharp/Abel comparison. It also found K135's conditional positive
particle/hole lift but no test of K137's directed filtration after the local
signed field is split. No correction entry supersedes K132 or K134--K137.

The route census covered Abelian cutoff asymptotics, dominated convergence,
finite renormalization, boundary triples/Weyl functions, permutation
commutants, inverse spectral and scattering data, spectral Dirac
polarization, charge conjugation, CAR path filtrations, finite-volume Coulomb
forms, source ownership and hostile scope audit. Exact asymptotics and graph
orbit enumeration dominate a broad cutoff-matrix search. Computation checks
the constants, tails, commutant and signed path; it does not replace the
analytic argument.

## 1. Matched sharp and Abel regulators have the same finite limit

Keep `omega_k=sqrt(m^2+k^2)`, `m,mu>0`. Compare

```text
r_N^S(k)=1_(|k|<=N),
r_N^A(k)=exp(-|k|/N),
c_N^j(mu)=sum_k |r_N^j(k)|^2/(omega_k+mu).             (1)
```

The word **matched** means that `r_N^j` occurs both in the point coupling and
in its own diagonal vacuum counterterm `c_N^j D_g`. Since
`(omega_k+mu)^-1-k^-1=O(k^-2)`, the finite raw counterterm difference is

```text
lim_N (c_N^A-c_N^S)
 =2 lim_N[-log(1-exp(-2/N))-H_N]
 =-2(gamma_E+log 2).                                   (2)
```

This is nonzero but is not yet a regulator effect in the renormalized
operator. In every vacuum contraction the matching counterterm leaves

```text
sum_k |r_N^j(k)|^2[(omega_k+mu)^-1
                   -(omega_k+mu+X)^-1].                (3)
```

The bracket is `O((1+X)k^-2)`. Both profiles are bounded by one and converge
pointwise to one, so dominated convergence gives the same limit in (3).
K137's remaining triangle, rectangle and exchange words have one subtracted
contraction or at least two resolvent weights in every free momentum. The
same domination applies word by word, and there are only finitely many words
because the positive branch still has `G^5=0`. Therefore

```text
W_min^A(mu,E_R,g)=W_min^S(mu,E_R,g)                    (4)
```

under the canonical identification using the same renormalized boundary
coordinate. This proves universality for these two matched admissible
profiles, not for arbitrary oscillatory, unbounded or nonlocal regulators.

If the Abel coupling is instead combined with the **sharp** counterterm, the
mismatch adds

```text
lim_N(c_N^S-c_N^A)D_g=2(gamma_E+log 2)D_g.             (5)
```

Equation (5) is a finite subtraction change. Calling it regulator dependence
would compare different renormalization conditions.

## 2. Finite schemes form an affine extension torsor

Let `F` be any bounded Hermitian finite boundary term allowed by the declared
carrier and parity. Replacing the counterterm by `c_N^j D_g+F` sends

```text
W -> W+F.                                               (6)
```

If at the same time `E_R -> E_R-F`, the bare cutoff family and its limit are
unchanged. Without that compensation, (6) generically changes poles,
resolvents and spectrum. Thus the finite `W` space is affine: regulator and
subtraction coordinates do not canonically mark a physical zero.

For equal graph couplings, even granting the full automorphism group of the
three-by-three rook graph does not close the ambiguity. Its action on ordered
vertex pairs has three orbitals: equality, same row-or-column, and distinct
row-and-column. The invariant Hermitian commutant is therefore

```text
W=a I+b A_rook+c J,       a,b,c real,                  (7)
```

with eigenvalues

```text
a+4b+9c (multiplicity 1),
a+b      (multiplicity 4),
a-2b     (multiplicity 4).                              (8)
```

Symmetry reduces the unrestricted Hermitian matrix but leaves three real
parameters. One bound-state pole or one determinant zero supplies only one
scalar condition and cannot select (7). At a common nonreal `z_0`, complete
finite boundary data do select it:

```text
S_W(z_0)=S_0(z_0)+W,
W=S_phys(z_0)-S_0(z_0).                                (9)
```

An equivalent complete scattering datum could select the coupled part of
`W`, but the finite circle has discrete spectrum and supplies no
infinite-volume on-shell scattering matrix. The repository contains no
source-owned action or measured `S_phys` fixing (9).

## 3. The natural signed split preserves positivity but loses the filtration

Choose the standard spectral particle/hole representation of each signed
Dirac species. Normal order relative to the filled negative branch, set the
reference sea charge to zero, and write schematically

```text
Psi_e(0)=a_(e,+)(delta)+a_(e,-)*(delta),
H_0^pol=dGamma(omega)_particles+dGamma(omega)_holes >=0. (10)
```

If `B_e=|v><u|` changes impurity charge by `b_e=q(v)-q(u)`, give the particle
charge `b_e` and the hole charge `-b_e`. Then both
`B_e a_(e,+)` and `B_e a_(e,-)*`, together with their adjoints, are neutral.
This is one explicit representation convention, not a source-selected sea.

The positive free lower bound survives. Doubling from eighteen to thirty-six
species changes only the constant in the Pauli estimate

```text
(N_p+N_h+1)^2 <= C_36(H_0^pol+1),                      (11)
```

so K136's finite-interval cumulative-charge counting bound remains available
after opposite particle/hole charges are inserted.

The point-domain proof does **not** transfer. The singular creation part now
contains both `B_e a_(e,-)*` and `B_e* a_(e,+)*`; it raises and lowers the
impurity label. The bidirected rook graph has the distinct-edge five-step
path

```text
0 -> 1 -> 2 -> 0 -> 3 -> 4.                            (12)
```

Its CAR factors use distinct edge/polarity channels, so the matrix-unit/CAR
word is not killed by K137's label filtration. In particular, `G^5=0` no
longer follows and K137's finite inverse polynomial cannot be reused.
Equation (12) does not prove that no signed point Hamiltonian exists. It
identifies the first exact missing theorem: uniform invertibility and
convergence for the nontriangular particle/hole boundary transform, together
with its doubled endpoint counterterms and regular exchange terms.

## Inline postflight bookend

- **Strongest advance:** two explicit matched regulator families select the
  same complete positive-energy `W_min`; their nonzero raw counterterm offset
  is exactly a finite coordinate change.
- **Strongest selection result:** finite Hermitian schemes act affinely on
  `W`; even full rook symmetry leaves three real parameters. Complete Schur
  boundary data would select `W`, but no physical data or owner-native action
  presently supplies them.
- **Strongest signed result:** the positive particle/hole free and
  finite-volume Coulomb counting estimates survive, but the natural local
  signed field creates in both impurity directions and destroys K137's
  `G^5=0` proof.
- **Strongest overclaim:** “K138 proves regulator-independent physical
  uniqueness or the signed point theory.” Refused. Universality is proved
  only for the two matched bounded profiles and the signed result is an exact
  transfer obstruction, not a no-go.
- **Weakest propagation seam:** (2) can be misreported as a physical
  difference even though it disappears after matched renormalization; (11)
  can be misreported as a point-domain proof even though (12) blocks the
  finite-polynomial argument.

The companion control checks the asymptotic constant, matched subtracted and
overlap limits, rook commutant, affine shifts, and signed path boundary, with
a baseline-first hostile selftest. No uniquely physical `W`, complete signed-
Dirac point limit, infinite-volume Moller/Ruelle theory, interacting
NESS/current, smooth unreduced gauge parent, Weinstein/source/GU action, Born
rule, held-out score, prediction, confirmation, canon, paper, release or
public-posture move follows.

## Next condition

For the signed route, replace K137's finite polynomial by a proved uniform
inverse for the bidirectional particle/hole boundary transform and enumerate
the doubled endpoint counterterms and graph-domain exchange terms. A
small-norm Neumann route is only admissible if its shift/coupling dependence
is shown to be a coordinate device rather than a hidden physical restriction.
For physical selection, obtain a complete finite Schur boundary value or an
infinite-volume scattering datum from an owner-native action or measurement;
rook symmetry and one pole are insufficient. Extend regulator universality
only to a stated admissible profile class with a common domination theorem.
Thermodynamic Moller/Ruelle and return-to-NESS work remains downstream of one
selected signed point-Fock/Gauss operator and uniform volume estimates.

## Reproduction

```bash
python3 tests/channel-swings/k138_regulator_universality_extension_selection_signed_boundary_probe.py
python3 tests/channel-swings/k138_regulator_universality_extension_selection_signed_boundary_probe.py --selftest
```
