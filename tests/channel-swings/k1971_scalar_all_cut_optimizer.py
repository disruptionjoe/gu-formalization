"""All-interval analytic separation; finite-union scouts remain explicitly finite."""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json
import k1969_scalar_continuum_separation as old
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1971-scalar-all-cut-optimizer.json'
M=F(23,100)
def interval_capacity(a,b):
    s=b-a;u=a+3;v=3-b
    if s<=3:return 9*s-max(F(0),s-u)**2-max(F(0),s-v)**2
    return 9*(u+v)-u*u-v*v

def D(u,v):
    """Affine baseline; start u in[0,1], end v in[2,9/4]."""
    u,v=F(u),F(v)
    return -F(77,200)*v*v+F(393,200)*v-F(5,2)+F(23,200)*(9-4*v)*u-u*u/25

def calculate():
    n=0
    def ck(c,m):
        nonlocal n
        assert c,m;n+=1
    for i in range(25):
        for j in range(i+1,25):
            a,b=F(-3)+F(i,4),F(-3)+F(j,4)
            ck(interval_capacity(a,b)==old.capacity([(a,b)]),'closed capacity vs full sliding integration')
    l,r=old.isolate();lam=old.iv(old.ip(old.D,(l,r)),old.ip(old.K,(l,r)))
    ck(F(3,50)<lam[0]<lam[1]<F(7,100),'inherited contact multiplier interval')
    ck(1-F(7,100)/2>4*M,'strict outer derivative exceeds4M')
    ck(9*M/2-1==F(7,200)>0,'unsaturated interval strict margin')
    ck(D(0,F(9,4))==F(-89,3200),'right rectangle edge')
    ck(D(1,2)==F(-7,200),'top/left rectangle edge')
    ck(-F(77,100)*(-F(2,25))-(-F(23,50))**2<0,'indefinite rectangle Hessian')
    ck(F(393,200)-F(77,100)*F(9,4)>0,'u0 edge increasing')
    ck(F(393,200)-F(23,50)-F(77,100)*2<0,'u1 edge decreasing')
    ck(F(23,200)-F(2,25)>0,'v2 edge increasing to u1')
    ck(-F(21,50)+F(23,40)/2-F(1,100)==-F(57,400),'v1 active edge')
    ck(8*M/2>F(3,4),'short outer interval')
    ck(9-2*(3)==3,'cross-zero one-excursion capacity derivative')
    ck(27-8*3-2*F(3,2)==0,'cross-zero two-excursion capacity derivative')
    ck(9-2/M==F(7,23),'all measurable small-mass exclusion')
    # Scout the rational surrogate only. Grid coverage is not all-cut coverage.
    import k1963_effective_scalar_cut_certificates as graph
    t=(l+r)/2;ll=old.poly(old.D,t)/old.poly(old.K,t);scouts=[]
    for h in [F(1,8),F(1,16),F(1,32)]:
        vals=[graph.phi0_integral(-3+i*h,-3+(i+1)*h)-ll*sum(old.green(-3+(i+1)*h,s)-old.green(-3+i*h,s) for s in [-t,t]) for i in range(int(6/h))]
        rec=graph.graph_certificate(h,vals);ck(F(rec['minimum_deficit'])==0,'finite all-grid-union rational scout');scouts.append(rec)
    return dict(result_id='K1971',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_controls=n,all_interval_status='proved analytically, both signs, including complements',all_measurable_status='OPEN; finite grid scouts are not a continuum certificate',small_mass_threshold='7/23',surrogate_t=str(t),finite_grid_scouts=scouts,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1969-scalar-continuum-separation.json','tests/channel-swings/k1969_scalar_continuum_separation.py','tests/channel-swings/k1963_effective_scalar_cut_certificates.py','tests/channel-swings/k1942_complete_scalar_energy_duality.py']})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=calculate()
    if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
    else:assert v==json.loads(OUT.read_text())
    print('PASS K1971',v['exact_controls'],'exact algebra/capacity and finite-union controls; full measurable status OPEN')
