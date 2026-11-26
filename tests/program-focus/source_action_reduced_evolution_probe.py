"""Exact reduced-evolution and derivative-energy controls for the held candidate.

Reconstructs the complete spin6/7 native bases. Reuses explicitly hash-bound
prior inverse certificates, computes the whole source needed for three new
witnesses, and propagates rational errors. No full49154 inverse or physical
state/domain is asserted. Standard library only.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse,json,hashlib

def build_context(root):
    """Complete highest-spin6 counts/readout and spin7 direct-observation controls.
    Pure finite native algebra; no PDE propagation or physical particle count.
    Standard library only; root is the GU repository root.
    """
    from pathlib import Path
    from fractions import Fraction as Q
    from types import SimpleNamespace
    import sys
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

    h=SimpleNamespace(C=C,I=I,E=E,pos=pos,zero=zero,bs=bs,N=N,meta=meta,rot=rot,add=add,scale=scale,symbols=symbols,conj=conj)
    spin7_obs=lambda v:{k:x for k,x in v.items()if k[0]in(1,2,4,8)}
    assert all(not spin7_obs(v)for v in bs)
    spin7_witnesses=[]
    for i,v in enumerate(bs):
     for a in range(14):
      xi=[Q(0)]*14;xi[a]=Q(1)
      image=spin7_obs(symbols(E,xi,v)[0])
      if image:
       spin7_witnesses.append({'basis':i,'axis':a,'receivers':[[e,c,C(x).ser()]for(e,c),x in sorted(image.items())]})
       break
    assert len(spin7_witnesses)==36
    def cwedge(a,b):
     out={}
     for c,x in a.items():
      for d,y in b.items():
       if c&d:continue
       k=c|d;out[k]=out.get(k,0)+E.sign(c,d)*x*y
     return {k:v for k,v in out.items()if v}
    def cmulti(vs):
     out={0:C(1)}
     for v in vs:out=cwedge(out,v)
     return out
    pos=[{1<<a:C(1),1<<b:I}for a,b in h.pos]
    neg=[{a:x.conj()for a,x in v.items()}for v in pos]
    zero=[{1<<a:C(1)}for a in h.zero]
    cl4=[]
    for omitted in range(3):
     for m in range(64):
      vs=[pos[j]for j in range(4)if j!=omitted]+[zero[j]for j in range(6)if m>>j&1]
      if len(vs)%4 in(0,3):cl4.append(cmulti(vs))
    for included in range(3):
     for m in range(64):
      vs=pos+[neg[included]]+[zero[j]for j in range(6)if m>>j&1]
      if len(vs)%4 in(0,3):cl4.append(cmulti(vs))
    assert len(cl4)==192
    cl5=[]
    for m in range(64):
     vs=pos+[zero[j]for j in range(6)if m>>j&1]
     if len(vs)%4 in(0,3):cl5.append(cmulti(vs))
    assert len(cl5)==36
    bs=[]
    for ext,cliffs in[(pos[3],cl4),(pos[0],cl5),(pos[1],cl5),(pos[2],cl5)]:
     for c in cliffs:
      v={(e,k):x*y for e,x in ext.items()for k,y in c.items()}
      bs.append(v)
    assert len(bs)==300

    def sparse_kernel(cols,progress=False):
     piv={};basis=[];kernels=[]
     for i,v in enumerate(cols):
      v=dict(v);cs={i:C(1)}
      while v:
       p=min(v)
       if p not in piv:
        q=v[p];v={k:x/q for k,x in v.items()};cs={k:x/q for k,x in cs.items()}
        piv[p]=len(basis);basis.append((v,cs));break
       b,bc=basis[piv[p]];q=v[p]
       for k,x in b.items():
        y=v.get(k,C(0))-q*x
        if y:v[k]=y
        elif k in v:del v[k]
       for k,x in bc.items():
        y=cs.get(k,C(0))-q*x
        if y:cs[k]=y
        elif k in cs:del cs[k]
      if not v:kernels.append(cs)
      # exact sparse elimination; no progress side effect
     return len(basis),kernels

    assert all(h.rot(0,1,b)==h.scale(6*I,b)for b in bs)

    rank,z=sparse_kernel(bs);assert rank==300

    xi=[Q(0)]*14;xi[3]=1
    cols=[]
    for i,b in enumerate(bs):
     cols.append(h.symbols(E,xi,b)[0])

    rank,z=sparse_kernel(cols)
    # Raising maps weight6 toweight7. Its kernel is the264 highestspin6 module.
    raised=[h.add(h.rot(0,2,b),h.scale(I,h.rot(1,2,b)))for b in bs]
    rraise,zraise=sparse_kernel(raised);assert rraise==36 and len(zraise)==264
    high6=[h.add(*(h.scale(c,bs[i])for i,c in z.items()))for z in zraise]
    assert all(not h.add(h.rot(0,2,b),h.scale(I,h.rot(1,2,b)))for b in high6)
    # Direct literal connection readout on completehighestspin6 basis.
    obs=lambda v:{k:x for k,x in v.items()if k[0]in(1,2,4,8)}
    qrank,qker=sparse_kernel([obs(b)for b in high6])
    # Timekernel withinhighestspin6: Ktime(high6) fullreceiver sparse eliminate.
    kh=[h.symbols(E,xi,b)[0]for b in high6]
    rhigh,zhigh=sparse_kernel(kh)
    Nh=[h.add(*(h.scale(c,high6[i])for i,c in z.items()))for z in zhigh]
    qNrank,qNker=sparse_kernel([obs(b)for b in Nh])
    assert len(zhigh)==len(z)-16
    result={'weight6_dimension':300,'weight6_time_rank':rank,'weight6_time_kernel':len(z),'spin7_weight6_kernel_subtracted':16,'spin6_multiplicity':264,'spin6_time_rank':rhigh,'spin6_time_kernel_multiplicity':len(zhigh),'spin6_real_carrier_dim':264*13,'spin6_real_kernel_dim':len(zhigh)*13,'literal_highestweight_readout_rank':qrank,'literal_readout_real_rank':qrank*13,'literal_kernel_highestweight_readout_rank':qNrank,'literal_kernel_readout_real_rank':qNrank*13,'certificate':'exact Gaussian-rational receiver elimination'}

    return {'C':C,'E':E,'h':h,'N6':Nh,'spin6_counts':result,
            'highest6_in_weight6':[{str(i):c.ser()for i,c in z.items()}for z in zraise],
            'time_kernel_in_highest6':[{str(i):c.ser()for i,c in z.items()}for z in zhigh],
            'rankker':rankker,'G7':GN}

def run(root):
    root=Path(root)
    ctx=build_context(root)
    C,E,h,N6=ctx['C'],ctx['E'],ctx['h'],ctx['N6']
    old=json.loads((root/'lab/process/source-action-kappa1-constraints.json').read_text())
    new=json.loads((root/'lab/process/source-action-reduced-evolution.json').read_text())
    def digest(x):
        return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    def norm(x):
        x=C(x);return abs(x.a)+abs(x.b)
    def serial(v):return [[e,c,C(z).ser()]for(e,c),z in sorted(v.items())]
    prior6=old['exact_probe']['spin6']
    assert ctx['highest6_in_weight6']==prior6['highest6_in_weight6']
    assert ctx['time_kernel_in_highest6']==prior6['time_kernel_in_highest6']
    gram6=[[C(E.pair(h.conj(u),v)).ser()for v in N6]for u in N6]
    assert digest(gram6)==prior6['constraint_inverse']['gram_sha256']
    assert digest([[C(x).ser()for x in row]for row in ctx['G7']])==old['exact_probe']['spin7']['kernel_gram_sha256']
    p6=old['spin6_inverse_candidates'];p7=new['spin7_inverse_candidates']
    assert len(p6)==len(p7)==2
    for ri,(six,seven)in enumerate(zip(p6,p7)):
        assert six['root']==seven['root']==ri
        assert len(six['blocks'])==4
        indices=[]
        for witness,proved in zip(six['blocks'],prior6['constraint_inverse']['root_certificates'][ri]['blocks']):
            assert witness['status']==proved['status']=='exact_rootball_invertibility_certified'
            assert witness['neumann_bound']==proved['neumann_bound']
            assert digest(witness['rational_inverse'])==proved['rational_inverse_sha256']
            assert Q(witness['neumann_bound'])<1
            indices+=witness['indices']
        assert sorted(indices)==list(range(128))
        official=old['exact_probe']['spin7']['root_certificates'][ri]
        assert digest(seven['inverse'])==official['inverse_sha256']
        assert seven['neumann_bound']==official['neumann_bound']
        assert Q(seven['neumann_bound'])<1
    tau=[Q(0)]*14;tau[3]=Q(1)
    xi=[Q(0)]*14;xi[0]=Q(1)
    N7=[h.add(h.rot(0,2,n),h.scale(-h.I,h.rot(1,2,n)))for n in h.N]
    lowering_controls=0
    for i,u in enumerate(N7):
        assert not h.symbols(E,tau,u)[0]
        assert h.add(h.rot(0,2,u),h.scale(h.I,h.rot(1,2,u)))==h.scale(-14,h.N[i])
        lowering_controls+=2
        for j,v in enumerate(N7):
            assert E.pair(h.conj(u),v)==14*E.pair(h.conj(h.N[i]),h.N[j])
            lowering_controls+=1
    obs=lambda v:{k:x for k,x in v.items()if k[0]in(1,2,4,8)}
    assert all(not obs(v)for v in h.bs+N7)
    sources=[]
    for index in (5,7,12):
        v=h.symbols(E,tau,h.bs[index])[0]
        assert v and not obs(v)
        force=h.symbols(E,xi,v)[0]
        # Highestweight7 times horizontalspin1 has onlyrotation6/7;8absent.
        assert h.rot(0,1,force)==h.scale(6*h.I,force)
        raiseforce=h.add(h.rot(0,2,force),h.scale(h.I,h.rot(1,2,force)))
        assert not h.add(h.rot(0,2,raiseforce),h.scale(h.I,h.rot(1,2,raiseforce)))
        b6=[C(E.pair(h.conj(n),force))for n in N6]
        b7=[C(E.pair(h.conj(n),force))for n in N7]
        if index==7:
            assert {i:z for i,z in enumerate(b6)if z}=={18:C(-3145728),27:C(9437184),117:C(6291456)}
        sources.append({'index':index,'v':v,'force':force,'b6':b6,'b7':b7})
    def solve(source,ri):
        b6,b7=source['b6'],source['b7']
        c6=[C()for _ in N6];e6=[Q(0)for _ in N6]
        for block in p6[ri]['blocks']:
            ids=block['indices'];R=[[C(*z)for z in row]for row in block['rational_inverse']]
            c0=[-sum((a*b6[j]for a,j in zip(row,ids)),C())for row in R]
            eta=Q(block['neumann_bound']);er=eta/(1-eta)*max(map(norm,c0))
            for i,z in zip(ids,c0):c6[i]=z;e6[i]=er
        R7=[[C(*z)/14 for z in row]for row in p7[ri]['inverse']]
        c7=[-sum((a*b for a,b in zip(row,b7)),C())for row in R7]
        eta=Q(p7[ri]['neumann_bound']);e7=eta/(1-eta)*max(map(norm,c7))
        return c6,e6,c7,e7
    # Full derivative-source energy: include BOTH N6 and N7, notonlyreadoutN6.
    energy=[]
    for ri in range(2):
        entries=[]
        for source in sources:
            if source['index']==7:continue
            c6,e6,c7,e7=solve(source,ri)
            value=sum((b.conj()*c for b,c in zip(source['b6'],c6)),C())+sum((b.conj()*c for b,c in zip(source['b7'],c7)),C())
            error=sum(norm(b)*er for b,er in zip(source['b6'],e6))+sum(norm(b)*e7 for b in source['b7'])+abs(value.b)
            assert abs(value.a)>error
            sign='positive'if value.a>0 else'negative'
            entries.append({'basis_index':source['index'],'sign':sign,'center':str(value.a),'error_bound':str(error),'lower':str(value.a-error),'upper':str(value.a+error)})
        assert {x['sign']for x in entries}=={'positive','negative'}
        energy.append({'root':ri,'witnesses':entries})
    # A fixed actual B_xi witness: w=-M^-1PK_xi v, hence B_xi v=G K_xi w.
    s=next(s for s in sources if s['index']==7)
    active6=sorted({i for block in p6[0]['blocks']if any(s['b6'][j]for j in block['indices'])for i in block['indices']})
    F6={i:h.symbols(E,xi,N6[i])[0]for i in active6}
    F7={i:h.symbols(E,xi,n)[0]for i,n in enumerate(N7)}
    receiver=(32,1725);nonzero=[]
    for ri in range(2):
        c6,e6,c7,e7=solve(s,ri)
        center=sum((c6[i]*v.get(receiver,0)for i,v in F6.items()),C())+sum((c7[i]*v.get(receiver,0)for i,v in F7.items()),C())
        error=sum(norm(v.get(receiver,0))*e6[i]for i,v in F6.items())+sum(norm(v.get(receiver,0))*e7 for v in F7.values())
        assert abs(center.a)>error
        nonzero.append({'root':ri,'receiver':list(receiver),'component':'real','center':str(center.a),'error_bound':str(error),'lower':str(center.a-error),'upper':str(center.a+error)})
    # Finitealgebra/control only. Written constant-rank proof supplies nativeB²=0.
    def mul(a,b):return [[sum(x*y for x,y in zip(row,col))for col in zip(*b)]for row in a]
    a,b,m=Q(1),Q(2),Q(3)
    B=[[a*b/m,b*b/m],[-a*a/m,-a*b/m]]
    assert mul(B,B)==[[0,0],[0,0]]and any(x for row in B for x in row)
    # Ordinarywaveequation has this same topdegree feature; weightedspaces survive.
    waveB=[[Q(0),Q(0)],[Q(-1),Q(0)]]
    assert mul(waveB,waveB)==[[0,0],[0,0]]and waveB[1][0]
    # Source-inspired normal compact algebra: exact principal-module controls.
    compact_masks={ (1<<a)|(1<<b) for a in range(4,14) for b in range(a+1,14)
                    if E.d[a]*E.d[b]>0 }
    assert len(compact_masks)==21
    compact_controls=[]
    for ext,axis,receivers in [(0,3,{(2,107):Q(2),(4,109):Q(2)}),
                               (3,0,{(2,107):Q(-2),(4,109):Q(-2)}),
                               (4,0,{(2,115):Q(-1,8),(4,117):Q(-1,8)})]:
        field={(1<<ext,(1<<5)|(1<<6)):Q(1)}
        covector=[Q(0)]*14;covector[axis]=Q(1)
        image=h.symbols(E,covector,field)[0]
        assert len(image)==10 and all(c not in compact_masks for e,c in image)
        assert all(image.get(key)==value for key,value in receivers.items())
        compact_controls.append({'input_exterior_axis':ext,'derivative_axis':axis,
            'total_terms':len(image),'all_outside_compact':True,
            'exact_receivers':[[e,c,str(v)]for(e,c),v in receivers.items()]})
    return {'compact_module_controls':compact_controls,'basis_replay':'Complete native6/7bases matchpredecessor kernelcoordinates/Gramhashes',
        'lowering_controls':lowering_controls,'lowered_spin7_gram_factor':14,
        'source_receivers':[{ 'basis_index':s['index'],'range_sha256':digest(serial(s['v'])),
            'b6':[[i,z.ser()]for i,z in enumerate(s['b6'])if z],
            'b7_lowered':[[i,z.ser()]for i,z in enumerate(s['b7'])if z]}for s in sources],
        'nilpotent_principal_nonzero':nonzero,'physical_derivative_energy':energy,
        'energy_convention':'Reportedb*c equalsphysicalb(Dv,M_N^-1Dv); c=-Hraw^-1b andphysicalimaginarypairing=-raw. Commonpositivefactor1/2 omitted.',
        'prior_inverse_validation':'Hash-boundpredecessor exactcertificates reused; no claimtheirentiretrilinearassembly rerunhere.',
        'full_N_regular':'not established; conditional regular-reduction theorems stateitexplicitly',
        'scope':'No physicalpropagation, quantumghost, instability, source/classC verdict ornewdomainchoice.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2]);p.add_argument('--output',type=Path)
    args=p.parse_args();result=json.dumps(run(args.repo),indent=2)+'\n'
    if args.output:args.output.write_text(result)
    else:print(result)
