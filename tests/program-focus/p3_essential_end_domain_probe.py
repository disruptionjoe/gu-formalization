"""Exact native B5 polynomial symbol identity and analytic scaling controls.
No spectral truncation is offered as proof of the infinite-domain theorem.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')
from pathlib import Path
import sys,json,hashlib
import sympy as sp
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tests/channel-swings'))
from b5_strict_massless_extension_dependence_probe import (folded_symbol_complex,rs_symbol_complex,gauge_symbol_complex,noether_symbol_complex,scale_complex)
from b5_native_rs_bv_hessian_lift_probe import (METRIC,N,ONE,gamma,add,multiply,matrix_multiply,zero_matrix)
from actual_sym2_c14_orbit_probe import native_gammas
NOTE='explorations/conditional-build/p3-essential-end-domain-2026-11-11.md'
REPORT='lab/process/p3-essential-end-domain.json'
checks=[]
def ck(name,value,kind='exact_supporting'):
    assert bool(value),name
    checks.append(dict(name=name,kind=kind))
def clean(a):return {m:sp.expand(c) for m,c in a.items() if sp.expand(c)!=0}
def zmat(a):return all(not clean(c) for row in a for c in row)
def run():
    checks.clear();d,m,n=sp.symbols('delta mu N');xi=[0]*N;xi[0]=-d;xi[4]=xi[9]=sp.I*n
    c=add(*(scale_complex(x,gamma(i)) for i,x in enumerate(xi) if x));cm=add(c,scale_complex(m,ONE));v=zero_matrix(N+1,1)
    v[2][0]=multiply(gamma(2),cm);v[3][0]=multiply(gamma(1),cm)
    ck('actual raised symbol square delta2',clean(multiply(c,c))=={0:d*d})
    ck('integral null raised tangent',METRIC[4]+METRIC[9]==0)
    lowered=[METRIC[i]*xi[i] for i in range(N)]
    ck('actual Fourier phase y4-minus-y9 raises to e4-plus-e9',lowered[4]==sp.I*n and lowered[9]==-sp.I*n)
    ck('plant wrong lowering changes raised normal symbol',METRIC[9]*sp.I*n != xi[9],'exact_contrary')
    middle=[[v[i+1][0]] for i in range(N)]
    trace=add(*(multiply(gamma(i,raised=True),middle[i][0]) for i in range(N)))
    ck('native gamma trace identically zero',not clean(trace))
    ck('native Noether divergence identically zero',zmat(matrix_multiply(noether_symbol_complex(xi),middle)))
    result=matrix_multiply(folded_symbol_complex(xi),v)
    for i in range(N+1):result[i][0]=add(result[i][0],scale_complex(m,v[i][0]))
    expected=zero_matrix(N+1,1);expected[2][0]=scale_complex(m*m-d*d,gamma(2));expected[3][0]=scale_complex(m*m-d*d,gamma(1))
    ck('ALL15 native fold rows satisfy polynomial identity',all(clean(result[i][0])==clean(expected[i][0]) for i in range(N+1)))
    ck('wrong scalar sign is detected',clean(add(result[2][0],scale_complex(-2*m,v[2][0])))!=clean(expected[2][0]),'exact_contrary')
    ck('ghost and field0 exactly absent',not clean(v[0][0]) and not clean(v[1][0]))
    ck('pure gauge has zero transverse slots1and2',not gauge_symbol_complex(xi)[1][0] and not gauge_symbol_complex(xi)[2][0])
    ck('transverse field is not the zero Clifford map',bool(clean(v[2][0])))
    # Cross-result: entire constant-radial K95 projector-compatible connection category.
    b=sp.symbols('b');omega=ONE
    for i in range(N):omega=multiply(omega,gamma(i))
    H=scale_complex(b,multiply(gamma(0),omega));cmh=add(cm,H);vb=zero_matrix(N+1,1)
    vb[2][0]=multiply(gamma(2),cmh);vb[3][0]=multiply(gamma(1),cmh)
    ov=[[multiply(omega,row[0])] for row in vb]
    e0=[1]+[0]*(N-1);extra=matrix_multiply(folded_symbol_complex(e0),ov)
    rb=matrix_multiply(folded_symbol_complex(xi),vb)
    for i in range(N+1):rb[i][0]=add(rb[i][0],scale_complex(b,extra[i][0]),scale_complex(m,vb[i][0]))
    R=add(scale_complex(m*m-d*d-b*b,ONE),scale_complex(2*b*d,omega),scale_complex(2*b*m,multiply(gamma(0),omega)))
    eb=zero_matrix(N+1,1);eb[2][0]=multiply(gamma(2),R);eb[3][0]=multiply(gamma(1),R)
    ck('constant radial compatible connection ALL15 rows polynomial identity',all(clean(rb[i][0])==clean(eb[i][0]) for i in range(N+1)))
    ck('radial connection residual independent of high frequency',all(not coeff.has(n) for row in eb for val in row for coeff in clean(val).values()))
    ck('radial connection is non-scalar',set(clean(H))!={0},'exact_contrary')
    ck('radial connection residual sign plant detected',clean(R)!=clean(add(R,scale_complex(-4*b*d,omega))),'exact_contrary')
    bp=sp.symbols('bprime')
    vbprime=[ [{mask:sp.diff(coeff,b)*bp for mask,coeff in row[0].items() if sp.diff(coeff,b)!=0}] for row in vb ]
    derivative_residual=matrix_multiply(folded_symbol_complex(e0),vbprime)
    ck('variable radial extra derivative independent of high frequency',all(not coeff.has(n) for row in derivative_residual for val in row for coeff in clean(val).values()))
    ck('variable radial derivative correction is not silently dropped',not zmat(derivative_residual),'exact_contrary')
    jj,BB,BBp=sp.symbols('j B Bprime',positive=True)
    chosen_frequency=jj*(1+BB**2+BBp)
    ck('whole smooth radial diagonal bound tends to zero',sp.simplify(1/jj+(1+BB**2+BBp)/chosen_frequency)==2/jj)
    # Native128 matrices independently verify a fixed nonzero spinor and exact growth.
    gs,eta=native_gammas();I=np.eye(128,dtype=complex);cl=gs[4]+gs[9]
    j=next(j for j in range(128) if np.any(cl[:,j]));s=I[:,j];lead=np.concatenate((gs[2]@(1j*cl@s),gs[1]@(1j*cl@s)))
    a=np.vdot(lead,lead).real
    ck('fixed native spinor has nonzero null-Clifford image',np.any(cl@s))
    ck('native norm leading coefficient positive exact integer',a>0 and a==int(a))
    growth=[]
    for delta,mu in [(0,0),(1,0),(2,3),(2,1j),(0,4)]:
        const=(mu*I-delta*gs[0])@s
        base=np.concatenate((gs[2]@const,gs[1]@const));bb=2*np.vdot(base,lead).real;cc=np.vdot(base,base).real
        for nn in [1,2,7,16]:
            vv=base+nn*lead
            ck(f'native exact norm polynomial d{delta}m{mu}N{nn}',np.vdot(vv,vv).real==a*nn*nn+bb*nn+cc)
        growth.append(dict(delta=delta,mu=str(mu),norm_squared_coefficients=[int(a),int(bb),int(cc)]))
    # The same shifted derivatives commute; polynomial complex identities survive weights.
    ck('weighted K A identity',zmat(matrix_multiply(rs_symbol_complex(xi),gauge_symbol_complex(xi))))
    ck('weighted Avee K identity',zmat(matrix_multiply(noether_symbol_complex(xi),rs_symbol_complex(xi))))
    # Scalar shift fails the original gauge identity, so no massive-complex claim.
    kg=matrix_multiply(rs_symbol_complex(xi),gauge_symbol_complex(xi))
    for i in range(N):kg[i][0]=add(kg[i][0],scale_complex(m,gauge_symbol_complex(xi)[i][0]))
    ck('scalar shift does not preserve original gauge complex',not zmat(kg),'exact_contrary')
    x,L=sp.symbols('x L',positive=True);bump=x*x*(1-x)*(1-x)
    norm=sp.integrate(bump*bump,(x,0,1));deriv=sp.integrate(sp.diff(bump,x)**2,(x,0,1))
    ck('H1 compact cutoff normalization nonzero',norm>0)
    ck('normalized cutoff derivative decays1overL',sp.simplify(deriv/(norm*L**2))==12/L**2)
    ck('asymptotic coefficient error times derivative tends zero',sp.limit(n**-2*n,n,sp.oo)==0)
    r,mu=sp.symbols('r mu',positive=True);f=sp.exp(-r);u=(sp.exp(-r)-sp.exp(-mu*r))/(mu-1)
    ck('scalar mass repair solves actual differential equation',sp.simplify(sp.diff(u,r)+mu*u-f)==0)
    ck('scalar mass repair has Dirichlet boundary',sp.simplify(u.subs(r,0))==0)
    ck('scalar Volterra L1 kernel bound',sp.integrate(sp.exp(-mu*r),(r,0,sp.oo))==1/mu)
    ck('weight is not same-Hilbert bounded equivalence',sp.limit(sp.exp(r),r,sp.oo)==sp.oo,'exact_contrary')
    deps=[NOTE,'explorations/conditional-build/x-p1-p2-projector-connection-2026-11-11.md',str(Path(__file__).relative_to(ROOT)),'tests/channel-swings/b5_native_rs_bv_hessian_lift_probe.py','tests/channel-swings/b5_strict_massless_extension_dependence_probe.py','tests/channel-swings/actual_sym2_c14_orbit_probe.py']
    return dict(schema_version='1.0',artifact='p3-essential-end-domain',checks=checks,native_norm_polynomials=growth,hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},proof_scope='Universal polynomial Clifford identity plus exact finite native norm and analytic scaling controls. Infinite-domain Fredholm and quotient arguments are written proofs independently reviewed, not numerical spectrum or Lean.',claim_effect='none')
if __name__=='__main__':
    data=run();p=ROOT/REPORT
    if '--write' in sys.argv:p.write_text(json.dumps(data,indent=2)+'\n')
    else:assert json.loads(p.read_text())==data
    print(json.dumps({k:sum(x['kind']==k for x in checks) for k in sorted({x['kind'] for x in checks})}))
