---
title: "Eric/Curt Wave 3D-B2C3: rolled Omega source matrix and canonical-Shiab collision"
status: active_research
doc_type: construction_result
created: 2026-07-31
lane: "1"
work_item: ECW3D-B2C3-ROLLED-OMEGA0-OMEGA1-SOURCE-ACTION-AND-SHIAB-MIDDLE-BLOCK
registry: lab/process/eric-curt-wave3d-b2c3-rolled-omega-source-shiab.json
probe: tests/channel-swings/eric_curt_wave3d_b2c3_rolled_omega_source_shiab_probe.py
grade: "EXACT SOURCE-MATRIX TRANSCRIPTION and exact canonical-Shiab candidate collision. The draft fixes the physical Omega1(S)+Omega0(S) block shape but explicitly leaves the Shiab selector in a family. In the active trace-reversed Cl(9,5) port, the repo's canonical Clifford-contraction candidate produces A(k)=K(k)Gamma-M(k), retains a rank-128 square-zero Jordan remainder, and admits no positive full-carrier one-time symmetrizer. Its Jordan endpoints are exactly the two null-Dirac halves of the physical d nu coupling. A characteristic quotient is algebraically positive and observer-nontrivial, but is not lawful without a distinct action-derived ghost/Noether map; the displayed square symbol has no nonzero polynomial right syzygy. The full Shiab-family/Bianchi and source-derived constraint searches remain open."
claim_status_change: false
canon_change: false
public_posture_change: false
---

# Wave 3D-B2C3 — rolled `Omega0 + Omega1` source matrix and Shiab collision

## Plain-English result

The source material helped, but not by simply confirming the successful
operator from the preceding swing.

Weinstein's 2021 draft really does write the missing coupled fermion matrix.
It treats a spinor-valued one-form `zeta` and a spinor zero-form `nu` as
physical fields, with a Shiab-of-derivative block, an ordinary derivative
coupling from `nu` into the `zeta` equation, and a codifferential returning
from `zeta` into the `nu` equation.

The draft does **not** uniquely write the Shiab inside that slot. It says the
Shiab belongs to a family, says the old choice was made using a Bianchi
identity, and says those calculations could not be located. That corrects the
stronger premise that the manuscript forces one Clifford contraction.

The most canonical natural contraction already constructed in this repo was
therefore inserted as a serious candidate, not as a source fact. It gives an
exact middle symbol

\[
A(k)=K(k)\Gamma-M(k),
\qquad
K(k)=k\otimes 1,
\qquad
M(k)=1\otimes c(k).
\]

That candidate does not reproduce the successful full-carrier Clifford
completion from B2C2. It brings back the same kind of rank-128 square-zero
Jordan defect. So the useful conclusion is not "the full carrier fixes the
problem." It is:

> The full carrier has a positive completion, but the first canonical
> source-shaped Shiab candidate does not select it.

The failure is unusually informative. Its bad Jordan endpoints are exactly
the two null-Dirac halves emitted by the physical `d nu` coupling. There is a
clean mathematical quotient that removes them, has a positive right-`H`
symmetrizer, and leaves a nonzero observed quotient. But the source calls
`nu` physical matter, not a ghost. Quotienting those modes now would turn a
physical coupling into gauge redundancy without an action-derived reason.

The next construction target is therefore sharper: search the complete
source-allowed Shiab family and the Bianchi/formal-adjoint/constraint
conditions that were supposed to select it. If no family member removes the
defect directly, derive a propagated constraint that removes the generalized
partners while retaining the physical `nu` endpoints. Do not quotient them
unless a distinct ghost and Noether identity are independently constructed.

## 1. Direct transcription of the source matrix

Draft equations 9.16--9.18 use

\[
\nu,\bar\nu\in\Omega^0(Y,S),
\qquad
\zeta,\bar\zeta\in\Omega^1(Y,S),
\]

and, after regrouping the four chiral rows, display the compact architecture

\[
D_\omega^{\mathrm F}
=
\begin{pmatrix}
\star\!\odot\,d_{A_\omega} & d_{A_\omega}\\
-d_{A_\omega}^{*} & 0
\end{pmatrix}
\tag{1}
\]

in 9.16. The Euler-vector packaging in 9.18 writes the lower component with
the opposite display sign:

\[
\Upsilon_\omega^{\mathrm F}
=\star
\begin{pmatrix}
d_{A_\omega}\nu+\star\!\odot\,d_{A_\omega}\zeta\\
d_{A_\omega}^{*}\zeta\\
\bar\nu\zeta+\bar\zeta\nu+\odot\,\bar\zeta\zeta
\end{pmatrix}.
\tag{2}
\]

The probe keeps both lower-left signs. Their admitted-section evolution is
identical at principal-symbol order. This does not make the signs physically
equivalent: the source's Hodge/density-dual placement, formal adjoint, Green
form, and conserved current still have to select the physical convention.

The draft immediately says that other versions have a nonzero lower-right
quadrant. Thus the zero southeast block is a displayed version, not a theorem
that every GU action must use it.

## 2. Source correction: the Shiab selector is open

Sections 8 and 9 do not supply one uniquely forced spinorial Shiab.

- Equation 8.1 describes a family of Shiab contractions assembled from
  invariant forms, Hodge stars, commutators or anticommutators, and weights.
- The prose says the former representation-theoretic selection used the
  Bianchi identity, but the original calculations were unavailable.
- Equations 9.2--9.3 select one explicit Einstein-like **bosonic** contraction
  for the action being explored there.
- Equation 9.16 places `star-shiab` in the fermionic matrix without giving a
  complete spinorial selector calculation.

This agrees with the repo's existing Shiab canon:

- a natural real Clifford-contraction Shiab exists;
- equivariance does not make it unique;
- after right-`H`, a real family remains; and
- the source-forced selector identity is open.

The correct source collision is consequently mixed:

| claim | disposition |
| --- | --- |
| physical `Omega1(S)+Omega0(S)` matrix and `d/d*` slots | `SOURCE-CONFIRMS` |
| `nu` and `zeta` are physical fields in a Dirac-like equation | `SOURCE-CONFIRMS` |
| the Shiab is selected from a family by a Bianchi-type criterion | `SOURCE-CONFIRMS` as intent |
| the 2021 draft uniquely forces the repo's Clifford contraction | `SOURCE-CORRECTS` — it does not |
| exact spinorial selector, real-form port, formal adjoint, and domain | `SOURCE-SILENT` |
| Jordan result and any proposed repair | `SOURCE-SILENT`; repo computation |

## 3. The canonical candidate and its exact symbol

The candidate used here is the repo-canon natural map

\[
\Phi(e^i\wedge e^j\otimes s)
=e^i\otimes c(e^j)s-e^j\otimes c(e^i)s.
\tag{3}
\]

For the exterior-derivative symbol

\[
(k\wedge\zeta)_{ab}=k_a\zeta_b-k_b\zeta_a,
\]

equation (3) gives, component by component,

\[
(\Phi\,\sigma_d(k)\zeta)_a
=k_a\sum_b c(e^b)\zeta_b-c(k)\zeta_a.
\]

Therefore

\[
\boxed{A(k)=K(k)\Gamma-M(k)}.
\tag{4}
\]

This formula was derived before inspecting the new evolution or Jordan
target. No characteristic projector, eigenvector, fitted coefficient, or
external datum appears.

It obeys the off-shell complex identity

\[
A(k)K(k)=0,
\tag{5}
\]

because `d^2=0`. It is nevertheless not the full Clifford multiplication:

\[
A(k)\ne \pm M(k).
\]

In the normalized gamma-trace splitting

\[
T^*Y\otimes S=\operatorname{im}\Gamma^\dagger\oplus\ker\Gamma,
\]

the RS-to-RS block of `A(k)` is exactly `-Q(k)`, where `Q(k)` is the
compressed W131 symbol, and both trace/RS coupling blocks are nonzero.

## 4. The rolled principal operator

After the density-dual/Hodge Riesz identification needed to compare equations
on one carrier, the two displayed lower-left conventions give

\[
D_\pm(k)=
\begin{pmatrix}
K(k)\Gamma-M(k) & K(k)\\
\pm C_g(k) & 0
\end{pmatrix},
\qquad
C_g(k)K(k)=q(k)1.
\tag{6}
\]

The continuous Lorentz time covector on the admitted section is
noncharacteristic for both signs. The signs cancel in the corresponding
section evolution matrices, so both principal evolutions are equal.

For a unit section-spatial covector `xi`, let

\[
E_\xi=D(dt)^{-1}D(\xi).
\]

The probe finds exactly

\[
N_\xi:=E_\xi^2-1,
\qquad
\operatorname{rank}N_\xi=128,
\qquad
N_\xi^2=0,
\qquad
N_\xi\ne0.
\tag{7}
\]

Thus `E_xi` is not semisimple. A positive definite symmetrizer for the full
displayed one-time system cannot exist: such a symmetrizer would make the
real characteristic generator similar to a Hermitian matrix and hence
diagonalizable.

The operator remains exactly right-`H` compatible. Indefinite compatibility
therefore survives; it is not enough to provide positive one-time energy.

## 5. Exact location of the Jordan endpoints

Let

\[
k_\pm=\xi\pm dt.
\]

Each is null on the admitted `(3,1)` section, `c(k_\pm)` has rank 64, and
the two intrinsic maps

\[
K(k_\pm)\ker c(k_\pm)
\]

have rank 64. The target-blind collision is

\[
\boxed{
\operatorname{im}N_\xi
=K(k_+)\ker c(k_+)
\oplus
K(k_-)\ker c(k_-).
}
\tag{8}

This explains the obstruction without making it gauge. It says the Jordan
endpoints are generated from null spinors through the same derivative block
that couples physical `nu` into the one-form field `zeta`.

The source descriptions reinforce that Layer-0 reading:

- 9.16 calls `nu` and `zeta` distinct fermionic fields;
- 9.17 calls their coupled equation Dirac-like;
- the Oxford/Portal account also calls them two separate physical fields; and
- later generation language associates the zero-form sector with matter, not
  with a parity-shifted ghost.

An independent RS parameter or BV ghost may live in an isomorphic spinor
bundle. It is not the same object as physical `nu`.

## 6. Why characteristic exactness is not yet gauge exactness

Define the natural inclusion

\[
R_d(k)=
\begin{pmatrix}
K(k)\\0
\end{pmatrix}.
\]

Equation (6) gives

\[
D_\pm(k)R_d(k)
=
\begin{pmatrix}
0\\ \pm q(k)1
\end{pmatrix}.
\tag{9}

This vanishes on the characteristic cone and fails away from it. It is a
matrix factorization of the wave polynomial, not an off-shell Noether or BV
identity.

There is a stronger local obstruction. Because `D(dt)` is invertible, the
polynomial right-syzygy module of the displayed square symbol is zero. If a
local polynomial symbol `R(k)` obeyed

\[
D(k)R(k)=0
\]

for every `k`, then `R` would vanish on the open set where `D` is invertible
and hence vanish identically. The displayed physical block alone therefore
cannot emit a nonzero local spinor gauge generator.

A lawful odd gauge symmetry must do at least one of the following:

1. come from a larger coupled field/equation system with cancellations outside
   this square block;
2. identify (6) as a gauge-fixed representative and derive the ungauge-fixed
   parent plus its independent ghost; or
3. use another source-allowed Shiab/lower-right block whose symbol is actually
   degenerate for a source-derived symmetry.

## 7. A useful but conditional quotient control

The probe nevertheless tests the tempting quotient rather than dismissing it.
For each unit `xi`, take the complete two-root image

\[
G_\xi
=\operatorname{im}K(k_+)\oplus\operatorname{im}K(k_-),
\qquad
\dim_\mathbb C G_\xi=256.
\]

Let `P_xi` be the orthogonal complement projector and

\[
Q_\xi=P_\xi E_\xi P_\xi.
\]

On three coordinate directions and a generic `(1,2,3)` direction, the probe
verifies

\[
Q_\xi^2=P_\xi.
\tag{10}
\]

The conditional quotient is semisimple. It has the explicit positive
right-`H` compatible symmetrizer

\[
H_\xi=P_\xi+Q_\xi^\dagger Q_\xi,
\qquad
H_\xi Q_\xi=Q_\xi^\dagger H_\xi,
\qquad
H_\xi\ge P_\xi.
\tag{11}

Observation also descends **if** the observed side is quotiented by the
corresponding observed derivative image. The induced observed quotient has
constant complex rank 384 in all four tested directions.

This is valuable conditional knowledge: if a distinct action-derived ghost
later owns `R_d`, the exact physical-symbol repair is already available.

It is not permission to perform that quotient now. Quotienting physical
`d nu` merely because it repairs hyperbolicity would repeat the orthodox
reflex in a subtler form: it would fit the interpretation to the desired PDE
answer and erase a source-labeled matter channel.

## 8. The better physical repair target: restriction, not erasure

The Jordan geometry suggests a second conditional route. On a size-two
Jordan block, quotienting the endpoint keeps the generalized vector as an
artificial quotient eigenvector. If the endpoint is physical, the preferable
operation is a propagated source constraint that removes the generalized
partner while retaining the endpoint.

A future source-derived constraint `Q_src(xi)` must be frozen without using
`N_xi` as its target and must pass

\[
Q_{\rm src}(\xi)E_\xi=B(\xi)Q_{\rm src}(\xi),
\]

\[
\ker Q_{\rm src}(\xi)\subseteq\ker N_\xi,
\qquad
\operatorname{im}N_\xi\subseteq\ker Q_{\rm src}(\xi),
\]

while retaining all physical `nu` polarizations and nonzero observation. The
lower-row equation, a Bianchi identity, or the missing Shiab selector are the
source-directed places to derive it. `Q_src=N_xi` chosen after seeing the
defect is forbidden.

## 9. The trace-reversed Frobenius-fibre boundary

This computation keeps the repo's active trace-reversed geometry explicit.

- The admitted base contributes signature `(3,1)`.
- The trace-reversed Frobenius metric on `Sym^2(T*X)` contributes `(6,4)`.
- The active total carrier is therefore `(9,5)` with
  `Cl(9,5)=M(64,H)` and the native right-`H` structure.

The 2021 draft pages containing (1) are written in a `(7,7)` presentation.
Transporting the matrix architecture to the active `(9,5)` carrier is a repo
construction justified by the later trace-reversal line; it is not an
identity between the two real theories. The right-`H`, formal-adjoint, Hodge,
and domain questions must be rerun on Curt's literal `(7,7)` rival before any
track convergence. Curt remains formally separate and no third lane is
promoted.

## 10. Layer 0 dictionary

| shared phrase | object here | must not be identified with |
| --- | --- | --- |
| zero-form spinor | physical `nu in Omega0(S)` | ghost in a distinct parity-shifted copy |
| derivative `d` | physical off-diagonal block `nu -> zeta` | BV differential |
| Shiab | open source family/slot | unique canonical Clifford contraction |
| canonical candidate | repo's natural Clifford contraction | Weinstein's recovered Bianchi-selected operator |
| characteristic exactness | `D(k)R_d(k)=0` only when `q(k)=0` | off-shell Noether identity |
| Jordan endpoint | observed physical null-Dirac emission | automatically unphysical gauge mode |
| conditional quotient | mathematical discriminator | accepted physical phase space |
| positive symmetrizer | principal quotient Hilbert form | native Krein form or global analytic domain |
| generation | observed chiral/index object | matrix block, kernel rank, or cochain degree |

## 11. Seven-axis read

| axis | result |
| --- | --- |
| L1 algebra | exact canonical-Shiab symbol, syzygy no-go, Jordan factorization, and conditional quotient pass |
| L2 representation | gamma-trace blocks and right-`H` compatibility exact on active `Cl(9,5)`; full Shiab family open |
| L3 geometry | trace-reversed `(9,5)` port explicit; draft `(7,7)` real-form transport not identified |
| L4 dynamics | canonical displayed-shape full system is non-semisimple; conditional quotient is positive; source constraint and domain open |
| L5 observation | raw `512+128` carrier retained; Jordan endpoints observed; conditional quotient observation rank 384 |
| L6 physics | source calls `nu/zeta` physical; no gauge erasure, mass, chirality, generation count, or SM recovery claimed |
| L7 empirical | no new prediction or fit claimed |

The canonical candidate has zero fitted PDE parameters, so its negative result
has real information content. The conditional quotient also has zero fitted
coefficients but has an unclosed semantic debit: no action-derived ghost or
constraint owns it.

## 12. Non-regression and datum disposition

- B2B remains exact for isolated `ker Gamma`.
- B2C1's fixed quotient that erases the observer carrier remains killed.
- B2C2A's ordinary `tau`/BRST carrier mismatch remains killed.
- B2C2's positive `1 tensor c(k)` completion remains a valid mathematical
  control, not the canonical source-shaped Shiab result.
- The physical `nu/zeta` interpretation is retained.
- P1/P2/P3 were not used. They cannot select a Shiab, turn `nu` into a ghost,
  choose a constraint, or repair the local Jordan symbol.
- No stationarity, CME, nonlinear constraint propagation, analytic domain,
  mass, index, generation count, cosmological prediction, or Standard Model
  recovery is claimed.

The executable probe passes `22 exact + 11 planted = 33` checks.

## 13. Next gate

`ECW3D-B2C4-SHIAB-FAMILY-BIANCHI-ADJOINT-AND-CONSTRAINT-SELECTOR`

Run the source-authorized family rather than treating the first canonical
member as final:

1. import the frozen contract/wedge chiral Shiab basis already constructed in
   the repo and build every rolled principal block before testing PDE targets;
2. impose the source-suggested Bianchi/gauge-perpendicularity condition, the
   action's density-dual/formal-adjoint condition, active right-`H`, and the
   trace-reversed `(9,5)` real form;
3. solve the surviving coefficient variety exactly, including lower-right
   block and Hodge-sign rivals as separately labeled source-silent choices;
4. collide every survivor with semisimplicity, uniform positive
   symmetrizability, and observation without fitting to the Jordan image;
5. if no full-carrier member passes, derive a propagated lower-row/Bianchi
   constraint that restricts generalized partners while retaining all
   physical `nu` endpoints; and
6. only if an enlarged action independently emits a distinct spinor ghost and
   off-shell Noether identity, rerun the conditional quotient as physical BV
   cohomology.

If the whole source-allowed family fails, the alternative route should close
the ordinary one-time full-carrier repair and move to the explicitly admitted
ultrahyperbolic/Krein boundary-value problem. That would still be a genuine
construction attempt, not an orthodox dismissal.
