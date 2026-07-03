#!/usr/bin/env python3
r"""
INDEPENDENT verification of R4 Leg A (Spin(9,5) chiral-spinor Hom-vanishing),
written from scratch by the adversarial verifier -- deliberately using a
DIFFERENT method than the swing agent's null-space linear algebra.

Method here: charge-conjugation matrices.

For a complex Clifford algebra with generators g_a (a=0..n-1, n=2r even), an
so-invariant bilinear form on the Dirac spinor is a matrix C obeying
    sigma_ab^T C + C sigma_ab = 0  for all sigma_ab = 1/4[g_a,g_b].
This is satisfied exactly by the charge-conjugation matrices C with
    g_a^T C = eps * C g_a     (eps = +1 or -1),
because then sigma_ab^T C = -C sigma_ab (eps^2 = 1).  We FIND those C directly
by solving g_a^T C = eps C g_a as a small linear system, then measure chirality:

    omega = g_0 ... g_{n-1}   (chirality operator)
    omega^T C = eps^n (-1)^{n(n-1)/2} C omega.

C pairs SAME chirality  (S^+ with S^+)  iff  omega^T C = + C omega.
C pairs OPPOSITE chirality (S^+ with S^-) iff omega^T C = - C omega.

So the same-chirality invariant count is governed purely by the sign
    kappa(eps,n) = eps^n * (-1)^{n(n-1)/2}.
For n even, eps^n = 1, so kappa = (-1)^{n(n-1)/2}, INDEPENDENT of eps.
  n=14: (-1)^{14*13/2} = (-1)^91 = -1  => BOTH C flip chirality
        => dim Hom(S^+ x S^+, triv) = 0.  (the claim)

We CONFIRM this three ways, all independent of the swing agent's script:
  (1) analytic sign kappa for r=2..8;
  (2) explicit small-dim numerics (r=1..5) building C by nullspace and checking
      its actual chirality commutation numerically -- a real matrix computation,
      independent gamma build (pure recursive Pauli, no signature games, complex
      Cl(n,C) so it is basis/signature-agnostic);
  (3) exact duality count from rep theory: half-spin S^+ is self-dual iff r even,
      dual to S^- iff r odd => (Hom++,Hom+-) = (1,0) if r even, (0,1) if r odd.
All three must agree.  Exit 0 on success.
"""
import itertools
import numpy as np

s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def gammas_complex(r):
    """2r Euclidean gammas of Cl(2r, C), pure recursive Pauli doubling.
    Different from BOTH swing-agent builders in ordering/recursion."""
    if r == 1:
        return [s1, s2]
    sub = gammas_complex(r - 1)
    d = sub[0].shape[0]
    Id = np.eye(d, dtype=complex)
    out = [np.kron(g, s3) for g in sub]        # note kron order swapped vs agent
    out.append(np.kron(Id, s1))
    out.append(np.kron(Id, s2))
    return out


def find_C(gammas, eps, tol=1e-9):
    """Solve g_a^T C = eps C g_a for all a. Return (dim of solution space, a basis C)."""
    n = len(gammas)
    d = gammas[0].shape[0]
    D = d * d
    # vec(C): constraint g^T C - eps C g = 0  ->  (I kron g^T) vec(C) - eps (g^T kron I) vec(C)
    # using vec(AXB) = (B^T kron A) vec(X):  g^T C I -> (I kron g^T) vec(C); C g = I C g -> (g^T kron I) vec(C)
    rows = []
    for g in gammas:
        M = np.kron(np.eye(d), g.T) - eps * np.kron(g.T, np.eye(d))
        rows.append(M)
    A = np.vstack(rows)
    # nullspace via SVD
    u, sv, vh = np.linalg.svd(A)
    ns = vh[sv.shape[0] - np.sum(sv < tol * max(sv.max(), 1.0)):].conj().T if False else None
    ndim = int(np.sum(sv < tol * max(sv[0], 1.0)))
    # get a nullspace vector
    Cbasis = []
    V = vh.conj().T
    for j in range(V.shape[1] - ndim, V.shape[1]):
        Cbasis.append(V[:, j].reshape(d, d))
    return ndim, Cbasis


def chirality_op(gammas):
    om = np.eye(gammas[0].shape[0], dtype=complex)
    for g in gammas:
        om = om @ g
    # normalize so omega^2 = I
    sq = (om @ om)[0, 0]
    return om / np.sqrt(complex(sq))


def analytic_kappa(n):
    # eps^n * (-1)^{n(n-1)/2}; n even => eps^n=1
    return (-1) ** ((n * (n - 1) // 2) % 2)


def duality_count(r):
    """rep theory: (dim Hom(S+xS+,triv), dim Hom(S+xS-,triv))."""
    if r % 2 == 0:
        return (1, 0)     # S+ self-dual
    else:
        return (0, 1)     # S+ dual to S-


print("=" * 74)
print("INDEPENDENT R4 Leg A verification (charge-conjugation method)")
print("=" * 74)

print("\n(1) Analytic same-chirality sign kappa = eps^n (-1)^{n(n-1)/2}, n=2r:")
for r in range(2, 9):
    n = 2 * r
    k = analytic_kappa(n)
    same_allowed = (k == 1)
    print(f"    r={r} (n={n}): kappa={k:+d}  -> same-chirality pairing "
          f"{'ALLOWED (r even, self-dual)' if same_allowed else 'FORBIDDEN (Hom++=0)'}")
    # cross check against parity of r
    assert (k == 1) == (r % 2 == 0), (r, k)
print("    r=7 (n=14): kappa = -1  => dim Hom(S+ x S+, triv) = 0  [Spin(9,5)/Spin(7,7)]")
assert analytic_kappa(14) == -1

print("\n(2) Explicit small-dim numerics: build C, check its chirality commutation:")
for r in range(1, 6):
    n = 2 * r
    G = gammas_complex(r)
    om = chirality_op(G)
    # verify Clifford
    d = G[0].shape[0]
    resid = max(np.linalg.norm(G[a] @ G[b] + G[b] @ G[a] - (2 if a == b else 0) * np.eye(d))
                for a in range(n) for b in range(n))
    same_forms = 0
    cross_forms = 0
    for eps in (+1, -1):
        nd, Cs = find_C(G, eps)
        for C in Cs:
            # same chirality iff omega^T C = + C omega
            lhs = om.T @ C
            plus = np.linalg.norm(lhs - C @ om)
            minus = np.linalg.norm(lhs + C @ om)
            if plus < 1e-6 * max(np.linalg.norm(C), 1):
                same_forms += 1
            elif minus < 1e-6 * max(np.linalg.norm(C), 1):
                cross_forms += 1
    # each of S+xS+ and S+xS- pairing space is at most 1-dim; C_+ and C_- may
    # give proportional restrictions, so collapse counts to 0/1 booleans:
    same_dim = 1 if same_forms > 0 else 0
    cross_dim = 1 if cross_forms > 0 else 0
    expect = duality_count(r)
    print(f"    r={r} (n={n}, spinor {d}): Cliff-resid={resid:.1e}; "
          f"found C same-chir={same_forms}, cross-chir={cross_forms} "
          f"-> (Hom++,Hom+-)=({same_dim},{cross_dim}) expect {expect}")
    assert (same_dim, cross_dim) == expect, (r, same_dim, cross_dim, expect)

print("\n(3) rep-theory duality count vs analytic sign -- must agree for all r:")
for r in range(2, 9):
    hpp = 1 if analytic_kappa(2 * r) == 1 else 0
    assert hpp == duality_count(r)[0], r
    print(f"    r={r}: analytic Hom++={hpp}, duality Hom++={duality_count(r)[0]}  OK")

print("\n" + "#" * 74)
print("# INDEPENDENT VERDICT: dim Hom_so(9,5)(S+ x S+, triv) = 0 confirmed by")
print("#   (1) analytic charge-conjugation sign, (2) explicit numerics r=1..5,")
print("#   (3) half-spin duality (r odd). r=7 (n=14) is ODD => forbidden. exit 0.")
print("#" * 74)
