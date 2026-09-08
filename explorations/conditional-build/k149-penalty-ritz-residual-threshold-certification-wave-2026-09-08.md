---
title: "K149 penalty--Ritz residual and threshold certification wave"
status: active_research
doc_type: conditional_native_hard_core_charge_sector_enclosure_cluster_form_factor_and_threshold_rank_certification_result
created: 2026-09-08
date: 2026-09-08
claim_ceiling: exact repository-owned convergence and certification theorem for the equal-coupling two-edge native hard-core signed point control: charge-sector isolated eigenvalues are squeezed between monotone finite-penalty min--max values and decreasing native form-core Ritz values; once an isolated cluster count and gap are certified, its spectral projection and complete basis-covariant residual form-factor Gram operator converge in norm; disjoint energy intervals certify the first residual threshold and a positive singular-value margin, together with an exact structural kernel bound when needed, certifies its rank; no numerical native residual energy, complete charge-sector spectrum, strict full-Fock Mourre/scattering, NESS/current, physical selector, source/GU action, Born derivation, prediction or confirmation follows
manifest: lab/process/k149-penalty-ritz-residual-threshold-certification-wave.json
probe: tests/channel-swings/k149_penalty_ritz_residual_threshold_certification_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K149 penalty--Ritz residual and threshold certification wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet keeps K148's equal-coupling two-edge shared corner, native
three-state impurity, positive particle/hole polarization, diagonal `W=0`,
`m=kappa=|q|=1`, positive self energy `1/4`, zero subtraction and threshold
mass `tau=5/4`. It supplies a rigorous route from the infinite-`U`
construction to certified residual energies and form-factor matrices. It does
not report uncertified floating-point eigenvalues.

```gu-typed-objects
result: isolated native charge-sector eigenvalue clusters admit convergent penalty--Ritz enclosures; their complete residual form-factor Gram operators converge in norm and finite margins certify first-threshold order and rank
carrier: each conserved q=(q1,q2) block of native span{|0>,|1>,|2>} tensor positive particle/hole Fock, with auxiliary C4 finite-penalty blocks used only below the native min--max values LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: closed semibounded charge-sector forms with the positive Hilbert pairing; bounded Hubbard endpoint operators define basis-covariant finite residual Gram operators ON=repository_signed_point_control
real_structure: the K146 flavorwise relative particle-hole structure organizes approximants but finite U and finite Ritz spaces are not native polarizations or source-selected states
grading: exact charges qi=ni+N(i,+)-N(i,-), combined Klein-CAR parity, penalty order U and conforming form-core order N
action_owner: repository-construction -- graph, polarization, operator, couplings, subtraction, W, screening, discretization and state are not selected by Weinstein's source or a GU action
target: two-sided isolated-cluster enclosure, norm-convergent full residual form factors, first-threshold interval separation and certified endpoint rank MAP-TYPE=intertwiner
```

## Inline preflight bookend

K148 leaves an operator-valued Feshbach equation, so a finite impurity Schur
root is not available. The correct next question is whether the native
residual data can nevertheless be approached with certificates that close in
the infinite-penalty and infinite-basis limits.

Object-level retrieval found K143's residual-plus-rest-mass HVZ formula,
K146's one-flavor charge spectrum, and K148's monotone hard-core limit,
isolated global ground and one-state density block. It found no two-sided
charge-sector eigenvalue squeeze, no convergence statement for degenerate
residual form factors, and no finite margin rule that decides which candidate
threshold is actually first. No correction entry supersedes those inputs.

The route census compared direct operator-valued Feshbach inversion, Bethe
ansatz, finite volume, finite penalty, conforming Galerkin approximation,
min--max duality, Riesz projections, gap perturbation, singular-value
certification and interval threshold ordering. No integrable structure is
proved. The selected route uses monotone penalty values as lower bounds and
native conforming Ritz values as upper bounds. A future certified IBC
quadrature may implement both sides; ordinary floating point is only a scout.

## 1. Charge reduction commutes with the hard-core limit

Let `H_qf,q` be K148's auxiliary two-flavor quadratic form in fixed charge
`q=(q1,q2)`, and let

```text
Q12=n1 n2,       P=1-Q12,       [Q12,q_i]=0.           (1)
```

For `U>=0`, write

```text
h_U,q[psi]=h_qf,q[psi]+U||Q12 psi||^2.                 (2)
```

The forms are closed, semibounded and monotone. Their limit is the native
charge-sector form

```text
h_hc,q=h_qf,q restricted to Dom(h_qf,q) intersect Ran(P). (3)
```

Thus the penalty does not mix charges and every enclosure below is attached
to one actual K148 residual sector, not to K147's projected labels.

## 2. Penalty--Ritz squeezing of isolated eigenvalues

Let `lambda_k(U,q)` and `lambda_k(hc,q)` denote ordered min--max values, counted
with multiplicity. Below a stable K143 essential edge, monotone form
convergence and compactness give

```text
lambda_k(U,q) increases to lambda_k(hc,q).              (4)
```

Now choose nested finite-dimensional spaces

```text
V_N,q subset Dom(h_hc,q),
closure union_N V_N,q = Dom(h_hc,q) in form norm.       (5)
```

Their conforming Ritz values `rho_k(N,q)` satisfy

```text
rho_k(N,q) decreases to lambda_k(hc,q).                 (6)
```

Consequently every isolated native value below the essential edge has the
two-sided enclosure

```text
lambda_k(U,q) <= lambda_k(hc,q) <= rho_k(N,q),          (7)
rho_k(N,q)-lambda_k(U,q) -> 0                           (8)
```

along any cofinal `U,N -> infinity` path. Equation (7) is the penalty dual:
the lower side is the exact finite-penalty min--max value, not a floating-point
Ritz estimate of it. An implementation must itself certify that side, for
example with a complement/Feshbach tail bound. A finite-`U` eigenvalue or a
finite Ritz eigenvalue is never relabeled native.

For the `r`-fold cluster in an interval `I=(a,b)`, the certificate must show
that exactly `r` lower/upper pairs close inside `I`, while the adjacent pairs
remain outside by positive margins. This prevents spectral pollution and
preserves multiplicity.

## 3. Isolated clusters transport the complete residual matrix

Once the cluster count and a gap `delta>0` to the rest of the native spectrum
are certified, the corresponding finite-penalty and conforming Ritz spectral
subspaces converge to the native cluster in gap norm. Equivalently, after the
canonical polar alignment of equal-rank subspaces,

```text
||P_(U,N),q-P_hc,q|| -> 0.                              (9)
```

This is stronger than convergence of eigenvalues and is the missing bridge to
K148's threshold data.

Let `C_alpha` range over every charge-compatible Hubbard particle/hole
endpoint operator for a fixed total threshold. On the residual eigenspace
`E_q=Ran(P_hc,q)`, define

```text
T_q : E_q tensor C^m -> H,
T_q(phi tensor e_alpha)=C_alpha phi,
G_q=T_q* T_q,
(G_q)_(alpha,beta)=P_q C_alpha* C_beta P_q.             (10)
```

`G_q` is the **complete** residual form-factor Gram operator. It includes all
off-diagonal matrix elements within a degenerate residual cluster. Under a
change of residual basis by `V in U(r)`, it transforms by
`G_q -> (V tensor I_m)* G_q (V tensor I_m)`; hence its spectrum, rank and
kernel dimension are basis independent.

All `C_alpha` are bounded Hubbard/CAR endpoint operators. If
`eta_P=||P_(U,N),q-P_q||` and `c=max_alpha||C_alpha||`, then blockwise

```text
||P_n C_alpha* C_beta P_n-P C_alpha* C_beta P||
  <= 2 c^2 eta_P,                                      (11)
```

and, with the declared `m`-channel block norm convention,

```text
||G_(U,N),q-G_q|| <= 2 m c^2 eta_P =: eta_G.            (12)
```

Thus the full matrix converges in norm. K148's one-state block is recovered
at `r=1`; it is not substituted for (10) when `r>1`.

## 4. Finite certificates for threshold order and rank

For every compatible residual candidate `a=(q',j,alpha)`, let its certified
energy interval be `[l_a,u_a]`. The attached one-escape interval is

```text
I_a=[l_a+tau,u_a+tau].                                 (13)
```

Candidate `a` is the unique first threshold if

```text
u_a < min_(b != a) l_b.                                (14)
```

If (14) fails, the threshold order remains unresolved; overlapping intervals
may represent a true degeneracy or insufficient enclosure precision.

Let the approximate positive Gram eigenvalues be
`mu_1^n>=...>=mu_d^n>=0`. Weyl's bound and (12) imply

```text
|mu_j^n-mu_j| <= eta_G.                                (15)
```

Therefore `mu_d^n>eta_G` certifies full rank. More generally,
`mu_s^n>eta_G` certifies rank at least `s`. Exact rank `s<d` additionally
requires an exact structural kernel of dimension at least `d-s` (from charge,
Pauli, symmetry or an explicit algebraic identity); numerical smallness alone
does not prove a zero singular value. With that kernel and the positive
margin, rank is exactly `s`.

Equations (13)--(15) turn K148's structural threshold list into a stopping
rule: refine `U`, the native form core and the certified tail bounds until the
energy and Gram margins close. Only a closed certificate may feed a strict
Mourre threshold exclusion.

## 5. What this does and does not compute

The theorem proves that the ground-carrying charge restrictions and their full
residual matrices are certifiably approximable. It does **not** provide the
missing numerical IBC tail implementation. A conforming hard-core Ritz value
is a valid upper bound; an ordinary diagonalization of a truncated
finite-`U` matrix is generally another upper bound and cannot be advertised as
the lower side of (7).

The companion exact control uses a finite two-level penalty model only as a
positive witness. For

```text
H=[0 1;1 2],       Q=|2><2|,                           (16)
```

the hard-core value is zero and

```text
lambda_1(U)=(U+2-sqrt((U+2)^2+4))/2 increases to 0.    (17)
```

This verifies direction, strictness and cofinal closure of the penalty bound;
it is not a numerical surrogate for the signed point Hamiltonian.

## Inline postflight bookend

- **Strongest advance:** every isolated native residual cluster now has a
  two-sided monotone enclosure whose width converges to zero.
- **Strongest threshold advance:** norm convergence of the cluster projection
  transports the complete degenerate residual Gram operator, and explicit
  energy/singular-value margins decide first-edge order and rank.
- **Strongest contrary route:** direct operator-valued Feshbach inversion may
  be faster once a certified singular-form quadrature exists; none is yet
  owned, so it is the implementation successor rather than evidence today.
- **Strongest overclaim:** treating truncated finite-`U` diagonalization as a
  certified lower bound. Refused: only the exact penalized min--max value, or
  a separately certified lower enclosure to it, supplies that side.
- **Weakest reproducibility seam:** isolated-cluster projection transport needs
  a certified count and stable gap below the relevant K143 HVZ edge; at an
  embedded eigenvalue or unresolved threshold collision, this packet gives no
  norm-projection claim.

The result was executed inline because all four admitted arcs use the same
min--max ordering, isolated-cluster gap and matrix perturbation seam. No
independent source or specialist tool context justified separate execution.

## Next condition

Implement a certified finite-volume or spectral-tail solver for the K148 IBC
forms. It must return lower bounds for the exact penalized values, conforming
native Ritz upper bounds, cluster-gap certificates and projection-error bounds.
Run it first on the symmetry-related ground-carrying charges, then apply
(10)--(15) to obtain the first numerical residual threshold list and full
form-factor ranks. Only after those margins close, test strict native Mourre
constants. Physical/source selection and open-system NESS/current remain
independent.

## Reproduction

```bash
python3 tests/channel-swings/k149_penalty_ritz_residual_threshold_certification_probe.py
python3 tests/channel-swings/k149_penalty_ritz_residual_threshold_certification_probe.py --selftest
```
