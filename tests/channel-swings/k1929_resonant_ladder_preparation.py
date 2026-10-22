"""Exact shell-rank and weighted-support calculation; universal proof in note."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]

def shells(energies,gap=F(1)):
    result={}
    for b in (0,1):
        for a,e in enumerate(energies):result.setdefault(e+b*gap,[]).append((b,a))
    return result

def feasible(support,energies,gap=F(1),rank=2):
    S=set(support)
    return all(rank*sum(a in S for b,a in cell)<=len(cell) for cell in shells(energies,gap).values())

def graph_support(energies,gap=F(1)):
    idx={e:i for i,e in enumerate(energies)};out=[]
    for low in sorted(e for e in energies if e-gap not in idx):
        chain=[];e=low
        while e in idx:chain.append(idx[e]);e+=gap
        out.extend(chain[1:-1:2])
    return sorted(out)

def mass_formula(d,t):
    L=(d-1)//2
    return t*(1-t**(2*L))/((1+t)*(1-t**d))

def calculate(fault=None):
    n=0
    def check(x,label):
        nonlocal n
        if not x:raise AssertionError(label)
        n+=1
    for d in range(3,10):
        energies=list(map(F,range(d)));chosen=graph_support(energies)
        if fault=='endpoint':chosen=[0]+chosen
        check(feasible(chosen,energies),'endpoint/shell support')
        for t in (F(1,3),F(1,2),F(3,4)):
            Z=sum(t**j for j in range(d));p=sum(t**j for j in chosen)/Z
            check(p==mass_formula(d,t),'closed mass formula')
            candidates=[S for k in range(d+1) for S in combinations(range(d),k) if feasible(S,energies)]
            check(p==max(sum(t**j for j in S)/Z for S in candidates),'global Gibbs maximum')
            s=[(t**j/Z/p if j in chosen else F(0)) for j in range(d)]
            if fault=='weight':s[chosen[0]]+=F(1,100)
            check(sum(s)==1,'state normalization')
            check(sum(abs(s[j]-t**j/Z) for j in range(d))/2==1-p,'trace distance optimum')
    for d in range(1,12):
        for m in range(1,5):
            es=list(map(F,range(d)));S=graph_support(es,F(m))
            check(bool(S)==(d>=2*m+1),'gap resonance existence')
            check(feasible(S,es,F(m)),'residue-class support')
            check(all(not feasible([a],es,F(m),rank=3) for a in range(d)),'rank3 excluded')
    es=[F(0),F(1),F(2),F(7,2),F(9,2),F(11,2),F(13,2)]
    check(graph_support(es)==[1,4],'two disconnected noninteger-offset chains')
    check(feasible([1,4],es),'general spectrum witness')
    check(not any(feasible([a],list(map(F,range(7))),F(3,2)) for a in range(7)),'noninteger bath gap')
    # A unitary target is an explicit excluded-hypothesis control.
    check(feasible(range(5),list(map(F,range(5))),rank=1),'rank1 identity control')
    check(mass_formula(5,F(1,2))==F(10,31),'example mass10/31')
    return {'exact_checks':n,'example_mass':'10/31','example_trace_distance':'21/31','rank3_possible':False}

def report():
    data=calculate();data['evidence_kind']='finite exact rational controls; universal statements use analytic proof'
    data['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return data

if __name__=='__main__':
    import sys
    value=report()
    if '--write' in sys.argv:(ROOT/'lab/process/k1929-resonant-ladder-preparation.json').write_text(json.dumps(value,indent=2)+'\n')
    print(json.dumps(value))
