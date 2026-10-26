"""Exact finite operator/state controls; universal claims rest on the linked written proof."""
import sympy as s

def check(value,msg):
    if not bool(value): raise AssertionError(msg)
def zero(M): return all(s.simplify(x)==0 for x in M)
def annihilator(n,j):
    A=s.zeros(2**n)
    for mask in range(2**n):
        if mask&(1<<j): A[mask^(1<<j),mask]=(-1)**sum((mask>>k)&1 for k in range(j))
    return A
def lift(H):
    n=H.rows; a=[annihilator(n,j) for j in range(n)];D=s.zeros(2**n)
    for i in range(n):
        for j in range(n):D+=H[i,j]*a[i].T*a[j]
    return D
def distance(D):return s.simplify(sum(abs(e)*m for e,m in D.eigenvals().items())/2)
def harness(test,faults):
    test(None);print('PASS clean exact baseline')
    for fault in faults:
        try:test(fault)
        except AssertionError as exc:print('DETECTED',fault,str(exc))
        else:raise AssertionError('undetected fault '+fault)
    print('PASS',len(faults),'genuine input/state/gate faults; finite controls are not universal proofs')

# Exact exterior-power lift of a one-particle permutation includes occupied-mode signs.
def exterior(U):
    n=U.rows;M=s.zeros(2**n)
    for a in range(2**n):
      ia=[i for i in range(n) if a&(1<<i)]
      for b in range(2**n):
        ib=[i for i in range(n) if b&(1<<i)]
        if len(ia)==len(ib):M[a,b]=U.extract(ia,ib).det() if ia else 1
    return M

def evolve(code,fault=None):
    P=s.zeros(4);P[2,0]=P[0,2]=P[3,1]=P[1,3]=1
    C=exterior(P)
    if fault=='unsigned_fermionic_swap':C=C.applyfunc(abs)
    # signal modes0,1 and memories2,3, plus ordinary binary pointer.
    v=C[:,code];out={}
    for mask,amp in enumerate(v):
        if amp==0:continue
        bits=(mask>>2)&3;record=int(bits.bit_count()==1)
        if fault=='wrong_coarse_record':record=int(bits!=0)
        if fault=='omit_capture_readout':record=int((mask&3).bit_count()==1)
        flag=bits if fault=='refined_readout' else 0
        for final,amp2 in enumerate(C[:,mask]):
            if amp2!=0:out[(final,record,flag)]=amp*amp2
    return out

def cp(v,w):
    out=s.zeros(8)
    for (a,p,fl),x in v.items():
      for (b,q,fr),y in w.items():
        if p==q and fl==fr and a>>2==b>>2:out[2*(a&3)+p,2*(b&3)+q]+=x*s.conjugate(y)
    return out

def test(fault):
    vs=[evolve(i,fault) for i in range(4)]
    for i in range(4):
      for j in range(4):
        expected=s.zeros(8);ri=int(i.bit_count()==1);rj=int(j.bit_count()==1)
        if ri==rj:expected[2*i+ri,2*j+rj]=1
        check(zero(cp(vs[i],vs[j])-expected),'full recorded instrument matrix unit '+str((i,j)))
    # Independently demand genuine exterior signs, even though a double sign error can cancel.
    P=s.zeros(4);P[2,0]=P[0,2]=P[3,1]=P[1,3]=1;C=exterior(P)
    if fault=='unsigned_fermionic_swap':C=C.applyfunc(abs)
    a=[annihilator(4,j) for j in range(4)]
    for j in range(4):
        target=sum((P[i,j]*a[i] for i in range(4)),s.zeros(16))
        check(zero(C*a[j]*C.T-target),'actual CAR automorphism at capture')
    coarse=s.zeros(8);fine=s.zeros(8)
    for i in [0,3]:
      for j in [0,3]:
        coarse+=cp(evolve(i),evolve(j))/2
        fine+=cp(evolve(i,'refined_readout'),evolve(j,'refined_readout'))/2
    check(distance(coarse-fine)==s.Rational(1,2),'coarse versus refined coherent-pair witness')
    # Nonreducing two-dimensional selected space: actual h, all residual singular values.
    A=s.Matrix([[3,s.Rational(1,5)],[s.Rational(1,5),3]])
    B=s.diag(s.Rational(3,5),s.Rational(4,5));Cq=s.diag(4,5)
    h=A.row_join(B.T).col_join(B.row_join(Cq))
    href=s.diag(A,Cq);V=h-href
    check(sorted(V.eigenvals().keys(),key=float)==[-s.Rational(4,5),-s.Rational(3,5),s.Rational(3,5),s.Rational(4,5)],'leakage signed singular spectrum')
    DF=lift(V);check(max(DF.eigenvals().keys())==s.Rational(7,5),'full Fock trace-norm residual')
    # An idle spectator really enters L at first derivative; cannot omit idle interval.
    idle_ref=h if fault=='omit_idle_residual' else href
    q=s.Matrix([0,0,1,0]);residual=(h-idle_ref)*q
    check(zero(residual-s.Matrix([s.Rational(3,5),0,0,0])),'actual inactive spectator drift')
    Amem=s.zeros(2) if fault=='wrong_memory_drift' else A
    D0=s.diag(A,Amem);couple=s.zeros(4)
    for j in range(2):couple[j,j+2]=couple[j+2,j]=1
    check(zero(D0*couple-couple*D0),'copied matrix memory commutes with exchange')
    # Exact resonant comparison swap, including non-diagonal A and correcting memory rotation.
    T=s.pi/2;EA=s.exp(-3*s.I*T)*(s.cos(T/5)*s.eye(2)-s.I*s.sin(T/5)*s.Matrix([[0,1],[1,0]]))
    U=-s.I*s.diag(EA,EA)*couple
    correction=s.diag(s.eye(2),s.I*EA.conjugate().T)
    for j in range(2):
        col=s.eye(4)[:,j];target=s.eye(4)[:,j+2]
        check(zero(correction*U*col-target),'entire selected-subspace capture with internal mixing')

    # Cutoff-like physical smear with both energy signs, in actual sea excitation representation.
    ap=annihilator(3,0);ah=annihilator(3,1);dm=annihilator(3,2)
    cp0=s.Rational(3,5);ch0=s.Rational(4,5);gg=s.Rational(2,3)
    br=cp0*ap+ch0*ah.T
    if fault=='omit_cutoff_hole':br=cp0*ap
    VR=gg*(dm.T*br+br.conjugate().T*dm);Videal=gg*(dm.T*ap+ap.T*dm)
    residual=VR-Videal;ev=residual.eigenvals();norm=max(abs(x) for x in ev)
    check(s.simplify(norm-gg*s.sqrt(2-2*cp0))==0,'full many-body cutoff coupling norm')
    free=lift(s.diag(2,3,2));H=free+VR
    if fault=='wrong_cutoff_pulse':H=free+2*VR
    vac=s.zeros(8,1);vac[0]=1;nm=dm.T*dm
    coeff=(vac.T*H*nm*H*vac)[0]
    check(coeff==gg*gg*ch0*ch0,'actual sea pair-creation short-time noise')
    # Smooth-cutoff inequality model: weighted values chi in[0,1].
    weights=[s.Rational(1,2),s.Rational(1,2)];chi=[s.Rational(1,2),s.Integer(1)]
    c2=sum(w*x*x for w,x in zip(weights,chi));av=sum(w*x for w,x in zip(weights,chi));c=s.sqrt(c2)
    delta2=2*(1-av/c)
    check(delta2>=0 and delta2<=2*(1-c),'normalized spatial cutoff distance bound')

    # Exact telescoping identity on noncommuting small unitary matrices, not a continuum proof.
    A=s.Matrix([[s.Rational(3,5),-s.Rational(4,5)],[s.Rational(4,5),s.Rational(3,5)]])
    B=s.diag(1,-1);C0=s.Matrix([[0,-1],[1,0]]);D=s.eye(2)
    check(zero(A*B-C0*D-((A-C0)*B+C0*(B-D))),'composition telescoping identity')
if __name__=='__main__':harness(test,['unsigned_fermionic_swap','wrong_coarse_record','omit_capture_readout','refined_readout','omit_idle_residual','wrong_memory_drift','omit_cutoff_hole','wrong_cutoff_pulse'])
