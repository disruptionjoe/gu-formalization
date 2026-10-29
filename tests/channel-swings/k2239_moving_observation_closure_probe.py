#!/usr/bin/env python3
"""K2239 exact graph contraction and principal-kernel controls; proof is in note."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tests/channel-swings'))
import k2236_raw_observation_closure_probe as prev
import argparse,hashlib,json
F=prev.F;o=prev.o;I=o.ONE;Z=o.ZERO
mm=prev.mm;rank=prev.rank;ident=prev.ident;minus=prev.minus
FAULTS=['dark_coefficient','word_entry','principal_entry','time_row_sign','normal_gamma','moving_derivative','graph_as_projector']
def run(fault=None):
    checks={}
    def ck(name,value):checks[name]=bool(value)
    E=[[F(0) for c in range(6)] for r in range(15)]
    R=[[F(0) for c in range(15)] for r in range(6)]
    for r,a in enumerate([0,7,8,9]):E[a][r]=R[r][a]=1
    for a in o.UN:E[a][4]=1;R[4][a]=F(1,10)
    E[14][5]=R[5][14]=1
    PV=minus(ident(15),mm(E,R))
    MI=[[F(0) for c in range(15)] for r in range(15)]
    MI[0][14]=-2;MI[14][0]=1
    for a in range(1,14):
        for c in range(1,14):MI[a][c]=F(1,12)-F(a==c)
    MS={k:[[o.scalar_m(k,a,c) for c in range(15)] for a in range(15)] for k in o.OBS}
    ck('original_M0_inverse',mm(MI,MS[0])==ident(15))
    LS={j:mm(MI,MS[j]) for j in o.OBS[1:]}
    if fault=='principal_entry':LS[7][0][0]+=1
    TS={j:mm(mm(R,LS[j]),E) for j in LS}
    d=[F(-4 if fault=='dark_coefficient' else -5)]*4+[F(1),F(0)]
    h=[[F(c==5) for c in range(6)]]
    rows=h+sum((mm(h,TS[j]) for j in LS),[])+mm(mm(h,TS[7]),TS[7] if fault=='word_entry' else TS[8])
    expected=[[0,0,0,0,0,1],[0,0,1,1,10,0],[0,1,0,1,10,0],[0,1,1,0,10,0],[1,0,0,1,10,0]]
    ck('actual_scalar_word_rows',rows==expected)
    ck('scalar_observability_rank_five',rank(rows)==5)
    ck('scalar_dark_line',not any(map(any,mm(rows,[[x] for x in d]))))
    for j in LS:
        ck('full_V_action_'+str(j),mm(LS[j],PV)==PV)
        ck('C_intertwining_'+str(j),mm(LS[j],E)==mm(E,TS[j]))
        ck('dark_invariance_'+str(j),mm(TS[j],[[x] for x in d])==[[x] for x in d])
        N=minus(mm(TS[j],TS[j]),ident(6))
        ck('quotient_Jordan_rank_one_'+str(j),rank(N)==1)
        ck('quotient_Jordan_square_zero_'+str(j),not any(map(any,mm(N,N))))
    A=o.mul(o.G[0],o.J);T=o.blade(o.UN)
    C={j:o.mul(o.G[0],o.G[j]) for j in LS}
    for j,c in C.items():
        ck('C_involution_'+str(j),o.mul(c,c)==I)
        ck('time_anticommutation_'+str(j),o.add(o.mul(o.G[0],c),o.mul(c,o.G[0]))==Z)
        # q0(A_j n)-Cj q0(n): the normal terms cancel, temporal terms do not.
        left=o.scale(o.mul(o.G[0],c),-5)
        right=o.scale(o.mul(c,o.G[0]),-5)
        actual=o.add(left,o.scale(right,-1 if fault!='time_row_sign' else 1))
        expected_defect=o.scale(o.mul(o.G[0],c),-10)
        ck('temporal_graph_defect_'+str(j),actual==expected_defect)
        ck('temporal_defect_invertible_'+str(j),o.mul(o.mul(o.G[0],c),o.mul(c,o.G[0]))==I)
        for r in o.UN:
            gr=o.G[0] if fault=='normal_gamma' and r==o.UN[0] else o.G[r]
            ck('normal_commutes_C_'+str(j)+'_'+str(r),o.mul(gr,c)==o.mul(c,gr))
    for r in o.UN:
        gr=o.G[r]
        ck('normal_mass_intertwiner_'+str(r),o.mul(gr,A)==o.mul(A,gr))
        ck('normal_flavor_intertwiner_'+str(r),o.add(o.mul(gr,T),o.mul(T,gr))==Z)
    # Genuine constrained positive countercontrol: w1=s,w2=-s, graph f1=t.
    positive_seed={(1,0):I,(2,0):o.scale(I,-1)}
    graph_positive={(0,1):o.G[1]}
    ck('positive_graph_observation',o.blockmul(graph_positive,positive_seed)=={(0,0):o.G[1]})
    ck('positive_graph_orthogonal',o.mul(o.transpose(o.G[1]),o.G[1])==I)
    for name,generator,sign in [('mass',A,1),('flavor',T,-1),*[(str(j),c,1) for j,c in C.items()]]:
        raw={(r,r):generator for r in o.UN}
        ck('positive_subsystem_invariant_'+name,o.blockmul(raw,positive_seed)==o.blockmul(positive_seed,{(0,0):generator}))
        ck('positive_observed_intertwiner_'+name,o.mul(o.G[1],generator)==o.scale(o.mul(generator,o.G[1]),sign))
    # Exact graph rank witnesses: slope on normal1, and four slopes on normals1..4.
    # Inputs w1..w4 are independent; normal13 compensates sum and has zero slopes.
    for r in [1,2,3,4]:
        gr=o.scale(o.G[r],o.ETA[r])
        ck('graph_rank_witness_'+str(r),o.mul(gr,o.G[r])==I)
    graph1={} if fault=='graph_as_projector' else {(0,0):o.scale(o.G[1],o.ETA[1])}
    inv1={(0,0):o.G[1]}
    ck('one_slope_rank128_witness',o.blockmul(graph1,inv1)=={(0,0):I})
    graph4={(r,r):o.scale(o.G[r+1],o.ETA[r+1]) for r in range(4)}
    inv4={(r,r):o.G[r+1] for r in range(4)}
    ck('four_slope_rank512_witness',o.blockmul(graph4,inv4)=={(r,r):I for r in range(4)})
    # Legitimate zero-sum datum w2=s,w3=-s; graph f1=t,f2=t^2/2.
    datum=[[F(0)] for r in range(15)];datum[2]=[F(1)];datum[3]=[F(-1)]
    ck('moving_datum_in_V',mm(PV,datum)==datum)
    ck('moving_datum_R0_zero',not any(map(any,mm(R,datum))))
    q_at_zero={(0,1):o.G[1]}
    q_derivative={(0,2):o.scale(o.G[2],-1 if fault=='moving_derivative' else 1)}
    datum_blocks={(2,0):I,(3,0):o.scale(I,-1)}
    ck('moving_initial_pullback_zero',o.blockmul(q_at_zero,datum_blocks)=={})
    ck('moving_nonzero_initial_jet',o.blockmul(q_derivative,datum_blocks)=={(0,0):o.G[2]})
    mass={(r,r):A for r in o.UN}
    ck('mass_cannot_cancel_moving_jet',o.blockmul(q_at_zero,o.blockmul(mass,datum_blocks))=={})
    # Additional w1,w2 output supplies rank256 on V and reconstructs Q_B at all t.
    repair={(0,1):I,(1,2):I}
    seed={(1,0):I,(2,1):I,(3,0):o.scale(I,-1),(3,1):o.scale(I,-1)}
    ck('repair_additional_rank256',o.blockmul(repair,seed)=={(0,0):I,(1,1):I})
    for t in [F(0),F(1),F(-2),F(3,7)]:
        consumer={(0,0):o.G[1]}
        if t:consumer[(0,1)]=o.scale(o.G[2],t)
        q={(0,1):o.G[1]}
        if t:q[(0,2)]=o.scale(o.G[2],t)
        ck('repaired_graph_consumer_'+str(t),o.blockmul(consumer,repair)==q)
    return checks

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
    checks=run();assert all(checks.values()),[k for k,v in checks.items() if not v]
    failures={}
    for fault in FAULTS:
        failed=[k for k,v in run(fault).items() if not v]
        assert failed,('undetected_fault',fault);failures[fault]=failed
    deps=['explorations/conditional-build/k2239-moving-observation-closure-2026-10-29.md','tests/channel-swings/k2236_raw_observation_closure_probe.py','tests/channel-swings/k2206_changed_raw_mass_construction_probe.py','explorations/conditional-build/k2236-raw-observation-closure-2026-10-29.md','explorations/conditional-build/k2233-degree-dependent-raw-pairing-2026-10-29.md','lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md']
    report=dict(result_id='K2239',status='conditional_literal_graph_principal_closure',checks=checks,fault_failures=failures,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Original scalar symbols, exact Clifford identities, graph rank witnesses and moving initial-jet controls; universal written kernel/rank/symmetrizer proof; no induced ambient operator or source selection.')
    dest=ROOT/'lab/process/k2239-moving-observation-closure.json'
    if args.write:dest.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dest.read_text())==report,'certificate drift'
    print(json.dumps(dict(result='K2239',controls=len(checks),faults=len(failures))))
if __name__=='__main__':main()
