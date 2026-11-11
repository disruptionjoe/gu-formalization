#!/usr/bin/env python3
"""Exact finite controls and separate numerical replay for the class-width audit.

No continuum, class-C membership, P1, or physical-count certification.
Run from repository root with its scientific Python environment.
"""
from pathlib import Path
import ast
import hashlib
import json
import sys
import numpy as np
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / 'lab/process/class-width-witness-audit.json'
checks = []

def check(ok, name, kind='exact'):
    if not bool(ok):
        raise AssertionError('FAIL: ' + name)
    checks.append({'name': name, 'kind': kind})


def exact_graph(twisted=True):
    # Actual old-code Lx=Ly=4, Phi=4 links are fourth roots of unity.
    L = 4; N = L*L
    tx,ty,w = [s.zeros(N) for _ in range(3)]
    edges = []
    def idx(x,y): return (y % L)*L + x % L
    for x in range(L):
        for y in range(L):
            a = idx(x,y)
            for t,b,u in [(tx,idx(x+1,y),s.Integer(1)),
                          (ty,idx(x,y+1),s.I**x if twisted else s.Integer(1))]:
                t[a,b] += -s.I*u/2; t[b,a] += s.I*s.conjugate(u)/2
                w[a,b] += -u/2; w[b,a] += -s.conjugate(u)/2
                w[a,a] += s.Rational(1,2); w[b,b] += s.Rational(1,2)
                edges.append((a,b,u))
    return tx,ty,w,edges


def old_functions():
    path = ROOT/'tests/function-space-ext/flux_index_2d.py'
    tree = ast.parse(path.read_text())
    # Reuse unmodified builders without running the historical top-level verdict.
    funcs = [n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('build_flux_dirac','chiral_index')]
    ns={'np':np,'s1':np.array([[0,1],[1,0]],complex),'s2':np.array([[0,-1j],[1j,0]],complex),'s3':np.diag([1,-1]).astype(complex)}
    exec(compile(ast.Module(body=funcs,type_ignores=[]),str(path),'exec'),ns)
    return ns,path


def positive_pivots(a):
    L=s.eye(a.rows); piv=[]
    for j in range(a.rows):
        dj=s.simplify(a[j,j]-sum(L[j,k]*s.conjugate(L[j,k])*piv[k] for k in range(j)))
        assert dj.is_positive is True, (j,dj)
        piv.append(dj)
        for i in range(j+1,a.rows):
            L[i,j]=s.simplify((a[i,j]-sum(L[i,k]*s.conjugate(L[j,k])*piv[k] for k in range(j)))/dj)
    assert s.simplify(L*s.diag(*piv)*L.conjugate().T-a)==s.zeros(a.rows)
    return piv


def replay_matches(saved, rows):
    if len(saved)!=len(rows):return False
    for a,b in zip(saved,rows):
        if set(a)!=set(b):return False
        for key in a:
            if isinstance(a[key],float):
                if not abs(a[key]-b[key])<1e-10:return False
            elif a[key]!=b[key]:return False
    return True


def main():
    tx,ty,w,edges=exact_graph()
    sx=s.Matrix([[0,1],[1,0]]);sy=s.Matrix([[0,-s.I],[s.I,0]]);sz=s.diag(1,-1)
    g=s.kronecker_product(sz,s.eye(16));d=s.kronecker_product(sx,tx)+s.kronecker_product(sy,ty)+s.kronecker_product(sz,w)
    incidence=s.zeros(len(edges),16)
    for k,(a,b,u) in enumerate(edges):incidence[k,a]=1;incidence[k,b]=-u
    check(w==incidence.conjugate().T*incidence/2,'magnetic energy equals sum of edge squares')
    check(d==d.conjugate().T and w==w.conjugate().T,'actual finite matrices Hermitian')
    check((g*d+d*g)/2==s.kronecker_product(s.eye(2),w),'actual Wilson anticommutator identity')
    check(g*d+d*g!=s.zeros(32),'Wilson operator is not odd for original grading','contrary_exact')
    pivots=positive_pivots(w)
    check(all(x>0 for x in pivots),'all magnetic Laplacian LDL pivots strictly positive')
    check(s.expand(w.det())>0,'magnetic Laplacian nonzero determinant')
    w0=exact_graph(False)[2]
    check(w0*s.ones(16,1)==s.zeros(16,1),'trivial holonomy restores parallel graph section','contrary_exact')
    d0=d-s.kronecker_product(sz,w)
    check(g*d0+d0*g==s.zeros(32),'removing Wilson term restores exact oddness','contrary_exact')
    # Rational lower bound from one four-cycle with |1-i|^2=2 and paths <=4.
    bound=s.Rational(1,4*16*(4/s.Integer(2)+4))
    bound_pivots=positive_pivots(w-bound*s.eye(16))
    check(all(x>0 for x in bound_pivots),'exact holonomy bound 1/384 lies below magnetic gap')
    # Exact control: a fixed separated spectral window has a noninteger chirality trace.
    q=s.Matrix([[s.Rational(3,5),-s.Rational(4,5)],[s.Rational(4,5),s.Rational(3,5)]])
    v=q[:,0];p=v*v.T;toy=q*s.diag(s.Rational(1,8),2)*q.T
    raw=s.trace(sz*p)
    check(q.T*q==s.eye(2) and p*p==p,'rational rotation and spectral projection are exact')
    check(raw==-s.Rational(7,25),'window chirality need not be integer','contrary_exact')
    check(toy.det()==s.Rational(1,4) and (toy-s.Rational(1,8)*s.eye(2)).det()==0,'fixed nonzero spectrum retains separated cutoff')
    check(round(raw)==0 and round(s.trace(sz*s.diag(1,0)))==1,'rounded chirality changes without any spectral crossing','contrary_exact')
    check(sz*p!=p*sz,'window is not invariant under original grading','contrary_exact')
    # Reuse the signed-readout identity on actual declared involution data.
    G=s.diag(1,1,-1,-1);eps=s.diag(-1,-1,-1,1);D=s.eye(4)+G*eps
    charge=-s.trace(eps)/2
    check(eps*eps==s.eye(4) and eps==eps.T,'signed-readout input is Hermitian involution')
    check(G*D+D*G==D*G*D,'reused Ginsparg-Wilson identity')
    P0=s.diag(1,1,0,1)
    check(P0*P0==P0 and D*P0==s.zeros(4) and 4-D.rank()==P0.rank(),'signed-readout projector is actual full kernel')
    check(charge==1 and s.trace(G*P0)==charge,'signed-readout equals exact kernel chirality in seed')
    check((G*(s.eye(4)-D))**2==s.eye(4),'modified grading is an involution')
    bad=s.diag(-2,-1,-1,1);badD=s.eye(4)+G*bad
    check(G*badD+badD*G!=badD*G*badD,'noninvolution destroys GW identity','contrary_exact')
    # Quantifier control: an external datum can realize an odd value not forced by interior.
    external=(-1,0,1,2,3)
    check(not all(n%2==1 for n in external) and any(n==3 for n in external),'not forcing odd does not imply not hosting odd','logic_exact')
    ns,old=old_functions();rows=[]
    exact_np=np.array(d.tolist(),complex)
    actual,ag,_=ns['build_flux_dirac'](4,4,4)
    check(np.max(np.abs(actual-exact_np))<1e-13,'exact fourth-root fixture matches historical builder','numerical')
    for phi in (0,1,2,3):
        Dn,Gn,_=ns['build_flux_dirac'](16,16,phi)
        vals,vecs=np.linalg.eigh(Dn)
        P=vecs[:,np.abs(vals)<.25]
        raw_trace=float(np.trace(P.conj().T@Gn@P).real)
        min_abs=float(np.min(np.abs(vals)))
        cut_small=min_abs/2 if phi else 1e-6
        rows.append({'L':16,'flux':phi,'cutoff':.25,'raw_window_chirality':raw_trace,'rounded':int(round(raw_trace)), 'window_dimension':P.shape[1],'minimum_absolute_eigenvalue':min_abs,'smaller_cutoff':cut_small,'smaller_window_dimension':int(np.sum(np.abs(vals)<cut_small))})
        check(abs(round(raw_trace))==phi,'historical rounded diagnostic reproduced flux '+str(phi),'numerical')
        if phi:
            check(min_abs>1e-4 and rows[-1]['smaller_window_dimension']==0,'nonzero flux has empty smaller window '+str(phi),'numerical')
    check(replay_matches(rows,rows),'historical replay shape baseline','report_consistency')
    check(not replay_matches(rows[:-1],rows),'truncated replay report rejected','contrary_report')
    missing=[dict(row) for row in rows];del missing[0]['minimum_absolute_eigenvalue']
    check(not replay_matches(missing,rows),'missing replay field rejected','contrary_report')
    report={'artifact':'CLASS_WIDTH_WITNESS_AUDIT','program_target':['LB-CLASS','X-P1-P2-P3'],'tier':'T2','claim_effect':'none; audit and conditional comparator evidence only','scope':'No new action, C membership, P1 physical propagation, source or ledger verdict. Universal kernel/coercivity proof is in the written note, not certified by this finite probe.','checks':checks,'summary':{k:sum(c['kind']==k for c in checks) for k in sorted({c['kind'] for c in checks})},'magnetic_fixture':{'L':4,'flux':4,'laplacian_determinant':str(w.det()),'ldl_pivots':[str(x) for x in pivots],'coercivity_lower_bound':str(bound)},'historical_numerical_replay':rows,'source_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'proofs':['explorations/conditional-build/class-width-witness-audit-2026-11-11.md','explorations/conditional-build/flux-control-kernel-audit-2026-11-11.md']}
    if '--write' in sys.argv:REPORT.write_text(json.dumps(report,indent=2)+'\n')
    else:
        saved=json.loads(REPORT.read_text())
        # Floating eigenvalues are numerical evidence, not byte-stable proof certificates.
        for key in ('checks','summary','magnetic_fixture','source_sha256'):assert saved[key]==report[key],key
        assert replay_matches(saved['historical_numerical_replay'],rows), 'historical replay mismatch'
    print(json.dumps({'PASS':report['summary'],'historical_replay':rows},indent=2))

if __name__=='__main__':main()
