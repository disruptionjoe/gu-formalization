"""Exact resonance lattice for the fixed K2038 positive-norm action."""
from pathlib import Path
import argparse,hashlib,json
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k2040-nonlinear-resonance-selection.json'
WEIGHTS=((140,0),(70,0),(38,2),(19,1),(0,2),(0,1))

def weight(k):
    return tuple(sum(n*w[j] for n,w in zip(k,WEIGHTS)) for j in (0,1))

def ball(n,budget):
    if not n:
        yield ()
    else:
        for x in range(-budget,budget+1):
            for tail in ball(n-1,budget-abs(x)):yield (x,)+tail

def produce():
    resonances=[]
    for k in ball(6,6):
        if weight(k)==(0,0):
            assert all(k[j+1]==-2*k[j] for j in (0,2,4))
            d=sum(map(abs,k))
            if d and d%2==0:resonances.append(k)
            assert not (0<d<=4 and d%2==0)
    witness6=(2,-4,0,0,0,0);witness80=(9,1,-35,0,35,0)
    assert witness6 in resonances and weight(witness80)==(0,0)
    assert sum(map(abs,witness80))==80
    # Each pair obeys 2*x+y=h; its sharp minimal l1 cost is ceil(|h|/2).
    for h in range(-160,161):
        costs=[abs(x)+abs(h-2*x) for x in range(-161,162)]
        assert min(costs)==(abs(h)+1)//2
    assert (19+1)//2+35+35==80
    inp=['lab/process/k2038-observed-action-compression.json','explorations/conditional-build/k2038-observed-action-compression-2026-10-24.md']
    return dict(result_id='K2040',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',frequency_squared_relation='a^2+19*a-70=0; a=(sqrt(641)-19)/2',positive_T_frequencies=['1','2','a','2*a','19+a','2*(19+a)'],complex_multiplicities=[288,288,32,32,32,32],rotation_weights=WEIGHTS,weight_denominator=140,resonance_equations=['2*k1+k2=19*r','2*k3+k4=-70*r','2*k5+k6=70*r'],small_even_resonances=[list(k) for k in sorted(resonances)],first_even_sector_transfer_degree=6,first_pair_group_transfer_degree=80,witness6=list(witness6),witness80=list(witness80),quartic_statement='Every even polynomial of degree at most4 satisfying dV(T^-1*u)=0 is invariant under six independent sector phases; six local positive norm currents.',below80_statement='Every invariant polynomial of degree less than80 preserves each of the three paired-sector norms; degree80 is sharp.',homogeneous_domain='Every C2 norm-preserving potential gives globally defined homogeneous solutions; no global PDE theorem.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inp},scope='Fixed real commuting K2038 graph action and fixed norm only; no source parity, physical positivity, quantum or novelty claim.')
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=produce();s=json.dumps(r,indent=2)+'\n'
    if args.write:OUT.write_text(s)
    else:assert json.loads(s)==json.loads(OUT.read_text())
    print('PASS K2040 integer lattice, low degree census, degree6 and degree80 witnesses')
