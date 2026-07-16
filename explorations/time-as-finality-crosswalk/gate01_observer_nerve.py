"""
Gate 0/1 for the live/dark observer-sheaf hypothesis
(see live-dark-observer-sheaf-existence-as-issuance-2026-07-15.md and the
ten-persona steelman note for the four-gate pipeline).

Question (assumption-light, NO dynamics, NO source action):
  Does a *generically issued* observer/record nerve have a non-trivial first
  Betti number b1 that is (a) FORCED (generic across seeds AND issuance models,
  not a hand-picked config), (b) EXTENSIVE (grows with system size, structural
  not marginal), and (c) DELETION-STABLE (survives removing a fraction of stalks)?

  b1 = E - V + C  (first Betti number of the 1-skeleton; independent loops)

  If b1 is generically 0 (forests/trees), there are no loops to carry a flat-Z/2
  holonomy -> the sign has no non-vacuous home on the nerve -> same death as S^3.

  Scope: tests the H1 / pi_1-holonomy reading (rho: pi_1 -> U(16)) ONLY. The H3
  2-gerbe reading (E054) needs the full Cech nerve with triple+ overlaps and is
  NOT tested here. This gate is necessary, not sufficient; the discriminator is
  Gate 2 (unique-sign vs domains under churn), which requires positing dynamics.

  Controls: ring -> b1=1 (a loop exists); tree -> b1=0 (discriminating negative).

No external deps (pure Python).
"""

import random
import math


def betti1(n_nodes, edges):
    parent = list(range(n_nodes))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    E = 0
    seen = set()
    for (u, v) in edges:
        seen.add(u); seen.add(v)
        E += 1
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
    V = len(seen)
    C = len(set(find(x) for x in seen))
    return E - V + C


def model_ER(N, avg_deg, rng):
    p = avg_deg / (N - 1)
    edges = []
    for u in range(N):
        for v in range(u + 1, N):
            if rng.random() < p:
                edges.append((u, v))
    return N, edges


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
            edges.append((new, t))
            repeated += [t, new]
    return N, edges


def model_RGG(N, radius, rng):
    pts = [(rng.random(), rng.random()) for _ in range(N)]
    edges = []
    r2 = radius * radius
    for u in range(N):
        xu, yu = pts[u]
        for v in range(u + 1, N):
            xv, yv = pts[v]
            if (xu - xv) ** 2 + (yu - yv) ** 2 < r2:
                edges.append((u, v))
    return N, edges


def delete_fraction(N, edges, frac, rng):
    dead = set(rng.sample(range(N), int(frac * N)))
    kept = [(u, v) for (u, v) in edges if u not in dead and v not in dead]
    return N, kept


def run_model(name, builder, sizes, seeds, params):
    print(f"\n=== {name} ===")
    print(f"{'N':>5} {'b1_mean':>9} {'b1/N':>7} {'frac>0':>7} {'b1_del20%':>10} {'del_frac>0':>10}")
    rows = []
    for N in sizes:
        b1s, b1s_del = [], []
        for s in seeds:
            rng = random.Random(1000 * N + s)
            n, edges = builder(N, params(N), rng)
            b1s.append(betti1(n, edges))
            n2, e2 = delete_fraction(n, edges, 0.20, rng)
            b1s_del.append(betti1(n2, e2))
        b1_mean = sum(b1s) / len(b1s)
        frac_pos = sum(1 for x in b1s if x > 0) / len(b1s)
        del_mean = sum(b1s_del) / len(b1s_del)
        del_frac = sum(1 for x in b1s_del if x > 0) / len(b1s_del)
        print(f"{N:>5} {b1_mean:>9.1f} {b1_mean/N:>7.3f} {frac_pos:>7.2f} {del_mean:>10.1f} {del_frac:>10.2f}")
        rows.append((N, b1_mean, b1_mean / N, frac_pos, del_mean, del_frac))
    ratios = [r[2] for r in rows]
    extensive = ratios[-1] > 0.5 * ratios[0] and ratios[-1] > 0.01
    generic = all(r[3] >= 0.95 for r in rows)
    del_stable = all(r[5] >= 0.95 for r in rows)
    forced = generic and extensive and del_stable
    print(f"  -> generic:{generic} extensive:{extensive} deletion-stable:{del_stable}")
    print(f"  -> GATE 0/1 {name}: {'PASS' if forced else 'FAIL'}")
    return forced


def main():
    sizes = [50, 100, 200, 400]
    seeds = list(range(20))

    print("=== CONTROLS ===")
    for N in [50, 400]:
        edges = [(i, (i + 1) % N) for i in range(N)]
        print(f" ring N={N}: b1={betti1(N, edges)} (expect 1)")
    for N in [50, 400]:
        rng = random.Random(N)
        edges = [(i, rng.randrange(i)) for i in range(1, N)]
        print(f" tree N={N}: b1={betti1(N, edges)} (expect 0)")

    results = {}
    results['ER (avg_deg=4)'] = run_model('ER (avg_deg=4)', model_ER, sizes, seeds, lambda N: 4)
    results['BA (m=2)'] = run_model('BA (m=2)', model_BA, sizes, seeds, lambda N: 2)
    results['RGG (avg_deg~6)'] = run_model('RGG (avg_deg~6)', model_RGG, sizes, seeds,
                                           lambda N: math.sqrt(6.0 / (math.pi * N)))

    print("\n=== GATE 0/1 SUMMARY ===")
    for k, v in results.items():
        print(f"  {k:>18}: {'PASS' if v else 'FAIL'}")
    any_pass = any(results.values())
    print(f"\nGATE 0/1 VERDICT: {'PROCEED to Gate 2' if any_pass else 'DEAD (no forced loops)'}")


if __name__ == '__main__':
    main()
