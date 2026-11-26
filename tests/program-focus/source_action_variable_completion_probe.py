"""Exact controls for the written actual-variable finite-band theorem.

Native principal controls check the actual repaired carrier. Rational 2x2
variable-coefficient controls test the density-dual and normalization mechanism;
they are not a replacement for the parameterized CK proof. No physical spectrum
or nonlinear coupled-domain certificate is claimed.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import json

from source_action_slice_completion_probe import (
    column, covector, inverse, sigma, norm, inject, readout,
)


def mat(rows):
    return [[Q(x) for x in r] for r in rows]


def mul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(*xs):
    return [[sum(x[i][j] for x in xs) for j in range(len(xs[0][0]))]
            for i in range(len(xs[0]))]


def scale(c, a):
    return [[c*x for x in r] for r in a]


def inv(a):
    det=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    assert det
    return scale(1/det, [[a[1][1],-a[0][1]],[-a[1][0],a[0][0]]])


def cmul(z, w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])


def csub(z, w):
    return (z[0]-w[0],z[1]-w[1])


def run():
    count=0
    for xi in (covector(3),covector(8)):
        assert norm(xi)!=0
        for j in range(15):
            v=column(j)
            assert inverse(xi,sigma(xi,v))==v
            assert sigma(xi,inverse(xi,v))==v
            count+=2
    for j in range(5):
        target=[{} for _ in range(5)];target[j]={0:Q(1)}
        assert readout(inject(j))==target
        count+=1

    # Nonconstant analytic toy data at z=0: density and Az derivatives matter.
    # Here row is UNABSORBED beta; the report instead uses eta=rho*beta.
    # The real parameter below is a mechanism control, not a native spectrum.
    az=mat([[2,1],[0,1]]);azp=mat([[0,1],[1,0]])
    at=mat([[1,1],[0,2]]);c=mat([[1,2],[-1,1]])
    f=mat([[1,0],[0,1]]);row=mat([[1,1],[0,1]])
    rho=Q(2);rhop=Q(1);zero=mat([[0,0],[0,0]])
    divergence=add(scale(rhop/rho,az),azp)
    for lam in map(Q,[-3,0,2]):
        p=add(c,scale(lam,at))
        fz=scale(-1,mul(inv(az),mul(p,f)))
        rz=mul(add(mul(row,p),scale(-1,mul(row,divergence))),inv(az))
        assert add(mul(az,fz),mul(p,f))==zero;count+=1
        assert add(scale(-1,mul(rz,az)),scale(-1,mul(row,divergence)),mul(row,p))==zero;count+=1
        fluxprime=add(scale(rhop,mul(row,mul(az,f))),
            scale(rho,mul(rz,mul(az,f))),scale(rho,mul(row,mul(azp,f))),
            scale(rho,mul(row,mul(az,fz))))
        assert fluxprime==zero;count+=1
        frozen_rz=mul(mul(row,p),inv(az))
        bad=add(scale(-1,mul(frozen_rz,az)),scale(-1,mul(row,divergence)),mul(row,p))
        assert bad!=zero;count+=1

    # A cross-Gram need not be Hermitian. Normalize on the LEFT, not by
    # congruence or by multiplication inside the native field slot.
    n=mat([[2,1],[0,1]]);t=mat([[1,0],[1,2]])
    raw=mul(n,inv(t));left=mul(inv(n),raw)
    assert mul(left,t)==f;count+=1
    assert mul(mul(raw,inv(n)),t)!=f;count+=1
    assert n!=[list(x) for x in zip(*n)];count+=1

    # Exact Gaussian-rational phase checks for S=Re integral eta D psi.
    # eta=phase*a^dagger G, delta psi=-i psi, psi_t=-i omega psi.
    unit_minus_i=(Q(0),Q(-1));z=(Q(2),Q(3));zbar=(z[0],-z[1])
    rows=[]
    for phase in [(Q(1),Q(0)),(Q(0),Q(1)),(Q(0),Q(-1))]:
        charge=cmul(phase,unit_minus_i)[0]
        symplectic=cmul(phase,csub(z,zbar))[0]
        energy=5*charge
        rows.append({'phase':list(map(str,phase)),'charge_factor':str(charge),
                     'symplectic_at_inner_2plus3i':str(symplectic),'energy_at_omega5':str(energy)})
        if phase==(Q(0),Q(1)):
            assert (charge,symplectic,energy)==(1,-6,5)
        elif phase==(Q(1),Q(0)):
            assert (charge,symplectic,energy)==(0,0,0)
        else:
            assert (charge,symplectic,energy)==(-1,6,-5)
        count+=3
    # Omega=-2Im <.,.>, complex structure I=-i: Omega(a,Ia)=2||a||².
    for squared_norm in map(Q,[1,2,5]):
        assert -2*(-squared_norm)==2*squared_norm>0;count+=1

    # Incompatible nonnegative selected laws; samples are controls only.
    # The theorem quantifies over every bounded real omega on fixed compact K.
    for k2 in map(Q,[0,1,4,9]):
        w1=1+k2;w2=1+2*k2
        assert 0<w1<=w2 and (w1==w2)==(k2==0);count+=1
    return {'controls':count,'native_principal_controls':65,
        'variable_density_dual_controls':12,'normalization_controls':3,
        'phase_charge_energy_controls':12,'dispersion_controls':4,
        'phase_table':rows,'derivative_omission_detected':True,
        'wrong_matrix_order_detected':True,
        'scope':'Native repaired noncharacteristic/readout algebra; synthetic exact variable-density dual, non-Hermitian Gram and real-action phase controls. Uniform CK, infinite-dimensional bounds, native specialization and source relevance are written/reviewed proofs, not inferred from samples.'}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path)
    args=parser.parse_args();s=json.dumps(run(),indent=2)+'\n'
    if args.output:args.output.write_text(s)
    else:print(s)
