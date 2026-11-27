#!/usr/bin/env python3
"""Exact selected-current controls on existing scalar-normal solution germs.

No inference of forced negative energy, physical admissibility or GU failure.
"""
from pathlib import Path
from fractions import Fraction as Q
from types import SimpleNamespace
from math import isqrt
import argparse, hashlib, inspect, json, os, sys, time
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
sys.dont_write_bytecode=True
import source_action_scalar_normal_operator_probe as s
from source_action_deep_algebra import add,scale
from source_action_physical_probe import mul,gamma,components
from source_action_slice_completion_probe import covector,inject,inverse,readout
import source_action_deep_geometry as geo

def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def write(path,data):return s.write(path,data)
def jd(data):return s.jd(data)
def binding(args):
    paths=['source_action_scalar_normal_operator_probe.py','source_action_current_receiver_probe.py',
           'source_action_receiver_strategy_probe.py','source_action_physical_probe.py',
           'source_action_slice_completion_probe.py','source_action_full_auxiliary_probe.py',
           'source_action_even_spin5_probe.py','source_action_normal_normal_probe.py',
           'source_action_reduced_evolution_probe.py']
    return s.inputs(args)|{'tests/program-focus/'+p:digest(args.repo/'tests/program-focus'/p)for p in paths}
def setup(args):
    records,owned=s.owned_records(args,'source-action-scalar-normal-operator-certificates.json',['scalar-geometry.json'])
    path=args.cache/'scalar-geometry.json'
    if path.exists():assert json.loads(path.read_text())==records['scalar-geometry.json']
    else:write(path,records['scalar-geometry.json'])
    c=s.setup(args);groups,inputs=s.response_data(c,args)
    return c,groups,inputs|{'scalar':owned}
def Eplus(c,v):return c.add(c.s.rot(0,2,v),c.scale(c.I,c.s.rot(1,2,v)))
def Fminus(c,v):return c.add(c.s.rot(0,2,v),c.scale(-c.I,c.s.rot(1,2,v)))
def delta(c,v):return c.add(c.K(8,c.s.rot(0,1,v)),c.K(9,c.s.rot(0,2,v)),c.K(11,c.s.rot(1,2,v)))
def vertex(w,field,se=-Q(1,2)):
    a=components(w);z,nu=field
    r=[add(*(scale(1/geo.d[b],mul(gamma(b),add(mul(a[b],z[j]),scale(-1,mul(a[j],z[b])))))for b in range(14)),mul(a[j],nu))for j in range(14)]
    t=add(*(scale(1/geo.d[j],mul(a[j],z[j]))for j in range(14)),*(scale(se/geo.d[j],mul(gamma(j),mul(a[j],nu)))for j in range(14)))
    return r,t
def receiver(c,w):
    cols=[readout(inverse(covector(3),vertex(w,inject(j))))for j in range(5)]
    return {(i,j,cl):c.C(x)for j,col in enumerate(cols)for i,row in enumerate(col)for cl,x in row.items()if x}
def source_data(c,groups,index):
    v=c.K(3,c.bs[index]);F=lambda x:Fminus(c,x)
    Ka=lambda x:c.add(c.K(5,x),c.scale(-c.I,c.K(8,x)))
    Kb=lambda x:c.add(c.K(9,x),c.scale(-c.I,c.K(11,x)))
    Kbp=lambda x:c.add(c.K(9,x),c.scale(c.I,c.K(11,x)))
    dv=delta(c,v)
    assert dv==c.add(c.scale(-Q(7,2),Ka(v)),c.scale(Q(1,2),Kbp(F(v))))
    a=c.P(Ka(v));b=c.P(Kb(v));a5=s.part(c,a,5);a6=s.part(c,a,6);b6=s.part(c,b,6)
    assert a6==c.scale(Q(1,6),F(b6))
    assert not Eplus(c,a5)and not Eplus(c,b6)
    assert s.part(c,c.P(dv),5)==c.scale(-Q(7,2),a5)
    assert s.part(c,c.P(dv),6)==c.scale(-Q(7,12),F(b6))
    other=c.add(c.P(dv),c.scale(Q(7,2),a5),c.scale(Q(7,12),F(b6)))
    assert c.cas(other)==c.scale(56,other)
    assert not receiver(c,v)and not receiver(c,other)
    rest=dict(a5);coordinates={}
    for name in ('old5','repair5','even5'):
        g=groups[name];rest,co=s.reduce_native(c,rest,g['basis'],g['pivots']);coordinates[name]=co
    assert not rest,('complete N5 reconstruction failed',len(rest))
    return v,a5,b6,coordinates,{'range_index':index,'range':s.ser(c,v),'full_delta':s.ser(c,dv),
           'a5':s.ser(c,a5),'b6':s.ser(c,b6),'spin7_remainder':s.ser(c,other),
           'N5_coordinates':{k:[z.ser()for z in row]for k,row in coordinates.items()},
           'spin5_group_support':{k:sum(bool(z)for z in row)for k,row in coordinates.items()},
           'full_delta_identity':True,'projected5_6_ladder_identities':True,
           'range_and_spin7_seed_receivers_zero':True}

def stage_sources(args):
    tick=time.monotonic();c,groups,owned=setup(args)
    rows=[]
    for index in(3,12):
        *_,record=source_data(c,groups,index);rows.append(record)
        print('ON-SHELL SOURCE',index,'N5',record['spin5_group_support'],'terms',len(record['a5']),len(record['b6']),flush=True)
    out={'complete':True,'execution_probe_sha256':digest(__file__),'bindings':binding(args),
         'owned_inputs':owned,'rows':rows,'seconds':time.monotonic()-tick,
         'scope':'Exact coefficient/ladders for the same two signed scalar-normal germ amplitudes. No current nonzero or energy-transfer conclusion yet.'}
    write(args.cache/'onshell-sources.json',out);print('ON-SHELL SOURCES PASS seconds',out['seconds'],flush=True)

def original_receiver(c,args):
    import ast
    path=args.repo/'tests/program-focus/source_action_current_receiver_probe.py'
    tree=ast.parse(path.read_text());names={'vertex','receiver','bflat'}
    nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name in names]
    assert {n.name for n in nodes}==names
    namespace={'Q':Q,'geo':geo,'add':add,'scale':scale,'mul':mul,'gamma':gamma,
               'components':components,'readout':readout,'inverse':inverse,'inject':inject,
               'tau':covector(3),'C':c.C}
    exec(compile(ast.Module(body=nodes,type_ignores=[]),str(path),'exec'),namespace)
    return lambda w:namespace['bflat'](namespace['receiver'](w))
def adj_sign(cl):
    z=(-1)**(cl.bit_count()*(cl.bit_count()-1)//2)
    for a in range(14):
        if cl>>a&1 and geo.d[a]<0:z=-z
    return z
def hsweight(cl):
    z=Q(1)
    for a in range(14):
        if cl>>a&1:z*=abs(geo.d[a])
    return z
def sqrt_bounds(q):
    q=Q(q);d=10**20;n=isqrt(q.numerator*d*d//q.denominator)
    lo=Q(n,d);return lo,lo if lo*lo==q else Q(n+1,d)
def current_report(c,B,err,part):
    B={k:c.C(getattr(z,part))for k,z in B.items()if getattr(z,part)}
    keys=set(B)|{(j,i,cl)for i,j,cl in B}
    H={k:(B.get(k,c.C())+adj_sign(k[2])*B.get((k[1],k[0],k[2]),c.C()).conj())/2 for k in keys}
    H={k:z for k,z in H.items()if z}
    b2=sum(hsweight(k[2])*(z.a*z.a+z.b*z.b)for k,z in B.items())
    h2=sum(hsweight(k[2])*(z.a*z.a+z.b*z.b)for k,z in H.items())
    e2=sum(hsweight(k[2])*e*e for k,e in err.items())
    _,bu=sqrt_bounds(b2);hl,_=sqrt_bounds(h2);_,eu=sqrt_bounds(e2)
    margin=2*hl-bu-3*eu
    separated=[(k,z,err.get(k,Q()))for k,z in B.items()if abs(z.a)>err.get(k,Q())]
    best=max(separated,key=lambda row:abs(row[1].a)-row[2])if separated else None
    return {'real_component':part,'receiver_terms':len(B),'Hermitian_terms':len(H),
            'receiver_HS_squared':str(b2),'Hermitian_HS_squared':str(h2),
            'root_error_HS_squared':str(e2),'root_error_HS_upper':str(eu),
            'all_allowed_crossGram_nonzero_margin':str(margin),
            'all_allowed_crossGram_nonzero':margin>0,
            'separated_coefficient_count':len(separated),
            'best_coefficient':None if best is None else {'key':list(best[0]),'center':best[1].ser(),'error':str(best[2])},
            'method':'2||Herm B_center||HS-||B_center||HS-3||error||HS>0 implies Herm(N^-1 B_exact)!=0 for every N=c(I+E), c>0, ||E||op<1/2. No forced-energy assertion.'}
def solve5(c,group,co,ri,name):
    proof=group['certificate']['roots'][ri];eta=Q(proof['neumann_bound']);assert eta<1
    assert name in('old5','repair5')
    R=s.dm(c,proof['inverse_candidate'])if name=='old5'else s.candidate_matrix(c,group['candidate']['roots'][ri])
    x=[sum((a*b for a,b in zip(row,co)),c.C())for row in R]
    error=eta/(1-eta)*max(map(s.n1,x))
    return x,error,{'receiver':name,'eta':str(eta),'coordinate_l1_error':str(error)}
def solve6(c,group,source,ri):
    rhs=[c.C(c.E.pair({k:z.conj()for k,z in n.items()},source))for n in group['basis']]
    x=[c.C()for _ in rhs];errors=[Q()for _ in rhs];proofs=[]
    cert=group['certificate']['root_certificates'][ri]
    for cand,proof in zip(group['candidate'][ri]['blocks'],cert['blocks']):
        assert jd(cand['rational_inverse'])==proof['rational_inverse_sha256']
        ids=cand['indices'];assert ids==group['certificate']['constraint_components'][proof['component']]
        R=s.dm(c,cand['rational_inverse']);z=[sum((a*rhs[j]for a,j in zip(row,ids)),c.C())for row in R]
        eta=Q(proof['neumann_bound']);assert eta<1
        error=eta/(1-eta)*max(map(s.n1,z))
        for i,v in zip(ids,z):x[i]=v;errors[i]=error
        proofs.append({'component':proof['component'],'eta':str(eta),'coordinate_l1_error':str(error)})
    return x,errors,proofs
def stage_current(args):
    tick=time.monotonic();c,groups,owned=setup(args)
    import source_action_full_auxiliary_probe as full
    inherited=full.inherited_regular_controls(args.repo)
    prior,prior_binding=s.owned_records(args,'source-action-scalar-normal-operator-certificates.json',['scalar-solvable-controls.json'])
    direct=original_receiver(c,args)
    central={(1<<3,0):c.C(1)}
    assert receiver(c,central)=={(j,j,0):c.C(1)for j in range(5)}==direct(central)
    rows=[]
    for ri,index in((0,3),(1,12)):
        v,a5,b6,co,source=source_data(c,groups,index)
        energy=next(row for row in prior['scalar-solvable-controls.json']['owned_axis4_energy_sign_replay']if row['root']==ri and row['range_basis_index']==index)
        assert energy['sign']=='negative'and Q(energy['upper'])<0
        assert not receiver(c,c.P(c.K(4,v)))
        assert not receiver(c,c.P(c.geo.lower(v)))
        assert not any(co['even5'])
        x6,e6,p6=solve6(c,groups['spin6'],b6,ri)
        terms=[];proofs=[]
        for name in('old5','repair5'):
            if not any(co[name]):continue
            x,error,proof=solve5(c,groups[name],co[name],ri,name);proofs.append(proof)
            terms.extend((Q(7,2)*z,Q(7,2)*error,b)for z,b in zip(x,groups[name]['basis']))
        terms.extend((Q(7,12)*z,Q(7,12)*er,Fminus(c,b))for z,er,b in zip(x6,e6,groups['spin6']['basis'])if z or er)
        B={};err={};field={}
        for z,e,b in terms:
            rb=receiver(c,b)
            field=c.add(field,c.scale(z,b))
            for k,a in rb.items():B[k]=B.get(k,c.C())+z*a;err[k]=err.get(k,Q())+e*s.n1(a)
        B={k:z for k,z in B.items()if z};err={k:e for k,e in err.items()if e}
        assert B==receiver(c,field)==direct(field)
        reports=[current_report(c,B,err,p)for p in('a','b')]
        row={'root':ri,'range_index':index,'source_sha256':jd(source),'owned_negative_principal_energy':energy,
             'N5_inverse_errors':proofs,'N6_inverse_errors':p6,
             'center_field':s.ser(c,field),'center_receiver':[[*k,z.ser()]for k,z in sorted(B.items())],
             'receiver_entry_l1_errors':[[*k,str(e)]for k,e in sorted(err.items())],
             'original_full_four_arrow_receiver_matches':True,'frequency_independent_by_exact_blindness':True,
             'real_components':reports}
        rows.append(row)
        print('ON-SHELL CURRENT root',ri,'terms',len(B),'margins',[float(Q(r['all_allowed_crossGram_nonzero_margin']))for r in reports],flush=True)
        out={'complete':len(rows)==2,'execution_probe_sha256':digest(__file__),'bindings':binding(args),
             'owned_inputs':owned,'owned_signed_germ_inputs':prior_binding,'inherited_inverse_authentication':inherited,'roots':rows,
             'seconds':time.monotonic()-tick,
             'scope':'Selected-current test on the exact same signed-energy scalar-normal solution germs. Root-center field plus rigorous inherited inverse errors; affine graph identity makes the seed current independent of k. Nonzero current is not forced negative-energy excitation, energy exchange, physical admission or GU failure.'}
        write(args.cache/'onshell-current.json',out)
    print('ON-SHELL CURRENT COMPLETE seconds',out['seconds'],flush=True)

def boost_matrix():
    H=[[Q()for _ in range(14)]for _ in range(14)]
    H[3][4]=-Q(1);H[3][7]=Q(3);H[4][3]=H[7][3]=Q(1,16)
    assert all(geo.d[i]*H[i][j]+geo.d[j]*H[j][i]==0 for i in range(14)for j in range(14))
    return H
def stage_boost(args):
    tick=time.monotonic();c=s.setup(args);H=boost_matrix();L=lambda v:c.geo.rho(H,v)
    B=lambda v:c.add(c.K(4,v),c.scale(-3,c.K(7,v)))
    Y=lambda v:c.scale(Q(3,2),c.add(c.K(4,v),c.scale(-1,c.K(7,v))))
    checks=[]
    for i,v in enumerate(c.bs):
        Lv=L(v)
        assert c.add(L(c.K(3,v)),c.scale(-1,c.K(3,Lv)))==B(v)
        assert c.add(L(B(v)),c.scale(-1,B(Lv)))==c.scale(Q(1,8),c.K(3,v))
        assert L(Y(v))==Y(Lv)
        v2=L(Lv);v3=L(v2);v5=L(L(v3))
        assert not c.add(c.scale(16,v5),c.scale(-10,v3),Lv)
        assert c.cas(Lv)==L(c.cas(v))
        checks.append({'basis_index':i,'generator_terms':len(Lv)})
    for i,j in((0,1),(0,2),(1,2)):
        J=geo.zero();J[i][j]=Q(1);J[j][i]=-Q(1)
        R=[[geo.h_action(J,b).get(a,Q())for b in range(14)]for a in range(14)]
        assert all(sum(H[a][k]*R[k][b]-R[a][k]*H[k][b]for k in range(14))==0 for a in range(14)for b in range(14))
    out={'complete':True,'execution_probe_sha256':digest(__file__),'bindings':binding(args),
         'rational_generator_tangent_matrix':[[str(z)for z in row]for row in H],
         'all36_full_tensor_native_checks':checks,'generator_commutes_SO3_exact':True,
         'rational_carrier_polynomial':'16 L^5-10 L^3+L=0; J=sqrt(8)L',
         'nine_operator_weights':list(range(-4,5)),
         'nine_weight_proof':'On tangent J has weights -1,0,1; each exterior Clifford blade has weights -1,0,1; one-form tensor Clifford has weights -2..2. End-carrier differences are -4..4. J is semisimple.',
         'exact_change':'u=sqrt(8)tanh(v); x=r+(1/2)log(cosh(v)); q=exp(-vJ)h',
         'fixed_time_equation':'K3 h_v + K_zeta(v) h_x + D(v)h=0',
         'zeta':'sqrt(8)sech(v)*(3/2)(theta4-theta7)-(sqrt(8)/2)*(theta4-3theta7)',
         'D':'sqrt(8)sech(v)*exp(vJ)C0S exp(-vJ)-K3 J',
         'zeta_squared':'1/4-3sech(v)^2/4','zeta_derivative_at_zero':0,
         'scope':'Exact full-carrier coordinate/gauge identity. Rotated lower/background and moving-frame term retained; no invariant20 or growth transfer asserted.',
         'seconds':time.monotonic()-tick}
    write(args.cache/'onshell-boost.json',out);print('ON-SHELL BOOST PASS seconds',out['seconds'],flush=True)

def stage_spin0_scope(args):
    tick=time.monotonic();c=s.setup(args)
    import source_action_full_auxiliary_probe as full
    import source_action_even_spin5_probe as even
    raw=json.loads((args.repo/'lab/process/source-action-deep-coefficients.json').read_text())
    Ts=[{(e,cl):Q(z)for e,cl,z in row}for row in raw['basis']]
    T=c.add(*(c.scale(Q(x),v)for x,v in zip(raw['certified_roots'][0]['coordinates'],Ts)))
    rows=[];owned=[]
    for label in('even0','odd0'):
        names=[label+sign+kind+'.json'for sign in('-plus','-minus')for kind in('-highest','-basis')]
        data,binding0=s.owned_records(args,'source-action-full-auxiliary-'+label+'-root0-certificates.json',names);owned.append(binding0)
        for sector in(0,1):
            prefix=label+('-plus'if sector==0 else'-minus');high=data[prefix+'-highest.json'];bd=data[prefix+'-basis.json']
            car,keys,spin,chi,n=full.space(c,label,sector)
            assert high['bindings']==full.high_binding(args,label,sector)
            assert bd['bindings']['highest_sha256']==binding0['records'][prefix+'-highest.json']
            assert high['complete']and bd['complete']and high['weight_keys']==[list(k)for k in keys[0]]
            assert high['highest_dimension']==high['weight_dimension']-high['next_weight_dimension']
            assert bd['dimension']==n
            # One deterministic largest coordinate-support sample per complete sector.
            j=max(range(len(high['highest_coordinates'])),key=lambda j:len(high['highest_coordinates'][j]))
            co={i:c.C(*z)for i,z in high['highest_coordinates'][j]}
            field=c.add(*(c.scale(z,car.native(keys[0][i]))for i,z in co.items()))
            assert all(not c.s.rot(a,b,field)for a,b in((0,1),(0,2),(1,2)))
            assert not delta(c,field)
            start=time.monotonic();image=c.add(field,c.geo.lower(field),c.scale(2,c.integer.N(T,field)));seconds=time.monotonic()-start
            assert all(not c.s.rot(a,b,image)for a,b in((0,1),(0,2),(1,2)))
            row={'block':label,'B_sector':sector,'ambient_spin0':high['highest_dimension'],
                 'N0':n,'R0':high['highest_dimension']-n,'sample_highest_index':j,
                 'sample_coordinate_terms':len(co),'sample_native_terms':len(field),
                 'root0_C_image_terms':len(image),'root0_C_image_sha256':jd(s.ser(c,image)),
                 'one_root0_full_C_column_seconds':seconds,'spin0_full_C_closure_on_sample':True}
            rows.append(row);print('ON-SHELL SPIN0 SCOPE',label,sector,'ambient/N/R',row['ambient_spin0'],n,row['R0'],'C sec',seconds,flush=True)
    assert sum(r['ambient_spin0']for r in rows)==1924 and sum(r['N0']for r in rows)==786
    out={'complete':True,'execution_probe_sha256':digest(__file__),'bindings':binding(args),
         'owned_carriers':owned,'sectors':rows,'ambient_spin0':1924,'N0':786,'R0':1138,
         'all_complete_highest_constructor_data_already_owned':True,
         'scope':'Authenticated complete spin0 dimension and four bounded native C timing/closure samples, not full matrix assembly or a spectral conclusion.',
         'seconds':time.monotonic()-tick}
    write(args.cache/'onshell-spin0-scope.json',out)

def stage_principal(args):
    tick=time.monotonic();c,_,owned=setup(args);gd,M=s.load_geometry(c,args)
    K7=[list(row)for row in zip(*(c.coords(c.K(7,v))for v in c.bs))]
    U,Ui=M['U'],M['Uinv'];B=s.fast_mm(c,s.fast_mm(c,Ui,M['B']),U)
    B7=s.fast_mm(c,s.fast_mm(c,Ui,K7),U)
    V=[row[:20]for row in B[20:]];Vb=s.ma(c,V,s.ms(-3,[row[:20]for row in B7[20:]]))
    ks=s.kernel(c,V);_,piv=s.rref(c,V);assert len(ks)==len(piv)==10
    T=[[v[i]for v in ks]+[c.C(i==j)for j in piv]for i in range(20)]
    Ti=s.inverse(c,T);Kcols=[list(row)for row in zip(*ks)];Vc=[[row[j]for j in piv]for row in V]
    _,ids=s.rref(c,[list(row)for row in zip(*Vc)]);assert len(ids)==10
    rhs=s.fast_mm(c,Vb,Kcols)
    dFc=s.fast_mm(c,s.inverse(c,[Vc[i]for i in ids]),[rhs[i]for i in ids])
    assert s.fast_mm(c,Vc,dFc)==rhs
    div=[sum(c.geo.gammas[a][a][b]for a in range(14))for b in range(14)]
    Kdiv=[list(row)for row in zip(*(c.coords(c.add(*(c.scale(z,c.K(b,v))for b,z in enumerate(div)if z)))for v in c.bs))]
    Gram=M['Gram'];Cgeo=M['Lgeo']
    assert all(not Gram[i][j]for i in range(36)for j in range(36)if i!=j)
    star=[[Cgeo[j][i].conj()*Gram[j][j]/Gram[i][i]for j in range(36)]for i in range(36)]
    assert s.ma(c,star,s.ms(-1,Cgeo))==s.ms(-1,Kdiv)
    H=boost_matrix();Lm=[list(row)for row in zip(*(c.coords(c.geo.rho(H,v))for v in c.bs))]
    AL=s.fast_mm(c,M['A'],Lm)
    ALstar=[[AL[j][i].conj()*Gram[j][j]/Gram[i][i]for j in range(36)]for i in range(36)]
    assert s.ma(c,ALstar,s.ms(-1,AL))==s.ma(c,M['B'],s.ms(-3,K7))
    out={'complete':True,'execution_probe_sha256':digest(__file__),'bindings':binding(args),
         'owned_inputs':owned,'K7':s.sm(K7),'rational_boost_L':s.sm(Lm),
         'range_K_C_frame':s.sm(T),'range_K_C_frame_inverse':s.sm(Ti),
         'direction_beta_dF_C_CK':s.sm(dFc),'direction_beta_dF_C_CK_nonzero':any(z for row in dFc for z in row),
         'dF_C_definition':'Keep the owned pivot complement C fixed; F_C is projection onto C along ker(PKxiR). Only its CK derivative is nonzero, and V_C dF_C_CK=V_beta|K.',
         'adapted_divergence_covector':[str(z)for z in div],
         'signed_adjoint_controls':{'Cgeo_star_minus_Cgeo_equals_minus_Kdiv':True,'AL_star_minus_AL_equals_Kbeta':True},
         'scope':'Exact principal direction/projector derivative and adjoint controls only; no unproved intrinsic-symbol formula used.',
         'seconds':time.monotonic()-tick}
    write(args.cache/'onshell-principal.json',out);print('ON-SHELL PRINCIPAL PASS seconds',out['seconds'],'dF nonzero',out['direction_beta_dF_C_CK_nonzero'],flush=True)

def read_ball(c,data):return s.ball(s.dm(c,data['center']),[[Q(z)for z in row]for row in data['entry_l1_error']])
def stage_intrinsic(args):
    tick=time.monotonic();c,_,owned=setup(args);gd,M=s.load_geometry(c,args)
    pr=json.loads((args.cache/'onshell-principal.json').read_text());assert pr['complete']and pr['bindings']==binding(args)
    records,prior=s.owned_records(args,'source-action-scalar-normal-operator-certificates.json',['scalar-operator.json'])
    op=records['scalar-operator.json'];T=s.dm(c,pr['range_K_C_frame']);Ti=s.dm(c,pr['range_K_C_frame_inverse'])
    assert s.sm(T)==op['range_adapted_T']
    X=s.ms(-1,s.dm(c,pr['direction_beta_dF_C_CK']))
    S=s.eye(c,20)
    for i in range(10):
        for j in range(10):S[i+10][j]=-c.I*X[i][j]
    diag=[]
    for v in c.bs:
        signs={(-1)**(((e^cl)&15).bit_count()%2)for e,cl in v};assert len(signs)==1;diag.append(signs.pop())
    B36=[[c.C(diag[i]if i==j else 0)for j in range(36)]for i in range(36)]
    BU=s.fast_mm(c,s.fast_mm(c,M['Uinv'],B36),M['U']);BR=[row[:20]for row in BU[:20]]
    BT=s.fast_mm(c,s.fast_mm(c,Ti,BR),T)
    assert all(not BT[i][j]for i in range(20)for j in range(20)if(i<10)!=(j<10))
    assert s.fast_mm(c,BT,S)==s.fast_mm(c,S,BT)
    roots=[]
    for rr in op['roots']:
        A2=s.bmul(c,s.bmul(c,s.ball(Ti),read_ball(c,rr['L2'])),s.ball(T))
        A1=s.bmul(c,s.bmul(c,s.ball(Ti),read_ball(c,rr['L1'])),s.ball(T))
        A0=s.bmul(c,s.bmul(c,s.ball(Ti),read_ball(c,rr['L0_without_transverse_correction'])),s.ball(T))
        H=[[c.C()for _ in range(20)]for _ in range(20)];EH=[[Q()for _ in range(20)]for _ in range(20)]
        for i in range(20):
            for j in range(20):
                source=A1 if(i<10)==(j<10)else(A2 if i<10 else A0)
                fac=c.I if(i<10)==(j<10)else c.C(-1 if i<10 else 1)
                H[i][j]=fac*source[0][i][j];EH[i][j]=source[1][i][j]
        nsq=s.bmul(c,s.ball(H,EH),s.ball(H,EH));nm=s.tr(nsq[0]);ne=sum(nsq[1][i][i]for i in range(20))
        assert nm.ser()==rr['naive_trace_H_squared_without_transverse_correction']['center']
        assert str(ne)==rr['naive_trace_H_squared_without_transverse_correction']['l1_error']
        assert not any(z for row in s.ma(c,s.fast_mm(c,BT,H),s.fast_mm(c,H,BT))for z in row)
        mu=s.bmul(c,s.ball(S),s.ball(H,EH))
        assert not any(z for row in s.ma(c,s.fast_mm(c,BT,mu[0]),s.fast_mm(c,mu[0],BT))for z in row)
        assert not s.tr(mu[0])
        square=s.bmul(c,mu,mu);moment=s.tr(square[0]);error=sum(square[1][i][i]for i in range(20))
        lower,upper=moment.a-error,moment.a+error
        row={'root':rr['root'],'owned_root_sha256':rr['owned_root_sha256'],'radius':rr['radius'],
             'H_naive_no_Delta0':s.sb(s.ball(H,EH)),'H_intrinsic':s.sb(mu),
             'trace_exact_zero_by_full_family_B':True,
             'trace_H_intrinsic_squared':{'center':moment.ser(),'l1_error':str(error),'real_lower':str(lower),'real_upper':str(upper),
                 'real_lower_float':float(lower),'real_upper_float':float(upper),'positive_certified':lower>0},
             'max_real_eigenvalue_above_1_over_40':lower>Q(19,80)}
        roots.append(row);print('ON-SHELL INTRINSIC root',rr['root'],'traceH2',float(lower),float(upper),'positive',lower>0,flush=True)
    out={'complete':True,'execution_probe_sha256':digest(__file__),'bindings':binding(args),
         'principal_record_sha256':digest(args.cache/'onshell-principal.json'),'owned_operator':prior,
         'X_CK':s.sm(X),'left_shear':s.sm(S),'B_in_K_C_frame':s.sm(BT),'roots':roots,
         'formula':'H_intrinsic = [[I,0],[-iX,I]] H_naive; this is left multiplication, not similarity. V_C X=-V_beta K.',
         'whole_family_trace_proof':'B preserves K,C and commutes X; all exact L_j anticommute B, hence H_naive anticommutes B. The left shear commutes B, hence H_intrinsic anticommutes B and has trace0.',
         'scope':'Exact root-box finite arithmetic for the independently derived actual microlocal principal-symbol formula. Interpretation requires its separately reviewed geometric/pseudodifferential derivation; no source-selected physical domain or GU verdict.',
         'seconds':time.monotonic()-tick}
    write(args.cache/'onshell-intrinsic.json',out);print('ON-SHELL INTRINSIC COMPLETE seconds',out['seconds'],flush=True)

RECORDS=('onshell-sources.json','onshell-current.json','onshell-boost.json',
         'onshell-spin0-scope.json','onshell-principal.json','onshell-intrinsic.json')
BUNDLE='source-action-onshell-dynamics-certificates.json'
STAGES=(stage_sources,stage_current,stage_boost,stage_spin0_scope,stage_principal,stage_intrinsic)
def stage_bundle(args):
    rows={name:json.loads((args.cache/name).read_text())for name in RECORDS}
    assert all(row['complete']and row['execution_probe_sha256']==digest(__file__)and row['bindings']==binding(args)for row in rows.values())
    assert all(r['all_allowed_crossGram_nonzero']for root in rows['onshell-current.json']['roots']for r in root['real_components'])
    assert all(r['trace_H_intrinsic_squared']['positive_certified']and r['max_real_eigenvalue_above_1_over_40']for r in rows['onshell-intrinsic.json']['roots'])
    assert rows['onshell-intrinsic.json']['principal_record_sha256']==digest(args.cache/'onshell-principal.json')
    out={'schema':'gu-onshell-dynamics-certificates-v1','data_only':True,
         'final_probe_sha256':digest(__file__),'bindings':binding(args),
         'records':{name:s.encode_record(args.cache/name)for name in RECORDS},
         'scope':'Same signed-germ pointwise selected current, exact boost straightening and intrinsic20 principal-symbol arithmetic under the separately reviewed microlocal derivation. Four spin0 columns are timing samples only. No forced negative energy, nonlinear/physical instability or GU verdict.'}
    path=args.repo/'lab/process'/BUNDLE;write(path,out);assert path.stat().st_size<45_000_000
    print('ON-SHELL BUNDLE',len(RECORDS),'records bytes',path.stat().st_size,flush=True)
def restore(args,copy):
    import base64,zlib
    path=args.repo/'lab/process'/BUNDLE;d=json.loads(path.read_text())
    assert d['schema']=='gu-onshell-dynamics-certificates-v1'and d['data_only']
    assert d['final_probe_sha256']==digest(__file__)and d['bindings']==binding(args)
    assert set(d['records'])==set(RECORDS)
    for name,r in d['records'].items():
        assert r['encoding']=='zlib-base64-json';raw=zlib.decompress(base64.b64decode(r['data']))
        assert len(raw)==r['uncompressed_bytes']and hashlib.sha256(raw).hexdigest()==r['sha256']
        if copy:(args.cache/name).write_bytes(raw)
        else:assert(args.cache/name).read_bytes()==raw
    return d
def stage_unpack(args):restore(args,True);print('ON-SHELL UNPACK',len(RECORDS),'authenticated records',flush=True)
def mathematical(data):
    excluded={'seconds','one_root0_full_C_column_seconds','execution_probe_sha256'}
    if isinstance(data,dict):return {k:mathematical(v)for k,v in data.items()if k not in excluded}
    if isinstance(data,list):return [mathematical(v)for v in data]
    return data
def stage_replay(args):
    import tempfile
    tick=time.monotonic();restore(args,False)
    child=SimpleNamespace(**vars(args));child.cache=Path(tempfile.mkdtemp(prefix='recomputed-',dir=args.cache))
    checks=[]
    for name,stage in zip(RECORDS,STAGES):
        stage(child)
        old=json.loads((args.cache/name).read_text());new=json.loads((child.cache/name).read_text())
        assert mathematical(old)==mathematical(new),('Native mathematical replay mismatch',name)
        (child.cache/name).write_bytes((args.cache/name).read_bytes())
        checks.append(name);print('ON-SHELL REPLAY mathematical match',name,flush=True)
    restore(args,False)
    receipt={'passed':True,'probe_sha256':digest(__file__),'bundle_sha256':digest(args.repo/'lab/process'/BUNDLE),
             'all_six_mathematical_records_recomputed':checks,
             'same_signed_germ_sources_and_original_receivers_recomputed':True,
             'both_roots_both_real_component_crossGram_margins_recomputed':True,
             'all36_full_tensor_boost_polynomial_controls_recomputed':True,
             'owned_spin0_dimension_and_four_native_columns_recomputed':True,
             'native_K7_projector_derivative_and_signed_adjoints_recomputed':True,
             'both_intrinsic20_moment_error_bounds_recomputed':True,
             'inherited_auxiliary_inverses_authenticated_not_regenerated':True,
             'floating_inverse_regenerated':False,'seconds':time.monotonic()-tick,
             'scope':'Bounded full native replay of this wave; the microlocal analytic theorem is separately reviewed. No full spin0 matrix assembly or forced-energy/physical conclusion.'}
    write(args.output or args.cache/'onshell-replay.json',receipt);print('ON-SHELL REPLAY PASS seconds',receipt['seconds'],flush=True)
def stage_status(args):
    restore(args,False);cur=json.loads((args.cache/'onshell-current.json').read_text());intr=json.loads((args.cache/'onshell-intrinsic.json').read_text())
    out={'probe_sha256':digest(__file__),'bundle_sha256':digest(args.repo/'lab/process'/BUNDLE),'all_records_authenticated':True,
         'four_crossGram_margins_positive':all(r['all_allowed_crossGram_nonzero']for root in cur['roots']for r in root['real_components']),
         'both_intrinsic_moments_positive':all(r['trace_H_intrinsic_squared']['positive_certified']for r in intr['roots']),
         'both_intrinsic_max_real_eigenvalue_above_1_over_40':all(r['max_real_eigenvalue_above_1_over_40']for r in intr['roots']),
         'scope':'Authentication/status only; replay performs native recomputation.'}
    if args.output:write(args.output,out)
    print('ON-SHELL STATUS PASS',out['four_crossGram_margins_positive'],out['both_intrinsic_moments_positive'],flush=True)
def stage_finalize(args):
    for stage in STAGES:stage(args)
    stage_bundle(args)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2])
    ap.add_argument('--cache',type=Path,required=True);ap.add_argument('--mode',choices=['sources','current','boost','spin0-scope','principal','intrinsic','bundle','unpack','replay','status','finalize'],default='sources')
    ap.add_argument('--output',type=Path)
    args=ap.parse_args();args.repo=args.repo.resolve();args.cache=args.cache.resolve();args.cache.mkdir(parents=True,exist_ok=True)
    assert args.repo==Path(__file__).resolve().parents[2]
    {'sources':stage_sources,'current':stage_current,'boost':stage_boost,'spin0-scope':stage_spin0_scope,'principal':stage_principal,'intrinsic':stage_intrinsic,
     'bundle':stage_bundle,'unpack':stage_unpack,'replay':stage_replay,'status':stage_status,'finalize':stage_finalize}[args.mode](args)
if __name__=='__main__':main()
