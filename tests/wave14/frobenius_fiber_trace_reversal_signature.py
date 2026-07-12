"""Frobenius fiber trace-reversal and the (9,5)-vs-(7,7) signature: does the trace-reversal SELECT the total
signature, or fix only the fiber to (6,4) and stay blind to the base sign?

Weinstein: "trace-reverse the Frobenius metric along the fibers, which gets you from a (7,3) signature to a
(6,4)." The DeWitt/Frobenius metric on the fiber Sym^2(T*X) (10-dim for a 4D base):
  raw:            V0_{ab,cd}(h) = h^{a(c} h^{d)b}                    (the plain Frobenius inner product)
  trace-reversed: V_{ab,cd}(h)  = h^{a(c} h^{d)b} - (1/2) h^{ab} h^{cd}   (Weinstein / the gimmel vertical block)
Total Y14 signature = fiber (+) base. (9,5) vs (7,7) is the base sign (eta vs -eta), per the wave-3 H2 result.

QUESTION (Joe): is the trace-reversal the lever that fixes the total signature (selecting (7,7)), or does it
fix ONLY the fiber to (6,4) -- the SAME (6,4) for both base signs -- leaving (9,5)/(7,7) as the base choice it
cannot see? We COMPUTE the fiber signature (raw + trace-reversed) for base (3,1) and (1,3), and the totals.

Run: python tests/wave14/frobenius_fiber_trace_reversal_signature.py
"""
from __future__ import annotations

import numpy as np

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# symmetric-pair basis of Sym^2(R^4): 10 pairs (a<=b)
PAIRS = [(a, b) for a in range(4) for b in range(a, 4)]


def Emat(ab):
    a, b = ab
    E = np.zeros((4, 4))
    E[a, b] += 1.0
    E[b, a] += 1.0
    if a == b:
        E[a, b] = 1.0
    return E


def fiber_metric(hmat, trace_reverse):
    """10x10 fiber metric V_{(ab),(cd)} on Sym^2, using the inverse metric hinv (indices up)."""
    hinv = np.linalg.inv(hmat)
    V = np.zeros((10, 10))
    for i, ab in enumerate(PAIRS):
        Ei = Emat(ab)
        for j, cd in enumerate(PAIRS):
            Ej = Emat(cd)
            # <Ei,Ej> = tr(hinv Ei hinv Ej)  (Frobenius with raised indices)
            frob = np.trace(hinv @ Ei @ hinv @ Ej)
            if trace_reverse:
                # - (1/2) tr(hinv Ei) tr(hinv Ej)
                frob -= 0.5 * np.trace(hinv @ Ei) * np.trace(hinv @ Ej)
            V[i, j] = frob
    return V


def signature(M):
    ev = np.linalg.eigvalsh((M + M.T) / 2)
    pos = int(np.sum(ev > 1e-9))
    neg = int(np.sum(ev < -1e-9))
    return pos, neg


def main():
    print("[Frobenius fiber trace-reversal and the (9,5)/(7,7) signature]\n")
    h_plus = np.diag([-1.0, 1.0, 1.0, 1.0])   # base (3,1) mostly-plus  -> total (9,5)
    h_minus = np.diag([1.0, -1.0, -1.0, -1.0])  # base (1,3) mostly-minus -> total (7,7)

    results = {}
    for label, h, base_sig in [("(3,1) base [->(9,5)]", h_plus, (3, 1)),
                               ("(1,3) base [->(7,7)]", h_minus, (1, 3))]:
        V0 = fiber_metric(h, trace_reverse=False)
        V = fiber_metric(h, trace_reverse=True)
        s0 = signature(V0)
        s = signature(V)
        results[label] = (s0, s, base_sig)
        tot0 = (s0[0] + base_sig[0], s0[1] + base_sig[1])
        tot = (s[0] + base_sig[0], s[1] + base_sig[1])
        print(f"    base {label}:")
        print(f"      raw fiber Frobenius      signature = {s0}   -> total {tot0}")
        print(f"      TRACE-REVERSED fiber     signature = {s}   -> total {tot}")

    # the decisive checks
    s0_p, s_p, _ = results["(3,1) base [->(9,5)]"]
    s0_m, s_m, _ = results["(1,3) base [->(7,7)]"]

    check("raw Frobenius fiber is (7,3)", s0_p == (7, 3), f"got {s0_p}")
    check("trace-reversal takes the fiber to (6,4) (flips the trace mode + -> -)", s_p == (6, 4),
          f"raw {s0_p} -> reversed {s_p}")
    check("the trace-reversed fiber is the SAME (6,4) for BOTH base signs -- trace-reversal is BASE-BLIND",
          s_p == s_m == (6, 4), f"(3,1)-base fiber {s_p}, (1,3)-base fiber {s_m}")

    tot_p = (s_p[0] + 3, s_p[1] + 1)   # (6,4)+(3,1)
    tot_m = (s_m[0] + 1, s_m[1] + 3)   # (6,4)+(1,3)
    check("(9,5) = (6,4)_fiber + (3,1)_base", tot_p == (9, 5), f"{tot_p}")
    check("(7,7) = (6,4)_fiber + (1,3)_base", tot_m == (7, 7), f"{tot_m}")

    print("\n[verdict]")
    print("  The Frobenius fiber TRACE-REVERSAL is a CANONICAL, BASE-BLIND operation: it flips exactly the")
    print("  trace mode (+ -> -), taking the raw (7,3) fiber to (6,4) -- and it produces the SAME (6,4) fiber")
    print("  for BOTH base signs. So the trace-reversal fixes the FIBER; it does NOT select the total signature.")
    print("  (9,5) and (7,7) differ ONLY in the BASE sign ((3,1) vs (1,3)): (9,5)=(6,4)+(3,1), (7,7)=(6,4)+(1,3).")
    print("  => The trace-reversal is NOT the (7,7)-selecting lever. It even ENFORCES under-determination: the")
    print("     (6,4) fiber is the conformal so(4,2)~so(2,4) form (VG-V3), which is signature-symmetric ->")
    print("     the whole conformal sector it enables is base-blind (wave-3 H2). The (9,5)/(7,7) decider is a")
    print("     BASE object (the H19 term LINEAR in g carrying the timelike-norm sign), NOT the fiber trace-")
    print("     reversal. Using (7,7) = keep the canonical (6,4) trace-reversed fiber, flip the BASE to (1,3).")

    if FAIL:
        print(f"\nFAILED: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = trace-reversal fixes the fiber to (6,4) (base-blind); (9,5)/(7,7) is the base sign, not the fiber.")


if __name__ == "__main__":
    main()
