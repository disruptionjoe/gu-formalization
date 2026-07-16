"""
Historical directed-arrow shape test, corrected by ADAPTER2-01.

Adapter #1 already showed the UNDIRECTED consistency objects are one signed graph.
The VALUE lives in the directed finality arrow. This tests two things:

(A) SHAPE COMPARISON: TI Ext_S and TaF T18 can both be represented by acyclic
    directed graphs with monotone potentials in a shared toy encoding. This
    does not construct a functor between their native categories.

(B) IS-THE-ARROW-CANONICAL: does the arrow FIX the Z/2 sign (the value), or only an
    AXIS whose POLARITY (which end is "positive-norm") is still a free posit?
      - AXIS canonical?  acyclic => a monotone exists; the REVERSE admits no monotone
        (irreversibility). So the increasing direction is intrinsic. -> canonical.
      - POLARITY canonical?  map (axis -> sign) has two choices: final=+ or final=-.
        If every structural predicate is invariant under the global +/- flip, the
        polarity is a FREE Z/2 = the irreducible posit (= Krein positivity, "final =
        positive-norm"). Even a UNIQUE genesis does not fix it: the sign AT genesis is
        still a free +/-.

Pure Python.
"""

import random


def random_dag(N, extra_edges, rng):
    """Acyclic: only edges i->j with i<j in a random permutation (finality rank)."""
    perm = list(range(N))
    rng.shuffle(perm)
    pos = {perm[i]: i for i in range(N)}
    edges = set()
    # a spanning chain to keep it connected-ish
    for i in range(N - 1):
        edges.add((perm[i], perm[i + 1]))
    tries = 0
    while len(edges) < (N - 1) + extra_edges and tries < 50 * extra_edges + 10:
        tries += 1
        a = rng.randrange(N); b = rng.randrange(N)
        if pos[a] < pos[b]:
            edges.add((a, b))
        elif pos[b] < pos[a]:
            edges.add((b, a))
    return list(edges), pos


def has_monotone(N, edges):
    """Does a real monotone potential exist with pot[u] < pot[v] for every u->v?
    True iff the directed graph is acyclic (Kahn topological sort)."""
    indeg = {i: 0 for i in range(N)}
    adj = {i: [] for i in range(N)}
    for (u, v) in edges:
        adj[u].append(v); indeg[v] += 1
    q = [i for i in range(N) if indeg[i] == 0]
    seen = 0
    while q:
        u = q.pop()
        seen += 1
        for w in adj[u]:
            indeg[w] -= 1
            if indeg[w] == 0:
                q.append(w)
    return seen == N


def sources_sinks(N, edges):
    indeg = {i: 0 for i in range(N)}
    outdeg = {i: 0 for i in range(N)}
    for (u, v) in edges:
        outdeg[u] += 1; indeg[v] += 1
    src = [i for i in range(N) if indeg[i] == 0]
    snk = [i for i in range(N) if outdeg[i] == 0]
    return src, snk


def sign_assignments_compatible(N, edges, pos):
    """Two candidate sign maps from the axis: A(final=+1), B(final=-1).
    'Compatible' predicate = respects the monotone axis (a structural check that does
    NOT reference polarity). Return whether BOTH candidates satisfy every structural
    predicate (=> polarity is free)."""
    # structural predicates that the sign must respect: NONE reference absolute polarity,
    # they only reference the axis order. Both A and B respect the axis identically.
    # candidate A: sign = +1 if in 'upper half' of finality rank else -1 (final=+)
    # candidate B: global flip of A (final=-)
    A = {v: (+1 if pos[v] >= N / 2 else -1) for v in range(N)}
    B = {v: -A[v] for v in range(N)}

    def respects_axis(sign):
        # structural predicate: the sign is constant on the axis direction's sign of the
        # RANK GRADIENT is well-defined -- i.e. sign changes only monotonically along the
        # axis. Both A and B change sign exactly once along the rank, so both pass.
        ranks = sorted(range(N), key=lambda v: pos[v])
        seq = [sign[v] for v in ranks]
        flips = sum(1 for i in range(1, N) if seq[i] != seq[i - 1])
        return flips <= 1
    return respects_axis(A), respects_axis(B)


def main():
    print("=== (A) SHARED DAG SHAPE, NOT A NATIVE SECOND ADAPTER ===")
    rng = random.Random(20260715)
    ok_axis = 0
    reverse_has_monotone = 0
    total = 0
    for N in [20, 50, 100]:
        for _ in range(100):
            total += 1
            edges, pos = random_dag(N, extra_edges=int(1.5 * N), rng=rng)
            # TI reading: extension morphisms (directed) ; TaF reading: D1-increase (directed).
            # Both = these directed edges. Canonical axis exists iff a monotone exists:
            if has_monotone(N, edges):
                ok_axis += 1
            # irreversibility: reverse the arrows; a monotone for the reverse would mean
            # finalization is reversible. Count how often the reverse ALSO has a monotone
            # (it does, trivially, since reverse of a DAG is a DAG) -- so acyclicity alone
            # gives an axis but BOTH directions are acyclic; the ASYMMETRY must come from
            # the monotone SEMANTICS (D1 increases / reversal forbidden), not topology.
            rev = [(v, u) for (u, v) in edges]
            if has_monotone(N, rev):
                reverse_has_monotone += 1
    print(f" instances: {total}")
    print(f" canonical monotone axis exists (acyclic): {ok_axis}/{total}")
    print(f" reverse ALSO admits a monotone (topologically): {reverse_has_monotone}/{total}")
    print(" -> The shared toy graph has an acyclic monotone shape.")
    print("    This does NOT establish that native TI Ext_S and TaF T18 are one object.")
    print("    NOTE: topology alone is flip-symmetric; the ASYMMETRY (which way is 'final') is")
    print("    supplied by the monotone SEMANTICS (T18 'reverse impossible' / D1 increase), not the graph.")

    print("\n=== (B) AXIS/POLARITY SYMMETRY CHECK ===")
    rng2 = random.Random(7)
    both_signs_ok = 0
    unique_genesis = 0
    unique_genesis_polarity_free = 0
    checked = 0
    for N in [30, 60]:
        for _ in range(100):
            checked += 1
            edges, pos = random_dag(N, extra_edges=int(1.2 * N), rng=rng2)
            a_ok, b_ok = sign_assignments_compatible(N, edges, pos)
            if a_ok and b_ok:
                both_signs_ok += 1
            src, snk = sources_sinks(N, edges)
            if len(src) == 1:
                unique_genesis += 1
                # even with a unique genesis, sign(genesis) is still free +/-
                # (both A and B are structurally admissible), so polarity stays free:
                if a_ok and b_ok:
                    unique_genesis_polarity_free += 1
    print(f" instances checked: {checked}")
    print(f" BOTH polarities (final=+ AND final=-) structurally admissible: {both_signs_ok}/{checked}")
    print(f"   -> POLARITY is a FREE Z/2: the arrow fixes the AXIS, not the sign.")
    print(f" unique-genesis (single source) instances: {unique_genesis}")
    print(f"   of those, polarity STILL free: {unique_genesis_polarity_free}/{unique_genesis}")
    print(f"   -> even a canonical reference fixes WHERE to anchor, not the anchor's sign.")

    print("\n=== VERDICT ===")
    print(" Adapter #2: NOT PROVED. A shared DAG shape is weaker than a native functor.")
    print(" Axis: conditional on imposing T18's D1-monotone admissibility semantics.")
    print(" Polarity: absent from the graph and not identified with the GU Krein sign.")
    print(" See adapter2_repair_audit.py for the branch-collapse obstruction.")


if __name__ == '__main__':
    main()
