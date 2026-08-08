---
artifact_type: hostile_review
mandatory_lenses: [layer0_semantics, prior_art, symplectic_geometry, principal_bundle_geometry, variational_pde, krein_operator]
---

# Hostile review — selected K77 action-bundle and observation overlap

Date: 2026-08-08
Disposition: **PASS WITH FINITE-ATLAS AND PHYSICAL-SECTION FENCE**

## Charges

### 1. Symplectic geometer

The correct object is the complete cotangent one-form/equation dual, not a
field-sector fragment.  The co-moving observation receiver and projector
preserve the full-support coefficient pairing on both overlaps and under the
opposite endpoint restriction.  This is necessary input to BFV work, but it
does not construct a moment map, polarization, charge algebra or reduced phase
space.  The charge passes only with that fence.

### 2. Principal-bundle and differential geometer

The source-owned `P_H`/`gamma_epsilon` bundle was reused.  The test contains
two noncommuting K77 transitions, checks direct versus sequential cocycles,
and transforms every exterior and Clifford index.  This is a strong finite
certificate of the natural associated-bundle law.  It is not an exhaustive
construction of a smooth atlas or an integrable physical observation section
on arbitrary `X`.

### 3. Variational and exact-computation reviewer

Every patch bank is recomputed from transformed `B,T` fields.  It is then
compared with the independently predicted coadjoint transport.  A second
background passes, and a separate Sage implementation rebuilds the full bank.
The wrong coefficient-dual order fails.  The result is not produced by
transporting a single bank under a new name.

### 4. Observation/no-leakage adversary

`R L=1` is insufficient.  The probe exhibits a nonzero ambient covector in the
kernel of the observed transpose.  No-leakage requires the complementary
projector to co-move; freezing it fails.  The report therefore does not infer
physical faithfulness merely from a complete equation coordinate system.

### 5. Krein/operator and hyperbolic-PDE reviewer

The coefficient form descends algebraically and remains indefinite.  Neither
descent nor finite nondegeneracy supplies positive energy, a maximal
dissipative domain, Green hyperbolicity or a common closed Krein domain.  All
remain open.

### 6. Source and Layer-0 reviewer

Weinstein's materials support `P_H`, moving `epsilon`/Clifford geometry, and
observation by a section.  They do not print this complete equation dual,
projector, preferred Shiab or BFV theorem.  Those are repo constructions.
The source return is correctly split into `SOURCE-CONFIRMS`, `SOURCE-SILENT`
and `REPO-DERIVES` clauses.

## Charge 3 — if this result stands, what else must change?

| surface | disposition | required consequence |
| --- | --- | --- |
| ledger rows `LT-GR1`, `LT-GR2b`, `LT-GR3`, `LT-GR5`, `LT-GR6` | **survives with narrower distance** | migrate from pointwise/global-overlap-open to physical-section-integrability/BFV-domain-open |
| ledger v0.77 and its full pointwise-bank report | **survives** | retain as the coefficient-fibre predecessor; do not rewrite it as a global theorem |
| current queue/context/contract pointers | **survives with update** | point to v0.78 and the physical observation-section successor |
| preferred historical Shiab, global `tau_A0`/BFV and common domain | **needs-recheck** | no conclusion follows from finite overlap descent |
| arbitrary-X Lorentz/observation-section existence and jet holonomicity | **needs-recheck** | construct rather than infer from the associated-bundle law |
| canon verdict, claim status, public posture, P1/P2/P3 | **survives unchanged** | no propagation or promotion authorized |

Nothing is dissolved. The result shortens five construction distances and
supersedes only the statement that action/complete-observation overlap itself
is still untested.

## Two-sided synthesis audit

- **Summary outruns artifact:** prevented by saying “finite noncommuting
  overlap certificate” rather than “arbitrary-X physical section exists.”
- **Fence defends superseded object:** prevented by composing the already-owned
  global K77 bundle and complete-germ theorem instead of rebuilding either.

## Independent rerun

```text
Python exact overlap probe:        41/41 PASS
Independent Sage overlap route:    19/19 PASS
v0.77 predecessor inside Python:   58/58 PASS
independent Sage predecessor:      27/27 PASS
seed and held-out patch families:  PASS
frozen observation/projector:      FIRED
hidden-covector left-inverse plant: FIRED
```

No claim-status, canon-verdict or public-posture change is authorized.
