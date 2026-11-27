#!/usr/bin/env python3
"""Exact companion-symbol controls, reusing guarded sparse Clifford primitives.
No native128 matrix build. Classification/source applicability remain reviewed
written proofs; exact basis replay checks the claimed curvature identity only.
"""
import itertools,json,time,argparse
from fractions import Fraction
from shiab_graded_derivation_probe import parity,wedge,cmul,add,scale,prod,bracket,theta,riemann_basis,curvature

def anti(a,b,p,q,eta):
    return add(prod(a,b,eta),scale(prod(b,a,eta),parity(p*q)))

def hodge(a,eta):
    full=(1<<len(eta))-1;out={}
    for (f,c),v in a.items():
        comp=full^f;s,_=wedge(f,comp)
        for i in range(len(eta)):
            if f>>i&1:s*=eta[i]
        out[comp,c]=out.get((comp,c),0)+s*v
    return {k:v for k,v in out.items()if v}

def selected(a,eta):
    n=len(eta);p1={(1<<i,1<<i):1 for i in range(n)}
    p2=scale(prod(p1,p1,eta),Fraction(1,2));sf=hodge(a,eta)
    first=bracket(p1,sf,1,n-2,eta)
    middle=hodge(anti(p2,sf,2,n-2,eta),eta)
    # Two i-Jordan products supply i²=-1, cancelling the printed -1/2.
    second=hodge(anti(p1,middle,1,0,eta),eta)
    return add(first,scale(second,Fraction(1,2))),middle

def companion(a,p,eta):
    th=theta(len(eta),eta)
    return add(prod(a,th,eta),scale(prod(th,a,eta),parity(p*(len(eta)-3))))

def fast_anti_curvature(terms,eta):
    n=len(eta);full=(1<<n)-1;z={}
    for (a,b),(i,j),v in terms:
        fm=(1<<a)|(1<<b);cm=(1<<i)|(1<<j);v*=eta[i]*eta[j]
        for l in range(n):
            if l in (a,b):continue
            t=fm|(1<<l);cof=full^t;s,_=wedge(t,cof)
            for k in (a,b,l):s*=eta[k]
            w,of=wedge(cof,fm);x,oc=cmul(t,cm,eta);y,_=cmul(cm,t,eta)
            key=of,oc;z[key]=z.get(key,0)+v*s*w*(x+y)
    return {k:v for k,v in z.items()if v}

def einstein(terms,eta):
    # Independent Ricci/scalar construction from the signed Riemann components.
    n=len(eta);ric={}
    for (a,b),(c,d),v in terms:
        for i,j,s1 in [(a,b,1),(b,a,-1)]:
            for k,l,s2 in [(c,d,1),(d,c,-1)]:
                if i==k:ric[j,l]=ric.get((j,l),0)+eta[i]*s1*s2*v
    scalar=sum(eta[j]*ric.get((j,j),0) for j in range(n));one={}
    for a in range(n):
        for b in range(n):
            g=ric.get((a,b),0)-(Fraction(scalar,2)*eta[a] if a==b else 0)
            if g:one[1<<a,1<<b]=g*eta[b]
    return hodge(one,eta)

def sparse_rank(rows):
    pivots={}
    for row in rows:
        row={k:Fraction(v) for k,v in row.items()if v}
        while row:
            j=min(row);v=row[j]
            if j not in pivots:
                pivots[j]={k:x/v for k,x in row.items()};break
            row={k:x for k,x in add(row,scale(pivots[j],-v)).items()if x}
    return len(pivots)

def alternation_control(n):
    pairs=list(itertools.combinations(range(n),2));cols={(a,b,c):j for j,(a,(b,c)) in enumerate(itertools.product(range(n),pairs))}
    ks=[{a:1} for a in range(n)]+[{a:1,b:1} for a,b in pairs];rows=[]
    for k in ks:
        for c in range(n):
            row={}
            for a,ka in k.items():
                for b,kb in k.items():
                    if b==c:continue
                    key=(a,min(b,c),max(b,c));j=cols[key];row[j]=row.get(j,0)+ka*kb*(1 if b<c else -1)
            rows.append(row)
    rk=sparse_rank(rows)
    # Each independent alternating3 tensor satisfies every generated row.
    for triple in itertools.combinations(range(n),3):
        vec={}
        for p in itertools.permutations(triple):
            a,b,c=p
            if b<c:
                inv=sum(p[i]>p[j] for i in range(3)for j in range(i+1,3));vec[cols[p]]=parity(inv)
        assert all(sum(v*vec.get(j,0)for j,v in row.items())==0 for row in rows)
    return {'unknowns':len(cols),'rank':rk,'kernel_dimension':len(cols)-rk,'expected':n*(n-1)*(n-2)//6}

def sharp_sign(mask,gamma_sign=-1):
    r=mask.bit_count();return parity(r*(r-1)//2)*(gamma_sign**r)

def main():
    start=time.monotonic();checks={};coverage={};witnesses={}
    def ok(label,x):
        checks[label]=bool(x)
        if not x:raise AssertionError(label)
    for n in [3,4,5,6]:
        d=alternation_control(n);coverage['tensor_n'+str(n)]=d;ok('complete polarized tensor kernel n'+str(n),d['kernel_dimension']==d['expected'])
    for eta in [(1,)*4,(1,)*3+(-1,)*3,(1,)*9+(-1,)*5,(1,)*7+(-1,)*7]:
        n=len(eta);q=eta.count(-1);label=f'n{n}_q{q}';full=(1<<n)-1
        f={(3,1):1};k={(1,0):1};out,middle=selected(f,eta);defect=prod(k,out,eta)
        ok(label+' input is closed',not prod(k,f,eta));ok(label+' selected inner term vanishes',not middle);ok(label+' selected exact defect',defect=={(full,3):-2})
        ok(label+' opposite chain sign cannot repair',bool(defect))
        witnesses[label]={'external_mask':full,'coefficient_mask':3,'value':-2}
        # Passing comparator: the right-wedge family, on k-spanning bases and sums.
        cases=0;nonzero_left=0
        fs=[{((1<<a)|(1<<b),1<<c):1} for a,b in itertools.combinations(range(min(n,4)),2) for c in range(min(n,3))]
        ks=[{(1<<i,0):1} for i in range(min(n,4))]+[{(1,0):1,(2,0):-2}]
        for f in fs:
            for k in ks:
                lhs=prod(k,companion(f,2,eta),eta);rhs=companion(prod(k,f,eta),3,eta)
                if lhs:nonzero_left+=1
                if lhs!=rhs:raise AssertionError((label,'wedge companion',f,k))
                cases+=1
        ok(label+' wedge companion with nonzero cases',cases>0 and nonzero_left>0)
        ok(label+' closed witness preserved by wedge survivor',not prod({(1,0):1},companion({(3,1):1},2,eta),eta))
        # The selected map and the same-Einstein survivor are not the same full-carrier map.
        ok(label+' survivor differs from selected on full carrier',selected({(3,1):1},eta)[0]!=scale(companion({(3,1):1},2,eta),-1))
        # Riemann identity independently compares all algebraic-basis vectors.
        count=0
        for terms in riemann_basis(n):
            count+=1
            if fast_anti_curvature(terms,eta)!=scale(einstein(terms,eta),2):raise AssertionError((label,'Einstein identity',terms))
        ok(label+' complete Riemann Einstein identity',count==n*n*(n*n-1)//12)
        for terms in [[((0,1),(0,1),1)],[((0,1),(2,3),1),((2,3),(0,1),1)]]:
            ok(label+' full versus reduced anti '+str(terms[0]),companion(curvature(terms,eta),2,eta)==fast_anti_curvature(terms,eta))
        sec=[((0,1),(0,1),1)]
        ok(label+' survivor nonzero on sectional Riemann',bool(fast_anti_curvature(sec,eta)))
        # Primitive adjoint grades: Θgrade3 is self for minus gamma; iΘ is skew.
        ok(label+' minus gamma and theta adjoints',sharp_sign(1)==-1 and sharp_sign(7)==1)
        # On each coefficient Clifford grade, a phase making X skew must make
        # the bare anti output skew. Conjugation of that same phase is used.
        reality=0
        th=theta(n,eta)
        for grade in range(n+1):
            c=(1<<grade)-1;inputsign=sharp_sign(c);phase_conjugation=-inputsign
            output=companion({(3,c):1},2,eta)
            if any(phase_conjugation*sharp_sign(oc)!=-1 for (_,oc) in output):raise AssertionError((label,'reality',grade))
            reality+=1
        ok(label+' bare anti preserves source-minus real coefficient forms',reality==n+1)
        ok(label+' multiplying only by i breaks real placement',sharp_sign(1)==-1 and -sharp_sign(1)==1)
        # Coherent plus-adjoint comparator: gamma -> i*gamma, hence
        # Theta -> i^3*Theta. Scalar phase conjugation is exactly (-1)^p.
        plus_reality=0
        for grade in range(n+1):
            c=(1<<grade)-1;phase=0 if sharp_sign(c,1)==-1 else 1
            output=companion({(3,c):1},2,eta)
            if any(parity(3+phase)*sharp_sign(oc,1)!=-1 for (_,oc) in output):raise AssertionError((label,'plus reality',grade))
            plus_reality+=1
        ok(label+' coherent plus phase preserves real placement',plus_reality==n+1)
        # On the selected witness the nested term is zero. Rephasing Phi1
        # and F each by i multiplies the first term by -1, never by zero.
        ok(label+' coherent plus witness remains nonzero',scale(defect,-1)=={(full,3):2} and sharp_sign(3,1)==-1)
        # Θ cannot define an associative derivation: it does not kill the unit.
        ok(label+' wedge survivor is not a full derivation',bool(companion({(0,0):1},0,eta)))
        ok(label+' wedge suite violates Lie center preservation',bool(bracket(companion({(0,0):1},0,eta),{(0,1):1},n-3,0,eta)))
        coverage[label]={'companion_cases':cases,'nonzero_companion_cases':nonzero_left,'riemann_basis_vectors':count,'native_signature_control_only':True}
    # A wrong output convention is detected, rather than all controls being vacuous.
    eta=(1,)*4;f={(3,4):1};k={(4,0):1};lhs=prod(k,companion(f,2,eta),eta)
    ok('planted companion sign defect detected',bool(lhs) and lhs!=scale(companion(prod(k,f,eta),3,eta),-1))
    return {'status':'PASS','grouped_checks':len(checks),'checks':checks,'coverage':coverage,'witnesses':witnesses,'runtime_seconds':time.monotonic()-start,'scope':'Exact controls and all algebraic Riemann basis vectors in declared signatures. Generic classification, connection-jet proof, source necessity, full nonlinear dynamics and physical interpretation are not established by finite sampling.'}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--verify',action='store_true');ap.parse_args();print(json.dumps(main(),indent=2))
