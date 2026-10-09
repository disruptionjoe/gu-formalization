#!/usr/bin/env python3
"""Check the coefficients of Lean's five necessary equations against I1B.

This is the explicitly external action-to-polynomial bridge. Lean checks
incompatibility over all real amplitudes, not this geometric derivation.
"""
from itertools import combinations
import json
from pathlib import Path
import re

import sympy as sp

from native_i1b_scalar_closure_probe import CORE, cubic_gradient, direction, dual_rows, exact
from native_zorro_geometry_probe import geometry, rational_frame
from native_zorro_i1b_probe import (clifford_form, covariant_gradient,
                                   first_order_euler, invariant_projectors,
                                   spin_curvature)

ROOT = Path(__file__).resolve().parents[2]
LEAN = ROOT / 'Lean/GUFormalization/NguyenPositivityKernels.lean'


def certify():
    a, b, c, kappa = sp.symbols('a b c kappa', real=True)
    variables = [a,b,c]
    source = LEAN.read_text().split('def CanonicalThreeBlockNecessary',1)[1]
    source = source.split(': Prop :=',1)[1].split('/--',1)[0]
    rows = source.strip().split('∧')
    assert len(rows) == 5
    parsed = []
    for row in rows:
        row = row.strip()
        assert row.endswith('= 0'), row
        expression = row[:-3].strip()
        assert not re.sub(r'kappa|[abc0-9\s+*/^().-]', '', expression), expression
        parsed.append(sp.sympify(expression.replace('^','**'), locals=dict(a=a,b=b,c=c,kappa=kappa)))

    g, _, gamma, curvature, _ = geometry()
    frame = rational_frame(g)
    projectors = invariant_projectors()
    fields = [clifford_form(frame.inv()*p*frame) for p,_ in projectors]
    gradients = [covariant_gradient(p, dp, gamma, frame) for p,dp in projectors]
    linear = [first_order_euler(gradient) for gradient in gradients]
    forcing = dual_rows(CORE.shiab(spin_curvature(frame,curvature)[0]))

    derived = [sum(variables[j]*linear[j].get(row,0) for j in range(3))
               for row in [(0,17),(0,1025)]]
    for mu in [0,4,10]:
        receiver = direction(mu,1<<mu)
        diagonal = [cubic_gradient(t,receiver) for t in fields]
        cubic_row = sum(diagonal[j]*variables[j]**2 for j in range(3))
        for i,j in combinations(range(3),2):
            mixed = cubic_gradient(CORE.fadd(fields[i],fields[j]),receiver)-diagonal[i]-diagonal[j]
            cubic_row += mixed*variables[i]*variables[j]
        mass_row = sum(variables[j]*exact(CORE.pair(receiver,CORE.hodge(fields[j]))) for j in range(3))
        derived.append(cubic_row+kappa*mass_row+forcing[(mu,1<<mu)])

    for i,(actual,declared) in enumerate(zip(derived,parsed)):
        assert sp.expand(actual-declared) == 0, (i,actual,declared)
    return {'checks_passed':5,
            'checks':['direct action matches Lean necessary polynomial '+str(i+1) for i in range(5)],
            'polynomials':[str(sp.expand(p)) for p in derived],
            'coefficient_field':'exact rational coefficients; real variables',
            'scope':'Five necessary full-distortion rows only. No Lean formalization of the curvature/Clifford derivation, Witten construction or physical GU domain.'}


if __name__ == '__main__':
    print(json.dumps(certify(),indent=2))
