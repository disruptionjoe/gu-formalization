#!/usr/bin/env python3
"""Matched first constraint-propagation source, with actual adapted-frame terms.

Root-serialized bounded stages. Rational root-center evaluations are diagnostic,
not exact-root membership or an obstruction. Kernel multipliers remain allowed.
"""
from pathlib import Path
from fractions import Fraction as Q
from types import SimpleNamespace
from functools import lru_cache
import argparse, hashlib, json, sys, time
sys.dont_write_bytecode = True


def digest(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix+'.new')
    temp.write_text(json.dumps(data, indent=2)+'\n'); temp.replace(path)


def setup(repo):
    sys.path.insert(0, str(repo/'tests/program-focus'))
    import source_action_weak_response_probe as w
    import source_action_spin4_compatibility_probe as fast
    import source_action_deep_geometry as g
    from source_action_paired_response_probe import C, I
    from source_action_deep_algebra import add, scale
    w.configure(repo); w.Engine = w._fast_exact_class()
    s = w.build_seed_context(SimpleNamespace(root=repo), False)
    integer = fast.IntegerScaledN(g)
    P = fast.IntegerKernelProjection(s.q, integer)
    return SimpleNamespace(repo=repo, w=w, fast=fast, g=g, C=C, I=I, add=add,
                           scale=scale, s=s, E=s.E, K=s.q['K'], P=P, integer=integer)


class RangeInverse:
    """Exact G=(K_dt|R)^-1 R on native 28-coordinate paired-XOR blocks."""
    def __init__(self, c): self.c=c; self.blocks={}
    def block(self, label):
        if label in self.blocks: return self.blocks[label]
        c=self.c; keys=[(1<<i, (1<<i)^label^z) for z in (0,8) for i in range(14)]
        columns=[c.K(3,{k:Q(1)}) for k in keys]
        assert all(set(v)<=set(keys) for v in columns)
        A=[[Q(v.get(k,0)) for v in columns] for k in keys]
        work=[row+[Q(i==j) for j in range(28)] for i,row in enumerate(A)]
        piv=[]; row=0
        for col in range(28):
            target=next((j for j in range(row,28) if work[j][col]),None)
            if target is None: continue
            work[row],work[target]=work[target],work[row]
            a=work[row][col]; work[row]=[x/a for x in work[row]]
            for j in range(28):
                if j!=row and work[j][col]:
                    a=work[j][col]; work[j]=[x-a*y for x,y in zip(work[j],work[row])]
            piv.append(col); row+=1
        # S chooses zero free coordinates in A x=R v. Projection R S R
        # gives the unique range solution; explicitly form only this tiny G.
        unitP=[c.P({key:Q(1)}) for key in keys]
        assert all(not c.C(z).b for v in unitP for z in v.values())
        P=[[c.C(v.get(key,0)).a for v in unitP] for key in keys]
        R=[[Q(i==j)-P[i][j] for j in range(28)] for i in range(28)]
        S=[[Q(0)]*28 for _ in range(28)]
        for i,p in enumerate(piv): S[p]=work[i][28:]
        def mm(a,b):
            out=[[Q(0)]*len(b[0]) for _ in a]
            sparse=[[(j,z) for j,z in enumerate(row) if z] for row in b]
            for i,row in enumerate(a):
                for k,x in enumerate(row):
                    if x:
                        for j,y in sparse[k]: out[i][j]+=x*y
            return out
        G=mm(mm(R,S),R)
        assert mm(A,G)==R and mm(G,A)==R
        assert all(not x for r in mm(P,G) for x in r)
        den,rows=c.fast.clear_matrix([{j:x for j,x in enumerate(r) if x} for r in G])
        self.blocks[label]=(keys,den,rows)
        return self.blocks[label]
    def __call__(self, v):
        c=self.c; den,integers=c.integer.clear_denominators(v); groups={}; out={}
        for key,z in integers.items(): groups.setdefault((key[0]^key[1])&~8,{})[key]=z
        for label,part in groups.items():
            keys,gd,rows=self.block(label)
            values=c.fast.integer_matvec(rows,[part.get(k,(0,0)) for k in keys])
            for k,(a,b) in zip(keys,values):
                if a or b: out[k]=c.C(Q(a,den*gd),Q(b,den*gd))
        return out


def geometry(c):
    """Gamma in the active adapted frame; beta_a=d_a(dx0)-d_a(log lapse)dx0."""
    g=c.g
    def isotropy(H): return [[g.h_action(H,j).get(i,Q()) for j in range(14)] for i in range(14)]
    gammas=[]; adapt=[]; betas=[]
    for a in range(14):
        H=g.zero(); S=g.A[a-4] if a>=4 else g.zero()
        if a>=4:
            for i in range(3): H[i][3]=H[3][i]=-S[3][i]
        J=isotropy(H)
        gammas.append([[g.L[a][i][j]+J[i][j] for j in range(14)] for i in range(14)])
        adapt.append(H)
        betas.append([S[0][b]+H[0][b]-S[3][3]*Q(b==0) for b in range(4)])
        assert all(S[3][i]+H[3][i]==0 for i in range(3))
    expected={5:{0:Q(1)},6:{0:Q(1)},7:{0:Q(4)},8:{1:Q(1)},9:{2:Q(1)},10:{3:Q(2)}}
    assert {a:{b:z for b,z in enumerate(row) if z} for a,row in enumerate(betas) if any(row)}==expected
    def rho(A,v):
        spin={(1<<a)|(1<<b):A[a][b]/(2*g.d[b]) for a in range(14) for b in range(a+1,14) if A[a][b]}
        out={}
        for(e,cl),x in v.items():
            a=e.bit_length()-1
            for b,z in enumerate(A[a]):
                if z: out[1<<b,cl]=out.get((1<<b,cl),0)-x*z
            for cc,z in c.E.cliff_product(spin,{cl:Q(1)},'comm').items():
                out[e,cc]=out.get((e,cc),0)+x*z
        return {k:z for k,z in out.items() if z}
    def lower(v, adapted=True):
        matrices=gammas if adapted else g.L
        return c.add(*(c.K(a,rho(A,v)) for a,A in enumerate(matrices) if any(any(r) for r in A)))
    return SimpleNamespace(gammas=gammas, adapt=adapt, betas=betas, rho=rho, lower=lower)


def n6_basis(c, cache):
    old=json.loads((c.repo/'lab/process/source-action-kappa1-constraints.json').read_text())
    binding=hashlib.sha256((c.repo/'tests/program-focus/source_action_reduced_evolution_probe.py').read_bytes()).hexdigest()
    if cache.exists():
        data=json.loads(cache.read_text()); assert data['native_builder_sha256']==binding
        assert data['coordinate_bindings']==digest([old['exact_probe']['spin6']['highest6_in_weight6'],old['exact_probe']['spin6']['time_kernel_in_highest6']])
    else:
        from source_action_reduced_evolution_probe import build_context
        ctx=build_context(c.repo)
        assert ctx['highest6_in_weight6']==old['exact_probe']['spin6']['highest6_in_weight6']
        assert ctx['time_kernel_in_highest6']==old['exact_probe']['spin6']['time_kernel_in_highest6']
        data={'native_builder_sha256':binding,'coordinate_bindings':digest([ctx['highest6_in_weight6'],ctx['time_kernel_in_highest6']]),
              'basis':[[[e,cl,z.ser()] for (e,cl),z in sorted(v.items())] for v in ctx['N6']]}
        write(cache,data)
    vectors=[{(e,cl):c.C(*z) for e,cl,z in row} for row in data['basis']]
    assert len(vectors)==128
    return vectors,old


def responses(c, basis, old, ri, index):
    evo=json.loads((c.repo/'lab/process/source-action-reduced-evolution.json').read_text())
    row=next(x for x in evo['exact_probe']['source_receivers'] if x['basis_index']==index)
    assert not row['b7_lowered']
    b={i:c.C(*z) for i,z in row['b6']}; coeff={}; errors={}
    official=old['exact_probe']['spin6']['constraint_inverse']['root_certificates'][ri]
    for block,cert in zip(old['spin6_inverse_candidates'][ri]['blocks'],official['blocks']):
        assert digest(block['rational_inverse'])==cert['rational_inverse_sha256']
        assert block['neumann_bound']==cert['neumann_bound']
        ids=block['indices']; eta=Q(block['neumann_bound']); assert eta<1
        if not any(j in b for j in ids):continue
        values=[sum((c.C(*z)*b.get(j,c.C()) for z,j in zip(row,ids)),c.C()) for row in block['rational_inverse']]
        bound=eta/(1-eta)*max(abs(z.a)+abs(z.b) for z in values)
        coeff.update(zip(ids,values)); errors.update((j,bound) for j in ids)
    return c.add(*(c.scale(z,basis[j]) for j,z in coeff.items() if z)),coeff,errors


def reduce_basis(c, v, data):
    for pivot,row in zip(data['basis_pivots'],data['basis']):
        a=c.C(v.get(tuple(pivot),0))
        if a: v=c.add(v,c.scale(-a,{(e,cl):c.C(*z) for e,cl,z in row}))
    return v


def boost_bridge(c, geo, Vs, e5):
    """Exact actual preservation-source quotient, no root arithmetic or inverse."""
    path=c.repo/'lab/process/source-action-firstjet-source-census-certificates.json'
    census=json.loads(path.read_text())
    evidence=json.loads((c.repo/'lab/process/source-action-firstjet-source-census.json').read_text())
    assert hashlib.sha256(path.read_bytes()).hexdigest()==evidence['current_sha256'][str(path.relative_to(c.repo))]
    for name,expected in census['bindings']['native_inputs'].items():
        assert hashlib.sha256((c.repo/name).read_bytes()).hexdigest()==expected
    background_path=c.repo/'lab/process/source-action-deep-coefficients.json'
    assert hashlib.sha256(background_path.read_bytes()).hexdigest()==census['bindings']['background_sha256']
    bp=e5/'inverse-stage3-basis.json'
    assert hashlib.sha256(bp.read_bytes()).hexdigest()==census['bindings']['receivers']['5']['basis_sha256']
    bd=json.loads(bp.read_text())
    gamma10=geo.gammas[10]
    assert not any(any(row) for row in c.g.L[10])
    S=lambda v:c.scale(-1,geo.rho(gamma10,v))
    background=json.loads(background_path.read_text())
    invariant=0
    for row in background['basis']:
        T={(e,cl):Q(z) for e,cl,z in row}
        assert not S(T), 'Owned background fails signed boost invariance'
        invariant+=1
    rows=[]; vectors=[]
    for index,case,V in zip((5,12),(8,17),Vs):
        assert c.add(S(c.K(3,V)),c.scale(-1,c.K(3,S(V))))==c.K(0,V)
        assert c.add(S(c.K(0,V)),c.scale(-1,c.K(0,S(V))))==c.K(3,V)
        SV=S(V); RSV=c.add(SV,c.scale(-1,c.P(SV)))
        full=c.P(c.K(0,RSV)); high=c.s.q['spin5'](full)
        assert c.s.q['cas'](high)==c.scale(30,high)
        assert not c.add(c.s.rot(0,2,high),c.scale(c.I,c.s.rot(1,2,high)))
        old=census['sources'][case]
        assert old['index']==case and old['Q7_basis_index']==index
        assert old['connection_family']=='normal' and old['intermediate']=='W6'
        assert old['principal_axis']==0 and old['target_spin']==5
        oldvector={(e,cl):c.C(*z) for e,cl,z in old['source']}
        assert high==c.scale(-1,oldvector), 'Native boost/census sign mismatch'
        remainder=reduce_basis(c,high,bd)
        assert remainder==high and len(high)==old['source_terms']
        vectors.append(high)
        rows.append({'basis_index':index,'old_census_case':case,'old_case_scale':'-1',
                     'terms':len(high),'full_source_terms':len(full),'old_E5_remainder_terms':len(remainder),
                     'source_sha256':digest([[e,cl,c.C(z).ser()] for (e,cl),z in sorted(high.items())]),
                     'source':[[e,cl,c.C(z).ser()] for (e,cl),z in sorted(high.items())],
                     'native_boost_commutators':True,'highest5':True})
    echelon=[]
    for vector in vectors:
        rem=vector
        for pivot,b in echelon:
            a=rem.get(pivot,0)
            if a:rem=c.add(rem,c.scale(-a,b))
        assert rem
        pivot=min(rem);echelon.append((pivot,c.scale(1/rem[pivot],rem)))
    return {'status':'EXACT_NATIVE_SOURCE_CLASS_BRIDGE',
            'identity':'C2(y)=P K0 R S V - M(P S y) + (P S P)(M y-P K0 V), S=-Gamma10.',
            'exact_response_class':'[C2(V)] = -[published cases8/17] in N5/im(M|N5).',
            'all59_background_boost_invariants':invariant,'source_rank':len(echelon),'sources':rows,
            'published_census_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'old_E5_basis_sha256':hashlib.sha256(bp.read_bytes()).hexdigest(),
            'scope':'Actual highest horizontal-Hessian first-prolongation source classes at both held roots. Old E5 noncoverage is not a cokernel obstruction; normal and zero-order kernel multiplier images remain.'}


def run(args):
    start=time.monotonic(); c=setup(args.repo); geo=geometry(c); G=RangeInverse(c)
    ser=lambda v:[[e,cl,c.C(z).ser()] for (e,cl),z in sorted(v.items())]
    out={'scope':'Matched first horizontal-Hessian constraint propagation on the two owned Q7 modules; kernel multipliers retained. Root-center results are diagnostics, never obstruction or exact-root solvability.',
         'stage':args.mode,'roots':[],'controls':{},'completed':0}
    bindings=['source_action_deep_geometry.py','source_action_deep_algebra.py','source_action_metric_symbol_probe.py','source_action_paired_response_probe.py','source_action_weak_response_probe.py','source_action_spin4_compatibility_probe.py','source_action_reduced_evolution_probe.py']
    out['bindings']={p:hashlib.sha256((args.repo/'tests/program-focus'/p).read_bytes()).hexdigest() for p in bindings}
    out['bindings']['self']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Vs=[c.K(3,c.s.bs[j]) for j in (5,12)]
    if args.mode in ('bridge','center-check'):
        out['bridge']=boost_bridge(c,geo,Vs,args.e5)
        if args.mode=='center-check':
            assert args.center_diagnostic is not None
            diagnostic=json.loads(args.center_diagnostic.read_text())
            for name,sha in diagnostic['bindings'].items():
                if name!='self': assert out['bindings'][name]==sha
            basis,old=n6_basis(c,args.cache/'native-n6.json')
            background=json.loads((args.repo/'lab/process/source-action-deep-coefficients.json').read_text())
            Ts=[{(e,cl):Q(z) for e,cl,z in row} for row in background['basis']]
            S=lambda v:c.scale(-1,geo.rho(geo.gammas[10],v))
            checks=[]
            for rr in diagnostic['roots']:
                ri=rr['root'];T=c.add(*(c.scale(Q(x),v) for x,v in zip(background['certified_roots'][ri]['coordinates'],Ts)))
                def J(v):return c.add(v,c.scale(2,c.integer.N(T,v)))
                for row in rr['sources']:
                    index=row['basis_index'];V=Vs[(5,12).index(index)]
                    y,coeff,errs=responses(c,basis,old,ri,index)
                    residual=c.add(c.P(J(y)),c.scale(-1,c.P(c.K(0,V))))
                    SV=S(V);boost=c.P(c.K(0,c.add(SV,c.scale(-1,c.P(SV)))))
                    jy=c.P(S(y));jr=c.P(S(residual))
                    rhs=c.s.q['spin5'](c.add(boost,c.scale(-1,c.P(J(jy))),jr))
                    direct={(e,cl):c.C(*z) for e,cl,z in row['highest5']}
                    assert rhs==direct, 'Corrected matched/boost identity failed'
                    correction=c.s.q['spin5'](jr)
                    checks.append({'root':ri,'basis_index':index,'exact_corrected_identity':True,
                                   'residual_correction_terms':len(correction),
                                   'direct_source_terms':len(direct)})
            out['center_checks']=checks
            out['diagnostic_input_sha256']=hashlib.sha256(args.center_diagnostic.read_bytes()).hexdigest()
        out['seconds']=time.monotonic()-start;out['completed']=2;write(args.output,out);return out
    for V in Vs:
        assert geo.lower(V,False)==c.E.K(V), 'Native covariant lower mismatch'
        assert c.K(3,G(V))==V
    out['controls']['native_covariant_lower_matches_Engine_K']=True
    out['controls']['range_inverse_two_Q_controls']=True
    out['controls']['adapted_lapse_frame_betas']=[[str(z) for z in row] for row in geo.betas]
    if args.mode=='controls':
        out['seconds']=time.monotonic()-start; write(args.output,out); return out
    basis,old=n6_basis(c,args.cache/'native-n6.json')
    bd=json.loads((args.e5/'inverse-stage3-basis.json').read_text())
    background=json.loads((args.repo/'lab/process/source-action-deep-coefficients.json').read_text())
    Ts=[{(e,cl):Q(z) for e,cl,z in row} for row in background['basis']]
    for ri in args.roots:
        T=c.add(*(c.scale(Q(x),v) for x,v in zip(background['certified_roots'][ri]['coordinates'],Ts)))
        def J(v):return c.add(v,c.scale(2,c.integer.N(T,v)))
        def C0(v):return c.add(J(v),geo.lower(v))
        rr={'root':ri,'sources':[]}
        out['roots'].append(rr)
        for index,V in zip((5,12),Vs):
            if index not in args.sources:continue
            tick=time.monotonic(); y,coeff,errs=responses(c,basis,old,ri,index)
            source=c.P(c.K(0,V))
            # This is a rational inverse candidate; retain actual finite residual.
            residual=c.add(c.P(J(y)),c.scale(-1,source))
            assert not c.K(3,y)
            assert not c.P(geo.lower(y)), 'Closed-dt lower cancellation mismatch'
            K0y=c.K(0,y); GK0y=G(K0y)
            assert not c.P(K0y)
            assert not c.P(c.K(0,GK0y)), 'Cubic symbol cancellation failed'
            principal=c.P(c.K(0,G(c.K(0,V))))
            correction1=c.P(c.K(0,G(C0(y))))
            correction2=c.P(C0(GK0y))
            frame=[]
            for a,beta in enumerate(geo.betas):
                if any(beta):
                    kb=c.add(*(c.scale(z,c.K(b,y)) for b,z in enumerate(beta) if z))
                    frame.append(c.P(c.K(a,G(kb))))
            pure_geometry=c.add(c.P(c.K(0,G(geo.lower(y)))),c.P(geo.lower(GK0y)),*frame)
            out['controls'].setdefault('geometric_first_order_cancellation',[]).append(
                {'root':ri,'basis_index':index,'remainder_terms':len(pure_geometry),'remainder':ser(pure_geometry)})
            matched=c.add(principal,c.scale(-1,c.add(correction1,correction2,*frame)))
            assert not c.K(3,matched)
            high5=c.s.q['spin5'](matched)
            assert c.s.q['cas'](high5)==c.scale(30,high5)
            assert not c.add(c.s.rot(0,2,high5),c.scale(c.I,c.s.rot(1,2,high5)))
            write(args.cache/('matched-before-reduction-r%d-s%d.json'%(ri,index)),
                  {'highest5':ser(high5),'geometric_remainder':ser(pure_geometry),'G_blocks':len(G.blocks),'seconds':time.monotonic()-tick})
            remainder=reduce_basis(c,high5,bd)
            row={'basis_index':index,'status':'RATIONAL_CENTER_DIAGNOSTIC_ONLY',
                 'response_terms':len(y),'response_coordinate_indices':sorted(coeff),'response_errors':{str(i):str(e) for i,e in errs.items()},
                 'native_M_candidate_residual_terms':len(residual),'native_M_candidate_residual_max':str(max((abs(z.a)+abs(z.b) for z in residual.values()),default=Q())),
                 'matched_terms':len(matched),'matched_highest5_terms':len(high5),'old_E5_remainder_terms':len(remainder),
                 'highest5':ser(high5),'remainder':ser(remainder),'seconds':time.monotonic()-tick}
            rr['sources'].append(row);out['completed']+=1;out['G_blocks']=len(G.blocks);out['seconds']=time.monotonic()-start
            write(args.output,out);print('matched',ri,index,'spin5',len(high5),'remainder',len(remainder),'seconds',row['seconds'],flush=True)
    return out


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2])
    ap.add_argument('--cache',type=Path,required=True)
    ap.add_argument('--e5',type=Path,required=True)
    ap.add_argument('--mode',choices=('controls','bridge','center-check','matched'),default='controls')
    ap.add_argument('--center-diagnostic',type=Path)
    ap.add_argument('--roots',type=int,nargs='+',choices=(0,1),default=[0,1])
    ap.add_argument('--sources',type=int,nargs='+',choices=(5,12),default=[5,12])
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();args.repo=args.repo.resolve();run(args)


if __name__=='__main__': main()
