"""Derivative-annihilating exact positive functional on the full K1945 family."""
import argparse,hashlib,json
from pathlib import Path
from sage.all import QQ,matrix,vector
from k1836_k77_differential_dirac_quotient import mat,enc,clifford
ROOT=Path(__file__).resolve().parents[2];UP='lab/process/k1945-energy-compatible-raw-columns.json';OUT=ROOT/'lab/process/k1948-variable-observation-rigidity.json'
def functional():
 w=matrix(QQ,4,64)
 for typ,scale in enumerate([16,1,1,16]):
  sign=-1 if typ<2 else 1;mag=1 if typ in [0,3] else 2
  for j,x in {3:1,28:sign*mag*QQ(9)/265,46:mag*QQ(9)/263,58:-sign*3,63:-sign*mag*QQ(18)/69695}.items():w[typ,j]=scale*x
 return w

def produce():
 r=json.loads((ROOT/UP).read_text());w=functional();d=[x/24 for x in clifford()];checks={};local=[];pairs=[]
 def ck(k,x):checks[k]=bool(x);assert x,k
 for typ in range(4):
  b=next(b for b in r['blocks'] if b['type']==typ);T=list(map(mat,b['T']));o=r['observation'][typ];ell=w.row(typ)
  for j,tr in enumerate(o['triples']):
   C,S=mat(tr['C']),mat(tr['S'])
   ck(f'time_annihilation_{typ}_{j}',ell*vector(QQ,S.list())==0)
   for i in range(3):ck(f'space_annihilation_{typ}_{j}_{i}',ell*vector(QQ,(T[i]*C-d[i]*S).list())==0)
  vals=[ell*vector(QQ,mat(q).list()) for q in o['quadratic_coefficients']];diag=[i==j for i in range(3) for j in range(i,3)]
  ck(f'local_positive_{typ}',all(v>0 if yes else v==0 for v,yes in zip(vals,diag)));local.append(list(map(str,vals)))
 for rec in r['cross_copy']:
  a,b=rec['types'];co=mat(rec['quadratic_coefficients']);ell=vector(QQ,list(w.row(a))+list(w.row(b)));vals=list(ell*co);diag=[i==j for i in range(4) for j in range(i,4)]
  ck(f'pair_positive_{a}_{b}',all(v>0 if yes else v==0 for v,yes in zip(vals,diag)));pairs.append({'types':[a,b],'coefficients':list(map(str,vals))})
 positive=[QQ(v) for row in local for v in row if QQ(v)>0]+[QQ(v) for p in pairs for v in p['coefficients'] if QQ(v)>0];mu=min(positive)
 counts=[sum(b['type']==typ for b in r['blocks']) for typ in range(4)];norm2=sum(counts[t]*sum(x*x for x in w.row(t)) for t in range(4));ck('all32_copies',counts==[8,8,8,8]);ck('strict_coercivity',mu>0 and norm2>0)
 return {'result_id':'K1948','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','functional':enc(w),'local_coefficients':local,'pair_coefficients':pairs,'minimum_square_weight':str(mu),'full_functional_frobenius_norm_squared':str(norm2),'residual_coercivity_squared_constant':str(norm2/(mu*mu)),'results':{'all_real_variable_one_column_conservative_solutions_zero':True,'arbitrary_cross_copy_mixing':True,'boundary_or_periodicity_assumptions_required':False,'locally_square_integrable_weak_coefficients':True,'approximate_full_residual_bound_requires_exact_first_order_equations':True,'physical_GU_exclusion':False},'checks':checks,'inputs':{UP:hashlib.sha256((ROOT/UP).read_bytes()).hexdigest()}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=produce()
 if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1948',len(v['checks']),'exact derivative and positivity controls; mu',v['minimum_square_weight'])
