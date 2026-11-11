#!/usr/bin/env python3
"""Exact supporting controls for the written phase/domain theorem, not a PDE certificate."""
import argparse
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / 'lab/process/x-p2-p3-phase-domain-index.json'

def build():
    checks = []
    controls = []
    def check(name, value, contrary=False):
        assert bool(value), name
        (controls if contrary else checks).append(name)
    matrices = [s.Matrix([[1, 2, 0], [0, 0, 0]]), s.Matrix([[1, 0], [0, 1], [1, 1]]), s.zeros(2, 3)]
    restrictions = [s.Matrix([[1, 0, 0]]), s.Matrix([[1, 1]]), s.Matrix([[1, 0, 0], [0, 1, 0]])]
    rows = []
    for i, (D, B) in enumerate(zip(matrices, restrictions)):
        m, n = D.shape
        Z = s.Matrix.hstack(*B.nullspace())
        R = D * Z
        k, c = n - D.rank(), m - D.rank()
        k0, c0 = Z.cols - R.rank(), m - R.rank()
        K = s.Matrix.hstack(*D.nullspace()) if D.nullspace() else s.zeros(n, 0)
        r = (B * K).rank()
        q = B.rank()
        check(f'exact_sequence_{i}', k0 == k-r and c0 == c+q-r)
        check(f'codimension_index_{i}', k0-c0 == k-c-q)
        for z in [s.Integer(-1), s.I, (s.Integer(3)+4*s.I)/5]:
            check(f'whole_phase_{i}_{z}', (z*D).rank() == D.rank() and (z*D).nullspace() == D.nullspace())
        check(f'adjoint_sign_{i}', (m-D.H.rank())-(n-D.H.rank()) == -(k-c))
        rows.append(dict(kernel=k,cokernel=c,constraint_rank=q,kernel_constraint_rank=r,restricted_kernel=k0,restricted_cokernel=c0,index=k-c,restricted_index=k0-c0))
    check('restriction_can_remove_kernel', rows[0]['restricted_kernel'] < rows[0]['kernel'], True)
    check('restriction_can_add_cokernel', rows[1]['restricted_cokernel'] > rows[1]['cokernel'], True)
    redundant=s.Matrix([[1,0,0],[2,0,0]])
    check('nominal_constraints_are_not_rank', redundant.rows == 2 and redundant.rank() == 1, True)
    x=s.symbols('x', nonnegative=True)
    a,b=s.symbols('a b', positive=True)
    # D_a u=f on the positive-a branch; zero initial trace.
    up=(s.exp(-b*x)-s.exp(-a*x))/(a-b)
    check('positive_branch_equation', s.simplify(s.diff(up,x)+a*up-s.exp(-b*x)) == 0)
    check('positive_branch_trace', up.subs(x,0)==0)
    check('positive_branch_kernel', s.simplify(s.diff(s.exp(-a*x),x)+a*s.exp(-a*x))==0)
    check('positive_kernel_L2', s.integrate(s.exp(-2*a*x),(x,0,s.oo))==1/(2*a))
    # D_{-a} u=f; unique L2 solution for a>0.
    un=-s.exp(-b*x)/(a+b)
    check('negative_branch_equation', s.simplify(s.diff(un,x)-a*un-s.exp(-b*x))==0)
    check('negative_trace_functional', un.subs(x,0)==-1/(a+b))
    check('negative_branch_trace_is_not_zero', un.subs({x:0,a:1,b:2})!=0, True)
    # A nonzero forcing in the codimension-one restricted negative-branch range.
    f=s.exp(-2*x)-s.Rational(4,3)*s.exp(-3*x)
    check('boundary_compatibility_can_hold', s.integrate(s.exp(-x)*f,(x,0,s.oo))==0)
    u=-s.exp(-2*x)/3+s.exp(-3*x)/3
    check('restricted_negative_solution', u.subs(x,0)==0 and s.simplify(s.diff(u,x)-u-f)==0)
    # Triangular escaping singular sequence: shift by3n, width2n, height1.
    n=s.symbols('n',positive=True);t=s.symbols('t',real=True)
    norm2=s.integrate((t/n)**2,(t,0,n))+s.integrate(((2*n-t)/n)**2,(t,n,2*n))
    grad2=2/n
    check('singular_sequence_norm', s.simplify(norm2-2*n/3)==0)
    check('singular_sequence_derivative_ratio', s.simplify(grad2/norm2-3/n**2)==0)
    check('singular_sequence_limit', s.limit(grad2/norm2,n,s.oo)==0)
    table=[{'a_sign':'+','domain':'H1','kernel':1,'cokernel':0,'index':1}, {'a_sign':'-','domain':'H1','kernel':0,'cokernel':0,'index':0}, {'a_sign':'+','domain':'H1_trace0','kernel':0,'cokernel':0,'index':0}, {'a_sign':'-','domain':'H1_trace0','kernel':0,'cokernel':1,'index':-1}]
    check('same_symbol_different_index_mod3', table[0]['index']%3 != table[1]['index']%3, True)
    check('both_boundary_index_drops', all(table[j+2]['index']==table[j]['index']-1 for j in [0,1]))
    check('sign_is_not_adjoint', rows[0]['index'] != -rows[0]['index'], True)
    check('real_sign_preserves_mod3_zero_property', all((v%3==0)==((-v)%3==0) for v in range(-12,13)))
    return dict(artifact='X_P2_P3_PHASE_DOMAIN_INDEX',program_target='X-P2-P3',tier='T2',status='internally_reviewed_conditional_structural_result',claim_effect='none',evidence_kind='Exact finite rational/complex linear algebra and symbolic analytic controls. Infinite-dimensional theorem is the written proof, not these totals.',checks=checks,contrary_controls=controls,finite_exact_sequence_rows=rows,halfline_index_table=table,halfline_table_basis='Written kernel/range proofs; symbolic probe checks solution identities and singular-sequence integrals.',scope=['Whole operator scalar multiplication with fixed domain and grading','Graph-norm finite-codimension restriction','Half-line analytic control, not a class-C action or GU realization'],not_established=['P2 is whole-operator scaling','Any class-C action exists with these domain choices','Physical chiral count or source 2+1','Global datum independence or class-C kill'])

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
    result=build()
    if args.write:REPORT.write_text(json.dumps(result,indent=2)+'\n')
    else:assert json.loads(REPORT.read_text())==result, 'report differs from exact replay'
    print(f"PASS {len(result['checks'])} supporting checks; {len(result['contrary_controls'])} contrary controls")
