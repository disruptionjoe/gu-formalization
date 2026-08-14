---
artifact_type: exact_pairing_ownership_and_layer0_result
created: 2026-08-13
run_id: RUN-20260814-002843-gu-w-mirror-action-pairing-ownership
status: CURRENT_SPIN_NATURAL_ACTION_PAIRING_CLASS_EXCLUDES_TRACE_HQ__REALITY_SELECTS_NEITHER__NONZERO_FERMION_BV_DOMAIN_OPEN
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE_SILENT_TRACE_HQ_AS_DEFINING_FERMION_FORM_AND_W_MIRROR_SELECTOR
ledger_rows: [RA-G2, LT-SM3, AC-G1a]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 W/mirror action-pairing ownership

## Result first

The trace-`H_q` W/mirror Witt pairing is **not** the pairing currently owned by
the source-compatible equation-9.16 fermion action classification.

The complete local Spin-natural, degree-diagonal action calculation had
already produced two and only two projective pairing lines on the rolled
fermion carrier:

\[
P_{\rm sym}=\eta_{14}\otimes B,
\qquad
P_{\rm skew}=\eta_{14}\otimes BJ.
\]

The trace compatibility form is a third object,

\[
P_{\rm tr}=\eta_{14}\otimes iB\gamma(q_g).
\]

On both the rank-192 `W` sector and its ASD mirror, all three bilinear forms
have full rank. Their bilinear `W`--mirror cross restrictions vanish. But the
two action restrictions span dimension two, while adding the trace form raises
the span to dimension three. A three-entry witness over `Q(i)` is

\[
\begin{pmatrix}
0&0&-3/8\\
3i/8&-3i/8&0\\
-3i/8&-3i/8&0
\end{pmatrix},
\qquad
\det=-27/256.
\]

Therefore trace-`H_q` is not either action line and is not in their span on
`W` or on the mirror. The existing graded Majorana construction also selects
neither action horn and does not insert trace-`H_q`.

The honest conclusion is scoped: the current equation-9.16 Spin-natural
pairing class and its existing reality graphs do not own the trace form. A
q-dependent nonzero-fermion Hessian, a different source-family completion, an
actual BV/BFV differential or an analytic domain could still own a new
physical form. None has been constructed here.

## Why this does not contradict the preceding Witt theorem

The preceding theorem used the Hermitian restriction

\[
W^\dagger P_{\rm tr}W,
\qquad
W^\dagger P_{\rm tr}M,
\]

and found zero same-sector form plus a rank-192 `W`--mirror cross-pair. The
fermion action begins with independent barred and unbarred variables and uses
a bilinear transpose restriction. Since complex conjugation exchanges `W`
and `M`,

\[
W^\dagger P_{\rm tr}W=M^T P_{\rm tr}W,
\qquad
W^\dagger P_{\rm tr}M=M^T P_{\rm tr}M.
\]

Thus Hermitian same-sector zero is exactly bilinear cross-sector zero, while
the Hermitian cross-pair is the nondegenerate bilinear restriction on the
mirror. The two certificates agree. They answer different typed questions.

## Layer 0

| object | exact status | forbidden inference |
| --- | --- | --- |
| independent barred/unbarred fields | source-owned classical action slots | already imposed Majorana reality |
| `P_sym`, `P_skew` | complete tested Spin-natural degree-diagonal action-compatible lines | source selection of one horn |
| `P_tr` | q-dependent trace-Hq compatibility form | defining source fermion pairing |
| transpose restriction | action bilinear on independent fields | Hermitian norm or conjugate-transpose restriction |
| graded Majorana graph | two exact local reality candidates | selection of a horn, trace form or physical cohomology |
| W and mirror | conjugate rank-192 one-form sectors | the two ambient `C^(32,32)` Weyl halves |

## Efficient exact certificate

The adaptive preflight rejected a search over arbitrary `192 x 192` forms.
Representation theory already reduced the relevant action family to two
lines, so the executable test compares exactly three forms.

- `GF(1009)` and `GF(1013)` both give rank `192` on `W` and mirror for all
  three forms and rank `0` for every bilinear W--mirror cross restriction.
- On each carrier the two action restrictions have coefficient-span rank two;
  adding trace-`H_q` gives rank three.
- The displayed three-coordinate `Q(i)` minor has exact determinant
  `-27/256`, so characteristic-zero nonmembership does not rest on modular
  evidence or a floating spectrum.

The probe passes `39/39` checks.

## Adaptive specialist close

1. **Representation/Clifford — ACTUAL MATH, very high.** The complete tested
   action class is two lines; trace-`H_q` is a third q-dependent intertwiner.
2. **Real structure — ACTUAL MATH, very high.** Conjugation exchanges W and
   mirror, which explains the transpose-versus-adjoint rank-table reversal.
3. **Variational/Grassmann — ACTUAL MATH, high.** Independent barred fields
   make the bilinear action pairing primary; a reality-reduced Hermitian form
   is later structure.
4. **Category/Layer 0 — ACTUAL MATH, very high.** Pairing classification,
   reality reduction and W/mirror restriction do not commute if trace-`H_q`
   is inserted without an owner.
5. **Symplectic/BV — ACTUAL MATH, high.** Neither a nondegenerate bilinear nor
   a graded Lagrangian reality graph is physical BV cohomology.
6. **Analytic/PDE — ACTUAL MATH, high.** No closed domain, positivity,
   spectrum or index follows from the finite pairing theorem.

## Claim ceiling and hostile disposition

The hostile review narrows “action-pairing space” to the complete tested
Spin-natural degree-diagonal class. It does not exclude a new q-dependent
pairing in an unconstructed action completion or nonzero-fermion Hessian.

Verdict:

```text
SCOPED_RESULT_SURVIVES__CURRENT_EQUATION916_PAIRING_CLASS_DOES_NOT_OWN_TRACE_HQ__NO_W_MIRROR_SELECTOR
```

## Progress and next gate

```text
Ledger v0.240 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
headline_delta: none
frontier_conditions_closed: 1
frontier_conditions_opened: 0
remaining_named_conditions: 2
```

Next: evaluate the first action-owned nonzero-fermion Hessian or graded BV
differential on W and mirror and demand an invariant fingerprint that differs
between them. Keep analytic-domain selection as a separate successor. Stop if
the distinction appears only after fitting a projector, compatible connection
or external datum.

## Reproduction

```sh
sage -python \
  tests/channel-swings/selected_k77_w_mirror_action_pairing_ownership_probe.py
```
