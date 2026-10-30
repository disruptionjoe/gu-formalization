#!/usr/bin/env python3
"""Exact formulas and finite 70-digit controls; uniform bounds live in the note."""
import argparse,copy,hashlib,json
from pathlib import Path
import sympy as s
import mpmath as mp
R=Path(__file__).resolve().parents[2];ST='k2330-microscopic-kerr-validity';mp.mp.dps=70
BASE=dict(chi=2,linear_quartic=-1,remainder=2,jump_sign=-1,number_sign=-1,compensate_atom=True,spacing=2,revival_energy="jc",drive_dressed=True)
def evaluate(c):
    exact=[];numeric=[]
    def ck(name,ok):exact.append((name,bool(ok)))
    def cn(name,ok):numeric.append((name,bool(ok)))
    x,D,g=s.symbols('x D g',positive=True);z=s.symbols('z');E=(D-s.sqrt(D*D+4*g*g*x))/2
    block=s.Matrix([[0,g*s.sqrt(x)],[g*s.sqrt(x),D]])
    ck('actual two-level characteristic polynomial',s.factor(block.charpoly(z).as_expr())==z*z-D*z-g*g*x)
    ck('lower energy is eigenvalue',s.simplify(E*E-D*E-g*g*x)==0)
    ck('second derivative',s.simplify(s.diff(E,x,2)-2*g**4/(D*D+4*g*g*x)**s.Rational(3,2))==0)
    ck('third derivative',s.simplify(s.diff(E,x,3)+12*g**6/(D*D+4*g*g*x)**s.Rational(5,2))==0)
    poly=-g*g*x/D+g**4*x*x/D**3;comp=(g*g/D+c['linear_quartic']*g**4/D**3)*x
    ck('quadratic becomes Kerr after TOTAL compensation',s.simplify(poly+comp-c['chi']*g**4*x*(x-1)/(2*D**3))==0)
    ck('Taylor third-order coefficient',s.simplify(s.diff(E,x,3).subs(x,0)/6+c['remainder']*g**6/D**5)==0)
    h=s.symbols('h',positive=True);a,b,d=s.symbols('a b d')
    def fd(f,order):return s.expand(sum((-1)**(order-j)*s.binomial(order,j)*f.subs(x,j*h) for j in range(order+1)))
    ck('second difference removes every affine',fd(a+b*x,2)==0)
    ck('third difference removes every quadratic',fd(a+b*x+d*x*x,3)==0)
    ck('affine lower-bound constant',s.Rational(2,4)==s.Rational(1,2))
    ck('quadratic lower-bound constant',s.Rational(12,8)==s.Rational(3,2))
    ck('quadratic fit cannot remove cubic',fd(x**3,3)==6*h**3)
    ck('Kerr revival identity on integer levels',all(s.simplify(s.exp(-s.I*s.pi*j*(j-1)))==1 for j in range(8)))
    # Complete fixed-total-excitation shell; includes upper branch and reference.
    N=4;dd=mp.mpf(10);gg=mp.mpf(1);basis=[(p,N-p-e,e) for e in (0,1) for p in range(N-e+1)];dim=len(basis);idx={v:i for i,v in enumerate(basis)}
    H=mp.matrix(dim);np=mp.matrix(dim);ne=mp.matrix(dim);U=mp.eye(dim);C=mp.matrix(dim)
    def theta(n):return mp.atan(2*gg*mp.sqrt(n)/dd)/2
    def ee(n):return (dd-mp.sqrt(dd*dd+4*gg*gg*n))/2
    for i,(p,r,e) in enumerate(basis):
        H[i,i]=dd*e;np[i,i]=p;ne[i,i]=e
        if e==0 and p>=1:
            j=idx[p-1,r,1];H[i,j]=H[j,i]=gg*mp.sqrt(p)
        if p>=1:
            j=idx[p-1,r+1,e];C[j,i]=C[i,j]=mp.mpf('.02')*mp.sqrt(p*(r+1))
    for n in range(1,N+1):
        i=idx[n,N-n,0];j=idx[n-1,N-n,1];cc=mp.cos(theta(n));ss=mp.sin(theta(n))
        U[i,i]=cc;U[j,i]=-ss;U[i,j]=ss;U[j,j]=cc
    def nf(M):return mp.sqrt(sum(abs(v)**2 for v in M))
    def op(M):return max(abs(v) for v in mp.eigsy(M,eigvals_only=True))
    tol=mp.mpf('1e-60')
    cn('full dressing unitary',nf(U.T*U-mp.eye(dim))<tol)
    HD=U.T*H*U
    cn('full dressed Hamiltonian diagonal',nf(HD-mp.diag([HD[j,j] for j in range(dim)]))<tol)
    for n in range(1,N+1):
        i=idx[n,N-n,0];j=idx[n-1,N-n,1];ss=mp.sin(theta(n));cc=mp.cos(theta(n));ND=U.T*np*U
        cn('number diagonal n='+str(n),abs(ND[i,i]-(n+c['number_sign']*ss**2))<tol)
        cn('number offbranch n='+str(n),abs(ND[j,i]-ss*cc)<tol)
        rn=ee(n)+gg*gg*n/dd-gg**4*n*n/dd**3
        cn('actual Taylor remainder n='+str(n),-c['remainder']*gg**6*n**3/dd**5<=rn<=0)
    total=np+ne
    compensation=np+(ne if c['compensate_atom'] else mp.matrix(dim))
    cn('specified compensation really commutes',nf(compensation*H-H*compensation)<tol)
    cn('photon loss number does not commute',nf(np*H-H*np)>1)
    rho=gg*mp.sqrt(N)/dd
    cn('dressing rotation bound',max(2*mp.sin(theta(n)/2) for n in range(1,N+1))<=rho)
    cactual=U.T*C*U if c['drive_dressed'] else C
    cn('actual transformed hopping matches basis',nf(cactual-U.T*C*U)<tol)
    cn('control conjugation norm bound',op(U.T*C*U-C)<=2*rho*op(C))
    # Direct actual annihilation across adjacent excitation doublets.
    for n in range(2,N+1):
        cn0=mp.cos(theta(n));sn=mp.sin(theta(n));cp=mp.cos(theta(n-1));sp=mp.sin(theta(n-1))
        init=mp.matrix([cn0,-sn]);amat=mp.diag([mp.sqrt(n),mp.sqrt(n-1)]);up=mp.matrix([[cp,sp],[-sp,cp]])
        out=up.T*amat*init
        alpha=mp.sqrt(n)*cn0*cp+mp.sqrt(n-1)*sn*sp
        beta=mp.sqrt(n)*cn0*sp+c['jump_sign']*mp.sqrt(n-1)*sn*cp
        cn('annihilation both branches n='+str(n),abs(out[0]-alpha)+abs(out[1]-beta)<tol)
        cn('nonzero upper loss branch n='+str(n),abs(out[1])>mp.mpf('1e-8'))
    for hh in (1,):
        sec=ee(2*hh)-2*ee(hh)+ee(0);third=ee(3*hh)-3*ee(2*hh)+3*ee(hh)-ee(0)
        cn('finite difference affine certificate',sec/4>=gg**4*hh**2/(2*(dd*dd+8*gg*gg*hh)**mp.mpf('1.5')))
        cn('finite difference quadratic certificate',-third/8>=3*gg**6*hh**3/(2*(dd*dd+12*gg*gg*hh)**mp.mpf('2.5')))
    gapmin=2*gg**4/(dd*dd+4*gg*gg*N)**mp.mpf('1.5')
    for n in range(1,N):
        actual=ee(n+1)-2*ee(n)+ee(n-1)
        cn('exact nonuniform gap n='+str(n),actual>=gapmin)
    # Constant error in claimed gap must also fail a small-coupling limit fixture.
    zz=mp.mpf('0.00001');actual=(1-mp.sqrt(1+8*zz**2))/2-2*(1-mp.sqrt(1+4*zz**2))/2
    cn('gap bound coefficient',actual>=c['spacing']*zz**4/(1+16*zz**2)**mp.mpf('1.5'))
    chi=2*gg**4/dd**3;compc=gg*gg/dd-gg**4/dd**3;Tchi=2*mp.pi/chi
    energy=ee(N)+compc*N if c["revival_energy"]=="jc" else chi*N*(N-1)/2
    phase=abs(mp.exp(-1j*energy*Tchi)-1)
    cn('nominal revival residual actually nonzero',phase>mp.mpf('.01'))
    cn('nominal revival residual bounded',phase<=2*mp.pi*(gg/dd)**2*N**3)
    # Direct whole-carrier Hamiltonian evolution; upper drift is retained exactly.
    HH=HD+compc*total;ideal=HH.copy()
    for n in range(N+1):ideal[idx[n,N-n,0],idx[n,N-n,0]]=chi*n*(n-1)/2
    tt=mp.mpf('.3');diff=mp.expm(-1j*(HH+U.T*C*U)*tt)-mp.expm(-1j*(ideal+C)*tt)
    # Frobenius comparison divided by sqrt(dim) is only a necessary numerical control;
    # actual spectral norm computed via positive diff*diff.
    normdiff=mp.sqrt(max(mp.eighe(diff.H*diff,eigvals_only=True)))
    bound=tt*(2*gg**6*N**3/dd**5+2*rho*op(C))
    cn('full-carrier propagator error bounded',normdiff<=bound)
    cn('actual hard charge includes mediator',all(p+r+e==N for p,r,e in basis) and any(p+r<N for p,r,e in basis))
    return exact,numeric

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    ex,nu=evaluate(BASE);bad=[n for n,v in ex+nu if not v]
    if bad:raise AssertionError('BASELINE FAIL '+str(bad))
    faults=dict(kerr_factor={'chi':1},wrong_linear_compensation={'linear_quartic':1},missing_remainder={'remainder':1},wrong_jump_branch={'jump_sign':1},bare_number={'number_sign':0},cavity_only_compensation={'compensate_atom':False},oversized_gap={'spacing':3},quadratic_spectrum_substitution={'revival_energy':'kerr'},untransformed_control={'drive_dressed':False})
    caught={}
    for name,changes in faults.items():
        c=copy.deepcopy(BASE);c.update(changes);a,b=evaluate(c);failed=[n for n,v in a+b if not v]
        if not failed:raise AssertionError('MUTATION ESCAPED '+name)
        caught[name]=failed
    deps=[f'explorations/conditional-build/{ST}-2026-10-30.md',str(Path(__file__).relative_to(R)),'explorations/conditional-build/k2328-local-neutral-readout-compiler-2026-10-30.md']
    out=dict(result_id='K2330',status='PASS',scope='Exact formulas and finite 70-digit matrix controls; written proofs supply uniform bounds. Not interval/proof-assistant/hardware certification.',exact_checks=len(ex),numerical_checks=len(nu),precision_digits=70,checks=[n for n,v in ex+nu],mutations=caught,dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
    if args.write:(R/f'lab/process/{ST}.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['result_id','status','exact_checks','numerical_checks']}),'faults',len(caught))
if __name__=='__main__':main()
