---
title: "K1960: Physical convexification and a thermal remainder envelope"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed conditional quantum model; constructive upper envelope, no global amplitude equality or GU claim
scripts:
  - tests/channel-swings/k1960_thermal_frontier_convexification.py
  - tests/channel-swings/k1960_thermal_frontier_convexification_probe.py
---

# K1960: Convexification without a degenerate catalyst

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
result: convex global energy-return frontier, exact dual representation and constructive asymptotic upper envelope
carrier: fixed extreme four-state Schur channel, t=1/2 bath, finite nondegenerate nonnegative catalyst LAYER=toy CHIRALITY=N/A
pairing: Hilbert trace and worst-input marginal half trace distance ON=independent_initial_registers
real_structure: complex energy-conserving shell unitaries and real populations
grading: additive energy resonance classes; no source chirality
action_owner: repository-construction -- exact conditional channel
target: all finite spectra at bounded initial mean energy MAP-TYPE=intertwiner
```

## 1. Results and scope

In exactly [K1958](k1958-sharp-thermal-energy-rate-2026-10-22.md)'s model,
let R_star(E) be the infimum return error at initial mean energy at most E.
The following hold for E>=1:

1. R_star is nonincreasing, continuous and convex, despite the requirement
   that every individual catalyst spectrum be nondegenerate.
2. With b(lambda)=inf_protocol [r+lambda e], it has the global dual form
   R_star(E)=sup_(lambda>=0)[b(lambda)-lambda E]. This ranges over ALL finite
   protocols; it does not identify a finite spectral cutoff for b.
3. Explicit rational vertices (E_n,R_n) give a rigorous piecewise-linear
   upper bound for E>=5/4. Their chord slopes strictly increase. The upper
   envelope has an explicit asymptotic periodic coefficient and a uniform
   limsup bound, sharpening the rounded-family bound in K1958.

Only the constructive upper bound has this periodic coefficient. No equality
with the global frontier, existence of global modulation, sharp additive
constant, finite minimizer or new low-energy facet is asserted. K1954's
counterexample to the proposed third secant remains in force.

## 2. Physical direct sums and the energy-slack issue

Take two finite exact protocols on catalyst spaces A1,A2, with initial states
sigma1,sigma2, energies e1,e2 and return errors r1,r2. On A=A1 direct-sum A2
use sigma=alpha sigma1 direct-sum (1-alpha)sigma2 and the controlled direct-sum
unitary on S tensor B tensor A. It preserves the fixed bath and exact target
channel because each block implements that same channel, and it preserves
initial independence from S and B. It is unitary on every unused input too.

Shift each catalyst Hamiltonian by a nonnegative scalar epsilon_i. This
commutes with each block unitary and changes no channel or return. Choose
arbitrarily small shifts avoiding the finitely many forbidden spectral
coincidences. They can also avoid every cross-block integral energy difference,
so the explicit shell examples have separate resonance classes. The resulting
catalyst is finite and nondegenerate, with energy

    e=alpha(e1+epsilon1)+(1-alpha)(e2+epsilon2).

Trace norm is additive on orthogonal blocks, hence for every system input

    r_mix(input)=alpha r1(input)+(1-alpha)r2(input),
    r_mix<=alpha r1+(1-alpha)r2.                         (1)

Equality of the suprema is NOT assumed for arbitrary protocols. The root
protocols below have input-independent marginal return, so equality holds
there. A classical flag without its energy cost would not prove this theorem.

The shifts introduce arbitrarily small positive energy, so an argument that
simply drops them at a saturated budget is invalid. Here is the needed repair.
There is a finite protocol at e0=1,r0'=1/2 (K1950). Also every feasible protocol
has e>=1: its lowest occupied catalyst energy must share its bath-zero shell
with a second physical catalyst level at energy lower by1,2 or3; shell rank
doubling and nonnegative spectra require the occupied energy to be at least1.
For fixed E>1 and E'>E, mix a near-optimal E' protocol with this e0 protocol,
choosing alpha=(E-1-eta)/(E'-1), where eta>0 pays both shifts. Then

    R_star(E)<=alpha(R_star(E')+xi)+(1-alpha)/2.

First send xi,eta to zero, then E' down to E. Monotonicity gives the reverse
inequality, proving RIGHT continuity for E>1. At E=1 the exact K1950 facet
R_star(E)=3/4-E/4 on[1,6/5] proves continuity directly. Now (1), applied at
budget alpha E1+(1-alpha)E2+eta and followed by right continuity, proves
convexity. A finite convex function is continuous in the interval interior.
This establishes exact-budget convexity, not only a statement about the
closure of a relaxed epigraph.

## 3. Global dual and useful consequences

For lambda>=0, every protocol with e<=E satisfies
r>=b(lambda)-lambda E, so the dual is always a lower bound. Conversely,
a supporting slope s<=0 of the continuous convex nonincreasing R_star at
E>1 gives lambda=-s. Since every protocol obeys r>=R_star(e), its supporting
line gives b(lambda)>=R_star(E)+lambda E. Near-optimal protocols at budget E
supply the reverse inequality. At E=1 the known first facet supplies slope
-1/4. This proves the stated equality everywhere E>=1, without a compact
optimizer or finite-dimensional Slater assumption.

Consequences: any rigorously proved global b(lambda) is a valid all-energy
supporting line, and chords between actual or limiting physical protocols are
upper bounds. Tangents to a finite-support numerical optimum need not lower
bound b(lambda). This distinction explains why finite-hull extrapolation can
fail. K1958 still supplies a strict positive gap above4/25 at each finite E.
The infimum and the supporting-line identity do not prove finite attainment.

## 4. Asymmetric rooted arms and exact limiting vertices

Set q=2/3, p=1/9, W=25/8. On occupied energies1,3,...,2(n+m)+1 choose the
unnormalized populations q^(n-i) for i<=n and p^(i-n) for i>n. Pad the finite
catalyst ladder as in K1939/K1956. The exact shell construction gives

    Z_nm=W-2q^n-p^m/8,
    R_nm=1/(2Z_nm),
    E_nm=1+2n+2[S_m(p)-S_n(q)]/Z_nm,
    S_k(t)=sum_(j=1..k) j t^j.                          (2)

These are physical finite protocols, not just inverse-column relaxations.
For fixed n, sending m to infinity yields

    Z_n=W-2q^n,
    R_n=1/(2Z_n),
    E_n=2n-11/4+(4n+9/2)q^n/Z_n.                       (3)

Every finite m has E_nm<E_n and R_nm>R_n. Indeed adding the next rightmost
population increases the mean energy (its energy is above the prior support)
and increases Z. Thus R_star(E_n)<=R_n using finite approximants. No infinite
catalyst is admitted. Their energy slack can pay the distinct shifts in
section2, yielding every chord as an infimal upper bound. E_0=5/4.

For n>=0 direct rational simplification gives

    (R_(n+1)-R_n)/(E_(n+1)-E_n)
      = -2 / { W[12W q^(-n)-(8n+33)] }.                 (4)

The denominator is positive at n=0 and increases, because its bracket's
increment is6W q^(-n)-8>0. Hence E_(n+1)>E_n and the slopes in(4) strictly
increase to0. The consecutive polygon is precisely the lower convex hull of
THESE vertices. Write U(E) for this polygon on E>=5/4. Then

    4/25 < R_star(E) <= U(E).

This does not say that these vertices are global optimizers or that other
rooted finite-arm supports lie above U. Global upper bounds may be improved
by any additional physical protocol. The result is useful without that claim.

## 5. Bounded remainder and the periodic upper coefficient

Let a=log(3/2), A=64/625, d=-11/4. From(3), uniformly as n grows,

    E_n=2n+d+O(n q^n),
    R_n-4/25=A q^n[1+O(q^n)].

For E between E_n and E_(n+1), write theta=(E-E_n)/(E_(n+1)-E_n).
Then, uniformly for0<=theta<=1,

    (U(E)-4/25)/q^(E/2)
      = A q^(11/8-theta)(1-theta/3)+o(1).               (5)

The coefficient has matching endpoint values, and its maximum is at

    theta_*=3-1/a,
    C_up=A q^(11/8) exp(3a-1)/(3a).                     (6)

Here0<theta_*<1 because1/3<a<1/2. Therefore

    limsup_(E->infinity) (R_star(E)-4/25)/q^(E/2)<=C_up.

This improves the worst-case rounding penalty from3/2 to
exp(3a-1)/(3a) for this asymptotic construction. It establishes a global
constructive upper coefficient only. K1958's universal lower coefficient is
not matched; no global limiting amplitude or periodicity is inferred.
For the inverse resource, it gives the corresponding limsup upper bound

    limsup_(delta->0+) [E_min(delta)-(2/a)log(1/delta)]
      <= (2/a)log(C_up).

To justify inversion, first replace C_up by C_up+epsilon in its eventual
uniform bound, choose energy using C_up+2epsilon to retain strict return slack, then send epsilon to zero. This is not
an equality or an assertion of a protocol at the infimum.

## 6. Verification and remaining work

The producer checks exact asymmetric populations, actual incoming-deficit
returns, limiting vertices, chord slopes and two fully complex physical
shell constructions with rational fractional shifts. The separate probe
rebuilds populations by a recurrence and evaluates bath-label deficits from
scratch; it symbolically checks the chord and asymptotic coefficients.
Actual ratio, origin, return-normalization and shift-energy faults are checked
separately from report/pin faults. Universal convexity, exact-budget continuity,
duality and uniform asymptotics are analytic arguments above, not inferred
from a finite check count. No independent external expert or formal proof
certification is claimed.

Strongest rejected shortcut: treating a direct-sum flag as free at an exact
energy budget. Strongest contrary possibility: other support paths or mixtures
beat U, which is fully compatible with this result. Weakest transfer seam:
physical channel/energy preservation under shifted blocks; the explicit
finite shell checks and block argument cover it. The next global question is
a matching all-spectrum priced dual or a counterexample below this upper
polygon, not proof of modulation from its shape.

[Ng et al., Limits to catalysis in quantum thermodynamics](https://arxiv.org/abs/1405.3039)
is established context for mean-energy restrictions. Its abstract was checked;
no literature-exhaustive novelty claim is made. SC-META-53 remains UNCERTAIN;
LT-SM8, LT-GR6b and AC-F1 remain NEEDS. This finite positive quantum model
supplies no source-owned GU action, quotient or physical observable.
