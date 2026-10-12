#!/usr/bin/env python3
"""Hostile semantic mutations for K1706."""
import copy, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1706-symmetric-eighth-order-fisher-law.json").read_text())


def valid(x):
    h, z = x.get("hermite_law", {}), x.get("decision", {})
    return all([x.get("claim_id") == "K1706", "bounded symmetric" in h.get("scope", ""),
                "h_8/40320" in h.get("density_ratio", ""),
                "-(7/36)kappa_4^2kappa_6 t^7" in h.get("fisher", ""),
                "h_8^2/5040" in h.get("fisher", ""), "71kappa_4^4/48" in h.get("fisher", ""),
                z.get("seventh_order_term_identified"), z.get("eighth_order_term_identified"),
                not z.get("all_seed_finite_strength_optimizer_identified"),
                "growing support" in x.get("scope_guard", "")])


def setp(x, path, value):
    y = copy.deepcopy(x); cur = y
    for key in path[:-1]: cur = cur[key]
    cur[path[-1]] = value; return y


def main():
    assert valid(D); print("PASS 01: baseline")
    muts = [(('claim_id',), 'K1705'), (('hermite_law','scope'), 'all seeds'),
            (('hermite_law','density_ratio'), 'changed'), (('hermite_law','fisher'), 'changed'),
            (('decision','seventh_order_term_identified'), False),
            (('decision','eighth_order_term_identified'), False),
            (('decision','all_seed_finite_strength_optimizer_identified'), True),
            (('scope_guard',), 'finite strength solved')]
    for n, (path, value) in enumerate(muts, 2):
        assert not valid(setp(D, path, value)); print(f"PASS {n:02d}: reject {'/'.join(path)}")
    print(f"RESULT: PASS {len(muts)+1}/{len(muts)+1}")


if __name__ == '__main__': main()
