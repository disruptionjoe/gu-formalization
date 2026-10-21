#!/usr/bin/env python3
"""Exact phase trace, constant-frame tangent obstruction and target bands."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sympy as s

ROOT = Path(os.environ.get('GU_ROOT', Path(__file__).resolve().parents[2]))
OUT = ROOT / 'lab/process/k1885-traveling-phase-rigidity-and-frame-reduction.json'
INPUTS = ['lab/process/k1832-k77-common-energy-form.json',
          'lab/process/k1836-k77-differential-dirac-quotient.json',
          'lab/process/k1840-k77-conservative-variable-observation.json',
          'lab/process/k1877-traveling-gram-amplitude-rigidity.json',
          'lab/process/k1879-rotating-observation-connection-repair.json']

def mat(x):
    out = s.zeros(x.get('rows', 16), x.get('columns', 16))
    for i, j, v in x['entries']:
        out[i, j] = s.Rational(v)
    return out

def zero(x):
    return all(s.expand(v) == 0 for v in x)

def tangent_system(er, sr, kr, D, J, v):
    A = list(map(mat, er['matrices']))
    H = mat(er['H']); Hi = H.inv()
    T = list(map(mat, sr['T'])); L = mat(er['J'])
    if T[0]*L != J*T[0]:
        L = -L
    C0 = (v*s.eye(16)-A[0])*L
    B0 = (v*s.eye(4)-D[0]/24)*J
    S0 = -T[0]*L
    B1 = mat(kr['repairs'][0]['B'])
    cols = []
    for row in mat(kr['full_conservative_kernel']).tolist():
        U = s.zeros(16); pos = 0
        for i in range(16):
            for j in range(i+1, 16):
                U[i,j] = row[pos]; U[j,i] = -row[pos]; pos += 1
        C = Hi*U; S = s.Matrix(4,16,row[126:])
        cols.append(s.Matrix(row[120:126]+list(S0*C+S*C0-B0*S)))
    M = s.Matrix.hstack(*cols)
    rhs = s.Matrix([B1[i,j] for i in range(4) for j in range(i+1,4)] + list(B1*S0))
    return M, rhs, (A,H,T,L,C0,B0,S0)

def produce():
    en, src, old, prior, frame = [json.loads((ROOT/p).read_text()) for p in INPUTS]
    D = list(map(mat,src['target_D'])); J = D[0]*D[1]*D[2]; I = s.eye(4)
    B1,B2 = [mat(x['B']) for x in old['blocks'][0]['repairs']]
    checks = {}
    def ck(name, cond):
        checks[name] = bool(cond)
        assert cond, name
    ck('Clifford_mass_algebra', all(D[i]*D[j]+D[j]*D[i] == (2*I if i==j else s.zeros(4)) for i in range(3) for j in range(3)) and B1*J==B2 and J*J==-I)
    ck('reused_complete_Gram_bank', prior['identities']['Gram_span_dimension']==4 and all(prior['checks'].values()))
    a=s.symbols('a0:3'); al,b,v,u,up,m,n,p,q,r,t=s.symbols('alpha b v u up m n p q r t')
    B=m*B1+n*B2; Bp=p*B1+q*B2; Bpp=r*B1+t*B2
    V=u*I-24*al*D[0]*Bp-24*sum((a[i]*D[i]*B*J for i in range(3)),s.zeros(4))
    Vp=up*I-24*al*D[0]*Bpp-24*sum((a[i]*D[i]*Bp*J for i in range(3)),s.zeros(4))
    G=a[0]*J+b*D[0]*J
    Z=(-v*I+D[0]/24)*Vp+B*V-V*B+al*Bpp-G*Bp
    angular=s.trace((D[0]*B*J).T*Z)
    ck('full_angular_trace',s.expand(angular-96*al*v*(m*t-n*r)-4*(24*a[0]*v+b)*(m*p+n*q))==0)
    R,w,wp=s.symbols('R omega omega_prime')
    jet={m:R,n:0,p:0,q:R*w,r:-R*w*w,t:R*wp,up:0}
    Z0=Z.subs(jet,simultaneous=True)
    ck('phase_acceleration_trace',s.expand(s.trace((D[0]*B2).T*Z0)-96*al*v*R*wp)==0)
    expected=[-4*R*w*(24*a[0]*v+24*al*v*w+b),-96*R*a[1]*v*w,-96*R*a[2]*v*w]
    for i in range(3):
        ck('constant_phase_projection_'+str(i),s.expand(s.trace((D[i]*B1).T*Z0)-expected[i])==0)
    ck('circular_positive_Gram_survives',zero(Z0.subs({wp:0,a[0]:-al*w,a[1]:0,a[2]:0,b:0})))
    witnesses=[]
    for ix,(er,sr,kr) in enumerate(zip(en['blocks'],src['blocks'],old['blocks'])):
        M,rhs,data=tangent_system(er,sr,kr,D,J,v)
        A,H,T,L,C0,B0,S0=data
        ck('frame_leading_'+str(ix),all(T[i]*L==J*T[i] and L*A[i]==A[i]*L for i in range(3)))
        ck('frame_conservation_'+str(ix),zero(H*C0+C0.T*H) and zero(B0+B0.T))
        ck('massless_base_first_'+str(ix),all(zero(T[i]*C0-B0*T[i]+S0*A[i]-D[i]*S0/24) for i in range(3)))
        ck('massless_base_zero_'+str(ix),zero(S0*C0-B0*S0))
        sign=1 if ix<2 else -1
        f=s.Rational(1,16) if ix in (0,3) else s.Rational(1,8)
        entries={4:-v/2,7:sign*(s.Rational(11,192)-v/4),8:sign*(v/4+s.Rational(11,192)),11:sign*s.Rational(1,16),12:-sign*s.Rational(1,16),18:sign*f,21:sign*f,39:sign*s.Rational(25,192),40:-sign*s.Rational(25,192)}
        y=s.zeros(70,1)
        for j,x in entries.items(): y[j]=x
        ck('all_speed_tangent_annihilator_'+str(ix),zero(y.T*M))
        ck('all_speed_tangent_contradiction_'+str(ix),s.expand((y.T*rhs)[0]-v)==0)
        ck('static_tangent_control_'+str(ix),M.subs(v,0).to_DM().rank()==M.subs(v,0).row_join(rhs).to_DM().rank())
        witnesses.append([[j,str(x)] for j,x in entries.items()])
    # Exact spectral reduction for the one-dimensional target, not the source lift.
    momentum,aa,bb,lam=s.symbols('p a b lambda',real=True)
    K=-s.I*J; beta=-s.I*B1; F=D[0]*K
    HH=momentum*D[0]+R*beta+aa*K+bb*F
    ck('spectral_involution',F*F==I and F.conjugate().T==F and s.trace(F)==0)
    ck('spectral_commutant',HH*F==F*HH)
    for e in (-1,1):
        Pi=(I+e*F)/2
        ck('band_projector_'+str(e),Pi*Pi==Pi and s.trace(Pi)==2)
        ck('band_square_'+str(e),zero(((HH-e*bb*I)**2-((momentum+e*aa)**2+R**2)*I)*Pi))
    cp=HH.charpoly().as_expr(); cp=cp.subs(next(iter(cp.free_symbols-{momentum,aa,bb,R})),lam)
    ck('band_characteristic_polynomial',s.expand(cp-((lam-bb)**2-(momentum+aa)**2-R**2)*((lam+bb)**2-(momentum-aa)**2-R**2))==0)
    return {'result_id':'K1885','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL',
            'identities':{'angular_trace_coefficient':96,'angular_radial_remainder':'4*(24*a1*v+b)*(m*m_prime+n*n_prime)','phase_second_derivative':0,'uniform_phase_only':True,'frame_target':'R*B1+(v*omega/2)*J-(omega/48)*D1*J','line_bands':'s*b +/- sqrt((p+s*a)^2+R^2)','line_gap':'max(0,abs(R)-abs(omega)/48)','tangent_normalization_omega':2,'tangent_dual_rhs':'v'},
            'tangent_dual_witnesses':witnesses,
            'scope':{'fixed_positive_symbols_and_leading_observation':True,'nonzero_travelling_speed':True,'nonzero_amplitude_for_phase':True,'canonical_massless_base_no_differentiable_constant_frame_mass_branch':True,'general_constant_frame_lift_excluded':False,'general_rotating_lift_excluded':False,'source_native_identification':False,'band_formula_one_spatial_dimension_only':True,'rotating_frame_gap_is_Floquet_gap':False,'odd_winding_changes_periodic_domain':True},
            'checks':checks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS}}

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--write',action='store_true');parser.add_argument('--output',type=Path);args=parser.parse_args()
    result=produce(); dest=args.output or OUT
    if args.write: dest.write_text(json.dumps(result,indent=2)+'\n')
    else: assert result==json.loads(dest.read_text()),'certificate drift'
    print('PASS K1885',len(result['checks']),'matrix/polynomial groups;',len(result['inputs']),'pins')
