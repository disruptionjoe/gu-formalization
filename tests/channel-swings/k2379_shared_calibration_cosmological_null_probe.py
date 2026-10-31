"""Exact covariance/calibration fixtures. --write saves deterministic evidence."""
from pathlib import Path
import json,hashlib,sys
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
checks={};controls={}
def ck(name,v,control=False):
    (controls if control else checks)[name]=bool(v)
    assert v,name
def solve(blocks,rho):
    ms=[];bs=[]
    for A,c,v,g,L in blocks:
        if A!=A.T or A.is_positive_semidefinite is not True:return False,None
        Ap=A.pinv()
        if A*Ap*c!=c or (c.T*Ap*c)[0]!=v:return False,None
        ms.append(A*L);bs.append(c-A*g)
    M=S.Matrix.vstack(*ms);b=S.Matrix.vstack(*bs);theta=M.pinv()*b
    return M*theta==b and (theta.T*theta)[0]<=rho**2,theta
one=S.ones(1,1);zero=S.zeros(1,1)
block=lambda c,v:(one,S.Matrix([c]),S.Rational(v),zero,one)
ck('one_shared_positive',solve([block(1,1),block(1,1)],1)[0])
ck('opposite_separate_fits',all(solve([block(x,1)],1)[0] for x in (1,-1)))
ck('opposite_shared_rejected',not solve([block(1,1),block(-1,1)],1)[0],True)
ck('positive_schur_debt_rejected',not solve([block(1,2)],100)[0],True)
ck('radius_rejected',not solve([block(2,4)],1)[0],True)
A=S.diag(1,0);c=S.Matrix([1,0]);g=S.Matrix([1,0]);L=S.Matrix([0,1])
ck('unexcited_gain_invisible',solve([(A,c,S.Integer(1),g,L)],0)[0])
ck('range_control',not solve([(A,S.Matrix([1,1]),S.Integer(1),g,L)],100)[0],True)
ck('indefinite_input_rejected',not solve([(S.diag(1,-1),c,S.Integer(1),g,L)],0)[0],True)
# Rank-deficient shared parameter map: minimum Euclidean norm, not one arbitrary solution.
ck('minimum_norm_solution',solve([(one,one,S.Integer(1),zero,S.Matrix([[1,1]]))],1)[1]==S.Matrix([S.Rational(1,2)]*2))
# Full joint graph covariance requires cross-block equations, not only block marginals.
A=S.eye(2);G=S.eye(2);C=S.Matrix([[1,S.Rational(1,4)],[0,1]]);V=C.T*C
Sig=A.row_join(C).col_join(C.T.row_join(V))
ck('cross_fixture_psd',Sig.is_positive_semidefinite is True)
# A simpler PSD counterexample with both same marginal deterministic graphs is impossible:
# zero marginal variance implies each full residual zero. Instead nonzero supplied cross
# covariance must be caught by PSD/range checks, not falsely called a valid covariance.
bad=S.Matrix([[1,0,1,S.Rational(1,4)],[0,1,0,1],[1,0,1,0],[S.Rational(1,4),1,0,1]])
ck('inconsistent_cross_data_not_psd',bad.det()<0,True)
# Fixed versus random calibration by direct enumeration, not assertion flipping.
samples=[(x,(2+t)*x) for x in (-1,1) for t in (-1,1)]
Avec=sum(S.Rational(p*p,4) for p,d in samples);cross=sum(S.Rational(p*d,4) for p,d in samples);v=sum(S.Rational(d*d,4) for p,d in samples)
ck('random_gain_covariance',(Avec,cross,v)==(1,2,5))
ck('random_gain_fixed_graph_rejected',v-cross**2/Avec==1,True)
# Means matter: covariance-zero constant offset does not satisfy the uncentered graph.
mean_M=S.Matrix([[0],[0],[1]]);mean_b=S.Matrix([0,0,2]);mean_theta=mean_M.pinv()*mean_b
ck('mean_row_radius_control',mean_M*mean_theta==mean_b and (mean_theta.T*mean_theta)[0]>1,True)
# Approximate residual exact identity at an arbitrary trial.
A=S.diag(2,3);g=S.Matrix([1,2]);c=A*g;v=(g.T*A*g)[0]+S.Rational(1,5);trial=S.Matrix([1,S.Rational(3,2)])
q=v-2*(trial.T*c)[0]+(trial.T*A*trial)[0]
ck('residual_decomposition',q==S.Rational(1,5)+((trial-g).T*A*(trial-g))[0])
ck('residual_trial_value',q==S.Rational(19,20))
# Stored response rows; synthetic covariance and synthetic common gain explicitly supplied.
p=ROOT/'lab/process/k2373-two-epoch-cosmological-observability.json';saved=json.loads(p.read_text());rows=[S.Matrix([S.Rational(str(x)) for x in row['density_coefficients']]) for row in saved['actual_rows']]
blocks=[]
for row in rows:
    c=S.Rational(11,10)*row;blocks.append((S.eye(4),c,(c.T*c)[0],row,row))
ok,theta=solve(blocks,S.Rational(1,5));ck('stored_common_gain_recovered',ok and theta==S.Matrix([S.Rational(1,10)]))
ck('stored_gain_radius_rejected',not solve(blocks,S.Rational(1,20))[0],True)
changed=list(blocks);row=rows[-1];c=S.Rational(9,10)*row;changed[-1]=(S.eye(4),c,(c.T*c)[0],row,row)
ck('stored_mode_dependent_gain_rejected',not solve(changed,S.Rational(1,5))[0],True)
report={'result_id':'K2379','checks':len(checks),'check_names':checks,'changed_input_controls':controls,'stored_gain':str(theta[0]),'scope':'Exact population covariance theorem and synthetic stored-decimal consumer, not finite-sample test or measured calibration.','dependencies':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()}}
text=json.dumps(report,sort_keys=True,indent=2)+'\n'
if '--write' in sys.argv:(ROOT/'lab/process/k2379-shared-calibration-cosmological-null.json').write_text(text)
print(text)
