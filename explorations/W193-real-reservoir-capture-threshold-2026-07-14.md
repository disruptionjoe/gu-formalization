---
artifact_type: exploration
label: W193
created: 2026-07-14
wave: W193
team: REAL-RESERVOIR-CAPTURE
posture: "coherence-first; exploration grade; bounded H21 big-bet discharge; no claim-status, canon, verdict, or public-posture change"
hypothesis: "W189/H21 names the generic-capture lemma as the decisive toy-vs-general gate for the open-Krein loop-unitarity draft. The cheapest bounded discharge is one W187-style dressed r* computation for a real reservoir. This wave replaces W187's analytic square-root toy self-energy with an Ohmic/Drude finite-continuum reservoir and asks whether the capture threshold and sign decider survive."
verdict: "PARTIAL ADVANCE. The W187 sign/capture structure survives one non-square-root real-reservoir model: with an Ohmic/Drude source reservoir J(E)=(E-E0) exp(-(E-E0)/Lambda), threshold E0=0.2, cutoff Lambda=2.5, and the Stelle ghost normalized to M=1, the first real-spectrum capture threshold is r_numeric=1.0802, matching the on-shell spectral-density width-balance prediction r_width=1.0742 within 0.7 percent. The source-off kinematic continuum is pathological; a favorable like-signed reservoir enters a real-spectrum capture window just above r*; a wrong-sign reservoir is not rescued by magnitude up to kappa=10. However, the finite continuum also shows additional resonance windows, so this is not a monotone all-kappa theorem and does not close H21. It advances H21 from pure square-root toy evidence to one explicit real-reservoir computation."
grade: "exploration / finite-model evidence. Deterministic Python test `tests/W193_real_reservoir_capture_threshold.py` gives 7/7 checks, exit 0. The real-reservoir computation is standard-field open-systems machinery applied to the GU/Stelle ghost sign problem; it is not a GU-native source-action construction and not a class theorem. No canon, RESEARCH-STATUS, claim-status, verdict, public-posture, paper-candidate, or cross-repo change."
depends_on:
  - explorations/W187-gu-dressed-open-selfenergy-2026-07-14.md
  - explorations/W188-class-paper-assessment-2026-07-14.md
  - explorations/W189-hardening-register-2026-07-14.md
  - tests/W187_gu_dressed_open_selfenergy.py
scripts:
  - tests/W193_real_reservoir_capture_threshold.py
---

# W193 -- real-reservoir capture threshold for H21

## Role

W189 identifies H21, the **generic-capture lemma**, as the highest-impact big bet for the
open-Krein loop-unitarity draft. The decisive gap is toy-vs-general: W186/W187 showed a finite
Friedrichs/Fano-Anderson stand-in with square-root threshold self-energies, but the draft needs evidence
that a physically reasonable reservoir realizes the same structure.

This wave takes the bounded alternative named in W189: one W187-style dressed `r*` computation for a real
reservoir. It does **not** try to prove the generic lemma. It asks whether the W187 sign/capture structure
survives when the reservoir is an explicit finite quadrature of an Ohmic/Drude continuum rather than an
analytic square-root toy.

## Construction Forks

| Object | Construction Used | Handling |
|---|---|---|
| Ghost / internal channel | GU/Stelle open-Krein sign structure inherited from W187 | Carried as the sign problem under test, not re-derived |
| Reservoir | Standard open-system Ohmic/Drude spectral density | Deliberately not GU-native; this is the toy-vs-general stress test |
| Capture threshold `r*` | On-shell width balance from spectral densities | Compared to the finite total-spectrum threshold |
| Operativity | Real total finite spectrum in the Krein Fano model | Finite-model evidence only |

The reservoir density is

```text
J(E) = (E - E0) exp(-(E - E0) / Lambda), E >= E0.
```

The load-bearing numerical case uses `E0 = 0.2`, `Lambda = 2.5`, internal threshold `0`, and ghost mass
`M = 1`.

## Result

The first real-spectrum capture threshold is:

```text
r_numeric = 1.0802
r_width   = sqrt(J_internal(M) / J_source(M)) = 1.0742
```

The difference is about 0.7 percent. This is the useful W193 fact: the first capture threshold of a
non-square-root real reservoir tracks the same on-shell width-balance object W187 used.

The controls matter:

- With the source off, the kinematic continuum is pathological (`max Im lambda = 0.248`).
- Just below the first threshold the total spectrum is still complex; just above it is real.
- A wrong-sign reservoir is not rescued by magnitude up to `kappa = 10`.
- A positive-definite analog stays real, so the effect is tied to the Krein indefiniteness.

## Honesty Boundary

The finite continuum also shows additional resonance windows. In the verifier, `kappa = 1.2` is real,
`kappa = 2.5` is complex again, and `kappa = 3.0` is real. That prevents the overclaim:

```text
This is a first-capture-window computation, not a monotone all-larger-couplings theorem.
```

So H21 is advanced, not closed. The generic-capture lemma still needs either a theorem over a reservoir
class or a genuine dressed QFT computation. W193 earns a narrower conclusion: W187's square-root toy was
not the only place the sign/capture structure appears.

## Reproduction

```text
python -u tests/W193_real_reservoir_capture_threshold.py
```

Recorded result: `7/7` checks passed, exit 0.

## Non-Effects

No claim status, canon verdict, public posture, paper-candidate status, or cross-repo claim changes. H21
remains open; the open-Krein draft remains draft-grade and toy-vs-general gated.
