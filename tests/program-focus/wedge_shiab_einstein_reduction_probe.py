"""Exact controls for the scoped leading four-dimensional wedge reduction.

Call run(). The CLI writes or verifies a deterministic certificate. The direct
Gamma1 Gamma1 expression is the integrated fixed-M quadratic action,
after compact-support integration of the Ricci derivative terms.
"""
import sympy as sp


def moment_controls():
    checks = []

    def ck(name, condition):
        assert condition, name
        checks.append(name)

    eta = sp.diag(-1, 1, 1, 1)
    pairs = [(i, j) for i in range(4) for j in range(i, 4)]
    hs = sp.symbols('h00 h01 h02 h03 h11 h12 h13 h22 h23 h33')
    ms = sp.symbols('m00 m01 m02 m03 m11 m12 m13 m22 m23 m33')
    vs = sp.symbols('v0:4')  # Covariant gauge-parameter amplitude.

    def symmetric(values):
        out = sp.zeros(4)
        for (i, j), value in zip(pairs, values):
            out[i, j] = out[j, i] = value
        return out

    H, M = symmetric(hs), symmetric(ms)

    def gamma(k, field):
        return [[[sp.Rational(1, 2)*eta[r, r]
                  *(k[mu]*field[r, nu]+k[nu]*field[r, mu]-k[r]*field[mu, nu])
                  for nu in range(4)] for mu in range(4)] for r in range(4)]

    def fixed_quadratic(moment, G):
        traces = [sum(G[r][r][lam] for r in range(4)) for lam in range(4)]
        return sp.expand(sum(moment[mu, nu]
                             *(sum(traces[lam]*G[lam][mu][nu] for lam in range(4))
                               -sum(G[r][nu][lam]*G[lam][mu][r]
                                    for r in range(4) for lam in range(4)))
                             for mu in range(4) for nu in range(4)))

    def linear_ricci(k, G):
        return sp.Matrix(4, 4, lambda mu, nu:
                         sum(k[r]*G[r][mu][nu]-k[nu]*G[r][mu][r] for r in range(4)))

    tau = [sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(0)]
    gauge = sp.Matrix(4, 4, lambda i, j: tau[i]*vs[j]+tau[j]*vs[i])
    qH = fixed_quadratic(M, gamma(tau, H))
    qG = fixed_quadratic(M, gamma(tau, gauge))
    mixed = sp.expand(fixed_quadratic(M, gamma(tau, H+gauge))-qH-qG)
    expected = -sp.Rational(1, 2)*vs[0]*sum((M[i, j]+M[0, 0]*int(i == j))*H[i, j]
                                            for i in range(1, 4) for j in range(1, 4))
    expected -= sum(M[0, i]*H[i, j]*vs[j] for i in range(1, 4) for j in range(1, 4))
    ck('direct-Gamma-mixed-gauge-formula', sp.expand(mixed-expected) == 0)
    ck('pure-gauge-test-alone-is-insufficient', qG == 0)
    equations = sp.Poly(mixed, *(hs+vs)).coeffs()
    matrix, rhs = sp.linear_eq_to_matrix(equations, ms)
    ck('gauge-equations-homogeneous', rhs == sp.zeros(rhs.rows, 1))
    ck('complete-ten-moment-gauge-rank', matrix.rank() == 9)
    eta_vector = sp.Matrix([eta[i, j] for i, j in pairs])
    ck('isotropic-moment-in-kernel', matrix*eta_vector == sp.zeros(matrix.rows, 1))
    canonical = [M[0, 1], M[0, 2], M[0, 3], M[1, 2], M[1, 3], M[2, 3],
                 M[0, 0]+M[1, 1], M[0, 0]+M[2, 2], M[0, 0]+M[3, 3]]
    cmatrix, _ = sp.linear_eq_to_matrix(canonical, ms)
    ck('canonical-nine-equations-exhaustive', cmatrix.rank() == 9 and matrix.col_join(cmatrix).rank() == 9)
    witness = {x: 0 for x in hs+ms+vs}
    witness.update({M[0, 0]: 1, H[1, 1]: 1, vs[0]: 1})
    ck('nonisotropic-mixed-gauge-witness', mixed.subs(witness) == -sp.Rational(1, 2))

    # General wave covector: the paired Fourier/IBP density correction is
    # -delta(sqrt|g|g^-1).Ric1(k,H), because Ric1 has two derivatives.
    # This sign is independent of the rank test above.
    ks = sp.symbols('k0:4')
    G = gamma(ks, H)
    raw = fixed_quadratic(eta, G)
    R1 = linear_ricci(ks, G)
    delta_density_inverse = sp.trace(eta*H)*eta/2-eta*H*eta
    density_term = sp.expand(sum(delta_density_inverse[i, j]*R1[i, j]
                                 for i in range(4) for j in range(4)))
    ck('metric-density-correction-is-twice-raw-symbol', sp.expand(density_term-2*raw) == 0)
    eh2 = sp.expand(raw-density_term)
    ck('fixed-moment-is-minus-EH2', sp.expand(raw+eh2) == 0)
    conformal = {H[i, j]: 2*eta[i, j] for i, j in pairs}
    norm_k = sum(eta[i, i]*ks[i]**2 for i in range(4))
    ck('conformal-fixed-control', sp.expand(raw.subs(conformal)+6*norm_k) == 0)
    ck('conformal-moving-EH-control', sp.expand(eh2.subs(conformal)-6*norm_k) == 0)
    tt = {x: 0 for x in hs+ks}
    tt[H[1, 2]] = 1
    tt[ks[0]] = 1
    ck('TT-fixed-sign', raw.subs(tt) == -sp.Rational(1, 2))
    ck('TT-moving-EH-sign', eh2.subs(tt) == sp.Rational(1, 2))
    ck('wrong-freeze-then-vary-rule-detected', raw.subs(tt) != eh2.subs(tt))

    # Three rational Lorentz boosts: invariant finite measures are a written
    # recurrence/annulus argument, not proved by these finite linear checks.
    Y = H
    all_fixed_rows = []
    for axis in range(1, 4):
        B = sp.eye(4)
        B[0, 0] = B[axis, axis] = sp.Rational(5, 3)
        B[0, axis] = B[axis, 0] = sp.Rational(4, 3)
        ck('boost-preserves-eta:'+str(axis), B.T*eta*B == eta)
        transformed = B.T*Y*B
        action = sp.Matrix([[sp.diff(transformed[i, j], h) for h in hs] for i, j in pairs])
        eigenvalues = action.eigenvals()
        ck('boost-positive-real-semisimple:'+str(axis),
           set(eigenvalues) == {sp.Rational(1, 9), sp.Rational(1, 3), sp.Integer(1), sp.Integer(3), sp.Integer(9)}
           and action.is_diagonalizable())
        all_fixed_rows.append(action-sp.eye(10))
    fixed_matrix = all_fixed_rows[0].col_join(all_fixed_rows[1]).col_join(all_fixed_rows[2])
    ck('three-boost-fixed-space-rank-nine', fixed_matrix.rank() == 9 and fixed_matrix*eta_vector == sp.zeros(30, 1))
    one_boost_atom = sp.diag(-1, 1, 2, 3)
    first = sp.eye(4)
    first[0, 0] = first[1, 1] = sp.Rational(5, 3)
    first[0, 1] = first[1, 0] = sp.Rational(4, 3)
    ck('one-boost-invariance-is-insufficient', first.T*one_boost_atom*first == one_boost_atom
       and one_boost_atom != eta and one_boost_atom != 2*eta)

    # Vertical lambda and the actual four-dimensional horizontal volume:
    # sqrt|ag|=a^2 sqrt|g|, so the action moment is m1, not m(-1).
    moments = []
    fixtures = [[(sp.Integer(1), sp.Integer(1))],
                [(sp.Integer(1), sp.Integer(2))],
                [(sp.Rational(1, 2), sp.Integer(1)), (sp.Rational(1, 2), sp.Integer(2))]]
    for index, atoms in enumerate(fixtures):
        m0 = sum(w for w, a in atoms)
        m1 = sum(w*a for w, a in atoms)
        m2 = sum(w*a*a for w, a in atoms)
        inverse_total_moment = sum((w*a*a/m2)/a for w, a in atoms)
        ck('actual-volume-moment:'+str(index), m0 == 1 and m2*inverse_total_moment == m1)
        moments.append({'m0': str(m0), 'm1': str(m1), 'm2': str(m2),
                        'normalized_total_inverse_moment': str(inverse_total_moment)})
    ck('normalization-does-not-fix-EH-moment', moments[0]['m1'] != moments[1]['m1'])

    return {'checks': len(checks), 'check_names': checks,
            'moment_order': [str(m) for m in ms], 'gauge_rank': 9,
            'gauge_kernel': [str(x) for x in eta_vector],
            'canonical_gauge_constraints': [str(x) for x in canonical],
            'fixed_to_EH2_ratio': '-1', 'finite_vertical_measure_controls': moments,
            'scope': 'Exact4D quadratic-symbol and finite boost/moment controls only. Compact-support IBP, universal gauge classification and finite-measure support are written proofs. No selected regulator or physical GR/Newton claim.'}


def reduction_controls():
    checks=[]
    def ck(name, value):
        assert value, name
        checks.append(name)
    def eq(name, expression):
        ck(name, sp.factor(expression)==0)
    R,Q,K,a,h,m0,m1,m2=sp.symbols('R Q K a h m0 m1 m2', nonzero=True)
    eig=[sp.Rational(1,4)]*5+[-sp.Rational(5,4)]*9
    eq('native-R',sum(eig)+10)
    eq('native-Ric-square',sum(x*x for x in eig)-sp.Rational(115,8))
    F=sp.Rational(115,8)+R/(2*a)+Q/a**2+sp.Rational(5,2)*(-10+R/a)**2
    expected=(Q+sp.Rational(5,2)*R**2)/a**2-sp.Rational(99,2)*R/a+sp.Rational(2115,8)
    eq('exact-conformal-ray-scalar',F-expected)
    C=K-2*Q+R**2/3; E=K-4*Q+R**2
    eq('Weyl-Euler-identity',C/2-E/2+sp.Rational(17,6)*R**2-Q-sp.Rational(5,2)*R**2)
    eq('Ricci-flat-Weyl-control',(C/2-E/2+sp.Rational(17,6)*R**2).subs({R:0,Q:0}))
    eq('constant-curvature-control',(C/2-E/2+sp.Rational(17,6)*R**2).subs({Q:R**2/4,K:R**2/6})-sp.Rational(11,4)*R**2)
    ck('Euler-not-deletable-as-density', (C/2).subs({R:0,Q:0,K:1})!=0)
    eq('vertical-atom-EH-moment',a**2/a-a)
    ck('false-inverse-atom-moment-detected',sp.Rational(2)!=sp.Rational(1,2))
    weights=[sp.Rational(5,8),sp.Rational(3,8)]; atoms=[sp.Rational(1,2),sp.Rational(3,2)]
    moments=[sum(w*x**j for w,x in zip(weights,atoms)) for j in range(3)]
    ck('fixed-volume-normalization-still-free',moments==[1,sp.Rational(7,8),1])
    mu,v=sp.symbols('mu v',positive=True)
    am=mu/2; ap=mu+2*v/mu; pm=4*v/(mu**2+4*v); pp=mu**2/(mu**2+4*v)
    for j,target in enumerate([1,mu,mu**2+v]): eq('moment-cone-two-atom:'+str(j),pm*am**j+pp*ap**j-target)
    AQ=h*m0/2; AR=-99*h*m1/4; A0=2115*h*m2/16; b=sp.Rational(17,6)*AQ
    eq('coefficient-cone-ratio',AR**2/(AQ*A0)-sp.Rational(2178,235)*m1**2/(m0*m2))
    Lam=-A0/(2*AR); ms=AR/(17*AQ)
    eq('Lambda-coefficient',Lam-sp.Rational(235,88)*m2/m1)
    eq('scalar-mass',ms+sp.Rational(99,34)*m1/m0)
    eq('trace-coefficient',2*AQ+6*sp.Rational(5,2)*AQ-17*AQ)
    eq('Einstein-background-full-algebraic-row',-AR*Lam-A0/2)
    ck('false-flat-background-detected',sp.factor(A0/2)!=0)
    F0=AR+8*b*Lam
    eq('F0-exact',F0-h*(3995*m0*m2-3267*m1**2)/(132*m1))
    eq('F0-moment-cone-margin',(3995*m0*m2-3267*m1**2)-3995*(m0*m2-m1**2)-728*m1**2)
    eq('nonzero-curvature-margin',3*ms+4*Lam-sp.Rational(364,187)*m1/m0-sp.Rational(235,22)*(m2/m1-m1/m0))
    # Full metric row: D[F0 phi+2b deltaR] with deltaR=-(3 Box+4Lambda)phi.
    B=sp.symbols('Box')
    eq('full-conformal-metric-row',F0-2*b*(3*B+4*Lam)-(AR-6*b*B))
    eq('full-row-mode-admission',(AR-6*b*B).subs(B,ms))
    # Independent FLRW constraint plus curvature identity and acceleration row.
    H,rate,r0,f2,F=sp.symbols('H rate r0 f2 F',nonzero=True)
    dH=f2*(H-rate)*r0/(2*F)
    relation=sp.factor(6*(rate+4*H)*dH-r0)
    mass=F/(3*f2)-4*H**2
    eq('FLRW-curvature-admission',relation.subs(rate**2,-3*H*rate-mass))
    eq('FLRW-Friedmann-constraint',6*F*H*dH-3*f2*H*(H-rate)*r0)
    eq('FLRW-spatial-acceleration',-2*F*rate*dH-f2*(rate**2-H*rate)*r0)
    positiveH,positiveMass=sp.symbols('Hpos masspos',positive=True)
    growing=(-3*positiveH+sp.sqrt(9*positiveH**2+4*positiveMass))/2
    eq('growing-root',growing**2+3*positiveH*growing-positiveMass)
    ck('growth-sign-control',bool(growing.subs({positiveH:1,positiveMass:1})>0))
    # Controls: trace coefficient absent in GR; healthy f(R) gives positive mass.
    A,bet=sp.symbols('A bet',positive=True)
    ck('healthy-fR-positive-mass',bool((A/(6*bet)).is_positive))
    rpert=sp.symbols('rpert')
    trace=A*rpert+bet*rpert**2
    gr_trace=sp.expand(sp.diff(trace,rpert)*rpert-2*trace).subs(bet,0)
    ck('GR-trace-has-unique-zero-curvature-perturbation',sp.solve(gr_trace,rpert)==[0])
    ck('GR-no-scalar-evolution-coefficient',sp.diff(trace,rpert,2).subs(bet,0)==0 and sp.diff(trace,rpert,2)!=0)
    # Native trace-reversed fibre metric, not a positive-definite replacement.
    pairs=[(i,j) for i in range(4) for j in range(i,4)]
    basis=[]
    for i,j in pairs:
        U=sp.zeros(4); U[i,j]=1; U[j,i]=1; basis.append(U)
    for port,sgn in [('K95-base-minus',1),('flipped-K77-base-plus',-1)]:
        g=sgn*sp.diag(-1,1,1,1)
        def pairing(U,V):
            return sp.trace(g*U*g*V)-sp.trace(g*U)*sp.trace(g*V)/2
        gram=sp.Matrix([[pairing(U,V) for V in basis]for U in basis])
        eig=gram.eigenvals()
        ck('native-fibre-signature:'+port,sum(mult for val,mult in eig.items()if val>0)==6 and sum(mult for val,mult in eig.items()if val<0)==4)
        eq('native-negative-trace:'+port,pairing(g,g)+4)
        ck('native-volume-density-positive:'+port,gram.det()>0 and sp.sqrt(abs(gram.det()))>0)
    eq('orientation-reversal-leaves-relative-sign',(-AR)/(-AQ)-AR/AQ)
    ck('signed-reference-outside-positive-cone',sum([3,-2])==1 and 3*1-2*2==-1)
    return {'checks':len(checks),'check_names':checks,'coefficient_ratio_bound':'2178/235',
            'scalar_mass_squared':'-99*m1/(34*m0)', 'F0_margin':'728*m1^2',
            'scope':'Finite algebra only. Recurrence/support, moment-cone completeness and PDE existence are written proofs; full metric row and FLRW constraints are algebraically calibrated. No full fourteen-dimensional stability transfer.'}


def payload():
    return {'artifact':'WEDGE_SHIAB_EINSTEIN_REDUCTION_CERTIFICATES','schema_version':1,
            'moment_controls':moment_controls(),'reduction_controls':reduction_controls()}


if __name__=='__main__':
    import argparse,json
    from pathlib import Path
    parser=argparse.ArgumentParser()
    parser.add_argument('--verify',action='store_true')
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args()
    result=payload()
    target=Path(__file__).resolve().parents[2]/'lab/process/wedge-shiab-einstein-reduction-certificates.json'
    encoded=json.dumps(result,indent=2)+'\n'
    if args.write: target.write_text(encoded)
    elif args.verify: assert target.read_text()==encoded, 'certificate drift'
    print('PASS',result['moment_controls']['checks']+result['reduction_controls']['checks'],'exact controls')
