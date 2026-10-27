"""Actual inherited-current/raw-image consumer. Universal PDE proof is in the note."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
import sympy as s
import k2120_inherited_core_current_probe as prev
q=prev.q;adj=prev.adj;tr=prev.trace;comm=prev.comm;dec=prev.dec
ROOT=Path(__file__).resolve().parents[2]
INPUTS=prev.INPUTS+['lab/process/k2028-all-grade-raw-common-form.json','tests/channel-swings/k2120_inherited_core_current_probe.py']
OUT=ROOT/'lab/process/k2123-same-current-potential-dynamics.json'
def native(fault=None):
 jc={};cs=[{} for _ in range(3)]
 for k,b in enumerate(json.loads((ROOT/INPUTS[0]).read_text())['blocks']):
  for (r,c),v in q.mul(dec(b['basis']),dec(b['section'])).items():jc[b['coordinates'][r],4*k+c]=v
  for ell in range(3):cs[ell].update({(4*k+r,4*k+c):v for (r,c),v in dec(b['quotient_generators'][ell]).items()})
 m=dec(json.loads((ROOT/INPUTS[1]).read_text())['scalar']['repair'][0]['M'])
 if fault=='injection':jc[min(jc)]*=2
 fc=q.mul(q.tr(jc),q.mul(q.H,q.mul(q.raw(0),jc)))
 mf=q.mul(q.tr(m),q.mul(fc,m));t=q.add((F(140,9),fc),(F(140,9),mf));a=q.add((F(140,27),fc),(F(-140,27),mf))
 v=q.mul(q.mul(cs[0],cs[1]),cs[2]);z=q.mul(a,q.add((-1,v)));r={(j^4,j):F(-1 if j>=64 else 1) for j in range(128)}
 p=q.add((F(1,4),q.mul(q.add((1,q.I),(s.I,t)),q.add((1,q.I),(1,r)))))
 return cs,m,fc,t,z,r,p

def checks(fault=None):
 cs,m,fc,t,z,r,p=native(fault);ck={};put=lambda k,x:ck.__setitem__(k,bool(x));S=q.add((s.I,fc));c=F(9,280)
 im=json.loads((ROOT/'lab/process/k2028-all-grade-raw-common-form.json').read_text())['complex_hermitian_branch'];basis=list(map(dec,im['induced_basis']));coords=[[F(x) for x in row] for row in im['image_coordinates']]
 if fault=='image-coordinate':coords[0][0]*=2
 for i,(b,row) in enumerate(zip(basis,coords)):
  put('raw-image-'+str(i),b==q.add(*[(a,B) for a,B in zip(row,[q.I]+cs)]))
 ids=[0,1,11,10]
 if fault=='right-inverse-order':ids[-1],ids[-2]=ids[-2],ids[-1]
 put('right-inverse',all(q.add((F(3,2),basis[j]))==B for j,B in zip(ids,[q.I]+cs)))
 put('same-current',q.mul(p,q.mul(S,p))==q.add((c,p)))
 pot=q.add((2,q.I),(3,cs[0]),(-5,cs[1]),(7,cs[2]));mass=q.add((-s.I,m))
 if fault=='mass-adjoint':mass=q.add((1,m))
 if fault=='nonreal-potential':pot=q.add((1,pot),(s.I,q.I))
 h=q.add((1,pot),(1,mass))
 put('projector-reduces',not comm(p,h));put('compressed-hermitian',q.mul(p,q.mul(adj(h),p))==q.mul(p,q.mul(h,p)))
 put('compressed-current-conserved',q.mul(p,q.mul(q.add((1,q.mul(adj(h),S)),(-1,q.mul(S,h))),p))=={})
 put('full-current-mass-not-conserved',bool(comm(S,m)))
 n=[F(2,3),F(1,3),F(2,3)];cn=q.add(*[(a,B) for a,B in zip(n,cs)])
 if fault=='principal-speed':cn=q.add((2,cn))
 put('unit-normal-speed',q.mul(cn,cn)==q.I)
 x,y,t0=s.symbols('x y t',real=True);aa=[0,0,3*s.sin(x),0];chi=t0*x*y;xx=[t0,x,y,s.Symbol('z')]
 shifted=[a-s.diff(chi,v) for a,v in zip(aa,xx)]
 if fault=='gauge-time':shifted[0]=0
 curvature=lambda a:[s.simplify(s.diff(a[j],xx[i])-s.diff(a[i],xx[j])) for i in range(4) for j in range(i+1,4)]
 put('gauge-curvature',curvature(aa)==curvature(shifted));put('nonflat-bounded',curvature(aa)[3]==3*s.cos(x))
 return ck
FAULTS=['injection','image-coordinate','right-inverse-order','mass-adjoint','nonreal-potential','principal-speed','gauge-time']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();good=checks();assert all(good.values()),good
 bad={f:[k for k,v in checks(f).items() if not v] for f in FAULTS};assert all(bad.values()),bad
 result=dict(result_id='K2123',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_checks=good,fault_failures=bad,scope='Actual K2028 stored image on same K2120 positive current. Universal domain and finite speed proofs are not inferred from finite checks.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS})
 if args.write:OUT.write_text(json.dumps(result,indent=2)+'\n')
 else:assert result==json.loads(OUT.read_text())
 print('PASS K2123',len(good),'exact checks;',len(bad),'genuine faults')
if __name__=='__main__':main()
