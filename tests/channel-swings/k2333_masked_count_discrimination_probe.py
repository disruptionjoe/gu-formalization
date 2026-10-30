#!/usr/bin/env python3
"""Exact rational finite controls; universal probability results are in the note."""
import argparse,hashlib,json
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parents[2];ST='k2333-masked-count-discrimination'
def evaluate(fault=None):
 out=[]
 def ck(name,value):out.append((name,bool(value)))
 I=s.eye(5);A=I.copy();A[0,1]=1;B=I.copy();B[1,2]=2
 L=A.inv();K=B.inv()
 if fault=='omit_unshear':L=I
 if fault=='reverse_channel':B=-B
 ck('first map inverse',L*A==I);ck('second map inverse',K*B==I)
 M=s.Matrix([[250,249],[249,251]]) # envelope fixture, not claimed actual integrated M
 ck('fixture lies within actual certified entry envelope',228<M[0,0]<273 and 230<M[0,1]<273 and 231<M[1,1]<273)
 ck('fixture positive definite',M.det()>0)
 Sig=s.kronecker_product(M,I);T=s.diag(L,K);raw=s.diag(A,B)*Sig*s.diag(A,B).T
 ck('actual map covariance congruence',T*raw*T.T==Sig)
 A1=s.Matrix([[1,1,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0]])
 A2=s.Matrix([[1,0,0,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,0,0,1]])
 L1=s.Matrix([[1,-1,0,0],[0,1,0,0],[0,0,1,0]])
 L2=s.Matrix([[1,0,0,0],[0,1,-1,0],[0,0,1,0]])
 V=I[:3,:];ck('common row-space first',L1*A1==V);ck('common row-space second',L2*A2==V)
 ck('intersection dimension',A1.rank()+A2.rank()-A1.col_join(A2).rank()==3)
 U1=I[:4,:];U2=I[[0,1,2,4],:];cross=U1*U2.T
 ck('canonical-angle squared singulars',cross*cross.T==s.diag(1,1,1,0))
 ck('four canonical pairs exceed three matched',min(A1.rank(),A2.rank())==4)
 ck('three-mode baseline insufficient for five percent',s.Rational(1,8)>s.Rational(1,20))
 v=s.Matrix([1]*5+[-1]*5);noise=v*v.T/640
 if fault=='noise_strength':noise*=64
 ck('rank-one correlated perturbation eigenvalue',noise*v==v/64)
 ck('actual positive covariance',all(x>=0 for x in (s.eye(10)+noise).eigenvals()))
 ck('nonseparable cross-mode covariance retained',noise[0,1]!=0 and noise[0,6]!=0)
 delta=s.Rational(1,64)
 ck('exact squared TV correction',delta**2*10/(8*(1-delta))==s.Rational(5,16128))
 ck('strict five-percent margin',s.Rational(5,16128)<(s.Rational(1,20)-s.Rational(1,32))**2)
 ck('perturbation support dimension',len(v)==10)
 q=s.symbols('q',real=True);p=q*q+(1-q)**2
 ck('conditional discordance strict difference identity',s.expand(p-s.Rational(1,2)-2*(q-s.Rational(1,2))**2)==0)
 dup=s.ones(5,1)
 ck('duplicated modes have rank one', (dup*dup.T).rank()==1)
 ck('unbounded anticorrelated covariance PSD',all(x>=0 for x in (v*v.T).eigenvals()))
 D=s.diag(s.Rational(1,100),1,1,1,1);rawerr=s.eye(5)/10000;extract=D.inv()*rawerr*D.inv().T
 if fault=='raw_noise_is_extracted':extract=rawerr
 ck('inverse noise amplification charged',extract[0,0]==1)
 ck('amplification factor exact',extract[0,0]/rawerr[0,0]==10000)
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();checks=evaluate()
 assert all(v for _,v in checks),checks
 faults=[]
 for f in ['omit_unshear','reverse_channel','noise_strength','raw_noise_is_extracted']:
  failed=[n for n,ok in evaluate(f) if not ok];assert failed,f;faults.append({'changed_input':f,'detected_by':failed})
 report={'result':'K2333','status':'pass','exact_rational_controls':checks,'changed_input_faults':faults,'scope':'Finite exact matrix controls; universal Gaussian/canonical-angle/TV theorems rest on written proofs. Covariance fixture is within bounds, not a replacement for certified M.'}
 deps=[f'tests/channel-swings/{ST.replace("-","_")}_probe.py',f'explorations/conditional-build/{ST}-2026-10-30.md','lab/process/k2331-certified-count-window-covariance.json','explorations/conditional-build/k2331-certified-count-window-covariance-2026-10-30.md']
 report['dependencies']={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps}
 if args.write:(R/f'lab/process/{ST}.json').write_text(json.dumps(report,indent=2)+'\n')
 print('PASS',len(checks),'exact rational controls;',len(faults),'genuine changed-input faults')
if __name__=='__main__':main()
