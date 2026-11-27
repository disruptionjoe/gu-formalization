#!/usr/bin/env python3
"""Small exact controls for full fixed-Shiab variational consistency.

Rational sl3/gl3 fixtures calibrate cyclic Hessian signs, central slots,
quasicentroid collapse and the quadratic mixed obstruction. The universal
matrix-unit/Spin/geometric proof is written separately. No Hom census,
dense Dirac construction, source equation selection or old replay is run.
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
CERT = 'lab/process/full-shiab-consistency-certificates.json'
DEPENDENCIES = (
    'explorations/conditional-build/source-action-riemann-silence-2026-11-27.md',
    'explorations/conditional-build/riemann-realform-transfer-2026-11-27.md',
    'tests/program-focus/riemann_realform_transfer_probe.py',
    'lab/process/riemann-realform-transfer-certificates.json',
    'lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md',
    'lab/sources/source-claim-register.yaml',
)
ZERO = tuple(tuple(Q(0) for _ in range(3)) for _ in range(3))
ID = tuple(tuple(Q(i==j) for j in range(3)) for i in range(3))


def matrix(rows):
    return tuple(tuple(map(Q,row)) for row in rows)


def add(*matrices):
    return tuple(tuple(sum((A[i][j] for A in matrices),Q(0)) for j in range(3)) for i in range(3))


def scale(c,A):
    return tuple(tuple(Q(c)*x for x in row) for row in A)


def mul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def transpose(A):
    return tuple(zip(*A))


def bracket(A,B):
    return add(mul(A,B),scale(-1,mul(B,A)))


def trace(A):
    return sum(A[i][i] for i in range(3))


def pair(A,B):
    return trace(mul(A,B))


def unit(i,j):
    return tuple(tuple(Q(a==i and b==j) for b in range(3)) for a in range(3))


def rank(rows):
    rows = [list(map(Q,row)) for row in rows]
    r = 0
    for c in range(len(rows[0])):
        p = next((i for i in range(r,len(rows)) if rows[i][c]),None)
        if p is None:
            continue
        rows[r],rows[p] = rows[p],rows[r]
        pivot = rows[r][c]
        rows[r] = [x/pivot for x in rows[r]]
        for i in range(len(rows)):
            if i!=r:
                q = rows[i][c]
                rows[i] = [x-q*y for x,y in zip(rows[i],rows[r])]
        r += 1
        if r==len(rows):
            break
    return r


def flat(A):
    return [x for row in A for x in row]


def field_add(T,b,c=1):
    return [add(X,scale(c,Y)) for X,Y in zip(T,b)]


def field_pair(T,U):
    return sum(pair(X,Y) for X,Y in zip(T,U))


def field(slot,A):
    return [A if i==slot else ZERO for i in range(3)]


def K(coefficients,i,j,k,Z):
    if j==k:
        return ZERO
    sign = 1 if j<k else -1
    callback = coefficients.get((i,min(j,k),max(j,k)))
    return scale(sign,callback(Z)) if callback else ZERO


def endpoint(coefficients,T):
    return [add(*(K(coefficients,i,j,k,bracket(T[j],T[k]))
                  for j in range(3) for k in range(j+1,3))) for i in range(3)]


def derivative_endpoint(coefficients,T,b):
    return [add(*(K(coefficients,i,j,k,add(bracket(b[j],T[k]),bracket(T[j],b[k])))
                  for j in range(3) for k in range(j+1,3))) for i in range(3)]


def derivative_ordered(coefficients,T,b):
    return [add(*(K(coefficients,i,j,k,bracket(T[j],b[k]))
                  for j in range(3) for k in range(3))) for i in range(3)]


def cubic(coefficients,T):
    return field_pair(T,endpoint(coefficients,T))/3


def direct_cubic_derivative(coefficients,T,b):
    # Exact derivative at0 of a degree<=3 polynomial, from four values.
    values = {s:cubic(coefficients,field_add(T,b,s)) for s in (-2,-1,1,2)}
    return (8*(values[1]-values[-1])-(values[2]-values[-2]))/12


def pderivative(p):
    return [Q(i)*p[i] for i in range(1,len(p))] or [Q(0)]


def pmul(p,q):
    out = [Q(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            out[i+j] += a*b
    return out


def integral01(p):
    return sum(c/Q(i+1) for i,c in enumerate(p))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(value,message):
    if not value:
        raise AssertionError(message)


def build_certificate(repo):
    checks = {}

    def check(label,value):
        require(label not in checks,'unique labels')
        require(value,label)
        checks[label] = True

    H1 = matrix([[1,0,0],[0,-1,0],[0,0,0]])
    H2 = matrix([[0,0,0],[0,1,0],[0,0,-1]])
    sl = [unit(i,j) for i in range(3) for j in range(3) if i!=j]+[H1,H2]
    gl = sl+[ID]
    check('sl3_trace_form_nondegenerate',rank([[pair(X,Y) for Y in sl] for X in sl])==8)
    check('commutators_span_sl3',rank([flat(bracket(X,Y)) for X in gl for Y in gl])==8)
    center_columns = [[x for X in sl for x in flat(bracket(X,Y))] for Y in sl]
    check('sl3_centerlessness',rank(center_columns)==8)
    cyclic_cases = 0
    cyclic_residual_cases = 0
    for X in sl:
        for Y in sl:
            for Z in sl:
                require(pair(X,bracket(Y,Z))==pair(Y,bracket(Z,X))==pair(Z,bracket(X,Y)),
                        'cyclic trace invariance')
                cyclic_cases += 1
    check('all512_basis_cyclic_trace_identities',cyclic_cases==512)

    # Scalar alternating external3-tensor, extended by zero on the other
    # eleven form directions: an actual non-Spin-invariant positive control.
    alt = {(0,1,2):lambda X:X,(1,0,2):lambda X:scale(-1,X),(2,0,1):lambda X:X}
    T = [unit(0,1),unit(1,2),unit(2,0)]
    b = field(0,unit(0,1))
    check('alternating_external_cubic_nonzero',cubic(alt,T)==1)
    check('alternating_external_exact_cubic_endpoint',direct_cubic_derivative(alt,T,b)==field_pair(b,endpoint(alt,T))==1)
    check('ordered_DF_has_no_extra_factor2',derivative_endpoint(alt,T,b)==derivative_ordered(alt,T,b))
    check('quadratic_endpoint_Euler_homogeneity',derivative_endpoint(alt,T,T)==[scale(2,X) for X in endpoint(alt,T)])
    background = field(2,unit(2,0))
    c = field(1,unit(1,2))
    hleft = field_pair(c,derivative_endpoint(alt,background,b))
    hright = field_pair(b,derivative_endpoint(alt,background,c))
    check('cyclic_Hessian_positive_sign',hleft==hright==1)
    bad_sign = dict(alt)
    bad_sign[(1,0,2)] = lambda X:X
    check('cyclic_Hessian_sign_mutant_rejected',field_pair(c,derivative_endpoint(bad_sign,background,b))!=
          field_pair(b,derivative_endpoint(bad_sign,background,c)))
    repeated = {(0,0,1):lambda X:X}
    repeated_T = field(0,unit(0,1))
    repeated_b = field(1,unit(1,2))
    repeated_c = field(0,unit(2,0))
    repeated_pair = field_pair(repeated_c,derivative_endpoint(repeated,repeated_T,repeated_b))
    check('repeated_external_label_detected',repeated_pair==1 and
          derivative_endpoint(repeated,repeated_T,repeated_c)==[ZERO]*3)
    central_out = {(2,0,1):lambda X:scale(pair(unit(2,0),X),ID)}
    two_slot_T = [unit(0,1),unit(1,2),ZERO]
    central_c = field(2,ID)
    central_endpoint = field_pair(central_c,endpoint(central_out,two_slot_T))
    central_derivative = direct_cubic_derivative(central_out,two_slot_T,central_c)
    check('central_output_on_commutator_detected',central_endpoint==3 and central_derivative==1)
    check('central_translation_DF_zero',derivative_endpoint(central_out,two_slot_T,central_c)==[ZERO]*3)

    # Three-cyclic-quasicentroid collapse signs: verify the formal residual
    # combination on arbitrary distinct maps, then the scalar positive and
    # unequal/noncentroid negative controls on the complete sl3 basis.
    D = lambda X:transpose(X)
    E = lambda X:bracket(H1,X)
    F = lambda X:scale(3,X)
    q1 = lambda X,Y:add(bracket(D(X),Y),scale(-1,bracket(X,E(Y))))
    q2 = lambda X,Y:add(bracket(E(X),Y),scale(-1,bracket(X,F(Y))))
    q3 = lambda X,Y:add(bracket(F(X),Y),scale(-1,bracket(X,D(Y))))
    for X in sl:
        for Y in sl:
            require(add(q1(Y,X),scale(-1,q2(X,Y)))==bracket(X,add(F(Y),scale(-1,D(Y)))),
                    'F-D residual combination')
            require(add(q3(X,Y),scale(-1,q1(X,Y)),scale(-1,bracket(add(F(X),scale(-1,D(X))),Y)))
                    ==bracket(X,add(E(Y),scale(-1,D(Y)))),'E-D residual combination')
            cyclic_residual_cases += 1
    check('three_cyclic_residual_identities',cyclic_residual_cases==64)
    check('scalar_quasicentroid_positive',all(bracket(scale(2,X),Y)==bracket(X,scale(2,Y)) for X in sl for Y in sl))
    check('unequal_cyclic_maps_rejected',any(bracket(scale(2,X),Y)!=bracket(X,scale(3,Y)) for X in sl for Y in sl))
    check('transpose_noncentroid_rejected',any(bracket(D(X),Y)!=bracket(X,D(Y)) for X in sl for Y in sl))
    check('derivation_noncentroid_rejected',any(bracket(E(X),Y)!=bracket(X,E(Y)) for X in sl for Y in sl))

    # The cubic alone does NOT imply S=0: central curvature inputs are absent
    # from every commutator. This nonzero map survives the cubic exactly.
    central_in = {(0,0,1):lambda X:scale(trace(X)/3,H1)}
    check('central_input_noncentral_map_nonzero',K(central_in,0,0,1,ID)==H1)
    check('central_input_map_kills_all_brackets',all(K(central_in,0,0,1,bracket(X,Y))==ZERO for X in gl for Y in gl))
    cubic_survivors = []
    for U,V,W in ((H1,ID,unit(0,1)),(unit(0,1),unit(1,2),unit(2,0)),(ID,H2,H1)):
        state = [U,V,W]
        direction = [W,U,V]
        cubic_survivors.append(endpoint(central_in,state)==[ZERO]*3 and
                               direct_cubic_derivative(central_in,state,direction)==0)
    check('central_input_map_cubic_survivor',all(cubic_survivors))

    # Quadratic mixed obstruction with genuine derivative and integration
    # by parts, not an incorrect pointwise transpose of D_B.
    # Base T_1=f(t)Id, variation b_0=g(t)H1, t=x0; both vanish at
    # the endpoints. The unit endpoint is <b,S dT>=mixed, while
    # <T,S db>=0. The following principal-jet test is independent
    # of these integrated fields and allows b_0(p)=H1.
    f = list(map(Q,[0,1,-1]))
    g = list(map(Q,[0,0,1,-1]))
    fp,gp = pderivative(f),pderivative(g)
    check('quadratic_mixed_boundary_zero',f[0]==g[0]==sum(f)==sum(g)==0)
    check('derivative_jet_central_input',f[0]==0 and fp[0]==1 and trace(H1)==0 and
          pair(H1,K(central_in,0,0,1,ID))==2)
    mixed = pair(H1,H1)*integral01(pmul(g,fp))
    check('quadratic_mixed_pair_exact',mixed==Q(-1,30))
    check('quadratic_half_derivative_not_unit_endpoint',mixed/2==Q(-1,60) and mixed/2!=mixed)
    # Reverse mixed pairing is zero because S kills every traceless input.
    check('reverse_quadratic_mixed_pair_zero',K(central_in,0,0,1,H1)==ZERO)
    # The alternating3-tensor survives BOTH action weights if Spin is dropped:
    # b_1=f H1, T_2=g H1 gives curl's two mixed pairings.
    reverse_alt = -pair(H1,H1)*integral01(pmul(f,gp))
    check('alternating_external_quadratic_positive_control',mixed==reverse_alt and (mixed+reverse_alt)/2==mixed)
    check('integration_by_parts_minus_sign_required',mixed!=-reverse_alt)

    # Central-input output must be scalar if orthogonal to all traceless
    # test matrices. Finite gl3 trace-pairing control, not a Hom census.
    trace_test_columns = [[pair(X,Y) for X in sl] for Y in gl]
    check('central_output_trace_test_rank8',rank(trace_test_columns)==8)
    check('identity_is_only_fixture_central_kernel',all(pair(X,ID)==0 for X in sl) and
          rank([flat(X) for X in sl]+[flat(ID)])==9)
    check('dimension14_minusId_special_orthogonal',(-1)**14==1)
    check('external3_parity_odd',(-1)**3==-1)
    check('central_input_output_parity_opposite',(-1)**2==1 and (-1)**13==-1)
    return {'schema':'gu-full-shiab-consistency-certificate-v1','data_only':True,
        'probe_sha256':sha(Path(__file__).resolve()),
        'dependency_only_sha256':{name:sha(repo/name) for name in DEPENDENCIES},
        'dependency_policy':'Prior source and real-form results are authenticated dependencies; no old numerical certificate or Hom census is replayed.',
        'conventions':{'field':'rational controls inside complexified gl3; universal carrier is separately full gl128',
            'pairing':'complex-bilinear trace, no Hermitian conjugation',
            'exterior':'e^a wedge omega_i=delta_ai vol; K_i^{kj}=-K_i^{jk}',
            'curvature':'F_i=sum_(j<k) K_i^{jk}[T_j,T_k]',
            'cubic':'I3=(1/3)sum_i tr(T_i F_i); target derivative is unit F',
            'linear':'I2=(1/2)<T,S D_B T>; mixed control uses flat d and boundary-vanishing fields',
            'three_slot_embedding':'Use external slots0,1,2 in dimension14, other slots zero; the alternating tensor is explicitly not Spin invariant.'},
        'finite_algebra':{'sl3_dimension':8,'trace_Gram_rank':8,'commutator_span_rank':8,
            'centerlessness_rank':8,'cyclic_basis_triples':cyclic_cases,
            'external_alternating_cubic_value':'1','cyclic_Hessian_sides':['1','1'],
            'repeated_label_pair':'1','central_output_bad_cubic_derivative':'1',
            'central_output_bad_endpoint':'3'},
        'quadratic_mixed_control':{'nonzero_cubic_survivor':'K_0^{01}(Z)=tr(Z)H1/3, H1=diag(1,-1,0)',
            'central_base_field':'T_1(t)=(t-t^2)Id','traceless_variation':'b_0(t)=(t^2-t^3)H1',
            'interval':['0','1'],'mixed_pair':str(mixed),'half_action_derivative':str(mixed/2),
            'unit_endpoint':str(mixed),'reverse_pair':'0',
            'independent_principal_jet':'Central base T(p)=0, (dT)_01(p)=Id; traceless variation b_0(p)=H1 detects the output by tr(H1^2)=2. This jet test is separate from the boundary-vanishing integral fixture.',
            'meaning':'Cubic consistency alone has nonzero central-input survivors; the same quadratic/unit-linear premise excludes noncentral output on those inputs.'},
        'without_Spin_positive_control':{'map':'K_i^{jk}=epsilon_ijk Id on slots0,1,2',
            'cubic_endpoint':True,'quadratic_endpoint_mixed_control':True,
            'reason_not_counterexample':'Its fixed nonzero alternating external3-tensor changes sign under -Id; it is not Spin14 equivariant.'},
        'checks':checks,'check_count':len(checks),
        'written_claim':'Under fixed pointwise real-linear Spin-equivariant S, full-U/full-Dirac translations and the same cubic/linear unit endpoints from the one-third/one-half action terms, S vanishes. Universal quasicentroid classification, arbitrary-metric jets, real-form transport and source applicability are written/reviewed, not established by sl3 fixtures.',
        'scope_limits':['No source uniqueness or GU-wide verdict','No derivative-valued or moving S theorem',
            'Restricted tangents, changed endpoints and extra equivariance-breaking tensors are different hypotheses',
            'No full action/operator/domain construction or physical stress conclusion'],
        'not_run':['Full Dirac matrices','Hom/character census','Old witness or root replay','Lean compilation'],
        'timing_policy':'Runtime and certificate byte count appear only in ephemeral receipts.'}


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
        'basis_trace_triples':actual['finite_algebra']['cyclic_basis_triples'],
        'quadratic_derivative':actual['quadratic_mixed_control']['half_action_derivative'],
        'quadratic_endpoint':actual['quadratic_mixed_control']['unit_endpoint'],
        'seconds':time.monotonic()-started}
    if args.output:
        write_json(args.output,receipt)
    print(json.dumps(receipt,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
