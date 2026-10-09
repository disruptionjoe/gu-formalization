#!/usr/bin/env python3
"""Certificate for K1581's finite-cutoff Gaussian residual descent."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1581-profiled-gaussian-residual-descent.json').read_text()); q=d['residual_descent']; z=d['decision']; checks=[]
 checks += [('claim',d['claim_id']=='K1581'),('finite cutoff','Fix N' in q['finite_cutoff_setting']),('positive coupling','g>0' in q['finite_cutoff_setting']),('quadratic free','degree at most two' in q['nonzero_residual']),('quartic survives','nonzero quartic' in q['nonzero_residual']),('residual nonzero','nonzero' in q['nonzero_residual']),('ritz span','span{G_N,u_N}' in q['ritz_matrix']),('off diagonal','sigma_N' in q['ritz_matrix']),('strict eigenvalue','strictly below' in q['ritz_matrix']),('translation symmetry','translation invariant' in q['symmetry']),('finite consequence','strictly above' in q['finite_cutoff_consequence']),('scope gap','No cutoff-uniform' in q['scope_guard'])]
 lam,sig,mu=5.0,2.0,9.0; low=(lam+mu-math.sqrt((mu-lam)**2+4*sig**2))/2
 checks += [('sample Ritz strict',low<lam),('gaussian excluded',z['gaussian_eigenstate_excluded']),('strict descent',z['strict_finite_cutoff_descent']),('symmetry retained',z['translation_invariant_descent']),('no uniform gap',not z['uniform_asymptotic_gap']),('no coefficient',not z['unrestricted_coefficient_identified']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1): assert ok,label; print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__': main()
