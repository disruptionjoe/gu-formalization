"""Exact complete P0 graph first-jet test. One serialized worker; numpy/sympy/python-flint.
Default replays stored evidence; --write intentionally produces it.
"""
from pathlib import Path
import sys,json,argparse,time,hashlib
from fractions import Fraction as F
import numpy as np
import sympy as s
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'tests/channel-swings'))
import k2134_noncircle_current_transport_probe as b
q=b.q;n=b.n
from flint import fmpq_mat,nmod_mat

def targets(fault=None):
    cs,m,S,t,z,r,Q,E,Y,_,_,_=b.nf.frame(c=1,sh=0)
    Ystar=n.adj(Y);P=q.add((F(1,2),q.mul(Y,Ystar)));Ip=q.add((1,q.I),(-1,P))
    def actual_tag(A):
        flips={i^j for i,j in A};assert len(flips)==1
        f=flips.pop();a=A[0,f]
        h=sum(1<<j for j in range(7) if A[1<<j,(1<<j)^f]==-a)
        assert all(A[i,i^f]==a*(-1)**((i&h).bit_count()) for i in range(128))
        return f,h
    tags=[actual_tag(A) for A in cs+[m,t,z]]
    commute=lambda a,c: ((a[0]&c[1]).bit_count()+(a[1]&c[0]).bit_count())%2==0
    candidates={(f,h) for f in range(128) for h in range(128) if all(commute((f,h),g) for g in tags)}
    assert len(candidates)==256
    tf,th=tags[-2];zf,zh=tags[-1]
    stab=[(0,0),(tf,th),(zf,zh),(tf^zf,th^zh)]
    reps=sorted({min((f^sf,h^sh) for sf,sh in stab) for f,h in candidates});assert len(reps)==64
    base=[q.I]+cs;out=[];seen=set()
    # Exact graph coordinates: skew X=iH; arbitrary b,c=H or iH.
    for f,h in reps:
        phase=s.I if (f&h).bit_count()%2 and fault!='missing_hermitian_phase' else 1
        A={(i,i^f):phase*(-1)**((i&h).bit_count()) for i in range(128)}
        H=q.mul(E,A);assert H==n.adj(H) and q.mul(E,H)==H, 'Hermitian compressed basis'
        # Distinct stabilizer cosets give Hilbert-Schmidt orthogonal E compressions.
        key=tuple(sorted((ij,str(v)) for ij,v in H.items()));assert key not in seen;seen.add(key)
        frames=[('U',q.mul(r,q.add((s.I,H)))),('Br',q.mul(Q,H)),('Bi',q.mul(Q,q.add((s.I,H)))),('Cr',q.mul(r,q.mul(Q,H))),('Ci',q.mul(r,q.mul(Q,q.add((s.I,H)))))]
        for kind,dY in frames:
            normal=dY if fault=='omit_normal_projection' else q.mul(Ip,dY)
            assert q.mul(P,normal)=={}, 'normal tangent projection'
            # General graph tangent has d h=0 at this basepoint. The omitted
            # S-cross leakage term is skew, so the old P0 energy rows are valid.
            comp=q.mul(Ystar,q.mul(S,normal));assert q.add((1,comp),(1,n.adj(comp)))=={}
            for mu,C in enumerate(base):
                T=q.add((F(-1,4) if fault=='target_half_scale' else F(-1,2),q.mul(normal,q.mul(Ystar,C))))
                assert q.mul(T,Y)==q.add((-1,q.mul(normal,C))), 'target frame evaluation'
                Tn=q.mul(b.J[14],q.mul(T,b.Fi))
                # Same exact target normalization as K2134.
                rhs={}
                for (i,j),v in Tn.items():
                    vr=s.re(v)*176*b.den*b.den;vi=s.im(v)*176*b.den*b.den
                    assert vr==int(vr) and vi==int(vi)
                    if vr:rhs[30*128*128+i*128+j]=int(vr)
                    if vi:rhs[31*128*128+i*128+j]=int(vi)
                out.append(dict(label=[kind,f,h,mu],rhs=rhs))
    assert len(out)==1280
    return out

def outputs(mask,y,im,fault=None):
    X=b.mono(q.blade(tuple(k for k in range(14) if mask>>k&1)))
    AA=[(zz[0],q.ETA[k]*y[k]*zz[1]) for k in range(14) for zz in [b.mul(b.gs[k],X)]]
    Om=[(a[0],b.ws*a[1]) for a in AA]
    TT=[b.add([b.mul(b.mul(b.gs[c],AA[k]),b.js[c]) for c in range(14)]) for k in range(14)]
    out=[]
    for a in range(14):
        terms=[]
        for k in range(14):
            if k==a:continue
            u=TT[k][1]-b.mul(b.mul(b.gs[a],AA[k]),b.js[a])[1]-b.mul(b.mul(b.gs[k],AA[k]),b.js[k])[1]
            terms.append(b.mul(b.gs[k],(TT[k][0],u)))
        zz=b.mul(b.gs[a],b.add(terms));assert zz[0]==Om[a][0]
        out.append((zz[0],(0 if fault=='drop_shiab' else 4)*q.ETA[a]*zz[1]+(43 if fault=='omega_scale' else 44)*Om[a][1]))
    return out

def column(im,f,mask,y):
    outs=outputs(mask,y,im);M=outs[0];assert M[0]==f;blocks=[]
    assert max(int(np.max(np.abs(o[1]))) for o in outs)<2**30
    for a,o in enumerate(outs):
        dm=b.mul(b.ds[a],M);D=(o[0],44*o[1]-dm[1]);dr,di=b.rightP(b.dense(D));blocks += [dr,di] if not im else [-di,dr]
    # Preserve original row IDs but OMIT lower-return constraints entirely.
    blocks += [np.zeros((128,128),dtype=np.int64)]*2
    mr,mi=b.rightP(b.dense(M))
    lr=b.den*mr-b.mm(b.Pr,mr)+b.mm(b.Pi,mi);li=b.den*mi-b.mm(b.Pr,mi)-b.mm(b.Pi,mr)
    if im:lr,li=-li,lr
    blocks += [lr,li]
    ar=mr*b.gr[:,None];ai=mi*b.gr[:,None]
    er=b.mm(b.Pr.T,ar)+b.mm(b.Pi.T,ai);ei=b.mm(b.Pr.T,ai)-b.mm(b.Pi.T,ar)
    if im:er,ei=-ei,er
    blocks += [er+er.T,ei-ei.T]
    vec=np.concatenate([v.ravel() for v in blocks]);return {int(i):int(vec[i]) for i in np.flatnonzero(vec)}

def direct_original_check(label,fault=None):
    """Replay frozen raw gamma contraction, independently of outputs' TT grouping."""
    imag,ff,mask,yy=label
    X=q.blade(tuple(k for k in range(14) if mask>>k&1))
    om=[q.add((F(q.ETA[k]*yy[k],4),q.mul(q.add((3,q.I),(1,q.J)),q.mul(q.gamma(k),X)))) for k in range(14)]
    fast=outputs(mask,yy,imag,fault)
    for a in [0,3,7,13]:
        terms=[(1,q.mul(om[a],b.Jn[14]))]
        for k in range(14):
            if k==a:continue
            for c in range(14):
                if c not in [a,k]:terms.append((q.ETA[a],q.mul(q.blade((a,k,c)),q.mul(q.W,q.mul(om[k],b.Jn[c])))))
        direct=q.add(*terms);f,vals=fast[a]
        expected={(i,i^f):F(int(vals[i]),176) for i in range(128) if vals[i]}
        assert direct==expected,('direct original contraction',imag,ff,mask,a)
        assert f==ff^b.ds[a][0]
    return 4

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    start=time.time();ts=targets();sub=[0,1,62,63];cosets=sorted({min(f^h for h in sub) for f in range(128)})
    rec=json.loads((ROOT/'lab/process/k2028-all-grade-raw-common-form.json').read_text())
    for path,digest in rec['inputs'].items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,('stale inherited K2028 input',path)
    input_paths=['lab/process/k2028-all-grade-raw-common-form.json','lab/process/k1951-coordinated-zero-southeast-principal.json','lab/process/k1967-paired-raw-coefficient-observation.json','tests/channel-swings/k2134_noncircle_current_transport_probe.py','tests/channel-swings/k2132_conserving_positive_sector_classification_probe.py','tests/channel-swings/k2021_common_degree_dual_operator.py']
    inputs={path:hashlib.sha256((ROOT/path).read_bytes()).hexdigest() for path in input_paths}
    labels=[(im,g['flip'],mask,y) for im,br in [(False,rec),(True,rec['complex_hermitian_branch'])] for g in br['groups'] for mask,y in g['labels']]
    assert len(labels)==16620
    assert all(max(map(abs,y))<=16 for _,_,_,y in labels)
    def rowcoset(row):
        block,pos=divmod(row,128*128);f=pos//128 ^ pos%128
        # Upper block a has permutation shift f_raw xor shift((D0 J)_a J14^-1).
        # Real and imaginary rows share that shift. Leakage/current rows
        # live in core coordinates already, so require no output normalization.
        if block<28:f ^= b.ds[block//2][0]
        return min(f^h for h in sub)
    print('PREPARED',len(ts),'real target columns',len(labels),'raw columns',len(cosets),'cosets',time.time()-start,flush=True)
    from math import gcd
    constraints=[];summaries=[]
    direct_checks=0
    for c in cosets:
        for imag in [False,True]:
            label=next(v for v in labels if v[0]==imag and min(v[1]^h for h in sub)==c)
            direct_checks+=direct_original_check(label)
            assert all(rowcoset(row)==c for row in column(*label))
    print('DIRECT ORIGINAL CONTRACTIONS',direct_checks,'across all32 cosets',flush=True)

    for c in cosets:
        labs=[v for v in labels if min(v[1]^h for h in sub)==c]
        cols=[column(*v) for v in labs]
        assert all(rowcoset(row)==c for co in cols for row in co)
        tids=[i for i,t in enumerate(ts) if any(rowcoset(row)==c for row in t['rhs'])]
        tc=[{row:v for row,v in ts[i]['rhs'].items() if rowcoset(row)==c} for i in tids]
        allcols=cols+tc;rows=sorted(set().union(*(set(v) for v in allcols)));ridx={r:i for i,r in enumerate(rows)}
        arr=np.zeros((len(rows),len(allcols)),dtype=np.int64)
        for j,co in enumerate(allcols):
            for r,v in co.items():arr[ridx[r],j]=v
        unique={}
        for row in arr:
            vals=list(map(int,row));g=0
            for v in vals:g=gcd(g,v)
            if g:
                if next(v for v in vals if v)<0:g=-g
                unique[tuple(v//g for v in vals)]=None
        eq=list(unique);nr=len(cols)
        mat=fmpq_mat(eq);rr,rank=mat.rref();rankA=fmpq_mat([row[:nr] for row in eq]).rank()
        assert nmod_mat(eq,101).rank()==rank
        assert nmod_mat([row[:nr] for row in eq],101).rank()==rankA
        for i in range(rankA,rank):
            assert all(rr[i,j]==0 for j in range(nr))
            con={tids[j]:str(rr[i,nr+j]) for j in range(len(tids)) if rr[i,nr+j]};constraints.append(con)
        summaries.append(dict(coset=c,raw_columns=nr,targets=len(tids),rows=len(eq),rankA=rankA,rankAug=rank,equations_sha256=hashlib.sha256(json.dumps(eq,separators=(',',':')).encode()).hexdigest()))
        print('COSET',summaries[-1],time.time()-start,flush=True)
    final=fmpq_mat([[co.get(j,'0') for j in range(1280)] for co in constraints]);rr,rank=final.rref()
    final_modular_prime=None
    for prime in [101,103,107,109,113]:
        if any(F(v).denominator%prime==0 for co in constraints for v in co.values()):continue
        def modp(v):
            v=F(v);return v.numerator*pow(v.denominator,-1,prime)%prime
        if nmod_mat([[modp(co.get(j,'0')) for j in range(1280)] for co in constraints],prime).rank()==rank:
            final_modular_prime=prime;break
    assert final_modular_prime is not None
    piv=[next(j for j in range(1280) if rr[i,j]) for i in range(rank)];free=[j for j in range(1280) if j not in piv];ker=[]
    for j in free:
        vec={j:'1'}
        for i,k in enumerate(piv):
            if rr[i,j]:vec[k]=str(-rr[i,j])
        ker.append(vec)
    # Every fault changes an actual equation or input; the clean full computation precedes it.
    failures={}
    for fault in ['missing_hermitian_phase','omit_normal_projection','target_half_scale']:
        try:targets(fault)
        except AssertionError as ex:
            assert ex.args and ex.args[0] in ['Hermitian compressed basis','normal tangent projection','target frame evaluation'], ('unexpected fault crash',fault,str(ex))
            failures[fault]=str(ex)
        else:raise AssertionError(('FAULT NOT DETECTED',fault))
    for fault in ['drop_shiab','omega_scale']:
        try:direct_original_check(labels[0],fault)
        except AssertionError as ex:
            assert ex.args and isinstance(ex.args[0],tuple) and ex.args[0][0]=='direct original contraction', ('unexpected fault crash',fault,str(ex))
            failures[fault]=str(ex)
        else:raise AssertionError(('FAULT NOT DETECTED',fault))
    checks={'complete_native_tangent_basis':len(ts)==1280,'complete_raw_bank_size':len(labels)==16620,'original_contractions_all_cosets':direct_checks==256,'all_cosets_covered':len(summaries)==32,'exact_and_modular_ranks_agree':final_modular_prime is not None,'final_target_partition':rank+len(free)==1280}
    assert all(checks.values())
    result=dict(result_id='K2141',status='conditional_exact_controls',target_count=1280,raw_count=len(labels),obstruction_rank=rank,final_modular_prime=final_modular_prime,survivor_dimension=len(free),direct_original_contraction_checks=direct_checks,inputs=inputs,target_labels=[t['label'] for t in ts],systems=summaries,kernel=ker,exact_checks=checks,fault_failures=failures,probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Exact rational elimination plus independent finite-field ranks; native basis and first-jet transfer have independently reviewed written proof. K2028 common-H class completeness is inherited by digest, not newly re-exhausted.',scope='P0 all graph first jets; original upper class, no lower-return constraint; no global graph rigidity')
    path=ROOT/'lab/process/k2141-full-graph-raw-tangent.json'
    if args.write:path.write_text(json.dumps(result,indent=2)+'\n')
    else:assert json.loads(path.read_text())==result,'stored evidence mismatch'
    print('FINAL',rank,'survivors',len(free),'faults',len(failures),flush=True)
if __name__=='__main__':main()
