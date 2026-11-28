#!/usr/bin/env python3
"""Reconcile the immutable v0.263 predecessor with exact reviewed v0.264 edits.
This checks evidence/accounting integrity, not source interpretation or physics.
"""
import copy, hashlib, json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
BASE='lab/process/conditional-physics-ledger-v0.263.json'
NEW='lab/process/conditional-physics-ledger-v0.264.json'
PROPOSALS='lab/process/ledger-v264-row-proposals.json'

def check(base,new,proposals):
    assert len(base['rows'])==len(new['rows'])==91
    before={x['id']:x for x in base['rows']};after={x['id']:x for x in new['rows']}
    assert len(before)==len(after)==91 and set(before)==set(after)
    proposed={x['row_id']:x for x in proposals['row_proposals']}
    assert len(proposed)==50
    changes=0
    for key,row in after.items():
        old=before[key]
        for field in proposals['application_contract']['protected_fields']:
            assert row.get(field)==old.get(field),(key,field,'protected')
        if key not in proposed:
            assert row==old,(key,'untouched')
            continue
        expected=copy.deepcopy(old)
        for c in proposed[key]['changes']:
            assert (c['field']in old)==c['old_present'] and old.get(c['field'])==c['old']
            expected[c['field']]=c['new'];changes+=1
        for field in ['context','target_claim','target_claim_note']:
            expected[field]=row.get(field)
        assert row==expected,(key,'unreviewed edit')
        assert row['evidence'].startswith(old['evidence'])
        assert row.get('context') and all(x in row['context']for x in ['layer','grant','carrier','note'])
    active=[x for x in new['rows']if x.get('row_status')!='SUPERSEDED']
    counts=dict(Counter(x['verdict']for x in active))
    assert len(active)==88 and counts==new['progress']['verdict_counts']==base['progress']['verdict_counts']
    assert new['denominator']==base['denominator'] and new['aliases']==base['aliases']
    assert new['conditional_hypotheses']==base['conditional_hypotheses']
    assert new['wave_row_dispositions']==base['wave_row_dispositions']
    assert new['schema_version']=='0.264' and new['predecessor']==BASE
    assert changes==107
    return {'rows':91,'active':88,'touched':50,'field_changes':changes,'verdict_changes':0,'counts':counts}

if __name__=='__main__':
    base=json.loads((ROOT/BASE).read_text());new=json.loads((ROOT/NEW).read_text());p=json.loads((ROOT/PROPOSALS).read_text())
    assert hashlib.sha256((ROOT/BASE).read_bytes()).hexdigest()==p['base_ledger_sha256']==new['base_sha256']
    result=check(base,new,p)
    # Sensitivity controls: a hidden verdict move and an unreviewed evidence mutation must fail.
    for mutation in ['verdict','evidence']:
        damaged=copy.deepcopy(new)
        damaged['rows'][0][mutation]='INVALID_PLANT'
        try:check(base,damaged,p)
        except AssertionError:pass
        else:raise AssertionError('undetected '+mutation)
    index=json.loads((ROOT/'lab/process/conditional-evidence-deltas/index.json').read_text())
    for item in index['deltas']:
        delta=json.loads((ROOT/item['path']).read_text());assert delta['status']==item['status']
        if delta['integration']and delta['integration']['canonical_ledger_ref']==NEW:
            assert delta['status']=='integrated' and delta['integration']['disposition']=='incorporated'
            assert set(delta['affected_rows'])<=set(x['id']for x in new['rows'])
    print(json.dumps({'status':'PASS',**result,'sensitivity_controls':2}))
