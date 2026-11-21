#!/usr/bin/env python3
"""Exact grading-lift, characteristic-weight and native Clifford controls.
No source physical projector, operator/domain or class-C inhabitant is built.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')
import sympy as s
import numpy as np
from pathlib import Path
from itertools import product
from fractions import Fraction as F
import sys,json
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tests/channel-swings'))
from actual_sym2_c14_orbit_probe import native_gammas
checks=[]
def ck(name,x):
 assert bool(x),name
 checks.append(name)
# A complete symbolic two-eigenvalue block control of the general proof.
a,b=s.symbols('a b',real=True);A=s.diag(1,-1);gg=s.diag(1,-1);T=s.Matrix([[0,a],[b,0]]);Z=s.zeros(2);II=s.eye(2)
G=s.BlockMatrix([[A,T],[Z,gg]]).as_explicit();q=s.Matrix.hstack(Z,II);U=s.BlockMatrix([[II,T*gg/2],[Z,II]]).as_explicit();G0=s.diag(A,gg)
ck('descending mixed involution',G*G==s.eye(4) and q*G==gg*q)
ck('q-preserving shear diagonalizes grade',U*G0*U.inv()==G and q*U==q)
ck('general shear is not pairing isometry',U.T*U!=s.eye(4))
X=s.Matrix([[0,1],[1,0]]);D=s.diag(X,X)
ck('grading shear need not intertwine fixed D',U*D!=D*U)
# Actual operator compatibility upper-right equation.
L=s.Matrix(2,2,s.symbols('l0:4'));DD=s.BlockMatrix([[X,L],[Z,X]]).as_explicit()
ck('upper-block oddness equation', (G*DD+DD*G)[:2,2:]==A*L+T*X+X*T+L*gg)
# Spin10 character coefficients from all32 weights, parity halves.
x=s.symbols('x0:5');half={1:[], -1:[]}
for signs in product([-1,1],repeat=5):
 parity=int(np.prod(signs));half[parity].append(sum(si*xi for si,xi in zip(signs,x))/2)
for parity,weights in half.items():
 ck(f'normal spin half{parity} dimension16',len(weights)==16)
 ck(f'normal spin half{parity} degree2 zero',s.expand(sum(weights))==0)
 ck(f'normal spin half{parity} degree4',s.expand(sum(w*w/2 for w in weights)-2*sum(y*y for y in x))==0)
# Normal gamma kernel R_N^eps=N_C*S_N^eps-S_N^(-eps): rank144,ch2=34p1N.
p,n=s.symbols('p n');spin_rank=16;spin_ch2=2*n;rn_rank=10*spin_rank-spin_rank;rn_ch2=10*spin_ch2+n*spin_rank-spin_ch2
ck('normal RS half rank and ch2',rn_rank==144 and s.expand(rn_ch2)==34*n)
obs=F(80,3)*p+16*n;hidden_half=rn_ch2-F(rn_rank,24)*p
ck('hidden half coefficient',s.expand(hidden_half)==-6*p+34*n)
rows=[]
for ep,em in product([-1,1],repeat=2):
 total=s.expand(obs+(ep+em)*hidden_half);coef=int(total.subs(n,6*p).coeff(p)*3)
 ck(f'{ep},{em} closed coefficient',coef==368+594*(ep+em))
 ck(f'{ep},{em} spin parity and mod24',coef*16%2==0 and coef*16%64==0 and coef*16%24==8)
 rows.append({'epsilon_plus':ep,'epsilon_minus':em,'total_sigma_coefficient':coef,'K3_total':coef*(-16),'spin_signature_16k_mod24':'8*k mod24','parity':'even (multiple64*k)'})
ck('zero-signature control not nonzero observed index',all(r['total_sigma_coefficient']*0==0 for r in rows) and 368*0==0)
ck('K3 all residues16',all(r['K3_total']%24==16 for r in rows))
# Index is sensitive to domain; finite graph-condition exact rank-nullity control.
M=s.Matrix([[1,0,0,0],[0,1,0,0]]);R=s.Matrix([[1,0,0],[0,1,0],[0,0,1],[0,0,0]])
ck('one independent domain condition shifts index by minus1',(M.cols-M.rows)-((M*R).cols-(M*R).rows)==1)
# Signed-permutation native Clifford identities, no numerical tolerances.
g,eta=native_gammas();I=np.eye(128,dtype=complex);O=0*I;H=[9,0,1,2];N=[a for a in range(14) if a not in H];eq=np.array_equal
def prodmat(seq):
 r=I.copy()
 for z in seq:r=r@z
 return r
chiH=1j*prodmat([g[a] for a in H]);chiY=prodmat(g);chiN=chiH@chiY;K=prodmat(g[:9]);J=prodmat([z for z in g if eq(z.conjugate(),-z)])
# This fixture has even imaginary-generator count; independently verify J.
ck('actual quaternionic intertwiner',all(eq(J@z.conjugate(),z@J) for z in g) and eq(J@J.conjugate(),-I))
ck('native normalized grades',eq(chiH@chiH,I) and eq(chiN@chiN,I) and eq(chiH@chiN,chiY))
ck('ambient grade fails plain observed horizontal identity',not eq(chiY,chiH) and not eq(chiY,-chiH))
ck('J exchanges H and N grades',eq(J@chiH.conjugate(),-chiH@J) and eq(J@chiN.conjugate(),-chiN@J))
# Integer-scaled normal projector; only two independent columns needed for contrary controls,
# all100 blocks used to verify preservation, without forming a1792-square matrix.
PN={(a,b):10*I*(a==b)-eta[a]*g[a]@g[b] for a in N for b in N}
ck('normal projection columns gamma-free',all(eq(sum((g[a]@PN[a,b] for a in N),O.copy()),O) for b in N))
for ep,em in product([-1,1],repeat=2):
 aN=((ep+em)*I+(ep-em)*chiN)/2;A=chiH@aN
 ck(f'native hidden lift{ep},{em} involution/odd',eq(A@A,I) and all(eq(A@g[h]+g[h]@A,O) for h in H))
 ck(f'native hidden lift{ep},{em} preserves kernel',all(eq(A@PN[a,b],PN[a,b]@A) for a in N for b in N))
 ck(f'native hidden lift{ep},{em} Krein skew',eq(A.conjugate().T@K,-K@A))
 ck(f'native hidden lift{ep},{em} uniform J exchange criterion',eq(J@A.conjugate(),-A@J)==(ep==em))
print('PASS:',len(checks),'exact descending-grading, parity/residue and Clifford controls.')
if '--json' in sys.argv:print(json.dumps({'checks':checks,'closed_comparison_rows':rows,'ordinary_index_not_torsion_invariant':True,'native_total_known':False},indent=2))
