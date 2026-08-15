#!/usr/bin/env python3
"""H2 corrected: does antilinear conjugation FLIP or PRESERVE chirality?
Bug in v1: used omega = g0g1g2g3 (omega^2 = -I in (1,3)), which is NOT the
chirality operator. Correct: gamma5 normalized so gamma5^2 = +I. The omitted
factor of i is exactly where the signature dependence enters."""
import itertools
def mm(A,B):
    n=len(A); return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]
def smul(c,A): return [[c*x for x in r] for r in A]
def conj(A): return [[x.conjugate() for x in r] for r in A]
def eye(n): return [[1 if i==j else 0 for j in range(n)] for i in range(n)]
def eq(A,B): return all(A[i][j]==B[i][j] for i in range(len(A)) for j in range(len(A)))
def kron(A,B):
    na,nb=len(A),len(B)
    return [[A[i//nb][j//nb]*B[i%nb][j%nb] for j in range(na*nb)] for i in range(na*nb)]
I2=eye(2); X=[[0,1],[1,0]]; Y=[[0,-1j],[1j,0]]; Z=[[1,0],[0,-1]]; eps=[[0,1],[-1,0]]

LOR=[kron(Z,I2), kron(eps,X), kron(eps,Y), kron(eps,Z)]          # (1,3)
EUC=[kron(X,I2), kron(Y,I2), kron(Z,X), kron(Z,Y)]               # (4,0)

def gamma5(G, sig):
    n=len(G[0]); w=eye(n)
    for g in G: w=mm(w,g)
    for ph in (1,1j,-1,-1j):
        c=smul(ph,w)
        if eq(mm(c,c),eye(n)): return c,ph
    return None,None

def analyse(G,name,expect_norm=None,expect_verdicts=None,checks=None):
    print(f"\n=== {name}")
    g5,ph=gamma5(G,name)
    print(f"  gamma5 = ({ph})*g0g1g2g3, gamma5^2 = +I  [normalisation {'REAL' if ph in (1,-1) else 'IMAGINARY'}]")
    print(f"  conj(gamma5) == gamma5 ? {eq(conj(g5),g5)}   conj(gamma5) == -gamma5 ? {eq(conj(g5),smul(-1,g5))}")
    n=len(G[0]); found=[]
    for r in range(len(G)+1):
        for combo in itertools.combinations(range(len(G)),r):
            M=eye(n)
            for i in combo: M=mm(M,G[i])
            for c_ph in (1,1j):
                C=smul(c_ph,M)
                for flip in (1,-1):
                    if all(eq(mm(C,conj(g)), smul(flip,mm(g,C))) for g in G):
                        # antilinear map psi -> C conj(psi); action on chirality:
                        lhs=mm(C,conj(g5)); rhs=mm(g5,C)
                        pres=eq(lhs,rhs); flips=eq(lhs,smul(-1,rhs))
                        found.append((combo,c_ph,flip,'PRESERVES' if pres else ('FLIPS' if flips else '?')))
    seen=set()
    for combo,c_ph,flip,verdict in found:
        k=(verdict,flip)
        if k in seen: continue
        seen.add(k)
        print(f"  C=phase({c_ph})*gamma{combo}, C conj(g)={flip:+d} g C  ->  chirality {verdict}")
    verdicts={v for _,_,_,v in found}
    print(f"  SUMMARY: verdicts present = {sorted(verdicts)}")

    # ---- FAILURE PATH (added 2026-08-15).
    # This probe printed its result and asserted NOTHING, so it could not fail:
    # certificate_shape_audit correctly flagged it as an unconditional PASS.
    # It backs a live claim (explorations/signature-chirality-conjugation-
    # check-2026-08-13.md), so every conclusion resting on it was uncertified.
    # The assertions below encode THAT ARTIFACT'S published table, not whatever
    # this code happens to print today.
    ck = checks if checks is not None else []
    def req(cond, label):
        ck.append(label)
        if not cond:
            raise AssertionError(f"{name}: {label}")

    # The most dangerous missing check: with `found` empty this function
    # printed "verdicts present = []" and returned happily.  An empty search is
    # not agreement, it is a vacuous pass.
    req(len(found) > 0, "at least one admissible conjugation exists")
    req(g5 is not None, "gamma5 normalisation exists with gamma5^2 = +I")
    req(eq(mm(g5, g5), eye(len(G[0]))), "gamma5^2 == +I verified, not assumed")
    req("?" not in verdicts, "every admissible conjugation is classified (no '?')")
    # Exactness: every entry is a Gaussian integer with unit-or-zero parts, so
    # the complex arithmetic above is exact and the equality tests are not
    # float comparisons in disguise.
    req(all(x.real in (-1.0, 0.0, 1.0) and x.imag in (-1.0, 0.0, 1.0)
            for row in g5 for x in (complex(v) for v in row)),
        "gamma5 entries are exact Gaussian units -- no load-bearing float")
    if expect_norm is not None:
        got = "REAL" if ph in (1, -1) else "IMAGINARY"
        req(got == expect_norm, f"gamma5 normalisation is {expect_norm} (got {got})")
    if expect_verdicts is not None:
        req(verdicts == expect_verdicts,
            f"verdict set is {sorted(expect_verdicts)} (got {sorted(verdicts)})")
    return ck


def main(lor=LOR, euc=EUC, expect=("IMAGINARY", {"FLIPS"}, "REAL", {"PRESERVES"})):
    checks = []
    analyse(lor, "Cl(1,3) Lorentzian", expect[0], expect[1], checks)
    analyse(euc, "Cl(4,0) Euclidean", expect[2], expect[3], checks)
    # Cross-signature check: the whole point of the artifact is that the two
    # signatures DISAGREE.  Asserting each table separately would still pass if
    # some future edit made both signatures identical.
    checks.append("the two signatures give opposite verdicts")
    assert expect[1] != expect[3], "signatures must disagree"
    print(f"\nsignature_chirality_conjugation_probe: {len(checks)}/{len(checks)} checks pass")
    return checks


def selftest():
    """Planted mutations.  Each must raise; a mutation that passes means the
    corresponding assertion is vacuous."""
    ok = True
    muts = [
        ("swapped-signatures", lambda: main(EUC, LOR)),
        ("wrong-lor-norm", lambda: main(expect=("REAL", {"FLIPS"}, "REAL", {"PRESERVES"}))),
        ("wrong-lor-verdict", lambda: main(expect=("IMAGINARY", {"PRESERVES"}, "REAL", {"PRESERVES"}))),
        ("wrong-euc-verdict", lambda: main(expect=("IMAGINARY", {"FLIPS"}, "REAL", {"FLIPS"}))),
        ("empty-generators", lambda: main([], [])),
    ]
    for label, fn in muts:
        try:
            fn()
            print(f"  mutation {label:20} DID NOT FAIL  <-- vacuous assertion")
            ok = False
        except Exception as exc:
            # Print the exception TYPE.  A bare "it raised" would score a typo
            # in the mutation itself as a healthy failure path.
            print(f"  mutation {label:20} raised {type(exc).__name__}  OK")
    print("FAILURE-PATH SELFTEST: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    import sys
    sys.exit(selftest() if "--selftest" in sys.argv else (main() and 0))
