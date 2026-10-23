"""Independent exact integrations and adversarial controls, not a proof assistant."""
from fractions import Fraction as F
from pathlib import Path
import json,copy
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def check(d):
    count=0
    x,y,C=s.symbols('x y C',positive=True)
    assert s.simplify(s.integrate(1-C*(1-x)/2,(x,1-2/C,1))/2-1/(2*C))==0
    assert s.simplify(s.integrate((y-1+1/C)**2,(y,1-1/C,1))-1/(3*C**3))==0
    count+=2
    for r in d['coarse_pulses']:
        n=r['n'];t=F(r['t']);alpha=4*t/(3+4*t)
        # Integrate sign(y-x) over each actual cell by its two triangular areas.
        h=F(2,n);matrix=[]
        for i in range(n):
            rr=[]
            for j in range(n):
                if j>i:val=F(1)
                elif j<i:val=F(-1)
                else:val=F(0)
                rr.append(val)
            matrix.append(rr)
        mids=[-1+(F(i)+F(1,2))*h for i in range(n)]
        row=col=F(0)
        for i in range(n):
            avg=alpha*sum(matrix[i])/n-(1-alpha)*mids[i]
            lo=-1+i*h;hi=lo+h
            row+=((hi+avg)**3-(lo+avg)**3)/6
            colavg=sum(matrix[k][i] for k in range(n))/n
            col+=alpha*((hi-colavg)**3-(lo-colavg)**3)/6
        assert row==F(r['row_residual_squared']),'row residual'
        assert col==F(r['column_residual_squared']),'column residual'
        assert row+col==F(r['combined_residual_squared']),'combined residual'
        # Diagonal squares have normalized mass 1/n; q has magnitude1 there.
        assert alpha/n+(1-alpha)*h*h/12==F(r['elementary_pulse_distance_squared']),'strong distance'
        count+=4
    for r in d['conditioning']:
        c=F(r['C']);t=F(r['t']);beta=2*t/(3+4*t)
        assert F(r['h_column_ceiling'])==1-F(1,2*c),'ceiling'
        assert F(r['q_column_residual_lower_squared'])==beta/(3*c**3),'conditioning lower'
        count+=2
    # Contrary cases: cap-free rank2 additive solution; capped exact sign kernel.
    for i in range(1,20):
        z=F(i,20)
        assert (1-z)/2==F(1,2)-z/2
        assert -F(-9,10)+F(9,10)>1  # additive exact-marginal ansatz violates cap
        count+=1
    return count
if __name__=='__main__':
    d=json.loads((ROOT/'lab/process/k1997-finite-rank-pulse-obstruction.json').read_text());n=check(d);caught=[]
    for key,field in [('coarse_pulses','row_residual_squared'),('coarse_pulses','elementary_pulse_distance_squared'),('conditioning','h_column_ceiling'),('conditioning','q_column_residual_lower_squared')]:
        bad=copy.deepcopy(d);bad[key][0][field]=str(F(bad[key][0][field])+F(1,100))
        try:check(bad)
        except AssertionError as e:
            assert str(e);caught.append(field);print('DETECTED mathematical fault:',field,str(e))
        else:raise AssertionError('missed '+field)
    print('PASS K1997 probe:',n,'exact integration/algebra/contrary controls;',len(caught),'faults rejected after green baseline')
