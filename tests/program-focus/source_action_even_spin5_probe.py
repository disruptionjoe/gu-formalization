#!/usr/bin/env python3
"""Complete even highest5 time-kernel and native M range test.

The carrier is complete by its weight character and invertible exterior-basis
change. Numerical inverse candidates are never acceptance; negative conclusions
retain the augmented normal/zero-order multiplier repairs.
"""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from types import SimpleNamespace
from collections import Counter
import argparse,hashlib,inspect,json,os,sys,time
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[name]='1'
sys.dont_write_bytecode=True
CHI_MASK=13319
PAIRS=((0,1,1),(10,12,1),(9,11,1),(5,8,2))
ZEROS=(2,3,4,6,7,13)


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def jd(value):return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def write(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_suffix(path.suffix+'.new');temp.write_text(json.dumps(value,indent=2)+'\n');temp.replace(path)
def serialize(v):return [[e,cl,z.ser()]for(e,cl),z in sorted(v.items())]
def coordinates_serial(v):return [[i,z.ser()]for i,z in sorted(v.items())]


def setup(args):
    sys.path.insert(0,str(args.repo/'tests/program-focus'))
    import source_action_mixed_consistency_probe as mixed
    c=mixed.setup(args);c.mixed=mixed
    return c


def native_bindings(args):
    names=('source_action_mixed_consistency_probe.py','source_action_constraint_consistency_probe.py',
           'source_action_spin4_compatibility_probe.py','source_action_weak_response_probe.py',
           'source_action_paired_response_probe.py','source_action_deep_algebra.py',
           'source_action_deep_geometry.py','source_action_metric_symbol_probe.py',
           'source_action_physical_probe.py','source_action_slice_completion_probe.py')
    out={'tests/program-focus/'+name:digest(args.repo/'tests/program-focus'/name)for name in names}
    for name in('source-action-deep-coefficients.json','source-action-mixed-consistency-certificates.json'):
        out['lab/process/'+name]=digest(args.repo/'lab/process'/name)
    return out


def sparse_kernel(c,columns):
    pivots={};rows=[];kernels=[]
    for index,v in enumerate(columns):
        v=dict(v);cs={index:c.C(1)}
        while v:
            pivot=min(v)
            if pivot not in pivots:
                z=v[pivot];v={k:x/z for k,x in v.items()};cs={k:x/z for k,x in cs.items()}
                pivots[pivot]=len(rows);rows.append((v,cs));break
            b,bc=rows[pivots[pivot]];z=v[pivot]
            for target,source in((v,b),(cs,bc)):
                for k,x in source.items():
                    y=target.get(k,c.C())-z*x
                    if y:target[k]=y
                    else:target.pop(k,None)
        if not v:kernels.append(cs)
    return rows,kernels


def combine(c,coordinates,basis):return c.add(*(c.scale(z,basis[i])for i,z in coordinates.items()if z))


class EvenCarrier:
    """Exact complete weight5/6 coordinates in the native imaginary carrier."""
    def __init__(self,c):
        self.c=c;C=c.C;I=c.I
        atoms=[];weights=[];charges=[]
        for sign in(1,-1):
            for a,b,w in PAIRS:
                atoms.append({1<<a:C(1),1<<b:sign*I});weights.append(sign*w)
                pa,pb=(CHI_MASK>>a)&1,(CHI_MASK>>b)&1;assert pa==pb;charges.append(pa)
        for a in ZEROS:
            atoms.append({1<<a:C(1)});weights.append(0);charges.append((CHI_MASK>>a)&1)
        self.atoms=atoms;self.weights=weights;self.charges=charges
        inv={}
        for j,(a,b,w)in enumerate(PAIRS):
            inv[a]={1<<j:C(1)/2,1<<(j+4):C(1)/2}
            inv[b]={1<<j:-I/2,1<<(j+4):I/2}
        for j,a in enumerate(ZEROS,8):inv[a]={1<<j:C(1)}
        self.inverse_atoms=inv
        for j,atom in enumerate(atoms):
            back={}
            for native,x in atom.items():
                for key,y in inv[native.bit_length()-1].items():back[key]=back.get(key,C())+x*y
            assert {k:v for k,v in back.items()if v}=={1<<j:C(1)}
        metadata=[]
        for mask in range(1<<14):
            degree=mask.bit_count()
            if degree%4 not in(0,3):continue
            weight=sum(weights[j]for j in range(14)if mask>>j&1)
            chi=sum(charges[j]for j in range(14)if mask>>j&1)%2
            metadata.append((mask,weight,chi))
        self.keys={m:[(j,mask)for mask,w,chi in metadata for j in range(14)
                      if w+weights[j]==m and chi==charges[j]]for m in(5,6)}
        assert len(self.keys[5])==664 and len(self.keys[6])==152
        self.lookup={m:{key:i for i,key in enumerate(keys)}for m,keys in self.keys.items()}

    @staticmethod
    def sign(a,b):return -1 if sum((b&((1<<k)-1)).bit_count()for k in range(14)if a>>k&1)%2 else 1

    def wedge(self,a,b):
        out={};C=self.c.C
        for e,x in a.items():
            for f,y in b.items():
                if e&f:continue
                key=e|f;out[key]=out.get(key,C())+self.sign(e,f)*x*y
        return {k:z for k,z in out.items()if z}

    @lru_cache(None)
    def cliff_native(self,mask):
        out={0:self.c.C(1)}
        for j in range(14):
            if mask>>j&1:out=self.wedge(out,self.atoms[j])
        return out

    @lru_cache(None)
    def cliff_inverse(self,mask):
        out={0:self.c.C(1)}
        for j in range(14):
            if mask>>j&1:out=self.wedge(out,self.inverse_atoms[j])
        return out

    def native(self,key):
        j,mask=key
        return {(e,cl):x*y for e,x in self.atoms[j].items()for cl,y in self.cliff_native(mask).items()if x*y}

    def coordinates(self,v,weight=5):
        out={};C=self.c.C
        for(e,cl),x in v.items():
            assert e.bit_count()==1 and cl.bit_count()%4 in(0,3)
            assert not(((e^cl)&CHI_MASK).bit_count()%2)
            for ei,y in self.inverse_atoms[e.bit_length()-1].items():
                j=ei.bit_length()-1
                for mask,z in self.cliff_inverse(cl).items():
                    key=j,mask;out[key]=out.get(key,C())+x*y*z
        out={k:z for k,z in out.items()if z}
        assert set(out)<=set(self.lookup[weight]),('Outside full weight space',weight)
        return {self.lookup[weight][k]:z for k,z in out.items()}

    def weight_basis(self):return [self.native(key)for key in self.keys[5]]


def basis_binding(args):
    funcs=(setup,sparse_kernel,combine,EvenCarrier,stage_highest,stage_profile,stage_kernel)
    return {'native_inputs':native_bindings(args),'constructor_sha256':hashlib.sha256('\n'.join(inspect.getsource(f)for f in funcs).encode()).hexdigest()}


def load_highest(c,carrier,args):
    data=json.loads((args.cache/'even-highest5.json').read_text());assert data['bindings']==basis_binding(args)
    assert data['complete']and data['weight5_dimension']==664 and data['highest_dimension']==512
    assert data['weight_keys']==[list(k)for k in carrier.keys[5]]
    W=carrier.weight_basis()
    relations=[{i:c.C(*z)for i,z in row}for row in data['highest_coordinates']]
    H=[combine(c,co,W)for co in relations]
    return data,W,H


def stage_highest(args):
    tick=time.monotonic();c=setup(args);carrier=EvenCarrier(c);W=carrier.weight_basis()
    columns=[];grade_counts=Counter()
    for i,(key,v)in enumerate(zip(carrier.keys[5],W)):
        assert carrier.coordinates(v)=={i:c.C(1)}
        assert c.s.rot(0,1,v)==c.scale(5*c.I,v)
        raised=c.add(c.s.rot(0,2,v),c.scale(c.I,c.s.rot(1,2,v)))
        columns.append(carrier.coordinates(raised,6));grade_counts[key[1].bit_count()]+=1
        if(i+1)%32==0:print('EVEN weight roundtrip/raising',i+1,'/664 seconds',time.monotonic()-tick,flush=True)
    rows,ker=sparse_kernel(c,columns);assert len(rows)==152 and len(ker)==512
    out={'scope':'Complete even ambient highest5 carrier, before time-kernel restriction.',
         'bindings':basis_binding(args),'execution_probe_sha256':digest(__file__),
         'weight5_dimension':664,'weight6_dimension':152,'raising_rank':152,'highest_dimension':512,
         'weight_grade_counts':dict(grade_counts),'weight_keys':[list(k)for k in carrier.keys[5]],
         'raising_columns':[coordinates_serial(v)for v in columns],
         'highest_coordinates':[coordinates_serial(v)for v in ker],
         'complete':True,'seconds':time.monotonic()-tick}
    write(args.cache/'even-highest5.json',out)
    print('EVEN complete highest5',512,'seconds',out['seconds'],flush=True)


def stage_profile(args):
    c=setup(args);carrier=EvenCarrier(c);data,W,H=load_highest(c,carrier,args)
    n=args.steps or 16;indices=sorted(set(i*len(H)//n for i in range(n)))
    out={'scope':'Timing only; compares K3 and P routes on the same complete-highest5 columns.',
         'bindings':basis_binding(args),'highest_sha256':digest(args.cache/'even-highest5.json'),'rows':[]}
    for i in indices:
        h=H[i];tick=time.monotonic();kh=c.K(3,h);kc=carrier.coordinates(kh);t1=time.monotonic()
        ph=c.P(h);pc=carrier.coordinates(ph);t2=time.monotonic()
        assert not c.K(3,ph)and c.P(ph)==ph
        assert not c.add(c.s.rot(0,2,ph),c.scale(c.I,c.s.rot(1,2,ph)))
        row={'index':i,'input_terms':len(h),'K_terms':len(kh),'P_terms':len(ph),
             'K_seconds':t1-tick,'P_seconds':t2-t1,'K_coordinate_terms':len(kc),'P_coordinate_terms':len(pc)}
        out['rows'].append(row);write(args.cache/'even-profile.json',out)
        print('EVEN profile',row,flush=True)


def stage_kernel(args):
    c=setup(args);carrier=EvenCarrier(c);high,W,H=load_highest(c,carrier,args)
    method=args.method;path=args.cache/('even-time-columns-'+method+'.json')
    live=basis_binding(args)|{'highest_sha256':digest(args.cache/'even-highest5.json'),'method':method}
    data={'scope':'Full512 highest5 native time-symbol or projection columns.','bindings':live,'completed':0,'columns':[]}
    if path.exists():
        data=json.loads(path.read_text());assert data['bindings']==live
        assert data['completed']==len(data['columns'])
    start=time.monotonic();begin=data['completed'];end=512 if args.steps==0 else min(512,begin+args.steps)
    for i in range(begin,end):
        v=c.P(H[i])if method=='project'else c.K(3,H[i])
        co=carrier.coordinates(v);data['columns'].append(coordinates_serial(co));data['completed']=i+1
        if(i+1)%16==0 or i+1==end:
            data['last_batch_seconds']=time.monotonic()-start;write(path,data)
            print('EVEN time columns',method,i+1,'/512 seconds',data['last_batch_seconds'],flush=True)
    if data['completed']!=512:return
    cols=[{i:c.C(*z)for i,z in row}for row in data['columns']]
    rows,ker=sparse_kernel(c,cols)
    fields=[combine(c,row,W)for row,cs in rows]if method=='project'else[combine(c,co,H)for co in ker]
    native_rows,dependence=sparse_kernel(c,fields);assert not dependence
    basis=[row for row,cs in native_rows];pivots=[min(v)for v in basis]
    for i,v in enumerate(basis):
        assert not c.K(3,v)
        assert c.s.rot(0,1,v)==c.scale(5*c.I,v)
        assert not c.add(c.s.rot(0,2,v),c.scale(c.I,c.s.rot(1,2,v)))
        assert c.s.q['cas'](v)==c.scale(30,v)
        assert not(((min(v)[0]^min(v)[1])&CHI_MASK).bit_count()%2)
        if(i+1)%32==0:print('EVEN final native basis checks',i+1,'/',len(basis),flush=True)
    dimension=len(basis)
    out={'scope':'Complete even highest5 native time-kernel; no M solvability yet.',
         'bindings':live|{'columns_sha256':digest(path)},'complete':True,
         'ambient_highest5_dimension':512,'complete_N5_even_dimension':dimension,
         'time_rank':512-dimension,'method':method,'native_equation_checks':4*dimension,
         'basis':[serialize(v)for v in basis],'basis_pivots':[list(p)for p in pivots],
         'seconds_finalization':time.monotonic()-start}
    write(args.cache/'even-basis.json',out)
    print('EVEN COMPLETE N5 dimension',dimension,'method',method,flush=True)



def load_even(c,args):
    data=json.loads((args.cache/'even-basis.json').read_text())
    assert data['complete']and data['bindings']['constructor_sha256']==basis_binding(args)['constructor_sha256']
    assert data['bindings']['native_inputs']==native_bindings(args)
    basis=[{(e,cl):c.C(*z)for e,cl,z in row}for row in data['basis']]
    pivots=[tuple(k)for k in data['basis_pivots']]
    assert len(basis)==data['complete_N5_even_dimension']==len(pivots)
    return data,basis,pivots


def reduce_field(c,v,basis,pivots):
    # sparse_kernel discovers pivots in column order. Sort the triangular
    # elimination order, while keeping returned coordinates in basis order.
    co=[c.C()for _ in basis];v=dict(v)
    for i in sorted(range(len(basis)),key=lambda j:pivots[j]):
        pivot,b=pivots[i],basis[i];z=c.C(v.get(pivot,0));co[i]=z
        if z:v=c.add(v,c.scale(-z,b))
    return v,co


def paired_rows(c,basis):
    from math import lcm
    q={};den=1
    for i,v in enumerate(basis):
        for k,z in v.items():
            value=z.conj()*c.E.weight(*k)
            q.setdefault(k,[]).append((i,value))
            den=lcm(den,value.a.denominator,value.b.denominator)
    qi={k:[(i,int(z.a*den),int(z.b*den))for i,z in row]for k,row in q.items()}
    return q,den,qi


def paired_integer(c,qi,n,vector,denominator,qden):
    values=[(0,0)for _ in range(n)]
    for k,(a,b)in vector.items():
        for i,x,y in qi.get(k,()):
            u,v=values[i];values[i]=(u+x*a-y*b,v+x*b+y*a)
    den=denominator*qden
    return [c.C(Q(a,den),Q(b,den))for a,b in values]


def source_records(c,args):
    bundle=json.loads((args.repo/'lab/process/source-action-mixed-consistency-certificates.json').read_text())
    records={k:json.loads(c.mixed.unpack_record(v))for k,v in bundle['records'].items()if k in('mixed-constants.json','mixed-numeric.json')}
    sources={}
    for row in records['mixed-constants.json']['columns']:
        if row['spin']==5 and row['normal_axis']!=10:
            label=('d9'if row['normal_axis']==9 else 'B')+'_V'+str(row['basis_index'])
            sources[label]={(e,cl):c.C(*z)for e,cl,z in row['source']}
    sources['A_root0_V5_rational_center']={(e,cl):c.C(*z)for e,cl,z in records['mixed-numeric.json']['source_A_rational_center']}
    return sources


def norm_constants(c,basis):
    g=(1,1,1,1,4,3,5,7,3,3,3,3,3,3)
    weights=[1]*16384
    for mask in range(1,16384):
        bit=mask&-mask;weights[mask]=weights[mask^bit]*g[bit.bit_length()-1]
    assert all(g[i]*g[i]>=abs(c.g.d[i])for i in range(14))
    total=sum(g);pairs=sum(g[i]*g[j]for i in range(14)for j in range(i+1,14))
    phi=max(2*Q(g[i],abs(c.g.d[i]))+2*Q(g[j],abs(c.g.d[j]))+2*Q(g[i]*g[j],abs(c.g.d[i]*c.g.d[j]))*total for i in range(14)for j in range(i+1,14))
    adj=max(2*(total-g[i])+2*Q(g[i],abs(c.g.d[i]))*pairs for i in range(14))
    bound=(2*phi+4*adj)/6
    assert(total,pairs,phi,adj,bound)==(41,762,86,1604,1098)
    ab=lambda z:abs(c.C(z).a)+abs(c.C(z).b)
    Tsum=sum(weights[cl]*ab(z)for T in c.Ts for(e,cl),z in T.items())
    assert Tsum==Q(128637452,3)
    D=[sum(weights[cl]*ab(z)for(e,cl),z in v.items())for v in basis]
    assert all(d>0 for d in D)
    return weights,D,{'coordinate_weights':list(g),'exterior_weight':1,'phi_bound':str(phi),
        'phi_adjoint_bound':str(adj),'N_bilinear_bound':str(bound),'background_basis_norm_sum':str(Tsum),
        'basis_norms':[str(d)for d in D],'interpretation':'Computational weighted coefficient1 norm; no physical positivity assertion.'}


def stage_validate(args):
    tick=time.monotonic();c=setup(args);bd,basis,pivots=load_even(c,args);n=len(basis)
    sources=source_records(c,args);checks=[]
    for name,v in sources.items():
        rem,co=reduce_field(c,v,basis,pivots);assert not rem,('Actual source outside complete carrier',name)
        checks.append({'name':name,'terms':len(v),'source_sha256':jd(serialize(v)),
            'coordinates':[z.ser()for z in co],'exact_status':'Rational-center diagnostic'if 'center'in name else 'Exact root-independent constant'})
    signs=[1,-1,-1,1,1,1,1,1,-1,-1,1,1,-1,-1]
    for v in basis:
        cc={(e,cl):z.conj()*((-1)**sum(1 for a,t in enumerate(signs)if t<0 and (((e>>a)&1)^((cl>>a)&1))))for(e,cl),z in v.items()}
        assert not reduce_field(c,cc,basis,pivots)[0]
    q,qd,qi=paired_rows(c,basis);G=[]
    for v in basis:
        den,vi=c.integer.clear_denominators(v)
        G.append(paired_integer(c,qi,n,vi,den,qd))
    assert all(G[j][i]==G[i][j].conj()for i in range(n)for j in range(n))
    rows,kernel=sparse_kernel(c,[{i:z for i,z in enumerate(col)if z}for col in G])
    assert len(rows)==n and not kernel
    for i,j in((0,0),(0,n-1),(n//2,n//2),(n-1,n-1)):
        assert G[j][i]==c.E.pair({k:z.conj()for k,z in basis[i].items()},basis[j])
    weights,D,norm=norm_constants(c,basis)
    out={'scope':'Complete native even N5 source/reality/pairing checks, before root-M certificate.',
        'bindings':native_bindings(args)|{'basis_sha256':digest(args.cache/'even-basis.json'),
        'validation_procedure_sha256':hashlib.sha256('\n'.join(inspect.getsource(f)for f in(load_even,reduce_field,paired_rows,paired_integer,source_records,norm_constants,stage_validate)).encode()).hexdigest()},
        'dimension':n,'source_checks':checks,'highest_reality_closed':True,'gram_rank':n,'gram_hermitian':True,
        'gram_columns':[[[i,z.ser()]for i,z in enumerate(col)if z]for col in G],
        'norm_constants':norm,'complete':True,'seconds':time.monotonic()-tick}
    write(args.cache/'even-validation.json',out)
    print('EVEN native sources/reality/Gram PASS',n,'seconds',out['seconds'],flush=True)


def matrix_binding(args):
    funcs=(load_even,paired_rows,paired_integer,stage_matrix)
    return {'native_inputs':native_bindings(args),'basis_sha256':digest(args.cache/'even-basis.json'),
        'assembly_procedure_sha256':hashlib.sha256('\n'.join(inspect.getsource(f)for f in funcs).encode()).hexdigest(),
        'engine_sha256':digest(args.repo/'tests/program-focus/source_action_spin4_compatibility_probe.py')}


def stage_matrix(args):
    c=setup(args);bd,basis,pivots=load_even(c,args);n=len(basis);E=c.integer
    q,qd,qi=paired_rows(c,basis);path=args.cache/'even-root-matrices.json';live=matrix_binding(args)
    out={'scope':'Exact paired H=Z†J C Z on complete even N5 at rational root centers; P omitted by native adjoint identity.',
        'bindings':live,'dimension':n,'roots':[]}
    if path.exists():out=json.loads(path.read_text());assert out['bindings']==live
    for ri,owned in enumerate(c.background['certified_roots']):
        if args.root_index is not None and ri!=args.root_index:continue
        rows=[r for r in out['roots']if r['root']==ri];assert len(rows)<=1
        if rows:r=rows[0]
        else:
            r={'root':ri,'root_record_sha256':jd(owned),'completed':0,'columns':[],'image_controls':[]};out['roots'].append(r)
        assert r['completed']==len(r['columns'])
        T=c.add(*(c.scale(Q(x),v)for x,v in zip(owned['coordinates'],c.Ts)))
        du,ui,au=E.prepare(T);start=time.monotonic();begin=r['completed'];end=n if args.steps==0 else min(n,begin+args.steps)
        for j in range(begin,end):
            tick=time.monotonic();dv,vi,av=E.prepare(basis[j])
            numerator=E.Phi_scaled(E.wedge_comm_int(ui,vi))
            c.fast.add_into(numerator,E.wadj_scaled(ui,av));c.fast.add_into(numerator,E.wadj_scaled(vi,au))
            denominator=3*E.Dphi*du*dv;c.fast.add_into(numerator,vi,3*E.Dphi*du)
            numerator=c.fast.prune(numerator)
            assert all(e.bit_count()==1 and cl.bit_count()%4 in(0,3)and not(((e^cl)&CHI_MASK).bit_count()%2)for e,cl in numerator)
            column=paired_integer(c,qi,n,numerator,denominator,qd)
            if j==0:
                raw=E.restore(numerator,denominator)
                projected=c.P(raw);rem,co=reduce_field(c,projected,basis,pivots);assert not rem
                assert not c.K(3,projected)
                assert not c.add(c.s.rot(0,2,projected),c.scale(c.I,c.s.rot(1,2,projected)))
                assert all(column[i]==c.E.pair({k:z.conj()for k,z in basis[i].items()},raw)for i in range(n))
                r['first_column_P_range_and_pairing_controls']=True
            r['columns'].append([[i,z.ser()]for i,z in enumerate(column)if z]);r['completed']=j+1
            r['image_controls'].append({'column':j,'complete_native_C_image_terms':len(numerator),
                'integer_denominator':str(denominator),'integer_image_sha256':jd([[e,cl,str(a),str(b)]for(e,cl),(a,b)in sorted(numerator.items())]),
                'seconds':time.monotonic()-tick})
            if(j+1)%8==0 or j+1==end:
                r['last_batch_seconds']=time.monotonic()-start;write(path,out)
                print('EVEN root paired-H',ri,j+1,'/',n,'seconds',r['last_batch_seconds'],flush=True)
        if r['completed']==n:
            cols=[{i:c.C(*z)for i,z in row}for row in r['columns']]
            assert all(cols[j].get(i,c.C())==cols[i].get(j,c.C()).conj()for i in range(n)for j in range(n))
            r['hermitian']=True;r['complete']=True;write(path,out)
    out['complete']=len(out['roots'])==2 and all(r.get('complete')for r in out['roots']);write(path,out)



def dense_paired_matrix(c,record,n):
    import numpy as np
    from math import lcm
    denominator=1;entries=[]
    assert record['completed']==n and len(record['columns'])==n and record['hermitian']
    for j,column in enumerate(record['columns']):
        previous=-1
        for i,z in column:
            assert previous<i<n;previous=i;value=c.C(*z);assert value
            denominator=lcm(denominator,value.a.denominator,value.b.denominator)
            entries.append((i,j,value))
    real=np.zeros((n,n),dtype=object);imag=np.zeros((n,n),dtype=object)
    for i,j,z in entries:real[i,j]=int(z.a*denominator);imag[i,j]=int(z.b*denominator)
    return real,imag,denominator


def balanced_matrix(real,imag,denominator,D):
    from math import lcm
    assert all(d.denominator==1 and d>0 for d in D)
    L=lcm(*(int(d)for d in D));multipliers=[L//int(d)for d in D]
    n=len(D);rr=real.copy();ri=imag.copy()
    for i in range(n):
        for j in range(n):
            rr[i,j]*=multipliers[i]*multipliers[j];ri[i,j]*=multipliers[i]*multipliers[j]
    return rr,ri,denominator*L*L,L


def balanced_candidate(args,real,imag,denominator,binding):
    import numpy as np
    path=args.cache/'even-inverse-candidates.json';n=real.shape[0]
    if path.exists():data=json.loads(path.read_text());assert data['format']=='gu-even-spin5-balanced-inverses-v1'
    else:data={'format':'gu-even-spin5-balanced-inverses-v1','scope':'Frozen rational approximate inverse of Hs=D^-1 H D^-1. Exact residual/root bound decides acceptance.','roots':[]}
    matches=[r for r in data['roots']if r['root']==binding['root']];assert len(matches)<=1
    if matches:
        row=matches[0];assert row['bindings']==binding
    else:
        assert args.generate_candidates,'Use --generate-candidates once; replay never regenerates floating inverses.'
        h=np.array([[complex(float(Q(int(a),denominator)),float(Q(int(b),denominator)))for a,b in zip(ar,ai)]for ar,ai in zip(real,imag)],dtype=np.complex128)
        inverse=np.linalg.inv(h);assert np.isfinite(inverse).all();den=10**args.precision
        rr=[[int(round(Q(str(float(z.real)))*den))for z in line]for line in inverse]
        ri=[[int(round(Q(str(float(z.imag)))*den))for z in line]for line in inverse]
        row={'root':binding['root'],'bindings':binding,'dimension':n,'denominator':str(den),
             'real_numerators':[[str(v)for v in line]for line in rr],
             'imag_numerators':[[str(v)for v in line]for line in ri]}
        data['roots'].append(row);data['roots'].sort(key=lambda r:r['root']);write(path,data)
    assert row['dimension']==n and len(row['real_numerators'])==len(row['imag_numerators'])==n
    assert all(len(r)==n for r in row['real_numerators']+row['imag_numerators'])
    assert all(type(v)is str and v.lstrip('+-').isdigit()for r in row['real_numerators']+row['imag_numerators']for v in r)
    den=int(row['denominator']);assert den>0
    rr=np.array([[int(v)for v in r]for r in row['real_numerators']],dtype=object)
    ri=np.array([[int(v)for v in r]for r in row['imag_numerators']],dtype=object)
    return rr,ri,den


def weighted_defect(Hr,Hi,DH,Rr,Ri,DR):
    import numpy as np
    n=Hr.shape[0];product_r=Rr@Hr-Ri@Hi;product_i=Rr@Hi+Ri@Hr;den=DH*DR
    er=np.eye(n,dtype=object)*den-product_r;ei=-product_i
    numerator=max(sum(abs(int(er[i,j]))+abs(int(ei[i,j]))for i in range(n))for j in range(n))
    return Q(numerator,den)


def triangle_bound(c,basis,D,weights,Rr,Ri,DR):
    from math import lcm
    n=len(basis);L=lcm(*(int(d)for d in D));DZ=1
    for v in basis:
        for z in v.values():DZ=lcm(DZ,z.a.denominator,z.b.denominator)
    t=[sum(abs(int(Rr[i,j]))+abs(int(Ri[i,j]))for i in range(n))*(L//int(D[j]))for j in range(n)]
    native={}
    for j,v in enumerate(basis):
        for key,z in v.items():
            a=int((abs(z.a)+abs(z.b))*DZ);native[key]=native.get(key,0)+t[j]*a
    denominator=DR*L*DZ
    return max((Q(value,denominator)*abs(c.E.weight(*key))/weights[key[1]]for key,value in native.items()),default=Q())


def certificate_controls(c):
    import numpy as np
    H=[[c.C(3),c.C(1,1)],[c.C(1,-1),c.C(4)]]
    Rs=[[c.C(1),c.C(0,2)],[c.C(0,-3),c.C(2)]];DR=7
    Hr=np.array([[3,1],[1,4]],dtype=object);Hi=np.array([[0,1],[-1,0]],dtype=object)
    Rr=np.array([[1,0],[0,2]],dtype=object);Ri=np.array([[0,2],[-3,0]],dtype=object)
    literal=[[c.C(i==j)-sum((Rs[i][k]*H[k][j]for k in range(2)),c.C())/DR for j in range(2)]for i in range(2)]
    expected=max(sum(abs(literal[i][j].a)+abs(literal[i][j].b)for i in range(2))for j in range(2))
    assert weighted_defect(Hr,Hi,1,Rr,Ri,DR)==expected
    rownorm=max(sum(abs(z.a)+abs(z.b)for z in row)for row in literal);assert rownorm!=expected
    basis=[{(1,0):c.C(2)},{(2,0):c.C(3)}];D=[Q(2),Q(3)]
    actual=triangle_bound(c,basis,D,[1]*16384,Rr,Ri,DR)
    expected_triangle=Q(max(sum(abs(int(Rr[i,j]))+abs(int(Ri[i,j]))for i in range(2))for j in range(2)),DR)
    assert actual==expected_triangle
    return {'complex_fraction_defect_control':True,'column_not_row_norm_control':True,'native_sparse_triangle_control':True}


def stage_certify(args):
    tick=time.monotonic();c=setup(args);bd,basis,pivots=load_even(c,args);n=len(basis)
    validation=json.loads((args.cache/'even-validation.json').read_text());assert validation['complete']and validation['gram_rank']==n
    assert validation['bindings']['basis_sha256']==digest(args.cache/'even-basis.json')
    validation_functions=(load_even,reduce_field,paired_rows,paired_integer,source_records,norm_constants,stage_validate)
    assert validation['bindings']['validation_procedure_sha256']==hashlib.sha256('\n'.join(inspect.getsource(f)for f in validation_functions).encode()).hexdigest()
    path=args.cache/'even-root-matrices.json';matrices=json.loads(path.read_text())
    assert matrices['bindings']==matrix_binding(args)and matrices['complete']and matrices['dimension']==n
    assert sorted(r['root']for r in matrices['roots'])==[0,1]
    weights,D,norm=norm_constants(c,basis);assert norm==validation['norm_constants']
    funcs=(dense_paired_matrix,balanced_matrix,balanced_candidate,weighted_defect,triangle_bound,certificate_controls,stage_certify)
    binding={'native_inputs':native_bindings(args),'basis_sha256':digest(args.cache/'even-basis.json'),
        'validation_sha256':digest(args.cache/'even-validation.json'),'matrix_sha256':digest(path),
        'certificate_procedure_sha256':hashlib.sha256('\n'.join(inspect.getsource(f)for f in funcs).encode()).hexdigest()}
    out={'scope':'Complete even highest5 native M invertibility throughout both owned root boxes via paired H=Gram*M. No positivity, propagation or source necessity claim.',
         'bindings':binding,'dimension':n,'norm_constants':norm,'controls':certificate_controls(c),'roots':[]}
    for ri,owned in enumerate(c.background['certified_roots']):
        record=next(r for r in matrices['roots']if r['root']==ri)
        assert record['complete']and record['first_column_P_range_and_pairing_controls']
        assert record['root_record_sha256']==jd(owned)
        Hr,Hi,DH=dense_paired_matrix(c,record,n);Hs_r,Hs_i,DHs,L=balanced_matrix(Hr,Hi,DH,D)
        cb=binding|{'root':ri,'root_record_sha256':jd(owned),'balanced_integer_denominator':str(DHs)}
        Rs_r,Rs_i,DR=balanced_candidate(args,Hs_r,Hs_i,DHs,cb)
        eta0=weighted_defect(Hs_r,Hs_i,DHs,Rs_r,Rs_i,DR)
        Ctri=triangle_bound(c,basis,D,weights,Rs_r,Rs_i,DR)
        radius=Q(owned['certificate']['radius']);delta=2196*radius*Q(128637452,3)*Ctri;eta=eta0+delta
        rr={'root':ri,'owned_root_record_sha256':jd(owned),'radius':str(radius),
            'balanced_center_defect_column1':str(eta0),'Ctriangle_upper':str(Ctri),
            'rootbox_perturbation_column1':str(delta),'neumann_bound':str(eta),
            'neumann_bound_float':float(eta),'invertible_on_complete_even_N5_rootbox':eta<1,
            'native_Gram_non_degenerate':True,'complete_native_M_invertible':eta<1}
        out['roots'].append(rr);out['seconds']=time.monotonic()-tick
        out['preconditioner_sha256']=digest(args.cache/'even-inverse-candidates.json')
        out['both_root_boxes_invertible']=len(out['roots'])==2 and all(r['complete_native_M_invertible']for r in out['roots'])
        write(args.cache/'even-certificate.json',out)
        print('EVEN root certificate',ri,'eta0',float(eta0),'delta',float(delta),'total',float(eta),'PASS',eta<1,flush=True)



class OddCarrier(EvenCarrier):
    """Same native exterior basis, complementary chi-odd sector."""
    def __init__(self,c):
        super().__init__(c);metadata=[]
        for mask in range(1<<14):
            if mask.bit_count()%4 not in(0,3):continue
            weight=sum(self.weights[j]for j in range(14)if mask>>j&1)
            chi=sum(self.charges[j]for j in range(14)if mask>>j&1)%2
            metadata.append((mask,weight,chi))
        self.keys={m:[(j,mask)for mask,w,chi in metadata for j in range(14)
                      if w+self.weights[j]==m and chi!=self.charges[j]]for m in(5,6)}
        assert len(self.keys[5])==684 and len(self.keys[6])==148
        self.lookup={m:{key:i for i,key in enumerate(keys)}for m,keys in self.keys.items()}

    def coordinates(self,v,weight=5):
        out={};C=self.c.C
        for(e,cl),x in v.items():
            assert e.bit_count()==1 and cl.bit_count()%4 in(0,3)
            assert((e^cl)&CHI_MASK).bit_count()%2==1
            for ei,y in self.inverse_atoms[e.bit_length()-1].items():
                j=ei.bit_length()-1
                for mask,z in self.cliff_inverse(cl).items():
                    key=j,mask;out[key]=out.get(key,C())+x*y*z
        out={k:z for k,z in out.items()if z}
        assert set(out)<=set(self.lookup[weight]),('Outside full odd weight space',weight)
        return {self.lookup[weight][k]:z for k,z in out.items()}


def stage_odd(args):
    tick=time.monotonic();c=setup(args);carrier=OddCarrier(c);W=carrier.weight_basis();raised=[]
    for i,v in enumerate(W):
        assert carrier.coordinates(v)=={i:c.C(1)}
        assert c.s.rot(0,1,v)==c.scale(5*c.I,v)
        raised.append(carrier.coordinates(c.add(c.s.rot(0,2,v),c.scale(c.I,c.s.rot(1,2,v))),6))
        if(i+1)%64==0:print('ODD weight roundtrip/raising',i+1,'/684 seconds',time.monotonic()-tick,flush=True)
    rrows,hco=sparse_kernel(c,raised);assert len(rrows)==148 and len(hco)==536
    H=[combine(c,co,W)for co in hco];time_columns=[]
    for i,v in enumerate(H):
        time_columns.append(carrier.coordinates(c.K(3,v)))
        if(i+1)%64==0:print('ODD native K3 columns',i+1,'/536 seconds',time.monotonic()-tick,flush=True)
    trows,kco=sparse_kernel(c,time_columns);dimension=536-len(trows);assert dimension==len(kco)
    owned=[];metadata={}
    for name,certname in(('source-action-weak-response.json','inverse-stage5-certificate.json'),
                        ('source-action-constraint-source-repair-certificates.json','repair-fast-certificate.json')):
        path=args.repo/'lab/process'/name;bundle=json.loads(path.read_text())
        records=bundle['reproduction']['records']if name=='source-action-weak-response.json'else bundle['records']
        bd=json.loads(c.mixed.unpack_record(records['inverse-stage3-basis.json']))
        cert=json.loads(c.mixed.unpack_record(records[certname]))
        assert len(bd['basis'])==120
        assert len(cert['roots'])==2 and all(r['invertible_on_block_over_rootball']and Q(r['neumann_bound'])<1 for r in cert['roots'])
        fields=[{(e,cl):c.C(*z)for e,cl,z in row}for row in bd['basis']]
        for v in fields:
            assert not c.K(3,v)
            assert c.s.rot(0,1,v)==c.scale(5*c.I,v)
            assert not c.add(c.s.rot(0,2,v),c.scale(c.I,c.s.rot(1,2,v)))
            assert all(((e^cl)&CHI_MASK).bit_count()%2==1 for e,cl in v)
            carrier.coordinates(v)
        owned.extend(fields)
        metadata[name]={'bundle_sha256':digest(path),'basis_sha256':records['inverse-stage3-basis.json']['sha256'],
            'certificate_sha256':records[certname]['sha256'],'dimension':120,
            'root_neumann_bounds':[r['neumann_bound']for r in cert['roots']]}
    independent,dependence=sparse_kernel(c,owned);assert not dependence and len(independent)==240
    funcs=(EvenCarrier,OddCarrier,sparse_kernel,combine,stage_odd)
    out={'scope':'Complete odd highest5 native time-kernel dimension and exact comparison to both previously certified120-dimensional receivers. No new odd inverse.',
        'bindings':{'native_inputs':native_bindings(args),'procedure_sha256':hashlib.sha256('\n'.join(inspect.getsource(f)for f in funcs).encode()).hexdigest()},
        'weight5_dimension':684,'weight6_dimension':148,'raising_rank':148,'ambient_highest5_dimension':536,
        'time_symbol_rank':len(trows),'complete_N5_odd_dimension':dimension,'owned_odd_receiver_rank':240,
        'owned_odd_sum_exhausts_complete_time_kernel':dimension==240,
        'owned_receivers':metadata,'weight_keys':[list(k)for k in carrier.keys[5]],
        'raising_columns':[coordinates_serial(v)for v in raised],
        'highest_coordinates':[coordinates_serial(v)for v in hco],
        'time_columns':[coordinates_serial(v)for v in time_columns],
        'complete':True,'seconds':time.monotonic()-tick}
    write(args.cache/'odd-completion.json',out)
    print('ODD COMPLETE N5 dimension',dimension,'owned rank240 exhausts',dimension==240,'seconds',out['seconds'],flush=True)



def stage_controls(args):
    tick=time.monotonic();c=setup(args);bd,basis,pivots=load_even(c,args)
    from source_action_deep_algebra import Engine
    original=Engine(c.g)
    validation=json.loads((args.cache/'even-validation.json').read_text())
    matrices=json.loads((args.cache/'even-root-matrices.json').read_text())
    assert matrices['complete']and matrices['bindings']==matrix_binding(args)
    gram=[{i:c.C(*z)for i,z in row}for row in validation['gram_columns']]
    out={'scope':'Independent native Hodge-Euler and pairing reconstruction of one exact H column at each center, plus generic integer/projection controls.',
        'probe_sha256':digest(__file__),'native_inputs':native_bindings(args),
        'basis_sha256':digest(args.cache/'even-basis.json'),'matrix_sha256':digest(args.cache/'even-root-matrices.json'),
        'integer_engine':c.fast.integer_controls(args.repo),'projection':c.fast.projection_controls(args.repo),'roots':[]}
    for ri,owned in enumerate(c.background['certified_roots']):
        T=c.add(*(c.scale(Q(x),v)for x,v in zip(owned['coordinates'],c.Ts)))
        raw=c.add(basis[0],c.scale(2,original.N(T,basis[0])))
        record=next(r for r in matrices['roots']if r['root']==ri);image=record['image_controls'][0];den=int(image['integer_denominator'])
        nums=[]
        for(e,cl),z in sorted(raw.items()):
            ar=z.a*den;ai=z.b*den;assert ar.denominator==ai.denominator==1
            nums.append([e,cl,str(int(ar)),str(int(ai))])
        assert jd(nums)==image['integer_image_sha256'],'Independent original Euler image differs'
        projected=c.P(raw);rem,co=reduce_field(c,projected,basis,pivots);assert not rem
        h={i:c.C(*z)for i,z in record['columns'][0]}
        for i in range(len(basis)):
            from_gram=sum((gram[j].get(i,c.C())*co[j]for j in range(len(basis))),c.C())
            paired=original.pair({k:z.conj()for k,z in basis[i].items()},raw)
            assert from_gram==paired==h.get(i,c.C())
        out['roots'].append({'root':ri,'original_Hodge_Euler_full_image_matches':True,
            'P_C_image_inside_complete_N5':True,'H_equals_Gram_times_native_M_column':True,
            'native_pairing_checks':len(basis),'native_image_sha256':image['integer_image_sha256']})
    out['all_passed']=True;out['seconds']=time.monotonic()-tick
    write(args.cache/'even-controls.json',out)
    print('EVEN original Euler/paired-H controls PASS seconds',out['seconds'],flush=True)


BUNDLE_NAME='source-action-even-spin5-certificates.json'
RECORD_NAMES=('even-highest5.json','even-profile.json','even-time-columns-kernel.json',
    'even-basis.json','even-validation.json','even-root-matrices.json',
    'even-inverse-candidates.json','even-certificate.json','odd-completion.json','even-controls.json')


def stage_bundle(args):
    import base64,zlib
    assert args.output,'Bundle requires --output.'
    controls=json.loads((args.cache/'even-controls.json').read_text())
    assert controls['probe_sha256']==digest(__file__)and controls['all_passed']
    cert=json.loads((args.cache/'even-certificate.json').read_text())
    odd=json.loads((args.cache/'odd-completion.json').read_text())
    assert cert['both_root_boxes_invertible']and odd['owned_odd_sum_exhausts_complete_time_kernel']
    records={}
    for name in RECORD_NAMES:
        raw=(args.cache/name).read_bytes();json.loads(raw)
        records[name]={'encoding':'zlib-base64-json','uncompressed_bytes':len(raw),
            'sha256':hashlib.sha256(raw).hexdigest(),'data':base64.b64encode(zlib.compress(raw,9)).decode()}
    out={'schema':'gu-complete-even-spin5-certificates-v1','data_only':True,
        'scope':'Complete even N5 root-box invertibility and complete odd N5 exhaustion by owned receivers; no physical admission or propagation verdict.',
        'probe_sha256':digest(__file__),'native_inputs':native_bindings(args),'records':records}
    write(args.output,out);print('EVEN installed-data bundle',args.output,flush=True)


def stage_unpack(args):
    import base64,zlib
    bundle=json.loads((args.repo/'lab/process'/BUNDLE_NAME).read_text())
    assert set(bundle['records'])==set(RECORD_NAMES)
    assert bundle['probe_sha256']==digest(__file__)and bundle['native_inputs']==native_bindings(args)
    for name in RECORD_NAMES:
        record=bundle['records'][name];assert record['encoding']=='zlib-base64-json'
        raw=zlib.decompress(base64.b64decode(record['data'],validate=True))
        assert len(raw)==record['uncompressed_bytes']and hashlib.sha256(raw).hexdigest()==record['sha256']
        json.loads(raw);(args.cache/name).write_bytes(raw)
    print('EVEN unpack authenticated records',len(RECORD_NAMES),flush=True)


def without_seconds(value):
    if isinstance(value,dict):return {k:without_seconds(v)for k,v in value.items()if k!='seconds'}
    if isinstance(value,list):return [without_seconds(v)for v in value]
    return value


def compare_fields(a,b,names):
    for name in names:assert a[name]==b[name],('Exact reconstruction differs',name)


def stage_replay(args):
    # Reconstruct complete native carriers; reuse/authenticate the expensive H
    # matrix record, with original-Euler first-column replay at both centers.
    original_cache=args.cache;original_output=args.output
    original={name:json.loads((original_cache/name).read_text())for name in RECORD_NAMES}
    child=original_cache/'reconstruction';suffix=0
    while child.exists():suffix+=1;child=original_cache/('reconstruction-'+str(suffix))
    child.mkdir();args.cache=child;args.steps=0;args.method='kernel'
    stage_highest(args);stage_kernel(args);stage_validate(args);stage_odd(args)
    high=json.loads((child/'even-highest5.json').read_text())
    compare_fields(original['even-highest5.json'],high,('weight5_dimension','weight6_dimension','raising_rank','highest_dimension','weight_grade_counts','weight_keys','raising_columns','highest_coordinates','complete'))
    timecols=json.loads((child/'even-time-columns-kernel.json').read_text())
    compare_fields(original['even-time-columns-kernel.json'],timecols,('completed','columns'))
    basis=json.loads((child/'even-basis.json').read_text())
    compare_fields(original['even-basis.json'],basis,('complete_N5_even_dimension','time_rank','native_equation_checks','basis','basis_pivots','complete'))
    validation=json.loads((child/'even-validation.json').read_text())
    compare_fields(original['even-validation.json'],validation,('dimension','source_checks','highest_reality_closed','gram_rank','gram_hermitian','gram_columns','norm_constants','complete'))
    odd=json.loads((child/'odd-completion.json').read_text())
    compare_fields(original['odd-completion.json'],odd,('weight5_dimension','weight6_dimension','raising_rank','ambient_highest5_dimension','time_symbol_rank','complete_N5_odd_dimension','owned_odd_receiver_rank','owned_odd_sum_exhausts_complete_time_kernel','owned_receivers','weight_keys','raising_columns','highest_coordinates','time_columns','complete'))
    args.cache=original_cache;args.generate_candidates=False
    for name,fn in(('even-controls.json',stage_controls),('even-certificate.json',stage_certify)):
        path=original_cache/name;saved=path.read_bytes()
        try:
            fn(args);new=json.loads(path.read_text())
            assert without_seconds(original[name])==without_seconds(new),('Frozen exact replay differs',name)
        finally:path.write_bytes(saved)
    args.output=original_output
    out={'scope':'Fresh-cache full even/odd carrier reconstruction, native first-H-column replay at each center and frozen exact certificate replay. Other H columns are authenticated stored arithmetic, not recomputed by this bounded mode.',
        'probe_sha256':digest(__file__),'all_passed':True,
        'even_dimension':basis['complete_N5_even_dimension'],'odd_dimension':odd['complete_N5_odd_dimension'],
        'all_N5_rootbox_invertible':True,'record_sha256':{name:digest(original_cache/name)for name in RECORD_NAMES}}
    write(args.output or original_cache/'even-replay.json',out)
    print('EVEN bounded fresh-cache replay PASS; all N5 dimension480',flush=True)


def stage_status(args):
    bundle=json.loads((args.repo/'lab/process'/BUNDLE_NAME).read_text())
    assert bundle['probe_sha256']==digest(__file__)and bundle['native_inputs']==native_bindings(args)
    for name in RECORD_NAMES:assert digest(args.cache/name)==bundle['records'][name]['sha256']
    basis=json.loads((args.cache/'even-basis.json').read_text());certificate=json.loads((args.cache/'even-certificate.json').read_text())
    odd=json.loads((args.cache/'odd-completion.json').read_text());controls=json.loads((args.cache/'even-controls.json').read_text())
    assert basis['bindings']['constructor_sha256']==basis_binding(args)['constructor_sha256']
    assert controls['all_passed']and controls['probe_sha256']==digest(__file__)
    assert certificate['both_root_boxes_invertible']and odd['owned_odd_sum_exhausts_complete_time_kernel']
    out={'scope':'Authenticated complete N5 range-certificate status; physical source/domain/propagation remain separate.',
        'probe_sha256':digest(__file__),'bundle_sha256':digest(args.repo/'lab/process'/BUNDLE_NAME),
        'complete_even_N5_dimension':basis['complete_N5_even_dimension'],'complete_odd_N5_dimension':odd['complete_N5_odd_dimension'],
        'complete_N5_dimension':basis['complete_N5_even_dimension']+odd['complete_N5_odd_dimension'],
        'both_roots_invertible':True,'root_neumann_bounds':[r['neumann_bound']for r in certificate['roots']],
        'native_controls_passed':True}
    write(args.output or args.cache/'even-status.json',out);print(json.dumps(out,indent=2),flush=True)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2])
    ap.add_argument('--cache',type=Path,required=True)
    ap.add_argument('--mode',choices=('highest','profile','kernel','validate','matrix','certify','odd','controls','bundle','unpack','replay','status'),required=True)
    ap.add_argument('--steps',type=int,default=16)
    ap.add_argument('--output',type=Path,help='Output for bundle, replay or status modes.')
    ap.add_argument('--generate-candidates',action='store_true')
    ap.add_argument('--precision',type=int,default=24)
    ap.add_argument('--root-index',type=int,choices=(0,1))
    ap.add_argument('--method',choices=('project','kernel'),default='project')
    args=ap.parse_args();args.repo=args.repo.resolve();args.cache=args.cache.resolve();args.cache.mkdir(parents=True,exist_ok=True)
    if args.output is not None:assert args.mode in('bundle','replay','status'),'--output is only used by bundle/replay/status.'
    globals()['stage_'+args.mode](args)


if __name__=='__main__':main()
