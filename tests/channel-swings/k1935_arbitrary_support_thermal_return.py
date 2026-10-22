"""Exact Bellman identities and full complex two-site channel controls for K1935."""
from pathlib import Path
import argparse,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/k1935-arbitrary-support-thermal-return.json'
def weights(t,d):
    Z=sum(t**b for b in range(4));L=sum(t**b for b in range(4-d))/Z
    return s.cancel(L),s.cancel(t**d*L)
def vectors():
    return [s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([1,1])/s.sqrt(2),s.Matrix([1,s.I])/s.sqrt(2)]
def shell(E,S,j,fault=None):
    occ=[b for b in range(4) if E-b in S]
    v=s.Matrix([[1,1],[1,-1]])*vectors()[j]/s.sqrt(2)
    if fault=='phase' and j==3:v=s.conjugate(v)
    U=s.eye(4)
    if len(occ)==1:
        col=occ[0];other=next(b for b in range(4) if b!=col);pairs=[(col,[col,other],other)]
    else:
        assert len(occ)==2
        heavy,light=sorted(occ);outside=[b for b in range(4) if b not in occ]
        pairs=[(heavy,[heavy,light],outside[0]),(light,outside,outside[1])]
        U=s.zeros(4)
    for col,rows,other in pairs:
        U[rows[0],col]=v[0];U[rows[1],col]=v[1]
        U[rows[0],other]=-s.conjugate(v[1]);U[rows[1],other]=s.conjugate(v[0])
    if fault=='pair':U[:,0]=U[:,1]
    return U

def symbolic():
    t=s.symbols('t',positive=True);A=1/(2*t*t);B=t*t/2
    q={d:s.cancel(weights(t,d)[0]/(1+weights(t,d)[1])) for d in (1,2,3)}
    p={d:s.cancel(weights(t,d)[1]/(1+weights(t,d)[0])) for d in (1,2,3)}
    X=q[1]*(1+q[3])/(1-q[1]*q[3]);X3=q[3]*(1+q[1])/(1-q[1]*q[3]);Y=p[1]*(1+p[3])/(1-p[1]*p[3]);Y3=p[3]*(1+p[1])/(1-p[1]*p[3]);C=q[3]*(1+A)
    Q=(2-t)+2*t*t*(1-t)+2*t**4*(1-t)+t**6*(2-t)+2*t**8
    R=(2-t)+t*t*(4-t)+t**4*(3-2*t)+t**6*(3-2*t)+t**8*(4-t)+2*t**10
    ids=[(A-X3,(2*t**4-t**3+2*t*t-t+1)/(2*t*t*(1+t*t)*(2*t*t+t+1))),
         (Y-B,t*((2-t)+2*t*t*(1-t)+t**4*(1-t))/(2*(1+t*t)*(t*t+t+2))),
         (B-Y3,t*t*(t**4-t**3+2*t*t-t+2)/(2*(1+t*t)*(t*t+t+2))),
         (A+B-X-Y3,Q/(2*t*t*(t*t+t+2)*(2*t*t+t+1))),
         (A+B-X3-Y,Q/(2*t*t*(t*t+t+2)*(2*t*t+t+1))),
         (A+B-C-Y,R/(2*t*(1+t*t)*(t*t+t+2)*(2*t**3+t*t+t+1))),
         (q[2]*(1+A),A),(p[2]*(1+B),B),
         (1/(2*(1+A+B)),t*t/(1+t*t)**2)]
    for a,b in ids:assert s.cancel(a-b)==0,'analytic rational identity'
    assert s.cancel(q[1]-q[2]-t*(2*t**3+t-1)/((1+2*t+2*t*t+2*t**3)*(1+2*t*t)))==0
    return len(ids)+1

def calculate(fault=None):
    count=symbolic();examples=[]
    def ck(ok,label):
        nonlocal count
        assert ok,label
        count+=1
    for t in (s.Rational(1,3),s.Rational(1,2),s.Rational(3,4)):
      for d in (1,2,3):
        L,H=weights(t,d);z=1+L+H;w=[L/z,(1+H)/z];S=[3,3+d];D=7+d;Z=sum(t**b for b in range(4));rstar=s.cancel(w[1]/2)
        if fault=='weights':w[0]+=s.Rational(1,100)
        ck(sum(w)==1,'normalization')
        outs=[[s.S(0)]*D for _ in range(4)]
        for E in range(3,7+d):
            occ=[b for b in range(4) if E-b in S]
            if not occ:continue
            us=[shell(E,S,j,fault) for j in range(4)]
            for j,U in enumerate(us):
                ck(all(s.simplify(x)==0 for x in U.H*U-s.eye(4)),'full shell unitary')
                for b in occ:
                    weight=w[S.index(E-b)]*t**b/Z
                    for a in range(4):outs[j][E-a]+=weight*s.simplify(abs(U[a,b])**2)
                    for k,V in enumerate(us):ck(s.simplify((V[:,b].H*U[:,b])[0]-(vectors()[k].H*vectors()[j])[0])==0,'complex target Gram')
        rs=[]
        for j,c in enumerate([s.Rational(1,2),s.Rational(1,2),1,s.Rational(1,2)]):
            out=[s.simplify(x) for x in outs[j]]
            ck(sum(out)==1 and all(x>=0 for x in out),'output probability')
            ck(s.simplify(out[S[0]]-c*(1-H)*w[0]-(1-c)*L*w[1])==0,'low support transport')
            ck(s.simplify(out[S[1]]-c*w[1])==0,'high support transport')
            rs.append(s.simplify(sum(abs(x-(w[S.index(a)] if a in S else 0)) for a,x in enumerate(out))/2))
        ck(max(rs)==rstar,'all-input attaining return')
        # Independent site-wise relaxation, check each linear segment breakpoint.
        for x in sorted(set([s.S(0),L/z,L/(L+H),(1+L)/z,s.S(1)])):
            m=max(H*x,L*(1-x));a=((1-H)*x+m)/2;b=((1-L)*(1-x)+m)/2
            ck(max(0,x-a)+max(0,1-x-b)>=rstar,'two-site lower bound')
        ck(rstar>t*t/(1+t*t)**2,'strict global floor')
        if t==s.Rational(3,4):examples.append({'gap':d,'weights':list(map(str,w)),'return':str(rstar)})
    ck(s.Rational(143,434)<s.Rational(17,50),'adjacent support improvement')
    return {'claim':'K1935','evidence_kind':'exact symbolic identities and finite full complex unitary controls; analytic universal proof in note','exact_controls':count,'t_three_quarters':examples,'global_infimum':'t^2/(1+t^2)^2','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=calculate()
    if args.write:REPORT.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r,indent=2))
