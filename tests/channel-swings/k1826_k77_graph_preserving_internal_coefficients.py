#!/usr/bin/env sage-python
"""K1826: fixed-graph internal coefficients and their generated algebras.

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
ARTIFACT = ROOT / "lab/process/k1826-k77-graph-preserving-internal-coefficients.json"
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
    return P, family, checks, gs, lift, observation


def pauli_expand(M):
    """Exact signed-permutation/Walsh basis coordinates, no numerical fit."""
    assert M.nrows()==M.ncols()==128
    diagonals={}
    for (r,c),v in M.dict().items():
        diagonals.setdefault(int(r)^int(c),[QQ(0)]*128)[int(r)]=v
    out={}
    for x,v in diagonals.items():
        h=1
        while h<128:
            for k in range(0,128,2*h):
                for j in range(k,k+h):
                    a,b=v[j],v[j+h];v[j]=a+b;v[j+h]=a-b
            h*=2
        for z,c in enumerate(v):
            if c:out[x+128*z]=c/128
    return out


def parity(a): return int(a).bit_count()%2


def symplectic(a,b):
    return parity((a%128)&(b//128))^parity((b%128)&(a//128))


def produce():
    from k1824_k77_joint_observed_symbol_algebra import generated_algebra, intertwiner_basis, entries
    P,family,checks,gs,L,O=build_family()
    def check(name,c):
        checks[name]=bool(c)
        if not c:raise AssertionError(name)
    I128=identity_matrix(QQ,128,sparse=True)
    I640=identity_matrix(QQ,640,sparse=True)
    vol=I128
    for g in gs:vol=vol*g
    eta=[1]*7+[-1]*7
    transverse=[j for j in range(14) if j not in OBS]
    graph_blocks=[]
    for r in transverse:
        for c,s in enumerate(OBS):
            M=L[128*r:128*(r+1),128*c:128*(c+1)]
            check('graph_closed_formula_'+str(r)+'_'+str(s), M==-QQ(eta[r])/20*gs[r]*gs[s])
            e=pauli_expand(M)
            check('single_graph_monomial_'+str(r)+'_'+str(s),len(e)==1)
            mask,coefficient=next(iter(e.items()))
            graph_blocks.append({'ambient_slot':r,'observed_slot':s,'mask':mask,'coefficient':str(coefficient)})
        check('zero_form_no_hidden_graph_'+str(r),L[128*r:128*(r+1),512:640]==0)
    masks=[b['mask'] for b in graph_blocks]
    survivors=[m for m in range(16384) if all(symplectic(m,g)==0 for g in masks)]
    volume_expansion=pauli_expand(vol)
    vm,vc=next(iter(volume_expansion.items()))
    check('complete_uniform_commutant',survivors==[0,vm] and len(volume_expansion)==1)
    binary=matrix(GF(2),[[int(m>>j)&1 for j in range(14)] for m in masks])
    check('graph_even_algebra_binary_rank_13',binary.rank()==13)
    check('volume_involution',vol*vol==I128 and vol.trace()==0)
    V=identity_matrix(QQ,5,sparse=True).tensor_product(vol)
    Va=identity_matrix(QQ,15,sparse=True).tensor_product(vol)
    check('volume_full_graph_descent',Va*L==L*V)
    check('volume_corrected_reduction',V*P==P*V)
    VP=P*V*P
    check('uniform_chiral_rank256_each',((P+VP)/2).trace()==256 and ((P-VP)/2).trace()==256)
    G=identity_matrix(QQ,5,sparse=True).tensor_product(gs[0])
    Ga=identity_matrix(QQ,15,sparse=True).tensor_product(gs[0])
    check('gamma0_graph_leakage',Ga*L!=L*G)
    check('gamma0_corrected_nonpreservation',(I640-P)*G*P!=0)

    # Reuse support method, and prove intertwiners for the enlarged family.
    augmented=family+[VP]
    adjacency=[set() for _ in range(640)]
    for M in [P]+augmented:
        for (i,j),v in M.dict().items():
            if v:adjacency[i].add(j);adjacency[j].add(i)
    seen=set();components=[]
    for start in range(640):
        if start in seen:continue
        pending=[start];component=set()
        while pending:
            v=pending.pop()
            if v in component:continue
            component.add(v);pending.extend(adjacency[v]-component)
        seen.update(component);components.append(sorted(component))
    check('same_32_support_components',len(components)==32 and all(len(c)==20 for c in components))
    representatives=[];types=[]
    for component in components:
        pb=P.matrix_from_rows_and_columns(component,component)
        cb=pb.matrix_from_columns(pb.pivots());rr=cb.transpose().pivots()
        li=cb.matrix_from_rows(rr).inverse()
        blocks=[M.matrix_from_rows_and_columns(component,component) for M in augmented]
        reduced=[li*M.matrix_from_rows(rr)*cb for M in blocks]
        check('exact_image_restriction_'+str(len(types)),cb.ncols()==16 and all(M*cb==cb*B for M,B in zip(blocks,reduced)))
        if reduced not in representatives:representatives.append(reduced)
        types.append(representatives.index(reduced))
    intertwiners=[];volume_signs=[]
    for k,rep in enumerate(representatives):
        basis=intertwiner_basis(representatives[0][:3],rep[:3])
        T=next((B for B in basis if B.det()),None)
        check('equivalent_principal_module_'+str(k),T is not None and all(T*A==B*T for A,B in zip(representatives[0][:3],rep[:3])))
        positive=T*representatives[0][3]==rep[3]*T
        negative=T*representatives[0][3]==-rep[3]*T
        check('volume_sign_transport_'+str(k),positive!=negative)
        volume_signs.append(1 if positive else -1)
        intertwiners.append(entries(T))
    abasis,words,rows=generated_algebra(representatives[0][:3])
    cbasis=intertwiner_basis(representatives[0][:3],representatives[0][:3])
    smallI=identity_matrix(QQ,16)
    J=next(C for C in cbasis if C*C==-smallI)
    V0=representatives[0][3]
    check('full_complex16_algebra_dimension128',len(abasis)==128 and all(C*J==J*C for C in abasis))
    check('volume_per_module_complex_linear',V0*J==J*V0 and V0*V0==smallI)
    signed_multiplicities=Counter(volume_signs[k] for k in types)
    check('two_inequivalent_sixteen_copy_sectors',signed_multiplicities==Counter({1:16,-1:16}))
    check('augmented_types_really_inequivalent',len(intertwiner_basis(representatives[0],representatives[1]))==0)
    # V0 is in the full principal M8(C); diag(V0,V0)*diag(V0,-V0)
    # yields diag(I,-I). Its central projectors split the diagonal algebra
    # into two independently available copies of M8(C), total dimension256.
    sharp=(smallI+24*representatives[0][0])/2*576*(smallI-representatives[0][0]**2)/575
    check('sector_rank_two_idempotent',sharp*sharp==sharp and sharp.rank()==2)

    # A different-slot repair: arbitrary zero-form endomorphism descends.
    seed=zero_matrix(QQ,1920,128,sparse=True)
    for j in range(128):seed[14*128+j,j]=1
    j0=O*seed;q0=j0.transpose()
    check('zero_form_identity',L*j0==seed and P*j0==j0 and q0*j0==I128)
    M=zero_matrix(QQ,128,128,sparse=True);M[0,0]=1
    repair=seed*M*seed.transpose();r=q0
    observed=j0*M*q0
    check('rank_one_same_graph_repair',repair*L==L*observed and (I640-P)*observed*P==0 and observed.rank()==1)
    check('rank_one_outside_augmented_algebra',observed.rank()%32!=0)
    # Constant two-slot family: one-form Bpsi=aI+bvol, zero-form arbitrary Bnu.
    one=block_diagonal_matrix([vol]*14+[zero_matrix(QQ,128,128,sparse=True)],sparse=True)
    oneo=block_diagonal_matrix([vol]*4+[zero_matrix(QQ,128,128,sparse=True)],sparse=True)
    check('different_slot_volume_repair',one*L==L*oneo and oneo*P==P*oneo)
    check('corrected_one_form_halves192',((P*oneo*P)**2).trace()==384 and (P*oneo*P).trace()==0)
    column_bank=block_matrix(QQ,1,4,[[j0]+[A*j0 for A in family]],sparse=True)
    row_bank=block_matrix(QQ,4,1,[[q0]]+[[q0*A] for A in family],sparse=True)
    denominators=lcm(*(int(v.denominator()) for Mx in (column_bank,row_bank) for v in Mx.dict().values()))
    column_rank=int(column_bank.change_ring(GF(1009)).rank());row_rank=int(row_bank.change_ring(GF(1009)).rank())
    check('cyclicity_good_reduction',gcd(denominators,1009)==1)
    check('zero_form_column_cyclic',column_rank==512 and P*column_bank==column_bank)
    check('zero_form_row_cyclic',row_rank==512 and row_bank*P==row_bank)
    return {'schema_version':'1.0','result_id':'K1826-K77-GRAPH-PRESERVING-INTERNAL-COEFFICIENTS',
      'created':'2026-10-20','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY',
      'target_claim':'NONE-NOT-A-KILL','scope':'Constant normalized evolution endomorphisms on fixed rational H640 and corrected E512; not source-selected interactions.',
      'source_and_ledger_effect':'none',
      'certificate':{'checks':checks,'graph_blocks':graph_blocks,'graph_formula':'L_rs=-eta_r*gamma_r*gamma_s/20 for transverse r and observed s; hidden zero-form column zero',
        'graph_generator_binary_rank':int(binary.rank()),'uniform_commutant_masks':survivors,'volume_mask':vm,'volume_coefficient':str(vc),
        'uniform_internal_algebra':'R direct_sum R','uniform_internal_rank_unit':256,
        'augmented_algebra':'M8(C) direct_sum M8(C)','augmented_real_dimension':256,'augmented_sector_multiplicities':[16,16],'augmented_sharp_rank_unit':32,'volume_signs_by_type':volume_signs,'principal_complex_structure':entries(J),
        'component_types':types,'representatives':[[entries(M) for M in rep] for rep in representatives],
        'intertwiners':intertwiners,'word_basis':[list(w) for w in words],
        'different_slot_algebra':'R direct_sum R direct_sum M128(R)','different_slot_dimension':16386,'different_slot_rank_one_available':True,'different_slot_plus_principal_algebra':'M512(R)','cyclicity':{'prime':1009,'denominator_lcm':denominators,'column_rank':column_rank,'row_rank':row_rank,'words':['identity','A7','A8','A9']},
        'normalization':'C is evolution endomorphism; raw K=D0*C is a separately constructed coefficient, not source-owned',
        'reused_inputs':{'K1822':'rational primitive fixture and invariant graph method','K1824':'support module method and joint principal algebra','K614':'source-zero-form injection; no selected value or Riesz return'},
        'scientific_ceiling':'No selected action, stationary odd background, degree differential, barred adjoint, physical form or common domain; no claim-status change.'}}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');parser.add_argument('--check',action='store_true')
    args=parser.parse_args();start=time.monotonic();result=produce()
    if args.write:ARTIFACT.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    if args.check:assert result==json.loads(ARTIFACT.read_text()),'saved artifact differs'
    checks=result['certificate']['checks']
    print(json.dumps({'checks_passed':sum(checks.values()),'checks_total':len(checks),'seconds':time.monotonic()-start,'write':args.write,'check':args.check}))

if __name__=='__main__':main()
