#!/usr/bin/env python3
"""Exact prescribed-pencil real kernel and finite invertibility certificates.

No broad nonlinear adapter search. The Pfaffian-grid decision can be expensive;
only small explicit subspaces are exhaustively scanned in this probe.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from itertools import combinations
import argparse,hashlib,json
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
I=S.eye(32);Z=S.zeros(32);gam=[]
for sign in [1,-1]:
    for j in range(5):
        g=S.zeros(32)
        for mask in range(32):
            c=(-1)**((mask&((1<<j)-1)).bit_count())
            g[mask^(1<<j),mask]=c*(sign if mask&(1<<j) else 1)
        gam.append(g)
gam[4]=S.I*gam[4]
def blade(indices):
    a=I
    for j in indices:a=a*gam[j-1]
    return a
IN=blade(range(1,11));B=S.zeros(32)
for mask in range(32):
    comp=31^mask;k=mask.bit_count()
    swaps=sum((comp&((1<<j)-1)).bit_count() for j in range(5) if mask&(1<<j))
    B[mask,comp]=(-1)**(k*(k-1)//2+swaps)
ids=[[m for m in range(32) if m.bit_count()%2==p] for p in range(2)]
ix=ids[1];epsilon=S.simplify(IN[ix[0],ix[0]]/S.I)
inds=list(combinations(range(1,11),3));blades=[blade(x) for x in inds]
phis=[(B*x).extract(ix,ix) for x in blades]
upp=list(combinations(range(16),2))
def upper(a):return S.Matrix([a[i,j] for i,j in upp])
G=S.Matrix.hstack(*(upper(x) for x in phis));Ginv=G.inv()
def coord(terms):
    v=S.zeros(120,1)
    for indices,c in terms:v[inds.index(tuple(indices))]+=c
    return v

def phi(a):return sum((c*z for c,z in zip(a,phis) if c),S.zeros(16))
def grade(a):return sum((c*z for c,z in zip(a,blades) if c),Z)
def clean(a):return a.applyfunc(S.expand)
def bar(a):
    C=blade([j for j in range(1,11) if j!=5])
    return clean(-C*a.conjugate()*C)

def constraint_matrix(Y,include_real=True):
    """392 real equations in120 real grade coordinates, for exact Gaussian Y."""
    columns=[]
    for z in phis:
        t=clean(z*Y);sym=t+t.T
        vals=[sym[i,j] for i in range(16) for j in range(i,16)]
        col=[S.re(x) for x in vals]+[S.im(x) for x in vals]
        if include_real:col += [S.im(x) for x in clean(Ginv*upper(t))]
        columns.append(S.Matrix(col))
    return S.Matrix.hstack(*columns)

def reconstruction_space(Y):
    return constraint_matrix(Y).nullspace()
def recover(a,Y,eps=epsilon):
    b=clean(Ginv*upper(phi(a)*Y))
    if any(S.im(x)!=0 for x in b):raise ValueError('not a real grade solution')
    if clean(phi(a)*Y-phi(b))!=S.zeros(16):raise ValueError('not alternating image')
    return (a+b)/14,eps*(a-b)/30

def compositions(n,m):
    if m==1:
        yield (n,);return
    for j in range(n+1):
        for rest in compositions(n-j,m-1):yield (j,)+rest

def invertible_member(basis):
    """Complete degree8 homogeneous Pfaffian grid for the supplied subspace.
    Returns a witness coefficient tuple or None (exact exhaustive rejection).
    """
    if not basis:return None
    for alpha in compositions(8,len(basis)):
        a=sum((c*x for c,x in zip(alpha,basis)),S.zeros(120,1))
        if phi(a).det()!=0:return alpha
    return None

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
    cs={};faults={}
    def ck(k,v):cs[k]=bool(v)
    ck('actual_volume_half_sign',epsilon in [1,-1] and IN.extract(ix,ix)==epsilon*S.I*S.eye(16))
    ck('all120_alternating',all(z.T==-z for z in phis))
    ck('complex_Phi_isomorphism',G*Ginv==S.eye(120))
    ck('normal_signature',all(g*g==(1 if j<4 else -1)*I for j,g in enumerate(gam)))
    ck('all_gamma_anticommutators',all(gam[j]*gam[k]+gam[k]*gam[j]==Z for j,k in combinations(range(10),2)))
    a=coord([((1,2,3),1)])
    ck('real_invertible_trivector',phi(a).det()!=0)
    nonalt=clean(phi(a)*phi(a).inv())
    ck('nonalternating_image_rejected',nonalt==S.eye(16) and nonalt+nonalt.T!=S.zeros(16) and Ginv*upper(nonalt)==S.zeros(120,1))
    # Complete real kernels for the entire scalar representative tests.
    Ereal=constraint_matrix(2*S.eye(16));Ephase=constraint_matrix(S.I*S.eye(16))
    ck('real_scalar_complete120_kernel',Ereal==S.zeros(392,120))
    ck('nonreal_scalar_zero_kernel',Ephase.rank()==120)
    ck('entrywise_reality_is_not_real_form',any(any(S.im(x)!=0 for x in z) for z in phis))
    Yi=S.I*I
    ck('nonreal_full_phase_norm_one',bar(Yi)*Yi==I)
    O=S.diag(*([S.Matrix([[0,1],[-1,0]])]*8))
    ck('nonreal_paired_Jordan_control',(S.I*S.eye(16)).T*O==O*(S.I*S.eye(16)))
    w,u=recover(a,2*S.eye(16));P=7*IN*grade(w)-15*S.I*grade(u);bp=7*IN*grade(w)+15*S.I*grade(u)
    Y=clean(P.inv()*bp)
    ck('real_scalar_both_halves',Y.extract(ix,ix)==2*S.eye(16) and Y.extract(ids[0],ids[0])==S.eye(16)/2)
    ck('real_scalar_full_reconstruction',clean(P*Y-bp)==Z and bar(Y)*Y==I)
    # Singular basis is not singular subspace. These are specified subspaces,
    # not asserted to be complete reconstruction kernels for a particular Y.
    a1=coord([((1,2,3),1),((2,3,5),1)])
    a2=coord([((1,2,3),1),((2,3,5),-1)])
    ck('both_basis_trivectors_nilpotent',grade(a1)**2==Z and grade(a2)**2==Z)
    ck('singular_basis_but_invertible_sum',phi(a1).det()==phi(a2).det()==0 and phi(a1+a2).det()!=0)
    ck('one_dimensional_full_rejection',invertible_member([a1]) is None)
    alpha=invertible_member([a1,a2]);ck('two_dimensional_grid_witness',alpha is not None)
    ck('explicit_balanced_grid_witness',phi(4*a1+4*a2).det()!=0)
    # Exact degree8 simplex interpolation at m=3: basis evaluations form a
    # nonsingular matrix, using barycentric falling factorials.
    nodes=list(compositions(8,3))
    table=S.Matrix([[S.prod(S.prod(alpha_i-j for j in range(beta_i)) for alpha_i,beta_i in zip(al,be)) for be in nodes] for al in nodes])
    ck('degree8_simplex_cardinality',len(nodes)==45)
    ck('degree8_simplex_unisolvent',table.is_diagonal() and all(x!=0 for x in table.diagonal()))
    # Actual K2205 pencil, reused without repeating its characteristic census.
    wc=coord([((1,2,3),1),((1,4,5),1),((2,6,7),2),((3,8,9),3),((4,6,10),5)])
    uc=coord([((1,2,4),2),((1,5,7),3),((2,6,8),5),((3,9,10),7),((4,5,6),11)])
    vv=IN*grade(wc);tt=S.I*grade(uc);PP=7*vv-15*tt;BP=7*vv+15*tt
    YY=clean(PP.inv()*BP);yp=YY.extract(ix,ix)
    ac=7*wc+15*epsilon*uc;bc=7*wc-15*epsilon*uc
    ck('actual_grade_real_form_equation',clean(phi(ac)*yp-phi(bc))==S.zeros(16))
    print('building_actual_real_kernel_equations',flush=True)
    EE=constraint_matrix(yp)
    ck('actual392_real_equations',EE.shape==(392,120) and EE*ac==S.zeros(392,1))
    wr,ur=recover(ac,yp)
    ck('actual_coefficient_recovery',wr==wc and ur==uc)
    PR=7*IN*grade(wr)-15*S.I*grade(ur)
    ck('actual_full32_reconstruction',PR==PP and clean(PR*YY-bar(PR))==Z)
    ck('actual_both_pencil_blocks_invertible',PP.extract(ids[0],ix).det()!=0 and PP.extract(ix,ids[0]).det()!=0)
    RR=vv+3*tt;br=vv-3*tt
    gradeK=lambda x:sum(((1 if j<4 else -1)*g*x*g for j,g in enumerate(gam)),Z)
    AA=3*gradeK(br*br)+34*br*br+36*RR*br+8*br*RR-24*RR*RR
    BB=184*RR*RR+140*RR*br+184*br*RR+194*br*br+24*gradeK(br*RR)+15*gradeK(br*br)
    res=clean(4*AA.extract(ix,ix)*yp-(5*BB-AA).extract(ix,ix))
    ck('reconstructed_actual_pencil_still_Euler_rejected',res[0,0]!=0)
    assert all(cs.values()),[k for k,v in cs.items() if not v]
    # Each fault below corrupts a mathematical ingredient and is tested against
    # the ORIGINAL equation, not a relaxed checker or a process crash.
    Ebad=constraint_matrix(S.I*S.eye(16),include_real=False)
    faults['omit_alternation_condition']=['diagonal image is not alternating'] if Ginv*upper(nonalt)==S.zeros(120,1) and nonalt+nonalt.T!=S.zeros(16) else []
    faults['omit_real_grade_condition']=['nonreal false positive'] if Ebad*a==S.zeros(272,1) and Ephase*a!=S.zeros(392,1) else []
    wr,ur=recover(ac,yp,eps=-epsilon);badP=7*IN*grade(wr)-15*S.I*grade(ur)
    faults['wrong_half_sign']=['original full pencil equation'] if clean(badP*YY-bar(badP))!=Z else []
    faults['basis_only_invertibility']=['invertible combination lost'] if all(phi(x).det()==0 for x in [a1,a2]) and alpha is not None else []
    bad=EE.copy();idx=next(i for i,x in enumerate(ac) if x);bad[0,idx]+=1
    faults['linear_coefficient_fault']=['actual original kernel witness'] if bad*ac!=S.zeros(392,1) else []
    badP=PP+gam[0]
    faults['outside_grade_pencil_fault']=['original full pencil equation'] if clean(badP*YY-bar(badP))!=Z else []
    assert all(faults.values()),faults
    deps=['explorations/conditional-build/k2208-grade-constrained-pencil-reconstruction-2026-10-28.md','explorations/conditional-build/k2205-ordered-pencil-real-constraints-2026-10-28.md','explorations/conditional-build/k2202-ordered-clifford-adapter-consequences-2026-10-28.md','explorations/conditional-build/k2197-general-ordered-adapter-constraints-2026-10-28.md']
    report=dict(result_id='K2208',status='exact_prescribed_real_grade_reconstruction',checks=cs,fault_failures=faults,chirality_epsilon=str(epsilon),grid_witness=list(alpha),actual_Euler_residual00=str(res[0,0]),dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Universal real-form reconstruction and degree8 interpolation proof; exact120-blade map and complete central kernels; exact specified-subspace grids; actual prior pencil reconstruction with retained Euler rejection; genuine data/equation faults. No nonlinear all10 solution or efficient-complexity claim.')
    dst=ROOT/'lab/process/k2208-grade-constrained-pencil-reconstruction.json'
    if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dst.read_text())==report,'report drift'
    print(json.dumps(dict(result='K2208',controls=len(cs),faults=len(faults))))
if __name__=='__main__':main()
