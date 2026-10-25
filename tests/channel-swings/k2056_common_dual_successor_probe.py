"""Separate small-matrix and antilinear-vector replay; imports no producer.

Spin factors are signed column maps formed by tensor-factor action, copy
identities use dense rational matrices, and actual conjugation acts on real/
imaginary vector pairs. No full raw or graph matrix is assembled.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import json
from itertools import permutations

ROOT = Path(__file__).resolve().parents[2]


def mm(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), Q(0)) for j in range(len(b[0]))] for i in range(len(a))]


def sc(c, a):
    return [[c*x for x in row] for row in a]


def plus(a, b):
    return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]


def tr(a):
    return [list(row) for row in zip(*a)]


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def det(a):
    a = [row[:] for row in a]; d = Q(1)
    for k in range(len(a)):
        pivot = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]; d = -d
        p = a[k][k]; d *= p
        for i in range(k+1, len(a)):
            q = a[i][k] / p
            for j in range(k+1, len(a)):
                a[i][j] -= q*a[k][j]
    return d


def mv(a, x):
    return [sum((v*w for v,w in zip(row,x)), Q(0)) for row in a]


def anti(r, xy, conjugate=True):
    # A=iR. iR conjugate(x+iy)=R y+iR x.
    x,y = xy
    return mv(r, y) if conjugate else mv(sc(-1,r),y), mv(r,x)


def tensor_generator(k):
    slot = k % 7
    result = []
    for column in range(128):
        bits = [(column >> (6-i)) & 1 for i in range(7)]
        sign = 1
        for i in range(slot):
            sign *= 1 if bits[i] == 0 else -1  # tensor Z
        if k >= 7:
            sign *= -1 if bits[slot] == 0 else 1  # [[0,1],[-1,0]]
        bits[slot] = 1-bits[slot]
        result.append((sum(bit << (6-i) for i,bit in enumerate(bits)), sign))
    return result


def compose(a,b):
    return [(a[j][0], sign*a[j][1]) for j,sign in b]


def word(gs):
    result = [(i,1) for i in range(128)]
    for g in gs:
        result = compose(result,g)
    return result


# Independently represent a complex matrix by separate real/imaginary matrices.
def zr(a):
    return a,sc(0,a)


def zc(a):
    return a[0],sc(-1,a[1])


def zt(a):
    return tr(a[0]),tr(a[1])


def zd(a):
    return zt(zc(a))


def zn(a):
    return sc(-1,a[0]),sc(-1,a[1])


def zi(a):
    return sc(-1,a[1]),a[0]


def zm(a,b):
    return plus(mm(a[0],b[0]),sc(-1,mm(a[1],b[1]))),plus(mm(a[0],b[1]),mm(a[1],b[0]))


def zdet(a):
    n=len(a[0]);total=(Q(0),Q(0))
    for perm in permutations(range(n)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        value=(Q(sign),Q(0))
        for i,j in enumerate(perm):
            x,y=value;u,v=a[0][i][j],a[1][i][j]
            value=(x*u-y*v,x*v+y*u)
        total=(total[0]+value[0],total[1]+value[1])
    return total


def leading_positive(a):
    for n in range(1,len(a[0])+1):
        minor=([row[:n] for row in a[0][:n]],[row[:n] for row in a[1][:n]])
        real,imag=zdet(minor)
        if imag or real<=0:
            return False
    return True


def mathematics(fault=None):
    checks = 0
    def ck(ok, name):
        nonlocal checks
        assert ok, name
        checks += 1
    gs = [tensor_generator(k) for k in range(14)]
    volume = word(gs); b = word(gs[7:]); g = compose(b,gs[0])
    ck(compose(g,g) == [(i,-1) for i in range(128)], 'spin square')
    ck(all(g[g[i][0]][1] == -g[i][1] for i in range(128)), 'spin skew')
    ck(all(volume[i][0] == i for i in range(128)), 'diagonal volume')
    wb = [Q(3+volume[i][1],2) for i in range(128)]
    ck(wb.count(1) == wb.count(2) == 64, 'both actual half weights')
    ck(all(wb[i] == wb[g[i][0]] for i in range(128)), 'spin weight commutation')
    c = [[Q(10 if i==j==0 else 4 if i==0 or j==0 else int(i!=j)) for j in range(11)] for i in range(11)]
    p2 = [[Q(1) if i==j==0 else Q(1,10) if i>0 and j>0 else Q(0) for j in range(11)] for i in range(11)]
    pp = plus(eye(11),sc(-1,p2)); c2=mm(c,p2)
    ck(mm(p2,p2)==p2, 'copy projection')
    ck(mm(c,pp)==sc(-1,pp), 'transverse copy eigenvalue')
    ck(mm(c2,c2)==plus(sc(19,c2),sc(70,p2)), 'copy polynomial')
    num=plus(sc(19,c2),sc(139 if fault=='absolute_numerator' else 140,p2))
    ck(mm(num,num)==sc(641,mm(c2,c2)), 'positive absolute copy square')
    ck(25*25<641<26*26, 'exact root bracket')
    j=[[Q(0),Q(1)],[Q(-1),Q(0)]]; i2=eye(2)
    xy=([Q(2,3),Q(-5,7)],[Q(11,13),Q(17,19)])
    for w in (Q(1),Q(2)):
        t=sc(w,j); ti=sc(-1/w,j)
        p=sc(Q(1) if fault=='drop_half_weight' else w,i2)
        r=sc(1 if fault=='kinetic_i_sign' else -1,mm(ti,p))
        ck(mm(tr(r),t)==p, 'kinetic i sign')
        ck(mm(mm(p,ti),p)==sc(-1,t), 'anti-involution classification')
        got=anti(r,anti(r,xy,conjugate=fault!='omit_conjugation'),conjugate=fault!='omit_conjugation')
        ck(got==([-x for x in xy[0]],[-y for y in xy[1]]), 'actual antilinear square')
        ck(mm(ti,ti)==sc(-1/(w*w),i2), 'identity-P distinction')
        # r=J, r^-1=-J; inverse-domain map c=i r^-1 conjugation.
        ri=sc(1 if fault=='dual_inverse_sign' else -1,r)
        ck(anti(ri,anti(r,xy))==xy and anti(r,anti(ri,xy))==xy, 'distinct dual inverse maps')
    pd=[[Q(1),Q(0)],[Q(0),Q(-1)]]; rd=mm(j,pd)
    ck(mm(tr(rd),j)==pd, 'indefinite kinetic coefficient')
    expected=sc(-1 if fault=='indefinite_generalization' else 1,i2)
    ck(mm(rd,rd)==expected, 'indefinite P escapes positive premise')
    # Genuinely noncommuting positive P in four dimensions.
    ti=[[Q(0),Q(-1),Q(0),Q(0)],[Q(1),Q(0),Q(0),Q(0)],
        [Q(0),Q(0),Q(0),Q(-1,2)],[Q(0),Q(0),Q(1,2),Q(0)]]
    s=[[Q(1),Q(1),Q(0),Q(0)],[Q(0),Q(1),Q(1),Q(0)],
       [Q(0),Q(0),Q(1),Q(1)],[Q(0),Q(0),Q(0),Q(1)]]
    d=[[Q(i+1) if i==j else Q(0) for j in range(4)] for i in range(4)]
    p=mm(tr(s),mm(d,s)); z=mm(ti,p)
    ck(mm(ti,p)!=mm(p,ti), 'noncommuting control')
    neg=mm(tr(z),mm(p,z))
    ck(neg==sc(-1,mm(p,mm(z,z))), 'negative square congruence')
    ck(all(det([row[:n] for row in p[:n]])>0 for n in range(1,5)), 'P positive Sylvester minors')
    ck(all(det([row[:n] for row in neg[:n]])>0 for n in range(1,5)), 'negative square positive congruence minors')
    # Non-real Hermitian P on BOTH actual two-plane weights.
    for w in (Q(1),Q(2)):
        pz=(sc(w,[[Q(2),Q(0)],[Q(0),Q(1)]]),sc(w,j))
        tz=zr(sc(w,j));tiz=zr(sc(-1/w,j))
        az=zn(zi(zm(tiz,pz if fault=='omit_P_transpose' else zc(pz))))
        ck(zd(pz)==pz and leading_positive(pz), 'non-real Hermitian positive P')
        ck(zdet(pz)==(w*w,Q(0)), 'exact complex determinant')
        ck(zm(zt(az),tz)==zi(pz), 'Hermitian kinetic transpose')
        ck(zm(az,zc(az))==zn(zr(i2)), 'Hermitian bar square')
        lhs=zm(zm(pz if fault=='criterion_missing_conjugate' else zc(pz),tiz),pz)
        ck(lhs==zn(tz), 'Hermitian minus-one criterion')
        # Arbitrary Hermitian 2x2 determinant identity, not only det=w^2.
        pp=(sc(2,pz[0]),sc(2,pz[1]));aa=zn(zi(zm(tiz,zc(pp))))
        ck(zm(aa,zc(aa))==zr(sc(-4,i2)), 'two-plane determinant square law')
    # A rational Hermitian positive C is the actual square root of P=C^2.
    cr=[[Q(i+4) if i==j else Q(0) for j in range(4)] for i in range(4)]
    ci=sc(0,cr);cr[0][2]=cr[2][0]=Q(1)
    ci[0][1]=ci[2][3]=Q(1);ci[1][0]=ci[3][2]=Q(-1)
    cz=(cr,ci);pz=zm(cz,cz);tiz=zr(ti)
    ck(zd(cz)==cz and leading_positive(cz), 'positive complex square root C')
    ck(zd(pz)==pz and leading_positive(pz) and pz[1]!=sc(0,pz[1]), 'genuine non-real P=C squared')
    mz=zm(zm(cz,tiz),zc(cz))
    ck(zt(mz)==zn(mz), 'complex skew M transpose')
    gram=zm(mz,zd(mz));negative=gram if fault=='skew_gram_sign' else zn(gram)
    ck(zm(mz,zc(mz))==negative, 'complex skew gives negative Hermitian Gram')
    az=zn(zi(zm(tiz,zc(pz))));square=zm(az,zc(az))
    ck(zm(cz,square)==zm(negative,cz), 'actual Hermitian similarity identity without inverse')
    ck(leading_positive(gram), 'strict positive Gram minors')
    return checks


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=ROOT)
    ap.add_argument('--report',type=Path);args=ap.parse_args()
    baseline=mathematics()  # All mathematical mutations follow a green baseline.
    faults=['kinetic_i_sign','omit_conjugation','absolute_numerator','drop_half_weight','dual_inverse_sign','indefinite_generalization','omit_P_transpose','criterion_missing_conjugate','skew_gram_sign']
    for fault in faults:
        try:
            mathematics(fault)
        except AssertionError:
            pass
        else:
            raise AssertionError('unrejected mathematical fault '+fault)
    report=json.loads((args.report or args.root/'lab/process/k2056-common-dual-successor.json').read_text())
    assert report['result_id']=='K2056' and report['target_claim']=='NONE-NOT-A-KILL'
    assert report['copy_data']['other_polynomial']==[1,-19,-70]
    assert report['copy_data']['absolute_numerator']==[19,140]
    assert [x['P_I_bar_square'] for x in report['half_controls']]==['-1','-1/4']
    assert [x['determinant'] for x in report['complex_controls']]==['1','4']
    assert report['identities']['minus_one_criterion']=='conjugate(P) T^-1 P=-T'
    for path,digest in report['inputs'].items():
        assert hashlib.sha256((args.root/path).read_bytes()).hexdigest()==digest
    print('PASS K2056 probe:',baseline,'independent exact checks;',len(faults),'mathematical faults rejected; report/provenance checks separate')


if __name__=='__main__':
    main()
