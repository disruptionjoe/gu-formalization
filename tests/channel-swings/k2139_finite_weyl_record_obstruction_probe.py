from pathlib import Path
import json,argparse,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]

OUT='k2139-finite-weyl-record-obstruction.json'
DEPS=['explorations/conditional-build/k2136-point-probe-recorded-field-2026-10-27.md']
EVIDENCE='Exact symbolic Weyl-phase, Gram, Vandermonde, finite-difference and Gaussian-moment controls. Universal circuit separation and finite alphabet error proof are written and internally reviewed; no finite test proves all protocols.'
FAULTS=['merge_distinct_paths','drop_weyl_phase','erase_one_photon_correction','wrong_difference_normalization']
def compute(fault=None):
 I=s.I;a,b=s.symbols('a b',positive=True);t=s.symbols('t',real=True)
 atoms=[0,1,I]
 if fault=='merge_distinct_paths':atoms=[0,1,1]
 vand=s.Matrix([[x**j for x in atoms] for j in range(3)])
 # Noncollinear one-mode paths: D(-1)D(i) carries phase exp(i).
 def cocycle(x,y):
  return 0 if fault=='drop_weyl_phase' else (x*s.conjugate(y)-s.conjugate(x)*y)/2
 phase=s.exp(cocycle(-s.Integer(1),I))
 correction=0 if fault=='erase_one_photon_correction' else 4
 points=[-s.sqrt(a),s.sqrt(a)]
 def overlap(x,y,photon):
  delta=y-x;gaussian=s.exp(cocycle(-x,y))*s.exp(-s.conjugate(delta)*delta/2)
  return gaussian*(1-s.Rational(correction,4)*s.conjugate(delta)*delta) if photon else gaussian
 G0=s.Matrix([[overlap(x,y,False).subs(s.exp(-2*a),b) for y in points] for x in points])
 G1=s.Matrix([[overlap(x,y,True).subs(s.exp(-2*a),b) for y in points] for x in points])
 cp=s.Matrix([1,1]);cm=s.Matrix([1,-1]);ratio=lambda c:s.factor((c.T*G1*c)[0]/(c.T*G0*c)[0])
 q0=s.exp(-t*t/2);q1=(1-t*t)*q0
 moment=lambda f,n:s.simplify((-1)**n*s.diff(f,t,2*n).subs(t,0))
 x=s.symbols('x');norm=1 if fault=='wrong_difference_normalization' else 2
 checks={
 'distinct_coherent_vandermonde':s.simplify(vand.det())!=0,
 'noncollinear_weyl_phase':s.simplify(phase-s.exp(I))==0,
 'two_path_vacuum_gram':G0*cp==(1+b)*cp and G0*cm==(1-b)*cm,
 'one_photon_symmetric_ratio':s.simplify(ratio(cp)-(1-4*a*b/(1+b)))==0,
 'one_photon_antisymmetric_ratio':s.simplify(ratio(cm)-(1+4*a*b/(1-b)))==0,
 'generalized_eigenvectors':G1*cp==(1+(1-4*a)*b)*cp and G1*cm==(1-(1-4*a)*b)*cm,
 'weak_two_path_limit':s.limit((1+4*a/(s.exp(2*a)-1)),a,0)==3,
 'strict_R_less_three_reduction':s.simplify(3-(1+4*a/(s.exp(2*a)-1))-2*(s.exp(2*a)-1-2*a)/(s.exp(2*a)-1))==0,
 'probability_error_bound_algebra':s.simplify((1-1/(1+b))-b/(1+b))==0,
 'quadrature_one_photon_normalization':q1.subs(t,0)==1 and moment(q1,1)==3,
 'finite_difference_cancellation':all(s.expand(sum((-1)**(n-j)*s.binomial(n,j)*x**j for j in range(n+1))-(x-1)**n)==0 for n in range(1,7)),
 'contraction_normalization':all(s.Rational(2,norm)**(2*n)==1 for n in range(1,7)),
 'vacuum_even_moments':all(moment(q0,n)==s.factorial2(2*n-1) for n in range(1,7)),
 'one_photon_moment_ratios':all(moment(q1,n)==(2*n+1)*moment(q0,n) for n in range(1,7)),
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
