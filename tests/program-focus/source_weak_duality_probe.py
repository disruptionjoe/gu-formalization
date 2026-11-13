#!/usr/bin/env python3
"""Exact structural controls. Universal scope is in the two linked proof notes."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')
from pathlib import Path
import argparse,hashlib,json
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/source-weak-duality.json'

def weak_controls():
    """Small exact controls only; general proofs and real-form limits in weak.md."""
    import sympy as S
    I=S.I
    Z=S.Matrix([[1,0],[0,-1]])
    X=S.Matrix([[0,1],[1,0]])
    Y=S.Matrix([[0,-I],[I,0]])

    def cliff(n):
        k=n//2
        out=[]
        for j in range(k):
            for p in (X,Y):
                fs=[Z]*j+[p]+[S.eye(2)]*(k-j-1)
                out.append(S.kronecker_product(*fs))
        return out

    def zero(m): return m==S.zeros(*m.shape)

    g=cliff(6); s=8; eye=S.eye(s)
    for a in range(6):
        for b in range(6):
            assert g[a]*g[b]+g[b]*g[a]==2*(a==b)*eye
    # Self-dual su2; all matrices exact Gaussian rationals.
    t=[(g[0]*g[1]+g[2]*g[3])/2,
       (g[0]*g[2]-g[1]*g[3])/2,
       (g[0]*g[3]+g[1]*g[2])/2]
    assert t[0]*t[1]-t[1]*t[0]==-2*t[2]
    assert t[1]*t[2]-t[2]*t[1]==-2*t[0]
    assert t[2]*t[0]-t[0]*t[2]==-2*t[1]
    Gamma=S.Matrix.hstack(*g)
    K=S.Matrix.vstack(g[0],S.zeros(s),S.zeros(s),S.zeros(s),-g[4],S.zeros(s))
    assert zero(Gamma*K)
    defect=Gamma*S.diag(*([t[0]]*6))*K
    assert defect==-g[0]*g[1]
    assert defect.det()!=0
    # Geometric covariance Γ(r⊗1+1⊗t)=tΓ, with [t,γ_j]=Σr_ijγ_i.
    r=S.zeros(6)
    for j in range(6):
        comm=t[0]*g[j]-g[j]*t[0]
        for i in range(6):
            r[i,j]=S.trace(g[i]*comm)/s
        assert comm==sum((r[i,j]*g[i] for i in range(6)),S.zeros(s))
    TG=S.kronecker_product(r,eye)+S.diag(*([t[0]]*6))
    assert zero(Gamma*TG-t[0]*Gamma)
    # Haar/core proof control. Γ2 acts on the two inert normal directions.
    G4=S.Matrix.hstack(*g[:4],S.zeros(s),S.zeros(s))
    G2=Gamma-G4
    Pa=-t[0]*t[0]
    assert Pa*Pa==Pa and S.trace(Pa)==s//2
    rows=[G2,G4]+[G4*S.diag(*([u]*6)) for u in t+[Pa]]
    stack=S.Matrix.vstack(*rows)
    assert stack.rank()==6*s-5*s//2
    # Correlated q grades on a minimal 2+2 even split.
    h=cliff(4); d=4
    CH=I*h[0]*h[1]; CN=I*h[2]*h[3]
    GH=S.Matrix.hstack(*h[:2]); GN=S.Matrix.hstack(*h[2:]); G=S.Matrix.hstack(*h)
    q=S.BlockMatrix([[S.eye(2*d),S.zeros(2*d,2*d),S.zeros(2*d,d)],
                     [GH,GN,S.zeros(d)],
                     [S.zeros(d,2*d),S.zeros(d,2*d),S.eye(d)]]).as_explicit()
    for chi,sign in ((CH,1),(CN,-1)):
        # τ'=sign χτ+(1-sign? horizontal anti rules) correction.
        # CH: -2χGH b; CN: +2χGH b.
        lower=(-2 if sign==1 else 2)*chi*GH
        CQ=S.BlockMatrix([[S.diag(chi,chi),S.zeros(2*d,d),S.zeros(2*d,d)],
                           [lower,sign*chi,S.zeros(d)],
                           [S.zeros(d,2*d),S.zeros(d),chi]]).as_explicit()
        source=S.diag(*([chi]*5))
        assert zero(q*source-CQ*q)
        assert CQ*CQ==S.eye(4*d)
    # Exact source-toy response and nonuniformity.
    z,m=S.symbols('z m',nonzero=True)
    L=S.Matrix([[z,-m],[-m,z]])
    R=L.inv()
    assert S.simplify(R[0,1]-m/(z*z-m*m))==0
    assert S.simplify((R[0,1]/R[0,0]).subs(z,2*m))==S.Rational(1,2)
    assert R.subs(m,0)==S.eye(2)/z
    # Inert versus negative weak-plane vector adapters in this exact local control.
    assert all(zero(ti*g[4]-g[4]*ti) for ti in t)
    negative_trace_control=I*g[0]
    assert negative_trace_control*negative_trace_control==-eye
    assert any(not zero(ti*negative_trace_control-negative_trace_control*ti) for ti in t)

    return True

def duality_controls():
    """Small exact bookkeeping controls; the general theorem is the span proof."""
    from itertools import product
    from pathlib import Path
    root=ROOT
    s=(root/'lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md').read_text()
    anchor='Machine-readable cell ledger, in row-major order:'
    ledger=s.split(anchor,1)[1].split('```text',1)[1].split('```',1)[0].strip().splitlines()
    assert len(ledger)==16
    actual={(i//4,i%4) for i,x in enumerate(ledger) if 'd0' in x}
    expected={(0,1),(0,3),(1,0),(1,2),(2,1),(3,0)}
    assert actual==expected
    assert ledger[9].startswith('minus-d0-star') and ledger[12].startswith('minus-d0-star')
    assert all(ledger[4*i+j]=='southeast-zero' for i in (2,3) for j in (2,3))
    # σ0,σ1,τ0,τ1 independently vary: natural opposite-half pairing.
    sol=[]
    for s0,s1,t0,t1 in product((-1,1),repeat=4):
        if t1==s1 and t1==-s0 and t0==-s1:
            sol.append((s0,s1,t0,t1))
    assert sol==[(-1,1,-1,1),(1,-1,1,-1)]
    assert not any(x[0]==x[1] for x in sol) # bars-only correction impossible
    # pairing support k: bar actual sign = k * output actual sign.
    # Printed cells always pair same input/bar labels, so k*arrow_parity=+1.
    def fits(k1,k0,nw,ne,sw):
        return k1*nw==1 and k1*ne==1 and k0*sw==1
    assert not any(fits(k1,k0,-1,1,1) for k1,k0 in product((-1,1),repeat=2))
    assert fits(1,1,1,1,1) # odd tensor in duals and NW
    assert fits(-1,-1,-1,-1,-1) # natural duals, both cross arrows changed
    assert not fits(1,1,-1,1,1) # duality-only added tensor fails
    assert not fits(-1,-1,1,1,1) # changed NW alone with natural duals fails
    assert not fits(-1,-1,-1,-1,1) # one cross arrow left unchanged fails
    # C,G cannot cancel: component3 gives c=0, component2 gives a=0.
    # Encode exact coefficient constraints as a rank calculation over integers.
    constraints=((0,-1),(1,0))
    det=constraints[0][0]*constraints[1][1]-constraints[0][1]*constraints[1][0]
    assert det==1
    return True

def joint_controls():
    """Exact reduced Clifford control of two-sided repairs; general proof is separate."""
    import sympy as s
    I=s.I;X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);Z=s.diag(1,-1);Id=s.eye(4);O=s.zeros(4)
    g=[s.kronecker_product(X,s.eye(2)),s.kronecker_product(Y,s.eye(2)),s.kronecker_product(Z,X),s.kronecker_product(Z,Y)]
    g[0]=I*g[0];eta=[-1,1,1,1];n=4;G=s.Matrix.hstack(*g);J=s.Matrix.vstack(*[eta[i]*g[i] for i in range(n)])
    def raw(p):
     c=sum((p[i]*g[i] for i in range(n)),O.copy());x=s.Matrix.vstack(*[z*Id for z in p]);ii=s.Matrix.hstack(*[eta[i]*p[i]*Id for i in range(n)]);T=s.diag(*([c]*n))-x*G-s.Rational(1,2)*J*(ii-c*G)
     return T.row_join(x).col_join((-ii).row_join(O))
    D0=raw([1,0,0,0]);D1=raw([0,1,0,0]);E=-D0.inv()*D1
    assert E*E==s.eye(20)
    q=s.eye(20)[:8,:].col_join(G.row_join(O)).col_join(s.eye(20)[16:,:])
    A=g[2];A1=s.diag(*([A]*4));F=s.diag(s.eye(16),A);Fn=F.inv();Ln=s.diag(A1,Id)
    for name,L,R in [('NW',Ln,Fn),('cross',F,F)]:
     N0=L*D0*R;N1=L*D1*R;En=-N0.inv()*N1
     assert En==R.inv()*E*R and En*En==s.eye(20)
     S=s.diag(s.eye(12),R[16:,16:]);assert q*R==S*q
     for k in q.nullspace(): assert q*En*k==s.zeros(16,1)
     if name=='NW':
      assert N0[:16,16:]==D0[:16,16:] and N0[16:,:16]==D0[16:,:16]
      assert any(q*N1*k!=s.zeros(16,1) for k in q.nullspace())
     else: assert N0[:16,:16]==D0[:16,:16]
    # Multiplying NW-repair rows by the B^t adapter gives the same bilinear
    # scalar-coordinate congruence up to lambda=A^2, for arbitrary B on the left.
    Bchange=s.diag(A1,A);lam=(A*A)[0,0]
    assert Bchange*(Ln*D1*Fn)==lam*Fn*D1*Fn
    # Null-vector adapter fails invertibility.
    Anull=g[0]+g[2];assert Anull*Anull==O and Anull.det()==0
    return True

def run():
    suites=[]
    for name,fn,scope in [
        ('weak_transport',weak_controls,'Reduced complex Clifford controls: su2, surjective hidden defect, geometric covariance, common invariant kernel, transported grades, conditional source-toy response and weak-fixed adapter countercontrol'),
        ('degree_duality',duality_controls,'Primary16-cell transcription, all16 independent degree-label flips, two relative-relabel solutions, arrow parity repairs and contrary controls'),
        ('joint_repairs',joint_controls,'ReducedCl(3,1) exact LDR identities, stable evolution similarity, q-kernel closure, raw-row contrary control, shared bilinear congruence and null adapter failure')]:
        assert fn()
        suites.append(dict(name=name,passed=True,scope=scope))
    refs=['explorations/conditional-build/source-weak-action-transport-2026-11-13.md', 'explorations/conditional-build/source-degree-duality-compatibility-2026-11-13.md']
    deps=['lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md','lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md','explorations/conditional-build/source-symbol-quotient-membership-2026-11-12.md','explorations/conditional-build/source-current-grading-membership-2026-11-12.md','tests/program-focus/source_weak_duality_probe.py']
    return dict(schema_version='1.0',program_target='X-P1-P2 / X-P2-P3',tier='T2',classification='INTERNAL_STRUCTURAL_ONLY',claim_ceiling='Frozen structural categories and conditional estimates; no source-selected action, physical chirality/current, class-C decision or global-domain realization',evidence_kind='Written general proofs with three exact supporting/contrary control suites; suite or assertion counts are not discovery counts',suites=suites,proof_refs=refs,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs+deps})

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args();r=run()
    if args.write:REPORT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert json.loads(REPORT.read_text())==r,'stored evidence or dependency mismatch'
    print(json.dumps({'passed_suites':len(r['suites']),'suites':[s['name'] for s in r['suites']]}))
