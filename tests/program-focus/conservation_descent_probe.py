#!/usr/bin/env python3
"""Exact finite controls for local ambient-conservation descent.

Uses rational exponential-polynomials on a flat collar, two normal signs,
and a nonabelian sl2 connection. The general Gaussian-normal extension
theorem and smooth free-jet consequence are separately written proofs.
No Euler equation, global domain, physical stress or old root is computed.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import json
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
CERT = 'lab/process/bet-cosmology-conservation-descent-certificates.json'
DEPENDENCIES = (
    'canon/dark-energy-theta-divergence-free.md',
    'lab/sources/source-claim-register.yaml',
    'explorations/conditional-build/source-action-theta-divergence-2026-11-27.md',
    'lab/process/source-action-theta-divergence-certificates.json',
    'tests/program-focus/source_action_theta_divergence_probe.py',
    'Lean/GUFormalization/ThetaDivergence.lean',
    'explorations/conditional-build/natural-density-fibre-volume-2026-11-25.md',
)
ZERO_RATE = (Q(0),Q(0),Q(0))
ZERO_POWER = (0,0,0)


# Scalar functions sum c exp(rate.x) x^powers, with all data rational.
def clean(p):
    return {k:v for k,v in p.items() if v}


def add(*polys):
    out = {}
    for p in polys:
        for k,v in p.items():
            out[k] = out.get(k,Q(0))+v
    return clean(out)


def scale(c,p):
    return clean({k:Q(c)*v for k,v in p.items()})


def mono(powers=ZERO_POWER, coefficient=1, rate=ZERO_RATE):
    return {(tuple(map(Q,rate)),tuple(powers)):Q(coefficient)} if coefficient else {}


def multiply(p,q):
    out = {}
    for (r,e),a in p.items():
        for (s,f),b in q.items():
            key = (tuple(x+y for x,y in zip(r,s)),tuple(x+y for x,y in zip(e,f)))
            out[key] = out.get(key,Q(0))+a*b
    return clean(out)


def partial(p,axis):
    out = {}
    for (r,e),a in p.items():
        if r[axis]:
            out[(r,e)] = out.get((r,e),Q(0))+a*r[axis]
        if e[axis]:
            f = list(e)
            f[axis] -= 1
            key = (r,tuple(f))
            out[key] = out.get(key,Q(0))+a*e[axis]
    return clean(out)


def restrict_z0(p):
    out = {}
    for (r,e),a in p.items():
        if not e[2]:
            key = ((r[0],r[1],Q(0)),e)
            out[key] = out.get(key,Q(0))+a
    return clean(out)


def precord(p):
    return [[list(map(str,r)),list(e),str(v)] for (r,e),v in sorted(p.items())]


def vzero():
    return [{},{},{}]


def vadd(*vectors):
    return [add(*(v[i] for v in vectors)) for i in range(3)]


def vscale(c,v):
    return [scale(c,p) for p in v]


def smul(p,v):
    return [multiply(p,q) for q in v]


def vpartial(v,axis):
    return [partial(p,axis) for p in v]


def bracket(u,v):
    # Ordered basis E,F,H: [E,F]=H, [H,E]=2E, [H,F]=-2F.
    return [scale(2,add(multiply(u[2],v[0]),scale(-1,multiply(u[0],v[2])))),
            scale(2,add(multiply(u[1],v[2]),scale(-1,multiply(u[2],v[1])))),
            add(multiply(u[0],v[1]),scale(-1,multiply(u[1],v[0])))]


def unit(i):
    out = vzero()
    out[i] = mono()
    return out


E,F,H = unit(0),unit(1),unit(2)
CONNECTION = (H,F,E)


def covariant(v,axis):
    return vadd(vpartial(v,axis),bracket(CONNECTION[axis],v))


def J(v):
    return bracket(E,v)


def linverse(a,v):
    return vadd(vscale(1/a,v),vscale(-1/a**2,J(v)),vscale(1/a**3,J(J(v))))


def lift(beta,normal_sign,a,b):
    # rho=exp(b*x+a*z), tangential metric diag(1,-1), A_z=E.
    forcing = vadd(covariant(beta[0],0),vscale(b,beta[0]),vscale(-1,covariant(beta[1],1)))
    z = mono((0,0,1))
    expminus = mono(rate=(0,0,-a))
    transported = smul(expminus,vadd(forcing,smul(scale(-1,z),J(forcing)),
                                    smul(mono((0,0,2),Q(1,2)),J(J(forcing)))))
    normal = vscale(-normal_sign,linverse(a,vadd(forcing,vscale(-1,transported))))
    return [*beta,normal],forcing


def divergence_expanded(theta,normal_sign,a,b):
    return vadd(covariant(theta[0],0),vscale(b,theta[0]),vscale(-1,covariant(theta[1],1)),
                vscale(normal_sign,vadd(covariant(theta[2],2),vscale(a,theta[2]))))


def divergence_density(theta,normal_sign,a,b):
    rho = mono(rate=(b,0,a))
    inverse = mono(rate=(-b,0,-a))
    return smul(inverse,vadd(covariant(smul(rho,theta[0]),0),
                            vscale(-1,covariant(smul(rho,theta[1]),1)),
                            vscale(normal_sign,covariant(smul(rho,theta[2]),2))))


def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def ma(A,B):
    return [[a+b for a,b in zip(row,other)] for row,other in zip(A,B)]


def ms(c,A):
    return [[c*a for a in row] for row in A]


def mt(A):
    return [list(row) for row in zip(*A)]


def matrix_bracket(A,B):
    return ma(mm(A,B),ms(-1,mm(B,A)))


def matrix_of_constant(v):
    mats = [[[0,1],[0,0]],[[0,0],[1,0]],[[1,0],[0,-1]]]
    out = [[Q(0),Q(0)],[Q(0),Q(0)]]
    for p,A in zip(v,mats):
        out = ma(out,ms(p.get((ZERO_RATE,ZERO_POWER),Q(0)),A))
    return out


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def require(value,message):
    if not value:
        raise AssertionError(message)


def build_certificate(repo):
    checks = {}

    def check(label,value):
        require(label not in checks,'unique labels')
        require(value,label)
        checks[label] = True

    # Real sl2 matrices preserve i*J0, a Hermitian form of inertia(1,1).
    # Multiplying the exact real equality X^t J0+J0 X=0 by i proves H-skewness.
    J0 = [[0,1],[-1,0]]
    zero_matrix = [[0,0],[0,0]]
    for i,X in enumerate((E,F,H)):
        A = matrix_of_constant(X)
        check(f'nonabelian_Krein_skew_generator_{i}',ma(mm(mt(A),J0),mm(J0,A))==zero_matrix)
        check(f'nilpotent_adE_order3_{i}',J(J(J(X)))==vzero())
        for j,Y in enumerate((E,F,H)):
            check(f'independent_matrix_commutator_{i}_{j}',
                  matrix_of_constant(bracket(X,Y))==matrix_bracket(A,matrix_of_constant(Y)))
    check('normal_connection_noncentral',bool(any(bracket(E,F))))
    beta_basis = []
    for slot in range(2):
        for color in range(3):
            for i in range(3):
                for j in range(3-i):
                    beta = [vzero(),vzero()]
                    beta[slot][color] = mono((i,j,0))
                    beta_basis.append(beta)
    mixed = [[add(mono((2,0,0)),mono((0,1,0))),mono((1,1,0)),add(mono((1,0,0)),mono((0,2,0),-1))],
             [add(mono((0,2,0)),mono((1,0,0))),add(mono((3,0,0)),mono((0,1,0))),mono((1,2,0))]]
    fixtures = [*beta_basis,mixed]
    check('complete_degree2_beta_control_basis',len(beta_basis)==36)
    cases = []
    for normal_sign in (-1,1):
        for a,b in ((Q(2),Q(3)),(Q(-1),Q(2))):
            label = f'normal{normal_sign}_density{a}_{b}'
            counts = dict(lift_zero=0,trace=0,zero_normal_initial=0,density_formula=0,
                          integration_factor=0,omit_density_failures=0,
                          omit_connection_failures=0,wrong_sign_failures=0,fixed_normal_failures=0)
            records = []
            for beta in fixtures:
                theta,forcing = lift(beta,normal_sign,a,b)
                expanded = divergence_expanded(theta,normal_sign,a,b)
                density = divergence_density(theta,normal_sign,a,b)
                counts['lift_zero'] += expanded==vzero()
                counts['density_formula'] += density==expanded
                counts['trace'] += theta[:2]==beta
                counts['zero_normal_initial'] += [restrict_z0(p) for p in theta[2]]==vzero()
                # Matrix-valued integrating factor exp(az) exp(z adE).
                z = mono((0,0,1))
                theta_transport = smul(mono(rate=(0,0,a)),
                    vadd(theta[2],smul(z,J(theta[2])),smul(mono((0,0,2),Q(1,2)),J(J(theta[2])))))
                source_transport = smul(mono(rate=(0,0,a)),
                    vadd(forcing,smul(z,J(forcing)),smul(mono((0,0,2),Q(1,2)),J(J(forcing)))))
                counts['integration_factor'] += vpartial(theta_transport,2)==vscale(-normal_sign,source_transport)
                counts['omit_density_failures'] += divergence_expanded(theta,normal_sign,Q(0),Q(0))!=vzero()
                counts['omit_connection_failures'] += vadd(expanded,vscale(-normal_sign,J(theta[2])))!=vzero()
                counts['wrong_sign_failures'] += divergence_expanded(theta,-normal_sign,a,b)!=vzero()
                counts['fixed_normal_failures'] += forcing!=vzero()
                records.append([precord(p) for p in theta[2]])
            for name in ('lift_zero','trace','zero_normal_initial','density_formula','integration_factor'):
                check(label+'_'+name,counts[name]==len(fixtures))
            for name in ('omit_density_failures','omit_connection_failures','wrong_sign_failures','fixed_normal_failures'):
                check(label+'_'+name,counts[name]>0)
            cases.append({'normal_sign':normal_sign,'rho':f'exp({b}*x+{a}*z)',
                'tested_beta_fields':len(fixtures),'counts':counts,
                'normal_lift_records_sha256':canonical_sha(records),
                'mixed_example_normal_lift':records[-1]})

    # Nonconstant source-distortion scalar: no ds appears in a connection's
    # algebraic coderivative variation. Pair the full symmetric off-diagonal G.
    theta,_ = lift(mixed,1,Q(2),Q(3))
    scalar = add(mono(),mono((1,0,1)),mono((0,2,0)))
    metric = [[Q(2),Q(1),Q(-2)],[Q(1),Q(3),Q(4)],[Q(-2),Q(4),Q(5)]]
    shift = vadd(*(vscale(metric[i][j],bracket(smul(scalar,theta[i]),theta[j]))
                   for i in range(3) for j in range(3)))
    check('source_distortion_symmetric_contraction_zero',shift==vzero())
    check('nonsymmetric_contraction_mutant_rejected',bracket(smul(scalar,theta[0]),theta[1])!=vzero())

    # Exact chain-rule map on every beta-dependent zero-order polynomial
    # stress of degree1/2, with 6 beta components and 2 observed coordinates.
    beta_monomials = []
    for i in range(6):
        e = [0]*6
        e[i] = 1
        beta_monomials.append(tuple(e))
    for i in range(6):
        for j in range(i,6):
            e = [0]*6
            e[i] += 1
            e[j] += 1
            beta_monomials.append(tuple(e))
    columns = []
    pivots = {}
    for mu in range(2):
        for nu in range(2):
            for e in beta_monomials:
                row = {}
                for r,c in enumerate(e):
                    if c:
                        f = list(e)
                        f[r] -= 1
                        row[(nu,mu,r,tuple(f))] = Q(c)
                pivot = min(row)
                require(pivot not in pivots,'distinct chain-rule pivot')
                pivots[pivot] = len(columns)
                columns.append(row)
    check('zeroorder_chainrule_108_independent_columns',len(columns)==108 and len(pivots)==108)
    check('zeroorder_chainrule_pivot_submatrix_diagonal',all(
        bool(columns[j].get(pivot,Q(0)))==(i==j)
        for pivot,i in pivots.items() for j in range(len(columns))))
    constant_beta = mono()
    varying_beta = add(mono(),mono((1,0,0)))
    constant_div = partial(multiply(constant_beta,constant_beta),0)
    varying_div = partial(multiply(varying_beta,varying_beta),0)
    check('constant_beta_only_test_is_insufficient',not constant_div and
          varying_div==add(mono(coefficient=2),mono((1,0,0),2)))
    chain_record = [[[[nu,mu,r,list(e)],str(v)] for (nu,mu,r,e),v in sorted(row.items())] for row in columns]

    # Flat Lorentzian 2D differential superpotential, not a curved identity.
    phi = add(mono((3,1,0)),mono((1,3,0)),mono((2,2,0)))
    xx = partial(partial(phi,0),0)
    xy = partial(partial(phi,0),1)
    yy = partial(partial(phi,1),1)
    stress = [[yy,scale(-1,xy)],[scale(-1,xy),xx]]
    stress_div = [add(partial(stress[0][nu],0),partial(stress[1][nu],1)) for nu in range(2)]
    check('flat_superpotential_nonzero',any(any(row) for row in stress))
    check('flat_superpotential_divergence_zero',stress_div==[{},{}])
    check('flat_superpotential_wrong_cross_sign_rejected',
          add(partial(yy,0),partial(xy,1))!={})
    return {'schema':'gu-conservation-descent-certificate-v1','data_only':True,
        'probe_sha256':sha(Path(__file__).resolve()),
        'dependency_only_sha256':{name:sha(repo/name) for name in DEPENDENCIES},
        'dependency_policy':'Source premises and previous conservation results are hash-bound only; no old root or certificate is replayed.',
        'collar_conventions':{'coordinates':['x','y','z'],'metric':'diag(1,-1,epsilon), epsilon=+1 or -1',
            'Lie_basis':'E=[[0,1],[0,0]], F=[[0,0],[1,0]], H=diag(1,-1); [E,F]=H',
            'connection':'A_x=H, A_y=F, A_z=E; nonabelian and nonflat',
            'positive_weight':'rho=exp(b*x+a*z)',
            'divergence':'rho^-1 sum_i g^ii (partial_i+[A_i,.])(rho theta_i); coderivative is its negative',
            'normal_ODE':'(partial_z+a+adE)theta_z=-epsilon*(D_x beta_x+b beta_x-D_y beta_y)',
            'normal_initial_data':'theta_z(x,y,0)=0',
            'construction':'-(epsilon)*(a+adE)^-1*(I-exp(-az)*exp(-z adE))*forcing; (adE)^3=0',
            'finite_scope':'All degree<=2 polynomial beta controls plus one mixed cubic field; the universal smooth/codimension theorem is written separately.'},
        'collar_cases':cases,'total_lifts':len(cases)*len(fixtures),
        'zeroorder_chainrule':{'beta_components':6,'stress_components':4,'positive_degree_monomials':27,
            'columns':108,'rank':108,'kernel_dimension':0,'map_sha256':canonical_sha(chain_record),
            'meaning':'Polynomial calibration of independent first-jet coefficients; beta-independent stress terms are excluded from these columns and are not automatically conserved.'},
        'flat_superpotential':{'phi':precord(phi),'stress':[[precord(p) for p in row] for row in stress],
            'formula':'F^{mu nu}=partial^mu partial^nu phi-g^{mu nu} box(phi), g=diag(1,-1)',
            'ceiling':'Nonzero derivative-dependent off-shell conservation control. Curved covariant replacement is not claimed.'},
        'checks':checks,'check_count':len(checks),
        'written_consequence':'Locally every smooth observed beta is the trace of an ambient weighted-coderivative-zero theta. Thus a q-local finite-jet stress conserved on every such ambient solution is identically conserved for every beta. A smooth zero-order such stress is beta-independent by free first jets.',
        'source_distortion':'delta_(B+s theta)^rho theta=delta_B^rho theta by symmetric contraction of [theta_i,theta_j], for smooth scalar s; no derivative of s occurs in this connection variation.',
        'scope_limits':['Conservation-only local solution class, not the full Euler solution set',
            'No fixed outer boundary/global extension or physical-domain theorem',
            'No native action, physical stress or cosmology calibration selected',
            'Finite-order stress may be a nonzero identically conserved differential superpotential',
            'Source theta/ordinary-coderivative dictionary remains a separately stated premise'],
        'not_run':['Old candidate root or divergence replay','Full native geometry/tensor construction',
            'PDE or bundle formalization','Lean compilation'],
        'timing_policy':'Runtime and byte count are confined to ephemeral receipts.'}


def write_json(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary = path.with_suffix(path.suffix+'.new')
    temporary.write_text(json.dumps(value,indent=2,sort_keys=True)+'\n')
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=ROOT)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write-certificate',action='store_true')
    mode.add_argument('--verify',action='store_true')
    parser.add_argument('--certificate',type=Path)
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    started = time.monotonic()
    repo = args.repo.resolve()
    path = args.certificate or repo/CERT
    actual = build_certificate(repo)
    if args.write_certificate:
        write_json(path,actual)
    else:
        require(json.loads(path.read_text())==actual,'exact frozen certificate equality')
    receipt = {'passed':True,'mode':'write-certificate' if args.write_certificate else 'verify',
        'probe_sha256':actual['probe_sha256'],'certificate_sha256':sha(path),
        'certificate_bytes':path.stat().st_size,'checks':actual['check_count'],
        'exact_collar_lifts':actual['total_lifts'],'stress_chainrule_rank':actual['zeroorder_chainrule']['rank'],
        'seconds':time.monotonic()-started}
    if args.output:
        write_json(args.output,receipt)
    print(json.dumps(receipt,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
