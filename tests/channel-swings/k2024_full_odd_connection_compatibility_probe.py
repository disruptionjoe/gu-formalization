"""Direct full-matrix replay of K2024; does not import its producer."""
from pathlib import Path
import json,hashlib
from sage.all import QQ,matrix,identity_matrix,zero_matrix,block_matrix,block_diagonal_matrix
from k1967_paired_raw_coefficient_observation import setup
from k1836_k77_differential_dirac_quotient import mat
from k2021_common_degree_dual_operator import raw,H as HD
ROOT=Path(__file__).resolve().parents[2]
def check_cert(cols,cert):
 rank=0;embedded=[];seen_columns=set();seen_equations=set()
 for group in cert['blocks']:
  ids=group['columns'];rows=group['selected_rows'];piv=group['pivot_columns']
  assert not seen_columns.intersection(ids);seen_columns.update(ids)
  A=matrix(QQ,[[cols[j].get(r,0) for j in ids] for r in rows]);inv=mat(group['inverse']);K=mat(group['kernel'])
  assert inv*A.matrix_from_columns(piv)==identity_matrix(QQ,len(rows))
  allrows=sorted(set().union(*(cols[j].keys() for j in ids)))
  assert not seen_equations.intersection(allrows);seen_equations.update(allrows)
  assert K.rank()==K.nrows()
  for r in allrows:
   row=matrix(QQ,1,len(ids),[cols[j].get(r,0) for j in ids])
   assert row*K.transpose()==zero_matrix(QQ,1,K.nrows())
  for kr in K:
   v=[QQ(0)]*len(cols)
   for j,x in zip(ids,kr):v[j]=x
   embedded.append(v)
  assert len(rows)+K.nrows()==len(ids);rank+=len(rows)
 assert seen_columns==set(range(len(cols)))
 assert rank==cert['rank']
 assert mat(cert['kernel'])==(matrix(QQ,embedded) if embedded else matrix(QQ,0,len(cols)))
 # The selected full-rank minor must reject a changed actual coefficient.
 g0=next(x for x in cert['blocks'] if x['selected_rows']);ids=g0['columns'];rows=g0['selected_rows'];piv=g0['pivot_columns']
 T=matrix(QQ,[[cols[j].get(r,0) for j in ids] for r in rows]);T[0,piv[0]]+=1
 assert mat(g0['inverse'])*T.matrix_from_columns(piv)!=identity_matrix(QQ,len(rows))
 return rank

def check_repair(report,J,h,C,djs):
 br=report['broader_repair'];N=mat(br['M']);S=J.transpose()*h*block_matrix(QQ,[[a] for a in djs],sparse=True)
 assert S==mat(br['S']) and S.transpose()==-S and N.transpose()==-N and N.rank()==128
 assert S.rank()==128 and (S*S).is_diagonal()
 assert set(-(S*S)[i,i] for i in range(128))=={QQ(81)/19600,QQ(81)/4900}
 assert N*S==S*N and all(N*c+c*N==0 for c in C)
 inv=N.inverse();assert sum(x*x for x in inv.dict().values())==QQ(br['inverse_frobenius_squared'])==31872
 assert QQ(br['gap_squared_lower'])==QQ(1)/31872
 target=block_matrix(QQ,[[a] for a in djs],sparse=True)*N
 for name in ['full_K','zero_southeast_K']:
  Kfull=mat(br[name]);assert h*Kfull==Kfull.transpose()*h and Kfull*J==target
 assert not mat(br['zero_southeast_K'])[1792:,1792:]
 # Actual wrong mass and raw block perturbations must violate live equations.
 bad=N.copy() if hasattr(N,'copy') else matrix(N);bad[0,0]+=1
 assert bad.transpose()!=-bad
 bad=matrix(mat(br['zero_southeast_K']));bad[0,0]+=1
 assert bad*J!=target
 old=mat(json.loads((ROOT/'lab/process/k1967-paired-raw-coefficient-observation.json').read_text())['scalar']['repair'][0]['M'])
 assert (S*old-(S*old).transpose()).rank()==128
 for name,tie in zip(['full_K','zero_southeast_K'],br['raw_connection_tie_defects']):
  Kf=mat(br[name]);expected=zero_matrix(QQ,1920,1920,sparse=True)
  for k in range(14):
   om=Kf[128*k:128*(k+1),1792:];D=matrix(QQ,1920,1920,{ij:QQ(v) for ij,v in raw(k).items()},sparse=True)
   expected+=D*block_diagonal_matrix([om]*15,sparse=True)
  diff=Kf[:1792,:1792]-expected[:1792,:1792];assert len(diff.dict())==tie['entries']
  i,j,v=tie['witness'];assert diff[i,j]==QQ(v)!=0
 print('PASS full positive massive core, both H completions including southeast zero, exact gap and three physical coefficient faults',flush=True)

def main():
 report=json.loads((ROOT/'lab/process/k2024-full-odd-connection-compatibility.json').read_text())
 g,volume,eta,js,C,P,djs,Fi,Ti,_=setup();I=identity_matrix(QQ,128,sparse=True);Z=zero_matrix(QQ,128,128,sparse=True)
 J=block_matrix(QQ,[[a] for a in js],sparse=True);DJ=block_matrix(QQ,[[a] for a in djs[:14]],sparse=True)
 cols=[];images=[]
 for k in range(14):
  D=matrix(QQ,1920,1920,{ij:QQ(v) for ij,v in raw(k).items()},sparse=True)
  for a in range(14):
   for dual in (0,1):
    B=g[a]*(volume if dual else I);out=D*block_diagonal_matrix([B]*15,sparse=True)*J;M=Fi*out[:128,:];defect=out[:1792,:]-DJ*M
    cols.append({r*128+s:v for (r,s),v in defect.dict().items()});images.append(M)
  print('direct coefficient row',k,flush=True)
 assert report['labels']==[[k,a,b] for k in range(14) for a in range(14) for b in (0,1)]
 r0=check_cert(cols,report['upper']);K=mat(report['upper']['kernel']);h=matrix(QQ,1920,1920,{ij:QQ(v) for ij,v in HD.items()},sparse=True);defs=[];joint=[]
 for ix,row in enumerate(K):
  full=zero_matrix(QQ,1920,1920,sparse=True)
  for k in range(14):
   om=sum((row[28*k+2*a+b]*g[a]*(volume if b else I) for a in range(14) for b in (0,1)),Z)
   if om:
    D=matrix(QQ,1920,1920,{ij:QQ(v) for ij,v in raw(k).items()},sparse=True)
    full+=D*block_diagonal_matrix([om]*15,sparse=True)
  df=(h*full-full.transpose()*h)[:1792,:1792];d={r*1792+s:v for (r,s),v in df.dict().items()};M=sum((x*m for x,m in zip(row,images)),Z);cons=P*M+M.transpose()*P
  defs.append(d);joint.append({**d,**{1792**2+r*128+s:v for (r,s),v in cons.dict().items()}})
  print('direct full defect',ix,flush=True)
 r1=check_cert(defs,report['upper_common_form']);r2=check_cert(joint,report['joint_common_form_and_energy'])
 check_repair(report,J,h,C,djs)
 for p,hsh in report['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==hsh
 print('PASS K2024 direct matrix ranks',r0,r1,r2,'three actual coefficient faults; four provenance hashes',flush=True)
if __name__=='__main__':
 import sys
 if '--repair-only' in sys.argv:
  r=json.loads((ROOT/'lab/process/k2024-full-odd-connection-compatibility.json').read_text())
  _,_,_,js,C,_,djs,_,_,_=setup();J=block_matrix(QQ,[[a] for a in js],sparse=True);h=matrix(QQ,1920,1920,{ij:QQ(v) for ij,v in HD.items()},sparse=True)
  check_repair(r,J,h,C,djs)
 else:main()
