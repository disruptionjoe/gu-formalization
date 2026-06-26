export const meta = {
  name: 'gu-research-loop',
  description: 'GU formalization research loop: orient (reads adversarial log) → cascading batches → adversarial check → fix → log → self-improve → commit to GitHub',
  phases: [
    { title: 'Orient', detail: 'Read adversarial log for calibration, read project state, pick 10 open items, plan dependency-aware batches' },
    { title: 'Batch-A', detail: 'First parallel batch: independent computations (~3 items)' },
    { title: 'Batch-B', detail: 'Second parallel batch: may use Batch-A context (~3-4 items)' },
    { title: 'Batch-C', detail: 'Third parallel batch: synthesis, canon, cross-program (~2-3 items)' },
    { title: 'Adversarial', detail: 'Single efficient adversarial pass applying 10 review lenses: 5 mathematical + 5 process' },
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
- w_2(Y^14) = pi*w_2(X^4): Y^14 spin IFF X^4 spin (CORRECTION W2-01, 2026-06-26;
  the old "w_2=0 for any orientable X^4 / spin even for CP2" was FALSE — a dropped
  w_2(V) term; verified by w_2(Sym^2 E)=w_1(E)^2 for rank-4 E). w_1(Y^14)=0 stays
  unconditional. X^4 spin is a STANDING PRECONDITION for the quaternionic ind_H
  (W2-FC1): Y^14 is spin-c for any orientable X^4 but a U(1) spin-c twist breaks
  H-linearity and shifts the index off Â(K3)=2, so spin-c does NOT suffice.

Algebra:
- Gauge group Sp(64) = U(64,H), dim sp(64) = 8256
- Sp(64) pseudoreal (J^2 = -1); Nguyen §3.1 complexification gap defused via Cl(9,5),
  §2 U(128) pincer defused via Sp(64). But FULL GU anomaly cancellation is OPEN /
  not-canon: local 14D degree-8 anomaly (explicit I_16/index-density) and global
  Dai-Freed/eta/spin-bordism checks are still required — do NOT call it closed.

Shiab and tau+:
- Shiab Phi: Omega^2(Y^14)@S -> Omega^1(Y^14)@S — H-linear, Spin(9,5)-equivariant.
  RESOLVED for EXISTENCE ONLY (CORRECTION SHIAB-01): non-injective (dimensionally);
  rank/kernel/uniqueness/selector identity NOT established.
- tau+: G -> IG = G x| Omega^1(ad P) — purely group-theoretic

Generation count = 3 is OPEN (NOT conditionally-resolved — CORRECTIONS GEN-04/GEN-05/
FC4-HOLONOMY-01):
- S(6,4) = C^16; Cl(6,4) ≅ M(16,C); Pati-Salam: S(6,4) -> 16 Weyl fermions = 1 SM
  generation (CONFIRMED, representation theory of the posited fiber)
- ind_H(D_GU)=24=16+8 is the TARGET, not a result. All analytic routes to the RS leg
  ind_H(D_RS)=8 FAILED (scalar BC1, A3 Harish-Chandra, tau-twisted). The surviving
  APS/K3 route is CIRCULAR (divides the target 8 by Â(K3)=2 then multiplies back).
- Decisive open test OQ-RK1: target-independent CAS rank of Pi_RS·E_+·Pi_RS in M(64,H);
  returns 4 (=> 3 gen) or 8 (=> 4 gen, Candidate B undismissed). UNRUN.
- K3: Â=2 (a SPIN invariant); X^4 must be spin (W2-FC1). T^4: Â=0 (ruled out).

VZ: horizontal-covector Schur complement CONDITIONALLY_RESOLVED (4D principal-symbol);
  mixed 14D CONDITIONALLY_EVADED gated on E-block invertibility FC-VZ-1
Dark energy: theta equivariant + dynamic (unconditional). But D_A*theta = 0 is
  CONDITIONALLY_RESOLVED, NOT closed — it rests on unproved reconstruction-grade
  Assumption 3 (theta = the EL gauge-potential sector), CORRECTION DARK-ENERGY-01.
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
    blockedStatus: {
      type: 'object',
      description: 'No-progress halt guard. Set halt=true when the loop is stuck (see Orient STEP 0.5).',
      properties: {
        halt: { type: 'boolean' },
        reason: { type: 'string', description: 'Why the loop is halting and the human action needed to unblock it' },
      },
      required: ['halt', 'reason'],
    },
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
  required: ['date', 'calibrationNotes', 'blockedStatus', 'batches'],
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

   STEP 0.5 — No-progress halt check (do this before anything else):
   The loop must STOP rather than mint more files when it is stuck making no real progress.
   Read the most recent 3 entries of ${LOG_FILE}, the 3 most recent "three-cycle ... synthesis"
   files in explorations/ (ls explorations/*synthesis* | tail), and git log --oneline -15.
   Also check whether the loop is blocked on SOURCE ACQUISITION: grep recent syntheses for
   source_admissions_count, claim_promotions, claim_status_change, and source-custody/byte-acquisition
   verdicts. Set blockedStatus.halt = true if EITHER holds:
     (a) the last 3 runs all report zero claim-status changes / zero source admissions
         (claim_status_change:false and source_admissions_count:0 across all three), OR
     (b) the live frontier is gated on lawful-local custody of source bytes (video/manuscript)
         that the agent cannot itself obtain.
   When halt=true, write a one-sentence reason naming the blocker and the human action needed
   (e.g. "place the UCSD/DGU video + PTUJ manuscript bytes into the repo with a checksum and
   lawful-basis note"), and DO NOT pick any items. Otherwise set blockedStatus.halt = false
   with reason "progress is being made / not source-blocked".

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
   OVERREACH COOL-DOWN: Extract the item labels listed in the most recent 2 log entries.
   Any label that appears in both of the last 2 entries (i.e., has been worked two consecutive
   sessions without reaching RESOLVED) is on a ONE-SESSION COOL-DOWN — do not re-pick it unless
   it is the only remaining OPEN item in its dependency chain. List the cooled-down labels in
   calibrationNotes so the next Orient pass can enforce the same gate.

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

// ── No-progress halt guard ──────────────────────────────────────────────────
// Stop the loop (rather than mint more zero-promotion files) when Orient's STEP 0.5
// determined the run is stuck — e.g. source-custody-blocked or 3 consecutive no-claim runs.
if (plan.blockedStatus && plan.blockedStatus.halt) {
  log(`HALTED — no-progress guard fired: ${plan.blockedStatus.reason}`)
  await agent(
    `The GU research loop halted itself by the no-progress guard. Working directory: ${REPO}
     Reason: ${plan.blockedStatus.reason}
     1. Append (do not duplicate) a dated "## HALT ${DATE}" entry to the TOP of ${LOG_FILE} stating
        this reason and the exact human action needed to unblock the loop.
     2. Do NOT run any computation, do NOT create exploration/test files, do NOT commit, do NOT push.
     Return: confirmation the halt was logged.`,
    { label: 'halt:escalate', phase: 'Orient' }
  )
  return { halted: true, reason: plan.blockedStatus.reason, date: DATE }
}

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
            - RESOLVED: complete proof present, all steps verifiable. BLOCKED if: (a) you used the
              word "reconstruction" anywhere in the file, (b) any step is labeled "need to recheck"
              or "need to check", or (c) you explicitly named an internal contradiction anywhere in
              the file. Any of these conditions forces the verdict to CONDITIONALLY_RESOLVED at best.
            - CONDITIONALLY_RESOLVED: name at least 3 explicit failure conditions (specific mathematical statements that would falsify the result)
            - OPEN: problem framed but not solved
            - EVADED: problem shown not to arise in this context
            - GENUINE_OBSTRUCTION: proved the thing fails, not just can't prove it works
            Before writing the frontmatter verdict, do a self-check: search your draft for the
            words "reconstruction", "need to recheck", "need to check", and any sentence of the
            form "X gives Y and Z, not W" (explicit contradiction). If any match, set verdict to
            CONDITIONALLY_RESOLVED or OPEN and document which trigger fired.
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

// ── Phase 5: Adversarial check — one pass, 10 review lenses ─────────────────

phase('Adversarial')

const MATH_LENSES = [
  {
    key: 'verdict-strength',
    name: 'Verdict-Strength Auditor',
    focus: `Your ONLY job: check whether each verdict label matches actual proof strength.
RESOLVED = complete proof, no gaps, no reconstruction-grade steps, no "one can show", no "need to recheck".
CONDITIONALLY_RESOLVED = partial proof with at least 3 specific named failure conditions.
If any file says RESOLVED but contains ANY reconstruction-grade step, flag it critical.
If a CONDITIONALLY_RESOLVED has fewer than 3 specific falsifiable failure conditions, flag it moderate.`
  },
  {
    key: 'assumption-hunter',
    name: 'Hidden Assumption Hunter',
    focus: `Assume every file contains at least one hidden or unstated assumption. Find them.
Hunt specifically for: "by analogy", "similarly", "one can show", "it follows that", "standard result", "clearly", "obviously", "it is known that".
Each such phrase is a candidate assumption. Check whether it is actually justified in the file.
Flag as critical if the assumption is load-bearing for the verdict. Flag as moderate if peripheral.`
  },
  {
    key: 'math-errors',
    name: 'Mathematical Error Detector',
    focus: `Check for computational and algebraic errors. Every explicit number or formula is a candidate.
Verify: group ranks, Clifford algebra types (M(n,R) vs M(n,C) vs M(n,H)), spinor module dimensions,
Â-hat genera, index values, cohomology groups, signature arithmetic.
Known facts to check against: Cl(9,5) ≅ M(64,H), spinor dim_R=256; Sp(64) dim=8256; K3 Â=2, ind_H=24; T^4 Â=0, ind_H=8.
Flag any number or formula that contradicts established facts as critical.`
  },
  {
    key: 'failure-conditions',
    name: 'Failure Condition Enforcer',
    focus: `CONDITIONALLY_RESOLVED requires at least 3 specific, falsifiable failure conditions.
A valid failure condition names a specific mathematical statement that would falsify the result
(e.g., "if Â(K3) ≠ 2, the index count fails").
INVALID failure conditions: "if the construction fails", "if assumptions break down", "if further work shows otherwise".
Count the failure conditions in each CONDITIONALLY_RESOLVED file. Flag fewer than 3 as moderate.
Flag vague failure conditions as critical.`
  },
  {
    key: 'canon-integrity',
    name: 'Canon Integrity Checker',
    focus: `Read all files in the canon/ directory. Check three things:
(a) Cross-file contradictions: do any two canon files make incompatible claims about the same object?
(b) Premature promotions: does each canon file meet ALL 5 promotion criteria (scope statement, proof/falsification target, explicit assumptions, known failure modes, no internal artifact dependency)?
(c) RESOLVED with reconstruction-grade assumptions: any RESOLVED canon file containing a reconstruction-grade assumption must be downgraded to CONDITIONALLY_RESOLVED.
Be especially suspicious of files promoted today — same-session promotion is a high-risk pattern.`
  },
]

const PROCESS_LENSES = [
  {
    key: 'same-session-circularity',
    name: 'Same-Session Circularity Detector',
    focus: `Find cases where a flag or problem is raised and then "resolved" within the same session.
Check file dates in frontmatter. If file A (dated today) raises a concern, and file B (also dated today) resolves it, that is critical same-session circularity — regardless of how many files are between them.
File separation does NOT constitute inter-session verification. Being a "separate file" is not a valid defense.
Pay extra attention to vz-*, h3-*, and generation-count files — these areas have repeated circularity history.`
  },
  {
    key: 'verdict-inflation',
    name: 'Verdict Inflation Detector',
    focus: `Find cases where CONDITIONALLY_RESOLVED was assigned when multiple undismissed hypotheses exist.
When two or more candidates are both plausible and neither has been formally dismissed by derivation,
the verdict must be OPEN — not CONDITIONALLY_RESOLVED with one candidate selected as "baseline".
Look for: "Candidate A" or "baseline" language selecting one undismissed option.
Look for: generation count files claiming CONDITIONALLY_RESOLVED when rank_H is still uncomputed.
Flag as critical: any CONDITIONALLY_RESOLVED where the body admits both candidates are undismissed.`
  },
  {
    key: 'tracking-adherence',
    name: 'Tracking File Auditor',
    focus: `Check whether tracking files reflect today's work.
For each new exploration file today: is there a corresponding DERIVATION-PROGRESS.md entry with the ### label (DATE) header?
Is NEXT-STEPS.md updated with a status note for each worked item?
Is RESEARCH-STATUS.md updated if any item changed status?
Missing tracking updates are moderate issues. Stale or contradictory status entries are critical.`
  },
  {
    key: 'scope-creep',
    name: 'Scope Creep and Contradiction Detector',
    focus: `Find files that claim closure but open unnamed sub-problems, or contradict the files they synthesize.
Look for: a file that says problem X is "closed" but the body shows X depends on unresolved Y and Z.
Look for: a synthesis file whose conclusion contradicts the individual files it synthesizes.
Look for: files that start scoped to one problem but drift into claiming results about a different problem mid-derivation.
Flag as moderate: scope expansion without acknowledgment. Flag as critical: synthesis contradiction.`
  },
  {
    key: 'methodology',
    name: 'Research Methodology Auditor',
    focus: `Audit HOW conclusions were reached, not just what they claim.
Check: Are proofs by analogy rather than derivation? Are results asserted without derivation steps?
Does a file cite a sister file produced today as external verification? (Same-session, so it cannot be.)
Are literature references used correctly and not selectively quoted to support a conclusion?
Does the file's conclusion actually follow from its stated premises?
Flag as critical: conclusion that does not follow from premises. Flag as moderate: proof by analogy without derivation.`
  },
]

const ALL_LENSES = [...MATH_LENSES, ...PROCESS_LENSES]

const SHARED_PREAMBLE = `Working directory: ${REPO}
Date: ${DATE}

You are one adversarial reviewer applying 10 distinct review lenses.
Read the changed files once, then run the lenses as separate mental passes over the same evidence.
The goal is broader perspective without multiplying token use.

Start by running: git diff --name-only HEAD
This lists files changed in this session. Read each changed file once, keeping short notes by file.
Then apply all 10 lenses below to those notes and reopen individual files only when a lens needs exact text.`

const issues = await agent(
  `ADVERSARIAL REVIEW — single-pass ten-lens check

${SHARED_PREAMBLE}

REVIEW LENSES:
${ALL_LENSES.map((lens, index) => `
${index + 1}. ${lens.name} (${lens.key})
${lens.focus}`).join('\n')}

Apply every lens, but do not reread the entire repository per lens. Use a single evidence pass,
then run the lenses as compact persona/checklist passes over that evidence.

severity guide:
- critical: wrong verdict, mathematical error, bad canon promotion, same-session circularity — must fix
- moderate: missing failure condition, hidden assumption, tracking gap, scope creep — should fix
- minor: unclear notation, missing citation — note only

For each issue, include the lens key in the issue id, for example "verdict-strength-01".
In sessionPatterns, summarize which lenses found the most serious recurring patterns.`,
  { label: 'adversarial:ten-lens-single-pass', phase: 'Adversarial', schema: ISSUES_SCHEMA }
)

const actionable = issues.items.filter(i => i.severity === 'critical' || i.severity === 'moderate')
log(`Adversarial: ten-lens single pass found ${issues.items.length} issues (${actionable.length} critical/moderate)`)

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
