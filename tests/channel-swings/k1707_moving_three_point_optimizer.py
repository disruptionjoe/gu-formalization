#!/usr/bin/env python3
"""Exact algebra and quadrature controls for K1707."""
import json, math
from fractions import Fraction
from pathlib import Path
import numpy as np
from numpy.polynomial.hermite_e import hermegauss
ROOT = Path(__file__).resolve().parents[2]


def fisher(p, t, order=180):
    nodes, weights = hermegauss(order); weights /= math.sqrt(2 * math.pi)
    points = np.array([-1 / math.sqrt(p), 0.0, 1 / math.sqrt(p)])
    priors = np.array([p / 2, 1 - p, p / 2]); rt, v = math.sqrt(t), 1 - t; out = 0.0
    for point, prior in zip(points, priors):
        y = rt * point + math.sqrt(v) * nodes
        logs = np.log(priors)[None, :] - (y[:, None] - rt * points[None, :]) ** 2 / (2 * v)
        logs -= logs.max(axis=1)[:, None]; post = np.exp(logs); post /= post.sum(axis=1)[:, None]
        mean = post @ points; score = rt / v * (mean - rt * y)
        out += prior * np.dot(weights, score * score)
    return out


def main():
    d = json.loads((ROOT / 'lab/process/k1707-moving-three-point-optimizer.json').read_text())
    q, z = d['three_point_branch'], d['decision']; root = math.sqrt(105)
    pstar = (15 + root) / 60; u = (root - 9) / 2
    kp = -2 / pstar**3 + 15 / pstar**2
    beta = (35 / 3) * u**1.5 / kp
    d_fixed = Fraction(227, 126) + Fraction(5, 168) * root
    d_opt = Fraction(1009, 1512) + Fraction(5, 168) * root
    checks = [('schema', d['schema_version'] == '1.0'), ('claim', d['claim_id'] == 'K1707'),
              ('pstar', math.isclose(pstar, 0.4207825127659933)), ('u positive', u > 0),
              ('kappa6 prime positive', kp > 0), ('beta positive', beta > 0),
              ('beta value', math.isclose(beta, 0.09924222021028861, rel_tol=2e-13)),
              ('fixed coefficient', math.isclose(float(d_fixed), 2.106556074383718, rel_tol=2e-13)),
              ('gain exact', math.isclose(d_fixed - d_opt, 245 / 216, rel_tol=2e-15)),
              ('optimized coefficient', math.isclose(float(d_opt), 0.9722968151244589, rel_tol=2e-13))]
    for defect in (0.001, 0.003, 0.01):
        moving_p = pstar + beta * math.sqrt(defect)
        j_fixed = fisher(pstar, math.sqrt(defect / (3 - 1 / pstar)))
        j_moving = fisher(moving_p, math.sqrt(defect / (3 - 1 / moving_p)))
        checks += [(f'moving admissible {defect}', pstar < moving_p < 1),
                   (f'moving gain {defect}', j_moving < j_fixed)]
    checks += [('family', '1/3<p<=1' in q['family']), ('sqrt motion', 'beta sqrt(q)' in q['motion']),
               ('quartic gain text', z['quartic_gain_exact'] == '245/216'),
               ('cubic preserved', z['k1702_cubic_equality_preserved']),
               ('fixed false', z['fixed_p_star_finite_strength_optimality_false']),
               ('all seed open', not z['all_seed_optimizer_identified']),
               ('scope', 'symmetric three-point family' in d['scope_guard'])]
    for n, (label, ok) in enumerate(checks, 1): assert ok, label; print(f'PASS {n:02d}: {label}')
    print(f'RESULT: PASS {len(checks)}/{len(checks)}')


if __name__ == '__main__': main()
