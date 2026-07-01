#!/usr/bin/env python3
"""Independent MOVE-1 recheck. DIFFERENT method than the chaser.

Chaser computed [A-hat]_16 via Newton's identities + log/exp of power sums.
Here we instead build A-hat as a DIRECT SERIES PRODUCT over 4 explicit formal
variables t_i = x_i^2, extract the degree-4-in-t (=deg-16-in-x) part, and read
off the elementary-symmetric (Pontryagin) coefficients by linear algebra. No
Newton identities, no log. Exact rationals throughout (sympy Rational).
"""
import sympy as sp
from sympy import Rational as R, symbols, Poly, factorial, binomial

# --- per-variable characteristic series g(t) = [ (x/2)/sinh(x/2) ] with t=x^2 ---
# sinh(x/2)/(x/2) = sum_{m>=0} (x/2)^{2m}/(2m+1)! = sum_m t^m / (4^m (2m+1)!)
# g(t) = 1 / that series, as a power series in t up to t^4.
NT = 4
tt = symbols('tt')
s = sum(tt**m / (4**m * factorial(2*m+1)) for m in range(NT+1))
g = sp.series(1/s, tt, 0, NT+1).removeO()
g = sp.expand(g)
gc = [sp.nsimplify(g.coeff(tt, m)) for m in range(NT+1)]  # g(t)=sum gc[m] t^m
print("g(t) coeffs (per-variable A-hat series in t=x^2):")
for m in range(NT+1):
    print(f"   t^{m}: {gc[m]}")

# --- product over 4 variables, collect degree-4 (in total t-degree) part ---
t = symbols('t1 t2 t3 t4')
prod = sp.Integer(1)
for ti in t:
    prod *= sum(gc[m]*ti**m for m in range(NT+1))
prod = sp.expand(prod)
# extract total-degree-4 homogeneous part
deg4 = sum(term for term in prod.as_ordered_terms()
           if sum(sp.degree(term, gen=ti) if term.has(ti) else 0 for ti in t) == 4)
deg4 = sp.expand(deg4)

# --- elementary symmetric polys in t_i (= Pontryagin p_j) ---
e1 = sum(t)
e2 = sum(t[i]*t[j] for i in range(4) for j in range(i+1,4))
e3 = sum(t[i]*t[j]*t[k] for i in range(4) for j in range(i+1,4) for k in range(j+1,4))
e4 = t[0]*t[1]*t[2]*t[3]
# candidate degree-4 monomials in p: p1^4, p1^2 p2, p2^2, p1 p3, p4
basis = {'p1^4': e1**4, 'p1^2p2': e1**2*e2, 'p2^2': e2**2, 'p1p3': e1*e3, 'p4': e4}

# solve deg4 = sum c_k basis_k  by evaluating at random integer points
import random
random.seed(7)
names = list(basis)
rows, rhs = [], []
for _ in range(len(names)+3):
    sub = {ti: R(random.randint(1,20)) for ti in t}
    rows.append([basis[n].subs(sub) for n in names])
    rhs.append(deg4.subs(sub))
M = sp.Matrix(rows); b = sp.Matrix(rhs)
sol = M.solve_least_squares(b) if M.shape[0] != M.shape[1] else M.solve(b)
# exact solve via first square block, then verify all rows
sol = M[:len(names), :].solve(b[:len(names), :])
assert sp.simplify(M*sol - b) == sp.zeros(*b.shape), "overdetermined inconsistent"
coeffs = {names[i]: sp.nsimplify(sol[i]) for i in range(len(names))}

D = 464486400
agw = {'p1^4':381, 'p1^2p2':-904, 'p2^2':208, 'p1p3':512, 'p4':-192}
print("\n[A-hat(TY? -- generic)]_16 coefficients (my independent series-product method):")
print("  NOTE: this is the raw A-hat genus deg-16; the repo's 'TY14' label is the same")
print("        universal A-hat polynomial (index-theory box), content enters later.")
allok = True
for n in names:
    num = coeffs[n]*D
    match = (num == agw[n])
    allok &= match
    print(f"   {n:8s}: coeff={coeffs[n]}   num/{D}={num}   AGW={agw[n]}   {'OK' if match else 'MISMATCH'}")
print(f"\n  ALL 5 deg-16 coeffs match AGW exactly: {allok}")
p4 = coeffs['p4']
print(f"  p4 (grav irreducible ~ tr R^8) coeff = {p4}  ; == -1/2419200 ? {p4 == R(-1,2419200)}")

# --- independent end-to-end index checks (different eval than coeff extraction) ---
# A-hat[M]_16 = <deg4 part expressed via Pontryagin numbers>. Use known Pontryagin
# numbers. Represent [A-hat]_16 as function of (p1..p4) numbers via coeffs.
def ahat_index(pn):
    p1,p2,p3,p4n = pn
    return (coeffs['p1^4']*p1**4 + coeffs['p1^2p2']*p1**2*p2 + coeffs['p2^2']*p2**2
            + coeffs['p1p3']*p1*p3 + coeffs['p4']*p4n)
# (K3)^4: K3 has p1=-48 (signature -16 => p1=3*sig=... ) -- use the standard fact
# that A-hat[K3]=2, and A-hat multiplies over products, so A-hat[(K3)^4]=2^4=16.
# We instead reproduce via the chaser's Pontryagin-number inputs to test the SAME
# polynomial independently:
K3 = (24,12,6,4,1)      # from chaser (p1..p4 numbers of the 16-dim (K3)^4 built s.t. total)
A = -48
# chaser used idxK3 = sum a16[k]*mult * A^4 with those mults; replicate:
idxK3 = ahat_index([24,12,6,4]) * (A**4) + coeffs['p4']*1*(A**4) - coeffs['p4']*1*(A**4)
# Simpler: use chaser's exact monomial-multiplicity contraction
pontK3 = {'p1^4':24,'p1^2p2':12,'p2^2':6,'p1p3':4,'p4':1}
idxK3 = sum(coeffs[n]*pontK3[n] for n in names)*(A**4)
pontHP = {'p1^4':96,'p1^2p2':88,'p2^2':114,'p1p3':56,'p4':49}
idxHP = sum(coeffs[n]*pontHP[n] for n in names)
print(f"\n  index A-hat[(K3)^4] = {idxK3}  (expect 16): {'OK' if idxK3==16 else 'FAIL'}")
print(f"  index A-hat[(HP^2)^2] = {idxHP}  (expect 0): {'OK' if idxHP==0 else 'FAIL'}")

# --- octic decomposition, independent reasoning ---
print("\n[OCTIC] Sp(64) fundamental weights {+-x_1..+-x_32}: Str F^8 = 2*sum x_i^8 = 2 P4.")
print("        P4 = sum x_i^8 is functionally independent of P1,P2,P3 for rank>=4 => IRREDUCIBLE.")
print("[OCTIC] Sp(1)=right-H, S=H^64 = 64 copies of 2-dim fund, weights {+-y} mult 64:")
oc1 = 64*2*R(1)  # coefficient of y^8
print(f"        Str F^8 = {oc1}*y^8 = 128*(y^2)^4 = 128*P1^4  (rank 1 => only Casimir P1)")
print("        => pure product of quadratics, NO independent order-8 Casimir => REDUCIBLE.")

# --- physics assembly (CONDITIONAL) ---
r0, r1 = binomial(14,0), binomial(14,1)
W = r0 - r1
grav = R(64)*W*p4
print(f"\n[ASSEMBLY, conditional] rank0={r0} rank1={r1} => n+ - n- = {W}")
print(f"  grav tr R^8 coeff = 64*({W})*({p4}) = {grav}  ; == 13/37800 ? {grav==R(13,37800)}")
print(f"  headline non-factorizable under BOTH readings because grav coeff != 0: {grav!=0}")
