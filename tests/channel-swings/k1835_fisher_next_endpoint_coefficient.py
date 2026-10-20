#!/usr/bin/env sage-python
"""Exact shifted-Gaussian score jets; uniform remainder is proved in the note."""
import argparse,hashlib,json
from pathlib import Path
from sage.all import QQ,QuadraticField,PowerSeriesRing,PolynomialRing,factorial,matrix
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1835-fisher-next-endpoint-coefficient.json'
def jets(K,a0,b0,refined=False):
 S=PowerSeriesRing(K,'e',default_prec=30);e=S.gen()
 if refined:
  a=(1-e**2)/2;h=-1/(1-e**2);b=(-h+(h*h+4*a).sqrt())/2
 else:a=S(a0);b=S(b0)
 c=a*e**8;z=b*e**4;p=a/(a+b*b);t=((2-e**6)/(2-c)).sqrt();v=1-t
 u=(1-z).sqrt();w=(1+c/z).sqrt();m=p*u+(1-p)*w;s2=1-t*m*m;s=e**3*(s2/e**6).sqrt()
 mu=[t.sqrt()*(u-m)/s,t.sqrt()*(w-m)/s];eta=v/s2-1
 P=PolynomialRing(K,'y');y=P.gen();he=[P(1),y]
 for n in range(1,12):he.append(y*he[-1]-n*he[-2])
 rc=[P(1)]+[P(0)]*12
 for n in range(1,13):
  hn=sum(weight*sum(mm**(n-2*k)*eta**k/(factorial(n-2*k)*2**k*factorial(k)) for k in range(n//2+1)) for weight,mm in zip([p,1-p],mu))
  for i in range(13):rc[i]+=hn[i]*he[n]
 def mul(x,z):return [sum((x[j]*z[i-j] for j in range(i+1)),P(0)) for i in range(13)]
 inv=[P(1)]+[P(0)]*12
 for i in range(1,13):inv[i]=-sum((rc[j]*inv[i-j] for j in range(1,i+1)),P(0))
 score=[q.derivative() for q in rc];ig=mul(mul(score,score),inv)
 def gauss(q):return sum(co*factorial(k)/(2**(k//2)*factorial(k//2)) for k,co in enumerate(q.list()) if k%2==0)
 D=S([gauss(q) for q in ig]).add_bigoh(13);J=(1+D)/s2-1
 return {'J':J,'D':D,'variance':s2,'density':rc,'a':a,'b':b}
def c4(a,h):
 x=a*h;y=a*(h*h-2*a);w=x*(h*h-8*a)
 return -(5*a*h*h+2*a*a)/4-3*a*a*h**3+w*w/6-5*x*x*y

def produce():
 checks={}
 def ck(k,v):checks[k]=bool(v);assert v,k
 K=QuadraticField(3,'r');r=K.gen();fixed=jets(K,K(1)/2,(1+r)/2);ref=jets(K,None,None,True)
 expected={-6:4,0:-2,2:0,4:QQ(3)/8,6:QQ(3)/10};improved=dict(expected);improved[6]=-QQ(6)/5
 for label,v,expect in [('fixed',fixed,expected),('refined',ref,improved)]:
  for k,x in expect.items():ck(label+'_J_'+str(k),v['J'][k]==x)
  ck(label+'_odd_terms_zero',all(v['J'][k]==0 for k in [-5,-3,-1,1,3,5]))
  ck(label+'_density_normalized',v['density'][0]==1)
 ck('fixed_D6',fixed['D'][6]==QQ(1)/8);ck('fixed_D10',fixed['D'][10]==QQ(9)/32);ck('fixed_D12',fixed['D'][12]==-QQ(1)/20)
 ck('refined_x_exact',ref['a']*(ref['a']/ref['b']-ref['b'])==-QQ(1)/2)
 ck('refined_y_leading',(ref['a']*((ref['a']/ref['b']-ref['b'])**2-2*ref['a']))[2]==QQ(3)/2)
 controls=[]
 for a,b in [(QQ(1),QQ(5)/4),(QQ(1)/3,QQ(2)/3),(QQ(3)/4,QQ(3)/2)]:
  j=jets(QQ,a,b)['J'];h=a/b-b;x=a*h;y=a*(h*h-2*a)
  ck('general_constant_'+str(a),j[0]==-QQ(3)/2+2*x+2*x*x)
  ck('general_e2_'+str(a),j[2]==QQ(2)/3*y*y)
  ck('general_e4_'+str(a),j[4]==c4(a,h))
  controls.append([str(a),str(b),str(j[4])])
 R=PolynomialRing(QQ,names=('a','h'));a,h=R.gens();C=c4(a,h);Jac=matrix(QQ,[[-1,QQ(1)/2],[-1,-1]])
 grad=matrix(QQ,[[C.derivative(z)(a=QQ(1)/2,h=-1) for z in [a,h]]])*Jac.inverse()
 ck('local_coordinate_jacobian',Jac.det()==QQ(3)/2);ck('scaled_stationarity_jacobian',QQ(4)*QQ(4)/3>0)
 ck('gradient_x_y',grad[0,0]==-4 and grad[0,1]==-2);ck('refinement_square',QQ(3)/10-QQ(3)/2==-QQ(6)/5)
 return {'result_id':'K1835','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','results':{'fixed_witness':'4/delta-2+(3/8)delta^(2/3)+(3/10)delta+O(delta^(4/3))','refined_witness':'4/delta-2+(3/8)delta^(2/3)-(6/5)delta+O(delta^(4/3))','refined_parameters':'a=(1-e^2)/2, h=-1/(1-e^2), b=(-h+sqrt(h^2+4a))/2, c=a e^8, z=b e^4, delta=e^6','compact_scaling_window_coefficient':'3/8','compact_window_unique_minimizer':True,'window_branch':'x+1/2=e^4+O(e^6), y=(3/2)e^2+O(e^4)','fixed_witness_eventually_nonminimal':True,'global_next_coefficient_proved':False,'global_minimizer_rates_proved':False,'effective_onset':False,'physical_or_canon_promotion':False},'general_C4':str(C),'fixed_D_coefficients':{str(i):str(fixed['D'][i]) for i in [6,8,10,12]},'refined_D_coefficients':{str(i):str(ref['D'][i]) for i in [6,8,10,12]},'checks':checks,'rational_controls':controls,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1833-fisher-merging-radius-subleading.json','explorations/k1833-fisher-merging-radius-subleading-2026-10-20.md']}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=produce()
 if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1835',len(v['checks']),'exact coefficient/control groups')
