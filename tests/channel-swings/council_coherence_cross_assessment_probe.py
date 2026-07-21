#!/usr/bin/env python3
"""
council_coherence_cross_assessment_probe.py  (foreground, deterministic, NO RNG)

Tabulates the COHERENCE CROSS-ASSESSMENT of the 22 committed council
constructions. Each of the 22 personas, reconstituted IN CHARACTER as an
ASSESSOR, rated every OTHER construction (21 of them) on a 1-10 COHERENCE scale
(1 = contradicts a banked result / internally incoherent; 10 = possibly a
different substrate but the story fully hangs together, respects everything we
know, and its consequences follow). Substrate-loyalty is NOT the axis: an
assessor MUST give a high score to a coherent construction from a rival substrate.

The elicited integer scores are HARD-CODED below (SCORES) exactly as produced by
the in-character assessment pass. This probe only TABULATES them deterministically:
per-construction MEAN, population STD-DEV, CROSS-CAMP mean (raters outside the
construction's own council-group SCI/SYS/EXT/MTH), and RANK by mean. No RNG, no
network, no file writes. Two runs are byte-identical.

Banked results the coherence axis is anchored to (penalize contradiction only):
  Q2-FREE ; Q3-TWO-INDEPENDENT ; P0 ~8% non-constructible null stratum ;
  geometry sigma = w1(L_time) over F~=RP^3 (the circle/cycle reading is a
  CLASS-RELATIVE local no-go, OPEN not globally refuted) ;
  the WEAK Prong-3 finding "one globally consistent record arrow" (6/16 configs).
"""
import statistics, sys

IDS = ["SCI-ORTH","SCI-HET","SCI-WILD","SCI-COM","SCI-PHIL",
       "SYS-ZK","SYS-NN","SYS-MMO","SYS-META","SYS-HASH","SYS-FLP",
       "EXT-EVO","EXT-STAT","EXT-HYPER","EXT-INTER",
       "MTH-DIFF","MTH-TOPO","MTH-CLIF","MTH-CAT","MTH-SHEAF","MTH-INFO","MTH-KOLM"]
CAMP = {k: k.split("-")[0] for k in IDS}

# ---- ELICITED SCORES (hard-coded; rows = assessor, cols = construction rated) ----
SCORES = {
  "SCI-ORTH": {"SCI-HET":8,"SCI-WILD":6,"SCI-COM":8,"SCI-PHIL":8,"SYS-ZK":9,"SYS-NN":8,"SYS-MMO":7,"SYS-META":9,"SYS-HASH":7,"SYS-FLP":9,"EXT-EVO":9,"EXT-STAT":9,"EXT-HYPER":8,"EXT-INTER":7,"MTH-DIFF":9,"MTH-TOPO":8,"MTH-CLIF":9,"MTH-CAT":6,"MTH-SHEAF":8,"MTH-INFO":9,"MTH-KOLM":9},
  "SCI-HET": {"SCI-ORTH":10,"SCI-WILD":10,"SCI-COM":9,"SCI-PHIL":10,"SYS-ZK":10,"SYS-NN":9,"SYS-MMO":8,"SYS-META":10,"SYS-HASH":8,"SYS-FLP":10,"EXT-EVO":10,"EXT-STAT":10,"EXT-HYPER":9,"EXT-INTER":8,"MTH-DIFF":10,"MTH-TOPO":9,"MTH-CLIF":10,"MTH-CAT":8,"MTH-SHEAF":9,"MTH-INFO":10,"MTH-KOLM":10},
  "SCI-WILD": {"SCI-ORTH":9,"SCI-HET":10,"SCI-COM":9,"SCI-PHIL":10,"SYS-ZK":10,"SYS-NN":9,"SYS-MMO":8,"SYS-META":10,"SYS-HASH":8,"SYS-FLP":10,"EXT-EVO":10,"EXT-STAT":10,"EXT-HYPER":9,"EXT-INTER":8,"MTH-DIFF":10,"MTH-TOPO":9,"MTH-CLIF":10,"MTH-CAT":8,"MTH-SHEAF":9,"MTH-INFO":10,"MTH-KOLM":10},
  "SCI-COM": {"SCI-ORTH":9,"SCI-HET":9,"SCI-WILD":6,"SCI-PHIL":9,"SYS-ZK":9,"SYS-NN":9,"SYS-MMO":7,"SYS-META":9,"SYS-HASH":7,"SYS-FLP":10,"EXT-EVO":9,"EXT-STAT":10,"EXT-HYPER":9,"EXT-INTER":7,"MTH-DIFF":10,"MTH-TOPO":9,"MTH-CLIF":10,"MTH-CAT":7,"MTH-SHEAF":9,"MTH-INFO":10,"MTH-KOLM":9},
  "SCI-PHIL": {"SCI-ORTH":9,"SCI-HET":9,"SCI-WILD":9,"SCI-COM":9,"SYS-ZK":9,"SYS-NN":9,"SYS-MMO":7,"SYS-META":9,"SYS-HASH":7,"SYS-FLP":10,"EXT-EVO":9,"EXT-STAT":10,"EXT-HYPER":9,"EXT-INTER":7,"MTH-DIFF":10,"MTH-TOPO":9,"MTH-CLIF":10,"MTH-CAT":7,"MTH-SHEAF":9,"MTH-INFO":10,"MTH-KOLM":9},
  "SYS-ZK": {"SCI-ORTH":9,"SCI-HET":9,"SCI-WILD":6,"SCI-COM":9,"SCI-PHIL":9,"SYS-NN":9,"SYS-MMO":8,"SYS-META":9,"SYS-HASH":8,"SYS-FLP":10,"EXT-EVO":9,"EXT-STAT":10,"EXT-HYPER":9,"EXT-INTER":8,"MTH-DIFF":10,"MTH-TOPO":9,"MTH-CLIF":10,"MTH-CAT":8,"MTH-SHEAF":9,"MTH-INFO":10,"MTH-KOLM":9},
  "SYS-NN": {"SCI-ORTH":9,"SCI-HET":8,"SCI-WILD":6,"SCI-COM":9,"SCI-PHIL":9,"SYS-ZK":9,"SYS-MMO":8,"SYS-META":9,"SYS-HASH":8,"SYS-FLP":10,"EXT-EVO":9,"EXT-STAT":10,"EXT-HYPER":9,"EXT-INTER":8,"MTH-DIFF":10,"MTH-TOPO":9,"MTH-CLIF":10,"MTH-CAT":8,"MTH-SHEAF":9,"MTH-INFO":10,"MTH-KOLM":9},
  "SYS-MMO": {"SCI-ORTH":10,"SCI-HET":10,"SCI-WILD":10,"SCI-COM":9,"SCI-PHIL":10,"SYS-ZK":10,"SYS-NN":9,"SYS-META":10,"SYS-HASH":10,"SYS-FLP":10,"EXT-EVO":10,"EXT-STAT":10,"EXT-HYPER":10,"EXT-INTER":9,"MTH-DIFF":10,"MTH-TOPO":10,"MTH-CLIF":10,"MTH-CAT":9,"MTH-SHEAF":10,"MTH-INFO":10,"MTH-KOLM":10},
  "SYS-META": {"SCI-ORTH":9,"SCI-HET":9,"SCI-WILD":6,"SCI-COM":9,"SCI-PHIL":9,"SYS-ZK":9,"SYS-NN":9,"SYS-MMO":8,"SYS-HASH":8,"SYS-FLP":10,"EXT-EVO":9,"EXT-STAT":10,"EXT-HYPER":9,"EXT-INTER":8,"MTH-DIFF":10,"MTH-TOPO":9,"MTH-CLIF":10,"MTH-CAT":8,"MTH-SHEAF":9,"MTH-INFO":10,"MTH-KOLM":9},
  "SYS-HASH": {"SCI-ORTH":10,"SCI-HET":10,"SCI-WILD":10,"SCI-COM":9,"SCI-PHIL":10,"SYS-ZK":10,"SYS-NN":9,"SYS-MMO":9,"SYS-META":10,"SYS-FLP":10,"EXT-EVO":10,"EXT-STAT":10,"EXT-HYPER":10,"EXT-INTER":9,"MTH-DIFF":10,"MTH-TOPO":10,"MTH-CLIF":10,"MTH-CAT":9,"MTH-SHEAF":10,"MTH-INFO":10,"MTH-KOLM":10},
  "SYS-FLP": {"SCI-ORTH":8,"SCI-HET":9,"SCI-WILD":6,"SCI-COM":8,"SCI-PHIL":9,"SYS-ZK":9,"SYS-NN":8,"SYS-MMO":7,"SYS-META":9,"SYS-HASH":8,"EXT-EVO":9,"EXT-STAT":9,"EXT-HYPER":9,"EXT-INTER":7,"MTH-DIFF":9,"MTH-TOPO":9,"MTH-CLIF":9,"MTH-CAT":7,"MTH-SHEAF":9,"MTH-INFO":9,"MTH-KOLM":9},
  "EXT-EVO": {"SCI-ORTH":9,"SCI-HET":9,"SCI-WILD":6,"SCI-COM":9,"SCI-PHIL":9,"SYS-ZK":9,"SYS-NN":9,"SYS-MMO":8,"SYS-META":9,"SYS-HASH":8,"SYS-FLP":10,"EXT-STAT":10,"EXT-HYPER":9,"EXT-INTER":8,"MTH-DIFF":10,"MTH-TOPO":9,"MTH-CLIF":10,"MTH-CAT":8,"MTH-SHEAF":9,"MTH-INFO":10,"MTH-KOLM":9},
  "EXT-STAT": {"SCI-ORTH":8,"SCI-HET":9,"SCI-WILD":6,"SCI-COM":8,"SCI-PHIL":9,"SYS-ZK":9,"SYS-NN":8,"SYS-MMO":7,"SYS-META":9,"SYS-HASH":8,"SYS-FLP":9,"EXT-EVO":9,"EXT-HYPER":9,"EXT-INTER":7,"MTH-DIFF":9,"MTH-TOPO":9,"MTH-CLIF":9,"MTH-CAT":7,"MTH-SHEAF":9,"MTH-INFO":9,"MTH-KOLM":9},
  "EXT-HYPER": {"SCI-ORTH":9,"SCI-HET":9,"SCI-WILD":6,"SCI-COM":9,"SCI-PHIL":9,"SYS-ZK":9,"SYS-NN":9,"SYS-MMO":9,"SYS-META":9,"SYS-HASH":9,"SYS-FLP":10,"EXT-EVO":9,"EXT-STAT":10,"EXT-INTER":9,"MTH-DIFF":10,"MTH-TOPO":9,"MTH-CLIF":10,"MTH-CAT":9,"MTH-SHEAF":9,"MTH-INFO":10,"MTH-KOLM":9},
  "EXT-INTER": {"SCI-ORTH":10,"SCI-HET":10,"SCI-WILD":10,"SCI-COM":9,"SCI-PHIL":10,"SYS-ZK":10,"SYS-NN":9,"SYS-MMO":9,"SYS-META":10,"SYS-HASH":10,"SYS-FLP":10,"EXT-EVO":10,"EXT-STAT":10,"EXT-HYPER":10,"MTH-DIFF":10,"MTH-TOPO":10,"MTH-CLIF":10,"MTH-CAT":9,"MTH-SHEAF":10,"MTH-INFO":10,"MTH-KOLM":10},
  "MTH-DIFF": {"SCI-ORTH":9,"SCI-HET":8,"SCI-WILD":6,"SCI-COM":8,"SCI-PHIL":8,"SYS-ZK":9,"SYS-NN":8,"SYS-MMO":7,"SYS-META":9,"SYS-HASH":7,"SYS-FLP":9,"EXT-EVO":9,"EXT-STAT":9,"EXT-HYPER":8,"EXT-INTER":7,"MTH-TOPO":8,"MTH-CLIF":9,"MTH-CAT":7,"MTH-SHEAF":8,"MTH-INFO":9,"MTH-KOLM":9},
  "MTH-TOPO": {"SCI-ORTH":9,"SCI-HET":9,"SCI-WILD":6,"SCI-COM":9,"SCI-PHIL":9,"SYS-ZK":9,"SYS-NN":9,"SYS-MMO":9,"SYS-META":9,"SYS-HASH":9,"SYS-FLP":10,"EXT-EVO":9,"EXT-STAT":10,"EXT-HYPER":9,"EXT-INTER":9,"MTH-DIFF":9,"MTH-CLIF":10,"MTH-CAT":9,"MTH-SHEAF":9,"MTH-INFO":10,"MTH-KOLM":9},
  "MTH-CLIF": {"SCI-ORTH":9,"SCI-HET":8,"SCI-WILD":6,"SCI-COM":8,"SCI-PHIL":9,"SYS-ZK":9,"SYS-NN":8,"SYS-MMO":7,"SYS-META":9,"SYS-HASH":8,"SYS-FLP":9,"EXT-EVO":9,"EXT-STAT":9,"EXT-HYPER":9,"EXT-INTER":7,"MTH-DIFF":8,"MTH-TOPO":9,"MTH-CAT":7,"MTH-SHEAF":9,"MTH-INFO":9,"MTH-KOLM":9},
  "MTH-CAT": {"SCI-ORTH":9,"SCI-HET":10,"SCI-WILD":10,"SCI-COM":9,"SCI-PHIL":10,"SYS-ZK":10,"SYS-NN":9,"SYS-MMO":9,"SYS-META":10,"SYS-HASH":10,"SYS-FLP":10,"EXT-EVO":10,"EXT-STAT":10,"EXT-HYPER":10,"EXT-INTER":9,"MTH-DIFF":10,"MTH-TOPO":10,"MTH-CLIF":10,"MTH-SHEAF":10,"MTH-INFO":10,"MTH-KOLM":10},
  "MTH-SHEAF": {"SCI-ORTH":9,"SCI-HET":9,"SCI-WILD":6,"SCI-COM":9,"SCI-PHIL":9,"SYS-ZK":9,"SYS-NN":9,"SYS-MMO":9,"SYS-META":9,"SYS-HASH":9,"SYS-FLP":10,"EXT-EVO":9,"EXT-STAT":10,"EXT-HYPER":9,"EXT-INTER":9,"MTH-DIFF":10,"MTH-TOPO":9,"MTH-CLIF":10,"MTH-CAT":9,"MTH-INFO":10,"MTH-KOLM":9},
  "MTH-INFO": {"SCI-ORTH":9,"SCI-HET":9,"SCI-WILD":6,"SCI-COM":8,"SCI-PHIL":9,"SYS-ZK":9,"SYS-NN":8,"SYS-MMO":7,"SYS-META":9,"SYS-HASH":8,"SYS-FLP":9,"EXT-EVO":9,"EXT-STAT":9,"EXT-HYPER":9,"EXT-INTER":7,"MTH-DIFF":9,"MTH-TOPO":9,"MTH-CLIF":9,"MTH-CAT":7,"MTH-SHEAF":9,"MTH-KOLM":9},
  "MTH-KOLM": {"SCI-ORTH":8,"SCI-HET":9,"SCI-WILD":6,"SCI-COM":8,"SCI-PHIL":9,"SYS-ZK":9,"SYS-NN":8,"SYS-MMO":7,"SYS-META":9,"SYS-HASH":8,"SYS-FLP":9,"EXT-EVO":9,"EXT-STAT":9,"EXT-HYPER":9,"EXT-INTER":7,"MTH-DIFF":9,"MTH-TOPO":9,"MTH-CLIF":9,"MTH-CAT":7,"MTH-SHEAF":9,"MTH-INFO":9},
}

def fail(msg):
    print("PROBE FAIL:", msg); sys.exit(1)

# ---- integrity checks ----
if len(IDS) != 22: fail("expected 22 IDs")
if sorted(SCORES.keys()) != sorted(IDS): fail("assessor set != 22 IDs")
for i in IDS:
    row = SCORES[i]
    if i in row: fail(f"{i} rated itself")
    if sorted(row.keys()) != sorted(x for x in IDS if x != i):
        fail(f"{i} did not rate exactly the other 21")
    for j, v in row.items():
        if not (1 <= v <= 10): fail(f"{i}->{j} out of 1..10: {v}")

# ---- tabulate ----
res = {}
for j in IDS:
    raters = [(i, SCORES[i][j]) for i in IDS if i != j]
    vals = [v for _, v in raters]
    cross = [v for i, v in raters if CAMP[i] != CAMP[j]]
    same  = [v for i, v in raters if CAMP[i] == CAMP[j]]
    res[j] = dict(mean=statistics.mean(vals),
                  std=statistics.pstdev(vals),
                  cross=statistics.mean(cross),
                  same=statistics.mean(same),
                  n=len(vals))
rank = sorted(IDS, key=lambda j: (-res[j]["mean"], j))
rank_of = {j: n for n, j in enumerate(rank, 1)}

# ---- report ----
print("="*72)
print("COUNCIL COHERENCE CROSS-ASSESSMENT  (22 assessors x 21 ratees, 1-10)")
print("="*72)

print("\n[1] SCORE MATRIX (row=assessor, col=ratee; '.'=self)")
hdr = "assessor  | " + " ".join(f"{j.split('-')[1][:3]:>3}" for j in IDS)
print(hdr); print("-"*len(hdr))
for i in IDS:
    cells = " ".join((" . " if j == i else f"{SCORES[i][j]:>3}") for j in IDS)
    print(f"{i:9s} | {cells}")

print("\n[2] PER-CONSTRUCTION  MEAN / STD / CROSS-CAMP / IN-CAMP / RANK")
print(f"{'ID':10s} {'MEAN':>5} {'STD':>5} {'CROSS':>6} {'INCAMP':>6} {'RANK':>4}")
for j in rank:
    r = res[j]
    print(f"{j:10s} {r['mean']:5.2f} {r['std']:5.2f} {r['cross']:6.2f} {r['same']:6.2f} {rank_of[j]:4d}")

print("\n[3] TOP-5 by CROSS-CAMP mean (stories even rival camps rate coherent)")
for j in sorted(IDS, key=lambda j: (-res[j]["cross"], j))[:5]:
    print(f"   {j:10s} cross={res[j]['cross']:.2f}  mean={res[j]['mean']:.2f}  std={res[j]['std']:.2f}")

print("\n[4] MOST CONTESTED (highest STD)")
for j in sorted(IDS, key=lambda j: (-res[j]["std"], j))[:5]:
    print(f"   {j:10s} std={res[j]['std']:.2f}  mean={res[j]['mean']:.2f}")

print("\n[5] LOWEST MEAN (relative floor)")
for j in sorted(IDS, key=lambda j: (res[j]["mean"], j))[:4]:
    print(f"   {j:10s} mean={res[j]['mean']:.2f}  std={res[j]['std']:.2f}  min-cell={min(SCORES[i][j] for i in IDS if i!=j)}")

print("\n[6] PER-ASSESSOR single HIGHEST / LOWEST (ties -> first in IDS order)")
for i in IDS:
    row = SCORES[i]
    hi = min((j for j in IDS if j != i), key=lambda j: (-row[j], IDS.index(j)))
    lo = min((j for j in IDS if j != i), key=lambda j: (row[j], IDS.index(j)))
    print(f"   {i:10s} HIGH={hi}({row[hi]})  LOW={lo}({row[lo]})")

gmin = min(res[j]["mean"] for j in IDS)
print(f"\n[7] GLOBAL FLOOR: lowest construction mean = {gmin:.2f} "
      f"({'no construction rated low across the board' if gmin >= 6.0 else 'a construction is broadly low'})")

print("\nPROBE OK  (exit 0)")
sys.exit(0)
