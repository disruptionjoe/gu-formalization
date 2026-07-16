---
title: "Recovery no-go GR W229 history audit and scope fork"
status: exploration
doc_type: recovery_no_go_defense
created: 2026-07-16
run_id: GUH-20260716T120943Z-gr-nogo-defense
target: RECOVERY-NOGO-GR-W229-VACUUM
test: tests/recovery-contract/gr_nogo_history_scope_gate.py
register: lab/process/recovery-no-go-defense-register.json
---

# Recovery no-go GR W229 history audit and scope fork

Operational result: `SCOPE_CONFIRMED` for Swing 1 of
`RECOVERY-NOGO-GR-W229-VACUUM`.

This does not strengthen the repo verdict, change claim status, move canon,
alter public posture, or call the GR recovery question exhausted. It only
records that the branch-local exact-vacuum GR no-go is not contradicted by prior
same-construction clearance, and that the first obstruction has a small typed
core.

## Decision question

Did GU already encounter and clear the same exact-vacuum GR residual
obstruction for the same frozen W203/W229/W230/W236 record-current
construction?

Answer: no prior same-construction clearance was found in the bounded search.

Prior work did clear the imported-vacuum linear residual, and it did clear the
record-current theta row in the `Psi=0` vacuum. Those clears do not cancel the
quadratic `Q^TF(B)` residual. In fact, the W236/W229 theta clear is one half of
the current obstruction: the available source/YM cancellation tensor is zero.

## Construction fork

The gravity side uses the GU-native `|II|^2` / second-fundamental-form residual
on `Y14 = Met(X4)`. The standard Schwarzschild metric is the imported vacuum
benchmark.

The source side uses the W229 record-current construction fixed by the action
fingerprint:

```text
(-Z_U D_A* D_A + c_theta eta) theta = J[Psi]
Psi = 0 -> J[Psi] = 0 -> theta = 0
```

The standard Einstein equation is used only as the comparator benchmark. It is
not imported as GU dynamics.

## History audit

Search surfaces: `canon/`, `explorations/`, `tests/`, `steward/runs/`,
`DERIVATION-PROGRESS.md`, `RESEARCH-STATUS.md`, `NEXT-STEPS.md`, and
`lab/process/`.

Mechanism terms included `Q^TF`, `Willmore residual`, `quadratic residual`,
`Schwarzschild residual`, `O(M^2)`, `record-current`, `J[Psi]`, `Psi=0`,
`theta=0`, `W229`, `source law`, `c_kin`, `bare theta`, `exact-vacuum`, `W225`,
`W236`, and `W238`.

| prior record | construction and outcome | applicability |
|---|---|---|
| `canon/schwarzschild-weak-field-rfail.md` / RFAIL-03 | Imported Schwarzschild weak-field metric. Linear-in-M Willmore residual vanishes by harmonicity; leading residual remains quadratic `Q(B)` and the verdict stays `OPEN`. | No conflict. It removes a linear false alarm and leaves the quadratic obstruction. |
| `explorations/willmore-residual-computed-and-buildbench-reconciliation-2026-07-11.md` | Computes nonzero `Q^TF(B)` and distinguishes H-class, II-class, ambient, and theta-source possibilities. | No conflict. It supports the residual and routes possible balances to different construction forks. |
| `explorations/W225-gravity-projected-shadow-schwarzschild-cheap-read-2026-07-15.md` | Imported exact Schwarzschild, `Psi=0`, computable linear slice. Built terms vanish at linear order; leading built contribution is `Q(B)`. | No conflict. Linear cheap-read compatibility is not exact recovery or quadratic cancellation. |
| `explorations/W236-gravity-theta-sector-residual-built-action-2026-07-15.md` | W229-built record-current theta equation. `J[Psi=0]=0` forces `theta=0`. | Same source construction, but not a clearance. It establishes the zero source side of the current no-go. |
| `explorations/W238-gravity-willmore-residual-kerr-2026-07-15.md` | Imported Kerr linear-in-M slice. Linear Willmore residual clears, while the `O(M^2)` obstruction remains. | No conflict. It extends the linear cheap-read clear and preserves the quadratic issue. |
| `explorations/W229-close-a2-source-action-znu-completion-2026-07-14.md` | Record-sourced induced-YM branch-3 action. Builds the source law and leaves `{kappa, Z_U}` as normalization data. | Same source construction, but no nonzero vacuum source or canceller is supplied. |

Audit result: `NO_PRIOR_CLEARANCE_FOUND` for the same target obstruction.

## Swing 1 scope result

The obstruction minimizes to six load-bearing facts:

1. The principled Schwarzschild `Q^TF(B)` residual is nonzero.
2. The current source law is the W229 record-current law.
3. In the imported exact vacuum, `Psi=0`.
4. `Psi=0` gives `J[Psi]=0`.
5. The finite positive screened operator gives `theta=0`.
6. A zero source/YM tensor cannot cancel `Q^TF(B)`, regardless of `kappa` or
   `Z_U`.

So Swing 1 outcome is `SCOPE_CONFIRMED`: the current no-go is valid for the
frozen W229 record-current vacuum construction and should proceed to a real
Swing 2 construction attempt before anyone calls the broader construction class
exhausted.

## Construction space

| construction member | Swing 1 status |
|---|---|
| Frozen W229 record-current nonlocal branch | `SCOPE_CONFIRMED_NO_GO` |
| W203 ultralocal limit | Same zero-source obstruction unless a different non-record source is supplied. |
| Fundamental-stiffness or bare-theta branch | Different construction. Eligible for Swing 2 only if stated without merging it with W229. |
| Boundary-conditioned adapter response | Explicit-assumption construction. Not a current-branch clearance. |
| Standard Einstein dynamics | Comparator only. Not importable as GU dynamics. |

## Next work

Proceed to Swing 2 for this target unless daily stewardship changes the lane:
attempt one genuinely different construction from the predeclared space. The
most natural candidates are the bare/fundamental-stiffness theta fork,
an ambient/H-class balance, or a boundary-conditioned adapter response. A valid
attempt must change a load-bearing construction or derive a previously absent
object; it must not retune `kappa`/`Z_U`, import Einstein dynamics, or count the
linear cheap-read clear as exact recovery.

Paper seed proposal: none.
