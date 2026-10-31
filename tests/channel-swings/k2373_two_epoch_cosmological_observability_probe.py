"""Exact identities and stored-transfer consumer; --write saves the reproducible report."""
from pathlib import Path
import json, sys
import hashlib
import sympy as S
import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]
checks = {}; controls = {}
def check(name, value):
    checks[name] = bool(value)
    if not value: raise AssertionError(name)
def reject(name, value):
    controls[name] = bool(value)
    if not value: raise AssertionError('undetected ' + name)

# Exact block determinant, local response, and an independently explicit example.
b, d, h = S.symbols('b d h', nonzero=True, real=True)
t00,t01,t02,t03,t10,t11,t12,t13 = S.symbols('t00 t01 t02 t03 t10 t11 t12 t13')
B = S.Matrix([[2,0,0,0],[0,2*b,0,0],
              [2*t00,2*t01,2*t02,2*t03],
              [2*b*t10,2*b*t11,2*b*t12,2*b*t13]])
check('exact_two_epoch_determinant', S.expand(B.det()-16*b*b*(t02*t13-t03*t12)) == 0)
A = S.Matrix([[0,-d/2],[1,0]])
check('exact_local_leading_coefficient', S.expand(16*b*b*(h*A).det()-8*b*b*d*h*h)==0)
# This rational transfer is an algebraic positive control, not the fitted history.
T = S.Matrix([[1,0,0,-1],[0,1,1,0],[0,0,1,0],[0,0,0,1]])
P = S.Matrix([[2,0,0,0],[0,-1,0,0]])  # b=-1/2
Bt = P.col_join(P*T)
r = S.Matrix([[-S.Rational(9,2),-6,-S.Rational(1,2),9]])
g = r*T*Bt.inv()
W = S.eye(4).col_join(g)
n = (-g).row_join(S.ones(1,1))
check('exact_rational_two_epoch_reconstruction', g*Bt == r*T)
check('exact_joint_null', n*W == S.zeros(1,4))
Cov = W*W.T
check('exact_shared_seed_covariance_null', n*Cov == S.zeros(1,5))
check('exact_rank_four_example', Cov.rank()==4)
N=S.diag(1,2,3,4,5)
data=S.Matrix([1,2,3,4,5])
noisevar=(n*N*n.T)[0]
projection=data-N*n.T*(n*data)[0]/noisevar
check('exact_noise_weighted_projection_constraint',(n*projection)[0]==0)
check('exact_noise_weighted_projection_cost',
      S.simplify(((data-projection).T*N.inv()*(data-projection))[0]-(n*data)[0]**2/noisevar)==0)
check('exact_noise_subtracted_null_variance',(n*(Cov+N)*n.T)[0]==noisevar)
# Same null tester, with actually changed covariance/readout/transfer input.
mut = Cov.copy(); mut[4,4] += 1
reject('independent_density_variance', (n*mut*n.T)[0] == 1)
mut = Cov.copy()
for i in range(4): mut[i,4] = mut[4,i] = 0
reject('separately_fitted_marginals_discard_cross_epoch_covariance', (n*mut*n.T)[0] != 0)
wrongg = g.copy(); wrongg[0] += 1
wrongW = S.eye(4).col_join(wrongg)
reject('changed_density_relation', n*(wrongW*wrongW.T) != S.zeros(1,5))
reject('coincident_epochs_not_identifiable', P.col_join(P*S.eye(4)).det()==0)
# Exact sharp singular-covariance escape: differing models agree on unexcited direction.
Asing = S.diag(0,1,1,1)
check('exact_singular_covariance_escape', W*Asing*W.T == wrongW*Asing*wrongW.T)
reject('positive_definite_covariance_closes_escape', W*W.T != wrongW*wrongW.T)
check('exact_wrong_model_noise_excess',
      (n*(wrongW*wrongW.T+N)*n.T)[0]-noisevar == 1)

# Actual fixed K2367 endpoint consumer, high precision finite matrix arithmetic.
mp.mp.dps = 75
source = ROOT/'lab/process/k2367-sourced-fit-dust-transfer.json'
j = json.loads(source.read_text())
def f(x): return mp.mpf(str(x))
bb = -1/mp.sqrt(6)
P = mp.matrix([[2,0,0,0],[0,2*bb,0,0]])
aa,HH,uu,dd,V,Vp,*_ = map(f,j['details']['background_today'])
rows=[]
for z in j['details']['transfers']:
    k=f(z['k_over_Hstar']); q=k*k/(aa*aa)
    TT=mp.matrix([[f(x) for x in row] for row in z['transfer']])
    PP=P*TT
    B=mp.matrix([[P[i,j] if i<2 else PP[i-2,j] for j in range(4)] for i in range(4)])
    detqp=TT[0,2]*TT[1,3]-TT[0,3]*TT[1,2]
    key=str(z['k_rd'])
    check('actual_endpoint_nonzero_block_'+key, abs(detqp)>mp.mpf('1e-20'))
    check('actual_block_determinant_'+key, abs(mp.det(B)/(16*bb*bb*detqp)-1)<mp.mpf('1e-65'))
    rr=mp.matrix([[-(2*q-uu*uu)/dd,-(3*HH*uu+Vp+4*bb*dd)/dd,-uu/dd,3*HH]])
    gg=rr*TT*(B**-1)
    check('actual_all_seed_relation_'+key, max(abs(x) for x in gg*B-rr*TT)<mp.mpf('1e-60'))
    seederrs=[]
    for seed in z['seeds']:
        xi=mp.matrix([f(x) for x in seed['initial']])
        yi=P*xi
        dj,lf,zf=map(f,seed['today_density_lensing_slip'])
        four=mp.matrix([yi[0],yi[1],lf,zf])
        prediction=(gg*four)[0]
        err=abs(prediction-dj)/max(1,abs(dj))
        check('actual_stored_seed_readout_'+key+'_'+seed['label'],err<mp.mpf('1e-7'))
        seederrs.append(float(err))
    # A changed slip-matter coefficient must fail against same stored seed outputs.
    rrwrong=rr.copy(); rrwrong[0,1] += 4*bb
    gw=rrwrong*TT*(B**-1)
    wrongerrs=[]
    for seed in z['seeds']:
        xi=mp.matrix([f(x) for x in seed['initial']]); yi=P*xi
        dj,lf,zf=map(f,seed['today_density_lensing_slip'])
        wrongerrs.append(abs((gw*mp.matrix([yi[0],yi[1],lf,zf]))[0]-dj))
    reject('omit_Jordan_slip_matter_term_'+key,max(wrongerrs)>mp.mpf('1e-6'))
    def infnorm(mat):
        return max(sum(abs(mat[i,j]) for j in range(mat.cols)) for i in range(mat.rows))
    scaled=B.copy()
    for i in range(4):
        rowscale=max(abs(B[i,j]) for j in range(4))
        for j in range(4):scaled[i,j]/=rowscale
    rows.append(dict(k_rd=z['k_rd'],potential_momentum_block_determinant=float(detqp),
        endpoint_determinant=float(mp.det(B)),density_coefficients=[float(x) for x in gg],
        endpoint_infinity_condition_number=float(infnorm(B)*infnorm(B**-1)),
        row_scaled_endpoint_infinity_condition_number=float(infnorm(scaled)*infnorm(scaled**-1)),
        stored_seed_relative_errors=seederrs,
        wrong_density_max_absolute_error=float(max(wrongerrs))))
st='k2373-two-epoch-cosmological-observability'
deps=['lab/process/k2367-sourced-fit-dust-transfer.json','explorations/conditional-build/k2370-potential-jet-density-identity-2026-10-31.md',f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(ROOT))]
out=dict(result_id='K2373',checks=len(checks),check_names=list(checks),changed_input_controls=controls,actual_rows=rows,scope='Written theorem exact; finite matrix consumer inherits K2367 ODE errors. No observation, likelihood, interval or native GU certificate.',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps})
p=ROOT/f'lab/process/{st}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print('PASS',out['checks'],len(controls))
