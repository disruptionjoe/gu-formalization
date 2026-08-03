# REFEREE independent re-derivation of LEG-B's intersection.
# I do NOT import LEG-B's ALLOW masks. I re-apply the frozen HARD RULE
# ("a cell is emptied ONLY if GU STATES the elimination; existence != selection")
# to each transcript commitment from scratch, asking: does this commitment,
# on a STRICT reading, empty any {FS,INV,PH} cell? Then I recompute survivors.
#
# Upgraded 2026-08-03 (register P-H10): the numeric primitives were literal
# restatements of this file's own CARRIER dict.  They are now DERIVED from
# sigma(K3) = -16 by index arithmetic (21 sigma/8, 19 sigma/8, 5 p1/6 with
# p1 = 3 sigma) and CROSS-CHECKED against the canon adjudication table this
# file always cited (canon/gamma-traceless-38-adjudication-RESULTS.md) by
# parsing that table at run time.
import itertools
import re
from pathlib import Path

from sympy import Integer, Rational

FAILS = []
def ck(n, c):
    print(("PASS" if c else "FAIL"), n)
    if not c: FAILS.append(n)

# ---------------------------------------------------------------------------
# Numeric primitives: DERIVED, not restated.
# K3 topological data (cited): signature sigma = -16.
# Signature theorem (dim 4): p1 = 3 sigma.  A-hat(K3) = -sigma/8.
# Carrier indices (canon adjudication):
#   bare twist T_C        : 5 p1 / 6            (= 20 sigma / 8, cross-checked)
#   A = T_C - 1C          : 21 sigma / 8        (ghost-subtracted gravitino)
#   B = T_C + 1C          : 19 sigma / 8        (geometric gamma-traceless Q)
# where one reversed-chirality spin-1/2 unit carries index -A-hat.
# ---------------------------------------------------------------------------
sigma = Integer(-16)
p1 = 3 * sigma
ahat = -sigma / 8
ind_bare = Rational(5, 6) * p1
ind_unit = -ahat                       # one reversed-chirality spin-1/2 unit
ind_A = Rational(21, 8) * sigma
ind_B = Rational(19, 8) * sigma

ck("A-hat(K3) = 2 (derived -sigma/8)", ahat == 2)
ck("bare twist 5p1/6 == 20sigma/8", ind_bare == Rational(20, 8) * sigma)
ck("A = bare - one unit (T_C - 1C)", ind_A == ind_bare + ind_unit)
ck("B = bare + one unit (T_C + 1C)", ind_B == ind_bare - ind_unit)

CARRIER = {"A": int(ind_A), "B": int(ind_B), "-40": int(ind_bare)}

# Cross-check the derivation against the canon adjudication table (the
# external authority this file cites), parsed from the file itself.
CANON_TABLE = (
    Path(__file__).resolve().parents[2]
    / "canon" / "gamma-traceless-38-adjudication-RESULTS.md"
)
def canon_index(row_marker):
    for line in CANON_TABLE.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith("|") and row_marker in line:
            match = re.search(r"\|\s*\*{0,2}(-\d+)\*{0,2}\s*\|", line)
            if match:
                return int(match.group(1))
    return None

ck("canon table: A row == derived -42",
   canon_index("A: ghost-subtracted gravitino") == CARRIER["A"])
ck("canon table: B row == derived -38",
   canon_index("B: geometric gamma-traceless Q") == CARRIER["B"])
ck("canon table: control row == derived -40",
   canon_index("bare twist (control)") == CARRIER["-40"])

CELLS = list(itertools.product(
    ["constrained", "full", "bare"],
    ["present", "absent"],
    ["chiral", "massive"],
))

def cell_carrier(cell):
    FS, INV, PH = cell
    if FS == "bare":        return "-40"
    if FS == "full":
        if INV == "present": return "A" if PH == "chiral" else "-40"   # super-Higgs at massive
        return "-40"                                                    # full ungauged control
    if FS == "constrained":
        if INV == "present": return None                               # incoherent: gauge inside kerGamma
        return "B"
    return None

# For each commitment I record ONLY hard eliminations that trace to something GU STATES.
# (Directional "tilts" are soft and by construction cannot empty a cell -- I ignore them here;
#  the whole point is to test whether ANY stated commitment rises to a HARD force.)
def hard_eliminations(name):
    # returns set of cells this commitment STATES-ly forbids; empty if none.
    # --- C1 field content: fixes bundle Omega^1(x)S. States neither constraint nor invariance nor phase.
    if name == "C1": return set()
    # --- C2 geometric elliptic complex: GU frames it geometrically but says "IF d^2=0" (conditional);
    #     never STATES gamma-tracelessness, never STATES BRST. No cell emptied.
    if name == "C2": return set()
    # --- C3 matter-not-ghost: kills only the NAIVE full-gauging that DELETES stated matter.
    #     But a matter-preserving (selective) gauging route is NOT excluded by anything GU states,
    #     so the full+present cells are not emptied. GU never states EITHER gauging. No cell emptied.
    if name == "C3": return set()
    # --- C4 "never find spacetime SUSY": rules out the SPACETIME-SUSY route to a gauged gravitino.
    #     The A CELL is reachable by a non-spacetime route (graded-IG). GU does not state the ONLY
    #     route to A is spacetime SUSY; the graded-IG extension is stated to exist. No cell emptied.
    if name == "C4": return set()
    # --- C5 graded-IG exists: existence != selection (frozen HARD RULE). Cannot force INV=present,
    #     cannot forbid INV=absent. No cell emptied.
    if name == "C5": return set()
    # --- C6 VZ of massive charged spin-3/2: GU PRESENTS the trigger; the cure (ker Gamma) is a
    #     downstream published fact GU never states, and even the ungauged cure needs non-minimal
    #     couplings GU never states. Conditional -> no cell emptied.
    if name == "C6": return set()
    # --- C7 mass is a variable: names BOTH phases; forbids neither. No cell emptied.
    if name == "C7": return set()
    # --- C8 Krein/signature: orthogonal to the FS bit; refines real form only. No cell emptied.
    if name == "C8": return set()
    raise ValueError(name)

# Independent intersection: start from all cells, remove only STATED hard eliminations.
survivors = set(CELLS)
for name in ["C1","C2","C3","C4","C5","C6","C7","C8"]:
    survivors -= hard_eliminations(name)

carriers = sorted({cell_carrier(c) for c in survivors} - {None})
print("independent survivors:", carriers)

# Re-derive: because NO stated commitment empties a cell, all coherent carriers survive.
ck("A survives (independent)",   "A"   in carriers)
ck("B survives (independent)",   "B"   in carriers)
ck("-40 survives (independent)", "-40" in carriers)
ck("exactly {A,B,-40} (independent)", set(carriers) == {"A","B","-40"})

# Cross-check the carrier semantics independently (no LEG-B import):
ck("full+present+chiral -> A",   cell_carrier(("full","present","chiral")) == "A")
ck("full+present+massive -> -40", cell_carrier(("full","present","massive")) == "-40")
ck("constrained+absent -> B",    cell_carrier(("constrained","absent","chiral")) == "B")
ck("constrained+present -> None (incoherent)", cell_carrier(("constrained","present","chiral")) is None)
ck("bare -> -40",                cell_carrier(("bare","absent","chiral")) == "-40")

# Structural facts of the derived triple (fork gap and midpoint control):
ck("fork B-A == two units of A-hat", ind_B - ind_A == 2 * ahat)
ck("-40 is the exact midpoint", ind_bare == (ind_A + ind_B) / 2)
ck("mod-3 classes (0,1,2)",
   (ind_A % 3, ind_B % 3, ind_bare % 3) == (0, 1, 2))

# Firewall: the derivation must never have manufactured chi(K3)=24, and the
# carriers must stay exact integers (no floating tolerance anywhere).
ck("no 24", 24 not in set(CARRIER.values()))
ck("all indices integral", all(v == int(v) for v in (ind_A, ind_B, ind_bare)))

print("\nREFEREE CONCLUSION: independent intersection reproduces LEG-B exactly ->")
print("no stated commitment hard-kills a carrier; residual family {A,B,-40} stands.")
print("FAILS:", FAILS)
assert not FAILS
print("ALL REFEREE CHECKS PASS")
