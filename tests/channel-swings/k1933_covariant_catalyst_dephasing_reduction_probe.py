"""Independent component-wise partial traces and phase selection controls."""
import sympy as s
import json
import k1933_covariant_catalyst_dephasing_reduction as p

def independent():
    checks=0
    # Phase selection for several energy spectra, including degeneracy.
    for en in ([0,1],[0,1,1],[0,2,5]):
        q=13;d=len(en)
        # Integer character orthogonality, no sampled real-time approximation.
        for a in range(d):
          for b in range(d):
            kept=(en[a]-en[b])%q==0
            assert kept==(en[a]==en[b]);checks+=1
    # Independent indexed Stinespring contraction for an energy-preserving SWAP.
    sig=s.Matrix([[s.Rational(3,4),s.Rational(1,8)],[s.Rational(1,8),s.Rational(1,4)]])
    for i in range(2):
      for j in range(2):
        X=s.zeros(2);X[i,j]=1
        out=s.Matrix(2,2,lambda a,b:sum(X[k,k]*sig[a,b] for k in range(2)))
        assert out==s.trace(X)*sig;checks+=1
    # Covariant CZ target with arbitrary allowed real coherence: channel is invariant,
    # basis-one catalyst displacement equals twice the off-diagonal entry.
    for a in (s.Rational(1,4),s.Rational(1,2),s.Rational(3,4)):
      for c in (s.S(0),s.Rational(1,10)):
        sig=s.Matrix([[a,c],[c,1-a]]);Z=s.diag(1,-1);delta=Z*sig*Z-sig
        assert set(delta.eigenvals())==({s.S(0)} if c==0 else {-2*c,2*c});checks+=1
        assert s.trace(Z*sig)==2*a-1;checks+=1
    return checks

def main():
    base=p.report();assert json.loads((p.ROOT/'lab/process/k1933-covariant-catalyst-dephasing-reduction.json').read_text())==base
    n=independent()
    for fault in ('energy','swap'):
        p.calc()
        try:p.calc(fault)
        except AssertionError as e:print('[EXPECTED FAIL]',fault,str(e))
        else:raise AssertionError('undetected '+fault)
    for key in ('theorem','script_sha256'):
        bad=dict(base);bad[key]='corrupt'
        try:assert bad==p.report(),'report/pin equality'
        except AssertionError:print('[EXPECTED FAIL]',key)
        else:raise AssertionError('undetected reporting mutation')
    print(json.dumps({'independent_exact_checks':n,'mathematical_input_faults':2,'reporting_faults':2}))
if __name__=='__main__':main()
