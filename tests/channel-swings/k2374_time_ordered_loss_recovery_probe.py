"""K2374 exact finite physical-support and cross-time Kraus discriminator.

Standard library only; no numerical exponential or finite difference.
Root integrator executes this candidate after review and serialized admission.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib, json, sys
R=Path(__file__).resolve().parents[2]
st='k2374-time-ordered-loss-recovery'
checks={}
def check(k,p):
    checks[k]=bool(p)
    assert p,k

def z(a=0,b=0):return F(a),F(b)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def conj(a):return a[0],-a[1]
def sumz(xs):
    s=z()
    for a in xs:s=add(s,a)
    return s
def eye(n):return [[z(i==j) for j in range(n)] for i in range(n)]
def zeros(n,m):return [[z() for _ in range(m)] for _ in range(n)]
def scale(A,c):return [[mul(c,a) for a in row] for row in A]
def plus(A,B):return [[add(a,b) for a,b in zip(x,y)] for x,y in zip(A,B)]
def adj(A):return [[conj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]
def mm(A,B):return [[sumz(mul(A[i][k],B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def gram(A,normalization=F(1)):return scale(mm(adj(A),A),z(normalization))
def scalar(A):return all(A[i][j]==(A[0][0] if i==j else z()) for i in range(len(A)) for j in range(len(A)))
def diag(ds):return [[z(ds[i] if i==j else 0) for j in range(len(ds))] for i in range(len(ds))]
I=eye(2);X=[[z(),z(1)],[z(1),z()]];Z=diag([1,-1])
labels=list(product(range(2),repeat=2))
def outer(r,b):return (r,r,r^b,r^b)
# None denotes vacuum. Both x_i and z_i vanish on vacuum.
def xp(w,i,j):
    if w[i] is None or w[j] is None:return None
    out=list(w);out[i]^=1;out[j]^=1
    return tuple(out)
def physical_X(words):
    A=zeros(len(words),len(words))
    for col,w in enumerate(words):
        N=sum(s is not None for s in w)
        for i,j in [(0,1),(2,3)]:
            out=xp(w,i,j)
            if out is not None:
                check(f'X_closure_{len(words)}_{col}_{i}_{str(w)}',out in words)
                row=words.index(out)
                A[row][col]=add(A[row][col],z(F(5-N,2)))
    return A
support=[outer(r,b) for r,b in labels]
H=physical_X(support)
expected=[[z(F(1,2) if b==1-c else 0) for s,c in labels] for r,b in labels]
check('physical_intact_X_restriction',H==expected)
V=[[z(b==c) for c in range(2)] for r,b in labels] # omits 1/sqrt2
check('code_intertwining',mm(H,V)==mm(V,X))
for j in range(4):
    for s in range(2):
        words=[]
        for b in range(2):
            r=s if j<2 else s^b
            w=list(outer(r,b));w[j]=None;words.append(tuple(w))
        check(f'physical_loss_X_{j}_{s}',physical_X(words)==X)
        zs=[]
        for w in words:
            vals=[0 if q is None else (-1)**q for q in w]
            N=sum(q is not None for q in w)
            zs.append(F(5-N,4)*(vals[0]+vals[1])*(vals[2]+vals[3]))
        check(f'physical_loss_Z_{j}_{s}',diag(zs)==Z)
H2=mm(H,H)
check('intact_cubic_identity',mm(H2,H)==H)
U=plus(plus(eye(4),scale(H2,z(-1))),scale(H,z(0,-1)))
check('actual_finite_pulse_unitary',gram(U)==eye(4))
check('actual_pulse_code_action',mm(U,V)==scale(mm(V,X),z(0,-1)))
D=diag([2,2,F(1,2),F(1,2)]);Di=diag([F(1,2),F(1,2),2,2])
core=mm(mm(mm(Di,U),D),V)
G=gram(core,F(1,2))
check('noncommuting_nojump_passes',G==scale(I,z(F(289,64))))
physicalG=scale(G,z(F(1,1024**2)))
check('physical_nojump_probability',physicalG==scale(I,z(F(289,67108864))))
# Loss at matched-pulse start/end, after removing only nonzero scalar factors.
Cpre=mm(D,V);Cpost=mm(U,Cpre)
start=mm(scale(X,z(0,-1)),Cpre[:2])
end=Cpost[:2]
check('actual_start_jump_matrix',start==scale(X,z(0,-2)))
check('actual_end_jump_matrix',end==plus(scale(I,z(F(3,4))),scale(X,z(0,F(-5,4)))))
check('start_self_Gram_scalar',gram(start)==scale(I,z(4)))
check('end_self_Gram_scalar',gram(end)==scale(I,z(F(17,8))))
Gcross=mm(adj(start),end)
check('cross_time_exact_value',Gcross==plus(scale(I,z(F(5,2))),scale(X,z(0,F(3,2)))))
check('cross_time_KL_fails',not scalar(Gcross))
eta_first=[(F(1,2),F(1,8))]*2+[(F(1,4),F(1,4))]*2
eta_last=[(b,a) for a,b in eta_first]
check('strict_positive_rates',all(0<a<1 for row in eta_first+eta_last for a in row))
check('integrated_rail_balance',all(a*c*F(1,2)==b*d*F(1,2)==F(1,32) for (a,b),(c,d) in zip(eta_first,eta_last)))
for n,(r,b) in enumerate(labels):
    p=F(1)
    for i,s in enumerate(outer(r,b)):p*=eta_first[i][s]
    d=[F(2),F(2),F(1,2),F(1,2)][n]
    check(f'first_physical_attenuation_{n}',p==(d/16)**2)
controls={}
def control(k,p):
    controls[k]=bool(p)
    assert p,k
balanced_pre=V
balanced_post=mm(U,V)
control('balanced_rates_cross_time_scalar',scalar(mm(adj(mm(scale(X,z(0,-1)),balanced_pre[:2])),balanced_post[:2])))
control('zero_pulse_cross_time_scalar',scalar(mm(adj(Cpre[:2]),Cpre[:2])))
control('zero_pulse_nojump_scalar',gram(mm(mm(Di,D),V),F(1,2))==I)
control('physical_offcode_extension_distinct',H!=[[z(r==s and b==1-c) for s,c in labels] for r,b in labels])
control('nonscalar_cross_not_a_self_Gram_failure',scalar(gram(start)) and scalar(gram(end)) and not scalar(Gcross))
# Positive schedule: two separately reversing idle exposures, with diagonal Z
# applied during the first, followed by a matched-rate finite X pulse. Split
# the X pulse at cos(theta)=3/5,sin(theta)=4/5. Scalar matched attenuation and
# sqrt(rate) are omitted only because nonzero trajectory scalar factors cannot
# alter KL. The unbalanced idle attenuation is retained on every physical word.
lam1=[(F(1,2),F(1,8))]*2+[(F(1,3),F(1,12))]*2
lam2=[(b,a) for a,b in lam1]
def attenuation(words,lams):
    values=[]
    for w in words:
        a=F(1)
        for i,s in enumerate(w):
            if s is not None:a*=lams[i][s]
        values.append(a)
    return diag(values)
def logical_xpulse(c,s):return plus(scale(I,z(c)),scale(X,z(0,-s)))
def intact_xpulse(c,s):return plus(plus(eye(4),scale(H2,z(c-1))),scale(H,z(0,-s)))
u1=logical_xpulse(F(3,5),F(4,5));u2=logical_xpulse(F(4,5),F(3,5))
U1=intact_xpulse(F(3,5),F(4,5));U2=intact_xpulse(F(4,5),F(3,5))
uz=scale(Z,z(0,-1));Uz=diag([1,-1,1,-1]);Uz=scale(Uz,z(0,-1))
fullops=[mm(attenuation(support,lam1),Uz),attenuation(support,lam2),U1,U2]
target=mm(mm(u2,u1),uz)
check('positive_schedule_noncommuting_XZ',mm(u2,uz)!=mm(uz,u2))
check('positive_schedule_actual_X_parts',mm(U2,U1)==U)
check('positive_schedule_strict_positive_rates',all(0<a<1 for row in lam1+lam2 for a in row))
for j in range(4):
    for s in range(2):
        words=[];select=zeros(2,4)
        for b in range(2):
            r=s if j<2 else s^b
            w=list(outer(r,b));w[j]=None;words.append(tuple(w))
            select[b][labels.index((r,b))]=z(1)
        lossops=[mm(attenuation(words,lam1),uz),attenuation(words,lam2),u1,u2]
        maps=[]
        for split in range(5):
            before=V
            for op in fullops[:split]:before=mm(op,before)
            branch=mm(select,before)
            for op in lossops[split:]:branch=mm(op,branch)
            maps.append(branch)
            check(f'positive_trajectory_target_{j}_{s}_{split}',scalar(mm(branch,adj(target))) and branch!=zeros(2,2))
        for t in range(5):
            for u in range(5):
                check(f'positive_complete_cross_time_{j}_{s}_{t}_{u}',scalar(mm(adj(maps[t]),maps[u])))
deps=['explorations/conditional-build/k2362-transparent-control-locality-2026-10-31.md','explorations/conditional-build/k2368-unequal-rail-recovery-2026-10-31.md','explorations/conditional-build/k2371-time-dependent-balance-ordering-2026-10-31.md',f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R))]
out=dict(result_id='K2374',checks=len(checks),check_names=list(checks),changed_schedule_or_scope_controls=controls,details=dict(nojump_Gram=[[[str(a),str(b)] for a,b in row] for row in physicalG],stripped_cross_time_Gram=[[[str(a),str(b)] for a,b in row] for row in Gcross]),scope='Written finite-block time-ordered iff theorem; exact finite physical-support and cross-time witness; no native GU or hardware certificate',dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
p=R/f'lab/process/{st}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print('PASS',out['checks'],len(controls))
