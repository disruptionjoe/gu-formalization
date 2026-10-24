"""Physical upper witnesses and exact onset formulas; no numerical global threshold."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
from k2010_countable_thermal_attainment import rate,shells
from k2013_energy_sensitive_thermal_cutoff import encode
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2014-unrestricted-ten-level-onset.json'
L=F(3,20);EA=F(6,5);EB=F(11,5)
def B(E):return F(63,100)-L*E
def G(d,E):return B(E)+L*d*min((E-EA)/(1+d),(EB-E)/(1-d))
def witness(d,E,shift):
    r=E-EA;w=r/(1+d) if shift=='B' else (r-d)/(1-d)
    assert 0<=w<=1
    oa,ob=(F(0),d) if shift=='B' else (d,F(0))
    a=sorted([F(i)+oa for i in range(5)]+[F(i)+ob for i in range(5)])
    pairs=sorted([(1+oa,(1-w)*F(9,10)),(3+oa,(1-w)/10),(1+ob,w*F(2,5)),(3+ob,w*F(3,5))])
    s=[x for x,p in pairs];p=[p for x,p in pairs]
    assert shells(a,s) and len(set(a))==10 and min(y-x for x,y in zip(a,a[1:]))==d
    assert sum(p)==1 and sum(x*y for x,y in zip(s,p))==E
    R=rate(s,p,F(1,2));gap=L*d*(r/(1+d) if shift=='B' else (1-r)/(1-d))
    assert R==B(E)+gap
    return dict(delta=d,energy=E,shift=shift,spectrum=a,support=s,populations=p,return_value=R,gap=gap)
def produce():
    rows=[];coeff=[];windows=[];slopes=0
    for k in range(1,20):
      E=EA+F(k,20);r=E-EA
      for d in [min(r/2,F(1,100)),min(r/2,F(1,20)),min(r/2,F(1,5))]:
       aa=witness(d,E,'A');bb=witness(d,E,'B');rows.extend([aa,bb]);assert min(aa['return_value'],bb['return_value'])==G(d,E)
       assert (bb['return_value']<=aa['return_value'])==(r<=(1+d)/2)
       q=F(15,22)*d;drop=(9-E)*q/(1-q);assert drop<6*d
       gamma=G(d,E)-B(E);qb=gamma/F(11,50);assert qb<=q
       if d<=F(1,100):
        kap=(7-3*E-20*d)/(20*(1+d));assert kap>F(1,101)
        windows.append(dict(delta=d,energy=E,preliminary_tail_upper=qb,budget_drop_upper=(9-E)*qb/(1-qb),cutoff_kappa=kap,faithful_bath_TV_radius=gamma/2,gibbs_t_radius=gamma/12,global_threshold_certified=False))
      ell=L*min(r,1-r);second=-L*r if r<=F(1,2) else L*(1-r)
      # Exact third-order remainder on the eventually winning branch.
      d=min(r/2,abs(2*r-1)/2 if r!=F(1,2) else F(1,100),F(1,100))
      gap=G(d,E)-B(E)
      rem=gap-ell*d-second*d*d
      expected=L*r*d**3/(1+d) if r<=F(1,2) else L*(1-r)*d**3/(1-d)
      assert rem==expected
      coeff.append(dict(energy=E,leading=ell,second=second,remainder_at_control_delta=rem,control_delta=d))
    for d in [F(1,100),F(1,10),F(1,2)]:
      for i in range(1,20):
       for j in range(i,20):
        x=EA+F(i,20);y=EA+F(j,20)
        assert G(d,x)>=G(d,y)+F(3,20)/(1+d)*(y-x);slopes+=1
    inputs=['explorations/conditional-build/k1998-uniform-small-spacing-transfer-2026-10-23.md','explorations/conditional-build/k2006-uniform-two-component-spacing-2026-10-24.md','explorations/conditional-build/k1975-thermal-sharp-dimension-threshold-2026-10-23.md','explorations/conditional-build/k2013-energy-sensitive-thermal-cutoff-2026-10-24.md','explorations/conditional-build/k2012-thermal-duality-gap-and-bath-stability-2026-10-24.md']
    return encode(dict(result_id='K2014',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',physical_upper_witnesses=rows,unrestricted_asymptotic_coefficients=coeff,conditional_regime_consumers=windows,counts={'physical_upper_witnesses':len(rows),'coefficient_identities':len(coeff),'conditional_window_bath_consumers':len(windows),'secant_controls':slopes},threshold={'existence':'uniform on compact interior budgets by written finite-ray and cutoff proof','numerical_threshold_executed':False,'intermediate_dimension':25,'attaining_dimension':10,'cutoff':9},scope='Exact unrestricted ten-level optimum for sufficiently small positive spacing, with compact-budget uniform existence, sharp coefficients and eventual minimum dimension10. Samples are physical upper witnesses and conditional consumers, NOT certified points inside the global regime. No complete25-level program executed.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs}))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();d=produce()
    if args.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
    else:assert d==json.loads(OUT.read_text())
    print('PASS K2014',d['counts'])
