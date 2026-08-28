#!/usr/bin/env python3
"""Durability audit for ledger v0.156 full-carrier stationary correction."""

from collections import Counter
import json
from pathlib import Path

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


ROOT = Path(__file__).resolve().parents[1]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def unique_json(path):
    def hook(items):
        keys = [key for key, _ in items]
        if len(keys) != len(set(keys)):
            raise ValueError(f"duplicate key: {path}")
        return dict(items)
    return json.loads(path.read_text(), object_pairs_hook=hook)


ledger = unique_json(ROOT / 'lab/process/conditional-physics-ledger-v0.156.json')
registry = unique_json(ROOT / 'lab/process/selected-k77-full-carrier-stationary-residual.json')
contract = unique_json(ROOT / 'lab/methods/research-evidence-contract-v1.0.json')
report = (ROOT / 'explorations/conditional-build/selected-k77-full-carrier-stationary-residual-2026-08-10.md').read_text()
review = (ROOT / 'lab/process/hostile-reviews/2026-08-10-selected-k77-full-carrier-stationary-residual-review.md').read_text()
source = (ROOT / 'lab/sources/selected-k77-full-carrier-stationary-residual-source-return-2026-08-10.md').read_text()
probe = (ROOT / 'tests/channel-swings/selected_k77_full_carrier_stationary_residual_probe.py').read_text()

print('A. LEDGER AND ACCOUNTING')
check('ledger', 'v0.156 is current and append-only from v0.155', ledger['schema_version']=='0.156' and ledger['predecessor'].endswith('v0.155.json'))
check('ledger', 'coverage remains 82 of 82', ledger['progress']['mapped']==ledger['progress']['total']==82)
check('ledger', 'verdict counts remain unchanged', ledger['progress']['verdict_counts']=={'SAME':32,'DIFFERS':19,'NEEDS':26,'OVER_DETERMINED':5})
check('ledger', 'residue remains 84', ledger['residue']['continuous_real']==84)
check('ledger', 'five quotients remain booked', ledger['residue']['quotients_ranked']==5)
check('ledger', 'P1/P2/P3 are not assigned by this wave', 'P1/P2/P3 are unchanged' in ledger['residue']['meter'])
check('ledger', 'frontier delta is 3 closed 1 opened 3 remaining', ledger['frontier_delta']=={'headline_delta':'NONE','conditions_closed':3,'conditions_opened':1,'remaining_named_conditions':3})

rows = {row['id']:row for row in ledger['rows']}
touched = ['RA-D4','RA-F1','RA-F2','RA-G2','LT-SM3','AC-F1']
check('ledger', 'all six declared rows exist', all(row in rows for row in touched))
check('ledger', 'all six point to the full-carrier result', all(rows[row]['evidence']=='selected-k77-full-carrier-stationary-residual-2026-08-10.md' for row in touched))
check('ledger', 'all six migrations are append-only from v0.155', sum(1 for m in ledger['migrations'] if m.get('from_version')=='0.155' and m.get('to_version')=='0.156')==6)

print('\nB. EXACT RESULT REGISTRY')
check('result', 'full dimensions are 1792 plus 128 equals 1920', registry['full_dimensions']['omega1_spinor']==1792 and registry['full_dimensions']['omega0_spinor']==128 and registry['full_dimensions']['total']==1920)
check('result', 'full residual dimension is 1664', registry['full_dimensions']['full_residual']==1664)
check('result', 'projected residual remains typed conditional', registry['full_dimensions']['conditional_projected_residual']==64)
check('result', 'q-repaired rank/nullity are 256/1664', registry['q_repaired']['rank']==256 and registry['q_repaired']['nullity']==1664)
check('result', 'q-repaired residual is zero rank', registry['q_repaired']['residual_rank']==0)
check('result', 'q-repaired kernel is not promoted', 'NO_PHYSICAL_PROMOTION' in registry['q_repaired']['status'])
check('result', 'source-faithful candidates are row and column Pin', set(registry['source_faithful']['candidates'])=={'row_pin','column_pin'})
check('result', 'source-faithful rank/nullity are 1920/0', registry['source_faithful']['rank_each']==1920 and registry['source_faithful']['nullity_each']==0)
check('result', 'good-prime certificate is recorded', registry['source_faithful']['good_prime']==1000033 and 'QQ_I' in registry['source_faithful']['characteristic_zero_certificate'])
check('result', 'lower-row suppression plant creates 128 modes', registry['source_faithful']['without_lower_row_nullity_each']==128)
check('result', 'all three parents remain separate', len(registry['parent_witnesses'])==3 and registry['parent_identity'].startswith('SEPARATE'))

print('\nC. LAYER 0, SOURCE AND HOSTILE FENCES')
check('layer0', 'report distinguishes projected and full residuals', 'projected residual' in report and 'full residual' in report)
check('layer0', 'report says v0.155 theorem survives', 'v0.155 quotient theorem survives unchanged' in report)
check('layer0', 'report does not identify equal-rank parents', 'equal rank does not identify' in report.lower() and 'parent witnesses' in report.lower())
check('source', 'source return has all three dispositions', all(x in source for x in ['SOURCE-CONFIRMS','SOURCE-CORRECTS','SOURCE-SILENT']))
check('source', 'source-admitted southeast rival stays open', 'southeast rival' in source.lower() and 'unspecified nonzero' in source.lower())
check('hostile', 'summary overrun charge is present', 'Charge 1' in review and 'GU has no fermions' in report)
check('hostile', 'superseded-object charge is present', 'Charge 2' in review and '64 x 64' in review)
check('hostile', 'downstream disposition charge is present', 'Charge 3' in review and 'needs-recheck' in review)
check('analytic', 'analytic fence is explicit', 'Analytic' in review and 'Fredholm' in review)
check('symplectic', 'symplectic/BV fence is explicit', 'Symplectic/BV' in review and 'reduced phase space' in review)

print('\nD. PROCESS POINTERS AND SUCCESSOR')
check('process', 'current append-only ledger descends to v0.156', reaches_historical_snapshot(
    contract, 'lab/process/conditional-physics-ledger-v0.156.json'
))
check('process', 'successor is moving-varpi determinant intersection', 'MOVING_VARPI_DETERMINANT_LOCUS' in registry['next_gate'])
check('process', 'southeast rival remains separate in successor', 'SOUTHEAST_NONZERO_RIVAL_SEPARATE' in registry['next_gate'])
for path in ['NEXT-STEPS.md','RESEARCH-STATUS.md','lab/process/README.md']:
    check('process', f'{path} names v0.156', 'v0.156' in (ROOT/path).read_text())
check('process', 'source index lists the return', 'selected-k77-full-carrier-stationary-residual-source-return' in (ROOT/'lab/sources/README.md').read_text())
check('process', 'test manifest lists the exact probe', 'selected_k77_full_carrier_stationary_residual_probe.py' in (ROOT/'tests/README.md').read_text())
check('process', 'process-gate manifest lists this audit', 'full_carrier_stationary_residual_audit.py' in (ROOT/'process_gates/README.md').read_text())

print('\nE. EXECUTABLE PROBE FENCES')
check('probe', 'probe uses the full 1792 carrier dimension', '1792 - 128' in probe)
check('probe', 'probe checks QQ(i) q-repaired identities', 'Gaussian-rational' in probe)
check('probe', 'probe computes full 1920 rank', 'row["full_rank"] == 1920' in probe)
check('probe', 'probe has a lower-row suppression plant', 'omitting the action-tied lower row' in probe)
check('probe', 'probe keeps all three parents separate', all(name in probe for name in registry['parent_witnesses']))
check('probe', 'probe carries variational, analytic and symplectic fences', all(f'"{kind}"' in probe for kind in ['variational','analytic','symplectic']))

total = sum(COUNTS.values())
print(f'\nSUMMARY {total-len(FAILURES)}/{total} PASS; counts={dict(COUNTS)}')
if FAILURES:
    raise SystemExit('failures: ' + '; '.join(FAILURES))
