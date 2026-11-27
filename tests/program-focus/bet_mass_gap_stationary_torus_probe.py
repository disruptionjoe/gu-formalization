#!/usr/bin/env python3
"""Exact finite controls for the stationary flat-torus MG1 theorem.

This checks off-shell covariant-jet identities, positive compact SU2 Fourier
fixtures, normalization and planted failures. It does not search for or
classify stationary backgrounds. The inherited flat-PS result is dependency
custody only, not a freshly executed census. Standard library only.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import argparse
import hashlib
import json
import sys
import time

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
CERT = 'lab/process/bet-mass-gap-stationary-torus-certificates.json'
DEPENDENCIES = (
    'explorations/conditional-build/bet-mass-gap-pati-salam-holonomy-2026-11-25.md',
    'tests/program-focus/bet_mass_gap_pati_salam_probe.py',
    'lab/process/bet-mass-gap-pati-salam-holonomy.json',
    'explorations/conditional-build/bet-mass-gap-stability-topology-2026-11-24.md',
    'explorations/conditional-build/signature-generic-cartan-ward-compose-2026-08-08.md',
)
ZERO = (Q(0), Q(0))
ONE = (Q(1), Q(0))


def require(value, message):
    if not value:
        raise AssertionError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def cadd(a, b):
    return a[0]+b[0], a[1]+b[1]


def cmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def cconj(a):
    return a[0], -a[1]


def clean(field):
    return {key: value for key, value in field.items() if value != ZERO}


def add(*fields):
    out = {}
    for field in fields:
        for key, value in field.items():
            out[key] = cadd(out.get(key, ZERO), value)
    return clean(out)


def scale(value, field):
    factor = value if isinstance(value, tuple) else (Q(value), Q(0))
    return clean({key: cmul(factor, entry) for key, entry in field.items()})


def unit(color):
    return {((0,0,0), color): ONE}


def wave(color, mode, sine=False):
    negative = tuple(-x for x in mode)
    if sine:
        return {(tuple(mode), color): (Q(0), Q(-1,2)),
                (negative, color): (Q(0), Q(1,2))}
    return {(tuple(mode), color): (Q(1,2), Q(0)),
            (negative, color): (Q(1,2), Q(0))}


def partial(axis, field):
    return clean({key: cmul((Q(0), Q(key[0][axis])), value) for key, value in field.items()})


def epsilon(a, b, c):
    if len({a,b,c}) != 3:
        return 0
    return 1 if (a,b,c) in ((0,1,2),(1,2,0),(2,0,1)) else -1


def bracket(left, right):
    out = {}
    for (k, a), x in left.items():
        for (l, b), y in right.items():
            if a == b:
                continue
            c = 3-a-b
            value = cmul(x, y)
            key = (tuple(v+w for v,w in zip(k,l)), c)
            signed = (epsilon(a,b,c)*value[0], epsilon(a,b,c)*value[1])
            out[key] = cadd(out.get(key, ZERO), signed)
    return clean(out)


def covariant(A, axis, field):
    return add(partial(axis, field), bracket(A[axis], field))


def curvature(A):
    return [[add(partial(i,A[j]), scale(-1,partial(j,A[i])), bracket(A[i],A[j]))
             for j in range(3)] for i in range(3)]


def equation(A, F):
    return [add(*(covariant(A,j,F[j][i]) for j in range(3))) for i in range(3)]


def dstar(A, a):
    return scale(-1,add(*(covariant(A,i,a[i]) for i in range(3))))


def exterior_covariant(A, a):
    return [[add(covariant(A,i,a[j]), scale(-1,covariant(A,j,a[i])))
             for j in range(3)] for i in range(3)]


def delta_equation(A, F, a, omit_connection_variation=False):
    da = exterior_covariant(A,a)
    return [add(*(add(covariant(A,j,da[j][i]),
                     {} if omit_connection_variation else bracket(a[j],F[j][i]))
                  for j in range(3))) for i in range(3)]


def coulomb_operator(A, F, a, omit_curvature=False):
    return [add(*(add(scale(-1,covariant(A,j,covariant(A,j,a[i]))),
                     {} if omit_curvature else scale(-2,bracket(F[i][j],a[j])))
                  for j in range(3))) for i in range(3)]


def inner(left, right):
    total = ZERO
    for key, value in left.items():
        total = cadd(total,cmul(cconj(value),right.get(key,ZERO)))
    require(total[1] == 0, 'real L2 pairing on Fourier-conjugate fields')
    return total[0]


def norm2(field):
    return inner(field,field)


def real_field(field):
    return all(field.get((tuple(-x for x in k), color),ZERO) == cconj(value)
               for (k,color),value in field.items())


def at_origin(field):
    out = [ZERO]*3
    for (_, color), value in field.items():
        out[color] = cadd(out[color],value)
    require(all(value[1] == 0 for value in out), 'real origin evaluation')
    return [value[0] for value in out]


def record(field):
    return [[list(k),color,str(value[0]),str(value[1])] for (k,color),value in sorted(field.items())]


# Sparse formal covariant-jet algebra. Antisymmetry is canonicalized, while
# differentiated Bianchi and [D_j,D_k]F=[F_jk,F] are explicit relations.
def formal_add(*terms):
    out = {}
    for term in terms:
        for key, coefficient in term.items():
            out[key] = out.get(key,0)+coefficient
    return {key: coefficient for key,coefficient in out.items() if coefficient}


def formal_scale(c, term):
    return {key: c*v for key,v in term.items() if c*v}


def oriented(i,j):
    return ((i,j),1) if i<j else (((j,i),-1) if j<i else (None,0))


def jet(derivatives,i,j):
    pair, sign = oriented(i,j)
    return {('D',tuple(derivatives),pair):sign} if sign else {}


def formal_bracket(i,j,k,l):
    left,a = oriented(i,j)
    right,b = oriented(k,l)
    if not a*b or left == right:
        return {}
    if left > right:
        left,right = right,left
        a = -a
    return {('bracket',left,right):a*b}


def formal_identity_records(check):
    records = []
    for k,i in product(range(3),repeat=2):
        original = {}
        relations = {}
        for j in range(3):
            # delta E_i(i_k F)-D_k E_i, expanded without using stationarity.
            original = formal_add(original, formal_bracket(k,j,j,i), jet((j,j),k,i),
                                 formal_scale(-1,jet((j,i),k,j)), formal_scale(-1,jet((k,j),j,i)))
            bianchi = formal_add(jet((j,j),k,i),formal_scale(-1,jet((j,i),k,j)),
                                 formal_scale(-1,jet((j,k),j,i)))
            commutator = formal_add(jet((j,k),j,i),formal_scale(-1,jet((k,j),j,i)),
                                    formal_scale(-1,formal_bracket(j,k,j,i)))
            relations = formal_add(relations,bianchi,commutator)
        remainder = formal_add(original,formal_scale(-1,relations))
        check(f'formal_offshell_deltaE_{k}_{i}', not remainder)
        records.append({'k':k,'i':i,'expanded_terms':len(original),
                        'Bianchi_and_commutator_relation_terms':len(relations),'remainder':[]})
    for k in range(3):
        div = formal_add(*(formal_scale(-1,jet((i,),k,i)) for i in range(3)))
        E = formal_add(*(jet((i,),i,k) for i in range(3)))
        check(f'formal_dstar_equals_E_{k}',div == E)
    return records


def build_certificate(repo):
    checks = {}
    def check(name, value):
        checks[name] = bool(value)
        require(value,name)
    formal = formal_identity_records(check)
    for a,b,c in product(range(3),repeat=3):
        jacobi = add(bracket(unit(a),bracket(unit(b),unit(c))),
                     bracket(unit(b),bracket(unit(c),unit(a))),
                     bracket(unit(c),bracket(unit(a),unit(b))))
        check(f'compact_su2_Jacobi_{a}_{b}_{c}',not jacobi)
    fixtures = [
        ('flat_zero',[{}, {}, {}]),
        ('flat_commuting',[unit(0),scale(Q(2,3),unit(0)),scale(-2,unit(0))]),
        ('constant_noncommuting',[unit(0),unit(1),unit(2)]),
        ('periodic_nonstationary',[
            add(unit(0),scale(Q(2,3),wave(1,(0,1,0)))),
            add(unit(1),scale(Q(3,5),wave(2,(0,0,1),True))),
            add(unit(2),scale(Q(4,7),wave(0,(1,0,0),True)))])]
    fixture_records = []
    for label,A in fixtures:
        F = curvature(A)
        E = equation(A,F)
        check(label+'_real_connection',all(real_field(x) for x in A))
        check(label+'_real_curvature',all(real_field(F[i][j]) for i,j in product(range(3),repeat=2)))
        check(label+'_curvature_antisymmetry',all(F[i][j] == scale(-1,F[j][i]) for i,j in product(range(3),repeat=2)))
        check(label+'_covariant_Bianchi',all(not add(covariant(A,i,F[j][k]),covariant(A,j,F[k][i]),covariant(A,k,F[i][j]))
              for i,j,k in product(range(3),repeat=3)))
        Fnorm = sum(norm2(F[i][j]) for i,j in combinations(range(3),2))
        contractions = [[F[k][i] for i in range(3)] for k in range(3)]
        norms = [sum(norm2(x) for x in a) for a in contractions]
        check(label+'_norm_sum_twice_twoform_norm',sum(norms)==2*Fnorm)
        row_records = []
        for k,a in enumerate(contractions):
            de = delta_equation(A,F,a)
            dkE = [covariant(A,k,x) for x in E]
            check(f'{label}_dstar_equals_E_{k}',dstar(A,a)==E[k])
            check(f'{label}_offshell_deltaE_equals_DkE_{k}',de==dkE)
            da = exterior_covariant(A,a)
            check(f'{label}_linearized_curvature_equals_DkF_{k}',all(da[j][i] == covariant(A,k,F[j][i])
                  for j,i in product(range(3),repeat=2)))
            check(f'{label}_covariant_commutator_{k}',all(
                add(covariant(A,j,covariant(A,k,F[j][i])),scale(-1,covariant(A,k,covariant(A,j,F[j][i]))))
                == bracket(F[j][k],F[j][i]) for j,i in product(range(3),repeat=2)))
            K = coulomb_operator(A,F,a)
            general_K = [add(scale(-1,de[i]),covariant(A,i,dstar(A,a))) for i in range(3)]
            check(f'{label}_K_minus_deltaE_plus_Ddstar_{k}',K==general_K)
            q = sum(norm2(da[i][j])+2*inner(F[i][j],bracket(a[i],a[j]))
                    for i,j in combinations(range(3),2))
            hessian_pair = -sum(inner(a[i],de[i]) for i in range(3))
            check(f'{label}_quadratic_energy_normalization_{k}',q==hessian_pair)
            row_records.append({'k':k,'norm_squared':str(norms[k]),'quadratic_energy':str(q),
                                'deltaE_nonzero_components':sum(bool(x) for x in de),
                                'Coulomb_defect_squared':str(norm2(dstar(A,a)))})
        if Fnorm == 0:
            check(label+'_zero_curvature_supplies_no_contraction_witness',not any(norms))
        else:
            check(label+'_wrong_single_count_norm_rejected',sum(norms)!=Fnorm)
            check(label+'_fixture_not_a_stationary_background',any(E))
            missing_term = [delta_equation(A,F,a,True) for a in contractions]
            check(label+'_omit_connection_variation_rejected',any(
                missing_term[k] != [covariant(A,k,x) for x in E] for k in range(3)))
            check(label+'_omit_stationarity_for_Jacobi_rejected',any(any(delta_equation(A,F,a)) for a in contractions))
            check(label+'_omit_Coulomb_for_K_minus_deltaE_rejected',any(
                coulomb_operator(A,F,a) != [scale(-1,x) for x in delta_equation(A,F,a)] for a in contractions))
            check(label+'_omit_curvature_term_rejected',any(
                coulomb_operator(A,F,a,True) != coulomb_operator(A,F,a) for a in contractions))
        point = next(((i,j,c,x) for i,j in combinations(range(3),2)
                      for c,x in enumerate(at_origin(F[i][j])) if x),None)
        independence = None
        if point:
            i,j,c,x = point
            matrix = [[at_origin(contractions[k][component])[c] for k in (i,j)] for component in (i,j)]
            det = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
            check(label+'_two_point_component_readouts',matrix==[[Q(0),-x],[x,Q(0)]])
            check(label+'_two_contractions_independent',det==x*x and det>0)
            duplicated = [[row[0], row[0]] for row in matrix]
            duplicate_det = duplicated[0][0]*duplicated[1][1]-duplicated[0][1]*duplicated[1][0]
            check(label+'_duplicate_contraction_fails_rank2',duplicated != matrix and duplicate_det == 0)
            independence={'axes':[i,j],'color':c,'Fij_at_origin':str(x),
                          'readout_matrix':[[str(y) for y in row] for row in matrix],
                          'determinant':str(det)}
        phi = add(wave(2,(1,1,0)),wave(1,(0,0,1),True))
        gauge = [covariant(A,i,phi) for i in range(3)]
        for k,a in enumerate(contractions):
            check(f'{label}_periodic_gauge_integration_by_parts_{k}',
                  sum(inner(a[i],gauge[i]) for i in range(3))==inner(dstar(A,a),phi))
        gauge_norm=sum(norm2(x) for x in gauge)
        check(label+'_positive_gauge_norm',gauge_norm>0)
        check(label+'_nonzero_gauge_not_Coulomb',inner(dstar(A,gauge),phi)==gauge_norm)
        if label == 'constant_noncommuting':
            check('constant_noncommuting_exact_E_minus2A',E==[scale(-2,x) for x in A])
        fixture_records.append({'id':label,'connection':[record(x) for x in A],
            'curvature_sha256':canonical_sha([[record(x) for x in row] for row in F]),
            'equation_sha256':canonical_sha([record(x) for x in E]),
            'curvature_twoform_norm_squared':str(Fnorm),'contractions':row_records,
            'point_independence':independence,'stationary':not any(E),
            'nonflat':Fnorm>0,'role':'finite identity control; no nonflat stationary existence assertion'})
    return {'schema':'gu-stationary-torus-certificate-v1','data_only':True,
        'probe_sha256':sha(Path(__file__).resolve()),
        'dependency_only_sha256':{name:sha(repo/name) for name in DEPENDENCIES},
        'dependency_policy':'The flat PS classification and its probes are authenticated dependencies only; none is rerun or counted as a fresh PASS.',
        'conventions':{'space':'fixed flat T3, period2pi in finite Fourier controls; arbitrary periods in the written theorem',
            'Lie_carrier':'real compact su2 with [T_a,T_b]=epsilon_abc T_c and positive orthonormal invariant pairing for finite controls',
            'energy':'(1/2) integral sum_i<j |Fij|^2',
            'E_i':'sum_j D_j F_ji; energy gradient is -E',
            'a_i_k':'F_ki; dstar a=-sum_i D_i a_i=E_k',
            'off_shell':'delta E_i(i_k F)=D_k E_i',
            'K_Coulomb':'-sum_j D_jD_j a_i-2 sum_j [Fij,a_j]',
            'general_K':'K_Coulomb a=-delta E(a)+D(dstar a)',
            'q':'||d_A a||^2+2<F,a wedge a>=-<a,delta E(a)>',
            'L2_normalization':'Fourier Parseval mean over T3; multiply by torus volume for unnormalized integrals'},
        'formal_covariant_jet_records':formal,'fixtures':fixture_records,
        'checks':checks,'check_count':len(checks),
        'written_consequences':'At a smooth stationary nonflat connection, at least two global contractions i_kF are independent Coulomb Jacobi fields and independent modulo infinitesimal gauge. Smoothness/compact T3 supplies the H2 domain; this bundle/PDE/domain theorem is a separately reviewed written argument.',
        'flat_PS_composition':'Combining the new nonflat theorem with the inherited flat-PS classification excludes a strictly positive full quadratic gap for every smooth static source-free stationary connection in that same compact PS flat-T3 category.',
        'scope_limits':['No stationary background census or existence search','No claim that every compact group has gapless flat bundles','Flat twisted SO3 positive control remains valid','No full nonlinear quotient or quantum gap theorem','No source-native GU or bet-wide verdict'],
        'not_run':['Old PS holonomy census','Full operator construction or spectral computation','Native indefinite/GU transfer','Lean compilation','Global bundle or PDE formalization'],
        'timing_policy':'Runtime and certificate byte count appear in ephemeral receipts, not this deterministic certificate.'}


def write_json(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_suffix(path.suffix+'.new')
    temporary.write_text(json.dumps(value,indent=2,sort_keys=True)+'\n')
    temporary.replace(path)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=ROOT)
    mode=parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write-certificate',action='store_true')
    mode.add_argument('--verify',action='store_true')
    parser.add_argument('--certificate',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args();started=time.monotonic();repo=args.repo.resolve()
    path=args.certificate or repo/CERT
    actual=build_certificate(repo)
    if args.write_certificate:
        write_json(path,actual)
    else:
        require(json.loads(path.read_text())==actual,'exact frozen certificate equality')
    receipt={'passed':True,'mode':'write-certificate' if args.write_certificate else 'verify',
        'probe_sha256':actual['probe_sha256'],'certificate_sha256':sha(path),
        'certificate_bytes':path.stat().st_size,'checks':actual['check_count'],
        'formal_offshell_components':len(actual['formal_covariant_jet_records']),
        'fixtures':len(actual['fixtures']),'seconds':time.monotonic()-started}
    if args.output:
        write_json(args.output,receipt)
    print(json.dumps(receipt,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
