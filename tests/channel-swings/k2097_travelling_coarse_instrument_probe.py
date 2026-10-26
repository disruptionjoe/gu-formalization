"""Exact finite/data controls; universal continuum scope rests on the linked proof."""
import sympy as s

def check(value,msg):
    if not bool(value):raise AssertionError(msg)
def zero(M):return all(s.simplify(x)==0 for x in M)
def harness(test,faults):
    test(None);print('PASS clean exact baseline')
    for fault in faults:
        try:test(fault)
        except AssertionError as exc:print('DETECTED',fault,str(exc))
        else:raise AssertionError('undetected fault '+fault)
    print('PASS',len(faults),'genuine state/input/gate faults; no finite proof of continuum scope')

# Occupancy masks use little-endian n1,n2,mem1,mem2,out1,out2.
# The note uses lexicographic basis; E=0 is mask2 here, not an operator change.
def add(d,key,val):d[key]=s.expand(d.get(key,0)+val)
def mix(v,i,j,c,a):
    out={}
    for (mask,ptr,flag),val in v.items():
        bi=(mask>>i)&1;bj=(mask>>j)&1
        if bi==bj:add(out,(mask,ptr,flag),val);continue
        add(out,(mask,ptr,flag),c*val)
        sign=(-1)**sum((mask>>k)&1 for k in range(min(i,j)+1,max(i,j)))
        add(out,(mask^(1<<i)^(1<<j),ptr,flag),a*sign*val*(1 if bi else -1))
    return out

def evolve(code,c,a,d,b,mem=0,ptr0=0,refined=False,wrong_phase=False):
    v={(code|(mem<<2),ptr0,0):s.Integer(1)}
    v=mix(v,2,0,c,a);v=mix(v,3,1,c,a)
    w={}
    for (mask,ptr,flag),val in v.items():
        n1=(mask>>2)&1;n2=(mask>>3)&1;e=1-(1-n1)*n2
        add(w,(mask,ptr^e,((mask>>2)&3) if refined else 0),val)
    v=mix(w,2,4,d,b);v=mix(v,3,5,d,b)
    if not wrong_phase:v={key:val*(-1)**(((key[0]>>4)&1)+((key[0]>>5)&1)) for key,val in v.items()}
    return v

def cp(v,w):
    # Trace all bypass/memory modes, dephase the readable pointer, retain outgoing code.
    M=s.zeros(8)
    for (mask,p,flag),a in v.items():
      for (mask2,p2,flag2),b in w.items():
        if p==p2 and mask&15==mask2&15 and flag==flag2:
          M[2*(mask>>4)+p,2*(mask2>>4)+p2]+=a*s.conjugate(b)
    return M

def test(fault):
    # Full ideal instrument on every matrix unit, including odd cross-sector operators.
    vs=[evolve(i,0,1,0,1,wrong_phase=fault=='omit_output_phase') for i in range(4)]
    for i in range(4):
      for j in range(4):
        expected=s.zeros(8);ei=1-(1-(i&1))*((i>>1)&1);ej=1-(1-(j&1))*((j>>1)&1)
        if ei==ej:expected[2*i+ei,2*j+ej]=1
        check(zero(cp(vs[i],vs[j])-expected),'ideal full instrument matrix unit '+str((i,j)))
    c=s.Rational(3,5);a=s.Rational(4,5);d=s.Rational(5,13);b=s.Rational(12,13);ec=a*a;er=b*b
    vs=[evolve(i,c,a,d,b,refined=fault=='refined_memory_readout') for i in range(4)]
    for v in vs:check(s.simplify(sum(x*x for x in v.values())-1)==0,'isometry norm')
    coherence=cp(vs[0],vs[3])[1,7]
    check(coherence==ec*er,'vacuum pair coherence survives with transfer factors')
    out=cp(vs[2],vs[2]);p0=sum(out[i,i] for i in range(0,8,2))
    check(p0==ec,'record failure lower witness')
    out11=cp(vs[3],vs[3]);both=out11[6,6]+out11[7,7]
    check(both==(ec*er)**2,'strong two-particle success witness')
    q1=s.Rational(1,3);q2=s.Rational(1,4);noisy=s.zeros(8)
    for mem in range(4):
      prob=(q1 if mem&1 else 1-q1)*(q2 if mem&2 else 1-q2)
      state_mem=0 if fault=='silently_reset_memory' else mem
      v=evolve(0,c,a,d,b,mem=state_mem);noisy+=prob*cp(v,v)
    p0=sum(noisy[i,i] for i in range(0,8,2))
    check(p0==(1-(1-ec)*q1)*(1-ec)*q2,'actual mixed-memory false record')
    noise=s.Rational(1,5);M=s.zeros(8)
    for ptr,weight in [(0,1-noise),(1,noise)]:
      v=evolve(2,0,1,0,1,ptr0=(0 if fault=='silently_reset_pointer' else ptr));M+=weight*cp(v,v)
    check(sum(M[i,i] for i in range(1,8,2))==noise,'actual noisy record flip')
    # Exact two-mode norm formula checked from its unitary eigenvalues at rational rotation.
    U=s.Matrix([[c,-a],[a,c]]);J=s.Matrix([[0,-1],[1,0]])
    check(zero((U-J).T*(U-J)-(2-2*a)*s.eye(2)),'operator distance to full swap')
if __name__=='__main__':harness(test,['omit_output_phase','refined_memory_readout','silently_reset_memory','silently_reset_pointer'])
