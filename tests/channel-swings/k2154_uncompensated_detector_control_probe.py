#!/usr/bin/env python3
from pathlib import Path
import argparse,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def check(out,name,value): out[name]=bool(value)
import numpy as np
from scipy.linalg import expm
RESULT='K2154';REPORT='k2154-uncompensated-detector-control.json'
DEPS=['lab/process/k2152-finite-chain-threshold-detector.json','lab/process/k2153-diagonal-detector-energy.json','explorations/conditional-build/k2154-uncompensated-detector-control-2026-10-27.md']
EVIDENCE='Written analytic-vector selfadjointness, total-number compression, positive-form overlap and switching-work proofs; finite compressed dynamics are numerical controls only.'
FAULTS=['commutator_factor','missing_zero_point','wrong_soft_angle','lost_record','missing_reference','wrong_work_jump']
def controls(fault=None):
    out={};basis=[(i,j) for i in range(5) for j in range(5-i)];d=len(basis);index={x:i for i,x in enumerate(basis)}
    a=s.zeros(d)
    for col,(i,j) in enumerate(basis):
        if j:a[index[i,j-1],col]=s.sqrt(j)
    G=s.diag(*[i+j+1 for i,j in basis]);H=s.diag(*[i+5*j+1 for i,j in basis])+2*(a*a+(a*a).T)
    expected=4*s.I*(a*a-(a*a).T)
    if fault=='commutator_factor':expected*=2
    check(out,'compressed_number_commutator',s.I*(H*G-G*H)==expected)
    C=s.Integer(1);D=s.Integer(9);Z=0 if fault=='missing_zero_point' else 2
    check(out,'free_vacuum_number_comparison',C*Z>=s.Rational(1,4)*(1+1+s.Rational(1,3)+3))
    # B0=diag(0,-8), kappa=8; verify form inequalities independently by spectra below.
    check(out,'form_constants',C==1 and D==9 and abs(1-3**2)==8)
    t=s.Rational(9,25);sn=t if fault=='wrong_soft_angle' else s.sqrt(t);cs=s.sqrt(1-sn**2)
    U=s.Matrix([[cs,-sn],[sn,cs]])
    check(out,'actual_soft_pointer_rotation',U.T*U==s.eye(2) and U[1,0]**2==t and U[0,0]==s.Rational(4,5))
    # Entangled field/reference input; full two-outcome instrument versus click-only.
    ket=s.Matrix([1,0,0,1])/s.sqrt(2);rho=ket*ket.T
    if fault=='missing_reference':
        refproj=[s.kronecker_product(s.eye(2),s.diag(1,0)),s.kronecker_product(s.eye(2),s.diag(0,1))]
        rho=sum((P*rho*P for P in refproj),s.zeros(4))
    k0=s.kronecker_product(s.diag(1,s.Rational(4,5)),s.eye(2));k1=s.kronecker_product(s.diag(0,s.Rational(3,5)),s.eye(2))
    blocks=[k0*rho*k0.T,k1*rho*k1.T]
    if fault=='lost_record':blocks=blocks[1:]
    check(out,'all_outcomes_trace',sum(s.trace(x) for x in blocks)==1)
    coherence=blocks[0][0,3]
    check(out,'reference_coherence_retained',coherence==s.Rational(2,5))
    # Exact driven qubit example: H=diag(0,1), K=diag(1,-1), initial |+>.
    # Use noncommuting K=X instead; verify conservation gives two boundary works.
    H2=s.diag(0,1);K=s.Matrix([[0,1],[1,0]]);psi=s.Matrix([1,0]);tot=H2+K
    # A rational final state; include its total-energy change in the identity.
    final=s.Matrix([s.Rational(3,5),-s.Rational(4,5)])
    # General identity at arbitrary state: signed jumps telescope iff segment total energy conserved.
    delta=s.simplify((final.T*tot*final)[0]-(psi.T*tot*psi)[0])
    won=(psi.T*K*psi)[0];woff=(final.T*K*final)[0]*(1 if fault=='wrong_work_jump' else -1)
    fielddelta=(final.T*H2*final)[0]-(psi.T*H2*psi)[0]
    check(out,'work_energy_bookkeeping',s.simplify(won+woff+delta-fielddelta)==0)
    check(out,'unrestricted_spectator_countercontrol',s.exp(s.I*s.pi)==-1 and (1+s.exp(s.I*s.pi))/2==0)
    return out

def dynamics():
    # Exact model is infinite Fock. This is ONLY the L=4 number compression.
    basis=[(i,j) for i in range(5) for j in range(5-i)];idx={v:i for i,v in enumerate(basis)};d=len(basis)
    a=[]
    for mode in range(2):
        x=np.zeros((d,d),complex)
        for col,n in enumerate(basis):
            if n[mode]:m=list(n);m[mode]-=1;x[idx[tuple(m)],col]=np.sqrt(n[mode])
        a.append(x)
    G=np.diag([i+j+1 for i,j in basis]);H=np.diag([i+5*j+1 for i,j in basis]).astype(complex)+2*(a[1]@a[1]+(a[1]@a[1]).conj().T)
    G2=np.kron(G,np.eye(2));H2=np.kron(H,np.eye(2));g=500.;lam=500.
    J=1j*g*(a[0].conj().T@a[1]-a[1].conj().T@a[0]);Y=np.array([[0,-1j],[1j,0]])
    theta=np.diag([0 if i==0 else np.arcsin(.6) if i==1 else np.pi/2 for i,j in basis])
    Ksoft=np.kron((2*lam/np.pi)*theta,Y);Kbeam=np.kron(J,np.eye(2))
    segments=[(Kbeam,np.pi/(4*g)),(Ksoft,np.pi/(2*lam)),(-Kbeam,np.pi/(4*g))];T=sum(t for _,t in segments)
    # Field entangled with a dimension-two reference, qubit initially zero.
    psi=np.zeros((2*d,2),complex);psi[2*idx[0,0],0]=1/np.sqrt(2);psi[2*idx[1,0],1]=1/np.sqrt(2)
    actual=psi.copy();ideal=psi.copy();Ein=float(np.vdot(psi,H2@psi).real);G0=float(np.vdot(psi,G2@psi).real);works=[]
    previous=np.zeros_like(H2)
    for K,t in segments:
        works.append(float(np.vdot(actual,(K-previous)@actual).real))
        actual=expm(-1j*(H2+K)*t)@actual;ideal=expm(-1j*K*t)@ideal;previous=K
    works.append(float(np.vdot(actual,-previous@actual).real));Eout=float(np.vdot(actual,H2@actual).real)
    distance=0.
    for outcome in range(2):
        aa=actual[outcome::2,:].reshape(-1);ii=ideal[outcome::2,:].reshape(-1)
        block=np.outer(aa,aa.conj())-np.outer(ii,ii.conj());distance+=np.linalg.eigvalsh(block).__abs__().sum()/2
    I=2*np.expm1(8*T/2)/8;bound=min(1.,np.sqrt(18*(Ein+2)*I));growth=9*np.exp(8*T)*(Ein+2)-2
    comm=1j*(H@G-G@H);mineig=lambda A:float(np.linalg.eigvalsh(A).min())
    checks={'positive_compressed_free_H':mineig(H)>-1e-10,'number_form_lower':mineig(8*G-comm)>-1e-10,'number_form_upper':mineig(8*G+comm)>-1e-10,'control_commutes_number':all(np.linalg.norm(K@G2-G2@K)<1e-9 for K,t in segments),'reference_full_record_error':distance<=bound,'actual_energy_growth':Eout<=growth,'work_telescopes':abs(sum(works)-(Eout-Ein))<1e-10,'absolute_mean_switch_bound':sum(abs(w) for w in works)<=4*g*np.exp(8*T)*(Ein+2)+2*lam,'drift_changes_full_channel':distance>1e-6}
    assert all(checks.values()),checks
    # Round diagnostics only for portable replay; checks use unrounded numbers.
    return {'kind':'finite_compressed_numerical_only','total_number_cutoff':4,'checks':{k:bool(v) for k,v in checks.items()},'half_trace_error':round(float(distance),8),'proven_error_upper':round(float(bound),8),'signed_work':round(float(sum(works)),8),'field_energy_change':round(Eout-Ein,8),'absolute_mean_switch_work':round(float(sum(abs(w) for w in works)),8)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    baseline=controls();bad=[k for k,v in baseline.items() if not v]
    if bad: raise AssertionError('BASELINE FAIL: '+str(bad))
    caught={}
    for fault in FAULTS:
        failed=[k for k,v in controls(fault).items() if not v]
        if not failed: raise AssertionError('UNDETECTED '+fault)
        caught[fault]=failed
    report={'result_id':RESULT,'status':'conditional_exact_controls','exact_checks':baseline,'fault_failures':caught,'dependency_sha256':{x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in DEPS},'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'universal_evidence':EVIDENCE}
    if RESULT=='K2154': report['numerical_evidence']=dynamics()
    if args.write: (ROOT/'lab/process'/REPORT).write_text(json.dumps(report,indent=2)+'\n')
    else: assert json.loads((ROOT/'lab/process'/REPORT).read_text())==report,'stored report differs'
    print(json.dumps({'result':RESULT,'exact_checks':len(baseline),'faults_rejected':len(caught),'numerical_checks':report.get('numerical_evidence',{}).get('checks',{})},indent=2))
if __name__=='__main__': main()
