---
title: "Selected K77 source-sign degree-duality and W/mirror graph gate"
status: active_research
doc_type: construction_result
created: 2026-08-10
lane: 1
ledger: v0.140
result: "SCOPED_KILL__BARE_TRACE_Q_LEAKS_RS_RANK64__PIN_COMPLETION_SWAPS_W_AND_MIRROR__BOTH_DEGREE_DUALITY_UPPER_GRAPHS_FAIL_JOINED_RANK256"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# K77 source-sign degree duality forces W/mirror closure and then misses the port

## Result first

The remaining canonical trace-`q` realization of the source's ambient-half
signs has been constructed without relabeling the source fields and fails at a
sharper place than the preceding rival.

The two already-enumerated degree-sensitive row/column primalizers each need
one chirality flip between the zero- and one-form sectors. The trace-reversed
metric fibre supplies the canonical flip `gamma(q)`, with `q=g/2`, without
adding a datum. But a bare spinor `gamma(q)` sends rank 64 of either proposed
rank-192 carrier outside the gamma-traceless Rarita--Schwinger carrier. The
natural Pin-completed one-form action repairs that defect and does something
decisive:

```text
Pin(q) W      = mirror
Pin(q) mirror = W
```

exactly over both `GF(1000033)` and `QQ(i)`. Thus this reality/duality map
cannot retain W alone. Within the proposed W/mirror pair, its smallest closed
comparator is the rank-384 sum `W + mirror`.

Both degree-duality solutions were then assembled as actual row/column
primalizers of the source-native upper-left, zero-form port, and lower-left
cells. For every retained parent and both exact fields:

```text
rank projected port = 128
rank projected leak = 128
rank [port | leak]  = 256
```

Therefore no graph `G:(W+mirror)->Omega0(S)` can solve even the upper
invariance equation. The action-tied lower map remains rank 128 but is not
used after the upper failure. A nonzero southeast block cannot repair this
obstruction because it enters only the lower graph equation.

This is a scoped kill of the canonical trace-`q` degree-duality repair on the
proposed RS carrier. It is not a no-go for the full source operator, another
Shiab-family member, a source-derived restricted zero-order connection port,
or a different physical carrier. The released sources remain silent on those
repairs.

Executable receipt:

```text
4 source + 5 prior-art + 4 Layer-0 + 51 exact + 5 type
+ 8 representation + 12 variational + 6 planted
+ 1 symplectic + 1 analytic + 1 adversarial = 98/98 PASS
```

## Plain English

The draft says the plus and minus signs label genuine ambient spinor halves.
Our earlier working operator made its bookkeeping fit by using an auxiliary
grading. The remaining honest repair was to use the metric fibre's own trace
direction as a map between the two spinor halves.

That map works on bare spinors, but matter here is supposed to sit inside the
gamma-traceless one-form sector. Acting on the spinor alone spills part of the
candidate out of that sector. Completing the action so it respects the whole
one-form-spinor geometry fixes the spill, but swaps the proposed carrier with
its mirror. Reality therefore makes us carry both.

Once both are carried, the ordinary zero-form connection slot points in a
different 128-dimensional direction from the remaining leakage. Since the two
directions are independent, no choice of graph field can cancel one with the
other. This is not "GU fails"; it says this particular clean way of honoring
the source signs does not finish the fermion construction.

## Pre-wave

- **Fork assumed:** labelled real K77 and the source-displayed southeast-zero
  candidate only; no physical parent or carrier was assumed.
- **Search space:** two degree-duality solutions, bare versus Pin-completed
  trace-`q`, W/mirror/their sum, three parents, and two exact fields.
- **Wholesale reach:** the canonical trace-`q` realization on the proposed RS
  carrier. Other Shiabs, other moving tensors, BV, and domains remain outside.
- **New object:** none. `q=g/2`, W, mirror, and the connection port were all
  already present.
- **What dies:** only the canonical trace-`q`/Pin degree-duality adapter through
  the displayed upper cells. The source family and other carriers survive.

Preregistered horn `DOUBLED_LOWER_OBSTRUCTION` did not fire: the
source-faithful primalizers fail one equation earlier, at upper image
inclusion. This is a legitimate sharpening, not a post-fit relabel.

## Layer 0

| phrase | object in this gate | not identified with it |
| --- | --- | --- |
| source sign | ambient `S+/-` label in section 11.2 | auxiliary total grading |
| degree duality | explicit row/column primalizer between source bundles and one common carrier | renaming a glyph |
| bare `q` | spinor map `gamma(q):S+<->S-` | an action on a one-form index |
| Pin completion | reflected one-form index tensored with `gamma(q)` | a new datum |
| W/mirror closure | rank-384 carrier preserved by the Pin map | selection of W or a physical quotient |
| graph | algebraic invariant subspace of `Omega1(S)+Omega0(S)` | BV cohomology or an analytic domain |

The bare `q` map remains a valid map on the source's full `Omega1(S)`. Its
rank-64 RS leakage becomes a kill condition only when it is also required to
preserve the proposed gamma-traceless generation carrier. That conditional is
kept explicit.

## Source return

- `SOURCE-CONFIRMS`: the ambient half-spinor field labels, the displayed
  southeast-zero candidate, and an admitted unspecified nonzero southeast
  rival.
- `SOURCE-CORRECTS`: none.
- `SOURCE-SILENT`: another sign convention, a replacement parity-compatible
  Shiab, a restricted zero-order port, and physical W/mirror selection.

The nonzero southeast rival does not affect this result: the obstruction lies
in the upper equation before the southeast cell is used.

## Exact construction

Write the native rolled upper blocks as

\[
D=\begin{pmatrix}A&B\\ C&0\end{pmatrix},
\]

where `A` is the native ambient-odd Shiab cell, `B` the ordinary
`Omega0 -> Omega1` connection cell, and `C` its action-tied lower-left cell.
The prior parity SAT problem has two solutions

```text
(r1,r0,c1,c0)=(-,+,+,-), (+,-,-,+).
```

Realizing minus parity by the trace flip and using the Pin completion `T` on
one-forms gives, up to irrelevant global inverse signs,

\[
\begin{aligned}
D_{\rm row}&=
\begin{pmatrix}TA&TBQ\\ C&0\end{pmatrix},\\
D_{\rm column}&=
\begin{pmatrix}AT&B\\ QCT&0\end{pmatrix}.
\end{aligned}
\]

These are row/column primalizations of the source density-dual matrix, not
field-subscript relabelings. On `P=W+mirror`, the upper graph condition is

\[
(1-P)(A'P+B'G)=0.
\]

For both displayed primalizers, all parents, and both exact fields, the two
images have ranks `128` and a direct-sum joined rank `256`. No `G` exists.

## Controls with power

- The old non-source-faithful q family has the same pair leak and port ranks
  but joined rank `128`; it passes this upper-image control before failing the
  lower equation in v0.139. Thus `256` is not forced by dimensions alone.
- A bare `gamma(q)` has exact rank-64 leakage out of RS for both W and mirror.
- Pin completion removes all RS leakage and exchanges W/mirror exactly in both
  directions.
- The lower map remains rank 128 but is deliberately not read as an additional
  obstruction once the upper equation fails.

## Constraint and ledger boundary

The canonical trace direction adds zero freedom and consumes no P1/P2/P3.
The result removes one construction route but supplies no physical carrier,
quotient, index, generation count, mass, or observed equation. Ledger v0.140
therefore changes six row distances/evidence fields only. Coverage, verdicts,
residue, forks, quotients, datum, canon verdicts, and public posture remain
unchanged.

## Next gate

The sign-repair cluster has reached a stopping rule: the source-native
ambient-even Shiab class is empty, the older total-grading q rival fails its
lower equation, and the canonical source-sign degree-duality realization
fails its upper equation. Do not keep retuning these cells.

The next Build should either:

1. supply a genuinely different, source-derived Shiab or restricted
   zero-order connection orbit with a new typed object and positive constraint
   surplus; or
2. leave draft 9.16 unresolved and advance the disjoint coupled-functional
   completion through metric, epsilon, observation, fermion-current, and
   Ward/BV owners.

The second option is the default until a new source-owned operator object is
found.
