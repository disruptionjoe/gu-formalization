#!/usr/bin/env python3
r"""LEG 2D - Velo-Zwanziger FC-VZ-4: the 4D subprincipal-symbol / characteristic
analysis for the section-pulled Rarita-Schwinger (spin-3/2) sector on the round-S^4
GU model.

CONTEXT
-------
canon/no-go-class-relative-map.md (Velo-Zwanziger row, FC-VZ-4) and
explorations/cycle2-vz-actual-operator-e-block-certificate-2026-06-24.md.

The 4D principal-symbol VZ evasion (OQ3-V1/V2/V3) is held at CONDITIONALLY_RESOLVED.
The named overturn route is FC-VZ-4:

  "(4) II_s = s*(theta) (the extrinsic curvature / second fundamental form of the
   section embedding) sources an effective FIRST-ORDER term in the effective RS
   symbol S_R^{4D}, producing spacelike characteristics -- i.e. the 4D principal-
   symbol evasion is overturned at the next (subprincipal) order."

The two in-repo inputs FC-VZ-4 names already exist:
  (i)  the second fundamental form  II_s = s*(theta)  (a zeroth-order tensor datum);
  (ii) the round-S^4 Lichnerowicz lowest TT eigenvalue = 8/R^2 (a curvature scale).

WHAT THIS FILE ACTUALLY COMPUTES (all numeric, all cross-checked; W2-01 discipline)
-----------------------------------------------------------------------------------
BLOCK A. Cross-check the 8/R^2 input from first principles via the tensor-harmonic
   Laplacian ladder on S^n, lambda(s,L,n)=L(L+n-1)-s, with two independent anchors
   (scalar first eigenvalue = n; Killing-vector transverse mode = n-1).

BLOCK B. Free/GR-limit recovery + the decisive conceptual fact. Build explicit 4D
   Lorentzian gammas; verify the Dirac-type RS principal symbol is a Clifford module
   (c(xi)^2 = q I, det = q^8) so its characteristic variety is exactly the metric
   NULL CONE {q=0}. Then show the load-bearing PDE fact: the characteristic variety
   is a property of the PRINCIPAL (top-order) symbol, and a ZEROTH-ORDER term (a
   mass, or II_s) does NOT change the principal symbol -- so a naive zeroth-order
   II_s insertion cannot, by itself, create characteristics.

BLOCK C. The real VZ mechanism + the dichotomy that decides FC-VZ-4. After the
   gamma-trace constraint is eliminated (Schur complement with the constant E-block),
   the reduced RS symbol is  S_R = A_1(xi) - B(xi) E_0^{-1} C(xi). With E_0 constant
   the genuine top-order part is the degree-2 Schur symbol sigma_2(S_R) = -B_1 E_0^{-1} C_1.
   II_s enters B,C at zeroth order, hence contributes only the LOWER-degree pieces.
   THEREFORE:
     * if sigma_2(S_R) is NON-DEGENERATE (the Clifford-module / "entanglement
       identity" A S_R = q Id_R case): II_s is strictly subprincipal -> characteristic
       variety = {q=0}, II_s-independent. Causal. (demonstrated)
     * if sigma_2(S_R) is DEGENERATE: the II_s-dependent lower-degree terms become
       leading and CAN produce spacelike characteristics. (demonstrated, with an
       explicit spacelike characteristic)
   The discriminator is exactly whether the entanglement identity holds = the actual
   first-order 0/1 coefficients (a,b,lambda_d) and the constant E-block of D_GU.

BLOCK D. The round-S^4 refinement (and its limit). On round S^4 the point-isotropy
   group SO(4) has NO invariant in the symmetric-traceless rank-2 representation, so
   a homogeneous II_s is FORCED isotropic (~ g) -- verified by group-averaging. This
   makes any II_s contribution covariant; but covariance is shown to be NECESSARY-
   NOT-SUFFICIENT (a covariant but degenerate Schur term still admits a spacelike
   root), so round-S^4 isotropy does not by itself decide causality.

HONEST SCOPE / VERDICT (read before quoting anything)
-----------------------------------------------------
ESTABLISHED: (A) lowest-TT eigenvalue = 8/R^2; (B) free/GR-limit characteristic
   variety = metric null cone, and II_s is a zeroth-order (subprincipal) datum.
NOT CLOSED: FC-VZ-4 is NOT closed and the VZ verdict is NOT upgraded. Whether II_s
   tilts the reduced RS cone is governed by the DEGENERACY of the top-order Schur
   symbol sigma_2(S_R) = -B_1 E_0^{-1} C_1 (i.e. whether the entanglement identity
   A S_R = q Id_R holds). That is fixed by the actual D_GU 0/1 first-order
   coefficients (a,b,lambda_d) + constant E-block, which are NOT pinned without the
   GU RS ACTION ON Y^14 -- the SAME missing object as FC-VZ-1.
=> BLOCKED on: the GU RS action on Y^14 (equivalently the pinned 0/1-sector
   coefficients a,b,lambda_d and the II_s off-diagonal insertions B_0,C_0). The
   4D leg stays CONDITIONALLY_RESOLVED; this file confirms causality + GR limit in
   the symmetric model and pins the exact missing object, nothing more.
"""

from __future__ import annotations

import numpy as np

TOL = 1e-9
RNG = np.random.default_rng(20260627)


# ======================================================================
# BLOCK A -- cross-check the round-S^4 input  lambda_TT^lowest = 8/R^2
# ======================================================================
def tensor_harmonic_eigenvalue(s: int, L: int, n: int) -> int:
    """Laplacian (rough/Bochner, units 1/R^2) on rank-s TT symmetric tensor
    harmonics of level L on S^n:  lambda = L(L+n-1) - s,  valid for L >= max(s,1).
    s=0 scalar, s=1 transverse vector, s=2 TT symmetric 2-tensor."""
    return L * (L + n - 1) - s


def block_A():
    print("=" * 78)
    print("BLOCK A  --  round-S^4 TT Lichnerowicz/Bochner lowest eigenvalue = 8/R^2")
    print("=" * 78)
    n = 4  # S^4

    lam_tt_lowest = tensor_harmonic_eigenvalue(2, 2, n)  # s=2, lowest level L=2
    print(f"  lambda_TT^lowest (s=2, L=2, n=4) = L(L+n-1)-2 = {lam_tt_lowest} / R^2")
    # closed form at L=2:  2(n+1)-2 = 2n  -> 8 for n=4
    assert lam_tt_lowest == 2 * n == 8, lam_tt_lowest

    # ---- CROSS-CHECK A1: scalar (s=0) first nonzero eigenvalue = n ----
    lam_scalar_1 = tensor_harmonic_eigenvalue(0, 1, n)
    print(f"  [A1] scalar first eigenvalue lambda(s=0,L=1) = {lam_scalar_1} "
          f"(known: first Laplace eigenvalue on S^n is n={n})")
    assert lam_scalar_1 == n

    # ---- CROSS-CHECK A2: transverse vector lowest = Killing-vector value n-1 ----
    # Killing vectors xi: Delta_Bochner xi = Ric.xi = (n-1)/R^2 xi  (lowest L=1).
    lam_vec_1 = tensor_harmonic_eigenvalue(1, 1, n)
    print(f"  [A2] transverse-vector lowest lambda(s=1,L=1) = {lam_vec_1} "
          f"(known Killing value n-1={n - 1})")
    assert lam_vec_1 == n - 1

    # ---- CROSS-CHECK A3: the -s curvature-shift pattern is self-consistent ----
    print("  [A3] harmonic ladder lambda(s,L,n=4)=L(L+3)-s :")
    for s in (0, 1, 2):
        row = [tensor_harmonic_eigenvalue(s, L, n) for L in range(max(s, 1), 5)]
        print(f"        s={s}:  {row}")
    base = [tensor_harmonic_eigenvalue(0, L, n) for L in range(2, 5)]
    for s in (1, 2):
        shifted = [tensor_harmonic_eigenvalue(s, L, n) for L in range(2, 5)]
        assert all(b - sh == s for b, sh in zip(base, shifted))
    print("  RESULT(A): lowest TT eigenvalue = 8/R^2 CONFIRMED "
          "(anchored by scalar=n and Killing=n-1).")
    return lam_tt_lowest


# ======================================================================
# explicit 4D Lorentzian Clifford algebra  {g^a,g^b}=2 eta^{ab}
# mostly-minus signature matching the Weyl gammas below.
# ======================================================================
ETA = np.diag([1.0, -1.0, -1.0, -1.0])
ETA_INV = np.linalg.inv(ETA)


def dirac_gammas():
    """4x4 Dirac gammas, Weyl basis, signature (+,-,-,-)."""
    I2 = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    sig = [I2, s1, s2, s3]            # sigma^mu
    sigbar = [I2, -s1, -s2, -s3]      # bar-sigma^mu
    g = []
    for mu in range(4):
        top = np.kron(np.array([[0, 1], [0, 0]]), sig[mu])
        bot = np.kron(np.array([[0, 0], [1, 0]]), sigbar[mu])
        g.append(top + bot)
    return g


def cliff(g, xi_low):
    """c(xi) = g^a xi_a."""
    return sum(g[a] * xi_low[a] for a in range(4))


def q_of(xi_low):
    """q = g^{-1}(xi,xi) = eta^{ab} xi_a xi_b."""
    return float(xi_low @ ETA_INV @ xi_low)


def sigma_min(M):
    return float(np.linalg.svd(M, compute_uv=False)[-1])


def block_B(g):
    print("\n" + "=" * 78)
    print("BLOCK B  --  free/GR-limit: Clifford-module RS symbol; characteristic")
    print("            variety = metric NULL CONE; II_s is a zeroth-order datum")
    print("=" * 78)

    # Clifford {g^a,g^b}=2 eta^{ab}
    for a in range(4):
        for b in range(4):
            anti = g[a] @ g[b] + g[b] @ g[a]
            assert np.allclose(anti, 2 * ETA[a, b] * np.eye(4), atol=TOL)
    print("  [B0] {g^a,g^b} = 2 eta^{ab} I : PASS")

    # c(xi)^2 = q I, det c = q^2
    maxerr = 0.0
    for _ in range(2000):
        xi = RNG.normal(size=4)
        c = cliff(g, xi)
        q = q_of(xi)
        maxerr = max(maxerr, np.max(np.abs(c @ c - q * np.eye(4))))
        assert abs(np.linalg.det(c) - q ** 2) < 1e-7
    print(f"  [B1] c(xi)^2 = q I (max err {maxerr:.1e}); det c(xi) = q^2 : PASS")

    # Dirac-type spinor-vector symbol D = I_vec (x) c(xi): D^2=qI_16, det=q^8
    I4 = np.eye(4, dtype=complex)
    for _ in range(500):
        xi = RNG.normal(size=4)
        q = q_of(xi)
        D = np.kron(I4, cliff(g, xi))
        assert np.allclose(D @ D, q * np.eye(16), atol=1e-7)
        assert abs(np.linalg.det(D) - q ** 8) <= 1e-3 * (abs(q) ** 8 + 1)
    print("  [B2] D=I_vec(x)c(xi): D^2 = q I_16, det D = q^8 : PASS")

    # characteristic variety via singular values (robust; det=q^8 is numerically
    # hopeless). c is a non-normal Clifford module: c^{-1}=c/q, which forces the
    # EXACT relation  sigma_min(c).sigma_max(c) = |q|.  Hence c is singular
    # (sigma_min=0) iff q=0 -> characteristic variety = null cone, no spacelike chars.
    worst_rel = 0.0
    spacelike = 0
    for _ in range(20000):
        xi = RNG.normal(size=4)
        xi /= np.linalg.norm(xi)            # |xi|_Eucl = 1 => q in [-1,1]
        q = q_of(xi)
        sv = np.linalg.svd(cliff(g, xi), compute_uv=False)
        smin, smax = float(sv[-1]), float(sv[0])
        worst_rel = max(worst_rel, abs(smin * smax - abs(q)))
        if smin < 1e-6 and abs(q) > 1e-3:     # |q|=smin*smax, smax~O(1) -> impossible
            spacelike += 1
    print(f"  [B3] sigma_min.sigma_max = |q| (max dev {worst_rel:.1e}); "
          f"spacelike/complex characteristics = {spacelike}")
    assert worst_rel < 1e-6 and spacelike == 0

    # [B4] DECISIVE conceptual fact: a zeroth-order term does NOT change the PRINCIPAL
    # symbol, hence not the characteristic variety. principal symbol = top homogeneous
    # part = lim_{lambda->inf} M(lambda xi)/lambda. Demonstrate for M = c(xi)+ m I.
    m = 0.7
    xhat = RNG.normal(size=4)
    xhat /= np.linalg.norm(xhat)
    princ = None
    for lam in (1e3, 1e6, 1e9):
        princ = (cliff(g, lam * xhat) + m * np.eye(4)) / lam
    err = np.max(np.abs(princ - cliff(g, xhat)))
    print(f"  [B4] principal_symbol(c(xi)+m I) -> c(xi) as lambda->inf "
          f"(residual {err:.1e}): the zeroth-order m (model for II_s) drops out.")
    assert err < 1e-6
    # the FULL symbol c(xi)+mI is singular at q=m^2 (q>0), but that is NOT a
    # characteristic -- characteristics use the principal symbol c(xi), singular only
    # at q=0. Confirm the spurious full-symbol zero sits at q=m^2:
    # pick xi with q=m^2 and c(xi) eigen -m: e.g. timelike xi0 with q=m^2.
    print("  RESULT(B): char. variety = {q=0} (null cone); II_s, being zeroth order,")
    print("             cannot enter the principal symbol of the UNconstrained operator.")


# ======================================================================
# BLOCK C -- the real VZ mechanism (constraint Schur reduction) + the dichotomy
# ======================================================================
def block_C(g):
    print("\n" + "=" * 78)
    print("BLOCK C  --  VZ mechanism: constraint Schur reduction. Whether II_s tilts")
    print("            the reduced cone is governed by DEGENERACY of sigma_2(S_R).")
    print("=" * 78)
    I4 = np.eye(4, dtype=complex)

    # The reduced RS symbol after eliminating the gamma-trace constraint with a
    # CONSTANT E-block E_0 is  S_R(xi) = A_1(xi) - B(xi) E_0^{-1} C(xi),  with
    #   A_1, B_1, C_1  first order in xi  (the genuine derivative couplings),
    #   B_0, C_0       zeroth order, PROPORTIONAL to II_s (the subprincipal insert).
    # With E_0 constant, the degree-2 (top) part is sigma_2 = -B_1 E_0^{-1} C_1;
    # II_s sits only in the degree-1 and degree-0 parts.  We exhibit both regimes.

    def build_SR(xi, ii_scale, B0, C0, degenerate):
        c = cliff(g, xi)
        E0inv = np.eye(4, dtype=complex)           # E_0 = I (constant E-block model)
        if not degenerate:
            B1 = c.copy(); C1 = c.copy()           # non-degenerate: sigma_2 = -c^2 = -qI
        else:
            P = np.diag([1, 1, 0, 0]).astype(complex)  # rank-deficient -> sigma_2 degenerate
            B1 = P @ c; C1 = c @ P
        B = B1 + ii_scale * B0
        C = C1 + ii_scale * C0
        A1 = c.copy()
        SR = A1 - B @ E0inv @ C
        # decompose by degree in xi for inspection:
        sig2 = -B1 @ E0inv @ C1                     # degree 2
        return SR, sig2

    # ---------- regime 1: NON-DEGENERATE sigma_2 (Clifford-module / GU-claimed) -----
    print("  [C1] NON-DEGENERATE sigma_2 (entanglement identity A S_R = q Id holds):")
    B0 = RNG.normal(size=(4, 4)) + 1j * RNG.normal(size=(4, 4))  # arbitrary II_s insert
    C0 = RNG.normal(size=(4, 4)) + 1j * RNG.normal(size=(4, 4))
    # verify sigma_2 = -q I (II_s-INDEPENDENT) and equals top homogeneous part
    okq = True
    for _ in range(300):
        xi = RNG.normal(size=4); q = q_of(xi)
        _, sig2 = build_SR(xi, 0.0, B0, C0, degenerate=False)
        if not np.allclose(sig2, -q * np.eye(4), atol=1e-7):
            okq = False
    print(f"       sigma_2(S_R) = -q I  (II_s-independent) : {'PASS' if okq else 'FAIL'}")
    assert okq
    # characteristic variety from the PRINCIPAL (degree-2) symbol: extract via lambda
    xhat = RNG.normal(size=4); xhat /= np.linalg.norm(xhat)
    lam = 1e7
    SR_big, _ = build_SR(lam * xhat, 1.0, B0, C0, degenerate=False)
    princ = SR_big / lam ** 2                       # -> sigma_2(xhat)
    qhat = q_of(xhat)
    err = np.max(np.abs(princ - (-qhat) * np.eye(4)))
    print(f"       principal symbol of S_R (incl. II_s) -> -q I (residual {err:.1e}):")
    print(f"       => char. variety = {{q=0}}, II_s strictly subprincipal. CAUSAL.")
    assert err < 1e-4

    # ---------- regime 2: DEGENERATE sigma_2 -> II_s becomes leading -----------------
    print("  [C2] DEGENERATE sigma_2 (entanglement identity FAILS): II_s leading ->")
    print("       spacelike characteristics become possible:")
    # use an ANISOTROPIC II_s insert with a fixed direction so the leading (now
    # II_s-dependent) part has a preferred direction.
    ndir = np.array([0.0, 1.0, 0.0, 0.0])
    B0a = cliff(g, ndir); C0a = cliff(g, ndir)
    # scan for a real spacelike characteristic (sigma_min ~ 0 with q>0):
    found = 0; example = None
    for _ in range(40000):
        xi = RNG.normal(size=4); xi /= np.linalg.norm(xi)
        SR, _ = build_SR(xi, 1.0, B0a, C0a, degenerate=True)
        if sigma_min(SR) < 1e-3 and q_of(xi) > 1e-2:
            found += 1
            if example is None:
                example = (xi.copy(), q_of(xi), sigma_min(SR))
    print(f"       spacelike characteristics found = {found > 0}; "
          f"example q={example[1]:.3f}>0 (sigma_min={example[2]:.1e})" if example
          else "       (none found)")
    assert found > 0, "degenerate-sigma2 regime must admit a spacelike characteristic"
    print("  RESULT(C): the FC-VZ-4 outcome is decided by DEGENERACY of sigma_2(S_R)")
    print("             = whether A S_R = q Id_R (the entanglement identity) holds")
    print("             = the actual D_GU 0/1 coefficients (a,b,lambda_d) + E-block.")


# ======================================================================
# BLOCK D -- round-S^4 forces II_s isotropic; isotropy is necessary-not-sufficient
# ======================================================================
def _expm(A):
    A = np.asarray(A, dtype=complex)
    norm = np.max(np.sum(np.abs(A), axis=1))
    s = max(0, int(np.ceil(np.log2(norm + 1e-12))))
    A = A / (2 ** s)
    E = np.eye(A.shape[0], dtype=complex)
    term = np.eye(A.shape[0], dtype=complex)
    for k in range(1, 30):
        term = term @ A / k
        E = E + term
    for _ in range(s):
        E = E @ E
    return E.real if np.allclose(E.imag, 0) else E


def random_SO4():
    """Haar-uniform SO(4) via QR of a Gaussian matrix (sign/det normalized)."""
    Z = RNG.normal(size=(4, 4))
    Q, Rm = np.linalg.qr(Z)
    Q = Q @ np.diag(np.sign(np.diag(Rm)))   # fix QR sign ambiguity -> Haar on O(4)
    if np.linalg.det(Q) < 0:                 # restrict to SO(4)
        Q[:, 0] = -Q[:, 0]
    return Q


def block_D():
    print("\n" + "=" * 78)
    print("BLOCK D  --  round-S^4 forces II_s ISOTROPIC (SO(4) isotropy irreducible);")
    print("            isotropy is NECESSARY-NOT-SUFFICIENT for causality")
    print("=" * 78)
    # Sym^2(R^4) = trace(1) + sym-traceless(9). SO(4) acts irreducibly (no invariant)
    # on the 9. Group-average a random sym-traceless tensor -> 0.
    M = RNG.normal(size=(4, 4)); M = 0.5 * (M + M.T)
    M = M - np.trace(M) / 4 * np.eye(4)
    avg = np.zeros((4, 4)); N = 40000
    for _ in range(N):
        R = random_SO4(); avg += R @ M @ R.T
    avg /= N
    rel = np.linalg.norm(avg) / np.linalg.norm(M)
    print(f"  [D1] SO(4)-average of random sym-traceless 2-tensor: "
          f"||avg||/||M||={rel:.2e}  -> 0 (no invariant; ~1/sqrt(N) Monte Carlo)")
    assert rel < 3e-2
    # trace part (~delta) is invariant:
    avg_tr = np.zeros((4, 4))
    for _ in range(200):
        R = random_SO4(); avg_tr += R @ np.eye(4) @ R.T
    avg_tr /= 200
    print(f"  [D2] SO(4)-average of delta: ||avg-delta||={np.linalg.norm(avg_tr - np.eye(4)):.1e}"
          f"  (delta invariant) => homogeneous II_s ~ g.")
    assert np.linalg.norm(avg_tr - np.eye(4)) < 1e-9
    # necessary-not-sufficient: a COVARIANT but degenerate Schur term still has a
    # spacelike root.  S_R = c(xi) - beta c(xi)^2 = c(xi) - beta q I  (covariant);
    # eigenvalues +-sqrt(q) - beta q  -> det 0 also at q = 1/beta^2 > 0 (spacelike).
    g = dirac_gammas(); beta = 0.5
    q_space = 1.0 / beta ** 2
    # build a spacelike xi with q = q_space: xi=(t,x,0,0), q=t^2-x^2; pick t,x
    t = np.sqrt(q_space + 1.0); x = 1.0
    xi = np.array([t, x, 0.0, 0.0]); assert abs(q_of(xi) - q_space) < 1e-9
    SR = cliff(g, xi) - beta * (cliff(g, xi) @ cliff(g, xi))
    print(f"  [D3] covariant-but-degenerate Schur term: spacelike root at q=1/beta^2="
          f"{q_space:.2f}>0, sigma_min(S_R)={sigma_min(SR):.1e}")
    assert sigma_min(SR) < 1e-6
    print("  RESULT(D): round-S^4 => II_s isotropic (~g); but covariance alone does")
    print("             NOT guarantee causality (degenerate covariant Schur term can")
    print("             still be spacelike). The decider is still sigma_2 degeneracy.")


def main():
    block_A()
    g = dirac_gammas()
    block_B(g)
    block_C(g)
    block_D()

    import textwrap
    print("\n" + "=" * 78)
    print("SYNTHESIS -- FC-VZ-4 round-S^4 model leg")
    print("=" * 78)
    print(textwrap.dedent("""
      ESTABLISHED (numerically cross-checked here):
        (A) round-S^4 lowest TT Lichnerowicz/Bochner eigenvalue = 8/R^2, anchored by
            scalar=n and Killing=n-1.
        (B) free/GR-limit characteristic variety of the Dirac-type RS symbol = metric
            null cone {q=0}; det=q^8; sigma_min.sigma_max=|q|; no spacelike chars.
            II_s = s*(theta) is a ZEROTH-ORDER datum and cannot enter the principal
            symbol of the unconstrained operator.

      THE DECIDING DICHOTOMY (Block C):
        After eliminating the gamma-trace constraint, the reduced RS symbol is
        S_R = A_1 - B E_0^{-1} C with constant E_0. Its top-order (degree-2) part is
        sigma_2 = -B_1 E_0^{-1} C_1; II_s sits only in the lower-degree parts.
          * sigma_2 non-degenerate (entanglement identity A S_R = q Id_R holds):
            II_s strictly subprincipal -> cone = {q=0}, causal.
          * sigma_2 degenerate: II_s becomes leading -> spacelike characteristics
            possible (explicit example exhibited).

      ROUND-S^4 REFINEMENT (Block D): SO(4) isotropy forces II_s ~ g, so any II_s
        contribution is covariant -- but covariance is NECESSARY-NOT-SUFFICIENT (a
        covariant-but-degenerate Schur term still has a spacelike root at q=1/beta^2).

      OPEN / BLOCKED -- DO NOT read FC-VZ-4 as closed:
        Whether GU is in the non-degenerate (causal) or degenerate (acausal) regime is
        fixed by whether the entanglement identity holds = the actual D_GU 0/1
        first-order coefficients (a,b,lambda_d) + the constant E-block + the II_s
        off-diagonal inserts (B_0,C_0). NONE is pinned without the GU RS ACTION ON
        Y^14 -- the SAME missing object as FC-VZ-1.
        => BLOCKED on: the GU RS action on Y^14 (pinned 0/1 coefficients + II_s
           inserts). The 4D VZ leg stays CONDITIONALLY_RESOLVED. This file confirms
           causality + GR limit in the symmetric model and pins the exact missing
           object; it does not upgrade the verdict.
    """))
    print("=" * 78)
    print("ALL ASSERTIONS PASSED.")


if __name__ == "__main__":
    main()
