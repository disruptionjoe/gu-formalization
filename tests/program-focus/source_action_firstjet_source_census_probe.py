#!/usr/bin/env python3
"""Exact actual-connection first-jet source census, no new inverse.

Membership includes the owned conjugate SO3 orbit, checked with the exact
halfturn-conjugation map on every E4/E5 basis vector. It creates no new
M-generated receiver. Nonmembership is not a cokernel obstruction.
Root schedules every native run. --limit permits bounded source batches.
"""
from pathlib import Path
from fractions import Fraction as Q
from types import SimpleNamespace
import argparse, hashlib, json, sys, time
sys.dont_write_bytecode=True


def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,obj):
    q=p.with_suffix(p.suffix+'.new');q.write_text(json.dumps(obj,indent=2));q.replace(p)
def matadd(A,B,factor=1):return [[a+factor*b for a,b in zip(ar,br)]for ar,br in zip(A,B)]
def mm(A,B):
    out=[[Q(0)for _ in B[0]]for _ in A]
    for i,row in enumerate(A):
        for j,a in enumerate(row):
            if a:
                for k,b in enumerate(B[j]):
                    if b:out[i][k]+=a*b
    return out

def initialize(args):
    global p,g,C,I,add,scale,Engine
    sys.path.insert(0,str(args.repo/'tests/program-focus'))
    import source_action_spin4_compatibility_probe as p
    import source_action_deep_geometry as g
    from source_action_paired_response_probe import C,I
    from source_action_deep_algebra import add,scale,Engine
    p.load(SimpleNamespace(root=args.repo,cache=args.e4))


def setup(args):
    initialize(args)
    s=p.context(SimpleNamespace(root=args.repo,cache=args.e4),False)
    integer=p.IntegerScaledN(g);proj=p.IntegerKernelProjection(s.q,integer)
    return s,proj


def isotropy(H):return [[g.h_action(H,j).get(i,Q(0))for j in range(14)]for i in range(14)]
def rotation(i,j):
    H=g.zero();H[i][j]=Q(1);H[j][i]=Q(-1);return H

def connection_matrices():
    matrices=[];adapt=[]
    for a in range(14):
        H=g.zero()
        if a>=4:
            S=g.A[a-4]
            for i in range(3):H[i][3]=H[3][i]=-S[3][i]
            assert [S[3][i]+H[3][i]for i in range(3)]==[0,0,0]
        adapt.append(H)
        matrices.append(matadd(g.L[a],isotropy(H)))
    return matrices,adapt


def rho_operator(s,A):
    """Connection on T*Y tensor End(S): -A^T on form leg, spin commutator."""
    sp={(1<<a)|(1<<b):A[a][b]/(2*g.d[b])for a in range(14)for b in range(a+1,14)if A[a][b]}
    def rho(v):
        out={}
        for(e,c),x in v.items():
            a=e.bit_length()-1
            for b in range(14):
                z=-A[a][b]
                if z:out[1<<b,c]=out.get((1<<b,c),0)+x*z
            for cc,z in s.E.cliff_product(sp,{c:Q(1)},'comm').items():
                out[e,cc]=out.get((e,cc),0)+x*z
        return {k:z for k,z in out.items()if z}
    return rho,sp


def geometry(s,matrices,adapt,repo):
    assert all(not any(g.Lambda[a][i])for a in range(4,14)for i in range(14))
    for x in range(4):
        for a in range(4,14):
            assert [g.L[x][k][a]for k in range(4)]==[-g.A[a-4][k][x]for k in range(4)]
            assert all(not g.L[x][k][a]for k in range(4,14))
        for v in range(4):
            assert all(not g.L[x][k][v]for k in range(4))
            for a in range(4,14):assert g.L[x][a][v]==g.eta[v]*g.A[a-4][v][x]/g.d[a]
    nonzero=[a for a,A in enumerate(matrices)if any(any(row)for row in A)]
    assert nonzero==[0,1,2,3,10,12,13]
    rotations=[isotropy(rotation(i,j))for i,j in((0,1),(0,2),(1,2))]
    checks=0
    for J in rotations:
        for a,A in enumerate(matrices):
            lhs=matadd(mm(J,A),mm(A,J),-1)
            rhs=[[Q(0)for _ in range(14)]for _ in range(14)]
            for b,z in enumerate([J[b][a]for b in range(14)]):
                if z:rhs=matadd(rhs,matrices[b],z)
            assert lhs==rhs,('connection_isotropy_failure',a);checks+=1
    spin_by_axis={3:0,4:0,7:0,0:1,1:1,2:1,10:1,12:1,13:1,5:2,6:2,8:2,9:2,11:2}
    Cas=[[Q(0)for _ in range(14)]for _ in range(14)]
    for J in rotations:Cas=matadd(Cas,mm(J,J),-1)
    assert all(Cas[i][a]==(spin_by_axis[a]*(spin_by_axis[a]+1)if i==a else 0)for a in range(14)for i in range(14))
    for a in nonzero:
        A=matrices[a];rho,sp=rho_operator(s,A)
        assert all(g.d[i]*A[i][j]+g.d[j]*A[j][i]==0 for i in range(14)for j in range(14))
        for j in range(14):
            assert s.E.cliff_product(sp,{1<<j:Q(1)},'comm')=={1<<i:A[i][j]for i in range(14)if A[i][j]}
    # Residual halfturn about spatialaxis0: derive normal signs from Sym2H.
    h=[1,-1,-1,1];signs=h[:]
    for A in g.A:
        image=[[h[i]*A[i][j]*h[j]for j in range(4)]for i in range(4)]
        sign=next(t for t in(1,-1)if image==[[t*x for x in row]for row in A]);signs.append(sign)
    def halfturn(v):
        return {(e,c):z*((-1)**sum(1 for a,sgn in enumerate(signs)if sgn==-1 and (((e>>a)&1)^((c>>a)&1))))for(e,c),z in v.items()}
    D=json.loads((repo/'lab/process/source-action-deep-coefficients.json').read_text())
    for row in D['basis']:
        T={(e,c):Q(z)for e,c,z in row};assert halfturn(T)==T
    return {'normal_Nomizu_zero':True,'horizontal_HN_mixing_formula':True,'canonical_adapted_nonzero_axes':nonzero,'SO3_connection_matrix_intertwining_checks':checks,'tangent_decomposition':'3V0+2V1+V2','no_normal_spin2_connection_component':True,'full_oneform_plus_End_action':True,'halfturn_signs':signs,'all59_backgrounds_halfturn_fixed':True},halfturn


def receiver(args,j,halfturn):
    cache=args.e4 if j==4 else args.e5
    owner=json.loads((args.repo/'lab/process'/('source-action-spin4-certificates.json'if j==4 else 'source-action-weak-response.json')).read_text())
    records=owner['records']if j==4 else owner['reproduction']['records']
    bp=cache/'inverse-stage3-basis.json';cp=cache/('spin4-fast-certificate.json'if j==4 else 'inverse-stage5-certificate.json')
    assert digest(bp)==records[bp.name]['sha256'];assert digest(cp)==records[cp.name]['sha256']
    bd=json.loads(bp.read_text());cert=json.loads(cp.read_text())
    assert len(cert['roots'])==2 and all(r['invertible_on_block_over_rootball']and Q(r['neumann_bound'])<1 for r in cert['roots'])
    bs=[{(e,c):C(Q(a),Q(b))for e,c,(a,b)in row}for row in bd['basis']]
    ps=[tuple(x)for x in bd['basis_pivots']]
    assert len(bs)==len(ps)==(282 if j==4 else 120)
    for i,(pp,b)in enumerate(zip(ps,bs)):
        assert b.get(pp,C())==C(1) and all(not b.get(p0,C())for p0 in ps[:i])
    def reduce(v):
        co=[];v=dict(v)
        for pp,b in zip(ps,bs):
            z=C(v.get(pp,0));co.append(z)
            if z:v=add(v,scale(-z,b))
        return v,co
    initial=len(bs)
    for b in list(bs):
        theta=halfturn({k:C(z).conj()for k,z in b.items()})
        rem,_=reduce(theta)
        if rem:
            pp=min(rem);bs.append(scale(1/rem[pp],rem));ps.append(pp)
    return SimpleNamespace(basis=bs,pivots=ps,reduce=reduce,initial=initial,dimension=len(bs),bindings={'basis_sha256':digest(bp),'inverse_certificate_sha256':digest(cp)})


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


def run(args):
    tick=time.monotonic();s,P=setup(args);K=s.q['K']
    matrices,adapt=connection_matrices();geom,halfturn=geometry(s,matrices,adapt,args.repo)
    R=lambda v:add(v,scale(-1,P(v)))
    raise_=lambda v:add(s.rot(0,2,v),scale(I,s.rot(1,2,v)))
    lower=lambda v:add(s.rot(0,2,v),scale(-I,s.rot(1,2,v)))
    part=s.part
    rho=[rho_operator(s,A)[0]for A in matrices]
    rec={j:receiver(args,j,halfturn)for j in(4,5)}
    data=json.loads((args.repo/'lab/process/source-action-deep-coefficients.json').read_text())
    labels=xor_basis([8]+[e^c for row in data['basis']for e,c,z in row])
    assert len(labels)==11
    out={'scope':'Exact actual LC/adapted-frame first-jet sources from two owned Q7 modules; no new inverse, full-R theorem or physical/source verdict.',
         'geometry':geom,'receiver_mode':'owned_real_SO3_orbits','highest_reality_checks':{str(j):{'vectors_tested':rec[j].initial,'added_directions':rec[j].dimension-rec[j].initial}for j in rec},
         'receiver_dimensions':{str(j):rec[j].dimension for j in rec},
         'bindings':{'probe_sha256':digest(__file__),'native_spin4_probe_sha256':digest(args.repo/'tests/program-focus/source_action_spin4_compatibility_probe.py'),
                     'native_inputs':p.w.native_bindings(args.repo)|{'tests/program-focus/source_action_weak_response_probe.py':digest(args.repo/'tests/program-focus/source_action_weak_response_probe.py')},
                     'background_sha256':digest(args.repo/'lab/process/source-action-deep-coefficients.json'),'receivers':{str(j):rec[j].bindings for j in rec}},
         'expected_reduced_channels':{'spin4':4,'spin5':18,'pointwise_Q_controls':2},'sources':[],'complete':False}
    write(args.output,out)
    fields={};sourcecache={};uncovered={4:[],5:[]}
    def getfields(index,family):
        key=index,family
        if key in fields:return fields[key]
        V=K(3,s.bs[index]);assert not P(V) and s.q['cas'](V)==scale(56,V)
        if family=='time':
            W7=R(rho[3](V));assert s.q['cas'](W7)==scale(56,W7) and not raise_(W7)
            assert s.rot(0,1,W7)==scale(7*I,W7)
            fields[key]={'V':V,'W7':W7};return fields[key]
        a0,a1,a2=(0,1,2)if family=='horizontal'else(10,12,13)
        raw=R(rho[a0](V));W6=part(raw,6,[6,7]);W7=R(rho[a2](V))
        assert raw==add(W6,part(raw,7,[6,7]))
        assert s.q['cas'](W6)==scale(42,W6) and not raise_(W6)
        assert s.rot(0,1,W6)==scale(6*I,W6)
        assert s.q['cas'](W7)==scale(56,W7) and not raise_(W7)
        assert s.rot(0,1,W7)==scale(7*I,W7)
        assert R(rho[a1](V))==scale(I,raw)
        assert raise_(raw)==scale(-1,W7)
        assert part(raw,7,[6,7])==scale(Q(1,14),lower(W7))
        fields[key]={'V':V,'W6':W6,'W7':W7};return fields[key]
    def image(index,family,intermediate,b):
        key=index,family,intermediate,b
        if key not in sourcecache:
            F=getfields(index,family)
            sourcecache[key]=P(K(b,F[intermediate]))
        return sourcecache[key]
    # Horizontal spin4 is first: the shortest genuinely missing check.
    cases=[]
    for family in('horizontal','normal'):
        for index in(5,12):cases.append((index,family,'W6',5,4,'K2_W6_to4'))
    for index in(5,12):
        for family in('horizontal','normal'):
            cases.extend([(index,family,'W6',0,5,'K1_horizontal_W6_to5'),(index,family,'W6',10,5,'K1_normal_W6_to5'),(index,family,'W6',9,5,'K2_W6_to5'),(index,family,'W7',5,5,'K2_W7_to5')])
        cases.append((index,'time','W7',5,5,'K2_time_W7_to5'))
    for index in(5,12):cases.append((index,'pointwise','V',5,5,'pointwise_Q_principal'))
    for number,(index,family,intermediate,b,j,channel)in enumerate(cases):
        if args.limit and number>=args.limit:break
        if family=='pointwise':
            V=K(3,s.bs[index]);L=P(K(b,V));src=part(L,5,[5,6,7])
        else:
            L=image(index,family,intermediate,b)
            spins=[4,5,6,7]if intermediate=='W6'and b in(5,9)else[5,6,7]
            src=part(L,j,spins)
        checks={}
        if intermediate=='W6'and b==5:
            W6=getfields(index,family)['W6']
            assert P(K(8,W6))==scale(I,L);checks['full_axis8_equals_i_axis5']=True
        if intermediate=='W6'and b==9:
            L5=image(index,family,intermediate,5);low=part(L5,5,[4,5,6,7])
            assert s.rot(0,1,low)==scale(4*I,low)
            assert raise_(low)==scale(-2,src)
            assert lower(raise_(low))==scale(-10,low)
            assert low==scale(Q(1,5),lower(src))
            checks.update({'K5_spin5_weight':4,'raise_K5_to_K9_factor':'-2','lower_raise_factor':'-10','K5_from_lower_K9_factor':'1/5'})
        assert P(src)==src and not K(3,src)
        assert s.q['cas'](src)==scale(j*(j+1),src)
        assert s.rot(0,1,src)==scale(j*I,src)and not raise_(src)
        rem,co=rec[j].reduce(src)
        support=set().union(*(set(v)for v in rec[j].basis))
        row={'index':number,'Q7_basis_index':index,'connection_family':family,'intermediate':intermediate,'principal_axis':b,'target_spin':j,'channel':channel,
             'source_terms':len(src),'zero':not bool(src),'inside_receiver':not bool(rem),'source_cosets':sorted({coset(e^c,labels)for e,c in src}),
             'source_outside_receiver_coordinate_support':len(set(src)-support),'remainder_terms':len(rem),'remainder_cosets':sorted({coset(e^c,labels)for e,c in rem}),
             'source':s.q['ser'](src),'coordinates':[[i,*C(z).ser()]for i,z in enumerate(co)if z],
             'remainder_witness':s.q['ser'](rem)[:12],'controls':checks}
        if rem:uncovered[j].append((number,rem))
        out['sources'].append(row);out['completed']=len(out['sources']);out['seconds']=time.monotonic()-tick
        write(args.output,out)
        print('FIRSTJET',number,index,family,channel,'terms',len(src),'inside',not bool(rem),'cosets',row['source_cosets'],'outside-support',row['source_outside_receiver_coordinate_support'],'seconds',out['seconds'],flush=True)
    out['quotient_source_spans']={str(j):span_summary(uncovered[j],s.q['ser'])for j in(4,5)}
    out['complete']=len(out['sources'])==len(cases)
    out['all_reduced_sources_covered']=out['complete']and all(r['inside_receiver']for r in out['sources'])
    out['uncovered_channels']=[{k:r[k]for k in('Q7_basis_index','connection_family','channel','target_spin','source_cosets','remainder_terms')}for r in out['sources']if not r['inside_receiver']]
    write(args.output,out);return out


def span_summary(vectors,ser):
    """Exact Q(i) dependence only; no native operator or module growth."""
    basis=[];pivots=[];owners=[];records=[]
    for case,original in vectors:
        v=dict(original);co=[]
        for pp,b in zip(pivots,basis):
            z=C(v.get(pp,0));co.append(z)
            if z:v=add(v,scale(-z,b))
        if v:
            pp=min(v);z=v[pp];pivots.append(pp);basis.append(scale(1/z,v));owners.append(case);co.append(z)
        assert original==add(*(scale(z,b)for z,b in zip(co,basis)if z))
        records.append({'case':case,'coordinates':[[i,*C(z).ser()]for i,z in enumerate(co)if z]})
    return {'field':'Q(i)','input_vectors':len(vectors),'rank':len(basis),
            'independent_case_indices':owners,'relations':records,
            'echelon_basis':[ser(b)for b in basis],
            'scope':'Span of actual uncovered source vectors modulo the already-owned receivers; no M closure or kernel claim.'}


def controls(args):
    initialize(args);matrices,adapt=connection_matrices()
    geo,halfturn=geometry(SimpleNamespace(E=Engine(g)),matrices,adapt,args.repo)
    receivers={j:receiver(args,j,halfturn)for j in(4,5)}
    return {'scope':'Native geometry, family equivariance, owned inverse provenance and highest reality closure; actual source/ladder checks are in census mode.',
            'geometry':geo,'highest_reality_checks':{str(j):{'vectors_tested':r.initial,'added_directions':r.dimension-r.initial}for j,r in receivers.items()},
            'bindings':{'probe_sha256':digest(__file__),'native_inputs':p.w.native_bindings(args.repo)|{'tests/program-focus/source_action_weak_response_probe.py':digest(args.repo/'tests/program-focus/source_action_weak_response_probe.py'),'tests/program-focus/source_action_spin4_compatibility_probe.py':digest(args.repo/'tests/program-focus/source_action_spin4_compatibility_probe.py')},'receivers':{str(j):r.bindings for j,r in receivers.items()}}}


def status(report):
    return {'scope':report.get('scope'),'complete':report.get('complete',False),
            'completed':report.get('completed',0),'all_reduced_sources_covered':report.get('all_reduced_sources_covered',False),
            'uncovered_count':len(report.get('uncovered_channels',[])),
            'uncovered_ranks':{j:v['rank']for j,v in report.get('quotient_source_spans',{}).items()},
            'evidence_probe_sha256':report.get('bindings',{}).get('probe_sha256'),
            'current_probe_sha256':digest(__file__)}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',required=True,type=Path)
    ap.add_argument('--cache',type=Path,help='Default outputs and unpacked e4/e5 folders live here.')
    ap.add_argument('--e4',type=Path);ap.add_argument('--e5',type=Path)
    ap.add_argument('--output',type=Path);ap.add_argument('--evidence',type=Path)
    ap.add_argument('--limit',type=int,default=0)
    ap.add_argument('--mode',choices=['census','controls','replay','status'],default='census')
    args=ap.parse_args();args.repo=args.repo.resolve()
    args.cache=(args.cache or args.repo/'_local/firstjet-census').resolve()
    args.e4=(args.e4 or args.cache/'e4').resolve();args.e5=(args.e5 or args.cache/'e5').resolve()
    names={'census':'firstjet-census.json','controls':'firstjet-controls.json','replay':'firstjet-replay.json','status':'firstjet-status.json'}
    args.output=(args.output or args.cache/names[args.mode]).resolve()
    assert args.limit>=0
    if args.mode=='status':
        evidence=args.evidence or args.cache/'firstjet-census.json'
        print(json.dumps(status(json.loads(evidence.read_text())),indent=2));return
    args.output.parent.mkdir(parents=True,exist_ok=True)
    if args.mode=='controls':
        result=controls(args);write(args.output,result);print(json.dumps(result,indent=2));return
    expected=None
    if args.mode=='replay':
        assert args.limit==0,'Replay must complete all24 cases'
        evidence=(args.evidence or args.cache/'firstjet-census.json').resolve()
        assert evidence!=args.output,'Replay must not overwrite the evidence it checks'
        expected=json.loads(evidence.read_text());assert expected['complete']
    result=run(args)
    if expected is not None:
        keys=('geometry','receiver_mode','highest_reality_checks','receiver_dimensions','expected_reduced_channels','sources','quotient_source_spans','complete','all_reduced_sources_covered','uncovered_channels')
        assert all(result[k]==expected[k]for k in keys),'Exact census replay mismatch'
        assert result['bindings']==expected['bindings'],'Replay code/input bindings differ'
        result['replay']={'all_exact_records_match':True,'evidence_sha256':digest(evidence)};write(args.output,result)
    print(json.dumps(status(result),indent=2))

if __name__=='__main__':main()
