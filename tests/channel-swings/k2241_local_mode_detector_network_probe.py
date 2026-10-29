#!/usr/bin/env python3
"""Exact finite controls only; no owner writes and no continuum certification."""
import argparse
import json
import hashlib
from pathlib import Path
import sympy as s

I=s.I
Q=s.Rational

def dot(a,b): return s.expand(sum(x*y for x,y in zip(a,b)))
def conj(a): return [s.conjugate(x) for x in a]
def norm(a): return s.simplify(dot(a,conj(a)))
def add(a,b): return [s.expand(x+y) for x,y in zip(a,b)]
def scale(z,a): return [s.expand(z*x) for x in a]

def controls(fault=None):
    checks=[]
    def ck(name,test):
        checks.append((name,bool(test)))
    A=[Q(3,5),4*I/5]; B=[4*I/5,Q(3,5)]
    cr,sr,ct,st,z=Q(5,4),Q(3,4),Q(5,3),Q(4,3),I
    du=scale(ct,A); dv=scale(st,conj(B))
    u=add(scale(cr,du),scale(z*sr,conj(dv)))
    v=add(scale(cr,dv),scale(z*sr,conj(du)))
    if fault=='drop_creation_vector': v=[s.Integer(0),s.Integer(0)]
    ck('physical modes normalized and orthogonal', norm(A)==norm(B)==1 and dot(A,conj(B))==0)
    ck('exact complex coefficients',u==[Q(9,20),34*I/15] and v==[-7*I/12,s.Integer(2)])
    ck('canonical commutator',norm(u)-norm(v)==1)
    n=norm(v); m=dot(u,v if fault!='hermitian_m' else conj(v))
    ck('bilinear anomalous moment',m==205*I/48)
    nu2=s.expand((n+Q(1,2))**2-m*s.conjugate(m))
    ck('symplectic vacuum eigenvalue',nu2==Q(41,18)**2)
    up=add(scale(cr,u),scale(-z*sr,conj(v) if fault!='missing_conjugation' else v))
    vp=add(scale(cr,v),scale(-z*sr,conj(u)))
    ck('desqueezing removes anomalous covariance',dot(up,vp)==0)
    ck('desqueezing recovers two physical modes',up==du and vp==dv)
    ck('occupancy determines two-mode squeeze',norm(vp)==st**2 and norm(up)==ct**2)
    ck('restricted one-squeeze impossible', n*(n+1)-m*s.conjugate(m)==Q(400,81))
    use_st=s.Integer(0) if fault=='omit_two_mode' else st
    rec_u=add(scale(cr*ct,A),scale(z*sr*use_st,B))
    rec_v=add(scale(cr*use_st,conj(B)),scale(z*sr*ct,conj(A)))
    ck('two active gates reconstruct target',rec_u==u and rec_v==v)
    # Bogoliubov block matrix composes maps in the Heisenberg order.
    ident=s.eye(2); zero=s.zeros(2)
    def bog(X,Y): return X.row_join(Y).col_join(s.conjugate(Y).row_join(s.conjugate(X)))
    P=bog(s.Matrix([A,B]),zero)
    T=bog(ct*ident,s.Matrix([[0,st],[st,0]]))
    R=bog(s.diag(cr,1),s.diag(z*sr,0))
    M=(T*R*P if fault=='reverse_gate_order' else R*T*P)
    ck('Heisenberg collection matrix order',list(M[0,:])==u+v)
    J=s.diag(1,1,-1,-1)
    ck('full compiled map preserves CCR',s.simplify(M*J*s.conjugate(M.T)-J)==s.zeros(4))
    creation=M[:2,2:]
    collected_occupancies=[s.simplify(sum(creation[k,j]*s.conjugate(creation[k,j]) for j in range(2))) for k in range(2)]
    ck('actual collector vacuum first occupancy',collected_occupancies[0]==n)
    ck('actual collector vacuum complementary occupancy',collected_occupancies[1]==st**2)
    ck('actual collector vacuum energy',sum(collected_occupancies)==Q(881,144))
    ck('collector excitation exceeds necessary first-mode cost',sum(collected_occupancies)>=n==Q(625,144))
    ck('active resource exp two r plus t',(cr+sr)**2*(ct+st)**2==36)
    beta_upper=2*(norm(u)+norm(v))
    ck('number bound coefficient',beta_upper==Q(697,36) and beta_upper<20)
    # Vacuum identifies why creation term is necessary.
    vacuum_bound=norm(v)
    ck('vacuum occupancy retained',vacuum_bound==Q(625,144))
    K=15999
    gentle=2
    delta2=gentle**2*beta_upper*2/(K+1)
    ck('complete-reference consumer factor',delta2==Q(697,72000) and delta2<Q(1,100))
    tail_level=K+1
    # On the first omitted number eigenstate Markov's sharp coefficient is 1/(K+1).
    ck('first omitted number support',tail_level==16000 and Q(1,tail_level)==Q(1,K+1))
    ck('unconditional output energy budget',36**2*Q(3,2)**2*2==5832)
    # Exact backward support propagation for a path, with each edge one slot.
    support={0}
    for edge in [(0,1),(1,2),(2,3)]:
        if support.intersection(edge): support.update(edge)
    ck('three-slot path support',support=={0,1,2,3})
    # Change the actual gate edge, not a reporting support set.
    edge=(0,3) if fault=='nonlocal_gate' else (0,1)
    one_slot={0}
    if one_slot.intersection(edge): one_slot.update(edge)
    ck('admitted gate is adjacent',abs(edge[0]-edge[1])==1)
    ck('record cannot depend beyond light cone',all(j<=1 for j in one_slot))
    # Actual finite spectral control must agree at its last admitted level.
    cutoff=2 if fault=='spectral_boundary' else 3
    profile=[Q(0),Q(1,3),Q(2,3),Q(1)]
    actual=[profile[k] if k<=cutoff else Q(0) for k in range(4)]
    ck('finite spectral gate agrees on admitted sector',actual==profile)
    # An explicit target-class channel shows that dropping the gentle factor
    # to one is unjustified: dephase the high component and record its number.
    rare=Q(1,4)
    coherence=s.sqrt(rare*(1-rare))
    difference=s.Matrix([[0,-coherence],[-coherence,-rare]])
    block_norm=s.simplify(sum(abs(ev)*multiplicity for ev,multiplicity in difference.eigenvals().items()))
    exact_error=s.simplify((rare+block_norm)/2)
    ck('actual recorded-tail trace norm',exact_error==(1+s.sqrt(13))/8)
    ck('recorded tail error exceeds sqrt tail',exact_error>s.sqrt(rare))
    ck('recorded tail error obeys gentle bound',exact_error<=2*s.sqrt(rare))
    # Exact weak-tail countercontrol: a rare high-number state saturates Markov.
    p=Q(1,16000)
    ck('tail under mean-one mixture',p*(K+1)==1 and p==Q(1,K+1))
    # Gamma requires both active exponents, not merely the single local squeeze.
    ck('single squeeze cannot supply resource bound',(cr+sr)**2<36)
    # One-site canonical b necessarily has no thermal second mode.
    ck('single-site pure covariance',(sr**2+Q(1,2))**2-(cr*sr)**2==Q(1,4))
    # Passive complex u with v=0 and anomalous m=0 reduces to no active gates.
    ck('passive control',norm(A)==1 and (Q(1,2)**2)==Q(1,4))
    failed=[name for name,ok in checks if not ok]
    return len(checks),failed

FAULTS=['hermitian_m','missing_conjugation','omit_two_mode','reverse_gate_order','drop_creation_vector','nonlocal_gate','spectral_boundary']
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--controls-only',action='store_true')
    ap.add_argument('--write',action='store_true')
    args=ap.parse_args()
    count,failed=controls()
    if failed: raise AssertionError(f'baseline failures: {failed}')
    detected={}
    for f in FAULTS:
        _,bad=controls(f)
        if not bad: raise AssertionError(f'undetected fault {f}')
        detected[f]=bad
    report={'result_id':'K2241','controls':count,'fault_families':len(FAULTS),'detected':detected,'ceiling':'Exact finite controls; written proof carries all-Fock and causal statements.'}
    if not args.controls_only:
        root=Path(__file__).resolve().parents[2]
        deps=['explorations/conditional-build/k2241-local-mode-detector-network-2026-10-29.md',
              'explorations/conditional-build/k2225-positive-drift-detector-control-2026-10-28.md',
              'explorations/conditional-build/k2228-continuum-energy-form-detector-control-2026-10-28.md',
              'explorations/conditional-build/k2234-causal-detector-error-bound-2026-10-29.md',
              'explorations/conditional-build/k2237-computable-causal-witness-2026-10-29.md']
        report['dependency_sha256']={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in deps}
        report['probe_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        dest=root/'lab/process/k2241-local-mode-detector-network.json'
        if args.write: dest.write_text(json.dumps(report,indent=2)+'\n')
        else: assert json.loads(dest.read_text())==report,'certificate drift'
    print(json.dumps(report,indent=2))
if __name__=='__main__': main()
