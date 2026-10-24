"""Separate vertical integration and actual-data checks, not producer imports."""
from fractions import Fraction as Q
from pathlib import Path
import copy,json,hashlib
ROOT=Path(__file__).resolve().parents[2];M=Q(23,100)

def area(a,b,c,d):
    cuts=sorted({c,d}|{x for x in (a,b,a+9,b+9) if c<x<d})
    def length(z):return max(Q(0),min(b,z)-max(a,z-9))
    return sum(((h-l)*(length(l)+length(h))/2 for l,h in zip(cuts,cuts[1:])),Q(0))

def cut_geometry(a):
    points=sorted({Q(-3),Q(3),Q(6),Q(12),a,a+9,2*a+3,2*a+6})
    points=[x for x in points if -3<=x<=12]
    def small(z):
      lo=max(Q(-3),z-9);hi=min(Q(3),z);ell=max(hi-lo,Q(0));m=max(Q(0),min(a,hi)-lo)
      return min(m,ell-m)
    return sum(((h-l)*(small(l)+small(h))/2 for l,h in zip(points,points[1:])),Q(0))

def verify_budget(d):
    prev=json.loads((ROOT/'lab/process/k1989-capped-pulse-dual-certificates.json').read_text());c=prev['certificate'];a=list(map(Q,c['row_potentials']));b=list(map(Q,c['column_potentials']));n=len(a)
    us=[-3+Q(6*i,n) for i in range(n+1)];zs=[-3+Q(6*i,n) for i in range(len(b)+1)]
    matrix=[[area(us[i],us[i+1],zs[j],zs[j+1]) for j in range(len(b))] for i in range(n)]
    A=max(map(abs,a));B=max(map(abs,b));T=sum((matrix[i][j]*max(abs(a[i]+b[j])-M,0) for i in range(n) for j in range(len(b))),Q(0));D=Q(c['squared_norm_lower_bound']);w=d['actual_witness']
    assert Q(w['A'])==A and Q(w['B'])==B and Q(w['T'])==T and Q(w['D_low'])==D, 'potential/area certificate'
    assert sum(map(sum,matrix))==Q(w['area'])==54, 'strip area'
    tl,tr=map(Q,prev['root_interval']);K=18-3*tl-tl*tl
    for row in d['actual_error_budgets']:
      e,r,c=map(Q,(row['epsilon'],row['row_error'],row['column_error']));penalty=2*A*r+2*B*c+2*e*T
      assert Q(row['norm_lower'])==D-penalty, 'unpaid cap/marginal error'
      bound=4*e*K+2*r+2*c
      assert Q(row['forced_L1_upper'])==bound and Q(row['forced_L2_squared_upper'])==(2*M+e)*bound, 'forced norm bound'

def verify_cut(row):
    seed=row['seed'];C=M+Q(row['epsilon']);cut=set(row['cut']);coeffs=[[Q((i+2*j+seed)%4+1,7) for j in range(5)] for i in range(4)];v=[[C*Q((3*i+j+seed)%9-4,4) for j in range(5)] for i in range(4)]
    signed=Q(0);K=Q(0);H=Q(0);integ=Q(0)
    for j in range(5):
      x=sum(coeffs[i][j] for i in cut);y=sum(coeffs[i][j] for i in range(4) if i not in cut);K+=min(x,y)
      integ+=sum(coeffs[i][j]*v[i][j] for i in cut)
      if x<=y:signed+=sum(coeffs[i][j]*v[i][j] for i in cut)
      else:
        signed-=sum(coeffs[i][j]*v[i][j] for i in range(4) if i not in cut)
        H+=sum(coeffs[i][j]*v[i][j] for i in range(4))
    assert C*K-signed==Q(row['slack'])==Q(row['epsilon'])*K-Q(row['rho'])+Q(row['Hcol']), 'signed cut identity'
    assert H==Q(row['Hcol']) and integ-M*K==Q(row['rho']), 'actual column imbalance'

def main():
    d=json.loads((ROOT/'lab/process/k2009-robust-tight-cut-pulse-certificates.json').read_text());verify_budget(d)
    for row in d['cut_controls']:verify_cut(row)
    for a in (Q(-5,2),Q(-1),Q(-23,50),Q(0),Q(23,50),Q(1),Q(5,2)):
      h=3-abs(a);assert cut_geometry(a)==9*h-h*h
    for p,h in d['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    faults=[]
    def reject(name,fn):
      try:fn()
      except AssertionError as e:faults.append((name,str(e)));return
      raise AssertionError('undetected mathematical fault '+name)
    bad=copy.deepcopy(d);bad['actual_witness']['T']=str(Q(bad['actual_witness']['T'])/2)
    reject('half triangle charge',lambda:verify_budget(bad))
    bad2=copy.deepcopy(d);bad2['actual_witness']['A']=str(Q(bad2['actual_witness']['A'])/2)
    reject('potential normalization',lambda:verify_budget(bad2))
    bad3=copy.deepcopy(d);bad3['actual_error_budgets'][1]['norm_lower']=bad3['actual_witness']['D_low']
    reject('unpaid error budget',lambda:verify_budget(bad3))
    row=copy.deepcopy(next(r for r in d['cut_controls'] if Q(r['Hcol'])!=0));row['Hcol']='0'
    reject('omitted column balance',lambda:verify_cut(row))
    print('PASS K2009 probe',len(d['cut_controls']),'cut identities;7 continuum geometry integrals;',len(d['actual_error_budgets']),'actual budgets;',len(faults),'mathematical faults;',len(d['inputs']),'hashes')
    for name,reason in faults:print('DETECTED',name,reason)
if __name__=='__main__':main()
