"""Targeted certificate reuse: mixed-negative form leg of existing kappa1 witnesses.

No native operator assembly or inverse recomputation. Reconstructs only the
negative-form projection of the already-certified highest spin6 kernel basis
from its published exact change-of-basis matrices. Uses one certified 32x32
inverse column at each root. Standard library; no native writes.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse, hashlib, json

class C:
    def __init__(self,a=0,b=0):
        if isinstance(a,C): self.a,self.b=a.a,a.b
        else: self.a,self.b=Q(a),Q(b)
    def __add__(x,y):
        y=C(y);return C(x.a+y.a,x.b+y.b)
    __radd__=__add__
    def __neg__(x):return C(-x.a,-x.b)
    def __sub__(x,y):return x+-C(y)
    def __mul__(x,y):
        y=C(y);return C(x.a*y.a-x.b*y.b,x.a*y.b+x.b*y.a)
    __rmul__=__mul__
    def __bool__(x):return bool(x.a or x.b)
    def __eq__(x,y):
        y=C(y);return x.a==y.a and x.b==y.b
    def ser(x):return [str(x.a),str(x.b)]
    def norm(x):return abs(x.a)+abs(x.b)

def addterm(out,key,v):
    z=out.get(key,C())+v
    if z:out[key]=z
    elif key in out:del out[key]

def cwedge(a,b):
    out={}
    for c,x in a.items():
        for d,y in b.items():
            if c&d:continue
            sign=(-1)**sum((d&((1<<i)-1)).bit_count()for i in range(14)if c>>i&1)
            addterm(out,c|d,sign*x*y)
    return out

def run(root):
    root=Path(root)
    oldpath=root/'lab/process/source-action-kappa1-constraints.json'
    redpath=root/'lab/process/source-action-reduced-evolution.json'
    old=json.loads(oldpath.read_text());red=json.loads(redpath.read_text())
    certified=old['exact_probe']['spin6']
    high=certified['highest6_in_weight6'];ker=certified['time_kernel_in_highest6']
    assert len(high)==264 and len(ker)==128
    I=C(0,1)
    pairs=[(0,1),(10,12),(9,11),(5,8)];zeros=[2,3,4,6,7,13]
    positives=[{1<<a:C(1),1<<b:I}for a,b in pairs]
    cl5=[]
    for mask in range(64):
        vs=positives+[{1<<zeros[j]:C(1)}for j in range(6)if mask>>j&1]
        if len(vs)%4 not in(0,3):continue
        p={0:C(1)}
        for v in vs:p=cwedge(p,v)
        cl5.append(p)
    assert len(cl5)==36
    # Published weight6 order: 192*(ext pos3),36*(pos0),36*(pos1),36*(pos2).
    # Only pos1=(theta10+i theta12) has negative form legs.
    weight6_projection={228+j:{(e,c):x*y for e,x in positives[1].items()
                                          for c,y in p.items()}
                        for j,p in enumerate(cl5)}
    Nnegative=[]
    for column in ker:
        out={}
        for j,a in column.items():
            for k,b in high[int(j)].items():
                if int(k) not in weight6_projection:continue
                for ec,z in weight6_projection[int(k)].items():
                    addterm(out,ec,C(*a)*C(*b)*z)
        Nnegative.append(out)
    assert any(Nnegative)
    rows=[]
    sources={x['basis_index']:x for x in red['exact_probe']['source_receivers']}
    for ri,index in [(0,12),(1,5)]:
        source=sources[index]
        assert not source['b7_lowered']
        assert len(source['b6'])==1
        col,b=source['b6'][0];b=C(*b)
        block=next(x for x in old['spin6_inverse_candidates'][ri]['blocks']if col in x['indices'])
        assert block['status']=='exact_rootball_invertibility_certified'
        ids=block['indices'];j=ids.index(col)
        R=block['rational_inverse']
        c=[-C(*row[j])*b for row in R]
        eta=Q(block['neumann_bound']);assert 0<=eta<1
        err=eta/(1-eta)*max(x.norm()for x in c)
        center={};radius={}
        for i,z in zip(ids,c):
            for ec,a in Nnegative[i].items():
                addterm(center,ec,a*z)
                radius[ec]=radius.get(ec,Q(0))+a.norm()*err
        certificates=[]
        for ec,z in sorted(center.items()):
            er=radius[ec]
            for name,value in [('real',z.a),('imag',z.b)]:
                if abs(value)>er:
                    certificates.append({'exterior_mask':ec[0],'clifford_mask':ec[1],
                        'component':name,'center':str(value),'error':str(er),
                        'lower':str(value-er),'upper':str(value+er),
                        'approx_center':float(value),'approx_error':float(er)})
        # A valid exact nonzero certificate, not a numerical rank/sign guess.
        rows.append({'root':ri,'range_basis_index':index,'source_N6_index':col,
            'active_inverse_block_dimension':len(ids),
            'mixed_negative_projection':'certified_nonzero' if certificates else 'undetermined_by_reused_bounds',
            'certified_component_count':len(certificates),
            'first_receivers':certificates[:4]})
    return {'scope':'Principal algebraically constrained auxiliary n at certification points; no physical quotient or propagation claim',
            'trace_form_leg':'zero by SO3 spin bound, not by a numerical tolerance',
            'range_all_negative_form_legs':'zero by spin7 bound',
            'auxiliary_mixed_negative_form_legs':rows,
            'method':'Exact published basis transformations plus certified Neumann inverse-column error; no new inverse',
            'inputs_sha256':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest()for p in [oldpath,redpath]}}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--output',type=Path)
    args=p.parse_args();result=run(args.repo)
    text=json.dumps(result,indent=2)
    if args.output:args.output.write_text(text+'\n')
    else:print(text)
