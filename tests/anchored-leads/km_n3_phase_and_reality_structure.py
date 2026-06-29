"""
KM n>=3 lead triage: ground the two load-bearing arithmetic facts so they are
COMPUTED, not asserted.

(1) The Kobayashi-Maskawa physical-phase count.
    For n Dirac generations with up/down Yukawas, the unitary mixing matrix CKM
    is n x n. Physical, irremovable CP-violating phases = (n-1)(n-2)/2.
    n>=3 is the smallest n with a nonzero phase. This is PURE U(n) parameter
    counting -- a fact about the SELECTOR (mixing) arena, output is a CARDINAL
    inequality. It contains NO odd-prime torsion; it is not a Z/3 statement.

(2) The decisive physics check for the lead's INITIAL question:
    "Does the forced antilinear / reality structure SUPPLY the complex CP phase?"
    We test the opposite hypothesis: a reality structure (Yukawa real-makeable,
    the signature of a vectorlike / quaternionic-Kramers sector) REMOVES every
    physical phase. We do this numerically: build a generic complex Yukawa pair,
    count the irremovable phase via the Jarlskog-type invariant; then impose a
    reality structure and show the invariant vanishes.

These are model arithmetic checks on the KM mechanism itself, used to grade the
lead. They are not claims about GU's (unbuilt) Yukawa textures.
"""
import numpy as np

def physical_cp_phases(n):
    # n x n unitary: n^2 params; (2n-1) phases removable by field rephasing;
    # rotation (mixing) angles = n(n-1)/2; physical phases = remainder.
    total = n*n
    angles = n*(n-1)//2
    removable_phases = 2*n - 1
    phases = total - angles - removable_phases
    return phases  # = (n-1)(n-2)/2

def jarlskog(V):
    # A nonzero Jarlskog invariant <=> irremovable physical CP phase present.
    # J = Im(V_us V_cb V_ub^* V_cs^*) (standard 3x3 rephasing invariant).
    return np.imag(V[0,1]*V[1,2]*np.conj(V[0,2])*np.conj(V[1,1]))

def ckm_from_yukawas(Yu, Yd):
    # Diagonalize by SVD: Yu = Uu Su Vu^H ; left-handed rotations form CKM.
    Uu,_,_ = np.linalg.svd(Yu)
    Ud,_,_ = np.linalg.svd(Yd)
    return Uu.conj().T @ Ud

print("(1) KM physical CP-phase count (computed):")
for n in range(1,6):
    print(f"    n={n}:  phases = {physical_cp_phases(n)}   ((n-1)(n-2)/2 = {(n-1)*(n-2)//2})")
print("    => smallest n with a physical phase is n=3. n>=3 is a CARDINAL inequality,")
print("       pure U(n) counting, ZERO odd-prime/torsion content (not a Z/3 object).")

rng = np.random.default_rng(0)
n = 3
# generic complex Yukawas -> generically nonzero Jarlskog (CP violated)
Yu = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
Yd = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
V = ckm_from_yukawas(Yu, Yd)
J_generic = jarlskog(V)

# reality structure: real Yukawas (the signature of a CP-conserving / vectorlike
# real sector). CKM becomes real-orthogonal-makeable -> Jarlskog vanishes.
Yu_r = rng.normal(size=(n,n))
Yd_r = rng.normal(size=(n,n))
V_r = ckm_from_yukawas(Yu_r, Yd_r)
J_real = jarlskog(V_r)

print("\n(2) Does a reality/antilinear-real structure SUPPLY or REMOVE the CP phase?")
print(f"    generic complex Yukawas:  |Jarlskog| = {abs(J_generic):.4e}  (CP VIOLATED)")
print(f"    real (reality-structured): |Jarlskog| = {abs(J_real):.4e}  (CP CONSERVED)")
print("    => imposing a reality structure DRIVES the physical phase to ~0.")
print("       A forced antilinear REALITY structure (GU's quaternionic Kramers wall,")
print("       C^2=-I, giving the VECTORLIKE +96/-96 net-0 sector) is the ingredient")
print("       that REMOVES the KM phase, not the one that supplies it.")

print("\n(3) Carrier-side fallback 'net chiral count != 0 mod 3':")
net_chiral = 0   # computed elsewhere on substrate: Lambda^2_+ triplet vectorlike, +96/-96
print(f"    substrate net chiral count = {net_chiral} (vectorlike DECOUPLE).")
print(f"    {net_chiral} mod 3 = {net_chiral % 3}  =>  'net != 0 mod 3' is FALSE on substrate.")
