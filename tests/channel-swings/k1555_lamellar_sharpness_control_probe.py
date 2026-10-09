#!/usr/bin/env python3
"""Hostile mutations for K1555."""
import copy,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1555-lamellar-sharpness-control.json').read_text())
def valid(x):
 q,d=x['sharpness_control'],x['decision'];return all([x['claim_id']=='K1555','sin(M_N x_1)' in q['construction'],'plus/minus M_N e_1' in q['bandlimit'],'8/pi^2' in q['sign_shell'],'one half' in q['phase_balance'],'3/8' in q['defect'],'N^0 cutoff exponent' in q['sharpness'],'sharpness only in the cutoff exponent' in q['scope_guard'],d['fixed_shell_lamellar_control_constructed'],d['constant_defect_computed'],d['cutoff_exponent_zero_sharp'],not d['optimal_eta_dependence_proved'],not d['low_energy_trial_constructed'],not d['protected_status_change']])
def main():
 assert valid(D);m=[(('claim_id',),'K1554'),(('sharpness_control','construction'),'changed'),(('sharpness_control','bandlimit'),'changed'),(('sharpness_control','sign_shell'),'changed'),(('sharpness_control','phase_balance'),'changed'),(('sharpness_control','defect'),'changed'),(('sharpness_control','sharpness'),'changed'),(('sharpness_control','scope_guard'),'changed'),(('decision','fixed_shell_lamellar_control_constructed'),False),(('decision','constant_defect_computed'),False),(('decision','cutoff_exponent_zero_sharp'),False),(('decision','optimal_eta_dependence_proved'),True),(('decision','low_energy_trial_constructed'),True),(('decision','protected_status_change'),True)]
 for i,(path,value) in enumerate(m,1):
  x=copy.deepcopy(D);cur=x
  for k in path[:-1]:cur=cur[k]
  cur[path[-1]]=value;assert not valid(x),path;print(f'PASS {i:02d}: rejected {"/".join(path)}')
 print(f'RESULT: PASS {len(m)}/{len(m)}')
if __name__=='__main__':main()
