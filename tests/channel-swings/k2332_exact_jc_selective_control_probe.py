#!/usr/bin/env python3
"""Exact polynomial controls and finite 60-digit full JC matrix/synthesis controls."""
import argparse,copy,hashlib,json
from pathlib import Path
import sympy as s
import mpmath as m
R=Path(__file__).resolve().parents[2];ST='k2332-exact-jc-selective-control';m.mp.dps=60
BASE={'cross':True,'tone':1,'reference':True,'clock':True,'phase':1,'target_phase':True}
def diag(v):return m.diag(v)
def matrices(N,D,g,c):
    labels=[(0,'-')]+[(n,b) for n in range(1,N+1) for b in ['-','+']];ix={z:i for i,z in enumerate(labels)};dim=len(labels)
    U=m.eye(dim);Hb=m.zeros(dim);B=m.zeros(dim);ener=[];theta=[m.mpf(0)]+[m.atan(2*g*m.sqrt(n)/D)/2 for n in range(1,N+1)]
    for n in range(1,N+1):
        i,j=ix[n,'-'],ix[n,'+'];co,si=m.cos(theta[n]),m.sin(theta[n]);U[i,i]=co;U[i,j]=si;U[j,i]=-si;U[j,j]=co
        Hb[i,j]=Hb[j,i]=g*m.sqrt(n);Hb[j,j]=D
        fac=m.sqrt(N-n+1) if c['reference'] else 1
        B[ix[n-1,'-'],i]=m.sqrt(n)*fac
        if n>1:B[ix[n-1,'+'],j]=m.sqrt(n-1)*fac
    H=U.T*Hb*U;Bd=U.T*B*U
    if not c['cross']:
        for i,(n,b) in enumerate(labels):
            for j,(q,a) in enumerate(labels):
                if b!=a:Bd[i,j]=0
    E=[m.mpf(0)]+[ (D+(-1 if b=='-' else 1)*m.sqrt(D*D+4*g*g*n))/2 for n,b in labels[1:]]
    return labels,ix,diag(E),Bd,U,Hb,B,diag([n for n,b in labels])
def norm(A):return m.norm(A) # Frobenius, conservative over operator norm

def actual_pulse(H,B,L,omega,u,phase,t0,tau,c):
    om=c['tone']*omega;ph=c['phase']*phase
    C=u*m.exp(1j*ph)*B+u*m.exp(-1j*ph)*B.T
    tstart=t0 if c['clock'] else m.mpf(0);tend=tstart+tau
    # Physical clock reset when clock=False: same duration, restarted carrier phase.
    return m.expm(-1j*om*L*tend)*m.expm(-1j*(H-om*L+C)*tau)*m.expm(1j*om*L*tstart)
def evaluate(c):
    exact=[];num=[]
    def ck(n,v):exact.append((n,bool(v)))
    def cn(n,v):num.append((n,bool(v)))
    x,D,g=s.symbols('x D g',positive=True);E=(D-s.sqrt(D*D+4*g*g*x))/2
    ck('lower curvature giving all-n separation',s.simplify(s.diff(E,x,2)-2*g**4/(D*D+4*g*g*x)**s.Rational(3,2))==0)
    z=s.symbols('z');A,B,lam,eps=s.symbols('A B lam eps',positive=True);disc=eps**2-4*A*lam*B
    for root in [(eps-s.sqrt(disc))/(2*A),(eps+s.sqrt(disc))/(2*A)]:ck('amplitude endpoints solve actual cost polynomial',s.simplify(A*root**2-eps*root+lam*B)==0)
    ck('positive cost optimizer stationary',s.simplify(s.diff(A*z+lam*B/z,z).subs(z,s.sqrt(lam*B/A)))==0)
    ck('positive-amplitude minimum identity',s.simplify((A*z+lam*B/z).subs(z,s.sqrt(lam*B/A))-2*s.sqrt(A*lam*B))==0)
    for N in [1,2,3,5]:
        D=m.mpf(2);g=m.mpf('0.7');labels,ix,H,Bd,U,Hb,Bbare,L=matrices(N,D,g,c)
        cn(f'N{N} complete dressed diagonalization',norm(U.T*Hb*U-H)<m.mpf('1e-50'))
        # Independently compare the actual physical bare operator, regardless of mutated assumption.
        trueB=m.zeros(len(labels))
        for n in range(1,N+1):
            trueB[ix[n-1,'-'],ix[n,'-']]=m.sqrt(n*(N-n+1))
            if n>1:trueB[ix[n-1,'+'],ix[n,'+']]=m.sqrt((n-1)*(N-n+1))
        cn(f'N{N} full bare hopping conjugation',norm(Bd-U.T*trueB*U)<m.mpf('1e-50'))
        formula=m.zeros(len(labels))
        for n in range(1,N+1):
            th=m.atan(2*g*m.sqrt(n)/D)/2;pr=m.atan(2*g*m.sqrt(n-1)/D)/2
            co,si,cp,sp=m.cos(th),m.sin(th),m.cos(pr),m.sin(pr);q=m.sqrt(N-n+1)
            formula[ix[n-1,'-'],ix[n,'-']]=q*(m.sqrt(n)*co*cp+m.sqrt(n-1)*si*sp)
            formula[ix[n-1,'-'],ix[n,'+']]=q*(m.sqrt(n)*si*cp-m.sqrt(n-1)*co*sp)
            if n>1:
                formula[ix[n-1,'+'],ix[n,'-']]=q*(m.sqrt(n)*co*sp-m.sqrt(n-1)*si*cp)
                formula[ix[n-1,'+'],ix[n,'+']]=q*(m.sqrt(n)*si*sp+m.sqrt(n-1)*co*cp)
        cn(f'N{N} manuscript four-block formulas match physical transform',norm(formula-U.T*trueB*U)<m.mpf('1e-50'))
        gap=2*g**4/(D*D+4*g*g*N)**m.mpf('1.5')
        for k in range(1,N+1):
            om=H[ix[k,'-'],ix[k,'-']]-H[ix[k-1,'-'],ix[k-1,'-']]
            det=[]
            for n in range(1,N+1):
                for b in ['-','+']:
                    for a in ['-','+']:
                        if (n-1,a) not in ix:continue
                        if a==b=='-' and n==k:continue
                        det.append(abs(H[ix[n,b],ix[n,b]]-H[ix[n-1,a],ix[n-1,a]]-om))
            cn(f'N{N} tone{k} all-branch detuning',min(det)>gap)
            cn(f'N{N} edge{k} positive lower coupling',Bd[ix[k-1,'-'],ix[k,'-']]>=m.sqrt(N)/2)
    # Full complex target, fixed N; actual exact finite matrix propagators including upper states.
    N=3;D=m.mpf(2);g=m.mpf('0.7');labels,ix,H,Bd,U,Hb,Bbare,L=matrices(N,D,g,c);J=m.mpf('0.000001')
    target=([m.mpc(0),m.mpc(0,1),m.mpc(0),m.mpc(1)] if c.get('sparse') else [m.mpc(1),m.mpc(0,2),m.mpc(-1,1),m.mpc(2,-1)]);scale=m.sqrt(sum(abs(v)**2 for v in target));target=[v/scale for v in target]
    angles=[m.atan2(m.sqrt(sum(abs(target[n])**2 for n in range(k,N+1))),abs(target[k-1])) for k in range(1,N+1)];T=sum(angles)/J
    tilde=[m.exp(1j*H[ix[n,'-'],ix[n,'-']]*T)*target[n] if c['target_phase'] else target[n] for n in range(N+1)]
    # Global phase makes first amplitude positive without changing physical state.
    globalphase=m.exp(-1j*m.arg(tilde[0]));tilde=[globalphase*x for x in tilde];goal=m.zeros(len(labels),1)
    for n in range(N+1):goal[ix[n,'-']]=globalphase*target[n]
    ideal=m.zeros(len(labels),1);ideal[0]=1;actual=ideal.copy();t0=m.mpf(0);errsum=m.mpf(0);tol=m.mpf('0.005')
    for k,angle in enumerate(angles,1):
        i,j=ix[k-1,'-'],ix[k,'-'];phase=m.arg(ideal[i])-m.arg(tilde[k])-m.pi/2
        om=H[j,j]-H[i,i];b=Bd[i,j];u=J/b;tau=angle/J
        sel=m.zeros(len(labels));sel[i,j]=J*m.exp(1j*phase);sel[j,i]=J*m.exp(-1j*phase)
        prop=actual_pulse(H,Bd,L,om,u,phase,t0,tau,c);actual=prop*actual;ideal=m.expm(-1j*sel*tau)*ideal;t0+=tau
    intended=diag([m.exp(-1j*H[i,i]*T) for i in range(len(labels))])*ideal
    cn('constructive ideal target with complete final phases',norm(intended-goal)<m.mpf('1e-45'))
    cn('full microscopic pulse sequence hits target within finite tolerance',norm(actual-goal)<tol)
    cn('actual upper leakage remains below finite tolerance',sum(abs(actual[i])**2 for i,(n,b) in enumerate(labels) if b=='+')<tol**2)
    # Exact spectral degeneracy and physical rates differ across shells.
    cn('same-edge cross-shell frequencies coincide',H[ix[1,'-'],ix[1,'-']]==(D-m.sqrt(D*D+4*g*g))/2)
    l2,i2,h2,b2,*_=matrices(2,D,g,c)
    cn('actual cross-shell frequency degeneracy',abs((h2[i2[1,'-'],i2[1,'-']]-h2[0,0])-(H[ix[1,'-'],ix[1,'-']]-H[0,0]))<m.mpf('1e-50'))
    cn('actual cross-shell resonant rate differs',abs(Bd[0,ix[1,'-']]-b2[0,i2[1,'-']])>m.mpf('0.01'))
    delta=2*g**4/(D*D+4*g*g*N)**m.mpf('1.5')
    Ac=8*N*(N+1)/(delta*m.sqrt(N))*(1+m.pi/2*(3+2*m.sqrt(N)));Bc=N*m.pi/2
    epsilon=m.mpf('0.1');lam=epsilon**2/(16*Ac*Bc);Jopt=m.sqrt(lam*Bc/Ac)
    cn('actual N3 sufficient control-noise window nonempty',Ac*Jopt+lam*Bc/Jopt<epsilon)
    cn('actual N3 minimum equals half tolerance',abs(Ac*Jopt+lam*Bc/Jopt-epsilon/2)<m.mpf('1e-50'))
    evidence={'finite_N3_sequence_state_error':str(norm(actual-goal)),'J':str(J),'duration':str(T),'finite_tolerance':str(tol),'A_N':str(Ac),'B_N':str(Bc),'constructed_noise_lambda':str(lam),'constructed_Jopt':str(Jopt),'note':'finite60digit controls; not interval or all-N proof'}
    return exact,num,evidence

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args()
    ex,nu,ev=evaluate(BASE)
    for n,ok in ex+nu:print(('PASS ' if ok else 'FAIL ')+n)
    assert all(ok for _,ok in ex+nu),'baseline before any faults'
    sparse=copy.deepcopy(BASE);sparse['sparse']=True;se,sn,sv=evaluate(sparse);assert all(ok for _,ok in se+sn), 'sparse-state zero endpoint control';print('PASS sparse target with initial and interior zero')
    faults=[]
    for key,value in [('cross',False),('reference',False),('tone',-1),('clock',False),('phase',-1),('target_phase',False)]:
        c=copy.deepcopy(BASE);c[key]=value;e,n,v=evaluate(c);failed=[x for x,ok in e+n if not ok];assert failed,(key,'not detected');faults.append({'changed_input':key,'failures':failed});print('PASS fault',key,failed)
    report={'result':'K2332','status':'pass','exact_controls':ex,'finite_60_digit_controls':nu,'changed_input_faults':faults,'evidence':ev,'sparse_target_evidence':sv,'sparse_target_controls':len(se)+len(sn),'scope':'all-N claims rest on written spectrum/averaging/synthesis proof; finite tests are numerical controls only'}
    if a.write:
        deps=[f'tests/channel-swings/{ST.replace("-","_")}_probe.py',f'explorations/conditional-build/{ST}-2026-10-30.md'];report['dependencies']={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps};(R/f'lab/process/{ST}.json').write_text(json.dumps(report,indent=2)+'\n')
if __name__=='__main__':main()
