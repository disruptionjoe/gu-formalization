---
title: "K1453--K1460 analytic-weight and fourth-chaos boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1453--K1460 analytic-weight and fourth-chaos boundary

Classification is `SOURCE_NATIVE_ROUTE` because the packet tests global-state
and positive-Hamiltonian requirements bordering SC-META-53. The charge
hierarchy and Wick field are repository controls, not released GU data.

```gu-typed-objects
result: analytic-weight globalization obstruction and fourth-chaos/domain necessity boundary
carrier: repository unbounded-charge Maxwell--matter hierarchy and beta=1 Gaussian symmetric Fock control LAYER=toy BRIDGE=positive-state-requirements CHIRALITY=N/A
pairing: positive hierarchy energy and free-Hamiltonian/Fock pairings ON=repository_owned_controls
real_structure: charge spectral conjugation and Gaussian real field
grading: charge powers, Wiener chaos, particle number and free energy
action_owner: repository-construction -- no released source selector, renormalized GU Hamiltonian or physical quotient
target: SC-META-53 global-dynamics and interacting-positive-state boundary MAP-TYPE=restriction
```

## K1453--K1455 — the exact analytic-weight boundary

K1450 chooses `R=rho^2` with

```text
R'(t) = -C B(t),
B(t)=1+||E||_H2+||phi||_H2 ||D_t phi||_H2 >= 1.
```

Hence `R(t)<=R(0)-Ct`. Every finite initial radius reaches zero no later than
`R(0)/C`, even if all field-dependent terms vanish. This is an obstruction to
globalizing that particular absolute-value hierarchy; it is not a blow-up
theorem for the PDE.

The issue is structural. For positive fixed weights `a_n`, let

```text
G_a(F)=sum_n a_n F_n,
S_a(F)=sum_n a_n sqrt(F_n F_(n+1)).
```

There is a finite constant `K` with `S_a<=K G_a` for every finitely supported
nonnegative sequence exactly when

```text
sup_n a_n/a_(n+1) < infinity.
```

Sufficiency is weighted AM--GM. Necessity follows by concentrating on one
adjacent pair, whose optimal quotient is
`(1/2)sqrt(a_n/a_(n+1))`. But the ratio bound implies
`a_n>=a_0 M^(-n)`, so the spectral multiplier
`W_a(q)=sum_n a_n q^(2n)` diverges for `|q|^2>=M`. A fixed no-loss weight can
therefore close the shift or be finite on an unbounded charge spectrum, but
not both.

For the entire factorial-Gevrey family

```text
a_n(R,p)=R^n/(n!)^p,
```

the shifted sum costs the moment
`D_p=sum n^p a_n F_n`. One radius derivative supplies only
`D_1`. Thus `0<p<=1` is absorbable because `n^p<=n`, but it again requires an
additive negative radius speed and collapses in finite time when `B>=1`.
For `p>1`, one scalar radius derivative cannot absorb the shift uniformly.
The exact remaining route must exploit sign/cancellation, spacetime decay,
modified energy, or another topology rather than another absolute one-step
weight of this class.

## K1456--K1459 — what the original beta=1 counterterm must do

Let `P_j` denote Wiener-chaos projection and `W_N=P_4 V_N Omega`. Any
deterministic counterterm of chaos degree at most three obeys

```text
P_4 C_N Omega=0,
P_4(gV_N+C_N)Omega=gW_N.
```

It cannot touch K1439's divergent vacuum fourth-chaos column. If the only new
quartic term is a scalar multiple `c_N V_N`, uniform control on the unchanged
free form requires

```text
|g+c_N| ||(H_0+1)^(-1/2)W_N|| = O(1).
```

K1439 gives the norm lower bound of order `N^2`, hence
`g+c_N=O(N^-2)`. The scalar subtraction cancels the bare quartic coupling to
zero; it does not construct a nonzero renormalized interaction.

For a general fourth-chaos counterterm `Z_N=P_4 C_N Omega`, use the negative
free-form inner product. Writing

```text
Z_N = alpha_N W_N + Z_N^perp,
<A^(-1/2)W_N,A^(-1/2)Z_N^perp>=0,
```

boundedness of `A^(-1/2)(gW_N+Z_N)` is equivalent to both

```text
g+alpha_N = O(1/||A^(-1/2)W_N||),
||A^(-1/2)Z_N^perp||=O(1).
```

Thus a successful fourth-chaos repair must asymptotically cancel the exact
divergent direction while controlling every orthogonal remainder. This is a
necessary projection criterion, not a construction.

Vacuum cancellation is still not enough. In a single fixed oscillator mode,
the diagonal expectation of the normally ordered quartic is proportional to
`6n(n-1)`, while the free energy is proportional to `n+1`. Their ratio grows
linearly. The quartic is therefore not uniformly form bounded by the free
Hamiltonian across particle number even with ultraviolet cutoff fixed. A
positive closed form may instead use the nonlinear domain
`D(H_0^(1/2)) intersect D(V_+^(1/2))`, as K1448 does in its changed
representation. The original beta=1 construction must control both the
ultraviolet fourth-chaos direction and this all-particle-sector domain.

## K1460 — admission replay

The bridge census is now 130 rows: 81 satisfied, ten conditional, 35 excluded
and four missing. The new rows sharpen method boundaries only. SC-ACT-01/02/06
remain `ASSERTS`, SC-META-53 remains `UNCERTAIN`, the physics ledger stays
33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED, K1145/K1150 stay `0/7`,
and no source, canon, paper, prediction, confirmation or public status moves.

## Exact next input

For the PDE, supply a sign-sensitive null-form/dispersive or modified-energy
estimate that avoids the absolute one-charge-shift loss on the unbounded
carrier. For the original `beta=1` quantum theory, supply a genuinely
momentum-dependent/singular fourth-chaos cancellation with bounded orthogonal
remainder and a semibounded nonlinear form domain controlling every particle
sector, then construct the interacting BRST operator on that domain.
