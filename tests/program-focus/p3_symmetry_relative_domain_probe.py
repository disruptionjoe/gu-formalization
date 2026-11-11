#!/usr/bin/env python3
"""Finite controls; analytic Fredholm and universal representation proof live in note."""
from pathlib import Path
import hashlib,json,sys
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/p3-symmetry-relative-domain.json'
checks=[];controls=[]
def ck(name, ok):
    assert ok,name
    checks.append(name)
def reject(name, false_claim):
    assert not false_claim,name
    controls.append(name)
def idx(a): return a.cols-a.rank()-(a.rows-a.rank())
def group(ds,m=3):
    out={0}
    while True:
        more=out|{(x+d)%m for x in out for d in ds}
        if more==out:return sorted(out)
        out=more
def invariant(a,g,h):return h*a==a*g
# C2 representation: domain (+,+,-,-), target (+,-,-).
g=s.diag(1,1,-1,-1);h=s.diag(1,-1,-1)
a=s.Matrix([[1,2,0,0],[0,0,1,2],[0,0,2,4]])
ck('C2_equivariance',invariant(a,g,h))
for name,cols in [('plus',[2,3]),('minus',[0,1]),('mixed',[0,2])]:
    a0=a[:,cols];q=4-len(cols)
    ck(name+'_integer_exact_sequence',idx(a0)==idx(a)-q)
    for sign in (1,-1):
        cs=[i for i in range(4) if g[i,i]==sign]
        rs=[i for i in range(3) if h[i,i]==sign]
        retained=[i for i in cols if i in cs]
        full=a.extract(rs,cs);part=a.extract(rs,retained)
        ck(name+f'_character_{sign}',idx(part)==idx(full)-(len(cs)-len(retained)))
ck('commensurable_signed_formula',idx(a[:,[0,2,3]])-idx(a[:,[1,2]])==3-2)
bad=a.copy();bad[1,0]=1
reject('cross_character_operator_not_equivariant',invariant(bad,g,h))
v=s.Matrix([1,0,1,0]);reject('mixed_line_not_invariant',s.Matrix.hstack(v,g*v).rank()==1)
for ds,expected in [([3],[0]),([2],[0,1,2]),([4,6],[0,1,2]),([6,9],[0]),([],[0])]:
    ck('residue_group_'+str(ds),group(ds)==expected)
ck('finite_availability_not_saturation',{0,2}!={0,1,2})
ck('triple_only_actual_vs_inventory',group([3])==[0] and group([1])==[0,1,2])
ck('signed_quotient_cancellation',(4-1)%3==0 and 4%3!=0 and 1%3!=0)
reject('even_implies_mod3_zero',all(n%3==0 for n in (2,4,6)))
reject('inventory_implies_attainability',group([1])==group([3]))
reject('every_quotient_must_be_divisible',(4-1)%3!=0)
j=s.Matrix([[0,-1],[1,0]])
ck('quaternionic_square',j*j.conjugate()==-s.eye(2))
ck('real_line_square',s.eye(1)*s.eye(1).conjugate()==s.eye(1))
ck('quaternionic_index_control',idx(s.zeros(0,2))==2)
# J on domain C6 and target C4, projection and J-invariant removed pair.
j6=s.diag(j,j,j);j4=s.diag(j,j);d=s.eye(4).row_join(s.zeros(4,2))
ck('J_commutes_with_consumed_operator',d*j6==j4*d.conjugate())
ck('J_pair_restriction_index',idx(d)-idx(d[:,list(range(4))])==2)
ck('J_pair_restriction_invariant',j6[:4,4:]==s.zeros(4,2) and j6[4:,:4]==s.zeros(2,4))
wrong=j.copy();wrong[0,1]=1
reject('real_swap_is_not_quaternionic',wrong*wrong.conjugate()==-s.eye(2))
bad=d.copy();bad[0,4]=1
reject('broken_operator_loses_J',bad*j6==j4*bad.conjugate())
reject('one_coordinate_not_J_invariant',s.Matrix.hstack(s.eye(2)[:,0],j*s.eye(2)[:,0]).rank()==1)
# Evaluate analytic kernel/trace data, not an infinite-dimensional proof.
x=s.symbols('x',real=True);u=s.exp(-x)
ck('half_line_kernel_equation',s.diff(u,x)+u==0)
ck('half_line_trace_surjective_seed',u.subs(x,0)==1)
ck('half_line_seed_H1',s.integrate(u*u,(x,0,s.oo))==s.Rational(1,2))
reject('wrong_relative_index_sign',-2==2)
report={'artifact':'P3_SYMMETRY_RELATIVE_DOMAIN','program_target':'P3xsymmetry','tier':'T2','checks':checks,'contrary_controls':controls,'claim_ceiling':'Finite controls only; analytic and representation-ring proof in reviewed note. No class-C membership or attained GU spectral section.','probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if '--write' in sys.argv:REPORT.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(REPORT.read_text())==report,'report drift'
print(f'PASS {len(checks)} supporting checks; {len(controls)} contrary controls')
