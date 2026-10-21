#!/usr/bin/env python3
"""Exact nonlinear residual controls; the zero-crossing theorem is analytic."""
import argparse,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1875-nonlinear-moving-zero-obstruction.json'
def mat(x):
 m=s.zeros(x.get('rows',16),x.get('columns',16))
 for i,j,v in x['entries']:m[i,j]=s.Rational(v)
 return m
def produce():
 src=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text());en=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text());old=json.loads((ROOT/'lab/process/k1840-k77-conservative-variable-observation.json').read_text());D=list(map(mat,src['target_D']));ds=[x/24 for x in D];checks={};r,v,z,a,m0=s.symbols('r v z a m0',real=True);f=r+r**3
 def ck(name,value):checks[name]=bool(value);assert value,name
 for ix,(sr,er,kr) in enumerate(zip(src['blocks'],en['blocks'],old['blocks'])):
  T=list(map(mat,sr['T']));A=list(map(mat,er['matrices']));H=mat(er['H']);Hi=H.inv();K=mat(kr['full_conservative_kernel'])
  G=s.Matrix([[x for i in range(3) for x in (T[i]*Hi*s.Matrix(4,16,row[126:]).T-s.Matrix(4,16,row[126:])*Hi*T[i].T)] for row in K.tolist()]).T
  Bmap=K[:,120:126].T
  ck('fixed_target_freedom38_'+str(ix),Bmap.rank()==6 and K.rows-Bmap.rank()==38)
  ck('gram_first_derivative_image4_'+str(ix),G.rank()==4)
  ck('massless_offset_gram_image4_'+str(ix),(G*s.Matrix.hstack(*Bmap.nullspace())).rank()==4)
  for j,rep in enumerate(kr['repairs']):
   C=mat(rep['C']);B=mat(rep['B']);S=mat(rep['S']);tag=f'{ix}_{j}'
   ck('first_order_'+tag,all(T[i]*C-B*T[i]+S*A[i]-ds[i]*S==s.zeros(4,16) for i in range(3)))
   ck('conservation_'+tag,H*C+C.T*H==s.zeros(16) and B+B.T==s.zeros(4))
   ck('nonlinear_cross_'+tag,S*C-B*S==s.zeros(4,16))
   ck('static_derivative_'+tag,T[0]*C-ds[0]*S==s.zeros(4,16))
   L=s.diff(f,r)*(T[0]*C+(v*s.eye(4)-ds[0])*S)
   ck('nonlinear_derivative_'+tag,s.simplify(L-v*(1+3*r*r)*S)==s.zeros(4,16))
   ck('nonzero_mass_tangent_'+tag,B!=s.zeros(4) and S.rank()==4)
 m=m0/(1-a*m0*z);ck('Riccati_identity',s.simplify(s.diff(m,z)-a*m*m)==0)
 ck('Riccati_pole',s.simplify((1-a*m0*z).subs(z,1/(a*m0)))==0)
 ck('tanh_zero',s.tanh(z).subs(z,0)==0 and s.diff(s.tanh(z),z).subs(z,0)==1)
 ck('sech_ratio',s.simplify(s.diff(1/s.cosh(z),z)/(1/s.cosh(z))**2+s.sinh(z))==0)
 ck('gaussian_ratio',s.simplify(s.diff(s.exp(-z*z),z)/s.exp(-z*z)**2+2*z*s.exp(z*z))==0)
 ck('reciprocal_control',s.simplify(s.diff(1/(1+z),z)/(1/(1+z))**2)==-1)
 n0,n1,n2,L,kappa,amp=s.symbols('n0 n1 n2 L kappa amp');poly=kappa*(amp**2-r**2)*L+n0+r*n1+r*r*n2
 ck('affine_kink_constant',s.expand(poly).coeff(r,0)==n0+kappa*amp**2*L)
 ck('affine_kink_linear',s.expand(poly).coeff(r,1)==n1)
 ck('affine_kink_quadratic',s.expand(poly).coeff(r,2)==n2-kappa*L)
 ck('affine_kink_sufficient',s.simplify(poly.subs({n0:-kappa*amp**2*L,n1:0,n2:kappa*L}))==0)
 return {'result_id':'K1875','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','residual':{'time_sign':1,'nonlinear_derivative_coefficients':[1,0,3],'riccati_denominator_sign':-1},'scope':{'fixed_symbols':True,'fixed_pairings':True,'C1_mass_local':True,'zero_normalized':True,'nonzero_mass_plane_tangent':True,'nonzero_speed':True,'finite_zero_for_nonconstant_profile':False,'exponential_zero_tail':False,'all_moving_backgrounds_excluded':False,'inverse_tail_solution_constructed':False,'native_GU_verdict':False},'checks':checks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1832-k77-common-energy-form.json','lab/process/k1836-k77-differential-dirac-quotient.json','lab/process/k1840-k77-conservative-variable-observation.json','lab/process/k1873-traveling-mass-compatibility.json','tests/channel-swings/k1873_traveling_mass_compatibility_probe.py']}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();z=produce()
 if a.write:OUT.write_text(json.dumps(z,indent=2)+'\n')
 else:assert z==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1875',len(z['checks']),'exact algebra groups;',len(z['inputs']),'pins')
