"""Independent signed-bit raw assembly for the fourteen-direction grade-one certificate."""
import hashlib
import json
from copy import deepcopy, copy
from pathlib import Path
from sage.all import QQ, matrix, identity_matrix, zero_matrix, block_matrix, diagonal_matrix, prod
from k1951_coordinated_zero_southeast_principal_probe import gamma, mat

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'lab/process/k1957-full-direction-grade-one.json'


def assemble(value):
    g = gamma(); eye = identity_matrix(QQ, 128, sparse=True)
    z = zero_matrix(QQ, 128, 128, sparse=True)
    vol = prod(g); W = (3 * eye - vol) / 2; Wi = (3 * eye + vol) / 4
    eta = [1] * 7 + [-1] * 7
    def D(k):
        return block_matrix([[eta[r] * g[r] * g[k] * g[c] * W if r != k and c not in (r, k) else z
                              for c in range(14)] + [eye if r == k else z] for r in range(14)] +
                            [[-eta[c] * eye if c == k else z for c in range(14)] + [z]], sparse=True)
    parts = [[z] * 15 for _ in range(15)]
    parts[0][14] = -eye; parts[14][0] = eye
    for r in range(1, 14):
        for c in range(1, 14):
            parts[r][c] = Wi * eta[r] * g[r] * g[0] * g[c] * (QQ(1) / 12 - (1 if r == c else 0))
    inv = block_matrix(parts, sparse=True); d0 = D(0)
    assert d0 * inv == identity_matrix(QQ, 1920), 'independent time inverse'
    rows = json.loads((ROOT / 'lab/process/k1951-coordinated-zero-southeast-principal.json').read_text())['blocks']
    J = matrix(QQ, 1920, 128, sparse=True)
    for b, row in enumerate(rows):
        js = mat(row['basis']) * mat(row['section'])
        for (i, j), v in js.dict().items():
            J[row['coordinates'][i], 4 * b + j] = v
    piv = J.transpose().pivots(); L = matrix(QQ, 128, 1920, sparse=True)
    small_inv = J.matrix_from_rows(piv).inverse()
    for j, p in enumerate(piv):
        L.set_column(p, small_inv.column(j))
    assert L * J == identity_matrix(QQ, 128), 'actual core coordinates'
    ds = {k: D(k) for k in range(14)}
    As = {k: inv * d for k, d in ds.items()}
    for n, k in enumerate([7, 8, 9]):
        C = block_matrix([[mat(rows[i]['quotient_generators'][n]) if i == j else zero_matrix(QQ, 4, 4)
                           for j in range(32)] for i in range(32)], sparse=True)
        assert ds[k] * J == d0 * J * C, 'independent actual principal restriction'
    for row in rows:
        h = mat(row['quotient_energy']); cs = list(map(mat, row['quotient_generators']))
        assert h.is_positive_definite() and all(h * c == c.transpose() * h for c in cs), 'stored positive principal energy'
    parity=diagonal_matrix(QQ,[1]*14+[-1],sparse=True).tensor_product(vol)
    pc=L*parity*J
    assert parity*J==J*pc and pc*pc==identity_matrix(QQ,128),'core parity'
    assert all(parity*d==-d*parity for d in ds.values()),'all14 odd symbols'
    assert all(parity*A==A*parity for A in As.values()),'all14 even evolutions'
    assert all(parity*identity_matrix(QQ,15,sparse=True).tensor_product(x)==-identity_matrix(QQ,15,sparse=True).tensor_product(x)*parity for x in g),'grade-one odd operators'
    def column(k, a, fault=None):
        generator = g[(a+1)%14] if fault == 'wrong_generator' else g[a]
        if fault == 'missing_connection': generator=0*generator
        slots=diagonal_matrix(QQ,[1]*14+[0],sparse=True) if fault=='missing_auxiliary' else identity_matrix(QQ,15,sparse=True)
        if fault=='wrong_covector':k=(k+1)%14
        V=As[k]*slots.tensor_product(generator)*J
        residual=V-J*(L*V)
        return [residual[i//128,i%128] for i in value['selected_rows']]
    B=matrix(QQ,[column(k,a) for k in range(14) for a in range(14)]).transpose()
    A=(d0*J).matrix_from_rows(list(range(1792,1920)))
    return B,column,A

def audit(v,B,A):
    assert mat(v['inverse'])*B==identity_matrix(QQ,196),'full196 leakage inverse'
    assert mat(v['auxiliary_complement_inverse'])*A==identity_matrix(QQ,128),'auxiliary complement inverse'
    assert v['rank']==v['parameter_count']==196 and v['induced_image_rank']==v['mass_image_rank']==0,'rank reports'
    assert mat(v['kernel']).nrows()==0 and v['arbitrary_auxiliary_parameter_count']==229376,'kernel and support dimensions'
    assert QQ(v['inverse_infinity_norm'])==max(sum(abs(x) for x in r) for r in mat(v['inverse']).rows()),'residual norm'

def metadata(v):
    assert v['result_id']=='K1957','identity'
    for p,h in v['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'pin'

if __name__=='__main__':
    v=json.loads(OUT.read_text());B,col,A=assemble(v);audit(v,B,A);metadata(v)
    print('PASS independent all14 exact baseline, inverse and auxiliary complement',flush=True)
    for fault in ['wrong_generator','missing_connection','missing_auxiliary','wrong_covector']:
        bad=copy(B);changed=False
        for j in range(196):
            values=col(j//14,j%14,fault)
            if values!=list(B.column(j)):
                bad.set_column(j,values);changed=True;break
        assert changed,'nontrivial mathematical fault'
        try:audit(v,bad,A)
        except AssertionError as err:assert str(err)=='full196 leakage inverse';print('CAUGHT',fault,str(err),flush=True)
        else:raise AssertionError('undetected '+fault)
    aa=copy(A);aa[0,0]+=1
    try:audit(v,B,aa)
    except AssertionError as err:assert str(err)=='auxiliary complement inverse';print('CAUGHT auxiliary map input',flush=True)
    else:raise AssertionError('undetected auxiliary input')
    for fault in ['identity','pin']:
        vv=deepcopy(v)
        if fault=='identity':vv['result_id']='bad'
        else:vv['inputs'][next(iter(vv['inputs']))]='bad'
        try:metadata(vv)
        except AssertionError as err:assert str(err)==fault
        else:raise AssertionError('undetected metadata fault')
    print('PASS five mathematical and two separate metadata faults',flush=True)
