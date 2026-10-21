#!/usr/bin/env python3
"""Independent characteristic-space and endpoint flux checks, then real faults."""
import copy,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2];OUT='lab/process/k1890-preparation-evolution-boundary-incompatibility.json';COUNT={'exact':0,'report_pin':0}
def ck(ok,name,kind='exact'):
    if not ok:raise AssertionError('FAIL '+name)
    COUNT[kind]+=1

def mat(d):
    v={(i,j):s.Rational(x) for i,j,x in d['entries']}
    return s.Matrix(d.get('rows',16),d.get('columns',16),lambda i,j:v.get((i,j),0))
def baseline(cert):
    en=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text());ob=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text());witnesses=[]
    for j,(e,o,b) in enumerate(zip(en['blocks'],ob['blocks'],cert['blocks'])):
        H=mat(e['H']);A=mat(e['matrices'][0]);T=mat(o['T'][0]);F=H*A
        ck(all(H[:n,:n].det()>0 for n in range(1,17)),'actual H positive')
        spaces={l:s.Matrix.hstack(*(A-l*s.eye(16)).nullspace()) for l in [s.S.One,-s.S.One,s.Rational(1,24),s.Rational(-1,24)]}
        whole=s.Matrix.hstack(*spaces.values());ck(whole.det()!=0,'characteristic basis complete')
        for l,V in spaces.items():
            ck(A*V==l*V,'exact characteristic eigenvectors');ck(V.T*F*V==l*V.T*H*V,'signed energy form')
        P,M=spaces[s.S.One],spaces[-s.S.One];N=P.row_join(M)
        ck(N.shape==(16,12) and T*N==s.zeros(4,12),'kernel exact fast-space sum')
        ck(P.T*F*M==s.zeros(6),'fast plus/minus orthogonal')
        # Matching characteristic Gram factors gives an explicit isotropic graph.
        Pn=P*(P.T*H*P).cholesky().T.inv();Mn=M*(M.T*H*M).cholesky().T.inv();W=Pn+Mn
        ck(s.simplify(W.T*F*W)==s.zeros(6),'six-dimensional invisible reflection')
        SP,SM=spaces[s.Rational(1,24)],spaces[s.Rational(-1,24)]
        SPn=SP*(SP.T*H*SP/24).cholesky().T.inv();SMn=SM*(SM.T*H*SM/24).cholesky().T.inv();V=SPn+SMn;L=W.row_join(V)
        ck(s.simplify(L.T*F*L)==s.zeros(8),'eight-dimensional repaired reflection')
        ck(L.rank()==8 and (T*L).rank()==2,'optimal observed boundary rank')
        D=mat(ob['target_D'][0]);target=(D*T*V).columnspace();Y=s.Matrix.hstack(*target)
        ck(Y.rank()==2 and s.simplify(Y.T*D*Y)==s.zeros(2),'repaired target boundary isotropic')
        ck(s.simplify(Y.T*T*V)==s.zeros(2),'target boundary orthogonal to source observation boundary')
        ck((T*L).rank()==2 and s.simplify(T*A.inv()*L-24*D*T*L)==s.zeros(4,8),'source generator jet induces target boundary')
        x,w=s.symbols('x w',real=True,nonzero=True);a=(T*V)[:,0]
        f=s.cos(w*x)*a+s.I*s.sin(w*x)*D*a;y=s.diff(f,x)
        ck(s.simplify(-D*s.diff(f,x)/24+s.I*w*f/24)==s.zeros(4,1),'source-observed standing wave evolution')
        ck(s.simplify(-D*s.diff(y,x)/24+s.I*w*y/24)==s.zeros(4,1),'derivative target evolution')
        ck(s.simplify(y.subs(x,0).T.conjugate()*y.subs(x,0)-w*w*(f.subs(x,0).T.conjugate()*f.subs(x,0)))==s.zeros(1),'nonzero mode derivative norm')
        ck(mat(b['positive_invisible_witness']).T*F*mat(b['positive_invisible_witness'])==P[:,0].T*F*P[:,0],'stored positive witness')
        p,n=P[:,0],M[:,0];ck((p.T*F*p)[0]>0 and (n.T*F*n)[0]<0,'zero-observation nonzero evolution flux')
        witnesses.append((T,F,p,n))
        # Endpoint form diag(-F,F); periodic traces (v,v) cancel exactly.
        E=s.diag(-F,F);periodic=s.eye(16).col_join(s.eye(16));ck(periodic.T*E*periodic==s.zeros(16) and periodic.rank()==16,'periodic conservative repair')
        restricted=N.col_join(s.zeros(16,12)).row_join(s.zeros(16,12).col_join(N));ck((restricted.T*E*restricted).rank()==24,'paired zero-flux form nondegenerate')
        ck(b['kernel_inertia']==[6,6,0] and b['whole_inertia']==[8,8,0],'reported inertia','report_pin')
    expected={'zero_flux_trace':12,'largest_isotropic_zero_flux_trace':6,'required_separated_selfadjoint_trace':8,'minimum_observed_boundary_rank':2,'paired_endpoint_zero_flux_max_isotropic':12,'paired_endpoint_required':16,'minimum_total_observed_boundary_rank':4}
    ck(cert['dimensions']==expected,'reported dimensions','report_pin')
    for p,h in cert['inputs'].items():ck(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'input pin','report_pin')
    return witnesses[0]
def main():
    cert=json.loads((ROOT/OUT).read_text());T,F,p,n=baseline(cert);counts=COUNT.copy();faults=[]
    jobs=[('preparation implies energy zero',lambda:ck((p.T*F*p)[0]==0,'positive flux')),
          ('negative invisible sector omitted',lambda:ck((n.T*F*n)[0]>=0,'negative flux')),
          ('wrong endpoint orientation',lambda:ck(s.eye(16).col_join(s.eye(16)).T*s.diag(F,F)*s.eye(16).col_join(s.eye(16))==s.zeros(16),'periodic flux')),
          ('all observable traces forbidden repair',lambda:ck(8<=6,'isotropic dimension'))]
    for name,job in jobs:
        try:job()
        except AssertionError as e:
            if not str(e).startswith('FAIL '):raise
            faults.append(name)
        else:raise AssertionError('FAIL undetected '+name)
    bad=copy.deepcopy(cert);bad['dimensions']['minimum_observed_boundary_rank']=0
    try:baseline(bad)
    except AssertionError as e:
        if str(e)!='FAIL reported dimensions':raise
        faults.append('reported dimension')
    else:raise AssertionError('FAIL undetected report fault')
    print('PASS K1890 independent baseline',counts,'rejected',len(faults),'faults:',', '.join(faults))
if __name__=='__main__':main()
