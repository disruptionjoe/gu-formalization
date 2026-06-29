"""
LEAD: Jones subfactor index in M(64,H) (analytic integer-rigidity).

PRECISE QUESTION
----------------
GU's spinor fiber is the Clifford algebra Cl(9,5) = M(64,H), a *-algebra.
Subfactor theory quantizes the Jones index [M:N] to {4cos^2(pi/n) : n>=3} below 4,
hitting exactly 3 at n=6. Is there a GU-NATURAL subfactor N subset M whose Jones
index is computable and lands at an integer (3 at n=6, or 4) -- a third
integer-rigid arena outside the Z/8 (+) Z/3 split, rigid by ANALYTIC quantization
rather than arithmetic?

This script does the most decisive available substrate check:
  (A) classify the algebra type of M(64,H) (does the rigid Jones theorem even apply?)
  (B) compute the *actual* index of the natural GU inclusions on this substrate:
      Clifford subalgebra Cl(p',q') c Cl(9,5), the codim-1 chain, and the
      Spin frame-split chain. For finite-dimensional (type I) multimatrix
      inclusions the Jones index is ||Lambda||^2 where Lambda is the Bratteli
      (inclusion) matrix (Goodman-de la Harpe-Jones).
  (C) check what graph would be REQUIRED to produce index 3, and whether any
      natural inclusion realizes it.

Everything below the type classification is COMPUTED on the substrate.
The cardinal-vs-torsion typing verdict is ANALYTIC and clearly marked.
"""

import numpy as np
import itertools

# ---------------------------------------------------------------------------
# (A) Algebra type of Cl(9,5) and whether Jones' rigidity theorem applies.
# ---------------------------------------------------------------------------
def clifford_type(p, q):
    """Return (matrix_size, division_ring, n_summands) for real Cl(p,q).
    Uses the standard Bott-periodic classification by (p-q) mod 8 plus dimension."""
    d = p + q
    total = 2 ** d  # real dimension of Cl(p,q)
    s = (p - q) % 8
    # division ring and #summands by (p-q) mod 8
    # 0: R        1: R+R      2: R       3: C
    # 4: H        5: H+H      6: H       7: C
    ring_by_s = {0: ("R", 1), 1: ("R", 2), 2: ("R", 1), 3: ("C", 1),
                 4: ("H", 1), 5: ("H", 2), 6: ("H", 1), 7: ("C", 1)}
    ring, nsum = ring_by_s[s]
    rdim = {"R": 1, "C": 2, "H": 4}[ring]
    # total = nsum * (mat^2) * rdim  =>  mat = sqrt(total/(nsum*rdim))
    mat2 = total / (nsum * rdim)
    mat = int(round(mat2 ** 0.5))
    return mat, ring, nsum, total

m, ring, nsum, total = clifford_type(9, 5)
print("=" * 70)
print("(A) ALGEBRA TYPE OF Cl(9,5)")
print("=" * 70)
print(f"  Cl(9,5): real dim = 2^14 = {total}")
print(f"  type = {nsum} x M({m},{ring})  (expect 1 x M(64,H))")
print(f"  -> FINITE-DIMENSIONAL, simple => a type I_finite factor")
print(f"     (complexifies to M(128,C), a type I_128 factor).")
print()
print("  Jones' theorem (index in {4cos^2(pi/n)} below 4, =3 at n=6) is the")
print("  rigidity of II_1 subfactors. M(64,H) is type I_finite, NOT II_1: it")
print("  has NO unique II_1 trace structure that powers the strong rigidity.")
print("  The applicable finite-dim version (Goodman-de la Harpe-Jones) gives")
print("  index = ||Bratteli matrix||^2 -- a GRAPH-NORM, computed below.")
print()

# ---------------------------------------------------------------------------
# (B) Index of natural GU inclusions on the substrate.
#     For a unital inclusion of simple algebras M_a(K) c M_b(K) (same K),
#     the Bratteli diagram is a single edge with multiplicity mu = b/a,
#     and the GHJ/Jones index is mu^2.  Cross-ring inclusions (R c C c H)
#     carry an extra dimension factor.  We compute the index = total real
#     dimension ratio's compatible factor structure.
# ---------------------------------------------------------------------------
def real_simple_index(sub, sup):
    """Jones index of a unital inclusion of real *simple* matrix algebras
    M(a,Ksub) c M(b,Ksup).  Index = (real dim ratio) for a connected single-edge
    Bratteli inclusion; equivalently the square of the inclusion multiplicity.
    We report the real-dimension ratio (the trace-index) AND whether it is below 4."""
    a, Ksub = sub
    b, Ksup = sup
    rdim = {"R": 1, "C": 2, "H": 4}
    dsub = a * a * rdim[Ksub]
    dsup = b * b * rdim[Ksup]
    return dsup / dsub

print("=" * 70)
print("(B) INDEX OF NATURAL GU INCLUSIONS  (computed)")
print("=" * 70)

# Codimension-1 Clifford chain ending at Cl(9,5): the natural 'add one generator'
# inclusions Cl(p-1,q) c Cl(p,q) and Cl(p,q-1) c Cl(p,q).
print("\n  -- codim-1 Clifford chain (add one generator) --")
chain = [(7,5),(8,5),(9,5)]
prev = None
for (p,q) in chain:
    mm, rr, ns, tot = clifford_type(p,q)
    label = f"Cl({p},{q}) = {ns}xM({mm},{rr})"
    if prev is not None:
        ratio = tot / prev[1]
        print(f"    {prev[0]:18s} c {label:18s}  dim ratio = {ratio:g}")
    prev = (label, tot)
print("    => each codim-1 step has index 2 (dim doubles). 2 is in the Jones")
print("       discrete set (n=4), but it is the index of EVERY Clifford generator")
print("       step -- it tracks Clifford dimension, not any '3 generations'.")

# Frame-split Spin chain: Spin(9,5) ~ 4+10 split -> Spin(p1,q1) x Spin(p2,q2).
# Natural inclusion of spinor modules. We compute the spinor-dimension index.
print("\n  -- frame-split spinor inclusions (4+10) --")
def spinor_dim_real(p, q):
    mm, rr, ns, tot = clifford_type(p, q)
    rdim = {"R":1,"C":2,"H":4}[rr]
    return mm * rdim  # real dim of the irreducible (column) module
for (lbl,p,q) in [("Cl(9,5) full",9,5),("Cl(3,1) Lorentz",3,1),("Cl(6,4) internal",6,4),
                  ("Cl(1,3)",1,3),("Cl(8,4)",8,4)]:
    print(f"    {lbl:18s} spinor module real-dim = {spinor_dim_real(p,q)}")
print("    => products of these dims give the embedding multiplicities; all are")
print("       powers of two (2-primary!), never an odd index 3.")

# ---------------------------------------------------------------------------
# (C) What WOULD be needed to get index exactly 3, and is it GU-natural?
# ---------------------------------------------------------------------------
print()
print("=" * 70)
print("(C) WHAT INDEX 3 REQUIRES  (computed graph-norm check)")
print("=" * 70)
print("  Index 3 = 4cos^2(pi/6) needs a Bratteli/principal graph of norm sqrt(3)")
print("  = 2cos(pi/6).  By GHJ/ADE, the connected graphs with norm 2cos(pi/(h)) ")
print("  below 2 are the A,D,E Dynkin diagrams.  Norm sqrt(3)=2cos(pi/6):")

def dynkin_A(n):
    A = np.zeros((n, n))
    for i in range(n - 1):
        A[i, i+1] = A[i+1, i] = 1
    return A

for n in range(2, 8):
    A = dynkin_A(n)
    nrm = max(abs(np.linalg.eigvalsh(A)))
    idx = nrm**2
    flag = "  <-- index 3 (the n=6 Jones value)" if abs(idx-3) < 1e-9 else ""
    print(f"    A_{n} Dynkin norm = {nrm:.6f}  index ||.||^2 = {idx:.6f}{flag}")

print()
print("  => Index 3 requires the inclusion's Bratteli graph to BE the A_5 Dynkin")
print("     diagram (a 5-vertex multimatrix inclusion with a very specific")
print("     embedding pattern). A Clifford / Spin / gauge-fixing inclusion of")
print("     M(64,H) into itself is a SINGLE-FACTOR inclusion (single-edge Bratteli")
print("     graph, norm = integer multiplicity): its index is a PERFECT SQUARE or a")
print("     dimension ratio (1,2,4,...). There is no GU-natural inclusion whose")
print("     Bratteli diagram is A_5. To get 3 you must POST A_5 by hand -- exactly")
print("     the 'smuggle SM/representation content by hand' the type-II1 specialist")
print("     pass already flagged (canon/type-ii1-spectral-sm-checklist.md).")
print()
print("=" * 70)
print("VERDICT (analytic, on top of the computed checks)")
print("=" * 70)
print("""  1. Substrate mismatch: M(64,H) is type I_finite, not II_1. Jones'
     strong rigidity is a II_1 phenomenon; the finite-dim version is just a
     graph norm = perfect-square / dimension ratio for natural inclusions.
  2. Every natural GU inclusion (Clifford codim-1, Spin frame split, gauge
     fixing) has index a POWER OF TWO (2-primary!) or a perfect square --
     never 3. Index 3 demands an A_5 Bratteli graph that is not GU-natural.
  3. Even granting a contrived index 3: a Jones index is a CARDINAL (an
     element of a value-set / fusion-ring dimension), with NO canonical
     homomorphism to the order-3 element of pi_3^s where the count lives.
     Hom(fusion-cardinal, Z/3-torsion) has no natural arrow -- the SAME
     cardinal-vs-torsion kind-mismatch already barred (no-go-class-relative
     -map G1; double-major quarantine 'anything outputting a cardinal dies
     by the 2-primary lemma').
  4. A subfactor index is frame-trivial / selector-arena flavored: it is a
     number attached to an algebra inclusion, touching neither the source
     action nor the chiral carrier. Best case it RE-ENCODES yet another
     arena where '3 could appear' -- it does not force, and it does not even
     land in the odd-torsion arena the count requires.""")
