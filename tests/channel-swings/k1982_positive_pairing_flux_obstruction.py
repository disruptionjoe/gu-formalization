"""Exact global trace/flux certificate on the frozen raw equation."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
import sympy as sp
from k1976_general_pairing_transport import setup,enc,norm
from k1970_weighted_adjoint_mass_completion_probe import plus,product,transpose
from k1979_multicoordinate_symmetric_pairing import right
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1982-positive-pairing-flux-obstruction.json'
def sym(A):return {ij:v/2 for ij,v in plus(A,transpose(A)).items()}
def rstar(Y,J,T,O,sign):
    out={}
    for k in range(14):out=plus(out,product(product(O[k],Y),transpose(J[k])),F(1 if k<7 else -1))
    return plus(out,product(Y,transpose(T)),-sign)
def produce():
    I,V,J,T,inv,O=setup();old=json.loads((ROOT/'lab/process/k1976-general-pairing-transport.json').read_text());out=[]
    for fam in old['families']:
        sign=fam['sign'];S={(i,j):F(v) for i,j,v in fam['permutation']};basis=[I,V,S,product(V,S)]
        A=sp.Matrix([[sp.Rational(x) for x in r] for r in fam['reduced_columns']]).T
        coeff=[F(x) for x in A.T.inv()*sp.Matrix([1,0,0,0])];X={}
        for x,b in zip(coeff,basis):X=plus(X,b,x)
        Y=product(X,transpose(inv))
        assert rstar(Y,J,T,O,sign)==I,'full adjoint trace identity, not only reduced projection'
        C=[sym({ij:(1 if k<7 else -1)*v for ij,v in product(Y,transpose(J[k])).items()}) for k in range(14)]
        bounds=[norm(c) for c in C];bound=sum(bounds);assert bound>0
        # The same certificate applies to every symmetric matrix and every PSD field.
        # Check each symmetric coordinate of R*Y=I, including all offdiagonals.
        count=128*129//2
        jets=json.loads((ROOT/'lab/process/k1979-multicoordinate-symmetric-pairing.json').read_text())['families'][0 if sign==-1 else 1]
        decode=lambda a:{(i,j):F(v) for i,j,v in a}
        compatibility=[]
        for h in map(decode,jets['identity_first_jets']):
            rhs=right(h,J,T,O,sign)
            compatibility.append([str(sum(v*rhs.get(ij,F(0)) for ij,v in decode(z).items())) for z in jets['cokernel']])
        assert all(v=='0' for row in compatibility for v in row),'canonical jets satisfy differentiated value constraints'
        out.append(dict(sign=sign,differentiated_value_constraints=compatibility,reduced_dual_coefficients=list(map(str,coeff)),dual=enc(Y),flux_matrices=[enc(c) for c in C],row_norm_bounds=list(map(str,bounds)),euclidean_flux_bound=str(bound),symmetric_coordinate_identities=count))
    return dict(result_id='K1982',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',families=out,scope='Fixed real symmetric raw-pairing PDE on all14 coordinates: trace divergence identity, no nonzero periodic PSD solution, exponential volume growth for nonzero global PSD solutions, hence no bounded or polynomial-growth PSD solution. Local existence and unbounded positive solutions remain open.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['tests/channel-swings/k1976_general_pairing_transport.py','lab/process/k1976-general-pairing-transport.json','lab/process/k1979-multicoordinate-symmetric-pairing.json']})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=produce()
    if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert r==json.loads(OUT.read_text())
    print('PASS K1982',[(x['sign'],x['euclidean_flux_bound']) for x in r['families']])
