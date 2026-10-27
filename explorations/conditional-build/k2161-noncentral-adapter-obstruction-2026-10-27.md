---
title: "K2161 Complete noncentral adapter obstruction for pure even-degree ports"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed Clifford splitting and declared common-connection operator only
scripts:
  - tests/channel-swings/k2161_noncentral_adapter_obstruction_probe.py
---

# K2161 Complete noncentral adapter obstruction

> **GU-COMPARATOR-ROUTING: scope before inference.** Any conventional particle-physics
> comparator binds its named model only. It is not evidence for or against Weinstein's
> source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2161 all smooth commutant adapters excluded for each pure even tangent-degree seven-form class
carrier: full real Cl77 spinor S128 and vector-spinor plus scalar, W(3,1) plus N(4,6) LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic evaluation, with no automatic source barred-density identification ON=declared_carrier
real_structure: real Clifford module and independently declared reverse coefficient
grading: full ambient Dirac module; adapter can mix ambient halves
action_owner: repository-construction: fixed simple-contraction common-connection operator
target: complete tangential equation descent through K2159 adapters MAP-TYPE=intertwiner
```

## Result and boundary

[K2159](k2159-commutant-equation-adapters-2026-10-27.md) excluded scalar adapters but
left ten arbitrary elements of a 1024-dimensional commutant. One upper-minus-lower equation
now excludes **every constant or smooth noncentral adapter in that entire family** for the
actual seven-form port. A trace identity extends this to EVERY nonzero pure tangent-degree-two seven-form,
including arbitrary nondecomposable sums and singular Clifford matrices. Separate parity
arguments also exclude each pure tangent degree zero and four. These are precisely the
three degrees that survive K2155's literal null-port test. A sum mixing those degrees is
not excluded here. No nonlinear matrix search is needed for the pure-class theorem.

SC-OP-04 ASSERTS a candidate four-independent-field operator, not this unique realization.
The [source extraction](../../lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md)
retains sixteen cells, barred-row order, rho wrapping and no proved global adjoint. Here the
reverse row, contraction, flat fixed gamma/splitting and tangential derivatives are supplied.
This does not exclude arbitrary adapters, other connection horns, moving gamma/splitting,
normal jets, all source equation9.16 realizations, or physical GU. LT-SM8/LT-GR6b/AC-F1,
full20, K/C real form, native2+1, observed chirality and physical quotient remain open.

## 1. Reuse the exact coupled criterion

Take eta=(+^7,-^7), W={0,1,2,7}, N its complement, and real T_j commuting with all tangent
gamma_mu. K2159's field and equation maps are DISTINCT:

    f=sum_N T_j zeta_j,
    A_T(zeta,nu)=(zeta_mu+gamma_mu f, nu-Gamma_N zeta+2f),
    R_T(E,F)=(E_mu-gamma_mu sum_N T_j E_j, F-sum_N T_j E_j).

The principal identity holds for all tangential covectors and all fields. For normal column j,
ker A_T has zeta_j=I, other normal zeta=0, zeta_mu=-gamma_mu T_j and
nu=eta_j gamma_j-2T_j. The SAME common coefficient is

    a_i={Z,gamma_i}/2,
    E_i=sum_l eta_l gamma_l(a_l zeta_i-a_i zeta_l)+a_i nu,
    F=-sum_l eta_l a_l zeta_l.                           (1)

Write S_projection,j=sum_N T_i E_i^j, Q_mu,j=E_mu^j-gamma_mu S_projection,j,
Q_0,j=F^j-S_projection,j.
For smooth adapters with fixed gamma/splitting, H_j=sum_W eta_mu gamma_mu partial_mu T_j.
The full descent conditions are Q_mu,j+gamma_mu H_j=0 and Q_0,j+H_j=0. Consequently

    Q_mu,j-gamma_mu Q_0,j=E_mu^j-gamma_mu F^j=0            (2)

is necessary for BOTH constant and smooth adapters. Equation projection and every first
adapter derivative cancel. It cannot be repaired by choosing a different derivative of T.

## 2. The actual witness: exhaustive contradiction

For Z=gamma0 gamma1 gamma3 gamma4 gamma5 gamma6 gamma8, put Q={3,4,5,6,8}.
Then a2=a7=0, sum_l eta_l gamma_l a_l=7Z, and sum_W eta_mu a_mu gamma_mu=2Z.
For mu=2 or7, direct evaluation of (1) on a kernel column gives

    E_mu^j=7 gamma_mu Z T_j,
    F^j=2 Z T_j-1_Q(j) eta_j Z gamma_j,
    E_mu^j-gamma_mu F^j
       =gamma_mu Z(5T_j+1_Q(j) eta_j gamma_j).            (3)

Since gamma2 Z is invertible, j=3 would require T3=-gamma3/5. But
[T3,gamma2]=(2/5)gamma2 gamma3, whose square is -4I/25. This contradicts the required
commutant membership. This is an all-parameter proof, including matrices that mix ambient
halves and all smooth choices, not an extrapolation from the exact fixtures.

## 3. Complete pure-degree-two theorem, with an exact elimination certificate

Let Z be ANY nonzero element of Lambda^2 W tensor Lambda^5 N. No decomposability,
common annihilator, nondegenerate support or invertibility of Z is assumed. Write
L_mu,j=E_mu^j-gamma_mu F^j. Clifford contraction identities give

    sum_V eta_l gamma_l a_l=7Z,
    sum_W eta_mu a_mu gamma_mu=sum_W eta_mu gamma_mu a_mu=2Z,
    sum_W eta_mu gamma_mu a_alpha gamma_mu=2a_alpha (alpha in W).

Substitute the original coefficient (1), without replacing the lower row, to obtain

    L_mu,j=(5gamma_mu Z-14a_mu)T_j
            +eta_j([a_mu,gamma_j]+gamma_mu a_j),
    S_j=sum_W eta_mu gamma_mu L_mu,j=-8ZT_j+8eta_j a_j.    (4)

Here S_j is the tangent trace of L, distinct from S_projection in section1. The mixed contraction identity
[a_mu,gamma_j]=[gamma_mu,a_j] and [T_j,gamma_mu]=0 give the polynomial certificate

    L_mu,j - (1/4)gamma_mu S_j - (7/8)S_j gamma_mu
       = -8eta_j a_j gamma_mu.                          (5)

One way to verify it is to replace S by (4), use
2a_mu T_j=ZT_j gamma_mu+gamma_mu ZT_j, and collect the two product orders.
If full smooth descent holds, (2) gives L=0, hence S=0 and a_j=0 for every normal j.
But sum_N eta_j gamma_j a_j=5Z, so Z=0, a contradiction. This exhausts the full
1512-real-dimensional pure(2,5) coefficient space jointly with all ten commutant parameters.
Those are coefficient dimensions, not physical particle counts. Finite basis checks alone
would not establish this bilinear universal statement; (5) is its algebraic certificate.

### The two other pure degrees surviving the literal null-port test

For pure tangent degree r, direct substitution instead gives

    L_mu,j=[(7-r)gamma_mu Z-(10+2r)a_mu]T_j
            +eta_j([a_mu,gamma_j]+gamma_mu a_j),
    sum_W eta_mu gamma_mu L_mu,j
       =(28-14r-2r^2)ZT_j+(2r+4)eta_j a_j.              (6)

For r=0, a_mu=0 and L_mu,j=gamma_mu(7ZT_j+eta_j a_j).
ZT_j anticommutes with gamma_mu while a_j commutes. For r=4,
a_mu=gamma_mu Z and L_mu,j=gamma_mu(-15ZT_j+3eta_j a_j);
ZT_j commutes while a_j anticommutes. Conjugating by any nonnull tangent gamma separates
these two eigenspaces, so either case forces all normal a_j=0. Their normal contraction
traces are respectively7Z and3Z, giving the same contradiction. No invertibility of Z is used.

Thus each nonzero pure degree0,2,4 port is excluded, even though K2155's weaker null-port
test admitted those degrees. A linear sum of different degrees can couple these identities;
the proof DOES NOT exclude all1752-dimensional mixed-degree ports. K2155's null-quotient
result survives in its original scope and is not being rewritten as full equation descent.

## 4. Useful consequences and repair boundary

The obstruction is pointwise. A smooth Z(x) of any one of the three covered pure-degree classes is
excluded wherever Z(x) is nonzero, with FIXED gamma/splitting. No derivative of Z enters this zeroth-order coefficient.
A varying scalar amplitude cannot rescue an open patch containing a nonzero port. At Z=0 the
algebraic obstruction disappears; smooth descent still requires H_j=0. Constant T and Z=0
are an honest positive control, not a solution for the nonzero interaction.

Another positive control is a_mu=lambda_mu I, a_N=0: the common coefficient becomes the
principal symbol D14(lambda), and every constant commutant adapter passes by K2159. It lies
outside the seven-form class. Changing the reverse row independently changes (2), and changing
gamma or the splitting adds derivative terms. Those are explicit new constructions, never
repairs silently credited to the unchanged source candidate.

The previous apparent high-dimensional nonlinear problem is settled for this class. The
next meaningful question is a genuinely mixed-degree0+2+4 port under the SAME
full equations, or an actually constructed moving Clifford geometry/other operator horn.
A fixed-point or sampled search over T for the excluded ports is no longer useful.

## Evidence

Exact sparse Clifford controls reconstruct (1), kernel columns and equation projection for
noncentral fixtures; they check the derivative cancellation, actual forced noncommutant,
positive controls, all1752 monomial even-degree ports, nonseparable r2 sums and a singular normal-form control.
Altered coefficient/sign/commutation inputs must fail real checks after a green baseline.
Universal and smooth-family claims rest on the written argument and independent internal
review. No proof-assistant, external-expert, novelty or remote-CI certification is claimed.
