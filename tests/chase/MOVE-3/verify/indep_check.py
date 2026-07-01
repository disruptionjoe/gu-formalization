"""
INDEPENDENT re-verification of MOVE-3.

I do NOT reuse the chaser's B1/alg_lin functions. I rebuild the vertical SFF
literally from ii-s-coordinate-formula sec 4 (eq for B_{mu nu,ab}), AND I also
build the HORIZONTAL component B^rho_{mu nu} (sec 4, line 222-227), which the
chaser ignored. The horizontal trace is the M/r^2-SCALING object that most
literally matches the canon's "H^i_Schw ~ O(M/r^2)" claim (line 89). If ANY
reading of the mean-curvature vector gives a non-harmonic O(M/r^2) whose
Laplacian is 2M/r^4, the falsification could survive. I test all readings.

Metric: g = eta + h, eta=diag(-1,1,1,1), phi=M/r, h_00=h_11=h_22=h_33=2phi.
Static (no t dependence).
"""
import sympy as sp

t,x,y,z,M = sp.symbols('t x y z M', real=True, positive=False)
X = [t,x,y,z]
r = sp.sqrt(x**2+y**2+z**2)
phi = M/r
eta = sp.diag(-1,1,1,1)
etaU = sp.diag(-1,1,1,1)

# full metric g and perturbation h
h = sp.zeros(4,4)
h[0,0]=2*phi
for i in (1,2,3): h[i,i]=2*phi
g = eta + h
gU = g.inv()   # exact inverse; we will linearize where needed

def d(f,i): return sp.diff(f, X[i])
def dd(f,i,j): return sp.diff(f, X[i], X[j])

def lap(f):  # flat Laplacian (static -> spatial); include -d_t^2 for completeness
    return -dd(f,0,0)+dd(f,1,1)+dd(f,2,2)+dd(f,3,3)

# ---- sanity: Delta(M/r)=0, Delta(M/r^2)=2M/r^4 ----
assert sp.simplify(lap(M/r))==0
assert sp.simplify(lap(M/r**2)-2*M/r**4)==0
print("sanity: Delta(M/r)=0 ; Delta(M/r^2)=2M/r^4  OK")

# ================= VERTICAL SFF B^V_{mn,ab}, linear in h =================
# ii-s sec4:
#   B_{mn,ab} = d_m d_n g_ab              (graph Hessian)
#             - gbarGamma^l_{mn} d_l g_ab (O(h^2), drop)
#             - (1/2)( g_{a(m}g_{n)b} - (1/2) g_ab g_mn )   (algebraic slice)
#             - (1/2)( (d_m g)_ar g^rs (d_n g)_sb + m<->n )  (O(h^2), drop)
# Linear-in-h: Hessian d_m d_n h_ab + linear part of algebraic slice.
def sym2(A,m,n,a,b):  # g_{a(m} g_{n)b} = 1/2(g_am g_nb + g_an g_mb)
    return sp.Rational(1,2)*(A[a,m]*A[n,b] + A[a,n]*A[m,b])

def alg_full(A,m,n,a,b):  # -(1/2)( g_{a(m}g_{n)b} - 1/2 g_ab g_mn )
    return -sp.Rational(1,2)*( sym2(A,m,n,a,b) - sp.Rational(1,2)*A[a,b]*A[m,n] )

# linear-in-h algebraic part = alg_full(g) - alg_full(eta)  (subtract flat ref, sec 6.1b)
def BV_lin(m,n,a,b):
    hess = dd(h[a,b], m, n)
    alg  = alg_full(g,m,n,a,b) - alg_full(eta,m,n,a,b)   # keeps linear + h^2; expand linear
    return hess + alg

# mean-curvature VERTICAL representative: trace with eta (leading order)
HV = sp.zeros(4,4)
for a in range(4):
    for b in range(4):
        s=0
        for m in range(4):
            for n in range(4):
                s+= etaU[m,n]*BV_lin(m,n,a,b)
        # linearize: drop terms O(M^2) by series in M
        HV[a,b]=sp.simplify(sp.expand(s))
# extract linear-in-M part
def linM(expr):
    ser = sp.series(expr, M, 0, 2).removeO()
    return sp.simplify(ser)
print("\nVERTICAL mean-curvature H^V_ab (linear in M):")
for a in range(4):
    for b in range(a,4):
        v=linM(HV[a,b])
        if v!=0: print("  H^V[%d,%d]="%(a,b), v, "   Delta=", sp.simplify(lap(v)))

# ================= HORIZONTAL SFF B^rho_{mn} (sec4 line222) =================
# B^rho_{mn} = 1/2 g^{rl}((d_m g)_{n l}+(d_n g)_{m l}) - gbarGamma^rho_{mn}
# linear order: gbar = g + O(h^2), so gbarGamma = Gamma(g) linear.
def Gamma_g(rho,m,n):  # LC of g, linear in h using eta inverse
    s=0
    for l in range(4):
        s+= sp.Rational(1,2)*etaU[rho,l]*( d(h[n,l],m)+d(h[m,l],n)-d(h[m,n],l) )
    return s
def Bhor(rho,m,n):
    s=0
    for l in range(4):
        s+= sp.Rational(1,2)*etaU[rho,l]*( d(h[n,l],m)+d(h[m,l],n) )   # linear part of 1/2 g^{rl}(dg+dg)
    return sp.simplify(s - Gamma_g(rho,m,n))
# horizontal mean curvature H^rho = eta^{mn} B^rho_{mn}
print("\nHORIZONTAL mean-curvature H^rho = eta^{mn}B^rho_{mn} (the M/r^2 reading):")
maxlap_h=0
for rho in range(4):
    s=0
    for m in range(4):
        for n in range(4):
            s+= etaU[m,n]*Bhor(rho,m,n)
    Hrho=sp.simplify(s)
    dl=sp.simplify(lap(Hrho))
    print("  H^rho[%d]="%rho, Hrho, "   scale~", "M/r^2" if Hrho!=0 else "0", "   Delta H^rho=", dl)
    if dl!=0: maxlap_h=1

print("\n== BREAK TEST: does ANY mean-curvature reading give Delta H != 0 at O(M)? ==")
allV = all(sp.simplify(lap(linM(HV[a,b])))==0 for a in range(4) for b in range(4))
print("  vertical  Delta H^V all zero:", allV)
print("  horizontal Delta H^rho all zero:", maxlap_h==0)

# ================= the note's literal scaling substitution =================
print("\n== the note's error, made explicit ==")
print("  note took 'H~M/r^2' and computed Delta(M/r^2)=", sp.simplify(lap(M/r**2)),"= 2M/r^4 (nonzero)")
grad = sp.simplify(d(phi,1))  # partial_x (M/r) = actual M/r^2-scaling object
print("  but the ACTUAL M/r^2-scaling object is d_x(M/r) =", grad)
print("  its Laplacian Delta(d_x phi)=", sp.simplify(lap(grad)), " (harmonic: deriv of harmonic)")

# ================= genuine quadratic residual exists? =================
print("\n== quadratic (a=2) check: is full HV nonzero at O(M^2)? ==")
q = sp.simplify(sp.expand(HV[1,1]) - linM(HV[1,1]))
print("  H^V[1,1] minus its linear part (=O(M^2) remainder):", sp.simplify(q))
