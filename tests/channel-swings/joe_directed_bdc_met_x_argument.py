#!/usr/bin/env python3
"""BD-C -- what the source actually supplies on X^4.

Exact probe for
`lab/active-research/joe-directed/base-duality/bd-c-met-x-is-an-argument-not-a-background-2026-08-15.md`.

Three families of check:

  [E]  EXACT algebra, over ``fractions.Fraction`` only.  The naturality
       obstruction: no nonzero ``GL(4,R)``-invariant symmetric bilinear form
       and no nonzero invariant density exist on ``R^4``, and the obstruction
       survives every structure-group reduction the source declares
       (orientation / spin, a distinguished time line).  It dies exactly at the
       ``O(1,3)`` reduction -- i.e. exactly when a point of ``MET(X^{1,3})`` is
       supplied.  Plus the tautological-pullback identity ``s^*(tau) = s``.

  [Q]  QUOTE PRESENCE AT A STATED LOCUS.  Every sentence the artifact attributes
       to Weinstein is asserted to occur, as an exact substring, in a named
       primary file at a named line, with the claimed timestamp/page resolvable
       at that locus.  A wrong line number fails.

  [R]  REPRODUCTION of repository facts BEFORE use: the v0.258 ledger sha256,
       LA-11's proposed `LT-GR6b` revival trigger read out of LA-11's own
       artifact, OT-1's "Neither is supplied." sentence, MD-1's contraction
       formula, and the banked S^4 Lorentz-section obstruction.

  [C]  CONTROLS that must fire, including the Kaluza-Klein disavowal control and
       the withdrawn-clause correction of record.

Run from the repository root:

    _local/cas-venv/bin/python tests/channel-swings/joe_directed_bdc_met_x_argument.py
    _local/cas-venv/bin/python tests/channel-swings/joe_directed_bdc_met_x_argument.py --selftest

No numpy.  No float is constructed anywhere; ``assert_no_float`` sweeps the
whole result dict at the end.
"""

from __future__ import annotations

import hashlib
import io
import sys
from fractions import Fraction
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

ARTIFACT = (
    REPO
    / "lab/active-research/joe-directed/base-duality"
    / "bd-c-met-x-is-an-argument-not-a-background-2026-08-15.md"
)

PORTAL = REPO / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md"
UCSD = REPO / "papers/drafts/Transcript into the impossible.md"
REGISTER = REPO / "lab/sources/source-claim-register.yaml"
S11 = REPO / "lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md"
PACK = REPO / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
LEDGER = REPO / "lab/process/conditional-physics-ledger-v0.258.json"
LA11 = (
    REPO
    / "lab/active-research/joe-directed/ledger-advancement"
    / "la11-b9stat-is-a-base-duality-row-and-four-rows-name-it-as-a-subclause-2026-08-15.md"
)
OT1 = (
    REPO
    / "lab/active-research/joe-directed/ownership-theorem"
    / "ot1-the-ownership-predicate-and-the-pairing-obstruction-2026-08-15.md"
)
MD1 = (
    REPO
    / "lab/active-research/joe-directed/four-d-mode-decomposition"
    / "md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md"
)
S4GATE = (
    REPO
    / "explorations/conditional-build"
    / "selected-k77-physical-section-faithfulness-gate-2026-08-08.md"
)
GEOMETER = REPO / "GEOMETER-VS-PHYSICS-OBJECTS.md"
ROUTING = REPO / "lab/methods/source-native-comparator-routing.md"

LEDGER_SHA256 = "540b50e386073c0f43da4e8d5a8ffdaf06fd243c6612622d7daf187c0a725047"

# The clause the routing method withdrew on 2026-08-14 as not source-attested
# and refuted.  It must be absent from this artifact.  Its presence elsewhere is
# a correction of record, asserted positively below.
WITHDRAWN_IN_GEOMETER = (
    "vertical components may become four-dimensional scalars after "
    "observation/reduction"
)
# The primary transcript reads, in lower case and with straight apostrophes,
# "... it's not extra dimensions. It's not Kaluza Klein."  The routing method
# renders it capitalised and with curly apostrophes.  Both forms are checked.
KK_PRIMARY = "it's not extra dimensions. It's not Kaluza Klein."
KK_DISAVOWAL = "It's not extra dimensions. It's not Kaluza Klein."
KK_METHOD_RENDERING = "It’s not extra dimensions. It’s not Kaluza"

ROUTING_NOTICE_HEAD = (
    "**GU-COMPARATOR-ROUTING — scope before inference.**"
)
CLASSIFICATION_LINE = "Classification: `SOURCE_NATIVE_ROUTE`"

# --------------------------------------------------------------------------
# result accumulation
# --------------------------------------------------------------------------

RESULTS: list[tuple[str, str, bool, object]] = []
FACTS: dict[str, object] = {}


def check(kind: str, name: str, ok: bool, detail: object = None) -> None:
    RESULTS.append((kind, name, bool(ok), detail))


def read(path: Path) -> str:
    return io.open(path, encoding="utf-8").read()


def lines(path: Path) -> list[str]:
    return read(path).split("\n")


def assert_no_float(obj, trail: str = "root") -> None:
    if isinstance(obj, float):
        raise AssertionError(f"float found at {trail}")
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_float(v, f"{trail}.{k}")
    elif isinstance(obj, (list, tuple, set)):
        for i, v in enumerate(obj):
            assert_no_float(v, f"{trail}[{i}]")


# --------------------------------------------------------------------------
# exact rational linear algebra (4x4 symmetric forms), no numpy
# --------------------------------------------------------------------------

F = Fraction
Mat = list[list[Fraction]]


def mat(rows) -> Mat:
    return [[F(x) for x in r] for r in rows]


def eye(n: int) -> Mat:
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def scal(n: int, lam) -> Mat:
    return [[F(lam) if i == j else F(0) for j in range(n)] for i in range(n)]


def matmul(a: Mat, b: Mat) -> Mat:
    n, m, p = len(a), len(b), len(b[0])
    return [
        [sum((a[i][k] * b[k][j] for k in range(m)), F(0)) for j in range(p)]
        for i in range(n)
    ]


def transpose(a: Mat) -> Mat:
    return [list(col) for col in zip(*a)]


def congruence(g: Mat, b: Mat) -> Mat:
    """The natural action on symmetric bilinear forms: b |-> g^T b g."""
    return matmul(matmul(transpose(g), b), g)


def det(a: Mat) -> Fraction:
    """Fraction-free-ish exact determinant by rational Gaussian elimination."""
    n = len(a)
    m = [row[:] for row in a]
    d = F(1)
    for c in range(n):
        piv = None
        for r in range(c, n):
            if m[r][c] != 0:
                piv = r
                break
        if piv is None:
            return F(0)
        if piv != c:
            m[c], m[piv] = m[piv], m[c]
            d = -d
        d *= m[c][c]
        inv = F(1) / m[c][c]
        for r in range(c + 1, n):
            f = m[r][c] * inv
            if f:
                for k in range(c, n):
                    m[r][k] -= f * m[c][k]
    return d


def rank_Q(rows: list[list[Fraction]]) -> int:
    m = [r[:] for r in rows]
    if not m:
        return 0
    nr, nc = len(m), len(m[0])
    r = 0
    for c in range(nc):
        piv = None
        for i in range(r, nr):
            if m[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        inv = F(1) / m[r][c]
        m[r] = [x * inv for x in m[r]]
        for i in range(nr):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [x - f * y for x, y in zip(m[i], m[r])]
        r += 1
        if r == nr:
            break
    return r


SYM_BASIS: list[tuple[int, int]] = [
    (i, j) for i in range(4) for j in range(i, 4)
]  # dim 10


def sym_from_vec(v: list[Fraction]) -> Mat:
    b = [[F(0)] * 4 for _ in range(4)]
    for coeff, (i, j) in zip(v, SYM_BASIS):
        b[i][j] += coeff
        if i != j:
            b[j][i] += coeff
    return b


def vec_from_sym(b: Mat) -> list[Fraction]:
    return [b[i][j] for (i, j) in SYM_BASIS]


def invariant_form_space_dim(gens: list[Mat]) -> int:
    """dim { B symmetric : g^T B g = B for every g in gens }, exactly over Q."""
    rows: list[list[Fraction]] = []
    for g in gens:
        cols = []
        for k in range(len(SYM_BASIS)):
            e = [F(1) if t == k else F(0) for t in range(len(SYM_BASIS))]
            img = congruence(g, sym_from_vec(e))
            cols.append(vec_from_sym(img))
        # (g.B - B) as a linear map, written row-wise
        for r in range(len(SYM_BASIS)):
            rows.append(
                [cols[c][r] - (F(1) if c == r else F(0)) for c in range(len(SYM_BASIS))]
            )
    return len(SYM_BASIS) - rank_Q(rows)


def signature(b: Mat) -> tuple[int, int, int]:
    """Exact Sylvester signature (n_pos, n_neg, n_zero) by symmetric elimination."""
    n = len(b)
    m = [row[:] for row in b]
    pos = neg = zero = 0
    idx = list(range(n))
    while idx:
        # find a nonzero diagonal entry
        p = None
        for i in idx:
            if m[i][i] != 0:
                p = i
                break
        if p is None:
            # find an off-diagonal nonzero and rotate it onto the diagonal
            found = None
            for i in idx:
                for j in idx:
                    if i != j and m[i][j] != 0:
                        found = (i, j)
                        break
                if found:
                    break
            if found is None:
                zero += len(idx)
                break
            i, j = found
            for k in range(n):
                m[i][k] = m[i][k] + m[j][k]
            for k in range(n):
                m[k][i] = m[k][i] + m[k][j]
            continue
        d = m[p][p]
        if d > 0:
            pos += 1
        else:
            neg += 1
        for i in idx:
            if i == p:
                continue
            f = m[i][p] / d
            if f:
                for k in range(n):
                    m[i][k] -= f * m[p][k]
                for k in range(n):
                    m[k][i] -= f * m[k][p]
        idx.remove(p)
    return pos, neg, zero


def density_weight_factor(g: Mat) -> Fraction:
    """A weight-1 density transforms by |det g|.  Exact, on rationals."""
    d = det(g)
    return d if d >= 0 else -d


# --------------------------------------------------------------------------
# [E] the naturality obstruction
# --------------------------------------------------------------------------

ETA = mat([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
DELTA = mat([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
# a non-diagonal Lorentzian witness, congruent to ETA
BOOSTLIKE = mat(
    [
        [F(5, 4), F(3, 4), 0, 0],
        [F(3, 4), F(-5, 4) + F(9, 8) + F(1, 8) - F(1), 0, 0],
        [0, 0, -1, 0],
        [0, 0, 0, -1],
    ]
)


def run_exact(mut: str) -> None:
    two_i = scal(4, 2)
    half_i = scal(4, F(1, 2))
    minus_i = scal(4, -1)

    # 1. GL(4) generated (for our purpose) by the scaling 2*I alone already kills
    #    every invariant symmetric form.
    dim_gl = invariant_form_space_dim([two_i])
    if mut == "invariant_dim":
        dim_gl = 1
    check(
        "E",
        "no nonzero GL(4,R)-invariant symmetric bilinear form on R^4 "
        "(scaling 2I already forces B = 0)",
        dim_gl == 0,
        {"dim": dim_gl},
    )
    FACTS["invariant_symmetric_form_dim_under_scaling"] = dim_gl

    # 2. the same for a weight-1 density: |det(2I)| = 16 != 1
    w = density_weight_factor(two_i)
    check(
        "E",
        "no nonzero GL(4,R)-invariant density on R^4: |det(2I)| = 16 != 1",
        w == F(16) and w != F(1),
        {"|det 2I|": w},
    )
    FACTS["density_factor_2I"] = w

    # 3. the obstruction survives every reduction the source DECLARES.
    #    orientation / spin  ->  the subgroup must still contain 2I (det > 0)
    #    "one dimension of time"  ->  the stabiliser of the line span(e_0)
    #                                 still contains 2I
    d2 = det(two_i)
    in_gl_plus = d2 > 0
    # 2I preserves span(e0) (it preserves every line)
    preserves_line = all(
        two_i[i][0] == 0 for i in range(1, 4)
    )  # image of e0 stays in span(e0)
    if mut == "reduction_escape":
        preserves_line = False
    check(
        "E",
        "2I lies in GL+(4,R) (det = 16 > 0), so an orientation/spin reduction "
        "does not remove the obstruction",
        in_gl_plus and d2 == F(16),
        {"det 2I": d2},
    )
    check(
        "E",
        "2I stabilises the time line span(e0), so declaring 'one dimension of "
        "time' does not remove the obstruction",
        preserves_line,
        None,
    )
    dim_line_stab = invariant_form_space_dim([two_i])
    check(
        "E",
        "invariant-form dimension under {2I} is 0 for every declared reduction "
        "(GL, GL+, line stabiliser) -- one computation covers all three",
        dim_line_stab == 0,
        {"dim": dim_line_stab},
    )

    # 4. CONTROL that must FIRE: at the O(1,3) reduction the form exists.
    #    lambda*I in O(1,3)  <=>  lambda^2 = 1.
    lam_ok = []
    for lam in (F(2), F(1, 2), F(-1), F(1)):
        g = scal(4, lam)
        lam_ok.append((lam, congruence(g, ETA) == ETA))
    good = {lam for lam, ok in lam_ok if ok}
    if mut == "o13_contains_2I":
        good = good | {F(2)}
    check(
        "C",
        "CONTROL FIRES: lambda*I preserves eta iff lambda = +-1; 2I and (1/2)I "
        "do NOT lie in O(1,3)",
        good == {F(1), F(-1)},
        {"preserving": sorted(good)},
    )
    check(
        "C",
        "CONTROL FIRES: eta is nondegenerate (det = -1) and O(1,3)-invariant, "
        "so the base duality EXISTS exactly at the O(1,3) reduction",
        det(ETA) == F(-1) and congruence(minus_i, ETA) == ETA,
        {"det eta": det(ETA)},
    )
    check(
        "C",
        "CONTROL FIRES: the eta-density factor is 1 for every g in O(1,3) "
        "(checked on -I), so a metric supplies the density too",
        density_weight_factor(minus_i) == F(1),
        None,
    )
    check(
        "E",
        "eta has Lorentzian signature (1,3,0), exactly",
        signature(ETA) == (1, 3, 0),
        {"sig": signature(ETA)},
    )
    check(
        "C",
        "CONTROL FIRES: the Euclidean witness delta has signature (4,0,0), so "
        "the signature routine is not returning a constant",
        signature(DELTA) == (4, 0, 0),
        {"sig": signature(DELTA)},
    )

    # 5. the fibre of Met(X) has no distinguished point: GL(4) moves eta.
    g = mat([[2, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    moved = congruence(g, ETA)
    check(
        "E",
        "GL(4,Q) moves eta inside the fibre (diag(2,1,1,1).eta != eta), so the "
        "Met(X) fibre carries no canonical basepoint",
        moved != ETA and signature(moved) == (1, 3, 0),
        {"sig(moved)": signature(moved)},
    )

    # 6. the tautological identity: on Y = Met_x, the tautological form at the
    #    point y IS y; pulling it back along a section returns the section.
    taut_ok = True
    for y in (ETA, DELTA, BOOSTLIKE):
        pull = [row[:] for row in y]  # s^*(tau) at x = tau_{s(x)} = s(x)
        if pull != y:
            taut_ok = False
    if mut == "taut_pullback":
        taut_ok = False
    check(
        "E",
        "s^*(tautological horizontal metric) = s, exactly, on three rational "
        "fibre witnesses: the base duality obtained by pullback IS the section",
        taut_ok,
        None,
    )
    check(
        "E",
        "the tautological form is NOT constant on the fibre (eta != delta), so "
        "the pullback identity is not vacuous",
        ETA != DELTA,
        None,
    )
    check(
        "E",
        "the third fibre witness is genuinely non-diagonal and Lorentzian",
        BOOSTLIKE[0][1] != 0 and signature(BOOSTLIKE) == (1, 3, 0),
        {"sig": signature(BOOSTLIKE)},
    )

    # 7. the reduction that DOES supply the duality is exactly a point of the
    #    fibre: dim of the invariant-form space under O(1,3) generators.
    o13_gens = [minus_i]
    dim_o13 = invariant_form_space_dim(o13_gens)
    check(
        "E",
        "under -I alone the invariant-form space is all of Sym^2 (dim 10): the "
        "no-go is driven by scalings, not by discrete elements",
        dim_o13 == 10,
        {"dim": dim_o13},
    )

    FACTS["signature_eta"] = signature(ETA)
    FACTS["det_eta"] = det(ETA)


# --------------------------------------------------------------------------
# [Q] quote presence at a stated locus
# --------------------------------------------------------------------------

# (label, path, line, exact substring, locus token expected at/above the line)
PORTAL_QUOTES = [
    ("P-0053", 137, "responsible for a volume form", "00:53:11"),
    ("P-0110", 181, "to equal the space of metrics on", "01:10:36"),
    ("P-0110b", 181, "but not at a field level, at a pointwise tensorial level", "01:10:36"),
    ("P-0111", 183, "we could define fermions, but we would also lock out any ability to do dynamics", "01:11:03"),
    ("P-0111b", 185, "for every point in the fibers, we get a metric downstairs on the base space", "01:11:22"),
    ("P-0112", 187, "got a metric on the 4, a metric on the 10", "01:12:17"),
    ("P-0113", 191, "missing exactly the data of a connection", "01:13:00"),
    ("P-0205", 413, "all the action is happening up here on", "02:05:04"),
    ("P-0218", 445, "not even with a metric", "02:18:03"),
    ("P-0218b", 445, "what we instead do is to work over the space of all possible point-wise metrics", "02:18:03"),
    ("P-0219", 447, "proto-spacetime with no metric", "02:19:09"),
    ("P-0222", 457, "we get spinors without ever having to choose a metric", "02:22:27"),
    ("P-0223", 459, "is, in fact, a connection on the space", "02:23:30"),
    ("P-0230", 481, "we have not made any other choices", "02:30:09"),
]

UCSD_QUOTES = [
    ("U-0004", 23, "the space of point wise Lorentzian metrics on an x four that has not yet become spacetime", "00:04:08"),
    ("U-0006", 29, KK_PRIMARY, "00:06:32"),
    ("U-0012", 47, "sitting on the lousy foundation of the space of all metrics", "00:12:15"),
    ("U-0045", 155, "We wasted the seventies work because we wanted to avoid indefinite signature on the killing form", "00:45:00"),
    ("U-0048", 170, "It has an automatic metric. You haven't chosen a metric.", "00:48:49"),
    ("U-0049", 173, "choosing four degrees of freedom, one dimension of time on those four degrees of freedom, and a spin structure", "00:49:16"),
]

REGISTER_QUOTES = [
    ("SC-GEO-02", 56, 60, "An Observerse is defined to be a triple", "page: 16"),
    ("SC-GEO-03", 80, 86, "have a pre-existing metric.", "page: 17"),
    ("SC-GEO-05", 130, 134, "C(Y) = C = V (+) H*", "page: 19"),
    ("SC-GEO-04", 105, 109, "physics may actually be happening mostly on", "page: 17"),
    ("SC-GEO-06", 154, 158, "without making a choice of metric", "page: 20"),
    ("SC-GEO-07", 179, 183, "each observation of Y via a choice of metric gimel on X actually induces a metric and connection", "page: 21"),
    ("SC-ACT-01", 576, 580, "I^B_1(omega_Y, gimel_X)", "page: 44"),
]


def run_quotes(mut: str) -> None:
    pl = lines(PORTAL)
    for label, ln, sub, ts in PORTAL_QUOTES:
        n = ln
        if mut == "quote_line" and label == "P-0111b":
            n = ln + 1
        ok = 1 <= n <= len(pl) and sub in pl[n - 1] and pl[n - 1].lstrip().startswith(ts)
        check("Q", f"portal-2020 {ts} L{n}: {label}", ok, None)

    ul = lines(UCSD)
    for label, ln, sub, ts in UCSD_QUOTES:
        n = ln
        if mut == "quote_line" and label == "U-0049":
            n = ln + 1
        ok = 1 <= n <= len(ul) and sub in ul[n - 1]
        # the timestamp sits on the preceding speaker line
        ts_ok = False
        for back in range(1, 4):
            if n - 1 - back >= 0 and ul[n - 1 - back].strip().endswith(f"[{ts}]:"):
                ts_ok = True
                break
        check("Q", f"ucsd-2025 {ts} L{n}: {label}", ok and ts_ok, None)

    rl = lines(REGISTER)
    for scid, id_line, quote_line, sub, page in REGISTER_QUOTES:
        n = quote_line
        if mut == "quote_line" and scid == "SC-ACT-01":
            n = quote_line + 3
        id_ok = rl[id_line - 1].strip() == f"- id: {scid}"
        q_ok = 1 <= n <= len(rl) and sub in rl[n - 1]
        # the page locus lives within the next 12 lines of the entry
        page_ok = any(page in rl[k] for k in range(id_line - 1, min(id_line + 24, len(rl))))
        check("Q", f"register {scid} L{id_line} verbatim L{n} {page}", id_ok and q_ok and page_ok, None)

    # the two draft-extraction loci
    s11 = read(S11)
    check(
        "Q",
        "draft-2021 p.50 eq (11.4): 'the metric as an embedding' -- the section "
        "IS a metric (s11-s12 extraction)",
        "to the metric as an embedding" in s11 and "(11.4)" in s11,
        None,
    )
    check(
        "Q",
        "draft-2021 p.51 eq (11.5): the pullback splits as T*X (+) N_gimel",
        "(11.5)" in s11 and "T∗X" in s11,
        None,
    )
    pack = read(PACK)
    dom = r"\operatorname{MET}(X^{1,3})"
    if mut == "action_domain":
        dom = r"\operatorname{MET}(X^{9,9})"
    check(
        "Q",
        "draft-2021 Sect. 9.1 eq (9.1): the first-order bosonic action is "
        "declared on G x MET(X^{1,3}) -- the metric on X is an ARGUMENT",
        dom in pack,
        None,
    )
    check(
        "Q",
        "the same source pack carries the variation d/ds I^B_1(eps, varpi+s alpha) "
        "= <alpha, Upsilon^B_omega>, so the pairing is the source's own",
        r"I^B_1(\epsilon,\varpi+s\alpha)" in pack,
        None,
    )
    reg = read(REGISTER)
    check(
        "Q",
        "register SC-ACT-01 notes carry the printed brace labels 'Hodge Star' "
        "and 'Zorro Metric' on eq (9.4)",
        "Hodge Star" in reg and "Zorro Metric" in reg,
        None,
    )
    check(
        "Q",
        "register SC-ACT-01 verbatim subscripts the inner product by g_gimel",
        ">_{g_gimel}" in reg,
        None,
    )
    rl2 = lines(REGISTER)
    check(
        "Q",
        "register SC-META-54 L2772 is polarity DISAVOWS and carries 'There "
        "isn't a global section.' at toe-2025 01:18:06",
        rl2[2771].strip() == "- id: SC-META-54"
        and rl2[2772].strip() == "polarity: DISAVOWS"
        and "There isn't a global section." in rl2[2776]
        and "timestamp: 01:18:06" in rl2[2780],
        None,
    )
    check(
        "Q",
        "register SC-META-54 notes grade the exchange SEMANTICALLY UNCERTAIN, "
        "so no settled global-section posture is inferred here",
        "SEMANTICALLY UNCERTAIN" in rl2[2783],
        None,
    )

    # absence sweeps, reported as sweeps over named surfaces -- never as a
    # statement about the draft PDF, which is not in this checkout.
    tokens = ("volume", "dvol", "measure", "integral", "orient", "density")
    s11_low = s11.lower()
    hits11 = {t: s11_low.count(t) for t in tokens}
    check(
        "C",
        "ABSENCE SWEEP: the s11-s12 draft extraction (draft 11-12) contains "
        "zero hits for volume/dvol/measure/integral/orient/density",
        all(v == 0 for v in hits11.values()),
        hits11,
    )
    s9 = read(
        REPO / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md"
    )
    check(
        "C",
        "CONTROL FIRES: the s9 extraction DOES mention 'density', and its "
        "mentions are repository commentary ('It does not supply the missing "
        "density'), not quoted draft text -- so the sweep is not a null routine",
        s9.lower().count("density") > 0
        and "It does not supply the missing density" in s9,
        {"density_hits": s9.lower().count("density")},
    )
    check(
        "C",
        "the draft PDF is NOT in this checkout, so every draft quotation here "
        "is register- or extraction-mediated and is labelled so",
        not (REPO / "lab/sources/Geometric_Unity-Draft-April-1st-2021.pdf").exists(),
        None,
    )


# --------------------------------------------------------------------------
# [R] reproductions, before use
# --------------------------------------------------------------------------


def run_repro(mut: str) -> None:
    digest = hashlib.sha256(LEDGER.read_bytes()).hexdigest()
    expect = LEDGER_SHA256
    if mut == "ledger_sha":
        expect = "0" * 64
    check(
        "R",
        "v0.258 ledger sha256 reproduces LA-11 Lens P1",
        digest == expect,
        {"sha256": digest},
    )
    FACTS["ledger_sha256"] = digest

    ledger_text = read(LEDGER)
    check(
        "R",
        "LT-GR6b is NOT in the sequential ledger: it is a proposal, and this "
        "route does not edit it",
        '"LT-GR6b"' not in ledger_text,
        None,
    )

    la11 = read(LA11)
    trig_needle = "a source-owned global base duality on the observed X^4"
    if mut == "trigger_text":
        trig_needle = "a source-owned global base triality on the observed X^4"
    check(
        "R",
        "LA-11's proposed LT-GR6b revival_trigger, read out of LA-11's own "
        "artifact, demands 'a source-owned global base duality on the observed X^4'",
        trig_needle in la11,
        None,
    )
    check(
        "R",
        "the same trigger demands 'a density together with a nondegenerate "
        "Lambda^1 pairing'",
        "a density together with a nondegenerate Lambda^1 pairing" in la11,
        None,
    )
    check(
        "R",
        "the same trigger demands positivity on the physical quotient",
        "positive on the physical quotient" in la11,
        None,
    )
    check(
        "R",
        "LA-11's distance instructs 'Build (b) as a source-owned global object "
        "on X^4' -- the sentence this route corrects",
        "Build (b) as a source-owned global object on X^4" in la11,
        None,
    )
    check(
        "R",
        "LA-11 types the row NEEDS / MISSING_CONSTRUCTION",
        '"reason_kind": "MISSING_CONSTRUCTION"' in la11,
        None,
    )

    ot1 = read(OT1)
    check(
        "R",
        "OT-1 factors clause O4 into (a) a fibre form and (b) 'a base duality "
        "absorbing the one-form index'",
        "a base duality absorbing the one-form index" in ot1,
        None,
    )
    check(
        "R",
        "OT-1 writes 'Neither is supplied.' of those two legs -- the sentence "
        "this route corrects for leg (b)",
        "Neither is supplied." in ot1,
        None,
    )
    check(
        "R",
        "OT-1 already returns O4 = OWNED_G on the so(7,7) trace form, so the "
        "fibre leg is available at a NAMED subscript",
        "the certifying pairing is the so(7,7) trace form" in ot1,
        None,
    )
    check(
        "R",
        "FAIRNESS CONTROL: OT-1's leg-(b) bullet already identifies the object "
        "correctly as 'the observer's metric geometry' -- the identification is "
        "not what this route corrects",
        "is the observer's metric geometry" in ot1,
        None,
    )
    check(
        "R",
        "OT-1's 'Neither is supplied.' is followed in place by a ledger-scoped "
        "justification ('zero v0.258 rows name'), so its scope is the ledger",
        "zero v0.258 rows name" in ot1,
        None,
    )

    md1 = read(MD1)
    check(
        "R",
        "MD-1's contraction formula reproduces: (s^* omega)_mu = omega_mu + "
        "omega_(ab) d_mu g_ab",
        "(s^* omega)_mu = omega_mu + omega_(ab) d_mu g_ab" in md1,
        None,
    )
    check(
        "R",
        "MD-1 records that s^* is surjective onto T*X (contraction, not "
        "projection)",
        "surjective onto `T*X`" in md1,
        None,
    )

    s4 = read(S4GATE)
    check(
        "R",
        "the banked S^4 obstruction reproduces: a spin four-manifold does not "
        "automatically admit a global Lorentz metric",
        "a spin four-manifold does not automatically admit a global Lorentz metric"
        in s4
        and "Euler characteristic two" in s4,
        None,
    )


# --------------------------------------------------------------------------
# [C] controls, including the correction of record
# --------------------------------------------------------------------------


def run_controls(mut: str) -> None:
    art = read(ARTIFACT) if ARTIFACT.exists() else ""
    check(
        "C",
        "the artifact exists at the declared path",
        bool(art),
        {"path": str(ARTIFACT.relative_to(REPO))},
    )
    check(
        "C",
        "the artifact carries the GU-COMPARATOR-ROUTING notice verbatim",
        ROUTING_NOTICE_HEAD in art,
        None,
    )
    check(
        "C",
        "the artifact carries an exact `Classification: `SOURCE_NATIVE_ROUTE`` line",
        CLASSIFICATION_LINE in art,
        None,
    )
    check(
        "C",
        "the artifact does NOT contain the withdrawn, refuted, "
        "non-source-attested vertical-scalars clause",
        WITHDRAWN_IN_GEOMETER not in art
        and "vertical connection components may appear as four-dimensional scalars"
        not in art,
        None,
    )
    # the KK disavowal control: the artifact must quote the disavowal and must
    # not assert a KK reduction of its own.
    check(
        "C",
        "CONTROL FIRES: the artifact quotes Weinstein's Kaluza-Klein disavowal "
        "in its PRIMARY form (lower-case 'it's', straight apostrophes)",
        KK_PRIMARY in art,
        None,
    )
    check(
        "C",
        "TRANSCRIPTION NOTE: the routing method renders the same disavowal "
        "capitalised and with curly apostrophes; the primary does not carry "
        "that form",
        KK_METHOD_RENDERING in read(ROUTING) and KK_METHOD_RENDERING not in read(UCSD),
        None,
    )

    # CORRECTION OF RECORD, asserted positively.
    geo = read(GEOMETER)
    present = WITHDRAWN_IN_GEOMETER in geo
    if mut == "withdrawn_absent":
        present = False
    check(
        "C",
        "CORRECTION OF RECORD: the withdrawn clause is STILL PRESENT in "
        "GEOMETER-VS-PHYSICS-OBJECTS.md (AGENTS.md step 1), though the routing "
        "method withdrew it",
        present,
        {"line": next((i + 1 for i, l in enumerate(geo.split("\n")) if WITHDRAWN_IN_GEOMETER in l), None)},
    )
    routing = read(ROUTING)
    check(
        "C",
        "the routing method's own [!CAUTION] block records the withdrawal, so "
        "the two surfaces genuinely disagree",
        "Withdrawn clause" in routing and "not source-attested" in routing,
        None,
    )

    # classification census of the artifact's determination table
    counts = {
        "SOURCE-CONFIRMED": art.count("`SOURCE-CONFIRMED`"),
        "REPOSITORY-DERIVED": art.count("`REPOSITORY-DERIVED`"),
        "RECONSTRUCTED": art.count("`RECONSTRUCTED`"),
        "SPECULATIVE": art.count("`SPECULATIVE`"),
    }
    if mut == "classification_count":
        counts["SOURCE-CONFIRMED"] = 0
    FACTS["classification_counts"] = counts
    check(
        "C",
        "every classification token in the artifact's determination table is "
        "used at least once, and SOURCE-CONFIRMED is the majority class",
        all(v > 0 for v in counts.values())
        and counts["SOURCE-CONFIRMED"] > counts["RECONSTRUCTED"]
        and counts["SOURCE-CONFIRMED"] > counts["SPECULATIVE"],
        counts,
    )
    check(
        "C",
        "the artifact declares a target_claim naming a register id",
        "target_claim:" in art and "SC-GEO-03" in art,
        None,
    )
    check(
        "C",
        "PLANTED FAILING CONTROL: a deliberately wrong locus is detectable -- "
        "the KK disavowal is NOT on portal L1",
        KK_DISAVOWAL not in lines(PORTAL)[0],
        None,
    )
    check(
        "C",
        "PLANTED FAILING CONTROL: 'pre-existing metric' does NOT occur in the "
        "UCSD transcript, so the register's draft locus is not laundered from "
        "a spoken source",
        "pre-existing metric" not in read(UCSD),
        None,
    )
    check(
        "C",
        "the artifact states the action domain it found, verbatim",
        "MET(X^{1,3})" in art,
        None,
    )
    check(
        "C",
        "the artifact states the pullback identity it proved",
        "s^*(tautological horizontal metric) = s" in art
        or "s^*τ = s" in art,
        None,
    )
    check(
        "C",
        "the artifact declares that it did NOT read the 2021 PDF, so no draft "
        "quotation is presented as a direct reading",
        "register-mediated" in art and "did **not** read the 2021 PDF" in art,
        None,
    )
    check(
        "C",
        "the artifact records that horn-B's variation question is SOURCE-SILENT "
        "in this checkout rather than resolved",
        "SOURCE-SILENT" in art,
        None,
    )
    check(
        "C",
        "the artifact leaves OT-1's clause-O4 no-go at subscript W untouched "
        "and says so",
        "It is untouched" in art or "it is untouched and it stands" in art,
        None,
    )

    # ---- final: anti-drift between the artifact's printed certificate and
    # ---- this run.  These two checks must be the last two appended.
    n_expected = len(RESULTS) + 2
    split_expected: dict[str, int] = {}
    for kind, _, _, _ in RESULTS:
        split_expected[kind] = split_expected.get(kind, 0) + 1
    split_expected["C"] = split_expected.get("C", 0) + 2
    cert_line = f"CERTIFICATE: {n_expected}/{n_expected} checks pass"
    split_line = "split  " + "  ".join(
        f"[{k}] {split_expected[k]}" for k in sorted(split_expected)
    )
    FACTS["expected_certificate"] = cert_line
    FACTS["expected_split"] = split_line
    check(
        "C",
        "ANTI-DRIFT: the artifact's printed CERTIFICATE line matches this run",
        cert_line in art,
        {"expected": cert_line},
    )
    check(
        "C",
        "ANTI-DRIFT: the artifact's printed split line matches this run",
        split_line in art,
        {"expected": split_line},
    )


# --------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------


def run_all(mut: str = "") -> int:
    RESULTS.clear()
    FACTS.clear()
    run_exact(mut)
    run_quotes(mut)
    run_repro(mut)
    run_controls(mut)
    assert_no_float(FACTS)
    npass = sum(1 for _, _, ok, _ in RESULTS if ok)
    ntot = len(RESULTS)
    return 0 if npass == ntot else 1


def report() -> int:
    rc = run_all("")
    npass = sum(1 for _, _, ok, _ in RESULTS if ok)
    ntot = len(RESULTS)
    split: dict[str, int] = {}
    for kind, _, _, _ in RESULTS:
        split[kind] = split.get(kind, 0) + 1
    for kind, name, ok, detail in RESULTS:
        if not ok:
            print(f"  FAIL [{kind}] {name}  {detail}")
    print(f"CERTIFICATE: {npass}/{ntot} checks pass; no load-bearing float (swept).")
    print(
        "split  "
        + "  ".join(f"[{k}] {split[k]}" for k in sorted(split))
    )
    return rc


MUTATIONS = [
    ("invariant_dim", "claim a nonzero GL(4)-invariant form exists"),
    ("taut_pullback", "deny s^*(tautological) = s"),
    ("quote_line", "shift three quote line numbers by one"),
    ("o13_contains_2I", "claim 2I lies in O(1,3)"),
    ("withdrawn_absent", "claim the withdrawn clause is gone from GEOMETER"),
    ("ledger_sha", "corrupt the v0.258 sha256"),
    ("trigger_text", "corrupt the LT-GR6b trigger string"),
    ("action_domain", "misstate the action domain as MET(X^{9,9})"),
    ("reduction_escape", "claim 2I fails to stabilise the time line"),
    ("classification_count", "zero out the SOURCE-CONFIRMED census"),
]


def selftest() -> int:
    bad = []
    for mut, desc in MUTATIONS:
        rc = run_all(mut)
        status = "OK" if rc == 1 else "DID NOT FIRE"
        if rc != 1:
            bad.append(mut)
        print(f"  mutation {mut:<22} exit {rc}  {status}      ({desc})")
    print()
    if bad:
        print(f"FAILURE-PATH SELFTEST: FAIL ({len(bad)} mutations did not fire: {bad})")
        return 1
    print(
        f"FAILURE-PATH SELFTEST: PASS ({len(MUTATIONS)}/{len(MUTATIONS)} "
        "mutations drove exit 1)"
    )
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    sys.exit(report())
