---
title: "G3 primary-source recheck: observation pullback, not a supplied defect action"
status: source
doc_type: claim_mining_report
created: 2026-07-31
branch: agent/weinstein-guided-source-action
run: lab/process/runs/GUH-20260731T144734Z-g3-full-variational-bvbfv/run-plan.md
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# G3 Weinstein recheck: section pullback versus defect action

## Trigger

The G3 variation found that the selected source action is a bulk functional on
`Y^14` and has no observation-section field. Before recording that absence as
a construction failure, the Eric-lane recheck gate was run against the local
Weinstein primary-source set.

## Layer-0 question

The two candidate meanings of “get four-dimensional physics from the
fourteen-dimensional action” are different:

| branch | map | effect |
| --- | --- | --- |
| observation pullback/restriction | `R_s: fields/equations on Y -> fields/equations on X` induced by a metric section `s` | reads or restricts the ambient theory downstairs; does not add a distributional source term upstairs |
| bulk-plus-defect action | `I_Y + s_! I_X` with `s` varied | adds a new four-dimensional functional and distributional Euler/corner terms to the ambient equation |

The maps go in opposite variational directions. They are `HOMONYM` under a
generic phrase such as “section coupling” until the construction names which
one it uses.

## Positive primary-source receipts

| source | timestamp | conservative content | G3 implication |
| --- | --- | --- | --- |
| TOE, *Geometric Unity: 40 Years in the Making* | local `01:18:26`--`01:19:15` | the dialogue distinguishes local metric sections on observation patches from a disputed global-section recollection | do not assume a globally selected section or bundle trivialization |
| same TOE episode | local `01:29:19`--`01:29:47` | one Standard Model generation is described as the pullback of a Weyl spinor from the space of pointwise Lorentz metrics to the four-manifold | the author-guided physicalization map is restriction/pullback |
| Portal/Oxford first-look transcript | `02:04:18`--`02:05:04` | the action is described as occurring on `U^14`; a projection and section `sigma` are then used to ask what fields pulled back to `X^4` look like | explicitly separates ambient dynamics from observation pullback |
| same Portal transcript | `02:11:07`--`02:12:34` | equations are built upstairs and then decomposed and pulled back; fourteen-dimensional propagation still has to explain the four-dimensional appearance | makes the observation/domain map a stated technical debt, not a defect-action term |
| *Into the Impossible* transcript | `00:32:07`--`00:33:36` | a metric is a section of its metric bundle; data and spinors upstairs are pulled back along it rather than compactified | independently confirms the pullback reading |

## Negative receipt

Exact searches of these three local primary transcripts for `defect`,
`pushforward`, `junction`, `distributional`, `supported on`, `boundary
action`, and `brane` return no mathematical construction of a defect action.
The ordinary-language word “injunction” in the TOE transcript is irrelevant.

The sources therefore do **not** supply

```text
I_total = I_Y + s_! I_X,
```

a varied embedding equation, a delta-supported ambient current, or a
bulk-defect BFV corner.

## Verdict

```text
AUTHOR-GUIDED-OBSERVATION-PULLBACK-BRANCH-FOUND
GLOBAL-SECTION-STATUS-UNCERTAIN
DEFECT-ACTION-BRANCH-NOT-SUPPLIED-BY-RECHECKED-SOURCES
```

The absence of `s` from the G2/G3 bulk source action is not itself an
Eric-lane failure. It places the next author-guided construction in G4:

\[
\mathcal R_s\mathcal L_s=1,
\qquad
\mathcal R_sD_Y\mathcal L_s=D_X,
\qquad
(1-\mathcal L_s\mathcal R_s)D_Y\mathcal L_s=0.
\]

The last equation is the off-slice leakage test. Pulling back an ambient Euler
covector and varying a pulled-back action need not commute, so G4 must also
type and test the equation-dual map. It may not infer the four-dimensional
Euler equation merely from equal dimensions or a bundle decomposition.

The repo's N1 bulk-plus-defect action remains a valuable independently
constructed comparator. In the Eric lane it must be charged as a repo
addition and used only after an explicit replacement/no-double-count map; it
cannot be attributed to the rechecked Weinstein sources.

## Source boundary

This is a source-disposition result, not a proof that the pullback/retract
exists globally, intertwines the corrected G3 Euler operator, supplies a
closed domain, removes off-slice modes, or produces the Standard Model. Those
are G4/G8 construction tests.
