#!/usr/bin/env python3
"""Lightweight custody and exact arithmetic for the finite-loss argument.

This does not verify the classical-PDO Taylor remainder, packet estimates,
norm-transfer theorem, source necessity, or a physical instability.
No native operator assembly, inverse regeneration, or PDE simulation is run.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse, ast, base64, hashlib, json, re, sys, time, zlib
sys.dont_write_bytecode=True

BUNDLE='lab/process/source-action-finite-loss-certificates.json'
BLOCKS={'even0':(0,183,211),'odd0':(0,196,196),'even1':(1,512,480),
        'odd1':(1,496,496),'even2':(2,576,592),'odd2':(2,584,584),'even3':(3,490,462)}
CLAIMS={'SC-ACT-01':'ASSERTS','SC-ACT-02':'ASSERTS','SC-META-52':'UNCERTAIN','SC-META-53':'UNCERTAIN'}
ASSUMPTIONS={
 'graph_norm_transfer':{
  'statement':'On the same compact non-null microlocal graph core, Jv=(v,-dv), v=S w with S=E diag(Lambda,1), and N_s(v) is microlocally equivalent to ||w||H^s modulo arbitrarily smoothing remainder, for states AND range residual f.',
  'forcing':'The forcing norm is the graph norm of (f,-df), f=(partial_t-L)v; it is not an unweighted original-PDE forcing norm.',
  'verification':'Written analytic proof and independent review; not verified by this probe.'},
 'alternative_norm_sandwich':{
  'statement':'On the SAME graph core and with the same graph forcing, ||w||H^(-a) <= C||w||Y <= Cprime||w||H^b for finite a,b. A bounded Y Duhamel estimate would then imply a fixed finite-loss Sobolev estimate.',
  'examples':'An elliptic finite-order invertible transformation with a parametrix qualifies when these estimates hold. A non-elliptic projection or infinite-order weight need not qualify.',
  'verification':'Hypotheses of the written norm-transfer corollary, not established for a source-selected physical norm by this probe.'}}

def jd(value):return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def sha(raw):return hashlib.sha256(raw).hexdigest()
def path_in(repo,name):
    path=(repo/name).resolve();assert path.is_relative_to(repo)and not Path(name).is_absolute(),('outside repository',name)
    return path
def file_sha(path):
    h=hashlib.sha256()
    with path.open('rb')as f:
        for block in iter(lambda:f.read(1<<20),b''):h.update(block)
    return h.hexdigest()
def write(path,value):
    path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_suffix(path.suffix+'.new')
    tmp.write_text(json.dumps(value,indent=2)+'\n');tmp.replace(path)
def check_paths(repo,mapping,files):
    for name,expected in mapping.items():
        assert isinstance(expected,str)and re.fullmatch('[0-9a-f]{64}',expected)
        actual=file_sha(path_in(repo,name));assert actual==expected,('dependency changed',name)
        files[name]=actual
def load(repo,name,files):
    path=path_in(repo,name);raw=path.read_bytes();files[name]=sha(raw);return json.loads(raw)
def unpack(record):
    assert record['encoding']=='zlib-base64-json'
    raw=zlib.decompress(base64.b64decode(record['data'],validate=True))
    assert len(raw)==record['uncompressed_bytes']and sha(raw)==record['sha256']
    return json.loads(raw)
def function_sources(path,names):
    source=path.read_text();lines=source.splitlines(keepends=True);tree=ast.parse(source)
    nodes={n.name:n for n in tree.body if isinstance(n,ast.FunctionDef)}
    return [''.join(lines[nodes[n].lineno-1:nodes[n].end_lineno])for n in names]
def prior_result(repo,name,files):
    result=load(repo,name,files);check_paths(repo,result['current_sha256'],files)
    replay=result['verification']['replay'];assert replay['passed']and not replay['floating_inverse_regenerated']
    return result
def complex_mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def l1(a):return abs(a[0])+abs(a[1])

def intrinsic_inputs(repo,files,roots):
    result=prior_result(repo,'lab/process/source-action-onshell-dynamics.json',files)
    name='lab/process/source-action-onshell-dynamics-certificates.json';bundle=load(repo,name,files)
    assert bundle['schema']=='gu-onshell-dynamics-certificates-v1'and bundle['data_only']
    producer='tests/program-focus/source_action_onshell_dynamics_probe.py'
    assert bundle['final_probe_sha256']==file_sha(path_in(repo,producer))
    check_paths(repo,bundle['bindings'],files)
    expected={'onshell-sources.json','onshell-current.json','onshell-boost.json','onshell-spin0-scope.json','onshell-principal.json','onshell-intrinsic.json'}
    assert set(bundle['records'])==expected
    records={n:unpack(r)for n,r in bundle['records'].items()}
    for row in records.values():
        assert row['complete']and row['execution_probe_sha256']==bundle['final_probe_sha256']and row['bindings']==bundle['bindings']
    intrinsic=records['onshell-intrinsic.json'];principal=records['onshell-principal.json']
    assert intrinsic['principal_record_sha256']==bundle['records']['onshell-principal.json']['sha256']
    assert principal['direction_beta_dF_C_CK_nonzero']
    assert all(principal['signed_adjoint_controls'].values())
    owned=intrinsic['owned_operator'];scalar=load(repo,owned['bundle'],files)
    assert files[owned['bundle']]==owned['bundle_sha256']
    assert scalar['final_probe_sha256']==file_sha(path_in(repo,'tests/program-focus/source_action_scalar_normal_operator_probe.py'))
    check_paths(repo,scalar['native_inputs'],files)
    for n,h in owned['records'].items():assert scalar['records'][n]['sha256']==h;unpack(scalar['records'][n])
    assert result['verification']['replay']['bundle_sha256']==files[name]
    assert result['verification']['replay']['probe_sha256']==bundle['final_probe_sha256']
    assert [r['root']for r in intrinsic['roots']]==[0,1]
    checked=[]
    for row,root in zip(intrinsic['roots'],roots):
        assert row['owned_root_sha256']==jd(root)and Q(row['radius'])==Q(root['certificate']['radius'])
        assert row['trace_exact_zero_by_full_family_B']
        H=[[(Q(a),Q(b))for a,b in r]for r in row['H_intrinsic']['center']]
        E=[[Q(z)for z in r]for r in row['H_intrinsic']['entry_l1_error']]
        assert len(H)==len(E)==20 and all(len(r)==20 for r in H+E)
        assert all(e>=0 for r in E for e in r)
        assert (sum(H[i][i][0]for i in range(20)),sum(H[i][i][1]for i in range(20)))==(0,0)
        products=[complex_mul(H[i][j],H[j][i])for i in range(20)for j in range(20)]
        moment=(sum(z[0]for z in products),sum(z[1]for z in products))
        error=sum(l1(H[i][j])*E[j][i]+E[i][j]*l1(H[j][i])+E[i][j]*E[j][i]for i in range(20)for j in range(20))
        saved=row['trace_H_intrinsic_squared'];lower,upper=moment[0]-error,moment[0]+error
        assert tuple(map(Q,saved['center']))==moment and Q(saved['l1_error'])==error
        assert Q(saved['real_lower'])==lower and Q(saved['real_upper'])==upper
        assert lower>Q(19,80)==20*19*Q(1,40)**2
        assert row['max_real_eigenvalue_above_1_over_40']and saved['positive_certified']
        checked.append({'root':row['root'],'root_record_sha256':jd(root),'radius':row['radius'],
                        'exact_real_lower':str(lower),'exact_real_upper':str(upper),
                        'strict_margin_over_19_over_80':str(lower-Q(19,80)),
                        'center_trace_and_400_product_terms_recomputed':True,
                        'whole_family_trace_zero_proof_authenticated_not_reproved':True})
    return {'bundle_sha256':files[name],'producer_sha256':bundle['final_probe_sha256'],
            'records_sha256':{n:r['sha256']for n,r in bundle['records'].items()},'roots':checked,
            'spectral_bridge':'The separately proved full-family trace-zero/trace-square lemma gives max Re eigenvalue>1/40. The maximal real part rho of the FULL finite microlocal principal is at least that positive block value; no full spectrum is computed.',
            'prior_native_replay_authenticated_not_rerun':True}

def full_M_inputs(repo,files,roots):
    result=prior_result(repo,'lab/process/source-action-full-auxiliary.json',files)
    name='lab/process/source-action-full-auxiliary-certificates.json';m=load(repo,name,files)
    producer='tests/program-focus/source_action_full_auxiliary_probe.py';source=path_in(repo,producer)
    assert m['schema']=='gu-full-auxiliary-manifest-v1'and m['data_only']
    assert m['final_probe_sha256']==file_sha(source);check_paths(repo,m['native_inputs'],files)
    assert result['verification']['replay']['manifest_sha256']==files[name]
    assert result['verification']['replay']['probe_sha256']==m['final_probe_sha256']
    expected={f'source-action-full-auxiliary-{label}-root{ri}-certificates.json'for label in BLOCKS for ri in(0,1)}
    assert set(m['bundles'])==expected
    record_hashes={n:h for meta in m['bundles'].values()for n,h in meta['records'].items()}
    procedure=sha('\n'.join(function_sources(source,['load_block','stage_certify'])).encode())
    status={(r['block'],r['B_sector'],r['root']):r for r in m['authenticated_status']['certificates']}
    assert len(status)==28 and m['authenticated_status']['all28pass']
    bounds=[]
    for label,(spin,plus,minus)in BLOCKS.items():
        for ri,root in enumerate(roots):
            bn=f'source-action-full-auxiliary-{label}-root{ri}-certificates.json';meta=m['bundles'][bn]
            path=path_in(repo,'lab/process/'+bn);assert file_sha(path)==meta['sha256']and path.stat().st_size==meta['bytes']
            b=load(repo,'lab/process/'+bn,files)
            assert b['schema']=='gu-full-auxiliary-sector-data-v1'and b['data_only']and b['final_probe_sha256']==m['final_probe_sha256']
            assert(b['block'],b['root'])==(label,ri)and set(b['records'])==set(meta['records'])
            assert all(r['sha256']==meta['records'][n]for n,r in b['records'].items())
            for sector,n in enumerate((plus,minus)):
                prefix=label+('-plus'if sector==0 else'-minus');stem=prefix+f'-root{ri}'
                cn=stem+'-certificate.json';cert=unpack(b['records'][cn]);bind=cert['bindings']
                assert cert['complete']and cert['dimension']==n and cert['native_M_invertible_on_complete_sector']
                assert bind['native_inputs']==m['native_inputs']and bind['procedure_sha256']==procedure
                assert bind['root']==ri and bind['root_record_sha256']==jd(root)
                assert bind['block']['dimension']==n and bind['block']['block']==label and bind['block']['B_sector']==sector
                assert bind['block']['basis_sha256']==record_hashes[prefix+'-basis.json']
                assert bind['matrix_sha256']==record_hashes[stem+'-matrix.json']
                assert cert['preconditioner_sha256']==record_hashes[stem+'-inverse-candidates.json']
                eta0,delta,eta=map(Q,(cert['balanced_center_defect_column1'],cert['rootbox_perturbation_column1'],cert['neumann_bound']))
                radius=Q(root['certificate']['radius']);assert Q(cert['radius'])==radius
                assert eta0>=0 and delta==2196*radius*Q(128637452,3)*Q(cert['Ctriangle_upper'])>=0
                assert eta==eta0+delta<1
                sr=status[label,sector,ri];assert sr['dimension']==n and Q(sr['exact_neumann_bound'])==eta
                assert sr['certificate_sha256']==record_hashes[cn]
                bounds.append({'block':label,'B_sector':sector,'root':ri,'dimension':n,'exact_neumann_bound':str(eta),'certificate_sha256':record_hashes[cn]})
    # Execute only the owned self-contained JSON/hash/Fraction helper, not its native module.
    helper=function_sources(source,['inherited_regular_controls'])[0];namespace={}
    exec(compile(helper,str(source),'exec'),namespace)
    inherited=namespace['inherited_regular_controls'](repo)
    assert inherited==m['authenticated_status']['inherited_regular_sectors']
    newdim=sum((2*spin+1)*(plus+minus)for spin,plus,minus in BLOCKS.values())
    assert newdim==m['new_complete_real_coefficient_dimension']==25082
    assert inherited['inherited_regular_real_dimension']==m['inherited_complete_real_coefficient_dimension']==24072
    assert newdim+24072==m['complete_time_kernel_dimension']==49154
    assert result['complete_auxiliary']['total_real_dimensions']==49154
    return {'manifest_sha256':files[name],'producer_sha256':m['final_probe_sha256'],
            'new_28_scalar_bounds_and_bindings':bounds,'full_M_dimension':49154,
            'inherited_helper_source_sha256':sha(helper.encode()),'inherited_certificate_controls':inherited,
            'scope':'Current bundle bytes, root/basis/matrix/candidate/producer bindings and rational scalar Neumann bounds authenticated. Native ranks and dense matrix defects are inherited, not recomputed.'}

def source_inputs(repo,files):
    name='lab/sources/source-claim-register.yaml';raw=path_in(repo,name).read_bytes();files[name]=sha(raw);text=raw.decode();rows=[]
    for claim,polarity in CLAIMS.items():
        match=re.findall(r'^- id: '+re.escape(claim)+r'\n.*?(?=^- id: |\Z)',text,re.M|re.S);assert len(match)==1
        block=match[0];actual=re.findall(r'^  polarity: (\S+)\s*$',block,re.M);assert actual==[polarity]
        rows.append({'id':claim,'polarity':polarity,'source_record_sha256':sha(block.encode())})
    return {'records':rows,'source_necessity':'Not established. ASSERTS action grammar does not identify W2; UNCERTAIN boundary/state claims do not require the tested unrestricted graph core or finite-loss estimate.'}

def loss_arithmetic():
    # Coefficients in (q,ell,constant), followed by ell=q-delta.
    initial=(-Q(1),Q(1),-Q(1));residual=(-Q(1),Q(1),-Q(3,2))
    substitute=lambda p:(p[0]+p[1],-p[1],p[2])
    assert substitute(initial)==(0,-1,-1)and substitute(residual)==(0,-1,-Q(3,2))
    assert Q(1)-Q(1)==0  # physical residual k and dt=d tau/k cancel
    controls=[]
    for ell in map(Q,('0','1/3','1','7/2','1000000/3')):
        q=-(-ell.numerator//ell.denominator);N=2*q+2;crho=q+1;delta=Q(q)-ell
        assert 0<=delta<1 and ell-crho==-delta-1<=-1
        assert ell-Q(N+1,2)==-delta-Q(3,2)<=-Q(3,2)
        controls.append({'loss':str(ell),'ceil_loss':q,'N':N,'c_times_rho':crho,
                         'initial_exponent':str(ell-crho),'residual_exponent':str(ell-Q(N+1,2))})
    return {'quantifier':'For every finite real ell>=0, q=ceil(ell), delta=q-ell>=0.',
            'schedule':{'N':'2q+2','c_times_rho':'q+1'},
            'universal_identities':{'initial':'ell-c*rho=-delta-1<=-1','residual':'ell-(N+1)/2=-delta-3/2<=-3/2'},
            'physical_time_factor_exponent':{'residual_k':1,'integration_dt':-1,'sum':0},
            'exact_polynomial_coefficient_identities_checked':True,'rational_sample_controls':controls,
            'scope':'Universal conclusion uses the stated ceiling inequality delta>=0; finite samples are controls only. No logarithmic-time Taylor remainder or packet estimate is verified here.'}

def build(repo):
    files={};background=load(repo,'lab/process/source-action-deep-coefficients.json',files);roots=background['certified_roots'];assert len(roots)==2
    intrinsic=intrinsic_inputs(repo,files,roots);full=full_M_inputs(repo,files,roots);sources=source_inputs(repo,files)
    return {'schema':'gu-finite-loss-proof-inputs-v1','data_only':True,'final_probe_sha256':file_sha(Path(__file__)),
            'files_sha256':files,'intrinsic_certificate_readback':intrinsic,'full_auxiliary_readback':full,
            'source_polarity':sources,'arbitrary_loss_arithmetic':loss_arithmetic(),'norm_transfer_assumptions':ASSUMPTIONS,
            'not_verified':['Classical-PDO logarithmic-time Taylor remainder','Approximate-packet analytic estimates','Norm-transfer theorem hypotheses on a proposed physical space','Exact exponentially growing solutions','Ward-nontrivial matter coupling or negative-mode forcing','Source-required physical admission or GU falsification'],
            'scope':'Lightweight exact proof-input authentication and loss arithmetic only. Prior accepted analytic/native results remain inherited at their declared scope.'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2])
    group=ap.add_mutually_exclusive_group(required=True);group.add_argument('--write-certificate',action='store_true');group.add_argument('--verify',action='store_true')
    ap.add_argument('--output',type=Path);args=ap.parse_args();repo=args.repo.resolve()
    assert repo==Path(__file__).resolve().parents[2],'Use the installed probe in its own checkout.'
    start=time.monotonic();result=build(repo);path=repo/BUNDLE
    if args.write_certificate:write(path,result)
    else:assert json.loads(path.read_text())==result,'Certificate or authenticated proof input changed.'
    receipt={'passed':True,'mode':'write'if args.write_certificate else'verify','probe_sha256':file_sha(Path(__file__)),
             'certificate_sha256':file_sha(path),'exact_intrinsic_roots_checked':2,'new_M_scalar_bounds_checked':28,
             'full_M_dimension_authenticated':49154,'native_assembly_or_previous_replay_run':False,
             'analytic_packet_remainder_verified':False,'seconds':time.monotonic()-start}
    if args.output:write(args.output,receipt)
    print(json.dumps(receipt),flush=True)
if __name__=='__main__':main()
