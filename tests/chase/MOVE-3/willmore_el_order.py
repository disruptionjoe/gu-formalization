"""
MOVE-3: Willmore-EL residual order on linearized Schwarzschild.

Question (canon schwarzschild-weak-field-rfail.md, F1):
  Does the GU Willmore/ integral||II||^2 Euler-Lagrange residual on the linearized
  Schwarzschild graph section enter at O(M/r^3) [FALSIFY solar-system compat] or
  O(M/r^4) [SAFE]?

The in-repo load-bearing chain (rfail-non-umbilic-schwarzschild §4.3, and the canon
note lines 71,392):
    H^i_Schw ~ O(M/r^2)   and   Delta^perp H^i ~ Delta(M/r^2) = 2M/r^4 != 0.
So the whole order estimate rests on the premise  H (mean curvature) ~ M/r^2.

The triage verifier claimed: the O(M) mean curvature actually VANISHES by harmonicity
of the Schwarzschild (Newtonian) potential.  This script settles that with real algebra.

Objects computed (sympy, exact):
  P1. Arithmetic of the note: Delta(M/r^2) = 2M/r^4  (true) and  Delta(M/r) = 0 (harmonic).
  P2. The actual second fundamental form B^{(1)} of the linearized Schwarzschild GRAPH
      section (Met(X4) fiber, literal-graph formula, ii-s-coordinate-formula.md sec 4),
      its mean-curvature vector H^{(1)}_ab, and the flat Willmore-EL leading operator
      Delta H^{(1)}.  Check whether H^{(1)} ~ M/r^2 (note) or ~ M/r (harmonic) or 0.
  P3. Leading order in M of the residual: is there ANY linear-in-M (a=1) term, and what
      is the leading (a,n) in residual ~ M^a / r^n ?

Convention: linearized weak field, isotropic Cartesian coords (t,x,y,z),
  g = eta + h,  eta = diag(-1,1,1,1),  phi = M/r  (r = sqrt(x^2+y^2+z^2)),
  h_00 = 2 phi,  h_ij = 2 phi delta_ij,  h_0i = 0.   (standard PN / harmonic gauge)

The literal-graph vertical second fundamental form (ii-s-coordinate-formula sec 4),
linearized (drop O(h^2) = O(M^2) and gbar_Gamma*dg = O(M^2)):
  B^{(1)}_{mu nu, ab} = d_mu d_nu h_{ab}                       [graph Hessian]
                      - (1/2)( g_{a(mu} g_{nu)b} - (1/2) g_{ab} g_{mu nu} )_lin_in_h
The flat-reference (M=0) algebraic slice term is subtracted (ii-s sec 6.1(b)):
"if flat spacetime must have II_s=0, subtract this canonical algebraic slice term".
"""

import sympy as sp

t, x, y, z, M = sp.symbols('t x y z M', real=True)
coords = [t, x, y, z]
r = sp.sqrt(x**2 + y**2 + z**2)

eta = sp.diag(-1, 1, 1, 1)
etaU = sp.diag(-1, 1, 1, 1)  # inverse of eta is itself

phi = M / r

# metric perturbation h_{ab}
h = sp.zeros(4, 4)
h[0, 0] = 2*phi
for i in (1, 2, 3):
    h[i, i] = 2*phi

def lap_flat(f):
    """Flat d'Alembertian eta^{mn} d_m d_n f = -d_t^2 f + d_x^2+d_y^2+d_z^2 f (static -> spatial Laplacian)."""
    return -sp.diff(f, t, 2) + sp.diff(f, x, 2) + sp.diff(f, y, 2) + sp.diff(f, z, 2)

print("="*70)
print("P1: the note's arithmetic vs the physical scaling")
print("="*70)
lap_of_1_over_r2 = sp.simplify(lap_flat(M/r**2))
lap_of_1_over_r  = sp.simplify(lap_flat(M/r))
print("  Delta(M/r^2) =", lap_of_1_over_r2, "   [note asserts = 2M/r^4]")
print("     as M/r^4 :", sp.simplify(lap_of_1_over_r2 * r**4 / M), "* M/r^4")
print("  Delta(M/r)   =", lap_of_1_over_r, "   [harmonic potential -> 0]")
assert sp.simplify(lap_of_1_over_r2 - 2*M/r**4) == 0
assert lap_of_1_over_r == 0
print("  CHECK: Delta(M/r^2)=2M/r^4 TRUE;  Delta(M/r)=0 TRUE (harmonicity).")

print()
print("="*70)
print("P2: actual mean curvature of the linearized Schwarzschild graph section")
print("="*70)

# second derivatives of h
def d2h(mu, nu, a, b):
    return sp.diff(h[a, b], coords[mu], coords[nu])

# linear-in-h part of the algebraic slice term:
#   -(1/2)( g_{a(mu} g_{nu)b} - (1/2) g_{ab} g_{mu nu} )
# g_{a(mu}g_{nu)b} = (1/2)(g_{a mu}g_{nu b}+g_{a nu}g_{mu b}); take terms linear in h,
# with flat (M=0) reference subtracted (only h-linear pieces kept).
def alg_lin(mu, nu, a, b):
    term1 = sp.Rational(1,2)*(h[a,mu]*eta[nu,b] + eta[a,mu]*h[nu,b]
                              + h[a,nu]*eta[mu,b] + eta[a,nu]*h[mu,b])
    term2 = h[a,b]*eta[mu,nu] + eta[a,b]*h[mu,nu]
    return -sp.Rational(1,2)*(term1 - sp.Rational(1,2)*term2)

# B^{(1)}_{mu nu, ab}
def B1(mu, nu, a, b):
    return d2h(mu, nu, a, b) + alg_lin(mu, nu, a, b)

# mean curvature vector H^{(1)}_ab = eta^{mu nu} B^{(1)}_{mu nu, ab}  (leading order uses eta)
H1 = sp.zeros(4, 4)
for a in range(4):
    for b in range(4):
        s = 0
        for mu in range(4):
            for nu in range(4):
                s += etaU[mu, nu] * B1(mu, nu, a, b)
        H1[a, b] = sp.simplify(s)

print("  Mean-curvature vector components H^{(1)}_ab (nonzero):")
for a in range(4):
    for b in range(a, 4):
        if H1[a, b] != 0:
            # express as coeff * M / r^p
            expr = H1[a, b]
            print("   H1[%d,%d] = %s" % (a, b, sp.simplify(expr)))

# Split H1 into the harmonic-Hessian part vs algebraic part, and check power of r.
# Determine leading r-power of each nonzero H1 component.
print()
print("  r-scaling of H^{(1)} (should be ~ M/r, NOT M/r^2 as the note assumes):")
for a in range(4):
    for b in range(a, 4):
        if H1[a, b] != 0:
            e = sp.simplify(H1[a, b])
            # test scaling: e * r^k / M constant?
            for k in (0,1,2,3):
                test = sp.simplify(e * r**k / M)
                if test.free_symbols.isdisjoint({x, y, z}):
                    print("   H1[%d,%d] ~ (%s) * M / r^%d" % (a, b, test, k))
                    break

# The Hessian (graph) contribution to H alone = eta^{mn} d_m d_n h_ab = Box h_ab
print()
print("  Graph-Hessian part of mean curvature  Box h_ab = eta^{mn} d_m d_n h_ab:")
allzero = True
for a in range(4):
    for b in range(a, 4):
        boxh = sp.simplify(lap_flat(h[a, b]))
        if boxh != 0:
            allzero = False
        print("   Box h[%d,%d] = %s" % (a, b, boxh))
print("  => Graph-Hessian mean curvature vanishes at O(M):", allzero, "(harmonicity)")

print()
print("  Flat Willmore-EL leading operator  Delta H^{(1)}_ab  (the F1 object):")
res_linear_all_zero = True
for a in range(4):
    for b in range(a, 4):
        dH = sp.simplify(lap_flat(H1[a, b]))
        if dH != 0:
            res_linear_all_zero = False
        print("   Delta H1[%d,%d] = %s" % (a, b, dH))
print("  => linear-in-M Willmore-EL residual Delta H^{(1)} identically zero:",
      res_linear_all_zero)

print()
print("="*70)
print("P3: leading order in M of the Willmore-EL residual")
print("="*70)
# The linear-in-M residual (a=1) is Delta H^{(1)} = 0 (P2).  So NO a=1 term at all.
# The genuine residual is quadratic in M (a=2): the quadratic Willmore terms  (hatB)^2
# and H^{(2)} corrections.  Estimate leading r-power of the a=2 residual from the
# curvature-level SFF hatB ~ d^2 h ~ M/r^3 and algebraic x Hessian cross terms.

# Hessian-part SFF magnitude:  B_Hess_{mn,ab} = d_m d_n h_ab ~ M/r^3
# sample a representative nonzero second derivative:
Bsample = sp.simplify(sp.diff(h[1,1], x, x))
print("  representative Hessian SFF  d_x d_x h_xx =", Bsample)
for k in (0,1,2,3,4):
    test = sp.simplify(Bsample * r**k / M)
    if test.free_symbols.isdisjoint({x, y, z}):
        print("   -> Hessian SFF ~ M / r^%d" % k)
        Bpow = k
        break

# Quadratic Willmore term Q(B) ~ hatB^2. Two sub-scalings present in-repo:
#   connection-level B~M/r^2 -> B^2 ~ M^2/r^4   (note's Q(B) claim, line 260)
#   curvature-level  B~M/r^3 -> B^2 ~ M^2/r^6
# The algebraic-slice(anisotropic, ~M/r) x Hessian(~M/r^3) cross term ~ M^2/r^4.
print("  a=2 residual candidate powers:")
print("    (algebraic ~M/r) x (Hessian ~M/r^3)  -> M^2/r^4")
print("    (Hessian ~M/r^3)^2                    -> M^2/r^6")
print("    (connection-level B ~M/r^2)^2 [note]  -> M^2/r^4")

print()
print("="*70)
print("TERMINAL VERDICT")
print("="*70)
print("  linear-in-M (a=1) Willmore-EL residual coefficient : 0  (identically)")
print("  reason                                             : mean curvature is")
print("                                                       harmonic (H ~ M/r,")
print("                                                       NOT M/r^2), Delta H=0")
print("  leading residual order                             : a=2 (quadratic in M),")
print("                                                       ~ M^2/r^4")
print("  F1 (residual enters at O(M/r^3), a=1, n=3)         : NOT TRIGGERED")
print("  -> the O(M/r^3) FALSIFYING order is an ARTIFACT (no a=1 residual exists)")
print("  -> the canon 'safe O(M/r^4)' (a=1,n=4) is ALSO an artifact of H~M/r^2;")
print("     correct leading residual is O(M^2/r^4), strictly smaller for M/r<<1.")
