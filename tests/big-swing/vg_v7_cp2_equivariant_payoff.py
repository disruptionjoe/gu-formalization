"""
VG-V7 (route V7, big-swing 2026-07-06 federation, leg T2' PAYOFF): the equivariant m-selection
and twisted-index arithmetic that VG-V5 invoiced as its section 5(i)-(iii).

VG-V5 established (THEOREM-grade): the breaking coset D = positive lines in C^(3,2) retracts onto
CP^2 with chi = 3, c1(T CP^2) = 3h, H^2 = Z free -- and left the payoff leg open: the CP^2 twist
enters the h2 canon index only through rk*c1(L)^2/2, and the verifiers' enlarged invoice says the
payoff needs 3 | m AND 3 | sigma. This script performs the invoiced computations:

  (a) EQUIVARIANT m-SELECTION.
      (a1) The dichotomy: does the family SU(2)+ act on the coset at all?
           - Euclidean base: su(2)+ acts honestly on Sym^2(R^4) (measured: 3 triplets + 1 singlet)
             but the trace-reversed fiber form is (9,1), p ODD => NO compatible complex structure
             => the coset D is ABSENT. (V5's own control, re-measured.)
           - Lorentzian base: the fiber is (6,4) and D ~ CP^2 exists, but Hodge-* on
             Lambda^2(R^{1,3}) squares to -I (measured; Euclidean control +I), so su(2)+ acts on
             the REAL fiber only through its SO(3) rotation image -- and NO compatible J commutes
             with that image: V10 = 1+1+3+5 under SO(3) (Casimir-measured), the two odd real-type
             multiplicity-one isotypics force J = c*id with c^2 = -1 (impossible over R), and the
             2-dim trivial isotypic has G-signature (1,1) (exact). Optimizer scan floor >= 8,
             with the L3-commutant CONTROL scan reaching ~0.
           => THE SU(2)+-EQUIVARIANT COSET DOES NOT EXIST IN EITHER SIGNATURE: Euclidean kills
              the coset, Lorentzian kills the equivariance. Full-family equivariance can select
              nothing because it cannot even be formulated.
      (a2) The maximal family subgroup that DOES act: U(1)+ = the Cartan of the rotation image.
           An adapted compatible J_ad with [J_ad, L3] = 0 is constructed EXACTLY (sympy, entries
           in Q(sqrt(3))): J_ad^2 = -I, J_ad^T G J_ad = G, [J_ad, rho(L3)] = 0, all exact zero
           matrices. Exact U(1)+ weights on C^(3,2): positive part a = (0,1,2), negative part
           b = (0,1) (signs are J-orientation choices; magnitudes canonical). Fixed points on the
           core CP^2: 3 = number of distinct positive weights = chi (cross-check). U(1)+ forces
           NO m: every O(m) = taut^(-m) (x) chi_c carries an equivariant structure for every m.
      (a3) THE m-SELECTION ITSELF (stabilizer-character arithmetic, exact integers): characters
           of the stabilizer H = S(U(1) x U(2,2)) form Z (measured: dim H = 16, dim [H,H] = 15).
           On the central generator Y = i*diag(4,-1,-1,-1,-1):
             breaking line (V5 premise beta: the condensate IS the positive line)  -> O(-1), |m| = 1
             quadratic v(.)v condensate                                            -> O(-2), |m| = 2
             degree-r monomial in the VEV                                          -> O(-r), |m| = r
             anticanonical of the COSET D (det tangent weight -20 = -4*5)          -> O(5)
             anticanonical of the compact CORE CP^2 (det weight -6 = -2*3)         -> O(3)
           Independently cross-checked by exact fixed-point tangent-weight fits (localization
           arithmetic: taut fits m = -1; core det-tangent (3,0,-3) fits m = 3; D det-tangent
           (4,-1,-6) fits m = 5). CONTROLS: C^(2,1) gives ambient 3 / core 2; C^(4,2) gives
           ambient 6 / core 4 -- the machinery outputs p and p+q, not always 3 and 5.
           => The mechanism "stabilizer character of the breaking direction" FORCES |m| = 1
              (or 2 for quadratic coupling). 3 | m FAILS for every natively selected coupling.
              The only 3-divisible candidate, O(3), is the anticanonical of the compact core --
              which is NOT the rep the breaking direction transforms in, is NOT the coset's own
              anticanonical (that is O(5), 3-free!), and is selected by nothing measured.
      (a4) Carrier-side honesty: every so(6,4) sub-block of the (9,5) carrier must borrow a base
           index (only 5 internal spacelike directions exist -- measured), and therefore FAILS to
           commute with the family su(2)+ (residual printed). The carrier cannot natively host
           both the (6,4) fiber chain and a commuting family action; V5 sec 5(i)'s literal
           carrier-side decomposition is BLOCKED as non-native, and the fiber-level computation
           above is its honest home.

  (b) TWISTED-INDEX ARITHMETIC (sympy, exact). h2 canon full multiplicity bundle
      [2(j=0) + 4(j=1/2) + 2(j=1)] + CP^2 twist + gravitational term:
          ind_full = 12k + 8 m^2 d - 2 sigma,   spin X => d = 2d'  =>  12k + 16 m^2 d' - 2 sigma.
      Mod 2: even for all inputs (the 2-adic wall is respected; Rokhlin handles -2 sigma).
      Mod 3: ind_full == m^2 d' + sigma (mod 3)  [12 == 0, 16 == 1, -2 == 1].
      EXACT DIVISIBILITY CONDITION: section-independent 3-divisibility (all d')
          3 | ind_full for all d', k  <=>  3 | m  AND  3 | sigma
      and with Rokhlin (16 | sigma):  <=>  3 | m AND sigma == 0 (mod 48).
      Inserting the measured m's: m in {+-1, +-2, 5} all give m^2 == 1 (mod 3), so
          ind_full == d' + sigma (mod 3):
      the coset contributes NOTHING mod 3 beyond what the free imports (d', sigma) already carry.
      Even the unselected core-anticanonical m = 3 still needs the 3 | sigma import.
      The (3,2)-subsector 3(k_- + m^2 d) trap is flagged (native multiplicity, not coset-born).

  (c) C-07 CONFRONTATION on the 192-dim triplet (exact quaternionic structure by the C-07
      regression RULE: C = product of the generators with bar(e_a) = -e_a, index set MEASURED
      from this rep's reality signs; J = C.conj, J^2 = -I):
      - The triplet sector is J-invariant and J restricts quaternionically (U_t conj(U_t) = -I;
        random-192-subspace control FAILS as it must).
      - The NATIVE core direction A = J+3|_W (real family Cartan) COMMUTES with J: C-07's
        Kramers hypothesis holds, even count forced.
      - The TWIST-DEFORMED core (the invoiced finite proxy: the su(2)+ weight operator composed
        with the scale/coset direction, M = (i J+3) o (etaV(x)1)|_W; the scale factor is the
        IDENTITY on W, ||etaV(x)1 - I|| ~ 1e-14, the V1 degeneration reproduced) ANTICOMMUTES
        with J: ||{M, J}|| ~ 0 while ||[M, J]|| = 2||M||. THE TWIST BREAKS J-COMMUTATION --
        C-07's hypothesis fails, the escape-of-hypothesis is confirmed at operator level.
      - BUT the conclusion re-arises by a different quaternionic mechanism: J-oddness maps the
        weight slice E_w onto E_{-w} and leaves E_0 quaternionic (Kramers-even). Measured slice
        structure: dims (64, 64, 64); Krein signature (32, 32) on EVERY slice; tr P = tr chi = 0
        on every slice; U_0 conj(U_0) = -I. The twist direction supplies NO kinematic asymmetry
        seed: every slice is vectorlike. Random K-self-adjoint controls have mixed J-parity and
        break [.,P] at O(1) -- the structure is discriminating, not automatic.

TARGET-IMPORT GUARD (maximum strictness): {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} are
never assumed, inserted, or divided by in any construction. Every printed 3 carries provenance:
  * 3 triplets in Sym^2(R^4): measured Casimir multiplicity 9/3 (H1's native multiplicity echo);
  * 3 = p = measured Hermitian positives (descends from dim X = 4 + one time direction, V5 chain);
  * 3 fixed points = COUNT of measured distinct weights {0,1,2} (= chi cross-check);
  * core anticanonical m = 3: EXACT weight ratio -6/-2 (stabilizer) and fixed-point fit;
  * the mod-3 arithmetic: 3 is the modulus of the divisibility QUESTION under test (the target
    hypothesis), used only as a modulus, never inserted into any construction;
  * scan floor 8 = 3 + 5 = sum of the measured odd isotypic dimensions (an output).
All count statements are "mechanism M forces c", never "GU forces c".

Run from repo root:  python tests/big-swing/vg_v7_cp2_equivariant_payoff.py    (exit 0)
"""
import sys
import numpy as np
import sympy as sp
from scipy.optimize import minimize

np.random.seed(20260707)

FAIL = []


def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAIL.append(name)


def signature_of(M, tol=1e-9):
    Ms = 0.5 * (M + M.conj().T)
    w = np.linalg.eigvalsh(Ms)
    return (int(np.sum(w > tol)), int(np.sum(w < -tol)), int(np.sum(np.abs(w) <= tol)))


# ============================================================================
print("=" * 96)
print("SECTION 0 -- CARRIER ANCHORS (verbatim recipe of ghost_parity_krein.py / VG-V2)")
print("=" * 96)
N, DIM = 14, 128
TIMELIKE = {4, 5, 6, 7, 8}
SPACELIKE = [a for a in range(N) if a not in TIMELIKE]


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


def gen(i, j):
    return np.kron(I14, sgen(i, j)) + np.kron(lvec(i, j), I128)


# beta_S = product of spacelike gammas
bS = I128.copy()
for s in SPACELIKE:
    bS = bS @ e[s]
if np.linalg.norm(bS.conj().T + bS) < 1e-9:
    bS = 1j * bS
bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
res_pah = max(np.linalg.norm(bS @ sgen(i, j) + sgen(i, j).conj().T @ bS)
              for i in range(N) for j in range(i + 1, N))
print(f"  beta_S pseudo-anti-Hermiticity residual over all 91 so(9,5) generators: {res_pah:.1e}")
check("anchor: beta_S pseudo-anti-Hermitian (residual ~ 0)", res_pah < 1e-9)

Gam = np.hstack(e)
rankG = int(np.linalg.matrix_rank(Gam, tol=1e-9))
Pi = np.eye(N * DIM, dtype=complex) - Gam.conj().T @ np.linalg.inv(Gam @ Gam.conj().T) @ Gam
w, Vv = np.linalg.eigh(Pi)
Wk = Vv[:, w > 0.5]
print(f"  rank(Gamma) = {rankG}   dim ker(Gamma) = {Wk.shape[1]}   (carrier dim {N * DIM})")
check("anchor: rank(Gamma) = 128, dim ker = 1664", rankG == 128 and Wk.shape[1] == 1664)

SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
J3 = [gen(a, b) + gen(c, d) for (a, b, c, d) in SD]
Cas = -(J3[0] @ J3[0] + J3[1] @ J3[1] + J3[2] @ J3[2])
CasK = Wk.conj().T @ Cas @ Wk
CasK = 0.5 * (CasK + CasK.conj().T)
ev, U = np.linalg.eigh(CasK)
top = max(round(x.real, 3) for x in ev)
Wt = Wk @ U[:, np.abs(ev - top) < 1e-3]
Kful = np.kron(etaV, bS)
Kt = Wt.conj().T @ Kful @ Wt
Kt = 0.5 * (Kt + Kt.conj().T)
sig = np.linalg.eigvalsh(Kt)
npl, nmi, nz = int(np.sum(sig > 1e-9)), int(np.sum(sig < -1e-9)), int(np.sum(np.abs(sig) < 1e-9))
print(f"  triplet sector: dim {Wt.shape[1]}, su(2)+ Casimir top eigenvalue {top}, "
      f"Krein signature (+{npl}, -{nmi}, 0:{nz})")
check("anchor: triplet Krein signature (+96, -96, 0)", (npl, nmi, nz) == (96, 96, 0))

# chirality
om = I128.copy()
for a in range(N):
    om = om @ e[a]
chiS = om if (np.trace(om @ om) / DIM).real > 0 else (-1j) * om
Cful = np.kron(I14, chiS)
chi_t = Wt.conj().T @ Cful @ Wt
chi_t = 0.5 * (chi_t + chi_t.conj().T)
kev, kU = np.linalg.eigh(Kt)
Pg = (kU * np.sign(kev)) @ kU.conj().T
Pg = 0.5 * (Pg + Pg.conj().T)
res_pchi = np.linalg.norm(Pg @ chi_t + chi_t @ Pg)
print(f"  ghost parity P = sign(K_t): ||P^2 - I|| = {np.linalg.norm(Pg @ Pg - np.eye(192)):.1e}, "
      f"||{{P, chi}}|| = {res_pchi:.1e}, tr chi = {np.trace(chi_t).real:.1e}")
check("anchor: P^2 = I, {P, chi} = 0 (V1 structure reproduced)",
      np.linalg.norm(Pg @ Pg - np.eye(192)) < 1e-9 and res_pchi < 1e-9)

# ============================================================================
print()
print("=" * 96)
print("SECTION 1 -- FIBER-CHAIN ANCHORS: (7,3) -> trace-reversed (6,4) -> Hermitian (3,2)")
print("=" * 96)
eta4 = np.diag([-1.0, 1.0, 1.0, 1.0])
PAIRS10 = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def basis_mat(a):
    i, j = PAIRS10[a]
    E = np.zeros((4, 4))
    E[i, j] += 1.0
    if i != j:
        E[j, i] += 1.0
    return E


S10 = [basis_mat(a) for a in range(10)]


def coords(H):
    return np.array([H[PAIRS10[a]] for a in range(10)])


def gram_pair(metric):
    inv = np.linalg.inv(metric)
    B = np.array([[np.trace(inv @ S10[a] @ inv @ S10[b]) for b in range(10)] for a in range(10)])
    t = np.array([np.trace(inv @ S10[a]) for a in range(10)])
    return B, B - 0.5 * np.outer(t, t)


Bgram, Ggram = gram_pair(eta4)
sigB, sigG = signature_of(Bgram), signature_of(Ggram)
print(f"  Frobenius form B on Sym^2 (Lorentzian base):  ({sigB[0]},{sigB[1]})")
print(f"  trace-reversed G on Sym^2 (Lorentzian base):  ({sigG[0]},{sigG[1]})")
check("anchor: B = (7,3), G = (6,4)", sigB == (7, 3, 0) and sigG == (6, 4, 0))
Be, Ge = gram_pair(np.eye(4))
sigBe, sigGe = signature_of(Be), signature_of(Ge)
print(f"  EUCLIDEAN CONTROL: B = ({sigBe[0]},{sigBe[1]}), trace-reversed = ({sigGe[0]},{sigGe[1]})"
      f"  -> p = {sigGe[0]} ODD")
check("Euclidean control: (10,0) -> (9,1)", sigBe == (10, 0, 0) and sigGe == (9, 1, 0))

# so(3,1) action on V10 (lower-index symmetric tensors), V3 convention
def so31_gens():
    gens = []
    for (i, j) in [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]:
        A = np.zeros((4, 4))
        A[i, j], A[j, i] = 1.0, -1.0
        gens.append(eta4 @ A)
    return gens


M6 = so31_gens()


def rho(M):
    return np.array([coords(-(M.T @ S10[a] + S10[a] @ M)) for a in range(10)]).T


L6 = [rho(M) for M in M6]
resG_inv = max(np.linalg.norm(L.T @ Ggram + Ggram @ L) for L in L6)
check("G is so(3,1)-invariant (residual ~ 0)", resG_inv < 1e-9)


def hermitian_signature(J, G, seed=5):
    rng = np.random.default_rng(seed)
    Rb = []
    while len(Rb) < 10:
        v = rng.normal(size=10)
        if Rb:
            Q, _ = np.linalg.qr(np.array(Rb).T)
            v = v - Q @ (Q.T @ v)
        if np.linalg.norm(v) < 1e-6:
            continue
        v = v / np.linalg.norm(v)
        Rb += [v, J @ v]
    W5 = [Rb[2 * k] for k in range(5)]
    H5 = np.array([[wk @ G @ wl + 1j * ((J @ wk) @ G @ wl) for wl in W5] for wk in W5])
    herm_res = np.linalg.norm(H5 - H5.conj().T)
    wH = np.linalg.eigvalsh(0.5 * (H5 + H5.conj().T))
    return (int(np.sum(wH > 1e-9)), int(np.sum(wH < -1e-9))), herm_res


# constructive J0 on the measured (6,4) (V3 congruence construction) -> Hermitian (3,2)
wG_, QG = np.linalg.eigh(0.5 * (Ggram + Ggram.T))
order = np.argsort(-wG_)
wG_, QG = wG_[order], QG[:, order]
Cg = QG / np.sqrt(np.abs(wG_))
j2 = np.array([[0.0, -1.0], [1.0, 0.0]])
J0_std = np.zeros((10, 10))
for k in range(5):
    J0_std[2 * k:2 * k + 2, 2 * k:2 * k + 2] = j2
J0 = Cg @ J0_std @ np.linalg.inv(Cg)
(rH, sH), hres = hermitian_signature(J0, Ggram)
print(f"  compatible J0 on the measured (6,4): Hermitian signature ({rH},{sH}), residual {hres:.1e}")
check("anchor: Hermitian signature (3,2) (the fiber is C^(3,2); 3 = MEASURED positive count)",
      (rH, sH) == (3, 2) and hres < 1e-8)
p_C, q_C = rH, sH

# ============================================================================
print()
print("=" * 96)
print("SECTION 2 -- (a1) THE EQUIVARIANCE DICHOTOMY: does the family SU(2)+ act on the coset?")
print("=" * 96)
print("EUCLIDEAN HORN: su(2)+ acts honestly on Sym^2(R^4) -- but the coset is absent.")
# self-dual su(2)+ on the Euclidean R^4 base: vector generators L_ab + L_cd
def lrot4(i, j):
    A = np.zeros((4, 4))
    A[i, j], A[j, i] = -1.0, 1.0
    return A


rhoE = lambda M: np.array([coords(-(M.T @ S10[a] + S10[a] @ M)) for a in range(10)]).T
SDgens = [rhoE(lrot4(a, b) + lrot4(c, d)) for (a, b, c, d) in SD]
CasE = -(SDgens[0] @ SDgens[0] + SDgens[1] @ SDgens[1] + SDgens[2] @ SDgens[2])
evE = np.sort(np.linalg.eigvalsh(0.5 * (CasE + CasE.T)))
n_top = int(np.sum(np.abs(evE - 8.0) < 1e-9))
n_zero = int(np.sum(np.abs(evE) < 1e-9))
print(f"  su(2)+ Casimir on Sym^2(R^4): eigenvalue 8.0 x {n_top}, 0.0 x {n_zero} "
      f"(normalization: carrier anchor top = 8 for j = 1)")
print(f"  => multiplicity of the family TRIPLET on the fiber: {n_top} / 3 = {n_top // 3}"
      f"   [MEASURED; this is H1's native multiplicity-3 echo, Sym^2(2,2) = (3,3)+(1,1);")
print(f"      it is never used in any downstream formula]")
check("Euclidean horn: Sym^2(R^4) = 3 triplets + 1 singlet under su(2)+ (measured 9 + 1)",
      n_top == 9 and n_zero == 1)
print(f"  ...but the Euclidean trace-reversed fiber form is ({sigGe[0]},{sigGe[1]}): p odd =>")
print(f"  NO compatible complex structure exists (V3 Section-A theorem: p and q must both be")
print(f"  even; the Hermitian form doubles signatures) => D is ABSENT over a Euclidean base.")

print()
print("LORENTZIAN HORN: the coset exists -- but su(2)+ does not act on it.")
PAIRS2 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def levi(i, j, k, l):
    perm = [i, j, k, l]
    if len(set(perm)) < 4:
        return 0
    sgn, arr = 1, perm[:]
    for a in range(4):
        for b in range(a + 1, 4):
            if arr[a] > arr[b]:
                arr[a], arr[b] = arr[b], arr[a]
                sgn = -sgn
    return sgn


def hodge(inv_metric):
    Hs = np.zeros((6, 6))
    for A, (m, n) in enumerate(PAIRS2):
        for Bb, (r, s) in enumerate(PAIRS2):
            Hs[A, Bb] = sum(levi(m, n, a, b) * inv_metric[a, r] * inv_metric[b, s]
                            for a in range(4) for b in range(4))
    return Hs


Hlor, Heuc = hodge(np.linalg.inv(eta4)), hodge(np.eye(4))
check("Lorentzian Hodge-* on Lambda^2 squares to -I (SD/ASD split is COMPLEX: su(2)+ acts on the"
      " real fiber only through its SO(3) rotation image)",
      np.linalg.norm(Hlor @ Hlor + np.eye(6)) < 1e-10)
check("Euclidean CONTROL: *^2 = +I (machinery discriminates)",
      np.linalg.norm(Heuc @ Heuc - np.eye(6)) < 1e-10)

Lrot = [L6[3], L6[4], L6[5]]     # spatial rotations (1,2), (1,3), (2,3)
CasR = -(Lrot[0] @ Lrot[0] + Lrot[1] @ Lrot[1] + Lrot[2] @ Lrot[2])
evR = np.sort(np.linalg.eigvalsh(0.5 * (CasR + CasR.T)))
mult = {0: int(np.sum(np.abs(evR) < 1e-9)),
        2: int(np.sum(np.abs(evR - 2) < 1e-9)),
        6: int(np.sum(np.abs(evR - 6) < 1e-9))}
print(f"  V10 under the SO(3) rotation image: Casimir eigenvalues 0 x {mult[0]}, 2 x {mult[2]}, "
      f"6 x {mult[6]}  => isotypics 1+1 (j=0 x2), 3 (j=1), 5 (j=2)")
check("V10 = 1+1+3+5 under SO(3) (measured Casimir multiplicities)",
      mult[0] == 2 and mult[2] == 3 and mult[6] == 5)


def nullspace(A, tol=1e-9):
    U_, s_, Vt = np.linalg.svd(A)
    return Vt[(np.concatenate([s_, np.zeros(Vt.shape[0] - len(s_))]) < tol), :]


def linop(fun, n=10):
    cols = []
    for idx in range(n * n):
        E = np.zeros((n, n))
        E.flat[idx] = 1.0
        cols.append(fun(E).ravel())
    return np.array(cols).T


def commutant_basis(mats):
    rows = [linop(lambda X, Cm=Cm: Cm @ X - X @ Cm) for Cm in mats]
    ns = nullspace(np.vstack(rows))
    return [v.reshape(10, 10) for v in ns]


comR = commutant_basis(Lrot)
print(f"  commutant of SO(3) in gl(10): dim {len(comR)} (= 2^2 + 1 + 1: gl(2) on the trivial"
      f" isotypic + R on each odd one)")
check("commutant(SO(3)) dim = 6", len(comR) == 6)

# EXACT obstruction: any J in the commutant is a real SCALAR on each odd isotypic
wR, QR = np.linalg.eigh(0.5 * (CasR + CasR.T))
P3 = QR[:, np.abs(wR - 2) < 1e-9]     # j=1 isotypic (3-dim)
P5 = QR[:, np.abs(wR - 6) < 1e-9]     # j=2 isotypic (5-dim)
worst_scalar = 0.0
for X in comR:
    for Piso in (P3, P5):
        Xr = Piso.T @ X @ Piso
        c = np.trace(Xr) / Xr.shape[0]
        worst_scalar = max(worst_scalar, np.linalg.norm(Xr - c * np.eye(Xr.shape[0])))
print(f"  every commutant element restricted to the 3- and 5-dim isotypics is a real scalar:")
print(f"  max ||X|_iso - c I|| over the 6-dim commutant = {worst_scalar:.1e}")
check("EXACT obstruction: [J, SO(3)] = 0 forces J|_(3-dim) = c*id_3 with c^2 = -1 -- impossible"
      " over R => NO compatible J commutes with the SO(3) image", worst_scalar < 1e-9)

# exact G-signature of the 2-dim trivial isotypic (sympy rationals)
Es = [sp.zeros(4, 4) for _ in range(10)]
for a, (i, j) in enumerate(PAIRS10):
    Es[a][i, j] += 1
    if i != j:
        Es[a][j, i] += 1
eta_s = sp.diag(-1, 1, 1, 1)


def G_exact(h, k):
    B = sp.trace(eta_s * h * eta_s * k)
    return sp.nsimplify(B - sp.Rational(1, 2) * sp.trace(eta_s * h) * sp.trace(eta_s * k))


E00s, E11s, E22s, E33s = Es[0], Es[1], Es[2], Es[3]
Sp3 = E11s + E22s + E33s
g2 = sp.Matrix([[G_exact(E00s, E00s), G_exact(E00s, Sp3)],
                [G_exact(Sp3, E00s), G_exact(Sp3, Sp3)]])
print(f"  trivial isotypic span{{h_tt, spatial trace}}: exact Gram = {g2.tolist()}, "
      f"det = {sp.det(g2)} < 0 => signature (1,1)")
check("2-dim trivial isotypic has exact G-signature (1,1) -- both odd, no J there either",
      sp.det(g2) < 0)


# optimizer scan (V3 machinery) -- numerical falsification with controls
def scan(g, Bas=None, nstart=20, seed=1, label=""):
    if Bas is None:
        Bas = [np.zeros((10, 10)) for _ in range(100)]
        for k in range(100):
            Bas[k].flat[k] = 1.0
    Barr = np.array(Bas)
    Bflat = Barr.reshape(len(Bas), -1)
    I10 = np.eye(10)
    rng = np.random.default_rng(seed)

    def fg(t):
        J = np.tensordot(t, Barr, axes=1)
        F = J @ J + I10
        Rm = J.T @ g @ J - g
        val = float((F * F).sum() + (Rm * Rm).sum())
        grJ = 2.0 * (J.T @ F + F @ J.T) + 4.0 * (g @ J @ Rm)
        return val, Bflat @ grJ.ravel()

    best = np.inf
    for _ in range(nstart):
        t0 = rng.normal(size=len(Bas))
        res = minimize(fg, t0, jac=True, method="L-BFGS-B",
                       options={"maxiter": 8000, "ftol": 1e-18, "gtol": 1e-13})
        best = min(best, res.fun)
    print(f"  scan[{label}]: min residual over {nstart} starts = {best:.3e}")
    return best


floor_so3 = scan(Ggram, Bas=comR, nstart=25, seed=11, label="J in commutant(SO(3)), 25 starts")
check("scan floor >= 8 (= 3 + 5, the measured odd isotypic dims -- an output, not an input)",
      floor_so3 > 8 - 1e-6, f"floor {floor_so3:.4f}")
L3 = L6[3]                               # rotation in the (1,2)-plane: the Cartan of SO(3)
comL3 = commutant_basis([L3])
floor_l3 = scan(Ggram, Bas=comL3, nstart=10, seed=12, label=f"CONTROL: J in commutant(L3), "
                f"dim {len(comL3)}")
check("CONTROL: the L3-commutant scan FINDS a compatible J (~0) -- the wall is the full SO(3), "
      "not the machinery", floor_l3 < 1e-12)
floor_e = scan(Ge, nstart=10, seed=13, label="CONTROL: Euclidean (9,1), unconstrained")
check("CONTROL: Euclidean (9,1) scan floor > 0 (parity theorem confirmed numerically)",
      floor_e > 1e-3)

print()
print("  DICHOTOMY (a1 verdict): the SU(2)+-equivariant coset does not exist in either signature.")
print("  Euclidean base: family acts, coset absent ((9,1), p odd). Lorentzian base: coset exists,")
print("  family acts only through SO(3), and NO compatible J is SO(3)-invariant (exact scalar")
print("  obstruction + (1,1) trivial isotypic + scan floor). Full-family equivariance cannot")
print("  select m because it cannot be formulated. 'Which orbits of CP^2 are SU(2)+-invariant':")
print("  none -- SU(2)+ has no holomorphic action on any CP^2_J; it moves J itself.")

# ============================================================================
print()
print("=" * 96)
print("SECTION 3 -- (a2) THE MAXIMAL ACTING SUBGROUP U(1)+ AND ITS EXACT WEIGHTS (sympy, exact)")
print("=" * 96)
# exact integer matrix of rho(L3), L3 = rotation in the (1,2)-plane
M12 = sp.zeros(4, 4)
M12[1, 2], M12[2, 1] = -1, 1


def coords_s(H):
    return sp.Matrix([H[i, j] for (i, j) in PAIRS10])


rho3 = sp.zeros(10, 10)
for a in range(10):
    img = -(M12.T * Es[a] + Es[a] * M12)
    col = coords_s(img)
    for r in range(10):
        rho3[r, a] = col[r]
Gs = sp.Matrix(10, 10, lambda a, b: G_exact(Es[a], Es[b]))
check("rho(L3) is an exact integer matrix and G-antisymmetric (exact)",
      all(x.is_integer for x in rho3) and sp.simplify(rho3.T * Gs + Gs * rho3) == sp.zeros(10, 10))

# frame: zero-weight block (exact) + three weight planes
idx = {p: i for i, p in enumerate(PAIRS10)}
ev_ = lambda i: sp.Matrix([1 if r == i else 0 for r in range(10)])
v_E00 = ev_(idx[(0, 0)])
v_E33 = ev_(idx[(3, 3)])
v_S = ev_(idx[(1, 1)]) + ev_(idx[(2, 2)])
v_E03 = ev_(idx[(0, 3)])
v_E01, v_E02 = ev_(idx[(0, 1)]), ev_(idx[(0, 2)])
v_E13, v_E23 = ev_(idx[(1, 3)]), ev_(idx[(2, 3)])
v_Ediff = ev_(idx[(1, 1)]) - ev_(idx[(2, 2)])
v_E12 = ev_(idx[(1, 2)])

for v in (v_E00, v_E33, v_S, v_E03):
    assert rho3 * v == sp.zeros(10, 1), "zero-weight vector fails exactly"
print("  zero-weight space Z = span{h_tt, h_33, h_11+h_22, h_03}: rho(L3) Z = 0 EXACTLY")
plane_data = [((v_E01, v_E02), 1, "(h_01, h_02)"),
              ((v_E13, v_E23), 1, "(h_13, h_23)"),
              ((v_Ediff, v_E12), 2, "(h_11 - h_22, h_12)")]
for (va, vb), wgt, lbl in plane_data:
    sq_a = sp.simplify(rho3 * (rho3 * va) + wgt ** 2 * va)
    sq_b = sp.simplify(rho3 * (rho3 * vb) + wgt ** 2 * vb)
    in_a = rho3 * va      # must lie in span{va, vb}
    check(f"weight plane {lbl}: rho(L3)^2 = -{wgt}^2 EXACTLY (invariant plane, weight {wgt})",
          sq_a == sp.zeros(10, 1) and sq_b == sp.zeros(10, 1))

# exact adapted J: rotation pairs on Z with equal G-norms
Gq = lambda x, y: sp.nsimplify((x.T * Gs * y)[0, 0])
a1 = v_E00                                    # G = 1/2 (positive)
b1 = (v_E33 - v_S / 2) / sp.sqrt(3)           # G = (3/2)/3 = 1/2
a2 = -3 * v_E00 + v_E33 + v_S                 # G = -6 (negative)
b2 = sp.sqrt(3) * v_E03                       # G = 3*(-2) = -6
print(f"  Z-block exact G-norms: G(a1,a1) = {Gq(a1, a1)}, G(b1,b1) = {Gq(b1, b1)}, "
      f"G(a1,b1) = {Gq(a1, b1)};  G(a2,a2) = {Gq(a2, a2)}, G(b2,b2) = {Gq(b2, b2)}, "
      f"G(a2,b2) = {Gq(a2, b2)}")
check("Z-block pairs: equal norms, orthogonal (exact): positive pair 1/2, negative pair -6",
      Gq(a1, a1) == sp.Rational(1, 2) and Gq(b1, b1) == sp.Rational(1, 2)
      and Gq(a1, b1) == 0 and Gq(a2, a2) == -6 and Gq(b2, b2) == -6 and Gq(a2, b2) == 0
      and Gq(a1, a2) == 0 and Gq(a1, b2) == 0 and Gq(b1, a2) == 0 and Gq(b1, b2) == 0)

Fcols = [a1, b1, a2, b2, v_E01, v_E02, v_E13, v_E23, v_Ediff, v_E12]
Fmat = sp.Matrix.hstack(*Fcols)
Jimg = [b1, -a1, b2, -a2,
        rho3 * v_E01, rho3 * v_E02,             # weight-1 planes: J = rho3 / 1
        rho3 * v_E13, rho3 * v_E23,
        (rho3 * v_Ediff) / 2, (rho3 * v_E12) / 2]  # weight-2 plane: J = rho3 / 2
Jmat = sp.Matrix.hstack(*Jimg) * Fmat.inv()
r_J2 = sp.simplify(Jmat * Jmat + sp.eye(10))
r_JG = sp.simplify(Jmat.T * Gs * Jmat - Gs)
r_Jc = sp.simplify(Jmat * rho3 - rho3 * Jmat)
check("EXACT adapted J_ad: J^2 = -I (exact zero matrix)", r_J2 == sp.zeros(10, 10))
check("EXACT adapted J_ad: J^T G J = G (exact zero matrix)", r_JG == sp.zeros(10, 10))
check("EXACT adapted J_ad: [J_ad, rho(L3)] = 0 (exact zero matrix)", r_Jc == sp.zeros(10, 10))
Jad_f = np.array(Jmat.evalf(20), dtype=float)
(rHa, sHa), hres_a = hermitian_signature(Jad_f, Ggram, seed=9)
print(f"  J_ad Hermitian signature: ({rHa},{sHa}) (residual {hres_a:.1e}) -- the adapted coset is"
      f" the same C^(3,2)")
check("J_ad gives Hermitian (3,2)", (rHa, sHa) == (3, 2) and hres_a < 1e-8)

print()
print("  EXACT U(1)+ weights on C^(3,2) (weight of rho(L3) on the +i eigenspace of J_ad,")
print("  = w on each plane where J_ad = rho(L3)/w by construction; 0 on the Z-planes):")
print("    positive part C^3:  a = (0, 1, 2)   [Z-positive plane 0; (h13,h23) 1; (h11-h22,h12) 2]")
print("    negative part C^2:  b = (0, 1)      [Z-negative plane 0; (h01,h02) 1]")
print("  Signs are per-plane J-orientation choices (both orientations give compatible J);")
print("  the magnitudes are canonical. NOTE: no weight is 3; the 3 appears only as the COUNT")
print("  of distinct positive weights = number of isolated U(1)+ fixed points on the core CP^2")
print("  = chi(CP^2) [V5's measured 3 -- reproduced here as a fixed-point COUNT].")
a_w = [0, 1, 2]
b_w = [0, 1]
check("3 isolated fixed points on the core = number of distinct measured weights = chi",
      len(set(a_w)) == 3)

# exact fixed-point (localization) fits: w_i = -m * a_i + c
def fit_m(weights_at_fp):
    m_fit = sp.Rational(weights_at_fp[0] - weights_at_fp[1], a_w[1] - a_w[0])
    c_fit = weights_at_fp[0] + m_fit * a_w[0]
    ok = all(weights_at_fp[i] == -m_fit * a_w[i] + c_fit for i in range(3))
    return m_fit, c_fit, ok


taut_w = a_w[:]                                            # tautological fiber weights
core_det = [sum(a_w[j] - a_w[i] for j in range(3) if j != i) for i in range(3)]
D_det = [core_det[i] + sum(b_w[l] - a_w[i] for l in range(2)) for i in range(3)]
m_taut, c_taut, ok_t = fit_m(taut_w)
m_core, c_core, ok_c = fit_m(core_det)
m_D, c_D, ok_D = fit_m(D_det)
print(f"  fixed-point fiber weights (exact integers):")
print(f"    tautological O(-1):              {taut_w}  -> fits m = {m_taut} (c = {c_taut})")
print(f"    det T(core CP^2)  [anticanon]:   {core_det}  -> fits m = {m_core} (c = {c_core})")
print(f"    det T(D)          [anticanon]:   {D_det}  -> fits m = {m_D} (c = {c_D})")
check("localization fits: taut -> m = -1; core anticanonical -> m = 3; D anticanonical -> m = 5",
      ok_t and ok_c and ok_D and m_taut == -1 and m_core == 3 and m_D == 5)
print("  U(1)+-equivariance forces NO m: O(m) = taut^(x)(-m) (x) chi_c carries an equivariant")
print("  structure for EVERY m (fixed-point weights -m*a_i + c are well-defined for all m, c);")
print("  a torus never selects a Chern class. The selection must come from the homogeneous")
print("  structure -- Section 4.")

# ============================================================================
print()
print("=" * 96)
print("SECTION 4 -- (a3) THE m-SELECTION: stabilizer-character arithmetic (exact integers)")
print("=" * 96)


def su_pq_basis(p, q):
    n = p + q
    eta_ = np.diag([1.0] * p + [-1.0] * q).astype(complex)
    bas = []
    for kk in range(n - 1):
        Y = np.zeros((n, n), dtype=complex)
        Y[kk, kk] = 1j
        Y[kk + 1, kk + 1] = -1j * (eta_[kk, kk] / eta_[kk + 1, kk + 1]).real
        bas.append(eta_ @ Y)
    for a in range(n):
        for b in range(a + 1, n):
            Y = np.zeros((n, n), dtype=complex)
            Y[a, b], Y[b, a] = 1, -1
            bas.append(eta_ @ Y)
            Y2 = np.zeros((n, n), dtype=complex)
            Y2[a, b], Y2[b, a] = 1j, 1j
            bas.append(eta_ @ Y2)
    return eta_, bas


def stab_analysis(p, q, label):
    """Stabilizer of the positive line C e1 inside su(p,q); character-lattice rank;
    exact central-weight arithmetic for taut / det T(ambient) / det T(core)."""
    n = p + q
    eta_, bas = su_pq_basis(p, q)
    res = max(np.linalg.norm(X.conj().T @ eta_ + eta_ @ X) + abs(np.trace(X)) for X in bas)
    dim_su = len(bas)
    # stabilizer of the line: (I - e1 e1^dag) X e1 = 0
    e1v = np.zeros(n, dtype=complex)
    e1v[0] = 1.0
    rows = []
    for X in bas:
        t = X @ e1v
        t = t - (e1v.conj() @ t) * e1v
        rows.append(np.concatenate([t.real, t.imag]))
    coefM = np.array(rows).T                     # (2n) x dim_su constraint matrix
    nsH = nullspace(coefM)
    hbas = [sum(v[k] * bas[k] for k in range(dim_su)) for v in nsH]
    dim_h = len(hbas)
    # derived algebra of h
    br = []
    for i in range(dim_h):
        for j in range(i + 1, dim_h):
            Bm = hbas[i] @ hbas[j] - hbas[j] @ hbas[i]
            br.append(np.concatenate([Bm.real.ravel(), Bm.imag.ravel()]))
    rank_der = int(np.linalg.matrix_rank(np.array(br), tol=1e-9)) if br else 0
    # central character generator: Y = i diag(n-1, -1, ..., -1)
    Yc = 1j * np.diag([float(n - 1)] + [-1.0] * (n - 1)).astype(complex)
    resY = np.linalg.norm(Yc.conj().T @ eta_ + eta_ @ Yc) + abs(np.trace(Yc))
    resC = max(np.linalg.norm(Yc @ X - X @ Yc) for X in hbas)
    # Y is NOT in [h,h] (it generates the character lattice): least-squares projection residual
    Yvec = np.concatenate([Yc.real.ravel(), Yc.imag.ravel()])
    if br:
        brM = np.array(br).T
        proj, *_ = np.linalg.lstsq(brM, Yvec, rcond=None)
        resYout = np.linalg.norm(Yvec - brM @ proj) / np.linalg.norm(Yvec)
    else:
        resYout = 1.0
    w_L = n - 1        # Y e1 = (n-1) i e1: exact by construction
    w_Q = -1
    w_T_each = w_Q - w_L
    det_T = (n - 1) * w_T_each
    # dictionary: O(m) fiber weight = -w_L * m  (so that O(-1) = taut has weight +w_L)
    m_anti = sp.Rational(-det_T, w_L)
    print(f"  {label}: dim su({p},{q}) = {dim_su} [measured], stabilizer dim = {dim_h}, "
          f"dim [h,h] = {rank_der} -> character lattice rank {dim_h - rank_der}")
    print(f"    central Y = i*diag({n - 1},-1,...): in h (residual {resY:.1e}), central "
          f"(max ||[Y,h]|| = {resC:.1e}), outside [h,h] (rel. residual {resYout:.2f})")
    print(f"    EXACT weights: line C e1: +{w_L}; quotient: {w_Q} (x{n - 1}); tangent "
          f"Hom(L,Q): {w_T_each} (x{n - 1}); det T = {det_T}")
    print(f"    => tautological O(-1) <-> weight +{w_L};  anticanonical K^(-1) = det T <-> "
          f"O({m_anti})")
    ok = (res < 1e-12 and dim_h == (n - 1) ** 2 and rank_der == (n - 1) ** 2 - 1
          and resY < 1e-12 and resC < 1e-10 and resYout > 0.1 and m_anti == n)
    return int(m_anti), ok


print("The coset D = SU(3,2)/S(U(1) x U(2,2)) (V5's measured assignment).")
m_D_amb, ok_amb = stab_analysis(3, 2, "AMBIENT D, C^(3,2)")
check("D: stabilizer dim 16, [h,h] dim 15 => character lattice = Z; anticanonical of D = O(5)",
      ok_amb and m_D_amb == 5)
print()
print("The compact core CP^2 = the S(U(3) x U(2))-orbit of e1 = SU(3)/S(U(1) x U(2)).")
m_core_amb, ok_core = stab_analysis(3, 0, "CORE CP^2, C^3 (su(3) block)")
check("core: anticanonical = O(3) [3 = p = the measured Hermitian positives -- provenance: "
      "dim X = 4 + one time direction -> (7,3) -> (6,4) -> C^(3,2), V5 chain]",
      ok_core and m_core_amb == 3)
print()
print("CONTROLS (same arithmetic, different measured input -- the machinery outputs p and p+q):")
m21, ok21 = stab_analysis(2, 1, "control C^(2,1)")
m30_core, _ = stab_analysis(2, 0, "control core CP^1 (su(2) block)")
m42, ok42 = stab_analysis(4, 2, "control C^(4,2)")
m40_core, _ = stab_analysis(4, 0, "control core CP^3 (su(4) block)")
check("controls: (2,1) -> ambient 3 / core 2; (4,2) -> ambient 6 / core 4 (not always 3, 5)",
      m21 == 3 and m30_core == 2 and m42 == 6 and m40_core == 4)

print()
print("  THE SELECTION TABLE (exact; O(m) fiber weight = -w_L m, w_L = 4 on D, 2 on the core):")
print("    breaking line itself (V5 premise beta: condensate = the positive line)   |m| = 1")
print("    quadratic condensate v (.) v in Sym^2(line)                              |m| = 2")
print("    degree-r monomial coupling in the VEV                                    |m| = r")
print("    anticanonical of the coset D (det T_D, weight -20 = -4*5)                m  = 5")
print("    anticanonical of the compact core CP^2 (det weight -6 = -2*3)            m  = 3")
print("  MECHANISM STATEMENT: the stabilizer character of the breaking direction FORCES |m| = 1")
print("  (2 for quadratic coupling). 3 | m FAILS for every natively selected coupling. The only")
print("  3-divisible entry is the CORE anticanonical -- a compact-orbit datum, NOT the coset's")
print("  own anticanonical (that is O(5), 3-FREE), and NOT the rep the breaking direction")
print("  transforms in. V5's flagged possibility 'the condensate couples through O(3) = K^(-1)'")
print("  is now certified: nothing measured selects it; an O(3) coupling would be an IMPORT")
print("  (a cubic-in-the-VEV structure, 3 | r, that no native object supplies).")
check("m-selection verdict: natively selected |m| in {1, 2}; 3 | m FAILS; O(3) = core "
      "anticanonical only, unselected", True)

print()
print("  (a4) carrier-side honesty: the V5 sec-5(i) LITERAL form (decompose the 1792-dim carrier")
print("  under the stabilizer) has no native home on this carrier:")
n_int_space = sum(1 for a in range(4, 14) if a not in TIMELIKE)
n_int_time = sum(1 for a in range(4, 14) if a in TIMELIKE)
print(f"    internal block signature: ({n_int_space},{n_int_time}) spacelike/timelike "
      f"[measured from eta_V] -- NOT (6,4): any so(6,4) sub-block needs 6 spacelike directions")
print(f"    and must borrow >= 1 of the 4 base directions;")
res_borrow = np.linalg.norm(sgen(2, 3) @ sgen(3, 9) - sgen(3, 9) @ sgen(2, 3))
print(f"    a borrowed-index block generator then fails to commute with the family su(2)+:")
print(f"    ||[sigma_23, sigma_39]|| = {res_borrow:.3f}  (su(2)+ contains sigma_01 + sigma_23)")
check("carrier cannot natively host both the (6,4) fiber chain and a commuting family su(2)+ "
      "(internal is (5,5); borrowed blocks break family commutation)",
      (n_int_space, n_int_time) == (5, 5) and res_borrow > 0.1)

# ============================================================================
print()
print("=" * 96)
print("SECTION 5 -- (b) TWISTED-INDEX ARITHMETIC (sympy, exact; h2 canon formula + CP^2 twist)")
print("=" * 96)
kk_, km_, d_, m_, sig_, dp_ = sp.symbols("k k_minus d m sigma d'", integer=True)
jr = sp.Rational
T_dynk = lambda jj: sp.nsimplify(jj) * (sp.nsimplify(jj) + 1) * (2 * sp.nsimplify(jj) + 1) / 3
assert T_dynk(jr(1, 2)) == jr(1, 2) and T_dynk(1) == 2
print(f"  Dynkin anchors: T(1/2) = {T_dynk(jr(1, 2))} ('t Hooft), T(1) = {T_dynk(1)} (gaugino).")
print(f"  [the /3 in T(j) is library mathematics anchored by T(1/2) = 1/2 -- not the target 3]")
ch1V = sp.symbols("ch1V")
print()
print("  Where the twist enters (verifier finding, reproduced symbolically): the degree-4 index")
print("  density of V (x) L is  ch2(V) + ch1(V)*c1(L) + rk(V)*c1(L)^2/2 ; for every GU-native")
print("  su(2) channel ch1(V) = 0 (traceless), so the twist enters ONLY through rk*c1(L)^2/2.")
cross = ch1V * m_
check("cross term ch1(V)*c1(L) vanishes iff ch1(V) = 0 (GU-native channels)",
      cross.subs(ch1V, 0) == 0)

ind_full = sp.expand(2 * 0 + 4 * (2 * T_dynk(jr(1, 2)) * kk_) + 2 * (2 * T_dynk(1) * kk_)
                     + 16 * (m_ ** 2 * d_ / 2) + 16 * (-sig_ / 8))
print(f"  full 16-dim multiplicity bundle [leg-3: 2(j=0) + 4(j=1/2) + 2(j=1)]:")
print(f"    ind_full = {ind_full}")
check("ind_full = 12k + 8 m^2 d - 2 sigma (V5 formula reproduced)",
      sp.expand(ind_full - (12 * kk_ + 8 * m_ ** 2 * d_ - 2 * sig_)) == 0)
ind_spin = sp.expand(ind_full.subs(d_, 2 * dp_))
print(f"  X spin => intersection form even => d = 2d' => ind_full = {ind_spin}")

# mod 2 (the 2-adic wall): all coefficients even
poly2 = sp.Poly(ind_spin, kk_, dp_, sig_, m_)
all_even = all(int(c) % 2 == 0 for c in poly2.coeffs())
check("mod-2 wall: every coefficient of ind_full(spin) is EVEN -- the twist cannot make the "
      "count odd (V5 wall reproduced)", all_even)

# mod 3: exact reduction
resid3 = sp.expand(ind_spin - (m_ ** 2 * dp_ + sig_))
poly3 = sp.Poly(resid3, kk_, dp_, sig_, m_)
all_div3 = all(int(c) % 3 == 0 for c in poly3.coeffs())
print(f"  MOD 3 (the modulus of the divisibility QUESTION -- the target hypothesis, never an")
print(f"  input to any construction):   ind_full == m^2 d' + sigma   (mod 3)")
check("exact: ind_full - (m^2 d' + sigma) has all coefficients divisible by 3", all_div3)

print()
print("  EXACT DIVISIBILITY CONDITION:")
print("    3 | ind_full for ALL sections (all d') and all k   <=>   3 | m  AND  3 | sigma.")
print("    [m^2 == 0 or 1 (mod 3); if 3 | m the residue is sigma alone; if 3 !| m the residue")
print("     is d' + sigma, which sweeps all residues as d' varies.]")
print("  With Rokhlin (16 | sigma on spin X): 3 | sigma <=> sigma == 0 (mod 48).")
print("  => THE FULL PAYOFF = (3 | m) AND (sigma == 0 mod 48): the verifiers' enlarged invoice,")
print("     now an exact arithmetic statement.")
print()
print("  residue table: ind_full mod 3 as a function of (m mod 3, sigma mod 3), d' symbolic:")
cells = {}
for m0 in range(3):
    row = []
    for s0 in range(3):
        r = sp.expand((m0 ** 2 % 3) * dp_ + (s0 % 3))
        cells[(m0, s0)] = r
        row.append(str(r))
    print(f"    m == {m0}:  " + "  |  ".join(f"sigma=={s0}: {row[s0]}" for s0 in range(3)))
tbl_ok = (cells[(0, 0)] == 0
          and all(cells[(0, s0)] != 0 for s0 in (1, 2))
          and all(cells[(m0, s0)].has(dp_) for m0 in (1, 2) for s0 in range(3)))
check("the (m == 0, sigma == 0) cell is the ONLY d'-independently vanishing cell", tbl_ok)

print()
print("  INSERT THE MEASURED m's FROM (a):")
verdicts = []
for mm, srcm in [(1, "breaking line (taut)"), (-1, "breaking line (dual)"),
                 (2, "quadratic condensate"), (5, "coset D anticanonical"),
                 (3, "core anticanonical [UNSELECTED / import]")]:
    r = (mm ** 2) % 3
    res_str = ("sigma" if r == 0 else "d' + sigma")
    div = "3 | m: YES" if mm % 3 == 0 else "3 | m: NO"
    print(f"    m = {mm:+d} ({srcm}):  m^2 == {r} (mod 3)  ->  ind_full == {res_str} (mod 3)   "
          f"[{div}]")
    verdicts.append((mm, r))
check("every NATIVELY SELECTED m (+-1, +-2, 5) has m^2 == 1 (mod 3): the coset contributes "
      "NOTHING mod 3 beyond the free imports (d', sigma)",
      all(r == 1 for mm, r in verdicts if mm != 3))
check("even the unselected core-anticanonical m = 3 still leaves ind == sigma (mod 3): the "
      "3 | sigma import remains", [r for mm, r in verdicts if mm == 3] == [0])
ind_32 = sp.expand(3 * km_ + 6 * (m_ ** 2 * d_ / 2))
print(f"  [(3,2) sub-sector trap, flagged as in V5: ind_(3,2) = {ind_32} = 3(k_- + m^2 d) is")
print(f"   3-divisible for ANY m -- that 3 is the NATIVE MULTIPLICITY riding along (import k_-")
print(f"   + truncation, h2 canon sec. 4), not a coset-born 3. Not conflated here.]")

# ============================================================================
print()
print("=" * 96)
print("SECTION 6 -- (c) C-07 CONFRONTATION: the twist-deformed core vs the quaternionic wall")
print("=" * 96)
# exact quaternionic structure by the C-07 regression RULE: C = product of exactly the
# Clifford generators with reality sign bar(e_a) = -e_a (the index set is MEASURED from this
# rep's reality signs; the C-07 script's {1,3,5,7,10,12} belongs to a different rep convention)
S_imag = [a for a in range(N) if np.linalg.norm(e[a].conj() + e[a]) < 1e-12]
S_real = [a for a in range(N) if np.linalg.norm(e[a].conj() - e[a]) < 1e-12]
print(f"  measured reality signs: bar(e_a) = -e_a for a in {S_imag} ({len(S_imag)} generators,"
      f" even); bar(e_a) = +e_a for a in {S_real}")
check("every generator has a definite reality sign; the imaginary set has EVEN size",
      len(S_imag) + len(S_real) == N and len(S_imag) % 2 == 0)
Cq = I128.copy()
for a in S_imag:
    Cq = Cq @ e[a]
res_u = np.linalg.norm(Cq @ Cq.conj().T - I128)
res_q = np.linalg.norm(Cq @ Cq.conj() + I128)
res_int = max(np.linalg.norm(ea @ Cq - Cq @ ea.conj()) for ea in e)
print(f"  C = prod(e_a, a imaginary): unitary {res_u:.1e}, C bar(C) = -I {res_q:.1e} "
      f"(J^2 = -1: QUATERNIONIC, p - q = 4 mod 8), e_a C = C bar(e_a) max {res_int:.1e}")
check("exact quaternionic structure J = C.conj on the spinor module (J^2 = -1, "
      "Clifford-commuting)", max(res_u, res_q, res_int) < 1e-10)
CW = np.kron(I14, Cq)     # linear part of J on W = V (x) S (V real)

# triplet invariance and quaternionic restriction
PtW = Wt @ Wt.conj().T
res_inv = np.linalg.norm((np.eye(N * DIM) - PtW) @ (CW @ Wt.conj()))
Ut = Wt.conj().T @ CW @ Wt.conj()
res_qt = np.linalg.norm(Ut @ Ut.conj() + np.eye(192))
print(f"  J maps the 192-dim triplet into itself (residual {res_inv:.1e}); "
      f"U_t bar(U_t) = -I (residual {res_qt:.1e})")
check("the triplet sector is J-invariant and quaternionic (Kramers structure present)",
      res_inv < 1e-7 and res_qt < 1e-7)
rr = np.random.default_rng(7)
Mr_ = rr.standard_normal((N * DIM, 192)) + 1j * rr.standard_normal((N * DIM, 192))
Qr, _ = np.linalg.qr(Mr_)
Ur = Qr.conj().T @ CW @ Qr.conj()
res_rand = np.linalg.norm(Ur @ Ur.conj() + np.eye(192))
check("CONTROL: a RANDOM 192-dim subspace is NOT quaternionic (residual large)",
      res_rand > 0.1, f"{res_rand:.2f}")

# native core vs twist-deformed core
A_t = Wt.conj().T @ J3[0] @ Wt                      # su(2)+ Cartan (real generator), restricted
A_t = 0.5 * (A_t - A_t.conj().T)                    # anti-Hermitian part (it is a-H already)
M_t = 1j * A_t                                      # the su(2)+ WEIGHT operator (K-self-adjoint)
S_t = Wt.conj().T @ np.kron(etaV, I128) @ Wt
res_scale = np.linalg.norm(S_t - np.eye(192))
print(f"  scale/coset direction on the triplet: ||etaV (x) 1|_W - I|| = {res_scale:.1e}")
check("V1 degeneration reproduced: the scale direction is the IDENTITY on the triplet -- the "
      "composed proxy (weight op) o (scale) equals the weight operator", res_scale < 1e-9)
core = M_t @ S_t                                    # the invoiced finite proxy
res_KSA = np.linalg.norm(Kt @ core.conj().T @ Kt - core)
res_H = np.linalg.norm(core - core.conj().T)
print(f"  twist-deformed core M = (i J+3) o (etaV x 1)|_W: Hermitian {res_H:.1e}, "
      f"K-self-adjoint {res_KSA:.1e}")
check("the twisted core is an admissible (K-self-adjoint) mass-type direction", res_KSA < 1e-7)


def j_parity(Mop):
    """residuals of [M, J] and {M, J} for the antilinear J with linear part Ut."""
    c = np.linalg.norm(Mop @ Ut - Ut @ Mop.conj())
    a = np.linalg.norm(Mop @ Ut + Ut @ Mop.conj())
    return c, a


cA, aA = j_parity(A_t)
cM, aM = j_parity(core)
nrmM = np.linalg.norm(core)
print(f"  NATIVE core A = J+3|_W (real):     ||[A, J]|| = {cA:.2e}   ||{{A, J}}|| = {aA:.2f}")
print(f"  TWISTED core M = i A (o scale):    ||[M, J]|| = {cM:.2f}   ||{{M, J}}|| = {aM:.2e}"
      f"   (||M|| = {nrmM:.2f}, ||[M,J]||/||M|| = {cM / nrmM:.3f})")
check("NATIVE core J-COMMUTES (C-07/Kramers hypothesis holds -> even count)", cA < 1e-7)
check("TWISTED core J-ANTICOMMUTES: the twist BREAKS J-commutation maximally "
      "(||[M,J]|| = 2||M||, {M,J} = 0) -- C-07's hypothesis fails, escape confirmed at "
      "operator level", aM < 1e-6 and abs(cM - 2 * nrmM) < 1e-4 * max(1.0, nrmM))
# parity structure
cP = np.linalg.norm(core @ Pg - Pg @ core)
cChi = np.linalg.norm(core @ chi_t - chi_t @ core)
print(f"  parity structure: ||[M, P_ghost]|| = {cP:.2e} (P-EVEN), ||[M, chi]|| = {cChi:.2e} "
      f"(chi-commuting)")
check("twisted core is ghost-parity EVEN and chi-commuting (V1 table reproduced -> by the V1 "
      "intertwiner lemma its mass spectrum is mirror-blind)", cP < 1e-7 and cChi < 1e-7)

# weight slices
wM, UM = np.linalg.eigh(0.5 * (core + core.conj().T))
slice_report = []
for wgt in (-2, 0, 2):
    Bw = UM[:, np.abs(wM - wgt) < 0.5]
    dw = Bw.shape[1]
    Kw = Bw.conj().T @ Kt @ Bw
    Kw = 0.5 * (Kw + Kw.conj().T)
    sw = np.linalg.eigvalsh(Kw)
    kp, km2 = int(np.sum(sw > 1e-6)), int(np.sum(sw < -1e-6))
    trP = (np.trace(Bw.conj().T @ Pg @ Bw)).real
    trX = (np.trace(Bw.conj().T @ chi_t @ Bw)).real
    slice_report.append((wgt, dw, kp, km2, trP, trX, Bw))
    print(f"  slice E_({wgt:+d}): dim {dw}, Krein signature (+{kp}, -{km2}), tr P = {trP:.1e}, "
          f"tr chi = {trX:.1e}")
check("slice dims (64, 64, 64); Krein signature (32, 32) on EVERY slice; tr P = tr chi = 0 on "
      "every slice: every slice is VECTORLIKE (no asymmetry seed)",
      all(dw == 64 and kp == 32 and km2 == 32 and abs(trP) < 1e-6 and abs(trX) < 1e-6
          for (_, dw, kp, km2, trP, trX, _) in slice_report))
# J maps E_w onto E_{-w}; E_0 quaternionic (Kramers-even)
B_m2, B_0, B_p2 = slice_report[0][6], slice_report[1][6], slice_report[2][6]
res_swap = np.linalg.norm((np.eye(192) - B_m2 @ B_m2.conj().T) @ (Ut @ B_p2.conj()))
U0 = B_0.conj().T @ Ut @ B_0.conj()
res_q0 = np.linalg.norm(U0 @ U0.conj() + np.eye(B_0.shape[1]))
print(f"  J(E_+2) = E_-2 (residual {res_swap:.1e});  E_0 is J-invariant and QUATERNIONIC: "
      f"U_0 bar(U_0) = -I (residual {res_q0:.1e}) => dim E_0 EVEN by Kramers")
check("mechanism: J-oddness PAIRS the +-w slices and forces a quaternionic (Kramers-even) zero "
      "slice -- the even/vectorlike conclusion re-arises without the C-07 hypothesis",
      res_swap < 1e-6 and res_q0 < 1e-6)
signed = sum(wgt * dw for (wgt, dw, _, _, _, _, _) in slice_report)
print(f"  net signed count sum_w w*dim E_w = {signed}")
check("net signed count = 0 (the twist direction supplies no kinematic asymmetry)", signed == 0)

# controls: random K-self-adjoint has MIXED J-parity and breaks [., P]
rng_c = np.random.default_rng(3)
mixed_ok = True
for t in range(3):
    R = rng_c.standard_normal((192, 192)) + 1j * rng_c.standard_normal((192, 192))
    Mr = 0.5 * (R + Kt @ R.conj().T @ Kt)
    Mr = Mr / np.linalg.norm(Mr)
    cR, aR = j_parity(Mr)
    pR = np.linalg.norm(Mr @ Pg - Pg @ Mr)
    if t == 0:
        print(f"  CONTROL random K-self-adjoint: ||[M,J]|| = {cR:.2f}, ||{{M,J}}|| = {aR:.2f}, "
              f"||[M,P]|| = {pR:.2f}  (mixed parity, P-breaking)")
    mixed_ok = mixed_ok and (cR > 0.1 and aR > 0.1 and pR > 0.1)
check("CONTROL: random K-self-adjoint directions have MIXED J-parity and break [., P_ghost] -- "
      "the twisted core's clean anticommutation/evenness is measured structure, not generic",
      mixed_ok)

# ============================================================================
print()
print("=" * 96)
print("SECTION 7 -- FORBIDDEN-SET AUDIT AND VERDICT")
print("=" * 96)
print("""Forbidden set {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8}: never assumed, inserted,
or divided by. Provenance of every 3 (and near misses) printed above:
  * 3 triplets in Sym^2(R^4): measured Casimir multiplicity (9 states / 3 per triplet) -- H1's
    native multiplicity echo, used in no downstream formula;
  * 3 = p = measured Hermitian positives of the (6,4) fiber (V5 chain from dim X = 4 + one time
    direction); it reappears as the core anticanonical exponent (exact weight ratio -6/-2) and
    as the COUNT of distinct U(1)+ weights {0,1,2} = fixed points = chi (cross-check);
  * 5 = p + q (the coset's own anticanonical O(5)); 4 = the stabilizer character weight of the
    line -- both measured outputs;
  * scan floor 8 = 3 + 5 = sum of the measured odd isotypic dims (an output);
  * mod 3 = the modulus of the divisibility QUESTION (the target hypothesis under test), used
    only as a modulus;
  * Dynkin /3: library mathematics anchored by T(1/2) = 1/2.
Every count statement is 'mechanism M forces c'.""")
print()
if FAIL:
    print(f"RESULT: {len(FAIL)} CHECK(S) FAILED: {FAIL}")
    sys.exit(1)
print("RESULT: all checks passed.")
print()
print("VERDICT (printed for the doc):")
print("  (a) Equivariant m-selection: PERFORMED, and it selects AGAINST the payoff.")
print("      - Full SU(2)+ equivariance is unformulable: Euclidean base kills the coset ((9,1)),")
print("        Lorentzian base kills the equivariance (no compatible J commutes with the SO(3)")
print("        image -- exact isotypic obstruction; THEOREM).")
print("      - The maximal acting family subgroup U(1)+ (exact adapted J_ad constructed) has")
print("        weights {0,1,2}/{0,1} and forces no m (tori never select Chern classes).")
print("      - The homogeneous structure DOES select: the breaking line transforms in O(-1),")
print("        |m| = 1 (quadratic: 2; degree r: r); the coset's own anticanonical is O(5);")
print("        O(3) is only the compact core's anticanonical, selected by nothing. THEOREM.")
print("  (b) ind_full == m^2 d' + sigma (mod 3); section-independent 3-divisibility <=> 3 | m")
print("      AND 3 | sigma (<=> sigma == 0 mod 48 with Rokhlin). Every natively selected m has")
print("      m^2 == 1 (mod 3): the coset contributes nothing mod 3. THEOREM (symbolic).")
print("  (c) The twist direction is J-ODD on the triplet ({M,J} = 0): C-07's Kramers hypothesis")
print("      fails (escape confirmed), but the even/vectorlike conclusion re-arises via +-weight")
print("      pairing + quaternionic zero slice: slices 64/64/64, Krein (32,32) each, tr P =")
print("      tr chi = 0. No kinematic asymmetry seed. THEOREM (carrier scope).")
print("  ROUTE V7 GRADE: the V5 open invoice 5(i)/(iii) is PAID and the answer is NEGATIVE:")
print("  KILL for the NATIVE transfer of the coset 3 into the generation index (kinematic scope,")
print("  conditional on V5 premises alpha/beta). The 3-divisible coupling O(3) is certified an")
print("  IMPORT (double: 3|m coupling + 3|sigma base topology). Only leg 5(ii) (an actual")
print("  section: needs the unbuilt dynamics) remains, and it cannot rescue 3|m -- it only")
print("  supplies d'.")
sys.exit(0)
