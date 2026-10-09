#!/usr/bin/env python3
"""Certificate for K1588's profiled bounded-recentering exclusion."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1588-profiled-bounded-recentering-exclusion.json').read_text());q=d['bounded_recentering'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1588'),('bottoms','lambda_N^prof' in q['gaussian_bottom'] and 'E_N' in q['gaussian_bottom']),('gap','c_g N^(5/2)' in q['diverging_gap']),('translation invariant','translation-invariant' in q['diverging_gap']),('window','o(N^(5/2))' in q['recentering_exclusion']),('bounded included','O(1)' in q['recentering_exclusion']),('bottom diverges','-infinity' in q['recentering_exclusion']),('class preserved','K1577 remains exact' in q['class_compatibility']),('defect exit','K1582' in q['class_compatibility']),('subleading','N^(5/2)=o(N^4)' in q['leading_limit_open']),('true shift open','E_N+O(1)' in q['leading_limit_open']),('scope','not bounded-error recentering by the unknown true E_N' in q['scope_guard'])]
 c += [('gap decision',z['profiled_gaussian_gap_diverges']),('recentering excluded',z['profiled_bounded_error_recentering_excluded']),('class',z['wick_dominant_class_theorem_preserved']),('coefficient open',not z['unrestricted_leading_coefficient_identified']),('true recentering open',not z['true_ground_bounded_recentering_decided']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
