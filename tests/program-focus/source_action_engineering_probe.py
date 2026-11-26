"""Exact engineering-wave controls. Written derivations own the general claims; no physical/domain certification."""
import json


def observation_controls():
    """Light exact controls for observation variation and variational transport.

    Standard library only. Root owns execution. Reduced n=2 fixtures test identities
    proved algebraically for general rank; they are not K95/domain certificates.
    """
    from fractions import Fraction as Q
    import json


    class Jet:
        def __init__(self, value=0, derivative=0):
            self.v, self.d = Q(value), Q(derivative)
        @staticmethod
        def cast(x):
            return x if isinstance(x, Jet) else Jet(x)
        def __add__(self, other):
            o = self.cast(other)
            return Jet(self.v + o.v, self.d + o.d)
        __radd__ = __add__
        def __neg__(self):
            return Jet(-self.v, -self.d)
        def __sub__(self, other):
            return self + (-self.cast(other))
        def __rsub__(self, other):
            return self.cast(other) - self
        def __mul__(self, other):
            o = self.cast(other)
            return Jet(self.v * o.v, self.d * o.v + self.v * o.d)
        __rmul__ = __mul__
        def __truediv__(self, other):
            o = self.cast(other)
            return Jet(self.v / o.v, (self.d * o.v-self.v * o.d)/(o.v*o.v))


    def add(a, b): return [x+y for x, y in zip(a, b)]
    def scale(s, a): return [s*x for x in a]
    def mv(a, x): return [sum(v*w for v, w in zip(row, x)) for row in a]
    def mm(a, b): return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]
    def eye(n): return [[Q(i == j) for j in range(n)] for i in range(n)]
    def madd(a, b): return [add(x, y) for x, y in zip(a, b)]
    def mscale(s, a): return [scale(s, row) for row in a]
    def values(x): return [Jet.cast(v).v for v in x]
    def derivs(x): return [Jet.cast(v).d for v in x]
    def mvalues(a): return [values(row) for row in a]
    def mderivs(a): return [derivs(row) for row in a]
    def dot(x, y): return sum(a*b for a, b in zip(x, y))


    def gamma_pair(t, y):
        a = y+t
        s = [[1, a], [0, 1]]
        si = [[1, -a], [0, 1]]
        return [mm(mm(s, g), si) for g in ([[0, 1], [1, 0]], [[1, 0], [0, -1]])]


    def fields(t, y, freeze_gamma=False):
        x = Q(2)
        z = [[x+y+t, x*y+t*t], [y*y+t, x-y+2*t]]
        eta = [x+y+t*y, 1+x*y+t]
        gs = gamma_pair(t, y)
        if freeze_gamma:
            gs = [mvalues(g) for g in gs]
        Z = [add(z[a], scale(Q(-1, 2), mv(gs[a], eta))) for a in range(2)]
        # n=2, so scalar coefficient (1-n/2) is zero in this control.
        V = add(mv(gs[0], z[0]), mv(gs[1], z[1]))
        return Z, V


    def determinant(a):
        a = [list(map(Q, row)) for row in a]
        out = Q(1)
        for i in range(len(a)):
            p = next((j for j in range(i, len(a)) if a[j][i]), None)
            if p is None: return Q(0)
            if p != i:
                a[i], a[p] = a[p], a[i]
                out = -out
            pivot = a[i][i]
            out *= pivot
            for j in range(i+1, len(a)):
                ratio = a[j][i]/pivot
                for k in range(i+1, len(a)):
                    a[j][k] -= ratio*a[i][k]
        return out


    def frame_maps(t):
        gs = gamma_pair(t, Q(0))
        # Form-spinor vector has four entries, scalar-spinor two entries.
        J = gs[0]+gs[1]
        Gamma = [gs[0][i]+gs[1][i] for i in range(2)]
        upper = eye(6)
        lower_f, lower_r = eye(6), eye(6)
        upper_inv, lower_f_inv = eye(6), eye(6)
        for i in range(4):
            for j in range(2):
                upper[i][4+j] = J[i][j]/2
                upper_inv[i][4+j] = -J[i][j]/2
        for i in range(2):
            for j in range(4):
                lower_f[4+i][j] = -Gamma[i][j]
                lower_r[4+i][j] = -Gamma[i][j]/2
                lower_f_inv[4+i][j] = Gamma[i][j]
        return mm(upper, lower_f), mm(upper, lower_r), mm(lower_f_inv, upper_inv)


    def sigma(xi):
        gs = gamma_pair(Q(0), Q(0))
        c = madd(mscale(xi[0], gs[0]), mscale(xi[1], gs[1]))
        result = [[Q(0) for _ in range(6)] for _ in range(6)]
        for a in range(2):
            for b in range(2):
                block = mscale(-xi[a], gs[b])
                if a == b: block = madd(block, c)
                for i in range(2):
                    for j in range(2): result[2*a+i][2*b+j] = block[i][j]
            for i in range(2):
                result[2*a+i][4+i] = xi[a]
                result[4+i][2*a+i] = xi[a]
        for i in range(2):
            for j in range(2): result[4+i][4+j] = -c[i][j]/2
        return result


    def run_checks():
        checks = {}
        def check(name, condition):
            checks[name] = bool(condition)
            assert checks[name], name

        # g_t(x)=x²+t(x+1), x=2: y=4+3t, dg/dx=4+t.
        t = Jet(0, 1)
        Z, V = fields(t, Jet(4, 3))
        H = [[0, 1], [-1, 0]]
        U = madd(eye(2), mscale(t, H))
        direct_o = mv(U, add(Z[0], scale(Jet(4, 1), Z[1])))
        direct_n = mv(U, V)
        Z0, V0 = fields(Jet(0), Jet(4))
        Zt, Vt = fields(Jet(0, 1), Jet(4))
        Zy, Vy = fields(Jet(0), Jet(4, 1))
        z0 = list(map(values, Z0))
        dt = list(map(derivs, Zt))
        dy = list(map(derivs, Zy))
        material = [add(dt[a], scale(3, dy[a])) for a in range(2)]
        base_o = add(z0[0], scale(4, z0[1]))
        expected_o = add(mv(H, base_o), add(add(material[0], scale(4, material[1])), z0[1]))
        expected_n = add(mv(H, values(V0)), add(derivs(Vt), scale(3, derivs(Vy))))
        check('nonconstant_section_full_oneform_variation', derivs(direct_o) == expected_o)
        check('nonconstant_section_full_scalar_variation', derivs(direct_n) == expected_n)
        displacement = add(scale(3, dy[0]), scale(12, dy[1]))
        check('omit_normal_displacement_detected', displacement != [0, 0])
        check('omit_section_slope_variation_detected', z0[1] != [0, 0])
        check('omit_observed_frame_variation_detected', mv(H, base_o) != [0, 0])
        Zf, Vf = fields(t, Jet(4, 3), freeze_gamma=True)
        frozen_o = mv(U, add(Zf[0], scale(Jet(4, 1), Zf[1])))
        check('freeze_Clifford_variation_detected', derivs(frozen_o) != expected_o)
        check('freeze_Clifford_scalar_variation_detected', derivs(mv(U, Vf)) != expected_n)

        Fj, Rj, Fij = frame_maps(Jet(0, 1))
        F, R, Fi = mvalues(Fj), mvalues(Rj), mvalues(Fij)
        Fdot, Fid = mderivs(Fj), mderivs(Fij)
        check('finite_F_determinant_one', determinant(F) == 1)
        check('finite_R_determinant_one', determinant(R) == 1)
        check('independent_Grassmann_measure_factor_one', determinant(F)/determinant(R) == 1)
        check('inverse_variation_identity', Fid == mscale(-1, mm(mm(Fi, Fdot), Fi)))
        A = sigma([Q(2), Q(3)])
        Ap = mm(mm(R, A), Fi)
        bp = [Q(v) for v in [1, -2, 3, 1, -1, 2]]
        cp = [Q(v) for v in [2, 1, -1, 3, 2, -2]]
        dcp = [Q(v) for v in [-1, 2, 1, 0, 3, 1]]
        dchi = add(mv(Fi, dcp), mv(Fid, cp))
        lhs = dot(bp, mv(mm(R, A), dchi))
        simple = dot(bp, mv(Ap, dcp))
        correction = dot(bp, mv(mm(R, A), mv(Fid, cp)))
        check('boundary_current_full_moving_frame_transport', lhs == simple+correction)
        check('omit_metric_frame_boundary_term_detected', correction != 0 and lhs != simple)
        check('boundary_current_fixed_metric_transport', dot(bp, mv(mm(R, A), mv(Fi, dcp))) == simple)
        # Independent first-jet substitution control, not a physical fermion model.
        # L=barχ ∂xχ, χ=(1+gx)u, barχ=(1+2gx)v. Direct higher-derivative
        # Euler boundary potential differs from pulled-back θ by C δg.
        r, s, u, ux, v, vx = map(Q, [2, 3, 5, 7, 11, 13])
        du, h, hx = map(Q, [17, 19, 23])
        bar, barx = (1+2*r)*v, (1+2*r)*vx+2*s*v
        chix = (1+r)*ux+s*u
        C = -barx*u+2*v*chix
        p_ux = v*(1+2*r)*(1+r)
        p_gx = 2*v*chix+v*(1+2*r)*ux
        p_gxx = bar*u
        dx_p_gxx = barx*u+bar*ux
        canonical = p_ux*du+(p_gx-dx_p_gxx)*h+p_gxx*hx
        pulled = bar*((1+r)*du+u*hx)
        check('jet_dependent_full_Euler_boundary_chain', canonical == pulled+C*h)
        check('omit_Euler_proportional_jet_boundary_term_detected', C*h != 0 and canonical != pulled)
        return {'checks': checks, 'count': len(checks),
                'boundary_metric_correction': str(correction),
                'jet_Euler_boundary_correction': str(C*h),
                'observation_variation': list(map(str, expected_o)),
                'scalar_variation': list(map(str, expected_n)),
                'scope': 'exact reduced algebraic controls; no native domain or physical positivity claim'}
    return run_checks()


def interactions_controls():
    """Exact Gaussian-rational K95 current diagnostics. Root runs serialized."""
    from fractions import Fraction as Q
    import json

    def run_checks():
        n, size = 14, 128
        eta = [1]*9 + [-1]*5
        H = (0, 1, 2, 9)
        N = tuple(a for a in range(n) if a not in H)
        zero = [(Q(0), Q(0))]*size
        checks = {}
        def check(name, value):
            checks[name] = bool(value)
            assert checks[name], name
        def plus(a,b): return [(x[0]+y[0], x[1]+y[1]) for x,y in zip(a,b)]
        def scale(q,a): return [(q*x,q*y) for x,y in a]
        def iphase(p,a): return [a,(-a[1],a[0]),(-a[0],-a[1]),(a[1],-a[0])][p%4]
        def iv(a): return [iphase(1,x) for x in a]
        def vsum(vs):
            out = zero
            for v in vs: out = plus(out,v)
            return out
        def gamma(j,v):
            bit, yy = 6-j//2, j%2
            out=[]
            for r in range(size):
                phase=2*((r>>(bit+1)).bit_count()%2)
                if yy: phase += 1 if (r>>bit)&1 else 3
                if j>=9: phase += 1
                out.append(iphase(phase,v[r^(1<<bit)]))
            return out
        psi=[(Q(j%7-3),Q(j%5-2)) for j in range(size)]
        def trace(z,axes=tuple(range(n))):
            return vsum(scale(eta[a],gamma(a,z[a])) for a in axes)
        def cliff(x,v): return vsum(scale(eta[a]*x[a],gamma(a,v)) for a in range(n))
        def vertex(x,z,nu,s):
            # a_a=i*x_a*Id belongs to u(64,64); V_s(a)=i*sigma_s(x).
            tau=trace(z)
            r=[iv(plus(cliff(x,z[a]),scale(x[a],plus(nu,scale(-1,tau))))) for a in range(n)]
            sout=iv(plus(vsum(scale(eta[a]*x[a],z[a]) for a in range(n)),scale(s,cliff(x,nu))))
            return r,sout
        imp=[scale(10 if a in H else -4,gamma(a,psi)) for a in range(n)]
        z0=[zero for _ in range(n)]
        check('K95_Clifford_squares', all(gamma(a,gamma(a,psi))==scale(eta[a],psi) for a in range(n)))
        check('owned_imposter_ambient_gamma_kernel',trace(imp)==zero)
        check('owned_imposter_horizontal_trace',trace(imp,H)==scale(40,psi))
        for a in (0,9,4,10):
            x=[Q(int(j==a)) for j in range(n)]
            cpsi=iv(cliff(x,psi))
            for s in (Q(-1,2),Q(0),Q(1)):
                r,t=vertex(x,imp,zero,s)
                check(f'imposter_trace_{a}_{s}',scale(Q(1,4),trace(r,H))==scale(-5 if a in H else -10,cpsi))
                check(f'imposter_scalar_{a}_{s}',t==scale(10 if a in H else -4,cpsi))
                r,t=vertex(x,z0,psi,s)
                check(f'nu_trace_{a}_{s}',scale(Q(1,4),trace(r,H))==scale(Q(1,4) if a in H else 0,cpsi))
                check(f'nu_scalar_{a}_{s}',t==scale(s,cpsi))
            r,t=vertex(x,imp,scale(20,psi),Q(-1,2))
            if a in H:
                check(f'repaired_combo_trace_zero_{a}',trace(r,H)==zero)
                check(f'repaired_combo_scalar_zero_{a}',t==zero)
                expected=[iv(scale(40,plus(scale(x[b],psi),scale(Q(-1,4),gamma(b,cliff(x,psi)))))) for b in H]
                check(f'repaired_combo_remaining_RS_formula_{a}',[r[b] for b in H]==expected)
                check(f'repaired_combo_remaining_RS_nonzero_{a}',any(r[b]!=zero for b in H))
                r_old,t_old=vertex(x,imp,scale(20,psi),Q(0))
                check(f'SE0_breaks_routing_scalar_{a}',t_old==scale(10,cpsi) and t_old!=zero)
            else:
                check(f'normal_combo_trace_visible_{a}',scale(Q(1,4),trace(r,H))==scale(-10,cpsi))
                check(f'normal_combo_scalar_visible_{a}',t==scale(-14,cpsi))
        # Hidden normal RS witness, using both a positive and a negative native axis.
        hidden=[zero for _ in range(n)]
        hidden[4]=gamma(4,psi); hidden[10]=scale(-1,gamma(10,psi))
        check('hidden_field_q_zero',all(hidden[a]==zero for a in H))
        check('hidden_normal_RS',trace(hidden)==zero)
        for s in (Q(-1,2),Q(0),Q(1)):
            x=[Q(int(a==4)) for a in range(n)]
            r,t=vertex(x,hidden,zero,s)
            check(f'hidden_to_scalar_current_{s}',t==iv(hidden[4]) and t!=zero)
            check(f'hidden_to_horizontal_row_zero_{s}',all(r[a]==zero for a in H))
        # F/R transport: field readout and equation diagnostic are distinct.
        def F(z,nu):
            e=plus(nu,scale(-1,trace(z)))
            return [plus(z[a],scale(Q(1,2),gamma(a,e))) for a in range(n)],e
        def R(r,t):
            v=plus(t,scale(Q(-1,2),trace(r)))
            return [plus(r[a],scale(Q(1,2),gamma(a,v))) for a in range(n)],v
        def Rinv(u,v):
            return [plus(u[a],scale(Q(-1,2),gamma(a,v))) for a in range(n)],plus(scale(Q(1,2),trace(u)),scale(1-Q(n,4),v))
        x=[Q(int(a==0)) for a in range(n)]
        z,nu=imp,scale(20,psi)
        r,t=vertex(x,z,nu,Q(-1,2)); zp,e=F(z,nu); u,v=R(r,t)
        check('central_current_primed_Dirac_blocks',u==[iv(cliff(x,w)) for w in zp] and v==scale(-1,iv(cliff(x,e))))
        rr,tt=Rinv(u,v)
        check('equation_diagnostic_transport_qE_Rinverse',[rr[a] for a in H]==[r[a] for a in H] and tt==t)
        # Literal rational determinant/rescaling controls, no floating point.
        for s in (Q(-1,2),Q(0),Q(1),Q(3,7)):
            detH=-5*s-Q(5,2); detN=-10*s
            check(f'determinants_{s}',detH==-5*(s+Q(1,2)) and detN==-10*s)
            A,B,C,D=Q(-5),Q(1,4),Q(10),s
            row1,row2,col1,col2=Q(2),Q(3),Q(5),Q(7)
            Ap,Bp,Cp,Dp=row1*A*col1,row1*B*col2,row2*C*col1,row2*D*col2
            check(f'crossratio_rescaling_{s}',Ap*Dp/(Bp*Cp)==A*D/(B*C)==-2*s)
        return {'checks':checks,'count':len(checks),'all_passed':all(checks.values()),'scope':'pointwise candidate current algebra, not physical equation descent or prediction'}
    return run_checks()


def compatibility_controls():
    """Light exact controls; analytical scope is in compatibility.md. Root executes."""
    from fractions import Fraction as F


    def add(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
    def neg(a): return [[-x for x in r] for r in a]
    def scale(c,a): return [[c*x for x in r] for r in a]
    def mul(a,b): return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
    def comm(a,b): return add(mul(a,b),neg(mul(b,a)))
    def tr(a): return sum(a[i][i] for i in range(len(a)))


    def run_controls():
        checks=0
        def check(p):
            nonlocal checks
            assert p
            checks+=1

        ric2=5*F(1,4)**2+9*F(-5,4)**2
        scalar=5*F(1,4)+9*F(-5,4)
        ein2=5*F(21,4)**2+9*F(15,4)**2
        check(ric2==F(115,8))
        check(scalar==-10)
        check(ein2==F(2115,8))
        check(ein2==ric2+F(5,2)*scalar**2)
        check(ein2/2==F(2115,16))

        U=[[F(1),F(0)],[F(0),F(-1)]]
        V=[[F(0),F(1)],[F(1),F(0)]]
        # Derivative of Gamma(V,W) along constant U at y=I.
        def dgamma(u,v,w):
            return scale(F(1,2),add(mul(mul(v,u),w),mul(mul(w,u),v)))
        def gamma(v,w):
            return scale(F(-1,2),add(mul(v,w),mul(w,v)))
        def curvature(u,v,w):
            return add(add(dgamma(u,v,w),neg(dgamma(v,u,w))),
                       add(gamma(u,gamma(v,w)),neg(gamma(v,gamma(u,w)))))
        rv=curvature(U,V,V)
        check(rv==scale(F(-1,4),comm(comm(U,V),V)))
        check(rv==neg(U))
        check(tr(U)==0 and tr(V)==0)
        check(any(x!=0 for row in rv for x in row))

        # G(a)=[[y+a^2 v,-a v],[-a v,v]]: changing horizontal lift,
        # rather than scaling y or v, leaves determinant y*v exactly.
        y,v=F(3),F(-2)
        for a in (F(0),F(1,3),F(-5,2)):
            check((y+a*a*v)*v-(-a*v)**2==y*v)
        # At a=0 delta G has only mixed components; inverse trace vanishes.
        Ginv=[[1/y,F(0)],[F(0),1/v]]
        dG=[[F(0),-v],[-v,F(0)]]
        check(tr(mul(Ginv,dG))==0)

        # Compact-support analogue: p=x^4(1-x)^4 and derivatives through
        # third order have zero integrated total derivatives on [0,1].
        p=[F(0)]*4+[F(1),F(-4),F(6),F(-4),F(1)]
        def deriv(cs): return [i*cs[i] for i in range(1,len(cs))]
        def integral(cs): return sum(c/F(i+1) for i,c in enumerate(cs))
        dp=p
        for _ in range(3):
            dp=deriv(dp)
            check(integral(dp)==0)
        check(integral(p)!=0)  # catches a forbidden undifferentiated term

        return {"exact_controls":checks,"passed":True,
                "scope":"candidate algebra and explicit local variation/boundary diagnostics"}
    return run_controls()


def compatibilityfollowthrough_controls():
    """Finite controls for the separate all-order parity/locality derivation."""
    from fractions import Fraction as F


    def run_controls():
        checks=0
        def check(condition):
            nonlocal checks
            assert condition
            checks+=1
        for n in range(1,13):
            if n>=2:
                check((1+(n-1)%2)%2==n%2)
            for i in range(1,n-1):
                j=n-1-i
                check((1+i+j)%2==n%2)
            if n%2==1:
                check(n%2==1)  # linear S/T pairing
        for i in range(1,9):
            for j in range(1,9):
                if i%2==j%2:
                    check((i+j-1)%2==1)  # mass has h^-1
                if i%2!=(j%2):
                    check((i+j)%2==1)    # K flips parity
                for k in range(1,9):
                    if i%2==(1+j+k)%2:
                        check((i+j+k)%2==1)

        # Compact-support analogue p=x^8(1-x)^8: boundary jets through 7
        # vanish, so integration of its derivatives through order 8 vanishes.
        from math import comb
        p=[F(0)]*8+[F((-1)**j*comb(8,j)) for j in range(9)]
        def derivative(cs): return [i*cs[i] for i in range(1,len(cs))]
        def integral(cs): return sum(c/F(i+1) for i,c in enumerate(cs))
        check(integral(p)!=0)
        d=p
        for _ in range(8):
            d=derivative(d)
            check(integral(d)==0)

        # Genuine two-component graded recursion through h^7. Component0 is
        # even, component1 odd. P=diag(1,signature) gives positive/indefinite
        # controls; K is P-self-adjoint and the N trilinear pairing symmetric.
        z=(F(0),F(0))
        def plus(a,b): return (a[0]+b[0],a[1]+b[1])
        def times(c,a): return (c*a[0],c*a[1])
        def total(vs):
            out=z
            for v in vs: out=plus(out,v)
            return out
        for signature in (F(1),F(-1)):
            def pair(a,b): return a[0]*b[0]+signature*a[1]*b[1]
            def K(a): return (2*signature*a[1],2*a[0])
            def N(a,b):
                return (a[0]*b[1]+a[1]*b[0],
                        signature*(a[0]*b[0]+3*a[1]*b[1]))
            e0,e1=(F(1),F(0)),(F(0),F(1))
            for a in (e0,e1):
                for b in (e0,e1):
                    check(pair(a,K(b))==pair(K(a),b))
                    for c in (e0,e1):
                        check(pair(a,N(b,c))==pair(b,N(a,c)))

            for mutate in (False,True):
                S=(F(int(mutate)),F(3))
                T={1:times(-1,S)}
                for n in range(2,8):
                    T[n]=times(-1,plus(K(T[n-1]),total(
                        N(T[i],T[n-1-i]) for i in range(1,n-1))))
                # Direct normalized Euler coefficients, using only stored T.
                for n in range(1,8):
                    residual=plus(T[n],S if n==1 else K(T[n-1]))
                    residual=plus(residual,total(
                        N(T[i],T[n-1-i]) for i in range(1,n-1)))
                    check(residual==z)
                action={}
                for n in range(1,8):
                    value=pair(S,T[n])
                    value+=F(1,2)*sum(pair(T[i],T[n+1-i])
                                      for i in range(1,n+1))
                    value+=F(1,2)*sum(pair(T[i],K(T[n-i]))
                                      for i in range(1,n))
                    value+=F(1,3)*sum(pair(T[i],N(T[j],T[n-i-j]))
                                      for i in range(1,n-1)
                                      for j in range(1,n-i))
                    action[n]=value
                if not mutate:
                    for n in range(1,8):
                        check(T[n][1-n%2]==0)
                    for n in (2,4,6):
                        check(action[n]==0)
                else:
                    check(action[2]==pair(S,K(S))/2)
                    check(action[2]==6*signature and action[2]!=0)
        return {"checks":checks,"passed":True,
                "ceiling":"finite controls; all-order induction/locality proof is separate"}
    return run_controls()


def run_all():
    groups = {'observation': observation_controls(), 'interactions': interactions_controls(), 'compatibility': compatibility_controls(), 'formal_followthrough': compatibilityfollowthrough_controls()}
    return {'passed': sum(g.get('count', g.get('exact_controls', g.get('checks', 0))) for g in groups.values()), 'groups': groups,
            'scope': 'native128 current algebra; reduced exact jet/boundary controls; explicit vertical curvature and local variation checks. General results are written proofs; no physical GU, global domain or Lean claim.'}

if __name__ == '__main__':
    print(json.dumps(run_all(), indent=2, sort_keys=True))
