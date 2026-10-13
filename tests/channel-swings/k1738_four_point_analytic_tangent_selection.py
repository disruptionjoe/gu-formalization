#!/usr/bin/env python3
"""Arbitrary-precision chart-Jacobian and tangent certificate for K1738."""
import json
from decimal import Decimal, getcontext
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
getcontext().prec=70
D=Decimal

class Jet:
 def __init__(self,v,dp=0,da=0):self.v=D(v);self.dp=D(dp);self.da=D(da)
 def __add__(self,o):o=o if isinstance(o,Jet) else Jet(o);return Jet(self.v+o.v,self.dp+o.dp,self.da+o.da)
 __radd__=__add__
 def __neg__(self):return Jet(-self.v,-self.dp,-self.da)
 def __sub__(self,o):return self+(-o if isinstance(o,Jet) else -Jet(o))
 def __rsub__(self,o):return Jet(o)-self
 def __mul__(self,o):o=o if isinstance(o,Jet) else Jet(o);return Jet(self.v*o.v,self.dp*o.v+self.v*o.dp,self.da*o.v+self.v*o.da)
 __rmul__=__mul__
 def __truediv__(self,o):
  o=o if isinstance(o,Jet) else Jet(o);return Jet(self.v/o.v,(self.dp*o.v-self.v*o.dp)/o.v**2,(self.da*o.v-self.v*o.da)/o.v**2)
 def __rtruediv__(self,o):return Jet(o)/self
 def __pow__(self,n):
  if n==0:return Jet(1)
  return Jet(self.v**n,D(n)*self.v**(n-1)*self.dp,D(n)*self.v**(n-1)*self.da)

def poly(u):return 17*u**3-38*u**2+84*u-24
def root():
 lo=D('0.3270136791');hi=D('0.3270136792')
 assert poly(lo)<0<poly(hi)
 for _ in range(230):
  mid=(lo+hi)/2
  if poly(mid)<0:lo=mid
  else:hi=mid
 return (lo+hi)/2
def invariants(pv,av):
 p=Jet(pv,1,0);a=Jet(av,0,1);b=(1-p*a)/(1-p)
 m4=p*a**2+(1-p)*b**2;m6=p*a**3+(1-p)*b**3;m8=p*a**4+(1-p)*b**4
 u=3-m4;k6=m6-15*m4+30;h8=m8-28*m6+210*m4-315;x=h8/u**2
 return u,k6,x
def main():
 d=json.loads((ROOT/"lab/process/k1738-four-point-analytic-tangent-selection.json").read_text());b=d["base_seed"];s=d["selection"];z=d["decision"]
 u=root();S=2*(6-7*u)/(2-u);R=S-(3-u);disc=S*S-4*R;sq=disc.sqrt();a0=(S-sq)/2;b0=(S+sq)/2;p0=(b0-1)/(b0-a0)
 uu,k6,x=invariants(p0,a0);J=k6.dp*x.da-k6.da*x.dp;c=D(35)/3*u.sqrt()*u
 P=c*x.da/J;A=-c*x.dp/J;h10=-730*u*u+840*u-120;y=h10/(u*u*u.sqrt());floor=D(139)/432+y*y/D(362880)
 checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1738"),("root residual",abs(poly(u))<D('1e-60')),
  ("u",abs(uu.v-u)<D('1e-55')),("k6 base",abs(k6.v)<D('1e-55')),("x base",abs(x.v-D(35))<D('1e-54')),
  ("jacobian positive",D(97048)<J<D(97049)),("P",abs(P-D('-0.1037580726956868180'))<D('1e-18')),
  ("A",abs(A-D('-0.1285250038860326462'))<D('1e-18')),("first condition",abs(k6.dp*P+k6.da*A-c)<D('1e-55')),
  ("second condition",abs(x.dp*P+x.da*A)<D('1e-53')),("h10",abs(h10-D('76.6267896554263481'))<D('1e-16')),
  ("y0",abs(y-D('1253.0425860990422142'))<D('1e-14')),("floor",abs(floor-D('4.6485772778267626'))<D('1e-15')),
  ("h10 formula","-730u^2+840u-120" in b["h_10"]),("jacobian recorded","97048.7740746550" in s["jacobian"]),
  ("P recorded","-0.1037580726956868" in s["solution"]),("A recorded","-0.1285250038860326" in s["solution"]),
  ("strict excess","xi^2/5040" in s["uniqueness"]),("second order open","remaining second-order freedom" in s["second_order_boundary"]),
  ("leading unique",z["leading_analytic_tangent_unique"]),("branch open",not z["complete_local_analytic_branch_unique"]),
  ("global open","remote-branch exclusion" in d["scope_guard"])]
 assert len(checks)==23
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
