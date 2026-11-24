#!/usr/bin/env python3
"""Exact small Clifford-word controls; not a full operator/anomaly proof.
Root executes serially. Faithful Cl14 blade algebra, actual K95 diagonal metric.
"""
from fractions import Fraction as F
from math import prod

# Exact Gaussian rationals as (real, imaginary).
def ga(a=0,b=0): return (F(a),F(b))
def add(a,b): return(a[0]+b[0],a[1]+b[1])
def neg(a): return(-a[0],-a[1])
def gm(a,b): return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a): return(a[0],-a[1])
ONE=ga(1); II=ga(0,1); ZERO=ga()
metric=(-1,1,1,1,2,2,2,2,6,12,-2,-2,-2,-4)

def clean(a): return {m:c for m,c in a.items() if c != ZERO}
def plus(a,b):
    out=dict(a)
    for m,c in b.items(): out[m]=add(out.get(m,ZERO),c)
    return clean(out)
def scale(a,z): return clean({m:gm(c,z) for m,c in a.items()})
def minus(a,b): return plus(a,scale(b,ga(-1)))
def mul(a,b):
    out={}
    for left,cl in a.items():
        for right,cr in b.items():
            swaps=sum((right & ((1<<j)-1)).bit_count() for j in range(14) if (left>>j)&1)
            w=(-1)**swaps * prod(metric[j] for j in range(14) if (left & right)>>j&1)
            out[left^right]=add(out.get(left^right,ZERO),gm(gm(cl,cr),ga(w)))
    return clean(out)
def sharp(a):
    return clean({m:gm(conj(c),ga((-1)**(m.bit_count()*(m.bit_count()-1)//2))) for m,c in a.items()})
def comm(a,b): return minus(mul(a,b),mul(b,a))
def anti(a,b): return plus(mul(a,b),mul(b,a))
I={0:ONE}
def c(j): return {1<<j:ONE}
Hvol={15:ONE}
ZN={(1<<14)-16:ga(F(1,192))}
Omega={(1<<14)-1:ga(F(1,192))}
chi=scale(Hvol,II)
checks=0
def check(condition,label):
    global checks
    assert condition,label
    checks+=1

check(mul(ZN,ZN)==scale(I,ga(-1)),"normal volume square")
check(mul(Omega,Omega)==I,"ambient volume square")
check(mul(chi,chi)==I,"horizontal chirality square")
check(scale(mul(Omega,chi),II)==ZN,"normal-center grade relation")
check(sharp(ZN)==scale(ZN,ga(-1)),"normal volume sharp")
check(sharp(Omega)==scale(Omega,ga(-1)),"ambient volume sharp")
for j in range(14):
    check((comm(ZN,c(j)) if j<4 else anti(ZN,c(j)))=={},f"normal volume parity axis{j}")
    check(anti(Omega,c(j))=={},f"ambient volume parity axis{j}")

# Two distinct source-admitted directions: mixed metric-spin and odd full-parent.
T=mul(c(0),c(4)); A=scale(c(0),II)
check(sharp(T)==scale(T,ga(-1)),"metric mixed generator Krein-skew")
check(sharp(A)==scale(A,ga(-1)),"odd unitary-parent generator Krein-skew")
check(comm(Omega,T)=={},"metric mixed preserves ambient grade")
check(comm(ZN,T)!={},"metric mixed breaks normal-center fixed-background symmetry")
check(comm(ZN,A)=={},"horizontal odd-parent direction preserves normal spin matrix")
check(anti(Omega,A)=={},"odd-parent direction flips ambient grade")
check(minus(mul(mul(Omega,A),Omega),A)==scale(A,ga(-2)),"actual axial NE vertex defect")
check(mul(A,A)!= {},"nonnull full-parent defect invertible scalar square")

# Actual q crossing: Gamma_H commutes; Gamma_N anticommutes. A reflected
# normal form contributes another minus and gives the uniform receiver action.
check(mul(c(0),ZN)==mul(ZN,c(0)),"q horizontal spin-only")
check(mul(c(4),ZN)==scale(mul(ZN,c(4)),ga(-1)),"q normal spin-only sign")
check(scale(mul(c(4),ZN),ga(-1))==mul(ZN,c(4)),"q simultaneous-form action")
# b<-sigma principal coefficient at xi=e0, perpendicular output=e1, a=1,c0=-1/12.
B=scale(mul(c(1),c(0)),ga(F(1,12)))
check(comm(ZN,B)=={},"principal coefficient commutes with normal volume")
check(plus(mul(ZN,B),mul(B,ZN))!= {},"spin-only receiver unequal-sign obstruction")
# sigma<-b shape blade: no universal theorem is inferred from this control.
Fshape=mul(c(4),c(0))
check(comm(ZN,Fshape)==scale(mul(ZN,Fshape),ga(2)),"geometric receiver lower commutator")
check(comm(Omega,Fshape)=={},"ambient lower countercontrol")

# Independent bars: phase uses inverse; axial grade uses same-side law.
z=scale(I,II); u=scale(Omega,II)
check(mul(mul(scale(z,ga(-1)),c(0)),z)==c(0),"phase contragredient bars")
check(mul(mul(u,c(0)),u)==c(0),"axial same-side bars")
check(mul(mul(scale(u,ga(-1)),c(0)),u)==scale(c(0),ga(-1)),"axial is not ordinary phase bar law")
check(sharp(u)==u and mul(sharp(u),u)==scale(I,ga(-1)),"axial Krein anti-isometry distinction")
check(mul(mul(u,I),scale(u,ga(-1)))==I,"raw NE opposite-slot axial bar law")
print(f"PASS {checks} exact Clifford-word controls; no physical anomaly or full-operator claim")
