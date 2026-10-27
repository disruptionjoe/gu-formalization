---
title: "K2165 Complete normalized principal adapters and pure-port descent obstruction"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: normalized zero-order adapters for the declared fixed-splitting coupled operator; no source or physical quotient claim
scripts:
  - tests/channel-swings/k2165_even_clifford_adapter_descent_probe.py
---

# K2165 Complete normalized principal adapters

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2165 exhaustive normalized principal adapters and full-equation exclusion of nondegenerate factorized pure-degree seven-form ports
carrier: full real Cl77 S128 vector-spinor plus scalar, W(3,1) and N(4,6) fixed LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic field-equation evaluation; no physical Hilbert pairing ON=declared_carrier
real_structure: real Clifford representation and independently supplied common reverse row
grading: full Dirac; tangent and normal exterior degrees are bookkeeping
action_owner: repository-construction: simple-contraction coupled operator and its fixed four-dimensional target
target: complete normalized zero-order principal and coefficient intertwiners MAP-TYPE=intertwiner
```

## Result and what changes

[K2163](k2163-mixed-degree-adapter-obstruction-2026-10-27.md) exhausted mixed even-tangent-degree
seven-forms in the tangent-Clifford COMMUTANT family. That family is only half the full
normalized principal-adapter space. Here the normalization is A B=I, where B inserts an
observed vector-spinor/scalar field with zero normal vector-spinor entries. With the same
fixed target principal operator, EVERY zero-order intertwiner is parameterized by ten
members of the centralizer of the EVEN tangent Clifford algebra. This doubles each slot
from1024 to2048 real coefficient directions and supplies the correct equation map.

The larger family still cannot descend any nonzero factorized decomposable seven-form of
pure tangent degree whose tangent and normal supports are nondegenerate. This covers all
3432 coordinate seven-blades, including the1752 even-tangent-degree blades, and their product-
orthogonal images and nonzero scalar multiples. Smooth amplitudes/supports remain excluded
with fixed splitting. Arbitrary mixed ports, degenerate supports, non-normalized adapters,
changed target operators and moving Clifford/splitting geometry are NOT exhausted here.

SC-OP-04 ASSERTS a candidate four-independent-field grammar; its
[source extraction](../../lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md)
does not select this contraction, common reverse, normalization, real horn or target operator.
SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita, not ordinary torsion. No
source/full16cell/full20/K-C closure, physical quotient, native2+1 or observed chirality
follows. LT-SM8/LT-GR6b/AC-F1 and all source, ledger and canon verdicts stay unchanged.

## 1. Exact principal classification

Let eta=(+^7,-^7), W={0,1,2,7}, N its complement, omega=gamma0 gamma1 gamma2 gamma7,
omega²=-I. For tangent covector k, s=sum_W eta_i gamma_i k_i. The supplied principal map is

    D_d(k)(zeta,nu)=(s zeta_i-k_i Gamma_d zeta+k_i nu, -sum_i eta_i k_i zeta_i).

In dimension14 the normal k_i vanish. D14 B=B D4. D4(k) is invertible for k²!=0:
if its output vanishes, contracting the upper row with k and using the lower row gives
Gamma4 zeta=nu; then s zeta_i=0 and finally zeta=nu=0.
Thus D4 A=R D14 and AB=I imply RB=I. No separate equation normalization is assumed.

Subtract the known A0=(zeta_W,nu-Gamma_N zeta), R0=(E_W,F).
For each normal column write the changes K=(U_mu,V), J=(J_mu,J0).
The identity is D4(k)K=J s. Lower coefficients give U_alpha=-J0 gamma_alpha.
Off-diagonal upper coefficients give J_mu=kappa_alpha(J0)gamma_mu for alpha!=mu,
where kappa_alpha(X)=eta_alpha gamma_alpha X gamma_alpha. Comparing the available
indices in dimension4 forces all kappa_alpha(J0) equal. Equivalently J0 commutes with every
tangent bivector gamma_alpha gamma_beta. On this centralizer E, their common restriction
kappa is an involutive algebra automorphism. Put T=-kappa(J0). The remaining diagonal
coefficient gives V=2T; the full maps become

    f=sum_N T_j zeta_j,
    A_T(zeta,nu)=(zeta_mu+gamma_mu f, nu-Gamma_N zeta+2f),
    h=sum_N kappa(T_j) E_j,
    R_T(E,F)=(E_mu-gamma_mu h, F-h).                       (1)

Conversely direct substitution proves D4 A_T=R_T D14 for every tangent covector and field.
A_T B=I makes rank A=640 and kernel dimension1280. These are field dimensions, not particles.

Every Clifford basis blade centralizes all tangent bivectors exactly when its tangent degree
is0 or4. Because Cl(7,7)=End_R(S128), the complete space is

    E=Cl(N) + omega Cl(N), dim E=2048.

This follows also from simultaneous diagonal conjugation characters on all16384 basis blades;
there are no unseen linear cancellations. Its kappa+ eigenspace has normal-even degree in the
first summand and normal-odd degree in the second, dimension1024: the old commutant.
The kappa- eigenspace has opposite normal parity, dimension1024: the new anticommuting part.
A general T may contain both. Using T in the equation projection instead of kappa(T) is wrong
on that new part. Ten arbitrary slots give20480 coefficients, not booked physical freedom.

## 2. Complete coefficient and moving-adapter criterion

The kernel column j of A has zeta_j=I, other normal entries0,
zeta_mu=-gamma_mu T_j, nu=eta_j gamma_j-2T_j.
For a seven-form Z set a_i={Z,gamma_i}/2 and keep the SAME coefficient in both rows:

    E_i=sum_l eta_l gamma_l(a_l zeta_i-a_i zeta_l)+a_i nu,
    F=-sum_l eta_l a_l zeta_l.                            (2)

On each kernel column form Q_mu=E_mu-gamma_mu h, Q0=F-h using (1).
For smooth T with fixed gamma/splitting set H_j=sum_W eta_mu gamma_mu partial_mu T_j.
Differentiating the actual A gives sum P4^mu partial_mu A=(-gamma_mu H_j,-H_j)
on the independent normal input. Therefore complete local descent holds exactly iff

    Q_mu+gamma_mu H_j=0, Q0+H_j=0 for every mu,j.          (3)

When this holds the observed lower-order map is uniquely
C4=(R C14-sum P4^mu partial_mu A)B. This is the factor-through-kernel criterion, so it is
sufficient as well as necessary. Principal matching alone is insufficient.
Subtract gamma_mu times the lower equation: both projection and derivative cancel, yielding
L_mu,j=E_mu-gamma_mu F=0. This necessary condition does not require T to commute with gamma.
For a pure tangent-degree r seven-form, the original maps give

    L_mu,j=[(7-r)gamma_mu Z-(10+2r)a_mu]T_j
             +eta_j([gamma_mu,a_j]+gamma_mu a_j).         (4)

This follows from metric-weighted Clifford contraction identities, with total degree7,
not from an assumed sign of individual generators.

## 3. Exhaust all nondegenerate pure factorized ports

Adapt orthonormal tangent and normal frames to Z=volume(P_r)volume(Q_(7-r)). Such a blade
is invertible since both supports are nondegenerate. Equation(4) becomes

    mu outside P: L=gamma_mu Z[(7-r)T_j+eta_j gamma_j 1_(j in Q)],
    mu inside P:  L=gamma_mu Z[-3(1+r)T_j+3eta_j gamma_j 1_(j in Q)].

For 0<r<4 both types occur, forcing for any j in Q the incompatible values
T_j=-eta_j gamma_j/(7-r) and T_j=eta_j gamma_j/(1+r).
Thus r=1,2,3 already fail the derivative-independent necessary equation, including smooth T.

For r=0 only the outside equation occurs and uniquely forces T_j=-eta_j gamma_j/7 on Q,
zero off Q. For r=4 the inside equation uniquely forces T_j=eta_j gamma_j/5 on Q, zero off Q.
These are valid kappa- parameters, so they really pass L and cannot be rejected as wrong
principal maps. The FULL lower equation remains essential. For NORMAL output indices i in N, on the kernel,

    E_i=7Z delta_ij+(2-2r)a_i T_j+eta_j[a_i,gamma_j].

Set T_j=t eta_j gamma_j on Q. Since kappa(T)=-T, h=-sum T_i E_i and a direct sum gives

    Q0^j=[-1+(19-r)t+(2-2r)(7-r)t²] eta_j a_j.

At r=0,t=-1/7 this is -(24/7)eta_j a_j; at r=4,t=1/5 it is +(32/25)eta_j a_j.
For j in Q these are nonzero invertible leakage matrices. Constant full descent fails.
This explicitly tests the tempting repair that passes only the projected upper-minus-lower
condition. The scalar tangential connection a_mu=lambda_mu I, a_N=0 is a positive control
outside the seven-form hypothesis and passes every constant parameter in E.

For smooth nonzero scalar multiples of a fixed blade the forced T stays constant, so H=0.
More generally let its nondegenerate support vary smoothly within the FIXED W,N splitting.
For r=0 or4 the unique forced T remains normal-vector-valued (the metric projector onto Q
followed by Clifford multiplication). Its derivative H has tangent degree1. The nonzero
Q0 has tangent degree0 for r=0 and degree4 for r=4. Their degrees cannot cancel in (3).
Thus moving supports within this pure factorized class still fail. A genuinely moving
splitting/gamma has additional derivatives and is outside the proof.

## 4. A uniform moving-adapter consequence for mixed even ports

For ANY Z with even tangent degrees0,2,4, including singular and nondecomposable mixtures,
the fixed-splitting coefficient Q0 has EVEN tangent parity for every T in E. Indeed T and
kappa(T) have degrees0 or4; a_normal is even, a_tangent is odd, and the original normal
output and lower output in (2) are even on each kernel column. In contrast, H has ODD
tangent parity: differentiation preserves E and left multiplication by gamma_mu exchanges
parity. Thus (3) forces Q0=0 and H=0 separately, then Q_mu=0. Consequently smooth adapters
cannot repair a failed frozen coefficient condition anywhere in this entire mixed-even class.
The remaining problem is the algebraic50-block criterion plus the independent equation H=0,
not a proposed cancellation by freely tuning adapter derivatives. Moving Clifford/splitting
geometry and odd-tangent ports do not inherit this parity argument.

## 5. Consumers and exact remaining boundary

K2163 remains valid for arbitrary mixed even-degree Z under kappa+ alone. It cannot be
silently transferred to mixed kappa parameters: the extra normal-parity terms change its
projection equations. The new exhaustive principal classification removes guessing about
normalized zero-order maps and exposes the precise remaining joint matrix problem for mixed
or degenerate ports. A construction there must pass all of (3), not just L=0. An alternative
source-selected reverse or target operator requires its own full principal and coefficient
checks. Field and equation maps in (1) differ; their algebraic duals do not supply a density,
barred-field identification, positive physical form or global domain.

Exact controls check all60 tangent-covector/input blocks on mixed kappa fixtures, right inverse
and kernel, original coefficient maps, lower leakage, all3432 pure coordinate ports and the
complete16384-blade centralizer census. Smooth product-rule and scalar/zero controls test the
full criterion. Genuine changed coefficient/order/sign inputs fail after a green baseline.
Universal normalized completeness, product-orthogonal extension and smooth degree separation
are written proofs with independent internal specialist review. No proof-assistant,
external-expert or novelty certification is claimed.
