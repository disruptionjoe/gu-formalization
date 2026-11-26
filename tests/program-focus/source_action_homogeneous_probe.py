"""Reproducible exact controls for the local homogeneous analytic candidate.
Written proofs own existence; no native numeric radius, full PDE or physical certificate.
"""


"""Exact small controls for the homogeneous analytic-reduction proof.
Root executes. No native216-variable solve or numerical native radius claim.
"""
from fractions import Fraction as Q
from collections import defaultdict
import json


def eye(n): return [[Q(i == j) for j in range(n)] for i in range(n)]
def transpose(a): return list(map(list, zip(*a)))
def mm(a, b): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def mv(a, v): return [sum(x*y for x,y in zip(row,v)) for row in a]
def tr(a): return sum(a[i][i] for i in range(len(a)))
def inverse(a):
    n=len(a); m=[list(map(Q,row))+e for row,e in zip(a,eye(n))]
    for i in range(n):
        p=next(j for j in range(i,n) if m[j][i])
        m[i],m[p]=m[p],m[i]
        pivot=m[i][i];m[i]=[x/pivot for x in m[i]]
        for j in range(n):
            if j!=i:
                f=m[j][i];m[j]=[x-f*y for x,y in zip(m[j],m[i])]
    return [row[n:] for row in m]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def metric(y,v,U,w,V):
    yi=inverse(y);yu,yv=mm(yi,U),mm(yi,V)
    return dot(v,mv(y,w))+tr(mm(yu,yv))-Q(1,2)*tr(yu)*tr(yv)
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(c,a):return tuple(c*x for x in a)


def homogeneous_controls():
    checks={}
    def check(name,cond):
        checks[name]=bool(cond);assert cond,name
    y=[[Q(1),0,0,0],[0,Q(2),0,0],[0,0,Q(3),0],[0,0,0,Q(-1)]]
    A=[[Q(2),1,0,1],[0,Q(1),1,0],[0,0,Q(3),1],[0,0,0,Q(1)]]
    Ai=inverse(A)
    U=[[Q(1),2,0,1],[2,Q(-1),1,0],[0,1,Q(2),1],[1,0,1,Q(3)]]
    V=[[Q(2),0,1,0],[0,Q(3),0,1],[1,0,Q(-2),2],[0,1,2,Q(1)]]
    v=list(map(Q,[1,2,-1,3]));w=list(map(Q,[2,-1,3,1]))
    def transport(M):return mm(mm(transpose(Ai),M),Ai)
    yp,Up,Vp=map(transport,[y,U,V])
    vp,wp=mv(A,v),mv(A,w)
    check('affine_full_K95_metric_covariance',metric(yp,vp,Up,wp,Vp)==metric(y,v,U,w,V))
    check('tautological_horizontal_covariance',dot(vp,mv(yp,wp))==dot(v,mv(y,w)))
    check('hold_fibre_metric_wrong_mutation',dot(vp,mv(y,wp))!=dot(v,mv(y,w)))
    check('vertical_trace_covariance',tr(mm(inverse(yp),Up))==tr(mm(inverse(y),U)))
    check('vertical_product_covariance',tr(mm(mm(inverse(yp),Up),mm(inverse(yp),Vp)))==tr(mm(mm(inverse(y),U),mm(inverse(y),V))))
    z=[Q(0)]*4
    check('trace_reversal_actual_value',metric(y,z,y,z,y)==-4)

    # Actual complex isotropy tangent weights: V11+V22+V00.
    weights=[(a,b) for a in (-1,1) for b in (-1,1)]
    weights += [(a,b) for a in (-2,0,2) for b in (-2,0,2)]
    weights += [(0,0)]
    char={(0,0,0):1}
    for a,b in weights:
        nxt=defaultdict(int)
        for (p,x,zv),c in char.items():
            nxt[(p,x,zv)]+=c;nxt[(1-p,x+a,zv+b)]+=c
        char=dict(nxt)
    multiplicities={}
    for p in (0,1):
        c={(a,b):v for (par,a,b),v in char.items() if par==p}
        check(f'parity{p}_dimension',sum(c.values())==8192)
        mult={}
        for a in range(9):
            for b in range(9):
                m=c.get((a,b),0)-c.get((a+2,b),0)-c.get((a,b+2),0)+c.get((a+2,b+2),0)
                check(f'parity{p}_nonnegative_mult_{a}_{b}',m>=0)
                if m:mult[(a,b)]=m
        reconstructed=defaultdict(int)
        for (a,b),m in mult.items():
            for x in range(-a,a+1,2):
                for zz in range(-b,b+1,2):reconstructed[(x,zz)]+=m
        check(f'parity{p}_full_character_reconstruction',dict(reconstructed)==c)
        check(f'parity{p}_irrep_dimension_sum',sum(m*(a+1)*(b+1) for (a,b),m in mult.items())==8192)
        check(f'parity{p}_trivial_mult',mult[(0,0)]==16)
        check(f'parity{p}_vector_mult',mult[(1,1)]==40)
        check(f'parity{p}_traceless_mult',mult[(2,2)]==52)
        multiplicities[p]=sum(mult[w] for w in [(0,0),(1,1),(2,2)])
    check('full_invariant_real_dimension216',sum(multiplicities.values())==216)
    check('both_invariant_parities108',multiplicities=={0:108,1:108})

    # Nontrivial graded toy recursion, exact l-infinity bounds s=3,k=2,n=4.
    def K(a):return (2*a[1],2*a[0])
    def N(a,b):return (a[0]*b[1]+a[1]*b[0],a[0]*b[0]+3*a[1]*b[1])
    def norm(a):return max(map(abs,a))
    S=(Q(0),Q(3));T={1:scale(-1,S)};major={1:Q(3)}
    for j in range(2,13):
        nonlinear=(Q(0),Q(0))
        for i in range(1,j-1):nonlinear=plus(nonlinear,N(T[i],T[j-1-i]))
        T[j]=scale(-1,plus(K(T[j-1]),nonlinear))
        major[j]=2*major[j-1]+4*sum(major[i]*major[j-1-i] for i in range(1,j-1))
    for j in range(1,13):
        check(f'coefficient{j}_majorant',norm(T[j])<=major[j])
        check(f'coefficient{j}_parity',T[j][1-j%2]==0)
    check('even_component_required',T[2]!=(0,0))
    check('omit_even_coefficient_Euler_mutation',K(T[1])!=(0,0))
    rho=Q(1,12);radius=Q(1,2)
    check('explicit_toy_majorant_ball_invariant',rho*(3+2*radius+4*radius**2)<=radius)
    check('explicit_toy_majorant_ball_contraction',rho*(2+8*radius)<1)
    check('explicit_toy_discriminant_positive',(1-2*rho)**2-4*4*3*rho**2>0)
    check('majorant_partial_sum_bounded',sum(major[j]*rho**j for j in major)<radius)
    return {'checks':checks,'count':len(checks),'invariant_dimension':216,
            'parity_dimensions':multiplicities,
            'scope':'exact affine/character/toy controls; no native numerical radius or physical solution certificate'}




"""Exact local-jet controls; root executes, no native proof implied by sampling."""
from fractions import Fraction as Q


def base_metric_controls():
    n=4
    g=[[Q(0) for _ in range(n)] for _ in range(n)]
    for i,v in enumerate((3,2,5,-7)): g[i][i]=Q(v)
    # Arbitrary symmetric first jets; this is not restricted to flat g jets.
    dg=[[[Q((mu+2)*(i+j+1)+(i-j)**2-5,mu+3)
          for j in range(n)] for i in range(n)] for mu in range(n)]
    checks={}
    def check(name,p):
        checks[name]=bool(p)
        assert p,name
    def christoffel(metric,jets):
        # Diagonal point metric; first jets may be fully non-diagonal.
        return [[[sum((Q(1)/metric[a][a] if c==a else Q(0))*
                       (jets[mu][c][b]+jets[b][c][mu]-jets[c][mu][b])/2
                       for c in range(n)) for b in range(n)]
                 for a in range(n)] for mu in range(n)]
    gamma=christoffel(g,dg)
    for c in (Q(2),Q(3,5),Q(9,4)):
        cg=[[c*v for v in row] for row in g]
        cdg=[[[c*v for v in row] for row in m] for m in dg]
        check('constant_scale_connection_'+str(c),christoffel(cg,cdg)==gamma)
    for mu in range(n):
        for i in range(n):
            for j in range(n):
                C=sum(gamma[mu][a][i]*g[a][j]+g[i][a]*gamma[mu][a][j]
                      for a in range(n))
                check(f'metric_compatibility_{mu}_{i}_{j}',C==dg[mu][i][j])
    # A variable scale has additional dc*g first-jet terms and changes Gamma.
    dc=(Q(1),Q(0),Q(0),Q(0))
    variable=[[[dg[mu][i][j]+dc[mu]*g[i][j] for j in range(n)]
               for i in range(n)] for mu in range(n)]
    check('not_local_Weyl_connection_invariance',christoffel(g,variable)!=gamma)
    # Symbolic-bound numerical control, not a computed native radius.
    m,C1,C2=Q(2),Q(3),Q(5)
    delta=min(Q(1),m/(2*(C1+C2)))
    error=C1*delta+C2*delta**2
    check('abstract_C1_radius_bound',error<=m/2 and m-error>0)
    return {'checks':checks,'count':len(checks),'all_passed':all(checks.values()),
            'scope':'finite rational jet controls; analytic existence proof is separate'}




"""Exact native128 leading connection/fermion response; root executes."""
from fractions import Fraction as Q
import json

def fermion_controls():
    n,size=14,128
    eta=[1]*9+[-1]*5
    H=(0,1,2,9); trace_axis=10
    weights=[Q(21,4) if a in H or a==trace_axis else Q(15,4) for a in range(n)]
    zero=[(Q(0),Q(0))]*size
    checks={}
    def check(k,v):
        checks[k]=bool(v)
        assert checks[k],k
    def add(a,b): return [(x[0]+y[0],x[1]+y[1]) for x,y in zip(a,b)]
    def scale(q,a): return [(q*x,q*y) for x,y in a]
    def phase(p,a): return [a,(-a[1],a[0]),(-a[0],-a[1]),(a[1],-a[0])][p%4]
    def vsum(vs):
        r=zero
        for v in vs:r=add(r,v)
        return r
    def gamma(j,v):
        bit,yy=6-j//2,j%2
        out=[]
        for r in range(size):
            p=2*((r>>(bit+1)).bit_count()%2)
            if yy:p+=1 if (r>>bit)&1 else 3
            if j>=9:p+=1
            out.append(phase(p,v[r^(1<<bit)]))
        return out
    def T(a,v):return scale(weights[a],gamma(a,v))
    def tr(z,axes=tuple(range(n))):return vsum(scale(eta[a],gamma(a,z[a])) for a in axes)
    def tr_t(z):return vsum(scale(eta[a],T(a,z[a])) for a in range(n))
    def direct(z,nu):
        r=[add(vsum(scale(eta[b],gamma(b,add(T(b,z[a]),scale(-1,T(a,z[b]))))) for b in range(n)),T(a,nu)) for a in range(n)]
        t=add(tr_t(z),scale(Q(-1,2),vsum(scale(eta[a],gamma(a,T(a,nu))) for a in range(n))))
        return r,t
    psi=[(Q(j%7-3),Q(j%5-2)) for j in range(size)]
    check('native_K95_Clifford_squares',all(gamma(a,gamma(a,psi))==scale(eta[a],psi) for a in range(n)))
    check('native_weighted_slash_60',vsum(scale(eta[a],gamma(a,T(a,psi))) for a in range(n))==scale(60,psi))
    z=[[(Q(((a+1)*(j+2))%11-5),Q((a+j)%7-3)) for j in range(size)] for a in range(n)]
    r,t=direct(z,psi)
    tau=add(tr(z),psi)
    expected=[add(scale(60-2*weights[a],z[a]),T(a,tau)) for a in range(n)]
    check('full_connection_derivative_oneform',r==expected)
    check('full_connection_derivative_scalar',t==add(tr_t(z),scale(-30,psi)))
    imp=[scale(10 if a in H else -4,gamma(a,psi)) for a in range(n)]
    check('owned_I_gamma_kernel',tr(imp)==zero)
    check('weighted_I_trace_54',tr_t(imp)==scale(54,psi))
    r,t=direct(imp,zero)
    check('I_diagnostic_495',scale(Q(1,4),tr(r,H))==scale(495,psi))
    check('I_diagnostic_54',t==scale(54,psi))
    zzero=[zero for _ in range(n)]
    r,t=direct(zzero,psi)
    check('nu_diagnostic_21_over4',scale(Q(1,4),tr(r,H))==scale(Q(21,4),psi))
    check('nu_diagnostic_minus30',t==scale(-30,psi))
    check('fingerprint_determinant',495*Q(-30)-Q(21,4)*54==Q(-30267,2))
    r,t=direct(imp,scale(20,psi))
    check('prior_central_kernel_trace_detected',scale(Q(1,4),tr(r,H))==scale(600,psi))
    check('prior_central_kernel_scalar_detected',t==scale(-546,psi))
    # F^-1(0,eta)=(-J eta/2,-6eta), then apply actual equation-row R.
    z=[scale(Q(-1,2),gamma(a,psi)) for a in range(n)]
    r,t=direct(z,scale(-6,psi))
    v=add(t,scale(Q(-1,2),tr(r)))
    u=[add(r[a],scale(Q(1,2),gamma(a,v))) for a in range(n)]
    check('primed_scalar_response_720',v==scale(720,psi))
    check('primed_scalar_to_oneform_formula',u==[scale(330-12*weights[a],gamma(a,psi)) for a in range(n)])
    check('not_scalar_mass_shift',all(row!=zero for row in u))
    check('horizontal_trace_coefficient_267',330-12*weights[0]==267 and 330-12*weights[10]==267)
    check('normal_traceless_coefficient_285',330-12*weights[4]==285 and 330-12*weights[11]==285)
    return {'checks':checks,'count':len(checks),'all_passed':all(checks.values()),'scope':'native pointwise leading operator response, not physical mass or family count'}



def run_checks():
    results={'homogeneous':homogeneous_controls(),'base_metric':base_metric_controls(),'fermion_response':fermion_controls()}
    # A restricted receiver can vanish while an omitted receiver remains: F=(t+h,t*t).
    h=Q(1,7);t=-h
    assert t+h==0 and t*t!=0
    results['scope_mutations']={'checks':{'restricted_receiver_is_not_full_residual':True},'count':1}
    return {'results':results,'count':sum(v['count'] for v in results.values()),'all_passed':True}

if __name__=='__main__':
    print(json.dumps(run_checks(),indent=2,sort_keys=True))
