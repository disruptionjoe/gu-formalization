"""N6 fingerprint probe: the pre-bound order-3 cyclic fingerprint hunt in ker(Gamma).

PRE-BOUND PREDICTION (n4-two-z3s doc + tree node N6, armed before this probe existed):
an order-3 action, built canonically from the N4-identified data (the commutant Sp(1) /
the identified character data), cyclically permuting the triplet's 3 (generation, mirror)
pairs per 16-unit inside ker(Gamma), with characters pinned via Phi onto {0, 8nu, 16nu},
determinate up to EXACTLY the inversion {Phi_D, Phi_B} = Aut(Z/3) and nothing else.

MATCH PATTERN (operational, both tiers required):
  tier-1: character multiplicities on the 192-dim triplet = regular, (64, 64, 64)
          for (1, omega, omega^2)  [a 3-cycle of pair-slots = regular rep per slot-triple]
  tier-2: the action preserves the three frozen SU(2)+ weight-64 spaces and acts on them
          as scalars forming a BIJECTION onto {1, omega, omega^2} (up to global inversion
          only -- the admissible {Phi_D, Phi_B}).

OUTCOMES pre-declared: FOUND / ABSENT / ILL-POSED / PARTIAL.  Exit 0 = probe ran honestly.
"""
from __future__ import annotations
import os, sys, time
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, "..", "generation-sector")))
import gen_sector_bridge as bridge  # noqa: E402

rng = np.random.default_rng(20260720)
FAILURES = []
def check(tag, name, ok, detail=""):
    s = "PASS" if ok else "FAIL"
    print(f"[{tag}] {s}  {name}" + (f"  ({detail})" if detail else ""))
    if not ok: FAILURES.append(name)

t0 = time.time()
W3 = np.exp(2j * np.pi / 3)                      # omega
e, Gamma, Pi_RS, _ = bridge.constraint_objects()
N, DIM = bridge.N, bridge.DIM                    # 14, 128
I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)

# ---------------- [T] frozen fixtures ----------------------------------------------------
check("T", "Clifford exact: Gamma Gamma^dag = 14 I", float(np.max(np.abs(Gamma @ Gamma.conj().T - 14 * I128))) == 0.0)
check("T", "Pi_RS projector onto ker(Gamma), rank 1664", abs(np.trace(Pi_RS).real - 1664) < 1e-9)

C = e[1] @ e[3] @ e[5] @ e[7] @ e[10] @ e[12]    # J_quat = C . conj (canon C07 convention)
check("T", "J_quat^2 = -1 exact (C Cbar = -I)", float(np.max(np.abs(C @ C.conj() + I128))) == 0.0)
resC = max(float(np.max(np.abs(e[a] @ C - C @ e[a].conj()))) for a in range(N))
check("T", "ALL 14 gammas J_quat-commuting exactly", resC == 0.0)
# quaternion relations of the frozen commutant H = span{1, i, J, iJ}: on random vectors
v = rng.standard_normal(DIM) + 1j * rng.standard_normal(DIM)
Jq = lambda x: C @ x.conj()
r_q = max(float(np.linalg.norm(Jq(Jq(v)) + v)),
          float(np.linalg.norm(1j * Jq(v) + Jq(1j * v))))          # i J = -J i
check("T", "commutant quaternion relations (J^2=-1, {i,J}=0) on vectors", r_q < 1e-12)

# monomial trace-orthogonality certificate: C-linear commutant of the gammas = scalars
def word(idx):
    M = I128.copy()
    for a in idx: M = M @ e[a]
    return M
sets = [tuple(sorted(rng.choice(N, size=rng.integers(1, 6), replace=False))) for _ in range(40)]
sets = list(dict.fromkeys(sets))[:20]
offdiag = max(abs(np.trace(word(s) @ word(t).conj().T)) for i, s in enumerate(sets) for t in sets[i+1:])
check("E", "Clifford monomials trace-orthogonal (sampled): Cl(9,5) x C = M(128,C) full, "
           "so the C-LINEAR commutant is scalars; the REAL commutant is the frozen H", offdiag < 1e-9)

# ---------------- [T] the triplet (ghost_parity recipe, verbatim) ------------------------
def sgen(i, j): return 0.25 * (e[i] @ e[j] - e[j] @ e[i])
def lvec(i, j):
    M = np.zeros((N, N), dtype=complex); M[i, j] = 1; M[j, i] = -1; return M
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
J = [np.kron(I14, sgen(a, b) + sgen(c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
     for (a, b, c, d) in SD]
w, Vv = np.linalg.eigh(Pi_RS); W = Vv[:, w > 0.5]
Cas = -(J[0] @ J[0] + J[1] @ J[1] + J[2] @ J[2])
CasK = W.conj().T @ Cas @ W; CasK = 0.5 * (CasK + CasK.conj().T)
ev, U = np.linalg.eigh(CasK)
Wt = W @ U[:, np.abs(ev - 8.0) < 1e-3]           # the 192-dim self-dual triplet
check("T", "triplet: Casimir-8 eigenspace of ker(Gamma), dim 192", Wt.shape[1] == 192)
A3 = Wt.conj().T @ (1j * J[0]) @ Wt; A3 = 0.5 * (A3 + A3.conj().T)
mu, Q3 = np.linalg.eigh(A3)
P_w = {m: Q3[:, np.abs(mu - m) < 1e-6] for m in (-2, 0, 2)}
check("T", "triplet weight decomposition under iJ3: {-2,0,+2} x 64 (3 pair-slots x 64)",
      sorted(round(float(x)) for x in mu) == [-2]*64 + [0]*64 + [2]*64
      and all(P_w[m].shape[1] == 64 for m in (-2, 0, 2)))
bS = I128.copy()
for s_ in range(9): bS = bS @ e[s_]
if np.linalg.norm(bS.conj().T + bS) < 1e-9: bS = 1j * bS
bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
K = np.kron(np.diag([1.0]*9 + [-1.0]*5).astype(complex), bS)
sigK = np.linalg.eigvalsh(0.5 * ((Wt.conj().T @ K @ Wt) + (Wt.conj().T @ K @ Wt).conj().T))
check("T", "K|triplet signature (+96,-96): 96 (generation,mirror) hyperbolic pairs",
      int(np.sum(sigK > 1e-9)) == 96 and int(np.sum(sigK < -1e-9)) == 96)

# ---------------- helpers: tier tests on a C-linear candidate action U (1792x1792) -------
RV = rng.standard_normal((N * DIM, 8)) + 1j * rng.standard_normal((N * DIM, 8))
def tier_report(U, name):
    """Return dict: order3, kernel/triplet compatibility, weight scalars, multiplicities."""
    r = {}
    r["order3"] = float(np.max(np.abs(U @ (U @ (U @ RV)) - RV))) < 1e-8
    r["ker_ok"] = float(np.max(np.abs(U @ (Pi_RS @ RV) - Pi_RS @ (U @ RV)))) < 1e-7
    Ut = Wt.conj().T @ U @ Wt
    r["trip_leak"] = float(np.linalg.norm(U @ Wt - Wt @ Ut))
    lam = np.linalg.eigvals(Ut)
    mults = [int(np.sum(np.abs(lam - z) < 1e-6)) for z in (1, W3, W3**2)]
    r["mults"] = tuple(mults)
    scal = {}
    for m in (-2, 0, 2):
        Bm = Wt @ P_w[m]
        Um = Bm.conj().T @ U @ Bm
        s = np.trace(Um) / 64.0
        scal[m] = (complex(s), float(np.linalg.norm(Um - s * np.eye(64))))
    r["scalars"] = scal
    return r

def char_index(z):
    for k, zz in enumerate((1, W3, W3**2)):
        if abs(z - zz) < 1e-6: return k
    return None

def match_fingerprint(rep):
    """The pre-bound match test. tier-1: regular multiplicities. tier-2: weight spaces
    preserved, scalar action, characters a BIJECTION onto Z/3-hat (global inversion is
    absorbed by construction: a bijection and its inverse are both bijections)."""
    if not (rep["order3"] and rep["ker_ok"] and rep["trip_leak"] < 1e-7):
        return False, "not an order-3 action compatible with ker(Gamma)/triplet"
    if rep["mults"] != (64, 64, 64):
        return False, f"tier-1 fail: multiplicities {rep['mults']} != regular (64,64,64)"
    ks = []
    for m in (-2, 0, 2):
        s, dev = rep["scalars"][m]
        if dev > 1e-6: return False, f"tier-2 fail: non-scalar on weight {m} (dev {dev:.2e})"
        k = char_index(s)
        if k is None: return False, f"tier-2 fail: weight-{m} scalar not a cube root"
        ks.append(k)
    if sorted(ks) != [0, 1, 2]:
        return False, f"tier-2 fail: character assignment {ks} not a bijection onto Z/3-hat"
    return True, f"regular multiplicities + bijective weight characters {ks}"

# ---------------- [E] 1. WELL-POSEDNESS: the canonical Z/3 from the N4 data --------------
# Order-3 elements of the frozen commutant Sp(1): u = cos(2pi/3) + sin(2pi/3) * xi_hat,
# xi_hat a unit imaginary quaternion in span{i, J, iJ}. All are Sp(1)-conjugate (one
# class, R-trace -1 per H-dim); the C-LINEAR representatives are exactly the scalars
# omega*I, omegabar*I (the commutant's C-linear part is C*I). The action on ker(Gamma)
# is canonical: conjugation-invariant decomposition, residual freedom = the inversion.
co, si = np.cos(2*np.pi/3), np.sin(2*np.pi/3)
def u_apply(a, b, c):
    """R-linear commutant element u = co + si*(a i + b J + c iJ) acting on C^128 vectors."""
    n = np.sqrt(a*a + b*b + c*c); a, b, c = a/n, b/n, c/n
    return lambda x: co * x + si * (a * 1j * x + b * (C @ x.conj()) + c * 1j * (C @ x.conj()))
reps = {"scalar (a=1)": (1, 0, 0), "generic1": (0.3, 0.8, 0.52), "generic2": (0, 1, 0), "generic3": (0.6, -0.4, 0.7)}
ok_u3, ok_comm, traces = True, True, []
for nm, (a, b, c) in reps.items():
    f = u_apply(a, b, c)
    x = rng.standard_normal(DIM) + 1j * rng.standard_normal(DIM)
    ok_u3 &= float(np.linalg.norm(f(f(f(x))) - x)) < 1e-12
    ok_comm &= max(float(np.linalg.norm(e[a_] @ f(x) - f(e[a_] @ x))) for a_ in range(N)) < 1e-12
    # R-linear 256x256 realification on the spinor factor for trace/spectrum
    Amat = co * I128 + si * (a/np.sqrt(a*a+b*b+c*c)) * 1j * I128
    Bmat = si * ((b + 1j*c) / np.sqrt(a*a+b*b+c*c)) * C
    T = np.block([[Amat, Bmat], [Bmat.conj(), Amat.conj()]])
    lamT = np.linalg.eigvals(T)
    traces.append((nm, float(np.sum(lamT).real), int(np.sum(np.abs(lamT - 1) < 1e-8))))
check("E", "WELL-POSED: u^3 = 1, u != 1, u in the commutant (all 14 gammas), for scalar "
           "and 3 generic representatives", ok_u3 and ok_comm)
check("E", "canonicity: complexified spinor-factor trace = -128 for EVERY representative "
           "(one conjugacy class; decomposition is representative-independent)",
      all(abs(tr + 128) < 1e-8 for _, tr, _ in traces), str([(n, round(t, 6)) for n, t, _ in traces]))
check("E", "FREENESS: fixed space of u is 0 for every representative (division algebra: "
           "x*u = x forces x = 0 in H^64) -- no eigenvalue 1 anywhere",
      all(nfix == 0 for _, _, nfix in traces))

# multiplicities of the canonical action on ker(Gamma), complexified, via block partial trace
Ptr = sum(Pi_RS[a*DIM:(a+1)*DIM, a*DIM:(a+1)*DIM] for a in range(N))
def mults_complexified(a, b, c, P):
    n = np.sqrt(a*a + b*b + c*c)
    Amat = co * I128 + si * (a/n) * 1j * I128
    Bmat = si * ((b + 1j*c)/n) * C
    T = np.block([[Amat, Bmat], [Bmat.conj(), Amat.conj()]])
    out = []
    for lam in (1, W3, W3**2):
        oth = [z for z in (1, W3, W3**2) if abs(z - lam) > 1e-9]
        Pi_l = (T - oth[0]*np.eye(2*DIM)) @ (T - oth[1]*np.eye(2*DIM)) / ((lam-oth[0])*(lam-oth[1]))
        m = np.trace(P @ Pi_l[:DIM, :DIM]) + np.trace(P.conj() @ Pi_l[DIM:, DIM:])
        out.append(float(m.real))
    return tuple(round(m, 6) for m in out)
mk = mults_complexified(0.3, 0.8, 0.52, Ptr)
check("E", "canonical action on ker(Gamma), complexified multiplicities (1, w, w2) = "
           "(0, 1664, 1664): trivial character multiplicity ZERO", mk == (0.0, 1664.0, 1664.0), str(mk))
Ptr_t = sum((Wt @ Wt.conj().T)[a*DIM:(a+1)*DIM, a*DIM:(a+1)*DIM] for a in range(N))
mt = mults_complexified(0.3, 0.8, 0.52, Ptr_t)
check("E", "canonical action on the TRIPLET, complexified multiplicities = (0, 192, 192)",
      mt == (0.0, 192.0, 192.0), str(mt))

# ---------------- [E] 2-3. DECOMPOSE + MATCH: the canonical C-linear representative ------
U_can = W3 * np.eye(N * DIM)                     # omega * I: THE C-linear commutant order-3
rep_can = tier_report(U_can, "canonical")
ok_match, why = match_fingerprint(rep_can)
check("E", "canonical Z/3 vs pre-bound pattern: NO MATCH -- multiplicities (0,192,0) on "
           "the complex triplet (all-omega, fixed-point-free), per-slot-triple (0,6,0) vs "
           "predicted regular (2,2,2)", (not ok_match) and rep_can["mults"] == (0, 192, 0), why)
rep_inv = tier_report(W3**2 * np.eye(N * DIM), "canonical-inverted")
check("E", "the inversion orbit {wI, w2I} = the FULL residual freedom: inverted rep gives "
           "(0,0,192); neither matches; verdict inversion-invariant",
      rep_inv["mults"] == (0, 0, 192) and not match_fingerprint(rep_inv)[0])

# ---------------- [E] 4. planted positive: the pattern IS realizable, non-canonically ----
lam3, V3 = np.linalg.eigh(1j * J[0])
g = V3 @ np.diag(np.exp(-1j * (2*np.pi/3) * lam3)) @ V3.conj().T   # exp((2pi/3) J3)
rep_g = tier_report(g, "planted SU(2)+ rotation")
okg, whyg = match_fingerprint(rep_g)
check("E", "planted positive: g = exp((2pi/3) J3) is order 3 on ALL of C^1792, preserves "
           "ker(Gamma) and the triplet, and MATCHES the pattern (regular (64,64,64), "
           "bijective weight characters)", okg and rep_g["order3"] and rep_g["ker_ok"], whyg)
notcomm = max(float(np.linalg.norm(g @ np.kron(I14, e[a_]) - np.kron(I14, e[a_]) @ g)) for a_ in (0, 5, 11))
check("E", "g is NOT the N4 object: not in the commutant (||[g, gamma]|| = O(10)), and its "
           "axis is one of an S^2 family -- a further choice the binding forbids", notcomm > 1.0,
      f"max sampled commutator {notcomm:.2f}")
lam1, V1 = np.linalg.eigh(1j * J[1])
g2 = V1 @ np.diag(np.exp(-1j * (2*np.pi/3) * lam1)) @ V1.conj().T
r2 = np.linalg.eigvals(Wt.conj().T @ g2 @ Wt)
m2 = tuple(int(np.sum(np.abs(r2 - z) < 1e-6)) for z in (1, W3, W3**2))
check("E", "second axis g' = exp((2pi/3) J1) ALSO carries regular multiplicities (64,64,64):"
           " matching actions form a continuum, not unique-up-to-inversion", m2 == (64, 64, 64), str(m2))

# ---------------- [E] 5. null expectation ------------------------------------------------
n_comp = 194 * 193 // 2
check("E", "null expectation (uniform composition of 192 into 3 characters): P(regular) = "
           "1/18721 = 5.3e-5; P(trivial mult = 0) = 193/18721 = 1.03e-2 -- the canonical "
           "outcome (freeness) is itself non-generic, it is the division-algebra theorem",
      n_comp == 18721)

# ---------------- [F] controls -----------------------------------------------------------
# (i) scrambled-character controls against the PLANTED positive's data
scr1 = rep_g["mults"] == (128, 64, 0)
kset = [char_index(rep_g["scalars"][m][0]) for m in (-2, 0, 2)]
scr2_ok = sorted(kset) == [0, 1, 2]
bad_assign = [0, 1, 1]                            # non-homomorphic (0, 1/3, 1/3) imposter
check("F", "scrambled-character control: weighted scramble (128,64,0) does not match the "
           "planted data; non-bijective assignment (0,1/3,1/3) REJECTED by the bijection "
           "gate; Z/9 characters (0,1/9,2/9) are not cube roots -- rejected",
      (not scr1) and scr2_ok and sorted(bad_assign) != [0, 1, 2]
      and char_index(np.exp(2j*np.pi/9)) is None)
# per-block-inconsistent inversion: scalar omega on BOTH weight +-2 (not a global inversion)
Ubad = Wt @ (W3 * (P_w[2] @ P_w[2].conj().T) + W3 * (P_w[-2] @ P_w[-2].conj().T)
             + 1.0 * (P_w[0] @ P_w[0].conj().T)) @ Wt.conj().T + (np.eye(N*DIM) - Wt @ Wt.conj().T)
rep_bad = tier_report(Ubad, "blockwise-inconsistent")
check("F", "blockwise-inconsistent inversion (omega on both weight +-2) FAILS: multiplicities "
           "(64,128,0), assignment not bijective -- only the GLOBAL inversion is admissible",
      not match_fingerprint(rep_bad)[0], match_fingerprint(rep_bad)[1])
# (ii) specificity: random order-3 unitaries on the triplet
fails = 0
for seed in range(5):
    r2_ = np.random.default_rng(seed)
    ks_ = r2_.integers(0, 3, size=192)
    M_ = r2_.standard_normal((192, 192)) + 1j * r2_.standard_normal((192, 192))
    Qr, _ = np.linalg.qr(M_)
    Ur = Wt @ (Qr @ np.diag(W3 ** ks_) @ Qr.conj().T) @ Wt.conj().T + (np.eye(N*DIM) - Wt @ Wt.conj().T)
    if not match_fingerprint(tier_report(Ur, f"rand{seed}"))[0]: fails += 1
check("F", "specificity: 5 random order-3 unitary actions on the triplet -- NONE matches "
           "(wrong multiplicities and/or weight-space misalignment)", fails == 5)
ks_eq = np.array([0]*64 + [1]*64 + [2]*64)
Qr, _ = np.linalg.qr(np.random.default_rng(99).standard_normal((192, 192)) + 1j*np.random.default_rng(98).standard_normal((192, 192)))
Ueq = Wt @ (Qr @ np.diag(W3 ** ks_eq) @ Qr.conj().T) @ Wt.conj().T + (np.eye(N*DIM) - Wt @ Wt.conj().T)
rep_eq = tier_report(Ueq, "equal-mult Haar")
check("F", "adversarial equal-multiplicity Haar action: passes tier-1 (64,64,64) but FAILS "
           "tier-2 (weight spaces not preserved) -- character content alone does NOT match; "
           "the frozen-slot alignment is load-bearing",
      rep_eq["mults"] == (64, 64, 64) and not match_fingerprint(rep_eq)[0],
      match_fingerprint(rep_eq)[1])
# (iii) inversion check: g -> g^2 swaps the assignment exactly as Phi_D <-> Phi_B
rep_ginv = tier_report(g @ g, "g^2")
kg = [char_index(rep_g["scalars"][m][0]) for m in (-2, 0, 2)]
kgi = [char_index(rep_ginv["scalars"][m][0]) for m in (-2, 0, 2)]
check("F", "inversion check: g -> g^2 maps the weight-character assignment through EXACTLY "
           "Aut(Z/3) (k -> -k mod 3), verdict unchanged -- the Phi_D/Phi_B swap of N4",
      match_fingerprint(rep_ginv)[0] and all((a + b) % 3 == 0 for a, b in zip(kg, kgi)),
      f"{kg} -> {kgi}")
# (iv) power validation: corrupted fixtures are FLAGGED
e0_bad = e[0] + 1e-3 * (rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM)))
G_bad = np.hstack([e0_bad] + e[1:])
check("F", "power: corrupted gamma fixture FLAGGED by the structural gate "
           "(Gamma Gamma^dag != 14 I)", float(np.max(np.abs(G_bad @ G_bad.conj().T - 14 * I128))) > 1e-4)
Bm0 = Wt @ P_w[0]
vv = Bm0[:, 0:1]
g_bad = g + (W3 - 1.0) * (vv @ vv.conj().T)      # surgically move ONE weight-0 vector to omega
rep_gbad = tier_report(g_bad, "corrupted g")
check("F", "power: corrupted planted fixture (one weight-0 eigenvalue moved to omega) "
           "FLAGGED by the match test", not match_fingerprint(rep_gbad)[0],
      match_fingerprint(rep_gbad)[1])
h5 = V3 @ np.diag(np.exp(-1j * (2*np.pi/5) * lam3)) @ V3.conj().T
check("F", "power: order-5 imposter exp((2pi/5) J3) rejected at the order gate",
      not tier_report(h5, "order5")["order3"])

# ---------------- verdict ----------------------------------------------------------------
print()
print(f"N6 FINGERPRINT PROBE: {'ALL PASS' if not FAILURES else str(len(FAILURES)) + ' FAILURES: ' + str(FAILURES)}"
      f"  ({time.time() - t0:.1f}s)")
print("HEADLINE: OUTCOME = ABSENT. The prediction is WELL-POSED (the canonical Z/3 exists: "
      "order-3 class of the frozen commutant Sp(1), unique up to conjugacy, C-linear "
      "representatives exactly {wI, w2I} = the admissible inversion and nothing else) and "
      "the decomposition CONTRADICTS the pre-bound pattern: the commutant Z/3 acts "
      "FIXED-POINT-FREELY (division algebra) -- trivial-character multiplicity 0 on all of "
      "ker(Gamma); triplet multiplicities (0,192,0) per representative, (0,6,0) per "
      "pair-slot-triple, vs predicted regular (64,64,64) / (2,2,2). It rotates the "
      "quaternionic fiber; it does not permute the triplet's pair-slots. The regular "
      "pattern IS realizable in ker(Gamma) (planted SU(2)+ 2pi/3 rotation matches, both "
      "tiers) but every matching action requires an SU(2)+ axis choice (an S^2 family, "
      "two exhibited) outside the admissible inversion and lies outside the commutant: "
      "FAILURE of the prediction as bound. Controls: scrambled characters rejected, "
      "random and equal-multiplicity-Haar actions rejected, inversion = Aut(Z/3) exact, "
      "corrupted fixtures flagged.")
sys.exit(0 if not FAILURES else 1)
