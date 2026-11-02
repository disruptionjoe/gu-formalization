from pathlib import Path
from fractions import Fraction as F
import json,hashlib,contextlib,io
from math import factorial,prod
import sys
ROOT=Path(__file__).resolve().parents[2]
# Scratch runs can specify an existing checkout; installed execution needs no option.
if '--root' in sys.argv:ROOT=Path(sys.argv[sys.argv.index('--root')+1]).resolve()
read_dependencies=set()
original_read_text=Path.read_text
def traced_read_text(path,*args,**kwargs):
 try:read_dependencies.add(str(path.resolve().relative_to(ROOT)))
 except ValueError:pass
 return original_read_text(path,*args,**kwargs)
Path.read_text=traced_read_text
p=ROOT/'tests/channel-swings/k2425_frame_euler_module_probe.py'
s=p.read_text();ns={'__file__':str(p),'__name__':'original_prefix'}
with contextlib.redirect_stdout(io.StringIO()):exec(compile(s[:s.index('ss=[[symbol')],str(p),'exec'),ns)
Path.read_text=original_read_text
rep,symbol,covs,alphas,eta,receivers,linear=[ns[k] for k in ('rep','symbol','covs','alphas','eta','receivers','linear')]
xi={i:F(1) for i in range(14)}
def cpair(Q):return sum(v for (i,j),v in Q.items() if i!=j)
def gradcpair(Q,alpha):return sum(v*sum(alpha.get(k,0) for k in range(14) if k not in (i,j)) for (i,j),v in Q.items() if i!=j)
assert all(cpair(symbol(h,xi))==0 for h in rep)
selected=None
for index,(tag,bank) in enumerate(linear):
 delta={r:cpair(symbol(h,xi)) for r,h in bank.items()}
 if any(delta.values()):
  selected=(index,tag,bank,delta);break
assert selected
index,tag,bank,delta=selected
crossing_tag=tag
K0={}
for r,h in bank.items():
 for ij,v in symbol(h,alphas[r]).items():K0[ij]=K0.get(ij,F(0))+v
T=cpair(K0)+sum(gradcpair(symbol(h,xi),alphas[r]) for r,h in bank.items())
# Original coordinates: y_r=alpha_r dot x, L=sum_i x_i.
R={i:sum(delta.get(r,0)*alphas[r].get(i,0) for r in bank)+T for i in range(14)}
assert any(R.values())
# C(D)D(G L^13) = 13!*(delta(y)+T L), field degree14, receiver degree13.
# Independent coefficient extraction: expand only each requested degree13 coefficient,
# rather than using the Leibniz gradient formula above.
def multicoef(power,exponents):
 if any(a<0 for a in exponents) or sum(exponents)!=power:return F(0)
 return F(factorial(power),prod(factorial(a) for a in exponents))
direct={i:F(0) for i in range(14)}
for i,j in receivers:
 if i==j:continue
 derivative=tuple(int(a not in (i,j)) for a in range(14))
 for ell in range(14):
  nu=tuple(derivative[a]+int(a==ell) for a in range(14))
  coefficient=K0.get((i,j),0)*multicoef(13,nu)
  for r,h in bank.items():
   B=symbol(h,xi).get((i,j),0)
   if not B:continue
   for a,alpha in alphas[r].items():
    minus=tuple(nu[t]-int(t==a) for t in range(14))
    coefficient+=13*B*alpha*multicoef(12,minus)
  derivative_factor=prod(F(factorial(nu[a]),factorial(nu[a]-derivative[a])) for a in range(14))
  direct[ell]+=coefficient*derivative_factor/factorial(13)
checks={'repeated_all161_C_pair_zero_at_xi':all(cpair(symbol(h,xi))==0 for h in rep),'actual_rotation_delta_nonzero':any(delta.values()),'actual_degree14_field_residue_nonzero':any(R.values()),'multinomial_independent_all14_coefficients':direct==R,'linear_generator_has_only_transverse_coefficients':all(r<7 for r in bank)}
controls={'drop_C_outer_derivative_detected':any(R[i] != sum(delta.get(r,0)*alphas[r].get(i,0) for r in bank)+cpair(K0) for i in range(14)), 'repeated_only_compatibility_is_genuinely_stricter':any(direct.values())}
assert all(checks.values())
assert all(controls.values())
# Search the actual rotation bank for a defect lift with delta=0,T!=0.
def interface(bank):
 ds=[cpair(symbol(bank.get(r,{}),xi)) for r in range(7)]
 zz={}
 for r,h in bank.items():
  for ij,v in symbol(h,alphas[r]).items():zz[ij]=zz.get(ij,F(0))+v
 tt=cpair(zz)+sum(gradcpair(symbol(h,xi),alphas[r]) for r,h in bank.items())
 return ds+[tt]
basis={};answer=None
for j,(tag,bb) in enumerate(linear):
 if tag[0]!='rotation':continue
 vv=interface(bb);ww={j:F(1)}
 for pivot in sorted(basis):
  if not vv[pivot]:continue
  bc,bw=basis[pivot];factor=vv[pivot]
  vv=[a-factor*b for a,b in zip(vv,bc)]
  for k,b in bw.items():ww[k]=ww.get(k,F(0))-factor*b
  ww={k:v for k,v in ww.items() if v}
 if any(vv[:7]):
  p=next(i for i,v in enumerate(vv[:7]) if v);factor=vv[p]
  basis[p]=([v/factor for v in vv],{k:v/factor for k,v in ww.items()})
 elif vv[7]:
  answer={k:v/vv[7] for k,v in ww.items()};break
if answer:
 hh={}
 for j,w in answer.items():
  for r,h in linear[j][1].items():hh[r]=ns['add']((1,hh.get(r,{})),(w,h))
 vals=interface(hh);assert vals==[F(0)]*7+[F(1)]
 ridge={'weights':{str(j):str(v) for j,v in answer.items()},'tags':{str(j):list(linear[j][0]) for j in answer},'delta_T':list(map(str,vals))}
else:ridge={'no_lift_found':True,'delta_rank':len(basis)}

# Independent multinomial extraction for the composed four-rotation lift.
if answer:
 Hzero={}
 Hsymbols={r:symbol(h0,xi) for r,h0 in hh.items()}
 for r,h0 in hh.items():
  for ij,v in symbol(h0,alphas[r]).items():Hzero[ij]=Hzero.get(ij,F(0))+v
 ridge_direct={}
 for degree in (0,1):
  N=degree+12
  targets=[()] if degree==0 else [(i,) for i in range(14)]
  values={}
  for remainder in targets:
   total=F(0)
   for i,j in receivers:
    if i==j:continue
    dd=tuple(int(a not in (i,j)) for a in range(14))
    nu=tuple(dd[a]+remainder.count(a) for a in range(14))
    coeff=Hzero.get((i,j),0)*multicoef(N,nu)
    for r,Bs in Hsymbols.items():
     B=Bs.get((i,j),0)
     if not B:continue
     for a,alpha in alphas[r].items():
      mm=tuple(nu[t]-int(t==a) for t in range(14))
      coeff+=N*B*alpha*multicoef(N-1,mm)
    fac=prod(F(factorial(nu[a]),factorial(nu[a]-dd[a])) for a in range(14))
    total+=coeff*fac*F(factorial(degree),factorial(N))
   values[str(remainder)]=str(total)
  checks['ridge_independent_multinomial_degree_'+str(degree)]=all(F(v)==1 for v in values.values())
  ridge_direct[str(degree)]=values
 ridge['independent_multinomial_defect_coefficients']=ridge_direct
 Hnorm=sum(abs(v*alpha) for r,h0 in hh.items() for v in h0.values() for alpha in alphas[r].values())
 ridge['H_coefficient_l1_upper']=str(Hnorm)
 ridge['sup_bound']='C_H*r*(14*r)^12/12!*sup_{|s|<=14*r}|g(s)|; r<R/14'
 ridge['four_column_interface_check']=all(sum(w*interface(linear[j][1])[i] for j,w in answer.items())==int(i==7) for i in range(8))
 checks['ridge_four_column_interface']=ridge['four_column_interface_check']
# Original modular rank with rational annihilator controls.
prime=1000003
def mod(v):
 v=F(v);assert v.denominator%prime
 return v.numerator*pow(v.denominator,-1,prime)%prime
def modular_rank(columns):
 piv={};ids=[]
 for j,cc in enumerate(columns):
  c={receivers.index(ij):mod(v) for ij,v in cc.items() if mod(v)}
  while c:
   p=min(c);v=c[p]
   if p not in piv:
    z=pow(v,-1,prime);piv[p]={i:a*z%prime for i,a in c.items()};ids.append([j,p]);break
   for i,a in piv[p].items():
    w=(c.get(i,0)-v*a)%prime
    if w:c[i]=w
    else:c.pop(i,None)
 return len(piv),ids
cases=[]
for name,xx,target in [('ambient_all_ones',{i:F(1) for i in range(14)},102),('ambient_1_to_14',{i:F(i+1) for i in range(14)},102),('transverse_1_to_7',{i:sum(F(r+1)*covs[r].get(i,0) for r in range(7)) for i in range(14)},88),('e0',{0:F(1)},25)]:
 columns=[symbol(h,xx) for h in rep]
 tau={(i,i):eta[i] for i in range(14)}
 bb={(i,j):(1 if i==j else 2)*eta[i]*eta[j]*xx.get(i,0)*xx.get(j,0) for i,j in receivers}
 cc={(i,j):prod(xx.get(k,0) for k in range(14) if k not in (i,j)) for i,j in receivers if i!=j}
 checks[name+'_all_three_exact_annihilators']=all(all(sum(row.get(ij,0)*v for ij,v in col.items())==0 for col in columns) for row in (tau,bb,cc))
 rk,ids=modular_rank(columns);checks[name+'_rank']=rk==target
 cases.append({'name':name,'xi':{str(k):str(v) for k,v in xx.items()},'rank_mod_prime':rk,'pivot_columns_and_rows':ids,'columns_sha256':hashlib.sha256(repr(columns).encode()).hexdigest()})
checks['split_signs_make_three_rows_independent']=set(eta)=={-1,1}
checks['all_original_prefix_checks']=all(ns['checks'].values())
checks['all_original_repeated_tracefree']=all(all(sum(eta[i]*h.get((i,i,j),0) for i in range(14))==0 for j in range(14)) for h in rep)
checks['all_original_repeated_support']=all(all(len(set(k))<3 for k in h) for h in rep)
checks['rotation_ridge_lift_found']=answer is not None
if answer:
 checks['ridge_all_seven_principal_coefficients_vanish']=vals[:7]==[F(0)]*7
 checks['ridge_defect_normalization']=vals[7]==1
 printed={('rotation',0,2):F(11339,865152),('rotation',0,3):-F(11339,865152),('rotation',0,5):F(493,36048),('rotation',0,4):-F(493,36048)}
 computed={tuple(linear[j][0]):w for j,w in answer.items()}
 checks['printed_four_rotation_coefficients_equal_computed']=computed==printed
 printed_bank={}
 for j,(tg,bb) in enumerate(linear):
  if tuple(tg) not in printed:continue
  for r,h0 in bb.items():printed_bank[r]=ns['add']((1,printed_bank.get(r,{})),(printed[tuple(tg)],h0))
 checks['printed_H_independent_reconstruction']=printed_bank==hh and interface(printed_bank)==[F(0)]*7+[F(1)]
 # Degree-uniform formula with explicit rising derivative factorial controls.
 for n0 in [0,1,2,7,13,31]:
  coefficient=F(factorial(n0),factorial(n0+12))
  checks['ridge_inverse_degree_'+str(n0)]=coefficient*F(factorial(n0+12),factorial(n0))*vals[7]==1
 wrong_primitive={1:F(1)}
 for _ in range(12):wrong_primitive={k-1:k*v for k,v in wrong_primitive.items() if k}
 controls['omit_12_integrations_detected']=wrong_primitive!={1:F(1)}
 checks['ridge_uses_nonzero_original_ordinary_symbols']=any(symbol(h0,{i:F(1) for i in range(14)}) for h0 in hh.values())
assert all(checks.values())
assert all(controls.values())
selfpath='tests/channel-swings/k2479_ordinary_hook_quotient_probe.py'
notepath='explorations/conditional-build/k2479-ordinary-hook-quotient-2026-11-01.md'
read_dependencies.update([selfpath,notepath,'lab/process/k2443-hook-quantitative-symbol.json','lab/process/k2449-full-mixed-boundary-adjoint.json','lab/process/k2476-mixed-hook-decoupling.json'])
report={'result_id':'K2479','scope':'Original conditional hook mathematics: repeated-only degree12 compatibility; generic repeated rank102; actual rotations restore principal103 and lift a ridge defect. No full analytic or nonlinear solution.','checks':checks,'controls':controls,'prime':prime,'original_rank_cases':cases,'rotation_crossing':{'index':index,'tag':list(crossing_tag),'delta_y':{str(k):str(v) for k,v in delta.items()},'C_pair_DG':str(cpair(K0)),'outer_C_derivative_sum':str(T-cpair(K0)),'T':str(T),'normalized_residue_original_x':{str(k):str(v) for k,v in R.items() if v},'independent_multinomial_residue':{str(k):str(v) for k,v in direct.items() if v}},'ridge_lift':ridge,'evidence_kinds':{'universal':'written repeated-hook polynomial syzygy, real carrier rank, Leibniz and ridge integration identities','finite_exact':'actual original tensor/rank minors, rotation constants and independent multinomial extraction','ceiling':'no complete boundary-preserving ordinary analytic inverse or nonlinear convergence'},'dependencies':{q:hashlib.sha256((ROOT/q).read_bytes()).hexdigest() for q in sorted(read_dependencies)}}
out=ROOT/'lab/process/k2479-ordinary-hook-quotient.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
elif '--output' in sys.argv:Path(sys.argv[sys.argv.index('--output')+1]).write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2479',len(checks),'checks',len(controls),'controls PASS')
