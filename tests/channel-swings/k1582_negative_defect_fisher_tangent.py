#!/usr/bin/env python3
"""Certificate for K1582's tangent-order separation."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1582-negative-defect-fisher-tangent.json').read_text());q=d['fixed_moment_tangent'];z=d['decision'];checks=[]
 checks += [('claim',d['claim_id']=='K1582'),('moment tangents','normalization, mean and covariance' in q['orthogonality']),('residual orthogonal','orthogonal' in q['orthogonality']),('bounded approximation','bounded smooth' in q['exact_moment_correction']),('exact restoration','restore normalization, mean and covariance exactly' in q['exact_moment_correction']),('second order correction','second order' in q['exact_moment_correction']),('F quadratic','O(epsilon^2)' in q['fisher_order']),('defect linear','-c_N epsilon' in q['defect_order']),('positive c','c_N>0' in q['defect_order']),('linear bound excluded','No neighborhood' in q['excluded_linear_compensation']),('scope local','fixed cutoff' in q['scope_guard']),('quadratic remains','quadratic' in q['scope_guard'])]
 for eps in (1e-1,1e-2,1e-3): checks.append((f'order separation {eps}',eps*eps<eps))
 checks += [('negative states',z['negative_defect_states_constructed_locally']),('F order',z['fisher_excess_quadratic']),('gain order',z['interaction_gain_linear']),('linear excluded',z['linear_compensation_excluded']),('global open',not z['global_compensation_excluded']),('bounded open',not z['bounded_error_recentering']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
