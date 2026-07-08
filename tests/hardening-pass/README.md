# tests/hardening-pass/

Certificate scripts for the 2026-07-03 located-not-forced hardening-pass drafts.
These scripts support staged paper-hardening artifacts; they are not canon,
claim status updates, verdicts, public posture changes, or paper status
changes. A green run keeps the draft-support computations reproducible and
preserves the no-target-import boundary. It does not provide a
generation-count derivation, promote the drafts, or close residuals named by
the drafts.

## Running This Family

List the discovered certificates:

```powershell
python scripts\reproduce_all.py --quick --tracked-only --list -k tests/hardening-pass
```

Run the family through the central harness:

```powershell
python scripts\reproduce_all.py --quick --tracked-only -k tests/hardening-pass --timeout 300
```

Run one direct certificate when reviewing a specific hardening-pass item:

```powershell
python tests\hardening-pass\oqrk1_indh_rank.py
```

## Boundary

The public boundary stays:

- These scripts support staged drafts under `papers/drafts/hardening-pass-2026-07-03/`; they do not promote the drafts.
- The OQ-RK1 rank result is honest-negative evidence for the tested route, not a generation-count derivation.
- The route-(a) classification reproduces exact symbolic dimensions while keeping the named residuals open.
- Independent verifiers reduce implementation risk; they do not change canon, claim status, verdicts, public posture, paper status, or protected governance surfaces.
- Do not use these scripts to divide by target numbers such as `3`, `4`, `8`, `24`, `chi(K3)`, or `Ahat(K3)`.

## Direct Certificates

| script | role | current shared outcome |
|---|---|---|
| `enum_route_a_classification.py` | Exact-arithmetic route-(a) classification for the hardening pass. | Rebuilds the `2/2/2/2/0` generator-space dimensions symbolically and names residuals R1/R2/R3 as open. |
| `oqrk1_indh_rank.py` | Direct OQ-RK1 composite-rank certificate on the common `Cl(9,5)` vector-spinor carrier. | Computes composite rank `832_C / 416_H` without target import; the physical-projector / gauge-fixed / K-theory legs remain blocked by specification needs. |

## Independent Verifiers

| script | role | current shared outcome |
|---|---|---|
| `verify/adv_recheck.py` | Adversarial recheck of OQ-RK1 structure and rank behavior. | Confirms the rank conclusion without relying on the main direct script path. |
| `verify/adv_recheck_832.py` | Focused recheck of the `832_C` composite-rank result. | Preserves the anti-target-import rank output. |
| `verify/indep_hom_klimyk_direct.py` | Independent Klimyk-style Hom-space recheck for the route-(a) classification. | Reconfirms the relevant Hom-space dimensions without the main symbolic implementation. |
| `verify/oqrk1_indh_rank_indep_check.py` | Independent OQ-RK1 rank derivation. | Rebuilds the rank check through a separate implementation path and agrees with the direct hardening-pass result. |
