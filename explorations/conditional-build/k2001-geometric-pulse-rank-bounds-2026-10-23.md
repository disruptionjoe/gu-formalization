---
title: "K2001: Logarithmic rank barriers and the elementary pulse spectrum"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2001_geometric_pulse_rank_bounds.py
  - tests/channel-swings/k2001_geometric_pulse_rank_bounds_probe.py
---

# K2001: Logarithmic rank barriers and the elementary pulse spectrum

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
result: logarithmic necessary rank and complete elementary-pulse approximation spectrum
carrier: K1991 actual central rectangle with normalized Lebesgue measures LAYER=toy CHIRALITY=N/A
pairing: real L2 kernel norm and row/column averages ON=central_rectangle
real_structure: real capped measurable kernels; arbitrary real finite-rank approximants
grading: separation rank, not source chirality or particle multiplicity
action_owner: repository-construction -- fixed optimal scalar phase and amplitude cap
target: universal representation barriers and one explicit pulse spectrum MAP-TYPE=intertwiner
```

## 1. Results and distinction between their quantifiers

Keep [K1997](k1997-finite-rank-pulse-obstruction-2026-10-23.md)'s ACTUAL
central rectangle, probability measures mu=dx/2, nu=dz/W, ramp marginal g,
alpha=4t/(3+4t)>1/3, and combined squared marginal residual J(q).
For every capped kernel |q|<=1 of separation rank at most r,

    J(q) > 1/[9437184 * 768^(3(r+1))].                 (1)

For EVERY exact capped central pulse q_* and ANY rank-at-most-r L2 kernel w,
even if w is uncapped or has incorrect marginals,

    ||q_*-w||² >= 3/[6400 * 768^(2(r+1))].            (2)

These improve [K1999](k1999-effective-rank-residual-bound-2026-10-23.md)'s
bounds and imply a necessary rank Omega(log(1/epsilon)) for marginal residual
norm or strong approximation error epsilon. They are still nonsharp universal
bounds; no matching universal upper construction is supplied.

For the SPECIFIC elementary exact pulse q0 from K1991, a separate result gives
the complete singular spectrum and the sharp unrestricted best rank-r law:

    inf_(rank w<=r) ||q0-w||² ~ 4 alpha/(pi² r).       (3)

Thus that pulse requires rank asymptotic to 4 alpha/(pi² epsilon²) for strong
error epsilon. It does not follow that every exact pulse has this rate.
Nor is q0 the minimum-norm pulse: K1995 already improves its central norm.
Spectral approximants need not preserve the cap or marginals. The wings,
global secondary optimizer and physical phase energy are not constructed.

## 2. Fixed geometric bands remove the artificial dimension loss

Reuse K1999's h=(1+q)/2, row coordinate s=(1-x)/2 and terminal-ramp coordinate
v=(1-g)/2. Desired h means are s and 1-v, and column measure is alpha dv.
Write e_row,e_col for h marginal errors, with e²=e_row²+e_col²=J(q)/4.
Set

    N=r+2, k=1/16, rho=1/768=(1/3)k²,
    a_i=(1/4)rho^(i-1), b_i=k a_i, i=1,...,N.

The bands I_i=[a_i,2a_i], T_i=[b_i,2b_i] are disjoint positive-measure
subsets of the actual rectangle/ramp. Let A_ij be the average of h on their
product. The cap and Cauchy-Schwarz, exactly as in K1999, give

    A_ij <= 3a_i/(2 alpha b_j)+e/(alpha b_j sqrt(a_i)),
    1-A_ij <= 3b_j/(2a_i)+e/(a_i sqrt(alpha b_j)).     (4)

Let U_ij=1 if j>=i and 0 otherwise. For j>=i use the second bound; for j<i
use the first. Their structural bounds are respectively

    (3k/2) rho^(j-i),   (3k/2) rho^(i-j-1).

Consequently EVERY row and column sum of the structural error is at most

    S=3k/(1-rho)=144/767.                            (5)

The crucial change is summing this geometric decay instead of multiplying
the largest entry by N. The band ratio no longer shrinks with rank.

Suppose e <= (alpha0 k/16)a_N^(3/2), where alpha0=1/3. The error terms in(4)
are bounded, respectively, by

    (1/16)rho^(N-j)rho^((N-i)/2),
    (1/16)rho^(N-i)rho^((N-j)/2).

For the second bound we also used sqrt(alpha0 k)<=1 and alpha>=alpha0.
Every row and column sum of their two full geometric matrices is at most

    E <= (1/16)[1/(1-rho)+1/(1-sqrt(rho))] <27/208,

because sqrt(rho)<1/27. This overcounts the two triangles safely.
S+27/208<3/8. Hence ||A-U||_2<=sqrt(||A-U||_1||A-U||_infinity)<3/8.
U^-1 has diagonal1 and superdiagonal-1, so ||U^-1||_2<=2 and
sigma_min(U)>=1/2. Therefore sigma_min(A)>1/8: A is invertible.
But rank(h)<=r+1=N-1 and averaging cannot increase rank. Contradiction.
The assumed e threshold is exactly J(q)<=1/(9437184*768^(3(N-1))), proving(1).
The proof controls continuum integrals, not selected point samples.

For an exact q_*, e=0 and sigma_min(A)>=1/2-S>3/10. Compress with orthonormal
band indicators. Its matrix is C=diag(sqrt(a_i)) A diag(sqrt(alpha b_j)), so
sigma_min(C)>=(3/10)a_N sqrt(alpha0 k). For w of rank<=r, the compression of
(1+w)/2 has rank<=r+1<N. A unit kernel vector yields
||C-C_w||_operator>=sigma_min(C). Orthogonal compression is bounded by the
kernel L2 norm, so ||q_*-w||²>=4(3/10)² alpha0 k a_N², which is(2).
This also certifies a positive singular value at every index for every exact
capped target. It neither clips w nor assumes bounded separated factors.

Examples: residual norm at most 1e-10, 1e-50, 1e-100 and 1e-250 respectively
requires rank at least 1, 10, 22 and 56 by(1), compared with K1999's 1, 6, 12
and 27. These are conservative necessary ranks, not precision recommendations.

## 3. Released successor: exact spectrum of the elementary pulse

The two ramps together carry mass alpha and uniform y in[-1,1]. On them
q0(x,y)=sign(y-x); the middle has mass1-alpha and q0(x,middle)=-x.
Thus its Gram operator G=T_q0 T_q0* on L2([-1,1],dx/2) has kernel

    G(x,z)=alpha(1-|x-z|)+(1-alpha)xz.                 (6)

The sign-product integral gives the first term; the middle gives the second.
In particular tr(G)=||q0||²=(1+2alpha)/3. G is positive compact and injective:
if Gf=0 then (Gf)''=-alpha f=0 in distributions. Each nonzero eigenfunction
satisfies f''+k² f=0 with eigenvalue lambda=alpha/k². Reflection splits even
and odd subspaces, since G commutes with reflection.

Even eigenfunctions are cos(kx). The identity (Gf)(1)+(Gf)(-1)=0 gives
cos(k)=0. Their complete eigenvalue list is

    lambda_even,n=alpha/[(n+1/2)pi]², n>=0.           (7)

For odd f, the kernel gives (Gf)'(1)=(1-alpha)(Gf)(1), hence

    f(x)=sin(kx),  k cot(k)=1-alpha,
    lambda_odd,n=alpha/k_n²,
    n pi<k_n<(n+1/2)pi, n>=0.                        (8)

Each interval has exactly one root: k cot(k) decreases from1 (n=0) or
infinity (n>=1) to0 there; derivative is (sin(k)cos(k)-k)/sin²(k)<0.
The actual alpha lies strictly between0 and1. At alpha=1 the even/odd
sequences coincide, a useful control but not the actual pulse.

These necessary conditions are also sufficient. Direct integration gives

    G cos(ky)=alpha[cos(kx)-cos(k)]/k²,
    G sin(ky)=alpha sin(kx)/k²
                +x[(1-alpha)sin(k)-k cos(k)]/k².

The boundary equations remove the extra terms. Equivalently the difference
between Gf and lambda f is affine; parity and the boundary conditions force
it to vanish. There are no missing nonzero eigenfunctions, because the ODE
and reflection exhaust them. Compact self-adjoint spectral decomposition and
injectivity give completeness. The standard compact spectral/SVD facts used
here are stated in [Hart Smith's University of Washington lecture notes](https://sites.math.washington.edu/~hart/m556/Lecture7.pdf);
the actual kernel, roots and bounds are derived above, not imported from that reference.

The eigenvalues in decreasing order are odd0, even0, odd1, even1,... . From
the root intervals, lambda_j~4alpha/(pi² j²) and hence
sum_(j>r)lambda_j~4alpha/(pi² r). This proves(3): spectral truncation attains
the tail, while any rank-r W has range in an r-dimensional subspace E and
||T-W||_HS²>=||(1-P_E)T||_HS². In the eigenbasis of G, the captured energy is
sum lambda_j||P_E u_j||², with coefficients in[0,1] and sum<=r. It is at
most the sum of the largest r eigenvalues. This elementary argument proves
the Hilbert-Schmidt best-rank formula rather than assuming an operator-norm
approximation result implies it. Real eigenfunctions give real approximants.

K1997's capped midpoint approximation has squared strong error alpha/r+O(r^-2)
for even r. Its leading error is pi²/4 times the unrestricted optimum. This
compares an explicitly feasible capped sequence with an unconstrained optimum;
it does NOT prove the optimal capped constant or exact finite marginals.

## 4. Verification, contrary cases and remaining questions

The producer checks12002 exact rational band/error identities across eight
ranks and serializes the explicit formulas/precision consumers. The separate
probe independently integrates the Gram kernel, checks70 exact geometric,
inverse and spectral identities, and detects four mathematical corruptions
(lost ramp measure, wrong Robin coefficient, normalization and triangular
inverse) only after a green baseline. A SymPy Boolean-to-int harness error
was repaired before that baseline; it is not counted as a detected mutant.
Finite checks support the derivation; they do not replace the universal
geometric-sum proof or spectral completeness argument.

Strongest overclaim: transferring the elementary pulse's polynomial error
law to every feasible pulse, or calling the new universal exponential floor
sharp. Neither follows. Strongest contrary control: the uncapped rank2
kernel -x+g has exact marginals and defeats a version of(1) without the cap.
K1997's capped approximants and K1995's improved exact pulse remain valid.
Weakest seam is the universal lower/upper gap: a matching low-rank family
for some exact capped pulse or a stronger continuum estimate is still needed.
The complete q0 spectrum removes the need for sampled singular-value fitting
on that kernel. No wing formula or global optimizer is implied. Source,
physics-ledger and canon remain unchanged; this is internal independent
mathematics, without novelty, external review or formal certification claims.
