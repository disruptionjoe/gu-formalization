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

def circuit(fault):
    # Exact permutation on system(a,b), flags(u,v), record(r).
    U=s.zeros(32)
    for col in range(32):
        a,b,u,v,r=[(col>>k)&1 for k in [4,3,2,1,0]]
        u^=a if fault!='omit_copy_a' else 0; v^=b
        r^=((u|v) if fault=='wrong_boolean' else (1-(1-u)*v))
        if fault!='omit_cleanup': u^=a; v^=b
        if fault=='flip_record':r^=1
        row=(a<<4)|(b<<3)|(u<<2)|(v<<1)|r; U[row,col]=1
    return U

def checks(fault):
    I=s.eye(4); E=s.diag(1,0,1,1); P=[I-E,E]; U=circuit(fault)
    close(U.T*U,s.eye(32),'unitary reversible circuit')
    K=[s.Matrix(4,4,lambda i,j:U[8*i+e,8*j]) for e in range(8)]
    for a in range(4):
      for b in range(4):
        X=s.zeros(4);X[a,b]=1
        for j in range(2):
          actual=sum((K[e]*X*K[e].T for e in range(8) if e%2==j),s.zeros(4))
          close(actual,P[j]*X*P[j],'full circuit instrument matrix unit '+str((a,b,j)))
    # Clean construction's missing-cleanup counterexample.
    bad=circuit('omit_cleanup'); KB=[s.Matrix(4,4,lambda i,j:bad[8*i+e,8*j]) for e in range(8)]
    X=s.zeros(4);X[0,3]=1
    close(sum((k*X*k.T for k in KB),s.zeros(4)),s.zeros(4),'uncomputed labels destroy even coherence')
    # Sharp d=kr with k=3 and mixed rank r=2, d=6.
    tau=s.diag(s.Rational(1,3),s.Rational(2,3),0,0,0,0)
    W=[]
    for j in range(3):
      shift=j if fault=='overlap_supports' else 2*j
      W.append(s.Matrix(6,6,lambda a,b:int(a==(b+shift)%6)))
    for a in range(3):
      for b in range(3):
       for j in range(3):
        record=s.diag(*[int(z//2==j) for z in range(6)])
        close(s.trace(record*W[a]*tau*W[b].T),int(a==b==j),'mixed rank support instrument')
    # Noisy readable instrument with exactly correct nonselective backaction.
    q=s.Rational(1,4); tauq=(s.diag(s.Rational(2,3),s.Rational(1,3)) if fault=='wrong_bath' else s.diag(1-q,q)); Xq=s.Matrix([[0,1],[1,0]])
    Wq=[Xq if int(E[i,i]) else s.eye(2) for i in range(4)]
    for a in range(4):
      for b in range(4):
       for j in range(2):
        val=(Wq[a]*tauq*Wq[b].T)[j,j]
        ea,eb=int(E[a,a]),int(E[b,b]); expected=(1-q if j==ea else q) if ea==eb else 0
        close(val,expected,'noisy qubit record branch')
    close(2*min(tauq.diagonal())/2,q,'lambda record bound saturation')
    # Exact spectral rank optimization for a finite nonuniform bath.
    from itertools import product
    ev=[s.Rational(1,2),s.Rational(1,4),s.Rational(1,8),s.Rational(1,8)]
    S=lambda n:sum(ev[:n],s.Rational(0))
    profiles=[z for z in product(range(5),repeat=3) if sum(z)==4]
    best=max(sum(S(n) for n in z)/3 for z in profiles)
    close(best,(2*S(1)+S(2))/3,'balanced record ranks maximize spectral success')
    # k=d=3 cyclic shift saturates full-instrument floor without extra phase loss.
    lam=s.Rational(1,6); bath3=s.diag(1-2*lam,lam,lam)
    W3=[s.Matrix(3,3,lambda a,b:int(a==(b+j)%3)) for j in range(3)]
    for a in range(3):
      for b in range(3):
       for j in range(3):
        val=(W3[a]*bath3*W3[b].T)[j,j]
        expected=(1-2*lam if j==a else lam) if a==b else 0
        close(val,expected,'three-outcome symmetric label instrument')
    close(1-bath3[0,0],3*lam*(1-s.Rational(1,3)),'k3 spectral bound saturation')
    # Faithful maximally mixed bath: dephasing without readable record.
    mixed=s.eye(2)/2; Z=s.diag(1,-1)
    close(s.trace(mixed*Z),0,'unrecorded coherence erased')
    close(Z*mixed*Z,mixed,'physical record marginals identical')
    # Swap evades readout floor only by disturbing the system eigenstate.
    SW=s.Matrix(4,4,lambda i,j:int(i==2*(j%2)+j//2))
    swapped=SW*s.kronecker_product(s.diag(1,0),mixed)*SW.T
    system=s.Matrix(2,2,lambda i,j:sum(swapped[2*i+k,2*j+k] for k in range(2)))
    bath=s.Matrix(2,2,lambda i,j:sum(swapped[2*k+i,2*k+j] for k in range(2)))
    close(system,mixed,'SWAP disturbs system')
    close(bath,s.diag(1,0),'SWAP exact record-only success')
    require(system!=s.diag(1,0),'swap fails eigenstate nondemolition')

if __name__=='__main__':exercise(['omit_copy_a','wrong_boolean','omit_cleanup','flip_record','overlap_supports','wrong_bath'],'k2090-coherent-coarse-readout')
