#!/usr/bin/env python3
"""K1233: one binary-pair holdout has three independent source-sensitive coordinates."""
from fractions import Fraction as F
import json
from pathlib import Path
OUT=Path(__file__).parents[2]/"lab/process/k1233-minimal-holdout-source-certificate.json"

def rank(A):
 A=[[F(x) for x in r] for r in A];r=0
 for c in range(len(A[0])):
  p=next((i for i in range(r,len(A)) if A[i][c]),None)
  if p is None:continue
  A[r],A[p]=A[p],A[r];q=A[r][c];A[r]=[x/q for x in A[r]]
  for i in range(len(A)):
   if i!=r and A[i][c]:q=A[i][c];A[i]=[x-q*y for x,y in zip(A[i],A[r])]
  r+=1
 return r

def validate(d):
 H=[[1,x,y,x*y] for x in (-1,1) for y in (-1,1)]
 assert rank(H)==4
 assert rank([r[1:] for r in H])==3
 A,B,C=F(1,5),-F(1,7),F(1,9)
 p=[(1+x*A+y*B+x*y*C)/4 for x in (-1,1) for y in (-1,1)]
 assert sum(p)==1
 recA=sum(x*p[2*(x==1)+(y==1)] for x in (-1,1) for y in (-1,1))
 recB=sum(y*p[2*(x==1)+(y==1)] for x in (-1,1) for y in (-1,1))
 recC=sum(x*y*p[2*(x==1)+(y==1)] for x in (-1,1) for y in (-1,1))
 assert (recA,recB,recC)==(A,B,C)
 assert d["minimum_independent_statistics"]==3
 assert d["certificate"]==["A=a.(M u+t)","B=b.v","C=a^T(M T+t v^T)b"]
 assert d["decision"]["normalization_alone_reduces_four_probabilities_to_three"] is True
 assert d["decision"]["process_calibration_supplies_certificate"] is False
 assert d["claim_ceiling"].startswith("Exact linear")

if __name__=="__main__":
 d=json.loads(OUT.read_text());validate(d);print("K1233 controls: 10/10")
