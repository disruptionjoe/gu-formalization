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

def projector(v): return v*v.conjugate().T
def traced_second(rho):return s.Matrix(2,2,lambda i,j:sum(rho[2*i+k,2*j+k] for k in range(2)))
def checks(fault):
    for t in [s.Rational(0),s.Rational(1,3),s.Rational(1,2),s.Rational(3,4),s.Rational(1)]:
      g=(1-t*t)/(1+t*t); D=2*t/(1+t*t)
      ex=s.Matrix([1,0]);ey=s.Matrix([g,D if fault!='record_vector' else D/2]);over=(ey.T*ex)[0]
      close((ey.T*ey)[0],1,'record vector normalization')
      close(s.simplify(s.trace((projector(ex)-projector(ey))**2)/2),D*D,'record trace-distance squared')
      close(g*g+D*D,1,'pure total record identity')
      rho=s.ones(2)/2; actual=s.Matrix([[rho[0,0],over*rho[0,1]],[over*rho[1,0],rho[1,1]]])
      eps=t*t/(1+t*t)
      close(s.trace((actual-rho)**2)/2,eps*eps,'sharp input distance')
      close(1-2*eps,g,'antipodal recovery contraction saturation')
    # complex phase: actual upper-right equals gamma, recovery uses its conjugate phase.
    gamma=3*s.I/5;actual=s.Matrix([[s.Rational(1,2),gamma/2],[-gamma/2,s.Rational(1,2)]])
    phase=s.I if fault=='wrong_phase' else -s.I
    corrected=s.diag(phase,1)*actual*s.diag(phase,1).conjugate().T
    close(corrected[0,1],s.Rational(3,10),'calibrated complex phase')
    raw=actual-s.ones(2)/2;close(s.simplify(s.trace(raw*raw)/2),s.Rational(34,100),'complex raw error squared')
    # phase alone can produce raw error1 with no record.
    neg=s.Matrix([[s.Rational(1,2),-s.Rational(1,2)],[-s.Rational(1,2),s.Rational(1,2)]])
    close(s.trace((neg-s.ones(2)/2)**2)/2,1,'negative overlap raw error')
    # Inaccessible record can keep complete which-state information.
    ex=s.eye(4)[:,0];ey=s.eye(4)[:,1 if fault!='wrong_subrecord' else 2]
    close(traced_second(projector(ex)),traced_second(projector(ey)),'accessible marginals no converse')
    close((ey.T*ex)[0],0,'total record is orthogonal')
    # Ideal coarse record: overlap1 within sectors, zero between.
    labels=[1,0,1,1] if fault!='refine_sector' else [0,1,2,3]
    basis=s.eye(4); vectors=[basis[:,j] for j in labels]
    gram=s.Matrix(4,4,lambda i,j:(vectors[j].T*vectors[i])[0])
    expected=s.Matrix(4,4,lambda i,j:int([1,0,1,1][i]==[1,0,1,1][j]))
    close(gram,expected,'coarse sector Gram identity')
    # Mixed physical bath information hidden in purification.
    tau=s.eye(2)/2;Z=s.diag(1,-1)
    close(Z*tau*Z,tau,'equal mixed physical bath marginals');close(s.trace(tau*Z),0,'mixed bath complete dephasing')
    # Fully refined classical instrument kills BOTH equatorial sign states identically.
    plus=s.ones(2)/2;minus=s.diag(1,-1)*plus*s.diag(1,-1)
    close(s.diag(*plus.diagonal()),s.diag(*minus.diagonal()),'classical records cannot distinguish lost phase')

if __name__=='__main__':exercise(['record_vector','wrong_phase','wrong_subrecord','refine_sector'],'k2091-intrasector-record-disturbance')
