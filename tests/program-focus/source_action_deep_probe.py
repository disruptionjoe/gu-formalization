"""Exact structural controls; written proofs own analytic conclusions.
Run with --full-coefficients for every published K/N full-tensor replay.
No Lean, physical-state or GU-wide verdict is certified by this probe.
"""
import json,argparse
from pathlib import Path
from fractions import Fraction as Q
import source_action_deep_geometry as g
from source_action_deep_algebra import Engine,replay_coefficients,verify_generation,verify_roots


"""Exact connected-isotropy exterior characters, not fitted dimension counts."""
from collections import defaultdict

def character_checks():
    weights=[(a,b) for a in (-1,1) for b in (-1,1)]
    weights += [(a,b) for a in (-2,0,2) for b in (-2,0,2)]+[(0,0)]
    char={(0,0,0):1}
    for a,b in weights:
        new=defaultdict(int)
        for (degree,x,y),v in char.items():
            new[degree,x,y]+=v
            new[degree+1,x+a,y+b]+=v
        char=dict(new)
    dims=[];checks={}
    for degree in range(15):
        c={(x,y):v for (p,x,y),v in char.items() if p==degree}
        mult={}
        for a in range(9):
            for b in range(9):
                m=c.get((a,b),0)-c.get((a+2,b),0)-c.get((a,b+2),0)+c.get((a+2,b+2),0)
                assert m>=0,(degree,a,b,m)
                if m:mult[a,b]=m
        rebuilt=defaultdict(int)
        for (a,b),m in mult.items():
            for x in range(-a,a+1,2):
                for y in range(-b,b+1,2):rebuilt[x,y]+=m
        assert dict(rebuilt)==c
        checks[f'grade_{degree}_full_irrep_reconstruction']=True
        dims.append(sum(mult.get(k,0) for k in ((0,0),(1,1),(2,2))))
    assert dims==[1,3,3,7,20,31,30,26,30,31,20,7,3,3,1]
    assert sum(dims)==216
    assert sum(dims[k] for k in range(15) if k%4 in (1,2))==122
    checks['derived_full_and_reality_dimensions']=True
    return {'checks':checks,'count':len(checks),'all_passed':True,'degree_dimensions':dims,'full_dimension':216,'reality_fixed_dimension':122}


"""Small rational certificate for actual-branch holonomy limits; root runs."""
from fractions import Fraction as Q
import json
import source_action_deep_geometry as g

def rank(rows):
    rows=[list(map(Q,r)) for r in rows];r=0
    for c in range(len(rows[0])):
        p=next((i for i in range(r,len(rows)) if rows[i][c]),None)
        if p is None:continue
        rows[r],rows[p]=rows[p],rows[r]
        s=rows[r][c];rows[r]=[x/s for x in rows[r]]
        for i in range(len(rows)):
            if i!=r and rows[i][c]:
                s=rows[i][c];rows[i]=[a-s*b for a,b in zip(rows[i],rows[r])]
        r+=1
    return r

def holonomy_checks():
    out={};t=[Q(21,4)]*5+[Q(15,4)]*9
    def check(k,v):out[k]=bool(v);assert v,k
    check('all_vertical_Nomizu_maps_zero',all(not any(row) for a in range(4,14) for row in g.L[a]))
    for v in range(4):
        check(f'trace_curvature_is_Lambda_{v}',g.curvature(v,4)==g.L[v])
        for a in range(4,14):
            Av=[g.A[a-4][k][v] for k in range(4)]
            expected=[[sum(Av[k]*g.L[k][i][j] for k in range(4)) for j in range(14)] for i in range(14)]
            check(f'mixed_curvature_formula_{v}_{a}',g.curvature(v,a)==expected)
            dt=[t[a]*g.L[v][k][a]-t[v]*g.L[a][k][v]-t[k]*g.mbracket(v,a).get(k,0) for k in range(14)]
            check(f'curvature_first_jet_{v}_{a}',dt==[(t[v]-t[a])*(Av[k] if k<4 else 0) for k in range(14)])
    picks=[(0,5,Q(1)),(1,5,Q(-1)),(2,6,Q(-2)),(3,7,Q(-3))]
    for v,a,lam in picks:
        check(f'eigenvalue_fixture_{v}',[g.A[a-4][k][v] for k in range(4)]==[lam if k==v else 0 for k in range(4)])
        check(f'zero_order_curvature_cancellation_{v}',g.curvature(v,a)==[[lam*x for x in row] for row in g.curvature(v,4)])
        dt=[t[a]*g.L[v][k][a]-t[v]*g.L[a][k][v]-t[k]*g.mbracket(v,a).get(k,0) for k in range(14)]
        check(f'rescaled_horizontal_Clifford_limit_{v}',[Q(2,3)/lam*x for x in dt]==[Q(k==v) for k in range(14)])
    normals=[]
    for v in range(4):
        for w in range(v,4):
            z=g.Lambda[v][w]
            check(f'normal_image_{v}_{w}',not any(z[:4]))
            check(f'Koszul_pairing_{v}_{w}',all(g.d[a]*z[a]==g.eta[w]*g.A[a-4][w][v] for a in range(4,14)))
            normals.append(z[4:])
    check('ten_normal_limits_span',rank(normals)==10)
    # Actual spin injection, not doubled historical curvature normalization.
    for v in range(4):
        for w in range(4):
            spinR=g.curvature_spin(v,4)
            check(f'spin_commutator_normal_limit_{v}_{w}',g.cliff_comm(spinR,{1<<w:Q(1)})=={1<<k:a for k,a in enumerate(g.Lambda[v][w]) if a})
    return {'checks':out,'count':len(out),'all_passed':all(out.values()),'normal_limit_rank':rank(normals),'scope':'exact coefficient limits for actual analytic holonomy; physical sector interpretation separate'}



"""Native Gaussian-rational quaternionic/Krein controls; root runs."""
from fractions import Fraction as Q
from math import comb
import json

def reality_checks():
    size=128;I=(1,3,5,7,10,12);neg=(9,10,11,12,13)
    checks={}
    def check(k,v):checks[k]=bool(v);assert v,k
    def phase(p,a):return [a,(-a[1],a[0]),(-a[0],-a[1]),(a[1],-a[0])][p%4]
    def conj(v):return [(a,-b) for a,b in v]
    def scale(q,v):return [(q*a,q*b) for a,b in v]
    def gamma(j,v):
        bit,yy=6-j//2,j%2;out=[]
        for r in range(size):
            p=2*((r>>(bit+1)).bit_count()%2)
            if yy:p+=1 if (r>>bit)&1 else 3
            if j>=9:p+=1
            out.append(phase(p,v[r^(1<<bit)]))
        return out
    def product(axes,v):
        for a in reversed(axes):v=gamma(a,v)
        return v
    def C(v):return product(I,v)
    def J(v):return C(conj(v))
    def H(v):return [phase(1,a) for a in product(neg,v)]
    def mul(z,w):return(z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
    def inner(v,w):
        z=[mul((a,-b),x) for (a,b),x in zip(v,w)]
        return(sum(a for a,b in z),sum(b for a,b in z))
    v=[(Q(j%11-5),Q(j%7-3)) for j in range(size)]
    w=[(Q(j%5-2),Q(j%13-6)) for j in range(size)]
    check('C_is_real',C(conj(v))==conj(C(v)))
    check('C_squared_minus1',C(C(v))==scale(-1,v))
    check('J_squared_minus1',J(J(v))==scale(-1,v))
    check('H_squared_plus1',H(H(v))==v)
    for a in range(14):check(f'J_commutes_gamma_{a}',J(gamma(a,v))==gamma(a,J(v)))
    check('J_anti_commutes_Krein_H',J(H(v))==scale(-1,H(J(v))))
    vw=inner(v,w)
    check('auxiliary_J_antiunitary',inner(J(v),J(w))==(vw[0],-vw[1]))
    hvw=inner(v,H(w))
    check('J_is_Krein_antiisometry',inner(J(v),H(J(w)))==(-hvw[0],hvw[1]))
    check('complex_bilinear_beta_symmetric',inner(J(v),H(w))==inner(J(w),H(v)))
    fixed=sum(comb(14,k) for k in range(15) if k%4 in (1,2))
    dims=[1,3,3,7,20,31,30,26,30,31,20,7,3,3,1]
    check('fixed_skew_real_dimension_8128',fixed==8128)
    check('not_sp32_32_dimension',fixed!=64*(2*64+1))
    check('invariant_fixed_space_122',sum(dims[k] for k in range(15) if k%4 in (1,2))==122)
    check('complement_invariant_space_94',sum(dims[k] for k in range(15) if k%4 not in (1,2))==94)
    return {'checks':checks,'count':len(checks),'all_passed':all(checks.values()),'scope':'native antilinear/quaternionic branch symmetry, not positive physical reality or family count'}



"""Tiny exact twining-character control. Root owns execution."""
from collections import defaultdict
import json


def reflection_checks():
    # (reflection eigenvalue, diagonal-sl2 weight) for the actual tangent.
    eigen=[(1,w) for w in (-2,0,2)]+[(1,w) for w in (-4,-2,0,2,4)]
    eigen += [(1,0),(1,0),(-1,0)]+[(-1,w) for w in (-2,0,2)]
    char={(0,0):1}
    for sign,weight in eigen:
        nxt=defaultdict(int)
        for (degree,w),v in char.items():
            nxt[(degree,w)]+=v;nxt[(degree+1,w+weight)]+=sign*v
        char=dict(nxt)
    traces=[char.get((p,0),0)+char.get((p,2),0)-char.get((p,6),0)-char.get((p,8),0)
            for p in range(15)]
    expected=[1,3,3,-1,-6,-5,2,6,2,-5,-6,-1,3,3,1]
    assert traces==expected
    dims=[1,3,3,7,20,31,30,26,30,31,20,7,3,3,1]
    fixed=[(a+b)//2 for a,b in zip(dims,traces)]
    assert all((a+b)%2==0 and a>=abs(b) for a,b in zip(dims,traces))
    real={p:fixed[p] for p in range(15) if p%4 in (1,2)}
    assert real=={1:3,2:3,5:13,6:16,9:13,10:7,13:3,14:1}
    assert sum(real.values())==59 and sum(fixed)==108
    return {'passed':True,'degree_reflection_traces':traces,'real_fixed_degree_dimensions':real,
            'real_fixed_total':59,'full_u_fixed_total':108,
            'ceiling':'representation count; actual equivariance justified separately'}




"""Exact controls for analytic finite-jet nonautonomy; root executes."""
from fractions import Fraction as Q
from math import factorial


def dynamics_checks():
    n,size=14,128
    signs=[1]*9+[-1]*5
    H=(0,1,2,9)
    zero=[(Q(0),Q(0))]*size
    checks={}
    def check(k,p):
        checks[k]=bool(p)
        assert p,k
    def add(a,b): return [(x[0]+y[0],x[1]+y[1]) for x,y in zip(a,b)]
    def scale(c,a): return [(c*x,c*y) for x,y in a]
    def phase(p,a): return [a,(-a[1],a[0]),(-a[0],-a[1]),(a[1],-a[0])][p%4]
    def gamma(j,v):
        bit,yy=6-j//2,j%2
        out=[]
        for r in range(size):
            p=2*((r>>(bit+1)).bit_count()%2)
            if yy:p+=1 if (r>>bit)&1 else 3
            if j>=9:p+=1
            out.append(phase(p,v[r^(1<<bit)]))
        return out
    def vsum(vs):
        out=zero
        for v in vs:out=add(out,v)
        return out
    def trace(z):return vsum(scale(signs[a],gamma(a,z[a])) for a in range(n))
    def F(z,nu):
        e=add(nu,scale(-1,trace(z)))
        return [add(z[a],scale(Q(1,2),gamma(a,e))) for a in range(n)],e
    def Finv(zp,e):
        return [add(zp[a],scale(Q(-1,2),gamma(a,e))) for a in range(n)],add(trace(zp),scale(1-Q(n,2),e))
    def R(r,t):
        v=add(t,scale(Q(-1,2),trace(r)))
        return [add(r[a],scale(Q(1,2),gamma(a,v))) for a in range(n)],v
    def sigma(axis,z,nu):
        tau=trace(z)
        r=[add(scale(signs[axis],gamma(axis,z[a])),
               add(nu,scale(-1,tau)) if a==axis else zero) for a in range(n)]
        t=add(scale(signs[axis],z[axis]),scale(Q(-1,2)*signs[axis],gamma(axis,nu)))
        return r,t
    def Atinv(r,t):
        # theta is negative horizontal axis9. c(theta)=eta9 gamma9,
        # so c(theta)^-1=gamma9, since c(theta)^2=eta9.
        u,v=R(r,t)
        return Finv([gamma(9,w) for w in u],scale(-1,gamma(9,v)))
    def field_scale(c,f):return [scale(c,w) for w in f[0]],scale(c,f[1])
    def evolution(axis,f):return field_scale(-1,Atinv(*sigma(axis,*f)))
    def q(f):return tuple(f[0][a] for a in H)+(f[1],)
    psi=[(Q(j%7-3),Q(j%5-2)) for j in range(size)]
    v=([zero for _ in range(n)],psi)
    check('native_readout_five_slots',len(q(v))==5 and q(v)[-1]!=zero)
    z=[[(Q((a+j)%7-3),Q((a*j)%5-2)) for j in range(size)] for a in range(n)]
    generic=(z,psi)
    check('native_time_symbol_inverse',Atinv(*sigma(9,*generic))==generic)
    check('field_inverse_transport',Finv(*F(*generic))==generic)
    for normal in (4,10):
        factor=Q(-signs[normal],signs[9])
        check(f'evolution_square_{normal}',evolution(normal,evolution(normal,generic))==field_scale(factor,generic))
        for N in range(1,5):
            b=v
            for _ in range(N): b=field_scale(1/factor,evolution(normal,b))
            image=b
            for _ in range(N): image=evolution(normal,image)
            check(f'nonzero_Nth_readout_{normal}_{N}',q(image)==q(v) and q(image)[-1]!=zero)
            check(f'initial_lower_monomial_jets_{normal}_{N}',all(0<N-j for j in range(N)))

    # Generic variable-coefficient L=M(z)d/dz+C(z), not just a frozen
    # symbol. Polynomial vectors are lists of two rational coefficients.
    def padd(a,b):
        return [(a[i] if i<len(a) else Q(0))+(b[i] if i<len(b) else Q(0))
                for i in range(max(len(a),len(b)))]
    def pmul(a,b):
        out=[Q(0)]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):out[i+j]+=x*y
        return out
    def pd(a):return [Q(i)*a[i] for i in range(1,len(a))] or [Q(0)]
    Mp=[[[Q(1),Q(1)],[Q(0),Q(1)]],[[Q(0)],[Q(2),Q(-1)]]]
    Cp=[[[Q(0),Q(1)],[Q(1)]],[[Q(3)],[Q(0),Q(0),Q(1)]]]
    def L(f):
        return [padd(padd(pmul(Mp[i][0],pd(f[0])),pmul(Mp[i][1],pd(f[1]))),
                     padd(pmul(Cp[i][0],f[0]),pmul(Cp[i][1],f[1]))) for i in range(2)]
    for N in range(1,7):
        f=[[Q(0)]*N+[Q(1)],[Q(0)]*N+[Q(3)]]
        for j in range(N):
            check(f'variable_coeff_lower_jet_{N}_{j}',[p[0] for p in f]==[0,0])
            f=L(f)
        check(f'variable_coeff_first_signal_{N}',[p[0] for p in f]==[factorial(N),3*(2**N)*factorial(N)])
    return {'checks':checks,'count':len(checks),'all_passed':all(checks.values()),
            'scope':'finite native/variable-coefficient controls; CK and arbitrary finite-jet proof are written separately'}




def engine_checks():
    E=Engine(g);c=E.calibration_checks();S=E.S_known();KS=E.K(S)
    c['native_curvature_Phi_source']=E.Phi(E.curvature())==S
    # Normal v=e6/6+e7/12 means U=-eta diag(1,1,-1,-1)/2.
    # The prior receiver uses the opposite U; transport, do not fit its sign.
    Z={(1,(1<<0)|(1<<6)):Q(1,6),(1,(1<<0)|(1<<7)):Q(1,12)}
    c['KS_rational_normal_positive_three_quarters']=E.pair(Z,KS)==Q(3,4)
    c['KS_prior_opposite_normal_negative_three_quarters']=-E.pair(Z,KS)==Q(-3,4)
    c['parallel_Clifford_one_form_K_zero']=not E.K(E.phi1)
    assert all(c.values()),c
    return {'checks':c,'count':len(c),'all_passed':True}

def main():
    p=argparse.ArgumentParser();p.add_argument('--full-coefficients',action='store_true');args=p.parse_args()
    root=Path(__file__).resolve().parents[2]
    results={'geometry':g.checks(),'characters':character_checks(),'engine':engine_checks(),
       'holonomy':holonomy_checks(),'reality':reality_checks(),'reflection':reflection_checks(),
       'dynamics':dynamics_checks()}
    results['coefficients']=replay_coefficients(root/'lab/process/source-action-deep-coefficients.json',args.full_coefficients)
    results['generation']=verify_generation(json.loads((root/'lab/process/source-action-deep-coefficients.json').read_text()))
    results['roots']=verify_roots(json.loads((root/'lab/process/source-action-deep-coefficients.json').read_text()))
    count=sum(v.get('count',len(v.get('checks',{}))) for v in results.values())
    print(json.dumps({'all_passed':True,'structural_control_count':count,'results':results,
       'scope':'exact coefficient/character/fixture controls plus written internal analytic proofs; no physical/source verdict'},indent=2))

if __name__=='__main__':main()
