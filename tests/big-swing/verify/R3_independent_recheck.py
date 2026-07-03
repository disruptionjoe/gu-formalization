#!/usr/bin/env python3
# Independent re-derivation of R3 claims, different code paths, different RNG.
import numpy as np
import itertools, sys

rng = np.random.default_rng(11111)
ok = True
def chk(name, cond, d=""):
    global ok
    ok &= bool(cond)
    print(f"[{'PASS' if cond else 'FAIL'}] {name}  {d}")

# --- 1. GW relation from an INDEPENDENT algebraic identity ------------------
# Claim: for any Hermitian involution eps (eps^2=1) and g5^2=1,
#   D=(1/a)(1+g5 eps) satisfies g5 D + D g5 = a D g5 D.
# Rewrite: a D g5 D - (g5 D + D g5) should be exactly 0. Test on independent eps.
for trial in range(50):
    N = 2*rng.integers(2,6)
    # random Hermitian involution via random orthonormal basis and +-1 signs
    A = rng.standard_normal((N,N))+1j*rng.standard_normal((N,N))
    Q_,_ = np.linalg.qr(A)
    signs = rng.choice([-1.0,1.0], size=N)
    eps = (Q_*signs)@Q_.conj().T
    g5 = np.diag(rng.choice([-1.0,1.0], size=N))  # arbitrary involution, not nec balanced
    a = rng.uniform(0.3,2.0)
    D = (1/a)*(np.eye(N)+g5@eps)
    resid = a*(D@g5@D) - (g5@D+D@g5)
    if np.linalg.norm(resid) > 1e-9:
        chk("GW residual", False, f"trial{trial} {np.linalg.norm(resid):.2e}"); break
else:
    chk("GW relation holds for 50 independent (eps,g5,a) with a arbitrary", True)

# --- 2. Independent index of engineered operator ----------------------------
# Q = -(1/2)Tr sign(H). Reconstruct the engineered H and count directly, no D.
nplus=nminus=6; N=12
g5 = np.diag([1.0]*6+[-1.0]*6)
r_neg, l_pos = 2, 3
h = np.array([1.0]*6+[-1.0]*6)
h[:r_neg] = -1.0
h[nplus:nplus+l_pos] = 1.0
eps = np.sign(h)
Q = -0.5*np.sum(eps)
# independent: count zero modes of D as sites where g5*eps = -1
diag_g5eps = np.diag(g5)*eps
zeromodes = np.sum(np.isclose(diag_g5eps, -1.0))
# chirality: among zero-mode sites, sign of g5
zm_idx = np.where(np.isclose(diag_g5eps,-1.0))[0]
nplus_zm = np.sum(np.diag(g5)[zm_idx]>0)
nminus_zm = np.sum(np.diag(g5)[zm_idx]<0)
chk("engineered Q = -1 (independent Tr-sign count)", Q==-1, f"Q={Q}")
chk("zero modes = 5 (g5*eps=-1 count)", zeromodes==5, f"nz={zeromodes}")
chk("chirality n+-n- = Q", (nplus_zm-nminus_zm)==Q, f"n+={nplus_zm} n-={nminus_zm}")

# --- 3. Theorem M independent brute force over G=Z, bigger box, k=2 ----------
mism=0; tot=0
for wv in itertools.product(range(-2,3), repeat=2):
    w=np.array(wv)
    allnn = np.all(w>=0)
    mono=True
    ev=list(itertools.product(range(4),repeat=2))
    for e in ev:
        for ep in ev:
            e=np.array(e); ep=np.array(ep)
            if np.all(e<=ep) and (e@w) > (ep@w):
                mono=False
    tot+=1
    if mono!=allnn: mism+=1
chk("Theorem M iff exhaustive independent (G=Z,k=2,box5x5)", mism==0, f"{tot} pats {mism} mism")

# --- 4. Kramers evenness: independent construction of H-linear operator ------
# A commutes with J: J psi = Om conj(psi), Om block-diag i*sigma_y. Build A that
# is H-linear directly as sum over quaternion basis, check kernel even.
m=4; N=2*m
isy=np.array([[0,1],[-1,0]],dtype=complex)
Om=np.zeros((N,N),dtype=complex)
for i in range(m): Om[2*i:2*i+2,2*i:2*i+2]=isy
badodd=0
for _ in range(100):
    B=rng.standard_normal((N,N))+1j*rng.standard_normal((N,N))
    A=B+Om@B.conj()@np.linalg.inv(Om)   # H-linear
    # verify commute with J: A@(Om@conj) = (Om@conj)@A on random vector
    v=rng.standard_normal(N)+1j*rng.standard_normal(N)
    lhs=A@(Om@v.conj())
    rhs=Om@(A@v).conj()
    if np.linalg.norm(lhs-rhs)>1e-8: badodd+=1; continue
    sv=np.sort(np.linalg.svd(A,compute_uv=False))
    if np.max(np.abs(sv[0::2]-sv[1::2]))>1e-7: badodd+=1
chk("H-linear operators commute with J and have paired sing.values", badodd==0, f"{badodd} bad")

print("\nRESULT:", "ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
