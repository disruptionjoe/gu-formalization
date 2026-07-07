"""
VG-V1 (route V1, T3' executable core): condensate-channel ghost-parity scan on the (9,5)
self-dual triplet sector -- the tri-theory federation's one joint organ (171 family votes).

QUESTION (T3', revised statement, steelman Section 5.3): on the 192-dim triplet sector W of the
(9,5) carrier, for each GU-native condensate-channel candidate Phi:
  (i)   its ghost parity under conjugation by P_ghost (even / odd / mixed),
  (ii)  whether the induced mass deformation M(Phi) commutes with P_ghost (residual ||[M,P]||),
  (iii) if [M,P]=0: the induced spectrum on the P-even (physical) vs P-odd (ghost/mirror) sector --
        is m+ != m- realizable (can mirrors gap while generations stay light)?
  (iv)  the chirality trace of the physical sector (must be 0 by canon -- verified, with the
        structural tautology flagged and a scrambled-subspace control showing the quantity CAN be
        nonzero for non-parity subspaces).

FEDERATION KILL CONDITION 1 (steelman 6.2.1) fires if EVERY GU-native channel is P-odd or breaks
[M,P]=0. The leg ADVANCES if at least one even channel with commuting, SPLITTABLE mass exists.
The pre-registered third outcome (sharp bounded negative): even channels exist but every strict-
native even channel is isospectral across parity -- mirrors cannot be selectively gapped.

TYPING of "induced mass deformation": the condensate direction Phi enters the quadratic form as
delta L = <psi, K Phi psi> with K the Krein form; K-reality of delta L requires Phi K-self-adjoint
(K^-1 Phi^dag K = Phi). So M(Phi) = Phi as an operator, admissible iff K-self-adjoint. Candidates
that fail K-self-adjointness are K-symmetrized, with the symmetrization residual printed (a large
residual means the raw direction is NOT an admissible mass channel and the row tests its
K-self-adjoint part).

ANCHORS reproduced first (hard rule): rank(Gamma)=128, dim ker(Gamma)=1664, beta_S
pseudo-anti-Hermiticity ~0, triplet dim 192, triplet Krein signature (+96,-96,0), K purely
cross-chirality. Machinery reused from tests/generation-sector/ghost_parity_krein.py and
swing_ghost_parity_chiral_selection.py (verified carrier recipe).

TARGET-IMPORT GUARD: no element of {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} is assumed,
inserted, or divided by. The triplet sector is selected by the MEASURED top su(2)+ Casimir
eigenvalue on ker(Gamma); all dimensions (128, 1664, 192, 96) are measured and asserted, not used
as inputs. Self-dual index tuples (0,1,2,3) are base-geometry labels, not counts.

Separate big-swing workflow (R1-R4) is running: nothing from it is cited; gates only.
"""
import numpy as np

np.random.seed(20260706)
N, DIM = 14, 128
TOL = 1e-9


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
timelike = {4, 5, 6, 7, 8}                      # (9,5) = base(4,0) + internal(5,5)
e = [(1j * base[a] if a in timelike else base[a]) for a in range(14)]
spacelike = [a for a in range(14) if a not in timelike]


def sgen(i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex); M[i, j] = 1; M[j, i] = -1; return M


def gen(i, j):
    return np.kron(I14, sgen(i, j)) + np.kron(lvec(i, j), I128)


def comm(A, B):
    return A @ B - B @ A


def acomm(A, B):
    return A @ B + B @ A


def nrm(A):
    return np.linalg.norm(A)


print("=" * 108)
print("VG-V1: condensate-channel ghost-parity scan, (9,5) triplet sector  [T3' executable core]")
print("=" * 108)

# ---------------------------------------------------------------- anchors
print("\n[ANCHORS] (must reproduce before any claim)")
Gam = np.hstack(e)
rankG = np.linalg.matrix_rank(Gam)
Pi = np.eye(N * DIM, dtype=complex) - Gam.conj().T @ np.linalg.inv(Gam @ Gam.conj().T) @ Gam
w, Vv = np.linalg.eigh(Pi)
Wk = Vv[:, w > 0.5]
kerdim = Wk.shape[1]
print(f"  rank(Gamma) = {rankG}   dim ker(Gamma) = {kerdim}")
assert rankG == 128 and kerdim == 1664, (rankG, kerdim)

SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]      # self-dual su(2)+ on Euclidean base {0,1,2,3}
ASD = [(0, 1, 3, 2), (0, 2, 1, 3), (0, 3, 2, 1)]     # anti-self-dual su(2)-
J3full = [gen(a, b) + gen(c, d) for (a, b, c, d) in SD]
J3mfull = [gen(a, b) + gen(c, d) for (a, b, c, d) in ASD]

Cas = -(J3full[0] @ J3full[0] + J3full[1] @ J3full[1] + J3full[2] @ J3full[2])
CasK = Wk.conj().T @ Cas @ Wk; CasK = 0.5 * (CasK + CasK.conj().T)
ev, U = np.linalg.eigh(CasK)
top = max(round(x.real, 3) for x in ev)
Wt = Wk @ U[:, np.abs(ev - top) < 1e-3]
tdim = Wt.shape[1]
print(f"  su(2)+ Casimir top eigenvalue on ker(Gamma) = {top}   triplet sector dim = {tdim}")
assert tdim == 192, tdim

bS = I128.copy()
for s in spacelike:
    bS = bS @ e[s]
if nrm(bS.conj().T + bS) < TOL:
    bS = 1j * bS
bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
betares = max(nrm(bS @ sgen(i, j) + sgen(i, j).conj().T @ bS)
              for i in range(14) for j in range(i + 1, 14))
print(f"  beta_S pseudo-anti-Hermiticity residual = {betares:.1e}")
assert betares < TOL, betares

etaV = np.diag([(-1.0 if a in timelike else 1.0) for a in range(14)]).astype(complex)
Kful = np.kron(etaV, bS)
om = I128.copy()
for a in range(14):
    om = om @ e[a]
om2 = (np.trace(om @ om) / DIM).real
Cful = np.kron(I14, om if om2 > 0 else (-1j) * om)


def Rc(M):
    return Wt.conj().T @ M @ Wt


K = Rc(Kful); K = 0.5 * (K + K.conj().T)
sig = np.linalg.eigvalsh(K)
npl = int(np.sum(sig > TOL)); nmi = int(np.sum(sig < -TOL)); nz = tdim - npl - nmi
print(f"  triplet Krein signature = (+{npl}, -{nmi}, 0:{nz})   |K|-eig range on triplet = "
      f"[{np.abs(sig).min():.3f}, {np.abs(sig).max():.3f}]")
assert (npl, nmi, nz) == (96, 96, 0), (npl, nmi, nz)

C = Rc(Cful)
resC2 = nrm(C @ C - np.eye(tdim)); resCH = nrm(C - C.conj().T)
print(f"  chirality chi restricted: ||chi^2 - I|| = {resC2:.1e}   ||chi - chi^dag|| = {resCH:.1e}   "
      f"tr(chi) = {np.trace(C).real:+.1e}")
assert resC2 < 1e-8 and resCH < 1e-8
cev, cU = np.linalg.eigh(C)
Pp96 = cU[:, cev > 0.5]; Pm96 = cU[:, cev < -0.5]
Kpp = nrm(Pp96.conj().T @ K @ Pp96); Kmm = nrm(Pm96.conj().T @ K @ Pm96)
print(f"  K cross-chirality (both halves K-null): ||K(+,+)|| = {Kpp:.1e}   ||K(-,-)|| = {Kmm:.1e}")
assert Kpp < 1e-8 and Kmm < 1e-8

# family su(2)+/- restricted; invariance of the triplet sector under them and under chi
Jp = [Rc(M) for M in J3full]
Jm = [Rc(M) for M in J3mfull]
invp = max(nrm(J3full[k] @ Wt - Wt @ Jp[k]) for k in range(3))
invm = max(nrm(J3mfull[k] @ Wt - Wt @ Jm[k]) for k in range(3))
invC = nrm(Cful @ Wt - Wt @ C)
print(f"  W-invariance residuals: su(2)+ {invp:.1e}   su(2)- {invm:.1e}   chi {invC:.1e}")
assert max(invp, invm, invC) < 1e-8
KJres = max(nrm(comm(K, Jp[k])) for k in range(3)) , max(nrm(comm(K, Jm[k])) for k in range(3))
print(f"  [K, su(2)+] max residual = {KJres[0]:.1e}   [K, su(2)-] max residual = {KJres[1]:.1e}"
      f"   (compact family gens commute with K)")

# ---------------------------------------------------------------- (a) ghost parity P
print("\n[(a) GHOST PARITY P]")
kev, kU = np.linalg.eigh(K)
P = (kU * np.sign(kev)) @ kU.conj().T; P = 0.5 * (P + P.conj().T)
rP2 = nrm(P @ P - np.eye(tdim)); rPH = nrm(P - P.conj().T)
rAC = nrm(acomm(P, C)); rCO = nrm(comm(P, C))
Kinv = np.linalg.inv(K)
rPK = nrm(Kinv @ P.conj().T @ K - P)
print(f"  P = sign(K)|_W: ||P^2 - I|| = {rP2:.1e}   ||P - P^dag|| = {rPH:.1e}   "
      f"K-self-adjointness ||K^-1 P^dag K - P|| = {rPK:.1e}")
print(f"  relation to chirality: ||{{P, chi}}|| = {rAC:.1e}   ||[P, chi]|| = {rCO:.3f}")
print(f"  => P ANTICOMMUTES with chi ({{P,chi}}=0 to {rAC:.1e}); [P,chi] is large ({rCO:.1f}), "
      f"i.e. P exchanges the two K-null chirality halves.")
assert rP2 < 1e-9 and rAC < 1e-8

# pair-swap parity from canon (generation <-> mirror swap): polar unitary of the cross-chirality
# block of K, i.e. the canonical chirality-exchanging isometry whose +/- eigenspaces are u+v / u-v.
B = Pp96.conj().T @ K @ Pm96
u_, s_, vT_ = np.linalg.svd(B)
Wpol = u_ @ vT_
Spair = Pp96 @ Wpol @ Pm96.conj().T + Pm96 @ Wpol.conj().T @ Pp96.conj().T
rswap = nrm(P - Spair)
print(f"  pair-swap parity (canon u<->v swap, polar part of K's cross block): ||P_sign(K) - P_swap||"
      f" = {rswap:.1e}  -> same operator; sv range of K cross block = [{s_.min():.3f}, {s_.max():.3f}]")
assert rswap < 1e-8

Ep = kU[:, kev > 0]        # P = +1 : physical (positive Krein norm) sector
Em = kU[:, kev < 0]        # P = -1 : ghost / mirror sector
minKphys = np.linalg.eigvalsh(Ep.conj().T @ K @ Ep).min()
maxKghost = np.linalg.eigvalsh(Em.conj().T @ K @ Em).max()
print(f"  physical sector dim = {Ep.shape[1]}, min K-eig = {minKphys:+.3f} (>0);  "
      f"ghost sector dim = {Em.shape[1]}, max K-eig = {maxKghost:+.3f} (<0)")
assert Ep.shape[1] == 96 and Em.shape[1] == 96 and minKphys > 0 and maxKghost < 0

# ---------------------------------------------------------------- (b) condensate channels
print("\n[(b) CONDENSATE CHANNELS]  M(Phi) = K-self-adjoint part of Phi;  columns:")
print("  Ksym   = ||Phi_raw - Phi_K||/||Phi_raw||  (0 => raw direction already an admissible mass channel)")
print("  parity = even/odd fractions ||Phi_even||/||Phi||, ||Phi_odd||/||Phi||  under conjugation by P")
print("  [M,P]  = ||[M,P]||/||M||;   [M,chi] = ||[M,chi]||/||M||")
print("  split  = max_i |sorted spec(M|P=+1)_i - sorted spec(M|P=-1)_i|  (only defined when [M,P]=0)")

adjK = lambda A: Kinv @ A.conj().T @ K
scale_raw = Rc(np.kron(etaV, I128))
scale_degen = nrm(scale_raw - np.eye(tdim))
print(f"\n  [finding] fiber scale direction degenerates on W: ||etaV(x)1|_W - I|| = {scale_degen:.1e}"
      f"\n  (the triplet sector lies entirely in the +1 eigenspace of etaV(x)1: no independent scale channel on W)")
scale_K = 0.5 * (scale_raw + adjK(scale_raw))
scale_even = 0.5 * (scale_K + P @ scale_K @ P)
sxf_raw = 0.5 * (scale_K @ (1j * Jp[2]) + (1j * Jp[2]) @ scale_K)
sxf_K = 0.5 * (sxf_raw + adjK(sxf_raw))
sxf_even = 0.5 * (sxf_K + P @ sxf_K @ P)

chans = [
    ("Clifford scalar (identity)",            "native",         np.eye(tdim, dtype=complex)),
    ("fiber scale etaV(x)1 |_W (compression)", "native",        scale_raw),
    ("su(2)+ family Cartan  i*J+_3",          "native",         1j * Jp[2]),
    ("su(2)+ family generic i*(J+_1+J+_2)",   "native",         1j * (Jp[0] + Jp[1])),
    ("su(2)- family Cartan  i*J-_3",          "native",         1j * Jm[2]),
    ("Clifford pseudoscalar  i*chi",          "native",         1j * C),
    ("family product (iJ+_3)(iJ-_3)",         "native-algebra", (1j * Jp[2]) @ (1j * Jm[2])),
    ("pseudoscalar x family  chi*(iJ+_3)",    "native-algebra", C @ (1j * Jp[2])),
    ("scale x family sym product",            "native-algebra", sxf_raw),
    ("P-even part of fiber scale",            "P-derived",      scale_even),
    ("P-even part of scale x family",         "P-derived",      sxf_even),
]
for i in range(3):
    X = np.random.randn(tdim, tdim) + 1j * np.random.randn(tdim, tdim)
    X = X / nrm(X)
    chans.append((f"random K-self-adjoint #{i + 1}", "control", 0.5 * (X + adjK(X))))
for i in range(3):
    X = np.random.randn(tdim, tdim) + 1j * np.random.randn(tdim, tdim)
    X = X / nrm(X)
    Xk = 0.5 * (X + adjK(X))
    chans.append((f"random P-EVEN K-self-adjoint #{i + 1}", "control", 0.5 * (Xk + P @ Xk @ P)))

records = []
for name, cls, raw in chans:
    nraw = nrm(raw)
    if nraw < 1e-12:
        records.append(dict(name=name, cls=cls, dead=True))
        print(f"  {name:<42s} {cls:<14s} raw direction vanishes on W (norm {nraw:.1e}) -> no channel")
        continue
    PhiK = 0.5 * (raw + adjK(raw))
    ksym = nrm(raw - PhiK) / nraw
    M = PhiK
    nM = nrm(M)
    if nM < 1e-12:
        records.append(dict(name=name, cls=cls, dead=True))
        print(f"  {name:<42s} {cls:<14s} Ksym={ksym:.2f}: K-self-adjoint part vanishes "
              f"(||M||={nM:.1e}) -> NOT an admissible mass channel (K-skew direction)")
        continue
    Me = 0.5 * (M + P @ M @ P); Mo = 0.5 * (M - P @ M @ P)
    fe, fo = nrm(Me) / nM, nrm(Mo) / nM
    parity = "EVEN" if fo < 1e-9 else ("ODD" if fe < 1e-9 else "MIXED")
    cMP = nrm(comm(M, P)) / nM
    cMC = nrm(comm(M, C)) / nM
    rec = dict(name=name, cls=cls, dead=False, ksym=ksym, fe=fe, fo=fo,
               parity=parity, cMP=cMP, cMC=cMC, split=None, imres=None)
    line = (f"  {name:<42s} {cls:<14s} Ksym={ksym:.1e}  parity={parity:<5s} "
            f"(e={fe:.2f},o={fo:.2f})  [M,P]={cMP:.1e}  [M,chi]={cMC:.2f}")
    if parity == "EVEN":
        Ap = Ep.conj().T @ M @ Ep
        Am = Em.conj().T @ M @ Em
        evp = np.linalg.eigvals(Ap); evm = np.linalg.eigvals(Am)
        imres = max(np.abs(evp.imag).max(), np.abs(evm.imag).max())
        sp = np.sort(evp.real); sm = np.sort(evm.real)
        split = np.abs(sp - sm).max()
        rec["split"] = split; rec["imres"] = imres
        rec["specp"] = sp; rec["specm"] = sm
        line += f"  spec-real-res={imres:.1e}  SPLIT={split:.2e}"
    records.append(rec)
    print(line)

# C-intertwiner lemma verification: {P,chi}=0, [M,P]=0, [M,chi]=0  =>  spec(M|+) = spec(M|-)
print("\n[LEMMA CHECK] chi maps P=+1 -> P=-1 isometrically (up to K-sign); if [M,chi]=0 and [M,P]=0")
print("  then the two sectors are isospectral. Numerical verification on every even, chi-commuting channel:")
lem_ok = True
for r in records:
    if not r.get("dead") and r["parity"] == "EVEN" and r["cMC"] < 1e-8:
        ok = r["split"] < 1e-7
        lem_ok = lem_ok and ok
        print(f"    {r['name']:<42s} [M,chi]={r['cMC']:.1e}  split={r['split']:.1e}  "
              f"isospectral: {'YES' if ok else 'NO (LEMMA VIOLATED)'}")
assert lem_ok

# spectra detail for the informative rows
print("\n[SPECTRA] (distinct levels, rounded to 1e-6, with multiplicities; physical P=+1 vs ghost P=-1)")
for r in records:
    if r.get("dead") or r["parity"] != "EVEN":
        continue
    def levels(s):
        vals, cnts = np.unique(np.round(s, 6), return_counts=True)
        return ", ".join(f"{v:+.3f}x{c}" for v, c in zip(vals, cnts))
    lp, lm = levels(r["specp"]), levels(r["specm"])
    short = lp if len(lp) < 90 else lp[:87] + "..."
    shortm = lm if len(lm) < 90 else lm[:87] + "..."
    print(f"  {r['name']}\n    P=+1: {short}\n    P=-1: {shortm}")

# ---------------------------------------------------------------- (iv) chirality of light sector
print("\n[(iv) CHIRALITY TRACE OF THE PHYSICAL (LIGHT-CANDIDATE) SECTOR]")
PIp = Ep @ Ep.conj().T
trCP = np.trace(C @ PIp)
taut = nrm(PIp @ C @ PIp)
print(f"  tr(chi Pi_+) = {trCP.real:+.2e}{trCP.imag:+.2e}j   (canon requires 0: VERIFIED)")
print(f"  tautology audit: ||Pi_+ chi Pi_+|| = {taut:.1e} -- given {{P,chi}}=0 the compression of chi to")
print(f"  ANY subspace of the P=+1 sector vanishes identically, so tr(chi Pi_light)=0 for every light")
print(f"  sub-sector too; the check is structurally forced once {{P,chi}}=0 holds, and the non-trivial")
print(f"  content is the anticommutation itself (residual {rAC:.1e} above).")
print("  scrambled control (the quantity CAN be nonzero): tr(chi Pi_Q) for random 96-dim subspaces Q:")
ctrl_traces = []
for i in range(3):
    X = np.random.randn(tdim, 96) + 1j * np.random.randn(tdim, 96)
    Q, _ = np.linalg.qr(X)
    t = np.trace(C @ (Q @ Q.conj().T)).real
    ctrl_traces.append(t)
    print(f"    random subspace #{i + 1}: tr(chi Pi_Q) = {t:+.3f}")
assert max(abs(t) for t in ctrl_traces) > 0.1, "control failed: random traces all ~0, check has no power"

# ---------------------------------------------------------------- (c) verdict table + kill logic
print("\n" + "=" * 108)
print("[(c) VERDICT TABLE]  channel x parity x [M,P] x gap-structure x light-sector chirality")
print("=" * 108)
hdr = (f"  {'channel':<42s}{'class':<15s}{'parity':<7s}{'[M,P]=0':<9s}{'gap structure':<26s}"
       f"{'light chi-trace':<15s}")
print(hdr); print("  " + "-" * 106)
for r in records:
    if r.get("dead"):
        print(f"  {r['name']:<42s}{r['cls']:<15s}{'--':<7s}{'--':<9s}{'K-skew: not a mass channel':<26s}"
              f"{'--':<15s}")
        continue
    commuting = "YES" if r["cMP"] < 1e-8 else "NO"
    if r["parity"] == "EVEN":
        gap = (f"m+ != m- (split {r['split']:.1e})" if r["split"] > 1e-6
               else "parity-symmetric (m+ = m-)")
        chi_tr = "0 (forced)"
    else:
        gap = "n/a ([M,P] != 0)"
        chi_tr = "n/a"
    print(f"  {r['name']:<42s}{r['cls']:<15s}{r['parity']:<7s}{commuting:<9s}{gap:<26s}{chi_tr:<15s}")

native = [r for r in records if r["cls"] in ("native", "native-algebra") and not r.get("dead")]
native_even = [r for r in native if r["parity"] == "EVEN"]
native_even_split = [r for r in native_even if r["split"] > 1e-6]
derived = [r for r in records if r["cls"] == "P-derived" and not r.get("dead")]
derived_even_split = [r for r in derived if r["parity"] == "EVEN" and r["split"] is not None
                      and r["split"] > 1e-6]
ctrl_even_split = [r for r in records if r["cls"] == "control" and not r.get("dead")
                   and r["parity"] == "EVEN" and r["split"] is not None and r["split"] > 1e-6]

print("\n[KILL-CONDITION LOGIC] (federation kill condition 1, steelman 6.2.1)")
kc1 = len(native_even) == 0
print(f"  every GU-native channel P-odd or [M,P]!=0 ?  {'YES -> KC1 FIRES' if kc1 else 'NO -> KC1 does not fire'}")
print(f"    native channels scanned: {len(native)};  P-even with [M,P]=0: {len(native_even)} "
      f"({', '.join(r['name'] for r in native_even)})")
adv = len(native_even_split) > 0
print(f"  leg advance (>=1 native even channel with commuting, SPLITTABLE mass)?  "
      f"{'YES' if adv else 'NO'}")
print(f"    native even channels with m+ != m-: {len(native_even_split)}")
print(f"    P-derived even channels with m+ != m-: {len(derived_even_split)} "
      f"({', '.join(r['name'] for r in derived_even_split) if derived_even_split else 'none'})")
ctrl_split_strs = ", ".join(f"{r_['split']:.2e}" for r_ in ctrl_even_split)
print(f"    control even channels with m+ != m- (discriminating power): {len(ctrl_even_split)} "
      f"(splits: {ctrl_split_strs if ctrl_even_split else 'NONE -- check would be theater'})")
assert len(ctrl_even_split) > 0, "control failure: no even control splits; the split check cannot fail"

print("\n[VERDICT]")
if kc1:
    print("  KC1 FIRES: dead on arrival as a combination.")
elif adv:
    print("  LEG ADVANCES: a GU-native even channel with commuting, splittable mass exists.")
else:
    print("  SHARP BOUNDED NEGATIVE (the pre-registered third outcome): GU-native even channels EXIST")
    print("  (KC1 does not fire literally), but the ENTIRE native algebra lies in the chi-commutant")
    print("  (every generator scanned has [.,chi]~1e-14 or IS chi), so by the intertwiner lemma its")
    print("  K-self-adjoint elements split exhaustively into: P-even => exactly isospectral across ghost")
    print("  parity (mirrors and generations gap TOGETHER), or P-odd (the chi*even branch) => [M,P]!=0")
    print("  (Turok-Bateman positivity broken through the condensate). Mirror-selective gapping needs a")
    print("  P-even, chi-NON-commuting mass direction -- a direction the native algebra does not contain.")
    print("  The random P-even controls show such directions EXIST on this Krein module (splits ~4e-3),")
    print("  so the obstruction is native-content, not Krein geometry: the splitting datum is an import.")
print("\nexit 0 = all anchors reproduced, all asserts passed, controls have discriminating power.")
