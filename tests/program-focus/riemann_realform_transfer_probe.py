#!/usr/bin/env python3
"""Exact finite controls for the real-form Riemann-silence adapter.

Standard library only. The universal complexification/naturality theorem is
a separately reviewed written proof. These small matrices calibrate its
algebra, not a dense native Dirac realization or a new witness census.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import argparse
import hashlib
import json
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
CERT = 'lab/process/riemann-realform-transfer-certificates.json'
OLD_CERT = 'lab/process/source-action-riemann-silence-certificates.json'
OLD_PROBE = 'tests/program-focus/source_action_riemann_silence_probe.py'
DEPENDENCIES = (
    OLD_CERT, OLD_PROBE,
    'explorations/conditional-build/source-action-riemann-silence-2026-11-27.md',
    'explorations/resolver-wave-k77b2-shiab-family-curvature-selector-transgression-2026-08-04.md',
    'explorations/conditional-build/source-action-external-datum-candidate-2026-11-25.md',
    'explorations/conditional-build/source-action-wave2-construction-2026-11-25.md',
)


@dataclass(frozen=True)
class G:
    re: Q = Q(0)
    im: Q = Q(0)

    def __post_init__(self):
        object.__setattr__(self, 're', Q(self.re))
        object.__setattr__(self, 'im', Q(self.im))

    def __add__(self, other):
        other = lift(other)
        return G(self.re+other.re, self.im+other.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self+-lift(other)

    def __rsub__(self, other):
        return lift(other)+-self

    def __mul__(self, other):
        other = lift(other)
        return G(self.re*other.re-self.im*other.im,
                 self.re*other.im+self.im*other.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = lift(other)
        denominator = other.re**2+other.im**2
        if not denominator:
            raise ZeroDivisionError('Gaussian-rational zero denominator')
        return self*G(other.re/denominator, -other.im/denominator)

    def conj(self):
        return G(self.re, -self.im)

    def __bool__(self):
        return bool(self.re or self.im)


def lift(x):
    return x if isinstance(x, G) else G(x)


I = G(0, 1)


def matrix(rows):
    return [[lift(x) for x in row] for row in rows]


def mscale(c, A):
    return [[lift(c)*x for x in row] for row in A]


def madd(A, B):
    return [[x+y for x,y in zip(row,other)] for row,other in zip(A,B)]


def mmul(A, B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), G())
             for j in range(len(B[0]))] for i in range(len(A))]


def adjoint(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def trace(A):
    return sum((A[i][i] for i in range(len(A))), G())


def inverse2(A):
    a,b = A[0]
    c,d = A[1]
    return mscale(G(1)/(a*d-b*c), [[d,-b],[-c,a]])


def sharp(H, A):
    return mmul(mmul(inverse2(H), adjoint(A)), H)


def skew(H, A):
    return sharp(H,A) == mscale(-1,A)


def bracket(A, B):
    return madd(mmul(A,B), mscale(-1,mmul(B,A)))


def rref(A):
    A = [row[:] for row in A]
    row = 0
    pivots = []
    for col in range(len(A[0])):
        pivot = next((k for k in range(row,len(A)) if A[k][col]), None)
        if pivot is None:
            continue
        A[row],A[pivot] = A[pivot],A[row]
        scale = A[row][col]
        A[row] = [x/scale for x in A[row]]
        for k in range(len(A)):
            if k != row:
                scale = A[k][col]
                A[k] = [x-scale*y for x,y in zip(A[k],A[row])]
        pivots.append(col)
        row += 1
        if row == len(A):
            break
    return A,pivots


def determinant(A):
    total = G()
    for p in permutations(range(len(A))):
        inversions = sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
        value = G((-1)**inversions)
        for i,j in enumerate(p):
            value = value*A[i][j]
        total += value
    return total


def encode(A):
    if isinstance(A,G):
        return [str(A.re), str(A.im)]
    return [encode(x) for x in A]


# Sparse Q[g,t] polynomials, used only for the Hessian chart countercontrol.
def padd(*polys):
    out = {}
    for p in polys:
        for e,c in p.items():
            out[e] = out.get(e,Q(0))+c
    return {e:c for e,c in out.items() if c}


def pscale(c, p):
    return {e:Q(c)*v for e,v in p.items() if c*v}


def pmul(p, q):
    return padd(*({(e[0]+f[0],e[1]+f[1]):c*d}
                  for e,c in p.items() for f,d in q.items()))


def power(p, n):
    out = {(0,0):Q(1)}
    for _ in range(n):
        out = pmul(out,p)
    return out


def derivative(p, axis):
    out = {}
    for e,c in p.items():
        if e[axis]:
            f = list(e)
            f[axis] -= 1
            out[tuple(f)] = c*e[axis]
    return out


def substitute_t(p, value):
    return padd(*(pmul({(e[0],0):c},power(value,e[1])) for e,c in p.items()))


def polynomial_record(p):
    return [[list(e),str(c)] for e,c in sorted(p.items())]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(value, message):
    if not value:
        raise AssertionError(message)


def build_certificate(repo):
    checks = {}

    def check(label, value):
        require(label not in checks, 'unique check labels')
        require(value,label)
        checks[label] = True

    inherited = json.loads((repo/OLD_CERT).read_text())
    check('inherited_producer_binding_only',inherited['producer_sha256']==sha(repo/OLD_PROBE))
    for name,digest in inherited['native_inputs_sha256'].items():
        check('inherited_dependency_binding_only:'+name,sha(repo/name)==digest)
    units = []
    for i in range(2):
        for j in range(2):
            A = matrix([[0,0],[0,0]])
            A[i][j] = G(1)
            units += [A,mscale(I,A)]
    identity = matrix([[1,0],[0,1]])
    Hs = [matrix([[1,0],[0,1]]),matrix([[1,0],[0,-1]]),
          matrix([[2,0],[0,-3]]),matrix([[0,1],[1,0]])]
    records = []
    for hidx,H in enumerate(Hs):
        prefix = f'H{hidx}'
        check(prefix+'_Hermitian_invertible',adjoint(H)==H and mmul(H,inverse2(H))==identity)
        basis = []
        for idx,A in enumerate(units):
            As = sharp(H,A)
            X = mscale(Q(1,2),madd(A,mscale(-1,As)))
            Y = mscale(G(1)/(2*I),madd(A,As))
            check(f'{prefix}_decomposition_{idx}',skew(H,X) and skew(H,Y) and madd(X,mscale(I,Y))==A)
            check(f'{prefix}_sharp_involution_{idx}',sharp(H,As)==A)
            for B in (X,Y):
                if any(any(row) for row in B) and B not in basis:
                    basis.append(B)
        # Rank over R checks the four-dimensional real form in this fixture.
        real_columns = [[G(x.re) for row in A for x in row]+[G(x.im) for row in A for x in row]
                        for A in basis]
        check(prefix+'_real_form_dimension4',len(rref(real_columns)[1])==4)
        z,w = G(2,3),G(-1,2)
        mutant_failures = 0
        for i,X in enumerate(basis):
            for j,Y in enumerate(basis):
                tr = trace(mmul(X,Y))
                check(f'{prefix}_trace_real_{i}_{j}',tr.im==0)
                check(f'{prefix}_complex_bilinear_{i}_{j}',trace(mmul(mscale(z,X),mscale(w,Y)))==z*w*tr)
                check(f'{prefix}_bracket_closed_{i}_{j}',skew(H,bracket(X,Y)))
                mutant_failures += bool(z*w*tr != z.conj()*w*tr)
        check(prefix+'_sesquilinear_mutant_rejected',mutant_failures>0)
        X = mscale(I,identity)
        check(prefix+'_associative_closure_mutant_rejected',skew(H,X) and not skew(H,mmul(X,X)))
        tr_complex = trace(mmul(mscale(I,X),X))
        check(prefix+'_discard_imaginary_trace_mutant_rejected',tr_complex.im!=0)
        # Transpose without conjugation incorrectly sends iId to itself.
        fakeY = mscale(G(1)/(2*I),madd(X,X))
        check(prefix+'_linear_adjoint_mutant_rejected',not skew(H,fakeY))
        T = (basis[0],basis[-1])
        b = (basis[1],basis[-2])
        Qcross = madd(bracket(b[0],T[1]),bracket(T[0],b[1]))
        polarized = madd(bracket(madd(T[0],b[0]),madd(T[1],b[1])),
                         mscale(-1,madd(bracket(*T),bracket(*b))))
        check(prefix+'_oneform_curvature_closure',skew(H,bracket(*T)))
        check(prefix+'_oneform_polarization',Qcross==polarized and skew(H,Qcross))
        records.append({'H':encode(H),'real_basis_count_before_rank':len(basis),
                        'sesquilinear_mutant_failures':mutant_failures,
                        'imaginary_trace_control':encode(tr_complex)})

    rows = matrix([[Q(x) for x in row] for row in inherited['normalized_matrix']])
    check('inherited_rows_shape',len(rows)==4 and all(len(row)==4 for row in rows))
    scales = [G(1,1),G(2,-1),G(-3,2),G(0,5)]
    scaled = [[s*x for x in row] for s,row in zip(scales,rows)]
    reduced,pivots = rref(scaled)
    check('complex_scaled_inherited_rows_rank4',pivots==[0,1,2,3])
    check('complex_scaled_rref_identity',reduced==matrix([[int(i==j) for j in range(4)] for i in range(4)]))
    product_scale = G(1)
    for s in scales:
        product_scale *= s
    check('independent_determinant_scaling',determinant(scaled)==product_scale*determinant(rows) and bool(determinant(scaled)))
    lost = [[G() for _ in row] if i==0 else row for i,row in enumerate(scaled)]
    check('zero_row_scale_mutant_rejected',len(rref(lost)[1])==3)
    outside = [scaled[0],scaled[0],scaled[2],scaled[2]]
    check('outside_only_rank2_mutant_rejected',len(rref(outside)[1])==2)
    imaginary_rows = mscale(I,rows)
    check('real_part_only_elimination_mutant_rejected',len(rref(imaginary_rows)[1])==4 and
          len(rref([[G(x.re) for x in row] for row in imaginary_rows])[1])==0)

    one,g,t = {(0,0):Q(1)},{(1,0):Q(1)},{(0,1):Q(1)}
    quadratic = padd(one,g,power(g,2))
    cubic = padd(pscale(2,one),pscale(-1,g))
    action = padd(pmul(quadratic,power(t,2)),pmul(cubic,power(t,3)))
    check('distortion_reference_action_zero',not substitute_t(action,{}))
    for axis in range(2):
        check(f'distortion_first_variation_{axis}_zero',not substitute_t(derivative(action,axis),{}))
    hessian = [[substitute_t(derivative(derivative(action,i),j),{}) for j in range(2)] for i in range(2)]
    check('distortion_metric_and_cross_blocks_zero',hessian[0]==[{},{}] and hessian[1][0]=={})
    check('distortion_TT_block',hessian[1][1]==pscale(2,quadratic))
    # In this second chart the second variable denotes A, and B(g)=2g.
    pullback = substitute_t(action,padd(t,pscale(-2,g)))
    reference = pscale(2,g)
    check('connection_chart_reference_action_zero',not substitute_t(pullback,reference))
    for axis in range(2):
        check(f'connection_chart_first_variation_{axis}_zero',not substitute_t(derivative(pullback,axis),reference))
    connection_hessian = [[substitute_t(derivative(derivative(pullback,i),j),reference)
                           for j in range(2)] for i in range(2)]
    expected = [[pscale(8,quadratic),pscale(-4,quadratic)],
                [pscale(-4,quadratic),pscale(2,quadratic)]]
    check('connection_chart_Hessian_chain_rule',connection_hessian==expected)
    check('joint_reference_tangent_radical',all(not padd(row[0],pscale(2,row[1])) for row in connection_hessian))
    check('fixed_A_metric_block_not_zero',bool(connection_hessian[0][0]))
    off_locus = pmul(g,t)
    check('pointwise_zero_coefficient_not_identical_mutant',substitute_t(off_locus,{})=={} and
          derivative(derivative(off_locus,0),1)==one)

    return {'schema':'gu-riemann-realform-transfer-certificate-v1','data_only':True,
        'probe_sha256':sha(Path(__file__).resolve()),
        'dependency_only_sha256':{name:sha(repo/name) for name in DEPENDENCIES},
        'dependency_policy':'Inherited K77 rows, classification and native certificate are bound as dependencies; their 317 checks are not rerun or counted as fresh checks.',
        'real_form_finite_controls':records,
        'inherited_row_adapter':{'rows':encode(rows),'nonzero_complex_scales':encode(scales),
            'scaled_rows':encode(scaled),'rref':encode(reduced),'determinant':encode(determinant(scaled)),
            'scale_scope':'abstract nonzero complex normalization controls, not measured K95 native coefficients'},
        'polynomial_chart_controls':{'variables':['g','T or A'],
            'distortion_action':polynomial_record(action),'connection_action':polynomial_record(pullback),
            'reference_connection':'A=2g','distortion_Hessian':[[polynomial_record(p) for p in row] for row in hessian],
            'connection_Hessian':[[polynomial_record(p) for p in row] for row in connection_hessian],
            'scope':'finite symbolic calibration of the written O(T^2) argument; not a newly proposed action'},
        'checks':checks,'check_count':len(checks),
        'written_theorem_scope':'For dimension14 real metric forms, full complex Dirac and full real u(H), a fixed real-linear Spin-equivariant Shiab with full-translation same-cubic unit endpoint annihilates injected algebraic Riemann curvature. The universal theorem follows by complexification and inherited K77 kernel inclusion, not by finite fixtures.',
        'reference_family_scope':'Conditional first bosonic template with induced spin-LC B(g,epsilon), zero matter and no other terms: its compatible zero-distortion family is stationary; family tangents lie in the Hessian radical. Metric blocks vanish in distortion coordinates, not necessarily at fixed A.',
        'not_run':['Inherited 317-check Clifford replay','Dense Dirac matrices or K95 witness reconstruction',
            'New representation/Hom census','New action or domain construction','Lean compilation',
            'PDE, physical quotient or source-wide proof'],
        'timing_policy':'Only ephemeral receipts include runtime and byte count.'}


def write_json(path, value):
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
        'seconds':time.monotonic()-started}
    if args.output:
        write_json(args.output,receipt)
    print(json.dumps(receipt,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
