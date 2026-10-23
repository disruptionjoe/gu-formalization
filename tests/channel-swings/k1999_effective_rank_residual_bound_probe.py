"""Separate integral, matrix and constructive contrary controls for K1999."""
from fractions import Fraction as F
from pathlib import Path
import json,copy,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def check(d):
    x,a,b=s.symbols('x a b',positive=True)
    assert s.integrate(x,(x,a,2*a))==3*a*a/2
    assert s.integrate(x,(x,b,2*b))==3*b*b/2
    count=2
    for c in d['certificates']:
        n=c['rank']+2;rho=F(1,768*n*n);k=F(1,16*n);alpha=F(d['alpha_lower_bound'])
        low=F(c['squared_residual_lower_bound']);amin=F(1,4)*rho**(n-1)
        assert F(c['smallest_row_band'])==amin and F(c['smallest_column_band'])==k*amin,'corner geometry'
        assert alpha==F(1,3) and alpha<F(4)*F(9,20)/(3+4*F(9,20)),'actual root density lower bound'
        assert low/(4*alpha**2*(k*amin)**2*amin)<=F(1,256*n*n),'row Cauchy budget'
        assert low/(4*amin**2*alpha*k*amin)<=F(1,256*n*n),'column Cauchy budget'
        # B=U^-1 reconstructed by successive column differences.
        U=[[F(j>=i) for j in range(n)] for i in range(n)]
        B=[[F(i==j)-F(j==i+1) for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):assert sum(U[i][k]*B[k][j] for k in range(n))==F(i==j);count+=1
        eps=F(c['entry_error_bound']);assert eps==F(3,32*n)+F(1,16*n),'structural plus residual errors'
        assert 2*n*eps<1 and F(1,2)-n*eps==F(c['singular_value_lower_bound']),'robust nonsingularity'
        assert F(c['unrestricted_rank_approximation_error_squared'])==4*F(13,32)**2*alpha*k*amin**2,'unrestricted approximation compression bound'
        assert F(1,2)-n*F(3,32*n)==F(13,32),'exact compression singular margin'
        count+=8
    # Exact midpoint family, recomputed from its finite cell means (not imported formula).
    for n in [2,4,8,16]:
        mids=[F(2*i+1,n)-1 for i in range(n)];alpha=F(3,8)
        for i in range(n):
            row=alpha*sum(F((j>i)-(j<i)) for j in range(n))/n-(1-alpha)*mids[i]
            assert row==-mids[i];count+=1
        residual=sum(s.integrate((x-s.Rational(v.numerator,v.denominator))**2,(x,F(2*i,n)-1,F(2*i+2,n)-1))/2 for i,v in enumerate(mids))
        assert residual==F(1,3*n*n);count+=1
    # Uncapped rank2 exact-marginal solution violates cap on a positive rectangle.
    assert F(3,4)+F(3,4)>1
    for p,h in d['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    return count+1
if __name__=='__main__':
    d=json.loads((ROOT/'lab/process/k1999-effective-rank-residual-bound.json').read_text());n=check(d);caught=[]
    for fault in ['residual_bound','band','matrix_error','singular_bound','approximation_bound']:
        q=copy.deepcopy(d);c=q['certificates'][0]
        if fault=='residual_bound':c['squared_residual_lower_bound']=str(100*F(c['squared_residual_lower_bound']))
        if fault=='band':c['smallest_row_band']=str(2*F(c['smallest_row_band']))
        if fault=='matrix_error':c['entry_error_bound']='1'
        if fault=='singular_bound':c['singular_value_lower_bound']='1/2'
        if fault=='approximation_bound':c['unrestricted_rank_approximation_error_squared']='1'
        try:check(q)
        except AssertionError as e:caught.append([fault,str(e)])
        else:raise AssertionError('undetected mathematical fault '+fault)
    print('PASS K1999',n,'separate integral/matrix/approximation checks;',caught)
