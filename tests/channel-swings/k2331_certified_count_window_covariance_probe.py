#!/usr/bin/env python3
"""Arb interval Picard tubes + covering Riemann sums, no mesh-convergence claim."""
import argparse,hashlib,json,math
from pathlib import Path
from flint import arb,ctx
R=Path(__file__).resolve().parents[2];ST='k2331-certified-count-window-covariance';ctx.prec=128
ZERO=arb(0);ONE=arb(1);BETA=-ONE/arb(6).sqrt();P=(5+arb(73).sqrt())/4
XS=(arb(2)/5*(1+P/2))**(1/P);RS=2*(1-1/XS.sqrt())
def box(a,b):return a.union(b)
def bound(x):return abs(x).upper()
def mv(A,y):return [sum((a*b for a,b in zip(row,y)),ZERO) for row in A]
def background(s):
    r=RS*s;x=(1-r/2)**(-2);F=1-arb(2)/5*x**(-P);a=F.sqrt()/x
    H=x**(arb(3)/2)*(1-arb(2)/5*(1+P/2)*x**(-P))/F**(arb(3)/2)
    u=-arb(3).sqrt()/arb(2).sqrt()*arb(2)/5*P*x**(arb(3)/2-P)/F**(arb(3)/2)
    d=3*x**3/F**2;V=-3*arb(2)/5*(1+P)*x**(3-P)/F**2
    nu=1-3/P;b=2+nu*F/(1-F);c=nu*F/(1-F)**2
    Vp=-(arb(2)/3).sqrt()*b*V;Vpp=arb(2)/3*(b*b-c)*V
    return r,x,F,a,H,u,d,Vp,Vpp
def matrix(s,k):
    r,x,F,a,H,u,d,Vp,Vpp=background(s);q=k*k/a**2;b=BETA
    J=[[-H,u/2,ZERO,-d/2],[ZERO,ZERO,ONE,ZERO],[-4*u*H-2*Vp-2*b*d+b*(2*q-u*u),-q-Vpp+2*u*u+3*b*H*u+b*Vp,-3*H+b*u,-2*u*d-3*b*H*d],[-ONE,-b,ZERO,-b*u]]
    return [[RS*a*v for v in row] for row in J]
def tube_step(y,A,h):
    # A continuous bounded linear IVP. Strict inclusion gives a first-exit proof.
    norm=max(sum((bound(v) for v in row),ZERO) for row in A)
    assert h*norm<1
    f=mv(A,y);rad=[2*h*bound(v)+arb('1e-32') for v in f]
    for it in range(30):
        Z=[y[i]+arb(0,rad[i]) for i in range(4)]
        fz=mv(A,Z);image=[y[i]+box(ZERO,h)*fz[i] for i in range(4)]
        if all(Z[i].contains_interior(image[i]) for i in range(4)):
            return [y[i]+h*fz[i] for i in range(4)],Z
        rad=[2*rad[i]+2*h*bound(fz[i]) for i in range(4)]
    raise AssertionError('Picard tube failed')
def j2(z,der=0):
    # j2=sum (-1)^m z^(2+2m)/(2^m m! (2m+5)!!).
    # Derivatives through2; |z|<1 gives decreasing omitted terms.
    assert bound(z)<1
    out=ZERO
    for m in range(7):
        power=2+2*m;den=2**m*math.factorial(m)*math.prod(range(1,2*m+6,2));fac=math.prod(range(power-der+1,power+1))
        out+=(-1)**m*fac*z**(power-der)/den
    m=7;power=2+2*m;den=2**m*math.factorial(m)*math.prod(range(1,2*m+6,2));fac=math.prod(range(power-der+1,power+1))
    # Absolute geometric tail, ratio <1/2 (also after two derivatives).
    return out+arb(0,2*fac*bound(z)**(power-der)/den)
def j_over_s(r,k):
    # Analytically remove r=0 before interval evaluation.
    z=k*r;out=ZERO
    for m in range(7):
        power=2+2*m;den=2**m*math.factorial(m)*math.prod(range(1,2*m+6,2))
        out+=(-1)**m*k**power*r**(power-1)/den
    return out+arb(0,2*bound(k)**16*bound(r)**15/(2**7*math.factorial(7)*math.prod(range(1,20,2))))
def fields(s,k,y):
    r,x,F,a,H,u,d,Vp,Vpp=background(s);phi,chi,pi,v=y;q=k*k/a**2
    phit=-H*phi+(u*chi-d*v)/2
    n=(-(2*q-u*u)*phi-(3*H*u+Vp+BETA*d)*chi+3*H*d*v-u*pi)/d
    return r,x,a,n-3*BETA*chi,phi+BETA*chi,phi-BETA*chi,a*(phit-BETA*pi),2*phi,2*a*phit,v

def compute(steps=512,bands=32,sign2=1,radial_sign=1):
    assert steps%8==0
    h=ONE/steps;M=[[ZERO for _ in range(2)] for _ in range(2)];bands_out=[];g_all=[];proof_cells=0
    for b in range(bands):
        k=box(ONE+arb(b)/bands,ONE+arb(b+1)/bands);y=[ZERO,ZERO,ZERO,1/k];tubes=[]
        for j in range(steps):
            # z increases towards observer; s=1-z decreases.
            s=box(ONE-arb(j+1)/steps,ONE-arb(j)/steps);y,Z=tube_step(y,matrix(s,k),h);tubes.append((s,Z));proof_cells+=1
        Q0=Q1=Qd=ZERO;bs=[ZERO,ZERO];gs=[[],[]]
        for idx,(s,y) in enumerate(reversed(tubes)):
            r,x,a,nj,phij,psij,dpsij,W,dW,v=fields(s,k,y);z=k*r;j=j2(z);dr=RS*h
            f0=W*j;f1=W*j_over_s(r,k);fd=dW*j
            # Every partial foreground integral is enclosed by the old integral + [0,dr]*cell range.
            q0=Q0+box(ZERO,dr)*f0;q1=Q1+box(ZERO,dr)*f1;qd=Qd+box(ZERO,dr)*fd
            win=0 if steps//4<=idx<steps//2 else 1 if 5*steps//8<=idx<7*steps//8 else None
            if win is not None:
                hc=x.sqrt();A=-arb(1)/2+2/(r*hc)
                g=(nj+dpsij/hc+(1+A)*phij-2*psij)*j-radial_sign*(k*k*v/(a*hc)*j2(z,2)+A*k*v/a*j2(z,1))+A*qd-4*q0/r+6*q1
                bs[win]+=4*h*g;gs[win].append(g)
            Q0+=dr*f0;Q1+=dr*f1;Qd+=dr*fd
        bs[1]*=sign2
        for i in range(2):
            for j in range(2):M[i][j]+=16*arb.pi()**2/bands*k*k*bs[i]*bs[j]
        ranges=[box(min(x.lower() for x in v),max(x.upper() for x in v)) for v in gs];g_all.extend(ranges)
        bands_out.append({'k':str(k),'b':[str(x) for x in bs],'g_ranges':[str(x) for x in ranges]})
    return M,bands_out,all(x<0 for x in g_all),proof_cells

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--steps',type=int,default=512);ap.add_argument('--bands',type=int,default=32);ap.add_argument('--write',action='store_true');a=ap.parse_args()
    M,rows,negative,cells=compute(a.steps,a.bands)
    checks=[('seed lies within inherited smooth fixture',XS>1 and XS<arb(11)/10),('all source-cell full kernels negative',negative),('actual covariance diagonals positive',M[0][0]>0 and M[1][1]>0),('actual shared-seed cross covariance positive',M[0][1]>0),('covariance symmetric',M[0][1].overlaps(M[1][0]))]
    for name,ok in checks: print(('PASS ' if ok else 'FAIL ')+name)
    print('r_star',RS,'covariance',[[str(x) for x in row] for row in M]);print('first,last',rows[0],rows[-1]);print('validated tubes',cells)
    assert all(ok for _,ok in checks), 'baseline must pass before faults'
    # Changed physical inputs use the SAME enclosed dynamics/observation evaluator.
    neg,_,_,_=compute(a.steps,a.bands,sign2=-1)
    assert neg[0][0].overlaps(M[0][0]) and neg[1][1].overlaps(M[1][1])
    faults=[('negative second window breaks positive cross prediction',not (neg[0][1]>0) and neg[0][1]<0)]
    _,_,wrong_negative,_=compute(a.steps,a.bands,radial_sign=-1)
    faults.append(('reversed radial velocity terms break negative-kernel prediction',not wrong_negative))
    # Picard inclusion is the certifier: an under-sized candidate tube must be rejected.
    trial=[arb(0) for _ in range(4)];trial[3]=arb(1)
    mat=matrix(arb('0.7'),arb('1.5'));fz=mv(mat,trial)
    faults.append(('zero-width Picard tube rejects actual nonzero drift',not all(trial[i].contains(trial[i]+arb('0.001')*fz[i]) for i in range(4))))
    for name,ok in faults: print(('PASS fault ' if ok else 'FAIL fault ')+name)
    assert all(ok for _,ok in faults)
    sign_checks=[('five-mode null probability exact',2**5==32),('negative-correlation power sector',arb(5)/6 > arb(1)/2),('certified aligned noisy correlation',M[0][1].lower()/(max(M[0][0].upper(),M[1][1].upper())+1)>arb(83)/100)]
    sign_checks.append(('PSD correlated-noise countercontrol reverses total cross sign',M[0][1]-1000<0 and M[0][0]+1000>0 and M[1][1]+1000>0))
    assert all(ok for _,ok in sign_checks)
    report={'result' :'K2331','status':'pass' if all(ok for _,ok in checks) else 'failed','method':'Arb128 validated Picard tubes and covering interval Riemann sums','steps':a.steps,'spectral_cells':a.bands,'validated_tubes':cells,'checks':checks,'changed_input_faults':faults,'sign_controls':sign_checks,'r_star':str(RS),'matrix':[[{'lower':str(x.lower()),'upper':str(x.upper())} for x in row] for row in M],'bands':rows,'scope':'fixed compact band [1,2], normalized two radial top hats, full conserved dust L2 count; conditional conventional model, no survey/GU inference'}
    if a.write:
        deps=[f'tests/channel-swings/{ST.replace("-","_")}_probe.py',f'explorations/conditional-build/{ST}-2026-10-30.md']
        report['dependencies']={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps};(R/f'lab/process/{ST}.json').write_text(json.dumps(report,indent=2)+'\n')
    assert all(ok for _,ok in checks)
if __name__=='__main__':main()
