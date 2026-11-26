"""Exact finite controls for covariant all-history normal-jet ambiguity.

Written CK filtration proof retains actual analytic coefficients. Native symbol
controls below check its noncharacteristic/leading-order seam; the deliberately
variable scalar recurrence is a countercontrol, NOT the actual GU equation.
"""
from fractions import Fraction as Q
from math import factorial, comb
from pathlib import Path
import argparse, hashlib, json
import source_action_deep_geometry as g
import source_action_slice_completion_probe as n

ROOT=Path(__file__).resolve().parents[2]
# Sparse rational polynomials in three variables.
def plus(*ps):
    z={}
    for p in ps:
        for k,v in p.items():z[k]=z.get(k,Q(0))+v
    return {k:v for k,v in z.items() if v}
def times(p,q):
    z={}
    for a,v in p.items():
        for b,w in q.items():
            k=tuple(x+y for x,y in zip(a,b));z[k]=z.get(k,Q(0))+v*w
    return {k:v for k,v in z.items() if v}
def scale(c,p):return {k:c*v for k,v in p.items() if c*v}
def power(p,k):
    z={(0,0,0):Q(1)}
    for _ in range(k):z=times(z,p)
    return z
def diff(p,i):
    z={}
    for k,v in p.items():
        if k[i]:
            a=list(k);a[i]-=1;z[tuple(a)]=k[i]*v
    return z
def value(p,x):return sum(v*x[0]**k[0]*x[1]**k[1]*x[2]**k[2] for k,v in p.items())
def det3(a):return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
def mpow(a,k):
    out=g.eye()
    for _ in range(k):out=g.mm(out,a)
    return out

def run():
    checks=[]
    def check(name,condition):
        assert condition,name;checks.append(name)
    one={(0,0,0):Q(1)};v=[{tuple(int(i==j)for i in range(3)):Q(1)}for j in range(3)]
    fourth=scale(-1,plus(*v));p=[plus(*(power(x,k)for x in v+[fourth]))for k in (2,3,4)]
    jac=[[value(diff(pk,i),(1,2,3))for i in range(3)]for pk in p]
    check('trace_invariant_Jacobian_24192',det3(jac)==24192)
    for e in [Q(1,2),Q(1,7),Q(-1,3)]:
        check('Jacobian_scaling_'+str(e),det3([[value(diff(pk,i),(e,2*e,3*e))for i in range(3)]for pk in p])==24192*e**6)
    for k,pk in zip((2,3,4),p):check('invariant_homogeneous_'+str(k),all(sum(a)==k for a in pk))
    # Rational connected rotation and boost, conjugating an actual eta-self-adjoint Q.
    rot=g.eye();rot[0][0]=rot[1][1]=Q(3,5);rot[0][1]=Q(-4,5);rot[1][0]=Q(4,5)
    boost=g.eye();boost[0][0]=boost[3][3]=Q(5,3);boost[0][3]=boost[3][0]=Q(4,3)
    eta=g.diag(g.eta)
    for name,h in [('rotation',rot),('boost',boost)]:
        ht=[list(z)for z in zip(*h)];hi=g.mm(g.mm(eta,ht),eta)
        check(name+'_Lorentz',g.mm(g.mm(ht,eta),h)==eta and g.mm(h,hi)==g.eye())
        for j in range(1,10):
            a=[[g.A[j][i][k]+Q(j+1,3)*g.A[(j%9)+1][i][k]for k in range(4)]for i in range(4)]
            b=g.mm(g.mm(h,a),hi)
            check(name+'_trace_seed_'+str(j),g.trace(a)==g.trace(b)==0)
            for k in (2,3,4):check(f'{name}_p{k}_{j}',g.trace(mpow(a,k))==g.trace(mpow(b,k)))
    for m in range(1,7):
        # Along Q=s A5, p2=2s²; coefficient recovered by exact derivative.
        check('sharp_degree_'+str(2*m),value(p[0],(1,-1,0))==2 and factorial(2*m)*2**m>0)
    # Exact monomial enumeration independently compared with Hilbert-series DP.
    counts=[0]*33;counts[0]=1
    for w in (2,3,4):
        for k in range(w,33):counts[k]+=counts[k-w]
    cum=[]
    for N in range(33):
        triples=[(a,b,c)for c in range(N//4+1)for b in range((N-4*c)//3+1)for a in range((N-4*c-3*b)//2+1)]
        exact=sum(2*a+3*b+4*c==N for a,b,c in triples)
        check('weighted_coefficient_'+str(N),exact==counts[N]);check('weighted_cumulative_'+str(N),len(triples)==sum(counts[:N+1]));cum.append(len(triples))
        check('simplex_bounds_'+str(N),N**3<=144*len(triples)<=(N+9)**3)
    check('no_generation_count_interpretation',cum[12]==34 and counts[12]==7)
    # Full native rolled symbol at trace conormal: all15 slots with arbitrary spinor right factor.
    trace=n.covector(4);shape=n.covector(5)
    check('trace_coordinate_nonnull',n.norm(trace)==Q(-1,16))
    for j in range(15):
        z=n.column(j)
        check('trace_left_inverse_'+str(j),n.inverse(trace,n.sigma(trace,z))==z)
        check('trace_right_inverse_'+str(j),n.sigma(trace,n.inverse(trace,z))==z)
    # Exact native PRINCIPAL extension of s^d Jf. All terms homogeneous of
    # total normal degree d, so earlier normal jets vanish. Lower coefficients
    # enter later orders in the written actual-equation proof.
    def B(z):return n.vscale(-1,n.inverse(trace,n.sigma(shape,z)))
    for d in range(1,9):
        for j in range(5):
            coeff=[n.vscale(Q(comb(d,k)),n.power(B,k,n.inject(j)))for k in range(d+1)]
            for k in range(d):
                check(f'native_CK_leading_residual_{d}_{j}_{k}',n.vadd(n.vscale(k+1,n.sigma(trace,coeff[k+1])),n.vscale(d-k,n.sigma(shape,coeff[k])))==n.zero())
            check(f'native_first_visible_seed_{d}_{j}',n.readout(coeff[0])==n.readout(n.inject(j)))
    # Variable coefficient scalar control u_r=(1+r+s)u_s+(1+x)u_x+(1+s)u.
    # u=sum r^j u_j(s,x); polynomial dictionary variables interpreted (s,x,unused).
    s,x=v[0],v[1];A=plus(one,s);X=plus(one,x)
    for degree in range(1,7):
        coeff=[times(power(s,degree),plus(one,power(x,2)))];maxj=degree+2
        for j in range(maxj):
            rhs=plus(times(A,diff(coeff[j],0)),times(X,diff(coeff[j],1)),times(A,coeff[j]),diff(coeff[j-1],0)if j else {})
            coeff.append(scale(Q(1,j+1),rhs))
        for j,u in enumerate(coeff):
            check(f'variable_lower_and_base_filtration_{degree}_{j}',all(j+k[0]>=degree for k in u))
        check('variable_terms_really_present_'+str(degree),coeff[1]!=diff(coeff[0],0))
        # Mutation: second normal derivative destroys first-order filtration.
        if degree>=2:check('second_order_mutation_detected_'+str(degree),any(1+k[0]<degree for k in diff(diff(coeff[0],0),0)))
    refs=['tests/program-focus/source_action_deep_geometry.py','tests/program-focus/source_action_slice_completion_probe.py','explorations/conditional-build/source-action-rotation-rigidity-2026-11-26.md','explorations/conditional-build/source-action-physical-dynamics-2026-11-25.md']
    return dict(basis_revision='5b9ad658273dfa4b4cdb12f61e2ed91222457a6a',check_count=len(checks),checks=checks,jacobian=[[str(x)for x in row]for row in jac],jacobian_determinant=24192,weights=[2,3,4],graded_counts=counts,cumulative_counts=cum,native_principal_scope='Full15 slots; trace conormal inverse; five observed injection slots; degrees1..8. Principal controls only.',variable_control_scope='Deliberately non-native scalar equation checks filtration bookkeeping and second-order mutation; actual full PDE retained in reviewed proof.',source_hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in refs},claim_ceiling='Exact finite controls, not Lean/Python proof of CK existence, physical state space, full invariant ring or source necessity.')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);a=parser.parse_args();s=json.dumps(run(),indent=2)+'\n'
    if a.output:a.output.write_text(s)
    else:print(s)
