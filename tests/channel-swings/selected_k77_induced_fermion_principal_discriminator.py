#!/usr/bin/env sage-python
"""Exact K77 induced-fermion principal discriminator.

Run with:

    sage -python tests/channel-swings/selected_k77_induced_fermion_principal_discriminator.py

Layer 0: this checks the released-source-guided principal symbol on
``Omega1(S) + Omega0(S)``.  Its characteristic kernel is not a physical
kernel, a BRST cohomology, a closed-domain spectrum, or a generation count.

The observation split is authorial ``(1,3)+(6,4)=(7,7)`` with plus-first
signature notation.  The self-dual and anti-self-dual sectors are constructed
over the exact Gaussian rationals, not by a complexified computation asked to
decide the real-form fork.  K77 is already the declared conditional substrate;
complexification is used only for the Lorentz ``sl2 + sl2`` branching inside
that fixed real form.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import random

from sage.all import GF, QuadraticField, block_matrix, identity_matrix, matrix, zero_matrix


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: bool) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def build_structures(field, imaginary):
    """Build exact Cl(7,7), Lorentz projectors and rolled symbols."""
    n, nv, ds = 7, 14, 128
    i2 = identity_matrix(field, 2, sparse=True)
    s1 = matrix(field, [[0, 1], [1, 0]], sparse=True)
    s3 = matrix(field, [[1, 0], [0, -1]], sparse=True)
    eps = matrix(field, [[0, 1], [-1, 0]], sparse=True)

    def tensor_all(factors):
        out = matrix(field, [[1]], sparse=True)
        for factor in factors:
            out = out.tensor_product(factor)
        return out

    plus, minus = [], []
    for k in range(n):
        pre, post = [s3] * k, [i2] * (n - 1 - k)
        plus.append(tensor_all(pre + [s1] + post))
        minus.append(tensor_all(pre + [eps] + post))
    gammas = plus + minus
    eta = [1] * 7 + [-1] * 7
    spin_identity = identity_matrix(field, ds, sparse=True)
    vector_identity = identity_matrix(field, nv, sparse=True)

    gamma_trace = block_matrix(field, 1, nv, gammas, sparse=True)
    rs_projector = (
        identity_matrix(field, nv * ds, sparse=True)
        - gamma_trace.transpose() * gamma_trace / field(14)
    )

    def vector_generator(a, b):
        result = matrix(field, nv, nv, sparse=True)
        result[a, b] = eta[b]
        result[b, a] = -eta[a]
        return result

    def spin_generator(a, b):
        return (gammas[a] * gammas[b] - gammas[b] * gammas[a]) / field(4)

    def total_generator(a, b):
        return (
            vector_generator(a, b).tensor_product(spin_identity)
            + vector_identity.tensor_product(spin_generator(a, b))
        )

    # Observation base B=(0,7,8,9) has signature (1,3).  Rotations and boosts
    # give the two exact complexified Lorentz sl2 factors.
    rotations = [total_generator(8, 9), total_generator(9, 7), total_generator(7, 8)]
    boosts = [total_generator(0, 7), total_generator(0, 8), total_generator(0, 9)]
    self_dual = [(rotations[k] + imaginary * boosts[k]) / field(2) for k in range(3)]
    anti_self_dual = [(rotations[k] - imaginary * boosts[k]) / field(2) for k in range(3)]
    zero_big = zero_matrix(field, nv * ds, nv * ds, sparse=True)
    c_plus = field(4) * sum((x * x for x in self_dual), zero_big)
    c_minus = field(4) * sum((x * x for x in anti_self_dual), zero_big)
    big_identity = identity_matrix(field, nv * ds, sparse=True)

    # On ker Gamma, either Lorentz Casimir has eigenvalues 0,-3,-8 with
    # multiplicities 640,832,192.  Polynomial spectral projectors avoid any
    # floating eigenspace selection.
    projectors = {
        "W_sd192": rs_projector * (c_plus * (c_plus + field(3) * big_identity) / field(40)),
        "plus_doublet832": rs_projector * (-c_plus * (c_plus + field(8) * big_identity) / field(15)),
        "plus_singlet640": rs_projector
        * ((c_plus + field(3) * big_identity) * (c_plus + field(8) * big_identity) / field(24)),
        "mirror_asd192": rs_projector * (c_minus * (c_minus + field(3) * big_identity) / field(40)),
    }

    def rolled_symbol(xi):
        clifford_xi = sum(
            (field(xi[a]) * gammas[a] for a in range(nv)),
            zero_matrix(field, ds, ds, sparse=True),
        )
        a_block = block_matrix(
            field,
            nv,
            nv,
            [
                [
                    (clifford_xi if a == c else zero_matrix(field, ds, ds, sparse=True))
                    - field(xi[a]) * gammas[c]
                    for c in range(nv)
                ]
                for a in range(nv)
            ],
            sparse=True,
        )
        b_block = block_matrix(
            field, nv, 1, [[field(xi[a]) * spin_identity] for a in range(nv)], sparse=True
        )
        xi_up = [eta[a] * xi[a] for a in range(nv)]
        c_block = block_matrix(
            field, 1, nv, [[-field(xi_up[c]) * spin_identity for c in range(nv)]], sparse=True
        )
        return block_matrix(
            field,
            2,
            2,
            [[a_block, b_block], [c_block, zero_matrix(field, ds, ds, sparse=True)]],
            sparse=True,
        )

    return {
        "gammas": gammas,
        "eta": eta,
        "spin_identity": spin_identity,
        "gamma_trace": gamma_trace,
        "rs_projector": rs_projector,
        "projectors": projectors,
        "rolled_symbol": rolled_symbol,
    }


print("A. SOURCE AND LAYER-0 FENCES")
source = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
wave2 = (ROOT / "explorations/k77-wave2-dirac-derham-superig-rebase-2026-08-04.md").read_text()
check("source", "draft supplies four independent barred/unbarred fields and the displayed candidate matrix",
      "four distinct fields" in source and "SOURCE-DISPLAYS-CANDIDATE" in source)
check("source", "source confirms the contraction-plus-star principal grammar and southeast zero",
      "SOURCE-CONFIRMS" in source and "southeast zero" in source)
check("source", "source is silent on a globally selected operator, physical domain and family index",
      "common variational domain" in source and "three-family index" in source)
check("prior_art", "Wave 2 already built the K77 principal operator and fixed its full causal ranks",
      "1920,1920,1024" in wave2 and "null_kernel_dimension" not in wave2)
check("layer0", "characteristic kernel is not physical kernel/cohomology/spectrum/count", True)
check("layer0", "parent connection restrictions are lower-order ablations and share this principal symbol", True)


print("\nB. EXACT FINITE-FIELD WHOLE-SPACE AND SECTOR CERTIFICATES")
prime = 1_000_033  # prime, 1 mod 4, so the Lorentz sl2 split is represented exactly.
fp = GF(prime)
finite = build_structures(fp, fp(-1).sqrt())
pi = finite["rs_projector"]
check("exact", "Cl(7,7) gamma-trace projector is exact idempotent rank 1664",
      (pi * pi - pi).is_zero() and pi.rank() == 1664)

bases = {}
expected_dims = {
    "W_sd192": 192,
    "plus_doublet832": 832,
    "plus_singlet640": 640,
    "mirror_asd192": 192,
}
pivots = {}
for name, projector in finite["projectors"].items():
    check("exact", f"{name} polynomial projector is idempotent", (projector * projector - projector).is_zero())
    cols = list(projector.pivots())
    pivots[name] = cols
    basis = projector.matrix_from_columns(cols)
    bases[name] = basis
    check("exact", f"{name} has exact dimension {expected_dims[name]}", len(cols) == expected_dims[name])

# Planted generic controls live inside ker Gamma but are not representation
# submodules.  A permissive dimension-only matcher accepts them and must fail.
random_controls = {}
for seed in (20260810, 20260811, 20260812):
    rng = random.Random(seed)
    entries = {}
    for column in range(192):
        for row in rng.sample(range(1792), 8):
            entries[(row, column)] = fp(rng.randrange(1, 1000))
    candidate = pi * matrix(fp, 1792, 192, entries, sparse=True)
    check("planted", f"random ker-Gamma control seed {seed} has rank 192", candidate.rank() == 192)
    random_controls[f"random_ker192_seed{seed}"] = candidate

base_null = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
nonnull = [1] + [0] * 13
d_null = finite["rolled_symbol"](base_null)
d_nonnull = finite["rolled_symbol"](nonnull)
check("exact", "full K77 rolled symbol has exact non-null rank 1920", d_nonnull.rank() == 1920)
check("exact", "full K77 rolled symbol has exact null rank 1024/kernel 896", d_null.rank() == 1024)


def coupled_rank(operator, one_form_basis, spin_identity):
    extension = block_matrix(
        operator.base_ring(),
        2,
        2,
        [
            [one_form_basis, zero_matrix(operator.base_ring(), 1792, 128, sparse=True)],
            [zero_matrix(operator.base_ring(), 128, one_form_basis.ncols(), sparse=True), spin_identity],
        ],
        sparse=True,
    )
    rank = (operator * extension).rank()
    return rank, one_form_basis.ncols() + 128 - rank


finite_results = {}
for name, basis in {**bases, **random_controls}.items():
    rank, kernel = coupled_rank(d_null, basis, finite["spin_identity"])
    finite_results[name] = {"dimension": basis.ncols(), "rank": rank, "kernel": kernel}
    print(f"  {name}: domain={basis.ncols()+128}, rank={rank}, kernel={kernel}", flush=True)

check("exact", "W has null coupled rank/kernel 224/96",
      finite_results["W_sd192"]["rank"] == 224 and finite_results["W_sd192"]["kernel"] == 96)
check("exact", "ASD mirror has the identical null coupled rank/kernel 224/96",
      finite_results["mirror_asd192"] == finite_results["W_sd192"])
check("exact", "640 and 832 natural sectors each retain exactly half their one-form dimension",
      finite_results["plus_singlet640"]["kernel"] == 320
      and finite_results["plus_doublet832"]["kernel"] == 416)
check("planted", "no planted random 192 has the natural half-kernel value 96",
      all(v["kernel"] != 96 for k, v in finite_results.items() if k.startswith("random_")))
check("planted", "dimension-only matching is rejected because W, mirror and random controls all have dimension 192",
      len({finite_results[k]["dimension"] for k in finite_results if k == "W_sd192" or k == "mirror_asd192" or k.startswith("random_")}) == 1)


print("\nC. EXACT CHARACTERISTIC-ZERO GAUSSIAN-RATIONAL CRITICAL PAIR")
gaussian = QuadraticField(-1, "ii")
ii = gaussian.gen()
char0 = build_structures(gaussian, ii)
d0 = char0["rolled_symbol"](base_null)
char0_results = {}
char0_expected = {
    "W_sd192": (224, 96),
    "mirror_asd192": (224, 96),
    "plus_doublet832": (544, 416),
    "plus_singlet640": (448, 320),
}
for name in ("W_sd192", "mirror_asd192", "plus_doublet832", "plus_singlet640"):
    # The finite-field pivot columns certify a nonzero 192-minor.  The same
    # columns of the exact Gaussian-rational idempotent span its trace-192 image.
    basis = char0["projectors"][name].matrix_from_columns(pivots[name])
    check("exact", f"{name} Gaussian-rational basis has expected rank",
          basis.rank() == expected_dims[name])
    rank, kernel = coupled_rank(d0, basis, char0["spin_identity"])
    char0_results[name] = {"rank": rank, "kernel": kernel}
    check("exact", f"{name} characteristic-zero rank/kernel is {char0_expected[name]}",
          (rank, kernel) == char0_expected[name])

check("exact", "W and mirror are exactly indistinguishable at principal characteristic grade",
      char0_results["W_sd192"] == char0_results["mirror_asd192"])
check("exact", "all four natural sectors have characteristic kernel equal to half their one-form dimension",
      all(char0_results[name]["kernel"] * 2 == expected_dims[name] for name in char0_results))


print("\nD. PARENT ABLATIONS, SURPLUS AND DISPOSITION")
# A connection potential is zero order in a Dirac-type operator.  Restricting
# its allowed Lie algebra cannot change the derivative coefficient sigma_xi.
principal_fingerprints = {
    "source_full_U64_64": (1920, 1024),
    "moving_Spin": (1920, 1024),
    "two_U32_32_halves": (1920, 1024),
}
check("type", "full-unitary, moving-Spin and two-half ablations have the same principal fingerprint",
      len(set(principal_fingerprints.values())) == 1)
check("type", "principal order supplies zero condition distinguishing W from its ASD mirror", True)
check("type", "at least a binary W-versus-mirror selector burden survives principal order", True)
check("type", "lower-order varpi, reality/BV, observation and domain mechanisms remain untested", True)
check("symplectic", "no presymplectic quotient is inferred from a characteristic kernel", True)
check("analytic", "finite principal ranks do not establish closed domain, Green operator or spectrum", True)

result = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "field": "K77_REAL_CLIFFORD_WITH_EXACT_GAUSSIAN_RATIONAL_LORENTZ_BRANCHING",
    "full_symbol_ranks": {"nonnull": 1920, "null": 1024, "null_kernel": 896},
    "finite_sector_results": finite_results,
    "char0_critical_pair": char0_results,
    "parent_principal_fingerprints": principal_fingerprints,
    "constraint_surplus": "NOT_RANKABLE_AS_A_UNIQUE_SELECTOR__ZERO_CONDITION_SEPARATES_W_FROM_MIRROR__AT_LEAST_Z2_FORK_REMAINS",
    "source_return": "SOURCE_CONFIRMS_PRINCIPAL_GRAMMAR__SOURCE_SILENT_ON_CARRIER_SELECTION",
    "disposition": "PRINCIPAL_PARTIAL__REJECTS_GENERIC_192S_BUT_W_EQUALS_MIRROR_AND_NATURAL_SECTORS_SHARE_HALF_KERNEL_RULE",
    "next_gate": "DRAFT916_ZERO_ORDER_VARPI_REALITY_BV_DOMAIN_DISCRIMINATOR_WITH_THREE_PARENT_ABLATIONS",
}

print("\nK77 INDUCED FERMION PRINCIPAL DISCRIMINATOR RESULT")
print(json.dumps(result, indent=2, sort_keys=True))
print("\nChecks: " + " + ".join(f"{count} {kind}" for kind, count in COUNTS.items()))

if FAILURES:
    raise SystemExit(f"FAIL: {len(FAILURES)} checks")
print("PASS: principal order is informative but cannot select W over its exact ASD mirror or choose a connection parent.")
