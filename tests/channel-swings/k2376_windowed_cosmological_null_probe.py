"""Exact finite observation operators and a labeled stored-coefficient consumer."""
from pathlib import Path
import json,hashlib,sys
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
checks={};controls={}
def ck(k,v):
    checks[k]=bool(v)
    assert v,k
def reject(k,v):
    controls[k]=bool(v)
    assert v,k
I=S.eye(4);U=I.row_join(I);a=S.Matrix([[1,0,0,0]]);b=2*a;D=S.diag(a,b);V=S.ones(1,2);F=V*D;H=U.col_join(F)
z=S.Matrix([1,0,0,0,-1,0,0,0])
ck('common_window_rank5',H.rank()==5)
reject('matched_windows_do_not_preserve_null',U*z==S.zeros(4,1) and (F*z)[0]==-1)
J=S.zeros(8,5)
for i in range(4):J[i,i]=1
J[0,0]+=1;J[0,4]-=1;J[4,0]=-1;J[4,4]=1
ck('explicit_right_inverse',H*J==S.eye(5))
C=S.Matrix([[2,1,0,0,0],[1,2,0,0,0],[0,0,3,0,0],[0,0,0,4,0],[0,0,0,0,5]])
ck('arbitrary_psd_covariance_lift',H*(J*C*J.T)*H.T==C)
c=a.row_join(-a);Ua=U.col_join(c);K=S.Matrix([[S.Rational(3,2),0,0,0,-S.Rational(1,2)]])
ck('minimal_extra_rank',H.rank()-U.rank()==1)
ck('contrast_repair_factorization',K*Ua==F)
Ha=Ua.col_join(F);n=(-K).row_join(S.ones(1,1));Sig=Ha*Ha.T
ck('repaired_exact_null',n*Ha==S.zeros(1,8) and n*Sig==S.zeros(1,6))
ck('noise_variance',(n*n.T)[0]==S.Rational(7,2))
wrong=S.Matrix([[-S.Rational(3,2),0,0,0,0,1]])
reject('omitted_contrast_false_rejection',(wrong*Sig*wrong.T)[0]==S.Rational(1,2))
Feq=a.row_join(a)
ck('constant_response_escape',a*U==Feq)
Ks=S.Matrix([[S.Rational(3,2),0,0,0]]);E=F-Ks*U;R=(-Ks).row_join(S.ones(1,1));N=S.eye(5)
ck('mismatch_power_identity',R*(H*H.T+N)*R.T-R*N*R.T==E*E.T)
# Physical joint covariance from epsilon=A*y+independent noise; displays cross term.
A=S.zeros(5,8);A[4,0]=1;Atotal=H+A
observed=Atotal*Atotal.T+N;noise=A*A.T+N
cross=E*A.T*R.T+R*A*E.T
ck('correlated_noise_full_identity',R*observed*R.T-R*noise*R.T==E*E.T+cross)
reject('correlation_cannot_be_ignored',cross!=S.zeros(1,1))
exc=S.zeros(8,8);exc[1,1]=1
ck('unexcited_mismatch_escape',E!=S.zeros(1,8) and E*exc*E.T==S.zeros(1,1))
vec=S.Matrix([1,2,3,4,5,6]);proj=vec-n.T*(n*vec)[0]/(n*n.T)[0]
ck('noise_projection_constraint',n*proj==S.zeros(1,1))
ck('noise_projection_cost',((vec-proj).T*(vec-proj))[0]==(n*vec)[0]**2/(n*n.T)[0])
# Actual stored decimal arithmetic, not an interval certificate for the inherited ODE.
p=ROOT/'lab/process/k2373-two-epoch-cosmological-observability.json';saved=json.loads(p.read_text())
g1,g2=[S.Matrix([[S.Rational(str(x)) for x in row['density_coefficients']]]) for row in saved['actual_rows'][:2]]
Fs=g1.row_join(g2);delta=(g1-g2)/2;ubar=(g1+g2)/2;cs=delta.row_join(-delta);Us=U.col_join(cs);ks=ubar.row_join(S.ones(1,1))
ck('stored_decimal_rank5',U.col_join(Fs).rank()==5)
ck('stored_decimal_weighted_contrast_repair',ks*Us==Fs)
z3=S.zeros(8,1);z3[2]=1;z3[6]=-1
reject('stored_decimal_hidden_mode_signal',U*z3==S.zeros(4,1) and (Fs*z3)[0]!=0)
report={'result_id':'K2376','checks':len(checks),'check_names':checks,'changed_input_controls':controls,'stored_decimal_signal':str((Fs*z3)[0]),'scope':'Exact finite linear theorem; stored decimal consumer not a new ODE or continuum certificate. No supplied physical survey windows.','dependencies':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()}}
text=json.dumps(report,indent=2,sort_keys=True)+'\n'
if '--write' in sys.argv:(ROOT/'lab/process/k2376-windowed-cosmological-null.json').write_text(text)
print(text)
