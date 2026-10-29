#!/usr/bin/env python3
"""Exact finite controls for K2231; not a continuum proof or certificate writer."""
from fractions import Fraction as F
import json


def dot(x, y):
    return sum((a*b for a, b in zip(x,y)), F(0))


def quadratic(M, x):
    return sum((x[i]*M[i][j]*x[j] for i in range(len(x))
                for j in range(len(x))), F(0))/2


def matmul(M, N):
    return [[sum((M[i][k]*N[k][j] for k in range(len(N))),F(0))
             for j in range(len(N[0]))] for i in range(len(M))]


def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))


def det2(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]


def twice_integrate(poly):
    return {k+2:v/F((k+1)*(k+2)) for k,v in poly.items()}


def run(fault=None):
    checks = []
    def check(name, got, expected):
        checks.append((name, got == expected))
    f = [F(3,5), F(4,5)]
    A = [F(1), F(9)]
    K = [[a*b for b in f] for a in f]
    if fault == 'delete_bilocal_cross':
        K[0][1] = K[1][0] = F(0)
    L = [[K[0][0], F(0)], [F(0), K[1][1]]]
    if fault == 'inject_local_cross':
        L[0][1] = L[1][0] = F(1,7)
    plus, minus = [F(1),F(1)], [F(1),F(-1)]
    check('canonical_normalization',dot(f,f),F(1))
    check('target_polarization',quadratic(K,plus)-quadratic(K,minus),F(24,25))
    check('local_polarization',quadratic(L,plus)-quadratic(L,minus),F(0))
    check('q_energy_lower_bound',abs(K[0][1]-L[0][1])/3,F(4,25))
    check('p_energy_lower_bound',abs(K[0][1]-L[0][1]),F(12,25))
    free = [[F(1),F(0)],[F(0),F(9)]]
    target_total=[[K[i][j]+free[i][j] for j in range(2)] for i in range(2)]
    local_total=[[L[i][j]+free[i][j] for j in range(2)] for i in range(2)]
    check('retained_drift_cross', target_total[0][1]-local_total[0][1],F(12,25))
    invAf=[f[i]/A[i] for i in range(2)]
    sigma=dot(f, invAf)
    if fault == 'wrong_susceptibility':
        sigma=dot(f, [A[i]*f[i] for i in range(2)])
    check('susceptibility',sigma,F(97,225))
    for g, expected in [(F(3),F(3,25)),(F(4),F(-652,225))]:
        rem=4-g*g*sigma
        check('schur_remainder_'+str(g),rem,expected)
        q=[-g*z for z in invAf]
        full=dot(q,[A[i]*q[i] for i in range(2)])+2*g*dot(f,q)+4
        check('explicit_schur_vector_'+str(g),full,expected)
        for qtest in ([F(2),F(-1)],[F(-2,3),F(5,7)]):
            for x in (F(1), F(-2)):
                left=dot(qtest,[A[i]*qtest[i] for i in range(2)])+2*g*x*dot(f,qtest)+4*x*x
                shifted=[qtest[i]+g*x*invAf[i] for i in range(2)]
                right=dot(shifted,[A[i]*shifted[i] for i in range(2)])+rem*x*x
                check('square_completion',left,right)
    g=F(3)
    for qtest in ([F(1),F(0)],[F(1),F(1)],[F(2,3),F(-4,7)]):
        Q=dot(f,qtest)
        x=(g*Q/4 if fault == 'wrong_minimizer_sign' else -g*Q/4)
        eliminated=2*x*x+g*x*Q
        proposed=-g*g*Q*Q/8
        check('static_elimination',eliminated,proposed)
        completed=2*(x+g*Q/4)**2
        check('bilocal_completion_counterterm',completed,eliminated+g*g*Q*Q/8)
    D=[[F(1),F(0),g*f[0]],
       [F(0),F(9),g*f[1]],
       [g*f[0],g*f[1],F(4)]]
    if fault == 'omit_field_return':
        D[1][2]=F(0)
    D2=matmul(D,D)
    check('star_hamiltonian_symmetry',D[1][2],D[2][1])
    check('stable_star_determinant',det3(D),F(27,25))
    check('star_zero_second_order_cross',D[1][0],F(0))
    check('star_fourth_order_cross',D2[1][0],F(108,25))
    check('star_response_t4',D2[1][0]/24,F(9,50))
    # K(t)=sin(Omega*t)/Omega; coefficients and ODE are exact jet checks.
    kernel={1:F(1),3:F(-2,3),5:F(2,15)}
    check('retarded_kernel_initial_derivative',kernel[1],F(1))
    for power in (1,3):
        check('retarded_kernel_ode_'+str(power),
              F((power+2)*(power+1))*kernel[power+2]+4*kernel[power],F(0))
    memory_sign=F(-1) if fault == 'reverse_memory_sign' else F(1)
    # Convolve the leading t kernel with constant Q, then integrate q'' twice.
    memory_leading={2:memory_sign*g*g*f[0]*f[1]/2}
    response=twice_integrate(memory_leading)
    check('retarded_memory_t4',response[4],F(9,50))
    check('block_memory_agreement',response[4],D2[1][0]/24)
    Daux=[[F(5),F(-1)],[F(-1),F(5)]]
    Dinv=[[F(5,24),F(1,24)],[F(1,24),F(5,24)]]
    Fmul=[[f[0],F(0)],[F(0),f[1]]]
    correction=matmul(matmul(Fmul,Dinv),Fmul)
    if fault == 'collapse_distributed_rank':
        correction=[[a*b for b in f] for a in f]
    check('auxiliary_inverse',matmul(Daux,Dinv),[[F(1),F(0)],[F(0),F(1)]])
    check('distributed_correction_rank',det2(correction),F(6,625))
    check('distributed_cross',correction[0][1],F(1,50))
    check('distributed_q_diagonal',correction[0][0],F(3,40))
    schur=[[F(i==j)*A[i]-correction[i][j] for j in range(2)] for i in range(2)]
    check('distributed_schur_positive',schur[0][0]>0 and det2(schur)>0,True)
    check('sufficient_stability',max(f)**2<F(4),True)
    Dlocal=[[F(1),F(0),f[0],F(0)],
            [F(0),F(9),F(0),f[1]],
            [f[0],F(0),F(5),F(-1)],
            [F(0),f[1],F(-1),F(5)]]
    Dlocal2=matmul(Dlocal,Dlocal)
    Dlocal3=matmul(Dlocal2,Dlocal)
    check('distributed_no_two_edge_cross',Dlocal2[1][0],F(0))
    check('distributed_three_edge_cross',Dlocal3[1][0],F(-12,25))
    # This finite graph path control does not establish a strict continuum cone.
    return checks



FAULTS=['delete_bilocal_cross', 'inject_local_cross', 'wrong_susceptibility', 'wrong_minimizer_sign', 'omit_field_return', 'reverse_memory_sign', 'collapse_distributed_rank']


def main():
    import argparse, hashlib, json
    from pathlib import Path
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--controls-only',action='store_true')
    args=parser.parse_args()
    baseline=run()
    bad=[name for name,ok in baseline if not ok]
    if bad:
        raise AssertionError('FAIL baseline: '+repr(bad))
    detected={}
    for fault in FAULTS:
        # Exceptions propagate as errors; they never count as detection.
        checks=run(fault)
        failed=[name for name,ok in checks if not ok]
        if not failed:
            raise AssertionError('FAIL mutation escaped: '+fault)
        detected[fault]=failed
    root=Path(__file__).resolve().parents[2]
    deps=['explorations/conditional-build/k2228-continuum-energy-form-detector-control-2026-10-28.md', 'explorations/conditional-build/k2231-spatial-local-control-boundary-2026-10-29.md']
    target=root/'lab/process/k2231-spatial-local-control-boundary.json'
    report=dict(result='K2231',controls=[dict(name=n,passed=ok) for n,ok in baseline],faults=detected,
        evidence_kind='exact finite arithmetic/Clifford controls; universal proof is in the note',
        probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in deps})
    if not args.controls_only:
        if args.write: target.write_text(json.dumps(report,indent=2)+'\n')
        elif json.loads(target.read_text())!=report:
            raise AssertionError('FAIL stale certificate')
    print(json.dumps(dict(result='K2231',controls=len(baseline),faults={k:len(v) for k,v in detected.items()})))

if __name__=='__main__': main()
