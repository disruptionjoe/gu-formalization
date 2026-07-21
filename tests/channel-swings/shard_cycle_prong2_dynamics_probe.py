#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prong 2 (DYNAMICS, Gorard/Wolfram/CA) probe -- oriented-shard-cycle swing.
Prereg: explorations/prereg-oriented-shard-cycle-swing-2026-07-21.md

QUESTION
  Can a CAUSAL-INVARIANT hypergraph/string-rewriting rule, externally seeded,
  generate the oriented shard-cycle WITHOUT a backward-causality paradox, and
  does *causal invariance* deliver the "circle-not-DAG" third-person structure
  the model claims?

METHOD (Gorard's 1D case = tokenized string rewriting)
  * State  = tuple of tokens (symbol, unique-id).  Issuance = a rewrite.
  * Multiway system = all rewrites applicable to a state.
  * CAUSAL edge  E1 -> E2  iff  produced(E1) ∩ consumed(E2) != {}   (Gorard's
    causal-edge definition, transcript lines 255-259).
  * CAUSAL INVARIANCE (operationalised as Church-Rosser confluence): do all
    branches of the multiway system re-join?  (source pack: order-isomorphic
    causal graphs across branches = discrete general covariance.)
  * ACYCLICITY of the causal graph (Kahn topological sort) = "no backward
    causality" = no closed timelike curve (transcript line 249: in a Wolfram
    causal graph "you never see a cycle").
  * TYPE-QUOTIENT: collapse tokens by shard TYPE (S/I/O). Is the quotient the
    oriented 3-cycle S->I->O->S ?

THREE SYSTEMS
  REAL      confluent; causal graph is an acyclic HELIX; its TYPE-quotient is
            the oriented 3-cycle.  The seam O->S mints a FRESH token (the model's
            q<0 / null-K_S stratum: direction undefined at the join => NO causal
            edge is written there).
  CONTROL-A NON-confluent critical pair (branches never rejoin) -> the
            causal-invariance test MUST catch branch-divergence.
  CONTROL-B identical issuance but the seam WELDS O's output back onto the seed's
            token id (same-token identification) -> a real causal CYCLE ->
            the acyclicity test MUST fail (the backward-causality paradox).

CRITERION (must be non-vacuous):  coherent := confluent AND acyclic-causal-graph.
  REAL passes both; CONTROL-A violates conjunct 1; CONTROL-B violates conjunct 2.
  If a control did NOT fail, "coherent" would be vacuous -> probe exits non-zero.

The probe is a DECISION instrument for the D-COHERENT / D-INCOHERENT / D-ANALOGY
verdict, not evidence that GU *is* a Wolfram model.  Its load-bearing readout:
the 3-cycle lives ONLY in the type-quotient; the causal graph itself is a DAG.
Hence causal invariance yields the invariant DAG, not the circle (see artifact).
"""

import sys
from itertools import count

_ids = count()


def fresh():
    return next(_ids)


# ---------------------------------------------------------------------------
# core rewriting engine
# ---------------------------------------------------------------------------

def canonical(state):
    """Structural form -- ignore token ids (Gorard: hyperedges are just data)."""
    return "".join(sym for sym, _ in state)


def matches(state, i, lhs):
    if i + len(lhs) > len(state):
        return False
    return all(state[i + k][0] == lhs[k] for k in range(len(lhs)))


def apply_at(state, i, prod):
    """
    Apply one production at position i. Returns (new_state, event).
    prod = (lhs, rhs, seam) where seam controls the id policy of the produced
    tokens:  None            -> all fresh ids (generic issuance)
             ('weld', anc)    -> the single produced token reuses ancestor id
                                 `anc` (models same-token loop closure).
    event = dict(consumed=set_of_ids, produced=set_of_ids,
                 c_type=type_of_active_consumed, p_type=type_of_produced).
    """
    lhs, rhs, seam = prod
    consumed_tokens = state[i:i + len(lhs)]
    consumed_ids = {tid for _, tid in consumed_tokens}

    if seam is not None and seam[0] == "weld":
        anc = seam[1]
        assert len(rhs) == 1, "weld seam expects a single produced token"
        new_tokens = [(rhs[0], anc)]
    else:
        new_tokens = [(sym, fresh()) for sym in rhs]

    produced_ids = {tid for _, tid in new_tokens}
    new_state = state[:i] + tuple(new_tokens) + state[i + len(lhs):]

    # active consumed type = last consumed token's symbol; produced type = first rhs
    c_type = consumed_tokens[-1][0] if consumed_tokens else None
    p_type = rhs[0] if rhs else None
    event = dict(consumed=consumed_ids, produced=produced_ids,
                 c_type=c_type, p_type=p_type)
    return new_state, event


def successors(state, rules):
    """All (new_state, event, key) reachable by one rewrite. key = (rule_idx, i)."""
    out = []
    for r_idx, prod in enumerate(rules):
        lhs = prod[0]
        for i in range(len(state)):
            if matches(state, i, lhs):
                # seam callbacks may depend on the concrete match -> resolve here
                resolved = prod
                if len(prod) == 4:  # (lhs, rhs, 'dynamic-seam', fn)
                    resolved = (prod[0], prod[1], prod[3](state, i))
                ns, ev = apply_at(state, i, resolved)
                out.append((ns, ev, (r_idx, i)))
    return out


# ---------------------------------------------------------------------------
# causal-invariance (confluence / Church-Rosser) over canonical states
# ---------------------------------------------------------------------------

def reachable(rules, seed, horizon, max_len):
    """BFS over CANONICAL states; returns adjacency canonical -> set(canonical)."""
    start = canonical(seed)
    # keep one representative concrete state per canonical form
    rep = {start: seed}
    adj = {}
    frontier = [start]
    depth = 0
    while frontier and depth < horizon:
        nxt = []
        for c in frontier:
            if c in adj:
                continue
            st = rep[c]
            succ = set()
            for ns, _ev, _k in successors(st, rules):
                if len(ns) > max_len:
                    continue
                cn = canonical(ns)
                succ.add(cn)
                if cn not in rep:
                    rep[cn] = ns
                    nxt.append(cn)
            adj[c] = succ
        frontier = nxt
        depth += 1
    for c in frontier:  # fill leaves at horizon
        adj.setdefault(c, set())
    return adj


def descendants(adj, c, horizon):
    seen = {c}
    frontier = [c]
    d = 0
    while frontier and d < horizon:
        nxt = []
        for x in frontier:
            for y in adj.get(x, ()):
                if y not in seen:
                    seen.add(y)
                    nxt.append(y)
        frontier = nxt
        d += 1
    return seen


def is_confluent(rules, seed, horizon=12, max_len=6):
    """
    Church-Rosser (bounded): every canonical state whose distinct successors do
    not all share a common descendant within the horizon is a divergence witness.
    """
    adj = reachable(rules, seed, horizon, max_len)
    for c, succ in adj.items():
        succ = [s for s in succ if s != c]
        if len(succ) < 2:
            continue
        # pairwise joinability
        dsets = {s: descendants(adj, s, horizon) for s in succ}
        for a_idx in range(len(succ)):
            for b_idx in range(a_idx + 1, len(succ)):
                a, b = succ[a_idx], succ[b_idx]
                if dsets[a].isdisjoint(dsets[b]):
                    return False, (c, a, b)
    return True, None


# ---------------------------------------------------------------------------
# causal graph along one evolution, acyclicity, type-quotient
# ---------------------------------------------------------------------------

def evolve_chain(rules, seed, steps):
    """
    Deterministic single-site linearisation (pick first successor each step).
    Returns the event log [(event_id, event)...].
    """
    state = seed
    log = []
    eid = 0
    for _ in range(steps):
        succ = successors(state, rules)
        if not succ:
            break
        ns, ev, _k = succ[0]
        log.append((eid, ev))
        eid += 1
        state = ns
    return log


def causal_edges(log):
    """E1 -> E2 iff produced(E1) ∩ consumed(E2) != {}  (Gorard's definition)."""
    edges = set()
    for i, (e1, ev1) in enumerate(log):
        for j, (e2, ev2) in enumerate(log):
            if e1 == e2:
                continue
            if ev1["produced"] & ev2["consumed"]:
                edges.add((e1, e2))
    return edges


def is_acyclic(nodes, edges):
    """Kahn topological sort; True iff no cycle (no backward causality)."""
    indeg = {n: 0 for n in nodes}
    for a, b in edges:
        indeg[b] += 1
    queue = [n for n in nodes if indeg[n] == 0]
    seen = 0
    while queue:
        n = queue.pop()
        seen += 1
        for a, b in edges:
            if a == n:
                indeg[b] -= 1
                if indeg[b] == 0:
                    queue.append(b)
    return seen == len(nodes)


def type_quotient(log):
    """Collapse the causal stream by shard TYPE; return the set of type-edges."""
    tedges = set()
    for _eid, ev in log:
        if ev["c_type"] and ev["p_type"]:
            tedges.add((ev["c_type"], ev["p_type"]))
    return tedges


def is_oriented_3cycle(tedges, types=("S", "I", "O")):
    want = {("S", "I"), ("I", "O"), ("O", "S")}
    return tedges == want


# ---------------------------------------------------------------------------
# systems under test
# ---------------------------------------------------------------------------

def seed_token(sym):
    return ((sym, fresh()),)


# REAL issuance: a single active token flips type S->I->O->S, minting a FRESH
# token each flip (the seam O->S is fresh => null-stratum: no causal edge back).
REAL_RULES = [
    (("S",), ("I",), None),
    (("I",), ("O",), None),
    (("O",), ("S",), None),   # seam: fresh id -> no backward edge
]

# CONTROL-A: overlapping critical pair that never rejoins -> non-confluent.
# From "SS":  SS->X  (merge)   vs   S->Y  (flip).  X, Y are terminal.
CONTROL_A_RULES = [
    (("S", "S"), ("X",), None),
    (("S",), ("Y",), None),
]


def build_control_b_log(steps=6):
    """
    CONTROL-B: identical issuance, but the seam O->S WELDS the produced token
    onto the SEED id (same-token loop closure) -> produced(seam) ∩ consumed(E0)
    != {} -> a real causal cycle.
    """
    seed_id = fresh()
    state = (("S", seed_id),)
    log = []
    eid = 0
    for _ in range(steps):
        sym = state[0][0]
        if sym == "S":
            ns, ev = apply_at(state, 0, (("S",), ("I",), None))
        elif sym == "I":
            ns, ev = apply_at(state, 0, (("I",), ("O",), None))
        else:  # O -> S, welded back onto the ORIGINAL seed id
            ns, ev = apply_at(state, 0, (("O",), ("S",), ("weld", seed_id)))
        log.append((eid, ev))
        eid += 1
        state = ns
    return log


# ---------------------------------------------------------------------------
# run
# ---------------------------------------------------------------------------

def main():
    print("=" * 74)
    print("PRONG 2 DYNAMICS PROBE -- causal-invariant rewriting vs the shard cycle")
    print("=" * 74)

    results = {}

    # ---- REAL -------------------------------------------------------------
    print("\n[REAL] confluent issuance; fresh-token seam (null stratum)")
    real_conf, real_wit = is_confluent(REAL_RULES, seed_token("S"))
    # two-independent-sites diamond to show confluence is NON-trivial
    two_site_seed = (("S", fresh()), ("|", fresh()), ("S", fresh()))
    REAL_TWO = REAL_RULES + [(("|",), ("|",), None)]  # separator inert-ish
    two_conf, _ = is_confluent(REAL_RULES, two_site_seed, horizon=8, max_len=4)
    real_log = evolve_chain(REAL_RULES, seed_token("S"), steps=9)
    real_nodes = [e for e, _ in real_log]
    real_edges = causal_edges(real_log)
    real_acyc = is_acyclic(real_nodes, real_edges)
    real_tq = type_quotient(real_log)
    real_cycle = is_oriented_3cycle(real_tq)
    print(f"    confluent (single site)      : {real_conf}")
    print(f"    confluent (two indep sites)  : {two_conf}  (non-trivial diamond)")
    print(f"    causal graph acyclic (DAG)   : {real_acyc}   edges={sorted(real_edges)}")
    print(f"    TYPE-quotient                : {sorted(real_tq)}")
    print(f"    type-quotient is 3-cycle     : {real_cycle}")
    print(f"    --> coherent := conf AND acyc: {real_conf and real_acyc}")
    print("    NOTE: the 3-cycle appears ONLY in the type-quotient; the causal")
    print("          graph itself is a DAG. Causal invariance gives the DAG.")
    results["REAL_confluent"] = real_conf and two_conf
    results["REAL_acyclic"] = real_acyc
    results["REAL_3cycle_quotient"] = real_cycle

    # ---- CONTROL-A --------------------------------------------------------
    print("\n[CONTROL-A] overlapping critical pair -- must be NON-confluent")
    a_conf, a_wit = is_confluent(CONTROL_A_RULES, seed_token("S") + seed_token("S"),
                                 horizon=8, max_len=4)
    print(f"    confluent : {a_conf}   divergence-witness={a_wit}")
    print(f"    --> causal-invariance test CATCHES branch divergence: {not a_conf}")
    results["CONTROL_A_caught"] = (a_conf is False)

    # ---- CONTROL-B --------------------------------------------------------
    print("\n[CONTROL-B] welded seam (same-token loop) -- must have CYCLIC causal graph")
    b_log = build_control_b_log(steps=6)
    b_nodes = [e for e, _ in b_log]
    b_edges = causal_edges(b_log)
    b_acyc = is_acyclic(b_nodes, b_edges)
    print(f"    causal edges : {sorted(b_edges)}")
    print(f"    causal graph acyclic : {b_acyc}")
    print(f"    --> acyclicity test CATCHES backward-causality paradox: {not b_acyc}")
    results["CONTROL_B_caught"] = (b_acyc is False)

    # ---- criterion non-vacuity -------------------------------------------
    print("\n" + "-" * 74)
    print("CRITERION NON-VACUITY (each control must violate exactly one conjunct)")
    print(f"  REAL:      confluent={results['REAL_confluent']}  acyclic={results['REAL_acyclic']}")
    print(f"  CONTROL-A: confluent=False (violates conjunct 1: causal invariance)")
    print(f"  CONTROL-B: acyclic=False   (violates conjunct 2: no backward causality)")

    expected = {
        "REAL_confluent": True,
        "REAL_acyclic": True,
        "REAL_3cycle_quotient": True,
        "CONTROL_A_caught": True,
        "CONTROL_B_caught": True,
    }
    ok = all(results.get(k) == v for k, v in expected.items())

    print("\n" + "=" * 74)
    for k, v in expected.items():
        got = results.get(k)
        print(f"  {'PASS' if got == v else 'FAIL'}  {k}: expected {v}, got {got}")
    print("=" * 74)
    print(f"CLASSIFIER BEHAVED AS DESIGNED (controls fail as planted): {ok}")
    print("READOUT: a causal-invariant acyclic rule DOES close the oriented cycle")
    print("  without paradox -- BUT the circle is the TYPE-QUOTIENT, not the causal")
    print("  graph, and confluence produces the DAG. See artifact for exact vs analogy.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
