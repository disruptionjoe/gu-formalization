#!/usr/bin/env python3
"""Sparse exact cubic endpoint test on the owned W2 analytic branch.

Reuses authenticated branch coordinates and endpoint receiver polynomials.
Recomputes the full ambient cubic coefficient using native D/Phi/K/N on
three small forms. No root replay, full59 D census or new K/N construction.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
CERT = 'lab/process/source-action-endpoint-cubic-certificates.json'
DATA = 'lab/process/source-action-deep-coefficients.json'
OLD_CERT = 'lab/process/source-action-endpoint-onshell-certificates.json'
OLD_PROBE = 'tests/program-focus/source_action_endpoint_onshell_probe.py'
OLD_EVIDENCE = 'lab/process/source-action-endpoint-onshell.json'
THETA = 'lab/process/source-action-theta-divergence-certificates.json'
GEOMETRY = 'tests/program-focus/source_action_deep_geometry.py'
ALGEBRA = 'tests/program-focus/source_action_deep_algebra.py'
DEPENDENCIES = (DATA, OLD_CERT, OLD_PROBE, OLD_EVIDENCE, THETA, GEOMETRY, ALGEBRA,
    'explorations/conditional-build/source-action-endpoint-onshell-2026-11-27.md',
    'explorations/conditional-build/source-action-homogeneous-analytic-vacuum-2026-11-25.md',
    'explorations/conditional-build/source-action-dynamics-and-continuation-2026-11-25.md')


def require(value, message):
    if not value:
        raise AssertionError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def form_record(form):
    return [[e,c,str(v)] for (e,c),v in sorted(form.items()) if v]


def coords_record(coords):
    return {str(i):str(v) for i,v in sorted(coords.items()) if v}


def clean(coords):
    return {i:v for i,v in coords.items() if v}


def add(*vectors):
    out = {}
    for vector in vectors:
        for i,v in vector.items():
            out[i] = out.get(i,Q(0))+v
    return clean(out)


def scale(c, vector):
    return clean({i:c*v for i,v in vector.items()})


def build_certificate(repo, progress=False):
    started = time.monotonic()
    checks = {}

    def check(label, value):
        require(label not in checks,'unique check label')
        require(value,label)
        checks[label] = True

    def announce(stage, **values):
        if progress:
            print(json.dumps({'stage':stage,'seconds':time.monotonic()-started,**values}),
                  file=sys.stderr,flush=True)

    inputs = {name:sha(repo/name) for name in DEPENDENCIES}
    old = json.loads((repo/OLD_CERT).read_text())
    evidence = json.loads((repo/OLD_EVIDENCE).read_text())
    check('endpoint_producer_custody',old['final_probe_sha256']==inputs[OLD_PROBE])
    check('endpoint_accepted_certificate_custody',evidence['current_sha256'][OLD_CERT]==inputs[OLD_CERT])
    for name,digest in old['native_inputs_sha256'].items():
        check('inherited_input_custody:'+name,sha(repo/name)==digest)
    inherited_coefficients = old['analytic_branch']['coefficients']
    check('inherited_full_C1_C2_zero_not_recomputed',
          inherited_coefficients==[{'order':1,'coefficient':[]},{'order':2,'coefficient':[]}])
    data = json.loads((repo/DATA).read_text())
    theta = json.loads((repo/THETA).read_text())
    check('inherited_complete_59_family',data['closed'] and data['coefficients_complete'] and data['dimension']==59)
    branch = [{int(k):Q(v) for k,v in row['T_coordinates'].items()}
              for row in theta['small_h_branch']['coefficients']]
    check('three_owned_branch_coefficients',len(branch)==3 and
          [row['order'] for row in theta['small_h_branch']['coefficients']]==[1,2,3])
    source = {int(k):Q(v) for k,v in data['S'].items()}

    def linear(vector):
        return add(*(scale(v,{int(k):Q(c) for k,c in data['K'][str(j)].items()})
                     for j,v in vector.items()))

    def bilinear(left, right):
        return add(*(scale(a*b,{int(k):Q(c) for k,c in
                     data['N'][f'{min(i,j)},{max(i,j)}'].items()})
                     for i,a in left.items() for j,b in right.items()))

    t1,t2,t3 = branch
    check('t1_minus_source',t1==scale(-1,source))
    check('t2_recurrence',t2==scale(-1,linear(t1)))
    check('t3_recurrence',t3==scale(-1,add(linear(t2),bilinear(t1,t1))))
    check('wrong_N_sign_in_t3_rejected',t3!=add(scale(-1,linear(t2)),bilinear(t1,t1)))
    receiver = next(r for r in old['receivers'] if r['id']=='KS_pivot_4')
    witness = (receiver['exterior_mask'],receiver['Clifford_mask'])
    check('owned_horizontal_receiver',witness==(1,33) and receiver['horizontal'] and
          Q(receiver['native_coordinate_weight'])==8 and Q(receiver['optional_4D_index_raise'])==1)
    polynomial = receiver['polynomial']
    check('owned_linear_receiver_identically_zero',polynomial['linear']=={})
    qtable = {tuple(map(int,key.split(','))):Q(v)
              for key,v in polynomial['symmetric_quadratic_upper'].items()}
    scalar = 2*sum(a*b*qtable.get((min(i,j),max(i,j)),Q(0))
                   for i,a in t1.items() for j,b in t2.items())
    check('known_answer_from_owned_three_pairs',scalar==Q(183,8))
    check('missing_symmetric_factor2_rejected',scalar/2!=scalar)
    check('wrong_T1_sign_rejected',-scalar!=scalar)
    check('double_receiver_weight_division_rejected',scalar/8!=scalar)
    announce('inherited_receiver_coefficient',C3=str(scalar),receiver=list(witness))

    # Import definitions only: no old build_certificate or main is invoked.
    old_module = load_module(repo/OLD_PROBE,'endpoint_cubic_inherited_helpers')
    geometry = load_module(repo/GEOMETRY,'source_action_deep_geometry')
    algebra = load_module(repo/ALGEBRA,'endpoint_cubic_native_algebra')
    engine = algebra.Engine(geometry)
    basis = [{(int(e),int(c)):Q(v) for e,c,v in row} for row in data['basis']]
    check('native_Gram_custody',list(engine.d)==list(map(Q,data['gram'])))
    active = sorted(set(t1)|set(t2)|set(t3))
    pivots = [tuple(p) for p in data['pivots']]
    check('active_basis_pivots',all(basis[j].get(pivots[i],Q(0))==int(i==j)
                                  for i in active for j in active))

    def expand(vector):
        return algebra.add(*(algebra.scale(v,basis[i]) for i,v in vector.items()))

    T1,T2,T3 = map(expand,branch)
    check('native_real_skew_branch_forms',all(engine.real_skew(T) for T in (T1,T2,T3)))
    check('native_t2_recurrence',T2==algebra.scale(-1,engine.K(T1)))
    K2 = engine.K(T2)
    N11 = engine.N_diag(T1)
    check('native_Kt2_table',K2==expand(linear(t2)))
    check('native_Nt1t1_table',N11==expand(bilinear(t1,t1)))
    check('native_t3_recurrence',T3==algebra.scale(-1,algebra.add(K2,N11)))
    D3 = engine.D(T3)
    check('independent_covariant_Dt3',D3==old_module.direct_D(T3,geometry,algebra))
    P3 = engine.Phi(D3)
    K3 = engine.K(T3)
    check('native_Kt3_table',K3==expand(linear(t3)))
    check('P_t3_nested_Hodge_control',P3==engine.star_inverse(engine.shiab(D3)))
    W12 = engine.wedge(T1,T2,'comm')
    check('raw_vs_commutator_wedge_polarization',W12==algebra.add(engine.wedge(T1,T2),engine.wedge(T2,T1)))
    PW12 = engine.Phi(W12)
    check('mixed_Phi_nested_Hodge_control',PW12==engine.star_inverse(engine.shiab(W12)))
    N12 = engine.N(T1,T2)
    check('native_Nt1t2_table',N12==expand(bilinear(t1,t2)))
    C3 = algebra.add(P3,algebra.scale(-1,K3),PW12,algebra.scale(-2,N12))
    check('native_full_C3_real_skew',engine.real_skew(C3))
    check('native_C3_receiver_matches_owned_polynomial',C3.get(witness,Q(0))==scalar)
    check('linear_native_t3_receiver_zero',algebra.add(P3,algebra.scale(-1,K3)).get(witness,Q(0))==0)
    Z = {witness:Q(1)}
    weight = engine.weight(*witness)
    H = algebra.scale(1/weight,engine.Phi_adj(Z))
    old_H = {(e,c):Q(v) for e,c,v in receiver['dual_form']}
    check('native_receiver_weight8',weight==8)
    check('native_dual_matches_owned_dual',H==old_H)
    check('native_mixed_Phi_adjoint',engine.pair(H,W12)==PW12.get(witness,Q(0)))
    check('raw_pairing_needs_weight',engine.pair(Z,C3)==8*scalar and engine.pair(Z,C3)!=scalar)
    pair_controls = []
    for i in sorted(t1):
        j = next(iter(t2))
        Wij = engine.wedge(basis[i],basis[j],'comm')
        Nij = engine.N(basis[i],basis[j])
        native = engine.Phi(Wij).get(witness,Q(0))/2-Nij.get(witness,Q(0))
        check(f'native_receiver_pair_{i}_{j}',native==qtable[(i,j)])
        pair_controls.append({'indices':[i,j],'Qij':str(native)})
    horizontal = {key:v for key,v in C3.items() if key[0] in (1,2,4,8)}
    check('horizontal_C3_nonzero',bool(horizontal) and scalar>0)
    announce('full_native_coefficient',support=len(C3),horizontal_support=len(horizontal),
             receiver_value=str(C3[witness]))
    return {'schema':'gu-endpoint-cubic-certificate-v1','data_only':True,
        'probe_sha256':sha(Path(__file__).resolve()),'native_inputs_sha256':inputs,
        'inherited_policy':'C1=C2=0, full-carrier/convergence/coupled-stationarity proofs and root results are authenticated dependencies. Their old probes and root certificates are not replayed.',
        'formula':{'h':'1/kappa','series':'T(h)=h*t1+h^2*t2+h^3*t3+O(h^4)',
            't1':'-S','t2':'K*S','t3':'-K^2*S-N(S,S)',
            'C3':'(Phi D_B-K)t3+Phi(t1 wedge t2+t2 wedge t1)-2N(t1,t2)',
            'receiver':'c.t3+2*t1^T Q*t2; c is the identically zero stored row',
            'Q_convention':'symmetric Qij; upper-triangle off-diagonal polynomial coefficients are 2Qij',
            'truncation_warning':'Original kappa*T=T/h requires t4 to recover its h3 coefficient; this test uses the exact E-eliminated defect and computes no h4 endpoint coefficient.'},
        'branch_coordinates':[{'order':i+1,'coordinates':coords_record(t)} for i,t in enumerate(branch)],
        'receiver':{'id':'KS_pivot_4','exterior_mask':1,'Clifford_mask':33,
            'name':'coefficient of theta0 gamma05','weight':str(weight),
            'dual_form':form_record(H),'active_quadratic_entries':pair_controls,
            'linear_row_zero':True,'coefficient_h3':str(scalar),
            'literal_flat_section_survives':True,'four_dimensional_index_raise':'1'},
        'full_ambient_C3':form_record(C3),'full_ambient_support':len(C3),
        'horizontal_C3':form_record(horizontal),'horizontal_support':len(horizontal),
        'checks':checks,'check_count':len(checks),
        'native_work':{'branch_forms':3,'active_basis_indices':active,'root_replays':0,
            'full_59_D_columns':0,'new_full_KN_tensors':False},
        'analytic_consequence':'Owned convergence and full C1=C2=0 imply this receiver is (183/8)h^3+O(h^4), hence positive for every sufficiently small positive h. No numerical radius or connection to either kappa1 root is inferred.',
        'scope':'Fixed W2/K95 candidate, full ambient adjoint fibre and literal pullback of the raised one-form. No pullback of degree13 Upsilon, source uniqueness, physical metric equation, global finite-action field or GU verdict.',
        'not_run':['Old full endpoint/theta certificates','Root search, inverse construction or root replay',
            'Full59 native tensor census','Endpoint h4 or higher test','Lean compilation'],
        'timing_policy':'Only ephemeral receipts include runtime and certificate byte count.'}


def write_json(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary = path.with_suffix(path.suffix+'.new')
    temporary.write_text(json.dumps(value,indent=2,sort_keys=True)+'\n')
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=ROOT)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write-certificate',action='store_true')
    mode.add_argument('--verify',action='store_true')
    parser.add_argument('--certificate',type=Path)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--progress',action='store_true')
    args = parser.parse_args()
    started = time.monotonic()
    repo = args.repo.resolve()
    path = args.certificate or repo/CERT
    actual = build_certificate(repo,args.progress)
    if args.write_certificate:
        write_json(path,actual)
    else:
        require(json.loads(path.read_text())==actual,'exact frozen certificate equality')
    receipt = {'passed':True,'mode':'write-certificate' if args.write_certificate else 'verify',
        'probe_sha256':actual['probe_sha256'],'certificate_sha256':sha(path),
        'certificate_bytes':path.stat().st_size,'checks':actual['check_count'],
        'C3_receiver':actual['receiver']['coefficient_h3'],
        'ambient_support':actual['full_ambient_support'],'horizontal_support':actual['horizontal_support'],
        'seconds':time.monotonic()-started}
    if args.output:
        write_json(args.output,receipt)
    print(json.dumps(receipt,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
