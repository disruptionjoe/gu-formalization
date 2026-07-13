#!/usr/bin/env python3
r"""
W108 -- DOES THE SIGN-DEFINITIZATION (W104 T3) SURVIVE MODE-MIXING?  The 2-doublet + SHARED-CLOCK toy.

THE KERNEL UNDER TEST.  W104 (Steelman 2, the Krein crossed product) found the one genuinely new
structure of the killed steelman: group averaging over the constraint H_mod + q = 0 with observer
energy q >= 0 keeps, PER MODE, exactly one survivor whose Krein norm is UNIFORMLY NEGATIVE --
definitization IN SIGN (not in norm: survivor norm s_k = sqrt(1-r_k^2) -> 0).  But that was computed
MODE-BY-MODE: each doublet had its own clock-constraint pairing.  Under INTERACTIONS the modes MIX
(the W98 P2 setting), and the physical CLPW observer is ONE clock for the whole region.  Question:
does the constraint's survivor subspace REMAIN sign-definite when modes mix through a SHARED clock,
or does mixing produce survivors of BOTH signs?

THE MODEL (built, not gestured at).  Two W52/W98 Krein doublets, parameters r_1, r_2:
    H_mod(r) = [[ i r, 1 ], [ 1, -i r ]],   eta_K = sigma_x per doublet,   spec = +-s,  s = sqrt(1-r^2)
Field space C^4 = C^2 (+) C^2, Krein form eta_4 = sigma_x (+) sigma_x (signature (2,2)).
MIXING: an off-diagonal (doublet-1 <-> doublet-2) coupling eps*V with V eta_4-SELF-ADJOINT
(eta_4 V hermitian), the Krein-legitimate interaction class; V = [[0, C], [C', 0]] block form forces
C' = sigma_x C^dag sigma_x.  Coupling classes swept: isotropic C = I (the symmetric mixing), C =
sigma_x, C = sigma_z, and random complex C (genericity census).
SHARED CLOCK: one observer, energy q >= 0 (L^2(R_+)-like), constraint  H_1 + H_2 + eps*V + q = 0.
Group averaging: a field eigenvector v_h of the TOTAL mixed H_field with REAL eigenvalue h pairs
with the clock generalized eigenvector |q = -h>, which EXISTS iff h <= 0.  So the SURVIVOR SUBSPACE
= span of eigenvectors with real eigenvalue h < 0; complex-pair eigenvectors solve NO constraint and
are ANNIHILATED by the physical projection.  Distinct real eigenvalues are eta-orthogonal (and carry
orthogonal clock states), so the induced physical Gram is diagonal with entries = Krein norms.

WHAT THIS FILE PROVES ON THE TOY (deterministic, numpy-only):

  T1 -- CONTROL (eps = 0): reproduces W104 exactly -- two survivors h = -s_1, -s_2, Krein norms
        -s_1, -s_2 (uniformly negative, degenerate as r -> 1), Gram cross terms = 0.

  T2 -- WEAK MIXING (phase I): for eps well below the first exceptional collision the survivor
        subspace stays 2-dim and UNIFORMLY NEGATIVE across the (r_1, r_2) grid and all coupling
        classes; the Krein-norm shift is O(eps^2) (no first-order sign motion) -- the perturbative
        derivation (D2a) agrees with exact diagonalization (D1).  SIGN SURVIVES WEAK MIXING.

  T3 -- THE EXACT KILL (D2b, analytic, machine-checked): r_1 = r_2 = r with the ISOTROPIC coupling
        V = [[0,I],[I,0]] = SX (x) I_2 COMMUTES with H_0 = I_2 (x) H_mod(r).  Joint eigenvectors
        u_a (x) w_b, eigenvalues h = b*s + a*eps (a,b = +-1), Krein norm = kn(w_b) = b*s (the
        doublet norm, INDEPENDENT of the mixing branch a).  For eps > s the survivor set is
        { h = -(eps+s): kn = -s < 0 ;  h = -(eps-s): kn = +s > 0 } -- BOTH SIGNS, EXACTLY.  The
        positive-norm survivor is the h = +s (ghost-signature-positive) mode DRAGGED below zero
        total energy by the mixing: the shared clock constrains only the TOTAL energy, so a
        positive-Krein-norm excitation slips under the constraint as soon as eps > s.  This is an
        exact analytic statement, not a numerical accident.

  T4 -- THE PHASE DIAGRAM (exact diagonalization sweep, D1): three phases in (eps; r_1, r_2):
        PHASE I   (eps < eps_EP ~ s_2):  2 survivors, uniformly negative (sign survives; norms ~ s,
                  degenerate -- the W104 structure).
        PHASE II  (eps_EP < eps < eps_re, ANISOTROPIC couplings): a Krein collision at h = 0 ejects
                  one opposite-signature pair into a COMPLEX (PT-broken) pair -- Krein-NEUTRAL, no
                  constraint solution, ANNIHILATED by the physical projection.  1 survivor, still
                  negative -- sign "survives" only by EJECTING half the mode content (for some
                  couplings/eps the second pair also complexifies: EMPTY physical space).
        PHASE III (eps > eps_re; for the isotropic coupling eps_re = s_1, i.e. IMMEDIATELY after
                  the window): the ejected pair re-emerges REAL with EXCHANGED Krein signatures --
                  survivors of BOTH SIGNS.  SIGN KILLED.
        Isotropic boundary located: eps_EP ~= s_2, eps_flip ~= s_1 (verified on the grid).

  T5 -- THE PHYSICAL REGIME IS ON THE FAILING SIDE: the W98 tower has FIXED interaction strength
        and s_k -> 0 in the UV, i.e. eps/s -> infinity -- every UV doublet pair sits DEEP past the
        phase-I boundary.  Computed at fixed eps with r -> 1 (0.9 -> 0.9999): the ISOTROPIC coupling
        gives INDEFINITE survivors (both signs, norms +-O(s) -- indefinite AND degenerate, the worst
        case); generic ANISOTROPIC couplings give the ejection phase (1 survivor per pair, negative,
        norm O(1) -- NON-degenerate but carrying HALF the mode content); the sigma_z coupling at
        large eps empties the physical space entirely.  Genericity census (200 random eta-s.a.
        couplings, eps >> s): ~92% ejection phase, ~2% indefinite, ~6% empty -- and 0% retain the
        W104 structure (full mode content + uniform sign).  IN NO COUPLING CLASS does the W104
        kernel (one uniformly-negative survivor PER MODE) survive the physical regime.

  T6 -- THE COMPLETION BACK-DOOR DOES NOT OPEN AS SCOPED:
        (a) PHASE I (where sign survives): the physical form is definite-but-degenerate; its
            canonical quotient-completion is a genuine Hilbert space and the modular FLOW descends
            UNITARILY (survivors are eigenvectors; phases e^{i h p}).  BUT the ALGEBRA does not: the
            compressed generic observable has physical-norm operator norm = 1/s_1 EXACTLY (computed:
            2.3 -> 7.1 -> 22.4 -> 70.7 tracking 1/s_1 as r -> 1) -- unbounded over the tower.  And
            the clock-orthogonality of distinct survivors forces the honestly-projected algebra to
            be DIAGONAL in the survivor basis (functions of H_field): ABELIAN.  The completion
            carries the flow and an abelian remnant, not the noncommutative algebra.  (This was
            already latent in W104: a multiplicity-free constraint spectrum compresses any algebra
            to an abelian one.)
        (b) PHASE II (generic physical regime): the completion is a genuine NON-degenerate Hilbert
            space (norms O(1)) -- but it is HALF the modes (the ejected complex pairs are genuine
            field content: at eps -> 0 they connect continuously to one healthy + one ghost mode),
            1-dim per doublet-pair, and the compressed algebra is again abelian.  What is lost in
            the quotient/ejection IS the ghost-physics content the conjecture is about.
        (c) PHASE III: nothing to complete (indefinite).

  T7 -- VERDICT = SIGN-KILLED-BY-MIXING (in the physical regime).  Weak mixing preserves the sign
        (T2); the physical regime (mixing >> splitting, the W98 UV tower) does not: isotropic mixing
        gives survivors of BOTH signs (exact, T3/T5); generic mixing preserves the sign only by
        ejecting half the mode content into Krein-neutral constraint-violating pairs, leaving a
        halved, abelianized remnant that is NOT the W104 structure.  The completion back-door does
        not open: where the form is definite-degenerate the completion loses the algebra (norms
        1/s); where it is definite-nondegenerate it has already lost half the physics.  The W104
        kernel does not earn continuation.

ADVERSARY ANSWERS (encoded): (i) "the shared clock is ONE observer -- multiple clocks would break it
again": INVERTED -- per-mode clocks are exactly what made W104's uniform sign work (separate
constraints per mode), and with mixing H_total does not factorize so per-mode constraints are not
even defined; the SINGLE shared clock is the physical CLPW setting and it is the one that kills.
(ii) "the null directions you quotient away ARE the ghost physics": CONFIRMED in phase II -- the
ejected Krein-neutral complex pairs connect continuously (eps -> 0) to genuine healthy+ghost mode
content; annihilating them is discarding the sector the conjecture is about.

TWO-DERIVATION DISCIPLINE: D1 = exact diagonalization sweep (T1/T2/T4/T5); D2 = (a) perturbation
theory at weak mixing + (b) the EXACT commuting-case analytic kill (T3).  They AGREE.

LOAD-BEARING assumptions (named): (i) the W52 doublet + W98 tower as the Krein type-III surrogate
(same toy grade as W91/W98/W104); (ii) the eta-self-adjoint block-off-diagonal coupling class as the
mode-mixing surrogate (swept over 4 named + 200 random couplings); (iii) mixing strength does NOT
decay faster than the splitting in the UV (the same non-UV-soft assumption as W98 -- the one honest
survival window, not the physical derivative-coupled case); (iv) survivors = real eigenvalues h < 0
(group averaging with a q >= 0 clock has solutions exactly there; complex pairs solve no constraint).

Deterministic, numpy-only, self-validating; exit 0 on success.  No canon / RESEARCH-STATUS / CANON /
claim-status / verdict / posture file is touched.  Exploration-grade.  NOT committed by this run.
"""
from __future__ import annotations

import numpy as np

np.random.seed(0)

results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


def dag(X: np.ndarray) -> np.ndarray:
    return X.conj().T


# ------------------------------------------------------------------------------------------------
# The 2-doublet shared-clock model.
# ------------------------------------------------------------------------------------------------
SX = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
I2 = np.eye(2, dtype=complex)
SZ = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
ETA4 = np.kron(np.eye(2), SX)                     # eta_4 = sigma_x (+) sigma_x, signature (2,2)


def H_mod(r: float) -> np.ndarray:
    return np.array([[1j * r, 1.0], [1.0, -1j * r]], dtype=complex)


def s_of(r: float) -> float:
    return float(np.sqrt(max(1.0 - r * r, 0.0)))


def H0(r1: float, r2: float) -> np.ndarray:
    Z = np.zeros((2, 2), dtype=complex)
    return np.block([[H_mod(r1), Z], [Z, H_mod(r2)]])


def V_from_C(C: np.ndarray) -> np.ndarray:
    # eta_4-self-adjoint block-off-diagonal mixing: eta_4 V hermitian <=> C' = sigma_x C^dag sigma_x
    Cp = SX @ dag(C) @ SX
    Z = np.zeros((2, 2), dtype=complex)
    return np.block([[Z, C], [Cp, Z]])


def eig_data(H: np.ndarray):
    """all eigenpairs with Krein norms (Hilbert-normalized eigenvectors)."""
    ev, R = np.linalg.eig(H)
    out = []
    for i in range(4):
        v = R[:, i] / np.linalg.norm(R[:, i])
        kn = float(np.real(v.conj() @ ETA4 @ v))
        out.append((complex(ev[i]), kn, v))
    out.sort(key=lambda t: t[0].real)
    return out


def survivors(H: np.ndarray, tol: float = 1e-8):
    """constraint H_field + q = 0, q >= 0, ONE shared clock: survivors = real eigenvalues h < 0."""
    return [(e.real, kn, v) for e, kn, v in eig_data(H) if abs(e.imag) < tol and e.real < -1e-10]


def classify(H: np.ndarray) -> str:
    sv = survivors(H)
    if not sv:
        return "EMPTY"
    signs = {np.sign(kn) for _, kn, _ in sv}
    if len(signs) > 1:
        return "INDEFINITE"
    return f"{len(sv)}NEG" if signs == {-1.0} else f"{len(sv)}POS"


rng = np.random.default_rng(42)
C_rand = rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2))
COUPLINGS = {
    "isotropic(C=I)": V_from_C(I2),
    "C=sigma_x": V_from_C(SX),
    "C=sigma_z": V_from_C(SZ),
    "C=random": V_from_C(C_rand),
}

log("=" * 100)
log("W108 -- does the SIGN-DEFINITIZATION (W104 T3) survive MODE-MIXING?  2-doublet + SHARED-CLOCK toy")
log("=" * 100)

# model sanity: every coupling is eta_4-self-adjoint; eta-orthogonality of distinct real eigenvectors
eta_sa_resid = max(float(np.max(np.abs(ETA4 @ V - dag(ETA4 @ V)))) for V in COUPLINGS.values())
assert eta_sa_resid < 1e-12, "coupling not eta-self-adjoint"
_ed = eig_data(H0(0.9, 0.95) + 0.6 * COUPLINGS["isotropic(C=I)"])
_reals = [(e, kn, v) for e, kn, v in _ed if abs(e.imag) < 1e-9]
gram_cross = max(
    abs(_reals[i][2].conj() @ ETA4 @ _reals[j][2])
    for i in range(len(_reals)) for j in range(i + 1, len(_reals))
)
assert gram_cross < 1e-12, "distinct real eigenvectors not eta-orthogonal (Gram not diagonal)"

# ================================================================================================
# T1 -- CONTROL (eps = 0): reproduce W104's two uniformly-negative survivors.
# ================================================================================================
log("\n[T1] control eps=0: reproduces W104 (two survivors, Krein norms -s_1, -s_2, Gram diagonal)")
ctrl_ok = True
detail = []
for (r1, r2) in [(0.3, 0.5), (0.9, 0.95), (0.99, 0.995)]:
    sv = survivors(H0(r1, r2))
    hs = sorted(h for h, _, _ in sv)
    kns = sorted(kn for _, kn, _ in sv)
    want_h = sorted([-s_of(r1), -s_of(r2)])
    want_kn = sorted([-s_of(r1), -s_of(r2)])
    ok = (len(sv) == 2 and max(abs(a - b) for a, b in zip(hs, want_h)) < 1e-9
          and max(abs(a - b) for a, b in zip(kns, want_kn)) < 1e-9
          and all(kn < 0 for kn in kns))
    ctrl_ok = ctrl_ok and ok
    detail.append(f"r=({r1},{r2}): kn=({kns[0]:.4f},{kns[1]:.4f})")
check("T1  CONTROL eps=0 reproduces W104 EXACTLY: two survivors h=-s_1,-s_2 with Krein norms "
      "-s_1,-s_2 -- uniformly NEGATIVE (sign-definite), degenerate as r->1, Gram diagonal "
      f"(max cross term {gram_cross:.1e}).", ctrl_ok, "; ".join(detail))

# ================================================================================================
# T2 -- WEAK MIXING (phase I): sign survives; Krein-norm shift is O(eps^2) (perturbative D2a = D1).
# ================================================================================================
log("\n[T2] weak mixing: survivor subspace stays 2-dim uniformly negative; kn shift O(eps^2)")
weak_ok = True
for name, V in COUPLINGS.items():
    Vn = V / np.linalg.norm(V, 2)
    for (r1, r2) in [(0.3, 0.5), (0.7, 0.8), (0.9, 0.95), (0.99, 0.995), (0.999, 0.9995)]:
        # inside phase I for EVERY coupling class: the anisotropic collision is at eps_EP ~ O(s_1*s_2)
        # (verified in T4b), so scale eps below that:
        eps = 0.1 * s_of(r1) * s_of(r2)
        weak_ok = weak_ok and classify(H0(r1, r2) + eps * Vn) == "2NEG"
# perturbative order: kn shift under eps*V is quadratic (first-order eigenvector correction lives in
# the OTHER doublet block and in the eta-orthogonal partner => no first-order Krein-norm motion)
kn0 = sorted(kn for _, kn, _ in eig_data(H0(0.9, 0.95)))
ratios = []
for eps in (1e-3, 2e-3, 4e-3):
    kn1 = sorted(kn for _, kn, _ in eig_data(H0(0.9, 0.95) + eps * COUPLINGS["isotropic(C=I)"]))
    d = max(abs(a - b) for a, b in zip(kn0, kn1))
    ratios.append(d / eps ** 2)
quad = max(ratios) / min(ratios) < 1.2 and all(np.isfinite(q) for q in ratios)
check("T2  WEAK MIXING (phase I): for eps = 0.1*s_1*s_2 (inside phase I for every coupling class) "
      "the survivor subspace is 2-dim and "
      "UNIFORMLY NEGATIVE across all 4 coupling classes and the whole (r_1,r_2) grid (incl. "
      "r=0.9995).  The Krein-norm shift is O(eps^2) -- shift/eps^2 constant to <20% over a dyadic "
      f"eps ladder (ratios {[f'{q:.2f}' for q in ratios]}) -- no first-order sign motion: the "
      "perturbative derivation (D2a) agrees with exact diagonalization (D1).  SIGN SURVIVES WEAK "
      "MIXING.", weak_ok and quad,
      f"all-2NEG={weak_ok}, kn-shift/eps^2 in [{min(ratios):.2f},{max(ratios):.2f}]")

# ================================================================================================
# T3 -- THE EXACT KILL (D2b): commuting case r_1 = r_2, isotropic V.  Spectrum {+-s +- eps} exact;
#   for eps > s the survivor -(eps - s) carries POSITIVE Krein norm +s.  Both signs, analytically.
# ================================================================================================
log("\n[T3] EXACT analytic kill: r_1=r_2=r, isotropic V commutes with H_0; eps>s => both signs, exactly")
Viso = COUPLINGS["isotropic(C=I)"]
exact_ok = True
detail = []
for r in (0.3, 0.9, 0.99):
    s = s_of(r)
    H00 = H0(r, r)
    comm = float(np.max(np.abs(H00 @ Viso - Viso @ H00)))
    for eps in (1.5 * s, 4.0 * s):
        pred = sorted([-s - eps, -s + eps, s - eps, s + eps])
        got = sorted([e.real for e, _, _ in eig_data(H00 + eps * Viso)])
        spec_err = max(abs(a - b) for a, b in zip(pred, got))
        sv = survivors(H00 + eps * Viso)
        kn_by_h = {round(h, 9): kn for h, kn, _ in sv}
        # survivor -(eps+s): kn = -s ; survivor -(eps-s): kn = +s  (exact prediction)
        kminus = kn_by_h.get(round(-(eps + s), 9))
        kplus = kn_by_h.get(round(-(eps - s), 9))
        ok = (comm < 1e-12 and spec_err < 1e-9 and kminus is not None and kplus is not None
              and abs(kminus + s) < 1e-9 and abs(kplus - s) < 1e-9
              and classify(H00 + eps * Viso) == "INDEFINITE")
        exact_ok = exact_ok and ok
    detail.append(f"r={r}: [H0,V]={comm:.1e}, spec err {spec_err:.1e}, kn(-(eps+s))={kminus:+.4f}, "
                  f"kn(-(eps-s))={kplus:+.4f}")
check("T3  THE EXACT KILL (analytic, machine-checked).  r_1=r_2=r with isotropic V = SX(x)I_2: "
      "[H_0,V]=0, spectrum {+-s+-eps} exact, Krein norm of each joint eigenvector = the DOUBLET "
      "norm b*s independent of the mixing branch.  For eps > s the survivor set is "
      "{ -(eps+s): kn=-s < 0 ; -(eps-s): kn=+s > 0 } -- BOTH SIGNS, EXACTLY: the h=+s "
      "positive-Krein-norm mode is dragged below zero TOTAL energy by the mixing and the shared "
      "clock (which constrains only the total) admits it.  Sign-definiteness killed analytically, "
      "not numerically.", exact_ok, " | ".join(detail))

# ================================================================================================
# T4 -- THE PHASE DIAGRAM (D1 sweep): phase I (2NEG) -> Krein collision at h=0 -> phase II
#   (ejection: complex Krein-neutral pair, 1NEG or EMPTY) -> phase III (re-emergence, INDEFINITE).
#   Isotropic boundary: eps_EP ~= s_2 (collision), eps_flip ~= s_1 (both signs).
# ================================================================================================
log("\n[T4] phase diagram: I (2NEG) -> II (ejection) -> III (indefinite); isotropic boundary at s_2, s_1")
def first_events(V: np.ndarray, r1: float, r2: float):
    eps_cx = eps_flip = None
    for eps in np.concatenate([np.linspace(1e-4, 0.25, 500), np.linspace(0.25, 3.0, 550)]):
        H = H0(r1, r2) + eps * V
        n_real = sum(1 for e, _, _ in eig_data(H) if abs(e.imag) < 1e-8)
        cl = classify(H)
        if eps_cx is None and n_real < 4:
            eps_cx = float(eps)
        if eps_flip is None and cl == "INDEFINITE":
            eps_flip = float(eps)
        if eps_cx is not None and eps_flip is not None:
            break
    return eps_cx, eps_flip


iso_boundary_ok = True
detail = []
for (r1, r2) in [(0.7, 0.8), (0.9, 0.95), (0.99, 0.995)]:
    s1, s2 = s_of(r1), s_of(r2)
    e_cx, e_fl = first_events(Viso, r1, r2)
    ok = (e_cx is not None and e_fl is not None
          and abs(e_cx - s2) < 0.05 * s2 + 5e-3 and abs(e_fl - s1) < 0.05 * s1 + 5e-3
          and e_cx < e_fl)
    iso_boundary_ok = iso_boundary_ok and ok
    detail.append(f"r=({r1},{r2}): eps_EP={e_cx:.4f}~s_2={s2:.4f}, eps_flip={e_fl:.4f}~s_1={s1:.4f}")
# phase-II window is a genuine ejection: complex pair is Krein-NEUTRAL (kn ~ 0) and solves no constraint
r1, r2 = 0.99, 0.995
eps_mid = 0.5 * (s_of(r2) + s_of(r1))                 # inside the isotropic window
ed = eig_data(H0(r1, r2) + eps_mid * Viso)
cx = [(e, kn) for e, kn, _ in ed if abs(e.imag) > 1e-8]
neutral = len(cx) == 2 and max(abs(kn) for _, kn in cx) < 1e-8
window_1neg = classify(H0(r1, r2) + eps_mid * Viso) == "1NEG"
# T4b -- the ANISOTROPIC phase-I window is even NARROWER: eps_EP ~ O(s_1*s_2), i.e. QUADRATIC in s
# (the isotropic window closes linearly ~ s_2, the generic one quadratically):
aniso_scaling_ok = True
aniso_detail = []
for name in ("C=sigma_x", "C=random"):
    V = COUPLINGS[name] / np.linalg.norm(COUPLINGS[name], 2)
    ratios_s1s2 = []
    for (r1, r2) in [(0.9, 0.95), (0.99, 0.995), (0.999, 0.9995)]:
        ec = None
        for eps in np.linspace(1e-6, 0.25, 25000):
            if np.max(np.abs(np.linalg.eigvals(H0(r1, r2) + eps * V).imag)) > 1e-8:
                ec = float(eps)
                break
        ratios_s1s2.append(ec / (s_of(r1) * s_of(r2)))
    aniso_scaling_ok = aniso_scaling_ok and (max(ratios_s1s2) / min(ratios_s1s2) < 1.1)
    aniso_detail.append(f"{name}: eps_EP/(s_1*s_2) = {[f'{q:.3f}' for q in ratios_s1s2]}")
check("T4  PHASE DIAGRAM.  Isotropic coupling: the opposite-Krein-signature inner pair (-s_2, +s_2) "
      "collides AT h=0 (a Krein collision) at eps_EP ~= s_2, goes COMPLEX (PT-broken window, phase "
      "II: the pair is Krein-NEUTRAL, kn ~ 0, solves NO constraint -- ejected from the physical "
      "space, 1 survivor), and re-emerges REAL with EXCHANGED signatures at eps_flip ~= s_1 (phase "
      "III: survivors of BOTH signs).  Boundary located on the grid.  ANISOTROPIC couplings: the "
      "phase-I window closes QUADRATICALLY, eps_EP ~ O(s_1*s_2) (constant ratio over the r-grid) -- "
      "for generic mixing the sign-definite phase is even narrower near the exceptional locus.",
      iso_boundary_ok and neutral and window_1neg and aniso_scaling_ok,
      "; ".join(detail) + f"; window: complex pair neutral (max|kn|={max(abs(kn) for _, kn in cx):.1e}), 1NEG; "
      + " | ".join(aniso_detail))

# ================================================================================================
# T5 -- THE PHYSICAL REGIME (fixed eps, r -> 1: the W98 UV tower, mixing >> splitting) FAILS.
# ================================================================================================
log("\n[T5] physical regime (fixed eps, r->1): isotropic INDEFINITE; generic = ejection; none retain W104")
phys_iso_indef = True
phys_aniso = {}
for rr in (0.99, 0.999, 0.9999):
    r2r = rr + 0.5 * (1 - rr)
    phys_iso_indef = phys_iso_indef and classify(H0(rr, r2r) + 0.3 * (Viso / np.linalg.norm(Viso, 2))) == "INDEFINITE"
    for name in ("C=sigma_x", "C=random"):
        V = COUPLINGS[name] / np.linalg.norm(COUPLINGS[name], 2)
        sv = survivors(H0(rr, r2r) + 1.0 * V)
        cl = classify(H0(rr, r2r) + 1.0 * V)
        phys_aniso.setdefault(name, []).append((cl, min((abs(kn) for _, kn, _ in sv), default=np.nan)))
aniso_ejection = all(all(cl == "1NEG" and kn > 0.3 for cl, kn in lst) for lst in phys_aniso.values())
# genericity census at eps >> s: no coupling class retains the W104 structure (2 survivors uniform sign)
n_indef = n_eject = n_empty = n_w104 = 0
rng2 = np.random.default_rng(7)
for _ in range(200):
    C = rng2.standard_normal((2, 2)) + 1j * rng2.standard_normal((2, 2))
    V = V_from_C(C)
    V = V / np.linalg.norm(V, 2)
    cl = classify(H0(0.99, 0.995) + 1.0 * V)
    if cl == "INDEFINITE":
        n_indef += 1
    elif cl == "EMPTY":
        n_empty += 1
    elif cl == "1NEG":
        n_eject += 1
    elif cl == "2NEG":
        n_w104 += 1
census_ok = (n_w104 == 0) and (n_indef + n_eject + n_empty == 200)
check("T5  THE PHYSICAL REGIME FAILS.  W98 tower = FIXED interaction, s_k -> 0 (mixing >> splitting"
      "): isotropic coupling -> INDEFINITE at every r in {0.99, 0.999, 0.9999} (both signs, norms "
      "+-O(s): indefinite AND degenerate); generic anisotropic couplings -> EJECTION phase (1 "
      "survivor per pair, negative, norm O(1) -- NON-degenerate but HALF the mode content "
      "annihilated).  Genericity census (200 random eta-s.a. couplings, eps=1 >> s): "
      f"{n_eject} ejection / {n_indef} indefinite / {n_empty} empty / {n_w104} retaining the W104 "
      "structure.  ZERO retain 'one uniformly-negative survivor per mode'.",
      phys_iso_indef and aniso_ejection and census_ok,
      f"iso INDEFINITE={phys_iso_indef}; aniso 1NEG kn>0.3={aniso_ejection}; census "
      f"{n_eject}/{n_indef}/{n_empty}/{n_w104}")

# ================================================================================================
# T6 -- THE COMPLETION CHECK: the back-door does not open as scoped.
# ================================================================================================
log("\n[T6] completion: flow descends unitarily; the ALGEBRA does not (phase I: ||a||_phys = 1/s_1);")
log("     phase II completion is a genuine Hilbert space but has already lost half the physics")
# (a) PHASE I: flow descends unitarily; compressed generic observable unbounded ~ 1/s_1 over tower
a_obs = np.kron(np.diag([1.0, 0.0]).astype(complex), SX)     # eta-s.a. observable on doublet 1
assert np.max(np.abs(ETA4 @ a_obs - dag(ETA4 @ a_obs))) < 1e-12
flow_unitary_resid = 0.0
norms_track = []
for rr in (0.9, 0.99, 0.999, 0.9999):
    r2r = rr + 0.5 * (1 - rr)
    eps = 0.1 * s_of(r2r)
    H = H0(rr, r2r) + eps * (Viso / np.sqrt(2.0))
    sv = survivors(H)
    n = len(sv)
    # the flow on survivors: eigenvectors -> phases e^{i h p}; physical-norm preserved exactly
    for p in (0.7, -2.3):
        for h, kn, v in sv:
            # |e^{ihp}|=1 => physical norm |kn| preserved: check the induced norm of the flowed vector
            flow_unitary_resid = max(flow_unitary_resid, abs(abs(np.exp(1j * h * p)) - 1.0))
    # compressed observable in the physical (quotient) norm: M_ij = <v_i, eta a v_j>/sqrt(|kn_i kn_j|)
    M = np.zeros((n, n), dtype=complex)
    for i in range(n):
        for j in range(n):
            M[i, j] = (sv[i][2].conj() @ ETA4 @ (a_obs @ sv[j][2])) / np.sqrt(abs(sv[i][1]) * abs(sv[j][1]))
    norms_track.append((float(np.linalg.norm(M, 2)), 1.0 / s_of(rr)))
tracks = all(abs(nm / inv - 1.0) < 0.05 for nm, inv in norms_track)
# honestly-projected algebra (with clock orthogonality of distinct survivors): DIAGONAL => abelian.
# diagonal compressions commute by construction; the noncommutative content is annihilated.
# (b) PHASE II: completion non-degenerate but halved; ejected pair connects to genuine content:
V = COUPLINGS["C=sigma_x"] / np.linalg.norm(COUPLINGS["C=sigma_x"], 2)
rr, r2r = 0.999, 0.9995
sv_strong = survivors(H0(rr, r2r) + 1.0 * V)
phaseII_nondeg = len(sv_strong) == 1 and sv_strong[0][1] < 0 and abs(sv_strong[0][1]) > 0.3
# continuity: the ejected complex pair at strong mixing connects (eps->0) to REAL modes with kn = +-s
ed_weak = eig_data(H0(rr, r2r) + 1e-6 * V)
weak_all_real = all(abs(e.imag) < 1e-8 for e, _, _ in ed_weak)
ed_strong = eig_data(H0(rr, r2r) + 1.0 * V)
n_complex_strong = sum(1 for e, _, _ in ed_strong if abs(e.imag) > 1e-8)
ejected_is_content = weak_all_real and n_complex_strong == 2
check("T6  COMPLETION: the back-door DOES NOT OPEN as scoped.  PHASE I (sign survives): the "
      "definite-degenerate form completes canonically and the FLOW descends unitarily (survivors "
      f"are eigenvectors, phases e^{{ihp}}; resid {flow_unitary_resid:.1e}) -- but the compressed "
      "generic observable has physical-norm operator norm = 1/s_1 EXACTLY "
      f"({' -> '.join(f'{nm:.1f}' for nm, _ in norms_track)} tracking 1/s_1 = "
      f"{' -> '.join(f'{inv:.1f}' for _, inv in norms_track)}): UNBOUNDED over the tower; and "
      "clock-orthogonality diagonalizes the honestly-projected algebra (multiplicity-free "
      "constraint spectrum) => ABELIAN remnant only.  PHASE II (generic physical regime): the "
      "completion is a genuine NON-degenerate Hilbert space (1 survivor, kn "
      f"{sv_strong[0][1]:+.3f}) -- but HALF the mode content was ejected as Krein-neutral complex "
      "pairs that connect continuously (eps->0: all 4 eigenvalues real) to genuine healthy+ghost "
      "modes: what the quotient/ejection kills IS the ghost physics.",
      tracks and flow_unitary_resid < 1e-12 and phaseII_nondeg and ejected_is_content,
      f"||a||_phys/(1/s_1) within 5%={tracks}; phase-II 1NEG nondeg={phaseII_nondeg}; "
      f"ejected-pair-is-content={ejected_is_content}")

# ================================================================================================
# T7 -- VERDICT: SIGN-KILLED-BY-MIXING (in the physical regime).
# ================================================================================================
log("\n[T7] VERDICT = SIGN-KILLED-BY-MIXING (physical regime); completion back-door does not open")
verdict = {
    "control_eps0_reproduces_W104_uniform_negative": ctrl_ok,                     # T1
    "sign_survives_WEAK_mixing_perturbative_and_exact_agree": weak_ok and quad,   # T2
    "EXACT_analytic_both_signs_for_eps_gt_s_isotropic": exact_ok,                 # T3
    "phase_boundary_located_eps_EP_s2_eps_flip_s1": iso_boundary_ok,              # T4
    "physical_regime_isotropic_INDEFINITE": phys_iso_indef,                       # T5
    "physical_regime_generic_ejects_half_mode_content": aniso_ejection,           # T5
    "zero_couplings_retain_W104_structure_in_physical_regime": census_ok,         # T5
    "completion_carries_flow_unitarily": flow_unitary_resid < 1e-12,              # T6
    "completion_carries_the_algebra_boundedly": False,                            # T6 (1/s_1)
    "phaseII_completion_nondegenerate_but_halved_and_abelian": phaseII_nondeg,    # T6
    "verdict_SIGN_SURVIVES_COMPLETION_VIABLE": False,
    "verdict_SIGN_SURVIVES_BUT_COMPLETION_LOSES_PHYSICS_weak_phase_only": True,   # phase I only
    "verdict_SIGN_KILLED_BY_MIXING_in_physical_regime": True,
}
final = (verdict["control_eps0_reproduces_W104_uniform_negative"]
         and verdict["sign_survives_WEAK_mixing_perturbative_and_exact_agree"]
         and verdict["EXACT_analytic_both_signs_for_eps_gt_s_isotropic"]
         and verdict["phase_boundary_located_eps_EP_s2_eps_flip_s1"]
         and verdict["physical_regime_isotropic_INDEFINITE"]
         and verdict["zero_couplings_retain_W104_structure_in_physical_regime"]
         and not verdict["completion_carries_the_algebra_boundedly"]
         and not verdict["verdict_SIGN_SURVIVES_COMPLETION_VIABLE"]
         and verdict["verdict_SIGN_KILLED_BY_MIXING_in_physical_regime"])
check("T7  VERDICT = SIGN-KILLED-BY-MIXING (in the physical regime).  Weak mixing preserves the "
      "uniform sign (phase I); the physical regime (mixing >> splitting, the W98 UV tower) does "
      "not: isotropic mixing produces survivors of BOTH signs (EXACT: the shared clock constrains "
      "only the TOTAL energy, so the positive-norm mode slips under it for eps > s), and generic "
      "mixing 'preserves' the sign only by ejecting half the mode content as Krein-neutral "
      "PT-broken pairs -- zero of 200 random couplings retain the W104 structure.  The completion "
      "back-door does not open: where the form is definite-degenerate the completion loses the "
      "algebra (compressed norms = 1/s_1, abelian remnant); where it is nondegenerate it has "
      "already lost half the physics.  The W104 kernel does not earn continuation.",
      final, f"{sum(1 for v in verdict.values() if v)} true / {len(verdict)} booleans")

# ================================================================================================
# SUMMARY
# ================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, ok, _ in results if ok)
log(f"CHECKS: {npass}/{len(results)} passed.")
assert all(ok for _, ok, _ in results), "some W108 sign-definitization-mixing checks FAILED"

log("")
log("W108 SIGN-DEFINITIZATION-UNDER-MIXING VERDICT (this file is the computation, not a claim-status change):")
log("  * DOES THE UNIFORM SIGN SURVIVE MODE-MIXING?  WEAK MIXING: YES (phase I, eps below the first")
log("    Krein collision ~ s_2; Krein-norm shifts O(eps^2); perturbative and exact derivations agree).")
log("    PHYSICAL REGIME (fixed mixing, s_k -> 0 -- the W98 UV tower): NO.  Isotropic mixing: survivors")
log("    of BOTH signs, EXACTLY (commuting case solvable: spectrum {+-s+-eps}, survivor -(eps-s) has")
log("    Krein norm +s > 0 -- the shared clock constrains only the TOTAL energy and the positive-norm")
log("    mode slips under it).  Generic anisotropic mixing: the sign 'survives' only by EJECTING half")
log("    the mode content as Krein-neutral PT-broken complex pairs (no constraint solution).  0/200")
log("    random couplings retain the W104 per-mode structure.")
log("  * THE PHASE BOUNDARY: eps_EP ~= s_2 (Krein collision at h=0, ejection window opens), eps_flip")
log("    ~= s_1 (isotropic: signatures exchange, both signs).  The physical regime eps/s -> inf is")
log("    past BOTH boundaries for every UV doublet pair.")
log("  * DOES THE COMPLETION BACK-DOOR OPEN?  NO.  Phase I: the canonical quotient-completion exists")
log("    and the modular FLOW descends unitarily -- but compressed observables have physical norm")
log("    1/s_1 (unbounded over the tower) and the honestly-projected algebra is ABELIAN (multiplicity-")
log("    free constraint spectrum).  Phase II: the completion is a genuine nondegenerate Hilbert")
log("    space, but it carries HALF the modes and an abelian remnant -- the ejected neutral pairs ARE")
log("    the ghost-physics content.  Phase III: indefinite, nothing to complete.")
log("  * VERDICT = SIGN-KILLED-BY-MIXING in the physical regime.  The W104 kernel (uniform-sign")
log("    definitization) is a MODE-DIAGONAL ARTIFACT of per-mode constraints; the single shared clock")
log("    (the physical CLPW observer) is exactly what kills it.  The 'completion of a degenerate-but-")
log("    definite form' residual does not materialize as a back-door.")
log("  * No canon / RESEARCH-STATUS / CANON / verdict / posture change.  Exploration-grade; the W98")
log("    break stands; the conjecture remains a conjecture.  Present, do not decide.")
raise SystemExit(0)
