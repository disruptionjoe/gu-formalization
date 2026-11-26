"""Exact native receiver-strategy probes with one shared context.

Replays owned high-spin constraint certificates, tests normal energy and seed
blindness, audits the receiver algebra, and checks finite transfer/duality
controls. No closed physical propagation or source-theory verdict.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse,sys,json,hashlib

def normal_screen(root,ctx):
    root=Path(root)
    sys.path.insert(0,str(root/'tests/program-focus'))
    import source_action_deep_geometry as geo
    from source_action_reduced_evolution_probe import build_context
    C,E,h=ctx['C'],ctx['E'],ctx['h']
    old=json.loads((root/'lab/process/source-action-kappa1-constraints.json').read_text())
    previous=json.loads((root/'lab/process/source-action-reduced-evolution.json').read_text())
    p7=previous['spin7_inverse_candidates']
    def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    def znorm(x):x=C(x);return abs(x.a)+abs(x.b)
    def serial(v):return [[e,c,C(z).ser()] for (e,c),z in sorted(v.items())]
    assert digest([[C(x).ser() for x in row]for row in ctx['G7']])==old['exact_probe']['spin7']['kernel_gram_sha256']
    for ri,p in enumerate(p7):
        cert=old['exact_probe']['spin7']['root_certificates'][ri]
        assert p['root']==ri
        assert digest(p['inverse'])==cert['inverse_sha256']
        assert p['neumann_bound']==cert['neumann_bound'] and Q(p['neumann_bound'])<1
    # theta4 is full trace; theta7 is the SO3-scalar trace-free diagonal.
    axes=[4,7]
    for axis in axes:
        for i,j in [(0,1),(0,2),(1,2)]:
            H=geo.zero();H[i][j]=1;H[j][i]=-1
            assert all(not geo.h_action(H,b).get(axis,0) for b in range(14))
    tau=[Q(0)]*14;tau[3]=1
    piv=[min(b)for b in h.bs]
    def complete7(v):
        co=[C(v.get(k,0))for k in piv]
        assert v==h.add(*(h.scale(c,b)for c,b in zip(co,h.bs)if c))
        return co
    all_sources=[]
    for axis in axes:
        xi=[Q(0)]*14;xi[axis]=1
        for j,bb in enumerate(h.bs):
            v=h.symbols(E,tau,bb)[0]
            force=h.symbols(E,xi,v)[0]
            complete7(v);complete7(force)
            assert h.rot(0,1,force)==h.scale(7*h.I,force)
            assert not h.add(h.rot(0,2,force),h.scale(h.I,h.rot(1,2,force)))
            b=[C(E.pair(h.conj(n),force))for n in h.N]
            all_sources.append({'axis':axis,'index':j,'v':v,'force':force,'b':b})
    roots=[]
    for ri,p in enumerate(p7):
        R=[[C(*z)for z in row]for row in p['inverse']]
        eta=Q(p['neumann_bound']);rows=[]
        for src in all_sources:
            b=src['b'];c=[-sum((a*z for a,z in zip(row,b)),C())for row in R]
            err=eta/(1-eta)*max(map(znorm,c))
            val=sum((z.conj()*w for z,w in zip(b,c)),C())
            error=sum(map(znorm,b))*err+abs(val.b)
            n=h.add(*(h.scale(x,y)for x,y in zip(c,h.N)if x))
            assert E.pair(n,n)==0
            assert E.pair(src['force'],n)==0
            sign='zero_source' if not any(b) else ('negative' if val.a+error<0 else 'positive' if val.a-error>0 else 'undetermined_interval')
            rows.append({'axis':src['axis'],'range_basis_index':src['index'],'nonzero_range':bool(src['v']),'source_nonzero_entries':sum(bool(z)for z in b),'source_coordinates':[[i,z.ser()]for i,z in enumerate(b)if z],'range_sha256':digest(serial(src['v'])),'force_sha256':digest(serial(src['force'])),'center':str(val.a),'error_bound':str(error),'lower':str(val.a-error),'upper':str(val.a+error),'sign':sign,'realification_bilinear_pair_zero':True,'realification_force_response_pair_zero':True})
        roots.append({'root':ri,'normal_covectors':axes,'rows':rows,'sign_counts':{axis:{s:sum(x['axis']==axis and x['sign']==s for x in rows)for s in ['zero_source','negative','positive','undetermined_interval']}for axis in axes}})
    # Seed-current blindness: normal-only gamma-traceless connection forms.
    from source_action_physical_probe import components,mul,gamma,contraction
    from source_action_deep_algebra import add,scale
    from source_action_slice_completion_probe import inverse,readout,inject
    def vertex(w,field):
        a=components(w);z,nu=field
        rr=[add(*(scale(1/geo.d[b],mul(gamma(b),add(mul(a[b],z[j]),scale(-1,mul(a[j],z[b]))))) for b in range(14)),mul(a[j],nu)) for j in range(14)]
        ss=add(*(scale(1/geo.d[j],mul(a[j],z[j])) for j in range(14)),*(scale(-Q(1,2)/geo.d[j],mul(gamma(j),mul(a[j],nu))) for j in range(14)))
        return rr,ss
    def seed_receiver(w):return [readout(inverse(tau,vertex(w,inject(j)))) for j in range(5)]
    for u in h.bs+h.N:
        assert not any(e in (1,2,4,8) for e,c in u)
        assert not contraction(components(u),range(14))
        assert not any(any(col)for col in seed_receiver(u))
    # A generic normal form need not be blind: gamma-tracelessness is essential.
    assert any(any(col)for col in seed_receiver({(1<<4,0):Q(1)}))
    return {'basis_revision':'da33e35d6921f30f2d7e0d6c1eba8955f34eee08','kind':'exact_normal_scalar_principal_energy_screen','controls':{'complete_highest_spin7_closed':True,'native_normal_covectors_SO3_scalar':True,'highest_spin7_gram_hash':True,'inverse_root_bounds_hash':True,'no_lower_inverse_required_for_these_columns':True},'axes':{'4':'normal full trace, inverse metric -1/16','7':'normal spatial-rotation scalar traceless diagonal, inverse metric +1/48'},'roots':roots,'seed_current_controls':{'highest_spin7_basis_count':len(h.bs),'highest_spin7_kernel_count':len(h.N),'all_normal_only':True,'all_gamma_trace_zero':True,'all_seed_receivers_zero':True,'generic_normal_nontraceless_control_nonzero':True},'energy_convention':'b*c is physical imaginary-sector derivative energy, common positive1/2 omitted; each real component gets half by nonzero rotation weight.','scope':'Pointwise principal-energy form only. Compact constrained data still require full M regularity. Selected CK normal-profile accessibility, closed-domain propagation, physical quotient, source/candidate bridge remain open. Base K-K bound does not constrain these normal covectors.'}

def finite_controls():
    def dot(a,b): return sum(x*y for x,y in zip(a,b))
    def mv(A,x): return [dot(row,x) for row in A]
    M=[[Q(2),Q(0)],[Q(0),Q(0)]]
    rhs=[Q(4),Q(0)]; source=[Q(6),Q(0)]
    ys=[[Q(2),Q(t)] for t in [-7,0,5]]
    assert all(mv(M,y)==rhs for y in ys)
    scalar=[dot(source,y) for y in ys]
    assert scalar==[Q(12)]*3
    badsource=[Q(6),Q(1)]
    ambiguous=[dot(badsource,y) for y in ys]
    assert len(set(ambiguous))==3
    # Adjoint solve is essential for a nonsymmetric coordinate matrix.
    A=[[Q(1),Q(1)],[Q(0),Q(1)]];At=list(map(list,zip(*A)))
    u=[Q(1),Q(0)];f=[Q(0),Q(1)];x=[Q(-1),Q(1)]
    y=[Q(1),Q(-1)];wrong=[Q(1),Q(0)]
    assert mv(A,x)==f and mv(At,y)==u and mv(A,wrong)==u
    assert dot(u,x)==dot(y,f)==Q(-1) and dot(wrong,f)==0
    # A PSD mixed-state relaxation does not preserve a rank-one quadratic target.
    rho=[[Q(1,2),Q(0)],[Q(0),Q(1,2)]]
    determinant=rho[0][0]*rho[1][1]-rho[0][1]*rho[1][0]
    assert determinant==Q(1,4)
    rankone=[]
    for a,b in [(Q(1),Q(0)),(Q(0),Q(1)),(Q(3,5),Q(4,5))]:
        R=[[a*a,a*b],[a*b,b*b]]
        det=R[0][0]*R[1][1]-R[0][1]*R[1][0]
        assert det==0;rankone.append(str(det))
    return {'singular_scalar_witness':{'M_rank':1,'dimension':2,'values':list(map(str,scalar)),'kernel_compatible':True},
            'incompatible_source_ambiguity_values':list(map(str,ambiguous)),
            'transpose_control':{'correct':'-1','wrong_primal_solve':'0'},
            'PSD_rank_relaxation_control':{'minus_det_rankone':rankone,'minus_det_mixed':'-1/4'},
            'scope':'Finite exact scaffolding controls only; no native GU constrained forcing or physical instability claim.'}

def run_receiver_products(ROOT,ctx):
    """Native complete6/7 receiver span/product audit, with shared ctx reuse."""
    sys.path.insert(0,str(Path(ROOT)/'tests/program-focus'))
    import source_action_deep_geometry as geo
    from source_action_deep_algebra import add,scale
    from source_action_physical_probe import mul,gamma,components
    from source_action_slice_completion_probe import covector,inject,inverse,readout
    C,E,h,N6=ctx['C'],ctx['E'],ctx['h'],ctx['N6']
    tau=covector(3)
    N7=[h.add(h.rot(0,2,n),h.scale(-h.I,h.rot(1,2,n)))for n in h.N]
    def vertex(w,field):
        a=components(w);z,nu=field;se=-Q(1,2)
        r=[add(*(scale(1/geo.d[b],mul(gamma(b),add(mul(a[b],z[j]),scale(-1,mul(a[j],z[b])))))for b in range(14)),mul(a[j],nu))for j in range(14)]
        s=add(*(scale(1/geo.d[j],mul(a[j],z[j]))for j in range(14)),*(scale(se/geo.d[j],mul(gamma(j),mul(a[j],nu)))for j in range(14)))
        return r,s
    def receiver(w):
        cols=[readout(inverse(tau,vertex(w,inject(j))))for j in range(5)]
        return {(i,j,c):C(x)for j,col in enumerate(cols)for i,v in enumerate(col)for c,x in v.items()if x}
    realBs=[];labels=[]
    for j,n in enumerate(N6+N7):
        B=receiver(n)
        for part in ['a','b']:
            R={k:Q(getattr(z,part))for k,z in B.items()if getattr(z,part)}
            if R:realBs.append(R);labels.append({'native_generator_index':j,'component':part})
    assert len(realBs)==32
    def clean(d):return {k:v for k,v in d.items()if v}
    def plus(A,B):
        R=A.copy()
        for k,v in B.items():R[k]=R.get(k,Q(0))+v
        return clean(R)
    def product(A,B):
        rows={}
        for (j,k,d),v in B.items():rows.setdefault(j,[]).append((k,d,v))
        out={}
        for (i,j,c),x in A.items():
            for k,d,y in rows.get(j,[]):
                blade,s=geo.cliff_mul(c,d);key=(i,k,blade)
                out[key]=out.get(key,Q(0))+x*y*s
        return clean(out)
    # Sparse elimination gives exact linear-span dimension, not physical matrix rank.
    echelon=[];independent=[];coordinates=[]
    for i,B in enumerate(realBs):
        v=B.copy();coeff={i:Q(1)}
        for pivot,row,comb in echelon:
            a=v.get(pivot,Q(0))
            if not a:continue
            v=plus(v,{k:-a*x for k,x in row.items()});coeff=plus(coeff,{k:-a*x for k,x in comb.items()})
        if v:
            pivot=min(v);a=v[pivot];v={k:x/a for k,x in v.items()};coeff={k:x/a for k,x in coeff.items()}
            echelon.append((pivot,v,coeff));independent.append(i)
        else: coordinates.append({str(k):str(v)for k,v in coeff.items()})
    for relation in coordinates:
        value={}
        for k,a in relation.items():value=plus(value,{b:Q(a)*v for b,v in realBs[int(k)].items()})
        assert not value
    tracebad=[];anti_bad=[];square_bad=[];allzero_product=0;tested=0
    for i,A in enumerate(realBs):
        AA=product(A,A)
        if AA:square_bad.append({'i':i,'terms':len(AA),'first':[(str(k),str(v))for k,v in list(sorted(AA.items()))[:3]]})
        for j in range(i,len(realBs)):
            tested+=1;AB=product(A,realBs[j]);BA=product(realBs[j],A);anti=plus(AB,BA)
            trace=sum(v for (a,b,c),v in AB.items()if a==b and c==0)
            if trace:tracebad.append((i,j,str(trace)))
            if not AB and not BA:allzero_product+=1
            if anti:anti_bad.append({'i':i,'j':j,'terms':len(anti),'first':[(str(k),str(v))for k,v in list(sorted(anti.items()))[:3]]})
    assert not tracebad
    return {'receiver_generators':len(realBs),'labels':labels,'exact_real_linear_span_dimension':len(echelon),'independent_generator_indices':independent,'dependency_relations':coordinates,'polarized_pairs':tested,'both_ordered_products_zero_pairs':allzero_product,'polarized_anticommutator_nonzero_pairs':len(anti_bad),'first_anticommutator_counterexamples':anti_bad[:8],'individual_square_nonzero_count':len(square_bad),'first_square_counterexamples':square_bad[:4],'trace_product_nonzero_pairs':tracebad,'all_real_combinations_square_zero':not anti_bad,'scope':'Same canonical I/q/At/four vertices; complete spin6 plus lowered spin7 derivative auxiliary receiver image. Linear span dimension is not particle count, physical state dimension, or forced-response rank.'}

def support_and_covariance_controls():
    a,b=Q(5,3),Q(4,3)
    assert a*a-b*b==1
    boosts=[]
    for c in [Q(1),Q(2)]:
        E,k=1+c,Q(1)
        Ep,kp=a*E+b*k,b*E+a*k
        assert Ep*Ep-kp*kp==E*E-k*k
        assert a*Ep-b*kp==E and -b*Ep+a*kp==k
        defect=k-2*c*k*(1+c*k*k)
        assert defect==-k*(2*c-1+2*c*c*k*k)
        assert defect!=0 and Ep!=1+c*kp*kp
        boosts.append({'c':str(c),'defect_at_k1':str(defect),'boosted_energy':str(Ep),'original_graph_energy_at_boosted_k':str(1+c*kp*kp)})
    E,k=Q(5),Q(3);Ep,kp=a*E+b*k,b*E+a*k
    assert Ep*Ep-kp*kp==16 and Ep>0
    K=[Q(-1),Q(0),Q(1)]
    graphs={}
    for name,w in [('constant',lambda k:Q(2)),('affine',lambda k:4+k),('quadratic',lambda k:1+k*k)]:
        D={(w(k)-w(l),k-l)for k in K for l in K}
        assert D=={(-t,-x)for t,x in D}
        assert all(t==0 for t,x in D if x==0) # exact pairs, not closure for measurable w
        if name=='constant':assert all(t==0 for t,x in D)
        if name=='affine':assert all(t==x for t,x in D)
        graphs[name]=sorted([[str(t),str(x)]for t,x in D])
    jumps=[]
    for n in [1,2,4,16,1024]:
        k,l=Q(1,n),Q(-1,n)
        w=lambda x:Q(2)if x>0 else Q(1)
        O,q=w(k)-w(l),k-l
        assert O==1 and q==Q(2,n)
        jumps.append({'n':n,'temporal_transfer':str(O),'spatial_transfer':str(q)})
    # q tends to0 with fixed O=1: closed essential support can contain(1,0).
    # Every pair has positive-measure neighbourhoods of the two graph pieces.
    # PT at fixed k: use exact rational complex pairs, not floating-point complex.
    conj=lambda z:(z[0],-z[1]);scale=lambda w,z:(w*z[0],w*z[1])
    z=(Q(2),Q(-3))
    for w in [Q(-3,7),Q(0),Q(5,9)]:assert conj(scale(w,z))==scale(w,conj(z))
    # A nonzero raw normal derivative can vanish in the real physical current.
    raw_derivative=(Q(0),Q(1))
    paired=tuple((x+y)/2 for x,y in zip(raw_derivative,conj(raw_derivative)))
    assert raw_derivative!=(0,0) and paired==(0,0)
    # Same massless branch can give nonzero NULL transfer, so strict spacelike is false.
    O,q=Q(2)-Q(1),Q(2)-Q(1)
    assert O*O-q*q==0 and q!=0
    # Mass-shell tangency permits negative m^2; positivity is a separate premise.
    assert Q(1)**2-Q(2)**2<0
    return {'boost_witnesses':boosts,'massive_shell_boost_control':True,'finite_difference_graphs':graphs,
        'measurable_jump_negative_control':jumps,'zero_spatial_transfer_rule':'True for exact identical pair; closed support needs uniform continuity. Measurable class permits vertical limit transfers.',
        'k_fixing_PT_multiplication_control':True,'raw_nonzero_jet_can_have_zero_Hermitian_current':True,'massless_nonzero_null_difference_control':True,
        'scope':'Exact finite controls plus stated analytic arguments; not proof of native physical Lorentz covariance, normal-profile access or coupled propagation.'}

def run(root):
    root=Path(root)
    sys.path.insert(0,str(root/'tests/program-focus'))
    from source_action_reduced_evolution_probe import build_context
    print('Reconstructing one native context',flush=True)
    ctx=build_context(root)
    print('Normal scalar energy and seed blindness',flush=True)
    normal=normal_screen(root,ctx)
    print('Receiver algebra and finite support/duality controls',flush=True)
    products=run_receiver_products(root,ctx)
    assert products['exact_real_linear_span_dimension']==32
    assert products['individual_square_nonzero_count']==32
    assert products['polarized_anticommutator_nonzero_pairs']==392
    assert not products['all_real_combinations_square_zero']
    expected=[{4:{'negative':6,'positive':4},7:{'negative':4,'positive':6}},
              {4:{'negative':4,'positive':6},7:{'negative':6,'positive':4}}]
    for i,row in enumerate(normal['roots']):
        for axis in [4,7]:
            assert row['sign_counts'][axis]['zero_source']==26
            assert row['sign_counts'][axis]['undetermined_interval']==0
            for s,v in expected[i][axis].items():assert row['sign_counts'][axis][s]==v
    return {'basis_revision':'da33e35d6921f30f2d7e0d6c1eba8955f34eee08',
      'normal_energy':normal,'receiver_algebra':products,
      'finite_adjoint_source_cone_controls':finite_controls(),
      'support_and_covariance_controls':support_and_covariance_controls(),
      'claim_ceiling':'Exact held-candidate pointwise and conditional structural results. No new choice, physical instability, fullM regularity or source/canon verdict.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2]);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    result=run(a.root);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print('PASS:144 normal energy cases,52 seed-blind forms,528 receiver pairs,finite adjoint/support/covariance controls')
