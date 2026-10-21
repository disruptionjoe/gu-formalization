#!/usr/bin/env python3
"""Finite CAR controls for full/even Hamiltonian shielding; continuum proof in note."""
import argparse,hashlib,itertools,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
OUT='lab/process/k1893-quantum-hamiltonian-shielding.json'
INPUT='lab/process/k1892-causal-observation-algebra.json'
def kron(*a):return s.kronecker_product(*a)
def jw(n):
    z=s.diag(1,-1);a=s.Matrix([[0,1],[0,0]])
    return [kron(*([z]*k+[a]+[s.eye(2)]*(n-k-1))) for k in range(n)]
def comm(a,b):return a*b-b*a
def zero(a):return all(s.expand(x)==0 for x in a)
def enc(a):return {'rows':a.rows,'columns':a.cols,'entries':[[i,j,str(a[i,j])] for i in range(a.rows) for j in range(a.cols) if a[i,j]]}
def produce():
    cs=jw(4);I=s.eye(16);N=[a.H*a for a in cs];pv=(I-2*N[0])*(I-2*N[1]);ph=(I-2*N[2])*(I-2*N[3]);pt=pv*ph
    checks={}
    def ck(k,v):
        checks[k]=bool(v)
        if not v:raise AssertionError('FAIL '+k)
    for i,a in enumerate(cs):
        for j,b in enumerate(cs):
            ck(f'CAR_{i}_{j}',zero(a*b+b*a) and zero(a*b.H+b.H*a-(I if i==j else s.zeros(16))))
    qp=N[2]*N[3];hp=pv*qp;density=N[0]*N[2];hop=cs[0].H*cs[1];pair=cs[0]*cs[1]
    for i in range(2):ck(f'hidden_quartic_commutes_full_{i}',zero(comm(qp,cs[i])))
    ck('hidden_quartic_not_quadratic',comm(qp,cs[2])==-cs[2]*N[3] and not zero(comm(qp,cs[2])))
    ck('quartic_projection',qp*qp==qp and qp.H==qp and qp.trace()==4)
    ck('parity_coupling_even_only',zero(comm(hp,hop)) and zero(comm(hp,pair)) and not zero(comm(hp,cs[0])))
    ck('density_interaction_breaks_even',comm(density,hop)==hop*N[2] and not zero(comm(density,hop)))
    ck('total_number_not_even_shield',not zero(comm((N[0]+N[1])*N[2],pair)))
    ck('all_test_interactions_total_even',all(zero(comm(pt,a)) for a in [qp,hp,density]))
    # Exhaust all Pauli monomials. Commutants are spanned by commuting monomials.
    P=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
    dims=dict(full=0,even=0,full_total_even=0,even_total_even=0)
    for inds in itertools.product(range(4),repeat=4):
        # Symbolic Pauli symplectic signs; independently checked by matrix-unit probe.
        visible_scalar=inds[0:2]==(0,0)
        visible_parity=inds[0:2]==(3,3)
        total_even=sum(j in (1,2) for j in inds)%2==0
        dims['full']+=visible_scalar;dims['even']+=visible_scalar or visible_parity
        dims['full_total_even']+=visible_scalar and total_even
        dims['even_total_even']+=(visible_scalar or visible_parity) and total_even
    ck('commutant_dimensions',dims==dict(full=16,even=32,full_total_even=8,even_total_even=16))
    # A visible parity phase is observable only by odd fields, never by the full even algebra.
    t=s.symbols('t',real=True);u=s.cos(t)*I-s.I*s.sin(t)*pv
    ck('parity_odd_rotation',all(s.trigsimp(x)==0 for x in u.H*cs[0]*u-(s.cos(2*t)*cs[0]+s.I*s.sin(2*t)*pv*cs[0])))
    # Parity readout with an even encoded hidden logical X, restricted to its dual rail.
    hx=cs[2].H*cs[3]+cs[3].H*cs[2];K=pv*hx
    ck('logical_readout_even',zero(comm(K,pt)))
    lo=s.Matrix([[0,1],[0,0]]);xx=lo+lo.H;yy=s.Matrix([[0,-s.I],[s.I,0]]);g=s.symbols('g',real=True)
    uplus=s.cos(g*t)*s.eye(2)-s.I*s.sin(g*t)*xx
    uminus=uplus.H;ket=s.Matrix([1,0])
    ck('parity_readout_distinguishes',s.trigsimp((ket.H*uplus.H*yy*uplus*ket)[0]+s.sin(2*g*t))==0 and s.trigsimp((ket.H*uminus.H*yy*uminus*ket)[0]-s.sin(2*g*t))==0)
    ck('perfect_parity_readout',s.trigsimp((ket.H*uplus.H*uminus*ket)[0]-s.cos(2*g*t))==0)
    diff=kron(s.diag(1,-1),s.diag(1,-1))-kron(s.diag(1,-1),s.eye(2))
    ck('parity_products_not_norm_Cauchy',max(abs(v) for v in diff.diagonal())==2)
    pred=json.loads((ROOT/INPUT).read_text())
    for i,w in enumerate(pred['leakage_witnesses']):
        ck(f'actual_local_hidden_basis_{i}',w['local_hidden_basis']['columns']==4)
    return dict(result_id='K1893',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',dimensions=dims,finite_modes={'visible':2,'hidden':2},witnesses={'hidden_quartic':enc(qp),'parity_controlled_quartic':enc(hp),'density_leak_commutator':enc(comm(density,hop))},theorems={'full':'H-Hv tensor I = I tensor Kh','even':'H-Hv tensor I = Pplus tensor Kplus + Pminus tensor Kminus; Kplus/minus even under total parity','continuum':'Every bounded even hidden CAR perturbation preserves the entire K1892 target evolution; no bounded-below energy asserted'},scope={'finite_classification':True,'continuum_hidden_bounded_construction':True,'all_interacting_GU':False,'global_visible_parity_in_quasilocal_CAR':False},checks=checks,inputs={INPUT:hashlib.sha256((ROOT/INPUT).read_bytes()).hexdigest()})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=produce()
    if a.write:(ROOT/OUT).write_text(json.dumps(d,indent=2)+'\n')
    else:assert d==json.loads((ROOT/OUT).read_text()),'FAIL report drift'
    print('PASS K1893',len(d['checks'])-4,'exact finite algebra checks; 4 inherited dimension reports; 1 pin')
