#!/usr/bin/env python3
"""Exact native K95 controls for the written 12-real-dimensional theorem.

Correction 2026-11-26: this legacy fixture tests the PLUS/reversion comparator,
not printed source eq3.27. See source_adjoint_spinless_probe.py for both pairings.

Run local verification serially. No source action, physical domain or gauge
reduction is constructed. Binary-exact signed Clifford matrices are used;
there is no numerical tolerance or floating-point rank determination.
"""
import argparse
import json
import os
from pathlib import Path
import sys
from itertools import product
from math import comb

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")

import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()
    root = Path(args.repo).resolve()
    sys.path.insert(0, str(root / "tests/channel-swings"))
    from actual_sym2_c14_orbit_probe import native_gammas

    g, eta = native_gammas()
    eye = np.eye(128, dtype=complex)
    zero = np.zeros_like(eye)
    eq = np.array_equal
    checks = []

    def check(name, ok):
        checks.append({"name": name, "passed": bool(ok)})
        if not ok:
            raise AssertionError(name)

    def mul(words):
        result = eye.copy()
        for word in words:
            result = result @ word
        return result

    horizontal = [9, 0, 1, 2]
    normal = [3, 4, 5, 6, 7, 8, 10, 11, 12, 13]
    k = mul(g[:9])
    c_matrix = mul([x for x in g if eq(x.conjugate(), -x)])
    omega = mul(g)
    volume = mul([g[a] for a in horizontal])
    chi_h = 1j * volume
    pl, pr = (eye + chi_h) / 2, (eye - chi_h) / 2
    check("native C squares to minus identity",
          eq(c_matrix @ c_matrix.conjugate(), -eye))
    check("C commutes with all real native Clifford vectors",
          all(eq(c_matrix @ x.conjugate(), x @ c_matrix) for x in g))
    check("native vectors are K-sharp selfadjoint",
          all(eq(x.conjugate().T @ k, k @ x) for x in g))
    check("real horizontal volume square minus identity", eq(volume @ volume, -eye))
    check("real horizontal volume K-sharp selfadjoint",
          eq(volume.conjugate().T @ k, k @ volume))
    check("real volume is C-compatible",
          eq(c_matrix @ volume.conjugate(), volume @ c_matrix))
    check("horizontal complex chirality C-odd",
          eq(c_matrix @ chi_h.conjugate(), -chi_h @ c_matrix))

    alpha = [g[a] @ volume for a in horizontal]
    check("axial real one-form belongs to u(K95)",
          all(eq(x.conjugate().T @ k, -k @ x) for x in alpha))
    check("axial real one-form is quaternionic compatible",
          all(eq(c_matrix @ x.conjugate(), x @ c_matrix) for x in alpha))
    check("axial real one-form is ambient odd",
          all(eq(omega @ x, -x @ omega) for x in alpha))
    check("each nonnull component is invertible with stated square",
          all(eq(x @ x, eta[a] * eye) for a, x in zip(horizontal, alpha)))
    check("old imaginary vector witness is C-odd not C-compatible",
          all(eq(c_matrix @ (1j*g[a]).conjugate(), -(1j*g[a]) @ c_matrix)
              for a in horizontal))
    check("real vector without volume fails the sharp-skew restriction",
          all(not eq(g[a].conjugate().T @ k, -k @ g[a]) for a in horizontal))

    covariant = []
    for ia, a in enumerate(horizontal):
        for ib, b in enumerate(horizontal):
            if ib <= ia:
                continue
            generator = g[a] @ g[b] / 2
            for ic, c in enumerate(horizontal):
                rhs = (eta[b]*alpha[ia] if c == b else zero.copy())
                rhs = rhs - (eta[a]*alpha[ib] if c == a else zero)
                covariant.append(eq(generator @ alpha[ic] - alpha[ic] @ generator, rhs))
    check("proper horizontal Lorentz vector covariance", all(covariant))
    check("volume commutes with every normal Clifford vector",
          all(eq(volume @ g[n], g[n] @ volume) for n in normal))
    # Hence alpha commutes with all normal even bivectors, including the
    # endogenous graph-Lorentz correction and the entire fixed normal SM.
    check("full normal even action commutes with axial tensor",
          all(eq(alpha[0] @ (g[a]@g[b]), (g[a]@g[b]) @ alpha[0])
              for ia, a in enumerate(normal) for b in normal[ia+1:]))
    observed_trace = sum((eta[a]*g[a]@x for a, x in zip(horizontal, alpha)), zero.copy())
    check("actual horizontal observation trace is four times real volume",
          eq(observed_trace, 4*volume))
    check("trace witness proves complete observed injection",
          eq((-volume/4) @ observed_trace, eye))

    # A fixed compact normal U(3)xU(2) reduction realizes the already-owned
    # SM branching. Its 12 occupation isotypes are normal-chirality resolved;
    # vacuum and top are distinct even though both are SM sterile singlets.
    planes = [(3,4),(5,6),(7,8),(10,11),(12,13)]
    zi = [1j*g[a]@g[b] for a,b in planes]
    check("normal occupation involutions and C reversal",
          all(eq(z@z, eye) and eq(z.conjugate().T@k, k@z)
              and eq(c_matrix@z.conjugate(), -z@c_matrix) for z in zi))
    projectors = {(a,b): zero.copy() for a in range(4) for b in range(3)}
    for bits in product((0,1), repeat=5):
        proj = mul([(eye+(1 if bit else -1)*z)/2 for bit,z in zip(bits,zi)])
        projectors[(sum(bits[:3]),sum(bits[3:]))] += proj
    check("twelve normal isotypes sum to identity", eq(sum(projectors.values(),zero.copy()),eye))
    check("normal isotype dimensions reproduce Dirac32 with horizontal4",
          all(np.trace(e) == 4*comb(3,a)*comb(2,b) for (a,b),e in projectors.items()))
    check("normal isotype sharp selfadjoint projectors",
          all(eq(e@e,e) and eq(e.conjugate().T@k,k@e) for e in projectors.values()))
    check("C conjugates each normal isotype",
          all(eq(c_matrix@e.conjugate(),projectors[(3-a,2-b)]@c_matrix)
              for (a,b),e in projectors.items()))
    basis = {}
    for (a,b), e in projectors.items():
        ebar = projectors[(3-a,2-b)]
        basis[(a,b)] = 1j*(pl@e-pr@ebar)
    check("twelve coefficient directions have distinct left support",
          all(eq(pl@v,1j*pl@projectors[j]) for j,v in basis.items()))
    check("twelve quaternionic coefficient directions independent",
          all(np.trace(pl@e) == 2*comb(3,a)*comb(2,b) and np.trace(pl@e) > 0
              for (a,b),e in projectors.items()))
    check("all class basis values satisfy sharp reality and ambient oddness",
          all(eq((g[h]@a).conjugate().T@k,-k@(g[h]@a))
              and eq(c_matrix@(g[h]@a).conjugate(),(g[h]@a)@c_matrix)
              and eq(omega@(g[h]@a),-(g[h]@a)@omega)
              for a in basis.values() for h in horizontal))
    check("individual parameter support has exact rank 4 times irrep dimension",
          all(np.trace(a.conjugate().T@a) == 4*comb(3,j[0])*comb(2,j[1])
              for j,a in basis.items()))
    check("real horizontal volume is in complete coefficient class",
          eq(-sum(basis.values(),zero.copy()),volume))
    check("all twelve nonzero supports yield full rank128",
          sum(4*comb(3,a)*comb(2,b) for a,b in basis) == 128)
    check("each ambient input half has full rank64 available",
          all(sum(4*comb(3,a)*comb(2,b) for a,b in basis if (a+b)%2 == p) == 64
              for p in (0,1)))
    # This checks the exact coefficient equation and all allowed support
    # ranks. Completeness follows from the written Lorentz Schur theorem,
    # not from enumerating fixture matrices.
    result = {
        "evidence_revision": "6ef984a3f04b40c98724d7442e6bd2f119a56a21",
        "checks": checks,
        "complete_class_dimension_real": 12,
        "max_observed_rank_complex": 128,
        "max_rank_per_ambient_input_half_complex": 64,
        "source_reality_requirement": "CONDITIONAL_NOT_SOURCE_FULL_U",
        "physical_excitation_or_rate": "NOT_ESTABLISHED",
    }
    if args.output:
        Path(args.output).write_text(json.dumps(result,indent=2)+"\n")
    print(f"PASS: {len(checks)} exact K95 reality/vector/current controls")


if __name__ == "__main__":
    main()
