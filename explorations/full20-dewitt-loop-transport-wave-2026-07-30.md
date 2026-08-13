---
title: "Full-20 DeWitt-loop transport: Gamma-naturality forces the missing normal grading and the returned coflip is uniformly -1"
status: active_research
doc_type: result
created: 2026-07-30
work_item: SOURCE-OWNED-CHIMERIC-BV-CAMPAIGN-S4-DEWITT-TRANSPORT
code:
  - tests/channel-swings/full20_dewitt_loop_transport_probe.py
canon_verdict_change: none
---

# Full-20 DeWitt-loop associated transport

## Result

The next construction swing returns:

```text
ACTUAL-SYM2-DEWITT-LOOP-RECOMPUTED
RAW-20-SLOT-REPRESENTATION-RETURN-NONSCALAR
THREE-COPY-MULTIPLICITY-RETURN-IDENTITY
PAIRING-ONLY-VECTOR-COFLIP-FAILS-GAMMA-PROVENANCE
GAMMA-NATURAL-NORMAL-GRADING-FORCED-UP-TO-GLOBAL-PHASE
ALL-20-DECLARED-MIRROR-MAPS-EXACT
ALL-20-RETURNED-MISMATCHES-CENTRAL-MINUS-ONE
ALL-136-WRITTEN-COEFFICIENT-INTERTWINERS-EXACT
INDEPENDENT-SLOT-PHASE-TWIST-REJECTED
P1/P2-ONE-BIT-WELD-CLOSED-AT-FINITE-ASSOCIATED-BUNDLE-GRADE
GLOBAL-NATIVE-DOMAIN/NONLINEAR-BV/P3-OPEN
```

There is one correction before the positive result.

The tempting extension of the spinor coflip

\[
C_\perp=KJ_{\rm obs}
\]

to vector-spinors by the pairing alone,

\[
C^{\rm pair}_{VS}=\eta_{9,5}\otimes C_\perp ,
\]

is **not** the normalized B5 coflip. It mixes the `imGamma` and low
`kerGamma` provenance copies. In the ordered multiplicity basis
\((I,R_{\rm low})\), the exact mixing matrix is

\[
M_{\rm pair}=
\begin{pmatrix}
-3/7&2\sqrt{10}/7\\
2\sqrt{10}/7&3/7
\end{pmatrix}.
\]

Thus the earlier whole-spinor `-1` could not simply be copied onto twenty
labels. Layer 0 catches the difference.

The written geometry supplies the correction rather than an added phase.
Demanding that the already-owned maps

\[
\Gamma:V\otimes S\to S,\qquad
j=\frac1{14}\Gamma^\sharp,\qquad
P_I=j\Gamma,\qquad P_R=1-P_I
\]

intertwine the coflip uniquely determines the vector factor, up to one common
phase:

\[
C^{B5}_{VS}=(N\eta_{9,5})\otimes C_\perp,\qquad
N=\operatorname{diag}(+1_{TX},-1_{\operatorname{Sym}^2T^*X}).
\]

This corrected map preserves `imGamma`, `kerGamma`, both product-rule X
families, and every one of the twenty declared mirror slots. Transporting it
around the actual DeWitt loop gives

\[
C_{0,s}^{-1}C_{1,s}=-I_{W_s}
\]

for every slot \(s\). The four repeated E-type isotypic components first give
the multiplicity matrices \(-I_3\); only after that calculation is the result
read as twenty equal Schur mismatches. The doubled loop gives \(+I\).

The nine written first-order formulas also intertwine the corrected map on
all 136 independently certified nonzero observer cells. A planted phase on
one mirror pair preserves the static support ledger and the antilinear
involution but fails 28 actual coefficient intertwiners, with normalized
residual \(2\). Therefore the full written coefficient construction removes
the relative phase freedom that the support-only calculation correctly left
open.

## Plain English

We successfully carried all twenty field types around the real geometric
loop.

There were two ways to extend the spinor flip to the spin-\(3/2\) fields. The
obvious one—“just include the indefinite pairing”—was wrong. It blended two
field copies that the B5 construction treats as different. That is exactly
the kind of false positive the Layer-0 rule was designed to catch.

The good news is that no new arbitrary choice was needed to fix it. Requiring
the flip to respect the already-written gamma-trace map forces an extra sign:
base directions get \(+\), while the ten genuine symmetric-metric directions
get \(-\). With that forced factor included:

- every field returns to its declared partner;
- the ordinary group motion is the same on repeated copies and contributes no
  hidden relative datum;
- every returned coflip differs by the same minus sign;
- the doubled loop removes the sign; and
- changing the sign of one field pair still looks legal to the old support
  census, but fails the actual differential.

So the orientation carried by the metric loop and the orientation required by
the X/vertical-symbol sector are now one bit at this finite, fibrewise,
first-order-expression grade. The separate count datum is untouched.

## Layer 0

| phrase | object computed | object explicitly not substituted |
| --- | --- | --- |
| raw return | the endpoint observer-group representation matrix on a slot | a scalar phase |
| Schur mismatch | the linear composition \(C_{0,s}^{-1}C_{1,s}\) after both antilinear maps land in the declared mirror slot | the raw frame/spin return |
| multiplicity matrix | the return on the three isomorphic `S`/`imGamma`/low-`kerGamma` copies after common irrep motion is factored | three independently assumed phases |
| pairing extension | \(\eta\otimes C_\perp\), which is contragredient but mixes \(I\) and \(R_{\rm low}\) | the normalized B5 provenance map |
| B5 extension | \((N\eta)\otimes C_\perp\), derived by \(\Gamma\)-naturality | a fitted sign table |
| differential compatibility | direct covariance of the nine written formulas on 136 nonzero coordinate projections | graph connectivity alone |
| closure grade | exact finite associated-bundle endpoint and formal first-order-expression covariance | a common global closed operator, nonlinear master equation, or physical index |

The corrected extension and the B5 map are `SAME-OBJECT` at this finite
associated-bundle grade. Transfer to the complete five-field native packet
remains `UNCERTAIN`, because the Green/domain and nonlinear fields have not
been supplied.

## Why the extra normal grading is forced

Let

\[
q_a=
\begin{cases}
+1,&a\in TX,\\
-1,&a\in\operatorname{Sym}^2T^*X .
\end{cases}
\]

The independently constructed spinor duality obeys

\[
C_\perp\gamma_a^*C_\perp^{-1}
=q_a\eta_a\gamma_a .
\]

Write a diagonal vector-spinor extension as

\[
C_{VS}(e_a\otimes s)=r_a e_a\otimes C_\perp s .
\]

The equation

\[
\Gamma C_{VS}=C_\perp\Gamma
\]

then demands, direction by direction,

\[
r_a=q_a\eta_a .
\]

All fourteen relative vector phases are fixed. One common phase remains,
which is the expected orientation freedom rather than a new per-slot input.
The same equation implies

\[
C_{VS}j=jC_\perp,\qquad
C_{VS}P_I=P_IC_{VS},\qquad
C_{VS}P_R=P_RC_{VS}.
\]

No endpoint sign or desired B5 phase was used to derive \(N\).

### Why the pairing-only map mixes provenance

Let \(B\) and \(F\) be the normalized partial gamma injections from the four
base and ten fibre directions. Then

\[
I=\sqrt{\frac4{14}}B+\sqrt{\frac{10}{14}}F,\qquad
R_{\rm low}=\sqrt{\frac{10}{14}}B-\sqrt{\frac4{14}}F.
\]

The pairing-only vector extension acts as \(+1\) on \(B\) and \(-1\) on
\(F\). Conjugating \(\operatorname{diag}(1,-1)\) into the
\((I,R_{\rm low})\) basis gives exactly

\[
\begin{pmatrix}
-3/7&2\sqrt{10}/7\\
2\sqrt{10}/7&3/7
\end{pmatrix}.
\]

Its off-diagonal entries are not numerical noise or removable slot phases.
They change the provenance decomposition. The \(N\) factor flips the fibre
action a second time, turning this matrix into \(I_2\).

## Actual loop transport

The metric-fibre generator is recomputed from

\[
h_t=B_t^T\eta B_t .
\]

Its actual gimmel frame is

\[
B_t^{-1}\quad\text{on }TX,\qquad
E\longmapsto B_t^TEB_t\quad\text{on }\operatorname{Sym}^2T^*X .
\]

At the endpoint it reverses:

```text
TX:                 2 legs = 1 positive + 1 negative
Sym^2 T*X:          4 legs = 2 positive + 2 negative
full (9,5) frame:   6 legs = 3 positive + 3 negative
```

The real metric closes, the actual ten-dimensional symmetric-fibre frame is
nontrivial, and the doubled loop returns the full frame to identity.

Let \(R\) be that vector return and \(L\) either Clifford lift. The associated
linear return is

\[
T_S=L,\qquad T_{VS}=R\otimes L .
\]

The result is independent of the central sign choice \(L\mapsto-L\), because
the returned antilinear map uses

\[
C_1=T C_0\overline{T}^{-1}.
\]

### Raw representation motion

Every one of the twenty thin summands is invariant under the endpoint
transport. Its raw coordinate return is generally non-scalar; the largest
centrality defect is exactly \(1\). That is expected because the return is an
observer-group element acting *inside* an irrep.

For each E-type, the three provenance copies have the same raw irrep matrix.
Factoring it gives:

```text
E+:L16+ multiplicity: I_3
E+:R16- multiplicity: I_3
E-:L16- multiplicity: I_3
E-:R16+ multiplicity: I_3
```

Thus the ordinary transport contributes no provenance modulus.

### Returned coflip

The transported corrected coflip lands back in every declared mirror slot
with maximum leakage \(9.4\times10^{-15}\). The returned linear mismatches
have:

```text
maximum centrality defect: 3.4e-15
maximum distance from -1:  4.4e-16
repeated E multiplicities: -I_3
doubled-loop mismatch:     +I
```

The nontrivial \(-1\) is therefore a returned coflip mismatch, not the raw
observer representation matrix.

## The written differential supplies the relative-phase equations

The probe uses the nine already-written primitives:

\[
\begin{array}{ccc}
c & c\Gamma & \delta\\
jc & jc\Gamma & j\delta\\
T & T\Gamma & Q
\end{array},
\qquad
T=P_R\ell,\quad Q=P_RcP_R.
\]

It first checks the actual loop covariance of \(\Gamma,j,P_R\) and all nine
coarse formulas. Maximum normalized operator defect is
\(1.6\times10^{-16}\).

It then evaluates the appropriate base or symmetric-fibre formula on
deterministic generic witnesses for every independently allowed observer
cell:

```text
allowed cells:                  136
base/fibre split:               68 + 68
minimum nonzero amplitude:      6.15e-2
maximum coflip residual:        1.34e-15
```

The coflip vector action is \(v\mapsto N\eta v\). With that input action, all
nine formulas are coflip-even. This does not contradict the preceding
vertical-symbol result. Under the pairing-only vector duality
\(v\mapsto\eta v\), vertical Clifford multiplication is odd; the newly
forced \(N=-1\) on the fibre is precisely the second sign that turns the full
B5 operator relation even.

### Planted phase

One declared mirror pair is multiplied by \(-1\), with every other pair left
unchanged. The plant:

- remains an antilinear involution;
- preserves every slot, mirror, dimension, and static support relation; and
- is accepted by the old permissive support matcher.

It nevertheless fails 28 direct coefficient intertwiner equations, with
maximum normalized residual \(2\). This is the requested discrimination
between support compatibility and a source-owned differential.

## Constraint surplus

Two independent reductions occur:

| stage | initial freedom | independent demand | residual |
| --- | ---: | ---: | ---: |
| vector-spinor coflip extension | fourteen unit vector phases | fourteen \(\Gamma\)-intertwining equations | one common normalization |
| twenty mirror-pair extensions | ten pair phases at static-support grade | actual nonzero differential intertwiners on a connected 136-cell coefficient graph | one common phase |
| DeWitt endpoint | no phase fitted to the outcome | returned coflip mismatch | common phase returns as \(-1\) |

The construction is therefore informative under the standing
constraint-surplus rule. The normal grading and relative slot phases were not
chosen to make the loop nontrivial; they were fixed by \(\Gamma\) and the
written differential before the endpoint mismatch was read.

## Datum ledger

At exact finite associated-bundle and formal first-order-expression grade,
the live ledger is now:

```text
D1 = one Z/2 orientation carried jointly by P1 and P2
D2 = P3, the still-separate physical chiral-index/count datum
```

This is a **grade-qualified reduction from three pieces to two**. It does not
mean that the source action derives either datum internally, and it does not
turn the orientation bit into a generation count. The earlier Layer-0
retraction remains in force:

```text
three multiplicity blocks != three generations
symbol support != chiral index
Z/2 orientation != P3 count
```

## What moved and what did not

### Moved

- The actual fibre-loop-to-\(C_\perp\) identification is closed on all twenty
  normalized provenance summands at finite associated-bundle grade.
- The pairing-only extension is recorded as a refuted near-miss rather than
  silently used.
- The missing vector-spinor factor is identified as the program-native normal
  grading \(N=(+1_4,-1_{10})\), uniquely forced up to a global phase.
- The twenty endpoint mismatches are uniformly \(-1\), after the required
  multiplicity computation.
- The written full coefficient differential rejects relative mirror-pair
  phases that static support admitted.
- P1 and P2 now share one orientation datum at the stated grade.

### Unchanged

- The fail-closed five-field native packet still lacks a common closed domain
  and nonlinear completion.
- W177 remains a nonstationary background on which the current physical
  \(R\)-sector gauge identity is obstructed.
- No absolute formal-adjoint special-edge sum is promoted without the complete
  pairing/Green convention.
- `SA-Y1` and physical `SA-Y8` still need the explicit vertical odd-form mass
  bilinear and four-dimensional retention test.
- P3 remains separate and unconstructed.
- No claim, canon verdict, public posture, physical index, count, vacuum, or
  spectrum moves.

## Highest-information next step

The next swing is now the second item of the prior ordered handoff:

> Write the vertical odd-form mass bilinear
> \[
> B_v(\psi,\chi)=\psi^TC_{14}\Gamma(v)\chi,
> \qquad v\in V_{10},
> \]
> alongside the sesquilinear \(K\Gamma(v)\) comparator, and decompose both
> across the normalized twenty-slot transport just constructed.

The build should derive, before any mass interpretation:

1. the charge-conjugation matrix \(C_{14}\) and its transpose symmetry;
2. Grassmann exchange symmetry of \(B_v\);
3. the exact observer-slot pairing table, with the new \(N\eta C_\perp\)
   transport applied;
4. the stabilizer of a nonzero vertical \(v\);
5. whether the same channel survives a declared \(Y^{14}\to X^4\) retention
   map; and
6. the Layer-0 relation to `SA-Y1` and the still-distinct physical `SA-Y8`
   scalar.

That is now the direct information-gaining decider. Curvature compensators,
global domains, and nonlinear BV closure should remain downstream until the
mass channel earns its physical type.

## Reproduction

```bash
python3 tests/channel-swings/full20_dewitt_loop_transport_probe.py
```

The new probe and the following independent owners all pass together:

```text
actual_fibre_cperp_b5_naturality_probe.py
vertical_krein_weld_probe.py
full20_observer_projector_support_probe.py
full20_native_polarization_probe.py
shiab_b5_observer_symbol_multiplicity_matrix.py
shiab_b5_krein_mirror_orbit_reduction.py
shiab_b5_native_packet_contract.py
```
