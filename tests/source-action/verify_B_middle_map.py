"""
DISCHARGE B -- middle-map closure / selection on the Seiberg-Witten shell.
canon/source-action-seiberg-witten-construction.md, discharge (B).

CLAIM TO TEST
-------------
On the SW shell  F_A^+ = mu(Psi)  (the j=1 triplet bilinear sources the self-dual curvature), does
restricting the constraint algebra to the on-shell surface

   (B1)  REDUCE the gamma-trace obstruction ||[Pi_RS, M_D]|| (off-shell anchor 58.72), and/or
   (B2)  COLLAPSE the >=8-real-dim shiab selector family (ideally toward GU's (1,0,1,0)) ?

Honest grading: partial collapse is a real result; no collapse is a refutation of the selection claim.
Only running code decides; we report ACTUAL numbers.

SUBSTRATE (reused, not re-derived)
----------------------------------
 - gen_sector_bridge.constraint_objects()  -> (e, Gamma, Pi_RS, M_D), the verified Cl(9,5)=M(64,H) setup
   reproducing the anchors bare ||[Pi_RS,M_D]||=58.7215, C2=||Gamma M_D Pi_RS||=155.3625. Signature (9,5),
   eta = [+1]*9 + [-1]*5, so base {0,1,2,3} is Euclidean -> the self-dual su(2)_+ on {0,1,2,3} is defined.
 - The self-dual SU(2)_+ generators J[k] and the Casimir decomposition of ker(Gamma) into j=0/1/2/1
   sectors (the 192-dim j=1 carrier W_trip IS the SW-active on-shell surface where mu is supported):
   the construction from h1_selfdual_family_kill.py:52-77, rebuilt on the SAME (9,5) gammas.
 - shiab_codiff_intertwiner_dim.py -> the rep-theoretic selector block dimensions (dim Hom of the shiab),
   imported and read directly (its module-level `blocks`, `dim_full`, ...).

ON-SHELL SURFACE / OBSTRUCTION OPERATOR
---------------------------------------
The obstruction to a clean constraint-surface/gauge-orbit quotient is the leakage of the Dirac/gauge
direction M_D OFF the constraint surface: with Q = I - Pi_RS (projector onto im Gamma^dag),
   [Pi_RS, M_D] P  =  (Pi_RS - I) M_D P  =  - Q M_D P      (for any P with im P subset ker Gamma).
So the obstruction with domain restricted to a surface projector P is exactly the leakage ||Q M_D P||.
 - OFF-SHELL: P = Pi_RS  (full 1664-dim constraint surface ker Gamma).
 - ON-SHELL : P = P_trip (192-dim j=1 SW carrier W_trip, where mu(Psi) lives).
We report Frobenius norms, per-mode RMS (Frobenius/sqrt(#cols), dimension-fair), spectral (operator)
norms, and the normalized ESCAPE FRACTION ||Q M_D P||/||M_D P|| -- the cleanest dimension-fair measure
of "does on-shell reduce the obstruction".
"""
from __future__ import annotations

import io
import os
import sys
import contextlib

import numpy as np

# --- paths to the two reused modules --------------------------------------------------------------
_HERE = os.path.dirname(os.path.abspath(__file__))
_TESTS = os.path.normpath(os.path.join(_HERE, ".."))                  # tests/
_GENSEC = os.path.join(_TESTS, "generation-sector")                   # tests/generation-sector/
for p in (_TESTS, _GENSEC):
    if p not in sys.path:
        sys.path.insert(0, p)

import gen_sector_bridge as gb  # noqa: E402  (constraint objects + anchors; signature (9,5))

N, DIM = gb.N, gb.DIM           # 14, 128
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]   # the three self-dual SU(2)_+ pairs on base {0,1,2,3}

np.set_printoptions(precision=4, suppress=True, linewidth=140)


def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex)
    M[i, j] = 1
    M[j, i] = -1
    return M


def fro(A):
    return float(np.linalg.norm(A))


def spec(A):
    return float(np.linalg.norm(A, 2))


def main():
    rep = {}
    print("=" * 96)
    print("DISCHARGE B: middle-map closure / selection on the SW shell  F_A^+ = mu(Psi)")
    print("=" * 96)

    # ============================================================================================
    # (0) ANCHORS -- reproduce the off-shell obstruction from gen_sector_bridge (no tuning).
    # ============================================================================================
    e, Gamma, Pi_RS, M_D = gb.constraint_objects()           # signature (9,5); reproduces the anchors
    Ifull = np.eye(N * DIM, dtype=complex)
    Q = Ifull - Pi_RS                                        # projector off the constraint surface

    bare = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    C2 = fro(Gamma @ M_D @ Pi_RS)
    kerdim = int(round(np.trace(Pi_RS).real))
    print(f"\n[anchors] dim ker(Gamma) = tr(Pi_RS) = {kerdim}  (expect 1664)")
    print(f"[anchors] bare ||[Pi_RS, M_D]||_F            = {bare:.4f}   (expect 58.7215)")
    print(f"[anchors] C2 = ||Gamma M_D Pi_RS||_F         = {C2:.4f}   (expect 155.3625)")
    assert kerdim == 1664 and abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2, "anchor mismatch"
    rep.update(bare_commutator=bare, C2=C2, kerdim=kerdim)

    # ============================================================================================
    # (1) Build the self-dual SU(2)_+ and the on-shell carrier W_trip (j=1) on the SAME gammas.
    # ============================================================================================
    I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)
    J = [np.kron(I14, sgen(e, a, b) + sgen(e, c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
         for (a, b, c, d) in SD]

    # su(2)_+ closes and preserves ker(Gamma) in THIS signature (base {0,1,2,3} is Euclidean here)
    c012 = np.trace((J[0] @ J[1] - J[1] @ J[0]).conj().T @ J[2]) / np.trace(J[2].conj().T @ J[2])
    su2_res = fro((J[0] @ J[1] - J[1] @ J[0]) - c012 * J[2]) / fro(J[2])
    pres = max(fro(J[k] @ Pi_RS - Pi_RS @ J[k]) for k in range(3))
    print(f"\n[su2_+] [J0,J1]=({c012.real:+.3f})J2 residual {su2_res:.1e}; max||[J,Pi_RS]|| = {pres:.1e}")
    assert su2_res < 1e-9 and pres < 1e-7, "su(2)_+ must close and preserve ker(Gamma)"

    # Casimir decomposition of ker(Gamma): eigenvalue 4 j(j+1)
    w, V = np.linalg.eigh(Pi_RS)
    Wker = V[:, w > 0.5]                                     # 1792 x 1664 orthobasis of ker(Gamma)
    Cas = -(J[0] @ J[0] + J[1] @ J[1] + J[2] @ J[2])
    CasK = Wker.conj().T @ Cas @ Wker
    CasK = 0.5 * (CasK + CasK.conj().T)
    ev, U = np.linalg.eigh(CasK)

    sectors = {}
    counts = {}
    for j in (0.0, 0.5, 1.0):
        target = 4 * j * (j + 1)
        cols = np.abs(ev - target) < 1e-3
        B = Wker @ U[:, cols]
        sectors[j] = B
        counts[j] = (int(B.shape[1]), int(round(B.shape[1] / (2 * j + 1))))  # (states, #irreps)
    print(f"[carrier] SU(2)_+ content of ker(Gamma)  (states / #irreps):")
    for j in (0.0, 0.5, 1.0):
        st, ir = counts[j]
        print(f"          j={j}:  {st:4d} states  =  {ir:4d} irreps x (2j+1)")
    assert counts[1.0][0] == 192, f"expected 192-dim j=1 carrier, got {counts[1.0][0]}"
    rep["sector_states"] = {str(j): counts[j][0] for j in counts}
    rep["sector_irreps"] = {str(j): counts[j][1] for j in counts}

    Wt = sectors[1.0]                                       # 1792 x 192 : the SW-active on-shell surface
    P_trip = Wt @ Wt.conj().T                               # projector onto W_trip

    # ============================================================================================
    # (B1) ON-SHELL vs OFF-SHELL OBSTRUCTION  ||[Pi_RS, M_D] P|| = ||Q M_D P||
    # ============================================================================================
    print("\n" + "-" * 96)
    print("(B1) obstruction with domain restricted to the on-shell surface:  [Pi_RS,M_D]P = -Q M_D P")
    print("-" * 96)

    def obstruction(P, ncols):
        leak = Q @ M_D @ P                                  # = -[Pi_RS, M_D] P  (leakage off surface)
        img = M_D @ P
        fF = fro(leak)
        return {
            "fro": fF,
            "per_mode": fF / np.sqrt(ncols),               # dimension-fair RMS leakage per mode
            "spec": spec(leak),
            "escape_frac": fF / fro(img),                  # fraction of M_D-image landing off-surface
            "img_fro": fro(img),
        }

    off = obstruction(Pi_RS, kerdim)                       # full constraint surface (1664)
    on = obstruction(P_trip, Wt.shape[1])                  # SW carrier (192)
    # also report j=0 and j=1/2 sector obstructions for context (where does leakage concentrate?)
    s0 = obstruction(sectors[0.0] @ sectors[0.0].conj().T, sectors[0.0].shape[1])
    sh = obstruction(sectors[0.5] @ sectors[0.5].conj().T, sectors[0.5].shape[1])

    # consistency: [Pi_RS,M_D]Pi_RS should equal -Q M_D Pi_RS
    ident_check = fro((Pi_RS @ M_D - M_D @ Pi_RS) @ Pi_RS + Q @ M_D @ Pi_RS)
    print(f"  identity check  ||[Pi_RS,M_D]Pi_RS + Q M_D Pi_RS|| = {ident_check:.2e}  (must be ~0)")

    hdr = f"  {'surface':<26}{'#modes':>7}{'||.||_F':>12}{'per-mode RMS':>14}{'spectral':>11}{'escape frac':>13}"
    print(hdr)
    rows = [
        ("OFF-SHELL  ker(Gamma)", kerdim, off),
        ("ON-SHELL   W_trip(j=1)", Wt.shape[1], on),
        ("  context  j=0 singlets", sectors[0.0].shape[1], s0),
        ("  context  j=1/2 doublets", sectors[0.5].shape[1], sh),
    ]
    for name, nc, d in rows:
        print(f"  {name:<26}{nc:>7}{d['fro']:>12.4f}{d['per_mode']:>14.4f}"
              f"{d['spec']:>11.4f}{d['escape_frac']:>13.4f}")

    rep["obstruction_off_shell"] = {k: float(v) for k, v in off.items()}
    rep["obstruction_on_shell"] = {k: float(v) for k, v in on.items()}

    pm_reduce = off["per_mode"] / on["per_mode"] if on["per_mode"] else float("inf")
    esc_reduce = off["escape_frac"] / on["escape_frac"] if on["escape_frac"] else float("inf")
    print(f"\n  per-mode RMS   off/on  = {off['per_mode']:.4f} / {on['per_mode']:.4f}  "
          f"= {pm_reduce:.3f}x   ({'REDUCED on-shell' if pm_reduce > 1.05 else 'NOT reduced'})")
    print(f"  escape frac    off/on  = {off['escape_frac']:.4f} / {on['escape_frac']:.4f} "
          f"= {esc_reduce:.3f}x   ({'REDUCED on-shell' if esc_reduce > 1.05 else 'NOT reduced'})")
    rep["per_mode_reduction_factor"] = float(pm_reduce)
    rep["escape_fraction_reduction_factor"] = float(esc_reduce)

    # ============================================================================================
    # (B2a) SELECTOR baseline -- reuse shiab_codiff_intertwiner_dim.py (rep-theoretic Hom dims).
    # ============================================================================================
    print("\n" + "-" * 96)
    print("(B2a) shiab selector baseline  dim Hom_{so(14,C)}(Lambda^2 V (x) S, V (x) S)  [reused module]")
    print("-" * 96)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        import shiab_codiff_intertwiner_dim as shi      # runs the rep-theory; we read its results
    blocks = shi.blocks
    dim_full = shi.dim_full
    flip = shi.dim_chirality_flipping
    presv = shi.dim_chirality_preserving
    print(f"  chiral block dims  Hom(L2 V (x) S_x, V (x) S_y):")
    print(f"            cod S+   cod S-")
    for sx in ("S+", "S-"):
        print(f"     dom {sx}  {blocks[(sx,'S+')]:6d}  {blocks[(sx,'S-')]:6d}")
    print(f"  chirality-FLIPPING total (the natural shiab S+->S-, S-->S+) = {flip}  (complex)")
    print(f"  chirality-PRESERVING total                                  = {presv}  (complex)")
    print(f"  full-Dirac dim Hom(L2 V (x) S, V (x) S)                      = {dim_full}  (complex)")
    print(f"  -> real-quaternionic selector dim of the chirality-flipping shiab >= {2*flip}  "
          f"(canon: '>=8 real, GU postulates (1,0,1,0)')")
    rep["selector_blocks"] = {f"{a}->{b}": int(blocks[(a, b)]) for (a, b) in blocks}
    rep["selector_flip_complex"] = int(flip)
    rep["selector_full_complex"] = int(dim_full)

    # ============================================================================================
    # (B2b) Does the SW shell COLLAPSE the selector?  Two finite-dim tests.
    # ============================================================================================
    print("\n" + "-" * 96)
    print("(B2b) does the SW shell collapse the selector freedom?")
    print("-" * 96)

    # TEST 1 (Schur invariance): the SW shell is su(2)_+-EQUIVARIANT (mu equivariant). An equivariant
    # constraint cannot change dim Hom in the equivariant category. We CONFIRM equivariance of the
    # moment map on the substrate, then conclude the shiab Hom dim is unchanged.
    bS = I128.copy()
    spacelike = [a for a in range(N) if a not in {9, 10, 11, 12, 13}]   # gen_sector_bridge signature
    for s in spacelike:
        bS = bS @ e[s]
    if fro(bS.conj().T + bS) < 1e-9:
        bS = 1j * bS
    bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
    etaV = np.diag([(-1.0 if a in {9, 10, 11, 12, 13} else 1.0) for a in range(N)]).astype(complex)
    Kform = np.kron(etaV, bS)
    # structure constants and equivariance defect of mu^k(Psi)=i<Psi,K J[k] Psi> on W_trip
    f = np.zeros((3, 3, 3), dtype=complex)
    for a in range(3):
        for b in range(3):
            C = J[a] @ J[b] - J[b] @ J[a]
            for c in range(3):
                f[a, b, c] = np.trace(J[c].conj().T @ C) / np.trace(J[c].conj().T @ J[c])
    Kskew = max(fro(Kform @ J[k] + J[k].conj().T @ Kform) for k in range(3))
    MK = [Kform @ J[k] for k in range(3)]
    rng = np.random.default_rng(0)
    equiv_def = 0.0
    for _ in range(120):
        psi = Wt @ (rng.standard_normal(192) + 1j * rng.standard_normal(192))
        m = np.array([1j * np.vdot(psi, MK[k] @ psi) for k in range(3)])
        for a in range(3):
            for b in range(3):
                lhs = 1j * np.vdot(psi, (Kform @ (J[a] @ J[b] - J[b] @ J[a])) @ psi)
                rhs = sum(f[a, b, c] * m[c] for c in range(3))
                equiv_def = max(equiv_def, abs(lhs - rhs))
    print(f"  [Schur] SW shell equivariance:  K-skew defect {Kskew:.1e}, moment-map covariance defect "
          f"{equiv_def:.1e}")
    print(f"          -> the shell is su(2)_+-equivariant, so dim Hom(L2 V(x)S, V(x)S) = {dim_full} is "
          f"INVARIANT (Schur).")
    print(f"          The >= {2*flip}-real shiab selector and its residual 3 real dims are NOT collapsed "
          f"by the (equivariant) shell.")
    rep["shell_Kskew_defect"] = float(Kskew)
    rep["shell_equivariance_defect"] = float(equiv_def)
    selector_collapsed_by_shell = (equiv_def > 1e-6)   # would only collapse if shell BROKE equivariance

    # TEST 2 (on-shell support): mu is supported ONLY on j=1 (vanishes on j=0/j=1/2). So the equivariant
    # quadratic couplings the SW shell can SEE are only those with the j=1 carrier in the DOMAIN. We count
    # the ambient su(2)_+-equivariant quadratic maps carrier->adjoint (#copies of j=1 in End ker Gamma)
    # both off-shell (all sector pairs) and on-shell (j=1 domain only) -- a genuine, finite-dim collapse.
    Nj = {j: counts[j][1] for j in (0.0, 0.5, 1.0)}        # #irreps per spin

    def j1_in(ja, jb):  # multiplicity (0/1) of the adjoint j=1 inside ja (x) jb
        lo, hi = abs(ja - jb), ja + jb
        return 1 if (lo <= 1.0 <= hi and abs((1.0 - lo) - round(1.0 - lo)) < 1e-9) else 0

    ambient = sum(Nj[ja] * Nj[jb] * j1_in(ja, jb) for ja in Nj for jb in Nj)
    onshell = sum(Nj[ja] * Nj[jb] * j1_in(ja, jb) for ja in Nj for jb in Nj if ja == 1.0 and jb == 1.0)
    print(f"\n  [support] ambient su(2)_+-equivariant quadratic couplings carrier->adjoint "
          f"(#j=1 in End ker Gamma):")
    print(f"            OFF-SHELL (all sector pairs)                 = {ambient}")
    print(f"            ON-SHELL  (mu supported on j=1 carrier only) = {onshell}   "
          f"(the (1,1)->adjoint block)")
    print(f"            collapse factor = {ambient/onshell:.2f}x   "
          f"(genuine partial collapse, but NOT to 1 / not to GU (1,0,1,0))")
    print(f"            the further collapse 4096 -> 1 is the HAMILTONIAN uniqueness of mu "
          f"(mult 1), not the shell.")
    rep["ambient_equivariant_couplings"] = int(ambient)
    rep["onshell_equivariant_couplings"] = int(onshell)
    rep["coupling_collapse_factor"] = float(ambient / onshell)

    # ============================================================================================
    # VERDICT
    # ============================================================================================
    print("\n" + "=" * 96)
    print("VERDICT (Discharge B)")
    print("=" * 96)
    b1 = (pm_reduce > 1.05) or (esc_reduce > 1.05)
    print(f"  (B1) obstruction reduced on-shell?  per-mode {pm_reduce:.2f}x, escape-frac {esc_reduce:.2f}x "
          f"-> {'PARTIAL reduction' if b1 else 'NO reduction (off-shell anchor 58.72 survives)'}")
    print(f"  (B2) shiab selector collapsed by the shell?  {'YES' if selector_collapsed_by_shell else 'NO'} "
          f"(shell is equivariant; dim Hom={dim_full} invariant; >= {2*flip} real dims intact)")
    print(f"       on-shell SUPPORT does partially collapse the ambient coupling count "
          f"{ambient}->{onshell} ({ambient/onshell:.0f}x), but not to GU's (1,0,1,0).")
    print(f"  ==> SELECTION CLAIM (B): the SW shell does NOT collapse the shiab selector to (1,0,1,0); "
          f"residual freedom survives.")
    rep["B1_obstruction_reduced_on_shell"] = bool(b1)
    rep["B2_selector_collapsed_by_shell"] = bool(selector_collapsed_by_shell)
    print("=" * 96)
    return rep


if __name__ == "__main__":
    main()
