#!/usr/bin/env python3
"""Actual scalar-normal quadratic-block operator in a named adapted frame.

Finite operator assembly only; no invariant 1+1 ansatz or propagation claim.
"""
from pathlib import Path
from fractions import Fraction as Q
from types import SimpleNamespace
import argparse, hashlib, inspect, json, os, sys, time
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[name]='1'
sys.dont_write_bytecode=True
import source_action_constraint_consistency_probe as cc


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def jd(value):return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def write(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_suffix(path.suffix+'.new');temp.write_text(json.dumps(data,indent=2)+'\n');temp.replace(path)
def ser(c,v):return [[e,cl,c.C(z).ser()]for(e,cl),z in sorted(v.items())]
def decode(c,v):return {(e,cl):c.C(*z)for e,cl,z in v}
def sm(M):return [[z.ser()for z in row]for row in M]
def dm(c,M):return [[c.C(*z)for z in row]for row in M]
def tr(M):return sum((M[i][i]for i in range(len(M))),0)
def mm(c,A,B):
    rows=[[(j,z)for j,z in enumerate(row)if z]for row in B]
    out=[[c.C()for _ in B[0]]for _ in A]
    for i,row in enumerate(A):
        for k,z in enumerate(row):
            if z:
                for j,w in rows[k]:out[i][j]+=z*w
    return out
def ma(c,*A):return [[sum((M[i][j]for M in A),c.C())for j in range(len(A[0][0]))]for i in range(len(A[0]))]
def ms(z,A):return [[z*x for x in row]for row in A]
def eye(c,n):return [[c.C(i==j)for j in range(n)]for i in range(n)]
def rref(c,A):
    A=[[c.C(z)for z in row]for row in A];piv=[];r=0
    for j in range(len(A[0])):
        p=next((i for i in range(r,len(A))if A[i][j]),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r];z=A[r][j];A[r]=[x/z for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][j]:
                z=A[i][j];A[i]=[x-z*y for x,y in zip(A[i],A[r])]
        piv.append(j);r+=1
        if r==len(A):break
    return A,piv
def inverse(c,A):
    n=len(A);a,p=rref(c,[row+e for row,e in zip(A,eye(c,n))]);assert p==list(range(n))
    return [row[n:]for row in a]
def kernel(c,A):
    a,p=rref(c,A);out=[]
    for j in range(len(A[0])):
        if j in p:continue
        v=[c.C(i==j)for i in range(len(A[0]))]
        for i,k in enumerate(p):v[k]=-a[i][j]
        out.append(v)
    return out


def inputs(args):
    names=['source_action_constraint_consistency_probe.py','source_action_deep_geometry.py',
           'source_action_deep_algebra.py','source_action_metric_symbol_probe.py',
           'source_action_weak_response_probe.py','source_action_paired_response_probe.py',
           'source_action_spin4_compatibility_probe.py']
    out={'tests/program-focus/'+n:digest(args.repo/'tests/program-focus'/n)for n in names}
    for n in ['source-action-deep-coefficients.json','source-action-kappa1-constraints.json',
              'source-action-graph-domain.json']:
        out['lab/process/'+n]=digest(args.repo/'lab/process'/n)
    return out


def setup(args):
    c=cc.setup(args.repo);c.geo=cc.geometry(c);c.bs=c.s.bs;c.piv=[min(v)for v in c.bs]
    def coords(v):
        a=[c.C(v.get(k,0))for k in c.piv]
        assert v==c.add(*(c.scale(z,b)for z,b in zip(a,c.bs)if z)),('outside full highest7',len(v))
        return a
    c.coords=coords
    c.field=lambda a:c.add(*(c.scale(z,b)for z,b in zip(a,c.bs)if z))
    c.cas=c.s.q['cas'];return c


def geometry_data(c):
    g=c.g;Xs=[]
    for S,H in zip(g.A,c.geo.adapt[4:]):
        X=[[S[i][j]+H[i][j]for j in range(4)]for i in range(4)]
        assert all(not X[3][j]for j in range(3));Xs.append(X)
    hs={};mc={};checked=0;v2={5,6,8,9,11};rots=[]
    for i,j in ((0,1),(0,2),(1,2)):
        H=g.zero();H[i][j]=1;H[j][i]=-1;rots.append(H)
    for b in range(4,14):
        for a in range(4,14):
            X=g.comm(Xs[b-4],Xs[a-4])
            S=[[Q(X[i][j]+g.eta[i]*g.eta[j]*X[j][i],2)for j in range(4)]for i in range(4)]
            co=[g.vg(S,A)/g.d[k+4]for k,A in enumerate(g.A)]
            assert not co[0]
            h=[[X[i][j]-sum(z*M[i][j]for z,M in zip(co,Xs))for j in range(4)]for i in range(4)]
            assert all(h[3][i]==h[i][3]==0 for i in range(4))
            if any(any(row)for row in h):
                assert a in v2 and b in v2;hs[b,a]=h
            if any(co):mc[b,a]=co
            for (i,j),J in zip(((0,1),(0,2),(1,2)),rots):
                cov=-g.h_action(J,a).get(b,Q())
                assert h[i][j]==(-g.d[b]*cov/8 if b in v2 else 0);checked+=1
    assert len(hs)==16 and all(not any(row)for row in c.geo.gammas[4])
    assert Xs[0]==g.eye()
    def derivative(b,v):
        terms=[]
        for a in range(4,14):
            h=hs.get((b,a))
            if h is not None:
                J=[[g.h_action(h,j).get(i,Q())for j in range(14)]for i in range(14)]
                terms.append(c.scale(-Q(1,2),c.K(a,c.geo.rho(J,v))))
        return c.add(*terms)
    return SimpleNamespace(Xs=Xs,h=hs,m=mc,v2=v2,derivative=derivative,checks=checked)


def stage_geometry(args):
    tick=time.monotonic();c=setup(args);gd=geometry_data(c);n=len(c.bs);assert n==36
    colsA=[];colsB=[];colsL=[];controls=[]
    for i,v in enumerate(c.bs):
        assert c.cas(v)==c.scale(56,v)
        assert not c.add(c.s.rot(0,2,v),c.scale(c.I,c.s.rot(1,2,v)))
        assert c.geo.lower(v,False)==c.E.K(v)
        colsA.append(c.coords(c.K(3,v)));colsB.append(c.coords(c.K(4,v)))
        colsL.append(c.coords(c.geo.lower(v)))
        for b in gd.v2:
            raw=c.K(b,v);dv=gd.derivative(b,v)
            rhs=c.scale(c.g.d[b]/32,c.add(c.scale(62,raw),c.scale(-1,c.cas(raw))))
            assert dv==rhs,('derivative/Casimir mismatch',i,b)
            controls.append([i,b,len(dv)])
        if(i+1)%6==0:print('SCALAR geometry',i+1,'/36 seconds',time.monotonic()-tick,flush=True)
    A=[list(row)for row in zip(*colsA)];B=[list(row)for row in zip(*colsB)];L=[list(row)for row in zip(*colsL)]
    old=json.loads((args.repo/'lab/process/source-action-kappa1-constraints.json').read_text())
    assert jd(sm(A))==old['exact_probe']['spin7']['time_matrix_sha256']
    zs=kernel(c,A);assert len(zs)==16
    N=[c.field(z)for z in zs]
    G=[[c.E.pair({k:z.conj()for k,z in u.items()},v)for v in c.bs]for u in c.bs]
    Z=[list(row)for row in zip(*zs)];ZH=[[z.conj()for z in row]for row in zs]
    GN=mm(c,mm(c,ZH,G),Z);assert jd(sm(GN))==old['exact_probe']['spin7']['kernel_gram_sha256']
    P=mm(c,mm(c,Z,inverse(c,GN)),mm(c,ZH,G));R=ma(c,eye(c,n),ms(-1,P))
    assert mm(c,P,P)==P and mm(c,A,P)==ms(0,A)and mm(c,P,A)==ms(0,A)
    assert mm(c,mm(c,P,L),P)==ms(0,A)
    assert mm(c,mm(c,P,B),P)==ms(0,A)
    _,rp=rref(c,R);assert len(rp)==20
    U=[[R[i][j]for j in rp]+[Z[i][j]for j in range(16)]for i in range(36)];Ui=inverse(c,U)
    As=mm(c,mm(c,Ui,A),U);Ar=[row[:20]for row in As[:20]]
    Gs=[[c.C()for _ in range(36)]for _ in range(36)]
    for i,row in enumerate(inverse(c,Ar)):
        for j,z in enumerate(row):Gs[i][j]=z
    Gtime=mm(c,mm(c,U,Gs),Ui)
    assert mm(c,A,Gtime)==R and mm(c,Gtime,A)==R
    for i,v in enumerate(c.bs):
        assert c.P(v)==c.field([P[j][i]for j in range(36)])
    out={'complete':True,'native_inputs':inputs(args),'execution_probe_sha256':digest(__file__),
         'procedure_sha256':hashlib.sha256('\n'.join(inspect.getsource(f)for f in(setup,geometry_data,stage_geometry)).encode()).hexdigest(),
         'dimension':36,'time_range_dimension':20,'time_kernel_dimension':16,
         'bracket_covector_checks':gd.checks,'native_derivative_Casimir_checks':controls,
         'adapted_generators':[[[str(z)for z in row]for row in X]for X in gd.Xs],
         'isotropy_brackets':[[b,a,[[str(z)for z in row]for row in H]]for(b,a),H in sorted(gd.h.items())],
         'basis':[ser(c,v)for v in c.bs],'range_basis':[ser(c,c.field([U[i][j]for i in range(36)]))for j in range(20)],
         'kernel_basis':[ser(c,v)for v in N],
         'matrices':{name:sm(M)for name,M in [('A',A),('B',B),('Lgeo',L),('Gram',G),('P',P),('R',R),('Gtime',Gtime),('U',U),('Uinv',Ui)]},
         'section':'s(x,z)=(x,exp(sum z^a(A_a+H_a))); left Maurer-Cartan; h_ba=pr_h[X_b,X_a]',
         'derivative_convention':'partial_b C0=-1/2 sum_a K_a rho(h_ba); only b in spatial V2; equals d_b(62-Cas)K_b/32 on spin7',
         'lapse':'e_a(t)=0 for a!=3; e3(t)=lambda; central trace lambda=exp(r); outer time inverse factor lambda^-1 retained',
         'scope':'Exact geometry and pointwise highest7 matrices only; no invariant1+1 ansatz or spectral conclusion.',
         'seconds':time.monotonic()-tick}
    write(args.cache/'scalar-geometry.json',out);print('SCALAR GEOMETRY PASS seconds',out['seconds'],flush=True)


def load_geometry(c,args):
    path=args.cache/'scalar-geometry.json';d=json.loads(path.read_text())
    assert d['complete']and d['native_inputs']==inputs(args)
    assert d['basis']==[ser(c,v)for v in c.bs]
    return d,{k:dm(c,v)for k,v in d['matrices'].items()}


def stage_affine(args):
    tick=time.monotonic();c=setup(args);geo,mat=load_geometry(c,args)
    raw=json.loads((args.repo/'lab/process/source-action-deep-coefficients.json').read_text())
    Ts=[{(e,cl):Q(z)for e,cl,z in row}for row in raw['basis']]
    reverse={}
    for a,T in enumerate(Ts):
        for key,z in T.items():reverse.setdefault(key,[]).append((a,z*c.E.weight(*key)))
    pairs=[(i,j)for i in range(36)for j in range(i,36)]
    live={'native_inputs':inputs(args),'geometry_sha256':digest(args.cache/'scalar-geometry.json'),
          'procedure_sha256':hashlib.sha256('\n'.join(inspect.getsource(f)for f in(setup,load_geometry,stage_affine)).encode()).hexdigest()}
    path=args.cache/'scalar-affine.json'
    out={'bindings':live,'completed':0,'pairs':[],'complete':False,'execution_probe_sha256':digest(__file__)}
    if path.exists():out=json.loads(path.read_text());assert out['bindings']==live and len(out['pairs'])==out['completed']
    begin=out['completed'];end=len(pairs)if args.steps==0 else min(len(pairs),begin+args.steps)
    for k in range(begin,end):
        i,j=pairs[k];left={key:z.conj()for key,z in c.bs[i].items()}
        receiver=c.scale(2,c.integer.N(left,c.bs[j]));co=[c.C()for _ in Ts]
        for key,z in receiver.items():
            for a,w in reverse.get(key,[]):co[a]+=z*w
        if i==j:assert all(not z.b for z in co)
        out['pairs'].append({'i':i,'j':j,'coefficients':[z.ser()for z in co],
                             'receiver_sha256':jd(ser(c,receiver)),'receiver_terms':len(receiver)})
        out['completed']=k+1
        if(k+1)%12==0 or k+1==end:
            out['last_batch_seconds']=time.monotonic()-tick;out['complete']=out['completed']==len(pairs)
            write(path,out);print('SCALAR affine',k+1,'/',len(pairs),'seconds',out['last_batch_seconds'],flush=True)


def owned_records(args,bundle,names,reproduction=False):
    import base64,zlib
    path=args.repo/'lab/process'/bundle;data=json.loads(path.read_text())
    records=data['reproduction']['records']if reproduction else data['records'];out={}
    for name in names:
        r=records[name];raw=zlib.decompress(base64.b64decode(r['data']))
        assert len(raw)==r['uncompressed_bytes']and hashlib.sha256(raw).hexdigest()==r['sha256']
        out[name]=json.loads(raw)
    return out,{'bundle':str(path.relative_to(args.repo)),'bundle_sha256':digest(path),
                'records':{name:records[name]['sha256']for name in names}}


def response_data(c,args):
    old,bo=owned_records(args,'source-action-weak-response.json',
        ['inverse-stage3-basis.json','inverse-stage5-certificate.json'],True)
    repair,br=owned_records(args,'source-action-constraint-source-repair-certificates.json',
        ['inverse-stage3-basis.json','repair-inverse-candidates.json','repair-fast-certificate.json'])
    ev,be=owned_records(args,'source-action-even-spin5-certificates.json',
        ['even-basis.json','even-inverse-candidates.json','even-certificate.json'])
    six,b6=owned_records(args,'source-action-mixed-consistency-certificates.json',['native-n6.json'])
    kappa=json.loads((args.repo/'lab/process/source-action-kappa1-constraints.json').read_text())
    groups={}
    for name,data,record,mode,cert,candidate in(
        ('old5',old,'inverse-stage3-basis.json','coordinates','inverse-stage5-certificate.json',None),
        ('repair5',repair,'inverse-stage3-basis.json','coordinates','repair-fast-certificate.json','repair-inverse-candidates.json'),
        ('even5',ev,'even-basis.json','balanced_paired','even-certificate.json','even-inverse-candidates.json')):
        bd=data[record];basis=[decode(c,row)for row in bd['basis']]
        pivots=[tuple(k)for k in bd['basis_pivots']]
        groups[name]={'basis':basis,'pivots':pivots,'mode':mode,'certificate':data[cert],
                      'candidate':None if candidate is None else data[candidate]}
    groups['spin6']={'basis':[decode(c,row)for row in six['native-n6.json']['basis']],
                     'mode':'paired','certificate':kappa['exact_probe']['spin6']['constraint_inverse'],
                     'candidate':kappa['spin6_inverse_candidates']}
    gd=json.loads((args.cache/'scalar-geometry.json').read_text())
    groups['spin7']={'basis':[decode(c,row)for row in gd['kernel_basis']],
                    'mode':'paired','certificate':kappa['exact_probe']['spin7'],'candidate':None}
    assert [len(groups[k]['basis'])for k in groups]==[120,120,240,128,16]
    sa=set().union(*(v.keys()for v in groups['old5']['basis']));sb=set().union(*(v.keys()for v in groups['repair5']['basis']))
    assert not sa&sb
    return groups,{'old5':bo,'repair5':br,'even5':be,'spin6':b6,
                   'kappa_sha256':digest(args.repo/'lab/process/source-action-kappa1-constraints.json')}


def reduce_native(c,v,basis,pivots):
    v=dict(v);co=[c.C()for _ in basis]
    for i in sorted(range(len(basis)),key=lambda j:pivots[j]):
        z=c.C(v.get(pivots[i],0));co[i]=z
        if z:v=c.add(v,c.scale(-z,basis[i]))
    return v,co


def part(c,v,j):
    for other in(5,6,7):
        if other!=j:v=c.scale(Q(1,j*(j+1)-other*(other+1)),c.add(c.cas(v),c.scale(-other*(other+1),v)))
    return v


def scalar_ladders(c):
    F=lambda v:c.add(c.s.rot(0,2,v),c.scale(-c.I,c.s.rot(1,2,v)))
    Ka=lambda v:c.add(c.K(5,v),c.scale(-c.I,c.K(8,v)))
    Kb=lambda v:c.add(c.K(9,v),c.scale(-c.I,c.K(11,v)))
    Kap=lambda v:c.add(c.K(5,v),c.scale(c.I,c.K(8,v)))
    Kbp=lambda v:c.add(c.K(9,v),c.scale(c.I,c.K(11,v)))
    return F,Ka,Kb,Kap,Kbp


def stage_maps(args):
    tick=time.monotonic();c=setup(args);geo,M=load_geometry(c,args);groups,owned=response_data(c,args)
    F,Ka,Kb,Kap,Kbp=scalar_ladders(c);Vr=[decode(c,row)for row in geo['range_basis']]
    src={5:[],6:[],7:[]};controls=[]
    for i,v in enumerate(Vr):
        a=c.P(Ka(v));b=c.P(Kb(v));s=c.P(c.K(6,v))
        a5,a6,a7=[part(c,a,j)for j in(5,6,7)];b6,b7=[part(c,b,j)for j in(6,7)]
        assert a==c.add(a5,a6,a7)and b==c.add(b6,b7)and c.cas(s)==c.scale(56,s)
        assert a6==c.scale(Q(1,6),F(b6))and b7==c.scale(-Q(3,7),F(s))
        assert a7==c.scale(-Q(3,91),F(F(s)))
        for j,w in((5,a5),(6,b6),(7,s)):
            assert not c.K(3,w)and not c.add(c.s.rot(0,2,w),c.scale(c.I,c.s.rot(1,2,w)))
            src[j].append(w)
        controls.append({'range_index':i,'terms':[len(a5),len(b6),len(s)],'all_ladder_identities_exact':True})
    live={'native_inputs':inputs(args),'owned_inputs':owned,'geometry_sha256':digest(args.cache/'scalar-geometry.json'),
          'procedure_sha256':hashlib.sha256('\n'.join(inspect.getsource(f)for f in(response_data,reduce_native,part,scalar_ladders,stage_maps)).encode()).hexdigest()}
    path=args.cache/'scalar-response-maps.json'
    out={'bindings':live,'input_controls':controls,'groups':{},'complete':False,'execution_probe_sha256':digest(__file__)}
    if path.exists():out=json.loads(path.read_text());assert out['bindings']==live and out['input_controls']==controls
    co5={k:[]for k in('old5','repair5','even5')}
    for source in src[5]:
        rem=source
        for name in co5:
            group=groups[name];rem,co=reduce_native(c,rem,group['basis'],group['pivots']);co5[name].append(co)
        assert not rem,'Full owned N5 source reconstruction required.'
    left=mm(c,M['Uinv'],M['Gtime'])[:20]
    completed=0;budget=args.steps if args.steps else 10**9
    for name,group in groups.items():
        bs=group['basis'];j=5 if name.endswith('5')else int(name[-1]);n=len(bs)
        if name in('old5','repair5'):S=[list(row)for row in zip(*co5[name])]
        else:S=[[c.C(c.E.pair({key:z.conj()for key,z in v.items()},s))for s in src[j]]for v in bs]
        entry=out['groups'].setdefault(name,{'dimension':n,'mode':group['mode'],'source_matrix':sm(S),'output_columns':[]})
        assert entry['source_matrix']==sm(S)and entry['dimension']==n
        for k in range(len(entry['output_columns']),n):
            if completed==budget:break
            v=bs[k]
            if j==5:w=c.scale(4,Kap(v))
            elif j==6:w=c.scale(Q(5,2),c.add(Kbp(v),c.scale(Q(1,6),Kap(F(v)))))
            else:w=c.add(c.scale(-Q(9,364),Kap(F(F(v)))),c.scale(-Q(9,28),Kbp(F(v))),c.scale(Q(9,2),c.K(6,v)))
            co=c.coords(w);column=[sum((a*b for a,b in zip(row,co)),c.C())for row in left]
            entry['output_columns'].append([z.ser()for z in column]);completed+=1
            if(k+1)%16==0 or k+1==n or completed==budget:
                out['seconds']=time.monotonic()-tick;write(path,out)
                print('SCALAR maps',name,k+1,'/',n,'seconds',out['seconds'],flush=True)
        if completed==budget:break
    out['complete']=len(out['groups'])==5 and all(len(v['output_columns'])==v['dimension']for v in out['groups'].values())
    out['seconds']=time.monotonic()-tick;write(path,out)


def n1(z):return abs(z.a)+abs(z.b)
def absm(A):return [[n1(z)for z in row]for row in A]
def qmm(A,B):
    out=[[Q()for _ in B[0]]for _ in A];s=[[(j,z)for j,z in enumerate(row)if z]for row in B]
    for i,row in enumerate(A):
        for k,z in enumerate(row):
            if z:
                for j,w in s[k]:out[i][j]+=z*w
    return out
def qadd(*A):return [[sum(M[i][j]for M in A)for j in range(len(A[0][0]))]for i in range(len(A[0]))]
def fast_mm(c,A,B):
    from math import lcm
    da=lcm(*(q.denominator for row in A for z in row for q in(z.a,z.b)))
    db=lcm(*(q.denominator for row in B for z in row for q in(z.a,z.b)))
    ar=[[int(z.a*da)for z in row]for row in A];ai=[[int(z.b*da)for z in row]for row in A]
    br=[[int(z.a*db)for z in row]for row in B];bi=[[int(z.b*db)for z in row]for row in B]
    try:
        from flint import fmpz_mat,ctx
        ctx.threads=1
        def mul(x,y):return (fmpz_mat(x)*fmpz_mat(y)).tolist()
    except ImportError:
        def mul(x,y):return [[sum(a*b for a,b in zip(row,col))for col in zip(*y)]for row in x]
    rr=mul(ar,br);ii=mul(ai,bi);ri=mul(ar,bi);ir=mul(ai,br);den=da*db
    return [[c.C(Q(int(rr[i][j]-ii[i][j]),den),Q(int(ri[i][j]+ir[i][j]),den))for j in range(len(B[0]))]for i in range(len(A))]
def ball(A,E=None):return(A,[[Q()for _ in row]for row in A]if E is None else E)
def badd(c,*As):return(ma(c,*(a[0]for a in As)),qadd(*(a[1]for a in As)))
def bneg(A):return(ms(-1,A[0]),A[1])
def bmul(c,A,B):
    return(fast_mm(c,A[0],B[0]),qadd(qmm(absm(A[0]),B[1]),qmm(A[1],absm(B[0])),qmm(A[1],B[1])))
def bpart(A,rows,cols):return([[A[0][i][j]for j in cols]for i in rows],[[A[1][i][j]for j in cols]for i in rows])
def sb(A):return {'center':sm(A[0]),'entry_l1_error':[[str(z)for z in row]for row in A[1]]}


def candidate_matrix(c,row):
    d=int(row['denominator'])
    return [[c.C(Q(int(a),d),Q(int(b),d))for a,b in zip(ar,ai)]for ar,ai in zip(row['real_numerators'],row['imag_numerators'])]


def solve_paired7(c,Hinv,GN,S,eta):
    rhs=bmul(c,ball(GN),S);X=fast_mm(c,Hinv,rhs[0]);extra=qmm(absm(Hinv),rhs[1])
    eps=[(eta*max(n1(row[j])for row in X)+max(row[j]for row in extra))/(1-eta)for j in range(len(X[0]))]
    return ball(X,[list(eps)for _ in X])


def correction_group(c,name,group,data,ri,Hinv=None):
    S=dm(c,data['source_matrix']);O=[list(row)for row in zip(*dm(c,data['output_columns']))]
    n=len(S);m=len(S[0]);errors=[[Q()for _ in range(m)]for _ in O]
    details=[]
    if name=='spin6':
        X=[[c.C()for _ in range(m)]for _ in range(n)]
        cert=group['certificate']['root_certificates'][ri]
        for source,proof in zip(group['candidate'][ri]['blocks'],cert['blocks']):
            assert jd(source['rational_inverse'])==proof['rational_inverse_sha256']
            assert source['indices']==group['certificate']['constraint_components'][proof['component']]
            ids=source['indices'];R=dm(c,source['rational_inverse']);Z=fast_mm(c,R,[S[i]for i in ids])
            eta=Q(proof['neumann_bound']);assert eta<1
            eps=[eta/(1-eta)*max(n1(row[j])for row in Z)for j in range(m)]
            for i,row in zip(ids,Z):X[i]=row
            for i,row in enumerate(O):
                w=sum(n1(row[k])for k in ids)
                for j in range(m):errors[i][j]+=w*eps[j]
            details.append({'indices':ids,'eta':str(eta),'coordinate_errors':[str(v)for v in eps]})
    else:
        if name=='old5':R=dm(c,group['certificate']['roots'][ri]['inverse_candidate'])
        elif name=='spin7':R=Hinv
        else:R=candidate_matrix(c,group['candidate']['roots'][ri])
        proof=group['certificate']['root_certificates'][ri]if name=='spin7'else group['certificate']['roots'][ri]
        eta=Q(proof['neumann_bound']);assert eta<1
        if name=='even5':
            D=list(map(Q,group['certificate']['norm_constants']['basis_norms']))
            Z=fast_mm(c,R,[[z/D[i]for z in row]for i,row in enumerate(S)])
            X=[[z/D[i]for z in row]for i,row in enumerate(Z)]
            eps=[eta/(1-eta)*sum(n1(row[j])for row in Z)for j in range(m)]
            for i,row in enumerate(O):
                w=max(n1(z)/d for z,d in zip(row,D))
                errors[i]=[w*e for e in eps]
        else:
            X=fast_mm(c,R,S);eps=[eta/(1-eta)*max(n1(row[j])for row in X)for j in range(m)]
            for i,row in enumerate(O):errors[i]=[sum(map(n1,row))*e for e in eps]
        details.append({'eta':str(eta),'response_error_bounds':[str(v)for v in eps]})
    return ball(fast_mm(c,O,X),errors),{'dimension':n,'response_matrix_sha256':jd(sm(X)),'error_details':details}


def stage_operator(args):
    tick=time.monotonic();c=setup(args);geo,M=load_geometry(c,args);groups,owned=response_data(c,args)
    aa=[[c.C(Q(i-j,7),Q(i+j+1,11))for j in range(4)]for i in range(3)]
    bb=[[c.C(Q(2*i+j,13),Q(i-j,17))for j in range(2)]for i in range(4)]
    assert fast_mm(c,aa,bb)==mm(c,aa,bb),'Exact integer backend must match direct Gaussian Fraction arithmetic.'
    aff=json.loads((args.cache/'scalar-affine.json').read_text());maps=json.loads((args.cache/'scalar-response-maps.json').read_text())
    assert aff['complete']and aff['completed']==666 and maps['complete']
    assert aff['bindings']['native_inputs']==maps['bindings']['native_inputs']==inputs(args)
    assert maps['bindings']['owned_inputs']==owned
    import source_action_full_auxiliary_probe as full
    inherited=full.inherited_regular_controls(args.repo)
    assert groups['repair5']['certificate']['preconditioner_sha256']==owned['repair5']['records']['repair-inverse-candidates.json']
    assert groups['even5']['certificate']['preconditioner_sha256']==owned['even5']['records']['even-inverse-candidates.json']
    raw=json.loads((args.repo/'lab/process/source-action-deep-coefficients.json').read_text())
    Ts=[{(e,cl):Q(z)for e,cl,z in row}for row in raw['basis']]
    assert all(not M['Gram'][i][j]for i in range(36)for j in range(36)if i!=j)
    coeff=[[[c.C()for _ in range(36)]for _ in range(36)]for _ in range(59)]
    for row in aff['pairs']:
        i,j=row['i'],row['j']
        for a,z in enumerate(row['coefficients']):
            z=c.C(*z);coeff[a][i][j]=z/M['Gram'][i][i]
            coeff[a][j][i]=z.conj()/M['Gram'][j][j]
    Bdiag=[]
    for v in c.bs:
        signs={(-1)**(((e^cl)&15).bit_count()%2)for e,cl in v};assert len(signs)==1;Bdiag.append(signs.pop())
    for A in coeff+[M['Lgeo'],M['B']]:
        assert all(not A[i][j]or Bdiag[i]==Bdiag[j]for i in range(36)for j in range(36))
    assert all(not M['A'][i][j]or Bdiag[i]==-Bdiag[j]for i in range(36)for j in range(36))
    U,Ui=M['U'],M['Uinv'];Ut=[[z.conj()for z in row]for row in zip(*U)]
    GG=fast_mm(c,fast_mm(c,Ut,M['Gram']),U);GN=[row[20:]for row in GG[20:]]
    Bt=fast_mm(c,fast_mm(c,Ui,M['B']),U);Gt=fast_mm(c,fast_mm(c,Ui,M['Gtime']),U)
    GR=[row[:20]for row in Gt[:20]];Rids=list(range(20));Nids=list(range(20,36))
    Brr=[row[:20]for row in Bt[:20]];Brn=[row[20:]for row in Bt[:20]];Bnr=[row[:20]for row in Bt[20:]]
    ks=kernel(c,Bnr);_,ps=rref(c,Bnr);assert len(ks)==len(ps)==10
    T=[[v[i]for v in ks]+[c.C(i==j)for j in ps]for i in range(20)];Ti=inverse(c,T)
    Kcols=[list(row)for row in zip(*ks)]
    assert not any(z for row in fast_mm(c,fast_mm(c,Bnr,GR),Brn)for z in row)
    assert not any(z for row in fast_mm(c,fast_mm(c,fast_mm(c,Bnr,GR),Brr),Kcols)for z in row)
    out={'complete':False,'execution_probe_sha256':digest(__file__),'native_inputs':inputs(args),
         'inherited_authentication_helper_sha256':digest(args.repo/'tests/program-focus/source_action_full_auxiliary_probe.py'),
         'owned_response_inputs':owned,'inherited_certificate_authentication':inherited,
         'input_hashes':{name:digest(args.cache/name)for name in('scalar-geometry.json','scalar-affine.json','scalar-response-maps.json')},
         'B_reflection_full59_controls':True,'exact_integer_matrix_arithmetic_control':True,
         'all_parameter_K_invariance_static_pencil_controls':True,
         'kernel_trace_source_dimension':10,'range_adapted_T':sm(T),'roots':[],
         'scope':'Correctly composed then frozen scalar-normal highest7 operator at p, with transverse Schur correction and inherited root-box errors. Not an invariant1+1 PDE or a physical propagation theorem.'}
    for ri,root in enumerate(raw['certified_roots']):
        xs=list(map(Q,root['coordinates']));radius=Q(root['certificate']['radius'])
        C0=ma(c,eye(c,36),M['Lgeo'],*(ms(x,A)for x,A in zip(xs,coeff)))
        Cerr=[[radius*sum(n1(A[i][j])for A in coeff)for j in range(36)]for i in range(36)]
        Tfield=c.add(*(c.scale(x,v)for x,v in zip(xs,Ts)))
        for j in(0,5,12):
            native=c.add(c.bs[j],c.geo.lower(c.bs[j]),c.scale(2,c.integer.N(Tfield,c.bs[j])))
            assert c.coords(native)==[row[j]for row in C0]
        Cs=bmul(c,bmul(c,ball(Ui),ball(C0,Cerr)),ball(U))
        Crr=bpart(Cs,Rids,Rids);Crn=bpart(Cs,Rids,Nids);Cnr=bpart(Cs,Nids,Rids);Mn=bpart(Cs,Nids,Nids)
        H=fast_mm(c,GN,Mn[0]);Hinv=inverse(c,H)
        prior=groups['spin7']['certificate']['root_certificates'][ri]
        assert jd(sm(H))==prior['matrix_center_sha256']and jd(sm(Hinv))==prior['inverse_sha256']
        eta=Q(prior['neumann_bound']);assert eta<1
        Y=solve_paired7(c,Hinv,GN,ball(Bnr),eta);Z=solve_paired7(c,Hinv,GN,Cnr,eta)
        L2=bmul(c,ball(GR),bmul(c,ball(Brn),Y))
        L1=bmul(c,ball(GR),badd(c,bneg(ball(Brr)),bmul(c,ball(Brn),Z),bmul(c,Crn,Y)))
        L0old=bmul(c,ball(GR),badd(c,bneg(Crr),bmul(c,Crn,Z)))
        pieces=[];details={}
        for name,group in groups.items():
            value,info=correction_group(c,name,group,maps['groups'][name],ri,Hinv)
            pieces.append(value);details[name]=info
        Delta=badd(c,*pieces);L0=badd(c,L0old,Delta)
        transformed=[bmul(c,bmul(c,ball(Ti),L),ball(T))for L in(L2,L1,L0)]
        A2,A1,A0=transformed
        assert all(not A2[0][i][j]for i in range(20)for j in range(20)if i>=10 or j<10)
        assert all(not A1[0][i][j]for i in range(10,20)for j in range(10))
        Hlead=[[c.C()for _ in range(20)]for _ in range(20)];EH=[[Q()for _ in range(20)]for _ in range(20)]
        for i in range(20):
            for j in range(20):
                source=A1 if(i<10)==(j<10)else(A2 if i<10 else A0)
                factor=c.I if(i<10)==(j<10)else c.C(-1 if i<10 else 1)
                Hlead[i][j]=factor*source[0][i][j];EH[i][j]=source[1][i][j]
        assert not tr(A1[0]),'Exact root-center trace check for family reflection identity.'
        square=bmul(c,ball(Hlead,EH),ball(Hlead,EH));moment=tr(square[0]);error=sum(square[1][i][i]for i in range(20))
        lower=moment.a-error;upper=moment.a+error
        oldCK=bpart(bmul(c,bmul(c,ball(Ti),Delta),ball(T)),list(range(10,20)),list(range(10)))
        naive0=bmul(c,bmul(c,ball(Ti),L0old),ball(T))
        Hnaive=[list(row)for row in Hlead];EN=[list(row)for row in EH]
        for i in range(10,20):
            for j in range(10):Hnaive[i][j]=naive0[0][i][j];EN[i][j]=naive0[1][i][j]
        nsquare=bmul(c,ball(Hnaive,EN),ball(Hnaive,EN));nmoment=tr(nsquare[0]);nerror=sum(nsquare[1][i][i]for i in range(20))
        change=bmul(c,bpart(A2,list(range(10)),list(range(10,20))),oldCK)
        change_center=-2*tr(change[0]);change_error=2*sum(change[1][i][i]for i in range(10))
        assert change_center==moment-nmoment
        rr={'root':ri,'owned_root_sha256':jd(root),'radius':str(radius),'native_full_C_columns_checked':[0,5,12],
            'N7_exact_inverse_and_matrix_owned_hashes_match':True,'response_certificates':details,
            'L2':sb(L2),'L1':sb(L1),'L0':sb(L0),'L0_without_transverse_correction':sb(L0old),
            'transverse_correction':sb(Delta),'correction_CK_center_exact_zero':not any(z for row in oldCK[0]for z in row),
            'H_leading':sb(ball(Hlead,EH)),
            'trace_H_squared':{'center':moment.ser(),'l1_error':str(error),'real_lower':str(lower),'real_upper':str(upper),
                              'real_lower_float':float(lower),'real_upper_float':float(upper),'positive_certified':lower>0},
            'naive_trace_H_squared_without_transverse_correction':{'center':nmoment.ser(),'l1_error':str(nerror),
                'real_lower':str(nmoment.a-nerror),'real_upper':str(nmoment.a+nerror),
                'real_lower_float':float(nmoment.a-nerror),'real_upper_float':float(nmoment.a+nerror),
                'scope':'Descriptive comparison of the omitted geometric term; not another physical model.'},
            'transverse_correction_trace_H_squared_change':{'center':change_center.ser(),'l1_error':str(change_error),
                'real_lower':str(change_center.a-change_error),'real_upper':str(change_center.a+change_error)},
            'trace_H_exact_zero_by_full_family_B_reflection':True,
            'max_real_H_eigenvalue_strictly_above_1_over_40':lower>Q(19,80),
            'trace_lemma':'For20 eigenvalues with sum real parts0, Re tr(H^2)>=c>0 implies max Re eigenvalue>=sqrt(c/(20*19)); no diagonalizability assumed.',
            'Fourier_convention':'L(k)=-k^2 L2+i k L1+L0; diag(k I_K,I_C)^-1 L(k) diag(k I_K,I_C)/k -> H',
            'seconds':time.monotonic()-tick}
        out['roots'].append(rr);write(args.cache/'scalar-operator.json',out)
        print('SCALAR operator root',ri,'traceH2 interval',float(lower),float(upper),'positive',lower>0,'seconds',rr['seconds'],flush=True)
    out['complete']=True;out['seconds']=time.monotonic()-tick;write(args.cache/'scalar-operator.json',out)


def stage_solvable(args):
    tick=time.monotonic();c=setup(args);geo,M=load_geometry(c,args);gd=geometry_data(c);g=c.g
    extra={};Xs=[[list(row)for row in X]for X in gd.Xs]
    for a,(i,j)in zip((8,9,11),((0,1),(0,2),(1,2))):
        J=g.zero();J[i][j]=1;J[j][i]=-1;extra[a]=J
        Xs[a-4]=[[x+y for x,y in zip(row,other)]for row,other in zip(Xs[a-4],J)]
    assert all(not X[i][j]for X in Xs for i in range(4)for j in range(i))
    brackets={}
    for a in range(14):
        for b in range(14):
            row={}
            if a>=4 and b<4:row={i:Xs[a-4][i][b]for i in range(4)if Xs[a-4][i][b]}
            elif a<4 and b>=4:row={i:-Xs[b-4][i][a]for i in range(4)if Xs[b-4][i][a]}
            elif a>=4 and b>=4:
                X=g.comm(Xs[a-4],Xs[b-4])
                S=[[Q(X[i][j]+g.eta[i]*g.eta[j]*X[j][i],2)for j in range(4)]for i in range(4)]
                co=[g.vg(S,A)/g.d[k+4]for k,A in enumerate(g.A)]
                assert X==[[sum(z*A[i][j]for z,A in zip(co,Xs))for j in range(4)]for i in range(4)]
                row={k+4:z for k,z in enumerate(co)if z}
            brackets[a,b]=row
    conn=[[list(row)for row in A]for A in c.geo.gammas]
    for a,J in extra.items():
        for j in range(14):
            for i,z in g.h_action(J,j).items():conn[a][i][j]+=z
    for a in range(14):
        for b in range(14):
            for k in range(14):
                value=(brackets[a,b].get(k,0)*g.d[k]-brackets[b,k].get(a,0)*g.d[a]+brackets[k,a].get(b,0)*g.d[b])/(2*g.d[k])
                assert value==conn[a][k][b],('S Koszul mismatch',a,b,k)
    rchar=[Q()]*4+[g.trace(X)/4 for X in Xs]
    lchar=[Q()]*4+[X[3][3]for X in Xs]
    assert rchar==[Q(i==4)for i in range(14)]
    assert lchar==[Q(i==4)-3*Q(i==7)for i in range(14)]
    assert 1/g.d[3]==-1 and 1/g.d[4]+9/g.d[7]==Q(1,8)
    def delta(v):return c.add(c.K(8,c.s.rot(0,1,v)),c.K(9,c.s.rot(0,2,v)),c.K(11,c.s.rot(1,2,v)))
    checks=[];leak=None
    for i,v in enumerate(c.bs):
        direct=c.add(*(c.K(a,c.geo.rho(A,v))for a,A in enumerate(conn)))
        w=delta(v);assert direct==c.add(c.geo.lower(v),w)
        res=c.add(c.cas(w),c.scale(-56,w))
        checks.append([i,len(w),len(res)])
        if res and leak is None:
            pieces={str(j):part(c,w,j)for j in(5,6,7)}
            assert w==c.add(*pieces.values())
            leak={'basis_index':i,'delta':ser(c,w),'Casimir56_residual':ser(c,res),
                  'spin_components':{j:{'terms':len(v),'sha256':jd(ser(c,v))}for j,v in pieces.items()}}
    for row in geo['kernel_basis']:assert not c.P(delta(decode(c,row)))
    # Recompute only the four already-owned scalar-normal principal signs.
    rp=args.repo/'lab/process/source-action-receiver-strategy.json';owned=json.loads(rp.read_text())
    for name,sha in owned['sha256'].items():assert digest(args.repo/name)==sha
    ep=args.repo/'lab/process/source-action-reduced-evolution.json';ev=json.loads(ep.read_text())
    kp=args.repo/'lab/process/source-action-kappa1-constraints.json';kappa=json.loads(kp.read_text())
    N=[decode(c,row)for row in geo['kernel_basis']];energy=[]
    for ri,pr in enumerate(ev['spin7_inverse_candidates']):
        cert=kappa['exact_probe']['spin7']['root_certificates'][ri]
        assert jd(pr['inverse'])==cert['inverse_sha256']and pr['neumann_bound']==cert['neumann_bound']
        R=dm(c,pr['inverse']);eta=Q(pr['neumann_bound']);assert eta<1
        for index in(3,12):
            v=c.K(3,c.bs[index]);force=c.K(4,v)
            source=[c.C(c.E.pair({key:z.conj()for key,z in n.items()},force))for n in N]
            co=[-sum((x*z for x,z in zip(row,source)),c.C())for row in R]
            val=sum((z.conj()*w for z,w in zip(source,co)),c.C())
            er=eta/(1-eta)*max(map(n1,co));error=sum(map(n1,source))*er+abs(val.b)
            saved=next(row for row in owned['exact_probe']['normal_energy']['roots'][ri]['rows']if row['axis']==4 and row['range_basis_index']==index)
            assert jd(ser(c,v))==saved['range_sha256']and jd(ser(c,force))==saved['force_sha256']
            assert [[i,z.ser()]for i,z in enumerate(source)if z]==saved['source_coordinates']
            assert(str(val.a),str(error),str(val.a-error),str(val.a+error))==tuple(saved[k]for k in('center','error_bound','lower','upper'))
            assert (val.a+error<0 if saved['sign']=='negative'else val.a-error>0)
            energy.append({'root':ri,'range_basis_index':index,'sign':saved['sign'],'lower':saved['lower'],'upper':saved['upper'],
                           'exact_owned_interval_recomputed':True})
    out={'complete':True,'execution_probe_sha256':digest(__file__),'native_inputs':inputs(args),
         'additional_inputs':{str(p.relative_to(args.repo)):digest(p)for p in(rp,ep,kp)},
         'S_affine_basis_dimension':14,'ordered_brackets_closed':196,'exact_Koszul_entries_checked':14**3,
         'generators':[[[str(z)for z in row]for row in X]for X in Xs],
         'r_character':[str(z)for z in rchar],'log_lambda_character':[str(z)for z in lchar],
         'du_squared_norm_coefficients':['-1','0','1/8'],
         'extra_lower_identity_all36':checks,'extra_NN_zero_controls':16,'spin7_leak':leak,
         'owned_axis4_energy_sign_replay':energy,
         'reduced_equation':'[K3-u(K4-3K7)] q_u+K4 q_r+C0S q=0 on the full carrier',
         'scope':'Exact native S subgroup/connection/profile controls and four inherited principal-energy intervals. No spin7 closed S ansatz, physical-state admission, global norm, nonlinear or GU verdict.',
         'seconds':time.monotonic()-tick}
    write(args.cache/'scalar-solvable-controls.json',out);print('SCALAR S CONTROLS PASS seconds',out['seconds'],'spin7 leak',None if leak is None else leak['basis_index'],flush=True)


RECORDS=('scalar-geometry.json','scalar-affine.json','scalar-response-maps.json',
         'scalar-operator.json','scalar-solvable-controls.json')
BUNDLE='source-action-scalar-normal-operator-certificates.json'


def encode_record(path):
    import base64,zlib
    raw=path.read_bytes();json.loads(raw)
    return {'encoding':'zlib-base64-json','sha256':hashlib.sha256(raw).hexdigest(),
            'uncompressed_bytes':len(raw),'data':base64.b64encode(zlib.compress(raw,9)).decode()}


def stage_bundle(args):
    values={name:json.loads((args.cache/name).read_text())for name in RECORDS}
    assert all(d['complete']for d in values.values())
    for name in('scalar-operator.json','scalar-solvable-controls.json'):
        assert values[name]['execution_probe_sha256']==digest(__file__)
    op=values['scalar-operator.json'];sol=values['scalar-solvable-controls.json']
    assert all(r['trace_H_squared']['positive_certified']and r['max_real_H_eigenvalue_strictly_above_1_over_40']for r in op['roots'])
    assert len(sol['owned_axis4_energy_sign_replay'])==4 and sol['spin7_leak']is not None
    for name,sha in op['input_hashes'].items():assert digest(args.cache/name)==sha
    out={'schema':'gu-scalar-normal-operator-certificates-v1','data_only':True,
         'final_probe_sha256':digest(__file__),'native_inputs':inputs(args),
         'records':{name:encode_record(args.cache/name)for name in RECORDS},
         'scope':'Corrected frozen highest7 range operator, positive-real high-frequency limit certificate at both held roots, exact full-carrier solvable-profile controls and four inherited energy intervals. Frozen growth is not a PDE estimate, physical instability or GU verdict.'}
    path=args.repo/'lab/process'/BUNDLE;write(path,out);assert path.stat().st_size<45_000_000
    print('SCALAR BUNDLE',len(RECORDS),'records bytes',path.stat().st_size,flush=True)


def restore(args,copy):
    import base64,zlib
    path=args.repo/'lab/process'/BUNDLE;d=json.loads(path.read_text())
    assert d['schema']=='gu-scalar-normal-operator-certificates-v1'and d['data_only']
    assert d['final_probe_sha256']==digest(__file__)and d['native_inputs']==inputs(args)
    assert set(d['records'])==set(RECORDS)
    for name,r in d['records'].items():
        assert r['encoding']=='zlib-base64-json';raw=zlib.decompress(base64.b64decode(r['data']))
        assert len(raw)==r['uncompressed_bytes']and hashlib.sha256(raw).hexdigest()==r['sha256']
        if copy:(args.cache/name).write_bytes(raw)
        else:assert(args.cache/name).read_bytes()==raw
    return d


def stage_unpack(args):restore(args,True);print('SCALAR UNPACK',len(RECORDS),'authenticated records',flush=True)


def mathematical(d):
    if isinstance(d,dict):return {k:mathematical(v)for k,v in d.items()if k not in('seconds','last_batch_seconds','execution_probe_sha256')}
    if isinstance(d,list):return [mathematical(v)for v in d]
    return d


def stage_replay(args):
    import tempfile
    tick=time.monotonic();bundle=restore(args,False)
    child=SimpleNamespace(**vars(args));child.cache=Path(tempfile.mkdtemp(prefix='recomputed-',dir=args.cache));child.steps=0
    stages=(stage_geometry,stage_affine,stage_maps,stage_operator,stage_solvable)
    checks=[]
    for name,stage in zip(RECORDS,stages):
        stage(child)
        old=json.loads((args.cache/name).read_text());new=json.loads((child.cache/name).read_text())
        assert mathematical(old)==mathematical(new),('Native mathematical replay mismatch',name)
        # Downstream procedures bind original bytes, including historical metadata.
        (child.cache/name).write_bytes((args.cache/name).read_bytes())
        checks.append(name);print('SCALAR REPLAY mathematical match',name,flush=True)
    restore(args,False)
    receipt={'passed':True,'probe_sha256':digest(__file__),'bundle_sha256':digest(args.repo/'lab/process'/BUNDLE),
             'all_five_mathematical_records_recomputed':checks,'native_geometry_vectors':36,
             'native_derivative_Casimir_checks':180,'all59_affine_trilinear_pairs_recomputed':666,
             'native_response_output_columns_recomputed':624,'native_full_C_columns_recomputed_at_both_roots':6,
             'exact_corrected20_operator_and_root_error_arithmetic_recomputed':True,
             'all_S_Koszul_entries_recomputed':2744,'owned_energy_intervals_recomputed':4,
             'inherited_M_inverse_certificates_authenticated_not_regenerated':True,
             'floating_inverse_regenerated':False,'seconds':time.monotonic()-tick,
             'scope':'Full reproduction of this bounded native operator/control calculation; inherited auxiliary inverses are authenticated. No PDE growth transfer or physical verdict.'}
    write(args.output or args.cache/'scalar-replay.json',receipt)
    print('SCALAR REPLAY PASS seconds',receipt['seconds'],flush=True)


def stage_status(args):
    d=restore(args,False);op=json.loads((args.cache/'scalar-operator.json').read_text())
    sol=json.loads((args.cache/'scalar-solvable-controls.json').read_text())
    out={'probe_sha256':digest(__file__),'bundle_sha256':digest(args.repo/'lab/process'/BUNDLE),
         'all_records_authenticated':True,'both_roots_positive_trace_moment':all(r['trace_H_squared']['positive_certified']for r in op['roots']),
         'both_roots_max_real_H_eigenvalue_above_1_over_40':all(r['max_real_H_eigenvalue_strictly_above_1_over_40']for r in op['roots']),
         'S_controls_complete':sol['complete'],'root_moment_intervals':[r['trace_H_squared']for r in op['roots']],
         'scope':'Authentication/status only; replay performs native recomputation.'}
    if args.output:write(args.output,out)
    print('SCALAR STATUS PASS',out['both_roots_positive_trace_moment'],flush=True)


def stage_finalize(args):
    stage_operator(args);stage_solvable(args);stage_bundle(args)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2])
    ap.add_argument('--cache',type=Path,required=True)
    ap.add_argument('--mode',choices=['geometry','affine','maps','operator','solvable','finalize','bundle','unpack','replay','status'],default='geometry')
    ap.add_argument('--steps',type=int,default=32)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args();args.repo=args.repo.resolve();args.cache=args.cache.resolve();args.cache.mkdir(parents=True,exist_ok=True)
    assert Path(__file__).resolve().parents[2]==args.repo,'Do not mix checkout namespaces.'
    {'geometry':stage_geometry,'affine':stage_affine,'maps':stage_maps,'operator':stage_operator,'solvable':stage_solvable,
     'finalize':stage_finalize,'bundle':stage_bundle,'unpack':stage_unpack,'replay':stage_replay,'status':stage_status}[args.mode](args)


if __name__=='__main__':main()
