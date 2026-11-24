#!/usr/bin/env python3
"""Exact sparse-Clifford controls for all metric normal extensions.

No large matrix elimination. Rational native shape coefficients come from the
already-owned trace-reversed symmetric-metric basis. Clifford words are exact
in the faithful complex Cl14 algebra. The written argument supplies the
arbitrary-endomorphism uniqueness theorem; this probe checks its coefficients,
injection certificate, torsion witness and failing controls.
"""
import argparse
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

ap=argparse.ArgumentParser()
ap.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2])
ap.add_argument('--output',type=Path)
args=ap.parse_args()
checks=[]
def check(name,condition):
    checks.append({'name':name,'pass':bool(condition)})
    if not condition: raise AssertionError(name)

path=args.repo/'tests/channel-swings/joe_directed_sa1_soldered_ad_selector.py'
spec=importlib.util.spec_from_file_location('native_geometry',path)
geometry=importlib.util.module_from_spec(spec)
spec.loader.exec_module(geometry)
geometry.MUT=''
T,gram=geometry.adapted_congruence(geometry.dewitt(F(1,2)))
normals=[geometry.vec_to_sym([T[r][i] for r in range(10)]) for i in range(10)]
diag=[gram[i][i] for i in range(10)]
eta=[F(-1),F(1),F(1),F(1)]
metric=eta+diag
check('native trace-reversed normal Gram',diag==[2,2,2,2,6,12,-2,-2,-2,-4])
I={0:F(1)}
def clean(x):return {k:v for k,v in x.items() if v}
def scale(t,x):return clean({k:F(t)*v for k,v in x.items()})
def add(*xs):
    out={}
    for x in xs:
        for k,v in x.items():out[k]=out.get(k,F(0))+v
    return clean(out)
def mul(x,y):
    out={}
    for u,a in x.items():
        for v,b in y.items():
            parity=sum((v&((1<<j)-1)).bit_count() for j in range(14) if u&(1<<j))
            c=a*b*(-1 if parity%2 else 1)
            both=u&v
            for j in range(14):
                if both&(1<<j):c*=metric[j]
            mask=u^v
            out[mask]=out.get(mask,F(0))+c
    return clean(out)
gamma=[{1<<j:F(1)} for j in range(14)]
omega=I
for j in range(4):omega=mul(omega,gamma[j])
check('horizontal volume squares to minus one',mul(omega,omega)==scale(-1,I))
check('normal Clifford commutes with horizontal volume',all(mul(omega,gamma[j])==mul(gamma[j],omega) for j in range(4,14)))
check('horizontal Clifford anticommutes with volume',all(not add(mul(omega,gamma[j]),mul(gamma[j],omega)) for j in range(4)))
check('all native Clifford squares',all(mul(gamma[j],gamma[j])==scale(metric[j],I) for j in range(14)))
check('all distinct native Clifford anticommutators',all(not add(mul(gamma[j],gamma[k]),mul(gamma[k],gamma[j])) for j in range(14) for k in range(j)))
# No large spinor matrices: each entry is a sparse Clifford word.
h,m,n=4,10,14
a,c0,e,g=F(12),F(-1),F(2),F(3)
def zeros(rows,cols):return [[{} for _ in range(cols)] for _ in range(rows)]
def scalar_zeros(rows,cols):return [[F(0) for _ in range(cols)] for _ in range(rows)]
def grade_residual(D,vol):
    signs=[1]*4+[-1,-1]
    return [[add(scale(signs[i],mul(vol,D[i][j])),scale(signs[j],mul(D[i][j],vol))) for j in range(6)] for i in range(6)]
def iszero(D):return all(not x for row in D for x in row)
def compose(A,B):
    return [[add(*(mul(A[i][k],B[k][j]) for k in range(len(B)))) for j in range(len(B[0]))] for i in range(len(A))]
shapes=[[[ -F(1,2)*eta[i]*normals[r][i][j] for j in range(h)] for i in range(h)] for r in range(m)]
mean_coeff=[sum(shapes[r][j][j] for j in range(h))/diag[r] for r in range(m)]
mean=add(*(scale(mean_coeff[r],gamma[h+r]) for r in range(m)))
check('actual mean Clifford square minus one',mul(mean,mean)==scale(-1,I))
base_B=[scalar_zeros(n,n) for _ in range(n)]
for u in range(h):
    for v in range(h):
        for r in range(m):base_B[u][h+r][v]=normals[r][u][v]/(2*diag[r])
    for r in range(m):
        for v in range(h):base_B[u][v][h+r]=shapes[r][v][u]

def family(A,ell):
    B=[[row[:] for row in mat] for mat in base_B]
    for r in range(m):
        for i in range(h):
            for j in range(h):B[h+r][i][j]=A[r][i][j]
            B[h+r][h+r][i]=ell[i]
            B[h+r][i][h+r]=-diag[r]*eta[i]*ell[i]
    return B

def metric_skew(B):
    return all(metric[i]*mat[i][j]+metric[j]*mat[j][i]==0 for mat in B for i in range(n) for j in range(n))

def lower_raw(B):
    # T(a,c)^j = B_a(e_c)^j-B_c(e_a)^j; exterior sign is PLUS.
    C=[[add(*(scale((B[u][j][v]-B[v][j][u])/metric[u],gamma[u]) for u in range(n))) for j in range(n)] for v in range(n)]
    GC=[add(*(scale(1/metric[v],mul(gamma[v],C[v][j])) for v in range(n))) for j in range(n)]
    V=[[add(scale(a,C[v][j]),scale(c0/2,mul(gamma[v],GC[j]))) for j in range(n)] for v in range(n)]
    w=[sum(B[u][j][u]/metric[u] for u in range(n))+(mean_coeff[j-h] if j>=h else 0) for j in range(n)]
    # Actual receiver is b, sigma=Gamma_N zeta_N, nu.
    Q=[row[:] for row in V[:h]]
    Q.append([add(*(scale(1/diag[r],mul(gamma[h+r],V[h+r][j])) for r in range(m))) for j in range(n)])
    Q.append([scale(g*w[j],I) for j in range(n)])
    return Q,w

PK=[[add(I if r==s else {},scale(-1/(m*diag[s]),mul(gamma[h+r],gamma[h+s]))) for s in range(m)] for r in range(m)]
Lift=zeros(n,6)
for j in range(h):Lift[j][j]=I
for r in range(m):Lift[h+r][4]=scale(F(1,m),gamma[h+r])
def hidden_defect(Q):return compose([row[h:] for row in Q],PK)
def observed(Q):return compose(Q,Lift)
def predicted(A,ell):
    AL=[[add(*(scale(eta[u]*(shapes[r][j][u]-A[r][j][u]),gamma[u]) for u in range(h))) for j in range(h)] for r in range(m)]
    Fr=[add(*(scale(1/diag[r],mul(gamma[h+r],AL[r][j])) for r in range(m))) for j in range(h)]
    CH=[[add(*(scale(-(shapes[r][j][i]-A[r][j][i])/diag[r],gamma[h+r]) for r in range(m))) for j in range(h)] for i in range(h)]
    cv=add(*(scale(eta[i]*ell[i],gamma[i]) for i in range(h)))
    V=zeros(6,6)
    for i in range(h):
        for j in range(h):V[i][j]=add(scale(a,CH[i][j]),scale(c0,mul(gamma[i],Fr[j])))
        V[i][4]=add(scale(a*ell[i],I),scale(c0,mul(gamma[i],cv)))
    for j in range(h):
        V[4][j]=scale(a+m*c0,Fr[j])
        V[5][j]=scale(-m*g*eta[j]*ell[j],I)
    V[4][4]=scale(a+m*c0,cv)
    return V,Fr,CH

def A0():return [scalar_zeros(h,h) for _ in range(m)]
ell0=[F(0)]*h
ambient=I
for j in range(n):ambient=mul(ambient,gamma[j])
Omega=scale(F(1,192),ambient)
check('ambient grade has square one',mul(Omega,Omega)==I)
check('ambient and horizontal grades differ',Omega!=omega)
B0=family(A0(),ell0);Q0,w0=lower_raw(B0);V0=observed(Q0)
check('base full connection is metric',metric_skew(B0))
check('base quotient closure retained',iszero(hidden_defect(Q0)))
check('base lower formula retained',V0==predicted(A0(),ell0)[0])
check('base horizontal grading defect nonzero',not iszero(grade_residual(V0,omega)))
check('base ambient grading survives',iszero(grade_residual(V0,Omega)))
check('weighted base scalar trace is zero',all(x==0 for x in w0))

# Exhaustive basis controls in the64-dimensional classified pointwise space.
# Exhaustion itself is the written factorization/Clifford-grade theorem.
for r in range(m):
    for i in range(h):
        for j in range(i+1,h):
            A=A0();A[r][i][j]=eta[i];A[r][j][i]=-eta[j]
            B=family(A,ell0);Q,w=lower_raw(B);V=observed(Q);Vp,Fr,CH=predicted(A,ell0)
            name=f'A[{r};{i},{j}]'
            check(name+' metric and all quotient rows',metric_skew(B) and iszero(hidden_defect(Q)))
            check(name+' complete observed lower formula',V==Vp)
            check(name+' horizontal trace contraction identity',all(add(*(scale(eta[u],mul(gamma[u],CH[u][k])) for u in range(h)))==Fr[k] for k in range(h)))
            Jw=add(*(mul(Fr[k],gamma[k]) for k in range(h)))
            degree1={blade:coef for blade,coef in Jw.items() if blade.bit_count()==1}
            check(name+' fixed mean degree one remains',degree1==mean)
            check(name+' horizontal fails and ambient survives',not iszero(grade_residual(V,omega)) and iszero(grade_residual(V,Omega)))
for j in range(h):
    ell=[F(i==j) for i in range(h)];B=family(A0(),ell);Q,w=lower_raw(B);V=observed(Q);Vp,Fr,CH=predicted(A0(),ell)
    name=f'ell[{j}]'
    check(name+' metric and all quotient rows',metric_skew(B) and iszero(hidden_defect(Q)))
    check(name+' complete observed lower formula',V==Vp)
    check(name+' scalar trace exactly horizontal',all(w[i]==(-m*eta[i]*ell[i] if i<h else 0) for i in range(n)))
    DV=[[add(V[i][k],scale(-1,V0[i][k])) for k in range(6)] for i in range(6)]
    check(name+' new lower terms horizontal-odd',iszero(grade_residual(DV,omega)))
    check(name+' ambient grade survives',iszero(grade_residual(V,Omega)))

# Nonadmissible but metric plants. Checking q is indispensable before grading.
Cplant=family(A0(),ell0)
Cplant[h][h+1][h+2]=diag[2]
Cplant[h][h+2][h+1]=-diag[1]
QC,wC=lower_raw(Cplant)
check('normal-normal plant remains metric',metric_skew(Cplant))
check('normal-normal plant breaks actual quotient',not iszero(hidden_defect(QC)))
Mplant=family(A0(),ell0)
Mplant[h][h+1][0]=1
Mplant[h][0][h+1]=-diag[1]/eta[0]
QM,wM=lower_raw(Mplant)
check('nonscalar mixed plant remains metric',metric_skew(Mplant))
check('nonscalar mixed plant breaks actual quotient',not iszero(hidden_defect(QM)))
# Matching S_n by a putative skew A_n would remove the selected witness,
# but the resulting B_n is not a metric connection: reject that fake repair.
Bfake=family(shapes,ell0)
check('shape-equals-skew fitted plant violates metricity',not metric_skew(Bfake))

# Dimensions, signature and the observed lower scalar coefficient are exact.
check('metric normal space dimension910',m*(n*(n-1)//2)==910)
check('classified metric normal space dimension64',m*(h*(h-1)//2)+h==64)
check('stable sigma coefficient nonzero a over six',a+m*c0==a/6 and a/6!=0)
check('stable tau coefficient nonzero five a over six',2*a+n*c0==5*a/6 and 5*a/6!=0)
result={'status':'PASS','checks_passed':len(checks),'checks':checks,
 'arithmetic':'exact rational sparse Clifford words; no spinor matrix elimination',
 'family':'R6-metric-normal-coherent: all metric B_n, held tangent split and coherent normal jets',
 'classified_dimension':64,'unconstrained_dimension':910,
 'basis_controls':{'horizontal_skew':60,'mixed_scalar':4},
 'quotient_classification':'B_n X=A_n X+ell(X)n; B_n m=-K(n,m)ell#; A_n g-skew',
 'horizontal_grade':'incompatible with actual nonzero shape for every quotient-admissible member',
 'ambient_grade':'survives compatible metric-spin family and descends whenever q does',
 'rank_ceiling':'fixed nonzero Clifford-degree witness; no uniform rank128 claim',
 'claim_ceiling':'same-horizontal-readout realization only; no full source parent, classC, physical index or GU verdict'}
if args.output:
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
