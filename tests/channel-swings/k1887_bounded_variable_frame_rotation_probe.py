#!/usr/bin/env python3
"""Independent full-bank, nonlinear residual action and budget fault probes."""
import argparse,copy,hashlib,json,os
from pathlib import Path
import sympy as sp
ROOT=Path(os.environ.get('GU_ROOT',Path(__file__).resolve().parents[2]))
def insist(ok,label):
    if not ok:raise AssertionError('FAIL '+label)
def mat(d):
    a=sp.zeros(d.get('rows',16),d.get('columns',16))
    for i,j,x in d['entries']:a[i,j]=sp.Rational(x)
    return a
def zero(a):return all(sp.expand(x)==0 for x in a)
def read(n):return json.loads((ROOT/('lab/process/'+n+'.json')).read_text())
def objects():
    en=read('k1832-k77-common-energy-form');src=read('k1836-k77-differential-dirac-quotient');old=read('k1840-k77-conservative-variable-observation')
    D=[mat(x) for x in src['target_D']];J=D[0]*D[1]*D[2]
    return en,src,old,D,J

def bank(doc,fault=None):
    en,src,old,D,J=objects();v=sp.Symbol('v');count=0
    for ix,(er,sr,kr) in enumerate(zip(en['blocks'],src['blocks'],old['blocks'])):
        H=mat(er['H']);Hi=H.inv();A=[mat(x) for x in er['matrices']];T=[mat(x) for x in sr['T']];L=mat(er['J'])
        if T[0]*L!=J*T[0]:L=-L
        C0=(v*sp.eye(16)-A[0])*L;B0=(v*sp.eye(4)-D[0]/24)*J;S0=-T[0]*L
        y=sp.zeros(70,1)
        for i,x in doc['blocks'][ix]['dual_entries']:y[i]=sp.sympify(x,locals={'v':v})
        if fault=='dual_entry' and ix==0:y[7]+=1
        Y=sp.Matrix(4,16,list(y[6:,0]));B1=mat(kr['repairs'][0]['B'])
        for row in mat(kr['full_conservative_kernel']).tolist():
            U=sp.zeros(16);q=iter(row[:120])
            for i in range(16):
                for j in range(i+1,16):U[i,j]=next(q);U[j,i]=-U[i,j]
            C=Hi*U;S=sp.Matrix(4,16,row[126:]);B=sp.zeros(4);q=iter(row[120:126])
            for i in range(4):
                for j in range(i+1,4):B[i,j]=next(q);B[j,i]=-B[i,j]
            insist(H*C+C.T*H==sp.zeros(16),'conservation bank');count+=1
            insist(all(T[i]*C-B*T[i]+S*A[i]-D[i]*S/24==sp.zeros(4,16) for i in range(3)),'first-order bank');count+=1
            pair=sum(y[k]*row[120+k] for k in range(6))+sp.trace(Y.T*(S0*C+S*C0-B0*S))
            insist(sp.expand(pair)==0,'complete dual annihilator');count+=1
        b1=[B1[i,j] for i in range(4) for j in range(i+1,4)]
        insist(sp.expand(sum(y[k]*b1[k] for k in range(6))+sp.trace(Y.T*B1*S0)-v)==0,'forcing');count+=1
        norm=sp.trace(Y*Y.T);reported=sp.sympify(doc['blocks'][ix]['dual_norm_squared'],locals={'v':v})
        if fault=='norm_constant' and ix==0:reported+=sp.Rational(1,9216)
        insist(sp.expand(norm-reported)==0,'dual norm');count+=1
        insist(sp.trace(T[0]*T[0].T)==sp.Rational(doc['blocks'][ix]['T1_Frobenius_squared']),'leading norm');count+=1
        insist(B1.T*B1==sp.eye(4),'unit mass norm');count+=1
    return count

def operator_action(doc,fault=None):
    # Reconstruct QO and OP on spatially constant test fields. Their
    # difference yields the zeroth-order residual including time derivatives.
    en,src,old,D,J=objects();z=sp.Symbol('z');count=0
    for ix,(er,sr,kr) in enumerate(zip(en['blocks'],src['blocks'],old['blocks'])):
        v=sp.Rational(2,7);h=sp.Rational(3,5);R=sp.Rational(5,11)
        T=[mat(x) for x in sr['T']];A=[mat(x) for x in er['matrices']];L=mat(er['J'])
        if T[0]*L!=J*T[0]:L=-L
        C0=(v*sp.eye(16)-A[0])*L;B0=(v*sp.eye(4)-D[0]/24)*J;S0=-T[0]*L;B1=mat(kr['repairs'][0]['B'])
        Y=sp.zeros(4,16)
        for i,x in doc['blocks'][ix]['dual_entries']:
            if i>=6:Y[(i-6)//16,(i-6)%16]=sp.sympify(x,locals={'v':v})
        # Arbitrary exact jets exercise the product rule and nonlinear terms;
        # complete-bank eligibility is checked independently above.
        c=sp.Matrix(16,16,lambda i,j:sp.Rational((3*i+5*j)%7-3,13)*(1+z)+(1 if i==j else 0)*z*z)
        s=sp.Matrix(4,16,lambda i,j:sp.Rational((2*i+3*j)%11-5,17)*(2-z)+(1 if j==i else 0)*z*z)
        C=h*C0+c;S=h*S0+s;B=h*B0+R*B1
        OP=T[0]*C.diff(z)+S*C
        QO=-v*S.diff(z)+D[0]*S.diff(z)/24+B*S
        actual=OP-QO
        time=0 if fault=='omit_advection' else v
        derivsign=-1 if fault=='derivative_sign' else 1
        N=derivsign*(T[0]*c.diff(z)+(time*sp.eye(4)-D[0]/24)*s.diff(z))
        lin=h*(S0*c+s*C0-B0*s-R*B1*S0)
        nonlinear=(sp.zeros(4,16) if fault=='omit_sc' else s*c)-(sp.zeros(4,16) if fault=='omit_mass_s' else R*B1*s)
        insist(zero(actual-N-lin-nonlinear),'zeroth-order product action');count+=1
        flux=sp.trace(Y.T*(T[0]*c+(v*sp.eye(4)-D[0]/24)*s))
        # This equality is universal before imposing the bank; after imposing
        # it, the separately proved dual reduces the linear term to -hRv.
        insist(sp.expand(sp.trace(Y.T*actual)-flux.diff(z)-sp.trace(Y.T*(lin+nonlinear)))==0,'projected nonlinear action');count+=1
        C1=mat(kr['repairs'][0]['C']);S1=mat(kr['repairs'][0]['S'])
        actual_static=h*R*(S0*C1+S1*C0-B0*S1-B1*S0)+R*R*(S1*C1-B1*S1)
        forcing=R*v if fault=='omit_frequency' else h*R*v
        insist(sp.expand(sp.trace(Y.T*actual_static)+forcing)==0,'actual mass-repair projected defect');count+=1
    return count

def budgets(fault=None):
    count=0
    for r,a in [(sp.Rational(1,10),sp.Rational(2,7)),(2,3),(sp.Rational(1,10000),1)]:
        e=(sp.sqrt(r*r+4*a)-r)/2
        insist(sp.simplify(e*(e+r)-a)==0 and e>0,'quadratic floor');count+=1
        ewrong=(sp.sqrt(r*r+4*a)+r)/2
        insist(sp.simplify(ewrong*(ewrong+r)-a)!=0,'wrong root control');count+=1
    # Exact integrated polynomial test: nonlinear integral plus boundary flux
    # equals constant forcing. Omitting endpoint flux must fail locally.
    z=sp.Symbol('z');g=sp.Rational(7,3);nonlinear=z*z+2*z;lam=g*z-z**3/3-z*z
    length=sp.Rational(5,2);left=lam.subs(z,length)-lam.subs(z,0)
    if fault=='omit_boundary_flux':left=0
    insist(sp.simplify(left+sp.integrate(nonlinear,(z,0,length))-g*length)==0,'finite interval flux');count+=1
    # Necessity does not assert that either the minimum branch or a lift exists.
    for h,v,R in [(0,2,3),(1,0,3),(1,2,0)]:insist(h*v*R==0,'degenerate contrary control');count+=1
    return count

def reporting(doc):
    truths=['fixed_pointwise_bank','bounded_whole_line_or_periodic','canonical_base','variable_frame_coefficients_allowed','no_bounded_differentiable_mass_branch','nonlinear_distance_is_necessary_only']
    falses=['local_lifts_excluded','all_rotating_lifts_excluded','square_root_branch_constructed','native_GU_identification','approximate_first_order_bank_covered']
    for k in truths:insist(doc['scope'][k] is True,'scope '+k)
    for k in falses:insist(doc['scope'][k] is False,'scope '+k)
    insist(doc['identities']['h']=='omega/2','frequency normalization')
    for p,d in doc['inputs'].items():insist(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==d,'input pin')
    return len(truths)+len(falses)+1+len(doc['inputs'])
def rejected(fn,label):
    try:fn()
    except AssertionError as exc:insist(str(exc).startswith('FAIL '),'explicit assertion rejection');print('DETECTED',label)
    else:raise AssertionError('FAIL missed '+label)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--certificate',type=Path);a=p.parse_args();doc=json.loads((a.certificate or ROOT/'lab/process/k1887-bounded-variable-frame-rotation.json').read_text())
    bc=bank(doc);oc=operator_action(doc);nc=budgets();rc=reporting(doc)
    print('BASELINE PASS',bc,oc,nc,rc)
    for f in ['dual_entry','norm_constant']:rejected(lambda f=f:bank(doc,f),'matrix '+f)
    for f in ['omit_advection','derivative_sign','omit_sc','omit_mass_s','omit_frequency']:rejected(lambda f=f:operator_action(doc,f),'operator '+f)
    rejected(lambda:budgets('omit_boundary_flux'),'mathematical boundary flux')
    for key in ['bounded_whole_line_or_periodic','canonical_base','all_rotating_lifts_excluded','square_root_branch_constructed','native_GU_identification']:
        bad=copy.deepcopy(doc);bad['scope'][key]=not bad['scope'][key];rejected(lambda bad=bad:reporting(bad),'report '+key)
    bad=copy.deepcopy(doc);bad['inputs'][next(iter(bad['inputs']))]='0'*64;rejected(lambda:reporting(bad),'report pin')
    print('PASS K1887 probe',bc,'bank/matrix;',oc,'operator;',nc,'budget;',rc,'report/pins; 8 mathematical faults; 6 report faults')
