"""Independent raw reconstruction checks the full adjoint and flux identities."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
from k1979_multicoordinate_symmetric_pairing_probe import data,decode
from k1967_paired_raw_coefficient_observation_probe import mul,add,tr
ROOT=Path(__file__).resolve().parents[2]
def check(fault=None):
 r=json.loads((ROOT/'lab/process/k1982-positive-pairing-flux-obstruction.json').read_text());I,V,J,T,O=data();n=0
 if fault=='coefficient':O[0]=add((2,O[0]))
 if fault=='core':J[0]=add((2,J[0]))
 for f in r['families']:
  sign=f['sign'];Y=decode(f['dual'])
  if fault=='dual':Y[0,0]=Y.get((0,0),F(0))+1
  if fault=='mass':sign=-sign
  adj=add(*[((1 if k<7 else -1),mul(mul(O[k],Y),tr(J[k]))) for k in range(14)],(-sign,mul(Y,tr(T))))
  assert adj==I,'full raw trace certificate';n+=1
  bounds=[]
  for k,c in enumerate(f['flux_matrices']):
   C=decode(c);raw=mul(Y,tr(J[k]));expected=add(((F(1,2) if k<7 else F(-1,2)),raw),((F(1,2) if k<7 else F(-1,2)),tr(raw)))
   assert C==expected and C==tr(C),'symmetric flux coefficient';n+=1
   b=max(sum(abs(v) for (i,j),v in C.items() if i==row) for row in range(128));bounds.append(b)
   assert b==F(f['row_norm_bounds'][k]),'row norm bound'
  assert sum(bounds)==F(f['euclidean_flux_bound'])>0
  # PSD rank-one controls for the flux bound, including cross terms.
  C=list(map(decode,f['flux_matrices']))
  for a,b in [(0,1),(3,99),(40,100),(63,127)]:
   x={a:F(2),b:F(-3)};trace=sum(v*v for v in x.values())
   vals=[sum(v*x.get(i,0)*x.get(j,0) for (i,j),v in c.items()) for c in C]
   assert sum(abs(v) for v in vals)<=sum(bounds)*trace,'PSD flux bound';n+=1
  prior=json.loads((ROOT/'lab/process/k1979-multicoordinate-symmetric-pairing.json').read_text())['families'][0 if sign==-1 else 1]
  for h in map(decode,prior['identity_first_jets']):
   rhs=add(*[((1 if k<7 else -1),mul(mul(tr(O[k]),h),J[k])) for k in range(14)],(-sign,mul(h,T)))
   for z in map(decode,prior['cokernel']):
    assert sum(v*rhs.get(ij,F(0)) for ij,v in z.items())==0,'differentiated value constraints';n+=1
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 return n
if __name__=='__main__':
 n=check();caught=[]
 for f in ['coefficient','core','dual','mass']:
  try:check(f)
  except AssertionError as e:caught.append((f,str(e)))
  else:raise AssertionError('undetected mathematical fault '+f)
 print('PASS K1982 separate',n,'full identities/PSD controls;',caught)
