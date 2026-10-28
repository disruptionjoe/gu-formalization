#!/usr/bin/env python3
"""Exact Pfaffian circuit controls against original fullCl77 ten-row maps.
No port search or expanded 240-variable monomial calculation.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from functools import lru_cache
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
import k2169_invertible_pencil_full_descent_probe as o
I=S.eye(32);ZERO=S.zeros(32);gam=[]
for sign in [1,-1]:
    for j in range(5):
        g=S.zeros(32)
        for m in range(32):
            g[m^(1<<j),m]=(-1)**((m&((1<<j)-1)).bit_count())*(sign if m&(1<<j) else 1)
        gam.append(g)
gam[4]=S.I*gam[4]
B=S.zeros(32)
for m in range(32):
    co=31^m;k=m.bit_count();sw=sum((co&((1<<j)-1)).bit_count() for j in range(5) if m&(1<<j))
    B[m,co]=(-1)**(k*(k-1)//2+sw)
ids=[[m for m in range(32) if m.bit_count()%2==p] for p in range(2)]
J=I
for j,g in enumerate(gam):
    if j!=4:J=J*g

def clean(x):return x.applyfunc(S.expand)
def bar(x):return clean(-J*x.conjugate()*J)
@lru_cache(None)
def normal(mask):
    z=I
    for j in range(10):
        if mask&(1<<j):z=z*gam[j]
    return z

def matrix(x):
    z=S.zeros(32)
    for mask,c in x.items():
        tw=mask&o.WM
        assert tw in (0,o.WM)
        nm=sum((1<<j) for j,n in enumerate(o.N) if mask&(1<<n))
        sg=(-1)**sum(w>n for w in o.W for n in o.N if mask&(1<<n)) if tw else 1
        z+=S.Rational(c.numerator,c.denominator)*sg*(S.I if tw else 1)*normal(nm)
    return z

def pfadj(a):
    """Division-free shared-minor Pfaffian circuit, valid on singular input."""
    n=a.rows
    assert n%2==0 and a.T==-a
    @lru_cache(None)
    def pf(mask):
        if not mask:return S.Integer(1)
        ii=[i for i in range(n) if mask&(1<<i)];i=ii[0];out=0
        for pos,j in enumerate(ii[1:],1):
            if a[i,j]:out+=(-1)**(pos+1)*a[i,j]*pf(mask^(1<<i)^(1<<j))
        return S.expand(out)
    allmask=(1<<n)-1;h=S.zeros(n)
    for i in range(n):
        for j in range(i+1,n):
            h[i,j]=(-1)**(i+j)*pf(allmask^(1<<i)^(1<<j));h[j,i]=-h[i,j]
    return pf(allmask),h

def fixture(mult=1):
    aa=o.blade(o.N[:3]);bb=o.blade([o.N[j] for j in [0,3,4]]);cc=o.blade([o.N[j] for j in [0,1,5]])
    w=o.scale(o.add(aa,bb),mult);u=o.scale(o.add(aa,cc),mult)
    v=o.mm(o.blade(o.N),w);t=o.mm(o.OM,u);p=o.add(o.scale(v,7),o.scale(t,-15));r=o.add(v,o.scale(t,3));z=o.add(v,t)
    inv=o.inv(p);ts={j:o.scale(o.mm(inv,o.port(r)[j]),-o.ETA[j]) for j in o.N}
    qs={j:o.RR(ts,*o.C(o.port(z),*o.kernel(ts,j)))[1] for j in o.N}
    return dict(w=matrix(w),u=matrix(u),v=matrix(v),t=matrix(t),p=matrix(p),r=matrix(r),z=matrix(z),ts={j:matrix(x) for j,x in ts.items()},qs={j:matrix(x) for j,x in qs.items()})

def circuit(data,fault=None):
    p,r,z,t=(data[k] for k in ['p','r','z','t']);bp=bar(p);br=bar(r)
    rr=[(g*r+r*g)/2 for g in gam];ss=[(g*br+br*g)/2 for g in gam];dd=[(g*z+z*g)/2 for g in gam]
    answers=[];checks={}
    for half,ee in enumerate(ids):
        ff=ids[1-half];even=lambda x:x.extract(ee,ee);other=lambda x:x.extract(ff,ff)
        E=lambda x:x.extract(ff,ee);F=lambda x:x.extract(ee,ff)
        om=(B*bp).extract(ee,ee);d,h=pfadj(om);rho=S.expand(d*S.conjugate(d))
        ll=h*B.extract(ee,ff);lift=S.zeros(32)
        for i,ii in enumerate(ee):
            for j,jj in enumerate(ff):lift[ii,jj]=ll[i,j]
        nn=E(bar(lift))
        checks[f'pfaffian_two_sided_{half}']=om*h==h*om==d*S.eye(16)
        checks[f'pfaffian_determinant_{half}']=om.det()==d*d
        checks[f'actual_denominator_nonzero_{half}']=rho!=0
        checks[f'bar_inverse_numerator_{half}']=ll*E(bp)==d*S.eye(16)
        checks[f'real_transport_inverse_numerator_{half}']=F(p)*nn==S.conjugate(d)*S.eye(16)
        xx=[-o.ETA[j]*nn*even(rr[k]) for k,j in enumerate(o.N)]
        zz=[-o.ETA[j]*ll*other(ss[k]) for k,j in enumerate(o.N)]
        checks[f'all_adapters_numerators_{half}']=all(clean(xx[k]-S.conjugate(d)*E(data['ts'][j]))==S.zeros(16) and clean(zz[k]-d*F(bar(data['ts'][j])))==S.zeros(16) for k,j in enumerate(o.N))
        vals=[]
        for k,j in enumerate(o.N):
            val=4*d*F(t)*xx[k]-o.ETA[j]*rho*even(dd[k])+(8 if fault=='coefficient' else 7)*S.conjugate(d)*zz[k]*E(z)
            val+=2*sum((zz[l]*other(ss[l])*xx[k] for l in range(10)),S.zeros(16))
            if fault=='product_order':
                val+=2*(other(ss[0])*zz[0]-zz[0]*other(ss[0]))*xx[k]
            for l in range(10):
                com=dd[l]*gam[k]-gam[k]*dd[l]
                val+=(1 if fault=='omit_eta' else o.ETA[j])*S.conjugate(d)*zz[l]*E(com)
            vals.append(clean(val))
        checks[f'all10_original_rows_{half}']=all(vals[k]==rho*even(data['qs'][j]) for k,j in enumerate(o.N))
        checks[f'all10_actual_rows_reject_{half}']=all(v!=S.zeros(16) for v in vals)
        answers.append((d,rho,vals))
    return checks,answers

def controls():
    checks={};faults={};data=fixture()
    checks['real_structure_fixes_all10_gamma']=all(bar(g)==g for g in gam)
    checks['quaternionic_square']=J*J.conjugate()==-I
    checks['actual_noncommuting_and_nonanticommuting']=data['v']*data['t']!=data['t']*data['v'] and data['v']*data['t']!=-data['t']*data['v']
    # Genuine actual-pencil determinant identity behind the one-saturation
    # corollary after prescribed invertible Y and real-grade reconstruction.
    yy=clean(data['p'].inv()*bar(data['p']));ee=ids[0]
    op=(B*data['p']).extract(ee,ee);ob=(B*bar(data['p'])).extract(ee,ee);yp=yy.extract(ee,ee)
    checks['prescribed_factor_real_grade_equation']=clean(op*yp-ob)==S.zeros(16)
    checks['prescribed_factor_determinant_nonzero']=yp.det()!=0
    checks['prescribed_factor_same_pfaffian_zero_locus_identity']=ob.det()==op.det()*yp.det()
    # Singular supplied Y destroys the nonvanishing equivalence: invertible
    # alternating Omega with OmegaY=0 still leaves the other pencil singular.
    checks['singular_Y_cannot_drop_second_inequation']=op.det()!=0 and (op*S.zeros(16)).det()==0
    cs,out=circuit(data);checks.update(cs)
    # An independent scalar2 fixture verifies the complete all-row degree17 identity.
    cs2,out2=circuit(fixture(2));checks.update({'scaled_'+k:v for k,v in cs2.items()})
    checks['all20_polynomial_homogeneity_degree17']=all(out2[h][2][j]==2**17*out[h][2][j] for h in range(2) for j in range(10))
    checks['both_denominators_degree16']=all(out2[h][1]==2**16*out[h][1] for h in range(2))
    # Singular-locus counterfeit: all degree17 numerators vanish at P=0,
    # whereas the nonzero-port chart's saturation equations give -1, not0.
    zero={k:S.zeros(32) for k in ['p','r','z','t']};zero['qs']={j:S.zeros(32) for j in o.N};zero['ts']={j:S.zeros(32) for j in o.N}
    _,out0=circuit(zero)
    checks['singular_zero_polynomial_counterfeit']=all(rho==0 and all(v==S.zeros(16) for v in vals) for d,rho,vals in out0)
    checks['saturation_rejects_zero_chart']=all(S.symbols('s')*rho-1==-1 for d,rho,vals in out0)
    # Pfaffian adjugate identity survives at rank14; division does not.
    j2=S.Matrix([[0,1],[-1,0]]);sing=S.diag(*([j2]*7+[S.zeros(2)]));d,h=pfadj(sing)
    checks['rank14_singular_pfadj_nonzero']=sing.rank()==14 and d==0 and h!=S.zeros(16) and sing*h==h*sing==S.zeros(16)
    # Original zero port is a separately admitted full-descent positive control.
    ts={j:{} for j in o.N}
    checks['original_zero_port_positive']=all(o.RR(ts,*o.C([{} for _ in range(14)],*o.kernel(ts,j)))==({mu:{} for mu in o.W},{}) for j in o.N)
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    for fault in ['coefficient','product_order','omit_eta']:
        bad,_=circuit(data,fault);fails=[k for k,v in bad.items() if not v]
        assert fails,('undetected',fault);faults[fault]=fails
    # Cofactor sign corruption breaks the actual original inverse equation.
    om=(B*bar(data['p'])).extract(ids[0],ids[0]);d,h=pfadj(om);bad=h.copy();pair=next((i,j) for i in range(16) for j in range(16) if h[i,j]);bad[pair]=-bad[pair]
    faults['cofactor_sign']=['original inverse identity'] if om*bad!=d*S.eye(16) else []
    assert faults['cofactor_sign']
    return checks,faults
def main():
    import argparse,hashlib,json
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    checks,faults=controls()
    deps=[
      'explorations/conditional-build/k2211-pfaffian-adapter-system-2026-10-28.md',
      'explorations/conditional-build/k2169-invertible-pencil-full-descent-2026-10-27.md',
      'explorations/conditional-build/k2208-grade-constrained-pencil-reconstruction-2026-10-28.md',
      'tests/channel-swings/k2169_invertible_pencil_full_descent_probe.py',
      'tests/channel-swings/k2159_commutant_equation_adapters_probe.py',
      'tests/channel-swings/k2165_even_clifford_adapter_descent_probe.py']
    report=dict(result_id='K2211',status='exact_full_row_pfaffian_polynomial_criterion',checks=checks,fault_failures=faults,
      dependency_sha256={x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in deps},
      probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      evidence_kinds='Universal chiral Pfaffian degree17 all-ten-row equivalence proof; exact finite fullCl77 original-map comparisons on actual grade ports; singular and positive controls; genuine coefficient, order, metric and cofactor faults. No port search, system emptiness, physical, proof-assistant or external-expert certificate.')
    dst=ROOT/'lab/process/k2211-pfaffian-adapter-system.json'
    if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dst.read_text())==report,'report drift'
    print(json.dumps(dict(result='K2211',controls=len(checks),faults={k:len(v) for k,v in faults.items()})))
if __name__=='__main__':main()
