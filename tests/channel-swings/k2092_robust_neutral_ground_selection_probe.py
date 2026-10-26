"""Exact finite controls; universal claims require the linked written proof."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def require(ok,msg):
    if not ok: raise AssertionError('[FAIL] '+msg)
def close(a,b,msg): require(a==b,msg)
def dependency_check(slug):
    d=json.loads((ROOT/('lab/process/'+slug+'.json')).read_text())
    for p,h in d['inputs'].items(): require(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'dependency '+p)
def exercise(faults,slug):
    checks(None)
    print('PASS exact finite mathematical baseline')
    for fault in faults:
        try: checks(fault)
        except AssertionError as e:
            require(str(e).startswith('[FAIL]'),'crash is not detection')
            print('CAUGHT',fault,str(e))
        else: raise AssertionError('undetected mathematical fault '+fault)
    dependency_check(slug)
    print('PASS',len(faults),'genuine faults; dependency custody separate; universal proofs are in note')

def annihilators(n):
    aa=[]
    for j in range(n):
      a=s.zeros(2**n)
      for col in range(2**n):
        if (col>>j)&1:a[col^(1<<j),col]=(-1)**((col&((1<<j)-1)).bit_count())
      aa.append(a)
    return aa
def qfree(C):
    n=C.rows;M=C*(s.eye(n)-C).inv();rho=s.zeros(2**n); pref=(s.eye(n)-C).det()
    for i in range(2**n):
      ii=[k for k in range(n) if (i>>k)&1]
      for j in range(2**n):
       jj=[k for k in range(n) if (j>>k)&1]
       if len(ii)==len(jj):rho[i,j]=pref*M.extract(ii,jj).det()
    return s.simplify(rho)
def covariance(rho,aa):return s.Matrix(len(aa),len(aa),lambda i,j:s.trace(rho*aa[j].conjugate().T*aa[i]))
def checks(fault):
    aa=annihilators(2);J=s.Matrix([[0,-1],[1,0]]);H=s.diag(1,-1)
    C=s.diag(s.Rational(1,2),s.Rational(3,4))
    if fault=='bad_covariance':C[1,1]=s.Rational(1,2)
    rho=qfree(C);G=aa[0].T*aa[0]-aa[1].T*aa[1];A=aa[1].T*aa[0]
    defect=s.trace(rho*A.T*(G*A-A*G));close(defect,-s.Rational(1,4),'sharp asymmetric neutral witness')
    eta=s.Rational(1,4);eps=s.Rational(1,4);m=s.Rational(2) if fault=='false_gap' else s.Rational(1)
    delta=(eta+s.sqrt(eta*eta+2*eps/m))/2;close(delta,s.Rational(1,2),'sharp asymmetric delta')
    close(J*C.conjugate()*J.T-(s.eye(2)-C),s.eye(2)/4,'complement defect')
    # Non-diagonal complex stationary case checks CAR covariance AND hole transpose.
    B=s.Matrix([[s.Rational(1,4),s.I/8],[-s.I/8,s.Rational(1,4)]])
    C4=s.diag(B,s.eye(2)-B.conjugate());a4=annihilators(4);rho4=qfree(C4)
    close(covariance(rho4,a4),C4,'original complex covariance')
    holes=[a4[0],a4[1],a4[2].T,a4[3].T]
    D=covariance(rho4,holes)
    predicted=s.diag(B,B.conjugate() if fault=='omit_hole_transpose' else B)
    close(D,predicted,'actual hole covariance transpose')
    sea=12;close(rho4[sea,sea],s.Rational(1225,4096),'complex four-mode sea weight')
    close((s.eye(4)-D).det(),rho4[sea,sea],'quasifree determinant')
    require(all(rho4[i,sea]==0 for i in range(16) if i!=sea),'sea is eigenvector')
    close(1-rho4[sea,sea],s.Rational(2871,4096),'exact finite trace distance')
    require(1-rho4[sea,sea]<=1-(1-s.Rational(3,8))**4,'dimension-dependent probability bound')
    # neutral test on complex eigenvector (max occupation3/8).
    f=s.Matrix([s.I,1,0,0])/s.sqrt(2);b4=s.Matrix.vstack(s.Matrix.hstack(s.zeros(2),-s.eye(2)),s.Matrix.hstack(s.eye(2),s.zeros(2)))
    g=b4*f.conjugate();af=sum((s.conjugate(f[j])*a4[j] for j in range(4)),s.zeros(16));ag=sum((s.conjugate(g[j])*a4[j] for j in range(4)),s.zeros(16));A=ag.conjugate().T*af
    G=sum(((1 if j<2 else -1)*a4[j].T*a4[j] for j in range(4)),s.zeros(16))
    close(s.simplify(s.trace(rho4*A.conjugate().T*(G*A-A*G))),-s.Rational(9,32),'complex sharp neutral witness')
    # Nonstationary pure one-particle counterexample: hole determinant cannot transfer.
    v=s.Matrix([0,1,1,0])/s.sqrt(2);rn=v*v.T;Cn=covariance(rn,aa)
    close(J*Cn*J.T,s.eye(2)-Cn,'nonstationary complement survives');require(H*Cn!=Cn*H,'stationarity missing')
    Dn=covariance(rn,[aa[0],aa[1].T]);close(rn[2,2],s.Rational(1,2),'actual nonstationary sea weight')
    close((s.eye(2)-Dn).det(),s.Rational(1,4),'wrong transferred determinant exposed')
    # Nonquasifree stationary complement control invalidates Wick despite covariance match.
    rc=s.diag(s.Rational(1,2),0,0,s.Rational(1,2));Cc=covariance(rc,aa);close(Cc,s.eye(2)/2,'nonquasifree covariance')
    A=aa[1].T*aa[0];N=aa[0].T*aa[0];hole=s.eye(4)-aa[1].T*aa[1]
    close(s.trace(rc*N*hole),0,'nonquasifree actual joint occupation')
    trial_rho=rc if fault=='replace_quasifree_state' else qfree(s.eye(2)/2)
    close(covariance(trial_rho,aa),s.eye(2)/2,'fixed trial covariance')
    close(s.trace(trial_rho*N*hole),s.Rational(1,4),'Wick premise guard')
    # finite portions of the infinite-volume counterexample
    t=s.Rational(1,4); M=2;bound=2*M*t*t
    for w in [s.Rational(0),s.Rational(1,3),s.Rational(1)]:require(2*(t*w)*(M*t*w)<=bound,'uniform band witness')
    require(1-(1-t)**16> s.Rational(9,10),'many-mode distance approaches one')

if __name__=='__main__':exercise(['bad_covariance','false_gap','omit_hole_transpose','replace_quasifree_state'],'k2092-robust-neutral-ground-selection')
