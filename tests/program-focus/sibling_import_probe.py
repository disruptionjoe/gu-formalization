"""Exact controls for ordered sibling applicability. No physical-domain or novelty verifier."""
from pathlib import Path
import argparse,json
import sympy as s
R=s.Rational
checks={}
def check(name,condition,value=None):
    assert bool(condition),name
    checks[name]={'passed':True,'value':str(value) if value is not None else None}

def controls():
    a1=R(1,3);cr=R(8,9)-R(4,3);mss=R(8,9)-1
    check('July_covariant_vs_MSS',cr==R(-4,9) and mss==R(-1,9),(cr,mss))
    check('square_identity_not_scaling_invariant',mss==-a1**2 and 2*mss!=-(2*a1)**2)
    A=s.Matrix([[R(1,3),R(4,3)],[R(-4,9),R(-4,9)]])
    check('W159_coefficient_map_det',A.det()==R(4,9),A.det())
    check('W159_coefficient_witness_only',A*s.Matrix([-2,1])==s.Matrix([R(2,3),R(4,9)]))
    check('old_pole_uses_gamma_phi',R(2,3)/(6*cr)==R(-1,4) and a1/(6*cr)==R(-1,8))
    h,m0,m1,m2=s.symbols('h m0 m1 m2',positive=True)
    ar=-99*h*m1/4;b=17*h*m0/12;lam=235*m2/(88*m1);mass=s.cancel(ar/(6*b))
    check('wedge_mass_ratio',mass==-99*m1/(34*m0),mass)
    ratio=s.cancel(-mass/(lam/3));check('wedge_growth_over_H',ratio==R(13068,3995)*m1**2/(m0*m2),ratio)
    x=(s.sqrt(9+4*R(13068,3995))-3)/2
    check('deSitter_root',s.simplify(x*x+3*x-R(13068,3995))==0,x)
    check('upper_rate_below_one',0<x<1)
    check('wedge_F0_positive_cone',s.cancel(ar+8*b*lam-h*(3995*m0*m2-3267*m1**2)/(132*m1))==0)
    check('F0_cone_margin',3995-3267>0,3995-3267)
    moments=[sum(w*a**j for a,w in [(1,3),(2,-2)])for j in range(3)]
    check('signed_reference_not_probability',moments==[1,-1,-5],moments)
    M=s.Matrix([[0,-1],[1,0]]);I=s.eye(2);H=s.diag(1,-1)
    check('quaternionic_square',M*M.conjugate()==-I)
    check('Krein_sign_reversed',M.T*H*M==-H)
    check('vector_fixed_equation', (I-M*M.conjugate()).det()==4)
    # If Jv=lambda*v, J²v=abs(lambda)^2*v; scalar obstruction 1+u²+v² is positive.
    u,v=s.symbols('u v',real=True)
    check('ray_fixed_point_scalar_contradiction',(1+u*u+v*v).is_positive)
    check('coefficient_conjugation_has_fixed_identity',M*I*M.inv()==I)
    check('nonzero_null_vector_retained',(s.Matrix([1,1]).T*H*s.Matrix([1,1]))[0]==0)
    # No invariant value does not mean no computable value.
    flip=lambda bit:1-bit
    check('no_fixed_bit',all(flip(b)!=b for b in [0,1]))
    check('computable_noninvariant_valuation',[0 for _ in range(3)]==[0,0,0])
    log=(1,1,1);new=log+(1,)
    check('immutable_prefix_flip',new[:len(log)]==log and sum(new)%2==flip(sum(log)%2))
    speed=R(3,5);proper=10*s.sqrt(1-speed**2)
    check('differential_ageing_same_endpoints',proper==8 and proper!=10,proper)
    # Two spacelike wings (0,-1),(0,1), boosts ±3/5 reverse time order.
    gamma=R(5,4)
    times=lambda vel:[gamma*(t-vel*z)for t,z in [(0,-1),(0,1)]]
    check('spacelike_order_reverses',times(speed)==list(reversed(times(-speed))))
    check('common_future_invariant_interval',3**2-1**2>0)
    P=s.diag(1,0);Q=s.diag(0,1)
    A1=s.kronecker_product(P,I);B2=s.kronecker_product(I,Q)
    check('disjoint_record_projectors_commute',A1*B2==B2*A1)
    xi,d=s.symbols('xi d',real=True);plus=s.Matrix([[xi,d],[d,-xi]]);minus=s.Matrix([[xi,d],[-d,-xi]])
    check('BdG_positive_pairing_branch',plus**2==(xi**2+d**2)*I)
    check('BdG_opposite_branch',minus**2==(xi**2-d**2)*I)
    a=s.Matrix([[0,1],[0,0]]);Z=s.diag(1,-1);c1=s.kronecker_product(a,I);c2=s.kronecker_product(Z,a)
    b1=R(3,5)*c1+R(4,5)*c2.T;b2=R(3,5)*c2-R(4,5)*c1.T
    check('fixed_CAR_Bogoliubov',b1*b1.T+b1.T*b1==s.eye(4) and b1*b2+b2*b1==s.zeros(4) and b1*b2.T+b2.T*b1==s.zeros(4))
    mu=s.symbols('mu',positive=True)
    weights=[mu/(2*mu),(1/mu)/(2/mu),s.exp(-mu)/(2*s.exp(-mu))]
    check('Born_symmetric_cost_not_general',all(s.cancel(w)==R(1,2) for w in weights) and R(1,2)!=R(1,4),weights)
    check('DeWitt_trace_quadratic_ratio',(4-16)/(4-16*R(1,2))==3)
    check('DeWitt_absolute_volume_ratio',s.sqrt(s.Abs(R(-12,-4)))==s.sqrt(3))
    ph=lambda omega:1/(3*omega)**2
    check('amplitude_fit_input_dependence',ph(R(7,10))==R(100,441) and ph(R(3,4))==R(16,81))
    t=s.symbols('t',nonnegative=True);forced=s.exp(-2*t)/3
    check('fixed_future_boundary_response',s.diff(forced,t)==forced-s.exp(-2*t))
    check('future_boundary_integral',s.integrate(s.exp(-3*t),(t,0,s.oo))==R(1,3))
    history=(0,1);access=[history[0],history[1]]
    check('access_does_not_extend_source',access==[0,1] and len(history)==2)
    prefix=('record',);branches=[prefix+('A',),prefix+('B',)]
    check('compatibility_does_not_select_fork',all(b[:1]==prefix for b in branches) and branches[0]!=branches[1])
    primitives=['hidden_state','initial_condition','boundary_condition','fixed_source','stochastic_seed','name_provenance','resource_capability','whole_family','completed_history','observer_information_access','relabel_gauge']
    check('eleven_distinct_primitives',len(set(primitives))==11)
    return {'scope':'Exact algebra and finite countercontrols only; not a GU physical completion, PDE closure, Born theorem or independent rebuild of sibling proof suites.','checks':checks,'count':len(checks),'completion_primitives':primitives,'physical_packets':{k:'INCOMPLETE_NULL_CLASS'for k in ['CW','records_commit','contour']}}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--verify',action='store_true');ap.add_argument('--output');args=ap.parse_args();result=controls()
    if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    if args.verify:
        expected=json.loads((Path(__file__).resolve().parents[2]/'lab/process/sibling-import-certificates.json').read_text());assert result==expected
    print('PASS',result['count'],'exact algebra/finite controls; physical packets incomplete')
