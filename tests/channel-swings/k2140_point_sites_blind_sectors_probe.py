from pathlib import Path
import json,argparse,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]

OUT='k2140-point-sites-blind-sectors.json'
DEPS=['explorations/conditional-build/k2133-recorded-instrument-vacuum-disturbance-2026-10-27.md','explorations/conditional-build/k2136-point-probe-recorded-field-2026-10-27.md','explorations/conditional-build/k2137-point-probe-energy-continuum-2026-10-27.md']
EVIDENCE='Exact finite fiber and record-matrix controls. Fock factorization, all-time complex cyclic density and lack of uniform inversion are written proofs, not numerical continuum claims. Sharp fair-record upper bound reused from K2133.'
FAULTS=['asymmetric_point_seed','coincident_sites','erase_record_coherence','omit_frame_cross_term']
def compute(fault=None):
 I=s.I;t=s.symbols('t',real=True);q=s.symbols('q',nonnegative=True);lam=s.symbols('lam',real=True)
 reflection=s.Matrix([[0,1],[1,0]]);omega=s.diag(2,2);seed=s.Matrix([1,1]);odd=s.Matrix([1,-1])
 if fault=='asymmetric_point_seed':seed=s.Matrix([1,2])
 phase=0 if fault=='coincident_sites' else t
 V=s.Matrix([[1,s.exp(-I*phase)],[1,s.exp(I*phase)]])/s.sqrt(2)
 gram=s.simplify(V.conjugate().T*V)
 if fault=='omit_frame_cross_term':gram=s.eye(2)
 plus=s.Matrix([[1,1],[1,1]])/2
 if fault=='erase_record_coherence':plus=s.eye(2)/2
 block=q*plus-s.diag(s.Rational(1,2),0)
 expected=(lam-1)**2-s.cos(t)**2
 checks={
 'free_reflection_reduces':omega*reflection==reflection*omega,
 'point_source_even':reflection*seed==seed,
 'odd_blind_overlap':(odd.T*seed)[0]==0,
 'two_site_determinant':s.simplify(V.det().expand(complex=True)-I*s.sin(t))==0,
 'frame_characteristic_polynomial':s.simplify(s.expand_trig((lam*s.eye(2)-gram).det()-expected))==0,
 'coincident_site_countercontrol':V.subs(t,0).rank()==1,
 'separated_fiber_control':V.subs(t,s.pi/2).rank()==2,
 'frame_resonance_has_zero_eigenvalue':gram.subs(t,s.pi).det()==0,
 'record_block_discriminant':s.simplify(s.trace(block)**2-4*block.det()-(q*q+s.Rational(1,4)))==0,
 'fair_record_distance':s.simplify(s.sqrt((q*q+s.Rational(1,4))).subs(q,s.Rational(1,2))-1/s.sqrt(2))==0,
 'convexity_of_record_norm':s.simplify(s.diff(s.sqrt(q*q+s.Rational(1,4)),q,2)-(s.Rational(1,4)/(q*q+s.Rational(1,4))**s.Rational(3,2)))==0,
 'no_uniform_inverse_sequence':s.limit(1-s.cos(t),t,0,dir='+')==0,
 }
 return {k:bool(v) for k,v in checks.items()}

def main():
 checks=compute();assert all(checks.values()),checks
 failures={}
 for fault in FAULTS:
  failed=[k for k,v in compute(fault).items() if not v]
  assert failed,('FAULT NOT DETECTED',fault)
  failures[fault]=failed
 report={'schema_version':'1.0','status':'conditional_exact_controls','exact_checks':checks,'fault_failures':failures,'universal_evidence':EVIDENCE,'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependency_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in DEPS}}
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();path=ROOT/'lab/process'/OUT
 if args.write:path.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(path.read_text())==report,'stored evidence differs; investigate before intentional refresh'
 print(json.dumps({'checks':len(checks),'faults':len(failures),'all_pass':all(checks.values()),'fault_failures':failures}))
if __name__=='__main__':main()
