"""Full complex Choi rigidity from the inherited global primal/dual gap."""
from pathlib import Path
import json,sys,hashlib
R=Path(__file__).resolve().parents[2]
p=R/'tests/channel-swings/k2424_recovery_saddle_reduction_probe.py';src=p.read_text()
# Replay exact original instrument and interval certificate; no report mutation.
exec(compile(src[:src.index("report={'result_id'")],str(p),'exec'),globals())
inherited_checks=dict(checks);inherited_controls=dict(controls);checks={};controls={}
from flint import acb,acb_mat
one=acb(1);ii=acb(0,1)
def mat(rows):return acb_mat(rows)
def eye(n):return mat([[int(i==j) for j in range(n)] for i in range(n)])
def tr(A):return sum(A[j,j] for j in range(A.nrows()))
def kron(A,B):return mat([[A[i//B.nrows(),j//B.ncols()]*B[i%B.nrows(),j%B.ncols()] for j in range(A.ncols()*B.ncols())] for i in range(A.nrows()*B.nrows())])
def scaleM(A,c):return mat([[A[i,j]*c for j in range(A.ncols())] for i in range(A.nrows())])
def transpose(A):return mat([[A[j,i] for j in range(A.nrows())] for i in range(A.ncols())])
def submat(A,ids):return mat([[A[i,j] for j in ids] for i in ids])
I2=eye(2);I4=eye(4);px=mat([[0,1],[1,0]]);py=mat([[0,-ii],[ii,0]]);pz=mat([[1,0],[0,-1]]);pa=[px,pz]
# Original output-first unnormalized Choi, including Y tensor Y^T.
J=scaleM(I4+kron(scaleM(px,tv[0])+scaleM(pz,tv[1]),I2)+sum((scaleM(kron(pa[a],transpose(pa[b])),AA0[a][b]) for a in range(2) for b in range(2)),mat([[0]*4 for _ in range(4)]))+scaleM(kron(py,transpose(py)),d0),acb(1)/2)
H=scaleM(kron(scaleM(px,V[0])+scaleM(pz,V[1]),I2)+sum((scaleM(kron(pa[a],transpose(pa[b])),N[a][b]) for a in range(2) for b in range(2)),mat([[0]*4 for _ in range(4)])),acb(1)/2)
zv=[a+b for a,b in zip(mv(trans(AA0),V),mv(trans(N),tv))]
Zd=scaleM(scaleM(I2,phi0)+scaleM(px,zv[0])+scaleM(pz,zv[1]),acb(1)/2);D=kron(I2,Zd)-H
ck('original_complementarity_interval_consistent',all((D*J)[i,j].contains(0) for i in range(4) for j in range(4)))
ck('nonzero_translation_and_strict_canonical_branch',dot(tv,tv)>0 and d0>0 and d0<1)
pJ=((tr(J)*tr(J)-tr(J*J))/2).real;pD=((tr(D)*tr(D)-tr(D*D))/2).real
ck('both_positive_rank_two_products',pJ>0 and pD>0)
# Exact rank two follows from physical canonical form, PSD complementarity,
# and these positive products. Interval zero alone is never the rank proof.
P=scaleM(scaleM(J,tr(J))-J*J,1/pJ)
ck('projector_interval_consistent',all((P*P-P)[i,j].contains(0) for i in range(4) for j in range(4)))
fs=[scaleM(f,1/arb(2).sqrt()) for f in [I2,px,py,pz]]
G=mat([[tr(kron(I2,a)*P*kron(I2,b)*P) for b in fs] for a in fs])
ck('complex_Hermitian_TP_Gram_positive',all(submat(G,list(range(k))).det().real>0 for k in range(1,5)))
mu2=(27*G.det()/(tr(G)**3)).real;gamma=(pD/tr(D)).real
ck('positive_conditioning_bounds',mu2>0 and gamma>0)
epsilon=ar(upper-lower);r=norm(sv);hgood=dot([1-w for w in ww],rr)
# Raw support coefficients divide by RR in the normalized minimax dual.
eta=4*RR*epsilon/gamma;bad_reduced=(1+arb(2).sqrt()/mu2.sqrt())*(8*RR*epsilon/gamma).sqrt();bad_original=(1+arb(2).sqrt()/mu2.sqrt())*(16*RR*epsilon/gamma).sqrt()
# Use 2r as gap only after proving it is the smaller Bell eigenvalue.
ck('good_gap_branch',hgood>=r and r>0)
gammag=2*r;etag=4*RR*epsilon/gammag;good_original=(2*etag).sqrt()+etag/2
ck('full_bad_original_bound_below_1e_minus10',bad_original<arb('1e-10'))
ck('full_good_original_bound_below_1e_minus12',good_original<arb('1e-12'))
# Exact fixture independently verifies all four Hermitian support directions.
v,M,t,A,y,phi=fixtures[0][1:];Jf=choi(lambda op:channel(t,A,y,op));Hf=support_matrix(v,M);zvf=A.T*v+M.T*t;Df=simp(s.kronecker_product(I,(phi*I+zvf[0]*X+zvf[1]*Z)/2)-Hf)
pf=s.simplify((s.trace(Jf)**2-s.trace(Jf*Jf))/2);Pf=simp((s.trace(Jf)*Jf-Jf*Jf)/pf)
Gf=s.Matrix([[s.simplify(s.trace(s.kronecker_product(I,a)*Pf*s.kronecker_product(I,b)*Pf)/2) for b in [I,X,Y,Z]] for a in [I,X,Y,Z]])
ck('exact_complex_Gram_positive',all(Gf[:k,:k].det()>0 for k in range(1,5)))
ck('exact_support_projector',simp(Pf*Pf-Pf)==s.zeros(4) and simp(Df*Pf)==s.zeros(4))
Pbad=s.diag(1,0,0,1);Gb=s.Matrix([[s.simplify(s.trace(s.kronecker_product(I,a)*Pbad*s.kronecker_product(I,b)*Pbad)/2) for b in [I,X,Y,Z]] for a in [I,X,Y,Z]])
Jother=Pbad.copy();Jother[0,3]=Jother[3,0]=Q(1,2)
ctrl('leakage_alone_not_rigidity',Gb.det()==0 and psd(Jother) and ptr(Jother)==I and Jother!=Pbad and Pbad*Jother*Pbad==Jother)
ctrl('imaginary_direction_is_actually_checked',Gf[2,2]>0 and len(fs)==4)
ctrl('original_sign_factor_two_required',bad_original>bad_reduced)
# Exact good-channel exposing functional, before channel replacement.
rg,hg=s.symbols('rg hg',real=True)
Hg=(rg*s.kronecker_product(X,X.T)+hg*s.kronecker_product(Y,Y.T)+rg*s.kronecker_product(Z,Z.T))/2
Dg=(2*rg+hg)*s.eye(4)/2-Hg
Bell=s.Matrix([[1,0,0,1],[0,1,1,0],[0,1,-1,0],[1,0,0,-1]])/s.sqrt(2)
ck('original_good_Bell_gap',s.simplify(Bell.T*Dg*Bell-s.diag(0,rg+hg,2*rg,rg+hg))==s.zeros(4))
# Identity on the whole Hermitian basis; trace need only equal2, not TP.
herm=[]
for a in range(4):
 Ht=s.zeros(4);Ht[a,a]=1;herm.append(Ht)
for a,b in combinations(range(4),2):
 Ht=s.zeros(4);Ht[a,b]=Ht[b,a]=1;herm.append(Ht)
 Ht=s.zeros(4);Ht[a,b]=s.I;Ht[b,a]=-s.I;herm.append(Ht)
ck('original_good_functional_all_Hermitian_directions',all(s.simplify(s.trace(Dg*Ht)-(hg+2*rg)*s.trace(Ht)/2+hg*s.trace(s.kronecker_product(Y,Y.T)*Ht)/2+rg*s.trace((s.kronecker_product(X,X.T)+s.kronecker_product(Z,Z.T))*Ht)/2)==0 for Ht in herm))

# Universal canonical support Gram: polynomial reduction, not fixture extrapolation.
ca,da,ta=s.symbols('ca da ta', real=True)
relation=(1-ca**2)*(1-da**2)
def red(x):
 num,den=s.fraction(s.cancel(x));return s.factor(s.rem(num,s.Poly(ta**2-relation,ta).as_expr(),ta)/den)
Jc=choi(lambda op:channel(s.Matrix([0,ta]),s.diag(ca,ca*da),da,op))
pc=1-ca**2*da**2;Pc=(2*Jc-Jc*Jc)/pc;Pc=Pc.applyfunc(red)
Gc=s.Matrix([[red(s.trace(s.kronecker_product(I,a)*Pc*s.kronecker_product(I,b)*Pc)/2) for b in [I,X,Y,Z]] for a in [I,X,Y,Z]])
ck('universal_canonical_Gram_trace',red(s.trace(Gc)-2-2*relation/pc**2)==0)
ck('universal_canonical_Gram_determinant',red(Gc.det()-relation**2/pc**4)==0)
# Strict canonical t>0 guarantees injectivity; t=0 does not.
ck('exact_fixture_canonical_determinant',Gf.det()>0)

# Scalar budget/regret and distance laws, including a finite useful consumer.
extra=arb('1e-8');budget=epsilon+2*extra
perturbed_bad=(1+arb(2).sqrt()/mu2.sqrt())*(16*RR*budget/gamma).sqrt()
ck('nonzero_uncertainty_consumer',perturbed_bad<arb('0.1'))
report={'result_id':'K2426','checks':checks,'controls':controls,'inherited_checks':inherited_checks,'inherited_controls':inherited_controls,'certificate':{'TP_Gram_det':str(G.det().real),'TP_mu_squared_lower':str(mu2),'raw_slack_gap_lower':str(gamma),'normalization_R':str(RR),'bad_reduced_half_diamond_bound':str(bad_reduced),'bad_original_each_aligned_sign_half_diamond_bound':str(bad_original),'good_original_half_diamond_bound':str(good_original),'uncertainty_1e_minus8_bad_bound':str(perturbed_bad),'exact_fixture_Gram':[[str(v) for v in row] for row in Gf.tolist()]},'scope':'All globally optimal or sufficiently near-optimal nominal controllers lie near one certified original full complex Choi channel. Exact optimizer uniqueness only under an exact dual support condition; no uniqueness from nonzero gap, no Kraus uniqueness, and no native apparatus or GU claim.'}
report['dependencies']={q:hashlib.sha256((R/q).read_bytes()).hexdigest() for q in ['tests/channel-swings/k2424_recovery_saddle_reduction_probe.py','tests/channel-swings/k2419_positive_visibility_dual_probe.py','explorations/conditional-build/k2422-joint-recovery-optimality-2026-10-31.md','lab/process/k2424-recovery-saddle-reduction.json']}
report['software']={'sympy':s.__version__,'python_flint':__import__('flint').__version__,'arb_bits':ctx.prec};out=R/'lab/process/k2426-recovery-rigidity.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:assert json.loads(out.read_text())==report
print(json.dumps({'checks':len(checks),'controls':len(controls),'certificate':report['certificate']}))
