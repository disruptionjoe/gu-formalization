"""Independent shell/path and acyclic reward reconstruction for K1935."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib,json
import k1935_arbitrary_support_thermal_return as producer

def coefficients(t,d):
    low=sum(t**b for b in range(4-d))/sum(t**b for b in range(4))
    return low,t**d*low

def check_path(gaps,t,signs):
    n=len(gaps)+1;co=[coefficients(t,d) for d in gaps]
    B=[1-(co[i-1][0] if i else 0)-(co[i][1] if i<n-1 else 0) for i in range(n)]
    assert all(b>=0 for b in B),'disjoint shell-label weights'
    diag=[b/2 for b in B];edges=[[] for _ in range(n)]
    for i,(L,H) in enumerate(co):
        src,dst,weight=(i+1,i,L) if signs[i]==0 else (i,i+1,H)
        diag[src]+=weight/2;edges[src].append((dst,weight/2))
    assert all(d<=F(1,2) for d in diag)
    memo={}
    def visits(i):
        if i not in memo:memo[i]=(1+sum(w*visits(j) for j,w in edges[i]))/(1-diag[i])
        return memo[i]
    bound=(1+t*t)**2/(t*t)
    for i in range(n):assert visits(i)<bound,'global reward bound'
    # Direct shell grouping reproduces B plus L/H maxima, not only its formula.
    S=[3]
    for d in gaps:S.append(S[-1]+d)
    raw=[F((i*5+3)%11+1) for i in range(n)];v=[x/sum(raw) for x in raw]
    Z=sum(t**b for b in range(4));shells={}
    for i,a in enumerate(S):
        for b in range(4):shells.setdefault(a+b,[]).append((i,t**b/Z*v[i]))
    assert max(map(len,shells.values()))<=2
    direct=[F(0)]*n
    for cell in shells.values():
        top=max(w for i,w in cell)/2
        for i,w in cell:direct[i]+=top
    formula=[]
    for i in range(n):
        y=B[i]*v[i]
        if i:y+=max(co[i-1][1]*v[i-1],co[i-1][0]*v[i])
        if i<n-1:y+=max(co[i][1]*v[i],co[i][0]*v[i+1])
        formula.append(y/2)
    assert direct==formula,'physical shell sums versus path bound'
    return n+4

def independent():
    count=0
    for t in (F(1,4),F(1,2),F(3,4),F(9,10)):
      for k in range(5):
        for gaps in product((1,2,3),repeat=k):
          if any(a+b<4 for a,b in zip(gaps,gaps[1:])):continue
          for signs in product((0,1),repeat=k):count+=check_path(gaps,t,signs)
      # Independent Bellman inequalities at rational points; continuum proof in note.
      q={d:coefficients(t,d)[0]/(1+coefficients(t,d)[1]) for d in (1,2,3)}
      p={d:coefficients(t,d)[1]/(1+coefficients(t,d)[0]) for d in (1,2,3)}
      A=1/(2*t*t);B=t*t/2;X=q[1]*(1+q[3])/(1-q[1]*q[3]);X3=q[3]*(1+q[1])/(1-q[1]*q[3]);Y=p[1]*(1+p[3])/(1-p[1]*p[3]);Y3=p[3]*(1+p[1])/(1-p[1]*p[3])
      left={1:max(A,X),2:A,3:max(q[3]*(1+A),X3)};right={1:Y,2:B,3:Y3}
      for d in (1,2,3):
        assert left[d]>=q[d]*(1+max(left[e] for e in (1,2,3) if d+e>=4))
        assert right[d]>=p[d]*(1+max(right[e] for e in (1,2,3) if d+e>=4));count+=2
        for e in (1,2,3):
          if d+e>=4:assert left[d]+right[e]<=A+B;count+=1
      # Four-shell capacities reject triple occupancy, including nonadjacent gaps1+2.
      for bad in ([3,4,5],[3,4,6]):
        occupancies=[sum(a<=E<=a+3 for a in bad) for E in range(10)]
        assert max(occupancies)>2;count+=1
    return count

def main():
    count=independent();base=producer.calculate();assert json.loads(producer.REPORT.read_text())==base,'report baseline'
    assert base['source_sha256']==hashlib.sha256(Path(producer.__file__).read_bytes()).hexdigest()
    for fault in ('weights','phase','pair'):
        try:producer.calculate(fault)
        except AssertionError as e:print('DETECTED mathematical input',fault,str(e))
        else:raise AssertionError('missed '+fault)
    try:check_path((1,1),F(1,2),(0,1))
    except AssertionError as e:print('DETECTED mathematical input triple support',str(e))
    else:raise AssertionError('missed triple support')
    for key in ('global_infimum','source_sha256'):
        bad=dict(base);bad[key]='corrupted'
        try:assert bad==base,key
        except AssertionError:print('DETECTED reporting',key)
        else:raise AssertionError('missed '+key)
    print('PASS independent exact controls',count,'mathematical faults 4; report/pin faults 2')
if __name__=='__main__':main()
