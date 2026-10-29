#!/usr/bin/env python3
"""K2233 exact full-raw controls; universal classification is the written proof."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tests/channel-swings'))
import k2206_changed_raw_mass_construction_probe as o
import argparse,hashlib,json
F=o.F; I=o.ONE; ZERO=o.ZERO; add=o.add; mul=o.mul; scale=o.scale
FAULTS=['raw_return','raw_order','temporal_sign','transport_sign','curvature_factor','even_pairing','holonomy_period','normal_volume','projector_grade']

def comm(x,y):return add(mul(x,y),scale(mul(y,x),-1))
def anti(x,y):return add(mul(x,y),mul(y,x))
def badd(*blocks):
    out={}
    for b in blocks:
        for key,v in b.items():out[key]=add(out.get(key,ZERO),v)
    return {k:v for k,v in out.items() if v}
def bs(b,s):return {k:scale(v,s) for k,v in b.items() if scale(v,s)}
def has_char(z,eps):return all(mul(z,o.GM[k])==scale(mul(o.GM[k],z),s) for k,s in zip(o.OBS,eps))

def run(fault=None):
    out=[]
    def ck(name,v):out.append((name,bool(v)))
    T=I if fault=='normal_volume' else o.blade(o.UN)
    A=mul(o.G[0],o.J);B=o.blade(range(7,14))
    C={j:mul(o.G[0],o.G[j]) for j in o.OBS[1:]}
    Xj={j:mul(C[j],T) for j in C}
    tr=[scale(o.G[k],o.ETA[k]) for k in range(14)]+[o.WB]
    inv=o.G+[scale(o.W,F(1,2))]
    PV={(a,c):scale(I,F(int(a==c))-F(1,10)) for a in o.UN for c in o.UN}
    DP={k:{(a,c):scale(o.GM[k],o.scalar_m(k,a,c)) for a in range(15) for c in range(15) if o.scalar_m(k,a,c)} for k in o.OBS}
    def rawlower(k,om):
        result={}
        for a in range(15):
            for c in range(15):
                raw=o.raw(k,a,c,'raw_return_sign' if fault=='raw_return' else None)
                product=mul(om,raw) if fault=='raw_order' else mul(raw,om)
                v=mul(mul(inv[a],product),tr[c])
                if v:result[a,c]=v
        return result
    ck('T_square',mul(T,T)==scale(I,-1))
    ck('T_B_skew',o.star(T)==scale(T,-1))
    ck('T_real_skew',o.transpose(T)==scale(T,-1))
    ck('T_mass_commutation',comm(T,A)==ZERO)
    ck('T_all_Gamma_commutation',all(comm(T,o.GM[k])==ZERO for k in o.OBS))
    central=[q for q in range(1<<14) if o.chars(q)==(1,1,1,1)]
    odd=[mul({q:F(1)},o.WB) for q in central if q.bit_count()%2]
    ck('Dodd_dimension512',len(odd)==512)
    for i,z in enumerate(odd):
        ck(f'Dodd_normal_volume_anti_{i}',anti(T,z)==ZERO)
    E=mul(o.J,o.W);EF=mul(o.J,o.WB)
    generators=[('mass',0,A,None),*[(f'a{j}',0,Xj[j],j) for j in C],('b',7,scale(Xj[7],-1) if fault=='temporal_sign' else Xj[7],0)]
    blocks={}
    for name,k,om,target in generators:
        K=rawlower(k,om);KS=o.sharp(K);blocks[name]=(K,KS)
        ck(name+'_V_C_preservation',o.blockmul(PV,K)==o.blockmul(K,PV))
        # Explicit full-block grammar independently evaluated from the original raw map.
        for a in range(15):
            for c in range(15):
                if target is None:
                    expected=scale(EF if c==14 else E,o.scalar_m(0,a,c)*(-1 if c==0 else 1))
                else:
                    j=7 if name=='b' else target
                    sign=-1 if c in (*o.UN,0,j) else 1
                    expected=scale(mul(o.GM[target],T),o.scalar_m(k,a,c)*sign)
                ck(f'{name}_original_block_{a}_{c}',K.get((a,c),ZERO)==expected)
        ck(name+'_original_bottom_return',mul(o.raw(k,14,k,'raw_return_sign' if fault=='raw_return' else None),om)==scale(om,-o.ETA[k]))
        if target is not None:
            eps=tuple(1 if p==target else -1 for p in o.OBS)
            ck(name+'_full_K_character',all(has_char(z,eps) for z in K.values()))
            ck(name+'_full_Ksharp_character',all(has_char(z,eps) for z in KS.values()))
        else:
            ck('mass_only_scalar_J_characters',all(set(z).issubset({0,(1<<14)-1}) for z in [*K.values(),*KS.values()]))
    chars=[(1,1,1,1),(-1,-1,-1,-1),*[tuple(1 if q==k else -1 for q in o.OBS) for k in o.OBS]]
    ck('six_character_separation',len(set(chars))==6)
    z=I if fault=='even_pairing' else mul(o.blade((0,7,8,9,1,2,3)),o.WB)
    ck('maximal_witness_square2',mul(z,z)==scale(I,2))
    ck('maximal_witness_B_selfadjoint',o.star(z)==z)
    ck('maximal_witness_J_odd',anti(z,o.J)==ZERO)
    ck('maximal_witness_Gamma_central',all(comm(z,o.GM[k])==ZERO for k in o.OBS))
    XX={key:mul(v,z) for key,v in PV.items()}
    for name,k,om,direction in generators:
        K,KS=blocks[name]
        rhs=badd(o.blockmul(XX,K),bs(o.blockmul(KS,XX),-1))
        derivative=scale(comm(T,z),-1 if fault=='transport_sign' else 1)
        lhs={} if direction is None else o.blockmul(DP[direction],{key:mul(v,derivative) for key,v in PV.items()})
        ck(name+'_full225_Green_identity',lhs==rhs)
    # Mass equations on C and V are tested without a constant-form shortcut.
    K,KS=blocks['mass']
    ck('mass_C_entry78',K[7,8]==E and KS[7,8]==scale(EF,-1))
    ck('mass_C_entry0h',K[0,14]==EF and KS[0,14]==EF)
    ck('mass_odd_survives',add(mul(z,E),mul(EF,z))==ZERO)
    ck('mass_even_rejected',add(E,EF)==scale(o.J,3) and add(E,EF)!=ZERO)
    # Rational genuine flat transport; U is B-unitary, not a raw-principal assertion.
    u=add(scale(I,F(3,5)),scale(T,F(4,5)));ui=o.transpose(u)
    zt=mul(mul(u,z),ui)
    ck('flat_frame_unitary',mul(u,ui)==I)
    ck('flat_frame_B_unitary',mul(o.star(u),u)==I)
    ck('flat_witness_moving',zt!=z)
    ck('flat_witness_square',mul(zt,zt)==scale(I,2))
    ck('flat_witness_symmetric',o.star(zt)==zt)
    ck('flat_witness_odd',anti(zt,o.J)==ZERO)
    ck('flat_witness_principal',all(comm(zt,o.GM[k])==ZERO for k in o.OBS))
    dz=comm(T,z)
    curvature=scale(mul(T,z),1 if fault=='curvature_factor' else 2)
    ck('curvature_commutator_exact',curvature==dz)
    ck('curvature_witness_invertible',mul(curvature,curvature)==scale(I,8))
    # Pi-period holonomy has spinor sign; Pi/2 gives minus the pairing.
    loop=T if fault=='holonomy_period' else scale(I,-1)
    ck('pi_period_pairing_descends',mul(mul(loop,z),o.transpose(loop))==z)
    ck('half_pi_period_rejected',mul(mul(T,z),o.transpose(T))==scale(z,-1) and z!=ZERO)
    # Nonflat positive reduced dynamics and an actual nonzero reducing observation.
    blade=o.blade((1,2,3) if fault=='projector_grade' else (1,2,3,4))
    P=scale(add(I,blade),F(1,2))
    ck('positive_observation_projector',mul(P,P)==P and o.transpose(P)==P)
    ck('positive_observation_spin_rank64',128*P.get(0,F(0))==64)
    ck('positive_observation_V_rank576',9*128*P.get(0,F(0))==576)
    ck('positive_observation_commutes',all(comm(P,v)==ZERO for v in [A,T,*C.values()]))
    N=add(scale(A,F(2,3)),scale(Xj[8],F(-4,5)))
    ck('nonflat_reduced_potential_skew',o.transpose(N)==scale(N,-1))
    ck('nonflat_observation_reduces',comm(P,N)==ZERO)
    for k,om in [(0,N),(7,Xj[7])]:
        # N is a real linear combination of allowed trace-compatible raw coefficients.
        for r in o.UN:
            ck(f'normal_trace_{k}_{r}',add(mul(o.star(om),o.G[r]),mul(o.G[r],om))==ZERO)
    ck('bilinear_dimension41472',81*512==41472)
    ck('symmetric_dimension20592',45*240+36*272==20592)
    ck('antisymmetric_dimension20880',45*272+36*240==20880)
    ck('full_carrier_rank_radical',15*128==1920 and 9*128==1152 and 6*128==768)
    return out

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');parser.add_argument('--controls-only',action='store_true');args=parser.parse_args()
    baseline=run();bad=[n for n,v in baseline if not v]
    if bad:raise AssertionError(('baseline',bad))
    faults={}
    for fault in FAULTS:
        failures=[n for n,v in run(fault) if not v]
        if not failures:raise AssertionError(('undetected',fault))
        faults[fault]=failures
    report=dict(result='K2233',controls=[dict(name=n,passed=v) for n,v in baseline],faults=faults,evidence_kind='exact original-block and Clifford controls; universal classification, transport and domain results are written proofs')
    if not args.controls_only:
        paths=['explorations/conditional-build/k2233-degree-dependent-raw-pairing-2026-10-29.md','tests/channel-swings/k2233_degree_dependent_raw_pairing_probe.py','tests/channel-swings/k2206_changed_raw_mass_construction_probe.py','explorations/conditional-build/k2200-observed-principal-pairing-freedom-2026-10-28.md','explorations/conditional-build/k2206-changed-raw-mass-construction-2026-10-28.md','explorations/conditional-build/k2230-time-dependent-pairing-compatibility-2026-10-29.md']
        report['sha256']={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
        cert=ROOT/'lab/process/k2233-degree-dependent-raw-pairing.json'
        if args.write:cert.write_text(json.dumps(report,indent=2)+'\n')
        elif not cert.exists() or json.loads(cert.read_text())!=report:raise AssertionError('stale or missing K2233 certificate')
    print(json.dumps(dict(result='K2233',controls=len(baseline),faults={k:len(v) for k,v in faults.items()})))
if __name__=='__main__':main()
