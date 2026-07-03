---
title: "Convergence Deep Read (OBJ-CONVERGE meta-audit, git+artifact wide)"
status: process
doc_type: metric_report
created_at: "2026-07-03"
note: "Companion DEEP read to the steward's `convergence-read-2026-07-03.md` (which reads the loop-adversarial-log with a pinned --check-report). This one widens the lens to full git history + hourly-cycle/steward artifacts. Does not replace the steward report; both stand. Report only; promotes nothing."
sources:
  - "git log (full history, 379 commits, 2026-05-30 .. 2026-07-03)"
  - "explorations/hourly-cycles/ (531 artifacts)"
  - "steward/runs/ (24 run receipts)"
  - "lab/process/loop-adversarial-log.md"
script: "lab/process/convergence_metrics_2026-07-03.py"
---

# Convergence Read: is the automated research loop still buying information?

Report only. Promotes nothing, changes no canon / status / paper / result. This read
supersedes the narrower bounded read that used only the 2-session adversarial log; it adds
git-cadence, create/rework, and artifact-generator instrumentation.

All numbers below are reproduced by:

```text
python lab/process/convergence_metrics_2026-07-03.py
```

Numbers are **computed**. The verdict and the research-vs-process split are **judgment-assisted**
(keyword heuristics + hand read of commit bodies). Both are flagged where used.

---

## 1. Computed metrics

### Commit cadence per day (declining off a sharp peak)

| date | commits | | date | commits |
|---|---|---|---|---|
| 06-22 | 13 | | 06-28 | 50 |
| 06-23 | 49 | | 06-29 | 39 |
| 06-24 | 26 | | 06-30 | 13 |
| 06-25 | **80** | | 07-01 | 14 |
| 06-26 | 44 | | 07-02 | 12 |
| 06-27 | 15 | | 07-03 | 10 |

Peak 80/day (06-25). Last four days steady at 10-14/day — roughly a 6-8x drop off peak, then flat.

### Create-vs-rework ratio (collapsed from ~12 to ~1)

Added vs modified files per commit-day (`create_rework_ratio = added/modified`):

- 05-30: 6.86 · 06-24: 4.73 · 06-25: **11.94** · 06-26: 4.80 · 06-27: 3.21 (creation-dominated)
- 06-28: 1.47 · **06-29: 0.36** (mass-normalization day, 74 add / 204 modified) · 06-30: 1.25
- 07-01: 1.39 · **07-02: 0.77** · 07-03: 1.16 (create ~= rework)

The loop now re-works roughly as many files as it creates. Early phase was ~5-12x creation.

### Net-new admitted-object proxy (canon RESULTS/SPEC adds)

Canon `.md` first-adds per day: 05-31: 3 · 06-23: 5 · 06-27: 1 · 06-28: 14 · 06-29: 9 · 07-02: 4 · 07-03: 7.
Still positive in the last window (11 canon files added 07-02/07-03). **Caveat (hand-read):** the recent
adds are increasingly *residual-closure* / interface-SPEC files — e.g.
`function-space-index-conservation-residual-closure-RESULTS.md` closes a residual opened by
`function-space-index-conservation-RESULTS.md` on the same day. That is convergent tail behavior
(closing your own residuals), not opening new frontiers.
No machine-readable verdict ledger exists, so a true **net RESOLVED gain** (promotions minus
downgrades/re-openings) is **not computable** — this proxy is the honest substitute.

### Primary generator is OFF

The hourly-cycle engine produced 531 artifacts on exactly **two days**: 06-25 (275) and 06-26 (222).
Zero since 06-26. The highest-throughput exploration generator has been dark for a week; recent
throughput is the lower-yield "steward progress fan-out" lane.

### Steward fan-out cadence: 07-01: 10 · 07-02: 11 · 07-03: 3.

### Research-substance vs process/meta share (recent window, since 06-30)

45 commits: **16 research-substance, 29 process/meta → research share 0.356.** About two-thirds of recent
loop effort is self-maintenance: hygiene/path-leak gates, roadmap-link gates, steward contracts, PR
templates, verification-vocabulary, relabels, de-theater moves. (Keyword-classified, hand-spot-checked.)

Whole-history rework-signal share (subjects containing demote/relabel/normalize/fix/audit/consolidate/...):
51/379 = 0.135.

### Repeat-touch concentration (same object churned many times)

Distinct commits touching one path: `canon/no-go-class-relative-map.md` **20**; the
`located-not-forced-generation-count` object **~30** across three mirrored copies (12+9+9 in
draft-papers, papers/candidates .md, .tex); `canon/shiab-existence-cl95.md` 8;
`canon/firewall-boundary-hypothesis.md` 7. The located-not-forced anchor was re-versioned v2.4 → v2.8 → v2.9.

### Adversarial-log repeat rate = 0.5

Both logged sessions reproduced the **same two** failure modes (`same_session_self_resolution`,
`verdict_grade_inflation`). The loop keeps re-committing the same class of error.

---

## 2. The read: PLATEAUING, with a rising thrash share

**Verdict: plateauing — a narrow convergent research tail wrapped in a growing thrash shell.**

Evidence it is NOT cleanly converging and NOT cleanly thrashing, but plateauing:

- **Converging signals (real but narrowing):** canon adds still positive; the recent research is a
  disciplined residual-closure chain (function-space index conservation → residual closure →
  antilinear bound → enum-completeness → RS boundary eta). This lane is still buying information, but
  it is closing *its own* residuals — the hallmark of a convergent tail, where each new certificate
  patches the last rather than opening new ground.
- **Thrash / diminishing-return signals:** create/rework ratio fell from ~12 to ~1; a full
  mass-normalization day (06-29, ratio 0.36); ~65% of recent commits are process/hygiene self-maintenance,
  not research; the top generator is dark for a week; single anchor objects re-touched 8-30 times; the
  adversarial loop reproduces the identical two verdict-hygiene errors every logged session.

The loop is not idling and not obviously churning in a loop, but its **marginal product per cycle has
dropped**: throughput is increasingly consumed by re-normalization, gate-manufacturing, and
re-versioning the same handful of anchors, while genuinely new admitted certificates arrive as a thin,
residual-closing stream.

---

## 3. Recommendation

**Marginal return on undirected automated loop effort has dropped enough that continuing at current
cadence is low value.** Report-only recommendations (promote nothing):

1. **Retire the generic "progress fan-out" lane.** It is manufacturing process work (hygiene gates,
   path-leak scrubs, templates) that dominates recent commits without buying research information.
2. **If the loop continues, restrict it to the residual-closure chain** (function-space / antilinear /
   eta / enum) — the only lane still buying information — and give it an explicit **stopping test**:
   enumerate the currently-open named residuals, close them, then halt rather than open new lanes.
3. **Stop re-touching settled anchors.** The located-not-forced object (~30 touches, v2.4→v2.9) and
   `no-go-class-relative-map` (20 touches) should be frozen pending a human submission decision, which
   would buy more than another automated re-version.
4. **Instrument a real verdict-transition ledger** (per-object promotion/downgrade/re-open with dates)
   before any future convergence *claim*. Net-RESOLVED-gain is currently unmeasurable; today's read
   leans on a canon-add proxy plus hand judgment.
5. **Fix the recurring loop defect at the harness level.** The same-session self-resolution and
   verdict-grade inflation recur every logged session (repeat rate 0.5) — a standing gate, not
   per-session calibration notes, is the fix.

Bottom line: one or two more *targeted* residual-closing cycles are justified; another week of
*undirected* fan-out is not. The next high-value move is a human call on whether the located-not-forced
spine is submission-ready, not another automated cycle.
