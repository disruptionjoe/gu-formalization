export const meta = {
  name: 'gu-research-loop',
  description: 'GU formalization autonomous research loop: pick 3 open computations, run them in parallel, commit results',
  phases: [
    { title: 'Orient', detail: 'Read project state and pick 3 next computations' },
    { title: 'Compute', detail: 'Run 3 parallel bounded computations with full mathematical context' },
    { title: 'Commit', detail: 'Stage all new files and commit' },
  ],
}

// ── Phase 1: Orient ──────────────────────────────────────────────────────────

phase('Orient')

const state = await agent(
  `You are orienting the GU formalization autonomous research loop.
   Working directory: C:\\Users\\joe\\JB\\Github Repos\\gu-formalization

   1. Run: git log --oneline -20
   2. Read: NEXT-STEPS.md (look for items NOT marked with ~~ strikethrough and NOT recently committed — check file dates in explorations/)
   3. Read: .claude/commands/gu-compute.md (this is the established mathematical context)

   DEDUPLICATION RULE (critical): Run `git log --oneline --since="6 hours ago"` and `ls explorations/` to get the list of files committed or created in the last 6 hours. Do NOT pick any item whose output file (by name pattern) already appears in that list — even if it is CONDITIONALLY_RESOLVED. Each item should only be worked on once per session unless its verdict is still OPEN (not CONDITIONALLY_RESOLVED or RESOLVED). Picks must be 3 DISTINCT items not already worked this session.

   Current known state (as of 2026-06-23, after 10 autonomous loop passes):
   RESOLVED: sc1-shiab-domain-codomain, vz-schur-complement (EVADED)
   CONDITIONALLY_RESOLVED (do not re-pick unless new sub-problem named): codazzi-sp64, codazzi-general, cpa1-tobs, hc1-sl2c, ic1-soldering-map, ic2-positivity, ic3-nonlinear-conservation, ic4-lagrangian-tmunu, ii-s-moving-frames, ind-top-eta-s3-aps, ind-top-x4-atiyah-singer, n5-discrete-series-gl4r, oq3a-gu-variational-k3, pc1-spin77, vz-oq1, vz-oq2, vz-subprincipal
   OPEN (eligible for re-pick): anything in NEXT-STEPS.md not in the above lists

   Priority list for genuinely new work (in order):
   1. plancherel-mult — Compute the Weyl-group orbit count for S(6,4)|_{SO_0(3,1)} = 4xD(1/2,0) + 4xD(0,1/2) in the Flensted-Jensen discrete decomposition of L^2(SL(4,R)/SO_0(3,1)). Verify each orbit contributes one discrete summand with the right H-type, giving m_H = 24. This is the LAST gate for the generation count. Output: explorations/n5-plancherel-multiplicity-2026-06-23.md
   2. vz-f5-curvature — Verify that lower-order curvature terms in the curved Sp(64) bundle do not reintroduce VZ acausality after the principal-symbol evasion (VZ failure condition F5). Uses sub-principal symbol from vz-subprincipal file. Output: explorations/vz-f5-curvature-check-2026-06-23.md
   3. rfail-umbilic — Show that totally umbilic critical sections of E[s]=int|II_s|^2 satisfy R_fail=0 in vacuum (or identify the obstruction). Uses Codazzi and Gauss equations already derived. Output: explorations/rfail-umbilic-sections-2026-06-23.md
   4. weyl-group-24 — Explicit Weyl group S_4 orbit enumeration for the Casimir condition pi(C_sl4r) = 3/4 on D(1/2,0) H-types in L^2(SL(4,R)x_{SO_0(3,1)}S(6,4)). Independent route to m_H=24. Output: explorations/weyl-group-s4-orbit-2026-06-23.md
   5. vz-4d-eft — Analyze the 4D EFT limit (VZ failure condition F6): does a KK-type mass scale separate the RS sector into an approximately standalone field? Use the section-pullback Codazzi correction to estimate the RS/spin-1/2 mixing gap. Output: explorations/vz-f6-eft-decoupling-2026-06-23.md
   6. cpa1-omega — Identify the Omega-constant tuning required for the CPA-1 coefficient match between GU Tikhonov Lambda~eps^2/t_obs^2 and TaF FR2 lambda_max=1/t_obs. What physical model produces exact equality? Output: explorations/cpa1-omega-tuning-2026-06-23.md
   7. n3-discharge — Discharge or record H3: the Cech-H^1 <-> holonomy dictionary in time-as-finality (tests/T63) is conditional on H3; run the cech_sheaf_fixture in temporal-issuance (E015 route). Output: explorations/n3-h3-cech-holonomy-2026-06-23.md

   If all 7 are already done: read NEXT-STEPS.md for any other OPEN items and propose genuinely new bounded computations.

   Return a JSON array of exactly 3 objects, each with:
   { "label": "plancherel-mult", "outputFile": "explorations/n5-plancherel-multiplicity-2026-06-23.md", "problem": "one sentence description of what to compute" }

   Today's date is 2026-06-23.`,
  {
    label: 'orient:pick-3',
    schema: {
      type: 'object',
      properties: {
        picks: {
          type: 'array',
          items: {
            type: 'object',
            properties: {
              label: { type: 'string' },
              outputFile: { type: 'string' },
              problem: { type: 'string' },
            },
            required: ['label', 'outputFile', 'problem'],
          },
          minItems: 3,
          maxItems: 3,
        },
      },
      required: ['picks'],
    },
  }
)

log(`Picked: ${state.picks.map(p => p.label).join(', ')}`)

// ── Phase 2: Compute ─────────────────────────────────────────────────────────

phase('Compute')

const MATH_CONTEXT = `
ESTABLISHED MATHEMATICAL CONTEXT — read before computing:

Geometry:
- Y^14 = Met(X^4): bundle of Lorentzian metrics on 4-manifold X^4
- Fiber: GL(4,R)/O(3,1) ≃ RP^3, signature (9,5) total
- Cl(9,5) ≅ M(64,H) — quaternionic; spinor module S = H^{64}, dim_R = 256
- w_2(Y^14) = 0 for any orientable X^4 — RESOLVED

Algebra and gauge group:
- Gauge group Sp(64) = U(64,H), dim sp(64) = 8256
- Sp(64) anomaly-free: pseudoreal (J^2 = -1), n_L - n_R = 0; pi_15(Sp) = Z, no global Z_2 anomaly
- Nguyen §2 (anomaly pincer) and §3.1 (complexification gap) FULLY CLOSED

Shiab and tau+:
- Shiab Phi: Omega^2(Y^14)@S -> Omega^1(Y^14)@S via Phi(alpha@s) = sum_a e^a @ c(iota_{e_a} alpha).s
- H-linear, Spin(9,5)-equivariant, no complexification
- tau+: G -> IG = G x| Omega^1(ad P); g |-> (g, g^{-1}d_Ag) — purely group-theoretic

Dark energy:
- Distortion theta = A - Gamma; D_A*theta = 0 by Noether (CLOSED)

Generation count (CONDITIONALLY 3):
- S(6,4) = C^16; Cl(6,4) ≅ M(16,C)
- Pati-Salam: S(6,4) -> (4,2,1) + (4bar,1,2) -> 16 Weyl fermions = 1 SM generation (CONFIRMED)
- D_GU commutes with right-H multiplication -> index counts H-lines; 8 H-lines per SM generation
- Generation count = 2 (spin-1/2) + 1 (RS) = 3 — CONDITIONAL on discrete-series computation

4D reduction (partial):
- s*(theta) = II_s (second fundamental form) — reconstruction grade
- Spinor branching S(9,5) = S(3,1) @ S(6,4) — SM content verified
- Willmore energy E[s] = integral |II_s|^2 selects critical sections
- Tikhonov scale: Lambda ~ eps^2/t_obs^2

VZ (OPEN):
- VZ fires at 4D (RS(3,1)@S(6,4) carries SM charges)
- 14D evasion candidate: RS sector = Leibniz cross-term in D_GU -> D_{RS,1/2} nonzero by construction
- Priority: Schur complement symbol D_RS_eff

Hidden curvature (CONDITIONALLY RESOLVED):
- 6-piece SO(1,3) decomp: W + S_0 + R (visible) + H^(1) + H^(2) + H^(3) (torsion-activated)
- SL(2,C) labels at reconstruction grade; coupling to theta vs standard torsion is main residual

Cross-program contact:
- GU Tikhonov: Lambda ~ eps^2/t_obs^2
- TaF FR2: lambda_max = 1/t_obs
- CPA-1: compute explicit coefficient and compare
`

const results = await parallel(
  state.picks.map(pick => () =>
    agent(
      `You are running a bounded GU formalization computation.
       Working directory: C:\\Users\\joe\\JB\\Github Repos\\gu-formalization
       Today's date: 2026-06-23

       PROBLEM: ${pick.problem}
       LABEL: ${pick.label}
       OUTPUT FILE: ${pick.outputFile}

       ${MATH_CONTEXT}

       For additional context on this specific problem, read .claude/commands/gu-compute.md.

       INSTRUCTIONS:
       1. Attempt the computation ambitiously. Aim for reconstruction grade or better — not just a plan.
       2. State explicit failure conditions (what would falsify the result).
       3. Write the output to ${pick.outputFile} with this frontmatter:
          ---
          title: "<descriptive title>"
          date: 2026-06-23
          problem_label: "${pick.label}"
          status: exploration|reconstruction|verified|open
          verdict: RESOLVED|CONDITIONALLY_RESOLVED|OPEN|EVADED|GENUINE_OBSTRUCTION
          ---
       4. Update NEXT-STEPS.md: find the relevant row and append a brief status note.
       5. Append a 3-4 sentence log entry to DERIVATION-PROGRESS.md:
          ### ${pick.label} (2026-06-23)
          Verdict: <verdict>
          <what was computed, result, what remains>
          File: \`${pick.outputFile}\`

       Return a summary: label, verdict, one sentence on the result, and whether tracking files were updated.`,
      { label: `compute:${pick.label}`, phase: 'Compute' }
    )
  )
)

log(`Computations complete: ${results.filter(Boolean).length}/3 succeeded`)

// ── Phase 3: Commit ───────────────────────────────────────────────────────────

phase('Commit')

const labels = state.picks.map(p => p.label).join(', ')

await agent(
  `Commit all new and modified files in the GU formalization repo.
   Working directory: C:\\Users\\joe\\JB\\Github Repos\\gu-formalization

   1. Run: git status
   2. Stage all untracked exploration files and modified tracking files (NEXT-STEPS.md, DERIVATION-PROGRESS.md, canon/no-go-class-relative-map.md if modified).
   3. Commit with message:
      GU autonomous loop: ${labels} (2026-06-23)

      Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
   4. Do NOT push.
   5. Return: commit hash and list of files committed.`,
  { label: 'commit', phase: 'Commit' }
)

return { labels, runs: results.filter(Boolean).length }
