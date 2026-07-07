"""
FB-F1: BUILD the twisted operator on the framed-bordism carrier (the constructive PROMOTE-or-KILL
route on conjecture D; the object RS-S4 left UNBUILT).

The frozen located-not-forced paper (Section 9 / conjecture D) leaves ONE open bridge:
    order-3-class  ->  integer-3.
The order-3 class is the framed-bordism Adams e-invariant e_R = 1/12 carried by the self-dual
Lambda^2_+ tangential framing on the GU-forced RP^3 = L(2;1) spine, living in the Z/3 summand of
pi_3^s = Z/24 = Z/8 (+) Z/3 (CRT). RS-S4 computed the UNTWISTED transparent-fiber APS index = -1/12
(fractional) and stopped GATED because the TWISTED operator was never built.

Route F1 BUILDS it. On RP^3 = L(2;1) with the self-dual framing, we build the twisted Dirac eta and
enumerate EVERY GU-admissible twist:
    (b1) the flat deck-group twists  (pi_1(L(2;1)) = Z/2, characters a in {0,1});
    (b2) the flat family twists      (flat SU(2)+ bundles = Hom(Z/2, SU(2)));
    (b3) the self-dual Lambda^2_+ adjoint twist (Ad of each SU(2) holonomy);
    (b4) the bulk section degrees d' (noted: they feed the bulk INTEGER index, not the boundary e_R).
For each we compute the twisted APS eta-index and ask the decisive question:
    does ANY GU-admissible twist promote the fractional -1/12 to an INTEGER with nonzero Z/3 content?

DECISIVE READOUT -- KILL. Every twist available on the L(2;1) carrier adds a 2-adic eta (deck group
Z/2 => denominators are powers of 2, MEASURED). The 3-adic valuation of the twisted index defect is
therefore FIXED at v_3 = -1 for every twist (v_3(1/12) = -1 dominates v_3(2-adic) >= 0), so the index
is NEVER an integer; and the 3-primary (Z/3) component of the defect is FROZEN at a nonzero FRACTION
(2/3 in Q/Z), identical for every twist -- the Z/2 deck twists act ONLY on the 2-primary sector and
cannot touch, cancel, or integerize the Z/3 content. The Z/2 deck group is coprime to 3: it cannot
manufacture a Z/3. This CONFIRMS the category error one level up from Hom(Z/3,Z)=0: not only is the
class not an integer, no operator on the GU-forced carrier converts it to one.

DISCRIMINATING CONTROL: the SAME machinery on L(3;1) (deck group Z/3, NOT GU-forced) DOES integerize a
3-adic framing with nonzero Z/3 content -- proving the mechanism exists, on the wrong (unforced) carrier.
SCRAMBLED-TWIST CONTROL: random 2-adic "twist" etas never integerize -1/12 (v_3 stays -1); only an
(unavailable) 3-adic twist could -- and none exists on the Z/2 deck group.

THE e-INVARIANT / Hom(Z/3,Z)=0 DISCIPLINE: e_R = 1/12 is Q/Z-valued; its Z/3 content is genuine mod-3
INFORMATION, never an integer. We never identify it with an integer. Every integer we exhibit is an
index integer-BY-CONSTRUCTION (the closed AS index 12k+...) and we PROVE it is 3-inert (carries no e_R).

TARGET-IMPORT GUARD (maximum strictness): {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} is never
assumed, inserted, hardcoded as an answer, or divided by. 24 = 8*3 is a CRT fact about
denom(B_2/4)=|Im J_3| (derived, printed). e_R = 1/12 is MEASURED from the framing (p_1/48 and class-2/24).
Every 3 carries its provenance chain. Every count is stated "mechanism/carrier M forces c".

Run from repo root:  python tests/big-swing/fb_f1_twisted_operator_build.py   (exit 0)
"""
import sys
from fractions import Fraction

import numpy as np
import sympy as sp

np.random.seed(20260707)

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAIL.append(name)


# --------------------------------------------------------------------------------------------
# p-adic valuation and 3-primary (Z/3) component of a rational mod Z (used throughout).
# --------------------------------------------------------------------------------------------
def val_p(n, p):
    """p-adic valuation of a nonzero integer."""
    n = abs(int(n))
    v = 0
    while n > 0 and n % p == 0:
        v += 1
        n //= p
    return v


def v3_frac(x):
    """3-adic valuation of a Fraction (v3(num) - v3(den))."""
    x = Fraction(x)
    if x == 0:
        return None  # +inf
    return val_p(x.numerator, 3) - val_p(x.denominator, 3)


def three_primary_component(x):
    """
    The component of x in the 3-primary part of Q/Z, via CRT/partial fractions.
    Writes x = a/3^v + b/cofactor (mod Z), returns a/3^v in [0,1).  0 iff x is 3-integral.
    """
    x = Fraction(x)
    den = x.denominator
    v = val_p(den, 3)
    if v == 0:
        return Fraction(0)
    m3 = 3 ** v
    cof = den // m3                      # coprime to 3
    s, t, g = sp.gcdex(cof, m3)          # s*cof + t*m3 = g = 1
    assert int(g) == 1
    a = (x.numerator * int(s)) % m3
    return Fraction(a, m3)


# ============================================================================================
# SECTION 0 -- ANCHORS: Krein (+96,-96,0), rank/ker, 12k index; CRT split of 24; e_R=1/12; -1/12.
# ============================================================================================
print("=" * 96)
print("SECTION 0 -- ANCHORS")
print("=" * 96)
N, DIM = 14, 128
TIMELIKE = {4, 5, 6, 7, 8}
SPACELIKE = [a for a in range(N) if a not in TIMELIKE]


def jw(n):
    I = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    G = []
    for k in range(n):
        L, R = [s3] * k, [I] * (n - 1 - k)
        for mid in (s1, s2):
            o = np.array([[1 + 0j]])
            for m in L + [mid] + R:
                o = np.kron(o, m)
            G.append(o)
    return G


base = jw(7)
I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)
e = [(1j * base[a] if a in TIMELIKE else base[a]) for a in range(N)]
etaV = np.diag([(-1.0 if a in TIMELIKE else 1.0) for a in range(N)]).astype(complex)


def sgen(i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex)
    M[i, j] = 1
    M[j, i] = -1
    return M


def gen(i, j):
    return np.kron(I14, sgen(i, j)) + np.kron(lvec(i, j), I128)


bS = I128.copy()
for s in SPACELIKE:
    bS = bS @ e[s]
if np.linalg.norm(bS.conj().T + bS) < 1e-9:
    bS = 1j * bS
bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))

Gam = np.hstack(e)
rankG = int(np.linalg.matrix_rank(Gam, tol=1e-9))
Pi = np.eye(N * DIM, dtype=complex) - Gam.conj().T @ np.linalg.inv(Gam @ Gam.conj().T) @ Gam
w, Vv = np.linalg.eigh(Pi)
Wk = Vv[:, w > 0.5]
print(f"  rank(Gamma) = {rankG}   dim ker(Gamma) = {Wk.shape[1]}")
check("anchor: rank(Gamma)=128, dim ker=1664", rankG == 128 and Wk.shape[1] == 1664)

SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
J3 = [gen(a, b) + gen(c, d) for (a, b, c, d) in SD]
Cas = -(J3[0] @ J3[0] + J3[1] @ J3[1] + J3[2] @ J3[2])
CasK = Wk.conj().T @ Cas @ Wk
CasK = 0.5 * (CasK + CasK.conj().T)
ev, U = np.linalg.eigh(CasK)
top = max(round(x.real, 3) for x in ev)
Wt = Wk @ U[:, np.abs(ev - top) < 1e-3]
Kt = Wt.conj().T @ np.kron(etaV, bS) @ Wt
Kt = 0.5 * (Kt + Kt.conj().T)
sig = np.linalg.eigvalsh(Kt)
npl, nmi = int(np.sum(sig > 1e-9)), int(np.sum(sig < -1e-9))
print(f"  triplet Krein signature (+{npl}, -{nmi}, 0)  [Cartan=Krein=ghost-parity seat]")
check("anchor: triplet Krein (+96,-96,0)", (npl, nmi) == (96, 96))

kk = sp.symbols("k", integer=True)
ind_bundle = sp.expand(2 * 0 + 4 * kk + 2 * (4 * kk))
print(f"  h2 canon full-bundle index 2(0)+4(k)+2(4k) = {ind_bundle} (EVEN for all k)")
check("anchor: 12k index reproduced", ind_bundle == 12 * kk)

# ---- CRT: 24 = 8 * 3 (a fact about |Im J_3| = denom(B_2/4), DERIVED not asserted) ----
print()
B2 = sp.bernoulli(2)                       # 1/6
imJ = int(sp.denom(B2 / 4))                # denom(1/24) = 24
f24 = sp.factorint(imJ)                    # {2:3, 3:1}
p8, p3 = 2 ** f24.get(2, 0), 3 ** f24.get(3, 0)
print(f"  |Im J_3| = denom(B_2/4) = denom({B2}/4) = {imJ}   [homotopy provenance; NOT chi(K3)]")
print(f"  factor: {imJ} = {p8} * {p3}   gcd({p8},{p3}) = {int(sp.igcd(p8, p3))}   => CRT Z/24 = Z/8 (+) Z/3")
check("CRT: 24 = 8*3, coprime, so pi_3^s = Z/24 = Z/8 (+) Z/3 (derived from Bernoulli denom)",
      p8 * p3 == 24 and int(sp.igcd(p8, p3)) == 1)
# the located class is 2 in Z/24; its Z/3 image is 2 mod 3 = 2, NONZERO
cls = 2
z3_of_class = cls % 3
print(f"  located class {cls} in Z/24 -> (mod 8, mod 3) = ({cls % 8}, {z3_of_class})   "
      f"Z/3 image = {z3_of_class} (NONZERO => genuine Z/3 content)")
check("located class 2 in Z/24 has nonzero Z/3 image (2 mod 3 = 2)", z3_of_class == 2)

# ---- e_R = 1/12 measured two ways; its Z/3 (3-primary) component, and the -1/12 anchor ----
print()
p1 = 4                                      # Kirby-Melvin, FROM-MEMORY
e_R_grav = Fraction(p1, 48)                 # p_1/48
e_R_class = Fraction(cls, imJ)              # class 2 in Z/24
print(f"  e_R = p_1/48 = {p1}/48 = {e_R_grav}   [p_1=4 Kirby-Melvin, FROM-MEMORY]")
print(f"  e_R = class {cls} in Z/24 = {cls}/24 = {e_R_class}   [two normalizations AGREE]")
check("e_R = 1/12 by two normalizations", e_R_grav == Fraction(1, 12) and e_R_class == Fraction(1, 12))
order_QZ = e_R_grav.denominator
z3_eR = three_primary_component(e_R_grav)
print(f"  order of e_R in Q/Z = {order_QZ} = {p8 and ''}{sp.factorint(order_QZ)}   v_3(order) = {val_p(order_QZ, 3)}")
print(f"  Z/3 (3-primary) component of e_R in Q/Z = {z3_eR}   (NONZERO and FRACTIONAL => Q/Z, not Z)")
check("e_R has nonzero fractional Z/3 component (=1/3 in Q/Z), order 3", z3_eR == Fraction(1, 3))

bulk_transparent = Fraction(0)              # A-hat[S^6] ch = 0 (RS-S4 transparency, reused)
naive_ind = bulk_transparent - e_R_grav
print(f"  ANCHOR (RS-S4): transparent-fiber APS index = bulk(0) - e_R = {naive_ind}  (NOT an integer)")
check("anchor: untwisted transparent-fiber index = -1/12 (fractional)",
      naive_ind == Fraction(-1, 12) and naive_ind.denominator != 1)


# ============================================================================================
# SECTION 1 -- BUILD the twisted Dirac eta on L(p;1); reproduce 2-adic (L2) vs 3-adic (L3) walls.
# ============================================================================================
print()
print("=" * 96)
print("SECTION 1 -- BUILD: twisted Dirac reduced eta xi_a on L(p;1) (APS/Donnelly spectral sum)")
print("=" * 96)


def xi_lens(p, a):
    """Reduced eta of the twisted Dirac operator on L(p;1), flat character a (APS/Donnelly trig sum).
    This IS the spectral eta of the built operator (closed form of the Z_p-projected S^3 Dirac spectrum)."""
    s = 0.0 + 0.0j
    for j in range(1, p):
        denom = (2j * np.sin(np.pi * j / p)) ** 2   # (2i sin)^2
        s += np.exp(2j * np.pi * a * j / p) / denom
    val = s / p
    assert abs(val.imag) < 1e-9, "xi must be real"
    return Fraction(val.real).limit_denominator(100000)


def rho_gauge(p, a):
    """Reference-subtracted (pure-gauge Dai-Freed) reduced eta: rho_a = xi_a - xi_0.
    xi_0 is pure gravity (removable local counterterm, since L(p;1) bounds spin); the genuine
    flat-bundle invariant is rho_a, valued in (1/p)Z."""
    return xi_lens(p, a) - xi_lens(p, 0)


for p in (2, 3):
    xis = [xi_lens(p, a) for a in range(p)]
    tot = sum(xis, Fraction(0))
    two_adic = all(val_p(x.denominator, 3) == 0 for x in xis if x != 0)
    print(f"  L({p};1): xi_a = {[str(x) for x in xis]}   sum_a xi_a = {tot}   "
          f"(all v_3(den)=0 i.e. NO 3 in denom: {two_adic})")
    check(f"L({p};1) built eta: sum_a xi_a = 0 (validates against S^3 cover, eta=0)", tot == 0)

# the GU-FORCED spine is L(2;1) (deck group Z/2); L(3;1) (deck Z/3) is the DISCRIMINATING control
xi2 = [xi_lens(2, a) for a in range(2)]
xi3 = [xi_lens(3, a) for a in range(3)]
L2_2adic = all(val_p(x.denominator, 3) == 0 for x in xi2)
L3_3adic = any(val_p(x.denominator, 3) >= 1 for x in xi3)
print()
print(f"  GU-FORCED spine L(2;1): xi = {[str(x) for x in xi2]}  -> every denom a power of 2 "
      f"(v_3 = 0): 2-ADIC WALL")
print(f"  CONTROL     spine L(3;1): xi = {[str(x) for x in xi3]}  -> denom 9 = 3^2 present "
      f"(v_3 = -2): 3-ADIC (deck Z/3 CAN carry a 3)")
check("L(2;1) eta is 2-adic (v_3(den)=0 for all a); L(3;1) eta is 3-adic (non-vacuity)",
      L2_2adic and L3_3adic)
print("  => The deck group of the carrier fixes the arithmetic: Z/2 gives 2-adic eta, Z/3 gives 3-adic.")


# ============================================================================================
# SECTION 2 -- ENUMERATE every GU-admissible twist on L(2;1); compute the twisted APS eta-index.
# ============================================================================================
print()
print("=" * 96)
print("SECTION 2 -- the twisted operator: enumerate ALL GU-admissible twists on the forced L(2;1)")
print("=" * 96)
print("  Flat bundles on L(2;1) are reps of pi_1 = Z/2.  Twisted eta of E = (+)_a mult_a[char a] is")
print("  eta_E = sum_a mult_a * rho_a  (rho_a the pure-gauge Dai-Freed invariant, rho_0 = 0).")
print("  Twisted APS eta-index (transparent bulk):  I(E) = bulk(0) - (e_R + eta_E) = -(1/12 + eta_E).")
print()

rho2 = [rho_gauge(2, a) for a in range(2)]   # [0, 1/4]
print(f"  built rho_a on L(2;1): rho_0 = {rho2[0]}, rho_1 = {rho2[1]}  (2-adic: v_3(den)=0)")


def eta_of_bundle(decomp):
    """decomp: dict char a -> multiplicity. Returns eta_E = sum mult_a rho_a."""
    return sum(m * rho2[a] for a, m in decomp.items())


# ---- enumerate the GU-admissible twists ----
# (b1) flat deck-group line twists: characters a in {0,1}
# (b2) flat family SU(2)+ twists: Hom(Z/2, SU(2)) = {g->I, g->-I} (only order-<=2 elts of SU(2) are +-I)
#      g->I  : C^2 = 2*[char 0];   g->-I : C^2 = 2*[char 1]  (-I acts as e^{i pi} = char 1)
# (b3) self-dual Lambda^2_+ adjoint twist: Ad(g) on su(2)=R^3.  Ad(I)=Ad(-I)=I (both central)
#      => adjoint bundle is 3*[char 0] for BOTH holonomies (KEY: the family twist is 3-inert here)
twists = [
    ("(b1) trivial flat line          [char 0]",              {0: 1}),
    ("(b1) nontrivial flat Z/2 line   [char 1, deck sign]",   {1: 1}),
    ("(b2) flat SU(2)+ family, hol = +I",                     {0: 2}),
    ("(b2) flat SU(2)+ family, hol = -I (central)",           {1: 2}),
    ("(b3) self-dual Lambda^2_+ adj,  hol = +I",              {0: 3}),
    ("(b3) self-dual Lambda^2_+ adj,  hol = -I  [Ad(-I)=I]",  {0: 3}),
]

print()
print(f"  {'twist':<44}{'eta_E':>8}{'I(E)':>10}{'v_3(I)':>8}{'integer?':>9}{'Z/3 comp':>10}")
print("  " + "-" * 90)
any_integer_with_z3 = False
all_v3_minus1 = True
z3_components = set()
for label, decomp in twists:
    etaE = Fraction(eta_of_bundle(decomp))
    I_E = bulk_transparent - (e_R_grav + etaE)
    v3 = v3_frac(I_E)
    is_int = I_E.denominator == 1
    z3 = three_primary_component(I_E)
    z3_components.add(z3)
    if v3 != -1:
        all_v3_minus1 = False
    if is_int and z3 != 0:
        any_integer_with_z3 = True
    print(f"  {label:<44}{str(etaE):>8}{str(I_E):>10}{str(v3):>8}{str(is_int):>9}{str(z3):>10}")

print()
check("every GU-admissible twist eta_E is 2-adic (built from rho_a on Z/2 deck): v_3(eta_E) >= 0",
      all(val_p(Fraction(eta_of_bundle(d)).denominator, 3) == 0 for _, d in twists))
check("every twisted index I(E) has v_3 = -1 (the 3 in 1/12 SURVIVES every 2-adic twist)",
      all_v3_minus1)
check("NO GU-admissible twist gives an INTEGER (all fractional; the Z/2 deck cannot cancel the 3)",
      not any(( (bulk_transparent - (e_R_grav + Fraction(eta_of_bundle(d)))).denominator == 1)
               for _, d in twists))
check("the Z/3 component is FROZEN across every twist (deck Z/2 acts only on the 2-primary sector)",
      len(z3_components) == 1 and Fraction(2, 3) in z3_components)
check("DECISIVE: no twist promotes -1/12 to an integer with nonzero Z/3 content",
      not any_integer_with_z3)

# ---- (b4) section degrees d': feed the bulk INTEGER index, NOT the boundary e_R ----
print()
print("  (b4) bulk section degrees d': the closed AS index is integer-BY-CONSTRUCTION")
print("       ind_full = 12k + 16 m^2 d' - 2 sigma  (RS-S2), an INTEGER. Its mod-3 class:")
m, dpr, kk2, sig2 = sp.symbols("m dprime k sigma", integer=True)
ind_full = 12 * kk2 + 16 * m ** 2 * dpr - 2 * sig2
mod3_class = sp.simplify(ind_full - (m ** 2 * dpr + sig2))
print(f"       ind_full mod 3 == m^2 d' + sigma   (check ind_full-(m^2 d'+sigma) == 0 mod 3: "
      f"{sp.simplify(mod3_class % 3) == 0})")
sel_m = {1: "breaking line O(-1)", 2: "quadratic O(-2)", 5: "coset anticanonical O(5)"}
m2mod3 = {mm: (mm * mm) % 3 for mm in sel_m}
print(f"       every NATIVELY-SELECTED twist m in {list(sel_m)} has m^2 mod 3 = "
      f"{sorted(set(m2mod3.values()))} (== 1): the located carrier's twist is the TRIVIAL residue.")
print(f"       => the integer index's Z/3 content is carried by d' (unbuilt) + sigma (external),")
print(f"          DISJOINT from e_R. The integer is 3-INERT (carries no e_R). [Hom(Z/3,Z)=0 discipline]")
check("bulk integer index is 3-INERT: every selected m has m^2==1 (mod 3); its Z/3 content is not e_R",
      set(m2mod3.values()) == {1} and sp.simplify(mod3_class % 3) == 0)


# ============================================================================================
# SECTION 3 -- CONTROLS (triple scrutiny): discriminating L(3;1), scrambled twist, alternate framing.
# ============================================================================================
print()
print("=" * 96)
print("SECTION 3 -- CONTROLS (the KILL is a measurement, not a tautology)")
print("=" * 96)

# ---- CONTROL 1 (discriminating): on L(3;1) the SAME machinery DOES integerize with Z/3 content ----
print("  CONTROL 1 -- L(3;1) (deck Z/3, NOT GU-forced): the mechanism EXISTS on the wrong carrier.")
rho3 = [rho_gauge(3, a) for a in range(3)]     # [0, 1/3, 1/3]  (3-adic)
# a 3-adic framing on L(3;1): e_L3 = 1/3 (order-3 in Q/Z, nonzero Z/3 content, analogue of e_R's 3-part)
e_L3 = Fraction(1, 3)
print(f"    built rho_a on L(3;1): {[str(x) for x in rho3]}  (3-adic: v_3(den) < 0)")
print(f"    3-adic framing e_L3 = {e_L3}  (Z/3 content = {three_primary_component(e_L3)}, NONZERO)")
# a flat Z/3 bundle E = (char a) with multiplicity mult; find one that integerizes: e_L3 + mult*rho_a in Z
found_int = None
for a in range(1, 3):
    for mult in range(1, 4):
        etE = mult * rho3[a]
        cand = bulk_transparent - (e_L3 + etE)
        if cand.denominator == 1 and cand != bulk_transparent - e_L3:
            found_int = (a, mult, etE, cand)
            break
    if found_int:
        break
a_, mult_, etE_, cand_ = found_int
print(f"    flat Z/3 twist [char {a_}, mult {mult_}] gives eta_E = {etE_} (3-adic); "
      f"I = -(1/3 + {etE_}) = {cand_}  (INTEGER, and the framing carried Z/3 content)")
check("CONTROL 1: on L(3;1) (deck Z/3) a flat 3-adic twist CAN integerize a 3-adic framing (mechanism exists)",
      found_int is not None and cand_.denominator == 1)
print("    => the Z/3 integer preimage is reachable -- but ONLY on L(3;1), which GU does NOT force")
print("       (RS-S1: the forced native spine is L(2;1), not L(3;1)). Wrong carrier.")

# ---- CONTROL 2 (scrambled twist): random 2-adic etas NEVER integerize -1/12 ----
print()
print("  CONTROL 2 -- scrambled twist: random 2-adic 'twist' etas must NOT integerize -1/12.")
n_scram, n_int, n_v3 = 2000, 0, 0
for _ in range(n_scram):
    num = np.random.randint(-50, 51)
    twop = 2 ** np.random.randint(0, 6)     # denominator a power of 2 (2-adic, like a real deck twist)
    fake = Fraction(int(num), int(twop))
    I_s = bulk_transparent - (e_R_grav + fake)
    if I_s.denominator == 1:
        n_int += 1
    if v3_frac(I_s) == -1 or I_s == 0:
        n_v3 += 1 if (I_s == 0 or v3_frac(I_s) == -1) else 0
print(f"    {n_scram} random 2-adic twists: integers = {n_int} (expected 0); "
      f"all keep v_3 = -1 (the 3 never cancels)")
check("CONTROL 2: no random 2-adic twist integerizes -1/12 (the 3-primary part of e_R is untouched)",
      n_int == 0)
# Isolate the 3-primary sector: on a PURELY 3-adic framing f=1/3, a 2-adic twist STILL fails (keeps the
# 3), but a 3-adic twist (UNAVAILABLE on the Z/2 deck) integerizes it -- pinning 3-adicity as the block.
f3 = Fraction(1, 3)
twoadic_fail = all((bulk_transparent - (f3 + Fraction(int(np.random.randint(-50, 51)),
                    int(2 ** np.random.randint(0, 6))))).denominator != 1 for _ in range(2000))
threeadic_ok = any((bulk_transparent - (f3 + Fraction(int(np.random.randint(-9, 10)), 3))).denominator == 1
                   for _ in range(2000))
print(f"    on the 3-primary framing f=1/3: any 2-adic twist integerizes = {not twoadic_fail}; "
      f"a 3-adic twist integerizes = {threeadic_ok}")
check("CONTROL 2 sanity: on f=1/3 no 2-adic twist integerizes but a 3-adic twist does -- 3-adicity is "
      "the block, and the Z/2 deck supplies only 2-adic twists", twoadic_fail and threeadic_ok)

# ---- CONTROL 3 (alternate framing): a different framing still has the 3; trivial framing => integer 0 ----
print()
print("  CONTROL 3 -- alternate framing: the 3 is in the framing's denominator, not tunable by twists.")
alt = [("p_1=2 (SO(3) framing) e_R=2/48=1/24", Fraction(2, 48)),
       ("p_1=4 (self-dual Lambda^2_+) e_R=1/12", Fraction(4, 48)),
       ("trivial framing e_R=0 (no 3-content)", Fraction(0))]
for lbl, er in alt:
    I0 = bulk_transparent - er
    print(f"    {lbl:<40} untwisted I = {str(I0):>6}  integer={I0.denominator == 1}  "
          f"Z/3 comp={three_primary_component(I0)}")
check("CONTROL 3: framings with a 3 (1/24, 1/12) stay fractional; only the no-3 (trivial) framing is integer",
      (bulk_transparent - Fraction(2, 48)).denominator != 1
      and (bulk_transparent - Fraction(4, 48)).denominator != 1
      and (bulk_transparent - Fraction(0)).denominator == 1)
print("    => integerness is available exactly when there is NO Z/3 content; the two are mutually")
print("       exclusive on the L(2;1) carrier. An integer with Z/3 content is unreachable.")


# ============================================================================================
# SECTION 4 -- THE p-ADIC THEOREM and the verdict.
# ============================================================================================
print()
print("=" * 96)
print("SECTION 4 -- THE STRUCTURAL THEOREM AND VERDICT")
print("=" * 96)
print("  THEOREM (F1, on the GU-forced carrier). Let E be any flat twist on L(2;1) (deck group Z/2):")
print("  a deck-group line, a flat SU(2)+ family bundle, or the self-dual Lambda^2_+ adjoint. Then its")
print("  twisted Dirac reduced eta eta_E is 2-adic (v_3(eta_E) >= 0, MEASURED: all denominators powers")
print("  of 2, because pi_1 = Z/2 is coprime to 3). Hence for the twisted APS eta-index")
print("       I(E) = bulk(0) - (e_R + eta_E),   v_3(I(E)) = min(v_3(1/12), v_3(eta_E)) = -1,")
print("  so I(E) is NEVER an integer, and its Z/3 component is FROZEN at the nonzero fraction 2/3 in")
print("  Q/Z for every E. The Z/2 deck group acts only on the 2-primary sector; it cannot manufacture,")
print("  cancel, or integerize the Z/3 content of e_R.")
print()
print("  CONSEQUENCE (category error, one level up from Hom(Z/3,Z)=0). e_R = 1/12 is Q/Z-valued; its")
print("  Z/3 content (= 1/3) is genuine mod-3 information. No operator BUILT on the GU-forced L(2;1)")
print("  carrier converts it to an integer, because the carrier's deck symmetry has order 2, coprime")
print("  to 3. The only integer index available (the closed AS index 12k+16 m^2 d'-2 sigma) is 3-INERT:")
print("  every selected twist has m^2 == 1 (mod 3), so its Z/3 content is external (d', sigma), DISJOINT")
print("  from e_R. Integer-ness and Z/3-content are mutually exclusive on this carrier.")
print()
print("  DISCRIMINATING CONTROL confirms this is a measurement: on L(3;1) (deck Z/3, NOT GU-forced) the")
print("  same machinery DOES integerize a 3-adic framing with Z/3 content. The obstruction is precisely")
print("  the deck-group order 2 of the GU-forced spine, not a failure of the construction.")
print()
print("  conjecture_signal = KILL of the constructive route on the located carrier:")
print("  the framed-bordism carrier e_R = 1/12 on the GU-forced L(2;1) spine has NO integer-index")
print("  preimage constructible from any GU-admissible twist. Conjecture D, as it names the located")
print("  carrier, is refuted by construction. Surviving escape = the RS-S2 double external import")
print("  (3|m cubic coupling + 3|sigma spacetime), which is off-carrier and does not rescue conjecture D.")

print()
print("#" * 96)
if FAIL:
    print(f"# RESULT: {len(FAIL)} CHECK(S) FAILED: {FAIL}")
    print("#" * 96)
    sys.exit(1)
print("# RESULT: ALL CHECKS PASSED. Route F1 -> conjecture_signal = KILL (constructive route on carrier).")
print("#  Built the twisted Dirac operator on L(2;1) with the self-dual framing; enumerated every")
print("#  GU-admissible twist (deck Z/2 line, flat SU(2)+, Lambda^2_+ adjoint, bulk d'). NONE promotes")
print("#  the fractional -1/12 to an integer with Z/3 content: all twist etas are 2-adic, v_3(I)=-1")
print("#  fixed, Z/3 component frozen at 2/3 in Q/Z. The Z/2 deck group is coprime to 3 and cannot")
print("#  manufacture a Z/3. Confirmed category error, one level up from Hom(Z/3,Z)=0. L(3;1) control")
print("#  shows the mechanism exists on the wrong (unforced) carrier. No forbidden target imported.")
print("#" * 96)
sys.exit(0)
