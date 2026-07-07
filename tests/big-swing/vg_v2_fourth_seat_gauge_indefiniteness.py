"""
VG-V2 -- THE FOURTH SEAT: can a parity-like structure render the noncompact gauge-sector
indefiniteness consistent on the actual GU carrier? (T8' fourth-seat scan, tri-theory federation
2026-07-06; kill condition #5.)

The gauge sector is so(9,5) acting on the 1792-dim module W = V (x) S (V = 14-dim vector,
S = 128-dim Cl(9,5) Dirac spinor, Jordan-Wigner build reused from
tests/generation-sector/ghost_parity_krein.py). Its Killing form is INDEFINITE (noncompact real
form). The candidate consistency structure is the CARTAN INVOLUTION theta (from memory: for a
noncompact semisimple real Lie algebra g, theta is an involutive Lie-algebra automorphism whose
twisted form B_theta(X,Y) = -B(X, theta Y) is positive definite; the theta-even part is the
maximal compact subalgebra -- standard Cartan theory).

What this script establishes, machine-checked:
  (A) theta exists concretely on the carrier: conjugation by the product of the timelike gammas
      (equivalently by beta_S = product of spacelike gammas) implements the standard split
      (+1 on so(9)+so(5), -1 on the mixed block); theta^2 = id; theta is a bracket automorphism;
      Killing is negative-definite on theta-even (dim 46), positive-definite on theta-odd
      (dim 45); B_theta > 0. This is the Gupta-Bleuler-style move for the gauge sector.
  (B) SEAT INTERPLAY: the module implementation of theta can be taken to be THE KREIN FORM
      K = eta_V (x) beta_S itself: K rho(X) K^{-1} = rho(theta X) exactly (pseudo-anti-
      Hermiticity IS the Cartan involution). Consequences computed: theta preserves ker(Gamma)
      and the SU(2)+ triplet, commutes with the family action, ANTIcommutes with chirality, and
      restricted to the triplet EQUALS the canonical ghost parity P_ghost = sign(K_triplet).
      The fourth seat and the quantization seat are filled by the same Z2, kinematically.
  (C) PUNCHLINE: the theta-even (compact) part of the internal block actually realized by this
      carrier ((9,5) = base(4,0) + internal(5,5)) is so(5)+so(5), the maximal compact of
      Spin(5,5); a theta-stable so(6,4) sub-block yields so(6)+so(4) = su(4)+su(2)+su(2)
      (Pati-Salam algebra, identified by measured dim/rank/definiteness/ideal-split); and a
      standalone su(3,2) fundamental yields s(u(3)+u(2)) = su(3)+su(2)+u(1) (SM algebra).
      Weinstein's maximal-compact chain [00:45:00] is exactly the theta-even sector: the
      punchline is the Gupta-Bleuler move. Kinematic grade only.
  (D) CONTROLS (the checks can fail): wrong-split involutions (conjugation by wrong gamma
      subsets) ARE automorphisms but FAIL B_theta > 0; random sign patterns fail the
      automorphism test; the fixed subalgebra of a wrong split is NOT compact; K restricted to
      a random 192-dim subspace does NOT square to the identity.

TARGET-IMPORT GUARD (maximum strictness): no element of {3, 8, 24, chi(K3)=24, Ahat=3,
rank_H=4, ind_H=8} is assumed, inserted, hardcoded as an input, or divided by. Dimensions such
as 3 = dim su(2), 8 = dim su(3), 24 = dim su(3,2) appear below ONLY as MEASURED OUTPUTS of the
geometry (printed with their measurement provenance); they enter no formula. Every count
statement is "mechanism M forces c", never "GU forces c".

Gates: whether theta/K commutes with any actual dynamics S is OPEN (GU supplies no S); the
PT/C-operator and conformal-fiber questions belong to the separate running big-swing workflow
(R1-R4) and are stated as gates only -- no outcomes cited.

Run: python tests/big-swing/vg_v2_fourth_seat_gauge_indefiniteness.py   (exit 0 = all checks pass)
"""
import sys
import numpy as np

np.random.seed(0)

N, DIM = 14, 128
TIMELIKE = {4, 5, 6, 7, 8}                       # (9,5) = base(4,0) + internal(5,5)
SPACELIKE = [a for a in range(N) if a not in TIMELIKE]

TOL = 1e-9          # exact-algebra residuals at dim <= 192
TOL_BIG = 1e-7      # residuals involving 1792-dim products / iterated constructions

FAILURES = []


def check(label, value, tol, mode="lt"):
    """mode 'lt': pass if value < tol. mode 'gt': pass if value > tol (controls must FAIL big)."""
    ok = (value < tol) if mode == "lt" else (value > tol)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}: {value:.3e} ({'<' if mode == 'lt' else '>'} {tol:.0e})")
    if not ok:
        FAILURES.append(label)
    return ok


def check_eq(label, value, target):
    ok = (value == target)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}: {value} (expect {target})")
    if not ok:
        FAILURES.append(label)
    return ok


# ---------------------------------------------------------------- carrier (verbatim recipe)
def jw(n):
    I = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    G = []
    for k in range(n):
        L, R = [s3] * k, [I] * (n - 1 - k)
        for mid in (s1, s2):
            o = np.array([[1 + 0j]])
            for m in L + [mid] + R:
                o = np.kron(o, m)
            G.append(o)
    return G


base = jw(7)
I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)
e = [(1j * base[a] if a in TIMELIKE else base[a]) for a in range(N)]
etaV = np.diag([(-1.0 if a in TIMELIKE else 1.0) for a in range(N)]).astype(complex)


def sgen(i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex)
    M[i, j] = 1
    M[j, i] = -1
    return M


def vgen(i, j):
    # so(9,5) vector representation: V_ab = lvec(a,b) @ etaV, i.e. (V_ab)_{dc} = d_da eta_bc - d_db eta_ac
    return lvec(i, j) @ etaV


def gen(i, j):
    # module generator on W = V (x) S (family-action convention of ghost_parity_krein.py,
    # base indices only, where vgen == lvec)
    return np.kron(I14, sgen(i, j)) + np.kron(lvec(i, j), I128)


def rho(i, j):
    # honest so(9,5) module generator on W = V (x) S
    return np.kron(vgen(i, j), I128) + np.kron(I14, sgen(i, j))


PAIRS = [(i, j) for i in range(N) for j in range(i + 1, N)]      # 91 generators
theta_sign = np.array([1.0 if ((i in TIMELIKE) == (j in TIMELIKE)) else -1.0 for (i, j) in PAIRS])

print("=" * 100)
print("VG-V2  THE FOURTH SEAT: Cartan involution vs gauge-sector indefiniteness on the GU carrier")
print("=" * 100)

# ================================================================ SECTION 0: ANCHORS
print("\n--- SECTION 0: ANCHOR REPRODUCTION (mandatory before any claim) ---")

# (0a) beta_S = product of spacelike gammas; pseudo-anti-Hermiticity anchor
bS = I128.copy()
for s in SPACELIKE:
    bS = bS @ e[s]
if np.linalg.norm(bS.conj().T + bS) < 1e-9:
    bS = 1j * bS
bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
res_bs2 = np.linalg.norm(bS @ bS - I128)
res_bsH = np.linalg.norm(bS - bS.conj().T)
res_pah = max(np.linalg.norm(bS @ sgen(i, j) + sgen(i, j).conj().T @ bS) for (i, j) in PAIRS)
check("anchor: beta_S^2 = I", float(res_bs2), TOL)
check("anchor: beta_S Hermitian", float(res_bsH), TOL)
check("anchor: beta_S pseudo-anti-Hermiticity max over 91 so(9,5) generators", float(res_pah), TOL)

# (0b) gamma-trace constraint: rank(Gamma) = 128, dim ker = 1664
Gam = np.hstack(e)                                # 128 x 1792
rankG = int(np.linalg.matrix_rank(Gam, tol=1e-9))
Pi = np.eye(N * DIM, dtype=complex) - Gam.conj().T @ np.linalg.inv(Gam @ Gam.conj().T) @ Gam
w, Vv = np.linalg.eigh(Pi)
Wk = Vv[:, w > 0.5]
check_eq("anchor: rank(Gamma)", rankG, 128)
check_eq("anchor: dim ker(Gamma)", Wk.shape[1], 1664)

# (0c) self-dual SU(2)+ triplet and its Krein signature (+96, -96, 0)
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
J3 = [gen(a, b) + gen(c, d) for (a, b, c, d) in SD]
Cas = -(J3[0] @ J3[0] + J3[1] @ J3[1] + J3[2] @ J3[2])
CasK = Wk.conj().T @ Cas @ Wk
CasK = 0.5 * (CasK + CasK.conj().T)
ev, U = np.linalg.eigh(CasK)
top = max(round(x.real, 3) for x in ev)
Wt = Wk @ U[:, np.abs(ev - top) < 1e-3]           # triplet sector
Kful = np.kron(etaV, bS)
Kt = Wt.conj().T @ Kful @ Wt
Kt = 0.5 * (Kt + Kt.conj().T)
sig = np.linalg.eigvalsh(Kt)
npl = int(np.sum(sig > 1e-9))
nmi = int(np.sum(sig < -1e-9))
nz = int(np.sum(np.abs(sig) < 1e-9))
print(f"  triplet sector: dim {Wt.shape[1]}, SU(2)+ Casimir eigenvalue {top}")
check_eq("anchor: triplet Krein signature (+)", npl, 96)
check_eq("anchor: triplet Krein signature (-)", nmi, 96)
check_eq("anchor: triplet Krein signature (0)", nz, 0)

# ================================================================ SECTION A: theta ON so(9,5)
print("\n--- SECTION A: THE CARTAN INVOLUTION ON THE GAUGE SECTOR so(9,5) ---")

# (A1) representation certification: vector rep intertwines the Clifford action
res_ad = max(
    np.linalg.norm(sgen(i, j) @ e[c] - e[c] @ sgen(i, j)
                   - sum(vgen(i, j)[d, c] * e[d] for d in range(N)))
    for (i, j) in PAIRS for c in range(N)
)
check("A1: [sigma_ab, gamma_c] = (V_ab)_dc gamma_d (vector rep = ad on gammas), max residual", float(res_ad), TOL)
res_soc = max(np.linalg.norm(vgen(i, j).T @ etaV + etaV @ vgen(i, j)) for (i, j) in PAIRS)
check("A1: vector rep satisfies so(9,5) condition V^T eta + eta V = 0, max residual", float(res_soc), TOL)

# structure constants from the vector rep; verify spinor rep closes with the SAME constants
Vmats = np.array([vgen(i, j) for (i, j) in PAIRS])               # (91,14,14)
Vflat = Vmats.reshape(91, -1)
Vpinv = np.linalg.pinv(Vflat)
brackets = np.einsum("iab,jbc->ijac", Vmats, Vmats) - np.einsum("jab,ibc->ijac", Vmats, Vmats)
cten = brackets.reshape(91, 91, -1) @ Vpinv                      # c[i,j,k]
res_vclose = float(np.abs(brackets.reshape(91, 91, -1) - cten @ Vflat).max())
check("A1: vector-rep closure onto 91-dim span (structure constants exact), max residual", res_vclose, TOL)
Smats = np.array([sgen(i, j) for (i, j) in PAIRS])               # (91,128,128)
rng = np.random.default_rng(1)
sample = rng.choice(91 * 91, size=300, replace=False)
res_sclose = 0.0
for idx in sample:
    i, j = divmod(int(idx), 91)
    br = Smats[i] @ Smats[j] - Smats[j] @ Smats[i]
    rec = np.tensordot(cten[i, j], Smats, axes=(0, 0))
    res_sclose = max(res_sclose, float(np.linalg.norm(br - rec)))
print(f"  A1: spinor rep closes with the SAME structure constants (300 random pairs sampled)")
check("A1: spinor-rep closure with vector-derived structure constants, max sampled residual", res_sclose, TOL)

# (A2) gauge-sector indefiniteness on the carrier: rho preserves the indefinite K (never a Hilbert form)
res_vK = max(np.linalg.norm(etaV @ vgen(i, j) + vgen(i, j).conj().T @ etaV) for (i, j) in PAIRS)
check("A2: vector factor pseudo-anti-Hermitian wrt eta_V (all 91)", float(res_vK), TOL)
check("A2: spinor factor pseudo-anti-Hermitian wrt beta_S (all 91) [= anchor 0a]", float(res_pah), TOL)
spot = [0, 17, 40, 55, 70, 90]
res_moduleK = 0.0
for k in spot:
    i, j = PAIRS[k]
    R = rho(i, j)
    res_moduleK = max(res_moduleK, float(np.linalg.norm(Kful @ R + R.conj().T @ Kful)))
check(f"A2: full 1792-dim module rho pseudo-anti-Hermitian wrt K (spot check {len(spot)} generators)",
      res_moduleK, TOL_BIG)

# (A3) Killing form of so(9,5): via structure constants (true Killing), cross-checked against trace forms
admats = np.transpose(cten, (0, 2, 1))                            # ad_i[k,j] = c[i,j,k]
Bkill = np.einsum("iab,jba->ij", admats, admats).real
Bkill = 0.5 * (Bkill + Bkill.T)
Gvec = np.einsum("iab,jba->ij", Vmats, Vmats).real
Gspin = np.einsum("iab,jba->ij", Smats, Smats)
check("A3: spinor trace form imaginary part (must be real)", float(np.abs(Gspin.imag).max()), TOL)
Gspin = Gspin.real
mask = np.abs(Gvec) > 1e-8
r1 = Bkill[mask] / Gvec[mask]
r2 = Gspin[mask] / Gvec[mask]
print(f"  A3: Killing = c * trace_vector with c = {r1.mean():.6f} (spread {r1.max()-r1.min():.2e}); "
      f"trace_spinor = c' * trace_vector with c' = {r2.mean():.6f} (spread {r2.max()-r2.min():.2e})")
check("A3: Killing/vector-trace proportionality constant (positive, so signatures agree)", float(r1.min()), 0.0, "gt")
kev_all = np.linalg.eigvalsh(Bkill)
kp, km = int(np.sum(kev_all > 1e-8)), int(np.sum(kev_all < -1e-8))
print(f"  A3: Killing signature of so(9,5) on the 91-dim algebra: ({kp} positive, {km} negative)")
check_eq("A3: Killing positive directions (noncompact boosts 9x5)", kp, 45)
check_eq("A3: Killing negative directions (compact so(9)+so(5))", km, 46)
print("  => the gauge sector is genuinely NONCOMPACT/indefinite on the carrier: the fourth seat is a real seat.")

# (A4) theta: existence, involution, automorphism, and the definiteness split
T5 = I128.copy()
for t in sorted(TIMELIKE):
    T5 = T5 @ e[t]
ThetaS = 1j * T5 if np.linalg.norm(T5.conj().T + T5) < 1e-9 else T5   # Hermitian involution normalization
check("A4: Theta_S (timelike-gamma product, normalized) squares to I", float(np.linalg.norm(ThetaS @ ThetaS - I128)), TOL)
check("A4: Theta_S Hermitian", float(np.linalg.norm(ThetaS - ThetaS.conj().T)), TOL)
res_theta_T = max(np.linalg.norm(ThetaS @ Smats[k] @ ThetaS - theta_sign[k] * Smats[k]) for k in range(91))
check("A4: conjugation by timelike product implements the split theta (+1 on so(9)+so(5), -1 mixed)",
      float(res_theta_T), TOL)
res_theta_b = max(np.linalg.norm(bS @ Smats[k] @ bS - theta_sign[k] * Smats[k]) for k in range(91))
check("A4: conjugation by beta_S (spacelike product) implements the SAME theta", float(res_theta_b), TOL)
res_theta_v = max(np.linalg.norm(etaV @ Vmats[k] @ etaV - theta_sign[k] * Vmats[k]) for k in range(91))
check("A4: conjugation by eta_V implements theta on the vector rep", float(res_theta_v), TOL)
check("A4: theta^2 = id (sign vector squares to 1)", float(np.abs(theta_sign ** 2 - 1.0).max()), TOL)
# bracket automorphism on random pairs (theta applied via basis signs)
res_auto = 0.0
for _ in range(20):
    x = rng.standard_normal(91)
    y = rng.standard_normal(91)
    X = np.tensordot(x, Smats, axes=(0, 0))
    Y = np.tensordot(y, Smats, axes=(0, 0))
    tX = np.tensordot(x * theta_sign, Smats, axes=(0, 0))
    tY = np.tensordot(y * theta_sign, Smats, axes=(0, 0))
    br = X @ Y - Y @ X
    # theta[X,Y]: expand bracket in basis, flip signs
    coef = (np.linalg.pinv(Smats.reshape(91, -1).T) @ br.reshape(-1))
    tbr = np.tensordot(coef.real * theta_sign, Smats, axes=(0, 0))
    res_auto = max(res_auto, float(np.linalg.norm(tbr - (tX @ tY - tY @ tX))))
check("A4: theta is a bracket automorphism, ||theta[X,Y] - [theta X, theta Y]|| over 20 random pairs",
      res_auto, 1e-8)
# definiteness split
even_idx = theta_sign > 0
odd_idx = theta_sign < 0
ev_even = np.linalg.eigvalsh(Bkill[np.ix_(even_idx, even_idx)])
ev_odd = np.linalg.eigvalsh(Bkill[np.ix_(odd_idx, odd_idx)])
print(f"  A4: Killing on theta-even part (dim {int(even_idx.sum())}): eigenvalue range "
      f"[{ev_even.min():.3f}, {ev_even.max():.3f}]  (negative-definite = compact so(9)+so(5))")
print(f"  A4: Killing on theta-odd part  (dim {int(odd_idx.sum())}): eigenvalue range "
      f"[{ev_odd.min():.3f}, {ev_odd.max():.3f}]  (positive-definite = boosts)")
check("A4: Killing NEGATIVE-definite on theta-even (max eig < 0)", float(-ev_even.max()), 0.0, "gt")
check("A4: Killing POSITIVE-definite on theta-odd (min eig > 0)", float(ev_odd.min()), 0.0, "gt")
Btheta = -(Bkill * theta_sign[None, :])
check("A4: B_theta symmetric (Killing theta-invariance)", float(np.abs(Btheta - Btheta.T).max()), 1e-8)
bt_min = float(np.linalg.eigvalsh(Btheta).min())
print(f"  A4: B_theta(X,Y) = -B(X, theta Y): min eigenvalue {bt_min:.3f}")
check("A4: B_theta POSITIVE-DEFINITE (the Gupta-Bleuler-style consistency structure exists)", bt_min, 0.0, "gt")

# ================================================================ SECTION B: SEAT INTERPLAY ON W
print("\n--- SECTION B: THE SEAT QUESTION -- theta vs the matter structures on W (induced conjugation) ---")

# (B1) the module implementation of theta IS the Krein form K = eta_V (x) beta_S
res_KimplV = res_theta_v          # eta_V side, shown above
res_KimplS = res_theta_b          # beta_S side, shown above
res_Kimpl_full = 0.0
for k in spot:
    i, j = PAIRS[k]
    R = rho(i, j)
    res_Kimpl_full = max(res_Kimpl_full,
                         float(np.linalg.norm(Kful @ R @ Kful - theta_sign[k] * R)))
check("B1: K rho(X) K^{-1} = rho(theta X) on the 1792-dim module (spot check; factor checks exact above)",
      res_Kimpl_full, TOL_BIG)
res_negdag = max(np.linalg.norm(Smats[k].conj().T + theta_sign[k] * Smats[k]) for k in range(91))
check("B1: theta X = -X^dagger generator-wise (so pseudo-anti-Hermiticity IS the Cartan involution)",
      float(res_negdag), TOL)
print("  => FINDING: the Krein form K itself implements the Cartan involution on the gauge algebra.")

# second implementation (timelike product) differs from K exactly by the spinor chirality
om = I128.copy()
for a in range(N):
    om = om @ e[a]
om2 = (np.trace(om @ om) / DIM).real
chiS = om if om2 > 0 else (-1j) * om
Cful = np.kron(I14, chiS)
prod = bS @ chiS
cfit = np.trace(prod.conj().T @ ThetaS) / np.trace(prod.conj().T @ prod)   # <prod, ThetaS>/<prod, prod>
res_two = float(np.linalg.norm(ThetaS - cfit * prod))
print(f"  B1: Theta_S(timelike) = c * beta_S * chi_S with c = {cfit:.4f} (residual {res_two:.1e}):")
check("B1: the two theta implementations differ exactly by the chirality operator", res_two, TOL)

# (B2) interplay residuals: [Theta, K], {Theta, K}, [Theta, chi], {Theta, chi}
def comm(A, B):
    return A @ B - B @ A


def acomm(A, B):
    return A @ B + B @ A


c_bK = float(np.linalg.norm(comm(bS, bS)))        # K-implementation vs K on spinor side: trivially 0
c_chi_c = float(np.linalg.norm(comm(bS, chiS)))
c_chi_a = float(np.linalg.norm(acomm(bS, chiS)))
print(f"  B2: spinor side, K-implementation (beta_S) vs chirality chi_S: ||[.,.]|| = {c_chi_c:.3e}, "
      f"||{{.,.}}|| = {c_chi_a:.3e}")
check("B2: theta(K-implementation) ANTIcommutes with chirality", c_chi_a, TOL)
check("B2: (control that the commutator does NOT vanish)", c_chi_c, 1.0, "gt")
t_chi_c = float(np.linalg.norm(comm(ThetaS, chiS)))
t_chi_a = float(np.linalg.norm(acomm(ThetaS, chiS)))
print(f"  B2: spinor side, timelike implementation vs chi_S: ||[.,.]|| = {t_chi_c:.3e}, ||{{.,.}}|| = {t_chi_a:.3e}")
check("B2: BOTH implementations anticommute with chirality (theta is chirality-odd on W)", t_chi_a, TOL)

# (B3) J_quat: the phase-unique quaternionic (antilinear) structure commuting with so(9,5)
def quaternionic_J(seed=1):
    ETA = np.array([(-1.0 if a in TIMELIKE else 1.0) for a in range(N)])

    def Phi(Um):
        out = np.zeros_like(Um)
        for a in range(N):
            out += ETA[a] * (e[a] @ Um @ e[a].conj())
        return out / N

    r = np.random.default_rng(seed)
    Um = r.standard_normal((DIM, DIM)) + 1j * r.standard_normal((DIM, DIM))
    for _ in range(400):
        Um = 0.5 * (Um + Phi(Um))
        Um /= np.linalg.norm(Um)
    Us, _, Vs = np.linalg.svd(Um)
    Um = Us @ Vs
    return Um / np.sqrt(abs(np.trace(Um @ Um.conj()) / DIM))


Uq = quaternionic_J(seed=1)
res_qint = max(float(np.linalg.norm(Uq @ e[a].conj() - e[a] @ Uq)) for a in range(N))
jj = Uq @ Uq.conj()
jsq = (np.trace(jj) / DIM).real
check("B3: J_quat intertwines the Clifford action (U conj(e_a) = e_a U, all a)", res_qint, 1e-6)
check("B3: J_quat^2 = -1 (quaternionic, M(64,H))", float(np.linalg.norm(jj + I128)), 1e-6)
q_c = float(np.linalg.norm(bS @ Uq - Uq @ bS.conj()))
q_a = float(np.linalg.norm(bS @ Uq + Uq @ bS.conj()))
print(f"  B3: theta(K-impl) vs J_quat (antilinear): ||Theta j - j Theta|| = {q_c:.3e}, "
      f"||Theta j + j Theta|| = {q_a:.3e}")
q2_c = float(np.linalg.norm(ThetaS @ Uq - Uq @ ThetaS.conj()))
q2_a = float(np.linalg.norm(ThetaS @ Uq + Uq @ ThetaS.conj()))
print(f"  B3: theta(timelike impl) vs J_quat: ||Theta j - j Theta|| = {q2_c:.3e}, ||Theta j + j Theta|| = {q2_a:.3e}")
jq_verdict = "commutes" if q_c < 1e-6 else ("anticommutes" if q_a < 1e-6 else "neither")
if min(q_c, q_a) > 1e-6:
    FAILURES.append("B3: theta vs J_quat has no definite parity")
print(f"  B3: theta {jq_verdict} with the quaternionic structure (as antilinear maps).")

# (B4) theta vs the constraint surface and the family action; theta vs P_ghost on the triplet
res_Pi = float(np.linalg.norm(comm(Kful, Pi)))
check("B4: [Theta_W, Pi] = 0 (theta preserves ker(Gamma))", res_Pi, TOL_BIG)
res_J3 = max(float(np.linalg.norm(comm(Kful, Jx))) for Jx in J3)
check("B4: [Theta_W, SU(2)+ family action] = 0 (theta respects the generation triplet)", res_J3, TOL_BIG)
Pt = Wt @ Wt.conj().T
res_stab = float(np.linalg.norm((np.eye(N * DIM) - Pt) @ (Kful @ Wt)))
check("B4: Theta_W stabilizes the 192-dim triplet sector", res_stab, TOL_BIG)
Theta_t = Wt.conj().T @ Kful @ Wt
Theta_t = 0.5 * (Theta_t + Theta_t.conj().T)
res_inv = float(np.linalg.norm(Theta_t @ Theta_t - np.eye(Theta_t.shape[0])))
check("B4: Theta_t^2 = I on the triplet (restriction is a genuine involution)", res_inv, TOL_BIG)
kev, kU = np.linalg.eigh(Kt)
Pg = (kU * np.sign(kev)) @ kU.conj().T
Pg = 0.5 * (Pg + Pg.conj().T)
res_id = float(np.linalg.norm(Pg - Theta_t))
print(f"  B4: canonical ghost parity P_ghost = sign(K_t); eigenvalues of K_t lie in "
      f"[{np.abs(kev).min():.6f}, {np.abs(kev).max():.6f}] in modulus")
check("B4: P_ghost = Theta_t EXACTLY (ghost parity IS the restricted Cartan involution)", res_id, TOL_BIG)
Ct = Wt.conj().T @ Cful @ Wt
Ct = 0.5 * (Ct + Ct.conj().T)
res_ca = float(np.linalg.norm(acomm(Theta_t, Ct)))
res_cc = float(np.linalg.norm(comm(Theta_t, Ct)))
print(f"  B4: on the triplet, ||{{Theta_t, chi}}|| = {res_ca:.3e}, ||[Theta_t, chi]|| = {res_cc:.3e}")
check("B4: Theta_t anticommutes with chirality on the triplet", res_ca, TOL_BIG)
check("B4: (=> theta-eigenspaces chirality-balanced: consistency-not-chirality reproduced)", res_cc, 1.0, "gt")
tt = float(np.trace(Theta_t).real)
check("B4: tr(Theta_t) = 0 (signature (+96,-96), matching the anchor)", abs(tt), TOL_BIG)

# ================================================================ SECTION C: THE PUNCHLINE
print("\n--- SECTION C: PUNCHLINE -- the theta-even sector IS the maximal-compact chain ---")
print("  Internal block realized by THIS carrier: (9,5) = base(4,0) + internal(5,5) -> so(5,5).")
print("  [Weinstein's named chain [00:45:00]: SM = max compact of SU(3,2); Pati-Salam = max compact of")
print("   Spin(6,4). The (6,4) fiber (trace reversal, transcript [00:43:47]) is NOT natively realized")
print("   by this (9,5) build; it is verified below on a theta-stable so(6,4) SUB-block of so(9,5),")
print("   plus a standalone su(3,2) fundamental. Lie-algebra level only.]")


def subalgebra(mats, label, expect_dim=None):
    """Analyze a real Lie algebra spanned by mats (list of matrices, real span).
    Returns (closure_residual, killing_eigs, rank)."""
    A = np.array(mats)
    k = A.shape[0]
    Aflat = A.reshape(k, -1)
    Apinv = np.linalg.pinv(Aflat)
    br = np.einsum("iab,jbc->ijac", A, A) - np.einsum("jab,ibc->ijac", A, A)
    cc = br.reshape(k, k, -1) @ Apinv
    res_close = float(np.abs(br.reshape(k, k, -1) - cc @ Aflat).max())
    check(f"{label}: closes as a Lie algebra (dim {k}), residual", res_close, 1e-8)
    ccr = cc.real
    check(f"{label}: structure constants real", float(np.abs(cc.imag).max()), 1e-8)
    ad = np.transpose(ccr, (0, 2, 1))
    B = np.einsum("iab,jba->ij", ad, ad)
    B = 0.5 * (B + B.T)
    kev = np.linalg.eigvalsh(B)
    ranks = []
    for sd in (3, 4):
        r = np.random.default_rng(sd)
        x = r.standard_normal(k)
        adX = np.tensordot(x, ad, axes=(0, 0))
        ranks.append(k - int(np.linalg.matrix_rank(adX, tol=1e-8 * max(1.0, float(np.abs(adX).max())))))
    if expect_dim is not None:
        check_eq(f"{label}: dimension", k, expect_dim)
    return res_close, kev, ranks


def compact_simple_report(mats, label, expect_dim, expect_rank):
    _, kev, ranks = subalgebra(mats, label, expect_dim)
    check(f"{label}: own Killing NEGATIVE-definite (compact), max eig < 0", float(-kev.max()), 0.0, "gt")
    check_eq(f"{label}: rank (generic-centralizer dim, 2 seeds agree)", ranks[0], expect_rank)
    check_eq(f"{label}: rank seed 2", ranks[1], expect_rank)


# (C1) theta-even part of the internal so(5,5): so(5) + so(5)
int_time = sorted(TIMELIKE)                       # {4..8}
int_space = [9, 10, 11, 12, 13]
F1 = [sgen(i, j) for a, i in enumerate(int_time) for j in int_time[a + 1:]]
F2 = [sgen(i, j) for a, i in enumerate(int_space) for j in int_space[a + 1:]]
print(f"\n  C1: internal block so(5,5) (indices {int_time} timelike + {int_space} spacelike), dim "
      f"{len(int_time+int_space)*(len(int_time+int_space)-1)//2}; theta-even part = "
      f"{{both-timelike}} + {{both-spacelike}}: dims {len(F1)} + {len(F2)} = {len(F1)+len(F2)} (measured)")
compact_simple_report(F1, "C1 factor 1 (timelike pairs)", 10, 2)
compact_simple_report(F2, "C1 factor 2 (internal-spacelike pairs)", 10, 2)
res_mut = max(float(np.linalg.norm(comm(x, y))) for x in F1 for y in F2)
check("C1: the two factors commute (direct sum)", res_mut, TOL)
print("  C1: classification (dims/ranks MEASURED; table from memory -- standard Cartan classification:")
print("      compact semisimple, rank 2: su(2)+su(2) has dim 6; the only rank-2 compact algebra of dim 10")
print("      is the simple so(5) = sp(2)). => theta-even(so(5,5)) = so(5) + so(5) = max compact of Spin(5,5)")
print("      (theta-even of a Cartan involution = maximal compact: standard theory, from memory).")

# the so(5,5) block's own B_theta > 0
int_all = int_time + int_space
blk_pairs = [(i, j) for a, i in enumerate(int_all) for j in int_all[a + 1:]]
blk_mats = [sgen(i, j) for (i, j) in blk_pairs]
blk_sign = np.array([1.0 if ((i in TIMELIKE) == (j in TIMELIKE)) else -1.0 for (i, j) in blk_pairs])
_, blk_kev, _ = subalgebra(blk_mats, "C1 so(5,5) block", 45)
Ablk = np.array(blk_mats).reshape(len(blk_mats), -1)
Apinv = np.linalg.pinv(Ablk)
brb = (np.einsum("iab,jbc->ijac", np.array(blk_mats), np.array(blk_mats))
       - np.einsum("jab,ibc->ijac", np.array(blk_mats), np.array(blk_mats)))
ccb = (brb.reshape(45, 45, -1) @ Apinv).real
adb = np.transpose(ccb, (0, 2, 1))
Bb = np.einsum("iab,jba->ij", adb, adb)
Bb = 0.5 * (Bb + Bb.T)
Btb = -(Bb * blk_sign[None, :])
check("C1: so(5,5) block B_theta positive-definite (min eig > 0)", float(np.linalg.eigvalsh(Btb).min()), 0.0, "gt")
kevb = np.linalg.eigvalsh(Bb)
print(f"  C1: so(5,5) own Killing signature: ({int(np.sum(kevb>1e-8))} positive / noncompact, "
      f"{int(np.sum(kevb<-1e-8))} negative / compact) [25 = 5x5 boosts, 20 = so(5)+so(5); measured]")

# (C2) theta-stable so(6,4) sub-block -> so(6) + so(4) = su(4) + su(2) + su(2) (Pati-Salam algebra)
sp6 = [3, 9, 10, 11, 12, 13]                      # six spacelike indices (theta-stable choice)
tm4 = [4, 5, 6, 7]                                # four timelike indices
print(f"\n  C2: theta-stable so(6,4) sub-block: spacelike {sp6} + timelike {tm4} "
      f"(documenting: NOT the native fiber; a sub-block of so(9,5) used for the Lie-algebra-level check)")
SO6 = [sgen(i, j) for a, i in enumerate(sp6) for j in sp6[a + 1:]]
SO4 = [sgen(i, j) for a, i in enumerate(tm4) for j in tm4[a + 1:]]
compact_simple_report(SO6, "C2 so(6) factor", 15, 3)
print("      rank-3 compact semisimple of dim 15: sums top out at 13 (so(5)+su(2)); the only option is the")
print("      simple su(4) = so(6) (dims/ranks measured; classification table from memory). => su(4).")
_, kev4, ranks4 = subalgebra(SO4, "C2 so(4) factor", 6)
check("C2 so(4): own Killing NEGATIVE-definite", float(-kev4.max()), 0.0, "gt")
check_eq("C2 so(4): rank", ranks4[0], 2)
# ideal split: self-dual / anti-self-dual combinations on the four timelike directions
t0, t1, t2, t3 = tm4
SDp = [sgen(t0, t1) + sgen(t2, t3), sgen(t0, t2) + sgen(t3, t1), sgen(t0, t3) + sgen(t1, t2)]
SDm = [sgen(t0, t1) - sgen(t2, t3), sgen(t0, t2) - sgen(t3, t1), sgen(t0, t3) - sgen(t1, t2)]
compact_simple_report(SDp, "C2 so(4) self-dual ideal", 3, 1)
compact_simple_report(SDm, "C2 so(4) anti-self-dual ideal", 3, 1)
res_sd = max(float(np.linalg.norm(comm(x, y))) for x in SDp for y in SDm)
check("C2: the two ideals commute (so(4) = su(2) + su(2), measured split)", res_sd, TOL)
res_mut64 = max(float(np.linalg.norm(comm(x, y))) for x in SO6 for y in SO4)
check("C2: so(6) and so(4) factors commute", res_mut64, TOL)
# so(6,4) block B_theta > 0
blk64 = sp6 + tm4
p64 = [(i, j) for a, i in enumerate(blk64) for j in blk64[a + 1:]]
m64 = np.array([sgen(i, j) for (i, j) in p64])
s64 = np.array([1.0 if ((i in TIMELIKE) == (j in TIMELIKE)) else -1.0 for (i, j) in p64])
A64 = m64.reshape(len(p64), -1)
br64 = np.einsum("iab,jbc->ijac", m64, m64) - np.einsum("jab,ibc->ijac", m64, m64)
cc64 = (br64.reshape(45, 45, -1) @ np.linalg.pinv(A64)).real
ad64 = np.transpose(cc64, (0, 2, 1))
B64 = np.einsum("iab,jba->ij", ad64, ad64)
B64 = 0.5 * (B64 + B64.T)
check("C2: so(6,4) sub-block B_theta positive-definite",
      float(np.linalg.eigvalsh(-(B64 * s64[None, :])).min()), 0.0, "gt")
print(f"  C2: so(6,4) own Killing signature: ({int(np.sum(np.linalg.eigvalsh(B64)>1e-8))} positive, "
      f"{int(np.sum(np.linalg.eigvalsh(B64)<-1e-8))} negative). NOTE: 24 here = 6x4 MEASURED boost-block")
print("      dimension (and 21 = 15+6 the compact part); neither number is used in any downstream formula.")
print("  => theta-even(so(6,4)) = su(4) + su(2) + su(2): the PATI-SALAM algebra, as the maximal compact")
print("     of Spin(6,4) -- Weinstein's [00:45:00] second chain link, verified at Lie-algebra level.")

# (C3) standalone su(3,2) fundamental -> s(u(3)+u(2)) = su(3) + su(2) + u(1) (SM algebra)
print("\n  C3: standalone su(3,2) check (5-dim fundamental; NOT carrier-native -- pure Lie-theory")
print("      verification of Weinstein's first chain link):")
eta5 = np.diag([1.0, 1.0, 1.0, -1.0, -1.0]).astype(complex)
basis32 = []
for kk in range(4):                                # traceless-eta diagonal combos
    Y = np.zeros((5, 5), dtype=complex)
    Y[kk, kk] = 1j
    Y[kk + 1, kk + 1] = -1j * (eta5[kk, kk] / eta5[kk + 1, kk + 1])
    basis32.append(eta5 @ Y)
for a in range(5):
    for b in range(a + 1, 5):
        Y = np.zeros((5, 5), dtype=complex)
        Y[a, b], Y[b, a] = 1, -1
        basis32.append(eta5 @ Y)
        Y2 = np.zeros((5, 5), dtype=complex)
        Y2[a, b], Y2[b, a] = 1j, 1j
        basis32.append(eta5 @ Y2)
res_su32 = max(float(np.linalg.norm(X.conj().T @ eta5 + eta5 @ X)) for X in basis32)
res_tr = max(abs(np.trace(X)) for X in basis32)
check("C3: basis satisfies X^dag eta + eta X = 0 and tr X = 0 (su(3,2))", max(res_su32, float(res_tr)), TOL)
check_eq("C3: dim su(3,2) [MEASURED: 24 = dim of the constructed basis; never an input]", len(basis32), 24)
th32 = [eta5 @ X @ eta5 for X in basis32]         # theta = Ad(eta): even iff block-diagonal
sgn32 = []
for X, tX in zip(basis32, th32):
    if np.linalg.norm(tX - X) < 1e-12:
        sgn32.append(1.0)
    elif np.linalg.norm(tX + X) < 1e-12:
        sgn32.append(-1.0)
    else:
        sgn32.append(0.0)
sgn32 = np.array(sgn32)
check("C3: theta = Ad(eta) is diagonal on the basis (+1/-1)", float(np.sum(sgn32 == 0.0)), 0.5)
evn = [X for X, s in zip(basis32, sgn32) if s > 0]
check_eq("C3: dim theta-even part [MEASURED]", len(evn), 12)
A32 = np.array(basis32).reshape(24, -1)
br32 = (np.einsum("iab,jbc->ijac", np.array(basis32), np.array(basis32))
        - np.einsum("jab,ibc->ijac", np.array(basis32), np.array(basis32)))
cc32 = (br32.reshape(24, 24, -1) @ np.linalg.pinv(A32))
check("C3: su(3,2) closes; structure constants real", float(np.abs(cc32.imag).max()), 1e-8)
ad32 = np.transpose(cc32.real, (0, 2, 1))
B32 = np.einsum("iab,jba->ij", ad32, ad32)
B32 = 0.5 * (B32 + B32.T)
check("C3: su(3,2) B_theta positive-definite", float(np.linalg.eigvalsh(-(B32 * sgn32[None, :])).min()), 0.0, "gt")
# center of the even part: v such that sum_i v_i [E_i, E_j] = 0 for all j
brm = np.array([[comm(evn[i], evn[j]).reshape(-1) for j in range(len(evn))] for i in range(len(evn))])
Mcen = brm.transpose(1, 2, 0).reshape(-1, len(evn))              # (j*entries, i)
scen = np.linalg.svd(Mcen, compute_uv=False)
dim_center = int(np.sum(scen < 1e-9 * scen.max()))
check_eq("C3: dim center of theta-even part [MEASURED: the u(1)]", dim_center, 1)
# derived algebra of the even part and its ideal split by eta-blocks
der = brm.reshape(-1, 25)
sder = np.linalg.svd(der, compute_uv=False)
dim_der = int(np.sum(sder > 1e-9 * sder.max()))
check_eq("C3: dim derived algebra of even part [MEASURED]", dim_der, 11)
blk3 = [X for X in evn if np.linalg.norm(X[3:, :]) + np.linalg.norm(X[:, 3:]) < 1e-12 and abs(np.trace(X)) < 1e-12]
blk2 = [X for X in evn if np.linalg.norm(X[:3, :]) + np.linalg.norm(X[:, :3]) < 1e-12 and abs(np.trace(X)) < 1e-12]
# supplement pure-block traceless combos from diagonal generators
def block_traceless(evn_list, sl, dim_blk):
    A = np.array([X.reshape(-1) for X in evn_list]).T
    # find combos supported purely on the block and traceless there
    mask = np.ones((5, 5), dtype=bool)
    mask[sl, sl] = False
    rowsM = [A[np.where(mask.reshape(-1))[0], :]]
    trrow = np.zeros((1, A.shape[1]), dtype=complex)
    for X_i in range(A.shape[1]):
        trrow[0, X_i] = np.trace(np.array(evn_list)[X_i][sl, sl])
    Mc = np.vstack(rowsM + [trrow])
    # nullspace over the REALS: su(3,2) is a real Lie algebra (real span of the basis); complex
    # coefficient combos would leave it and fake complex structure constants downstream
    Mreal = np.vstack([Mc.real, Mc.imag])
    _, sv, Vh = np.linalg.svd(Mreal)
    rank = int(np.sum(sv > 1e-9 * max(float(sv.max()), 1e-30)))
    null = Vh.T[:, rank:]
    combos = [np.tensordot(null[:, m], np.array(evn_list), axes=(0, 0)) for m in range(null.shape[1])]
    return combos


su3blk = block_traceless(evn, slice(0, 3), 3)
su2blk = block_traceless(evn, slice(3, 5), 2)
check_eq("C3: dim su(3)-block ideal [MEASURED: 8 = output dimension, never an input]", len(su3blk), 8)
check_eq("C3: dim su(2)-block ideal [MEASURED]", len(su2blk), 3)
compact_simple_report(su3blk, "C3 su(3) ideal", 8, 2)
compact_simple_report(su2blk, "C3 su(2) ideal", 3, 1)
res_32mut = max(float(np.linalg.norm(comm(x, y))) for x in su3blk for y in su2blk)
check("C3: the two ideals commute", res_32mut, 1e-8)
print("  => theta-even(su(3,2)) = su(3) + su(2) + u(1): the STANDARD MODEL algebra, as the maximal")
print("     compact of SU(3,2) -- Weinstein's [00:45:00] first chain link, verified at Lie-algebra level.")

# ================================================================ SECTION D: CONTROLS
print("\n--- SECTION D: CONTROLS (every headline check must be able to fail) ---")

# (D1) wrong-split involutions: conjugation by wrong gamma subsets -> automorphisms that FAIL positivity
print("  D1: conjugation by the product of a WRONG gamma subset S is still an involutive automorphism,")
print("      but its twisted form B_S = -B(X, theta_S X) must FAIL positive-definiteness:")
wrong_subsets = [
    {4, 5, 6, 7},               # four of the five timelike
    {0, 4, 5, 6, 8},            # mixed
    {0},                        # single spacelike
    {2, 3, 9, 10, 11},          # five spacelike
    {0, 1, 2, 3},               # the Euclidean base
    {4, 9},                     # one of each
    {0, 1, 4, 5, 6, 7, 8},      # timelike + two spacelike
    {5, 6, 7, 8, 9, 10, 11},    # shifted window
]
all_fail = True
for S in wrong_subsets:
    epsS = np.array([1.0 if ((i in S) == (j in S)) else -1.0 for (i, j) in PAIRS])
    # automorphism certificate (conjugations are always automorphisms; verify on one random pair)
    x = rng.standard_normal(91)
    y = rng.standard_normal(91)
    X = np.tensordot(x, Smats, axes=(0, 0))
    Y = np.tensordot(y, Smats, axes=(0, 0))
    tX = np.tensordot(x * epsS, Smats, axes=(0, 0))
    tY = np.tensordot(y * epsS, Smats, axes=(0, 0))
    br = X @ Y - Y @ X
    coef = (np.linalg.pinv(Smats.reshape(91, -1).T) @ br.reshape(-1)).real
    tbr = np.tensordot(coef * epsS, Smats, axes=(0, 0))
    auto_res = float(np.linalg.norm(tbr - (tX @ tY - tY @ tX)))
    BS = -(Bkill * epsS[None, :])
    BS = 0.5 * (BS + BS.T)     # symmetrize (theta_S-invariance of B makes the asymmetric part 0)
    mn = float(np.linalg.eigvalsh(BS).min())
    ok = mn < -1e-6 and auto_res < 1e-8
    all_fail &= ok
    print(f"      S = {sorted(S)}: automorphism residual {auto_res:.1e}, min eig(B_S) = {mn:+.3f} "
          f"[{'correctly FAILS positivity' if mn < -1e-6 else 'UNEXPECTED: positive'}]")
check_eq("D1: all wrong splits are automorphisms yet fail B_theta > 0 (check has power)", all_fail, True)

# identity involution also fails
mn_id = float(np.linalg.eigvalsh(-Bkill).min())
check("D1: theta = id fails positivity (min eig(-B) < 0)", -mn_id, 0.0, "gt")

# (D2) random +-1 sign patterns are generically NOT automorphisms
worst = np.inf
for _ in range(5):
    epsR = rng.choice([-1.0, 1.0], size=91)
    x = rng.standard_normal(91)
    y = rng.standard_normal(91)
    X = np.tensordot(x, Smats, axes=(0, 0))
    Y = np.tensordot(y, Smats, axes=(0, 0))
    tX = np.tensordot(x * epsR, Smats, axes=(0, 0))
    tY = np.tensordot(y * epsR, Smats, axes=(0, 0))
    br = X @ Y - Y @ X
    coef = (np.linalg.pinv(Smats.reshape(91, -1).T) @ br.reshape(-1)).real
    tbr = np.tensordot(coef * epsR, Smats, axes=(0, 0))
    worst = min(worst, float(np.linalg.norm(tbr - (tX @ tY - tY @ tX))))
check("D2: random sign patterns FAIL the bracket-automorphism test (min residual over 5 draws)",
      float(worst), 0.1, "gt")

# (D3) the fixed subalgebra of a wrong split is NOT compact (max-compact identification has power)
Swr = {0, 4, 5, 6, 8}
epsS = np.array([1.0 if ((i in Swr) == (j in Swr)) else -1.0 for (i, j) in PAIRS])
fixed = [Smats[k] for k in range(91) if epsS[k] > 0]
Af = np.array(fixed).reshape(len(fixed), -1)
brf = (np.einsum("iab,jbc->ijac", np.array(fixed), np.array(fixed))
       - np.einsum("jab,ibc->ijac", np.array(fixed), np.array(fixed)))
ccf = (brf.reshape(len(fixed), len(fixed), -1) @ np.linalg.pinv(Af))
res_fclose = float(np.abs(brf.reshape(len(fixed), len(fixed), -1) - ccf @ Af).max())
adf = np.transpose(ccf.real, (0, 2, 1))
Bf = np.einsum("iab,jba->ij", adf, adf)
Bf = 0.5 * (Bf + Bf.T)
mxf = float(np.linalg.eigvalsh(Bf).max())
print(f"  D3: wrong-split fixed subalgebra (S = {sorted(Swr)}): dim {len(fixed)}, closure residual "
      f"{res_fclose:.1e}, max Killing eig = {mxf:+.3f}")
check("D3: wrong-split fixed subalgebra closes (it IS a subalgebra)", res_fclose, 1e-8)
check("D3: ...but is NOT compact (max Killing eig > 0) -- identification check has power", mxf, 1e-6, "gt")

# (D4) K restricted to a RANDOM 192-dim subspace does not square to I (P_ghost = Theta_t is not a tautology)
rr = np.random.default_rng(7)
Mr = rr.standard_normal((N * DIM, 192)) + 1j * rr.standard_normal((N * DIM, 192))
Qr, _ = np.linalg.qr(Mr)
Kr = Qr.conj().T @ Kful @ Qr
res_rand = float(np.linalg.norm(Kr @ Kr - np.eye(192)))
check("D4: ||(K|_random-192)^2 - I|| LARGE (triplet K-stability is a real property, not automatic)",
      res_rand, 0.1, "gt")

# ================================================================ SUMMARY
print("\n" + "=" * 100)
print("SUMMARY")
print("=" * 100)
print("""  (A) The gauge sector so(9,5) is genuinely indefinite on the carrier (Killing signature 45+/46-),
      and the Cartan involution theta exists concretely: conjugation by the timelike-gamma product
      (equivalently by beta_S), theta^2 = id, bracket automorphism, Killing negative-definite on
      theta-even / positive-definite on theta-odd, B_theta > 0. The fourth seat HAS a GU-native
      candidate occupant, and it is the Gupta-Bleuler-style move.
  (B) The module implementation of theta IS the Krein form K (pseudo-anti-Hermiticity = Cartan
      involution); theta preserves ker(Gamma) and the triplet, commutes with the family action,
      anticommutes with chirality, and restricted to the triplet EQUALS the canonical ghost parity
      P_ghost = sign(K_t). The fourth seat and the quantization seat are the same Z2 -- kinematically.
  (C) The theta-even (physical/compact) sector is exactly the maximal-compact chain: so(5)+so(5) for
      the carrier's own internal so(5,5); su(4)+su(2)+su(2) (Pati-Salam) for a theta-stable so(6,4)
      sub-block; su(3)+su(2)+u(1) (SM) for the standalone su(3,2) fundamental. Weinstein's punchline
      [00:45:00] is the theta-even sector of the Gupta-Bleuler move.
  (D) Controls: wrong splits fail positivity, random sign patterns fail automorphism, wrong fixed
      subalgebras fail compactness, random subspaces fail K^2 = I. Every headline check can fail.
  OPEN + GATED: whether theta/K commutes with any actual dynamics S ([theta, S] = 0) cannot be checked
      (GU supplies no S); the PT/C-operator derivation of such a structure and the conformal-fiber
      questions belong to the separate running big-swing workflow (R1-R4) -- gates only, no outcomes
      cited here. Chirality is NOT claimed: theta anticommutes with chirality, reproducing
      consistency-not-chirality (canon/swing-ghost-parity-no-chiral-selection.md).
  TARGET-IMPORT GUARD: {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} -- none assumed, inserted,
      or divided by. All small dimensions above (3, 8, 12, 15, 20, 24, ...) are MEASURED outputs.""")

if FAILURES:
    print(f"\nRESULT: {len(FAILURES)} CHECK(S) FAILED:")
    for f in FAILURES:
        print(f"  - {f}")
    sys.exit(1)
print("\nRESULT: ALL CHECKS PASS (exit 0)")
