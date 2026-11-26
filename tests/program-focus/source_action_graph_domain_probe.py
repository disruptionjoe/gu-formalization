"""Exact native graph-lift symbol test, standard library only.

No full auxiliary inverse or propagated physical state is asserted. The finite
calculation uses the actual imaginary-U real coefficient sector and native K95
symbol. Root owns serialized execution and repository integration.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse,json,math,sys

def run_graph_symbols(root):
    root=Path(root);sys.path.insert(0,str(root/'tests/program-focus'))
    import source_action_deep_geometry as geo
    from source_action_deep_algebra import Engine
    from source_action_metric_symbol_probe import symbols
    E=Engine(geo)
    def rr(a):
        a=[list(r)for r in a];row=0;ps=[]
        for c in range(len(a[0])):
            k=next((k for k in range(row,len(a))if a[k][c]),None)
            if k is None:continue
            a[row],a[k]=a[k],a[row];v=a[row][c];a[row]=[x/v for x in a[row]]
            for j in range(len(a)):
                if j!=row and a[j][c]:
                    q=a[j][c];a[j]=[x-q*y for x,y in zip(a[j],a[row])]
            ps.append(c);row+=1
            if row==len(a):break
        return a,ps
    def null(a):
        R,ps=rr(a);out=[]
        for k in range(len(a[0])):
            if k not in ps:
                v=[Q(0)]*len(a[0]);v[k]=Q(1)
                for j,c in enumerate(ps):v[c]=-R[j][k]
                out.append(v)
        return out
    def inv(a):
        n=len(a);R,p=rr([list(row)+[Q(i==j)for j in range(n)]for i,row in enumerate(a)])
        assert p[:n]==list(range(n));return [row[n:]for row in R]
    def mm(a,b):
        return [[sum((x*y for x,y in zip(row,col)),Q(0))for col in zip(*b)]for row in a]
    def tr(a):return list(map(list,zip(*a)))
    def rk(a):return len(rr(a)[1])if a and a[0]else 0
    def zer(a):return not any(x for row in a for x in row)
    def serial_vector(bs,v):return [[e,c,str(a[0])]for(e,c),a in zip(bs,v)if a[0]]
    def block_test(axes,coefficients,size):
        t=3;generators=[t]+axes;others=[i for i in range(14)if i not in generators]
        r=sum(1<<a for a in others[:size])
        labels=[r^sum((1<<axis)for j,axis in enumerate(generators)if bits>>j&1)
                for bits in range(1<<len(generators))]
        bs=[(1<<i,(1<<i)^lab)for lab in labels for i in range(14)]
        # Actual imaginary-Clifford coefficient subspace; physical field is iX.
        bs=[b for b in bs if b[1].bit_count()%4 in(0,3)]
        assert len(set(bs))==len(bs)
        mats=[]
        for mode in ('time','space'):
            xi=[Q(0)]*14
            if mode=='time':xi[t]=Q(1)
            else:
                for axis,c in zip(axes,coefficients):xi[axis]=Q(c)
            cols=[symbols(E,xi,{key:Q(1)})[0]for key in bs]
            assert all(set(v)<=set(bs)for v in cols)
            mats.append([[v.get(key,Q(0))for v in cols]for key in bs])
        A,K=mats;n=len(bs);_,ps=rr(A);rank=len(ps)
        R=tr([[A[i][j]for i in range(n)]for j in ps]);N=tr(null(A))
        S=[u+v for u,v in zip(R,N)];Si=inv(S)
        At=mm(mm(Si,A),S);Kt=mm(mm(Si,K),S)
        assert zer([row[rank:]for row in At])
        assert zer(At[rank:])
        Ar=[row[:rank]for row in At[:rank]];G=inv(Ar)
        C=[row[:rank]for row in Kt[:rank]];W=[row[rank:]for row in Kt[:rank]]
        V=[row[:rank]for row in Kt[rank:]];NN=[row[rank:]for row in Kt[rank:]]
        assert zer(NN)
        U=mm(G,W);assert zer(mm(V,U))
        F=mm(G,C);VF=mm(V,F);Z=tr(null(V));leak=mm(VF,Z)
        nonzero=next(((i,j,z)for i,row in enumerate(leak)for j,z in enumerate(row)if z),None)
        item={'transverse_degree':size,'imaginary_dimension':n,'time_range':rank,
              'time_kernel':n-rank,'V_rank':rk(V),'VF_rank':rk(VF),
              'Levi_leak_rank':rk(leak)}
        if nonzero:
            i,j,value=nonzero;coords=[[row[j]]for row in Z];v=mm(R,coords)
            residue_N=mm(VF,coords);raw=mm(N,residue_N)
            assert zer(mm(V,coords))and not zer(raw)and zer(mm(A,raw))
            item['witness']=serial_vector(bs,v)
            item['native_PKxi_G_Kxi_v']=serial_vector(bs,raw)
            item['nonzero_N_coordinate']=[i,str(value)]
            stack=[list(row)for row in V];power=[list(row)for row in V];filtration=[rk(stack)]
            for degree in range(1,8):
                power=mm(power,F);stack+=power;filtration.append(rk(stack))
                if filtration[-1]==filtration[-2]:break
            item['frozen_jet_filtration_ranks']=filtration
        return item
    nonnull=[block_test([0],[1],s)for s in range(13)]
    nulls=[block_test([0,4],[1,4],s)for s in range(12)]
    assert Q(1)/geo.d[0]+Q(16)/geo.d[4]==0
    assert all(c['Levi_leak_rank']==0 for c in nonnull)
    assert [c['transverse_degree']for c in nulls if c['Levi_leak_rank']]==[1,3,5,7,9]
    minimal=nulls[1]
    assert minimal['witness']==[[2,0,'2'],[8,27,'1']]
    assert minimal['native_PKxi_G_Kxi_v']==[[1,11,'4'],[16,26,'-4'],[1,26,'-1'],[16,11,'16']]
    assert minimal['frozen_jet_filtration_ranks']==[22,23,23]
    totals=[]
    for rest,cases in[(12,nonnull),(11,nulls)]:
        dim=sum(math.comb(rest,c['transverse_degree'])*c['imaginary_dimension']for c in cases)
        ran=sum(math.comb(rest,c['transverse_degree'])*c['time_range']for c in cases)
        ker=sum(math.comb(rest,c['transverse_degree'])*c['time_kernel']for c in cases)
        assert(dim,ran,ker)==(115584,66430,49154)
        totals.append({'remaining_axes':rest,'imaginary_dimension':dim,'time_range':ran,'time_kernel':ker})
    return {'object':'actual K95 imaginary connection symbol; dt=theta3',
        'nonnull_covector':{'axes':[0],'coefficients':[1],'cases':nonnull},
        'null_covector':{'axes':[0,4],'coefficients':[1,4],'norm':'0','cases':nulls},
        'complete_block_totals':totals,
        'minimal_witness':minimal,
        'definitions':'P=projection onto ker Kdt along im Kdt; G=Kdt inverse on range; V=P Kxi|R; C=R Kxi|R; F=G C. The reduced first-order F in the written evolution carries the opposite overall sign, irrelevant to factorization failure.',
        'factorization_conclusion':'V G C does not factor through V at the displayed null covector. Any invertible left M_N factor preserves this obstruction.',
        'scope':'No full M_N inverse, physical quotient, propagated ghost or GU verdict. Non-null covariance and variable-coefficient graph consequences require the separate written proofs.'}



"""Narrow native central-current and positive-charge controls.

Root owns execution/resource scheduling. The written proof supplies bosonic
reality closure, compact-test existence and perturbative coupled obstruction.
This finite script does not construct a coupled solution or physical quotient.
"""
from pathlib import Path
from fractions import Fraction as Q
import sys


def run_central_charge_controls(repo):
    repo=Path(repo)
    sys.path.insert(0,str(repo/'tests/program-focus'))
    import source_action_deep_geometry as geo
    from source_action_deep_algebra import add,scale
    from source_action_slice_completion_probe import column,covector,sigma,slash
    from source_action_physical_probe import mul,gamma,contraction
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        assert checks[name],name
    n=14
    # Factor out the single central i. This independently expands all four
    # actual connection vertices using a_a=i*alpha_a*Id, then compares sigma.
    def central_vertex_without_i(alpha,field,s):
        z,nu=field
        row=[]
        for a in range(n):
            row.append(add(*(scale(Q(1)/geo.d[b],mul(gamma(b),
                add(scale(alpha[b],z[a]),scale(-alpha[a],z[b]))))for b in range(n)),
                scale(alpha[a],nu)))
        scalar=add(*(scale(alpha[a]/geo.d[a],z[a])for a in range(n)),
                   *(scale(s*alpha[a]/geo.d[a],mul(gamma(a),nu))for a in range(n)))
        return row,scalar
    def F(field):
        z,nu=field;eta=add(nu,scale(-1,contraction(z,range(n))))
        return [add(z[a],scale(Q(1,2),mul(gamma(a),eta)))for a in range(n)],eta
    def R(field):
        r,t=field;v=add(t,scale(-Q(1,2),contraction(r,range(n))))
        return [add(r[a],scale(Q(1,2),mul(gamma(a),v)))for a in range(n)],v
    covectors=[('physical_dt',covector(3)),('positive_normal',covector(8)),
               ('negative_normal',covector(4))]
    mixed=[Q(0)]*n;mixed[0]=Q(2);mixed[3]=Q(1);mixed[4]=Q(-3)
    covectors.append(('mixed',mixed))
    for name,alpha in covectors:
        for j in range(15):
            field=column(j)
            current=central_vertex_without_i(alpha,field,-Q(1,2))
            check(f'{name}_full_vertex_equals_symbol_column{j}',current==sigma(alpha,field))
            zp,eta=F(field);u,v=R(current);c=slash(alpha)
            check(f'{name}_prime_FR_two_Dirac_column{j}',
                  u==[mul(c,w)for w in zp] and v==scale(-1,mul(c,eta)))
        # Omitting southeast current is detected, including actual physical dt.
        check(f'{name}_omitted_SE_rejected',
              central_vertex_without_i(alpha,column(14),Q(0))!=sigma(alpha,column(14)))
    def cmul(z,w):return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
    i=(Q(0),Q(1));mi=(Q(0),Q(-1))
    for j,z in enumerate([(Q(2),Q(3)),(Q(-5),Q(7)),(Q(0),Q(1)),(Q(4),Q(0))]):
        source=cmul(i,z)[0];charge=cmul(mi,z)[0]
        check(f'central_source_minus_phase_charge{j}',source==-charge)
    for norm_sq in map(Q,[1,2,7]):
        # Exact existing normalized graph identity integral eta A^t psi=i*n.
        z=(Q(0),norm_sq)
        source=cmul(i,z)[0];charge=cmul(mi,z)[0]
        check(f'positive_graph_source_nonzero_{norm_sq}',source==-norm_sq<0 and charge==norm_sq>0)
    # Bosonic reality proof reduces each imaginary-central variation to Re(i*r)=0.
    # These are sign/conjugation controls, not a reassembly of all Euler tensors.
    for r in map(Q,[-5,-1,0,2,9]):
        check(f'real_bosonic_trace_imaginary_variation_zero_{r}',cmul(i,(r,Q(0)))[0]==0)
    # Density is already absorbed into eta: adding rho again is detectably wrong.
    rho=Q(3);beta_At_psi=(Q(2),Q(5));eta_At_psi=(rho*beta_At_psi[0],rho*beta_At_psi[1])
    correct=cmul(i,eta_At_psi)[0]
    check('density_absorbed_once',correct==rho*cmul(i,beta_At_psi)[0])
    check('density_double_count_rejected',correct!=rho*correct)
    return {'checks':checks,'count':len(checks),'all_passed':all(checks.values()),
      'native_covectors':[name for name,_ in covectors],
      'full_field_columns':15,'spinor_rank_per_column':128,
      'native_identity':'All four current vertices: V_s(i alpha Id)=i sigma_s(alpha); s=-1/2.',
      'integrated_identity':'Source_time_center=-Q_phase=-||a||^2 on the existing normalized positive matter graph.',
      'reality_scope':'Real bosonic residual has zero imaginary-central source by written real-Clifford closure; scalar controls check phase algebra only.',
      'scope':'Coupled real-boson truncation obstruction, not negative-channel excitation, admitted propagation or physical ghost.'}



"""Exact native scalar-trace pencil control; no physical characteristic claim."""
def run_trace_pencil(root):
    from pathlib import Path
    from fractions import Fraction as Q
    from itertools import combinations
    import sys,json
    sys.path.insert(0,str(Path(root)/'tests/program-focus'))
    import source_action_deep_geometry as g
    from source_action_deep_algebra import Engine,add,scale
    from source_action_metric_symbol_probe import symbols
    class C:
     def __init__(self,a=0,b=0):
      if isinstance(a,C):self.a,self.b=a.a,a.b
      else:self.a,self.b=Q(a),Q(b)
     def __add__(x,y):
      y=C(y);return C(x.a+y.a,x.b+y.b)
     __radd__=__add__
     def __neg__(x):return C(-x.a,-x.b)
     def __sub__(x,y):return x+-C(y)
     def __rsub__(x,y):return C(y)+-x
     def __mul__(x,y):
      y=C(y);return C(x.a*y.a-x.b*y.b,x.a*y.b+x.b*y.a)
     __rmul__=__mul__
     def __truediv__(x,y):
      y=C(y);d=y.a*y.a+y.b*y.b;return C((x.a*y.a+x.b*y.b)/d,(x.b*y.a-x.a*y.b)/d)
     def __rtruediv__(x,y):return C(y)/x
     def __bool__(x):return bool(x.a or x.b)
     def __eq__(x,y):
      y=C(y);return x.a==y.a and x.b==y.b
     def __repr__(x):return str(x.a)+'+i*'+str(x.b)
     def conj(x):return C(x.a,-x.b)
     def ser(x):return [str(x.a),str(x.b)]
    I=C(0,1);E=Engine(g)

    def rankker(a):
     a=[[C(x)for x in row]for row in a];row=0;ps=[]
     for c in range(len(a[0])):
      k=next((j for j in range(row,len(a))if a[j][c]),None)
      if k is None:continue
      a[k],a[row]=a[row],a[k];q=a[row][c];a[row]=[x/q for x in a[row]]
      for j in range(len(a)):
       q=a[j][c]
       if j!=row and q:a[j]=[x-q*y for x,y in zip(a[j],a[row])]
      ps.append(c);row+=1
      if row==len(a):break
     z=[]
     for k in range(len(a[0])):
      if k in ps:continue
      v=[C()for _ in range(len(a[0]))];v[k]=C(1)
      for j,p in enumerate(ps):v[p]=-a[j][k]
      z.append(v)
     return ps,z

    def conj(x):return {k:C(v).conj()for k,v in x.items()}
    def rot(i,j,x):
     H=g.zero();H[i][j]=Q(1);H[j][i]=Q(-1)
     act=[g.h_action(H,a)for a in range(14)];sp={}
     for a in range(14):
      for b in range(a+1,14):
       q=act[b].get(a,Q(0))/(2*g.d[b])
       if q:sp[(1<<a)|(1<<b)]=q
     out={}
     for(e,c),v in x.items():
      ai=e.bit_length()-1
      # theta_ai transforms - transpose of tangent generator
      for b in range(14):
       q=-act[b].get(ai,Q(0))
       if q:
        k=(1<<b,c);out[k]=out.get(k,0)+v*q
      for cc,q in E.cliff_product(sp,{c:Q(1)},'comm').items():
       k=(e,cc);out[k]=out.get(k,0)+v*q
     return {k:v for k,v in out.items()if v}

    pos=[(0,1),(10,12),(9,11),(5,8)];zero=[2,3,4,6,7,13]
    p={0:C(1)}
    for a,b in pos:
     p=E.cliff_product(p,{1<<a:C(1),1<<b:I})
    bs=[];meta=[];piv=[]
    for mask in range(64):
     z=[zero[j]for j in range(6)if mask>>j&1]
     if (4+len(z))%4 not in(0,3):continue
     cliff=p
     for a in z:cliff=E.cliff_product(cliff,{1<<a:C(1)})
     v={}
     for a,f in[(5,C(1)),(8,I)]:
      for c,q in cliff.items():v[(1<<a,c)]=f*q
     key=min(v);v=scale(1/v[key],v)
     bs.append(v);piv.append(key);meta.append({'zeros':z,'degree':4+len(z)})
    assert len(bs)==36
    assert all(B.get(p,C(0))==int(i==j)for i,p in enumerate(piv)for j,B in enumerate(bs))
    for b in bs:
     assert rot(0,1,b)==scale(7*I,b),('weight',rot(0,1,b),scale(7*I,b))
     # If J01 has +i*m, J02+i J12 annihilates highestweight (checked scalarvector).
     assert not add(rot(0,2,b),scale(I,rot(1,2,b))),('raise',add(rot(0,2,b),scale(I,rot(1,2,b))))

    def coords(v):
     cs=[C(v.get(k,0))for k in piv]
     assert v==add(*(scale(c,b)for c,b in zip(cs,bs)if c)),('outside_spin7',len(v))
     return cs
    xi=[Q(0)]*14;xi[3]=1
    cols=[coords(symbols(E,xi,b)[0])for b in bs]
    K=[list(row)for row in zip(*cols)]
    ps,zs=rankker(K)
    N=[add(*(scale(c,b)for c,b in zip(z,bs)if c))for z in zs]
    G=[[E.pair(conj(u),v)for v in bs]for u in bs]
    GN=[[E.pair(conj(u),v)for v in N]for u in N]

    # Complete polynomial null-chain census, plus an elementary rank certificate.
    xi=[Q(0)]*14;xi[4]=1
    cols4=[coords(symbols(E,xi,b)[0])for b in bs]
    B=[list(row)for row in zip(*cols4)];A=K;n=len(A)
    def mv(M,v):return [sum((a*b for a,b in zip(row,v)),C())for row in M]
    def rankcols(cols):return len(rankker(list(map(list,zip(*cols))))[0])if cols else 0
    def pair(u,M,v):return sum((a.conj()*b for a,b in zip(u,mv(G,mv(M,v)))),C())
    ks=[]
    for degree in range(3):
     M=[]
     for rowblock in range(degree+2):
      for i in range(n):
       row=[C()for _ in range(n*(degree+1))]
       for j in range(n):
        if rowblock<=degree:row[rowblock*n+j]=A[i][j]
        if rowblock>=1:row[(rowblock-1)*n+j]+=B[i][j]
       M.append(row)
     _,ker=rankker(M);ks.append(ker)
    assert list(map(len,ks))==[6,22,38]
    c0=ks[0];selected=[];columns=list(c0)
    for chain in ks[1]:
     x0,x1=chain[:n],chain[n:]
     if rankcols(columns+[x0])>len(columns):
      selected.append((x0,x1));columns.append(x0)
    assert len(selected)==10
    W=c0+[a for a,b in selected]+[b for a,b in selected]
    assert rankcols(W)==26 and rankcols([mv(A,b)for a,b in selected])==10
    for a,b in selected:
     assert not any(mv(A,a))and not any(mv(B,b))
     assert not any(x+y for x,y in zip(mv(A,b),mv(B,a)))
    for u in W:
     for v in W:
      assert not pair(u,A,v)and not pair(u,B,v)
    nullranks=[]
    for z in (C(0,4),C(0,-4)):
     M=[[a+z*b for a,b in zip(row,other)]for row,other in zip(A,B)]
     assert len(rankker(M)[0])==20
     nullranks.append({'K4_multiplier':z.ser(),'rank':20})
    import hashlib
    def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    old=json.loads((Path(root)/'lab/process/source-action-kappa1-constraints.json').read_text())
    assert digest([[z.ser()for z in row]for row in A])==old['exact_probe']['spin7']['time_matrix_sha256']
    return {'highest_multiplicity':36,'time_rank':20,'polynomial_kernel_dimensions':[6,22,38],
            'common_kernel_dimension':6,'linear_chain_count':10,'chain_coefficient_span':26,
            'A_chain_top_image_rank':10,'both_pencil_forms_zero_on_chain_span':True,
            'null_covector_ranks':nullranks,'normal_trace_inverse_metric':str(1/g.d[4]),
            'time_matrix_sha256':digest([[z.ser()for z in row]for row in A]),
            'trace_matrix_sha256':digest([[z.ser()for z in row]for row in B]),
            'claim':'Elementary chain/cross-rank proof yields projective rank20 throughout scalar time-trace plane. Sixzero andten singularthreevariable blocks; no actual propagation speed inferred.'}



def run(root):
    return {'graph_symbols':run_graph_symbols(root),
            'central_charge':run_central_charge_controls(root),
            'scalar_trace_pencil':run_trace_pencil(root)}

if __name__=='__main__':
    import argparse,json
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2]);p.add_argument('--output',type=Path)
    args=p.parse_args();body=json.dumps(run(args.repo),indent=2)+'\n'
    if args.output:args.output.write_text(body)
    else:print(body)
