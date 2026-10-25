"""Exact reduced action, fixed-norm coefficient class and nonlinear action lift.

Real commuting classical fields, not a source-selected fermionic action.
Run with SageMath Python. Universal claims use the accompanying derivation.
"""
from pathlib import Path
import argparse, hashlib, json
from sage.all import QQ, matrix, identity_matrix, block_diagonal_matrix, PolynomialRing
import k2021_common_degree_dual_operator as b
from k2032_principal_form_rigidity import sm, raw
from k2036_maximal_graph_raw_couplings import graph, mm
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k2038-observed-action-compression.json'

def extension(N,E,D,H,R):
    Y=mm(H,D,E,N);S=mm(E.transpose(),Y)
    assert S==S.transpose(), 'compressed symmetry obstruction'
    return mm(H,mm(Y,R)+mm(R.transpose(),Y.transpose())-mm(R.transpose(),S,R))

def produce():
    E,D,_,_=graph();H=sm(b.H,1920);I=identity_matrix(QQ,128,sparse=True)
    g=[sm(b.gamma(k)) for k in range(14)];B=sm(b.B);Wb=3*I-sm(b.W);V=sm(b.J)
    A=matrix(QQ,11,11,lambda i,j:10 if i==j==0 else 4 if i==0 or j==0 else int(i!=j))
    F=-mm(B,g[0],Wb);T=mm(E.transpose(),H,D,E)
    assert T==A.tensor_product(F) and T.transpose()==-T
    assert F.transpose()==-F and F*F==-Wb*Wb
    assert (V-I)*(V+I)==0 and V.trace()==0
    x=PolynomialRing(QQ,'x').gen()
    assert A.charpoly()(x)==(x+1)**9*(x*x-19*x-70) and A.det()==70
    Ti=A.inverse().tensor_product(-Wb.inverse()*Wb.inverse()*F)
    assert mm(T,Ti)==identity_matrix(QQ,1408,sparse=True)
    Cs=[block_diagonal_matrix([g[0]*g[k]]*11) for k in (7,8,9)]
    for k,C in zip((7,8,9),Cs):
        assert C==C.transpose() and C*C==identity_matrix(QQ,1408,sparse=True)
        assert mm(T,C)==mm(E.transpose(),H,raw(k,sm(b.W)),E)
        assert mm(T,C)==mm(C,T) and mm(T,C).transpose()==-mm(T,C)
    M=g[0]*g[1]*g[2]*g[10];N=block_diagonal_matrix([M]*11)
    assert M.transpose()==-M and M*M==-I and mm(T,N)==mm(N,T)
    for C in Cs:assert mm(C,N)+mm(N,C)==0
    R=matrix(QQ,1408,1920,sparse=True)
    for j,r in enumerate([0,1,2,3,4,5,6,10,11,12,13]):
        R[128*j:128*(j+1),128*r:128*(r+1)]=g[r]
    assert mm(R,E)==identity_matrix(QQ,1408,sparse=True)
    ext=extension(N,E,D,H,R)
    assert mm(H,ext)==mm(ext.transpose(),H) and mm(ext,E)==mm(D,E,N)
    assert not ext[1792:,1792:]
    Kt=extension(T,E,D,H,R)
    assert mm(Kt,E)==mm(D,E,T) and mm(H,Kt)==mm(Kt.transpose(),H)
    assert not Kt[1792:,1792:] and any(mm(C,T)+mm(T,C) for C in Cs)
    S=mm(T,N);assert S==S.transpose()
    u=matrix(QQ,1408,1,{(i,0):QQ((i*17+3)%19-9)/7 for i in range(1408)},sparse=True)
    h=matrix(QQ,1408,1,{(i,0):QQ((i*13+1)%17-8)/5 for i in range(1408)},sparse=True)
    s=(u.transpose()*mm(S,u))[0,0]/2
    ds=(h.transpose()*mm(S,u))[0,0];mu=QQ(2)/3;coupling=QQ(3)/5
    grad=(mu+coupling*s)*mm(S,u);flow=mm(Ti,grad)
    assert (h.transpose()*grad)[0,0]==(mu+coupling*s)*ds
    assert flow==(mu+coupling*s)*mm(N,u) and (u.transpose()*flow)[0,0]==0
    # Full nonlinear action lift, including its actual first derivative on graph.
    Q=identity_matrix(QQ,1920,sparse=True)-mm(E,R);Y0=mm(H,D,E)
    assert mm(Q,E)==0 and not R[:,1792:]
    assert Q[:,1792:]==identity_matrix(QQ,1920,sparse=True)[:,1792:]
    lifted_gradient=mm(R.transpose(),grad)+mm(Q.transpose(),Y0,flow)
    assert lifted_gradient==mm(Y0,flow)
    # Directional derivative agrees for arbitrary ambient variation, not just tangents.
    z=matrix(QQ,1920,1,{(i,0):QQ((i*7+1)%23-11)/13 for i in range(1920)},sparse=True)
    direct=(mm(R,z).transpose()*grad)[0,0]+(mm(Q,z).transpose()*mm(Y0,flow))[0,0]
    assert direct==(z.transpose()*mm(Y0,flow))[0,0]
    # General tangent perturbations need not conserve the same norm.
    nu=mm(N,u);su=mm(S,u)
    assert (su.transpose()*nu)[0,0]==0 and nu and su
    # Rank-one shear of the homogeneous flow: no dense Jacobian needed.
    tangent=su-coupling*nu*(su.transpose()*su)[0,0]
    assert (tangent.transpose()*tangent)[0,0]==(su.transpose()*su)[0,0]+coupling**2*(su.transpose()*su)[0,0]**2*(u.transpose()*u)[0,0]
    assert 25**2<641<26**2
    multiplicities=[288,288,32,32,32,32]
    assert 2*sum(multiplicities)==1408
    dimension=sum(n*n for n in multiplicities);assert dimension==169984
    refs=['tests/channel-swings/k2021_common_degree_dual_operator.py',
          'lab/process/k2034-observed-principal-forms.json',
          'lab/process/k2036-maximal-graph-raw-couplings.json']
    return dict(result_id='K2038',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',
        target_claim='NONE-NOT-A-KILL',compression=dict(copy_matrix=[[str(v) for v in row] for row in A],
        spinor_factor='-B*g0*Wbar',rank=1408,copy_charpoly='(x+1)^9*(x^2-19*x-70)',
        determinant='70^128 * 2^704',spinor_frequency_multiplicities=[32,32]),
        positive_action_coefficients=dict(condition='N^T=-N and [T,N]=0',real_dimension=dimension,
        invisible_full_coefficient_dimension=123072,total_full_coefficient_dimension=293056,
        compact_lie_algebra='u(288)^2 + u(32)^4',frequency_intervals=['{1}','{2}','(3,7/2)','(6,7)','(22,45/2)','(44,45)'],mass_gap_for_general_member=False),
        extension=dict(mass_entries=len(ext.dict()),general_example_entries=len(Kt.dict()),southeast_zero=True),
        nonlinear=dict(field_parity='real commuting classical fields',invariant='s=u^T*T*N*u/2',
        potential='mu*s+g*s^2/2',equation='du+(mu+g*s)*N*u=0',
        full_potential='V(R*psi)+(Q*psi)^T*H*D0*E*T^-1*gradV(R*psi)',
        local_current='dt |u|^2 + sum dj(u^T*Cj*u)=0',global_nonlinear_existence=False,
        full_nonlinear_action_lift=True,auxiliary_hessian_zero=True,linearized_norm_conservation=False,homogeneous_global_flow=True,homogeneous_tangent_shear="I-g*t*(N*u0)*(S*u0)^T"),
        inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs},
        scope='Fixed observed1408 graph and Euclidean norm, changed unrestricted H-selfadjoint coefficient class. No raw-tie rescue, source physical selection, Grassmann reduction, global nonlinear domain or quantum positivity claim.')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=produce()
    if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert r==json.loads(OUT.read_text())
    print('PASS K2038 full compression, extension, class invariants and nonlinear action identities')
