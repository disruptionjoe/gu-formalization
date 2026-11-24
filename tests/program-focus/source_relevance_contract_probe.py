#!/usr/bin/env python3
"""Adversarial process controls; labels are not scientific acceptance."""
from pathlib import Path
import copy
import importlib.util
import json
import tempfile
import yaml

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('focus_gate', ROOT/'process_gates/program_focus_audit.py')
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)
checks = []
def check(name, value):
    assert value, name
    checks.append(name)

valid = {'class_covered':'All operators in declared structural class',
         'premises':['source-constrained: SC-CHI-04; lab/sources/source-claim-register.yaml'],
         'source_bridge':{'status':'conditional','reason':'Physical current identification remains explicit'},
         'kill_condition':'Closes only named family under the declared physical bridge'}
check('conditional declared bridge accepted', not gate.relevance_errors(valid))
for status in ['proved','absent']:
    p=copy.deepcopy(valid);p['source_bridge']['status']=status
    check(status+' label accepted without endorsing truth', not gate.relevance_errors(p))
for key in valid:
    p=copy.deepcopy(valid);p.pop(key)
    check('missing '+key+' rejected', bool(gate.relevance_errors(p)))
for key in ['class_covered','kill_condition']:
    p=copy.deepcopy(valid);p[key]=' '
    check('blank '+key+' rejected', bool(gate.relevance_errors(p)))
for bad in [[],[''], 'SC-CHI-04', [None]]:
    p=copy.deepcopy(valid);p['premises']=bad
    check('malformed premises '+repr(bad), bool(gate.relevance_errors(p)))
for bad in ['probably',None,'source-required']:
    p=copy.deepcopy(valid);p['source_bridge']['status']=bad
    check('invalid bridge label '+repr(bad), bool(gate.relevance_errors(p)))
p=copy.deepcopy(valid);p['source_bridge']['reason']=' '
check('bridge needs its reason',bool(gate.relevance_errors(p)))
focus=yaml.safe_load((ROOT/'CURRENT-STATE.yaml').read_text())['program_focus']
legacy,errors=gate.relevance_baseline(focus)
check('frozen baseline available',not errors and bool(legacy))
check('completed prior metric family retained', 'explorations/conditional-build/metric-normal-family-grading-2026-11-24.md' in legacy)
check('new current wave not grandfathered', 'explorations/conditional-build/source-small-vev-current-test-2026-11-24.md' not in legacy)
with tempfile.TemporaryDirectory(prefix='gu_relevance_') as d:
    fixture=Path(d);gate.copy_fixture(fixture)
    check('clean policy fixture passes',not gate.audit(fixture))
    p=fixture/gate.KITEM_DIR/'new-source-result-2026-11-24.md';p.parent.mkdir(parents=True,exist_ok=True)
    metadata={'program_target':'X-P1-P2-P3','tier':'T2','expected_delta':'Applicability','actual_delta':'Constraint',**valid}
    body='\nprogram_target: X-P1-P2-P3\ntier: T2\nexpected_delta: Applicability\nactual_delta: Constraint\n'
    p.write_text('---\n'+yaml.safe_dump(metadata)+'---\n'+body)
    check('new complete result passes whole gate',not gate.audit(fixture))
    metadata.pop('source_bridge');p.write_text('---\n'+yaml.safe_dump(metadata)+'---\n'+body)
    check('new incomplete result rejected by whole gate',any('source_bridge' in e for e in gate.audit(fixture)))
check('recurring LC rule retained',any('count % 4 == 3' in s for s in focus['run_selection']))
check('no new stopping threshold', 'Add no stopping threshold' in focus['continuation_priority'])
print(json.dumps({'status':'PASS','checks_passed':len(checks),'checks':checks,'ceiling':'Declaration enforcement only; no proof of source necessity or scientific verdict'},indent=2))
