"""Normalized Slater constants and sharper actual finite-cut repair certificates."""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json
from k1942_complete_scalar_energy_duality import active_solve,green,mean,INTERVALS
from k1963_effective_scalar_cut_certificates import graph_certificate,phi0_integral
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1965-scalar-uniform-lipschitz-certificates.json'
M=F(23,100);M0=F(22451259,97656250);U0=F(78227902689379,19531250000000)
def slope_bound(cuts,lam):
    slopes=[]
    for a,b in INTERVALS:
        L=b-a;base=F(-1) if a==-1 else F(1)
        for x in sorted({a,b}|{t for t in cuts if a<t<b}):
            value=base
            for t,w in zip(cuts,lam):
                v=max(F(0),min(L,t-a));raw=v-v*v/(2*L)-min(v,x-a)
                projected=raw-mean(t)/F(5,6)*(a+b-2*x)/2
                value-=w*projected
            slopes.append(value)
    return max(map(abs,slopes))
def calculate():
    Delta=M-M0;S=(U0-4)/(2*Delta);Lstar=1+F(8,15)*S;checks=3;rows=[]
    assert Delta>0 and U0>4 and S>0
    for h,s in [(F(1,2),F(1,2)),(F(1,16),F(7,16))]:
        cuts=[-s,s];_,_,la,J=active_solve(cuts,M);la=list(map(F,la));J=F(J);L=slope_bound(cuts,la)
        vals=[phi0_integral(-3+i*h,-3+(i+1)*h)-sum(w*(green(-3+(i+1)*h,t)-green(-3+i*h,t)) for t,w in zip(cuts,la)) for i in range(int(6/h))]
        cert=graph_certificate(h,vals);assert F(cert['minimum_deficit'])==0
        eps=F(2,3)*h*(L+M);theta=eps/(Delta+eps);upper=(1-theta)*J+theta*U0
        assert L<=Lstar and J<upper<U0
        assert (1-theta)*(M+eps)+theta*M0==M
        normsum=sum(w*(3-abs(t))*(6+abs(t)) for w,t in zip(la,cuts))
        assert normsum<=S,'normalized dual multiplier mass'
        rows.append(dict(h=str(h),halfcut=str(s),energy=str(J),slope=str(L),amplitude_allowance=str(eps),mixing=str(theta),upper=str(upper),improvement=str(U0-upper),normalized_multiplier_mass=str(normsum),graph=cert));checks+=5
    old=F(27930071724033303,6973333745000000)
    assert F(rows[-1]['upper'])<old;checks+=1
    # All normalized cut forcings have ||f||1<=1/3; projected mean<=1/5.
    assert F(1,2)/F(5,6)/3==F(1,5)
    assert F(1,3)+F(1,5)==F(8,15);checks+=2
    return dict(result_id='K1965',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_controls=checks,constants=dict(M=str(M),M0=str(M0),U0=str(U0),Delta=str(Delta),multiplier_mass=str(S),uniform_slope=str(Lstar),linear_amplitude_coefficient=str(F(2,3)*(Lstar+M))),certificates=rows,inputs={x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in ['lab/process/k1942-complete-scalar-energy-duality.json','lab/process/k1944-optimized-scalar-pulse-certificate.json','lab/process/k1963-effective-scalar-cut-certificates.json']},scope='Uniform Lipschitz finite minimizers and continuum phase; O(h) energy-gap certificate. No exact continuum optimum or explicit new pulse bytes.')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=calculate()
    if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert r==json.loads(OUT.read_text())
    print('PASS K1965',r['exact_controls'],r['constants'],r['certificates'][-1]['upper'])
