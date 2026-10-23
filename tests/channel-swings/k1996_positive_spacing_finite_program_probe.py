"""Separate finite coverage, placement and dominance checks; mathematical faults."""
from fractions import Fraction as F
from pathlib import Path
from itertools import combinations,product
import json,copy
import k1996_positive_spacing_finite_program as subject
from k1950_global_catalyst_energy_certificates_probe import shell_return
R=Path(__file__).resolve().parents[2]
def rank(A,S):
    for e in S:
        for bath in range(4):
            z=e+bath
            assert len([(a,b) for a in A for b in range(4) if a+b==z])>=2*len([(s,b) for s in S for b in range(4) if s+b==z]),'shell rank'
def check(d):
    count=0;raw=set()
    for n in [5,6]:
        for gaps in product([1,2,3],repeat=n-1):
            A=[0]
            for x in gaps:A.append(A[-1]+x)
            for S in combinations(A[1:-1],2):
                if S[1]-S[0]>3:continue
                try:rank(A,S)
                except AssertionError:continue
                raw.add((tuple(A),S))
    expected={(A,S,(0,a,a+b),side) for A,S in raw for a in range(1,4) for b in range(1,4) if a+b<=4 for side in ['A','B']}
    got={(tuple(r['A']),tuple(r['S']),tuple(r['B']),r['shifted']) for r in d['dominance_witnesses']}
    assert len(raw)==17 and got==expected and len(got)==len(d['dominance_witnesses']),'coverage'
    for r in d['dominance_witnesses']:
        A,B,S=r['A'],r['B'],r['S'];T,C=r['target_support'],r['target_spectrum'];i,j=r['pair_indices'];q=r['pure_index']
        assert {i,j,q}=={0,1,2};rank(C,T)
        assert T[j]-T[i]==S[1]-S[0],'preserved pair gap'
        for delta in [F(501,1000),F(3,4),F(1)]:
            left,right=(B,A) if r['shifted']=='A' else (A,B)
            endpoints=sorted({F(0)}|{F(a-b)+delta for a in left for b in right if a-b+delta>=0})
            valid=[x for x in endpoints if all(abs(a-b-x)>=delta for a in left for b in right)]
            shift=min(valid);assert shift==r['shift_integer']+delta,'minimum offset'
            aa=shift if r['shifted']=='A' else F(0);bb=shift-aa;energies=[aa+x for x in S]+[bb+r['pure']]
            assert T[i]<=energies[0] and T[j]<=energies[1] and T[q]<=energies[2],'energy domination'
            count+=1
        for t in [F(1,3),F(1,2),F(2,3)]:
            for p0,p1 in [(F(1,5),F(2,5)),(F(0),F(1,2)),(F(1,2),F(1,2))]:
                pp=1-p0-p1;p=[F(0)]*3;p[i]=p0;p[j]=p1;p[q]=pp
                # Old pair return is homogeneous; isolated pure mass contributes pp/2.
                old=shell_return(t,list(map(F,S)),[p0,p1])+pp/2
                new=shell_return(t,list(map(F,T)),p)
                assert new<=old,'return domination';count+=1
    curves=[[{k:None if v is None else F(v) for k,v in p.items()} for p in d[key]] for key in ['half_spacing_curve','wide_spacing_curve']]
    for row in d['budget_controls']:
        x=F(row['energy']);vals=[next(p['slope']*x+p['intercept'] for p in c if p['lo']<=x and(p['hi'] is None or x<=p['hi'])) for c in curves]
        assert vals==[F(row['half']),F(row['wide'])] and vals[1]-vals[0]==F(row['jump']),'curve value';count+=1
    return count

def budget_checks(d):
    from k1992_wide_spacing_eight_level_rigidity_probe import minimum
    prior=json.loads((R/'lab/process/k1994-nine-level-thermal-reduction.json').read_text())
    connected=[list(map(F,b['S'])) for b in prior['pareto_blocks']]
    mixed=[]
    for S,A in [([1,3],range(5)),([2,3],range(6)),([1,4],range(6))]:
        for shifted in [False,True]:
            aa=F(1,2) if shifted else F(0);bb=F(1,2)-aa
            mixed.append(sorted([aa+s for s in S]+[bb+1]))
    n=0
    for E in [F(18,11),F(2)]:
        for key,supports in [('wide_spacing_curve',connected),('half_spacing_curve',connected+mixed)]:
            true=min(v for S in supports if (v:=minimum(F(1,2),S,E)) is not None)
            value=next(F(p['slope'])*E+F(p['intercept']) for p in d[key] if F(p['lo'])<=E and(p['hi'] is None or E<=F(p['hi'])))
            assert true==value,'independent budget optimum';n+=1
    return n

def placements():
    n=0
    for A,B in [([0,1,2],[0,1,2]),([0,1,2,3,4],[0,1,2])]:
        for pick in combinations(range(len(A)+len(B)),len(A)):
            aa=iter(A);bb=iter(B);order=[(0,next(aa)) if k in pick else (1,next(bb)) for k in range(len(A)+len(B))]
            for delta in [F(1,4),F(3,4),F(1)]:
                y=subject.placement([A,B],order,delta)
                if y is None:
                    # Two variables: exact intersected bounds independently decide feasibility.
                    low=F(0);high=None;bad=False
                    for (i,a),(j,b) in zip(order,order[1:]):
                        w=delta+a-b
                        if i==j:bad|=w>0
                        elif i==0:low=max(low,w)
                        else:high=-w if high is None else min(high,-w)
                    # Relative offsets can be negative, so recompute without low>=0.
                    lows=[delta+a-b for (i,a),(j,b) in zip(order,order[1:]) if (i,j)==(0,1)]
                    highs=[-delta-a+b for (i,a),(j,b) in zip(order,order[1:]) if (i,j)==(1,0)]
                    assert bad or(lows and highs and max(lows)>min(highs)),'false infeasible'
                else:
                    assert min(y)==0 and all(y[j]+b-y[i]-a>=delta for (i,a),(j,b) in zip(order,order[1:])),'placement'
                n+=1
    return n
if __name__=='__main__':
    d=json.loads((R/'lab/process/k1996-positive-spacing-finite-program.json').read_text());n=check(d);m=placements();b=budget_checks(d);print('PASS baseline',n,'coverage/physical/return/curve and',m,'placement controls plus',b,'independent optimizations')
    mutants=[]
    x=copy.deepcopy(d);x['dominance_witnesses'].pop();mutants.append(('missing shape',x))
    x=copy.deepcopy(d);x['dominance_witnesses'][0]['shift_integer']+=1;mutants.append(('nonminimal placement',x))
    x=copy.deepcopy(d);x['dominance_witnesses'][0]['target_support'][1]+=1;mutants.append(('broken support',x))
    x=copy.deepcopy(d);x['budget_controls'][0]['wide']='0';mutants.append(('wrong optimum',x))
    for name,x in mutants:
        try:check(x)
        except AssertionError as e:print('DETECTED mathematical fault:',name,str(e))
        else:raise AssertionError('MISSED '+name)
