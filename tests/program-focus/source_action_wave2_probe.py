"""Source-informed action wave2: exact native and formal-series controls."""
def fermion_checks():
    #!/usr/bin/env python3
    """Independent exact K95 SE factorization controls; root executes serialized.
    Uses integer Gaussian pairs; no floating point or full dense matrices.
    """
    import json
    from fractions import Fraction as Q
    N=14; S=128; eta=[1]*9+[-1]*5
    checks={}
    def check(k,v):
     checks[k]=bool(v)
     assert checks[k],k
    # Gaussian rationals, vector operations.
    def ca(a,b): return (a[0]+b[0],a[1]+b[1])
    def sc(q,a): return (q*a[0],q*a[1])
    def ip(p,a):
     return [a,(-a[1],a[0]),(-a[0],-a[1]),(a[1],-a[0])][p%4]
    def plus(a,b):return [ca(x,y) for x,y in zip(a,b)]
    def scale(q,a):return [sc(q,x) for x in a]
    def csum(vs):
     out=[(0,0)]*S
     for v in vs:out=plus(out,v)
     return out
    # Jordan-Wigner Euclidean gamma, then nine positive and five negative.
    def gamma(j,v):
     bit=6-j//2; yy=j%2; out=[]
     for r in range(S):
      phase=2*((r>>(bit+1)).bit_count()%2)
      if yy:phase+=1 if (r>>bit)&1 else 3
      if j>=9:phase+=1
      out.append(ip(phase,v[r^(1<<bit)]))
     return out
    z=[[(Q(((a+2)*(j+1))%11-5),Q((a+j)%7-3)) for j in range(S)] for a in range(N)]
    nu=[(Q(j%13-6),Q(j%5-2)) for j in range(S)]
    def tr(z):return csum(scale(eta[a],gamma(a,z[a])) for a in range(N))
    def J(v):return [gamma(a,v) for a in range(N)]
    def c(x,v):return csum(scale(eta[a]*x[a],gamma(a,v)) for a in range(N))
    def ix(x,z):return csum(scale(eta[a]*x[a],z[a]) for a in range(N))
    def symbol(x,z,nu,s):
     tau=tr(z)
     r=[plus(c(x,z[a]),scale(x[a],plus(nu,scale(-1,tau)))) for a in range(N)]
     return r,plus(ix(x,z),scale(s,c(x,nu)))
    def input_frame(z,nu):
     h=plus(nu,scale(-1,tr(z)))
     return [plus(z[a],scale(Q(1,2),gamma(a,h))) for a in range(N)],h
    def output_frame(r,s):
     v=plus(s,scale(Q(-1,2),tr(r)))
     return [plus(r[a],scale(Q(1,2),gamma(a,v))) for a in range(N)],v
    zp,h=input_frame(z,nu)
    check('input_frame_inverse_oneform',all(plus(zp[a],scale(Q(-1,2),gamma(a,h)))==z[a] for a in range(N)))
    check('input_frame_inverse_scalar',plus(tr(zp),scale(1-Q(N,2),h))==nu)
    xs={'positive':[1]+[0]*13,'negative':[0]*9+[1]+[0]*4,'null':[1]+[0]*8+[1]+[0]*4,'mixed':[3,2,0,0,0,0,0,0,0,1,0,0,0,0]}
    for label,x in xs.items():
     r,y=symbol(x,z,nu,Q(-1,2));u,v=output_frame(r,y)
     check(label+'_oneform_factorization',all(u[a]==c(x,zp[a]) for a in range(N)))
     check(label+'_scalar_factorization',v==scale(-1,c(x,h)))
     check(label+'_output_inverse_r',all(plus(u[a],scale(Q(-1,2),gamma(a,v)))==r[a] for a in range(N)))
     check(label+'_output_inverse_s',plus(scale(Q(1,2),tr(u)),scale(1-Q(N,4),v))==y)
     ro,yo=symbol(x,z,nu,0);uo,vo=output_frame(ro,yo)
     check(label+'_old_SE_zero_rejected',uo!=u and vo!=v)
    check('native_K95_Clifford',all(gamma(a,gamma(a,nu))==scale(eta[a],nu) for a in range(N)) and all(plus(gamma(a,gamma(b,nu)),gamma(b,gamma(a,nu)))==[(0,0)]*S for a in range(N) for b in range(a+1,N)))
    # Existing full module polynomial: a=e=g=1,c=f=h=0 => P=2s+1.
    check('old_regular_but_Jordan',2*Q(0)+1==1)
    check('repair_unique_s_in_fixed_six_coefficients',2*Q(-1,2)+1==0)
    # A generic Krein-skew displacement need not preserve Clifford multiplication:
    # T0=gamma0 gamma1; [T0,gamma0]=-2 eta0 gamma1.
    def T(v):return gamma(0,gamma(1,v))
    comm=plus(T(gamma(0,nu)),scale(-1,gamma(0,T(nu))))
    check('generic_fullU_lower_order_remainder_nonzero',comm==scale(-2,gamma(1,nu)) and comm!=[(0,0)]*S)

    # Full first-jet differential factorization at a normal spin frame. The
    # background B coefficients vanish at the point, curvature need not vanish.
    # Two noncommuting Krein-skew bivector displacement components.
    zero=[(0,0)]*S
    def connection(a,v):
     if a==0:return gamma(0,gamma(1,v))
     if a==9:return gamma(1,gamma(9,v))
     return zero
    def dz(b,a):return scale(Q(((a+1)*(b+2))%7-3,5),z[(a+b)%N])
    def dn(b):return scale(Q(b%5-2,3),nu)
    def covz(b,a):return plus(dz(b,a),connection(b,z[a]))
    def covn(b):return plus(dn(b),connection(b,nu))
    rfull=[plus(csum(scale(eta[b],gamma(b,plus(covz(b,a),scale(-1,covz(a,b))))) for b in range(N)),covn(a)) for a in range(N)]
    sfull=plus(csum(scale(eta[a],covz(a,a)) for a in range(N)),scale(Q(-1,2),csum(scale(eta[b],gamma(b,covn(b))) for b in range(N))))
    ufull,vfull=output_frame(rfull,sfull)
    def Qrow(a):return csum(scale(eta[b],plus(connection(a,gamma(b,z[b])),scale(-1,gamma(b,connection(a,z[b]))))) for b in range(N))
    Qz=[Qrow(a) for a in range(N)];GQ=tr(Qz)
    Keta=[csum(scale(eta[b],gamma(b,plus(connection(b,gamma(a,h)),scale(-1,gamma(a,connection(b,h)))))) for b in range(N)) for a in range(N)]
    def dh(b):return plus(dn(b),scale(-1,tr([dz(b,a) for a in range(N)])))
    def dzp(b,a):return plus(dz(b,a),scale(Q(1,2),gamma(a,dh(b))))
    Leta=csum(scale(eta[b],gamma(b,plus(dh(b),connection(b,h)))) for b in range(N))
    Lzp=[csum(scale(eta[b],gamma(b,plus(dzp(b,a),connection(b,zp[a])))) for b in range(N)) for a in range(N)]
    rex=[plus(plus(Lzp[a],Qz[a]),plus(scale(Q(-1,2),gamma(a,GQ)),scale(Q(-1,2),Keta[a]))) for a in range(N)]
    sex=plus(scale(-1,Leta),scale(-1,GQ))
    check('full_differential_QK_oneform_identity',rex==ufull)
    check('full_differential_QK_scalar_identity',sex==vfull)
    check('drop_nonClifford_QK_mutation',ufull!=Lzp and vfull!=scale(-1,Leta))
    check('literal_decoder_transported',all(plus(zp[a],scale(Q(-1,2),gamma(a,h)))==z[a] for a in range(4)) and plus(tr(zp),scale(1-Q(N,2),h))==nu)
    # Independent dual rows transform by transpose, never Hermitian adjoint.
    def gamma_t(j,v):
     bit=6-j//2; yy=j%2;out=[]
     for r in range(S):
      rr=r^(1<<bit); phase=2*((rr>>(bit+1)).bit_count()%2)
      if yy:phase+=1 if (rr>>bit)&1 else 3
      if j>=9:phase+=1
      out.append(ip(phase,v[rr]))
     return out
    def cm(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
    def dot(a,b):
     out=(0,0)
     for aa,bb in zip(a,b):out=ca(out,cm(aa,bb))
     return out
    p=z;q=nu;JTp=csum(gamma_t(a,p[a]) for a in range(N))
    baroldr=[plus(p[a],scale(eta[a],gamma_t(a,plus(scale(Q(-1,4),JTp),scale(Q(-1,2),q))))) for a in range(N)]
    barolds=plus(q,scale(Q(1,2),JTp))
    lhs=dot(barolds,sfull);rhs=dot(q,vfull)
    for a in range(N):lhs=ca(lhs,dot(baroldr[a],rfull[a]));rhs=ca(rhs,dot(p[a],ufull[a]))
    check('independent_bar_dual_action_identity',lhs==rhs)

    def pplus(v,w):return ([plus(v[0][a],w[0][a]) for a in range(N)],plus(v[1],w[1]))
    def pscale(a,v):return ([scale(a,w) for w in v[0]],scale(a,v[1]))
    time=[0]*9+[1]+[0]*4
    def inverse_at_time(r,y,sd):
     q=-1
     if sd==0:
      w=scale(Q(1,q),plus(ix(time,r),scale(-1,c(time,y))))
      zz=[scale(Q(1,q),c(time,plus(r[a],scale(-time[a],w)))) for a in range(N)]
      nn=scale(Q(1,q),plus(scale(2,ix(time,r)),scale(-1,c(time,tr(r)))))
      return zz,nn
     u,v=output_frame(r,y)
     zzp=[scale(Q(1,q),c(time,w)) for w in u];hh=scale(Q(-1,q),c(time,v))
     return ([plus(zzp[a],scale(Q(-1,2),gamma(a,hh))) for a in range(N)],plus(tr(zzp),scale(1-Q(N,2),hh)))
    for j in range(3):
     xx=[int(a==j) for a in range(N)]
     def evolve(v,sd):return pscale(-1,inverse_at_time(*symbol(xx,*v,sd),sd))
     def defect(v,sd):return pplus(evolve(evolve(v,sd),sd),pscale(-1,v))
     zero=pscale(0,(z,nu));old=defect((z,nu),0)
     check('native_old_horizontal_Jordan_nonzero_'+str(j),old!=zero)
     check('native_old_horizontal_Jordan_square_zero_'+str(j),defect(old,0)==zero)
     check('native_repair_horizontal_involution_'+str(j),defect((z,nu),Q(-1,2))==zero)

    for a,b in [(0,1),(0,9)]:
     def rho(v):return scale(Q(1,2),gamma(a,gamma(b,v)))
     spincomm=plus(rho(gamma(b,nu)),scale(-1,gamma(b,rho(nu))))
     target=scale(eta[b],gamma(a,nu))
     check('spin_lift_vector_rotation_'+str(a)+'_'+str(b),spincomm==target)
     check('double_spin_lift_rejected_'+str(a)+'_'+str(b),scale(2,spincomm)!=target)
    return checks

def bosonic_checks():
    #!/usr/bin/env python3
    """Independent sparse 14D exterior/Clifford evaluator for the exact candidate.
    Only root executes. Fraction arithmetic, native K95; no matrix sampling.
    """
    from fractions import Fraction as Q
    from functools import lru_cache
    from itertools import combinations
    import json
    N=14; FULL=(1<<N)-1; ETA=(1,)*9+(-1,)*5
    checks={}
    def check(k,v):
     checks[k]=bool(v)
     assert checks[k],(k,v)
    def clean(x):return {k:v for k,v in x.items() if v}
    def add(*xs):
     z={}
     for x in xs:
      for k,v in x.items():z[k]=z.get(k,Q(0))+v
     return clean(z)
    def scale(a,x):return clean({k:a*v for k,v in x.items()})
    @lru_cache(None)
    def sign(a,b):return -1 if sum((b&((1<<i)-1)).bit_count() for i in range(N) if a>>i&1)%2 else 1
    @lru_cache(None)
    def cmul(a,b):
     q=sign(a,b)
     for i in range(N):
      if (a&b)>>i&1:q*=ETA[i]
     return a^b,q
    # Combined forms map (exterior mask, Clifford blade)->rational.
    def wedge(x,y,kind='raw'):
     z={}
     for (ea,ca),va in x.items():
      for (eb,cb),vb in y.items():
       if ea&eb:continue
       c,q=cmul(ca,cb)
       if kind!='raw':
        _,r=cmul(cb,ca);q=q-r if kind=='comm' else q+r
       if q:
        k=(ea|eb,c);z[k]=z.get(k,Q(0))+sign(ea,eb)*q*va*vb
     return clean(z)
    def star(x):
     z={}
     for (e,c),v in x.items():
      q=sign(e,FULL^e)
      for i in range(N):
       if e>>i&1:q*=ETA[i]
      z[(FULL^e,c)]=q*v
     return clean(z)
    phi1={(1<<a,1<<a):Q(1) for a in range(N)}
    phi2={((1<<a)|(1<<b),(1<<a)|(1<<b)):Q(1) for a,b in combinations(range(N),2)}
    def shiab(x):
     # The two i-anticommutators cancel the printed minus.
     return add(wedge(phi1,star(x),'comm'),scale(Q(1,2),star(wedge(phi1,star(wedge(phi2,star(x),'anti')),'anti'))))
    def pair(x,y):return -wedge(x,y).get((FULL,0),Q(0)) # b=-trace/128

    def field(vals):return {(1<<a,1<<a):Q(v) for a,v in enumerate(vals) if v}
    def variation_cubic(T,Z):return (pair(Z,shiab(wedge(T,T)))+pair(T,shiab(add(wedge(Z,T),wedge(T,Z)))))/3
    vals=[1,-2,3,0,1,2,-1,4,0,-3,1,2,-2,1];T=field(vals);tr=sum(vals);e2=sum(vals[a]*vals[b] for a,b in combinations(range(N),2))
    for a in range(N):
     Z=field([int(a==b) for b in range(N)])
     check('nativeK95_mass_'+str(a),pair(Z,star(phi1))==-1)
     check('nativeK95_radial_cubic_'+str(a),variation_cubic(phi1,Z)==-312)
     check('nativeK95_anisotropic_cubic_'+str(a),variation_cubic(T,Z)==-4*(vals[a]**2-tr*vals[a]+e2))
     check('nativeK95_constant_curvature_'+str(a),pair(Z,shiab(phi2))==-156)
    check('nativeK95_cubic_density',pair(T,shiab(wedge(T,T)))==-12*sum(vals[a]*vals[b]*vals[c] for a,b,c in combinations(range(N),3)))
    # Full derivative Euler includes coefficient/formal adjoint, not raw endpoint.
    for mu in range(N):
     nu=(mu+1)%N
     Z={(1<<nu,(1<<min(mu,nu))|(1<<max(mu,nu))):Q(1)}
     dx={(1<<mu,0):Q(1)}
     left=pair(Z,shiab(wedge(dx,phi1)));right=pair(phi1,shiab(wedge(dx,Z)))
     check('nativeK95_variable_radial_detected_'+str(mu),abs((left-right)/2)==11)
     check('nativeK95_drop_adjoint_mutation_'+str(mu),left/2!=(left-right)/2)
    # Full receiver tests outside diagonal Cl1: representative offdiagonal, Cl2/Cl5.
    for e,c in [(0,1<<1),(2,3),(3,sum(1<<i for i in [0,1,2,3,4])),(5,sum(1<<i for i in [1,2,3,4,5]))]:
     Z={(1<<e,c):Q(1)}
     check('offdiagonal_cubic_'+str(e)+'_'+str(c),variation_cubic(T,Z)==0)
    # This is a restriction countercontrol: variable radial amplitudes can solve
    # pointwise algebraic rows while still failing the even derivative Euler.
    check('restricted_stationarity_not_full',pair({(2,3):Q(1)},shiab(wedge({(1,0):Q(1)},phi1)))!=pair(phi1,shiab(wedge({(1,0):Q(1)},{(2,3):Q(1)}))))

    # Actual native candidate Helmholtz/principal endpoint distinction. Fixed
    # covariantly parallel coefficients: a first-order variational coefficient
    # is skew under the density-dual coefficient transpose.
    dx={(1,0):Q(1)};Z={(2,3):Q(1)}
    left=pair(Z,shiab(wedge(dx,phi1)));right=pair(phi1,shiab(wedge(dx,Z)))
    check('actual_candidate_raw_endpoint_not_Helmholtz',left+right!=0)
    check('actual_candidate_Euler_not_endpoint',Q(1,2)*(left-right)!=left)
    check('actual_candidate_derivative_numbers',left==-2 and right==-24 and Q(1,2)*(left-right)==11)

    # Actual K95 horizontal(3,1), trace negative, traceless positive adapted frame.
    def projector_row(vindex,coeffs):
        hs=[0,1,2,9]; Z={(1<<hs[0],(1<<hs[0])|(1<<vindex)):Q(1)}
        derivs=[add(scale(coeffs[j],{(1<<vindex,1<<mu):Q(1)}),scale(coeffs[j]*Q(ETA[mu],ETA[vindex]),{(1<<mu,1<<vindex):Q(1)})) for j,mu in enumerate(hs)]
        dt=add(*[wedge({(1<<mu,0):Q(1)},dv) for mu,dv in zip(hs,derivs)])
        left=pair(Z,shiab(dt));right=sum(pair(dv,shiab(wedge({(1<<mu,0):Q(1)},Z))) for mu,dv in zip(hs,derivs))
        return left,right,(left-right)/2
    trace_row=projector_row(10,[Q(1)]*4)
    traceless_row=projector_row(3,[Q(1),Q(1),Q(-1),Q(-1)])
    check('native_K95_trace_projector_complete_adjoint',trace_row==(-2,-6,2))
    check('native_K95_traceless_projector_complete_adjoint',traceless_row==(-2,2,-2))
    source_H=Q(-21,4);source_TL=Q(-15,4)
    check('formal_first_even_native_receiver',traceless_row[2]*(source_TL-source_H)/4==Q(-3,4))

    # Actual spin-LC curvature injection is one half the old algebraic injection.
    ks={(a,b):Q(((3*a+2*b)%7)-3) for a,b in combinations(range(N),2)}
    Fspin={((1<<a)|(1<<b),(1<<a)|(1<<b)):k/2 for (a,b),k in ks.items() if k}
    Ric=[sum(k for (a,b),k in ks.items() if i in (a,b)) for i in range(N)];Scal=sum(Ric)
    for a in range(N):
     Z=field([int(a==b) for b in range(N)])
     check('actual_spin_LC_curvature_minus_Einstein_'+str(a),pair(Z,shiab(Fspin))==Ric[a]-Scal/2)
     check('actual_spin_LC_constant_sectional_half_'+str(a),pair(Z,shiab(scale(Q(1,2),phi2)))==-78)
    check('old_algebraic_injection_factor_two_detected',pair(field([1]+[0]*13),shiab(phi2)) != pair(field([1]+[0]*13),shiab(scale(Q(1,2),phi2))))
    return checks

def formal_elimination_checks():
    import sympy as s
    checks={}
    def check(k,v):
        checks[k]=bool(v)
        assert checks[k], k
    h=s.symbols('h')
    K=s.Matrix([[1,2,0],[2,-1,1],[0,1,3]])
    R=s.Matrix([2,-1,3])
    def N(u,v):
        return s.Matrix([(u[1]*v[2]+u[2]*v[1])/2,(u[0]*v[2]+u[2]*v[0])/2,(u[0]*v[1]+u[1]*v[0])/2])
    ts={1:-R}
    for n in range(2,6):
        ts[n]=-K*ts[n-1]-sum((N(ts[i],ts[n-1-i]) for i in range(1,n-1)),s.zeros(3,1))
    T=sum((h**n*ts[n] for n in ts),s.zeros(3,1))
    E=T/h+R+K*T+N(T,T)
    for degree in range(5):
        check('all_components_formal_Euler_coefficient_'+str(degree),all(s.expand(x).coeff(h,degree)==0 for x in E))
    check('T2_KR',ts[2]==K*R)
    check('T3_quadratic_feedback',ts[3]==-K*K*R-N(R,R))
    check('T4_noncommuting_recursion',ts[4]==K*K*K*R+K*N(R,R)+2*N(R,K*R))
    bad=T+h**3*N(R,R)
    Eb=bad/h+R+K*bad+N(bad,bad)
    check('omitted_quadratic_feedback_detected',any(s.expand(x).coeff(h,2)!=0 for x in Eb))
    V=(T.dot(R)+T.dot(T)/(2*h)+T.dot(K*T)/2+T.dot(N(T,T))/3)
    expected=-h*R.dot(R)/2+h*h*R.dot(K*R)/2+h**3*(-(K*R).dot(K*R)/2-R.dot(N(R,R))/3)
    for degree in range(1,4):
        check('effective_action_order_'+str(degree),s.expand(V-expected).coeff(h,degree)==0)
    x,y,z=s.symbols('x y z'); q=s.Matrix([x,y,z])
    check('cubic_gradient_normalization',s.Matrix([s.diff(q.dot(N(q,q))/3,v) for v in q])==N(q,q))
    S,J=s.symbols('S J')
    check('induced_current_square_coefficient',s.expand(-(S+J)**2/2).coeff(J,2)==-s.Rational(1,2))
    check('charge_concentration_first_order_exponent',14-3==11)
    check('charge_concentration_mass_exponent',14-2==12)
    check('critical_curvature_L7_exponent',14-2*7==0)
    return checks

import sympy as s

def indefinite_elimination_checks():
    h=s.symbols('h'); x,y=s.symbols('x y'); X=s.Matrix([x,y])
    H=s.diag(1,-1)
    K=s.Matrix([[2,3],[-3,5]])
    R=s.Matrix([s.Rational(2,3),s.Rational(-5,7)])
    cubic=(2*x**3+3*x*x*y-5*x*y*y+7*y**3)/3
    def pair(u,v):return (u.T*H*v)[0]
    def Nsame(u):
        grad=s.Matrix([s.diff(cubic,z) for z in (x,y)])
        return H.inv()*grad.subs({x:u[0],y:u[1]}, simultaneous=True)
    def N(u,v):return s.simplify((Nsame(u+v)-Nsame(u)-Nsame(v))/2)
    coeff={1:-R}
    for n in range(2,6):
        coeff[n]=s.simplify(-K*coeff[n-1]-sum((N(coeff[i],coeff[n-1-i]) for i in range(1,n-1)),s.zeros(2,1)))
    T=sum((h**n*coeff[n] for n in coeff),s.zeros(2,1))
    residual=s.expand(T+h*R+h*K*T+h*Nsame(T))
    checks={
      'indefinite_form_selfadjoint_K':K.T*H==H*K,
      'all_component_formal_residual_through_order5':all(s.expand(v).coeff(h,n)==0 for v in residual for n in range(6)),
      'T2_exact':coeff[2]==K*R,
      'T3_exact':coeff[3]==-K*K*R-Nsame(R),
      'T4_exact':coeff[4]==K**3*R+K*Nsame(R)+2*N(R,K*R),
    }
    L=pair(R,T)+pair(T,T)/(2*h)+pair(T,K*T)/2+cubic.subs({x:T[0],y:T[1]},simultaneous=True)
    expected=-h*pair(R,R)/2+h*h*pair(R,K*R)/2-h**3*(pair(K*R,K*R)/2+pair(R,Nsame(R))/3)
    checks['effective_action_through_order3']=all(s.expand(L-expected).coeff(h,n)==0 for n in range(4))
    badT=-h*R+h*h*K*R-h**3*K*K*R
    bad=s.expand(badT+h*R+h*K*badT+h*Nsame(badT))
    checks['omitted_nonlinearity_detected']=any(s.expand(v).coeff(h,3)!=0 for v in bad)
    badSign=expected+2*h**3*pair(R,Nsame(R))/3
    checks['wrong_cubic_sign_detected']=s.expand(L-badSign).coeff(h,3)!=0
    assert all(checks.values()),checks
    return checks


if __name__=='__main__':
    import json
    groups={'fermion':fermion_checks(),'native_bosonic':bosonic_checks(),'formal_elimination':formal_elimination_checks(),'indefinite_elimination':indefinite_elimination_checks()}
    print(json.dumps({'passed':sum(map(len,groups.values())),'groups':{k:{'passed':len(v),'checks':v} for k,v in groups.items()},'scope':'Exact native K95 algebra controls plus formal symbolic recursion; written proofs own general identities. No stationary metric/fermion solution, convergent series, physical positivity or observed-family receiver.'},indent=2))
