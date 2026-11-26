---
title: 'Quantitative escape of observer distributions at Weyl degenerations'
status: exploration
doc_type: structural-result
created: '2026-11-26'
program_target: LB-CLASS
tier: T1
expected_delta: Classify continuous Weyl-only observer probabilities and quantify degeneration beyond fixed-orbit normalization.
actual_delta: Every type-I approach to nonzero II or III forces at least one-half or three-quarters probability escape from each compact observer region; continuous laws have maximal covariance defect along escaping stabilizers.
class_covered: Pointwise four-dimensional Lorentz Weyl tensors with fixed metric, orientation and time orientation; arbitrary normalized Borel probabilities on future unit timelike vectors. Ambient invariant open domains for the continuity classification.
premises:
- Classical Weyl-spinor and binary-quartic identification; exact SL2C action, not quartics modulo complex scale.
- Classical proper Lorentz action on hyperbolic observer space; weak probability topology, no moment assumption.
- SC-GEO-03 supplies Met(X), not a Weyl-only probability selector; SC-META-52/53 remain uncertain.
source_bridge:
  status: absent
  reason: Neither source necessity of a pointwise Weyl-only clock law nor its identification with physical observation or metric-fibre normalization is established.
kill_condition: Exclude continuous Lorentz-equivariant observer-probability laws on invariant ambient open neighborhoods containing algebraically special Weyl tensors, not GU or class C.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
internal_target: INTERNAL-WEYL-ONLY-CONTINUOUS-OBSERVER-LAW
internal_target_verdict: excluded across algebraically special strata under the stated assumptions
canon_verdict_change: none
---

# Quantitative escape of observer distributions at Weyl degenerations

**Mathematical result:** arbitrary type-I sequences approaching nonzero type II
or III force the compact-region mass of any covariant observer law to at most
one-half or one-quarter, respectively. These constants are attained along suitable
sequences. No moment, density, principal-observer or energy-minimization
assumption is needed.

**Novelty ceiling:** a quantitative formulation/refinement candidate, not a
certified world-first. The positive type-I selector is the classical Julia
covariant. General proper-action and barycenter arguments are established tools.
The potential contribution is the universal, sharp degeneration mass bound and
the maximal total-variation consequence. See §7 for the closer prior art that
narrowed the initial chat-level originality claim.

```yaml
program_target: LB-CLASS
tier: T1
expected_delta: Classify continuous Weyl-only observer probabilities and quantify degeneration beyond fixed-orbit normalization.
actual_delta: Universal II/III compact-mass bounds, sharp examples and maximal-TV covariance defect; source necessity absent.
```

```gu-typed-objects
result: Quantitative escape of observer distributions at Weyl degenerations
carrier: real four-dimensional Weyl curvature tensors encoded by binary quartics and future unit timelike vectors LAYER=observed BRIDGE=none CHIRALITY=N/A
pairing: fixed four-dimensional Lorentz metric ON=real_tangent_space; normalized positive Borel probabilities on H3
real_structure: real ten-dimensional Weyl tensor space identified with complex binary quartics; proper orthochronous Lorentz group
grading: none; no ambient or observed fermion grading
action_owner: repository-construction mathematical comparator; no physical action selected
target: continuous Lorentz-equivariant probability assignment MAP-TYPE=intertwiner
```

## 1. Scope and definitions

Let `V = Sym^4(C^2)` be viewed as a real ten-dimensional vector space of
four-dimensional Weyl spinors. Use the **left** action

\[
 (\rho(g)f)(z)=f(g^{-1}z),\qquad g\in SL_2(\mathbb C).
\]

The center acts trivially, so the effective group is
`G = PSL2(C) = SO+(3,1)`. Stabilizers preserve the actual quartic, not merely its
root set or its complex line. The observer space is
`H3 = {positive Hermitian 2x2 matrices of determinant 1}`, with action `X -> gXg*`.
It is the space of future unit timelike vectors. Its group action is proper:
the transporter of two compact sets is compact, since `H3 = G/PSU(2)`.

A law is a map `P: U -> Prob(H3)` with
`P(g f) = g_* P(f)`. Continuity means weak convergence against bounded continuous
functions. `U` is an invariant **open subset of the ambient Weyl tensor space**.
No global spacetime, equations of motion, finite moments or absolutely continuous
densities are assumed. Bounded rapidity regions are compact in H3; ordinary
three-velocities being below light speed is not a compactness condition.

Petrov I has four distinct projective roots; II has multiplicities `(2,1,1)`,
III `(3,1)`, D `(2,2)`, N `(4)`, and O is zero.

## 2. Exact finite stabilizers

### Lemma 2.1: the type-I Klein group

Every type-I quartic has an exact projective Klein-four stabilizer subgroup.
The three root double-transpositions are Möbius involutions and form this
subgroup. For each involution, its two fixed points are not roots. In an
eigenbasis the roots occur in opposite pairs, so the quartic has only the terms
`x^4`, `x^2 y^2`, `y^4`. The determinant-one lift `diag(i,-i)` fixes each term
under the stated action. Thus the involutions fix the actual quartic, not merely
its roots. Additional root-set symmetries of special type-I configurations are
not needed; preserving the root set alone is insufficient for exact invariance.

Every nonidentity element of this subgroup has trace-zero determinant-one
lifts, which square to `-I`. Such elements cannot converge projectively to the
identity: lifts near it have trace tending to `2` or `-2`.

### Lemma 2.2: the limiting stabilizers

A type-II form can be put into
`f = alpha x^2 y^2 + beta x y^3`, with `alpha beta != 0`.
Its exact projective stabilizer has order two. The double root must be fixed;
the two simple roots can only be fixed or exchanged. The exchange exists, with
lift

\[
 M=\begin{pmatrix}-i&-i\beta/\alpha\\0&i\end{pmatrix},
 \qquad M^2=-I,\qquad \rho(M)f=f.
\]

For type III, `f = beta x y^3`, multiplicities force both roots to be fixed.
The lift is diagonal, and exact invariance forces it to be `+I` or `-I`.
The projective stabilizer is therefore trivial. This calculation is not a
statement about the larger stabilizer of the quartic's projective line.

## 3. Universal probability escape

**Theorem 3.1.** Let `f_n` be any sequence of type-I quartics converging to a
nonzero type-II or type-III quartic `f`. Choose an exact Klein-four subgroup
`H_n` of each stabilizer. For **any** `H_n`-invariant probabilities `mu_n` and
every compact `K` in H3, eventually

\[
 \mu_n(K)\le
 \begin{cases}
 1/2,& f\text{ has type II},\\
 1/4,& f\text{ has type III}.
 \end{cases}
\]

No continuity of the laws is required. In particular the statement holds for
every equivariant assignment, even a merely set-theoretic one.

**Proof.** Put `m=2` or `1` according to the limiting type. For nonempty compact
`K`, let `C_K = {g: gK intersects K}`, a compact transporter. Eventually
`|H_n intersect C_K| <= m`. Otherwise select `m+1` distinct bounded group
elements and take simultaneous convergent subsequences. Their limits stabilize
`f`. They remain distinct: a quotient of two distinct elements is a nontrivial
Klein involution and cannot tend to the identity by Lemma 2.1. This would give
more than `m` exact stabilizers of `f`, contradicting Lemma 2.2.

Each point belongs to at most `m` of the four translates `hK`, `h in H_n`.
Indeed, if it belongs to translates indexed by `h_1,...,h_r`, then all distinct
`h_1^{-1}h_j` belong to `H_n intersect C_K`. Integrate the multiplicity bound:

\[
 4\mu_n(K)=\int\sum_{h\in H_n}1_{hK}\,d\mu_n\le m.
\]

The empty `K` case is immediate. This proves the bounds. QED.

The same argument is a general stabilizer-degeneration principle: a finite
subgroup of order `q` whose distinct elements cannot coalesce, converging to a
parameter with at most `m` exact stabilizers, permits at most `m/q` probability
in each fixed compact target region when the target action is proper. The
uniform no-coalescence condition is essential, not an automatic property of
arbitrary changing finite groups.

### Sharpness

For III use `f_t = x y^3 + t^{-2} x^3 y`, `t>0`. Exact stabilizer lifts are

\[
 J_t=\begin{pmatrix}0&it\\i/t&0\end{pmatrix},\quad
 A_t=\frac1{\sqrt2}\begin{pmatrix}i&-t\\t^{-1}&-i\end{pmatrix},\quad
 B_t=\frac1{\sqrt2}\begin{pmatrix}i&t\\-t^{-1}&-i\end{pmatrix}.
\]

Their determinants are one, their squares `-I`, and `A_t B_t=J_t`,
`B_t A_t=-J_t`. Each fixes `f_t`; all three and all their nonidentity pairwise
quotients escape compact subsets of G. Averaging a fixed observer's point mass
over the four-element group leaves exactly one-quarter of the mass in any
sufficiently large fixed compact region containing that observer, eventually.

For II take `f_e = e x^4 + x^2 y^2 + y^4`, with positive `e -> 0` and `e<1/4`.
These are type I, and the limit is type II. The fixed projective involution
`R = diag(i,-i)` belongs to their Klein group. It fixes the observer `o=I` in H3.
The other two involutions escape: otherwise their limits, separated from `I`
and `R` by Lemma 2.1, would give an extra stabilizer of the limit. Averaging
`delta_o` over the group retains exactly one-half of its mass near `o`.

These are sharp examples among stabilizer-invariant laws. They do not claim
that every degeneration attains its upper bound, or that each such family is
already a globally prescribed physical probability law.

## 4. Continuous laws have maximal covariance defect

**Theorem 4.1.** Along every sequence in Theorem 3.1, let `mu_n` converge weakly
to a probability `mu`. There is a choice of exact stabilizers `h_n in H_n`
escaping all compact subsets of G, and

\[
 d_{TV}(\mu_n,(h_n)_*\mu_n)\longrightarrow1,
 \qquad d_{TV}(\mu,\nu)=\sup_A|\mu(A)-\nu(A)|.
\]

**Proof.** An escaping choice exists by the compactness contradiction above:
choose an element of `H_n` of maximal value of a proper exhaustion function on
G. If those maxima had a bounded subsequence, all four elements would converge
to four distinct limiting stabilizers. For III, any nonidentity choices escape.

Weak convergence gives uniform tightness. Given `epsilon>0`, choose compact
`K,L` each carrying at least `1-epsilon` of every sufficiently late `mu_n`.
Properness gives `h_n L intersect K = empty` eventually. Therefore
`(h_n)_*mu_n(K) <= epsilon`, whereas `mu_n(K) >= 1-epsilon`.
The TV distance is at least `1-2 epsilon` and at most one. QED.

This is a failure of covariance under **unbounded Lorentz transformations**.
It does not imply an obstruction to approximate covariance restricted to a fixed
compact set of boosts. The unnormalized variation norm would tend to two.

## 5. Exact open-domain classification

**Corollary 5.1.** A continuous equivariant `P: U -> Prob(H3)` on an invariant
ambient open `U` exists iff `U` consists entirely of type-I quartics.

At II/III, openness admits type-I sequences and continuity would give tightness,
contradicting Theorem 3.1. At D/N/O the failure is already pointwise: their exact
stabilizers contain respectively a noncompact diagonal group, an upper-triangular
unipotent group (for `y^4` under our action), or all of G. A probability on a
proper G-space has compact stabilizer. To see this, take compact `K` with mass
greater than one-half; every measure-preserving `g` lies in `C_K`.

For sufficiency use the **classical Julia covariant**, recalled here for
completeness. Four distinct future null rays have representatives `n_j`; on H3,

\[
 F(u)=\sum_{j=1}^4\log[-g(u,n_j)].
\]

Changing a representative's scale adds a constant. Each summand is a Busemann
function with Hessian `g_H - db_j tensor db_j`. The sum is strictly convex:
equality in a tangent direction would place all four endpoints at the two ends
of one geodesic. Relative to a fixed observer, normalize the four null vectors.
Their angular separation ensures at most one lies near any boost direction;
three summands are bounded below by `r-C`, the remaining one by `-r`.
Thus `F >= 2r-C`, so a unique minimizer exists. Its positive Hessian and local
smooth dependence of distinct roots give smooth dependence on the quartic;
the symmetric sum removes root-label monodromy. The minimizer is equivariant,
and its point mass is the required probability law.

This construction is established mathematics, not a new selection method.
Type II/III can admit equivariant laws on isolated orbits: compact/trivial
isotropy permits averaging over the stabilizer. The theorem excludes their
continuous extension through an **ambient open neighborhood**.

## 6. Three-state interpretation and source custody

| State | Exact claim |
|---|---|
| ESTABLISHED | The stated probability escape, TV limit and open-domain classification; reviewed written proofs plus the separately scoped finite certificates. |
| RULED OUT | Continuous Lorentz-equivariant, pointwise Weyl-only observer probability on an ambient open domain containing special Petrov types. |
| NOT MODELED / UNDETERMINED | Whether source GU requires any such law; its physical observer/quantum-state meaning; dynamics; curvature derivatives, Ricci or matter input; boundary/global data; source-selected predictions; worldwide priority. |

This extends the existing [tensor-stabilizer normalization](tensor-stabilizer-normalization-2026-11-25.md)
only at its expressly open **cross-stratum continuity** seam. Compact isotropy
still suffices for the old fixed-orbit question. The
[symmetry-restoration result](symmetry-restoration-measure-limit-2026-11-25.md)
treated a fully Lorentz-fixed limit, not the finite-isotropy II/III limits here.

SC-GEO-03 asserts `Y=Met(X)`; SC-META-52/53 leave analytic and physical-positivity
ownership uncertain. None supplies a pointwise Weyl-only timelike clock law.
SC-OP-03's displayed Shiab kills **ambient** Weyl curvature and retains
Ricci/scalar analogues: that is a different decomposition, not a bridge to this
four-dimensional theorem. Source register: [claim custody](../../lab/sources/source-claim-register.yaml).

GVP T01/T02/T04/T13/T15/T16 apply: downstairs Lorentz geometry is neither K95
nor K77; no ambient spinor-frame reduction, observation contraction, physical
pairing or probability is identified. This theorem says nothing about source
`2+1`, observed chirality or integer counts. It is not a source-required class-C
exclusion. The weakest unproved link is **source necessity of the tested law**.

Metric-fibre probability is a different target. A transfer would need an explicit
continuous equivariant construction into observer probabilities or other proved
support hypotheses. Singular `delta_g`/conformal-ray metric laws, Ricci clocks,
matter/derivative input and restricted domains remain outside this result.
No new candidate choice, obligation, prediction or ledger verdict is adopted.

## 7. Primary literature and originality audit

1. **Stoll and Cremona, _On the reduction theory of binary forms_ (2003),
   Proposition 3.4 and §§4–5.** [Author PDF](https://www.mathe2.uni-bayreuth.de/stoll/papers/reduction-part-1.pdf).
   The complex squarefree quartic covariant into H3 is already unique; the stable
   binary-form minimizer and root-direction interpretation are classical Julia
   reduction. The discussion after Corollary 5.4 also treats repeated-root
   boundary behavior. This is the closest precedent for §5, which earns no
   independent novelty credit here.
2. **Douady and Earle, _Conformally natural extension of homeomorphisms of the
   circle_ (1986).** [DOI](https://doi.org/10.1007/BF02392590).
   For H3/S2 specifically see also [DeMarco, §8](https://people.math.harvard.edu/~demarco/M2.pdf)
   and [Cantarella–Schumacher](https://arxiv.org/abs/2004.03958).
   Conformal barycenters are established machinery. Mixing the visual boundary
   probabilities of observers gives a nonatomic boundary probability; its
   barycenter provides a continuous equivariant reduction from observer
   probabilities to an observer, without moments. This further limits the
   originality of the qualitative randomization statement.
3. **Wylleman, Costa and Natário, _Poynting vector, super-Poynting vector, and
   principal observers_ (2021).** [Primary text](https://arxiv.org/abs/2007.15384).
   Principal/rest observers are already classified and type-I uniqueness is
   known. Our probabilities need not be supported on principal observers.
4. **Dym, Lawrence and Siegel, _Equivariant Frames and the Impossibility of
   Continuous Canonicalization_ (2024).** [Proceedings](https://proceedings.mlr.press/v235/dym24a.html).
   Weighted probabilistic frames and continuity are already explicit objects;
   the compact-group constructions are not a theorem for these Lorentz
   degenerations.
5. **Shumaylov et al., _Lie Algebra Canonicalization_ (2025), especially
   Appendices F/H.** [Proceedings PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/056521a35eacd9d2127b66a7d3c499c5-Paper-Conference.pdf).
   Noncompact orbit closures and weighted canonicalization are relevant
   neighboring theory, not an automatic novelty certificate or contradiction.
6. **Bhargava and Shankar, _Binary quartic forms having bounded invariants_**,
   Theorem 3.2, final paragraph. [Primary text](https://arxiv.org/html/1006.1002).
   The determinant-normalized projective stabilizer is the two-torsion group
   of the associated elliptic curve. Over C it gives the exact Klein group.
   Lemma 2.1 includes an elementary proof in our stated action convention.
7. **Elezi, _Equilibrium Laws for Julia's Zero and the Hyperbolic Zero of Binary
   Forms_ (2026).** [Primary preprint, v3](https://arxiv.org/abs/2608.27876).
   Its sharp one-half root-concentration threshold concerns a selected
   barycenter. Our fractions concern compact-region mass of arbitrary observer
   distributions under degenerating stabilizers; these are different measures
   and quantifiers. This adjacent recent result is retained in the novelty audit.

The bounded search inspected these primary sources and searched combinations
of Petrov, probability selection, Lorentz covariance, proper actions, binary
quartic reduction and weighted frames. No exact statement of the universal
`1/2,1/4` mass bounds or the TV formulation was found. This supports a
**potential quantitative refinement**, not proof that nobody has established it.
The earlier chat's broader originality emphasis is narrowed accordingly.

## 8. Verification and continuation

[Exact probe](../../tests/program-focus/petrov_probability_selection_probe.py),
[finite Lean certificate](../../Lean/GUFormalization/PetrovProbability.lean),
[review record](../../lab/process/hostile-reviews/2026-11-26-petrov-probability-selection-review.md),
and [machine evidence](../../lab/process/petrov-probability-selection.json).

The finite certificate covers polynomial stabilizer identities and the weighted
overlap arithmetic. Properness, tightness, Petrov classification, existence of
the Julia covariant and the infinite-dimensional probability statements remain
written mathematical proofs reviewed separately. No full theorem is advertised
as Lean-formalized.

The existing source-supported physical-domain/selection investigation continues.
The exact uncovered bridge is whether the source requires a continuous law of
this category or instead supplies Ricci, matter, derivative or global inputs.
This result does not create a new default workstream or a stopping condition.
