#!/usr/bin/env python3
r"""
ADVERSARIAL REFUTATION: does the criticality verdict survive tracking the RIGHT object?

The construct's criticality script tracks lambda_net = trace(H(eps))/dim = MEAN of the whole
carrier spectrum. Its slope = trace(dB)/dim, which is 0 iff dB is traceless. The construct ITSELF
admits this is "largely re-encoded" (tracelessness = vectorlike-balance lemma).

But the genuine flat direction is NOT "the mean of the spectrum." B is non-degenerate (+96,-96,0):
it has NO zero eigenvalue. The flatness is a NULL DIRECTION of the indefinite form -- the balanced
occupancy vector occ = (upos+uneg)/||.|| with occ^dag B occ = 0. A proper criticality test asks
whether THAT direction's second variation moves: d/deps [ occ^dag H(eps) occ ] = occ^dag dB occ.
This is a single matrix element, NOT a trace -- it need not be protected by tracelessness.

If occ^dag dB occ is ALSO ~0 for the GU torsion -> protection is real.
If occ^dag dB occ is NONZERO for the GU torsion -> the "slope=0" verdict is an ARTIFACT of averaging
over the whole spectrum (trace/dim), and the actual flat direction DOES acquire curvature.

We also track the gentlest honest object: the smallest |eigenvalue| of H(eps) (the gap to the
null cone) and the most-negative/least-positive eigenvalue crossing.

Run: python tests/hessian-z3/adv_refute_flatdir_curvature.py
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import criticality_torsion_lambda_epsilon as C  # noqa: E402

N, DIM = C.N, C.DIM
herm = C.herm


def main():
    np.set_printoptions(precision=6, suppress=True, linewidth=160)
    print("=" * 92)
    print("ADVERSARIAL: flat-direction curvature occ^dag dB occ  vs  the construct's trace(dB)/dim")
    print("=" * 92)

    S = C.build_substrate()
    Wt, K, B = S["Wt"], S["K"], S["B"]
    evB, VB = np.linalg.eigh(B)
    Vpos = VB[:, evB > 1e-9]
    Vneg = VB[:, evB < -1e-9]
    print(f"carrier signature (+{Vpos.shape[1]}, -{Vneg.shape[1]}); min|eig(B)| = {np.min(np.abs(evB)):.3e} "
          f"(NO kernel: the 'zero' is a NULL DIRECTION, not an eigenvector)")

    # the genuine flat / occupancy direction (same construction as carrier_occupancy_hessian.py)
    upos = Vpos.sum(axis=1); upos /= np.linalg.norm(upos)
    uneg = Vneg.sum(axis=1); uneg /= np.linalg.norm(uneg)
    occ = (upos + uneg); occ /= np.linalg.norm(occ)
    print(f"occ^dag B occ (flat dir second variation at eps=0) = {float((occ.conj()@B@occ).real):+.3e} (null)")

    thetas = C.torsion_operators(S)
    print("\n" + "-" * 92)
    print(f"  {'torsion':<16}{'trace(dB)/dim':>16}{'occ^dag dB occ':>18}{'<v dB v> rand-null':>22}{'min|eig| slope':>16}")
    print("-" * 92)
    rng = np.random.default_rng(0)
    for name, th in thetas.items():
        dH = herm(K @ th)
        dB = herm(Wt.conj().T @ dH @ Wt)
        nrm = np.linalg.norm(dB)
        if nrm > 1e-30:
            dB = dB / nrm
        trace_slope = float(np.trace(dB).real) / dB.shape[0]
        flat_slope = float((occ.conj() @ dB @ occ).real)
        # robustness: average |occ-like null direction second variation| over many random balanced nulls
        accum = []
        for _ in range(400):
            cp = Vpos @ (rng.standard_normal(Vpos.shape[1]) + 1j * rng.standard_normal(Vpos.shape[1]))
            cm = Vneg @ (rng.standard_normal(Vneg.shape[1]) + 1j * rng.standard_normal(Vneg.shape[1]))
            cp /= np.linalg.norm(cp); cm /= np.linalg.norm(cm)
            v = (cp + cm); v /= np.linalg.norm(v)
            accum.append(float((v.conj() @ dB @ v).real))
        rand_null_rms = float(np.sqrt(np.mean(np.array(accum) ** 2)))
        # min|eigenvalue| linear response: finite-diff of the smallest |eig| of B + eps dB
        eps = 1e-4
        mp = np.min(np.abs(np.linalg.eigvalsh(herm(B + eps * dB))))
        mm = np.min(np.abs(np.linalg.eigvalsh(herm(B - eps * dB))))
        mineig_slope = (mp - mm) / (2 * eps)
        print(f"  {name:<16}{trace_slope:>16.3e}{flat_slope:>18.3e}{rand_null_rms:>22.3e}{mineig_slope:>16.3e}")

    print("\n" + "=" * 92)
    print("READING")
    print("=" * 92)
    print("If occ^dag dB occ and the random-null RMS are ALSO ~0 for the GU 'couple' torsion, the")
    print("protection is genuine. If they are O(1) while trace(dB)/dim is ~0, the construct's slope=0")
    print("is an averaging artifact (it tracked the spectrum MEAN, masking real flat-direction curvature).")


if __name__ == "__main__":
    main()
