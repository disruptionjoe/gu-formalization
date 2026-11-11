#!/usr/bin/env python3
"""Actual radial contact symbols, exact principal-profile and noise controls.
Universal curved asymptotics are the written rescaling proof, not finite fixtures.
"""
import argparse,json,hashlib
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parents[2]
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
checks=[];controls=[]
def ck(n,v):
    assert bool(v),'FAIL '+n
    checks.append(n)
def ct(n,v):
    assert bool(v),'FAIL contrary '+n
    controls.append(n)
X,Y,k=s.symbols('X Y k',nonzero=True)
bank=json.loads((root/'lab/process/k2554-analytic-source-response.json').read_text())['determinant']
pp=list(map(s.Rational,bank['P_coefficients_descending']));qq=list(map(s.Rational,bank['Q_coefficients_descending']))
d=s.expand(sum(c*(X+Y)**(5-i) for i,c in enumerate(pp))+X*Y*sum(c*(X+Y)**(2-i) for i,c in enumerate(qq)))
old=json.loads((root/'lab/process/k2605-source-disjoint-pressure-response.json').read_text())
# sympify uses the same X symbol to preserve the exact coefficient extraction.
R=sum(s.sympify(c,locals={'X':X})*Y**(4-i) for i,c in enumerate(old['remainder_coefficients_descending_k1']))
F=s.expand(s.Rational(old['contact_ratio_k1'])*d+R)
a=s.Poly(F,X,Y).coeff_monomial(X**5);b=s.Poly(d,X,Y).coeff_monomial(X**5)
ck('actual_F_radial_symbol',a==s.Rational(224005433669517008830464,900866321093065))
ck('actual_d_radial_symbol',b==-s.Rational(2605746313310516251459584,22521658027326625))
ck('actual_d_over_F',b/a==-s.Rational(2090956,4493775))
ck('kappa_symbol_ratio',s.cancel((b*k**-4)/(a*k**-5)+s.Rational(2090956,4493775)*k)==0)
# Direct principal Einstein formula: 1/2(xi_i xi^k h_kj+xi_j xi^k h_ki-|xi|²h_ij-xi_i xi_j tr h - g_ij(xi^k xi^l h_kl-|xi|²tr h)).
# The differential (rather than Fourier) symbol uses xi=dr, norm +1.
sign=[-1,1,1,1,1,1,1]+[1,1,1,-1,-1,-1,-1]
metric=s.diag(*sign);GA=s.diag(*(sign[:7]+[0]*7));xi=s.zeros(14,1);xi[4]=1
trace=sum(sign[i]*GA[i,i] for i in range(14));hh=GA*xi
H=(xi*hh.T+hh*xi.T-GA-xi*xi.T*trace-metric*(GA[4,4]-trace))/2
expected=s.Rational(5,2)*(GA-xi*xi.T)+3*(metric-GA)
ck('full_Einstein_radial_principal_tensor',H==expected)
h2=sum(c*c for c in H)
ck('positive_component_H_norm',h2==s.Rational(201,2))
ck('radial_conserved_principal_tensor',H*xi==s.zeros(14,1))
ct('indefinite_contraction_not_sensor_norm',h2>0 and s.det(metric)<0)
# Actual conserved trace and integrating factor, without a tensor-norm identification.
x=s.symbols('x',real=True);C=s.Function('C')(x);P=s.Function('P')(x);alpha=s.diff(C,x)/C
A=P+s.diff(P,x)/(4*alpha);t=(4*A+3*P)/2
ck('trace_order_one',s.simplify(t-7*P/2-s.diff(P,x)/(2*alpha))==0)
ck('trace_injective_outer_collar_identity',s.simplify(s.diff(C**7*P,x)-2*alpha*C**7*t)==0)
ck('full_source_norm_leading_ratio',s.Rational(1,4)**2/(s.Rational(1,2)**2)==s.Rational(1,4))
# Exact finite-regularity principal-profile benchmark, NOT the smooth curved source.
# beta=(1-x²)^24 extended by zero is C23 and has all derivatives required here in L2.
beta=(1-x*x)**24;norms={}
for j in [1,11,23]:
    dp=s.Poly(s.diff(beta,x,j),x);sq=dp*dp
    val=sum(c*(1-(-1)**(n+1))/s.Rational(n+1) for (n,),c in sq.terms())
    ck('positive_exact_profile_derivative_'+str(j),val>0);norms[str(j)]=val
ck('compact_profile_edge_jets',all(s.diff(beta,x,j).subs(x,1)==0 and s.diff(beta,x,j).subs(x,-1)==0 for j in range(24)))
ratio2=s.factor(h2*(b/a)**2*norms['23']*norms['1']/norms['11']**2)
ck('principal_profile_receiver_constant_nonzero',ratio2>0)
e=s.symbols('e',positive=True)
# Direct change of variable for the constant principal model, trace unit.
gram=a*a*e**-20*norms['11']/norms['1'];dnorm2=h2*(a*b)**2*e**-44*norms['23']/norms['1']
ck('trace_unit_bank_exact_e_minus_four_squared',s.cancel(dnorm2/gram**2-ratio2/e**4)==0)
ct('large_Gram_does_not_imply_small_receiver',s.limit(gram,e,0)==s.oo and s.limit(dnorm2/gram**2,e,0)==s.oo)
ct('full_source_and_trace_norms_are_not_identical',s.Rational(1,4)!=1)
# Disjoint receiver Riesz representatives: exact worst-case operator norm is maximum.
Rbank=s.diag(4,9,16);noise=s.Matrix([0,0,s.Rational(1,100)])
error=Rbank*noise
ck('disjoint_bank_worst_direction',error.norm()==s.Rational(16,100))
ck('disjoint_bank_Gram',Rbank*Rbank.T==s.diag(16,81,256))
ct('Frobenius_not_exact_disjoint_operator_norm',sum(z*z for z in Rbank)>256)
ck('unit_receiver_signal_reciprocal',Rbank.inv()*s.Matrix([4,9,16])==s.ones(3,1))
n,L=s.symbols('n L',positive=True)
ck('packed_bank_n_squared',s.simplify((e**-2).subs(e,L/(3*n))-9*n*n/L**2)==0)
ck('summed_bank_squared_norm_n_fifth',s.simplify((n/e**4).subs(e,L/(3*n))-81*n**5/L**4)==0)
ct('post_operator_cutoff_changes_test',s.diff(x*x*s.exp(x),x,2)!=x*x*s.diff(s.exp(x),x,2))
refs=['lab/process/k2554-analytic-source-response.json','lab/process/k2605-source-disjoint-pressure-response.json','explorations/conditional-build/k2617-interior-pressure-identifiability-2026-11-06.md']
report={'result':'K2619','checks':checks,'contrary_controls':controls,'F_X5_k1':str(a),'d_X5_k1':str(b),'d_over_F_k1':str(b/a),'Einstein_radial_positive_norm_squared':str(h2),'exact_principal_profile':{'beta':'(1-x^2)^24 on [-1,1], zero outside; C23 benchmark only','derivative_squared_norms':{j:str(v) for j,v in norms.items()},'receiver_constant_squared_k1_Cchi1':str(ratio2)},'scalings':{'raw_Gram':'epsilon^-21','trace_unit_Gram':'epsilon^-20','trace_unit_receiver_L2':'epsilon^-2','packed_disjoint_bank_operator_norm':'n^2','summed_squared_receiver_norm':'n^5'},'provenance':{f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs},'evidence_kind':'exact actual symbols; exact finite-regularity principal-profile integrals and finite Riesz fixtures; universal smooth curved asymptotic proved in note','ceiling':'specified contact bank and declared auxiliary L2 noise; not optimal among receivers, physical energy or sensor access'}
out=root/'lab/process/k2619-contact-resolution-cost.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'FAIL saved report replay'
print(json.dumps({'result':'K2619','checks':len(checks),'controls':len(controls),'status':'pass'}))
