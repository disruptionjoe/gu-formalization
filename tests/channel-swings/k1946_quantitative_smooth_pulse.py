"""Quantitative smooth pulse defined by exact finite data and normalized integrals.
No floating quadrature or new LP participates in acceptance.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json
from bisect import bisect_right
from k1944_optimized_scalar_pulse_certificate import verify
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1946-quantitative-smooth-pulse.json'
SEED='lab/process/k1944-optimized-scalar-pulse-certificate.json'
def affine(knots,x):
    if x<=knots[0][0] or x>=knots[-1][0]:return F(0)
    i=bisect_right([u for u,v in knots],x)-1;a,A=knots[i];b,B=knots[i+1]
    return A+(B-A)*(x-a)/(b-a)
def flattened(y,h,e):
    points={F(-3):F(0),F(3):F(0),F(-2):F(1),F(-1):F(1),F(1):F(-1),F(2):F(-1)}
    for a,b in [(F(-3),F(-2)),(F(-1),F(1)),(F(2),F(3))]:
        for i,Y in enumerate(y):
            u=-3+i*h
            if a<=u<=b:points[a+e+(b-a-2*e)*(u-a)/(b-a)]=Y
    return sorted(points.items())
def bounds(seed,e):
    h=F(seed['h']);y=list(map(F,seed['phase_nodes']));knots=[(-3+i*h,Y) for i,Y in enumerate(y)]
    L=max(abs((b-a)/h) for a,b in zip(y,y[1:]));A=max(map(abs,y));energy=F(seed['energy']);M=F(seed['amplitude'])
    assert 0<e<F(1,4),'smoothing radius range'
    flat=flattened(y,h,e);J=sum((B-A0)**2/(b-a) for (a,A0),(b,B) in zip(flat,flat[1:]))
    maxdiff=max(abs(affine(flat,u)-affine(knots,u)) for u in sorted(set(u for u,v in flat+knots)))
    assert maxdiff<=L*e,'flattening uniform error';assert J<=energy/(1-2*e),'flattening energy bound'
    # e is flattening width, pulse contraction1-e and pulse convolution radius e.
    # Phase convolution radius e/4 keeps closed plateaux exactly constant.
    residual=F(5,4)*L*e+e*(A+4*L)
    T=F(9,2);G=16/T;Gp=128/T**2;Gpp=10240/T**3
    K=3*Gp+G;peak=M+K*residual
    rprime=L/(1-2*e)+L
    dx=32*M/e+Gp*residual/2+G*rprime
    dt=32*M/e+(3*Gpp+F(3,2)*Gp)*residual+G*rprime
    return dict(radius=str(e),phase_radius=str(e/4),contraction=str(1-e),lipschitz=str(L),phase_sup=str(A),flattened_knots=[[str(u),str(v)] for u,v in flat],flattened_energy=str(J),phase_energy_upper=str(J),flattening_error=str(maxdiff),residual_sup_bound=str(residual),correction_coefficient=str(K),pulse_amplitude_upper=str(peak),energy_slack=str(F(401,100)-J),amplitude_slack=str(F(23,100)-peak),spatial_derivative_upper=str(dx),time_derivative_upper=str(dt),phase_support_margin=str(3*e/4),seed_pulse_u_margin=str(2*e),seed_pulse_characteristic_margin=str(F(5,2)*e),g_bounds=list(map(str,[G,Gp,Gpp])))
def produce():
    seed=json.loads((ROOT/SEED).read_text())['pulse'];reused,_=verify(seed);r=bounds(seed,F(1,2000000));assert F(r['amplitude_slack'])>0,'certified amplitude budget';assert F(r['energy_slack'])>0,'certified energy budget'
    # Exact consumers at three scales; largest tested one trades amplitude for derivatives.
    family=[bounds(seed,e) for e in [F(1,10000000),F(1,4000000),F(1,2000000)]]
    for v in family:assert F(v['pulse_amplitude_upper'])<F(23,100) and F(v['phase_energy_upper'])<F(401,100)
    return dict(result_id='K1946',status='active_research',seed_ref=SEED,seed_sha256=hashlib.sha256((ROOT/SEED).read_bytes()).hexdigest(),reused_seed_exact_checks=reused,construction=r,family=family,definition={'bump':'eta(s)=exp(-1/(1-s^2))/integral_-1^1 exp(-1/(1-r^2))dr for |s|<1, else0','smooth_phase':'psi=eta_(e/4)*f_e; f_e is flattened_knots interpolated linearly, zero outside','pulse_seed':'w_a(u,z)=w(u/a,(z-(1-a)*9/2)/a), a=1-e; w is the exact inherited affine-rectangle pulse','pulse_smooth':'w_p=(eta_e tensor eta_e)*w_a; phi_p=eta_e*(a phi(. /a))','residual':'r=psi-phi_p; f(u)=-1/2 integral_-infinity^u r(v)dv','time_bump':'g(t)=(4/T)eta(4(t-T/2)/T), T=9/2','physical_pulse':'V(t,x)=2 w_p(x-t,x+t)+g_prime(t) f(x-t)+g(t)r(x-t)'},scope={'smooth_exact_plateaux':True,'exact_zero_opposite_phase':True,'native_GU':False,'spectral_bandlimit':False,'exact_global_optimizer':False},source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();r=produce()
    if args.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert r==json.loads(OUT.read_text()),'report drift'
    print('PASS K1946 rational geometry and3 quantitative consumers;',r['reused_seed_exact_checks'],'inherited pulse checks')
    for key in ['pulse_amplitude_upper','phase_energy_upper','spatial_derivative_upper','time_derivative_upper']:print(key,float(F(r['construction'][key])))
