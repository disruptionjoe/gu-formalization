#!/usr/bin/env python3
"""Exact structural controls; universal scope is in the two linked proof notes."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')
from pathlib import Path
import argparse,hashlib,json
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/source-prescription.json'

def primitive_controls():
    import sympy as s
    I=s.I; eye=s.eye(2); zero=s.zeros(2)
    x,z=s.symbols('x z', real=True)
    N=s.Matrix([[I,1],[1,-I]])
    H=s.diag(1,-1)
    assert N*N==zero and N.H*H+H*N==zero
    E=eye+x*N
    assert s.simplify(E.H*H*E)==H
    eta=x*s.Matrix([[0,1],[1,0]])
    A0=s.Matrix([[I*x,1],[1,-I*x]])
    beta=s.Matrix([[I,0],[0,2*I]])
    varpi=s.Matrix([[0,x],[x,0]])
    alpha=I*eye
    Es=E*(eye+z*eta)
    A0s=A0+z*beta
    vars=varpi+z*alpha
    Bs=Es.inv()*A0s*Es+Es.inv()*Es.diff(x)
    As=A0s+vars
    Ts=As-Bs
    simp=lambda M:M.applyfunc(s.simplify)
    B=simp(Bs.subs(z,0)); A=A0+varpi
    DBeta=eta.diff(x)+B*eta-eta*B
    assert simp(Bs.diff(z).subs(z,0)-E.inv()*beta*E-DBeta)==zero
    assert simp(As.diff(z).subs(z,0)-beta-alpha)==zero
    assert simp(Ts.diff(z).subs(z,0)-alpha-beta+E.inv()*beta*E+DBeta)==zero
    # The independent translation direction leaves epsilon and reference B fixed.
    assert simp((A+z*alpha-B).diff(z)-alpha)==zero
    # Conjugated invariant tensor and its primitive epsilon variation.
    Phi=s.Matrix([[1,2],[3,4]])
    Phis=Es.inv()*Phi*Es; PhiE=E.inv()*Phi*E
    assert simp(Phis.diff(z).subs(z,0)-(PhiE*eta-eta*PhiE))==zero
    # Native trace identity: all universal rank claims use this polynomial identity.
    C=s.Matrix([[0,2],[-2,0]])
    J=s.diag(1,-1)
    assert C*C==-4*eye and C*J+J*C==zero
    assert (C-eye)*(-(C+eye)/5)==eye
    assert (C-eye).det()==5
    assert alpha*C!=alpha and alpha*C==C*alpha
    f=s.symbols('f', real=True)
    assert simp((f*C-eye)*(f*C+eye)+(4*f*f+1)*eye)==zero
    assert (I*C/2-eye).det()==0 and I*C/2!=eye  # Complex normalization removes full-rank defect, not identity mismatch.
    # Fixed invertible epsilon conjugation cannot remove central-current defect.
    Cg=E.inv()*C*E
    assert simp(Cg*Cg+4*eye)==zero
    assert simp((Cg-eye)*(-(Cg+eye)/5))==eye
    assert simp(E.inv()*alpha*E)==alpha
    # Source-native trace can be made parallel but central current still changes.
    X=s.diag(1,-1)  # exact Clifford control X^2=1, X C + C X=0
    assert X*C+C*X==zero
    K=X*C/16
    assert X/2+K*C-C*K==zero
    assert alpha*C-C*alpha==zero and alpha*C-alpha!=zero
    # Differential wrapper derivative including d(eta), tested on arbitrary polynomial section.
    psi=s.Matrix([x*x+1,x+2])
    D=lambda u:u.diff(x)+A*u
    Ds=lambda u:u.diff(x)+(A+z*alpha)*u
    wrapped=Es*Ds(Es.inv()*psi)
    u=E.inv()*psi
    expected=E*(alpha*u+eta*D(u)-D(eta*u))
    assert simp(wrapped.diff(z).subs(z,0)-expected)==s.zeros(2,1)
    assert simp(eta*D(u)-D(eta*u)+(eta.diff(x)+A*eta-eta*A)*u)==s.zeros(2,1)
    return True

def geometry_controls():
    import sympy as s
    from itertools import combinations_with_replacement
    n=4
    g=s.diag(-1,1,1,1);gi=g.inv();pairs=list(combinations_with_replacement(range(n),2));basis=[]
    for i,j in pairs:
     E=s.zeros(n);E[i,j]=E[j,i]=1;basis.append(E)
    def coord(M):return s.Matrix([M[i,j] for i,j in pairs])
    def mat(v):return sum((v[i]*basis[i] for i in range(10)),s.zeros(n))
    def K(A,B):return s.trace(gi*A*gi*B)-s.trace(gi*A)*s.trace(gi*B)/2
    V=s.Matrix(10,10,lambda i,j:K(basis[i],basis[j]));Vi=V.inv();t=coord(g)
    def B(X,Y):
     xf=g*X;yf=g*Y;inner=(X.T*g*Y)[0]
     return -(xf*yf.T+yf*xf.T)/4+inner*g/4
    es=[s.eye(n)[:,i] for i in range(n)]
    Bmap=s.Matrix.hstack(*(coord(B(es[i],es[j])) for i,j in pairs))
    assert Bmap.rank()==10
    assert K(g,g)==-4
    mean=sum((gi[i,j]*B(es[i],es[j]) for i in range(n) for j in range(n)),s.zeros(n))
    assert mean==g/2 and K(mean,mean)==-1
    norm=sum(gi[i,i]*gi[j,j]*K(B(es[i],es[j]),B(es[i],es[j])) for i in range(n) for j in range(n))
    assert norm==2
    for X in [es[0],es[1],es[0]+es[1],es[0]+2*es[1]-3*es[2]]:
     BX=s.Matrix.hstack(*(coord(B(X,Y)) for Y in es))
     assert BX.rank()==4
     F=BX.T*V
     assert F.rank()==4 and len(F.nullspace())==6
     # Exact six-dimensional kernel always supplies a nonnull gamma-correction leg.
     null=F.nullspace();cand=null+[u+v for i,u in enumerate(null) for v in null[i+1:]]
     witness=next(z for z in cand if (z.T*V*z)[0]!=0)
     assert F*witness==s.zeros(4,1)
     assert (witness.T*V*witness)[0]!=0
     # Trace-parallel-only correction retains rank4 and t itself supplies gamma repair.
     BXtf=s.Matrix.hstack(*(coord(B(X,Y)-(X.T*g*Y)[0]*g/8) for Y in es))
     Ftf=BXtf.T*V
     assert BXtf.rank()==4 and Ftf.rank()==4
     assert Ftf*t==s.zeros(4,1) and (t.T*V*t)[0]==-4
     for Y in es:
      assert K(B(X,Y),g)==-(X.T*g*Y)[0]/2
      for v in basis:
       # Shape tensor and mixed derivative are dual; no nonzero v yields zero shape.
       assert K(B(X,Y),v)==-(X.T*v*Y)[0]/2
    # Along y=exp(r)g, t=partial_r. Compute mixed curvature on horizontal/radial plane.
    r,x=s.symbols('r x',real=True);coords=[x,r]
    metric=s.diag(-s.exp(r),-4);inv=metric.inv()
    Gamma=[[[s.simplify(sum(inv[a,d]*(s.diff(metric[d,c],coords[b])+s.diff(metric[d,b],coords[c])-s.diff(metric[b,c],coords[d])) for d in range(2))/2) for c in range(2)] for b in range(2)] for a in range(2)]
    # R(U,V)W = nabla_U nabla_V W - nabla_V nabla_U W, U=x,V=r,W=r.
    Rxtr=s.Matrix([s.simplify(s.diff(Gamma[a][1][1],x)-s.diff(Gamma[a][0][1],r)+sum(Gamma[a][0][b]*Gamma[b][1][1]-Gamma[a][1][b]*Gamma[b][0][1] for b in range(2))) for a in range(2)])
    assert Gamma[0][0][1]==s.Rational(1,2)
    assert Rxtr==s.Matrix([-s.Rational(1,4),0])
    num=(Rxtr.T*metric*s.Matrix([1,0]))[0]
    assert s.simplify(num/(metric[0,0]*metric[1,1]))==s.Rational(1,16)
    assert Rxtr!=s.zeros(2,1) # rejects the overbroad all-ambient trace-flat claim.
    return True

def joint_controls():
    import sympy as s
    I=s.I
    X=s.Matrix([[0,1],[1,0]])
    N=s.Matrix([[0,-I],[I,0]])
    C=2*I*s.diag(1,-1)
    E=s.eye(2);Z=s.zeros(2)
    assert C*C==-4*E
    assert X*C+C*X==Z and N*C+C*N==Z
    K=X*C/16
    assert K*C-C*K==-X/2
    assert s.simplify(-(C+E)/5*(C-E))==E
    f=s.symbols('f',real=True)
    assert s.simplify(-(f*C+E)/(1+4*f*f)*(f*C-E))==E
    # A central variation survives trace-parallelism but detects the whole scalar.
    assert (I*E)*C-C*(I*E)==Z
    assert (I*(C-E)).rank()==2
    # The trace correction does not remove traceless H/N mixing.
    K_other=X*N/2
    assert K_other*C-C*K_other==Z
    assert K_other*X-X*K_other==-N
    # Both paired trace repairs acquire the same central cross-current factor C.
    B1=s.diag(2,3);B0=s.diag(5,7)
    B=s.diag(B1,B0)
    J=s.BlockMatrix([[Z,I*E],[I*E,Z]]).as_explicit()
    Rminus=s.diag(E,C.inv());Rplus=s.diag(E,C)
    Nminus=-4*B*Rminus*J*Rminus
    Nplus=B*Rplus*J*Rplus
    assert Nminus[:2,2:]==Nplus[:2,2:]==B1*I*C
    assert (Nplus[:2,2:]-B1*I).rank()==2
    # Unpaired NW manipulation is different: central NE unchanged before dual change.
    Lminus=s.diag(C,E)
    assert (Lminus*J*Rminus)[:2,2:]==I*E
    return True

def full_operator_controls():
    import sympy as s
    I=s.I;E=s.eye(2);Z=s.zeros(4)
    pa=s.Matrix([[0,1],[1,0]]);pb=s.Matrix([[0,-I],[I,0]]);pc=s.diag(1,-1)
    g=[s.kronecker_product(pa,E),s.kronecker_product(pb,E),s.kronecker_product(pc,pa),s.kronecker_product(pc,pb)]
    for i in range(4):
     for j in range(4):assert g[i]*g[j]+g[j]*g[i]==(2*s.eye(4) if i==j else Z)
    # Hidden normal gamma-kernel map z:S->N* tensor S.
    z=[Z,Z,g[2],-g[3]]
    def gamma(v):return sum((g[i]*v[i] for i in range(4)),Z)
    assert gamma(z)==Z
    # Symmetric tracefree II_00=n2, II_11=-n2.
    vec=[];spin=[]
    for mu,sgn in [(0,1),(1,-1)]:
     w=s.zeros(4);w[2,mu]=sgn;w[mu,2]=-sgn
     vec.append(w);spin.append(sgn*g[2]*g[mu]/2)
    responses=[]
    for mu in range(2):
     r=[spin[mu]*z[a]-sum((vec[mu][b,a]*z[b] for b in range(4)),Z) for a in range(4)]
     assert gamma(r)==Z # FULL trace, not merely horizontal trace.
     assert sum((g[a]*r[a] for a in range(2)),Z)!=Z
     responses.append(r)
    # Complete natural raw symbol with native stable ratio c=-a/12.
    a=s.Integer(1);c=-s.Rational(1,12)
    def symbol(mu,v):
     tr=gamma(v);con=v[mu]
     return [a*(g[mu]*v[k]-(tr if k==mu else Z))+c*g[k]*(con-g[mu]*tr) for k in range(4)]
    full=[sum((symbol(mu,responses[mu])[k] for mu in range(2)),Z) for k in range(4)]
    assert full[0]==-g[0]*g[2] and full[1]==g[1]*g[2]
    assert full[0].det()!=0
    assert responses[0][0]+responses[1][1]==Z # mean trace zero
    # Wrong truncation drops spin-generated normal response and falsely cancels.
    truncated=[[r[0],r[1],Z,Z] for r in responses]
    bad=[sum((symbol(mu,truncated[mu])[k] for mu in range(2)),Z) for k in range(4)]
    assert all(x==Z for x in bad)
    return True

def run():
    suites=[]
    for name,fn,scope in [
        ('source_primitive_current',primitive_controls,'Exact A/B/T variation jet, moving invariant tensor and differential wrappers; full-rank native trace polynomial identity, real/complex normalization and parallel-background contrary controls'),
        ('source_adapted_geometry',geometry_controls,'Native second fundamental form, mean and indefinite norm, rank4 bare defect including null tangents, trace-only survivor leakage and mixed horizontal/trace curvature'),
        ('joint_connection_current',joint_controls,'Mixed Spin correction, central tangent variation and paired-versus-unpaired current controls'),
        ('full_operator',full_operator_controls,'Coherent full form+spin tracefree lower defect versus false cancellation after dropping normal spin response; four active complex Clifford generators, universal14-dimensional proof in note')]:
        assert fn();suites.append(dict(name=name,passed=True,scope=scope))
    refs=['explorations/conditional-build/source-prescription-current-2026-11-13.md', 'explorations/conditional-build/source-chimeric-trace-compatibility-2026-11-13.md']
    deps=['lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md','explorations/conditional-build/source-symbol-quotient-membership-2026-11-12.md','explorations/conditional-build/source-joint-symmetry-current-2026-11-13.md','explorations/conditional-build/source-moving-repair-2026-11-13.md','tests/program-focus/source_prescription_probe.py']
    return dict(schema_version='1.0',program_target='X-P1-P2 / X-P2-P3',tier='T2',classification='INTERNAL_STRUCTURAL_ONLY',claim_ceiling='Source-guided connection-metric reconstruction and specified paired repairs/minimal tangential family; no source unique completion, stationary action, effective sector or class-C decision',evidence_kind='Written general proofs with four exact supporting/contrary suites; suite counts are not discovery counts',primary_source_sha256='3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4',suites=suites,proof_refs=refs,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs+deps})

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args();r=run()
    if args.write:REPORT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert json.loads(REPORT.read_text())==r,'stored evidence or dependency mismatch'
    print(json.dumps({'passed_suites':len(r['suites']),'suites':[s['name'] for s in r['suites']]}))
