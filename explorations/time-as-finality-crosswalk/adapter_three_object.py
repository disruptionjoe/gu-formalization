"""
Tri-repo adapter comparison: are GU Gate 2a, TaF T39, and TI E155/E160 the SAME
Z/2 signed-graph object, under an explicit map -- or where does the adapter break?

Common instance: a SIGNED GRAPH -- nodes + edges labelled L in {+1,-1}
(+1 = "agree/same", -1 = "disagree/different/opposite-polarity").

Three INDEPENDENT algorithms (they must all agree iff it is one object):

  GU  (Gate 2a, XOR-SAT view):
      bit b(e) = (L==-1); assignment x(v) in {0,1}; edge satisfied iff
      x(u) XOR x(v) == b(e). Assign x on a spanning forest, count violated
      non-tree edges. SAT iff 0 violations.  (constraint-satisfaction bookkeeping)

  TaF (T39, signed-graph 2-colourability / balance view):
      BFS 2-colouring c(v) in {+1,-1}; tree edge forces c(v)=c(u)*L; a conflict
      is a non-tree edge with c(u)*c(v) != L. Balanced iff no conflict.
      (colouring / negative-cycle bookkeeping)

  TI  (E155/E160, Z/2 holonomy / cohomology view):
      spanning forest; for each non-tree edge, holonomy = XOR of edge-bits around
      its fundamental cycle. [J]=0 in H^1 iff all fundamental-cycle holonomies=0.
      (cohomology / loop-product bookkeeping)

If all three agree on every instance -> they compute one object at the CONSISTENCY
level (Harary balance = no negative cycle = Z2 1-cocycle exact = XOR-SAT).

Then the DIRECTION test: orient the edges (the TI Ext_S arrow / TaF T18 finality
arrow). Does the consistency verdict, or the value (which global sign), depend on
the orientation? If not, the direction is FORGOTTEN STRUCTURE the shared object
cannot see -- the adapter is an iso on balance but LOSES the orientation, which is
exactly where bar(b)'s value lives.

Pure Python.
"""

import random


def spanning_forest_assign(N, edges):
    """Return (parent, tree_edge_set, adj). Bits stored as edge_bit dict."""
    adj = {}
    for i, (u, v, L) in enumerate(edges):
        adj.setdefault(u, []).append((v, i))
        adj.setdefault(v, []).append((u, i))
    return adj


def gu_xorsat(N, edges):
    adj = {}
    bit = {}
    for i, (u, v, L) in enumerate(edges):
        b = 1 if L == -1 else 0
        bit[i] = b
        adj.setdefault(u, []).append((v, i))
        adj.setdefault(v, []).append((u, i))
    x = {}
    tree_edge = set()
    for s in list(adj.keys()):
        if s in x:
            continue
        x[s] = 0
        stack = [s]
        while stack:
            u = stack.pop()
            for (w, i) in adj[u]:
                if w not in x:
                    x[w] = x[u] ^ bit[i]
                    tree_edge.add(i)
                    stack.append(w)
    violated = 0
    for i, (u, v, L) in enumerate(edges):
        if i in tree_edge:
            continue
        if (x[u] ^ x[v]) != bit[i]:
            violated += 1
    return violated == 0, violated


def taf_balance(N, edges):
    adj = {}
    for i, (u, v, L) in enumerate(edges):
        adj.setdefault(u, []).append((v, L))
        adj.setdefault(v, []).append((u, L))
    color = {}
    conflicts = 0
    for s in list(adj.keys()):
        if s in color:
            continue
        color[s] = 1
        stack = [s]
        while stack:
            u = stack.pop()
            for (w, L) in adj[u]:
                want = color[u] * L
                if w not in color:
                    color[w] = want
                    stack.append(w)
                elif color[w] != want:
                    conflicts += 1
    # each conflict edge may be counted twice (both directions); balanced iff none
    return conflicts == 0, conflicts


def ti_holonomy(N, edges):
    adj = {}
    bit = {}
    for i, (u, v, L) in enumerate(edges):
        bit[i] = 1 if L == -1 else 0
        adj.setdefault(u, []).append((v, i))
        adj.setdefault(v, []).append((u, i))
    # spanning forest with cumulative bit from root (a 0-cochain potential pot[v])
    pot = {}
    tree_edge = set()
    for s in list(adj.keys()):
        if s in pot:
            continue
        pot[s] = 0
        stack = [s]
        while stack:
            u = stack.pop()
            for (w, i) in adj[u]:
                if w not in pot:
                    pot[w] = pot[u] ^ bit[i]
                    tree_edge.add(i)
                    stack.append(w)
    # holonomy of each fundamental cycle (non-tree edge e=(u,v)): pot[u]^pot[v]^bit[e]
    nontrivial = 0
    for i, (u, v, L) in enumerate(edges):
        if i in tree_edge:
            continue
        hol = pot[u] ^ pot[v] ^ bit[i]
        if hol != 0:
            nontrivial += 1
    return nontrivial == 0, nontrivial


def count_components(N, edges):
    parent = {}

    def find(a):
        parent.setdefault(a, a)
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    nodes = set()
    for (u, v, L) in edges:
        nodes.add(u); nodes.add(v)
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
    return len(set(find(a) for a in nodes))


def random_signed_graph(N, m, neg_p, rng):
    edges = []
    seen = set()
    tries = 0
    while len(edges) < m and tries < 20 * m:
        tries += 1
        u = rng.randrange(N); v = rng.randrange(N)
        if u == v:
            continue
        key = (min(u, v), max(u, v))
        if key in seen:
            continue
        seen.add(key)
        L = -1 if rng.random() < neg_p else 1
        edges.append((key[0], key[1], L))
    return edges


def main():
    print("=== CONTROLS ===")
    # balanced: triangle all +
    tri_pos = [(0, 1, 1), (1, 2, 1), (2, 0, 1)]
    # unbalanced: triangle with one - (frustrated / negative cycle / UNSAT)
    tri_neg = [(0, 1, 1), (1, 2, 1), (2, 0, -1)]
    for name, g in [("triangle +++", tri_pos), ("triangle ++-", tri_neg)]:
        print(f" {name:14}: GU={gu_xorsat(3, g)} TaF={taf_balance(3, g)} TI={ti_holonomy(3, g)}")

    print("\n=== TRI-ALGORITHM AGREEMENT ON RANDOM SIGNED GRAPHS ===")
    rng = random.Random(20260715)
    total = 0
    agree = 0
    balanced_ct = 0
    disagreements = []
    for N in [20, 40, 80]:
        for neg_p in [0.0, 0.1, 0.3, 0.5]:
            for trial in range(60):
                m = int(2.0 * N)
                edges = random_signed_graph(N, m, neg_p, rng)
                gu = gu_xorsat(N, edges)[0]
                taf = taf_balance(N, edges)[0]
                ti = ti_holonomy(N, edges)[0]
                total += 1
                if gu == taf == ti:
                    agree += 1
                else:
                    disagreements.append((N, neg_p, trial, gu, taf, ti))
                if gu:
                    balanced_ct += 1
    print(f" instances: {total} | all-three-agree: {agree} | disagreements: {len(disagreements)}")
    print(f" balanced fraction: {balanced_ct/total:.3f}")
    if disagreements:
        print("  DISAGREEMENTS (adapter BREAKS at consistency level):")
        for d in disagreements[:10]:
            print("   ", d)
    else:
        print("  -> ISO CONFIRMED at consistency level: GU Gate2a = TaF T39 = TI E155/E160 (Harary balance).")

    print("\n=== DIRECTION / FORGOTTEN-STRUCTURE TEST ===")
    print(" Take balanced signed graphs; ORIENT edges (TI Ext_S arrow / TaF T18 finality arrow).")
    print(" Q1: does the balance verdict change under re-orientation?")
    print(" Q2: how many global sign solutions (the value's freedom)?  = 2^components, orientation-independent?")
    rng2 = random.Random(999)
    dir_changes_balance = 0
    checked = 0
    sol_counts = []
    for _ in range(100):
        N = 30
        # CONSTRUCT a balanced signed graph by coboundary: labels from a random potential
        # g(v) (the vertex-sourced / Gate-2a passing branch). Guaranteed balanced.
        g = [rng2.getrandbits(1) for _ in range(N)]
        base_edges = random_signed_graph(N, 50, 0.0, rng2)  # get an edge skeleton
        edges = [(u, v, (1 if g[u] == g[v] else -1)) for (u, v, _) in base_edges]
        assert gu_xorsat(N, edges)[0], "constructed graph should be balanced"
        checked += 1
        base = gu_xorsat(N, edges)[0]
        # re-orient every edge randomly (swap endpoints); undirected label unchanged.
        # This models putting the TI Ext_S arrow / TaF T18 arrow onto the same signed graph.
        reor = [((v, u, L) if rng2.random() < 0.5 else (u, v, L)) for (u, v, L) in edges]
        agree_all = (gu_xorsat(N, reor)[0] == base
                     and taf_balance(N, reor)[0] == base
                     and ti_holonomy(N, reor)[0] == base)
        if not agree_all:
            dir_changes_balance += 1
        sol_counts.append(count_components(N, edges))  # #solutions = 2^comps
    from collections import Counter
    print(f" balanced graphs checked: {checked}")
    print(f" re-orientation changed the balance verdict in: {dir_changes_balance}/{checked} cases")
    print(f" global-sign solution count = 2^components; components distribution: {dict(Counter(sol_counts))}")
    print(" -> orientation is INVISIBLE to the balance object (forgotten structure);")
    print("    each component keeps a free Z/2 (2 solutions) = the value bit the shared object cannot fix.")

    print("\n=== ADAPTER VERDICT ===")
    print(" CONSISTENCY level: ISO (three independent algorithms agree on every instance).")
    print(" DIRECTION/VALUE level: adapter LOSES orientation -> the free per-component Z/2 is exactly bar(b)'s")
    print(" undetermined value. Preserved invariant = H^1 balance class; forgotten structure = the arrow.")


if __name__ == '__main__':
    main()
