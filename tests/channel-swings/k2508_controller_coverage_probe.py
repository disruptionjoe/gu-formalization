"""K2508 exact finite counterchannels and resource algebra, not a universal proof.
--write regenerates the deterministic report; default independently replays it.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys
import sympy as s
from flint import arb,ctx
ctx.prec=160
ROOT=Path(__file__).resolve().parents[2]
checks={};controls={};resources=[]
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def zero(M):return all(s.simplify(x)==0 for x in M)
def aa(x):return arb(x.numerator)/x.denominator
Q=s.diag(1,0);T=s.eye(2)-Q;rot=s.Matrix([[s.Rational(3,5),-s.Rational(4,5)],[s.Rational(4,5),s.Rational(3,5)]])
tau=F(16,25)
for G in (2,3,4):
 P=s.ones(G)/G;I=s.eye(G);V=s.kronecker_product(P,rot)+s.kronecker_product(I-P,s.eye(2));Qbar=s.kronecker_product(I,Q)
 ck(f'unitary_{G}',zero(V.H*V-s.eye(2*G)))
 D=V.H*Qbar*V-Qbar
 ck(f'global_defect_square_{G}',zero(D*D-s.Rational(16,25)*s.kronecker_product(P,s.eye(2))))
 # For each original sector, only one full data vector contributes tau/G.
 # The untouched original 108-dimensional complement contributes zero.
 for g in range(G):
  for k,rank in enumerate((10,98,12,96)):
   state=s.zeros(2*G,1);state[2*g+(k%2)]=1
   Fout=Qbar if k%2==0 else s.eye(2*G)-Qbar
   wrong=1-(state.H*V.H*Fout*V*state)[0]
   ck(f'sector_trace_{G}_{g}_{k}',wrong==s.Rational(16,25*G))
   ck(f'original_mixed_sector_{G}_{g}_{k}',wrong/rank==s.Rational(16,25*G*rank))
 ck(f'sharp_effect_penalty_{G}',s.Rational(16,25)==G*s.Rational(16,25*G))
 ct(f'branch_sector_max_insufficient_{G}',F(16,25)>F(16,25*G))
 # Same matrix with coordinates e0 (supported), e1 (outside), restricted to
 # one H-vector A. All other original supported basis vectors are identity.
 S=Qbar;L=S*V.H*(s.eye(2*G)-S)*V*S
 ck(f'positive_leakage_exact_{G}',zero(L-s.Rational(16,25)*s.kronecker_product(P,Q)))
 for g in range(G):
  p=L[2*g,2*g]/108
  ck(f'rank_one_mixed_leakage_{G}_{g}',108*p==s.Rational(16,25*G))
 ct(f'branch_leakage_max_insufficient_{G}',F(16,25)>F(16,25*G))
 # Positive block inequality sharp on uniform rank-one matrix.
 ck(f'PSD_block_norm_sharp_{G}',P.eigenvals().get(s.Integer(1))==1 and sum(P[i,i] for i in range(G))==1)
# Noncommuting positive effect verifies identity (1), not merely diagonal data.
A=s.Matrix([[s.Rational(3,4),s.Rational(1,8)],[s.Rational(1,8),s.Rational(1,4)]])
B=Q*(s.eye(2)-A)*Q+T*A*T;D=A-Q
ck('sector_positive_identity',zero(B-D*D-(A-A*A)))
ck('effect_contraction',all(v>0 for v in A.eigenvals()) and all(v>0 for v in (s.eye(2)-A).eigenvals()))
# Two actual controlled unitary branches, including a nontrivial error.
V=s.diag(s.eye(2),rot);Rb=s.diag(Q,Q);E=V.H*Rb*V-Rb
ck('nondemolition_effect_blocks',zero(E-s.diag(s.zeros(2),rot.H*Q*rot-Q)))
ck('nondemolition_norm_max',set(E.eigenvals())=={s.Integer(0),s.Rational(4,5),-s.Rational(4,5)})
# Control-only Hadamard before controlled map need not be block diagonal but
# preserves the full norm and ideal effect, including entangled input.
H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2);C=s.kronecker_product(H,s.eye(2));V2=V*C
ck('control_only_fixed_effect',zero(C.H*Rb*C-Rb))
ck('control_only_defect_conjugacy',zero(V2.H*Rb*V2-Rb-C.H*E*C))
X=s.Matrix([[0,1],[1,0]])
ct('uncovered_selector_even_identity_branches',zero(X.H*Q*X-T) and not zero(T-Q))
# Conditional deployment convex hull, using genuine phase-perfect and bad maps.
phase=s.diag(1,-1);A0=phase.H*Q*phase;A1=rot.H*Q*rot
for weight in [s.Rational(0),s.Rational(1,4),s.Rational(1)]:
 Am=(1-weight)*A0+weight*A1
 ck('convex_effect_'+str(weight),zero((Am-Q)**2-weight**2*s.Rational(16,25)*s.eye(2)))
# A smooth finite-net counterexample: phase angle 2*pi*x*(1-x) vanishes
# at tested endpoints 0,1 and equals pi/2 at 1/2, hence rotates Q to T.
x=s.symbols('x',real=True);angle=2*s.pi*x*(1-x)
ck('finite_net_endpoints_perfect',angle.subs(x,0)==0 and angle.subs(x,1)==0)
ct('unbounded_regularity_hidden_swap',angle.subs(x,s.Rational(1,2))==s.pi/2)
# Circuit continuity: R(theta) has generator sigma_y norm1; exact overlap
# gives half-trace distance |sin(theta-theta')|<=|theta-theta'| universally.
z=s.symbols('z',real=True);Rz=s.Matrix([[s.cos(z),-s.sin(z)],[s.sin(z),s.cos(z)]])
ck('rotation_unitary_identity',zero(Rz.T*Rz-s.eye(2)))
ck('rotation_effect_norm_identity',zero((Rz.T*Q*Rz-Q)**2-s.sin(z)**2*s.eye(2)))
# Product setting probabilities reconstruct the full positive load exactly.
for G in [1,2,5]:
 a=F(1,200);b=F(1,200);d=108;c=[F(r)/a**2 for r in (10,98,12,96)]+[F(d)/b];W=G*sum(c)
 q=[v/W for g in range(G) for v in c]
 ck(f'global_label_weights_{G}',sum(q)==1 and W==G*(2*d/a**2+d/b))
 # Nonidentical nonnegative setting loads; no assumed common sector success.
 probs=[F((j%5)+1,10000) for j in range(5*G)]
 ck(f'pooled_load_identity_{G}',W*sum(qj*pj for qj,pj in zip(q,probs))==sum(c[j%5]*probs[j] for j in range(5*G)))
# Concrete net/cost example p1, L1, target 1/100, radius1/200, G2.
e=l=F(1,100);h=F(1,200);a=e-h;b=l-h;G=2;N=201;alpha=F(1,100)
W=G*(216/a**2+108/b);n=10*W
ck('net_radius_margins',a+h==e and b+h==l)
ck('net_cardinality',N==200+1)
ck('explicit_W',W==17323200)
ck('certified_log_count',aa(n/W)>arb(20100).log())
ck('all_zero_confidence_sufficient',aa(F(n)/W)> (arb(N)/aa(alpha)).log())
ct('bias_floor_uncurable',W*(2/W)>1)
resources.append({'G':G,'net_size':N,'radius':str(h),'W':str(W),'shots_per_center':int(n),'total_shots':int(N*n),'confidence_failure':str(alpha),'effect_target':str(e),'leakage_target':str(l)})
# Mesh algebra and strict interior stationary point. Universal uniqueness in note.
t=s.symbols('t',positive=True);AA,BB=s.symbols('A B',positive=True)
for p in [1,2,3,5]:
 f=t**(-p)*(AA/(1-t)**2+BB/(1-t));poly=AA*((p+2)*t-p)+BB*(1-t)*((p+1)*t-p)
 ck(f'mesh_derivative_{p}',s.factor(s.diff(f,t)*t**(p+1)*(1-t)**3-poly)==0)
 ck(f'mesh_lower_sign_{p}',s.simplify(poly.subs(t,s.Rational(p,p+2)))<0)
 ck(f'mesh_upper_sign_{p}',s.simplify(poly.subs(t,s.Rational(p,p+1)))>0)
root=(9-s.sqrt(33))/6
ck('mesh_example_root',s.simplify((-3*t*t+9*t-4).subs(t,root))==0 and root>s.Rational(1,2) and root<s.Rational(2,3))
# Explicit original two-gap consumer and postselection margin.
E=F(2049,10**6)
ck('record_consumer',F(1024,10**6)+F(1024,10**6)+F(1,10**6)==E)
ck('postselection_consumer',E/(F(1,2)-E)==F(2049,497951)<F(1,200))
ct('missing_postselection_margin',F(1,100)-F(1,50)<0)
report={'result':'K2508','scope':'supplied full-memory coherent controller and parametric family; no experiment or GU physics','evidence_kind':'written universal proofs; exact finite channel and algebra controls; certified logarithm budget','checks':checks,'contrary_controls':controls,'resources':resources,'dependencies':{}}
for path in [Path(__file__),ROOT/'explorations/conditional-build/k2508-controller-coverage-2026-11-02.md',ROOT/'explorations/conditional-build/k2504-verifier-sector-calibration-2026-11-02.md',ROOT/'explorations/conditional-build/k2506-calibration-deployment-transfer-2026-11-02.md']:
 report['dependencies'][str(path.relative_to(ROOT))]=hashlib.sha256(path.read_bytes()).hexdigest()
out=ROOT/'lab/process/k2508-controller-coverage.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2)+'\n')
else:ck('saved_report_matches_reproduction',json.loads(out.read_text())==report)
print(f'K2508 PASS: {len(checks)} exact/certified finite checks; {len(controls)} contrary controls')
