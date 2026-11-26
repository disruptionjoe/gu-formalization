"""Exact off-section Q4 coefficient in the declared W2 K95 tangent.
No physical spectrum or fibre integration. Reuses certified stationary-root balls.
"""
from fractions import Fraction as Q
from pathlib import Path
import json,argparse
from math import isqrt
repo=Path(__file__).resolve().parents[2]
import source_action_deep_geometry as geo
from source_action_deep_algebra import Engine,add,scale,clean
from source_action_metric_symbol_probe import metric_symbol,matrix_unit,wedge_xi
from source_action_physical_probe import interval
E=Engine(geo)

def Hform(h,x):
    out={}
    for (e,c),v in x.items():
        for j in range(14):
            if not(e>>j&1):continue
            f=e^(1<<j)
            for i in range(14):
                if not h[j][i] or f>>i&1:continue
                q=h[j][i]/geo.d[j]*E.sign(1<<j,f)*E.sign(1<<i,f)
                key=(f|1<<i,c);out[key]=out.get(key,Q(0))+v*q
    return clean(out)

def trH(h):return sum(h[i][i]/geo.d[i] for i in range(14))

def delta_star(h,x):return E.star(add(scale(trH(h)/2,x),scale(-1,Hform(h,x))))

def delta_phi_explicit(h,x):
    def ds(z):
        v,d=z;return E.star(v),add(E.star(d),delta_star(h,v))
    def di(z):
        v,d=z;y=E.star_inverse(v)
        return y,add(E.star_inverse(d),scale(-1,E.star_inverse(delta_star(h,y))))
    def dw(a,b,kind):
        v,d=a;w,e=b
        return E.wedge(v,w,kind),add(E.wedge(d,w,kind),E.wedge(v,e,kind))
    p1=(E.phi1,scale(Q(1,2),Hform(h,E.phi1)))
    p2=(E.phi2,scale(Q(1,2),Hform(h,E.phi2)))
    # Antisymmetrized Phi2 differentiation, not gamma_i gamma_j at a
    # varying off-diagonal metric (which would introduce a false scalar).
    assert p2[1]==scale(Q(1,2),add(E.wedge(p1[1],p1[0]),E.wedge(p1[0],p1[1])))
    z=(x,{})
    first=dw(p1,ds(z),'comm')
    second=ds(dw(p1,ds(dw(p2,ds(z),'anti')),'anti'))
    v,d=di((add(first[0],scale(Q(1,2),second[0])),add(first[1],scale(Q(1,2),second[1]))))
    assert v==E.Phi(x)
    return d

def coeff_variation(h,T,W):
    # COMPLETE volume, pairing and Phi variation, divided by rho.
    return (trH(h)*E.pair(T,E.Phi(W))-E.pair(Hform(h,T),E.Phi(W))-E.pair(T,E.Phi(Hform(h,W))))/2

def shifted(l,m,r):
    z=interval(l,r)
    for key in ['center','lower','upper']:z[key]=str(Q(z[key])+m)
    z['approximate_center']=float(Q(z['center']))
    z['sign']='positive' if Q(z['lower'])>0 else ('negative' if Q(z['upper'])<0 else 'unresolved')
    return z


def evaluate(amp,r,basis,explicit_check=False):
    xi=[Q(0)]*14;xi[3]=Q(1)
    h,b=metric_symbol([Q(1),Q(1),Q(1),-1/r],amp,xi)
    W=wedge_xi(xi,b)
    natural=scale(Q(1,2),add(Hform(h,E.Phi(W)),scale(-1,E.Phi(Hform(h,W)))))
    if explicit_check:assert delta_phi_explicit(h,W)==natural
    PW=E.Phi(W)
    c=[coeff_variation(h,T,W)for T in basis]
    for T,z in zip(basis,c):
        assert trH(h)/2*E.pair(T,PW)-E.pair(Hform(h,T),PW)+E.pair(T,natural)==z
    bb=E.wedge(b,b);Pbb=E.Phi(bb);Pb=E.Phi_adj(b)
    algebra=[Q(1,3)*E.pair(T,Pbb)-Q(1,6)*E.pair(Pb,add(E.wedge(b,T),E.wedge(T,b)))for T in basis]
    mass=Q(1,2)*E.pair(b,b)
    return {'mass':[mass],'C':c,'algebra':algebra,
            'jet':[a+z/2 for a,z in zip(algebra,c)],
            'fourier':[a-z/2 for a,z in zip(algebra,c)]}

def polynomial(v1,v2,v3):
    c2=[(c-2*b+a)/2 for a,b,c in zip(v1,v2,v3)]
    c1=[b-a-3*c for a,b,c in zip(v1,v2,c2)]
    c0=[a-b-c for a,b,c in zip(v1,c1,c2)]
    return [c0,c1,c2]

def peval(poly,r):return [sum(r**i*poly[i][j] for i in range(3)) for j in range(len(poly[0]))]

def global_signs(pol,roots):
    # Identity holds as an affine functional, not just at approximate roots.
    assert pol['mass'][1][0]==-2*pol['mass'][2][0]
    assert all(a==-2*b for a,b in zip(pol['fourier'][1],pol['fourier'][2]))
    out=[]
    for root in roots:
        central=shifted(peval(pol['fourier'],Q(1)),peval(pol['mass'],Q(1))[0],root)
        curvature=shifted(pol['fourier'][2],pol['mass'][2][0],root)
        assert Q(central['lower'])>0
        if Q(curvature['lower'])>0:
            out.append({'classification':'strictly_positive_for_every_r_gt_zero',
                        'center':central,'curvature':curvature})
        else:
            assert Q(curvature['upper'])<0
            low=Q(central['lower'])/(-Q(curvature['lower']))
            high=Q(central['upper'])/(-Q(curvature['upper']))
            scale=10**12
            dlo=Q(isqrt(low.numerator*scale*scale//low.denominator),scale)
            dhi=Q(isqrt(high.numerator*scale*scale//high.denominator)+1,scale)
            assert dlo*dlo<=low and dhi*dhi>high and 0<dlo<dhi<1
            left=(1-dhi,1-dlo);right=(1+dlo,1+dhi)
            out.append({'classification':'two_simple_positive_r_zeros; positive_between_actual_zeros; negative_outside',
                'center':central,'curvature':curvature,
                'left_zero_interval':list(map(str,left)),
                'right_zero_interval':list(map(str,right)),
                'approximate_zero_intervals':[[float(v)for v in left],[float(v)for v in right]],
                'uniform_positive_interval':[str(left[1]),str(right[0])],
                'uniform_negative_intervals':[['0',str(left[0])],[str(right[1]),'infinity']]})
    return out


def periodic_sign_control():
    # Exact Laurent coefficients represented by rational (real,imag) pairs.
    def derivative(f):return {k:(-k*v[1],k*v[0])for k,v in f.items()}
    def average(f,g):
        return sum(v[0]*g.get(-k,(0,0))[0]-v[1]*g.get(-k,(0,0))[1]for k,v in f.items())
    p={1:(Q(1,2),Q(0)),-1:(Q(1,2),Q(0))}
    p1=derivative(p);p2=derivative(p1);p3=derivative(p2)
    assert average(p1,p3)==-Q(1,2) and average(p2,p2)==Q(1,2)
    return {'average_pprime_pthird':'-1/2','average_psecond_squared':'1/2'}


def run():
    data=json.loads((repo/'lab/process/source-action-deep-coefficients.json').read_text())
    basis=[{(int(e),int(c)):Q(v) for e,c,v in row} for row in data['basis']]
    roots=data['certified_roots'];results={};checks=0
    p=matrix_unit(1,1);p[2][2]=Q(-1);q=matrix_unit(1,2)
    allpolys={}
    for name,amp in [('TT_plus',p),('TT_cross',q)]:
        values=[evaluate(amp,Q(r),basis,explicit_check=(r==2))for r in (1,2,3)]
        pol={key:polynomial(*(v[key]for v in values))for key in values[0]}
        control=evaluate(amp,Q(1,2),basis,explicit_check=True)
        assert all(peval(pol[key],Q(1,2))==control[key]for key in pol);checks+=len(pol)
        assert not any(values[0]['C']) and any(control['C']);checks+=2
        assert control['fourier']!=control['jet'];checks+=1
        allpolys[name]=pol
        intervals=[]
        # Coefficients of each root's scalar quadratic polynomial; errors are
        # coordinate-ball bounds. Correlations retained in evaluation below.
        for root in roots:
            intervals.append([shifted(pol['fourier'][i],pol['mass'][i][0],root)for i in range(3)])
        samples={}
        for r in [Q(1,8),Q(1,4),Q(1,2),Q(1),Q(2),Q(4),Q(8)]:
            m=peval(pol['mass'],r)[0];f=peval(pol['fourier'],r);j=peval(pol['jet'],r);c=peval(pol['C'],r);a=peval(pol['algebra'],r)
            samples[str(r)]={'fourier':[shifted(f,m,z)for z in roots],
                 'jet_density':[shifted(j,m,z)for z in roots],
                 'complete_C':[interval(c,z)for z in roots],
                 'omitted_geometry_mutation':[shifted(a,m,z)for z in roots]}
        results[name]={'mass_polynomial':list(map(str,[row[0]for row in pol['mass']])),
             'fourier_functional_polynomial':[[str(v)for v in row]for row in pol['fourier']],
             'C_functional_polynomial':[[str(v)for v in row]for row in pol['C']],
             'root_fourier_polynomial_intervals':intervals,'samples':samples,
             'all_positive_r_sign_proof':global_signs(pol,roots)}
    assert allpolys['TT_plus']==allpolys['TT_cross'];checks+=1
    # Exact full59 relation: no fit to two backgrounds, no higher-grade debt.
    hfun=[sum(T.get((1<<i,1<<i),Q(0))for i in range(4))/4 for T in basis]
    tfun=[T.get((1<<4,1<<4),Q(0))for T in basis]
    ufun=[sum(T.get((1<<i,1<<i),Q(0))for i in range(5,14))/9 for T in basis]
    native=allpolys['TT_plus']
    assert peval(native['mass'],Q(1))==[Q(1,16)] and native['mass'][2]==[Q(1,16)];checks+=1
    assert peval(native['fourier'],Q(1))==[u/12 for u in ufun];checks+=1
    assert native['fourier'][2]==[h/3+t/6+4*u/3 for h,t,u in zip(hfun,tfun,ufun)];checks+=1

    together=[[p[i][j]+q[i][j]for j in range(4)]for i in range(4)]
    combined=[evaluate(together,Q(r),basis)for r in (1,2,3)]
    for key in allpolys['TT_plus']:
        crosspoly=polynomial(*(v[key]for v in combined))
        assert all(a==2*b for row,base in zip(crosspoly,allpolys['TT_plus'][key])for a,b in zip(row,base));checks+=1
    # Independently differentiate the actual star/glyph under uniform scaling.
    hd=[[geo.d[i]*int(i==j)for j in range(14)]for i in range(14)]
    W={((1<<0)|(1<<1),1<<0):Q(1)}
    PW=E.Phi(W);assert PW
    Tcontrol={next(iter(PW)):Q(1)}
    assert E.pair(Tcontrol,PW)!=0;checks+=1
    assert coeff_variation(hd,Tcontrol,W)==Q(11,2)*E.pair(Tcontrol,PW);checks+=1
    assert delta_phi_explicit(hd,W)==scale(-Q(1,2),PW);checks+=1
    for T in basis:
        assert coeff_variation(hd,T,W)==Q(11,2)*E.pair(T,E.Phi(W));checks+=1
    return {'controls':checks,'periodic_sign_control':periodic_sign_control(),
       'parameter':'r=1/a>0, g0=diag(1,1,1,-a), y=diag(1,1,1,-1), xi=theta3',
       'degree_proof':'h and b are affine in r; every complete Q4 term is quadratic in them, hence degree<=2. Three evaluations determine it, fourth checks it.',
       'TT_polarizations_equal_as_functionals':True,'polarized_TT_cross_identically_zero':True,
       'exact_full59_response_relation':'Q(r)=A+C(r-1)^2; A=1/16+u/12; C=1/16+h/3+t/6+4u/3. h,t,u are horizontal, normal-trace, normal-traceless Clifford-vector coefficients. All higher grades cancel.',
       'existing_scalar_relation':'C+2A=3/16+mH/3+5*mN/3, mH=h, mN=(t+9u)/10; mY,mH,mN alone do not determine trace/traceless split.',
       'results':results,
       'scope':'Pointwise per-native-volume coefficient; Ahat coordinate one-form held in symmetric spin identification. No fibre integral or physical spectrum. Root certificates reused.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);args=parser.parse_args()
    result=json.dumps(run(),indent=2)+'\n'
    if args.output:args.output.write_text(result)
    else:print(result)
