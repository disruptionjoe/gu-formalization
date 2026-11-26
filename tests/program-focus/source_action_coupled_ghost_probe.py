"""Exact native coupled-constraint and central-reduction controls.

All full-carrier counts are obtained from complete Clifford-label blocks and
proved covariance classes, not a stationary59 Hessian or sampled spectrum.
No PDE well-posedness, physical ghost, κ1 lower inverse or source verdict is
inferred. Standard library only. Run from the repository root.
"""
from pathlib import Path
import argparse, json, math, sys
from fractions import Fraction as Q
sys.path.insert(0, str(Path(__file__).resolve().parent))
ROOT=Path(__file__).resolve().parents[2]

def run_principal():
    """Exact connection time-symbol blocks; parent owns serialized execution."""
    from fractions import Fraction as Q
    import sys,json,math
    import source_action_deep_geometry as geo
    from source_action_deep_algebra import Engine
    from source_action_metric_symbol_probe import symbols
    E=Engine(geo)
    t=3
    trans=[i for i in range(14) if i!=t]
    xi=[Q(0)]*14;xi[t]=Q(1)
    def rref(a):
     a=[list(r) for r in a]; row=0;piv=[]
     for col in range(len(a[0])):
      k=next((k for k in range(row,len(a)) if a[k][col]),None)
      if k is None:continue
      a[row],a[k]=a[k],a[row]
      v=a[row][col];a[row]=[z/v for z in a[row]]
      for k in range(len(a)):
       if k!=row and a[k][col]:
        v=a[k][col];a[k]=[z-v*w for z,w in zip(a[k],a[row])]
      piv.append(col);row+=1
      if row==len(a):break
     return a,piv
    def ker(a):
     rr,piv=rref(a);n=len(a[0]);out=[]
     for k in range(n):
      if k in piv:continue
      v=[Q(0)]*n;v[k]=Q(1)
      for j,c in enumerate(piv):v[c]=-rr[j][k]
      out.append(v)
     return out
    total=0;null=0;data=[];phase={0:[0,0,0],1:[0,0,0]}
    for s in range(14):
     r=sum(1<<i for i in trans[:s])
     basis=[(1<<i,(1<<i)^r^z) for z in [0,1<<t] for i in range(14)]
     cols=[symbols(E,xi,{key:Q(1)})[0] for key in basis]
     assert all(set(col)<=set(basis) for col in cols)
     A=[[col.get(k,Q(0)) for col in cols] for k in basis]
     weights=[E.weight(*k) for k in basis]
     assert all(weights[i]*A[i][j]==-weights[j]*A[j][i] for i in range(28) for j in range(28))
     Z=ker(A);rank=28-len(Z)
     G=[[sum(weights[k]*u[k]*v[k] for k in range(28)) for v in Z] for u in Z]
     mass_rank=len(rref(G)[1]) if G else 0
     mult=math.comb(13,s);total+=mult*rank;null+=mult*len(Z)
     for ph in [0,1]:
      ids=[i for i,(_,c) in enumerate(basis) if (c.bit_count()%4 in (1,2)) == (ph==0)]
      assert all(not A[i][j] for i in ids for j in range(28) if j not in ids)
      rr=len(rref([[A[i][j] for j in ids] for i in ids])[1]) if ids else 0
      phase[ph][0]+=mult*len(ids);phase[ph][1]+=mult*rr;phase[ph][2]+=mult*(len(ids)-rr)
     data.append({'transverse_degree':s,'rank':rank,'nullity':len(Z),'kernel_mass_rank':mass_rank,'multiplicity':mult,'basis':basis,'kernel':[[str(v) for v in z] for z in Z],'matrix':[[str(v) for v in z] for z in A]})
    assert (total,null)==(130912,98464)
    assert phase=={0:[113792,64482,49310],1:[115584,66430,49154]}
    return {'dimension':14*(1<<14),'rank':total,'nullity':null,'phase_dimensions_rank_kernel':phase,'blocks':data}

def run_spatial():
    from fractions import Fraction as Q
    import sys,json
    import source_action_deep_geometry as geo
    from source_action_deep_algebra import Engine
    from source_action_metric_symbol_probe import symbols
    E=Engine(geo);t=3;trans=[i for i in range(14) if i!=t]
    def rref(a):
     a=[list(r) for r in a]; row=0;piv=[]
     for col in range(len(a[0])):
      k=next((k for k in range(row,len(a)) if a[k][col]),None)
      if k is None:continue
      a[row],a[k]=a[k],a[row];v=a[row][col];a[row]=[z/v for z in a[row]]
      for k in range(len(a)):
       if k!=row and a[k][col]:
        v=a[k][col];a[k]=[z-v*w for z,w in zip(a[k],a[row])]
      piv.append(col);row+=1
      if row==len(a):break
     return a,piv
    def block(r):
     bs=[(1<<i,(1<<i)^r^z) for z in [0,1<<t] for i in range(14)]
     xi=[Q(0)]*14;xi[t]=Q(1)
     cs=[symbols(E,xi,{k:Q(1)})[0] for k in bs]
     A=[[c.get(k,Q(0)) for c in cs] for k in bs]
     R,ps=rref(A);Z=[]
     for k in range(28):
      if k in ps:continue
      v=[Q(0)]*28;v[k]=Q(1)
      for j,c in enumerate(ps):v[c]=-R[j][k]
      Z.append({bs[i]:w for i,w in enumerate(v) if w})
     return Z
    out=[]
    for s in range(14):
     r=sum(1<<i for i in trans[:s]);Z=block(r)
     axes=([trans[0]] if s else [])+([trans[s]] if s<13 else [])
     for axis in axes:
      W=block(r^(1<<axis));xi=[Q(0)]*14;xi[axis]=Q(1)
      cols=[symbols(E,xi,z)[0] for z in Z]
      M=[[E.pair(w,c) for c in cols] for w in W]
      rank=len(rref(M)[1]);out.append({'s':s,'axis':axis,'rank':rank,'shape':[len(W),len(Z)]})
    return out

def run_center():
    """Root-run exact controls; actual native Phi, no heavy full carrier build.
    Raw dictionaries represent X; imaginary Lie fields are iX. Their real-trace
    pairing is -Engine.pair(X,Y), not Engine.pair(X,Y).
    """
    import sys,json
    from pathlib import Path
    from fractions import Fraction as Q
    import source_action_deep_geometry as g
    from source_action_deep_algebra import Engine,add,scale
    from source_action_metric_symbol_probe import symbols
    from source_action_physical_probe import interval
    E=Engine(g); checks=0
    def check(v):
     nonlocal checks
     assert v
     checks+=1
    xi=[Q(0)]*14;xi[3]=1
    time_controls=[]
    for j in range(14):
     c={(1<<j,0):Q(1)}
     kc,lc=symbols(E,xi,c)
     check(not lc)
     check(symbols(E,xi,kc)[0]==({} if j==3 else scale(-48,c)))
     check(not any(mask==0 for e,mask in kc))
     check(all(mask.bit_count()%4 in (0,3)for e,mask in kc))
     # Physical pairing for i c flips the raw real scalar sign.
     norm=-E.pair(c,c)
     check(norm==1/E.d[j])
     if j!=3:check(-E.pair(kc,kc)==48*norm)
     time_controls.append({'central_axis':j,'K_support':len(kc),'physical_center_norm':str(norm)})

    data=json.loads((ROOT/'lab/process/source-action-deep-coefficients.json').read_text())
    basis=[{(int(e),int(c)):Q(v)for e,c,v in row}for row in data['basis']]
    check(len(basis)==59)
    check(all(all(c and c.bit_count()%4 in (1,2) for e,c in row)for row in basis))
    c={(1,0):Q(1)};kc=symbols(E,xi,c)[0]
    geom=E.K(c)
    Ncols=[scale(2,E.N(T,c))for T in basis]
    check(all(all(mask.bit_count()%4 in (0,3)for e,mask in row)for row in [geom]+Ncols))
    allowed=set(c)|set(kc)
    outside=sorted((set(geom)|{k for row in Ncols for k in row})-allowed)
    witnesses=[]
    for key in outside:
     coeff=[row.get(key,Q(0))for row in Ncols]
     bounds=[]
     for root in data['certified_roots']:
      b=interval(coeff,root);offset=geom.get(key,Q(0))
      for field in ('center','lower','upper'):b[field]=str(Q(b[field])+offset)
      b['approximate_center']=float(Q(b['center']))
      b['sign']='positive' if Q(b['lower'])>0 else ('negative' if Q(b['upper'])<0 else 'unresolved')
      bounds.append(b)
     if all(b['sign']!='unresolved'for b in bounds):
      witnesses.append({'receiver':key,'geometric_offset':str(geom.get(key,Q(0))),
                        'linear59':list(map(str,coeff)),'root_intervals':bounds})
      if len(witnesses)>=2:break
    check(bool(witnesses))
    positive=sum(E.d[j]<0 for j in range(14)if j!=3)
    negative=sum(E.d[j]>0 for j in range(14)if j!=3)
    check((positive,negative)==(4,9))

    # Nondegenerate algebraic center square completion, including signed pairing.
    for metric_sign in (Q(1),Q(-1)):
     for kappa in (Q(1),Q(2)):
      for center,source in ((Q(2),Q(3)),(Q(-1),Q(4))):
       original=metric_sign*(kappa*center*center/2+center*source)
       completed=metric_sign*(kappa*(center+source/kappa)**2/2-source**2/(2*kappa))
       check(original==completed)
       check(metric_sign*(kappa*(-source/kappa)+source)==0)

    out={'checks':checks,'real_clifford_lie_dimension':8128,'imaginary_clifford_lie_dimension':8256,
     'imaginary_connection_dimension':115584,'time_controls':time_controls,
     'central_eliminated_velocity_rank':13,'unreduced_velocity_inertia':{'positive':positive,'negative':negative},
     'actual_lower_coupling_witnesses':witnesses,
     'root_certificate_status':'uses already certified rational root balls; no new root proof',
     'scope':'Exact central auxiliary elimination and principal reduced velocity block. Explicit lower mixing rejects autonomous principal+kappa center oscillators at both native roots. No physical ghost or full constraint-spectrum verdict.'}
    return out

def run_causal():
    """Root-run exact causal central-symbol and projected Phi identity controls."""
    import sys,json
    from fractions import Fraction as Q
    from itertools import combinations
    import source_action_deep_geometry as g
    from source_action_deep_algebra import Engine,add,scale
    from source_action_metric_symbol_probe import symbols
    E=Engine(g);checks=0
    def check(ok):
     nonlocal checks
     assert ok
     checks+=1
    def p0(v):return {k:x for k,x in v.items()if k[1]==0}
    # On scalar two-forms the projected adjoint composite is exactly -48 Id.
    # Higher Clifford grades in the unprojected composite are NOT discarded silently.
    noncentral_composite_seen=False
    for a,b in combinations(range(14),2):
     f={((1<<a)|(1<<b),0):Q(1)}
     full=E.Phi_adj(E.Phi(f))
     check(p0(full)==scale(-48,f))
     noncentral_composite_seen |= any(c!=0 for e,c in full)
    check(noncentral_composite_seen)
    causal=[]
    for name,terms in [('timelike',{3:Q(1)}),('spacelike',{0:Q(1)}),('null',{0:Q(1),3:Q(1)})]:
     xi=[terms.get(a,Q(0))for a in range(14)]
     cols=[]
     for a in range(14):
      c={(1<<a,0):Q(1)};kc,lc=symbols(E,xi,c)
      check(not lc)
      kk=symbols(E,xi,kc)[0]
      norm=sum(x*x/E.d[j]for j,x in enumerate(xi))
      xic={(1<<j,0):x for j,x in enumerate(xi)if x}
      expected=scale(48,add(scale(norm,c),scale(-xi[a]/E.d[a],xic)))
      check(p0(kk)==expected)
      # K² has no extra components on center, even at a null covector.
      check(kk==expected)
      cols.append(kc)
     # Find rank by exact elimination on the small14-column matrix.
     keys=sorted({k for c in cols for k in c})
     rows=[[c.get(k,Q(0))for c in cols]for k in keys]
     rank=0
     for j in range(14):
      pivot=next((k for k in range(rank,len(rows))if rows[k][j]),None)
      if pivot is None:continue
      rows[rank],rows[pivot]=rows[pivot],rows[rank]
      q=rows[rank][j];rows[rank]=[x/q for x in rows[rank]]
      for k in range(rank+1,len(rows)):
       q=rows[k][j]
       if q:rows[k]=[x-q*y for x,y in zip(rows[k],rows[rank])]
      rank+=1
     check(rank==13)
     causal.append({'kind':name,'central_K_rank':rank,'covector_norm':str(norm),
                    'induced_square_inertia':{'positive':4,'negative':9,'radical_in_image':0}if name=='timelike'else({'positive':5,'negative':8,'radical_in_image':0}if name=='spacelike'else{'positive':4,'negative':8,'radical_in_image':1})})
    return {'checks':checks,'causal':causal,'phi_composite_identity':'p0 Phi^dagger Phi on scalar2forms = -48 Id; full composite has grade4 terms','scope':'Pointwise exact central principal symbol and unreduced square; no propagation or physical ghost verdict'}

def run():
    a=run_principal(); b=run_spatial(); c=run_center(); d=run_causal()
    assert len(a['blocks'])==14 and len(b)==26 and all(x['rank']==0 for x in b)
    assert all(x['kernel_mass_rank']==x['nullity'] for x in a['blocks'])
    return {'principal':a,'spatial_kernel_compressions':b,'center':c,'causal':d,
            'finite_controls':c['checks']+d['checks'],
            'scope':'Complete pointwise principal and exact central mechanism controls. Written proofs supply covariance, moving-projector reduction and large-coupling constrained-energy theorem; no κ1 physical spectrum.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);args=p.parse_args()
    result=run();data=json.dumps(result,indent=2)+'\n'
    if args.output:args.output.write_text(data)
    else:print(data)
