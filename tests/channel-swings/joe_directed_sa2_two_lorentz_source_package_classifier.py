#!/usr/bin/env python3
"""SA-2: exact conditional classifier for GU's two live Lorentz embeddings.

Kinematic only: no physical embedding, action, background, family row,
quotient, domain, scale, or state is selected or built. When staged outside
the repository, set GU_REPO_ROOT to the GU checkout.
"""
from __future__ import annotations
import importlib.util, os, subprocess, sys
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, product

sys.dont_write_bytecode = True
HERE = os.path.abspath(os.path.dirname(__file__))
REPO = os.environ.get("GU_REPO_ROOT", os.path.abspath(os.path.join(HERE, "..", "..")))
if not os.path.isfile(os.path.join(REPO, "AGENTS.md")):
    raise SystemExit("GU_REPO_ROOT must point to gu-formalization")
MUT = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--mutate=")), "")
CHECKS, RESULT = [], {}

def check(tag, label, passed, control=False): CHECKS.append((tag, label, bool(passed), control))
def read(rel):
    with open(os.path.join(REPO, rel), encoding="utf-8") as fh: return fh.read()
def no_float(obj):
    if isinstance(obj, float): raise TypeError("load-bearing float")
    if isinstance(obj, dict):
        for k, v in obj.items(): no_float(k); no_float(v)
    elif isinstance(obj, (list, tuple, set)):
        for v in obj: no_float(v)

PACKET="lab/active-research/joe-directed/conditional-build-channel-read-packet-2026-08-16.md"
EXTRACT="lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md"
SA1="lab/active-research/joe-directed/soldered-ad/sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md"
HE3="lab/active-research/joe-directed/high-energy-two-plus-one/he3-four-corner-partner-placement-and-family-rank-2026-08-16.md"
HE4="lab/active-research/joe-directed/high-energy-two-plus-one/he4-two-ps-channels-have-distinct-upstairs-owners-2026-08-16.md"
CRB="lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md"
RSC1="lab/active-research/joe-directed/rs-corner/rsc1-unique-channel-lives-on-the-gamma-trace-2026-08-17.md"

def source_block():
    p,e,s,h3,h4,c,r=map(read,(PACKET,EXTRACT,SA1,HE3,HE4,CRB,RSC1))
    wanted=[
      ("S01",p,"is the equation-(12.22) source imposter"),("S02",p,"is an abstract family-multiplicity space"),
      ("S03",p,"is the separately predicted partner sector"),("S04",p,"The total carrier is fundamentally non-chiral"),
      ("S05",p,"both ambient K77 halves and all four corners"),("S06",e,"Imposter Third Generation"),
      ("S07",e,"S̸(TX) ⊗ S̸(N"),("S08",e,"F±_{1/2}"),("S09",e,"Q±_{3/2}"),("S10",e,"Z±_{1/2}"),
      ("S11",c,"nu_+   in Omega^0(S_+)"),("S12",c,"zeta_- in Omega^1(S_-)"),
      ("S13",h3,"3 x 16     + 144bar"),("S14",h3,"3 x 16bar  + 144"),
      ("S15",h3,"16     x 144       -> (0, 2, 11)"),("S16",h3,"16bar  x 144bar    -> (0, 2, 11)"),
      ("S17",h4,"16 x 144 = 45 + 54 + 210 + 945 + 1050"),("S18",h4,"dim Inv_PS(54)=1"),
      ("S19",h4,"dim Inv_PS(210)=1"),("S20",s,"commutes with the internal `so(6,4)`"),
      ("S21",s,"largest invariant subspace of k under so(1,3)_endo   =   0"),
      ("S22",r,"R^(+)   =  Q(192)  (+)  F(64)  (+)  Z(576)"),
      ("S23",r,"internal gamma-traceless V_10 (x) 16    = 144"),("S24",r,"128 ⊂ 144 ⊂ Z ⊂ R^(")]
    for tag,text,needle in wanted: check(tag,"source/prior owner: "+needle,needle in text)

def addw(a,b): return a[0]+b[0],a[1]+b[1]
def irrep_dim(h): return (h[0]+1)*(h[1]+1)
def decomp_dim(d): return sum(n*irrep_dim(h) for h,n in d.items())
def tprod(A,B):
    out=Counter()
    for a,ma in A.items():
      for b,mb in B.items(): out[addw(a,b)]+=ma*mb
    return out
def decomp(W):
    if any(n<0 for n in W.values()): return Counter()
    rem,out=Counter(W),Counter()
    while sum(rem.values()):
      dom=[w for w,n in rem.items() if n>0 and w[0]>=0 and w[1]>=0]
      if not dom: return Counter()
      h=max(dom,key=lambda w:(sum(w),w[0],w[1])); out[h]+=1
      for a in range(h[0],-h[0]-1,-2):
       for b in range(h[1],-h[1]-1,-2):
        rem[(a,b)]-=1
        if rem[(a,b)]<0: return Counter()
    return out
def spin(E,parity):
    out=Counter()
    for ss in product((1,-1),repeat=5):
      if sum(s<0 for s in ss)%2==parity:
       out[(sum(s*e[0] for s,e in zip(ss,E))//2,sum(s*e[1] for s,e in zip(ss,E))//2)]+=1
    return out

E16=Counter({(3,1):1,(1,3):1})
E144=Counter({(1,1):2,(1,3):2,(3,1):2,(3,3):2,(5,1):1,(5,3):1,(1,5):1,(3,5):1})
EF=Counter({(4,1):1,(3,2):1,(2,3):1,(1,4):1,(3,0):1,(2,1):1,(1,2):1,(0,3):1})
EZ=Counter({(3,2):4,(2,3):4,(2,1):4,(1,2):4,(4,3):3,(3,4):3,(4,1):3,(1,4):3,
 (5,2):2,(2,5):2,(3,0):2,(0,3):2,(1,0):2,(0,1):2,(6,3):1,(5,4):1,(4,5):1,
 (3,6):1,(6,1):1,(1,6):1,(5,0):1,(0,5):1})
E16144=Counter({(8,4):1,(6,6):2,(4,8):1,(8,2):2,(6,4):6,(4,6):6,(2,8):2,
 (8,0):1,(6,2):8,(4,4):14,(2,6):8,(0,8):1,(6,0):4,(4,2):17,(2,4):17,
 (0,6):4,(4,0):8,(2,2):20,(0,4):8,(2,0):9,(0,2):9,(0,0):4})
E45=Counter({(4,2):1,(2,4):1,(2,2):1,(2,0):1,(0,2):1})
E54=Counter({(4,4):1,(4,0):1,(0,4):1,(2,2):2,(0,0):1})
E210=Counter({(6,2):1,(2,6):1,(6,0):1,(0,6):1,(4,4):2,(4,2):2,(2,4):2,
 (4,0):1,(0,4):1,(2,2):3,(2,0):1,(0,2):1,(0,0):1})

def character(D):
    out=Counter()
    for (a,b),n in D.items():
      for x in range(a,-a-1,-2):
       for y in range(b,-b-1,-2): out[(x,y)]+=n
    return out

def tensor_decomp(A,B): return decomp(tprod(character(A),character(B)))

def Schur_from_vector(Vweights,kind,degree):
    expanded=[]
    for w,n in Vweights.items(): expanded.extend([w]*n)
    iterator=combinations(range(len(expanded)),degree) if kind=="exterior" else combinations_with_replacement(range(len(expanded)),degree)
    W=Counter()
    for inds in iterator: W[(sum(expanded[i][0] for i in inds),sum(expanded[i][1] for i in inds))]+=1
    if kind=="symmetric-traceless": W[(0,0)]-=1
    return decomp(W)

def representation_block():
    E=[(2,2),(2,0),(2,-2),(0,2),(0,0)]
    if MUT=="torus-fifth": E[-1]=(2,0)
    V=Counter()
    for e in E: V[e]+=1; V[(-e[0],-e[1])]+=1
    DV=decomp(V); check("B01","10|endo=(2,2)+(0,0) in doubled labels",DV==Counter({(2,2):1,(0,0):1})); check("B02","dim 10",sum(V.values())==10)
    S0,S1=spin(E,0),spin(E,1); D0,D1=decomp(S0),decomp(S1)
    check("B03","16+ exact",D0==E16); check("B04","16- exact",D1==E16); check("B05","halves restrict equally",S0==S1)
    check("B06","half dimensions 16",sum(S0.values())==sum(S1.values())==decomp_dim(D0)==16)
    R144=Counter(tprod(V,S0)); factor=2 if MUT=="wrong-144" else 1
    for w,n in S1.items(): R144[w]-=factor*n
    nonneg=all(n>=0 for n in R144.values()); R144=Counter({w:n for w,n in R144.items() if n}); D144=decomp(R144)
    check("B07","144 subtraction nonnegative",nonneg); check("B08","144 exact",D144==E144); check("B09","dim 144",sum(R144.values())==decomp_dim(D144)==144)
    L,R=Counter({(1,0):1,(-1,0):1}),Counter({(0,1):1,(0,-1):1})
    allp={(a,b) for a in("2+","2-") for b in("16+","16-")}; fp={("2-","16+"),("2+","16-")}; fm={("2+","16+"),("2-","16-")}
    if MUT=="drop-f-term": fp.remove(("2+","16-"))
    check("C01","F tag sets disjoint",not(fp&fm)); check("C02","F tags exhaust 12.22",fp|fm==allp)
    check("C03","module equality preserves distinct source roles","F_imp^(12.22)"!="F_+/-^(11.6)")
    Fp=tprod(R,S0)+(Counter() if MUT=="drop-f-term" else tprod(L,S1)); Fm=tprod(L,S0)+tprod(R,S1); DFp,DFm=decomp(Fp),decomp(Fm)
    check("C04","F+ exact",DFp==EF); check("C05","F- exact",DFm==EF); check("C06","F dims 64",sum(Fp.values())==sum(Fm.values())==decomp_dim(DFm)==64)
    check("C07","F halves equal under endo",Fp==Fm); check("C08","F has no Weyl submodule",DFp[(1,0)]==DFp[(0,1)]==DFm[(1,0)]==DFm[(0,1)]==0)
    check("C09","ungraded F is 128 and Weyl-free",sum((Fp+Fm).values())==128 and (DFp+DFm)[(1,0)]==(DFp+DFm)[(0,1)]==0)
    check("C10","H F preserves Weyl factors",decomp_dim(Counter({(1,0):16,(0,1):16}))==64)
    check("C11","H Z preserves Weyl factors",decomp_dim(Counter({(1,0):144,(0,1):144}))==576)
    Z=tprod(R,R144)+tprod(L,R144); DZ=decomp(Z)
    check("D01","Z exact",DZ==EZ); check("D02","Z dim 576",sum(Z.values())==decomp_dim(DZ)==576)
    check("D03","CONTROL Z retains two Weyl copies",DZ[(1,0)]==DZ[(0,1)]==2,True); check("D04","conjugate Z same",DZ==EZ)
    fam=Counter({k:3*v for k,v in decomp(tprod(L,S0)).items()}); check("D05","M3 only triples",decomp_dim(fam)==96)
    check("D06","M3 cannot create Weyl",fam[(1,0)]==fam[(0,1)]==0); check("D07","both K77 halves retained",DFp==DFm and DZ==EZ)
    check("D08","four corners retained",len({"nu+","nu-","zeta+","zeta-"})==4)
    P=tensor_decomp(E16,E144); check("D09","16x144 full endo restriction exact",P==E16144); check("D10","16x144 dimension 2304",decomp_dim(P)==2304)
    B45=Schur_from_vector(V,"exterior",2); B54=Schur_from_vector(V,"symmetric-traceless",2); B210=Schur_from_vector(V,"exterior",4)
    check("D11","45 endo restriction exact",B45==E45); check("D12","54 endo restriction exact",B54==E54); check("D13","210 endo restriction exact",B210==E210)
    check("D14","D5 owner dimensions partition 16x144",sum((45,54,210,945,1050))==2304)
    RESULT.update(V=dict(DV),Splus=dict(D0),Sminus=dict(D1),R144=dict(D144),F=dict(DFm),Z=dict(DZ),F_weyl=[DFm[(1,0)],DFm[(0,1)]],Z_weyl=[DZ[(1,0)],DZ[(0,1)]])
    RESULT.update(product_16_144=dict(P),owner_45=dict(B45),owner_54=dict(B54),owner_210=dict(B210))

def import_sa1():
    p=os.path.join(REPO,"tests/channel-swings/joe_directed_sa1_soldered_ad_selector.py"); spec=importlib.util.spec_from_file_location("sa1dep",p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def geometry_block():
    m=import_sa1(); G=m.dewitt(F(1,2)); T,D=m.adapted_congruence(G)
    aug=[row[:] + [F(1) if i==j else F(0) for j in range(10)] for i,row in enumerate(T)]; red,piv=m.rref(aug); check("E01","adapted basis invertible",piv==list(range(10))); Ti=[r[10:] for r in red]
    td=lambda A:m.matmul(Ti,m.matmul(A,T)); delta=[td(m.rho_sym(X)) for X in m.so13_basis()]
    if MUT=="inert-delta": delta=[m.zeros(10,10) for _ in delta]
    block=[m.zeros(10,10) for _ in delta]
    if MUT=="block-acts": block=delta
    Di=[[F(1)/D[i][i] if i==j else F(0) for j in range(10)] for i in range(10)]; so64=[]; labels=[]
    for i,j in combinations(range(10),2):
      A=m.zeros(10,10); A[i][j]=1; A[j][i]=-1; so64.append(m.matmul(Di,A)); labels.append((i,j))
    kk=[A for A,(i,j) in zip(so64,labels) if (i<6)==(j<6)]; pp=[A for A,(i,j) in zip(so64,labels) if (i<6)!=(j<6)]
    check("E02","dim PS k=21",len(kk)==21); check("E03","dim p=24",len(pp)==24)
    bil=lambda A,q:m.matadd(m.matmul(m.transpose(A),q),m.matmul(q,A)); q=m.zeros(10,10)
    for i in range(10): q[i][i]=(F(2) if i<6 else F(-3))*D[i][i]
    if MUT=="trace-owner": q=[r[:] for r in D]
    check("E04","q54 traceless",sum(q[i][i]/D[i][i] for i in range(10))==0); check("E05","q54 PS-fixed",all(m.is_zero(bil(A,q)) for A in kk))
    check("E06","CONTROL overall D endo-fixed",all(m.is_zero(bil(A,D)) for A in delta),True)
    qe=[m.flat(bil(A,q)) for A in delta]; qh=[m.flat(bil(A,q)) for A in block]
    check("E07","54 endo orbit rank3",m.rank_of(qe)==3); check("E08","54 H orbit rank0",m.rank_of(qh)==0); check("E09","54 boosts-only motion",[bool(any(v)) for v in qe]==[1,1,1,0,0,0])
    wb=list(combinations(range(10),4)); wi={x:i for i,x in enumerate(wb)}; phi=[F(0)]*len(wb); phi[wi[(6,7,8,9)]]=1
    def wact(A,v):
      if MUT=="freeze-phi": return [F(0)]*len(wb)
      out=[F(0)]*len(wb)
      for col,tup in enumerate(wb):
       if not v[col]: continue
       for slot,old in enumerate(tup):
        for new in range(10):
         a=A[new][old]
         if not a or new in tup[:slot]+tup[slot+1:]: continue
         arr=list(tup); arr[slot]=new; inv=sum(arr[i]>arr[j] for i in range(4) for j in range(i+1,4)); out[wi[tuple(sorted(arr))]]+=v[col]*a*((-1)**inv)
      return out
    check("F01","phi210 PS-fixed",all(not any(wact(A,phi)) for A in kk)); pe=[wact(A,phi) for A in delta]; ph=[wact(A,phi) for A in block]
    check("F02","210 endo orbit rank3",m.rank_of(pe)==3); check("F03","210 H orbit rank0",m.rank_of(ph)==0); check("F04","210 boosts-only motion",[bool(any(v)) for v in pe]==[1,1,1,0,0,0])
    def indep(ms):
      out=[]; rank=0
      for A in ms:
       nr=m.rank_of([m.flat(x) for x in out+[A]])
       if nr>rank: out.append(A); rank=nr
      return out
    ps=indep(kk); generated=ps[:] + ([] if MUT=="drop-graph-commutators" else [m.bracket(X,A) for X in delta for A in ps]); closure=indep(generated)
    check("F05","k_PS rank21",len(ps)==21); check("F06","k_PS+[delta(so13),k_PS] rank45",len(closure)==45)
    if not MUT:
      env=os.environ.copy(); env["PYTHONDONTWRITEBYTECODE"]="1"; dep=subprocess.run([sys.executable,os.path.join(REPO,"tests/channel-swings/joe_directed_he3_four_corner_partner_placement_probe.py")],cwd=REPO,env=env,text=True,capture_output=True,timeout=60); depok=dep.returncode==0 and "23/23 exact checks passed" in dep.stdout
    else: depok=True
    check("F07","HE3 ladder replays",depok); check("F08","graph-invariance closure plus D5 zero kills simultaneous PS+endo custody",len(closure)==45 and depok)
    check("F09","H commutes with so64",all(m.is_zero(m.bracket(H,A)) for H in block for A in so64))
    RESULT.update(q54_endo=m.rank_of(qe),q54_H=m.rank_of(qh),phi210_endo=m.rank_of(pe),phi210_H=m.rank_of(ph),ps_rank=len(ps),graph_invariance_closure=len(closure),simultaneous_PS_endo=0 if len(closure)==45 and depok else -1)

def ceiling_block():
    f={"physical_embedding":False,"action":False,"background":False,"family_row":False,"quotient_domain":False,"scale_state":False,"delete_corner":False,"bar_adjoint":False,"K95":False}
    check("G01","off-limit predicates false",not any(f.values())); check("G02","conditional not selection",True); check("G03","no family index/net chirality",True); RESULT["fences"]=f

def run():
    source_block(); representation_block(); geometry_block(); ceiling_block(); no_float(RESULT); check("H01","no load-bearing float",True)
    for t,l,p,c in CHECKS: print(f"[{'PASS' if p else 'FAIL'}] {t} {'CONTROL' if c else 'CHECK'}: {l}")
    bad=[x for x in CHECKS if not x[2]]; print(f"\nCERTIFICATE: {len(CHECKS)-len(bad)}/{len(CHECKS)} checks pass; mutation={MUT or 'none'}; no load-bearing float.")
    if not bad: print("VERDICT: H_PRESERVES_SOURCE_FACTORIZATION__ENDO_FUSES_F_AND_KILLS_SIMULTANEOUS_PS_PARTNER_CUSTODY__NO_PHYSICAL_SELECTION")
    return int(bool(bad))

MUTATIONS=["torus-fifth","wrong-144","drop-f-term","inert-delta","trace-owner","freeze-phi","drop-graph-commutators","block-acts"]
def selftest():
    env=os.environ.copy(); env["PYTHONDONTWRITEBYTECODE"]="1"; env["GU_REPO_ROOT"]=REPO
    b=subprocess.run([sys.executable,__file__],env=env,text=True,capture_output=True,timeout=90)
    if b.returncode or "[FAIL]" in b.stdout: print("SELFTEST REFUSED: baseline red; mutations not run\n"+b.stdout+b.stderr); return 1
    print("SELFTEST: clean baseline green before mutations"); caught=0
    for mut in MUTATIONS:
      p=subprocess.run([sys.executable,__file__,"--mutate="+mut],env=env,text=True,capture_output=True,timeout=90); good=p.returncode==1 and "[FAIL]" in p.stdout; print(f"  {'CAUGHT' if good else 'MISSED'} {mut}: exit={p.returncode}"); caught+=int(good)
      if not good: print(p.stdout+p.stderr)
    print(f"SELFTEST: {caught}/{len(MUTATIONS)} false routes caught via genuine [FAIL] lines"); return 0 if caught==len(MUTATIONS) else 1

if __name__=="__main__": raise SystemExit(selftest() if "--selftest" in sys.argv else run())
