#!/usr/bin/env python3
"""Independent raw replay for K247."""
import json
from hashlib import sha256
from math import factorial
from flint import fmpq
from k230_order_six_permutation_projection_probe import raw_entries
from k242_order_six_third_shell_signed_taylor import coefficient_hash
from k243_order_six_budget_composition_q6_method_limit import PI_LOWER
from k244_order_six_exact_corner_shell_ladder import sinh_log
import k246_order_six_inner_cube_reallocation_probe as base
from k247_order_six_cumulative_q15_boundary import OUT, ORDER, QMAX, TAIL_START

def main():
    base.ORDER=ORDER; base.TAIL_START=TAIL_START
    m=json.loads(OUT.read_text()); groups=base.independent_groups(list(raw_entries())); polys=base.independent_polynomials(groups)
    assert len(groups)==307 and len(polys)==ORDER+1
    for i,p in enumerate(polys): assert coefficient_hash(p)==m['expansion']['degree_sha256'][str(i)]
    moments=base.independent_moments(QMAX); coefficients=[fmpq(0)]*9
    for p in polys:
        for i,v in enumerate(base.independent_integral(p,moments)): coefficients[i]+=v
    assert sha256(';'.join(map(str,coefficients)).encode()).hexdigest()==m['expansion']['integrated_log_polynomial_sha256']
    core=base.independent_tail(groups,QMAX); c=m['certificate']; assert str(core)==c['exact_core_tail_majorant']
    tail=fmpq(2**8*256**6,factorial(5))/PI_LOWER**8*sinh_log(QMAX)**8*core
    assert tail==base.row_value(c['normalized_tail_upper'])
    assert base.row_value(c['complete_lower'])>fmpq(1,10**21)
    assert m['decision']['result']=='cumulative_q15_prefix_exceeds_target__farther_signed_cancellation_unresolved'
    print('[PASS] K247 independent raw-orbit, moment, h22-tail replay')

if __name__=='__main__': main()
