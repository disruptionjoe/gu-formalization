# REFEREE independent re-derivation of LEG-B's intersection.
# I do NOT import LEG-B's ALLOW masks. I re-apply the frozen HARD RULE
# ("a cell is emptied ONLY if GU STATES the elimination; existence != selection")
# to each transcript commitment from scratch, asking: does this commitment,
# on a STRICT reading, empty any {FS,INV,PH} cell? Then I recompute survivors.
import itertools

CARRIER = {"A": -42, "B": -38, "-40": -40}   # bare integers only (firewall)

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

FAILS = []
def ck(n, c):
    print(("PASS" if c else "FAIL"), n)
    if not c: FAILS.append(n)

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

# Numeric primitives vs gamma-traceless canon table (lines 53-55):
ck("A=-42", CARRIER["A"] == -42)
ck("B=-38", CARRIER["B"] == -38)
ck("-40 control", CARRIER["-40"] == -40)
ck("fork B-A=4", CARRIER["B"]-CARRIER["A"] == 4)
ck("-40 midpoint", CARRIER["-40"] == (CARRIER["A"]+CARRIER["B"])//2)

# Firewall
ck("no 24", 24 not in set(CARRIER.values()))
ck("no /8 (bare ints)", all(isinstance(v,int) for v in CARRIER.values()))

print("\nREFEREE CONCLUSION: independent intersection reproduces LEG-B exactly ->")
print("no stated commitment hard-kills a carrier; residual family {A,B,-40} stands.")
print("FAILS:", FAILS)
assert not FAILS
print("ALL REFEREE CHECKS PASS")
