"""Native symbol controls for analytic slice-history lifting.

The actual variable-coefficient CK and triangular-rank proofs are written
results. Polynomial solutions below are PRINCIPAL controls, not substitutes
for the actual curved equation. Full carrier rank1920, literal readout640,
all complex. No59-variable dynamical approximation or physical domain.
"""
from fractions import Fraction as Q
from math import comb
import json
from pathlib import Path
import argparse
import source_action_deep_geometry as geo
from source_action_deep_algebra import add,scale
from source_action_physical_probe import mul,gamma,contraction,field_F_inverse


def zero():return ([{}for _ in range(14)],{})
def vadd(*vs):return ([add(*(v[0][i]for v in vs))for i in range(14)],add(*(v[1]for v in vs)))
def vscale(a,v):return ([scale(a,x)for x in v[0]],scale(a,v[1]))
def column(i):
    z,s=zero()
    if i==14:s={0:Q(1)}
    else:z[i]={0:Q(1)}
    return z,s

def covector(i):
    xi=[Q(0)]*14;xi[i]=Q(1);return xi

def slash(xi):return add(*(scale(xi[i]/geo.d[i],gamma(i))for i in range(14)))
def norm(xi):return sum(xi[i]*xi[i]/geo.d[i]for i in range(14))
def sigma(xi,v):
    z,nu=v;c=slash(xi);tr=contraction(z,range(14))
    r=[add(mul(c,z[i]),scale(-xi[i],tr),scale(xi[i],nu))for i in range(14)]
    s=add(*(scale(xi[i]/geo.d[i],z[i])for i in range(14)),scale(-Q(1,2),mul(c,nu)))
    return r,s

def inverse(xi,v):
    r,s=v
    eta=add(s,scale(-Q(1,2),contraction(r,range(14))))
    u=[add(r[i],scale(Q(1,2),mul(gamma(i),eta)))for i in range(14)]
    ci=scale(1/norm(xi),slash(xi))
    return field_F_inverse([mul(ci,x)for x in u],scale(-1,mul(ci,eta)))

def readout(v):return v[0][:4]+[v[1]]
def inject(j):return column(j if j<4 else 14)
def power(op,j,v):
    for _ in range(j):v=op(v)
    return v

def run():
    checks=0;t=covector(3);n=covector(8);nneg=covector(4);other=covector(9)
    for xi in (t,n,nneg):
        assert norm(xi)!=0
        for j in range(15):
            v=column(j)
            assert inverse(xi,sigma(xi,v))==v;checks+=1
            assert sigma(xi,inverse(xi,v))==v;checks+=1
    def M(v):return vscale(-1,inverse(t,sigma(n,v)))
    def Minv(v):return vscale(-1,inverse(n,sigma(t,v)))
    for j in range(15):
        v=column(j)
        assert M(M(v))==vscale(-norm(n)/norm(t),v);checks+=1
        assert M(Minv(v))==v and Minv(M(v))==v;checks+=1
    # Generic shifted Clifford cone, not just orthogonal/diagonal tests.
    tau=covector(3);tau[0]=Q(1,2)
    for spatial in [(1,1,0),(0,1,2),(2,-1,1)]:
        k=list(map(Q,spatial))+[Q(0)]*11
        aa=norm(tau);dd=sum(tau[i]*k[i]/geo.d[i]for i in range(14));ee=norm(k)
        shift=-dd/aa;cone=dd*dd/(aa*aa)-ee/aa
        def shifted_M(v):return vadd(vscale(-1,inverse(tau,sigma(k,v))),vscale(-shift,v))
        for j in range(15):
            v=column(j)
            assert shifted_M(shifted_M(v))==vscale(cone,v);checks+=1
        if spatial==(1,1,0):assert dd!=0 and shift!=0;checks+=1
    for j in range(5):
        expected=[{}for _ in range(5)];expected[j]={0:Q(1)}
        assert readout(inject(j))==expected;checks+=1
        for order in range(7):
            # q M^order M^-order J = I on ALL128 spinor coefficients.
            assert readout(power(M,order,power(Minv,order,inject(j))))==expected;checks+=1
    # Actual native principal polynomial extension of boundary t^d Jf:
    # psi=sum binomial(d,j)t^(d-j)z^j Minv^j Jf.
    for degree in range(1,6):
        v=inject(4)
        coeff=[vscale(Q(comb(degree,j)),power(Minv,j,v))for j in range(degree+1)]
        for j in range(degree):
            residual=vadd(vscale(degree-j,sigma(t,coeff[j])),vscale(j+1,sigma(n,coeff[j+1])))
            assert residual==zero();checks+=1
        assert readout(coeff[0])==readout(v);checks+=1
    # Whole-history kernel prototype: z2*v-z1*A_n^-1 A_z2*v.
    # Its boundary data is z2*v, and q at z1=z2=0 vanishes for ALL time.
    v=inject(4);w=vscale(-1,inverse(n,sigma(other,v)))
    assert vadd(sigma(other,v),sigma(n,w))==zero();checks+=1
    assert v!=zero() and readout(v)!=[{}for _ in range(5)];checks+=1
    # Mutation: dropping compensating normal derivative does not solve D.
    assert sigma(other,v)!=zero();checks+=1
    # Universal triangular-rank control with deliberately nonzero lower blocks.
    # This is an elementary control, not claimed actual curved coefficients.
    for size in range(1,8):
        target=[Q((j+1)**2)for j in range(size)];sol=[]
        for j in range(size):sol.append(target[j]-sum(Q((j+1)*(i+2))*sol[i]for i in range(j)))
        assert [sol[j]+sum(Q((j+1)*(i+2))*sol[i]for i in range(j))for j in range(size)]==target;checks+=1
    return {'controls':checks,'principal_inverse_full_columns':15,
      'complex_carrier_rank':1920,'complex_literal_readout_rank':640,
      'jet_rank_formula_complex':'640*(N+1)','jet_kernel_formula_complex':'1280*(N+1)',
      'jet_rank_formula_real':'1280*(N+1)','jet_kernel_formula_real':'2560*(N+1)',
      'native_shifted_cone_full_columns':15,'generic_spatial_covectors':3,
      'native_diagonal_right_inverse_orders':list(range(7)),
      'native_principal_visible_polynomial_degrees':list(range(1,6)),
      'native_principal_whole_history_kernel':True,
      'scope':'Controls verify actual repaired principal algebra. Variable-coefficient analytic onto/lift/kernel and rank claims rely on written CK/free-jet proofs; no physical contour/domain selected.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);args=parser.parse_args()
    text=json.dumps(run(),indent=2)+'\n'
    if args.output:args.output.write_text(text)
    else:print(text)
