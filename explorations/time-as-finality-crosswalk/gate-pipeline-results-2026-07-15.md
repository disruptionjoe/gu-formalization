---
title: "Gate 0/1 -> Gate 3 pipeline results for the live/dark observer sheaf"
status: exploration
doc_type: results-log
created: 2026-07-15
grade: "running results log for the four-gate falsifier. Gate 0/1 = PASS (assumption-light, no dynamics). Gates 2-3 pending. Moves no ledger; asserts no identity; the generation NUMBER stays behind the unwritten source action throughout."
provenance: "Joe, chat 2026-07-15: run the reordered check; start with the assumption-light gates."
depends_on:
  - explorations/time-as-finality-crosswalk/live-dark-observer-sheaf-existence-as-issuance-2026-07-15.md
  - explorations/time-as-finality-crosswalk/ten-persona-steelman-live-dark-observer-sheaf-2026-07-15.md
runnable:
  - explorations/time-as-finality-crosswalk/gate01_observer_nerve.py
verdict: "Gate 0/1 PASS (necessary, not sufficient). Gate 2 is the discriminator and is assumption-heavy (requires positing sign-selection dynamics = the unwritten source action); it is a Joe-gated modeling fork, not auto-run."
---

# Gate pipeline results

## The reordered check (from the ten-persona synthesis, corrected)

Not four co-equal gates: **one artifact** (a dynamically-issued observer nerve) with a decisive
readout plus cheap instrumentation.

- **Gate 0/1 — b1 forced/extensive/deletion-stable (assumption-light, no dynamics).** Best-first: tests the
  oldest wall (forced-not-stipulated) with zero modeling. Read off the nerve alone.
- **Gate 2 — unique-sign vs domains under churn (THE discriminator, assumption-HEAVY).** Requires positing
  the sign-selection dynamics, which *is* the unwritten source action. Any "unique basin" result is
  conditional on the toy dynamics being faithful. Decisive in principle; model-dependent in practice.
- **Gate 3 — redundancy R_delta (records vs discardable redundancy).** Conditional tail: only meaningful if
  Gate 2 yields a unique surviving sign.

## Gate 0/1 — PASS (2026-07-15)

Script: `gate01_observer_nerve.py` (pure Python, no deps). 20 seeds x sizes {50,100,200,400} x three
issuance models. `b1 = E - V + C` (independent loops of the 1-skeleton).

Controls behaved: ring -> b1=1, tree -> b1=0.

| model | b1/N (N=50 -> 400) | frac seeds b1>0 | b1 after 20% node deletion | deletion-stable |
|---|---|---|---|---|
| ER (avg_deg=4) | 0.98 -> 1.05 | 1.00 all N | ~half retained, all >0 | yes |
| BA (m=2) | 0.94 -> 0.99 | 1.00 all N | ~half retained, all >0 | yes |
| RGG (avg_deg~6) | 1.54 -> 1.84 | 1.00 all N | ~half retained, all >0 | yes |

**Verdict: PASS.** The observer nerve carries loops that are **generic** (100% of seeds), **extensive**
(b1/N sustained as N grows -> structural, not marginal), and **deletion-stable** (survives random 20% stalk
removal, still positive and extensive). The specific "no non-vacuous home" wall that killed the spatial-`S^3`
reading (`S^3` is 2-connected, no 1-cycles) is **cleared** for the H1 / pi_1-holonomy reading.

**Honest weighting.** This is the necessary-but-easy gate. `b1 > 0` for a connected graph above the
giant-component threshold is nearly automatic; the genuine content is (i) it concretely removes the `S^3`
objection and (ii) deletion-stability held (not guaranteed a priori). It tests **H1** (1-cycles), **not** the
**H3** 2-gerbe reading E054 used (that needs the full Cech nerve with triple+ overlaps) and **not** the
sign's uniqueness. The weight of the falsification always sat on Gate 2.

## Gate 2a — CONDITIONAL PASS (2026-07-15), exact 𝔽₂

The twenty-persona panel (`twenty-persona-gate2-approach-2026-07-15.md`) reframed Gate 2's core as an
**exact 𝔽₂ / XOR-SAT computation**, not a stochastic sim. Script: `gate2a_f2_consistency.py` (pure Python).
The sign is an Ising/ℤ2 variable `s(v)` per observer; a local rule fixes each edge coupling `J(uv) ∈ {0,1}`
(agree/disagree). A globally consistent **unique universal sign** exists iff `s(u)+s(v)=J(uv) (mod 2)` is
SATISFIABLE, i.e. iff `[J]=0` in `H¹(N;ℤ2)` (no frustrated cycle); the connected SAT solution space is
exactly `2^{components}` = one global bit (bar(b)) up to the external flip. UNSAT ⇒ frustration ⇒ **domains**
⇒ falsified. Controls: all-agree triangle SAT, frustrated triangle UNSAT.

Swept rule family (a stand-in for the C-parity; the specific source action is NOT invented):

| rule | what it models | result (all models, N=100/400, 20 seeds) |
|---|---|---|
| **(P) vertex-potential** `J=g(u)⊕g(v)` | the sign **sourced per-observer** (Joe's "each observer issues its own sign") | **SAT 20/20 everywhere; churn-stable 20/20 after 20% deletion** |
| **(R) random-edge(p)** | a purely **relational / edge** sign | SAT 0/20; frustrated-cycle fraction → ~0.5 |
| **(PN) potential+noise(p)** | per-observer + relational contamination | SAT collapses by `p~0.005` (needs all `b₁` cycles clean); frustration density grows ~linearly in `p` |

**Reading — conditional PASS with a sharp, falsifiable condition.** The hypothesis survives, and Gate 2a
converts it into one crisp requirement: **universality (a unique global bar(b), no domains) holds iff the
sign is vertex-sourced — a per-observer coboundary, cohomologically exact (`[J]=0`).** That is exactly Joe's
"each individual observer sends back the signal it is on / issues its own sign." In that case the global sign
is exact, robust for any `b₁`, and churn-stable. **Any genuinely relational (edge) component produces
frustration → domains → falsified**, and perfect consistency is fragile to relational noise once `b₁` is
large. So the whole question reduces to a single checkable physical claim: **is bar(b) a per-observer datum
(vertex → pass) or a relational one (edge → fail)?**

Scope/honesty: tests the H1 / π₁-holonomy reading (the primary obstruction), not H3; the rule family stands
in for the C-parity and does not derive that bar(b) IS vertex-sourced, nor Krein positivity, nor the number.

## Gate 2b — NOT NEEDED for the pass branch

The panel's rule was: run stochastic dynamics only if 2a shows **generic degeneracy** requiring a dynamics to
break it. 2a shows the opposite — the vertex-sourced (physical) case is **decisively unique** (SAT, one bit),
with no degenerate regime to adjudicate. Gate 2b (consensus / spin-glass domains under churn) would only
characterize the already-falsified relational case. **Skipped.**

## Gate 3 — NEXT (records vs redundancy)

Now the load-bearing follow-on. Persona 12 (threshold secret-sharing) folds it with individual-invisibility:
model bar(b) as a `(k,n)` secret over the observer nerve — individually invisible below threshold `k`
(= T12' zero-trace), collectively reconstructable at `≥ k`. Question: is the vertex-sourced sign a genuine
**record** (redundantly, robustly encoded across independent observers — high redundancy `R_δ`) or
**discardable gauge redundancy**? Plus the standing physics question that Gate 2a isolated: **is the GU/TI
C-parity actually a per-observer (vertex) datum or a relational (edge) one?**
