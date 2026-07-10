# tests/carrier-bit-decision/

Carrier-bit decision campaign certificates for the carrier A / carrier B fork.
These scripts and companion analyses support the carrier-bit campaign result;
they are computational and bookkeeping certificates, not claim-status updates.
A green run means the listed checks reproduce the current campaign arithmetic,
field-space declaration fork, and referee cross-checks. It does not change canon,
verdicts, public posture, paper status, or the source action gate.

## Running This Family

List the discovered certificates:

```powershell
python scripts\reproduce_all.py --quick -k carrier-bit-decision --list
```

Run the family through the central harness:

```powershell
python scripts\reproduce_all.py --quick -k carrier-bit-decision --timeout 300
```

Run one leg directly when reviewing a specific claim:

```powershell
python tests\carrier-bit-decision\leg2_obstruction_hardening.py
```

Run the SG4 declaration-triple harness directly when reviewing a source-action
field-space declaration candidate:

```powershell
python tests\carrier-bit-decision\sg4_declaration_triple_harness.py
```

## Boundary

The public boundary stays:

- The campaign outcome is bit-narrowed-but-open, not a carrier verdict.
- SG4 remains the source-action / field-space declaration decider.
- The B-tilt is evidence-tier and cannot be used as canon movement.
- Story-shopping checks are part of the campaign discipline, not public posture.
- Do not use these scripts to change claim status, canon, verdicts, public
  posture, paper status, or protected governance surfaces.

## Direct Analyses

| file | role | current shared outcome |
|---|---|---|
| `leg1_applicability_matrix.py` | Published spin-3/2 no-go and consistency theorem applicability matrix against GU commitments. | No fetched theorem makes gauging mandatory or impossible for GU-as-stated; the ungauged massive vectorlike carrier remains published-viable in its named window. |
| `leg1_applicability_matrix.md` | Narrative analysis for Leg 1, including theorem rows and source quotes. | Records the theorem-applicability matrix and the surviving partial corners. |
| `leg2_obstruction_hardening.py` | Exact Clifford-algebra hardening of the gamma-trace / gauge-orbit obstruction and BRST dichotomy. | Re-derives the obstruction as a mutual-exclusion certificate between constrained and full field spaces. |
| `leg2_obstruction_hardening.md` | Narrative analysis for Leg 2. | Interprets the obstruction as field-space mutual exclusion, not evidence for either carrier. |
| `leg3_ungauged_consistency.py` | Published ungauged spin-3/2 consistency window plus exact Velo-Zwanziger finite check. | Certifies carrier B's physics window while leaving the massless/chiral reconciliation on SG4. |
| `leg3_ungauged_consistency.md` | Narrative analysis for Leg 3. | Records the ungauged consistency window and remaining reading fork. |
| `leg4_verdict_bookkeeping.py` | Exact carrier-bit decision table and consequence bookkeeping. | Keeps all sub-SG4 outcomes as tilts or open states; no leg combo moves canon. |
| `leg4_verdict_bookkeeping.md` | Narrative analysis for Leg 4. | Records the decision table, edge cases, and campaign-level story-shopping corrections. |
| `sg4_declaration_triple_harness.py` | Reusable SG4 harness that reports the required `invariance / declaration / phase` triple for source-action candidates. | Keeps the current state `open_unbuilt` while discriminating carrier A, carrier B, bare, target-import, and acausal-trap controls. |

## Independent Referees

| file | role | current shared outcome |
|---|---|---|
| `referee_leg1_independent.py` | Independent characteristic-class derivation of Leg 1 index arithmetic. | Re-derives the -21 / -19 / -20 densities from signature data without chi import. |
| `referee_leg2_independent.py` | Independent numpy-float and hand-derived route for Leg 2 identities. | Reconfirms the obstruction formula, injectivity off the null cone, null-cone exception, and full-space BRST complex. |
| `referee_leg3_verify.py` | Independent chiral-representation verification for Leg 3. | Rebuilds the VZ computation and PDF-anchor checks through a separate code path. |
| `referee_leg4_verdict_independent.py` | Independent Leg 4 bookkeeping and adversarial probe. | Re-derives the decision-table distribution and carrier class algebra. |

## Process Gate

`process_gates/carrier_bit_decision_readme_inventory_audit.py` keeps this
README synchronized with the live direct scripts and analyses in this directory
and checks that the bit-open / SG4 / no-status-movement boundary remains visible.
