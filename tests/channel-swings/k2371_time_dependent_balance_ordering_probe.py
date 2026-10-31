"""K2371 exact physical-support and time-ordering counterexample.

Standard library only. Complex numbers are pairs of Fractions; no float
evaluation or finite differences; --write refreshes the saved evidence report.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,hashlib,sys
R=Path(__file__).resolve().parents[2]
st='k2371-time-dependent-balance-ordering'

checks = {}
def check(name, condition):
    checks[name] = bool(condition)
    assert condition, name

def z(a=0, b=0): return F(a), F(b)
def add(a,b): return a[0]+b[0],a[1]+b[1]
def neg(a): return -a[0],-a[1]
def mul(a,b): return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def conj(a): return a[0],-a[1]
def zeros(n,m): return [[z() for _ in range(m)] for _ in range(n)]
def eye(n): return [[z(int(i==j)) for j in range(n)] for i in range(n)]
def adj(A): return [[conj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]
def mm(A,B):
    return [[sumz(mul(A[i][k],B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def sumz(seq):
    out=z()
    for a in seq: out=add(out,a)
    return out
def scale(A,c): return [[mul(c,a) for a in row] for row in A]
def gram(A): return scale(mm(adj(A),A),z(F(1,2))) # V below omits 1/sqrt2
def scalar(A): return all(A[i][j]==(A[0][0] if i==j else z()) for i in range(len(A)) for j in range(len(A)))
def diag(ds): return [[z(ds[i] if i==j else 0) for j in range(len(ds))] for i in range(len(ds))]

# Four support strings embedded in the actual eight physical rail qubits.
def outer(r,b): return (r,r,r^b,r^b)
def rail_word(w): return tuple(v for s in w for v in (s,1-s))
labels=list(product(range(2),repeat=2))
support=[rail_word(outer(r,b)) for r,b in labels]
def xi(word,i):
    if word[2*i]+word[2*i+1]!=1: return None
    q=list(word);q[2*i]^=1;q[2*i+1]^=1
    return tuple(q)
def xpair(word,i,j):
    a=xi(word,i)
    return None if a is None else xi(a,j)
H=zeros(4,4)
for col,w in enumerate(support):
    N=sum(w)
    for i,j in [(0,1),(2,3)]:
        out=xpair(w,i,j)
        check(f'physical_support_{col}_{i}_{j}',out in support)
        row=support.index(out)
        H[row][col]=add(H[row][col],z(F(5-N,2)))
Pplus=[[F(1,2)]*2 for _ in range(2)]
expected=[[z(Pplus[r][s] if b==1-c else 0) for s,c in labels] for r,b in labels]
check('physical_X_ET_restriction',H==expected)
V=[[z(int(b==c)) for c in range(2)] for r,b in labels]
X=[[z(0),z(1)],[z(1),z(0)]]
check('code_X_intertwining',mm(H,V)==mm(V,X))
H2=mm(H,H)
check('physical_spectrum_0_plusminus1',mm(H2,H)==H)
# exp(-i*pi*H/2)=I-H^2-iH; no numerical exponential used.
U=[[sumz([eye(4)[i][j],neg(H2[i][j]),mul(z(0,-1),H[i][j])]) for j in range(4)] for i in range(4)]
check('finite_pulse_unitary',mm(adj(U),U)==eye(4))
check('finite_pulse_code_action',mm(U,V)==scale(mm(V,X),z(0,-1)))

# Duration1 exposure rates: mu=ln4, delta=(-ln2,-ln2,-ln3,-ln3).
# Survival values are exact, strictly between zero and one.
eta_first=[(F(1,2),F(1,8))]*2+[(F(3,4),F(1,12))]*2
eta_last=[(b,a) for a,b in eta_first]
check('strictly_positive_exposure_rates',all(0<q<1 for row in eta_first+eta_last for q in row))
check('pairwise_integrated_balance',all(a*c==b*d==F(1,16) for (a,b),(c,d) in zip(eta_first,eta_last)))
d=[F(6),F(2,3),F(1,6),F(3,2)]
for n,(r,b) in enumerate(labels):
    w=outer(r,b)
    p1=F(1);p2=F(1)
    for i,s in enumerate(w):p1*=eta_first[i][s];p2*=eta_last[i][s]
    check(f'physical_first_nojump_square_{n}',p1==(d[n]/16)**2)
    check(f'physical_last_nojump_square_{n}',p2==(1/(16*d[n]))**2)
check('pulse_positive_matched_survival',F(1,2)**4==F(1,4)**2)
check('total_pair_survival',all(a*c*F(1,2)==b*d0*F(1,2)==F(1,32) for (a,b),(c,d0) in zip(eta_first,eta_last)))

D=diag(d);Di=diag([1/x for x in d])
core=mm(mm(mm(Di,U),D),V)
G=gram(core)
target=[[z(F(860809,5184)),z(0,F(12025,216))],[z(0,-F(12025,216)),z(F(110809,5184))]]
check('exact_nojump_Gram',G==target)
check('non_scalar_nojump',not scalar(G))
physicalG=scale(G,z(F(1,1024**2)))
check('physical_probability_difference',physicalG[0][0][0]-physicalG[1][1][0]==F(15625,113246208))
check('physical_probability_range',all(0<physicalG[i][i][0]<1 for i in range(2)))

# Actual changed schedules, not mutations of a preasserted verdict.
check('remove_pulse_scalar',gram(mm(mm(Di,D),V))==eye(2))
Zdiag=diag([1,-1,1,-1])
UZ=scale(Zdiag,z(0,-1))
check('diagonal_Z_order_control',gram(mm(mm(mm(Di,UZ),D),V))==eye(2))
check('move_X_after_exposures',gram(mm(mm(mm(U,Di),D),V))==eye(2))
fakeU=[[z(0,-int(r==s and b==1-c)) for s,c in labels] for r,b in labels]
check('wrong_extension_matches_only_on_code',mm(fakeU,V)==mm(U,V) and fakeU!=U)
fakeG=gram(mm(mm(mm(Di,fakeU),D),V))
check('wrong_extension_deceptive_scalar',fakeG==scale(eye(2),z(F(3281,81))))

controls={k:checks.pop(k) for k in ['remove_pulse_scalar','diagonal_Z_order_control','move_X_after_exposures','wrong_extension_matches_only_on_code','wrong_extension_deceptive_scalar']}
deps=['explorations/conditional-build/k2368-unequal-rail-recovery-2026-10-31.md','explorations/conditional-build/k2362-transparent-control-locality-2026-10-31.md','explorations/conditional-build/k2365-serial-transparent-control-2026-10-31.md',f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R))]
out=dict(result_id='K2371',checks=len(checks),check_names=list(checks),changed_schedule_operator_controls=controls,details=dict(unscaled_Gram=[[[str(a),str(b)] for a,b in row] for row in G],physical_diagonal_difference=str(physicalG[0][0][0]-physicalG[1][1][0])),scope='Universal idle/diagonal trajectory proof; finite exact noncommuting physical-control counterexample; no measured hardware or native GU claim',dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
p=R/f'lab/process/{st}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print('PASS',out['checks'],len(controls))
