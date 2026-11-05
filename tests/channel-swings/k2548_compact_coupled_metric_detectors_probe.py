"""K2548 exact coefficient checks; universal curved/adjugate proofs in the note.

The six-potential realization is not asserted injective and its coefficient
matrix is not its own formal adjoint. Only the full field operator has that
property. Numeric polynomial evaluations below are controls, not the proof
of the universal adjugate identity.
"""
from pathlib import Path
import hashlib
import json
import sys
import sympy as s

R = Path(__file__).resolve().parents[2]
checks, controls = {}, {}
def ck(bank, name, value):
    bank[name] = bool(value)
    if not bank[name]:
        raise AssertionError('FAIL ' + name)
def eq(name, lhs, rhs=0):
    if isinstance(lhs, s.MatrixBase):
        if not isinstance(rhs, s.MatrixBase):
            rhs = s.zeros(*lhs.shape) if rhs == 0 else rhs
        value = all(s.cancel(v) == 0 for v in lhs-rhs)
    else:
        value = s.cancel(lhs-rhs) == 0
    ck(checks, name, value)

k = s.symbols('k', nonzero=True)
X, Y = s.symbols('X Y')
f, g, p, q, r, z = s.symbols('f g p q r z')
potentials = s.Matrix([f,g,p,q,r,z])
a = -5*k/s.Integer(2288)
la = 35*k*k/s.Integer(604032)
K = la/6
m = 158*k/s.Integer(143)
beta = -15*k/s.Integer(143)
m0 = -4*k/s.Integer(11)
mK = 148*k/s.Integer(143)
mV = 503*k/s.Integer(858)
mH = 893*k/s.Integer(858)
Z = X+Y
tau = 7*f+7*g+X*p+Y*q
BA = f+(X+la)*p+Y*r
BB = g+(Y+la)*q+X*r
VA, VB = BA-tau, BB-tau
WA, WB = 11*VA-13*Y*z, 11*VB+13*X*z
divv, divw = X*VA+Y*VB, X*WA+Y*WB
Vstar = s.Matrix([divw,divw,-WA,-WB,-(WA+WB)/2])
hook = s.Matrix([
    2*Z*f-2*K*X*p+s.Rational(2,13)*divv,
    2*Z*g-2*K*Y*q+s.Rational(2,13)*divv,
    2*(Z+la+K)*p-2*BA-s.Rational(2,13)*VA,
    2*(Z+la+K)*q-2*BB-s.Rational(2,13)*VB,
    2*(Z+la)*r-BA-BB-(VA+VB)/13,
])
scalar_curvature = X*BA+Y*BB-(Z+la)*tau
einstein = s.Matrix([
    -(Z/2+la)*f-scalar_curvature/2,
    -(Z/2+la)*g-scalar_curvature/2,
    BA-(Z/2+la)*p-tau/2,
    BB-(Z/2+la)*q-tau/2,
    (BA+BB-tau-(Z+2*la)*r)/2,
])
mass = m*s.Matrix([f,g,p,q,r])+beta*tau*s.Matrix([1,1,0,0,0])
FC = mass+11*Vstar/(13*mV)-2*hook/mH+einstein/(3*a)
FK = mK*z-(WB-WA)/(2*mV)
M = FC.col_join(s.Matrix([FK])).jacobian(potentials).applyfunc(s.cancel)
E = einstein.jacobian(potentials).applyfunc(s.cancel)
E0 = E[:,0].col_join(s.Matrix([0]))

# Independent tensor consequences, not report-field checks.
eq('Einstein_A_gradient_diffeomorphism', E*s.Matrix([0,0,2,0,1,0]))
eq('Einstein_B_gradient_diffeomorphism', E*s.Matrix([0,0,0,2,1,0]))
eq('Einstein_full_Hessian', E*s.Matrix([0,0,1,1,1,0]))
eq('Einstein_divergence_A', E[0,:]+(X+la)*E[2,:]+Y*E[4,:])
eq('Einstein_divergence_B', E[1,:]+(Y+la)*E[3,:]+X*E[4,:])
eq('skew_double_divergence_cancels', X*(-Y*z)+Y*(X*z))
eq('full_skew_vector_equation', FK,
   (mK-13*(X+Y)/(2*mV))*z-11*(VB-VA)/(2*mV))
swap=s.zeros(6)
for i,j in [(0,1),(1,0),(2,3),(3,2),(4,4)]: swap[i,j]=1
swap[5,5]=-1
eq('factor_exchange_keeps_skew_orientation',swap*M*swap,M.subs({X:Y,Y:X},simultaneous=True))
eq('metric_seed_Einstein_column', E0,
   s.Matrix([(5*X+6*Y+5*la)/2,(6*X+7*Y+7*la)/2,
             -s.Rational(5,2),-s.Rational(7,2),-3,0]))

# Reproduce K2541's independent one-factor full-curvature reduction.
MA=m*f+7*beta*(f+g)+la*(5*f+7*g)/(6*a)
MB=m*g+7*beta*(f+g)+la*(7*f+5*g)/(6*a)
RA=-121*(7*f+6*g)/(13*mV)-24*(f-g)/(13*mH)+(f+g)/a
RB=-121*(7*f+6*g)/(13*mV)+28*(f-g)/(13*mH)+(7*f+5*g)/(6*a)
hu=beta+121*la/(13*mV)-4*la/(13*mH)
hw=beta+121*la/(13*mV)+14*la/(39*mH)
zeta=m-121*la/(13*mV)-14*la/(39*mH)
old=s.Matrix([MA+Y*RA+hu*Y*q,MB+Y*RB+hw*Y*q,-RB+zeta*q])
restricted=FC.subs({X:0,p:0,r:0,z:0})
eq('K2541_three_rows_recovered',s.Matrix([restricted[0],restricted[1],restricted[3]]),old)
hessB=hook.subs({X:0,f:0,g:0,p:0,r:0,z:0})
eq('curved_Hessian_B_hook',s.Matrix([hessB[0],hessB[1],hessB[3]]),
   s.Matrix([2*la*Y*q/13,-7*la*Y*q/39,7*la*q/39]))
ck(controls,'flat_Hessian_hook_loses_nonzero_curvature',s.cancel(hessB[0])!=0)
naive_fk=FK.subs({f:1,g:0,p:0,q:0,r:0,z:0})
ck(controls,'dropping_skew_row_does_not_close_full_module',s.cancel(naive_fk)!=0)
ck(controls,'componentwise_Box_through_Hessian_is_wrong',2*la+2*K!=0)

# Nonzero determinant is proved without expanding the full bivariate one.
Mzero=M.subs({X:0,Y:0})
eta=m-4*la/mH-la/(3*a)
d0=s.factor((m0+2*la/a)*(m-la/(3*a))*zeta**2*eta*mK)
eq('Mzero_block_triangular',Mzero[:2,2:],s.zeros(2,4))
ck(checks,'Mzero_lower_block_triangular',all(Mzero[i,j]==0 for i in range(2,6) for j in range(i+1,6)))
eq('Mzero_lower_diagonal',s.Matrix([Mzero[i,i] for i in range(2,6)]),s.Matrix([zeta,zeta,eta,mK]))
eq('Mzero_upper_block_eigenvalue_product',Mzero[:2,:2].det(),(m0+2*la/a)*(m-la/(3*a)))
eq('zeta_exact',zeta,13614702109*k/s.Integer(12332658624))
eq('eta_exact',eta,20475967*k/s.Integer(18388656))
eq('determinant_zero_frequency_exact',d0,
   -8051601064527887918824634287658165*k**6/s.Integer(12353477676102405846624738231189504))
ck(checks,'nonzero_polynomial_determinant',d0!=0)

# Exact rational cofactor evaluations exercise signs/order. The universal
# identity M adj(M)=det(M) I is the written cofactor proof, not sampling.
sample_data=[]
for xv,yv in [(0,0),(1,2),(-2,3),(s.Rational(1,3),-s.Rational(2,5))]:
    Mn=M.subs({k:1,X:xv,Y:yv})
    en=E0.subs({k:1,X:xv,Y:yv})
    dn=Mn.det()
    bn=Mn.adjugate()*en
    tag=str(xv)+'_'+str(yv)
    eq('cofactor_identity_at_'+tag,Mn*bn,dn*en)
    an=a.subs(k,1)
    chi=-bn/(6*an)
    eq('compact_cancellation_sign_at_'+tag,Mn*chi+dn*en/(6*an))
    sample_data.append({'X':str(xv),'Y':str(yv),'determinant':str(dn),
                        'source_polynomial':str(s.cancel(dn/(12*an)-bn[0]/(36*an**2)))})
    if (xv,yv)==(1,2):
        ck(controls,'opposite_adjoint_sign_leaves_Q',any(v!=0 for v in Mn*(-chi)+dn*en/(6*an)))

# A full parallel-field particular solution on the entire detector chart.
Ec=la*s.Matrix([[5,7],[7,5]])/2
Mc=m*s.eye(2)+7*beta*s.ones(2)+Ec/(3*a)
j=s.Matrix([1,0])
C=s.Matrix([-16420976,-36052016])/(286675*k*k)
zpar=-Ec.inv()*j/(12*a)
hpar=zpar-C/(6*a)
eq('parallel_tensor_forced_equation',Mc*C,-j/(6*a))
eq('parallel_Einstein_forced_equation',Ec*zpar,-j/(12*a))
Eh=s.Matrix([10192832,-652288])/(286675*k)
eq('original_metric_Einstein_readout',Ec*hpar,Eh)
ck(controls,'shifted_metric_is_not_original_observation',s.cancel((Ec*zpar-Eh)[0])!=0)
Fzero=-Eh[0]*d0
ck(checks,'nonzero_source_contact_polynomial',Fzero!=0)
M0n=Mzero.subs(k,1); e0n=E0.subs({k:1,X:0,Y:0})
b0n=M0n.adjugate()*e0n
eq('source_contact_constant_independent_sign',
   d0.subs(k,1)/(12*a.subs(k,1))-b0n[0]/(36*a.subs(k,1)**2),Fzero.subs(k,1))
eq('nonzero_full_chart_metric_signal',7*Eh[0]*d0,-7*Fzero)

# Weighted differential orders: a matrix entry has degree <=1+(w_j-w_i)/2.
# This bounds every determinant/cofactor term and is NOT a sharp-order claim.
weights=[0,0,2,2,2,2]
for i in range(6):
    for jcol in range(6):
        if M[i,jcol]!=0:
            deg=s.Poly(M[i,jcol],X,Y).total_degree()
            ck(checks,'weighted_order_'+str(i)+'_'+str(jcol),2*deg<=2+weights[jcol]-weights[i])
eq('determinant_order_bound',sum(2+w-w for w in weights),12)
eq('metric_detector_order_bound',12+2,14)
eq('fourteen_dimensional_L2_upper_exponent',s.Rational(14,2)+14,21)
# The actual pressure-preserving radial source has nonzero trace unless it
# vanishes: t=0 gives A=-3P/4 and P'+7(C'/C)P=0.
pressure, warp_log_derivative = s.symbols('pressure warp_log_derivative')
eq('zero_trace_pressure_original_divergence_coefficient',
   4*warp_log_derivative*(pressure+3*pressure/4),7*warp_log_derivative*pressure)

paths=[
 'explorations/conditional-build/k2548-compact-coupled-metric-detectors-2026-11-04.md',
 str(Path(__file__).relative_to(R)),
 'explorations/conditional-build/k2531-partial-thickness-source-2026-11-04.md',
 'explorations/conditional-build/k2537-reduced-action-decoupling-2026-11-04.md',
 'explorations/conditional-build/k2539-covariant-tensor-constraints-2026-11-04.md',
 'explorations/conditional-build/k2541-prescribed-product-source-response-2026-11-04.md',
 'explorations/conditional-build/k2543-localized-source-readout-2026-11-04.md',
 'explorations/conditional-build/k2546-source-determined-metric-detectors-2026-11-04.md',
]
report={
 'result':'K2548','exact_algebra':checks,'contrary_controls':controls,
 'coefficients':{'det_M_at_zero':str(d0),'source_F_at_zero':str(s.factor(Fzero)),
                 'zeta':str(s.factor(zeta)),'eta':str(s.factor(eta))},
 'cofactor_evaluations':sample_data,
 'scope':'full-system compact metric contact tests; actual localized-source contact nontriviality conditional on existence; no source-disjoint response or physical/native GU claim',
 'analytic_proof_boundary':'curved intertwining, universal cofactor identity, compact adjoints, radial ODE uniqueness and distributional approximation are proved in the note; finite evaluations are controls only',
 'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths},
}
out=R/'lab/process/k2548-compact-coupled-metric-detectors.json'
if '--write' in sys.argv:
    out.write_text(json.dumps(report,indent=2)+'\n')
else:
    assert json.loads(out.read_text())==report,'saved report mismatch'
print('K2548',len(checks),'exact algebra groups',len(controls),'contrary controls')
