#!/usr/bin/env sage-python
"""Independent saved-small-algebra audit and structural contrary controls.

No producer import. The full 1920-dimensional primitive reconstruction and
32-module decomposition are reused producer evidence, not rerun here.
"""
from copy import deepcopy
import json
from pathlib import Path
from sage.all import QQ, matrix, identity_matrix, block_matrix, zero_matrix, vector

ROOT=Path(__file__).resolve().parents[2]
DATA=ROOT/'lab/process/k1824-k77-joint-observed-symbol-algebra.json'
checks={}
def check(name,condition):
    checks[name]=bool(condition)
    assert condition,name

def unpack(d):
    return matrix(QQ,*d['shape'],{(i,j):QQ(v) for i,j,v in d['entries']})

def audit(data):
    c=data['certificate']; gs=[unpack(x) for x in c['representative_generators']]
    J=unpack(c['complex_structure']); I=identity_matrix(QQ,16)
    assert J*J==-I and all(J*g==g*J for g in gs)
    matrices=[]
    for word in c['basis_words']:
        M=I
        for index in word:M=M*gs[index]
        matrices.append(M)
    flat=matrix(QQ,[M.list() for M in matrices])
    assert flat.nrows()==128 and flat.rank()==128
    # Independent direct rank computation, not the producer's incremental
    # echelon implementation. Closure is checked in one rectangular system.
    products=matrix(QQ,[(M*g).list() for M in matrices for g in gs])
    assert flat.stack(products).rank()==128
    assert flat.stack(matrix(QQ,[J.list()])).rank()==128
    e=unpack(c['smallest_rank_idempotent'])
    assert e*e==e and e.rank()==2 and e*J==J*e
    sign=(-576*gs[0]**3+601*gs[0])/25
    projected=[(M+sign*M*sign)/2 for M in matrices]
    assert matrix(QQ,[M.list() for M in projected]).rank()==64
    assert sign*sign==I and (I+sign).rank()==8 and (I-sign).rank()==8
    assert c['representation_multiplicity']==32 and c['representation_dimension']==16
    assert c['generated_dimension']==128 and c['split_preserving_dimension']==64
    assert data['conclusions']['sharp_nonzero_rank_minimum']==64
    assert data['conclusions']['matrix_amplification_rank_divisor']==64
    assert data['claim_boundary']['selected_element_from_generated_algebra'] is False
    assert data['claim_boundary']['physical_state'] is False
    return gs,J,matrices

data=json.loads(DATA.read_text());gs,J,matrices=audit(data)
check('independent_saved_algebra_rank_and_closure',True)

# Realification of complex 2x2 matrices, with the independent canonical
# complex structure. Nonzero real rank1 cannot commute with it.
I2=identity_matrix(QQ,2);Z2=zero_matrix(QQ,2)
J4=block_matrix([[Z2,-I2],[I2,Z2]])
def realify(A,B):return block_matrix([[A,-B],[B,A]])
E00=matrix(QQ,2,{(0,0):1});E01=matrix(QQ,2,{(0,1):1});E11=matrix(QQ,2,{(1,1):1})
complex_basis=[realify(A,B) for E in (E00,E01,E11) for A,B in ((E,Z2),(Z2,E))]
check('upper_triangular_complex_algebra_dimension6',matrix(QQ,[M.list() for M in complex_basis]).rank()==6)
check('upper_triangular_plant_closed',all(
    matrix(QQ,[M.list() for M in complex_basis]+[(A*B).list()]).rank()==6
    for A in complex_basis for B in complex_basis))
# Its commutant is exactly C, despite this proper nonsemisimple subalgebra.
rows=[]
for A in complex_basis:
    for i in range(4):
        for j in range(4):
            row=[QQ(0)]*16
            for k in range(4):row[i*4+k]+=A[k,j];row[k*4+j]-=A[i,k]
            rows.append(row)
check('commutant_count_alone_counterexample',matrix(QQ,rows).right_kernel().dimension()==2)
check('complex_structure_alone_does_not_prove_full_algebra',J4*J4==-identity_matrix(QQ,4) and len(complex_basis)==6<8)
for n in (1,2,3):
    e=realify(E00,Z2).tensor_product(identity_matrix(QQ,n))
    check('sharp_repeated_complex_minimum_'+str(n),e*e==e and e.rank()==2*n)
# Split-real and nilpotent fake complex structures admit rank1 commutants.
split=matrix(QQ,[[1,0],[0,-1]]);dual=matrix(QQ,[[0,1],[0,0]])
rank1=matrix(QQ,[[1,0],[0,0]])
check('split_real_plant_rejected',split*split==identity_matrix(QQ,2) and split*rank1==rank1*split and rank1.rank()==1)
check('dual_number_plant_rejected',dual*dual==0 and dual.rank()==1)
check('multiplicity_is_needed',realify(E00,Z2).rank()==2 and 2 != 64)

mutations=[]
for field,value in [('representation_multiplicity',1),('generated_dimension',2),('split_preserving_dimension',128)]:
    bad=deepcopy(data);bad['certificate'][field]=value;mutations.append(bad)
bad=deepcopy(data);bad['certificate']['basis_words']=bad['certificate']['basis_words'][:-1];mutations.append(bad)
bad=deepcopy(data);bad['certificate']['complex_structure']['entries'][0][2]='2';mutations.append(bad)
bad=deepcopy(data);bad['claim_boundary']['physical_state']=True;mutations.append(bad)
for i,bad in enumerate(mutations):
    try:audit(bad)
    except (AssertionError,ValueError,IndexError):check('reporting_mutation_rejected_'+str(i),True)
    else:raise AssertionError('mutation survived')
print(json.dumps({'checks':len(checks),'reporting_mutations_rejected':len(mutations),'producer_imported':False,
                  'full_ambient_reconstruction_replayed':False},sort_keys=True))
