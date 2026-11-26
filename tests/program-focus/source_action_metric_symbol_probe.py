"""Exact highest-order coupled W2 metric/connection symbols.

No homogeneous ansatz is imposed on perturbations. Formal symbols replace
partial_mu by real xi_mu (no Fourier i). Pairing is -Re tr/128. This owns
orders (A,A)=1, (A,g)=3 and the vanishing order5 (g,g) block, NOT the
full off-section order4 block, a physical quotient, or a graviton spectrum.
The declared held-coordinate-one-form section order4 density is also tested.
"""
from fractions import Fraction as Q
from itertools import combinations
import json
from pathlib import Path
from source_action_physical_probe import interval
import source_action_deep_geometry as geo
from source_action_deep_algebra import Engine,add,scale,clean


def wedge_xi(xi,T):
    out={}
    for i,v in enumerate(xi):
        if not v:continue
        for (e,c),w in T.items():
            if e>>i&1:continue
            key=(e|1<<i,c)
            out[key]=out.get(key,Q(0))+v*w*Engine.sign(1<<i,e)
    return clean(out)


def wedge_adj(E,xi,W):
    out={}
    for (e,c),w in W.items():
        for i,v in enumerate(xi):
            if not v or not(e>>i&1):continue
            f=e^(1<<i);key=(f,c)
            out[key]=out.get(key,Q(0))+v*w*Engine.sign(1<<i,f)/E.d[i]
    return clean(out)


def symbols(E,xi,T):
    p=E.Phi(wedge_xi(xi,T))
    pt=wedge_adj(E,xi,E.Phi_adj(T))
    return scale(Q(1,2),add(p,scale(-1,pt))),scale(Q(1,2),add(p,pt))


def metric_symbol(base_diag,p,xi):
    """At y=eta; base constant g may differ from y. Symmetric frame ID.

    h=delta G has only horizontal/vertical blocks at principal order1.
    b=delta B is the symmetric-orthonormal-frame order2 symbol.
    Independent a must use this SAME identification. Holding a coordinate
    connection fixed in another moving spin frame needs its D_A u adapter.
    """
    eta=geo.eta;h=[[Q(0) for _ in range(14)] for _ in range(14)]
    for mu in range(4):
        Gam=[[Q(1,2)*(xi[mu]*p[r][j]+xi[j]*p[r][mu]-xi[r]*p[mu][j])/base_diag[r]
              for j in range(4)] for r in range(4)]
        C=[[eta[i]*Gam[i][j]+Gam[j][i]*eta[j] for j in range(4)] for i in range(4)]
        for Aidx,A in enumerate(geo.A,4):
            U=[[-2*eta[i]*A[i][j] for j in range(4)] for i in range(4)]
            value=sum(eta[i]*C[i][j]*eta[j]*U[j][i] for i in range(4) for j in range(4))
            value-=Q(1,2)*sum(eta[i]*C[i][i] for i in range(4))*sum(eta[i]*U[i][i] for i in range(4))
            h[mu][Aidx]=h[Aidx][mu]=-value
    b={}
    for i in range(14):
        for a,c in combinations(range(14),2):
            value=(xi[c]*h[i][a]-xi[a]*h[i][c])/(4*geo.d[a]*geo.d[c])
            if value:b[(1<<i,(1<<a)|(1<<c))]=value
    return h,b


def matrix_unit(i,j):
    p=[[Q(0) for _ in range(4)] for _ in range(4)]
    p[i][j]=p[j][i]=Q(1)
    return p


def section_order4(E):
    """Held Ahat COORDINATE ONE-FORM in symmetric spin identification.

    Baseline orthogonal coframe only REPORTS components; its variation is
    NOT used to hold Ahat coframe coefficients fixed. Full fibre integral,
    different spin adapters and elimination of connection fields are absent.
    """
    data=json.loads((Path(__file__).resolve().parents[2]/
                    'lab/process/source-action-deep-coefficients.json').read_text())
    basis=[{(int(e),int(c)):Q(v) for e,c,v in row} for row in data['basis']]
    roots=data['certified_roots']
    assert len(roots)==2 and all(Q(str(r['h']))==1 for r in roots)
    xi=[Q(0)]*14;xi[3]=Q(1)
    p=matrix_unit(1,1);p[2][2]=Q(-1)
    q=matrix_unit(1,2)
    assert sum(geo.eta[i]*p[i][i] for i in range(4))==0
    assert sum(geo.eta[i]*q[i][i] for i in range(4))==0
    assert all(not p[3][i] and not q[3][i] for i in range(4))
    _,bp=metric_symbol(geo.eta,p,xi);_,bq=metric_symbol(geo.eta,q,xi)
    def coeff(b):
        assert not wedge_xi(xi,b) and not E.wedge(b,b)
        W=E.Phi_adj(b)
        l=[-Q(1,6)*E.pair(W,add(E.wedge(b,T),E.wedge(T,b))) for T in basis]
        return Q(1,2)*E.pair(b,b),l
    mp,lp=coeff(bp);mq,lq=coeff(bq);ms,ls=coeff(add(bp,bq))
    mc=(ms-mp-mq)/2;lc=[(s-p-q)/2 for s,p,q in zip(ls,lp,lq)]
    # Nontrivial cubic/background receiver: dropping it changes the symbolic
    # answer, even before asking whether its value vanishes at a given root.
    assert any(lp) and any(lq)
    def shifted(l,m,r):
        z=interval(l,r)
        for key in ['center','lower','upper']:z[key]=str(Q(z[key])+m)
        z['approximate_center']=float(Q(z['center']))
        z['sign']='positive' if Q(z['lower'])>0 else ('negative' if Q(z['upper'])<0 else 'unresolved')
        return z
    out={}
    for name,m,l in [('TT_plus',mp,lp),('TT_cross',mq,lq),('polarized_cross',mc,lc)]:
        out[name]={'mass_only':str(m),'functional':list(map(str,l)),
                   'intervals':[shifted(l,m,r)for r in roots],
                   'background_correction_intervals':[interval(l,r)for r in roots]}
    # Direct native-Phi versus adjoint implementation on an actual basis
    # witness, guarding the cubic coefficient and transpose convention.
    j=next(i for i,v in enumerate(lp) if v)
    direct=-Q(1,6)*E.pair(bp,E.Phi(add(E.wedge(bp,basis[j]),E.wedge(basis[j],bp))))
    assert direct==lp[j] and direct!=0
    assert -Q(1,3)*E.pair(bp,E.Phi(add(E.wedge(bp,basis[j]),E.wedge(basis[j],bp))))!=direct
    assert mp==mq and lp==lq
    assert mc==0 and not any(lc)
    out['controls']={'mass_only_mutation_rejected':True,'wrong_cubic_factor_rejected':True,
                     'direct_and_adjoint_Phi_agree':True,
                     'two_TT_functionals_equal':mp==mq and lp==lq,
                     'polarized_cross_identically_zero':mc==0 and not any(lc),
                     'root_certificates_recomputed_here':False}
    out['scope']='Pointwise section principal-action coefficient per unit native volume in declared held-coordinate-one-form tangent, not integrated or physical gravity Hessian.'
    return out


def run():
    E=Engine(geo);checks=0;witness=None;section_checks=0;off_section_curvature=None
    # Full ten-dimensional metric amplitude space at a timelike/spacelike
    # and mixed covector; arbitrary field jets, not invariant field variations.
    for base in [geo.eta,[Q(2),Q(1),Q(1),Q(-1)]]:
        for xi4 in [(1,0,0,0),(0,0,0,1),(1,1,0,1)]:
            xi=list(map(Q,xi4))+[Q(0)]*10
            Bs=[]
            for i,j in combinations(range(4),2):
                _,b=metric_symbol(base,matrix_unit(i,j),xi);Bs.append(b)
            for i in range(4):
                _,b=metric_symbol(base,matrix_unit(i,i),xi);Bs.append(b)
            for b in Bs:
                assert all(c.bit_count()==2 for e,c in b);checks+=1
                kb,lb=symbols(E,xi,b)
                assert all(c.bit_count()%2 for e,c in kb);checks+=1
                # Every cross-amplitude order5 metric bilinear vanishes.
                for other in Bs:
                    assert E.pair(other,kb)==0;checks+=1
                if base==geo.eta:
                    # At the observation point delta G is a pure principal
                    # vertical coordinate shift: b=xi*u, hence D b=0.
                    assert not wedge_xi(xi,b);section_checks+=1
                elif wedge_xi(xi,b) and off_section_curvature is None:
                    off_section_curvature=[[e,c,str(v)]for(e,c),v in sorted(wedge_xi(xi,b).items())]
                if lb and witness is None:
                    key=next(iter(sorted(lb)))
                    a={key:Q(1)}
                    # Coefficient-adjoint and formal-adjoint sign controls.
                    p_a=E.Phi(wedge_xi(xi,a))
                    pt_b=wedge_adj(E,xi,E.Phi_adj(b))
                    assert E.pair(a,pt_b)==E.pair(p_a,b);checks+=1
                    val=E.pair(a,lb);assert val;checks+=1
                    assert E.pair(a,kb)!=val;checks+=1
                    witness={'base_diag':list(map(str,base)),'xi':list(map(str,xi4)),
                             'b':[[e,c,str(v)]for(e,c),v in sorted(b.items())],
                             'a':[key[0],key[1]],'mixed_symbol':str(val),
                             'sign_mutation':str(E.pair(a,kb))}
            # Pure frame-change connection jets a=xi*u have zero AA symbol
            # pairing against another such jet; this is a control, NOT the
            # full native gauge/Noether identity including geometry changes.
            u={(0,1):Q(1)};v={(0,3):Q(1)}
            a_u=wedge_xi(xi,u);a_v=wedge_xi(xi,v)
            assert a_u!=a_v
            assert not wedge_xi(xi,a_u) and not wedge_xi(xi,a_v);checks+=1
            k_v,l_v=symbols(E,xi,a_v)
            # Distinct amplitudes of opposite Clifford parity: neither the
            # same-vector skew identity nor trace parity forces this zero.
            assert E.pair(a_u,k_v)==0;checks+=1
    assert witness is not None
    assert off_section_curvature is not None
    return {'checks':checks,'section_principal_curvature_controls':section_checks,
            'nonzero_mixed_receiver':witness,
            'nonzero_off_section_curvature_symbol':off_section_curvature,
            'section_order4':section_order4(E),
            'scope':'Principal coupled symbols and stated section order4 density only; no full fibre integral, lower-order Noether complex or physical spectrum.'}

if __name__=='__main__':print(json.dumps(run(),indent=2))
