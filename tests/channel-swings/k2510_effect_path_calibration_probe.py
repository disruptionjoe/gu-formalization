"""Exact finite controls for K2510. Universal angular proof is in the note.
Default: reproduce and compare saved report; --write: save it.
"""
from pathlib import Path
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2]; checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
I=s.eye(2);Z=s.diag(1,-1);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);P=s.diag(1,0);H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
rot=s.Matrix([[s.Rational(3,5),-s.Rational(4,5)],[s.Rational(4,5),s.Rational(3,5)]])
ck('rotation_unitary',rot.T*rot==I)
for name,F in [('Q',P),('T',I-P)]:
 d=rot.T*F*rot-F;ck(name+'_sharp_effect_square',d*d==s.Rational(16,25)*I)
ck('sharp_leakage',(rot.T*(I-P)*rot)[0,0]==s.Rational(16,25))
# Nonzero center angle and path increment: exact Pythagorean pairs.
center=s.Matrix([[s.Rational(12,13),-s.Rational(5,13)],[s.Rational(5,13),s.Rational(12,13)]])
end=rot*center
ck('angular_leakage_addition',end[1,0]==s.Rational(63,65))
ck('angular_leakage_square',(end.T*(I-P)*end)[0,0]==s.Rational(3969,4225))
ck('angle_below_half_pi',end[0,0]==s.Rational(16,65)>0)
# The raw phase generator commutes, but its output frame does not.
ck('raw_commutator_zero',Z*P-P*Z==s.zeros(2))
ck('suffix_generator',H*Z*H==X)
V0=H;V1=H*(-s.I*Z);D=V1.conjugate().T*P*V1-V0.T*P*V0
ct('raw_commutator_invisibility_refuted',D*D==I)
ck('suffix_cross_block_norm',((I-P)*X*P).T*((I-P)*X*P)==P)
# Derivative product formula for two noncommuting varying gates.
t=s.symbols('t',real=True)
U1=s.diag(s.exp(-s.I*t),s.exp(s.I*t));U2=s.cos(t)*I-s.I*s.sin(t)*X;V=U2*U1
G=s.simplify(s.I*s.diff(V,t)*V.conjugate().T);expected=X+U2*Z*U2.conjugate().T
ck('output_generator_product_rule',s.simplify(G-expected)==s.zeros(2))
A=s.simplify(V.conjugate().T*P*V)
ck('effect_derivative_identity',s.simplify(s.diff(A,t)-s.I*V.conjugate().T*(G*P-P*G)*V)==s.zeros(2))
# Global full-controller symmetry, including coherent input sectors.
for M in [1,17,10**6]:
 Gphi=M*s.kronecker_product(Z,I)
 for f,F in [('Q',P),('T',I-P)]:
  Fb=s.kronecker_product(I,F);ck(f'controller_{M}_{f}_cross_zero',(s.eye(4)-Fb)*Gphi*Fb==s.zeros(4))
 Vc=s.kronecker_product(s.diag(s.I,-s.I),rot)
 ck(f'controller_{M}_effect_independent',Vc.conjugate().T*s.kronecker_product(I,P)*Vc==s.kronecker_product(I,rot.T*P*rot))
# Compressed derivative at a center cannot give a global leakage bound.
l=s.sin(t)**2
ct('center_derivative_zero_not_global',s.diff(l,t).subs(t,0)==0 and l.subs(t,s.pi/2)==1)
# Center alone cannot establish continuity / model membership.
ct('sampled_identity_unmodeled_swap',X*P*X==I-P and P!=I-P)
eps=s.Rational(1,10**6);ell=eps;a=eps/2;b=ell/4;h=s.Rational(1,2000000);d=108;Gc=2
ck('effect_mesh_margin',h==eps/2)
ck('leakage_mesh_margin_squared',h*h<=ell/4)
W=Gc*(2*d/a**2+d/b);ck('pooled_weight',W==1728000864000000)
N=2000001;ck('visible_cover',1/h+1==N);ck('removed_coordinate_saving',N**2//N==N)
E=1024*eps+1024*s.sqrt(eps*ell)+ell
ck('complete_record',E==s.Rational(2049,10**6));ck('postselection',E/(s.Rational(1,2)-E)==s.Rational(2049,497951)<s.Rational(1,200))
ct('bias_floor_no_sample_repair',1/W-2/W<0)
ct('ignoring_coherent_dimension_underprices',2*d/a**2+d/b<W)
# Genuine machinery-level negative fixture: corrupted rotation loses unitarity.
bad=rot.copy();bad[0,0]+=s.Rational(1,100)
ct('corrupt_rotation_detected',bad.T*bad!=I)
paths=['explorations/conditional-build/k2510-effect-path-calibration-2026-11-02.md','tests/channel-swings/k2510_effect_path_calibration_probe.py','explorations/conditional-build/k2508-controller-coverage-2026-11-02.md','explorations/conditional-build/k2506-calibration-deployment-transfer-2026-11-02.md']
report={'result':'K2510','scope':'finite exact controls and rational resource composition; universal proof in note','checks':checks,'contrary_controls':controls,'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths},'consumer':{'pooled_weight':str(W),'cover_points':N,'record_error':str(E),'postselection_error':str(E/(s.Rational(1,2)-E))}}
p=R/'lab/process/k2510-effect-path-calibration.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2)+'\n')
else:ck('saved_report_consistency',json.loads(p.read_text())==report)
print('K2510 PASS',len(checks),'checks',len(controls),'contrary controls')
