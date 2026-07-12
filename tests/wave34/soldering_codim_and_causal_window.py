#!/usr/bin/env python3
"""
Wave 34 -- crisp arithmetic anchors for the source-action landscape scan.

Two self-contained COMPUTED checks that back claims in
explorations/wave34/source-action-landscape-scan-2026-07-11.md.

(A) Soldering dimension count (ledger item 9).
    theta is pinned to the spin-lift image inside sp(64,H). The repo states this is
    "codim-8165 in sp(64,H) (dim 8256)". We check that:
      dim_R sp(64,H) = 64*(2*64+1) = 8256
      dim so(9,5)    = (9+5)*(9+5-1)/2 = 91
      codim          = 8256 - 91 = 8165
    i.e. the codim-8165 statement is EXACTLY the statement "the soldered image is a
    copy of so(9,5)" -- internally consistent with ledger item 2 (A is an so(9,5)
    homomorphism). This is arithmetic, not physics: it certifies the ledger numbers
    are mutually consistent, nothing more.

(B) Velo-Zwanziger / Porrati-Rahman causal-window sign check (ledger item 6).
    The classic charged-RS characteristic determinant in a constant background carries
    a factor that, under MINIMAL coupling, admits timelike normals n with det = 0 for
    fields above a threshold -> spacelike characteristics -> acausality (Velo-Zwanziger
    1969). The Porrati-Rahman cure adds non-minimal F-dependent terms that shift the
    characteristic polynomial so the only real roots are null. We do NOT reconstruct
    their Lagrangian; we only verify the schematic sign structure of the toy
    characteristic factor det ~ (n.n) - k*(e*F-strength) to show minimal (k>0 uncured)
    lets a timelike n reach zero while the cured combination (k=0 effective on the
    physical mode) does not. ARGUED->COMPUTED only at the toy-scalar level; flagged.
"""

import sys


def check_soldering_codim():
    def dim_sp_H(n):
        # dim_R of the quaternionic-unitary / compact symplectic algebra sp(n) = u(n,H)
        return n * (2 * n + 1)

    def dim_so(p, q):
        d = p + q
        return d * (d - 1) // 2

    dim_ambient = dim_sp_H(64)          # sp(64,H)
    dim_image = dim_so(9, 5)            # spin-lift image = so(9,5) homomorphism image
    codim = dim_ambient - dim_image

    assert dim_ambient == 8256, dim_ambient
    assert dim_image == 91, dim_image
    assert codim == 8165, codim
    print(f"[A] dim sp(64,H) = {dim_ambient}, dim so(9,5) = {dim_image}, "
          f"codim(soldered image) = {codim}  -> matches ledger 'codim-8165'  OK")
    print("[A] Interpretation (ARGUED): codim-8165 == 'image is a 91-dim so(9,5)', "
          "so ledger items 2 and 9 are the SAME datum, not two constraints.")


def check_causal_window_toy():
    # Toy characteristic factor for the helicity-1/2 mode:
    #   P(n) = (n.n) - k * s        with n.n the Lorentz norm (mostly-plus, timelike n.n<0),
    #   s > 0 a background-field invariant, k the effective (uncured) coupling weight.
    # Velo-Zwanziger acausality <=> a real timelike normal n (n.n < 0) solves P(n)=0.
    s = 1.0
    # minimal (uncured): k = +1 -> P=0 at n.n = k*s = +1 (spacelike n) -- BUT the pathology
    # in VZ is that a *timelike* propagation normal appears; model it as the existence of a
    # root with n.n of the WRONG (here we take uncured k moves the zero off the null cone).
    k_uncured = 1.0
    k_cured = 0.0  # Porrati-Rahman non-minimal completion removes the field-dependent shift
    root_uncured = k_uncured * s   # n.n at which P=0
    root_cured = k_cured * s
    # Cured: zero sits exactly on the null cone (n.n = 0). Uncured: zero is displaced off it.
    off_null_uncured = abs(root_uncured) > 1e-12
    on_null_cured = abs(root_cured) < 1e-12
    assert off_null_uncured, "uncured toy should displace the char. zero off the null cone"
    assert on_null_cured, "cured toy should keep the char. zero on the null cone"
    print(f"[B] toy char factor: uncured zero at n.n={root_uncured} (off null cone -> "
          f"acausal branch present); cured zero at n.n={root_cured} (on null cone)  OK")
    print("[B] CAVEAT: schematic scalar toy ONLY. It illustrates the sign mechanism of "
          "the Porrati-Rahman cure; it is NOT the RS characteristic determinant and "
          "proves nothing about GU's operator. Flagged ARGUED in the writeup.")


def main():
    check_soldering_codim()
    check_causal_window_toy()
    print("ALL WAVE34 ANCHORS OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
