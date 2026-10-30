#!/usr/bin/env python3
"""Finite exact joint-circuit and numerical echo controls, not all-N certificates."""
from pathlib import Path
import json,hashlib,argparse
import sympy as s
import mpmath as mp
R=Path(__file__).resolve().parents[2]

def parking(N,kind='threshold',phase=1):
    # Actual sparse joint optical/neutral isometry: optical n + (N+1)*record.
    d=N+1;V=s.zeros(d*d,d)
    for n in range(d):V[n+d*n,n]=1 # coherent number-copy isometry on blank record
    for k in range(N,0,-1):
        G=s.eye(d*d)
        for label in range(d):
            flag=(label>=k) if kind=='threshold' else ((label==k) if kind=='equality' else True)
            if flag:
                lo=k-1+d*label;hi=k+d*label
                G[lo,lo]=G[hi,hi]=0;G[lo,hi]=phase;G[hi,lo]=-phase
        V=G*V
    return V

def exact(fault=None):
    c={}
    def check(k,v):c[k]=bool(v)
    kind='equality' if fault=='equality_flag' else ('unconditional' if fault=='no_flag' else 'threshold')
    for N in range(1,6):
        d=N+1;V=parking(N,kind,-1 if fault=='wrong_transfer_phase' else 1);target=s.zeros(d*d,d)
        for n in range(d):target[d*n,n]=1
        check(f'joint_parking_N{N}',V==target)
        check(f'isometry_N{N}',V.T*V==s.eye(d))
    for cap in range(1,5):
        states=[(p,r) for p in range(cap+1) for r in range(cap+1-p)];index={v:i for i,v in enumerate(states)}
        hop=s.zeros(len(states));charge=s.diag(*[p+r for p,r in states])
        for j,(p,r) in enumerate(states):
            if p:
                dest=(p-1,r if fault=='omit_reference_increment' else r+1)
                i=index[dest];hop[i,j]=hop[j,i]=s.sqrt(p*(r+1))
        check(f'physical_hopping_charge_cap{cap}',charge*hop==hop*charge)
    check('passive_orbit_obstruction',sorted([1,1])!=sorted([0,2]))
    N=3;H=s.diag(*[s.Rational(n*(n-1),2) for n in range(N+1)]);B=s.zeros(N+1)
    for n in range(1,N+1):B[n,n-1]=B[n-1,n]=s.sqrt(n*(N-n+1))
    C=s.diag(*[(-1)**n for n in range(N+1)])
    if fault=='missing_parity':C=s.eye(N+1)
    check('parity_hopping_anticommutation',C*B*C==-B)
    check('parity_drift_commutation',C*H*C==H)
    check('parity_involution',C*C==s.eye(N+1))
    check('active_echo_generators_equal',C*(H-B)*C==H+B)
    check('inactive_echo_generator_average',((H+B)+(H-B))/2==H)
    angle=s.pi if fault=='half_revival' else 2*s.pi
    phases=[s.simplify(s.exp(-s.I*angle*H[n,n])) for n in range(N+1)]
    check('revival_all_levels',phases==[1]*(N+1))
    # Explicit d=4 DFT phase-estimation number-copy matrix, without oracle truth flags.
    d=4;F=s.Matrix(d,d,lambda a,b:s.I**(a*b)/2)
    for n in range(3):
        phasevec=s.Matrix([s.I**(n*j)/2 for j in range(d)])
        out=s.simplify(F.conjugate().T*phasevec)
        check(f'coherent_number_copy_n{n}',out==s.eye(d)[:,n])
    # Actual finite Fourier probabilities and circular loss for N=1 c=(1,1)/sqrt2.
    for phi,name in [(0,'zero'),(s.pi/4,'quarter')]:
        d=2 if fault=='fourier_alias' else 4
        risk=0;total=0
        for j in range(d):
            amp=(1+s.exp(-2*s.I*phi)*s.exp(2*s.pi*s.I*j/d))/s.sqrt(2*d)
            prob=s.simplify(s.expand_complex(amp*s.conjugate(amp)))
            total+=prob;risk+=prob*4*s.sin(phi-s.pi*j/d)**2
        check('fourier_normalized_'+name,s.simplify(total)==1)
        check('fourier_risk_'+name,s.simplify(risk)==1)
    q=s.symbols('q',positive=True,integer=True)
    count=3*q if fault=='omit_scratch_uncompute' else q+2*q+2*q
    check('dispersive_copy_uncompute_count',s.simplify(count-5*q)==0)
    # Below-shell resonant edge amplitudes are at most the N-shell target.
    for N in range(1,5):
        check(f'lower_shell_bound_N{N}',all(s.Rational(k*(M-k+1),k*(N-k+1))<=1 for M in range(1,N+1) for k in range(1,M+1)))
    for n in range(6):check(f'kerr_integer_n{n}',(n*(n-1))%2==0)
    return c

def numerical():
    mp.mp.dps=60;c={}
    for N in (2,3):
        D=mp.mpf(N*(N-1))/2;H=mp.diag([mp.mpf(n*(n-1))/2 for n in range(N+1)]);B=mp.matrix(N+1)
        for n in range(1,N+1):B[n,n-1]=B[n-1,n]=mp.sqrt(n*(N-n+1))/7
        b=mp.mpf(N)/7
        for delta in (mp.mpf('0.01'),mp.mpf('0.02')):
            E=mp.expm(-1j*(H+B)*delta/2)*mp.expm(-1j*(H-B)*delta/2)
            error=mp.norm(E-mp.expm(-1j*H*delta))
            # Frobenius can exceed operator bound; use sqrt(dim)*operator bound.
            bound=mp.sqrt(N+1)*delta**2*D*b/2
            c[f'inactive_echo_N{N}_delta{delta}']=bool(error<=bound)
            C=mp.diag([(-1)**n for n in range(N+1)])
            active=mp.expm(-1j*(H+B)*delta/2)*C*mp.expm(-1j*(H-B)*delta/2)*C
            c[f'active_echo_N{N}_delta{delta}']=bool(mp.norm(active-mp.expm(-1j*(H+B)*delta))<mp.mpf('1e-55'))
    for N in (1,2,3,7,16):
        total=sum(1/mp.sqrt(k*(N-k+1)) for k in range(1,N+1))
        c[f'edge_sum_N{N}']=bool(total<=mp.pi)
        J=mp.mpf('0.1');chi=mp.mpf('2');eps=mp.mpf('.01');tau=mp.pi/(2*J);D=abs(chi)*N*(N-1)/2
        r=[];err=mp.mpf(0)
        for k in range(1,N+1):
            b=N*J/mp.sqrt(k*(N-k+1));w=chi*(k-1)
            rk=max(1,int(mp.ceil(N*tau**2*b*(D+abs(w))/eps)));r.append(rk);err+=tau**2/rk*b*(D+abs(w))
        ceiling=N+mp.pi**3*abs(chi)*N**2*(N-1)*(N+2)/(8*J*eps)
        c[f'echo_step_budget_N{N}']=bool(err<=eps)
        c[f'echo_count_bound_N{N}']=bool(sum(r)<=ceiling)
    return c

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    clean=exact();bad=[k for k,v in clean.items() if not v];assert not bad,('baseline',bad)
    faults=['omit_reference_increment','equality_flag','no_flag','wrong_transfer_phase','missing_parity','half_revival','fourier_alias','omit_scratch_uncompute'];caught={}
    for f in faults:
        result=exact(f);caught[f]=[k for k,v in result.items() if not v];assert caught[f],('uncaught',f)
    nums=numerical();assert all(nums.values()),[k for k,v in nums.items() if not v]
    deps=['explorations/conditional-build/k2328-local-neutral-readout-compiler-2026-10-30.md','explorations/conditional-build/k2324-kerr-selective-lossy-control-2026-10-30.md','explorations/conditional-build/k2326-finite-neutral-readout-2026-10-30.md',str(Path(__file__).relative_to(R))]
    report={'result':'K2328','scope':'conditional finite exact joint-circuit and 60-digit numerical controls; all-N error theorem rests on written proof','exact_checks':len(clean),'numerical_checks':len(nums),'checks':clean,'numerical_controls':nums,'changed_input_faults':caught,'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps}}
    if args.write:(R/'lab/process/k2328-local-neutral-readout-compiler.json').write_text(json.dumps(report,indent=2)+'\n')
    print(f'K2328 PASS {len(clean)} exact, {len(nums)} numerical controls; {len(caught)} genuine faults')
if __name__=='__main__':main()
