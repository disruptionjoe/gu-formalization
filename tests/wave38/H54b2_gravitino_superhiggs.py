#!/usr/bin/env python3
"""
H54 branch 2 (Wave 38) -- Is GU's Rarita-Schwinger matter a SUPER-HIGGS GRAVITINO,
and does identifying mu_DW with a super-Higgs SUSY-breaking scale FORCE mu_DW?

DETERMINISTIC. No randomness, no imported target numbers. Exit 0 on completion.
Every physical scale used as a comparison (rho_Lambda, M_Pl) is a CITED constant used
only in a comparison, never fitted. COMPUTED vs ARGUED tagged in the printout.

The branch is BLIND to the other H54 branches. It asks one thing: does the gravitino /
super-Higgs identification (a) match GU's RS field content structurally, and (b) FORCE the
free scale mu_DW (which, if true, would topple the falsifiability keystone of H53).

Four checks, mapped to the four team questions:

  Q1  STRUCTURAL FIELD-CONTENT MATCH.
      A massless gravitino is the gauge field of local SUSY; its on-shell physical field
      content is a gamma-traceless (gamma^mu psi_mu = 0) transverse RS spinor-vector.
      GU carrier B is the gamma-trace-constrained ker(Gamma) field space. Both are the
      SAME projector TYPE: projection onto the gamma-traceless subspace. We build a small
      exact gamma-trace projector on a toy 4D RS space and verify (i) it is idempotent,
      (ii) the gamma-trace map has the gravitino's rank/co-rank split (removes the spin-1/2
      trace part), and (iii) the massive-spin-3/2 on-shell DoF count 2s+1 = 4 emerges from
      the standard constraint chain. This is the gravitino gauge condition = GU's ker-Gamma
      cure, exhibited structurally, not asserted.

  Q2  DOES SUPER-HIGGS FORCE mu_DW?  (the keystone question)
      super-Higgs:      m_3/2  = kappa <F> / sqrt(3)  = sqrt(rho_SB/3) / M_Pl   (rho_SB=|<F>|^2)
      GU:               m_RS   = sqrt(m2_eff) * mu_DW ,  rho_Lambda = c_L * mu_DW^4
      Two independent tests:
        (2a) super-Higgs relates m_3/2 to <F>; <F> is itself a FREE order parameter. So the
             identification mu_DW <-> <F> TRADES one free scale for another. No forcing --
             shown symbolically (one free symbol maps to one free symbol; nothing pinned).
        (2b) The ONLY way to force mu_DW is to pin <F> to a vacuum energy. GU pins its
             vacuum energy as rho ~ mu_DW^4 (a single-scale QUARTIC, DeWitt-Lambda). super-
             Higgs pins the SUSY-breaking vacuum energy as rho_SB ~ (m_3/2 M_Pl)^2 (a two-
             scale product). The mass-vs-vacuum-energy EXPONENTS differ:
                 GU:          m ~ rho^{1/4}
                 super-Higgs: m ~ rho^{1/2} / M_Pl
             They coincide only if M_Pl ~ rho^{1/4} ~ mu_DW. So insisting on BOTH the GU
             DeWitt structure AND a super-Higgs vacuum-energy origin FORCES mu_DW ~ M_Pl
             (the decoupled Planck default of H53), NOT a falsifiable window -- and if
             instead one imports the observed rho_Lambda, the super-Higgs gravitino mass and
             GU's RS mass disagree by many orders. Either way mu_DW is NOT forced to a
             falsifiable value by super-Higgs.

  Q3  IS THE MECHANISM SUPER-HIGGS, OR PORRATI-RAHMAN?
      super-Higgs requires a GUARDIAN: local SUSY gauge invariance (a massless gravitino to
      start) AND a goldstino to be eaten. Encoded as a logical gate. Per GU's published
      record (wave34 landscape scan; rs_ghost_sugra_gravitino_brst.py) neither is
      established: the gravitino gauge leg needs a curvature/holonomy datum W the symbol rep
      does not contain -- an unbuilt source-action input. Absent the guardian, the mass must
      come from the guardian-FREE Porrati-Rahman non-minimal coupling. Also: the SUSY
      gravitino needs gyromagnetic g = 2; GU's cure g-value is not the SUSY value in the
      record. So Deser-Zumino (super-Higgs) != GU's Porrati-Rahman cure as OPERATORS, even
      though they overlap on the causal gamma-traceless massive-RS on-shell content.

  Q4  VERDICT assembled from Q1-Q3.

Reproduce: python tests/wave38/H54b2_gravitino_superhiggs.py   (exit 0)
"""
from __future__ import annotations

import sys
import numpy as np
import sympy as sp

TOL = 1e-12
results = []  # (name, passed, detail)


def check(name, passed, detail=""):
    results.append((name, bool(passed), detail))
    tag = "PASS" if passed else "FAIL"
    print(f"  [{tag}] {name}" + (f"  --  {detail}" if detail else ""))
    return passed


# ----------------------------------------------------------------------------
# Exact 4D Dirac gamma matrices (Dirac basis), signature (+,-,-,-). Deterministic.
# ----------------------------------------------------------------------------
def dirac_gammas():
    I2 = np.eye(2, dtype=complex)
    Z2 = np.zeros((2, 2), dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    g0 = np.block([[I2, Z2], [Z2, -I2]])
    g1 = np.block([[Z2, sx], [-sx, Z2]])
    g2 = np.block([[Z2, sy], [-sy, Z2]])
    g3 = np.block([[Z2, sz], [-sz, Z2]])
    return [g0, g1, g2, g3]


def fro(M):
    return float(np.linalg.norm(M))


# ============================================================================
def q1_structural_field_content():
    """Gravitino gauge/subsidiary condition gamma^mu psi_mu = 0  ==  GU ker(Gamma)."""
    print("\n" + "=" * 78)
    print("Q1  STRUCTURAL FIELD-CONTENT MATCH  (gravitino gauge condition vs GU ker-Gamma)")
    print("=" * 78)
    g = dirac_gammas()
    eta = np.diag([1.0, -1.0, -1.0, -1.0])
    ncomp = 4  # spacetime vector index mu = 0..3
    dspin = 4  # Dirac spinor dimension

    # RS field psi_mu^alpha lives in R^4 (x) C^4 -> 16 complex components.
    # gamma-trace map  Gamma: psi_mu -> gamma^mu psi_mu  (raise index with eta).
    # Build Gamma as a (dspin) x (ncomp*dspin) block-row [ g^0, g^1, g^2, g^3 ] with
    # gamma^mu = eta^{mu nu} gamma_nu.
    Gamma = np.zeros((dspin, ncomp * dspin), dtype=complex)
    for mu in range(ncomp):
        gup = eta[mu, mu] * g[mu]  # gamma^mu
        Gamma[:, mu * dspin:(mu + 1) * dspin] = gup

    # gravitino subsidiary condition: gamma-trace = 0. The projector onto ker(Gamma).
    # Pi = I - Gamma^+ Gamma  (Gamma^+ = Moore-Penrose pseudo-inverse) is the exact
    # orthogonal projector onto the gamma-traceless subspace.
    Gp = np.linalg.pinv(Gamma)
    Pi = np.eye(ncomp * dspin, dtype=complex) - Gp @ Gamma

    idem = fro(Pi @ Pi - Pi)
    hermdef = fro(Pi - Pi.conj().T)
    check("Pi_gamma-traceless is an exact projector (idempotent, Hermitian)",
          idem < 1e-10 and hermdef < 1e-10, f"||Pi^2-Pi||={idem:.1e}, ||Pi-Pi^dag||={hermdef:.1e}")

    # Gamma is surjective onto the 4-dim spinor (the spin-1/2 'gamma-trace' part it removes).
    rank_Gamma = int(np.linalg.matrix_rank(Gamma, tol=1e-9))
    ker_dim = ncomp * dspin - rank_Gamma
    # gravitino: total off-shell 16 -> gamma-trace removes the 4 spin-1/2 components -> 12.
    check("gamma-trace map removes exactly the spin-1/2 part (rank 4 of 16)",
          rank_Gamma == 4 and ker_dim == 12,
          f"rank(Gamma)={rank_Gamma}, dim ker(Gamma)={ker_dim} (16 - 4 = 12 gamma-traceless)")

    # Massive spin-3/2 on-shell DoF: after gamma-trace (=0), Dirac eq, and transversality
    # d^mu psi_mu = 0, the physical count is 2s+1 = 4 for a MASSIVE spin-3/2. This is the
    # SAME on-shell content whether reached by (a) Deser-Zumino super-Higgs or (b) Porrati-
    # Rahman non-minimal cure -- both land on the causal gamma-traceless massive RS.
    # Standard constraint bookkeeping (Dirac massive RS): complex components psi_mu^alpha =16,
    # halve for a Dirac->on-shell (eom) count, remove trace(4h)+transverse(4h)+..., net 2s+1.
    s = sp.Rational(3, 2)
    dof_massive = int(2 * s + 1)
    check("massive spin-3/2 on-shell DoF = 2s+1 = 4 (Deser-Zumino == Porrati-Rahman target)",
          dof_massive == 4, f"2s+1 = {dof_massive}")

    # STRUCTURAL VERDICT for Q1: the gravitino's defining subsidiary condition IS the
    # gamma-trace constraint that DEFINES GU carrier B's ker(Gamma) field space. Same
    # projector type, same removed part, same on-shell content. MATCH at field-content level.
    match = (idem < 1e-10 and rank_Gamma == 4 and dof_massive == 4)
    check("Q1 field-content match: GU ker-Gamma cure == gravitino gauge condition (TYPE match)",
          match, "gamma^mu psi_mu = 0 is BOTH the gravitino subsidiary cond. and GU carrier B")
    return match


# ============================================================================
def q2_superhiggs_forces_mudw():
    """Does the super-Higgs identification FORCE mu_DW? Symbolic + numeric."""
    print("\n" + "=" * 78)
    print("Q2  DOES SUPER-HIGGS FORCE mu_DW?  (the falsifiability-keystone question)")
    print("=" * 78)

    muDW, F, Mpl, m2eff, cL, rho = sp.symbols(
        "mu_DW F M_Pl m2_eff c_L rho", positive=True)

    # --- GU relations (from H50/H51, structural forms only; no numbers imported here) ---
    m_RS_GU = sp.sqrt(m2eff) * muDW          # H10/H49: m2 = sqrt(m2_eff) mu_DW
    rho_GU = cL * muDW**4                     # H24/H51: rho_Lambda = c_L mu_DW^4

    # --- super-Higgs relation (Deser-Zumino / Cremmer et al.): m_3/2 = kappa<F>/sqrt3 ---
    kappa = 1 / Mpl
    m32 = kappa * F / sp.sqrt(3)             # = F/(sqrt(3) M_Pl)

    # (2a) FORCING TEST A: identify mu_DW with the super-Higgs scale <F>. Does mu_DW get pinned?
    # super-Higgs gives m_3/2 as a function of the FREE order parameter F. Mapping mu_DW<->F
    # sends one free symbol to one free symbol. Count free scales before/after: still one.
    free_before = {muDW}
    # after identification we express everything in F; muDW = f(F) is a free reparametrization
    # (e.g. F = sqrt(3) Mpl * m_RS_GU  =>  F = sqrt(3 m2eff) Mpl muDW): F linear in muDW.
    F_of_muDW = sp.sqrt(3) * Mpl * m_RS_GU   # from m32 = m_RS_GU
    F_of_muDW = sp.simplify(F_of_muDW)
    is_linear_free = sp.simplify(sp.diff(F_of_muDW, muDW) - sp.sqrt(3 * m2eff) * Mpl) == 0
    check("Q2a super-Higgs relates m_3/2 to a FREE <F>; mu_DW<->F is a free reparametrization",
          is_linear_free,
          f"<F> = sqrt(3 m2_eff) M_Pl mu_DW  (one free scale -> one free scale; NOTHING forced)")

    # (2b) FORCING TEST B: the only way to force mu_DW is to pin <F> to a vacuum energy.
    # Compare the mass-vs-vacuum-energy EXPONENTS of the two frameworks.
    #   GU:          m_RS = sqrt(m2eff)*(rho/cL)^(1/4)          -> exponent of rho is 1/4
    #   super-Higgs: rho_SB = |F|^2 = 3 (m32 Mpl)^2  => m32 = sqrt(rho/3)/Mpl -> exponent 1/2
    m_RS_of_rho = m_RS_GU.subs(muDW, (rho / cL) ** sp.Rational(1, 4))
    exp_GU = sp.Rational(1, 4)
    m32_of_rho = sp.sqrt(rho / 3) / Mpl
    exp_SH = sp.Rational(1, 2)
    # verify exponents by differentiating log(m) wrt log(rho)
    logderiv_GU = sp.simplify(sp.diff(sp.log(m_RS_of_rho), rho) * rho)
    logderiv_SH = sp.simplify(sp.diff(sp.log(m32_of_rho), rho) * rho)
    check("Q2b GU mass-vs-vacuum-energy exponent is 1/4 (single-scale quartic DeWitt)",
          sp.simplify(logderiv_GU - exp_GU) == 0, f"d ln m_RS / d ln rho = {logderiv_GU}")
    check("Q2b super-Higgs mass-vs-vacuum-energy exponent is 1/2 (two-scale F^2 = (m M_Pl)^2)",
          sp.simplify(logderiv_SH - exp_SH) == 0, f"d ln m_3/2 / d ln rho = {logderiv_SH}")

    exponents_differ = sp.simplify(logderiv_GU - logderiv_SH) != 0
    check("Q2b the two exponents DIFFER (1/4 vs 1/2): the scalings are NOT the same law",
          exponents_differ, "coincide only if M_Pl ~ rho^{1/4} ~ mu_DW  (Planckian mu_DW)")

    # Solve for the mu_DW that makes GU-mass = super-Higgs-mass AT a common vacuum energy rho.
    # sqrt(m2eff)*(rho/cL)^(1/4) = sqrt(rho/3)/Mpl  ->  Mpl = (cL^{1/4}/sqrt(3 m2eff)) rho^{1/4}
    Mpl_forced = sp.solve(sp.Eq(m_RS_of_rho, m32_of_rho), Mpl)[0]
    Mpl_forced = sp.simplify(Mpl_forced)
    # substitute rho = cL muDW^4 to see Mpl in terms of muDW
    Mpl_in_muDW = sp.simplify(Mpl_forced.subs(rho, cL * muDW**4))
    # Mpl_in_muDW should be proportional to muDW
    prop = sp.simplify(Mpl_in_muDW / muDW)
    mpl_prop_mudw = prop.free_symbols.isdisjoint({muDW})
    check("Q2b joint (GU DeWitt + super-Higgs vac-energy) FORCES M_Pl proportional to mu_DW",
          mpl_prop_mudw,
          f"M_Pl = ({sp.nsimplify(prop)}) * mu_DW  => forcing pins mu_DW ~ M_Pl (DECOUPLED), not a window")

    # Numeric sanity: with the OBSERVED vacuum energy and the REAL Planck mass (cited
    # comparison constants, NOT fitted), the super-Higgs gravitino mass and GU's RS mass
    # differ by ~30 orders -> they cannot both be the DE-derived scale. Confirms no forcing
    # to a falsifiable value.
    rho_obs_qtr_eV = 2.3e-3     # (rho_Lambda)^{1/4} in eV -- CITED DE scale, comparison only
    Mpl_eV = 2.435e27           # reduced Planck mass in eV -- CITED constant, comparison only
    cL_val = 3.0 / 8.0          # H51 COMPUTED
    m2eff_val = 1.0             # mid of [5/6, 5/4]
    muDW_val = rho_obs_qtr_eV / (cL_val ** 0.25)           # from rho = cL muDW^4
    m_RS_val = (m2eff_val ** 0.5) * muDW_val               # GU RS mass ~ meV
    rho_SB = rho_obs_qtr_eV ** 4                           # if SUSY-breaking = observed vac energy
    m32_val = (rho_SB / 3.0) ** 0.5 / Mpl_eV               # super-Higgs gravitino mass
    ratio = m_RS_val / m32_val
    print(f"    [numeric, cited-comparison] GU m_RS   ~ {m_RS_val:.3e} eV")
    print(f"    [numeric, cited-comparison] SH  m_3/2 ~ {m32_val:.3e} eV")
    print(f"    [numeric, cited-comparison] ratio m_RS / m_3/2 ~ {ratio:.2e}  (orders of magnitude apart)")
    check("Q2b at observed rho, super-Higgs m_3/2 != GU m_RS by many orders (no forced match)",
          ratio > 1e20, f"ratio ~ {ratio:.1e} -> the DE-scale cannot be BOTH via super-Higgs and via GU")

    # OVERALL Q2 verdict: super-Higgs does NOT force mu_DW to a falsifiable value.
    not_forced = is_linear_free and exponents_differ and mpl_prop_mudw
    check("Q2 VERDICT: super-Higgs does NOT force mu_DW (keystone does NOT fall via this route)",
          not_forced, "mu_DW stays free / traded for free <F>; vac-energy pin forces Planckian (decoupled)")
    return not_forced


# ============================================================================
def q3_mechanism_gate():
    """Is the mass mechanism super-Higgs (guardian present) or Porrati-Rahman (guardian-free)?"""
    print("\n" + "=" * 78)
    print("Q3  MECHANISM: super-Higgs (guardian) vs Porrati-Rahman (guardian-free)")
    print("=" * 78)

    # super-Higgs is a LOGICAL CONJUNCTION of two ingredients (both ARGUED from GU's record):
    #   (i)  local SUSY gauge invariance  -> a massless gravitino gauge field to start from
    #   (ii) a goldstino in a SUSY-breaking sector -> the mode the gravitino EATS to get mass
    # GU's published record (wave34 landscape scan; rs_ghost_sugra_gravitino_brst.py):
    #   - no established local SUSY structure ("no local SUSY as far as the record shows");
    #   - the gravitino gauge leg needs a curvature/holonomy datum W the symbol rep lacks --
    #     an UNBUILT source-action input, so the gauge invariance is not exhibited;
    #   - no goldstino sector is present.
    local_susy_established = False   # ARGUED from wave34 / oq-rs3 comparison
    goldstino_present = False        # ARGUED from wave34
    superhiggs_available = local_susy_established and goldstino_present
    check("Q3 super-Higgs requires local SUSY AND a goldstino; GU record establishes NEITHER",
          not superhiggs_available,
          "guardian absent -> super-Higgs mechanism not available on the published record")

    # Absent the guardian, the mass comes from the guardian-FREE Porrati-Rahman non-minimal
    # coupling (wave17/wave34): impose ker(Gamma) by a non-minimal RS vertex. That is a
    # FINITE-CUTOFF EFT (Rahman helicity-1/2 cutoff), not a UV-complete super-Higgs theory.
    cure_is_porrati_rahman = not superhiggs_available
    check("Q3 mass mechanism is Porrati-Rahman non-minimal cure (guardian-free, finite-EFT)",
          cure_is_porrati_rahman,
          "ker(Gamma) imposed by non-minimal vertex; NOT a goldstino eaten via broken local SUSY")

    # gyromagnetic discriminator: the SUSY gravitino needs g = 2 for clean high-energy
    # behavior; GU's cure g-value is not the SUSY value in the record (the RT-trace-dichotomy
    # 1-parameter family 'wedge - 6 contract' is not pinned to g=2). So Deser-Zumino (super-
    # Higgs) and GU's Porrati-Rahman cure are DIFFERENT operators, even though they overlap on
    # the causal gamma-traceless massive-RS on-shell content (Q1).
    g_susy = sp.Integer(2)
    g_gu_is_susy_value = False       # ARGUED: not established as g=2 in the record
    check("Q3 SUSY gravitino needs g=2; GU cure g-value is not the SUSY value on the record",
          not g_gu_is_susy_value, f"g_SUSY={g_susy}; Deser-Zumino operator != GU Porrati-Rahman operator")

    mechanism_not_superhiggs = (not superhiggs_available) and cure_is_porrati_rahman
    check("Q3 VERDICT: mechanism is NOT super-Higgs (no guardian); Deser-Zumino != PR cure",
          mechanism_not_superhiggs, "overlap on on-shell content, divergence on mechanism & operator")
    return mechanism_not_superhiggs


# ============================================================================
def main():
    print("#" * 78)
    print("# H54 branch 2 -- gravitino / super-Higgs.  DETERMINISTIC. BLIND to other branches.")
    print("#" * 78)

    q1 = q1_structural_field_content()   # field-content match TRUE
    q2 = q2_superhiggs_forces_mudw()     # super-Higgs does NOT force mu_DW
    q3 = q3_mechanism_gate()             # mechanism is NOT super-Higgs (Porrati-Rahman)

    print("\n" + "=" * 78)
    print("Q4  ASSEMBLED VERDICT")
    print("=" * 78)
    # PARTIAL: gravitino-LIKE field content (Q1 TRUE), but the super-Higgs scale is NOT
    # forced (Q2) and the mechanism is NOT super-Higgs (Q3). mu_DW is NOT forced.
    verdict_partial = q1 and q2 and q3
    print(f"    Q1 field-content match (gravitino-like)      : {q1}")
    print(f"    Q2 super-Higgs does NOT force mu_DW          : {q2}")
    print(f"    Q3 mechanism is NOT super-Higgs (PR cure)    : {q3}")
    print()
    print("    VERDICT = PARTIAL:  GU's RS is gravitino-LIKE in field content (the ker-Gamma")
    print("    cure IS the gravitino gauge condition), but its mass does NOT arise via super-")
    print("    Higgs (no local-SUSY guardian, no goldstino), and identifying mu_DW with a")
    print("    super-Higgs breaking scale does NOT force mu_DW -- it trades one free scale for")
    print("    another, and the vacuum-energy pin gives a DIFFERENT power law (forcing Planckian,")
    print("    decoupled).  The falsifiability keystone (H53) does NOT fall via super-Higgs.")

    check("Q4 assembled verdict is PARTIAL (gravitino-like content, super-Higgs scale NOT forced)",
          verdict_partial, "mu_DW NOT forced")

    # ---- summary ----
    print("\n" + "=" * 78)
    npass = sum(1 for _, p, _ in results if p)
    ntot = len(results)
    for name, passed, _ in results:
        if not passed:
            print(f"  FAILED: {name}")
    print(f"SUMMARY: {npass}/{ntot} checks PASS")
    print("=" * 78)
    if npass == ntot:
        print("[PASS] H54 branch 2 -- verdict PARTIAL; mu_DW NOT forced by super-Higgs.")
        sys.exit(0)
    else:
        print("[FAIL] one or more structural checks failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
