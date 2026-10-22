"""Independent rational controls for the finite-energy thermal-gap argument.

No producer imports. Finite checks support the analytic all-spectrum proof;
they do not certify Jensen's inequality or the universal quantifiers by sampling.
"""
from copy import deepcopy
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "lab/process/k1956-finite-energy-thermal-gap.json"
INPUTS = (
    "lab/process/k1934-nonuniform-four-level-catalyst-optimization.json",
    "lab/process/k1935-arbitrary-support-thermal-return.json",
    "lab/process/k1943-arbitrary-preparation-catalyst-energy.json",
)


def bath_coefficients():
    """Derive each overlapping-label sum from the actual four probabilities."""
    bath = [F(8, 15), F(4, 15), F(2, 15), F(1, 15)]
    assert sum(bath) == 1
    low = {d: sum(bath[:4-d]) for d in (1, 2, 3)}
    high = {d: sum(bath[d:]) for d in (1, 2, 3)}
    return low, high


def constants(q_override=None):
    low, high = bath_coefficients()
    q = low[2] / (1 + high[2])
    p = high[2] / (1 + low[2])
    if q_override is not None:
        q = q_override
    assert q * (1 + high[2]) == low[2], "left-arm bath recurrence"
    assert p * (1 + low[2]) == high[2], "right-arm bath recurrence"
    A, B = q / (1-q), p / (1-p)
    q3 = low[3] / (1 + high[3])
    p1 = high[1] / (1 + low[1])
    p3 = high[3] / (1 + low[3])
    F3 = q3 * (1+A)
    G1 = p1 * (1+p3) / (1-p1*p3)
    W = 1+A+B
    c = A+B-F3-G1
    assert all(low[d] / (1+high[d]) <= q for d in low)
    assert c > 0 and c <= 2
    return dict(q=q, p=p, W=W, c=c, C=c/(2*W*W),
                lower_exponent=W/2, upper_C=(A+B)/(2*W),
                upper_energy_offset=1+2*p/(1-p)**2)


def rewards(gaps, orientation):
    """Solve D^T w=1 along its directed acyclic graph, with no matrix inverse."""
    low, high = bath_coefficients()
    n = len(gaps)+1
    diagonal = [F(1)]*n
    outgoing = [[] for _ in range(n)]
    for i, (gap, winner) in enumerate(zip(gaps, orientation)):
        if winner == 0:
            diagonal[i+1] += low[gap]
            outgoing[i].append((i+1, high[gap]))
        else:
            diagonal[i] += high[gap]
            outgoing[i+1].append((i, low[gap]))

    @lru_cache(None)
    def value(i):
        return (1+sum(a*value(j) for j, a in outgoing[i])) / diagonal[i]

    return [value(i) for i in range(n)]


def column_controls(max_sites=6, c_override=None, exponent_denominator=2):
    v = constants()
    c = v["c"] if c_override is None else c_override
    controls = 0
    for n in range(1, max_sites+1):
        for gaps in product((1, 2, 3), repeat=n-1):
            if any(a+b < 4 for a, b in zip(gaps, gaps[1:])):
                continue
            energy = [max(1, 3-gaps[0]) if gaps else 1]
            for d in gaps:
                energy.append(energy[-1]+d)
            for direction in product((0, 1), repeat=n-1):
                for e, w in zip(energy, rewards(gaps, direction)):
                    gap = v["W"]-w
                    # Positive powers avoid numerical square roots.
                    assert gap > 0 and gap**exponent_denominator >= (
                        c**exponent_denominator * v["q"]**e
                    ), "finite-energy column reward gap"
                    controls += 1
    return controls


def long_root_control(exponent_denominator=2):
    """A long exact witness distinguishes a falsely strengthened exponent."""
    n = 16
    v = constants()
    w = rewards([2]*(2*n), [1]*n+[0]*n)[n]
    gap = v["W"]-w
    e = 1+2*n
    assert gap**exponent_denominator >= (
        v["c"]**exponent_denominator * v["q"]**e
    ), "long-root exponent bound"
    return 1


def population_rate(gaps, population, flip_first=False):
    low, high = bath_coefficients()
    incoming = [F(0)]*len(population)
    direction = []
    for i, gap in enumerate(gaps):
        x, y = high[gap]*population[i], low[gap]*population[i+1]
        winner = int(y > x)
        if i == 0 and flip_first:
            winner = 1-winner
        direction.append(winner)
        if winner == 0:
            incoming[i+1] += x-y
        else:
            incoming[i] += y-x
    deficit = [p-i for p, i in zip(population, incoming)]
    positive = [max(F(0), z) for z in deficit]
    assert all(0 <= u <= p for u, p in zip(positive, population)), (
        "positive deficit is bounded by the actual preparation"
    )
    w = rewards(gaps, direction)
    assert sum(a*b for a, b in zip(w, deficit)) == sum(population), (
        "independent reward/deficit identity"
    )
    assert sum(a*b for a, b in zip(w, positive)) >= sum(population)
    return sum(positive)/2


def preparation_controls():
    count = 0
    for gaps in ((2,), (1, 3), (3, 1), (2, 2, 2), (3, 2, 1, 3)):
        for power in (0, 1, 2, 3):
            raw = [F((i+1)**power) for i in range(len(gaps)+1)]
            population = [x/sum(raw) for x in raw]
            population_rate(gaps, population)
            count += 3
    population_rate([2], [F(1, 2), F(1, 2)])
    return count+3


def upper_controls(corrupt_preparation=False):
    v = constants()
    q, p, W = v["q"], v["p"], v["W"]
    count = 0
    for n in range(16):
        raw = [q**k for k in range(n, 0, -1)]+[F(1)]+[
            p**k for k in range(1, n+1)
        ]
        Z = sum(raw)
        assert Z == W-2*q**n-F(1, 8)*p**n, "finite geometric normalization"
        if corrupt_preparation and n == 1:
            raw[0] *= 2
        population = [x/sum(raw) for x in raw]
        energy = sum((1+2*i)*x for i, x in enumerate(population))
        rate = population_rate([2]*(2*n), population)
        assert rate == 1/(2*Z), "actual preparation achieves the rooted return"
        assert energy <= 2*n+v["upper_energy_offset"], "mean-energy bound"
        assert rate-F(4, 25) <= v["upper_C"]*q**n, "exponential upper gap"
        count += 4
    return count


def reporting_checks(report):
    assert report["result_id"] == "K1956", "report identity"
    expected = constants()
    assert {k: F(report["constants"][k]) for k in expected} == expected, (
        "report constants match independently derived bath sums"
    )
    for relative in INPUTS:
        assert report["inputs"][relative] == hashlib.sha256(
            (ROOT/relative).read_bytes()
        ).hexdigest(), "prior evidence pin"
    return 2+len(INPUTS)


def expect_failure(label, operation):
    try:
        operation()
    except AssertionError as exc:
        return [label, str(exc)]
    raise AssertionError("undetected mathematical/reporting fault: "+label)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--math-only", action="store_true")
    args = parser.parse_args()
    counts = dict(column_rewards=column_controls(), long_root=long_root_control(),
                  preparations=preparation_controls(), upper_family=upper_controls())
    print("PASS K1956 independent finite supporting controls", counts, flush=True)
    faults = [
        expect_failure("bath_recurrence", lambda: constants(F(3, 4))),
        expect_failure("overstrong_gap_constant", lambda: column_controls(1, F(3))),
        expect_failure("overstrong_energy_exponent", lambda: long_root_control(4)),
        expect_failure("wrong_population_orientation", lambda: population_rate(
            [2], [F(1, 2), F(1, 2)], flip_first=True)),
        expect_failure("changed_upper_preparation", lambda: upper_controls(True)),
    ]
    print("PASS K1956 load-bearing mathematical faults", faults, flush=True)
    if not args.math_only:
        report = json.loads(REPORT.read_text())
        print("PASS K1956 separate reporting controls", reporting_checks(report), flush=True)
        for field in ("identity", "pin"):
            bad = deepcopy(report)
            if field == "identity":
                bad["result_id"] = "WRONG"
            else:
                bad["inputs"][INPUTS[0]] = "0"*64
            print("PASS K1956 reporting fault", expect_failure(
                field, lambda: reporting_checks(bad)), flush=True)
    print("Universal scope rests on the analytic proof, not these finite totals.", flush=True)
