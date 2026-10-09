---
title: "K1543--K1547 lamellar sign-texture obstruction"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1543--K1547 lamellar sign-texture obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification is `SOURCE_NATIVE_ROUTE` because the packet tests the positive
Hamiltonian prerequisite bordering SC-META-53. The cutoff field, lamellar
texture and nonlinear Hamiltonian are repository controls, not released GU
data.

```gu-typed-objects
result: exact lamellar square-wave Parseval tail, Wick-defect scale, ultraviolet sign-shell tradeoff and family-scoped endpoint exclusion
carrier: beta=1 Gaussian reduced Fock space LAYER=toy BRIDGE=positive-state-requirements CHIRALITY=N/A
pairing: Gaussian Q-space pairing ON=repository_owned_control
real_structure: real cutoff Fourier covariance basis with one-coordinate odd-harmonic lamellar centers
grading: cutoff frequency, lamellar fundamental, odd Fourier harmonic, fixed-ratio ultraviolet shell, Wick-square energy and Gaussian form domain
action_owner: repository-construction -- no released source measure, counterterm, Hamiltonian, BRST charge, physical quotient or observed map
target: SC-META-53 interacting-positive-state boundary MAP-TYPE=restriction
```

## Preflight bookend

K1541 reduces every possible order-`N^2` fixed-representation trial to an
amplitude-rigid spatial sign texture with nonvanishing sign mass in a
fixed-ratio ultraviolet shell. The cheapest candidate is a lamellar square
wave: choose alternating slabs, truncate its odd Fourier series at the field
cutoff, and scale the result to amplitude `A_N=sqrt(3C_N)`. This is the natural
construction because it uses every available odd harmonic to sharpen each
interface.

The decisive comparison is not another local derivative estimate. Parseval
computes both the truncation error and the sign field's outer-shell mass. The
same `1/R` harmonic tail controls both. That makes the family exactly
classifiable without importing a general nodal-capacity theorem.

## K1543 — exact square-wave truncation tail

On the normalized circle let

```text
s(t)=sgn(sin t),
p_R(t)=(4/pi) sum_(r=0)^R sin((2r+1)t)/(2r+1).
```

The classical Dirichlet-integral positivity lemma gives

```text
sgn(p_R(t))=s(t)                           almost everywhere.
```

Indeed the unscaled sum has derivative

```text
sum_(r=0)^R cos((2r+1)t)=sin(2(R+1)t)/(2 sin t).
```

On `(0,pi/2]`, integration over successive half-periods against the positive
decreasing weight `1/(2 sin t)` leaves a positive alternating remainder;
symmetry under `t -> pi-t` covers the second half. The same representation
also gives a universal bound `||p_R||_infinity<=C_0` independent of `R`.

Parseval is exact:

```text
T_R:=||p_R-s||_2^2
    =(8/pi^2) sum_(r=R+1)^infinity 1/(2r+1)^2
    =Theta(1/(R+1)).
```

This is an approximation identity, not a capacity estimate.

## K1544 — the optimal lamellar Wick defect is at least cubic

For integers `M>=1`, put

```text
p_(M,R)(x)=p_R(Mx_1),
N_(M,R)=(2R+1)M,
h_(M,R),N=A_N p_(M,R).
```

The center is an admissible real trigonometric polynomial at cutoff
`N=N_(M,R)`. More generally, let `f_N` be any real trigonometric polynomial
of degree at most `N` whose sign is `s_M(x)=s(Mx_1)`. Then

```text
int(f_N^2-1)^2
 >=||f_N-s_M||_2^2
 >=||s_M-P_<=N s_M||_2^2.
```

The second inequality is the Hilbert-space best-approximation property of the
Fourier projection. Its right side is the omitted square-wave tail and is
`Theta(M/N)` for `1<=M<=N`. Conversely, `p_(M,R)` is the projection at the
saturating cutoff and, since `p_R` has the sign of `s`,

```text
(p_R^2-1)^2=(p_R-s)^2(|p_R|+1)^2.
```

Consequently

```text
T_R <= delta_R:=int_T (p_R^2-1)^2
    <=(C_0+1)^2 T_R,
```

and therefore

```text
W_N(h_(M,R),N)
 =A_N^4 delta_R
 =Theta(C_N^2/(R+1)).
```

With `C_N=Theta(N^2)` and `R+1=Theta(N/M)`, this proves the sharp lamellar
class scale

```text
W_N(h_(M,R),N)=Theta(N^3 M).
```

Even the slowest lamella `M=1`, using order `N` harmonics to sharpen one pair
of interfaces, costs `Omega(N^3)`. No band-limited configuration with this
exact square-wave sign pattern reaches the required order `N^2` Wick budget.

## K1545 — outer-shell sign mass uses the same harmonic tail

The spatial sign field is exactly

```text
s_(M)(x)=sgn(sin(Mx_1)).
```

For a fixed shell ratio `0<alpha<1`, its cutoff-`N` shell mass is

```text
H_(alpha,M,R)
 =||1_{alpha N<=|D|<=N}s_M||_2^2
 =(8/pi^2) sum_{alpha(2R+1)<=2r+1<=2R+1} 1/(2r+1)^2.
```

For fixed `alpha`, this is `Theta_alpha(1/(R+1))`, with the obvious exact
finite-sum interpretation when `R` is bounded. Thus

```text
H_(alpha,M,R)=Theta_alpha(M/N),
W_N(h_(M,R),N)=Theta_alpha(C_N^2 H_(alpha,M,R)).
```

The best-approximation tail beyond `N` and the sign mass in the last fixed
fraction below `N` are comparable up to `alpha`-dependent constants.
Therefore every degree-`N` configuration with exact lamellar sign satisfies

```text
int(f_N^2-1)^2>=c_alpha H_(alpha,M,R).
```

Lamellar geometry cannot independently tune amplitude error and ultraviolet
sign texture. Moving a fixed fraction of sign energy to the outer shell
restores order-`C_N^2=Theta(N^4)` interaction.

## K1546 — family-scoped endpoint exclusion

Two consequences are exact for the saturating lamellar family.

1. Every band-limited configuration with exact lamellar square-wave sign has
   `W_N=Omega(N^3)` because `M>=1`.
2. Every sequence or mixture in that class with
   `liminf H_(alpha,M,R)>0`, as required by K1541, has
   `W_N=Omega(C_N^2)=Omega(N^4)`.

Therefore no likelihood supported on this exact lamellar sign class can
produce an order-`N^2` endpoint trial. The class fails already in the
multiplication term, before relative Fisher information or Gaussian boundary
capacity is counted.

The family qualifier is load-bearing. An arbitrary three-dimensional
band-limited sign texture need not be a one-coordinate periodic square wave,
need not use Fourier partial sums, and a likelihood need not concentrate near
one deterministic center. No universal inverse approximation theorem or
weighted-capacity lower bound is proved here.

## K1547 — admission replay

The bridge census is now 262 rows: 183 satisfied, ten conditional, 65 excluded
and four missing. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains
`UNCERTAIN`, the physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS /
2 OVER-DETERMINED, K1145/K1150 stay `0/7`, and no source, canon, paper,
prediction, confirmation or public status moves.

## Postflight hostile review

The strongest overclaim would replace “saturating lamellar Fourier family” by
“all ultraviolet sign textures.” Nothing in the one-dimensional odd-harmonic
calculation controls branched, cellular, randomized or genuinely
three-dimensional nodal geometry. K1546 excludes a canonical construction,
not the complete K1541 tube.

The strongest contrary construction uses a non-lamellar texture or a density
spread over many textures so that entropy and Gaussian weight alter the
boundary quotient. It must still satisfy K1541's order-one amplitude-error
budget and nonvanishing fixed-ratio sign-shell mass.

The weakest proof seam is sign preservation of the Fourier partial sum. The
Dirichlet-integral positivity argument is essential: without it, Parseval
would compare `p_R` to a prescribed square wave rather than to the actual sign
of the center. The proof above supplies that missing identification.

The source boundary is unchanged. These are repository-owned controls
bordering SC-META-53, not an action-owned GU quantization.

## Exact next input

Prove a quantitative inverse theorem for arbitrary three-dimensional
band-limited `f_N`: either bound fixed-ratio shell mass of `sgn(f_N)` by the
normalized defect `int(f_N^2-1)^2`, or construct a non-lamellar counterexample
with defect `O(N^-2)` and nonvanishing sign-shell mass. Lift the winning
configuration geometry to a finite-Fisher likelihood and compute its Gaussian
weighted boundary quotient. K1413 and the action-owned selector tuple remain
independent parallel wakes.
