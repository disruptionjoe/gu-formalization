export const meta = {
  name: 'gu-research-loop',
  description: 'GU formalization research loop: orient (reads adversarial log) → cascading batches → adversarial check → fix → log → self-improve → commit to GitHub',
  phases: [
    { title: 'Orient', detail: 'Read adversarial log for calibration, read project state, pick 10 open items, plan dependency-aware batches' },
    { title: 'Batch-A', detail: 'First parallel batch: independent computations (~3 items)' },
    { title: 'Batch-B', detail: 'Second parallel batch: may use Batch-A context (~3-4 items)' },
    { title: 'Batch-C', detail: 'Third parallel batch: synthesis, canon, cross-program (~2-3 items)' },
    { title: 'Adversarial', detail: 'Skeptical structured review of all new outputs for errors and overreach' },
    { title: 'Fix', detail: 'Address critical and moderate issues found by adversarial check' },
    { title: 'Log', detail: 'Prepend run summary + patterns to process/loop-adversarial-log.md' },
    { title: 'Self-Improve', detail: 'Read log patterns, make 1-2 targeted calibration edits to this workflow' },
    { title: 'Commit', detail: 'Stage all changes, commit, push to GitHub (never arXiv)' },
  ],
}

const REPO = 'C:\\Users\\joe\\JB\\research\\Church of AI\\gu-formalization'
const LOG_FILE = 'process/loop-adversarial-log.md'
const WORKFLOW_FILE = '.claude/workflows/gu-research-loop.js'

const MATH_CONTEXT = `
ESTABLISHED MATHEMATICAL CONTEXT:

Geometry:
- Y^14 = Met(X^4): bundle of Lorentzian metrics on 4-manifold X^4
- Fiber: GL(4,R)/O(3,1), signature (9,5) total
- Cl(9,5) ≅ M(64,H) — quaternionic; spinor module S = H^64, dim_R = 256
- w_2(Y^14) = 0 for any orientable X^4 — RESOLVED

Algebra:
- Gauge group Sp(64) = U(64,H), dim sp(64) = 8256
- Sp(64) anomaly-free: pseudoreal (J^2 = -1), n_L - n_R = 0
- Nguyen §2 (anomaly pincer) and §3.1 (complexification gap) FULLY CLOSED

Shiab and tau+:
- Shiab Phi: Omega^2(Y^14)@S -> Omega^1(Y^14)@S — H-linear, Spin(9,5)-equivariant, RESOLVED
- tau+: G -> IG = G x| Omega^1(ad P) — purely group-theoretic

Generation count (CONDITIONALLY 3):
- S(6,4) = C^16; Cl(6,4) ≅ M(16,C)
- Pati-Salam: S(6,4) -> 16 Weyl fermions = 1 SM generation (CONFIRMED)
- Generation count = 2 (spin-1/2) + 1 (RS) = 3 — CONDITIONAL on discrete-series
- Rank-1 BC1 chain FAILED for (SL(4,R), SO_0(3,1)); need rank-3 or tau-twisted route
- K3: Â=2, ind_H=24 (target); T^4: Â=0, ind_H=8 (ruled out)

VZ: horizontal-covector Schur complement CONDITIONALLY_RESOLVED; mixed 14D OPEN
Dark energy: D_A*theta = 0 by Noether — CLOSED
Signed-readout: monotone provenance + signed boundary readout — active_research, no formal theorem yet
OC2: conditional H-linear Fredholm/KSp; full noncompact Y^14 weighted Fredholmness OPEN
Type II1: s*(J_GU)^2 = -1, CC KO-6 needs +1; twisted real structure not yet attempted

Cross-program contact:
- GU Tikhonov: Lambda ~ eps^2/t_obs^2
- TaF: lambda_max = 1/t_obs, Gamma_min = ln(1/eps)*lambda_max
- Compare Lambda with lambda_max^2 or Gamma_min^2 (not raw rates)
`

const PLAN_SCHEMA = {
  type: 'object',
  properties: {
    date: { type: 'string' },
    calibrationNotes: { type: 'string', description: 'Key patterns from adversarial log that should shape this run' },
    batches: {
      type: 'array',
      minItems: 1,
      maxItems: 3,
      items: {
        type: 'object',
        properties: {
          name: { type: 'string' },
          rationale: { type: 'string' },
          items: {
            type: 'array',
            minItems: 1,
            maxItems: 5,
            items: {
              type: 'object',
              properties: {
                label: { type: 'string' },
                outputFile: { type: 'string' },
                problem: { type: 'string' },
              },
              required: ['label', 'outputFile', 'problem'],
            },
          },
        },
        required: ['name', 'rationale', 'items'],
      },
    },
  },
  required: ['date', 'calibrationNotes', 'batches'],
}

const ISSUES_SCHEMA = {
  type: 'object',
  properties: {
    items: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          severity: { type: 'string', enum: ['critical', 'moderate', 'minor'] },
          file: { type: 'string' },
          description: { type: 'string' },
          fix: { type: 'string' },
        },
        required: ['id', 'severity', 'file', 'description', 'fix'],
      },
    },
    sessionPatterns: { type: 'string', description: 'Recurring failure modes across this session worth logging' },
  },
  required: ['items', 'sessionPatterns'],
}

// ── Phase 1: Orient ──────────────────────────────────────────────────────────

phase('Orient')

const plan = await agent(
  `Orient the GU formalization research loop. Working directory: ${REPO}

   STEP 0 — Read adversarial log for calibration:
   Run: cat ${LOG_FILE} (or Read it)
   Extract the 2-3 most recent entries. Note any recurring patterns:
   - Which verdicts keep being downgraded (e.g., CONDITIONALLY_RESOLVED → OPEN)?
   - Which problem areas keep producing overreach?
   - What guidance did the previous run leave for this run?
   Use this to shape item selection and computation discipline in this run.

   STEP 1 — Determine today's date:
   Run: git log --format="%as" -1
   Use this as the DATE for all output files this session.

   STEP 2 — Deduplication (critical):
   Run: git log --oneline --since=6.hours.ago
   Run: ls explorations/ (sort by date, note recent files)
   Any item whose output file already exists today is OFF-LIMITS — do not re-pick it.

   STEP 3 — Read project state:
   Read NEXT-STEPS.md (full file — find rows that are OPEN, not struck-through, not done today)
   Read RESEARCH-STATUS.md (current research map — what is canon, active_research, exploration)
   Read DERIVATION-PROGRESS.md (last 30 lines — what has been worked recently)
   Read .claude/commands/gu-compute.md if it exists (mathematical context supplement)

   STEP 3b — RESOLVED canon audit (run this before picking items):
   List every file in canon/ with verdict: RESOLVED.
   For each, scan for any assumption explicitly labeled "reconstruction grade" or "reconstruction-grade".
   Any RESOLVED file that contains a reconstruction-grade assumption must be immediately downgraded
   to CONDITIONALLY_RESOLVED: update the verdict field in its frontmatter, add a note explaining which
   assumption is reconstruction-grade, and append a correction note to DERIVATION-PROGRESS.md.
   Log how many files were downgraded in calibrationNotes.
   This audit runs first so that item selection in STEP 4 reflects accurate verdicts.

   STEP 4 — Pick 10 OPEN items:
   Select 10 distinct items that are genuinely OPEN (not RESOLVED, not CONDITIONALLY_RESOLVED
   unless a NEW sub-problem has been named, not already done today).
   Prefer items with: high publish potential, clear failure conditions, blocking other work.
   Apply calibration from Step 0: avoid problem areas that keep producing overreach.

   STEP 5 — Plan dependency-aware batches:
   Organize the 10 items into 2-3 batches:
   - batch_a: fully independent computations (run first, in parallel, ~3 items)
   - batch_b: items that may benefit from or reference batch_a results (run second, ~3-4 items)
   - batch_c: synthesis items — canon promotion, cross-program, no-go map updates (~2-3 items)
   Each batch runs internally in parallel. Batches cascade sequentially.
   Aim for ~3 items per batch; never more than 5.

   Return the plan with the date, calibration notes, and all batches.`,
  { label: 'orient:plan', phase: 'Orient', schema: PLAN_SCHEMA }
)

const DATE = plan.date
log(`Date: ${DATE} | Calibration: ${plan.calibrationNotes.slice(0, 120)}`)
log(`Batches: ${plan.batches.map(b => b.name + '(' + b.items.length + ')').join(', ')}`)

// ── Helper: run one batch in parallel ───────────────────────────────────────

async function runBatch(batch, phaseName) {
  const results = await parallel(
    batch.items.map(pick => () =>
      agent(
        `You are running a bounded GU formalization computation.
         Working directory: ${REPO}
         Today's date: ${DATE}

         PROBLEM: ${pick.problem}
         LABEL: ${pick.label}
         OUTPUT FILE: ${pick.outputFile}

         ${MATH_CONTEXT}

         Read .claude/commands/gu-compute.md for additional problem-specific context.
         Read any existing exploration files related to this label before starting.

         INSTRUCTIONS:
         1. Attempt the computation ambitiously — aim for reconstruction grade or better, not a plan.
         2. Verdict discipline:
            - RESOLVED: complete proof present, all steps verifiable
            - CONDITIONALLY_RESOLVED: name at least 3 explicit failure conditions (specific mathematical statements that would falsify the result)
            - OPEN: problem framed but not solved
            - EVADED: problem shown not to arise in this context
            - GENUINE_OBSTRUCTION: proved the thing fails, not just can't prove it works
         3. Write output to ${pick.outputFile} with frontmatter:
            ---
            title: "<descriptive title>"
            date: ${DATE}
            problem_label: "${pick.label}"
            status: exploration|reconstruction|verified|open
            verdict: RESOLVED|CONDITIONALLY_RESOLVED|OPEN|EVADED|GENUINE_OBSTRUCTION
            ---
         4. Update NEXT-STEPS.md: find the relevant row and append a status note.
         5. Append 3-4 sentence log to DERIVATION-PROGRESS.md:
            ### ${pick.label} (${DATE})
            Verdict: <verdict>
            <what was computed, result, what remains>
            File: \`${pick.outputFile}\`

         Return: label, verdict, one sentence on result, whether tracking files updated.`,
        { label: 'compute:' + pick.label, phase: phaseName }
      )
    )
  )
  return results
}

// ── Phases 2-4: Cascading batches ───────────────────────────────────────────

const batchResults = []

for (let i = 0; i < plan.batches.length; i++) {
  const batch = plan.batches[i]
  const phaseName = i === 0 ? 'Batch-A' : i === 1 ? 'Batch-B' : 'Batch-C'
  phase(phaseName)
  log(`Running ${batch.name}: ${batch.items.map(p => p.label).join(', ')}`)
  const results = await runBatch(batch, phaseName)
  batchResults.push(results)
  log(`${batch.name} complete: ${results.filter(Boolean).length}/${batch.items.length} succeeded`)
}

const totalRuns = batchResults.flat().filter(Boolean).length
const totalItems = plan.batches.reduce((sum, b) => sum + b.items.length, 0)

// ── Phase 5: Adversarial check ───────────────────────────────────────────────

phase('Adversarial')

const issues = await agent(
  `ADVERSARIAL REVIEW of new GU formalization outputs produced in this session.
   Working directory: ${REPO}
   Date: ${DATE}

   You are a skeptical mathematical reviewer. Find errors, overreach, and weaknesses.

   1. Run: git diff --name-only HEAD (or git status) to identify new/modified files.
   2. Read each new exploration file and any modified canon or active-research files.
   3. For each file check:
      - Does the verdict match the actual strength of the argument?
        (RESOLVED requires a complete proof; CONDITIONALLY_RESOLVED requires at least 3 named failure conditions)
      - Are there claims that outrun their proofs?
      - Are failure conditions explicitly named as specific falsifiable mathematical statements?
      - Are assumptions stated so another researcher could check them?
      - Are there contradictions with existing canon?
      - Are there mathematical errors (wrong ranks, wrong signs, wrong group theory)?
      - For any canon promotions: do they meet all 5 promotion criteria?
      - SAME-SESSION SELF-RESOLUTION CHECK (critical): For any item where a flag was raised AND
        a resolution was provided, check whether both originated in this session (i.e., the flag
        appears in a file written today and the resolution is also from today). If flag and resolution
        are both intra-session, the verdict upgrade is BLOCKED — downgrade the verdict to
        DEFERRED_VERIFICATION and note that external verification or an intervening verified
        computation is required before upgrading.
      - UNDISMISSED-CANDIDATE CHECK: If two or more generation-count candidates (or analogous
        competing hypotheses) are present and neither has been formally dismissed by a derivation,
        the verdict must be OPEN. CONDITIONALLY_RESOLVED is only valid when one candidate is
        supported by a derivation and the remaining candidates are explicitly named as failure
        conditions. Two undismissed guesses do not support CONDITIONALLY_RESOLVED.
   4. Be harsh. A CONDITIONALLY_RESOLVED that should be OPEN is a real problem.
      A bad canon promotion damages credibility.
   5. After reviewing all files, identify session-level patterns:
      - Did the same type of overreach recur across multiple files?
      - Was there a systematic gap (e.g., always missing failure conditions for a specific class)?
      - What should the next run do differently?

   severity guide:
   - critical: wrong verdict, mathematical error, or bad canon promotion — must fix
   - moderate: missing failure condition, overstated claim, incomplete proof — should fix
   - minor: unclear notation, missing citation — note but skip in fix phase`,
  { label: 'adversarial', phase: 'Adversarial', schema: ISSUES_SCHEMA }
)

const actionable = issues.items.filter(i => i.severity === 'critical' || i.severity === 'moderate')
log(`Adversarial: ${issues.items.length} total issues, ${actionable.length} critical/moderate`)
log(`Session patterns: ${issues.sessionPatterns.slice(0, 150)}`)

// ── Phase 6: Fix ─────────────────────────────────────────────────────────────

phase('Fix')

if (actionable.length > 0) {
  await parallel(
    actionable.map(issue => () =>
      agent(
        `FIX this issue in the GU formalization repo.
         Working directory: ${REPO}

         ISSUE: ${issue.id} (${issue.severity})
         FILE: ${issue.file}
         PROBLEM: ${issue.description}
         RECOMMENDED FIX: ${issue.fix}

         1. Read the file.
         2. Apply the fix: correct the verdict, add missing failure conditions (at least 3),
            fix the mathematical error, or revert a premature canon promotion
            (if reverting: move content back to explorations/, update CANON.md and RESEARCH-STATUS.md).
         3. If the verdict changed, append a correction note to DERIVATION-PROGRESS.md.
         Return: what was changed.`,
        { label: 'fix:' + issue.id, phase: 'Fix' }
      )
    )
  )
} else {
  log('No critical/moderate issues — skipping fix phase')
}

// ── Phase 7: Log ─────────────────────────────────────────────────────────────

phase('Log')

const allLabels = plan.batches.flatMap(b => b.items.map(i => i.label)).join(', ')

await agent(
  `Prepend a run summary to the adversarial log file.
   Working directory: ${REPO}
   Log file: ${LOG_FILE}

   1. Read the current ${LOG_FILE} (create it if it doesn't exist — just an empty string).
   2. Build a new entry with this format:

   ## Run ${DATE} — ${totalRuns}/${totalItems} completed, ${actionable.length} fixed

   **Items:** ${allLabels}

   **Session patterns (from adversarial review):**
   ${issues.sessionPatterns}

   **Calibration for next run:**
   <1-3 specific instructions for the next Orient phase based on what went wrong this run>

   **Issue summary:** ${issues.items.length} total (${actionable.length} critical/moderate, ${issues.items.length - actionable.length} minor)

   ---

   3. Prepend this entry to the top of the file (newest first), keeping all existing content below.
   4. Write the full updated file back.
   5. Return: confirmation that the log was updated, number of existing entries preserved.`,
  { label: 'log:write', phase: 'Log' }
)

// ── Phase 8: Self-Improve ─────────────────────────────────────────────────────

phase('Self-Improve')

await agent(
  `Make 1-2 targeted calibration improvements to the GU research loop workflow.
   Working directory: ${REPO}
   Workflow file: ${WORKFLOW_FILE}
   Adversarial log: ${LOG_FILE}

   1. Read the last 2-3 entries of ${LOG_FILE} (newest first — top of file).
   2. Read the full ${WORKFLOW_FILE}.
   3. Identify 1-2 specific, targeted improvements that would address recurring patterns in the log.
      Good targets:
      - A prompt clause that's producing consistent overreach (tighten the failure-condition requirement)
      - A missing deduplication guard that lets the same problem recur
      - An Orient step that's missing a calibration read
      - A compute instruction that's being systematically misread
   4. Make at most 2 changes. Each change must be:
      - Targeted: a specific prompt addition/change, not a structural rewrite
      - Justified: directly traceable to a pattern in the log
      - Non-breaking: do not change the phase structure, schema shapes, or commit/arXiv rules
   5. After editing, verify the file is valid JavaScript (check for syntax errors visually).
   6. Return: what was changed and why (traceable to which log pattern).

   HARD CONSTRAINTS:
   - Do not restructure phases or change the schema field names
   - Do not touch the commit instructions or the "never arXiv" rule
   - Do not make more than 2 changes
   - If no clear improvement is warranted from the log, make zero changes and say so`,
  { label: 'self-improve', phase: 'Self-Improve' }
)

// ── Phase 9: Commit ───────────────────────────────────────────────────────────

phase('Commit')

await agent(
  `Commit all new and modified files in the GU formalization repo.
   Working directory: ${REPO}
   IMPORTANT: git push to GitHub only. Never submit to arXiv or any other platform.

   1. Run: git status
   2. Stage all new and modified files:
      explorations/*.md, active-research/**/*.md, canon/*.md, tests/*.py,
      NEXT-STEPS.md, DERIVATION-PROGRESS.md, RESEARCH-STATUS.md, CANON.md,
      process/loop-adversarial-log.md,
      .claude/workflows/gu-research-loop.js
      (only if they have changes)
   3. Commit with message:
      GU loop: ${allLabels} (${DATE})

      Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
   4. Run: git push
   5. Return: commit hash, number of files committed, push status.`,
  { label: 'commit', phase: 'Commit' }
)

return {
  date: DATE,
  totalItems,
  totalRuns,
  batches: plan.batches.length,
  calibrationNotes: plan.calibrationNotes,
  issues: issues.items.length,
  fixed: actionable.length,
  sessionPatterns: issues.sessionPatterns,
}
