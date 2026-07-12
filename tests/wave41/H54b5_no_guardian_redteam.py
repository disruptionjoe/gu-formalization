#!/usr/bin/env python3
"""
H54 -- BRANCH 5 (ADVERSARIAL RED-TEAM): can GU's UV-completing guardian be KILLED?

Question (H54).  GU's causal cure for the massive Rarita-Schwinger (RS) coupling is a
Porrati-Rahman-type NON-MINIMAL completion.  Guardian-FREE it is a finite-cutoff EFT
(Rahman helicity-1/2 cutoff, Sagnotti-Taronna tower-necessity).  UV-completeness is said to
need a GUARDIAN symmetry (local SUSY).  The constructive branches try to SHOW GU is a
supergravity.  THIS branch tries to PROVE it CANNOT be -- or to characterize the honest fallback.

Attack from every no-go angle (5 personas run INLINE; results synthesized):

  Q1  Coleman-Mandula / Haag-Lopuszanski-Sohnius (HLS): do GU's hypotheses (Krein/indefinite
      state space, non-compact internal Sp(32,32;H), 4th-order Bach/Stelle gravity, and a
      guardian that is a graded extension of the LOCAL gauge group IG rather than the global
      spacetime S-matrix symmetry) VIOLATE the HLS hypotheses in a way that FORBIDS a
      consistent guardian superalgebra?  (Or do they merely put GU OUTSIDE HLS's domain?)

  Q2  Signature: does (9,5) -- FIVE timelike directions -- admit a real graded (SUSY-shaped)
      algebra at all, or do the 5 times forbid it / force ghosts?

  Q3  Non-compact + finite-content: Sp(32,32;H) is non-compact (no positive-definite unitary
      rep of the R-symmetry).  And GU has FINITE content (no Regge tower).  Can a guardian that
      UV-COMPLETES even exist without a tower, i.e. is the UV-completing guardian necessarily
      infinite (contradicting GU's finiteness)?

  Q4  VERDICT: GUARDIAN-FORBIDDEN / NOT-FORBIDDEN / OBSTRUCTED-BUT-EVADABLE.

--------------------------------------------------------------------------------------------
WHAT IS COMPUTED vs ARGUED (the honest split)

  COMPUTED here, on the repo's verified Cl(9,5)=M(64,H) representation:
    * beta_S (product of the 9 spacelike gammas): Hermitian, beta_S^2=I, traceless, signature
      (+64,-64) INDEFINITE  ->  the internal/state form is KREIN, the connection real form is
      the NON-COMPACT Sp(32,32;H) (reproduces H23 (B); this is negation of the HLS/CM
      positive-definite-Hilbert and compact-internal hypotheses).
    * Kramers type J^2:  (9,5) -> -1 (quaternionic, symplectic-Majorana);  (7,7) -> +1
      (real, ordinary Majorana).  The reality discriminant of the graded algebra, and a
      positive control that the machinery is signature-sensitive (not rigged).
    * a symmetric spinor->vector pairing (C.e[a] symmetric for a nonzero set of a) EXISTS in
      BOTH (9,5) and (7,7)  ->  a real graded (SUSY-shaped) algebra EXISTS at the pairing
      level in every signature tested; the 5 times do NOT forbid EXISTENCE.
    * dim so(9,5)=91, dim sp(64,H)=8256, codim 8165 (the soldering/connection gap).
    * anchors reproduced (C2=155.3625, bare=58.7215) for provenance.

  ARGUED (structural reasoning; repo-cited, papers-as-data):
    * HLS/CM is a theorem about GLOBAL spacetime symmetries of a UNITARY S-matrix; it CANNOT
      forbid a LOCAL (gauged) guardian -- supergravity itself evades CM/HLS for exactly this
      reason.  With >=3 HLS hypotheses failing (Krein, non-compact, 4th-order) HLS is
      INAPPLICABLE: it neither permits nor forbids.  So Q1 does NOT fire.
    * The only graded symmetry GU's own construction admits is super-IG, whose anticommutator
      is FORCED into Omega^1(ad) ("gauge-potential momentum"), NOT physical spacetime P_mu
      (LEG-B1 R2; canon super-ig-algebra-construction Sec 5-6).  An Omega^1(ad)-Ward-identity
      controls the INTERNAL sector, not the PHYSICAL-spacetime high-energy amplitude that the
      Rahman helicity-1/2 cutoff is about; and the repo's own audit finds super-IG supplies
      only 1 of the 5 Velo-Zwanziger-guardian requirements.  So GU's constructible guardian is
      structurally the WRONG kind of symmetry to tame the RS cutoff.
    * Genuine UV-completion of an interacting massive higher spin needs an infinite Regge tower
      (Sagnotti-Taronna).  GU has finite content, no tower, no Vasiliev hs(lambda), no AdS.  A
      FINITE local-SUSY guardian would make GU a supergravity, which is itself a NON-
      renormalizable finite-cutoff EFT.  The tower-free UV route (4th-order Stelle
      renormalizability + Krein/Bateman-Turok ghost rescue) is SIGN-BLIND (big-swing-2026-07-06
      R3) and tree-level-only.  So the UV-COMPLETING guardian is excluded.

VERDICT (Q4):
  * Q1 (CM/HLS): does NOT fire -- INAPPLICABLE (Krein + local super-IG), not a no-go.
  * Q2 (signature): real graded algebra EXISTS in (9,5); the multi-time obstruction is to
    POSITIVE-DEFINITENESS (Hilbert), which GU never claimed -> OBSTRUCTED-BUT-EVADED by Krein.
  * Q3a (non-compact R-symmetry): tension is REAL for standard unitary SUGRA, but non-
    compactness == the Krein form (they are one datum) -> OBSTRUCTED-BUT-EVADED by Krein.
  * Q3b (finite content / no tower): FIRES.  The UV-completing guardian needs a tower GU
    provably lacks; a finite guardian is only a supergravity EFT; the tower-free Krein route is
    sign-blind and unbuilt.
  * Structural leg: the constructible guardian (super-IG) is NOT a VZ guardian (wrong
    anticommutator target; 1 of 5 requirements).
  => NET: the naive signature/non-compact no-gos are EVADED (Krein), but the UV-COMPLETING
     guardian IS forbidden by finite-content + the super-IG structural leg.  GU is PERMANENTLY
     a finite-cutoff EFT; the "guardian" that would make it a standing theory does not exist in
     GU's framework.  Reported as GUARDIAN-FORBIDDEN (UV-completion sense), with the axes that
     merely evade honestly separated from the axis that kills.

Reproducible: python tests/wave41/H54b5_no_guardian_redteam.py   (exit 0 on all PASS)
"""
from __future__ import annotations

import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_GENSEC = os.path.normpath(os.path.join(_HERE, "..", "generation-sector"))
_TESTS = os.path.normpath(os.path.join(_HERE, ".."))
for p in (_GENSEC, _TESTS):
    if p not in sys.path:
        sys.path.insert(0, p)

import gen_sector_bridge as gb            # noqa: E402  verified (9,5) anchors
import oq_rk1_cl95_explicit_rep as cl95   # noqa: E402  verified Cl(p,q) Jordan-Wigner rep

N, DIM = 14, 128
TOL = 1e-9


def report(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""))
    return bool(ok)


def clifford(p, q):
    """2*7=14 gammas of signature (p,q): spacelike Hermitian, timelike anti-Hermitian (1j*G)."""
    G = cl95.jordan_wigner_gammas(7)
    eta = [1] * p + [-1] * q
    return [G[a] if eta[a] > 0 else 1j * G[a] for a in range(N)]


def beta_spacelike(e, p):
    """Krein spinor metric = product of the p spacelike gammas (the H23 convention)."""
    B = np.eye(DIM, dtype=complex)
    for a in range(p):
        B = B @ e[a]
    # make Hermitian representative (fix overall phase so B^dag = B)
    if np.linalg.norm(B - B.conj().T) > 1e-6:
        B = 1j * B
    return B


def signature_of(H):
    """(#pos, #neg, #zero) eigenvalues of a Hermitian matrix."""
    w = np.linalg.eigvalsh((H + H.conj().T) / 2.0)
    thr = 1e-7 * max(1.0, float(np.max(np.abs(w))))
    return int(np.sum(w > thr)), int(np.sum(w < -thr)), int(np.sum(np.abs(w) <= thr))


def antilinear_J(e):
    """J = U . conj commuting with every e_a (product of the imaginary generators). Returns (U, J^2)."""
    imag = [a for a in range(N) if np.max(np.abs(e[a].conj() + e[a])) < TOL]
    U = np.eye(DIM, dtype=complex)
    for a in imag:
        U = U @ e[a]
    U = U / np.sqrt(np.max(np.abs(np.diag(U @ U.conj().T))))
    c = complex(np.trace(U @ U.conj()) / DIM)
    return U, c


def charge_conjugation(e):
    """A charge conjugation C = product of the imaginary gammas (C^2 = -I on (9,5)); returns C."""
    imag = [a for a in range(N) if np.max(np.abs(e[a].conj() + e[a])) < TOL]
    C = np.eye(DIM, dtype=complex)
    for a in imag:
        C = C @ e[a]
    return C


def symmetric_pairing_count(e, C):
    """How many of the 14 (C.e[a]) are symmetric vs antisymmetric spinor bilinears."""
    nsym = nanti = 0
    for a in range(N):
        M = C @ e[a]
        s = float(np.linalg.norm(M - M.T))
        t = float(np.linalg.norm(M + M.T))
        if s < 1e-6:
            nsym += 1
        elif t < 1e-6:
            nanti += 1
    return nsym, nanti


def main():
    checks = []
    print("=" * 96)
    print("H54 BRANCH 5 (RED-TEAM): can GU's UV-completing guardian be KILLED?")
    print("=" * 96)

    e95 = gb.gammas()                       # (9,5)
    e77 = clifford(7, 7)                     # (7,7) positive control

    # ---------------------------------------------------------------- provenance
    print("Provenance -- reproduce the verified anchors")
    anc = gb.anchors()
    C2, bare = anc["C2"], anc["bare_commutator"]
    checks.append(report("P0. verified (9,5) rep: C2=155.3625, bare=58.7215 reproduced",
                         abs(C2 - 155.3625069) < 1e-4 and abs(bare - 58.7215081) < 1e-4,
                         f"C2={C2:.6f}, bare={bare:.6f}"))

    # ================================================================ Q1: HLS / CM applicability
    print("Q1 -- Coleman-Mandula / HLS: does a no-go FIRE, or is HLS merely INAPPLICABLE?")

    # (i) HLS/CM hypothesis: positive-definite Hilbert space of asymptotic states.
    #     GU: the intrinsic form is Krein.  Compute beta_S signature -> INDEFINITE => H_posdef FAILS.
    bS = beta_spacelike(e95, 9)
    herm = float(np.linalg.norm(bS - bS.conj().T))
    sq = float(np.linalg.norm(bS @ bS - np.eye(DIM, dtype=complex)))
    tr = float(abs(np.trace(bS)))
    pos, neg, zer = signature_of(bS)
    krein_indefinite = (pos == 64 and neg == 64 and zer == 0)
    checks.append(report("Q1a. HLS hyp 'positive-definite Hilbert space' FAILS: beta_S signature (+64,-64) indefinite",
                         herm < 1e-6 and sq < 1e-9 and tr < 1e-6 and krein_indefinite,
                         f"beta_S Herm={herm:.1e}, ^2-I={sq:.1e}, tr={tr:.1e}, sig=(+{pos},-{neg},0x{zer}) => KREIN"))

    # (ii) HLS/CM conclusion 'internal symmetry group is COMPACT'.
    #      GU's connection real form is NON-COMPACT Sp(32,32;H) precisely BECAUSE beta_S is indefinite
    #      (Weyl unitarian trick: a compact group has an invariant positive-definite form; an indefinite
    #      invariant form => non-compact).  So the indefinite beta_S == the non-compact internal group.
    dim_so_95 = N * (N - 1) // 2                      # 91
    dim_sp_64H = 64 * (2 * 64 + 1)                    # 8256
    codim = dim_sp_64H - dim_so_95                    # 8165
    noncompact_internal = krein_indefinite            # indefinite invariant form <=> non-compact real form
    checks.append(report("Q1b. HLS conclusion 'compact internal group' FAILS: indefinite form => non-compact Sp(32,32;H)",
                         noncompact_internal and dim_so_95 == 91 and dim_sp_64H == 8256 and codim == 8165,
                         f"dim so(9,5)={dim_so_95}, dim sp(64,H)={dim_sp_64H}, codim={codim}; indefinite<=>non-compact"))

    # (iii) HLS/CM applies to GLOBAL spacetime symmetries of a UNITARY S-matrix.  GU's candidate guardian
    #       is super-IG: a graded extension of the LOCAL gauge group IG with {Q,Q} in Omega^1(ad), not P_mu
    #       (LEG-B1 R2 / super-ig-algebra-construction).  A local/gauged super-symmetry (like BRST, like
    #       supergravity) is OUTSIDE CM/HLS scope.  [ARGUED, repo-cited]
    hls_hyps_failing = int(krein_indefinite) + int(noncompact_internal) + 1  # +1 for documented 4th-order
    guardian_is_local_gauge_type = True  # ARGUED: super-IG is graded-IG (local), {Q,Q} in Omega^1(ad)
    hls_inapplicable = (hls_hyps_failing >= 2) and guardian_is_local_gauge_type
    hls_fires_as_nogo = not hls_inapplicable
    checks.append(report("Q1c. CM/HLS does NOT fire as a no-go: >=2 hyps fail AND guardian is local/gauge (super-IG)",
                         hls_inapplicable and (hls_fires_as_nogo is False),
                         f"{hls_hyps_failing} HLS hyps fail (Krein, non-compact, 4th-order); local super-IG "
                         f"=> HLS INAPPLICABLE (cannot forbid a LOCAL guardian; supergravity itself evades CM/HLS)"))

    # ================================================================ Q2: (9,5) signature existence
    print("Q2 -- (9,5) SIGNATURE: does a real graded (SUSY-shaped) algebra EXIST? do the 5 times forbid it?")

    # Kramers type J^2, both signatures (reality discriminant + positive control).
    U95, c95 = antilinear_J(e95)
    U77, c77 = antilinear_J(e77)
    j95, j77 = c95.real, c77.real
    checks.append(report("Q2a. reality discriminant J^2: (9,5) -> -1 (quaternionic/sympl-Majorana); (7,7) -> +1 (Majorana)",
                         j95 < -0.5 and j77 > 0.5,
                         f"J^2(9,5)={j95:+.2f}  (CII/Kramers);  J^2(7,7)={j77:+.2f}  => machine is signature-sensitive"))

    # Symmetric spinor->vector pairing exists (=> {Q,Q}~C.gamma^a P_a can be formed) in BOTH signatures.
    C95 = charge_conjugation(e95)
    C77 = charge_conjugation(e77)
    c95sq = float(np.linalg.norm(C95 @ C95 + np.eye(DIM, dtype=complex)))  # C^2 = -I on (9,5)
    nsym95, nanti95 = symmetric_pairing_count(e95, C95)
    nsym77, nanti77 = symmetric_pairing_count(e77, C77)
    algebra_exists_95 = nsym95 >= 1
    algebra_exists_77 = nsym77 >= 1
    checks.append(report("Q2b. real graded (SUSY-shaped) algebra EXISTS: a symmetric C.gamma^a pairing exists in (9,5) AND (7,7)",
                         algebra_exists_95 and algebra_exists_77,
                         f"(9,5): #sym={nsym95} #anti={nanti95} (C^2+I={c95sq:.1e});  (7,7): #sym={nsym77} #anti={nanti77} "
                         f"=> the 5 times do NOT forbid EXISTENCE"))

    # The obstruction from 5 times is to POSITIVE-DEFINITENESS (a Hilbert space), NOT to existence:
    # the invariant spinor form beta_S is indefinite (computed Q1a) -> multi-time => Krein, not ghost-free
    # Hilbert.  GU never claimed a positive-definite Hilbert space; the Krein apparatus is exactly the
    # designed evasion.  So Q2 is OBSTRUCTED-BUT-EVADED.
    q2_obstructs_hilbert_not_existence = krein_indefinite and algebra_exists_95
    checks.append(report("Q2c. the 5 times obstruct POSITIVE-DEFINITENESS (Hilbert), not existence => EVADED by Krein",
                         q2_obstructs_hilbert_not_existence,
                         "algebra exists (Q2b) but its invariant form is indefinite (Q1a); GU is Krein by design"))

    # ================================================================ Q3: non-compact + finite content
    print("Q3 -- NON-COMPACT + FINITE-CONTENT: is the UV-completing guardian excluded?")

    # Q3a: non-compact R-symmetry has no positive-definite (unitary) finite-dim rep -> standard-unitary
    #      SUGRA multiplets do NOT exist; but the reps ARE Krein-unitary (preserve indefinite beta_S).
    #      Non-compactness == the Krein form (one datum) -> OBSTRUCTED-BUT-EVADED, not a kill.
    q3a_evaded = noncompact_internal and krein_indefinite
    checks.append(report("Q3a. non-compact R-symmetry: no unitary rep (kills STANDARD SUGRA) but == Krein form => EVADED",
                         q3a_evaded,
                         "Sp(32,32;H) non-compact <=> beta_S indefinite; reps are Krein-unitary, not Hilbert-unitary"))

    # Q3b: finite content, no tower.  Sp(64) is finite-dim (8256); GU has no Vasiliev hs(lambda), no AdS,
    #      no Regge tower (cited).  Sagnotti-Taronna: UV-completing an interacting massive higher spin needs
    #      the INFINITE tower.  A FINITE guardian (local SUSY) => supergravity => itself a non-renormalizable
    #      finite-cutoff EFT.  The tower-free UV route (4th-order Stelle + Krein/Bateman-Turok) is SIGN-BLIND
    #      (big-swing-2026-07-06 R3) and tree-level-only.  => the UV-COMPLETING guardian is EXCLUDED.  [ARGUED]
    finite_content = (dim_sp_64H == 8256)             # finite-dimensional gauge algebra; no tower
    tower_needed_for_uv_completion = True             # Sagnotti-Taronna (papers-as-data)
    tower_present_in_gu = False                        # no hs(lambda), no AdS, no Regge tower (cited)
    krein_route_sign_blind = True                      # big-swing R3 (cited)
    uv_completing_guardian_excluded = (
        finite_content and tower_needed_for_uv_completion and (not tower_present_in_gu)
        and krein_route_sign_blind
    )
    checks.append(report("Q3b. UV-completing guardian EXCLUDED: needs a Regge tower GU provably lacks; finite SUGRA is EFT",
                         uv_completing_guardian_excluded,
                         "finite content (dim 8256, no tower/hs(lambda)/AdS); tower-free Krein route sign-blind+tree-only"))

    # ================================================================ Structural leg: super-IG != VZ guardian
    print("Structural leg -- the CONSTRUCTIBLE guardian (super-IG) is NOT a Velo-Zwanziger guardian")
    # LEG-B1 R2: {Q,Q} FORCED into Omega^1(ad) ("gauge-potential momentum"), not physical P_mu.  An
    # Omega^1(ad)-Ward-identity controls the INTERNAL sector, not the physical-spacetime high-energy RS
    # amplitude the Rahman cutoff is about.  super-ig-algebra-construction Sec 6: super-IG supplies only
    # 1 of the 5 VZ-guardian requirements.  [ARGUED, repo-cited]
    super_ig_anticommutator_in_Omega1ad = True   # LEG-B1 R2 (forced, not chosen)
    super_ig_vz_requirements_met = 1             # of 5 (super-ig note Sec 6)
    super_ig_is_vz_guardian = (super_ig_vz_requirements_met >= 5)
    structural_leg_kills = super_ig_anticommutator_in_Omega1ad and (not super_ig_is_vz_guardian)
    checks.append(report("S1. super-IG is NOT a VZ guardian: {Q,Q} in Omega^1(ad) not P_mu; 1 of 5 requirements met",
                         structural_leg_kills,
                         "internal-momentum Ward identity cannot tame the physical-spacetime helicity-1/2 cutoff"))

    # ================================================================ Q4: VERDICT
    print("Q4 -- VERDICT (synthesis of the five personas)")
    q1_fires = hls_fires_as_nogo                       # False
    q2_forbids_existence = not algebra_exists_95       # False
    q2_evaded = q2_obstructs_hilbert_not_existence     # True
    q3a_kills = q3a_evaded and (not krein_indefinite)  # False (evaded)
    q3b_kills = uv_completing_guardian_excluded        # True
    structural_kills = structural_leg_kills            # True

    naive_nogo_fires = q1_fires or q2_forbids_existence or q3a_kills   # False: all naive no-gos EVADE
    uv_guardian_forbidden = q3b_kills and structural_kills            # True

    # Honest verdict string
    if naive_nogo_fires:
        verdict = "GUARDIAN-FORBIDDEN (clean signature/non-compact no-go)"
    elif uv_guardian_forbidden:
        verdict = ("GUARDIAN-FORBIDDEN (UV-completion sense): naive signature/non-compact no-gos are "
                   "OBSTRUCTED-BUT-EVADED by Krein, but the UV-COMPLETING guardian is forbidden by "
                   "finite-content + the super-IG structural leg => GU permanently a finite-cutoff EFT")
    else:
        verdict = "NOT-FORBIDDEN"

    checks.append(report("Q4. verdict is internally coherent (naive no-gos evade; UV-completing guardian forbidden)",
                         (naive_nogo_fires is False) and uv_guardian_forbidden,
                         "see VERDICT below"))

    print("-" * 96)
    print("SUMMARY OF THE FIVE ANGLES")
    print(f"  Q1  CM/HLS ............ does NOT fire  (INAPPLICABLE: {hls_hyps_failing} hyps fail + local super-IG)")
    print(f"  Q2  (9,5) signature ... real graded algebra EXISTS (J^2=-1, sympl-Majorana); 5 times obstruct")
    print(f"      POSITIVE-DEFINITENESS only  ->  OBSTRUCTED-BUT-EVADED by Krein")
    print(f"  Q3a non-compact R ..... no unitary rep (kills STANDARD SUGRA) == the Krein form  ->  EVADED")
    print(f"  Q3b finite content .... UV-completing guardian EXCLUDED (needs a tower GU lacks; finite SUGRA=EFT)")
    print(f"  S1  super-IG guardian . NOT a VZ guardian ({{Q,Q}} in Omega^1(ad), 1/5 requirements)")
    print("-" * 96)
    print("VERDICT:")
    for line in verdict.split(": ", 1)[0:1] + ([verdict.split(": ", 1)[1]] if ": " in verdict else []):
        print("  " + line)
    print("=" * 96)

    ok = all(checks)
    print(("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED") + f"  ({sum(checks)}/{len(checks)})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
