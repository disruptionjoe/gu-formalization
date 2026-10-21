---
title: "K1881: The minimum-energy observation lift intertwines evolution"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional positive fixed-symbol system, dynamical Hilbert quotient and raw observation range; no native GU, locality of lift or physical quotient claim
---

# Instantaneous recovery extends to dynamics, with a weaker raw target norm

K1879 constructs an instantaneous right inverse but leaves its evolution
property unclaimed. For its constant massive system and all its unitary
rotating repairs, the minimum-source-energy right inverse does intertwine
evolution. The unobserved kernel and its orthogonal complement are transported
exactly. A normalized observation is a coisometry, giving an exact unitary
Hilbert-space quotient. The raw observed L2 norm is **not** the inherited
source energy: the inherited norm is a massive H^-1 norm.

The distinction matters. The raw inverse is unbounded in the massless R3
limit, although normalized observation still has a bounded isometric lift.
On a torus an odd phase winding changes the domain and can give a massless
raw gap on the fixed periodic repaired domain. This is topology/domain
selection in a conditional model, not generation or chirality selection.

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
result: dynamical minimum-energy lift and normalized Hilbert observation quotient
carrier: K1832 real16 source and K1836 real4 target over R3 or matched twisted torus LAYER=toy CHIRALITY=N/A
pairing: positive H source L2 and Euclidean target L2, raw target Hminus1 ON=closed_Fourier_operator_domains
real_structure: real fields via conjugate-symmetric complex Fourier multipliers
grading: observed orthogonal complement and unobserved kernel
action_owner: repository-construction -- conservative first-order propagators
target: right inverse, normalized coisometry and evolution-compatible quotient MAP-TYPE=quotient
```

## 1. Frozen matrices and closed operators

Use the actual four K1840 coordinate types, positive H, leading A_i,T_i,
and d_i=D_i/24. For fixed real R!=0 write

```
L_P=A_i partial_i+R C1,   L_Q=d_i partial_i+R B1,
O=T_i partial_i+R S1,    O L_P=L_Q O.
```

The generators are skew-adjoint on their maximal Fourier domains; smooth
compactly supported fields form a core. The observation O is the closed
maximal Fourier multiplier from source H-L2 to target L2. Its domain is
not assumed to be all H1 or exactly H1; H1 is a useful sufficient domain.
Unobserved source components can have less regularity. All statements below
use the maximal domain or its explicitly stated bounded extension.

K1879 supplies, and the present exact probe checks at the coefficient level,

```
K=O O^dagger=alpha(-Delta+kappa²)I,
kappa=24|R|,    alpha>0.
```

The dagger uses H on the source. In Fourier space, with
M(xi)=i T_i xi_i+R S1 and M^dagger=H^-1 M*:
`M M^dagger=alpha(|xi|²+kappa²)I`. This gives an actual closed-domain
factorization, not just a formal adjoint assertion. No native GU coefficient,
source full20 placement, injection, physical pairing or domain is supplied.
SC-OP-04 ASSERTS candidate grammar, SC-MAS-01/SC-CHI-02 ASSERTS a stylized
toy; SC-OP-05/SC-META-53 remain UNCERTAIN. RA-F1,AC-F1,LT-SM8 and all
source/ledger/canon verdicts stay unchanged.

## 2. Raw minimum-energy inverse and exact intertwining

Let E_P(t)=exp(-t L_P), E_Q(t)=exp(-t L_Q). Fourier intertwining gives
`O E_P(t)=E_Q(t) O` on the observation domain. Unitarity allows adjointing
this identity and replacing t by -t, yielding
`E_P(t) O^dagger=O^dagger E_Q(t)` on the adjoint domain.
K commutes with E_Q. Hence

```
R0=O^dagger K^-1,
O R0=I,          ||R0||=1/(kappa sqrt(alpha)),
R0 E_Q(t)=E_P(t) R0.                                    (1)
```

The norm is the essential supremum of1/sqrt(alpha(|xi|²+kappa²));
low-frequency packets approach equality even though xi=0 has measure zero.
R0 maps target L2 into source H1. Every source preimage of y is
`R0 y+n`, n in ker O, and the two terms are H-orthogonal. Therefore
R0 y is the unique minimum-L2-energy lift and

```
min_(O psi=y) ||psi||_H²=<y,K^-1 y>.                     (2)
```

No arbitrary right inverse has this property. A deliberately added
kernel-valued map N still gives O(R0+N)=I, but generally fails evolution
intertwining. Conservativity and the minimum-norm choice are the load-bearing
premises; instantaneous surjectivity alone is insufficient.

## 3. Hilbert quotient and the raw-norm distinction

The bounded extension

```
V=K^-1/2 O,    V V^dagger=I,
Pi=V^dagger V,  Pi²=Pi=Pi^dagger
```

is a coisometry. Fourier multiplication proves this without manipulating
unbounded products outside their domain. Pi projects onto (ker O)^perp.
V restricts to a unitary from that observed source subspace onto target L2,
and V E_P=E_Q V. The positive conserved source energy splits as

```
||psi||_H²=||V psi||²+||(I-Pi)psi||_H².                  (3)
```

In contrast, R0(L2) is dense in the observed subspace but is not all of it.
The norm in(2) is equivalent to H^-1 for kappa>0; it is weaker than raw L2.
For unit-norm target packets supported near |xi|=N, their minimum source
energy tends to0 as N tends to infinity. Thus there is no positive c such
that min source energy >=c||y||² on all raw target L2.
Completing raw L2 in(2) gives H^-1. The raw O extends to a unitary from
the observed subspace onto that weighted completion, while normalized V
uses ordinary L2. One must not present the raw quotient as an L2 isometry.

Pi and V are nonlocal Fourier multipliers. R0 has denominator
alpha(|xi|²+kappa²) and a nonzero affine numerator, so it cannot be a
finite-order differential operator. The Yukawa inverse followed by O^dagger
is another expression. This nonlocal preparation/lifting operation does not
prove superluminal propagation or provide a local physical observable.
The model's local evolution and its nonlocal reconstruction are distinct.

## 4. Rotating repairs, domains and driven solutions

For K1879's phase set U=exp(-theta J/2), W=exp(-theta L/2), and
`O(t)=U(t) O W(t)^-1`. On R3 assume theta is C2 and its first spacetime
derivatives are bounded on each finite time interval. This sufficient
regularity ensures unitary H1-preserving multipliers and strong
common-domain differentiation; we do not infer that from C2 alone.
The exact propagators are

```
E_P^theta(t,s)=W(t) E_P(t-s) W(s)^-1,
E_Q^theta(t,s)=U(t) E_Q(t-s) U(s)^-1.
```

They include K1879's time and space connection terms. Set

```
R(t)=W(t) R0 U(t)^-1,   V(t)=U(t) V W(t)^-1,
Pi(t)=W(t) Pi W(t)^-1.
```

Then

```
R(t) E_Q^theta(t,s)=E_P^theta(t,s) R(s),
Pi(t) E_P^theta(t,s)=E_P^theta(t,s) Pi(s).                (4)
```

This proves transport of the kernel and observed complement, and exact
minimum-energy recovery at every time. Norm(1) is uniform in the phase.
Dropping the endpoint frames or the time connection invalidates(4).
On smooth data, differentiating gives `R_t+L_P^theta R-R L_Q^theta=0`.
Thus if `y_t+L_Q^theta y=f`, psi=R(t)y solves
`psi_t+L_P^theta psi=R(t)f`. Duhamel extends this to L1-in-time L2 forcing:
source forcing norm is bounded by ||f||/(kappa sqrt(alpha)), and the
minimum lift of the driven observed solution remains in the moving observed
subspace. An arbitrary added kernel forcing changes that minimal solution.

## 5. Massless continuum and winding consumers

For R=0 on R3, the raw observation range in L2 is exactly

```
{y in L2: integral |yhat(xi)|²/|xi|² dxi < infinity}.      (5)
```

Pointwise minimum energy proves necessity and the multiplier inverse proves
sufficiency. This dense range is proper: a radial yhat proportional to
|xi|^-1 on0<|xi|<1 lies in L2(R3) but not in(5). Packets concentrating at
zero frequency show that no bounded raw L2 right inverse exists. These are
infrared obstructions, not a finite-dimensional kernel count.
Nevertheless V=M/sqrt(alpha|xi|²) remains a bounded coisometry almost
everywhere (xi=0 is a null set), so V^dagger is an isometric lift for the
**normalized** target. It does not satisfy O V^dagger=I; instead it gives
K^1/2. This separates a valid quotient from false raw recovery.

On a rectangular torus, R=0 and untwisted periodic domains omit the constant
target modes. On the orthogonal complement the smallest nonzero momentum
controls the inverse norm. If theta(x1+ell)=theta(x1)+2pi n, odd n makes
U,W antiperiodic. On matched transported domains the base spectrum is
unchanged. If the repaired fields are instead required to be periodic,
the base domain is antiperiodic in x1 for odd n. It has momenta
`(2m+1)pi/ell`, hence no zero mode and

```
K >= alpha(pi/ell)² I,       ||R||=ell/(pi sqrt(alpha)).  (6)
```

The other coordinates are periodic and may have zero momentum. An even
winding retains the periodic base zero mode. Formula(6) is a domain effect
with the connection retained, not a frame rotation creating absent modes on
the same fixed domain. Nonzero mass gives lower spectral bound
alpha[(pi/ell)²+kappa²] in the odd-twist case. No count of physical families
or chirality follows from either boundary choice.

## 6. Verification and remaining scientific question

The producer checks the actual four matrix types, polynomial Fourier Gram,
conservativity/intertwining, weighted projections and right inverse at exact
rational frequencies. The separate probe reconstructs row-wise actions,
checks adjoint evolution and rational unitary evolution via Cayley transforms,
and rejects wrong-adjoint, denominator, sign and endpoint-frame faults.
Analytic Fourier/domain arguments above carry global claims; finite-frequency
controls alone do not prove them. Inline hostile review focused on raw versus
normalized target norm, maximal domain, time-dependent frames, infrared
range, parity of twist and nonlocality. No external expert or formal proof.

The conditional dynamical quotient is now explicit. Native fullC/injection/
pairing/domain identification remains separate; pure mass-plane rotating
lifts still require new C,S solving the full equations without K1879's
non-mass connection. Repeating Hilbert polar decomposition cannot solve
those missing scientific identifications.
