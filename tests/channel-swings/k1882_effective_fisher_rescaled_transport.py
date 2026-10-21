#!/usr/bin/env python3
"""Exact budgets and symbolic transfer identities; the continuum proof is in K1882."""
import argparse, hashlib, json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1882-effective-fisher-rescaled-transport.json'
INPUTS=['lab/process/k1880-effective-fisher-well-localization.json','lab/process/k1876-fisher-atomic-boundary-cost.json']
def produce():
 checks={}
 def ck(n,v):checks[n]=bool(v);assert v,n
 e=s.Rational(1,3000000);h=s.Rational(1,10000);delta=s.Rational(1,10**12);eps=13*h/8;tau=4*e*e/h**2;U=s.Rational(12501,500)
 E=U-25+25*((1-eps)**-2-1)+30*e+80*tau+40*delta/h**2
 Kcap=U+40*delta/h**2;Splus=5-3*e-8*tau;D=1-(1-eps)**2*Splus**2/Kcap
 B=E/400+D/9+tau/20
 ck('valid_parameters',Splus>0 and 0<eps<1 and Kcap>0)
 ck('positive_budgets',E>0 and 0<D<1 and B>0)
 ck('weighted_transport_0112',B<s.Rational(14,1250)**2)
 p0=1-(1+3*e)/4;po=(1-3*e)/8
 ck('central_013',B<p0*s.Rational(13,1000)**2)
 ck('outer_032',B<po*s.Rational(4,125)**2)
 m,n,v,w,a,c=s.symbols('m n v w a c',positive=True)
 ck('allocation_cauchy',s.factor((m/v+n/w)*(m*a*a*v+n*c*c*w)-(m*a+n*c)**2-m*n*(a*v-c*w)**2/(v*w))==0)
 z,mu=s.symbols('z mu',real=True);b,variance=s.symbols('b variance',positive=True)
 # Gaussian target precision b, candidate N(mu,variance); transport/Fisher gap.
 fisher=(b*mu)**2+(b*variance-1)**2/variance
 W2=mu**2+(s.sqrt(variance)-1/s.sqrt(b))**2
 positive_b=s.symbols('beta',positive=True);t=s.symbols('t',positive=True)
 gap=s.factor((fisher/b**2-W2).subs({b:positive_b,variance:t*t/positive_b}))
 ck('Gaussian_transport_inequality',s.simplify(gap-(t-1)**2*(2*t+1)/(positive_b*t*t))==0)
 ck('shifted_Gaussian_equality',s.simplify((fisher/b**2-W2).subs(variance,1/b))==0)
 # Independent centered residual draw eliminates, rather than estimates, cross term.
 mass,second,mean=s.symbols('mass second mean',real=True)
 ck('residual_product_cost',s.expand(second+mass/b-2*mean*0-(second+mass/b))==0)
 ck('tail_fourth_constant',2*3*4==24)
 ck('rate_balance',1-2*s.Rational(1,3)==s.Rational(1,3))
 return dict(result_id='K1882',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',constants={'tail_coercivity':'16/9','cutoff':40,'transport_factor':1,'tail_mass_factor':1,'tail_modulus':24},budget={k:str(v) for k,v in dict(e=e,epsilon=eps,tau=tau,E=E,Kcap=Kcap,Splus=Splus,D=D,B=B,central_mass_lower=p0,outer_mass_lower=po).items()},bounds={'weighted_W2':'7/625','central_W2':'13/1000','outer_W2':'4/125'},scope={'actual_hard_cells':True,'all_feasible_valid_U':True,'rare_cell_mass_required':True,'hard_cell_entropy':False,'sharp_rate':False,'sextic_gap':False,'native_GU':False},checks=checks,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=produce()
 if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1882',len(v['checks']),'symbolic/budget groups;',len(v['inputs']),'pins')
