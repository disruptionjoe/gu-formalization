#!/usr/bin/env python3
"""Hostile mutations for K1701."""
import copy, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]


def valid(d):
    i, c, q = d.get("inputs", {}), d.get("coefficient", {}), d.get("decision", {})
    return all([d.get("claim_id") == "K1701", "bounded symmetric" in i.get("seed_class", ""),
        "q=u t^2" in i.get("matched_coordinate", ""), "q^2/6" in c.get("matched_law", ""),
        "1/4+kappa_6(X)^2/(120u^3)" in c.get("formula", ""), c.get("sharp_floor") == "c_X>=1/4.",
        "if and only if kappa_6(X)=0" in c.get("equality", ""), q.get("universal_fixed_seed_cubic_floor") is True,
        q.get("finite_strength_optimizer_identified") is False, "not yet uniform" in d.get("scope_guard", "")])


def main():
    src = json.loads((ROOT / "lab/process/k1701-universal-weak-channel-cubic-floor.json").read_text())
    muts = [(('claim_id',), 'K1700'), (('inputs','seed_class'), 'Gaussian'), (('inputs','matched_coordinate'), 'wrong'),
        (('coefficient','matched_law'), 'linear'), (('coefficient','formula'), '1/5'), (('coefficient','sharp_floor'), 'none'),
        (('coefficient','equality'), 'always'), (('decision','universal_fixed_seed_cubic_floor'), False),
        (('decision','finite_strength_optimizer_identified'), True), (('scope_guard',), 'global theorem')]
    assert valid(src)
    for n, (path, value) in enumerate(muts, 1):
        d = copy.deepcopy(src); cur = d
        for key in path[:-1]: cur = cur[key]
        cur[path[-1]] = value
        assert not valid(d), n
        print(f"REJECT {n:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(muts)}/{len(muts)}")


if __name__ == "__main__": main()
