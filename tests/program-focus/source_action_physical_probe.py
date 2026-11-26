"""Exact stationary-root response diagnostics; no physical mass or quotient claim.
Run by the coordinating agent; rational root certificates are recomputed.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import json
import source_action_deep_geometry as g
from source_action_deep_algebra import add, scale, certificate_for


def mul(A, B):
    out = {}
    for a, x in A.items():
        for b, y in B.items():
            c, s = g.cliff_mul(a, b)
            out[c] = out.get(c, Q(0)) + x*y*s
    return {c: x for c, x in out.items() if x}


def gamma(a):
    return {1 << a: Q(1)}


def components(T):
    assert all(e and not e & (e-1) for e, c in T)
    return [{c: v for (e, c), v in T.items() if e == 1 << a} for a in range(14)]


def contraction(T, axes):
    return add(*(scale(1/g.d[a], mul(gamma(a), T[a])) for a in axes))


def field_F_inverse(z, eta):
    return [add(z[a], scale(Q(-1, 2), mul(gamma(a), eta))) for a in range(14)], add(contraction(z, range(14)), scale(-6, eta))


def scalar_input_response(T):
    """V_T(0,nu), followed by actual -sigma(dt)^-1 and literal q on fields.
    dt has metric-dual e3 (dt=-theta3), a horizontal timelike covector; input nu is arbitrary.
    Returned entries are Clifford endomorphisms multiplying that input.
    """
    slash = contraction(T, range(14))
    r = T
    s = scale(Q(-1, 2), slash)
    # Equation-row R; this is distinct from literal field readout q.
    v = add(s, scale(Q(-1, 2), contraction(r, range(14))))
    u = [add(r[a], scale(Q(1, 2), mul(gamma(a), v))) for a in range(14)]
    ct_inv = scale(1/g.d[3], gamma(3))
    zprime = [mul(ct_inv, a) for a in u]
    eta = scale(-1, mul(ct_inv, v))
    z, nu = field_F_inverse(zprime, eta)
    back_r, back_s = sigma_time(z, nu)
    assert back_r == r and back_s == s, "Native principal inverse failed"
    return [scale(-1, z[a]) for a in range(4)] + [scale(-1, nu)]


def sigma_time(z, nu):
    c = gamma(3)
    trace = contraction(z, range(14))
    r = [add(mul(c, z[a]), scale(-g.d[3]*int(a == 3), trace), scale(g.d[3]*int(a == 3), nu)) for a in range(14)]
    s = add(z[3], scale(Q(-1, 2), mul(c, nu)))
    return r, s


def interval(l, root):
    x = list(map(Q, root['coordinates']))
    radius = Q(root['certificate']['radius'])
    center = sum(a*b for a, b in zip(l, x))
    error = radius*sum(map(abs, l))
    return {'center': str(center), 'error': str(error), 'lower': str(center-error), 'upper': str(center+error), 'approximate_center': float(center), 'approximate_error': float(error)}


def separated(a, b):
    return Q(a['upper']) < Q(b['lower']) or Q(b['upper']) < Q(a['lower'])


def variational_controls():
    """Exact small controls; the written proofs own the general conclusions."""
    checks = {}
    def check(name, value):
        checks[name] = bool(value)
        assert value, name
    def product(a, b):
        return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
    def plus(a, b):
        return [[x+y for x,y in zip(row,col)] for row,col in zip(a,b)]
    def neg(a): return [[-x for x in row] for row in a]
    def transpose(a): return list(map(list, zip(*a)))
    identity = [[1,0],[0,1]]
    positive_normal = [[0,-1],[-1,0]]
    negative_normal = [[0,-1],[1,0]]
    e = [[1],[1]]
    check('positive_normal_square', product(positive_normal,positive_normal)==identity)
    check('negative_normal_square', product(negative_normal,negative_normal)==neg(identity))
    check('preserved_line', product(positive_normal,e)==neg(e))
    check('nonzero_observed_derivative', product([[1,0]],product(positive_normal,e))==[[-1]])
    image = product(positive_normal,[[1],[0]])
    check('nonpreserved_line_rejected', image[1][0] != 0)
    H = [[2,3],[3,-2]]
    check('indefinite_symmetrizer', product(H,negative_normal)==product(transpose(negative_normal),H))
    check('congruence_reverses_H', product(transpose(negative_normal),product(H,negative_normal))==neg(H))
    check('positive_identity_not_symmetrizer', product(identity,negative_normal)!=product(transpose(negative_normal),identity))
    # Arbitrary point jets of A,C,row,field. The derivative of A is part
    # of the formal dual; omitting it is a deliberate detectable mutation.
    A=[[2,1],[3,4]];dA=[[1,2],[0,-1]];C=[[3,1],[-2,2]]
    row=[[2,3]];drow=[[1,-2]];psi=[[3],[-1]];dpsi=[[2],[4]]
    Dpsi=plus(product(A,dpsi),product(C,psi))
    dual=plus(neg(plus(product(drow,A),product(row,dA))),product(row,C))
    lhs=plus(product(row,Dpsi),neg(product(dual,psi)))
    rhs=plus(plus(product(drow,product(A,psi)),product(row,product(dA,psi))),product(row,product(A,dpsi)))
    check('Green_density_dual_product_rule',lhs==rhs)
    wrong=plus(neg(product(drow,A)),product(row,C))
    check('missing_coefficient_derivative_mutation',plus(product(row,Dpsi),neg(product(wrong,psi)))!=rhs)
    # lambda-degree bookkeeping with nonconstant density and operator.
    rho=[2,3,5];dop=[7,11,13]
    coefficients=[Q(0)]*7
    for i,a in enumerate(rho):
        for j,b in enumerate(dop): coefficients[i+j+2]+=a*b
    check('quadratic_matter_held_coefficients',coefficients[2]==14)
    check('bosonic_first_variations_enter_cubic',coefficients[3]==43)
    check('no_linear_or_constant_matter',coefficients[0]==coefficients[1]==0)
    return {'checks':checks,'count':len(checks),'all_passed':True,
            'scope':'Small exact controls, not native dimension or universal-proof substitutes.'}


def run(path):
    data = json.loads(path.read_text())
    roots = data['certified_roots']
    assert len(roots) == 2 and data['dimension'] == 59
    for root in roots:
        cert = certificate_for(data, root)
        assert Q(str(root['h'])) == 1
        assert cert['status'] == 'exact_local_root_certified'
        for key in ('e', 'a', 'b', 'radius', 'ball_image_bound', 'lipschitz_bound'):
            assert cert[key] == root['certificate'][key]
    basis = [components({(int(e), int(c)): Q(v) for e, c, v in row}) for row in data['basis']]
    functionals = {}
    for name, axes in [('mY', range(14)), ('mH', range(4)), ('mN', range(4, 14))]:
        functionals[name] = [contraction(T, axes).get(0, Q(0))/len(axes) for T in basis]
    assert all(14*y == 4*h+10*n for y, h, n in zip(functionals['mY'], functionals['mH'], functionals['mN']))
    values = {name: [interval(l, root) for root in roots] for name, l in functionals.items()}
    # Full fixed-reference central gauge counterexample: source scalar absent,
    # central d_B=d, d²=0 and T wedge T=0, leaving the mass term exactly.
    source = [add(*(scale(Q(v), basis[int(j)][a]) for j, v in data['S'].items())) for a in range(14)]
    assert all(not row.get(0, 0) for row in source)
    assert all(g.cliff_mul(0, c) == g.cliff_mul(c, 0) for c in range(1 << 14))
    # Nontrivial polynomial gradient fixture phi=x0²*x1+x2³.
    polynomial = {(2, 1, 0): Q(1), (0, 0, 3): Q(1)}
    def derivative(poly, axis):
        out = {}
        for powers, value in poly.items():
            if powers[axis]:
                new = list(powers); new[axis] -= 1
                out[tuple(new)] = value*powers[axis]
        return out
    gradient = [derivative(polynomial, a) for a in range(3)]
    assert all(derivative(gradient[a], b) == derivative(gradient[b], a) for a in range(3) for b in range(3))
    assert g.d[0] > 0 and g.d[3] < 0
    assert (-Q(-1))/g.d[0] > 0  # -Re(i*i) times inverse metric.
    # Canonical grade1 spinless component is mY*Phi1; the grade13 partner
    # is not excluded. H/N are observation-dependent scalars.
    # Recover the scalar response via principal inversion, rather than interpreting
    # an equation-row q_E as the field readout q_F.
    response = [scalar_input_response(T) for T in basis]
    receivers = sorted({(a, c) for R in response for a, row in enumerate(R) for c in row})
    witnesses = []
    for a, c in receivers:
        l = [R[a].get(c, Q(0)) for R in response]
        iv = [interval(l, root) for root in roots]
        if separated(*iv):
            witnesses.append({'observed_field_slot': a, 'clifford_mask': c, 'intervals': iv, 'functional': list(map(str, l))})
    witnesses.sort(key=lambda w: abs(Q(w['intervals'][0]['center'])-Q(w['intervals'][1]['center'])), reverse=True)
    assert witnesses, 'No certified literal instantaneous field-response distinction found'
    # Positive/negative controls: arbitrary scalar connection and zero response.
    zero = [{} for _ in range(14)]
    assert scalar_input_response(zero) == [{} for _ in range(5)]
    controls = 1
    for a in range(14):
        T = [{} for _ in range(14)]; T[a] = gamma(a)
        assert contraction(T, range(14)) == {0: Q(1)}
        assert scalar_input_response(T) != [{} for _ in range(5)]
        controls += 2
    return {'all_passed': True, 'root_certificates_recomputed': 2, 'exact_controls': controls,
            'variational_controls': variational_controls(),
            'scalar_definitions': 'mY=tr_Cl(gamma^a T_a)/14; mH and mN divide restricted contractions by4 and10. tr_Cl=Re tr/128.',
            'central_active_gauge_controls': {'source_scalar_absent': True, 'center_commutes_with_full_Clifford_basis': True, 'exact_gradient_closed': True, 'mass_energy_has_nonzero_positive_axis': True},
            'scalar_intervals': values, 'scalar_intervals_disjoint': {k: separated(*v) for k, v in values.items()},
            'literal_response_witness_count': len(witnesses), 'strongest_literal_response_witness': witnesses[0],
            'receiver': 'q_F[-sigma(dt)^-1 V_T](zeta=0,nu), dt=-theta3 (metric-dual e3), same field and principal frame; q_F=(zeta_H,nu).',
            'scope': 'Different stationary candidate backgrounds, same ambient R=-10 and kappa1. This is instantaneous zero-order response on the full classical field space, not a physical mass, response rate, autonomous observed equation, source-unique law, or gauge quotient.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run(Path(__file__).resolve().parents[2]/'lab/process/source-action-deep-coefficients.json')
    text = json.dumps(result, indent=2) + '\n'
    if args.output:
        args.output.write_text(text)
    else:
        print(text)
