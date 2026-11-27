#!/usr/bin/env python3
"""Targeted native M repair of the two actual horizontal consistency sources.

Numerical discovery is never acceptance. Exact receiver closure plus both-root
Neumann certification is required for a preimage claim. No 16-source expansion,
full-R inverse or negative conclusion from old-receiver noncoverage.
"""
from pathlib import Path
from fractions import Fraction as Q
from types import SimpleNamespace
import argparse, hashlib, inspect, json, os, sys, time
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[name]='1'
sys.dont_write_bytecode=True


def write(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_suffix(path.suffix+'.new');tmp.write_text(json.dumps(obj,indent=2)+'\n');tmp.replace(path)


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def load(args):
    global w,p,g,C,I,add,scale,original_context
    sys.path.insert(0,str(args.root/'tests/program-focus'))
    import source_action_weak_response_probe as w
    import source_action_spin4_compatibility_probe as p
    import source_action_deep_geometry as g
    from source_action_paired_response_probe import C,I
    from source_action_deep_algebra import add,scale
    w.configure(args.root);w.Engine=w._fast_exact_class()
    original_context=w.build_seed_context
    # Generic numerical/exact engines receive only this authenticated seed context.
    w.build_seed_context=context
    p.w,p.g,p.C,p.I,p.add,p.scale=w,g,C,I,add,scale
    p.context=context;p.binding=binding


def binding(args):
    names=['tests/program-focus/source_action_weak_response_probe.py',
           'tests/program-focus/source_action_spin4_compatibility_probe.py',
           'tests/program-focus/source_action_paired_response_probe.py',
           'tests/program-focus/source_action_deep_algebra.py',
           'tests/program-focus/source_action_deep_geometry.py',
           'tests/program-focus/source_action_metric_symbol_probe.py',
           'lab/process/source-action-deep-coefficients.json',
           'lab/process/source-action-firstjet-source-census-certificates.json',
           'lab/process/source-action-constraint-consistency-certificates.json']
    return {'target':'minus_census_cases8_17_actual_highest5_consistency',
            'source_context_sha256':hashlib.sha256(inspect.getsource(context).encode()).hexdigest(),
            'native_inputs':{name:digest(args.root/name)for name in names}}


def context(args,numeric=False):
    s=original_context(args,numeric)
    cert=json.loads((args.root/'lab/process/source-action-constraint-consistency-certificates.json').read_text())
    bridge=cert['exact_native_bridge']['bridge']
    censuspath=args.root/'lab/process/source-action-firstjet-source-census-certificates.json'
    assert digest(censuspath)==bridge['published_census_sha256']
    census=json.loads(censuspath.read_text())
    H=g.zero();H[0][3]=H[3][0]=Q(-1)
    act=[g.h_action(H,a)for a in range(14)]
    spin={(1<<a)|(1<<b):act[b].get(a,Q())/(2*g.d[b])for a in range(14)for b in range(a+1,14)if act[b].get(a,Q())}
    def S(v):
        out={}
        for(e,cl),x in v.items():
            a=e.bit_length()-1
            for b in range(14):
                z=-act[b].get(a,Q())
                if z:out[1<<b,cl]=out.get((1<<b,cl),0)+z*x
            for cc,z in s.E.cliff_product(spin,{cl:Q(1)},'comm').items():out[e,cc]=out.get((e,cc),0)+z*x
        return {k:z for k,z in out.items()if z}
    seeds=[]
    for index,case,owned in zip((5,12),(8,17),bridge['sources']):
        V=s.q['K'](3,s.bs[index]);sv=S(V);sv=add(sv,scale(-1,s.q['P'](sv)))
        v=s.q['spin5'](s.q['P'](s.q['K'](0,sv)))
        old={(e,cl):C(*z)for e,cl,z in census['sources'][case]['source']}
        bound={(e,cl):C(*z)for e,cl,z in owned['source']}
        assert v==scale(-1,old)==bound
        assert s.q['P'](v)==v and not s.q['K'](3,v)
        assert s.q['cas'](v)==scale(30,v)
        assert s.rot(0,1,v)==scale(5*I,v)
        assert not add(s.rot(0,2,v),scale(I,s.rot(1,2,v)))
        seeds.append(v)
    assert list(map(len,seeds))==[56,80]
    s.seeds=seeds
    print('TARGET native source cases8/17',[len(v)for v in seeds],flush=True)
    return s


def stage_seeds(args):
    s=context(args)
    out={'scope':'Exact native minus cases8/17, not a new solvability claim.',
         'bindings':binding(args),'exact_seeds':[s.q['ser'](v)for v in s.seeds]}
    write(args.output,out)


def stage_numeric(args):
    p.stage_numeric(args,scout=args.mode=='scout')
    out=json.loads(args.output.read_text())
    out['scope']='NUMERICAL_DISCOVERY_ONLY full ambient M action on actual minus cases8/17; no exact-root or multiplier obstruction claim.'
    write(args.output,out)


def stage_basis(args):
    inputs=args.input or [args.cache/'inverse-stage2.json'];roots=[]
    for path in inputs:
        data=json.loads(path.read_text());assert data['bindings']==binding(args)
        roots.extend(data['roots'])
    support={(e,cl)for r in roots for e,cl,*_ in r['solution']}
    assert len(support)<=args.max_support,('resource_cap',len(support),args.max_support)
    write(args.cache/'inverse-stage2.json',{'roots':roots,'input_hashes':{str(p):digest(p)for p in inputs}})
    w.mode_basis(args)
    out=json.loads(args.output.read_text());out['bindings']=binding(args)
    out['scope']='Exact complete highest5/time-kernel space inside discovered support; M invariance not yet certified.'
    write(args.output,out)


def integer_binding(args):
    return {'format':'targeted-spin5-sparse-integer-v1',
            'engine_sha256':p.integer_engine_digest(),
            'projection_sha256':hashlib.sha256('\n'.join(inspect.getsource(f)for f in (p.clear_matrix,p.integer_matvec,p.IntegerKernelProjection)).encode()).hexdigest(),
            'closure_procedure_sha256':hashlib.sha256(inspect.getsource(stage_closure).encode()).hexdigest(),
            'basis_sha256':digest(args.cache/'inverse-stage3-basis.json'),
            'background_sha256':digest(args.root/'lab/process/source-action-deep-coefficients.json'),
            'native_inputs':w.native_bindings(args.root),'target':binding(args)}


def stage_closure(args):
    s=context(args);controls=p.integer_controls(args.root)
    seedpath=args.cache/'inverse-stage1.json'
    seeddata={'scope':'Exact native minus cases8/17, not a new solvability claim.',
              'bindings':binding(args),'exact_seeds':[s.q['ser'](v)for v in s.seeds]}
    if seedpath.exists():assert json.loads(seedpath.read_text())==seeddata
    else:write(seedpath,seeddata)
    E=p.IntegerScaledN(g);P=p.IntegerKernelProjection(s.q,E)
    bd=json.loads((args.cache/'inverse-stage3-basis.json').read_text())
    basis=[{(e,cl):C(*z)for e,cl,z in row}for row in bd['basis']]
    pivots=[tuple(x)for x in bd['basis_pivots']];n=len(basis)
    assert n<=args.max_dimension,('resource_cap',n,args.max_dimension)
    data=json.loads((args.root/'lab/process/source-action-deep-coefficients.json').read_text())
    backgrounds=[{(e,cl):Q(z)for e,cl,z in row}for row in data['basis']]
    for T in backgrounds:E.prepare(T)
    def reduce(v):
        cs=[]
        for pivot,b in zip(pivots,basis):
            z=C(v.get(pivot,0));cs.append(z)
            if z:v=add(v,scale(-z,b))
        return v,cs
    out={'scope':'Exact all59 native family closure of the two-source highest5 receiver; valid only when completed equals dimension.',
         'bindings':integer_binding(args),'engine_controls':controls,
         'dimension':n,'maps':59,'completed':0,'columns':[]}
    if args.output.exists():
        prior=json.loads(args.output.read_text());assert prior['bindings']==out['bindings']
        assert prior['completed']==len(prior['columns']) and not prior.get('failure')
        out=prior
    start=time.monotonic();begin=out['completed'];end=n if args.steps==0 else min(n,begin+args.steps)
    for bi in range(begin,end):
        columns=[]
        for ti,T in enumerate(backgrounds):
            du,ui,au=E.prepare(T);dv,vi,av=E.prepare(basis[bi])
            numerator=E.Phi_scaled(E.wedge_comm_int(ui,vi))
            p.add_into(numerator,E.wadj_scaled(ui,av));p.add_into(numerator,E.wadj_scaled(vi,au))
            image=P.apply_integer(numerator,3*E.Dphi*du*dv)
            rem,cs=reduce(image)
            if rem:
                out['failure']={'basis':bi,'background':ti,'outside_terms':len(rem),'witness':s.q['ser'](rem)[:5]}
                write(args.output,out);raise AssertionError(out['failure'])
            columns.append([[i,*z.ser()]for i,z in enumerate(cs)if z])
        out['columns'].append(columns);out['completed']=bi+1
        out['last_batch_seconds']=time.monotonic()-start;write(args.output,out)
        print('TARGET exact59 closure',bi+1,'/',n,'seconds',out['last_batch_seconds'],flush=True)


def validate_basis(module,args,bd,ctx=None):
    ctx=ctx or context(args);tick=time.monotonic()
    basis=[{(e,cl):C(*z)for e,cl,z in row}for row in bd['basis']]
    pivots=[tuple(x)for x in bd['basis_pivots']]
    assert len(pivots)==len(basis)==len(set(pivots))
    for i,(pivot,v)in enumerate(zip(pivots,basis)):
        assert v.get(pivot)==C(1) and all(not v.get(k,C())for k in pivots[:i])
        assert not ctx.q['K'](3,v)
        assert ctx.rot(0,1,v)==scale(5*I,v)
        assert not add(ctx.rot(0,2,v),scale(I,ctx.rot(1,2,v)))
        assert ctx.q['cas'](v)==scale(30,v)
    # Native spatial halfturn diag(1,-1,-1,1), then coefficient conjugation.
    # This maps highest5 back to highest5 and authenticates real orbit closure.
    signs=[1,-1,-1,1,1,1,1,1,-1,-1,1,1,-1,-1]
    for v in basis:
        rem={(e,cl):z.conj()*((-1)**sum(1 for a,sgn in enumerate(signs)if sgn<0 and (((e>>a)&1)^((cl>>a)&1))))for(e,cl),z in v.items()}
        for pivot,b in zip(pivots,basis):
            z=rem.get(pivot,0)
            if z:rem=add(rem,scale(-z,b))
        assert not rem,'Highest reality closure failed'
    out={'scope':'Every native receiver vector: exact time-kernel, weight5, raising, Casimir30 and echelon independence.',
         'dimension':len(basis),'native_equation_checks':4*len(basis),'highest_reality_closure':True,'complete':True,
         'seconds':time.monotonic()-tick,
         'bindings':{'basis_sha256':digest(args.cache/'inverse-stage3-basis.json'),
                     'native_seed_context_sha256':hashlib.sha256(inspect.getsource(context).encode()).hexdigest(),
                     'validator_sha256':hashlib.sha256(inspect.getsource(validate_basis).encode()).hexdigest()}}
    write(args.cache/'repair-basis-validation.json',out);return out


def stage_reference(args):
    """Original Hodge-star Euler engine and Fraction P on the first59-map column."""
    from source_action_deep_algebra import Engine
    s=context(args);E=Engine(g)
    bd=json.loads((args.cache/'inverse-stage3-basis.json').read_text())
    cl=json.loads((args.cache/'repair-closure-integer.json').read_text())
    assert cl['bindings']==integer_binding(args) and cl['completed']>=1
    basis=[{(e,cc):C(*z)for e,cc,z in row}for row in bd['basis']]
    data=json.loads((args.root/'lab/process/source-action-deep-coefficients.json').read_text())
    out={'scope':'Independent original star-based Engine.N and native Fraction P match the first all59 integer closure column.',
         'bindings':{'basis_sha256':digest(args.cache/'inverse-stage3-basis.json'),
          'first_column_sha256':p.sn_jd(cl['columns'][0]),'native_inputs':binding(args),
          'reference_procedure_sha256':hashlib.sha256(inspect.getsource(stage_reference).encode()).hexdigest()},
         'completed':0,'maps':59,'all_passed':False}
    tick=time.monotonic()
    for j,row in enumerate(data['basis']):
        T={(e,cc):Q(z)for e,cc,z in row}
        got=s.q['P'](scale(2,E.N(T,basis[0])))
        expected=add(*(scale(C(a,b),basis[i])for i,a,b in cl['columns'][0][j]))
        assert got==expected,('Original native seam mismatch',j)
        out['completed']=j+1;out['seconds']=time.monotonic()-tick
        if j%10==0:print('TARGET original-engine comparison',j+1,'/59','seconds',out['seconds'],flush=True)
        write(args.output,out)
    out['all_passed']=True;write(args.output,out)


def stage_certificate(args):
    import numpy as np
    assert 12<=args.precision<=80
    p.sn_validate_basis=validate_basis
    args.closure=args.cache/'repair-closure-integer.json'
    module=sys.modules[__name__]
    cl,bd,sd,data,module=p.sn_validate_inputs(args,module)
    refpath=args.cache/'repair-reference-controls.json'
    reference=json.loads(refpath.read_text())
    assert reference['all_passed'] and reference['completed']==reference['maps']==59
    assert reference['bindings']['basis_sha256']==digest(args.cache/'inverse-stage3-basis.json')
    assert reference['bindings']['first_column_sha256']==p.sn_jd(cl['columns'][0])
    assert reference['bindings']['native_inputs']==binding(args)
    assert reference['bindings']['reference_procedure_sha256']==hashlib.sha256(inspect.getsource(stage_reference).encode()).hexdigest()
    sources,validation=p.sn_source_coordinates(module,args,bd,sd)
    da,S,roots=p.sn_assemble(cl,data['certified_roots'])
    base={'closure_sha256':digest(args.closure),'basis_sha256':digest(args.cache/'inverse-stage3-basis.json'),
          'seeds_sha256':digest(args.cache/'inverse-stage1.json'),
          'background_sha256':digest(args.root/'lab/process/source-action-deep-coefficients.json'),
          'native_seed_context_sha256':hashlib.sha256(inspect.getsource(context).encode()).hexdigest(),
          'reference_controls_sha256':digest(refpath)}
    out={'scope':'Exact root-box M preimages for minus cases8/17 in a native invariant highest5 receiver; therefore explicit repair of these tested augmented first-consistency classes. Not full propagation or a physical/GU verdict.',
         'dimension':cl['dimension'],'family_maps':59,'bindings':base|{'closure_bindings':cl['bindings'],
          'verifier_sha256':digest(Path(__file__)),'integer_neumann_engine_sha256':digest(args.root/'tests/program-focus/source_action_spin4_compatibility_probe.py')},
         'controls':p.sn_controls(),'basis_validation':validation,'roots':[]}
    cp=args.cache/'repair-inverse-candidates.json';tick=time.monotonic()
    for ri,(root,owned)in enumerate(zip(roots,data['certified_roots'])):
        cb=base|{'root':ri,'root_record_sha256':p.sn_jd(owned)}
        Rr,Ri,Dr=p.sn_rational_preconditioner(root,cl['dimension'],cb,cp,args.generate_candidates,args.precision)
        result=p.sn_certificate_numbers(root['Mr'],root['Mi'],root['Dm'],Rr,Ri,Dr,S,da,Q(owned['certificate']['radius']),sources)
        result.update({'root':ri,'radius':owned['certificate']['radius'],'owned_root_record_sha256':p.sn_jd(owned)})
        out['roots'].append(result);out['preconditioner_sha256']=digest(cp)
        out['both_roots_solved']=len(out['roots'])==2 and all(r['invertible_on_block_over_rootball']and len(r['sources'])==2 for r in out['roots'])
        out['seconds']=time.monotonic()-tick;write(args.output,out)
        print('TARGET ROOT',ri,'eta',float(Q(result['neumann_bound'])),'PASS',result['invertible_on_block_over_rootball'],flush=True)


def stage_unpack(args):
    import base64,zlib
    data=json.loads(args.bundle.read_text());restored=[]
    allowed={'inverse-stage1.json','inverse-stage3-basis.json','repair-closure-integer.json',
             'repair-basis-validation.json','repair-inverse-candidates.json','repair-fast-certificate.json',
             'repair-reference-controls.json'}
    for name,record in data['records'].items():
        assert name in allowed and record['encoding']=='zlib-base64-json'
        count=record['uncompressed_bytes'];assert type(count)is int and 0<count<100_000_000
        dec=zlib.decompressobj();raw=dec.decompress(base64.b64decode(record['data'],validate=True),count+1)
        assert dec.eof and not dec.unconsumed_tail and not dec.unused_data
        assert len(raw)==count and hashlib.sha256(raw).hexdigest()==record['sha256'];json.loads(raw)
        dest=args.cache/name
        if dest.exists():assert dest.read_bytes()==raw,('Different cache bytes',name)
        else:dest.write_bytes(raw)
        restored.append(name)
    write(args.output,{'restored':restored,'all_exact_bytes_verified':True})


def stage_status(args):
    out={}
    for name in ('inverse-stage3-basis.json','repair-closure-integer.json','repair-fast-certificate.json'):
        path=args.cache/name
        if not path.exists():out[name]={'present':False};continue
        data=json.loads(path.read_text());row={'present':True,'bytes':path.stat().st_size}
        for k in ('dimension','highest5_timekernel_dimension','completed','failure','both_roots_solved'):
            if k in data:row[k]=data[k]
        if 'roots'in data:row['roots']=[{k:r[k]for k in ('root','neumann_bound','invertible_on_block_over_rootball')}for r in data['roots']]
        out[name]=row
    write(args.output,out);print(json.dumps(out,indent=2),flush=True)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2])
    ap.add_argument('--cache',type=Path,required=True)
    ap.add_argument('--mode',choices=('seeds','scout','numeric','basis','closure','reference','certify','replay','unpack','status'),required=True)
    ap.add_argument('--steps',type=int,default=30)
    ap.add_argument('--root-index',type=int,choices=(0,1))
    ap.add_argument('--source-index',type=int,choices=(0,1))
    ap.add_argument('--prune',type=float,default=1e-13)
    ap.add_argument('--input',type=Path,nargs='*')
    ap.add_argument('--max-support',type=int,default=5000)
    ap.add_argument('--max-dimension',type=int,default=300)
    ap.add_argument('--generate-candidates',action='store_true')
    ap.add_argument('--precision',type=int,default=24)
    ap.add_argument('--bundle',type=Path)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args();args.root=args.repo.resolve();args.cache.mkdir(parents=True,exist_ok=True)
    names={'seeds':'inverse-stage1.json','scout':'repair-scout.json','numeric':'inverse-stage2.json','basis':'inverse-stage3-basis.json',
           'closure':'repair-closure-integer.json','reference':'repair-reference-controls.json','certify':'repair-fast-certificate.json','replay':'repair-replay.json',
           'unpack':'repair-unpack.json','status':'repair-status.json'}
    args.output=args.output or args.cache/names[args.mode]
    args.bundle=args.bundle or args.root/'lab/process/source-action-constraint-source-repair-certificates.json'
    if args.mode=='unpack':stage_unpack(args);return
    if args.mode=='status':stage_status(args);return
    load(args)
    if args.mode=='seeds':stage_seeds(args)
    elif args.mode=='basis':stage_basis(args)
    elif args.mode=='closure':stage_closure(args)
    elif args.mode=='reference':stage_reference(args)
    elif args.mode in ('certify','replay'):
        if args.mode=='replay':assert not args.generate_candidates,'Replay must use frozen rational preconditioners.'
        stage_certificate(args)
    else:stage_numeric(args)


if __name__=='__main__':main()
