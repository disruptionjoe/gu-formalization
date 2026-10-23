"""Nine-level wide-spacing dominance and a general finite-placement primitive.

Exact all-temperature dominance rests on preserved pair gaps and added
nonnegative incoming shell flows; counts are finite identities, not GU evidence.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import combinations,product
import argparse,json,hashlib
import k1968_joint_thermal_finite_dimension_program as k
import k1994_nine_level_thermal_reduction as n
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1996-positive-spacing-finite-program.json'
PURE=[(a,b) for a in range(1,4) for b in range(1,4) if a+b<=4]
def first_shift(A,B,delta):
    """Smallest x>=0 with |a-b-x|>=delta for every pair."""
    x=F(0)
    for z in sorted({F(a-b) for a in A for b in B}):
        if z-delta<x<z+delta:x=z+delta
    assert all(abs(a-b-x)>=delta for a in A for b in B)
    return x

def placement(shapes,order,delta):
    """K1978 lower-constraint potentials, or None for an infeasible order.

    order is a shuffle of (component, offset) pairs preserving each shape order.
    The returned energies are actual noncolliding levels, including new resonances.
    """
    assert sorted(order)==sorted((i,a) for i,A in enumerate(shapes) for a in A)
    edges=[(i,j,delta+a-b) for (i,a),(j,b) in zip(order,order[1:])]
    y=[F(0)]*len(shapes)
    for turn in range(len(shapes)):
        z=y.copy()
        for i,j,w in edges:z[j]=max(z[j],y[i]+w)
        if z==y:return y
        y=z
    if any(y[j]<y[i]+w for i,j,w in edges):return None
    return y

def witnesses():
    prior=json.loads((ROOT/'lab/process/k1994-nine-level-thermal-reduction.json').read_text())
    blocks=[(tuple(r['S']),tuple(r['A'])) for r in prior['pareto_blocks']]
    rows=[]
    for r in n.improving_census():
        A,S=tuple(r['spectrum']),tuple(r['support']);g=S[1]-S[0]
        for l,h in PURE:
            B=(0,l,l+h)
            for side in [0,1]:
                sh=first_shift(A,B,F(3,4)) if side==0 else first_shift(B,A,F(3,4))
                integer=sh-F(3,4);assert integer.denominator==1
                # Because differences are integers, this same right endpoint
                # integer+delta is the least feasible shift for 1/2<delta<=1.
                low=F(S[0])+(integer+F(1,2) if side else 0)
                pure=F(l)+(0 if side else integer+F(1,2))
                candidates=[]
                for T,C in blocks:
                    if len(T)!=3:continue
                    for i,j in combinations(range(3),2):
                        q=3-i-j
                        if T[j]-T[i]==g and T[i]<=low and T[q]<=pure:
                            candidates.append((T,C,i,j,q))
                assert candidates,(A,S,B,side)
                T,C,i,j,q=min(candidates)
                rows.append(dict(A=A,S=S,B=B,pure=l,shifted='A' if side else 'B',shift_integer=int(integer),half_right_pair_lower=str(low),half_right_pure=str(pure),target_spectrum=C,target_support=T,pair_indices=[i,j],pure_index=q))
    assert len(rows)==204
    return rows

def produce():
    rows=witnesses();checks=0
    for r in rows:
        C,T=r['target_spectrum'],r['target_support'];i,j=r['pair_indices'];q=r['pure_index']
        assert len(C)<=9 and k.shells(C,T)
        for delta in [F(51,100),F(2,3),F(3,4),F(99,100),F(1)]:
            sh=r['shift_integer']+delta;aa=sh if r['shifted']=='A' else F(0);bb=sh-aa
            spec=sorted([aa+a for a in r['A']]+[bb+b for b in r['B']]);S=[aa+s for s in r['S']]+[bb+r['pure']]
            assert min(b-a for a,b in zip(spec,spec[1:]))>=delta
            assert k.shells(spec,S) and T[i]<=S[0] and T[j]<=S[1] and T[q]<=S[2]
            checks+=1
    prior=json.loads((ROOT/'lab/process/k1994-nine-level-thermal-reduction.json').read_text())
    bs=[(tuple(r['S']),tuple(r['A'])) for r in prior['pareto_blocks']]
    half,connected,count,extra=n.compute(bs,F(1,2));saved=[{a:None if b is None else F(b) for a,b in p.items()} for p in prior['connected_curve']]
    assert connected==saved
    cuts=sorted({p['lo'] for p in half+connected}|{p['hi'] for p in half+connected if p['hi'] is not None})
    jumps=[]
    for lo,hi in zip(cuts,cuts[1:]+[None]):
        x=lo+1 if hi is None else (lo+hi)/2
        a=next(p for p in connected if p['lo']<=x and(p['hi'] is None or x<=p['hi']))
        b=next(p for p in half if p['lo']<=x and(p['hi'] is None or x<=p['hi']))
        m=a['slope']-b['slope'];c=a['intercept']-b['intercept']
        assert m*lo+c>=0 and(hi is None or m*hi+c>=0)
        jumps.append(dict(lo=lo,hi=hi,jump_slope=m,jump_intercept=c))
    positive=[r for r in jumps if r['jump_slope'] or r['jump_intercept']]
    assert positive[0]['lo']==F(1117,743) and positive[-1]['hi']==F(79,45)
    return dict(result_id='K1996',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',dominance_witnesses=rows,physical_controls=checks,temperature='1/2',half_spacing_curve=k.encode(half),wide_spacing_curve=k.encode(connected),half_right_jump=k.encode(jumps),budget_controls=[dict(energy=str(e),half=str(k.evaluate(half,e)),wide=str(k.evaluate(connected,e)),jump=str(k.evaluate(connected,e)-k.evaluate(half,e))) for e in [F(7,5),F(18,11),F(2),F(3),F(4),F(5)]],scope='For all0<t<1,E>=1,1/2<delta<=1, F9(delta,E,t)=F9(1,E,t), computed by connected integer spectra. General positive-spacing fixed-d finite actual-spectrum algorithm and rational optimal energy/populations/value at rational delta,E,t follow from reused K1978 potentials plus shell realization. No efficient complexity, all-d closed curve, rational unitary, GU or novelty claim.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['tests/channel-swings/k1968_joint_thermal_finite_dimension_program.py','tests/channel-swings/k1994_nine_level_thermal_reduction.py','lab/process/k1994-nine-level-thermal-reduction.json','explorations/conditional-build/k1978-thermal-spectral-spacing-2026-10-23.md']})
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();d=k.encode(produce())
    if a.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
    else:assert d==json.loads(OUT.read_text())
    print('PASS K1996:204 dominance witnesses;',d['physical_controls'],'physical controls;',len(d['half_spacing_curve']),'half pieces; wide',len(d['wide_spacing_curve']));print(d['budget_controls'])
