#!/usr/bin/env python3
"""Complete remaining native auxiliary M blocks at the two owned W2/K95 roots.

Exact B=base-inversion sectors, complete carriers, paired-H certificates.
No physical-domain, wellposedness, propagation or GU verdict is inferred.
"""
from pathlib import Path
from fractions import Fraction as Q
from types import SimpleNamespace
from collections import Counter
import argparse, hashlib, inspect, json, os, sys, time
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[name]='1'
sys.dont_write_bytecode=True
import source_action_normal_normal_probe as nn
import source_action_even_spin5_probe as even

BLOCKS={'even0':(0,0,183,211),'odd0':(0,1,196,196),
        'even1':(1,0,512,480),'odd1':(1,1,496,496),
        'even2':(2,0,576,592),'odd2':(2,1,584,584),'even3':(3,0,490,462)}
B_MASK=15
ATOM_B_MASK=785
digest,jd,write,ser,decode=nn.digest,nn.jd,nn.write,nn.ser,nn.decode


def setup(args):
    c=nn.setup(args)
    assert all(B(c,T)==T for T in c.Ts),'Every owned background direction must be B-fixed.'
    return c


def inputs(args):
    out=nn.bindings(args)['native_inputs']
    for name in ('tests/program-focus/source_action_normal_normal_probe.py',
                 'lab/process/source-action-normal-normal-certificates.json',
                 'lab/process/source-action-coupled-ghost.json'):
        out[name]=digest(args.repo/name)
    return out


def procedure(*functions):
    return hashlib.sha256('\n'.join(inspect.getsource(f)for f in functions).encode()).hexdigest()


def binding(args):
    return {'native_inputs':inputs(args),'blocks':{k:list(v)for k,v in BLOCKS.items()},
            'B_native_mask':B_MASK,'B_atom_mask':ATOM_B_MASK,
            'constructor_procedure_sha256':procedure(setup,inputs,procedure,binding,B,selection,space,
                high_binding,load_highest,insert_field,check_field,build_carrier)}


def B(c,v):
    return {k:z*((-1)**(((k[0]^k[1])&B_MASK).bit_count()%2))for k,z in v.items()}


def selection(args):
    labels=list(BLOCKS)if args.block=='all'else[args.block]
    sectors=(0,1)if args.sector=='both'else(0 if args.sector=='plus'else 1,)
    return [(label,b)for label in labels for b in sectors]


def space(c,label,b):
    spin,chi,*dims=BLOCKS[label];_,car=nn.carrier_setup(c,spin,chi)
    keys={m:[key for key in car.keys[m]
              if (((ATOM_B_MASK>>key[0])&1)+(key[1]&ATOM_B_MASK).bit_count())%2==b]
          for m in (spin,spin+1)}
    return car,keys,spin,chi,dims[b]


def high_binding(args,label,b):
    return binding(args)|{'block':label,'B_sector':b}


def load_highest(c,args,label,b):
    car,keys,spin,chi,n=space(c,label,b);prefix=label+('-plus'if b==0 else'-minus')
    path=args.cache/(prefix+'-highest.json');live=high_binding(args,label,b);tick=time.monotonic()
    W=[car.native(key)for key in keys[spin]]
    if path.exists():
        data=json.loads(path.read_text());assert data['bindings']==live and data['complete']
        assert data['weight_keys']==[list(k)for k in keys[spin]]
    else:
        columns=[]
        for i,v in enumerate(W):
            assert car.coordinates(v)=={car.lookup[spin][keys[spin][i]]:c.C(1)}
            assert B(c,v)==c.scale((-1)**b,v)
            columns.append(car.coordinates(c.Eraise(v),spin+1))
            if(i+1)%256==0:print('FULL raising',prefix,i+1,'/',len(W),'seconds',time.monotonic()-tick,flush=True)
        rows,ker=even.sparse_kernel(c,columns)
        highest=len(keys[spin])-len(keys[spin+1])
        assert len(rows)==len(keys[spin+1])and len(ker)==highest
        data={'bindings':live,'complete':True,'spin':spin,'chi':chi,'B_sector':b,
              'weight_dimension':len(W),'next_weight_dimension':len(keys[spin+1]),'highest_dimension':highest,
              'weight_keys':[list(k)for k in keys[spin]],
              'raising_columns':[even.coordinates_serial(v)for v in columns],
              'highest_coordinates':[even.coordinates_serial(v)for v in ker],
              'execution_probe_sha256':digest(__file__),'seconds':time.monotonic()-tick}
        write(path,data)
    H=[even.combine(c,{i:c.C(*z)for i,z in row},W)for row in data['highest_coordinates']]
    return car,H,path,data,n


def insert_field(c,v,rows,pivots):
    v=dict(v)
    while v:
        k=min(v);z=v[k]
        if k not in pivots:
            v={key:x/z for key,x in v.items()};pivots[k]=len(rows);rows.append(v);return True
        for key,x in rows[pivots[k]].items():
            value=v.get(key,c.C())-z*x
            if value:v[key]=value
            else:v.pop(key,None)
    return False


def check_field(c,v,spin,chi,b):
    assert not c.K(3,v)and not c.Eraise(v)
    assert c.s.rot(0,1,v)==c.scale(spin*c.I,v)
    assert c.s.q['cas'](v)==c.scale(spin*(spin+1),v)
    assert all(((e^cl)&13319).bit_count()%2==chi for e,cl in v)
    assert B(c,v)==c.scale((-1)**b,v)


def stage_profile(args):
    c=setup(args);out={'execution_probe_sha256':digest(__file__),'bindings':binding(args),'sectors':[]}
    for label,b in selection(args):
        tick=time.monotonic();car,H,path,high,n=load_highest(c,args,label,b)
        count=min(args.steps or 32,len(H));rows=[];piv={};pt=0.;kt=0.;kcols=[]
        for v in H[:count]:
            start=time.monotonic();p=c.P(v);pt+=time.monotonic()-start
            insert_field(c,p,rows,piv)
            start=time.monotonic();kcols.append(car.coordinates(c.K(3,v)));kt+=time.monotonic()-start
        kr,kk=even.sparse_kernel(c,kcols)
        row={'block':label,'B_sector':b,'highest_dimension':len(H),'expected_N':n,'columns':count,
             'projector_seconds':pt,'projected_rank':len(rows),'Kt_seconds':kt,'Kt_partial_rank':len(kr),
             'total_seconds':time.monotonic()-tick}
        out['sectors'].append(row);print('FULL PROFILE',json.dumps(row),flush=True)
    write(args.cache/'profile.json',out)


def build_carrier(c,args,label,b):
    tick=time.monotonic();car,H,hp,high,n=load_highest(c,args,label,b)
    prefix=label+('-plus'if b==0 else'-minus');spin,chi,*_=BLOCKS[label]
    path=args.cache/(prefix+'-construction.json');bp=args.cache/(prefix+'-basis.json')
    live=high_binding(args,label,b)|{'highest_sha256':digest(hp),'method':args.method}
    if bp.exists():
        result=json.loads(bp.read_text());assert result['bindings']==live and result['complete'];return result
    data={'bindings':live,'completed':0,'images':[],'complete':False,'execution_probe_sha256':digest(__file__)}
    if path.exists():
        data=json.loads(path.read_text());assert data['bindings']==live and data['completed']==len(data['images'])
    rows=[];pivots={}
    if args.method=='projector':
        for field in data['images']:insert_field(c,decode(c,field),rows,pivots)
    for i in range(data['completed'],len(H)):
        if args.method=='projector':
            if len(rows)==n:break
            field=c.P(H[i]);assert B(c,field)==c.scale((-1)**b,field)
            data['images'].append(ser(c,field));insert_field(c,field,rows,pivots)
        else:
            field=c.K(3,H[i]);assert B(c,field)==c.scale((-1)**(1-b),field)
            data['images'].append(even.coordinates_serial(car.coordinates(field)))
        data['completed']=i+1
        if(i+1)%32==0 or i+1==len(H)or(args.method=='projector'and len(rows)==n):
            data['seconds']=time.monotonic()-tick;write(path,data)
            print('FULL kernel',prefix,args.method,i+1,'/',len(H),'rank',len(rows),'seconds',data['seconds'],flush=True)
    if args.method=='direct':
        cols=[{i:c.C(*z)for i,z in row}for row in data['images']]
        r,k=even.sparse_kernel(c,cols);assert len(k)==n
        for co in k:insert_field(c,even.combine(c,co,H),rows,pivots)
        data['Kt_rank']=len(r)
    assert len(rows)==n
    for v in rows:check_field(c,v,spin,chi,b)
    result={'bindings':live,'complete':True,'spin':spin,'chi':chi,'B_sector':b,
            'dimension':n,'highest_dimension':len(H),'time_rank':len(H)-n,
            'construction_sha256':None,'basis':[ser(c,v)for v in rows],
            'pivots':[list(min(v))for v in rows],'completeness':'Exact native independent kernel/highest vectors attain owned saturated-character dimension.',
            'execution_probe_sha256':digest(__file__),'seconds':time.monotonic()-tick}
    data['complete']=True;write(path,data);result['construction_sha256']=digest(path);write(bp,result)
    print('FULL CARRIER',prefix,'dimension',n,'seconds',result['seconds'],flush=True);return result


def stage_carrier(args):
    c=setup(args)
    for label,b in selection(args):build_carrier(c,args,label,b)


def load_block(c,args,label,b):
    prefix=label+('-plus'if b==0 else'-minus');path=args.cache/(prefix+'-basis.json')
    d=json.loads(path.read_text());live=high_binding(args,label,b)
    assert d['complete']and all(d['bindings'][k]==v for k,v in live.items())
    basis=[decode(c,row)for row in d['basis']];assert len(basis)==BLOCKS[label][2+b]
    phases=[];Z=[]
    for v in basis:
        kv={k:z.conj()*((-1)**(((k[0]^k[1])&11525).bit_count()%2))for k,z in v.items()}
        sign=kv[min(v)]/v[min(v)];assert sign in(c.C(1),c.C(-1))and kv==c.scale(sign,v)
        phase=c.C(1)if sign==1 else c.I;phases.append(phase.ser());Z.append(c.scale(phase,v))
    meta={'basis_sha256':digest(path),'dimension':len(Z),'B_sector':b,'block':label,
          'kappa_mask':11525,'column_phases':phases,'phase_aligned_kappa_sign':1}
    return d,basis,[tuple(k)for k in d['pivots']],Z,meta


def matrix_binding(args,meta):
    return {'native_inputs':inputs(args),'block':meta,
            'procedure_sha256':procedure(load_block,matrix_binding,stage_matrix)}


def stage_matrix(args):
    c=setup(args);E=c.integer
    for label,b in selection(args):
        bd,basis,pivots,Z,meta=load_block(c,args,label,b);n=len(Z);_,qd,qi=even.paired_rows(c,Z)
        prefix=label+('-plus'if b==0 else'-minus');live=matrix_binding(args,meta)
        for ri,root in enumerate(c.background['certified_roots']):
            if args.root_index is not None and ri!=args.root_index:continue
            path=args.cache/(prefix+f'-root{ri}-matrix.json')
            out={'bindings':live,'dimension':n,'root':ri,'root_record_sha256':jd(root),'completed':0,
                 'columns':[],'image_controls':[],'complete':False,'execution_probe_sha256':digest(__file__)}
            if path.exists():out=json.loads(path.read_text());assert out['bindings']==live
            assert out['root_record_sha256']==jd(root)and out['completed']==len(out['columns'])
            T=c.add(*(c.scale(Q(x),v)for x,v in zip(root['coordinates'],c.Ts)))
            du,ui,au=E.prepare(T);tick=time.monotonic();start=out['completed'];end=n if args.steps==0 else min(n,start+args.steps)
            for j in range(start,end):
                one=time.monotonic();dv,vi,av=E.prepare(Z[j])
                numerator=E.Phi_scaled(E.wedge_comm_int(ui,vi))
                c.fast.add_into(numerator,E.wadj_scaled(ui,av));c.fast.add_into(numerator,E.wadj_scaled(vi,au))
                denominator=3*E.Dphi*du*dv;c.fast.add_into(numerator,vi,3*E.Dphi*du);numerator=c.fast.prune(numerator)
                assert all(e.bit_count()==1 and cl.bit_count()%4 in(0,3)and ((e^cl)&13319).bit_count()%2==bd['chi']
                           and ((e^cl)&B_MASK).bit_count()%2==b for e,cl in numerator)
                col=even.paired_integer(c,qi,n,numerator,denominator,qd);assert all(not z.b for z in col)
                if j==0:
                    raw=E.restore(numerator,denominator);projected=c.P(raw)
                    rem,co=even.reduce_field(c,projected,basis,pivots);assert not rem
                    check_field(c,projected,bd['spin'],bd['chi'],b)
                    assert all(col[i]==c.E.pair({k:z.conj()for k,z in Z[i].items()},raw)for i in range(n))
                    out['first_column_full_native_range_pairing_control']=True
                out['columns'].append([[i,z.ser()]for i,z in enumerate(col)if z]);out['completed']=j+1
                out['image_controls'].append({'column':j,'native_C_image_terms':len(numerator),'denominator':str(denominator),
                    'integer_image_sha256':jd([[e,cl,str(a),str(bb)]for(e,cl),(a,bb)in sorted(numerator.items())]),
                    'seconds':time.monotonic()-one})
                if(j+1)%8==0 or j+1==end:
                    out['last_batch_seconds']=time.monotonic()-tick;write(path,out)
                    print('FULL H',prefix,ri,j+1,'/',n,'seconds',out['last_batch_seconds'],flush=True)
            if out['completed']==n:
                cols=[{i:c.C(*z)for i,z in row}for row in out['columns']]
                assert all(cols[j].get(i,c.C())==cols[i].get(j,c.C())for i in range(n)for j in range(n))
                out.update({'real_symmetric':True,'complete':True});write(path,out)
        E.clear_prepared()


def stage_certify(args):
    import numpy as np
    c=setup(args);arithmetic=nn.arithmetic_controls(args.backend)
    for label,b in selection(args):
        bd,basis,pivots,Z,meta=load_block(c,args,label,b);n=len(Z);prefix=label+('-plus'if b==0 else'-minus')
        w,exactD,norm=even.norm_constants(c,Z)
        D=[Q(1<<(((d.numerator+d.denominator-1)//d.denominator)-1).bit_length())for d in exactD]
        assert all(a>=v>0 for a,v in zip(D,exactD))
        for ri,root in enumerate(c.background['certified_roots']):
            if args.root_index is not None and ri!=args.root_index:continue
            stem=prefix+f'-root{ri}';path=args.cache/(stem+'-matrix.json');record=json.loads(path.read_text())
            assert record['bindings']==matrix_binding(args,meta)and record['complete']and record['dimension']==n
            assert record['root_record_sha256']==jd(root)and record['real_symmetric']and record['first_column_full_native_range_pairing_control']
            Hr,Hi,DH=even.dense_paired_matrix(c,record|{'hermitian':record['real_symmetric']},n)
            assert not any(int(v)for row in Hi for v in row)
            H,zero,den,_=even.balanced_matrix(Hr,Hi,DH,D);assert not any(int(v)for row in zero for v in row)
            live={'native_inputs':inputs(args),'block':meta,'root':ri,'root_record_sha256':jd(root),'matrix_sha256':digest(path),
                  'procedure_sha256':procedure(load_block,stage_certify),'balanced_integer_denominator':str(den),
                  'integer_basis_norm_majorants':[str(v)for v in D]}
            tick=time.monotonic();R,DR=nn.real_candidate(args,stem,H,den,live)
            eta0,engine=nn.real_defect(H,den,R,DR,args.backend)
            Ctri=even.triangle_bound(c,Z,D,w,R,np.zeros((n,n),dtype=object),DR)
            radius=Q(root['certificate']['radius']);delta=2196*radius*Q(128637452,3)*Ctri;eta=eta0+delta
            out={'bindings':live,'execution_probe_sha256':digest(__file__),'dimension':n,'complete':True,
                 'norm_constants':norm,'integer_basis_norm_majorants':[str(v)for v in D],
                 'radius':str(radius),'balanced_center_defect_column1':str(eta0),'Ctriangle_upper':str(Ctri),
                 'rootbox_perturbation_column1':str(delta),'neumann_bound':str(eta),'neumann_bound_float':float(eta),
                 'native_M_invertible_on_complete_sector':eta<1,'arithmetic_backend':engine,'arithmetic_controls':arithmetic,
                 'preconditioner_sha256':digest(args.cache/(stem+'-inverse-candidates.json')),'seconds':time.monotonic()-tick,
                 'scope':'Complete native auxiliary sector range at held root box; no propagation, wellposedness, physical admission or GU verdict.'}
            write(args.cache/(stem+'-certificate.json'),out)
            print('FULL CERT',stem,'eta0',float(eta0),'delta',float(delta),'total',float(eta),'PASS',eta<1,flush=True)


def stage_status(args):
    out=authenticated_status(args)
    if args.output:write(args.output,out)
    print(json.dumps(out,indent=2),flush=True)


def owned_character(args):
    import source_action_mixed_consistency_probe as mixed
    path=args.repo/'lab/process/source-action-normal-normal-certificates.json';bundle=json.loads(path.read_text())
    assert bundle['final_probe_sha256']==digest(args.repo/'tests/program-focus/source_action_normal_normal_probe.py')
    character=mixed.unpack_record(bundle['records']['normal-time-kernel-character.json'])
    controls=json.loads(mixed.unpack_record(bundle['records']['normal-controls.json']))
    assert controls['complete']and controls['all_complete_certificates_pass']
    for name,sha in controls['dependencies'].items():assert digest(args.repo/name)==sha,('Changed inherited native input',name)
    target=args.cache/'normal-time-kernel-character.json'
    if target.exists():assert target.read_bytes()==character
    else:target.write_bytes(character)
    return json.loads(character),controls['dependencies'],bundle['records']['normal-time-kernel-character.json']['sha256']


def symmetry_controls(c,args):
    tick=time.monotonic();data,deps,sha=owned_character(args);checked=nn.character_controls(c,args)
    car,keys,_,_,_=space(c,'even0',0);atoms=[]
    for i,atom in enumerate(car.atoms):
        sign=(-1)**((ATOM_B_MASK>>i)&1)
        assert all((-1)**((mask&B_MASK).bit_count()%2)==sign for mask in atom)
        atoms.append((car.weights[i],car.charges[i],(ATOM_B_MASK>>i)&1))
    ambient=Counter()
    for mask in range(1<<14):
        if mask.bit_count()%4 not in(0,3):continue
        weight=sum(a[0]for i,a in enumerate(atoms)if mask>>i&1)
        chi=sum(a[1]for i,a in enumerate(atoms)if mask>>i&1)%2
        bb=sum(a[2]for i,a in enumerate(atoms)if mask>>i&1)%2
        for w,p,b in atoms:ambient[weight+w,chi^p,bb^b]+=1
    rows=[]
    for label,(j,p,plus,minus)in BLOCKS.items():
        total=data['highest_multiplicities']['even'if p==0 else'odd'][str(j)]
        traces=[ambient[m,p,0]-ambient[m,p,1]for m in(j,j+1)];trace=traces[0]-traces[1]
        assert(plus+minus,plus-minus)==(total,trace)
        rows.append({'block':label,'spin':j,'chi':p,'N':total,'B_plus':plus,'B_minus':minus,
                     'trace_B':trace,'ambient_highest_B':[ambient[j,p,b]-ambient[j+1,p,b]for b in(0,1)]})
    for T in c.Ts:
        assert B(c,T)==T and all(((e^cl)&13319).bit_count()%2==0 for e,cl in T)
        assert all(not c.s.rot(i,j,T)for i,j in((0,1),(0,2),(1,2)))
    column_count=0
    for block in data['principal_blocks']:
        for key in block['basis']:
            v={tuple(key):c.C(1)};assert B(c,c.K(3,v))==c.scale(-1,c.K(3,B(c,v)))
            assert c.E.pair(B(c,v),B(c,v))==c.E.pair(v,v);column_count+=1
    rotation=(-1,1,-1,1);signs=list(rotation)
    for a in c.g.A:
        moved=[[rotation[i]*a[i][j]*rotation[j]for j in range(4)]for i in range(4)]
        matches=[s for s in(1,-1)if moved==[[s*z for z in row]for row in a]];assert len(matches)==1;signs+=matches
    assert sum(1<<i for i,s in enumerate(signs)if s<0)==11525
    return {'complete':True,'native_dependencies':deps,'owned_character_record_sha256':sha,
            'full_character_replay':checked,'B_native_mask':B_MASK,'B_atom_mask':ATOM_B_MASK,
            'atom_weight_chi_B':atoms,'sector_dimensions':rows,'backgrounds_B_fixed_rotation_fixed_chi_even':59,
            'native_Kt_B_anticommutation_columns':column_count,'native_pairing_B_isometry_unit_controls':column_count,
            'native_kappa_rotation_mask':11525,'seconds':time.monotonic()-tick,
            'structural_argument':'B is a native metric isometry preserving N and R because BAB=-A; hence BP=PB. Natural cubic covariance and BT=T give BC=CB and BM=MB throughout each root box. The B-twisted trace of invertible R vanishes.'}


def stage_symmetry(args):
    c=setup(args);out=symmetry_controls(c,args);out['execution_probe_sha256']=digest(__file__)
    write(args.cache/'symmetry-controls.json',out);print('FULL SYMMETRY PASS seconds',out['seconds'],flush=True)


def stage_controls(args):
    tick=time.monotonic();c=setup(args);sym=symmetry_controls(c,args);rows=[]
    for label,b in selection(args):
        bd,basis,pivots,Z,meta=load_block(c,args,label,b);prefix=label+('-plus'if b==0 else'-minus')
        independent=[];ps={}
        for v in basis:
            assert all(0<=e<(1<<14)and 0<=cl<(1<<14)and e.bit_count()==1
                       and cl.bit_count()%4 in(0,3)and isinstance(z.a,Q)and isinstance(z.b,Q)and bool(z)
                       for(e,cl),z in v.items()),'Exact native one-form/imaginary-Clifford ambient membership required.'
            check_field(c,v,bd['spin'],bd['chi'],b);assert insert_field(c,v,independent,ps)
        assert len(independent)==BLOCKS[label][2+b]
        q,qd,qi=even.paired_rows(c,Z)
        for ri,root in enumerate(c.background['certified_roots']):
            stem=prefix+f'-root{ri}';record=json.loads((args.cache/(stem+'-matrix.json')).read_text())
            assert record['complete']and record['bindings']==matrix_binding(args,meta)
            validate_producer(args,record)
            T=c.add(*(c.scale(Q(x),v)for x,v in zip(root['coordinates'],c.Ts)))
            raw=c.add(Z[0],c.scale(2,c.E.N(T,Z[0])));first=record['image_controls'][0];den=int(first['denominator']);ints=[]
            assert B(c,raw)==c.scale((-1)**b,raw)
            for(e,cl),z in sorted(raw.items()):
                a,bb=z.a*den,z.b*den;assert a.denominator==bb.denominator==1
                ints.append([e,cl,str(int(a)),str(int(bb))])
            assert jd(ints)==first['integer_image_sha256']
            dv,vi=c.integer.clear_denominators(raw);column=even.paired_integer(c,qi,len(Z),vi,dv,qd)
            assert [[i,z.ser()]for i,z in enumerate(column)if z]==record['columns'][0]
            assert all(not z.b for z in column)
            cert=json.loads((args.cache/(stem+'-certificate.json')).read_text())
            assert cert['complete']and cert['native_M_invertible_on_complete_sector']and Q(cert['neumann_bound'])<1
            rows.append({'block':label,'B_sector':b,'root':ri,'dimension':len(Z),
                         'exact_native_basis_rank':len(independent),'explicit_native_ambient_membership':True,
                         'native_kernel_highest_chi_B_residuals_zero':True,
                         'original_Fraction_C_image_matches_integer_image':True,'all_first_H_column_entries_match':True,
                         'phase_real_and_signed_H_symmetric':record['real_symmetric'],
                         'rootbox_certificate_pass':True})
    out={'complete':True,'execution_probe_sha256':digest(__file__),'native_inputs':inputs(args),
         'symmetry':sym,'sector_controls':rows,'seconds':time.monotonic()-tick,
         'scope':'Complete native sector certificates with original-engine first-column controls; other native H columns authenticated, not independently recomputed here.'}
    write(args.cache/f'controls-{args.block}-{args.sector}.json',out)
    print('FULL CONTROLS PASS',len(rows),'root sectors seconds',out['seconds'],flush=True)


def authenticated_status(args):
    c=setup(args);owned_character(args);rows=[]
    for label,b in selection(args):
        prefix=label+('-plus'if b==0 else'-minus');bp=args.cache/(prefix+'-basis.json')
        if not bp.exists():continue
        bd,basis,pivots,Z,meta=load_block(c,args,label,b);n=len(Z)
        w,norms,norm=even.norm_constants(c,Z)
        D=[Q(1<<(((v.numerator+v.denominator-1)//v.denominator)-1).bit_length())for v in norms]
        for ri,root in enumerate(c.background['certified_roots']):
            stem=prefix+f'-root{ri}';cp=args.cache/(stem+'-certificate.json')
            if not cp.exists():continue
            mp=args.cache/(stem+'-matrix.json');matrix=json.loads(mp.read_text());cert=json.loads(cp.read_text())
            assert matrix['complete']and matrix['bindings']==matrix_binding(args,meta)and matrix['dimension']==n
            validate_producer(args,matrix)
            assert matrix['root_record_sha256']==jd(root)and matrix['root']==ri
            expected={'native_inputs':inputs(args),'block':meta,'root':ri,'root_record_sha256':jd(root),
                      'matrix_sha256':digest(mp),'procedure_sha256':procedure(load_block,stage_certify),
                      'balanced_integer_denominator':cert['bindings']['balanced_integer_denominator'],
                      'integer_basis_norm_majorants':[str(v)for v in D]}
            assert cert['bindings']==expected and cert['norm_constants']==norm and cert['dimension']==n and cert['complete']
            rp=args.cache/(stem+'-inverse-candidates.json');candidate=json.loads(rp.read_text())
            assert digest(rp)==cert['preconditioner_sha256']and len(candidate['roots'])==1
            rr=candidate['roots'][0];assert rr['bindings']==expected and rr['dimension']==n and rr['root']==ri
            eta0=Q(cert['balanced_center_defect_column1']);delta=Q(cert['rootbox_perturbation_column1']);eta=Q(cert['neumann_bound'])
            assert Q(cert['radius'])==Q(root['certificate']['radius'])
            assert delta==2196*Q(cert['radius'])*Q(128637452,3)*Q(cert['Ctriangle_upper'])and eta==eta0+delta
            assert cert['native_M_invertible_on_complete_sector']==(eta<1)
            rows.append({'block':label,'B_sector':b,'root':ri,'dimension':n,'neumann_bound':float(eta),
                         'exact_neumann_bound':str(eta),'pass':eta<1,'certificate_sha256':digest(cp),
                         'current_basis_matrix_root_candidate_function_bindings_verified':True})
    prior=inherited_regular_controls(args.repo)
    return {'probe_sha256':digest(__file__),'certificates':rows,'all28pass':len(rows)==28 and all(r['pass']for r in rows),
            'inherited_regular_sectors':prior,
            'scope':'Authenticated saved exact certificates; status does not recompute integer matrix defects. Replay performs that arithmetic.'}


def record_names(label,ri):
    names=[]
    for sign in ('plus','minus'):
        prefix=label+'-'+sign
        if ri==0:names.extend(prefix+'-'+suffix+'.json'for suffix in('highest','construction','basis'))
        names.extend(prefix+f'-root{ri}-'+suffix+'.json'for suffix in('matrix','inverse-candidates','certificate'))
    return names


def bundle_name(label,ri):
    return f'source-action-full-auxiliary-{label}-root{ri}-certificates.json'


def encode_record(path):
    import base64,zlib
    raw=path.read_bytes();json.loads(raw)
    return {'encoding':'zlib-base64-json','uncompressed_bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
            'data':base64.b64encode(zlib.compress(raw,9)).decode()}


def stage_bundle(args):
    status=authenticated_status(args);assert status['all28pass']
    controls=json.loads((args.cache/'controls-all-both.json').read_text())
    assert controls['complete']and controls['execution_probe_sha256']==digest(__file__)and len(controls['sector_controls'])==28
    groups={};record_hashes={}
    for label in BLOCKS:
        for ri in(0,1):
            records={name:encode_record(args.cache/name)for name in record_names(label,ri)}
            out={'schema':'gu-full-auxiliary-sector-data-v1','data_only':True,'final_probe_sha256':digest(__file__),
                 'block':label,'root':ri,'B_sectors':[0,1],'records':records}
            path=args.repo/'lab/process'/bundle_name(label,ri);write(path,out)
            assert path.stat().st_size<100_000_000
            groups[path.name]={'sha256':digest(path),'bytes':path.stat().st_size,'records':{n:r['sha256']for n,r in records.items()}}
            record_hashes.update(groups[path.name]['records']);print('FULL BUNDLE',path.name,path.stat().st_size,flush=True)
    assert len(record_hashes)==126
    out={'schema':'gu-full-auxiliary-manifest-v1','data_only':True,'final_probe_sha256':digest(__file__),
         'native_inputs':inputs(args),'bundles':groups,
         'records':{name:encode_record(args.cache/name)for name in('controls-all-both.json','packing-benchmark.json')},
         'authenticated_status':status,'new_complete_real_coefficient_dimension':25082,
         'inherited_complete_real_coefficient_dimension':24072,'complete_time_kernel_dimension':49154,
         'scope':'Full native auxiliary M regularity on the49154-dimensional time kernel of the held autonomous imaginary-U W2/K95 block, at the two owned root boxes. No physical-domain necessity, wellposedness, propagated solution or GU verdict.'}
    path=args.repo/'lab/process/source-action-full-auxiliary-certificates.json';write(path,out)
    print('FULL MANIFEST',path,'records',len(record_hashes)+2,flush=True)


def restore_or_authenticate(args,restore):
    import source_action_mixed_consistency_probe as mixed
    path=args.repo/'lab/process/source-action-full-auxiliary-certificates.json';manifest=json.loads(path.read_text())
    assert manifest['schema']=='gu-full-auxiliary-manifest-v1'and manifest['data_only']
    assert manifest['final_probe_sha256']==digest(__file__)and manifest['native_inputs']==inputs(args)
    expected={bundle_name(label,ri)for label in BLOCKS for ri in(0,1)};assert set(manifest['bundles'])==expected
    hashes={}
    for label in BLOCKS:
        for ri in(0,1):
            name=bundle_name(label,ri);p=path.parent/name;meta=manifest['bundles'][name]
            assert digest(p)==meta['sha256'];bundle=json.loads(p.read_text())
            assert bundle['schema']=='gu-full-auxiliary-sector-data-v1'and bundle['data_only']
            assert bundle['final_probe_sha256']==digest(__file__)and(bundle['block'],bundle['root'])==(label,ri)
            assert set(bundle['records'])==set(record_names(label,ri))==set(meta['records'])
            for n,r in bundle['records'].items():
                assert r['sha256']==meta['records'][n];raw=mixed.unpack_record(r);target=args.cache/n
                if restore:target.write_bytes(raw)
                else:assert target.read_bytes()==raw
                hashes[n]=r['sha256']
    assert set(manifest['records'])=={'controls-all-both.json','packing-benchmark.json'}
    for n,r in manifest['records'].items():
        raw=mixed.unpack_record(r)
        if restore:(args.cache/n).write_bytes(raw)
        else:assert(args.cache/n).read_bytes()==raw
        hashes[n]=r['sha256']
    return manifest,hashes


def stage_unpack(args):
    manifest,hashes=restore_or_authenticate(args,True);owned_character(args)
    print('FULL UNPACK',len(hashes),'records',flush=True)


def stage_replay(args):
    import subprocess
    tick=time.monotonic();manifest,hashes=restore_or_authenticate(args,False)
    rebuilt=args.cache/'recomputed';rebuilt.mkdir(exist_ok=True);log=rebuilt/'carrier-replay.log'
    common=[sys.executable,__file__,'--repo',str(args.repo),'--cache',str(rebuilt),'--mode','carrier','--method','direct']
    if args.rebuild_carriers:
        for label in BLOCKS:
            for sign in('plus','minus'):
                with log.open('a')as f:subprocess.run(common+['--block',label,'--sector',sign],stdout=f,stderr=subprocess.STDOUT,check=True)
                prefix=label+'-'+sign
                for suffix,fields in(
                    ('highest',('spin','chi','B_sector','weight_dimension','next_weight_dimension','highest_dimension','weight_keys','raising_columns','highest_coordinates','complete')),
                    ('construction',('completed','images','Kt_rank','complete')),
                    ('basis',('spin','chi','B_sector','dimension','highest_dimension','time_rank','basis','pivots','complete'))):
                    name=prefix+'-'+suffix+'.json';nn.same_fields(json.loads((args.cache/name).read_text()),json.loads((rebuilt/name).read_text()),fields,name)
                print('FULL REPLAY carrier',prefix,'PASS',flush=True)
    packed_check=args.cache/'recomputed-packing';packed_check.mkdir(exist_ok=True)
    for name in('even0-plus-basis.json','even0-plus-root0-matrix.json','even0-plus-root1-matrix.json'):
        (packed_check/name).write_bytes((args.cache/name).read_bytes())
    bench=SimpleNamespace(**vars(args));bench.cache=packed_check;bench.block='even0';bench.sector='plus';bench.steps=32
    stage_packed_benchmark(bench)
    oldbench=json.loads((args.cache/'packing-benchmark.json').read_text());newbench=json.loads((packed_check/'packing-benchmark.json').read_text())
    assert oldbench['packing_procedure_sha256']==newbench['packing_procedure_sha256']
    for oldrow,newrow in zip(oldbench['reports'],newbench['reports']):
        nn.same_fields(oldrow,newrow,('block','B_sector','columns_per_root','column_indices','all_complete_native_images_equal','max_radix_bits'),'packing')
    certificates={name:(args.cache/name).read_bytes()for name in hashes if name.endswith('-certificate.json')}
    frozen_controls=(args.cache/'controls-all-both.json').read_bytes()
    child=SimpleNamespace(**vars(args));child.block='all';child.sector='both';child.root_index=None;child.generate_candidates=False
    stage_certify(child)
    fields=('bindings','dimension','norm_constants','integer_basis_norm_majorants','radius','balanced_center_defect_column1',
            'Ctriangle_upper','rootbox_perturbation_column1','neumann_bound','native_M_invertible_on_complete_sector','preconditioner_sha256')
    for name,raw in certificates.items():
        nn.same_fields(json.loads(raw),json.loads((args.cache/name).read_text()),fields,name);(args.cache/name).write_bytes(raw)
    stage_controls(child)
    old=json.loads(frozen_controls);new=json.loads((args.cache/'controls-all-both.json').read_text())
    nn.same_fields(old,new,('complete','native_inputs','sector_controls'),'controls')
    nn.same_fields(old['symmetry'],new['symmetry'],[k for k in old['symmetry']if k!='seconds'],'symmetry')
    (args.cache/'controls-all-both.json').write_bytes(frozen_controls)
    status=authenticated_status(child);assert status['all28pass']
    assert all(digest(args.cache/name)==sha for name,sha in hashes.items())
    out={'passed':True,'probe_sha256':digest(__file__),'manifest_sha256':digest(args.repo/'lab/process/source-action-full-auxiliary-certificates.json'),
         'record_count':len(hashes),'complete_carriers_verified_by_native_membership_independence_and_character':14,
         'full_carriers_reconstructed':14 if args.rebuild_carriers else 0,
         'native_H_columns_recomputed':28,'all_native_H_columns_recomputed':False,
         'all_12116_H_columns_used_in_exact_defects':True,'floating_inverse_regenerated':False,
         'two_root_packing_full_native_images_recomputed_and_compared_to_fresh_direct':64,
         'inherited_certificates_authenticated':True,'seconds':time.monotonic()-tick,
         'scope':'Bounded native replay: all complete carriers verified by exact native ambient/kernel/highest membership, full rank and independent character dimension; first original C/H column each root/sector and all exact certificate arithmetic; remaining12088 H columns authenticated.'}
    write(args.output or args.cache/'full-replay.json',out);print('FULL REPLAY PASS seconds',out['seconds'],flush=True)


def stage_compare(args):
    assert args.reference_cache is not None
    for label,b in selection(args):
        prefix=label+('-plus'if b==0 else'-minus')
        for ri in(0,1):
            name=prefix+f'-root{ri}-matrix.json';old=json.loads((args.reference_cache/name).read_text());new=json.loads((args.cache/name).read_text())
            nn.same_fields(old,new,('bindings','dimension','root','root_record_sha256','completed','columns','real_symmetric','complete'),name)
            assert[entry['integer_image_sha256']for entry in old['image_controls']]==[entry['integer_image_sha256']for entry in new['image_controls']]
    print('FULL native matrix mathematical columns and raw image hashes MATCH',flush=True)


def prepare_root_pair(c):
    from math import lcm
    E=c.integer;prepared=[]
    for root in c.background['certified_roots']:
        T=c.add(*(c.scale(Q(x),v)for x,v in zip(root['coordinates'],c.Ts)))
        prepared.append(E.prepare(T))
    du=lcm(*(p[0]for p in prepared));scaled=[]
    for own,u,a in prepared:
        factor=du//own
        scaled.append((own,{k:(x*factor,y*factor)for k,(x,y)in u.items()},
                       {k:(x*factor,y*factor)for k,(x,y)in a.items()}))
    weights=nn.weights()
    norm0=sum(weights[cl]*(abs(a)+abs(b))for(e,cl),(a,b)in scaled[0][1].items())
    return du,scaled,weights,norm0


def packed_C_images(c,prepared,v):
    """Exact centered-integer encoding of two real-linear background inputs.

    F(U,V)=6Dphi*N(U,V) is Gaussian integral. The old1098 weighted bound
    bounds each real/imag coefficient of Cnum0 because every native weight>=1.
    Decode before signed pairing; return each original per-root denominator.
    """
    du,roots,weights,norm0=prepared;E=c.integer;dv,vi,av=E.prepare(v)
    normv=sum(weights[cl]*(abs(a)+abs(b))for(e,cl),(a,b)in vi.items())
    bound0=(6*E.Dphi*1098*norm0+3*E.Dphi*du)*normv
    radix=1<<(2*bound0).bit_length();assert radix>2*bound0
    ui=dict(roots[0][1]);c.fast.add_into(ui,roots[1][1],radix)
    au=dict(roots[0][2]);c.fast.add_into(au,roots[1][2],radix)
    numerator=E.Phi_scaled(E.wedge_comm_int(ui,vi))
    c.fast.add_into(numerator,E.wadj_scaled(ui,av));c.fast.add_into(numerator,E.wadj_scaled(vi,au))
    c.fast.add_into(numerator,vi,3*E.Dphi*du*(1+radix))
    out=[{},{}];factors=[du//r[0]for r in roots]
    for key,(a,b)in numerator.items():
        a0=(a+radix//2)%radix-radix//2;b0=(b+radix//2)%radix-radix//2
        assert abs(a0)<=bound0 and abs(b0)<=bound0
        values=((a0,b0),((a-a0)//radix,(b-b0)//radix))
        for ri,(x,y)in enumerate(values):
            assert x%factors[ri]==y%factors[ri]==0
            x//=factors[ri];y//=factors[ri]
            if x or y:out[ri][key]=(x,y)
    return out,[3*E.Dphi*r[0]*dv for r in roots],{'radix_bits':radix.bit_length(),'root0_component_bound':str(bound0)}


def stage_packed_benchmark(args):
    c=setup(args);reports=[]
    for label,b in selection(args):
        bd,basis,pivots,Z,meta=load_block(c,args,label,b);prefix=label+('-plus'if b==0 else'-minus')
        records=[json.loads((args.cache/(prefix+f'-root{ri}-matrix.json')).read_text())for ri in(0,1)]
        assert all(r['complete']and r['bindings']==matrix_binding(args,meta)for r in records)
        prepared=prepare_root_pair(c);count=min(args.steps or 32,len(Z))
        indices=sorted({j*(len(Z)-1)//max(1,count-1)for j in range(count)});tick=time.monotonic();packed=[]
        for j in indices:
            v=Z[j]
            images,dens,control=packed_C_images(c,prepared,v)
            for ri in(0,1):
                expected=records[ri]['image_controls'][j]
                assert dens[ri]==int(expected['denominator'])
                assert jd([[e,cl,str(a),str(bb)]for(e,cl),(a,bb)in sorted(images[ri].items())])==expected['integer_image_sha256']
            packed.append(control)
        elapsed=time.monotonic()-tick
        direct=sum(r['image_controls'][j]['seconds']for r in records for j in indices)
        # Fresh direct integer production, excluding inherited cold P/pairing time.
        tick=time.monotonic();E=c.integer
        for ri,(own,ui,au)in enumerate(prepared[1]):
            factor=prepared[0]//own;ui={k:(a//factor,bb//factor)for k,(a,bb)in ui.items()};au={k:(a//factor,bb//factor)for k,(a,bb)in au.items()}
            for j in indices:
                v=Z[j]
                dv,vi,av=E.prepare(v);num=E.Phi_scaled(E.wedge_comm_int(ui,vi))
                c.fast.add_into(num,E.wadj_scaled(ui,av));c.fast.add_into(num,E.wadj_scaled(vi,au));c.fast.add_into(num,vi,3*E.Dphi*own)
                num=c.fast.prune(num)
                assert jd([[e,cl,str(a),str(bb)]for(e,cl),(a,bb)in sorted(num.items())])==records[ri]['image_controls'][j]['integer_image_sha256']
        direct_fresh=time.monotonic()-tick
        row={'block':label,'B_sector':b,'columns_per_root':len(indices),'column_indices':indices,'all_complete_native_images_equal':True,
             'packed_seconds':elapsed,'fresh_direct_seconds':direct_fresh,'historical_with_pairing_seconds':direct,
             'speed_ratio_fresh_direct_over_packed':direct_fresh/elapsed,'max_radix_bits':max(v['radix_bits']for v in packed)}
        reports.append(row);print('FULL PACKED BENCHMARK',json.dumps(row),flush=True)
    write(args.cache/'packing-benchmark.json',{'execution_probe_sha256':digest(__file__),
          'packing_procedure_sha256':procedure(prepare_root_pair,packed_C_images,stage_packed_benchmark),'reports':reports})


def packed_producer(args):
    benchmark=args.cache/'packing-benchmark.json';data=json.loads(benchmark.read_text())
    assert data['packing_procedure_sha256']==procedure(prepare_root_pair,packed_C_images,stage_packed_benchmark)
    assert data['reports']and all(r['all_complete_native_images_equal']for r in data['reports'])
    return {'method':'exact_two_root_integer_packing',
            'implementation_sha256':procedure(prepare_root_pair,packed_C_images,packed_producer,stage_matrix_packed),
            'benchmark_sha256':digest(benchmark),
            'binding_semantics':'bindings.procedure_sha256 specifies the unchanged canonical direct mathematical/reproduction algorithm; this separate implementation_sha256 authenticates the actual packed producer. Original per-root denominators are restored.'}


def validate_producer(args,record):
    if 'actual_producer'in record:assert record['actual_producer']==packed_producer(args)


def stage_matrix_packed(args):
    if args.root_index is not None or not(args.cache/'packing-benchmark.json').exists():return stage_matrix(args)
    c=setup(args);E=c.integer;producer=packed_producer(args)
    for label,b in selection(args):
        bd,basis,pivots,Z,meta=load_block(c,args,label,b);n=len(Z);prefix=label+('-plus'if b==0 else'-minus')
        paths=[args.cache/(prefix+f'-root{ri}-matrix.json')for ri in(0,1)]
        existing=[json.loads(p.read_text())if p.exists()else None for p in paths]
        # Preserve every existing direct producer and its checkpoint semantics.
        if any(r is not None and 'actual_producer'not in r for r in existing):
            child=SimpleNamespace(**vars(args));child.block=label;child.sector='plus'if b==0 else'minus'
            stage_matrix(child);continue
        live=matrix_binding(args,meta);records=[]
        for ri,root in enumerate(c.background['certified_roots']):
            r=existing[ri]or{'bindings':live,'actual_producer':producer,'dimension':n,'root':ri,
                'root_record_sha256':jd(root),'completed':0,'columns':[],'image_controls':[],
                'complete':False,'execution_probe_sha256':digest(__file__)}
            assert r['bindings']==live and r['actual_producer']==producer and r['root_record_sha256']==jd(root)
            assert r['completed']==len(r['columns']);records.append(r)
        _,qd,qi=even.paired_rows(c,Z);prepared=prepare_root_pair(c)
        weights,_,norm=even.norm_constants(c,[Z[0]]);assert weights==prepared[2]and Q(norm['N_bilinear_bound'])==1098
        begin=min(r['completed']for r in records);end=n if args.steps==0 else min(n,begin+args.steps);tick=time.monotonic()
        for j in range(begin,end):
            one=time.monotonic();images,dens,control=packed_C_images(c,prepared,Z[j])
            for ri,(r,numerator,denominator)in enumerate(zip(records,images,dens)):
                rawhash=jd([[e,cl,str(a),str(bb)]for(e,cl),(a,bb)in sorted(numerator.items())])
                if j<r['completed']:
                    assert r['image_controls'][j]['integer_image_sha256']==rawhash
                    continue
                assert j==r['completed']
                assert all(e.bit_count()==1 and cl.bit_count()%4 in(0,3)and ((e^cl)&13319).bit_count()%2==bd['chi']
                           and ((e^cl)&B_MASK).bit_count()%2==b for e,cl in numerator)
                col=even.paired_integer(c,qi,n,numerator,denominator,qd);assert all(not z.b for z in col)
                if j==0:
                    raw=E.restore(numerator,denominator);projected=c.P(raw)
                    rem,co=even.reduce_field(c,projected,basis,pivots);assert not rem
                    check_field(c,projected,bd['spin'],bd['chi'],b)
                    assert all(col[i]==c.E.pair({k:z.conj()for k,z in Z[i].items()},raw)for i in range(n))
                    r['first_column_full_native_range_pairing_control']=True
                r['columns'].append([[i,z.ser()]for i,z in enumerate(col)if z]);r['completed']=j+1
                r['image_controls'].append({'column':j,'native_C_image_terms':len(numerator),'denominator':str(denominator),
                    'integer_image_sha256':rawhash,'seconds':(time.monotonic()-one)/2,
                    'shared_two_root_packing_control':control})
            if(j+1)%8==0 or j+1==end:
                for p,r in zip(paths,records):r['last_batch_seconds_shared_two_roots']=time.monotonic()-tick;write(p,r)
                print('FULL PACKED H',prefix,j+1,'/',n,'both roots seconds',time.monotonic()-tick,flush=True)
        for p,r in zip(paths,records):
            if r['completed']==n:
                cols=[{i:c.C(*z)for i,z in row}for row in r['columns']]
                assert all(cols[j].get(i,c.C())==cols[i].get(j,c.C())for i in range(n)for j in range(n))
                r.update({'real_symmetric':True,'complete':True});write(p,r)
        E.clear_prepared()


def inherited_regular_controls(repo):
    """Authenticate owned regular carriers; no native matrices/defects reassembled.

    Exact scalar bound arithmetic and all referenced compressed bytes are checked.
    Carrier rank and dense-product proofs are inherited from their authenticated
    accepted records, not rerun or replaced by this aggregation.
    """
    from pathlib import Path
    from fractions import Fraction as F
    import base64, hashlib, json, zlib
    repo = Path(repo)
    files, records, documents, raw_cache = {}, {}, {}, {}
    def digest(raw): return hashlib.sha256(raw).hexdigest()
    def jd(obj): return digest(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode())
    def file_hash(name):
        if name not in files: files[name] = digest((repo / name).read_bytes())
        return files[name]
    def load(name):
        if name not in documents:
            raw = (repo / name).read_bytes(); files[name] = digest(raw)
            documents[name] = json.loads(raw)
        return documents[name]
    def check_paths(mapping):
        for name, expected in mapping.items():
            if '/' in name and isinstance(expected, str) and len(expected) == 64:
                assert file_hash(name) == expected, ('inherited_native_binding', name)
    def record(bundle_name, name, parse=True):
        bundle = load(bundle_name)
        rs = bundle['reproduction']['records'] if 'reproduction' in bundle else bundle['records']
        item = rs[name]; key = bundle_name + '::' + name
        if key not in raw_cache:
            assert item['encoding'] == 'zlib-base64-json'
            raw = zlib.decompress(base64.b64decode(item['data'], validate=True))
            assert len(raw) == item['uncompressed_bytes']
            assert digest(raw) == item['sha256'], ('inherited_record_hash', key)
            raw_cache[key] = raw; records[key] = item['sha256']
        return json.loads(raw_cache[key]) if parse else records[key]
    def record_hash(bundle, name): return record(bundle, name, False)
    def checked_roots(rows):
        assert [r['root'] for r in rows] == [0, 1]
        return rows
    background_name = 'lab/process/source-action-deep-coefficients.json'
    background = load(background_name); roots = background['certified_roots']
    assert len(roots) == 2
    radii = [F(r['certificate']['radius']) for r in roots]
    def bind_root(row):
        ri = row['root']; assert ri in (0, 1)
        if 'radius' in row: assert F(row['radius']) == radii[ri]
        if 'root_radius' in row: assert F(row['root_radius']) == radii[ri]
        for key in ('root_record_sha256', 'owned_root_record_sha256'):
            if key in row: assert row[key] == jd(roots[ri]), ('root_record', ri, key)
    bound_rows = []
    def bound(label, row, defect_key, delta_key):
        bind_root(row)
        defect, delta, eta = F(row[defect_key]), F(row[delta_key]), F(row['neumann_bound'])
        assert defect >= 0 and delta >= 0 and eta == defect + delta and eta < 1
        bound_rows.append({'block': label, 'root': row['root'], 'neumann_bound': str(eta)})
    # Complete N7 and N6, with owned full-carrier dimensions and all components.
    kname = 'lab/process/source-action-kappa1-constraints.json'; old = load(kname)
    check_paths(old['dependencies'])
    s7 = old['exact_probe']['spin7']
    assert (s7['time_kernel'], s7['kernel_gram_rank'], s7['real_spin7_kernel_dimension']) == (16, 16, 240)
    for row in checked_roots(s7['root_certificates']):
        bind_root(row); eta = F(row['neumann_bound'])
        assert F(row['center_defect']) == 0
        assert eta == F(row['radius']) * F(row['affine_inverse_coefficient_bound']) and 0 <= eta < 1
        bound_rows.append({'block': 'N7_complete16', 'root': row['root'], 'neumann_bound': str(eta)})
    s6 = old['exact_probe']['spin6']['constraint_inverse']
    assert (s6['multiplicity_kernel_dimension'], s6['kernel_pairing_rank'], s6['real_rotation_spin6_kernel_dimension']) == (128, 128, 1664)
    comps = s6['constraint_components']
    assert sorted(i for component in comps for i in component) == list(range(128))
    assert [len(c) for c in comps] == [32] * 4
    for row, candidates in zip(checked_roots(s6['root_certificates']), checked_roots(old['spin6_inverse_candidates'])):
        assert len(row['blocks']) == len(candidates['blocks']) == 4
        for bi, (b, c) in enumerate(zip(row['blocks'], candidates['blocks'])):
            assert b['component'] == c['component'] == bi and b['dimension'] == c['dimension'] == 32
            assert c['indices'] == comps[bi]
            assert jd(c['rational_inverse']) == b['rational_inverse_sha256']
            assert all(len(line) == 32 for line in c['rational_inverse'])
            x = dict(b, root=row['root']); bind_root(x)
            eta = F(b['center_defect']) + F(b['inverse_norm_bound']) * F(b['root_radius']) * F(b['coefficient_norm_bound'])
            assert eta == F(b['neumann_bound']) == F(c['neumann_bound']) and 0 <= eta < 1
            bound_rows.append({'block': 'N6_component' + str(bi), 'root': row['root'], 'neumann_bound': str(eta)})
    # Complete even N5 and authenticated odd N5 exhaustion by two old120 spaces.
    ename = 'lab/process/source-action-even-spin5-certificates.json'
    eb = load(ename); check_paths(eb['native_inputs'])
    assert eb['probe_sha256'] == file_hash('tests/program-focus/source_action_even_spin5_probe.py')
    ec = record(ename, 'even-certificate.json'); check_paths(ec['bindings']['native_inputs'])
    assert ec['dimension'] == 240
    for key, name in [('basis_sha256', 'even-basis.json'), ('validation_sha256', 'even-validation.json'), ('matrix_sha256', 'even-root-matrices.json')]:
        assert ec['bindings'][key] == record_hash(ename, name)
    assert ec['preconditioner_sha256'] == record_hash(ename, 'even-inverse-candidates.json')
    ev = record(ename, 'even-validation.json'); assert ev['dimension'] == ev['gram_rank'] == 240
    for row in checked_roots(ec['roots']):
        assert F(row['rootbox_perturbation_column1']) == 2196 * radii[row['root']] * F('128637452/3') * F(row['Ctriangle_upper'])
        bound('N5_even240', row, 'balanced_center_defect_column1', 'rootbox_perturbation_column1')
    oc = record(ename, 'odd-completion.json'); check_paths(oc['bindings']['native_inputs'])
    assert oc['weight5_dimension'] - oc['raising_rank'] == oc['ambient_highest5_dimension'] == 536
    assert 536 - oc['time_symbol_rank'] == oc['complete_N5_odd_dimension'] == oc['owned_odd_receiver_rank'] == 240
    for short, cname in [('source-action-weak-response.json', 'inverse-stage5-certificate.json'), ('source-action-constraint-source-repair-certificates.json', 'repair-fast-certificate.json')]:
        name = 'lab/process/' + short; owned = oc['owned_receivers'][short]
        assert file_hash(name) == owned['bundle_sha256']
        assert owned['dimension'] == 120
        assert record_hash(name, 'inverse-stage3-basis.json') == owned['basis_sha256']
        assert record_hash(name, cname) == owned['certificate_sha256']
        cert = record(name, cname); assert cert['dimension'] == 120 and cert['family_maps'] == 59
        assert cert['bindings']['background_sha256'] == file_hash(background_name)
        assert cert['bindings']['basis_sha256'] == owned['basis_sha256']
        for row in checked_roots(cert['roots']):
            assert row['neumann_bound'] == owned['root_neumann_bounds'][row['root']]
            bound('N5_odd120_' + short, row, 'center_preconditioned_residual_inf', 'rootball_perturbation_inf')
        if short == 'source-action-weak-response.json':
            check_paths(load(name)['sha256'])
            assert cert['bindings']['closure_sha256'] == record_hash(name, 'inverse-stage4-closure-certified.json')
        else:
            assert load(name)['probe_sha256'] == file_hash('tests/program-focus/source_action_constraint_source_repair_probe.py')
            check_paths(cert['bindings'].get('closure_bindings', {}).get('native_inputs', {}))
            assert cert['bindings']['closure_sha256'] == record_hash(name, 'repair-closure-integer.json')
            assert cert['preconditioner_sha256'] == record_hash(name, 'repair-inverse-candidates.json')
    # Full N4 and odd N3, including the separately owned E4 complement sum.
    nn = 'lab/process/source-action-normal-normal-certificates.json'; nb = load(nn)
    assert nb['final_probe_sha256'] == file_hash('tests/program-focus/source_action_normal_normal_probe.py')
    e4bundle = 'lab/process/source-action-spin4-certificates.json'
    e4cert = record(e4bundle, 'spin4-fast-certificate.json')
    e4basis = record(e4bundle, 'inverse-stage3-basis.json')
    assert e4cert['dimension'] == 282 and e4cert['family_maps'] == 59
    assert e4cert['bindings']['basis_sha256'] == record_hash(e4bundle, 'inverse-stage3-basis.json')
    assert e4cert['bindings']['background_sha256'] == file_hash(background_name)
    assert e4cert['bindings']['closure_sha256'] == record_hash(e4bundle, 'spin4-closure-integer-v2.json')
    check_paths(e4cert['bindings']['closure_bindings']['native_inputs'])
    for row in checked_roots(e4cert['roots']):
        assert row['preconditioner_sha256'] == record_hash(e4bundle, 'spin4-inverse-candidates.json')
        bound('N4_even_E4_282', row, 'center_preconditioned_residual_inf', 'rootball_perturbation_inf')
    for label, dim, full in [('even4', 286, 568), ('odd4', 568, 568), ('odd3', 952, 952)]:
        cert = record(nn, label + '-certificate.json'); basis = record(nn, label + '-basis.json')
        check_paths(cert['bindings']['native_inputs']); check_paths(basis['bindings']['native_inputs'])
        assert cert['dimension'] == dim and cert['complete_carrier_dimension'] == full
        assert basis['dimension'] == full and basis['ambient_highest_dimension'] - basis['time_rank'] == full
        block = cert['bindings']['block']
        assert block['basis_sha256'] == record_hash(nn, label + '-basis.json')
        assert cert['bindings']['matrix_sha256'] == record_hash(nn, label + '-matrices.json')
        assert cert['preconditioner_sha256'] == record_hash(nn, label + '-inverse-candidates.json')
        if label == 'even4':
            assert block['complete_dimension'] == full and block['owned_E4_dimension'] == block['native_Gram_rank_E4'] == 282
            assert block['old_basis_sha256'] == record_hash(e4bundle, 'inverse-stage3-basis.json')
            assert block['old_certificate_sha256'] == record_hash(e4bundle, 'spin4-fast-certificate.json')
            oldsupport = {(int(e), int(c)) for row in e4basis['basis'] for e,c,*_ in row}
            inside, outside = [], []
            for i, row in enumerate(basis['basis']):
                support = {(int(e), int(c)) for e,c,*_ in row}
                if support <= oldsupport: inside.append(i)
                elif support.isdisjoint(oldsupport): outside.append(i)
                else: raise AssertionError(('E4_partition_mixed', i))
            assert len(inside) == 282 and len(outside) == 286 and outside == block['retained_indices']
        for row in checked_roots(cert['roots']):
            assert F(row['rootbox_perturbation_column1']) == 2196 * radii[row['root']] * F('128637452/3') * F(row['Ctriangle_upper'])
            bound(label, row, 'balanced_center_defect_column1', 'rootbox_perturbation_column1')
    coverage = [
        {'spin':7, 'parity':'both', 'highest_multiplicity':16, 'real_dimension':240},
        {'spin':6, 'parity':'both', 'highest_multiplicity':128, 'real_dimension':1664},
        {'spin':5, 'parity':'both', 'highest_multiplicity':480, 'real_dimension':5280},
        {'spin':4, 'parity':'both', 'highest_multiplicity':1136, 'real_dimension':10224},
        {'spin':3, 'parity':'odd', 'highest_multiplicity':952, 'real_dimension':6664},
    ]
    total = sum(r['real_dimension'] for r in coverage); assert total == 24072
    return {'scope':'Inherited accepted carrier/root certificates authenticated by current dependencies, exact raw record hashes, ownership/dimension links and rational scalar bound arithmetic. No native basis ranks or dense matrix defects reassembled here.',
            'coverage':coverage, 'inherited_regular_real_dimension':total,
            'both_roots':[0,1], 'root_record_sha256':[jd(r) for r in roots],
            'bound_checks':bound_rows, 'files_sha256':files, 'records_sha256':records}


def guard_producer_resume(args):
    if args.mode=='packed_benchmark'and(args.cache/'packing-benchmark.json').exists():
        for path in args.cache.glob('*-root*-matrix.json'):
            assert 'actual_producer'not in json.loads(path.read_text()),'Packing benchmark is frozen by matrix producers; rerun in a separate cache.'
    if args.mode!='matrix':return
    for label,b in selection(args):
        prefix=label+('-plus'if b==0 else'-minus')
        roots=(args.root_index,)if args.root_index is not None else(0,1)
        records=[]
        for ri in roots:
            p=args.cache/(prefix+f'-root{ri}-matrix.json');records.append(json.loads(p.read_text())if p.exists()else None)
        direct_path=(args.matrix_method=='direct'or args.root_index is not None
                     or not(args.cache/'packing-benchmark.json').exists()
                     or any(r is not None and 'actual_producer'not in r for r in records))
        partial=lambda r:not r.get('complete')or r.get('completed')!=r.get('dimension')or len(r.get('columns',[]))!=r.get('dimension')
        assert not(direct_path and any(r is not None and 'actual_producer'in r and partial(r)for r in records)),\
            'Resume partial packed records with both roots and the packed producer, or use a fresh direct cache; hybrid labels are forbidden.'


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2]);ap.add_argument('--cache',type=Path,required=True)
    ap.add_argument('--block',choices=['all']+list(BLOCKS),default='all');ap.add_argument('--sector',choices=('both','plus','minus'),default='both')
    ap.add_argument('--method',choices=('direct','projector'),default='direct');ap.add_argument('--root-index',type=int,choices=(0,1))
    ap.add_argument('--matrix-method',choices=('direct','packed'),default='packed')
    ap.add_argument('--steps',type=int,default=32);ap.add_argument('--backend',choices=('auto','flint','python'),default='auto')
    ap.add_argument('--precision',type=int,default=24);ap.add_argument('--generate-candidates',action='store_true');ap.add_argument('--output',type=Path)
    ap.add_argument('--reference-cache',type=Path)
    ap.add_argument('--rebuild-carriers',action='store_true',help='Optional complete highest/time-kernel constructor rediscovery during replay')
    ap.add_argument('--mode',choices=('profile','carrier','matrix','certify','symmetry','controls','status','bundle','unpack','replay','compare','packed_benchmark'),required=True)
    args=ap.parse_args();args.repo=args.repo.resolve();args.cache=args.cache.resolve();args.cache.mkdir(parents=True,exist_ok=True)
    assert args.repo==Path(__file__).resolve().parents[2],'Run the installed probe from its own repository; mixed-checkout imports are forbidden.'
    pause=args.cache/'pause-native'
    if pause.exists()and args.mode!='packed_benchmark':
        write(args.cache/'paused.json',{'mode':args.mode,'block':args.block,'sector':args.sector,'pid':os.getpid()})
        print('FULL PAUSED at safe child boundary',flush=True)
        while pause.exists():time.sleep(1)
        (args.cache/'paused.json').unlink(missing_ok=True)
    guard_producer_resume(args)
    if args.mode=='matrix'and args.matrix_method=='packed':stage_matrix_packed(args)
    else:globals()['stage_'+args.mode](args)


if __name__=='__main__':main()
