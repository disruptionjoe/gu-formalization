#!/usr/bin/env python3
"""Independent rational audit of K1820's correlated terminal certificates.

Does not import the K1820 producer. Bernstein conversion uses exact collocation
matrix inversion, rather than its power-to-unit-to-Bernstein binomial loop.
Quadrature and the previously validated necessary-root transport are inputs.
"""
import argparse
import copy
import hashlib
import json
import re
from fractions import Fraction as Q
from functools import lru_cache
from math import comb, factorial
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'lab/process/k1820-full-fisher-global-optimizer-admission.json'
OUTPUT=ROOT/'lab/process/k1820-independent-certificate-audit.json'

def add(x,y):return x[0]+y[0],x[1]+y[1]
def scale(a,x):return tuple(sorted((a*x[0],a*x[1])))
def product(x,y):
    v=[a*b for a in x for b in y];return min(v),max(v)
def enc(s):
    m=re.fullmatch(r'\[(.+) \+/- (.+)\]',s)
    if m:
        a,b=map(Q,m.groups());assert b>=0;return a-b,a+b
    return Q(s),Q(s)
def within(x,outer):return outer[0]<=x[0]<=x[1]<=outer[1]
def inside(box,hull):return within(box[:2],hull[:2]) and within(box[2:],hull[2:])

def inverse(a):
    n=len(a);rows=[list(row)+[Q(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        k=next(i for i in range(j,n) if rows[i][j]);rows[j],rows[k]=rows[k],rows[j]
        p=rows[j][j];rows[j]=[v/p for v in rows[j]]
        for i in range(n):
            if i!=j:
                p=rows[i][j];rows[i]=[v-p*w for v,w in zip(rows[i],rows[j])]
    return [row[n:] for row in rows]

@lru_cache(None)
def interpolation_inverse(n):
    nodes=[Q(i,n) for i in range(n+1)]
    return inverse([[Q(comb(n,j))*x**j*(1-x)**(n-j) for j in range(n+1)] for x in nodes])

@lru_cache(None)
def monomial_controls(n,lo,hi):
    inv=interpolation_inverse(n);nodes=[lo+(hi-lo)*Q(i,n) for i in range(n+1)]
    return [[sum((inv[b][k]*nodes[k]**p for k in range(n+1)),Q(0)) for p in range(n+1)] for b in range(n+1)]

def polynomial_bound(coeffs,box,n):
    wx=monomial_controls(n,box[0],box[1]);wy=monomial_controls(n,box[2],box[3]);out=[]
    for bx in range(n+1):
        for by in range(n+1):
            value=(Q(0),Q(0))
            for (i,j),bounds in coeffs.items():value=add(value,scale(wx[bx][i]*wy[by][j],bounds))
            out.append(value)
    return min(x[0] for x in out),max(x[1] for x in out)

def derivative_bound(packet,box,tail,terms):
    orders={i+j for i,j,w in terms};assert len(orders)==1
    d=orders.pop();assert d in (1,2);n=8-d
    anchor=list(map(Q,packet['anchor']));off=[box[0]-anchor[0],box[1]-anchor[0],box[2]-anchor[1],box[3]-anchor[1]]
    radius=[max(abs(off[0]),abs(off[1])),max(abs(off[2]),abs(off[3]))]
    coeff={};error=Q(0)
    for i in range(n+1):
        for j in range(n+1-i):
            jet=packet['hull_jet'] if i+j==n else packet['point_jet'];value=(Q(0),Q(0))
            for a,b,w in terms:
                factor=Q(w)*Q(factorial(i+a),factorial(i))*Q(factorial(j+b),factorial(j))
                value=add(value,scale(factor,tuple(map(Q,jet[f'{i+a},{j+b}']))))
            if i+j==n:error+=max(map(abs,value))*radius[0]**i*radius[1]**j
            else:coeff[i,j]=value
    keys={(1,0):'t',(0,1):'z',(2,0):'tt',(1,1):'tz',(0,2):'zz'}
    error+=sum(abs(Q(w))*Q(tail[keys[a,b]]) for a,b,w in terms)
    low,high=polynomial_bound(coeff,tuple(off),n-1)
    return low-error,high+error

def audit(data):
    cert=data['certificate'];profiles=cert['stationary_derivative_transport']['leaf_results']
    expected={x['leaf']:x for x in profiles if not x['stationary_excluded']}
    seen=set();counts={'gradient_excluded':0,'positive_hessian':0};positive=[];min_a=None;min_det=None
    packets_by_digest={p['input_digest']:p for p in cert['correlated_profile']['packets']}
    for packet in data['correlated_profile_inputs']:
        raw={k:v for k,v in packet.items() if k!='digest'}
        digest=hashlib.sha256(json.dumps(raw,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        assert digest==packet['digest'],'packet digest'
        assert packet['parameter_order']==8 and packet['observation_order']==14 and packet['cell_half_width']=='1/4'
        hull=tuple(map(Q,packet['hull']));a,b=map(Q,packet['anchor'])
        assert inside((a,a,b,b),hull),'anchor outside hull'
        assert 0<hull[0]<=hull[1]<1 and 0<hull[2]<=hull[3]<1 and 2*hull[0]**2>Q(1,1024)
        keys={f'{i},{j}' for i in range(9) for j in range(9-i)}
        for name in ('point_jet','hull_jet'):
            assert set(packet[name])==keys
            assert all(len(v)==2 and Q(v[0])<=Q(v[1]) for v in packet[name].values())
        saved={x['leaf']:x for x in packets_by_digest[digest]['leaves']}
        assert len(saved)==len(packet['leaf_inputs']) and list(saved)==packet['leaf_ids'],'packet leaf coverage'
        ratio=Q(packet['direction_ratio'])
        for leaf in packet['leaf_inputs']:
            ident=leaf['leaf'];assert ident in expected and ident not in seen,'missing/duplicate leaf';seen.add(ident)
            polygon=[tuple(map(Q,p)) for p in expected[ident]['root_feasible_polygon']]
            box=(min(p[0] for p in polygon),max(p[0] for p in polygon),min(p[1] for p in polygon),max(p[1] for p in polygon))
            assert tuple(map(Q,leaf['box']))==box and inside(box,hull),'root box or hull'
            tail=leaf['tail_upper'];assert set(tail)=={'t','z','tt','tz','zz'} and all(Q(v)>=0 for v in tail.values())
            def walk(node,region):
                nonlocal min_a,min_det
                assert inside(region,hull)
                status=node['status']
                if status=='split':
                    axis=node['axis'];assert axis in (0,2) and len(node['children'])==2,'closed binary cover'
                    mid=(region[axis]+region[axis+1])/2
                    left=list(region);right=list(region);left[axis+1]=mid;right[axis]=mid
                    walk(node['children'][0],tuple(left));walk(node['children'][1],tuple(right));return
                assert status in counts,'unresolved or invalid terminal'
                counts[status]+=1
                if status=='gradient_excluded':
                    terms={'t':[(1,0,1)],'z':[(0,1,1)],'t_minus_r_z':[(1,0,1),(0,1,-ratio)]}[node['axis']]
                    actual=derivative_bound(packet,region,tail,terms);assert actual[0]>0 or actual[1]<0,'unsigned gradient'
                    assert within(actual,tuple(map(Q,node['bound']))),'saved gradient enclosure'
                else:
                    aa=derivative_bound(packet,region,tail,[(2,0,1),(1,1,-2*ratio),(0,2,ratio**2)])
                    bb=derivative_bound(packet,region,tail,[(1,1,1),(0,2,-ratio)])
                    cc=derivative_bound(packet,region,tail,[(0,2,1)])
                    det=product(aa,cc)[0]-max(x*x for x in bb)
                    assert aa[0]>0 and det>0,'nonpositive Hessian'
                    assert aa[0]>=Q(node['a_lower']) and det>=Q(node['det_lower']),'saved Hessian lower'
                    positive.append((ident,region));min_a=aa[0] if min_a is None else min(min_a,aa[0]);min_det=det if min_det is None else min(min_det,det)
            walk(saved[ident]['partition'],box)
    assert seen==set(expected),'total leaf coverage'
    assert counts=={'gradient_excluded':79,'positive_hessian':1} and len(positive)==1 and positive[0][0]==50
    # The only positive-Hessian terminal must be the entire necessary rectangle,
    # not multiple disconnected boxes whose local convexity would not give uniqueness.
    polygon=[tuple(map(Q,p)) for p in expected[50]['root_feasible_polygon']]
    full=(min(p[0] for p in polygon),max(p[0] for p in polygon),min(p[1] for p in polygon),max(p[1] for p in polygon))
    assert positive[0][1]==full,'single convex rectangle'
    def load(stem):return json.loads((ROOT/f'lab/process/{stem}.json').read_text())
    local=load('k1787-full-fisher-stationary-krawczyk')['certificate']
    root=[]
    for axis in ('t','z'):
        x=Q(local['parameter_box']['center'][axis]);r=Q(local['parameter_box']['radius'][axis]);root.extend([x-r,x+r])
    original=next(tuple(map(Q,x['box'])) for x in data['stationary_transport_inputs'] if x['leaf']==50)
    assert inside(tuple(root),original) and all(local['strict_inclusion'].values())
    bound=load('k1819-full-fisher-slab-three-boundary-cover')['certificate'];threshold=Q(bound['whole_line_value_threshold'])
    upper=enc(local['stationary_value_enclosure'])[1]
    old=load('k1763-hermite-degree-escalation')['certificate'];outer=load('k1769-degree-seven-survivor-refinement')['refinement']
    assert upper<threshold<Q(outer['threshold']) and upper<enc(old['candidate_compact'])[0]
    assert sorted(bound['whole_line_value_certified_leaf_ids']+[x['leaf'] for x in data['stationary_transport_inputs']])==list(range(78))
    return {'terminals':counts,'unresolved':0,'surviving_leaf':50,'single_convex_rectangle':True,
            'a_lower':str(min_a),'determinant_lower':str(min_det),'strict_threshold_slack':str(threshold-upper),
            'local_root_box_inside_original_leaf':True,'candidate_value_partition_size':78}

def controls():
    # Collocation independently reconstructs monomials and mixed polynomials.
    for n in (5,6):
        w=monomial_controls(n,Q(-2),Q(3))
        for p in range(n+1):
            for t in (Q(0),Q(1,7),Q(2,3),Q(1)):
                value=sum(w[j][p]*comb(n,j)*t**j*(1-t)**(n-j) for j in range(n+1))
                assert value==(-2+5*t)**p
    point={f'{i},{j}':['0','0'] for i in range(9) for j in range(9-i)}
    packet={'anchor':['0','0'],'point_jet':copy.deepcopy(point),'hull_jet':copy.deepcopy(point)}
    packet['point_jet']['2,0']=['64','64'];packet['point_jet']['1,1']=['16','16'];packet['point_jet']['0,2']=['1','1']
    tail={k:'0' for k in ('t','z','tt','tz','zz')}
    assert derivative_bound(packet,(Q(-1),Q(1),Q(-1),Q(1)),tail,[(2,0,1),(1,1,-16),(0,2,64)])==(0,0)
    # Exact x^8 highest-degree remainder: dxx=56x^6 in [-56,56].
    packet['point_jet']=copy.deepcopy(point);packet['hull_jet']['8,0']=['1','1']
    assert derivative_bound(packet,(Q(-1),Q(1),Q(0),Q(1)),tail,[(2,0,1)])==(-56,56)

def main():
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');p.add_argument('--selftest',action='store_true');args=p.parse_args()
    controls();data=json.loads(SOURCE.read_text());result=audit(data)
    if args.selftest:
        # Baseline has passed; faults fail via explicit assertions, not crash counts.
        for name,change,expected in [
          ('missing leaf',lambda d:d['correlated_profile_inputs'].pop(),'total leaf coverage'),
          ('rehashed hull',lambda d:d['correlated_profile_inputs'][0].update(hull=['0','0','0','0']),'anchor outside hull')]:
            bad=copy.deepcopy(data);change(bad)
            if name=='rehashed hull':
                item=bad['correlated_profile_inputs'][0];old=item['digest'];raw={k:v for k,v in item.items() if k!='digest'};item['digest']=hashlib.sha256(json.dumps(raw,sort_keys=True,separators=(',',':')).encode()).hexdigest()
                for row in bad['certificate']['correlated_profile']['packets']:
                    if row['input_digest']==old:row['input_digest']=item['digest']
            try:audit(bad)
            except AssertionError as exc:
                assert str(exc)==expected,(name,str(exc));print('REJECTED:',name,expected)
            else:raise AssertionError('missed '+name)
    payload={'schema_version':'1.0','scope':'independent exact correlated Taylor terminal audit; reused upstream quadrature, tail, transport and outer-cover proofs',
             'input_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'result':result,
             'new_quadrature':False,'canon_promotion':False,'source_or_physics_effect':False}
    if args.write:OUTPUT.write_text(json.dumps(payload,indent=2)+'\n')
    elif OUTPUT.exists():assert json.loads(OUTPUT.read_text())==payload,'saved audit drift'
    print('PASS: independent interpolation/Taylor replay; 79 gradient terminals, one convex Hessian terminal, zero unresolved')

if __name__=='__main__':main()
