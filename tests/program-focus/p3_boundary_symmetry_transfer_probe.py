#!/usr/bin/env python3
"""Exact finite controls; the infinite-domain theorem is proved in the note."""
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
checks = []
controls = []

def ck(name, predicate):
    assert bool(predicate), name
    checks.append(name)

def reject(name, false_predicate):
    assert not bool(false_predicate), name
    controls.append(name)

I = s.eye(2)
J = s.Matrix([[0, -1], [1, 0]])
e1, e2 = I[:, 0], I[:, 1]
ck('quaternionic_square', J * J.conjugate() == -I)
ck('positive_norm_preserved', J.H * J == I)
ck('real_scalar_holonomy_preserved', J * (2*I).conjugate() == (2*I)*J)
reject('complex_center_breaks_antilinear_intertwiner', J*(s.I*I).conjugate() == (s.I*I)*J)
z = (-1+s.sqrt(3)*s.I)/2
ck('su3_center_order_three', s.simplify(z**3) == 1)
ck('su3_center_nonreal', s.simplify(z-z.conjugate()) != 0)
a,b,c,d = s.symbols('a b c d', real=True)
U = s.Matrix([[a+s.I*b,c+s.I*d],[-c+s.I*d,a-s.I*b]])
ck('su2_entire_quaternionic_form_intertwines', s.simplify(J*U.conjugate()-U*J) == s.zeros(2))
B = s.diag(-1,1)
ck('spectral_sign_exchange', J*B.conjugate() == -B*J)
reject('principal_symmetry_implies_lower_order_symmetry', J*B.conjugate() == B*J)
ck('negative_to_positive', J*e1 == e2)
reject('negative_spectral_space_preserved', s.Matrix.hstack(e1,J*e1).rank() == 1)
ck('zero_operator_commutes', J*s.zeros(2) == s.zeros(2)*J)
reject('zero_operator_forces_zero_choice_invariance', s.Matrix.hstack(e1,J*e1).rank() == 1)
ck('whole_zero_space_preserved', J.rank() == 2)
ck('zero_subspace_preserved', J*s.zeros(2,0) == s.zeros(2,0))
x,t = s.symbols('x t', nonnegative=True)
f = s.Matrix([s.exp(-2*x), x*s.exp(-x)])
u = s.exp(-x)*s.integrate(s.exp(t)*f.subs(x,t),(t,0,x))
ck('actual_right_inverse_on_nontrivial_test_force', s.simplify(s.diff(u,x)+u-f) == s.zeros(2,1))
ck('right_inverse_has_zero_trace', u.subs(x,0) == s.zeros(2,1))
kernel = s.exp(-x)*e1
ck('actual_kernel_equation', s.diff(kernel,x)+kernel == s.zeros(2,1))
ck('actual_kernel_trace', kernel.subs(x,0) == e1)
ck('kernel_is_l2', s.integrate(s.exp(-2*x),(x,0,s.oo)) == s.Rational(1,2))
reject('kernel_domain_preserved', (J*kernel).subs(x,0)[1] == 0)
trace_constraint = s.Matrix([[0,1]])
ck('one_allowed_kernel_coefficient', len(trace_constraint.nullspace()) == 1)
ck('zero_trace_kernel_dimension', len(I.nullspace()) == 0)
ck('unrestricted_kernel_dimension', len(s.zeros(0,2).nullspace()) == 2)
spectral = [-3,-1,0,0,2,4]
allowed_a = [v for v in spectral if v < 0]
allowed_b = [v for v in spectral if v < 3]
band = [v for v in spectral if 0 <= v < 3]
ck('cut_adds_actual_band', len(allowed_b)-len(allowed_a) == len(band) == 3)
reject('reversed_relative_index_sign', len(allowed_b)-len(allowed_a) == -len(band))
# A linear involution need not preserve a trace line despite full bulk commutation.
T = s.Matrix([[0,1],[1,0]])
ck('linear_coflip_involution', T*T == I)
reject('involution_implies_trace_invariance', s.Matrix.hstack(e1,T*e1).rank() == 1)

payload = {'artifact':'P3_BOUNDARY_SYMMETRY_TRANSFER','program_target':'P3xsymmetry',
 'tier':'T2','claim_effect':'none','finite_supporting_checks':checks,
 'contrary_controls':controls,'counts':{'supporting':len(checks),'contrary':len(controls)},
 'analytic_evidence':'Written trace-surjectivity, spectral-domain and half-line proofs; finite checks do not certify infinite-dimensional Fredholmness.',
 'scope':'Conditional analytic subfamily and controls; no class-C action, full GU boundary operator or physical count.',
 'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
report = ROOT/'lab/process/p3-boundary-symmetry-transfer.json'
if __name__ == '__main__':
    import sys
    if '--write' in sys.argv:
        report.write_text(json.dumps(payload,indent=2)+'\n')
    else:
        assert json.loads(report.read_text()) == payload, 'evidence replay mismatch'
    print(json.dumps({'counts':payload['counts'],'status':'pass'}))
