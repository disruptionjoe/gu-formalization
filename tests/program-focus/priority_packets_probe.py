#!/usr/bin/env python3
"""Dated T3 controls for the 2026-11-20 packet registration and source inventory.

No scheduler, source operator, physical count or analytic Fredholm theorem.
The finite examples reproduce p1-p2-domain-index-2026-11-11 §5D/E.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import yaml
from sympy import Matrix, zeros, symbols, simplify

ROOT = Path(__file__).resolve().parents[2]
P1 = 'lab/process/work-packets/observed-hidden-index-split-2026-11-20.md'
P2 = 'lab/process/work-packets/native-complex-order3-fork-2026-11-20.md'

def packet(path):
    text = (ROOT/path).read_text()
    return yaml.safe_load(re.search(r'```yaml\n(.*?)```', text, re.S).group(1))

def select(count, open_t1, available, last):
    """Reference examples of Joe's precedence, not an executing selector."""
    if open_t1:
        return 'finish-T1'
    if count % 4 == 3:
        return 'LC-BETS'
    ready = [p for p in (P1, P2) if p in available]
    if len(ready) == 2:
        return P2 if last == P1 else P1
    return ready[0] if ready else 'ordinary-B-selection'

def controls():
    checks = 0
    assert select(23, False, [P1, P2], P2) == 'LC-BETS'; checks += 1
    assert select(23, True, [P1, P2], P2) == 'finish-T1'; checks += 1
    assert select(24, False, [P1, P2], None) == P1; checks += 1
    assert select(24, False, [P1, P2], P1) == P2; checks += 1
    assert select(24, False, [P1, P2], P2) == P1; checks += 1
    assert select(24, False, [P2], P2) == P2; checks += 1
    assert select(24, False, [], P2) == 'ordinary-B-selection'; checks += 1
    # Exact finite balanced-total / compensating hidden example.
    D = zeros(2, 2); qE = Matrix([[1, 0]]); qF = zeros(0, 2)
    Do = zeros(0, 1); ihE = Matrix([[0], [1]]); Dh = D*ihE
    assert qF*D == Do*qE; checks += 1
    index = lambda A: (A.cols-A.rank())-(A.rows-A.rank())
    assert (index(D), index(Dh), index(Do)) == (0, -1, 1); checks += 1
    # Nonzero connecting map: D=id, Eh=0, Fh=C, Eo=C, Fo=0.
    assert Matrix([[1]]).nullspace() == [] and index(zeros(1, 0)) == -1; checks += 1
    assert index(zeros(0, 1)) == 1; checks += 1
    # Proper q cannot obey the same nondegenerate Krein conformality.
    K = Matrix([[0, 1], [1, 0]]); k, lam = symbols('k lam', nonzero=True)
    assert (qE.T*Matrix([[k]])*qE-lam*K)[0, 1] == -lam; checks += 1
    # Finite exact-sequence dimension telescope, not analytic existence.
    r = symbols('r0:5')
    dims = [r[0]]+[r[i-1]+r[i] for i in range(1, 5)]+[r[4]]
    assert simplify(sum((-1)**i*d for i, d in enumerate(dims))) == 0; checks += 1
    return checks

def audit_current_registration():
    state = yaml.safe_load((ROOT/'CURRENT-STATE.yaml').read_text())
    focus = state['program_focus']; assert focus['version'] == '2026-11-20-v2'
    assert focus['authority'] == 'joe_direct_chat_2026_11_20'
    assert focus['priority_packets'] == [P1, P2]
    matrix = json.loads((ROOT/'lab/process/action-constraint-matrix.json').read_text())
    p3 = next(x for x in matrix['cells'] if (x['row'],x['column']) == ('P3','global_index'))
    assert (p3['packet'], p3['secondary_packet']) == (P1, P2)
    ix = {x['id']:x for x in matrix['intersections']}
    assert ix['X-P1-P2-P3']['packet'] == P1 and ix['X-D1-P3']['packet'] == P2
    for path in [P1, P2]:
        p = packet(path)
        assert [s['id'] for s in p['steps']] == list(range(1,len(p['steps'])+1))
        for step in p['steps']:
            assert step['status'] in ['ready','blocked','done']
            assert all(k in step for k in ['target','tier','expected_delta','kill_condition'])
            assert step['tier'] in ['T1','T2','T3']
        assert p['steps'][0]['status'] == 'done'
    bet = next(x for x in json.loads((ROOT/'lab/process/discovery-bets.json').read_text())['bets'] if x['id']=='BET-2PLUS1')
    assert bet['active_bet_note']['packet'] == P1

def audit_inventory():
    inv = json.loads((ROOT/'lab/process/order3-fork-audit-2026-11-20.json').read_text())
    rx = re.compile(inv['query'], re.I); seen = set(); cache = {}
    for row in inv['records']:
        p = row['path']
        if p not in cache:
            cache[p] = subprocess.check_output(['git','show',f"{inv['base_revision']}:{p}"],cwd=ROOT)
        blob = cache[p]; assert hashlib.sha256(blob).hexdigest() == row['source_sha256']
        lines = blob.decode().splitlines()
        assert any(m.group() == row['text'] and blob.decode().count('\n',0,m.start())+1 == row['line_start'] for m in re.finditer(r'\S[\s\S]*?(?=\n\s*\n|\Z)', blob.decode()))
        assert rx.search(row['text']) and row['construction_tags'] and row['role']
        key = (p,row['line_start']); assert key not in seen; seen.add(key)
    # Rebuild all candidate spans from the pinned source tree, including release copies.
    paths = subprocess.check_output(['git','ls-tree','-r','--name-only',inv['base_revision'],'canon','papers'],cwd=ROOT,text=True).splitlines()
    expected=set()
    for p in paths:
        if Path(p).suffix not in ['.md','.tex','.json','.yaml','.yml','.txt','.cff']: continue
        raw = cache.get(p)
        if raw is None: raw = subprocess.check_output(['git','show',f"{inv['base_revision']}:{p}"],cwd=ROOT)
        text = raw.decode()
        for m in re.finditer(r'\S[\s\S]*?(?=\n\s*\n|\Z)',text):
            if rx.search(m.group()): expected.add((p,text.count('\n',0,m.start())+1))
    assert expected == seen, (expected-seen,seen-expected)
    return len(seen)

if __name__ == '__main__':
    n=controls();audit_current_registration();spans=audit_inventory()
    print(f'PASS: {n} exact precedence/algebra controls; packet wiring; {spans} pinned source spans and full query coverage.')
