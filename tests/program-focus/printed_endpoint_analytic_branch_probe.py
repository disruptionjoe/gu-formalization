#!/usr/bin/env python3
"""Exact printed-endpoint branch coefficients; no root search or full tensor rebuild.

Universal analytic existence and homogeneous PDE lifting are written proofs.
This probe recomputes finite coefficients from the native Phi/D/wedge maps.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse, hashlib, importlib.util, json, sys, time
sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
CERT = 'lab/process/printed-endpoint-analytic-branch-certificates.json'
DATA = 'lab/process/source-action-deep-coefficients.json'
CUBIC = 'lab/process/source-action-endpoint-cubic-certificates.json'
THETA = 'lab/process/source-action-theta-divergence-certificates.json'
DEP = [DATA, CUBIC, THETA,
 'tests/program-focus/source_action_deep_geometry.py',
 'tests/program-focus/source_action_deep_algebra.py',
 'tests/program-focus/source_action_theta_divergence_probe.py',
 'tests/program-focus/source_action_endpoint_onshell_probe.py',
 'tests/program-focus/source_action_endpoint_cubic_probe.py',
 'lab/process/source-action-endpoint-cubic.json',
 'lab/process/source-action-theta-divergence.json',
 'explorations/conditional-build/source-action-homogeneous-analytic-vacuum-2026-11-25.md',
 'explorations/conditional-build/source-action-endpoint-cubic-2026-11-27.md',
 'explorations/conditional-build/source-action-theta-divergence-2026-11-27.md']

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p,name):
    s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s)
    sys.modules[name]=m;s.loader.exec_module(m);return m

def record(f): return [[e,c,str(v)] for (e,c),v in sorted(f.items()) if v]
def from_record(r): return {(e,c):Q(v) for e,c,v in r}

def build(repo):
    checks={}
    def ck(label,value):
        assert label not in checks
        if not value: raise AssertionError(label)
        checks[label]=True
    inputs={p:sha(repo/p) for p in DEP}
    cub=json.loads((repo/CUBIC).read_text());th=json.loads((repo/THETA).read_text())
    data=json.loads((repo/DATA).read_text())
    # Check the inherited certificate against its own producer and dependency pins.
    ck('cubic_producer',cub['probe_sha256']==inputs['tests/program-focus/source_action_endpoint_cubic_probe.py'])
    for p,d in cub['native_inputs_sha256'].items(): ck('cubic_dependency:'+p,sha(repo/p)==d)
    ce=json.loads((repo/'lab/process/source-action-endpoint-cubic.json').read_text())
    ck('accepted_cubic_certificate',ce['verification']['root_replay']['certificate_sha256']==inputs[CUBIC])
    te=json.loads((repo/'lab/process/source-action-theta-divergence.json').read_text())
    ck('accepted_theta_certificate',te['current_sha256'][THETA]==inputs[THETA])
    g=load(repo/DEP[3],'source_action_deep_geometry')
    a=load(repo/DEP[4],'printed_branch_algebra')
    d=load(repo/DEP[5],'printed_branch_divergence')
    direct=load(repo/DEP[6],'printed_branch_direct')
    e=a.Engine(g)
    basis=[from_record(row) for row in data['basis']]
    def expand(coords): return a.add(*(a.scale(Q(v),basis[int(i)]) for i,v in coords.items()))
    old=[expand(row['T_coordinates']) for row in th['small_h_branch']['coefficients']]
    S=e.Phi(e.curvature())
    ck('source_from_actual_curvature',S==expand(data['S']))
    def P(T):
        DT=e.D(T)
        ck('direct_D:'+str(len(checks)),DT==direct.direct_D(T,g,a))
        out=e.Phi(DT)
        ck('nested_Hodge_P:'+str(len(checks)),out==e.star_inverse(e.shiab(DT)))
        return out
    def B(T,U): return a.scale(Q(1,2),e.Phi(a.add(e.wedge(T,U),e.wedge(U,T))))
    u1=a.scale(-1,S);u2=a.scale(-1,P(u1));u3=a.scale(-1,a.add(P(u2),B(u1,u1)))
    branch=[u1,u2,u3]
    for i,u in enumerate(branch):
        ck('native_printed_equals_owned_Euler_coefficient_'+str(i+1),u==old[i])
        ck('native_real_skew_'+str(i+1),e.real_skew(u))
    ck('t1_sign_mutation_detected',u1!=S)
    ck('u3_wrong_quadratic_sign_detected',u3!=a.add(a.scale(-1,e.Phi(e.D(u2))),B(u1,u1)))
    # Compute the missing fourth coefficient, in full ambient coordinates (no projection).
    Pu3=P(u3);mixed=e.Phi(a.add(e.wedge(u1,u2),e.wedge(u2,u1)))
    ck('polarized_wedge',mixed==e.Phi(e.wedge(u1,u2,'comm')))
    u4=a.scale(-1,a.add(Pu3,mixed))
    Ku3=e.K(u3);Nmixed=a.scale(2,e.N(u1,u2))
    t4=a.scale(-1,a.add(Ku3,Nmixed))
    C3=a.add(Pu3,a.scale(-1,Ku3),mixed,a.scale(-1,Nmixed))
    ck('full_C3_recomputed',C3==from_record(cub['full_ambient_C3']))
    ck('fourth_field_difference_is_minus_C3',a.add(u4,a.scale(-1,t4))==a.scale(-1,C3))
    ck('printed_residual_h3_cancels_including_u4',not a.add(u4,Pu3,mixed))
    Ecoeff=a.add(u4,Ku3,Nmixed)
    ck('actual_Euler_h3_on_printed_branch',Ecoeff==a.scale(-1,C3))
    ck('native_horizontal_receiver',Ecoeff.get((1,33))==-Q(183,8))
    ck('missing_fourth_coefficient_is_not_zero',bool(u4))
    ck('truncated_printed_residual_is_not_exact',bool(a.add(Pu3,mixed)))
    ck('u4_real_skew',e.real_skew(u4))
    ck('receiver_pairing_weight_not_divided_twice',e.weight(1,33)==8 and Ecoeff[(1,33)]/8!=Ecoeff[(1,33)])
    divergences=[]
    for i,u in enumerate(branch):
        D=d.coderivative_covariant(u,g);W=d.coderivative_weak(u,g,e);O=d.coderivative_observed(u,g)
        ck('two_independent_coderivatives_'+str(i+1),D==W)
        rows=d.split_one(u)
        ck('observed_minus_ambient_trace_'+str(i+1),a.add(O,a.scale(-1,D))==a.scale(Q(1,4),rows[4]))
        divergences.append({'order':i+1,'ambient':{str(k):str(v) for k,v in D.items()},'observed':{str(k):str(v) for k,v in O.items()}})
    ck('ambient_leading_order3',divergences[0]['ambient']=={} and divergences[1]['ambient']=={} and divergences[2]['ambient']=={'16':'-27/32'})
    ck('observed_leading_order1',divergences[0]['observed']=={'16':'21/16'})
    ck('observed_second_order_zero',divergences[1]['observed']=={})
    ck('parallel_solder_control',not d.coderivative_covariant(e.phi1,g))
    # Raw Clifford identity is a complexified control only, not native u(H); i times it is native.
    trace={(1<<4,0):Q(1)}
    ck('density_control_complexified_trace',d.coderivative_covariant(trace,g)=={0:-Q(1,4)})
    ck('omitted_density_fault_detected',d.coderivative_weak(trace,g,e,omit_divergence=True)!=d.coderivative_covariant(trace,g))
    # Scalar affine controls calibrate the one-order shift for kappa=1/h.
    for s,p,k in [(Q(2),Q(3),Q(3)),(Q(2),Q(3),Q(5)),(Q(-2),Q(0),Q(1))]:
        up=[(-1)**(j+1)*s*p**j for j in range(4)]
        ue=[(-1)**(j+1)*s*k**j for j in range(4)]
        ck('scalar_recurrence:'+str((s,p,k)),all(up[j]+p*up[j-1]==0 for j in range(1,4)))
        ck('scalar_reverse_defect:'+str((s,p,k)),up[1]+k*up[0]==-(p-k)*up[0])
        ck('scalar_equal_operator_control:'+str((s,p,k)),(up==ue)==(p==k))
    return {'schema':'gu-printed-endpoint-branch-certificate-v1','data_only':True,
      'probe_sha256':sha(Path(__file__)),'native_inputs_sha256':inputs,
      'printed_coefficients':[{'order':i+1,'ambient_form':record(u)} for i,u in enumerate(branch+[u4])],
      'fourth_difference':record(a.add(u4,a.scale(-1,t4))),
      'actual_Euler_coefficient_h3':record(Ecoeff),
      'horizontal_receiver':{'form_mask':1,'Clifford_mask':33,'value':'-183/8','pairing_weight':'8','raise_factor':'1'},
      'divergences':divergences,'checks':checks,'check_count':len(checks),
      'inherited_not_replayed':['full216 dimension','59 full tensor census','old root certificates','old complete certificate probes'],
      'scope':'Finite native exact coefficients. Full216 closure and analytic local solution lifting are written/reviewed. No printed59 closure, kappa1, source uniqueness, full source Euler or physical state claim.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',type=Path,default=ROOT)
    m=p.add_mutually_exclusive_group(required=True);m.add_argument('--write-certificate',action='store_true');m.add_argument('--verify',action='store_true')
    a=p.parse_args();t=time.monotonic();c=build(a.repo);path=a.repo/CERT
    if a.write_certificate:path.write_text(json.dumps(c,indent=2,sort_keys=True)+'\n')
    else:
        if json.loads(path.read_text())!=c:raise AssertionError('certificate differs from exact recomputation')
    print(json.dumps({'status':'PASS','checks':c['check_count'],'seconds':time.monotonic()-t,'certificate':str(path)}))
if __name__=='__main__':main()
