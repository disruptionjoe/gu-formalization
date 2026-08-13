---
title: "Actual-fibre C_perp / B5 naturality start: the DeWitt lift preserves the Krein Z/2, but normalized 20-slot centrality is an associated-bundle map, not support data"
status: active_research
doc_type: result
created: 2026-07-29
code: tests/channel-swings/actual_fibre_cperp_b5_naturality_probe.py
canon_verdict_change: none
---

# Actual-fibre `C_perp` / B5 naturality start

## Result

`K-LINE-MONODROMY-EXACT-C_PERP-ASSOCIATED-MAP-OPEN`.

The actual metric-fibre calculation can be done.  Starting with

\[
h_t=B_t^{T}\eta B_t,\qquad \eta=\operatorname{diag}(1,1,1,-1),
\]

the induced orthonormal frame on the program-native gimmel carrier is

\[
F_t=
\left(B_t^{-1}\right)
\oplus
\left[E\longmapsto B_t^T E B_t\right]
\quad\text{on}\quad
TX\oplus\operatorname{Sym}^2T^*X.
\]

The second summand is an isometry from the reference trace-reversed DeWitt
form to the DeWitt form at \(h_t\).  The full frame equation holds along the
loop to `5.55e-16`; a planted lift that leaves the symmetric-tensor factor
fixed fails with defect `1.00`.

At the generator endpoint:

| carrier part | positive legs reversed | negative legs reversed |
| --- | ---: | ---: |
| `TX`, signature `(3,1)` | 1 | 1 |
| `Sym²T*X`, DeWitt signature `(6,4)` | 2 | 2 |
| full gimmel carrier `(9,5)` | 3 | 3 |

Thus the actual `Sym²` action is nontrivial, but its positive-orientation
contribution is even.  It does not erase the base result:

\[
\det(H_+)=-1,\qquad K_1=-K_0 .
\]

The doubled loop returns the full frame and gives `+1`.  The repository's
Krein-line `Z/2` therefore survives the move from an abstract `(9,5)` mixed
plane to the actual `TX + Sym²T*X` DeWitt carrier.

A reference Clifford lift of the computed endpoint return then:

- returns `J_obs` exactly;
- returns the distinct quaternionic `J_H` exactly;
- preserves base and internal chirality separately;
- preserves both algebraic gamma-traceless projectors, of ranks `12` and
  `288`; and
- gives
  \[
  C_0^{-1}C_1=-I,\qquad C_\perp=KJ_{\rm obs},
  \]
  on the irreducible spinor factor.

That is a genuine construction-level advance.  It is not yet the requested
20-slot theorem.  The B5 ledger supplies an observer representation
decomposition and a support matrix, not a connection or normalized endpoint
identification on its multiplicity/provenance bundles.  In the conservative
sign-only part of its commutant, all `2^10` mirror-pair assignments preserve
the checked support, mirror, dimension, provenance, and special-edge facts.
Only two are central.  Modulo a common sign, `2^9` relative classes remain.

The probe plants one such noncentral return.  A permissive support matcher
accepts it; an actual centrality test rejects it.  Therefore:

- the actual-fibre Krein monodromy **passes**;
- the reference irreducible-spinor `C_perp` return **passes**;
- inference from support preservation to normalized 20-slot centrality is
  **killed**; and
- the physical one-bit P1/P2 merger is **open at one named
  associated-bundle map**, not refuted.

## Layer 0: object and map identity

Layer 0 runs before reading any shared sign as a shared datum.

| term | object used here | map or predicate | not identified with |
| --- | --- | --- | --- |
| metric loop | loop of Lorentzian forms \(h_t\) in the fibre of `Met(X)` | congruence \(B_t^T\eta B_t\) | a Lorentz transformation fixing \(\eta\) |
| actual ten | \(\operatorname{Sym}^2T^*X\), including diagonal tensors | \(E\mapsto B_t^TEB_t\) with the DeWitt form | \(\Lambda^2\oplus\Lambda^3\), which has no diagonal sector |
| Krein line | orientation line of the positive nine-plane in the `(9,5)` frame | character \(\det(H_+)\in\{\pm1\}\) | an antilinear duality or a table of slot phases |
| `K` | Clifford product/pairing representative for the positive frame | returned matrix \(K_1=-K_0\) in the reference lift | positive-Hilbert bookkeeping |
| `J_obs` | observer-factor antilinear real structure | `J_obs²=+1`; observer duality input | GU's quaternionic `J_H` |
| `J_H` | quaternionic structure on the `Cl(9,5)=M(64,H)` spinor | `J_H²=-1`; returned separately | `J_obs`, despite both being antilinear |
| `C_perp` | Krein-dual antilinear map \(KJ_{\rm obs}\) | reference mismatch \(C_0^{-1}C_1\) | the Krein line by itself |
| RS projectors | algebraic gamma-traceless projectors on `V4⊗S4` and `V10⊗S10` | covariance under the reference endpoint lift | a closed differential/domain |
| 20 B5 slots | 12 `E` slots in `S`, `imGamma`, `kerGamma`, plus 8 `X` slots | observer branching and 136-cell support ledger | normalized associated bundles with chosen transport |
| count | physical chiral/Fredholm index | not mapped in this lane | multiplicity, number of blocks, or this `Z/2` |

The first seven rows are connected at frame and Clifford grade by the probe.
The passage from that result to normalized maps on the ninth row is precisely
the open map.  No statement about the tenth row follows.

## Construction fork

This stays on the program-native fork:

- `TX + Sym²T*X`, with the actual trace-reversed DeWitt/gimmel metric;
- indefinite Krein pairing;
- factorized `Cl(9,5)=Cl(3,1) hat-tensor Cl(6,4)` only as a matrix model of
  the computed frame return;
- both product-rule RS projectors; and
- all 20 observer-labelled B5 slots with all three provenance copies and the
  full `X` sector.

Two hostile controls are explicit:

1. holding the ten-dimensional fibre frame fixed is rejected by the DeWitt
   frame equation; and
2. checking only support and mirror labels accepts a planted noncentral slot
   return, while the strict scalar test rejects it.

No exterior `6+4` carrier, positive-Hilbert pairing, one-quaternionic-line
reduction, or freely normalized slot table is substituted.

## The actual induced frame

For a vector-frame column \(v\), the base frame is \(B_t^{-1}v\), since

\[
(B_t^{-1})^T h_t B_t^{-1}=\eta .
\]

For a covariant symmetric tensor \(E\), use

\[
Q_t(E)=B_t^TEB_t .
\]

Writing

\[
V_h(E,F)=
\operatorname{tr}(h^{-1}Eh^{-1}F)
-\frac12
\operatorname{tr}(h^{-1}E)\operatorname{tr}(h^{-1}F),
\]

cyclicity of trace gives

\[
V_{h_t}(Q_tE,Q_tF)=V_\eta(E,F).
\]

This is the missing naturality check in the earlier abstract `(9,5)` habitat
probe.  It also explains the endpoint census.  If the mixed loop reverses one
spacelike base leg and the timelike base leg, the symmetric square reverses
the four tensors containing exactly one of those two legs.  Two are positive
spatial off-diagonal modes and two are negative space-time modes.  Diagonal
tensors are present and return unchanged.

## What the reference Clifford lift earns

In a DeWitt-orthonormal `6+4` frame, the endpoint return is diagonal with four
reversed vertical legs.  Together with the two reversed base legs, the
Clifford product of the six corresponding generators supplies a reference
lift.  Its overall sign is irrelevant to conjugation of `K`, `J_obs`, `J_H`,
chirality, or the projectors.

This lift proves existence of a coherent frame-grade return with central
spinor mismatch.  It does **not** prove uniqueness of transport on the
observer multiplicity bundles.  In particular, returning `J_obs` and `J_H`
under this lift is not permission to rename them: their squares and their
roles remain different.

## Parameter, choice, and constraint-surplus ledger

The geometric computation fits no continuous parameter.  Once the generator
representative and the repository's DeWitt coefficient `1/2` are fixed, its
Krein character is forced.

| layer | free choices before constraints | source-owned constraints applied | residual |
| --- | ---: | ---: | ---: |
| actual 14-frame return | 0 fitted continuous parameters | DeWitt frame equation and loop closure | fixed |
| reference Clifford lift | one global `±` lift choice | conjugation makes it inert for the tested returns | 0 relevant |
| sign-only 20-slot commutant | 10 mirror-pair signs | mirror/support/dimension constraints | 10 signs |
| relative slot return | quotient one common sign | no associated-bundle transport equation exists yet | 9 binary moduli |

At the current support grade, the conservative constraint surplus for
centrality is therefore

```text
independent source-owned relative-phase constraints - relative sign choices
= 0 - 9
= -9.
```

This is only a lower-bound model of the freedom: allowing unit phases or
higher multiplicity commutants can enlarge it.  The negative surplus does not
show that a source-owned connection cannot select the central return.  It
shows that the present support ledger does not.

## Ratified L1-L7 classification

Layer 0 is the semantic precondition in the earlier table.  It is not an
eighth structural axis.  The candidate's actual seven-axis specification is:

| axis | class | specification in this construction | literature / repository anchor | class-assumption signature |
| --- | --- | --- | --- | --- |
| L1 — substrate | **(a) smooth principal/associated bundle** | The substrate in scope is the smooth pseudo-Riemannian frame/Clifford/RS bundle over the Lorentzian locus of `Y14 = Met(X)`, with tangent carrier `TX + Sym²T*X`. | Lawson–Michelsohn, *Spin Geometry*; repository realization `tests/W131_covariant_operator_y14.py`. | Preserves the smooth-bundle assumptions of the standard no-go arena; this lane claims no scope exit at L1. |
| L2 — observer | **(a) finite Turing observer** | A finite algebraic observer computes the `Spin(3,1) × Spin(6,4)` branching, the 20 labelled slots, and their finite support matrix.  No oracle, hypercomputation, or consensus observer is used. | The finite observer ledger `tests/shiab_b5_observer_symbol_multiplicity_matrix.py`. | Preserves the ordinary finite-observer assumption.  Its limitation is explicit: it observes support but does not manufacture normalized bundle transport. |
| L3 — pairing | **(a) Cartesian/smooth associated-bundle pairing** | The channel is the smooth tensor/associated-bundle channel, with the physical duality written as the Krein-composed map `C_perp = K J_obs`.  The signature of that pairing is isolated at L7 rather than smuggled into this axis. | Lawson–Michelsohn for associated Clifford bundles; `vertical_krein_weld_probe.py` for the repository map. | Preserves the smooth pairing class; no anomaly or centrality escape is claimed from L3 alone. |
| L4 — causal order | **(a) total-order Lorentzian** | `X` remains a smooth Lorentzian base.  The parameter around the metric-fibre generator is a homotopy parameter, not a replacement physical causal order. | O'Neill, *Semi-Riemannian Geometry*; the Lorentzian-locus construction in `W131`. | Preserves the total smooth Lorentzian assumption. |
| L5 — emergence | **(a) specific-object substrate** | The calculation uses the specified DeWitt/gimmel metric and a specified generator loop.  It invokes no RG fixed point, universality class, attractor, or topological-phase emergence. | The explicit `fiber_metric` / `gimmel` construction in `W131`. | Preserves the specific-object assumption. |
| L6 — coordination loop | **(a) no observer–substrate feedback loop** | The metric loop is a topological probe inside the substrate, not a feedback law coupling observer extraction back into substrate dynamics. | Conservative protocol baseline; no additional coordination dynamics is introduced. | Preserves the no-loop assumption. |
| L7 — positivity / state-space signature | **(b) indefinite Krein with the existing ghost-parity `Z2` superselection** | The tangent signature is `(9,5)` and the spinor/RS bilinear uses the program-native Krein pairing.  This lane computes its positive-orientation-line monodromy; it does not rederive the probability rule or claim positivity of the full dynamics. | Turok–Bateman/Mannheim indefinite-state-space line as typed by the ratified protocol; repository Krein anchors in `sig_b5_habitat_probe.py` and `vertical_krein_weld_probe.py`. | Breaks the positive-definite-Hilbert premise only.  On the conservative reading, this is L3 with its otherwise-hidden signature and superselection datum made explicit. |

This classification makes the negative result sharper: L1-L6 remain on the
conservative smooth/finitary/no-feedback baseline.  The heterodox lever is
localized at L7, and even there the exact Krein-line character does not by
itself select normalized phases on the 20 L2 observer slots.

## Smallest next construction

Build one source-owned transport

\[
\tau_t:\mathcal E_{\mathrm{B5},h_0}\longrightarrow
\mathcal E_{\mathrm{B5},h_t}
\]

on

\[
\mathcal E_{\mathrm{B5}}=\bigoplus_{s=1}^{20}\mathcal E_s,
\]

covering the computed frame
\[
B_t^{-1}\oplus\operatorname{Sym}^2(B_t^*)
\]
and satisfying, in normalized slot pairings:

1. `tau` preserves the two RS projectors;
2. `tau` intertwines the written horizontal and vertical principal symbols;
3. `tau` intertwines each slot with its `C_perp` mirror; and
4. `tau` respects the provenance/multiplicity connection actually supplied by
   the differential, not an arbitrary trivialization.

Then compute the twenty endpoint mismatch scalars \(u_s\).  The one-bit weld
passes exactly if all \(u_s\) are the same central `-1`.  A relative
provenance or `X` value kills the merger.  Failure to define `tau` from the
written differential leaves the result open; support counts cannot replace
it.

## Validation

Executed successfully:

```text
python3 tests/channel-swings/actual_fibre_cperp_b5_naturality_probe.py
```

All scoped checks pass, including both planted controls.  This exploration
changes no claim, canon verdict, source-action row, count datum, or public
posture.
