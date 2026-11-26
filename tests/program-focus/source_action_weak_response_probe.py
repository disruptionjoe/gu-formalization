"""Reproducible native weak-response diagnostics and exact finite certificates.

Default --domain runs only the244 inexpensive finite controls. Heavy stages are
explicit and serialized by the caller. All inputs/outputs are in --repo/--cache;
no scratch Python code is executed or imported. NumPy/SciPy are optional except
for numerical discovery/certification/matched modes. Restrict BLAS threads to1.

To replay recorded certificates, use --unpack --cache <empty-directory>, then
--certify, --gram and --exact. --closure requires a fresh cache/version binding.

Suggested fresh sequence:
  --seeds --steps 0 ; --numeric --steps 20 ; --basis ; --closure ; --certify
  --matched --save-kernels <cache>/kernels.npz
  --targets --input <cache>/kernels.npz ; --exact
The numerical modes produce candidates, not certificates. --closure certifies
only the exact discovered invariant subspace, not the full auxiliary operator.
--certify checks exact rational residuals over the existing certified root balls.
--matched alone remains a numerical pointwise kernel diagnostic, not a physical
or integrated-response certificate. Domain/CK and the conditional SO3 reduction
are written proofs with separate premises, not established by these controls.

Legacy completed closure records can be READ by --certify after explicit source
and native-input validation. They cannot be silently resumed by --closure under
a different implementation binding. Use a fresh cache for a new closure run.
"""
from pathlib import Path
from fractions import Fraction as Q
from types import SimpleNamespace
from functools import lru_cache
import argparse,json,sys,time,hashlib,subprocess,inspect,textwrap

FAST_EXACT_LEGACY_FILE_SHA256 = '8e4d68589fd89c5738bd58003b6c4fdd20c5ec24aa06f02fee18e1666bfdfa2f'
FAST_EXACT_CLASS_SHA256 = 'fd8310be94007a79216c12e4f5bc00b6b269a394ea52f84978e9a03e217ffdf4'
NATIVE_BINDING_PATHS = [
    'tests/program-focus/source_action_deep_algebra.py',
    'tests/program-focus/source_action_deep_geometry.py',
    'tests/program-focus/source_action_paired_response_probe.py',
    'tests/program-focus/source_action_metric_symbol_probe.py',
    'tests/program-focus/source_action_physical_probe.py',
    'tests/program-focus/source_action_slice_completion_probe.py',
    'tests/program-focus/source_action_reduced_evolution_probe.py',
    'tests/program-focus/source_action_kappa1_constraints_probe.py',
    'tests/program-focus/source_action_coupled_ghost_probe.py',
    'lab/process/source-action-kappa1-constraints.json',
    'lab/process/source-action-reduced-evolution.json',
]

def configure(repo):
    global g,Engine,add,scale,C,I,build_api,symbols,p,column
    sys.path.insert(0,str(repo/'tests/program-focus'))
    import source_action_deep_geometry as g
    import source_action_paired_response_probe as p
    from source_action_slice_completion_probe import column
    from source_action_deep_algebra import Engine,add,scale
    from source_action_paired_response_probe import C,I,build_api
    from source_action_metric_symbol_probe import symbols

def file_digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def native_bindings(repo):
    return {p:file_digest(repo/p) for p in NATIVE_BINDING_PATHS}

def fast_class_digest():
    cls=_fast_exact_class()
    source=textwrap.dedent(inspect.getsource(cls)).rstrip()+'\n'
    got=hashlib.sha256(source.encode()).hexdigest()
    assert got==FAST_EXACT_CLASS_SHA256, 'Embedded FastExact changed; update proof/checkpoint binding deliberately.'
    return got

def current_closure_bindings(args,basispath):
    return {'implementation_format':'integrated-v2',
            'basis_sha256':file_digest(basispath),
            'background_sha256':file_digest(args.root/'lab/process/source-action-deep-coefficients.json'),
            'fast_exact_class_sha256':fast_class_digest(),
            'native_inputs':native_bindings(args.root),
            'source_revision':subprocess.check_output(['git','rev-parse','HEAD'],cwd=args.root,text=True).strip()}

def validate_closure_bindings(cl,args,basispath):
    b=cl.get('bindings',{});now=current_closure_bindings(args,basispath)
    assert b.get('basis_sha256')==now['basis_sha256'],'Closure basis digest differs'
    assert b.get('background_sha256')==now['background_sha256'],'Closure background digest differs'
    if b.get('implementation_format')=='integrated-v2':
        assert b.get('fast_exact_class_sha256')==now['fast_exact_class_sha256']
        assert b.get('native_inputs')==now['native_inputs']
        return {'format':'integrated-v2','recorded_source_revision':b.get('source_revision'),'current_inputs_equal':True}
    assert b.get('fast_exact_sha256')==FAST_EXACT_LEGACY_FILE_SHA256,'Unrecognized legacy exact engine'
    revision=b.get('source_revision');assert revision
    for rel,digest in now['native_inputs'].items():
        old=subprocess.check_output(['git','show',revision+':'+rel],cwd=args.root)
        assert hashlib.sha256(old).hexdigest()==digest,('Legacy native dependency changed',rel)
    return {'format':'legacy-v1-explicit-read-only','recorded_source_revision':revision,
            'legacy_fast_file_sha256':FAST_EXACT_LEGACY_FILE_SHA256,
            'embedded_class_sha256':now['fast_exact_class_sha256'],
            'native_input_equality':list(now['native_inputs']),
            'note':'Original file hash is provenance; it is not claimed to hash this integrated file.'}



def _fast_exact_class():
    from source_action_deep_algebra import Engine,add,scale
    class FastExact(Engine):
     def __init__(self,geometry):
      super().__init__(geometry)
      assert self.dim==14 and self.negative==5
      assert self.d==tuple(map(Q,[1,1,1,-1,-16,8,24,48,8,8,-8,8,-8,-8]))
     def Phi(self,X):
      components=self.split_two(X);out=[{}for _ in range(self.dim)];Z={}
      for(i,j),x in components.items():
       gi={1<<i:Q(1)};gj={1<<j:Q(1)};gij={(1<<i)|(1<<j):Q(1)}
       out[j]=add(out[j],scale(-1/self.d[i],self.cliff_product(gi,x,'comm')))
       out[i]=add(out[i],scale(1/self.d[j],self.cliff_product(gj,x,'comm')))
       Z=add(Z,scale(1/(self.d[i]*self.d[j]),self.cliff_product(gij,x,'anti')))
      for j in range(self.dim):out[j]=add(out[j],scale(-Q(1,2),self.cliff_product({1<<j:Q(1)},Z,'anti')))
      return {(1<<j,c):v for j,x in enumerate(out)for c,v in x.items()if v}
     def Phi_adj(self,V):
      vs=self.split_one(V);A={}
      for i,x in vs.items():A=add(A,scale(1/self.d[i],self.cliff_product({1<<i:Q(1)},x,'anti')))
      out={}
      for i in range(self.dim):
       for j in range(i+1,self.dim):
        w=add(self.cliff_product({1<<i:Q(1)},vs.get(j,{}),'comm'),scale(-1,self.cliff_product({1<<j:Q(1)},vs.get(i,{}),'comm')),scale(-Q(1,2),self.cliff_product({(1<<i)|(1<<j):Q(1)},A,'anti')))
        for c,v in w.items():out[(1<<i)|(1<<j),c]=v
      return out
     def wadj(self,U,W):
      us=self.split_one(U);ws=self.split_two(W);out=[{}for _ in range(self.dim)]
      for(i,j),w in ws.items():
       out[j]=add(out[j],scale(-1/self.d[i],self.cliff_product(us.get(i,{}),w,'comm')))
       out[i]=add(out[i],scale(1/self.d[j],self.cliff_product(us.get(j,{}),w,'comm')))
      return {(1<<j,c):v for j,x in enumerate(out)for c,v in x.items()if v}
     def N(self,U,V):
      return scale(Q(1,6),add(self.Phi(self.wedge(U,V,'comm')),self.wadj(U,self.Phi_adj(V)),self.wadj(V,self.Phi_adj(U))))
    return FastExact


def _dense_class():
    import numpy as np
    from math import sqrt
    class DenseNative:
     def __init__(self,d):
      self.d=np.asarray(d,dtype=float);self.n=len(d);assert self.n==14
      self.dim=128;self.ncl=16384;self.bs=np.arange(128);self.ms=np.arange(16384)
      self.x=np.zeros(16384,dtype=int);self.z=self.x.copy();self.phase=np.ones(16384,dtype=complex)
      self.gamma=[]
      for i in range(14):
       j=i//2;x=1<<j;z=(1<<j)-1
       c=sqrt(abs(d[i]))*(1j if d[i]<0 else 1)
       if i%2:z|=1<<j;c*=1j
       self.gamma.append((x,z,c))
      for mask in range(1,16384):
       bit=mask.bit_length()-1;prev=mask^(1<<bit);x,z,c=self.gamma[bit]
       self.phase[mask]=self.phase[prev]*c*((-1)**int(int(self.z[prev]&x).bit_count()))
       self.x[mask]=self.x[prev]^x;self.z[mask]=self.z[prev]^z
      self.pidx=self.x*128+self.z
      assert len(set(self.pidx))==16384
      self.row=np.bitwise_xor(np.arange(128)[:,None],self.bs[None,:])
      self.col=np.broadcast_to(self.bs[None,:],(128,128))
      self.gm=[self.pauli(x,z,c)for x,z,c in self.gamma]
      self.pairs=[(i,j)for i in range(14)for j in range(i+1,14)]
      self.gij={(i,j):self.gm[i]@self.gm[j]for i,j in self.pairs}
     def pauli(self,x,z,c):
      m=np.zeros((128,128),complex);m[self.bs^x,self.bs]=[c*(-1)**int(int(z&b).bit_count())for b in self.bs];return m
     def fwht(self,f):
      f=np.array(f,copy=True);h=1
      while h<128:
       g=f.reshape(*f.shape[:-1],-1,2*h);a=g[...,:h].copy();b=g[...,h:].copy();g[...,:h]=a+b;g[...,h:]=a-b;h*=2
      return f
     def to_matrix(self,a):
      a=np.asarray(a);flat=np.zeros(a.shape[:-1]+(16384,),complex);flat[...,self.pidx]=a*self.phase
      vals=self.fwht(flat.reshape(a.shape[:-1]+(128,128)))
      out=np.empty_like(vals);out[...,self.row,self.col]=vals;return out
     def from_matrix(self,m):
      a=self.fwht(m[...,self.row,self.col])/128
      return a.reshape(m.shape[:-2]+(16384,))[...,self.pidx]/self.phase
     def sparse_to_array(self,v):
      a=np.zeros((14,16384),complex)
      for(e,c),z in v.items():a[e.bit_length()-1,c]=z
      return a
     def array_to_sparse(self,a,relative=1e-12):
      w=np.abs(self.phase)[None,:]/np.sqrt(np.abs(self.d))[:,None]
      z=np.abs(a)*w;threshold=z.max()*relative
      ii,jj=np.nonzero(z>threshold)
      return {(1<<int(i),int(j)):complex(a[i,j])for i,j in zip(ii,jj)}
     def comm(self,a,b):return a@b-b@a
     def anti(self,a,b):return a@b+b@a
     def phi(self,W):
      # W shape91x128x128, ordered pairs i<j. First term contracts commutator.
      out=np.zeros((14,128,128),complex);Z=np.zeros((128,128),complex)
      for k,(i,j)in enumerate(self.pairs):
       out[j]-=self.comm(self.gm[i],W[k])/self.d[i]
       out[i]+=self.comm(self.gm[j],W[k])/self.d[j]
       Z+=self.anti(self.gij[i,j],W[k])/(self.d[i]*self.d[j])
      for j in range(14):out[j]-=.5*self.anti(self.gm[j],Z)
      return out
     def phi_adj(self,V):
      A=sum((self.anti(self.gm[i],V[i])/self.d[i]for i in range(14)),start=np.zeros((128,128),complex))
      return np.asarray([self.comm(self.gm[i],V[j])-self.comm(self.gm[j],V[i])-.5*self.anti(self.gij[i,j],A)for i,j in self.pairs])
     def wadj(self,U,W):
      out=np.zeros((14,128,128),complex)
      for k,(i,j)in enumerate(self.pairs):
       out[j]-=self.comm(U[i],W[k])/self.d[i]
       out[i]+=self.comm(U[j],W[k])/self.d[j]
      return out
     def N(self,T,V,adjT=None):
      W=np.asarray([self.comm(T[i],V[j])-self.comm(T[j],V[i])for i,j in self.pairs])
      return (self.phi(W)+self.wadj(T,self.phi_adj(V))+self.wadj(V,self.phi_adj(T)if adjT is None else adjT))/6

    return DenseNative


def build_seed_context(args,numeric=False):
    E=Engine(g)
    def rot(i,j,x):
     H=g.zero();H[i][j]=Q(1);H[j][i]=Q(-1)
     act=[g.h_action(H,a)for a in range(14)];sp={}
     for a in range(14):
      for b in range(a+1,14):
       z=act[b].get(a,Q(0))/(2*g.d[b])
       if z:sp[(1<<a)|(1<<b)]=z
     out={}
     for(e,c),v in x.items():
      ai=e.bit_length()-1
      for b in range(14):
       z=-act[b].get(ai,Q(0))
       if z:out[1<<b,c]=out.get((1<<b,c),0)+v*z
      for cc,z in E.cliff_product(sp,{c:Q(1)},'comm').items():out[e,cc]=out.get((e,cc),0)+v*z
     return {k:v for k,v in out.items()if v}
    start=time.monotonic();poly={0:C(1)}
    for a,b in[(0,1),(10,12),(9,11),(5,8)]:poly=E.cliff_product(poly,{1<<a:C(1),1<<b:I})
    bs=[]
    for mask in range(64):
     z=[a for j,a in enumerate([2,3,4,6,7,13])if mask>>j&1]
     if(4+len(z))%4 not in(0,3):continue
     c=poly
     for a in z:c=E.cliff_product(c,{1<<a:C(1)})
     v={(1<<a,k):f*x for a,f in[(5,C(1)),(8,I)]for k,x in c.items()};v=scale(1/v[min(v)],v);bs.append(v)
    h=SimpleNamespace(bs=bs,I=I,rot=rot);ctx={'C':C,'E':E,'h':h};q=build_api(args.root,ctx)
    seeds=[q['spin5'](q['P'](q['K'](5,q['K'](3,bs[j]))))for j in(5,12)]
    assert all(seeds)
    for s in seeds:assert q['P'](s)==s and not q['K'](3,s) and q['cas'](s)==scale(30,s)
    print('exact seeds ready',len(bs),[len(s)for s in seeds],'seconds',time.monotonic()-start,flush=True)
    ctxout=SimpleNamespace(E=E,rot=rot,bs=bs,h=h,q=q,seeds=seeds,start=start)
    if not numeric:return ctxout
    class FloatEngine(Engine):
     def __init__(self):
      super().__init__(g);self.d=tuple(map(float,self.d));self.volume=float(self.volume)
      self.phi1={k:float(v)for k,v in self.phi1.items()};self.phi2={k:float(v)for k,v in self.phi2.items()}
     @lru_cache(maxsize=16384)
     def dprod(self,mask):
      result=1.
      while mask:
       low=mask&-mask;result*=self.d[low.bit_length()-1];mask-=low
      return result
    F=FloatEngine()
    def num(z):return complex(float(z.a),float(z.b))if isinstance(z,C)else complex(z)
    def tofloat(v):return {k:num(x)for k,x in v.items()}
    import numpy as np
    @lru_cache(maxsize=None)
    def pblock(r):
     zz,gi=q['block'](r);keys=[(1<<i,(1<<i)^r^z)for z in(0,8)for i in range(14)]
     Z=np.array([[float(v.get(k,0))for v in zz]for k in keys]);G=np.array([[float(v)for v in row]for row in gi]);w=np.array([float(E.weight(*k))for k in keys]);return keys,(Z@G@Z.T)*w

    def project(v):
     groups={}
     for(e,c),x in v.items():groups.setdefault((e^c)&~8,{})[e,c]=x
     out={}
     for r,w in groups.items():
      keys,P=pblock(r);a=P@np.array([w.get(k,0j)for k in keys])
      for k,x in zip(keys,a):
       if x:out[k]=complex(x)
     return out

    def clean_scaled(v,tol=1e-13):
     if not v:return v
     n=max(abs(z)*abs(float(E.weight(*k)))**.5 for k,z in v.items())
     return {k:z for k,z in v.items()if abs(z)*abs(float(E.weight(*k)))**.5>tol*n}

    def norm(v):return float(sum(abs(z)**2*abs(float(E.weight(*k)))for k,z in v.items())**.5)
    def matvec(T,v):return clean_scaled(add(v,scale(2.,project(F.N(T,v)))))

    ctxout.F=F;ctxout.num=num;ctxout.tofloat=tofloat;ctxout.pblock=pblock;ctxout.project=project;ctxout.norm=norm;ctxout.matvec=matvec
    return ctxout


def mode_seeds(args):
    s=build_seed_context(args,True)
    E,rot,bs,h,q,seeds,start=s.E,s.rot,s.bs,s.h,s.q,s.seeds,s.start
    F,num,tofloat,pblock,project,norm,matvec=s.F,s.num,s.tofloat,s.pblock,s.project,s.norm,s.matvec
    D=json.loads((args.root/'lab/process/source-action-deep-coefficients.json').read_text())
    out={'scope':'NUMERICAL_DIAGNOSTIC_ONLY pointwise actual M=I+2PN(T); not full weak response, inverse certificate or physical quantity','exact_seeds':[[[e,c,C(z).ser()]for(e,c),z in s.items()]for s in seeds],'root_results':[]}
    for ri,root in enumerate(D['certified_roots']):
     T={}
     for x,row in zip(root['coordinates'],D['basis']):
      for e,c,v in row:T[e,c]=T.get((e,c),0.)+float(x)*float(Q(v))
     T={k:v for k,v in T.items()if v};s=tofloat(seeds[0]);v=s
     rr={'root':ri,'T_terms':len(T),'seed_norm':norm(s),'steps':[]}
     for i in range(args.steps):
      t=time.monotonic();w=matvec(T,v);rr['steps'].append({'step':i+1,'input_terms':len(v),'output_terms':len(w),'output_norm':norm(w),'seconds':time.monotonic()-t,'P_cached_blocks':pblock.cache_info().currsize});print('root',ri,rr['steps'][-1],flush=True);v=w
     rr['last_vector']=[[e,c,z.real,z.imag]for(e,c),z in sorted(v.items())];out['root_results'].append(rr);args.output.write_text(json.dumps(out,indent=2))
    print('DONE',time.monotonic()-start,flush=True)


def mode_domain(args):
    from source_action_paired_response_probe import C,I,vertex
    from source_action_slice_completion_probe import column,inject,covector,sigma,inverse,readout,vscale

    def mm(a,b):
        return [[sum((a[i][k]*b[k][j] for k in range(len(b))),C(0)) for j in range(len(b[0]))]for i in range(len(a))]
    def adj(a):return [[a[j][i].conj()for j in range(len(a))]for i in range(len(a[0]))]
    def inverse2(a):
        det=a[0][0]*a[1][1]-a[0][1]*a[1][0]
        return [[a[1][1]/det,-a[0][1]/det],[-a[1][0]/det,a[0][0]/det]]
    def herm(a):
        ah=adj(a);return [[(a[i][j]+ah[i][j])/2 for j in range(2)]for i in range(2)]
    def run():
        checks=0
        # Actual full15-slot vertex identity, not only scalar-column example.
        for axis in range(14):
            u={(1<<axis,0):I};xi=covector(axis)
            for j in range(15):
                assert vertex(u,column(j))==vscale(I,sigma(xi,column(j)));checks+=1
        # On the old hypersurface V=q At^-1, so V At J=Id.
        for j in range(5):
            assert readout(inverse(covector(3),sigma(covector(3),inject(j))))==readout(inject(j));checks+=1
        assert I*I==C(-1);checks+=1
        # Finite controls for non-Hermitian N and the safe2/(9Vol) bound.
        examples=[[[C(Q(1,4)),C(0)],[C(0),C(-Q(1,4))]],
                  [[C(0,Q(1,4)),C(0)],[C(0),C(0,-Q(1,4))]],
                  [[C(0),C(Q(1,4))],[C(0),C(0)]],
                  [[C(0),C(0,Q(1,4))],[C(Q(1,4)),C(0)]]]
        for e in examples:
            f2=sum(z.a*z.a+z.b*z.b for row in e for z in row)
            assert f2<Q(1,4);checks+=1
            for vol in [Q(1,3),Q(1),Q(2)]:
                n=[[vol*(e[i][j]+(1 if i==j else 0))for j in range(2)]for i in range(2)]
                ni=inverse2(n);h=herm(ni)
                b=[[h[i][j]-Q(2,9)/vol*(1 if i==j else 0)for j in range(2)]for i in range(2)]
                assert b[0][0].b==0 and b[1][1].b==0 and b[0][0].a>0
                det=b[0][0]*b[1][1]-b[0][1]*b[1][0]
                assert det.b==0 and det.a>0;checks+=1
                # Mutation: missing the inherited old-row i flips/erases realcurrent.
                assert (I*I).a==-1 and (C(1)*I).a==0;checks+=1
        return {'checks':checks,'actual_vertex_columns':210,'old_readout_inverse_controls':5,
                'gram_examples':12,'raw_current_second_derivative_sign':'negative for nonzero same-band amplitude',
                'scope':'finite algebra only; domain mismatch and compact-parameter CK proof are written'}

    result=run()
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


def mode_numeric(args):
    import numpy as np
    s=build_seed_context(args,True)
    E,rot,bs,h,q,seeds,start=s.E,s.rot,s.bs,s.h,s.q,s.seeds,s.start
    F,num,tofloat,pblock,project,norm,matvec=s.F,s.num,s.tofloat,s.pblock,s.project,s.norm,s.matvec
    from scipy.sparse.linalg import LinearOperator,gmres
    D=json.loads((args.root/'lab/process/source-action-deep-coefficients.json').read_text())
    dense=_dense_class()(list(map(float,g.d)))
    def errdict(a,b):return norm(add(a,scale(-1,b)))/max(1.,norm(a),norm(b))
    # Owned sparse vs derived dense controls BEFORE using faster action.
    controls=[]
    sample={(1,0):1.,(8,7):.3j,(32,31):-.4}
    control={(2,3):.6,(16,0):1j,(256,15):.7}
    back=dense.array_to_sparse(dense.from_matrix(dense.to_matrix(dense.sparse_to_array(sample))))
    controls.append(('clifford_roundtrip',errdict(sample,back)))
    for T,V in[(sample,control),(control,sample)]:
     raw=dense.from_matrix(dense.N(dense.to_matrix(dense.sparse_to_array(T)),dense.to_matrix(dense.sparse_to_array(V))))
     got=dense.array_to_sparse(raw);native=F.N(T,V);controls.append(('native_N_crosscheck',errdict(native,got)))
    assert all(e<1e-10 for _,e in controls),controls
    # Every Clifford blade uses a bijective Pauli label; test all16384 coefficient
    # positions simultaneously with distinct bounded values, plus generator algebra.
    all_coeff=(np.arange(16384)%97-48)/49+1j*(np.arange(16384)%31-15)/17
    rt=dense.from_matrix(dense.to_matrix(all_coeff));allerr=float(np.max(np.abs(rt-all_coeff)))
    assert allerr<1e-10;controls.append(('all16384_clifford_roundtrip',allerr))
    ident=np.eye(128)
    for a in range(14):
     for b in range(14):
      lhs=dense.gm[a]@dense.gm[b]+dense.gm[b]@dense.gm[a]
      expected=2*dense.d[a]*ident if a==b else np.zeros_like(ident)
      assert np.max(np.abs(lhs-expected))<1e-10
    controls.append(('all196_clifford_generator_relations',0.0))
    for a,b in [(0,1),(1,2),(3,31),(255,1024),(8191,16383),(16382,17)]:
     ca=np.zeros(16384,complex);cb=np.zeros(16384,complex);ca[a]=1;cb[b]=1
     prod=dense.from_matrix(dense.to_matrix(ca)@dense.to_matrix(cb));c,v=E.cmul(a,b)
     expected=np.zeros(16384,complex);expected[c]=float(v)
     assert np.max(np.abs(prod-expected))/max(1,abs(float(v)))<1e-10
    controls.append(('six_composite_blade_products',0.0))
    print('dense controls PASS',controls,flush=True)
    weights=np.abs(dense.phase)[None,:]/np.sqrt(np.abs(dense.d))[:,None]
    source=dense.sparse_to_array(tofloat(seeds[0]));rhs=(source*weights).reshape(-1)
    source_scale=np.linalg.norm(rhs);rhs=rhs/source_scale
    out={'scope':'NUMERICAL_CANDIDATE_ONLY. Actual pointwise root-center M; no exact inverse/rootball certificate, full weak scalar or physical quantity. Small roundoff coefficient pruning remains a diagnostic implementation choice.','controls':controls,'roots':[]}
    for ri,r in enumerate(D['certified_roots']):
     T={}
     for x,row in zip(r['coordinates'],D['basis']):
      for e,c,v in row:T[e,c]=T.get((e,c),0.)+float(x)*float(Q(v))
     T={k:v for k,v in T.items()if v};TM=dense.to_matrix(dense.sparse_to_array(T));adjT=dense.phi_adj(TM)
     calls=0;times=[]
     def mv(v):
      nonlocal calls
      t=time.monotonic();a=v.reshape(14,16384)/weights
      n=dense.from_matrix(dense.N(TM,dense.to_matrix(a),adjT))
      ns=dense.array_to_sparse(n,relative=1e-13)
      pn=project(ns);outarr=a+2*dense.sparse_to_array(pn)
      calls+=1;times.append(time.monotonic()-t)
      if calls%5==1:print('root',ri,'matvec',calls,'Nterms',len(ns),'seconds',times[-1],flush=True)
      return (outarr*weights).reshape(-1)
     # First action validates direct sparse stage1 where its stored result exists.
     first=mv(rhs)*source_scale
     old=args.cache/'inverse-stage1.json'
     if old.exists() and len(json.loads(old.read_text())['root_results'][ri].get('steps',[]))==1:
      prior=json.loads(old.read_text())['root_results'][ri]['last_vector'];z={(e,c):complex(re,im)for e,c,re,im in prior};got=dense.array_to_sparse(first.reshape(14,16384)/weights);check=errdict(z,got);print('fullroot sparse/dense M check',ri,check,flush=True);assert check<1e-9
     residual_history=[]
     def cb(x):
      residual_history.append(float(x))
      if len(residual_history)%5==0:print('root',ri,'GMRES',len(residual_history),'relative',x,flush=True)
     L=LinearOperator((len(rhs),len(rhs)),matvec=mv,dtype=np.complex128)
     x,info=gmres(L,rhs,rtol=1e-10,atol=0.,restart=30,maxiter=args.steps,callback=cb,callback_type='pr_norm')
     res=mv(x)-rhs;Y=x.reshape(14,16384)/weights*source_scale
     ys=dense.array_to_sparse(Y,relative=1e-12)
     rr={'root':ri,'info':int(info),'relative_residual':float(np.linalg.norm(res)),'solution_weighted_norm':float(np.linalg.norm(x)*source_scale),'matvec_calls':calls,'matvec_seconds':times,'residual_history':residual_history,'solution':[[e,c,z.real,z.imag]for(e,c),z in sorted(ys.items())],'source_index':0,'rootball_certified':False}
     out['roots'].append(rr);args.output.write_text(json.dumps(out,indent=2));print('rootDONE',ri,'res',rr['relative_residual'],'terms',len(ys),flush=True)
    print('DONE',flush=True)


def mode_basis(args):
    s=build_seed_context(args,False)
    E,rot,bs,h,q,seeds,start=s.E,s.rot,s.bs,s.h,s.q,s.seeds,s.start
    D=json.loads((args.cache/'inverse-stage2.json').read_text())
    keys=sorted({(e,c)for r in D['roots']for e,c,re,im in r['solution']})
    print('raw support',len(keys),flush=True)
    # Exact sparse column elimination with relations; no floating rank decisions.
    piv={};basis=[];kernels=[]
    for index,key in enumerate(keys):
     unit={key:Q(1)}
     w=add(rot(0,1,unit),scale(-5*I,unit));raising=add(rot(0,2,unit),scale(I,rot(1,2,unit)));kt=q['K'](3,unit)
     v={(tag,e,c):C(x)for tag,u in enumerate((kt,w,raising))for(e,c),x in u.items()};cs={index:C(1)}
     while v:
      p=min(v)
      if p not in piv:
       z=v[p];v={k:x/z for k,x in v.items()};cs={k:x/z for k,x in cs.items()};piv[p]=len(basis);basis.append((v,cs));break
      b,bc=basis[piv[p]];z=v[p]
      for k,x in b.items():
       y=v.get(k,C())-z*x
       if y:v[k]=y
       elif k in v:del v[k]
      for k,x in bc.items():
       y=cs.get(k,C())-z*x
       if y:cs[k]=y
       elif k in cs:del cs[k]
     if not v:kernels.append(cs)
     if(index+1)%128==0:print('constraints',index+1,'rank',len(basis),'kernel',len(kernels),'seconds',time.monotonic()-start,flush=True)
    fields=[{keys[j]:x for j,x in rel.items()}for rel in kernels]
    for v in fields:
     assert rot(0,1,v)==scale(5*I,v)
     assert not add(rot(0,2,v),scale(I,rot(1,2,v)))
     assert not q['K'](3,v)
    # Certify both seeds belong to this exact space without using floating values.
    pivots={};redbasis=[]
    for v in fields:
     v=dict(v)
     for p,b in zip(pivots,redbasis):
      x=v.get(p,0)
      if x:v=add(v,scale(-x,b))
     assert v;p=min(v);redbasis.append(scale(1/v[p],v));pivots[p]=len(redbasis)-1
    for s in seeds:
     v=dict(s)
     for p,b in zip(pivots,redbasis):
      x=v.get(p,0)
      if x:v=add(v,scale(-x,b))
     assert not v,('seed_outside',len(v))
    out={'scope':'Exact constraint space inside discovered2176coordinate support; M invariance NOT yet certified','raw_support_dimension':len(keys),'constraint_rank':len(basis),'highest5_timekernel_dimension':len(fields),'both_seeds_in_space':True,'basis':[[[e,c,C(x).ser()]for(e,c),x in sorted(v.items())]for v in redbasis],'basis_pivots':[list(p)for p in pivots],'seconds':time.monotonic()-start}
    args.output.write_text(json.dumps(out,indent=2));print('DONE dimension',len(fields),'seconds',time.monotonic()-start,flush=True)


def mode_closure(args):
    s=build_seed_context(args,False)
    E,rot,bs,h,q,seeds,start=s.E,s.rot,s.bs,s.h,s.q,s.seeds,s.start
    import hashlib,subprocess
    fast=_fast_exact_class()(g)
    checks=0
    # Everyformaxis and representative Clifford grades; independent original code.
    for a in range(14):
     for c in [0,1,3,7,15,255,8191,16383]:
      v={(1<<a,c):Q(2,3)};assert fast.Phi_adj(v)==E.Phi_adj(v);checks+=1
    for i,j in[(0,1),(0,3),(3,4),(5,8),(10,13)]:
     for c in [0,1,3,7,15,255,8191,16383]:
      w={((1<<i)|(1<<j),c):Q(5,7)};assert fast.Phi(w)==E.Phi(w);checks+=1
    for i in[0,3,5]:
     u={(1<<i,7):C(2,3),(1<<4,15):Q(2)};v={(1<<8,31):C(-1,2),(1,0):Q(1,3)}
     assert fast.N(u,v)==E.N(u,v);checks+=1
    print('exact starfree controls',checks,'PASS',flush=True)
    basisdata=json.loads((args.cache/'inverse-stage3-basis.json').read_text());bb=[{(e,c):C(Q(x),Q(y))for e,c,(x,y)in row}for row in basisdata['basis']];pivots=[tuple(x)for x in basisdata['basis_pivots']]
    D=json.loads((args.root/'lab/process/source-action-deep-coefficients.json').read_text());Ts=[{(e,c):Q(x)for e,c,x in row}for row in D['basis']]
    def reduce(v):
     cs=[]
     for p,b in zip(pivots,bb):
      x=C(v.get(p,0));cs.append(x)
      if x:v=add(v,scale(-x,b))
     return v,cs
    bindings=current_closure_bindings(args,args.cache/'inverse-stage3-basis.json')
    out={'bindings':bindings,'scope':'Exact native family closure/coordinate columns, only complete if completed equals dimension','dimension':len(bb),'maps':59,'completed':0,'controls':checks,'columns':[]}
    if args.output.exists():
     out=json.loads(args.output.read_text());assert out['dimension']==len(bb)
     assert out.get('bindings',{}).get('implementation_format')=='integrated-v2', 'Legacy closure cannot be resumed by this implementation; use a fresh cache.'
     validate_closure_bindings(out,args,args.cache/'inverse-stage3-basis.json')
     assert out['completed']==len(out['columns']) and out['maps']==59
     assert all(len(col)==59 and all(len(cs)==len(bb) for cs in col) for col in out['columns'])
    start_at=out['completed'];limit=len(bb)if args.steps==0 else min(len(bb),start_at+args.steps)
    for bi in range(start_at,limit):
     v=bb[bi];cols=[]
     for j,T in enumerate(Ts):
      w=q['P'](scale(2,fast.N(T,v)));rem,cs=reduce(w)
      if rem:
       out['failure']={'basis':bi,'background':j,'outside_terms':len(rem),'witness':[[e,c,C(x).ser()]for(e,c),x in list(sorted(rem.items()))[:5]]};args.output.write_text(json.dumps(out,indent=2));raise AssertionError(out['failure'])
      cols.append([C(z).ser()for z in cs])
     out['columns'].append(cols);out['completed']=bi+1;args.output.write_text(json.dumps(out,indent=2));print('closure',bi+1,'/',len(bb),'maps59','seconds',time.monotonic()-start,flush=True)
    print('DONE',out['completed'],len(bb),flush=True)


def mode_certify(args):
    import numpy as np
    scratch=args.cache
    closure_path=scratch/'inverse-stage4-closure-certified.json'
    cl=json.loads(closure_path.read_text());bd=json.loads((scratch/'inverse-stage3-basis.json').read_text());sd=json.loads((scratch/'inverse-stage1.json').read_text());D=json.loads((args.root/'lab/process/source-action-deep-coefficients.json').read_text())
    import hashlib,subprocess
    validation=validate_closure_bindings(cl,args,scratch/'inverse-stage3-basis.json')
    expected=dict(cl['bindings'])
    n=cl['dimension'];assert cl['completed']==n and len(cl['columns'])==n and not cl.get('failure');assert cl['maps']==59
    assert all(len(col)==59 and all(len(co)==n and all(len(z)==2 for z in co)for co in col)for col in cl['columns'])
    As=[[[C()for j in range(n)]for i in range(n)]for k in range(59)]
    for j,col in enumerate(cl['columns']):
     for k,co in enumerate(col):
      for i,(re,im)in enumerate(co):As[k][i][j]=C(Q(re),Q(im))
    def n1(x):x=C(x);return abs(x.a)+abs(x.b)
    def cn(x):return complex(float(x.a),float(x.b))
    def mm(A,B):return [[sum((x*y for x,y in zip(row,col)),C())for col in zip(*B)]for row in A]
    def mv(A,b):return [sum((x*y for x,y in zip(row,b)),C())for row in A]
    def norminf(A):return max(sum(n1(x)for x in row)for row in A)
    def vnorm(v):return max(n1(x)for x in v)
    def ser(A):return [[C(x).ser()for x in row]for row in A]
    basis=[{(e,c):C(Q(x),Q(y))for e,c,(x,y)in row}for row in bd['basis']];piv=[tuple(x)for x in bd['basis_pivots']]
    native_seed=build_seed_context(args,numeric=False).seeds
    assert [{(e,c):C(Q(x),Q(y)) for e,c,(x,y) in row} for row in sd['exact_seeds']]==native_seed
    sources=[]
    for row in sd['exact_seeds']:
     v={(e,c):C(Q(x),Q(y))for e,c,(x,y)in row};co=[]
     for pp,b in zip(piv,basis):
      z=C(v.get(pp,0));co.append(z)
      if z:v=add(v,scale(-z,b))
     assert not v;sources.append(co)
    # Entrywise uniform radius derivative bound: dM <= radius * Aabs.
    Aabs=[[sum(n1(As[k][i][j])for k in range(59))for j in range(n)]for i in range(n)]
    out={'scope':'Exact rational Neumann certificate for120-dimensional invariant source block. Not fullN regularity or full-kernel current compatibility.','bindings':expected|{'closure_sha256':hashlib.sha256(closure_path.read_bytes()).hexdigest(),'stage1_sha256':hashlib.sha256((scratch/'inverse-stage1.json').read_bytes()).hexdigest(),'certificate_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},'coordinate_norm':'max_i (abs(real_i)+abs(imag_i))','dimension':n,'family_maps':59,'roots':[],'closure_validation':validation,'integrated_probe_sha256':file_digest(Path(__file__))}
    start=time.monotonic()
    for ri,root in enumerate(D['certified_roots']):
     xs=list(map(Q,root['coordinates']));radius=Q(root['certificate']['radius'])
     M=[[C(i==j)+sum((x*As[k][i][j]for k,x in enumerate(xs)),C())for j in range(n)]for i in range(n)]
     Mf=np.array([[cn(x)for x in row]for row in M]);Rf=np.linalg.inv(Mf)
     # Any rational R is admissible; exact residual below, not a floating proof.
     R=[[C(Q(str(float(z.real))),Q(str(float(z.imag))))for z in row]for row in Rf]
     print('root',ri,'M/R ready','seconds',time.monotonic()-start,flush=True)
     RM=mm(R,M);E=[[C(i==j)-RM[i][j]for j in range(n)]for i in range(n)];eta0=norminf(E)
     # row sums of |R| Aabs without a full rational triple product
     ar=[sum(row)for row in Aabs]
     eta_delta=radius*max(sum(n1(R[i][j])*ar[j]for j in range(n))for i in range(n));eta=eta0+eta_delta
     rr={'root':ri,'center_preconditioned_residual_inf':str(eta0),'rootball_perturbation_inf':str(eta_delta),'neumann_bound':str(eta),'invertible_on_block_over_rootball':eta<1,'inverse_candidate':ser(R),'sources':[]}
     print('root',ri,'eta',float(eta),'PASS',eta<1,'seconds',time.monotonic()-start,flush=True)
     if eta<1:
      rr['inverse_norm_inf_upper']=str(norminf(R)/(1-eta))
      for si,s in enumerate(sources):
       y=mv(R,s);res=[x-z for x,z in zip(mv(M,y),s)];pre=mv(R,res)
       ay=[sum(Aabs[i][j]*n1(y[j])for j in range(n))for i in range(n)]
       perr=radius*max(sum(n1(R[i][j])*ay[j]for j in range(n))for i in range(n))
       error=(vnorm(pre)+perr)/(1-eta)
       rr['sources'].append({'index':si,'coefficient_error_inf':str(error),'coordinates':[C(x).ser()for x in y],'center_residual_inf':str(vnorm(res)),'preconditioned_center_residual_inf':str(vnorm(pre))})
     out['roots'].append(rr);args.output.write_text(json.dumps(out,indent=2));print('root complete',ri,'seconds',time.monotonic()-start,flush=True)
    print('DONE',flush=True)


def lower(h,v):
    return h.add(h.rot(0,2,v),h.scale(-h.I,h.rot(1,2,v)))


def verify_geometry():
    import source_action_deep_geometry as g
    assert all(not any(g.Lambda[a][i]) for a in range(4,14) for i in range(14))
    assert all(not any(g.A[a-4][3]) for a in [5,6,8,9,11])
    assert g.A[0][3]==[Q(0),Q(0),Q(0),Q(1)]
    assert g.A[3][3]==[Q(0),Q(0),Q(0),Q(-3)]
    assert g.A[6][3]==[Q(-1),Q(0),Q(0),Q(0)]
    assert g.A[8][3]==[Q(0),Q(-1),Q(0),Q(0)]
    assert g.A[9][3]==[Q(0),Q(0),Q(-1),Q(0)]
    return {'normal_Nomizu_zero':True,'nonzero_time_seed_tangent_axes':[4,7,10,12,13],
            'spatial_solving_axis8_preserves_dt':True}


def known_response(root,ctx,source,weight,ri):
    """Solve spin6/7 components with existing rootball inverse certificates.

    source may include spin5 if weight5; it is orthogonal to spin6/7 and is not
    solved here. u=M^-1 source (POSITIVE sign), unlike old energy c=-M^-1b.
    Returns native sparse center, per-coefficient l1-error envelope and evidence.
    """
    assert weight in [5,6,7]
    C,E,h=ctx['C'],ctx['E'],ctx['h']
    old=json.loads((Path(root)/'lab/process/source-action-kappa1-constraints.json').read_text())
    p7=json.loads((Path(root)/'lab/process/source-action-reduced-evolution.json').read_text())['spin7_inverse_candidates'][ri]
    def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    def norm(x):x=C(x);return abs(x.a)+abs(x.b)
    p7cert=old['exact_probe']['spin7']['root_certificates'][ri]
    assert digest(p7['inverse'])==p7cert['inverse_sha256']
    assert p7['neumann_bound']==p7cert['neumann_bound'] and Q(p7['neumann_bound'])<1
    out={};err={};info=[]
    def add_response(basis,coeff,errors,label,gram_scale):
        nonlocal out,err
        for n,a,er in zip(basis,coeff,errors):
            out=h.add(out,h.scale(a,n))
            for k,z in n.items():err[k]=err.get(k,Q(0))+er*norm(z)
        info.append({'sector':label,'weight':weight,'basis_size':len(basis),'lowering_Gram_scale':gram_scale,'nonzero_source_coordinates':sum(bool(c)for c in coeff),'max_coefficient_error':str(max(errors,default=Q(0)))})
    if weight<=6:
        N6=ctx['N6']
        factor6=1
        if weight==5:N6=[lower(h,n)for n in N6];factor6=12
        b6=[C(E.pair(h.conj(n),source))for n in N6]
        cs=[C()for _ in N6];es=[Q(0)for _ in N6]
        certs=old['exact_probe']['spin6']['constraint_inverse']['root_certificates'][ri]['blocks']
        for p,cert in zip(old['spin6_inverse_candidates'][ri]['blocks'],certs):
            assert digest(p['rational_inverse'])==cert['rational_inverse_sha256']
            assert p['neumann_bound']==cert['neumann_bound']
            ids=p['indices'];R=[[C(*z)/factor6 for z in row]for row in p['rational_inverse']]
            c=[sum((x*b6[j]for x,j in zip(row,ids)),C())for row in R]
            eta=Q(p['neumann_bound']);assert eta<1
            er=eta/(1-eta)*max(map(norm,c),default=Q(0))
            for i,z in zip(ids,c):cs[i]=z;es[i]=er
        add_response(N6,cs,es,'spin6',factor6)
    N7=h.N;factor7=1
    if weight<=6:N7=[lower(h,n)for n in N7];factor7*=14
    if weight==5:N7=[lower(h,n)for n in N7];factor7*=26
    b7=[C(E.pair(h.conj(n),source))for n in N7]
    R=[[C(*z)/factor7 for z in row]for row in p7['inverse']]
    cs=[sum((x*y for x,y in zip(row,b7)),C())for row in R]
    eta=Q(p7['neumann_bound']);er=eta/(1-eta)*max(map(norm,cs),default=Q(0))
    add_response(N7,cs,[er]*len(N7),'spin7',factor7)
    return out,err,info


def tangent_matrix(u,axis):
    """Fixed-u tangent seed-current derivative; omit axis8 (solving derivative)."""
    assert axis!=8
    import source_action_paired_response_probe as p
    import source_action_deep_geometry as g
    def convert(v):return {k:p.C(x.a,x.b) if hasattr(x,'a') else p.C(x)for k,x in v.items()}
    u=convert(u);tau=p.covector(3)
    atprime=[Q(g.A[axis-4][3][i])for i in range(4)]+[Q(0)]*10
    cols=[]
    for j in range(5):
        image=p.inverse(tau,p.vertex(u,p.inject(j)))
        value=p.readout(p.inverse(tau,p.sigma(atprime,image)))
        cols.append([{c:-p.C(z)for c,z in v.items()}for v in value])
    return p.flat(cols)


def source_controls(ctx,api,index):
    """Use existing native symbols; inspect weight/type rather than guessing."""
    C,E,h=ctx['C'],ctx['E'],ctx['h']
    K,P,cas,spin5=api['K'],api['P'],api['cas'],api['spin5']
    V=K(3,h.bs[index]);src={a:P(K(a,V))for a in range(4,14)}
    assert src[12]==h.scale(h.I,src[10])
    assert spin5(src[8])==h.scale(h.I,spin5(src[5]))
    for a in [4,7,13]:
        assert cas(src[a])==h.scale(56,src[a]),a
        assert h.rot(0,1,src[a])==h.scale(7*h.I,src[a]),a
    for a in [10,12]:
        assert h.rot(0,1,src[a])==h.scale(6*h.I,src[a]),a
        assert not h.add(cas(cas(src[a])),h.scale(-98,cas(src[a])),h.scale(2352,src[a])),a
    for a in [5,8]:assert h.rot(0,1,src[a])==h.scale(5*h.I,src[a]),a
    for a in [4,6,7,9,10,11,12,13]:assert not spin5(src[a]),a
    return V,src


def mode_matched(args):
    import numpy as np
    import source_action_deep_geometry as g
    import source_action_paired_response_probe as pr
    from source_action_reduced_evolution_probe import build_context
    def num(z):return complex(float(z.a),float(z.b))if hasattr(z,'a')else complex(z)
    def sparse_float(v):return {k:num(x)for k,x in v.items()}

    t0=time.monotonic();print('build full shared context',flush=True);ctx=build_context(args.root);api=pr.build_api(args.root,ctx);print('context ready',time.monotonic()-t0,flush=True)
    C,E,h=ctx['C'],ctx['E'],ctx['h'];V,src=source_controls(ctx,api,5);geom=verify_geometry();print('source controls pass',flush=True)
    dense=_dense_class()(list(map(float,g.d)));d=np.array(g.d,dtype=float);n=128;m=640
    # left multiplication by a Clifford generator is a weighted permutation.
    perms=[]
    for x,z,c in dense.gamma:
     perms.append((dense.bs^x,np.array([c*(-1)**int(int(z&b).bit_count())for b in dense.bs])))
    def ga(i,F):
     out=np.empty_like(F);out[perms[i][0]]=perms[i][1][:,None]*F;return out

    def slash(xi,F):return sum((float(xi[i])/d[i]*ga(i,F)for i in range(14)if xi[i]),start=np.zeros_like(F))
    def trace(F):return sum((ga(i,F[i])/d[i]for i in range(14)),start=np.zeros_like(F[0]))
    def sigma(xi,F):
     z,nu=F[:14],F[14];tr=trace(F);out=np.empty_like(F)
     for i in range(14):out[i]=slash(xi,z[i])+float(xi[i])*(nu-tr)
     out[14]=sum((float(xi[i])/d[i]*z[i]for i in range(14)if xi[i]),start=np.zeros_like(nu))-.5*slash(xi,nu)
     return out

    def inverse(xi,F):
     norm=sum(float(xi[i])**2/d[i]for i in range(14));assert norm
     eta=F[14]-.5*trace(F);up=np.array([F[i]+.5*ga(i,eta)for i in range(14)])
     zp=np.array([slash(xi,z)/norm for z in up]);ep=-slash(xi,eta)/norm
     out=np.empty_like(F)
     for i in range(14):out[i]=zp[i]-.5*ga(i,ep)
     out[14]=trace(zp)-6*ep
     return out

    def read(F):return np.concatenate([F[i]for i in [0,1,2,3,14]],axis=0)
    def cmatrix(form):return dense.to_matrix(dense.sparse_to_array(sparse_float(form)))
    def prep(U):return U,sum((ga(i,U[i])/d[i]for i in range(14)),start=np.zeros((n,n),complex))
    def vertex(UF,F):
     U,SA=UF;out=np.empty_like(F);z,nu=F[:14],F[14]
     nonzero=[b for b in range(14)if np.any(z[b])]
     for i in range(14):
      out[i]=SA@z[i]+U[i]@nu
      if np.any(U[i]):
       for b in nonzero:out[i]-=ga(b,U[i]@z[b])/d[b]
     out[14]=sum((U[i]@z[i]/d[i]for i in nonzero),start=np.zeros_like(nu))-.5*(SA@nu)
     return out

    # Five exact same-injection columns are evaluated together.
    J=np.zeros((15,n,m),complex)
    for j,i in enumerate([0,1,2,3,14]):J[i,:,j*n:(j+1)*n]=np.eye(n)
    tau=[0]*14;tau[3]=1;nz=[0]*14;nz[8]=1
    # Independent finite controls: dense actual symbol/inverse and owned centralcurrent.
    controls={}
    for axis in [3,4,8]:
     xi=[0]*14;xi[axis]=1
     error=float(np.max(np.abs(inverse(xi,sigma(xi,J))-J)));assert error<1e-10;controls['symbol_inverse_'+str(axis)]=error
    central={(8,0):Q(1)};Bcentral=read(inverse(tau,vertex(prep(cmatrix(central)),J)))
    assert np.max(np.abs(Bcentral-np.eye(m)))<1e-10;controls['central_seed_identity']=float(np.max(np.abs(Bcentral-np.eye(m))))
    # Cross-check the dense vertex with the exact owned sparse implementation on
    # a sparse full-U form and all five injected columns, not just central control.
    small={(1,0):Q(2,3),(8,7):Q(1,5),(32,31):Q(-3,7)}
    SD=vertex(prep(cmatrix(small)),J)
    for j in range(5):
     sp=pr.vertex(small,pr.inject(j));fields=sp[0]+[sp[1]]
     for i,field in enumerate(fields):
      co=np.zeros(16384,complex)
      for blade,z in field.items():co[blade]=num(z)
      ref=dense.to_matrix(co);err=float(np.max(np.abs(SD[i,:,j*n:(j+1)*n]-ref)));assert err<1e-10
    controls['sparse_native_vertex_75blocks']=True

    # Czero uses the actual spin+T vertex plus oneform-slot Nomizu corrections.
    spin={(1<<a,c):z for a,row in enumerate(g.spin)for c,z in row.items()}
    def Czero(Tprep,F):
     out=vertex(Tprep,F);z=F[:14]
     for j in range(14):
      for a in range(14):
       for b,zcoeff in g.mbracket(a,j).items():out[j]-=float(zcoeff)/d[a]*ga(a,z[b])
     for a in range(14):
      for b in range(14):
       if g.Lambda[a][a][b]:out[14]-=float(g.Lambda[a][a][b])/d[a]*z[b]
     return out

    def matched(ua,Tprep):
     # All ua already represent the SAME realification of V and its constrainedlift.
     U8=prep(cmatrix(ua[8]));UJ=vertex(U8,J);ZU=inverse(nz,UJ)
     term=Czero(Tprep,ZU)-vertex(U8,inverse(nz,Czero(Tprep,J)))
     # Actual dual CK equation includes tangent seed derivatives; do not duplicate
     # these inside the later T10/T12 terms (those differentiate different currents).
     for a in range(4,14):
      if a==8:continue
      ap=list(map(float,g.A[a-4][3]))+[0.]*10
      if any(ap):term+=sigma(ap,inverse(tau,sigma([float(i==a)for i in range(14)],ZU)))
     B8=read(inverse(tau,term));Tcorr=np.zeros_like(B8)
     for a in [10,12]:
      ap=list(map(float,g.A[a-4][3]))+[0.]*10
      F=vertex(prep(cmatrix(ua[a])),J)
      Tcorr-=read(inverse(tau,sigma(ap,inverse(tau,F))))
     return B8,Tcorr

    def report(B):
     H=(B+B.conj().T)/2;b2=float(np.vdot(B,B).real/128);h2=float(np.vdot(H,H).real/128)
     ix=np.unravel_index(np.argmax(np.abs(H)),H.shape)
     return {'raw_HS2':b2,'Herm_HS2':h2,'Herm_ratio':h2/b2 if b2 else None,'Gram_margin_no_error':2*h2**.5-b2**.5,'strongest_Herm_entry':{'row':int(ix[0]),'column':int(ix[1]),'real':float(H[ix].real),'imag':float(H[ix].imag)},'nonzero_numeric_Herm':bool(h2>1e-16)}
    D=json.loads((args.root/'lab/process/source-action-deep-coefficients.json').read_text());Y5=json.loads(args.inverse.read_text());out={'scope':'NUMERICAL_DIAGNOSTIC_ONLY. Full matched pointwise diagonal lambda0 kernel conditional on reviewed smoothSO3-equivariant auxiliary-family reduction. Rootball inverse error, response support/integration and physical admission NOT certified.','geometry':geom,'controls':controls,'roots':[]}
    saved_kernels={}
    for ri,rd in enumerate(D['certified_roots']):
     print('assemble root',ri,flush=True);known8,err8,info8=known_response(args.root,ctx,src[8],5,ri)
     u10,err10,info10=known_response(args.root,ctx,src[10],6,ri)
     u12,err12,info12=known_response(args.root,ctx,src[12],6,ri)
     # Unknownhighest5 component of axis8=i*source5; existingGMRES solves source5.
     y5={(int(e),int(c)):complex(re,im)for e,c,re,im in Y5['roots'][ri]['solution']}
     u8=sparse_float(known8)
     for k,z in y5.items():u8[k]=u8.get(k,0j)+1j*z
     ua={8:u8,10:sparse_float(u10),12:sparse_float(u12)}
     rel=max((abs(ua[12].get(k,0)-1j*ua[10].get(k,0))for k in set(ua[10])|set(ua[12])),default=0)
     assert rel<1e-9;print('known higher responses assembled',ri,'axis12relation',rel,flush=True)
     T=dict(spin)
     for x,row in zip(rd['coordinates'],D['basis']):
      for e,c,z in row:T[int(e),int(c)]=T.get((int(e),int(c)),Q(0))+Q(x)*Q(z)
     Tprep=prep(cmatrix(T));rr={'root':ri,'spin5_input_relative_residual':Y5['roots'][ri]['relative_residual'],'known_inverse_bounds':info8+info10+info12,'axis12_equals_i_axis10_error':rel,'realifications':{}}
     for part in ['real','imag']:
      ur={a:{k:(z.real if part=='real'else z.imag)for k,z in v.items()if(z.real if part=='real'else z.imag)}for a,v in ua.items()}
      B8,TC=matched(ur,Tprep);B=B8+TC
      if args.save_kernels:
       saved_kernels['r'+str(ri)+'_'+part]=B
       np.savez_compressed(args.save_kernels,**saved_kernels)
      rr['realifications'][part]={'solving_axis8':report(B8),'tangent_correction10_12':report(TC),'matched_total':report(B),'tangent_relative_size':float(np.linalg.norm(TC)/max(1.,np.linalg.norm(B8))),'elapsed_seconds':time.monotonic()-t0}
      print('root',ri,part,'matched',rr['realifications'][part]['matched_total'],flush=True)
     out['roots'].append(rr);args.output.write_text(json.dumps(out,indent=2))
    print('DONE',time.monotonic()-t0,flush=True)




def as_C(v):return {k:p.C(x.a,x.b)if hasattr(x,'a')else p.C(x)for k,x in v.items()}
def slots(v):return v[0]+[v[1]]
def coeff(v,c):return p.C(v.get(c,0))

def target_product(A,B,c):
    """Coefficient of gamma_c in A*B, exact; no full convolution."""
    out=p.C()
    if len(A)<=len(B):
        for a,x in A.items():
            b=a^c;y=B.get(b)
            if y:
                k,s=p.E.cmul(a,b);assert k==c;out+=p.C(x)*p.C(y)*s
    else:
        for b,y in B.items():
            a=b^c;x=A.get(a)
            if x:
                k,s=p.E.cmul(a,b);assert k==c;out+=p.C(x)*p.C(y)*s
    return out


def target_dot(row,col,c):return sum((target_product(a,b,c)for a,b in zip(row,col)),p.C())


class MatchedCoefficients:
    def __init__(self,T,u8,u10,u12):
        self.T=as_C(T);self.us={8:as_C(u8),10:as_C(u10),12:as_C(u12)}
        self.tau=p.covector(3);self.nz=p.covector(8)
        self.Crows={};self.Urows={};self.ZUcols={};self.ZCcols={};self.Lcols={};self.cache={}
        self.cprep=p.prepare_vertex(add(p.spin_form(),self.T))
        self.uprep=p.prepare_vertex(self.us[8])
        self.small_uprep={a:p.prepare_vertex(self.us[a])for a in [10,12]}
    def C(self,v):
        # Call owned Czero to retain covector-slot, actual spin/background and
        # scalar divergence terms; it caches by the exact T object's identity.
        return p.Czero(self.T,v)
    def U(self,v):return p.apply_vertex(self.uprep,v)
    def Q(self,v):return p.readout(p.inverse(self.tau,v))
    def C_row(self,i):
        if i not in self.Crows:self.Crows[i]=[self.Q(self.C(column(k)))[i]for k in range(15)]
        return self.Crows[i]
    def U_row(self,i):
        if i not in self.Urows:self.Urows[i]=[self.Q(self.U(column(k)))[i]for k in range(15)]
        return self.Urows[i]
    def ZU_col(self,j):
        if j not in self.ZUcols:self.ZUcols[j]=slots(p.inverse(self.nz,self.U(p.inject(j))))
        return self.ZUcols[j]
    def ZC_col(self,j):
        if j not in self.ZCcols:self.ZCcols[j]=slots(p.inverse(self.nz,self.C(p.inject(j))))
        return self.ZCcols[j]
    def linear_col(self,j):
        if j in self.Lcols:return self.Lcols[j]
        zlist=self.ZU_col(j);ZU=(zlist[:14],zlist[14]);v=p.vscale(0,ZU)
        for a in range(4,14):
            if a==8:continue
            ap=[Q(g.A[a-4][3][i])for i in range(4)]+[Q(0)]*10
            if not any(ap):continue
            v=p.vadd(v,p.sigma(ap,p.inverse(self.tau,p.sigma(p.covector(a),ZU))))
        out=self.Q(v)
        for a in [10,12]:
            ap=[Q(g.A[a-4][3][i])for i in range(4)]+[Q(0)]*10
            base=p.apply_vertex(self.small_uprep[a],p.inject(j))
            ta=self.Q(p.sigma(ap,p.inverse(self.tau,base)))
            out=[add(x,scale(-1,y))for x,y in zip(out,ta)]
        self.Lcols[j]=out;return out
    def raw(self,i,j,c):
        key=(i,j,c)
        if key not in self.cache:
            self.cache[key]=target_dot(self.C_row(i),self.ZU_col(j),c)-target_dot(self.U_row(i),self.ZC_col(j),c)+coeff(self.linear_col(j)[i],c)
        return self.cache[key]
    def herm(self,i,j,c):
        return (self.raw(i,j,c)+p.adj_sign(c)*self.raw(j,i,c).conj())/2


def finite_controls():
    """Small exact rearrangement controls; root runs them, not at import."""
    checks=0
    A={0:p.C(2,3),7:p.C(Q(2,5),Q(-1,7)),19:p.C(-2)}
    B={2:p.C(4,-2),9:p.C(3),31:p.C(Q(1,3))}
    prod=p.mul(A,B)
    for c in set(prod)|{0,1,7,16383}:
        assert target_product(A,B,c)==prod.get(c,p.C());checks+=1
    T={(1,7):p.C(Q(2,3)),(32,15):p.C(Q(1,7))}
    u={(1,3):p.C(Q(1,5)),(8,31):p.C(Q(-2,7))}
    K=MatchedCoefficients(T,u,{},{});full=p.center_full_R_base(u,T)
    # Tangent corrections zero here; center_full_R_base is full_jet lambda0.
    candidates=set(full)|{(0,0,0),(4,4,16383)}
    for i,j,c in candidates:
        assert K.raw(i,j,c)==full.get((i,j,c),p.C());checks+=1
    return {'exact_factored_coefficient_controls':checks,'scope':'small independently-owned full_jet agreement, not actual root evaluation'}

def certified_field(C, root_index, source_index, scratch=None):
    assert scratch is not None, "Explicit cache required"
    scratch = Path(scratch)
    basis_path = scratch / 'inverse-stage3-basis.json'
    cert_path = scratch / 'inverse-stage5-certificate.json'
    basis_data = json.loads(basis_path.read_text())
    certificate = json.loads(cert_path.read_text())
    assert certificate['bindings']['basis_sha256'] == hashlib.sha256(basis_path.read_bytes()).hexdigest()
    assert certificate['coordinate_norm'] == 'max_i (abs(real_i)+abs(imag_i))'
    rr = certificate['roots'][root_index]
    assert rr['root'] == root_index and rr['invertible_on_block_over_rootball']
    assert Q(rr['neumann_bound']) < 1
    ss = rr['sources'][source_index]
    assert ss['index'] == source_index
    coordinates = [C(Q(re), Q(im)) for re, im in ss['coordinates']]
    epsilon = Q(ss['coefficient_error_inf'])
    assert len(coordinates) == len(basis_data['basis']) == 120 and epsilon >= 0
    center = {}
    errors = {}
    for ci, bb in zip(coordinates, basis_data['basis']):
        for e, c, (re, im) in bb:
            z = C(Q(re), Q(im))
            key = (e, c)
            center[key] = center.get(key, C()) + ci*z
            errors[key] = errors.get(key, Q()) + epsilon*(abs(z.a)+abs(z.b))
    return ({k:v for k,v in center.items() if v},
            {k:v for k,v in errors.items() if v},
            {'root': root_index, 'source': source_index,
             'coefficient_error_inf': str(epsilon),
             'scope': certificate['scope'],
             'certificate_sha256': hashlib.sha256(cert_path.read_bytes()).hexdigest()})

def target_ball_product(A,B,c):
    out=p.Ball()
    if len(A)>len(B):
        for b,y in B.items():
            a=b^c;x=A.get(a)
            if x:
                k,s=p.E.cmul(a,b);assert k==c
                out+=p.Ball(x)*p.Ball(y)*s
    else:
        for a,x in A.items():
            b=a^c;y=B.get(b)
            if y:
                k,s=p.E.cmul(a,b);assert k==c
                out+=p.Ball(x)*p.Ball(y)*s
    return out

def target_ball_dot(row,col,c):
    return sum((target_ball_product(a,b,c) for a,b in zip(row,col)),p.Ball())

class MatchedInterval(MatchedCoefficients):
    def __init__(self,T,dT,us,dus):
        def balls(v,e):return {k:p.Ball(v.get(k,0),e.get(k,0)) for k in v.keys()|e.keys()}
        self.T=balls(T,dT);self.us={a:balls(us[a],dus[a])for a in [8,10,12]}
        self.tau=p.covector(3);self.nz=p.covector(8)
        self.Crows={};self.Urows={};self.ZUcols={};self.ZCcols={};self.Lcols={};self.cache={}
        self.cprep=p.prepare_vertex(add(p.spin_form(),self.T))
        self.uprep=p.prepare_vertex(self.us[8])
        self.small_uprep={a:p.prepare_vertex(self.us[a])for a in [10,12]}
    def raw(self,i,j,c):
        key=(i,j,c)
        if key not in self.cache:
            self.cache[key]=target_ball_dot(self.C_row(i),self.ZU_col(j),c)-target_ball_dot(self.U_row(i),self.ZC_col(j),c)+p.Ball(self.linear_col(j)[i].get(c,0))
        return self.cache[key]
    def herm(self,i,j,c):
        a=self.raw(i,j,c);b=self.raw(j,i,c)
        return (a+p.adj_sign(c)*p.Ball(b.c.conj(),b.e))/2


def mode_exact(args):
    import source_action_paired_response_probe as pr
    from source_action_reduced_evolution_probe import build_context
    cl=json.loads((args.cache/'inverse-stage4-closure-certified.json').read_text())
    validate_closure_bindings(cl,args,args.cache/'inverse-stage3-basis.json')
    cert=json.loads((args.cache/'inverse-stage5-certificate.json').read_text())
    assert cert['bindings']['closure_sha256']==file_digest(args.cache/'inverse-stage4-closure-certified.json')
    def toC(v):return {k:pr.C(x.a,x.b)if hasattr(x,'a')else pr.C(x)for k,x in v.items()}
    def norm(z):z=pr.C(z);return abs(z.a)+abs(z.b)
    def addforms(a,b):
     out=dict(a)
     for k,z in b.items():out[k]=out.get(k,pr.C())+z
     return {k:z for k,z in out.items()if z}
    def adderr(a,b):
     out=dict(a)
     for k,z in b.items():out[k]=out.get(k,Q(0))+z
     return {k:z for k,z in out.items()if z}
    def sqrtbounds(q):
     from math import isqrt
     den=10**18;q=Q(q);n=isqrt(q.numerator*den*den//q.denominator);lo=Q(n,den)
     return lo,lo if lo*lo==q else Q(n+1,den)

    t0=time.monotonic();controls=finite_controls();print('exact coefficient rearrangement controls',controls,flush=True)
    ctx=build_context(args.root);api=pr.build_api(args.root,ctx);V,src=source_controls(ctx,api,[5,12][args.source]);fixed=pr.fixed_jet_norm_bounds();atinv=pr.linear_op_bound(lambda v:pr.inverse(pr.covector(3),v))
    apnorm={a:pr.linear_op_bound(lambda v,a=a:pr.sigma(list(map(Q,g.A[a-4][3]))+[Q(0)]*10,v))for a in [10,12]}
    D=json.loads((args.root/'lab/process/source-action-deep-coefficients.json').read_text());targets=json.loads(args.targets.read_text());out={'scope':'EXACT_SELECTED_UNNORMALIZED_HERMITIAN_FORMAL_WEAK_COEFFICIENT for the authenticated reached-block particular auxiliary responses. The equivariant contracted formal-jet correction is assigned through the complete N7 inverse and is current-blind. Full spin5 complement-kernel independence and smooth-family realizability remain unproved. No all-Gram statement, integrated response or physical admission.','source_index':args.source,'controls':controls,'roots':[]}
    for ri,rd in enumerate(D['certified_roots']):
     print('assemble certified root',ri,flush=True)
     y5,e5,certmeta=certified_field(pr.C,ri,args.source,scratch=args.cache)
     known8,e8,meta8=known_response(args.root,ctx,src[8],5,ri)
     u10,e10,meta10=known_response(args.root,ctx,src[10],6,ri)
     u12,e12,meta12=known_response(args.root,ctx,src[12],6,ri)
     u8=addforms(toC(known8),{k:pr.I*z for k,z in y5.items()});e8=adderr(e8,e5)
     centers={8:u8,10:toC(u10),12:toC(u12)};errors={8:e8,10:e10,12:e12}
     T={};Terr={};radius=Q(rd['certificate']['radius'])
     for x,row in zip(rd['coordinates'],D['basis']):
      for e,c,v in row:
       k=(int(e),int(c));T[k]=T.get(k,pr.C())+pr.C(Q(x)*Q(v));Terr[k]=Terr.get(k,Q(0))+radius*abs(Q(v))
     T={k:z for k,z in T.items()if z};Terr={k:z for k,z in Terr.items()if z}
     rr={'root':ri,'spin5_certificate':certmeta,'known_inverse_metadata':meta8+meta10+meta12,'realifications':{}}
     for part,attribute in [('real','a'),('imag','b')]:
      realcenters={a:{k:pr.C(getattr(pr.C(z),attribute))for k,z in v.items()if getattr(pr.C(z),attribute)}for a,v in centers.items()}
      bound=pr.full_jet_error_bounds(T,Terr,realcenters[8],errors[8],fixed)['constant'];terms={'solving_axis8':str(bound)}
      for a in [10,12]:
       du=pr.vertex_norm_from_component_norms(pr.connection_component_norms(errors[a]))
       ea=Q(9,4)*fixed['Q']*apnorm[a]*atinv*du;bound+=ea;terms['tangent_'+str(a)]=str(ea)
      key='r'+str(ri)+'_'+part;target=targets['kernels'][key]['targets'][0];i,j,c=[target[k]for k in ['i','j','c']]
      engine=MatchedCoefficients(T,realcenters[8],realcenters[10],realcenters[12]);value=engine.herm(i,j,c)
      weight=Q(1)
      for a in range(14):
       if c>>a&1:weight*=abs(g.d[a])
      wl,wu=sqrtbounds(weight);mag=max(abs(value.a),abs(value.b));lower=mag*wl-bound
      interval=MatchedInterval(T,Terr,realcenters,errors).herm(i,j,c)
      assert interval.c==value, 'Exact selected center disagrees with interval center'
      interval_margin=mag-interval.e
      interval_weighted=mag*wl-interval.e*wu
      print('target interval margin',float(interval_margin),'weighted',float(interval_weighted),flush=True)
      rr['realifications'][part]={'target':{'i':i,'j':j,'c':c},'exact_Herm_coefficient':value.ser(),'exact_weight':str(weight),'sqrt_weight_lower':str(wl),'center_weighted_component_lower':str(mag*wl),'normalized_HS_error_upper':str(bound),'error_components':terms,'strict_weighted_margin_lower':str(lower),'certified_nonzero':interval_margin>0,'selected_interval_error':str(interval.e),'selected_interval_margin':str(interval_margin),'selected_interval_weighted_margin':str(interval_weighted),'global_norm_certified_nonzero':lower>0,'numerical_target_center':target['center'],'center_approximation':[float(value.a),float(value.b)],'seconds':time.monotonic()-t0}
      print('root',ri,part,'exacttarget',i,j,c,'center',float(mag*wl),'error',float(bound),'global_HS_margin',float(lower),'global_HS_pass',lower>0,'selected_interval_pass',interval_margin>0,flush=True)
     out['roots'].append(rr);args.output.write_text(json.dumps(out,indent=2))
    print('DONE',time.monotonic()-t0,flush=True)


def mode_gram(args):
    from source_action_paired_response_probe import C
    bp = args.cache/'inverse-stage3-basis.json'
    bd = json.loads(bp.read_text())
    bs = [{(e,c): C(Q(re), Q(im)) for e,c,(re,im) in row}
          for row in bd['basis']]
    E = Engine(g)
    n = len(bs)
    G = [[sum((z.conj()*bj.get(k,C())*E.weight(*k)
               for k,z in bi.items()), C()) for bj in bs] for bi in bs]
    assert all(G[i][j] == G[j][i].conj() for i in range(n) for j in range(n))
    # Same-weight bilinear isotropy is a useful guard on weight conventions.
    assert all(not sum((z*bj.get(k,C())*E.weight(*k)
                        for k,z in bi.items()), C()) for bi in bs for bj in bs)
    H = [row[:] for row in G]
    positive = negative = 0
    pivots = []
    while H:
        size = len(H)
        diag = next((i for i in range(size) if H[i][i]), None)
        if diag is not None:
            ids = [i for i in range(size) if i != diag]
            d = H[diag][diag]
            assert not d.b
            positive += d.a > 0
            negative += d.a < 0
            pivots.append({'size':1, 'value':d.ser()})
            H = [[H[i][j]-H[i][diag]*H[diag][j]/d for j in ids] for i in ids]
        else:
            pair = next(((i,j) for i in range(size) for j in range(i+1,size) if H[i][j]), None)
            if pair is None:
                break
            i,j = pair
            z = H[i][j]
            ids = [k for k in range(size) if k not in pair]
            positive += 1
            negative += 1
            pivots.append({'size':2, 'off_diagonal':z.ser(), 'signature':[1,1]})
            # [[0,z],[conj(z),0]] inverse = [[0,1/conj(z)],[1/z,0]].
            H = [[H[k][l]-H[k][i]*H[j][l]/z.conj()-H[k][j]*H[i][l]/z
                  for l in ids] for k in ids]
        assert all(H[i][j] == H[j][i].conj() for i in range(len(H)) for j in range(len(H)))
    nullity = len(H)
    out = {'scope':'Native Hermitian Gram on the exact highest5 120-space; no physical positivity or complement-kernel verdict.',
           'basis_sha256':hashlib.sha256(bp.read_bytes()).hexdigest(),
           'dimension':n, 'same_weight_bilinear_isotropic':True,
           'hermitian_signature':[positive,negative,nullity],
           'nondegenerate':nullity==0, 'conjugate_realification_signature':[2*positive,2*negative,2*nullity],
           'exact_congruence_pivots':pivots,
           'gram':[[z.ser() for z in row] for row in G]}
    assert positive+negative+nullity == n
    args.output.write_text(json.dumps(out, indent=2))
    print(json.dumps({k:v for k,v in out.items() if k not in ('gram','exact_congruence_pivots')}, indent=2), flush=True)


def mode_targets(args):
    import numpy as np
    assert args.input is not None, "--input kernels.npz is required"
    D=_dense_class()(list(map(float,g.d)));data=np.load(args.input);out={'scope':'numerical target selection only; exact coefficient and remainder/norm bounds required','kernels':{}}
    for key in data.files:
     B=data[key];H=(B+B.conj().T)/2;rows=[]
     for i in range(5):
      for j in range(5):
       co=D.from_matrix(H[128*i:128*(i+1),128*j:128*(j+1)])
       weights=(np.abs(co)*np.abs(D.phase))**2
       for c in np.flatnonzero(weights>0):rows.append((float(weights[c]),i,j,int(c),co[c]))
     rows.sort(key=lambda x:x[0],reverse=True);total=float(np.vdot(H,H).real/128);raw=float(np.vdot(B,B).real/128);sel=[];cum=0.
     for w,i,j,c,z in rows:
      sel.append({'i':i,'j':j,'c':c,'center':[float(z.real),float(z.imag)],'weighted_square':w,'weight':float(abs(D.phase[c])**2)});cum+=w
      if cum>=0.85*total:break
     out['kernels'][key]={'raw_HS2':raw,'Herm_HS2':total,'selected_Herm_HS2':cum,'selected_fraction':cum/total,'targets':sel}
    args.output.write_text(json.dumps(out,indent=2));print({k:{'targets':len(v['targets']),'fraction':v['selected_fraction']}for k,v in out['kernels'].items()})


def mode_unpack(args):
    """Restore exact recorded machine certificates to an explicit local cache."""
    import base64,zlib
    evidence=args.evidence or args.root/'lab/process/source-action-weak-response.json'
    records=json.loads(evidence.read_text())['reproduction']['records']
    allowed={'inverse-stage1.json','inverse-stage2.json','inverse-stage3-basis.json',
             'inverse-stage4-closure-certified.json','inverse-stage5-certificate.json',
             'inverse-stage5-gram.json','matched-targets.json','matched-stage3.json',
             'matched-exact-coefficient.json','scalar-goal-affine.json','scalar-goal-membership.json'}
    restored=[]
    for name,record in records.items():
        assert name in allowed and record['encoding']=='zlib-base64-json'
        assert 0<record['uncompressed_bytes']<100_000_000
        decoder=zlib.decompressobj()
        raw=decoder.decompress(base64.b64decode(record['data'],validate=True),record['uncompressed_bytes']+1)
        assert decoder.eof and not decoder.unconsumed_tail and not decoder.unused_data
        assert len(raw)==record['uncompressed_bytes']
        assert hashlib.sha256(raw).hexdigest()==record['sha256']
        json.loads(raw) # Data only, never Python source.
        dest=args.cache/name
        if dest.exists():assert dest.read_bytes()==raw,('Different existing cache input',name)
        else:dest.write_bytes(raw)
        restored.append(name)
    args.output.write_text(json.dumps({'restored':restored,'all_exact_bytes_verified':True},indent=2)+'\n')
    print('Restored',len(restored),'hash-verified certificate inputs',flush=True)


def as_c(z):
    return p.C(z.a, z.b) if hasattr(z, 'a') else p.C(z)


def slots(v):
    return v[0] + [v[1]]


def acc(out, key, value):
    value = out.get(key, 0) + value
    if value:
        out[key] = value
    else:
        out.pop(key, None)


def eval_goal(ell, u):
    return sum((z * as_c(u.get(k, 0)) for k, z in ell.items()), p.C())


def target_sandwich(out, axis, left, right, target, factor=1,
                    imaginary_only=True):
    """Accumulate [gamma_target](left*u_axis*right) as a sparse covector.

    For each pair (l,r), the only contributing unknown blade is d=l^r^target.
    Both Clifford multiplication signs AND metric factors are retained.
    """
    for l, x in left.items():
        for r, y in right.items():
            d = l ^ r ^ target
            if imaginary_only and d.bit_count() % 4 not in (0, 3):
                continue
            ld, s1 = p.E.cmul(l, d)
            result, s2 = p.E.cmul(ld, r)
            assert result == target
            acc(out, (1 << axis, d), factor * x * y * s1 * s2)


class GoalBuilder:
    """All maps below are right-Clifford-linear; their coefficients act LEFT.

    There are only 15 fixed carrier columns here, plus 14 identity-valued
    connection component probes per injection. No unknown blade enumeration.
    Tangent u10/u12 are constants with respect to the unknown u8 and omitted
    from this derivative functional; they remain in the scalar's affine offset.
    """
    def __init__(self, T):
        self.T = {k: as_c(z) for k, z in T.items() if z}
        assert all(not z.b for z in self.T.values()), 'real T required'
        self.tau, self.nz = p.covector(3), p.covector(8)
        self.first_rows = None
        self.q_rows = None
        self.zc = {}

    def q(self, v):
        return p.readout(p.inverse(self.tau, v))

    def c(self, v):
        return p.Czero(self.T, v)

    def row_seed(self, v):
        out = p.vscale(0, v)
        for axis in range(4, 14):
            if axis == 8:
                continue
            ap = list(map(Q, g.A[axis - 4][3])) + [Q(0)] * 10
            if any(ap):
                out = p.vadd(out, p.sigma(ap, p.inverse(
                    self.tau, p.sigma(p.covector(axis), v))))
        return out

    def prepare(self):
        if self.first_rows is not None:
            return
        first_columns, q_columns = [], []
        for k in range(15):
            col = p.column(k)
            z = p.inverse(self.nz, col)
            first_columns.append(self.q(p.vadd(self.c(z), self.row_seed(z))))
            q_columns.append(self.q(col))
        self.first_rows = [[first_columns[k][i] for k in range(15)]
                           for i in range(5)]
        self.q_rows = [[q_columns[k][i] for k in range(15)]
                       for i in range(5)]

    def raw_goal(self, i, j, target, imaginary_only=True):
        self.prepare()
        out = {}
        if j not in self.zc:
            self.zc[j] = slots(p.inverse(self.nz, self.c(p.inject(j))))
        v = self.zc[j]
        qrow, first = self.q_rows[i], self.first_rows[i]
        one = {0: Q(1)}
        for a in range(14):
            # Since inject(j) has identity-valued slots, each component of
            # U(inject(j)) is a LEFT polynomial times the formal unknown u_a.
            unit = {(1 << a, 0): Q(1)}
            uv = slots(p.vertex(unit, p.inject(j)))
            left = add(*(p.mul(f, z) for f, z in zip(first, uv) if f and z))
            target_sandwich(out, a, left, one, target,
                            imaginary_only=imaginary_only)
            ga = p.gamma(a)
            # Minus Q U(v), v=Z C inject(j). Five actual vertex terms:
            # r_l = sum_a gamma_a*u_a*v_l/d_a
            #       -sum_b gamma_b*u_l*v_b/d_b + u_l*nu
            # s   = sum_a u_a*v_a/d_a -sum_a gamma_a*u_a*nu/(2*d_a).
            for l in range(14):
                target_sandwich(out, a, p.mul(qrow[l], ga), v[l], target,
                                -1 / g.d[a], imaginary_only)
            for b in range(14):
                target_sandwich(out, a, p.mul(qrow[a], p.gamma(b)), v[b],
                                target, 1 / g.d[b], imaginary_only)
            target_sandwich(out, a, qrow[a], v[14], target, -1,
                            imaginary_only)
            target_sandwich(out, a, qrow[14], v[a], target, -1 / g.d[a],
                            imaginary_only)
            target_sandwich(out, a, p.mul(qrow[14], ga), v[14], target,
                            Q(1, 2) / g.d[a], imaginary_only)
        return {k: as_c(z) for k, z in out.items()}

    def hermitian_real_goal(self, target=(3, 4, 1910)):
        i, j, blade = target
        ij, ji = self.raw_goal(i, j, blade), self.raw_goal(j, i, blade)
        assert all(not z.b for z in list(ij.values()) + list(ji.values()))
        # First form a REAL-linear functional. Its unique complex-linear
        # extension has these same real coefficients; do NOT conjugate u.
        return scale(Q(1, 2), add(ij, scale(p.adj_sign(blade), ji)))


def restricted_dual(ell, api, *, max_rotation_spin=7):
    """Return the exact lowest5 representer of ell on highest5/time-kernel.

    Premise: complete carrier has integer spins <=7, and the native P and
    rotation action preserve the bilinear pairing as established separately.
    This is not a numerical/Hermitian projection onto E.
    """
    assert max_rotation_spin == 7, 'authenticate different carrier bound first'
    C, E, h = api['C'], api['E'], api['h']
    cv = lambda z: C(z.a, z.b) if hasattr(z, 'a') else C(z)
    r = {k: cv(z) / E.weight(*k) for k, z in ell.items()
         if k[1].bit_count() % 4 in (0, 3)}
    r = api['P'](r)
    J = lambda v: h.rot(0, 1, v)
    # Select weights +/-5 from the authenticated integer weight range [-7,7].
    for m in (0, 1, 2, 3, 4, 6, 7):
        r = scale(Q(1, m*m - 25), add(J(J(r)), scale(m*m, r)))
    # J has eigenvalue -5i on the bilinear dual to the +5 space.
    r = scale(Q(1, 2), add(r, scale(h.I / 5, J(r))))
    assert J(r) == scale(-5*h.I, r)
    # Only after selecting weight -5 can spins <5 be absent. This is the
    # precise setting where the existing two-factor spin5 projector is valid.
    r = api['spin5'](r)
    assert api['cas'](r) == scale(30, r)
    assert not add(h.rot(0, 2, r), scale(-h.I, h.rot(1, 2, r)))
    assert not api['K'](3, r)
    assert api['P'](r) == r
    return r


def reduce_conjugate_E(r, basis_data, api):
    """Exact full-carrier residual against conjugated normalized echelon E.

    A nonzero residual proves nonmembership at the supplied T only; it does
    NOT prove that M has a kernel or that the scalar is ambiguous.
    """
    C = api['C']
    basis = [{(e,c): C(Q(re), -Q(im)) for e,c,(re,im) in row}
             for row in basis_data['basis']]
    pivots = [tuple(k) for k in basis_data['basis_pivots']]
    assert len(basis)==len(pivots)==len(set(pivots))==120
    assert all(b[pp]==C(1) and all(not b.get(p,0)for p in pivots[:i])for i,(b,pp)in enumerate(zip(basis,pivots)))
    remainder, coordinates = dict(r), []
    for b, pivot in zip(basis, pivots):
        assert b[pivot] == C(1)
        z = remainder.get(pivot, C())
        coordinates.append(z)
        if z:
            remainder = add(remainder, scale(-z, b))
    reconstructed = add(remainder, *(scale(z,b) for z,b in zip(coordinates,basis)))
    assert reconstructed == r
    return {'member': not remainder, 'remainder': remainder,
            'coordinates': coordinates}


def goal_finite_controls():
    """Prepared lightweight controls; root executes explicitly, never import.

    Agreement with independently owned matched evaluator on a small fixture;
    also checks complex extension separately from real Hermitian evaluation.
    """
    T = {(1,7): p.C(Q(2,3)), (32,15): p.C(Q(1,7))}
    target = (3,4,1910)
    builder = GoalBuilder(T)
    ell = builder.hermitian_real_goal(target)
    # This sparse fixture need not excite target1910. The additional target
    # probes at active covector positions prevent a vacuous zero control.
    checks = 0
    for test_target in (target, (0,1,7), (3,4,0)):
        ell = builder.hermitian_real_goal(test_target)
        keys = sorted(ell)[:4] + [(1,0), (8,7), (32,15)]
        u = {k: p.C(Q(n+2, 2*n+3)) for n,k in enumerate(keys)}
        engine = MatchedCoefficients(T,u,{},{})
        assert eval_goal(ell,u) == engine.herm(*test_target)
        checks += 1
        # For imaginary u the complexified real functional is i*ell(u),
        # rather than Herm(raw(i*u)), whose conjugation is a different map.
        iu = {k:p.I*z for k,z in u.items()}
        assert eval_goal(ell,iu) == p.I*eval_goal(ell,u)
        checks += 1
    return {'checks': checks, 'scope':'small exact coefficient controls only'}


def mode_goals(args):
    root=args.root;scratch=args.cache
    cl=json.loads((scratch/'inverse-stage4-closure-certified.json').read_text())
    assert cl['completed']==cl['dimension']==120 and not cl.get('failure')
    validate_closure_bindings(cl,args,scratch/'inverse-stage3-basis.json')
    start=time.monotonic();ctx=build_seed_context(SimpleNamespace(root=root),numeric=False);api=ctx.q
    basis=json.loads((scratch/'inverse-stage3-basis.json').read_text());D=json.loads((root/'lab/process/source-action-deep-coefficients.json').read_text())
    # Review-requested exact echelon validation.
    bs=[{(e,c):C(Q(re),Q(im))for e,c,(re,im)in row}for row in basis['basis']];piv=[tuple(x)for x in basis['basis_pivots']]
    assert len(bs)==len(piv)==len(set(piv))==120
    assert all(b[pp]==C(1) and all(not b.get(p,0)for p in piv[:i])for i,(b,pp)in enumerate(zip(bs,piv)))
    # Nonvacuous transposed-coefficient control: pick an actual nonzero goal entry.
    b=GoalBuilder({});ell=b.hermitian_real_goal((3,4,1910));assert ell
    key=next(k for k,z in ell.items()if z);u={key:C(1)}
    assert eval_goal(ell,u)==MatchedCoefficients({},u,{},{}).herm(3,4,1910)!=C()
    targets=[(3,4,c)for c in [1910,3446,4981,1909]]
    path=args.output
    out={'scope':'Exact affine-family adjoint representer membership in conjugate(E), only the specified highest5 scalar ambiguity. Not smooth auxiliary realizability, Gram-normalized or physical response.','targets':targets,'dimension':120,'maps':59,'completed':0,'controls':{'echelon_full_validation':True,'nonzero_transposed_coefficient':True},'cases':[],'bindings':{'basis_sha256':hashlib.sha256((scratch/'inverse-stage3-basis.json').read_bytes()).hexdigest(),'background_sha256':hashlib.sha256((root/'lab/process/source-action-deep-coefficients.json').read_bytes()).hexdigest(),'integrated_probe_sha256':file_digest(Path(__file__))}}
    for ji in range(-1,59):
     T={}if ji==-1 else {(e,c):Q(v)for e,c,v in D['basis'][ji]}
     builder=GoalBuilder(T);case={'background_basis':ji,'targets':[]}
     for target in targets:
      ell=builder.hermitian_real_goal(target);r=restricted_dual(ell,api);result=reduce_conjugate_E(r,basis,api)
      # Source-block dual controls authenticate the transposed native pairing.
      for v in bs:assert eval_goal(ell,v)==api['E'].pair(r,v)
      record={'target':list(target),'ambient_terms':len(ell),'restricted_terms':len(r),'member':result['member'],'coordinates':[C(z.a,z.b).ser()for z in result['coordinates']]}
      if not result['member']:
       record['remainder']=[[e,c,C(z.a,z.b).ser()]for(e,c),z in sorted(result['remainder'].items())]
       case['targets'].append(record);out['cases'].append(case);out['failure']={'background_basis':ji,'target':list(target),'meaning':'This representer shortcut fails; no scalar nonuniqueness or source verdict'};path.write_text(json.dumps(out,indent=2));print('MEMBERSHIP FAILURE',ji,target,flush=True);raise SystemExit(2)
      case['targets'].append(record)
     out['cases'].append(case);out['completed']=ji+2;path.write_text(json.dumps(out,indent=2));print('affine',ji+2,'/60 all4 goals pass','seconds',time.monotonic()-start,flush=True)
    print('DONE ALL AFFINE GOALS',flush=True)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    modes=p.add_mutually_exclusive_group()
    for name in ['domain','seeds','numeric','basis','closure','certify','matched','targets','exact','gram','unpack','goals']:
        modes.add_argument('--'+name,action='store_const',const=name,dest='mode')
    p.set_defaults(mode='domain')
    p.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2])
    p.add_argument('--cache',type=Path)
    p.add_argument('--output',type=Path)
    p.add_argument('--save-kernels',type=Path)
    p.add_argument('--targets-file',type=Path)
    p.add_argument('--input',type=Path)
    p.add_argument('--evidence',type=Path)
    p.add_argument('--source',type=int,default=0,choices=[0,1])
    p.add_argument('--inverse',type=Path,help='Numerical candidate input for --matched; defaults to cache/inverse-stage2.json')
    p.add_argument('--steps',type=int,help='Matvec steps / GMRES restart cycles / closure columns; closure0 means all')
    args=p.parse_args();args.root=args.repo.resolve()
    assert (args.root/'tests/program-focus/source_action_deep_geometry.py').exists(),'--repo must name GU repository root'
    args.cache=(args.cache or args.root/'_local/weak-response-reproduction').resolve();args.cache.mkdir(parents=True,exist_ok=True)
    outputs={'domain':'domain-probe.json','seeds':'inverse-stage1.json','numeric':'inverse-stage2.json','basis':'inverse-stage3-basis.json','closure':'inverse-stage4-closure-certified.json','certify':'inverse-stage5-certificate.json','matched':'matched-stage3.json','targets':'matched-targets.json','exact':'matched-exact-coefficient.json','gram':'inverse-stage5-gram.json','unpack':'unpack-result.json','goals':'scalar-goal-affine.json'}
    args.output=(args.output or args.cache/outputs[args.mode]).resolve();args.output.parent.mkdir(parents=True,exist_ok=True)
    args.inverse=(args.inverse or args.cache/'inverse-stage2.json').resolve()
    args.targets=args.targets_file or args.cache/'matched-targets.json'
    if args.steps is None:args.steps=0 if args.mode=='closure' else 1
    assert args.steps>=0
    configure(args.root)
    globals()['mode_'+args.mode](args)

if __name__=='__main__':main()
