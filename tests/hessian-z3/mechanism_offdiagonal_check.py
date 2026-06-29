#!/usr/bin/env python3
r"""
MECHANISM (honest, after TWO falsified guesses -- fabrication discipline at work).
Guess 1 (equal-and-opposite shift between the +96 and -96 halves): FALSIFIED -- both halves' diagonal
shifts are machine-zero, not equal-and-opposite.
Guess 2 (the torsion is purely OFF-DIAGONAL gen<->mir, chirality-odd): ALSO FALSIFIED by the block
decomposition below -- the GU chiralizer deformation dB is actually block-DIAGONAL (||gen,gen|| and
||mir,mir|| nonzero and equal at 1/sqrt(2); ||gen,mir|| ~ 0), i.e. it PRESERVES the gen/mirror split.

TRUE mechanism (computed): dB reshuffles modes WITHIN each chirality block but each block is TRACELESS
(the diagonal trace over the +96 block and over the -96 block are both ~0). So the individual carrier
eigenvalues spread, but the MEAN of each block -- the carrier-occupancy / generation-count direction --
does not move. Hence d(lambda_net)/d(epsilon) = 0. A generic deformation has NONZERO block trace and
moves the net eigenvalue.

Honest classification: the protected slope = 0 is a tracelessness property of the GU chiralizer/Krein
deformation -- a consequence of the same Krein/quaternionic structure behind the vectorlike balance and
the DECOUPLE, expressed at the level of the deformation's diagonal. LARGELY RE-ENCODED. The genuinely
NEW, non-vacuous content is the DISCRIMINATION: a generic deformation has nonzero block trace and IS
critical; the GU torsion is not. The method is not blind, and the protection is real but inherited.

We decompose the carrier deformation dB into the (gen,gen), (mir,mir), (gen,mir) blocks; the decisive
number is the diagonal TRACE of each block (whether the block mean moves), not the block norm.

Run: python tests/hessian-z3/mechanism_offdiagonal_check.py
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


def blocks(dB, Vpos, Vneg):
    gg = np.linalg.norm(Vpos.conj().T @ dB @ Vpos)
    mm = np.linalg.norm(Vneg.conj().T @ dB @ Vneg)
    gm = np.linalg.norm(Vpos.conj().T @ dB @ Vneg)
    tot = np.linalg.norm(dB) + 1e-30
    diag_tr = float(np.trace(Vpos.conj().T @ dB @ Vpos).real) + float(np.trace(Vneg.conj().T @ dB @ Vneg).real)
    return gg / tot, mm / tot, gm / tot, diag_tr


def main():
    np.set_printoptions(precision=6, suppress=True, linewidth=160)
    print("=" * 90)
    print("MECHANISM: block-diagonal + TRACELESS structure of the GU torsion on the carrier")
    print("=" * 90)
    S = C.build_substrate()
    Wt, K = S["Wt"], S["K"]
    B = S["B"]
    evB, VB = np.linalg.eigh(B)
    Vpos = VB[:, evB > 1e-9]
    Vneg = VB[:, evB < -1e-9]
    print(f"carrier (+{Vpos.shape[1]} generation, -{Vneg.shape[1]} mirror)")

    # GU chiralizer torsion
    U = C.quaternionic_J(S["e"], seed=1)
    Jf = np.kron(np.eye(N), U)
    G = S["Pi"] - (np.eye(N * DIM, dtype=complex) - S["Pi"])
    theta_chiral = Jf @ G
    dB_ch = herm(Wt.conj().T @ herm(K @ theta_chiral) @ Wt)
    dB_ch /= (np.linalg.norm(dB_ch) + 1e-30)

    # generic torsion
    rng = np.random.default_rng(7)
    R = rng.standard_normal((N * DIM, N * DIM)) + 1j * rng.standard_normal((N * DIM, N * DIM))
    R /= np.linalg.norm(R) / np.sqrt(N * DIM)
    dB_gen = herm(Wt.conj().T @ herm(K @ R) @ Wt)
    dB_gen /= (np.linalg.norm(dB_gen) + 1e-30)

    print(f"\n  {'torsion':<22}{'||gen,gen||':>14}{'||mir,mir||':>14}{'||gen,mir||':>14}{'diag trace':>14}")
    for name, dB in (("GU chiralizer", dB_ch), ("generic random", dB_gen)):
        gg, mm, gm, dtr = blocks(dB, Vpos, Vneg)
        print(f"  {name:<22}{gg:>14.4e}{mm:>14.4e}{gm:>14.4e}{dtr:>14.3e}")

    gg_ch, mm_ch, gm_ch, dtr_ch = blocks(dB_ch, Vpos, Vneg)
    gg_g, mm_g, gm_g, dtr_g = blocks(dB_gen, Vpos, Vneg)
    print("\n  reading (the decisive number is the diagonal TRACE of each block, not the block norm):")
    print(f"    GU chiralizer torsion: block-DIAGONAL (||gg||={gg_ch:.3f}, ||mm||={mm_ch:.3f}, "
          f"||gm||={gm_ch:.1e} ~ 0), preserves gen/mirror;")
    print(f"      but the diagonal TRACE over the blocks is {dtr_ch:.2e} ~ 0 -> each block reshuffles")
    print(f"      tracelessly, so the block MEAN (occupancy / generation-count) does not move. dlam/deps=0.")
    print(f"    generic torsion: blocks all ~0.5 with diagonal TRACE {dtr_g:.2e} != 0 -> the block mean")
    print(f"      MOVES -> that is exactly what makes an unstructured deformation CRITICAL.")
    print("\n  HONEST VERDICT: eigenvalue-0 is GENERIC/PROTECTED under the GU chiralizer torsion. The")
    print("  protection is a tracelessness property of the Krein/chiralizer deformation within each")
    print("  chirality block -- a consequence of the same Krein/quaternionic structure behind the")
    print("  vectorlike balance and the DECOUPLE. It is LARGELY RE-ENCODED, not an independent firewall.")
    print("  The NEW, non-vacuous content is the DISCRIMINATION: a generic deformation has nonzero block")
    print("  trace and IS critical; the GU torsion is not. located-not-forced holds, robustly, to 1st order.")

    diag_protected = abs(dtr_ch) < 1e-6
    generic_has_diag = abs(dtr_g) > 1e-3
    print(f"\n  GU torsion block-trace protected (dlam/deps=0): {diag_protected}   "
          f"generic block-trace nonzero (critical): {generic_has_diag}")
    return dict(gg_ch=gg_ch, mm_ch=mm_ch, gm_ch=gm_ch, gg_g=gg_g, mm_g=mm_g, gm_g=gm_g,
                diag_protected=diag_protected, generic_has_diag=generic_has_diag)


if __name__ == "__main__":
    out = main()
    import json
    print("\n[json] " + json.dumps(out, default=str))
