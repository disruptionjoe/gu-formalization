#!/usr/bin/env python3
"""Separate spectral-resolvent, finite CAR and covariance failure controls."""
import copy,hashlib,json
import sympy as s
from k1892_causal_observation_algebra import ROOT,OUT,INPUTS,mat

def clean(M):return M.applyfunc(lambda x:s.cancel(s.expand(x)))

def verify(report,fault=None):
    n=0
    def ck(name,b):
        nonlocal n
        if not b:raise AssertionError('FAIL '+name)
        n+=1
    en,ob,rep,_=[json.loads((ROOT/p).read_text()) for p in INPUTS];D=list(map(mat,ob['target_D']));alpha=s.Rational(report['alpha'])
    for j,(e,o,r) in enumerate(zip(en['blocks'],ob['blocks'],rep['blocks'])):
        H=mat(e['H']);hi=H.inv(method="DM");A=list(map(mat,e['matrices']));T=list(map(mat,o['T']));C,B,S=[mat(r['repairs'][0][k]) for k in ['C','B','S']]
        for xi,R in [((1,2,0),1),((2,-1,1),0)]:
            O=s.I*sum((xi[a]*T[a] for a in range(3)),s.zeros(4,16))+R*S;P=s.I*sum((xi[a]*A[a] for a in range(3)),s.zeros(16))+R*C;Q=s.I*sum((xi[a]*D[a]/24 for a in range(3)),s.zeros(4))+R*B
            kap=alpha*(sum(v*v for v in xi)+576*R*R);od=hi*O.conjugate().T
            den2=kap*kap if fault=='wrong_normalization' else kap
            ck('CAR_isometry',clean(O*od/den2)==s.eye(4))
            ck('retarded_Laplace_transfer',clean(O*(2*s.eye(16)+P).inv(method="DM")-(2*s.eye(4)+Q).inv(method="DM")*O)==s.zeros(4,16))
            ck('normalized_covariance_resolvent',clean(O*(2*s.eye(16)+P).inv(method="DM")*od/den2)==(2*s.eye(4)+Q).inv(method="DM"))
            projection=clean(od*O/kap)
            ck('reducing_visible_projection',clean(projection*P-P*projection)==s.zeros(16) and clean(projection*projection-projection)==s.zeros(16))
            # Actual target density0.2 and hidden density0.7: spectral union, no state selection.
            state=clean(s.Rational(1,5)*projection+s.Rational(7,10)*(s.eye(16)-projection))
            ck('state_compression',clean(O*state*od/den2)==s.eye(4)/5)
            ck('state_extension_polynomial',clean((state-s.eye(16)/5)*(state-7*s.eye(16)/10))==s.zeros(16))
        # A local scalar phase potential commutes in principal order but leaves a gradient defect.
        for direction in [T[0],T[1],T[2]]:
            ck('scalar_gradient_defect',direction*hi*direction.T==alpha*s.eye(4) and direction.rank()==4)
        wr=report['leakage_witnesses'][j];rfast=mat(wr['fast_vector']);leak=mat(wr['leak']);norm=s.Rational(wr['energy_norm_squared'])
        if fault=='fast_speed':speed=s.Rational(1,24)
        else:speed=s.S.One
        ck('fast_resolvent',clean(leak*(2*s.eye(16)+s.I*A[0]).inv(method="DM")-leak/(2+s.I*speed))==s.zeros(4,16))
        ck('fast_nonzero_covariance',leak*hi*leak.T==s.diag(norm,0,0,0) and norm>0)
        ck('actual_invisible_fast',(T[0]*rfast)==s.zeros(4,1))
        W=mat(wr['protected_local_potential']);Z=mat(wr['local_hidden_basis'])
        ck('protected_local_skew',H*W+W.T*H==s.zeros(16) and W.rank()==2)
        ck('protected_local_output',all(t*W==s.zeros(4,16) for t in T) and S*W==s.zeros(4,16) and Z.cols==4)
        ck('protected_local_range',Z.row_join(W).rank()==4)
    # Independent two-mode Jordan-Wigner representation of the CAR algebra.
    a=s.Matrix([[0,1],[0,0]]);z=s.diag(1,-1);a1=s.kronecker_product(a,s.eye(2));a2=s.kronecker_product(s.eye(2) if fault=='ungraded_tensor' else z,a)
    ck('CAR_offdiagonal',a1*a2.T+a2.T*a1==s.zeros(4) and a1*a2+a2*a1==s.zeros(4))
    ck('CAR_diagonal',a1*a1.T+a1.T*a1==s.eye(4) and a2*a2.T+a2.T*a2==s.eye(4))
    N1=a1.T*a1;N2=a2.T*a2;ck('even_commutation',N1*N2==N2*N1)
    b=(a1+a2)/s.sqrt(2);Nb=b.T*b
    ck('overlap_matters',N1*Nb-Nb*N1!=s.zeros(4))
    # Flux speed from every sphere direction is fixed algebraically, not a numerical mesh.
    nx,ny,nz=s.symbols('nx ny nz',real=True);Ds=nx*D[0]+ny*D[1]+nz*D[2]
    ck('target_speed_polynomial',Ds*Ds==(nx*nx+ny*ny+nz*nz)*s.eye(4))
    ck('reported_speed',s.Rational(report['causal_speed'])==s.Rational(1,24))
    for p,h in report['inputs'].items():ck('input_pin',hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h)
    return n
if __name__=='__main__':
    report=json.loads((ROOT/OUT).read_text());n=verify(report);caught=[]
    for fault in ['wrong_normalization','fast_speed','ungraded_tensor']:
        try:verify(report,fault)
        except AssertionError as e:assert str(e).startswith('FAIL ');caught.append(str(e))
        else:raise AssertionError('FAIL undetected '+fault)
    bad=copy.deepcopy(report);bad['causal_speed']='1'
    try:verify(bad)
    except AssertionError as e:assert str(e).startswith('FAIL ');caught.append(str(e))
    else:raise AssertionError('FAIL undetected speed report')
    print('PASS K1892 probe',n,'exact/resolvent/CAR/pin checks;',len(caught),'faults:',caught)
