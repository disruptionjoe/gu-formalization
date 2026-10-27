from pathlib import Path
import json,argparse,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]

ID='K2144';OUT='k2144-raw-neighborhood-rank-budget.json'
DEPS=['tests/channel-swings/k2141_full_graph_raw_tangent_probe.py','tests/channel-swings/k2134_noncircle_current_transport_probe.py','lab/process/k2141-full-graph-raw-tangent.json','lab/process/k2028-all-grade-raw-common-form.json','tests/channel-swings/k2132_conserving_positive_sector_classification_probe.py']
EVIDENCE='Reused pinned K2141/K2028 rank and completeness certificates, new exact native current/commutant transfer and scalar rank-jump controls. Neighborhood and path-integrability theorems are written proofs; new single-coset raw kernel replay, no full32-bank replay or numerical radius.'
FAULTS=['raw-rank','universal-kernel','current-generator','drop-rank-jump','integrable-solution']
def compute(fault=None):
 import k2132_conserving_positive_sector_classification_probe as n
 q=n.q;mul=n.mul;add=n.add;adj=n.n.adj
 a=json.loads((ROOT/'lab/process/k2141-full-graph-raw-tangent.json').read_text());b=json.loads((ROOT/'lab/process/k2028-all-grade-raw-common-form.json').read_text())['complex_hermitian_branch']
 ranks=sum(x['rankA'] for x in a['systems']);nker=b['joint_dimension'];nt=a['target_count'];nr=a['raw_count']
 if fault=='raw-rank':ranks+=1
 if fault=='universal-kernel':nker-=1
 ck={'reused_global_rank_budget':ranks==16604 and a['obstruction_rank']==nt==1280 and nr==16620,'universal_coefficient_rank':nker==13 and b['image_rank']==4 and b['invisible_dimension']==9,'nearby_joint_jet_dimension_bound':nt+(nr-nker)-(ranks+nt)==3,'all_stored_input_digests':all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in a['inputs'].items())}
 cs,m,S,t,z,r,Q,E,Y,dY,c,sh=n.frame();P=add((1/(2*c*c),mul(Y,adj(Y))))
 gens=[q.I]+cs
 # Reconstruct all13 induced images from the stored sparse bank, not image-count assertions.
 bank=[{(i,j):s.Rational(v) for i,j,v in x['entries']} for x in b['induced_basis']]
 ck['thirteen_original_core_images']=all(B==add(*[(s.Rational(v),C) for v,C in zip(row,gens)]) for B,row in zip(bank,b['image_coordinates'])) and len(bank)==13
 if fault=='current-generator':gens[1]=add((1,gens[1]),(1,m))
 ck['native_S_current_commutants']=all(not n.n.comm(S,C) and adj(C)==C for C in gens)
 ck['native_graph_homogeneous_leakage']=all(not n.n.comm(P,C) for C in gens)
 ck['native_graph_current_transfer']=all(not mul(P,mul(add((s.I,mul(S,C)),(-s.I,mul(adj(C),S))),P)) for C in gens)
 z0=s.symbols('z',real=True);F=s.Matrix([[z0]]);T=s.ones(1,1)
 if fault=='drop-rank-jump':F=s.zeros(1)
 dim=lambda z:1+F.subs(z0,z).rank()-F.subs(z0,z).row_join(T).rank()
 ck['rank_jump_countercontrol']=dim(0)==0 and dim(1)==1
 x=s.symbols('x',positive=True);f=s.exp(x);coef=-1
 ck['bounded_nonconstant_punctured_solution']=s.simplify(f*coef+s.diff(f,x))==0
 f=x*x;coef=-2/x;ck['nonintegrable_escape_solution']=s.simplify(f*coef+s.diff(f,x))==0 and s.limit(s.integrate(-coef,(x,s.symbols('a',positive=True),1)),s.symbols('a',positive=True),0,dir='+')==s.oo
 coef=1/s.sqrt(x);sol=s.exp(-2*s.sqrt(x)) if fault!='integrable-solution' else s.exp(-s.sqrt(x))
 ck['unbounded_integrable_flow']=s.simplify(s.diff(sol,x)+coef*sol)==0 and s.integrate(coef,(x,0,1))==2
 rec=json.loads((ROOT/'lab/process/k2028-all-grade-raw-common-form.json').read_text());universal_counts={}
 for branch in [rec,rec['complex_hermitian_branch']]:
  for group in branch['groups']:
   coset=min(group['flip']^h for h in [0,1,62,63]);universal_counts[coset]=universal_counts.get(coset,0)+group['kernel']['rows']
 excess={row['coset']:row['raw_columns']-row['rankA']-universal_counts.get(row['coset'],0) for row in a['systems']}
 ck['all_extra_dimensions_localized']={k:v for k,v in excess.items() if v}=={64:3} and sum(universal_counts.values())==13
 Fz=s.Matrix([[-z0,1]])
 ck['moving_kernel_countercontrol']=Fz.rank()==1 and Fz.subs(z0,0).col_join(Fz.subs(z0,1)).rank()==2 and Fz*s.Matrix([1,z0])==s.zeros(1,1)

 return {k:bool(v) for k,v in ck.items()}

def localized_kernel():
    from fractions import Fraction as F
    from math import gcd
    from flint import fmpq_mat,nmod_mat
    import k2141_full_graph_raw_tangent_probe as b
    rec=json.loads((ROOT/'lab/process/k2028-all-grade-raw-common-form.json').read_text())
    labels=[(im,g['flip'],mask,y) for im,br in [(False,rec),(True,rec['complex_hermitian_branch'])] for g in br['groups'] if g['flip'] in [64,65,126,127] for mask,y in g['labels']]
    assert len(labels)==556
    # Original gamma-contraction check on real and imaginary representatives.
    direct_checks=sum(b.direct_original_check(next(v for v in labels if v[0]==im)) for im in [False,True])
    cols=[b.column(*v) for v in labels];rows=sorted(set().union(*(set(c) for c in cols)))
    unique={}
    for row in rows:
     vals=[c.get(row,0) for c in cols];gg=0
     for v in vals:gg=gcd(gg,v)
     if gg:
      if next(v for v in vals if v)<0:gg=-gg
      unique[tuple(v//gg for v in vals)]=None
    eq=list(unique);A=fmpq_mat(eq);rr,rank=A.rref();assert rank==nmod_mat(eq,101).rank()==549
    piv=[next(j for j in range(556) if rr[i,j]) for i in range(rank)];free=[j for j in range(556) if j not in piv];ker=[]
    for j in free:
     v=[F(0)]*556;v[j]=F(1)
     for i,k in enumerate(piv):v[k]=F(str(-rr[i,j]))
     ker.append(v)
    assert len(ker)==7
    def mat(vs):return fmpq_mat([[str(x) for x in v] for v in vs])
    assert A*mat(ker).transpose()==fmpq_mat(len(eq),7)
    universal=[];offset=0
    for im,br in [(False,rec),(True,rec['complex_hermitian_branch'])]:
     for g in br['groups']:
      if g['flip'] not in [64,65,126,127]:continue
      kk=g['kernel']
      for i in range(kk['rows']):
       v=[F(0)]*556
       for ii,j,val in kk['entries']:
        if ii==i:v[offset+j]=F(val)
       universal.append(v)
      offset+=len(g['labels'])
    assert len(universal)==4 and mat(universal).rank()==4 and A*mat(universal).transpose()==fmpq_mat(len(eq),4)
    basis=universal[:];extra=[]
    for v in ker:
     if mat(basis+[v]).rank()>len(basis):basis.append(v);extra.append(v)
    assert len(extra)==3
    q=b.q;n=b.n;mul=b.b.nf.mul;add=b.b.nf.add;adj=n.adj
    cs,m,S,t,z,r,Q,E,Y,_,c,sh=b.b.nf.frame(c=F(5,3),sh=F(4,3));P1=add((1/(2*c*c),mul(Y,adj(Y))))
    P0=b.b.p
    extra_maps=[];allrows=[]
    for v in extra:
     outs=[{} for _ in range(14)]
     for coeff,lab in zip(v,labels):
      if not coeff:continue
      im,ff,mask,y=lab
      for a,(flip,vals) in enumerate(b.outputs(mask,y,im)):
       co=coeff*(s.I if im else 1)/176
       outs[a]=add((1,outs[a]),(co,{(i,i^flip):int(val) for i,val in enumerate(vals) if val}))
     M=outs[0];An=mul(b.b.Fi,mul(M,b.b.J[14]))
     residual=[mul(add((1,outs[a]),(-1,mul(b.b.DJ[a],M))),b.b.J[14]) for a in range(14)]
     assert all(not mul(x,P0) for x in residual)
     leak0=mul(add((1,q.I),(-1,P0)),mul(An,P0));cur0=mul(P0,mul(add((1,mul(S,An)),(1,mul(adj(An),S))),P0))
     assert not leak0 and not cur0
     res1=[mul(x,P1) for x in residual]
     leak1=mul(add((1,q.I),(-1,P1)),mul(An,P1));cur1=mul(P1,mul(add((1,mul(S,An)),(1,mul(adj(An),S))),P1))
     vals={}
     for block,x in enumerate(res1+[leak1,cur1]):
      for (i,j),val in x.items():
       for imag,w in enumerate([s.re(val),s.im(val)]):
        if w:vals[(block,imag,i,j)]=str(w)
     allrows.append(vals)
     extra_maps.append({'coefficients':{str(j):str(x) for j,x in enumerate(v) if x},'core_action_entries':[[i,j,str(x)] for (i,j),x in sorted(An.items())],'full_upper_nonzero_blocks':[j for j,x in enumerate(residual) if x],'noncircle_nonzero_blocks':[j for j,x in enumerate(res1) if x],'noncircle_leakage_nonzero':bool(leak1),'noncircle_current_nonzero':bool(cur1)})
    keys=sorted(set().union(*(set(v) for v in allrows)));rank1=fmpq_mat([[v.get(k,'0') for v in allrows] for k in keys]).rank()
    out={'raw_columns':556,'raw_rows':len(eq),'raw_rank':rank,'kernel_dimension':7,'universal_dimension':4,'extra_dimension':3,'noncircle_restricted_extra_residual_rank':rank1,'raw_equations_sha256':hashlib.sha256(json.dumps(eq,separators=(',',':')).encode()).hexdigest(),'labels':labels,'raw_kernel':[{str(j):str(x) for j,x in enumerate(v) if x} for v in ker],'extra_maps':extra_maps}

    assert rank1==3 and direct_checks==8, ("clean localized baseline failed",rank1,direct_checks)
    # Two genuine altered coefficient faults, following the clean kernel/transport computation.
    mut=list(ker[0]);mut[piv[0]]+=1
    bad_kernel=A*mat([mut]).transpose()!=fmpq_mat(len(eq),1)
    mutrows=allrows[:];mutrows[0]={}
    bad_extra=fmpq_mat([[v.get(k,'0') for v in mutrows] for k in keys]).rank()!=3
    assert bad_kernel and bad_extra
    out['direct_original_contraction_checks']=direct_checks
    out['exact_checks']={'localized_raw_rank':rank==549,'raw_right_kernel':len(ker)==7,'universal_subspace':len(universal)==4,'quotient_extras':len(extra)==3,'noncircle_fixed_extra_exclusion':rank1==3,'original_contraction_controls':direct_checks==8}
    out['fault_failures']={'corrupt_raw_kernel_coefficient':['raw_right_kernel'],'delete_extra_coefficient_direction':['noncircle_fixed_extra_exclusion']}
    return out

def main():
 ck=compute();assert all(ck.values()),ck
 kr=localized_kernel();ck.update(kr['exact_checks']);assert all(ck.values()),ck
 failures={}
 for f in FAULTS:
  failures[f]=[k for k,v in compute(f).items() if not v]
  assert failures[f],('FAULT UNDETECTED',f)
 failures.update(kr['fault_failures'])
 report={'localized_kernel':kr,'result_id':ID,'status':'conditional_exact_controls','exact_checks':ck,'fault_failures':failures,'universal_evidence':EVIDENCE,'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependency_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in DEPS}}
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();out=ROOT/'lab/process'/OUT
 if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(out.read_text())==report,'stored evidence differs'
 print(json.dumps({'result':ID,'checks':len(ck),'faults':len(failures),'failures':failures,'pass':True}))
if __name__=='__main__':main()
