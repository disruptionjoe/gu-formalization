---
title: "K2155 Observation and real-form test of the grade-six port"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source selection, physical quotient or GU recovery
scripts:
  - tests/channel-swings/k2155_observed_grade_six_port_probe.py
---

# K2155 Observation and real-form test of the grade-six port

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2155 frozen observed on-shell port classification and local real-form witness
carrier: full real Cl(7,7) Dirac S=R128 and its complexification, W of signature(3,1) orthogonal to N of signature(4,6), W* tensor S LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: Clifford-skew real B and separately trace-normal Hermitian Hq=iB gamma(q), with induced W-vector-spinor forms ON=declared_carrier
real_structure: real Cl77 matrices before complexification; source barred fields remain independent
grading: ambient volume J halves, tangential exterior degree r and total Clifford grade remain distinct
action_owner: repository-construction -- supplied frozen null quotient and seven-form coefficient; source equation9.16 supplies candidate grammar only
target: coefficient pullback from V* tensor End(S) to W* tensor End(S) and quotient-dual functional MAP-TYPE=intertwiner
```

## Result and source boundary

The [prediction kickoff](../../lab/active-research/joe-directed/prediction-kickoff/interaction-transverse-port-2026-10-27.md)
constructs a fixed grade-six port that descends on ambient null quotients when its
input is massless. Literal observation does not preserve that result automatically.
For the same seven-form port class, observed all-null descent holds exactly when
the seven-form has no tangential-degree-one or tangential-degree-three component.
Degree zero is the zero observed port; degree four is pure observed Clifford trace.
Degree two can carry a nonzero functional: an explicit example has rank64 from
massless inputs into the dual of the observed null quotient.

That example also satisfies a selected trace-normal Hq real-form condition and
preserves both ambient J halves. This is a local compatibility result. It does not
select its coefficient, identify an observed physical quotient, repair the complete
four-field operator, establish full20/K-C compatibility or derive a particle interaction.
SC-OP-04 ASSERTS equation9.16 at candidate strength; SC-OP-05 is UNCERTAIN: the draft admits a rival
with a nontrivial southeast quadrant without selecting it. Neither source assertion selects this seven-form.
No source, ledger or canon verdict moves.

## Fixed objects and inherited results

Work at one point with real V of signature(7,7), full faithful Cl(V) module
S=R128, and an orthogonal split V=W+N with signatures(3,1)+(4,6). Observation
P restricts the one-form leg to W; it leaves S full. There is no replacement by a
four-component physical spinor. Gamma_i squared=eta_i and B makes every gamma
B-skew. For any Z in Lambda7 V, supply

    a_i={Z,gamma_i}/2,     a:S -> V* tensor S.

These coefficients have total Clifford grade6. Let Z=sum_(r=0)^4 Z_r, where
Z_r lies in Lambda^r W times Lambda^(7-r) N. For a nonzero null covector k in
W, put s=slash_W(k), u psi=k_mu psi, j psi=gamma_mu psi,
Gamma=sum_W eta_mu gamma_mu, d=sum_W eta_mu k_mu. Reuse the kickoff's

    T=ker Gamma intersect ker d,   R=tS,   t=u-js/4,
    dim T=256, dim R=128, dim(T/R)=128, ker s=im s, dim ker s=64.

Its annihilator is T-perp=uS+jS. These are supplied algebraic external states,
not a derived gauge quotient. The descended interaction is a FUNCTIONAL on T/R;
a psi need not itself be in T.

## Complete tangential-degree classification

For a basis blade Z_r, a_mu=gamma_mu Z_r when mu belongs to its tangential
support and is zero otherwise. Linearity gives Gamma a_r=r Z_r. Therefore

    F_k=t^times a = (1/2) Z s + sum_r (1/2-r/4) s Z_r.

On the massless input domain ker s=im s, descent is equivalent to

    F_k s = sum_r ((2-r)/4) s Z_r s = 0.                 (1)

Multiplication by tangential gamma preserves normal degree. Distinct normal
blades remain independent in faithful Cl(7,7)=Mat128(R); cancellation between
different r is impossible. This proof would need revision on a nonfaithful or
Weyl-only carrier.

- r=0: Z anticommutes with tangent gamma, so a=0 and sZs=-Zs^2=0.
- r=2: the coefficient in(1) vanishes, so all such Z pass.
- r=4: Z=omega_W C with C a normal3-form commutes with tangent gamma;
  a_mu=gamma_mu Z is pure trace and sZs=Zs^2=0.
- r=1: expand Z=sum_A gamma(v_A) C_A in independent normal6 blades. Since
  C_A commutes with s, sZs=sum_A 2<k,v_A>s C_A. For every null k this is zero
  only if every v_A is orthogonal to every null k. Null vectors span W, so
  every v_A=0.
- r=3: write its tangent3-form as gamma(v_A)omega_W with normal4 blades C_A.
  Since omega_W anticommutes with s, sZs=-sum_A 2<k,v_A>s omega_W C_A.
  The same independence and null-span argument gives v_A=0.

Thus descent on every nonzero tangent null k and every massless input holds
iff Z_1=Z_3=0. In this fixed seven-form family, the allowed vector space has
120+1512+120=1752 real dimensions out of binomial(14,7)=3432. The potentially
visible r2 space has dimension6*252=1512; this is a coefficient-space dimension,
not an independent-particle or independent-amplitude count. No assertion that
every r2 combination is nonzero at each momentum is needed.

## A failed old coefficient and a surviving replacement

Use eta=(+,+,+,+,+,+,+,-,-,-,-,-,-,-), W={0,1,2,7}, k=e0+e7.
The kickoff coefficient Z_old=gamma0...gamma6 has r3, so it fails observed
massless descent; the exact probe verifies F_k s is nonzero. It remains a valid
ambient on-shell construction. Its failure here is not a correction of that claim.

Take instead

    Z_new=gamma0 gamma1 gamma3 gamma4 gamma5 gamma6 gamma8.

It has r2 and passes(1). Its functional map on ker s is injective. Indeed, if
a psi has zero pairing with all T, then a_mu psi=k_mu x+gamma_mu y. At mu=2,
a_2=k_2=0, hence y=0 because gamma2 is invertible. At mu=1, k_1=0 and a_1 is
an invertible grade6 blade, hence psi=0. The map ker s -> (T/R)^* has rank64.
This proof is exact on the full real module; it also holds after complexification.
It proves survival in the supplied target, not an on-shell cross section.

## Released real-form and cell test

The existing [trace-normal reduction](selected-k77-i2b-observer-time-hermitian-reduction-2026-08-12.md)
and [unitary image calculation](selected-k77-i2b-full-unitary-image-covariance-2026-08-12.md)
own Hq=iB gamma(q). In the real exterior Cl77 representation let
B=gamma7...gamma13, J=gamma0...gamma13. Then B is symmetric, B^2=I, and
J^2=I; J is B-skew, so its real eigenspaces are B-isotropic, not separate
nondegenerate B-unitary spaces.

Choose a supplied negative unit normal q=e9, of the trace-normal Hq algebraic
type. The existing geometric q_g=g/2 construction is not identified with this
coordinate split without a frame/signature bridge; none is proved here.
Hq is Hermitian, Hq^2=I and commutes with J. The traces on each J half vanish,
so each complex64 half has signature(32,32). For real grade6 A,

    A^T B + B A=0,
    A^dagger Hq + Hq A = iB [gamma(q),A].                (2)

Every nonzero observed coefficient of Z_new excludes index9, hence commutes
with gamma9. It satisfies(2) and is J-even. Thus this local coefficient lies in
the two Hq-unitary diagonal blocks. Taking q=e8, which occurs in Z_new, fails
this commutator test for the same real coefficients. Multiplying the observed
coefficients by i repairs that observed Hq-skew condition, but changes the real
coefficient choice; uniform phase multiplication does not preserve the complete
ambient port condition because a_8 has the other adjoint parity. Thus this is
a countercontrol to automatic membership, not a general unitary obstruction.
The coordinate q9 is supplied, not a theorem that the source selects it or
selects Z orthogonal to it. A moving q or frame requires connection,
derivative and transport identities separately.

For tangent gamma, the Hq adjoint is SELF-adjoint, unlike its B adjoint.
Nevertheless j^times=Gamma and s^times=s give t^times=d-sGamma/4, the same
formula used above. Nondegeneracy, injectivity of the combined (j,u) map and
its Gram matrix give the same T radical and descent criterion with Hq. With the convention Hq(z,a psi), this is a complex-linear map from psi into
the conjugate dual of T/R (antilinear functionals of z); equivalently one may
use an antilinear map into the ordinary complex dual. This
justifies the complex rank64 functional with this Hermitian pairing; it does
not transfer a false all-gamma-skew Hq hypothesis.

The [source cell extraction](../../lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md)
and [CB-2](../../lab/active-research/joe-directed/high-energy-two-plus-one/cb2-h210-equation916-cross-half-composition-2026-08-16.md)
keep derivative and zero-order cells separate. An even coefficient preserves
ambient halves and belongs in pp/mm zero-order forward blocks, with the
corresponding reverse-shaped cells. It is not the odd H210 offdiagonal construction.
Four source fields are independent. B pairs opposite J halves, whereas Hq
pairs the same halves. A source-compatible barred-row adapter, such as a
properly typed gamma(q) insertion, remains to be derived; it is not supplied
by unitary-algebra membership. These two local compatibility tests therefore
do not establish one full source density-dual construction, a common barred
connection or the full sixteen-cell operator.

## Coupled-domain and observation control

A tangent-null k extended by zero on N has the same ambient slash s. The
kickoff's ambient D14 characteristic equation has nu in ker s and one-form
lift zeta_Y=j_Y nu/12. Hence the input restriction used here retains actual
ambient characteristic nu inputs. It does NOT prove descent of the whole
coupled equation. Literal restriction gives P zeta_Y=j_W nu/12, whereas the
separately supplied D4 principal lift is j_W nu/2. Substitution into D4's
upper row leaves (1-2/12)u nu=5u nu/6, generally nonzero. The exact probe
checks this mismatch. A full operator intertwinement remains an independent
next obligation, and rescaling a lift cannot silently be substituted for pullback.

## Verification and next test

The probe checks all3432 seven-form basis elements against tangential trace and
six null spanning representatives, exact Cl77/real-form matrices and explicit
positive/negative witnesses. It checks altered observation dimension, coefficient,
input-domain, trace-Q and lift data; a failed clean baseline is not a caught fault.
Universal completeness, quotient dimensions and rank64 use the proofs above,
not finite sampling as a universal substitute. No proof-assistant, external
certification or novelty claim.

Next test the complete pulled-back operator and dual with a source-admissible
field map, retaining the actual characteristic input and the trace-Q pairing.
Include derivative/moving-frame terms before claiming physical descent; a
failure excludes that field map only. The compatible local coefficient and
its failed old r3 rival remain reusable exact controls.
