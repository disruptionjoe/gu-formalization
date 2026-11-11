#!/usr/bin/env python3
"""Exact raw-matrix observation controls. Written analytic proofs are separate."""
import sys
sys.dont_write_bytecode=True
import argparse,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tests/channel-swings'))
import k2236_raw_observation_closure_probe as old
REPORT=ROOT/'lab/process/bet-2plus1-observation-jets.json'
NOTES=['explorations/conditional-build/bet-2plus1-temporal-observation-2026-11-11.md','explorations/conditional-build/bet-2plus1-polarized-observed-evolution-2026-11-11.md']
def simp(m):return m.applyfunc(lambda x:s.cancel(s.expand(x)))
def zero(m):return simp(m)==s.zeros(*m.shape)
def raw():
    obs=[0,7,8,9];un=[i for i in range(14) if i not in obs]
    def M(k):return s.Matrix([[s.Rational(old.o.scalar_m(k,a,c)) for c in range(15)] for a in range(15)])
    E=s.zeros(15,6);R=s.zeros(6,15)
    for i,a in enumerate(obs):E[a,i]=R[i,a]=1
    for a in un:E[a,4]=1;R[4,a]=s.Rational(1,10)
    E[14,5]=R[5,14]=1;mi=M(0).inv();ts=[]
    for k in obs[1:]:
        A=mi*M(k);T=R*A*E;assert A*E==E*T;ts.append(T)
    return ts

def build():
    checks=[]
    def ck(name,value,kind='supporting_exact'):
        assert bool(value),name
        checks.append({'name':name,'kind':kind})
    T=raw();P=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
    p=s.symbols('p1 p2 p3',real=True);rho=sum(x*x for x in p);I=s.eye(2)
    C=sum((p[j]*P[j] for j in range(3)),s.zeros(2));A=sum((p[j]*s.kronecker_product(T[j],P[j]) for j in range(3)),s.zeros(12))
    Q=s.kronecker_product(s.eye(6).extract([0,1,2,3,5],range(6)),I);ev=s.kronecker_product(s.eye(6)[:,4],I)
    F=Q*A*ev;expected=s.zeros(2,2).col_join(s.Matrix.vstack(*[10*p[j]*P[j]-s.Rational(5,6)*C for j in range(3)])).col_join(10*C)
    ck('original_raw_hidden_column',F==expected);ck('Clifford_square',zero(C*C-rho*I))
    k=s.Rational(2225,12);ck('exact_full_residual_Gram',zero(F.H*F-k*rho*I))
    inv=F.H/(s.I*k*rho);ck('first_jet_left_inverse',zero(inv*(s.I*F)-I))
    projector=F*F.H/(k*rho);ck('residual_consistency_projector',zero(projector*projector-projector) and zero(projector.H-projector))
    ck('zero_mode_first_jet_dark',F.subs(dict.fromkeys(p,0))==s.zeros(10,2),'contrary_exact')
    wrong=s.MutableDenseMatrix(F);wrong[8,0]+=p[0];ck('changed_hidden_return_rejected',not zero(wrong.H*wrong-k*rho*I),'contrary_exact')
    N=simp(A*A-rho*s.eye(12));ck('universal_square_zero_defect',zero(N*N));ck('uniform_nonzero_defect_block',zero(N[:2,8:10]-s.Rational(55,6)*rho*I))
    L=s.zeros(2,2).row_join(s.Matrix.hstack(*[I-p[j]*C*P[j]/rho for j in range(3)])).row_join(10*I).row_join(-I)
    W=(rho*I).col_join(s.Matrix.vstack(*[-p[j]*P[j]*C for j in range(3)])).col_join(s.zeros(4,2))
    ck('universal_polarization_factor',zero(N-s.Rational(11,12)*W*L));ck('factor_nilpotence',zero(L*W))
    ck('factor_surjectivity',L[:,8:10]==10*I);ck('factor_injective_first_block',W[:2,:]==rho*I)
    ck('parity_even_lift',zero(L.subs({x:-x for x in p})-L))
    # E q is the explicit unique polarized lift. The free q coordinate is literal Q.
    E=s.MutableDenseMatrix(Q.T);E[8:10,:]=-L*Q.T/10
    ck('literal_observation_lift',Q*E==s.eye(10));ck('polarized_lift',zero(L*E))
    B=simp(Q*A*E);ck('observed_autonomous_intertwiner',zero(A*E-E*B));ck('observed_massless_wave_identity',zero(B*B-rho*s.eye(10)));ck('full_observed_Euclidean_symmetrizer',zero(B.H-B))
    # Rational metric, no square-root symbolic simplification needed.
    G=simp((s.eye(10)+B.H*B/rho)/2)
    ck('observed_positive_metric_symmetry',zero(G*B-B.H*G));ck('observed_h_propagation',zero(B[-2:,:]-C*Q[-2:,:]*E))
    E4=E[:,:8];B4=B[:8,:8]
    ck('scalar_zero_principal_invariance',zero(A*E4-E4*B4));ck('scalar_zero_Euclidean_symmetrizer',zero(B4.H-B4))
    # Exact longitudinal/transverse formula in x_j=C_j b_j coordinates.
    U=s.diag(I,*P);Bt=simp(U*B4*U)
    Bt_expected=s.zeros(8)
    for j in range(3):Bt_expected[:2,2+2*j:4+2*j]=p[j]*I;Bt_expected[2+2*j:4+2*j,:2]=p[j]*I
    for j in range(3):
        for l in range(3):Bt_expected[2+2*j:4+2*j,2+2*l:4+2*l]=-(int(j==l)-p[j]*p[l]/rho)*C
    ck('longitudinal_transverse_decomposition',zero(Bt-Bt_expected))
    # Defect identities are homogeneous even Clifford polynomials. Both Pauli
    # summands also replay a concrete direction, independent of representation choice.
    for sign in [1,-1]:
        c=[sign*x for x in P];a=sum((v*s.kronecker_product(t,g) for v,t,g in zip([1,2,3],T,c)),s.zeros(12));n=simp(a*a-14*s.eye(12))
        ck(f'faithful_Cl3_summand_{sign}',n.rank()==2 and zero(n*n))
    # Full mass algebra uses both Cl3 summands with a skew involution and
    # J commuting with C_j, anticommuting with the mass generator Z.
    C4=[s.diag(x,-x) for x in P];Z=s.zeros(2).row_join(I).col_join((-I).row_join(s.zeros(2)));J=s.diag(I,-I);I4=s.eye(4)
    ck('mass_algebra',Z.H==-Z and Z*Z==-I4 and J*J==I4 and Z*J+J*Z==s.zeros(4) and all(zero(Z*c+c*Z) and zero(J*c-c*J) for c in C4))
    for jsgn in [1,-1]:
        jj=jsgn*J;Wbar=(3*I4+jj)/2;H=Z*Wbar*Wbar/2;D=s.diag(-Z,Z,Z,Z,Z,H)
        for coords in [(1,0,0),(3,4,0),(1,2,3)]:
            r2=sum(x*x for x in coords);c=sum((x*g for x,g in zip(coords,C4)),s.zeros(4));a=sum((x*s.kronecker_product(t,g) for x,t,g in zip(coords,T,C4)),s.zeros(24));q=s.kronecker_product(s.eye(6).extract([0,1,2,3,5],range(6)),I4)
            l=s.zeros(4).row_join(s.Matrix.hstack(*[I4-x*c*g/r2 for x,g in zip(coords,C4)])).row_join(10*I4).row_join(-I4);ee=s.MutableDenseMatrix(q.T);ee[16:20,:]=-l*q.T/10;e4=ee[:,:16];b4=q[:16,:]*a*e4;dq=s.diag(-Z,Z,Z,Z)
            label=f'{jsgn}_{coords}'
            ck('mass_leakage_'+label,zero(l*D*ee-(Z-H)*q[-4:,:]*ee))
            ck('full_polarization_not_mass_invariant_'+label,(Z-H).det()!=0,'contrary_exact')
            ck('mass_preserves_scalar_zero_'+label,zero(D*e4-e4*dq))
            ck('massive_positive_generator_'+label,zero(b4.H-b4) and dq.H==-dq)
            grow=s.kronecker_product(s.Matrix([[1,1,1,1,10,0]]),I4)*e4
            frow=2*s.eye(16)[:4,:]-grow
            ck('massless_trace_and_partner_'+label,zero(grow*b4-c*grow) and zero(frow*b4+c*frow))
            ck('mass_trace_partner_mixing_'+label,zero(grow*dq+Z*frow) and zero(frow*dq+Z*grow))
            # A genuine wrong scalar mass kills the leakage formula.
            bad=D.copy();bad[20:24,20:24]=Z
            ck('changed_scalar_mass_detected_'+label,not zero(l*bad*ee-(Z-H)*q[-4:,:]*ee),'contrary_exact')
    # Concrete provenance projection fails to retain the polarized constraint.
    pp={p[0]:1,p[1]:0,p[2]:0};la=L.subs(pp);e=E.subs(pp);trace=s.Matrix([1,1,1,1,1,0])/14;g=s.Matrix([[1,1,1,1,10,0]]);PT=s.kronecker_product(trace*g,I);PN=s.kronecker_product(s.diag(0,0,0,0,0,1),I)
    ck('trace_projection_breaks_constraint',not zero(la*PT*e),'contrary_exact');ck('scalar_projection_breaks_constraint',not zero(la*PN*e),'contrary_exact')
    # Actual autonomous readouts, distinguished from their original insertions.
    grow=s.kronecker_product(g,I)*E
    ck('massless_trace_readout',zero(grow*B-C*grow))
    ck('pure_trace_insertion_not_polarized',zero(L*s.kronecker_product(trace,I)-s.Rational(6,7)*I))
    # Spatially varying mass shifts momentum and violates the imposed lift.
    before=s.zeros(12,1);before[4]=1;before[8]=-s.Rational(1,10)
    ck('incoming_transverse_lift',zero(L.subs(pp)*before))
    ck('momentum_shift_breaks_lift',not zero(L.subs({p[0]:0,p[1]:1,p[2]:0})*before),'contrary_exact')
    # The exact Gram scales quadratically; normalized hidden data cannot have
    # an infrared-uniform residual estimate (the continuum proof is in the note).
    eps=s.symbols('eps',positive=True)
    ck('infrared_residual_scaling',zero((F.H*F).subs({p[0]:eps,p[1]:0,p[2]:0})-k*eps**2*I))
    # Symbolic characteristic factor of the positive h=0 massive subsystem,
    # separate longitudinal and transverse blocks in its orthogonal coordinates.
    rr,mm,lam=s.symbols('r m lambda',real=True);cl=C4[0];long=s.zeros(4).row_join(rr*I4).col_join((rr*I4).row_join(s.zeros(4)))-s.I*mm*s.diag(-Z,-Z)
    transverse=-rr*cl+s.I*mm*Z
    cp=long.charpoly(); zz=cp.gen
    ck('longitudinal_real_branches',s.factor(cp.as_expr()-((zz-rr)**2-mm**2)**2*((zz+rr)**2-mm**2)**2)==0)
    ck('transverse_relativistic_branches',zero(transverse*transverse-(rr**2+mm**2)*I4))
    ck('nonzero_mass_not_a_spectral_gap',long.subs({rr:1,mm:1}).det()==0,'contrary_exact')
    deps=['tests/channel-swings/k2236_raw_observation_closure_probe.py','tests/channel-swings/k2206_changed_raw_mass_construction_probe.py','explorations/conditional-build/k2236-raw-observation-closure-2026-10-29.md','explorations/conditional-build/k2034-observed-principal-forms-2026-10-24.md','explorations/conditional-build/selected-k77-nonlocal-ultrahyperbolic-polarization-gate-2026-08-11.md',*NOTES]
    return dict(artifact='BET_2PLUS1_OBSERVATION_JETS',program_target='BET-2PLUS1',tier='T2',status='conditional_internal_result',checks=checks,exact_residual_gram=str(k),dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),claim_ceiling='No physical count, source-selected action/observation/constraint, matrix/ledger change or proof-assistant certification. Symbolic identities and finite controls supplement written universal Fourier/domain proofs.')
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();d=build()
    if args.write:REPORT.write_text(json.dumps(d,indent=2)+'\n')
    else:assert json.loads(REPORT.read_text())==d,'report or dependency changed'
    print('PASS',len(d['checks']),'checks;',json.dumps({k:sum(x['kind']==k for x in d['checks']) for k in {x['kind'] for x in d['checks']}}))
