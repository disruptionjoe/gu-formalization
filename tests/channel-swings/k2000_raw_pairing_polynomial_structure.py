"""Full raw zero-order invertibility and nonlinear one-phase obstruction."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import json,argparse,hashlib
import sympy as sp
from k1976_general_pairing_transport import setup,norm
from k1979_multicoordinate_symmetric_pairing import right,reduce_rows
from k1970_weighted_adjoint_mass_completion_probe import plus,product,transpose
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2000-raw-pairing-polynomial-structure.json'
def rank_mod(rows,p):
    piv={};pivots=[]
    for row in rows:
        d={j:v.numerator*pow(v.denominator,-1,p)%p for j,v in row.items() if v}
        d={j:v for j,v in d.items() if v}
        while d:
            k=min(d);v=d[k]
            if k not in piv:
                pivots.append(v);inv=pow(v,-1,p);piv[k]={j:x*inv%p for j,x in d.items()};break
            for j,x in piv[k].items():
                z=(d.get(j,0)-v*x)%p
                if z:d[j]=z
                else:d.pop(j,None)
    return len(piv),hashlib.sha256(json.dumps(pivots).encode()).hexdigest()
def blocks(J,T,inv,O,sign):
    B=[product(j,inv) for j in J[:14]];C=product(T,inv)
    left=[{j:(i,v) for (i,j),v in transpose(a).items()} for a in O]
    rightmaps=[{i:(j,v) for (i,j),v in a.items()} for a in B];cr={i:(j,v) for (i,j),v in C.items()}
    for mask in range(64):
        nodes=[(i,i^mask^s) for i in range(128) for s in [0,64]];idx={ij:k for k,ij in enumerate(nodes)};rows=[{} for _ in nodes]
        for c,(i,j) in enumerate(nodes):
            values=defaultdict(F)
            for k in range(14):
                a,u=left[k][i];b,v=rightmaps[k][j];values[a,b]+=(1 if k<7 else -1)*u*v
            b,v=cr[j];values[i,b]-=sign*v
            assert all(ab in idx for ab,v in values.items() if v),'invariant sector'
            for ab,v in values.items():
                if v:rows[idx[ab]][c]=v
        yield mask,nodes,rows

def produce():
    I,V,J,T,inv,O=setup();families=[];prime=1000003
    assert sp.isprime(prime)
    for sign in [-1,1]:
        reports=[]
        for mask,nodes,rows in blocks(J,T,inv,O,sign):
            rank,pivot_hash=rank_mod(rows,prime);assert rank==256
            reports.append(dict(mask=mask,dimension=256,rank_mod_prime=rank,pivot_sha256=pivot_hash))
        R=right(I,J,T,O,sign)
        columns=[plus(product(transpose(j),R),product(transpose(R),j),-1) for j in J[:14]]
        slots=[];rows=[]
        for ij in sorted(set().union(*columns)):
            row=[c.get(ij,F(0)) for c in columns]
            if len(reduce_rows(rows+[row]))>len(rows):slots.append(ij);rows.append(row)
            if len(rows)==14:break
        assert len(rows)==14
        M=sp.Matrix(rows);Minv=M.inv();B=max(sum(abs(F(x)) for x in row) for row in Minv.tolist())
        CR=sum(norm(transpose(o))*norm(j) for o,j in zip(O,J))+norm(T)
        C=2*CR*sum(norm(transpose(j)) for j in J[:14]);radius=1/(2*B*C)
        assert radius>0 and B*C*radius==F(1,2)
        families.append(dict(sign=sign,prime=prime,full_rank=16384,sectors=reports,phase_slots=[list(x) for x in slots],phase_matrix=[[str(v) for v in r] for r in rows],phase_inverse=[[str(v) for v in r] for r in Minv.tolist()],phase_inverse_row_norm=str(B),right_operator_norm_bound=str(CR),phase_perturbation_bound=str(C),one_phase_exclusion_radius=str(radius)))
    return dict(result_id='K2000',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',families=families,scope='Exact fixed raw128 equation, both mass signs. Zero-order map invertible on ALL real matrices; no nonzero algebraic matrix-field germ solves it, using Newton-Puiseux at generic infinity (rational case has an elementary degree proof). Symmetric one-scalar-field ansatz excluded through I and an explicit neighborhood. General multivariable analytic positive pairings remain open; no source or physical identification.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['tests/channel-swings/k1976_general_pairing_transport.py','tests/channel-swings/k1979_multicoordinate_symmetric_pairing.py','lab/process/k1967-paired-raw-coefficient-observation.json','lab/process/k1951-coordinated-zero-southeast-principal.json']})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=produce()
    if a.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
    else:assert d==json.loads(OUT.read_text())
    print('PASS K2000 128 complete 256-dimensional modular blocks and two exact 14-dimensional phase certificates')
