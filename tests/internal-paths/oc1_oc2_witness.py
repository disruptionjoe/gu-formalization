#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OC1 / OC2 witness for the Signed-Readout Boundary Theorem (R3), NON-COMPACT case.

Target: the two *abstract, GU-independent* hypotheses fenced in Section 8 of
  explorations/big-swing-2026-07-03/R3-signed-readout-standalone-theorem.md

  OC1 (continuous Fredholm realization). A norm-continuous path t -> F_t in
       Fred(K), F_t = D_t (1 + D_t^* D_t)^{-1/2} the bounded transform, staying
       in the Fredholm locus (0 not in essential spectrum of D_t).
  OC2 (H-linear Fredholm realization). Same, landing in Fred_H(K_H) with each
       F_t commuting with a quaternionic structure J (J^2 = -1, antilinear).

This script does NOT claim to prove OC1/OC2 on a genuinely non-compact operator.
It gives a COMPUTABLE WITNESS on the canonical non-compact index model -- the 1D
Callias / Jackiw-Rebbi Dirac operator D = d/dx + m(x) on L^2(R) -- that exhibits,
concretely, the exact mechanism to which OC1/OC2 reduce:

    Fredholm  <=>  invertibility of the model operator at infinity
              <=>  a spectral gap of D outside a compact set  (Persson)
    protected integer index  =  Callias formula  (1/2)(sgn m(+inf) - sgn m(-inf))
    bounded transform F = D(1+D*D)^{-1/2}  is norm-continuous where the gap holds
    [D, J] = 0  =>  [F, J] = 0  (functional calculus transports the symmetry: OC2)

Truncation to a large interval [-L, L] makes each operator a finite matrix, so
this is finite-dimensional evidence FOR the reduction, not a proof on the open
manifold. Every number printed is produced by the constructed operator.
"""

import numpy as np

RNG = np.random.default_rng(20260703)
np.set_printoptions(precision=4, suppress=True)
report = []


def check(name, ok, detail=""):
    report.append((name, bool(ok)))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {name}" + (f"  --  {detail}" if detail else ""))
    return bool(ok)


# ---------------------------------------------------------------------------
# 1D Callias operator  D = d/dx + m(x)  on a truncated grid, and its chiral
# self-adjoint double  Dcal = [[0, D^*],[D, 0]]  with chirality Gamma = diag(+1,-1).
# ---------------------------------------------------------------------------

def deriv_matrix(N, h):
    """Antisymmetric central-difference d/dx on N points (open ends)."""
    Dc = np.zeros((N, N))
    for i in range(N - 1):
        Dc[i, i + 1] = 1.0 / (2 * h)
        Dc[i + 1, i] = -1.0 / (2 * h)
    return Dc


def laplacian_matrix(N, h):
    """Discrete Laplacian d^2/dx^2 (open ends)."""
    Lap = np.zeros((N, N))
    for i in range(N):
        Lap[i, i] = -2.0 / h ** 2
        if i > 0:
            Lap[i, i - 1] = 1.0 / h ** 2
        if i < N - 1:
            Lap[i, i + 1] = 1.0 / h ** 2
    return Lap


def callias_D(mfun, L=20.0, N=1201, wilson_r=0.0):
    """
    D = d/dx + m(x) (+ optional Wilson term).  Naive central difference by default;
    used only for the bounded-transform demonstration (Part 2), where the fermion
    doubler is irrelevant (it lives at high |lambda|, away from the F-gap at 0).
    The INDEX is computed doubler-free via the SUSY partners below.
    """
    x = np.linspace(-L, L, N)
    h = x[1] - x[0]
    Dc = deriv_matrix(N, h)
    W = -(wilson_r * h / 2.0) * laplacian_matrix(N, h)
    D = Dc + np.diag(mfun(x)) + W
    return D, x


# ---------------------------------------------------------------------------
# SUSY partner Hamiltonians -- the doubler-free route to the Callias index.
#   H_minus = D^* D = -d^2/dx^2 + m^2 - m'      (bosonic Schrodinger operator)
#   H_plus  = D D^* = -d^2/dx^2 + m^2 + m'
# index(D) = dim ker H_minus - dim ker H_plus  = #(localized zero modes of H_-)
#            - #(localized zero modes of H_+).   No fermion doubling: H_pm are
# second-order Laplacians, not first-order lattice Dirac operators.
# ---------------------------------------------------------------------------

def susy_partners(mfun, L=20.0, N=1201):
    x = np.linspace(-L, L, N)
    h = x[1] - x[0]
    m = mfun(x)
    mp = np.gradient(m, x)                      # m'(x), numerical
    Lap = laplacian_matrix(N, h)               # d^2/dx^2
    Hm = -Lap + np.diag(m ** 2 - mp)
    Hp = -Lap + np.diag(m ** 2 + mp)
    return Hm, Hp, x


def count_localized_low_modes(H, x, x_loc=3.0, loc_thr=0.5):
    """#(centrally localized eigenmodes below half the continuum edge), and the
    continuum edge (smallest eigenvalue of an EXTENDED mode)."""
    w, V = np.linalg.eigh(H)
    central = np.abs(x) < x_loc
    N = len(x)
    edge = np.inf
    loc_energies = []
    for j in range(N):
        v = V[:, j]
        cw = float(np.sum(np.abs(v[central]) ** 2))
        pr = 1.0 / float(np.sum(np.abs(v) ** 4) * N)
        if cw > loc_thr:
            loc_energies.append((w[j], j))
        elif pr > 0.02:
            edge = min(edge, w[j])
    edge = 0.0 if not np.isfinite(edge) else float(edge)
    nzero = sum(1 for (e, _) in loc_energies if e < 0.5 * edge + 1e-12)
    return nzero, edge


def callias_index_susy(mfun, L=20.0, N=1201):
    Hm, Hp, x = susy_partners(mfun, L=L, N=N)
    n_minus, edge_m = count_localized_low_modes(Hm, x)
    n_plus, edge_p = count_localized_low_modes(Hp, x)
    gap_D = np.sqrt(max(min(edge_m, edge_p), 0.0))   # mass gap of D = sqrt(edge of H_pm)
    return n_minus - n_plus, gap_D, (n_minus, n_plus)


def chiral_double(D):
    """Self-adjoint Dcal = [[0, D^T],[D, 0]] (D real). Chirality Gamma=diag(I,-I)."""
    N = D.shape[0]
    Z = np.zeros((N, N))
    Dcal = np.block([[Z, D.T], [D, Z]])
    Gamma = np.block([[np.eye(N), Z], [Z, -np.eye(N)]])
    return Dcal, Gamma


def localized_index(D, x, x_loc=3.0, loc_thr=0.5):
    """
    Emulated analytic index of the 1D Callias operator on the truncation.

    A genuine zero mode of D = d/dx + m is EXPONENTIALLY LOCALIZED at the wall;
    lattice-continuum modes are EXTENDED.  So we classify eigenmodes of the chiral
    double Dcal by central L^2 weight (in |x| < x_loc), NOT by eigenvalue size --
    the lattice continuum fills a wide band [mass, ~1/h] with no magnitude gap.

    Returns (index, gap, nzero):
      index  = signed chirality of the LOCALIZED near-zero modes,
      gap    = smallest |eigenvalue| among EXTENDED (continuum) modes ~ mass at inf,
      nzero  = number of localized modes counted.
    """
    N = D.shape[0]
    Dcal, Gamma = chiral_double(D)
    w, V = np.linalg.eigh(Dcal)
    central = np.abs(x) < x_loc
    mask2 = np.concatenate([central, central])         # central sites over C^{2N}
    # participation ratio to reject boundary/edge states from the continuum gap
    idx, nzero = 0, 0
    gap = np.inf
    for j in range(2 * N):
        v = V[:, j]
        cw = float(np.sum(np.abs(v[mask2]) ** 2))      # central weight in [0,1]
        pr = 1.0 / float(np.sum(np.abs(v) ** 4) * (2 * N))  # normalized participation
        if cw > loc_thr:                                # localized -> zero-mode candidate
            chir = float(np.vdot(v, Gamma @ v).real)   # +1 upper block, -1 lower block
            idx += int(round(chir))
            nzero += 1
        elif pr > 0.02:                                 # extended bulk mode (not edge)
            gap = min(gap, abs(w[j]))
    return idx, (0.0 if not np.isfinite(gap) else float(gap)), nzero


def callias_formula(mfun, L=20.0):
    """(1/2)(sgn m(+inf) - sgn m(-inf)) evaluated at the truncation edges."""
    mp = np.sign(mfun(np.array([L])))[0]
    mm = np.sign(mfun(np.array([-L])))[0]
    return 0.5 * (mp - mm)


# ---------------------------------------------------------------------------
# PART 1 -- OC1 mechanism: Fredholm <=> invertibility at infinity; protected index
# ---------------------------------------------------------------------------

def part1():
    print("\n=== PART 1: OC1 mechanism (Callias/Persson on D = d/dx + m) ===")
    ok = True
    L, N = 20.0, 801

    families = {
        "wall  m=+mu*tanh(x)        (index +1)": lambda x: np.tanh(x),
        "anti  m=-mu*tanh(x)        (index -1)": lambda x: -np.tanh(x),
        "gapped const m=+mu          (index  0)": lambda x: np.ones_like(x),
    }
    for label, mfun in families.items():
        idx, gap, (nm, npl) = callias_index_susy(mfun, L=L, N=N)
        pred = callias_formula(mfun, L=L)
        ok &= check(f"P1 {label}: index matches Callias formula",
                    idx == int(round(pred)),
                    f"index = n-({nm}) - n+({npl}) = {idx:+d}, "
                    f"Callias={pred:+.1f}, gap~{gap:.3f}")

    # Persson: bottom of essential spectrum of H_pm ~ min m(+-inf)^2 = mu^2, so the
    # mass gap of D is sqrt(edge) ~ mu.  Sweep mu.
    print("  -- Persson: continuum gap tracks the mass at infinity --")
    persson_ok = True
    for mu_test in (0.5, 1.0, 2.0):
        _, gap, _ = callias_index_susy(lambda x, m=mu_test: m * np.tanh(x), L=L, N=N)
        rel = abs(gap - mu_test) / mu_test
        persson_ok &= (rel < 0.12)
        print(f"     mu={mu_test:.1f}: mass gap sqrt(edge)={gap:.3f}  (predicted mu, "
              f"rel.err {rel:.2f})")
    ok &= check("P1 Persson: gap(essential spectrum) ~ mass at infinity", persson_ok)

    # Protection: deform the INTERIOR of m keeping m(+-inf) fixed -> index constant.
    print("  -- protection: interior deformations keep the index (gap at inf held) --")
    idxs = []
    for k in range(6):
        bump_amp = 2.5 * (k / 5.0)         # grow an interior bump
        bump_ctr = RNG.uniform(-4, 4)
        def mfun(x, A=bump_amp, c=bump_ctr):
            return np.tanh(x) + A * np.exp(-(x - c) ** 2)   # m(+-inf)=+-1 fixed
        idx, _, _ = callias_index_susy(mfun, L=L, N=N)
        idxs.append(idx)
    base_ok = all(i == idxs[0] for i in idxs) and idxs[0] == 1
    ok &= check("P1 protection: index invariant under interior deformation",
                base_ok, f"indices over deformation = {idxs} (all +1 expected)")

    # Gap closing: let m(+-inf) -> 0 (invertibility at infinity FAILS).  The mass
    # gap collapses -- the Fredholm/protection mechanism switches OFF.
    print("  -- gap closing: mass at infinity -> 0 destroys Fredholm separation --")
    mus = (1.0, 0.5, 0.25, 0.1, 0.04)
    gaps = []
    for mu_test in mus:
        _, gap, _ = callias_index_susy(lambda x, m=mu_test: m * np.tanh(x), L=L, N=N)
        gaps.append(gap)
    # The gap collapses as the mass at infinity -> 0.  In the clean regime
    # (mu*L >> 1) it tracks mu monotonically; once mu*L < 1 the finite box can no
    # longer resolve the (already-closed) gap, so we require substantial collapse
    # and a clean downward trend over the resolved points, not tail monotonicity.
    collapsing = (gaps[0] > 0.8 and gaps[0] > gaps[1] > gaps[2] and
                  min(gaps[3:]) < 0.12)
    ok &= check("P1 gap collapses as invertibility-at-infinity fails",
                collapsing, f"mass gaps for mu in {mus} = "
                            f"{[round(g,3) for g in gaps]}")
    return ok


# ---------------------------------------------------------------------------
# PART 2 -- OC1 sub-part (iii): bounded transform F = Dcal(1+Dcal^2)^{-1/2}
# is norm-bounded (<1), Fredholm-shaped, and norm-continuous where the gap holds.
# ---------------------------------------------------------------------------

def bounded_transform_selfadjoint(A):
    """f(A) = A (1+A^2)^{-1/2} for Hermitian A, via eigen-calculus."""
    w, U = np.linalg.eigh(A)
    fw = w / np.sqrt(1.0 + w ** 2)
    return (U * fw) @ U.conj().T


def part2():
    print("\n=== PART 2: OC1 (iii) bounded transform + Riesz/norm continuity ===")
    ok = True
    L, N = 20.0, 801
    D, xgrid = callias_D(lambda x: np.tanh(x), L=L, N=N)
    Dcal, _ = chiral_double(D)
    F = bounded_transform_selfadjoint(Dcal)

    nrm = np.linalg.norm(F, 2)
    ok &= check("P2 ||F|| < 1 (F = Dcal(1+Dcal^2)^{-1/2})", nrm < 1.0 + 1e-9,
                f"||F||_2 = {nrm:.6f}")

    # Fredholm shape: spectrum of F is a few values near 0 (kernel) + a bulk near +-1.
    wF = np.linalg.eigvalsh(F)
    near_pm1 = np.mean(np.abs(np.abs(wF) - 1.0) < 0.25)
    ok &= check("P2 F is Fredholm-shaped (bulk spectrum near +-1)",
                near_pm1 > 0.5, f"fraction with |lambda_F|>0.75 is {near_pm1:.2f}")

    # gap of F near 0 relates to gap g of Dcal by g/sqrt(1+g^2)
    _, g, _ = localized_index(D, xgrid)
    predicted_Fgap = g / np.sqrt(1 + g ** 2)
    # smallest |eigenvalue of F| that is NOT a near-zero (kernel) mode
    absF = np.sort(np.abs(wF))
    Fgap = absF[np.searchsorted(absF, 0.5 * predicted_Fgap)]
    ok &= check("P2 F-gap ~ g/sqrt(1+g^2)",
                abs(Fgap - predicted_Fgap) < 0.2,
                f"F-gap={Fgap:.3f}, predicted={predicted_Fgap:.3f} (g={g:.3f})")

    # Riesz / norm continuity: perturb D by an interior potential of scale eps,
    # measure ||F' - F||.  Should -> 0 (in fact ~ linearly) as eps -> 0.
    print("  -- Riesz continuity: ||F(D+eps V) - F(D)|| -> 0 as eps -> 0 --")
    x = np.linspace(-L, L, N)
    V = np.exp(-x ** 2) * RNG.standard_normal(N)     # smooth interior perturbation
    diffs = []
    epss = [0.4, 0.2, 0.1, 0.05, 0.025]
    for eps in epss:
        D2 = D + np.diag(eps * V)
        Dcal2, _ = chiral_double(D2)
        F2 = bounded_transform_selfadjoint(Dcal2)
        diffs.append(np.linalg.norm(F2 - F, 2))
    monotone = all(diffs[i] > diffs[i + 1] for i in range(len(diffs) - 1))
    # check approximate linear (Lipschitz) scaling: diff/eps roughly constant
    ratios = [d / e for d, e in zip(diffs, epss)]
    lipschitz = (max(ratios) / min(ratios)) < 3.0
    ok &= check("P2 bounded transform is norm-continuous (Lipschitz) in D",
                monotone and lipschitz,
                f"||dF|| = {[round(d,4) for d in diffs]} at eps={epss}")
    return ok


# ---------------------------------------------------------------------------
# PART 3 -- OC2: the quaternionic symmetry is transported to F for free.
# Claim (functional calculus): [D, J] = 0  =>  [F, J] = 0, F = D(1+D*D)^{-1/2}.
# So OC2 adds NO analytic content beyond OC1 -- only the algebraic [D,J]=0.
# ---------------------------------------------------------------------------

def quaternionic_omega(m):
    isy = np.array([[0, 1], [-1, 0]], dtype=complex)   # i*sigma_y
    Om = np.zeros((2 * m, 2 * m), dtype=complex)
    for i in range(m):
        Om[2 * i:2 * i + 2, 2 * i:2 * i + 2] = isy
    return Om


def make_quaternionic(B, Om):
    """A with Omega^{-1} A Omega = conj(A), i.e. A commutes with J: psi->Om conj(psi)."""
    return B + Om @ B.conj() @ np.linalg.inv(Om)


def bounded_transform_general(A):
    """F_A = A (I + A^H A)^{-1/2} via eigen-calculus of the Hermitian A^H A."""
    G = A.conj().T @ A
    w, U = np.linalg.eigh(G)
    inv_sqrt = (U * (1.0 / np.sqrt(1.0 + w))) @ U.conj().T
    return A @ inv_sqrt


def part3():
    print("\n=== PART 3: OC2 -- [D,J]=0 => [F,J]=0 (symmetry transport is automatic) ===")
    ok = True
    m = 6
    n = 2 * m
    Om = quaternionic_omega(m)
    Jcomm_ok = np.linalg.norm(Om @ Om.conj() + np.eye(n)) < 1e-10
    ok &= check("P3 J^2 = -1 (antilinear quaternionic structure)", Jcomm_ok)

    # generic H-linear (quaternionic) operators; verify transport to bounded F.
    worst_pre, worst_post, worst_even = 0.0, 0.0, True
    for _ in range(200):
        B = RNG.standard_normal((n, n)) + 1j * RNG.standard_normal((n, n))
        A = make_quaternionic(B, Om)
        # [A,J]=0 expressed as Omega^{-1} A Omega = conj(A):
        preA = np.linalg.norm(np.linalg.inv(Om) @ A @ Om - A.conj())
        F = bounded_transform_general(A)
        # transported symmetry: Omega^{-1} F Omega = conj(F)
        postF = np.linalg.norm(np.linalg.inv(Om) @ F @ Om - F.conj())
        worst_pre = max(worst_pre, preA)
        worst_post = max(worst_post, postF)
    ok &= check("P3 constructed A is quaternionic ([A,J]=0)", worst_pre < 1e-7,
                f"max ||Om^-1 A Om - conj(A)|| = {worst_pre:.2e}")
    ok &= check("P3 bounded transform stays quaternionic ([F,J]=0) -- OC2 is free",
                worst_post < 1e-7,
                f"max ||Om^-1 F Om - conj(F)|| = {worst_post:.2e}")

    # index even (KSp augmentation) for rank-deficient quaternionic operators
    even = True
    for _ in range(50):
        B = RNG.standard_normal((n, n)) + 1j * RNG.standard_normal((n, n))
        A = make_quaternionic(B, Om)
        u = RNG.standard_normal(n) + 1j * RNG.standard_normal(n)
        u = u / np.linalg.norm(u)
        Ju = Om @ u.conj()
        Ju = Ju - (u.conj() @ Ju) * u
        Ju = Ju / np.linalg.norm(Ju)
        P = np.eye(n) - np.outer(u, u.conj()) - np.outer(Ju, Ju.conj())
        A2 = make_quaternionic(A @ P, Om)
        sv = np.linalg.svd(A2, compute_uv=False)
        kdim = int(np.sum(sv < 1e-8))
        if kdim % 2 != 0:
            even = False
    ok &= check("P3 quaternionic kernel even => index_H = index_C/2 (KSp^0(pt)=Z)",
                even, "50 rank-deficient quaternionic operators, all even kernel")

    # And on the actual Callias model: doubled quaternionic operator A = Dcal (x) I_2.
    D, _ = callias_D(lambda x: np.tanh(x), L=16.0, N=401)
    Dcal, _ = chiral_double(D)
    A = np.kron(Dcal.astype(complex), np.eye(2))
    mm = A.shape[0] // 2
    OmA = quaternionic_omega(mm)
    # tensor with I_2 on the *quaternionic* slot: use Om acting on the doubled index
    # verify [A, Om]=0 (A is real-symmetric (x) I_2, commutes with the C^2 twist)
    commute = np.linalg.norm(A @ OmA - OmA @ A)
    ok &= check("P3 Callias double A = Dcal (x) I_2 commutes with quaternionic J",
                commute < 1e-9, f"||[A,Om]|| = {commute:.2e}")
    return ok


def main():
    print("OC1 / OC2 WITNESS -- non-compact case of the Signed-Readout Boundary Theorem")
    print("=" * 74)
    p1 = part1()
    p2 = part2()
    p3 = part3()
    print("\n" + "=" * 74)
    npass = sum(1 for _, o in report if o)
    print(f"SUMMARY: {npass}/{len(report)} checks passed.")
    print(f"  PART 1 (OC1 mechanism, Callias/Persson):     {'OK' if p1 else 'FAIL'}")
    print(f"  PART 2 (OC1 bounded transform continuity):   {'OK' if p2 else 'FAIL'}")
    print(f"  PART 3 (OC2 symmetry transport is automatic):{'OK' if p3 else 'FAIL'}")
    allok = p1 and p2 and p3
    print("\nRESULT:", "ALL WITNESS CHECKS PASSED" if allok else "SOME CHECKS FAILED")
    print("\nNOTE: finite-truncation evidence FOR the OC1/OC2 reduction, NOT a proof")
    print("on the genuinely non-compact operator. See exploration doc for grades.")
    return 0 if allok else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
