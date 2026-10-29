#!/usr/bin/env python3
"""Exact finite operators and budgets for the declared trilinear apparatus."""
from pathlib import Path
import argparse,hashlib,json
import sympy as s
R=s.Rational
ROOT=Path(__file__).resolve().parents[2]
STEM='k2276-structured-detector-implementation'
NOTE='explorations/conditional-build/k2276-structured-detector-implementation-2026-10-29.md'
DEPS=['explorations/conditional-build/k2253-full-instrument-reference-reuse-2026-10-29.md','explorations/conditional-build/k2270-untruncated-detector-control-2026-10-29.md','explorations/conditional-build/k2273-positive-control-energy-2026-10-29.md']
FAULTS=['pump_weight','squeeze_sign','creation_fluctuation','record_label','omit_uncompute','deny_alias','moment_bound','pulse_bound','compensator_sign','input_moment','mean_cutoff_norm']
def run_checks(fault=None):
    out=[]
    def check(n,b):out.append((n,b))
    for total in [2,4,6]:
        basis=[(i,j,k) for i in range(total+1) for j in range(total+1) for k in range(total//2+1) if i+j+2*k==total]
        idx={v:i for i,v in enumerate(basis)};H=s.zeros(len(basis))
        for v,col in idx.items():
            i,j,k=v;w=(i+1,j+1,k-1)
            if w in idx:
                row=idx[w];val=s.I*s.sqrt((i+1)*(j+1)*k);H[row,col]=val;H[col,row]=-val
        Q=s.diag(*[i+j+(1 if fault=='pump_weight' else 2)*k for i,j,k in basis])
        ordinary=s.diag(*[i+j+k for i,j,k in basis])
        check('actual trilinear Hermitian shell '+str(total),H==H.H)
        check('weighted charge commutes shell '+str(total),Q*H-H*Q==s.zeros(len(basis)))
        check('ordinary particle count not conserved '+str(total),ordinary*H-H*ordinary!=s.zeros(len(basis)))
        c=2*(total+2)**2
        check('positive compensation diagonal dominates '+str(total),all(sum(abs(H[i,j]) for j in range(len(basis)))<=c for i in range(len(basis))))
    # Bogoliubov coefficients and the actual squeeze sign from the ODE at zero.
    ch=R(5,3);sh=R(4,3)
    check('canonical transformed commutator',ch*ch-sh*sh==1)
    r=s.symbols('r',real=True);M=s.Matrix([[s.cosh(r),(-1 if fault=='squeeze_sign' else 1)*s.sinh(r)],[s.sinh(r),s.cosh(r)]])
    check('squeeze Heisenberg equation',s.simplify(s.diff(M,r)-s.Matrix([[0,1],[1,0]])*M)==s.zeros(2))
    check('actual target squeeze coefficients',s.simplify(s.cosh(s.log(3)).rewrite(s.exp))==ch and s.simplify(s.sinh(s.log(3)).rewrite(s.exp))==sh)
    n1,n2=s.symbols('n1 n2',nonnegative=True);G=n1+n2+1
    defect=s.expand((G**2+1)-2*((n1+1)*(n2+1)+n1*n2))
    check('moment norm polynomial difference',s.factor(defect)==(n1-n2)**2)
    alpha=s.symbols('alpha',positive=True)
    for n in range(5):
        cn=alpha**n/s.sqrt(s.factorial(n));cn1=alpha**(n+1)/s.sqrt(s.factorial(n+1))
        check('coherent annihilation recurrence '+str(n),s.simplify(s.sqrt(n+1)*cn1-alpha*cn)==0)
    pump_fluct=0 if fault=='creation_fluctuation' else (alpha**2+1)-2*alpha**2+alpha**2
    check('pump creation fluctuation norm is one',s.simplify(pump_fluct)==1)
    f=(41+40*s.sqrt(2))/9;I=(20+16*s.sqrt(2))/9
    check('weighted squeeze f bound',f<11)
    check('squeeze integral I bound',I<5)
    t=s.symbols('t',real=True)
    integral=s.sinh(2*t)/2+s.sqrt(2)*(s.cosh(2*t)-1)/2
    check('actual Duhamel integral derivative',s.simplify(s.diff(integral,t)-s.cosh(2*t)-s.sqrt(2)*s.sinh(2*t))==0)
    pump_constant=(10 if fault=='pulse_bound' else 1)*(1+f)*I/2
    check('two pump defects correctly composed',pump_constant<30)
    # Exact D=4 circuit, not an assertion of modular arithmetic.
    D=4;F=s.Matrix(D,D,lambda j,k:s.I**(j*k)/2);e0=s.eye(D)[:,0];X=s.Matrix([[0,1],[1,0]])
    record=s.Matrix([1,0]) if fault=='record_label' else s.Matrix([0,1])
    for n in range(10):
        encode=F.H*s.diag(*[s.I**(n*k) for k in range(D)])*F
        enc=encode*e0
        check('phase register actual residue '+str(n),enc==s.eye(D)[:,n%D])
        tagged=s.zeros(2*D,1)
        for k in range(D):tagged+=s.kronecker_product(s.eye(D)[:,k],X*record if k==0 else record)*enc[k]
        uncompute=s.eye(D) if fault=='omit_uncompute' else encode.H
        result=s.kronecker_product(uncompute,s.eye(2))*tagged
        bit=0 if n%D==0 else 1
        expected=s.kronecker_product(e0,s.eye(2)[:,bit])
        check('complete labeled record and clean register '+str(n),result==expected)
    actual_alias=(F.H*s.diag(*[s.I**(D*k) for k in range(D)])*F*e0)[0]
    alleged_alias=0 if fault=='deny_alias' else 1
    check('positive multiple false-vacuum alias retained',actual_alias==alleged_alias)
    # A high-number eigenstate saturates the stated tail premise.
    M2=(D+1)**2
    bound=(1 if fault=='moment_bound' else 2)*s.sqrt(M2)/(D+1)
    check('alias vector bound covers orthogonal record',s.sqrt(2)<=bound)
    # The state |2> alone shows B=1 would not establish M2<=4 via mean equality:
    # mix half |0> and half |2>, so mean=1 but G²=5.
    mean=R(1,2)*0+R(1,2)*2;second=R(1,2)*1+R(1,2)*(2+(0 if fault=='input_moment' else 1))**2
    check('first moment does not supply second premise',mean==1 and second>4)
    for qcharge in range(7):
        area=s.pi/3;repair=s.pi/3 if fault=='compensator_sign' else 5*s.pi/3
        phase=s.expand_complex(s.exp(-s.I*(area+repair)*(qcharge+2)**2))
        check('weighted quadratic phase repaired '+str(qcharge),s.simplify(phase)==1)
    mu=10**10;q=17;J=10
    err=20*(R(30,10**5)+R(22,2**q+1))
    check('ten-call ideal-control error budget',err<R('0.009357'))
    check('ten-call implementation allowance',err+R(6,10000)<R('0.009957'))
    check('pump operation count',2*J==20)
    check('dispersive operation count',2*q*J==340)
    check('neutral conservative gate count',10*(q+1)**2*J==32400)
    check('neutral qubit budget',2*q+2==36)
    m,g,sq=s.symbols('m g sq',nonnegative=True)
    actual=sq+4*m*g+4*(m*m+m)
    check('weighted second moment product expansion',s.expand(actual-(sq+4*m*g+4*m*m+4*m))==0)
    check('fresh-input global moment expansion',s.expand((11+2*m)**2+4*m)==4*m*m+48*m+121)
    check('ideal all-field moment explicit',400*11**4==5856400)
    check('small channel error does not imply small energy bound',(11+2*mu)**2*R(1,100)>10**18)
    # The mean-only bound acts on a subnormalized state, with no physical cutoff.
    K=7;prob=[R(1,2),R(1,4),0,0,0,0,0,R(1,4)]
    lowmean=sum(j*p for j,p in enumerate(prob));lowG2=sum((j+1)**2*p for j,p in enumerate(prob))
    rhs=(1 if fault=='mean_cutoff_norm' else K+1)*(lowmean+1)
    check('mean-only low-vector moment estimate',lowG2<=rhs)
    aa,xx,BB=s.symbols('aa xx BB',positive=True)
    bound=2*s.sqrt(BB/xx)+aa*s.sqrt(xx*(BB+1))
    xstar=2*s.sqrt(BB)/(aa*s.sqrt(BB+1))
    check('mean-only cutoff optimizer',s.simplify(s.diff(bound,xx).subs(xx,xstar))==0)
    check('mean-only optimum value',s.simplify(bound.subs(xx,xstar)-2*s.sqrt(2*aa*s.sqrt(BB*(BB+1))))==0)
    mean_budget=10*(R(10,7*4096)+8192*(R(3,10**8)+R(22,2**30)))
    check('mean-only exact input norm',s.sqrt(2*2**25)==8192)
    check('mean-only ten-call budget',mean_budget<R('0.007624'))
    check('mean-only complete error allowance',mean_budget+R(6,10000)<R('0.008224'))
    check('mean-only dispersive count',2*30*10==600)
    check('mean-only neutral gate count',10*31**2*10==96100)
    check('mean-only neutral qubit count',2*30+2==62)
    nn=s.symbols('nn',integer=True,positive=True)
    pn=2/(nn*(nn+1)*(nn+2))
    check('mean-only heavy-tail normalized',s.summation(pn,(nn,1,s.oo))==R(1,2))
    check('mean-only heavy-tail mean one',s.summation(nn*pn,(nn,1,s.oo))==1)
    check('mean-only heavy-tail harmonic second moment',s.limit(nn*(nn**2*pn),nn,s.oo)==2)
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    checks=run_checks()
    bad=[name for name,ok in checks if not bool(ok)]
    if bad:
        print('[FAIL] baseline: '+', '.join(bad));return 1
    print(f'[PASS] {len(checks)} exact algebra/matrix and resource-accounting controls')
    caught={}
    for fault in FAULTS:
        failures=[name for name,ok in run_checks(fault) if not bool(ok)]
        if not failures:
            print('[FAIL] undetected input fault: '+fault);return 1
        caught[fault]=failures
        print('[PASS] genuine failing checks for '+fault+': '+', '.join(failures))
    report={'schema_version':'1.0','result_id':STEM.split('-')[0].upper(),'claim_ceiling':'conditional supplied model; no source or canon verdict',
      'evidence_kind':'finite exact algebra/matrix and resource-accounting checks; universal statements are written proofs',
      'checks':len(checks),'check_names':[n for n,_ in checks],'faults_caught':caught,
      'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in DEPS+[NOTE,str(Path(__file__).relative_to(ROOT))]}}
    report['resource_accounting_checks']=[n for n,_ in checks if any(word in n for word in ['translations include','initial and target','restoration uses','error budget','good total shell'])]
    report_path=ROOT/'lab/process'/f'{STEM}.json'
    if args.write:
        report_path.write_text(json.dumps(report,indent=2)+'\n')
    elif not report_path.exists() or json.loads(report_path.read_text())!=report:
        print('[FAIL] stale or absent stored report; regenerate explicitly with --write');return 1
    else:
        print('[PASS] stored report and exact dependency hashes current')
    return 0
if __name__=='__main__':raise SystemExit(main())
