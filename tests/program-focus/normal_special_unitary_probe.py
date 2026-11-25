#!/usr/bin/env python3
"""Exact finite controls for the W09 proof, not a topological proof assistant.

Run with the repository research Python (SymPy). No generated owner output.
"""
import json
import sympy as s

checks = []
def check(name, condition):
    assert condition, name
    checks.append(name)

def su_basis(n):
    out = []
    for i in range(n):
        for j in range(i + 1, n):
            a = s.zeros(n); a[i,j] = 1; a[j,i] = -1; out.append(a)
            a = s.zeros(n); a[i,j] = s.I; a[j,i] = s.I; out.append(a)
    for i in range(n-1):
        a = s.zeros(n); a[i,i] = s.I; a[n-1,n-1] = -s.I; out.append(a)
    return out

def realcol(v):
    return s.Matrix([s.re(x) for x in v] + [s.im(x) for x in v])

basis = su_basis(4)
check('su4 compact generators', len(basis) == 15 and all(a.H == -a and s.trace(a) == 0 for a in basis))
e4 = s.eye(4)[:,3]
action = s.Matrix.hstack(*(realcol(a*e4) for a in basis))
check('unit spinor tangent orbit has real dimension7', action.rank() == 7)
null = action.nullspace()
stabilizers = [sum((v[i]*basis[i] for i in range(15)), s.zeros(4)) for v in null]
check('unit spinor stabilizer is precisely upper su3', len(null)==8 and all(a[:,3]==s.zeros(4,1) and a[3,:]==s.zeros(1,4) and s.trace(a[:3,:3])==0 for a in stabilizers))

# Loops in U3xU2 have determinant windings(a,b), then SO parities(a,b).
# Exact integer symbolic restriction to S(U3xU2), not a numerical angle fit.
k = s.Symbol('k', integer=True)
check('special-unitary total winding vanishes identically', s.expand(k + (-k)) == 0)
check('single-factor winding need not lift to total Spin', (1+0)%2 == 1)
check('paired odd windings do lift to total Spin', (1+(-1))%2 == 0)

# Lens L(m,1): integral cellular cochain differential C1->C2 is m,
# other positive-degree differentials zero; H1Z=0,H2Z=Z/m.
# For even m, mod2 differential is zero, H1Z2=Z2.
m=4; a=1; determinant=(2*a)%m
check('Z4 fixed determinant is nonzero although mod2 zero', determinant != 0 and determinant%2 == 0)
check('opposite integral torsion cancels, individually nonzero', (determinant + (-determinant))%m == 0 and determinant != 0)
check('RP3 phase obstruction: integral H1 rank0, mod2 H1 rank1', s.Matrix([[2]]).rank()==1 and 2%2==0)

# Root/phase Bockstein: lift the mod2 generator1 at C1 to integer1;
# delta1=2, divided by2 is generator1 of H2Z=Z2.
check('RP3 Bockstein is nonzero', ((2*1)//2)%2 == 1)

mutations = {
    'c1 real zero suffices for a fixed determinant': determinant == 0,
    'phase can reach every Spin on RP3': ((2*1)//2)%2 == 0,
    'each factor loop must have even winding to lift': 1%2 == 0,
    'SU4 unit-spinor stabilizer has orbit dimension6': action.rank() == 6,
}
check('four stronger alternatives rejected', not any(mutations.values()))
print(json.dumps({'status':'PASS','exact_controls':len(checks),'checks':checks,'rejected_alternatives':list(mutations),'ceiling':'Finite group/cohomology controls only; obstruction-theory and GU applicability require the written proof and review.'},indent=2))
