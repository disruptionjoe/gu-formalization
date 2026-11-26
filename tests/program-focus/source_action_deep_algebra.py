"""Exact invariant W2 Euler algebra. Root owns execution/resource scheduling.

All coefficient forms use {(exterior_bitmask, Clifford_bitmask): Fraction}.
This engine follows the real-Clifford coefficient subspace containing S. The
actual two i-anticommutators cancel their i² against the printed minus; B, K
and N preserve this subspace. This is closure inside full u(64,64), not an
assumed source quaternionic restriction. Geometry API: d, Lambda[i][j][k],
spin[i]:{clifford_mask:Fraction}, and mbracket(i,j):{k:Fraction}.
"""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from math import isqrt


def clean(x): return {k:v for k,v in x.items() if v}
def add(*xs):
    z={}
    for x in xs:
        for k,v in x.items(): z[k]=z.get(k,Q(0))+v
    return clean(z)
def scale(a,x): return clean({k:a*v for k,v in x.items()})


class Engine:
    def __init__(self, geometry):
        self.geo=geometry
        self.d=tuple(map(Q,geometry.d));self.dim=len(self.d)
        self.full=(1<<self.dim)-1
        self.Lambda=geometry.Lambda
        self.spin=geometry.spin
        self.mbracket=geometry.mbracket
        det=Q(1)
        for x in self.d:det*=x
        numerator=isqrt(abs(det.numerator));denominator=isqrt(det.denominator)
        if numerator*numerator!=abs(det.numerator) or denominator*denominator!=det.denominator:
            raise ValueError('Use rational orthogonal geometry with rational volume')
        self.volume=Q(numerator,denominator)
        self.negative=sum(x<0 for x in self.d)
        self.phi1={(1<<a,1<<a):Q(1) for a in range(self.dim)}
        self.phi2={((1<<a)|(1<<b),(1<<a)|(1<<b)):Q(1)
                   for a,b in combinations(range(self.dim),2)}
        self.lam_nonzero=[[[ (k,Q(v)) for k,v in enumerate(self.Lambda[i][j]) if v]
                           for j in range(self.dim)] for i in range(self.dim)]

    @staticmethod
    @lru_cache(maxsize=131072)
    def sign(a,b):
        parity=0
        while a:
            low=a&-a;parity+=(b&(low-1)).bit_count();a-=low
        return -1 if parity%2 else 1

    @lru_cache(maxsize=16384)
    def dprod(self,mask):
        result=Q(1)
        while mask:
            low=mask&-mask;result*=self.d[low.bit_length()-1];mask-=low
        return result

    @lru_cache(maxsize=131072)
    def cmul(self,a,b):
        return a^b,self.sign(a,b)*self.dprod(a&b)

    @lru_cache(maxsize=32768)
    def weight(self,e,c):
        # Pointwise real trace/form pairing b=-Re tr/128.
        return -self.cmul(c,c)[1]/self.dprod(e)

    def pair(self,x,y):
        return sum(v*y.get(k,Q(0))*self.weight(*k) for k,v in x.items())

    def cliff_product(self,x,y,kind='raw'):
        z={}
        for ca,va in x.items():
            for cb,vb in y.items():
                if kind!='raw':
                    swap_odd=(ca.bit_count()*cb.bit_count()-(ca&cb).bit_count())%2
                    if (kind=='comm' and not swap_odd) or (kind!='comm' and swap_odd):continue
                c,q=self.cmul(ca,cb)
                if kind!='raw':q*=2
                if q:z[c]=z.get(c,Q(0))+q*va*vb
        return clean(z)

    def wedge(self,x,y,kind='raw'):
        z={}
        for (ea,ca),va in x.items():
            for (eb,cb),vb in y.items():
                if ea&eb:continue
                if kind!='raw':
                    swap_odd=(ca.bit_count()*cb.bit_count()-(ca&cb).bit_count())%2
                    if (kind=='comm' and not swap_odd) or (kind!='comm' and swap_odd):continue
                c,q=self.cmul(ca,cb)
                if kind!='raw':q*=2
                if q:
                    key=(ea|eb,c)
                    z[key]=z.get(key,Q(0))+self.sign(ea,eb)*q*va*vb
        return clean(z)

    def star(self,x):
        return clean({(self.full^e,c):v*self.sign(e,self.full^e)*self.volume/self.dprod(e)
                      for (e,c),v in x.items()})

    def star_inverse(self,x):
        out={}
        for (e,c),v in x.items():
            degree=e.bit_count()
            q=(-1)**(degree*(self.dim-degree)+self.negative)
            out[(self.full^e,c)]=q*v*self.sign(e,self.full^e)*self.volume/self.dprod(e)
        return clean(out)

    def star_adj(self,x):
        out={}
        for (eo,c),v in x.items():
            ei=self.full^eo
            forward=self.sign(ei,eo)*self.volume/self.dprod(ei)
            out[(ei,c)]=v*forward*self.weight(eo,c)/self.weight(ei,c)
        return clean(out)

    def star_inverse_adj(self,x):
        out={}
        for (eo,c),v in x.items():
            ei=self.full^eo;degree=ei.bit_count()
            forward=(-1)**(degree*(self.dim-degree)+self.negative)
            forward*=self.sign(ei,eo)*self.volume/self.dprod(ei)
            out[(ei,c)]=v*forward*self.weight(eo,c)/self.weight(ei,c)
        return clean(out)

    def left_wedge_adj(self,fixed,y,kind='raw'):
        """Adjoint of v -> fixed wedge_kind v for the exact trace/form pairing."""
        out={}
        by_form={}
        for (ea,ca),va in fixed.items():by_form.setdefault(ea,[]).append((ca,va))
        allowed={eo:[(ea,ca,va) for ea,terms in by_form.items() if eo&ea==ea
                                  for ca,va in terms] for eo in {e for e,c in y}}
        for (eo,co),vo in y.items():
            for ea,ca,va in allowed[eo]:
                eb=eo^ea;cb=ca^co
                if kind!='raw':
                    swap_odd=(ca.bit_count()*cb.bit_count()-(ca&cb).bit_count())%2
                    if (kind=='comm' and not swap_odd) or (kind!='comm' and swap_odd):continue
                c,q=self.cmul(ca,cb)
                assert c==co
                if kind!='raw':q*=2
                if q:
                    coefficient=self.sign(ea,eb)*q*va
                    key=(eb,cb)
                    out[key]=out.get(key,Q(0))+vo*coefficient*self.weight(eo,co)/self.weight(eb,cb)
        return clean(out)

    def shiab(self,x):
        # S0 = Phi1 comm *x -1/2 *[Phi1 ianti * (Phi2 ianti *x)].
        # Both i factors are retained algebraically: i² reverses the minus.
        first=self.wedge(self.phi1,self.star(x),'comm')
        second=self.star(self.wedge(self.phi1,self.star(self.wedge(self.phi2,self.star(x),'anti')),'anti'))
        return add(first,scale(Q(1,2),second))

    @lru_cache(maxsize=4096)
    def _phi_basis(self,e,c):
        return self.star_inverse(self.shiab({(e,c):Q(1)}))

    def Phi(self,x):
        out={}
        for (e,c),v in x.items():
            if e.bit_count()!=2:raise ValueError('Phi expects two-forms')
            for key,a in self._phi_basis(e,c).items():out[key]=out.get(key,Q(0))+v*a
        return clean(out)

    @lru_cache(maxsize=2048)
    def _phi_adj_basis(self,e,c):
        # Reverse every actual factor in Phi=*^-1 S0. No invariant transpose.
        z=self.star_inverse_adj({(e,c):Q(1)})
        first=self.star_adj(self.left_wedge_adj(self.phi1,z,'comm'))
        second=self.star_adj(z)
        second=self.left_wedge_adj(self.phi1,second,'anti')
        second=self.star_adj(second)
        second=self.left_wedge_adj(self.phi2,second,'anti')
        second=self.star_adj(second)
        return add(first,scale(Q(1,2),second))

    def Phi_adj(self,x):
        out={}
        for (e,c),v in x.items():
            if e.bit_count()!=1:raise ValueError('Phi_adj expects one-forms')
            for key,a in self._phi_adj_basis(e,c).items():out[key]=out.get(key,Q(0))+v*a
        return clean(out)

    @staticmethod
    def split_one(T):
        out={}
        for (e,c),v in T.items():
            if e.bit_count()!=1:raise ValueError('Expected one-form')
            out.setdefault(e.bit_length()-1,{})[c]=v
        return out

    @staticmethod
    def split_two(W):
        out={}
        for (e,c),v in W.items():
            if e.bit_count()!=2:raise ValueError('Expected two-form')
            low=e&-e;i=low.bit_length()-1;j=(e^low).bit_length()-1
            out.setdefault((i,j),{})[c]=v
        return out

    def D(self,T):
        t=self.split_one(T);out={}
        for i,j in combinations(range(self.dim),2):
            row=add(self.cliff_product(self.spin[i],t.get(j,{}),'comm'),
                    scale(-1,self.cliff_product(self.spin[j],t.get(i,{}),'comm')),
                    *[scale(-v,t.get(k,{})) for k,v in self.mbracket(i,j).items()])
            for c,v in row.items():out[((1<<i)|(1<<j),c)]=v
        return out

    def Dadj(self,W):
        w=self.split_two(W);out={}
        def row(i,j):
            if i==j:return {}
            return w.get((i,j),{}) if i<j else scale(-1,w.get((j,i),{}))
        for a in range(self.dim):
            answer={}
            for i in range(self.dim):
                term=self.cliff_product(self.spin[i],row(i,a),'comm')
                term=add(term,*[scale(-v,row(k,a)) for k,v in self.lam_nonzero[i][i]],
                              *[scale(-v,row(i,k)) for k,v in self.lam_nonzero[i][a]])
                answer=add(answer,scale(-1/self.d[i],term))
            for c,v in answer.items():out[(1<<a,c)]=v
        return clean(out)

    def K(self,T):
        return scale(Q(1,2),add(self.Phi(self.D(T)),self.Dadj(self.Phi_adj(T))))

    def N(self,U,V):
        # Q_U(V)=V wedge U+U wedge V=U wedge_comm V for one-forms.
        return scale(Q(1,6),add(self.Phi(self.wedge(U,V,'comm')),
            self.left_wedge_adj(U,self.Phi_adj(V),'comm'),
            self.left_wedge_adj(V,self.Phi_adj(U),'comm')))

    def N_diag(self,T):
        return scale(Q(1,3),add(self.Phi(self.wedge(T,T)),
            self.left_wedge_adj(T,self.Phi_adj(T),'comm')))

    def curvature(self):
        """Uses geometry.curvature_spin if supplied; never assumes its sign."""
        if not hasattr(self.geo,'curvature_spin'):
            raise AttributeError('geometry.curvature_spin(i,j) required for independent S')
        out={}
        for i,j in combinations(range(self.dim),2):
            for c,v in self.geo.curvature_spin(i,j).items():
                if v:out[((1<<i)|(1<<j),c)]=Q(v)
        return out

    def S_known(self):
        # Actual native W2 normalization; independent curvature replay required.
        return {(1<<a,1<<a):Q(-21,4) if a<5 else Q(-15,4)
                for a in range(self.dim)}

    def real_skew(self,T):
        return all(c.bit_count()%4 in (1,2) for (_,c),v in T.items() if v)

    def euler(self,T,kappa=1):
        return add(self.S_known(),scale(Q(kappa),T),self.K(T),self.N_diag(T))

    def pointwise_cubic(self,T):
        return self.pair(T,self.Phi(self.wedge(T,T)))/3

    def calibration_checks(self):
        """Light API-level exact controls; root chooses when to run."""
        checks={}
        def check(name,condition):
            checks[name]=bool(condition);assert condition,name
        check('native_volume',self.volume==196608)
        check('native_negative_count',self.negative==5)
        for a in (0,3,4,5,13):
            e=1<<a
            check('mass_weight_'+str(a),self.pair({(e,e):Q(1)},{(e,e):Q(1)})==-1)
        U={(1,1):Q(2),(1<<4,1<<4):Q(-1),(1<<8,(1<<0)|(1<<8)):Q(3)}
        W={((1<<0)|(1<<4),(1<<0)|(1<<4)):Q(2),
           ((1<<3)|(1<<5),1<<5):Q(-3)}
        check('Phi_actual_pointwise_adjoint',self.pair(U,self.Phi(W))==self.pair(self.Phi_adj(U),W))
        check('Phi_star_inverse',self.Phi(W)==self.star_inverse(self.shiab(W)))
        check('N_polarization',self.N(U,U)==self.N_diag(U))
        # Actual polynomial derivative, not finite differences.
        Z={(1<<2,1<<2):Q(1),(1<<4,(1<<0)|(1<<4)):Q(2)}
        deriv=(self.pair(Z,self.Phi(self.wedge(U,U)))+
               self.pair(U,self.Phi(self.wedge(U,Z,'comm'))))/3
        check('N_full_cubic_gradient',deriv==self.pair(Z,self.N_diag(U)))
        check('S_real_Krein_skew',self.real_skew(self.S_known()))
        check('K_S_real_Krein_skew',self.real_skew(self.K(self.S_known())))
        check('N_S_real_Krein_skew',self.real_skew(self.N_diag(self.S_known())))
        return checks


# Exact isotropy and generated-span verifier.

import source_action_deep_geometry as geometry
def serialize_form(T):return [[e,c,str(v)] for (e,c),v in sorted(T.items())]
def serialize_coords(c):return {str(i):str(v) for i,v in sorted(c.items()) if v}


class Span:
    def __init__(self, engine, max_dimension=122):
        self.engine=engine;self.max_dimension=max_dimension
        self.basis=[];self.pivots=[];self.adj=[];self.provenance=[]
        self.parities=[];self.isotropy_checks=0;self.replay_checks=0
        self.isotropy=[]
        for i,j in combinations(range(4),2):
            H=geometry.zero();H[i][j]=Q(1);H[j][i]=-geometry.eta[i]*geometry.eta[j]
            action=[geometry.h_action(H,a) for a in range(14)]
            spin={}
            for a in range(14):
                for b in range(a+1,14):
                    val=action[b].get(a,Q(0))/(2*geometry.d[b])
                    if val:spin[(1<<a)|(1<<b)]=val
            self.isotropy.append((action,spin))

    def verify_invariant(self,T):
        rows=self.engine.split_one(T)
        for action,spin in self.isotropy:
            for a in range(14):
                defect=add(self.engine.cliff_product(spin,rows.get(a,{}),'comm'),
                           *[scale(-v,rows.get(k,{})) for k,v in action[a].items()])
                if defect:raise AssertionError(('not_isotropy_invariant',a,defect))
        self.isotropy_checks+=1

    def expand(self,coordinates):
        return add(*[scale(v,self.basis[i]) for i,v in coordinates.items() if v])

    def insert(self,T,source):
        if not self.engine.real_skew(T):raise AssertionError(('outside_real_Krein_sector',source))
        remainder=dict(T);coords={}
        for i,(pivot,row) in enumerate(zip(self.pivots,self.basis)):
            coeff=remainder.get(pivot,Q(0))
            if coeff:
                coords[i]=coeff
                remainder=add(remainder,scale(-coeff,row))
        if remainder:
            if len(self.basis)>=self.max_dimension:
                raise AssertionError(('generated_rank_exceeds_proved_ceiling',source))
            pivot=min(remainder);coefficient=remainder[pivot]
            row=scale(1/coefficient,remainder)
            self.verify_invariant(row)
            parity={c.bit_count()%2 for e,c in row}
            if len(parity)!=1:raise AssertionError(('basis_not_parity_homogeneous',source))
            index=len(self.basis)
            self.basis.append(row);self.pivots.append(pivot)
            self.provenance.append(source);self.parities.append(parity.pop())
            self.adj.append(self.engine.Phi_adj(row))
            coords[index]=coefficient
            print(json.dumps({'event':'new_basis','rank':index+1,'source':source,
                              'support':len(row),'grades':sorted({c.bit_count() for e,c in row})}),
                  file=sys.stderr,flush=True)
        # Replay all coordinates in original full receiver space immediately.
        if self.expand(coords)!=T:raise AssertionError(('coordinate_replay_failed',source))
        self.replay_checks+=1
        return coords


def replay_coefficients(path, full=False):
    import json
    from pathlib import Path
    data=json.loads(Path(path).read_text())
    basis=[{(int(e),int(c)):Q(v) for e,c,v in row} for row in data['basis']]
    E=Engine(geometry);verifier=Span(E,max_dimension=59)
    for B in basis:verifier.verify_invariant(B)
    flip=sum(1<<i for i in (0,8,9,10))
    assert len(basis)==59 and all(E.real_skew(B) for B in basis)
    assert all(((e^c)&flip).bit_count()%2==0 for B in basis for e,c in B)
    pivots=[tuple(p) for p in data['pivots']]
    assert all(B.get(p,Q(0))==int(i==j) for i,p in enumerate(pivots) for j,B in enumerate(basis))
    def expand(cs):return add(*[scale(Q(v),basis[int(i)]) for i,v in cs.items() if Q(v)])
    assert expand(data['S'])==E.Phi(E.curvature())==E.S_known()
    count=1
    if full:
        adj=[E.Phi_adj(B) for B in basis]
        for i,B in enumerate(basis):
            assert expand(data['K'][str(i)])==E.K(B),('K',i)
            count+=1
            for j in range(i+1):
                actual=scale(Q(1,6),add(E.Phi(E.wedge(B,basis[j],'comm')),
                    E.left_wedge_adj(B,adj[j],'comm'),E.left_wedge_adj(basis[j],adj[i],'comm')))
                assert expand(data['N'][f'{j},{i}'])==actual,('N',j,i)
                count+=1
    return {'basis_dimension':59,'all_isotropy_generators_checked':True,
            'reality_reflection_fixed':True,'exact_full_tensor_replays':count,
            'coefficient_table_full_replay':full}

def verify_generation(data):
    n=data['dimension'];w=data['generation_witness'];assert n==w['rank']==59
    basis=[{(int(e),int(c)):Q(v) for e,c,v in row} for row in data['basis']]
    rows=[{int(i):Q(v) for i,v in cs.items()} for cs in w['basis_coordinates']]
    pivots=[tuple(p) for p in w['original_pivots']]
    def value(cs,p):return sum(c*basis[i].get(p,Q(0)) for i,c in cs.items())
    def linear(cs):
        out={}
        for j,x in cs.items():
            for k,v in data['K'][str(j)].items():
                k=int(k);out[k]=out.get(k,Q(0))+x*Q(v)
        return {k:v for k,v in out.items() if v}
    def bilinear(x,y):
        out={}
        for i,a in x.items():
            for j,b in y.items():
                key=f'{min(i,j)},{max(i,j)}'
                for k,v in data['N'][key].items():
                    k=int(k);out[k]=out.get(k,Q(0))+a*b*Q(v)
        return {k:v for k,v in out.items() if v}
    for i,B in enumerate(rows):
        assert value(B,pivots[i])==1
        assert all(not value(B,pivots[j]) for j in range(i))
        source=w['operations'][i];op=source['operation']
        if op=='S':assert i==0;v={int(k):Q(c) for k,c in data['S'].items()}
        elif op=='K':assert source['i']<i;v=linear(rows[source['i']])
        elif op=='N':
            assert source['i']<i and source['j']<i
            v=bilinear(rows[source['i']],rows[source['j']])
        else:raise AssertionError(op)
        last=None
        for j in range(i+1):
            c=value(v,pivots[j]);last=c
            for k,b in rows[j].items():v[k]=v.get(k,Q(0))-c*b
            v={k:b for k,b in v.items() if b}
        assert not v and last,(i,source)
    return {'recursive_generated_rank':59,'all_recursive_S_K_N_memberships_exact':True,'smallest_closed_generated_space_exhausts_fixed_family':True}


def certificate_for(data,guess):

    assert data['closed'] and data.get('coefficients_complete',True)
    h=Q(str(guess['h']));assert h>0
    n=data['dimension'];x=list(map(Q,guess['coordinates']))
    R=[list(map(Q,row)) for row in guess['approximate_inverse_normalized_J']]
    assert len(x)==n and len(R)==n and all(len(row)==n for row in R)
    F=x.copy();J=[[Q(i==j) for j in range(n)] for i in range(n)]
    for i,v in data['S'].items():F[int(i)]+=h*Q(v)
    for col,row in data['K'].items():
        j=int(col)
        for target,v in row.items():
            k=int(target);a=h*Q(v);F[k]+=a*x[j];J[k][j]+=a
    quadratic_norm=[Q(0)]*n
    for pair,row in data['N'].items():
        i,j=map(int,pair.split(','));factor=1 if i==j else 2
        for target,v in row.items():
            k=int(target);a=h*Q(v)
            F[k]+=factor*a*x[i]*x[j]
            if i==j:J[k][i]+=2*a*x[i]
            else:J[k][i]+=2*a*x[j];J[k][j]+=2*a*x[i]
            quadratic_norm[k]+=factor*abs(a)
    RF=[sum(R[i][k]*F[k] for k in range(n)) for i in range(n)]
    e=max(map(abs,RF));a=Q(0)
    for i in range(n):
        rownorm=sum(abs(Q(i==j)-sum(R[i][k]*J[k][j] for k in range(n))) for j in range(n))
        a=max(a,rownorm)
    # Componentwise positive bound for the bilinear norm of R N.
    b=max(sum(abs(R[i][k])*quadratic_norm[k] for k in range(n)) for i in range(n))
    status='not_certified_by_this_bound';radius=None;invariance=None;lipschitz=None
    if a<1:
        if e:
            radius=2*e/(1-a)
        elif b:
            radius=(1-a)/(4*b)
        else:radius=Q(1)
        invariance=e+a*radius+b*radius*radius
        lipschitz=a+2*b*radius
        if invariance<=radius and lipschitz<1:status='exact_local_root_certified'
    result={'status':status,'dimension':n,'h':str(h),'kappa':str(1/h),
            'e':str(e),'a':str(a),'b':str(b),'radius':None if radius is None else str(radius),
            'ball_image_bound':None if invariance is None else str(invariance),
            'lipschitz_bound':None if lipschitz is None else str(lipschitz),
            'approximate_sizes':{'e':float(e),'a':float(a),'b':float(b),'radius':None if radius is None else float(radius)},
            'proof':'T(x)=x−R F(x); exact rational bounds give invariant complete closed ball and strict contraction. a<1 makes RJ(x0), hence squareR, invertible; its fixed point has F=0.',

            'ceiling':'local real root of the exported invariant candidate polynomial; numerical connection to small-h branch is not thereby certified'}
    return result



def verify_roots(data):
    roots=data['certified_roots'];assert len(roots)==2
    output=[]
    for root in roots:
        cert=certificate_for(data,root)
        assert cert['status']=='exact_local_root_certified'
        for key in ('e','a','b','radius','ball_image_bound','lipschitz_bound'):
            assert cert[key]==root['certificate'][key],(root['id'],key)
        output.append({'id':root['id'],**cert})
    basis=[{(int(e),int(c)):Q(v) for e,c,v in row} for row in data['basis']]
    E=Engine(geometry);G=[[E.pair(A,B) for B in basis] for A in basis]
    assert G==list(map(list,zip(*G)))
    n=len(G);gnorm=sum(abs(v) for row in G for v in row);intervals=[]
    for root,expected in zip(roots,data['root_distinction']['roots']):
        x=list(map(Q,root['coordinates']));r=Q(root['certificate']['radius'])
        Gx=[sum(G[i][j]*x[j] for j in range(n)) for i in range(n)]
        value=sum(x[i]*Gx[i] for i in range(n));error=2*r*sum(map(abs,Gx))+r*r*gnorm
        assert str(value)==expected['center'] and str(error)==expected['error']
        intervals.append((value-error,value+error))
    assert intervals[0][1]<intervals[1][0] or intervals[1][1]<intervals[0][0]
    return {'exact_local_roots':output,'pointwise_pairing_intervals_disjoint':True,
       'scope':'two mathematical homogeneous stationary candidates at kappa1; no physical selection or small-h path certificate'}


# Optional numerical discovery; exact certification above is independent of NumPy.
import json,time
from pathlib import Path
def load_system(path):
    import os
    for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","VECLIB_MAXIMUM_THREADS","NUMEXPR_NUM_THREADS"):
        os.environ[key]="1"
    import numpy as np
    data=json.loads(Path(path).read_text())
    assert data['closed'] and data.get('coefficients_complete',True)
    n=data['dimension'];S=np.zeros(n);K=np.zeros((n,n));N=np.zeros((n,n,n))
    for i,v in data['S'].items():S[int(i)]=float(Q(v))
    for j,row in data['K'].items():
        for i,v in row.items():K[int(i),int(j)]=float(Q(v))
    for key,row in data['N'].items():
        i,j=map(int,key.split(','))
        for k,v in row.items():N[int(k),i,j]=N[int(k),j,i]=float(Q(v))
    d=list(map(lambda x:float(Q(x)),data['gram']))
    def product(mask):
        ans=1.
        for i,di in enumerate(d):
            if mask>>i&1:ans*=di
        return ans
    scales=[]
    for row in data['basis']:
        square=sum(abs(product(int(c))/product(int(e)))*float(Q(v))**2 for e,c,v in row)
        scales.append(np.sqrt(square))
    scales=np.asarray(scales)
    assert np.all(scales>0)
    return data,S*scales,K*scales[:,None]/scales[None,:],N*scales[:,None,None]/scales[None,:,None]/scales[None,None,:],scales


def continue_branch(path,output,target=1.,initial_step=.001,min_step=1e-8,max_steps=2000):
    import numpy as np
    started=time.monotonic();data,S,K,N,scales=load_system(path);n=len(S);I=np.eye(n)
    def qterm(x):return np.einsum('kij,i,j->k',N,x,x,optimize=True)
    def F(x,h):return x+h*(S+K@x+qterm(x))
    def J(x,h):return I+h*(K+2*np.einsum('kij,j->ki',N,x,optimize=True))
    def newton(x,h):
        x=x.copy()
        for iteration in range(30):
            f=F(x,h);norm=float(np.max(np.abs(f)))
            tolerance=2e-12*(1+float(np.max(np.abs(x))))
            if norm<tolerance:return x,True,iteration,norm
            try:step=np.linalg.solve(J(x,h),-f)
            except np.linalg.LinAlgError:return x,False,iteration,norm
            alpha=1.;accepted=False
            for _ in range(18):
                candidate=x+alpha*step;newnorm=float(np.max(np.abs(F(candidate,h))))
                if np.isfinite(newnorm) and newnorm<norm:
                    x=candidate;accepted=True;break
                alpha*=.5
            if not accepted:return x,False,iteration,norm
        return x,False,30,float(np.max(np.abs(F(x,h))))
    x=np.zeros(n);h=0.;step=initial_step;history=[];reason='step_limit'
    for count in range(max_steps):
        if h>=target:reason='target_reached';break
        attempted=min(step,target-h)
        try:predictor=x-attempted*np.linalg.solve(J(x,h),S+K@x+qterm(x))
        except np.linalg.LinAlgError:predictor=x.copy()
        trial,ok,iterations,residual=newton(predictor,h+attempted)
        if not ok:
            step*=.5
            event={'accepted':False,'h':h,'attempted_step':attempted,'next_step':step,'residual':residual}
            history.append(event);print(json.dumps(event),flush=True)
            if step<min_step:reason='parameter_continuation_stalled_not_exclusion';break
            continue
        h+=attempted;x=trial
        condition=float(np.linalg.cond(J(x,h)))
        event={'accepted':True,'h':h,'step':attempted,'iterations':iterations,'residual':residual,
               'jacobian_condition':condition,'scaled_norm':float(np.max(np.abs(x)))}
        history.append(event);print(json.dumps(event),flush=True)
        if iterations<=4:step=min(step*1.45,.05)
        elif iterations>=10:step*=.65
        if h>=target-1e-14:reason='target_reached';h=target;break
    original=x/scales
    try:
        inv=np.linalg.inv(J(x,h));R=inv*scales[None,:]/scales[:,None]
        inverse=[[format(v,'.17g') for v in row] for row in R]
    except np.linalg.LinAlgError:inverse=None
    result={'status':reason,'h':h,'kappa':None if h==0 else 1/h,'dimension':n,
            'source_polynomial':str(path),'coordinates':[format(v,'.17g') for v in original],
            'approximate_inverse_normalized_J':inverse,
            'normalization':'F_h=x+h(S+Kx+Nxx); at h1 identical to kappa1 Euler',
            'history':history,'elapsed_seconds':time.monotonic()-started,
            'ceiling':'floating candidate/continuation trace only; requires exact local-ball certification'}
    Path(output).write_text(json.dumps(result,indent=2)+'\n')
    return result



def search_target(polynomial,previous,output,trials=120,max_roots=2):
    import numpy as np
    started=time.monotonic();data,S,K,N,scales=load_system(polynomial);n=len(S);I=np.eye(n)
    odd=np.array([i for i,p in enumerate(data['basis_parity']) if p==1],dtype=int)
    even=np.array([i for i,p in enumerate(data['basis_parity']) if p==0],dtype=int)
    assert len(odd)==32 and len(even)==27
    assert np.max(np.abs(S[even]))==0 and np.max(np.abs(K[np.ix_(odd,odd)]))==0 and np.max(np.abs(K[np.ix_(even,even)]))==0
    for pair,row in data['N'].items():
        i,j=map(int,pair.split(','))
        assert all(data['basis_parity'][int(k)]==(1+data['basis_parity'][i]+data['basis_parity'][j])%2 for k in row)
    def F(x):return x+S+K@x+np.einsum('kij,i,j->k',N,x,x,optimize=True)
    def J(x):return I+K+2*np.einsum('kij,j->ki',N,x,optimize=True)
    def complete(o):
        x=np.zeros(n);x[odd]=o
        M=np.eye(len(even))+2*np.einsum('kij,i->kj',N[np.ix_(even,odd,even)],o,optimize=True)
        x[even]=np.linalg.solve(M,-K[np.ix_(even,odd)]@o)
        return x
    def evaluate(z,reduced):
        x=complete(z) if reduced else z
        f=F(x);j=J(x)
        if not reduced:return x,f,j
        schur=j[np.ix_(odd,odd)]-j[np.ix_(odd,even)]@np.linalg.solve(j[np.ix_(even,even)],j[np.ix_(even,odd)])
        return x,f[odd],schur
    def solve(seed,reduced):
        z=seed[odd].copy() if reduced else seed.copy();best=None
        for iteration in range(70):
            try:x,f,j=evaluate(z,reduced)
            except (np.linalg.LinAlgError,FloatingPointError):break
            norm=float(np.max(np.abs(f)));fullnorm=float(np.max(np.abs(F(x))))
            if not np.isfinite(norm) or np.max(np.abs(x))>1e8:break
            if best is None or fullnorm<best[0]:best=(fullnorm,x.copy(),iteration)
            if fullnorm<1e-10*(1+np.max(np.abs(x))):return x,True,iteration,fullnorm
            try:step=np.linalg.solve(j,-f)
            except np.linalg.LinAlgError:break
            accepted=False;alpha=1.
            for _ in range(24):
                try:xx,ff,jj=evaluate(z+alpha*step,reduced);newnorm=float(np.max(np.abs(ff)))
                except (np.linalg.LinAlgError,FloatingPointError):newnorm=np.inf
                if np.isfinite(newnorm) and newnorm<norm:
                    z+=alpha*step;accepted=True;break
                alpha*=.5
            if not accepted:break
        return (best[1],False,best[2],best[0]) if best else (seed,False,0,np.inf)
    previous_data=json.loads(Path(previous).read_text());branch=np.array([float(Q(v)) for v in previous_data['coordinates']])*scales
    seeds=[('zero',np.zeros(n)),('small_branch',branch),('minus_source',-S),
           ('minus_half_source',-.5*S),('minus_double_source',-2*S),('source',S)]
    for factor in (.5,2.,-1.,-2.,4.,-4.):seeds.append((f'branch_times_{factor}',factor*branch))
    for i in odd[:3]:
        for amplitude in (-5.,-1.,1.,5.):
            x=np.zeros(n);x[i]=amplitude;seeds.append((f'grade1_{i}_{amplitude}',x))
    rng=np.random.default_rng(20261125)
    while len(seeds)<trials:
        amplitude=(.1,.5,1.,2.,4.,8.,16.)[len(seeds)%7]
        x=rng.normal(size=n);x*=amplitude/max(np.max(np.abs(x)),1e-15)
        seeds.append((f'deterministic_random_{len(seeds)}_amp{amplitude}',x))
    history=[];roots=[];best=None
    def save():
        Path(output).write_text(json.dumps({'roots':roots,'attempts':history,'best_residual':None if best is None else best[0],
          'best_coordinates':None if best is None else [format(v,'.17g') for v in best[1]/scales],
          'elapsed_seconds':time.monotonic()-started,'ceiling':'numerical root discovery only; no failed-solver exclusion'},indent=2)+'\n')
    for name,seed in seeds[:trials]:
        for reduced in (True,False):
            x,ok,it,res=solve(seed,reduced)
            if np.isfinite(res) and (best is None or res<best[0]):best=(res,x.copy())
            event={'seed':name,'mode':'odd32_Schur' if reduced else 'full59','success':bool(ok),
                   'iterations':it,'residual':res,'seconds':time.monotonic()-started}
            history.append(event);print(json.dumps(event),flush=True)
            if ok and all(np.max(np.abs(x-np.array([float(Q(v)) for v in r['coordinates']])*scales))>1e-6 for r in roots):
                jac=J(x);condition=float(np.linalg.cond(jac));inv=np.linalg.inv(jac)
                R=inv*scales[None,:]/scales[:,None]
                root={'status':'numerical_kappa1_candidate','h':1.,'kappa':1.,'dimension':n,
                      'source_polynomial':str(polynomial),'coordinates':[format(v,'.17g') for v in x/scales],
                      'approximate_inverse_normalized_J':[[format(v,'.17g') for v in row] for row in R],
                      'seed':name,'mode':event['mode'],'residual':res,'jacobian_condition':condition,
                      'ceiling':'candidate only; no certified connection to small-h branch'}
                roots.append(root)
                candidate_path=Path(output).with_name(Path(output).stem+f'-root{len(roots)}.json')
                candidate_path.write_text(json.dumps(root,indent=2)+'\n')
                print(json.dumps({'event':'candidate_saved','path':str(candidate_path),'condition':condition}),flush=True)
            save()
            if len(roots)>=max_roots:return
    save()



def follow_arclength(polynomial,previous,output,steps=1200,initial_step=.01):
    import numpy as np
    started=time.monotonic();data,S,K,N,scales=load_system(polynomial);n=len(S);I=np.eye(n)
    previous_data=json.loads(Path(previous).read_text())
    z=np.r_[np.array([float(Q(v)) for v in previous_data['coordinates']])*scales,float(previous_data['h'])]
    def qterm(x):return np.einsum('kij,i,j->k',N,x,x,optimize=True)
    def F(z):
        x,h=z[:-1],z[-1];return x+h*(S+K@x+qterm(x))
    def block(z):
        x,h=z[:-1],z[-1]
        J=I+h*(K+2*np.einsum('kij,j->ki',N,x,optimize=True))
        Gh=S+K@x+qterm(x)
        return J,Gh
    def tangent(z,previous=None):
        J,Gh=block(z);_,sv,Vh=np.linalg.svd(np.column_stack((J,Gh)),full_matrices=True)
        t=Vh[-1]
        if previous is None:
            orientation=np.r_[-np.linalg.solve(J,Gh),1.]
        else:orientation=previous
        if np.dot(t,orientation)<0:t=-t
        return t,float(sv[-1])
    def correct(pred,t):
        q=pred.copy()
        for iteration in range(25):
            residual=np.r_[F(q),np.dot(t,q-pred)];norm=float(np.max(np.abs(residual)))
            if norm<2e-12*(1+np.max(np.abs(q))):return q,True,iteration,norm
            J,Gh=block(q);A=np.vstack((np.column_stack((J,Gh)),t))
            try:delta=np.linalg.solve(A,-residual)
            except np.linalg.LinAlgError:return q,False,iteration,norm
            alpha=1.;accepted=False
            for _ in range(18):
                trial=q+alpha*delta
                val=float(np.max(np.abs(np.r_[F(trial),np.dot(t,trial-pred)])))
                if np.isfinite(val) and val<norm:q=trial;accepted=True;break
                alpha*=.5
            if not accepted:return q,False,iteration,norm
        return q,False,25,float(np.max(np.abs(F(q))))
    t,rankmargin=tangent(z);ds=initial_step;history=[];folds=[];candidates=[];reason='step_limit'
    def save():
        Path(output).write_text(json.dumps({'status':reason,'last_h':float(z[-1]),
          'last_coordinates':[format(v,'.17g') for v in z[:-1]/scales],
          'history':history,'fold_crossings':folds,'kappa1_candidates':candidates,
          'elapsed_seconds':time.monotonic()-started,
          'ceiling':'numerical connected-path evidence only; no exclusion or rigorous fold certificate'},indent=2)+'\n')
    for index in range(steps):
        old=z.copy();oldt=t.copy();trial,ok,it,res=correct(z+ds*t,t)
        if not ok:
            ds*=.5
            if ds<1e-7:reason='arclength_corrector_stalled_not_exclusion';break
            continue
        z=trial;t,rankmargin=tangent(z,oldt)
        event={'step':index,'h':float(z[-1]),'arc_step':ds,'tangent_h':float(t[-1]),
               'scaled_norm':float(np.max(np.abs(z[:-1]))),'residual':res,
               'augmented_rank_margin':rankmargin,'iterations':it}
        history.append(event);print(json.dumps(event),flush=True)
        if oldt[-1]*t[-1]<0:
            fold={'between_steps':[index-1,index],'h_bracket':[float(old[-1]),float(z[-1])],
                  'coordinates':[format(v,'.17g') for v in z[:-1]/scales],
                  'scaled_tangent':list(map(float,t)), 'ceiling':'numerical turning point only'}
            folds.append(fold);print(json.dumps({'event':'fold_crossing',**fold}),flush=True)
        if (old[-1]-1)*(z[-1]-1)<=0 and old[-1]!=z[-1]:
            # Refine an actual h=1 intersection, not a nearby arclength point.
            weight=(1-old[-1])/(z[-1]-old[-1]);x=old[:-1]+weight*(z[:-1]-old[:-1])
            found=False
            for _ in range(30):
                fixed=np.r_[x,1.];f=F(fixed);J,Gh=block(fixed)
                if np.max(np.abs(f))<1e-11*(1+np.max(np.abs(x))):found=True;break
                try:x+=np.linalg.solve(J,-f)
                except np.linalg.LinAlgError:break
            if found:
                J,_=block(np.r_[x,1.]);inverse=np.linalg.inv(J)*scales[None,:]/scales[:,None]
                candidate={'status':'arclength_kappa1_candidate','h':1.,'kappa':1.,'dimension':n,
                  'coordinates':[format(v,'.17g') for v in x/scales],
                  'approximate_inverse_normalized_J':[[format(v,'.17g') for v in row] for row in inverse],
                  'source_polynomial':str(polynomial),'ceiling':'numerical path and root; needs exact certification'}
                path=Path(output).with_name(Path(output).stem+f'-root{len(candidates)+1}.json')
                path.write_text(json.dumps(candidate,indent=2)+'\n');candidates.append(str(path))
                reason='kappa1_crossing_found';save();return
        if not np.all(np.isfinite(z)) or np.max(np.abs(z[:-1]))>1e4:
            reason='large_coordinate_window_reached_not_exclusion';break
        if abs(z[-1])>3:
            reason='parameter_window_reached';break
        if it<=4:ds=min(ds*1.3,.1)
        elif it>=10:ds*=.65
        save()
    save()



def refine_numeric(polynomial,candidate,output):
    import numpy as np
    data,S,K,N,scales=load_system(polynomial);n=len(S)
    guess=json.loads(Path(candidate).read_text());h=float(guess['h'])
    x=np.array([float(Q(v)) for v in guess['coordinates']])*scales
    for step in range(4):
        f=x+h*(S+K@x+np.einsum('kij,i,j->k',N,x,x,optimize=True))
        J=np.eye(n)+h*(K+2*np.einsum('kij,j->ki',N,x,optimize=True))
        x-=np.linalg.solve(J,f)
    J=np.eye(n)+h*(K+2*np.einsum('kij,j->ki',N,x,optimize=True))
    R=np.linalg.inv(J)*scales[None,:]/scales[:,None]
    guess.update(coordinates=[format(v,'.17g') for v in x/scales],
       approximate_inverse_normalized_J=[[format(v,'.17g') for v in row] for row in R])
    Path(output).write_text(json.dumps(guess,indent=2)+'\n')

def numerical_main():
    import argparse,os
    for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
        os.environ[key]='1'
    parser=argparse.ArgumentParser(description='Optional discovery from the owned exact polynomial; use native probe for acceptance.')
    parser.add_argument('operation',choices=['continue','search','arclength','refine','certify'])
    parser.add_argument('polynomial');parser.add_argument('--previous');parser.add_argument('--output',required=True)
    parser.add_argument('--steps',type=int,default=1200);parser.add_argument('--target',type=float,default=1.)
    a=parser.parse_args()
    if a.operation=='continue':continue_branch(a.polynomial,a.output,target=a.target)
    elif a.operation=='search':search_target(a.polynomial,a.previous,a.output)
    elif a.operation=='arclength':follow_arclength(a.polynomial,a.previous,a.output,steps=a.steps)
    elif a.operation=='refine':refine_numeric(a.polynomial,a.previous,a.output)
    else:
        answer=certificate_for(json.loads(Path(a.polynomial).read_text()),json.loads(Path(a.previous).read_text()))
        Path(a.output).write_text(json.dumps(answer,indent=2)+'\n')
        print(answer['status'])

if __name__=='__main__':numerical_main()
