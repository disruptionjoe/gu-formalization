#!/usr/bin/env python3
"""Exact dual flux and quantitative bounded variable-frame obstruction."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sympy as s
ROOT=Path(os.environ.get('GU_ROOT',Path(__file__).resolve().parents[2]))
OUT=ROOT/'lab/process/k1887-bounded-variable-frame-rotation.json'
INPUTS=['lab/process/k1832-k77-common-energy-form.json','lab/process/k1836-k77-differential-dirac-quotient.json','lab/process/k1840-k77-conservative-variable-observation.json','lab/process/k1885-traveling-phase-rigidity-and-frame-reduction.json','tests/channel-swings/k1885_traveling_phase_rigidity_and_frame_reduction.py']
def module():
    p=ROOT/'tests/channel-swings/k1885_traveling_phase_rigidity_and_frame_reduction.py'
    spec=importlib.util.spec_from_file_location('k1885_data',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def produce():
    m=module();en,src,old,prior=[json.loads((ROOT/p).read_text()) for p in INPUTS[:4]]
    D=list(map(m.mat,src['target_D']));J=D[0]*D[1]*D[2]
    v,h,R=s.symbols('v h R');checks={};blocks=[]
    def ck(name,condition):
        checks[name]=bool(condition)
        if not condition:raise AssertionError('FAIL '+name)
    for ix,(er,sr,kr) in enumerate(zip(en['blocks'],src['blocks'],old['blocks'])):
        M,rhs,(A,H,T,L,C0,B0,S0)=m.tangent_system(er,sr,kr,D,J,v)
        y=s.zeros(70,1)
        for i,x in prior['tangent_dual_witnesses'][ix]:y[i]=s.sympify(x,locals={'v':v})
        Y=s.Matrix(4,16,list(y[6:,0]));B1=m.mat(kr['repairs'][0]['B']);C1=m.mat(kr['repairs'][0]['C']);S1=m.mat(kr['repairs'][0]['S'])
        ck('all_direction_dual_'+str(ix),m.zero(y.T*M))
        ck('all_speed_forcing_'+str(ix),s.expand((y.T*rhs)[0]-v)==0)
        ck('mass_operator_norm_one_'+str(ix),B1.T*B1==s.eye(4))
        norm=s.factor(s.trace(Y*Y.T));constant=s.Rational(517 if ix in (0,3) else 733,9216)
        ck('dual_norm_'+str(ix),s.expand(norm-v*v/8-constant)==0)
        tn=s.trace(T[0]*T[0].T);expected=s.Rational(12888 if ix in (0,3) else 12792,625)
        ck('leading_norm_'+str(ix),tn==expected)
        ck('static_repair_nonlinear_control_'+str(ix),S1*C1==B1*S1)
        E=h*R*(S0*C1+S1*C0-B0*S1-B1*S0)+R*R*(S1*C1-B1*S1)
        ck('actual_static_slope_defect_'+str(ix),s.expand(s.trace(Y.T*E)+h*R*v)==0)
        ck('scaled_bank_identity_'+str(ix),m.zero((h*y[:6,0].T).row_join(y[6:,0].T)*M[:6,:].col_join(h*M[6:,:])))
        blocks.append({'type':ix,'dual_entries':prior['tangent_dual_witnesses'][ix], 'dual_norm_squared':str(norm),'T1_Frobenius_squared':str(tn)})
    # Exact algebra underlying the quadratic lower bound, without rounding.
    a,r=s.symbols('a r',positive=True);eps=(s.sqrt(r*r+4*a)-r)/2
    ck('quadratic_distance_root',s.simplify(eps*(eps+r)-a)==0)
    ck('positive_rationalized_distance_root',s.simplify(eps-2*a/(s.sqrt(r*r+4*a)+r))==0)
    return {'result_id':'K1887','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','identities':{'h':'omega/2','flux':'lambda_prime = h*R*v - <Y,s*c-R*B1*s>','nonlinear_distance':'abs(h*R*v) <= N_v*epsilon_s*(epsilon_c+abs(R))','equal_norm_floor':'(sqrt(R^2+4*abs(h*R*v)/N_v)-abs(R))/2','tangent_flux':'lambda_1_prime=h*v','finite_interval':'abs(h*R*v) <= 2*N_v*(t*epsilon_c+(abs(v)+1/24)*epsilon_s)/ell+N_v*epsilon_s*(epsilon_c+abs(R))','residual_floor':'max(0,abs(h*R*v)/N_v-epsilon_s*(epsilon_c+abs(R)))'},'blocks':blocks,'scope':{'fixed_pointwise_bank':True,'bounded_whole_line_or_periodic':True,'canonical_base':True,'variable_frame_coefficients_allowed':True,'no_bounded_differentiable_mass_branch':True,'nonlinear_distance_is_necessary_only':True,'local_lifts_excluded':False,'all_rotating_lifts_excluded':False,'square_root_branch_constructed':False,'native_GU_identification':False,'approximate_first_order_bank_covered':False},'checks':checks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS}}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');p.add_argument('--output',type=Path);a=p.parse_args();d=produce();dest=a.output or OUT
    if a.write:dest.write_text(json.dumps(d,indent=2)+'\n')
    else:
        if d!=json.loads(dest.read_text()):raise AssertionError('FAIL certificate drift')
    print('PASS K1887',len(d['checks']),'exact dual/budget groups;',len(d['inputs']),'pins')
