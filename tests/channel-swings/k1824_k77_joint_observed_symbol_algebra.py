#!/usr/bin/env sage-python
"""K1824: full observed joint-symbol algebra on the corrected K77 carrier.

The rational primitive reconstruction and graph method are reused from K1822.
New joint-algebra identities are evaluated over QQ, hence over R. No source
action selection or physical quotient is asserted. Run with Sage's Python.
"""
from __future__ import annotations

import argparse
from copy import copy
import hashlib
import json
from math import lcm, gcd
from itertools import product
from collections import Counter
import time
from pathlib import Path

from sage.all import QQ, GF, block_matrix, block_diagonal_matrix, identity_matrix, matrix, zero_matrix, vector

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1824-k77-joint-observed-symbol-algebra.json"
OBS = (0, 7, 8, 9)
PRIMES = (1009, 1013)


def digest(m, rational=False):
    entries = [[int(i), int(j), str(v) if rational else int(v)]
               for (i, j), v in sorted(m.dict().items()) if v]
    payload = {"shape": [int(m.nrows()), int(m.ncols())], "entries": entries}
    return "sha256:" + hashlib.sha256(json.dumps(payload, separators=(",", ":"), sort_keys=True).encode()).hexdigest()


def tensor(factors):
    out = matrix(QQ, [[1]], sparse=True)
    for f in factors:
        out = out.tensor_product(f)
    return out


def sparse_block_inverse(m):
    """Invert disconnected bipartite support components, then verify globally."""
    n = m.nrows()
    assert m.ncols() == n
    adjacency = {j:set() for j in range(2*n)}
    for r,c in m.dict():
        adjacency[r].add(n+c)
        adjacency[n+c].add(r)
    seen, result, sizes = set(), {}, []
    for vertex in range(2*n):
        if vertex in seen:
            continue
        pending, component = [vertex], set()
        while pending:
            v = pending.pop()
            if v in component:
                continue
            component.add(v)
            pending.extend(adjacency[v]-component)
        seen.update(component)
        rows = sorted(v for v in component if v < n)
        cols = sorted(v-n for v in component if v >= n)
        assert len(rows) == len(cols) and rows
        inv = m.matrix_from_rows_and_columns(rows, cols).inverse()
        sizes.append(len(rows))
        for (r,c),v in inv.dict().items():
            result[cols[r],rows[c]] = v
    out = matrix(QQ,n,n,result,sparse=True)
    assert out*m == identity_matrix(QQ,n,sparse=True) == m*out
    return out, sizes


def build_family():
    checks = {}
    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)
    i2 = identity_matrix(QQ, 2, sparse=True)
    s1 = matrix(QQ, [[0, 1], [1, 0]], sparse=True)
    s3 = matrix(QQ, [[1, 0], [0, -1]], sparse=True)
    eps = matrix(QQ, [[0, 1], [-1, 0]], sparse=True)
    gs = [tensor([s3] * j + [v] + [i2] * (6-j))
          for v in (s1, eps) for j in range(7)]
    eta = [1]*7 + [-1]*7
    I = identity_matrix(QQ, 128, sparse=True)
    Z = zero_matrix(QQ, 128, 128, sparse=True)
    volume = I
    for g in gs:
        volume = volume*g
    check("all_Clifford_relations", all(gs[i]*gs[j]+gs[j]*gs[i] == (2*eta[i]*I if i == j else Z)
                                               for i in range(14) for j in range(i, 14)))
    pp, pm = (I+volume)/2, (I-volume)/2
    W, Wi = pp+2*pm, pp+pm/2
    S = 11*pp/24+11*pm/12
    check("chirality_weights_inverse", W*Wi == I)

    def blocks(rows):
        return block_matrix(QQ, rows, sparse=True)

    def symbol(k):
        rows = []
        for r in range(14):
            rows.append([eta[r]*gs[r]*gs[k]*gs[c]*W
                         if r != k and c not in (r, k) else Z for c in range(14)]
                        + [I if r == k else Z])
        rows.append([-eta[c]*I if c == k else Z for c in range(14)] + [gs[k]*S])
        return blocks(rows)

    # Exact elimination of D0, derived in the accompanying proof.
    inverse_rows = [[Z]*15 for _ in range(15)]
    inverse_rows[0][0], inverse_rows[0][14] = gs[0]*S, -I
    inverse_rows[14][0] = I
    for r in range(1, 14):
        for c in range(1, 14):
            inverse_rows[r][c] = Wi*eta[r]*gs[r]*gs[0]*gs[c]*(QQ(1)/12-(1 if r == c else 0))
    D0, D0i = symbol(0), blocks(inverse_rows)
    I1920 = identity_matrix(QQ, 1920, sparse=True)
    check("rational_time_right_inverse", D0*D0i == I1920)
    check("rational_time_left_inverse", D0i*D0 == I1920)

    observation = blocks([[I if r == s else Z for r in range(15)] for s in OBS+(14,)])
    gamma = blocks([[eta[j]*gs[j] for j in OBS]])
    I640 = identity_matrix(QQ, 640, sparse=True)
    seed = blocks([[I if r == 14 else Z] for r in range(15)])
    evolutions = {k:D0i*symbol(k) for k in (7,8,9)}
    words = [seed, evolutions[7]*seed, evolutions[8]*seed, evolutions[9]*seed,
             evolutions[7]*evolutions[8]*seed, evolutions[7]*evolutions[9]*seed,
             evolutions[8]*evolutions[9]*seed, evolutions[7]*evolutions[8]*evolutions[9]*seed]
    span = block_matrix(QQ, 1, 8, [words], sparse=True)
    observed_span = observation*span
    span_denominator = lcm(*(int(v.denominator()) for v in observed_span.dict().values()))
    check("rank_witness_denominators_invertible", gcd(span_denominator, 1009) == 1)
    pivots = observed_span.change_ring(GF(1009)).pivots()
    rank_lower = len(pivots)
    check("good_reduction_rank_lower_640", rank_lower == 640)
    basis = span.matrix_from_columns(pivots)
    observed_inverse, inverse_block_sizes = sparse_block_inverse(observation*basis)
    lift = basis*observed_inverse
    check("observation_lift_identity", observation*lift == I640)
    check("seed_in_graph", lift*observation*seed == seed)
    for k,e in evolutions.items():
        check("rational_graph_invariant_"+str(k), lift*observation*e*lift == e*lift)
    check("all_words_in_graph", lift*observation*span == span)
    check("rational_word_span_rank_640", rank_lower == 640)

    trace_lift = blocks([[gs[j]/4] for j in OBS])
    check("gamma_trace_split", gamma*trace_lift == I)
    P = block_diagonal_matrix([identity_matrix(QQ, 512, sparse=True)-trace_lift*gamma, I], sparse=True)
    check("rational_corrected_projector", P*P == P and P.trace() == 512)
    reduced = observation*evolutions[7]*lift
    check("rational_observed_normal_involution", reduced*reduced == I640)
    A = P*reduced*P
    check("rational_compressed_endomorphism", P*A == A and A*P == A)
    family = [P*observation*evolutions[j]*lift*P for j in (7,8,9)]
    old = json.loads((ROOT/"lab/process/k1822-k77-rational-corrected-carrier.json").read_text())
    check("same_K1822_lift",digest(lift,True)==old["certificate"]["rational_matrices"]["lift"]["digest"])
    check("same_K1822_projector",digest(P,True)==old["certificate"]["rational_matrices"]["P"]["digest"])
    check("same_K1822_A7",digest(family[0],True)==old["certificate"]["rational_matrices"]["A"]["digest"])
    return P, family, checks, gs[0]


def independent_span(matrices, labels=None):
    """Exact incremental rational echelon, retaining original matrices."""
    basis, kept, rows = [], [], []
    if labels is None:
        labels = list(range(len(matrices)))
    for M, label in zip(matrices, labels):
        v = vector(QQ, M.list())
        for pivot, row in rows:
            if v[pivot]:
                v -= v[pivot]*row
        if not v:
            continue
        pivot = next(i for i,x in enumerate(v) if x)
        v /= v[pivot]
        basis.append(M); kept.append(label); rows.append((pivot,v))
    return basis, kept, rows


def generated_algebra(generators):
    n = generators[0].nrows()
    basis, words, rows = independent_span([identity_matrix(QQ,n)], [()])
    def reduce(M):
        v = vector(QQ,M.list())
        for pivot,row in rows:
            if v[pivot]:
                v -= v[pivot]*row
        return v
    index = 0
    while index < len(basis):
        for j,g in enumerate(generators):
            M = basis[index]*g
            v = reduce(M)
            if v:
                pivot = next(i for i,x in enumerate(v) if x)
                v /= v[pivot]
                rows.append((pivot,v));basis.append(M);words.append(words[index]+(j,))
        index += 1
    assert all(not reduce(M*g) for M in basis for g in generators)
    return basis,words,rows


def intertwiner_basis(source, target):
    n=source[0].nrows(); rows=[]
    for A,B in zip(source,target):
        for i in range(n):
            for j in range(n):
                row={}
                for k in range(n):
                    if A[k,j]: row[i*n+k]=row.get(i*n+k,0)+A[k,j]
                    if B[i,k]: row[k*n+j]=row.get(k*n+j,0)-B[i,k]
                rows.append(row)
    equations=matrix(QQ,len(rows),n*n,
        {(i,j):v for i,row in enumerate(rows) for j,v in row.items()},sparse=True)
    return [matrix(QQ,n,n,list(v)) for v in equations.right_kernel().basis()]


def entries(M):
    return {"shape":[int(M.nrows()),int(M.ncols())],
            "entries":[[int(i),int(j),str(v)] for (i,j),v in sorted(M.dict().items()) if v]}


def produce():
    P, family, checks, gamma0 = build_family()
    def check(name, condition):
        checks[name]=bool(condition)
        if not condition: raise AssertionError(name)
    n=P.nrows(); adjacency=[set() for _ in range(n)]
    for M in [P]+family:
        for (i,j),v in M.dict().items():
            if v: adjacency[i].add(j);adjacency[j].add(i)
    seen=set();components=[]
    for start in range(n):
        if start in seen: continue
        pending=[start];component=set()
        while pending:
            v=pending.pop()
            if v in component:continue
            component.add(v);pending.extend(adjacency[v]-component)
        seen.update(component);components.append(sorted(component))
    check("thirty_two_support_components",len(components)==32 and all(len(c)==20 for c in components))
    block_of={i:j for j,c in enumerate(components) for i in c}
    check("exact_full_offblock_zero",all(block_of[i]==block_of[j] for M in [P]+family for i,j in M.dict()))
    representatives=[];component_types=[];image_bases=[];image_data=[]
    for component in components:
        pb=P.matrix_from_rows_and_columns(component,component)
        cb=pb.matrix_from_columns(pb.pivots())
        rr=cb.transpose().pivots()
        li=cb.matrix_from_rows(rr).inverse()
        ab=[M.matrix_from_rows_and_columns(component,component) for M in family]
        reduced=[li*M.matrix_from_rows(rr)*cb for M in ab]
        check("image_basis_"+str(len(component_types)),
            cb.ncols()==16 and pb*cb==cb and all(M*cb==cb*B for M,B in zip(ab,reduced)))
        if reduced not in representatives: representatives.append(reduced)
        component_types.append(representatives.index(reduced))
        image_data.append((cb,rr,li))
        image_bases.append({"columns":list(map(int,pb.pivots())),"left_inverse_rows":list(map(int,rr))})
    check("four_types_eight_each",Counter(component_types)==Counter({0:8,1:8,2:8,3:8}))
    base=representatives[0]; I=identity_matrix(QQ,16)
    intertwiners=[]
    for i,target in enumerate(representatives):
        candidates=intertwiner_basis(base,target)
        # Deterministic first invertible exact solution. The certificate fails
        # rather than assuming a module equivalence if none is found.
        invertible=[T for T in candidates if T.det()]
        check("equivalent_type_"+str(i),bool(invertible))
        T=invertible[0]
        check("exact_intertwiner_"+str(i),all(T*A==B*T for A,B in zip(base,target)))
        intertwiners.append(T)
    central=intertwiner_basis(base,base)
    check("joint_commutant_dimension_two",len(central)==2)
    complex_structures=[J for J in central if J*J == -I]
    check("actual_complex_not_split_structure",bool(complex_structures))
    J=complex_structures[0]
    check("all_generators_commute_complex_structure",all(A*J==J*A for A in base))
    algebra,words,echelon=generated_algebra(base)
    check("joint_word_dimension_128",len(algebra)==128)
    check("every_word_complex_linear",all(M*J==J*M for M in algebra))
    # The real centralizer of a complex structure on R^16 has real dimension
    # 2*8^2=128. Inclusion plus exact independent dimension proves equality.
    # This is stronger than inferring semisimplicity from a commutant count.
    check("maximal_complex_matrix_algebra",len(algebra)==2*(16//2)**2)
    A=base[0]
    slow=576*(I-A*A)/575
    smallest=(I+24*A)*slow/2
    check("attained_rank_two_idempotent",smallest*smallest==smallest and smallest.rank()==2)
    sign=(-576*A**3+601*A)/25
    check("oriented_sign_involution",sign*sign==I and sign.trace()==0)
    comm_ranks=[int((g*sign-sign*g).rank()) for g in base]
    check("other_axes_violate_fixed_split",comm_ranks==[0,16,16])
    even=[(M+sign*M*sign)/2 for M in algebra]
    even_basis,even_labels,_=independent_span(even)
    check("split_preserving_subalgebra_dimension64",len(even_basis)==64)
    check("split_preserving_repair",all(M*sign==sign*M for M in even_basis))
    check("smallest_idempotent_survives_repair",smallest*sign==sign*smallest)
    # Exact polynomial in every real spatial covector, not sampled axes.
    quartic={}
    for word in product(range(3),repeat=4):
        powers=tuple(word.count(i) for i in range(3));M=I
        for j in word:M=M*base[j]
        quartic[powers]=quartic.get(powers,0)+576*M
    for i,j,k in product(range(3),repeat=3):
        powers=[0]*3;powers[i]+=1;powers[j]+=1;powers[k]+=2
        key=tuple(powers);quartic[key]=quartic.get(key,0)-577*base[i]*base[j]
    for i,j in product(range(3),repeat=2):
        powers=[0]*3;powers[i]+=2;powers[j]+=2
        key=tuple(powers);quartic[key]=quartic.get(key,0)+I
    check("all_spatial_direction_quartic_coefficients",len(quartic)==15 and all(M==0 for M in quartic.values()))
    changed=[base[0]+base[1],base[1]+base[2],base[2]]
    check("invertible_frame_recombination_recovers_generators",
          [changed[0]-changed[1]+changed[2],changed[1]-changed[2],changed[2]]==base)
    # Computational faults rather than only artifact assertions.
    bad=copy(J);bad[0,0]+=1
    check("planted_complex_structure_failure",bad*bad != -I)
    broken=copy(intertwiners[1]);broken[0,0]+=1
    check("planted_module_equivalence_failure",any(broken*A!=B*broken for A,B in zip(base,representatives[1])))
    bad_family=list(base);bad_family[1]=base[1]+I
    test=sum(bad_family)
    check("planted_directional_polynomial_failure",576*test**4-577*3*test**2+9*I != 0)
    # Reuse the explicit gamma0 internal-action plant from the Aug11 H640
    # typing probe. It is a contrary control, not a selected connection field.
    # O (I15 tensor gamma0) L = I5 tensor gamma0 follows from OL=I.
    jentries={}
    for component,kind,(cb,rr,li) in zip(components,component_types,image_data):
        T=intertwiners[kind]
        local=cb*T*J*T.inverse()*li
        for (i,j),v in local.dict().items():
            if v:jentries[component[i],component[rr[j]]]=v
    global_J=matrix(QQ,640,640,jentries,sparse=True)*P
    check("full_complex_structure_on_imP",global_J*global_J == -P)
    check("full_complex_structure_commutes_symbols",all(global_J*M==M*global_J for M in family))
    plant=P*block_diagonal_matrix([gamma0]*5,sparse=True)*P
    plant_commutator=plant*global_J-global_J*plant
    plant_rank=int(plant.rank());plant_commutator_rank=int(plant_commutator.rank())
    check("existing_lower_order_plant_breaks_joint_complex_structure",plant_commutator_rank>0)
    dependency_paths=["tests/channel-swings/k1822_k77_rational_corrected_carrier.py",
                      "lab/process/k1822-k77-rational-corrected-carrier.json",
                      "tests/channel-swings/selected_k77_h640_observation_pullback_bv_typing_probe.py",
                      "lab/process/selected-k77-h640-observation-pullback-bv-typing.json"]
    return {
        "schema_version":"1.0","result_id":"K1824-K77-JOINT-OBSERVED-SYMBOL-ALGEBRA",
        "created":"2026-10-20","status":"active_research","classification":"INTERNAL_STRUCTURAL_ONLY",
        "target_claim":"NONE-NOT-A-KILL",
        "scope":"Rational fixed K435/K1822 principal fixture on im(P); spatial symbol algebra at a fixed time covector, not an action-selected interaction or physical complex.",
        "dependencies":{p:"sha256:"+hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependency_paths},
        "certificate":{
            "checks":checks,"family_digests":[digest(M,True) for M in family],
            "support_components":components,"component_types":component_types,"image_bases":image_bases,
            "representation_dimension":16,"representation_multiplicity":32,
            "representative_generators":[entries(M) for M in base],
            "type_intertwiners":[entries(T) for T in intertwiners],"complex_structure":entries(J),
            "generated_dimension":len(algebra),"basis_words":[list(w) for w in words],
            "maximum_basis_word_length":max(map(len,words)),"basis_echelon_pivots":[int(p) for p,v in echelon],
            "smallest_rank_idempotent":entries(smallest),"fixed_sign_commutator_ranks":comm_ranks,
            "split_preserving_dimension":len(even_basis),"split_preserving_projected_word_indices":even_labels,
            "direction_polynomial_coefficients_checked":len(quartic),
            "existing_lower_order_plant":{"source":"Aug11 H640 typing probe, internal=I15 tensor gamma0",
                "compressed_formula":"P (I5 tensor gamma0) P", "compressed_rank":plant_rank,
                "complex_structure_commutator_rank":plant_commutator_rank,
                "compressed_digest":digest(plant,True),"new_source_coefficient":False,
                "historical_ambient_graph_leakage_rank":128,"complete_coupled_operator":False}},
        "conclusions":{
            "real_joint_algebra":"M_8(C), acting as 32 equivalent real 16-dimensional modules",
            "full_carrier_real_dimension":512,"single_normal_algebra_dimension":4,
            "joint_algebra_real_dimension":128,"sharp_nonzero_rank_minimum":64,
            "matrix_amplification_rank_divisor":64,"finite_homology_dimension_divisor":64,
            "fixed_split_subalgebra":"M_4(C) direct_sum M_4(C), repeated 32 times",
            "fixed_split_subalgebra_real_dimension":64,"fixed_split_sharp_nonzero_rank_minimum":64,
            "spatial_frame_basis_independence":True,"time_covector_independence_proved":False,
            "all_spatial_direction_identity":"576 A(n)^4-577 |n|^2 A(n)^2+|n|^4 I=0"},
        "claim_boundary":{"new_source_action_coefficients":False,"physical_state":False,
            "nonfactorized_KT_differential":False,"source_or_ledger_effect":"none","canon_effect":"none",
            "selected_element_from_generated_algebra":False,"arbitrary_interaction_excluded":False}}


def main():
    parser=argparse.ArgumentParser();parser.add_argument("--write",action="store_true");parser.add_argument("--check",action="store_true")
    args=parser.parse_args();start=time.monotonic();data=produce()
    if args.write:ARTIFACT.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n")
    if args.check:assert json.loads(ARTIFACT.read_text())==data,"certificate mismatch"
    print(json.dumps({"checks":len(data["certificate"]["checks"]),"algebra_dimension":128,"sharp_rank_minimum":64,
        "seconds":round(time.monotonic()-start,3),"artifact_written":args.write},sort_keys=True))

if __name__=="__main__":main()
