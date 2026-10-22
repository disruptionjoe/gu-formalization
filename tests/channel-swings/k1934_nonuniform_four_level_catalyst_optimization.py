"""Exact unequal-weight shell construction and fixed-protocol optimization."""
from pathlib import Path
import hashlib,json
import sympy as s
import k1932_four_level_bath_catalyst_return as old
ROOT=Path(__file__).resolve().parents[2]
def weights(N,t):
    z=1+2*t*t
    return [s.cancel(z**i/sum(z**k for k in range(N))) for i in range(N)]
def optimum(N,t):return s.cancel(1/(2*sum((1+2*t*t)**(-k) for k in range(N))))
def transport(N,t,c):
    L=1/(1+t*t);H=1-L;P=s.zeros(N)
    if N==1:P[0,0]=c;return P
    for i in range(N-1):P[i,i]=c*L;P[i,i+1]=(1-c)*L
    P[N-1,N-1]=c
    return P

def output(N,t,w,j,fault=None):
    S=list(range(3,3+2*N,2));d=2*N+5;Z=sum(t**b for b in range(4));out=[s.S(0)]*d
    for i,n in enumerate(S):
        for b in range(4):
            E=n+b;occupied=[bb for bb in range(4) if E-bb in S]
            U=old.edge_shell(4,b,j,fault) if len(occupied)==1 else old.shell(1,(E-1)%2,j,fault)
            for a in range(4):out[E-a]+=t**b/Z*w[i]*s.simplify(s.conjugate(U[a,b])*U[a,b])
    return S,[s.simplify(x) for x in out]

def root_data(N,t,a):
    L=1/(1+t*t);H=1-L;q=L/(2-L);p=H/(2-H)
    raw=[q**(a-i) if i<=a else p**(i-a) for i in range(N)]
    Z=sum(raw);return [s.cancel(v/Z) for v in raw],s.cancel(1/(2*Z))
def best_root(N,t):
    return min((root_data(N,t,a)[1],a) for a in range(N))
def oriented_matrix(N,t,bits):
    L=1/(1+t*t);H=1-L;T=s.zeros(N)
    T[0,0]+=L/2;T[N-1,N-1]+=H/2
    for i,bit in enumerate(bits):
        col=i+1 if bit==0 else i;weight=L if bit==0 else H
        T[i,col]+=weight/2;T[i+1,col]+=weight/2
    return T

def rooted_unitary(E,S,a,j):
    occ=[b for b in range(4) if E-b in S]
    if len(occ)==1:return old.edge_shell(4,occ[0],j)
    low,high=occ;right=S.index(E-low)
    # Edges left of root send probability left; right edges send it right.
    heavy=low if right<=a else high;light=high if heavy==low else low
    outside=[b for b in range(4) if b not in occ]
    v=s.Matrix([[1,1],[1,-1]])*old.vectors()[j]/s.sqrt(2)
    U=s.zeros(4)
    for col,rows,other in [(heavy,[heavy,light],outside[0]),(light,outside,outside[1])]:
        U[rows[0],col]=v[0];U[rows[1],col]=v[1]
        U[rows[0],other]=-s.conjugate(v[1]);U[rows[1],other]=s.conjugate(v[0])
    return U

def rooted_output(N,t,a,w,j):
    S=list(range(3,3+2*N,2));out=[s.S(0)]*(2*N+5);Z=sum(t**b for b in range(4))
    for i,n in enumerate(S):
      for b in range(4):
        E=n+b;U=rooted_unitary(E,S,a,j)
        for bout in range(4):out[E-bout]+=w[i]*t**b/Z*s.simplify(abs(U[bout,b])**2)
    return S,[s.simplify(v) for v in out]

def calculate(fault=None):
    count=0
    def ck(ok,msg):
        nonlocal count
        assert ok,msg
        count+=1
    cases=[]
    for N in (1,2,3,5):
      for t in (s.Rational(1,3),s.Rational(1,2),s.Rational(3,4)):
        w=weights(N,t)
        if fault=='weights':w[0]+=s.Rational(1,100)
        ck(sum(w)==1,'preparation normalization')
        rs=[]
        for j,c in enumerate([s.Rational(1,2),s.Rational(1,2),1,s.Rational(1,2)]):
            S,out=output(N,t,w,j,fault)
            ck(sum(out)==1 and all(x>=0 for x in out),'output probability')
            ck(s.Matrix([out[n] for n in S])==transport(N,t,c)*s.Matrix(w),'full unitary versus reduced transport')
            r=sum(abs(x-(w[S.index(n)] if n in S else 0)) for n,x in enumerate(out))/2
            rs.append(r)
        ck(max(rs)==optimum(N,t),'worst input optimum attained')
        M=s.eye(N)-transport(N,t,s.Rational(1,2));wi=(s.ones(1,N)*M.inv());f=wi/wi[N-1]
        if fault=='dual':f[0,0]+=s.Rational(1,100)
        ck(all(0<x<=1 for x in f),'dual effect in unit interval')
        ck(f*M==s.ones(1,N)*optimum(N,t),'exact dual certificate')
        ck(all((M*s.Matrix(w))[i]==0 for i in range(N-1)),'only terminal deficit')
        ck(s.simplify(s.Rational(1,2)*w[-1]-optimum(N,t))==0,'terminal deficit value')
        if N>1:ck(optimum(N,t)<t*t/(1+t*t)+(s.Rational(1,2)-t*t/(1+t*t))/N,'strict uniform improvement')
        # Reuse shell formula but check every occupied complex matrix-unit coefficient.
        for E in range(3,2*N+5):
            occ=[b for b in range(4) if E-b in S]
            if not occ:continue
            us=[old.edge_shell(4,occ[0],j,fault) if len(occ)==1 else old.shell(1,(E-1)%2,j,fault) for j in range(4)]
            for j,U in enumerate(us):
                ck(old.zero(U.H*U-s.eye(4)),'unitary shell')
                for b in occ:
                    for k,V in enumerate(us):ck(s.simplify((V[:,b].H*U[:,b])[0]-(old.vectors()[k].H*old.vectors()[j])[0])==0,'complex channel coefficient')
        if t==s.Rational(1,2):cases.append({'N':N,'weights':list(map(str,w)),'return':str(max(rs)),'uniform_return':str(t*t/(1+t*t)+(s.Rational(1,2)-t*t/(1+t*t))/N)})
        # All-unitary two-site relaxation: each physical site gets at most the
    # largest eigenvalue in each occupied shell. Check both ordering regions.
    for u in (s.Rational(1,9),s.Rational(1,4),s.Rational(9,16)):
        L=1/(1+u);H=1-L;best=s.Rational(1,2)-L/4
        candidates=[s.S(0),L/2,L,1-H/2,s.S(1)]
        for x in candidates:
            mx=max(L*(1-x),H*x)
            bound=max(0,x-(L*x+mx)/2)+max(0,1-x-(H*(1-x)+mx)/2)
            ck(bound>=best,'two-site universal piecewise lower bound')
        ck(best==optimum(2,s.sqrt(u)),'two-site sharp value')
    # Stronger outcome-released theorem: optimize all conserving unitaries on S.
    import itertools
    rooted=[]
    for N in (1,2,3,5,7):
      for t in (s.Rational(1,2),s.Rational(2,3)):
        r,a=best_root(N,t);w,_=root_data(N,t,a);S=list(range(3,3+2*N,2))
        bits=tuple(0 if i<a else 1 for i in range(N-1));Q=oriented_matrix(N,t,bits)
        deficit=(s.eye(N)-Q)*s.Matrix(w)
        ck(deficit==s.Matrix([r if i==a else 0 for i in range(N)]),'rooted exact dual attainment')
        rs=[]
        for j in range(4):
            SS,out=rooted_output(N,t,(a+1)%N if fault=='root' else a,w,j)
            ck(sum(out)==1,'rooted full matrix normalization')
            rs.append(sum(abs(v-(w[SS.index(i)] if i in SS else 0)) for i,v in enumerate(out))/2)
            if j==0:ck(s.Matrix([out[n] for n in S])==Q*s.Matrix(w),'rooted unitary transport')
        ck(max(rs)==r,'rooted worst input return')
        for E in range(3,2*N+5):
            occ=[b for b in range(4) if E-b in S]
            if not occ:continue
            us=[rooted_unitary(E,S,a,j) for j in range(4)]
            for j,U in enumerate(us):
                ck(old.zero(U.H*U-s.eye(4)),'rooted unitary')
                for b in occ:
                    for k,V in enumerate(us):ck(s.simplify((V[:,b].H*U[:,b])[0]-(old.vectors()[k].H*old.vectors()[j])[0])==0,'rooted full complex channel')
        if t==s.Rational(1,2):rooted.append({'N':N,'root_index_zero_based':a,'return':str(r)})
    for N in range(1,7):
      t=s.Rational(1,2);r,a=best_root(N,t)
      for bits in itertools.product((0,1),repeat=N-1):
        Q=oriented_matrix(N,t,bits);M=s.eye(N)-Q
        w=s.ones(1,N)*M.inv()
        ck(all(v>0 for v in w),'all orientations inverse nonnegative column sums')
        ck(max(w)<=1/r,'all orientations root bound')
    ck(best_root(7,s.Rational(1,2))[0]<optimum(7,s.Rational(1,2)),'interior root strictly beats endpoint')
    return {'exact_checks':count,'cases':cases,'all_unitary_rooted_cases':rooted,'all_unitary_fixed_support_optimum':'1/(2 max_{a+b=N-1} [1+sum_{k=1}^a q^k+sum_{k=1}^b p^k]); q=1/(1+2u),p=u/(2+u)','all_unitary_fixed_support_limit':'u/(1+u)^2','optimum':'1/(2 sum_{k=0}^{N-1}(1+2t^2)^(-k))','limiting_return':'t^2/(1+2t^2)','scope':'fixed boundary-repaired K1932 protocol and odd support; all preparation states on that support via K1933','all_unitaries_optimum_claimed':'all N for fixed consecutive odd support and fixed bath/spectra; not arbitrary supports', 'two_site_global_optimum':'(1+2t^2)/(4(1+t^2))'}
def report():
    x=calculate();x['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();x['dependency_sha256']=hashlib.sha256(Path(old.__file__).read_bytes()).hexdigest();x['evidence_kind']='finite exact matrices/rationals; universal theorem in linked note';return x
if __name__=='__main__':
    import sys
    r=report()
    if '--write' in sys.argv:(ROOT/'lab/process/k1934-nonuniform-four-level-catalyst-optimization.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r))
