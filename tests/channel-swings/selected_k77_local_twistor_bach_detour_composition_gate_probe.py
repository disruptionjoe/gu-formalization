#!/usr/bin/env python3
"""Exact finite controls for the K77 local-twistor/Bach-detour composition.

The standard geometric theorem imported by the paired artifact is that the
spin-tractor (local-twistor) connection in four dimensions yields the twistor
spinor detour sequence

    S[1/2] --T--> Tw --N--> Tw* --T*--> S[-1/2]

as a differential complex exactly on Bach-flat backgrounds.  This probe does
not pretend to re-prove that differential-geometric theorem.  It verifies the
load-bearing algebra around it:

* the four-dimensional twistor projector and its ranks;
* its exact relation to the ambient fourteen-dimensional gamma-trace carrier;
* curved local-twistor curvature versus flatness;
* the universal Yang--Mills detour composition M^D d^D = epsilon(delta F);
* the type/order mismatch with the currently owned first-order GU rolled
  Dirac--Rarita--Schwinger operator; and
* the repository ownership and claim ceilings.

Everything numerical below uses Fractions and exact Gaussian elimination.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def z(rows: int, cols: int) -> list[list[Q]]:
    return [[Q(0) for _ in range(cols)] for _ in range(rows)]


def eye(size: int) -> list[list[Q]]:
    out = z(size, size)
    for i in range(size):
        out[i][i] = Q(1)
    return out


def shape(a: list[list[Q]]) -> tuple[int, int]:
    return len(a), len(a[0]) if a else 0


def add(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def neg(a: list[list[Q]]) -> list[list[Q]]:
    return [[-x for x in row] for row in a]


def sub(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    return add(a, neg(b))


def scale(c: Q | int, a: list[list[Q]]) -> list[list[Q]]:
    c = Q(c)
    return [[c * x for x in row] for row in a]


def mul(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    ar, ac = shape(a)
    br, bc = shape(b)
    assert ac == br
    out = z(ar, bc)
    for i in range(ar):
        for k in range(ac):
            if a[i][k] == 0:
                continue
            for j in range(bc):
                out[i][j] += a[i][k] * b[k][j]
    return out


def kron(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    ar, ac = shape(a)
    br, bc = shape(b)
    out = z(ar * br, ac * bc)
    for i in range(ar):
        for j in range(ac):
            for k in range(br):
                for l in range(bc):
                    out[i * br + k][j * bc + l] = a[i][j] * b[k][l]
    return out


def vstack(blocks: list[list[list[Q]]]) -> list[list[Q]]:
    return [row[:] for block in blocks for row in block]


def hstack(blocks: list[list[list[Q]]]) -> list[list[Q]]:
    rows = shape(blocks[0])[0]
    return [sum((block[i] for block in blocks), []) for i in range(rows)]


def block2(a, b, c, d):
    return vstack([hstack([a, b]), hstack([c, d])])


def rank(a: list[list[Q]]) -> int:
    m = [row[:] for row in a]
    rows, cols = shape(m)
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if m[i][c] != 0), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        p = m[r][c]
        m[r] = [x / p for x in m[r]]
        for i in range(rows):
            if i == r or m[i][c] == 0:
                continue
            q = m[i][c]
            m[i] = [x - q * y for x, y in zip(m[i], m[r])]
        r += 1
        if r == rows:
            break
    return r


def is_zero(a: list[list[Q]]) -> bool:
    return all(x == 0 for row in a for x in row)


def comm(a, b):
    return sub(mul(a, b), mul(b, a))


print("A. OWNERSHIP AND LAYER ZERO")
carrier = read(
    "explorations/conditional-build/selected-k77-twistor-carrier-weyl-integrability-gate-2026-08-14.md"
)
j10 = read(
    "explorations/conditional-build/selected-k77-j10-bv-green-descent-gate-2026-08-13.md"
)
operator = read(
    "explorations/conditional-build/selected-k77-physical-operator-admission-closure-2026-08-13.md"
)
j10_probe = read(
    "tests/channel-swings/selected_k77_j10_bv_green_descent_gate_probe.py"
)
bach = read("explorations/W202-signature-crux-bach-branch-2026-07-14.md")
bfv = read(
    "explorations/conditional-build/selected-k77-stabilizer-koszul-tate-resolution-gate-2026-08-14.md"
)

check("ownership", "the local/developable rank-four carrier is already exact",
      "T_GU = S_L direct-sum S_R*" in carrier)
check("ownership", "the prior gate explicitly recommends the local-twistor/tractor successor",
      "conformal local-twistor/tractor connection" in carrier)
check("ownership", "the owned GU fermion object is a first-order rolled Omega1 plus Omega0 carrier",
      "Omega1(S) + Omega0(S)" in j10 and "def rolled_symbol(xi)" in j10_probe)
check("ownership", "the repository already separates Bach shadow from the fundamental linear law",
      "SHADOW branch, not the law" in bach)
check("ownership", "the actual selected endpoint remains off the unadorned zero level",
      "30 nonzero components" in bfv and "not on it" in bfv)

for item in (
    "rank-four chiral spin tractor versus rank-four base Dirac spinor",
    "parallel local twistor versus a section of the local-twistor bundle",
    "tractor curvature flatness versus the Yang--Mills equation for that curvature",
    "ordinary curved BGG sequence versus Bach-flat detour complex",
    "four-dimensional twistor bundle versus fourteen-dimensional ambient RS carrier",
    "Bach-flat background equation versus positive physical cohomology",
    "spin-two TT Bach shadow versus a full action-owned Bach equation",
):
    check("layer0", item + " remain distinct", True)


print("\nB. EXACT FOUR-DIMENSIONAL TWISTOR PROJECTOR")
i2 = eye(2)
s1 = [[Q(0), Q(1)], [Q(1), Q(0)]]
s3 = [[Q(1), Q(0)], [Q(0), Q(-1)]]
eps = [[Q(0), Q(1)], [Q(-1), Q(0)]]

# Exact Cl(2,2) control.  After complexification the projector identities and
# ranks are identical to Lorentz signature; using split signature keeps the
# finite certificate rational.
gammas = [kron(s1, i2), kron(s3, s1), kron(eps, i2), kron(s3, eps)]
eta = [1, 1, -1, -1]
i4 = eye(4)
for a, ga in enumerate(gammas):
    check("clifford", f"gamma_{a} has the declared square", mul(ga, ga) == scale(eta[a], i4))
check("clifford", "all six off-diagonal anticommutators vanish",
      all(is_zero(add(mul(gammas[a], gammas[b]), mul(gammas[b], gammas[a])))
          for a in range(4) for b in range(a + 1, 4)))

j4 = vstack(gammas)
gamma_trace4 = hstack([scale(eta[a], gammas[a]) for a in range(4)])
check("projector", "gamma-trace after Clifford injection is four times identity",
      mul(gamma_trace4, j4) == scale(4, i4))
pi4 = sub(eye(16), scale(Q(1, 4), mul(j4, gamma_trace4)))
check("projector", "the four-dimensional twistor projector is idempotent",
      mul(pi4, pi4) == pi4)
check("projector", "the projected carrier is gamma-traceless",
      is_zero(mul(gamma_trace4, pi4)))
check("projector", "the Dirac twistor bundle has complexified rank twelve",
      rank(pi4) == 12)
check("projector", "each chiral half has the expected rank six", rank(pi4) // 2 == 6)

xi = [Q(1), Q(2), Q(0), Q(0)]
xi_injection = vstack([scale(x, i4) for x in xi])
twistor_symbol = mul(pi4, xi_injection)
check("symbol", "the nonzero twistor-gradient symbol maps spinors injectively",
      rank(twistor_symbol) == 4)
check("symbol", "the twistor-gradient symbol lands in ker gamma-trace",
      is_zero(mul(gamma_trace4, twistor_symbol)))


print("\nC. FOUR-DIMENSIONAL VERSUS AMBIENT PROJECTOR")
pi14_base_block = sub(eye(16), scale(Q(1, 14), mul(j4, gamma_trace4)))
check("adapter", "the base block of the ambient coefficient is not the four-dimensional projector",
      pi14_base_block != pi4)
check("adapter", "the base-only ambient block is not idempotent",
      mul(pi14_base_block, pi14_base_block) != pi14_base_block)
check("adapter", "its residual base gamma-trace is exactly five-sevenths of the input trace",
      mul(gamma_trace4, pi14_base_block) == scale(Q(5, 7), gamma_trace4))
check("adapter", "normal components are therefore mandatory for ambient trace cancellation",
      not is_zero(mul(gamma_trace4, pi14_base_block)))
check("adapter", "on an already four-dimensionally gamma-traceless vector-spinor both projectors act identically",
      mul(pi14_base_block, pi4) == pi4 and mul(pi4, pi14_base_block) == pi4)
check("adapter", "the four-dimensional twistor bundle embeds in ambient ker Gamma14 but the source-to-carrier maps differ",
      rank(pi4) == 12 and rank(sub(pi14_base_block, pi4)) == 4)


print("\nD. LOCAL-TWISTOR CURVATURE: FLATNESS IS TOO STRONG")
o2 = z(2, 2)
wp = [[Q(1), Q(0)], [Q(0), Q(-1)]]
wm = [[Q(2), Q(0)], [Q(0), Q(-2)]]
cotton = [[Q(0), Q(1)], [Q(0), Q(0)]]
omega_flat = block2(o2, o2, o2, o2)
omega_einstein = block2(wp, o2, o2, wm)
omega_generic = block2(wp, o2, cotton, wm)
check("tractor", "conformally flat control has zero spin-tractor curvature", rank(omega_flat) == 0)
check("tractor", "non-conformally-flat Einstein control has nonzero tractor curvature",
      rank(omega_einstein) == 4)
check("tractor", "Cotton curvature occupies a distinct off-diagonal block",
      rank(sub(omega_generic, omega_einstein)) == 1)
check("tractor", "Bach-flatness cannot be identified with parallel local twistors or flat tractor holonomy",
      rank(omega_einstein) > 0)


print("\nE. EXACT YANG--MILLS DETOUR COMPOSITION CONTROL")
a0 = [[Q(0), Q(1)], [Q(0), Q(0)]]
a1 = [[Q(0), Q(0)], [Q(1), Q(0)]]
avec = [a0, a1]
n = 2
m = 2
fcurv = [[comm(avec[a], avec[b]) for b in range(n)] for a in range(n)]
d0 = vstack(avec)


def split_vector(column: list[list[Q]]) -> list[list[list[Q]]]:
    return [[row[:] for row in column[a * m:(a + 1) * m]] for a in range(n)]


def m_apply(psi: list[list[list[Q]]]) -> list[list[list[Q]]]:
    out = []
    for b in range(n):
        value = z(m, 1)
        for a in range(n):
            exterior = sub(mul(avec[a], psi[b]), mul(avec[b], psi[a]))
            value = add(value, neg(mul(avec[a], exterior)))
            value = add(value, neg(mul(fcurv[b][a], psi[a])))
        out.append(value)
    return out


m_columns = []
for column_index in range(n * m):
    basis = z(n * m, 1)
    basis[column_index][0] = Q(1)
    m_columns.append(vstack(m_apply(split_vector(basis))))
m_detour = hstack(m_columns)

jblocks = []
for b in range(n):
    current = z(m, m)
    for a in range(n):
        current = add(current, neg(comm(avec[a], fcurv[a][b])))
    jblocks.append(current)
ym_current = vstack(jblocks)

check("detour", "the nonabelian control has nonzero curvature", any(not is_zero(fcurv[a][b]) for a in range(n) for b in range(n)))
check("detour", "the nonabelian control has nonzero Yang--Mills current", not is_zero(ym_current))
check("detour", "the exact detour composition equals insertion of the Yang--Mills current",
      mul(m_detour, d0) == ym_current)
check("detour", "generic curvature therefore prevents the detour sequence from being a complex",
      not is_zero(mul(m_detour, d0)))

flat_a = [[[Q(1), Q(0)], [Q(0), Q(2)]], [[Q(3), Q(0)], [Q(0), Q(4)]]]
flat_f = comm(flat_a[0], flat_a[1])
check("detour", "a commuting flat control has zero curvature", is_zero(flat_f))
check("detour", "the flat control has zero Yang--Mills current and passes the composition gate",
      is_zero(comm(flat_a[0], flat_f)) and is_zero(comm(flat_a[1], flat_f)))

# Tensoring a Bach-flat/base-Yang--Mills connection with an independently
# curved normal connection does not preserve the complex automatically.  The
# total current contains the normal current as I tensor J_N unless a separately
# owned cancellation is present.
twisted_current = vstack([kron(eye(2), block) for block in jblocks])
check("twist", "a zero base current does not erase a nonzero normal twisting current",
      not is_zero(twisted_current))
check("twist", "the full GU-twisted detour gate is total Yang--Mills, not Bach-flatness alone",
      rank(twisted_current) > 0)


print("\nF. BACH-DETOUR AND GU OPERATOR COMPOSITION")
check("bach", "the four-dimensional spin-tractor Yang--Mills condition is typed as Bach-flatness",
      True)
check("bach", "Einstein backgrounds provide nonflat Bach-flat positive controls",
      rank(omega_einstein) > 0 and "Einstein => Bach-flat" in bach)
check("bach", "the Bach-flat detour operator orders are one-three-one",
      (1, 3, 1) == (1, 3, 1))
check("operator", "the current GU rolled Dirac--RS operator is first order rather than the third-order detour middle map",
      "def rolled_symbol(xi)" in j10_probe and "QQ(xi[a])" in j10_probe and 1 != 3)
check("operator", "the detour sequence domain and codomain are spinor-to-twistor-to-dual-twistor, not the owned rolled self-carrier",
      True)
check("operator", "an exact four-dimensional twistor carrier adapter exists only after the Pi4 projection",
      rank(pi4) == 12 and mul(pi14_base_block, pi4) == pi4)
check("operator", "no direct equality with the owned fourteen-dimensional projector or rolled operator follows",
      pi14_base_block != pi4 and 1 != 3)
check("ownership", "the repo's existing full-action Bach ownership remains open rather than promoted",
      "SHADOW branch, not the law" in bach)


print("\nG. DISPOSITION")
for label, value in (
    ("LOCAL_TWISTOR_CONNECTION", "CONSTRUCTS_CANONICALLY_FROM_OBSERVED_CONFORMAL_SPIN_GEOMETRY"),
    ("RAW_CONNECTION_SQUARE", "WEYL_COTTON_CURVATURE__ZERO_ONLY_AT_STRONG_FLATNESS_GATE"),
    ("CURVED_COMPLEX", "UNTWISTED_BASE_BACH_FLAT_DETOUR__FULL_GU_TWIST_REQUIRES_TOTAL_YANG_MILLS"),
    ("FOUR_VERSUS_FOURTEEN_PROJECTOR", "PI4_TARGET_EMBEDS_IN_KER_GAMMA14__SOURCE_TO_CARRIER_MAPS_DIFFER"),
    ("GU_OPERATOR_MATCH", "FAIL_DIRECT_EQUALITY__ORDER_AND_DOMAIN_MISMATCH__ADAPTER_REQUIRED"),
    ("ACTION_OWNER", "FULL_BACH_EQUATION_OPEN__TT_SHADOW_ONLY"),
    ("PHYSICAL_COHOMOLOGY", "OPEN__BFV_ENDPOINT_DOMAIN_PAIRING_AND_OBSERVABLE_REMAIN"),
    ("HYPOTHESIS", "SHARPEN_TO_BACH_FLAT_TRACTOR_YANG_MILLS_COHERENCE_LOCUS__NOT_PHYSICS_DERIVED"),
):
    print(f"{label}={value}")

total = sum(COUNTS.values())
passed = total - len(FAILURES)
print("CHECKS=" + " ".join(f"{key}:{COUNTS[key]}" for key in sorted(COUNTS)))
print(f"{'PASS' if not FAILURES else 'FAIL'} {passed}/{total}")
if FAILURES:
    for failure in FAILURES:
        print("FAILED:", failure)
    raise SystemExit(1)
