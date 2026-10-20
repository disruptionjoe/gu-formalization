#!/usr/bin/env sage-python
"""Independent small-dimensional elimination and reporting controls; no producer import."""
from sage.all import QQ,matrix,identity_matrix,zero_matrix,block_matrix
from pathlib import Path
import json,copy,hashlib
ROOT=Path(__file__).resolve().parents[2]
I=identity_matrix(QQ,2);Z=zero_matrix(QQ,2);g=matrix(QQ,[[0,1],[1,0]]);h=matrix(QQ,[[0,1],[-1,0]]);S=matrix(QQ,[[QQ(11)/24,0],[0,QQ(11)/12]]);T=g*S
# Three field slots: observed time, hidden, zero form. Invert directly,
# rather than importing the declared inverse block formula.
D=block_matrix([[Z,Z,I],[Z,I,Z],[-I,Z,T]]);Di=D.inverse()
O=block_matrix([[I,Z,Z],[Z,Z,I]]);L=block_matrix([[I,Z],[-h*g/20,Z],[Z,I]])
e0=block_matrix([[I],[Z],[Z]]);en=block_matrix([[Z],[Z],[I]])
assert O*L==identity_matrix(QQ,4)
count=0
for B in [matrix(QQ,2,2,{(a,b):1}) for a in range(2) for b in range(2)]+[I,Z,matrix(QQ,[[1,2],[3,4]])]:
    raw=Di*en*B;defect=raw-L*O*raw
    assert defect.rank()==B.rank()
    N=T.inverse()*B
    fixed=Di*(e0*N+en*B)
    assert fixed==en*N and fixed==L*O*fixed and fixed.rank()==B.rank()
    if B:
        wrong=Di*(-e0*N+en*B)
        assert wrong!=L*O*wrong
    count+=1
# Noncommuting order matters: an incorrect Riesz/normalization order is caught.
assert S.inverse()*g!=g*S.inverse()
assert T*(g*S.inverse())!=I
# Basis-level elimination proves the two-cell relation on all 2x2 N,B.
for row in range(2):
 for col in range(2):
    N=matrix(QQ,2,2,{(row,col):1});B=T*N
    assert Di*(e0*N+en*B)==en*N
# Coordinate compression is not graph descent: O sees none of a hidden perturbation.
wrongL=copy.copy(L);wrongL[2,0]+=1
assert O*wrongL==identity_matrix(QQ,4) and wrongL!=L

def validate(d):
    r=d['results'];assert r['raw_southeast_only_preserves_graph_iff']=='B=0'
    assert r['leakage_rank']=='rank(B)' and r['minimal_two_cell_repair']=='N=S^-1 gamma0 B'
    assert r['corrected_one_column_dimension']==65536 and r['fixed_southeast_affine_dimension']==49152
    assert r['raw_source_action_selected'] is False and r['physical_or_canon_promotion'] is False
    assert all(d['checks'].values()) and len(d['checks'])==49
    for p,digest in d['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==digest
    assert d['test_ranks']=={'identity':128,'rank_one':1,'nilpotent':1,'rank_64':64,'zero':0,'gamma':128}
d=json.loads((ROOT/'lab/process/k1828-k77-raw-zero-form-completion.json').read_text());validate(d)
faults={'raw_southeast_only_preserves_graph_iff':'any B','leakage_rank':'0','minimal_two_cell_repair':'N=gamma0 S^-1 B','fixed_southeast_affine_dimension':65536,'raw_source_action_selected':True,'physical_or_canon_promotion':True}
for key,val in faults.items():
    bad=copy.deepcopy(d);bad['results'][key]=val
    try:validate(bad)
    except AssertionError:pass
    else:raise AssertionError('reporting fault not rejected')
print(f'PASS K1828 probe: {count} small-model column/rank controls, 4 basis eliminations, normalization-order and false-lift faults; {len(faults)} reporting faults')
