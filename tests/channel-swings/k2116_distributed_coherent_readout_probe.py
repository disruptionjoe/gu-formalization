#!/usr/bin/env python3
"""Exact finite controls; continuum statements require the linked written proofs."""
import sympy as s
I=s.I

def kron(*xs):
    out=s.Matrix([[1]])
    for x in xs: out=s.kronecker_product(out,x)
    return out

def annihilators(n, bosonic=False):
    a=s.Matrix([[0,1],[0,0]]);z=s.diag(1,-1);eye=s.eye(2)
    return [kron(*([eye if bosonic else z]*j+[a]+[eye]*(n-j-1))) for j in range(n)]

def equal(a,b):
    if isinstance(a,s.MatrixBase): return all(s.simplify(v)==0 for v in a-b)
    return s.simplify(a-b)==0

def run_suite(checks, faults):
    baseline=checks(None)
    if baseline: print('[FAIL] baseline',baseline);raise SystemExit(1)
    print('PASS clean exact finite baseline; sympy',s.__version__)
    for fault in faults:
        try: failed=checks(fault)
        except Exception as exc: print('CRASH-NOT-DETECTION',fault,repr(exc));raise SystemExit(1)
        if not failed: print('[FAIL] undetected',fault);raise SystemExit(1)
        print('DETECTED',fault,':','; '.join(failed))
    print('PASS',len(faults),'genuine input/machinery faults; no continuum certification')


def checks(fault):
    failures=[]
    def check(ok,msg):
        if not ok:failures.append(msg)
    eye=s.eye(2);Z=s.diag(1,-1);R=kron(Z,Z);P={q:(s.eye(4)+q*R)/2 for q in [-1,1]}
    U=s.zeros(16)
    for a in [0,1]:
      for b in [0,1]:
        v=s.zeros(4,1);v[2*a+b]=1
        B=eye if fault=='omit_bob_control' else Z**b
        U+=kron(Z**a,B,v*v.T)
    def kraus(c,d):
      eta=s.Matrix([c,0,0,(-d if fault=='resource_phase' else d)])
      ans={}
      for x in [-1,1]:
        for y in [-1,1]:
          vx=s.Matrix([1,x])/s.sqrt(2);vy=s.Matrix([1,y])/s.sqrt(2)
          if fault=='measure_z':vx=s.Matrix([1,0]) if x==1 else s.Matrix([0,1]);vy=s.Matrix([1,0]) if y==1 else s.Matrix([0,1])
          ans[x,y]=kron(s.eye(4),kron(vx,vy).H)*U*kron(s.eye(4),eta)
      return ans
    ks=kraus(1/s.sqrt(2),1/s.sqrt(2))
    for xy,K in ks.items():check(equal(K,P[xy[0]*xy[1]]/s.sqrt(2)),'derived joint ancilla Kraus operator')
    def branch(ks,A,q):
      val=s.zeros(4)
      for (x,y),K in ks.items():
        if (x if fault=='wrong_record_group' else x*y)==q:val+=K*A*K.H
      if fault=='fine_system_readout':val=s.diag(*[val[j,j] for j in range(4)])
      return val
    for i in range(4):
      for j in range(4):
        M=s.zeros(4);M[i,j]=1
        for q in [-1,1]:check(equal(branch(ks,M,q),P[q]*M*P[q]),'full recorded map matrix units')
    for x in [-1,1]:check(equal(sum((ks[x,y].H*ks[x,y] for y in [-1,1]),s.zeros(4)),s.eye(4)/2),'uniform single-site record')
    c=s.Rational(3,5);d=s.Rational(4,5);badks=kraus(c,d)
    v=s.Matrix([1,1,0,0])/s.sqrt(2);rho=v*v.H;dist=0
    for q in [-1,1]:
      diff=branch(badks,rho,q)-P[q]*rho*P[q]
      dist+=sum(abs(ev)*n for ev,n in diff.eigenvals().items())/2
    check(equal(dist,1/(5*s.sqrt(2))),'exact full-instrument Schmidt error')
    # Eigenstate label error is smaller than coherent error; both evaluated from Kraus.
    rho=s.diag(1,0,0,0);wrong=s.trace(branch(badks,rho,-1))
    check(equal(wrong,s.Rational(1,50)),'record-only error is squared coherent error')
    plus=s.Matrix([1,1])/s.sqrt(2);product=kron(plus,plus);rho=product*product.H
    for q in [-1,1]:
      out=2*P[q]*rho*P[q]
      marginal=s.Matrix([[out[0,0]+out[1,1],out[0,2]+out[1,3]],[out[2,0]+out[3,1],out[2,2]+out[3,3]]])
      check(equal(marginal,s.eye(2)/2),'one-ebit output from product input')
    return failures

if __name__=='__main__':run_suite(checks,['omit_bob_control','resource_phase','measure_z','wrong_record_group','fine_system_readout'])
