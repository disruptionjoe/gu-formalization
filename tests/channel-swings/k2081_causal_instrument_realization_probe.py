"""Independent Jordan-Wigner, exterior-power and local-rotation controls."""
from pathlib import Path
from copy import deepcopy
from itertools import combinations
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def modes(N):
 out=[]
 for k in range(N):
  a=s.zeros(2**N)
  for word in range(2**N):
   if word>>k&1:a[word^(1<<k),word]=(-1)**sum((word>>j)&1 for j in range(k))
  out.append(a)
 return out
def number(a):return a.H*a
def wedge(U):
 N=U.rows;V=s.zeros(2**N)
 for i in range(2**N):
  rows=[k for k in range(N) if i>>k&1]
  for j in range(2**N):
   cols=[k for k in range(N) if j>>k&1]
   if len(rows)==len(cols):V[i,j]=s.simplify(U.extract(rows,cols).det()) if rows else 1
 return V
def equal(a,b):return (a-b).applyfunc(s.simplify)==s.zeros(a.rows,a.cols)
def funnel(f,edges):
 N=f.rows;U=s.eye(N);x=f.copy()
 # On-site phases followed by real rotations on a rooted tree.
 D=s.diag(*[s.conjugate(z)/s.sqrt(s.conjugate(z)*z) if z!=0 else 1 for z in x]);U=D*U;x=D*x
 for parent,child in edges:
  aa,bb=x[parent],x[child];norm=s.sqrt(aa**2+bb**2)
  if norm==0:continue
  G=s.eye(N);G[parent,parent]=G[child,child]=aa/norm;G[parent,child]=bb/norm;G[child,parent]=-bb/norm
  U=(G*U).applyfunc(s.simplify);x=(G*x).applyfunc(s.simplify)
 return U,x

def check(d,omit_reverse=False,corrupt_swap=False):
 a=modes(3);I=s.eye(8);vac=s.eye(8)[:,0];h=a[0].H*vac;hp=a[1].H*vac
 af=(a[0]+a[2])/s.sqrt(2);N=number(af);R=I-2*N;Ng=number(a[2])
 swap1=s.Matrix([[0,1,0],[-1,0,0],[0,0,1]]) if not corrupt_swap else s.eye(3);W=wedge(swap1)
 assert equal(W.H*W,I),'even swap unitary'
 assert equal((W*h)*(W*h).H,hp*hp.H),'local swap witness'
 out=lambda rho:(rho+R*rho*R)/2
 delta=s.trace(Ng*(out(h*h.H)-out(hp*hp.H)))
 c=d['constants'];assert delta==s.Rational(c['channel_signal_factor'])/4==s.Rational(c['example_channel_signal']),'channel signalling witness'
 assert (h.H*N*h)[0]-(hp.H*N*hp)[0]==s.Rational(1,2),'record witness'
 assert s.Rational(c['record_error_factor'])/2==s.Rational(c['example_record_error']),'record triangle factor'
 assert s.Rational(c['channel_error_factor'])/4==delta/2,'channel triangle factor'
 assert equal(N*N,N) and equal(R*R,I),'complete Lueders reflection'
 # A phase-only swap can miss symmetric populations; our occupation swap does not.
 phase=s.diag(-1,1,1);Wp=wedge(phase)
 assert s.trace(Ng*out(Wp*h*h.H*Wp.H))==s.trace(Ng*out(h*h.H)),'phase countercontrol'
 a4=modes(4);I4=s.eye(16);e=s.eye(4)[:,0]
 for f,edges in [(s.Matrix([1,2*s.I,2,-4*s.I])/5,[(2,3),(1,2),(0,1)]),(s.Matrix([0,0,1,0]),[(0,3),(0,2),(0,1)])]:
  U,x=funnel(f,edges);assert equal(x,e) and equal(U.H*U,s.eye(4)),'tree funnel'
  V=wedge(U);nf=number(sum((s.conjugate(f[j])*a4[j] for j in range(4)),s.zeros(16)))
  n0=number(a4[0]);K=n0*V if omit_reverse else V.H*n0*V
  assert equal(K,nf),'reverse rotations preserve full instrument'
  assert equal(K*K,K) and equal(K.H*K+(I4-K).H*(I4-K),I4),'all outcomes retained'
  assert equal(V.H*V,I4),'exterior power unitary'
 assert s.Rational(c['mixing_time_factor'])==1,'two passes each at most pi/2 per edge'
 return 'exact three-mode causal witnesses and two four-mode full-instrument tree controls'
def grid_control(shape,omit_last=False):
 from itertools import product
 sites=list(product(*[range(n) for n in shape]));index={x:i for i,x in enumerate(sites)};N=len(sites)
 f=s.Matrix(range(1,N+1));f=f/s.sqrt((f.H*f)[0]);x=f.copy();U=s.eye(N);layers=[]
 for axis,L in enumerate(shape):
  for k in range(L-1,0,-1):
   edges=[]
   for site in sites:
    if site[axis]!=k or any(site[j]!=0 for j in range(axis)):continue
    parent=list(site);parent[axis]-=1;edges.append((index[tuple(parent)],index[site]))
   layers.append(edges)
 assert len(layers)==sum(L-1 for L in shape),'grid layer depth'
 for edges in layers[:-1] if omit_last else layers:
  touched=[n for e in edges for n in e];assert len(set(touched))==len(touched),'parallel edges disjoint'
  G=s.eye(N)
  for a,b in edges:
   aa,bb=x[a],x[b];norm=s.sqrt(aa**2+bb**2)
   if norm==0:continue
   G[a,a]=G[b,b]=aa/norm;G[a,b]=bb/norm;G[b,a]=-bb/norm
   assert sum(abs(sites[a][j]-sites[b][j]) for j in range(len(shape)))==1,'grid locality'
  U=(G*U).applyfunc(s.simplify);x=(G*x).applyfunc(s.simplify)
 assert equal(x,s.eye(N)[:,0]) and equal(U.H*U,s.eye(N)),'parallel grid funnel'
 return len(layers)
def main():
 d=json.loads((ROOT/'lab/process/k2081-causal-instrument-realization.json').read_text());print('PASS baseline',check(d));print('PASS grid layers',grid_control((3,3)),grid_control((2,2,2)));faults=[]
 for key,val in [('channel_signal_factor','1'),('record_error_factor','1'),('channel_error_factor','2')]:
  b=deepcopy(d);b['constants'][key]=val;faults.append((key,lambda z=b:check(z)))
 faults.extend([('omit reverse',lambda:check(d,omit_reverse=True)),('wrong swap',lambda:check(d,corrupt_swap=True)),('missing grid layer',lambda:grid_control((3,3),omit_last=True))])
 for name,fn in faults:
  try:fn()
  except AssertionError as e:assert str(e);print('DETECTED',name,str(e))
  else:raise AssertionError('undetected '+name)
 print('PASS 6 faults; finite algebra is not a continuum apparatus proof')
if __name__=='__main__':main()
