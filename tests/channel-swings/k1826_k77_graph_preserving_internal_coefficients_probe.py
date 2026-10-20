#!/usr/bin/env sage-python
"""Independent small-matrix and Clifford audit of K1826 (no producer import).

Full rational ambient reconstruction is reused evidence. This audit checks
Pauli completeness, the saved module equivalences and complex product algebra,
and row/column cyclicity's algebraic transfer, including contrary controls.
"""
import copy
import json
from pathlib import Path
from sage.all import QQ, matrix, identity_matrix, block_diagonal_matrix, zero_matrix

ROOT=Path(__file__).resolve().parents[2]
PATH=ROOT/'lab/process/k1826-k77-graph-preserving-internal-coefficients.json'
checks={}
def check(n,c):
    checks[n]=bool(c)
    if not c:raise AssertionError(n)
def read_matrix(d):
    return matrix(QQ,*d['shape'],{(i,j):QQ(v) for i,j,v in d['entries']})
def parity(x):return int(x).bit_count()%2
def commutes(a,b):return parity((a&127)&(b>>7))==parity((b&127)&(a>>7))
def monomial(mask):
    x,z=mask&127,mask>>7
    return matrix(QQ,128,128,{(r,r^x):(-1)**parity(r&z) for r in range(128)},sparse=True)
def validate(d):
    c=d['certificate']
    assert c['uniform_commutant_masks']==[0,16256]
    assert c['graph_generator_binary_rank']==13
    assert c['augmented_algebra']=='M8(C) direct_sum M8(C)'
    assert c['augmented_sector_multiplicities']==[16,16] and c['augmented_sharp_rank_unit']==32
    assert c['different_slot_plus_principal_algebra']=='M512(R)'
    assert c['cyclicity']['column_rank']==c['cyclicity']['row_rank']==512
    assert d['source_and_ledger_effect']=='none'
    assert 'not source-owned' in c['normalization']

D=json.loads(PATH.read_text());validate(D);C=D['certificate']
# Reconstruct all gamma matrices directly, not via the producer.
i2=identity_matrix(QQ,2,sparse=True)
x=matrix(QQ,[[0,1],[1,0]],sparse=True)
z=matrix(QQ,[[1,0],[0,-1]],sparse=True)
y=matrix(QQ,[[0,1],[-1,0]],sparse=True)
def tensor(fs):
    out=matrix(QQ,[[1]],sparse=True)
    for f in fs:out=out.tensor_product(f)
    return out
gammas=[tensor([z]*j+[g]+[i2]*(6-j)) for g in (x,y) for j in range(7)]
for b in C['graph_blocks']:
    r,s=b['ambient_slot'],b['observed_slot'];eta=1 if r<7 else -1
    check('graph_clifford_word_'+str(r)+'_'+str(s),QQ(b['coefficient'])*monomial(b['mask'])==-QQ(eta)/20*gammas[r]*gammas[s])
masks=[b['mask'] for b in C['graph_blocks']]
survivors=[k for k in range(16384) if all(commutes(k,m) for m in masks)]
check('all_real_matrix_coefficients_classified',survivors==[0,16256])
# Sparse conjugation is diagonal on the complete Pauli basis. A sum of
# distinct eigencharacters cannot cancel a nonzero commutator with a monomial.
check('explicit_gamma0_rejected',any(not commutes(64,m) for m in masks))
check('volume_non_scalar_involution',monomial(16256)**2==identity_matrix(QQ,128) and monomial(16256).trace()==0)
reps=[[read_matrix(a) for a in rep] for rep in C['representatives']]
J=read_matrix(C['principal_complex_structure']);I=identity_matrix(QQ,16)
check('complex_structure',J*J==-I and all(A*J==J*A for A in reps[0]))
for k,rep in enumerate(reps):
    T=read_matrix(C['intertwiners'][k]);sign=C['volume_signs_by_type'][k]
    check('actual_principal_intertwiner_'+str(k),T.det()!=0 and all(T*A==B*T for A,B in zip(reps[0][:3],rep[:3])))
    check('actual_volume_sign_'+str(k),T*reps[0][3]==sign*rep[3]*T)
words=[]
for w in C['word_basis']:
    M=I
    for j in w:M=M*reps[0][j]
    words.append(M)
check('independent_complex_algebra_rank',matrix(QQ,[M.list() for M in words]).rank()==128)
check('words_stay_complex_linear',all(M*J==J*M for M in words))
V=reps[0][3];check('volume_is_unit_inside_local_algebra',V*V==I and V*J==J*V)
# The algebra contains both diagonal copies and the independent sign sector.
Dvol=block_diagonal_matrix([V,-V]);same=block_diagonal_matrix([V,V])
sep=block_diagonal_matrix([I,-I]);check('central_separation',same*Dvol==sep)
left=(identity_matrix(QQ,32)+sep)/2;right=(identity_matrix(QQ,32)-sep)/2
check('central_idempotents',left*left==left and right*right==right and left*right==0)
check('two_sixteen_copy_sectors',sum(C['volume_signs_by_type'][t]==1 for t in C['component_types'])==16 and len(C['component_types'])==32)
# Contraries: a triangular preserving operator need not reduce a projector;
# mere column cyclicity cannot establish full two-sided algebra generation.
P=matrix(QQ,[[1,0],[0,0]]);B=matrix(QQ,[[1,1],[0,2]])
check('preservation_not_general_commutation',(identity_matrix(QQ,2)-P)*B*P==0 and B*P!=P*B)
S=matrix(QQ,[[1],[0]]);Q=S.transpose();A=matrix(QQ,[[0,0],[1,0]])
check('column_cyclic_row_not_cyclic',matrix(QQ,[S.column(0), (A*S).column(0)]).rank()==2 and (Q*A)==0)
# Independent constructive two-sided transfer: cyclic column/row bases
# multiplied around embedded End(seed) give all matrix units.
Swap=matrix(QQ,[[0,1],[1,0]])
units=[U*S*Q*V for U in (identity_matrix(QQ,2),Swap) for V in (identity_matrix(QQ,2),Swap)]
check('two_sided_cyclicity_gives_all_endomorphisms',matrix(QQ,[M.list() for M in units]).rank()==4)
check('rank_one_does_not_select_action',S*Q==P and P.rank()==1)
for field,value in [('uniform_commutant_masks',[0]),('augmented_algebra','M16(R)'),('augmented_sharp_rank_unit',64),('augmented_sector_multiplicities',[32]),('different_slot_plus_principal_algebra','M8(C)')]:
    bad=copy.deepcopy(D);bad['certificate'][field]=value
    try:validate(bad)
    except AssertionError:check('reporting_fault_'+field,True)
    else:raise AssertionError(field)
bad=copy.deepcopy(D);bad['source_and_ledger_effect']='physical-state'
try:validate(bad)
except AssertionError:check('reporting_fault_physics',True)
else:raise AssertionError('physics')
print(json.dumps({'checks_passed':sum(checks.values()),'checks_total':len(checks),'full_ambient_reconstruction':'reused producer evidence; not independently rerun','reporting_mutations':6}))
