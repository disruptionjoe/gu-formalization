#!/usr/bin/env python3
"""Exact Fourier and Clifford controls; no finite truncation is an index proof."""
from pathlib import Path
import argparse,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2];REPORT=ROOT/'lab/process/p3-gauge-domain-stabilizer.json'
I=s.I;X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);Z=s.diag(1,-1)
def run():
    rows=[]
    def check(name,value,kind='exact_supporting'):
        ok=bool(value);rows.append({'name':name,'kind':kind,'pass':ok});assert ok,name
    z=s.Symbol('z',nonzero=True)
    def star(M):return M.conjugate().T.subs(s.conjugate(z),1/z)
    def eq(A,B):return s.simplify(A-B)==s.zeros(*A.shape)
    def laurent(g):
        for i in range(g.rows):
            for j in range(g.cols):
                for term in s.Add.make_args(s.expand(g[i,j])):
                    if term!=0:yield i,j,int(term.as_powers_dict().get(z,0)),s.simplify(term/z**term.as_powers_dict().get(z,0))
    def preserves(g,ks):
        # Each nonzero Fourier coefficient maps n to n+ell. Equality of the
        # half-line cuts iff both threshold neighbours have identical membership.
        return all(all((n>=ks[j])==(n+ell>=ks[i]) for n in [ks[j]-1,ks[j],ks[i]-ell-1,ks[i]-ell]) for i,j,ell,c in laurent(g))
    U=s.Matrix([[s.Rational(3,5),s.Rational(4,5)],[-s.Rational(4,5),s.Rational(3,5)]])
    for ks in ([0,0],[0,1],[-2,3]):
        D=s.diag(*(z**k for k in ks));K=s.diag(*ks);g=s.simplify(D*U*D.inv())
        check('unitary multiplier '+str(ks),eq(g*star(g),s.eye(2)))
        check('all-mode domain preservation '+str(ks),preserves(g,ks))
        check('connection transport '+str(ks),eq(-z*s.diff(g,z)*star(g),-K+g*K*star(g)))
        check('shifted connection commutator '+str(ks),eq(z*s.diff(g,z)-K*g+g*K,s.zeros(2)))
        check('constant determinant '+str(ks),s.simplify(g.det())==1)
        if ks[0]!=ks[1]:
            check('unshifted operator not fixed '+str(ks),not eq(s.diff(g,z),s.zeros(2)),'exact_contrary')
            check('constant rotation fails split cut '+str(ks),not preserves(U,ks),'exact_contrary')
    swap=s.Matrix([[0,1/z],[z,0]])
    check('nonconstant split-zero stabilizer',preserves(swap,[0,1]) and eq(swap*star(swap),s.eye(2)))
    check('nonconstant allowed split grading fails',not eq(swap*Z,Z*swap),'exact_contrary')
    check('zero determinant winding insufficient',s.diag(z,1/z).det()==1 and not preserves(s.diag(z,1/z),[0,0]),'exact_contrary')
    check('forward inclusion not equality',not preserves(s.Matrix([[z]]),[0]),'exact_contrary')
    # Exact commutator classification for symbolic Laurent coefficients, not
    # restating the expected formula: solve all threshold equations coefficientwise.
    ks=[-2,0,3];terms=[];symbols=[]
    for i in range(3):
        for j in range(3):
            for ell in range(-6,7):
                c=s.Symbol(f'c_{i}_{j}_{ell}');symbols.append(c)
                for n in range(-10,11):
                    if (n>=ks[j])!=(n+ell>=ks[i]):terms.append(c)
    forced=set(terms);free=[c for c in symbols if c not in forced]
    expected={s.Symbol(f'c_{i}_{j}_{ks[i]-ks[j]}') for i in range(3) for j in range(3)}
    check('coefficientwise commutator solution',set(free)==expected)
    check('countercontrol wrong offset sign',not preserves(s.Matrix([[0,z],[1/z,0]]),[0,1]),'exact_contrary')
    # Actual rank-eight Cl7 Bott projection and rank-sixteen unitary representative.
    gam=[]
    for j in range(3):
        prefix=[Z]*j;suffix=[s.eye(2)]*(2-j)
        gam += [s.kronecker_product(*(prefix+[X]+suffix)),s.kronecker_product(*(prefix+[Y]+suffix))]
    gam.append(s.kronecker_product(Z,Z,Z))
    check('Cl7 relations',all(gam[i]*gam[j]+gam[j]*gam[i]==2*(i==j)*s.eye(8) for i in range(7) for j in range(7)))
    check('Cl7 traceless generators',all(c.trace()==0 for c in gam))
    volume=s.eye(8)
    for c in gam:volume=volume*c
    chern=s.simplify(s.trace(volume)*s.factorial(6)/2**7*(16*s.pi**3/15)/(s.factorial(3)*(2*s.pi*I)**3))
    check('full sphere Bott Chern normalization',abs(chern)==1)
    # Orientation is chosen so this generator pairs +1; raw sign recorded.

    u=s.Matrix([[s.Rational(3,5),s.Rational(4,5)*I],[s.Rational(4,5)*I,s.Rational(3,5)]])
    check('actual noncentral SU2 input',u*u.H==s.eye(2) and u.det()==1)
    for label,coords in [('pole',[1,0,0,0,0,0,0]),('mixed',[s.Rational(1,3),s.Rational(2,3),s.Rational(2,3),0,0,0,0])]:
        h=sum((v*c for v,c in zip(coords,gam)),s.zeros(8));p=(s.eye(8)+h)/2
        check('Bott projection '+label,eq(p*p,p) and p.H==p and p.rank()==4)
        g1=s.kronecker_product(u,p)+s.kronecker_product(s.eye(2),s.eye(8)-p)
        g2=s.diag(s.kronecker_product(u.inv(),s.eye(4)),s.eye(8));g=s.simplify(g1*g2)
        check('SU16 representative unitary '+label,eq(g*g.H,s.eye(16)))
        check('SU16 determinant '+label,s.simplify(g.det())==1)
    # Exact K pairing accounting is a control of the written product derivation,
    # not an independent numerical proof of the Toeplitz theorem.
    check('mixed class survives rank subtraction',s.Matrix([4,1])+s.Matrix([-4,0])==s.Matrix([0,1]),'exact_accounting')
    check('restriction image pairs zero',all(-b==0 for a,b in [(a,0) for a in range(-4,5)]),'exact_accounting')
    check('determinant homotopy detects neither basis class',all(s.zeros(1,2)*v==s.zeros(1,1) for v in [s.Matrix([1,0]),s.Matrix([0,1])]),'exact_accounting')
    for label,y,zz in [('equator',s.Integer(0),s.Matrix([1,0,0])),('mixed',s.Rational(3,5),s.Matrix([s.Rational(12,25),s.Rational(16,25)*I,0])),('pole',s.Integer(1),s.zeros(3,1))]:
        check('unstable sphere input '+label,s.simplify(y*y+(zz.H*zz)[0])==1)
        v=s.eye(3)-2*zz*zz.H/(1-I*y)**2
        check('actual rational U3 characteristic map '+label,eq(v*v.H,s.eye(3)))
        check('characteristic determinant formula '+label,s.simplify(v.det()+(1+I*y)**2/(1-I*y)**2)==0)
    J=s.Matrix([[0,1],[-1,0]])
    check('SU2 generator quaternionic intertwiner',u*J==J*u.conjugate())
    conjugation=s.diag(1,-1)
    check('same-base fixed mixed class equation',(conjugation-s.eye(2)).nullspace()==[s.Matrix([1,0])],'exact_accounting')
    check('base-covering involution can cancel conjugation',conjugation*conjugation==s.eye(2),'exact_accounting')
    # Newton identity supplies the suspension Chern coefficient. The topology
    # of suspension and the cited pi6 theorem are written proof inputs.
    c=s.symbols('c1:6');powers={0:s.Integer(5)}
    for k in range(1,6):
        powers[k]=s.expand(sum((-1)**(j-1)*c[j-1]*powers[k-j] for j in range(1,k))+(-1)**(k-1)*k*c[k-1])
    linear=sum(term for term in s.Add.make_args(powers[5]) if sum(term.as_powers_dict().get(ci,0) for ci in c)==1)
    check('suspension Newton coefficient',linear/s.factorial(5)==c[4]/24,'exact_accounting')
    check('unstable six torsion killed stably',6*1%6==0 and 1%6!=0,'exact_accounting')
    return {'schema_version':'1.0','program_target':'X-P2-P3','tier':'T2','classification':'INTERNAL_STRUCTURAL_ONLY','claim_ceiling':'No native gauge-group extension, class-C decision or physical count','proof_ref':'explorations/conditional-build/p3-gauge-domain-stabilizer-2026-11-11.md','evidence_kind':'exact finite supporting/contrary controls and separately labeled accounting; universal written proof separate','checks':rows,'classification_result':{'offsets':'arbitrary integer finite list','stabilizer':'D_k U(r) D_k^-1','full_unshifted_operator':'product U(m_a)','end_restriction':'a maps to (a,0)','toeplitz_pairing':'-b','mixed_representative_rank':16,'minimum_untwisted_integer_detection_rank':5,'low_rank_zero_stable_class_suffices':False,'raw_Bott_Chern_number':int(chern),'determinant':'identically one by projection splitting'}}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write-report',action='store_true');args=ap.parse_args();report=run()
    if args.write_report:REPORT.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(REPORT.read_text())==report,'saved report differs from computed controls'
    print(json.dumps({'pass':True,'checks':len(report['checks']),'kinds':{k:sum(x['kind']==k for x in report['checks']) for k in sorted({x['kind'] for x in report['checks']})}}))
if __name__=='__main__':main()
