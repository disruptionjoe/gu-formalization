#!/usr/bin/env python3
"""Exact sparse-Clifford controls for the six-spinor grading theorem.

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
# chi_H=i omega. All oddness identities below are homogeneous in chi,
# so checking omega is equivalent over Q(i), and chi_H^2=1 follows above.
def zero_matrix():return [[{} for _ in range(6)] for _ in range(6)]
sign=[1,1,1,1,-1,-1]
def anticomm_grade(D,sgn=sign):
    return [[add(scale(sgn[j],mul(omega,D[j][k])),scale(sgn[k],mul(D[j][k],omega))) for k in range(6)] for j in range(6)]
def iszero(D):return all(not x for row in D for x in row)
# One rational coefficient control in the admitted structural locus, not a
# selected action. Arbitrary nonzero a,e,g and c0=-a/12 are handled in proof.
a,c0,e,g=F(12),F(-1),F(2),F(3)
m,h,n=10,4,14
L=2*a+n*c0
def symbol(xi):
    D=zero_matrix()
    c=add(*(scale(xi[j],gamma[j]) for j in range(4)))
    for j in range(4):
        for k in range(4):
            D[j][k]=add(scale(a if j==k else 0,c),scale(-a*eta[j]*xi[j]*eta[k],gamma[k]),scale(c0*xi[k],gamma[j]),scale(-c0*eta[k],mul(mul(gamma[j],c),gamma[k])))
        D[j][4]=add(scale(-a*eta[j]*xi[j],I),scale(-c0,mul(gamma[j],c)))
        D[j][5]=scale(e*eta[j]*xi[j],I)
        D[4][j]=scale(m*c0,add(scale(xi[j],I),scale(-eta[j],mul(c,gamma[j]))))
        D[5][j]=scale(g*xi[j],I)
    D[4][4]=scale(-(a+m*c0),c)
    return D
symbols=[symbol([F(j==k) for j in range(4)]) for k in range(4)]
check('candidate odd for all four tangent principal coefficients',all(iszero(anticomm_grade(D)) for D in symbols))
check('wrong trace sign rejected by principal coefficient',not iszero(anticomm_grade(symbols[0],[1,1,1,1,1,-1])))
check('wrong independent-scalar sign rejected by principal coefficient',not iszero(anticomm_grade(symbols[0],[1,1,1,1,-1,1])))
# This exact invertible perpendicular block proves joint injection of
# [U_sigma,e xi]. It is the universal uniqueness step, not a sampled rank.
Uperp=symbols[0][1][4]
check('perpendicular scalar-output coefficient zero',not symbols[0][1][5])
check('perpendicular sigma block has exact inverse',mul(Uperp,scale(1/(c0*c0),Uperp))==I)
check('remaining time scalar coefficient nonzero',symbols[0][0][5]==scale(-e,I))
# Native S_ni=-1/2 eta^-1 n_i. C_N=A and C_H are the two form blocks of
# C(b composed T_B), retaining exterior torsion with its plus sign.
A=[]
for r in range(m):
    A.append([add(*(scale(-F(1,2)*eta[mu]*eta[j]*normals[r][j][mu],gamma[mu]) for mu in range(h))) for j in range(h)])
Frow=[add(*(scale(1/diag[r],mul(gamma[4+r],A[r][j])) for r in range(m))) for j in range(h)]
CH=[[add(*(scale(F(1,2)*eta[k]*normals[r][k][j]/diag[r],gamma[4+r]) for r in range(m))) for k in range(h)] for j in range(h)]
check('horizontal gamma of exterior C_H equals F',all(add(*(scale(eta[j],mul(gamma[j],CH[j][k])) for j in range(h)))==Frow[k] for k in range(h)))
V=zero_matrix()
for j in range(h):
    for k in range(h):V[j][k]=add(scale(a,CH[j][k]),scale(c0,mul(gamma[j],Frow[k])))
for k in range(h):V[4][k]=scale(a+m*c0,Frow[k])
check('observed sigma coefficient equals a over six',a+m*c0==a/6)
check('observed total-trace coefficient equals five a over six',L==5*a/6)
check('torsion b block commutes with horizontal volume',all(mul(omega,V[j][k])==mul(V[j][k],omega) for j in range(h) for k in range(h)))
check('torsion sigma block anticommutes with horizontal volume',all(not add(mul(omega,V[4][k]),mul(V[4][k],omega)) for k in range(h)))
means=[-F(1,2)*sum(eta[j]*normals[r][j][j] for j in range(h)) for r in range(m)]
mean=add(*(scale(means[r]/diag[r],gamma[4+r]) for r in range(m)))
trace=scale(2,mean)
check('actual mean matrix equals metric over two',all(sum(means[r]/diag[r]*normals[r][j][k] for r in range(m))==(eta[j]/2 if j==k else 0) for j in range(h) for k in range(h)))
check('actual mean Clifford square minus one',mul(mean,mean)==scale(-1,I))
check('actual metric-trace Clifford square minus four',mul(trace,trace)==scale(-4,I))
check('symmetric-shape trace identity for every normal',all(add(*(mul(A[r][j],gamma[j]) for j in range(h)))==scale(means[r],I) for r in range(m)))
check('F on horizontal insertion equals mean Clifford',add(*(mul(Frow[j],gamma[j]) for j in range(h)))==mean)
R=anticomm_grade(V)
R_sigma=add(*(mul(R[4][j],gamma[j]) for j in range(h)))
expected_sigma=scale(-2*(a+m*c0),mul(omega,mean))
check('sigma residual on insertion is exact nonzero witness',R_sigma==expected_sigma and bool(R_sigma))
check('sigma witness has exact inverse',mul(R_sigma,scale(1/(4*(a+m*c0)**2),R_sigma))==I)
# tau=sigma+Gamma_H b; compare in original source-shaped observation coords.
R_tau=add(R_sigma,*(scale(eta[j],mul(gamma[j],add(*(mul(R[j][k],gamma[k]) for k in range(h))))) for j in range(h)))
expected_tau=scale(-2*L,mul(omega,mean))
check('original total-trace residual agrees after coordinate transport',R_tau==expected_tau)
check('total-trace witness has exact inverse',mul(R_tau,scale(1/(4*L**2),R_tau))==I)
check('omitting exterior torsion gives zero artificial defect',iszero(anticomm_grade(zero_matrix())))
check('omitted-torsion false survivor rejected by retained native witness',bool(R_tau))
# Recorded follow-through: the already-owned, constant ambient-chiral W.
# The native orthogonal basis has Clifford volume square 192^2. This gives
# an exact rational chirality representative, with no floating square root.
ambient_volume=I
for j in range(14):ambient_volume=mul(ambient_volume,gamma[j])
Omega=scale(F(1,192),ambient_volume)
check('native ambient chirality normalization',mul(Omega,Omega)==I)
check('ambient chirality anticommutes with all vector coefficients',all(not add(mul(Omega,gamma[j]),mul(gamma[j],Omega)) for j in range(14)))
check('ambient chirality commutes with horizontal grade',mul(Omega,omega)==mul(omega,Omega))
W=scale(F(1,2),add(scale(3,I),scale(-1,Omega)))
Wbar=scale(F(1,2),add(scale(3,I),Omega))
Winv=scale(F(1,4),add(scale(3,I),Omega))
Wbarinv=scale(F(1,4),add(scale(3,I),scale(-1,Omega)))
check('held chiral W inverses',mul(W,Winv)==I and mul(Wbar,Wbarinv)==I)
check('gamma contraction crosses the W weight',all(mul(gamma[j],W)==mul(Wbar,gamma[j]) for j in range(14)))
field=[W]*4+[Wbar,I]
field_inverse=[Winv]*4+[Wbarinv,I]
row=[I]*5+[W]
row_inverse=[I]*5+[Winv]
def wrapped(D):return [[mul(mul(row_inverse[j],D[j][k]),field[k]) for k in range(6)] for j in range(6)]
wrapped_symbols=[wrapped(D) for D in symbols]
check('held W receiver grade remains principal-odd',all(iszero(anticomm_grade(D)) for D in wrapped_symbols))
check('held W row-field identity exact',all(mul(mul(row[j],wrapped_symbols[r][j][k]),field_inverse[k])==symbols[r][j][k] for r in range(4) for j in range(6) for k in range(6)))
Uw=wrapped_symbols[0][1][4]
Uwinv=mul(Wbarinv,scale(1/(c0*c0),Uperp))
check('wrapped uniqueness perpendicular block has inverse',mul(Uw,Uwinv)==I and mul(Uwinv,Uw)==I)
Vw=wrapped(V)
Rw=anticomm_grade(Vw)
check('whole observed grading defect transports under held W',Rw==wrapped(R))
# Transport the actual input too: b_old=W^-1 J_H psi, sigma=nu=0.
wrapped_input=[mul(Winv,gamma[j]) for j in range(h)]
Rw_sigma=add(*(mul(Rw[4][j],wrapped_input[j]) for j in range(h)))
Rw_tau=add(Rw_sigma,*(scale(eta[j],mul(gamma[j],add(*(mul(Rw[j][k],wrapped_input[k]) for k in range(h))))) for j in range(h)))
check('held W transported sigma witness equals original',Rw_sigma==R_sigma)
check('held W transported total-trace witness equals original',Rw_tau==R_tau)
check('literal observed b uses W not crossed Wbar',any(mul(W,gamma[j])!=mul(Wbar,gamma[j]) for j in range(h)))
result={'status':'PASS','checks_passed':len(checks),'checks':checks,
 'arithmetic':'exact Fraction Clifford-word algebra; no sampled or floating rank',
 'control_coefficients':{'a':str(a),'c0':str(c0),'e':str(e),'g':str(g)},
 'normalization':'chi_H=i times horizontal Clifford volume; computed oddness homogeneous in chi_H',
 'witness':'original trace residual = -(5a/6) chi_H c_N(t); t^2=-4',
 'witness_rank_over_C':128,
 'rank_reason':'restriction to one full spinor input has an explicit invertible Clifford output; not a full residual-rank claim',
 'claim_ceiling':'same-input/output grading of existing K95 coherent-jet density-repaired R6-Bn0 only; no source physical chirality or class-C verdict'}
if args.output:
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
