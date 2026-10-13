#!/usr/bin/env python3
"""Hostile semantic mutations for K1726."""
import copy, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1726-regular-path-quartic-floor.json").read_text())


def valid(x):
    q, z = x.get("regular_path", {}), x.get("decision", {})
    return all([x.get("claim_id") == "K1726", "uniformly bounded" in q.get("scope", ""),
                "u_0>0" in q.get("scope", ""), "11/108" in q.get("completed_squares", ""),
                "(a-35/3)^2/120" in q.get("completed_squares", ""),
                "(x-35)^2/5040" in q.get("completed_squares", ""),
                q.get("equality_conditions") == "a=35/3 and x=35.",
                "O(q^(9/2))" in q.get("uniformity", ""),
                z.get("two_square_defect_exact"), z.get("fixed_seed_cubic_floor_preserved"),
                not z.get("all_seed_nonperturbative_optimizer_identified"),
                "growing support" in x.get("scope_guard", "")])


def setp(x, path, value):
    y = copy.deepcopy(x); cur = y
    for key in path[:-1]: cur = cur[key]
    cur[path[-1]] = value; return y


def main():
    assert valid(D); print("PASS 01: baseline")
    muts = [(('claim_id',), 'K1725'), (('regular_path','scope'), 'all seeds'),
            (('regular_path','completed_squares'), 'D=0'), (('regular_path','equality_conditions'), 'any'),
            (('decision','two_square_defect_exact'), False), (('decision','fixed_seed_cubic_floor_preserved'), False),
            (('decision','all_seed_nonperturbative_optimizer_identified'), True),
            (('scope_guard',), 'finite strength solved'), (('regular_path','uniformity'), 'pointwise only')]
    for n, (path, value) in enumerate(muts, 2):
        assert not valid(setp(D, path, value)); print(f"PASS {n:02d}: reject {'/'.join(path)}")
    print(f"RESULT: PASS {len(muts)+1}/{len(muts)+1}")


if __name__ == '__main__': main()
