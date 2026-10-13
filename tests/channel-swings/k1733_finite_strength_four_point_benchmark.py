#!/usr/bin/env python3
"""Independent-order, multistart finite-channel benchmark for K1733."""
import json, math
from pathlib import Path
import numpy as np
from numpy.polynomial.hermite_e import hermegauss
from scipy.optimize import brentq, minimize, minimize_scalar
ROOT=Path(__file__).resolve().parents[2]
U0=.327013679166042; A0=.441384393880459; B0=3.994879309683925; P0=.842798253731782

def chart(p,a):
 b=(1-p*a)/(1-p);m2=p*a*a+(1-p)*b*b;return b,3-m2
def k6(p,a):
 b,u=chart(p,a);m2=3-u;m3=p*a**3+(1-p)*b**3;return m3-15*m2+30,u
def fisher(points,pri,t,order):
 z,w=hermegauss(order);w/=math.sqrt(2*math.pi);rt=math.sqrt(t);v=1-t;out=0.
 for x,pr in zip(points,pri):
  y=rt*x+math.sqrt(v)*z; logs=np.log(pri)[None,:]-(y[:,None]-rt*points[None,:])**2/(2*v)
  logs-=logs.max(axis=1)[:,None];post=np.exp(logs);post/=post.sum(axis=1)[:,None]
  mean=post@points;score=rt/v*(mean-rt*y);out+=pr*np.dot(w,score*score)
 return out
def f4(x,q,order):
 p,a=x;b,u=chart(p,a)
 if min(p,1-p,a,1-a,u-q)<=0:return 1.
 return fisher(np.array([-math.sqrt(b),-math.sqrt(a),math.sqrt(a),math.sqrt(b)]),
               np.array([(1-p)/2,p/2,p/2,(1-p)/2]),math.sqrt(q/u),order)
def fixed(q,order):
 target=(35/3)*math.sqrt(q)
 def eq(p):
  v=p*A0+(1-p)*B0;a=A0/v;kk,u=k6(p,a);return kk/u**1.5-target
 p=brentq(eq,P0-.2,P0);v=p*A0+(1-p)*B0;a=A0/v;return f4((p,a),q,order)
def f3(p,q,order):
 u=3-1/p
 if p<=1/3 or u<=q:return 1.
 return fisher(np.array([-1/math.sqrt(p),0.,1/math.sqrt(p)]),np.array([p/2,1-p,p/2]),math.sqrt(q/u),order)
def solve(q,order):
 starts=[[P0-.12*math.sqrt(q),A0-.15*math.sqrt(q)],[P0,A0],[.8,.4],[.9,.6]]; sols=[]
 for x0 in starts:
  r=minimize(lambda x:f4(x,q,order),x0,method="Nelder-Mead",options={"maxiter":4000,"xatol":1e-11,"fatol":1e-17})
  sols.append((r.fun,*r.x))
 return min(sols),max(s[0] for s in sols)-min(s[0] for s in sols)
def main():
 d=json.loads((ROOT/"lab/process/k1733-finite-strength-four-point-benchmark.json").read_text());checks=[]
 checks += [("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1733"),
            ("computed grade",d["grade"]=="reproducible_numerical_evidence_not_interval_certification")]
 records={r["q"]:r for r in d["benchmark"]["order_180_minimizers"]}
 for q in (.003,.01,.03):
  s120,spread120=solve(q,120);s180,spread180=solve(q,180);b,u=chart(s180[1],s180[2])
  tri=minimize_scalar(lambda p:f3(p,q,180),bounds=(1/3+1e-7,.999),method="bounded",options={"xatol":1e-11})
  checks += [(f"orders {q}",abs(s120[0]-s180[0])<1e-15),(f"starts {q}",max(spread120,spread180)<1e-15),
             (f"interior {q}",0<s180[2]<1 and 0<s180[1]<1 and b>1 and u>q),
             (f"record j {q}",abs(s180[0]-records[q]["j"])<2e-15),
             (f"record p {q}",abs(s180[1]-records[q]["p"])<3e-6),
             (f"record a {q}",abs(s180[2]-records[q]["a"])<3e-6),
             (f"beats fixed {q}",s180[0]<fixed(q,180)),(f"beats three {q}",s180[0]<tri.fun)]
 z=d["decision"];checks += [("joint",z["joint_radius_probability_motion_observed"]),("fixed unsupported",not z["k1728_path_exact_finite_strength_optimality_supported"]),
   ("two-radius open",not z["two_radius_global_optimizer_proved"]),("all seed open",not z["all_seed_optimizer_proved"]),
   ("scope intervals","intervals" in d["scope_guard"]),("scope remote","remote" in d["scope_guard"])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
