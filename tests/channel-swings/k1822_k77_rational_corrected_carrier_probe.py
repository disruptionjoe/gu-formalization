#!/usr/bin/env sage-python
"""Independent small-matrix controls for K1822's algebraic proof transfers.

Does not import the producer. Direct inversion in smaller Clifford modules
tests the elimination formula; rational conjugates and a Jordan counterfeit
test the semisimple spectral argument. These are not a second reconstruction
of the full physical fixture.
"""
import json
from copy import copy
from pathlib import Path
from sage.all import QQ, block_matrix, identity_matrix, matrix, zero_matrix

ROOT = Path(__file__).resolve().parents[2]


def kron(fs):
    out = matrix(QQ, [[1]])
    for f in fs:
        out = out.tensor_product(f)
    return out


def inverse_controls():
    count = 0
    i2 = identity_matrix(QQ,2)
    pauli = matrix(QQ,[[0,1],[1,0]])
    parity = matrix(QQ,[[1,0],[0,-1]])
    skew = matrix(QQ,[[0,1],[-1,0]])
    for n in (2,3):
        dim, nv = 2**n, 2*n
        gs = [kron([parity]*j+[last]+[i2]*(n-j-1)) for last in (pauli,skew) for j in range(n)]
        eta = [1]*n+[-1]*n
        I,Z = identity_matrix(QQ,dim),zero_matrix(QQ,dim)
        for weight in (QQ(1),QQ(3)/2):
            W=weight*I
            S=QQ(5)/7*I
            source = [[eta[r]*gs[r]*gs[0]*gs[c]*W if r != 0 and c not in (r,0) else Z
                       for c in range(nv)]+[I if r == 0 else Z] for r in range(nv)]
            source.append([-I if c == 0 else Z for c in range(nv)]+[gs[0]*S])
            D=block_matrix(QQ,source)
            rows=[[Z]*(nv+1) for _ in range(nv+1)]
            rows[0][0],rows[0][nv],rows[nv][0]=gs[0]*S,-I,I
            for r in range(1,nv):
                for c in range(1,nv):
                    rows[r][c]=eta[r]/weight*gs[r]*gs[0]*gs[c]*(QQ(1)/(nv-2)-(1 if r==c else 0))
            inverse=block_matrix(QQ,rows)
            assert inverse == D.inverse() # independent dense exact elimination
            bad=copy(inverse);bad[dim,dim]+=1
            assert D*bad != identity_matrix(QQ,(nv+1)*dim)
            count+=1
    return count


def spectral_controls():
    roots=[QQ(0),QQ(1),QQ(-1),QQ(1)/24,QQ(-1)/24]
    diagonal=matrix.diagonal(roots)
    p=matrix.diagonal([0,1,1,1,1])
    change=matrix(QQ,[[1,1,0,0,0],[0,1,2,0,0],[0,0,1,3,0],[0,0,0,1,4],[0,0,0,0,1]])
    A=change*diagonal*change.inverse();P=change*p*change.inverse()
    assert 576*A**4-577*A**2+P == 0
    # Independent Lagrange interpolation, not the producer fast/slow formula.
    projections=[]
    I=identity_matrix(QQ,5)
    for lam in roots[1:]:
        projector=P
        for other in roots[1:]:
            if other != lam:
                projector=projector*(A-other*P)/(lam-other)
        assert projector**2==projector and projector.trace()==1 and A*projector==lam*projector
        projections.append(projector)
    assert sum(projections)==P
    assert all(x*y==0 for i,x in enumerate(projections) for j,y in enumerate(projections) if i!=j)
    # A defective repeated root cannot be justified by eigenvalues alone.
    jordan=matrix(QQ,[[1,1],[0,1]])
    assert 576*jordan**4-577*jordan**2+identity_matrix(QQ,2) != 0
    return 4


def main():
    inverses=inverse_controls();spectral=spectral_controls()
    data=json.loads((ROOT/"lab/process/k1822-k77-rational-corrected-carrier.json").read_text())
    cert=data["certificate"]
    assert cert["rational_spectral_multiplicities"]==[192,192,64,64]
    assert len(cert["checks"])==29 and all(cert["checks"].values())
    assert cert["checks"]["planted_wrong_graph_rejected"]
    assert cert["checks"]["planted_two_prime_invisible_error_rejected"]
    assert not any(data["claim_boundary"][k] for k in
                   ("new_source_action_coefficients","physical_state","nonfactorized_KT_differential","Euclidean_ellipticity"))
    print(f"PASS: {inverses} independent exact inverse controls and coefficient faults; {spectral} Lagrange spectral projectors; Jordan counterfeit rejected; native boundaries checked")


if __name__=="__main__":
    main()
