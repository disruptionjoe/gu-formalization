#!/usr/bin/env python3
"""Exact graded-word variation and native wedge controls, without matrix census.
Source field-space and physical interpretation remain separate reviewed claims.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json, sys, time
sys.dont_write_bytecode = True
from shiab_graded_derivation_probe import (
    theta, prod as native_prod, add as native_add, scale as native_scale,
)
from shiab_bianchi_companion_probe import hodge

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT/'lab/process/wedge-shiab-action-recheck-certificates.json'
DEG = {'T':1, 'F':2, 'Y':2, 'H':11, 'K':12, 'v':1, 'dv':2, 'h':11}

def add(*args):
    z={}
    for a in args:
        for w,c in a.items(): z[w]=z.get(w,F(0))+c
    return {w:c for w,c in z.items() if c}

def scale(c,a): return {w:c*v for w,v in a.items() if c*v}
def letter(x): return {(x,):F(1)}
def mul(*args):
    out={():F(1)}
    for arg in args:
        z={}
        for w,c in out.items():
            for v,d in arg.items(): z[w+v]=z.get(w+v,F(0))+c*d
        out={w:c for w,c in z.items() if c}
    return out

T,H,K,Y,R = map(letter,['T','H','K','Y','F'])
DR={'T':Y,'H':K,'F':{},'Y':add(mul(R,T),scale(-1,mul(T,R))),
    'K':add(mul(R,H),scale(-1,mul(H,R)))}

def derivative(poly):
    out={}
    for w,c in poly.items():
        degree=0
        for j,x in enumerate(w):
            out=add(out,scale(c*(-1)**degree,mul({w[:j]:F(1)},DR[x],{w[j+1:]:F(1)})))
            degree+=DEG[x]
    return out

def vary(poly, replacements):
    out={}
    for w,c in poly.items():
        for j,x in enumerate(w):
            if x in replacements:
                out=add(out,scale(c,mul({w[:j]:F(1)},replacements[x],{w[j+1:]:F(1)})))
    return out

def euler(poly, symbol='v', derivative_symbol='dv'):
    """Move the sole variation to the left by graded cyclicity, then IBP."""
    out={}; boundary={}
    for w,c in poly.items():
        positions=[i for i,x in enumerate(w) if x in [symbol,derivative_symbol]]
        assert len(positions)==1
        j=positions[0]; before=w[:j]; after=w[j:]
        sign=(-1)**(sum(DEG[x]for x in before)*sum(DEG[x]for x in after))
        rest=w[j+1:]+before; piece={rest:c*sign}
        if w[j]==symbol: out=add(out,piece)
        else:
            # integral Dv X = (-1)^(deg(v)+1) integral v DX.
            out=add(out,scale((-1)**(DEG[symbol]+1),derivative(piece)))
            boundary=add(boundary,piece)
    return out,boundary

def anti(a,b): return add(mul(a,b),mul(b,a))
def serialize(p): return [{'word':' '.join(w),'coefficient':str(c)}for w,c in sorted(p.items())]

def build():
    checks=[]
    def ck(n,v): assert v,n;checks.append(n)
    density=mul(H,add(anti(R,T),scale(F(1,2),anti(Y,T)),scale(F(2,3),mul(T,T,T))))
    et,bt=euler(vary(density,{'T':letter('v'),'Y':letter('dv')}))
    eb,bb=euler(vary(density,{'F':letter('dv'),'Y':anti(letter('v'),T)}))
    eh,bh=euler(vary(density,{'H':letter('h')}),symbol='h')
    expected_et=add(scale(-1,anti(H,add(R,Y))),scale(F(1,2),anti(K,T)),
                    scale(-F(2,3),add(anti(H,mul(T,T)),scale(-1,mul(T,H,T)))))
    expected_eb=add(anti(K,T),scale(-1,anti(H,Y)),scale(-F(1,2),anti(H,mul(T,T))),mul(T,H,T))
    expected_eh=add(anti(R,T),scale(F(1,2),anti(Y,T)),scale(F(2,3),mul(T,T,T)))
    ck('primitive variation independently extracted',et==expected_et)
    ck('reference connection variation independently extracted',eb==expected_eb)
    ck('moving insertion variation independently extracted',eh==expected_eh)
    residual=add(mul(H,T),scale(-1,mul(T,H)))
    ck('primitive boundary exact',bt==scale(F(1,2),residual))
    ck('reference boundary exact',bb==residual and not bh)
    ka=add(K,anti(T,H));fa=add(R,Y,mul(T,T));sfa=scale(-1,anti(H,fa))
    ck('compact own Euler equation',et==add(sfa,scale(F(1,6),anti(add(K,scale(2,ka)),T))))
    ck('full moving Noether identity',not add(derivative(eb),anti(T,et),anti(H,eh)))
    eps=add(derivative(add(et,scale(-1,eb))),scale(-1,anti(H,eh)))
    daet=add(derivative(et),anti(T,et))
    ck('epsilon source pullback redundancy',eps==daet)
    ck('reference row compact current',eb==add(derivative(residual),scale(F(1,2),
       add(mul(T,residual),scale(-1,mul(residual,T))))))
    packet=add(R,scale(F(1,2),Y),scale(F(1,3),mul(T,T)))
    dapacket=add(derivative(packet),mul(T,packet),scale(-1,mul(packet,T)))
    ck('completed packet derivative',dapacket==add(scale(F(1,2),add(mul(T,R),scale(-1,mul(R,T)))),
       scale(F(1,6),add(mul(T,Y),scale(-1,mul(Y,T))))))
    s2=scale(-1,anti(H,packet))
    das2=add(derivative(s2),anti(T,s2))
    ck('moving companion defect exact',das2==add(mul(H,dapacket),scale(-1,mul(dapacket,H)),scale(-1,anti(ka,packet))))
    ck('general moving correction not identically zero',bool(add(et,scale(-1,sfa))))
    # A genuine algebraic positive control is central parallel H; in that
    # quotient H T=-T H and H Y=Y H, restoring the unit curvature endpoint.
    def centralize(p):
        out={}
        for w,c in p.items():
            if 'K'in w:continue
            hh=w.index('H') if 'H'in w else -1
            if hh>=0:
                c*=(-1)**sum(DEG[x]for x in w[:hh]);w=('H',)+w[:hh]+w[hh+1:]
            out=add(out,{w:c})
        return out
    ck('central parallel comparator restores endpoint',not centralize(add(et,scale(-1,sfa))))
    # Native noncentral Clifford insertion: no large spinor matrices or old
    # Einstein-basis replay. Test the exact extra quadratic term directly.
    witnesses={}
    for label,eta in [('K95',[-1,1,1,1]+[1]*6+[-1]*4),('K77',[1]*7+[-1]*7)]:
        th=theta(14,eta)
        t={(1,4):F(1),(2,8):F(1)} # e0 gamma2 + e1 gamma3, primary-minus skew.
        np=lambda a,b:native_prod(a,b,eta)
        t2=np(t,t);kt=native_add(np(t,th),np(th,t))
        correction=native_scale(native_add(np(kt,t),np(t,kt)),F(1,3))
        own=native_scale(native_add(np(th,t2),np(t2,th),native_scale(np(np(t,th),t),-1)),-F(2,3))
        printed=native_scale(native_add(np(th,t2),np(t2,th)),-1)
        ck(label+' actual noncentral correction',bool(correction))
        ck(label+' actual own/printed difference',native_add(own,native_scale(printed,-1))==correction)
        ck(label+' theta has correct degree and Clifford grade',all(f.bit_count()==11 and c.bit_count()==3 for f,c in th))
        star_t=hodge(t,eta)
        ck(label+' ordinary metric mass commutator vanishes',not native_add(np(t,star_t),np(star_t,t)))
        witnesses[label]={'T':[[f,c,str(v)]for(f,c),v in t.items()],
          'difference':[[f,c,str(v)]for(f,c),v in sorted(correction.items())],
          'difference_is_existing_endpoint_exclusion_control':True}
    deps=['tests/program-focus/shiab_graded_derivation_probe.py','tests/program-focus/shiab_bianchi_companion_probe.py',
          'explorations/conditional-build/shiab-bianchi-companion-class-2026-11-27.md',
          'explorations/conditional-build/full-shiab-variational-consistency-2026-11-27.md',
          'explorations/conditional-build/source-prescription-current-2026-11-13.md']
    return {'schema':'gu-wedge-action-recheck-v1','status':'PASS','check_count':len(checks),'check_names':checks,
      'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in deps},
      'rows':{'E_T':serialize(et),'E_B':serialize(eb),'E_Theta':serialize(eh),'epsilon':serialize(eps)},
      'native_witnesses':witnesses,'limits':['Free graded-word identities and native constant-displacement checks; source field-space bridge separately reviewed.',
      'Theta is not an independently variable source field; use the metric/epsilon pullback.',
      'No physical norm, positive energy, native stationary vacuum or source-GU verdict.']}

if __name__=='__main__':
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group(required=True)
    g.add_argument('--write',action='store_true');g.add_argument('--verify',action='store_true');a=p.parse_args()
    start=time.monotonic();data=build()
    if a.write:OUTPUT.write_text(json.dumps(data,indent=2)+'\n')
    else:assert json.loads(OUTPUT.read_text())==data
    print(json.dumps({'status':'PASS','checks':data['check_count'],'seconds':time.monotonic()-start}))
