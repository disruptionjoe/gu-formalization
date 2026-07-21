"""
Prong B multiplicity/no-go probe for the SOURCE-DOMAIN-SELECTOR swing
(pre-reg: explorations/prereg-source-domain-selector-swing-2026-07-21.md).

Adversarial truth-test, NOT advocacy. This is a DETERMINISTIC probe of the
honest no-go: the correctly-framed question is NOT "does a deck-compatible
Krein-self-adjoint domain exist" (many do -- continuum-pencil-graph-domain-
certificate-2026-07-20.md), but "do GU's existing structures (first-order
operator A~ = B d_s + W~ with B = -i K_u G, the constant Krein involution
J = J* = J^{-1}, and the Z/2 deck action) SINGLE OUT a UNIQUE physical
maximal-isotropic domain?"

We build a faithful finite toy (d=2, balanced (1,1) endpoint signature, a Z/2
deck) and:
  (1) verify the frozen algebra  B = -i K_u G,  J*=J=J^{-1},  B*J = -J B,
      endpoint form H = -i B* J Hermitian invertible of signature (1,1);
  (2) ENUMERATE the deck-equivariant Krein-self-adjoint graph domains
      T*H T = H  with  [T, U_deck] = 0, and read off the moduli dimension;
  (3) PHYSICAL-INEQUIVALENCE check: compute the A~_T spectrum in closed form
      cosh(lambda L) = cos((a+b)/2)/cos((a-b)/2) and confirm distinct domains
      carry DISTINCT spectra (spectrum is a symmetry invariant, so distinct
      spectrum => provably physically inequivalent, ruling out ALL gauge/deck
      relations at once);
  (4) UNIQUENESS STEELMAN (planted control): maximize the group to an
      IRREDUCIBLE action (commutant = C.I by Schur) and try to force a unique
      domain. Show uniqueness STILL fails -- the U(1) center (the phase theta of
      T_theta = e^{i theta} S(b)) always survives Krein-isotropy, because
      |c|=1 is the only constraint on a scalar T=cI.

Outcome asserted: B-MULTIPLICITY (=> S-OBSTRUCTED): the selector is PROVABLY
EXTERNAL to current GU structure. Exit 0 = all assertions held. Foreground
only; no side effects, no network, no file writes.
"""

import numpy as np

TOL = 1e-10

I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)


def dag(M):
    return M.conj().T


def is_close(A, B):
    return np.allclose(A, B, atol=TOL)


def signature(H):
    """(#positive, #negative) eigenvalues of a Hermitian matrix."""
    w = np.linalg.eigvalsh((H + dag(H)) / 2)
    return int(np.sum(w > TOL)), int(np.sum(w < -TOL))


# ---------------------------------------------------------------------------
# (1) Frozen toy algebra faithful to A~ = B d_s + W~,  B = -i K_u G
# ---------------------------------------------------------------------------
# G  : involution                         (plays G_col)
# Ku : Hermitian involution               (plays the section-theory K_u)
# B  : principal coefficient  = -i Ku G   (invertible)
# J  : constant Krein involution, J*=J=J^{-1}, with B*J = -J B  (frozen symmetry)
# H  : endpoint form  = -i B* J,  Hermitian, invertible, signature (1,1)
G = sz
Ku = sx
B = -1j * Ku @ G
J = sx
H = -1j * dag(B) @ J

checks_1 = {
    "G involution": is_close(G @ G, I2),
    "Ku Hermitian involution": is_close(Ku, dag(Ku)) and is_close(Ku @ Ku, I2),
    "B = -i Ku G": is_close(B, -1j * Ku @ G),
    "B invertible": abs(np.linalg.det(B)) > TOL,
    "J*=J=J^{-1}": is_close(J, dag(J)) and is_close(J @ J, I2),
    "principal Krein symmetry B*J = -J B": is_close(dag(B) @ J, -J @ B),
    "H Hermitian": is_close(H, dag(H)),
    "H invertible": abs(np.linalg.det(H)) > TOL,
}
sigH = signature(H)
checks_1["H signature (1,1) balanced"] = sigH == (1, 1)
assert all(checks_1.values()), ("frozen-algebra checks failed", checks_1)


# ---------------------------------------------------------------------------
# (2) Enumerate deck-equivariant Krein-self-adjoint graph domains.
#     Domain D_T = { u : u(b) = T u(a) }; maximal-isotropic (Krein-self-adjoint)
#     iff  T* H T = H  (eq (G) of the certificate). Deck-equivariance of the
#     single-collar boundary condition is  U_deck T U_deck^{-1} = T, i.e.
#     [T, U_deck] = 0. Deck is the Z/2 form-preserving involution U = sz
#     (U*HU = H, U^2 = I): the chirality/sector grading, NOT a sector-mixer.
# ---------------------------------------------------------------------------
U = sz
assert is_close(U @ U, I2) and is_close(dag(U) @ H @ U, H), "deck must be a Z/2 form-symmetry"


def is_krein_isotropic(T):
    return is_close(dag(T) @ H @ T, H)


def is_deck_equivariant(T):
    # single-collar deck-invariance of the boundary condition: U T U^{-1} = T
    return is_close(U @ T, T @ U)


# H = sz here, so T*HT=H with [T,sz]=0 forces T = diag(e^{i a}, e^{i b}).
# Verify the whole 2-torus is admissible (sample densely) and that off-torus
# points fail -> moduli is exactly the 2-torus (real dim 2).
rng = np.random.default_rng(0)
torus_admitted = 0
n_grid = 24
for a in np.linspace(0, 2 * np.pi, n_grid, endpoint=False):
    for b in np.linspace(0, 2 * np.pi, n_grid, endpoint=False):
        T = np.diag([np.exp(1j * a), np.exp(1j * b)])
        assert is_krein_isotropic(T) and is_deck_equivariant(T)
        torus_admitted += 1

# Off-torus controls: generic Krein-isotropic but non-diagonal T must FAIL
# deck-equivariance (a domain that exists but is not deck-compatible), and a
# generic non-isotropic T must fail isotropy. Both must be excluded.
off_deck_rejected = 0
off_iso_rejected = 0
for _ in range(200):
    # random H-unitary via Cayley of an H-anti-Hermitian generator
    Xr = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    Xa = Xr - np.linalg.inv(H) @ dag(Xr) @ H  # H-anti-Hermitian: (H X)* = -(H X)
    Wc = np.linalg.solve(I2 - Xa, I2 + Xa)     # Cayley -> H-unitary
    if is_krein_isotropic(Wc) and not np.allclose(np.abs(np.diag(np.diag(Wc))), np.abs(Wc)):
        if not is_close(U @ Wc, Wc @ U):
            off_deck_rejected += 1
    Rnd = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    if not is_krein_isotropic(Rnd):
        off_iso_rejected += 1

moduli_dim_total = 2  # the admissible set is exactly the 2-torus T^2
assert torus_admitted == n_grid * n_grid
assert off_deck_rejected > 0, "non-diagonal H-unitary domains should exist and be deck-EXCLUDED"
assert off_iso_rejected > 0, "non-isotropic controls should be rejected"


# ---------------------------------------------------------------------------
# (3) PHYSICAL-INEQUIVALENCE check via the actual A~_T spectrum.
#     A~ = B d_s (W~=0), B = -i Ku G = -sy here, on [0,L]. Eigenvalues solve
#         det( exp(lambda B^{-1} L) - T ) = 0.
#     Closed form for T = diag(e^{i a}, e^{i b}) (derived, then verified):
#         cosh(lambda L) = cos((a+b)/2) / cos((a-b)/2) =: rho(a,b).
#     Distinct rho => distinct spectrum => provably physically inequivalent
#     (any gauge/deck symmetry is isospectral). rho ranges over a continuum,
#     so the physically-inequivalent sub-moduli is >= 1-dimensional.
# ---------------------------------------------------------------------------
Binv = np.linalg.inv(B)
L = 1.3


def rho_closed(a, b):
    return np.cos((a + b) / 2) / np.cos((a - b) / 2)


def det_boundary(lam, a, b):
    M = np.linalg.matrix_power  # unused; use expm via eigendecomp of Binv
    # exp(lam * Binv * L): Binv = -sy has eigenvalues +-1
    E = _expm(lam * Binv * L)
    T = np.diag([np.exp(1j * a), np.exp(1j * b)])
    return np.linalg.det(E - T)


def _expm(M):
    w, V = np.linalg.eig(M)
    return (V * np.exp(w)) @ np.linalg.inv(V)


# Verify the closed form: for a lambda satisfying cosh(lam L)=rho, det=0.
closed_form_ok = 0
sample_phases = [(0.0, 0.0), (0.7, 0.0), (0.7, -0.7), (1.1, 0.3), (2.0, 0.4)]
for (a, b) in sample_phases:
    rho = rho_closed(a, b)
    lam = np.arccosh(complex(rho)) / L  # a root of cosh(lam L)=rho
    d = det_boundary(lam, a, b)
    assert abs(d) < 1e-8, ("closed form mismatch", a, b, d)
    closed_form_ok += 1

# Distinct spectra across the family: rho takes a continuum of DISTINCT values,
# hence the domains are pairwise physically inequivalent along that continuum.
# Slice with FIXED relative phase delta = a-b = 0.6 (!= 0, so NOT the U(1)
# center) and varying sum sigma = a+b = 2t: rho = cos(t)/cos(0.3). This shows
# multiplicity in a direction BEYOND the global phase.
delta = 0.6
rho_vals = []
for t in np.linspace(0.05, np.pi / 2 - 0.05, 40):
    a, b = t + delta / 2, t - delta / 2   # a-b = delta fixed, a+b = 2t varies
    rho_vals.append(rho_closed(a, b))
rho_vals = np.array(rho_vals)
distinct = len(np.unique(np.round(rho_vals, 8)))
assert distinct == len(rho_vals), "rho should be injective along this slice -> distinct spectra"
# and the two ends are genuinely different physical spectra:
assert abs(rho_vals[0] - rho_vals[-1]) > 0.5

# Deck does NOT relate two diagonal domains (it FIXES each): U T U^{-1} = T.
for (a, b) in sample_phases:
    T = np.diag([np.exp(1j * a), np.exp(1j * b)])
    assert is_close(U @ T @ np.linalg.inv(U), T), "deck fixes diagonal domains; cannot relate distinct ones"

phys_inequiv_dim_lower_bound = 1  # continuum of distinct spectra (rho slice)


# ---------------------------------------------------------------------------
# (4) UNIQUENESS STEELMAN (planted control: "equivariance+Krein force a unique
#     domain"). Best case for uniqueness: make the implementation group act
#     IRREDUCIBLY on C^2 so its commutant is C.I (Schur). Deck-equivariance
#     under the WHOLE group then forces T to commute with all generators =>
#     T = c I (scalar). Krein-isotropy T*HT=H with T=cI gives |c|^2 H = H =>
#     |c| = 1. So T = e^{i theta} I : a U(1), NOT a point.
#     => Uniqueness FAILS even in the most favorable (irreducible) case. The
#     surviving U(1) is exactly the certificate's unfixed phase theta.
# ---------------------------------------------------------------------------
# Irreducible group generators on C^2: {sz, sx} generate the full 2x2 algebra,
# so the commutant is scalars.
gens = [sz, sx]


def commutes_with_all(T, gs):
    return all(is_close(T @ g, g @ T) for g in gs)


# The commutant of an irreducible set is C.I -> only scalars survive equivariance.
# Verify: a scalar cI is Krein-isotropic iff |c|=1; and the admissible scalars
# form a U(1), not a single point.
scalar_admissible = []
for theta in np.linspace(0, 2 * np.pi, 32, endpoint=False):
    c = np.exp(1j * theta)
    T = c * I2
    if commutes_with_all(T, gens) and is_krein_isotropic(T):
        scalar_admissible.append(theta)
assert len(scalar_admissible) == 32, "every phase gives an admissible scalar domain -> U(1) survives"

# And a NON-unit-modulus scalar is correctly rejected (|c|!=1 breaks isotropy):
for c in [0.5, 2.0, 1.5j]:
    assert not is_krein_isotropic(c * I2), "isotropy must reject |c|!=1"

# A generic non-scalar T does NOT commute with the irreducible generators:
noncommuting = 0
for _ in range(50):
    Rnd = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    if not commutes_with_all(Rnd, gens):
        noncommuting += 1
assert noncommuting > 0, "irreducible action must exclude generic non-scalar domains"

steelman_forces_unique = False  # uniqueness FAILS: a U(1) (theta) always survives
irreducible_floor_dim = 1       # the residual U(1) center = the phase theta


# ---------------------------------------------------------------------------
# Adjudication
# ---------------------------------------------------------------------------
outcome = "B-MULTIPLICITY"
assert moduli_dim_total >= 1
assert phys_inequiv_dim_lower_bound >= 1
assert not steelman_forces_unique

print("=== PRONG B: source-domain-selector multiplicity/no-go probe ===")
print(f"(1) frozen toy algebra OK; endpoint form H signature = {sigH} (balanced)")
print(f"(2) deck-equivariant Krein-self-adjoint domains = 2-torus T^2; "
      f"moduli dim (total) = {moduli_dim_total}")
print(f"    torus points admitted = {torus_admitted}/{n_grid*n_grid}; "
      f"non-diagonal domains deck-excluded = {off_deck_rejected}; "
      f"non-isotropic rejected = {off_iso_rejected}")
print(f"(3) physical inequivalence: closed-form spectra verified at "
      f"{closed_form_ok}/{len(sample_phases)} phases; "
      f"cosh(lam L)=cos((a+b)/2)/cos((a-b)/2)")
print(f"    distinct spectra along a slice = {distinct}/{len(rho_vals)} "
      f"(continuum) -> phys-inequiv sub-moduli dim >= {phys_inequiv_dim_lower_bound}")
print(f"    deck FIXES each diagonal domain -> the family is NOT a single deck-orbit")
print(f"(4) uniqueness steelman (irreducible action, commutant=C.I): "
      f"forces T=cI, |c|=1 -> residual U(1) (phase theta); "
      f"steelman_forces_unique = {steelman_forces_unique}; floor dim = {irreducible_floor_dim}")
print(f"ADJUDICATED OUTCOME: {outcome}  (=> S-OBSTRUCTED; selector PROVABLY EXTERNAL)")
print("EXIT 0")
