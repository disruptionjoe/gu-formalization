"""Independent parameter-event and bath-label check of optimal-ray contacts."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
from copy import deepcopy
import json,hashlib
from k2015_finite_thermal_ray_separation_probe import bath_planes,direct
ROOT=Path(__file__).resolve().parents[2];D=Q(4,15);A=Q(6,5);Z=Q(11,5);EC=Q(113,91);M=Q(17,10)
def g(d,E):return min(Q(9,20)-Q(3,20)*(E-A)/(1+d),Q(3,10)+Q(3,20)*(Z-E)/(1-d))
def events(e,b,f=None,k=None):
    ds={Q(0),D}
    for x,z in [(e,b)]+([] if f is None else [(f,k)]):
        if z!=Q(1,2):
            d=(M-x)/(z-Q(1,2))
            if 0<=d<=D:ds.add(d)
        if z:
            for E in [A,Z]:
                d=(E-x)/z
                if 0<=d<=D:ds.add(d)
    out=sorted(ds)
    return sorted(ds|{(a+b)/2 for a,b in zip(out,out[1:])})
def pair(e,R,b,f,S,k,kind):
    count=0
    for d in events(e,b,f,k):
        x,y,mid=e+b*d,f+k*d,M+d/2
        if not x<=mid<=y:continue
        numerator=R*(y-mid)+S*(mid-x)-Q(3,8)*(y-x)
        assert numerator>=0,'negative actual chord'
        count+=1
        if d>0 and numerator==0:
            assert kind=='separated'
            assert (e,R,f,S)==(A,Q(9,20),Z,Q(3,10)) or (d==D and (e,R,b,f,S,k)==(EC,Q(81,182),0,Z,Q(3,10),1))
    return count

def run():
    c=json.loads((ROOT/'lab/process/k2015-finite-thermal-ray-separation.json').read_text())['census'];rs=sorted({(Q(v['energy']),Q(v['return'])) for cell in c['cells'] for v in cell['vertices']});n_single=n_sep=n_same=0
    for e,R in rs:
      for b in [0,1]:
        for d in events(e,b):
          E=e+b*d
          if not A<=E<=Z:continue
          assert R>=g(d,E);n_single+=1
          if d>0 and A<E<Z and R==g(d,E):assert (d,e,R,b)==(D,EC,Q(81,182),0)
    for e,R in rs:
      for f,S in rs:
        if e<=M+D/2 and f+D>=M:n_sep+=pair(e,R,0,f,S,1,'separated')
        if f<=M+D/2 and e+D>=M:n_sep+=pair(f,S,1,e,R,0,'separated')
    for cell in c['cells']:
      vs=cell['vertices'];_,_,de=bath_planes(cell['support'],cell['orientation'],True)
      signs=[[sum(x*Q(y) for x,y in zip(row,v['p'])) for row in de] for v in vs]
      for i,j in combinations(range(len(vs)),2):
        if any(x*y<0 for x,y in zip(signs[i],signs[j])):continue
        e,R=Q(vs[i]['energy']),Q(vs[i]['return']);f,S=Q(vs[j]['energy']),Q(vs[j]['return'])
        if e>f:e,f,R,S=f,e,S,R
        if e<=M+D/2 and f>=M:n_same+=pair(e,R,0,f,S,0,'same')
    return n_single,n_sep,n_same

def check_witness(row):
    E=Q(row['energy']);p=list(map(Q,row['populations']));a=row['spectrum'];s=[1,3,5]
    assert sum(p)==1 and sum(x*y for x,y in zip(s,p))==E
    assert direct(s,p)==Q(row['return_value'])==g(D,E)
    assert all(sum(x+b==e for x in a for b in range(4))>=2*sum(x+b==e for x in s for b in range(4)) for e in {x+b for x in s for b in range(4)})
if __name__=='__main__':
    counts=run();r=json.loads((ROOT/'lab/process/k2018-thermal-optimizer-rigidity.json').read_text())
    for row in r['endpoint_seven_level_witnesses']:check_witness(row)
    completions=[]
    for s in [(1,3),(1,3,5)]:
      first=None;count=0
      # Independent bitset enumeration includes every relevant completion.
      for mask in range(1<<(max(s)+4)):
        aa=[i for i in range(max(s)+4) if mask>>i&1]
        if not {0,*s}.issubset(aa):continue
        count+=1
        if all(sum(e-b in aa for b in range(4))>=2*sum(e-b in s for b in range(4)) for e in {x+b for x in s for b in range(4)}):first=len(aa) if first is None else min(first,len(aa))
      assert first==(5 if len(s)==2 else 7);completions.append(count)
    for w in r['above_transition_witnesses']:
        d,E,cross=map(Q,[w[k] for k in ['delta','energy','crossing_energy']]);s0=list(map(Q,w['support']));p0=list(map(Q,w['populations']));aa=list(map(Q,w['spectrum']))
        rv=direct(s0,p0);assert rv==Q(w['return_value']) and sum(x*y for x,y in zip(s0,p0))==E and sum(p0)==1
        assert min(y-x for x,y in zip(aa,aa[1:]))>=d
        assert all(sum(e-b in aa for b in range(4))>=2*sum(e-b in s0 for b in range(4)) for e in {x+b for x in s0 for b in range(4)})
        assert (rv<g(d,E))==(E<cross) and (rv==g(d,E))==(E==cross)
        # Derive the crossing by equality of independently formed line slopes.
        mc=(Q(81,182)-Q(3,10))/(Z+d-EC);ma=Q(3,20)/(1-d)
        assert cross==(ma*Z-mc*(Z+d))/(ma-mc)
    faults=[]
    for name in ['population','energy','completion','return']:
      row=deepcopy(r['endpoint_seven_level_witnesses'][9])
      if name=='population':row['populations'][0]=str(Q(row['populations'][0])+Q(1,100))
      elif name=='energy':row['energy']=str(Q(row['energy'])+Q(1,100))
      elif name=='completion':row['spectrum']=list(range(6))
      else:row['return_value']=str(Q(row['return_value'])-Q(1,100))
      try:check_witness(row)
      except AssertionError:faults.append(name)
      else:raise AssertionError('undetected '+name)
    for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    print('PASS K2018 separate events',counts,'completion candidates',completions,'seven-level witnesses',len(r['endpoint_seven_level_witnesses']),'post-transition witnesses',len(r['above_transition_witnesses']),'actual faults',len(faults),'hashes',len(r['inputs']))
