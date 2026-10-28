---
title: "K2167 Mixed middle-port elimination in the complete adapter family"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: normalized zero-order adapters for the declared fixed-splitting coupled operator; no source or physical quotient claim
scripts:
  - tests/channel-swings/k2167_mixed_port_complete_adapters_probe.py
---

# K2167 Mixed middle-port elimination

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
result: K2167 arbitrary mixed-even middle-component obstruction and universal pure-degree exclusion
carrier: full real Cl77 S128 vector-spinor plus scalar, W(3,1) and N(4,6) fixed LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: algebraic field-equation evaluation; no physical Hilbert pairing ON=declared_carrier
real_structure: real Clifford representation and independently supplied common reverse row
grading: full Dirac; tangent and normal exterior degrees are bookkeeping
action_owner: repository-construction: simple-contraction coupled operator and its fixed four-dimensional target
target: complete normalized zero-order principal and coefficient intertwiners MAP-TYPE=intertwiner
```

## Result and exact scope

[K2165](k2165-even-clifford-adapter-descent-2026-10-27.md) classified the COMPLETE normalized
principal adapter family, doubling the old commutant ansatz. In this enlarged family,
any seven-form Z with even tangent degrees0,2,4 that descends through the supplied
fixed-splitting common-connection operator must have **Z2=0**. This includes arbitrary
nondecomposable and singular Z2 and arbitrary Z0/Z4 companions. It is not merely a
coordinate-blade census, a factorized ansatz or an exclusion in the old commutant.

Two useful consequences are also proved: every pure tangent-degree1 or3 seven-form
fails the same necessary equation, even without factorization; a pure degree0 or4
normal form must be invertible. Composing with K2165 extends exclusion of factorized
decomposable pure-degree ports to degenerate supports. A further full-row Euler contraction excludes EVERY remaining invertible pure normal
form without a scalar-square assumption. Thus all nonzero PURE tangent-degree seven-forms
are excluded. The genuinely coupled0+4 problem still requires the FULL lower equation.
A necessary residual equation is not declared sufficient.

SC-OP-04 ASSERTS the candidate four-independent-field grammar, not this chosen
contraction, common reverse, real horn, normalization or target. SC-GEO-55 ASSERTS
displacement from gauge-rotated Levi-Civita, not ordinary torsion. This result does not
settle source/full16cell/full20/K-C descent, a physical quotient, native2+1, chirality,
or observed particle counting. LT-SM8/LT-GR6b/AC-F1 and source/ledger/canon stay unchanged.

## 1. Freeze the original maps before reducing them

Use K2165's real Cl77 full Dirac carrier, W(3,1)={0,1,2,7}, N(4,6) its complement,
eta=(+^7,-^7), omega=gamma0 gamma1 gamma2 gamma7 and omega²=-1.
Every normalized principal adapter is parameterized by

    T_j=A_j+omega B_j, A_j,B_j in Cl(N), j in N.

Here A_j denotes a normal Clifford coefficient, not the complete field adapter A_T.
The field and equation maps differ: equation projection uses kappa(T_j), the common
conjugation by tangent generators on the even-tangent centralizer. On the kernel
column j, zeta_j=I, zeta_mu=-gamma_mu T_j, nu=eta_j gamma_j-2T_j. For a_i={Z,gamma_i}/2,
use the original upper and lower coefficient maps

    E_i=sum_l eta_l gamma_l(a_l zeta_i-a_i zeta_l)+a_i nu,
    F=-sum_l eta_l a_l zeta_l.

The necessary residual L_mu,j=E_mu-gamma_mu F cancels both the equation projection
and every smooth-adapter derivative at fixed geometry. For pure tangent degree r,

    L_mu,j=[(7-r)gamma_mu Z_r-(10+2r)a_mu^(r)]T_j
              +eta_j([gamma_mu,a_j^(r)]+gamma_mu a_j^(r)).     (1)

Linearity in Z permits mixed-degree analysis without fitting a different T to each
summand. All equations below use the SAME A_j,B_j for the entire Z.

## 2. Project mixed-even equations without throwing away companions

For fixed j set X_r=Z_r A_j, Y_r=Z_r omega B_j, N_r=eta_j a_j^(r).
Let pi_r project tangent exterior degree r. Left Clifford multiplication splits as
 gamma_mu=epsilon_mu+iota_mu on that exterior algebra; normal coefficients may have
arbitrary Clifford parity. Define

    F0=7X0-15Y4+N0,
    F2=-9X2+5Y2+3N2,
    F4=-15X4+7Y0+3N4,
    G2=5X2-9Y2+N2.

Direct reduction of (1) gives

    pi1 L_mu=epsilon_mu F0+iota_mu F2,
    pi3 L_mu=iota_mu F4+epsilon_mu G2.                  (2)

Metric-weighted gamma traces are respectively 4F0+2F2 and4F4+2G2. Project their
tangent degrees to separate F0,F2,F4,G2. Thus L=0 forces

    Z2 A_j=(4/7)eta_j d_j Z2,
    Z2 omega B_j=(3/7)eta_j d_j Z2,                   (3)

where d_j is normal metric contraction, equivalently {Z2,gamma_j}/2 here.
No Z0 or Z4 assumption was used. In particular they cannot cancel the middle equations.

## 3. A cyclic bimodule argument removes all middle coefficients

Let D=Cl(N) and I=Z2 D inside Lambda²W tensor D. Its right-module presentation is
cyclic, so dim_R I<=dim_R D=1024. The first equation of (3) places every d_j Z2 in I.
The Clifford relation

    gamma_j Z2=2d_j Z2-Z2 gamma_j

therefore makes I invariant under every left normal generator, hence a D-bimodule.
D is central simple over R (Cl(4,6)=Mat16(H)); equivalently the normal Clifford
basis gives a concrete proof adequate here. Conjugation by each of the ten invertible
normal generators is diagonal on basis blades. The1024 joint sign characters are
distinct, so products of (1+/-Ad_gamma_j)/2 isolate any normal blade coefficient.
Applying such projections to Z2 shows that for each tangent coefficient P_alpha,
P_alpha tensor blade_alpha belongs to I. Right multiplying by that invertible blade
and arbitrary D gives P_alpha tensor D contained in I. Conversely all coefficients
of Z2d lie in their tangent span U. Hence **I=U tensor D**.

The dimension bound now forces dim U<=1. If Z2 is nonzero it factorizes as P tensor q
with real P!=0 and q!=0 (and qD=D). The second equation of (3) lies on the tangent
line RPomega on the left and RP on the right. These lines are independent: a real
eigenvector Pomega=cP would imply c²=-1. Therefore d_jq=0 for every normal j.
But q is a normal five-form and sum_j eta_j gamma_j d_jq=5q; hence q=0, contradiction.
Thus Z2=0.

This is a universal finite-dimensional algebraic proof. The exact character census
in the probe checks the projection instrument; it does not substitute a sampled
matrix search for the dimension argument. Complexifying provides a separate check:
a nonzero coefficient x of the +i tangent-Hodge eigenspace would have xD_C stable
under left multiplication and therefore x invertible. Equations(3) then force
A_j=(4i/3)B_j, impossible for real A_j,B_j unless all contractions vanish.

## 4. Released consequences for odd and degenerate pure ports

For pure tangent degree r, expand (1) with X=ZA_j,Y=Zomega B_j,N=eta_jd_jZ:

    L=(7-r)epsilon X-3(1+r)iota X
       -3(1+r)epsilon Y+(7-r)iota Y+epsilon N+3iota N. (4)

For r=1, degree0 forces X=N/2 and degree4 forces Y=0. The remaining degree2
is4epsilon N=0, hence N=0. For r=3, degree4 forces X=-N/4 and degree0 forces
Y=0. Degree2 then gives6iota N=0, hence N=0. These statements hold for all tangent
indices; exterior creation or contraction of every basis direction annihilates no
nonzero form at these degrees. Normal Euler reconstruction gives Z=0. No decomposability
or nondegeneracy assumption enters, and smooth adapters cannot evade L.

For r=0 write Z=v in Lambda7 N. The mixed equations reduce to
vA_j=-eta_j d_jv/7 and vB_j=0. Therefore vD is a nonzero two-sided ideal if v!=0,
so vD=D and v is invertible. For r=4 write Z=omega u with u in Lambda3 N; similarly
uA_j=eta_jd_ju/5 and uB_j=0, so a nonzero u must be invertible. A decomposable
normal blade with degenerate support is singular, so it cannot survive. Combined
with K2165's nondegenerate calculation and the universal pure1/2/3 obstructions,
this excludes every nonzero factorized decomposable pure-degree seven-form port,
including null/degenerate tangent or normal support.

## 5. Full-row Euler contraction excludes every remaining pure normal form

Let x be an arbitrary normal seven-form (r=0) or three-form (r=4). Section4 forces
x invertible for nonzero candidates. Write Omega=1 or omega, Z=Omega x, k=7-r,
D_j=d_jx, t=-1/7 or1/5, and c=t/2. The necessary equations uniquely force

    T_j=t eta_j x^-1 D_j,
    alpha_j=x^-1 gamma_j x,
    D_j=x(gamma_j+alpha_j)/2.

No scalar-square or decomposability condition is imposed. Put w=x² and
K(y)=sum_N eta_i gamma_i y gamma_i. The full original lower residual is

    Q0^j=Omega[r xT_j-eta_jD_j+7T_jx
                  +(2-2r)S T_j+eta_j sum_iT_i[D_i,gamma_j]],
    S=sum_iT_iD_i=c[(2k-5)x+(1/2)x^-1 K(w)].          (6)

The relevant Euler identities are

    sum_j T_j gamma_j=kt I,
    sum_i T_i x gamma_i=c[(2k-10)x+x^-1 K(w)],
    sum_j eta_j D_j gamma_j=kx,
    sum_j eta_j[D_i,gamma_j]gamma_j=(2k-2)D_i.

The last identity uses the even normal degree k-1 of D_i. Contracting (6) on the
RIGHT by gamma_j and summing WITHOUT an extra eta_j (already carried by Q0^j)
gives

    r0: sum_j Q0^j gamma_j=-(6/7)x^-1[K(w)+18w],
    r4: sum_j Q0^j gamma_j=(6/25)omega x^-1[3K(w)-14w].  (7)

Thus full descent demands K(w)=-18w or K(w)=(14/3)w. But w is even and K has
only eigenvalues10,6,2,-2,-6,-10 on normal grades0,2,4,6,8,10. Neither demanded
eigenvalue occurs, so w=0, contradicting invertibility. Every nonzero pure0 and
pure4 port fails; together with Sections3/4 this excludes ALL pure tangent degrees0..4,
including arbitrary nondecomposable, null, degenerate and nonscalar-square forms.

A concrete nonscalar-square check avoids a matrix inversion: a=gamma345,
b=gamma369 commute, a²=-1,b²=1, x3=a+2b has x3²=3+4ab and inverse(-a+2b)/5.
Its normal-volume multiple is a seven-form with the same square and an explicit
inverse. Both pass the necessary L equations and fail the full lower residual.
The probe verifies (7) from original E,F in all ten columns. Separately, scalar-square
examples x3=gamma345+2gamma689 and its normal-volume multiple verify the stronger
uncontracted identities

    r0: Q0^j=(eta_j x/28)[K(alpha_j)-48gamma_j-40alpha_j],
    r4: Q0^j=(eta_j omega x/100)[64gamma_j+24alpha_j-5K(alpha_j)].

Those are additional controls, not assumptions of the universal proof. Smooth
fixed-geometry adapters cannot repair any even pure-port failure by K2165's parity
separation, while pure odd failure already occurs in derivative-independent L.

## 6. Exact residual problem, not a false full exclusion

For general Z=v+omega u, (2) leaves precisely the necessary coupled equations

    7vA_j+15uB_j=-eta_jd_jv,
    -15uA_j+7vB_j=-3eta_jd_ju.                         (5)

A proposed solution still owes Q0^j=F-sum_i kappa(T_i) E_i=0 for all ten kernel
columns. Together with L=0 this is sufficient for frozen coefficient factorization;
L alone is not. The old coordinate pure0 and pure4 repairs pass L but have nonzero
lower leak -24 eta_j a_j/7 and32 eta_j a_j/25 respectively. They remain negative
controls in the new probe. The genuinely coupled0+4 system has not been excluded here; any nonzero surviving
even candidate must have BOTH components nonzero.

On the open locus where P=7v-15i u is invertible in the complexified normal algebra,
(5) is equivalent to

    A_j+iB_j=-eta_j P^-1(d_jv+3i d_ju).                (8)

This determines all adapter parameters uniquely before the full lower test. It is a
reduction of the remaining problem, not a proof of descent. Both A_j,B_j are odd here,
so kappa(T_j)=-A_j+omega B_j, not -T_j. Singular pencils require their own compatibility
analysis and are not discarded by (8).

A useful entire mixed family can now be excluded. Freeze the complementary coordinate
blades v=gamma34568910 (the first seven normal indices) and u0=gamma111213 (the last
three), and let Z=v+t omega u0 for arbitrary real t. They obey v²=u0²=1 and vu0=-u0v,
so P²=dI with d=49-225t². For d!=0, (8) gives the unique necessary adapters

    A_j=-eta_j[7v d_jv+45u d_ju]/d,
    B_j=eta_j[-21v d_ju+15u d_jv]/d, u=t u0.

The resulting full lower row at j=3 has sorted Clifford-blade coefficients whose
numerators after multiplication by d² are

    blade {4,5,6,8,9,10}: P0(t)=-12(6075t⁴-4557t²+686),
    blade {0,1,2,3,7,11,12,13}: P4(t)=12t(4005t²-833).

The probe reconstructs these coefficients from original maps by exact polynomial
interpolation. This is a proof, not a sampling extrapolation: Z is degree1 in t,
the adapter numerators have degree at most2 over d, C is bilinear in Z and the
kernel coefficients, and the equation projection adds at most one more adapter.
Consequently d²Q is polynomial of degree at most5; six distinct exact points determine
it uniquely. An additional half-ratio control is checked independently. The exact
Bezout identity

    (-1330995t²/3303776-1/8232)P0
      +(-2018925t³/3303776+78137t/235984)P4 = 1

excludes a simultaneous zero, including complex t where d!=0. For t=+/-7/15,
P²=0, so solving P(A+iB)=rhs would require P rhs=0. At j=3, d_ju=0 and the real
part of P rhs is -7eta_j v d_jv!=0. These singular cases also fail the necessary
equations. Arbitrary real relative amplitudes of this pair therefore fail: a nonzero
v amplitude rescales to t, and zero v amplitude is the already excluded pure case.
This excludes this fixed complementary two-blade family, NOT all coupled0+4 ports.
At t=1 the unique necessary adapter passes all40 L blocks but Q0^3 has the nonzero
coefficients -1653/1936 and2379/1936; it is a useful full-row countercontrol.

K2165's even-tangent parity theorem also applies: with fixed geometry Q0 is even
and H_j=sum_W eta_mu gamma_mu partial_mu T_j is odd, so smooth descent forces
Q0=H_j=0 separately. Adapter derivatives cannot repair failure of the new equations.
Moving Clifford/splitting geometry, mixed odd/even ports, a different source-selected
reverse or target, and non-normalized maps require new principal/coefficient analysis.

## 7. Evidence and next decision

The exact sparse Clifford probe reconstructs original E,F on all ten kernel columns
for noncentral mixed-parity A/B fixtures, verifies mixed projections and traces,
retains residuals while inverting the middle system, tests nonfactorized odd ports,
all six real middle-Hodge basis pairs, normal reconstruction and left-ideal closure,
all1024 normal conjugation characters, all512 odd-grade K eigenvectors, and the
nondecomposable scalar-square full-row identities and nonscalar-square Euler
contractions; all512 even-grade K eigenvectors are checked as well. Zero and scalar tangential connections
are full-map positive controls. Null degree0/4 witnesses are explicitly nonzero and
singular. Mutations alter actual port, kernel, lower-row sign, derivative factor or
kappa projection, inverse sign, Euler contraction weight or pencil sign and must trigger genuine failed checks after the green baseline.

The surviving coupled0+4 lower equation outside the excluded complementary two-blade
family is now a smaller, precisely typed question;
repeating a search with arbitrary Z2 or a degenerate pure blade cannot repair the
frozen construction. Strong alternatives remain moving geometry/native jet integrability
and a changed supplied operator horn. Independent internal specialists inspect these
proofs and controls; no source admissibility, external-expert, proof-assistant or
novelty certification is claimed.
