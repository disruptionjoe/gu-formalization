#!/usr/bin/env python3
"""Exact load-bearing Clifford controls; universal exclusion is proved in the note."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,json,hashlib,itertools
import sympy as S
import k2185_clifford_spectral_obstruction_probe as p
k=p.k;ROOT=Path(__file__).resolve().parents[2]
def ix(*a):return k.blade([k.N[i-1] for i in a])
def nonscalar(x):return k.add(x,k.scale(k.I,-k.scalar(x)))
def controls(fault=None):
 cs={};ck=lambda n,v:cs.__setitem__(n,bool(v));I=k.I
 # Clifford and exterior products are distinct computations.
 J=k.mm(k.OM,k.blade(k.N));ck('combined_volume_square',k.mm(J,J)==I)
 for label,E,expect in [('positive',[1,2,3,4],1),('indefinite',[1,2,3,5],-1)]:
  e=[ix(i) for i in E];B=k.add(k.mm(e[0],e[1]),k.mm(e[2],e[3]));D=k.scale(k.mm(k.mm(e[0],e[1]),k.mm(e[2],e[3])),2)
  b2=k.mm(B,B);ck(label+'_bivector_defect',nonscalar(b2)==k.scale(D,2 if fault=='wedge_factor' else 1))
  ck(label+'_gram_sign',k.mm(D,D)==k.scale(I,4*(1 if fault=='gram_sign' else expect)))
  K=[n for n in range(1,11) if n not in E];H=k.add(ix(*K[:2]),k.scale(ix(*K[2:4]),2));C=k.mm(D,H)
  ck(label+'_orthogonal_commutation',not k.comm(D,H))
  ck(label+'_factor_square',k.mm(C,C)==k.scale(k.mm(k.mm(D,D),k.mm(H,H)),-1 if fault=='factor_sign' else 1))
  ck(label+'_complement_support',all(not (m&sum(1<<k.N[i-1] for i in E)) for m in k.mm(C,C)))
  ck(label+'_nonscalar_complement_positive_control',bool(nonscalar(k.mm(C,C))))
  ck(label+'_PBW_intersection',set(nonscalar(k.mm(C,C))).isdisjoint(set(D)))
  ck(label+'_dual_B_square',k.mm(k.mm(J,B),k.mm(J,B))==k.scale(b2,-1 if fault=='dual_sign' else 1))
  ck(label+'_dual_C_square',k.mm(k.mm(J,C),k.mm(J,C))==k.mm(C,C))
  # D anticommutes on E-odd but commutes on E-even K-odd trivectors.
  a=ix(*E[:3]);b=k.mm(ix(*E[:2]),ix(K[0]));ck(label+'_E3_anticommutator',not k.add(k.mm(D,a),k.mm(a,D)))
  ck(label+'_E2K_commutator',not k.comm(D,b))
 # Null support is a real control, not an assumption of invertibility.
 ell=k.add(ix(1),ix(5));B=k.add(k.mm(ell,ix(2)),ix(3,4));D=k.scale(k.mm(k.mm(ell,ix(2)),ix(3,4)),2)
 ck('null_support_nonzero_top',bool(D));ck('null_support_square_zero',not k.mm(D,D));ck('null_support_defect',nonscalar(k.mm(B,B))==D)
 ck('null_support_scalar_part',k.scalar(k.mm(B,B))==-1)
 r=S.symbols('r');c0=49-301*r+108*r*r;c1=(638 if fault=='nilpotent_polynomial' else 637)-133*r-72*r*r
 resultant=S.resultant(c0,c1,r);ck('nilpotent_resultant',resultant==S.Integer(-1443826944))
 # Vertical scalar V is a separate asymmetric branch, not a renaming.
 a,c,Y,V,T,kk=S.symbols('a c Y V T kk');Q=35*V**2-157*V*T-54*T**2+(14*a-42*c)*V+(-102*a+162*c)*T
 vertical=S.expand(Q.subs({V:a,T:c+Y}));C0=49*a*a-301*a*c+108*c*c;dd=-259*a+54*c
 ck('vertical_operator_quadratic',S.expand(vertical-(-54*Y*Y+dd*Y+C0))==0)
 ev=2303-2807*r+648*r*r;dv=-259+54*r;cv=49-301*r+108*r*r
 ck('vertical_trace_elimination',S.expand(8*cv+3*(637-133*r-72*r*r)-ev)==0)
 ck('vertical_repeated_root_resultant',S.resultant(ev,dv,r)==10925334)
 vp=-54*(1024-4*kk)*cv+kk*dv*dv
 target=7001316*(21990393*kk*kk+20902856704*kk-5674993975296)
 ck('vertical_resultant_polynomial',S.expand(S.resultant(ev,vp,r)-target)==0)
 ck('vertical_discriminant_nonsquare',S.discriminant(ev,r)==1909873 and 1381**2<1909873<1382**2)
 remainder=((41391*kk-18450432)*r-31213*kk+37029888)/2
 ck('vertical_irrational_remainder',S.expand(S.rem(vp,ev,r)-remainder)==0)
 ck('vertical_remainder_coefficient_bound',41391*256-18450432==-7854336<0)
 for m in range(1,32):
  rm=vp.subs(kk,m*(32-m));aa,bb,gg=S.gcdex(S.Poly(ev,r),S.Poly(rm,r))
  ck('vertical_Bezout_'+str(m),gg==1 and aa*S.Poly(ev,r)+bb*S.Poly(rm,r)==1)
 # v²=0,t⁴=0 implies (7v-15t)^5=0 in the commutative quotient.
 vv,tt=S.symbols('v t');rem=S.reduced((7*vv-15*tt)**5,[vv**2,tt**4],vv,tt)[1]
 ck('vertical_zero_scalars_nilpotent_pencil',rem==0)
 # Direct rank of wedge-plus-contraction maps. Selfdual exception matters.
 dims={}
 for label,B in [('special',k.add(ix(1,2),ix(3,4))),('generic',k.add(ix(1,2),k.scale(ix(3,4),2)))]:
  columns=[]
  for inds in itertools.combinations([1,2,3,4],2):
   a=ix(*inds);z=k.add(k.mm(B,a),k.mm(a,B));columns.append([z.get(0,0),z.get(next(iter(ix(1,2,3,4))),0)])
  dims[label]=6-S.Matrix(2,6,lambda i,j:columns[j][i]).rank()
 ck('special_coefficient_kernel',dims['special']==5);ck('generic_coefficient_kernel',dims['generic']==4)
 # Genuine nonaffine central structural ports, not purported solutions.
 aa=ix(1,3);bb=k.add(ix(2,3),ix(1,4));w=k.add(k.mm(aa,ix(5)),k.mm(bb,ix(6)));u=k.add(k.mm(bb,ix(5)),k.scale(k.mm(aa,ix(6)),2))
 v=k.mm(k.blade(k.N),w);t=k.mm(k.OM,u);B0=k.neg(k.add(ix(1,2),ix(3,4)));D0=ix(1,2,3,4)
 wu=k.mm(w,u);V=k.mm(v,v);T=k.mm(t,t)
 ck('nonaffine_anticommutator',not k.add(wu,k.mm(u,w)));ck('nonaffine_B_owned',k.grade(wu,2)==B0)
 ck('nonaffine_C_owned',k.grade(wu,6)==k.scale(k.mm(D0,ix(5,6)),-2))
 ck('nonaffine_B_centrality',not k.add(k.mm(B0,w),k.mm(w,B0)) and not k.add(k.mm(B0,u),k.mm(u,B0)))
 ck('nonaffine_U_centrality',not k.comm(k.K(k.mm(v,t)),v) and not k.comm(k.K(k.mm(v,t)),t))
 ck('nonaffine_V_formula',V==k.add(k.scale(I,3),k.scale(D0,-2),k.scale(k.mm(B0,ix(5,6)),2)))
 ck('nonaffine_T_formula',T==k.add(k.scale(I,-6),k.scale(D0,2),k.scale(k.mm(B0,ix(5,6)),4)))
 basis=set(V)|set(T)|{0};mat=S.Matrix([[I.get(m,0),V.get(m,0),T.get(m,0)] for m in sorted(basis)])
 ck('nonaffine_rank3',mat.rank()==3)
 rr,pp,fl,*_=k.filt(v,u);pi=k.inv(pp);ck('nonaffine_pencil_inverse',k.mm(pp,pi)==I)
 adapters={j:k.scale(k.mm(pi,k.port(rr)[j]),-k.ETA[j]) for j in k.N}
 qs={j:k.RR(adapters,*k.C(k.port(k.add(v,t)),*k.kernel(adapters,j)))[1] for j in k.N}
 contraction=k.add(*(k.mm(qs[j],k.G[j]) for j in k.N));ck('nonaffine_original_transfer',k.scale(k.mm(k.bar(pp),contraction),6)==fl)
 ck('nonaffine_original_rejected',bool(fl) and any(qs.values()))
 return cs,dict(nilpotent_resultant=str(resultant),coefficient_kernel_dimensions=dims,nonaffine_original_nonzero_rows=sum(bool(q) for q in qs.values()))
FAULTS=['wedge_factor','gram_sign','factor_sign','dual_sign','nilpotent_polynomial']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();cs,details=controls();assert all(cs.values()),[n for n,v in cs.items() if not v]
 faults={}
 for f in FAULTS:
  bad=[n for n,v in controls(f)[0].items() if not v];assert bad,('undetected',f);faults[f]=bad
 deps=['explorations/conditional-build/k2187-affine-clifford-exclusion-2026-10-28.md','explorations/conditional-build/k2185-clifford-spectral-obstruction-2026-10-28.md','explorations/conditional-build/k2183-commuting-trace-descent-2026-10-28.md','tests/channel-swings/k2185_clifford_spectral_obstruction_probe.py']
 report=dict(result_id='K2187',status='conditional_exact_controls',checks=cs,fault_failures=faults,details=details,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written affine quadratic, degenerate blade and orthogonal PBW argument; finite exact Clifford identities and genuine nonaffine original-row countercontrol supplement internal independent review, not proof-assistant or physical certification.')
 dst=ROOT/'lab/process/k2187-affine-clifford-exclusion.json'
 if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dst.read_text())==report
 print(json.dumps(dict(result='K2187',checks=len(cs),faults=len(faults),details=details)))
if __name__=='__main__':main()
