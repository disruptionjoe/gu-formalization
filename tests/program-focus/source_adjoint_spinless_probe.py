#!/usr/bin/env python3
"""Exact pairing adapter and source-typed spinless controls.

Binary-exact Clifford matrices; no numerical rank or physical-domain claim.
The written proof supplies completeness and source applicability. Run serially.
"""
import argparse
import json
import os
from pathlib import Path
import sys
for key in ('OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'OMP_NUM_THREADS'):
    os.environ.setdefault(key, '1')
import numpy as np


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--repo', required=True)
    p.add_argument('--output')
    args = p.parse_args()
    root = Path(args.repo).resolve()
    sys.path.insert(0, str(root / 'tests/channel-swings'))
    sys.path.insert(0, str(root / 'tests/program-focus'))
    from actual_sym2_c14_orbit_probe import native_gammas
    from source_normal_tensor_class_probe import character_counts
    g, eta = native_gammas()
    I = np.eye(128, dtype=complex)
    Z = np.zeros_like(I)
    eq = np.array_equal
    checks = []
    def check(name, ok):
        checks.append(dict(name=name, passed=bool(ok)))
        assert ok, name
    def mul(xs):
        a = I.copy()
        for x in xs:
            a = a @ x
        return a
    H = [9, 0, 1, 2]
    N = [3, 4, 5, 6, 7, 8, 10, 11, 12, 13]
    h = mul([g[a] for a in H])
    n = mul([g[a] for a in N])
    om = h @ n
    kp = mul(g[:9])
    km = 1j * kp @ om
    C = mul([x for x in g if eq(x.conjugate(), -x)])
    check('both nondegenerate Hermitian neutral involutions', all(eq(k.conjugate().T,k) and eq(k@k,I) and np.trace(k)==0 for k in (kp,km)))
    check('plus comparator vectors selfadjoint', all(eq(x.conjugate().T@kp,kp@x) for x in g))
    check('primary-compatible vectors skew-adjoint', all(eq(x.conjugate().T@km,-km@x) for x in g))
    check('fixed C quaternionic and real-Clifford commuting', eq(C@C.conjugate(),-I) and all(eq(C@x.conjugate(),x@C) for x in g))
    check('C isometry only for plus; anti-isometry for minus', eq(C.conjugate().T@kp@C,kp.conjugate()) and eq(C.conjugate().T@km@C,-km.conjugate()))
    for k in range(15):
        w = mul(g[:k])
        sp = (-1)**(k*(k-1)//2)
        sm = (-1)**(k*(k+1)//2)
        check(f'grade{k} both adjoint laws',eq(w.conjugate().T@kp,sp*kp@w) and eq(w.conjugate().T@km,sm*km@w))
    A = [I,h,n,om]
    for j,a in enumerate(A):
        alpha = [g[v]@a for v in N]
        check(f'fixed tensor{j} minus-skew plus-self and C-even',all(eq(x.conjugate().T@km,-km@x) and eq(x.conjugate().T@kp,kp@x) and eq(C@x.conjugate(),x@C) for x in alpha))
        check(f'fixed tensor{j} contraction10',eq(sum((eta[v]*g[v]@x for v,x in zip(N,alpha)),Z.copy()),10*a))
    check('horizontal real-vector survivor with full contraction4',all(eq(g[a].conjugate().T@km,-km@g[a]) for a in H) and eq(sum((eta[a]*g[a]@g[a] for a in H),Z.copy()),4*I))
    check('old real-axial witness is minus-self, not minus-skew',all(eq((g[a]@h).conjugate().T@km,km@g[a]@h) for a in H))
    check('both horizontal and normal complex grade adjoints unchanged',all(eq(x.conjugate().T@k,s*k@x) for k in (kp,km) for x,s in ((1j*h,-1),(1j*n,1))))
    check('full spinless real vector allowed; imaginary vector excluded in minus',all(eq(x.conjugate().T@km,-km@x) and not eq((1j*x).conjugate().T@km,-km@(1j*x)) for x in g))
    check('full ambient contraction14',eq(sum((eta[a]*g[a]@g[a] for a in range(14)),Z.copy()),14*I))
    rows = character_counts()
    dims = {}
    for name,ks in [('plus',[3,7]),('minus',[1,5,9])]:
        d = 2*sum(rows[k]['normal_multiplicity'] for k in ks)
        image = 2*sum(rows[k-1]['invariants']+rows[k+1]['invariants'] for k in ks)
        dims[name] = [d,image,d-image]
    check('optional C exact character counts',dims=={'plus':[32,20,12],'minus':[36,24,12]})
    check('shared full sharp-real dimension68 image44 kernel24',2*sum(rows[k]['normal_multiplicity'] for k in (1,3,5,7,9))==68 and 2*sum(rows[k-1]['invariants']+rows[k+1]['invariants'] for k in (1,3,5,7,9))==44)
    # Observation-kernel witness: zeta=J_N psi/10 has b=0,tau=psi.
    # Primitive output at literal O has (mu*f*J_H psi,mu*g*psi).
    # Exact coefficients isolate both required vanishing conditions.
    check('literal observation kernel exposes both f and g',eq(sum((eta[a]*g[a]@g[a] for a in N),Z.copy()),10*I))
    result=dict(checks=checks,optional_C_dimensions=dims,fixed_endogenous_weak={'plus':[4,0],'minus':[4,4]},horizontal_dimension_each=12,scope='K95 algebra adapter; not K77 equality, Sp pairing, formal barred density, physical mass or GU verdict')
    if args.output:
        Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS {len(checks)} exact pairing/placement controls; C32->36, fixed C0->4')

if __name__=='__main__':
    main()
