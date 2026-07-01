#!/usr/bin/env python3
"""
Is 'net chiral index of the mass operator == 0' VACUOUS (always 0 on this triplet),
or is it a real property forced by the moment-map structure?

Net chiral index of a chirality-EVEN (mass) operator M = kerdim(M_++) - kerdim(M_--),
where M_++ , M_-- are the two chirality blocks (M commutes with omega so it block-splits).

Demonstration:
  * A hand-built chirality-EVEN operator with M_++ = 0 (96-dim kernel) and M_-- = I (no kernel)
    is a perfectly legal operator on this exact triplet and has net chiral index = +96 != 0.
    => the (96,96)-balanced space does NOT force index 0. The index is content-bearing.
  * The moment-map mass M(mu) = sum mu_k Sig_k is pinned to index 0 for EVERY Psi because it
    commutes with the chirality-swap P=c(e_b), which the hand-built operator does NOT.
"""
import numpy as np
import importlib.util, sys, os
spec = importlib.util.spec_from_file_location("ic", os.path.join(os.path.dirname(__file__), "indep_check.py"))
ic = importlib.util.module_from_spec(spec); sys.modules["ic"] = ic
# we only need build(); avoid running its main
src = open(os.path.join(os.path.dirname(__file__), "indep_check.py")).read()
exec(compile(src.split("def main()")[0], "ic_partial", "exec"), ic.__dict__)

e, K, Jfull, Sig, Wt, chir, top = ic.build()
d = Wt.shape[1]
chir_tr = 0.5 * (Wt.conj().T @ chir @ Wt + (Wt.conj().T @ chir @ Wt).conj().T)
cev, cU = np.linalg.eigh(chir_tr)
Pp = cU[:, cev > 0.5]; Pm = cU[:, cev < -0.5]
np_, nm_ = Pp.shape[1], Pm.shape[1]
print(f"triplet dim={d}, chirality split (+,-)=({np_},{nm_})")

# ---- hand-built EVEN operator with maximally imbalanced kernel ----
Mhand = Pm @ Pm.conj().T          # = 0 on +sector, = I on -sector (chirality-even, Hermitian)
# net chiral index of kernel:
def netchir_kernel(M):
    ev, U = np.linalg.eigh(0.5*(M+M.conj().T))
    ker = U[:, np.abs(ev) < 1e-8]
    g = np.trace(ker.conj().T @ chir_tr @ ker).real
    kpp = np.trace((Pp.conj().T@ker).conj().T @ (Pp.conj().T@ker)).real
    kmm = np.trace((Pm.conj().T@ker).conj().T @ (Pm.conj().T@ker)).real
    return g, ker.shape[1], kpp, kmm
g, kd, kpp, kmm = netchir_kernel(Mhand)
print(f"[hand-built even op M=(0 on +, I on -)]: ker dim={kd}, net chiral index (graded tr over ker)={g:+.1f} "
      f"(kerdim+={kpp:.0f}, kerdim-={kmm:.0f})  => NONZERO index is achievable on this space")

# does it commute with the chirality-swap? (it should NOT)
Pb = Wt.conj().T @ np.kron(np.eye(14, dtype=complex), e[9]) @ Wt
c_hand = np.linalg.norm(Pb@Mhand - Mhand@Pb)/(np.linalg.norm(Mhand)*np.linalg.norm(Pb)+1e-30)
print(f"[hand-built] [P, M_hand]/norm = {c_hand:.2e}  (NOT ~0 -> swap does not protect it, index free to be !=0)")

# ---- the actual moment-map mass operator over many Psi ----
Jr = [Wt.conj().T @ Jfull[k] @ Wt for k in range(3)]
Kr = 0.5*(Wt.conj().T@K@Wt + (Wt.conj().T@K@Wt).conj().T)
KJ = [Kr@Jr[k] for k in range(3)]
Sigr = [Wt.conj().T @ np.kron(np.eye(14, dtype=complex), Sig[k]) @ Wt for k in range(3)]
rng = np.random.default_rng(99)
worst_idx = 0.0; worst_comm = 0.0
for _ in range(150):
    psi = rng.standard_normal(d)+1j*rng.standard_normal(d)
    mu = np.array([np.vdot(psi, KJ[k]@psi) for k in range(3)])
    M = sum(mu[k]*Sigr[k] for k in range(3)); M = 0.5*(M+M.conj().T)
    g, kd, kpp, kmm = netchir_kernel(M)
    worst_idx = max(worst_idx, abs(g))
    worst_comm = max(worst_comm, np.linalg.norm(Pb@M-M@Pb)/(np.linalg.norm(M)*np.linalg.norm(Pb)+1e-30))
print(f"[moment-map M(mu), 150 Psi]: max|net chiral index over ker| = {worst_idx:.2e}  "
      f"max [P,M]/norm = {worst_comm:.2e}")
print()
print("CONCLUSION: index != 0 IS achievable on the (96,96) triplet (hand-built op gives +96).")
print("The moment-map mass operator is pinned to index 0 BECAUSE it commutes with the")
print("chirality-swap P=c(e_b) (mu lives in span(Sig_k)=commutant of P). Result is NON-VACUOUS.")
