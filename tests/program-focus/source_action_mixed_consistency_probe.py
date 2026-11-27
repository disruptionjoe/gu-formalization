#!/usr/bin/env python3
"""Exact mixed consistency receiver tests using the ambient-generator quotient.

No numerical horizontal response is an acceptance input. Failure of a strong
coefficientwise receiver test is only noncoverage, not a native obstruction.
"""
from pathlib import Path
from fractions import Fraction as Q
from types import SimpleNamespace
import argparse,hashlib,inspect,json,sys,time
sys.dont_write_bytecode=True


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def write(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_suffix(path.suffix+'.new');tmp.write_text(json.dumps(obj,indent=2)+'\n');tmp.replace(path)


def setup(args):
    sys.path.insert(0,str(args.repo/'tests/program-focus'))
    import source_action_constraint_consistency_probe as native
    c=native.setup(args.repo);c.native=native;c.geometry=native.geometry(c)
    c.Vs=[c.K(3,c.s.bs[j])for j in(5,12)]
    c.background=json.loads((args.repo/'lab/process/source-action-deep-coefficients.json').read_text())
    c.Ts=[{(e,cl):Q(z)for e,cl,z in row}for row in c.background['basis']]
    c.ser=lambda v:[[e,cl,c.C(z).ser()]for(e,cl),z in sorted(v.items())]
    def operator(axis):
        U=[[Q(0)]*14 for _ in range(14)]
        U[3][axis]=Q(-1);U[axis][3]=-Q(1)/c.g.d[axis]
        assert all(c.g.d[i]*U[i][j]+c.g.d[j]*U[j][i]==0 for i in range(14)for j in range(14))
        return lambda v:c.geometry.rho(U,v)
    c.U={a:operator(a)for a in(0,1,2,5,8,9,10,11,12,13)}
    # Horizontal S is the BASE Lorentz embedding, including its Sym2H action
    # on normal tangent indices. Ambient U_xi alone would not fix the59 T's.
    c.S={}
    for xi in(0,2):
        H=c.g.zero();H[xi][3]=H[3][xi]=Q(-1)
        A=[[c.g.h_action(H,a).get(b,Q())for a in range(14)]for b in range(14)]
        c.S[xi]=lambda v,A=A:c.geometry.rho(A,v)
    def part(v,j,lo):
        for k in range(lo,8):
            if k!=j:v=c.scale(Q(1,j*(j+1)-k*(k+1)),c.add(c.s.q['cas'](v),c.scale(-k*(k+1),v)))
        return v
    c.part=part
    return c


def bindings(args):
    names=['tests/program-focus/source_action_constraint_consistency_probe.py',
           'tests/program-focus/source_action_spin4_compatibility_probe.py',
           'tests/program-focus/source_action_weak_response_probe.py',
           'tests/program-focus/source_action_deep_algebra.py',
           'tests/program-focus/source_action_deep_geometry.py',
           'tests/program-focus/source_action_metric_symbol_probe.py',
           'tests/program-focus/source_action_paired_response_probe.py',
           'lab/process/source-action-deep-coefficients.json',
           'lab/process/source-action-kappa1-constraints.json',
           'lab/process/source-action-reduced-evolution.json']
    return {'native_inputs':{name:digest(args.repo/name)for name in names},'probe_sha256':digest(Path(__file__))}


def receiver(c,args):
    specs=[('E4',args.e4,'spin4-fast-certificate.json','source-action-spin4-certificates.json',4),
           ('E5_old',args.e5_old,'inverse-stage5-certificate.json','source-action-weak-response.json',5),
           ('E5_new',args.e5_new,'repair-fast-certificate.json','source-action-constraint-source-repair-certificates.json',5)]
    spaces={4:[],5:[]};meta={}
    for name,cache,certname,bundlename,j in specs:
        bundle=json.loads((args.repo/'lab/process'/bundlename).read_text())
        records=bundle['reproduction']['records']if name=='E5_old'else bundle['records']
        bp=cache/'inverse-stage3-basis.json';cp=cache/certname
        assert digest(bp)==records[bp.name]['sha256']
        assert digest(cp)==records[cp.name]['sha256']
        bd=json.loads(bp.read_text());cert=json.loads(cp.read_text())
        assert len(cert['roots'])==2 and all(r['invertible_on_block_over_rootball']and Q(r['neumann_bound'])<1 for r in cert['roots'])
        basis=[{(e,cl):c.C(*z)for e,cl,z in row}for row in bd['basis']]
        pivots=[tuple(k)for k in bd['basis_pivots']]
        assert len(basis)==len(pivots)
        for pivot,v in zip(pivots,basis):
            assert v.get(pivot)==c.C(1)
            spaces[j].append((pivot,v))
        meta[name]={'dimension':len(basis),'basis_sha256':digest(bp),'certificate_sha256':digest(cp)}
    # The two E5 supports are disjoint; concatenation is an exact echelon basis.
    for j,bs in spaces.items():
        for i,(pivot,v)in enumerate(bs):assert all(not v.get(p,c.C())for p,b in bs[:i])
    def reduce(j,v):
        for pivot,b in spaces[j]:
            z=v.get(pivot,0)
            if z:v=c.add(v,c.scale(-z,b))
        return v
    return reduce,meta


def input_channel_controls(c):
    """Native contragredient covector tensor Casimir, with exact normalization."""
    rotations=[]
    for i,j in((0,1),(0,2),(1,2)):
        H=c.g.zero();H[i][j]=Q(1);H[j][i]=Q(-1)
        tangent=[c.g.h_action(H,a)for a in range(14)]
        rotations.append([[(b,-tangent[b].get(a,Q()))for b in range(14)if tangent[b].get(a,Q())]for a in range(14)])
    def rot(R,v):
        out={}
        for(a,b),z in v.items():
            for aa,t in R[a]:out[aa,b]=out.get((aa,b),0)+z*t
            for bb,t in R[b]:out[a,bb]=out.get((a,bb),0)+z*t
        return {k:z for k,z in out.items()if z}
    def cas(v):return c.scale(-1,c.add(*(rot(R,rot(R,v))for R in rotations)))
    a={(0,9):c.C(1),(0,11):-c.I,(1,9):-c.I,(1,11):c.C(-1)}
    b={(2,5):c.C(1),(2,8):-c.I}
    assert cas(a)==c.add(c.scale(10,a),c.scale(4,b))
    assert cas(b)==c.add(c.scale(2,a),c.scale(8,b))
    v2=c.add(a,c.scale(-2,b));v3=c.add(a,b)
    assert cas(v2)==c.scale(6,v2)and cas(v3)==c.scale(12,v3)
    return {'weight_minus2_Casimir_columns':[[10,4],[2,8]],
            'spin2_eigenvector':'a-2b','spin3_eigenvector':'a+b',
            'raw_A':'q(theta0,theta9)','raw_B':'q(theta2,theta5)',
            'reduced_spin2_map':'4*(A-B)','reduced_spin3_map':'2*(2*A+B)',
            'normalization':'Exact unnormalized native covector/ladder convention.'}


def stage_controls(args):
    tick=time.monotonic();c=setup(args);out={'scope':'Exact ambient-generator covariance and zero horizontal-axis2 primary source; no mixed membership verdict.',
        'bindings':bindings(args),'input_channels':input_channel_controls(c),'sources':[],'covariance_checks':0,'parity_controls':parity_controls(c,args)}
    for index,V in zip((5,12),c.Vs):
        assert not c.P(c.K(2,V)), 'Expected highest7 axis2 primary zero failed'
        for a in(5,9,10):
            assert c.add(c.U[a](c.K(3,V)),c.scale(-1,c.K(3,c.U[a](V))))==c.K(a,V)
        for xi in(0,2):
            assert c.add(c.S[xi](c.K(3,V)),c.scale(-1,c.K(3,c.S[xi](V))))==c.K(xi,V)
            assert c.add(c.S[xi](c.K(xi,V)),c.scale(-1,c.K(xi,c.S[xi](V))))==c.K(3,V)
        out['sources'].append({'basis_index':index,'P_K2_V_zero':True,'ambient_K_commutators':3,'base_Lorentz_commutators':4})
    for xi in(0,2):
        assert all(not c.S[xi](T)for T in c.Ts)
    out['base_Lorentz_background_invariance_checks']=118
    fixture=c.P(c.K(0,c.Vs[0]));assert fixture
    for a in(5,9,10):
        U=c.U[a];un=U(fixture)
        for j,T in enumerate(c.Ts):
            lhs=U(c.integer.N(T,fixture))
            rhs=c.add(c.integer.N(T,un),c.integer.N(U(T),fixture))
            assert lhs==rhs,('Native cubic covariance failure',a,j)
            out['covariance_checks']+=1
        out['seconds']=time.monotonic()-tick;write(args.output,out)
        print('MIXED all59 cubic covariance axis',a,'PASS','seconds',out['seconds'],flush=True)
    out['all_passed']=True;out['seconds']=time.monotonic()-tick;write(args.output,out)


def stage_constants(args):
    tick=time.monotonic();c=setup(args);reduce,metadata=receiver(c,args)
    out={'scope':'Root-independent constant columns of the no-G mixed representative; strong sufficient test only.',
         'bindings':bindings(args),'receivers':metadata,'input_channels':input_channel_controls(c),'columns':[]}
    for index,V in zip((5,12),c.Vs):
        assert not c.P(c.K(2,V))
        for xi,eta,j in((0,5,4),(0,10,5),(0,9,5),(2,5,5)):
            d=c.part(c.P(c.U[eta](c.S[xi](c.K(3,V)))),j,4 if eta==5 and xi==0 else 5)
            assert c.s.rot(0,1,d)==c.scale(j*c.I,d)
            assert not c.add(c.s.rot(0,2,d),c.scale(c.I,c.s.rot(1,2,d)))
            rem=reduce(j,d)
            parity=1 if eta==10 else 0
            assert all(((e^cl)&13319).bit_count()%2==parity for e,cl in d)
            out['columns'].append({'basis_index':index,'horizontal_axis':xi,'normal_axis':eta,'spin':j,
                                   'terms':len(d),'remainder_terms':len(rem),'inside_receiver':not rem,'parity':parity,
                                   'source':c.ser(d),'remainder':c.ser(rem)})
            out['seconds']=time.monotonic()-tick;write(args.output,out)
            print('MIXED constant',index,xi,eta,j,'terms',len(d),'remainder',len(rem),flush=True)
    out['all_constants_covered']=all(row['inside_receiver']for row in out['columns']);write(args.output,out)


def stage_affine(args):
    """Exact coefficientwise sufficient test on the owned32-coordinate Y block."""
    tick=time.monotonic();c=setup(args);reduce,metadata=receiver(c,args)
    basis,old=c.native.n6_basis(c,args.cache/'native-n6.json')
    ids=old['exact_probe']['spin6']['constraint_inverse']['constraint_components'][3]
    assert len(ids)==32 and 37 in ids and 40 in ids
    # The two old paired source rows live in this same certified diagonal block.
    evo=json.loads((args.repo/'lab/process/source-action-reduced-evolution.json').read_text())
    source_rows={r['basis_index']:r for r in evo['exact_probe']['source_receivers']}
    for index,V in zip((5,12),c.Vs):
        row=source_rows[index];assert not row['b7_lowered']
        force=c.K(0,V)
        paired=[[i,c.C(c.E.pair({k:z.conj()for k,z in n.items()},force)).ser()]
                for i,n in enumerate(basis)if c.E.pair({k:z.conj()for k,z in n.items()},force)]
        assert paired==row['b6'] and all(i in ids for i,z in paired)
    for i in ids:
        n=basis[i]
        assert not c.K(3,n)
        assert c.s.rot(0,1,n)==c.scale(6*c.I,n)
        assert not c.add(c.s.rot(0,2,n),c.scale(c.I,c.s.rot(1,2,n)))
        assert c.s.q['cas'](n)==c.scale(42,n)
    live={'native_inputs':bindings(args)['native_inputs'],'receivers':metadata,
          'native_n6_sha256':digest(args.cache/'native-n6.json'),
          'implementation_sha256':hashlib.sha256('\n'.join(inspect.getsource(f)for f in (setup,receiver,stage_affine)).encode()).hexdigest()}
    out={'scope':'Strong exact all59 coefficientwise membership for arbitrary y in the owned32-coordinate horizontal response block; no actual-root conclusion from a failed column.',
         'bindings':live,'domain_indices':ids,'domain_dimension':32,'backgrounds':59,
         'target_channels':[{'normal_axis':5,'spin':4},{'normal_axis':10,'spin':5},{'normal_axis':9,'spin':5}],
         'completed':0,'columns':[]}
    if args.output.exists():
        prior=json.loads(args.output.read_text());assert prior['bindings']==live
        assert prior['completed']==len(prior['columns']);out=prior
    print('MIXED exact N6 domain authenticated','seconds',time.monotonic()-tick,flush=True)
    transformed={(a,j):c.U[a](T)for a in(5,10,9)for j,T in enumerate(c.Ts)}
    for T in transformed.values():c.integer.prepare(T)
    start=time.monotonic();begin=out['completed'];end=32 if args.steps==0 else min(32,begin+args.steps)
    for position in range(begin,end):
        bi=ids[position];n=basis[bi];rows=[]
        for j in range(59):
            for eta,spin in((5,4),(10,5),(9,5)):
                raw=c.scale(-2,c.integer.N(transformed[eta,j],n))
                image=c.part(c.P(raw),spin,4 if eta==5 else 5)
                assert not c.K(3,image)
                assert c.s.rot(0,1,image)==c.scale(spin*c.I,image)
                assert not c.add(c.s.rot(0,2,image),c.scale(c.I,c.s.rot(1,2,image)))
                rem=reduce(spin,image)
                rows.append({'background':j,'normal_axis':eta,'spin':spin,'image_terms':len(image),
                             'inside_receiver':not rem,'remainder_terms':len(rem),
                             'image_sha256':c.native.digest(c.ser(image)),
                             'remainder':c.ser(rem)})
        out['columns'].append({'n6_index':bi,'maps':rows});out['completed']=position+1
        out['tested_maps']=out['completed']*59*3
        out['all_tested_columns_covered']=all(r['inside_receiver']for col in out['columns']for r in col['maps'])
        out['complete']=out['completed']==32;out['seconds']=time.monotonic()-start
        write(args.output,out)
        print('MIXED affine',position+1,'/32','all covered',out['all_tested_columns_covered'],'seconds',out['seconds'],flush=True)



def input_patterns(c,eta,j):
 rotations=[]
 for i,k in ((0,1),(0,2),(1,2)):
  H=c.g.zero();H[i][k]=Q(1);H[k][i]=Q(-1)
  tangent=[c.g.h_action(H,a)for a in range(14)]
  rotations.append([[(b,-tangent[b].get(a,Q()))for b in range(14)if tangent[b].get(a,Q())]for a in range(14)])
 def rot(r,v):
  out={}
  def put(a,k,z):
   if z:out[a,k]=out.get((a,k),c.C())+z
  for (a,k),z in v.items():
   for b,t in rotations[r][a]:put(b,k,z*t)
   if r==0:put(a,k,z*c.I*(6-k))
   if r==1:
    put(a,k-1,z*Q(-k*(13-k),2));put(a,k+1,z*Q(1,2))
   if r==2:
    put(a,k-1,z*c.I*Q(k*(13-k),2));put(a,k+1,z*c.I*Q(1,2))
  return {k:z for k,z in out.items()if z}
 def cas(v):return c.scale(-1,c.add(*(rot(r,rot(r,v))for r in range(3))))
 v={(eta,0):c.C(1)}
 for k in range(4,9):
  if k!=j:v=c.scale(Q(1,j*(j+1)-k*(k+1)),c.add(cas(v),c.scale(-k*(k+1),v)))
 assert cas(v)==c.scale(j*(j+1),v)
 return v

def prepare_input(c,n,pat):
 ns=[n]
 for k in range(max(k for a,k in pat)):
  ns.append(c.add(c.s.rot(0,2,ns[-1]),c.scale(-c.I,c.s.rot(1,2,ns[-1]))))
 return {a:c.add(*(c.scale(z,ns[k])for (aa,k),z in pat.items()if aa==a)) for a in set(a for a,k in pat)}

def projected_image(c,Ts,prepared):
    # Sum all Gaussian-integer cubic numerators before the single native P.
    # Each numerator is Dphi times the three unscaled Euler terms;
    # -2N therefore has denominator 3*Dphi*du*dv and negative numerator.
    from math import lcm
    E=c.integer;terms=[];denominator=1
    for a,n in prepared.items():
        du,ui,au=E.prepare(Ts[a]);dv,vi,av=E.prepare(n)
        numerator=E.Phi_scaled(E.wedge_comm_int(ui,vi))
        c.fast.add_into(numerator,E.wadj_scaled(ui,av))
        c.fast.add_into(numerator,E.wadj_scaled(vi,au))
        d=3*E.Dphi*du*dv;denominator=lcm(denominator,d)
        terms.append((numerator,d))
    numerator={}
    for v,d in terms:c.fast.add_into(numerator,v,-denominator//d)
    return c.P.apply_integer(numerator,denominator)


def ambient_operator(c,axis):
    U=[[Q(0)]*14 for _ in range(14)]
    U[3][axis]=Q(-1);U[axis][3]=-Q(1)/c.g.d[axis]
    assert all(c.g.d[i]*U[i][j]+c.g.d[j]*U[j][i]==0 for i in range(14)for j in range(14))
    return lambda v:c.geometry.rho(U,v)


def active_domain(c,args):
    basis,old=c.native.n6_basis(c,args.cache/'native-n6.json')
    ids=old['exact_probe']['spin6']['constraint_inverse']['constraint_components'][3]
    assert len(ids)==32 and 37 in ids and 40 in ids
    evo=json.loads((args.repo/'lab/process/source-action-reduced-evolution.json').read_text())
    for index,V in zip((5,12),c.Vs):
        row=next(r for r in evo['exact_probe']['source_receivers']if r['basis_index']==index)
        assert not row['b7_lowered'];force=c.K(0,V)
        paired=[]
        for i,n in enumerate(basis):
            z=c.C(c.E.pair({k:z.conj()for k,z in n.items()},force))
            if z:paired.append([i,z.ser()])
        assert paired==row['b6']and all(i in ids for i,z in paired)
    for i in ids:
        n=basis[i]
        assert not c.K(3,n)
        assert c.s.rot(0,1,n)==c.scale(6*c.I,n)
        assert not c.add(c.s.rot(0,2,n),c.scale(c.I,c.s.rot(1,2,n)))
        assert c.s.q['cas'](n)==c.scale(42,n)
    return basis,old,ids


def stage_family(args):
    """Full exact family test with the input-Casimir projection optimization."""
    c=setup(args);reduce,metadata=receiver(c,args);basis,old,ids=active_domain(c,args)
    patterns={(a,j):input_patterns(c,a,j)for a,j in ((5,4),(10,5),(9,5))}
    funcs=(setup,receiver,active_domain,ambient_operator,input_patterns,prepare_input,projected_image,stage_family)
    live={'native_inputs':bindings(args)['native_inputs'],'receivers':metadata,
          'native_n6_sha256':digest(args.cache/'native-n6.json'),
          'implementation_sha256':hashlib.sha256('\n'.join(inspect.getsource(f)for f in funcs).encode()).hexdigest()}
    witnesses=[(2048,6415),(256,10511)]
    out={'scope':'Exact coefficientwise membership and scalar witness rows on the entire owned32 horizontal-response block. Failed coverage is not a range obstruction.',
         'bindings':live,'domain_indices':ids,'witness_coordinates':[list(k)for k in witnesses],
         'patterns':{str(a):[[aa,k,z.ser()]for(aa,k),z in sorted(p.items())]for(a,j),p in patterns.items()},
         'completed':0,'columns':[]}
    if args.output.exists():
        prior=json.loads(args.output.read_text());assert prior['bindings']==live
        assert prior['completed']==len(prior['columns']);out=prior
    # Authenticate the optimized projection against the already-recorded direct
    # output-Casimir implementation for every background/target of column zero.
    direct=json.loads((args.cache/'mixed-affine.json').read_text())
    assert direct['bindings']['native_inputs']==live['native_inputs']
    assert direct['bindings']['receivers']==metadata and direct['columns'][0]['n6_index']==ids[0]
    reference={(r['background'],r['normal_axis']):r['image_sha256']for r in direct['columns'][0]['maps']}
    axes=set(a for p in patterns.values()for a,k in p)
    ops={a:ambient_operator(c,a)for a in axes}
    transformed={j:{a:ops[a](T)for a in axes}for j,T in enumerate(c.Ts)}
    for ts in transformed.values():
        for T in ts.values():c.integer.prepare(T)
    start=time.monotonic();begin=out['completed'];end=32 if args.steps==0 else min(32,begin+args.steps)
    for position in range(begin,end):
        tick=time.monotonic();bi=ids[position];n=basis[bi]
        prepared={key:prepare_input(c,n,p)for key,p in patterns.items()};rows=[]
        for j in range(59):
            for eta,spin in patterns:
                image=projected_image(c,transformed[j],prepared[eta,spin])
                # Exact complete ambient equations, not only compressed rows.
                assert not c.K(3,image)
                assert c.s.rot(0,1,image)==c.scale(spin*c.I,image)
                assert not c.add(c.s.rot(0,2,image),c.scale(c.I,c.s.rot(1,2,image)))
                rem=reduce(spin,image);h=c.native.digest(c.ser(image))
                if position==0:assert h==reference[j,eta]
                rows.append({'background':j,'normal_axis':eta,'spin':spin,'image_terms':len(image),
                             'inside_receiver':not rem,'remainder_terms':len(rem),'image_sha256':h,
                             'witness_values':[c.C(image.get(k,0)).ser()for k in witnesses]if eta==9 else []})
        out['columns'].append({'n6_index':bi,'maps':rows,'seconds':time.monotonic()-tick})
        out['completed']=position+1;out['complete']=out['completed']==32
        out['coverage_by_axis']={str(a):all(r['inside_receiver']for col in out['columns']for r in col['maps']if r['normal_axis']==a)for a in(5,10,9)}
        out['direct_projection_controls']=177 if out['completed']else 0
        out['last_batch_seconds']=time.monotonic()-start;write(args.output,out)
        print('MIXED family',out['completed'],'/32',out['coverage_by_axis'],'column seconds',out['columns'][-1]['seconds'],flush=True)



def stage_witnesses(args):
    """Rigorous actual-root receiver nonmembership; not full-M nonmembership."""
    c=setup(args);reduce,metadata=receiver(c,args)
    basis,old=c.native.n6_basis(c,args.cache/'native-n6.json')
    path=args.family_input or args.cache/'mixed-family-v2.json';data=json.loads(path.read_text())
    funcs=(setup,receiver,active_domain,ambient_operator,input_patterns,prepare_input,projected_image,stage_family)
    live={'native_inputs':bindings(args)['native_inputs'],'receivers':metadata,
          'native_n6_sha256':digest(args.cache/'native-n6.json'),
          'implementation_sha256':hashlib.sha256('\n'.join(inspect.getsource(f)for f in funcs).encode()).hexdigest()}
    assert data['bindings']==live and data['complete']and data['completed']==32
    assert data['direct_projection_controls']==177
    ids=data['domain_indices'];assert ids==old['exact_probe']['spin6']['constraint_inverse']['constraint_components'][3]
    witnesses=[tuple(k)for k in data['witness_coordinates']]
    constants={}
    for index,V in zip((5,12),c.Vs):
        da=c.part(c.P(c.U[9](c.S[0](c.K(3,V)))),5,5)
        db=c.part(c.P(c.U[5](c.S[2](c.K(3,V)))),5,5)
        assert da and db
        assert reduce(5,db)==db
        assert all(not da.get(k,0)and not db.get(k,0)for k in witnesses)
        assert not c.P(c.K(2,V))  # y2=0, but db is NOT zero.
        constants[index]={'A_constant_terms':len(da),'B_constant_terms':len(db),
                          'both_constants_zero_on_selected_witnesses':True,
                          'A_constant_sha256':c.native.digest(c.ser(da)),
                          'B_constant_sha256':c.native.digest(c.ser(db)),
                          'B_source':c.ser(db),'B_entirely_outside_owned_receiver':True}
    # These coordinate rows annihilate BOTH owned spin5 receivers exactly.
    for cache in(args.e5_old,args.e5_new):
        bd=json.loads((cache/'inverse-stage3-basis.json').read_text())
        assert all((e,cl)not in witnesses for row in bd['basis']for e,cl,z in row)
    matrices={}
    for position,col in enumerate(data['columns']):
        assert col['n6_index']==ids[position]and len(col['maps'])==177
        rows=[r for r in col['maps']if r['normal_axis']==9]
        assert [r['background']for r in rows]==list(range(59))
        matrices[ids[position]]=[[c.C(*z)for z in r['witness_values']]for r in rows]
    ab=lambda z:abs(z.a)+abs(z.b)
    out={'scope':'Certified actual-root nonmembership in E5_old+E5_new only; no cokernel or no-repair conclusion.',
         'bindings':{'probe':bindings(args),'family_sha256':digest(path),'family_bindings':live},
         'coefficient_coverage':data['coverage_by_axis'],'witnesses_annihilate_owned_E5':True,
         'constant_controls':constants,'reduced_normal_spin2_maps':['4*(A-B)','2*(2*A+B)'],'roots':[]}
    for ri,r in enumerate(c.background['certified_roots']):
        theta=[Q(x)for x in r['coordinates']];radius=Q(r['certificate']['radius']);rr={'root':ri,'sources':[]}
        for index in(5,12):
            y,coeff,errors=c.native.responses(c,basis,old,ri,index)
            assert set(coeff)==set(ids)and set(errors)==set(ids)
            tests=[]
            for wi,key in enumerate(witnesses):
                row={i:sum((theta[j]*matrices[i][j][wi]for j in range(59)),c.C())for i in ids}
                variation={i:sum(ab(matrices[i][j][wi])for j in range(59))for i in ids}
                center=sum((row[i]*coeff[i]for i in ids),c.C())
                error=sum(errors[i]*ab(row[i])+radius*(ab(coeff[i])+errors[i])*variation[i]for i in ids)
                margin=ab(center)-error
                tests.append({'coordinate':list(key),'center':center.ser(),'error_bound':str(error),
                              'nonzero_margin':str(margin),'nonzero_margin_float':float(margin),
                              'certified_nonzero':margin>0,'both_reduced_maps_nonzero_margin':str(4*margin)})
            assert any(t['certified_nonzero']for t in tests),('No certified witness',ri,index)
            rr['sources'].append({'basis_index':index,'witnesses':tests,'outside_owned_receiver_at_exact_root':True,'both_reduced_normal_spin2_maps_outside':True,'A_B_independent_mod_owned_receiver':True})
        out['roots'].append(rr)
    out['all_four_actual_sources_outside_owned_E5']=True;write(args.output,out)
    print('MIXED exact-root witness margins',[[max(t['nonzero_margin_float']for t in r['witnesses'])for r in rr['sources']]for rr in out['roots']],flush=True)



def stage_numeric(args):
    """One actual eta9/root0/V5 center solve; diagnostic full ambient operator."""
    c=setup(args);basis,old=c.native.n6_basis(c,args.cache/'native-n6.json')
    T=c.add(*(c.scale(Q(x),v)for x,v in zip(c.background['certified_roots'][0]['coordinates'],c.Ts)))
    y,coeff,errors=c.native.responses(c,basis,old,0,5)
    constant=c.P(c.U[9](c.S[0](c.K(3,c.Vs[0]))))
    seed=c.part(c.add(constant,c.P(c.scale(-2,c.integer.N(c.U[9](T),y)))),5,5)
    assert not c.K(3,seed)and c.s.q['cas'](seed)==c.scale(30,seed)
    assert c.s.rot(0,1,seed)==c.scale(5*c.I,seed)
    assert not c.add(c.s.rot(0,2,seed),c.scale(c.I,c.s.rot(1,2,seed)))
    seed_B=c.part(c.P(c.U[5](c.S[2](c.K(3,c.Vs[0])))),5,5)
    assert seed_B
    assert all(((e^cl)&13319).bit_count()%2==0 for v in(seed,seed_B)for e,cl in v)
    original=c.w.build_seed_context
    def context(native_args,numeric=False):
        s=original(native_args,numeric);s.seeds=[seed];return s
    p=c.fast;p.w=c.w;p.g=c.g;p.C=c.C;p.I=c.I;p.add=c.add;p.scale=c.scale
    p.context=context;p.binding=lambda native_args:{'target':'actual_mixed_eta9_root0_V5_rational_center_diagnostic',
        'bindings':bindings(args),'seed_sha256':c.native.digest(c.ser(seed)),
        'constant_B_sha256':c.native.digest(c.ser(seed_B))}
    native_args=SimpleNamespace(root=args.repo,cache=args.cache,output=args.output,
        root_index=0,source_index=0,steps=args.steps or 40,prune=1e-13)
    p.stage_numeric(native_args)
    out=json.loads(args.output.read_text())
    out['source_A_rational_center']=c.ser(seed)
    out['source_B_exact_constant']=c.ser(seed_B)
    out['reduced_source_maps']=['4*(A-B)','2*(2*A+B)']
    out['scope']='NUMERICAL_DISCOVERY_ONLY actual mixed eta9/root0/V5 rational-center source, full ambient M matvec. No exact-root preimage or cokernel claim.'
    write(args.output,out)



def parity_controls(c,args):
    mask=13319
    parity=lambda e,cl:((e^cl)&mask).bit_count()%2
    assert all(parity(e,cl)==0 for T in c.Ts for e,cl in T)
    assert parity(8,0)==0
    for i,j in((0,1),(0,2),(1,2)):
        H=c.g.zero();H[i][j]=Q(1);H[j][i]=Q(-1)
        assert all(((mask>>a)&1)==((mask>>b)&1)for a in range(14)for b,z in c.g.h_action(H,a).items()if z)
    for cache in(args.e5_old,args.e5_new):
        bd=json.loads((cache/'inverse-stage3-basis.json').read_text())
        assert all(parity(e,cl)==1 for row in bd['basis']for e,cl,z in row)
    assert (args.cache/'native-n6.json').exists(),'Unpack the authenticated native N6 cache before controls.'
    nb,old=c.native.n6_basis(c,args.cache/'native-n6.json')
    ids=old['exact_probe']['spin6']['constraint_inverse']['constraint_components'][3]
    assert len(ids)==32
    assert all(parity(e,cl)==0 for i in ids for e,cl in nb[i])
    # Exterior algebra on the native weight eigenvectors; parity is homogeneous
    # on each eigenvector. The one-form factor uses the same weight character.
    wp=[(0,1),(0,0),(0,0),(0,0),(0,0),(0,1),
        (1,1),(-1,1),(1,1),(-1,1),(1,0),(-1,0),(2,0),(-2,0)]
    dp={(0,0,0):1}
    for w,p in wp:
        nxt=dict(dp)
        for(degree,weight,par),count in dp.items():
            key=(degree+1,weight+w,par^p);nxt[key]=nxt.get(key,0)+count
        dp=nxt
    char={}
    for(degree,weight,par),count in dp.items():
        if degree%4 not in(0,3):continue
        for w,p in wp:
            if not(par^p):char[weight+w]=char.get(weight+w,0)+count
    assert(char[5],char[6],char[5]-char[6])==(664,152,512)
    return {'parity_mask':mask,'backgrounds_even':59,'time_covector_even':True,
        'rotation_generators_preserve_parity':3,'both_old_E5_receivers_odd':True,
        'horizontal_Y_basis_even':32,'native_n6_sha256':digest(args.cache/'native-n6.json'),
        'even_ambient_weight5_dimension':664,'even_ambient_weight6_dimension':152,
        'complete_even_ambient_highest5_dimension':512,
        'even_N5_dimension':'Not computed; at most512. This is not an inverse certificate.'}


RECORD_NAMES=('mixed-controls.json','mixed-constants.json','mixed-affine.json',
              'mixed-family-v2.json','mixed-witnesses.json','mixed-numeric.json','native-n6.json')
BUNDLE_NAME='source-action-mixed-consistency-certificates.json'


def unpack_record(record):
    import base64,zlib
    assert record['encoding']=='zlib-base64-json'
    raw=zlib.decompress(base64.b64decode(record['data'],validate=True))
    assert len(raw)==record['uncompressed_bytes']
    assert hashlib.sha256(raw).hexdigest()==record['sha256']
    json.loads(raw);return raw


def stage_unpack(args):
    bundle=json.loads((args.repo/'lab/process'/BUNDLE_NAME).read_text())
    assert set(bundle['records'])==set(RECORD_NAMES)
    args.cache.mkdir(parents=True,exist_ok=True)
    for name in RECORD_NAMES:(args.cache/name).write_bytes(unpack_record(bundle['records'][name]))
    for cache,bundlename,certname in((args.e4,'source-action-spin4-certificates.json','spin4-fast-certificate.json'),
        (args.e5_old,'source-action-weak-response.json','inverse-stage5-certificate.json'),
        (args.e5_new,'source-action-constraint-source-repair-certificates.json','repair-fast-certificate.json')):
        bd=json.loads((args.repo/'lab/process'/bundlename).read_text())
        records=bd['reproduction']['records']if bundlename=='source-action-weak-response.json'else bd['records']
        cache.mkdir(parents=True,exist_ok=True)
        for name in('inverse-stage3-basis.json',certname):(cache/name).write_bytes(unpack_record(records[name]))
    print('MIXED unpacked',len(RECORD_NAMES),'records plus authenticated receiver bases/certificates',flush=True)


def stage_bundle(args):
    import base64,zlib
    records={}
    codehash=digest(Path(__file__))
    controls=json.loads((args.cache/'mixed-controls.json').read_text())
    constants=json.loads((args.cache/'mixed-constants.json').read_text())
    assert controls['bindings']['probe_sha256']==constants['bindings']['probe_sha256']==codehash
    for name in RECORD_NAMES:
        raw=(args.cache/name).read_bytes();json.loads(raw)
        records[name]={'encoding':'zlib-base64-json','sha256':hashlib.sha256(raw).hexdigest(),
            'uncompressed_bytes':len(raw),'data':base64.b64encode(zlib.compress(raw,9)).decode()}
    out={'schema':'gu-native-mixed-consistency-certificates-v1','data_only':True,
         'scope':'Actual mixed principal compatibility coverage and certified old-receiver noncoverage. Numeric solve is discovery only.',
         'final_probe_sha256':digest(Path(__file__)),'records':records}
    write(args.output,out);print('MIXED bundle',args.output,flush=True)


def stage_status(args):
    rows={name:json.loads((args.cache/name).read_text())for name in RECORD_NAMES}
    f=rows['mixed-family-v2.json'];w=rows['mixed-witnesses.json'];n=rows['mixed-numeric.json']
    codehash=digest(Path(__file__))
    assert rows['mixed-controls.json']['bindings']==rows['mixed-constants.json']['bindings']==bindings(args)
    assert w['bindings']['probe']==bindings(args)
    assert n['bindings']['bindings']==bindings(args)
    funcs=(setup,receiver,active_domain,ambient_operator,input_patterns,prepare_input,projected_image,stage_family)
    assert f['bindings']['implementation_sha256']==hashlib.sha256('\n'.join(inspect.getsource(fn)for fn in funcs).encode()).hexdigest()
    assert f['bindings']['native_inputs']==bindings(args)['native_inputs']
    assert w['bindings']['family_sha256']==digest(args.cache/'mixed-family-v2.json')
    out={'scope':'Status of authenticated local records; status alone does not recompute family images.',
         'probe_sha256':digest(Path(__file__)),'record_sha256':{name:digest(args.cache/name)for name in RECORD_NAMES},
         'family_columns_completed':f['completed'],'family_complete':f['complete'],
         'coefficient_coverage':f['coverage_by_axis'],
         'actual_root_old_receiver_noncoverage':w['all_four_actual_sources_outside_owned_E5'],
         'numeric':[{'root':r['root'],'info':r.get('info'),'relative_residual':r.get('relative_residual'),
                     'solution_support':r.get('solution_support')}for r in n['roots']]}
    write(args.output,out);print(json.dumps(out,indent=2),flush=True)


def stage_replay(args):
    # Recompute native controls, all constants and rational root witness bounds.
    # Full5664-map reproduction remains the explicit --mode family operation.
    original=args.output;results={}
    for name,func in(('controls',stage_controls),('constants',stage_constants),('witnesses',stage_witnesses)):
        prior=json.loads((args.cache/('mixed-'+name+'.json')).read_text())
        args.output=args.cache/('mixed-replay-'+name+'.json');func(args)
        now=json.loads(args.output.read_text())
        for value in(prior,now):value.pop('seconds',None)
        assert prior==now,('Replay differs',name)
        results[name]=True
    args.output=original
    family=json.loads((args.cache/'mixed-family-v2.json').read_text())
    assert family['complete']and family['completed']==32
    out={'scope':'Fresh-cache native controls/constants and exact root-witness replay; full family record authenticated, not recomputed by this bounded mode.',
         'probe_sha256':digest(Path(__file__)),'native_replays':results,
         'family_sha256':digest(args.cache/'mixed-family-v2.json'),'all_passed':True}
    write(args.output,out);print('MIXED bounded fresh-cache replay PASS',flush=True)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2])
    ap.add_argument('--cache',type=Path,required=True)
    ap.add_argument('--e4',type=Path)
    ap.add_argument('--e5-old',type=Path)
    ap.add_argument('--e5-new',type=Path)
    ap.add_argument('--mode',choices=('controls','constants','affine','family','witnesses','numeric','unpack','bundle','status','replay'),required=True)
    ap.add_argument('--steps',type=int,default=1)
    ap.add_argument('--output',type=Path)
    ap.add_argument('--family-input',type=Path)
    args=ap.parse_args();args.repo=args.repo.resolve()
    default_name='mixed-family-v2.json'if args.mode=='family'else 'mixed-'+args.mode+'.json'
    args.output=args.output or args.cache/default_name
    args.e4=args.e4 or args.cache/'receivers/e4'
    args.e5_old=args.e5_old or args.cache/'receivers/e5-old'
    args.e5_new=args.e5_new or args.cache/'receivers/e5-new'
    globals()['stage_'+args.mode](args)


if __name__=='__main__':main()
