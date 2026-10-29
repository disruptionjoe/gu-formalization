#!/usr/bin/env python3
"""K2243 finite shell permutations, reference matrix units and exact resources."""
from fractions import Fraction as F
from itertools import product
from math import comb
FAULTS=['shift_sign','cyclic_wrap','unconditional_swap','insufficient_margin','omit_lowering','multi_axis_shift','work_sign']
Q=(0,1,3);N=8
# state: control, record, cell1, cell2, battery
STATES=list(product(range(3),range(2),range(2),range(2),range(N+1)))
def energy(x):return Q[x[0]]*x[1]+Q[1]*x[2]+Q[2]*x[3]+x[4]
def ramp(x,a,b,fault=None):
    z=list(x)
    if z[0] not in (a,b):return x
    dest=b if z[0]==a else a;d=(Q[z[0]]-Q[dest])*z[1]
    if fault=='shift_sign':d=-d
    k=z[4]+d
    if fault=='cyclic_wrap':k%=N+1
    if 0<=k<=N:z[0]=dest;z[4]=k
    return tuple(z)
def swap(x,j,fault=None):
    z=list(x)
    if z[0]==j or fault=='unconditional_swap':z[1],z[j+1]=z[j+1],z[1]
    return tuple(z)
def circuit(x,fault=None):
    for j in [1,2]:x=swap(ramp(x,j-1,j,fault),j,fault)
    return x if fault=='omit_lowering' else ramp(x,2,0,'shift_sign' if fault=='work_sign' else fault)
def controls(fault=None):
    ck={}
    for a,b in [(0,1),(1,2),(2,0)]:
        images=[ramp(x,a,b,fault) for x in STATES]
        ck['ramp_bijection_'+str((a,b))]=len(set(images))==len(STATES)
        ck['ramp_energy_'+str((a,b))]=all(energy(x)==energy(y) for x,y in zip(STATES,images))
    for j in [1,2]:
        images=[swap(x,j,fault) for x in STATES]
        ck['swap_bijection_'+str(j)]=len(set(images))==len(STATES)
        ck['swap_global_energy_'+str(j)]=all(energy(x)==energy(y) for x,y in zip(STATES,images))
    support=[3,4,5] if fault!='insufficient_margin' else [0,1,2]
    p1,p2=F(1,3),F(1,9)
    # Exact map of all record matrix units; orthogonal reference entries carry through.
    # Test diagonal and fully coherent uniform battery density matrices separately.
    for coherent in [False,True]:
      for a,b in product(range(2),repeat=2):
        output=[[F(0),F(0)],[F(0),F(0)]]
        for c1,c2 in product(range(2),repeat=2):
          prob=(p1 if c1 else 1-p1)*(p2 if c2 else 1-p2)
          for k,l in product(support,repeat=2):
            if not coherent and k!=l:continue
            u=circuit((0,a,c1,c2,k),fault);v=circuit((0,b,c1,c2,l),fault)
            if (u[0],u[2],u[3],u[4])==(v[0],v[2],v[3],v[4]):output[u[1]][v[1]]+=prob/F(len(support))
        expected=[[1-p2,F(0)],[F(0),p2]] if a==b else [[F(0)]*2 for _ in range(2)]
        ck['matrix_unit_reset_'+str((coherent,a,b))]=output==expected
    ck['control_returns_zero']=all(circuit((0,n,c1,c2,k),fault)[0]==0 for n,c1,c2,k in product(range(2),range(2),range(2),support))
    # Exact work for arbitrary rational initial occupation, verified from path enumeration.
    w=F(2,5);actual=F(0)
    for n,c1,c2 in product(range(2),repeat=3):
      p=(w if n else 1-w)*(p1 if c1 else 1-p1)*(p2 if c2 else 1-p2)
      x=(0,n,c1,c2,4);actual+=p*(4-circuit(x,fault)[4])
    ck['mean_work_from_paths']=actual==w+2*p1-3*p2
    # Two-axis exact energies tracked as vectors, so no irrational floating arithmetic.
    basis=[(0,0),(1,0),(0,1)]
    allsafe=True;cons=True
    for ns in product(range(2),repeat=3):
      k=[2,2];n=ns[0];label=0
      for j in [1,2,0]:
        e0=tuple(k[t]+n*basis[label][t] for t in range(2))
        d=[(basis[label][t]-basis[j][t])*n for t in range(2)]
        if fault=='multi_axis_shift':d=[-x for x in d]
        k=[k[t]+d[t] for t in range(2)];label=j
        cons &= e0==tuple(k[t]+n*basis[label][t] for t in range(2))
        allsafe &= all(1<=x<=3 for x in k)
        if j:n=ns[j]
    ck['arbitrary_gap_energy_vectors']=cons;ck['multi_axis_safe_histories']=allsafe
    ck['reset_consumer']=F(1,1+2**20)<F(1,10**6)
    ck['clock_consumer']=F(comb(49,9),10**54)<F(1,10**44)
    ck['joint_sine_consumer']=F(40*22,7*12573)<F(1,100)
    work20=F(1,2)+sum(F(1,1+2**j) for j in range(1,20))-F(20,1+2**20)
    ck['twenty_cell_mean_work_bracket']=F(126,100)<work20<F(127,100)
    ck['gate_count']=2*20+1==41
    return ck

RESULT='K2243'
REPORT='lab/process/k2243-variable-gap-battery-reset.json'
DEPS=['explorations/conditional-build/k2243-variable-gap-battery-reset-2026-10-29.md', 'explorations/conditional-build/k2229-finite-step-thermal-reset-work-2026-10-28.md', 'explorations/conditional-build/k2240-finite-battery-gate-2026-10-29.md', 'explorations/conditional-build/k2238-finite-clock-thermal-circuit-2026-10-29.md']
EVIDENCE='Exact complete finite permutations, energy vectors, reference matrix-unit channel and rational resources; universal arbitrary-gap/reference/clock arguments in note.'

def main():
    import argparse,hashlib,json
    from pathlib import Path
    args=argparse.ArgumentParser();args.add_argument('--write',action='store_true');a=args.parse_args()
    root=Path(__file__).resolve().parents[2]
    checks=controls();assert all(checks.values()),[k for k,v in checks.items() if not v]
    faults={}
    for fault in FAULTS:
        bad=[k for k,v in controls(fault).items() if not v]
        assert bad,('undetected mathematical input fault',fault)
        faults[fault]=bad
    report=dict(result_id=RESULT,checks=checks,fault_failures=faults,evidence_kinds=EVIDENCE,
        dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in DEPS},
        probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    p=root/REPORT
    if a.write:p.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(p.read_text())==report,'certificate drift'
    print(json.dumps(dict(result=RESULT,controls=len(checks),faults=len(faults))))
if __name__=='__main__':main()
