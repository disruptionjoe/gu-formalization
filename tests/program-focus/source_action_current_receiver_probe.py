"""Actual same-injection current receivers; sole serialized native job.

Exact native sparse algebra with hash-bound inherited inverse certificates.
No claim of a physical propagated ghost.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt
import sys,json,hashlib,time,argparse

parser=argparse.ArgumentParser()
parser.add_argument('root',nargs='?',type=Path,default=Path(__file__).resolve().parents[2])
parser.add_argument('--output',type=Path,default=None)
args=parser.parse_args()
ROOT=args.root
sys.path.insert(0,str(ROOT/'tests/program-focus'))
import source_action_deep_geometry as geo
from source_action_deep_algebra import add,scale
from source_action_physical_probe import mul,gamma,components
from source_action_slice_completion_probe import covector,inject,inverse,readout
from source_action_reduced_evolution_probe import build_context

def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
print('build_context start',flush=True)
t0=time.time();ctx=build_context(ROOT)
C,E,h,N6=ctx['C'],ctx['E'],ctx['h'],ctx['N6']
print('build_context finished',round(time.time()-t0,2),flush=True)
old=json.loads((ROOT/'lab/process/source-action-kappa1-constraints.json').read_text())
new=json.loads((ROOT/'lab/process/source-action-reduced-evolution.json').read_text())
assert ctx['highest6_in_weight6']==old['exact_probe']['spin6']['highest6_in_weight6']
assert ctx['time_kernel_in_highest6']==old['exact_probe']['spin6']['time_kernel_in_highest6']
assert digest([[C(E.pair(h.conj(u),v)).ser()for v in N6]for u in N6])==old['exact_probe']['spin6']['constraint_inverse']['gram_sha256']
assert digest([[C(x).ser()for x in row]for row in ctx['G7']])==old['exact_probe']['spin7']['kernel_gram_sha256']
p6=old['spin6_inverse_candidates'];p7=new['spin7_inverse_candidates']
for ri in range(2):
 for w,p in zip(p6[ri]['blocks'],old['exact_probe']['spin6']['constraint_inverse']['root_certificates'][ri]['blocks']):
  assert digest(w['rational_inverse'])==p['rational_inverse_sha256']
  assert w['neumann_bound']==p['neumann_bound'] and Q(w['neumann_bound'])<1
 p=old['exact_probe']['spin7']['root_certificates'][ri]
 assert digest(p7[ri]['inverse'])==p['inverse_sha256']
 assert p7[ri]['neumann_bound']==p['neumann_bound'] and Q(p7[ri]['neumann_bound'])<1

tau=covector(3);xi=covector(0)
N7=[h.add(h.rot(0,2,n),h.scale(-h.I,h.rot(1,2,n)))for n in h.N]
def znorm(z):z=C(z);return abs(z.a)+abs(z.b)

def vertex(w,field,se=-Q(1,2)):
 a=components(w);z,nu=field
 r=[add(*(scale(1/geo.d[b],mul(gamma(b),add(mul(a[b],z[j]),scale(-1,mul(a[j],z[b])))))for b in range(14)),mul(a[j],nu))for j in range(14)]
 s=add(*(scale(1/geo.d[j],mul(a[j],z[j]))for j in range(14)),*(scale(se/geo.d[j],mul(gamma(j),mul(a[j],nu)))for j in range(14)))
 return r,s

def receiver(w):
 cols=[readout(inverse(tau,vertex(w,inject(j))))for j in range(5)]
 return [[cols[j][i]for j in range(5)]for i in range(5)]

def bflat(B):return {(i,j,c):C(x)for i,row in enumerate(B)for j,v in enumerate(row)for c,x in v.items()if x}
def reim(B,part):return {k:Q(getattr(C(z),part))for k,z in B.items()if getattr(C(z),part)}
def adj_sign(c):
 s=(-1)**(c.bit_count()*(c.bit_count()-1)//2)
 for a in range(14):
  if c>>a&1 and geo.d[a]<0:s=-s
 return s
def hsweight(c):
 w=Q(1)
 for a in range(14):
  if c>>a&1:w*=abs(geo.d[a])
 return w
def adj(B):return {(j,i,c):C(v).conj()*adj_sign(c)for(i,j,c),v in B.items()}
def plus(A,B):return {k:C(A.get(k,0))+C(B.get(k,0))for k in A.keys()|B.keys()if C(A.get(k,0))+C(B.get(k,0))}
def herm(B):return {k:v/2 for k,v in plus(B,adj(B)).items()}
def hs2(B):return sum(hsweight(c)*(C(z).a**2+C(z).b**2)for(i,j,c),z in B.items())
def sqrt_bounds(q):
 q=Q(q);scale10=10**18
 n=isqrt(q.numerator*scale10**2//q.denominator)
 lo=Q(n,scale10);hi=lo if lo*lo==q else Q(n+1,scale10)
 return lo,hi
def report(B,err):
 H=herm(B);b2=hs2(B);h2=hs2(H);e2=sum(hsweight(c)*v*v for(i,j,c),v in err.items())
 blo,bhi=sqrt_bounds(b2);hlo,hhi=sqrt_bounds(h2);elo,ehi=sqrt_bounds(e2)
 robust=bool(b2) and 2*hlo>bhi+3*ehi
 sample=next(iter(H.items()),None)
 certified=[(k,z,err.get(k,Q(0)))for k,z in B.items()if abs(C(z).a)>err.get(k,Q(0))]
 best=max(certified,key=lambda row:abs(C(row[1]).a)-row[2])if certified else None
 return {'nonzero_terms':len(B),'hermitian_terms':len(H),'B_HS2':str(b2),'Herm_HS2':str(h2),
  'Herm_ratio':float(h2/b2)if b2 else None,'rootball_error_HS2':str(e2),
  'rootball_error_HS_upper':str(ehi),'coarse_norm_gram_robust_certified':robust,
  'robust_margin_lower':str(2*hlo-bhi-3*ehi),
  'certified_nonzero_coefficients':len(certified),
  'strongest_nonzero_coefficient':{'key':best[0],'value':C(best[1]).ser(),'error_bound':str(best[2]),'strict_margin':str(abs(C(best[1]).a)-best[2])}if best else None,
  'one_Herm_coefficient':{'key':sample[0],'value':C(sample[1]).ser(),'error_bound':str((err.get(sample[0],0)+err.get((sample[0][1],sample[0][0],sample[0][2]),0))/2)}if sample else None}

# Full four-arrow/current identity control on the same actual dt convention.
central={(1<<3,0):Q(1)}
assert bflat(receiver(central))=={(j,j,0):C(1)for j in range(5)}
central_bad=[readout(inverse(tau,vertex(central,inject(j),0)))for j in range(5)]
assert central_bad != [readout(inverse(tau,vertex(central,inject(j))))for j in range(5)]
for j in range(5):
 expected=[{}for _ in range(5)];expected[j]={0:Q(1)}
 assert readout(inject(j))==expected
print('building receiver basis',flush=True)
Bs=[bflat(receiver(n))for n in N6+N7]
print('receiver basis finished',round(time.time()-t0,2),flush=True)
realBs=[reim(B,p)for B in Bs for p in ['a','b']]
realBs=[B for B in realBs if B]
def trace_product(A,B):
 return sum(x*B.get((j,i,c),Q(0))*geo.cliff_mul(c,c)[1]for(i,j,c),x in A.items())
bad=[];tested=0
for i,A in enumerate(realBs):
 for j in range(i,len(realBs)):
  tested+=1;q=trace_product(A,realBs[j])
  if q:bad.append({'i':i,'j':j,'value':str(q)})
structural={'real_receiver_vectors':len(realBs),'polarized_trace_pairs_tested':tested,'all_trace_products_zero':not bad,'counterexamples_first5':bad[:5]}
print('structural trace finished',structural,round(time.time()-t0,2),flush=True)
out={'controls':{'same_horizontal_injection':True,'full_four_arrows':True,'central_B_equals_identity':True,'SE_omission_rejected':True,'inverse_hashes_verified':True},'roots':[]}
out['structural_Herm_half_identity']=structural
for ri,index in [(0,12),(1,5)]:
 v=h.symbols(E,tau,h.bs[index])[0];force=h.symbols(E,xi,v)[0]
 assert h.rot(0,1,force)==h.scale(6*h.I,force)
 b6=[C(E.pair(h.conj(n),force))for n in N6]
 b7=[C(E.pair(h.conj(n),force))for n in N7]
 c6=[C()for _ in N6];e6=[Q(0)for _ in N6]
 for block in p6[ri]['blocks']:
  ids=block['indices'];R=[[C(*z)for z in row]for row in block['rational_inverse']]
  c0=[-sum((a*b6[j]for a,j in zip(row,ids)),C())for row in R]
  eta=Q(block['neumann_bound']);er=eta/(1-eta)*max(map(znorm,c0))
  for i,z in zip(ids,c0):c6[i]=z;e6[i]=er
 R7=[[C(*z)/14 for z in row]for row in p7[ri]['inverse']]
 c7=[-sum((a*b for a,b in zip(row,b7)),C())for row in R7]
 eta=Q(p7[ri]['neumann_bound']);e7=eta/(1-eta)*max(map(znorm,c7))
 coeff=c6+c7;errors=e6+[e7]*len(c7)
 energy=sum((b.conj()*c for b,c in zip(b6+b7,coeff)),C())
 energyerr=sum(znorm(b)*er for b,er in zip(b6+b7,errors))+abs(energy.b)
 assert energy.a+energyerr<0
 B={};err={}
 for a,e,basis in zip(coeff,errors,Bs):
  for k,z in basis.items():
   B[k]=B.get(k,C())+a*z
   err[k]=err.get(k,Q(0))+e*znorm(z)
 B={k:z for k,z in B.items()if z};err={k:z for k,z in err.items()if z}
 n=h.add(*(h.scale(a,b)for a,b in zip(coeff,N6+N7)if a))
 assert h.rot(0,1,n)==h.scale(6*h.I,n)
 # Check linear coefficient assembly against direct complete field receiver.
 assert B==bflat(receiver(n))
 # Pure nonzero rotation weight gives zero bilinear self-pair and equal real parts.
 assert E.pair(n,n)==0
 assert E.pair(force,n)==0
 Bv=bflat(receiver(v))
 out['roots'].append({'root_index':ri,'range_basis_index':index,'energy_center':str(energy.a),'energy_error_bound':str(energyerr),
  'normal_response_weight':6,'normal_pair_self_zero':True,'force_response_bilinear_zero':True,
  'each_real_component_energy_center':str(energy.a/2),'each_real_component_energy_error_bound':str(energyerr/2),
  'normal_real':report(reim(B,'a'),err),'normal_imag':report(reim(B,'b'),err),
  'range_real':report(reim(Bv,'a'),{}),'range_imag':report(reim(Bv,'b'),{}),
  'full_normal_terms':len(n),'full_receiver_terms':len(B)})
 for part in ['normal_real','normal_imag']:
  out['roots'][-1][part]['gram_robust_certified']=structural['all_trace_products_zero'] and out['roots'][-1][part]['certified_nonzero_coefficients']>0
  out['roots'][-1][part]['certificate_method']='All polarized trace products vanish, hence exact Herm-HS ratio1/2 on the complete real image; one coefficient is separated on the root ball; 1/2>1/4 defeats every allowed N/Vol-I operator norm<1/2.'
 print('root finished',ri,'ratios',[(p,out['roots'][-1][p]['Herm_ratio'],out['roots'][-1][p].get('gram_robust_certified',False))for p in ['normal_real','normal_imag','range_real','range_imag']],flush=True)
"""Exact native symmetry and finite caution controls; appended to receiver probe."""

def symmetry_controls():
    from source_action_slice_completion_probe import column, sigma
    checks={}
    def check(k,v):
        checks[k]=bool(v)
        assert v,k
    # b=-Re tr/128. Multiplying both arguments by i changes the real
    # Clifford coefficient pairing by minus, and tau reverses these fields.
    central=[]
    for axis in (0,3):
        e=1<<axis
        bx=-E.weight(e,0)
        bt=-bx
        central.append({'axis':axis,'b_X_X':str(bx),'b_X_tauX':str(bt)})
    check('tau_majorant_indefinite',central==[
        {'axis':0,'b_X_X':'1','b_X_tauX':'-1'},
        {'axis':3,'b_X_X':'-1','b_X_tauX':'1'}])
    # Exact PT lift on the native unprimed 15-component field. J commutes
    # with real gamma generators; this tests the remaining U/form action.
    U={15:Q(1)}
    def T(field):
        z,nu=field
        return [scale(-1 if a<4 else 1,mul(U,z[a]))for a in range(14)],mul(U,nu)
    def fs(c,v):return [scale(c,x)for x in v[0]],scale(c,v[1])
    for axis in range(14):
        sign=-1 if axis<4 else 1
        for j in range(15):
            field=column(j)
            check(f'PT_native_symbol_{axis}_{j}',
                sigma(covector(axis),T(field))==fs(sign,T(sigma(covector(axis),field))))
    for j in range(5):
        observed=readout(T(inject(j)))
        wanted=[{}for _ in range(5)]
        wanted[j]=scale(-1 if j<4 else 1,U)
        check(f'PT_same_injection_{j}',observed==wanted)
        check(f'PT_injection_no_normal_leak_{j}',not any(T(inject(j))[0][4:]))
    check('PT_spin_lift_square',mul(U,U)=={0:Q(-1)})
    check('PT_spin_lift_Euclidean_unitary',hsweight(15)==1)
    # Real-action independent-bar transformation: use a rational complex
    # quaternionic control and arbitrary non-Hermitian vertex. This is a
    # control for the general dual covariance proof, not a native matrix.
    def mm(A,B):
        return [[sum((C(x)*C(y)for x,y in zip(row,col)),C())for col in zip(*B)]for row in A]
    def cc(A):return [[C(z).conj()for z in row]for row in A]
    QJ=[[0,1],[-1,0]];QJi=[[0,-1],[1,0]]
    V=[[C(2,3),C(1,-2)],[C(-4,1),C(3,2)]]
    psi=[[C(1,2)],[C(3,-1)]];beta=[[C(2,-1),C(4,3)]]
    transformed=mm(mm(cc(beta),QJi),mm(mm(mm(QJ,cc(V)),QJi),mm(QJ,cc(psi))))[0][0]
    before=mm(beta,mm(V,psi))[0][0]
    check('independent_bar_interaction_conjugates',transformed==before.conj())
    check('real_interaction_invariant',transformed.a==before.a)
    for n in (Q(1),Q(2),Q(7,3)):
        Z=C(0,n);I=C(0,1)
        q=(-I*Z).a
        check(f'pureJ_charge_reversed_{n}',(-I*Z.conj()).a==-q and q>0)
        check(f'PT_charge_preserved_{n}',(-I*(-Z.conj())).a==q)
    # Exact elementary counterexample to equating work with forced energy.
    check('negative_test_vector',Q(1)**2-Q(2)**2<0)
    check('nonzero_work_positive_only_force',Q(1)*Q(1)+Q(0)*Q(2)!=0)
    check('force_energy_positive',Q(1)**2-Q(0)**2>0)
    return {'checks':checks,'count':len(checks),'central_pairing':central,
        'scope':'Native pointwise pairing, all15symbol columns for14axes, same literal injection; independent-bar two-dimensional mechanism and phase controls. Closed-domain and actual-variable symmetry require the written covariance/CK proof.'}


out['symmetry_controls']=symmetry_controls()

out['scope']='Pointwise same-injection current matrix on complete derivative-source spin6/7 response. Cross-Gram-robust nonzero, when certified, is not full reduced forcing, admitted propagation, physical ghost or instability.'
s=json.dumps(out,indent=2)+'\n'
if args.output: args.output.write_text(s)
else: print(s)
print('DONE',round(time.time()-t0,2),flush=True)
