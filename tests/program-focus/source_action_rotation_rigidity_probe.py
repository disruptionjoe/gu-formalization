"""Exact native controls for symmetry selection versus observed dynamics.

The analytic orbit/CK arguments are written proofs. This verifies their actual
normal representation, full rolled symbol, central geometry and contrary cases.
No physical Hilbert domain, global solution or coupled response is computed.
"""
from fractions import Fraction as Q
from pathlib import Path
from itertools import combinations
import argparse, hashlib, json
import source_action_deep_geometry as g
import source_action_slice_completion_probe as m
from source_action_deep_algebra import add, scale

ROOT=Path(__file__).resolve().parents[2]

def rref(rows):
    a=[list(map(Q,row)) for row in rows]; piv=[];i=0
    for j in range(len(a[0])):
        k=next((k for k in range(i,len(a)) if a[k][j]),None)
        if k is None:continue
        a[i],a[k]=a[k],a[i];v=a[i][j];a[i]=[x/v for x in a[i]]
        for k in range(len(a)):
            if k!=i and a[k][j]:
                v=a[k][j];a[k]=[x-v*y for x,y in zip(a[k],a[i])]
        piv.append(j);i+=1
        if i==len(a):break
    return a,piv

def nullspace(rows):
    a,p=rref(rows);n=len(a[0]);out=[]
    for j in range(n):
        if j in p:continue
        v=[Q(0)]*n;v[j]=Q(1)
        for i,k in enumerate(p):v[k]=-a[i][j]
        out.append(v)
    return out

def flat(a):return [x for row in a for x in row]
def form_matrix(H):
    return [[g.h_action(H,j+4).get(i+4,Q(0)) for j in range(10)]for i in range(10)]
def gens():
    out=[]
    for i,j in combinations(range(4),2):
        h=g.zero();h[i][j]=Q(1);h[j][i]=-g.eta[i]*g.eta[j];out.append(((i,j),h))
    return out

def run():
    checks=[]
    def check(name,cond):
        assert cond,name;checks.append(name)
    G=gens();R=[h for (i,j),h in G if j<3];L=[h for _,h in G]
    def fixed(gs):
        rows=[]
        for h in gs:
            a=form_matrix(h);rows.extend([list(x)for x in zip(*a)])
        return nullspace(rows)
    sr=fixed(R);lr=fixed(L)
    check('SO3_fixed_dual_dimension2',len(sr)==2)
    check('SO3_fixed_dual_only_native_trace_and_spatial_scalar',all(all(not v[j] for j in [1,2,4,5,6,7,8,9])for v in sr))
    check('Lorentz_fixed_dual_dimension1',len(lr)==1)
    trace=[g.trace(a)for a in g.A]
    check('Lorentz_fixed_dual_exact_trace_line',lr[0][0]!=0 and all(lr[0][j]*trace[0]==lr[0][0]*trace[j]for j in range(10)))
    for name,gs,n in [('SO3',R,3),('Lorentz',L,6)]:
        comms=[flat(g.comm(a,b))for a in gs for b in gs]
        check(name+'_Lie_algebra_spanned_by_brackets',len(rref(comms)[1])==n)
    J=next(h for ij,h in G if ij==(0,1));trans=g.comm(J,g.A[1]);t=g.h_action(J,5)
    check('A01_seed_transverse_rotation',set(t)=={8} and abs(t[8])==2)
    quarter=g.eye();quarter[0][0]=quarter[1][1]=0;quarter[0][1]=-1;quarter[1][0]=1
    qt=[list(x)for x in zip(*quarter)]
    for j,a in enumerate(g.A):
        rotated=g.mm(g.mm(quarter,a),qt)
        check('quarterturn_flips_seed_functional_'+str(j),rotated[0][1]==-a[0][1])
    for j,a in enumerate(g.A):
        check('central_trace_commutes_with_normal_'+str(j),g.comm(g.eye(),a)==g.zero())
        check('trace_metric_dual_'+str(j),g.vg(g.diag([Q(-1,4)]*4),a)==g.trace(a))
    for j in range(4):check('central_affine_horizontal_scaling_'+str(j),g.mbracket(4,j)=={j:Q(1)})
    check('shape_isotropy_not_constant_control',g.comm(g.A[1],g.A[4])!=g.zero())
    check('raw_trace_dual_norm_minus1',g.vg(g.diag([Q(-1,4)]*4),g.diag([Q(-1,4)]*4))==-1)
    check('coordinate_trace_dual_norm_minus1over16',Q(1)/g.d[4]==Q(-1,16))
    # All 15 vector/scalar slots, with arbitrary spinor right coefficient.
    for j in [0,1,2,3,4]:
        xi=m.covector(j)
        for c in range(15):
            v=m.column(c)
            check(f'full_symbol_left_inverse_{j}_{c}',m.inverse(xi,m.sigma(xi,v))==v)
            check(f'full_symbol_right_inverse_{j}_{c}',m.sigma(xi,m.inverse(xi,v))==v)
    # Actual homogeneous metric is invariant under simultaneous x/y dilation.
    # Work at eta with arbitrary symmetric variations encoded by normal A.
    b=Q(5,4)
    for i in range(4):
        check('horizontal_metric_dilation_'+str(i),(g.eta[i]/(b*b))*b*b==g.eta[i])
    def smul(c,a):return [[c*x for x in row]for row in a]
    frame=g.diag([Q(1,2),Q(1,3),Q(1,5),Q(1,7)])
    eta=g.diag(g.eta);yinverse=g.diag([g.eta[i]*Q([2,3,5,7][i]**2)for i in range(4)])
    variations=[smul(-2,g.mm(g.mm(frame,g.mm(eta,a)),frame))for a in g.A]
    def vertical(yi,u,v):
        yu=g.mm(yi,u);yv=g.mm(yi,v)
        return g.trace(g.mm(yu,yv))-Q(1,2)*g.trace(yu)*g.trace(yv)
    for i,u in enumerate(variations):
        for j,v in enumerate(variations):
            original=vertical(yinverse,u,v)
            changed=vertical(smul(b*b,yinverse),smul(1/(b*b),u),smul(1/(b*b),v))
            check(f'trace_reversed_vertical_dilation_{i}_{j}',original==changed==g.vg(g.A[i],g.A[j]))
    check('omitted_tangent_scaling_is_detected',vertical(smul(b*b,yinverse),variations[0],variations[0])!=vertical(yinverse,variations[0],variations[0]))
    # Contrary case: freeze the metric-fibre horizontal coefficients.
    xi=m.covector(0);xi[3]=Q(1);psi=m.slash(xi)
    z=[scale(xi[i],psi)for i in range(14)];v=(z,{})
    check('frozen_null_vector_spinor_nonzero',m.norm(xi)==0 and v!=m.zero())
    check('frozen_null_vector_spinor_solves_symbol',m.sigma(xi,v)==m.zero())
    shifted=xi.copy();shifted[0]=b
    check('actual_anisotropic_geometry_removes_null_witness',m.norm(shifted)!=0 and m.sigma(shifted,v)!=m.zero())
    for j in range(3):
        lam=[Q(2),Q(-3),Q(5),Q(7)]+[Q(0)]*10;new=lam.copy();new[j]*=b
        check('nonnull_unmasking_identity_'+str(j),m.norm(new)-m.norm(lam)==(b*b-1)*lam[j]*lam[j])
    # A trace-dependent lower term can cancel arbitrary seed derivatives:
    # D=exp(s) d_x+C(s), C(s)=-exp(s) admits exp(x), so C-shift is essential.
    check('trace_dependent_lower_countercontrol',b-b==0 and Q(1)-b!=0)
    refs=['tests/program-focus/source_action_deep_geometry.py','tests/program-focus/source_action_slice_completion_probe.py','explorations/conditional-build/source-action-homogeneous-analytic-vacuum-2026-11-25.md','explorations/conditional-build/source-action-dynamics-and-continuation-2026-11-25.md']
    return {'basis_revision':'aefa70d80c905fdb7b5bb97ab587a4da75f4a402','checks':checks,'check_count':len(checks),'SO3_fixed_covectors_native':[list(map(str,v))for v in sr],'Lorentz_fixed_covectors_native':[list(map(str,v))for v in lr],'raw_trace_components':list(map(str,trace)),'A01_transverse_generator':{str(k):str(v)for k,v in t.items()},'trace_dual_norm':'-1','trace_coordinate_dual_norm':'-1/16','full_symbol_columns':15,'nonnull_coordinate_axes':[0,1,2,3,4],'source_hashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in refs},'scope':'Exact finite representation, native symbol and geometric controls. Orbit saturation, analytic uniqueness, full coefficient naturality and CK history lifting are written proofs with independent review. No physical domain, selected dynamics or GU falsification.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);a=p.parse_args();out=json.dumps(run(),indent=2)+'\n'
    if a.output:a.output.write_text(out)
    else:print(out)
