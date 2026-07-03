#!/usr/bin/env python3
# Independent re-check of family_index_bundle.py. DIFFERENT parameter m (=-1.6), DIFFERENT grid
# (Nk=32), and an INDEPENDENT cross-check that does not rely on the value of any single Chern
# number: since P_lower(k) + P_upper(k) = I identically (the two band projectors sum to the trivial
# identity bundle), c1(lower) + c1(upper) = c1(trivial) = 0 as a matter of principle. We verify the
# projector-completeness identity pointwise AND recompute both Chern numbers by FHS at the new
# (m, Nk), confirming each is nonzero and integer and that they cancel, so c1(E_-(D)) = 0.
import numpy as np

NASSERT = 0
def check(c, m):
    global NASSERT
    NASSERT += 1
    assert c, m

s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)

def qwz(kx, ky, m):
    return np.sin(kx) * s1 + np.sin(ky) * s2 + (m + np.cos(kx) + np.cos(ky)) * s3

def vec(kx, ky, m, which):
    w, V = np.linalg.eigh(qwz(kx, ky, m))
    return V[:, 0] if which == "lower" else V[:, 1]

def chern(m, Nk, which):
    g = [[vec(2*np.pi*i/Nk, 2*np.pi*j/Nk, m, which) for j in range(Nk)] for i in range(Nk)]
    U = lambda u, v: (lambda z: z/abs(z))(np.vdot(u, v))
    tot = 0.0
    for i in range(Nk):
        for j in range(Nk):
            a=g[i][j]; b=g[(i+1)%Nk][j]; c=g[i][(j+1)%Nk]; d=g[(i+1)%Nk][(j+1)%Nk]
            tot += np.log(U(a,b)*U(b,d)/U(c,d)/U(a,c)).imag
    return tot/(2*np.pi)

m, Nk = -1.6, 32
cl, cu = chern(m, Nk, "lower"), chern(m, Nk, "upper")
print("independent re-check: QWZ m=%.1f, Nk=%d -> c1(lower)=%+.3f c1(upper)=%+.3f" % (m, Nk, cl, cu))
check(abs(cl-round(cl))<1e-6 and round(cl)!=0, "lower band integer & nonzero")
check(abs(cu-round(cu))<1e-6 and round(cu)!=0, "upper band integer & nonzero")
check(round(cl)+round(cu)==0, "Chern numbers cancel -> c1(E_-(D)) = 0")

# projector-completeness identity P_lower + P_upper = I pointwise (basis-free reason they cancel)
rng = np.random.default_rng(4242)
maxdev = 0.0
for _ in range(40):
    kx, ky = rng.uniform(0, 2*np.pi, 2)
    w, V = np.linalg.eigh(qwz(kx, ky, m))
    Pl = np.outer(V[:, 0], V[:, 0].conj()); Pu = np.outer(V[:, 1], V[:, 1].conj())
    maxdev = max(maxdev, np.max(np.abs(Pl + Pu - np.eye(2))))
check(maxdev < 1e-12, "P_lower + P_upper = I pointwise (trivial total bundle) dev=%.1e" % maxdev)
print("  projector completeness dev = %.1e" % maxdev)
print("INDEPENDENT CHECK PASS: bands cancel (independent m, grid, and completeness identity); asserts %d" % NASSERT)
