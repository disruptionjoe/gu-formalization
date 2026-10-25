"""Exact resource consumption for the written local-control response theorem."""
from pathlib import Path
from fractions import Fraction as Q
import argparse,json,hashlib
from k2076_separated_detector_locality import upper
ROOT=Path(__file__).resolve().parents[2]
def response(a,action):
    action=Q(action)
    assert action>=0
    return min(Q(1),2*action*upper(a),4*upper(a))
def conditioned(epsilon,leakage):
    epsilon,leakage=Q(epsilon),Q(leakage)
    assert 0<=epsilon<=1 and 0<=leakage<1
    return min(Q(1),epsilon+leakage)
def produce():
    refs=['lab/process/k2076-separated-detector-locality.json','tests/channel-swings/k2076_separated_detector_locality.py','explorations/conditional-build/k2062-bounded-local-multiplier-rigidity-2026-10-25.md','explorations/conditional-build/k2071-confined-pointer-control-2026-10-25.md','explorations/conditional-build/k2067-sector-preserving-pointer-control-2026-10-25.md','lab/process/k2073-confined-pointer-energy.json']
    rows=[]
    for a in [8,12,20,32]:
        for action in ['1/10','1','10','1000']:
            eps=response(a,action)
            rows.append(dict(effective_mass_gap=a,integrated_control_norm=action,remote_record_tv_upper=str(eps),conditional_upper_if_leakage_at_most_1e_6=str(conditioned(eps,Q(1,10**6)))))
    assert response(20,1000)<Q(1,10**7)
    assert response(32,1000)<Q(1,10**12)
    assert response(20,10)==response(20,1000)
    assert conditioned(response(32,1),Q(1,10**6))<Q(1001,10**9)
    tau=Q(1,500);assert Q(14,5)-64*tau*tau>2
    instrument=dict(core_radius_times_mass=2000,duration_times_mass=1,ramp_width_times_mass=1,control_radius_times_mass=2002,click_input_radius_times_mass=2003,amplitude_over_mass='pi/2',integrated_norm='pi/2',tail_norm_upper=str(tau),state_error_upper=str(2*tau),record_tv_upper=str(4*tau*tau),leakage_probability_upper=str(4*tau*tau),two_copy_chsh_lower=str(Q(14,5)-64*tau*tau),spacelike_center_separation_times_mass=4006,scope='prepared Gaussian spatial state and arbitrary internal qubit/entanglement; added ancilla, no physical field embedding')
    return dict(id='K2077',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs},carrier='L2(R3,C4 tensor C352); optional finite ancillary factor',control='strongly measurable bounded Hermitian spatial multiplier V(s), integral ||V(s)|| ds finite',domain='H0 on H1; bounded interaction-picture Dyson propagator; no common H1 invariance assumed for rough V',gap='ell_s=dist(C_s,G)-(T-s)>0 a.e.; uniform ell=dist(closure union_s (C_s)_(T-s),G)>0 for amplitude cap',norm_bound='min(1,2 integral v(s)*eta(m*ell_s) ds,4*eta(m*ell))',uniform_bound='min(1,2*Lambda*eta(m*ell),4*eta(m*ell))',raw_local_response='exactly zero under causal separation',records='compressed remote spatial POVM plus one coarse residual outcome; TV bounded by same epsilon, independent of outcome count',postselection_bound='min(1,epsilon+1-q); no bound from separation alone',resources=rows,strict_resource_targets={'gap20_action_arbitrary':'1/10000000','gap32_action_arbitrary':'1/1000000000000'},bounded_ancilla_instrument=instrument,non_effects=['no exact P preservation','no application to first-order unbounded Hchi','no global ancillary-only readout locality','no locality of sector-failure outcome','no source-selected detector, physical preparation, control energy, novelty or GU confirmation'])
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();d=produce();p=ROOT/'lab/process/k2077-controlled-detector-response.json'
    if args.write:p.write_text(json.dumps(d,indent=2)+'\n')
    else:assert json.loads(p.read_text())==d
    print('PASS 16 exact control/separation resources; amplitude saturation, conditioned tolerance and finite ancilla/Bell resources')
