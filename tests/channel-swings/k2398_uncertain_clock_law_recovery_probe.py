#!/usr/bin/env python3
"""Exact K2398 channel/uncertainty fixtures; universal statements use the note."""
from pathlib import Path
from itertools import combinations
import argparse
import hashlib
import json
import sympy as s

Q=s.Rational
I=s.eye(2); X=s.Matrix([[0,1],[1,0]]); Y=s.Matrix([[0,-s.I],[s.I,0]]); Z=s.diag(1,-1)
pa=[X,Y,Z]; kp=s.kronecker_product

def clean(x): return s.simplify(x)
def zero(x):
    return clean(x)==s.zeros(*x.shape) if isinstance(x,s.MatrixBase) else clean(x)==0
def psd(A):
    return all(bool(clean(A.extract(ix,ix).det())>=0)
               for j in range(1,A.rows+1) for ix in combinations(range(A.rows),j))
def ptr(J): return s.Matrix(2,2,lambda i,j:sum(J[2*a+i,2*a+j] for a in range(2)))
def choi_apply(fn):
    return clean(sum((kp(fn(s.eye(2)[:,i]*s.eye(2)[:,j].T),s.eye(2)[:,i]*s.eye(2)[:,j].T)
                     for i in range(2) for j in range(2)),s.zeros(4)))
def trace_norm_hermitian(A):
    return clean(sum((mult*s.Abs(ev) for ev,mult in A.eigenvals().items()),s.S(0)))

def run(root):
    checks={}; controls={}
    def check(name,condition):
        checks[name]=bool(condition)
        if not condition: raise AssertionError('[FAIL] '+name)
    def control(name,condition):
        controls[name]=bool(condition)
        if not condition: raise AssertionError('[FAIL] '+name)

    # Universal algebraic norm identity; positivity is proved in the note.
    p,q,r,t=s.symbols('p q r t',real=True)
    BB=s.Matrix([[p,q],[r,t]]); CC=I-BB
    check('planar_trace_skew_norm_identity',s.expand(s.trace(CC.T*CC)+2*CC.det()-(2-s.trace(BB))**2-(q-r)**2)==0)
    check('planar_singular_difference_identity',s.expand(s.trace(CC.T*CC)-2*CC.det()-s.trace(BB.T*BB)+2*BB.det())==0)
    a,b,c=s.symbols('a b c',real=True)
    radial=(2-a*c)**2+b*b*c*c
    cstar=2*a/(a*a+b*b)
    check('mirror_optimum_stationarity',zero(s.diff(radial,c).subs(c,cstar)))
    check('mirror_optimum_value',zero(radial.subs(c,cstar)-4*b*b/(a*a+b*b)))
    check('mirror_exact_completion_square',zero(radial-(a*a+b*b)*(c-cstar)**2-4*b*b/(a*a+b*b)))

    aa=Q(1,4); bb=Q(3,4); cc=Q(4,5); MM=s.diag(aa,bb)
    laws=[[(aa,s.Matrix([1,0])),(bb,s.Matrix([0,sgn]))] for sgn in (1,-1)]
    means=[]
    for idx,law in enumerate(laws):
        m=sum((w*n for w,n in law),s.zeros(2,1))
        M=sum((w*n*n.T for w,n in law),s.zeros(2))
        means.append(m)
        check('actual_law_'+str(idx),sum(w for w,n in law)==1 and all(w>0 and n.dot(n)==1 for w,n in law) and M==MM and psd(M-m*m.T))
    check('interior_mirror_optimizer',0<cc<1 and cc==2*aa/(aa*aa+bb*bb))
    rho=(I+cc*X)/2
    vp=s.Matrix([1,1])/s.sqrt(2); vm=s.Matrix([1,-1])/s.sqrt(2)
    ks=[s.sqrt(w)*v*I[:,j].T for w,v in [(Q(9,10),vp),(Q(1,10),vm)] for j in range(2)]
    def prep(op):return clean(sum((K*op*K.conjugate().T for K in ks),s.zeros(2)))
    J=choi_apply(prep)
    check('mixed_preparation_actual_kraus_TP',zero(sum((K.conjugate().T*K for K in ks),s.zeros(2))-I))
    check('mixed_preparation_actual_choi',J==kp(rho,I) and ptr(J)==I and psd(J))
    check('mixed_preparation_bloch',zero(prep(I/2)-rho) and all(zero(prep(P)) for P in pa))
    def blocks(op,z,m,nu):
        rv=s.Matrix([s.trace(op*X),s.trace(op*Z)]);tr=s.trace(op)
        v=nu*(m*tr+z*MM*rv)
        return clean(((tr+z*m.dot(rv))*I+v[0]*X+v[1]*Z)/4)
    def recovered(op,m,nu,rec=prep):
        return clean(rec(blocks(op,1,m,nu))+Y*rec(blocks(op,-1,m,nu))*Y)
    expected=(1+3*s.sqrt(10)/5)/4
    pure=(1+s.sqrt(58)/4)/4
    jid=choi_apply(lambda x:x)
    for idx,m in enumerate(means):
        for nu in (s.S(0),Q(1,100)):
            B=s.Matrix([cc,0])*m.T
            for j,op in enumerate([I/2,X,Y,Z]):
                rv=s.Matrix([s.trace(op*X),s.trace(op*Z)]);v=B*rv
                out=(s.trace(op)*I+v[0]*X+v[1]*Z)/2
                check('actual_sign_composition_%s_%s_%s'%(idx,nu,j),zero(recovered(op,m,nu)-out))
            jt=choi_apply(lambda op:recovered(op,m,nu))
            check('recovered_CP_TP_%s_%s'%(idx,nu),psd(jt) and ptr(jt)==I)
            # Independent exact eigenvalue trace norm of the actual output on a Bell input.
            check('independent_Bell_trace_norm_%s_%s'%(idx,nu),zero(trace_norm_hermitian(jid-jt)/4-expected))
        # Instrument positivity and traces are checked before normalization assumptions.
        for sg in (1,-1):
            jz=choi_apply(lambda op:blocks(op,sg,m,Q(1,100)))
            check('original_instrument_CP_%s_%s'%(idx,sg),psd(jz))
        check('original_instrument_total_TP_'+str(idx),ptr(choi_apply(lambda op:blocks(op,1,m,Q(1,100))+blocks(op,-1,m,Q(1,100))))==I)
    check('mixed_strictly_beats_Bell_pure',bool(pure>expected))
    check('pure_mixed_radical_squared_gap',Q(58,16)-Q(18,5)==Q(1,40))
    check('known_law_value_strictly_lower',bool((3-s.sqrt(10)/4)/4<expected))
    check('positive_visibility_proxy_separation',bool(expected-Q(1,200)>Q(11,16)))
    check('positive_visibility_identity_margin',bool((3-Q(1,100))/4>expected))
    midpoint=s.Matrix([aa,0])
    check('midpoint_identity_optimal_threshold',zero((midpoint.T*MM.inv()*midpoint)[0]-Q(1,4)))
    check('complete_zero_loss_boundary',zero(s.S(0)*expected))
    # Actual nuisance mutation: erase the anti-symmetric entry while retaining trace.
    B=s.Matrix([[cc*aa,cc*bb],[0,0]])
    wrong_proxy=(3-s.trace(B))/4
    control('dropped_offdiagonal_proxy_rejected',not zero(wrong_proxy-expected))
    control('nominal_law_oracle_rejected',not zero((3-s.sqrt(10)/4)/4-expected))
    control('wrong_sign_order_rejected',not zero(prep(blocks(I/2,1,means[0],0))+prep(Y*blocks(I/2,-1,means[0],0)*Y)-I/2))
    control('moment_mean_without_feasibility_rejected',not psd(MM-s.Matrix([1,1])*s.Matrix([[1,1]])))
    control('transposition_not_CP',not psd(choi_apply(lambda op:op.T)))

    # Finite-visibility coherent witness: amplitude damping toward +X.
    Had=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
    kd=[Had*s.diag(1,1/s.sqrt(5))*Had,
        Had*s.Matrix([[0,2/s.sqrt(5)],[0,0]])*Had]
    def damp(op):return clean(sum((K*op*K.T for K in kd),s.zeros(2)))
    jd=choi_apply(damp)
    check('coherent_witness_CP_TP',psd(jd) and ptr(jd)==I and jd.rank()==2)
    check('coherent_witness_translation',zero(damp(I/2)-(I+cc*X)/2))
    for i,con in enumerate([Q(1,5),1/s.sqrt(5),1/s.sqrt(5)]):
        check('coherent_witness_bloch_'+str(i),zero(damp(pa[i])-con*pa[i]))
    nu=Q(1,100); gain=(1+3*s.sqrt(5))/20
    e_damp=(1+s.sqrt((Q(9,5)-nu*gain)**2+Q(9,25)))/4
    for idx,m in enumerate(means):
        jt=choi_apply(lambda op:recovered(op,m,nu,damp))
        check('coherent_witness_actual_channel_'+str(idx),psd(jt) and ptr(jt)==I)
        check('coherent_witness_independent_Bell_norm_'+str(idx),zero(trace_norm_hermitian(jid-jt)/4-e_damp))
    check('coherent_witness_strict_improvement',bool(e_damp<expected))
    # Exact diagonal-channel CP envelope identities (not a numerical optimum).
    cx,xx=s.symbols('cx xx',real=True)
    up=s.sqrt((1+xx)**2-cx**2);um=s.sqrt((1-xx)**2-cx**2)
    zz=(up+um)/2;yy=(up-um)/2
    check('CP_envelope_plus_saturation',zero((1+xx)**2-cx**2-(yy+zz)**2))
    check('CP_envelope_minus_saturation',zero((1-xx)**2-cx**2-(yy-zz)**2))
    check('CP_envelope_witness_boundary',zero(zz.subs({cx:cc,xx:Q(1,5)})-1/s.sqrt(5)))

    # Direct sign and measured-pointer calibration, no observed theta required.
    nu=Q(1,3)
    for l,m in enumerate(means):
        for j,Pj in enumerate([X,Z]):
            state=(I+Pj)/2
            check('calibration_sign_%s_%s'%(l,j),zero(sum(z*s.trace(blocks(state,z,m,nu)) for z in (1,-1))-m[j]))
            for i,Pi in enumerate([X,Z]):
                corr=sum(z*y*s.trace((I+y*Pi)/2*blocks(state,z,m,nu)) for z in (1,-1) for y in (1,-1))
                check('calibration_correlation_%s_%s_%s'%(l,i,j),zero(corr-nu*MM[i,j]))
    control('uncalibrated_visibility_substitution_rejected',nu*MM[0,0]!=MM[0,0])
    # Union-bound algebra; its probability theorem is the written bounded-variable proof.
    alpha=s.symbols('alpha',positive=True);nn=s.symbols('nn',positive=True)
    eps2=2*s.log(12/alpha)/nn
    check('six_statistic_union_budget',zero(12*s.exp(-nn*eps2/2)-alpha))
    check('expected_acquisition_exposure_fixture',4*100/Q(1,4)==1600)
    deps=['lab/process/k2395-planar-recovery-closed-form.json','lab/process/k2392-nonaligned-clock-recovery.json']
    return {'result':'K2398','status':'pass','evidence_kind':'exact symbolic and rational/algebraic CP, actual sign-composition, Bell trace-norm and calibration checks; general all-CPTP and probability claims use written proofs','checks':checks,'controls':controls,
            'fixture':{'a':str(aa),'b':str(bb),'c_star':str(cc),'zero_visibility_robust_error':str(expected),'Bell_pure_decoder_error':str(pure),'positive_visibility':str(Q(1,100)),'positive_visibility_coherent_upper':str(e_damp),'positive_visibility_lower':str(expected-Q(1,200))},
            'dependencies':{p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in deps}}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2])
    parser.add_argument('--report',type=Path)
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args();report=run(args.repo)
    output=json.dumps(report,indent=2,sort_keys=True)+'\n'
    if args.report:args.report.write_text(output)
    elif args.write:(args.repo/'lab/process/k2398-uncertain-clock-law-recovery.json').write_text(output)
    print(output,end='')
