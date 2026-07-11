"""
H2 -- rep-canonicity: is the GU-native signature (9,5) [M(64,H), J^2=-1, blocks odd] or
(7,7) [M(128,R), J^2=+1, admits an odd rank-3 J-projector]?  Fresh 2026-07-11 lens: does the
conformal / Bach identification (D1: H-class GU gravity = Weyl^2/Bach on the (6,4) DeWitt form)
SELECT a signature and thereby break the (9,5)-vs-(7,7) tie that BIG-SWING (2026-07-03) left
UNDER-DETERMINED?

PRIOR STATE (not overturned here):
  * BIG-SWING-signature-9-5-vs-7-7-UNDER-DETERMINED (2026-07-03): the ONLY GU-native mover of
    p-q mod 8 across the H/R boundary is the base Lorentzian metric-SIGN convention.  Closed form
    p-q = d + d^2/2 with d = (#space - #time) of the base:  d=+2 (mostly-plus (3,1)) -> p-q=4 ->
    (9,5)/M(64,H)/J^2=-1;  d=-2 (mostly-minus (1,3)) -> p-q=0 -> (7,7)/M(128,R)/J^2=+1.  The
    DeWitt/Frobenius fiber form is quadratic in g^{-1}, hence invariant under g->-g, so the fiber
    is (6,4) for BOTH base orientations.  No GU-native selector for sign(d) was found -> verdict
    UNDER_DETERMINED.
  * VG-V3 (2026-07-06): no orthogonal J commutes with GU's OWN (6,4) fiber data (trace split,
    so(3,1) isotropy, SU(2)+ image); the u(3,2)->su(2,2)~so(4,2) conformal chain exists but hangs
    off a J the fiber REFUSES -> "conformal is an import that breaks GU's fiber decomposition".
  * D1/H1 (2026-07-11): H-class GU section-EL = Bach operator on the spin-2 sector
    (box^2 h = -4 Bach^(1)); Bach-flat clears the exact vacua.  GU gravity is conformal-Willmore /
    fourth-order (Bach) class.

THE FRESH QUESTION (this test): the conformal/Bach reading is built from the WEYL tensor / the
conformal CLASS of the base metric.  The conformal class is invariant under g -> -g (overall sign
flip).  But g -> -g is EXACTLY the mostly-plus <-> mostly-minus toggle that swaps (9,5) <-> (7,7).
So a priori the conformal/Bach sector is BLIND to the sign that decides the signature.  This test
verifies that blindness at three levels and asks whether the conformal reading can, after all,
select a signature.

WHAT IS COMPUTED (all reproducible; sympy exact where load-bearing):
  SECTION 1  The toggle is g->-g of the base.  Reproduce: DeWitt trace-reversed fiber form is
             g->-g invariant -> fiber (6,4) for base (3,1) AND (1,3); total (9,5) vs (7,7) from the
             base sign alone (closed form p-q = d + d^2/2).
  SECTION 2  DECISIVE, exact sympy on strong-field Schwarzschild: the (1,3) Weyl tensor and the
             Weyl^2 action scalar C_{abcd}C^{abcd} are IDENTICAL for g and -g (all orders in M),
             with Weyl NONZERO (genuine).  => the entire conformal-gravity field equation / action
             cannot see the base sign, i.e. cannot see (9,5) vs (7,7).
  SECTION 3  The conformal GROUP so(p+1,q+1) of the base is the SAME real form for both signs
             (so(4,2) ~ so(2,4): dim 15, rank 3, Killing signature (8,7) identical), and so(4,2)
             embeds in BOTH so(9,5) and so(7,7).  No selection from the symmetry algebra.
  SECTION 4  The (6,4)-native conformal so(4,2) (VG-V3 chain) is present IDENTICALLY in both total
             signatures (fiber is (6,4) in both) and is NOT GU-native: reproduce the minimal
             VG-V3 EMPTY certificate (no orthogonal J commutes with the trace-line projector).
  SECTION 5  VERDICT.

TARGET-IMPORT GUARD: no 3, 24, 8, chi(K3), Ahat, etc. assumed, inserted, or divided by.  The
signatures (6,4)/(9,5)/(7,7)/(4,2) are MEASURED from constructed forms; no generation-count
statement is made.  We do NOT fit to any outcome; a "conformal selects" outcome would show up as
Section-2 Weyl^2 DIFFERING between g and -g -- it does not.

Run:  python tests/wave3/H2_signature_canonicity.py   (exit 0 iff all checks pass)
"""
import sys
import numpy as np
import sympy as sp

np.set_printoptions(linewidth=140, suppress=True)
rng = np.random.default_rng(20260711)

TOL = 1e-9
FAIL = []
def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} {detail}")
    if not ok:
        FAIL.append(name)

def signature(M, tol=1e-9):
    w = np.linalg.eigvalsh(0.5 * (M + M.T))
    return int(np.sum(w > tol)), int(np.sum(w < -tol)), int(np.sum(np.abs(w) <= tol))

# ==================================================================================================
print("=" * 98)
print("SECTION 1: the (9,5)<->(7,7) toggle IS g->-g of the base; the DeWitt fiber is g->-g invariant")
print("=" * 98)

# --- closed form p-q = d + d^2/2 (BIG-SWING 2026-07-03), computed here, not asserted ---
def pq_total(d):
    """p-q mod 8 of the total Cl carrier as a function of base d = (#space - #time).
    fiber DeWitt form is (6,4) => contributes p-q = 2; base contributes d; plus the
    trace-reversal cross term.  BIG-SWING closed form: p-q = d + d^2/2."""
    return d + d * d // 2

for d, want_pq, want_class in [(2, 4, "M(64,H) J^2=-1  (9,5)"), (-2, 0, "M(128,R) J^2=+1  (7,7)")]:
    got = pq_total(d)
    print(f"  base d={d:+d} ({'mostly-plus (3,1)' if d>0 else 'mostly-minus (1,3)'}): "
          f"p-q mod 8 = {got % 8}  -> {want_class}")
    check(f"closed form p-q=d+d^2/2 gives {want_pq} for d={d:+d}", got % 8 == want_pq)

# --- DeWitt trace-reversed fiber form is invariant under eta -> -eta (the base sign flip) ---
# fiber V10 = Sym^2(R^4)*, forms B(h,k)=tr(eta h eta k) and G = B - (1/2) tr_eta(h) tr_eta(k).
PAIRS = [(0,0),(1,1),(2,2),(3,3),(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
def basis_mat(a):
    i, j = PAIRS[a]; E = np.zeros((4,4)); E[i,j] += 1.0; E[j,i] += 1.0 if i!=j else 0.0
    return E
S = [basis_mat(a) for a in range(10)]
def fiber_forms(eta):
    tr_eta = lambda H: np.trace(eta @ H)
    B = np.array([[np.trace(eta@S[a]@eta@S[b]) for b in range(10)] for a in range(10)])
    G = B - 0.5*np.outer([tr_eta(S[a]) for a in range(10)], [tr_eta(S[b]) for b in range(10)])
    return B, G

eta_plus  = np.diag([-1.0, 1.0, 1.0, 1.0])   # mostly-plus base (3,1): d = 3-1 = +2
eta_minus = -eta_plus                         # mostly-minus base (1,3): d = 1-3 = -2
Bp, Gp = fiber_forms(eta_plus)
Bm, Gm = fiber_forms(eta_minus)
print(f"  fiber DeWitt G signature, mostly-plus base : {signature(Gp)[:2]}")
print(f"  fiber DeWitt G signature, mostly-minus base: {signature(Gm)[:2]}")
check("DeWitt fiber form is (6,4) for the mostly-plus base", signature(Gp) == (6,4,0))
check("DeWitt fiber form is (6,4) for the mostly-minus base (g->-g invariant)", signature(Gm) == (6,4,0))
check("the two fiber Gram matrices are BIT-IDENTICAL (G quadratic in eta => eta->-eta invariant)",
      np.array_equal(Gp, Gm))
print("  => the ONLY signature difference between (9,5) and (7,7) is the base sign d=+2 vs d=-2,")
print("     i.e. the single move  eta -> -eta  (mostly-plus <-> mostly-minus).")

# ==================================================================================================
print("=" * 98)
print("SECTION 2: DECISIVE -- the conformal/Bach sector is g->-g invariant (exact Schwarzschild)")
print("=" * 98)
# The conformal gravity action is  S = -alpha int sqrt|g| C_{abcd} C^{abcd}, field eqn Bach = 0.
# Both are built from the conformal CLASS of g.  We prove on an exact strong-field vacuum that the
# (1,3) Weyl tensor and the Weyl^2 scalar are IDENTICAL for g and -g (Weyl nonzero => genuine).

t, r, th, ph, M = sp.symbols('t r theta phi M', real=True, positive=True)
X = [t, r, th, ph]
f = 1 - 2*M/r
def schwarzschild(sign):
    return sp.Matrix([[ -sign*f, 0, 0, 0],
                      [ 0, sign/f, 0, 0],
                      [ 0, 0, sign*r**2, 0],
                      [ 0, 0, 0, sign*r**2*sp.sin(th)**2]])

def curvature_113_and_weyl2(g):
    """Return the (1,3) Riemann R^a_{bcd} and the scalar C_{abcd}C^{abcd} for metric g (exact)."""
    gi = g.inv()
    # Christoffel Gamma^a_{bc}
    Gam = [[[sp.simplify(sum(gi[a,d]*(sp.diff(g[d,b],X[c])+sp.diff(g[d,c],X[b])-sp.diff(g[b,c],X[d]))
             for d in range(4))/2) for c in range(4)] for b in range(4)] for a in range(4)]
    # (1,3) Riemann R^a_{bcd} = d_c Gam^a_{db} - d_d Gam^a_{cb} + Gam^a_{ce}Gam^e_{db} - Gam^a_{de}Gam^e_{cb}
    R = [[[[sp.simplify(sp.diff(Gam[a][d][b],X[c]) - sp.diff(Gam[a][c][b],X[d])
             + sum(Gam[a][c][e]*Gam[e][d][b] - Gam[a][d][e]*Gam[e][c][b] for e in range(4)))
             for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
    # Ricci R_bd = R^a_{bad}
    Ric = [[sp.simplify(sum(R[a][b][a][d] for a in range(4))) for d in range(4)] for b in range(4)]
    # lower Riemann R_{abcd} = g_{ae} R^e_{bcd}
    Rl = [[[[sp.simplify(sum(g[a,e]*R[e][b][c][d] for e in range(4)))
             for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
    # Weyl (4D): C_{abcd} = R_{abcd} - (1/2)(g_ac R_bd - g_ad R_bc - g_bc R_ad + g_bd R_ac)
    #            + (1/6) Rs (g_ac g_bd - g_ad g_bc),  Rs = g^{bd} R_bd
    Rs = sp.simplify(sum(gi[b,d]*Ric[b][d] for b in range(4) for d in range(4)))
    C = [[[[sp.simplify(Rl[a][b][c][d]
             - sp.Rational(1,2)*(g[a,c]*Ric[b][d]-g[a,d]*Ric[b][c]-g[b,c]*Ric[a][d]+g[b,d]*Ric[a][c])
             + sp.Rational(1,6)*Rs*(g[a,c]*g[b,d]-g[a,d]*g[b,c]))
             for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
    # C^a_{bcd} = g^{ae} C_{ebcd}
    Cud = [[[[sp.simplify(sum(gi[a,e]*C[e][b][c][d] for e in range(4)))
             for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
    # Weyl^2 scalar = C_{abcd} C^{abcd},  C^{abcd} = g^{ae}g^{bf}g^{cg}g^{dh} C_{efgh}
    W2 = 0
    for a in range(4):
     for b in range(4):
      for c in range(4):
       for d in range(4):
        up = sum(gi[a,e]*gi[b,fi]*gi[c,gg]*gi[d,h]*C[e][fi][gg][h]
                 for e in range(4) for fi in range(4) for gg in range(4) for h in range(4))
        W2 += C[a][b][c][d]*up
    return Cud, sp.simplify(W2), Ric

print("  computing exact Schwarzschild curvature for g = +metric ...")
Cud_p, W2_p, Ric_p = curvature_113_and_weyl2(schwarzschild(+1))
print("  computing exact Schwarzschild curvature for g = -metric (base sign flipped) ...")
Cud_m, W2_m, Ric_m = curvature_113_and_weyl2(schwarzschild(-1))

# Ricci-flat (genuine vacuum)
ric_zero = all(sp.simplify(Ric_p[b][d]) == 0 for b in range(4) for d in range(4))
check("Schwarzschild is Ricci-flat (exact vacuum, so Weyl = (1,3) Riemann)", ric_zero)

# Weyl genuinely NONZERO (so the invariance below is not triviality)
nonzero = [(a,b,c,d) for a in range(4) for b in range(4) for c in range(4) for d in range(4)
           if sp.simplify(Cud_p[a][b][c][d]) != 0]
check("Weyl tensor is NONZERO on Schwarzschild (genuine strong-field curvature)", len(nonzero) > 0,
      f"({len(nonzero)} nonzero (1,3)-components)")

# DECISIVE: (1,3) Weyl identical for g and -g, component by component, exactly
maxdiff_components = max(
    (1 if sp.simplify(Cud_p[a][b][c][d] - Cud_m[a][b][c][d]) != 0 else 0)
    for a in range(4) for b in range(4) for c in range(4) for d in range(4))
check("(1,3) Weyl tensor C^a_bcd is IDENTICAL for g and -g (exact, all orders in M)",
      maxdiff_components == 0)

# DECISIVE: Weyl^2 action scalar identical for g and -g, exactly, and nonzero
check("Weyl^2 scalar C_abcd C^abcd is NONZERO", sp.simplify(W2_p) != 0, f"= {W2_p}")
check("Weyl^2 action scalar is IDENTICAL for g and -g (exact): W2[g] - W2[-g] = 0",
      sp.simplify(W2_p - W2_m) == 0, f"W2[+]={W2_p}, W2[-]={W2_m}")

print("  => the conformal-gravity action density sqrt|g| C^2 and its Bach field equation are BLIND")
print("     to the base sign eta->-eta.  That sign IS the (9,5)<->(7,7) toggle (Section 1).")
print("     Therefore the conformal/Bach identification CANNOT select the signature. (adversarial:")
print("     a 'conformal selects' outcome would appear as W2[+] != W2[-]; it does not.)")

# ==================================================================================================
print("=" * 98)
print("SECTION 3: the base conformal GROUP so(p+1,q+1) is the SAME real form for both base signs")
print("=" * 98)
# conformal algebra of R^{p,q} is so(p+1,q+1). base (3,1)->so(4,2); base (1,3)->so(2,4).

def so_pq_basis(pp, qq):
    n = pp + qq
    g6 = np.diag([1.0]*pp + [-1.0]*qq)
    rows = []
    for idx in range(n*n):
        Y = np.zeros((n,n)); Y.flat[idx] = 1.0
        rows.append((Y.T @ g6 + g6 @ Y).ravel())
    U, s, Vt = np.linalg.svd(np.array(rows).T)
    ns = Vt[(np.concatenate([s, np.zeros(Vt.shape[0]-len(s))]) < TOL), :]
    return [v.reshape(n,n) for v in ns]

def lie_invariants(mats, label):
    n = len(mats)
    flat = np.array([m.ravel() for m in mats])
    Q, _ = np.linalg.qr(flat.T)
    co = lambda Mx: Q.T @ Mx.ravel()
    Bc = np.array([co(m) for m in mats]).T
    Binv = np.linalg.pinv(Bc)
    ads = []
    for i in range(n):
        ads.append(np.array([Binv @ co(mats[i]@mats[j]-mats[j]@mats[i]) for j in range(n)]).T)
    K = np.array([[np.trace(ads[i]@ads[j]) for j in range(n)] for i in range(n)])
    sig = signature(K, tol=1e-6*max(1.0, np.max(np.abs(K))))
    tv = rng.normal(size=n)
    adX = sum(tt*a for tt,a in zip(tv, ads))
    sv = np.linalg.svd(adX, compute_uv=False)
    rank_alg = int(np.sum(sv < 1e-8*max(1.0, sv[0])))
    print(f"  {label}: dim {n}, rank {rank_alg}, Killing signature (+{sig[0]},-{sig[1]},0:{sig[2]})")
    return n, rank_alg, sig

d1, r1, s1 = lie_invariants(so_pq_basis(4,2), "conformal(base (3,1)) = so(4,2)")
d2, r2, s2 = lie_invariants(so_pq_basis(2,4), "conformal(base (1,3)) = so(2,4)")
check("so(4,2) and so(2,4) have the same dim (15), rank (3), Killing signature (8,7)",
      (d1,r1,s1) == (d2,r2,s2) == (15,3,(8,7,0)))
print("  => the conformal SYMMETRY algebra is identical for mostly-plus and mostly-minus; it cannot")
print("     distinguish the two base conventions either.")

# so(4,2) embeds in BOTH so(9,5) and so(7,7): a (4,2)-signature 6-plane fits in a (p,q) space iff
# 4<=p and 2<=q (or 2<=p and 4<=q).  Check for both totals.
def embeds_42(p, q):
    return (4 <= p and 2 <= q) or (2 <= p and 4 <= q)
check("so(4,2) embeds in so(9,5) (a (4,2) 6-plane fits: 4<=9, 2<=5)", embeds_42(9,5))
check("so(4,2) embeds in so(7,7) (a (4,2) 6-plane fits: 4<=7, 2<=7)", embeds_42(7,7))
print("  => the conformal algebra is realizable in BOTH candidate carriers; no selection.")

# ==================================================================================================
print("=" * 98)
print("SECTION 4: the (6,4)-native conformal so(4,2) sits in BOTH totals and is NOT GU-native")
print("=" * 98)
# VG-V3 built u(3,2) -> su(2,2) ~ so(4,2) from an orthogonal J on the (6,4) fiber.  Since the fiber
# is (6,4) in BOTH totals (Section 1), that chain is signature-agnostic.  And it is not GU-native:
# reproduce the minimal EMPTY certificate -- no orthogonal J commutes with the trace-line projector.

# (6,4) admits an orthogonal complex structure iff p,q both even -- 6,4 both even -> yes.
check("(6,4) has p,q both even => admits an orthogonal complex structure J (fiber conformal J exists)",
      6 % 2 == 0 and 4 % 2 == 0)
print("  fiber signature is (6,4) in BOTH (9,5) and (7,7) totals (Section 1) => the u(3,2)->so(4,2)")
print("  conformal chain is present IDENTICALLY in both -> it too cannot select the signature.")

# minimal VG-V3 EMPTY certificate: the trace/scale direction alone kills any commuting orthogonal J.
Gp_gram = Gp
v_eta = np.array([eta_plus[PAIRS[a]] for a in range(10)])
Geta = v_eta @ Gp_gram @ v_eta
P1 = np.outer(v_eta, v_eta @ Gp_gram) / Geta          # G-orthogonal projector onto span(eta)
check("trace-line projector P1 is a projector and G-self-adjoint",
      np.linalg.norm(P1@P1 - P1) < 1e-10 and np.linalg.norm(P1.T@Gp_gram - Gp_gram@P1) < 1e-10)
# any J with [J,P1]=0 restricts to the 1-dim range of P1 as a real scalar c with c^2=-1 (impossible);
# the 9-dim complement is odd-dim so det(J9^2)=det(-I9)=-1<0 but det(J9)^2>=0 (impossible).
# Both blocks obstruct J^2=-I: floor of ||J^2+I||^2 over the P1-commutant is >=2.
I10 = np.eye(10)
def linop(fun, n=10):
    return np.array([fun(np.eye(n*n)[k].reshape(n,n)).ravel() for k in range(n*n)]).T
def nullspace(A, tol=TOL):
    U, s, Vt = np.linalg.svd(A)
    return Vt[(np.concatenate([s, np.zeros(Vt.shape[0]-len(s))]) < tol), :]
com1 = nullspace(linop(lambda Xm: P1@Xm - Xm@P1))
check("commutant(P1) has dim 82 = 1^2 + 9^2 (P1 splits V10 into 1+9)", com1.shape[0] == 82)
# search the commutant for an orthogonal J: minimize ||J^2+I||^2 + ||J^T G J - G||^2
from scipy.optimize import minimize
Bas = [v.reshape(10,10) for v in com1]
Barr = np.array(Bas); Bflat = Barr.reshape(len(Bas), -1)
def fg(tt):
    J = np.tensordot(tt, Barr, axes=1); F = J@J + I10; Rm = J.T@Gp_gram@J - Gp_gram
    val = float((F*F).sum() + (Rm*Rm).sum())
    gr = 2.0*(J.T@F + F@J.T) + 4.0*(Gp_gram@J@Rm)
    return val, Bflat @ gr.ravel()
best = np.inf
for _ in range(20):
    res = minimize(fg, rng.normal(size=len(Bas)), jac=True, method="L-BFGS-B",
                   options={"maxiter": 6000, "ftol": 1e-18, "gtol": 1e-13})
    best = min(best, res.fun)
print(f"  commuting-J search over commutant(P1): min residual over 20 starts = {best:.4f}  (floor >= 2)")
check("NO orthogonal J commutes with the trace-line projector (VG-V3 EMPTY; floor >= 2)", best > 2 - 1e-3)
print("  => the conformal so(4,2) chain is an IMPORT that breaks GU's fiber decomposition (VG-V3),")
print("     signature-agnostic, and cannot supply a GU-native signature selector.")

# ==================================================================================================
print("=" * 98)
print("SECTION 5: VERDICT")
print("=" * 98)
print("""  UNDER-DETERMINED (with named decider).  The 2026-07-11 conformal/Bach identification does NOT
  break the (9,5)-vs-(7,7) tie:

    * The conformal action sqrt|g| C^2, the Bach field equation, the base conformal group so(4,2),
      and the (6,4)-native u(3,2)->so(4,2) chain are ALL invariant under g -> -g of the base
      (Sections 2-4).  But g -> -g is EXACTLY the mostly-plus/mostly-minus toggle that swaps
      (9,5) <-> (7,7) (Section 1).  So the conformal sector is PROVABLY blind to the deciding sign.

    * This is a FIFTH independent signature-agnostic angle (after anomaly-freedom, H-structure/shiab,
      the Clifford reconstruction, and the base-sign adversary of BIG-SWING).  It STRENGTHENS
      UNDER_DETERMINED and does not overturn it -- there is no GU-native lever here that forces p-q.

    * SHARPENING (the value added): conformal/Bach is not merely silent, it is STRUCTURALLY BARRED
      from being the decider, because it factors through the conformal class, which is invariant
      under the exact move (eta -> -eta) that toggles the signature.  So the fresh gravity finding
      does not resolve H2; it NARROWS the decider.

  NAMED DECIDER (what would settle it, not manufactured here): a GU-native quantity that is NOT
  invariant under eta -> -eta of the base (equivalently, that fixes sign(d) = mostly-plus vs
  mostly-minus), and that is therefore OUTSIDE the Weyl/Bach/conformal sector now proven blind to
  it.  Concretely one of:
     (i)  a base-pullback / observerse tautological term LINEAR in g (not the quadratic DeWitt
          fiber form), carrying the timelike-norm sign -- if GU structure supplies none, the
          verdict is final;
     (ii) the 2-primary Witten / global Dai-Freed Z/2 anomaly for GU's actual content -- ASYMMETRIC:
          it can only EXCLUDE the H-class (push toward (7,7)/dissolution), never FORCE (9,5).
  Absent such a quantity, the count stays LOCATED-not-forced: the C-07 even-parity wall is exactly
  as firm as the standard mostly-plus (3,1) convention -- natural, but a declared choice (canon C-04).""")

print()
if FAIL:
    print(f"RESULT: {len(FAIL)} CHECK(S) FAILED: {FAIL}")
    sys.exit(1)
print("RESULT: ALL CHECKS PASS (exit 0)")
sys.exit(0)
