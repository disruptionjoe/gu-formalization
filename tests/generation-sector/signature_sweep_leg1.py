#!/usr/bin/env python3
"""LEG 1 - signature sweep: is the generation-multiplicity obstruction UNIVERSAL across Cl(p,q),
p+q=14, or only the (9,5)+(7,7) pair already tested?

For each signature we recompute, with NO target import:
  (a) C-04: the native dimension spectrum {spinor, RS vector, RS space, ker(Gamma), rank Gamma}
      and its prime factorization -- is the prime 3 ABSENT and the spectrum {2,7,13}-flavored?
  (b) C-05: a sample of METRIC connections (self-dual su(2)_+, generic so(p,q), random so(p,q),
      enveloping products) -- do they all give grading index 0?
  (c) the parity J^2 sign (real M(n,R) class => +1, quaternionic M(n,H) class => -1), confirming
      the module class predicted by (p-q) mod 8.
  plus the anchors bare ||[Pi,M_D]||, C2 ||Gamma M_D Pi||.

BREAK CONDITIONS (if any fires for a defensible signature, the Multiplicity Theorem dies there):
  * the prime 3 APPEARS in the native dimension spectrum, OR
  * a metric connection gives a NONZERO or ODD grading index.

Run: python tests/generation-sector/signature_sweep_leg1.py
"""
from __future__ import annotations

import itertools

import numpy as np

N = 14
DIM = 128  # 2^7, fixed by 14 = 2*7 gammas -> Cl(p,q) complexification is M(128,C)
XI = np.array([1, 2, 3, 4, 0.5, 1.5, 2.5, 0.7, 1.1, 0.3, 2.2, 1.7, 0.9, 1.3], dtype=complex)


def jw(n):
    """Jordan-Wigner: 2n Hermitian gamma generators of the Euclidean Cl(2n)."""
    I = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    G = []
    for k in range(n):
        L = [s3] * k
        R = [I] * (n - 1 - k)

        def kr(ms):
            o = np.array([[1 + 0j]])
            for m in ms:
                o = np.kron(o, m)
            return o
        G.append(kr(L + [s1] + R))
        G.append(kr(L + [s2] + R))
    return G


_G7 = jw(7)  # 14 Hermitian generators, reused for every signature


def signature_clifford(p, q):
    """e_a for Cl(p,q): first p timelike (+1), then q spacelike (-1)."""
    assert p + q == N
    eta = np.array([1.0] * p + [-1.0] * q)
    e = [_G7[a] if eta[a] > 0 else 1j * _G7[a] for a in range(N)]
    return e, eta


def factorize(n):
    n = int(round(n))
    f = {}
    d = 2
    m = abs(n)
    while d * d <= m:
        while m % d == 0:
            f[d] = f.get(d, 0) + 1
            m //= d
        d += 1
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f


def fac_str(n):
    f = factorize(n)
    return " . ".join(f"{p}^{k}" if k > 1 else f"{p}" for p, k in sorted(f.items())) or "1"


def parity_J2(e, eta):
    """Project onto the Clifford supercommutant fixed point; J^2 sign = module-class invariant."""
    def Phi(U):
        out = np.zeros_like(U)
        for a in range(N):
            out += eta[a] * (e[a] @ U @ e[a].conj())
        return out / N
    rng = np.random.default_rng(1)
    U = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    for _ in range(400):
        U = 0.5 * (U + Phi(U))
        nrm = np.linalg.norm(U)
        if nrm < 1e-14:
            return 0.0
        U /= nrm
    Us, _, Vs = np.linalg.svd(U)
    U = Us @ Vs
    return float((np.trace(U @ U.conj()) / DIM).real)


def analyze(p, q):
    e, eta = signature_clifford(p, q)
    # Clifford-relation check
    cliff_err = max(
        np.linalg.norm(e[a] @ e[b] + e[b] @ e[a] - (2 * eta[a] if a == b else 0) * np.eye(DIM))
        for a in range(N) for b in range(N)
    )

    Gamma = np.hstack(e)
    Pi = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    Q = np.eye(N * DIM, dtype=complex) - Pi
    M_D = np.kron(np.eye(N), sum(XI[a] * e[a] for a in range(N)))
    bare = float(np.linalg.norm(Pi @ M_D - M_D @ Pi))
    C2 = float(np.linalg.norm(Gamma @ M_D @ Pi))

    rank_gamma = int(round(np.trace(Q).real))
    dimker = int(round(np.trace(Pi).real))

    # (a) C-04 native dimension spectrum
    dims = {
        "spinor S": DIM,
        "RS vector": N,
        "RS space": N * DIM,
        "ker(Gamma)": dimker,
        "rank Gamma": rank_gamma,
    }
    all_primes = set()
    for v in dims.values():
        all_primes |= set(factorize(v).keys())
    three_absent = 3 not in all_primes

    # (c) parity / module class
    j2 = parity_J2(e, eta)
    pmq = (p - q) % 8
    predicted = "R" if pmq in (0, 2) else ("H" if pmq in (4, 6) else "C/other")

    # (b) C-05 metric connection indices
    def sig(A):
        ev = np.linalg.eigvalsh(0.5 * (A + A.conj().T))
        tol = 1e-7 * max(np.abs(ev).max(), 1e-30)
        return int((ev > tol).sum()) - int((ev < -tol).sum())

    def gd(X):
        return Pi @ X @ Pi + Q @ X @ Q

    def herm(X):
        return 0.5 * (X + X.conj().T)

    def Mvec(i, j):
        M = np.zeros((N, N), dtype=complex)
        M[i, j] = eta[j]
        M[j, i] = -eta[i]
        return M

    def sigma(i, j):
        return 0.25 * (e[i] @ e[j] - e[j] @ e[i])

    def Jfull(i, j):
        return np.kron(Mvec(i, j), np.eye(DIM)) + np.kron(np.eye(N), sigma(i, j))

    def conn_index(J):
        return sig(herm(gd(1j * J)))

    # self-dual su(2)_+ over Euclidean 4-frame {0,1,2,3} (the natural geometric "3")
    SDp = [Jfull(0, 1) + Jfull(2, 3), Jfull(0, 2) + Jfull(3, 1), Jfull(0, 3) + Jfull(1, 2)]
    sd = [conn_index(J) for J in SDp]
    # generic so(p,q) and enveloping products
    pairs = list(itertools.combinations(range(N), 2))
    Js = [Jfull(i, j) for i, j in pairs]
    rng = np.random.default_rng(3)
    alg = [conn_index(sum(c * Js[i] for i, c in enumerate(rng.standard_normal(len(Js))))) for _ in range(3)]
    quad = [conn_index(Js[rng.integers(len(Js))] @ Js[rng.integers(len(Js))]
                       + Js[rng.integers(len(Js))] @ Js[rng.integers(len(Js))]) for _ in range(2)]
    all_conn = sd + alg + quad
    conn_all_zero = all(v == 0 for v in all_conn)

    return {
        "p": p, "q": q, "pmq": pmq, "predicted": predicted, "j2": j2,
        "cliff_err": cliff_err, "bare": bare, "C2": C2,
        "dims": dims, "all_primes": sorted(all_primes), "three_absent": three_absent,
        "dimker_fac": fac_str(dimker), "sd": sd, "alg": alg, "quad": quad,
        "conn_all_zero": conn_all_zero,
    }


def main():
    # spanning set: residues (p-q) mod 8 in {0,2,4,6}, both real and quaternionic classes,
    # the requested (10,4)(5,9)(8,6)(11,3) plus (9,5)(7,7) controls plus extremes.
    sigs = [(14, 0), (13, 1), (11, 3), (10, 4), (9, 5), (8, 6),
            (7, 7), (6, 8), (5, 9), (4, 10)]
    rows = []
    print("=" * 110)
    print(f"{'sig':>7} {'p-q%8':>5} {'cls':>3} {'J^2':>6} {'class?':>7} "
          f"{'ker(Gamma)':>14} {'3?':>4} {'primes':>12} {'selfdual':>10} {'so(p,q)':>14} {'idx0?':>6}")
    print("-" * 110)
    break_hits = []
    for p, q in sigs:
        r = analyze(p, q)
        rows.append(r)
        cls_ok = (r["predicted"] == "R" and r["j2"] > 0) or (r["predicted"] == "H" and r["j2"] < 0)
        three_str = "ABS" if r["three_absent"] else "HAS3!"
        idx_str = "yes" if r["conn_all_zero"] else "NO!"
        print(f"({r['p']:>2},{r['q']:>2}) {r['pmq']:>5} {r['predicted']:>3} "
              f"{r['j2']:>+6.2f} {('OK' if cls_ok else 'MISMATCH'):>7} "
              f"{str(r['dims']['ker(Gamma)'])+'='+r['dimker_fac']:>14} {three_str:>4} "
              f"{str(r['all_primes']):>12} {str(r['sd']):>10} {str(r['alg']):>14} {idx_str:>6}")
        if not r["three_absent"]:
            break_hits.append((f"({p},{q})", "prime 3 in dimension spectrum"))
        if not r["conn_all_zero"]:
            break_hits.append((f"({p},{q})", f"nonzero/odd connection index sd={r['sd']} alg={r['alg']} quad={r['quad']}"))
    print("=" * 110)

    # universality checks
    all_three_absent = all(r["three_absent"] for r in rows)
    all_idx0 = all(r["conn_all_zero"] for r in rows)
    all_ker_same = len({r["dims"]["ker(Gamma)"] for r in rows}) == 1
    all_anchors_same = (max(abs(r["bare"] - rows[0]["bare"]) for r in rows) < 1e-2
                        and max(abs(r["C2"] - rows[0]["C2"]) for r in rows) < 1e-2)
    print(f"anchors (all signatures): bare={rows[0]['bare']:.4f}  C2={rows[0]['C2']:.4f}  "
          f"identical across signatures? {all_anchors_same}")
    print(f"ker(Gamma) identical across all signatures? {all_ker_same} "
          f"(= {rows[0]['dims']['ker(Gamma)']} = {rows[0]['dimker_fac']} in every case)")
    print(f"C-04: prime 3 ABSENT in EVERY signature? {all_three_absent}")
    print(f"C-05: every sampled metric connection gives index 0 in EVERY signature? {all_idx0}")
    print(f"max Clifford-relation error across all signatures: "
          f"{max(r['cliff_err'] for r in rows):.1e}")
    print()
    if break_hits:
        print("BREAK CONDITIONS FIRED:")
        for s, why in break_hits:
            print(f"  {s}: {why}")
    else:
        print("NO break condition fired: obstruction is UNIVERSAL across all 10 signatures / all module classes.")

    return rows, all_three_absent, all_idx0, break_hits


if __name__ == "__main__":
    main()
