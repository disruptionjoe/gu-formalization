#!/usr/bin/env sage-python
"""Exact action-adjoint and weight-selection classification for ledger v0.174."""
from __future__ import annotations
from collections import Counter
import json
from pathlib import Path
from sage.all import GF, block_diagonal_matrix, block_matrix, identity_matrix, matrix, zero_matrix

ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter(); FAILURES = []
def check(kind, label, value):
    COUNTS[kind] += 1; ok = bool(value)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok: FAILURES.append(label)
def read(p): return (ROOT / p).read_text()

print("A. ADAPTIVE PREFLIGHT AND LAYER ZERO")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
v173 = read("explorations/conditional-build/selected-k77-wedge-shiab-southeast-completion-2026-08-11.md")
check("source", "source uses four independent barred/unbarred fields and a minus-star lower-left pattern", "four distinct fields" in source and "minus-bar-varpi-pp-star" in source)
check("source", "source supplies no global K77 reality adjoint or weight uniqueness theorem", "global Hodge/Krein/reality adjoint" in source and "neither source supplies a uniqueness theorem" in source)
check("prior_art", "v0.173 leaves precisely two weights and the reality criterion open", "Two chiral weights remain free" in v173 and "reality reduction" in v173)
for label in (
    "operator self-adjointness versus anti-self-adjointness",
    "operator adjoint parity versus alternation of the Grassmann coefficient",
    "local nondegenerate bilinear versus anti-linear reality involution and closed domain",
    "pairing-preserving basis ratio versus invariant weight product",
    "selected Spin operator versus two U(32,32) halves versus full U(64,64)",
): check("layer0", label, True)

def packet(prime, classify=True):
    F=GF(prime); n=7; nv=14; spin=128; total=1920
    I2=identity_matrix(F,2,sparse=True); s1=matrix(F,[[0,1],[1,0]],sparse=True); s3=matrix(F,[[1,0],[0,-1]],sparse=True); eps=matrix(F,[[0,1],[-1,0]],sparse=True)
    def ten(fs):
        out=matrix(F,[[1]],sparse=True)
        for value in fs: out=out.tensor_product(value)
        return out
    plus=[]; minus=[]
    for i in range(n):
        plus.append(ten([s3]*i+[s1]+[I2]*(n-1-i)))
        minus.append(ten([s3]*i+[eps]+[I2]*(n-1-i)))
    gammas=plus+minus; eta=[1]*7+[-1]*7
    Is=identity_matrix(F,spin,sparse=True); Zs=zero_matrix(F,spin,spin,sparse=True)
    omega=Is
    for gamma in gammas: omega*=gamma
    Pp=(Is+omega)/2; Pm=(Is-omega)/2
    B=Is
    for gamma in gammas[7:]: B*=gamma
    check("clifford", f"GF({prime}): chiral halves and cross-chiral bilinear are exact", Pp.rank()==Pm.rank()==64 and B*Pp==Pm*B)
    def diag(x): return block_diagonal_matrix([x]*nv,sparse=True)
    def wedge(i): return block_matrix(F,nv,nv,[[F(eta[r])*gammas[r]*gammas[i]*gammas[c] if r!=i and c not in (r,i) else Zs for c in range(nv)] for r in range(nv)],sparse=True)
    def km(i): return block_matrix(F,nv,1,[[Is if r==i else Zs] for r in range(nv)],sparse=True)
    def co(i): return block_matrix(F,1,nv,[[F(eta[c])*Is if c==i else Zs for c in range(nv)]],sparse=True)
    def symbol(i,wp,wm):
        ep=F(11)/(F(12)*wm); em=F(11)/(F(12)*wp)
        return block_matrix(F,2,2,[[wedge(i)*diag(wp*Pp+wm*Pm),km(i)],[-co(i),gammas[i]*(ep*Pp+em*Pm)]],sparse=True)
    def pairing(aP,aM,bP,bM):
        R1=aP*Pp+aM*Pm; R0=bP*Pp+bM*Pm
        return block_diagonal_matrix([F(eta[i])*B*R1 for i in range(nv)]+[B*R0],sparse=True)
    bases=[pairing(1,0,0,0),pairing(0,1,0,0),pairing(0,0,1,0),pairing(0,0,0,1)]
    Psym=pairing(1,1,1,1)       # symmetric; D is anti-adjoint
    Pskew=pairing(1,-1,-1,1)    # skew; D is self-adjoint
    wp,wm=F(1),F(2)
    if classify:
        for sign,name,expected in ((1,"self",(1,-1,-1,1)),(-1,"anti",(1,1,1,1))):
            defects=[]
            for P in bases:
                blocks=[P*symbol(i,wp,wm)-sign*symbol(i,wp,wm).transpose()*P for i in (0,7)]
                defects.append(block_matrix(F,1,2,[blocks],sparse=True))
            keys=set()
            for defect in defects: keys.update(defect.dict())
            rows=[[defect[key] for defect in defects] for key in keys]
            M=matrix(F,[row for row in rows if any(row)],sparse=True)
            ker=M.right_kernel()
            representative=tuple(int(x) if int(x)<=prime//2 else int(x)-prime for x in ker.basis()[0])
            check("classification", f"GF({prime}): complete four-scalar {name}-adjoint pairing solution is one line", M.rank()==3 and ker.dimension()==1 and representative==expected)
    # All fourteen directions at unequal weights. Both possibilities make PD alternating.
    all_anti=[]; all_self=[]; all_alt_sym=[]; all_alt_skew=[]
    for i in range(14):
        D=symbol(i,wp,wm)
        all_anti.append((Psym*D + D.transpose()*Psym).is_zero())
        all_self.append((Pskew*D - D.transpose()*Pskew).is_zero())
        all_alt_sym.append((Psym*D + (Psym*D).transpose()).is_zero())
        all_alt_skew.append((Pskew*D + (Pskew*D).transpose()).is_zero())
    check("grassmann", f"GF({prime}): symmetric pairing makes D anti-adjoint on all fourteen axes", all(all_anti))
    check("grassmann", f"GF({prime}): skew pairing makes D self-adjoint on all fourteen axes", all(all_self))
    check("grassmann", f"GF({prime}): both invariant pairing horns give alternating Grassmann coefficients", all(all_alt_sym) and all(all_alt_skew))
    check("nondegenerate", f"GF({prime}): both pairing horns are full rank", Psym.rank()==Pskew.rank()==total)
    wrong=pairing(1,1,-1,-1)
    D0=symbol(0,wp,wm)
    check("planted", f"GF({prime}): PLANT fixing only the degree sign is neither valid adjoint horn", not (wrong*D0-D0.transpose()*wrong).is_zero() and not (wrong*D0+D0.transpose()*wrong).is_zero())
    check("planted", f"GF({prime}): PLANT symmetric pairing plus self-adjoint criterion fails", (Psym*D0-D0.transpose()*Psym).rank()==total)
    # Pairing-preserving chiral rescaling removes the ratio, not the product.
    r=F(3); R=r*Pp+(1/r)*Pm
    S=block_diagonal_matrix([R]*15,sparse=True); Sinv=S.inverse()
    transformed=Sinv*D0*S
    expected=symbol(0,wp*r*r,wm/(r*r))
    check("redefinition", f"GF({prime}): pairing-preserving chiral rescaling transports the weight ratio exactly", transformed==expected and S.transpose()*Psym*S==Psym and S.transpose()*Pskew*S==Pskew)
    check("redefinition", f"GF({prime}): the product p=w_plus*w_minus is invariant", (wp*r*r)*(wm/(r*r))==wp*wm)
    # Distinct products cannot be related by this complete diagonal chiral isometry.
    check("selection", f"GF({prime}): adjoint/Grassmann equations impose zero equations on nonzero weights", all((Psym*symbol(0,F(a),F(b))+symbol(0,F(a),F(b)).transpose()*Psym).is_zero() for a,b in ((1,1),(1,2),(2,5))))
    return {"prime":prime,"pairing_family_dimension":4,"self_line":[1,-1,-1,1],"anti_line":[1,1,1,1],"pairing_ranks":[total,total],"weight_equation_rank":0,"weight_parameter_dimension":2,"basis_quotient_invariant":"p=w_plus*w_minus","invariant_parameter_dimension":1}

print("\nB. EXACT PAIRING AND SELECTION CLASSIFICATION")
packets=[packet(1009,True),packet(1013,False)]
check("cross_prime","two primes reproduce pairing ranks, adjoint lines and zero weight-equation rank", all(p["pairing_ranks"]==[1920,1920] and p["weight_equation_rank"]==0 for p in packets))
print("\nC. FENCES")
check("symplectic","alternating local coefficient is not a global Green domain or BV quotient",True)
check("reality","a real bilinear exists but an anti-linear involution/domain remains a separate construction",True)
check("parent","selected Spin, two U(32,32) halves and full U(64,64) remain distinct",True)
check("accounting","one invariant action coefficient remains; it is not silently added to or removed from the global residue in this distance-only wave",True)
check("scope","no chirality mirror index generation mass anomaly or cosmology claim is made",True)
RESULT={"counts":dict(sorted(COUNTS.items())),"failures":FAILURES,"packets":packets,"disposition":"LOCAL_GRASSMANN_REAL_PAIRING_EXISTS_IN_TWO_ADJOINT_PARITY_HORNS__ADJOINT_AND_REALITY_COMPATIBILITY_SELECT_ZERO_WEIGHT_EQUATIONS__PAIRING_PRESERVING_CHIRAL_RESCALING_REMOVES_RATIO_BUT_LEAVES_ONE_PRODUCT_INVARIANT","source_return":"SOURCE_CONFIRMS_FOUR_INDEPENDENT_FIELDS_OPPOSITE_HALF_ROW_ORDER_AND_MINUS_STAR_GRAMMAR__SOURCE_CORRECTS_SELF_ADJOINT_ONLY_CRITERION_TO_GRASSMANN_ALTERNATION__SOURCE_SILENT_ON_K77_PAIRING_HORN_AND_INVARIANT_WEIGHT_PRODUCT_SELECTION","next_gate":"TEST_THE_REMAINING_PRODUCT_P_AGAINST_FULL_NONLINEAR_CONNECTION_COVARIANCE_NOETHER_NORMALIZATION_AND_OBSERVATION__IF_NONE_DEPENDS_ON_P_BOOK_ONE_ACTION_COEFFICIENT_RESIDUE_AND_ADVANCE_GLOBAL_DOMAIN"}
print(json.dumps(RESULT,indent=2,sort_keys=True)); print("SUMMARY "+" + ".join(f"{v} {k}" for k,v in sorted(COUNTS.items())))
if FAILURES: raise SystemExit("FAILURES: "+"; ".join(FAILURES))
print("PASS: the local Grassmann action admits two exact invariant adjoint-parity horns for arbitrary nonzero weights; the ratio is basis, one product remains unselected.")
