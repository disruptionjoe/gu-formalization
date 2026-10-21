#!/usr/bin/env python3
"""Boundary inertia and explicit positive/negative support-flux witnesses."""
import argparse,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
INPUTS=['lab/process/k1832-k77-common-energy-form.json','lab/process/k1836-k77-differential-dirac-quotient.json','lab/process/k1888-bounded-support-energy-inverse.json']
OUT='lab/process/k1890-preparation-evolution-boundary-incompatibility.json'
def mat(d):
    a=s.zeros(d.get('rows',16),d.get('columns',16))
    for i,j,v in d['entries']:a[i,j]=s.Rational(v)
    return a

def encode(M):return {'rows':M.rows,'columns':M.cols,'entries':[[i,j,str(M[i,j])] for i in range(M.rows) for j in range(M.cols) if M[i,j]]}
def produce(root=ROOT):
    en,ob,_=[json.loads((root/p).read_text()) for p in INPUTS];D=list(map(mat,ob['target_D']));alpha=s.Rational(138,25);checks={};blocks=[]
    def ck(n,b):
        checks[n]=bool(b)
        if not b:raise AssertionError('FAIL '+n)
    for j,(e,o) in enumerate(zip(en['blocks'],ob['blocks'])):
        H=mat(e['H']);A=mat(e['matrices'][0]);T=mat(o['T'][0]);F=H*A;N=s.Matrix.hstack(*T.nullspace());V=F.inv()*T.T;Q=T*V
        ck('symmetrized_flux_'+str(j),F==F.T and F.det()!=0)
        ck('source_inertia_'+str(j),A.eigenvals()=={s.S.One:6,-s.S.One:6,s.Rational(1,24):2,s.Rational(-1,24):2})
        ck('actual_principal_observation_'+str(j),T*A==D[0]*T/24)
        ck('normal_observation_gram_'+str(j),T*H.inv()*T.T==alpha*s.eye(4))
        ck('flux_complement_'+str(j),Q==24*alpha*D[0] and Q*Q==(24*alpha)**2*s.eye(4) and s.trace(Q)==0)
        ck('kernel_dimension_'+str(j),N.shape==(16,12) and T*N==s.zeros(4,12))
        ck('orthogonal_direct_sum_'+str(j),N.T*F*V==s.zeros(12,4) and N.row_join(V).det()!=0)
        # Actual invisible speed+1/-1 eigenspaces are a concrete repair construction.
        plus=(A-s.eye(16)).nullspace();minus=(A+s.eye(16)).nullspace();P=s.Matrix.hstack(*plus);M=s.Matrix.hstack(*minus)
        ck('invisible_characteristic_spaces_'+str(j),len(plus)==len(minus)==6 and T*P==T*M==s.zeros(4,6))
        ck('opposite_flux_witnesses_'+str(j),(plus[0].T*F*plus[0])[0]>0 and (minus[0].T*F*minus[0])[0]<0)
        # Slow modes are complementary visible incoming/outgoing sectors.
        slowp=s.Matrix.hstack(*(A-s.eye(16)/24).nullspace());slowm=s.Matrix.hstack(*(A+s.eye(16)/24).nullspace())
        ck('visible_slow_spaces_'+str(j),(T*slowp).rank()==(T*slowm).rank()==2)
        blocks.append({'kernel_basis':encode(N),'complement_basis':encode(V),'complement_flux':encode(Q),'positive_invisible_witness':encode(plus[0]),'negative_invisible_witness':encode(minus[0]),'kernel_inertia':[6,6,0],'whole_inertia':[8,8,0],'complement_inertia':[2,2,0]})
    return dict(result_id='K1890',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',blocks=blocks,dimensions={'zero_flux_trace':12,'largest_isotropic_zero_flux_trace':6,'required_separated_selfadjoint_trace':8,'minimum_observed_boundary_rank':2,'paired_endpoint_zero_flux_max_isotropic':12,'paired_endpoint_required':16,'minimum_total_observed_boundary_rank':4},scope={'conditional_constant_source_system':True,'preparation_domain_can_be_unitary_evolution_domain':False,'no_modewise_unitary_extension_contained_in_zero_flux':True,'all_boundary_conditions_excluded':False,'reflection_repair_constructed_algebraically':True,'massless_normal_repaired_domain_intertwining':True,'massive_or_tangential_repaired_domain_intertwining':False,'native_GU':False},checks=checks,inputs={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in INPUTS})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=produce()
 if a.write:(ROOT/OUT).write_text(json.dumps(d,indent=2)+'\n')
 elif d!=json.loads((ROOT/OUT).read_text()):raise AssertionError('FAIL certificate drift')
 print('PASS K1890',len(d['checks']),'exact matrix groups;',len(INPUTS),'pins; inertia/dimension proof analytic')
