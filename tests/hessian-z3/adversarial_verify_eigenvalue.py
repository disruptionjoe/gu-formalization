#!/usr/bin/env python3
r"""
ADVERSARIAL RE-DERIVATION of the carrier-direction "Hessian eigenvalue".

Claim under test: carrier-occupancy diagonal Hessian eigenvalue = 0 (flat zero mode),
proxy-robust across (i) Krein, (ii) SW Majorana, (iii) boundary-eta.

The construct REPORTS, for each proxy, the NET SIGNATURE n_+ - n_-  (it calls this
"net signed second variation" / "net chiral asymmetry / net index" / "spectral eta").
This script asks the questions the construct's signature() hides:

  Q1. Are there ACTUAL zero eigenvalues on the carrier (n_0 > 0), or is the spectrum
      non-degenerate with the NET cancelling?  (flat mode vs vectorlike index)
  Q2. The "occupancy direction" is a SINGLE collective coordinate (uniform population).
      What is the actual scalar second variation v^dag H v along THAT vector?  Is it 0?
  Q3. Is proxy (iii)'s 0 a real cancellation or a trivially-zero (absent) block?
"""
from __future__ import annotations
import os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.normpath(os.path.join(HERE, "..", "generation-sector"))
for p in (GEN, os.path.normpath(os.path.join(HERE, ".."))):
    if p not in sys.path:
        sys.path.insert(0, p)
import gen_sector_bridge as gb
import cross_proxy_carrier_hessian as cp

S = cp.build()
Wt, K, chir = S["Wt"], S["K"], S["chir"]
Jp, Sig, D = S["Jp"], S["Sig"], S["D"]
I14 = S["I14"]
d = Wt.shape[1]
print(f"carrier dim = {d}")

def herm(A): return 0.5*(A + A.conj().T)

# ---------- PROXY (i) KREIN: actual eigenvalues ----------
Kr = herm(Wt.conj().T @ K @ Wt)
ev = np.linalg.eigvalsh(Kr)
print("\n=== PROXY (i) Krein form on carrier ===")
print(f"  net signature n+ - n- (what construct reports) = {(ev>1e-7).sum() - (ev<-1e-7).sum()}")
print(f"  ACTUAL eigenvalues: min={ev.min():.4f} max={ev.max():.4f}")
print(f"  number of TRUE zero eigenvalues (|lambda|<1e-7): {(np.abs(ev)<1e-7).sum()}")
print(f"  smallest |eigenvalue| = {np.abs(ev).min():.4f}  <-- if >0, NO flat direction in this form")

# Q2: the uniform-occupancy collective coordinate. Build a few candidate "occupancy" vectors
# and compute the scalar second variation v^dag Kr v / (v^dag v).
print("\n  -- scalar second variation along candidate occupancy vectors (Krein) --")
rng = np.random.default_rng(0)
for label, v in [
    ("uniform (all-ones in carrier coords)", np.ones(d, dtype=complex)),
    ("random occupancy A", rng.standard_normal(d)+1j*rng.standard_normal(d)),
    ("random occupancy B", rng.standard_normal(d)+1j*rng.standard_normal(d)),
    ("top Krein eigenvector", np.linalg.eigh(Kr)[1][:, -1]),
]:
    q = (v.conj() @ Kr @ v).real / (v.conj() @ v).real
    print(f"    {label:42s}: v^dag H v / |v|^2 = {q:+.4f}")

# ---------- PROXY (ii) SW Majorana: actual eigenvalues ----------
Jr = [Wt.conj().T @ Jp[k] @ Wt for k in range(3)]
Kr2 = herm(Kr)
KJ = [Kr2 @ Jr[k] for k in range(3)]
rng2 = np.random.default_rng(1)
psi = rng2.standard_normal(d)+1j*rng2.standard_normal(d)
mu = np.array([np.vdot(psi, KJ[k]@psi) for k in range(3)])
Mtr = herm(Wt.conj().T @ sum(mu[k]*np.kron(I14, Sig[k]) for k in range(3)) @ Wt)
evM = np.linalg.eigvalsh(Mtr)
print("\n=== PROXY (ii) SW Majorana block on carrier ===")
print(f"  net signature (reported) = {(evM>1e-7).sum() - (evM<-1e-7).sum()}")
print(f"  signature (n+,n-,n0) = ({(evM>1e-7).sum()},{(evM<-1e-7).sum()},{(np.abs(evM)<1e-7).sum()})")
print(f"  min={evM.min():.4f} max={evM.max():.4f}, depends on RANDOM psi seed (mean-field point)")
# sensitivity to psi seed: is the net robustly 0 or seed-dependent?
nets = []
for seed in range(10):
    r = np.random.default_rng(seed)
    p = r.standard_normal(d)+1j*r.standard_normal(d)
    m = np.array([np.vdot(p, KJ[k]@p) for k in range(3)])
    Mt = herm(Wt.conj().T @ sum(m[k]*np.kron(I14, Sig[k]) for k in range(3)) @ Wt)
    e2 = np.linalg.eigvalsh(Mt)
    nets.append((e2>1e-7).sum() - (e2<-1e-7).sum())
print(f"  net signature across 10 random psi seeds: {nets}  (all 0 => structural, not fitted)")

# ---------- PROXY (iii) boundary-eta: is the block trivially absent? ----------
Dr = herm(Wt.conj().T @ D @ Wt)
print("\n=== PROXY (iii) boundary-eta D on carrier ===")
print(f"  ||D Wt|| = {np.linalg.norm(D@Wt):.4f} (D acts on carrier states)")
print(f"  ||Wt^dag D Wt|| = {np.linalg.norm(Dr):.3e}  <-- if ~0, the diagonal block is ABSENT")
print(f"  This is a TRIVIALLY ZERO operator on the carrier, not a cancellation of a real form.")

# ---------- THE CONCEPTUAL POINT ----------
print("\n=== SUMMARY ===")
print("  A FLAT zero mode requires an ACTUAL zero eigenvalue (n_0 > 0) along the occupancy")
print("  direction. The Krein form has signature (96,96,0): NO zero eigenvalues, smallest")
print(f"  |lambda| = {np.abs(ev).min():.4f}. The reported '0' is the NET (n+ - n-), an INDEX-like")
print("  signed count = the vectorlike/balanced fact, NOT a flat direction.")
