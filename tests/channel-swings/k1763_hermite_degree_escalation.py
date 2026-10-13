#!/usr/bin/env python3
"""Arb candidate upper bound and Hermite-projection degree escalation for K1763."""
import importlib.util,json,sys
from fractions import Fraction as Q
from math import comb,factorial
from pathlib import Path
from flint import arb,ctx

ROOT=Path(__file__).resolve().parents[2];ARTIFACT=ROOT/"lab/process/k1763-hermite-degree-escalation.json"
P=ROOT/"tests/channel-swings/k1749_arb_finite_channel_boundary.py"
s=importlib.util.spec_from_file_location("k1749",P);k=importlib.util.module_from_spec(s);s.loader.exec_module(k)
ctx.dps=100;ctx.threads=1

def central_hermites(c,z,max_degree):
 w=c/z-z;mu={0:arb(1),1:arb(0),2:c}
 for r in range(3,max_degree//2+1):mu[r]=w*mu[r-1]+c*mu[r-2]
 raw={r:sum((k.aq(Q(comb(r,j)))*mu[j] for j in range(r+1)),arb(0)) for r in range(max_degree//2+1)}
 return {n:sum((k.aq(Q((-1)**j*factorial(n),factorial(j)*factorial(n-2*j)*2**j))*raw[(n-2*j)//2] for j in range(n//2+1)),arb(0)) for n in range(0,max_degree+1,2)}

def solve(A,b):
 n=len(b);M=[row[:]+[b[i]] for i,row in enumerate(A)]
 for j in range(n):
  assert abs(M[j][j])>0
  for i in range(j+1,n):
   f=M[i][j]/M[j][j]
   for ell in range(j,n+1):M[i][ell]-=f*M[j][ell]
 x=[arb(0)]*n
 for i in range(n-1,-1,-1):x[i]=(M[i][n]-sum((M[i][j]*x[j] for j in range(i+1,n)),arb(0)))/M[i][i]
 return x

def projection(cq,zq,degree):
 c,z=k.aq(cq),k.aq(zq);t=(k.aq(Q(1,1024))/(2-c)).sqrt();hx=central_hermites(c,z,2*degree);hy={n:t**(n//2)*hx[n] for n in hx}
 ds=list(range(3,degree+1,2));b=[hy[n+1] for n in ds]
 G=[[sum((k.aq(Q(factorial(j)*comb(m,j)*comb(n,j)))*hy[m+n-2*j] for j in range(min(m,n)+1)),arb(0)) for n in ds] for m in ds]
 x=solve(G,b);return sum((b[i]*x[i] for i in range(len(b))),arb(0))

def candidate():
 c=Q(3308164903,2000000000);z=Q(1127044207,2000000000);p=k.aq(c/(c+z*z));a=k.aq(1-z);b,u,_,_=k.chart_invariants(p,a);t=(k.aq(Q(1,1024))/u.v).sqrt()
 return {"p":p,"a":a,"b":b.v,"u":u.v,"t":t,"v":1-t}

def compact_single(channel):
 total=arb(0);remmax=arb(0);h=k.CELL_HALF_WIDTH;cells=int(k.COMPACT_RADIUS/h)
 for index in range(-cells,cells):
  midpoint=(Q(index)+Q(1,2))*h;local=h/2
  point=k.T([k.aq(midpoint),1]+[0]*(k.TAYLOR_ORDER-1));val=k.fisher_integrand(point,channel)
  poly=sum((val.c[d]*k.aq(2*local**(d+1)/Q(d+1)) for d in range(0,k.TAYLOR_ORDER,2)),arb(0))
  iy=k.T([k.ball_q(midpoint-local,midpoint+local),1]+[0]*(k.TAYLOR_ORDER-1));iv=k.fisher_integrand(iy,channel)
  rr=(abs(iv.c[k.TAYLOR_ORDER-1])*k.aq(2*local**k.TAYLOR_ORDER/Q(k.TAYLOR_ORDER))).upper();r=arb(0,rr);total+=poly+r
  if abs(r).upper()>remmax.upper():remmax=abs(r)
 return total,remmax,2*cells

def enc(x):return x.str(45,radius=True,more=True)
def compute():
 ch=candidate();compact,rem,cells=compact_single(ch);tail=k.tail_bound(ch);upper=compact+arb(0,tail.upper())
 pts={"rademacher":(Q(0),Q(1)),"interior_control":(Q(33,20),Q(2,5)),"near_control":(Q(167,100),Q(1107,2000)),"candidate":(Q(3308164903,2000000000),Q(1127044207,2000000000))}
 return {"candidate_upper":enc(upper),"candidate_compact":enc(compact),"candidate_tail":enc(tail),"maximum_cell_remainder":enc(rem),"cells":cells,
  "projections":{name:{str(d):enc(projection(c,z,d)) for d in (3,5,7,9)} for name,(c,z) in pts.items()}}

def validate(d):
 got=compute();cert=d["certificate"];dec=d["decision"];checks=[("schema",d["schema_version"]=="1.0"),("claim",d["claim_id"]=="K1763"),("backend",d["backend"]=="python-flint==0.9.0"),("cells",cert["cells"]==got["cells"]==352)]
 for key in ("candidate_upper","candidate_compact","candidate_tail","maximum_cell_remainder"):checks.append((key,arb(cert[key]).contains(arb(got[key]))))
 for name,rows in got["projections"].items():
  for degree,val in rows.items():checks.append((f"{name}.{degree}",arb(cert["projections"][name][degree]).contains(arb(val))))
 ub=arb(cert["candidate_upper"]);checks += [("R5 prunes",arb(cert["projections"]["rademacher"]["5"]).lower()>ub.upper()),("interior D5 prunes",arb(cert["projections"]["interior_control"]["5"]).lower()>ub.upper()),("near D9 prunes",arb(cert["projections"]["near_control"]["9"]).lower()>ub.upper()),("candidate survives",arb(cert["projections"]["candidate"]["9"]).upper()<ub.lower()),("hierarchy certified",dec["degree_escalation_certified_at_named_controls"]),("not cover",not dec["global_interval_cover_completed"]),("not optimum",not dec["global_optimizer_proved"])]
 return checks

def main():
 if "--print" in sys.argv:print(json.dumps(compute(),indent=2));return
 d=json.loads(ARTIFACT.read_text());checks=validate(d)
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
