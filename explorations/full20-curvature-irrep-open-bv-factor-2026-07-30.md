---
title: "N4a full-20 curvature irreps and frozen open-BV incidence: the LC obstruction is exactly traceless Ricci; Hom rank is deferred"
status: active_research
doc_type: result
created: 2026-07-30
run_id: GUH-20260730T135740Z-n2a-n4a-dual-screen
lane_id: "N4a"
work_item: SOURCE-OWNED-CHIMERIC-BV-CAMPAIGN-N4A
depends_on_packet: explorations/unified-source-datum-packet-v0-2026-07-30.md
frozen_packet_hash: 1efdffd34e3ad5358fed16c08cda9ecf681df676e817560bf36b436d79658ffb
code:
  - tests/channel-swings/full20_curvature_irrep_open_bv_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# N4a: curvature irreps and the frozen open-BV incidence problem

## Result

N4a returns a sharp construction equation and an equally sharp refusal to
invent a rank:

```text
N1-PACKET-HASH-UNCHANGED
LC-RIEMANN-IRREP-MAP-IS-HALF-TRACELESS-RICCI-ONLY
LC-SCALAR-AND-WEYL-CHANNELS-ANNIHILATED
W177-TYPED-LC-C_RR-NONZERO-FULL-RANK
PRIOR-W177-QUALITATIVE-VERDICT-SURVIVES
PRIOR-W177-NORM/DECOMPOSITION-SUPERSEDED-FOR-N4A
POINTWISE-SPIN-COMPATIBLE-PIG-WITNESS-SEPARATED
FULL-SP-IG-COVARIANCE-UNRESOLVED
OPEN-BV-TYPED-INCIDENCE-BUILT
OPEN-BV-HOM-RANK-DEFERRED
NO-SOURCE-EOM-FACTORIZATION
NO-CME-TEST
```

For a metric/Clifford-compatible Levi--Civita spin lift,

\[
\nabla g=0,\qquad \nabla\gamma=0,\qquad \nabla P_R=0,
\]

the physical vector-spinor curvature map is

\[
\boxed{
\left(\mathcal C_{RR}^{\rm LC}s\right)_b
=
\frac12P_R\!\left(
\operatorname{Ric}^{0}_{bd}\gamma^d s
\right).
}
\]

Because \(\operatorname{Ric}^0\) is symmetric and trace free, its image is
already gamma trace free:

\[
\gamma^b\operatorname{Ric}^{0}_{bd}\gamma^d=0.
\]

Thus the displayed \(P_R\) is harmless on this term and

\[
\mathcal C_{RR}^{\rm LC}=0
\quad\Longleftrightarrow\quad
\operatorname{Ric}^{0}=0
\]

for the faithful Clifford module used here. The LC contribution therefore
isolates the Einstein equation, not a Weyl-flatness equation. Pure scalar
curvature and pure Weyl curvature contribute exactly zero to
\(\mathcal C_{RR}^{\rm LC}\); traceless Ricci contributes with the fixed
coefficient \(1/2\).

This is useful construction information. It says precisely which background
equation the physical-\(R\) identity asks for before any source correction is
introduced. It also prevents an unrestricted “curvature compensator” story:
there is one LC irrep to address.

The separate IG leg is not yet a frozen operator. N1 names
\(\Omega^{IG}\) among ten insertion families but does not specify its
carrier map or its relation to \(F_A\). N4a therefore gives a conditional
**pointwise Spin-subalgebra witness** using the already declared
\(P_{\rm IG}\in\Omega^2(Y,\operatorname{ad}P)\):

\[
\Omega^{IG}_{\rm cand}:=\rho(P_{\rm IG}),\qquad
\left(\mathcal C_{RR}^{IG,\rm cand}s\right)_b
=P_R\!\left(\gamma^a\rho(P_{{\rm IG},ab})s\right).
\]

At this grade \(P_{\rm IG}\) is independent of \(F_A\). The executable
witness represents one coefficient by a
\(\frac14[\gamma_4,\gamma_5]\) Spin generator. It therefore proves that a
non-Riemann-symmetry-bearing Spin-compatible two-form can be projected to the
same pointwise source and target as the LC arrow. It does **not** prove
covariance under the full \(Sp(32,32;\mathbb H)\) action. That would require
a vector/soldering action satisfying
\(u\gamma(v)u^{-1}=\gamma(u_Vv)\), together with \(P_R\)-equivariance.
Identifying \(P_{\rm IG}\) with
\(F_A\), or imposing the induced-parent equation
\(P_{\rm IG}=Z_U D_AU\), would be a new construction choice or an N3 Euler
equation. Neither is made here. The conditional map proves that LC and IG
matrices can share a pointwise source and target after the restricted Spin
typing is supplied; it establishes neither a full-\(Sp\) IG arrow nor an IG
Hom rank.

Finally, the frozen open-BV grammar is finite but under-typed. N4a exhausts
the incidence information actually present. It can reject definite
type/degree/depth failures and quotient exact identity/projector repetitions.
It cannot compute the equivariant Hom rank without inventing the missing 20
observer-slot maps and contractions. The correct verdict is
`OPEN-BV-HOM-RANK-DEFERRED`, not \(233{,}100\) and not zero.

## Plain English

The earlier calculation found a curvature leftover that blocked the
physical spin-\(3/2\) gauge direction on the W177 test geometry. N4a asks
what kind of curvature it really is.

The answer is unusually clean: ordinary Levi--Civita curvature reaches that
leftover only through the part of Ricci curvature that measures failure to
be Einstein. The scalar part cancels. The Weyl part cancels. That turns a
vague obstruction into a conditional construction target:

> Find the source-selected Einstein locus, or show that a separately typed
> IG/source term cancels the traceless-Ricci map modulo the actual source
> equations.

The open-BV question is less complete for a principled reason. N1 froze ten
names and hard degree limits, but a name is not yet a linear map on every
pair of the 20 observer slots. Counting all possible words gives a search
ceiling, not the number of independent corrections. N4a records everything
that can already be typed and tells N4b exactly what must be supplied before
a rank or factorization can be computed.

This is a conditional step toward learning more: it narrows the geometric
equation while preventing missing representation data from being laundered
into a negative result.

## Layer 0

| shared term | object computed here | object not identified with it |
| --- | --- | --- |
| curvature map | \(\mathcal C_{RR}:S\to T^*Y\otimes R\) | scalar curvature, a curvature norm, an EOM, or a CME obstruction |
| LC curvature | Riemann-symmetry-bearing curvature of a metric/Clifford-compatible spin lift | an arbitrary \(\operatorname{End}(S)\)-valued two-form |
| IG curvature | a pointwise Spin-subalgebra \(\rho(P_{\rm IG})\) witness | a full-\(\operatorname{Sp}(32,32;\mathbb H)\)-covariant IG arrow, \(F_A\), LC Riemann curvature, or a proved induced curvature |
| physical \(R\) | \(R=\ker\Gamma\subset T^*Y\otimes S\) | a free Weyl-spin-\(3/2\) comparator or a ghost-subtracted standard gravitino |
| open-BV basis | slot-pair/word tuples after actual Hom typing and quotient | the 233,100-element syntactic ceiling |
| rank | dimension of a specified native-real-form equivariant Hom quotient | a count of token strings or partial incidence statuses |
| Jacobi control | a planted sign error in a finite algebraic aggregation | the nonlinear classical master equation |
| W177 | a local actual-\(\operatorname{Sym}^2\) discriminator already known nonstationary | a selected source solution or a constraint counted toward surplus |

The LC calculation and the prior full-20 curvature remainder are
`SAME-OBJECT` only after the raised/lowered gamma convention is made
consistent. The LC arrow and the pointwise Spin witness have the same matrix
source and target. Their full-\(\operatorname{Sp}(32,32;\mathbb H)\)
equivariance is `UNCERTAIN` until the gamma/soldering and \(P_R\) data are
intertwined. They are therefore not promoted to the same equivariant Hom
space. The frozen token \(\Omega^{IG}\) and the conditional
\(\rho(P_{\rm IG})\) witness are not silently declared identical.

## Construction fork

This result stays on the program-native branch:

\[
Y^{14}=\operatorname{Met}(X^4),\qquad
TY=TX\oplus\operatorname{Sym}^2T^*X,
\]

with actual \(4+10\) base/fibre order, signature
\((3,1)+(6,4)=(9,5)\), the `Cl(9,5)` spinor, the Krein-compatible
gamma-trace splitting, and the geometric Rarita--Schwinger carrier.

It does not use:

- the numerically equal but inequivalent
  \(\Lambda^2T^*X\oplus\Lambda^3T^*X\) exterior ten;
- a positive-Hilbert replacement for the native Krein structure;
- a free Weyl-spin-\(3/2\) curvature formula;
- a nonparallel gamma-trace projector; or
- W177 as an assumed vacuum.

The IG leg has two explicit future forks:

1. **independent auxiliary carrier:** retain
   \(\Omega^{IG}_{\rm cand}=\rho(P_{\rm IG})\), with
   \(P_{\rm IG}\) independent of \(F_A\);
2. **induced parent:** use an N3 equation to relate \(P_{\rm IG}\) to
   \(D_AU\), and only then derive its relation to \(F_A\).

N4a does not choose between them.

## 1. The LC identity

Use gamma matrices with raised labels,

\[
\{\gamma^a,\gamma^b\}=2g^{ab},\qquad
\gamma_a=g_{ab}\gamma^b,
\]

and define

\[
\Gamma(\psi)=\gamma^a\psi_a,\qquad
j(s)_a=\frac1n\gamma_as,\qquad
P_R=1-j\Gamma,\qquad n=14.
\]

The exact projector identities are

\[
\Gamma j=1,\qquad
(j\Gamma)^2=j\Gamma,\qquad
P_R^2=P_R,\qquad
\Gamma P_R=0,\qquad
P_Rj=0.
\]

For the compatible spin lift,

\[
\Omega^{LC}_{ab}
=\frac14R_{cdab}\gamma^c\gamma^d.
\]

Clifford contraction, Riemann pair symmetry, and the first Bianchi identity
give

\[
\gamma^a\Omega^{LC}_{ab}
=\frac12\operatorname{Ric}_{bd}\gamma^d.
\]

Decompose

\[
\operatorname{Ric}_{bd}
=\frac{\operatorname{Scal}}{n}g_{bd}
+\operatorname{Ric}^{0}_{bd}.
\]

The scalar term is in \(\operatorname{im}j\):

\[
\frac{\operatorname{Scal}}{2n}\gamma_b,
\]

so \(P_R\) kills it. For the trace-free symmetric term,

\[
\gamma^b\operatorname{Ric}^{0}_{bd}\gamma^d
=
\operatorname{Ric}^{0}_{bd}g^{bd}
+\operatorname{Ric}^{0}_{bd}\gamma^{bd}
=0.
\]

It already lies in \(R\). Weyl curvature has zero Ricci contraction and
therefore never enters the map. This proves

\[
\boxed{
\mathcal C_{RR}^{LC}
=\frac12\operatorname{Ric}^{0}_{bd}\gamma^d.
}
\]

The hypothesis is load-bearing. Metric/Clifford compatibility makes
\(\Gamma\), \(j\), and \(P_R\) parallel:

\[
\nabla\gamma=0\quad\Longrightarrow\quad\nabla P_R=0.
\]

The probe conjugates \(P_R\) by a nonmetric vector-slot shear. The conjugate
is still algebraically idempotent, but it does not intertwine the native
gamma trace: its transport defect is \(2.280903\), and a projected sample
has nonzero gamma trace. This planted failure prevents the LC Ricci collapse
from being transferred to a nonparallel projector.

## 2. Irrep controls

Three independent algebraic curvature fixtures were constructed in
signature \((9,5)\):

| fixture | scalar | \(\|\operatorname{Ric}^0\|\) | \(\|\mathcal C_{RR}^{LC}\|\) | result |
| --- | ---: | ---: | ---: | --- |
| constant sectional curvature | \(182\) | \(0\) | \(0\) | scalar channel killed |
| pure traceless Ricci | \(0\) | \(\sqrt2\) | \(8\) | exact \(1/2\) channel survives |
| pure Weyl | \(0\) | \(0\) | \(0\) | Weyl channel killed |

Each fixture satisfies the algebraic Riemann symmetries and first Bianchi
identity. Each agrees with
\(\frac12P_R(\operatorname{Ric}^0_{bd}\gamma^d)\) to numerical roundoff.
The pure Weyl fixture is not obtained by subtracting a desired answer from
W177: it is an independently planted diagonal sectional-curvature tensor
whose sectional row sums vanish.

Flat curvature is contained in both zero channels. Constant nonzero
curvature is the stronger scalar control: the Riemann tensor is nonzero
while the physical-\(R\) map vanishes.

## 3. Convention correction and W177

The earlier
`tests/channel-swings/full20_native_polarization_probe.py` mixed two
vector-spinor index conventions inside its curvature routine. It formed the
spin curvature and the \(a\)-contraction with
\(\gamma_a=g_{ab}\gamma^b\), then applied a projector whose
\(\Gamma\) used \(\gamma^a\), without raising the output \(b\)-index. All of
that code was internally executable, so its controls verified the
calculation it stated. They did not verify that the stated map was the
single consistently typed LC map.

The new constant-curvature regression exposes the mismatch:

```text
correct typed LC scalar leakage:   0
legacy mixed-convention leakage:   263.68812748
```

This note is append-only. It does not rewrite the prior artifact. Its
disposition is:

- the prior qualitative W177 result—nonzero and full column rank
  \(128\)—**survives**;
- the prior norm \(21.04321084\) and any decomposition inferred from it are
  **superseded for the consistently typed N4a LC map**;
- the corrected central-scale result is

\[
\operatorname{Scal}=-10.000000618,\qquad
\|\mathcal C_{RR}^{LC}\|=15.66992510,\qquad
\operatorname{rank}\mathcal C_{RR}^{LC}=128;
\]

- its gamma-trace leakage is below \(2\times10^{-11}\);
- its difference from
  \(\frac12P_R(\operatorname{Ric}^0_{bd}\gamma^d)\) is below
  \(2\times10^{-5}\), the finite-difference curvature floor.

W177's grouped \((+^9,-^5)\) frame was explicitly permuted to native
base/fibre order

```text
(0,1,2,9,3,4,5,6,7,8,10,11,12,13).
```

The grouped and correctly permuted native realizations agree in norm and
rank. Feeding grouped curvature labels to the native-interleaved gamma list
changes the result and is rejected.

W177 therefore remains a negative control for the current physical-\(R\)
identity. It is not promoted to a source solution. Its failure is now more
informative: its nonzero LC obstruction is exactly its nonzero traceless
Ricci channel.

## 4. The separately typed IG candidate

The LC Riemann decomposition must not be applied to IG curvature. A general
\(\operatorname{End}(S)\)-valued two-form need not have Riemann pair
symmetry, a Ricci tensor, or a scalar/Ricci/Weyl decomposition.

For the conditional independent-carrier fork, define

\[
P_{\rm IG}\in\Omega^2(Y,\operatorname{ad}P),\qquad
\rho(P_{\rm IG})\in\Omega^2(Y,\operatorname{End}S).
\]

For a subgroup \(H\) whose action also intertwines the soldering/Clifford map
and preserves \(P_R\), one may define

\[
\mathcal C_{RR}^{IG,\rm cand}:
S\longrightarrow T^*Y\otimes R,\qquad
s\longmapsto
P_R\!\left(\gamma^a\rho(P_{{\rm IG},ab})s\right)
\]

is \(H\)-covariantly typed. The probe uses an antisymmetric two-form with the
fixed Spin generator \(\frac14[\gamma_4,\gamma_5]\). Its output is nonzero
and gamma-traceless. This is a pointwise Spin-compatible, non-Riemann-
symmetry-bearing control; it is not a full-\(Sp\) IG construction and is not
decomposed into LC irreps.

The executable `Arrow` control records source, target, label, and matrix
separately. The LC arrow and pointwise Spin witness sum as matrices only
because both have

\[
S\longrightarrow T^*Y\otimes R.
\]

A planted target \(T^*Y\otimes S\) is rejected. This is a pointwise type
control, not a gauge-covariance test. Provenance is retained in the sum label.

This construction does **not** establish any of the following:

- that N1's bare \(\Omega^{IG}\) token canonically means
  \(\rho(P_{\rm IG})\);
- full-\(Sp(32,32;\mathbb H)\) covariance of the pointwise witness;
- that \(P_{\rm IG}=F_A\);
- that \(P_{\rm IG}=Z_UD_AU\) off shell;
- an IG equivariant Hom dimension; or
- cancellation of the W177 LC term.

Those are N3/N4b questions.

## 5. Frozen open-BV incidence

N1 freezes ten insertion families, word length one through three, 20
observer slots, and the ceiling

\[
\binom{21}{2}(10+10^2+10^3)
=210(1110)
=233{,}100.
\]

N4a does not alter that API. The packet hash remains exactly
`1efdffd34e3ad5358fed16c08cda9ecf681df676e817560bf36b436d79658ffb`.

The maximal incidence ledger supported by the presently written maps is:

| token | supplied carrier/incidence at N4a | order/field-degree charge used by the partial filter | disposition |
| --- | --- | --- | --- |
| \(1\) | polymorphic identity | \(0/0\) | typed; removed from nontrivial words |
| \(\Omega^{LC}\) | LC correction arrow \(S\to T^*Y\otimes R\) | \(2/0\) | full 20-slot insertion map absent |
| \(F_A\) | \(\Omega^2(Y,\operatorname{ad}P)\) carrier | \(1/\le2\) | observer-slot representation/contractions absent |
| \(\Omega^{IG}\) | frozen name; conditional \(\rho(P_{\rm IG})\) witness kept distinct | \(1/\le1\) | frozen slot map and relation to \(F_A\) absent |
| \(v\) | \(\mathfrak c_\rho(v)\) is written | \(0/\le1\) | complete 20-slot incidence absent |
| \(II\) | geometric second-fundamental-form carrier | \(1/\le1\) | 20-slot insertion map absent |
| \(T\delta\) | \(R\to R\) | \(2/0\) | typed in the supplied partial graph |
| \(\delta T\) | \(S\to S\) | \(2/0\) | typed in the supplied partial graph |
| \(Q\) | \(R\to R\) | \(1/0\) | typed in the supplied partial graph |
| \(j\Gamma\) | \(VS\to VS\), image \(I\) | \(0/0\) | typed projector; \((j\Gamma)^2=j\Gamma\) |

The executable filter enumerates all 1,110 token words before observer-slot
assignment. Under this deliberately partial graph it returns:

```text
definitely typed word shapes:           36
definitely rejected word shapes:       712
map-deferred word shapes:              362
typed partial quotient representatives: 6
```

These four numbers are **not** Hom dimensions. They record the status of
word shapes under the maps currently supplied. A later map may move a
deferred word to typed or rejected, but it cannot rescue a word that already
violates the frozen derivative, field-degree, composition-depth, or definite
source/target rules.

The exact equivariant Hom quotient rank still requires:

1. source and target carriers for all 20 observer slots;
2. the action of each token on every eligible slot;
3. the frozen construction of \(\Omega^{IG}\) and its relation to \(F_A\);
4. native-real-form equivariant multiplicities; and
5. the first invariant pairing/contraction for every typed tuple.

Without those data, multiplying any partial word count by 210 would turn a
syntactic surplus into a fictitious parameter surplus.

## 6. Quotient and hostile controls

The probe exercises:

- the full Clifford relation in grouped and native `Cl(9,5)`
  realizations;
- \(\Gamma j=1\), complementary \(j\Gamma/P_R\) projectors, and
  \(\Gamma P_R=0\);
- the algebraic Bianchi identity on every synthetic LC fixture;
- identity deletion and
  \((j\Gamma)^2=j\Gamma\) word canonicalization;
- rejection of the ill-typed word
  \((T\delta,\delta T)\);
- rejection of a length-four word;
- rejection of derivative-overdepth \((Q,Q,Q)\);
- rejection of field-degree excess \((F_A,F_A,F_A)\);
- rejection of an LC/IG target mismatch;
- rejection of the nonparallel projector; and
- a planted sign error in a Jacobi aggregation.

The correct cross-product Jacobi sum vanishes and the one-sign-flipped plant
does not. This is a control that the checker can detect a sign error. It is
not a CME calculation. Integration-by-parts and formal-adjoint identities
remain in the frozen quotient specification, but a complete tuple quotient
cannot be executed until each tuple's density pairing and carrier maps are
provided.

## 7. Parameter and constraint account

N4a adds no coefficient to the sealed N1 packet.

| quantity | value/status |
| --- | --- |
| new physical/source parameters | \(0\) |
| frozen insertion families | \(10\) |
| frozen composition depth | \(3\) |
| ordered word ceiling before slots | \(1110\) |
| unordered-with-repetition observer-slot pairs | \(210\) |
| frozen syntactic ceiling | \(233{,}100\) |
| exact LC irrep coefficients | scalar \(0\), traceless Ricci \(1/2\), Weyl \(0\) |
| exact frozen Hom quotient rank | `RANK-DEFERRED` |
| N3 EOM jet-span rank | not run |
| source-EOM coefficient quotient | not run |
| W177 contribution to constraint surplus | \(0\); discriminator only |

It would be invalid to report a numerical constraint surplus for the open
BV family before the Hom rank and N3 EOM rank exist. The LC result does have
positive information content without a fit: three preregistered irrep
fixtures resolve to the exact fixed pattern \(0,\frac12,0\), with no
adjustable coefficient.

## 8. Five-leg findings ledger

| leg | N4a result | what remains conditional |
| --- | --- | --- |
| Y — Yukawa/mass | untouched; no mass term is inferred from a curvature map | the already typed bilinear/channel questions remain with their owners |
| Q — quantum/BV | finite grammar preserved; partial incidence and exact rejection controls built | Hom rank, EOM factorization, antifield coefficient, and CME wait |
| G — gravity | LC physical-\(R\) equation isolated as \(\operatorname{Ric}^0=0\); W177 remains a negative control | source-selected Einstein locus or separately typed IG/source cancellation |
| I — index/count | no index, multiplicity, or generation count read | held-out topology/count tests remain sealed |
| U — UV/causality | the tested maps are lower-order curvature insertions and do not alter the preregistered principal symbol | global domain, hyperbolicity on a source solution, and loop closure remain open |

## Scoped kills and survives

The following construction routes are killed:

- attributing an LC physical-\(R\) obstruction to pure scalar curvature;
- attributing it to the LC Weyl irrep;
- using the legacy mixed-convention norm as the N4a LC norm;
- transferring the LC Ricci collapse to a nonparallel gamma projector;
- decomposing IG curvature into LC scalar/Ricci/Weyl pieces;
- identifying \(\Omega^{IG}\), \(P_{\rm IG}\), and \(F_A\) by notation alone;
- reporting \(233{,}100\), 36, or 6 as the frozen Hom rank;
- selecting an open term because it cancels W177;
- running EOM factorization before N3; and
- calling the planted Jacobi check a CME test.

The following routes survive:

- an Einstein/source-selected background, for which the LC map vanishes;
- a separately constructed IG map with the same source and target;
- an N3-generated relation that makes the combined LC/IG term factor
  through source equations;
- a finite antifield-quadratic correction already inside N1's grammar, once
  its exact Hom type and coefficient are derived; and
- the prior qualitative conclusion that W177 does not support the current
  full physical-\(R\) gauge identity.

None of these survives by being shaped to W177. Their next information
content will be the constraint surplus after the missing maps and N3
equations are written.

## Next conditional step

N4b should begin only after N3 supplies the Euler derivatives and their jet
symbols. Its input is now narrower:

\[
\Delta_R
=
\frac12\operatorname{Ric}^{0}_{bd}\gamma^d
+\mathcal C_{RR}^{IG}
+\mathcal C_{RR}^{\rm other,frozen}.
\]

It should then:

1. choose and write the \(\Omega^{IG}\) construction fork, including its
   relation or nonrelation to \(F_A\);
2. complete the 20-slot token incidence and invariant contraction table;
3. compute the native-real-form Hom quotient rank;
4. test
   \(\Delta_R=M_R{}^a\mathcal E_a\) against the actual N3 equations;
5. if the factor is exact, fix the coefficient of the corresponding
   predeclared N1 antifield-quadratic term;
6. if it is not exact, compute the finite obstruction class and eliminate
   only the affected source/background stratum; and
7. leave the nonlinear CME to its preregistered later gate.

That sequence gives the proposal a real shot: the construction is allowed
to close on a source-selected equation locus, but missing type data cannot
be converted into either a rescue or a no-go.

## Reproduction

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 \
python3 tests/channel-swings/full20_curvature_irrep_open_bv_probe.py
```

The probe is deterministic and writes no files.
