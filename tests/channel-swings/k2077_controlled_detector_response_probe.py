"""Independent matrix controls and genuine faults; not a continuum proof."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,math
import numpy as np
from scipy.linalg import expm
ROOT=Path(__file__).resolve().parents[2]
def norm(a):return np.linalg.norm(a,2)
def check(fault=None):
    count=0
    # Exact rational envelope, independently summing positive exponential series.
    from k2077_controlled_detector_response import produce
    data=produce()
    for row in data['resources']:
        a=row['effective_mass_gap'];l=math.isqrt(a);h=l+(l*l<a)
        e=sum((Q(a)**k/math.factorial(k) for k in range(81)),Q(0))
        eta=min(Q(1,2),(Q(2*h)+Q(27,8*l))/(2*e))
        lam=Q(row['integrated_control_norm']);want=min(Q(1),2*lam*eta,4*eta)
        assert Q(row['remote_record_tv_upper'])==want
        leak=Q(1,10**6);assert Q(row['conditional_upper_if_leakage_at_most_1e_6'])==min(Q(1),want+leak);count+=2
    # Finite separated supports: exact localized unitary difference, arbitrary projector.
    # These verify algebraic support transfer, not the Dirac continuum eta estimate.
    rng=np.random.default_rng(2077)
    for dim in [4,8,12]:
        EC=np.diag([1]*(dim//2)+[0]*(dim-dim//2));EG=np.eye(dim)-EC
        for _ in range(10):
            X=rng.normal(size=(dim,dim))+1j*rng.normal(size=(dim,dim));W=np.linalg.qr(X)[0];P=W[:,:dim//2]@W[:,:dim//2].conj().T
            X=rng.normal(size=(dim//2,dim//2))+1j*rng.normal(size=(dim//2,dim//2));V=np.zeros((dim,dim),complex);V[:dim//2,:dim//2]=(X+X.conj().T)/2
            U=expm(-1j*V);B=P@EG@P;delta=U-np.eye(dim);eta=norm(EG@P@EC);D=U.conj().T@B@U-B
            assert norm((np.eye(dim)-EC)@delta)<1e-12
            assert norm(U.conj().T@EG@U-EG)<1e-12
            assert norm(D)<=min(1,2*norm(delta)*eta,2*norm(V)*eta)+1e-11
            if fault=='exact_projected_causality':assert norm(D)<1e-12
            # Direct finite differences verify the interaction-picture derivative sign.
            dt=1e-6;der=(expm(1j*dt*V)@B@expm(-1j*dt*V)-expm(-1j*dt*V)@B@expm(1j*dt*V))/(2*dt)
            sign=-1 if fault=='duhamel_sign' else 1
            assert norm(der-sign*1j*(V@B-B@V))<1e-7
            count+=5
    # Small crossblock exposes a false quadratic tail replacing the linear eta bound.
    theta=1e-3;u=np.array([math.cos(theta),math.sin(theta)]);P=np.outer(u,u);B=P@np.diag([0.,1.])@P;U=np.diag([-1.,1.]);eta=abs(P[0,1]);D=U@B@U-B
    # Generic state with projection onto remote coordinate has response linear in crossblock.
    u=np.array([math.sin(theta),math.cos(theta)]);P=np.outer(u,u);B=P@np.diag([0.,1.])@P;D=U@B@U-B
    if fault=='quadratic_tail':assert norm(D)<=4*eta**2
    else:assert norm(D)<=4*eta and norm(D)>4*eta**2
    count+=1
    # Exact finite countermodel for postselection: commuting local remote click remains
    # invariant, global sector filter deletes the local branch. Continuum construction in note.
    P=np.diag([1.,0.,1.]);G=np.diag([0.,0.,1.]);U=np.array([[0,1,0],[1,0,0],[0,0,1.]])
    psi=np.array([1.,0.,1.])/math.sqrt(2);rho=np.outer(psi,psi);rr=U@rho@U.T
    n0=np.trace(rho@G);n=np.trace(rr@P@G@P);q=np.trace(rr@P)
    assert abs(n-n0)<1e-14 and abs(q-.5)<1e-14 and abs(n/q-n0-.5)<1e-14
    if fault=='condition_without_leakage':assert abs(n/q-n0)<=0
    if fault=='sector_record_local':assert abs(q-1)<1e-14
    # Separately test conditioning denominator and coarse-record TV on scalar probabilities.
    for q in [Q(1,10),Q(1,2),Q(9,10)]:
        for p0 in [Q(1,10),Q(1,2),Q(9,10)]:
            for n in [Q(0),q/2,q]:
                eps=abs(n-p0);actual=abs(n/q-p0)
                bound=eps+((1-q)**2 if fault=='square_leakage_probability' else 1-q)
                assert actual<=bound;count+=1
    # Spatial support is indispensable: a global internal readout can detect a local flip.
    H=np.array([[0.,1.],[1.,0.]]);M=np.diag([1.,0.]);J=expm(-1j*math.pi*H/2)
    if fault=='global_ancilla_locality':assert norm(J.conj().T@M@J-M)<1e-14
    else:assert norm(J.conj().T@M@J-M)>.99
    # Actual finite ancilla dilation: full outcome completeness and ideal qubit readout.
    Y=np.array([[0,-1j],[1j,0]]);A=np.diag([1.,0.]);initial=np.kron(np.eye(2),np.array([[1.],[0.]]))
    for chi in [0.,.2,.6,1.]:
        UU=expm(-1j*(math.pi/2)*chi*np.kron(A,Y));k0=UU[::2,:]@initial;k1=UU[1::2,:]@initial
        assert norm(k0.conj().T@k0+k1.conj().T@k1-np.eye(2))<1e-12
        assert norm(k1.conj().T@k1-math.sin(math.pi*chi/2)**2*A)<1e-12
        if fault=='exact_cutoff_readout' and chi==.2:assert norm(k1.conj().T@k1-A)<1e-12
        count+=2
    inst=data['bounded_ancilla_instrument'];tau=Q(inst['tail_norm_upper'])
    assert tau==Q(4,inst['core_radius_times_mass'])
    assert Q(inst['leakage_probability_upper'])==4*tau*tau
    assert Q(inst['record_tv_upper'])==4*tau*tau
    radius=inst['control_radius_times_mass'];T=inst['duration_times_mass']
    assert inst['click_input_radius_times_mass']==radius+T
    assert inst['spacelike_center_separation_times_mass']>2*radius+T
    if fault=='omit_causal_margin':assert radius==inst['core_radius_times_mass']+inst['ramp_width_times_mass']
    if fault=='bell_error_underestimate':assert Q(inst['two_copy_chsh_lower'])==Q(14,5)-16*tau*tau
    else:assert Q(inst['two_copy_chsh_lower'])==Q(14,5)-64*tau*tau>2
    count+=7
    return count
if __name__=='__main__':
    d=json.loads((ROOT/'lab/process/k2077-controlled-detector-response.json').read_text())
    for p,h in d['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    n=check();caught=[]
    for fault in ['exact_projected_causality','duhamel_sign','quadratic_tail','condition_without_leakage','sector_record_local','square_leakage_probability','global_ancilla_locality','exact_cutoff_readout','omit_causal_margin','bell_error_underestimate']:
        try:check(fault)
        except AssertionError:caught.append(fault)
        else:raise AssertionError('undetected '+fault)
    print('PASS',n,'independent resource/matrix/conditioning controls;',len(caught),'actual faults',caught)
