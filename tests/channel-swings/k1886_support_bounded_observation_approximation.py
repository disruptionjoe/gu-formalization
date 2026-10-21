#!/usr/bin/env python3
"""Exact coefficients and Hilbert-projection identities; continuum proof in K1886."""
import argparse,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1886-support-bounded-observation-approximation.json'
INPUTS=['lab/process/k1883-compact-support-observation-range.json','lab/process/k1836-k77-differential-dirac-quotient.json','lab/process/k1840-k77-conservative-variable-observation.json']
def mat(v):
 out=s.zeros(v.get('rows',16),v.get('columns',16))
 for i,j,x in v['entries']:out[i,j]=s.Rational(x)
 return out

def simplify(v):
 return s.simplify(v.rewrite(s.exp))

def produce():
 checks={}
 def ck(name,value):
  checks[name]=bool(value)
  assert value,name
 cert,src,old=[json.loads((ROOT/p).read_text()) for p in INPUTS]
 for n,(cr,sr,orr) in enumerate(zip(cert['blocks'],src['blocks'],old['blocks'])):
  T=list(map(mat,sr['T']));N=mat(cr['right_inverse_Z']);K=mat(cr['K']);S=mat(orr['repairs'][0]['S'])
  ck('full_primitive_right_inverse_'+str(n),s.Matrix.vstack(*T)*N==s.eye(12))
  ck('actual_charge_adjoint_'+str(n),S.T==24*T[0].T*K and K==s.diag(1,-1,-1,1))
 x,a,L,c=s.symbols('x a L c',positive=True)
 g=4*L**2*s.sinh(2*a*L)/a
 ck('Gram_integral',simplify(s.integrate(s.exp(2*a*x),(x,-L,L))-s.sinh(2*a*L)/a)==0)
 ck('opposite_charge_equal_norm',simplify(s.integrate(s.exp(-2*a*x),(x,-L,L))-s.sinh(2*a*L)/a)==0)
 ck('massless_limit',s.limit(g,a,0)==8*L**3)
 ck('mass_sign_independent',simplify(g.subs(a,-a)-g)==0)
 ck('translated_Gram',simplify(s.integrate(s.exp(2*a*x),(x,c-L,c+L))-s.exp(2*a*c)*s.sinh(2*a*L)/a)==0)
 ck('squared_error_factorization',simplify((1/g)-(a*s.exp(-2*a*L)/(2*L**2*(1-s.exp(-4*a*L)))))==0)
 ck('strict_monotonicity_formula',simplify(s.diff(g,L)/g-2/L-2*a/s.tanh(2*a*L))==0)
 return dict(result_id='K1886',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',formula={'cube_gram_prefactor':4,'cube_gram_exponent':2,'massless_volume_factor':8,'massive_squared_error_prefactor':'1/2','massive_tail_exponent':4,'optimal_squared_error':'q^T G^-1 q'},scope={'infimum_over_Cc_sources':True,'nonzero_charge_smooth_target_attained':False,'fixed_support_floor':True,'source_energy_bound':False,'native_GU':False,'rotating_requires_repaired_map':True},checks=checks,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS})
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args();v=produce()
 if args.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1886',len(v['checks']),'exact matrix/integral identities;',len(v['inputs']),'input pins')
