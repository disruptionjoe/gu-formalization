#!/usr/bin/env python3
"""Actual six pure-normal first-consistency channels, with native full-K terms.

All six channel types and both Q copies remain in scope. A failed receiver
membership is not a full-M obstruction; negative conclusions retain every
allowed normal and zero-order kernel-multiplier repair.
"""
from pathlib import Path
from fractions import Fraction as Q
from types import SimpleNamespace
import argparse,hashlib,inspect,json,os,sys,time
for name in('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[name]='1'
sys.dont_write_bytecode=True


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def jd(value):return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def write(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_suffix(path.suffix+'.new');temp.write_text(json.dumps(value,indent=2)+'\n');temp.replace(path)
def ser(c,v):return [[e,cl,c.C(z).ser()]for(e,cl),z in sorted(v.items())]


def setup(args):
    sys.path.insert(0,str(args.repo/'tests/program-focus'))
    import source_action_mixed_consistency_probe as mixed
    c=mixed.setup(args);c.mixed=mixed
    c.covectors={'a':{5:c.C(1),8:-c.I},'b':{9:c.C(1),11:-c.I},'c':{10:c.C(1),12:-c.I}}
    operators={i:mixed.ambient_operator(c,i)for i in range(4,14)}
    c.Ucov=lambda cov,v:c.add(*(c.scale(z,operators[i](v))for i,z in cov.items()))
    c.Kcov=lambda cov,v:c.add(*(c.scale(z,c.K(i,v))for i,z in cov.items()))
    def covrot(i,j,cov):
        H=c.g.zero();H[i][j]=Q(1);H[j][i]=Q(-1)
        acts=[c.g.h_action(H,a)for a in range(14)];out={}
        for a,z in cov.items():
            for b in range(14):
                t=-acts[b].get(a,Q())
                if t:out[b]=out.get(b,c.C())+z*t
        return {k:z for k,z in out.items()if z}
    c.covrot=covrot
    c.Eraise=lambda v:c.add(c.s.rot(0,2,v),c.scale(c.I,c.s.rot(1,2,v)))
    c.Flower=lambda v:c.add(c.s.rot(0,2,v),c.scale(-c.I,c.s.rot(1,2,v)))
    return c


def bindings(args):
    names=('source_action_mixed_consistency_probe.py','source_action_even_spin5_probe.py',
        'source_action_constraint_consistency_probe.py','source_action_spin4_compatibility_probe.py',
        'source_action_weak_response_probe.py','source_action_paired_response_probe.py',
        'source_action_deep_algebra.py','source_action_deep_geometry.py','source_action_metric_symbol_probe.py')
    result={'tests/program-focus/'+name:digest(args.repo/'tests/program-focus'/name)for name in names}
    for name in('source-action-deep-coefficients.json','source-action-kappa1-constraints.json',
        'source-action-reduced-evolution.json','source-action-weak-response.json',
        'source-action-spin4-certificates.json','source-action-even-spin5-certificates.json'):
        result['lab/process/'+name]=digest(args.repo/'lab/process'/name)
    return {'native_inputs':result,'probe_sha256':digest(__file__)}


def input_controls(c):
    a,b,v=c.covectors['a'],c.covectors['b'],c.covectors['c']
    for name,weight,spin in(('a',-2,2),('b',-1,2),('c',-1,1)):
        x=c.covectors[name]
        assert c.covrot(0,1,x)==c.scale(weight*c.I,x)
        cas=c.scale(-1,c.add(*(c.covrot(i,j,c.covrot(i,j,x))for i,j in((0,1),(0,2),(1,2)))))
        assert cas==c.scale(spin*(spin+1),x)
    ea=c.add(c.covrot(0,2,a),c.scale(c.I,c.covrot(1,2,a)))
    scalar=ea[next(iter(b))]/b[next(iter(b))];assert ea==c.scale(scalar,b)
    assert scalar
    return {'weights':{'a':-2,'b':-1,'c':-1},'spins':{'a':2,'b':2,'c':1},
        'raising_a_equals_lambda_b':scalar.ser(),
        'qaa_raising_equals_2lambda_qab':(2*scalar).ser(),
        'input_types':['Sym2(V2) rank4: a*a, a*b','V2*V1 rank3: a*c'],
        'representatives':['Pi3 q(a,a)/2','Pi4 q(a,b)','Pi4 q(a,c)'],
        'convention':'q is the symmetric full-cross principal coefficient; diagonal quadratic coefficient is q(a,a)/2.'}


def spin4_receiver(c,args):
    path=args.repo/'lab/process/source-action-spin4-certificates.json';bundle=json.loads(path.read_text())
    b= json.loads(c.mixed.unpack_record(bundle['records']['inverse-stage3-basis.json']))
    cert=json.loads(c.mixed.unpack_record(bundle['records']['spin4-fast-certificate.json']))
    assert len(cert['roots'])==2 and all(r['invertible_on_block_over_rootball']and Q(r['neumann_bound'])<1 for r in cert['roots'])
    basis=[{(e,cl):c.C(*z)for e,cl,z in row}for row in b['basis']]
    pivots=[tuple(k)for k in b['basis_pivots']]
    def reduce(v):
        for i in sorted(range(len(basis)),key=lambda i:pivots[i]):
            z=v.get(pivots[i],0)
            if z:v=c.add(v,c.scale(-z,basis[i]))
        return v
    return reduce,{'basis_sha256':bundle['records']['inverse-stage3-basis.json']['sha256'],
        'certificate_sha256':bundle['records']['spin4-fast-certificate.json']['sha256'],'dimension':len(basis)}


def stage_constants(args):
    tick=time.monotonic();c=setup(args);inputs=input_controls(c);reduce,E4=spin4_receiver(c,args)
    out={'scope':'Exact native channel spanning/constant terms only; no actual-root range verdict.',
        'bindings':bindings(args),'input_controls':inputs,'E4':E4,'sources':[]}
    lam=c.C(*inputs['raising_a_equals_lambda_b'])
    for index,V in zip((5,12),c.Vs):
        primary={name:c.P(c.Kcov(cov,V))for name,cov in c.covectors.items()}
        fullK={name:c.Kcov(cov,V)for name,cov in c.covectors.items()}
        assert c.Eraise(primary['a'])==c.scale(lam,primary['b'])
        assert c.Eraise(fullK['a'])==c.scale(lam,fullK['b'])
        assert c.K(8,V)==c.scale(c.I,c.K(5,V))
        assert c.K(12,V)==c.scale(c.I,c.K(10,V))
        rows=[];constant={}
        for x,y,j,lo,factor in(('a','a',3,3,Q(1,2)),('a','b',4,4,Q(1)),('a','c',4,4,Q(1))):
            raw=c.P(c.add(c.Ucov(c.covectors[x],fullK[y]),c.Ucov(c.covectors[y],fullK[x])))
            d=c.scale(factor,c.part(raw,j,lo));constant[x,y,j]=d
            assert not c.K(3,d)and c.s.q['cas'](d)==c.scale(j*(j+1),d)
            assert c.s.rot(0,1,d)==c.scale(j*c.I,d)and not c.Eraise(d)
            parity=1 if y!='c'else 0
            assert all(((e^cl)&13319).bit_count()%2==parity for e,cl in d)
            rem=reduce(d)if j==4 else None
            rows.append({'pair':[x,y],'spin':j,'parity':parity,'terms':len(d),'source':ser(c,d),
                'source_sha256':jd(ser(c,d)),'E4_remainder_terms':None if rem is None else len(rem),
                'inside_E4':None if rem is None else not rem})
            print('NN constant',index,x,y,j,'terms',len(d),'E4 remainder',None if rem is None else len(rem),flush=True)
        aa=c.P(c.scale(2,c.Ucov(c.covectors['a'],fullK['a'])))
        aa4=c.part(aa,4,3)
        assert c.Eraise(aa4)==c.scale(2*lam,constant['a','b',4])
        assert c.Flower(c.Eraise(aa4))==c.scale(-8,aa4)
        out['sources'].append({'Q_basis_index':index,'primary_terms':{name:len(v)for name,v in primary.items()},
            'full_K_terms':{name:len(v)for name,v in fullK.items()},'full_K_sources':{name:ser(c,v)for name,v in fullK.items()},
            'primary_sources':{name:ser(c,v)for name,v in primary.items()},'constants':rows,
            'native_raising_identity_qaa_to_qab':True})
        out['seconds']=time.monotonic()-tick;write(args.cache/'normal-constants.json',out)
    out['complete']=True;write(args.cache/'normal-constants.json',out)



def decode(c,row):return {(e,cl):c.C(*z)for e,cl,z in row}
def n1(c,z):z=c.C(z);return abs(z.a)+abs(z.b)
def linear(c,basis,coords):return c.add(*(c.scale(z,v)for z,v in zip(coords,basis)if z))

def load_primaries(c,args):
    oldbundle=json.loads((args.repo/'lab/process/source-action-weak-response.json').read_text())['reproduction']['records']
    old={name:json.loads(c.mixed.unpack_record(oldbundle[name]))for name in('inverse-stage1.json','inverse-stage3-basis.json','inverse-stage5-certificate.json')}
    B5=[decode(c,row)for row in old['inverse-stage3-basis.json']['basis']]
    assert [decode(c,row)for row in old['inverse-stage1.json']['exact_seeds']]==c.s.seeds
    assert len(B5)==120
    mixedbundle=json.loads((args.repo/'lab/process/source-action-mixed-consistency-certificates.json').read_text())
    raw=c.mixed.unpack_record(mixedbundle['records']['native-n6.json'])
    path=args.cache/'native-n6.json'
    if path.exists():assert path.read_bytes()==raw
    else:path.write_bytes(raw)
    B6,kappa=c.native.n6_basis(c,path)
    return B5,B6,old,kappa


def primary_data(c,args,B5,B6,old,kappa,ri,si,V):
    source={name:c.P(c.Kcov(cov,V))for name,cov in c.covectors.items()}
    a5=c.part(source['a'],5,5);assert a5==c.scale(2,c.s.seeds[si])
    a6=c.part(source['a'],6,5);b6=c.part(source['b'],6,6);cc6=c.part(source['c'],6,6)
    assert a6==c.scale(Q(1,6),c.Flower(b6))
    rr=old['inverse-stage5-certificate.json']['roots'][ri]
    assert rr['invertible_on_block_over_rootball'] and Q(rr['neumann_bound'])<1
    item=rr['sources'][si];assert item['index']==si
    co5=[2*c.C(*z)for z in item['coordinates']];er5=[2*Q(item['coefficient_error_inf'])for v in B5]
    out={'a5':{'coordinates':[z.ser()for z in co5],'coordinate_error':[str(e)for e in er5]},'n6':{}}
    values={'a5':linear(c,B5,co5)};errors={'a5':er5}
    for name,src in(('b6',b6),('c6',cc6)):
        assert not c.Eraise(src)and c.s.q['cas'](src)==c.scale(42,src)
        paired=[c.C(c.E.pair({k:c.C(z).conj()for k,z in n.items()},src))for n in B6]
        coeff=[c.C()for v in B6];err=[Q()for v in B6];used=[]
        official=kappa['exact_probe']['spin6']['constraint_inverse']['root_certificates'][ri]
        for block,cert in zip(kappa['spin6_inverse_candidates'][ri]['blocks'],official['blocks']):
            assert jd(block['rational_inverse'])==cert['rational_inverse_sha256']
            assert block['neumann_bound']==cert['neumann_bound'];eta=Q(cert['neumann_bound']);assert eta<1
            ids=block['indices']
            if not any(paired[j]for j in ids):continue
            co=[sum((c.C(*z)*paired[j]for z,j in zip(row,ids)),c.C())for row in block['rational_inverse']]
            er=eta/(1-eta)*max((n1(c,z)for z in co),default=Q())
            for j,z in zip(ids,co):coeff[j]=z;err[j]=er
            used.append({'indices':ids,'neumann_bound':str(eta),'coordinate_error':str(er)})
        values[name]=linear(c,B6,coeff);errors[name]=err
        out['n6'][name]={'paired_source':[[i,z.ser()]for i,z in enumerate(paired)if z],
            'coordinates':[z.ser()for z in coeff],'coordinate_error':[str(e)for e in err],'blocks':used}
    values['a6']=c.scale(Q(1,6),c.Flower(values['b6']))
    out['a6_from_b6_lowering_factor']='1/6'
    return values,errors,out


def stage_scout(args):
    tick=time.monotonic();c=setup(args);inputs=input_controls(c);reduce,E4=spin4_receiver(c,args)
    B5,B6,old,kappa=load_primaries(c,args)
    constants=json.loads((args.cache/'normal-constants.json').read_text())
    assert constants['complete'] and constants['bindings']['native_inputs']==bindings(args)['native_inputs']
    out={'scope':'Actual rational-center six-channel sources, with certified primary-response coordinate errors retained. Center noncoverage alone is not root-box noncoverage or obstruction.',
         'bindings':bindings(args),'constant_sha256':digest(args.cache/'normal-constants.json'),
         'native_n6_sha256':digest(args.cache/'native-n6.json'),'E4':E4,'roots':[]}
    for ri,root in enumerate(c.background['certified_roots']):
        T=c.add(*(c.scale(Q(x),v)for x,v in zip(root['coordinates'],c.Ts)))
        Ua=c.Ucov(c.covectors['a'],T);Uc=c.Ucov(c.covectors['c'],T)
        rr={'root':ri,'radius':root['certificate']['radius'],'sources':[]}
        for si,(index,V)in enumerate(zip((5,12),c.Vs)):
            start=time.monotonic();ys,ers,primary=primary_data(c,args,B5,B6,old,kappa,ri,si,V)
            print('NN primaries',ri,index,'terms',{k:len(v)for k,v in ys.items()},'seconds',time.monotonic()-start,flush=True)
            maps={}
            for name,U,y in(('a_a5',Ua,ys['a5']),('a_a6',Ua,ys['a6']),('a_c6',Ua,ys['c6']),('c_a5',Uc,ys['a5'])):
                maps[name]=c.P(c.integer.N(U,y))
                print('NN bilinear',ri,index,name,len(maps[name]),'seconds',time.monotonic()-start,flush=True)
            const=constants['sources'][si]['constants']
            d3,dab,dac=[decode(c,row['source'])for row in const]
            q3=c.add(d3,c.scale(-2,c.part(maps['a_a5'],3,3)))
            q4ab=c.add(dab,c.Eraise(c.part(c.add(maps['a_a5'],maps['a_a6']),4,3)))
            q4ac=c.add(dac,c.scale(-2,c.part(c.add(maps['a_c6'],maps['c_a5']),4,4)))
            rows=[]
            for label,j,v,parity in(('aa3',3,q3,1),('ab4',4,q4ab,1),('ac4',4,q4ac,0)):
                assert not c.K(3,v)and not c.Eraise(v)
                assert c.s.q['cas'](v)==c.scale(j*(j+1),v)
                assert c.s.rot(0,1,v)==c.scale(j*c.I,v)
                assert all(((e^cl)&13319).bit_count()%2==parity for e,cl in v)
                rem=reduce(v)if j==4 else None
                rows.append({'channel':label,'spin':j,'parity':parity,'terms':len(v),'source':ser(c,v),
                    'source_sha256':jd(ser(c,v)),'E4_remainder_terms':None if rem is None else len(rem),
                    'center_coefficient_l1_max':str(max((n1(c,z)for z in v.values()),default=Q())),
                    'center_remainder':None if rem is None else ser(c,rem)})
                print('NN actual center',ri,index,label,'terms',len(v),'E4 remainder',None if rem is None else len(rem),flush=True)
            rr['sources'].append({'Q_basis_index':index,'primary':primary,'channels':rows,'seconds':time.monotonic()-start})
            out['roots']=out['roots'][:ri]+[rr];out['seconds']=time.monotonic()-tick
            write(args.cache/'normal-scout.json',out)
        c.integer.clear_prepared()
    out['complete']=True;write(args.cache/'normal-scout.json',out)

def weights():
    g=(1,1,1,1,4,3,5,7,3,3,3,3,3,3);w=[1]*16384
    for m in range(1,16384):b=m&-m;w[m]=w[m^b]*g[b.bit_length()-1]
    return w

def weighted(c,v,w):return sum(w[cl]*n1(c,z)for(e,cl),z in v.items())

def stage_witnesses(args):
    tick=time.monotonic();c=setup(args);input_controls(c);B5,B6,old,kappa=load_primaries(c,args)
    data=json.loads((args.cache/'normal-scout.json').read_text());assert data['complete']
    assert data['bindings']['native_inputs']==bindings(args)['native_inputs']
    constants=json.loads((args.cache/'normal-constants.json').read_text());assert constants['complete']
    eb=json.loads((args.repo/'lab/process/source-action-spin4-certificates.json').read_text())
    E4=json.loads(c.mixed.unpack_record(eb['records']['inverse-stage3-basis.json']))
    support4={(e,cl)for row in E4['basis']for e,cl,z in row}
    w=weights();B6lower=[c.scale(Q(1,6),c.Flower(v))for v in B6]
    norms5=[weighted(c,v,w)for v in B5];norms6=[weighted(c,v,w)for v in B6];normsl=[weighted(c,v,w)for v in B6lower]
    sums={name:sum(weighted(c,c.Ucov(c.covectors[name],T),w)for T in c.Ts)for name in('a','c')}
    out={'scope':'Uniform actual-root nonzero source coordinates; spin4 coordinates annihilate the old E4 receiver. This is not a full-M or multiplier-augmented obstruction.',
        'bindings':bindings(args),'scout_sha256':digest(args.cache/'normal-scout.json'),
        'constants_sha256':digest(args.cache/'normal-constants.json'),'N_weighted_bound':'1098',
        'transformed_background_basis_weighted_norm_sums':{k:str(v)for k,v in sums.items()},'rows':[]}
    for rr in data['roots']:
        ri=rr['root'];root=c.background['certified_roots'][ri];radius=Q(root['certificate']['radius'])
        T=c.add(*(c.scale(Q(x),v)for x,v in zip(root['coordinates'],c.Ts)))
        U={name:c.Ucov(c.covectors[name],T)for name in('a','c')}
        for si,item in enumerate(rr['sources']):
            V=c.Vs[si];ys,ers,primary=primary_data(c,args,B5,B6,old,kappa,ri,si,V)
            assert primary==item['primary'];err5=sum(e*n for e,n in zip(ers['a5'],norms5))
            errb=sum(e*n for e,n in zip(ers['b6'],normsl));errc=sum(e*n for e,n in zip(ers['c6'],norms6))
            for ci,row in enumerate(item['channels']):
                start=time.monotonic();label=row['channel'];j=row['spin'];source=decode(c,row['source'])
                choices=[(k,z)for k,z in source.items()if j==3 or k not in support4];assert choices
                key,value=max(choices,key=lambda item:max(abs(c.C(item[1]).a),abs(c.C(item[1]).b)))
                component=0 if abs(value.a)>=abs(value.b)else 1;center=(value.a,value.b)[component]
                unit={key:c.C(1)/c.E.weight(*key)}
                # Bilinear native transpose: rotation generators are skew,
                # hence E^t=-E; P and the Casimir projector are self-adjoint.
                if label=='ab4':unit=c.scale(-1,c.Eraise(unit))
                h=c.P(c.part(unit,j,3 if label in('aa3','ab4')else 4))
                dual=max((n1(c,z)*abs(c.E.weight(*k))/w[k[1]]for k,z in h.items()),default=Q())
                rows={name:c.integer.N(U[name],h)for name in(('a','c')if label=='ac4'else('a',))}
                def pair(v,x):return c.C(c.E.pair(v,x))
                def er(v,basis,errors):return sum(e*n1(c,pair(v,b))for e,b in zip(errors,basis)if e)
                constant=decode(c,constants['sources'][si]['constants'][ci]['source']).get(key,c.C())
                if label=='aa3':
                    calculated=constant-2*pair(rows['a'],ys['a5'])
                    error_response=2*er(rows['a'],B5,ers['a5'])
                    error_background=2*1098*dual*radius*sums['a']*(weighted(c,ys['a5'],w)+err5)
                elif label=='ab4':
                    calculated=constant+pair(rows['a'],c.add(ys['a5'],ys['a6']))
                    error_response=er(rows['a'],B5,ers['a5'])+er(rows['a'],B6lower,ers['b6'])
                    error_background=1098*dual*radius*sums['a']*(weighted(c,c.add(ys['a5'],ys['a6']),w)+err5+errb)
                else:
                    calculated=constant-2*(pair(rows['a'],ys['c6'])+pair(rows['c'],ys['a5']))
                    error_response=2*(er(rows['a'],B6,ers['c6'])+er(rows['c'],B5,ers['a5']))
                    error_background=2*1098*dual*radius*(sums['a']*(weighted(c,ys['c6'],w)+errc)+sums['c']*(weighted(c,ys['a5'],w)+err5))
                assert calculated==value,(ri,si,label,'native adjoint/direct coordinate mismatch')
                error=error_response+error_background
                result={'root':ri,'Q_basis_index':item['Q_basis_index'],'channel':label,'spin':j,
                    'coordinate':list(key),'component':'real'if component==0 else'imag','center':str(center),
                    'primary_response_error':str(error_response),'background_error':str(error_background),'total_error':str(error),
                    'lower':str(center-error),'upper':str(center+error),'excludes_zero':abs(center)>error,
                    'annihilates_old_E4':j==4 and key not in support4,'native_adjoint_matches_direct':True,
                    'dual_weighted_norm':str(dual),'adjoint_test_terms':len(h),'seconds':time.monotonic()-start}
                out['rows'].append(result);out['seconds']=time.monotonic()-tick;write(args.cache/'normal-witnesses.json',out)
                print('NN witness',ri,item['Q_basis_index'],label,'center',float(center),'error',float(error),
                      'PASS',abs(center)>error,'seconds',result['seconds'],flush=True)
            c.integer.clear_prepared()
    out['complete']=len(out['rows'])==12;out['all_nonzero']=all(r['excludes_zero']for r in out['rows'])
    write(args.cache/'normal-witnesses.json',out)

def stage_numeric(args):
    """Bounded full-native numerical discovery, three actual root0/Q5 sources."""
    c=setup(args);data=json.loads((args.cache/'normal-scout.json').read_text());assert data['complete']
    assert data['bindings']['native_inputs']==bindings(args)['native_inputs']
    item=data['roots'][0]['sources'][0];assert item['Q_basis_index']==5
    seeds=[decode(c,row['source'])for row in item['channels']]
    for row,seed in zip(item['channels'],seeds):
        j=row['spin'];assert not c.K(3,seed)and not c.Eraise(seed)
        assert c.s.q['cas'](seed)==c.scale(j*(j+1),seed)
        assert jd(ser(c,seed))==row['source_sha256']
    original=c.w.build_seed_context
    def context(native_args,numeric=False):
        s=original(native_args,numeric);s.seeds=seeds;return s
    p=c.fast;p.w=c.w;p.g=c.g;p.C=c.C;p.I=c.I;p.add=c.add;p.scale=c.scale;p.context=context
    p.binding=lambda native_args:{'target':'actual_pure_normal_root0_Q5_three_channels_rational_center',
        'bindings':bindings(args),'scout_sha256':digest(args.cache/'normal-scout.json'),
        'channels':[{k:row[k]for k in('channel','spin','parity','source_sha256')}for row in item['channels']]}
    path=args.cache/'normal-numeric.json'
    native_args=SimpleNamespace(root=args.repo,cache=args.cache,output=path,
        root_index=0,source_index=None,steps=args.steps,prune=1e-13)
    p.stage_numeric(native_args)
    out=json.loads(path.read_text());out['scope']='NUMERICAL_DISCOVERY_ONLY full native ambient M matvec on all three actual pure-normal root0/Q5 rational-center channel sources. No exact-root solvability or negative conclusion.'
    write(path,out)

def carrier_setup(c,spin,parity):
    import source_action_even_spin5_probe as even
    class Carrier(even.EvenCarrier):
        def __init__(self,c):
            super().__init__(c);self.spin=spin;self.parity=parity
            metadata=[]
            for mask in range(1<<14):
                if mask.bit_count()%4 not in(0,3):continue
                weight=sum(self.weights[j]for j in range(14)if mask>>j&1)
                chi=sum(self.charges[j]for j in range(14)if mask>>j&1)%2
                metadata.append((mask,weight,chi))
            self.keys={m:[(j,mask)for mask,w,chi in metadata for j in range(14)
                       if w+self.weights[j]==m and (chi+self.charges[j])%2==parity]for m in(spin,spin+1)}
            self.lookup={m:{key:i for i,key in enumerate(keys)}for m,keys in self.keys.items()}
        def coordinates(self,v,weight=None):
            if weight is None:weight=self.spin
            out={};C=self.c.C
            for(e,cl),x in v.items():
                assert e.bit_count()==1 and cl.bit_count()%4 in(0,3)
                assert ((e^cl)&13319).bit_count()%2==self.parity
                for ei,y in self.inverse_atoms[e.bit_length()-1].items():
                    j=ei.bit_length()-1
                    for mask,z in self.cliff_inverse(cl).items():
                        key=j,mask;out[key]=out.get(key,C())+x*y*z
            out={k:z for k,z in out.items()if z};assert set(out)<=set(self.lookup[weight])
            return {self.lookup[weight][k]:z for k,z in out.items()}
        def weight_basis(self):return [self.native(key)for key in self.keys[self.spin]]
    return even,Carrier(c)


def carrier_binding(args):
    return {'native_inputs':bindings(args)['native_inputs'],
        'constructor_sha256':hashlib.sha256('\n'.join(inspect.getsource(f)for f in(setup,carrier_setup,carrier_binding,stage_carrier)).encode()).hexdigest()}


def stage_carrier(args):
    """Complete spin/parity carriers, independent of all numerical supports."""
    c=setup(args);start=time.monotonic();metadata=carrier_binding(args)
    types={'even4':(4,0,1984,664,1320),'odd4':(4,1,1968,684,1284),'odd3':(3,1,4276,1968,2308)}
    selected=types if args.carrier=='all'else{args.carrier:types[args.carrier]}
    for label,(spin,parity,w0,w1,highest)in selected.items():
        tick=time.monotonic();even,car=carrier_setup(c,spin,parity)
        assert (len(car.keys[spin]),len(car.keys[spin+1]))==(w0,w1)
        W=car.weight_basis();hp=args.cache/(label+'-highest.json');kp=args.cache/(label+'-kernel.json')
        if hp.exists():
            high=json.loads(hp.read_text());assert high['bindings']==metadata and high['complete']
            assert high['weight_keys']==[list(k)for k in car.keys[spin]]
        else:
            columns=[]
            for i,v in enumerate(W):
                assert car.coordinates(v)=={i:c.C(1)}
                columns.append(car.coordinates(c.Eraise(v),spin+1))
                if (i+1)%128==0:print('NN complete weight/raising',label,i+1,'/',w0,'seconds',time.monotonic()-tick,flush=True)
            rows,ker=even.sparse_kernel(c,columns);assert len(rows)==w1 and len(ker)==highest
            high={'bindings':metadata,'complete':True,'spin':spin,'parity':parity,'weight_dimension':w0,'next_weight_dimension':w1,
                  'highest_dimension':highest,'weight_keys':[list(k)for k in car.keys[spin]],
                  'raising_columns':[even.coordinates_serial(v)for v in columns],
                  'highest_coordinates':[even.coordinates_serial(v)for v in ker],
                  'execution_probe_sha256':digest(__file__),'seconds':time.monotonic()-tick}
            write(hp,high)
        H=[even.combine(c,{i:c.C(*z)for i,z in row},W)for row in high['highest_coordinates']]
        live=metadata|{'highest_sha256':digest(hp)}
        data={'bindings':live,'completed':0,'columns':[]}
        if kp.exists():
            data=json.loads(kp.read_text());assert data['bindings']==live and data['completed']==len(data['columns'])
        for i in range(data['completed'],highest):
            co=car.coordinates(c.K(3,H[i]));data['columns'].append(even.coordinates_serial(co));data['completed']=i+1
            if(i+1)%32==0 or i+1==highest:
                data['seconds']=time.monotonic()-tick;write(kp,data)
                print('NN complete Kt',label,i+1,'/',highest,'seconds',data['seconds'],flush=True)
        cols=[{i:c.C(*z)for i,z in row}for row in data['columns']]
        rows,ker=even.sparse_kernel(c,cols)
        fields=[even.combine(c,co,H)for co in ker]
        native_rows,dependence=even.sparse_kernel(c,fields);assert not dependence
        basis=[row for row,co in native_rows];pivots=[min(v)for v in basis]
        for v in basis:
            assert not c.K(3,v)and not c.Eraise(v)
            assert c.s.rot(0,1,v)==c.scale(spin*c.I,v)
            assert c.s.q['cas'](v)==c.scale(spin*(spin+1),v)
            assert all(((e^cl)&13319).bit_count()%2==parity for e,cl in v)
        sources=[];scout=json.loads((args.cache/'normal-scout.json').read_text())
        channel={'even4':'ac4','odd4':'ab4','odd3':'aa3'}[label]
        for rr in scout['roots']:
            for item in rr['sources']:
                row=next(r for r in item['channels']if r['channel']==channel)
                rem,co=even.reduce_field(c,decode(c,row['source']),basis,pivots);assert not rem
                sources.append({'root':rr['root'],'Q_basis_index':item['Q_basis_index'],'source_sha256':row['source_sha256'],
                                'coordinates':[z.ser()for z in co]})
        out={'scope':'Complete native time-kernel in the specified spin/parity highest carrier. No M invertibility claim.',
             'bindings':live|{'kernel_columns_sha256':digest(kp)},'execution_probe_sha256':digest(__file__),
             'complete':True,'spin':spin,'parity':parity,'ambient_highest_dimension':highest,'time_rank':len(rows),
             'dimension':len(basis),'basis':[ser(c,v)for v in basis],'basis_pivots':[list(k)for k in pivots],
             'exact_center_source_membership':sources,'seconds':time.monotonic()-tick}
        write(args.cache/(label+'-basis.json'),out)
        print('NN COMPLETE CARRIER',label,'dimension',len(basis),'time rank',len(rows),'seconds',out['seconds'],flush=True)
    print('NN carriers finished seconds',time.monotonic()-start,flush=True)

def load_block(c,args,label):
    import source_action_even_spin5_probe as even
    path=args.cache/(label+'-basis.json');data=json.loads(path.read_text())
    assert data['complete']and data['bindings']['constructor_sha256']==carrier_binding(args)['constructor_sha256']
    assert data['bindings']['native_inputs']==bindings(args)['native_inputs']
    basis=[decode(c,row)for row in data['basis']];pivots=[tuple(k)for k in data['basis_pivots']]
    meta={'basis_sha256':digest(path),'complete_dimension':len(basis),'retained_indices':list(range(len(basis)))}
    if label=='even4':
        bundle=json.loads((args.repo/'lab/process/source-action-spin4-certificates.json').read_text())
        bd=json.loads(c.mixed.unpack_record(bundle['records']['inverse-stage3-basis.json']))
        cert=json.loads(c.mixed.unpack_record(bundle['records']['spin4-fast-certificate.json']))
        assert len(cert['roots'])==2 and all(r['invertible_on_block_over_rootball']and Q(r['neumann_bound'])<1 for r in cert['roots'])
        old=[decode(c,row)for row in bd['basis']];support=set().union(*(set(v)for v in old))
        inside=[i for i,v in enumerate(basis)if set(v)<=support]
        outside=[i for i,v in enumerate(basis)if not(set(v)&support)]
        assert len(inside)==len(old)==282 and len(outside)==286 and sorted(inside+outside)==list(range(568))
        known=[basis[i]for i in inside];kp=[pivots[i]for i in inside]
        assert all(not even.reduce_field(c,v,known,kp)[0]for v in old)
        q,qd,qi=even.paired_rows(c,old);gram=[]
        for v in old:
            den,vi=c.integer.clear_denominators(v);col=even.paired_integer(c,qi,282,vi,den,qd)
            gram.append({i:z for i,z in enumerate(col)if z})
        rows,kernel=even.sparse_kernel(c,gram);assert len(rows)==282 and not kernel
        meta.update({'retained_indices':outside,'owned_E4_dimension':282,'exact_old_span_identification':True,
            'native_Gram_rank_E4':282,'orthogonality_by_disjoint_support':True,
            'old_basis_sha256':bundle['records']['inverse-stage3-basis.json']['sha256'],
            'old_certificate_sha256':bundle['records']['spin4-fast-certificate.json']['sha256']})
        basis=[basis[i]for i in outside];pivots=[pivots[i]for i in outside]
    phases=[];gauged=[];signs=[]
    for v in basis:
        kv={k:z.conj()*((-1)**(((k[0]^k[1])&11525).bit_count()%2))for k,z in v.items()}
        epsilon=kv[min(v)]/v[min(v)];assert epsilon in(c.C(1),c.C(-1))
        assert kv==c.scale(epsilon,v)
        phase=c.C(1)if epsilon==1 else c.I
        phases.append(phase);signs.append(int(epsilon.a));gauged.append(c.scale(phase,v))
    meta.update({'kappa_mask':11525,'kappa_original_signs':signs,'column_phases':[z.ser()for z in phases],
                 'phase_aligned_kappa_sign':1,'dimension':len(basis)})
    return even,data,basis,pivots,gauged,meta


def matrix_binding(args,label,metadata):
    return {'native_inputs':bindings(args)['native_inputs'],'block':metadata,
        'assembly_procedure_sha256':hashlib.sha256('\n'.join(inspect.getsource(f)for f in(load_block,matrix_binding,stage_matrix)).encode()).hexdigest()}


def stage_matrix(args):
    c=setup(args);labels=('even4','odd4','odd3')if args.carrier=='all'else(args.carrier,)
    for label in labels:
        even,bd,basis,pivots,Z,meta=load_block(c,args,label);n=len(Z);E=c.integer
        q,qd,qi=even.paired_rows(c,Z);path=args.cache/(label+'-matrices.json');live=matrix_binding(args,label,meta)
        out={'scope':'Exact paired H=Z†J C Z on complete native block (even4: exact E4 orthogonal complement), with checked κ column phase gauge.',
             'bindings':live,'execution_probe_sha256':digest(__file__),'dimension':n,'roots':[]}
        if path.exists():out=json.loads(path.read_text());assert out['bindings']==live
        for ri,owned in enumerate(c.background['certified_roots']):
            if args.root_index is not None and ri!=args.root_index:continue
            found=[r for r in out['roots']if r['root']==ri];assert len(found)<=1
            if found:r=found[0]
            else:
                r={'root':ri,'root_record_sha256':jd(owned),'completed':0,'columns':[],'image_controls':[]};out['roots'].append(r)
            assert r['completed']==len(r['columns'])
            T=c.add(*(c.scale(Q(x),v)for x,v in zip(owned['coordinates'],c.Ts)))
            du,ui,au=E.prepare(T);start=time.monotonic();begin=r['completed'];end=n if args.steps==0 else min(n,begin+args.steps)
            for j in range(begin,end):
                tick=time.monotonic();dv,vi,av=E.prepare(Z[j])
                numerator=E.Phi_scaled(E.wedge_comm_int(ui,vi))
                c.fast.add_into(numerator,E.wadj_scaled(ui,av));c.fast.add_into(numerator,E.wadj_scaled(vi,au))
                denominator=3*E.Dphi*du*dv;c.fast.add_into(numerator,vi,3*E.Dphi*du);numerator=c.fast.prune(numerator)
                assert all(e.bit_count()==1 and cl.bit_count()%4 in(0,3)and ((e^cl)&13319).bit_count()%2==bd['parity']for e,cl in numerator)
                column=even.paired_integer(c,qi,n,numerator,denominator,qd)
                assert all(not z.b for z in column),'κ-aligned H must be real; never discard an imaginary entry'
                if j==0:
                    raw=E.restore(numerator,denominator);projected=c.P(raw)
                    rem,co=even.reduce_field(c,projected,basis,pivots);assert not rem
                    assert not c.K(3,projected)and not c.Eraise(projected)
                    assert all(column[i]==c.E.pair({k:z.conj()for k,z in Z[i].items()},raw)for i in range(n))
                    r['first_column_full_native_range_pairing_control']=True
                r['columns'].append([[i,z.ser()]for i,z in enumerate(column)if z]);r['completed']=j+1
                r['image_controls'].append({'column':j,'complete_native_C_image_terms':len(numerator),
                    'integer_denominator':str(denominator),'integer_image_sha256':jd([[e,cl,str(a),str(b)]for(e,cl),(a,b)in sorted(numerator.items())]),
                    'seconds':time.monotonic()-tick})
                if(j+1)%8==0 or j+1==end:
                    r['last_batch_seconds']=time.monotonic()-start;write(path,out)
                    print('NN paired-H',label,ri,j+1,'/',n,'seconds',r['last_batch_seconds'],flush=True)
            if r['completed']==n:
                cols=[{i:c.C(*z)for i,z in row}for row in r['columns']]
                assert all(cols[j].get(i,c.C())==cols[i].get(j,c.C())for i in range(n)for j in range(n))
                r['hermitian']=True;r['real_symmetric']=True;r['complete']=True;write(path,out)
        out['complete']=len(out['roots'])==2 and all(r.get('complete')for r in out['roots']);write(path,out)
        E.clear_prepared()

def real_product(A,B,backend):
    """Exact integer product; optional FLINT is only an arithmetic accelerator."""
    if backend in('auto','flint'):
        try:
            import flint
        except ImportError:
            if backend=='flint':raise
        else:
            flint.ctx.threads=1
            aa=flint.fmpz_mat([[int(x)for x in row]for row in A])
            bb=flint.fmpz_mat([[int(x)for x in row]for row in B]);p=aa*bb
            return [[int(p[i,j])for j in range(p.ncols())]for i in range(p.nrows())],{'backend':'python-flint','version':flint.__version__,'threads':1}
    p=A@B
    return [[int(x)for x in row]for row in p],{'backend':'numpy-object Python integers','threads':1}


def real_defect(H,DH,R,DR,backend):
    product,meta=real_product(R,H,backend);n=len(product);den=DH*DR
    numerator=max(sum(abs((den if i==j else 0)-product[i][j])for i in range(n))for j in range(n))
    return Q(numerator,den),meta


def arithmetic_controls(backend):
    import numpy as np
    A=np.array([[11,-7,3],[9,2,-5]],dtype=object);B=np.array([[5,-2],[7,13],[-4,8]],dtype=object)
    got,meta=real_product(A,B,backend)
    expected=[[sum(int(A[i,k])*int(B[k,j])for k in range(3))for j in range(2)]for i in range(2)]
    assert got==expected
    H=np.array([[3,1],[1,4]],dtype=object);R=np.array([[2,-3],[5,1]],dtype=object)
    actual,_=real_defect(H,1,R,7,backend)
    literal=[[Q(i==j)-sum(Q(int(R[i,k]))*Q(int(H[k,j]))for k in range(2))/7 for j in range(2)]for i in range(2)]
    assert actual==max(sum(abs(literal[i][j])for i in range(2))for j in range(2))
    assert actual!=max(sum(abs(z)for z in row)for row in literal)
    return meta|{'integer_rectangular_product_control':True,'rational_column_defect_control':True}


def real_candidate(args,label,H,denominator,binding):
    import numpy as np
    n=H.shape[0];path=args.cache/(label+'-inverse-candidates.json')
    if path.exists():data=json.loads(path.read_text());assert data['format']=='gu-normal-normal-real-balanced-inverse-v1'
    else:data={'format':'gu-normal-normal-real-balanced-inverse-v1','scope':'Frozen rational candidate only; exact defect and root-box perturbation decide invertibility.','roots':[]}
    found=[row for row in data['roots']if row['root']==binding['root']];assert len(found)<=1
    if found:row=found[0];assert row['bindings']==binding
    else:
        assert args.generate_candidates,'Explicit --generate-candidates required; replay never regenerates floating inverses'
        adjacency=[{j for j,v in enumerate(line)if int(v)and j!=i}for i,line in enumerate(H)]
        pending=set(range(n));components=[]
        while pending:
            stack=[min(pending)];component=set()
            while stack:
                i=stack.pop()
                if i in component:continue
                component.add(i);stack.extend(adjacency[i]-component)
            pending-=component;components.append(sorted(component))
        assert sorted(i for block in components for i in block)==list(range(n))
        den=10**args.precision;values=[[0]*n for _ in range(n)]
        for block in components:
            h=np.array([[float(Q(int(H[i,j]),denominator))for j in block]for i in block],dtype=np.float64)
            inverse=np.linalg.inv(h);assert np.isfinite(inverse).all()
            for ii,i in enumerate(block):
                for jj,j in enumerate(block):values[i][j]=int(round(Q(str(float(inverse[ii,jj])))*den))
        row={'root':binding['root'],'bindings':binding,'dimension':n,'denominator':str(den),
             'center_component_indices':components,'center_component_sizes':[len(v)for v in components],
             'real_numerators':[[str(v)for v in line]for line in values]}
        data['roots'].append(row);data['roots'].sort(key=lambda r:r['root']);write(path,data)
    assert row['dimension']==n and len(row['real_numerators'])==n and all(len(r)==n for r in row['real_numerators'])
    assert all(type(v)is str and v.lstrip('+-').isdigit()for r in row['real_numerators']for v in r)
    den=int(row['denominator']);assert den>0
    return np.array([[int(v)for v in r]for r in row['real_numerators']],dtype=object),den


def stage_certify(args):
    import numpy as np
    tick=time.monotonic();c=setup(args);controls=arithmetic_controls(args.backend)
    labels=('even4','odd4','odd3')if args.carrier=='all'else(args.carrier,)
    for label in labels:
        even,bd,basis,pivots,Z,meta=load_block(c,args,label);n=len(Z)
        path=args.cache/(label+'-matrices.json');matrix=json.loads(path.read_text())
        assert matrix['bindings']==matrix_binding(args,label,meta)and matrix['complete']and matrix['dimension']==n
        assert sorted(r['root']for r in matrix['roots'])==[0,1]
        w,exactD,norm=even.norm_constants(c,Z)
        # Dyadic majorants preserve ||W Z D^-1||_1<=1. Their common multiple
        # is just the largest weight, avoiding an LCM of unrelated integers.
        D=[Q(1<<(((d.numerator+d.denominator-1)//d.denominator)-1).bit_length())for d in exactD]
        assert all(a>=b>0 for a,b in zip(D,exactD))
        funcs=(load_block,real_product,real_defect,arithmetic_controls,real_candidate,stage_certify)
        binding={'native_inputs':bindings(args)['native_inputs'],'matrix_sha256':digest(path),'block':meta,
            'certificate_procedure_sha256':hashlib.sha256('\n'.join(inspect.getsource(f)for f in funcs).encode()).hexdigest()}
        out={'scope':'Exact test of uniform both-root native M invertibility on the complete specified carrier; even4 joins its certified E4 complement to the owned E4 inverse. No propagation/physical-domain necessity claim.',
             'bindings':binding,'execution_probe_sha256':digest(__file__),'dimension':n,'complete_carrier_dimension':bd['dimension'],
             'norm_constants':norm,'integer_basis_norm_majorants':[str(d)for d in D],'arithmetic_controls':controls,'roots':[]}
        for ri,owned in enumerate(c.background['certified_roots']):
            record=next(r for r in matrix['roots']if r['root']==ri)
            assert record['complete']and record['real_symmetric']and record['first_column_full_native_range_pairing_control']
            assert record['root_record_sha256']==jd(owned)
            Hr,Hi,DH=even.dense_paired_matrix(c,record,n);assert not any(int(z)for row in Hi for z in row)
            Hs,zero,DHs,L=even.balanced_matrix(Hr,Hi,DH,D);assert not any(int(z)for row in zero for z in row)
            cb=binding|{'root':ri,'root_record_sha256':jd(owned),'balanced_integer_denominator':str(DHs),
                        'integer_basis_norm_majorants':[str(d)for d in D]}
            R,DR=real_candidate(args,label,Hs,DHs,cb)
            eta0,backend=real_defect(Hs,DHs,R,DR,args.backend)
            Ctri=even.triangle_bound(c,Z,D,w,R,np.zeros((n,n),dtype=object),DR)
            radius=Q(owned['certificate']['radius']);delta=2196*radius*Q(128637452,3)*Ctri;eta=eta0+delta
            row={'root':ri,'root_record_sha256':jd(owned),'radius':str(radius),'balanced_center_defect_column1':str(eta0),
                 'Ctriangle_upper':str(Ctri),'rootbox_perturbation_column1':str(delta),'neumann_bound':str(eta),
                 'neumann_bound_float':float(eta),'native_M_invertible_on_complete_block':eta<1,'arithmetic_backend':backend}
            out['roots'].append(row);out['seconds']=time.monotonic()-tick
            out['preconditioner_sha256']=digest(args.cache/(label+'-inverse-candidates.json'))
            out['both_root_boxes_invertible']=len(out['roots'])==2 and all(r['native_M_invertible_on_complete_block']for r in out['roots'])
            write(args.cache/(label+'-certificate.json'),out)
            print('NN CERTIFICATE',label,ri,'eta0',float(eta0),'delta',float(delta),'total',float(eta),'PASS',eta<1,flush=True)

def rational_rank(matrix):
    a=[[Q(v)for v in row]for row in matrix];rank=0
    if not a:return 0
    for col in range(len(a[0])):
        pivot=next((i for i in range(rank,len(a))if a[i][col]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank];z=a[rank][col];a[rank]=[x/z for x in a[rank]]
        for i in range(rank+1,len(a)):
            if a[i][col]:
                z=a[i][col];a[i]=[x-z*y for x,y in zip(a[i],a[rank])]
        rank+=1
        if rank==len(a):break
    return rank


def character_controls(c,args):
    from math import comb
    from collections import Counter
    path=args.cache/'normal-time-kernel-character.json';data=json.loads(path.read_text())
    owned_path=args.repo/'lab/process/source-action-coupled-ghost.json';owned=json.loads(owned_path.read_text())
    assert digest(owned_path)==data['owned_principal_artifact_sha256']
    principal=owned['principal'];total=0;rows=[];trans=[i for i in range(14)if i!=3]
    assert len(data['principal_blocks'])==14
    for block,reference in zip(data['principal_blocks'],principal['blocks']):
        degree=block['transverse_degree'];assert degree==reference['transverse_degree']==len(rows)
        assert jd(block['matrix'])==reference['matrix_sha256']==block['owned_matrix_sha256']
        rho=sum(1<<i for i in trans[:degree]);basis=[(1<<i,(1<<i)^rho^z)for z in(0,8)for i in range(14)]
        assert block['basis']==[list(k)for k in basis]
        A=[[Q(z)for z in row]for row in block['matrix']];assert len(A)==28 and all(len(row)==28 for row in A)
        for j,key in enumerate(basis):
            image=c.K(3,{key:c.C(1)})
            assert set(image)<=set(basis)
            assert all(c.C(image.get(k,0))==c.C(A[i][j])for i,k in enumerate(basis))
        ids=[i for i,(e,cl)in enumerate(basis)if cl.bit_count()%4 in(0,3)]
        assert all(not A[i][j]for i in ids for j in range(28)if j not in ids)
        rank=rational_rank([[A[i][j]for j in ids]for i in ids]);nullity=len(ids)-rank;mult=comb(13,degree)
        assert block['multiplicity']==reference['multiplicity']==mult
        total+=mult*nullity;rows.append({'transverse_degree':degree,'imaginary_dimension':len(ids),'imaginary_rank':rank,'imaginary_nullity':nullity,'multiplicity':mult})
    assert total==49154==principal['phase_dimensions_rank_kernel']['1'][2]==data['kernel_dimension']
    # Reconstruct the actual even/odd Clifford-grade irreducible table.
    copies=Counter()
    for grade in(0,3,4,7,8,11,12):
        parity=grade%2
        for degree in(grade,grade-1):
            if not 0<=degree<=13:continue
            k=min(degree,13-degree);copies[parity,'L'+str(k)]+=1
            if k==0:copies[parity,'L1']+=1
            else:
                copies[parity,'L'+str(k-1)]+=1;copies[parity,'L'+str(min(k+1,12-k))]+=1
                copies[parity,'H'+str(k)]+=1
    lower=0
    for row in data['irreducible_multiplicity_table']:
        name=row['irrep'];k=int(name[1:]);dimension=comb(13,k)if name[0]=='L'else 13*comb(13,k)-comb(13,k-1)-comb(13,k+1)
        even,odd=copies[0,name],copies[1,name];bound=abs(even-odd)
        assert (dimension,even,odd,bound)==(row['dimension'],row['even_clifford_multiplicity'],row['odd_clifford_multiplicity'],row['kernel_lower_bound_copies'])
        lower+=dimension*bound
    assert lower==total==data['kernel_lower_bound']
    atoms=[tuple(v)for v in data['transverse_weight_chi_atoms']]
    expected=Counter([(m,1)for m in(-1,0,1)for _ in range(2)]+[(m,0)for m in(-2,-1,0,1,2)]+[(0,0),(0,0)])
    assert Counter(atoms)==expected
    exterior=Counter({(0,0,0):1})
    for weight,chi in atoms:
        old=dict(exterior)
        for(k,m,p),n in old.items():exterior[k+1,m+weight,p^chi]+=n
    S=Counter()
    for(k,m,p),n in exterior.items():
        if k<=6:S[m,p]+=n
    character=Counter()
    for(m,p),n in S.items():
        character[m,p]-=n
        for weight,chi in atoms:character[m+weight,p^chi]+=n
    character[0,0]+=2
    multiplicities={name:{str(j):character[j,p]-character[j+1,p]for j in range(8)}for p,name in enumerate(('even','odd'))}
    assert multiplicities==data['highest_multiplicities']
    assert sum((2*j+1)*multiplicities[name][str(j)]for name in multiplicities for j in range(8))==total
    spinor=data['spinorial_corollary'];assert spinor['spinor_dimension']==64 and spinor['gamma_traceless_vector_spinor_dimension']==768
    assert (13-1)*64*64+2==spinor['dimension_check']==total
    return {'data_sha256':digest(path),'owned_principal_artifact_sha256':digest(owned_path),
            'native_K_columns_recomputed':392,'exact_imaginary_rank_rows':rows,'kernel_dimension':total,
            'irreducible_lower_bound_recomputed':lower,'highest_multiplicities':multiplicities,
            'abstract_RS_dimension_check':True,'M_factorization_or_regularity_inferred':False}

def producer_custody(args):
    """Reconstruct historical producer bytes; do not relabel old execution hashes."""
    source=Path(__file__).read_text()
    def old_tail(level):
        out="def main():\n    ap=argparse.ArgumentParser(description=__doc__)\n    ap.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2]);ap.add_argument('--cache',type=Path,required=True)\n"
        if level>=4:out+="    ap.add_argument('--carrier',choices=('all','even4','odd4','odd3'),default='all')\n"
        if level>=5:out+="    ap.add_argument('--root-index',type=int,choices=(0,1))\n"
        if level>=3:out+="    ap.add_argument('--steps',type=int,default=30)\n"
        choices=["('constants',)","('constants','scout')","('constants','scout','witnesses')","('constants','scout','witnesses','numeric')","('constants','scout','witnesses','numeric','carrier')","('constants','scout','witnesses','numeric','carrier','matrix')"][level]
        out+="    ap.add_argument('--mode',choices="+choices+",required=True)\n    args=ap.parse_args();args.repo=args.repo.resolve();args.cache.mkdir(parents=True,exist_ok=True)\n    globals()['stage_'+args.mode](args)\n\n\nif __name__=='__main__':main()\n"
        return out
    specs=[('normal-constants.json','def decode(c,row)',0,3),('normal-scout.json','def weights()',1,2),
           ('normal-witnesses.json','def stage_numeric(args)',2,2),('normal-numeric.json','def carrier_setup(c,spin,parity)',3,2)]
    specs += [(label+'-basis.json','def load_block(c,args,label)',4,2)for label in('even4','odd4','odd3')]
    specs += [(label+'-matrices.json','def real_product(A,B,backend)',5,2)for label in('even4','odd4','odd3')]
    results=[]
    for name,cut,level,newlines in specs:
        value=json.loads((args.cache/name).read_text())
        if name=='normal-numeric.json':expected=value['bindings']['bindings']['probe_sha256']
        elif name.startswith('normal-'):expected=value['bindings']['probe_sha256']
        else:expected=value['execution_probe_sha256']
        if expected==digest(__file__):
            got=expected
        else:
            prefix=source[:source.index(cut)].rstrip('\n');rebuilt=prefix+'\n'*newlines+old_tail(level)
            got=hashlib.sha256(rebuilt.encode()).hexdigest()
        assert got==expected,('Historical producer reconstruction failed',name,got,expected)
        results.append({'record':name,'execution_probe_sha256':expected,'reconstructed_sha256':got,
                        'unchanged_prefix_ends_before':cut,'historical_cli_level':level,'passed':True})
    return results


def stage_controls(args):
    tick=time.monotonic();c=setup(args);input_checks=input_controls(c);custody=producer_custody(args);character=character_controls(c,args)
    rotation=(-1,1,-1,1);tangent_signs=list(rotation)
    for A in c.g.A:
        moved=[[rotation[i]*A[i][j]*rotation[j]for j in range(4)]for i in range(4)]
        signs=[sign for sign in(1,-1)if moved==[[sign*z for z in row]for row in A]]
        assert len(signs)==1;tangent_signs.append(signs[0])
    assert sum(1<<i for i,sign in enumerate(tangent_signs)if sign<0)==11525
    for V in c.Vs:
        for name,cov in c.covectors.items():
            lhs=c.add(c.Ucov(cov,c.K(3,V)),c.scale(-1,c.K(3,c.Ucov(cov,V))))
            assert lhs==c.Kcov(cov,V)
    for T in c.Ts:
        assert all(((e^cl)&13319).bit_count()%2==0 for e,cl in T)
        assert all(not c.s.rot(i,j,T)for i,j in((0,1),(0,2),(1,2)))
    results=[]
    for label in('even4','odd4','odd3'):
        even,bd,basis,pivots,Z,meta=load_block(c,args,label)
        matrices=json.loads((args.cache/(label+'-matrices.json')).read_text())
        assert matrices['complete']and matrices['bindings']==matrix_binding(args,label,meta)
        q,qd,qi=even.paired_rows(c,Z)
        for rr in matrices['roots']:
            ri=rr['root'];root=c.background['certified_roots'][ri]
            T=c.add(*(c.scale(Q(x),v)for x,v in zip(root['coordinates'],c.Ts)))
            raw=c.add(Z[0],c.scale(2,c.E.N(T,Z[0])))
            record=rr['image_controls'][0];den=int(record['integer_denominator']);ints=[]
            for(e,cl),z in sorted(raw.items()):
                a,b=z.a*den,z.b*den;assert a.denominator==b.denominator==1
                ints.append([e,cl,str(int(a)),str(int(b))])
            assert jd(ints)==record['integer_image_sha256']
            dv,vi=c.integer.clear_denominators(raw);column=even.paired_integer(c,qi,len(Z),vi,dv,qd)
            assert [[i,z.ser()]for i,z in enumerate(column)if z]==rr['columns'][0]
            assert all(not z.b for z in column)
            results.append({'block':label,'root':ri,'column':0,'full_original_Euler_image_matches_integer_image':True,
                            'all_paired_entries_match':True,'phase_aligned_real':True,'native_image_terms':len(raw)})
        for suffix,field in(('highest','raising_columns'),('highest','highest_coordinates'),('kernel','columns')):
            record=json.loads((args.cache/(label+'-'+suffix+'.json')).read_text())
            assert all(not c.C(*z).b for row in record[field]for i,z in row)
    dependencies=bindings(args)['native_inputs']|c.w.native_bindings(args.repo)
    for name in('tests/program-focus/source_action_reduced_evolution_probe.py','lab/process/source-action-mixed-consistency-certificates.json','lab/process/source-action-coupled-ghost.json','tests/program-focus/source_action_coupled_ghost_probe.py'):
        dependencies[name]=digest(args.repo/name)
    certificates={label:json.loads((args.cache/(label+'-certificate.json')).read_text())for label in('even4','odd4','odd3')}
    assert all(v['both_root_boxes_invertible']for v in certificates.values())
    out={'scope':'Native no-G representative normalization, complete-carrier real coordinate controls, original-Euler first-column controls at both roots, and exact producer custody. This is not propagation or physical-domain necessity.',
         'execution_probe_sha256':digest(__file__),'dependencies':dependencies,'input_controls':input_checks,
         'native_kappa_rotation_mask':11525,'ambient_U_Ktau_commutator_checks':6,'all_59_backgrounds_rotation_fixed_and_even':True,
         'producer_custody':custody,'complete_time_kernel_character':character,'matrix_controls':results,'all_complete_certificates_pass':True,
         'seconds':time.monotonic()-tick,'complete':True}
    write(args.cache/'normal-controls.json',out)
    print('NN controls PASS seconds',out['seconds'],flush=True)


BASE_RECORDS=('native-n6.json','normal-constants.json','normal-scout.json','normal-witnesses.json','normal-numeric.json','normal-time-kernel-character.json','normal-controls.json')
NORMAL_RECORDS=BASE_RECORDS+tuple(label+'-'+suffix+'.json'for label in('even4','odd4','odd3')for suffix in('highest','kernel','basis','matrices','inverse-candidates','certificate'))
NORMAL_BUNDLE='source-action-normal-normal-certificates.json'


def stage_bundle(args):
    import base64,zlib
    controls=json.loads((args.cache/'normal-controls.json').read_text())
    assert controls['complete']and controls['execution_probe_sha256']==digest(__file__)
    producer_custody(args);records={}
    for name in NORMAL_RECORDS:
        raw=(args.cache/name).read_bytes();json.loads(raw)
        records[name]={'encoding':'zlib-base64-json','uncompressed_bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
                       'data':base64.b64encode(zlib.compress(raw,9)).decode()}
    out={'schema':'gu-native-normal-normal-consistency-v1','data_only':True,
         'scope':'Complete native lower-block range certificates for all six chosen no-G normal-normal first-consistency representatives; no propagation or GU falsification claim.',
         'final_probe_sha256':digest(__file__),'records':records}
    path=args.output or args.repo/'lab/process'/NORMAL_BUNDLE;write(path,out)
    assert path.stat().st_size<100_000_000,('Bundle exceeds single-file publication limit',path.stat().st_size)
    print('NN bundle',path,'bytes',path.stat().st_size,'records',len(records),flush=True)


def stage_unpack(args):
    path=args.bundle or args.repo/'lab/process'/NORMAL_BUNDLE;bundle=json.loads(path.read_text())
    assert bundle['schema']=='gu-native-normal-normal-consistency-v1'and bundle['data_only']
    assert bundle['final_probe_sha256']==digest(__file__)and set(bundle['records'])==set(NORMAL_RECORDS)
    import source_action_mixed_consistency_probe as mixed
    for name in NORMAL_RECORDS:(args.cache/name).write_bytes(mixed.unpack_record(bundle['records'][name]))
    print('NN unpacked',len(NORMAL_RECORDS),'records into',args.cache,flush=True)


def stage_status(args):
    rows=[]
    for label in('even4','odd4','odd3'):
        p=args.cache/(label+'-certificate.json')
        if p.exists():
            d=json.loads(p.read_text());rows.append({'block':label,'dimension':d['dimension'],'complete_carrier_dimension':d['complete_carrier_dimension'],
                'both_root_boxes_invertible':d['both_root_boxes_invertible'],'root_neumann_bounds':[r['neumann_bound_float']for r in d['roots']]})
    out={'probe_sha256':digest(__file__),'blocks':rows,'scope':'First-consistency range only; no propagation or physical-domain necessity claim.'}
    if args.output:write(args.output,out)
    print(json.dumps(out,indent=2),flush=True)

def same_fields(a,b,keys,label):
    for key in keys:assert a[key]==b[key],('Reproduction mismatch',label,key)


def stage_replay(args):
    """Full carrier reconstruction, six native H-column controls, exact frozen-R arithmetic.

    Remaining H columns are authenticated; no fresh floating inverse is generated.
    """
    tick=time.monotonic();bundlepath=args.bundle or args.repo/'lab/process'/NORMAL_BUNDLE
    bundle=json.loads(bundlepath.read_text());assert bundle['final_probe_sha256']==digest(__file__)
    assert set(bundle['records'])==set(NORMAL_RECORDS)
    import source_action_mixed_consistency_probe as mixed
    originals={}
    for name in NORMAL_RECORDS:
        raw=mixed.unpack_record(bundle['records'][name]);assert (args.cache/name).read_bytes()==raw
        originals[name]=raw
    custody=producer_custody(args)
    rebuilt=args.cache/'recomputed';rebuilt.mkdir(exist_ok=True)
    (rebuilt/'normal-scout.json').write_bytes(originals['normal-scout.json'])
    child=SimpleNamespace(**vars(args));child.cache=rebuilt;child.carrier='all'
    stage_constants(child)
    original=json.loads(originals['normal-constants.json']);new=json.loads((rebuilt/'normal-constants.json').read_text())
    same_fields(original,new,('input_controls','E4','sources','complete'),'constants')
    stage_carrier(child)
    for label in('even4','odd4','odd3'):
        for suffix,keys in(('highest',('spin','parity','weight_dimension','next_weight_dimension','highest_dimension','weight_keys','raising_columns','highest_coordinates','complete')),
                            ('kernel',('completed','columns')),
                            ('basis',('complete','spin','parity','ambient_highest_dimension','time_rank','dimension','basis','basis_pivots','exact_center_source_membership'))):
            name=label+'-'+suffix+'.json'
            same_fields(json.loads(originals[name]),json.loads((rebuilt/name).read_text()),keys,name)
    child=SimpleNamespace(**vars(args));child.generate_candidates=False;child.carrier='all'
    stage_certify(child)
    certs={}
    for label in('even4','odd4','odd3'):
        name=label+'-certificate.json';old=json.loads(originals[name]);new=json.loads((args.cache/name).read_text())
        same_fields(old,new,('bindings','dimension','complete_carrier_dimension','norm_constants','integer_basis_norm_majorants','both_root_boxes_invertible'),name)
        for a,b in zip(old['roots'],new['roots']):
            same_fields(a,b,('root','root_record_sha256','radius','balanced_center_defect_column1','Ctriangle_upper','rootbox_perturbation_column1','neumann_bound','native_M_invertible_on_complete_block'),name)
        certs[label]={'dimension':old['dimension'],'complete_carrier_dimension':old['complete_carrier_dimension'],
                     'root_neumann_bounds':[r['neumann_bound_float']for r in old['roots']]}
        (args.cache/name).write_bytes(originals[name])
    stage_controls(child)
    old=json.loads(originals['normal-controls.json']);new=json.loads((args.cache/'normal-controls.json').read_text())
    same_fields(old,new,('dependencies','input_controls','native_kappa_rotation_mask','ambient_U_Ktau_commutator_checks','all_59_backgrounds_rotation_fixed_and_even','producer_custody','complete_time_kernel_character','matrix_controls','all_complete_certificates_pass','complete'),'controls')
    (args.cache/'normal-controls.json').write_bytes(originals['normal-controls.json'])
    assert all(digest(args.cache/name)==bundle['records'][name]['sha256']for name in NORMAL_RECORDS)
    out={'passed':True,'probe_sha256':digest(__file__),'bundle_sha256':digest(bundlepath),'record_count':len(NORMAL_RECORDS),
         'complete_carriers_reconstructed':['even4','odd4','odd3'],'all_native_H_columns_recomputed':False,
         'native_H_columns_recomputed':6,'remaining_H_columns':'Authenticated frozen exact native production records',
         'all_exact_frozen_preconditioner_defects_recomputed':True,'floating_inverse_regenerated':False,
         'producer_custody_verified':True,'certificates':certs,'seconds':time.monotonic()-tick,
         'scope':'Bounded fresh-cache replay: full carriers, first native H column eachroot/block, and all exact certificate arithmetic; no propagation or physical-domain necessity claim.'}
    path=args.output or args.cache/'normal-replay.json';write(path,out);print('NN REPLAY PASS',path,'seconds',out['seconds'],flush=True)


def stage_compare(args):
    assert args.reference_cache is not None,'--reference-cache is required for compare'
    for label in('even4','odd4','odd3'):
        name=label+'-matrices.json';left=json.loads((args.reference_cache/name).read_text());right=json.loads((args.cache/name).read_text())
        assert left['complete']and right['complete'];same_fields(left,right,('bindings','dimension'),name)
        for a,b in zip(sorted(left['roots'],key=lambda r:r['root']),sorted(right['roots'],key=lambda r:r['root'])):
            same_fields(a,b,('root','root_record_sha256','completed','columns','real_symmetric','hermitian','complete'),name)
            assert [r['integer_image_sha256']for r in a['image_controls']]==[r['integer_image_sha256']for r in b['image_controls']]
    print('NN full native H reproduction: all mathematical columns and complete native image hashes match',flush=True)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2]);ap.add_argument('--cache',type=Path,required=True)
    ap.add_argument('--carrier',choices=('all','even4','odd4','odd3'),default='all')
    ap.add_argument('--root-index',type=int,choices=(0,1))
    ap.add_argument('--steps',type=int,default=30)
    ap.add_argument('--backend',choices=('auto','flint','python'),default='auto')
    ap.add_argument('--precision',type=int,default=24)
    ap.add_argument('--generate-candidates',action='store_true')
    ap.add_argument('--output',type=Path,help='Output path for bundle, replay, or status')
    ap.add_argument('--bundle',type=Path,help='Installed certificate bundle override for unpack/replay')
    ap.add_argument('--reference-cache',type=Path,help='Frozen cache for full matrix comparison')
    ap.add_argument('--mode',choices=('constants','scout','witnesses','numeric','carrier','matrix','certify','controls','bundle','unpack','replay','compare','status'),required=True)
    args=ap.parse_args();args.repo=args.repo.resolve();args.cache.mkdir(parents=True,exist_ok=True)
    sys.path.insert(0,str(args.repo/'tests/program-focus'))
    globals()['stage_'+args.mode](args)


if __name__=='__main__':main()
