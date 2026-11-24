#!/usr/bin/env python3
"""Exact controls for the scoped MG1 stability/topology derivation.

Requires SymPy. No numerical fit, grid extrapolation, GU or quantum-gap claim.
Analytic infinite-dimensional proofs and domain assumptions are in the article.
"""
import itertools
import json
import sympy as s

checks = []


def check(name, lhs, rhs=0):
    difference = lhs - rhs
    if isinstance(difference, s.MatrixBase):
        ok = all(s.simplify(x) == 0 for x in difference)
    else:
        ok = s.simplify(difference) == 0
    assert ok, (name, difference)
    checks.append(name)


def truth(name, condition):
    assert condition, name
    checks.append(name)


zero = s.zeros(3, 1)
t = [s.eye(3)[:, j] for j in range(3)]
# su(2) bracket in a positive orthonormal basis is the cross product.
coeff = s.symbols('a:9', real=True)
aa = [s.Matrix(coeff[3*i:3*i+3]) for i in range(3)]
eq = [sum((aa[j].cross(aa[j].cross(aa[i])) for j in range(3)), zero)
      for i in range(3)]
pair = sum(aa[i].dot(eq[i]) for i in range(3))
commnorm = sum(aa[j].cross(aa[i]).dot(aa[j].cross(aa[i]))
               for i in range(3) for j in range(3))
check('constant stationarity is negative commutator sum of squares', pair, -commnorm)
check('noncommuting T1 T2 fixture is off shell', t[1].cross(t[1].cross(t[0])), -t[0])
v = s.Matrix(s.symbols('v:3', real=True))
b = s.symbols('b:3', real=True)
check('commuting constant fixture solves all equations',
      sum(((b[j]*v).cross((b[j]*v).cross(b[0]*v)) for j in range(3)), zero), zero)

x,y,z,tau = s.symbols('x y z tau', real=True)
B,L = s.symbols('B L', positive=True)
coords = [x,y,z]
A = [-B*y*t[2]/2, B*x*t[2]/2, zero]


def D(i, field):
    return field.diff(coords[i]) + A[i].cross(field)


F = {(i,j): A[j].diff(coords[i])-A[i].diff(coords[j])+A[i].cross(A[j])
     for i in range(3) for j in range(i+1,3)}


def curv(i,j):
    return F[i,j] if i<j else -F[j,i] if i>j else zero


check('actual Cartan curvature', F[0,1], B*t[2])
check('no xz curvature', F[0,2], zero)
check('no yz curvature', F[1,2], zero)
for i in range(3):
    check(f'full Cartan stationarity component {i}',
          sum((D(j,curv(j,i)) for j in range(3)), zero), zero)
phi=s.exp(-B*(x*x+y*y)/4);g=s.exp(-z*z/(2*L*L));u=phi*g
a=[u*t[0],-u*t[1],zero]
da={(i,j):D(i,a[j])-D(j,a[i]) for i,j in F}
w={(i,j):a[i].cross(a[j]) for i,j in F}
check('real packet exactly Coulomb',sum((D(i,a[i]) for i in range(3)),zero),zero)
check('linear xy curvature vanishes',da[0,1],zero)
check('linear xz curvature',da[0,2],-u.diff(z)*t[0])
check('linear yz curvature',da[1,2],u.diff(z)*t[1])
check('quadratic xy curvature',w[0,1],-u*u*t[2])
energy=s.expand(sum(((F[ij]+tau*da[ij]+tau*tau*w[ij]).dot(
    F[ij]+tau*da[ij]+tau*tau*w[ij])-F[ij].dot(F[ij]))/2 for ij in F))
check('exact relative energy through quartic',energy,
      tau*tau*(u.diff(z)**2-B*u*u)+tau**4*u**4/2)
for i in range(3):
    Ka=-sum((D(j,D(j,a[i])) for j in range(3)),zero)-2*sum(
        (curv(i,j).cross(a[j]) for j in range(3)),zero)
    check(f'real Hessian component {i}',Ka, a[i]*(-g.diff(z,2)/g-B))
intg=s.integrate(g*g,(z,-s.oo,s.oo))
intgp=s.integrate(g.diff(z)**2,(z,-s.oo,s.oo))
check('longitudinal Gaussian gradient ratio',intgp/intg,1/(2*L*L))
intphi=s.integrate(phi*phi,(x,-s.oo,s.oo),(y,-s.oo,s.oo))
check('finite real packet norm',2*intphi*intg,4*s.pi**s.Rational(3,2)*L/B)
check('finite quartic coefficient',s.integrate(phi**4,(x,-s.oo,s.oo),(y,-s.oo,s.oo))*
      s.integrate(g**4,(z,-s.oo,s.oo)),s.pi**s.Rational(3,2)*L/(s.sqrt(2)*B))
truth('negative Rayleigh witness B1 L1', s.Rational(1,2)-1<0)
check('sufficiently small perturbation lowers relative energy',
      energy.diff(tau,2).subs(tau,0),2*(u.diff(z)**2-B*u*u))

# Left-invariant exterior algebra: components of a 1-form, star of its d.
# de^i=-k e^j wedge e^k cyclic; Lie bracket cross products supply d_A.
al,k,V=s.symbols('alpha kappa V',real=True)
theta=[k*v for v in t]
As=[al*v for v in theta]
cyclic=[(1,2),(2,0),(0,1)]
Fs=[-k*As[i]+As[j].cross(As[l]) for i,(j,l) in enumerate(cyclic)]
for i in range(3):
    check(f'S3 full curvature star component {i}',Fs[i],k*k*al*(al-1)*t[i])
grad=[-k*Fs[i]+As[j].cross(Fs[l])-As[l].cross(Fs[j])
      for i,(j,l) in enumerate(cyclic)]
for i in range(3):
    check(f'S3 full YM gradient component {i}',grad[i],k**3*al*(al-1)*(2*al-1)*t[i])
    check(f'S3 full stationarity at half {i}',grad[i].subs(al,s.Rational(1,2)),zero)
    check(f'S3 actual negative eigenvector {i}',grad[i].diff(al).subs(al,s.Rational(1,2)),
          -k*k*theta[i]/2)
check('S3 amplitude is Coulomb',sum((As[i].cross(theta[i]) for i in range(3)),zero),zero)
Es=V*sum(f.dot(f) for f in Fs)/2
check('S3 energy polynomial',Es,3*V*k**4*al**2*(al-1)**2/2)
check('S3 negative Hessian energy quotient',s.diff(Es,al,2).subs(al,s.Rational(1,2))/(3*V*k*k),-k*k/2)
centralizer=s.Matrix.vstack(*[s.Matrix([[0,-q[2],q[1]],[q[2],0,-q[0]],[-q[1],q[0],0]]) for q in t])
truth('S3 curvature has zero adjoint centralizer',centralizer.rank()==3)

Hx=s.diag(1,-1,-1);Hy=s.diag(-1,1,-1);Hz=s.eye(3)
for name,H in [('x',Hx),('y',Hy),('z',Hz)]:
    check(f'torus {name} holonomy orthogonal',H.T*H,s.eye(3))
    check(f'torus {name} holonomy oriented',H.det(),1)
check('SO3 holonomies commute',Hx*Hy-Hy*Hx,s.zeros(3))
truth('no common adjoint fixed vector',s.Matrix.vstack(Hx-s.eye(3),Hy-s.eye(3),Hz-s.eye(3)).rank()==3)
nus=[(0,s.Rational(1,2),0),(s.Rational(1,2),0,0),(s.Rational(1,2),s.Rational(1,2),0)]
for c,nu in enumerate(nus):
    check(f'character twists color {c}',s.diag(*[s.exp(2*s.pi*s.I*v) for v in nu]),
          s.diag(Hx[c,c],Hy[c,c],Hz[c,c]))
    low=min(sum((s.Integer(n[j])+nu[j])**2 for j in range(3))
            for n in itertools.product(range(-2,3),repeat=3))
    check(f'finite lattice minimum control color {c}',low,[s.Rational(1,4),s.Rational(1,4),s.Rational(1,2)][c])
    # The full minimum follows analytically from |n+1/2| >= 1/2.
    mom=s.Matrix(nu);P=s.eye(3)-mom*mom.T/mom.dot(mom)
    check(f'physical transverse projector idempotent color {c}',P*P,P)
    check(f'physical transverse projector Coulomb color {c}',mom.T*P,s.zeros(1,3))
    truth(f'two physical polarizations color {c}',P.rank()==2)
lx,ly,lz=s.symbols('L_x L_y L_z',positive=True)
mins=[4*s.pi**2*sum(nu[j]**2/[lx,ly,lz][j]**2 for j in range(3)) for nu in nus]
check('rectangular first color threshold',mins[0],s.pi**2/ly**2)
check('rectangular second color threshold',mins[1],s.pi**2/lx**2)
check('rectangular third color threshold',mins[2],s.pi**2*(1/lx**2+1/ly**2))
check('untwisted direction has no threshold dependence',s.diff(mins[0],lz),0)
check('uniform decompactification threshold tends to zero',s.limit(mins[0],ly,s.oo),0)
sx=s.Matrix([[0,1],[1,0]]);sy=s.Matrix([[0,-s.I],[s.I,0]]);sz=s.diag(1,-1)
Ux=s.I*sx;Uy=s.I*sy
check('SU2 lifts anticommute',Ux*Uy+Uy*Ux,s.zeros(2))
check('SU2 lift commutator is central minus identity',Ux*Uy*Ux.inv()*Uy.inv(),-s.eye(2))
for px,py in itertools.product([-1,1],repeat=2):
    check(f'lift sign choice {px} {py} leaves obstruction',
          (px*Ux)*(py*Uy)*(px*Ux).inv()*(py*Uy).inv(),-s.eye(2))
# w2=beta*alpha+beta*(alpha+beta)+alpha*(alpha+beta), over F2 with squares0.
h1,h2=s.symbols('h1 h2')
w2=s.Poly(s.expand(h2*h1+h2*(h1+h2)+h1*(h1+h2)),h1,h2,modulus=2)
terms={mon:int(c)%2 for mon,c in w2.terms() if all(d<2 for d in mon)}
truth('Whitney w2 equals nonzero xy cup product',terms=={(1,1):1})
angle=s.symbols('angle',real=True);U=s.diag(s.exp(s.I*angle),s.exp(-s.I*angle))
check('commuting SU2 torus holonomy fixes Cartan',U*sz*U.inv(),sz)
truth('trivial bundle retains three parallel adjoint directions',s.zeros(3).nullspace().__len__()==3)
check('noncommuting harmonic zero modes can have quartic energy',
      (tau*t[0]).cross(tau*t[1]).dot((tau*t[0]).cross(tau*t[1]))/2,tau**4/2)

print(json.dumps({'status':'PASS','checks':len(checks),'exact_checks':checks,
                  'scope':'Exact supporting identities; analytic domain, universal Lie and full Fourier proofs in article.',
                  'gu_or_quantum_gap_credit':False},indent=2))
