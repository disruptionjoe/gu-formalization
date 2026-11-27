#!/usr/bin/env python3
"""Matched selected CK current first jet on the intrinsic scalar graph.

No physical admission, coherent-packet output, forced response or GU verdict.
All native jobs are explicit modes; imported owned probes do not run their CLI.
"""
from pathlib import Path
from fractions import Fraction as Q
from types import SimpleNamespace
import argparse, base64, hashlib, inspect, json, os, sys, time, zlib
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[name]='1'
sys.dont_write_bytecode=True
import source_action_scalar_normal_operator_probe as s
import source_action_onshell_dynamics_probe as o
import source_action_paired_response_probe as p
from source_action_deep_algebra import add,scale

ROOT=Path(__file__).resolve().parents[2]
C,I=p.C,p.I
digest=s.digest
jd=s.jd
write=s.write


def require(ok,label):
    if not ok:raise ValueError(label)


def binding(args):
    names=['source_action_selected_jet_probe.py','source_action_scalar_normal_operator_probe.py',
           'source_action_onshell_dynamics_probe.py','source_action_paired_response_probe.py',
           'source_action_constraint_consistency_probe.py','source_action_current_receiver_probe.py',
           'source_action_physical_probe.py','source_action_slice_completion_probe.py']
    # Procedure binding permits adding read-only diagnostics without relabeling production.
    out=s.inputs(args)|{'tests/program-focus/'+name:digest(args.repo/'tests/program-focus'/name)
                       for name in names if name!='source_action_selected_jet_probe.py'}
    return out


def records(args,bundle,names):
    values,owned=s.owned_records(args,bundle,names)
    for name,value in values.items():
        path=args.cache/name
        if path.exists():require(json.loads(path.read_text())==value,'owned cache differs: '+name)
        else:write(path,value)
    return values,owned


def field_errors(basis,errors):
    out={}
    for v,e in zip(basis,errors):
        if e:
            for key,z in v.items():out[key]=out.get(key,Q())+s.n1(C(z))*e
    return out


def scale_errors(q,errors):return {k:abs(q)*v for k,v in errors.items()if v}
def error_record(errors):return [[e,cl,str(z)]for(e,cl),z in sorted(errors.items())if z]
def read_errors(rows):return {(e,cl):Q(z)for e,cl,z in rows}
def matrix_record(B):return [[i,j,cl,C(z).ser()]for(i,j,cl),z in sorted(B.items())if z]
def read_matrix(rows):return {(i,j,cl):C(*z)for i,j,cl,z in rows}


def solve_low(c,group,name,source,root):
    """One inherited response, with native coefficient bounds, no new inverse."""
    n=len(source)
    if not any(source):return [C()for _ in source],[Q()for _ in source],{'exact_zero_source':True}
    if name=='spin6':
        x=[C()for _ in source];err=[Q()for _ in source];details=[]
        proofs=group['certificate']['root_certificates'][root]['blocks']
        for cand,proof in zip(group['candidate'][root]['blocks'],proofs):
            require(jd(cand['rational_inverse'])==proof['rational_inverse_sha256'],'N6 inverse hash')
            ids=cand['indices'];eta=Q(proof['neumann_bound']);require(eta<1,'N6 bound')
            values=[sum((C(*z)*source[j]for z,j in zip(row,ids)),C())for row in cand['rational_inverse']]
            eps=eta/(1-eta)*max(map(s.n1,values))
            for j,z in zip(ids,values):x[j]=z;err[j]=eps
            details.append({'eta':str(eta),'indices':ids,'error':str(eps)})
        return x,err,{'blocks':details}
    proof=group['certificate']['roots'][root];eta=Q(proof['neumann_bound']);require(eta<1,'N5 bound')
    R=s.dm(c,proof['inverse_candidate'])if name=='old5'else s.candidate_matrix(c,group['candidate']['roots'][root])
    if name=='even5':
        D=list(map(Q,group['certificate']['norm_constants']['basis_norms']))
        y=[sum((a*b/d for a,b,d in zip(row,source,D)),C())for row in R]
        x=[z/d for z,d in zip(y,D)]
        eps=eta/(1-eta)*sum(map(s.n1,y))
        # Coordinatewise consequence of the stronger weighted-l1 certificate.
        err=[eps/d for d in D]
    else:
        x=[sum((a*b for a,b in zip(row,source)),C())for row in R]
        eps=eta/(1-eta)*max(map(s.n1,x));err=[eps]*n
    return x,err,{'eta':str(eta),'coordinate_error_bound':str(eps),'mode':group['mode']}


def stage_prepare(args):
    tick=time.monotonic()
    inherited,scalar=records(args,'source-action-scalar-normal-operator-certificates.json',
                            ['scalar-geometry.json','scalar-affine.json','scalar-response-maps.json'])
    intrinsic,onshell=records(args,'source-action-onshell-dynamics-certificates.json',
                             ['onshell-principal.json','onshell-intrinsic.json'])
    c=s.setup(args);gd,M=s.load_geometry(c,args);groups,owned=s.response_data(c,args)
    maps=inherited['scalar-response-maps.json'];aff=inherited['scalar-affine.json']
    require(maps['complete']and aff['complete'],'complete owned source maps')
    require(maps['bindings']['native_inputs']==s.inputs(args)and
            maps['bindings']['owned_inputs']==owned,'source map bindings')
    T=s.dm(c,intrinsic['onshell-principal.json']['range_K_C_frame'])
    require(all(sum(bool(z)for z in col)==1 for col in zip(*T)),'owned sparse K/C frame')
    U,Ui=M['U'],M['Uinv'];Ut=[[z.conj()for z in row]for row in zip(*U)]
    GG=s.fast_mm(c,s.fast_mm(c,Ut,M['Gram']),U);GN=[row[20:]for row in GG[20:]]
    Bt=s.fast_mm(c,s.fast_mm(c,Ui,M['B']),U);Bnr=[row[:20]for row in Bt[20:]]
    N=groups['spin7']['basis'];Rfields=[s.decode(c,row)for row in gd['range_basis']]
    Efields=[add(*(scale(T[i][j],Rfields[i])for i in range(20)))for j in range(20)]
    geom=s.geometry_data(c)
    require(not any(any(row)for row in c.geo.adapt[8]),'H8=0 chart matching')
    direct=[]
    for j in(0,10):
        v=Efields[j]
        formula=scale(Q(1,4),add(scale(62,c.K(8,v)),scale(-1,c.cas(c.K(8,v)))))
        require(geom.derivative(8,v)==formula,'actual isotropy derivative equals Casimir formula')
        require(not add(c.K(5,v),scale(I,c.K(8,v))),'highest7 Kap zero')
        direct.append({'column':j,'native_derivative_terms':len(formula),'Casimir_identity':True,'Kap_zero':True})
    F=lambda v:o.Fminus(c,v)
    print('SELECTED prepare geometry controls seconds',time.monotonic()-tick,flush=True)
    lowered6=[F(v)for v in groups['spin6']['basis']]
    coeff=[[[C()for _ in range(36)]for _ in range(36)]for _ in range(59)]
    for row in aff['pairs']:
        i,j=row['i'],row['j']
        for a,z in enumerate(row['coefficients']):
            z=C(*z);coeff[a][i][j]=z/M['Gram'][i][i]
            coeff[a][j][i]=z.conj()/M['Gram'][j][j]
    raw=json.loads((args.repo/'lab/process/source-action-deep-coefficients.json').read_text())
    evo=json.loads((args.repo/'lab/process/source-action-reduced-evolution.json').read_text())
    rootrows=[]
    for ri,root in enumerate(raw['certified_roots']):
        xs=list(map(Q,root['coordinates']));radius=Q(root['certificate']['radius'])
        C0=s.ma(c,s.eye(c,36),M['Lgeo'],*(s.ms(x,A)for x,A in zip(xs,coeff)))
        Cerr=[[radius*sum(s.n1(A[i][j])for A in coeff)for j in range(36)]for i in range(36)]
        Cs=s.bmul(c,s.bmul(c,s.ball(Ui),s.ball(C0,Cerr)),s.ball(U))
        Cnr=s.bpart(Cs,range(20,36),range(20));Mn=s.bpart(Cs,range(20,36),range(20,36))
        candidate=evo['spin7_inverse_candidates'][ri];Hinv=s.dm(c,candidate['inverse'])
        proof=groups['spin7']['certificate']['root_certificates'][ri]
        require(jd(candidate['inverse'])==proof['inverse_sha256'],'N7 inverse hash')
        require(jd(s.sm(s.fast_mm(c,GN,Mn[0])))==proof['matrix_center_sha256'],'N7 same center matrix')
        eta=Q(proof['neumann_bound'])
        Y=s.bmul(c,s.solve_paired7(c,Hinv,GN,s.ball(Bnr),eta),s.ball(T))
        Z=s.bmul(c,s.solve_paired7(c,Hinv,GN,Cnr,eta),s.ball(T))
        rows=[]
        for j in range(20):
            resp=Z if j<10 else Y;fac=-C(1)if j<10 else -I
            field=add(Efields[j]if j<10 else {},*(scale(fac*resp[0][i][j],N[i])for i in range(16)))
            errors=field_errors(N,[resp[1][i][j]for i in range(16)])
            require(not o.receiver(c,field),'leading graph exact center seed blindness')
            correction={};de={};details={}
            if j<10:
                for name in('old5','repair5','even5','spin6'):
                    group=groups[name];S=s.dm(c,maps['groups'][name]['source_matrix'])
                    source=[sum((row[k]*T[k][j]for k in range(20)),C())for row in S]
                    co,er,detail=solve_low(c,group,name,source,ri);details[name]=detail
                    bs=lowered6 if name=='spin6'else group['basis']
                    fac=-Q(5,12)*I if name=='spin6'else -4*I
                    correction=add(correction,*(scale(fac*z,v)for z,v in zip(co,bs)))
                    de=add(de,scale_errors(s.n1(fac),field_errors(bs,er)))
            rows.append({'column':j,'G1':s.ser(c,field),'G1_entry_errors':error_record(errors),
                         'd8G1_visible_part':s.ser(c,correction),'d8G1_entry_errors':error_record(de),
                         'response_proofs':details})
        rootrows.append({'root':ri,'radius':str(radius),'owned_root_sha256':jd(root),'columns':rows})
        print('SELECTED prepared root',ri,'seconds',time.monotonic()-tick,flush=True)
    out={'complete':True,'execution_probe_sha256':digest(__file__),'bindings':binding(args),
         'owned':{'scalar':scalar,'onshell':onshell,'responses':owned},'direct_controls':direct,
         'K_C_frame':s.sm(T),'roots':rootrows,'seconds':time.monotonic()-tick,
         'formula':'G1=[eK-ZeK,-iYeC]; visible d8G1_K=-4i M5^-1 a5-(5i/12)F M6^-1 b6; d8G1_C=0',
         'scope':'Matched pointwise graph and solving-axis derivative only; the seed-blind N7 derivative part is omitted only after the current receiver.'}
    write(args.cache/'selected-prepare.json',out)
    print('SELECTED PREPARE PASS seconds',out['seconds'],flush=True)


def hs_inner(A,B):
    return sum(o.hsweight(k[2])*(C(z).conj()*B.get(k,C())).a for k,z in A.items())


def output_stats(B):
    H=p.herm(B);b=hs_inner(B,B);h=hs_inner(H,H)
    return {'terms':len(B),'Hermitian_terms':len(H),'raw_HS_squared':str(b),
            'Hermitian_HS_squared':str(h),'robust_quadratic_center':str(4*h-b),
            'Hermitian_raw_ratio':float(h/b)if b else None}


def stage_outputs(args):
    tick=time.monotonic();data=json.loads((args.cache/'selected-prepare.json').read_text())
    require(data['complete']and data['bindings']==binding(args),'prepared bindings')
    fixed=p.fixed_jet_norm_bounds();controls=p.fast_error_control(fixed)
    c=SimpleNamespace(C=C);path=args.cache/'selected-outputs.json'
    bind={'inputs':binding(args),'prepare_sha256':digest(args.cache/'selected-prepare.json'),
          'procedure_sha256':hashlib.sha256('\n'.join(inspect.getsource(fn)for fn in(stage_outputs,output_stats,hs_inner)).encode()).hexdigest()}
    out={'complete':False,'bindings':bind,'execution_probe_sha256':digest(__file__),
         'realification':'For w=x+i y and physical real coefficient field Re(G1 w), output columns are Re(G1) and -Im(G1); no adjoint contour is imposed.',
         'norm_control':{k:str(v)for k,v in controls.items()},'columns':[]}
    if path.exists():out=json.loads(path.read_text());require(out['bindings']==bind,'output checkpoint binding')
    done={(row['root'],row['column'])for row in out['columns']}
    budget=args.steps or 10**9;completed=0
    for rr in data['roots']:
        ri=rr['root']
        if args.root_index is not None and ri!=args.root_index:continue
        Tb=p.root_T(args.repo,ri);Tc={k:z.c for k,z in Tb.items()if z.c};Te={k:z.e for k,z in Tb.items()if z.e}
        for row in rr['columns']:
            j=row['column']
            if args.columns and j not in args.columns:continue
            if(ri,j)in done:continue
            if completed>=budget:break
            start=time.monotonic();u=s.decode(c,row['G1']);ue=read_errors(row['G1_entry_errors'])
            du=s.decode(c,row['d8G1_visible_part']);de=read_errors(row['d8G1_entry_errors'])
            print('SELECTED output start',ri,j,'terms',len(u),len(du),flush=True)
            base=p.center_full_R(u,Tc);correction=o.receiver(c,du);constant=add(base,correction)
            bounds=p.full_jet_error_bounds(Tc,Te,u,ue,fixed)
            derivative_error=Q(9,4)*fixed['Q']*p.vertex_norm_from_component_norms(p.connection_component_norms(de))
            errors=[bounds['constant']+derivative_error]+bounds['spectral']
            realrows=[]
            for part,sign,label in(('a',1,'Re_w'),('b',-1,'Im_w')):
                realu={k:C(sign*getattr(z,part))for k,z in u.items()if getattr(z,part)}
                B0={k:C(sign*getattr(z,part))for k,z in constant.items()if getattr(z,part)}
                coeffs=[B0]+[p.jet(realu,a)for a in range(4)]
                require(all(not z.b for z in B0.values())and
                        all(not z.a for B in coeffs[1:]for z in B.values()),'exact constant/spectral coefficient reality')
                require(all(hs_inner(B0,B)==hs_inner(p.herm(B0),p.herm(B))==0 for B in coeffs[1:]),
                        'constant/spectral HS cross terms exactly zero')
                realrows.append({'part':label,'coefficients':[matrix_record(B)for B in coeffs],
                                 'global_HS_error_bounds':list(map(str,errors)),
                                 'statistics':[output_stats(B)for B in coeffs],
                                 'constant_spectral_cross_exact_zero':True})
            result={'root':ri,'column':j,'constant_without_graph_motion_sha256':jd(matrix_record(base)),
                    'graph_motion_receiver':matrix_record(correction),'graph_motion_terms':len(correction),
                    'complex_constant':matrix_record(constant),'real_columns':realrows,
                    'seconds':time.monotonic()-start}
            out['columns'].append(result);completed+=1
            out['complete']=len(out['columns'])==40;out['seconds_this_batch']=time.monotonic()-tick
            write(path,out)
            print('SELECTED output complete',ri,j,'seconds',result['seconds'],'constant stats',
                  [r['statistics'][0]['Hermitian_raw_ratio']for r in realrows],flush=True)
        if completed>=budget:break
    print('SELECTED OUTPUT CHECKPOINT',len(out['columns']),'/40 seconds',time.monotonic()-tick,flush=True)


def modular_rank(columns,prime=65537):
    """Exact independence witness modulo a good prime, on real native fields."""
    rows={};pivots=[]
    for value in columns:
        v={k:(Q(z).numerator%prime)*pow(Q(z).denominator%prime,-1,prime)%prime
           for k,z in value.items()if z}
        v={k:z for k,z in v.items()if z}
        while v:
            k=min(v);z=v[k]
            if k in rows:
                row=rows[k]
                for t,a in row.items():
                    w=(v.get(t,0)-z*a)%prime
                    if w:v[t]=w
                    else:v.pop(t,None)
            else:
                inv=pow(z,-1,prime);rows[k]={t:a*inv%prime for t,a in v.items()};pivots.append(k);break
    return {'rank':len(rows),'prime':prime,'denominators_all_invertible':True,'pivots':pivots}


def integer_operator(B):
    from math import lcm,gcd
    denominator=lcm(*(q.denominator for z in B.values()for q in(z.a,z.b)))if B else 1
    raw={k:(int(z.a*denominator),int(z.b*denominator))for k,z in B.items()}
    content=0
    for a,b in raw.values():content=gcd(content,abs(a));content=gcd(content,abs(b))
    content=content or 1
    return {k:(a//content,b//content)for k,(a,b)in raw.items()},Q(content,denominator)


def real_trace(A,B):
    value=0
    for(i,j,cl),(a,b)in A.items():
        c,d=B.get((j,i,cl),(0,0));value+=int(p.g.cliff_mul(cl,cl)[1])*(a*c-b*d)
    return value


def integer_hs(A,B):
    return sum(int(o.hsweight(k[2]))*(a*B.get(k,(0,0))[0]+b*B.get(k,(0,0))[1])
               for k,(a,b)in A.items())


def stage_spectral(args):
    tick=time.monotonic()
    records0,owned=records(args,'source-action-scalar-normal-operator-certificates.json',['scalar-geometry.json'])
    geometry=records0['scalar-geometry.json'];basis=[s.decode(SimpleNamespace(C=C),row)for row in geometry['basis']]
    require(len(basis)==36,'complete owned highest7 carrier')
    maps=[];labels=[];real8=[];controls=0
    c=SimpleNamespace(C=C)
    for j,u in enumerate(basis):
        require(set(e for e,cl in u)<={32,256},'highest7 has only normal legs5/8')
        require(not p.contraction(p.components(u),range(14)),'native gamma trace zero')
        require(not o.receiver(c,u),'complete36 seed receiver blind')
        for part,sign in(('a',1),('b',-1)):
            ur={k:Q(sign*getattr(z,part))for k,z in u.items()if getattr(z,part)}
            require(not p.contraction(p.components(ur),range(14)),'realification gamma trace zero')
            real8.append({cl:z for(e,cl),z in ur.items()if e==256})
        complex_maps=[]
        for axis in range(4):
            B=p.jet(u,axis);expected={};u8=p.components(u)[8]
            # Use owned matter contraction; no compact raw-current formula is assumed.
            from source_action_slice_completion_probe import slash
            clambda=slash(p.covector(axis))
            for col in range(5):
                z,nu=p.inject(col);t=add(nu,scale(-1,p.contraction(z,range(4))))
                T8=add(p.mul(u8,nu),*(scale(-1/p.g.d[h],p.mul(p.gamma(h),p.mul(u8,z[h])))for h in range(4)))
                v3=scale(-2*I,p.mul(u8,p.mul(clambda,t)))
                vs=scale(2*I,p.mul(p.gamma(3),add(p.mul(clambda,T8),p.mul(u8,p.mul(clambda,t)))))
                expected.update({(3,col,cl):v for cl,v in v3.items()})
                expected.update({(4,col,cl):v for cl,v in vs.items()})
                controls+=1
            require(B==expected,'direct complete spectral jet equals corrected formula')
            complex_maps.append(B)
        for part,label in(('b','Re_field'),('a','minus_Im_field')):
            for axis,B in enumerate(complex_maps):
                realmap={k:I*getattr(z,part)for k,z in B.items()if getattr(z,part)}
                integer,factor=integer_operator(realmap)
                require(all(a==0 for a,b in integer.values()),'real insertion spectral output is imaginary')
                maps.append(integer);labels.append({'basis':j,'part':label,'axis':axis,'positive_scale':str(factor)})
        if(j+1)%6==0:print('SELECTED spectral',j+1,'/36 seconds',time.monotonic()-tick,flush=True)
    rank=modular_rank(real8);require(rank['rank']==72,'realified u8 map injective')
    n=len(maps);raw=[[0]*n for _ in range(n)];trace=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            raw[i][j]=raw[j][i]=integer_hs(maps[i],maps[j])
            trace[i][j]=trace[j][i]=real_trace(maps[i],maps[j])
    robust=[[raw[i][j]+2*trace[i][j]for j in range(n)]for i in range(n)]
    # A rational exact negative witness, if found, refutes only this sufficient Gram condition.
    import numpy as np
    diagonal=np.sqrt(np.maximum(1,np.array([raw[i][i]for i in range(n)],dtype=float)))
    balanced=np.array(robust,dtype=float)/diagonal[:,None]/diagonal[None,:]
    eig,vec=np.linalg.eigh(balanced);witness=None
    if eig[0]<-1e-9:
        v=vec[:,0]/diagonal;v=v/max(abs(v))
        for scale10 in(10**3,10**5,10**7):
            z=[int(round(float(x)*scale10))for x in v]
            value=sum(z[i]*robust[i][j]*z[j]for i in range(n)for j in range(n))
            if value<0:
                witness={'integer_coordinates':z,'exact_robust_quadratic':str(value),
                         'interpretation':'The full-carrier spectral robust-Gram sufficient condition fails. This is not current blindness or a growing-sector statement.'};break
        require(witness is not None,'negative discovery requires exact rational witness')
    out={'complete':True,'execution_probe_sha256':digest(__file__),'bindings':binding(args),'owned_geometry':owned,
         'procedure_sha256':hashlib.sha256('\n'.join(inspect.getsource(fn)for fn in(stage_spectral,integer_operator,real_trace,integer_hs,modular_rank)).encode()).hexdigest(),
         'native_complex_basis_dimension':36,'realification_dimension':72,'direct_five_slot_formula_checks':controls,
         'complete_seed_blindness_checks':36,'realified_u8_rank':rank,'affine_spectral_labels':labels,
         'integer_spectral_maps':[[[i,j,cl,a,b]for(i,j,cl),(a,b)in sorted(B.items())]for B in maps],
         'real_trace_pairing_matrix':trace,'raw_HS_Gram':raw,'robust_Gram':robust,
         'real_trace_is_identically_zero':not any(z for row in trace for z in row),
         'balanced_minimum_eigenvalue_diagnostic':float(eig[0]),'exact_negative_witness':witness,
         'seconds':time.monotonic()-tick,
         'scope':'Complete native highest7 spectral current map and actual real trace/Gram controls. The diagonal scaling is computational only. No constant-frequency or physical normalized-current conclusion is inferred.'}
    write(args.cache/'selected-spectral.json',out)
    print('SELECTED SPECTRAL PASS seconds',out['seconds'],'min diagnostic',float(eig[0]),'exact negative',bool(witness),flush=True)


def spectral_certificate(data):
    labels=data['affine_spectral_labels'];raw=data['raw_HS_Gram'];trace=data['real_trace_pairing_matrix']
    G=data['robust_Gram'];n=len(G);require(n==288,'complete real spectral tensor dimension')
    factors=[Q(row['positive_scale'])for row in labels]
    require(all(x>0 for x in factors),'positive exact coefficient scaling')
    require(all(G[i][j]==G[j][i]==raw[i][j]+2*trace[i][j]
                for i in range(n)for j in range(n)),'actual real robust Gram identity')
    seen=set();blocks=[];lowers=[]
    for i in range(n):
        if i in seen:continue
        todo=[i];ids=[]
        while todo:
            j=todo.pop()
            if j in seen:continue
            seen.add(j);ids.append(j);todo.extend(k for k,z in enumerate(G[j])if z and k not in seen)
        ids.sort();require(1<=len(ids)<=2,'exact sparse Gram components at most two')
        a=Q(G[ids[0]][ids[0]])*factors[ids[0]]**2;require(a>0,'positive Gram diagonal')
        if len(ids)==1:
            lower=a;det=a;trace0=a
        else:
            j,k=ids;b=Q(G[j][k])*factors[j]*factors[k];c0=Q(G[k][k])*factors[k]**2
            det=a*c0-b*b;trace0=a+c0
            require(c0>0 and det>0,'positive exact two-by-two determinant')
            lower=det/trace0
        lowers.append(lower)
        blocks.append({'indices':ids,'determinant':str(det),'trace':str(trace0),
                       'minimum_eigenvalue_lower':str(lower)})
    delta=min(lowers);h=delta/4
    upper=max(sum(abs(Q(z)*factors[i]*factors[j])for j,z in enumerate(row))for i,row in enumerate(raw))
    require(upper>0 and h>0,'strict universal spectral bounds')
    return {'complete':True,'dimension':n,'blocks':blocks,
            'component_sizes':{str(k):sum(len(b['indices'])==k for b in blocks)for k in(1,2)},
            'robust_Gram_minimum_eigenvalue_lower':str(delta),
            'Hermitian_HS_squared_lower_coefficient_h':str(h),
            'raw_HS_squared_upper_coefficient_U':str(upper),
            'spectral_Hermitian_raw_ratio_squared_lower':str((1+delta/upper)/4),
            'coordinate_norm':'Euclidean arithmetic norm on the72 native realified basis coefficients; no physical bosonic norm is installed.',
            'bounds':'For real field coordinates x and real lambda in order0,1,2,3: h ||x||^2 ||lambda||^2 <= ||Herm Bspec||_HS^2; ||Bspec||_HS^2 <= U ||x||^2 ||lambda||^2.',
            'claim':'For a nonzero realified carrier field and nonzero real lambda, the complete spectral output survives every held cross-Gram defect norm<1/2. Total normalized affine output still requires its constant term or the separately proved sufficiently-small-tube argument.',
            'method':'Exact positive diagonal/determinant controls on every component; no floating eigenvalue is used for certification.'}


def stage_certify(args):
    data=json.loads((args.cache/'selected-spectral.json').read_text())
    require(data['complete']and data['bindings']==binding(args),'spectral input binding')
    result=spectral_certificate(data)
    result.update({'spectral_sha256':digest(args.cache/'selected-spectral.json'),
                   'execution_probe_sha256':digest(__file__)})
    write(args.cache/'selected-spectral-certificate.json',result)
    print('SELECTED EXACT SPECTRAL PD',result['component_sizes'],'h',result['Hermitian_HS_squared_lower_coefficient_h'],
          'U',result['raw_HS_squared_upper_coefficient_U'],flush=True)


RECORDS=('selected-prepare.json','selected-outputs.json','selected-spectral.json',
         'selected-spectral-certificate.json','selected-dense-producer.txt','selected-spectral-producer.txt')
BUNDLE='lab/process/source-action-selected-jet-certificates.json'


def definition_text(source,name):
    import ast
    tree=ast.parse(source)
    nodes=[node for node in tree.body if isinstance(node,ast.FunctionDef)and node.name==name]
    require(len(nodes)==1,'unique production function '+name)
    return ast.get_source_segment(source,nodes[0])


def custody(args,data,texts):
    prepare,outputs,spectral=data['selected-prepare.json'],data['selected-outputs.json'],data['selected-spectral.json']
    dense=texts['selected-dense-producer.txt'];spec=texts['selected-spectral-producer.txt']
    dh=hashlib.sha256(dense.encode()).hexdigest();sh=hashlib.sha256(spec.encode()).hexdigest()
    require(prepare['execution_probe_sha256']==outputs['execution_probe_sha256']==dh,'original dense producer bytes')
    require(spectral['execution_probe_sha256']==sh,'original spectral producer bytes')
    live=Path(__file__).read_text()
    common=('binding','records','field_errors','scale_errors','error_record','read_errors','matrix_record',
            'read_matrix','solve_low','stage_prepare','hs_inner','output_stats','stage_outputs')
    for name in common:require(definition_text(dense,name)==definition_text(live,name),'unchanged dense procedure '+name)
    for name in('modular_rank','integer_operator','real_trace','integer_hs','stage_spectral'):
        require(definition_text(spec,name)==definition_text(live,name),'unchanged spectral procedure '+name)
    require(prepare['bindings']==spectral['bindings']==outputs['bindings']['inputs']==binding(args),'current native inputs')
    require(outputs['bindings']['prepare_sha256']==jd_bytes(args,data,'selected-prepare.json'),'prepared raw-record binding')
    require(not outputs['complete']and len(outputs['columns'])==2,'dense production remains partial2/40')
    require(prepare['complete']and len(prepare['roots'])==2 and all(len(r['columns'])==20 for r in prepare['roots']),
            'both-root complete leading graph reconstruction')
    return {'dense_producer_sha256':dh,'spectral_producer_sha256':sh,'unchanged_production_functions':len(common)+5,
            'matched_dense_outputs':2,'planned_dense_outputs':40,'dense_status':'PARTIAL',
            'graph_columns_both_roots':40,'spectral_complete_complex_basis':36}


def jd_bytes(args,data,name):
    # During fresh unpack the authenticated original byte representation is retained.
    return digest(args.cache/name)


def stage_bundle(args):
    data={name:json.loads((args.cache/name).read_text())for name in RECORDS if name.endswith('.json')}
    texts={name:(args.cache/name).read_text()for name in RECORDS if name.endswith('.txt')}
    control=custody(args,data,texts)
    proof=data['selected-spectral-certificate.json'];expected=spectral_certificate(data['selected-spectral.json'])
    require(all(proof[k]==v for k,v in expected.items()),'exact spectral certificate replay')
    records0={}
    for name in RECORDS:
        raw=(args.cache/name).read_bytes()
        records0[name]={'encoding':'zlib-base64-utf8'if name.endswith('.txt')else'zlib-base64-json',
                        'sha256':hashlib.sha256(raw).hexdigest(),'uncompressed_bytes':len(raw),
                        'data':base64.b64encode(zlib.compress(raw,9)).decode()}
    out={'schema':'gu-selected-jet-certificate-v1','data_only':True,'final_probe_sha256':digest(__file__),
         'native_inputs':binding(args),'custody':control,'records':records0,
         'scope':'Complete native spectral map and exact real robust-Gram positivity; both-root graph reconstruction; only2/40 dense matched affine outputs. Source snapshots are inert custody data and are never executed by verification. No full affine normalized-visibility or coherent-packet computation is claimed.'}
    write(args.repo/BUNDLE,out);print('SELECTED BUNDLE',digest(args.repo/BUNDLE),'bytes',(args.repo/BUNDLE).stat().st_size,flush=True)


def unpack(args):
    bundle=json.loads((args.repo/BUNDLE).read_text());require(bundle['final_probe_sha256']==digest(__file__),'final probe hash')
    require(bundle['native_inputs']==binding(args),'bundle native bindings')
    require(set(bundle['records'])==set(RECORDS),'exact record whitelist')
    data={};texts={}
    for name,record in bundle['records'].items():
        raw=zlib.decompress(base64.b64decode(record['data'],validate=True))
        require(len(raw)==record['uncompressed_bytes']and hashlib.sha256(raw).hexdigest()==record['sha256'],'record bytes '+name)
        path=args.cache/name
        if path.exists():require(path.read_bytes()==raw,'fresh cache conflict '+name)
        else:path.write_bytes(raw)
        if name.endswith('.json'):data[name]=json.loads(raw)
        else:texts[name]=raw.decode()
    return bundle,data,texts


def verify_spectral_native(args,data):
    gd,_=s.owned_records(args,'source-action-scalar-normal-operator-certificates.json',['scalar-geometry.json'])
    basis=[s.decode(SimpleNamespace(C=C),row)for row in gd['scalar-geometry.json']['basis']]
    maps=[];real8=[];labels=[];controls=0
    from source_action_slice_completion_probe import slash
    for j,u in enumerate(basis):
        require(set(e for e,cl in u)<={32,256},'only5/8 support')
        require(not p.contraction(p.components(u),range(14))and not o.receiver(SimpleNamespace(C=C),u),'native seed blindness')
        for part,sign in(('a',1),('b',-1)):
            ur={k:Q(sign*getattr(z,part))for k,z in u.items()if getattr(z,part)}
            require(not p.contraction(p.components(ur),range(14)),'realified gamma trace')
            real8.append({cl:z for(e,cl),z in ur.items()if e==256})
        jets=[]
        for axis in range(4):
            actual=p.jet(u,axis);expected={};u8=p.components(u)[8];clambda=slash(p.covector(axis))
            for col in range(5):
                z,nu=p.inject(col);t=add(nu,scale(-1,p.contraction(z,range(4))))
                T8=add(p.mul(u8,nu),*(scale(-1/p.g.d[h],p.mul(p.gamma(h),p.mul(u8,z[h])))for h in range(4)))
                v3=scale(-2*I,p.mul(u8,p.mul(clambda,t)))
                vs=scale(2*I,p.mul(p.gamma(3),add(p.mul(clambda,T8),p.mul(u8,p.mul(clambda,t)))))
                expected.update({(3,col,cl):v for cl,v in v3.items()});expected.update({(4,col,cl):v for cl,v in vs.items()})
                controls+=1
            require(actual==expected,'720 native output formula controls');jets.append(actual)
        for part,label in(('b','Re_field'),('a','minus_Im_field')):
            for axis,B in enumerate(jets):
                realmap={k:I*getattr(z,part)for k,z in B.items()if getattr(z,part)}
                integer,factor=integer_operator(realmap);maps.append(integer)
                labels.append({'basis':j,'part':label,'axis':axis,'positive_scale':str(factor)})
    require(labels==data['affine_spectral_labels'],'spectral coordinate scales')
    require([[[i,j,cl,a,b]for(i,j,cl),(a,b)in sorted(B.items())]for B in maps]==data['integer_spectral_maps'],
            'complete spectral native maps replay')
    require(modular_rank(real8)==data['realified_u8_rank'],'realified native rank replay')
    for i,A in enumerate(maps):
        for j in range(i,len(maps)):
            require(integer_hs(A,maps[j])==data['raw_HS_Gram'][i][j]and
                    real_trace(A,maps[j])==data['real_trace_pairing_matrix'][i][j],
                    'full actual real trace and HS pairings')
    return {'direct_native_five_slot_checks':controls,'spectral_operators':len(maps),'realified_u8_rank':72,
            'exact_Gram_entries_recomputed':len(maps)**2}


def stage_verify(args):
    tick=time.monotonic();bundle,data,texts=unpack(args);receipt=custody(args,data,texts)
    proof=spectral_certificate(data['selected-spectral.json'])
    require(all(data['selected-spectral-certificate.json'][k]==v for k,v in proof.items()),'exact PD block certificate')
    receipt.update(verify_spectral_native(args,data['selected-spectral.json']))
    # Reconstruct the complete40 graph columns in a dedicated child, not the expensive dense current outputs.
    child=SimpleNamespace(**vars(args));child.cache=args.cache/'graph-reconstruction';child.cache.mkdir(exist_ok=True)
    stage_prepare(child);rebuilt=json.loads((child.cache/'selected-prepare.json').read_text())
    original=data['selected-prepare.json']
    ignore={'execution_probe_sha256','seconds'}
    require({k:v for k,v in rebuilt.items()if k not in ignore}=={k:v for k,v in original.items()if k not in ignore},
            'complete graph/current-derivative reconstruction replay')
    receipt.update({'passed':True,'probe_sha256':digest(__file__),'bundle_sha256':digest(args.repo/BUNDLE),
                    'seconds':time.monotonic()-tick,'dense_matched_outputs_authenticated_not_recomputed':2,
                    'spectral_robust_Gram_positive':True,'graph_columns_reconstructed':40,
                    'scope':'All36 native spectral maps, full real Gram and exact positivity, full both-root graph fields and errors replayed; dense2-column current evaluations authenticated. Physical normalized-band interpretation remains a written conditional theorem.'})
    write(args.cache/'selected-verify.json',receipt);print('SELECTED VERIFY PASS',json.dumps(receipt,sort_keys=True),flush=True)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,default=ROOT);ap.add_argument('--cache',type=Path,required=True)
    ap.add_argument('--mode',choices=['prepare','outputs','spectral','certify','bundle','verify','unpack'])
    ap.add_argument('--verify',action='store_true',help='Alias for --mode verify; uses an empty or matching cache.')
    ap.add_argument('--steps',type=int,default=0);ap.add_argument('--root-index',type=int,choices=[0,1])
    ap.add_argument('--columns',type=int,nargs='*')
    args=ap.parse_args();require(not(args.verify and args.mode),'choose --verify or --mode')
    args.mode='verify'if args.verify else args.mode;require(args.mode is not None,'a mode is required')
    args.repo=args.repo.resolve();args.cache.mkdir(parents=True,exist_ok=True)
    {'prepare':stage_prepare,'outputs':stage_outputs,'spectral':stage_spectral,'certify':stage_certify,
     'bundle':stage_bundle,'verify':stage_verify,'unpack':unpack}[args.mode](args)


if __name__=='__main__':main()
