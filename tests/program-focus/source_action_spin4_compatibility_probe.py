#!/usr/bin/env python3
"""Targeted reached-spin4 receiver diagnostic. Heavy stages are opt-in.

No changed action, pairing, support or root. A numerical residual is not proof;
a source outside a candidate envelope is not an ambient cokernel obstruction.
Run serially, BLAS threads1. Native inputs come only from --repo.
"""
from pathlib import Path
from fractions import Fraction as Q
from types import SimpleNamespace
from collections import Counter
import argparse, hashlib, json, os, sys, time
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[name]='1'
sys.dont_write_bytecode=True


def write(path,obj):
    tmp=path.with_suffix(path.suffix+'.new');tmp.write_text(json.dumps(obj,indent=2));tmp.replace(path)

def load(args):
    global w,g,C,I,add,scale,original_context
    sys.path.insert(0,str(args.root/'tests/program-focus'))
    import source_action_weak_response_probe as w
    import source_action_deep_geometry as g
    from source_action_deep_algebra import add,scale
    from source_action_paired_response_probe import C,I
    w.configure(args.root);original_context=w.build_seed_context
    w.build_seed_context=context


def context(args,numeric=False):
    s=original_context(args,numeric);E=s.E;q=s.q
    def iso(i,j,x):
        H=g.zero();H[i][j]=Q(1);H[j][i]=-g.eta[i]*g.eta[j]
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
    def part(v,j,spins):
        for k in spins:
            if k!=j:v=scale(Q(1,j*(j+1)-k*(k+1)),add(q['cas'](v),scale(-k*(k+1),v)))
        return v
    seeds=[];metadata=[]
    for j in (5,12):
        V=q['K'](3,s.bs[j]);W=iso(0,3,V);W=add(W,scale(-1,q['P'](W)))
        W6=part(W,6,[6,7]);L4=part(q['P'](q['K'](5,W6)),4,[4,5,6,7])
        assert q['cas'](W6)==scale(42,W6)
        assert L4 and q['cas'](L4)==scale(20,L4)
        assert q['P'](L4)==L4 and not q['K'](3,L4)
        assert s.rot(0,1,L4)==scale(4*I,L4)
        assert not add(s.rot(0,2,L4),scale(I,s.rot(1,2,L4)))
        other=part(q['P'](q['K'](8,W6)),4,[4,5,6,7]);assert other==scale(I,L4)
        seeds.append(L4);key=min(L4)
        metadata.append({'source_basis_index':j,'W6_terms':len(W6),'L4_terms':len(L4),'first_coefficient':[list(key),C(L4[key]).ser()]})
    s.seeds=seeds;s.spin4_metadata=metadata;s.iso=iso;s.part=part
    print('SPIN4 seeds exact',metadata,'seconds',time.monotonic()-s.start,flush=True)
    return s


def binding(args):
    paths=['tests/program-focus/source_action_weak_response_probe.py','tests/program-focus/source_action_paired_response_probe.py','tests/program-focus/source_normal_tensor_class_probe.py','lab/process/source-action-deep-coefficients.json']
    return {'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'native_inputs':{p:hashlib.sha256((args.root/p).read_bytes()).hexdigest()for p in paths}}


def xor_basis(labels):
    bs={}
    for x in labels:
        for p,b in sorted(bs.items(),reverse=True):
            if x>>p&1:x^=b
        if x:bs[x.bit_length()-1]=x
    return bs


def coset(x,bs):
    for p,b in sorted(bs.items(),reverse=True):
        if x>>p&1:x^=b
    return x


def stage_seeds(args):
    s=context(args);D=json.loads((args.root/'lab/process/source-action-deep-coefficients.json').read_text())
    bs=xor_basis([8]+[e^c for row in D['basis']for e,c,x in row]);assert len(bs)==11
    occupied=sorted({coset(e^c,bs)for v in s.seeds for e,c in v})
    # Coordinate support ceiling: all admissible W2 imaginary grades0,3 mod4
    # in reached XOR cosets. Rotation-highest/time constraints can shrink it.
    support=[(1<<a,c)for a in range(14)for c in range(16384)if c.bit_count()%4 in(0,3)and coset((1<<a)^c,bs)in occupied]
    weights=[0]*6+[1]*3+[-1]*3+[2,-2];dp={(0,0):1}
    for weight in weights:
        nxt=dict(dp)
        for (degree,m),count in dp.items():nxt[degree+1,m+weight]=nxt.get((degree+1,m+weight),0)+count
        dp=nxt
    char=Counter()
    for (degree,m),count in dp.items():
        if degree%4 in(0,3):
            for weight in weights:char[m+weight]+=count
    report={'scope':'Exact two source reconstruction and algebraic support bounds; no solve or cokernel verdict.','bindings':binding(args),'metadata':s.spin4_metadata,'exact_seeds':[s.q['ser'](v)for v in s.seeds],'root_results':[], 'full_highest_spin4_multiplicity':char[4]-char[5], 'family_plus_time_xor_rank':len(bs),'xor_basis':list(bs.values()),'occupied_cosets':occupied,'full_grade_coordinate_support_in_cosets':len(support),'raw_seed_support':len(set().union(*[set(v)for v in s.seeds])),'root_radii':[r['certificate']['radius']for r in D['certified_roots']]}
    write(args.output,report);print(json.dumps({k:v for k,v in report.items()if k not in('exact_seeds','bindings')},indent=2),flush=True)


def stage_numeric(args,scout=False):
    import numpy as np
    from scipy.sparse.linalg import LinearOperator,gmres
    s=context(args,True);D=json.loads((args.root/'lab/process/source-action-deep-coefficients.json').read_text())
    dense=w._dense_class()(list(map(float,g.d)));weights=np.abs(dense.phase)[None,:]/np.sqrt(np.abs(dense.d))[:,None]
    def rel(a,b):return s.norm(add(a,scale(-1,b)))/max(1.,s.norm(a),s.norm(b))
    sample={(1,0):1.,(8,7):.3j,(32,31):-.4};control={(2,3):.6,(16,0):1j,(256,15):.7}
    controls=[]
    for T,V in [(sample,control),(control,sample)]:
        got=dense.array_to_sparse(dense.from_matrix(dense.N(dense.to_matrix(dense.sparse_to_array(T)),dense.to_matrix(dense.sparse_to_array(V)))))
        err=rel(s.F.N(T,V),got);assert err<1e-10;controls.append(err)
    ac=(np.arange(16384)%97-48)/49+1j*(np.arange(16384)%31-15)/17
    rt=float(np.max(np.abs(dense.from_matrix(dense.to_matrix(ac))-ac)));assert rt<1e-10
    out={'scope':'NUMERICAL_DISCOVERY_ONLY; pruning/support and GMRES are not exact rank/solvability statements.','bindings':binding(args),'controls':{'native_N_errors':controls,'all16384_roundtrip_error':rt},'inner_iteration_cap':args.steps,'roots':[]}
    for ri,r in enumerate(D['certified_roots']):
        if args.root_index is not None and ri!=args.root_index:continue
        T={}
        for x,row in zip(r['coordinates'],D['basis']):
            for e,c,v in row:T[e,c]=T.get((e,c),0.)+float(x)*float(Q(v))
        T={k:v for k,v in T.items()if v};TM=dense.to_matrix(dense.sparse_to_array(T));adjT=dense.phi_adj(TM)
        for si,seed in enumerate(s.seeds):
            if args.source_index is not None and si!=args.source_index:continue
            times=[];last={};rhs=(dense.sparse_to_array(s.tofloat(seed))*weights).reshape(-1);ss=np.linalg.norm(rhs);rhs/=ss
            def mv(v):
                tick=time.monotonic();a=v.reshape(14,16384)/weights
                n=dense.from_matrix(dense.N(TM,dense.to_matrix(a),adjT));ns=dense.array_to_sparse(n,relative=args.prune)
                pn=s.project(ns);outarr=a+2*dense.sparse_to_array(pn);times.append(time.monotonic()-tick)
                last.update({'N_support':len(ns),'PN_support':len(pn),'P_cached_blocks':s.pblock.cache_info().currsize})
                print('SPIN4 root',ri,'seed',si,'matvec',len(times),'seconds',times[-1],last,flush=True)
                return (outarr*weights).reshape(-1)
            first=mv(rhs)
            if scout:
                yy=dense.array_to_sparse(first.reshape(14,16384)/weights*ss,relative=args.prune)
                rr={'root':ri,'source_index':si,'matvec_seconds':times,'stats':dict(last),'output_support':len(yy),'first_action':[[e,c,z.real,z.imag]for(e,c),z in sorted(yy.items())]}
            else:
                history=[]
                # legacy callback makes maxiter an INNER-iteration budget.
                op=LinearOperator((len(rhs),len(rhs)),matvec=mv,dtype=np.complex128)
                x,info=gmres(op,rhs,rtol=1e-10,atol=0.,restart=min(30,args.steps),maxiter=args.steps,callback=lambda v:history.append(float(v)),callback_type='legacy')
                residual=float(np.linalg.norm(mv(x)-rhs));yy=dense.array_to_sparse(x.reshape(14,16384)/weights*ss,relative=args.prune)
                rr={'root':ri,'source_index':si,'info':int(info),'relative_residual':residual,'solution':[[e,c,z.real,z.imag]for(e,c),z in sorted(yy.items())],'solution_support':len(yy),'matvec_seconds':times,'residual_history':history,'stats':dict(last),'rootball_certified':False}
            out['roots'].append(rr);write(args.output,out)
    print('COMPLETE',args.output,flush=True)


def stage_basis(args):
    """Exact highest4/time-kernel nullspace in discovered coordinate support.

    The support is a candidate. This stage proves all equations on its output,
    not closure under M and not completeness of the full highest4 carrier.
    """
    s=context(args);keys=set().union(*(set(v)for v in s.seeds))
    inputs=args.input or [args.cache/'inverse-stage2.json']
    input_hashes={}
    for path in inputs:
        dat=json.loads(path.read_text());input_hashes[str(path)]=hashlib.sha256(path.read_bytes()).hexdigest()
        for row in dat['roots']:
            for e,c,*_ in row.get('solution',row.get('first_action',[])):keys.add((int(e),int(c)))
    keys=sorted(keys)
    assert len(keys)<=args.max_support,('resource_cap_raise_explicitly',len(keys),args.max_support)
    piv={};basis=[];kernels=[];start=time.monotonic()
    # Sparse exact column elimination records kernel relations over Q(i).
    for index,key in enumerate(keys):
        unit={key:Q(1)}
        equations=(s.q['K'](3,unit),add(s.rot(0,1,unit),scale(-4*I,unit)),add(s.rot(0,2,unit),scale(I,s.rot(1,2,unit))))
        v={(tag,e,c):C(x)for tag,u in enumerate(equations)for(e,c),x in u.items()};cs={index:C(1)}
        while v:
            pp=min(v)
            if pp not in piv:
                z=v[pp];v={k:x/z for k,x in v.items()};cs={k:x/z for k,x in cs.items()};piv[pp]=len(basis);basis.append((v,cs));break
            b,bc=basis[piv[pp]];z=v[pp]
            for k,x in b.items():
                y=v.get(k,C())-z*x
                if y:v[k]=y
                elif k in v:del v[k]
            for k,x in bc.items():
                y=cs.get(k,C())-z*x
                if y:cs[k]=y
                elif k in cs:del cs[k]
        if not v:kernels.append(cs)
        if (index+1)%128==0:
            progress={'scope':'INCOMPLETE basis-stage progress; not a mathematical result.','processed':index+1,'support':len(keys),'constraint_rank':len(basis),'nullity_so_far':len(kernels),'seconds':time.monotonic()-start}
            write(args.cache/'spin4-basis-progress.json',progress);print('SPIN4 basis',progress,flush=True)
    fields=[{keys[j]:x for j,x in rel.items()}for rel in kernels]
    for v in fields:
        assert s.rot(0,1,v)==scale(4*I,v)
        assert not add(s.rot(0,2,v),scale(I,s.rot(1,2,v)))
        assert not s.q['K'](3,v)
    redbasis=[];pivots=[]
    for v in fields:
        for pp,b in zip(pivots,redbasis):
            z=v.get(pp,0)
            if z:v=add(v,scale(-z,b))
        assert v;pp=min(v);redbasis.append(scale(1/v[pp],v));pivots.append(pp)
    for source in s.seeds:
        rem=source
        for pp,b in zip(pivots,redbasis):
            z=rem.get(pp,0)
            if z:rem=add(rem,scale(-z,b))
        assert not rem,('source_outside',len(rem))
    out={'scope':'Exact complete highest4/time-kernel space INSIDE the recorded coordinate support. M closure not yet certified.','bindings':binding(args),'input_hashes':input_hashes,'raw_support_dimension':len(keys),'constraint_rank':len(basis),'highest4_timekernel_dimension':len(fields),'both_seeds_in_space':True,'basis':[s.q['ser'](v)for v in redbasis],'basis_pivots':[list(pp)for pp in pivots],'seconds':time.monotonic()-start}
    write(args.output,out);print('SPIN4 basis DONE',len(fields),'support',len(keys),'seconds',out['seconds'],flush=True)


def stage_closure(args):
    bd=json.loads((args.cache/'inverse-stage3-basis.json').read_text());n=len(bd['basis'])
    assert n<=args.max_dimension,('resource_cap_raise_explicitly',n,args.max_dimension)
    # Native generic closure: same exact Engine.N, P and 59 backgrounds; the
    # replaced build_seed_context supplies highest4 sources, not old spin5.
    w.mode_closure(args)
    out=json.loads(args.output.read_text());out['scope']='Exact all59-background invariant receiver envelope for reached highest4 sources; complete iff completed==dimension. Not complete ambient spin4 or a cokernel verdict.'
    out['spin4_script_bindings']=binding(args);out['rotation_spin']=4
    write(args.output,out)


def stage_certify(args):
    cl=json.loads((args.cache/'inverse-stage4-closure-certified.json').read_text());n=cl['dimension']
    assert n<=args.max_dimension,('resource_cap_raise_explicitly',n,args.max_dimension)
    assert cl['completed']==n and not cl.get('failure')
    # Native generic Neumann certificate verifies R*M exactly as Q(i), then
    # adds the existing entire 59-coordinate rootball. Float inverse is only
    # a candidate; passing exact eta<1 is the proof.
    w.mode_certify(args)
    out=json.loads(args.output.read_text());out['scope']='Exact rootball certificate for the reached highest4 invariant receiver envelope. Passing both roots supplies preimages for both owned seeds in the full native N. Failure is INCONCLUSIVE unless paired with a separately validated actual ambient adjoint kernel.'
    out['spin4_script_bindings']=binding(args);out['rotation_spin']=4
    out['both_roots_solved']=len(out['roots'])==2 and all(r['invertible_on_block_over_rootball'] and len(r.get('sources',[]))==2 for r in out['roots'])
    write(args.output,out)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True,type=Path);ap.add_argument('--cache',required=True,type=Path);ap.add_argument('--output',type=Path)
    ap.add_argument('--mode',choices=['seeds','scout','numeric','basis','closure','legacy-certify','certify','validate-basis','integer-closure','controls','benchmark','unpack','status'],default='seeds');ap.add_argument('--steps',type=int,default=20);ap.add_argument('--root-index',type=int,choices=[0,1]);ap.add_argument('--source-index',type=int,choices=[0,1]);ap.add_argument('--generate-candidates',action='store_true');ap.add_argument('--precision',type=int,default=24);ap.add_argument('--prune',type=float,default=1e-13);ap.add_argument('--input',type=Path,nargs='+');ap.add_argument('--max-support',type=int,default=20000);ap.add_argument('--max-dimension',type=int,default=512)
    args=ap.parse_args();args.root=args.repo.resolve();args.cache=args.cache.resolve();args.cache.mkdir(parents=True,exist_ok=True)
    names={'seeds':'inverse-stage1.json','scout':'spin4-scout.json','numeric':'inverse-stage2.json','basis':'inverse-stage3-basis.json','closure':'inverse-stage4-closure-certified.json','legacy-certify':'inverse-stage5-certificate.json','certify':'spin4-fast-certificate.json','validate-basis':'spin4-basis-validation.json','integer-closure':'spin4-closure-integer-v2.json','controls':'spin4-controls.json','benchmark':'spin4-benchmark.json','unpack':'spin4-unpack.json','status':'spin4-status.json'}
    args.output=args.output or args.cache/names[args.mode];load(args)
    if args.mode=='seeds':stage_seeds(args)
    elif args.mode=='scout':stage_numeric(args,True)
    elif args.mode=='numeric':stage_numeric(args)
    elif args.mode=='basis':stage_basis(args)
    elif args.mode=='closure':stage_closure(args)
    elif args.mode=='legacy-certify':stage_certify(args)
    elif args.mode=='certify':sn_run(args,sys.modules[__name__])
    elif args.mode=='validate-basis':sn_basis_stage(args,sys.modules[__name__])
    elif args.mode=='integer-closure':stage_resume_integer_closure(args)
    elif args.mode=='controls':stage_controls(args)
    elif args.mode=='benchmark':stage_benchmark(args)
    elif args.mode=='unpack':stage_unpack(args)
    elif args.mode=='status':stage_status(args)



from functools import lru_cache
from math import gcd, lcm
import random, inspect
ZERO = (0, 0)

def accumulate(out, key, re, im):
    if re or im:
        old = out.get(key)
        if old is None:
            out[key] = (re, im)
        else:
            a, b = old
            out[key] = (a + re, b + im)

def prune(out):
    return {k: z for k, z in out.items() if z[0] or z[1]}


def add_into(out, other, multiplier=1):
    for key, (re, im) in other.items():
        accumulate(out, key, multiplier * re, multiplier * im)


class IntegerScaledN:
    """Drop-in Phi/Phi_adj/wadj/N API; inputs must remain immutable while cached.

    Prepared input references are retained so object IDs cannot be reused.
    Call clear_prepared() after a batch to release retained vectors if desired.
    Geometry is checked against the owned14D rational metric, not inferred.
    """
    def __init__(self, geometry):
        from source_action_paired_response_probe import C
        self.C = C
        self.d = tuple(int(x) for x in geometry.d)
        assert all(Q(x) == y for x, y in zip(geometry.d, self.d))
        assert self.d == (1, 1, 1, -1, -16, 8, 24, 48, 8, 8, -8, 8, -8, -8)
        self.dim = len(self.d); self.negative = sum(x < 0 for x in self.d)
        self.L = lcm(*(abs(x) for x in self.d))
        self.Dphi = 2 * self.L * self.L
        self.Dadj = 2 * self.L
        assert (self.L, self.Dphi, self.Dadj) == (48, 4608, 96)
        assert self.L * self.Dadj == self.Dphi
        # Mask metric factors and degrees need only16384 integer entries.
        self.metric = [1] * (1 << self.dim)
        self.degree = [0] * (1 << self.dim)
        for mask in range(1, 1 << self.dim):
            bit = mask & -mask; rest = mask ^ bit
            self.metric[mask] = self.metric[rest] * self.d[bit.bit_length()-1]
            self.degree[mask] = self.degree[rest] + 1
        self._prepared = {}

    def clear_prepared(self):
        self._prepared.clear()

    @staticmethod
    @lru_cache(maxsize=262144)
    def sign(a, b):
        parity = 0
        while a:
            low = a & -a; parity ^= (b & (low-1)).bit_count() & 1; a ^= low
        return -1 if parity else 1

    @lru_cache(maxsize=262144)
    def cmul(self, a, b):
        return a ^ b, self.sign(a, b) * self.metric[a & b]

    @staticmethod
    def split_one(v):
        out = {}
        for (e, c), z in v.items():
            assert e and not (e & (e-1)), 'Expected one-form'
            out.setdefault(e.bit_length()-1, {})[c] = z
        return out

    @staticmethod
    def split_two(v):
        out = {}
        for (e, c), z in v.items():
            low = e & -e; high = e ^ low
            assert low and high and not (high & (high-1)), 'Expected two-form'
            out.setdefault((low.bit_length()-1, high.bit_length()-1), {})[c] = z
        return out

    def clear_denominators(self, vector):
        """One positive common rational denominator, with exact integer pairs."""
        coeff = {}
        den = 1
        for key, z in vector.items():
            if hasattr(z, 'a') and hasattr(z, 'b'):
                a, b = Q(z.a), Q(z.b)
            else:
                a, b = Q(z), Q(0)
            if a or b:
                coeff[key] = (a, b)
                den = lcm(den, a.denominator, b.denominator)
        ints = {key: (a.numerator * (den // a.denominator),
                      b.numerator * (den // b.denominator))
                for key, (a, b) in coeff.items()}
        common = den
        for a, b in ints.values():
            common = gcd(common, a); common = gcd(common, b)
            if common == 1: break
        if common > 1:
            den //= common
            ints = {k: (a // common, b // common) for k, (a, b) in ints.items()}
        return den, ints

    def restore(self, vector, denominator):
        assert isinstance(denominator, int) and denominator > 0
        C = self.C
        return {k: C(Q(a, denominator), Q(b, denominator))
                for k, (a, b) in vector.items() if a or b}

    def blade_into(self, out, blade, vector, multiplier, kind):
        """Add multiplier*[blade,vector] or {blade,vector}, entirely integral."""
        if not vector or not multiplier: return
        degree = self.degree[blade]
        for c, (a, b) in vector.items():
            odd = (degree * self.degree[c] - self.degree[blade & c]) & 1
            if odd != (kind == 'comm'): continue
            target, factor = self.cmul(blade, c); factor *= 2 * multiplier
            accumulate(out, target, factor * a, factor * b)

    def product_into(self, out, left, right, multiplier=1, kind='comm'):
        if not multiplier or not left or not right: return
        wanted = kind == 'comm'
        for ca, (ar, ai) in left.items():
            degree = self.degree[ca]
            for cb, (br, bi) in right.items():
                odd = (degree * self.degree[cb] - self.degree[ca & cb]) & 1
                if odd != wanted: continue
                target, factor = self.cmul(ca, cb); factor *= 2 * multiplier
                # Real coefficient branches are common for all59 background T.
                if not ai:
                    re, im = ar * br, ar * bi
                elif not bi:
                    re, im = ar * br, ai * br
                else:
                    re, im = ar * br - ai * bi, ar * bi + ai * br
                accumulate(out, target, factor * re, factor * im)

    def wedge_comm_int(self, U, V):
        us = self.split_one(U); vs = self.split_one(V); out = {}
        for i in range(self.dim):
            ui = us.get(i, {}); vi = vs.get(i, {})
            for j in range(i+1, self.dim):
                row = {}
                self.product_into(row, ui, vs.get(j, {}))
                self.product_into(row, us.get(j, {}), vi, -1)
                e = (1 << i) | (1 << j)
                for c, z in row.items():
                    if z[0] or z[1]: out[e, c] = z
        return out

    def Phi_scaled(self, X):
        """Dphi * Phi(X), for Gaussian-integer X."""
        out = [{} for _ in range(self.dim)]; Z = {}
        for (i, j), row in self.split_two(X).items():
            self.blade_into(out[j], 1 << i, row, -self.Dphi // self.d[i], 'comm')
            self.blade_into(out[i], 1 << j, row, self.Dphi // self.d[j], 'comm')
            # Z = (Dphi/2) sum (di*dj)^-1 {gamma_ij, X_ij}.
            factor = self.L * self.L // (self.d[i] * self.d[j])
            assert factor * self.d[i] * self.d[j] == self.L * self.L
            self.blade_into(Z, (1 << i) | (1 << j), row, factor, 'anti')
        Z = prune(Z)
        for j in range(self.dim):
            self.blade_into(out[j], 1 << j, Z, -1, 'anti')
        return {(1 << j, c): z for j, row in enumerate(out)
                for c, z in row.items() if z[0] or z[1]}

    def Phi_adj_scaled(self, V):
        """Dadj * Phi_adj(V), for Gaussian-integer V."""
        vs = self.split_one(V); A = {}; out = {}
        for i, row in vs.items():
            self.blade_into(A, 1 << i, row, self.L // self.d[i], 'anti')
        A = prune(A)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                row = {}
                self.blade_into(row, 1 << i, vs.get(j, {}), self.Dadj, 'comm')
                self.blade_into(row, 1 << j, vs.get(i, {}), -self.Dadj, 'comm')
                self.blade_into(row, (1 << i) | (1 << j), A, -1, 'anti')
                e = (1 << i) | (1 << j)
                for c, z in row.items():
                    if z[0] or z[1]: out[e, c] = z
        return out

    def wadj_scaled(self, U, W):
        """L * wadj(U,W), for Gaussian-integer U,W."""
        us = self.split_one(U); out = [{} for _ in range(self.dim)]
        for (i, j), row in self.split_two(W).items():
            self.product_into(out[j], us.get(i, {}), row, -self.L // self.d[i])
            self.product_into(out[i], us.get(j, {}), row, self.L // self.d[j])
        return {(1 << j, c): z for j, row in enumerate(out)
                for c, z in row.items() if z[0] or z[1]}

    def prepare(self, vector):
        key = id(vector); old = self._prepared.get(key)
        if old is not None:
            assert old[0] is vector
            return old[1:]
        den, ints = self.clear_denominators(vector)
        adj = self.Phi_adj_scaled(ints)
        self._prepared[key] = (vector, den, ints, adj)
        return den, ints, adj

    def Phi(self, X):
        den, ints = self.clear_denominators(X)
        return self.restore(self.Phi_scaled(ints), self.Dphi * den)

    def Phi_adj(self, V):
        den, ints, adj = self.prepare(V)
        return self.restore(adj, self.Dadj * den)

    def wadj(self, U, W):
        du, ui = self.clear_denominators(U); dw, wi = self.clear_denominators(W)
        return self.restore(self.wadj_scaled(ui, wi), self.L * du * dw)

    def N(self, U, V):
        du, ui, au = self.prepare(U); dv, vi, av = self.prepare(V)
        numerator = self.Phi_scaled(self.wedge_comm_int(ui, vi))
        add_into(numerator, self.wadj_scaled(ui, av))
        add_into(numerator, self.wadj_scaled(vi, au))
        # Each numerator summand is Dphi times its unscaled native term.
        return self.restore(numerator, 6 * self.Dphi * du * dv)


def integer_controls(repo):
    sys.path.insert(0, str(repo / 'tests/program-focus'))
    import source_action_deep_geometry as g
    import source_action_weak_response_probe as w
    from source_action_paired_response_probe import C
    w.configure(repo); old = w._fast_exact_class()(g); new = IntegerScaledN(g)
    start = time.monotonic(); checks = []
    def check(label, left, right):
        assert left == right, (label, left, right)
        checks.append(label)
    # Every Clifford grade0..14, including the non-imaginary control grades.
    for a in (0, 3, 13):
        for degree in range(15):
            v = {(1 << a, (1 << degree)-1): C(Q(2, 3), Q(-5, 7))}
            check('Phi_adj axis%d grade%d' % (a, degree), new.Phi_adj(v), old.Phi_adj(v))
    for a in range(14):
        v = {(1 << a, (1 << ((a+4) % 15))-1): Q(11, 13)}
        check('Phi_adj allaxis%d' % a, new.Phi_adj(v), old.Phi_adj(v))
    for i, j in ((0, 1), (0, 3), (3, 4), (5, 8), (10, 13)):
        for degree in range(15):
            v = {((1 << i) | (1 << j), (1 << degree)-1): C(Q(-3, 5), Q(7, 11))}
            check('Phi pair%d,%d grade%d' % (i, j, degree), new.Phi(v), old.Phi(v))
    rng = random.Random(20261126)
    def field(n):
        out = {}
        for _ in range(n):
            out[(1 << rng.randrange(14), rng.randrange(16384))] = C(Q(rng.randint(-9, 9), rng.randint(1, 13)), Q(rng.randint(-9, 9), rng.randint(1, 13)))
        return out
    for case in range(8):
        U, V = field(3), field(4)
        check('N Gaussian-rational%d' % case, new.N(U, V), old.N(U, V))
        check('N symmetry%d' % case, new.N(U, V), new.N(V, U))
        check('wadj Gaussian-rational%d' % case, new.wadj(U, old.Phi_adj(V)), old.wadj(U, old.Phi_adj(V)))
    # Bilinearity tests catch accidental denominator/scale handling errors.
    from source_action_deep_algebra import add, scale
    U, V, Z = field(2), field(2), field(2); a = C(Q(3, 17), Q(2, 19))
    check('N exact complex scaling', new.N(scale(a, U), V), scale(a, new.N(U, V)))
    check('N exact addition', new.N(add(U, Z), V), add(new.N(U, V), new.N(Z, V)))
    check('N zero input', new.N({}, V), {})
    return {'scope':'Exact finite engine-equivalence controls, not closure/root solvability. Algebraic scaling proof supplies all-input equivalence.', 'checks':len(checks), 'all_passed':True, 'seconds':time.monotonic()-start, 'scales':{'L':new.L,'Dphi':new.Dphi,'Dadj':new.Dadj,'N_denominator_factor':6*new.Dphi}, 'labels':checks,
            'bindings':{'integer_engine_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'native_weak_probe_sha256':hashlib.sha256((repo/'tests/program-focus/source_action_weak_response_probe.py').read_bytes()).hexdigest(), 'native_algebra_sha256':hashlib.sha256((repo/'tests/program-focus/source_action_deep_algebra.py').read_bytes()).hexdigest()}}



def integer_engine_digest():
    functions=(accumulate,prune,add_into,IntegerScaledN)
    return hashlib.sha256('\n'.join(inspect.getsource(f) for f in functions).encode()).hexdigest()


def integer_binding(args):
    return {'format':'spin4-sparse-integer-v2','engine_sha256':integer_engine_digest(),
            'projection_sha256':hashlib.sha256('\n'.join(inspect.getsource(f) for f in (clear_matrix,integer_matvec,IntegerKernelProjection)).encode()).hexdigest(),
            'closure_procedure_sha256':hashlib.sha256(inspect.getsource(stage_integer_closure).encode()).hexdigest(),
            'basis_sha256':w.file_digest(args.cache/'inverse-stage3-basis.json'),
            'background_sha256':w.file_digest(args.root/'lab/process/source-action-deep-coefficients.json'),
            'native_inputs':w.native_bindings(args.root)}


def stage_integer_closure(args):
    s=context(args);checks=integer_controls(args.root);E=IntegerScaledN(g);ip=IntegerKernelProjection(s.q,E)
    bd=json.loads((args.cache/'inverse-stage3-basis.json').read_text())
    bb=[{(e,c):C(Q(x),Q(y))for e,c,(x,y)in row}for row in bd['basis']]
    piv=[tuple(x)for x in bd['basis_pivots']];n=len(bb)
    assert n<=args.max_dimension
    data=json.loads((args.root/'lab/process/source-action-deep-coefficients.json').read_text())
    Ts=[{(e,c):Q(z)for e,c,z in row}for row in data['basis']]
    for T in Ts:E.prepare(T)
    def reduce(v):
        cs=[]
        for pp,b in zip(piv,bb):
            z=C(v.get(pp,0));cs.append(z)
            if z:v=add(v,scale(-z,b))
        return v,cs
    bindings=integer_binding(args)
    out={'scope':'Exact282-envelope family closure only if all columns complete; sparse coordinates, no ambient cokernel assertion.',
         'bindings':bindings,'dimension':n,'maps':len(Ts),'completed':0,'columns':[],
         'engine_controls':checks,'source_revision':__import__('subprocess').check_output(['git','rev-parse','HEAD'],cwd=args.root,text=True).strip()}
    if args.output.exists():
        out=json.loads(args.output.read_text());assert out['bindings']==bindings
        assert out['completed']==len(out['columns']) and not out.get('failure')
    oldpath=args.cache/'inverse-stage4-closure-certified.json'
    old=json.loads(oldpath.read_text())if oldpath.exists()else None
    start=time.monotonic();begin=out['completed'];end=n if args.steps==0 else min(n,begin+args.steps)
    for bi in range(begin,end):
        cols=[]
        for j,T in enumerate(Ts):
            du,ui,au=E.prepare(T);dv,vi,av=E.prepare(bb[bi])
            numerator=E.Phi_scaled(E.wedge_comm_int(ui,vi))
            add_into(numerator,E.wadj_scaled(ui,av));add_into(numerator,E.wadj_scaled(vi,au))
            image=ip.apply_integer(numerator,3*E.Dphi*du*dv);rem,cs=reduce(image)
            if rem:
                out['failure']={'basis':bi,'background':j,'outside_terms':len(rem),'witness':s.q['ser'](rem)[:5]}
                write(args.output,out);raise AssertionError(out['failure'])
            if old and bi<old['completed']:
                assert [C(z).ser()for z in cs]==old['columns'][bi][j],('legacy_column_mismatch',bi,j)
            cols.append([[i,*C(z).ser()]for i,z in enumerate(cs)if z])
        out['columns'].append(cols);out['completed']=bi+1
        write(args.output,out)
        print('INTEGER closure',bi+1,'/',n,'maps',len(Ts),'seconds',time.monotonic()-start,flush=True)
    print('INTEGER closure DONE',out['completed'],'of',n,flush=True)

def clear_matrix(rows):
    """Return one exact positive denominator and sparse integer matrix rows."""
    den = 1
    rows = [{j: Q(x) for j, x in row.items() if x} for row in rows]
    for row in rows:
        for x in row.values(): den = lcm(den, x.denominator)
    ints = [tuple((j, x.numerator * (den // x.denominator))
                  for j, x in sorted(row.items())) for row in rows]
    common = den
    for row in ints:
        for _, x in row: common = gcd(common, x)
        if common == 1: break
    if common > 1:
        den //= common
        ints = [tuple((j, x // common) for j, x in row) for row in ints]
    # Exact reconstruction is checked once when each factor is cached.
    assert all({j: Q(x, den) for j, x in ir} == row
               for ir, row in zip(ints, rows))
    return den, tuple(ints)


def integer_matvec(rows, vector):
    """Sparse integer matrix times vector of exact Gaussian-integer pairs."""
    out = []
    for row in rows:
        real = imag = 0
        for j, coefficient in row:
            a, b = vector[j]
            real += coefficient * a
            imag += coefficient * b
        out.append((real, imag))
    return out


class IntegerKernelProjection:
    def __init__(self, q, integerEngine):
        self.q = q; self.engine = integerEngine
        self.E = q['E']; self.C = q['C']
        assert self.E.dim == 14
        assert tuple(self.E.d) == tuple(integerEngine.d)
        self._blocks = {}; self.calls = 0; self.groups_applied = 0

    def block(self, r):
        """Cache exact factors on one native paired-time XOR block."""
        old = self._blocks.get(r)
        if old is not None: return old
        assert r >= 0 and r < 16384 and not (r & 8)
        zs, gi = self.q['block'](r)
        keys = tuple((1 << i, (1 << i) ^ r ^ z)
                     for z in (0, 8) for i in range(14))
        assert len(set(keys)) == 28
        index = {k: i for i, k in enumerate(keys)}
        n = len(zs)
        assert len(gi) == n and all(len(row) == n for row in gi)
        # Z has native kernel basis columns. B=Z^T W uses the exact same
        # real diagonal trace/form pairing as native E.pair.
        Z = [{} for _ in keys]; B = [{} for _ in zs]
        for j, vector in enumerate(zs):
            assert set(vector) <= set(keys)
            for key, coefficient in vector.items():
                coefficient = Q(coefficient)
                if coefficient:
                    i = index[key]
                    Z[i][j] = coefficient
                    B[j][i] = coefficient * self.E.weight(*key)
        G = [{j: Q(x) for j, x in enumerate(row) if x} for row in gi]
        dz, zi = clear_matrix(Z); dg, gii = clear_matrix(G); db, bi = clear_matrix(B)
        ans = {'keys': keys, 'index': index, 'kernel_dimension': n,
               'Z': zi, 'Ginv': gii, 'B': bi,
               'factor_denominators': (dz, dg, db),
               'denominator': dz * dg * db}
        self._blocks[r] = ans
        return ans

    def apply_integer(self, vector, denominator=1):
        """Apply P to Gaussian-integer numerator / positive denominator.

        This optional seam allows a caller to avoid restoring N's intermediate
        fractions; ordinary __call__ already handles all native Q(i) inputs.
        """
        assert isinstance(denominator, int) and denominator > 0
        groups = {}
        for (e, c), z in vector.items():
            assert e and not (e & (e-1)) and e < (1 << 14)
            assert 0 <= c < 16384
            assert len(z) == 2 and all(isinstance(a, int) for a in z)
            if z[0] or z[1]: groups.setdefault((e ^ c) & ~8, {})[e, c] = z
        out = {}; self.calls += 1
        for r, part in groups.items():
            block = self.block(r); self.groups_applied += 1
            values = [part.get(key, (0, 0)) for key in block['keys']]
            values = integer_matvec(block['B'], values)
            values = integer_matvec(block['Ginv'], values)
            values = integer_matvec(block['Z'], values)
            den = denominator * block['denominator']
            # Different r blocks have disjoint output supports.
            for key, (a, b) in zip(block['keys'], values):
                if a or b:
                    assert key not in out
                    out[key] = self.C(Q(a, den), Q(b, den))
        return out

    def __call__(self, vector):
        den, ints = self.engine.clear_denominators(vector)
        return self.apply_integer(ints, den)

    def metadata(self):
        return {'cached_blocks': len(self._blocks), 'calls': self.calls,
                'groups_applied': self.groups_applied,
                'blocks': [{'r': r, 'kernel_dimension': b['kernel_dimension'],
                            'factor_denominators': list(b['factor_denominators'])}
                           for r, b in sorted(self._blocks.items())]}



def projection_controls(repo):
    sys.path.insert(0, str(repo/'tests/program-focus'))
    import source_action_deep_geometry as g
    from source_action_deep_algebra import Engine, add, scale
    from source_action_paired_response_probe import C, build_api
    ie = IntegerScaledN(g)
    # P/K construction does not need h rotations or the expensive seed context.
    q = build_api(repo, {'C': C, 'E': Engine(g), 'h': SimpleNamespace()})
    ip = IntegerKernelProjection(q, ie)
    tick = time.monotonic(); names = []
    def check(label, lhs, rhs):
        assert lhs == rhs, (label, lhs, rhs)
        names.append(label)
    keys = []
    for r in (0, 7, 16):
        block = ip.block(r); keys.extend(block['keys'])
        for i, key in enumerate(block['keys']):
            v = {key: C(Q(2, 3), Q(-5, 7))}
            got = ip(v)
            check('native unit r%d col%d' % (r, i), got, q['P'](v))
            check('timekernel r%d col%d' % (r, i), q['K'](3, got), {})
    rng = random.Random(20261126)
    def random_field():
        v = {}
        for key in rng.sample(keys, 9):
            v[key] = C(Q(rng.randint(-10, 10), rng.randint(1, 17)), Q(rng.randint(-10, 10), rng.randint(1, 17)))
        return v
    for i in range(6):
        v = random_field(); got = ip(v)
        check('random native%d' % i, got, q['P'](v))
        check('random idempotence%d' % i, ip(got), got)
        den, ints = ie.clear_denominators(v)
        check('cleared input seam%d' % i, ip.apply_integer(ints, den), got)
    u, v = random_field(), random_field(); a = C(Q(3, 11), Q(-7, 13))
    check('complex linearity', ip(scale(a, u)), scale(a, ip(u)))
    check('addition', ip(add(u, v)), add(ip(u), ip(v)))
    check('zero', ip({}), {})
    check('native bilinear adjoint', q['E'].pair(ip(u), v), q['E'].pair(u, ip(v)))
    return {'scope':'Exact factor arithmetic and finite native projection agreement. Not a receiver/root certificate.',
            'checks':len(names), 'all_passed':True, 'seconds':time.monotonic()-tick,
            'labels':names, 'cache':ip.metadata(),
            'bindings':{'projection_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                        'integer_engine_sha256':integer_engine_digest(),
                        'paired_probe_sha256':hashlib.sha256((repo/'tests/program-focus/source_action_paired_response_probe.py').read_bytes()).hexdigest()}}



def covariance_countermodel_controls():
    """Tiny exact generic control; the accompanying proof supplies scope.

    Uses only standard-library Fraction. No native GU engine or external
    scratch import. The model is not identified with the W2/K95 candidate.
    """
    from fractions import Fraction as Q

    n=4
    g=[Q(-1),Q(1),Q(1),Q(1)]
    def zmat(): return [[Q(0) for _ in range(n)] for _ in range(n)]
    def zvec(): return [Q(0) for _ in range(n)]
    def addmat(a,b): return [[a[i][j]+b[i][j] for j in range(n)] for i in range(n)]
    def add(x,y): return (addmat(x[0],y[0]),[a+b for a,b in zip(x[1],y[1])])
    def neg(x): return ([[-v for v in row] for row in x[0]],[-v for v in x[1]])
    ZERO=(zmat(),zvec())
    def basisvec(i):
     v=zvec();v[i]=Q(1);return v

    def pair(x,y):
     S,v=x;T,w=y
     return sum(g[i]*g[j]*S[i][j]*T[i][j] for i in range(n) for j in range(n))+sum(g[i]*v[i]*w[i] for i in range(n))
    def K(b,x):
     S,v=x
     return ([[ (b[i]*v[j]+v[i]*b[j])/2 for j in range(n)] for i in range(n)],[-sum(g[j]*b[j]*S[j][i] for j in range(n)) for i in range(n)])
    def P(x):
     S,v=x
     return ([[S[i][j] if i and j else Q(0) for j in range(n)] for i in range(n)],zvec())
    def R(x):return add(x,neg(P(x)))
    def J(x):
     S,v=x;tr=sum(g[i]*S[i][i] for i in range(n))
     return ([[S[i][j]-(g[i]*tr/3 if i==j else 0) for j in range(n)] for i in range(n)],v[:])
    def M(x):return P(J(P(x)))
    def Av(A,v):return [sum(A[i][j]*v[j] for j in range(n)) for i in range(n)]
    def rho(A,x):
     S,v=x
     return ([[sum(A[i][k]*S[k][j]+A[j][k]*S[i][k] for k in range(n)) for j in range(n)] for i in range(n)],Av(A,v))
    basis=[]
    for i in range(n):
     for j in range(i,n):
      S=zmat();S[i][j]=S[j][i]=Q(1);basis.append((S,zvec()))
    for i in range(n):basis.append((zmat(),basisvec(i)))
    assert len(basis)==14
    As=[]
    for i in range(n):
     for j in range(i+1,n):
      A=zmat();A[i][j]=Q(1);A[j][i]=-g[i]*g[j];As.append(A)
    checks=0
    for x in basis:
     assert P(P(x))==P(x);checks+=1
     assert K(basisvec(0),P(x))==ZERO;checks+=1
     for b in map(basisvec,range(n)):
      assert P(K(b,P(x)))==ZERO;checks+=1
     for A in As:
      assert rho(A,J(x))==J(rho(A,x));checks+=1
      for b in map(basisvec,range(n)):
       assert add(rho(A,K(b,x)),neg(K(b,rho(A,x))))==K(Av(A,b),x);checks+=1
     for y in basis:
      assert pair(P(x),y)==pair(x,P(y));checks+=1
      assert pair(J(x),y)==pair(x,J(y));checks+=1
      for A in As:
       assert pair(rho(A,x),y)+pair(x,rho(A,y))==0;checks+=1
      for b in map(basisvec,range(n)):
       assert pair(K(b,x),y)+pair(x,K(b,y))==0;checks+=1
    V=(zmat(),basisvec(0));Y=ZERO;A=As[0];b=basisvec(1)
    assert R(V)==V
    assert all(P(K(c,V))==ZERO for c in map(basisvec,range(n)))
    t=P(K(b,R(rho(A,V))))
    expected=zmat();expected[1][1]=Q(1)
    assert t==(expected,zvec())
    kS=zmat()
    for i in range(1,4):kS[i][i]=Q(1)
    k=(kS,zvec())
    assert M(k)==ZERO and pair(k,t)==1
    for x in basis:
     assert pair(k,M(x))==0
     assert M(M(x))==M(x)
    rhs=add(M(P(rho(A,Y))),add(P(J(R(rho(A,Y)))),add(neg(P(rho(A,R(J(Y))))),add(neg(P(K(Av(A,b),V))),P(rho(A,R(K(b,V))))))))
    assert t==rhs
    # A second direct-summand copy with J=Id makes the old source nonzero
    # while the original adjoint obstruction survives unchanged.
    W=(zmat(),basisvec(1))
    assert P(K(b,W))==t
    assert P(K(b,R(rho(A,W))))==ZERO
    return {'scope':'INTERNAL_STRUCTURAL_ONLY generic Lorentz-covariant countermodel; no W2/K95 or source/candidate verdict.',
            'exact_premise_checks':checks,'dimension':14,
            'old_sources_all_zero':True,'new_source_equals_e1_tensor_e1':True,
            'adjoint_kernel_pairing':'1','M_projection_to_spatial_traceless':True,
            'full_carrier_J_invertible':True,'identity_verified':True,
            'nonzero_old_source_direct_sum_available':True}


def projected_cubic(engine, projection, U, V, multiplier=2):
    """Exact reusable multiplier*P*N(U,V); hold prepared inputs immutable."""
    assert isinstance(multiplier,int)
    du,ui,au=engine.prepare(U);dv,vi,av=engine.prepare(V)
    numerator=engine.Phi_scaled(engine.wedge_comm_int(ui,vi))
    add_into(numerator,engine.wadj_scaled(ui,av));add_into(numerator,engine.wadj_scaled(vi,au))
    numerator={k:(multiplier*a,multiplier*b)for k,(a,b)in numerator.items()}
    return projection.apply_integer(numerator,6*engine.Dphi*du*dv)


def stage_controls(args):
    result={'scope':'Exact arithmetic/structural controls, no physical or root verdict.',
            'integer_cubic':integer_controls(args.root),
            'integer_projection':projection_controls(args.root),
            'covariance_countermodel':covariance_countermodel_controls()}
    write(args.output,result)
    print(json.dumps({k:v.get('checks',v.get('exact_premise_checks'))for k,v in result.items()if isinstance(v,dict)}),flush=True)


def stage_benchmark(args):
    s=context(args);E=IntegerScaledN(g);ip=IntegerKernelProjection(s.q,E);old=w._fast_exact_class()(g)
    bd=json.loads((args.cache/'inverse-stage3-basis.json').read_text())
    v={(e,c):C(Q(a),Q(b))for e,c,(a,b)in bd['basis'][0]}
    data=json.loads((args.root/'lab/process/source-action-deep-coefficients.json').read_text())
    Ts=[{(e,c):Q(z)for e,c,z in data['basis'][j]}for j in (0,1,10)]
    rows=[]
    for j,T in zip((0,1,10),Ts):
        tick=time.perf_counter();reference=s.q['P'](scale(2,old.N(T,v)));reference_seconds=time.perf_counter()-tick
        tick=time.perf_counter();got=projected_cubic(E,ip,T,v);fast_seconds=time.perf_counter()-tick
        assert got==reference,('benchmark_exact_mismatch',j)
        rows.append({'background':j,'exact_match':True,'reference_seconds':reference_seconds,'integer_seconds':fast_seconds,'output_terms':len(got)})
    # A warm replay compares the same data after both native factor caches exist.
    warm=[]
    for j,T in zip((0,1,10),Ts):
        tick=time.perf_counter();reference=s.q['P'](scale(2,old.N(T,v)));a=time.perf_counter()-tick
        tick=time.perf_counter();got=projected_cubic(E,ip,T,v);b=time.perf_counter()-tick
        assert got==reference
        warm.append({'background':j,'exact_match':True,'reference_seconds':a,'integer_seconds':b})
    out={'scope':'Local timing of identical exact2PN maps; hardware-dependent, not a scientific result.',
         'bindings':integer_binding(args),'cold':rows,'warm':warm,
         'warm_reference_seconds':sum(x['reference_seconds']for x in warm),
         'warm_integer_seconds':sum(x['integer_seconds']for x in warm)}
    out['warm_speedup']=out['warm_reference_seconds']/out['warm_integer_seconds']
    write(args.output,out);print(json.dumps({k:v for k,v in out.items()if k!='bindings'},indent=2),flush=True)


def stage_unpack(args):
    """Restore authenticated data only; never execute code stored in a bundle."""
    import base64,zlib
    bundle=args.root/'lab/process/source-action-spin4-certificates.json'
    data=json.loads(bundle.read_text());restored=[]
    allowed={'inverse-stage1.json','inverse-stage3-basis.json','spin4-closure-integer-v2.json',
             'spin4-basis-validation.json','spin4-inverse-candidates.json','spin4-fast-certificate.json',
             'spin4-controls.json','spin4-benchmark.json'}
    for name,record in data['records'].items():
        assert name in allowed and record['encoding']=='zlib-base64-json'
        assert isinstance(record['uncompressed_bytes'],int)and 0<record['uncompressed_bytes']<100_000_000
        decoder=zlib.decompressobj();raw=decoder.decompress(base64.b64decode(record['data'],validate=True),record['uncompressed_bytes']+1)
        assert decoder.eof and not decoder.unconsumed_tail and not decoder.unused_data
        assert len(raw)==record['uncompressed_bytes']and hashlib.sha256(raw).hexdigest()==record['sha256']
        json.loads(raw);dest=args.cache/name
        if dest.exists():assert dest.read_bytes()==raw,('Different cache bytes',name)
        else:dest.write_bytes(raw)
        restored.append(name)
    write(args.output,{'restored':restored,'all_exact_bytes_verified':True});print('Restored',len(restored),'data records',flush=True)


def stage_status(args):
    """Cheap progress inspection; no geometry or inverse calculation."""
    out={}
    for name in ('spin4-closure-integer-v2.json','spin4-fast-certificate.json','spin4-basis-validation.json'):
        p=args.cache/name
        if not p.exists():out[name]={'present':False};continue
        d=json.loads(p.read_text());item={'present':True,'bytes':p.stat().st_size}
        for k in ('dimension','maps','completed','failure','all_passed','both_roots_solved'):
            if k in d:item[k]=d[k]
        if 'roots'in d:item['roots']=[{k:r[k]for k in ('root','invertible_on_block_over_rootball','neumann_bound')if k in r}for r in d['roots']]
        out[name]=item
    print(json.dumps(out,indent=2),flush=True)


#!/usr/bin/env python3
"""Exact bigint Neumann verifier for a completed sparse spin4 receiver closure.

NumPy dtype=object products multiply arbitrary-precision Python integers.
Floating inversion is used ONLY with --generate-candidates to suggest a
rational preconditioner. All accepted bounds are recomputed exactly.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import lcm
from types import SimpleNamespace
import argparse, hashlib, importlib.util, inspect, json, os, sys, time
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[name]='1'
sys.dont_write_bytecode=True
import numpy as np


def sn_digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def sn_jd(obj):return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def sn_write(path,obj):
    temp=path.with_suffix(path.suffix+'.new');temp.write_text(json.dumps(obj,indent=2));temp.replace(path)
def sn_zeros(shape):return np.zeros(shape,dtype=object)
def sn_identity(n):return np.eye(n,dtype=object)
def sn_rownorm(a):return max((sum(int(x)for x in row)for row in a),default=0)
def sn_abscomplex(real,imag):return np.abs(real)+np.abs(imag)
def sn_vecnorm(real,imag):return max((int(x)for x in sn_abscomplex(real,imag)),default=0)
def sn_cmul(ar,ai,br,bi):return ar@br-ai@bi,ar@bi+ai@br

def sn_validate_structure(cl,n=None,m=59):
    n=cl['dimension']if n is None else n
    assert isinstance(n,int) and n>0 and cl['dimension']==n
    assert cl['maps']==m and cl['completed']==n and len(cl['columns'])==n, 'Incomplete closure is not certifiable'
    assert not cl.get('failure'),'Closure has a nonzero native remainder'
    for col in cl['columns']:
        assert isinstance(col,list)and len(col)==m
        for sparse in col:
            prev=-1
            for item in sparse:
                assert isinstance(item,list)and len(item)==3
                i,a,b=item
                assert isinstance(i,int)and prev<i<n,'Duplicate, unordered or invalid sparse row'
                assert type(a)in(str,int)and type(b)in(str,int),'Inexact sparse coefficient type'
                a,b=Q(a),Q(b);assert a or b,'Sparse zero entry'
                prev=i
    return n


def sn_entries(cl):
    for j,col in enumerate(cl['columns']):
        for k,sparse in enumerate(col):
            for i,a,b in sparse:yield i,j,k,Q(a),Q(b)


def sn_assemble(cl,roots):
    """Global affine denominator; no59 dense matrices are materialized."""
    n=cl['dimension'];da=1
    for i,j,k,a,b in sn_entries(cl):da=lcm(da,a.denominator,b.denominator)
    rootdata=[]
    for root in roots:
        assert all(type(v)in(str,int)for v in root['coordinates']),'Inexact root coordinate type'
        x=list(map(Q,root['coordinates']));assert len(x)==cl['maps']
        dx=lcm(*(v.denominator for v in x));xi=[int(v*dx)for v in x]
        dm=da*dx;rootdata.append({'Mr':sn_identity(n)*dm,'Mi':sn_zeros((n,n)),'Dm':dm,'X':xi,'Dx':dx})
    S=sn_zeros((n,n))
    for i,j,k,a,b in sn_entries(cl):
        ar=int(a*da);ai=int(b*da);S[i,j]+=abs(ar)+abs(ai)
        for root in rootdata:
            root['Mr'][i,j]+=root['X'][k]*ar;root['Mi'][i,j]+=root['X'][k]*ai
    return da,S,rootdata


def sn_certificate_numbers(Mr,Mi,Dm,Rr,Ri,Dr,S,Da,radius,sources=()):
    """Exact native old Neumann bound and optional source coordinate errors."""
    n=Mr.shape[0]
    assert Mr.shape==Mi.shape==Rr.shape==Ri.shape==S.shape==(n,n)
    assert all(a.dtype==object for a in(Mr,Mi,Rr,Ri,S))
    assert all(isinstance(x,int)and x>0 for x in(Dm,Dr,Da))and radius>=0
    rr,ri=sn_cmul(Rr,Ri,Mr,Mi);de=Dr*Dm
    Er=sn_identity(n)*de-rr;Ei=-ri
    eta0=Q(sn_rownorm(sn_abscomplex(Er,Ei)),de)
    Rabs=sn_abscomplex(Rr,Ri);ar=np.array([sum(int(v)for v in row)for row in S],dtype=object)
    delta_vector=Rabs@ar
    eta_delta=radius*Q(max(map(int,delta_vector),default=0),Dr*Da)
    eta=eta0+eta_delta;rnorm=Q(sn_rownorm(Rabs),Dr)
    out={'center_preconditioned_residual_inf':str(eta0),'rootball_perturbation_inf':str(eta_delta),
         'neumann_bound':str(eta),'invertible_on_block_over_rootball':eta<1,
         'preconditioner_norm_inf':str(rnorm),'sources':[]}
    if eta<1:
        out['inverse_norm_inf_upper']=str(rnorm/(1-eta))
        for index,(Sr,Si,Ds)in enumerate(sources):
            assert len(Sr)==len(Si)==n and Ds>0
            Yr,Yi=sn_cmul(Rr,Ri,Sr,Si);dy=Dr*Ds
            # y=R*s. R(M*y-s)=-E*y, so the already-certified exact E
            # avoids another matrix product without changing the old bound.
            pre_r,pre_i=sn_cmul(Er,Ei,Yr,Yi)
            pre_norm=Q(sn_vecnorm(pre_r,pre_i),de*dy)
            ay=S@sn_abscomplex(Yr,Yi)
            perr=radius*Q(max(map(int,Rabs@ay),default=0),Dr*Da*dy)
            error=(pre_norm+perr)/(1-eta)
            res_r,res_i=sn_cmul(Mr,Mi,Yr,Yi)
            res_r-=Sr*(Dm*Dr);res_i-=Si*(Dm*Dr)
            out['sources'].append({'index':index,'coefficient_error_inf':str(error),
                 'center_residual_inf':str(Q(sn_vecnorm(res_r,res_i),Dm*dy)),
                 'preconditioned_center_residual_inf':str(pre_norm),
                 'rootball_preconditioned_source_error':str(perr),
                 'coordinates_denominator':str(dy),
                 'coordinates_real_numerators':[str(int(v))for v in Yr],
                 'coordinates_imag_numerators':[str(int(v))for v in Yi]})
    return out


def sn_validate_basis(module,args,bd,ctx=None):
    """Execute every native basis equation; no trusted result flags."""
    ctx=ctx or module.context(args,numeric=False)
    C=module.C;scale=module.scale;add=module.add
    basis=[{(e,c):C(Q(a),Q(b))for e,c,(a,b)in row}for row in bd['basis']]
    pivots=[tuple(p)for p in bd['basis_pivots']]
    assert len(pivots)==len(basis) and len(set(pivots))==len(pivots)
    tick=time.monotonic();count=0
    for j,(p,v)in enumerate(zip(pivots,basis)):
        assert v.get(p,C())==C(1),'Unnormalized echelon pivot'
        assert all(not v.get(prev,C())for prev in pivots[:j]),'Echelon independence failed'
        assert not ctx.q['K'](3,v),('Kdt_basis_failure',j)
        assert ctx.rot(0,1,v)==scale(4*module.I,v),('weight4_failure',j)
        assert not add(ctx.rot(0,2,v),scale(module.I,ctx.rot(1,2,v))),('highest_failure',j)
        assert ctx.q['cas'](v)==scale(20,v),('Casimir20_failure',j)
        count+=4
        if (j+1)%32==0:print('Native spin4 basis validation',j+1,'/',len(basis),'seconds',time.monotonic()-tick,flush=True)
    out={'scope':'Executed exact native equations on every receiver basis vector; no full-spin4 completeness claim.',
         'dimension':len(basis),'native_equation_checks':count,'echelon_pivots_independent':True,
         'Kdt_zero':True,'weight4':True,'raising_zero':True,'Casimir20':True,'complete':True,
         'seconds':time.monotonic()-tick,
         'bindings':{'basis_sha256':sn_digest(args.cache/'inverse-stage3-basis.json'),
                     'native_inputs':module.w.native_bindings(args.root),
                     'native_weak_probe_sha256':sn_digest(args.root/'tests/program-focus/source_action_weak_response_probe.py'),
                     'native_seed_context_sha256':hashlib.sha256(inspect.getsource(module.context).encode()).hexdigest(),
                     'validator_procedure_sha256':hashlib.sha256(inspect.getsource(sn_validate_basis).encode()).hexdigest()}}
    sn_write(args.cache/'spin4-basis-validation.json',out)
    return out


def sn_source_coordinates(module,args,bd,sd):
    """Reconstruct owned seeds, then exact echelon membership; no float fit."""
    C=module.C;add=module.add;scale=module.scale
    ctx=module.context(args,numeric=False)
    validation=sn_validate_basis(module,args,bd,ctx)
    native=ctx.seeds
    seeds=[{(e,c):C(Q(a),Q(b))for e,c,(a,b)in row}for row in sd['exact_seeds']]
    assert len(seeds)==2 and seeds==native,'Seed reconstruction mismatch'
    basis=[{(e,c):C(Q(a),Q(b))for e,c,(a,b)in row}for row in bd['basis']]
    pivots=[tuple(x)for x in bd['basis_pivots']];assert len(basis)==len(pivots)
    # The ordered echelon property is required by the coordinate algorithm.
    assert len(set(pivots))==len(pivots)
    for j,(p,v)in enumerate(zip(pivots,basis)):
        assert v.get(p,C())==C(1)
        assert all(not v.get(prev,C())for prev in pivots[:j])
    output=[]
    for s in seeds:
        v=dict(s);cs=[]
        for p,b in zip(pivots,basis):
            z=C(v.get(p,0));cs.append(z)
            if z:v=add(v,scale(-z,b))
        assert not v,'Source is outside certified envelope'
        ds=lcm(*(z.a.denominator for z in cs),*(z.b.denominator for z in cs))
        output.append((np.array([int(z.a*ds)for z in cs],dtype=object),np.array([int(z.b*ds)for z in cs],dtype=object),ds))
    return output,validation


def sn_exact_int(value):
    assert type(value)in(str,int),'Inexact integer payload type'
    if isinstance(value,str):
        assert value and value.lstrip('+-').isdigit(),'Noninteger payload'
    return int(value)


def sn_rational_preconditioner(root,n,binding,path,generate=False,precision=24):
    """Frozen common-denominator candidates; exact verifier decides quality."""
    if path.exists():
        bundle=json.loads(path.read_text())
        assert bundle.get('format')=='spin4-rational-inverses-v1'
        assert len({x['root']for x in bundle['roots']})==len(bundle['roots'])
    else:bundle={'format':'spin4-rational-inverses-v1','scope':'Rational inverse candidates only; verify exact residual and whole root box.','roots':[]}
    matches=[x for x in bundle['roots']if x['root']==binding['root']]
    assert len(matches)<=1
    if matches:
        data=matches[0];assert data['bindings']==binding,'Preconditioner binding mismatch'
    else:
        assert generate,'Missing preconditioner; explicit --generate-candidates is required'
        mf=np.array([[complex(float(Q(int(a),root['Dm'])),float(Q(int(b),root['Dm'])))
                      for a,b in zip(ar,ai)]for ar,ai in zip(root['Mr'],root['Mi'])],dtype=np.complex128)
        rf=np.linalg.inv(mf);assert np.isfinite(rf).all()
        dr=10**precision
        rr=[[int(round(Q(str(float(z.real)))*dr))for z in row]for row in rf]
        ri=[[int(round(Q(str(float(z.imag)))*dr))for z in row]for row in rf]
        data={'root':binding['root'],'bindings':binding,'dimension':n,'denominator':str(dr),
              'real_numerators':[[str(v)for v in row]for row in rr],
              'imag_numerators':[[str(v)for v in row]for row in ri]}
        bundle['roots'].append(data);bundle['roots'].sort(key=lambda x:x['root']);sn_write(path,bundle)
    assert data['dimension']==n
    assert len(data['real_numerators'])==len(data['imag_numerators'])==n
    assert all(len(row)==n for row in data['real_numerators']+data['imag_numerators'])
    dr=sn_exact_int(data['denominator']);assert dr>0
    rr=np.array([[sn_exact_int(x)for x in row]for row in data['real_numerators']],dtype=object)
    ri=np.array([[sn_exact_int(x)for x in row]for row in data['imag_numerators']],dtype=object)
    return rr,ri,dr


def sn_validate_inputs(args,module=None):
    cl=json.loads(args.closure.read_text());bd=json.loads((args.cache/'inverse-stage3-basis.json').read_text())
    sd=json.loads((args.cache/'inverse-stage1.json').read_text())
    D=json.loads((args.root/'lab/process/source-action-deep-coefficients.json').read_text())
    n=sn_validate_structure(cl,len(bd['basis']),59)
    assert len(D['basis'])==59 and len(D['certified_roots'])==2
    probe=args.root/'tests/program-focus/source_action_spin4_compatibility_probe.py'
    if module is None:
        spec=importlib.util.spec_from_file_location('bound_spin4_native_probe',probe)
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        module.load(args)
    expected=module.integer_binding(args)
    assert cl['engine_controls']['all_passed']
    assert cl['engine_controls']['bindings']['native_weak_probe_sha256']==sn_digest(args.root/'tests/program-focus/source_action_weak_response_probe.py'),'Direct weak-probe binding mismatch'
    assert cl['engine_controls']['bindings']['native_algebra_sha256']==sn_digest(args.root/'tests/program-focus/source_action_deep_algebra.py')
    assert expected==cl['bindings'],'Live closure implementation/native-input binding mismatch'
    assert expected['basis_sha256']==sn_digest(args.cache/'inverse-stage3-basis.json')
    assert expected['background_sha256']==sn_digest(args.root/'lab/process/source-action-deep-coefficients.json')
    for r in D['certified_roots']:
        assert type(r['certificate']['radius'])in(str,int),'Inexact root radius type'
        assert len(r['coordinates'])==59 and Q(r['certificate']['radius'])>0
    return cl,bd,sd,D,module


def sn_run(args,module=None):
    sn_prepare_args(args)
    tick=time.monotonic();cl,bd,sd,D,module=sn_validate_inputs(args,module)
    print('COMPLETE closure bindings validated',cl['dimension'],flush=True)
    sources,basis_validation=sn_source_coordinates(module,args,bd,sd)
    da,S,roots=sn_assemble(cl,D['certified_roots'])
    print('EXACT integer affine assembly done; denominator digits',len(str(da)),flush=True)
    base={'closure_sha256':sn_digest(args.closure),'basis_sha256':sn_digest(args.cache/'inverse-stage3-basis.json'),
          'seeds_sha256':sn_digest(args.cache/'inverse-stage1.json'),'background_sha256':sn_digest(args.root/'lab/process/source-action-deep-coefficients.json'),
          'native_weak_probe_sha256':sn_digest(args.root/'tests/program-focus/source_action_weak_response_probe.py'),
          'native_seed_context_sha256':hashlib.sha256(inspect.getsource(module.context).encode()).hexdigest()}
    out={'scope':'Exact Neumann invertibility of the completed reached-spin4 invariant receiver envelope at both existing root boxes; not full-R/full-N or physical admission.',
         'dimension':cl['dimension'],'family_maps':59,'coordinate_norm':'max_i(abs(real_i)+abs(imag_i))',
         'bindings':base|{'closure_bindings':cl['bindings'],'verifier_sha256':sn_digest(__file__)},
         'affine_integer_denominator':str(da),'roots':[],'controls':sn_controls(),'basis_validation':basis_validation}
    for ri,(root,owned)in enumerate(zip(roots,D['certified_roots'])):
        cb=base|{'root':ri,'root_record_sha256':sn_jd(owned)}
        cp=args.candidate_dir/'spin4-inverse-candidates.json'
        Rr,Ri,Dr=sn_rational_preconditioner(root,cl['dimension'],cb,cp,args.generate_candidates,args.precision)
        print('Exact root',ri,'bigint products begin',flush=True)
        rr=sn_certificate_numbers(root['Mr'],root['Mi'],root['Dm'],Rr,Ri,Dr,S,da,Q(owned['certificate']['radius']),sources)
        rr.update({'root':ri,'owned_root_record_sha256':sn_jd(owned),'radius':owned['certificate']['radius'],
                   'preconditioner_file':cp.name,'preconditioner_sha256':sn_digest(cp),'matrix_integer_denominator':str(root['Dm'])})
        out['roots'].append(rr)
        for recorded in out['roots']:recorded['preconditioner_sha256']=sn_digest(cp)
        out['both_roots_solved']=len(out['roots'])==2 and all(x['invertible_on_block_over_rootball']and len(x['sources'])==2 for x in out['roots'])
        out['seconds']=time.monotonic()-tick;sn_write(args.output,out)
        print('ROOT',ri,'eta',float(Q(rr['neumann_bound'])),'pass',rr['invertible_on_block_over_rootball'],'seconds',out['seconds'],flush=True)
    return out


def sn_controls():
    """Tiny integer-products vs literal Fraction/Gaussian-pair formulas."""
    def plus(a,b):return(a[0]+b[0],a[1]+b[1])
    def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
    def norm(z):return abs(z[0])+abs(z[1])
    def mm(a,b):return [[sum_pair(mul(x,y)for x,y in zip(row,col))for col in zip(*b)]for row in a]
    def sum_pair(xs):
        out=(Q(0),Q(0))
        for x in xs:out=plus(out,x)
        return out
    n=2;Mr=np.array([[17,2],[-3,22]],dtype=object);Mi=np.array([[1,-2],[4,0]],dtype=object);dm=20
    Rr=np.array([[100,3],[-7,90]],dtype=object);Ri=np.array([[0,1],[-2,0]],dtype=object);dr=100
    S=np.array([[3,2],[7,1]],dtype=object);da=9;radius=Q(1,1000)
    sr=np.array([2,-3],dtype=object);si=np.array([1,4],dtype=object);ds=7
    got=sn_certificate_numbers(Mr,Mi,dm,Rr,Ri,dr,S,da,radius,[(sr,si,ds)])
    M=[[(Q(int(a),dm),Q(int(b),dm))for a,b in zip(ar,ai)]for ar,ai in zip(Mr,Mi)]
    R=[[(Q(int(a),dr),Q(int(b),dr))for a,b in zip(ar,ai)]for ar,ai in zip(Rr,Ri)]
    RM=mm(R,M);E=[[(Q(i==j)-RM[i][j][0],-RM[i][j][1])for j in range(n)]for i in range(n)]
    eta0=max(sum(norm(z)for z in row)for row in E)
    ar=[sum(Q(int(x),da)for x in row)for row in S]
    delta=radius*max(sum(norm(R[i][j])*ar[j]for j in range(n))for i in range(n))
    assert Q(got['center_preconditioned_residual_inf'])==eta0
    assert Q(got['rootball_perturbation_inf'])==delta
    assert Q(got['neumann_bound'])==eta0+delta and got['invertible_on_block_over_rootball']
    sv=[(Q(int(a),ds),Q(int(b),ds))for a,b in zip(sr,si)]
    y=[sum_pair(mul(a,b)for a,b in zip(row,sv))for row in R]
    res=[plus(sum_pair(mul(a,b)for a,b in zip(row,y)),(-s[0],-s[1]))for row,s in zip(M,sv)]
    pre=[sum_pair(mul(a,b)for a,b in zip(row,res))for row in R]
    ay=[sum(Q(int(S[i,j]),da)*norm(y[j])for j in range(n))for i in range(n)]
    perr=radius*max(sum(norm(R[i][j])*ay[j]for j in range(n))for i in range(n))
    old=(max(map(norm,pre))+perr)/(1-eta0-delta)
    assert Q(got['sources'][0]['coefficient_error_inf'])==old
    assert Q(got['sources'][0]['center_residual_inf'])==max(map(norm,res))
    assert Q(got['sources'][0]['preconditioned_center_residual_inf'])==max(map(norm,pre))
    dy=int(got['sources'][0]['coordinates_denominator'])
    assert [(Q(int(a),dy),Q(int(b),dy))for a,b in zip(got['sources'][0]['coordinates_real_numerators'],got['sources'][0]['coordinates_imag_numerators'])]==y
    failed=sn_certificate_numbers(Mr,Mi,dm,sn_zeros((2,2)),sn_zeros((2,2)),1,S,da,radius)
    assert not failed['invertible_on_block_over_rootball']and Q(failed['neumann_bound'])==1
    rejects=0
    for bad in ({'dimension':2,'maps':59,'completed':1,'columns':[[]]},
                {'dimension':1,'maps':59,'completed':1,'columns':[[[[0,'1','0'],[0,'2','0']]]+[[]]*58]}):
        try:sn_validate_structure(bad)
        except AssertionError:rejects+=1
    assert rejects==2
    # Sparse affine assembly orientation: columns[j][k][i] -> A_k[i,j].
    small={'dimension':2,'maps':2,'completed':2,'columns':[[[[0,'1/3','2/7']],[[1,'-4/5','0']]],[[],[[0,'0','3/11']]]]}
    sn_validate_structure(small,2,2)
    da2,S2,rr=sn_assemble(small,[{'coordinates':['2/3','-3/4']}])
    assert Q(int(rr[0]['Mr'][0,0]),rr[0]['Dm'])==Q(11,9)
    assert Q(int(rr[0]['Mi'][0,1]),rr[0]['Dm'])==-Q(9,44)
    return {'all_passed':True,'checks':14,'incomplete_and_duplicate_records_rejected':True,'literal_fraction_comparison':True,'floating_inversion_used':False}


def sn_prepare_args(args):
    """Defaults also support dispatch from the owning probe's existing CLI."""
    if not hasattr(args,'root'):args.root=args.repo.resolve()
    args.cache=args.cache.resolve()
    if not getattr(args,'closure',None):args.closure=args.cache/'spin4-closure-integer-v2.json'
    if not getattr(args,'output',None):args.output=args.cache/'spin4-fast-certificate.json'
    if not getattr(args,'candidate_dir',None):args.candidate_dir=args.cache
    if not hasattr(args,'generate_candidates'):args.generate_candidates=False
    if not hasattr(args,'precision'):args.precision=24
    args.candidate_dir.mkdir(parents=True,exist_ok=True)
    assert 12<=args.precision<=80
    return args


def sn_basis_stage(args,module=None):
    sn_prepare_args(args)
    if module is None:
        probe=args.root/'tests/program-focus/source_action_spin4_compatibility_probe.py'
        spec=importlib.util.spec_from_file_location('bound_spin4_native_probe',probe)
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);module.load(args)
    bd=json.loads((args.cache/'inverse-stage3-basis.json').read_text())
    return sn_validate_basis(module,args,bd)





def stage_resume_integer_closure(args):
    """Fail before heavy work if a saved checkpoint's direct engine inputs drift."""
    if args.output.exists():
        cl=json.loads(args.output.read_text())
        assert cl['bindings']==integer_binding(args),'Checkpoint input/implementation drift'
        for key,path in [('native_weak_probe_sha256','tests/program-focus/source_action_weak_response_probe.py'),('native_algebra_sha256','tests/program-focus/source_action_deep_algebra.py')]:
            assert cl['engine_controls']['bindings'][key]==w.file_digest(args.root/path),'Checkpoint direct dependency drift'
        assert cl['completed']==len(cl['columns'])and 0<=cl['completed']<=cl['dimension']
        assert cl['maps']==59 and all(len(column)==59 for column in cl['columns'])
        assert not cl.get('failure'),'Checkpoint records a native closure failure'
    return stage_integer_closure(args)


if __name__=='__main__':main()
