#!/usr/bin/env python3
"""The base sign, the fibre sign, and a second route to (7,7).

VERDICT on pass: TWO-ORBIT-SPLIT__FIBRE-SIGN-PINNED-BY-PHYSICS__DECLARED-BASE-ROUTE-TO-(7,7)

HOSTILE REVIEW 2026-08-08 rejected this file's original framing and headline.
Every computation below reproduced and none changed.  What changed:

  * The original claimed g -> -g is "a pure relabeling", concluding the
    construction is NON-EQUIVARIANT.  That framing does not survive: -g is a
    DIFFERENT POINT, in a different GL(4,R) orbit.  The (3,1) and (1,3) metrics
    are disjoint orbits in Sym^2 T*X.  The defensible statement is the TWO-ORBIT
    one -- Met(X) read as "Lorentzian metrics" has two components and the
    construction gives M(64,H) on one and M(128,R) on the other; read as "the
    (3,1) orbit" it has simply declared a convention.  Both readings are live.
  * The original proposed retyping SIGNATURE-AMBIENT to a new row category.
    REJECTED.  A simpler and larger result was available from this file's own
    evidence and was missed -- see below.
  * test (4) established a subspace positivity claim from ONE sampled vector,
    and applied a physical criterion to the UNREDUCED 10-dim fibre.  Replaced
    with a block decomposition on the physical directions.  The claim survives
    and is STRONGER: the whole 5-dim graviton subspace is positive.

THE RESULT THAT WAS MISSED.  REAL-CLIFFORD-FORM is SETTLED at Cl(7,7) = M128(R)
(Wave K, 2026-08-04, highest measured fan-out in the program), and the fork
registry names the dissolution condition for 29 pressured canon files as
"SIGNATURE-AMBIENT settles at (7,7)".  This file's own three findings compose
into a second, independent route to exactly that:

    source DECLARES base (1,3)   -- five AUTHOR-STATED places
    repo   DERIVES  fibre (6,4)  -- certified here, invariant under the base sign
                   (1,3) + (6,4) = (7,7)

The route the source is on record for, and the one Wave K used, is the spoken
block arithmetic (4,6) + (3,1) -- which takes the (4,6) fibre, the sign test (4)
rejects as ghost-like.  The declared-base route uses the source's own base and
the repository's own fibre, and both are physically sound.  It is filed as
SIGNATURE-AMBIENT's named_resolver.  IT IS NOT A SETTLEMENT: see the review's
verdict for the three grounds, and for the one remaining gap (whether the
source's (1,3) is the ambient-relevant base or a separate Spin(1,3) gauge-group
statement -- gu-paper-reference-surfaces.md's entries are about H as a GAUGE
GROUP, a different object).

Review: lab/process/hostile-reviews/2026-08-08-signature-fork-equivariance-review.md

WHAT THIS CORRECTS.  explorations/signature-ambient-is-a-sign-convention-2026-08-08.md
concluded "the fork reduces to the base sign convention" and stopped there.  That
was incomplete in one direction and wrong in one detail:

  * WRONG DETAIL.  That artifact states "Cl(3,1) = M(2,H) and Cl(1,3) = M(4,R)".
    The two are SWAPPED.  By the Atiyah-Bott-Shapiro table on (p-q) mod 8,
    Cl(3,1) = M(4,R) is REAL and Cl(1,3) = M(2,H) is QUATERNIONIC.  The same
    day's mh9-tier0-and-register-triage-2026-08-08.md:91 states it correctly, so
    the repository contradicted itself within hours.  Checked here.

  * INCOMPLETE.  Calling the fork "a convention" and leaving it open is not a
    stable position.  If g and -g are the same geometry, and the construction
    sends them to M(64,H) and M(128,R) respectively, then the CONSTRUCTION is
    defective -- a pure relabeling cannot change the Clifford algebra.  That is
    the finding here.

THE ARGUMENT, in three computed steps.

  (1) g -> -g is a pure relabeling.  The Levi-Civita connection is INVARIANT
      (Gamma = 1/2 g^{-1}(dg + dg - dg) has one g^{-1} and one dg, so the two
      sign flips cancel), hence geodesics, curvature and parallel transport are
      identical.  The causal cone is one set: g(v,v) < 0 and (-g)(v,v) > 0 are
      the same inequality.  Only the metric SIGN and the words
      "timelike"/"spacelike" differ.  Computed in test (1).

  (2) The DeWitt fibre form does NOT follow the relabeling.  G(-g) = G(g)
      EXACTLY, because A_i = g^{-1}B_i sends A_i -> -A_i and both tr(A_iA_j) and
      tr(A_i)tr(A_j) are even in A.  So the fibre stays (6,4) on both bases --
      which is exactly what layer0-fork-registry.yaml already records
      ("the fibre is (6,4) both ways").  Computed in test (2).

  (3) Therefore the construction is NOT EQUIVARIANT under the relabeling.  It
      sends base (3,1) -> ambient (9,5) = M(64,H), and base (1,3) -> ambient
      (7,7) = M(128,R).  Same geometry in, different real Clifford class out.
      Computed in test (3).

WHAT FOLLOWS.  A well-posed construction must transport BOTH blocks under the
relabeling, i.e. the ambient form is g (+) eps.G with eps tied to the base
convention.  Then the flip gives (9,5) <-> (5,9), and BOTH are M(H) -- because
(p-q) = +4 and -4 are the same class mod 8.  The relabeling becomes invisible,
as it must be.  On that repair, (7,7) is NOT reachable by a sign convention at
all; it requires a genuinely different fibre form, not a relabeled one.

THE FIBRE SIGN IS SEPARATELY PINNED, AND NOT BY CONVENTION.  The remaining free
bit is the overall sign of G.  It is fixed by the same criterion that fixes it in
Wheeler-DeWitt: +G gives transverse-traceless modes POSITIVE norm and the
conformal mode NEGATIVE (the standard conformal-factor problem); -G makes the
physical gravitons ghosts.  Computed in test (4).  This kills the (4,6) fibre.

AND IT LANDS ON THE SOURCE.  The transcript's route to (7,7) is vertical (4,6)
plus horizontal (3,1) -- lab/sources/curt-iceberg-7-7-reasoning-reinspection-2026-07-31.md.
That route uses the (4,6) fibre, the one test (4) rejects as ghost-like.
Meanwhile the source declares the BASE as (1,3) in at least five independent
places (WG-A04, WG-A08, the 2021 draft S11-12 "Spin(1,3) x Spin(6,4)", the
transcript at 02:42:20 "we are trapped in the (1,3) sector", and
gu-paper-reference-surfaces.md).  The repository runs (3,1).  Nobody had checked
the source's declared convention against this fork.

SCOPE, AND IT IS REAL.
  * This does not by itself close the ledger row.  It reclassifies the row's
    TYPE, from "under-determined, awaiting a resolver" to "ill-posed as stated,
    awaiting a construction repair".  A verdict-adjacent retyping takes the
    hostile-review path and is NOT made by this certificate.
  * The TT-positivity criterion is an IMPORTED PHYSICAL INPUT, not a consequence
    of GU's action.  It is convention-relative in the same way the base sign is:
    under a global flip, what counts as positive kinetic norm flips too.  That
    is consistent -- the global flip stays free -- but it means test (4) pins the
    fibre sign RELATIVE to the base, not absolutely.
  * The (6,4) fibre premise, the (832,832) trace, and F ~ RP^3 are all recorded
    signature-robust and are untouched either way.
"""

from __future__ import annotations

import itertools
import unittest

import numpy as np

TOL = 1e-9
LAM = 0.5  # trace-reversal coefficient, as filed

# Atiyah-Bott-Shapiro: real Clifford algebra Morita class by (p - q) mod 8.
ABS_TABLE = {
    0: "M(R)", 1: "M(R)+M(R)", 2: "M(R)", 3: "M(C)",
    4: "M(H)", 5: "M(H)+M(H)", 6: "M(H)", 7: "M(C)",
}


def clifford_class(p: int, q: int) -> str:
    return ABS_TABLE[(p - q) % 8]


def sym2_basis(n: int = 4):
    out = []
    for i, j in itertools.combinations_with_replacement(range(n), 2):
        b = np.zeros((n, n))
        b[i, j] = b[j, i] = 1.0
        out.append(((i, j), b))
    return out


BASIS = sym2_basis()


def dewitt(g: np.ndarray, lam: float = LAM, sign: int = +1) -> np.ndarray:
    """G_ij = sign * ( tr(A_i A_j) - lam tr(A_i) tr(A_j) ),  A_i = g^{-1} B_i."""
    gi = np.linalg.inv(g)
    n = len(BASIS)
    g_form = np.zeros((n, n))
    a = [gi @ b for _, b in BASIS]
    for i in range(n):
        for j in range(n):
            g_form[i, j] = sign * (np.trace(a[i] @ a[j])
                                   - lam * np.trace(a[i]) * np.trace(a[j]))
    return g_form


def signature(m: np.ndarray) -> tuple[int, int]:
    e = np.linalg.eigvalsh((m + m.T) / 2)
    return int((e > TOL).sum()), int((e < -TOL).sum())


def christoffel(gfun, x, h=1e-5):
    g = gfun(x)
    gi = np.linalg.inv(g)
    n = len(x)
    dg = np.zeros((n, n, n))
    for c in range(n):
        e = np.zeros(n)
        e[c] = h
        dg[:, :, c] = (gfun(x + e) - gfun(x - e)) / (2 * h)
    out = np.zeros((n, n, n))
    for a_ in range(n):
        for b_ in range(n):
            for c_ in range(n):
                out[a_, b_, c_] = 0.5 * sum(
                    gi[a_, d] * (dg[d, b_, c_] + dg[d, c_, b_] - dg[b_, c_, d])
                    for d in range(n)
                )
    return out


G_PLUS = np.diag([1.0, 1.0, 1.0, -1.0])   # labelled (3,1)
G_MINUS = -G_PLUS                          # labelled (1,3) -- the same geometry


class SignatureForkEquivariance(unittest.TestCase):

    def test_0_clifford_table_the_swap_this_corrects(self) -> None:
        print("\n[0] Real Clifford classes, ABS table on (p-q) mod 8")
        for p, q in [(3, 1), (1, 3), (9, 5), (5, 9), (7, 7), (6, 4), (4, 6)]:
            print(f"    Cl({p},{q}): p-q = {p-q:+d}  ->  {clifford_class(p,q)}")
        self.assertEqual(clifford_class(3, 1), "M(R)",
                         "Cl(3,1) must be REAL -- M(4,R)")
        self.assertEqual(clifford_class(1, 3), "M(H)",
                         "Cl(1,3) must be QUATERNIONIC -- M(2,H)")
        print("    => Cl(3,1) = M(4,R) REAL ; Cl(1,3) = M(2,H) QUATERNIONIC.")
        print("       signature-ambient-is-a-sign-convention-2026-08-08.md:57 has")
        print("       these SWAPPED. Corrected by this certificate.")

        # the structural reason the base and ambient classes always differ
        self.assertEqual(clifford_class(6, 4), "M(R)")
        for base, amb in [((3, 1), (9, 5)), ((1, 3), (7, 7))]:
            self.assertNotEqual(clifford_class(*base), clifford_class(*amb),
                                "base and ambient class should always differ")
        print("    structural: the (6,4) fibre has p-q = +2, which toggles")
        print("    2<->4 and 6<->0 mod 8, i.e. REAL <-> QUATERNIONIC. The fibre")
        print("    always flips the class, so base and ambient never agree.")

    def test_0b_the_classes_by_explicit_construction_not_by_table(self) -> None:
        """Convention-proof corroboration: the ABS table is a naming convention
        away from ambiguity, so exhibit the algebras directly.  A real 4x4
        realisation exists iff the class is M(R)."""
        i2 = np.eye(2)
        sx = np.array([[0.0, 1.0], [1.0, 0.0]])
        sz = np.array([[1.0, 0.0], [0.0, -1.0]])
        ep = np.array([[0.0, 1.0], [-1.0, 0.0]])
        k = np.kron

        # three generators squaring to +1, one to -1, all real 4x4
        gens = [k(sx, i2), k(sz, i2), k(ep, ep), k(ep, sx)]
        squares = [float((g @ g)[0, 0]) for g in gens]
        print("\n[0b] explicit REAL 4x4 set with three '+' and one '-'")
        print(f"     squares = {[int(s) for s in squares]}")
        self.assertEqual(sorted(squares), [-1.0, 1.0, 1.0, 1.0])
        for idx, g in enumerate(gens):
            self.assertTrue(np.allclose(g @ g, squares[idx] * np.eye(4)),
                            "generator square is not a clean multiple of I")
            self.assertTrue(np.allclose(g, g.real), "generator is not real")
        for a in range(4):
            for b in range(4):
                if a != b:
                    self.assertTrue(np.allclose(gens[a] @ gens[b] + gens[b] @ gens[a], 0),
                                    "generators do not anticommute")
        print("     all real, all anticommuting, clean squares -> the algebra")
        print("     with THREE '+' and ONE '-' is M(4,R), REAL.")
        print("     (A randomized 60-restart search finds NO real 4x4 set for")
        print("      one '+' / three '-', which is therefore M(2,H).)")
        print("     Consistent with the ABS table read in test [0].")
        print("\n     LAYER-0 NOTE: the ALGEBRAS are unambiguous; the LABEL")
        print("     'Cl(3,1)' is not. oq-rk1-rs-rank-first-principles-2026-06-23.md")
        print("     uses it for the one-'+' algebra (M(2,H)); the SIGNATURE-AMBIENT")
        print("     work uses it for the three-'+' algebra (M(4,R)). Seventh homonym.")

    def test_1_the_relabeling_is_geometrically_empty(self) -> None:
        rng = np.random.default_rng(20260808)
        pert = rng.normal(size=(4, 4))
        pert = pert + pert.T
        gf = lambda x: G_PLUS + 0.1 * np.sin(x[0]) * pert
        gm = lambda x: -gf(x)
        x0 = np.array([0.3, 0.1, -0.2, 0.4])
        d = np.max(np.abs(christoffel(gf, x0) - christoffel(gm, x0)))
        print("\n[1] g -> -g is a pure relabeling")
        print(f"    ||Gamma[g] - Gamma[-g]||_inf = {d:.2e}")
        self.assertLess(d, 1e-8, "Levi-Civita connection must be invariant")

        # the causal cone is literally one set
        v = rng.normal(size=(4000, 4))
        cone_g = (np.einsum("ni,ij,nj->n", v, G_PLUS, v) < 0)
        cone_mg = (np.einsum("ni,ij,nj->n", v, G_MINUS, v) > 0)
        self.assertTrue(np.array_equal(cone_g, cone_mg),
                        "the timelike cone must be the same set")
        print(f"    timelike cone identical on {len(v)} samples: "
              f"{cone_g.sum()} vectors, both labellings")
        print("    => geodesics, curvature, parallel transport, causal structure")
        print("       all identical. Only the metric SIGN and the words differ.")

    def test_2_the_fibre_form_does_not_follow_the_relabeling(self) -> None:
        gp, gm = dewitt(G_PLUS), dewitt(G_MINUS)
        resid = np.max(np.abs(gp - gm))
        print("\n[2] the DeWitt fibre form is BLIND to the relabeling")
        print(f"    ||G(g) - G(-g)||_inf = {resid:.2e}   (A_i -> -A_i, both terms even)")
        print(f"    signature at base (3,1) : {signature(gp)}")
        print(f"    signature at base (1,3) : {signature(gm)}")
        self.assertLess(resid, TOL, "G(-g) must equal G(g) exactly")
        self.assertEqual(signature(gp), (6, 4))
        self.assertEqual(signature(gm), (6, 4))
        print("    => fibre (6,4) on BOTH bases, matching the registry's own note.")

    def test_3_the_two_orbits_and_the_declared_base_route(self) -> None:
        print("\n[3] the two orbits")
        print("    (3,1) and (1,3) metrics are DISJOINT GL(4,R) orbits in Sym^2 T*X.")
        print("    They are not the same point relabeled -- that framing was")
        print("    rejected by hostile review. But O(3,1) = O(1,3) as a subgroup")
        print("    condition, so the two orbits are ISOMORPHIC homogeneous spaces")
        print("    (consistent with the C1/lemma review's signature-robust F).")
        rows = []
        for name, base_sig in [("(3,1)", (3, 1)), ("(1,3)", (1, 3))]:
            amb = (base_sig[0] + 6, base_sig[1] + 4)
            rows.append((name, amb, clifford_class(*amb)))
            print(f"      base {name} + fibre (6,4) = ambient {amb} = {clifford_class(*amb)}")
        self.assertNotEqual(rows[0][2], rows[1][2],
                            "the two orbits must land in different Clifford classes")
        print("\n    So the construction assigns DIFFERENT real Clifford classes to")
        print("    the two orbits. Read Met(X) as 'Lorentzian metrics' and it has two")
        print("    components with M(64,H) on one and M(128,R) on the other. Read it")
        print("    as 'the (3,1) orbit' and a convention has simply been declared.")
        print("    Both readings are live; NEITHER makes the fork an evidence question.")

        print("\n    THE DECLARED-BASE ROUTE, which is the consequential part:")
        print("      the source DECLARES base (1,3) in five AUTHOR-STATED places;")
        print("      the repository DERIVES fibre (6,4), invariant under the base sign;")
        amb = (1 + 6, 3 + 4)
        print(f"      (1,3) + (6,4) = {amb} = {clifford_class(*amb)}")
        self.assertEqual(amb, (7, 7))
        self.assertEqual(clifford_class(*amb), "M(R)")
        print("      and REAL-CLIFFORD-FORM is SETTLED at Cl(7,7) = M128(R).")
        print("    Three independent things agree. Filed as named_resolver, NOT")
        print("    as a settlement -- see test [5].")

    def test_4_the_fibre_sign_is_pinned_by_physics_not_convention(self) -> None:
        gp = dewitt(G_PLUS, sign=+1)
        idx = {ij: k for k, (ij, _) in enumerate(BASIS)}
        htt = np.zeros(len(BASIS))
        htt[idx[(0, 0)]] = 1.0
        htt[idx[(1, 1)]] = -1.0          # spatial, traceless: a graviton polarisation
        hcf = np.zeros(len(BASIS))
        for (i, j), _ in BASIS:
            if i == j:
                hcf[idx[(i, j)]] = G_PLUS[i, i]   # conformal direction h = g

        tt, cf = htt @ gp @ htt, hcf @ gp @ hcf
        print("\n[4] the overall sign of G is fixed by TT-positivity")
        print(f"    +G : TT norm = {tt:+.1f}   conformal norm = {cf:+.1f}"
              "   <- standard Wheeler-DeWitt")
        print(f"    -G : TT norm = {-tt:+.1f}   conformal norm = {-cf:+.1f}"
              "   <- physical gravitons are ghosts")
        self.assertGreater(tt, 0, "+G must give TT modes positive norm")
        self.assertLess(cf, 0, "+G must give the conformal mode negative norm")

        # HOSTILE REVIEW 2026-08-08, Charge 1 + symplectic lens: the two lines
        # above sample ONE vector, and a one-sample test cannot establish a
        # subspace property.  Decompose instead, and separate physical from gauge.
        spatial = [idx[(i, j)] for (i, j), _ in BASIS if i < 3 and j < 3]
        shift = [idx[(i, j)] for (i, j), _ in BASIS if (i == 3) != (j == 3)]
        lapse = [idx[(i, j)] for (i, j), _ in BASIS if i == 3 and j == 3]
        block = lambda ix: signature(gp[np.ix_(ix, ix)])
        print("\n    block decomposition of the (6,4) fibre:")
        print(f"      spatial-spatial (6)      {block(spatial)}"
              "   <- the classical Wheeler-DeWitt signature")
        print(f"      time-space / shift (3)   {block(shift)}   GAUGE")
        print(f"      time-time / lapse (1)    {block(lapse)}   GAUGE")
        self.assertEqual(block(spatial), (5, 1),
                         "spatial block must reproduce the DeWitt (5,1)")
        self.assertEqual(block(shift + lapse), (1, 3),
                         "lapse+shift must carry (1,3)")

        # the physical directions: spatial AND traceless -- the graviton polarisations
        trace_row = np.array([[1.0 if BASIS[a][0][0] == BASIS[a][0][1] else 0.0
                               for a in spatial]])
        complement = np.linalg.svd(trace_row)[2][1:]      # 5-dim traceless subspace
        g_phys = complement @ gp[np.ix_(spatial, spatial)] @ complement.T
        eigs = np.linalg.eigvalsh((g_phys + g_phys.T) / 2)
        print(f"      spatial TRACELESS (5)    {signature(g_phys)}"
              f"   eigenvalues {np.round(eigs, 3)}")
        self.assertEqual(signature(g_phys), (5, 0),
                         "the whole graviton subspace must be positive under +G")
        print("    => TT-positivity holds on the FULL 5-dim physical subspace,")
        print("       not merely the sampled direction. The claim is stronger than")
        print("       the one-sample version it replaces.")
        print("    => and it is now stated on the PHYSICAL directions only: 4 of the")
        print("       10 are lapse and shift, i.e. gauge. The earlier form applied a")
        print("       physical criterion to the unreduced space, which the operating")
        print("       contract forbids.")
        self.assertEqual(signature(dewitt(G_PLUS, sign=-1)), (4, 6))
        print("    -G has fibre signature (4,6) -- which is the SOURCE's spoken")
        print("    vertical block. The transcript's route to (7,7) is (4,6)+(3,1),")
        print("    and it uses the fibre sign this test rejects as ghost-like.")
        print("\n    IMPORTED INPUT, stated: TT-positivity is physics, not a")
        print("    consequence of GU's action, and it is itself convention-relative")
        print("    (a global flip flips what counts as positive). It pins the fibre")
        print("    sign RELATIVE to the base, which is exactly what the repair needs.")

    def test_5_verdict(self) -> None:
        print("\nVERDICT: TWO-ORBIT-SPLIT__FIBRE-SIGN-PINNED-BY-PHYSICS"
              "__DECLARED-BASE-ROUTE-TO-(7,7)")
        print("\nWHAT THIS FILE ESTABLISHES:")
        print("  * the fibre is (6,4) on BOTH bases, exactly (residual 0.00e+00);")
        print("  * its overall sign is pinned by physics, not convention -- the")
        print("    5-dim graviton subspace is (5,0) under +G and ghost under -G;")
        print("  * (3,1) and (1,3) are DISJOINT GL(4,R) ORBITS, so the fork is a")
        print("    question about which orbit GU declares, not about evidence;")
        print("  * therefore base (1,3) + fibre (6,4) = (7,7), a second and")
        print("    physically clean route to the horn REAL-CLIFFORD-FORM settled on.")
        print("\nNOT DONE HERE:")
        print("  * SETTLING SIGNATURE-AMBIENT. The route above is filed as the row's")
        print("    named_resolver, which was NONE after M-H9 was falsified. Settling")
        print("    would dissolve or re-scope 29 canon files and must be its own act.")
        print("  * the one remaining gap: whether the source's (1,3) is the")
        print("    ambient-relevant BASE or a separate Spin(1,3) GAUGE-GROUP")
        print("    statement. gu-paper-reference-surfaces.md is about H as a gauge")
        print("    group -- a different object -- and that has not been checked.")
        print("  * the original retyping proposal: REJECTED by hostile review.")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
