"""
W150 -- consensus / cryptography / network-systems substrate sweep: deterministic scoring checks.

Family Team 6 of the full-roster steelman sweep (label W150). This test does NOT assert any
physics; it (a) reproduces the W138 kill-battery anchors as positive controls so the family's
scoring rides on the same frozen numbers, and (b) computes the dimension/finality bookkeeping the
surviving stories pin (the (9,5)=(3,1)+(6,4) commitment split; the (9,5) confirmed/frontier split;
the {2,7,13}-smooth ledger dims with 3 absent as the binding gap; the causal-set N=S_dS finality
count). Exploration grade. No canon change.

Run: python tests/W150_consensus_crypto_scoring_checks.py   (deterministic; exit 0 on pass)
"""
import math

TOL = 5e-3
checks = []


def chk(name, got, want, rel=TOL):
    ok = abs(got - want) <= rel * max(1.0, abs(want))
    checks.append((name, ok, got, want))
    return ok


# ---------------------------------------------------------------------------
# Positive controls: reproduce the W138 de Sitter / Landauer ledger anchors.
# (SI constants; same values W138 froze in tests/W138_issuance_kill_battery.py.)
# ---------------------------------------------------------------------------
hbar = 1.054571817e-34
c = 2.99792458e8
G = 6.67430e-11
kB = 1.380649e-23
H0 = 67.36 * 1000.0 / (3.0856775815e22)   # s^-1
OmL = 0.6847

lp = math.sqrt(hbar * G / c ** 3)
RH = c / H0
S_dS = math.pi * RH ** 2 / lp ** 2                         # k_B units (dimensionless count)
T_dS = hbar * H0 / (2.0 * math.pi * kB)                    # K
rho_crit = 3.0 * H0 ** 2 / (8.0 * math.pi * G)
rho_L = OmL * rho_crit
VH = (4.0 / 3.0) * math.pi * RH ** 3
E_L = rho_L * c ** 2 * VH
TS = (T_dS * kB) * S_dS                                    # J
ratio = TS / E_L                                           # the W138 factor 1.46

chk("PC1 S_dS ~ 2.27e122", S_dS, 2.268e122, rel=2e-2)
chk("PC2 T_dS ~ 2.65e-30 K", T_dS, 2.654e-30, rel=2e-2)
chk("PC3 E_Lambda ~ 5.69e69 J", E_L, 5.690e69, rel=3e-2)
chk("PC4 T_dS*S_dS ~ 8.31e69 J", TS, 8.310e69, rel=3e-2)
chk("PC5 factor T_dS S_dS / E_L = 1.46 (W138 G5)", ratio, 1.46, rel=1e-2)

# Landauer confirmed-ledger capacity at T_dS (W138 G6): bits/S_dS = 2.96.
budget = 3.0 * E_L                                         # per Hubble time per Hubble volume
bits_TdS = budget / (kB * T_dS * math.log(2.0))
chk("PC6 bits(T_dS)/S_dS = 2.96 (= 3/(ln2) / 1.46)", bits_TdS / S_dS, 3.0 / math.log(2.0) / 1.46, rel=2e-2)

# ---------------------------------------------------------------------------
# Story pins (new bookkeeping this wave). Integer/structural facts of (9,5).
# ---------------------------------------------------------------------------
# Marquee A -- commitment split: the message (hidden) space is the DeWitt fiber (6,4),
# the commitment string (visible shadow) is the base (3,1). Y14 = (9,5) = (3,1) + (6,4).
base_dim = 3 + 1
fiber_dim = 6 + 4
chk("A1 visible/commitment dim = 4", float(base_dim), 4.0, rel=0)
chk("A2 hidden/message dim = 10", float(fiber_dim), 10.0, rel=0)
chk("A3 base(3,1)+fiber(6,4) = (9,5) total 14", float(base_dim + fiber_dim), 14.0, rel=0)

# Marquee C/D -- finality split: in an indefinite Krein metric of signature (p,q)=(9,5)
# the maximal positive ("confirmed") subspace has dim p=9; the q=5 negative directions are
# the permanently-unconfirmable remainder = the nonzero finality frontier. H_C+ is PROPER
# (dim 9 < 14) exactly because q=5>0 -- the structural reason finality never closes.
p, q = 9, 5
chk("D1 confirmed (max positive) dim = 9", float(p), 9.0, rel=0)
chk("D2 finality-frontier width q = 5 (nonzero => never closes)", float(q), 5.0, rel=0)
frontier_nonempty = q > 0
checks.append(("D3 H_C+ proper iff q>0 (Krein indefinite)", frontier_nonempty, q, 1))

# Binding gap: the ledger dimensions are {2,7,13}-smooth (firewall canon, signature-robust):
# spinor 128 = 2^7 ; ker(Gamma) = 13*128 = 1664. The prime 3 divides none of them, so a count
# of 3 (the imported multiplicity) is the "computational-binding gap" -- what the perfectly
# hiding Y14->X4 commitment cannot bind internally. (This mirrors the Multiplicity Theorem.)
spinor = 2 ** 7
kerGamma = 13 * 128
chk("B1 spinor dim = 128 = 2^7", float(spinor), 128.0, rel=0)
chk("B2 ker(Gamma) = 1664 = 13*128", float(kerGamma), 1664.0, rel=0)
three_divides = (spinor % 3 == 0) or (kerGamma % 3 == 0) or (14 % 3 == 0)
checks.append(("B3 3 divides no ledger dim (binding gap = imported prime)", (not three_divides), 0, 0))

# Shadow map (inherited causal-set template, NOT the family's novelty): with the finalized-record
# count identified with the horizon entropy N = S_dS, Lambda ~ 1/sqrt(N) is order-consistent with
# rho_L in Planck units (sqrt(rho_L/rho_Pl) ~ 1/sqrt(N) to a causal-set O(1)). Reported, not pinned.
rho_Pl = c ** 5 / (hbar * G ** 2)
lhs = math.sqrt(rho_L / rho_Pl)
rhs = 1.0 / math.sqrt(S_dS)
# order check only: this template is INHERITED from causal sets (not a family novelty); it carries
# the standard everpresent-Lambda O(1) ambiguity (V in Planck units vs horizon count). Assert the
# two agree to within a factor of 3 (|log10 ratio| < ~0.5), i.e. same order.
oom_ok = abs(math.log10(lhs / rhs)) < 0.5
checks.append(("S1 sqrt(rho_L/rho_Pl) ~ 1/sqrt(S_dS) to O(1) (inherited causal-set template)",
               oom_ok, lhs / rhs, 1.0))

# ---------------------------------------------------------------------------
if __name__ == "__main__":
    npass = sum(1 for _, ok, *_ in checks if ok)
    for name, ok, got, want in checks:
        tag = "PASS" if ok else "FAIL"
        print(f"[{tag}] {name}: got={got}, want={want}")
    print(f"\n{npass}/{len(checks)} checks passed.")
    raise SystemExit(0 if npass == len(checks) else 1)
