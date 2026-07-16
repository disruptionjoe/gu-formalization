"""
Gate 2a (EXACT F2 cohomology / XOR-SAT) for the observer-sheaf sign.

The sign is an Ising/Z2 variable s(v) at each observer. A local rule fixes, per
edge (u,v), a coupling J(uv) in {0,1}: whether the two observers' signs should
agree (0) or disagree (1). A globally consistent universal sign exists iff the
F2 linear system

    s(u) + s(v) = J(uv)  (mod 2)   for all edges

is SATISFIABLE, i.e. iff [J] = 0 in H^1(N; Z2) (no frustrated cycle). Then the
solution is unique up to one global flip per connected component (the universal
sign, fixed by the boundary/positivity posit). If UNSAT -> frustration -> the
ground state fragments into DOMAINS (observer-dependent sign) -> falsified.

We SWEEP a family of local rules (we do NOT invent the specific source action):
  (P)  vertex-potential  : J(uv) = g(u) XOR g(v), g a per-OBSERVER bit
                           -> coboundary by construction (Joe's "each observer
                              sources its own sign via issuance"). Predict SAT.
  (R)  random-edge(p)    : J(uv) ~ Bernoulli(p), a purely RELATIONAL/edge sign.
                           Predict frustration -> UNSAT above threshold.
  (PN) potential+noise(p): J = g(u) XOR g(v) XOR noise_p(uv). Find the noise
                           tolerance before domains appear.

Exact, deterministic given the rule draw; F2 elimination via spanning-forest.
Reuses the Gate 0/1 nerves. No external deps.
"""

import random
import math


def key(u, v):
    return (u, v) if u < v else (v, u)


def betti1(N, edges):
    parent = list(range(N))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    seen = set()
    E = 0
    for (u, v) in edges:
        seen.add(u); seen.add(v); E += 1
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
    V = len(seen)
    C = len(set(find(x) for x in seen))
    return E - V + C


def sat_and_frustration(N, edges, J):
    """Assign s by BFS over a spanning forest; count non-tree edges violated.
    Returns (is_sat, n_frustrated_fundamental_cycles, b1)."""
    adj = {}
    for (u, v) in edges:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)
    s = {}
    tree_used = set()
    b1 = betti1(N, edges)
    frustrated = 0
    non_tree_checked = set()
    # BFS assigning s
    for start in adj:
        if start in s:
            continue
        s[start] = 0
        stack = [start]
        while stack:
            u = stack.pop()
            for w in adj[u]:
                e = key(u, w)
                if w not in s:
                    s[w] = s[u] ^ J[e]
                    tree_used.add(e)
                    stack.append(w)
    # check every edge; non-tree edges are the fundamental cycles
    for (u, v) in edges:
        e = key(u, v)
        if e in tree_used:
            continue
        if e in non_tree_checked:
            continue
        non_tree_checked.add(e)
        if (s[u] ^ s[v]) != J[e]:
            frustrated += 1
    return (frustrated == 0), frustrated, b1


# ---------- nerve builders (Gate 0/1) ----------
def model_ER(N, avg_deg, rng):
    p = avg_deg / (N - 1)
    return N, [(u, v) for u in range(N) for v in range(u + 1, N) if rng.random() < p]


def model_BA(N, m, rng):
    if N <= m:
        return N, [(i, i + 1) for i in range(N - 1)]
    targets = list(range(m))
    edges = [(m, t) for t in targets]
    repeated = []
    for t in targets:
        repeated += [t, m]
    for new in range(m + 1, N):
        chosen = set()
        while len(chosen) < m:
            chosen.add(rng.choice(repeated) if repeated else rng.randrange(new))
        for t in chosen:
            edges.append((new, t)); repeated += [t, new]
    return N, edges


def model_RGG(N, radius, rng):
    pts = [(rng.random(), rng.random()) for _ in range(N)]
    r2 = radius * radius
    edges = []
    for u in range(N):
        xu, yu = pts[u]
        for v in range(u + 1, N):
            xv, yv = pts[v]
            if (xu - xv) ** 2 + (yu - yv) ** 2 < r2:
                edges.append((u, v))
    return N, edges


# ---------- rule families ----------
def rule_potential(N, edges, rng):
    g = [rng.getrandbits(1) for _ in range(N)]
    return {key(u, v): g[u] ^ g[v] for (u, v) in edges}


def rule_random(N, edges, p, rng):
    return {key(u, v): (1 if rng.random() < p else 0) for (u, v) in edges}


def rule_potential_noise(N, edges, p, rng):
    g = [rng.getrandbits(1) for _ in range(N)]
    J = {}
    for (u, v) in edges:
        base = g[u] ^ g[v]
        if rng.random() < p:
            base ^= 1
        J[key(u, v)] = base
    return J


def churn_delete(N, edges, J, frac, rng):
    dead = set(rng.sample(range(N), int(frac * N)))
    e2 = [(u, v) for (u, v) in edges if u not in dead and v not in dead]
    J2 = {key(u, v): J[key(u, v)] for (u, v) in e2}
    return N, e2, J2


def main():
    print("=== CONTROLS ===")
    # all-agree triangle -> SAT; frustrated triangle -> UNSAT
    tri = [(0, 1), (1, 2), (2, 0)]
    Jsat = {key(u, v): 0 for (u, v) in tri}
    Jfrust = {key(0, 1): 0, key(1, 2): 0, key(2, 0): 1}
    print(" triangle all-agree :", sat_and_frustration(3, tri, Jsat), "(expect SAT, 0 frustrated)")
    print(" triangle frustrated:", sat_and_frustration(3, tri, Jfrust), "(expect UNSAT, 1 frustrated)")

    sizes = [100, 400]
    seeds = list(range(20))
    models = [
        ('ER(deg4)', model_ER, lambda N: 4),
        ('BA(m2)', model_BA, lambda N: 2),
        ('RGG(deg6)', model_RGG, lambda N: math.sqrt(6.0 / (math.pi * N))),
    ]

    for mname, builder, params in models:
        print(f"\n=== {mname} ===")
        for N in sizes:
            # (P) vertex potential -- Joe's per-observer sourcing
            sat_P = 0
            for s in seeds:
                rng = random.Random(7 * N + s)
                n, edges = builder(N, params(N), rng)
                J = rule_potential(n, edges, rng)
                sat, fr, b1 = sat_and_frustration(n, edges, J)
                sat_P += sat
            # (P) churn-stability: delete 20% then re-check SAT
            sat_P_churn = 0
            for s in seeds:
                rng = random.Random(7 * N + s)
                n, edges = builder(N, params(N), rng)
                J = rule_potential(n, edges, rng)
                n2, e2, J2 = churn_delete(n, edges, J, 0.20, rng)
                sat, fr, b1 = sat_and_frustration(n2, e2, J2)
                sat_P_churn += sat
            print(f" N={N:>4} (P) vertex-potential : SAT {sat_P}/{len(seeds)} | after 20% churn SAT {sat_P_churn}/{len(seeds)}")

            # (R) random-edge across p
            for p in [0.02, 0.05, 0.1, 0.25, 0.5]:
                sat_R = 0
                frac_frust = 0.0
                for s in seeds:
                    rng = random.Random(7 * N + s)
                    n, edges = builder(N, params(N), rng)
                    J = rule_random(n, edges, p, rng)
                    sat, fr, b1 = sat_and_frustration(n, edges, J)
                    sat_R += sat
                    frac_frust += (fr / b1 if b1 else 0.0)
                print(f"        (R) random p={p:<4}: SAT {sat_R:>2}/{len(seeds)} | mean frustrated-cycle frac {frac_frust/len(seeds):.3f}")

            # (PN) potential + noise across p
            for p in [0.001, 0.005, 0.02, 0.05]:
                sat_PN = 0
                frac_frust = 0.0
                for s in seeds:
                    rng = random.Random(7 * N + s)
                    n, edges = builder(N, params(N), rng)
                    J = rule_potential_noise(n, edges, p, rng)
                    sat, fr, b1 = sat_and_frustration(n, edges, J)
                    sat_PN += sat
                    frac_frust += (fr / b1 if b1 else 0.0)
                print(f"        (PN) pot+noise p={p:<5}: SAT {sat_PN:>2}/{len(seeds)} | mean frustrated-cycle frac {frac_frust/len(seeds):.4f}")

    print("\n=== GATE 2a READING ===")
    print(" (P) per-observer/vertex-sourced sign  -> expect SAT always + churn-stable  = unique universal sign")
    print(" (R) purely relational/edge sign       -> expect UNSAT (frustration ~1/2)   = domains")
    print(" (PN) per-observer + relational noise   -> SAT collapses with tiny p, but frustration DENSITY grows")
    print("      gracefully -> the dichotomy is vertex-sourced (universal) vs edge-sourced (domained).")


if __name__ == '__main__':
    main()
