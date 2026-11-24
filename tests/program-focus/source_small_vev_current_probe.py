#!/usr/bin/env python3
"""Small exact controls for the written all-dimension primitive-current proof.

Root owns serialized execution. No source action, physical norm or fluctuation
propagator is constructed. The finite matrix is a parity/sharp-law control;
the n=64 ranks follow from T^2=-I in the written proof.
"""

import argparse
from collections import Counter
import json
from pathlib import Path

import sympy as s
from sympy.physics.matrices import mgamma


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output")
    args = ap.parse_args()
    checks = []

    def check(name, condition):
        passed = bool(condition)
        checks.append({"name": name, "passed": passed})
        if not passed:
            raise AssertionError(name)

    i2, z2 = s.eye(2), s.zeros(2)
    om = s.diag(i2, -i2)
    k = s.Matrix.vstack(s.Matrix.hstack(z2, i2),
                        s.Matrix.hstack(i2, z2))
    t_mix = s.I * k
    weak2 = s.diag(s.I, -s.I)
    t_weak = s.diag(weak2, weak2)
    i4, z4 = s.eye(4), s.zeros(4)

    def sharp(t):
        return k * t.conjugate().T * k

    check("K95 volume skew-adjoint involution", om**2 == i4 and sharp(om) == -om)
    check("odd generator belongs to actual u(K)", sharp(t_mix) == -t_mix)
    check("odd generator invertible on both halves", t_mix**2 == -i4)
    check("odd generator exchanges Omega halves", om*t_mix + t_mix*om == z4)
    check("weak generator belongs to u(K)", sharp(t_weak) == -t_weak)
    check("geometric weak parity even", om*t_weak - t_weak*om == z4)

    # Two form slots and one scalar slot. This is an algebraic control, not
    # a replacement for the actual fourteen-dimensional exterior operator.
    g = s.diag(om, om, -om)
    density = s.diag(k, k, k)
    ident = s.eye(12)
    p_plus, p_minus = (ident+g)/2, (ident-g)/2

    def response(t, include_nw=False):
        ne = s.Matrix.vstack(t, z4)    # xi=e1 retained by literal b readout
        sw = s.Matrix.hstack(-t, z4)  # negative formal-adjoint-shaped cross slot
        nw = s.zeros(8)
        if include_nw:
            # One Omega-odd contraction coefficient, enough to check parity.
            nw = s.Matrix.vstack(s.Matrix.hstack(z4, k*t),
                                  s.Matrix.hstack(-k*t, z4))
        return s.Matrix.vstack(s.Matrix.hstack(nw, ne),
                               s.Matrix.hstack(sw, z4))

    v_even, v_odd = response(t_weak, True), response(t_mix, True)
    zero = s.zeros(12)
    check("even current response is G-odd", g*v_even+v_even*g == zero)
    check("odd current response is G-even", g*v_odd-v_odd*g == zero)
    j_even, j_odd = density*v_even, density*v_odd
    check("same-sector weak bilinear", g.conjugate().T*j_even-j_even*g == zero)
    check("opposite-sector parent bilinear", g.conjugate().T*j_odd+j_odd*g == zero)
    check("weak opposite-sector blocks vanish",
          p_plus.conjugate().T*j_even*p_minus == zero
          and p_minus.conjugate().T*j_even*p_plus == zero)
    check("odd same-sector blocks vanish",
          p_plus.conjugate().T*j_odd*p_plus == zero
          and p_minus.conjugate().T*j_odd*p_minus == zero)
    check("odd mixed block survives", p_plus.conjugate().T*j_odd*p_minus != zero)

    half_plus, half_minus = (i4+om)/2, (i4-om)/2
    check("literal horizontal NE is injective", t_mix.rank() == 4)
    check("NE rank per ambient half", (t_mix*half_plus).rank() == 2
          and (t_mix*half_minus).rank() == 2)

    epsilon, fluctuation = s.symbols("epsilon fluctuation", real=True)
    vertex = (epsilon+fluctuation)*t_mix
    derivative = vertex.diff(fluctuation)
    check("zero VEV does not remove derivative", derivative.subs(epsilon, 0) == t_mix)
    check("small actual fluctuation does suppress vertex",
          vertex.subs(epsilon, 0) == fluctuation*t_mix)
    # Contrary controls distinguish the actual u(K) sharp law from an
    # arbitrary spin matrix and opposite-half density from a positive form.
    check("bad sharp-law plant rejected", sharp(k) != -k)
    check("positive density is not same sector law",
          g.conjugate().T*v_even-v_even*g != zero)

    # Reused source normal16 charge table, not a family multiplicity census.
    f = Counter({("3", 2, 1): 1, ("3bar", 1, 2): 1,
                 ("3bar", 1, -4): 1, ("1", 2, -3): 1,
                 ("1", 1, 6): 1, ("1", 1, 0): 1})
    conj_color = {"3": "3bar", "3bar": "3", "1": "1"}
    fbar = Counter({(conj_color[c], w, -y): m
                    for (c, w, y), m in f.items()})
    color_dim = {"3": 3, "3bar": 3, "1": 1}

    def dimension(rep):
        return sum(color_dim[c]*w*m for (c, w, _), m in rep.items())

    check("normal dimensions balanced", dimension(f) == dimension(fbar) == 16)
    common = f & fbar
    check("only sterile irrep common", common == Counter({("1", 1, 0): 1}))
    difference = {r: f[r]-fbar[r] for r in set(f) | set(fbar)
                  if f[r] != fbar[r]}
    check("charge-resolved chirality nonzero", len(difference) == 10)
    check("RH conjugate is not same-charge mirror", fbar[("3bar", 2, -1)] == 1
          and fbar[("3", 2, 1)] == 0)

    def forget_to_weak(rep):
        out = Counter()
        for (color, weak, _), mult in rep.items():
            out[weak] += color_dim[color]*mult
        return out

    check("weak-only characters lose the chiral distinction",
          forget_to_weak(f) == forget_to_weak(fbar) == Counter({2: 4, 1: 8}))

    # New supplement: actual sharp-skew intersection on the already-owned
    # sterile Hom space. Both normal pairing sign choices are checked; the
    # written formula holds for arbitrary nonzero real d_+,d_-.
    normal_chi = s.diag(1, -1)
    omega_st = s.diag(s.kronecker_product(i2, normal_chi),
                     -s.kronecker_product(i2, normal_chi))
    for normal_sign in (1, -1):
        normal_density = s.diag(1, normal_sign)
        cross_density = s.kronecker_product(i2, normal_density)
        k_st = s.Matrix.vstack(s.Matrix.hstack(z4, cross_density),
                               s.Matrix.hstack(cross_density, z4))

        def sterile_generator(b, c):
            left = s.Matrix([[0, b], [c, 0]])
            right = -normal_density.inv()*left.conjugate().T*normal_density
            return s.diag(s.kronecker_product(i2, left),
                          s.kronecker_product(i2, right))

        basis = [sterile_generator(1, 0), sterile_generator(s.I, 0),
                 sterile_generator(0, 1), sterile_generator(0, s.I)]
        check(f"sterile parent sharp law sign {normal_sign}",
              all(t.conjugate().T*k_st+k_st*t == s.zeros(8) for t in basis))
        check(f"sterile generators Omega-odd sign {normal_sign}",
              all(omega_st*t+t*omega_st == s.zeros(8) for t in basis))
        real_columns = []
        for t in basis:
            entries = list(t)
            real_columns.append(s.Matrix([s.re(x) for x in entries]
                                          + [s.im(x) for x in entries]))
        check(f"sterile sharp intersection four real parameters sign {normal_sign}",
              s.Matrix.hstack(*real_columns).rank() == 4)
        check(f"sterile possible ranks sign {normal_sign}",
              [sterile_generator(b, c).rank() for b, c in ((0, 0), (1, 0), (1, 1))]
              == [0, 4, 8])
        bad_right = s.diag(s.kronecker_product(i2, s.Matrix([[0, 1], [0, 0]])), z4)
        check(f"independent unpaired right block rejected sign {normal_sign}",
              bad_right.conjugate().T*k_st+k_st*bad_right != s.zeros(8))

    # Whole one-form covariance control. These exact Cl(3,1) matrices have
    # the actual horizontal sharp type, and the normal spectator makes
    # Omega=chi_H chi_N. They do not stand in for a selected GU background.
    horizontal_gamma = [s.I*mgamma(a) for a in range(4)]
    horizontal_sign = [-1, 1, 1, 1]
    chi_h = mgamma(5)
    k_h = s.I*mgamma(0)*chi_h
    check("horizontal K is nondegenerate Hermitian", k_h.conjugate().T == k_h
          and k_h.det() != 0)
    check("horizontal Clifford type",
          all(horizontal_gamma[a]*horizontal_gamma[b]+horizontal_gamma[b]*horizontal_gamma[a]
              == (2*horizontal_sign[a]*s.eye(4) if a == b else s.zeros(4))
              for a in range(4) for b in range(4)))
    check("horizontal vectors sharp-selfadjoint",
          all(c.conjugate().T*k_h == k_h*c for c in horizontal_gamma))
    check("horizontal chirality sharp-skew", chi_h.conjugate().T*k_h == -k_h*chi_h)
    gamma_full = [s.kronecker_product(c, i2) for c in horizontal_gamma]
    k_full = s.kronecker_product(k_h, normal_chi)
    omega_full = s.kronecker_product(chi_h, normal_chi)
    alpha = [s.I*c for c in gamma_full]
    check("covariant one-form values in actual unitary parent",
          all(a.conjugate().T*k_full+k_full*a == s.zeros(8) for a in alpha))
    check("covariant one-form Omega-odd",
          all(omega_full*a+a*omega_full == s.zeros(8) for a in alpha))
    # Normal factor is arbitrary here; checking its matrix units confirms
    # the structural commutation argument for every normal group action.
    normal_units = []
    for row in range(2):
        for col in range(2):
            unit = s.zeros(2)
            unit[row, col] = 1
            normal_units.append(s.kronecker_product(s.eye(4), unit))
    check("covariant one-form commutes with every normal spectator action",
          all(a*u-u*a == s.zeros(8) for a in alpha for u in normal_units))
    tensor_covariance = []
    for a in range(4):
        for b in range(a+1, 4):
            generator = gamma_full[a]*gamma_full[b]/2
            for c in range(4):
                rhs = (horizontal_sign[b]*alpha[a] if c == b else s.zeros(8))
                rhs -= horizontal_sign[a]*alpha[b] if c == a else s.zeros(8)
                tensor_covariance.append(generator*alpha[c]-alpha[c]*generator == rhs)
    check("whole one-form Lorentz covariance", all(tensor_covariance))
    check("individual vector coefficient is not Lorentz scalar",
          (gamma_full[0]*gamma_full[1]/2)*alpha[0]
          - alpha[0]*(gamma_full[0]*gamma_full[1]/2) != s.zeros(8))
    j_h = s.Matrix.vstack(*gamma_full)
    gamma_h = s.Matrix.hstack(*[horizontal_sign[a]*gamma_full[a] for a in range(4)])
    check("observed one-form insertion has rank and trace witness",
          gamma_h*j_h == 4*s.eye(8) and j_h.rank() == 8)

    result = {
        "baseline": "14778ad8a4308d2d88357bba8a81819cedbc3f40",
        "classification": "source-authenticated vertex; physical response conditional",
        "checks": checks,
        "passed": all(row["passed"] for row in checks),
        "all_dimension_written_identity": "T_odd^2=-I implies rank 2n, rank n per Omega half",
        "n64_parent_even_real_dimension": 8192,
        "n64_parent_odd_real_dimension": 8192,
        "lorentz_scalar_SM_neutral_odd_sharp_dimension_real": 4,
        "lorentz_scalar_SM_neutral_odd_ranks": [0, 4, 8],
        "covariant_one_form_is_larger_than_scalar_generator_category": True,
        "physical_propagator_or_current_quotient_computed": False,
        "source_or_C_kill": False,
    }
    result["readout_controls"] = run_readout_controls()
    rendered = json.dumps(result, indent=2)
    if args.output:
        Path(args.output).write_text(rendered+"\n", encoding="utf-8")
    print(rendered)


#!/usr/bin/env python3
"""Exact finite witnesses for the effective-port bound and channel ceilings.
No optimization/rank sampling proves the universal theorem; see readout-bound.md.
Root executes serially. Matrices are at most8x8 with Gaussian-rational entries.
"""
import json
import sympy as s

def run_readout_controls():
    I2=s.eye(2); Z2=s.zeros(2); ii=s.I
    count=0

    def check(cond,label):
        nonlocal count
        assert bool(cond),label
        count+=1

    def eq(a,b):
        if isinstance(a,s.MatrixBase) or isinstance(b,s.MatrixBase):
            return a.shape==b.shape and all(s.simplify(z)==0 for z in a-b)
        return s.simplify(a-b)==0

    def unit(v): return eq((v.H*v)[0],1)

    def witness(u,v,lam):
        # lam is supplied exactly; this is a witness check, not numerical phase fitting.
        check(unit(u) and unit(v),"unit port vectors")
        check(eq(s.conjugate(lam)*lam,1),"unit phase")
        rho=(u.H*(lam*v))[0]
        check(eq(rho,s.conjugate(rho)),"phase-adjusted overlap real")
        w=u-lam*v
        H=I2 if eq(w,s.zeros(2,1)) else I2-2*w*w.H/(w.H*w)[0]
        C=ii*H
        check(eq(H.H,H) and eq(H*H,I2),"Hermitian Householder involution")
        check(eq(H*u,lam*v),"Householder transport")
        check(eq(C.H,-C) and eq(C*C,-I2),"admitted anti-Hermitian unitary direction")
        check(eq(C.H*C,I2),"direction norm one")
        amp=(v.H*C*u)[0]
        check(eq(amp,s.I*lam) and eq(s.conjugate(amp)*amp,1),"rank-one ports attain product")
        K=s.BlockMatrix([[Z2,I2],[I2,Z2]]).as_explicit()
        O=s.diag(1,1,-1,-1)
        T=s.BlockMatrix([[Z2,C],[C,Z2]]).as_explicit()
        check(eq(T.H*K+K*T,s.zeros(4)),"genuine real Krein-skew parent")
        check(eq(T*O+O*T,s.zeros(4)) and eq(T*T,-s.eye(4)),"odd invertible full-parent witness")
        return C

    u=s.Matrix([1,0]); v=s.Matrix([0,1])
    Csame=witness(u,u,s.Integer(1))
    Corth=witness(u,v,s.Integer(1))
    vc=s.Matrix([3*s.I/5,s.Rational(4,5)])
    Ccomplex=witness(u,vc,-s.I)

    # A fixed invertible direction can miss a response: quantifier is all directions.
    check(eq((v.H*(ii*I2)*u)[0],0),"restricted-support countercontrol")
    check(not eq((v.H*Corth*u)[0],0),"other admitted direction detects same ports")

    # Scaled, zero, and full-rank rectangular-port controls; norms known exactly.
    a=s.Rational(2,3); b=s.Rational(5,7)
    amp=(b*v.H*Corth*(a*u))[0]
    check(eq(s.conjugate(amp)*amp,(a*b)**2),"scaled product bound attained")
    check(eq(v.H*Corth*s.zeros(2,1),s.zeros(1,1)),"zero inclusion survivor")
    check(eq(s.zeros(1,2)*Corth*u,s.zeros(1,1)),"zero effective row survivor")
    Inc=s.diag(2,1); Row=s.diag(1,3); Out=Row*Corth*Inc
    check(eq(Out.H*Out,s.diag(36,1)),"general full-rank ports attain 2 times3")
    check(eq((s.Rational(1,11)*Out).H*(s.Rational(1,11)*Out),s.diag(s.Rational(36,121),s.Rational(1,121))),"small physical prefactor is a real escape")

    # Transport every leg. R matrices need not preserve the old numerical norm;
    # K, support and norms transport with them, per the theorem.
    Rp=s.diag(2,s.Rational(1,3)); Rm=s.Matrix([[1,1],[0,2]])
    Ip=Rp*Inc; Pp=Row*Rm.inv(); Cp=Rm*Corth*Rp.inv()
    check(eq(Pp*Cp*Ip,Out),"complete moving-frame response invariant")
    check(not eq(Pp*Corth*Ip,Out),"omitted generator transport is detected")

    # q-channel controls in (b0,b1,sigma,nu) coordinates. This is a finite
    # representative of the written all-dimension channel proof, not a physical map.
    jh0=s.Matrix.vstack(I2,Z2,Z2,Z2)
    jh1=s.Matrix.vstack(Z2,I2,Z2,Z2)
    N=s.Matrix([[0,1],[-1,0]])
    jn=s.Matrix.vstack(Z2,Z2,N,Z2)
    jsw=s.Matrix.vstack(Z2,Z2,Z2,I2)
    Lsig=s.Matrix.hstack(Z2,Z2,I2,Z2)
    Lnu=s.Matrix.hstack(Z2,Z2,Z2,I2)
    check(eq(Lsig*jh0,Z2) and eq(Lsig*jh1,Z2),"nonzero sigma row blind to horizontal NE")
    check(not eq(Lsig*jn,Z2),"normal primitive NE detects sigma row")
    check(all(eq(Lnu*j,Z2) for j in (jh0,jh1,jn)),"nu-output row blind to all NE")
    check(eq(Lnu*jsw,I2),"independent SW detects nu-output row")
    check(s.Matrix.hstack(jh0,jh1,jn,jsw).det()!=0,"complete two-cross-channel image spans receiver control")
    return {"passed": True, "checks": count, "scope": "exact effective-port and observation-channel controls; physical response conditional", "countercontrols": ["restricted odd support", "zero effective port", "small physical prefactor", "omitted frame leg", "horizontal NE blind sigma row", "all NE blind scalar row"]}


if __name__ == "__main__":
    main()
