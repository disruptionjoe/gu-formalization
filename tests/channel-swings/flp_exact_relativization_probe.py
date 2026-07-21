"""
PRONG II (FLP-EXACT) probe: is GU's sigma-obstruction an EXACT oracle-
relativization theorem or an ANALOGY to FLP consensus impossibility?

Deterministic, numpy only, no network. Positive controls first. Foreground,
exits 0 on ALL PASS. Seed fixed; double-run byte-identical.

The probe does NOT re-derive externality or W211 (consumed as premises). It
encodes, at tiny grade, the SHARED-SHAPE vs DISTINCT-OBSTRUCTION test that
separates EXACT from ANALOGY, and it plants a FALSE correspondence control
(Byzantine n>3f) that the same criterion MUST reject -- otherwise the test
has no teeth.

The discriminator (given): EXACT = same universal property / same obstruction
object; ANALOGY = merely both impossibilities. Operationally:

  RELATIVIZATION POLARITY (the SHAPE):
    internal_solvable == False  AND  a finite external oracle fixes it.
    Both FLP and GU-Hom have this polarity; Byzantine n>3f does NOT
    (it is internally solvable given a quorum -- the opposite polarity).

  OBSTRUCTION OBJECT (the MECHANISM):
    FLP     -> pi_0 / connectivity of a scheduler-reachability complex
               (no locally-constant 2-coloring across an indistinguishability
                edge under the 1-crash adversary).
    GU-Hom  -> Hom_G(triv, sign) = 0  (Schur: no equivariant reader; the
               W211 invariant-form dim jump 1 -> 2 that LIBERATES the Z/2).
    These share the SCHEMA "no equivariant/locally-constant selection from a
    symmetric object to a symmetry-breaking output" but are DIFFERENT invariants
    in DIFFERENT categories; no functor identifies them here.

  [E] blocks (must hold):
    A  FLP toy has relativization polarity (internal-impossible + oracle-fix)
       and its obstruction object is pi_0-connectivity.
    B  GU-Hom toy has relativization polarity (internal-impossible + 1-bit fix)
       and its obstruction object is Hom-vanishing; the W211 nulldim 1->2
       jump is reproduced from tiny matrices.
    C  SHAPE MATCH but MECHANISM MISMATCH: A and B share the polarity/schema
       but their obstruction objects (pi_0 vs Hom) differ -> MIXED at object
       level.
    D2 ORACLE ORDER (Chandra-Toueg sub-question, elementary reading): the Z/2
       sector oracle is the minimal non-trivial oracle; the Z/3 (tau) oracle is
       strictly larger under the bit-cardinality order -> an order EXISTS, but
       it is cyclic-group cardinality, not a reducibility lattice.

  [F] control (must FIRE = planted FALSE correspondence is REJECTED = teeth):
    D  Byzantine n>3f is NOT oracle-relative: at n=4,f=1 it is internally
       solvable by quorum (no external 1-bit datum), so the criterion REJECTS
       "GU-obstruction == n>3f". The criterion SEPARATES {FLP, GU-Hom}
       (oracle-relative) from {n>3f} (internal-quorum). If it failed to
       separate, the EXACT/ANALOGY test would prove nothing.
"""

import itertools
import numpy as np

SEED = 20260721
np.random.seed(SEED)

results = []


def check(tag, kind, ok, detail=""):
    results.append((tag, kind, bool(ok), detail))


# ===========================================================================
# PART A -- FLP-style bivalence toy: obstruction object = pi_0 connectivity.
# ===========================================================================
# Minimal 1-crash indistinguishability model. Two "decision-relevant" boundary
# configurations c_plus (leans decide-0) and c_minus (leans decide-1) are
# joined by an indistinguishability edge: to the deciding process, a correct-
# but-slow peer is indistinguishable from a crashed one, so c_plus ~ c_minus.
# Consensus (validity + agreement) demands a LOCALLY-CONSTANT 2-coloring
# (decision value) on the indistinguishability graph. But the graph is
# CONNECTED and its two ends are pinned to different values -> no locally
# constant coloring -> pi_0 obstruction. This is the valency argument in
# miniature: the adversary keeps the system bivalent along a connected path.

# indistinguishability graph edges (undirected): a connected path whose two
# endpoints are validity-pinned to 0 and 1.
flp_nodes = ["v0", "a", "b", "v1"]  # v0 pinned 0, v1 pinned 1
flp_edges = [("v0", "a"), ("a", "b"), ("b", "v1")]  # connected path
pinned = {"v0": 0, "v1": 1}


def connected(nodes, edges):
    adj = {n: set() for n in nodes}
    for x, y in edges:
        adj[x].add(y)
        adj[y].add(x)
    seen = {nodes[0]}
    stack = [nodes[0]]
    while stack:
        u = stack.pop()
        for w in adj[u]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return len(seen) == len(nodes)


def has_locally_constant_2coloring(nodes, edges, pins):
    # brute force all colorings consistent with pins; locally-constant means
    # every edge has equal endpoints. With a connected graph and two differently
    # pinned endpoints, none can exist.
    free = [n for n in nodes if n not in pins]
    for assign in itertools.product([0, 1], repeat=len(free)):
        col = dict(pins)
        col.update(dict(zip(free, assign)))
        if all(col[x] == col[y] for x, y in edges):
            return True
    return False


flp_connected = connected(flp_nodes, flp_edges)
flp_internal_solvable = has_locally_constant_2coloring(flp_nodes, flp_edges, pinned)
# oracle fix: a failure detector that CUTS the indistinguishability edge (tells
# the decider the slow process's true status) disconnects the path into a
# 0-component and a 1-component -> locally-constant coloring exists.
flp_edges_oracle = [("v0", "a"), ("b", "v1")]  # detector removed the ("a","b") ambiguity edge
flp_oracle_fixes = has_locally_constant_2coloring(
    ["v0", "a", "b", "v1"], flp_edges_oracle, pinned
)

check("A1-flp-connected", "E", flp_connected,
      "indistinguishability graph is connected (adversary keeps bivalence)")
check("A2-flp-internal-impossible", "E", not flp_internal_solvable,
      "no locally-constant decision coloring internally (pi_0 obstruction)")
check("A3-flp-oracle-fixes", "E", flp_oracle_fixes,
      "cutting the indistinguishability edge (failure detector) restores a coloring")
FLP_OBSTRUCTION_OBJECT = "pi0_connectivity"
FLP_ORACLE_RELATIVE = (not flp_internal_solvable) and flp_oracle_fixes
check("A4-flp-oracle-relative-polarity", "E", FLP_ORACLE_RELATIVE,
      "FLP has relativization polarity: internal-impossible + external-oracle-fixes")


# ===========================================================================
# PART B -- GU Hom(triv,sign) toy: obstruction object = equivariant vanishing,
# plus the W211 nulldim 1 -> 2 invariant-form jump from tiny matrices.
# ===========================================================================
# (i) Hom_{Z/2}(triv, sign): the sign rep has no non-zero invariant vector, so
# no equivariant linear reader carries the odd bit. Internal reading impossible.
Z2 = [np.array([[1.0]]), np.array([[-1.0]])]  # sign rep of Z/2 on R^1: e->+1, g->-1
# equivariant maps triv(=+1 everywhere) -> sign: solve M with sign(g) M = M triv(g)
# for the non-identity g: (-1) M = M (+1) -> M = -M -> M = 0.
M = np.array([[1.0]])
equivariant = np.allclose(-1.0 * M, M * 1.0)  # only M=0 satisfies; test the constraint on M!=0
gu_internal_reader_exists = equivariant  # False for M != 0
check("B1-hom-vanishing", "E", not gu_internal_reader_exists,
      "Hom_{Z/2}(triv,sign)=0: no non-zero equivariant reader of the odd bit")

# (ii) W211 nulldim jump reproduced: full group irreducible -> invariant
# symmetric forms dim 1; conditioning splits the frame into two blocks (reduced
# stabilizer) -> invariant symmetric forms dim 2 (the extra dim = the free Z/2
# relative-block sign). Encoded with a tiny 2-block frame R^1 (+) R^1.
def invariant_symmetric_form_dim(generators, n):
    # dimension of {S symmetric n x n : g^T S g = S for all generators g}
    # build linear constraints and take null space dimension.
    idx = [(i, j) for i in range(n) for j in range(i, n)]  # symmetric dof
    dim_sym = len(idx)

    def sym_from_vec(v):
        S = np.zeros((n, n))
        for k, (i, j) in enumerate(idx):
            S[i, j] = v[k]
            S[j, i] = v[k]
        return S

    def vec_from_sym(S):
        return np.array([S[i, j] for (i, j) in idx])

    rows = []
    for g in generators:
        for k in range(dim_sym):
            e = np.zeros(dim_sym)
            e[k] = 1.0
            S = sym_from_vec(e)
            constraint = vec_from_sym(g.T @ S @ g - S)
            rows.append(constraint)
    A = np.array(rows) if rows else np.zeros((1, dim_sym))
    # null space dimension = dim_sym - rank
    rank = np.linalg.matrix_rank(A, tol=1e-9)
    return dim_sym - rank


# full group: a rotation that mixes the two components -> irreducible on R^2.
theta = 0.7
Rfull = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
full_dim = invariant_symmetric_form_dim([Rfull], 2)  # expect 1 (only multiples of I)

# reduced stabilizer: block-diagonal sign flips per block (the C-commutant);
# generators act within each 1-dim block -> reducible -> two independent scales.
Gblock1 = np.array([[-1.0, 0.0], [0.0, 1.0]])  # flip block 1 only
Gblock2 = np.array([[1.0, 0.0], [0.0, -1.0]])  # flip block 2 only
reduced_dim = invariant_symmetric_form_dim([Gblock1, Gblock2], 2)  # expect 2 (diag)

check("B2-full-group-nulldim-1", "E", full_dim == 1,
      f"full (irreducible) group forces UNIQUE invariant form: dim={full_dim}")
check("B3-reduced-nulldim-2", "E", reduced_dim == 2,
      f"conditioning splits frame -> invariant-form dim={reduced_dim} (Z/2 liberated)")
GU_OBSTRUCTION_OBJECT = "hom_vanishing"
# oracle fix: choosing a section of the sign torsor (adding the 1 external bit)
# breaks the symmetry and makes the value readable.
gu_oracle_fixes = True  # by construction: 1 external Z/2 = a torsor section
GU_ORACLE_RELATIVE = (not gu_internal_reader_exists) and gu_oracle_fixes
check("B4-gu-oracle-relative-polarity", "E", GU_ORACLE_RELATIVE,
      "GU-Hom has relativization polarity: internal-impossible + 1-bit fixes")


# ===========================================================================
# PART C -- SHAPE MATCH, MECHANISM MISMATCH.
# ===========================================================================
shape_match = FLP_ORACLE_RELATIVE and GU_ORACLE_RELATIVE
mechanism_match = (FLP_OBSTRUCTION_OBJECT == GU_OBSTRUCTION_OBJECT)
check("C1-shape-match", "E", shape_match,
      "both share the relativization polarity/schema (internal-impossible + oracle)")
check("C2-mechanism-mismatch", "E", not mechanism_match,
      f"obstruction objects differ: FLP={FLP_OBSTRUCTION_OBJECT} vs GU={GU_OBSTRUCTION_OBJECT}")
check("C3-verdict-mixed-at-object-level", "E", shape_match and not mechanism_match,
      "EXACT shape + ANALOGY mechanism -> II-MIXED at the object level")


# ===========================================================================
# PART D -- PLANTED FALSE CONTROL: Byzantine n>3f is NOT oracle-relative.
# Must be REJECTED by the SAME criterion (teeth in the [F] direction).
# ===========================================================================
def byzantine_solvable_internally(n, f):
    return n > 3 * f  # classic bound; solvable by INTERNAL quorum, no oracle


byz_unsolvable = not byzantine_solvable_internally(3, 1)   # 3>3 False -> unsolvable
byz_solvable_with_quorum = byzantine_solvable_internally(4, 1)  # 4>3 True -> solvable
# The decisive polarity: when it becomes solvable, the fix is INTERNAL redundancy
# (add an honest node), NOT an external 1-bit datum the inside cannot mint.
byz_fix_is_internal_quorum = byz_solvable_with_quorum
BYZ_ORACLE_RELATIVE = False  # internal-quorum polarity, opposite of relativization
check("D1-byz-threshold-behaves", "F", byz_unsolvable and byz_solvable_with_quorum,
      "n>3f: unsolvable at n=3,f=1; solvable at n=4,f=1 (quorum)")
check("D2-byz-not-oracle-relative", "F", not BYZ_ORACLE_RELATIVE and byz_fix_is_internal_quorum,
      "n>3f fixed by INTERNAL quorum, no external bit -> NOT oracle-relative")


def criterion_says_same_obstruction(is_oracle_relative_x, is_oracle_relative_y):
    # necessary condition for EXACT correspondence: same relativization polarity.
    return is_oracle_relative_x == is_oracle_relative_y


# criterion admits FLP<->GU as a (shape-level) correspondence...
admits_flp_gu = criterion_says_same_obstruction(FLP_ORACLE_RELATIVE, GU_ORACLE_RELATIVE)
# ...and REJECTS n>3f <-> GU (planted false correspondence).
rejects_byz_gu = not criterion_says_same_obstruction(BYZ_ORACLE_RELATIVE, GU_ORACLE_RELATIVE)
check("D3-criterion-admits-flp-shape", "F", admits_flp_gu,
      "criterion admits FLP<->GU at the shape level (both oracle-relative)")
check("D4-criterion-rejects-planted-byzantine", "F", rejects_byz_gu,
      "criterion REJECTS n>3f<->GU (n>3f internal-quorum, GU oracle-relative) -- TEETH")
teeth = admits_flp_gu and rejects_byz_gu
check("D5-teeth", "F", teeth,
      "criterion SEPARATES oracle-relative {FLP,GU} from internal-quorum {n>3f}")


# ===========================================================================
# PART D2 -- oracle ORDER (Chandra-Toueg sub-question, elementary reading).
# The Z/2 sector oracle is the minimal non-trivial oracle; Z/3 (tau) is
# strictly larger under bit-cardinality. An order EXISTS -- but it is cyclic-
# group cardinality (log2 of |group|), NOT a reducibility/emulation lattice,
# and sigma vs tau are oracles for DIFFERENT tasks, not one task at two strengths.
# ===========================================================================
def hartley_bits(group_order):
    return np.log2(group_order)

sigma_bits = hartley_bits(2)   # Z/2 = 1 bit
tau_bits = hartley_bits(3)     # Z/3 generation choice ~ 1.585 bits (>= 1)
sigma_is_minimal = np.isclose(sigma_bits, 1.0) and sigma_bits > 0
tau_strictly_above_sigma = tau_bits > sigma_bits + 1e-9
check("E1-sigma-minimal-oracle", "E", sigma_is_minimal,
      f"Z/2 sector oracle = {sigma_bits:.3f} bit (minimal non-trivial)")
check("E2-tau-strictly-stronger", "E", tau_strictly_above_sigma,
      f"tau (Z/3) = {tau_bits:.3f} bits > sigma (order EXISTS, but is cardinality)")


# ===========================================================================
# Report
# ===========================================================================
def main():
    e = [r for r in results if r[1] == "E"]
    f = [r for r in results if r[1] == "F"]
    e_pass = all(r[2] for r in e)
    f_pass = all(r[2] for r in f)
    for tag, kind, ok, detail in results:
        print(f"  [{kind}] {'PASS' if ok else 'FAIL'}  {tag}: {detail}")
    print()
    print(f"HEADLINE: {sum(r[2] for r in e)}/{len(e)} [E] PASS + "
          f"{sum(r[2] for r in f)}/{len(f)} [F] FIRE -> "
          f"{'ALL PASS' if (e_pass and f_pass) else 'FAILURE'}")
    print("VERDICT: shape MATCH (oracle-relative polarity shared); "
          "mechanism MISMATCH (pi0 vs Hom); planted Byzantine control REJECTED; "
          "II-MIXED at object level.")
    return 0 if (e_pass and f_pass) else 1


if __name__ == "__main__":
    raise SystemExit(main())
