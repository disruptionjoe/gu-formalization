#!/usr/bin/env python3
"""Independent rational Gaussian moments and score projections.

Does not import the producer or its symbolic formulas to construct moments.
Finite controls verify algebra and declared scope, not the continuum theorem.
"""
import copy
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def gaussian(n):
    return F(0) if n % 2 else F(math.factorial(n), 2**(n//2)*math.factorial(n//2))


def moments(p, gap, variance):
    locations = [(p, -(1-p)*gap), (1-p, p*gap)]
    return [sum(weight * sum(F(math.comb(n, j))*location**(n-j)
                            *variance**(j//2)*gaussian(j)
                            for j in range(0, n+1, 2))
                for weight, location in locations) for n in range(7)]


def inverse(matrix):
    n = len(matrix)
    rows = [[F(x) for x in row]+[F(i==j) for j in range(n)]
            for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = rows[j][j]
        assert pivot > 0
        rows[j] = [x/pivot for x in rows[j]]
        for k in range(n):
            if k != j:
                factor = rows[k][j]
                rows[k] = [x-factor*y for x,y in zip(rows[k], rows[j])]
    return [row[n:] for row in rows]


def main():
    count = 0
    fixtures = 0
    def ck(value):
        nonlocal count
        assert value
        count += 1
    def inner(poly, other, M):
        return sum(c*d*M[n+m] for n,c in poly.items() for m,d in other.items())

    # General rare, balanced, reversed and high-separation Gaussian mixtures.
    for p in [F(1,10000),F(1,10),F(1,3),F(1,2),F(2,3),F(9,10),F(9999,10000)]:
        for gap,noise in [(F(1,10),F(1,7)),(F(2),F(1,100)),(F(10),F(1,3))]:
            fixtures += 1
            M = moments(p,gap,noise)
            S = M[2]; k3 = M[3]; k4 = M[4]-3*S*S
            k5 = M[5]-10*S*k3
            k6 = M[6]-15*M[4]*S-10*k3*k3+30*S**3
            ck(M[0]==1 and M[1]==0)
            ck(k5==k3*(1-12*p*(1-p))*gap*gap)
            q2={2:F(1),0:-S,1:-k3/S}
            q3={3:F(1),1:-3*S-k4/S,0:-k3}
            for q,cov in [(q2,k3/S),(q3,k4/S)]:
                ck(sum(c*M[n] for n,c in q.items())==0)
                ck(inner(q,{1:F(1)},M)==0)
                ck(-sum(n*c*M[n-1] for n,c in q.items() if n)==cov)
            A=inner(q2,q2,M); B=inner(q2,q3,M); C=inner(q3,q3,M)
            ck(A==2*S*S+k4-k3*k3/S)
            ck(B==6*S*k3+k5-k3*k4/S)
            ck(C==6*S**3+9*S*k4+9*k3*k3+k6-k4*k4/S)
            sigma=C-B*B/A
            ck(A>0 and sigma>0)
            excess=(k3/S)**2/A+(k4/S-(k3/S)*B/A)**2/sigma
            # Compare against a directly constructed degree1/2/3 score Gram.
            qs=[{1:F(1)},{2:F(1),0:-S},{3:F(1),1:-3*S,0:-k3}]
            gram=[[inner(q,u,M) for u in qs] for q in qs]
            ck(inverse(gram)[0][0]==1/S+excess)
            ck(excess>0)
            reverse=moments(1-p,gap,noise)
            ck(reverse[3]==-M[3] and reverse[4]==M[4] and reverse[6]==M[6])

    # Total variance1 keeps every standardized cumulant rational. Test the
    # explicit eventual bound with A>=1, sigma in[3,9], |B|<=8|alpha|.
    for p in [F(1,1000),F(1,6),F(1,2),F(5,6),F(999,1000)]:
        for gap in [F(1,2),F(1,5),F(1,20)]:
            fixtures += 1
            M=moments(p,gap,1-p*(1-p)*gap*gap)
            ck(M[2]==1)
            a=M[3];b=M[4]-3;d=M[5]-10*a;f=M[6]-15*M[4]-10*a*a+30
            A=2+b-a*a;B=6*a+d-a*b;C=6+9*b+9*a*a+f-b*b;sigma=C-B*B/A
            ck(A>=1 and 3<=sigma<=9 and abs(B)<=8*abs(a))
            projection=a*a/A+(b-a*B/A)**2/sigma
            coarse=a*a/2+b*b/18-a*a*abs(b)/2-F(64,3)*a**4
            ck(projection>=coarse)
            ck(d==a*(1-12*p*(1-p))*gap**2)

    # Elementary coercivity is global in the positive ratio, not a sample
    # of the putative optimal family. Cube to avoid irrational cube roots.
    values=[F(1,10000),F(1,10),F(1,2),F(1),F(2),F(10),F(10000)]
    for x in values:
        for y in values:
            m=min(x,2*y)
            ck(x+2*y==abs(x-2*y)+2*m)
            ck(m**3<=2*x*x*y)
    # Exact fourth-cumulant identity in a rational-radius chart.
    for n in [10,30,100,1000]:
        aa=1-F(1,n*n);bb=1+F(1,2*n*n);z=1-aa*aa;r=bb*bb-1;c=z*r;H=z-r
        root_t=1-F(1,n**3);t=root_t*root_t;v=1-t
        delta=2-(2-c)*t*t;p=r/(r+z);gap=root_t*(bb-aa)
        M=moments(p,gap,v);S=M[2];k4=M[4]-3*S*S
        ell=c*H/delta**2;Q=t*t*delta**2/((aa+bb)**4*S*S)
        ck(S==1-t*(1-c/(aa+bb)**2))
        ck(k4/S**2==Q*ell*(H-2*c/H))
        ck(c*c/delta**2==ell*c/H)
        ck(M[5]-10*S*M[3]==M[3]*t*(H*H-8*c)/(aa+bb)**2)

    # Fractional inverse coefficient is determined by its positive cube;
    # the integer coefficient follows independently after the B+2 shift.
    ck((F(3,8)**3)*4**5==3**3*2)
    ck(F(16)*(-F(6,5))==-F(96,5))
    ck(F(16)-F(96,5)==-F(16,5))
    for b,d in [(F(1,3),F(1,5)),(F(-2),F(5)),(F(0),F(1))]:
        ck((b-d)**2-(b*b/2-d*d)==(b-2*d)**2/2)

    payload=json.loads((ROOT/'lab/process/k1841-fisher-global-scaling.json').read_text())
    for path,digest in payload['inputs'].items():
        ck(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest)
    def report(value):
        result=value['results']
        assert result['global_compact_scaling_proved'] is True
        assert result['eventual_unique_global_shape_proved'] is True
        assert result['global_next_coefficients_proved'] is True
        assert result['effective_onset_proved'] is False
        assert result['all_q_uniqueness_proved'] is False
        assert result['arbitrary_near_minimizer_localization_proved'] is False
        assert result['GU_physics_claim'] is False
        assert result['stability_scope']=='fixed small convex (u,y) neighborhood only'
    report(payload)
    mutations=0
    for key in ['global_compact_scaling_proved','eventual_unique_global_shape_proved',
                'global_next_coefficients_proved','effective_onset_proved',
                'all_q_uniqueness_proved','arbitrary_near_minimizer_localization_proved',
                'GU_physics_claim','stability_scope']:
        changed=copy.deepcopy(payload)
        changed['results'][key]=('all shapes' if key=='stability_scope' else not changed['results'][key])
        try:
            report(changed)
        except AssertionError:
            mutations+=1
        else:
            raise AssertionError('reporting fault escaped')
    print('PASS K1841 probe',count,'independent rational controls;',fixtures,'mixture fixtures;',mutations,'reporting faults')


if __name__=='__main__':
    main()
