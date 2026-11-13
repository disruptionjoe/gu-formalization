#!/usr/bin/env python3
"""Exact structural controls; universal scope is in the two linked proof notes."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')
from pathlib import Path
import argparse,hashlib,json
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/source-current-geometry.json'

def symmetry_controls():
    from collections import Counter
    from fractions import Fraction as F
    from math import prod
    checks=[]
    def check(label,p):
     assert p,label
     checks.append(label)
    def conj_sm(k):
     c,w,y=k;return ({'3':'b3','b3':'3'}.get(c,c),w,-y)
    def conj_em(k):
     c,q=k;return ({'3':'b3','b3':'3'}.get(c,c),-q)
    def dims(c):return {'1':1,'3':3,'b3':3,'4':4,'b4':4}[c]
    def hom(a,b):return sum(m*b[k] for k,m in a.items())
    def overlap(a,b,dim):return sum(dim(k)*min(m,b[k]) for k,m in a.items())
    # Pati-Salam zero-overlap control and universal-rank formula instances.
    Fps=Counter({('4',2,1):1,('b4',1,2):1})
    Bps=Counter({('b4',2,1):1,('4',1,2):1})
    check('PS zero odd Hom',hom(Fps,Bps)==0)
    check('PS full Lorentz commutant dimension 8',2*sum(m*m for m in (Fps+Bps).values())==8)
    check('PS maximal odd rank zero',8*overlap(Fps,Bps,lambda k:dims(k[0])*k[1]*k[2])==0)
    Fsm=Counter({('3',2,1):1,('b3',1,2):1,('b3',1,-4):1,('1',2,-3):1,('1',1,6):1,('1',1,0):1})
    Fbar=Counter({conj_sm(k):m for k,m in Fsm.items()})
    check('SM Hom dimension 1',hom(Fsm,Fbar)==1)
    check('SM common dimension 1',overlap(Fsm,Fbar,lambda k:dims(k[0])*k[1])==1)
    check('SM maximal odd rank 8',8*overlap(Fsm,Fbar,lambda k:dims(k[0])*k[1])==8)
    Fem=Counter()
    for (c,w,y),m in Fsm.items():
     for t in range(-w+1,w,2):Fem[(c,F(y,6)+F(t,2))]+=m
    FbEm=Counter({conj_em(k):m for k,m in Fem.items()})
    check('EM conjugate contents identical',Fem==FbEm)
    check('EM maximal odd rank 128',8*overlap(Fem,FbEm,lambda k:dims(k[0]))==128)
    check('EM Hom dimension 10',hom(Fem,FbEm)==10)
    check('EM common dimension16',overlap(Fem,FbEm,lambda k:dims(k[0]))==16)
    check('EM six multiplicity1 and one multiplicity2 blocks',sorted(Fem.values())==[1]*6+[2])
    for name,a,b,expected_total,expected_odd in [('SM',Fsm,Fbar,28,4),('EM',Fem,FbEm,80,40)]:
     total=a+b
     check(name+' full complex commutant',2*hom(total,total)==expected_total)
     check(name+' odd complex commutant',4*hom(a,b)==expected_odd)
    # Sparse exact normal Cl10 exterior realization: rows/columns are five-mode masks.
    N=32
    I={(i,i):1 for i in range(N)}
    def add(a,b,s=1):
     d=a.copy()
     for k,v in b.items():d[k]=d.get(k,0)+s*v
     return {k:v for k,v in d.items() if v}
    def mul(a,b):
     d={}; br={}
     for (k,j),v in b.items():br.setdefault(k,[]).append((j,v))
     for (i,k),v in a.items():
      for j,w in br.get(k,[]):d[i,j]=d.get((i,j),0)+v*w
     return {k:v for k,v in d.items() if v}
    def comm(a,b):return add(mul(a,b),mul(b,a),-1)
    def create(k):return {(m|(1<<k),m):(-1)**((m&((1<<k)-1)).bit_count()) for m in range(N) if not m&(1<<k)}
    def trans(a):return {(j,i):v for (i,j),v in a.items()}
    c=[create(k) for k in range(5)];ann=[trans(x) for x in c]
    number=[mul(c[k],ann[k]) for k in range(5)]
    def diag_charge(weights):return {(m,m):sum(weights[k] for k in range(5) if m&(1<<k)) for m in range(N) if sum(weights[k] for k in range(5) if m&(1<<k))}
    Y6=diag_charge([-2,-2,-2,3,3]);Q3=diag_charge([-1,-1,-1,3,0]);chi={(m,m):(-1)**m.bit_count() for m in range(N)}
    P=I
    for x in c:P=mul(P,x)
    M=trans(P);sterile=add(P,M)
    check('normal degree5 sterile transition rank1 each',len(P)==len(M)==1 and len(sterile)==2)
    check('degree5 transition is chirality odd',not add(mul(chi,sterile),mul(sterile,chi)))
    check('degree5 transition commutes Y',not comm(Y6,sterile))
    for i in range(5):
     for j in range(5):
      if i!=j:check('degree5 commutes sl5 E'+str(i)+str(j),not comm(mul(c[i],ann[j]),sterile))
    V=add(c[4],ann[4])
    check('neutral vector square identity',mul(V,V)==I)
    check('neutral vector odd',not add(mul(chi,V),mul(V,chi)))
    check('neutral vector EM fixed',not comm(Q3,V))
    check('neutral vector not Y fixed',bool(comm(Y6,V)))
    check('neutral vector not weak raising fixed',bool(comm(mul(c[3],ann[4]),V)))
    for i in range(3):
     for j in range(3):check('neutral vector color fixed '+str(i)+str(j),not comm(mul(c[i],ann[j]),V))
    return True

def current_controls():
    import sympy as s

    n=6
    I=s.eye(n)
    Z=s.zeros(n)
    chi=s.diag(1,1,1,-1,-1,-1)
    rho=s.diag(1,2,0,1,2,0)
    C=s.zeros(n)
    for i in range(3):
        C[i,i+3]=C[i+3,i]=1
    assert C*C==I
    assert chi*C+C*chi==Z
    assert rho*C-C*rho==Z  # Odd full-rank equivariance is possible.
    assert rho*C-rho != Z  # It does NOT preserve the held cross-current.

    # Arbitrary invertible sterile modification preserves both current vertices.
    F=I.copy()
    F[2,2]=F[5,5]=0
    F[2,5]=F[5,2]=1
    assert rho*F==rho and F*rho==rho
    assert chi*F+F*chi != Z  # Such a repair is not globally odd.

    # Full-parent variation sees that sterile modification too.
    assert I*F != I

    # Two-sided cross-only classification permits separate triangular maps.
    V=I.copy(); V[2,0]=3
    U=I.copy(); U[0,2]=5
    assert rho*V==rho and U*rho==rho
    assert V*rho!=rho and rho*U!=rho
    assert U*rho*V==rho

    # Density row and spinor endomorphism cannot be silently identified.
    B0=s.diag(1,2,3,4,5,6)*C
    B1=s.diag(7,8,9,10,11,12)*C
    B=s.diag(B1,B0)
    D=s.BlockMatrix([[I,rho],[rho,Z]]).as_explicit()
    R=s.diag(I,C)
    K=B*D
    transformed=B*R*D*R
    assert transformed==(B*R*B.inv())*K*R
    assert transformed!=R*K*R

    # Exact connection-dependent chain rule, with a density scale absorbed left.
    a=s.symbols('a', real=True)
    H=s.zeros(2); H[0,1]=1
    L=(1+a)*s.eye(2)
    R2=s.eye(2)+a*H
    D2=s.Matrix([[a,1],[1,0]])
    exact=(L*D2*R2).diff(a)
    three=L.diff(a)*D2*R2+L*D2.diff(a)*R2+L*D2*R2.diff(a)
    assert s.simplify(exact-three)==s.zeros(2)
    assert s.simplify(exact-L*D2.diff(a)*R2)!=s.zeros(2)

    # Independently verified branching table dimensions, not a particle count.
    multiplets=[(6,True,True),(3,False,True),(3,False,True),
                (2,True,True),(1,False,True),(1,False,False)]
    assert sum(d for d,_,_ in multiplets)==16
    assert sum(d for d,w,_ in multiplets if w)==8
    assert sum(d for d,_,sm in multiplets if sm)==15
    return True

def moving_controls():
    import sympy as s
    x=s.symbols('x',real=True);I=s.I
    X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);J=s.diag(1,-1)
    A=s.cos(x*x)*X+s.sin(x*x)*Y
    simp=lambda M:M.applyfunc(s.simplify)
    assert simp(A*A)==s.eye(2) and A.H==A and simp(A*J+J*A)==s.zeros(2)
    dA=A.diff(x);assert simp(dA.H*dA)==4*x*x*s.eye(2)
    # Exact involution connection correction, not automatically Spin-valued.
    K=A*dA/2
    assert simp(dA+K*A-A*K)==s.zeros(2)
    assert simp(K.H+K)==s.zeros(2)
    # Full Leibniz compensation and covariant connection variation.
    f=s.Matrix([x*x,x+1]);omega=x*J;rho=X
    nabla=lambda M:M.diff(x)+omega*M-M*omega
    Cp=nabla(A);Cm=-Cp*A
    assert simp((A*f).diff(x)+omega*A*f-A*(f.diff(x)+omega*f)-Cp*f)==s.zeros(2,1)
    alpha=s.symbols('alpha');Cpvar=A.diff(x)+(omega+alpha*rho)*A-A*(omega+alpha*rho)
    assert simp(Cpvar.diff(alpha)-(rho*A-A*rho))==s.zeros(2)
    # General graph-normal trace metric; vertical t=(1,0), K(t,t)=-4.
    a,b=s.symbols('a b',real=True);G=s.Matrix([[-1]]);V=s.diag(-4,1);L=s.Matrix([a,b]);t=s.Matrix([1,0]);M=G+L.T*V*L;beta=L.T*V*t
    u=M.inv()*beta;N=s.Matrix.vstack(-u,t-L*u);ambient=s.diag(-1,-4,1);tangent=s.Matrix.vstack(s.eye(1),L)
    assert simp(tangent.T*ambient*N)==s.zeros(1)
    norm=s.factor((N.T*ambient*N)[0]);assert s.simplify(norm-(-4-(beta.T*M.inv()*beta)[0]))==0
    for av,bv,expected in [(0,s.Rational(1,2),-4),(1,0,-s.Rational(4,5)),(1,1,0),(1,2,12)]:
     assert norm.subs({a:av,b:bv})==expected
     assert M[0].subs({a:av,b:bv})<0
     assert N.subs({a:av,b:bv})!=s.zeros(3,1)
    return True

def graph_trace_controls():
    from fractions import Fraction as F


    def dot(u, v):
        return -u[0] * v[0] - 4*u[1]*v[1] + u[2]*v[2]


    def projected(a, c):
        a, c = F(a), F(c)
        M = -1-4*a*a+c*c
        if not M:
            raise ValueError('degenerate tangent; orthogonal projector unavailable')
        b = -4*a
        x = b/M
        tangent = (F(1), a, c)
        normal = (-x, 1-a*x, -c*x)
        assert dot(normal, tangent) == 0
        assert dot(normal, normal) == -4-b*b/M
        assert dot(normal, normal) == 4*(c*c-1)/(1+4*a*a-c*c)
        assert normal != (0, 0, 0)
        return M, normal, dot(normal, normal)


    cases = [
        (1, 0, F(-5), F(-4, 5)),
        (1, 1, F(-4), F(0)),
        (1, F(3, 2), F(-11, 4), F(20, 11)),
        (0, F(1, 2), F(-3, 4), F(-4)),
    ]
    for a, c, expected_M, expected_norm in cases:
        M, n, norm = projected(a, c)
        assert M == expected_M < 0  # three untouched spatial +1 slots: same Lorentz signature
        assert norm == expected_norm
    assert projected(1, 1)[1] == (F(-1), F(0), F(-1))
    assert projected(1, F(3, 2))[1] == (F(-16, 11), F(-5, 11), F(-24, 11))
    try:
        projected(0, 1)
    except ValueError:
        pass
    else:
        raise AssertionError('failed to reject degenerate tangent')
    return True

def run():
    suites=[]
    for name,fn,scope in [
        ('full_symmetry',symmetry_controls,'Exact branching, PS/SM/EM commutant dimensions and ranks, degree-five sterile exchange, neutral-vector and broken-generator controls'),
        ('fixed_current',current_controls,'Charged/sterile support, equivariance versus held current, independent triangular maps, density-row conjugation and full connection chain rule'),
        ('moving_geometry',moving_controls,'Moving involution, connection adjustment, Leibniz and connection-current variation, symbolic graph-normal projection with fixed tangent signature'),
        ('graph_trace',graph_trace_controls,'Independent rational negative/null/positive/tracefree graph controls, nonzero null normal, exact orthogonality and rejection of tangent degeneracy')]:
        assert fn()
        suites.append(dict(name=name,passed=True,scope=scope))
    refs=['explorations/conditional-build/source-joint-symmetry-current-2026-11-13.md', 'explorations/conditional-build/source-moving-repair-2026-11-13.md']
    deps=['lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md','lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md','explorations/conditional-build/source-symbol-quotient-membership-2026-11-12.md','explorations/conditional-build/source-current-grading-membership-2026-11-12.md','explorations/conditional-build/source-weak-action-transport-2026-11-13.md','explorations/conditional-build/source-degree-duality-compatibility-2026-11-13.md','tests/program-focus/source_current_geometry_probe.py']
    return dict(schema_version='1.0',program_target='X-P1-P2 / X-P2-P3',tier='T2',classification='INTERNAL_STRUCTURAL_ONLY',claim_ceiling='Conditional symmetry/current/geometry categories; no source-selected action, physical chirality/current, class-C decision or global-domain realization',evidence_kind='Written general proofs with four exact supporting/contrary suites; suite or assertion counts are not discovery counts',suites=suites,proof_refs=refs,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs+deps})

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args();r=run()
    if args.write:REPORT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert json.loads(REPORT.read_text())==r,'stored evidence or dependency mismatch'
    print(json.dumps({'passed_suites':len(r['suites']),'suites':[s['name'] for s in r['suites']]}))
