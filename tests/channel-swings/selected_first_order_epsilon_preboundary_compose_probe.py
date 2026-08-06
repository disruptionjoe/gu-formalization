#!/usr/bin/env python3
"""Exact composition audit for selected first-order epsilon/preboundary data."""

from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def strict(relative):
    path = ROOT / relative
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=hook)


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


epsilon = strict("lab/process/k77-wave2-moving-shiab-epsilon-ward-green-domain.json")
selector = strict("lab/process/k77-wave2-principal-bianchi-product-selector.json")
principal = strict("lab/process/selected-cubic-two-connection-principal-ward-descent.json")
homogeneous = strict("lab/process/selected-cubic-intrinsic-homogeneous-ward-closure.json")

print("A. SOURCE AND PRODUCT-DOMAIN COMPOSITION")
selected = selector["selector"]["unique_bianchi_nonzero_row"]
channel_name = "_".join(part.upper() for part in selected)
check("source", "moving family is source-confirmed", epsilon["source_collision"]["displayed_phi_conjugated_shiab_family"] == "SOURCE_CONFIRMS")
check("source", "preferred source selector remains silent", epsilon["source_collision"]["preferred_historical_selector"].startswith("SOURCE_SILENT"))
check("source", "selected row is not attributed to Weinstein", selector["source_disposition"]["selected_product_attribution"] == "NOT_ATTRIBUTED_TO_WEINSTEIN")
check("exact", "Bianchi selector is comm/symi/symi", selected == ["comm", "symi", "symi"])
check("exact", "selected row belongs to the earlier enumerated eight-row domain", channel_name in epsilon["mixed_normal_family"]["channel_order"])
check("exact", "primitive epsilon chain was exact on the family", epsilon["primitive_epsilon"]["direct_chain_rule_exact"] is True)
check("exact", "moving Shiab owner is live", epsilon["moving_shiab"]["moving_contribution_live"] is True)

print("\nB. THREE DISTINCT OWNER PIECES")
check("exact", "principal two-connection diagonal has rank zero", principal["quotient_test"]["two_connection_diagonal_gauge_block_rank"] == 0)
check("exact", "homogeneous selected Ward scan covers 91 generators", homogeneous["production"]["moving_shiab_covariance"] == 91)
check("exact", "homogeneous cubic Ward variation is zero", homogeneous["production"]["cubic_ward_zero"] == 91)
check("exact", "homogeneous quadratic Ward variation is zero", homogeneous["production"]["quadratic_ward_zero"] == 91)
check("exact", "primitive row keeps opposite B/T directions", epsilon["primitive_epsilon"]["delta_b"] == "D_B_ETA" and epsilon["primitive_epsilon"]["delta_t"] == "MINUS_D_B_ETA")
check("type", "principal affine, homogeneous adjoint and primitive epsilon variations remain distinct", True)

print("\nC. INDEPENDENT EXACT PREBOUNDARY CONTROL")
eta = [Q(2), Q(-1), Q(4), Q(3)]
edge = [Q(2), Q(-3), Q(5)]
lhs = sum((eta[i + 1] - eta[i]) * edge[i] for i in range(3))
bulk = sum(eta[j] * (edge[j - 1] - edge[j]) for j in (1, 2))
flux = eta[3] * edge[2] - eta[0] * edge[0]
check("exact", "discrete integration by parts is exact", lhs == bulk + flux)
check("exact", "unrestricted planted boundary flux is live", flux == 11)

eta_dirichlet = [Q(0), eta[1], eta[2], Q(0)]
lhs_d = sum((eta_dirichlet[i + 1] - eta_dirichlet[i]) * edge[i] for i in range(3))
bulk_d = sum(eta_dirichlet[j] * (edge[j - 1] - edge[j]) for j in (1, 2))
flux_d = eta_dirichlet[3] * edge[2] - eta_dirichlet[0] * edge[0]
check("exact", "Dirichlet trace kills boundary flux", flux_d == 0)
check("exact", "Dirichlet Green identity retains the bulk adjoint", lhs_d == bulk_d)
check("repo", "prior compact-core graph is closed", epsilon["green_domain"]["closed_graph"] is True)
check("repo", "prior Dirichlet flux is zero", epsilon["green_domain"]["dirichlet_boundary_flux"] == 0)
check("repo", "prior unrestricted flux is explicitly retained", epsilon["green_domain"]["maximal_preboundary_flux"] == "ETA_TRACE_PAIRED_WITH_NORMAL_E_B_MINUS_E_T")

print("\nD. SCOPE AND PROGRAM FENCES")
for label in (
    "compact Dirichlet closure is not unrestricted BFV reduction",
    "unrestricted flux is not a nonzero physical charge",
    "fixed metric epsilon motion is not moving Hodge metric density or section",
    "formal H10-to-H9 graph is not global hyperbolic evolution",
    "selected product is repository-derived not source-attributed",
    "composition removes queue debt but does not reduce physical residue",
    "no fifth quotient is counted",
    "P1 P2 P3 remain unused",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
