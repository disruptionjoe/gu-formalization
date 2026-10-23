"""Independent symbolic cycle algebra and certified midpoint gain comparison."""
from fractions import Fraction as F
from pathlib import Path
import json,copy
import sympy as s
from k1969_scalar_continuum_separation import isolate
R=Path(__file__).resolve().parents[2]
def check(d):
    x,t,e=s.symbols('x t e',real=True);f=lambda z:(3+4*t)*z/(3+4*t*z)
    q=s.Matrix([-f(x),1,-f(x+s.Rational(1,2)),-f(x+s.Rational(1,2))]);direction=s.Matrix([1,-1,-1,1])
    reduction=s.expand((q.dot(q)-(q+e*direction).dot(q+e*direction)))
    assert s.simplify(reduction-(2*e*(1+f(x))-4*e*e))==0,'cycle gain identity'
    assert direction[0]+direction[1]==direction[2]+direction[3]==direction[0]+direction[2]==direction[1]+direction[3]==0
    # Independent monotone bounds: f_t(x) increasing in both t,x for x in[0,1].
    tl,tr=isolate();fun=lambda z,tt:(3+4*tt)*z/(3+4*tt*z);lo=F(0);hi=F(0);N=1024;dx=F(1,4*N)
    for i in range(N):
        a=F(1,4)+i*dx;b=a+dx
        el=1-fun(b+F(1,2),tr);eh=1-fun(a+F(1,2),tl)
        fl=fun(a,tl);fh=fun(b,tr)
        assert 0<=el<=eh<F(1,5) and 4*eh<1+fl,'optimal admissible amplitude'
        # g=2e(1+f)-4e² increases in e and f in this whole rectangle.
        D=10**30;left=dx*(2*el*(1+fl)-4*el*el);right=dx*(2*eh*(1+fh)-4*eh*eh)
        lo+=F((left*D).__floor__(),D);hi+=F((right*D).__ceil__(),D)
    M=F(23,100);lo*=M*M*tl*tl;hi*=M*M*tr*tr
    a,b=map(F,d['gain_interval']);assert lo<=b and a<=hi and 0<a<b,'certified gain'
    old=json.loads((R/'lab/process/k1991-tight-cut-pulse-factorization.json').read_text());u=F(d['whole_pulse_norm_squared_upper_bound']);assert u==F(old['whole_pulse_norm_squared_upper_bound'])-a,'upper transfer'
    assert F(d['strong_distance_squared_upper_bound'])==u-F(d['inherited_squared_norm_lower_bound']),'distance transfer'
    # Pointwise cap and exact row/column cancellation tested without subject formula.
    for tt in [tl,tr]:
        for j in range(1,65):
            z=F(1,4)+F(j,260);ff=fun(z,tt);gg=fun(z+F(1,2),tt);ee=1-gg
            oldv=[-ff,F(1),-gg,-gg];new=[-ff+ee,1-ee,-1,-gg+ee]
            assert all(abs(v)<=1 for v in new)
            assert new[0]+new[1]==oldv[0]+oldv[1] and new[2]+new[3]==oldv[2]+oldv[3]
            assert new[0]+new[2]==oldv[0]+oldv[2] and new[1]+new[3]==oldv[1]+oldv[3]
    return N+128+5
if __name__=='__main__':
    d=json.loads((R/'lab/process/k1995-central-marginal-cycle-improvement.json').read_text());print('PASS baseline',check(d),'symbolic/interval/cycle obligations')
    faults=[]
    z=copy.deepcopy(d);z['gain_interval']=['1','2'];faults.append(('wrong integral',z))
    z=copy.deepcopy(d);z['whole_pulse_norm_squared_upper_bound']='0';faults.append(('wrong upper transfer',z))
    z=copy.deepcopy(d);z['strong_distance_squared_upper_bound']='0';faults.append(('wrong strong distance',z))
    for name,z in faults:
        try:check(z)
        except AssertionError as e:print('DETECTED mathematical fault:',name,str(e))
        else:raise AssertionError('MISSED '+name)
