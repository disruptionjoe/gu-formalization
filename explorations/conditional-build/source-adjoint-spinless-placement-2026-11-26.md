---
title: Primary adjoint correction and ordered spinless placement
status: active_research
doc_type: conditional-build-result
program_target: LB-CLASS
tier: T2
expected_delta: Reconcile primary adjoint, classify corrected source-compatible coefficient spaces, and
  place the full ambient spinless connection through actual arrows
actual_delta: Primary minus adjoint restores four fixed-symmetry C-compatible tensors; complete normal
  C-class36R/image24/kernel12; exact spinless placement retains independent fields and unresolved arrows.
  No source falsifier.
class_covered: All normal odd End tensors with declared block or fixed endogenous/weak symmetry; both
  K95 pairing conventions; source-named grade1 scalar through held natural exterior family
premises:
- 'Primary draft section3.5 eq3.27 and source-lower-term-compatibility-2026-11-13.md: printed conjugation,
  not reversion'
- 'source-normal-tensor-class-2026-11-26.md: complete characters and Lie generation, corrected applicability'
- 'source-exterior-connection-2026-11-13.md: held natural exterior map, independent density-dual bars'
- SC-MAS-02/WGS-05 spinless connection carrier; physical curvature bridge not supplied
source_bridge:
  status: conditional
  reason: Printed involution and named grade1 carrier source-authenticated; K95 adapter, actual barred-density
    operator, reduction and physical mass relation remain conditional.
kill_condition: A contradiction must use a source-required map and pairing; plus-comparator emptiness
  or an unbuilt coefficient cannot exclude GU.
---

# Primary adjoint correction and ordered spinless placement

program_target: LB-CLASS
tier: T2
expected_delta: Correct pairing custody and compute actual primitive placement
actual_delta: Corrected classes and ordered placement; no source exclusion

> **Conventional-comparator routing notice.** The plus/reversion pairing below is a named comparator. A conclusion for it cannot transfer to the printed source minus/conjugation pairing without a proved bridge. Read [source-native routing](../../lab/methods/source-native-comparator-routing.md). Neither a K95 algebra adapter nor a shared adjoint sign authenticates K77, the barred-density formal adjoint, or a physical space.

```gu-typed-objects
result: primary adjoint reconciliation and primitive spinless insertion
carrier: K95 H3_1 plus N6_4 complex S128 and independent one-form zeta/zero-form nu LAYER=ambient+observed BRIDGE=explicit-Clifford-adapter-and-contraction CHIRALITY=S-FULL-DIRAC
pairing: Hplus reversion comparator; Hminus=i Hplus Omega implements printed conjugation algebraically ON=declared_carrier
real_structure: fixed antilinear C square-minus1 commutes real Clifford; isometry of Hplus and anti-isometry of Hminus, not an automatic Sp32_32 label
grading: ambient Omega and retained correlated grades; not physical chirality or family count
action_owner: source-action primitive connection arrows, held natural exterior realization; no new action
target: actual q=(P_H zeta,Gamma zeta,nu) and literal O=(P_H zeta,nu) MAP-TYPE=contraction
```

## 1. What changed, and why this came first

Basis: fetched clean `f754e924e6bdf9c9506a09e1bec2c8248dd6e941`. The last normal-tensor result proved its plus-adjoint theorem correctly but called that pairing source-side. The printed source instead uses Clifford conjugation. This correction takes precedence over further candidate constructions because the mistaken attribution changes an apparent exclusion into a survivor.

Primary custody: [official April 2021 draft](https://geometricunity.nyc3.digitaloceanspaces.com/Geometric_Unity-Draft-April-1st-2021.pdf), printed p23, §3.5, eq3.27; SHA256 `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`. Root and source reviewer visually inspected the page. The stated adjoint composes grade involution with reversal. The displayed unitary algebra has real Clifford degrees1,2 mod4 and imaginary degrees0,3 mod4. Its footnote warns the old checkerboard should be checked; the sign conclusion follows independently from the stated involution. The repo already authenticated this in [November13 lower-term compatibility](source-lower-term-compatibility-2026-11-13.md#source-authentication). This is a custody regression repaired, not new source content or a changed source verdict.

For a real degree-k word,

    sharp_plus(w)=(-1)^[k(k-1)/2] w,
    sharp_minus(w)=(-1)^[k(k+1)/2] w.

Thus real vectors are sharp-minus skew. Retain the former plus theorem as a mathematical comparator, including its finite Lean coefficient proof. Withdraw only its source attribution and resulting transfer claim.

Selection: mandatory basis is Joe's continued falsification work with quick20 mathematical descriptions (including category and number theory). Complete class coverage is useful only with correct source relevance. Strongest alternative is the reached full-R spin4/cokernel test on W2; it is still executable but candidate-only. The shared missing input for physical use is authentic operator/domain/observation selection. This wave requires bounded algebra and review; it adds no action, physical choice, policy or waiting checkpoint.

## 2. Exact K95 adapter and changed pairing compatibility

Use the existing K95 Clifford fixture, Hplus, real volume Omega with Omega²=1 and Omega^sharp_plus=-Omega. Define

    Hminus = i Hplus Omega.

It is Hermitian, invertible and neutral. Directly,

    T^sharp_minus = Omega T^sharp_plus Omega.

Every odd Clifford adjoint sign reverses, and every even one is retained. This realizes the printed algebraic involution on the geometry-derived K95 branch; it does not identify that branch with the source-asserted K77 or finish the §9.16 dual/density bridge.

The same quaternionic C commutes with real Clifford words. It is an isometry of Hplus but an **anti-isometry of Hminus**. Indeed anti-linearity sends i to -i while fixing Omega. Writing the antilinear map as `C=C0 conjugation`, equivalently `C0† Hplus C0=conjugate(Hplus)` and `C0† Hminus C0=-conjugate(Hminus)`. The bilinear form `h(Cv,w)` changes from alternating to symmetric. Therefore `[alpha,C]=0` remains a meaningful optional algebraic condition, but its intersection with the new unitary algebra must not inherit the old `Sp(32,32)` name. No physical positivity is claimed.

## 3. Complete normal tensor correction

Reuse the complete all-End argument and fixed-versus-moving distinction in the [normal tensor proof](source-normal-tensor-class-2026-11-26.md). Odd normal multiplicities in degrees1,3,5,7,9 are `(4,8,10,8,4)`; invariant even degrees0,2,4,6,8,10 have `(1,2,3,3,2,1)`. The two horizontal invariant factors are `1,omega_H`.

| Exact normal coefficient class | Plus/reversion comparator | Minus/conjugation adapter |
|---|---:|---:|
| Complex block-Lorentz × geometric-SM | 68 complex | 68 complex |
| Sharp-skew real dimension / contraction image / kernel | 68 / 44 / 24 | 68 / 44 / 24 |
| Additional fixed-C commutation | 32 / 20 / 12 | **36 / 24 / 12** |
| Fixed endogenous graph Lorentz + SAME fixed geometric weak, sharp-skew | 4 / 4 / 0 | 4 / 4 / 0 |
| Same fixed class with additional C | 0 / 0 / 0 | **4 / 4 / 0** |

Proof of changed C count: C fixes real words. Minus-skew keeps real degrees1,5,9 rather than3,7, so the dimension is `2(4+10+4)=36`. Their adjacent even output supports are disjoint, and the exact wedge/interior right inverses give image `2[(1+2)+(3+3)+(2+1)]=24` and kernel12. The full sharp-real phases reverse together; its image44/kernel24 are unchanged.

The generated full product symmetry still gives exactly

    alpha(n)=c_N(n) A,
    A in span_C{1,omega_H,omega_N,Omega}.

All four real tensors are minus-skew and C-commuting. Thus A has four REAL coefficients in the minus class; the plus class requires four imaginary coefficients and its C intersection is zero. In both cases `Gamma_N alpha=10A`, injectively, with spinor ranks0,64,128. For real coefficients C pairs eigenvalues by conjugation (the plus imaginary class used minus-conjugation); paired zeros and ranks remain unchanged. These ranks are not family counts.

In particular the primary-compatible normal grade1 scalar is `alpha=mu c_N`, real mu, with output `10mu I`. The full ambient scalar is `mu c_V`, output `14mu I`. Both survive optional C commutation. Ambient pseudoscalar `c_V Omega` is a different Clifford-degree13 tensor, not automatically SC-MAS-02's grade1 subspace.

Moving reductions remain distinct from fixed-object invariance. The old real degree3 Kahler countercontrol is plus-skew and minus-self; retain it only in the comparator. A minus-compatible moving countercontrol is `alpha_J(n)=c(P_color(J)n)`, real/C-commuting, contraction `6I`; it transforms with J but is not fixed under all normal Spin transformations. No reduction is selected physically here.

### Horizontal companion

The November24 complete block-Lorentz horizontal class remains dimension12R under either adjoint. In the same Schur basis `P_L E_j,P_R E_j`, plus skew/C gives

    A=i sum_j t_j(P_L E_j-P_R E_bar(j)),

whereas minus skew/C gives

    A=sum_j t_j(P_L E_j+P_R E_bar(j)),  t_j real.

Reason: every `alpha(X)=c_H(X)A` is odd, so sharp-skew coefficients change from imaginary to real; C still exchanges the horizontal halves and j with its conjugate. The new simple witness is real `c_H(X)`, contraction `4I`, full support. The old real axial `c_H(X)omega_H` is minus-self and is not this source-compatible witness. The class-existence conclusion survives, but the witness and phase must be corrected. The scalar sterile-support theorem and the Z4 centralizer dimensions do not change: their even projectors/volumes have unchanged sharp laws; their odd test direction must use real c(v), not i c(v).

## 4. Source-only placement before choosing an operator

SC-MAS-02 / WGS-05 names the true-spin-zero `Lambda1 tensor Lambda1` displaced-connection component. It does not identify it with the stylized `R/4` or its complete observed operator. The four independent fields in printed §9.16 remain independent. Keep unbuilt arrows symbolic:

    alpha(v)=mu c(v),
    delta D(zeta,nu)=(Phi(alpha wedge zeta)+mu e J nu,
                      B_SW[alpha] zeta+Z_SE[alpha] nu).

Here J is unnormalized Clifford insertion, Gamma J=nI, n14. B_SW is the actual barred/starred dual-connection prescription; Z_SE is the selected rival's actual variation. The printed SE-zero candidate has Z_SE=0. This is the source-only answer. No independence of bars is removed by introducing notation for a conditional formal adjoint.

If a pairing/density realization is explicitly fixed with `D_SW=-g delta_A` and `c^sharp=chi c`, then `B_SW=-g chi conjugate(mu) Gamma`. Compatible sharp-skew connection means `chi conjugate(mu)=-mu`, giving `B_SW=mu g Gamma`. Thus primary minus allows real mu; plus comparator allows imaginary mu. A different held dual connection or moving density retains its discrepancy in B_SW.

## 5. Ordered exterior insertion, complete scalar natural family

Reuse the already-owned exterior-compatible two-channel family, with fixed scalar coefficients a,c0:

    C(F)_u=sum_v eta_v c_v F_vu,
    Phi(F)=a C(F)+(c0/2) J Gamma C(F),
    T_xi=a(c_xi I-xi Gamma)+c0 J(i_xi-c_xi Gamma).

Do not replace xi by matrix alpha in the principal symbol as though it commuted with Clifford coefficients. Actual exterior multiplication gives

    C(alpha wedge zeta)=mu[(n-2)zeta+J Gamma zeta],
    Gamma C(alpha wedge zeta)=2mu(n-1)Gamma zeta.

The identity `sum_v eta_v c_v c_u zeta_v=2zeta_u-c_u Gamma zeta` proves the first; contraction proves the second. The exact word probe checks all196 coefficient blocks of each identity.

Set `k=(n-2)a=12a`, `f=a+(n-1)c0=a+13c0`, `ell=k+n f=26a+182c0`. With the conditional SW realization,

    delta D = [ mu(kI+f JGamma)   mu e J ]
              [ mu g Gamma       Z_SE   ].

A held same-connection scalar SE Dirac term gives `Z_SE=14mu s I`; an arbitrary SE rival does not. For right-input chiral weights A,B in `T_xi=C_xi A+G_xi B`, the properly ordered insertion is

    delta NW=mu[(n-2)A^op+(A^op+(n-1)B^op)JGamma],

where op exchanges ambient +/- weights. It acts by `(n-2)A^op` on ambient RS and `(n-1)(2A+nB)` on the contracted trace. Coefficient order is load-bearing; physical half labels remain open.

## 6. Observation and 2+1 provenance

Write `zeta=r+J tau/n`, `Gamma r=0`, with nu still an independent field. Then

    r'=mu k r,
    tau'=mu ell tau+mu n e nu,
    nu'=mu g tau+Z_SE nu.

For actual retained `q=(b=P_H zeta,tau,nu)`,

    b'=mu[k b+f J_H tau+e J_H nu].

The horizontal gamma-traceless part and `Gamma_H b-(4/14)tau` both receive mu k. The existing imposter injection `(10J_H psi,-4J_N psi)` is ambient gamma-traceless, observes to horizontal gamma-TRACE and receives the same mu k as the RS cousin in this scalar family. Do not identify independent nu with tau, turn these pieces into three repeated families, or call their coefficients physical masses.

Literal `O=(b,nu)` alone descends for nonzero mu iff f=g=0 in this fixed scalar realization: a hidden normal input with `Gamma_N zeta=psi` has output `(mu f J_H psi,mu g psi)`. This is a primitive zero-order placement statement, not a replacement for the prior principal/domain obstruction. Augmented q carries the displayed map.

For SE0, the trace/nu block determinant is `-mu² n e g`, independently of a,c0. If mu,e,g are nonzero it is invertible; if a is also nonzero the raw full15S insertion is invertible. These are algebraic coefficient ranks. No mode count, physical mass spectrum, source-selected curvature relation or effective low-energy prediction follows.

## 7. Status, coverage correction and continuation

- **ESTABLISHED at the stated internal scope:** printed adjoint custody; both complete algebraic class counts; the source-compatible grade1 survivor; exact ordered primitive placement under named map assumptions.
- **RULED OUT:** only the already-proved plus/reversion fixed-symmetry optional-C class. Its source applicability is withdrawn. No new source-required class is excluded.
- **NOT MODELED / UNDETERMINED:** authenticated K77-to-K95 physical transfer; mandatory C and its physical role; actual barred-density/operator/SE realization; source-selected VEV/curvature/mass map; physical quotient, normalization and propagation; GU's consistency.

Choice budget stays10 families /4 obligation bundles /bookkeepingnet6 /0 source-selected predictions, at its candidate scope. No GU-wide lower bound is inferred. Source/physics/canon/class-C verdicts unchanged. Directed accounting68to69, LB-CLASS27to28; ordinary pendingLC unchanged.

The source-spinless finite placement task is consumed. Its remaining physical bridge needs named input, not another broad scan or invented coefficient. The already-owned full-R spin4 receiver/cokernel test remains the next concrete candidate discriminator; only an actual incompatible cokernel pairing would exclude that realization. Category theory caught the failure to preserve the real/pairing structure under a purported source identification; number theory supplied exact charge/character counts, never generation counts. All20 descriptions are retained in the JSON reassessment; no persona-per-agent or vote replaces proof.

Verification and limitations:36 exact matrix/character controls plus392 dependency-free Clifford identities; separate concrete T2 mathematical and source/placement reviews, with their independence stated. Existing Lean theorem remains comparator-scoped finite coefficient arithmetic, not source verification. No new T1 kill or global proof is claimed. Native gates and reproducibility hashes are in [evidence](../../lab/process/source-adjoint-spinless-placement.json).
