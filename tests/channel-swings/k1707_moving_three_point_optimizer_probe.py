#!/usr/bin/env python3
"""Hostile semantic mutations for K1707."""
import copy, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1707-moving-three-point-optimizer.json').read_text())
def valid(x):
 q,z=x.get('three_point_branch',{}),x.get('decision',{})
 return all([x.get('claim_id')=='K1707','1/3<p<=1' in q.get('family',''),'beta sqrt(q)' in q.get('motion',''),
             '245/216' in q.get('optimized_quartic',''),'q^3/4' in q.get('optimized_law',''),
             z.get('k1702_cubic_equality_preserved'),z.get('fixed_p_star_finite_strength_optimality_false'),
             z.get('moving_branch_identified'),z.get('quartic_gain_exact')=='245/216',
             not z.get('all_seed_optimizer_identified'),'symmetric three-point family' in x.get('scope_guard','')])
def setp(x,path,value):
 y=copy.deepcopy(x);c=y
 for k in path[:-1]:c=c[k]
 c[path[-1]]=value;return y
def main():
 assert valid(D);print('PASS 01: baseline')
 muts=[(('claim_id',),'K1706'),(('three_point_branch','family'),'all seeds'),(('three_point_branch','motion'),'p=p*'),
       (('three_point_branch','optimized_quartic'),'wrong'),(('decision','k1702_cubic_equality_preserved'),False),
       (('decision','fixed_p_star_finite_strength_optimality_false'),False),(('decision','moving_branch_identified'),False),
       (('decision','quartic_gain_exact'),'0'),(('decision','all_seed_optimizer_identified'),True),(('scope_guard',),'global')]
 for n,(p,v) in enumerate(muts,2):assert not valid(setp(D,p,v));print(f"PASS {n:02d}: reject {'/'.join(p)}")
 print(f'RESULT: PASS {len(muts)+1}/{len(muts)+1}')
if __name__=='__main__':main()
