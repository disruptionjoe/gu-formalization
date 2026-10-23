"""Physical spacing-transfer controls and exact small-spacing consumers.

Universal all-d and eventually fractional-linear claims are proved in the note;
this script does not enumerate arbitrary-d LP bases.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
import k1968_joint_thermal_finite_dimension_program as k
from k1950_global_catalyst_energy_certificates_probe import shell_return
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1998-uniform-small-spacing-transfer.json'
def overhead(d):return max(0,(d-5)//3)
def transfer(m,delta,t):
    shapes=[list(range(5))]+[list(range(3)) for _ in range(m-1)]
    supports=[[1,3]]+[[1] for _ in range(m-1)]
    weights=[F(2,5*m),F(3,5*m)]+[F(1,m)]*(m-1)
    spec=sorted(F(a)+j*delta for j,A in enumerate(shapes) for a in A)
    S=[F(a)+j*delta for j,A in enumerate(supports) for a in A]
    assert len(set(spec))==len(spec) and min(b-a for a,b in zip(spec,spec[1:]))>=delta
    assert k.shells(spec,S)
    before=shell_return(t,[F(1),F(3)],[F(2,5),F(3,5)])/m+F(m-1,2*m)
    after=shell_return(t,S,weights)
    assert after==before
    energy=sum(e*p for e,p in zip(S,weights));base=F(11,5*m)+F(m-1,m)
    assert energy-base==delta*F(m-1,2)
    assert energy<=base+overhead(len(spec))*delta
    return dict(m=m,d=len(spec),delta=str(delta),t=str(t),spectrum=list(map(str,spec)),support=list(map(str,S)),weights=list(map(str,weights)),energy=str(energy),base_energy=str(base),return_error=str(after),overhead=overhead(len(spec)))
def produce():
    transfers=[transfer(m,delta,t) for m in range(1,7) for delta in [F(1,m),F(1,2*m),F(1,11*m)] for t in [F(1,3),F(1,2),F(2,3)]]
    prior=json.loads((ROOT/'lab/process/k1968-joint-thermal-finite-dimension-program.json').read_text())
    lips=[]
    for row in prior['frontiers']:
        L=max(abs(F(p['slope'])) for p in row['pieces']);c=overhead(row['d'])
        lips.append(dict(d=row['d'],t='1/2',lipschitz_constant=str(L),energy_overhead=c,uniform_return_error_coefficient=str(L*c),spacing_ceiling=str(F(1,c+1)),spacing_sufficient_for_error_one_thousandth=None if L*c==0 else str(min(F(1,c+1),F(1,1000)/(L*c)))))
    sharp=[]
    for delta in [F(1,10000),F(1,1000),F(1,100),F(1,20),F(1,4),F(32,125)]:
        value=min(F(81,182),F(1,2)-F(2,5)/(6+5*delta));gap=value-F(13,30)
        assert gap==delta/(18+15*delta)
        assert F(25,546)*delta<=gap<=delta/18
        sharp.append(dict(delta=str(delta),value=str(value),zero_spacing_infimum='13/30',gap=str(gap),gap_over_delta=str(gap/delta)))
    chord=[]
    for E in [F(5,4),F(7,5),F(3,2),F(17,10),F(2),F(21,10)]:
        r=E-F(6,5)
        for delta in [F(1,1000),F(1,100),min(F(1,10),r/2)]:
            for shifted in ['A','B']:
                wb=(r-delta)/(1-delta) if shifted=='A' else r/(1+delta)
                aa=delta if shifted=='A' else F(0);bb=delta-aa
                A=sorted([aa+i for i in range(5)]+[bb+i for i in range(5)])
                S=[aa+1,aa+3,bb+1,bb+3]
                p=[(1-wb)*F(9,10),(1-wb)/10,wb*F(2,5),wb*F(3,5)]
                assert min(p)>=0 and k.shells(A,S)
                assert sum(e*w for e,w in zip(S,p))==E
                value=shell_return(F(1,2),S,p);gap=value-(F(63,100)-F(3,20)*E)
                expected=F(3,20)*delta*((1-r)/(1-delta) if shifted=='A' else r/(1+delta))
                assert gap==expected
                chord.append(dict(E=str(E),delta=str(delta),shifted=shifted,spectrum=list(map(str,A)),support=list(map(str,S)),weights=list(map(str,p)),gap=str(gap),sharp_leading_coefficient=str(F(3,20)*min(r,1-r))))
    return dict(result_id='K1998' ,status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',physical_transfers=transfers,exposed_face_families=chord,lipschitz_consumers=lips,sharp_eight_level_controls=sharp,exact_linear_coefficient_eight_levels='1/18',scope='All fixed d>=3,0<t<1,E>=1: V_d(E)<=F_d(delta,E)<=V_d(max(1,E-c_d*delta)), c_d=max(0,floor((d-5)/3)),0<delta<=1/(c_d+1). Uniform gap<=L_d*c_d*delta. At every fixed d,E,t, eventually F_d(delta)=V_d+ell*delta/(1+kappa*delta),ell>=0: exactly flat or positive linear onset. At t1/2,d>=10,6/5<E<11/5 the onset is strictly linear by existing nonattainment; sharp coefficient (3/20)*min(E-6/5,11/5-E) for every fixed d>=10, using the full equality-face census. Eventually the better shifted-A/shifted-B ten-level family is exactly optimal at each fixed d>=10 and interior E; validity threshold not computed, no full-spacing or growing-d uniformity claim.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1968-joint-thermal-finite-dimension-program.json','lab/process/k1990-small-dimension-thermal-frontier.json','explorations/conditional-build/k1978-thermal-spectral-spacing-2026-10-23.md','explorations/conditional-build/k1996-positive-spacing-finite-program-2026-10-23.md','explorations/conditional-build/k1975-thermal-sharp-dimension-threshold-2026-10-23.md']})
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();d=produce()
    if args.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
    else:assert d==json.loads(OUT.read_text())
    print('PASS K1998',len(d['physical_transfers']),'physical transfers;',len(d['lipschitz_consumers']),'full-curve modulus consumers;',len(d['sharp_eight_level_controls']),'sharpness controls')
