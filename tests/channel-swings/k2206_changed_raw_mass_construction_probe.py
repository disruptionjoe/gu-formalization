#!/usr/bin/env python3
"""Exact independent sparse-Clifford controls; no dense1920 matrices."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import argparse, hashlib, json

ETA=(1,)*7+(-1,)*7
OBS=(0,7,8,9)
UN=tuple(k for k in range(14) if k not in OBS)
ONE={0:F(1)}
ZERO={}

def add(*xs):
    out={}
    for x in xs:
        for m,c in x.items(): out[m]=out.get(m,0)+c
    return {m:c for m,c in out.items() if c}

def scale(x,s): return {m:c*s for m,c in x.items() if c*s}

def mul(x,y):
    out={}
    for a,c in x.items():
        for b,d in y.items():
            sign=1
            for i in range(14):
                if (a>>i)&1:
                    if (b&((1<<i)-1)).bit_count()%2: sign=-sign
                    if (b>>i)&1: sign*=ETA[i]
            out[a^b]=out.get(a^b,0)+sign*c*d
    return {m:c for m,c in out.items() if c}

def blade(indices):
    v=ONE
    for k in indices: v=mul(v,{1<<k:F(1)})
    return v

def star(x,fault=None):
    return {m:c*(-1)**(m.bit_count()*(m.bit_count()+(3 if fault=='adjoint_sign' else 1))//2) for m,c in x.items()}

def transpose(x):
    out={}
    for m,c in x.items():
        r=m.bit_count()
        s=(-1)**(r*(r-1)//2)
        for k in range(14):
            if m>>k&1: s*=ETA[k]
        out[m]=c*s
    return out

G=[{1<<k:F(1)} for k in range(14)]
J=blade(range(14))
W=scale(add(scale(ONE,3),scale(J,-1)),F(1,2))
WB=scale(add(scale(ONE,3),J),F(1,2))
GM=[mul(g,WB) for g in G]
FF=[F(-1)]*14+[F(2)]

def raw(k,a,c,fault=None):
    if a<14 and c<14 and len({a,k,c})==3:
        return scale(mul(blade((a,k,c)),W),ETA[a])
    if a==k and c==14: return ONE
    if a==14 and c==k: return scale(ONE,ETA[k] if fault=='raw_return_sign' else -ETA[k])
    return ZERO

def raw_lower(fault=None):
    tr=[scale(G[k],ETA[k]) for k in range(14)]+[WB]
    inv=G+[scale(W,F(1,2))]
    om=ONE if fault=='replace_gamma0_by_scalar' else G[0]
    return {(a,c):v for a in range(15) for c in range(15)
            if (v:=mul(mul(inv[a],mul(raw(0,a,c,fault),om)),tr[c]))}

def scalar_m(k,a,c):
    if a<14 and c<14 and len({a,k,c})==3:return F(1)
    if a==k and c==14:return F(1)
    if a==14 and c==k:return F(-1,2)
    return F(0)

def blockmul(x,y):
    out={}
    for (a,b),v in x.items():
        for (bb,c),w in y.items():
            if b==bb: out[a,c]=add(out.get((a,c),ZERO),mul(v,w))
    return {k:v for k,v in out.items() if v}

def sharp(x,fault=None):
    return {(c,a):scale(star(v,fault),FF[a]/FF[c]) for (a,c),v in x.items()}

def chars(m,observed=OBS):
    return tuple((-1)**(m.bit_count()-((m>>k)&1)) for k in observed)

def derivative(poly,k):
    out={}
    for exponent,c in poly.items():
        if exponent[k]:
            e=list(exponent);e[k]-=1
            out[tuple(e)]=c*exponent[k]
    return out

def pdiff(p,q):
    out=dict(p)
    for e,c in q.items():out[e]=out.get(e,0)-c
    return {e:c for e,c in out.items() if c}


def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    T=blade(UN); A0=mul(T,G[0]); A=mul(T,blade((7,8,9)))
    if fault=='gamma0_coefficient':A=G[0]
    if fault=='wrong_source_axis':A=A0
    E=mul(J,W); EF=mul(J,WB)
    ck('mass_grade13',set(m.bit_count() for m in A)=={13})
    ck('mass_real_skew',transpose(A)==scale(A,-1))
    ck('mass_square',mul(A,A)==scale(ONE,-1))
    ck('mass_gamma0_volume',mul(G[0],A)==J)
    ck('two_mass_axes_anticommute',add(mul(A0,A),mul(A,A0))==ZERO)
    ck('second_axis_square',mul(A0,A0)==scale(ONE,-1))
    ck('second_axis_skew',transpose(A0)==scale(A0,-1))
    for k in UN:
        ck('normal_commutation_'+str(k),mul(A,G[k])==mul(G[k],A))
        ck('trace_Hq_compatibility_'+str(k),add(mul(star(A),G[k]),mul(G[k],A))==ZERO)
        ck('other_axis_Hq_countercontrol_'+str(k),add(mul(star(A0),G[k]),mul(G[k],A0))!=ZERO)
    for k in OBS[1:]:
        Ck=mul(G[0],G[k]);ck('spatial_symmetric_'+str(k),transpose(Ck)==Ck)
        ck('mass_spatial_anticommutation_'+str(k),add(mul(A,Ck),mul(Ck,A))==ZERO)
    # Entire blade basis: a complete exact linear character calculation.
    axes=[m for m in range(1<<14) if all((-1)**(m.bit_count()-((m>>k)&1))==1 for k in UN)
          and all((((m>>0)&1)+((m>>k)&1))%2==1 for k in OBS[1:])]
    ck('complete_mass_space',axes==sorted(list(A0)+list(mul(T,blade((7,8,9))))))
    tr=[scale(G[k],ETA[k]) for k in range(14)]+[WB];inv=G+[scale(W,F(1,2))]
    if fault=='aux_normalization':inv[-1]=W
    K={(a,c):v for a in range(15) for c in range(15) if (v:=mul(mul(inv[a],mul(raw(0,a,c,'raw_return_sign' if fault=='return_sign' else None),A)),tr[c]))}
    for a in range(15):
        for c in range(15):ck(f'raw_block_{a}_{c}',K.get((a,c),ZERO)==scale(EF if c==14 else E,scalar_m(0,a,c)*(-1 if c==0 else 1)))
    PV={(a,c):scale(ONE,F(int(a==c))-F(1,10)) for a in UN for c in UN}
    ck('no_sector_leakage',blockmul(K,PV)==blockmul(PV,K))
    ck('actual_mass_on_V',blockmul(K,PV)=={k:scale(mul(v,E),-1) for k,v in PV.items()})
    KS=sharp(K);ck('C_pair_equations',K.get((7,8))==E and KS.get((7,8))==scale(EF,-1) and K.get((0,14))==EF and KS.get((0,14))==EF)
    central=[m for m in range(1<<14) if chars(m)==(1,1,1,1)]
    ck('complete_pairing_parity',all((mul(z,E)==scale(mul(EF,z),-1))==(m.bit_count()%2==1) for m in central for z in [({m:F(1)} if m.bit_count()%2==0 else mul({m:F(1)},WB))]))
    z=mul(blade((0,7,8,9,1,2,3)),WB)
    if fault=='even_pairing':z=ONE
    X={k:mul(v,z) for k,v in PV.items()}
    ck('full225_pairing_witness',blockmul(X,K)==blockmul(KS,X))
    ck('witness_square',mul(z,z)==scale(ONE,2))
    ck('witness_selfadjoint',star(z)==z)
    Ns=[mul(mul(inv[c],A),tr[c]) for c in range(15)]
    ck('full_evolution_normalization',all(Ns[c]==(mul(A,scale(mul(WB,WB),F(1,2))) if c==14 else scale(A,-1 if c==0 else 1)) for c in range(15)))
    # Actual graph equation coefficients: all observed outputs must coincide.
    ck('graph_t_forced_zero',add(Ns[0],scale(Ns[7],-1))==scale(A,-2))
    rem=add(scale(mul(WB,WB),F(1,2)),scale(ONE,-1))
    rinv=add(scale(ONE,F(-1,2)),scale(J,F(3,2)))
    if fault=='graph_inverse':rinv=add(scale(ONE,F(1,2)),scale(J,F(3,2)))
    ck('graph_sum_factor_inverse',mul(rem,rinv)==ONE)
    ck('graph_aux_minus_each_normal',all(add(Ns[14],scale(Ns[k],-1))==mul(A,rem) for k in UN))
    # Fourier generator square is checked at independent mixed rational momenta.
    for coeff in [(1,2,3),(F(2,3),F(-3,4),F(5,7))]:
        # Real Clifford representative H(k) uses spatial C and mass A; i terms
        # are handled as a complex pair (real, imaginary).
        real=scale(A,F(-5,3));imag=scale(add(*(scale(mul(G[0],G[k]),v) for k,v in zip(OBS[1:],coeff))),-1)
        ck('dispersion_'+str(coeff),add(mul(real,real),scale(mul(imag,imag),-1))==scale(ONE,-F(25,9)-sum(v*v for v in coeff)) and add(mul(real,imag),mul(imag,real))==ZERO)
    return out

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--write',action='store_true');args=pa.parse_args()
    cs=controls();assert all(cs.values()),[k for k,v in cs.items() if not v]
    faults={}
    for f in ['gamma0_coefficient','wrong_source_axis','aux_normalization','return_sign','even_pairing','graph_inverse']:
        bad=[k for k,v in controls(f).items() if not v];assert bad,('undetected',f);faults[f]=bad
    root=Path(__file__).resolve().parents[2]
    deps=['explorations/conditional-build/k2206-changed-raw-mass-construction-2026-10-28.md','explorations/conditional-build/k2200-observed-principal-pairing-freedom-2026-10-28.md','explorations/conditional-build/k2034-observed-principal-forms-2026-10-24.md','explorations/conditional-build/k2203-observed-lower-pairing-compatibility-2026-10-28.md']
    report=dict(result_id='K2206',status='conditional_common_raw_mass_and_sharp_positive_sector',checks=cs,fault_failures=faults,dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Universal character and sector proofs; complete finite blade character calculation; exact original225-block identities; genuine data/equation faults. Constant formal pairings and positive evolution metrics are different. No source selection, physical quotient, external-expert or proof-assistant claim.')
    dst=root/'lab/process/k2206-changed-raw-mass-construction.json'
    if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dst.read_text())==report,'report drift'
    print(json.dumps(dict(result='K2206',controls=len(cs),faults=len(faults))))
if __name__=='__main__':main()
