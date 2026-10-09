#!/usr/bin/env python3
"""Derive a coupled scalar mode from the selected flat K77 I1B action.

The sparse Clifford engine is used directly, without loading a coefficient
bank or executing historical probes. All adjoints below are formal bulk
adjoints on compactly supported variations. This is not a GU domain theorem.
"""

from itertools import combinations
import json

import sympy as sp

from k77_exact_bank_api import K77Core, ONE


ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
CORE = K77Core(ETA, ("comm", "symi", "symi"))
SLOTS = [(i, j) for i in range(4) for j in range(i, 4)]
PAIRS = list(combinations(range(14), 2))


def direction(mu, mask):
    return {1 << mu: {mask: ONE}}


def exact(value):
    return sp.Rational(value[0]) + sp.I * sp.Rational(value[1])


def dual_rows(image):
    """Every nonzero one-form Euler row in a sparse 13-form image."""
    out = {}
    for form, element in image.items():
        complement = CORE.full ^ form
        assert complement and not complement & (complement - 1)
        mu = complement.bit_length() - 1
        for mask in element:
            value = exact(CORE.pair(direction(mu, mask), image))
            if value:
                out[(mu, mask)] = value
    return out


def derivative_block(axis, labels):
    basis = [(mu, label ^ (1 << mu)) for label in labels for mu in range(14)]
    index = {item: i for i, item in enumerate(basis)}
    raw = sp.zeros(len(basis))
    for j, (mu, mask) in enumerate(basis):
        image = CORE.shiab(CORE.wedge_raw(direction(axis, 0), direction(mu, mask)))
        rows = dual_rows(image)
        assert set(rows) <= set(index), "derivative image escaped invariant label block"
        for row, value in rows.items():
            raw[index[row], j] = value
    return basis, (raw - raw.T) / 2


def mass_block(basis):
    return sp.diag(*[exact(CORE.pair(direction(mu, mask), CORE.hodge(direction(mu, mask))))
                     for mu, mask in basis])


def curvature_columns(q):
    """K132/K135 curvature-injection convention, differentiated before restriction."""
    columns = []
    for p, r in SLOTS:
        def h(i, j):
            return int((i, j) == (p, r) or (p != r and (i, j) == (r, p)))
        curvature = {}
        for i, j in PAIRS:
            element = {}
            for a, b in PAIRS:
                value = ETA[a] * ETA[b] * (
                    q[i]*q[a]*h(j, b) - q[i]*q[b]*h(j, a)
                    - q[j]*q[a]*h(i, b) + q[j]*q[b]*h(i, a))
                if value:
                    element = CORE.eadd(element, CORE.escale(value, CORE.blade((a, b))))
            if element:
                curvature[(1 << i) | (1 << j)] = element
        columns.append(dual_rows(CORE.shiab(curvature)))
    return columns


def matrix_from_columns(columns, basis):
    return sp.Matrix([[column.get(row, 0) for column in columns] for row in basis])


def cubic_gradient(field, receiver):
    square = CORE.wedge_raw(field, field)
    varied = CORE.fadd(CORE.wedge_raw(receiver, field), CORE.wedge_raw(field, receiver))
    return exact(CORE.pair(receiver, CORE.shiab(square)))/3 + exact(CORE.pair(field, CORE.shiab(varied)))/3


def certify():
    passed = []

    def zero(value):
        if isinstance(value, sp.MatrixBase):
            return all(sp.simplify(entry) == 0 for entry in value)
        return sp.simplify(value) == 0

    def check(label, value):
        if not bool(value):
            raise AssertionError(label)
        passed.append(label)

    basis, E = derivative_block(0, (0, 1))
    K = mass_block(basis)
    check("formal first-order Euler coefficient is skew", E.T == -E)
    check("mass form is an involution on complete label block", K*K == sp.eye(28))

    # Nonlinear necessary rows are varied before imposing the radial ansatz.
    radial = CORE.phi1
    companion = {1 << mu: {(1 << mu)^1: ONE} for mu in range(1,14)}
    rv = sp.Matrix([1]*14+[0]*14)
    vv = sp.Matrix([0]*15+[1]*13)
    check("a varying pure radial scalar excites omitted bivector equations",
          E*rv == -11*vv)
    check("bivector derivative enters transverse but not longitudinal radial row",
          E*vv == sp.Matrix([0]+[11]*13+[0]*14))
    rows = [(direction(0,1), (312,0,-sp.Rational(260,3))),
            (direction(1,2), (312,0,-88)),
            (direction(1,3), (0,-sp.Rational(568,3),0))]
    for i, (receiver, expected) in enumerate(rows):
        pp = cubic_gradient(radial,receiver)
        vv_row = cubic_gradient(companion,receiver)
        pv = cubic_gradient(CORE.fadd(radial,companion),receiver)-pp-vv_row
        check(f"full nonlinear normal Euler row {i+1} differentiated from cubic action",
              (pp,pv,vv_row) == expected)
    phi, v, kap = sp.symbols("phi v kap", real=True)
    F = kap*phi+312*phi**2-sp.Rational(260,3)*v**2
    phip = -(kap/sp.Integer(11)+sp.Rational(568,33)*phi)*v
    vp = sp.Rational(4,33)*v*v
    compatibility = sp.cancel((sp.diff(F,phi)*phip+sp.diff(F,v)*vp)/v)
    compatibility = sp.factor(compatibility.subs(v*v,3*(kap*phi+312*phi**2)/260))
    check("radial plus single-vector nonlinear compatibility obstruction",
          zero(compatibility+(118976*phi**2+816*kap*phi+kap**2)/11))

    # a: time grade one; b,d: horizontal-spatial/vertical grade one;
    # u,w: their gamma_0 gamma_mu bivector companions.
    R = sp.zeros(28, 5)
    R[0, 0] = 1
    for mu in range(1, 14):
        R[mu, 1 if mu < 4 else 2] = 1
        R[14+mu, 3 if mu < 4 else 4] = 1
    Er, Kr = R.T*E*R, R.T*K*R
    expected_E = sp.Matrix([[0,0,0,0,0], [0,0,0,3,30], [0,0,0,30,80],
                            [0,-3,-30,0,0], [0,-30,-80,0,0]])
    check("five-field derivative matrix derived from Clifford action", Er == expected_E)
    check("five-field Hodge mass signs and multiplicities", Kr == sp.diag(1,3,10,-3,-10))

    q0 = (1,) + (0,)*13
    columns = curvature_columns(q0)
    A = matrix_from_columns(columns, basis)
    h = sp.Matrix([int(i == j and i != 0) for i, j in SLOTS])
    check("scalar curvature image has no omitted Clifford rows",
          all(sum(columns[j].get(row, 0)*h[j] for j in range(10)) == 0
              for row in set().union(*[set(col) for col in columns]) - set(basis)))
    Ar = R.T*A*h
    check("native metric coupling distinguishes horizontal and vertical scalars", Ar == sp.Matrix([0,-12,-60,0,0]))

    k, z = sp.symbols("kappa z", real=True, nonzero=True)
    H = sp.zeros(6)
    H[0, 1:] = z*z*Ar.T
    H[1:, 0] = z*z*Ar
    H[1:, 1:] = k*Kr + z*Er
    full = sp.zeros(38)
    full[:10, 10:] = z*z*A.T
    full[10:, :10] = z*z*A
    full[10:, 10:] = k*K + z*E
    lift = sp.zeros(38, 6)
    lift[:10, 0] = h
    lift[10:, 1:] = R
    check("all ten metric and twenty-eight distortion rows close on scalar ansatz",
          zero(full*lift-lift*(lift.T*lift).inv()*H))
    determinant = sp.factor(H.det())
    check("complete coupled scalar characteristic polynomial",
          zero(determinant-21600*k*k*z**4*(113*z*z-17*k*k)))
    check("uniform transverse distortion shell is removed by metric coupling", H.subs({k:11,z:1}).det() != 0)
    transverse = sp.Matrix([0,1,1,-11*z/k,-11*z/k])
    check("uniform transverse distortion-only mode fails the metric equation",
          zero(((k*Kr+z*Er)*transverse).subs(z*z,k*k/121))
          and (Ar.T*transverse)[0] == -72)

    mode = sp.Matrix([135/(17*k), 0, -5, 1, -5*z/k, 7*z/k])
    residual = sp.simplify(full*lift*mode)
    check("growing mode satisfies every lifted row on its dispersion relation",
          zero(residual.subs(z*z, sp.Rational(17,113)*k*k)))
    check("characteristic mode is simple in six-field sector",
          H.subs({k:113,z:sp.sqrt(1921)}).rank() == 5)
    check("new coupled root occurs with invertible five-field distortion block",
          (k*Kr+z*Er).subs({k:113,z:sp.sqrt(1921)}).det() != 0)
    check("mode has nonzero tensorial distortion, so is not T0 frame gauge", mode[3] == 1)
    # The h_11 time-time curvature jet is proportional to z^2 psi.
    check("metric perturbation has nonzero flat linearized curvature", sp.simplify(z*z*mode[0]) != 0)

    # Derive the dynamics again by eliminating the auxiliary bivectors in
    # the action and imposing the zero-affine metric-equation branch.
    d, dp, b, bp, u, w = sp.symbols("d dp b bp u w", real=True)
    L = k*(3*b*b+10*d*d-3*u*u-10*w*w)/2-u*(3*bp+30*dp)-w*(30*bp+80*dp)
    auxiliary = {u:-(bp+10*dp)/k, w:-(3*bp+8*dp)/k}
    check("both eliminated bivectors satisfy their actual Euler equations",
          zero(sp.diff(L,u).subs(auxiliary)) and zero(sp.diff(L,w).subs(auxiliary)))
    Lr = sp.factor(L.subs(auxiliary).subs({b:-5*d,bp:-5*dp}))
    check("reduced zero-affine-branch action derived directly",
          zero(Lr-565*dp*dp/(2*k)-85*k*d*d/2))
    check("independent Euler derivation gives the same growth rate",
          zero(sp.diff(Lr,d)/sp.diff(Lr,dp,2)-sp.Rational(17,113)*k*k*d))
    energy = sp.factor(dp*sp.diff(Lr,dp)-Lr)
    check("conserved reduced energy is indefinite", zero(energy-565*dp*dp/(2*k)+85*k*d*d/2))
    check("kappa zero is degenerate rather than a positive continuation", H.subs({k:0,z:1}).rank() == 4)

    # A rational nonzero-spatial-frequency mode: q=(25,36i,0,0),
    # q^2=1921=17*113, kappa=113. This tests the Lorentz-covariant
    # polarization beyond the homogeneous time-axis calculation.
    labels = (0,1,2,3)
    basis2, E0 = derivative_block(0, labels)
    _, E1 = derivative_block(1, labels)
    q1 = (0,1)+(0,)*12
    q01 = (1,1)+(0,)*12
    cols0, cols1, cols01 = columns, curvature_columns(q1), curvature_columns(q01)
    union = set().union(*[set(col) for cols in (cols0,cols1,cols01) for col in cols])
    complete_basis = sorted(set(basis2)|union)
    Aq = 25**2*matrix_from_columns(cols0,complete_basis) + (36*sp.I)**2*matrix_from_columns(cols1,complete_basis)
    Aq += 25*36*sp.I*(matrix_from_columns(cols01,complete_basis)-matrix_from_columns(cols0,complete_basis)-matrix_from_columns(cols1,complete_basis))
    q = sp.Matrix([25,36*sp.I,0,0])
    eta4 = sp.diag(*ETA[:4])
    mu2 = 1921
    P = sp.eye(4)-q*(eta4*q).T/mu2
    hm = -sp.Rational(135,1921)*P*eta4
    hv = sp.Matrix([hm[i,j] for i,j in SLOTS])
    tv = sp.zeros(56,1)
    idx = {item:i for i,item in enumerate(basis2)}
    for a in range(14):
        if a < 4:
            for j in range(4):
                if P[a,j]:
                    tv[idx[(a,1<<j)]] += -5*P[a,j]
        else:
            tv[idx[(a,1<<a)]] += 1
        gain = -sp.Rational(5,113) if a < 4 else sp.Rational(7,113)
        for j in range(2):
            if a != j:
                blade = CORE.emul(CORE.blade(j), CORE.blade(a))
                for mask, coef in blade.items():
                    tv[idx[(a,mask)]] += gain*ETA[j]*q[j]*exact(coef)
    eqt = (113*mass_block(basis2)+25*E0+36*sp.I*E1)*tv
    padded = sp.Matrix([tv[idx[row]] if row in idx else 0 for row in complete_basis])
    padded_eq = sp.Matrix([eqt[idx[row]] if row in idx else 0 for row in complete_basis])
    check("nonzero spatial frequency has exact dispersion", (q.T*eta4*q)[0] == mu2)
    check("all distortion rows vanish for spatially varying growing mode", zero(padded_eq+Aq*hv))
    check("all ten metric rows vanish for spatially varying growing mode", zero(Aq.T*padded))

    return {
        "result_id":"NATIVE-I1B-SCALAR-CLOSURE",
        "checks_passed":len(passed), "checks":passed, "sympy_version":sp.__version__,
        "base_signature":list(ETA), "selected_shiab":["comm","symi","symi"],
        "coupled_scalar_determinant":str(determinant),
        "growing_dispersion":"gamma^2+|p|^2=17*kappa_1^2/113, kappa_1!=0",
        "full_metric_and_distortion_rows_checked":True,
        "nonlinear_consistent_truncation_proved":False,
        "native_global_background_or_physical_domain_constructed":False,
        "claim_ceiling":"Exact coupled linearized modes on the selected flat source-shaped K77 I1B germ; no GU quantum-consistency verdict."
    }


if __name__ == "__main__":
    print(json.dumps(certify(),indent=2))
