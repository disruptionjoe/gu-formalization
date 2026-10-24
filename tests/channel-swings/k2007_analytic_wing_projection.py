"""Exact algebraic/logarithmic norm certificate for the actual full wing.

Continuum projection, weighted inverse and cap-penalty proofs are in the
accompanying note. All production enclosures use rational arithmetic.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
OUT_REL = 'lab/process/k2007-analytic-wing-projection.json'
DEN = 10**35

class Interval:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = self.lo if hi is None else F(hi)
        assert self.lo <= self.hi
    @staticmethod
    def cast(x):
        return x if isinstance(x, Interval) else Interval(x)
    @staticmethod
    def rounded(lo, hi):
        return Interval(F((lo*DEN).__floor__(), DEN), F((hi*DEN).__ceil__(), DEN))
    def __add__(self, x):
        x=self.cast(x)
        return self.rounded(self.lo+x.lo, self.hi+x.hi)
    __radd__=__add__
    def __neg__(self): return Interval(-self.hi, -self.lo)
    def __sub__(self,x): return self+-self.cast(x)
    def __rsub__(self,x): return self.cast(x)+-self
    def __mul__(self,x):
        x=self.cast(x)
        vals=[self.lo*x.lo,self.lo*x.hi,self.hi*x.lo,self.hi*x.hi]
        return self.rounded(min(vals),max(vals))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self.cast(x)
        assert x.lo*x.hi>0
        return self*Interval(1/x.hi,1/x.lo)
    def __rtruediv__(self,x): return self.cast(x)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        out=Interval(1)
        for _ in range(n): out=out*self
        return out
    def strings(self): return [str(self.lo),str(self.hi)]

def horner(p,x):
    out=0
    for c in p[::-1]: out=out*x+c
    return out

def parameters():
    p=[-138,392,-168,-102,101]
    lo,hi=F(9,20),F(23,50)
    for _ in range(100):
        mid=(lo+hi)/2
        if horner(p,mid)<0: lo=mid
        else: hi=mid
    t=Interval(lo,hi)
    k=horner([F(1,6),0,F(-1,2),F(2,3),F(-1,4)],t)
    d=horner([F(-7,100),F(69,200),F(-77,200)],t)
    return t,d/k

def log_point(x):
    """atanh series and geometric tail; arguments here lie in[1/3,3]."""
    x=F(x)
    assert x>0
    if x<1:
        lo,hi=log_point(1/x)
        return -hi,-lo
    z=(x-1)/(x+1)
    assert 0<=z<F(3,4)
    terms=60
    partial=2*sum(z**(2*j+1)/F(2*j+1) for j in range(terms))
    tail=2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return partial,partial+tail

def logarithm(x):
    x=Interval.cast(x)
    return Interval.rounded(log_point(x.lo)[0],log_point(x.hi)[1])

def poly_integral(p,x):
    return sum(c*x**(j+1)/F(j+1) for j,c in enumerate(p))

def row_pieces(t,lam):
    L=3-t; M=F(23,100)
    phases=[ [0,1-lam/2,lam/2], [1,0,0],
        [3+lam*(3-t*t),-1+lam*(t*t-5)/2,lam/2] ]
    return [[2*Interval.cast(c)/M+([-9+2*L,-1,0][j])
             for j,c in enumerate(p)] for p in phases]

def moment_pieces(t,lam):
    L=3-t; rows=row_pieces(t,lam)
    bounds=[Interval(0),Interval(1),Interval(2),L]
    total=Interval(0); moments=[]
    for row,lo,hi in zip(rows,bounds,bounds[1:]):
        constant=poly_integral(row,lo)-total
        moments.append([constant,Interval(0),row[1]/2,2*row[2]/3])
        total+=poly_integral(row,hi)-poly_integral(row,lo)
    return bounds,rows,moments,total

def rational_integral(p,lo,hi,L,squared=True):
    """Integral p(x)^2/[x²(2L-x)] via polynomial+partial fractions."""
    numerator=[Interval(0) for _ in range(7)]
    if squared:
        for i,a in enumerate(p):
            for j,b in enumerate(p): numerator[i+j]+=a*b
    else:
        numerator[:len(p)]=p
    B=(p[0]*p[0] if squared else p[0])/(2*L)
    A=B/(2*L)
    C=(horner(p,2*L)**2 if squared else horner(p,2*L))/(4*L*L)
    numerator[0]-=2*L*B
    numerator[1]-=-B+2*L*A
    numerator[2]-=-A+C
    quotient=[Interval(0) for _ in range(4)]
    for j in range(6,2,-1):
        quotient[j-3]=-numerator[j]
        numerator[j-1]-=2*L*quotient[j-3]
        numerator[j]=Interval(0)
    assert all(v.lo<=0<=v.hi for v in numerator[:3])
    value=poly_integral(quotient,hi)-poly_integral(quotient,lo)
    value-=C*logarithm((2*L-hi)/(2*L-lo))
    if lo.lo>0:
        if A.lo!=0 or A.hi!=0: value+=A*logarithm(hi/lo)
        if B.lo!=0 or B.hi!=0: value+=B*(1/lo-1/hi)
    else:
        assert p[0].lo==p[0].hi==0
    return value

def clipped_dual_certificates(bounds,moments,L,wing,subdivisions=48):
    """Whole-domain continuum lower bounds for rationally scaled potentials."""
    tails=[Interval(0)]*4
    for j in range(2,-1,-1):
        tails[j]=tails[j+1]+rational_integral(moments[j],bounds[j],bounds[j+1],L,False)
    nodes=[]
    for j,(left,right) in enumerate(zip(bounds,bounds[1:])):
        width=(right-left)/subdivisions
        for k in range(subdivisions):
            x=left+F(2*k+1,2)*width
            e=rational_integral(moments[j],x,right,L,False)+tails[j+1]
            d=horner(moments[j],x)/(x*(2*L-x))-e
            nodes.append((x,width,d,e))
    def top_excess(d,g):
        return (max(F(0),-1-g*d)**3-max(F(0),-1-g*(d+1))**3
                +max(F(0),g*(d+1)-1)**3-max(F(0),g*d-1)**3)
    results=[]
    for gamma in [F(1),F(9,8),F(5,4),F(11,8),F(3,2),F(7,4),F(2)]:
        assert 0<gamma<=2
        top=bottom=F(0)
        for i,(x,width,d,e) in enumerate(nodes):
            dlo,dhi=d.lo-3*width.hi,d.hi+3*width.hi
            cost=(top_excess(dhi,gamma) if dhi < -1/gamma else
                  top_excess(dlo,gamma) if dlo > 1/gamma-1 else F(0))
            top+=width.lo*L.lo*cost/(3*gamma)
            # Off-diagonal cells are complete rectangles in x<y<L.
            # Omit diagonal triangles; their excess is nonnegative.
            for _,ywidth,_,ye in nodes[i+1:]:
                qlo=d.lo+ye.lo-3*width.hi-ywidth.hi
                qhi=d.hi+ye.hi+3*width.hi+ywidth.hi
                deficit=max(F(0),gamma*qlo-1,-1-gamma*qhi)
                bottom+=width.lo*ywidth.lo*deficit*deficit
        dual=(2*gamma-gamma*gamma)*wing+top+bottom
        results.append({'scale':str(gamma),'top_rectangle_penalty_lower':str(top),
                        'lower_triangle_penalty_lower':str(bottom),
                        'normalized_wing_dual_interval':dual.strings()})
    return results,[[v.strings() for v in node] for node in nodes]

def restricted_existing_dual(root,bounds,rows,L,reflected=False):
    """Restrict the already published full-strip additive witness to one wing."""
    old=json.loads((root/'lab/process/k1989-capped-pulse-dual-certificates.json').read_text())['certificate']
    M=F(23,100); step=F(6,old['grid_rows'])
    ap=[F(v)/M for v in old['row_potentials']]
    bp=[F(v)/M for v in old['column_potentials']]
    if reflected:
        ap=[-v for v in ap[::-1]]
        bp=[-v for v in bp[::-1]]
    xs=[]; ys=[]
    for i,a in enumerate(ap):
        lo=Interval(i*step)
        if lo.lo>=L.hi: break
        hi=Interval((i+1)*step) if (i+1)*step<L.lo else L
        xs.append((lo,hi,a))
    for j,b in enumerate(bp):
        lo=Interval(j*step)
        if lo.lo>=(2*L).hi: break
        hi=Interval((j+1)*step) if (j+1)*step<(2*L).lo else 2*L
        ys.append((lo,hi,b))
    linear=Interval(0); conjugate=Interval(0)
    for lo,hi,a in xs:
        mass=Interval(0)
        for left,right,row in zip(bounds,bounds[1:],rows):
            if hi.hi<=left.lo or lo.lo>=right.hi: continue
            l=left if left.lo>lo.lo else lo
            h=right if right.hi<hi.hi else hi
            mass+=poly_integral(row,h)-poly_integral(row,l)
        linear+=a*mass
    for lo,hi,b in ys:
        def positive(v): return Interval(max(F(0),v.lo),max(F(0),v.hi))
        mass=(positive(hi-L)**2-positive(lo-L)**2)/2
        linear+=b*mass
    for i,(xl,xh,a) in enumerate(xs):
        for j,(yl,yh,b) in enumerate(ys):
            if i>j: continue
            area=(xh-xl)*(yh-yl) if i<j else (xh-xl)*(yh-xl)-(xh-xl)**2/2
            p=a+b; H=p*p if abs(p)<=1 else 2*abs(p)-1
            conjugate+=area*H
    return 2*linear-conjugate,len(xs),len(ys)

def produce(root=ROOT):
    t,lam=parameters(); L=3-t; W=3+4*t; M=F(23,100)
    bounds,rows,moments,total=moment_pieces(t,lam)
    integrals=[rational_integral(p,lo,hi,L)
               for p,lo,hi in zip(moments,bounds,bounds[1:])]
    integral=sum(integrals,Interval(0))
    wing=L*L/3+integral
    central_data=json.loads((root/'lab/process/k2003-exact-central-pulse-optimizer.json').read_text())
    central=Interval(*map(F,central_data['central_minimum_squared_norm_interval']))
    whole=M*M*(54-F(7,3)*L*L-2*t*W+2*integral)+central
    # Exact terminal derivative bound for s in[0,1/9].
    Lmin=F(127,50)
    rprime=F(29,3)+F(14,207)
    bound=(rprime+F(3,2)/(1-1/(81*Lmin*Lmin)))/Lmin
    assert bound<F(9,2)
    assert F(3,2)*Lmin>rprime/9
    assert F(1,9)<1-t.hi
    penalty=L/864
    duals,nodes=clipped_dual_certificates(bounds,moments,L,wing)
    best=max(duals,key=lambda row:F(row['normalized_wing_dual_interval'][0]))
    best_wing=Interval(*map(F,best['normalized_wing_dual_interval']))
    inherited_left,old_rows,old_cols=restricted_existing_dual(root,bounds,rows,L)
    inherited_right,_,_=restricted_existing_dual(root,bounds,rows,L,True)
    inherited_wing=max([inherited_left,inherited_right],key=lambda value:value.lo)
    inherited_side='left' if inherited_wing is inherited_left else 'right_reflected'
    method='scaled_analytic_projection'
    if inherited_wing.lo>best_wing.lo:
        best_wing=inherited_wing
        method='restricted_k1989_dual_with_exact_forced_and_central_regions'
    strengthened=M*M*(54-3*L*L-2*t*W)+central+2*M*M*best_wing
    inherited=F(central_data['inherited_squared_norm_lower_bound'])
    upper=F(central_data['whole_pulse_squared_norm_upper_bound'])
    assert integral.lo>0 and wing.lo>0
    assert total.lo <= (L*L/2).hi and (L*L/2).lo <= total.hi
    terminal=horner(moments[-1],L)+F(3,2)*L*L
    assert terminal.lo<=0<=terminal.hi
    assert strengthened.hi<upper
    checks=7
    # Integrate the entire certified wedge, not only a sampled rectangle.
    C=F(9,2); smax=1/(2*C)
    wedge=F(1,3)*(F(1,2)**4)/(4*C)
    assert wedge==F(1,864) and smax==F(1,9)
    checks+=2
    inputs=[
        'explorations/conditional-build/k1991-tight-cut-pulse-factorization-2026-10-23.md',
        'explorations/conditional-build/k1986-pulse-primal-dual-certificates-2026-10-23.md',
        'lab/process/k2003-exact-central-pulse-optimizer.json',
        'lab/process/k1989-capped-pulse-dual-certificates.json']
    return {
        'result_id':'K2007','status':'active_research',
        'classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL',
        'root_interval':t.strings(),'lambda_interval':lam.strings(),
        'wing_length_interval':L.strings(),
        'rational_integral_piece_intervals':[v.strings() for v in integrals],
        'normalized_wing_uncapped_minimum_squared_norm_interval':wing.strings(),
        'factorized_uncapped_whole_squared_norm_lower_interval':whole.strings(),
        'normalized_wing_cap_penalty_interval':penalty.strings(),
        'scaled_clipped_dual_certificates':duals,
        'selected_dual_scale':best['scale'],
        'selected_dual_method':method,
        'restricted_k1989_normalized_wing_dual_interval':inherited_wing.strings(),
        'restricted_k1989_left_wing_dual_interval':inherited_left.strings(),
        'restricted_k1989_right_reflected_wing_dual_interval':inherited_right.strings(),
        'restricted_k1989_selected_side':inherited_side,
        'restricted_k1989_cell_shape':[old_rows,old_cols],
        'certified_whole_norm_lower_decimal':str(F((strengthened.lo*10**6).__floor__(),10**6)),
        'clipped_dual_cells_per_phase_piece':48,
        'clipped_dual_potential_nodes':nodes,
        'whole_capped_squared_norm_lower_interval':strengthened.strings(),
        'whole_capped_squared_norm_upper_bound':str(upper),
        'improvement_over_k1989_lower_interval':(strengthened-inherited).strings(),
        'terminal_derivative_upper':str(bound),
        'certified_wedge':{'s_interval':['0','1/9'],
            'y_interval':'L < y < L*(3/2-(9/2)*s)',
            'normalized_penalty':'L/864'},
        'weighted_marginal_inverse_norm_upper':'2',
        'exact_controls':checks,
        'scope':'Actual full-wing uncapped minimum by explicit rational/log integral; strict capped penalty and whole-pulse lower combined with exact central minimum. Effective weighted unrestricted marginal inverse. No capped feasible wing, full optimizer, cap-preserving correction, phase-energy change, GU verdict, novelty or external certification.',
        'inputs':{p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in inputs}}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--root',type=Path,default=ROOT)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=produce(args.root)
    out=args.output or args.root/OUT_REL
    if args.write: out.write_text(json.dumps(result,indent=2)+'\n')
    else: assert result==json.loads(out.read_text())
    print('PASS K2007 exact wing/whole norm',
          [float(F(v)) for v in result['whole_capped_squared_norm_lower_interval']],
          'controls',result['exact_controls'])
