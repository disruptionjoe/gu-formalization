#!/usr/bin/env python3
"""Fail-closed audit for CURRENT-STATE live-versus-historical frontier custody."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CURRENT = ROOT / "CURRENT-STATE.yaml"
REGISTRY = ROOT / "lab/process/current-frontier-semantic-currency.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_inputs() -> dict:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    basis = registry["basis"]
    return {
        "current": yaml.safe_load(CURRENT.read_text(encoding="utf-8")),
        "registry": registry,
        "agenda": json.loads((ROOT / basis["research_agenda"]["path"]).read_text()),
        "k696": json.loads(
            (ROOT / "lab/process/k696-k500-column-remainder-integration-compiler.json").read_text()
        ),
        "k697": json.loads(
            (ROOT / "lab/process/k697-k500-seed-complement-a-margin-compiler.json").read_text()
        ),
        "k698": json.loads(
            (ROOT / "lab/process/k698-k500-boundary-denominator-end-to-end-compiler.json").read_text()
        ),
        "k699": json.loads(
            (ROOT / "lab/process/k699-k500-approximate-form-a-margin-compiler.json").read_text()
        ),
        "k700": json.loads(
            (ROOT / "lab/process/k700-k500-cross-coupled-a-margin-compiler.json").read_text()
        ),
        "k701": json.loads(
            (ROOT / "lab/process/k701-k500-interval-boundary-denominator-compiler.json").read_text()
        ),
        "k702": json.loads(
            (ROOT / "lab/process/k702-k500-interval-cross-coupled-a-margin-compiler.json").read_text()
        ),
        "k703": json.loads(
            (ROOT / "lab/process/k703-k500-interval-complete-cancellation-floor-compiler.json").read_text()
        ),
        "k704": json.loads(
            (ROOT / "lab/process/k704-k500-coordinate-transported-boundary-margin-compiler.json").read_text()
        ),
        "k705": json.loads(
            (ROOT / "lab/process/k705-sc-act-06-reduced-symbol-projector-criterion.json").read_text()
        ),
        "k706": json.loads(
            (ROOT / "lab/process/k706-sc-act-06-euclidean-frame-transport.json").read_text()
        ),
        "k707": json.loads(
            (ROOT / "lab/process/k707-sc-act-06-coupled-symbol-homotopy-compiler.json").read_text()
        ),
        "k708": json.loads(
            (ROOT / "lab/process/k708-sc-act-06-euclidean-dewitt-signature-gate.json").read_text()
        ),
        "k709": json.loads(
            (ROOT / "lab/process/k709-sc-act-06-real-frame-euclideanization-obstruction.json").read_text()
        ),
        "k710": json.loads(
            (ROOT / "lab/process/k710-sc-act-06-null-symbol-ellipticity-boundary.json").read_text()
        ),
        "k711": json.loads(
            (ROOT / "lab/process/k711-sc-act-06-exact-complex-hodge-criterion.json").read_text()
        ),
        "k712": json.loads(
            (ROOT / "lab/process/k712-sc-act-06-auxiliary-positive-gauge-repair.json").read_text()
        ),
        "k713": json.loads(
            (ROOT / "lab/process/k713-sc-act-06-native-symmetry-gauge-metric-obstruction.json").read_text()
        ),
        "k714": json.loads(
            (ROOT / "lab/process/k714-sc-act-06-cartan-reduction-gauge-metric.json").read_text()
        ),
        "k715": json.loads(
            (ROOT / "lab/process/k715-sc-act-06-lorentz-natural-auxiliary-family.json").read_text()
        ),
        "k716": json.loads(
            (ROOT / "lab/process/k716-sc-act-06-compact-reduction-selection-boundary.json").read_text()
        ),
        "k717": json.loads(
            (ROOT / "lab/process/k717-sc-act-06-flat-euclidean-gimmel-germ.json").read_text()
        ),
        "k718": json.loads(
            (ROOT / "lab/process/k718-sc-act-06-bosonic-projected-principal-complex.json").read_text()
        ),
        "k719": json.loads(
            (ROOT / "lab/process/k719-sc-act-06-zero-fermion-full-symbol-reduction.json").read_text()
        ),
        "k720": json.loads(
            (ROOT / "lab/process/k720-sc-act-06-selected-i1b-euclidean-bosonic-symbol.json").read_text()
        ),
        "k721": json.loads(
            (ROOT / "lab/process/k721-sc-act-06-eq916-euclidean-fermion-symbol.json").read_text()
        ),
        "k722": json.loads(
            (ROOT / "lab/process/k722-sc-act-06-flat-full-symbol-obstruction.json").read_text()
        ),
        "k723": json.loads(
            (ROOT / "lab/process/k723-sc-act-06-t0-curvature-principal-invariance.json").read_text()
        ),
        "k724": json.loads(
            (ROOT / "lab/process/k724-sc-act-06-kappa-zero-order-ellipticity-obstruction.json").read_text()
        ),
        "k725": json.loads(
            (ROOT / "lab/process/k725-sc-act-06-current-bosonic-repair-input-gate.json").read_text()
        ),
        "k726": json.loads(
            (ROOT / "lab/process/k726-sc-act-06-homogeneous-nonzero-t-stationarity-obstruction.json").read_text()
        ),
        "k727": json.loads(
            (ROOT / "lab/process/k727-sc-act-06-algebraic-trace-repair-principal-invariance.json").read_text()
        ),
        "k728": json.loads(
            (ROOT / "lab/process/k728-sc-act-06-current-stationary-principal-input-gate.json").read_text()
        ),
        "k729": json.loads(
            (ROOT / "lab/process/k729-sc-act-06-serialized-i2b-principal-rank-ceiling.json").read_text()
        ),
        "k730": json.loads(
            (ROOT / "lab/process/k730-sc-act-06-i1b-i2b-flat-bosonic-repair-obstruction.json").read_text()
        ),
        "k731": json.loads(
            (ROOT / "lab/process/k731-sc-act-06-i1b-i2b-displayed-full-symbol-obstruction.json").read_text()
        ),
        "k732": json.loads(
            (ROOT / "lab/process/k732-sc-act-06-all-grade-connection-i2b-rank-ceiling.json").read_text()
        ),
        "k733": json.loads(
            (ROOT / "lab/process/k733-sc-act-06-all-grade-connection-bosonic-repair-obstruction.json").read_text()
        ),
        "k734": json.loads(
            (ROOT / "lab/process/k734-sc-act-06-all-grade-connection-displayed-full-symbol-obstruction.json").read_text()
        ),
        "k735": json.loads(
            (ROOT / "lab/process/k735-sc-act-06-source-low-grade-i2b-rank-ceiling.json").read_text()
        ),
        "k736": json.loads(
            (ROOT / "lab/process/k736-sc-act-06-source-low-grade-bosonic-repair-obstruction.json").read_text()
        ),
        "k737": json.loads(
            (ROOT / "lab/process/k737-sc-act-06-expanded-parent-dimension-threshold.json").read_text()
        ),
        "k738": json.loads(
            (ROOT / "lab/process/k738-sc-act-06-source-low-grade-displayed-full-symbol-obstruction.json").read_text()
        ),
        "k739": json.loads(
            (ROOT / "lab/process/k739-sc-act-06-expanded-action-parent-ownership.json").read_text()
        ),
        "k740": json.loads(
            (ROOT / "lab/process/k740-sc-act-06-expanded-principal-response-rank.json").read_text()
        ),
        "k741": json.loads(
            (ROOT / "lab/process/k741-sc-act-06-expanded-bosonic-repair-test.json").read_text()
        ),
        "k742": json.loads(
            (ROOT / "lab/process/k742-sc-act-06-expanded-displayed-full-symbol-test.json").read_text()
        ),
        "k743": json.loads(
            (ROOT / "lab/process/k743-sc-act-06-residual-square-image-cap.json").read_text()
        ),
        "k744": json.loads(
            (ROOT / "lab/process/k744-sc-act-06-full-trace-hessian-rank.json").read_text()
        ),
        "k745": json.loads(
            (ROOT / "lab/process/k745-sc-act-06-gauge-redundancy-obstruction.json").read_text()
        ),
        "k746": json.loads(
            (ROOT / "lab/process/k746-sc-act-06-residual-square-full-symbol-obstruction.json").read_text()
        ),
        "k747": json.loads(
            (ROOT / "lab/process/k747-sc-act-06-t0-response-invariance.json").read_text()
        ),
        "k748": json.loads(
            (ROOT / "lab/process/k748-sc-act-06-released-action-parent-inventory.json").read_text()
        ),
        "k749": json.loads(
            (ROOT / "lab/process/k749-sc-act-06-t0-full-symbol-obstruction.json").read_text()
        ),
        "k750": json.loads(
            (ROOT / "lab/process/k750-sc-act-06-successor-input-gate.json").read_text()
        ),
        "k751": json.loads(
            (ROOT / "lab/process/k751-sc-act-06-supercomplex-body-reduction.json").read_text()
        ),
        "k752": json.loads(
            (ROOT / "lab/process/k752-sc-act-06-nonzero-odd-saddle-body-obstruction.json").read_text()
        ),
        "k753": json.loads(
            (ROOT / "lab/process/k753-sc-act-06-even-condensate-reopener-audit.json").read_text()
        ),
        "k754": json.loads(
            (ROOT / "lab/process/k754-sc-act-06-nonzero-fermion-successor-gate.json").read_text()
        ),
        "k755": json.loads(
            (ROOT / "lab/process/k755-sc-act-06-cyclic-two-connection-square.json").read_text()
        ),
        "k756": json.loads(
            (ROOT / "lab/process/k756-sc-act-06-cyclic-adapter-linearization.json").read_text()
        ),
        "k757": json.loads(
            (ROOT / "lab/process/k757-sc-act-06-cyclic-adapter-current-carrier-composition.json").read_text()
        ),
        "k758": json.loads(
            (ROOT / "lab/process/k758-sc-act-06-cyclic-adapter-successor-gate.json").read_text()
        ),
        "k759": json.loads(
            (ROOT / "lab/process/k759-sc-act-06-even-spectator-rank-update-theorem.json").read_text()
        ),
        "k760": json.loads(
            (ROOT / "lab/process/k760-sc-act-06-derivative-condensate-cohomology-bound.json").read_text()
        ),
        "k761": json.loads(
            (ROOT / "lab/process/k761-sc-act-06-finite-even-extension-threshold.json").read_text()
        ),
        "k762": json.loads(
            (ROOT / "lab/process/k762-sc-act-06-even-owner-successor-gate.json").read_text()
        ),
        "k763": json.loads(
            (ROOT / "lab/process/k763-sc-act-06-finite-rank-even-owner-update.json").read_text()
        ),
        "k764": json.loads(
            (ROOT / "lab/process/k764-sc-act-06-scalar-metric-derivative-control.json").read_text()
        ),
        "k765": json.loads(
            (ROOT / "lab/process/k765-sc-act-06-scalar-metric-cohomology-bound.json").read_text()
        ),
        "k766": json.loads(
            (ROOT / "lab/process/k766-sc-act-06-derivative-even-successor-gate.json").read_text()
        ),
        "k767": json.loads(
            (ROOT / "lab/process/k767-sc-act-06-curvature-square-control.json").read_text()
        ),
        "k768": json.loads(
            (ROOT / "lab/process/k768-sc-act-06-curvature-square-rank-boundary.json").read_text()
        ),
        "k769": json.loads(
            (ROOT / "lab/process/k769-sc-act-06-curvature-square-cohomology-bound.json").read_text()
        ),
        "k770": json.loads(
            (ROOT / "lab/process/k770-sc-act-06-curvature-square-successor-gate.json").read_text()
        ),
        "k771": json.loads(
            (ROOT / "lab/process/k771-sc-act-06-positive-curvature-i1b-composition.json").read_text()
        ),
        "k772": json.loads(
            (ROOT / "lab/process/k772-sc-act-06-positive-curvature-total-complex.json").read_text()
        ),
        "k773": json.loads(
            (ROOT / "lab/process/k773-sc-act-06-positive-curvature-full-symbol.json").read_text()
        ),
        "k774": json.loads(
            (ROOT / "lab/process/k774-sc-act-06-positive-curvature-successor-gate.json").read_text()
        ),
        "k775": json.loads(
            (ROOT / "lab/process/k775-sc-act-06-residual-zero-variation-theorem.json").read_text()
        ),
        "k776": json.loads(
            (ROOT / "lab/process/k776-sc-act-06-homogeneous-residual-square-stationarity-closure.json").read_text()
        ),
        "k777": json.loads(
            (ROOT / "lab/process/k777-sc-act-06-nonzero-residual-hessian-split.json").read_text()
        ),
        "k778": json.loads(
            (ROOT / "lab/process/k778-sc-act-06-residual-stratum-successor-gate.json").read_text()
        ),
        "k779": json.loads(
            (ROOT / "lab/process/k779-sc-act-06-nonzero-residual-euler-image.json").read_text()
        ),
        "k780": json.loads(
            (ROOT / "lab/process/k780-sc-act-06-kernel-transverse-stationarity-obstruction.json").read_text()
        ),
        "k781": json.loads(
            (ROOT / "lab/process/k781-sc-act-06-residual-curvature-novelty.json").read_text()
        ),
        "k782": json.loads(
            (ROOT / "lab/process/k782-sc-act-06-nonzero-residual-two-jet-admission.json").read_text()
        ),
        "k783": json.loads(
            (ROOT / "lab/process/k783-sc-act-06-source-zero-locus-boundary.json").read_text()
        ),
        "k784": json.loads(
            (ROOT / "lab/process/k784-sc-act-06-i1b-i2b-action-sum-ownership-correction.json").read_text()
        ),
        "k785": json.loads(
            (ROOT / "lab/process/k785-sc-act-06-nonzero-residual-variational-salvage.json").read_text()
        ),
        "k786": json.loads(
            (ROOT / "lab/process/k786-sc-act-06-zero-residual-deformation-input-gate.json").read_text()
        ),
        "k787": json.loads(
            (ROOT / "lab/process/k787-sc-act-06-flat-zero-locus-custody.json").read_text()
        ),
        "k788": json.loads(
            (ROOT / "lab/process/k788-sc-act-06-direct-response-orbit-classification.json").read_text()
        ),
        "k789": json.loads(
            (ROOT / "lab/process/k789-sc-act-06-maximal-symmetry-budget.json").read_text()
        ),
        "k790": json.loads(
            (ROOT / "lab/process/k790-sc-act-06-flat-zero-locus-realization-gate.json").read_text()
        ),
        "k791": json.loads(
            (ROOT / "lab/process/k791-sc-act-06-released-first-order-row-inventory.json").read_text()
        ),
        "k792": json.loads(
            (ROOT / "lab/process/k792-sc-act-06-redundant-prolongation-kernel-theorem.json").read_text()
        ),
        "k793": json.loads(
            (ROOT / "lab/process/k793-sc-act-06-full-field-kernel-persistence.json").read_text()
        ),
        "k794": json.loads(
            (ROOT / "lab/process/k794-sc-act-06-released-flat-realization-closure.json").read_text()
        ),
        "k795": json.loads(
            (ROOT / "lab/process/k795-k500-complete-ab-decision-interface.json").read_text()
        ),
        "k796": json.loads(
            (ROOT / "lab/process/k796-k500-current-custody-product-countermodels.json").read_text()
        ),
        "k797": json.loads(
            (ROOT / "lab/process/k797-k500-current-custody-no-assembly-theorem.json").read_text()
        ),
        "k798": json.loads(
            (ROOT / "lab/process/k798-k500-current-packet-closure.json").read_text()
        ),
        "k799": json.loads(
            (ROOT / "lab/process/k799-sc-act-06-curved-t0-direct-response-transport.json").read_text()
        ),
        "k800": json.loads(
            (ROOT / "lab/process/k800-sc-act-06-curved-t0-full-field-kernel-persistence.json").read_text()
        ),
        "k801": json.loads(
            (ROOT / "lab/process/k801-sc-act-06-curvature-only-reopener-theorem.json").read_text()
        ),
        "k802": json.loads(
            (ROOT / "lab/process/k802-sc-act-06-certified-t0-family-closure.json").read_text()
        ),
        "k803": json.loads(
            (ROOT / "lab/process/k803-sc-act-06-nonzero-t-principal-invariance.json").read_text()
        ),
        "k804": json.loads(
            (ROOT / "lab/process/k804-sc-act-06-fixed-structure-full-field-kernel.json").read_text()
        ),
        "k805": json.loads(
            (ROOT / "lab/process/k805-sc-act-06-fixed-structure-symmetry-threshold.json").read_text()
        ),
        "k806": json.loads(
            (ROOT / "lab/process/k806-sc-act-06-nonzero-t-alone-closure.json").read_text()
        ),
        "k807": json.loads(
            (ROOT / "lab/process/k807-sc-act-06-comoving-principal-conjugacy.json").read_text()
        ),
        "k808": json.loads(
            (ROOT / "lab/process/k808-sc-act-06-comoving-full-field-kernel.json").read_text()
        ),
        "k809": json.loads(
            (ROOT / "lab/process/k809-sc-act-06-comoving-symmetry-quotient.json").read_text()
        ),
        "k810": json.loads(
            (ROOT / "lab/process/k810-sc-act-06-comoving-frame-closure.json").read_text()
        ),
        "k811": json.loads(
            (ROOT / "lab/process/k811-sc-act-06-relative-response-rank-budget.json").read_text()
        ),
        "k812": json.loads(
            (ROOT / "lab/process/k812-sc-act-06-relative-transverse-block.json").read_text()
        ),
        "k813": json.loads(
            (ROOT / "lab/process/k813-sc-act-06-relative-full-field-symmetry-budget.json").read_text()
        ),
        "k814": json.loads(
            (ROOT / "lab/process/k814-sc-act-06-relative-packet-gate.json").read_text()
        ),
        "k815": json.loads(
            (ROOT / "lab/process/k815-sc-act-06-zero-locus-tangent-compatibility.json").read_text()
        ),
        "k816": json.loads(
            (ROOT / "lab/process/k816-sc-act-06-response-symmetry-overlap.json").read_text()
        ),
        "k817": json.loads(
            (ROOT / "lab/process/k817-sc-act-06-finite-parameter-schur-gate.json").read_text()
        ),
        "k818": json.loads(
            (ROOT / "lab/process/k818-sc-act-06-uniform-covector-gate.json").read_text()
        ),
        "k819": json.loads(
            (ROOT / "lab/process/k819-sc-act-06-second-order-zero-locus-obstruction.json").read_text()
        ),
        "k820": json.loads(
            (ROOT / "lab/process/k820-sc-act-06-differentiated-complex-compatibility.json").read_text()
        ),
        "k821": json.loads(
            (ROOT / "lab/process/k821-sc-act-06-quotient-slice-equivalence.json").read_text()
        ),
        "k822": json.loads(
            (ROOT / "lab/process/k822-sc-act-06-joint-parameter-covector-uniformity.json").read_text()
        ),
        "k823": json.loads(
            (ROOT / "lab/process/k823-sc-act-06-stationarity-transport-gate.json").read_text()
        ),
        "k824": json.loads(
            (ROOT / "lab/process/k824-sc-act-06-mixed-symbol-schur-gate.json").read_text()
        ),
        "k825": json.loads(
            (ROOT / "lab/process/k825-sc-act-06-common-analytic-domain-gate.json").read_text()
        ),
        "k826": json.loads(
            (ROOT / "lab/process/k826-sc-act-06-relative-coefficient-ownership-gate.json").read_text()
        ),
        "k827": json.loads(
            (ROOT / "lab/process/k827-sc-act-06-regular-parameter-jet-invariance.json").read_text()
        ),
        "k828": json.loads(
            (ROOT / "lab/process/k828-sc-act-06-differentiable-domain-transport.json").read_text()
        ),
        "k829": json.loads(
            (ROOT / "lab/process/k829-sc-act-06-schur-complex-compatibility.json").read_text()
        ),
        "k830": json.loads(
            (ROOT / "lab/process/k830-sc-act-06-relative-family-admission-compiler.json").read_text()
        ),
        "k831": json.loads(
            (ROOT / "lab/process/k831-sc-act-06-noncompact-fredholm-boundary.json").read_text()
        ),
        "k832": json.loads(
            (ROOT / "lab/process/k832-sc-act-06-kuranishi-obstruction-gate.json").read_text()
        ),
        "k833": json.loads(
            (ROOT / "lab/process/k833-sc-act-06-quotient-regularity-gate.json").read_text()
        ),
        "k834": json.loads(
            (ROOT / "lab/process/k834-sc-act-06-rich-moduli-admission-compiler.json").read_text()
        ),
        "k835": json.loads(
            (ROOT / "lab/process/k835-sc-act-06-higher-order-kuranishi-obstruction.json").read_text()
        ),
        "k836": json.loads(
            (ROOT / "lab/process/k836-sc-act-06-smooth-flat-obstruction.json").read_text()
        ),
        "k837": json.loads(
            (ROOT / "lab/process/k837-sc-act-06-analytic-category-closure.json").read_text()
        ),
        "k838": json.loads(
            (ROOT / "lab/process/k838-sc-act-06-nonlinear-germ-admission-compiler.json").read_text()
        ),
        "k839": json.loads(
            (ROOT / "lab/process/k839-sc-act-06-finite-cutoff-limit-gate.json").read_text()
        ),
        "k840": json.loads(
            (ROOT / "lab/process/k840-sc-act-06-collapsing-nonlinear-radius.json").read_text()
        ),
        "k841": json.loads(
            (ROOT / "lab/process/k841-sc-act-06-analytic-hilbert-zero-accumulation.json").read_text()
        ),
        "k842": json.loads(
            (ROOT / "lab/process/k842-sc-act-06-infinite-dimensional-admission-compiler.json").read_text()
        ),
        "k843": json.loads(
            (ROOT / "lab/process/k843-sc-act-06-microlocal-cohomology-obstruction.json").read_text()
        ),
        "k844": json.loads(
            (ROOT / "lab/process/k844-sc-act-06-flat-symbol-sobolev-obstruction.json").read_text()
        ),
        "k845": json.loads(
            (ROOT / "lab/process/k845-sc-act-06-lower-order-repair-boundary.json").read_text()
        ),
        "k846": json.loads(
            (ROOT / "lab/process/k846-sc-act-06-flat-function-space-disposition.json").read_text()
        ),
        "k847": json.loads(
            (ROOT / "lab/process/k847-sc-act-06-quotient-repair-theorem.json").read_text()
        ),
        "k848": json.loads(
            (ROOT / "lab/process/k848-sc-act-06-rank-budget-overlap-countermodels.json").read_text()
        ),
        "k849": json.loads(
            (ROOT / "lab/process/k849-sc-act-06-exact-repair-certificate.json").read_text()
        ),
        "k850": json.loads(
            (ROOT / "lab/process/k850-sc-act-06-flat-quotient-repair-interface.json").read_text()
        ),
        "k851": json.loads(
            (ROOT / "lab/process/k851-sc-act-06-compact-cosphere-hodge-gap.json").read_text()
        ),
        "k852": json.loads(
            (ROOT / "lab/process/k852-sc-act-06-uniformity-failure-controls.json").read_text()
        ),
        "k853": json.loads(
            (ROOT / "lab/process/k853-sc-act-06-robust-exactness-radius.json").read_text()
        ),
        "k854": json.loads(
            (ROOT / "lab/process/k854-sc-act-06-robust-quotient-repair-certificate.json").read_text()
        ),
        "k855": json.loads(
            (ROOT / "lab/process/k855-sc-act-06-cohomology-bundle.json").read_text()
        ),
        "k856": json.loads(
            (ROOT / "lab/process/k856-sc-act-06-s13-stable-triviality.json").read_text()
        ),
        "k857": json.loads(
            (ROOT / "lab/process/k857-sc-act-06-abstract-orthogonal-repair.json").read_text()
        ),
        "k858": json.loads(
            (ROOT / "lab/process/k858-sc-act-06-topological-repair-disposition.json").read_text()
        ),
        "k859": json.loads(
            (ROOT / "lab/process/k859-sc-act-06-cohomology-rank-custody.json").read_text()
        ),
        "k860": json.loads(
            (ROOT / "lab/process/k860-sc-act-06-homogeneous-intertwiner-gate.json").read_text()
        ),
        "k861": json.loads(
            (ROOT / "lab/process/k861-sc-act-06-equivariant-triviality-countermodel.json").read_text()
        ),
        "k862": json.loads(
            (ROOT / "lab/process/k862-sc-act-06-naturality-repair-disposition.json").read_text()
        ),
        "k693": json.loads(
            (ROOT / "lab/process/k693-k500-graph-equivalent-column-compiler.json").read_text()
        ),
        "k694": json.loads(
            (ROOT / "lab/process/k694-k500-monotone-gram-closure-compiler.json").read_text()
        ),
        "k695": json.loads(
            (ROOT / "lab/process/k695-k500-friedrichs-defect-cofinal-compiler.json").read_text()
        ),
        "k690": json.loads(
            (ROOT / "lab/process/k690-k500-summable-core-density-compiler.json").read_text()
        ),
        "k691": json.loads(
            (ROOT / "lab/process/k691-k500-form-core-remainder-identification.json").read_text()
        ),
        "k692": json.loads(
            (ROOT / "lab/process/k692-k500-friedrichs-trace-anchor-compiler.json").read_text()
        ),
        "k687": json.loads(
            (ROOT / "lab/process/k687-k500-countable-closed-column-compiler.json").read_text()
        ),
        "k688": json.loads(
            (ROOT / "lab/process/k688-k500-partial-gram-bound-compiler.json").read_text()
        ),
        "k689": json.loads(
            (ROOT / "lab/process/k689-k500-gamma-anchor-propagation-compiler.json").read_text()
        ),
        "dispositions": json.loads(
            (ROOT / basis["phenomenology_disposition_register"]["path"]).read_text()
        ),
        "b2": json.loads((ROOT / basis["b2_frontier"]["path"]).read_text()),
        "qualification": json.loads(
            (ROOT / basis["w154_w229_qualification"]["path"]).read_text()
        ),
        "b5_artifact": (ROOT / registry["b5_agenda_currency"]["result_ref"]).read_text(),
        "k684": json.loads(
            (ROOT / "lab/process/k684-k500-closed-column-remainder-compiler.json").read_text()
        ),
        "k685": json.loads(
            (ROOT / "lab/process/k685-k500-component-square-budget-compiler.json").read_text()
        ),
        "k686": json.loads(
            (ROOT / "lab/process/k686-k500-weyl-gamma-field-variation-compiler.json").read_text()
        ),
        "k681": json.loads(
            (ROOT / "lab/process/k681-k500-monotone-remainder-form-compiler.json").read_text()
        ),
        "k682": json.loads(
            (ROOT / "lab/process/k682-k500-graph-relative-bounded-reduction-compiler.json").read_text()
        ),
        "k683": json.loads(
            (ROOT / "lab/process/k683-k500-weyl-target-level-robustness.json").read_text()
        ),
        "k678": json.loads(
            (ROOT / "lab/process/k678-k500-native-remainder-custody-audit.json").read_text()
        ),
        "k679": json.loads(
            (ROOT / "lab/process/k679-k500-closed-form-square-root-symmetry-compiler.json").read_text()
        ),
        "k680": json.loads(
            (ROOT / "lab/process/k680-k500-reference-base-floor-target.json").read_text()
        ),
        "k675": json.loads(
            (ROOT / "lab/process/k675-k500-seed-leakage-operator.json").read_text()
        ),
        "k676": json.loads(
            (ROOT / "lab/process/k676-k500-three-line-native-compression-criterion.json").read_text()
        ),
        "k677": json.loads(
            (ROOT / "lab/process/k677-k500-complement-cofinal-norm-certificate.json").read_text()
        ),
        "k673": json.loads(
            (ROOT / "lab/process/k673-k500-seed-line-leakage-custody.json").read_text()
        ),
        "k674": json.loads(
            (ROOT / "lab/process/k674-k500-compressed-leakage-complement-budget.json").read_text()
        ),
        "k671": json.loads(
            (ROOT / "lab/process/k671-k500-auxiliary-chart-a-margin-custody.json").read_text()
        ),
        "k672": json.loads(
            (ROOT / "lab/process/k672-k500-direct-a-cofinal-certificate.json").read_text()
        ),
        "k669": json.loads(
            (ROOT / "lab/process/k669-k500-leakage-remainder-factorization-bridge.json").read_text()
        ),
        "k670": json.loads(
            (ROOT / "lab/process/k670-k500-asymmetric-native-margin-target.json").read_text()
        ),
        "k667": json.loads(
            (ROOT / "lab/process/k667-k500-matched-trace-square-telescoping-bound.json").read_text()
        ),
        "k668": json.loads(
            (ROOT / "lab/process/k668-k500-rational-complete-floor-target.json").read_text()
        ),
        "k665": json.loads(
            (ROOT / "lab/process/k665-k500-parity-cofinal-effective-margin-composition.json").read_text()
        ),
        "k666": json.loads(
            (ROOT / "lab/process/k666-k500-complete-cancellation-floor-certificate.json").read_text()
        ),
        "k663": json.loads(
            (ROOT / "lab/process/k663-k500-sharp-cancellation-graph-floor.json").read_text()
        ),
        "k664": json.loads(
            (ROOT / "lab/process/k664-k500-cofinal-effective-margin-transfer.json").read_text()
        ),
        "k661": json.loads(
            (ROOT / "lab/process/k661-k500-friedrichs-reference-nonidentifiability.json").read_text()
        ),
        "k662": json.loads(
            (ROOT / "lab/process/k662-k500-reference-preserving-boundary-coordinate-group.json").read_text()
        ),
        "k659": json.loads(
            (ROOT / "lab/process/k659-k500-auxiliary-chart-floor-nonidentifiability.json").read_text()
        ),
        "k660": json.loads(
            (ROOT / "lab/process/k660-k500-boundary-translation-denominator-covariance.json").read_text()
        ),
        "k657": json.loads(
            (ROOT / "lab/process/k657-k500-boundary-weyl-base-floor-certificate.json").read_text()
        ),
        "k658": json.loads(
            (ROOT / "lab/process/k658-k500-cofinal-denominator-margin-transfer.json").read_text()
        ),
        "k655": json.loads(
            (ROOT / "lab/process/k655-k500-shifted-target-custody-obstruction.json").read_text()
        ),
        "k656": json.loads(
            (ROOT / "lab/process/k656-k500-base-floor-target-lift.json").read_text()
        ),
        "k653": json.loads((ROOT / "lab/process/k653-k500-shifted-schur-target-certificate.json").read_text()),
        "k654": json.loads((ROOT / "lab/process/k654-k500-all-order-shifted-schur-tail.json").read_text()),
        "k651": json.loads((ROOT / "lab/process/k651-k500-parity-tail-prefix-nonidentifiability.json").read_text()),
        "k652": json.loads((ROOT / "lab/process/k652-k500-all-order-parity-tail-certificate.json").read_text()),
        "k649": json.loads((ROOT / "lab/process/k649-k500-parity-cancellation-matching.json").read_text()),
        "k650": json.loads((ROOT / "lab/process/k650-k500-parity-cancelled-core-lower-interface.json").read_text()),
        "k647": json.loads((ROOT / "lab/process/k647-k500-common-domain-flavor-intertwiner.json").read_text()),
        "k648": json.loads((ROOT / "lab/process/k648-k500-native-parity-form-interface.json").read_text()),
        "k645": json.loads((ROOT / "lab/process/k645-k500-flavor-exchange-covariance.json").read_text()),
        "k646": json.loads((ROOT / "lab/process/k646-k500-parity-sector-lower-reduction.json").read_text()),
        "k643": json.loads((ROOT / "lab/process/k643-k500-bath-sector-boundary-reduction.json").read_text()),
        "k644": json.loads((ROOT / "lab/process/k644-k500-operator-block-lower-certificate.json").read_text()),
        "k641": json.loads((ROOT / "lab/process/k641-k500-spectator-boundary-type-audit.json").read_text()),
        "k642": json.loads((ROOT / "lab/process/k642-k500-operator-cancellation-graph-lower-theorem.json").read_text()),
        "k639": json.loads((ROOT / "lab/process/k639-k500-k179-channel-quotient.json").read_text()),
        "k640": json.loads((ROOT / "lab/process/k640-k500-cancellation-graph-lower-theorem.json").read_text()),
        "k637": json.loads((ROOT / "lab/process/k637-k77-natural-commutant-selection-ceiling.json").read_text()),
        "k638": json.loads((ROOT / "lab/process/k638-k500-vector-cancellation-coordinate.json").read_text()),
        "k635": json.loads((ROOT / "lab/process/k635-k77-full-commutant-source-stabilizer.json").read_text()),
        "k636": json.loads((ROOT / "lab/process/k636-k500-non-equivalent-cancellation-graph.json").read_text()),
        "k633": json.loads((ROOT / "lab/process/k633-k77-zero-form-polynomial-endomorphism-obstruction.json").read_text()),
        "k634": json.loads((ROOT / "lab/process/k634-k500-equivalent-domain-repair-obstruction.json").read_text()),
        "k631": json.loads((ROOT / "lab/process/k631-k77-owned-input-type-census.json").read_text()),
        "k632": json.loads((ROOT / "lab/process/k632-k77-owned-input-composition-closure.json").read_text()),
        "k629": json.loads((ROOT / "lab/process/k629-k77-domain-family-determinant-line-obstruction.json").read_text()),
        "k630": json.loads((ROOT / "lab/process/k630-k77-determinant-line-gauge-invariance.json").read_text()),
        "k627": json.loads((ROOT / "lab/process/k627-k77-block-gauge-positive-pairing-nonselection.json").read_text()),
        "k628": json.loads((ROOT / "lab/process/k628-k77-k622-domain-map-pairing-obstruction.json").read_text()),
        "k625": json.loads((ROOT / "lab/process/k625-k77-canonical-projector-pairing-realization.json").read_text()),
        "k626": json.loads((ROOT / "lab/process/k626-k77-ambient-pairing-embedding-gauge.json").read_text()),
        "k623": json.loads((ROOT / "lab/process/k623-k77-constructed-orbit-pairing-defect.json").read_text()),
        "k624": json.loads((ROOT / "lab/process/k624-k77-pairing-preserving-commutant-orbit-obstruction.json").read_text()),
        "k621": json.loads((ROOT / "lab/process/k621-k77-full-action-commutant-seed-adapter-obstruction.json").read_text()),
        "k622": json.loads((ROOT / "lab/process/k622-k77-domain-reparameterized-commutant-orbit.json").read_text()),
        "k619": json.loads((ROOT / "lab/process/k619-k77-zero-form-moving-graph-common-action-module.json").read_text()),
        "k620": json.loads((ROOT / "lab/process/k620-k77-action-functional-calculus-selection-obstruction.json").read_text()),
        "k617": json.loads((ROOT / "lab/process/k617-k77-moving-varpi-corrected-carrier-descent.json").read_text()),
        "k618": json.loads((ROOT / "lab/process/k618-k77-moving-varpi-corrected-action-hull.json").read_text()),
        "k615": json.loads((ROOT / "lab/process/k615-k77-zero-form-stationarity-obstruction.json").read_text()),
        "k616": json.loads((ROOT / "lab/process/k616-k77-unsplit-rank-one-transport-obstruction.json").read_text()),
        "k614": json.loads((ROOT / "lab/process/k614-k77-zero-form-corrected-carrier-injection.json").read_text()),
        "k612": json.loads((ROOT / "lab/process/k612-k139-quantitative-semibound-custody-audit.json").read_text()),
        "k613": json.loads((ROOT / "lab/process/k613-k77-central-parity-tensor-network-obstruction.json").read_text()),
    }


def audit(data: dict, check_digests: bool = True) -> list[str]:
    failures: list[str] = []
    current = data["current"]
    registry = data["registry"]
    surface = registry["surface_contract"]
    live = current.get(surface["live_key"])
    history = current.get(surface["history_key"])

    def check(ok: bool, message: str) -> None:
        if not ok:
            failures.append(message)

    check(isinstance(live, str) and bool(live.strip()), "live next_condition missing")
    check(isinstance(history, str) and bool(history.strip()), "prior_conditions history missing")
    check(registry["latest_gu_formalization_result"] ==
          "K859_K862_SC_ACT_06_NATURALITY_REPAIR_DISPOSITION_CURRENT",
          "latest GU result pointer moved")
    if isinstance(live, str):
        check("K859--K862 prove that the current 90124 value is only the lower endpoint" in live and
              "natural repair maps are determined by `SO(13)`-intertwiners" in live and
              "rank-91 product bundle" in live,
              "live K859--K862 naturality repair disposition missing")
        check("K855--K858 prove that once a complete real constant-rank old cohomology" in live and
              "rank-`h>=14` bundle over `S^13` is trivial" in live and
              "a chosen global frame to an owner" in live,
              "live K855--K858 topological repair disposition missing")
        check("K851--K854 require the next SC-ACT-06 repair attempt" in live and
              "uniform positive Hodge gap" in live and
              "K853's explicit radius" in live,
              "live K851--K854 robust quotient repair certificate missing")
        check("K847--K850 require the next SC-ACT-06 repair attempt" in live and
              "im(S_bar_q)=ker(tau_bar_q)" in live and
              "Do not credit raw" in live,
              "live K847--K850 exact quotient repair certificate missing")
        check("K843--K846 require the next SC-ACT-06 attempt" in live and
              "r+s>=90124" in live and
              "Do not retry lower-order" in live,
              "live K843--K846 flat function-space disposition missing")
        check("K839--K842 require a future SC-ACT-06 candidate" in live and
              "bounded or tame" in live and
              "all 30 rows" in live,
              "live K839--K842 infinite-dimensional admission gate missing")
        check("K835--K838 require a future SC-ACT-06 candidate" in live and
              "actual smooth obstruction germ" in live and
              "convergent analytic expansion" in live,
              "live K835--K838 nonlinear-germ category gate missing")
        check("K831--K834 require a future SC-ACT-06 candidate" in live and
              "closed Fredholm realization" in live and
              "proper stabilizer-typed local gauge quotient" in live,
              "live K831--K834 post-symbol moduli gate missing")
        check("K827--K830 require one source/action-owned normalized relative family" in live and
              "all eighteen admission rows" in live and
              "graph differentiability" in live,
              "live K827--K830 integrated relative-family gate missing")
        check("K823--K826 require a future relative candidate" in live and
              "stationary action jet" in live and
              "source/action-owned normalized family" in live,
              "live K823--K826 action/domain/ownership packet missing")
        check("K819--K822 require a future relative candidate" in live and
              "second-order" in live and
              "one common punctured interval" in live,
              "live K819--K822 relative-family coherence packet missing")
        check("K815--K818 require every future relative-coefficient candidate" in live and
              "pi_coker(J)b=0" in live and
              "uniform positive" in live,
              "live K815--K818 relative-germ admission packet missing")
        check("K811--K814 close only low-budget relative principal motion" in live and
              "r+s>=90124" in live and
              "passing that threshold does not prove ellipticity" in live,
              "live K811--K814 relative-response budget missing")
        check("K807--K810 close regular natural co-moving frame transport" in live and
              "90124-class lower bound" in live and
              "relative moving coefficients" in live,
              "live K807--K810 co-moving-frame closure missing")
        check("K803--K806 close nonzero background `T` alone" in live and
              "90124-class lower bound" in live and
              "genuinely moving principal coefficients" in live,
              "live K803--K806 nonzero-T-alone closure missing")
        check("K799--K802 close only the current released first-order packet" in live and
              "90124-class lower bound" in live and
              "nonzero-`T` or otherwise non-Levi-Civita" in live,
              "live K799--K802 certified-family closure missing")
        check("K795--K798 close only unchanged-current-custody assembly" in live and
              "all four A/B outcomes" in live and
              "genuinely new native A and B data" in live,
              "live K795--K798 current-custody packet closure missing")
        check("K791--K794 close K790's omitted-row audit" in live and
              "at least 90124 middle classes" in live and
              "genuinely different source-typed `Upsilon=0` germ" in live,
              "live K791--K794 released-flat-packet closure missing")
        check("K787--K790 close the current serialized K717/K788 flat packet" in live and
              "at least 90124 middle classes" in live and
              "omitted source-owned first-order row" in live,
              "live K787--K790 flat-packet realization gate missing")
        check("K783--K786 restore the direct SC-ACT-06 route" in live and
              "source-typed `Upsilon=0` background" in live and
              "source-selected relative coefficient" in live,
              "live K783--K786 source zero-locus route correction missing")
        check("K779--K782 close nonzero residual as a free stationarity" in live and
              "annihilates `ker(J)`" in live and "contracted residual curvature" in live,
              "retained K779--K782 conditional mathematics missing")
        check("K775--K778 close every fixed-pairing or finite-weight I2B rescue" in live and
              "Upsilon != 0" in live and "Nonzero residual alone" in live,
              "live K775--K778 residual-stratum gate missing")
        check("K771--K774 remove the fixed unit-weight identity-Cartan" in live and
              "8193/8196" in live and "candidate-kernel containment" in live,
              "live K771--K774 positive-curvature composition boundary missing")
        check("K767--K770 remove the native-pairing pure-curvature-square comparator" in live and
              "81927" in live and "positive Cartan" in live,
              "live K767--K770 curvature-square boundary missing")
        check("K763--K766 remove every Ward-compatible finite-rank old-block correction" in live and
              "r+m<98311" in live and "98297/98300" in live,
              "live K763--K766 finite-rank derivative-even boundary missing")
        check("K759--K762 remove every body-valued even spectator extension" in live and
              "m<98311" in live and "complete native K500 A/B certificates" in live,
              "live K759--K762 finite even spectator boundary missing")
        check("K755--K758 remove current-carrier cyclic path-adapter variations" in live and
              "complete native K500 A/B packet" in live and "98308/98311" in live,
              "live K755--K758 cyclic adapter boundary missing")
        check("K77 route" in live, "K77 nonfactorized route missing")
        check("K637" in live and "basis-naturality" in live,
              "K77 natural commutant selection ceiling missing")
        check("K633" in live and "scalar stabilizer" in live,
              "K77 polynomial source-seed stabilizer missing")
        check("K635" in live and "full-commutant" in live,
              "K77 full-commutant source stabilizer missing")
        check("outside `R[A]`" in live and "unselected full-commutant freedom" in live,
              "K77 post-commutant selected-input reopener missing")
        check("K631" in live and "K632" in live and "current typed operation closure" in live,
              "K77 current-owned-input closure missing")
        check("J0^* H_Sigma J0" in live and "X^* H_Sigma X" in live,
              "K77 nondegenerate pullback-form custody missing")
        check("K627" in live and "41,216" in live and "orthogonal reduction" in live,
              "K77 block-gauge pairing nonselection missing")
        check("K625" in live and "H_Sigma" in live,
              "K77 canonical projector point missing")
        check("K629--K630" in live, "K77 family-wide determinant-line predecessor missing")
        check("v0.163--v0.165" in live and "already banked" in live,
              "K77 completed unrestricted/BV route repeat fence missing")
        check("mixed Hessian" in live and "common BV/Green" in live,
              "K77 current reopener/ownership fence missing")
        check("universal" in live and "no-go" in live,
              "K77 relative-closure scope fence missing")
        check("K614" in live and "K617" in live and "K625" in live,
              "K77 current positive-content preservation missing")
        check("K596/K598" in live, "K77 unsplit-packet interface missing")
        check("nonzero stationary moving background" in live and "independently action-owned" in live,
              "K77 moving reopener missing")
        check("K596" in live and "K598" in live,
              "K77 discriminator/transport succession missing")
        check("K609" in live and "below 1/3" in live,
              "K500 complete leakage route missing")
        check("K612" in live and "cancelled-core" in live,
              "K500 quantitative-custody obstruction missing")
        check("K634" in live and "equivalent-norm" in live and "bounded-correlation" in live,
              "K500 equivalent-domain closure missing")
        check("K636" in live and "scalar domain" in live,
              "K500 constructed cancellation topology missing")
        check("K638" in live and "sixteen labels" in live,
              "K500 vector cancellation coordinate missing")
        check("K639" in live and "algebraically independent" in live and
              "spectator Fock" in live,
              "K500 actual K179 quotient missing")
        check("K641" in live and "spectator Fock" in live and "C^6 tensor H_spec" in live,
              "K500 native spectator type correction missing")
        check("K642" in live and "min(1/2,m-1/128)" in live and
              "min(1/2-alpha,m-delta-1/128)" in live,
              "K500 operator-valued graph lower theorem missing")
        check("K643" in live and "m=inf_n m_n" in live and "uniform tail" in live,
              "K500 bath-sector lower reduction missing")
        check("K644" in live and "lambda_min(C_n)" in live and "fifteen" in live,
              "K500 operator-block comparison certificate missing")
        check("K645" in live and "2,958" in live and "1,479" in live and
              "516" in live and "output-wedge" in live,
              "K500 exact flavor covariance missing")
        check("K646" in live and "m_n=min(m_n^+,m_n^-)" in live and
              "m=min(inf_n m_n^+,inf_n m_n^-)" in live,
              "K500 parity lower reduction missing")
        check("K647" in live and "D_K139=S Dom(H0)" in live and
              "same-form identity" in live and "J invariance" in live,
              "live native common-domain theorem missing")
        check("K648" in live and "product of channel swap and spectator swap" in live and
              "twelve" in live and "thirty" in live and
              "effective-margin obligation" in live,
              "live native parity-form interface or numerical handoff missing")
        check("K649" in live and "unique identity" in live and "harmonic divergent" in live,
              "live parity cancellation matching missing")
        check("K650" in live and "a_s,n,d_s,n" in live and "rho_s,n<=1" in live and
              "kappa_s,n" in live and "two-by-two comparison" in live,
              "live cancelled-quadrant lower interface missing")
        check("K651" in live and "orders two through twelve" in live and
              "finite prefix" in live,
              "live parity-tail prefix obstruction missing")
        check("K652" in live and "A_s(n),D_s(n)" in live and "K_s(n)" in live and
              "min(A_s(n)-K_s(n),D_s(n)-K_s(n))" in live,
              "live all-order parity-tail certificate missing")
        check("K653" in live and "target-relative" in live and
              "|c|^2<=(a-b)(d-b)" in live and "theta<=1" in live,
              "live shifted-Schur target certificate missing")
        check("K654" in live and "both parity signs" in live and
              "Synthetic" in live and "not a native floor" in live,
              "live all-order shifted-Schur composition missing")
        check("K655" in live and "same-interface control" in live and
              "first shifted diagonal fails" in live,
              "live shifted-target custody obstruction missing")
        check("K656" in live and "R0>=r0 M" in live and "b=r0-2" in live,
              "live base-floor target lift missing")
        check("K657--K658" in live and "D(-s)>=0" in live and "r0=-s" in live,
              "live boundary/Weyl floor certificate missing")
        check("K658" in live and "d_N>=eta_N" in live and "complete operator-norm" in live,
              "live cofinal denominator-margin transfer missing")
        check("K659" in live and "compensated auxiliary chart parameter" in live and
              "qualitative semiboundedness supplies existence but no number" in live,
              "live auxiliary-chart floor custody missing")
        check("K660" in live and "coordinate-invariant packet" in live and
              "D=W-M" in live and "joint boundary translation" in live,
              "live boundary-translation denominator covariance missing")
        check("K661" in live and "Friedrichs premise" in live and
              "norm-resolvent convergence" in live,
              "live Friedrichs-reference custody result missing")
        check("K662" in live and "D'=U^{-*}DU^{-1}" in live and
              "condition-number bounds" in live,
              "live reference-preserving coordinate group missing")
        check("K663" in live and "lambda_-" in live and "A B>beta^2" in live,
              "live sharp cancellation-graph floor missing")
        check("K664" in live and "A_lower,B_lower" in live and
              "spectator complements" in live,
              "live cofinal effective-margin transfer missing")
        check("K665" in live and "finite" in live and "tail lower" in live and
              "B_lower" in live,
              "live parity-cofinal effective-margin composition missing")
        check("K666" in live and "A_lower B_lower>beta_upper^2" in live and
              "determinant endpoint" in live,
              "live complete cancellation-floor certificate missing")
        check("K667" in live and "1/257<beta^2<2/513" in live and
              "K668" in live and "(A_lower-mu)(B_lower-mu)>=2/513" in live,
              "live matched-trace custody or rational floor target missing")
        check("K669" in live and "A>2/3" in live and
              "K670" in live and "B>=1/170" in live and "2/58653" in live,
              "live leakage bridge or asymmetric native-margin target missing")
        check("K671" in live and "auxiliary-chart" in live and
              "K672" in live and "kappa^2<(a_N-2/3)(a_tail-2/3)" in live,
              "live auxiliary-chart custody or direct-A certificate missing")
        check("K673" in live and "three" in live and "seed" in live and
              "K674" in live and "1/3-lambda_K609" in live and "1/100" in live,
              "live seed-line custody or compressed complement budget missing")
        check("K675" in live and "L_seed" in live and
              "K676" in live and "3-by-3 Gram" in live and
              "K677" in live and "u_N+v_N<=1/100" in live,
              "live seed operator, native comparison or complement compiler missing")
        check("K678" in live and "r_free" in live and
              "K679" in live and "closed" in live and
              "K680" in live and "341/170" in live,
              "live native remainder custody, square-root compiler or base-floor target missing")
        check("K681" in live and "finite-supremum" in live and
              "K682" in live and "complete relative form inequality" in live and
              "K683" in live and "complete Weyl difference budget" in live,
              "live monotone-form, graph-relative or Weyl robustness compiler missing")
        check("K693" in live and "two-sided graph equivalence" in live and
              "K694" in live and "dense-core positive partial-Gram" in live and
              "K695" in live and "complete Friedrichs domain" in live,
              "live graph-equivalence, Gram-closure or boundary-cofinal compiler missing")
        check("K696" in live and "column-to-`R` composition" in live and
              "K697" in live and "P_seed" in live and
              "K698" in live and "boundary chain" in live,
              "live K696--K698 end-to-end composition missing")
        check("K699" in live and "a`-relative form" in live and
              "K700" in live and "strict Schur" in live and
              "K701" in live and "outward boundary uncertainty" in live,
              "live K699--K701 robustness routes missing")
        check("K702" in live and "seed/complement/cross error" in live and
              "K703" in live and "floor above `5/8`" in live and
              "K704" in live and "reference-preserving `U,C` map" in live,
              "live K702--K704 robust composition routes missing")
        check("K705" in live and "rank thirteen" in live and
              "K706" in live and "invertible Euclidean chain transport" in live and
              "K707" in live and "Euler-after-gauge" in live,
              "live K705--K707 SC-ACT-06 symbol routes missing")
        check("K708" in live and "DeWitt `lambda=1/2` trace line" in live and
              "K709" in live and "real frame shortcut" in live and
              "K710" in live and "indefinite Hodge adjoint" in live,
              "live K708--K710 SC-ACT-06 signature boundary missing")
        check("K711" in live and "positive auxiliary metric" in live and
              "K712" in live and "bare exterior control" in live and
              "K713" in live and "full `O(13,1)`" in live,
              "live K711--K713 SC-ACT-06 auxiliary gauge route missing")
        check("K714" in live and "compact reduction" in live and
              "K715" in live and "null-direction Hodge ranks" in live and
              "K716" in live and "abstract auxiliary-metric feasibility" in live,
              "live K714--K716 SC-ACT-06 compact-reduction boundary missing")
        check("K717's flat Euclidean" in live and "K719 makes the full" in live and
              "block diagonal" in live,
              "live K717--K719 predecessor custody missing")
        check("K726" in live and "rank-one metric Euler" in live and
              "K727" in live and "derivative-free algebraic trace repair" in live and
              "K728" in live and "field two-jet" in live,
              "live K726--K728 stationary/principal input gate missing")
        check("K729--K731 reject the strongest possible use" in live and
              "196-direction" in live and "98274/106438" in live,
              "live K729--K731 serialized I2B repair ceiling missing")
        check("K735--K738 prove that the complete selected low-grade" in live and
              "96899/105063" in live and "113893" in live and "229477" in live,
              "live K735--K738 selected low-grade ceiling and parent threshold missing")
        check("K743--K746 close every residual-square repair" in live and
              "131074/131071" in live and "98308/98311" in live and
              "im(E_I1B)+im(J^T)" in live,
              "live K743--K746 same-response residual-square disposition missing")
        check("K732--K734 remain the sharper connection-only" in live and
              "97000/105164" in live and "98470/106634" in live,
              "live K732--K734 all-grade connection I2B ceiling missing")
        check("K720--K722 reject the frozen K132-selected I1B" in live and
              "98470" in live and "106634" in live and
              "displayed fermion candidate is exact" in live,
              "live K720--K722 SC-ACT-06 flat full-symbol obstruction missing")
        check("25/9" in live, "live residual target missing")
        check("shifted-form residual or spectral-error bound" in live,
              "live K152 claim ceiling missing")
        for marker in surface["stale_live_markers_forbidden"]:
            check(marker not in live, f"stale marker remains live: {marker}")
    if isinstance(history, str):
        check("25 terminal rows and 66 open rows" in history, "historical 25/66 condition lost")
        check("b2_selectable=false" in history, "historical B2 gate condition lost")
    summary = current.get("current_result", {}).get("summary", "")
    check("K851--K854 strengthen K849/K850's pointwise quotient repair criterion" in summary and
          "uniformly positive Hodge gap" in summary and
          "fourteen exact and fifteen robust" in summary,
          "current K851--K854 robust quotient repair result lost")
    check("K847--K850 sharpen K845's scalar repair budget" in summary and
          "im(S_bar)=ker(tau_bar)" in summary and
          "ten conjunctive" in summary,
          "current K847--K850 exact quotient repair result lost")
    check("K839--K842 close the finite-cutoff shortcut" in summary and
          "dense nonclosed range" in summary and
          "30-row interface" in summary,
          "current K839--K842 infinite-dimensional result lost")
    check("K835--K838 close the finite-jet shortcut" in summary and
          "complete formal data" in summary and
          "27-row interface" in summary,
          "current K835--K838 nonlinear-germ result lost")
    check("K831--K834 separate the source's claimed elliptic deformation complex" in summary and
          "quadratic Kuranishi obstruction" in summary and
          "25-row interface" in summary,
          "current K831--K834 result lost")
    check("K827--K830 compose the complete relative-family admission interface" in summary and
          "eighteen required rows" in summary and
          "current GU packet" in summary,
          "current K827--K830 result lost")
    check("K823--K826 complete four remaining typed admission seams" in summary and
          "B-C F^-1 D" in summary and
          "pointwise closed or self-adjoint operators need not share a domain" in summary and
          "SC-ACT-06 remains `ASSERTS`" in summary,
          "current K823--K826 action/domain/ownership result lost")
    check("K791--K794 complete the released first-order row audit" in summary and
          "delta Xi=D_omega(delta Upsilon)" in summary and
          "at least 90124 classes persist" in summary and
          "current released-source direct elliptic realization" in summary,
          "current K791--K794 released-flat-packet result lost")
    check("K787--K790 execute the corrected direct SC-ACT-06 route" in summary and
          "rank 122864" in summary and "at least 90124 middle classes" in summary and
          "rejects only the current serialized K717/K788 flat" in summary,
          "current K787--K790 flat-packet result lost")
    check("K783--K786 correct the source-object routing" in summary and
          "repository-conditional comparator" in summary and
          "Current custody supplies the claim and zero locus only" in summary,
          "current K783--K786 route-correction result lost")
    check("K771--K774 resolve the exact positive-curvature composition" in summary and
          "221189 and 221186" in summary and "8193 and 8196" in summary,
          "current K771--K774 positive-curvature composition result lost")
    check("K767--K770 test the first natural high-rank comparator" in summary and
          "196608" in summary and "81927" in summary,
          "current K767--K770 curvature-square result lost")
    check("K763--K766 extend the fixed-old-block spectator theorem" in summary and
          "rank(H)-rank(E)<=r+2m" in summary and "98297/98300" in summary and
          "r+m<98311" in summary,
          "current K763--K766 finite-rank derivative-even result lost")
    check("K759--K762 bound the complete fixed-old-block even-spectator repair class" in summary and
          "max(0,98308-m)" in summary and "max(0,98311-m)" in summary and
          "m<98311" in summary,
          "current K759--K762 finite even spectator result lost")
    check("K755--K758 construct and classify" in summary and
          "rank 13" in summary and "rank 14" in summary and
          "98308/98311" in summary,
          "current K755--K758 cyclic adapter result lost")
    check("K743--K746 close every residual-square repair" in summary and
          "131074/131071" in summary and "98308/98311" in summary and
          "122864/61439" in summary and "98308/106568" in summary,
          "current K743--K746 result lost")
    check("K739--K742 close the expanded-parent ownership/rank fork" in summary and
          "60594/113792" in summary and "122864/229376" in summary and
          "37775/45939" in summary,
          "current K739--K742 result lost")
    check("K735--K738 close the entire currently certified selected low-grade" in summary and
          "total dimension 1571" in summary and "96899/105063" in summary and
          "Spin 113893" in summary and "full-unitary 229477" in summary,
          "current K735--K738 result lost")
    check("K732--K734 test the strongest dimension-only use" in summary and
          "domain and rank 1470" in summary and "97000/105164" in summary and
          "98470/106634" in summary,
          "current K732--K734 result lost")
    check("K729--K731 test the strongest repair supplied" in summary and
          "any-weight serialized I2B" in summary and "98274" in summary and
          "106438" in summary,
          "current K729--K731 result lost")
    check("K726--K728 expose and close the cheapest current stationary-background" in summary,
          "current K726--K728 result lost")
    check("K723--K725 test every currently serialized alternative bosonic input" in summary,
          "current K723--K725 result lost")
    check("K720--K722 decide the first frozen full-symbol realization" in summary and
          "rank 192 and kernel 768 per block" in summary,
          "current K720--K722 result lost")
    check("K717--K719 construct the first native flat Euclidean germ" in summary,
          "current K717--K719 result lost")
    check("K714--K716 close the abstract ownership shape" in summary,
          "current K714--K716 result lost")
    check("K711--K713 refine K710's Euclidean-signature boundary" in summary,
          "current K711--K713 result lost")
    check("K708--K710 expose the Euclidean-signature datum" in summary,
          "current K708--K710 result lost")
    check("K705--K707 switch the active construction front" in summary,
          "current K705--K707 result lost")
    check("K702--K704 compose the post-K701 robustness results" in summary,
          "current K702--K704 result lost")
    check("K699--K701 replace three brittle exact-input seams" in summary,
          "current K699--K701 result lost")
    check("K696--K698 compose the post-K695 certificates" in summary,
          "current K696--K698 result lost")
    check("K693--K695 make the post-K692 native obligations" in summary,
          "current K693--K695 result lost")
    check("K684--K686 turn the two K681--K683 abstract routes" in summary,
          "current K684--K686 result lost")
    check("K681--K683 convert the K678--K680 missing-input frontier" in summary,
          "current K681--K683 result lost")
    check("K678--K680 resolve the next native-input fork" in summary,
          "current K678--K680 result lost")
    check("K675--K677 turn K674's two abstract missing inputs" in summary,
          "current K675--K677 result lost")
    check("K673--K674 resolve how K609 can honestly contribute" in summary,
          "current K673--K674 result lost")
    check("K671--K672 close the auxiliary-chart shortcut" in summary,
          "current K671--K672 result lost")
    check("K669--K670 expose the exact K609-to-A bridge" in summary,
          "current K669--K670 result lost")
    check("K667--K668 close the matched-trace custody mismatch" in summary,
          "current K667--K668 result lost")
    check("K665--K666 close the abstract composition" in summary,
          "current K665--K666 result lost")
    check("K663--K664 sharpen the independent K642 complete-domain lower route" in summary,
          "current K663--K664 result lost")
    check("K661--K662 close the Friedrichs-reference custody inference" in summary,
          "current K661--K662 result lost")
    check("K659--K660 close the auxiliary-chart custody question" in summary,
          "current K659--K660 result lost")
    check("K657--K658 convert K656's missing base floor" in summary,
          "current K657--K658 result lost")
    check("K655--K656 resolve the target-selection question" in summary,
          "current K655--K656 result lost")
    check("K653--K654 add a target-relative all-order route" in summary,
          "current K653--K654 result lost")
    check("K651--K652 close the finite-prefix tail-identifiability question" in summary,
          "current K651--K652 result lost")
    check("K649--K650 remain the direct predecessors" in summary,
          "K649--K650 predecessor result lost")
    check("K647--K648 remain the direct predecessors" in summary,
          "K647--K648 predecessor result lost")
    check("K645--K646 remain the direct predecessors" in summary,
          "K645--K646 predecessor result lost")
    check("K643--K644 remain the direct predecessors" in summary,
          "current K643--K644 result lost")
    check("K641--K642 remain the direct predecessors" in summary,
          "current K641--K642 result lost")
    check("K639--K640 remain the direct predecessors" in summary,
          "K639--K640 predecessor result lost")
    check("K637--K638 remain earlier direct predecessors" in summary,
          "K637--K638 predecessor result lost")
    check("K635--K636 remain earlier predecessors" in summary,
          "K635--K636 predecessor result lost")
    check("K633--K634 advance two independent post-K632 fronts" in summary,
          "K633--K634 predecessor result lost")
    check("K631--K632 prove that the post-K630 demand for new owned input" in summary,
          "current K631--K632 result lost")
    check("K629--K630 close the alternative K622 domain-map family" in summary,
          "current K629--K630 predecessor lost")
    check("K627--K628 sharpen the ambient-pairing result" in summary,
          "current K627--K628 result lost")
    check("K625--K626 resolve the ambient-pairing seam" in summary,
          "current K625--K626 result lost")
    check("K623--K624 close the projector-induced pairing repair" in summary,
          "current K623--K624 result lost")
    check("K621--K622 classify the complete nonpolynomial commutant escape" in summary,
          "current K621--K622 result lost")
    check("K619--K620 compose K614's source-owned zero-form seed" in summary,
          "current K619--K620 result lost")
    check("K617--K618 test the strongest already-owned moving-background candidate" in summary,
          "current K617--K618 result lost")
    check("K615--K616 close K614's natural frozen-background successor" in summary,
          "current K615--K616 result lost")
    check("K614 closes the map half of K613's cheapest odd-data reopener" in summary,
          "current K614 result lost")
    check("K612--K613 close two post-K611/K610 extraction routes" in summary,
          "current K612--K613 result lost")
    check("no named" in summary and "floor" in summary,
          "current claim ceiling lost")

    question = current.get("current_question", "")
    check(
        "K859--K862 separate ordinary high-rank bundle triviality" in data["agenda"].get("latest_result_2026_10_02_k859_k862", "")
        and "rank-91 ordinary trivial bundle" in data["agenda"].get("latest_result_2026_10_02_k859_k862", "")
        and "SC-ACT-06 remains ASSERTS" in data["agenda"].get("latest_result_2026_10_02_k859_k862", ""),
        "agenda K859--K862 result is not current",
    )
    check(
        "K859--K862 replace ordinary bundle triviality" in question
        and "SO(13)" in question
        and "im(S_0)=ker(tau_0)" in question,
        "current question lost K859--K862 naturality repair interface",
    )
    check(
        "K855--K858 close the purely topological obstruction route" in data["agenda"].get("latest_result_2026_10_02_k855_k858", "")
        and "rank h>=14 bundle is trivial" in data["agenda"].get("latest_result_2026_10_02_k855_k858", "")
        and "SC-ACT-06 remains ASSERTS" in data["agenda"].get("latest_result_2026_10_02_k855_k858", ""),
        "agenda K855--K858 result is not current",
    )
    check(
        "K851--K854 upgrade the exact quotient-repair interface" in question
        and "uniform positive Hodge gap" in question
        and "K853's explicit radius" in question,
        "current question lost K851--K854 robust quotient repair interface",
    )
    check(
        "K851--K854 upgrade K849/K850's pointwise quotient repair interface" in data["agenda"].get("latest_result_2026_10_02_k851_k854", "")
        and "fourteen exact and fifteen robust" in data["agenda"].get("latest_result_2026_10_02_k851_k854", "")
        and "SC-ACT-06 remains ASSERTS" in data["agenda"].get("latest_result_2026_10_02_k851_k854", ""),
        "agenda K851--K854 result is not current",
    )
    check(
        "K847--K850 replace the coarse raw-rank reopener" in question
        and "im(S_bar_q)=ker(tau_bar_q)" in question
        and "cannot substitute for quotient-effective ranks" in question,
        "current question lost K847--K850 exact quotient repair interface",
    )
    check(
        "K847--K850 sharpen K845's necessary raw-rank budget" in data["agenda"].get("latest_result_2026_10_02_k847_k850", "")
        and "ten conjunctive" in data["agenda"].get("latest_result_2026_10_02_k847_k850", "")
        and "SC-ACT-06 remains ASSERTS" in data["agenda"].get("latest_result_2026_10_02_k847_k850", ""),
        "agenda K847--K850 result is not current",
    )
    check(
        "K843--K846 turn the current flat packet's symbol count" in question
        and "at least 90124 middle symbol classes" in question
        and "not a global SC-ACT-06 verdict" in question,
        "current question lost K843--K846 flat microlocal disposition",
    )
    check(
        "K843--K846 switch from generic admission-distance accumulation" in data["agenda"].get("latest_result_2026_10_02_k843_k846", "")
        and "r+s>=90124" in data["agenda"].get("latest_result_2026_10_02_k843_k846", "")
        and "SC-ACT-06 remain unadjudicated" in data["agenda"].get("latest_result_2026_10_02_k843_k846", ""),
        "agenda K843--K846 result is not current",
    )
    check(
        "K839--K842 make the nonlinear rich-moduli obligation genuinely infinite" in question
        and "completed function-space topology" in question
        and "uniform through the actual approximation limit" in question,
        "current question lost K839--K842 infinite-dimensional gates",
    )
    check(
        "K839--K842 close the finite-cutoff shortcut" in data["agenda"].get("latest_result_2026_10_02_k839_k842", "")
        and "30 rows" in data["agenda"].get("latest_result_2026_10_02_k839_k842", "")
        and "SC-ACT-06 remains ASSERTS" in data["agenda"].get("latest_result_2026_10_02_k839_k842", ""),
        "agenda K839--K842 result is not current",
    )
    check(
        "K835--K838 make the nonlinear-germ obligation category-sensitive" in question
        and "complete formal Taylor series" in question
        and "convergent analytic expansion" in question,
        "current question lost K835--K838 nonlinear-germ category gates",
    )
    check(
        "K835--K838 close the nonlinear-germ category seam" in data["agenda"].get("latest_result_2026_10_02_k835_k838", "")
        and "27 rows" in data["agenda"].get("latest_result_2026_10_02_k835_k838", "")
        and "SC-ACT-06 remains ASSERTS" in data["agenda"].get("latest_result_2026_10_02_k835_k838", ""),
        "agenda K835--K838 result is not current",
    )
    check(
        "K831--K834 make explicit that a source-owned exact symbol complex" in question
        and "closed Fredholm realization" in question
        and "proper slice with stabilizer/orbit type" in question,
        "current question lost K831--K834 post-symbol moduli gates",
    )
    check(
        "K831--K834 separate symbol ellipticity" in data["agenda"].get("latest_result_2026_10_02_k831_k834", "")
        and "25 rows" in data["agenda"].get("latest_result_2026_10_02_k831_k834", "")
        and "SC-ACT-06 remains ASSERTS" in data["agenda"].get("latest_result_2026_10_02_k831_k834", ""),
        "agenda K831--K834 result is not current",
    )
    check(
        "K827--K830 make the future relative-family decision conjunctive" in question
        and "graph-differentiable transports" in question
        and "eighteen-row compiler" in question,
        "current question lost K827--K830 integrated admission gates",
    )
    check(
        "K827--K830 compose the relative-family admission interface" in data["agenda"].get("latest_result_2026_10_02_k827_k830", "")
        and "graph-differentiable domain transport" in data["agenda"].get("latest_result_2026_10_02_k827_k830", "")
        and "SC-ACT-06 remains ASSERTS" in data["agenda"].get("latest_result_2026_10_02_k827_k830", ""),
        "agenda K827--K830 result is not current",
    )
    check(
        "K823--K826 add the action and analytic typing" in question
        and "two-sided mixed Schur complement" in question
        and "source/action-owned normalized family" in question,
        "current question lost K823--K826 action/domain/ownership gates",
    )
    check(
        "K823--K826 complete four remaining typed admission seams" in data["agenda"].get("latest_result_2026_10_02_k823_k826", "")
        and "pointwise self-adjointness" in data["agenda"].get("latest_result_2026_10_02_k823_k826", "")
        and "SC-ACT-06 remains ASSERTS" in data["agenda"].get("latest_result_2026_10_02_k823_k826", ""),
        "agenda K823--K826 result is not current",
    )
    check(
        "K819--K822 make the relative-family coherence test explicit" in question
        and "Delta G0+J0 Gdot=0" in question
        and "one common punctured interval" in question,
        "current question lost K819--K822 relative-family coherence gates",
    )
    check(
        "K819--K822 add four coherence gates" in data["agenda"].get("latest_result_2026_10_02_k819_k822", "")
        and "arbitrary extra rows" in data["agenda"].get("latest_result_2026_10_02_k819_k822", "")
        and "SC-ACT-06 remains ASSERTS" in data["agenda"].get("latest_result_2026_10_02_k819_k822", ""),
        "agenda K819--K822 result is not current",
    )
    check(
        "K815--K818 make the future SC-ACT-06 relative-germ gate executable" in question
        and "pi_coker(J)b=0" in question
        and "uniform Euclidean-sphere gap" in question,
        "current question lost K815--K818 relative-germ admission discriminators",
    )
    check(
        "K815--K818 turn the future relative-germ packet" in data["agenda"].get("latest_result_2026_10_02_k815_k818", "")
        and "dim K-rank(tau)-dim G" in data["agenda"].get("latest_result_2026_10_02_k815_k818", "")
        and "SC-ACT-06 remains ASSERTS" in data["agenda"].get("latest_result_2026_10_02_k815_k818", ""),
        "agenda K815--K818 result is not current",
    )
    check(
        "K811--K814 quantify every genuinely relative principal-response repair" in question
        and "max(0,90124-r-s)" in question
        and "necessary but not sufficient" in question,
        "current question lost K811--K814 relative-response budget",
    )
    check(
        "K811--K814 price every genuinely relative principal-response repair" in data["agenda"].get("latest_result_2026_10_02_k811_k814", "")
        and "r+s>=90124 is necessary" in data["agenda"].get("latest_result_2026_10_02_k811_k814", "")
        and "SC-ACT-06 remains ASSERTS" in data["agenda"].get("latest_result_2026_10_02_k811_k814", ""),
        "agenda K811--K814 result is not current",
    )
    check(
        "K807--K810 close regular co-moving metric/epsilon/Shiab/Hodge frame motion" in question
        and "kernel 106512" in question
        and "relative coefficient motion" in question,
        "current question lost K807--K810 co-moving-frame closure",
    )
    check(
        "K807--K810 close only regular natural co-moving metric/epsilon/Shiab/Hodge frame transport" in data["agenda"].get("latest_result_2026_10_02_k807_k810", "")
        and "rank 122864 and kernel 106512" in data["agenda"].get("latest_result_2026_10_02_k807_k810", "")
        and "SC-ACT-06 remains ASSERTS" in data["agenda"].get("latest_result_2026_10_02_k807_k810", ""),
        "agenda K807--K810 result is not current",
    )
    check(
        "K803--K806 close nonzero background `T` alone" in question
        and "kernel remains 106512" in question
        and "owned symmetry image spanning the kernel" in question,
        "current question lost K803--K806 nonzero-T-alone closure",
    )
    check(
        "K803--K806 close nonzero background T alone" in data["agenda"].get("latest_result_2026_10_02_k803_k806", "")
        and "rank 122864 and kernel 106512" in data["agenda"].get("latest_result_2026_10_02_k803_k806", "")
        and "SC-ACT-06 remains ASSERTS" in data["agenda"].get("latest_result_2026_10_02_k803_k806", ""),
        "agenda K803--K806 result is not current",
    )
    check(
        "K799--K802 close the curvature-only reopener" in question
        and "kernel 106512" in question
        and "at least 90124 middle classes" in question,
        "current question lost K799--K802 certified-family closure",
    )
    check(
        "K799--K802 close only the current released first-order Upsilon packet" in data["agenda"].get("latest_result_2026_10_02_k799_k802", "")
        and "rank 122864 and kernel 106512" in data["agenda"].get("latest_result_2026_10_02_k799_k802", "")
        and "SC-ACT-06 remains ASSERTS" in data["agenda"].get("latest_result_2026_10_02_k799_k802", ""),
        "agenda K799--K802 result is not current",
    )
    check(
        "K795--K798 close only the attempt to assemble" in question
        and "every A/B truth pair" in question
        and "genuinely new native same-domain remainder/complement data" in question,
        "current question lost K795--K798 current-custody packet closure",
    )
    check(
        "K795--K798 close only the attempt to assemble" in data["agenda"].get("latest_result_2026_10_02_k795_k798", "")
        and "every A/B truth pair" in data["agenda"].get("latest_result_2026_10_02_k795_k798", "")
        and "future native K500" in data["agenda"].get("latest_result_2026_10_02_k795_k798", "")
        and "No protected conclusion moves" in data["agenda"].get("latest_result_2026_10_02_k795_k798", ""),
        "agenda K795--K798 result is not current",
    )
    check(
        "K791--K794 complete K790's released first-order row audit" in data["agenda"].get("latest_result_2026_10_02_k791_k794", "")
        and "106512-dimensional kernel" in data["agenda"].get("latest_result_2026_10_02_k791_k794", "")
        and "90124" in data["agenda"].get("latest_result_2026_10_02_k791_k794", "")
        and "SC-ACT-06 remains ASSERTS" in data["agenda"].get("latest_result_2026_10_02_k791_k794", ""),
        "agenda K791--K794 result is not current",
    )
    check(
        "repository-constructed local source-typed Upsilon=0 background" in data["agenda"].get("latest_result_2026_10_02_k787_k790", "")
        and "rank 122864" in data["agenda"].get("latest_result_2026_10_02_k787_k790", "")
        and "90124" in data["agenda"].get("latest_result_2026_10_02_k787_k790", "")
        and "SC-ACT-06 remains ASSERTS" in data["agenda"].get("latest_result_2026_10_02_k787_k790", ""),
        "agenda K787--K790 result is not current",
    )
    check(
        "K783--K786 require one source-typed" in question
        and "complete first-order Euclidean deformation" in question
        and "separate conditional action problem" in question,
        "current question lost K783--K786 zero-locus gate",
    )
    check(
        "binds the claim to the first-order zero locus" in data["agenda"].get("latest_result_2026_10_01_k783_k786", "")
        and "repository-conditional comparator" in data["agenda"].get("latest_result_2026_10_01_k783_k786", "")
        and "SC-ACT-06 remains ASSERTS" in data["agenda"].get("latest_result_2026_10_01_k783_k786", ""),
        "agenda K783--K786 result is not current",
    )
    check(
        "K779--K782 sharpen the first admissible nonzero-residual" in question
        and "kernel-transverse" in question and "contracted residual curvature" in question,
        "current question lost K779--K782 nonzero-residual admission gate",
    )
    check(
        "dI2B=J^*Q Upsilon remains inside im(J^*)" in data["agenda"].get("latest_result_2026_10_01_k779_k782", "")
        and "transverse to im(J^*)" in data["agenda"].get("latest_result_2026_10_01_k779_k782", "")
        and "nonzero C_U alone" in data["agenda"].get("latest_result_2026_10_01_k779_k782", ""),
        "agenda K779--K782 result is not current",
    )
    check(
        "K775--K778 split the source-owned residual-square" in question
        and "D2Upsilon" in question and "Do not retry K726" in question,
        "current question lost K775--K778 residual-stratum gate",
    )
    check(
        "dI2B=J^*Q Upsilon" in data["agenda"].get("latest_result_2026_10_01_k775_k778", "")
        and "metric Euler rank remains one" in data["agenda"].get("latest_result_2026_10_01_k775_k778", "")
        and "nonzero residual alone" in data["agenda"].get("latest_result_2026_10_01_k775_k778", ""),
        "agenda K775--K778 result is not current",
    )
    check(
        "K771--K774 close the unit-weight identity-Cartan" in question
        and "8193/8196" in question and "additional metric-coupled classes" in question,
        "current question lost K771--K774 composition boundary",
    )
    check(
        "ranks are 221183" in data["agenda"].get("latest_result_2026_10_01_k771_k774", "")
        and "8193/8196" in data["agenda"].get("latest_result_2026_10_01_k771_k774", "")
        and "q-lambda candidate" in data["agenda"].get("latest_result_2026_10_01_k771_k774", ""),
        "agenda K771--K774 result is not current",
    )
    check(
        "K767--K770 close the natural full-connection" in question
        and "81927" in question and "positive Cartan" in question,
        "current question lost K767--K770 boundary",
    )
    check(
        "rank 212992" in data["agenda"].get("latest_result_2026_10_01_k767_k770", "")
        and "196608" in data["agenda"].get("latest_result_2026_10_01_k767_k770", "")
        and "81927" in data["agenda"].get("latest_result_2026_10_01_k767_k770", ""),
        "agenda K767--K770 result is not current",
    )
    check(
        "K763--K766 prove that a Ward-compatible correction" in question
        and "r+m<98311" in question and "98297/98300" in question,
        "current question lost K763--K766 boundary",
    )
    check(
        "rank-r Ward-compatible correction" in data["agenda"].get("latest_result_2026_10_01_k763_k766", "")
        and "98297/98300" in data["agenda"].get("latest_result_2026_10_01_k763_k766", "")
        and "necessary only" in data["agenda"].get("latest_result_2026_10_01_k763_k766", ""),
        "agenda K763--K766 result is not current",
    )
    check(
        "rank by at most 2m" in data["agenda"].get("latest_result_2026_10_01_k759_k762", "")
        and "98307/98310" in data["agenda"].get("latest_result_2026_10_01_k759_k762", "")
        and "not sufficient" in data["agenda"].get("latest_result_2026_10_01_k759_k762", ""),
        "agenda K759--K762 result is not current",
    )
    check(
        "exact square" in data["agenda"].get("latest_result_2026_10_01_k755_k758", "")
        and "rank 13" in data["agenda"].get("latest_result_2026_10_01_k755_k758", "")
        and "98308/98311" in data["agenda"].get("latest_result_2026_10_01_k755_k758", ""),
        "agenda K755--K758 result is not current",
    )
    check(
        "finite-free supercomplex" in data["agenda"].get("latest_result_2026_10_01_k751_k754", "")
        and "98308/98311" in data["agenda"].get("latest_result_2026_10_01_k751_k754", "")
        and "intrinsic metric equation" in data["agenda"].get("latest_result_2026_10_01_k751_k754", ""),
        "agenda K751--K754 result is not current",
    )
    check(
        "131074/131071" in data["agenda"].get("latest_result_2026_10_01_k747_k750", "")
        and "98308/98311" in data["agenda"].get("latest_result_2026_10_01_k747_k750", "")
        and "source-silent and unbuilt" in data["agenda"].get("latest_result_2026_10_01_k747_k750", ""),
        "agenda K747--K750 result is not current",
    )
    check(
        "H_Q=J^T Q J" in data["agenda"].get("latest_result_2026_10_01_k743_k746", "")
        and "131074/131071" in data["agenda"].get("latest_result_2026_10_01_k743_k746", "")
        and "98308/106568" in data["agenda"].get("latest_result_2026_10_01_k743_k746", ""),
        "agenda K743--K746 result is not current",
    )
    check(
        "full unprojected 16384-coefficient" in data["agenda"].get("latest_result_2026_10_01_k739_k742", "")
        and "650, 60594 and 122864" in data["agenda"].get("latest_result_2026_10_01_k739_k742", "")
        and "37775/45939" in data["agenda"].get("latest_result_2026_10_01_k739_k742", ""),
        "agenda K739--K742 result is not current",
    )
    check(
        "complete selected low-grade source-native tangent is 1571" in data["agenda"].get("latest_result_2026_10_01_k735_k738", "")
        and "at least 96899/105063" in data["agenda"].get("latest_result_2026_10_01_k735_k738", "")
        and "113893 and 229477" in data["agenda"].get("latest_result_2026_10_01_k735_k738", ""),
        "agenda K735--K738 result is not current",
    )
    check(
        "domain and rank are 1470" in data["agenda"].get("latest_result_2026_10_01_k732_k734", "")
        and "at least 97000/105164" in data["agenda"].get("latest_result_2026_10_01_k732_k734", "")
        and "98470/106634" in data["agenda"].get("latest_result_2026_10_01_k732_k734", ""),
        "agenda K732--K734 result is not current",
    )
    check(
        "bank has dimension 196" in data["agenda"].get("latest_result_2026_10_01_k729_k731", "")
        and "at least 98274/106438" in data["agenda"].get("latest_result_2026_10_01_k729_k731", "")
        and "flat selected-I1B plus any-weight serialized-I2B" in data["agenda"].get("latest_result_2026_10_01_k729_k731", ""),
        "agenda K729--K731 result is not current",
    )
    check(
        "first-action density 7*kappa_1^3/18252" in data["agenda"].get("latest_result_2026_10_01_k726_k728", "")
        and "rank-91 lower-order moving-epsilon cross" in data["agenda"].get("latest_result_2026_10_01_k726_k728", "")
        and "no current serialized packet passes both stationarity and principal exactness" in data["agenda"].get("latest_result_2026_10_01_k726_k728", ""),
        "agenda K726--K728 result is not current",
    )
    check(
        "curvature changes subprincipal or lower-order transport" in data["agenda"].get("latest_result_2026_09_30_k723_k725", "")
        and "zero-order involution" in data["agenda"].get("latest_result_2026_09_30_k723_k725", "")
        and "current serialized candidates therefore supply no replacement bosonic principal symbol" in data["agenda"].get("latest_result_2026_09_30_k723_k725", ""),
        "agenda K723--K725 result is not current",
    )
    check(
        "Euler ranks 130912 and 122748" in data["agenda"].get("latest_result_2026_09_30_k720_k722", "")
        and "rank 192 and kernel 768 per block" in data["agenda"].get("latest_result_2026_09_30_k720_k722", "")
        and "frozen flat selected-I1B realization is rejected as elliptic" in data["agenda"].get("latest_result_2026_09_30_k720_k722", ""),
        "agenda K720--K722 result is not current",
    )
    check(
        "local source-typed flat Euclidean Y=Met(X) germ" in data["agenda"].get("latest_result_2026_09_30_k717_k719", "")
        and "zero mixed Hessian" in data["agenda"].get("latest_result_2026_09_30_k717_k719", "")
        and "both complete action-owned diagonal symbols" in data["agenda"].get("latest_result_2026_09_30_k717_k719", ""),
        "agenda K717--K719 result is not current",
    )
    check(
        "compact reduction of the native real (13,1) carrier" in data["agenda"].get("latest_result_2026_09_30_k714_k716", "")
        and "eigenvalue pairs (1,1), (9,1/9), and (81,1/81)" in data["agenda"].get("latest_result_2026_09_30_k714_k716", "")
        and "Further abstract metric work is closed" in data["agenda"].get("latest_result_2026_09_30_k714_k716", ""),
        "agenda K714--K716 result is not current",
    )
    check(
        "positive auxiliary inner product" in data["agenda"].get("latest_result_2026_09_30_k711_k713", "")
        and "native-null covector norm 3" in data["agenda"].get("latest_result_2026_09_30_k711_k713", "")
        and "no positive form is invariant under full `O(13,1)`" in data["agenda"].get("latest_result_2026_09_30_k711_k713", ""),
        "agenda K711--K713 result is not current",
    )
    check(
        "total Y=Met(X) carrier has signature (13,1)" in data["agenda"].get("latest_result_2026_09_30_k708_k710", "")
        and "real coherent frame transport preserves that inertia" in data["agenda"].get("latest_result_2026_09_30_k708_k710", "")
        and "metric-adjoint gauge-fixed symbol collapses" in data["agenda"].get("latest_result_2026_09_30_k708_k710", ""),
        "agenda K708--K710 result is not current",
    )
    check(
        "rank-13 curvature image" in data["agenda"].get("latest_result_2026_09_30_k705_k707", "")
        and "singular equation frame drops to rank 12" in data["agenda"].get("latest_result_2026_09_30_k705_k707", "")
        and "breaking Euler-after-gauge composition" in data["agenda"].get("latest_result_2026_09_30_k705_k707", ""),
        "agenda K705--K707 result is not current",
    )
    check(
        "A>=5113/7050" in data["agenda"].get("latest_result_2026_09_30_k702_k704", "")
        and "105532769/164194200>5/8" in data["agenda"].get("latest_result_2026_09_30_k702_k704", "")
        and "1993/1020000" in data["agenda"].get("latest_result_2026_09_30_k702_k704", ""),
        "agenda K702--K704 result is not current",
    )
    check(
        "||R*R-B*B||<=epsilon" in data["agenda"].get("latest_result_2026_09_30_k699_k701", "")
        and "A>=134/183" in data["agenda"].get("latest_result_2026_09_30_k699_k701", "")
        and "9039/2125000" in data["agenda"].get("latest_result_2026_09_30_k699_k701", ""),
        "agenda K699--K701 result is not current",
    )
    check(
        "polar-decomposition norm identity" in data["agenda"].get("latest_result_2026_09_30_k696_k698", "")
        and "A>=3/4" in data["agenda"].get("latest_result_2026_09_30_k696_k698", "")
        and "3993/722500" in data["agenda"].get("latest_result_2026_09_30_k696_k698", ""),
        "agenda K696--K698 result is not current",
    )
    check(
        "uniformly equivalent to the graph weight" in data["agenda"].get("latest_result_2026_09_30_k693_k695", "")
        and "monotone complete Gram limit" in data["agenda"].get("latest_result_2026_09_30_k693_k695", "")
        and "comparison floor 25" in data["agenda"].get("latest_result_2026_09_30_k693_k695", ""),
        "agenda K693--K695 result is not current",
    )
    check(
        "dense common core" in data["agenda"].get("latest_result_2026_09_30_k690_k692", "")
        and "common form core" in data["agenda"].get("latest_result_2026_09_30_k690_k692", "")
        and "complete Friedrichs form lower" in data["agenda"].get("latest_result_2026_09_30_k690_k692", ""),
        "agenda K690--K692 result is not current",
    )
    check(
        "countably many closed component operators" in data["agenda"].get("latest_result_2026_09_30_k687_k689", "")
        and "positive partial-Gram interface" in data["agenda"].get("latest_result_2026_09_30_k687_k689", "")
        and "one complete gamma anchor" in data["agenda"].get("latest_result_2026_09_30_k687_k689", ""),
        "agenda K687--K689 result is not current",
    )
    check(
        "closed-column construction route" in data["agenda"].get("latest_result_2026_09_30_k684_k686", "")
        and "component operator bounds" in data["agenda"].get("latest_result_2026_09_30_k684_k686", "")
        and "gamma-field norm bounds" in data["agenda"].get("latest_result_2026_09_30_k684_k686", ""),
        "agenda K684--K686 result is not current",
    )
    check(
        "monotone complete-form construction" in data["agenda"].get("latest_result_2026_09_30_k681_k683", "")
        and "h[u]<=c^2" in data["agenda"].get("latest_result_2026_09_30_k681_k683", "")
        and "341/170" in data["agenda"].get("latest_result_2026_09_30_k681_k683", ""),
        "agenda K681--K683 result is not current",
    )
    check(
        "current native artifacts do not yet define" in data["agenda"].get("latest_result_2026_09_30_k678_k680", "")
        and "341/170" in data["agenda"].get("latest_result_2026_09_30_k678_k680", "")
        and "data insufficiency" in data["agenda"].get("latest_result_2026_09_30_k678_k680", ""),
        "agenda K678--K680 result is not current",
    )
    check(
        "charge-graded three-line seed leakage operator" in data["agenda"].get("latest_result_2026_09_30_k675_k677", "")
        and "u_N+v_N" in data["agenda"].get("latest_result_2026_09_30_k675_k677", "")
        and "K643 does not itself prove" in data["agenda"].get("latest_result_2026_09_30_k675_k677", ""),
        "agenda K675--K677 result is not current",
    )
    check(
        "hidden graph-orthogonal complement" in data["agenda"].get("latest_result_2026_09_30_k673_k674", "")
        and "1/3-lambda_K609" in data["agenda"].get("latest_result_2026_09_30_k673_k674", "")
        and "1/100" in data["agenda"].get("latest_result_2026_09_30_k673_k674", ""),
        "agenda K673--K674 result is not current",
    )
    check(
        "same raw auxiliary ratio" in data["agenda"].get("latest_result_2026_09_30_k671_k672", "")
        and "(a_N-2/3)(a_tail-2/3)>kappa^2" in data["agenda"].get("latest_result_2026_09_30_k671_k672", "")
        and "43/60" in data["agenda"].get("latest_result_2026_09_30_k671_k672", ""),
        "agenda K671--K672 result is not current",
    )
    check(
        "A>2/3" in data["agenda"].get("latest_result_2026_09_30_k669_k670", "")
        and "B>=1/170" in data["agenda"].get("latest_result_2026_09_30_k669_k670", "")
        and "2/58653" in data["agenda"].get("latest_result_2026_09_30_k669_k670", ""),
        "agenda K669--K670 result is not current",
    )
    check(
        "1/257<beta^2" in data["agenda"].get("latest_result_2026_09_30_k667_k668", "")
        and "1/131328" in data["agenda"].get("latest_result_2026_09_30_k667_k668", ""),
        "agenda K667--K668 result is not current",
    )
    check(
        registry["live_frontier"]["current_question_contains"] in question,
        "current_question disagrees with live frontier",
    )

    disposition = data["dispositions"]["exhaustion_evaluation"]
    expected = registry["basis"]["phenomenology_disposition_register"]
    for key in ("terminal_rows", "open_rows", "exhausted", "b2_selectable"):
        check(disposition.get(key) == expected[key], f"disposition mismatch: {key}")

    root = data["qualification"]["root_candidate_rebuild"]
    qual = data["qualification"]["admission_result"]
    check(root.get("current_named_root_candidate_set") == [], "named B2 root is not empty")
    check(
        root.get("state") == registry["basis"]["w154_w229_qualification"]["root_candidate_state"],
        "root-candidate state mismatch",
    )
    check(qual.get("candidate_admitted") is False, "W154/W229 unexpectedly admitted")

    check(
        "common minimum" in data["agenda"].get("latest_result_2026_09_30_k665_k666", "")
        and "determinant margin 125/256"
        in data["agenda"].get("latest_result_2026_09_30_k665_k666", ""),
        "agenda K665--K666 result is not current",
    )
    check(
        "optimal scalar-information floor"
        in data["agenda"].get("latest_result_2026_09_30_k663_k664", "")
        and "A_lower=1-alpha_hat-e_alpha"
        in data["agenda"].get("latest_result_2026_09_30_k663_k664", ""),
        "agenda K663--K664 result is not current",
    )
    check(
        "symplectically swapped Neumann non-Friedrichs reference"
        in data["agenda"].get("latest_result_2026_09_30_k661_k662", "")
        and "D transforms by U^{-*} D U^{-1}"
        in data["agenda"].get("latest_result_2026_09_30_k661_k662", ""),
        "agenda K661--K662 result is not current",
    )
    check(
        "auxiliary resolvent parameter" in data["agenda"].get("latest_result_2026_09_29_k659_k660", "")
        and "D=W-M" in data["agenda"].get("latest_result_2026_09_29_k659_k660", ""),
        "agenda K659--K660 result is not current",
    )
    check(
        "ordinary-boundary-triple criterion"
        in data["agenda"].get("latest_result_2026_09_29_k657_k658", "")
        and "d_N-eta_N" in data["agenda"].get("latest_result_2026_09_29_k657_k658", ""),
        "agenda K657--K658 result is not current",
    )
    check(
        "every finite target b" in data["agenda"].get("latest_result_2026_09_29_k655_k656", "")
        and "b=r0-2" in data["agenda"].get("latest_result_2026_09_29_k655_k656", ""),
        "agenda K655--K656 result is not current",
    )
    check(
        "shifted-Schur target certificate"
        in data["agenda"].get("latest_result_2026_09_29_k653_k654", ""),
        "agenda K653--K654 result is not current",
    )
    check(
        "orders two through twelve do not determine"
        in data["agenda"].get("latest_result_2026_09_29_k651_k652", ""),
        "agenda K651--K652 result is not current",
    )
    check(
        "harmonic divergent direction"
        in data["agenda"].get("latest_result_2026_09_29_k649_k650", ""),
        "agenda K649--K650 result is not current",
    )
    check(
        "twelve parity-local diagonal-floor rows"
        in data["agenda"].get("latest_result_2026_09_29_k647_k648", ""),
        "agenda K647--K648 result is not current",
    )
    check(
        "1,479 two-element orbits"
        in data["agenda"].get("latest_result_2026_09_29_k645_k646", ""),
        "agenda K645--K646 result is not current",
    )
    check(
        "global lower m=inf_n m_n"
        in data["agenda"].get("latest_result_2026_09_29_k643_k644", ""),
        "agenda K643--K644 result is not current",
    )
    check(
        "corrected coefficient space is C^6 tensor H_spec"
        in data["agenda"].get("latest_result_2026_09_29_k641_k642", ""),
        "agenda K641--K642 result is not current",
    )
    check(
        "rank six and kernel dimension ten"
        in data["agenda"].get("latest_result_2026_09_29_k639_k640", ""),
        "agenda K639--K640 result is not current",
    )
    check(
        "two-dimensional block center"
        in data["agenda"].get("latest_result_2026_09_29_k637_k638", ""),
        "agenda K637--K638 result is not current",
    )
    check(
        "polynomial route"
        in data["agenda"].get("latest_result_2026_09_29_k633_k634", ""),
        "agenda K633--K634 result is not current",
    )
    check(
        "eight strongest current serialized K77 candidates"
        in data["agenda"].get("latest_result_2026_09_29_k631_k632", ""),
        "agenda K631--K632 result is not current",
    )
    check(
        "8,192-dimensional family"
        in data["agenda"].get("latest_result_2026_09_29_k629_k630", ""),
        "agenda K629--K630 result is not current",
    )
    check(
        "41,216-dimensional homogeneous space"
        in data["agenda"].get("latest_result_2026_09_29_k627_k628", ""),
        "agenda K627--K628 result is not current",
    )
    check(
        "ambient-embedding gauge"
        in data["agenda"].get("latest_result_2026_09_29_k625_k626", ""),
        "agenda K625--K626 result is not current",
    )
    check(
        "pullback Gram forms" in data["agenda"].get("latest_result_2026_09_29_k623_k624", ""),
        "agenda K623--K624 result is not current",
    )
    check(
        "full K438 action commutant"
        in data["agenda"].get("latest_result_2026_09_29_k621_k622", ""),
        "agenda K621--K622 result is not current",
    )
    check(
        "same rank-384 K438 module"
        in data["agenda"].get("latest_result_2026_09_29_k619_k620", ""),
        "agenda K619--K620 result is not current",
    )
    check(
        "Krylov ranks are 128,256,384,384,384"
        in data["agenda"].get("latest_result_2026_09_29_k617_k618", ""),
        "agenda K617--K618 result is not current",
    )
    check(
        "rank-two K596 defect" in data["agenda"].get("latest_result_2026_09_29_k615_k616", ""),
        "agenda K615--K616 result is not current",
    )
    check(
        "rank-128 zero-form inclusion" in data["agenda"].get("latest_result_2026_09_29_k614", ""),
        "agenda K614 result is not current",
    )
    check(
        "central parity" in data["agenda"].get("latest_result_2026_09_29_k612_k613", ""),
        "agenda K612--K613 result is not current",
    )
    check(
        "K600 proves" in data["agenda"].get("latest_result_2026_09_28_k600_k601", ""),
        "agenda K600--K601 result is not current",
    )
    check(
        "109,732" in data["agenda"].get("latest_result_2026_09_28_k602_k603", ""),
        "agenda K602--K603 result is not current",
    )
    check(
        "minimum nonzero carrier-idempotent rank is 64"
        in data["agenda"].get("latest_result_2026_09_28_k608_k610", ""),
        "agenda K77 route is not current",
    )
    check(
        "uniformly below 1/3"
        in data["agenda"].get("latest_result_2026_09_28_k608_k610", ""),
        "agenda K500 route is not current",
    )
    check(
        "operator product is ill-typed"
        in data["agenda"].get("latest_result_2026_09_29_k611", ""),
        "agenda K611 floor obstruction is not current",
    )
    check(
        "41,063 exact determinant-simplex classes"
        in data["agenda"].get("latest_result_2026_09_28_k604_k605", ""),
        "agenda K604--K605 result is not current",
    )
    check(
        "1,614 positive diagonal self norms"
        in data["agenda"].get("latest_result_2026_09_28_k606_k607", ""),
        "agenda K606--K607 result is not current",
    )

    k649 = data["k649"]
    k649_t = k649["parity_matching_theorem"]
    k649_r = k649["quantitative_route_consequence"]
    k649_n = k649["native_interface_status"]
    check(k649_t["new_matching_condition"].endswith("Alpha=I_6") and
          k649_t["each_mismatched_parity_component_has_harmonic_divergent_direction"] and
          not k649_t["parity_change_makes_separate_singular_factors_bounded"] and
          k649_t["complete_matched_combination_remains_the_valid_object"],
          "K649 parity matching theorem moved")
    check(not k649_r["K644_raw_row_route_disproved"] and
          not k649_r["K644_raw_row_route_automatically_available_from_parity"] and
          k649_r["cancellation_adapted_complete_parity_form_route_live"] and
          k649_n["native_parity_cancellation_matching_proved"] and
          not k649_n["native_global_m_identified"] and
          not k649_n["K473_released"],
          "K649 native interface ceiling moved")

    k650 = data["k650"]
    k650_t = k650["cancelled_quadrant_theorem"]
    k650_q = k650["native_quantitative_schema"]
    k650_n = k650["native_interface_status"]
    check(k650_t["relative_range"] == "0<=rho_s,n<=1" and
          k650_t["rho_equal_one_allowed"] and
          not k650_t["separately_singular_raw_channel_bounds_required"] and
          k650_t["complete_cancelled_quadrant_bounds_required"] and
          k650_t["same_domain_required"],
          "K650 cancelled-quadrant theorem moved")
    check(len(k650_q["uniform_tail_rows"]) == 2 and
          not k650_q["finite_prefix_is_tail"] and
          not k650_q["raw_twelve_plus_thirty_rows_mandatory_for_this_route"] and
          k650_q["raw_rows_remain_valid_if_independently_same_domain_bounded"] and
          k650_n["cancellation_adapted_parity_lower_theorem_proved"] and
          not k650_n["actual_cancelled_quadrant_floors_identified"] and
          not k650_n["native_global_m_identified"] and
          not k650_n["K473_released"],
          "K650 native interface ceiling moved")

    k651 = data["k651"]
    k651_p = k651["k179_prefix"]
    k651_t = k651["prefix_nonidentifiability_theorem"]
    k651_n = k651["native_interface_status"]
    check(k651_p["orders"] == list(range(2, 13)) and
          k651_p["term_count"] == 2958 and
          not k651_p["all_order_tail_serialized"],
          "K651 prefix custody moved")
    check(k651_t["preserves_K650_relative_interface"] and
          k651_t["preserves_total_parity_reduction"] and
          not k651_t["finite_prefix_determines_uniform_tail"] and
          not k651_t["fixed_native_operator_has_no_floor"] and
          not k651_n["actual_uniform_parity_tails_identified"] and
          not k651_n["native_global_m_identified"],
          "K651 claim ceiling moved")

    k652 = data["k652"]
    k652_t = k652["all_order_tail_theorem"]
    k652_c = k652["exact_controls"]
    k652_n = k652["native_interface_status"]
    check(k652_t["rho_endpoint_allowed"] and
          not k652_t["separately_singular_raw_rows_required"] and
          k652_t["all_order_hypotheses_required"] and
          not k652_t["finite_prefix_alone_sufficient"] and
          "min(A_s(n)-K_s(n),D_s(n)-K_s(n))" in k652_t["sector_row_floor"],
          "K652 all-order theorem moved")
    check(k652_c["synthetic_not_native"] and
          k652_c["global_declared_tail"] == "7/4" and
          k652_c["all_rows_pass"] and
          k652_n["all_order_certificate_shape_complete"] and
          not k652_n["actual_uniform_parity_tails_identified"] and
          not k652_n["native_global_m_identified"] and
          not k652_n["K473_released"],
          "K652 native interface ceiling moved")

    k653 = data["k653"]
    k653_t = k653["shifted_schur_theorem"]
    k653_c = k653["exact_controls"]
    k653_n = k653["native_interface_status"]
    check(k653_t["theta_endpoint_allowed"] and
          k653_t["same_domain_required"] and
          not k653_t["separately_singular_raw_rows_required"] and
          not k653_t["absolute_A_D_K_serialization_required"] and
          "|c|^2<=(a-b)(d-b)" in k653_t["scalar_sharp_iff"],
          "K653 shifted-Schur theorem moved")
    check(k653_c["synthetic_not_native"] and
          k653_c["observed_pattern"] == [True, True, False, False] and
          k653_n["shifted_target_certificate_shape_complete"] and
          not k653_n["actual_native_target_b_identified"] and
          not k653_n["actual_native_shifted_diagonal_positivity_proved"] and
          not k653_n["actual_native_shifted_cross_contraction_proved"] and
          not k653_n["native_global_m_identified"] and
          not k653_n["K473_released"],
          "K653 native interface ceiling moved")

    k654 = data["k654"]
    k654_t = k654["all_order_shifted_tail_theorem"]
    k654_c = k654["exact_controls"]
    k654_n = k654["native_interface_status"]
    check(k654_t["single_target_may_be_tested_directly"] and
          not k654_t["absolute_A_D_K_envelopes_required"] and
          k654_t["all_order_shifted_hypotheses_required"] and
          not k654_t["finite_prefix_alone_sufficient"] and
          k654_t["equivalent_native_burden_is_not_removed"],
          "K654 all-order shifted tail theorem moved")
    check(k654_c["synthetic_not_native"] and
          k654_c["target_b"] == "5/4" and
          k654_c["all_tail_rows_pass"] and
          k654_c["finite_sectors_at_least_target"] and
          k654_n["all_order_shifted_tail_shape_complete"] and
          not k654_n["actual_native_target_b_identified"] and
          not k654_n["actual_uniform_parity_tails_identified"] and
          not k654_n["native_global_m_identified"] and
          not k654_n["K473_released"],
          "K654 native interface ceiling moved")

    k655 = data["k655"]
    k655_t = k655["interface_theorem"]
    k655_c = k655["exact_controls"]
    k655_n = k655["native_interface_status"]
    check(k655_t["all_finite_targets_defeated_over_interface_class"] and
          not k655_t["actual_native_sector_row_identified"] and
          not k655_t["fixed_native_operator_proved_unbounded_below"] and
          "-L-2-b<0" in k655_t["first_failure"],
          "K655 shifted-target custody theorem moved")
    check(k655_c["same_interface_not_native"] and
          k655_c["all_rows_fail_first_shifted_diagonal"] and
          all(row["first_K653_hypothesis_fails"] for row in k655_c["rows"]) and
          not k655_n["actual_native_target_b_identified"] and
          not k655_n["native_global_m_identified"] and
          not k655_n["K473_released"],
          "K655 native interface ceiling moved")

    k656 = data["k656"]
    k656_t = k656["base_floor_lift_theorem"]
    k656_c = k656["exact_controls"]
    k656_n = k656["native_interface_status"]
    check(k656_t["selected_target"] == "b=r0-2" and
          k656_t["same_domain_required"] and
          k656_t["two_unit_loss_sharp_over_declared_reference_class"] and
          not k656_t["K653_sector_search_required_after_global_base_lower"],
          "K656 base-floor target lift moved")
    check(k656_c["conditional_not_native_number"] and
          k656_c["all_rows_pass"] and k656_c["all_rows_sharp"] and
          not k656_n["actual_native_base_floor_r0_identified"] and
          not k656_n["actual_native_target_b_identified"] and
          not k656_n["actual_uniform_parity_tails_identified"] and
          not k656_n["native_global_m_identified"] and
          not k656_n["K473_released"],
          "K656 native interface ceiling moved")

    k659 = data["k659"]
    k659_t = k659["compensated_chart_theorem"]
    k659_s = k659["semiboundedness_nonidentifiability"]
    k659_c = k659["exact_controls"]
    k659_n = k659["native_interface_status"]
    check(not k659_t["lambda_256_is_native_floor"] and
          not k659_t["arbitrarily_large_chart_shift_improves_floor"] and
          not k659_t["chart_contraction_implies_positive_operator"] and
          k659_t["same_target_operator_required"] and
          k659_c["chart_rows_preserve_one_floor"] and
          k659_c["displayed_256_rejected_as_floor"],
          "K659 compensated-chart theorem moved")
    check(not k659_s["numerical_s_identified"] and
          not k659_s["best_floor_identified"] and
          k659_s["same_qualitative_interface_allows_arbitrary_negative_floors"] and
          not k659_s["fixed_native_operator_has_no_floor"] and
          not k659_n["actual_native_s_identified"] and
          not k659_n["actual_native_denominator_serialized"] and
          not k659_n["actual_native_base_floor_r0_identified"] and
          not k659_n["K473_released"],
          "K659 native interface ceiling moved")

    k660 = data["k660"]
    k660_t = k660["translation_theorem"]
    k660_c = k660["exact_controls"]
    k660_x = k660["composition"]
    k660_n = k660["native_interface_status"]
    check(k660_t["denominator_identity"] == "D'_W(z)=W'-M'(z)=W-M(z)=D_W(z)" and
          k660_t["reference_extension_unchanged"] and
          k660_t["reference_resolvent_level_unchanged"] and
          k660_t["friedrichs_status_preserved_if_previously_proved"] and
          not k660_t["friedrichs_status_created_by_translation"] and
          k660_t["complete_denominator_order_unchanged"] and
          k660_t["same_coordinate_approximant_error_unchanged"] and
          not k660_t["finite_impurity_translation_sufficient"] and
          not k660_t["unbounded_translation_covered"],
          "K660 boundary-translation theorem moved")
    check(k660_c["denominator_invariant"] and
          k660_c["approximant_denominator_invariant"] and
          k660_c["operator_norm_error_invariant"] and
          not k660_x["K139_regulator_coordinates_already_authenticated_as_boundary_translation"] and
          not k660_n["actual_native_boundary_triple_serialized"] and
          not k660_n["actual_native_translation_law_proved"] and
          not k660_n["actual_native_s_identified"] and
          not k660_n["actual_native_denominator_serialized"] and
          not k660_n["K473_released"],
          "K660 native interface ceiling moved")

    k663 = data["k663"]
    k663_t = k663["sharp_floor_theorem"]
    k663_c = k663["exact_control"]
    k663_n = k663["native_interface_status"]
    check(k663_t["comparison_matrix"] == "[[A,-beta],[-beta,B]]" and
          k663_t["sharp_for_declared_scalar_information"] and
          k663_t["dimension_free"] and
          k663_t["complete_spectator_space_required"] and
          k663_t["positive_floor_iff"] == "A>0, B>0 and A*B>beta^2" and
          k663_t["young_optimization_recovers_lambda_minus"],
          "K663 sharp floor theorem moved")
    check(k663_c["sharp_conservative_floor"] == "5/8" and
          k663_c["K642_fixed_floor"] == "1/4" and
          k663_c["strict_improvement"] and
          k663_c["determinant_margin"] == "125/256" and
          k663_c["rayleigh_equals_floor"] and
          not k663_n["actual_complete_effective_A_identified"] and
          not k663_n["actual_complete_effective_B_identified"] and
          not k663_n["named_complete_sector_floor_emitted"],
          "K663 control or native-interface ceiling moved")

    k664 = data["k664"]
    k664_t = k664["transfer_theorem"]
    k664_c = k664["exact_controls"]
    k664_n = k664["native_interface_status"]
    check(k664_t["same_complete_domain_required"] and
          k664_t["complete_spectator_complement_required"] and
          not k664_t["finite_block_only_sufficient"] and
          not k664_t["sampled_sector_only_sufficient"] and
          not k664_t["uncontrolled_complement_allowed"] and
          k664_t["one_sided_error_orientation_required"],
          "K664 cofinal transfer theorem moved")
    check(k664_c["all_rows_positive"] and
          k664_c["floors_monotone"] and
          k664_c["floors"] == ["1/2", "9/16", "5/8"] and
          k664_c["terminal_floor_matches_K663_control"] and
          k664_c["finite_block_only_rejected"] and
          k664_c["sampled_sector_only_rejected"] and
          k664_c["uncontrolled_complement_rejected"] and
          not k664_n["actual_native_cofinal_packet_identified"] and
          not k664_n["named_complete_sector_floor_emitted"],
          "K664 controls or native-interface ceiling moved")

    k665 = data["k665"]
    k665_t = k665["composition_theorem"]
    k665_c = k665["exact_control"]
    k665_n = k665["native_interface_status"]
    check(k665_t["complete_domain_required"] and
          k665_t["both_total_parities_required"] and
          k665_t["all_finite_rows_through_N_required"] and
          k665_t["independent_tail_for_each_parity_required"] and
          not k665_t["finite_prefix_only_sufficient"] and
          not k665_t["sampled_sectors_only_sufficient"] and
          not k665_t["uncontrolled_complement_allowed"],
          "K665 parity-cofinal composition theorem moved")
    check(k665_c["plus_lower"] == "11/16" and
          k665_c["minus_lower"] == "21/32" and
          k665_c["global_B_lower"] == "21/32" and
          k665_c["finite_prefix_counterexample"]["destroys_global_lower"] and
          not k665_n["actual_complete_B_lower_identified"],
          "K665 control or native-interface ceiling moved")

    k666 = data["k666"]
    k666_t = k666["certificate_theorem"]
    k666_c = k666["exact_control"]
    k666_n = k666["native_interface_status"]
    check(k666_t["K647_common_domain_required"] and
          k666_t["K648_both_total_parities_required"] and
          k666_t["K665_finite_rows_and_two_tails_required"] and
          k666_t["matched_trace_same_domain_required"] and
          not k666_t["finite_prefix_only_sufficient"] and
          not k666_t["one_parity_only_sufficient"] and
          not k666_t["uncontrolled_complement_allowed"],
          "K666 complete cancellation certificate moved")
    check(k666_c["determinant_margin"] == "125/256" and
          k666_c["certified_floor"] == "5/8" and
          k666_c["endpoint_control"]["certified_floor"] == "0" and
          k666_c["negative_determinant_rejected"] and
          not k666_n["native_complete_floor_emitted"],
          "K666 control or native-interface ceiling moved")

    k675 = data["k675"]
    k675_t = k675["seed_operator_theorem"]
    k675_n = k675["native_interface_status"]
    check(k675_t["input_charge_lines_orthogonal"] and
          k675_t["output_charge_sectors_orthogonal"] and
          k675_t["operator_norm_square_is_maximum_of_line_uppers"] and
          not k675_t["sum_of_line_uppers_used"] and
          not k675_t["complete_domain_extension_claimed"] and
          not k675_t["native_R_compression_identity_claimed"] and
          not k675_n["actual_seed_compression_identity_proved"] and
          not k675_n["native_A_above_two_thirds_proved"],
          "K675 seed leakage operator or native ceiling moved")

    k676 = data["k676"]
    k676_t = k676["three_line_criterion"]
    k676_n = k676["native_interface_status"]
    check(k676_t["exact_identity_route_sufficient"] and
          k676_t["gram_domination_route_sufficient_for_norm_bound"] and
          k676_t["charge_preserving_shortcut_requires_native_charge_intertwiner"] and
          not k676_t["ungraded_linewise_sum_below_one_third"] and
          not k676_t["K609_alone_supplies_native_R_actions"] and
          not k676_n["native_charge_intertwiner_proved"] and
          not k676_n["native_compression_identity_proved"] and
          not k676_n["native_A_above_two_thirds_proved"],
          "K676 three-line native criterion or ceiling moved")

    k677 = data["k677"]
    k677_g = k677["general_cofinal_theorem"]
    k677_b = k677["bath_reducing_shortcut"]
    k677_n = k677["native_interface_status"]
    check(k677_g["two_column_conclusion"] == "||R Q_seed||^2<=u_N+v_N" and
          not k677_g["output_range_orthogonality_required"] and
          not k677_g["finite_rows_without_complete_tail_sufficient"] and
          not k677_b["K643_exchange_bath_preservation_proves_R_reduction"] and
          k677_b["native_reduction_must_be_proved_for_R"] and
          not k677_b["individual_sector_bounds_without_reduction_sufficient"] and
          not k677_n["native_R_bath_reduction_proved"] and
          not k677_n["native_tau2_at_most_one_over_one_hundred_proved"] and
          not k677_n["native_A_above_two_thirds_proved"],
          "K677 complement cofinal certificate or native ceiling moved")

    k678 = data["k678"]
    k678_t = k678["custody_theorem"]
    k678_n = k678["native_interface_status"]
    check(not k678_t["current_native_r_free_defined"] and
          not k678_t["current_native_T_defined"] and
          not k678_t["current_native_R_defined"] and
          not k678_t["absence_proves_native_remainder_nonexistent"] and
          not k678_t["absence_proves_factorization_impossible"] and
          not k678_n["actual_native_R_serialized"] and
          not k678_n["native_A_above_two_thirds_proved"],
          "K678 native remainder custody or claim ceiling moved")

    k679 = data["k679"]
    k679_s = k679["square_root_theorem"]
    k679_r = k679["projection_reduction_theorem"]
    k679_n = k679["native_interface_status"]
    check(k679_s["required_form_closedness"] and
          k679_s["required_form_density"] and
          k679_s["required_form_symmetry"] and
          k679_s["closed_nonpositive_form_suffices_for_factorization"] and
          not k679_s["bounded_R_follows_from_factorization_alone"] and
          not k679_s["K609_map_identity_follows_from_factorization_alone"] and
          not k679_r["K643_monomial_preservation_alone_sufficient"] and
          not k679_n["actual_native_T_constructed"] and
          not k679_n["native_A_above_two_thirds_proved"],
          "K679 square-root symmetry compiler or native ceiling moved")

    k680 = data["k680"]
    k680_t = k680["base_floor_target_theorem"]
    k680_w = k680["weyl_target_translation"]
    k680_n = k680["native_interface_status"]
    check(k680_t["required_complete_base_floor"] == "r0>=341/170" and
          k680_t["equality_check"] == "341/170-2=1/170" and
          k680_t["target_is_sharp_over_K168_reference_class"] and
          k680_w["target_lambda"] == "341/170" and
          k680_w["target_s"] == "-341/170" and
          not k680_w["synthetic_negative_floor_rows_supply_target"] and
          not k680_n["actual_complete_B_lower_identified"] and
          not k680_n["native_complete_floor_emitted"],
          "K680 reference base-floor target or native ceiling moved")

    k690 = data["k690"]
    k690_t = k690["summable_core_theorem"]
    k690_n = k690["native_interface_status"]
    check(k690_t["dense_common_core_required"] and
          k690_t["complete_square_sum_required"] and
          not k690_t["nonsummable_uniform_component_bounds_sufficient"] and
          not k690_n["actual_native_maximal_domain_dense"] and
          not k690_n["native_complete_floor_emitted"],
          "K690 summable-core compiler or native ceiling moved")

    k691 = data["k691"]
    k691_t = k691["form_core_theorem"]
    k691_n = k691["native_interface_status"]
    check(k691_t["one_common_form_core_for_both_required"] and
          not k691_t["algebraically_dense_test_space_sufficient"] and
          not k691_t["core_for_only_native_form_sufficient"] and
          not k691_n["actual_native_CstarC_equals_H"] and
          not k691_n["native_complete_floor_emitted"],
          "K691 form-core identification or native ceiling moved")

    k692 = data["k692"]
    k692_g = k692["friedrichs_gap_theorem"]
    k692_t = k692["defect_trace_theorem"]
    k692_n = k692["native_interface_status"]
    check(k692_g["authenticated_friedrichs_reference_required"] and
          k692_g["complete_form_lower_required"] and
          not k692_g["finite_sector_lower_sufficient"] and
          k692_t["complete_defect_space_required"] and
          not k692_t["sampled_trace_vectors_sufficient"] and
          not k692_n["actual_native_anchor_gamma_norm_proved"] and
          not k692_n["native_complete_floor_emitted"],
          "K692 Friedrichs-trace compiler or native ceiling moved")

    k696 = data["k696"]
    k696_t = k696["integration_theorem"]
    k696_n = k696["native_interface_status"]
    check(k696_t["complete_two_sided_graph_equivalence_required"] and
          k696_t["common_form_core_for_column_and_native_form_required"] and
          not k696_t["graph_equivalence_without_form_identity_sufficient"] and
          not k696_t["reduction_of_column_labels_alone_reduces_native_R"] and
          not k696_n["actual_native_R_constructed"] and
          not k696_n["native_complete_floor_emitted"],
          "K696 column/remainder integration or native ceiling moved")

    k697 = data["k697"]
    k697_t = k697["block_theorem"]
    k697_n = k697["native_interface_status"]
    check(k697_t["native_seed_compression_required"] and
          k697_t["complete_complement_bound_required"] and
          k697_t["R_star_R_reduction_required_for_maximum_rule"] and
          not k697_t["seed_and_complement_norms_without_cross_or_reduction_sufficient"] and
          not k697_n["native_A_above_two_thirds_proved"] and
          not k697_n["native_complete_floor_emitted"],
          "K697 seed/complement A margin or native ceiling moved")

    k698 = data["k698"]
    k698_t = k698["end_to_end_theorem"]
    k698_n = k698["native_interface_status"]
    check(k698_t["complete_Friedrichs_domain_inclusion_required"] and
          k698_t["complete_anchor_defect_trace_packet_required"] and
          k698_t["same_boundary_coordinate_and_fixed_W_required"] and
          not k698_t["finite_trace_block_without_tail_and_cross_sufficient"] and
          not k698_n["actual_native_target_denominator_nonnegative"] and
          not k698_n["native_complete_floor_emitted"],
          "K698 boundary denominator chain or native ceiling moved")

    k699 = data["k699"]
    k699_t = k699["theorem"]
    k699_n = k699["native_interface_status"]
    check(k699_t["complete_a_relative_mismatch_required"] and
          not k699_t["finite_test_equality_sufficient"] and
          not k699_t["componentwise_mismatch_without_complete_sum_sufficient"] and
          not k699_n["actual_native_complete_mismatch_proved"] and
          not k699_n["native_A_above_two_thirds_proved"] and
          not k699_n["native_complete_floor_emitted"],
          "K699 approximate-form margin or native ceiling moved")

    k700 = data["k700"]
    k700_t = k700["theorem"]
    k700_n = k700["native_interface_status"]
    check(k700_t["complete_cross_bound_required_without_reduction"] and
          not k700_t["individual_compression_bounds_alone_sufficient"] and
          not k700_t["finite_complement_prefix_sufficient"] and
          not k700_n["actual_native_cross_bound_proved"] and
          not k700_n["native_A_above_two_thirds_proved"] and
          not k700_n["native_complete_floor_emitted"],
          "K700 cross-coupled margin or native ceiling moved")

    k701 = data["k701"]
    k701_t = k701["theorem"]
    k701_n = k701["native_interface_status"]
    check(k701_t["outward_denominator_error_required"] and
          k701_t["same_boundary_coordinate_and_fixed_W_required"] and
          not k701_t["point_estimates_without_outward_error_sufficient"] and
          not k701_t["finite_defect_or_sector_errors_sufficient"] and
          not k701_n["actual_native_complete_denominator_enclosure_proved"] and
          not k701_n["actual_native_target_denominator_nonnegative"] and
          not k701_n["native_complete_floor_emitted"],
          "K701 interval boundary denominator or native ceiling moved")

    k702 = data["k702"]
    k702_t = k702["theorem"]
    k702_n = k702["native_interface_status"]
    check(k702_t["all_three_errors_outward_required"] and
          k702_t["all_errors_complete_space_required"] and
          not k702_t["nominal_bounds_without_errors_sufficient"] and
          not k702_t["finite_sector_errors_sufficient"] and
          not k702_n["actual_native_cross_enclosure_proved"] and
          not k702_n["native_A_above_two_thirds_proved"] and
          not k702_n["native_complete_floor_emitted"],
          "K702 interval cross-coupled margin or native ceiling moved")

    k703 = data["k703"]
    k703_t = k703["theorem"]
    k703_n = k703["native_interface_status"]
    check(k703_t["same_complete_graph_domain_required"] and
          k703_t["A_and_B_errors_paid_downward_required"] and
          k703_t["beta_square_error_paid_upward_required"] and
          not k703_t["nominal_values_without_errors_sufficient"] and
          not k703_t["finite_parity_prefix_sufficient"] and
          not k703_n["native_floor_above_five_eighths_proved"] and
          not k703_n["native_complete_floor_emitted"],
          "K703 interval cancellation floor or native ceiling moved")

    k704 = data["k704"]
    k704_t = k704["theorem"]
    k704_n = k704["native_interface_status"]
    check(k704_t["reference_preserving_coordinate_authentication_required"] and
          k704_t["joint_W_and_M_transport_required"] and
          k704_t["complete_residual_error_required"] and
          not k704_t["raw_floor_invariant_under_nonunitary_U"] and
          not k704_t["finite_boundary_block_error_sufficient"] and
          not k704_n["actual_native_coordinate_map_authenticated"] and
          not k704_n["actual_native_target_denominator_nonnegative"] and
          not k704_n["native_complete_floor_emitted"],
          "K704 coordinate-transported margin or native ceiling moved")

    k705 = data["k705"]
    k705_t = k705["theorem"]
    k705_n = k705["native_interface_status"]
    check(k705_t["reduction_must_be_injective_on_curvature_image"] and
          k705_t["rank_thirteen_is_necessary_and_sufficient_for_middle_exactness"] and
          not k705_t["row_count_alone_is_sufficient"] and
          not k705_t["lorentzian_defect_transfers_to_euclidean_claim"] and
          not k705_n["source_independent_row_projector_supplied"] and
          not k705_n["SC_ACT_06_ellipticity_proved"],
          "K705 reduced-symbol criterion or source ceiling moved")

    k706 = data["k706"]
    k706_t = k706["theorem"]
    k706_n = k706["native_interface_status"]
    check(k706_t["gauge_and_euler_maps_must_transport_coherently"] and
          k706_t["rank_and_middle_exactness_are_invariant"] and
          not k706_t["singular_equation_frame_is_allowed"] and
          not k706_t["lorentzian_signature_change_is_a_frame_transport"] and
          not k706_n["native_frame_map_authenticated"] and
          not k706_n["SC_ACT_06_ellipticity_proved"],
          "K706 Euclidean frame transport or source ceiling moved")

    k707 = data["k707"]
    k707_t = k707["theorem"]
    k707_n = k707["native_interface_status"]
    check(k707_t["off_diagonal_coupling_must_annihilate_gauge_image"] and
          k707_t["triangular_gauge_compatible_extension_preserves_exactness"] and
          k707_t["rank_repair_that_breaks_chain_is_rejected"] and
          not k707_t["one_exact_diagonal_is_sufficient"] and
          not k707_n["native_mixed_principal_coupling_supplied"] and
          not k707_n["SC_ACT_06_ellipticity_proved"],
          "K707 coupled-symbol theorem or source ceiling moved")

    k708 = data["k708"]
    k708_t = k708["theorem"]
    k708_n = k708["native_interface_status"]
    check(k708_t["positive_definite_iff_lambda_below_one_over_n"] and
          k708_t["one_negative_trace_direction_above_threshold"] and
          not k708_t["euclidean_base_implies_euclidean_total_for_native_lambda"] and
          k708["exact_controls"]["native_total_signature"] == [13, 1, 0] and
          not k708_n["real_euclidean_continuation_supplied"] and
          not k708_n["SC_ACT_06_ellipticity_proved"],
          "K708 DeWitt signature boundary or source ceiling moved")

    k709 = data["k709"]
    k709_t = k709["theorem"]
    k709_n = k709["native_interface_status"]
    check(k709_t["real_congruence_preserves_inertia"] and
          not k709_t["real_invertible_frame_can_map_13_1_to_14_0"] and
          k709_t["complex_trace_rotation_gives_bilinear_identity"] and
          not k709_t["complex_trace_rotation_is_real_invertible"] and
          not k709_n["authenticated_real_euclidean_frame_constructed"] and
          not k709_n["SC_ACT_06_ellipticity_proved"],
          "K709 real-frame Euclideanization boundary or source ceiling moved")

    k710 = data["k710"]
    k710_t = k710["theorem"]
    k710_n = k710["native_interface_status"]
    check(k710_t["koszul_exact_for_every_nonzero_covector_without_metric"] and
          k710_t["metric_hodge_symbol_equals_covector_norm_times_identity"] and
          not k710_t["native_metric_gauge_fixed_symbol_is_elliptic"] and
          not k710_t["source_claim_is_refuted_by_null_symbol"] and
          k710["exact_controls"]["null_metric_laplacian_rank"] == 0 and
          k710["exact_controls"]["euclideanized_laplacian_rank"] == 14 and
          not k710_n["SC_ACT_06_ellipticity_proved"],
          "K710 null-symbol boundary or source ceiling moved")

    k711 = data["k711"]
    k711_t = k711["theorem"]
    k711_n = k711["native_interface_status"]
    check(k711_t["middle_exact_iff_positive_hodge_laplacian_invertible"] and
          k711_t["holds_for_every_positive_auxiliary_inner_product"] and
          not k711_t["action_pairing_positive_required"] and
          k711["exact_controls"]["hodge_laplacian_rank"] == 4 and
          k711["exact_controls"]["nonexact_control_laplacian_rank"] == 3 and
          not k711_n["SC_ACT_06_ellipticity_proved"],
          "K711 exact-complex Hodge criterion or source ceiling moved")

    k712 = data["k712"]
    k712_t = k712["theorem"]
    k712_n = k712["native_interface_status"]
    check(k712_t["native_action_pairing_remains_indefinite"] and
          k712_t["auxiliary_positive_metric_exists_on_same_real_carrier"] and
          not k712_t["real_structure_changed"] and
          k712["exact_controls"]["native_null_auxiliary_nonnull"]["native"]["laplacian_rank"] == 0 and
          k712["exact_controls"]["native_null_auxiliary_nonnull"]["auxiliary"]["laplacian_rank"] == 14 and
          not k712_n["SC_ACT_06_ellipticity_proved"],
          "K712 auxiliary-positive gauge repair or source ceiling moved")

    k713 = data["k713"]
    k713_t = k713["theorem"]
    k713_n = k713["native_interface_status"]
    check(k713_t["rational_boost_preserves_native_1_1_form"] and
          not k713_t["positive_definite_O_13_1_invariant_form_exists"] and
          k713_t["auxiliary_positive_metric_requires_symmetry_reduction_or_extra_choice"] and
          k713["exact_controls"]["boost_eigenvalues"] == ["3", "1/3"] and
          k713["exact_controls"]["solution_generator_signature"] == [1, 1, 0] and
          not k713_n["SC_ACT_06_ellipticity_proved"],
          "K713 native-symmetry gauge-metric obstruction or source ceiling moved")

    k714 = data["k714"]
    k714_t = k714["theorem"]
    k714_n = k714["native_interface_status"]
    check(k714_t["theta_is_involution"] and
          k714_t["eta_theta_is_symmetric_positive_definite"] and
          k714_t["compact_stabilizer_is_O13_times_O1"] and
          not k714_t["compact_reduction_is_source_owned"] and
          k714["exact_controls"]["q_signature"] == [14, 0, 0] and
          not k714_n["SC_ACT_06_ellipticity_proved"],
          "K714 Cartan-reduction gauge metric or source ceiling moved")

    k715 = data["k715"]
    k715_t = k715["theorem"]
    k715_n = k715["native_interface_status"]
    check(k715_t["transported_q_is_positive_definite"] and
          k715_t["transported_q_equals_L_inverse_transpose_q_L_inverse"] and
          k715_t["cartan_compatibility_q_eta_inverse_q_equals_eta"] and
          k715_t["bare_hodge_symbol_full_rank_at_both_native_null_directions"] and
          not k715_t["coordinate_transport_selects_a_source_owned_reduction"] and
          k715["exact_controls"]["auxiliary_null_norms"] == ["18", "2/9"] and
          not k715_n["SC_ACT_06_ellipticity_proved"],
          "K715 Lorentz-natural auxiliary family or source ceiling moved")

    k716 = data["k716"]
    k716_t = k716["theorem"]
    k716_n = k716["native_interface_status"]
    check(k716_t["cartan_compatible_positive_metrics_exist"] and
          k716_t["boost_orbit_contains_infinitely_many_distinct_reductions"] and
          not k716_t["native_eta_selects_a_unique_reduction"] and
          not k716_t["mathematical_existence_implies_source_ownership"] and
          k716["exact_controls"]["plane_eigenvalue_pairs"] == [["1", "1"], ["9", "1/9"], ["81", "1/81"]] and
          not k716_n["SC_ACT_06_ellipticity_proved"],
          "K716 compact-reduction selection boundary or source ceiling moved")

    k717 = data["k717"]
    k717_t = k717["theorem"]
    k717_n = k717["native_interface_status"]
    check(k717_t["source_connection_formula_instantiated"] and
          k717_t["native_curvature_orbit_identity_holds"] and
          k717_t["background_frobenius_q_equals_eta_theta"] and
          k717_t["reduction_is_O4_natural"] and
          not k717_t["full_O13_1_canonical_selection_follows"] and
          k717["exact_controls"]["total_signature"] == [13, 1] and
          not k717_t["SC_ACT_06_ellipticity_proved"] and
          not k717_n["euclidean_fermion_symbol"],
          "K717 flat Euclidean gimmel germ or source ceiling moved")

    k718 = data["k718"]
    k718_t = k718["theorem"]
    k718_n = k718["native_interface_status"]
    check(k718_t["field_transverse_projector_constructed"] and
          k718_t["independent_euler_row_projector_constructed"] and
          k718_t["native_null_covectors_are_included"] and
          k718["exact_controls"]["all_cases_projector_ranks"] == [[13, 13], [13, 13], [13, 13]] and
          k718["exact_controls"]["all_cases_middle_cohomology"] == [0, 0, 0] and
          not k718_t["complete_action_owned_bosonic_symbol_constructed"] and
          not k718_t["full_SC_ACT_06_ellipticity_proved"] and
          not k718_n["action_owned_bosonic_euler_symbol"],
          "K718 projected exterior complex or source ceiling moved")

    k719 = data["k719"]
    k719_t = k719["theorem"]
    k719_n = k719["native_interface_status"]
    check(k719_t["boson_fermion_mixed_hessian_vanishes_at_zero_fermion"] and
          k719_t["gauge_symbol_has_zero_fermion_component_at_zero_fermion"] and
          k719_t["middle_cohomology_splits_boson_plus_fermion"] and
          k719_t["full_exactness_requires_both_action_bosonic_and_fermion_exactness"] and
          k719["exact_controls"]["exact_total_middle_cohomology"] == 0 and
          k719["exact_controls"]["deficient_total_middle_cohomology"] == 1 and
          not k719_t["full_SC_ACT_06_ellipticity_proved"] and
          not k719_n["complete_full_field_symbol"],
          "K719 zero-fermion full-symbol reduction or source ceiling moved")

    k720 = data["k720"]
    k720_t = k720["transport_theorem"]
    k720_c = k720["exact_controls"]
    check(k720_t["complex_clifford_14_real_forms_are_isomorphic"] and
          k720_t["independent_row_restriction_preserves_euler_kernel"] and
          not k720_t["selected_bosonic_middle_symbol_is_exact"] and
          k720_c["field_dimension"] == 229386 and
          k720_c["owned_metric_diffeomorphism_rank"] == 4 and
          k720_c["nonnull_cohomology_dimension"] == 98470 and
          k720_c["native_null_cohomology_dimension"] == 106634 and
          not k720_t["full_SC_ACT_06_ellipticity_proved"],
          "K720 selected I1B bosonic transport or source ceiling moved")

    k721 = data["k721"]
    k721_t = k721["theorem"]
    k721_c = k721["exact_controls"]
    check(k721_t["each_pure_contraction_chiral_block_is_invertible"] and
          k721_t["two_mirror_blocks_are_jointly_invertible"] and
          k721_t["equal_contraction_wedge_ratio_is_singular"] and
          not k721_t["source_uniquely_selects_pure_contraction_over_family"] and
          k721_c["pure_contraction_two_block_rank"] == 1920 and
          k721_c["equal_ratio_kernel_per_block"] == 768 and
          not k721_t["full_SC_ACT_06_ellipticity_proved"],
          "K721 equation-(9.16) fermion symbol or selector ceiling moved")

    k722 = data["k722"]
    k722_t = k722["composition_theorem"]
    k722_c = k722["exact_controls"]
    k722_d = k722["decision"]
    check(k722_t["middle_cohomology_is_direct_sum"] and
          k722_t["displayed_fermion_candidate_is_exact"] and
          not k722_t["selected_bosonic_candidate_is_exact"] and
          not k722_t["full_frozen_symbol_is_exact_at_every_nonzero_covector"] and
          k722_c["nonnull_full_cohomology_dimension"] == 98470 and
          k722_c["native_null_full_cohomology_dimension"] == 106634 and
          k722_d["frozen_flat_selected_i1b_plus_displayed_eq916_realization_rejected_as_elliptic"] and
          not k722_d["source_global_SC_ACT_06_refuted"],
          "K722 flat full-symbol obstruction or realization ceiling moved")

    k723 = data["k723"]
    k723_t = k723["principal_invariance_theorem"]
    k723_c = k723["exact_controls"]
    k723_d = k723["decision"]
    check(k723_t["selected_t0_principal_ranks_are_curvature_independent"] and
          not k723_t["curved_subprincipal_transport_can_repair_principal_cohomology"] and
          k723_c["nonnull_euler_rank"] == 130912 and
          k723_c["native_null_euler_rank"] == 122748 and
          k723_c["nonnull_middle_cohomology_dimension"] == 98470 and
          k723_c["native_null_middle_cohomology_dimension"] == 106634 and
          not k723_d["k127_ricci_flat_weyl_family_repairs_k722"],
          "K723 T=0 curvature principal invariance or claim ceiling moved")

    k724 = data["k724"]
    k724_t = k724["zero_order_theorem"]
    k724_c = k724["exact_controls"]
    k724_d = k724["decision"]
    check(k724_t["K_is_action_owned"] and
          k724_t["K_is_nondegenerate_on_distortion_carrier"] and
          k724_t["kappa_term_is_zero_order"] and
          not k724_t["kappa_changes_principal_symbol"] and
          not k724_t["nonzero_kappa_repairs_k720"] and
          k724_c["distortion_K_dimension"] == 229376 and
          not k724_d["different_nonzero_kappa_is_different_principal_bosonic_data"],
          "K724 kappa zero-order obstruction or claim ceiling moved")

    k725 = data["k725"]
    k725_t = k725["nonzero_t_admission_theorem"]
    k725_d = k725["decision"]
    check(k725_t["pointwise_connection_hessian_is_full_rank"] and
          k725_t["nonzero_t_background_missing"] and
          not k725_t["pointwise_full_rank_implies_principal_ellipticity"] and
          not k725_t["current_nonzero_t_packet_is_complete_k722_repair_input"] and
          not k725_d["current_serialized_candidates_supply_new_complete_bosonic_principal_data"] and
          k725_d["nonzero_t_route_remains_open"] and
          not k725_d["source_global_SC_ACT_06_refuted"],
          "K725 current bosonic repair-input gate or source ceiling moved")

    k726 = data["k726"]
    k726_t = k726["homogeneous_branch_theorem"]
    k726_d = k726["decision"]
    check(k726_t["first_action_density"] == "7*kappa_1^3/18252" and
          k726_t["normalized_metric_euler_rank_for_nonzero_kappa"] == 1 and
          k726_t["raw_residual_zero"] and
          k726_t["residual_square_first_variation_zero"] and
          not k726_t["residual_square_cancels_metric_trace"] and
          not k726_t["nonzero_kappa_branch_is_full_stationary_background"] and
          not k726_d["current_homogeneous_nonzero_t_branch_admissible_for_k722_retest"] and
          k726_d["nonhomogeneous_or_derivative_bearing_branch_remains_open"],
          "K726 homogeneous nonzero-T stationarity obstruction or ceiling moved")

    k727 = data["k727"]
    k727_r = k727["conditional_trace_repair"]
    k727_c = k727["principal_invariance"]
    k727_d = k727["decision"]
    check(k727_r["background_metric_euler_can_be_cancelled_conditionally"] and
          not k727_r["repair_is_source_owned"] and
          k727_r["linearized_repair_differential_order"] == 0 and
          not k727_r["repair_changes_highest_order_euler_symbol"] and
          k727_c["nonnull_middle_cohomology_dimension"] == 98470 and
          k727_c["native_null_middle_cohomology_dimension"] == 106634 and
          not k727_c["principal_middle_exact_after_algebraic_repair"] and
          not k727_d["algebraic_trace_repair_is_sufficient_k722_repair"],
          "K727 algebraic trace repair principal invariance or ceiling moved")

    k728 = data["k728"]
    k728_rows = k728["candidate_census"]
    k728_t = k728["two_gate_theorem"]
    k728_d = k728["decision"]
    check(len(k728_rows) == 4 and
          not k728_rows[0]["direct_metric_euler_zero"] and
          not k728_rows[0]["full_stationary_background"] and
          not k728_rows[1]["changes_complete_principal_symbol"] and
          k728_rows[2]["rank"] == 91 and
          k728_rows[2]["differential_order"] == "LOWER_ORDER" and
          k728_rows[3]["owned_field_order"] == 1 and
          k728_rows[3]["required_field_order_at_least"] == 2 and
          not k728_t["current_serialized_packet_passes_both_gates"] and
          not k728_d["current_nonzero_t_route_admissible_for_ker_equals_image_test"] and
          k728_d["nonzero_t_route_remains_open"],
          "K728 current stationary/principal input gate or ceiling moved")

    k729 = data["k729"]
    k729_o = k729["owner_reconciliation"]
    k729_b = k729["serialized_bank"]
    k729_d = k729["decision"]
    check(k729_o["printed_endpoint_residual_square_source_owned"] and
          k729_o["residual_zero_first_variation_zero_does_not_force_zero_hessian"] and
          k729_o["i1b_and_i2b_kept_distinct"] and
          k729_b["serialized_connection_bank_dimension"] == 196 and
          k729_b["universal_extension_rank_ceiling"] == 196 and
          not k729_b["complete_moving_all_grade_i2b_symbol_serialized"] and
          k729_d["serialized_i2b_can_be_tested_as_a_favorable_repair"] and
          not k729_d["serialized_i2b_is_the_complete_moving_gu_second_action"],
          "K729 serialized I2B ownership or rank ceiling moved")

    k730 = data["k730"]
    k730_t = k730["rank_theorem"]
    k730_c = k730["exact_controls"]
    k730_d = k730["decision"]
    check(k730_t["allows_maximally_favorable_image_placement"] and
          k730_t["valid_for_every_scalar_weight"] and
          k730_t["requires_no_assumption_about_i1b_i2b_image_overlap"] and
          k730_c["i2b_universal_rank_ceiling"] == 196 and
          k730_c["nonnull_middle_cohomology_lower"] == 98274 and
          k730_c["native_null_middle_cohomology_lower"] == 106438 and
          not k730_d["serialized_i2b_bank_can_repair_k720_to_middle_exactness"] and
          k730_d["moving_all_grade_i2b_or_different_principal_owner_remains_open"],
          "K730 I1B plus I2B rank obstruction or ceiling moved")

    k731 = data["k731"]
    k731_t = k731["composition_theorem"]
    k731_c = k731["exact_controls"]
    k731_d = k731["decision"]
    check(k731_t["middle_cohomology_is_direct_sum"] and
          k731_t["mixed_boson_fermion_principal_blocks_vanish"] and
          k731_t["displayed_fermion_candidate_is_exact"] and
          not k731_t["arbitrary_weight_serialized_i2b_can_make_full_symbol_exact"] and
          k731_c["fermion_two_block_rank"] == 1920 and
          k731_c["nonnull_full_cohomology_lower"] == 98274 and
          k731_c["native_null_full_cohomology_lower"] == 106438 and
          k731_d["flat_selected_i1b_plus_any_weight_serialized_i2b_plus_displayed_eq916_realization_rejected_as_elliptic"] and
          not k731_d["source_global_SC_ACT_06_refuted"],
          "K731 displayed full-symbol obstruction or ceiling moved")

    k732 = data["k732"]
    k732_t = k732["factorization_theorem"]
    k732_e = k732["existing_all_grade_connection_response"]
    k732_d = k732["decision"]
    check(k732_t["rank_H_le_rank_J"] and
          k732_t["independent_of_pairing_signature"] and
          k732_e["domain_dimension"] == 1470 and
          k732_e["response_rank"] == 1470 and
          k732_e["i2b_hessian_rank_ceiling"] == 1470 and
          not k732_e["complete_moving_metric_epsilon_i2b_map_serialized"] and
          not k732_e["same_stationary_background_as_k720_flat_germ"] and
          k732_d["existing_response_may_be_granted_as_a_favorable_dimension_only_transfer"] and
          not k732_d["native_cross_background_composition_proved"],
          "K732 all-grade connection I2B factorization or rank ceiling moved")

    k733 = data["k733"]
    k733_g = k733["strongest_grant"]
    k733_c = k733["exact_controls"]
    k733_d = k733["decision"]
    check(k733_g["maximally_favorable_image_placement"] and
          k733_g["cross_background_transport_granted_for_dimension_test_only"] and
          not k733_g["native_cross_background_composition_claimed"] and
          k733_c["connection_i2b_rank_ceiling"] == 1470 and
          k733_c["nonnull_middle_cohomology_lower"] == 97000 and
          k733_c["native_null_middle_cohomology_lower"] == 105164 and
          k733_c["cases"][0]["minimum_new_rank_required_for_middle_exactness"] == 98470 and
          k733_c["cases"][1]["minimum_new_rank_required_for_middle_exactness"] == 106634 and
          not k733_d["existing_all_grade_connection_response_can_repair_k720_to_middle_exactness"] and
          k733_d["moving_metric_epsilon_or_other_new_principal_directions_remain_required"],
          "K733 all-grade connection bosonic repair obstruction moved")

    k734 = data["k734"]
    k734_t = k734["composition_theorem"]
    k734_c = k734["exact_controls"]
    k734_d = k734["decision"]
    check(k734_t["mixed_boson_fermion_principal_blocks_vanish"] and
          k734_t["middle_cohomology_is_direct_sum"] and
          k734_t["displayed_fermion_candidate_is_exact"] and
          not k734_t["connection_only_i2b_grant_can_make_full_symbol_exact"] and
          k734_c["fermion_two_block_rank"] == 1920 and
          k734_c["nonnull_full_cohomology_lower"] == 97000 and
          k734_c["native_null_full_cohomology_lower"] == 105164 and
          k734_d["flat_selected_i1b_plus_favorable_all_grade_connection_i2b_plus_displayed_eq916_realization_rejected_as_elliptic"] and
          not k734_d["source_global_SC_ACT_06_refuted"],
          "K734 all-grade connection displayed full-symbol obstruction moved")

    k735 = data["k735"]
    k735_t = k735["factorization_theorem"]
    k735_e = k735["selected_low_grade_tangent"]
    k735_d = k735["decision"]
    check(k735_t["rank_H_le_rank_J"] and
          k735_t["does_not_require_full_response_serialization"] and
          k735_e["connection_directions"] == 1470 and
          k735_e["primitive_epsilon_directions"] == 91 and
          k735_e["metric_directions"] == 10 and
          k735_e["source_native_y14_first_jet_total"] == 1571 and
          k735_e["i2b_hessian_rank_ceiling"] == 1571 and
          not k735_e["expanded_parent_covered"] and
          not k735_d["missing_low_grade_metric_epsilon_coefficients_can_raise_rank_above_1571"],
          "K735 selected low-grade I2B ceiling moved")

    k736 = data["k736"]
    k736_c = k736["exact_controls"]
    k736_d = k736["decision"]
    check(k736_c["selected_low_grade_i2b_rank_ceiling"] == 1571 and
          k736_c["nonnull_middle_cohomology_lower"] == 96899 and
          k736_c["native_null_middle_cohomology_lower"] == 105063 and
          k736_c["cases"][0]["minimum_rank_required_outside_selected_low_grade"] == 96899 and
          k736_c["cases"][1]["minimum_rank_required_outside_selected_low_grade"] == 105063 and
          not k736_d["complete_selected_low_grade_parent_can_repair_k720_to_middle_exactness"] and
          k736_d["expanded_parent_or_different_action_owned_principal_packet_required"],
          "K736 selected low-grade bosonic repair obstruction moved")

    k737 = data["k737"]
    k737_t = k737["exact_thresholds"]
    k737_r = k737["candidate_parent_classification"]
    k737_o = k737["ownership_controls"]
    k737_d = k737["decision"]
    check(k737_t["minimum_total_new_rank_nonnull"] == 98470 and
          k737_t["minimum_total_new_rank_native_null"] == 106634 and
          [row["dimension"] for row in k737_r] == [1131, 1571, 113893, 229477] and
          [row["dimension_meets_both_requirements"] for row in k737_r] == [False, False, True, True] and
          all(not row["actual_response_rank_proved"] for row in k737_r) and
          k737_o["moving_parent_selection"] == "OPEN_ACTION_PROJECTOR_OWNERSHIP" and
          k737_o["dimension_is_not_response_rank"] and
          k737_d["expanded_parent_action_selection_remains_open"] and
          not k737_d["source_global_SC_ACT_06_refuted"],
          "K737 expanded-parent dimension threshold or ownership ceiling moved")

    k738 = data["k738"]
    k738_t = k738["composition_theorem"]
    k738_c = k738["exact_controls"]
    k738_d = k738["decision"]
    check(k738_t["mixed_boson_fermion_principal_blocks_vanish"] and
          k738_t["displayed_fermion_candidate_is_exact"] and
          not k738_t["selected_low_grade_i2b_grant_can_make_full_symbol_exact"] and
          not k738_t["expanded_parent_full_symbol_test_performed"] and
          k738_c["nonnull_full_cohomology_lower"] == 96899 and
          k738_c["native_null_full_cohomology_lower"] == 105063 and
          k738_d["flat_selected_i1b_plus_complete_selected_low_grade_i2b_grant_plus_displayed_eq916_realization_rejected_as_elliptic"] and
          not k738_d["source_global_SC_ACT_06_refuted"],
          "K738 selected low-grade displayed full-symbol obstruction moved")

    k739 = data["k739"]
    check(k739["exact_action_ownership"]["action_owned_connection_coefficient_directions"] == 16384 and
          k739["exact_action_ownership"]["action_owned_connection_one_form_directions"] == 229376 and
          not k739["exact_action_ownership"]["hard_spin_reduction_generated_by_written_action"] and
          k739["decision"]["full_connection_carrier_is_action_owned_at_zero_branch"] and
          not k739["decision"]["operative_unitary_symmetry_parent_is_selected"],
          "K739 expanded action-parent ownership moved")

    k740 = data["k740"]
    for case in k740["exact_controls"]["cases"]:
        check(case["ranks"]["selected_low_grade"]["rank"] == 650 and
              case["ranks"]["grade_saturated_spin"]["rank"] == 60594 and
              case["ranks"]["full_connection"]["rank"] == 122864,
              "K740 expanded principal-response rank moved")
    check(not k740["operator"]["zero_order_hodge_kappa_u_included"] and
          k740["decision"]["spin_fails_both_required_thresholds_even_with_maximal_metric_epsilon_grant"] and
          k740["decision"]["full_connection_clears_both_required_thresholds_without_metric_epsilon_grant"] and
          not k740["decision"]["full_connection_middle_exactness_proved"],
          "K740 principal-response disposition moved")

    k741 = data["k741"]
    check([row["spin_middle_cohomology_lower"] for row in k741["exact_controls"]["cases"]] == [37775, 45939] and
          all(row["full_rank_threshold_cleared"] for row in k741["exact_controls"]["cases"]) and
          k741["decision"]["grade_saturated_spin_parent_excluded_even_under_favorable_metric_epsilon_grant"] and
          not k741["decision"]["action_owned_full_connection_parent_proves_middle_exactness"],
          "K741 expanded bosonic repair disposition moved")

    k742 = data["k742"]
    check(k742["composition_theorem"]["displayed_fermion_candidate_is_exact"] and
          not k742["decision"]["grade_saturated_spin_plus_displayed_fermion_realization_is_elliptic"] and
          not k742["decision"]["action_owned_full_carrier_plus_displayed_fermion_is_proved_elliptic"] and
          k742["decision"]["expanded_parent_frontier"] == "SPIN_HORN_CLOSED__ACTION_OWNED_FULL_CARRIER_HORN_SURVIVES_NECESSARY_RANK_TEST",
          "K742 expanded displayed full-symbol disposition moved")

    k743 = data["k743"]
    check([row["distortion_universal_image_cap_rank"] for row in k743["exact_controls"]["cases"]] == [131068, 131068] and
          [row["total_coupled_image_cap_rank"] for row in k743["exact_controls"]["cases"]] == [131074, 131071] and
          [row["bosonic_middle_cohomology_lower_bound"] for row in k743["exact_controls"]["cases"]] == [98308, 98311] and
          k743["decision"]["every_same_response_residual_pairing_fails_middle_exactness"] and
          not k743["decision"]["unitary_pairing_fork_selected"],
          "K743 pairing-independent residual-square image cap moved")

    k744 = data["k744"]
    check([row["hessian_rank"] for row in k744["exact_controls"]["cases"]] == [122864, 61439] and
          [row["rank_gain_over_i1b"] for row in k744["exact_controls"]["cases"]] == [162, 66] and
          [row["bosonic_middle_cohomology_after_gauge"] for row in k744["exact_controls"]["cases"]] == [98308, 106568] and
          not k744["decision"]["full_trace_pairing_repairs_middle_exactness"] and
          k744["decision"]["pairing_independent_k743_is_stronger_scope"],
          "K744 full-trace Hessian rank control moved")

    k745 = data["k745"]
    check([row["gauge_rank"] for row in k745["exact_controls"]["cases"]] == [4, 4] and
          all(row["i1b_euler_times_gauge_rank"] == 0 for row in k745["exact_controls"]["cases"]) and
          all(row["redundancy_times_i1b_euler_rank"] == 0 for row in k745["exact_controls"]["cases"]) and
          not k745["decision"]["same_response_residual_square_repair_is_elliptic"] and
          not k745["decision"]["actual_redundancy_tower_beyond_metric_diffeomorphism_owned"],
          "K745 actual gauge/redundancy obstruction moved")

    k746 = data["k746"]
    check(k746["composition_theorem"]["displayed_fermion_candidate_is_exact"] and
          k746["composition_theorem"]["middle_cohomology_is_direct_sum"] and
          not k746["composition_theorem"]["same_response_residual_pairing_can_repair_full_symbol"] and
          [row["universal_full_symbol_middle_cohomology_lower"] for row in k746["exact_controls"]["cases"]] == [98308, 98311] and
          k746["decision"]["k742_full_carrier_threshold_survivor_is_closed_for_same_response_residual_squares"] and
          not k746["decision"]["displayed_full_symbol_realization_is_elliptic"],
          "K746 same-response full-symbol obstruction moved")

    k747 = data["k747"]
    check(k747["principal_transport_theorem"]["same_response_image_cap_transports_over_certified_family"] and
          not k747["principal_transport_theorem"]["global_all_t0_stationary_germs_classified"] and
          [row["total_coupled_image_cap_rank"] for row in k747["exact_controls"]["cases"]] == [131074, 131071] and
          [row["middle_cohomology_lower_bound"] for row in k747["exact_controls"]["cases"]] == [98308, 98311] and
          not k747["decision"]["k127_curved_t0_family_repairs_same_response_obstruction"],
          "K747 T=0 response transport disposition moved")

    k748 = data["k748"]
    check(k748["ownership_theorem"]["released_t0_derivative_grammar_exhausted_by_i1b_plus_same_response_residual_squares"] and
          not k748["ownership_theorem"]["released_source_owns_third_independent_bosonic_principal_response"] and
          not k748["ownership_theorem"]["source_silent_path_adapter_is_proved_nonexistent"] and
          not k748["decision"]["another_pairing_or_weight_is_a_new_action_parent"],
          "K748 released action-parent inventory moved")

    k749 = data["k749"]
    check(k749["composition_theorem"]["certified_t0_family_same_response_obstruction"] and
          k749["composition_theorem"]["displayed_fermion_diagonal_exact"] and
          not k749["composition_theorem"]["released_t0_full_symbol_family_elliptic"] and
          [row["full_symbol_middle_cohomology_lower_bound"] for row in k749["exact_controls"]["cases"]] == [98308, 98311],
          "K749 T=0 full-symbol obstruction moved")

    k750 = data["k750"]
    check(k750["gate_theorem"]["current_homogeneous_nonzero_t_branch_rejected"] and
          k750["gate_theorem"]["current_stationary_principal_packet_absent"] and
          k750["gate_theorem"]["released_source_third_response_absent"] and
          k750["gate_theorem"]["released_t0_full_symbol_family_rejected"] and
          not k750["gate_theorem"]["global_SC_ACT_06_refuted"] and
          k750["decision"]["do_not_retry_same_response_t0_family"],
          "K750 successor input gate moved")

    k751 = data["k751"]
    check(k751["theorem"]["exact_supercomplex_implies_exact_body_complex"] and
          k751["theorem"]["nonexact_body_complex_obstructs_exact_supercomplex"] and
          not k751["theorem"]["nilpotent_off_diagonal_blocks_can_change_body_exactness"] and
          k751["exact_controls"]["obstructed_fixture_body_middle_cohomology"] == 1,
          "K751 finite-free body-reduction theorem moved")

    k752 = data["k752"]
    check(k752["composition_theorem"]["nonzero_odd_saddles_may_exist"] and
          k752["composition_theorem"]["mixed_boson_fermion_principal_body_zero"] and
          not k752["composition_theorem"]["minimal_nonzero_odd_saddle_repairs_middle_exactness"] and
          [row["body_middle_cohomology_lower_bound"] for row in k752["exact_controls"]["cases"]] == [98308, 98311],
          "K752 nonzero odd-saddle body obstruction moved")

    k753 = data["k753"]
    check(k753["admission_audit"]["normal_j4_field_plus_condensate_saddles"] == 4 and
          k753["admission_audit"]["full_metric_stationary_j4_bodies"] == 0 and
          k753["admission_audit"]["derivative_free_ultralocal_action"] and
          not k753["admission_audit"]["new_principal_derivative_image"] and
          not k753["decision"]["minimal_even_condensate_repairs_k749"],
          "K753 even-condensate reopener audit moved")

    k754 = data["k754"]
    check(k754["gate_theorem"]["minimal_nonzero_odd_class_closed"] and
          k754["gate_theorem"]["minimal_even_condensate_candidate_closed"] and
          not k754["gate_theorem"]["all_nonzero_fermion_or_condensate_actions_excluded"] and
          not k754["gate_theorem"]["global_SC_ACT_06_refuted"] and
          k754["decision"]["do_not_retry_minimal_grassmann_bilinear_saddle"] and
          k754["decision"]["do_not_retry_cbrs1r_ultralocal_condensate"],
          "K754 narrowed successor gate moved")

    k755 = data["k755"]
    check(k755["operator"]["exact_match"] and
          k755["operator"]["expected_square"] == "[[F_A-F_B,0],[d_A-d_B,0]]" and
          not k755["source_grade"]["exact_formula_released"] and
          not k755["decision"]["new_current_carrier_principal_response_proved"],
          "K755 cyclic two-connection square moved")

    k756 = data["k756"]
    check(k756["theorem"]["principal_rank_per_internal_coefficient"] == 13 and
          k756["theorem"]["combined_relative_rank_per_internal_coefficient"] == 14 and
          k756["linearization"]["common_direction_killed"] and
          not k756["decision"]["current_one_connection_complex_reopened"],
          "K756 cyclic adapter linearization moved")

    k757 = data["k757"]
    check(k757["current_obstruction"]["body_middle_bounds_preserved"] == [98308, 98311] and
          not k757["composition_theorem"]["current_carrier_reopened"] and
          not k757["composition_theorem"]["independent_doubled_adapter_can_be_inserted_without_rebuilding_complex"] and
          not k757["decision"]["cyclic_reconstruction_killed_globally"],
          "K757 cyclic adapter carrier composition moved")

    k758 = data["k758"]
    check(k758["gate_theorem"]["current_one_connection_cyclic_repair_closed"] and
          k758["gate_theorem"]["independent_doubled_candidate_exists_as_exact_algebra"] and
          not k758["gate_theorem"]["independent_doubled_candidate_is_action_owned"] and
          not k758["gate_theorem"]["global_SC_ACT_06_refuted"] and
          k758["decision"]["do_not_retry_current_carrier_cyclic_specializations"],
          "K758 cyclic adapter successor gate moved")

    k759 = data["k759"]
    check(k759["theorem"]["update_rank_bound"] == "rank(E_ext)-rank(E) <= 2m" and
          k759["theorem"]["middle_cohomology_bound"] == "dim H_ext >= dim H_old-m" and
          k759["theorem"]["requires_fixed_old_block"] and
          k759["decision"]["one_new_even_field_can_remove_at_most_one_old_middle_class"],
          "K759 even spectator rank-update theorem moved")

    k760 = data["k760"]
    check(k760["composed_formula"]["native_nonnull"] == "max(0,98308-m)" and
          k760["composed_formula"]["native_null_auxiliary_nonzero"] == "max(0,98311-m)" and
          k760["decision"]["one_scalar_bounds"] == {
              "native_nonnull": 98307,
              "native_null_auxiliary_nonzero": 98310,
          } and not k760["decision"]["one_scalar_repairs_k749"],
          "K760 derivative-condensate cohomology bound moved")

    k761 = data["k761"]
    check(k761["threshold"]["minimum_m_not_excluded_by_dimension_on_both_strata"] == 98311 and
          k761["decision"]["every_m_below_98311_excluded_from_all_covector_exactness_by_native_null_stratum"] and
          not k761["decision"]["m_at_least_98311_sufficient_for_exactness"],
          "K761 finite even extension threshold moved")

    k762 = data["k762"]
    check(k762["decision"]["SC_ACT_06_status"] == "ASSERTS" and
          k762["decision"]["do_not_retry_small_spectator_condensate_extension"] and
          k762["decision"]["changed_old_block_owner_remains_open"] and
          not k762["decision"]["global_SC_ACT_06_refuted"],
          "K762 even owner successor gate moved")

    k763 = data["k763"]
    check(k763["theorem"]["rank_update_bound"] == "rank(H)-rank(E) <= r+2m" and
          k763["theorem"]["middle_cohomology_bound"] == "dim H_ext >= dim H_old-r-m" and
          k763["theorem"]["requires_rank_bound_on_old_block_correction"] and
          not k763["decision"]["global_SC_ACT_06_refuted"],
          "K763 finite-rank even-owner theorem moved")

    k764 = data["k764"]
    check(k764["stationarity"]["full_background_stationary_relative_to_k749"] and
          k764["principal_support"]["old_block_correction_rank_upper_r"] == 10 and
          k764["principal_support"]["new_even_dimension_m"] == 1 and
          k764["principal_support"]["old_connection_update_rank"] == 0 and
          not k764["decision"]["owner_is_source_or_GU_selected"],
          "K764 scalar-metric derivative control moved")

    k765 = data["k765"]
    check(k765["composition"]["maximum_middle_class_removal_r_plus_m"] == 11 and
          k765["composition"]["new_lower_bounds"] == {
              "native_nonnull": 98297,
              "native_null_auxiliary_nonzero": 98300,
          } and not k765["decision"]["scalar_metric_control_repairs_k749"],
          "K765 scalar-metric cohomology bound moved")

    k766 = data["k766"]
    check(k766["decision"]["SC_ACT_06_status"] == "ASSERTS" and
          k766["decision"]["do_not_retry_low_rank_scalar_tensor_or_small_derivative_even_owner"] and
          k766["decision"]["large_rank_or_changed_germ_routes_remain_open"] and
          not k766["decision"]["global_SC_ACT_06_refuted"],
          "K766 derivative-even successor gate moved")

    k767 = data["k767"]
    check(k767["stationarity"]["full_flat_germ_stationary_for_comparator"] and
          k767["ward"]["curvature_hessian_annihilates_old_gauge_image"] and
          not k767["ownership"]["pure_curvature_square_is_source_I2B"] and
          not k767["decision"]["natural_high_rank_source_action_owner_constructed"],
          "K767 curvature-square control moved")

    k768 = data["k768"]
    k768_rows = k768["exact_controls"]["rows"]
    check(k768_rows[0]["connection_hessian_rank"] == 212992 and
          k768_rows[1]["connection_hessian_rank"] == 16384 and
          k768_rows[1]["connection_only_middle_cohomology_dimension"] == 196608 and
          k768_rows[3]["connection_hessian_rank"] == 212992 and
          not k768["decision"]["curvature_hessian_equals_gauge_fixed_hodge_laplacian"],
          "K768 curvature-square rank boundary moved")

    k769 = data["k769"]
    check(k769["composition"]["rows"][1]["k763_lower_bound"] == 81927 and
          not k769["decision"]["native_pairing_repairs_native_null"] and
          k769["decision"]["positive_pairing_clears_both_necessary_rank_thresholds"] and
          not k769["decision"]["positive_pairing_repairs_both_proved"],
          "K769 curvature-square cohomology bound moved")

    k770 = data["k770"]
    check(k770["decision"]["SC_ACT_06_status"] == "ASSERTS" and
          k770["decision"]["do_not_retry_native_pairing_curvature_square_comparator"] and
          k770["decision"]["do_not_promote_comparator_to_source_I2B"] and
          k770["decision"]["positive_reduction_branch_mathematically_open_but_unowned"] and
          not k770["decision"]["global_SC_ACT_06_refuted"],
          "K770 curvature-square successor gate moved")

    k771 = data["k771"]
    k771_rows = {row["case"]: row for row in k771["exact_controls"]["cases"]}
    check(k771_rows["native_nonnull"]["distortion_summed_operator_rank"] == 221183 and
          k771_rows["native_null_auxiliary_nonzero"]["distortion_summed_operator_rank"] == 221183 and
          k771_rows["native_nonnull"]["bosonic_middle_cohomology_dimension"] == 8193 and
          k771_rows["native_null_auxiliary_nonzero"]["bosonic_middle_cohomology_dimension"] == 8196 and
          not k771["decision"]["source_owned_total_action"],
          "K771 positive-curvature/I1B composition moved")

    k772 = data["k772"]
    k772_rows = {row["case"]: row for row in k772["exact_controls"]["cases"]}
    check(k772_rows["native_nonnull"]["internal_candidate_kernel_dimension"] == 8193 and
          k772_rows["native_null_auxiliary_nonzero"]["internal_candidate_kernel_dimension"] == 8193 and
          k772_rows["native_nonnull"]["candidate_kernel_equals_distortion_kernel"] and
          k772_rows["native_null_auxiliary_nonzero"]["refined_middle_cohomology_dimension"] == 8196 and
          not k772["complex_theorem"]["accidental_candidate_kernel_promoted_to_gauge"],
          "K772 positive-curvature total complex moved")

    k773 = data["k773"]
    k773_rows = {row["case"]: row for row in k773["exact_controls"]["cases"]}
    check(k773_rows["native_nonnull"]["full_symbol_middle_cohomology_dimension"] == 8193 and
          k773_rows["native_null_auxiliary_nonzero"]["full_symbol_middle_cohomology_dimension"] == 8196 and
          k773["composition_theorem"]["displayed_fermion_candidate_is_exact"] and
          not k773["decision"]["displayed_full_symbol_comparator_is_elliptic"],
          "K773 positive-curvature full symbol moved")

    k774 = data["k774"]
    check(k774["decision"]["SC_ACT_06_status"] == "ASSERTS" and
          k774["decision"]["do_not_retry_fixed_identity_cartan_unit_weight_comparator"] and
          k774["decision"]["do_not_promote_candidate_kernel_to_gauge"] and
          not k774["decision"]["source_owned_positive_family_globally_closed"] and
          not k774["decision"]["global_SC_ACT_06_refuted"],
          "K774 positive-curvature successor gate moved")

    k775 = data["k775"]
    check(k775["variation_theorem"]["residual_zero_first_variation_zero"] and
          k775["variation_theorem"]["residual_zero_hessian"] == "J_x^* Q J_x" and
          k775["variation_theorem"]["residual_zero_hessian_image_contained_in_response_adjoint_image"] and
          not k775["variation_theorem"]["residual_zero_stationarity_can_cancel_first_action_euler"],
          "K775 residual-zero variation theorem moved")

    k776 = data["k776"]
    check(k776["exact_composition"]["combined_metric_euler_rank_for_nonzero_kappa"] == 1 and
          not k776["exact_composition"]["nonzero_kappa_branch_stationary"] and
          k776["decision"]["current_homogeneous_branch_closed_for_all_fixed_residual_pairings_and_finite_weights"] and
          not k776["decision"]["global_nonzero_T_stationarity_closed"],
          "K776 homogeneous residual-square closure moved")

    k777 = data["k777"]
    check(k777["hessian_split"]["gauss_newton_term"] == "J^* Q J" and
          k777["hessian_split"]["residual_zero_kills_residual_curvature_term"] and
          k777["hessian_split"]["nonzero_residual_makes_residual_curvature_term_potentially_live"] and
          not k777["hessian_split"]["nonzero_residual_alone_proves_new_rank"] and
          not k777["decision"]["route_is_currently_constructed"],
          "K777 nonzero-residual Hessian split moved")

    k778 = data["k778"]
    check(len(k778["residual_strata"]) == 3 and
          not k778["residual_strata"][0]["stationary_for_I1B_plus_I2B"] and
          k778["residual_strata"][1]["stationary_for_I1B_plus_I2B"] and
          k778["residual_strata"][2]["stationary_for_I1B_plus_I2B"] is None and
          k778["decision"]["SC_ACT_06_status"] == "ASSERTS" and
          not k778["decision"]["global_nonzero_T_no_go_proved"],
          "K778 residual-stratum successor gate moved")

    k779 = data["k779"]
    check(k779["theorem"]["euler_covector_lies_in_image_J_star"] and
          k779["theorem"]["euler_covector_annihilates_kernel_J"] and
          not k779["theorem"]["nonzero_residual_changes_first_variation_image"] and
          not k779["decision"]["nonzero_residual_opens_new_first_variation_directions"],
          "K779 nonzero-residual Euler image theorem moved")

    k780 = data["k780"]
    check(k780["theorem"]["one_kernel_transverse_witness_rejects_candidate"] and
          not k780["theorem"]["pairing_or_finite_weight_can_cancel_transverse_component"] and
          k780["exact_control"]["transverse_kernel_pairing"] == -1 and
          k780["decision"]["compatible_candidate_admitted_to_next_gate_only"],
          "K780 kernel-transverse stationarity obstruction moved")

    k781 = data["k781"]
    check(k781["theorem"]["only_possible_new_kernel_action_is_C_U"] and
          k781["theorem"]["affine_residual_has_C_U_zero"] and
          not k781["theorem"]["nonzero_residual_alone_implies_C_U_nonzero"] and
          k781["exact_control"]["curvature_image_escapes_im_J_star"],
          "K781 residual-curvature novelty theorem moved")

    k782 = data["k782"]
    check(len(k782["required_packet"]) == 10 and
          all(value is False for value in k782["current_custody"].values()) and
          not k782["decision"]["candidate_admitted"] and
          k782["decision"]["SC_ACT_06_status"] == "ASSERTS",
          "K782 nonzero-residual two-jet admission gate moved")

    k783 = data["k783"]
    check(k783["source_custody"]["claimed_solution_locus"] == "Upsilon=0" and
          not k783["source_custody"]["source_exhibits_one_complete_solution_two_jet"] and
          k783["decision"]["zero_residual_is_required_for_direct_SC_ACT_06_test"] and
          not k783["decision"]["nonzero_residual_is_direct_SC_ACT_06_input"],
          "K783 source zero-locus boundary moved")

    k784 = data["k784"]
    check(k784["ownership"]["combined_stationarity_classification"] == "REPO_CONDITIONAL_COMPARATOR" and
          not k784["ownership"]["combined_stationarity_is_source_owned"] and
          not k784["ownership"]["source_supplies_relative_sum_coefficient"] and
          not k784["decision"]["nonzero_residual_sum_can_directly_adjudicate_SC_ACT_06"],
          "K784 action-sum ownership correction moved")

    k785 = data["k785"]
    check(all(k785["preserved_results"][key] for key in (
              "K779_first_variation_image",
              "K780_kernel_transverse_obstruction_for_fixed_sum",
              "K781_residual_curvature_decomposition",
              "K782_packet_fields_useful_for_conditional_joint_action")) and
          all(k785["withdrawn_current_inferences"].values()) and
          k785["decision"]["route_status"] ==
              "RETAINED_CONDITIONAL_MATHEMATICS__DIRECT_SC_ACT_06_ROUTE_WITHDRAWN",
          "K785 variational salvage or route withdrawal moved")

    k786 = data["k786"]
    check(len(k786["required_packet"]) == 10 and
          k786["current_custody"]["source_claim_and_zero_locus"] and
          sum(bool(value) for value in k786["current_custody"].values()) == 1 and
          not k786["decision"]["candidate_admitted"] and
          k786["decision"]["SC_ACT_06_status"] == "ASSERTS",
          "K786 zero-residual deformation input gate moved")

    k787 = data["k787"]
    check(k787["custody_reconciliation"]["repository_constructs_local_source_typed_background"] and
          not k787["custody_reconciliation"]["released_source_exhibits_complete_solution_two_jet"] and
          not k787["decision"]["background_search_remains_first_missing_input"] and
          not k787["decision"]["complete_K786_packet_supplied"],
          "K787 flat zero-locus custody moved")

    k788 = data["k788"]
    check(k788["operator"]["is_direct_first_order_linearization"] and
          not k788["operator"]["is_action_hessian"] and
          k788["decision"]["connection_response_rank"] == 122864 and
          k788["decision"]["connection_kernel_dimension"] == 106512 and
          k788["orbit_theorem"]["all_orbits_tested"] and
          k788["orbit_theorem"]["rank_constant_across_all_orbits"],
          "K788 direct-response orbit classification moved")

    k789 = data["k789"]
    check(k789["composition_theorem"]["internal_candidate_rank"] == 16384 and
          k789["composition_theorem"]["metric_diffeomorphism_rank"] == 4 and
          not k789["composition_theorem"]["internal_candidate_promoted_to_source_owned_total_gauge"] and
          k789["decision"]["uniform_middle_cohomology_lower_bound"] == 90124 and
          not k789["decision"]["all_three_orbits_middle_exact_under_maximal_grant"],
          "K789 maximal symmetry budget moved")

    k790 = data["k790"]
    check(k790["composition"]["uniform_middle_cohomology_lower_bound_after_grant"] == 90124 and
          not k790["decision"]["current_flat_packet_middle_exact"] and
          not k790["decision"]["current_flat_packet_satisfies_K786"] and
          not k790["decision"]["K717_background_itself_globally_refuted"] and
          not k790["decision"]["global_SC_ACT_06_proved_or_refuted"],
          "K790 flat zero-locus realization gate moved")

    k791 = data["k791"]
    check(k791["decision"]["released_independent_first_order_bosonic_row_count_beyond_Upsilon"] == 0 and
          k791["decision"]["only_displayed_extra_bosonic_equation_is_declared_redundant"] and
          not k791["decision"]["source_inventory_supplies_K790_missing_independent_row"] and
          k791["typing"]["i2b_row_belongs_to_distinct_second_action"],
          "K791 released first-order row inventory moved")

    k792 = data["k792"]
    check(k792["linearization"]["xi_row_factors_through_direct_response"] and
          k792["exact_consequence"]["stacked_row_kernel_dimension"] == 106512 and
          not k792["decision"]["xi_supplies_K790_missing_independent_row"] and
          not k792["decision"]["discarding_xi_changes_field_kernel"],
          "K792 redundant prolongation theorem moved")

    k793 = data["k793"]
    check(k793["extension_lemma"]["embedded_subspace_is_in_full_kernel"] and
          not k793["extension_lemma"]["adding_field_columns_can_delete_old_kernel_vectors"] and
          k793["exact_bound"]["persistent_middle_classes_lower_bound"] == 90124 and
          not k793["decision"]["released_full_field_extension_repairs_K790"],
          "K793 full-field kernel persistence moved")

    k794 = data["k794"]
    check(k794["decision"]["K717_direct_released_source_packet_closed"] and
          not k794["decision"]["K717_is_complete_elliptic_realization_under_released_serialization"] and
          not k794["decision"]["global_SC_ACT_06_proved_or_refuted"] and
          k794["composition"]["uniform_persistent_middle_classes"] == 90124,
          "K794 released flat-realization closure moved")

    k795 = data["k795"]
    check(k795["decision"]["conditional_compiler_chain_complete"] and
          not k795["decision"]["current_native_A_packet_complete"] and
          not k795["decision"]["current_native_B_packet_complete"] and
          not k795["decision"]["current_complete_K500_AB_packet_executable"] and
          "neither gate substitutes" in k795["decision_interface"]["final_requirement"],
          "K795 complete A/B decision interface moved")

    k796 = data["k796"]
    check(k796["theorem"]["all_four_A_B_truth_pairs_realized"] and
          k796["theorem"]["A_and_B_missing_inputs_are_logically_independent"] and
          not k796["theorem"]["current_projection_entails_complete_K500_AB"] and
          not k796["theorem"]["seed_data_determines_complete_A"] and
          not k796["theorem"]["finite_prefix_determines_complete_B"],
          "K796 current-custody product countermodels moved")

    k797 = data["k797"]
    check(k797["decision"]["current_serialized_K500_assembly_route_closed"] and
          k797["decision"]["new_native_data_required"] and
          not k797["dependency_reconciliation"]["future_native_AB_packet_excluded"] and
          k797["no_assembly_theorem"]["therefore_projection_does_not_entail_A_and_B"],
          "K797 current-custody no-assembly theorem moved")

    k798 = data["k798"]
    check(k798["decision"]["unchanged_current_custody_K500_AB_packet_closed"] and
          not k798["decision"]["complete_native_K500_route_killed"] and
          not k798["decision"]["K473_or_K152_released"] and
          not k798["decision"]["conditional_compilers_retracted"] and
          not k798["decision"]["source_or_physics_verdict_changed"],
          "K798 current-packet closure moved")

    k799 = data["k799"]
    check(k799["transport_theorem"]["normal_frame_freezes_highest_order_coefficients"] and
          k799["transport_theorem"]["curvature_changes_only_subprincipal_or_lower_order_transport"] and
          not k799["transport_theorem"]["global_all_t0_or_all_zero_locus_germs_classified"] and
          k799["decision"]["connection_response_rank"] == 122864 and
          k799["decision"]["connection_kernel_dimension"] == 106512,
          "K799 curved T0 direct-response transport moved")

    k800 = data["k800"]
    check(k800["composition"]["xi_principal_row_factors_through_D_Upsilon"] and
          not k800["composition"]["candidate_internal_symmetry_promoted_to_owned_gauge"] and
          not k800["composition"]["global_all_zero_locus_germs_classified"] and
          k800["exact_bound"]["persistent_middle_classes_lower_bound"] == 90124 and
          not k800["decision"]["curvature_only_family_middle_exact_under_maximal_grant"],
          "K800 curved T0 full-field kernel persistence moved")

    k801 = data["k801"]
    check(k801["theorem"]["curvature_twojet_changes_subprincipal_transport"] and
          not k801["theorem"]["curvature_twojet_changes_direct_principal_response"] and
          not k801["theorem"]["all_t0_or_all_zero_locus_germs_classified"] and
          not k801["decision"]["k127_curvature_only_family_reopens_k794"] and
          not k801["decision"]["global_sc_act_06_proved_or_refuted"],
          "K801 curvature-only reopener theorem moved")

    k802 = data["k802"]
    check(k802["decision"]["certified_k127_t0_family_packet_closed"] and
          not k802["decision"]["certified_k127_t0_family_is_complete_elliptic_realization_under_released_packet"] and
          not k802["decision"]["all_t0_or_all_zero_locus_germs_closed"] and
          not k802["decision"]["global_sc_act_06_proved_or_refuted"] and
          k802["protected_effects"]["sc_act_06"] == "ASSERTS_UNCHANGED",
          "K802 certified T0 family closure moved")

    k803 = data["k803"]
    check(k803["frechet_calculus"]["background_A_commutator_is_lower_order"] and
          k803["frechet_calculus"]["hodge_u_is_zero_order"] and
          not k803["frechet_calculus"]["background_T_enters_principal_connection_symbol"] and
          not k803["frechet_calculus"]["nonzero_T_alone_changes_principal_response"] and
          k803["orbit_consequence"]["connection_response_rank"] == 122864 and
          k803["orbit_consequence"]["connection_kernel_dimension"] == 106512,
          "K803 nonzero-T principal invariance moved")

    k804 = data["k804"]
    check(k804["extension_theorem"]["xi_principal_row_factors_through_D_Upsilon"] and
          not k804["extension_theorem"]["xi_acts_nontrivially_on_connection_kernel"] and
          k804["extension_theorem"]["embedded_kernel_dimension_in_full_field_symbol"] == 106512 and
          not k804["decision"]["fixed_structure_released_full_field_packet_middle_exact_before_symmetry"],
          "K804 fixed-structure full-field kernel moved")

    k805 = data["k805"]
    check(k805["threshold_theorem"]["minimum_owned_symmetry_rank_needed_if_no_new_row"] == 106512 and
          k805["threshold_theorem"]["persistent_middle_classes_under_current_grant"] == 90124 and
          not k805["threshold_theorem"]["candidate_internal_symmetry_is_source_owned_total_gauge"] and
          not k805["decision"]["current_grant_closes_fixed_structure_packet"],
          "K805 fixed-structure symmetry threshold moved")

    k806 = data["k806"]
    check(not k806["decision"]["nonzero_T_alone_reopens_certified_packet"] and
          not k806["decision"]["all_nonzero_T_or_non_levi_civita_zero_locus_germs_closed"] and
          not k806["decision"]["moving_principal_geometry_closed"] and
          not k806["decision"]["global_sc_act_06_proved_or_refuted"] and
          k806["protected_effects"]["sc_act_06"] == "ASSERTS_UNCHANGED",
          "K806 nonzero-T-alone closure moved")

    k807 = data["k807"]
    check(k807["intertwiner_theorem"]["pure_frame_motion_is_basis_change"] and
          k807["intertwiner_theorem"]["moving_projector_cocycle_exact"] and
          not k807["intertwiner_theorem"]["genuine_relative_coefficient_motion_covered"] and
          k807["orbit_consequence"]["transported_rank"] == 122864 and
          k807["orbit_consequence"]["transported_kernel_dimension"] == 106512 and
          not k807["decision"]["comoving_frame_orbit_is_new_principal_packet"],
          "K807 co-moving principal conjugacy moved")

    k808 = data["k808"]
    check(k808["extension_theorem"]["pure_connection_subspace_intertwined"] and
          k808["extension_theorem"]["xi_row_factors_through_transported_D_Upsilon"] and
          not k808["extension_theorem"]["extra_transported_field_columns_delete_pure_connection_kernel"] and
          k808["extension_theorem"]["embedded_transported_kernel_dimension"] == 106512 and
          not k808["decision"]["comoving_full_field_packet_middle_exact_before_symmetry"],
          "K808 co-moving full-field kernel moved")

    k809 = data["k809"]
    check(k809["quotient_transport"]["same_domain_intertwiner_used"] and
          not k809["quotient_transport"]["basis_motion_creates_owned_symmetry"] and
          k809["quotient_transport"]["transported_current_grant_rank"] == 16388 and
          k809["quotient_transport"]["transported_kernel_dimension"] == 106512 and
          k809["quotient_transport"]["transported_persistent_classes"] == 90124 and
          not k809["decision"]["current_transported_grant_closes_packet"],
          "K809 co-moving symmetry quotient moved")

    k810 = data["k810"]
    check(not k810["composition"]["regular_comoving_frame_changes_principal_rank"] and
          not k810["composition"]["genuine_relative_coefficient_motion_available"] and
          k810["composition"]["persistent_classes_under_current_grant"] == 90124 and
          not k810["decision"]["regular_comoving_frame_reopens_certified_packet"] and
          not k810["decision"]["all_moving_principal_geometry_closed"] and
          not k810["decision"]["global_sc_act_06_proved_or_refuted"] and
          k810["protected_effects"]["sc_act_06"] == "ASSERTS_UNCHANGED",
          "K810 co-moving-frame closure moved")

    k811 = data["k811"]
    check(k811["rank_theorem"]["reference_kernel_dimension"] == 106512 and
          k811["rank_theorem"]["maximal_current_grant"] == 16388 and
          k811["rank_theorem"]["minimum_relative_rank_with_current_grant"] == 90124 and
          k811["rank_theorem"]["bound_is_necessary_not_sufficient"] and
          not k811["decision"]["threshold_proves_ellipticity"],
          "K811 relative-response rank budget moved")

    k812 = data["k812"]
    check(k812["transverse_theorem"]["block"] == "tau=pi_Q o Delta|ker(J)" and
          k812["transverse_theorem"]["post_current_grant_lift_requires_induced_rank"] == 90124 and
          k812["transverse_theorem"]["cokernel_capacity_must_be_checked"] and
          not k812["transverse_theorem"]["finite_parameter_sufficiency_follows"] and
          k812["exact_controls"]["absorbed_sum_rank"] == 3 and
          k812["exact_controls"]["sharp_sum_rank"] == 7,
          "K812 relative transverse block moved")

    k813 = data["k813"]
    check(k813["combined_budget_theorem"]["class_lower_bound"] == "max(0,90124-r-s)" and
          k813["combined_budget_theorem"]["beyond_current_grant_condition"] == "r+s>=90124" and
          k813["combined_budget_theorem"]["new_symmetry_must_compose_to_zero"] and
          not k813["combined_budget_theorem"]["necessary_condition_is_sufficient"] and
          not k813["decision"]["current_candidate_grant_promoted_to_owned_gauge"],
          "K813 relative full-field symmetry budget moved")

    k814 = data["k814"]
    check(k814["necessary_packet"]["transverse_rank_plus_new_authenticated_symmetry_minimum"] == 90124 and
          not k814["necessary_packet"]["threshold_is_sufficient_for_ellipticity"] and
          k814["closure"]["low_budget_relative_motion_closed_as_sufficient_repair"] and
          not k814["closure"]["all_relative_motion_closed"] and
          not k814["closure"]["global_sc_act_06_proved_or_refuted"] and
          k814["protected_effects"]["sc_act_06"] == "ASSERTS_UNCHANGED",
          "K814 relative packet gate moved")

    k815 = data["k815"]
    check(k815["tangent_theorem"]["necessary_cokernel_condition"] == "pi_coker(J)(b)=0" and
          not k815["tangent_theorem"]["parameter_source_equals_principal_correction"] and
          k815["tangent_theorem"]["cokernel_failure_rejects_solution_germ"] and
          not k815["decision"]["actual_relative_germ_constructed"],
          "K815 zero-locus tangent compatibility moved")

    k816 = data["k816"]
    check(k816["overlap_theorem"]["composition_requirement"] == "G subset ker(tau)" and
          k816["exact_controls"]["symmetry_union_rank"] == 3 and
          k816["exact_controls"]["exact_unresolved_dimension"] == 1 and
          not k816["decision"]["budget_without_overlap_is_credited"],
          "K816 response/symmetry overlap moved")

    k817 = data["k817"]
    check(k817["schur_theorem"]["invertible_tau_implies_punctured_local_invertibility"] and
          not k817["schur_theorem"]["deficient_tau_implies_no_finite_parameter_repair"] and
          k817["exact_controls"]["higher_order_family"]["determinant"] == "t^3" and
          not k817["decision"]["finite_parameter_gu_ellipticity_proved"],
          "K817 finite-parameter Schur gate moved")

    k818 = data["k818"]
    check(not k818["uniformity_theorem"]["finite_samples_imply_all_covectors"] and
          k818["uniformity_theorem"]["finite_orbit_representatives_suffice_only_with_proved_equivariance_and_orbit_coverage"] and
          k818["exact_controls"]["missed_zero_determinant"] == 0 and
          not k818["decision"]["all_covector_exactness_proved_for_gu"],
          "K818 uniform covector gate moved")

    k819 = data["k819"]
    check(not k819["second_order_theorem"]["first_order_pass_implies_second_order_pass"] and
          k819["second_order_theorem"]["kernel_choice_must_be_solved"] and
          not k819["exact_controls"]["obstructed_real_second_order_solution_exists"] and
          k819["exact_controls"]["repairable_kernel_speeds"] == [-1, 1] and
          not k819["decision"]["actual_source_two_jet_constructed"],
          "K819 second-order zero-locus obstruction moved")

    k820 = data["k820"]
    check(k820["differentiated_complex_theorem"]["left_identity"] == "Delta G0 + J0 Gdot = 0" and
          k820["differentiated_complex_theorem"]["right_identity"] == "Rdot J0 + R0 Delta = 0" and
          not k820["differentiated_complex_theorem"]["rank_budget_without_identities_is_credited"] and
          k820["exact_controls"]["invalid_gauge_rejected"] and
          k820["exact_controls"]["invalid_redundancy_rejected"],
          "K820 differentiated-complex compatibility moved")

    k821 = data["k821"]
    check(k821["slice_theorem"]["dimension_condition"] == "dim(Z)=rank(G)" and
          k821["slice_theorem"]["arbitrary_extra_rows_may_erase_physical_classes"] and
          k821["exact_controls"]["invalid_middle_cohomology_dimension"] == 1 and
          k821["exact_controls"]["arbitrary_stack_rank"] == 3 and
          not k821["exact_controls"]["arbitrary_rows_are_gauge_slice"] and
          not k821["decision"]["source_gauge_slice_authenticated"],
          "K821 quotient/slice equivalence moved")

    k822 = data["k822"]
    check(k822["uniform_persistence_theorem"]["common_interval"] == "0 < |t| <= mu/(2C)" and
          not k822["uniform_persistence_theorem"]["pointwise_thresholds_imply_common_interval"] and
          k822["exact_controls"]["actual_gap_at_test_t"] == "5/16" and
          not k822["exact_controls"]["common_punctured_interval_exists"] and
          not k822["decision"]["actual_gu_uniform_interval_proved"],
          "K822 joint parameter-covector uniformity moved")

    k823 = data["k823"]
    check(not k823["stationarity_transport_theorem"]["zero_locus_transport_implies_stationarity_transport"] and
          k823["stationarity_transport_theorem"]["stationarity_is_required_before_action_hessian_credit"] and
          k823["exact_controls"]["nonstationary_first_jet_residual"] == 1 and
          not k823["exact_controls"]["nonstationary_stationarity_transport_passes"] and
          not k823["decision"]["actual_source_action_family_constructed"],
          "K823 stationarity transport gate moved")

    k824 = data["k824"]
    check(k824["mixed_symbol_schur_theorem"]["effective_bosonic_symbol"] == "S_B=B-C F^-1 D" and
          not k824["mixed_symbol_schur_theorem"]["one_sided_mixed_block_repairs_bosonic_kernel"] and
          k824["exact_controls"]["one_sided_full_nullity"] == 1 and
          k824["exact_controls"]["two_sided_full_nullity"] == 0 and
          not k824["decision"]["actual_source_mixed_packet_constructed"],
          "K824 mixed-symbol Schur gate moved")

    k825 = data["k825"]
    check(not k825["common_domain_theorem"]["pointwise_closed_or_self_adjoint_implies_common_domain"] and
          not k825["exact_controls"]["domains_equal"] and
          k825["exact_controls"]["reflection_maps_D0_onto_D1"] and
          k825["exact_controls"]["transported_graph_norm_constant"] == 1 and
          not k825["decision"]["actual_gu_common_domain_constructed"],
          "K825 common analytic-domain gate moved")

    k826 = data["k826"]
    check(not k826["ownership_theorem"]["owned_endpoints_determine_relative_coefficient"] and
          not k826["ownership_theorem"]["owned_endpoints_determine_parameter_normalization"] and
          k826["exact_controls"]["Delta_A_rank"] == 1 and
          k826["exact_controls"]["Delta_B_rank"] == 0 and
          not k826["decision"]["actual_source_relative_family_constructed"],
          "K826 relative-coefficient ownership gate moved")

    k827 = data["k827"]
    check(k827["jet_invariance_theorem"]["vanishing_order_preserved"] and
          k827["jet_invariance_theorem"]["first_order_rank_preserved"] and
          not k827["jet_invariance_theorem"]["singular_change_is_same_normalization_class"] and
          k827["exact_controls"]["regular_composite_vanishing_order"] == 1 and
          k827["exact_controls"]["singular_composite_vanishing_order"] == 2 and
          not k827["decision"]["actual_source_normalization_constructed"],
          "K827 regular parameter-jet invariance moved")

    k828 = data["k828"]
    check(not k828["domain_transport_theorem"]["domain_bijection_alone_defines_derivative"] and
          k828["domain_transport_theorem"]["jump_transport_has_uniform_bounds"] and
          not k828["domain_transport_theorem"]["jump_transport_is_differentiable"] and
          k828["exact_controls"]["conjugated_derivative_matches_commutator"] and
          not k828["decision"]["actual_gu_domain_transport_constructed"],
          "K828 differentiable domain transport moved")

    k829 = data["k829"]
    check(k829["schur_complex_theorem"]["factorization"] == "P M L=S" and
          not k829["schur_complex_theorem"]["kernel_equivalence_alone_authenticates_reduced_complex"] and
          k829["exact_controls"]["M_G"] == [0, 0, 0] and
          k829["exact_controls"]["R_M"] == [0, 0, 0] and
          k829["exact_controls"]["gauge_image_equals_reduced_kernel"] and
          not k829["decision"]["actual_gu_mixed_complex_constructed"],
          "K829 Schur complex compatibility moved")

    k830 = data["k830"]
    check(k830["compiler"]["row_count"] == 18 and
          not k830["compiler"]["partial_pass_implies_ellipticity"] and
          k830["exact_controls"]["synthetic_candidate_admitted"] and
          not k830["exact_controls"]["single_missing_candidate_admitted"] and
          k830["exact_controls"]["current_gu_missing_row_count"] == 18 and
          not k830["decision"]["actual_gu_candidate_admitted"],
          "K830 relative-family admission compiler moved")

    k831 = data["k831"]
    check(k831["operator_theorem"]["principal_symbol_invertible_for_nonzero_covector"] and
          not k831["operator_theorem"]["bounded_below_modulo_kernel"] and
          not k831["operator_theorem"]["fredholm"] and
          k831["exact_controls"]["derivative_norm_squared"] == ["1/2", "1/8", "1/32", "1/128"] and
          k831["exact_controls"]["compact_control_fredholm"] and
          not k831["decision"]["actual_gu_fredholm_domain_constructed"],
          "K831 noncompact Fredholm boundary moved")

    k832 = data["k832"]
    check(k832["obstructed_control"]["cokernel_obstruction_coefficient"] == 2 and
          not k832["obstructed_control"]["second_order_lift_exists"] and
          k832["obstructed_control"]["actual_local_dimension"] == 0 and
          k832["unobstructed_control"]["second_order_equation_residual"] == 0 and
          not k832["decision"]["actual_gu_unobstructedness_proved"],
          "K832 Kuranishi obstruction gate moved")

    k833 = data["k833"]
    check(k833["nonfree_control"]["generator_ranks"] == [0, 1, 1, 1] and
          not k833["nonfree_control"]["orbit_type_constant"] and
          not k833["nonfree_control"]["quotient_is_smooth_manifold_without_boundary_near_origin"] and
          k833["free_control"]["action_proper"] and
          k833["free_control"]["quotient_is_smooth_one_manifold"] and
          not k833["decision"]["actual_gu_local_slice_constructed"],
          "K833 quotient regularity gate moved")

    k834 = data["k834"]
    check(k834["compiler"]["family_row_count"] == 18 and
          k834["compiler"]["post_symbol_row_count"] == 7 and
          k834["compiler"]["total_row_count"] == 25 and
          not k834["compiler"]["elliptic_complex_implies_rich_moduli"] and
          k834["exact_controls"]["missing_nonlinear_elliptic_admitted"] and
          not k834["exact_controls"]["missing_nonlinear_rich_moduli_admitted"] and
          k834["exact_controls"]["current_gu_missing_row_count"] == 25 and
          not k834["decision"]["actual_gu_rich_moduli_admitted"],
          "K834 rich-moduli admission compiler moved")

    k835 = data["k835"]
    check(k835["exact_controls"]["first_obstruction_orders"] == [2, 3, 4] and
          k835["exact_controls"]["quadratic_obstruction_vanishes_for_orders"] == [3, 4] and
          not k835["theorem"]["vanishing_quadratic_obstruction_determines_integrability"] and
          not k835["theorem"]["any_fixed_finite_jet_order_is_universal"] and
          not k835["decision"]["actual_gu_kuranishi_germ_constructed"],
          "K835 higher-order Kuranishi obstruction moved")

    k836 = data["k836"]
    check(k836["smooth_control"]["all_derivatives_of_f_at_origin_zero"] and
          k836["smooth_control"]["formal_taylor_series"] == "0" and
          k836["smooth_control"]["formal_zero_set_dimension"] == 1 and
          k836["smooth_control"]["actual_local_dimension"] == 0 and
          not k836["theorem"]["complete_formal_series_determines_smooth_zero_germ"] and
          not k836["decision"]["actual_gu_smooth_kuranishi_map_constructed"],
          "K836 smooth flat obstruction moved")

    k837 = data["k837"]
    check(k837["analytic_identity_theorem"]["convergent_taylor_series_determines_local_germ"] and
          k837["analytic_identity_theorem"]["all_taylor_coefficients_zero_implies_local_zero_germ"] and
          not k837["analytic_identity_theorem"]["finite_jet_order_suffices_without_degree_bound"] and
          k837["category_boundary"]["regularity_category_must_be_declared"] and
          not k837["decision"]["actual_gu_regular_category_declared"],
          "K837 analytic category closure moved")

    k838 = data["k838"]
    check(k838["compiler"]["k834_row_count"] == 25 and
          k838["compiler"]["new_row_count"] == 2 and
          k838["compiler"]["total_row_count"] == 27 and
          not k838["compiler"]["finite_jet_or_formal_data_alone_admissible"] and
          k838["exact_controls"]["category_complete_admitted"] and
          not k838["exact_controls"]["finite_jet_only_admitted"] and
          k838["exact_controls"]["current_gu_missing_row_count"] == 27 and
          not k838["decision"]["actual_gu_rich_moduli_admitted"],
          "K838 nonlinear-germ admission compiler moved")

    k839 = data["k839"]
    check(k839["finite_cutoff_limit_certificate"]["finite_section"]["inverse_norm_rule"] == "N" and
          k839["finite_cutoff_limit_certificate"]["capped_full_space_cutoff"]["operator_norm_convergence_to_T"] and
          k839["finite_cutoff_limit_certificate"]["uniform_inverse_bound"] is False and
          k839["limit_certificate"]["range_dense"] and
          not k839["limit_certificate"]["range_closed"] and
          not k839["limit_certificate"]["fredholm"] and
          not k839["decision"]["actual_gu_cutoff_family_or_limit_domain_constructed"],
          "K839 finite-cutoff limit gate moved")

    k840 = data["k840"]
    check(k840["collapsing_family"]["inverse_derivative_norm"] == "||(Df_N(0))^-1||=N" and
          k840["pointwise_ift_certificate"]["largest_open_zero_isolation_radius"] == "1/N" and
          not k840["uniform_failure_certificate"]["positive_N_uniform_injectivity_radius_exists"] and
          k840["well_conditioned_control"]["uniform_certified_radius"] == "1/4" and
          k840["controls"]["controls_passed"] == 47 and
          not k840["decision"]["actual_gu_uniform_nonlinear_radius_proved"],
          "K840 collapsing nonlinear radius gate moved")

    k841 = data["k841"]
    check(k841["analytic_hilbert_map"]["real_analytic"] and
          k841["finite_cutoffs"]["zero_count_formula"] == "2^N" and
          k841["finite_cutoffs"]["origin_is_isolated_for_every_finite_cutoff"] and
          not k841["full_space_zero_set"]["origin_is_isolated"] and
          k841["full_space_zero_set"]["norm_limit"] == "1/N -> 0" and
          not k841["decision"]["actual_gu_hilbert_kuranishi_map_constructed"],
          "K841 analytic Hilbert zero-accumulation gate moved")

    k842 = data["k842"]
    check(k842["compiler"]["k838_row_count"] == 27 and
          k842["compiler"]["new_row_count"] == 3 and
          k842["compiler"]["total_row_count"] == 30 and
          not k842["compiler"]["finite_cutoff_exactness_alone_admissible"] and
          k842["exact_controls"]["infinite_dimensional_complete_admitted"] and
          not k842["exact_controls"]["finite_cutoff_only_admitted"] and
          k842["exact_controls"]["current_gu_missing_row_count"] == 30 and
          not k842["decision"]["actual_gu_rich_moduli_admitted"],
          "K842 infinite-dimensional admission compiler moved")

    k843 = data["k843"]
    check(k843["theorem"]["positive_middle_symbol_cohomology_required"] and
          k843["theorem"]["open_covector_cone_required"] and
          not k843["theorem"]["local_elliptic_quotient_estimate_holds"] and
          k843["theorem"]["quotient_to_residual_ratio_growth_exponent"] == 1 and
          k843["decision"]["local_high_frequency_obstruction_obtained"] and
          not k843["decision"]["global_fredholmness_adjudicated_without_a_global_realization"],
          "K843 microlocal cohomology obstruction moved")

    k844 = data["k844"]
    check(k844["hypothesis_match"]["open_covector_cone"] == "native_positive" and
          k844["hypothesis_match"]["connection_symbol_kernel_on_cone"] == 106512 and
          k844["hypothesis_match"]["middle_symbol_cohomology_lower_bound"] == 90124 and
          not k844["hypothesis_match"]["global_torus_or_compact_realization_assumed"] and
          not k844["microlocal_consequence"]["current_flat_symbol_complex_is_middle_elliptic"] and
          not k844["microlocal_consequence"]["local_first_order_elliptic_quotient_estimate_holds"] and
          not k844["decision"]["global_SC_ACT_06_proved_or_refuted"],
          "K844 flat symbol Sobolev obstruction moved")

    k845 = data["k845"]
    check(not k845["principal_invariance_theorem"]["lower_order_only_repair_restores_local_elliptic_estimate"] and
          not k845["principal_invariance_theorem"]["nonlinear_terms_with_same_linearization_change_principal_symbol"] and
          k845["repair_budget"]["necessary_threshold"] == "r+s>=90124" and
          not k845["repair_budget"]["threshold_is_sufficient"] and
          not k845["decision"]["current_lower_order_or_same_linearization_repair_route_open"],
          "K845 lower-order repair boundary moved")

    k846 = data["k846"]
    check(k846["composition"]["uniform_middle_symbol_cohomology_lower_bound"] == 90124 and
          not k846["composition"]["local_elliptic_quotient_estimate"] and
          not k846["decision"]["K717_current_serialized_packet_is_direct_elliptic_realization"] and
          not k846["decision"]["SC_ACT_06_source_claim_proved_or_refuted"] and
          not k846["decision"]["source_register_or_ledger_moves"] and
          len(k846["decision"]["reopeners"]) == 4,
          "K846 flat function-space disposition moved")

    k847 = data["k847"]
    check(k847["theorem"]["exactness_criterion"] == "im(S_bar)=ker(tau_bar)" and
          k847["theorem"]["dimension_formula"] == "h_new=h_old-rank(tau_bar)-rank(S_bar)" and
          not k847["theorem"]["raw_rank_budget_is_sufficient"] and
          k847["exact_control"]["middle_exact_after_repair"] and
          k847["exact_control"]["new_middle_cohomology_dimension"] == 0 and
          not k847["decision"]["source_owned_GU_repair_constructed"],
          "K847 quotient repair theorem moved")

    k848 = data["k848"]
    check(k848["comparison"]["all_raw_budgets_equal_old_h"] and
          k848["comparison"]["pass_effective_split"] == [1, 1] and
          k848["comparison"]["duplicate_response_effective_split"] == [0, 1] and
          k848["comparison"]["gauge_overlap_effective_split"] == [1, 0] and
          not k848["comparison"]["raw_rank_threshold_decides_exactness"] and
          k848["decision"]["response_rows_already_in_old_equation_span_get_zero_credit"],
          "K848 raw-rank overlap countermodels moved")

    k849 = data["k849"]
    check(k849["certificate"]["row_count"] == 10 and
          k849["certificate"]["core_equality"] == "im(S_bar)=ker(tau_bar)" and
          not k849["certificate"]["raw_rank_substitution_allowed"] and
          k849["exact_controls"]["complete_synthetic_candidate"]["admitted"] and
          k849["exact_controls"]["all_single_row_omissions_rejected"] and
          not k849["decision"]["source_owned_GU_candidate_admitted"],
          "K849 exact repair certificate moved")

    k850 = data["k850"]
    check(k850["current_flat_packet"]["old_middle_cohomology_lower_bound"] == 90124 and
          not k850["current_flat_packet"]["kernel_image_equality_every_q"] and
          k850["future_packet_contract"]["for_each_nonzero_covector_q"] and
          not k850["future_packet_contract"]["raw_rank_budget_is_sufficient"] and
          not k850["decision"]["current_flat_packet_passes_certificate"] and
          not k850["decision"]["SC_ACT_06_proved_or_refuted"],
          "K850 flat quotient repair interface moved")

    k851 = data["k851"]
    check(k851["theorem"]["pointwise_exactness"] ==
          "im(S_bar_q)=ker(tau_bar_q) for every q in K" and
          not k851["theorem"]["uniform_gap_is_separate_input_after_hypotheses"] and
          k851["exact_family_control"]["all_cardinal_exact"] and
          k851["exact_family_control"]["analytic_uniform_gap"] == 1 and
          not k851["decision"]["finite_covector_sampling_sufficient"] and
          not k851["decision"]["source_owned_GU_maps_constructed"],
          "K851 compact-cosphere Hodge-gap theorem moved")

    k852 = data["k852"]
    check(k852["controls"]["noncompact_continuous_exact"]["gap_infimum"] == 0 and
          k852["controls"]["compact_discontinuous_exact"]["gap_infimum"] == 0 and
          k852["controls"]["compact_continuous_nonexact"]["gap_minimum"] == 0 and
          k852["controls"]["compact_continuous_exact_positive"]["gap_minimum"] == 1 and
          k852["decision"]["compactness_is_load_bearing"] and
          k852["decision"]["continuity_is_load_bearing"] and
          k852["decision"]["pointwise_exactness_is_load_bearing"] and
          not k852["decision"]["finite_sampling_proves_uniformity"],
          "K852 uniformity failure controls moved")

    k853 = data["k853"]
    check(k853["theorem"]["composition_is_required"] and
          k853["theorem"]["hodge_difference_bound"] ==
          "||L'_q-L_q||<=2(T+R)epsilon+2epsilon^2" and
          not k853["theorem"]["positive_hodge_without_composition_certifies_a_complex"] and
          k853["exact_controls"]["certified_radius"]["bound_below_mu"] and
          k853["exact_controls"]["safe_diagonal_perturbation"]["middle_exact"] and
          not k853["exact_controls"]["composition_breaker"]["valid_complex"] and
          not k853["decision"]["arbitrary_perturbations_preserve_complex_structure"],
          "K853 robust exactness radius moved")

    k854 = data["k854"]
    check(k854["certificate"]["exact_row_count"] == 14 and
          k854["certificate"]["robust_row_count"] == 15 and
          not k854["certificate"]["raw_rank_substitution_allowed"] and
          not k854["certificate"]["uniform_gap_is_an_independent_GU_input"] and
          k854["exact_controls"]["complete_synthetic_candidate"]["robust_admitted"] and
          k854["exact_controls"]["all_single_row_omissions_reject_robust_admission"] and
          not k854["decision"]["current_flat_packet_exact_admitted"] and
          not k854["decision"]["current_flat_packet_robust_admitted"] and
          not k854["decision"]["SC_ACT_06_proved_or_refuted"],
          "K854 robust quotient repair certificate moved")

    k855 = data["k855"]
    check(k855["decision"]["constant_rank_old_complex_produces_cohomology_bundle"] and
          not k855["decision"]["current_flat_packet_complete_cosphere_bundle_established"] and
          not k855["decision"]["source_owned_repair_maps_constructed"] and
          not k855["decision"]["SC_ACT_06_proved_or_refuted"],
          "K855 cohomology bundle theorem moved")

    k856 = data["k856"]
    check(k856["exact_controls"]["stable_h14"] and
          k856["exact_controls"]["stable_h90124"] and
          not k856["decision"]["high_rank_S13_bundle_has_topological_clutching_obstruction"] and
          not k856["decision"]["current_flat_packet_bundle_hypotheses_established"] and
          not k856["decision"]["SC_ACT_06_proved_or_refuted"],
          "K856 S13 stable triviality theorem moved")

    k857 = data["k857"]
    check(k857["decision"]["abstract_continuous_exact_repair_exists_under_hypotheses"] and
          not k857["decision"]["topological_triviality_selects_GU_maps"] and
          not k857["decision"]["source_owned_repair_maps_constructed"] and
          not k857["decision"]["current_flat_packet_repaired"] and
          not k857["decision"]["SC_ACT_06_proved_or_refuted"],
          "K857 abstract orthogonal repair moved")

    k858 = data["k858"]
    check(k858["decision"]["pure_topological_nonexistence_route_closed_conditionally"] and
          k858["decision"]["ownership_and_complete_family_are_now_the_decisive_gates"] and
          not k858["decision"]["current_flat_packet_repaired"] and
          not k858["decision"]["current_flat_packet_repairability_refuted"] and
          not k858["decision"]["SC_ACT_06_proved_or_refuted"] and
          not k858["compiled_result"]["source_or_action_ownership_supplied"],
          "K858 topological repair disposition moved")

    k859 = data["k859"]
    check(k859["rank_theorem"]["conditional_exact_rank_interval"] == [90124, 106512] and
          k859["rank_theorem"]["lower_bound_is_not_exact_rank"] and
          not k859["decision"]["current_exact_old_cohomology_rank_known"] and
          not k859["decision"]["90124_promoted_to_exact_bundle_rank"] and
          not k859["decision"]["SC_ACT_06_proved_or_refuted"],
          "K859 cohomology rank custody moved")

    k860 = data["k860"]
    check(k860["theorem"]["bijection"] == "Hom_G(E,F)=Hom_H(U,V)" and
          k860["decision"]["source_naturality_requires_isotropy_intertwiners"] and
          not k860["decision"]["current_GU_isotropy_modules_authenticated"] and
          not k860["decision"]["current_source_owned_intertwiners_constructed"] and
          not k860["decision"]["SC_ACT_06_proved_or_refuted"],
          "K860 homogeneous intertwiner gate moved")

    k861 = data["k861"]
    check(k861["countermodel"]["ordinary_bundle_trivial"] and
          k861["countermodel"]["ordinary_rank"] == 91 and
          k861["countermodel"]["isotropy_fixed_dimension"] == 0 and
          not k861["countermodel"]["nonzero_equivariant_section_exists"] and
          not k861["decision"]["K857_abstract_frame_promoted_to_natural_owner"] and
          not k861["decision"]["SC_ACT_06_proved_or_refuted"],
          "K861 equivariant triviality countermodel moved")

    k862 = data["k862"]
    check(k862["naturality_certificate"]["row_count"] == 11 and
          k862["naturality_certificate"]["all_rows_conjunctive"] and
          not k862["naturality_certificate"]["rank_lower_bound_allowed_as_exact_dimension"] and
          not k862["naturality_certificate"]["arbitrary_global_frame_allowed_as_owner"] and
          not k862["compiled_result"]["current_flat_exact_admitted"] and
          not k862["decision"]["current_flat_packet_repaired"] and
          not k862["decision"]["SC_ACT_06_proved_or_refuted"],
          "K862 naturality repair disposition moved")

    k693 = data["k693"]
    k693_t = k693["graph_equivalence_theorem"]
    k693_n = k693["native_interface_status"]
    check(k693_t["closed_graph_weight_required"] and
          k693_t["bounded_everywhere_a_inverse_required"] and
          not k693_t["upper_bound_alone_sufficient_for_closedness"] and
          not k693_t["form_identity_with_native_remainder_automatic"] and
          not k693_n["actual_native_closed_column_proved"] and
          not k693_n["native_complete_floor_emitted"],
          "K693 graph-equivalent column compiler or native ceiling moved")

    k694 = data["k694"]
    k694_t = k694["monotone_gram_theorem"]
    k694_n = k694["native_interface_status"]
    check(k694_t["bounded_component_transforms_required"] and
          k694_t["one_dense_core_required"] and
          not k694_t["finite_prefix_without_complete_tail_sufficient"] and
          not k694_t["order_on_nondense_test_space_sufficient"] and
          not k694_n["actual_native_complete_tail_proved"] and
          not k694_n["native_complete_floor_emitted"],
          "K694 monotone Gram compiler or native ceiling moved")

    k695 = data["k695"]
    k695_f = k695["friedrichs_authentication_theorem"]
    k695_t = k695["defect_cofinal_theorem"]
    k695_n = k695["native_interface_status"]
    check(k695_f["ordinary_triple_reference_self_adjoint_required"] and
          not k695_f["ordinary_triple_validity_alone_sufficient"] and
          not k695_f["core_or_sampled_boundary_vanishing_sufficient"] and
          not k695_t["finite_block_without_tail_sufficient"] and
          not k695_t["separate_block_lowers_without_cross_control_sufficient"] and
          not k695_n["actual_native_complete_trace_coercivity_proved"] and
          not k695_n["native_complete_floor_emitted"],
          "K695 Friedrichs-defect cofinal compiler or native ceiling moved")

    k687 = data["k687"]
    k687_t = k687["countable_column_theorem"]
    k687_n = k687["native_interface_status"]
    check(k687_t["density_hypothesis"] == "D_col is dense in H" and
          not k687_t["finite_prefix_proves_complete_domain"] and
          not k687_t["individual_component_density_proves_common_domain_density"] and
          not k687_n["actual_native_column_closed"] and
          not k687_n["native_complete_floor_emitted"],
          "K687 countable-column compiler or native ceiling moved")

    k688 = data["k688"]
    k688_t = k688["partial_gram_theorem"]
    k688_n = k688["native_interface_status"]
    check(k688_t["identity"] == "||B x||^2=sum_j||B_j x||^2=sup_N <x,G_N x>" and
          not k688_t["finite_partial_gram_without_tail_sufficient"] and
          not k688_t["diagonal_matrix_elements_on_sampled_vectors_sufficient"] and
          not k688_n["actual_native_partial_gram_order_proved"] and
          not k688_n["native_complete_floor_emitted"],
          "K688 partial-Gram compiler or native ceiling moved")

    k689 = data["k689"]
    k689_t = k689["gamma_resolvent_theorem"]
    k689_n = k689["native_interface_status"]
    check(k689_t["same_reference_required"] and
          k689_t["complete_boundary_space_required"] and
          not k689_t["finite_sector_gap_sufficient"] and
          not k689_t["endpoint_membership_without_quantitative_gap_sufficient"] and
          not k689_n["actual_native_target_gamma_norm_proved"] and
          not k689_n["native_complete_floor_emitted"],
          "K689 gamma-anchor compiler or native ceiling moved")

    k684 = data["k684"]
    k684_t = k684["closed_column_theorem"]
    k684_b = k684["bounded_realization"]
    k684_n = k684["native_interface_status"]
    check(k684_t["column_hypothesis"] == "C is densely defined and closed on the complete carrier" and
          not k684_t["finite_or_formal_component_list_sufficient"] and
          not k684_t["unclosed_column_sufficient"] and
          not k684_b["factorization_without_bounded_column_sufficient"] and
          not k684_n["actual_native_complete_column_serialized"] and
          not k684_n["native_complete_floor_emitted"],
          "K684 closed-column compiler or native ceiling moved")

    k685 = data["k685"]
    k685_t = k685["component_square_theorem"]
    k685_n = k685["native_interface_status"]
    check(k685_t["one_over_one_hundred_admission"] == "sum_(j<=N)b_j^2+v_N<=1/100" and
          not k685_t["finite_prefix_without_tail_sufficient"] and
          not k685_t["same_codomain_sum_without_cross_Gram_control_sufficient"] and
          not k685_t["scalar_coefficient_bounds_without_operator_norms_sufficient"] and
          not k685_n["actual_native_complement_below_one_over_one_hundred"] and
          not k685_n["native_complete_floor_emitted"],
          "K685 component-square compiler or native ceiling moved")

    k686 = data["k686"]
    k686_t = k686["gamma_field_identity"]
    k686_n = k686["native_interface_status"]
    check(k686_t["complete_boundary_space_required"] and
          k686_t["connected_reference_resolvent_interval_required"] and
          k686_t["same_boundary_coordinate_required"] and
          not k686_t["finite_sector_gamma_bounds_sufficient"] and
          not k686_n["actual_native_complete_gamma_norms_proved"] and
          not k686_n["native_complete_floor_emitted"],
          "K686 gamma-field variation compiler or native ceiling moved")

    k681 = data["k681"]
    k681_t = k681["monotone_form_theorem"]
    k681_r = k681["reduction_and_bound_inheritance"]
    k681_n = k681["native_interface_status"]
    check(k681_t["limit_density_required"] and
          not k681_t["finite_prefix_sufficient"] and
          not k681_t["pointwise_nonmonotone_family_sufficient"] and
          not k681_t["native_identification_follows_from_abstract_convergence"] and
          not k681_r["stagewise_bath_labels_without_form_reduction_sufficient"] and
          not k681_n["actual_native_r_free_identified"] and
          not k681_n["native_complete_floor_emitted"],
          "K681 monotone remainder-form compiler or native ceiling moved")

    k682 = data["k682"]
    k682_t = k682["boundedness_theorem"]
    k682_r = k682["projection_reduction_theorem"]
    k682_n = k682["native_interface_status"]
    check(k682_t["complete_domain_required"] and
          not k682_t["factorization_alone_sufficient"] and
          not k682_t["finite_seed_rows_sufficient"] and
          not k682_t["sampled_bath_rows_sufficient"] and
          not k682_r["K643_monomial_preservation_substitutable"] and
          not k682_r["reduction_of_h_without_reduction_of_a_sufficient"] and
          not k682_n["actual_native_R_bounded"] and
          not k682_n["native_complete_floor_emitted"],
          "K682 graph-relative bounded reduction compiler or native ceiling moved")

    k683 = data["k683"]
    k683_t = k683["level_transfer_theorem"]
    k683_m = k683["monotone_shortcut"]
    k683_n = k683["native_interface_status"]
    check(k683_t["same_boundary_coordinate_required"] and
          k683_t["same_target_extension_W_required"] and
          k683_t["complete_boundary_coverage_required"] and
          not k683_t["pointwise_or_finite_block_variation_sufficient"] and
          not k683_t["raw_floor_transport_across_nonunitary_coordinate_change_allowed"] and
          not k683_m["reference_interval_and_sign_may_be_inferred"] and
          not k683_n["actual_native_target_denominator_nonnegative"] and
          not k683_n["native_complete_floor_emitted"],
          "K683 Weyl target-level robustness or native ceiling moved")

    k673 = data["k673"]
    k673_t = k673["coverage_theorem"]
    k673_c = k673["hidden_complement_countermodel"]
    k673_n = k673["native_interface_status"]
    check(k673_t["K609_complete_in_truncation_order"] and
          k673_t["K609_complete_on_named_seed_lines"] and
          k673_t["named_seed_lines"] == ["q00", "q10", "q01"] and
          k673_t["seed_lines_pairwise_orthogonal_by_charge"] and
          not k673_t["K609_complete_domain_operator_norm_proved"] and
          not k673_t["seed_line_bounds_determine_hidden_complement"] and
          not k673_t["seed_line_bounds_alone_identify_K669_map"] and
          not k673_t["native_complete_extension_denied"],
          "K673 carrier-coverage theorem moved")
    check(k673_c["all_seed_line_values_unchanged_for_every_M_nonnegative"] and
          k673_c["displayed_hidden_M"] == "1" and
          k673_c["displayed_complete_norm_square"] == "1" and
          k673_c["displayed_A_upper_at_most"] == "0" and
          k673_c["proves_seed_data_insufficient_not_native_A_nonpositive"] and
          not k673_n["actual_seed_compression_identity_proved"] and
          not k673_n["actual_complete_extension_identified"] and
          not k673_n["actual_complete_A_lower_identified"] and
          not k673_n["native_complete_floor_emitted"],
          "K673 controls or native-interface ceiling moved")

    k674 = data["k674"]
    k674_t = k674["compressed_bridge_theorem"]
    k674_x = k674["exact_native_target"]
    k674_c = k674["exact_controls"]
    k674_n = k674["native_interface_status"]
    check(not k674_t["range_orthogonality_required"] and
          k674_t["complete_A_lower"] == "A>=1-lambda-tau2" and
          k674_t["K672_cross_input"] == "kappa^2<=lambda*tau2" and
          k674_t["strict_two_thirds_test"] == "lambda+tau2<1/3" and
          not k674_t["finite_or_sampled_complement_sufficient"] and
          not k674_t["uncontrolled_complement_allowed"],
          "K674 compressed bridge theorem moved")
    check(k674_x["K609_lambda_strictly_below_one_third"] and
          k674_x["simple_sufficient_tau2_target"] == "1/100" and
          k674_x["simple_target_strictly_inside_budget"] and
          k674_x["simple_target_A_strictly_above_two_thirds"] and
          k674_x["target_is_conditional_not_native"] and
          k674_c["lambda_plus_tau2"] == "65/196" and
          k674_c["complete_A"] == "131/196" and
          k674_c["endpoint_strict_target_rejected"] and
          not k674_n["actual_seed_compression_identity_proved"] and
          not k674_n["actual_complete_complement_tau2_identified"] and
          not k674_n["actual_complete_A_lower_identified"] and
          not k674_n["native_complete_floor_emitted"],
          "K674 controls or native-interface ceiling moved")

    k671 = data["k671"]
    k671_t = k671["compensated_margin_theorem"]
    k671_c = k671["exact_controls"]
    k671_n = k671["native_interface_status"]
    check(k671_t["contraction_can_change_while_A_fixed"] and
          k671_t["same_contraction_can_coexist_with_distinct_A"] and
          not k671_t["auxiliary_contraction_alone_identifies_A"] and
          not k671_t["smaller_auxiliary_contraction_implies_A_above_two_thirds"] and
          k671_t["K659_semiboundedness_retained"] and
          not k671_t["fixed_native_A_denied"] and
          k671_t["complete_common_domain_required"],
          "K671 auxiliary-chart A custody moved")
    check(k671_c["fixed_A"] == "3/4" and
          k671_c["all_compensated_rows_preserve_fixed_A"] and
          k671_c["same_chart_ratio"] == "1/16" and
          k671_c["same_chart_rows_have_distinct_A"] and
          not k671_n["actual_compensating_regular_form_lower_identified"] and
          not k671_n["actual_invariant_total_A_lower_identified"] and
          not k671_n["native_complete_floor_emitted"],
          "K671 controls or native-interface ceiling moved")

    k672 = data["k672"]
    k672_t = k672["direct_A_theorem"]
    k672_c = k672["exact_controls"]
    k672_n = k672["native_interface_status"]
    check(k672_t["comparison_matrix"] == "[[a_N,-kappa],[-kappa,a_tail]]" and
          "(a_N-2/3)(a_tail-2/3)>kappa^2" in k672_t["two_thirds_test"] and
          not k672_t["finite_prefix_only_sufficient"] and
          not k672_t["sampled_complement_sufficient"] and
          not k672_t["uncontrolled_cross_allowed"] and
          not k672_t["auxiliary_chart_contraction_substitutable_for_total_form_bound"] and
          k672_t["complete_common_domain_required"],
          "K672 direct-A theorem moved")
    check(k672_c["passing_control"]["shifted_determinant"] == "1/48" and
          k672_c["passing_shifted_det_over_trace"] == "1/20" and
          k672_c["passing_complete_A_strict_lower"] == "43/60" and
          k672_c["endpoint_control"]["shifted_determinant"] == "0" and
          k672_c["endpoint_exact_complete_A"] == "2/3" and
          not k672_n["actual_complete_A_lower_identified"] and
          not k672_n["native_complete_floor_emitted"],
          "K672 controls or native-interface ceiling moved")

    k669 = data["k669"]
    k669_t = k669["factorization_bridge_theorem"]
    k669_b = k669["exact_bounds"]
    k669_n = k669["native_interface_status"]
    check(k669_t["required_native_identity"].endswith("complete common domain") and
          "unitarily" in k669_t["required_map_identification"] and
          k669_t["K609_strict_consequence"] == "lambda_K609<1/3 implies A>2/3" and
          not k669_t["finite_or_sampled_identification_sufficient"] and
          not k669_t["equal_numerical_norm_without_map_identity_sufficient"] and
          not k669_t["uncontrolled_complement_allowed"],
          "K669 leakage-to-remainder bridge moved")
    check(k669_b["conservative_rational_A_lower"] == "2/3" and
          k669_b["conditional_A_strictly_above_two_thirds"] and
          not k669_n["actual_native_factorization_identified"] and
          not k669_n["actual_native_map_intertwiner_identified"] and
          not k669_n["actual_complete_A_lower_identified"] and
          not k669_n["native_complete_floor_emitted"],
          "K669 bounds or native-interface ceiling moved")

    k670 = data["k670"]
    k670_t = k670["asymmetric_target_theorem"]
    k670_c = k670["exact_controls"]
    k670_n = k670["native_interface_status"]
    check(k670_t["positivity_threshold_at_A_two_thirds"] == "B=1/171" and
          k670_t["selected_rational_B_target"] == "1/170" and
          k670_t["determinant_slack_against_trace_upper"] == "1/43605" and
          k670_t["strict_complete_floor"] == "lambda_->2/58653" and
          k670_t["same_domain_required"] and
          k670_t["both_total_parity_tails_required"] and
          not k670_t["finite_prefix_only_sufficient"] and
          not k670_t["uncontrolled_complement_allowed"],
          "K670 asymmetric margin theorem moved")
    check(k670_c["determinant_slack"] == "1/43605" and
          k670_c["trace_corner"] == "343/510" and
          k670_c["det_over_trace_floor"] == "2/58653" and
          not k670_n["actual_K669_native_factorization_identified"] and
          not k670_n["actual_complete_A_lower_identified"] and
          not k670_n["actual_complete_B_lower_identified"] and
          not k670_n["native_complete_floor_emitted"],
          "K670 controls or native-interface ceiling moved")

    k667 = data["k667"]
    k667_t = k667["telescoping_theorem"]
    k667_b = k667["exact_bounds"]
    k667_n = k667["native_interface_status"]
    check(k667_t["strict_complete_enclosure"] == "1/257<beta^2<2/513" and
          k667_t["complete_infinite_tail_controlled"] and
          not k667_t["finite_partial_sum_promoted_to_complete_bound"] and
          k667_t["spectator_dimension_independent"],
          "K667 complete trace-square theorem moved")
    check(k667_b["lower"] == "1/257" and k667_b["upper"] == "2/513" and
          k667_b["width"] == "1/131841" and
          k667_b["new_upper_strictly_improves_old"] and
          k667_n["complete_matched_trace_beta_squared_upper_identified"] and
          not k667_n["actual_complete_A_lower_identified"] and
          not k667_n["actual_complete_B_lower_identified"] and
          not k667_n["native_complete_floor_emitted"],
          "K667 bounds or native-interface ceiling moved")

    k668 = data["k668"]
    k668_t = k668["rational_target_theorem"]
    k668_c = k668["exact_controls"]
    k668_n = k668["native_interface_status"]
    check(k668_t["K667_sufficient_strict_test"].endswith(">=2/513") and
          not k668_t["square_root_evaluation_required"] and
          k668_t["complete_A_B_same_domain_required"] and
          not k668_t["finite_prefix_only_sufficient"] and
          not k668_t["uncontrolled_complement_allowed"],
          "K668 rational target theorem moved")
    check(k668_c["positive_row"]["determinant_slack_against_upper"] == "1/131328" and
          k668_c["B_control_excess_over_threshold"] == "1/16416" and
          k668_c["threshold_row_passes_strictly_for_actual_beta"] and
          k668_c["below_threshold_row_rejected"] and
          k668_n["complete_matched_trace_beta_squared_upper_identified"] and
          not k668_n["actual_complete_A_lower_identified"] and
          not k668_n["actual_complete_B_lower_identified"] and
          not k668_n["native_complete_floor_emitted"],
          "K668 controls or native-interface ceiling moved")

    k661 = data["k661"]
    k661_i = k661["interval_control"]
    k661_c = k661["exact_controls"]
    k661_t = k661["custody_theorem"]
    k661_n = k661["native_interface_status"]
    check(k661_i["green_identity_exact_on_polynomial_controls"] and
          k661_i["dirichlet_is_friedrichs"] and
          k661_i["swapped_green_identity_valid"] and
          not k661_i["swapped_reference_is_friedrichs"] and
          k661_i["same_minimal_operator"] and
          k661_i["both_references_self_adjoint_and_semibounded"],
          "K661 interval boundary-triple control moved")
    check(k661_c["constant_is_neumann_not_dirichlet"] and
          k661_c["dirichlet_witness_is_dirichlet_not_neumann"] and
          k661_c["both_constant_families_norm_resolvent_converge"] and
          not k661_t["ordinary_boundary_triple_alone_selects_friedrichs"] and
          not k661_t["semibounded_reference_alone_selects_friedrichs"] and
          not k661_t["norm_resolvent_convergence_alone_selects_friedrichs"] and
          not k661_t["profile_universality_alone_selects_friedrichs"] and
          not k661_t["fixed_native_reference_is_not_friedrichs"] and
          not k661_n["actual_native_reference_proved_friedrichs"] and
          not k661_n["actual_native_s_identified"] and
          not k661_n["K473_released"],
          "K661 custody or native-interface ceiling moved")

    k662 = data["k662"]
    k662_t = k662["coordinate_group_theorem"]
    k662_q = k662["quantitative_transport"]
    k662_c = k662["exact_controls"]
    k662_x = k662["composition"]
    k662_n = k662["native_interface_status"]
    check(k662_t["reference_extension_unchanged"] and
          k662_t["friedrichs_status_preserved_if_previously_proved"] and
          not k662_t["friedrichs_status_created"] and
          k662_t["denominator_transform"] == "D'(z)=U^{-*}D(z)U^{-1}" and
          k662_t["complete_denominator_nonnegativity_equivalent"] and
          k662_t["strict_positivity_equivalent"] and
          k662_t["numerical_floor_invariant_for_unitary_U"] and
          not k662_t["numerical_floor_invariant_for_general_U"] and
          not k662_t["K661_symplectic_swap_covered"],
          "K662 reference-preserving coordinate theorem moved")
    check(k662_q["floor_hypothesis"] == "d>=0 and d_N>=0" and
          k662_q["if_D_ge_nonnegative_d_then"] == "D'>=d/||U||^2" and
          k662_q["if_error_le_eta_then"] == "||D_N'-D'||<=||U^{-1}||^2 eta" and
          k662_c["congruence_identity"] and
          k662_c["floor_bound_holds"] and
          k662_c["approximant_congruence_identity"] and
          k662_c["error_bound_holds"] and
          k662_c["approximant_floor_bound_holds"] and
          k662_c["conservative_margin_nonnegative"] and
          k662_c["original_denominator_floor"] == "1" and
          k662_c["transformed_denominator_floor"] == "3/8" and
          k662_c["operator_norm_error"] == "1/20" and
          k662_c["transformed_operator_norm_error"] == "2/25" and
          not k662_x["K139_regulator_coordinates_already_authenticated_in_group"] and
          not k662_n["actual_native_coordinate_group_law_proved"] and
          not k662_n["actual_native_s_identified"] and
          not k662_n["K473_released"],
          "K662 quantitative or native-interface ceiling moved")

    k657 = data["k657"]
    k657_t = k657["ordinary_boundary_triple_theorem"]
    k657_g = k657["fail_closed_admission"]
    k657_n = k657["native_interface_status"]
    check(k657_t["equivalence"] == "A_W>=lambda iff D_W(lambda)>=0" and
          "Theorem A.7(i)" in k657_t["theorem_basis"] and
          "A-lambda I" in k657_t["scalar_shift"] and
          "Friedrichs extension" in k657_t["reference_premise"] and
          "M(lambda) is bounded" in k657_t["boundary_space_premise"] and
          not k657_t["common_free_form_domain_required"] and
          not k657_t["finite_impurity_denominator_sufficient"] and
          not k657_t["native_sign_convention_may_be_inferred"],
          "K657 boundary/Weyl floor theorem moved")
    check(k657_g["missing_any_field_rejects"] and
          k657_g["pointwise_sector_samples_reject"] and
          k657_g["finite_impurity_only_reject"] and
          not k657_g["synthetic_controls_are_native_evidence"] and
          not k657_n["actual_native_denominator_nonnegative"] and
          not k657_n["actual_native_base_floor_r0_identified"] and
          not k657_n["actual_native_target_b_identified"] and
          not k657_n["K473_released"],
          "K657 native interface ceiling moved")

    k658 = data["k658"]
    k658_t = k658["cofinal_margin_theorem"]
    k658_c = k658["exact_controls"]
    k658_n = k658["native_interface_status"]
    check(k658_t["order_consequence"] == "D(-s)>=(d_N-eta_N)I" and
          k658_t["same_s_required"] and
          k658_t["same_extension_coordinate_required"] and
          k658_t["self_adjointness_required"] and
          k658_t["complete_boundary_coverage_required"] and
          not k658_t["finite_impurity_only_sufficient"] and
          not k658_t["sectorwise_pointwise_convergence_sufficient"] and
          not k658_t["uncontrolled_complement_sufficient"],
          "K658 cofinal denominator-margin theorem moved")
    check(k658_c["zero_transferred_margin_accepts"] and
          k658_c["negative_transferred_margin_rejects"] and
          k658_c["incomplete_coverage_rejects_despite_large_margin"] and
          not k658_n["actual_native_s_identified"] and
          not k658_n["actual_native_d_n_identified"] and
          not k658_n["actual_native_eta_n_identified"] and
          not k658_n["actual_complete_boundary_coverage_proved"] and
          not k658_n["actual_native_base_floor_r0_identified"] and
          not k658_n["K473_released"],
          "K658 native interface ceiling moved")

    k647 = data["k647"]
    k647_t = k647["intertwiner_theorem"]
    k647_n = k647["native_interface_status"]
    check(k647_t["recursive_domain"] == "D_K139=S Dom(H0)" and
          k647_t["recursive_domain_invariance"] == "J D_K139=D_K139" and
          k647_t["physical_gram_covariance"] == "JM=MJ for M=S*S" and
          "single common free-form domain" in k647_t["same_form_identity"],
          "K647 native common-domain intertwiner moved")
    check(k647_n["actual_K139_recursive_domain_J_invariant"] and
          k647_n["actual_K139_K168_same_form_identity_J_invariant"] and
          k647_n["actual_physical_gram_J_invariant"] and
          not k647_n["actual_parity_block_floors_identified"] and
          not k647_n["native_global_m_identified"] and
          not k647_n["K473_released"],
          "K647 native interface ceiling moved")

    k648 = data["k648"]
    k648_c = k648["total_parity_carriers"]
    k648_q = k648["quantitative_certificate_schema"]
    k648_n = k648["native_interface_status"]
    check("C^6_+ tensor H_n^(U,+)" in k648_c["total_plus"] and
          "C^6_- tensor H_n^(U,+)" in k648_c["total_minus"] and
          not k648_c["three_scalar_channel_reduction"],
          "K648 total-parity product carriers moved")
    check("six operator blocks" in k648_q["per_total_parity_blocks"] and
          "1<=i<j<=6" in k648_q["required_coupling_rows"] and
          "i=1,...,6" in k648_q["required_diagonal_rows"] and
          len(k648_q["uniform_tail_rows"]) == 2 and
          not k648_q["finite_prefix_is_tail"],
          "K648 quantitative certificate schema moved")
    check(k648_n["actual_K139_K168_common_domain_identity_proved"] and
          k648_n["actual_total_parity_compression_forms_serialized"] and
          k648_n["actual_channel_spectator_quadrants_serialized"] and
          not k648_n["actual_parity_block_floors_identified"] and
          not k648_n["actual_uniform_parity_tails_identified"] and
          not k648_n["native_global_m_identified"] and
          not k648_n["K473_released"],
          "K648 native interface ceiling moved")

    k645 = data["k645"]
    k645_r = k645["complete_family_replay"]
    k645_t = k645["finite_order_theorem"]
    k645_l = k645["limit_interface"]
    k645_n = k645["native_interface_status"]
    check(k645_r["terms"] == 2958 and
          k645_r["two_element_orbits"] == 1479 and
          k645_r["fixed_terms"] == 0 and
          k645_r["output_wedge_phase_counts"] == {"-1": 516, "1": 2442} and
          k645_r["swap_is_involutive"] and
          k645_r["all_partners_present"] and
          k645_r["CAR_coefficients_transform_by_output_wedge_phase"] and
          k645_r["naive_sign_preservation_is_false"],
          "K645 exact family covariance moved")
    check("every finite N" in k645_t["operator_identity"] and
          "commutes with total bath number" in k645_t["bath_number_compatibility"],
          "K645 finite-order or sector theorem moved")
    check(not k645_l["physical_flavor_symmetry_claimed"] and
          not k645_l["source_selected_family_interpretation_claimed"] and
          k645_n["equal_coupling_coefficient_covariance_proved"] and
          not k645_n["full_native_K139_K168_to_K642_form_identity_proved"] and
          not k645_n["native_global_m_identified"] and
          not k645_n["K473_released"],
          "K645 native interface ceiling moved")

    k646 = data["k646"]
    k646_t = k646["parity_reduction_theorem"]
    k646_c = k646["K644_composition"]
    k646_n = k646["native_interface_status"]
    check(k646_t["sector_floor"] == "m_n=min(m_n^+,m_n^-)" and
          k646_t["global_floor"] == "m=min(inf_n m_n^+,inf_n m_n^-)" and
          k646_t["cross_parity_identity"] == "b_n[P_n^+x,P_n^-y]=0" and
          "does not identify" in k646_t["no_scalar_matrix_reduction"],
          "K646 parity reduction theorem moved")
    check("independent uniform parity tails" in k646_c["global_output"] and
          k646_c["K642_base_floor"] == "min(1/2,m-1/128)" and
          k646_c["K642_controlled_floor"] == "min(1/2-alpha,m-delta-1/128)",
          "K646 K644/K642 composition moved")
    check(k646_n["cross_parity_blocks_eliminated_under_invariant_domain_hypothesis"] and
          not k646_n["actual_K139_K168_common_domain_identity_proved"] and
          not k646_n["actual_parity_compression_forms_identified"] and
          not k646_n["actual_parity_floors_identified"] and
          not k646_n["actual_uniform_parity_tails_identified"] and
          not k646_n["native_global_m_identified"] and
          not k646_n["K473_released"],
          "K646 native interface ceiling moved")

    k643 = data["k643"]
    k643_r = k643["native_replay"]
    k643_t = k643["sector_reduction_theorem"]
    k643_n = k643["native_interface_status"]
    check(k643_r["term_count"] == 2958 and
          k643_r["matched_polarity_for_every_term"] and
          k643_r["one_bath_creation_and_one_bath_annihilation_per_exchange_monomial"] and
          k643_r["total_bath_number_preserved_by_every_exchange_monomial"] and
          k643_r["K603_all_action_terms_retained"],
          "K643 native number-preservation replay moved")
    check(k643_t["global_lower_constant"] == "m=inf_(n>=0)m_n" and
          "same m" in k643_t["uniform_equivalence"] and
          "tail" in k643_t["finite_prefix_consequence"] and
          "min(m_prefix,m_tail)" in k643_t["tail_composition"],
          "K643 sector lower theorem moved")
    check(k643_n["sector_localization_of_future_B_proved"] and
          not k643_n["actual_K139_K168_intertwiner_identified"] and
          not k643_n["uniform_tail_lower_identified"] and
          not k643_n["native_global_m_identified"] and
          not k643_n["K473_released"],
          "K643 native interface ceiling moved")

    k644 = data["k644"]
    k644_t = k644["operator_block_theorem"]
    k644_c = k644["sector_to_global_composition"]
    k644_n = k644["native_interface_status"]
    check(k644_t["sharp_comparison_floor"] == "m_n>=lambda_min(C_n)" and
          "g_n=min_i" in k644_t["row_sum_floor"] and
          k644_t["no_bounded_diagonal_operator_requirement"] and
          k644_t["failed_row_sum_is_not_a_negative_spectrum_proof"],
          "K644 operator-block theorem moved")
    check(k644_c["global_output"] == "m=inf_n m_n, with a separately proved uniform tail beyond any finite prefix" and
          k644_c["K642_base_floor"] == "min(1/2,m-1/128)" and
          k644_c["K642_controlled_floor"] == "min(1/2-alpha,m-delta-1/128)",
          "K644 K642 composition moved")
    check(k644_n["six_channel_operator_certificate_constructed"] and
          not k644_n["actual_K139_K168_common_domain_identity_proved"] and
          not k644_n["actual_diagonal_sector_floors_identified"] and
          not k644_n["actual_off_diagonal_sector_bounds_identified"] and
          not k644_n["native_global_m_identified"] and
          not k644_n["native_complete_sector_floor_emitted"],
          "K644 native interface ceiling moved")

    b5 = next(
        item for item in data["agenda"]["work_items"]
        if item["id"] == registry["b5_agenda_currency"]["work_item"]
    )
    b5_contract = registry["b5_agenda_currency"]
    check(b5["state"] == b5_contract["state"], "B5 agenda state is stale")
    check("RB6 recertification and the full-20 Gram-adjoint wave completed" in b5["latest_result"],
          "B5 latest result does not retire RB6/Wave One")
    check("EXTERNAL-VIA-GRAM" in b5["latest_result"],
          "B5 graph-mixing branch ceiling lost")
    check(b5_contract["live_reopener"] in b5["next_swing"],
          "B5 live reopener missing")
    check("Do not repeat RB6 recertification" in b5["next_swing"],
          "B5 completed work is not forbidden as a repeat")
    check("odd rank-128 spinor" in b5["current_authority"],
          "B5 boundary multiplier typing lost")
    check("source-native `B5-MIDDLE-DIFFERENTIAL` row remains" in data["b5_artifact"],
          "B5 source-native/independent boundary lost")
    check("## Hostile review and ceiling" in data["b5_artifact"],
          "B5 currency hostile review missing")

    check(data["b2"]["basis"]["terminal_rows"] == 91, "B2 basis terminal count moved")
    check(data["b2"]["basis"]["b2_selectable"] is True, "B2 selectability history moved")
    check(all(value is False for value in registry["protected_effects"].values()),
          "protected movement field changed")

    k641 = data["k641"]
    k641_f = k641["complete_family_replay"]
    k641_t = k641["native_type_theorem"]
    k641_r = k641["K640_reconciliation"]
    check(k641_f["term_count"] == 2958 and
          k641_f["surviving_monomial_count"] == 6 and
          k641_f["every_surviving_monomial_occurs_at_every_order"] and
          k641_f["remaining_variable_arity_by_order"] == {str(order): order for order in range(2, 13)},
          "K641 complete family type census moved")
    check(k641_t["K639_algebraic_rank_six_preserved"] and
          k641_t["K179_output_kernels_retain_spectator_variables"] and
          k641_t["K148_native_self_energy_acts_on_full_bath_Fock_space"] and
          k641_t["K159_operator_valued_spectator_denominator_required"] and
          k641_t["constant_6x6_native_identification_rejected_by_current_typing"] and
          k641_t["minimal_corrected_coefficient_space"] == "C^6 tensor H_spec" and
          not k641_t["native_complete_boundary_operator_identified_with_constant_6x6_matrix"],
          "K641 native type theorem moved")
    check(k641_r["spectator_amplification_required"] and
          k641_r["operator_valued_lower_bound_required"] and
          not k641_r["parameterized_scalar_matrix_theorem_retracted"] and
          not k641_r["reference_control_is_native_floor"],
          "K641 K640 reconciliation moved")

    k642 = data["k642"]
    k642_a = k642["spectator_amplification_theorem"]
    k642_o = k642["operator_lower_theorem"]
    k642_e = k642["controlled_extension_theorem"]
    k642_n = k642["native_interface_status"]
    check(not k642_a["spectator_dimension_restricted"] and
          k642_a["matched_Bochner_trace_continuous"] and
          k642_a["beta_squared_strictly_below_one_over_256"] and
          k642_a["proof_constant_independent_of_H_spec"],
          "K642 spectator amplification moved")
    check(k642_o["floor_function"] == "min(1/2,m-1/128)" and
          k642_o["dimension_free"] and
          not k642_o["finite_boundary_matrix_required"] and
          not k642_o["reference_control_is_actual_K139_K168_floor"],
          "K642 operator lower theorem moved")
    check(k642_e["floor_function"] == "min(1/2-alpha,m-delta-1/128)" and
          k642_e["same_cancellation_domain_required"] and
          not k642_e["mixed_incompatible_graphs_used"] and
          all(row["passes"] for row in k642_e["finite_controls"]),
          "K642 controlled extension theorem moved")
    check(not k642_n["actual_K139_K168_to_D_op_intertwiner_identified"] and
          not k642_n["actual_complete_boundary_form_B_identified"] and
          not k642_n["actual_operator_lower_m_identified"] and
          not k642_n["actual_remainder_alpha_delta_identified"] and
          not k642_n["named_complete_sector_floor_emitted"] and
          not k642_n["K473_released"],
          "K642 native interface ceiling moved")

    k639 = data["k639"]
    k639_f = k639["complete_family_replay"]
    k639_q = k639["quotient_theorem"]
    k639_r = k639["dependency_reconciliation"]
    check(k639_f["term_count"] == 2958 and
          k639_f["all_terms_map_to_declared_K638_labels"] and
          len(k639_f["surviving_label_counts"]) == 6,
          "K639 complete family replay moved")
    check(k639_q["declared_dimension"] == 16 and
          k639_q["surviving_dimension"] == 6 and
          k639_q["kernel_dimension"] == 10 and
          k639_q["quotient_matrix_rank"] == 6 and
          k639_q["separating_functional_rank"] == 6 and
          k639_q["surviving_operator_monomials_linearly_independent_on_finite_particle_core"] and
          not k639_q["independent_physical_channel_ranges_proved"],
          "K639 quotient theorem moved")
    check(not k639_r["complete_K139_K168_core_controlled"] and
          not k639_r["named_complete_sector_floor_emitted"] and
          not k639_r["K473_released"],
          "K639 dependency ceiling moved")

    k640 = data["k640"]
    k640_t = k640["trace_and_domain_theorem"]
    k640_l = k640["parameterized_lower_theorem"]
    k640_n = k640["native_interface_status"]
    check(k640_t["channel_dimension"] == 6 and
          k640_t["cancellation_domain_strictly_larger"] and
          k640_t["matched_trace_continuous"] and
          k640_t["beta_squared_strictly_below_one_over_256"],
          "K640 trace/domain theorem moved")
    check(k640_l["floor_function"] == "min(1/2,m-1/128)" and
          k640_l["all_finite_Hermitian_boundary_matrices_semibounded_on_same_graph"] and
          not k640_l["reference_control_is_actual_K139_K168_floor"] and
          not k640_l["diagonal_weight_graph_splice_used"] and
          not k640_l["separate_singular_factor_estimates_used"],
          "K640 parameterized lower theorem moved")
    check(k640_n["K639_actual_six_channel_coordinate_consumed"] and
          k640_n["same_domain_lower_method_constructed"] and
          not k640_n["actual_K139_K168_form_equal_to_parameterized_q_B_proved"] and
          not k640_n["actual_complete_regular_core_lower_m_identified"] and
          not k640_n["named_complete_sector_floor_emitted"] and
          not k640_n["K473_released"],
          "K640 native interface ceiling moved")

    k637 = data["k637"]
    k637_t = k637["naturality_theorem"]
    k637_o = k637["ownership_reconciliation"]
    k637_d = k637["decision"]
    check(len(k637["cross_characteristic_packets"]) == 2 and
          all(packet["single_block_fixed_dimension"] == 1 and
              packet["independent_two_block_fixed_dimension"] == 2 and
              packet["block_exchange_fixed_dimension"] == 1
              for packet in k637["cross_characteristic_packets"]),
          "K637 cross-characteristic naturality fingerprint moved")
    check(k637_t["internal_basis_gauge_fixed_dimension"] == 2 and
          k637_t["unlabeled_exchange_fixed_dimension"] == 1 and
          k637_t["labeled_grading_is_basis_natural"] and
          not k637_t["action_only_selected_nonscalar_operator"],
          "K637 naturality theorem moved")
    check(not k637_o["independently_action_owned_source_endomorphism_found"] and
          not k637_o["K596_K598_released"] and
          not k637_d["existing_data_selects_a_unique_nonscalar_operator"],
          "K637 ownership ceiling moved")

    k638 = data["k638"]
    k638_c = k638["native_coordinate_census"]
    k638_t = k638["vector_graph_theorem"]
    k638_m = k638["matrix_matching_uniqueness"]
    k638_r = k638["dependency_reconciliation"]
    check(k638_c["declared_label_count"] == 16 and
          k638_c["all_sixteen_monomials_included"] and
          not k638_c["bookkeeping_dimension_proved_minimal"],
          "K638 native coordinate census moved")
    check(k638_t["vector_cancellation_domain_strictly_larger"] and
          k638_t["matched_vector_trace_continuous"] and
          k638_t["K636_scalar_graph_is_one_coordinate_restriction"],
          "K638 vector graph theorem moved")
    check(k638_m["componentwise_matching_is_unique_on_declared_coordinate"] and
          k638_m["every_nonidentity_subtraction_matrix_has_a_divergent_direction"] and
          not k638_m["complete_matched_combination_lower_bounded"],
          "K638 matrix matching boundary moved")
    check(k638_r["actual_K176_label_census_bound_to_graph"] and
          not k638_r["named_complete_sector_floor_emitted"],
          "K638 dependency ceiling moved")

    k635 = data["k635"]
    k635_t = k635["stabilizer_theorem"]
    k635_o = k635["ownership_reconciliation"]
    k635_d = k635["decision"]
    check(len(k635["cross_characteristic_packets"]) == 2 and
          all(packet["slow_kernel_join_rank"] == 128 and
              packet["slow_kernel_intersection_rank"] == 0 and
              packet["induced_algebra_dimension"] == 8192 and
              packet["full_stabilizer_dimension"] == 32768
              for packet in k635["cross_characteristic_packets"]),
          "K635 cross-characteristic stabilizer fingerprint moved")
    check(k635_t["induced_source_algebra_dimension"] == 8192 and
          k635_t["full_commutant_seed_stabilizer_dimension"] == 32768 and
          k635_t["explicit_nonscalar_involution_exists"],
          "K635 stabilizer theorem moved")
    check(not k635_t["every_induced_operator_is_selected_by_the_action"] and
          k635_o["full_commutant_contains_nonscalar_seed_stabilizers"] and
          not k635_o["independently_action_owned_source_endomorphism_found"],
          "K635 ownership ceiling moved")
    check(k635_d["full_frozen_commutant_stabilizer_classified"] and
          not k635_d["algebraic_existence_releases_K596_K598"],
          "K635 decision boundary moved")

    k636 = data["k636"]
    k636_t = k636["cancellation_graph_theorem"]
    k636_m = k636["matching_uniqueness"]
    k636_r = k636["dependency_reconciliation"]
    k636_d = k636["decision"]
    check(k636["partial_trace_witness"]["diverges"] and
          k636_t["cancellation_domain_strictly_contains_trace_domain"] and
          k636_t["renormalized_trace_continuous"] and
          not k636_t["equivalent_norm_repair"],
          "K636 non-equivalent graph theorem moved")
    check(k636_m["matched_coefficient"] == "alpha=1" and
          k636_m["every_mismatched_coefficient_diverges_for_c_nonzero"] and
          k636_m["cancelled_combination_bounded"],
          "K636 matching uniqueness moved")
    check(k636_r["genuinely_non_equivalent_domain_constructed"] and
          not k636_r["complete_K139_K168_core_controlled"] and
          not k636_r["named_complete_sector_floor_emitted"],
          "K636 dependency boundary moved")
    check(k636_d["topological_part_of_K634_reopener_released"] and
          not k636_d["quantitative_complete_form_part_released"],
          "K636 decision boundary moved")

    k633 = data["k633"]
    k633_t = k633["stabilizer_theorem"]
    k633_o = k633["ownership_reconciliation"]
    k633_d = k633["decision"]
    check(len(k633["cross_characteristic_packets"]) == 2,
          "K633 characteristic packet count moved")
    check(all(packet["seed_action_seed_join_rank"] == 256 and
              packet["nonconstant_quotient_coefficient_rank"] == 3 and
              packet["nonconstant_stabilizer_nullity"] == 0
              for packet in k633["cross_characteristic_packets"]),
          "K633 quotient fingerprint moved")
    check(k633_t["polynomial_stabilizer_dimension"] == 1 and
          k633_t["polynomial_stabilizer_basis"] == ["identity"] and
          k633_t["every_induced_source_endomorphism_is_scalar"],
          "K633 stabilizer theorem moved")
    check(not k633_t["nontrivial_owned_source_endomorphism_obtained"] and
          not k633_o["arbitrary_commutant_or_mixed_hessian_excluded"],
          "K633 ownership or scope ceiling moved")
    check(k633_d["frozen_action_polynomial_route_to_new_V128_endomorphism_closed"] and
          not any((k633_d["independently_owned_V128_endomorphism_found"],
                   k633_d["actual_K596_K598_packet_released"],
                   k633_d["selected_source_action_rejected"])),
          "K633 decision boundary moved")

    k634 = data["k634"]
    k634_t = k634["equivalent_norm_theorem"]
    k634_c = k634["bounded_correlation_corollary"]
    k634_s = k634["surviving_domain_class"]
    k634_d = k634["decision"]
    check(k634["reciprocity_witness"]["lower_is_unbounded"] and
          not k634["reciprocity_witness"]["positive_diagonal_domain_with_both_requirements_exists"],
          "K634 reciprocity input moved")
    check(k634_t["underlying_domain_set_is_unchanged"] and
          k634_t["membership_of_boundary_profile_is_unchanged"] and
          k634_t["continuity_of_every_linear_trace_is_invariant"] and
          k634_t["unbounded_trace_cannot_become_bounded"],
          "K634 equivalent-norm theorem moved")
    check(not any((k634_c["chart_membership_repaired"],
                   k634_c["point_trace_continuity_repaired"],
                   k634_c["same_domain_K611_product_well_typed"],
                   k634_c["bounded_correlation_is_genuinely_new_domain"])),
          "K634 bounded-correlation corollary moved")
    check(k634_s["genuinely_non_equivalent_correlated_domain_not_excluded"] and
          k634_s["complete_matched_form_estimated_before_factor_separation_not_excluded"] and
          not k634_s["named_quantitative_floor_constructed"],
          "K634 surviving domain class moved")
    check(k634_d["bounded_equivalent_domain_repair_route_closed"] and
          not any((k634_d["all_correlated_domains_ruled_out"],
                   k634_d["named_complete_sector_floor_emitted"],
                   k634_d["K473_released"],
                   k634_d["native_K152_interval_emitted"])),
          "K634 decision boundary moved")

    k631 = data["k631"]
    k631_t = k631["census_theorem"]
    k631_o = k631["ownership_reconciliation"]
    check(k631["candidate_count"] == 8 and len(k631["candidates"]) == 8,
          "K631 candidate census moved")
    check(k631_t["every_strong_current_candidate_typed"] and
          k631_t["current_new_owned_input_dependency_is_not_a_retrieval_gap_at_single_object_level"],
          "K631 census theorem moved")
    check(not any((k631_t["single_candidate_matching_ambient_gram"],
                   k631_t["single_candidate_matching_source_domain_endomorphism"],
                   k631_t["single_candidate_matching_stationary_odd_adapter"])),
          "K631 reopener invented")
    check(k631_t["composition_loophole_left_for_K632"] and
          not any((k631_o["H_Sigma_retracted"], k631_o["K590_factorized_completion_retracted"],
                   k631_o["K614_source_owned_injection_retracted"],
                   k631_o["K617_corrected_descent_retracted"],
                   k631_o["K629_K630_family_obstruction_retracted"],
                   k631_o["source_or_action_rejected"])),
          "K631 ownership/continuation boundary moved")

    k632 = data["k632"]
    k632_t = k632["closure_theorem"]
    k632_o = k632["ownership_reconciliation"]
    k632_d = k632["decision"]
    check(k632_t["current_serialized_operation_set_exhausted"] and
          k632_t["post_K630_dependency_requires_genuinely_new_owned_input"],
          "K632 closure theorem moved")
    check(not any((k632_t["owned_ambient_Gram_reachable"],
                   k632_t["owned_source_domain_endomorphism_reachable"],
                   k632_t["owned_stationary_odd_adapter_with_Riesz_and_domain_reachable"],
                   k632_t["universal_future_action_no_go"])),
          "K632 target or universal no-go invented")
    check(k632_t["nondegenerate_unowned_source_pullback_forms_reachable"] and
          k632_t["factorized_action_complex_reachable"],
          "K632 positive current content lost")
    check(k632_d["composition_loophole_closed_for_current_serialized_objects"] and
          not k632_d["actual_K596_K598_packet_released"],
          "K632 decision boundary moved")
    check(not any((k632_o["K590_factorized_completion_retracted"],
                   k632_o["K614_source_owned_injection_retracted"],
                   k632_o["K617_historical_descent_retracted"],
                   k632_o["K625_H_Sigma_retracted"],
                   k632_o["K629_K630_family_obstruction_retracted"],
                   k632_o["selected_source_action_rejected"],
                   k632_o["common_BV_Green_domain_constructed"])),
          "K632 ownership ceiling moved")

    k629 = data["k629"]
    k629_t = k629["determinant_line_theorem"]
    k629_o = k629["ownership_reconciliation"]
    k629_d = k629["decision"]
    check(len(k629["cross_characteristic_packets"]) == 2, "K629 characteristic packet count moved")
    check(k629_t["family_parameter_group_dimension"] == 8192, "K629 family dimension moved")
    check(k629_t["combined_slow_ratio_squares"] == [949, 1004] and k629_t["both_fast_ratio_squares"] == [1, 1], "K629 determinant-line fingerprint moved")
    check(k629_t["every_K622_family_member_tested"] and k629_t["alternative_domain_map_family_excluded_for_simultaneous_nondegenerate_block_isometry"], "K629 family theorem moved")
    check(k629_t["K622_abstract_nonisometric_orbit_exists"] and not k629_o["K622_abstract_orbit_retracted"], "K629 abstract-orbit boundary moved")
    check(not any((k629_o["family_wide_pairing_obstruction_is_action_selection"], k629_o["source_owned_domain_map_or_Gram_constructed"], k629_o["mixed_hessian_or_stationary_background_constructed"], k629_o["common_BV_Green_domain_constructed"])), "K629 ownership ceiling moved")
    check(k629_d["broader_K622_family_pairing_orbit_decided"] and not k629_d["K622_family_contains_pairing_preserving_repair"] and not any((k629_d["actual_K596_K598_packet_released"], k629_d["selected_source_action_rejected"])), "K629 decision ceiling moved")

    k630 = data["k630"]
    k630_t = k630["gauge_invariance_theorem"]
    k630_o = k630["ownership_reconciliation"]
    k630_d = k630["decision"]
    check(len(k630["cross_characteristic_packets"]) == 2, "K630 characteristic packet count moved")
    check(k630_t["invariant_slow_ratio_squares"] == [949, 1004] and k630_t["all_tested_source_and_ambient_gauges_preserve_obstruction"], "K630 gauge fingerprint moved")
    check(not k630_t["K629_family_obstruction_is_coordinate_artifact"] and not k630_t["K628_serialized_row_basis_witness_is_required_for_K629"], "K630 coordinate/pivot theorem moved")
    check(not any((k630_o["K629_family_obstruction_retracted"], k630_o["ambient_gauge_invariance_selects_a_positive_Gram"], k630_o["source_coordinate_invariance_selects_a_source_endomorphism"], k630_o["mixed_hessian_or_stationary_background_constructed"], k630_o["common_BV_Green_domain_constructed"])), "K630 ownership ceiling moved")
    check(k630_d["K629_obstruction_survives_allowed_coordinate_changes"] and not k630_d["admissible_common_basis_or_pivot_change_reopens_K622_pairing_family"] and not any((k630_d["actual_K596_K598_packet_released"], k630_d["selected_source_action_rejected"])), "K630 decision ceiling moved")

    k627 = data["k627"]
    k627_t = k627["pairing_nonselection_theorem"]
    k627_o = k627["ownership_reconciliation"]
    k627_d = k627["decision"]
    check(k627_t["block_ranks"] == [192, 192, 64, 64], "K627 block ranks moved")
    check(k627_t["block_positive_pairing_dimensions"] == [18528, 18528, 2080, 2080] and k627_t["total_positive_pairing_family_dimension"] == 41216, "K627 pairing dimensions moved")
    check(not k627_t["full_block_gauge_has_nonzero_invariant_symmetric_form"] and k627_t["selecting_a_gram_is_a_gauge_reduction"], "K627 nonselection theorem moved")
    check(k627_t["K625_H_Sigma_is_one_projector_induced_point"] and not k627_t["K441_abstract_data_select_a_positive_gram"], "K627 canonical-point boundary moved")
    check(not any((k627_o["K625_canonical_realization_retracted"], k627_o["K626_embedding_gauge_retracted"], k627_o["full_gauge_nonselection_is_source_or_action_selection"], k627_o["orthogonal_reduction_is_supplied_by_K441"], k627_o["mixed_hessian_or_stationary_background_constructed"], k627_o["common_BV_Green_domain_constructed"])), "K627 ownership ceiling moved")
    check(not k627_d["abstract_K441_pairing_is_canonical_on_actual_carrier"] and k627_d["extra_reduction_data_required_to_select_pairing"] and not any((k627_d["actual_K596_K598_packet_released"], k627_d["selected_source_action_rejected"])), "K627 decision ceiling moved")

    k628 = data["k628"]
    k628_t = k628["determinant_obstruction_theorem"]
    k628_o = k628["ownership_reconciliation"]
    k628_d = k628["decision"]
    check(len(k628["cross_characteristic_packets"]) == 2, "K628 characteristic packet count moved")
    check(k628_t["obstructed_blocks"] == ["fast_outgoing", "fast_incoming", "slow_outgoing"] and k628_t["unobstructed_blocks"] == ["slow_incoming"], "K628 block obstruction fingerprint moved")
    check(not k628_t["K622_serialized_domain_map_preserves_some_nondegenerate_block_pairing"] and k628_t["K622_abstract_nonisometric_orbit_exists"], "K628 serialized-map/orbit boundary moved")
    check(not k628_t["every_K622_family_member_tested"] and not k628_t["alternative_domain_map_family_excluded"], "K628 family scope broadened")
    check(not any((k628_o["K622_abstract_orbit_retracted"], k628_o["K624_H_Sigma_obstruction_retracted"], k628_o["K627_gauge_nonselection_retracted"], k628_o["serialized_map_all_pairing_obstruction_is_action_selection"], k628_o["source_owned_domain_map_or_Gram_constructed"], k628_o["mixed_hessian_or_stationary_background_constructed"], k628_o["common_BV_Green_domain_constructed"])), "K628 ownership ceiling moved")
    check(not k628_d["K622_serialized_witness_can_be_repaired_by_only_changing_positive_Gram"] and not k628_d["broader_K622_family_pairing_orbit_decided"] and not any((k628_d["actual_K596_K598_packet_released"], k628_d["selected_source_action_rejected"])), "K628 decision ceiling moved")

    k625 = data["k625"]
    k625_t = k625["real_pairing_theorem"]
    k625_o = k625["ownership_reconciliation"]
    k625_d = k625["decision"]
    check(len(k625["cross_characteristic_packets"]) == 2, "K625 characteristic packet count moved")
    check(k625_t["four_eigenspaces_are_H_Sigma_orthogonal"] and k625_t["restricted_pairing_is_positive_definite_on_each_block"], "K625 positive orthogonal split moved")
    check(k625_t["isometric_factorized_coordinate_map_exists"] and k625_t["K441_rational_pair_rotations_pull_back_to_H_Sigma_isometries"], "K625 factorized bridge moved")
    check(k625_t["K441_closed_trace_domain_and_Green_conjugation_pull_back"] and not k625_t["ambient_coordinate_map_is_unique"], "K625 transport/nonuniqueness boundary moved")
    check(k625_o["K624_applies_to_canonical_projector_realization"] and not any((k625_o["K623_projector_pairing_retracted"], k625_o["K624_H_Sigma_obstruction_retracted"], k625_o["K441_selects_this_realization_uniquely"], k625_o["canonical_projector_realization_is_action_owned_adapter"], k625_o["stationary_background_or_mixed_hessian_constructed"])), "K625 ownership ceiling moved")
    check(k625_d["missing_ambient_pairing_bridge_constructed"] and k625_d["canonical_K441_realization_available"] and not any((k625_d["all_K441_ambient_realizations_identified"], k625_d["actual_K596_K598_packet_released"], k625_d["selected_source_action_rejected"])), "K625 decision ceiling moved")

    k626 = data["k626"]
    k626_t = k626["embedding_gauge_theorem"]
    k626_o = k626["ownership_reconciliation"]
    k626_d = k626["decision"]
    check(len(k626["cross_characteristic_packets"]) == 2, "K626 characteristic packet count moved")
    check(k626_t["gauge_group"] == "GL(192) x GL(192) x GL(64) x GL(64)", "K626 gauge group moved")
    check(k626_t["all_blockwise_changes_preserve_four_root_action_up_to_factorized_coordinates"] and not k626_t["K441_serializes_one_ambient_embedding"], "K626 abstract-model gauge boundary moved")
    check(k626_t["H_Sigma_is_a_canonical_projector_point_in_the_family"] and not k626_t["K624_normalized_trace_fingerprints_are_embedding_gauge_invariant"], "K626 canonical/gauge-invariance boundary moved")
    check(k626_t["actual_carrier_shears_tested"] == 8 and k626_t["every_tested_shear_changes_both_seed_fingerprints"], "K626 shear discriminator moved")
    check(not any((k626_o["K625_canonical_realization_retracted"], k626_o["K624_H_Sigma_obstruction_retracted"], k626_o["K624_universalized_to_every_K441_embedding"], k626_o["K441_abstract_transport_selects_an_ambient_Gram"], k626_o["embedding_gauge_is_source_or_action_selection"], k626_o["pairing_gauge_constructs_mixed_hessian_or_stationary_background"])), "K626 ownership ceiling moved")
    check(k626_d["canonical_projector_realization_classified"] and not k626_d["abstract_K441_pairing_alone_decides_K622_orbit"] and k626_d["source_or_action_owned_embedding_required_for_broader_verdict"], "K626 decision boundary moved")
    check(not any((k626_d["actual_K596_K598_packet_released"], k626_d["selected_source_action_rejected"])), "K626 protected decision moved")

    k623 = data["k623"]
    k623_t = k623["pairing_theorem"]
    k623_o = k623["ownership_reconciliation"]
    k623_d = k623["decision"]
    check(len(k623["cross_characteristic_packets"]) == 2, "K623 characteristic packet count moved")
    check(k623_t["domain_orthogonality_defect_rank"] == 96, "K623 domain orthogonality defect moved")
    check(k623_t["block_pullback_gram_defect_ranks"] == [128, 128, 64, 0], "K623 block Gram defects moved")
    check(k623_t["three_of_four_necessary_gram_identities_fail"] and not k623_t["K622_constructed_orbit_preserves_projector_pairing"], "K623 pairing verdict moved")
    check(not k623_t["arbitrary_domain_map_and_projector_pairing_isometric_orbit_excluded"], "K623 scope broadened")
    check(k623_t["projector_pairing_is_action_self_adjoint"] and not k623_t["projector_pairing_identified_with_K441_factorized_pairing"], "K623 projector/K441 pairing boundary moved")
    check(not any((k623_o["K622_abstract_orbit_equivalence_retracted"], k623_o["K622_constructed_domain_map_is_source_selected"], k623_o["pairing_failure_supplies_action_owned_adapter"], k623_o["common_BV_Green_domain_constructed"], k623_o["nonzero_stationary_background_constructed"])), "K623 ownership ceiling moved")
    check(not any((k623_d["constructed_K622_witness_passes_pairing_gate"], k623_d["K441_pairing_preservation_decided"], k623_d["actual_K596_K598_packet_released"], k623_d["selected_source_action_rejected"])), "K623 decision ceiling moved")

    k624 = data["k624"]
    k624_t = k624["simultaneous_congruence_theorem"]
    k624_o = k624["ownership_reconciliation"]
    k624_d = k624["decision"]
    check(len(k624["cross_characteristic_packets"]) == 2, "K624 characteristic packet count moved")
    check(k624_t["total_pullback_forms_are_nondegenerate"] and k624_t["trace_is_similarity_invariant"], "K624 normalized-form theorem moved")
    check(k624_t["all_four_first_traces_mismatch_at_both_primes"], "K624 trace obstruction moved")
    check(not k624_t["projector_pairing_preserving_commutant_and_domain_orbit_exists"] and k624_t["abstract_nonisometric_K622_orbit_exists"], "K624 orbit boundary moved")
    check(k624_t["pairing_model"] == "projector_induced_H_Sigma" and not k624_t["K441_factorized_pairing_identification_serialized"], "K624 projector/K441 pairing boundary moved")
    check(k624_o["projector_pairing_preserving_same_data_repair_excluded"] and not k624_o["different_action_owned_mixed_hessian_excluded"], "K624 same-data/new-data boundary moved")
    check(not any((k624_o["K621_fixed_domain_obstruction_retracted"], k624_o["K622_abstract_orbit_equivalence_retracted"], k624_o["common_BV_Green_domain_constructed"], k624_o["nonzero_stationary_background_constructed"])), "K624 ownership ceiling moved")
    check(not any((k624_d["current_seed_identification_can_preserve_projector_pairing"], k624_d["K441_pairing_preservation_decided"], k624_d["actual_K596_K598_packet_released"], k624_d["selected_source_action_rejected"])), "K624 decision ceiling moved")

    k621 = data["k621"]
    k621_t = k621["commutant_theorem"]
    k621_o = k621["ownership_reconciliation"]
    k621_d = k621["decision"]
    check(len(k621["cross_characteristic_packets"]) == 2, "K621 characteristic packet count moved")
    check(k621_t["full_commutant_dimension"] == 81920, "K621 commutant dimension moved")
    check(k621_t["fast_block_solution_affine_dimensions"] == [12288, 12288], "K621 fast solution dimensions moved")
    check(k621_t["slow_block_row_space_intersections"] == [0, 0] and k621_t["slow_block_row_space_joins"] == [128, 128], "K621 slow row-space obstruction moved")
    check(not k621_t["fixed_domain_commuting_adapter_exists"], "K621 fixed-domain adapter obstruction moved")
    check(k621_o["fixed_domain_nonpolynomial_commutant_adapter_excluded"] and not any((k621_o["full_commutant_is_action_owned_as_a_selected_adapter"], k621_o["source_domain_reparameterization_tested"], k621_o["mixed_hessian_or_domain_adapter_excluded"], k621_o["nonzero_stationary_background_constructed"])), "K621 ownership ceiling moved")
    check(k621_d["K620_functional_calculus_obstruction_strengthened"] and not any((k621_d["K619_common_module_retracted"], k621_d["actual_K596_K598_packet_released"], k621_d["selected_source_action_rejected"])), "K621 decision ceiling moved")

    k622 = data["k622"]
    k622_t = k622["orbit_theorem"]
    k622_o = k622["ownership_reconciliation"]
    k622_d = k622["decision"]
    check(len(k622["cross_characteristic_packets"]) == 2, "K622 characteristic packet count moved")
    check(k622_t["zero_seed_slow_row_pair_is_direct_sum"] and k622_t["moving_seed_slow_row_pair_is_direct_sum"], "K622 slow decompositions moved")
    check(k622_t["one_invertible_domain_reparameterization_matches_both_slow_rows"] and k622_t["invertible_commutant_and_domain_orbit_equivalence_exists"], "K622 orbit existence moved")
    check(not k622_t["fixed_domain_commutant_adapter_exists"] and k622_t["block_transport_affine_freedom_for_constructed_domain_map"] == 24576 and not k622_t["orbit_equivalence_selects_unique_adapter"], "K622 nonuniqueness/fixed-domain boundary moved")
    check(not any((k622_o["K621_fixed_domain_obstruction_retracted"], k622_o["domain_reparameterization_is_source_selected"], k622_o["commutant_transport_is_action_selected"], k622_o["orbit_equivalence_identifies_seed_constructions"], k622_o["pairing_or_Green_domain_preservation_proved"], k622_o["mixed_hessian_or_stationary_background_constructed"])), "K622 ownership ceiling moved")
    check(k622_d["full_abstract_commutant_orbit_is_nonempty"] and not any((k622_d["K619_common_module_retracted"], k622_d["actual_K596_K598_packet_released"], k622_d["selected_source_action_rejected"])), "K622 decision ceiling moved")

    k619 = data["k619"]
    k619_t = k619["common_module_theorem"]
    k619_o = k619["ownership_reconciliation"]
    k619_d = k619["decision"]
    check(len(k619["cross_characteristic_packets"]) == 2, "K619 characteristic packet count moved")
    check(k619_t["seed_intersection_rank"] == 0, "K619 seed intersection moved")
    check(k619_t["depth_2_intersection_rank"] == 128, "K619 depth-two intersection moved")
    check(k619_t["depth_3_join_rank"] == k619_t["depth_3_intersection_rank"] == 384, "K619 common hull equality moved")
    check(k619_t["filtrations_equal_from_depth_3"] and k619_t["corrected_carrier_complement_rank"] == 128, "K619 stabilization/complement moved")
    check(k619_o["source_owns_zero_form_field_space"] and not k619_o["source_selects_nonzero_zero_form_background"], "K619 source ownership boundary moved")
    check(not any((k619_o["historical_moving_graph_is_source_selected"], k619_o["equality_of_generated_subspaces_identifies_seed_maps"], k619_o["common_module_is_stationary_solution_space"], k619_o["common_module_supplies_mixed_hessian_coupling"])), "K619 ownership ceiling moved")
    check(k619_o["unrestricted_southeast_route_already_completed"] and k619_o["local_full_field_ordinary_gauge_bv_already_completed"], "K619 prior-route currency moved")
    check(k619_d["two_disjoint_seeds_generate_same_A_module"] and not any((k619_d["K615_stationarity_obstruction_retracted"], k619_d["actual_K596_K598_packet_released"], k619_d["selected_source_action_rejected"])), "K619 decision ceiling moved")

    k620 = data["k620"]
    k620_m = k620["module_projector_theorem"]
    k620_a = k620["seed_adapter_theorem"]
    k620_o = k620["ownership_reconciliation"]
    k620_d = k620["decision"]
    check(len(k620["cross_characteristic_packets"]) == 2, "K620 characteristic packet count moved")
    check(k620_m["fast_eigenspace_ranks"] == [192, 192] and k620_m["common_module_fast_ranks"] == [128, 128], "K620 fast block ranks moved")
    check(k620_m["slow_eigenspace_ranks"] == k620_m["common_module_slow_ranks"] == [64, 64], "K620 slow block ranks moved")
    check(not any((k620_m["common_module_is_union_of_full_eigenspaces"], k620_m["polynomial_projector_with_image_common_module_exists"], k620_m["polynomial_projector_with_image_rank128_complement_exists"])), "K620 module-projector obstruction moved")
    check(k620_a["each_seed_meets_all_four_eigenspaces"] and not k620_a["corresponding_seed_maps_scalar_proportional_in_any_eigenspace"] and not k620_a["scalar_polynomial_p_with_pA_J0_equals_X_exists"], "K620 seed-adapter obstruction moved")
    check(not k620_a["arbitrary_commutant_or_domain_endomorphism_tested"] and not k620_a["mixed_hessian_bilinear_adapter_constructed"], "K620 scope broadened")
    check(k620_o["A_owns_four_spectral_projectors"] and not any((k620_o["A_owns_common_module_projector"], k620_o["A_owns_seed_identification"], k620_o["A_invariance_of_common_module_implies_action_selection"], k620_o["nonpolynomial_action_owned_adapter_excluded"], k620_o["moving_nonlinear_mixed_hessian_excluded"])), "K620 ownership ceiling moved")
    check(not any((k620_d["K619_common_module_retracted"], k620_d["common_module_selected_by_frozen_action"], k620_d["zero_form_and_moving_graph_seeds_identified"], k620_d["actual_K596_K598_packet_released"], k620_d["selected_source_action_rejected"])), "K620 decision ceiling moved")

    k617 = data["k617"]
    k617_t = k617["descent_theorem"]
    k617_o = k617["ownership_reconciliation"]
    k617_d = k617["decision"]
    check(len(k617["cross_characteristic_packets"]) == 2, "K617 characteristic packet count moved")
    check(k617_t["both_pin_candidates_descend_injectively"] and k617_t["pin_candidates_become_identical_after_correction"], "K617 descent/collapse moved")
    check(k617_t["corrected_graph_rank"] == 128, "K617 corrected graph rank moved")
    check(k617_t["corrected_graph_intersection_K614_zero_seed_rank"] == 0 and k617_t["corrected_graph_join_K614_zero_seed_rank"] == 256, "K617 zero-seed relation moved")
    check(k617_t["all_four_frozen_spectral_sign_blocks_met"], "K617 spectral/sign coverage moved")
    check(k617_t["frozen_action_residual_rank"] == 128 and not k617_t["stationary_for_frozen_K438_action"], "K617 frozen-action residual moved")
    check(not any((k617_o["historical_graph_is_source_selected"], k617_o["bounded_graph_route_action_owned_by_unrestricted_four_field_action"], k617_o["corrected_descent_reverses_prior_action_ownership_kill"], k617_o["moving_differential_BV_Green_domain_constructed"], k617_o["mixed_hessian_Riesz_packet_constructed"])), "K617 ownership ceiling moved")
    check(k617_d["moving_graph_has_nontrivial_corrected_descent"] and not any((k617_d["K615_frozen_stationarity_obstruction_retracted"], k617_d["K616_unsplit_packet_obstruction_retracted"], k617_d["moving_graph_revives_bounded_action_owned_route"], k617_d["selected_source_action_rejected"])), "K617 decision ceiling moved")

    k618 = data["k618"]
    k618_h = k618["action_hull_theorem"]
    k618_o = k618["ownership_and_typing"]
    k618_r = k618["revival_gate"]
    k618_d = k618["decision"]
    check(len(k618["cross_characteristic_packets"]) == 2, "K618 characteristic packet count moved")
    check(k618_h["krylov_ranks_A0_through_A4"] == [128, 256, 384, 384, 384], "K618 Krylov ranks moved")
    check(k618_h["minimal_action_hull_rank"] == 384 and k618_h["corrected_carrier_complement_rank"] == 128 and not k618_h["action_hull_is_full_corrected_carrier"], "K618 hull/complement moved")
    check([k618_h[key] for key in ("fast_outgoing_missing_rank", "fast_incoming_missing_rank", "slow_outgoing_missing_rank", "slow_incoming_missing_rank")] == [64, 64, 0, 0], "K618 block complement moved")
    check(k618_o["spectral_vector_components_are_action_derived"] and not k618_o["action_derived_vector_split_owns_mixed_hessian_coupling"], "K618 vector/coupling ownership boundary moved")
    check(not k618_o["equal_rank_identifies_historical_and_current_hulls"] and not k618_o["bounded_route_action_owned"], "K618 rank coincidence or route ownership moved")
    check(k618_r["corrected_carrier_supplies_nontrivial_diagnostic_module"] and not k618_r["corrected_carrier_revives_historical_bounded_graph_as_action_subsystem"], "K618 revival gate moved")
    check(k618_r["K616_vector_projection_ownership_narrowed"] and not k618_r["K616_core_unsplit_packet_obstruction_retracted"], "K618 K616 reconciliation moved")
    check(not any((k618_d["K617_nontrivial_descent_retracted"], k618_d["K615_frozen_zero_form_obstruction_retracted"], k618_d["prior_unrestricted_Euler_route_kill_retracted"], k618_d["rank384_coincidence_promoted_to_identity"], k618_d["actual_K596_K598_packet_released"], k618_d["selected_source_action_rejected"])), "K618 decision ceiling moved")

    k615 = data["k615"]
    k615_r = k615["rank_fingerprint"]
    k615_f = k615["fibrewise_stationarity_theorem"]
    k615_c = k615["closed_domain_stationarity_theorem"]
    k615_d = k615["decision"]
    check(len(k615["cross_characteristic_packets"]) == 2, "K615 characteristic packet count moved")
    check(k615_r["action_euler_image"] == 128, "K615 Euler image rank moved")
    check(k615_r["outgoing_zero_form"] == k615_r["incoming_zero_form"] == 128, "K615 zero-form half ranks moved")
    check(k615_r["outgoing_euler"] == k615_r["incoming_euler"] == 128, "K615 Euler half ranks moved")
    check(k615_r["fast_euler"] == k615_r["slow_euler"] == 128, "K615 fast/slow Euler ranks moved")
    check(k615_f["kernel_dimension"] == 0 and not k615_f["nonzero_zero_form_value_is_stationary"], "K615 fibrewise stationarity moved")
    check(k615_c["K440_kernel_dimension"] == k615_c["K440_cokernel_dimension"] == 0, "K615 K440 kernel/cokernel moved")
    check(k615_c["four_source_fermion_slots_direct_sum_kernel_dimension"] == 0, "K615 four-field consequence moved")
    check(not k615_c["moving_lower_order_or_nonlinear_operator_covered"], "K615 scope broadened")
    check(not any((k615_d["nonzero_stationary_zero_form_in_K440_model_exists"], k615_d["four_field_frozen_stationary_background_nonzero"], k615_d["moving_nonlinear_nonzero_background_excluded"], k615_d["selected_source_action_rejected"], k615_d["K596_K598_released_by_stationarity"])), "K615 decision ceiling moved")

    k616 = data["k616"]
    k616_i = k616["input_injectivity"]
    k616_u = k616["unsplit_defect_theorem"]
    k616_m = k616["matching_half_repair"]
    k616_t = k616["transport_theorem"]
    k616_d = k616["decision"]
    check([k616_i[k] for k in ("outgoing_x_rank", "incoming_x_rank", "outgoing_y_rank", "incoming_y_rank")] == [128, 128, 128, 128], "K616 input half ranks moved")
    check(k616_i["every_nonzero_v_has_all_four_components_nonzero"], "K616 injectivity consequence moved")
    check(k616_u["rank_for_every_nonzero_v"] == 2 and not k616_u["natural_unsplit_packet_satisfies_K596"], "K616 unsplit defect moved")
    check(k616_m["typed_square_defect_rank"] == 0 and not k616_m["equals_natural_unsplit_packet"] and not k616_m["split_is_action_owned"], "K616 matching-half boundary moved")
    check(k616_t["rank_preserved"] and k616_t["rank_at_every_transport_fibre"] == 2 and not k616_t["moving_nonlinear_action_coupling_covered"], "K616 transport ceiling moved")
    check(k616_d["natural_unsplit_packet_rejected_in_frozen_model"] and not any((k616_d["matching_half_action_ownership_constructed"], k616_d["K596_actual_action_owned_packet_released"], k616_d["K598_actual_action_owned_packet_released"], k616_d["selected_source_action_rejected"])), "K616 decision ceiling moved")

    k614 = data["k614"]
    k614_f = k614["cross_characteristic_rank_fingerprint"]
    k614_t = k614["injection_theorem"]
    k614_b = k614["background_and_riesz_reconciliation"]
    k614_d = k614["decision"]
    check(len(k614["cross_characteristic_packets"]) == 2, "K614 characteristic packet count moved")
    check(k614_f["source_zero_form"] == k614_f["corrected_image"] == 128, "K614 corrected injection rank moved")
    check(k614_f["fast_projection"] == k614_f["slow_projection"] == 128, "K614 fast/slow ranks moved")
    check(k614_f["incoming_projection"] == k614_f["outgoing_projection"] == 128, "K614 sign-half ranks moved")
    check([k614_f[key] for key in ("fast_incoming_projection", "fast_outgoing_projection", "slow_incoming_projection", "slow_outgoing_projection")] == [128, 128, 64, 64], "K614 four-block ranks moved")
    check(k614_t["source_owned_zero_form_field"] and k614_t["image_lies_in_corrected_carrier"], "K614 source/injection ownership lost")
    check(k614_t["incoming_projection_is_injective"] and k614_t["outgoing_projection_is_injective"], "K614 sign-half injectivity lost")
    check(k614_t["fast_projection_is_injective"] and k614_t["slow_projection_is_injective"], "K614 speed injectivity lost")
    check(k614_t["all_four_action_spectral_sign_blocks_met"], "K614 spectral/sign coverage lost")
    check(k614_t["field_space_is_not_a_selected_field_value"], "K614 field/value distinction lost")
    check(k614_b["active_background"] == "zero fermion" and k614_b["injection_evaluated_on_active_background_is_zero"], "K614 zero-background boundary moved")
    check(k614_b["zero_fermion_current_rank"] == k614_b["zero_fermion_mixed_hessian_rank"] == 0, "K614 zero-background action ranks moved")
    check(not any((k614_b["nonzero_fermion_stationary_solution_owned"], k614_b["K441_action_Riesz_return_for_zero_form_background_owned"], k614_b["K596_actual_rank_one_packet_released"], k614_b["K598_actual_covariant_packet_released"])), "K614 missing background/Riesz packet invented")
    check(k614_d["source_owned_zero_form_injection_constructed"] and k614_d["K613_hypothetical_field_to_carrier_map_narrowed"], "K614 decision advance lost")
    check(not any((k614_d["action_owned_nonzero_background_constructed"], k614_d["actual_action_owned_soldering_constructed"], k614_d["K590_factorized_completion_retracted"], k614_d["K613_central_parity_obstruction_retracted"], k614_d["selected_source_action_rejected"])), "K614 decision ceiling moved")

    k612 = data["k612"]
    k612_s = k612["serialized_numeric_custody"]
    k612_m = k612["missing_quantitative_custody"]
    k612_c = k612["same_interface_countermodels"]
    k612_r = k612["dependency_reconciliation"]
    k612_d = k612["decision"]
    check(k612_s["chart_contraction_upper"] == "3/8", "K612 chart constant moved")
    check(k612_s["chart_inverse_norm_upper"] == "8/5", "K612 inverse constant moved")
    check(k612_s["physical_gram_interval"] == ["64/121", "64/25"], "K612 Gram interval moved")
    check(k612_s["existential_complete_sector_semibound"] and k612_s["matched_counterterm_cancellation_identified"], "K612 existential/cancellation input lost")
    check(not k612_s["raw_counterterm_separately_convergent"], "K612 raw counterterm incorrectly converges")
    check(not any((k612_m["named_regular_lower_bound_r0"], k612_m["named_complete_lower_bound_L0"], k612_m["named_graph_relative_bound_for_complete_cancelled_X"], k612_m["named_identity_constant_for_complete_cancelled_X"], k612_m["named_common_domain_for_chart_and_complete_core"])), "K612 missing custody fabricated")
    check(k612_c["floors_are_distinct"] and k612_c["no_uniform_floor_follows_from_serialized_interface"], "K612 countermodel conclusion lost")
    check(len(k612_c["rows"]) == 4, "K612 countermodel family size moved")
    check([row["native_floor"] for row in k612_c["rows"]] == ["-3", "-9", "-66", "-1026"], "K612 countermodel floors moved")
    check(not any((k612_r["K139_semiboundedness_retracted"], k612_r["K462_existential_coercivity_retracted"], k612_r["K581_noncyclic_inheritance_retracted"])), "K612 dependency retraction invented")
    check(k612_r["K611_mixed_graph_obstruction_preserved"] and k612_r["new_cancellation_adapted_estimate_still_live"], "K612 live escape lost")
    check(k612_d["K139_constant_extraction_from_current_serialized_custody_rejected"] and not any((k612_d["named_complete_sector_floor_emitted"], k612_d["named_noncyclic_floor_emitted"], k612_d["K473_released"], k612_d["native_K152_interval_emitted"])), "K612 decision ceiling moved")

    k613 = data["k613"]
    k613_p = k613["carrier_parity"]
    k613_s = k613["full_stabilizer_consequence"]
    k613_k = k613["K594_replay"]
    k613_r = k613["reopener"]
    k613_x = k613["dependency_reconciliation"]
    k613_d = k613["decision"]
    check(k613_p["all_available_generators_have_even_carrier_parity"], "K613 generator parity moved")
    check(k613_p["allowed_contractions_remove_carrier_slots_in_pairs"], "K613 contraction parity moved")
    check(k613_p["homogeneous_tensor_networks_preserve_even_carrier_parity"], "K613 tensor parity moved")
    check(not k613_p["nonzero_natural_vector_or_covector_from_even_inputs"], "K613 vector selector invented")
    check(k613_s["spectral_block_ranks"] == [192, 192, 64, 64], "K613 block ranks moved")
    check(k613_s["minimum_nonzero_invariant_endomorphism_rank"] == 64, "K613 minimum invariant rank moved")
    check(k613_s["possible_invariant_idempotent_ranks"] == [0, 64, 128, 192, 256, 320, 384, 448, 512], "K613 invariant ranks moved")
    check(not k613_s["rank_one_natural_endomorphism_from_current_tensors"], "K613 rank-one selector invented")
    check(k613_s["arbitrary_tensor_contraction_stronger_than_K610_factorwise_scope"], "K613 scope regression")
    check(not any((k613_k["one_carrier_slot_component_serialized"], k613_k["odd_carrier_valence_background_contraction_serialized"], k613_k["existing_third_jet_breaks_central_parity"])), "K613 K594 odd datum invented")
    check(not k613_r["affine_field_dependent_or_odd_action_data_ruled_out"], "K613 live odd escape lost")
    check(not any((k613_d["all_current_homogeneous_tensor_networks_select_vector_or_covector"], k613_d["all_current_homogeneous_tensor_networks_select_rank_one_packet"], k613_d["K598_released"])), "K613 decision ceiling moved")
    check(not any((k613_x["K590_factorized_complex_retracted"], k613_x["K600_no_selector_retracted"], k613_x["K607_action_symbol_refinement_retracted"], k613_x["K610_factorwise_obstruction_retracted"], k613_x["K598_actual_action_owned_packet_constructed"], k613_x["selected_source_action_rejected"])), "K613 dependency boundary moved")

    if check_digests:
        for name, entry in registry["basis"].items():
            if "path" in entry:
                check(digest(ROOT / entry["path"]) == entry["sha256"],
                      f"basis digest mismatch: {name}")
    return failures


def selftest(base: dict) -> tuple[int, int]:
    mutations = []

    def add(name: str, fn) -> None:
        case = copy.deepcopy(base)
        fn(case)
        mutations.append((name, case))

    add("k807-rank", lambda d: d["k807"]["orbit_consequence"].__setitem__("transported_rank", 122865))
    add("k808-kernel", lambda d: d["k808"]["extension_theorem"].__setitem__("embedded_transported_kernel_dimension", 0))
    add("k809-quotient", lambda d: d["k809"]["quotient_transport"].__setitem__("transported_persistent_classes", 0))
    add("k810-overclaim", lambda d: d["k810"]["decision"].__setitem__("global_sc_act_06_proved_or_refuted", True))
    add("k811-threshold", lambda d: d["k811"]["rank_theorem"].__setitem__("minimum_relative_rank_with_current_grant", 0))
    add("k812-sufficiency", lambda d: d["k812"]["transverse_theorem"].__setitem__("finite_parameter_sufficiency_follows", True))
    add("k813-budget", lambda d: d["k813"]["combined_budget_theorem"].__setitem__("beyond_current_grant_condition", "r+s>=1"))
    add("k814-overclaim", lambda d: d["k814"]["closure"].__setitem__("global_sc_act_06_proved_or_refuted", True))
    add("k815-source-delta", lambda d: d["k815"]["tangent_theorem"].__setitem__("parameter_source_equals_principal_correction", True))
    add("k816-overlap", lambda d: d["k816"]["exact_controls"].__setitem__("symmetry_union_rank", 4))
    add("k817-first-order-close", lambda d: d["k817"]["schur_theorem"].__setitem__("deficient_tau_implies_no_finite_parameter_repair", True))
    add("k818-sampling", lambda d: d["k818"]["uniformity_theorem"].__setitem__("finite_samples_imply_all_covectors", True))
    add("k819-first-implies-second", lambda d: d["k819"]["second_order_theorem"].__setitem__("first_order_pass_implies_second_order_pass", True))
    add("k820-rank-without-identities", lambda d: d["k820"]["differentiated_complex_theorem"].__setitem__("rank_budget_without_identities_is_credited", True))
    add("k821-arbitrary-slice", lambda d: d["k821"]["exact_controls"].__setitem__("arbitrary_rows_are_gauge_slice", True))
    add("k822-pointwise-uniform", lambda d: d["k822"]["uniform_persistence_theorem"].__setitem__("pointwise_thresholds_imply_common_interval", True))
    add("k823-infer-stationarity", lambda d: d["k823"]["stationarity_transport_theorem"].__setitem__("zero_locus_transport_implies_stationarity_transport", True))
    add("k824-one-sided-repair", lambda d: d["k824"]["mixed_symbol_schur_theorem"].__setitem__("one_sided_mixed_block_repairs_bosonic_kernel", True))
    add("k825-pointwise-domain", lambda d: d["k825"]["common_domain_theorem"].__setitem__("pointwise_closed_or_self_adjoint_implies_common_domain", True))
    add("k826-endpoint-ownership", lambda d: d["k826"]["ownership_theorem"].__setitem__("owned_endpoints_determine_relative_coefficient", True))
    add("k827-singular-same-class", lambda d: d["k827"]["jet_invariance_theorem"].__setitem__("singular_change_is_same_normalization_class", True))
    add("k828-domain-bijection-suffices", lambda d: d["k828"]["domain_transport_theorem"].__setitem__("domain_bijection_alone_defines_derivative", True))
    add("k829-kernel-authenticates-complex", lambda d: d["k829"]["schur_complex_theorem"].__setitem__("kernel_equivalence_alone_authenticates_reduced_complex", True))
    add("k830-partial-pass", lambda d: d["k830"]["compiler"].__setitem__("partial_pass_implies_ellipticity", True))
    add("k831-fredholm", lambda d: d["k831"]["operator_theorem"].__setitem__("fredholm", True))
    add("k832-unobstructed", lambda d: d["k832"]["decision"].__setitem__("actual_gu_unobstructedness_proved", True))
    add("k833-smooth-quotient", lambda d: d["k833"]["nonfree_control"].__setitem__("quotient_is_smooth_manifold_without_boundary_near_origin", True))
    add("k834-rich-without-nonlinear", lambda d: d["k834"]["exact_controls"].__setitem__("missing_nonlinear_rich_moduli_admitted", True))
    add("k835-quadratic-suffices", lambda d: d["k835"]["theorem"].__setitem__("vanishing_quadratic_obstruction_determines_integrability", True))
    add("k836-formal-determines-smooth", lambda d: d["k836"]["theorem"].__setitem__("complete_formal_series_determines_smooth_zero_germ", True))
    add("k837-finite-jet-suffices", lambda d: d["k837"]["analytic_identity_theorem"].__setitem__("finite_jet_order_suffices_without_degree_bound", True))
    add("k838-finite-formal-admissible", lambda d: d["k838"]["compiler"].__setitem__("finite_jet_or_formal_data_alone_admissible", True))
    add("k839-range-closed", lambda d: d["k839"]["limit_certificate"].__setitem__("range_closed", True))
    add("k840-uniform-radius", lambda d: d["k840"]["uniform_failure_certificate"].__setitem__("positive_N_uniform_injectivity_radius_exists", True))
    add("k841-origin-isolated", lambda d: d["k841"]["full_space_zero_set"].__setitem__("origin_is_isolated", True))
    add("k842-cutoff-admissible", lambda d: d["k842"]["compiler"].__setitem__("finite_cutoff_exactness_alone_admissible", True))
    add("k843-elliptic-estimate", lambda d: d["k843"]["theorem"].__setitem__("local_elliptic_quotient_estimate_holds", True))
    add("k844-middle-exact", lambda d: d["k844"]["microlocal_consequence"].__setitem__("current_flat_symbol_complex_is_middle_elliptic", True))
    add("k845-lower-order-repair", lambda d: d["k845"]["principal_invariance_theorem"].__setitem__("lower_order_only_repair_restores_local_elliptic_estimate", True))
    add("k846-global-verdict", lambda d: d["k846"]["decision"].__setitem__("SC_ACT_06_source_claim_proved_or_refuted", True))
    add("k847-raw-rank-sufficient", lambda d: d["k847"]["theorem"].__setitem__("raw_rank_budget_is_sufficient", True))
    add("k848-overlap-decides", lambda d: d["k848"]["comparison"].__setitem__("raw_rank_threshold_decides_exactness", True))
    add("k849-raw-rank-substitution", lambda d: d["k849"]["certificate"].__setitem__("raw_rank_substitution_allowed", True))
    add("k850-current-passes", lambda d: d["k850"]["decision"].__setitem__("current_flat_packet_passes_certificate", True))
    add("k851-gap-independent", lambda d: d["k851"]["theorem"].__setitem__("uniform_gap_is_separate_input_after_hypotheses", True))
    add("k852-finite-sampling", lambda d: d["k852"]["decision"].__setitem__("finite_sampling_proves_uniformity", True))
    add("k853-composition-unneeded", lambda d: d["k853"]["theorem"].__setitem__("composition_is_required", False))
    add("k854-current-robust", lambda d: d["k854"]["decision"].__setitem__("current_flat_packet_robust_admitted", True))
    add("k855-current-bundle", lambda d: d["k855"]["decision"].__setitem__("current_flat_packet_complete_cosphere_bundle_established", True))
    add("k856-current-hypotheses", lambda d: d["k856"]["decision"].__setitem__("current_flat_packet_bundle_hypotheses_established", True))
    add("k857-source-owned", lambda d: d["k857"]["decision"].__setitem__("source_owned_repair_maps_constructed", True))
    add("k858-current-repaired", lambda d: d["k858"]["decision"].__setitem__("current_flat_packet_repaired", True))
    add("k859-exact-rank-known", lambda d: d["k859"]["decision"].__setitem__("current_exact_old_cohomology_rank_known", True))
    add("k860-modules-authenticated", lambda d: d["k860"]["decision"].__setitem__("current_GU_isotropy_modules_authenticated", True))
    add("k861-natural-frame", lambda d: d["k861"]["decision"].__setitem__("K857_abstract_frame_promoted_to_natural_owner", True))
    add("k862-current-repaired", lambda d: d["k862"]["decision"].__setitem__("current_flat_packet_repaired", True))

    add("k696-form", lambda d: d["k696"]["integration_theorem"].__setitem__("graph_equivalence_without_form_identity_sufficient", True))
    add("k696-reduction", lambda d: d["k696"]["integration_theorem"].__setitem__("reduction_of_column_labels_alone_reduces_native_R", True))
    add("k696-native", lambda d: d["k696"]["native_interface_status"].__setitem__("actual_native_R_constructed", True))
    add("k697-cross", lambda d: d["k697"]["block_theorem"].__setitem__("seed_and_complement_norms_without_cross_or_reduction_sufficient", True))
    add("k697-reduction", lambda d: d["k697"]["block_theorem"].__setitem__("R_star_R_reduction_required_for_maximum_rule", False))
    add("k697-native", lambda d: d["k697"]["native_interface_status"].__setitem__("native_A_above_two_thirds_proved", True))
    add("k698-reference", lambda d: d["k698"]["end_to_end_theorem"].__setitem__("complete_Friedrichs_domain_inclusion_required", False))
    add("k698-trace", lambda d: d["k698"]["end_to_end_theorem"].__setitem__("finite_trace_block_without_tail_and_cross_sufficient", True))
    add("k698-coordinate", lambda d: d["k698"]["end_to_end_theorem"].__setitem__("same_boundary_coordinate_and_fixed_W_required", False))
    add("k698-native", lambda d: d["k698"]["native_interface_status"].__setitem__("actual_native_target_denominator_nonnegative", True))
    add("k699-finite", lambda d: d["k699"]["theorem"].__setitem__("finite_test_equality_sufficient", True))
    add("k699-complete", lambda d: d["k699"]["theorem"].__setitem__("complete_a_relative_mismatch_required", False))
    add("k699-native", lambda d: d["k699"]["native_interface_status"].__setitem__("native_A_above_two_thirds_proved", True))
    add("k700-cross", lambda d: d["k700"]["theorem"].__setitem__("complete_cross_bound_required_without_reduction", False))
    add("k700-blocks", lambda d: d["k700"]["theorem"].__setitem__("individual_compression_bounds_alone_sufficient", True))
    add("k700-native", lambda d: d["k700"]["native_interface_status"].__setitem__("actual_native_cross_bound_proved", True))
    add("k701-error", lambda d: d["k701"]["theorem"].__setitem__("outward_denominator_error_required", False))
    add("k701-coordinate", lambda d: d["k701"]["theorem"].__setitem__("same_boundary_coordinate_and_fixed_W_required", False))
    add("k701-native", lambda d: d["k701"]["native_interface_status"].__setitem__("actual_native_target_denominator_nonnegative", True))
    add("k702-errors", lambda d: d["k702"]["theorem"].__setitem__("all_three_errors_outward_required", False))
    add("k702-native", lambda d: d["k702"]["native_interface_status"].__setitem__("native_A_above_two_thirds_proved", True))
    add("k703-domain", lambda d: d["k703"]["theorem"].__setitem__("same_complete_graph_domain_required", False))
    add("k703-native", lambda d: d["k703"]["native_interface_status"].__setitem__("native_floor_above_five_eighths_proved", True))
    add("k704-joint", lambda d: d["k704"]["theorem"].__setitem__("joint_W_and_M_transport_required", False))
    add("k704-native", lambda d: d["k704"]["native_interface_status"].__setitem__("actual_native_target_denominator_nonnegative", True))
    add("k705-projector", lambda d: d["k705"]["theorem"].__setitem__("reduction_must_be_injective_on_curvature_image", False))
    add("k705-native", lambda d: d["k705"]["native_interface_status"].__setitem__("SC_ACT_06_ellipticity_proved", True))
    add("k706-frame", lambda d: d["k706"]["theorem"].__setitem__("gauge_and_euler_maps_must_transport_coherently", False))
    add("k706-native", lambda d: d["k706"]["native_interface_status"].__setitem__("native_frame_map_authenticated", True))
    add("k707-coupling", lambda d: d["k707"]["theorem"].__setitem__("off_diagonal_coupling_must_annihilate_gauge_image", False))
    add("k707-native", lambda d: d["k707"]["native_interface_status"].__setitem__("SC_ACT_06_ellipticity_proved", True))
    add("k708-signature", lambda d: d["k708"]["exact_controls"].__setitem__("native_total_signature", [14, 0, 0]))
    add("k708-native", lambda d: d["k708"]["native_interface_status"].__setitem__("real_euclidean_continuation_supplied", True))
    add("k709-inertia", lambda d: d["k709"]["theorem"].__setitem__("real_invertible_frame_can_map_13_1_to_14_0", True))
    add("k709-native", lambda d: d["k709"]["native_interface_status"].__setitem__("authenticated_real_euclidean_frame_constructed", True))
    add("k710-koszul", lambda d: d["k710"]["theorem"].__setitem__("koszul_exact_for_every_nonzero_covector_without_metric", False))
    add("k710-native", lambda d: d["k710"]["native_interface_status"].__setitem__("SC_ACT_06_ellipticity_proved", True))
    add("k711-hodge", lambda d: d["k711"]["theorem"].__setitem__("middle_exact_iff_positive_hodge_laplacian_invertible", False))
    add("k711-native", lambda d: d["k711"]["native_interface_status"].__setitem__("SC_ACT_06_ellipticity_proved", True))
    add("k712-aux", lambda d: d["k712"]["theorem"].__setitem__("auxiliary_positive_metric_exists_on_same_real_carrier", False))
    add("k712-native", lambda d: d["k712"]["native_interface_status"].__setitem__("SC_ACT_06_ellipticity_proved", True))
    add("k713-invariant", lambda d: d["k713"]["theorem"].__setitem__("positive_definite_O_13_1_invariant_form_exists", True))
    add("k713-native", lambda d: d["k713"]["native_interface_status"].__setitem__("SC_ACT_06_ellipticity_proved", True))
    add("k714-positive", lambda d: d["k714"]["theorem"].__setitem__("eta_theta_is_symmetric_positive_definite", False))
    add("k714-native", lambda d: d["k714"]["native_interface_status"].__setitem__("SC_ACT_06_ellipticity_proved", True))
    add("k715-covariant", lambda d: d["k715"]["theorem"].__setitem__("transported_q_equals_L_inverse_transpose_q_L_inverse", False))
    add("k715-native", lambda d: d["k715"]["native_interface_status"].__setitem__("SC_ACT_06_ellipticity_proved", True))
    add("k716-selection", lambda d: d["k716"]["theorem"].__setitem__("native_eta_selects_a_unique_reduction", True))
    add("k716-native", lambda d: d["k716"]["native_interface_status"].__setitem__("SC_ACT_06_ellipticity_proved", True))
    add("k717-owned", lambda d: d["k717"]["theorem"].__setitem__("background_frobenius_q_equals_eta_theta", False))
    add("k717-native", lambda d: d["k717"]["theorem"].__setitem__("SC_ACT_06_ellipticity_proved", True))
    add("k718-projector", lambda d: d["k718"]["theorem"].__setitem__("independent_euler_row_projector_constructed", False))
    add("k718-native", lambda d: d["k718"]["native_interface_status"].__setitem__("action_owned_bosonic_euler_symbol", True))
    add("k719-mixed", lambda d: d["k719"]["theorem"].__setitem__("boson_fermion_mixed_hessian_vanishes_at_zero_fermion", False))
    add("k719-native", lambda d: d["k719"]["native_interface_status"].__setitem__("complete_full_field_symbol", True))
    add("k723-curvature", lambda d: d["k723"]["principal_invariance_theorem"].__setitem__("curved_subprincipal_transport_can_repair_principal_cohomology", True))
    add("k723-rank", lambda d: d["k723"]["exact_controls"].__setitem__("nonnull_euler_rank", 229382))
    add("k723-repair", lambda d: d["k723"]["decision"].__setitem__("k127_ricci_flat_weyl_family_repairs_k722", True))
    add("k724-order", lambda d: d["k724"]["zero_order_theorem"].__setitem__("kappa_term_is_zero_order", False))
    add("k724-principal", lambda d: d["k724"]["zero_order_theorem"].__setitem__("kappa_changes_principal_symbol", True))
    add("k724-repair", lambda d: d["k724"]["zero_order_theorem"].__setitem__("nonzero_kappa_repairs_k720", True))
    add("k725-background", lambda d: d["k725"]["nonzero_t_admission_theorem"].__setitem__("nonzero_t_background_missing", False))
    add("k725-elliptic", lambda d: d["k725"]["nonzero_t_admission_theorem"].__setitem__("pointwise_full_rank_implies_principal_ellipticity", True))
    add("k725-input", lambda d: d["k725"]["decision"].__setitem__("current_serialized_candidates_supply_new_complete_bosonic_principal_data", True))
    add("k726-stationary", lambda d: d["k726"]["homogeneous_branch_theorem"].__setitem__("nonzero_kappa_branch_is_full_stationary_background", True))
    add("k726-trace", lambda d: d["k726"]["homogeneous_branch_theorem"].__setitem__("residual_square_cancels_metric_trace", True))
    add("k726-input", lambda d: d["k726"]["decision"].__setitem__("current_homogeneous_nonzero_t_branch_admissible_for_k722_retest", True))
    add("k727-owner", lambda d: d["k727"]["conditional_trace_repair"].__setitem__("repair_is_source_owned", True))
    add("k727-principal", lambda d: d["k727"]["conditional_trace_repair"].__setitem__("repair_changes_highest_order_euler_symbol", True))
    add("k727-exact", lambda d: d["k727"]["principal_invariance"].__setitem__("principal_middle_exact_after_algebraic_repair", True))
    add("k728-background", lambda d: d["k728"]["candidate_census"][0].__setitem__("direct_metric_euler_zero", True))
    add("k728-order", lambda d: d["k728"]["candidate_census"][2].__setitem__("differential_order", "PRINCIPAL"))
    add("k728-input", lambda d: d["k728"]["two_gate_theorem"].__setitem__("current_serialized_packet_passes_both_gates", True))
    add("k729-owner", lambda d: d["k729"]["owner_reconciliation"].__setitem__("printed_endpoint_residual_square_source_owned", False))
    add("k729-hessian", lambda d: d["k729"]["owner_reconciliation"].__setitem__("residual_zero_first_variation_zero_does_not_force_zero_hessian", False))
    add("k729-ceiling", lambda d: d["k729"]["serialized_bank"].__setitem__("universal_extension_rank_ceiling", 197))
    add("k730-weight", lambda d: d["k730"]["rank_theorem"].__setitem__("valid_for_every_scalar_weight", False))
    add("k730-cohomology", lambda d: d["k730"]["exact_controls"].__setitem__("nonnull_middle_cohomology_lower", 0))
    add("k730-repair", lambda d: d["k730"]["decision"].__setitem__("serialized_i2b_bank_can_repair_k720_to_middle_exactness", True))
    add("k731-mixed", lambda d: d["k731"]["composition_theorem"].__setitem__("mixed_boson_fermion_principal_blocks_vanish", False))
    add("k731-exact", lambda d: d["k731"]["composition_theorem"].__setitem__("arbitrary_weight_serialized_i2b_can_make_full_symbol_exact", True))
    add("k731-global", lambda d: d["k731"]["decision"].__setitem__("source_global_SC_ACT_06_refuted", True))
    add("k732-factor", lambda d: d["k732"]["factorization_theorem"].__setitem__("rank_H_le_rank_J", False))
    add("k732-rank", lambda d: d["k732"]["existing_all_grade_connection_response"].__setitem__("i2b_hessian_rank_ceiling", 1471))
    add("k732-background", lambda d: d["k732"]["existing_all_grade_connection_response"].__setitem__("same_stationary_background_as_k720_flat_germ", True))
    add("k733-grant", lambda d: d["k733"]["strongest_grant"].__setitem__("cross_background_transport_granted_for_dimension_test_only", False))
    add("k733-cohomology", lambda d: d["k733"]["exact_controls"].__setitem__("nonnull_middle_cohomology_lower", 0))
    add("k733-repair", lambda d: d["k733"]["decision"].__setitem__("existing_all_grade_connection_response_can_repair_k720_to_middle_exactness", True))
    add("k734-mixed", lambda d: d["k734"]["composition_theorem"].__setitem__("mixed_boson_fermion_principal_blocks_vanish", False))
    add("k734-exact", lambda d: d["k734"]["composition_theorem"].__setitem__("connection_only_i2b_grant_can_make_full_symbol_exact", True))
    add("k734-global", lambda d: d["k734"]["decision"].__setitem__("source_global_SC_ACT_06_refuted", True))
    add("k735-factor", lambda d: d["k735"]["factorization_theorem"].__setitem__("rank_H_le_rank_J", False))
    add("k735-total", lambda d: d["k735"]["selected_low_grade_tangent"].__setitem__("source_native_y14_first_jet_total", 1572))
    add("k735-expanded", lambda d: d["k735"]["selected_low_grade_tangent"].__setitem__("expanded_parent_covered", True))
    add("k736-cohomology", lambda d: d["k736"]["exact_controls"].__setitem__("nonnull_middle_cohomology_lower", 0))
    add("k736-repair", lambda d: d["k736"]["decision"].__setitem__("complete_selected_low_grade_parent_can_repair_k720_to_middle_exactness", True))
    add("k737-spin", lambda d: d["k737"]["candidate_parent_classification"][2].__setitem__("dimension_meets_both_requirements", False))
    add("k737-rank", lambda d: d["k737"]["candidate_parent_classification"][2].__setitem__("actual_response_rank_proved", True))
    add("k737-owner", lambda d: d["k737"]["ownership_controls"].__setitem__("moving_parent_selection", "SELECTED"))
    add("k738-mixed", lambda d: d["k738"]["composition_theorem"].__setitem__("mixed_boson_fermion_principal_blocks_vanish", False))
    add("k738-exact", lambda d: d["k738"]["composition_theorem"].__setitem__("selected_low_grade_i2b_grant_can_make_full_symbol_exact", True))
    add("k738-global", lambda d: d["k738"]["decision"].__setitem__("source_global_SC_ACT_06_refuted", True))
    add("k739-owner", lambda d: d["k739"]["decision"].__setitem__("full_connection_carrier_is_action_owned_at_zero_branch", False))
    add("k739-spin", lambda d: d["k739"]["exact_action_ownership"].__setitem__("hard_spin_reduction_generated_by_written_action", True))
    add("k740-spin-rank", lambda d: d["k740"]["exact_controls"]["cases"][0]["ranks"]["grade_saturated_spin"].__setitem__("rank", 0))
    add("k740-full-rank", lambda d: d["k740"]["exact_controls"]["cases"][1]["ranks"]["full_connection"].__setitem__("rank", 0))
    add("k740-zero-order", lambda d: d["k740"]["operator"].__setitem__("zero_order_hodge_kappa_u_included", True))
    add("k741-spin-cohom", lambda d: d["k741"]["exact_controls"]["cases"][0].__setitem__("spin_middle_cohomology_lower", 0))
    add("k741-full-exact", lambda d: d["k741"]["decision"].__setitem__("action_owned_full_connection_parent_proves_middle_exactness", True))
    add("k742-spin-exact", lambda d: d["k742"]["decision"].__setitem__("grade_saturated_spin_plus_displayed_fermion_realization_is_elliptic", True))
    add("k742-full-exact", lambda d: d["k742"]["decision"].__setitem__("action_owned_full_carrier_plus_displayed_fermion_is_proved_elliptic", True))
    add("k743-cap", lambda d: d["k743"]["exact_controls"]["cases"][0].__setitem__("distortion_universal_image_cap_rank", 0))
    add("k743-exact", lambda d: d["k743"]["decision"].__setitem__("every_same_response_residual_pairing_fails_middle_exactness", False))
    add("k744-rank", lambda d: d["k744"]["exact_controls"]["cases"][1].__setitem__("hessian_rank", 0))
    add("k744-repair", lambda d: d["k744"]["decision"].__setitem__("full_trace_pairing_repairs_middle_exactness", True))
    add("k745-gauge", lambda d: d["k745"]["exact_controls"]["cases"][0].__setitem__("gauge_rank", 0))
    add("k745-exact", lambda d: d["k745"]["decision"].__setitem__("same_response_residual_square_repair_is_elliptic", True))
    add("k746-mixed", lambda d: d["k746"]["composition_theorem"].__setitem__("middle_cohomology_is_direct_sum", False))
    add("k746-exact", lambda d: d["k746"]["decision"].__setitem__("displayed_full_symbol_realization_is_elliptic", True))
    add("k747-family", lambda d: d["k747"]["principal_transport_theorem"].__setitem__("same_response_image_cap_transports_over_certified_family", False))
    add("k747-cap", lambda d: d["k747"]["exact_controls"]["cases"][0].__setitem__("total_coupled_image_cap_rank", 0))
    add("k748-owner", lambda d: d["k748"]["ownership_theorem"].__setitem__("released_source_owns_third_independent_bosonic_principal_response", True))
    add("k748-nonexistence", lambda d: d["k748"]["ownership_theorem"].__setitem__("source_silent_path_adapter_is_proved_nonexistent", True))
    add("k749-exact", lambda d: d["k749"]["composition_theorem"].__setitem__("released_t0_full_symbol_family_elliptic", True))
    add("k749-cohom", lambda d: d["k749"]["exact_controls"]["cases"][1].__setitem__("full_symbol_middle_cohomology_lower_bound", 0))
    add("k750-global", lambda d: d["k750"]["gate_theorem"].__setitem__("global_SC_ACT_06_refuted", True))
    add("k750-retry", lambda d: d["k750"]["decision"].__setitem__("do_not_retry_same_response_t0_family", False))
    add("k751-body", lambda d: d["k751"]["theorem"].__setitem__("exact_supercomplex_implies_exact_body_complex", False))
    add("k751-nilpotent", lambda d: d["k751"]["theorem"].__setitem__("nilpotent_off_diagonal_blocks_can_change_body_exactness", True))
    add("k752-repair", lambda d: d["k752"]["composition_theorem"].__setitem__("minimal_nonzero_odd_saddle_repairs_middle_exactness", True))
    add("k752-cohom", lambda d: d["k752"]["exact_controls"]["cases"][0].__setitem__("body_middle_cohomology_lower_bound", 0))
    add("k753-stationary", lambda d: d["k753"]["admission_audit"].__setitem__("full_metric_stationary_j4_bodies", 1))
    add("k753-principal", lambda d: d["k753"]["admission_audit"].__setitem__("new_principal_derivative_image", True))
    add("k754-global", lambda d: d["k754"]["gate_theorem"].__setitem__("global_SC_ACT_06_refuted", True))
    add("k754-all", lambda d: d["k754"]["gate_theorem"].__setitem__("all_nonzero_fermion_or_condensate_actions_excluded", True))
    add("k755-square", lambda d: d["k755"]["operator"].__setitem__("exact_match", False))
    add("k755-source", lambda d: d["k755"]["source_grade"].__setitem__("exact_formula_released", True))
    add("k756-rank", lambda d: d["k756"]["theorem"].__setitem__("combined_relative_rank_per_internal_coefficient", 13))
    add("k756-reopen", lambda d: d["k756"]["decision"].__setitem__("current_one_connection_complex_reopened", True))
    add("k757-bounds", lambda d: d["k757"]["current_obstruction"].__setitem__("body_middle_bounds_preserved", [0, 0]))
    add("k757-insert", lambda d: d["k757"]["composition_theorem"].__setitem__("independent_doubled_adapter_can_be_inserted_without_rebuilding_complex", True))
    add("k758-owner", lambda d: d["k758"]["gate_theorem"].__setitem__("independent_doubled_candidate_is_action_owned", True))
    add("k758-global", lambda d: d["k758"]["gate_theorem"].__setitem__("global_SC_ACT_06_refuted", True))
    add("k759-rank", lambda d: d["k759"]["theorem"].__setitem__("update_rank_bound", "BROKEN"))
    add("k759-fixed", lambda d: d["k759"]["theorem"].__setitem__("requires_fixed_old_block", False))
    add("k760-formula", lambda d: d["k760"]["composed_formula"].__setitem__("native_null_auxiliary_nonzero", "BROKEN"))
    add("k760-repair", lambda d: d["k760"]["decision"].__setitem__("one_scalar_repairs_k749", True))
    add("k761-threshold", lambda d: d["k761"]["threshold"].__setitem__("minimum_m_not_excluded_by_dimension_on_both_strata", 1))
    add("k761-sufficient", lambda d: d["k761"]["decision"].__setitem__("m_at_least_98311_sufficient_for_exactness", True))
    add("k762-retry", lambda d: d["k762"]["decision"].__setitem__("do_not_retry_small_spectator_condensate_extension", False))
    add("k762-global", lambda d: d["k762"]["decision"].__setitem__("global_SC_ACT_06_refuted", True))
    add("k763-rank", lambda d: d["k763"]["theorem"].__setitem__("rank_update_bound", "BROKEN"))
    add("k763-global", lambda d: d["k763"]["decision"].__setitem__("global_SC_ACT_06_refuted", True))
    add("k764-rank", lambda d: d["k764"]["principal_support"].__setitem__("old_block_correction_rank_upper_r", 98311))
    add("k764-source", lambda d: d["k764"]["decision"].__setitem__("owner_is_source_or_GU_selected", True))
    add("k765-bound", lambda d: d["k765"]["composition"]["new_lower_bounds"].__setitem__("native_null_auxiliary_nonzero", 0))
    add("k765-repair", lambda d: d["k765"]["decision"].__setitem__("scalar_metric_control_repairs_k749", True))
    add("k766-retry", lambda d: d["k766"]["decision"].__setitem__("do_not_retry_low_rank_scalar_tensor_or_small_derivative_even_owner", False))
    add("k766-global", lambda d: d["k766"]["decision"].__setitem__("global_SC_ACT_06_refuted", True))
    add("k767-stationary", lambda d: d["k767"]["stationarity"].__setitem__("full_flat_germ_stationary_for_comparator", False))
    add("k767-source", lambda d: d["k767"]["ownership"].__setitem__("pure_curvature_square_is_source_I2B", True))
    add("k768-native-null-rank", lambda d: d["k768"]["exact_controls"]["rows"][1].__setitem__("connection_hessian_rank", 212992))
    add("k768-hodge", lambda d: d["k768"]["decision"].__setitem__("curvature_hessian_equals_gauge_fixed_hodge_laplacian", True))
    add("k769-bound", lambda d: d["k769"]["composition"]["rows"][1].__setitem__("k763_lower_bound", 0))
    add("k769-exact", lambda d: d["k769"]["decision"].__setitem__("positive_pairing_repairs_both_proved", True))
    add("k770-retry", lambda d: d["k770"]["decision"].__setitem__("do_not_retry_native_pairing_curvature_square_comparator", False))
    add("k770-global", lambda d: d["k770"]["decision"].__setitem__("global_SC_ACT_06_refuted", True))
    add("k771-rank", lambda d: d["k771"]["exact_controls"]["cases"][0].__setitem__("distortion_summed_operator_rank", 221184))
    add("k771-middle", lambda d: d["k771"]["exact_controls"]["cases"][1].__setitem__("bosonic_middle_cohomology_dimension", 0))
    add("k772-kernel", lambda d: d["k772"]["exact_controls"]["cases"][0].__setitem__("internal_candidate_kernel_dimension", 8192))
    add("k772-gauge", lambda d: d["k772"]["complex_theorem"].__setitem__("accidental_candidate_kernel_promoted_to_gauge", True))
    add("k773-full", lambda d: d["k773"]["exact_controls"]["cases"][1].__setitem__("full_symbol_middle_cohomology_dimension", 0))
    add("k773-elliptic", lambda d: d["k773"]["decision"].__setitem__("displayed_full_symbol_comparator_is_elliptic", True))
    add("k774-retry", lambda d: d["k774"]["decision"].__setitem__("do_not_retry_fixed_identity_cartan_unit_weight_comparator", False))
    add("k774-global", lambda d: d["k774"]["decision"].__setitem__("global_SC_ACT_06_refuted", True))
    add("k775-zero", lambda d: d["k775"]["variation_theorem"].__setitem__("residual_zero_first_variation_zero", False))
    add("k775-cancel", lambda d: d["k775"]["variation_theorem"].__setitem__("residual_zero_stationarity_can_cancel_first_action_euler", True))
    add("k776-rank", lambda d: d["k776"]["exact_composition"].__setitem__("combined_metric_euler_rank_for_nonzero_kappa", 0))
    add("k776-global", lambda d: d["k776"]["decision"].__setitem__("global_nonzero_T_stationarity_closed", True))
    add("k777-term", lambda d: d["k777"]["hessian_split"].__setitem__("nonzero_residual_makes_residual_curvature_term_potentially_live", False))
    add("k777-rank", lambda d: d["k777"]["hessian_split"].__setitem__("nonzero_residual_alone_proves_new_rank", True))
    add("k778-status", lambda d: d["k778"]["decision"].__setitem__("SC_ACT_06_status", "REFUTED"))
    add("k778-global", lambda d: d["k778"]["decision"].__setitem__("global_nonzero_T_no_go_proved", True))
    add("k779-image", lambda d: d["k779"]["theorem"].__setitem__("euler_covector_lies_in_image_J_star", False))
    add("k779-new", lambda d: d["k779"]["decision"].__setitem__("nonzero_residual_opens_new_first_variation_directions", True))
    add("k780-transverse", lambda d: d["k780"]["theorem"].__setitem__("pairing_or_finite_weight_can_cancel_transverse_component", True))
    add("k780-pairing", lambda d: d["k780"]["exact_control"].__setitem__("transverse_kernel_pairing", 0))
    add("k781-affine", lambda d: d["k781"]["theorem"].__setitem__("affine_residual_has_C_U_zero", False))
    add("k781-escape", lambda d: d["k781"]["exact_control"].__setitem__("curvature_image_escapes_im_J_star", False))
    add("k782-admit", lambda d: d["k782"]["decision"].__setitem__("candidate_admitted", True))
    add("k782-status", lambda d: d["k782"]["decision"].__setitem__("SC_ACT_06_status", "CONFIRMED"))
    add("k783-locus", lambda d: d["k783"]["source_custody"].__setitem__("claimed_solution_locus", "Upsilon!=0"))
    add("k783-route", lambda d: d["k783"]["decision"].__setitem__("nonzero_residual_is_direct_SC_ACT_06_input", True))
    add("k784-coefficient", lambda d: d["k784"]["ownership"].__setitem__("source_supplies_relative_sum_coefficient", True))
    add("k784-owned", lambda d: d["k784"]["ownership"].__setitem__("combined_stationarity_is_source_owned", True))
    add("k785-preserve", lambda d: d["k785"]["preserved_results"].__setitem__("K779_first_variation_image", False))
    add("k785-route", lambda d: d["k785"]["decision"].__setitem__("route_status", "SOURCE_NATIVE"))
    add("k786-custody", lambda d: d["k786"]["current_custody"].__setitem__("complete_first_order_linearization", True))
    add("k786-admit", lambda d: d["k786"]["decision"].__setitem__("candidate_admitted", True))
    add("k787-background", lambda d: d["k787"]["custody_reconciliation"].__setitem__("repository_constructs_local_source_typed_background", False))
    add("k787-search", lambda d: d["k787"]["decision"].__setitem__("background_search_remains_first_missing_input", True))
    add("k788-hessian", lambda d: d["k788"]["operator"].__setitem__("is_action_hessian", True))
    add("k788-rank", lambda d: d["k788"]["decision"].__setitem__("connection_response_rank", 122865))
    add("k788-orbits", lambda d: d["k788"]["orbit_theorem"].__setitem__("all_orbits_tested", False))
    add("k789-gauge", lambda d: d["k789"]["composition_theorem"].__setitem__("internal_candidate_promoted_to_source_owned_total_gauge", True))
    add("k789-lower", lambda d: d["k789"]["decision"].__setitem__("uniform_middle_cohomology_lower_bound", 0))
    add("k789-exact", lambda d: d["k789"]["decision"].__setitem__("all_three_orbits_middle_exact_under_maximal_grant", True))
    add("k790-exact", lambda d: d["k790"]["decision"].__setitem__("current_flat_packet_middle_exact", True))
    add("k790-global", lambda d: d["k790"]["decision"].__setitem__("global_SC_ACT_06_proved_or_refuted", True))
    add("k791-row", lambda d: d["k791"]["decision"].__setitem__("released_independent_first_order_bosonic_row_count_beyond_Upsilon", 1))
    add("k791-i2b", lambda d: d["k791"]["typing"].__setitem__("i2b_row_belongs_to_distinct_second_action", False))
    add("k792-factor", lambda d: d["k792"]["linearization"].__setitem__("xi_row_factors_through_direct_response", False))
    add("k792-kernel", lambda d: d["k792"]["exact_consequence"].__setitem__("stacked_row_kernel_dimension", 0))
    add("k793-columns", lambda d: d["k793"]["extension_lemma"].__setitem__("adding_field_columns_can_delete_old_kernel_vectors", True))
    add("k793-lower", lambda d: d["k793"]["exact_bound"].__setitem__("persistent_middle_classes_lower_bound", 0))
    add("k794-close", lambda d: d["k794"]["decision"].__setitem__("K717_direct_released_source_packet_closed", False))
    add("k794-global", lambda d: d["k794"]["decision"].__setitem__("global_SC_ACT_06_proved_or_refuted", True))
    add("k795-executable", lambda d: d["k795"]["decision"].__setitem__("current_complete_K500_AB_packet_executable", True))
    add("k795-native-a", lambda d: d["k795"]["decision"].__setitem__("current_native_A_packet_complete", True))
    add("k796-four-pairs", lambda d: d["k796"]["theorem"].__setitem__("all_four_A_B_truth_pairs_realized", False))
    add("k796-entails", lambda d: d["k796"]["theorem"].__setitem__("current_projection_entails_complete_K500_AB", True))
    add("k797-closure", lambda d: d["k797"]["decision"].__setitem__("current_serialized_K500_assembly_route_closed", False))
    add("k797-future", lambda d: d["k797"]["dependency_reconciliation"].__setitem__("future_native_AB_packet_excluded", True))
    add("k798-packet", lambda d: d["k798"]["decision"].__setitem__("unchanged_current_custody_K500_AB_packet_closed", False))
    add("k798-native", lambda d: d["k798"]["decision"].__setitem__("complete_native_K500_route_killed", True))

    add("k693-lower", lambda d: d["k693"]["graph_equivalence_theorem"].__setitem__("upper_bound_alone_sufficient_for_closedness", True))
    add("k693-native", lambda d: d["k693"]["native_interface_status"].__setitem__("actual_native_closed_column_proved", True))
    add("k693-floor", lambda d: d["k693"]["native_interface_status"].__setitem__("native_complete_floor_emitted", True))
    add("k694-tail", lambda d: d["k694"]["monotone_gram_theorem"].__setitem__("finite_prefix_without_complete_tail_sufficient", True))
    add("k694-core", lambda d: d["k694"]["monotone_gram_theorem"].__setitem__("order_on_nondense_test_space_sufficient", True))
    add("k694-native", lambda d: d["k694"]["native_interface_status"].__setitem__("actual_native_complete_tail_proved", True))
    add("k695-reference", lambda d: d["k695"]["friedrichs_authentication_theorem"].__setitem__("ordinary_triple_validity_alone_sufficient", True))
    add("k695-tail", lambda d: d["k695"]["defect_cofinal_theorem"].__setitem__("finite_block_without_tail_sufficient", True))
    add("k695-cross", lambda d: d["k695"]["defect_cofinal_theorem"].__setitem__("separate_block_lowers_without_cross_control_sufficient", True))
    add("k695-native", lambda d: d["k695"]["native_interface_status"].__setitem__("actual_native_complete_trace_coercivity_proved", True))

    add("k690-density", lambda d: d["k690"]["summable_core_theorem"].__setitem__("dense_common_core_required", False))
    add("k690-sum", lambda d: d["k690"]["summable_core_theorem"].__setitem__("complete_square_sum_required", False))
    add("k690-nonsummable", lambda d: d["k690"]["summable_core_theorem"].__setitem__("nonsummable_uniform_component_bounds_sufficient", True))
    add("k690-native", lambda d: d["k690"]["native_interface_status"].__setitem__("actual_native_maximal_domain_dense", True))
    add("k691-core", lambda d: d["k691"]["form_core_theorem"].__setitem__("one_common_form_core_for_both_required", False))
    add("k691-dense", lambda d: d["k691"]["form_core_theorem"].__setitem__("algebraically_dense_test_space_sufficient", True))
    add("k691-native", lambda d: d["k691"]["native_interface_status"].__setitem__("actual_native_CstarC_equals_H", True))
    add("k691-floor", lambda d: d["k691"]["native_interface_status"].__setitem__("native_complete_floor_emitted", True))
    add("k692-reference", lambda d: d["k692"]["friedrichs_gap_theorem"].__setitem__("authenticated_friedrichs_reference_required", False))
    add("k692-sector", lambda d: d["k692"]["friedrichs_gap_theorem"].__setitem__("finite_sector_lower_sufficient", True))
    add("k692-trace", lambda d: d["k692"]["defect_trace_theorem"].__setitem__("sampled_trace_vectors_sufficient", True))
    add("k692-native", lambda d: d["k692"]["native_interface_status"].__setitem__("actual_native_anchor_gamma_norm_proved", True))

    add("k687-density", lambda d: d["k687"]["countable_column_theorem"].__setitem__("density_hypothesis", "optional"))
    add("k687-prefix", lambda d: d["k687"]["countable_column_theorem"].__setitem__("finite_prefix_proves_complete_domain", True))
    add("k687-native", lambda d: d["k687"]["native_interface_status"].__setitem__("actual_native_column_closed", True))
    add("k687-floor", lambda d: d["k687"]["native_interface_status"].__setitem__("native_complete_floor_emitted", True))
    add("k688-prefix", lambda d: d["k688"]["partial_gram_theorem"].__setitem__("finite_partial_gram_without_tail_sufficient", True))
    add("k688-sampled", lambda d: d["k688"]["partial_gram_theorem"].__setitem__("diagonal_matrix_elements_on_sampled_vectors_sufficient", True))
    add("k688-native", lambda d: d["k688"]["native_interface_status"].__setitem__("actual_native_partial_gram_order_proved", True))
    add("k688-floor", lambda d: d["k688"]["native_interface_status"].__setitem__("native_complete_floor_emitted", True))
    add("k689-reference", lambda d: d["k689"]["gamma_resolvent_theorem"].__setitem__("same_reference_required", False))
    add("k689-gap", lambda d: d["k689"]["gamma_resolvent_theorem"].__setitem__("endpoint_membership_without_quantitative_gap_sufficient", True))
    add("k689-native", lambda d: d["k689"]["native_interface_status"].__setitem__("actual_native_target_gamma_norm_proved", True))
    add("k689-floor", lambda d: d["k689"]["native_interface_status"].__setitem__("native_complete_floor_emitted", True))

    add("k684-closed", lambda d: d["k684"]["closed_column_theorem"].__setitem__("unclosed_column_sufficient", True))
    add("k684-bounded", lambda d: d["k684"]["bounded_realization"].__setitem__("factorization_without_bounded_column_sufficient", True))
    add("k684-native", lambda d: d["k684"]["native_interface_status"].__setitem__("actual_native_complete_column_serialized", True))
    add("k684-floor", lambda d: d["k684"]["native_interface_status"].__setitem__("native_complete_floor_emitted", True))
    add("k685-tail", lambda d: d["k685"]["component_square_theorem"].__setitem__("finite_prefix_without_tail_sufficient", True))
    add("k685-geometry", lambda d: d["k685"]["component_square_theorem"].__setitem__("same_codomain_sum_without_cross_Gram_control_sufficient", True))
    add("k685-native", lambda d: d["k685"]["native_interface_status"].__setitem__("actual_native_complement_below_one_over_one_hundred", True))
    add("k685-floor", lambda d: d["k685"]["native_interface_status"].__setitem__("native_complete_floor_emitted", True))
    add("k686-space", lambda d: d["k686"]["gamma_field_identity"].__setitem__("complete_boundary_space_required", False))
    add("k686-finite", lambda d: d["k686"]["gamma_field_identity"].__setitem__("finite_sector_gamma_bounds_sufficient", True))
    add("k686-native", lambda d: d["k686"]["native_interface_status"].__setitem__("actual_native_complete_gamma_norms_proved", True))
    add("k686-floor", lambda d: d["k686"]["native_interface_status"].__setitem__("native_complete_floor_emitted", True))

    add("k681-density", lambda d: d["k681"]["monotone_form_theorem"].__setitem__("limit_density_required", False))
    add("k681-finite-prefix", lambda d: d["k681"]["monotone_form_theorem"].__setitem__("finite_prefix_sufficient", True))
    add("k681-native-r-free", lambda d: d["k681"]["native_interface_status"].__setitem__("actual_native_r_free_identified", True))
    add("k681-native-floor", lambda d: d["k681"]["native_interface_status"].__setitem__("native_complete_floor_emitted", True))
    add("k682-complete-domain", lambda d: d["k682"]["boundedness_theorem"].__setitem__("complete_domain_required", False))
    add("k682-factorization", lambda d: d["k682"]["boundedness_theorem"].__setitem__("factorization_alone_sufficient", True))
    add("k682-native-R", lambda d: d["k682"]["native_interface_status"].__setitem__("actual_native_R_bounded", True))
    add("k682-native-floor", lambda d: d["k682"]["native_interface_status"].__setitem__("native_complete_floor_emitted", True))
    add("k683-coordinate", lambda d: d["k683"]["level_transfer_theorem"].__setitem__("same_boundary_coordinate_required", False))
    add("k683-finite-block", lambda d: d["k683"]["level_transfer_theorem"].__setitem__("pointwise_or_finite_block_variation_sufficient", True))
    add("k683-native-denominator", lambda d: d["k683"]["native_interface_status"].__setitem__("actual_native_target_denominator_nonnegative", True))
    add("k683-native-floor", lambda d: d["k683"]["native_interface_status"].__setitem__("native_complete_floor_emitted", True))

    add("live-key-missing", lambda d: d["current"].pop("next_condition"))
    add("history-key-missing", lambda d: d["current"].pop("prior_conditions"))
    add("stale-25-66-live", lambda d: d["current"].__setitem__(
        "next_condition", d["current"]["next_condition"] + " 25 terminal and 66 open"))
    add("root-fabricated", lambda d: d["qualification"]["root_candidate_rebuild"].__setitem__(
        "current_named_root_candidate_set", ["SYNTHETIC-CBRS-1AC"]))
    add("terminal-count-moved", lambda d: d["dispositions"]["exhaustion_evaluation"].__setitem__(
        "terminal_rows", 90))
    add("b2-gate-reversed", lambda d: d["b2"]["basis"].__setitem__("b2_selectable", False))
    add("agenda-stale", lambda d: d["agenda"].__setitem__(
        "latest_result_2026_09_28_k608_k610", "Repeat the superseded K466 shifted-coercivity bridge."))
    add("agenda-latest-stale", lambda d: d["agenda"].__setitem__(
        "latest_result_2026_09_28_k600_k601", "K599 remains the latest result."))
    add("b5-rb6-repeat", lambda d: next(
        item for item in d["agenda"]["work_items"]
        if item["id"] == "B5-INDEPENDENT-RECONSTRUCTION"
    ).__setitem__("next_swing", "Step 0: recertify the remaining RB6 null with exact derivatives."))
    add("protected-effect-moved", lambda d: d["registry"]["protected_effects"].__setitem__(
        "ledger_verdict_change", True))

    add("k647-domain", lambda d: d["k647"]["intertwiner_theorem"].__setitem__("recursive_domain", "Dom(H0)"))
    add("k647-invariance", lambda d: d["k647"]["intertwiner_theorem"].__setitem__("recursive_domain_invariance", "unknown"))
    add("k647-gram", lambda d: d["k647"]["intertwiner_theorem"].__setitem__("physical_gram_covariance", "unknown"))
    add("k647-same-form", lambda d: d["k647"]["native_interface_status"].__setitem__("actual_K139_K168_same_form_identity_J_invariant", False))
    add("k647-floor", lambda d: d["k647"]["native_interface_status"].__setitem__("native_global_m_identified", True))
    add("k648-plus", lambda d: d["k648"]["total_parity_carriers"].__setitem__("total_plus", "C^3"))
    add("k648-scalar", lambda d: d["k648"]["total_parity_carriers"].__setitem__("three_scalar_channel_reduction", True))
    add("k648-couplings", lambda d: d["k648"]["quantitative_certificate_schema"].__setitem__("required_coupling_rows", "none"))
    add("k648-tail", lambda d: d["k648"]["quantitative_certificate_schema"].__setitem__("finite_prefix_is_tail", True))
    add("k648-floor", lambda d: d["k648"]["native_interface_status"].__setitem__("native_global_m_identified", True))

    add("k649-matching", lambda d: d["k649"]["parity_matching_theorem"].__setitem__("new_matching_condition", "unknown"))
    add("k649-divergence", lambda d: d["k649"]["parity_matching_theorem"].__setitem__("each_mismatched_parity_component_has_harmonic_divergent_direction", False))
    add("k649-bounded", lambda d: d["k649"]["parity_matching_theorem"].__setitem__("parity_change_makes_separate_singular_factors_bounded", True))
    add("k649-raw-route", lambda d: d["k649"]["quantitative_route_consequence"].__setitem__("K644_raw_row_route_automatically_available_from_parity", True))
    add("k649-floor", lambda d: d["k649"]["native_interface_status"].__setitem__("native_global_m_identified", True))
    add("k650-rho", lambda d: d["k650"]["cancelled_quadrant_theorem"].__setitem__("relative_range", "rho>1"))
    add("k650-raw", lambda d: d["k650"]["cancelled_quadrant_theorem"].__setitem__("separately_singular_raw_channel_bounds_required", True))
    add("k650-domain", lambda d: d["k650"]["cancelled_quadrant_theorem"].__setitem__("same_domain_required", False))
    add("k650-tail", lambda d: d["k650"]["native_quantitative_schema"].__setitem__("finite_prefix_is_tail", True))
    add("k650-floor", lambda d: d["k650"]["native_interface_status"].__setitem__("native_global_m_identified", True))
    add("k651-prefix", lambda d: d["k651"]["k179_prefix"].__setitem__("orders", list(range(2, 14))))
    add("k651-tail", lambda d: d["k651"]["prefix_nonidentifiability_theorem"].__setitem__("finite_prefix_determines_uniform_tail", True))
    add("k651-native", lambda d: d["k651"]["native_interface_status"].__setitem__("native_global_m_identified", True))
    add("k652-row", lambda d: d["k652"]["all_order_tail_theorem"].__setitem__("sector_row_floor", "g>=min(A,D)"))
    add("k652-prefix", lambda d: d["k652"]["all_order_tail_theorem"].__setitem__("finite_prefix_alone_sufficient", True))
    add("k652-native", lambda d: d["k652"]["native_interface_status"].__setitem__("actual_uniform_parity_tails_identified", True))
    add("k653-domain", lambda d: d["k653"]["shifted_schur_theorem"].__setitem__("same_domain_required", False))
    add("k653-target", lambda d: d["k653"]["native_interface_status"].__setitem__("actual_native_target_b_identified", True))
    add("k654-prefix", lambda d: d["k654"]["all_order_shifted_tail_theorem"].__setitem__("finite_prefix_alone_sufficient", True))
    add("k654-native", lambda d: d["k654"]["native_interface_status"].__setitem__("actual_uniform_parity_tails_identified", True))
    add("k655-native-row", lambda d: d["k655"]["interface_theorem"].__setitem__("actual_native_sector_row_identified", True))
    add("k655-target", lambda d: d["k655"]["native_interface_status"].__setitem__("actual_native_target_b_identified", True))
    add("k656-formula", lambda d: d["k656"]["base_floor_lift_theorem"].__setitem__("selected_target", "b=r0"))
    add("k656-r0", lambda d: d["k656"]["native_interface_status"].__setitem__("actual_native_base_floor_r0_identified", True))
    add("k659-promote-256", lambda d: d["k659"]["compensated_chart_theorem"].__setitem__("lambda_256_is_native_floor", True))
    add("k659-improve-floor", lambda d: d["k659"]["compensated_chart_theorem"].__setitem__("arbitrarily_large_chart_shift_improves_floor", True))
    add("k659-invent-s", lambda d: d["k659"]["semiboundedness_nonidentifiability"].__setitem__("numerical_s_identified", True))
    add("k659-deny-floor", lambda d: d["k659"]["semiboundedness_nonidentifiability"].__setitem__("fixed_native_operator_has_no_floor", True))
    add("k660-denominator", lambda d: d["k660"]["translation_theorem"].__setitem__("denominator_identity", "D'=D+C"))
    add("k660-create-friedrichs", lambda d: d["k660"]["translation_theorem"].__setitem__("friedrichs_status_created_by_translation", True))
    add("k660-unbounded", lambda d: d["k660"]["translation_theorem"].__setitem__("unbounded_translation_covered", True))
    add("k660-authenticate-regulator", lambda d: d["k660"]["composition"].__setitem__("K139_regulator_coordinates_already_authenticated_as_boundary_translation", True))
    add("k660-native-translation", lambda d: d["k660"]["native_interface_status"].__setitem__("actual_native_translation_law_proved", True))
    add("k661-green", lambda d: d["k661"]["interval_control"].__setitem__("green_identity_exact_on_polynomial_controls", False))
    add("k661-swap-friedrichs", lambda d: d["k661"]["interval_control"].__setitem__("swapped_reference_is_friedrichs", True))
    add("k661-convergence-selects", lambda d: d["k661"]["custody_theorem"].__setitem__("norm_resolvent_convergence_alone_selects_friedrichs", True))
    add("k661-deny-native", lambda d: d["k661"]["custody_theorem"].__setitem__("fixed_native_reference_is_not_friedrichs", True))
    add("k662-denominator", lambda d: d["k662"]["coordinate_group_theorem"].__setitem__("denominator_transform", "D'=D"))
    add("k662-create-friedrichs", lambda d: d["k662"]["coordinate_group_theorem"].__setitem__("friedrichs_status_created", True))
    add("k662-nonunitary-invariant", lambda d: d["k662"]["coordinate_group_theorem"].__setitem__("numerical_floor_invariant_for_general_U", True))
    add("k662-error", lambda d: d["k662"]["exact_controls"].__setitem__("error_bound_holds", False))
    add("k662-authenticate", lambda d: d["k662"]["composition"].__setitem__("K139_regulator_coordinates_already_authenticated_in_group", True))
    add("k665-one-parity", lambda d: d["k665"]["composition_theorem"].__setitem__("both_total_parities_required", False))
    add("k665-tail", lambda d: d["k665"]["composition_theorem"].__setitem__("independent_tail_for_each_parity_required", False))
    add("k665-lower", lambda d: d["k665"]["exact_control"].__setitem__("global_B_lower", "3/4"))
    add("k665-native", lambda d: d["k665"]["native_interface_status"].__setitem__("actual_complete_B_lower_identified", True))
    add("k666-domain", lambda d: d["k666"]["certificate_theorem"].__setitem__("K647_common_domain_required", False))
    add("k666-floor", lambda d: d["k666"]["exact_control"].__setitem__("certified_floor", "1/4"))
    add("k666-endpoint", lambda d: d["k666"]["exact_control"]["endpoint_control"].__setitem__("certified_floor", "1/8"))
    add("k666-native", lambda d: d["k666"]["native_interface_status"].__setitem__("native_complete_floor_emitted", True))
    add("k669-identity", lambda d: d["k669"]["factorization_bridge_theorem"].__setitem__("required_native_identity", "none"))
    add("k669-map", lambda d: d["k669"]["factorization_bridge_theorem"].__setitem__("equal_numerical_norm_without_map_identity_sufficient", True))
    add("k669-A", lambda d: d["k669"]["exact_bounds"].__setitem__("conservative_rational_A_lower", "3/4"))
    add("k669-native", lambda d: d["k669"]["native_interface_status"].__setitem__("actual_native_factorization_identified", True))
    add("k670-threshold", lambda d: d["k670"]["asymmetric_target_theorem"].__setitem__("selected_rational_B_target", "1/171"))
    add("k670-floor", lambda d: d["k670"]["exact_controls"].__setitem__("det_over_trace_floor", "0"))
    add("k670-tail", lambda d: d["k670"]["asymmetric_target_theorem"].__setitem__("both_total_parity_tails_required", False))
    add("k670-native", lambda d: d["k670"]["native_interface_status"].__setitem__("native_complete_floor_emitted", True))
    add("k673-full-domain", lambda d: d["k673"]["coverage_theorem"].__setitem__("K609_complete_domain_operator_norm_proved", True))
    add("k673-native", lambda d: d["k673"]["native_interface_status"].__setitem__("actual_complete_A_lower_identified", True))
    add("k674-test", lambda d: d["k674"]["compressed_bridge_theorem"].__setitem__("strict_two_thirds_test", "lambda<1/3"))
    add("k674-target", lambda d: d["k674"]["exact_native_target"].__setitem__("simple_sufficient_tau2_target", "1/10"))
    add("k674-native", lambda d: d["k674"]["native_interface_status"].__setitem__("actual_complete_A_lower_identified", True))
    add("k671-identifies", lambda d: d["k671"]["compensated_margin_theorem"].__setitem__("auxiliary_contraction_alone_identifies_A", True))
    add("k671-native", lambda d: d["k671"]["native_interface_status"].__setitem__("actual_invariant_total_A_lower_identified", True))
    add("k672-determinant", lambda d: d["k672"]["exact_controls"]["passing_control"].__setitem__("shifted_determinant", "0"))
    add("k672-native", lambda d: d["k672"]["native_interface_status"].__setitem__("actual_complete_A_lower_identified", True))
    add("k667-tail", lambda d: d["k667"]["telescoping_theorem"].__setitem__("complete_infinite_tail_controlled", False))
    add("k667-upper", lambda d: d["k667"]["exact_bounds"].__setitem__("upper", "1/256"))
    add("k667-native-A", lambda d: d["k667"]["native_interface_status"].__setitem__("actual_complete_A_lower_identified", True))
    add("k667-floor", lambda d: d["k667"]["native_interface_status"].__setitem__("native_complete_floor_emitted", True))
    add("k668-test", lambda d: d["k668"]["rational_target_theorem"].__setitem__("K667_sufficient_strict_test", "A>=mu"))
    add("k668-domain", lambda d: d["k668"]["rational_target_theorem"].__setitem__("complete_A_B_same_domain_required", False))
    add("k668-slack", lambda d: d["k668"]["exact_controls"]["positive_row"].__setitem__("determinant_slack_against_upper", "0"))
    add("k668-native", lambda d: d["k668"]["native_interface_status"].__setitem__("native_complete_floor_emitted", True))
    add("k663-floor", lambda d: d["k663"]["exact_control"].__setitem__("sharp_conservative_floor", "1/4"))
    add("k663-threshold", lambda d: d["k663"]["sharp_floor_theorem"].__setitem__("positive_floor_iff", "A>0 and B>0"))
    add("k663-native", lambda d: d["k663"]["native_interface_status"].__setitem__("actual_complete_effective_A_identified", True))
    add("k663-sharp", lambda d: d["k663"]["exact_control"].__setitem__("rayleigh_equals_floor", False))
    add("k664-finite", lambda d: d["k664"]["transfer_theorem"].__setitem__("finite_block_only_sufficient", True))
    add("k664-sampled", lambda d: d["k664"]["transfer_theorem"].__setitem__("sampled_sector_only_sufficient", True))
    add("k664-floors", lambda d: d["k664"]["exact_controls"].__setitem__("floors", ["1/2"]))
    add("k664-complement", lambda d: d["k664"]["exact_controls"].__setitem__("uncontrolled_complement_rejected", False))
    add("k664-native", lambda d: d["k664"]["native_interface_status"].__setitem__("actual_native_cofinal_packet_identified", True))
    add("k657-equivalence", lambda d: d["k657"]["ordinary_boundary_triple_theorem"].__setitem__("equivalence", "false"))
    add("k657-basis", lambda d: d["k657"]["ordinary_boundary_triple_theorem"].__setitem__("theorem_basis", "unknown"))
    add("k657-shift", lambda d: d["k657"]["ordinary_boundary_triple_theorem"].__setitem__("scalar_shift", "unknown"))
    add("k657-friedrichs", lambda d: d["k657"]["ordinary_boundary_triple_theorem"].__setitem__("reference_premise", "generic reference"))
    add("k657-weyl", lambda d: d["k657"]["ordinary_boundary_triple_theorem"].__setitem__("boundary_space_premise", "unbounded M"))
    add("k657-impurity", lambda d: d["k657"]["ordinary_boundary_triple_theorem"].__setitem__("finite_impurity_denominator_sufficient", True))
    add("k657-r0", lambda d: d["k657"]["native_interface_status"].__setitem__("actual_native_base_floor_r0_identified", True))
    add("k658-order", lambda d: d["k658"]["cofinal_margin_theorem"].__setitem__("order_consequence", "D>=d+eta"))
    add("k658-coverage", lambda d: d["k658"]["cofinal_margin_theorem"].__setitem__("complete_boundary_coverage_required", False))
    add("k658-native", lambda d: d["k658"]["native_interface_status"].__setitem__("actual_native_d_n_identified", True))

    add("k645-term-count", lambda d: d["k645"]["complete_family_replay"].__setitem__("terms", 2957))
    add("k645-orbits", lambda d: d["k645"]["complete_family_replay"].__setitem__("two_element_orbits", 1478))
    add("k645-phase", lambda d: d["k645"]["complete_family_replay"]["output_wedge_phase_counts"].__setitem__("-1", 0))
    add("k645-naive", lambda d: d["k645"]["complete_family_replay"].__setitem__("naive_sign_preservation_is_false", False))
    add("k645-native", lambda d: d["k645"]["native_interface_status"].__setitem__("native_global_m_identified", True))
    add("k646-sector", lambda d: d["k646"]["parity_reduction_theorem"].__setitem__("sector_floor", "m_n=m_n^+"))
    add("k646-global", lambda d: d["k646"]["parity_reduction_theorem"].__setitem__("global_floor", "m=inf_n m_n^+"))
    add("k646-cross", lambda d: d["k646"]["parity_reduction_theorem"].__setitem__("cross_parity_identity", "unknown"))
    add("k646-domain", lambda d: d["k646"]["native_interface_status"].__setitem__("actual_K139_K168_common_domain_identity_proved", True))
    add("k646-floor", lambda d: d["k646"]["native_interface_status"].__setitem__("native_global_m_identified", True))

    add("k643-term-count", lambda d: d["k643"]["native_replay"].__setitem__("term_count", 2957))
    add("k643-number", lambda d: d["k643"]["native_replay"].__setitem__("total_bath_number_preserved_by_every_exchange_monomial", False))
    add("k643-global", lambda d: d["k643"]["sector_reduction_theorem"].__setitem__("global_lower_constant", "m=m_0"))
    add("k643-tail", lambda d: d["k643"]["native_interface_status"].__setitem__("uniform_tail_lower_identified", True))
    add("k643-native-m", lambda d: d["k643"]["native_interface_status"].__setitem__("native_global_m_identified", True))
    add("k644-comparison", lambda d: d["k644"]["operator_block_theorem"].__setitem__("sharp_comparison_floor", "m_n=max_i d_i"))
    add("k644-row-negative", lambda d: d["k644"]["operator_block_theorem"].__setitem__("failed_row_sum_is_not_a_negative_spectrum_proof", False))
    add("k644-global", lambda d: d["k644"]["sector_to_global_composition"].__setitem__("global_output", "m=min prefix"))
    add("k644-common-domain", lambda d: d["k644"]["native_interface_status"].__setitem__("actual_K139_K168_common_domain_identity_proved", True))
    add("k644-diagonals", lambda d: d["k644"]["native_interface_status"].__setitem__("actual_diagonal_sector_floors_identified", True))
    add("k644-couplings", lambda d: d["k644"]["native_interface_status"].__setitem__("actual_off_diagonal_sector_bounds_identified", True))
    add("k644-floor", lambda d: d["k644"]["native_interface_status"].__setitem__("native_complete_sector_floor_emitted", True))

    add("k635-join", lambda d: d["k635"]["cross_characteristic_packets"][0].__setitem__("slow_kernel_join_rank", 64))
    add("k635-algebra", lambda d: d["k635"]["stabilizer_theorem"].__setitem__("induced_source_algebra_dimension", 1))
    add("k635-stabilizer", lambda d: d["k635"]["stabilizer_theorem"].__setitem__("full_commutant_seed_stabilizer_dimension", 8192))
    add("k635-selected", lambda d: d["k635"]["stabilizer_theorem"].__setitem__("every_induced_operator_is_selected_by_the_action", True))
    add("k635-owner", lambda d: d["k635"]["ownership_reconciliation"].__setitem__("independently_action_owned_source_endomorphism_found", True))
    add("k635-release", lambda d: d["k635"]["decision"].__setitem__("algebraic_existence_releases_K596_K598", True))
    add("k636-domain", lambda d: d["k636"]["cancellation_graph_theorem"].__setitem__("cancellation_domain_strictly_contains_trace_domain", False))
    add("k636-equivalent", lambda d: d["k636"]["cancellation_graph_theorem"].__setitem__("equivalent_norm_repair", True))
    add("k636-alpha", lambda d: d["k636"]["matching_uniqueness"].__setitem__("matched_coefficient", "alpha=0"))
    add("k636-core", lambda d: d["k636"]["dependency_reconciliation"].__setitem__("complete_K139_K168_core_controlled", True))
    add("k636-floor", lambda d: d["k636"]["dependency_reconciliation"].__setitem__("named_complete_sector_floor_emitted", True))
    add("k636-release", lambda d: d["k636"]["decision"].__setitem__("quantitative_complete_form_part_released", True))

    add("k633-join", lambda d: d["k633"]["cross_characteristic_packets"][0].__setitem__("seed_action_seed_join_rank", 128))
    add("k633-quotient", lambda d: d["k633"]["cross_characteristic_packets"][0].__setitem__("nonconstant_quotient_coefficient_rank", 2))
    add("k633-stabilizer", lambda d: d["k633"]["stabilizer_theorem"].__setitem__("polynomial_stabilizer_dimension", 2))
    add("k633-endomorphism", lambda d: d["k633"]["stabilizer_theorem"].__setitem__("nontrivial_owned_source_endomorphism_obtained", True))
    add("k633-scope", lambda d: d["k633"]["ownership_reconciliation"].__setitem__("arbitrary_commutant_or_mixed_hessian_excluded", True))
    add("k633-release", lambda d: d["k633"]["decision"].__setitem__("actual_K596_K598_packet_released", True))
    add("k634-membership", lambda d: d["k634"]["equivalent_norm_theorem"].__setitem__("membership_of_boundary_profile_is_unchanged", False))
    add("k634-continuity", lambda d: d["k634"]["equivalent_norm_theorem"].__setitem__("continuity_of_every_linear_trace_is_invariant", False))
    add("k634-repair", lambda d: d["k634"]["bounded_correlation_corollary"].__setitem__("point_trace_continuity_repaired", True))
    add("k634-scope", lambda d: d["k634"]["decision"].__setitem__("all_correlated_domains_ruled_out", True))
    add("k634-floor", lambda d: d["k634"]["surviving_domain_class"].__setitem__("named_quantitative_floor_constructed", True))

    add("k631-count", lambda d: d["k631"].__setitem__("candidate_count", 7))
    add("k631-ambient", lambda d: d["k631"]["census_theorem"].__setitem__("single_candidate_matching_ambient_gram", True))
    add("k631-composition", lambda d: d["k631"]["census_theorem"].__setitem__("composition_loophole_left_for_K632", False))
    add("k631-retract", lambda d: d["k631"]["ownership_reconciliation"].__setitem__("K614_source_owned_injection_retracted", True))
    add("k632-exhausted", lambda d: d["k632"]["closure_theorem"].__setitem__("current_serialized_operation_set_exhausted", False))
    add("k632-gram", lambda d: d["k632"]["closure_theorem"].__setitem__("owned_ambient_Gram_reachable", True))
    add("k632-pullback", lambda d: d["k632"]["closure_theorem"].__setitem__("nondegenerate_unowned_source_pullback_forms_reachable", False))
    add("k632-universal", lambda d: d["k632"]["closure_theorem"].__setitem__("universal_future_action_no_go", True))
    add("k632-release", lambda d: d["k632"]["decision"].__setitem__("actual_K596_K598_packet_released", True))
    add("k632-retract", lambda d: d["k632"]["ownership_reconciliation"].__setitem__("K625_H_Sigma_retracted", True))

    add("k629-dimension", lambda d: d["k629"]["determinant_line_theorem"].__setitem__("family_parameter_group_dimension", 4096))
    add("k629-slow-ratios", lambda d: d["k629"]["determinant_line_theorem"].__setitem__("combined_slow_ratio_squares", [1, 1]))
    add("k629-fast-ratios", lambda d: d["k629"]["determinant_line_theorem"].__setitem__("both_fast_ratio_squares", [949, 1004]))
    add("k629-family", lambda d: d["k629"]["determinant_line_theorem"].__setitem__("every_K622_family_member_tested", False))
    add("k629-repair", lambda d: d["k629"]["decision"].__setitem__("K622_family_contains_pairing_preserving_repair", True))
    add("k629-owner", lambda d: d["k629"]["ownership_reconciliation"].__setitem__("family_wide_pairing_obstruction_is_action_selection", True))
    add("k630-ratios", lambda d: d["k630"]["gauge_invariance_theorem"].__setitem__("invariant_slow_ratio_squares", [1, 1]))
    add("k630-invariant", lambda d: d["k630"]["gauge_invariance_theorem"].__setitem__("all_tested_source_and_ambient_gauges_preserve_obstruction", False))
    add("k630-artifact", lambda d: d["k630"]["gauge_invariance_theorem"].__setitem__("K629_family_obstruction_is_coordinate_artifact", True))
    add("k630-pivot", lambda d: d["k630"]["decision"].__setitem__("admissible_common_basis_or_pivot_change_reopens_K622_pairing_family", True))
    add("k630-owner", lambda d: d["k630"]["ownership_reconciliation"].__setitem__("ambient_gauge_invariance_selects_a_positive_Gram", True))

    add("k627-dimension", lambda d: d["k627"]["pairing_nonselection_theorem"].__setitem__("total_positive_pairing_family_dimension", 41215))
    add("k627-invariant", lambda d: d["k627"]["pairing_nonselection_theorem"].__setitem__("full_block_gauge_has_nonzero_invariant_symmetric_form", True))
    add("k627-reduction", lambda d: d["k627"]["pairing_nonselection_theorem"].__setitem__("selecting_a_gram_is_a_gauge_reduction", False))
    add("k627-selected", lambda d: d["k627"]["pairing_nonselection_theorem"].__setitem__("K441_abstract_data_select_a_positive_gram", True))
    add("k627-owner", lambda d: d["k627"]["ownership_reconciliation"].__setitem__("orthogonal_reduction_is_supplied_by_K441", True))
    add("k627-release", lambda d: d["k627"]["decision"].__setitem__("actual_K596_K598_packet_released", True))
    add("k628-blocks", lambda d: d["k628"]["determinant_obstruction_theorem"].__setitem__("obstructed_blocks", ["fast_outgoing"]))
    add("k628-pairing", lambda d: d["k628"]["determinant_obstruction_theorem"].__setitem__("K622_serialized_domain_map_preserves_some_nondegenerate_block_pairing", True))
    add("k628-family", lambda d: d["k628"]["determinant_obstruction_theorem"].__setitem__("every_K622_family_member_tested", True))
    add("k628-retract", lambda d: d["k628"]["ownership_reconciliation"].__setitem__("K622_abstract_orbit_retracted", True))
    add("k628-owner", lambda d: d["k628"]["ownership_reconciliation"].__setitem__("source_owned_domain_map_or_Gram_constructed", True))
    add("k628-broader", lambda d: d["k628"]["decision"].__setitem__("broader_K622_family_pairing_orbit_decided", True))

    add("k625-orthogonal", lambda d: d["k625"]["real_pairing_theorem"].__setitem__("four_eigenspaces_are_H_Sigma_orthogonal", False))
    add("k625-positive", lambda d: d["k625"]["real_pairing_theorem"].__setitem__("restricted_pairing_is_positive_definite_on_each_block", False))
    add("k625-bridge", lambda d: d["k625"]["real_pairing_theorem"].__setitem__("isometric_factorized_coordinate_map_exists", False))
    add("k625-rotation", lambda d: d["k625"]["real_pairing_theorem"].__setitem__("K441_rational_pair_rotations_pull_back_to_H_Sigma_isometries", False))
    add("k625-unique", lambda d: d["k625"]["real_pairing_theorem"].__setitem__("ambient_coordinate_map_is_unique", True))
    add("k625-k624", lambda d: d["k625"]["ownership_reconciliation"].__setitem__("K624_applies_to_canonical_projector_realization", False))
    add("k625-action-owner", lambda d: d["k625"]["ownership_reconciliation"].__setitem__("canonical_projector_realization_is_action_owned_adapter", True))
    add("k625-all-embeddings", lambda d: d["k625"]["decision"].__setitem__("all_K441_ambient_realizations_identified", True))
    add("k625-release", lambda d: d["k625"]["decision"].__setitem__("actual_K596_K598_packet_released", True))
    add("k626-gauge", lambda d: d["k626"]["embedding_gauge_theorem"].__setitem__("gauge_group", "O(512)"))
    add("k626-embedding-selected", lambda d: d["k626"]["embedding_gauge_theorem"].__setitem__("K441_serializes_one_ambient_embedding", True))
    add("k626-invariant", lambda d: d["k626"]["embedding_gauge_theorem"].__setitem__("K624_normalized_trace_fingerprints_are_embedding_gauge_invariant", True))
    add("k626-shears", lambda d: d["k626"]["embedding_gauge_theorem"].__setitem__("actual_carrier_shears_tested", 4))
    add("k626-fingerprints", lambda d: d["k626"]["embedding_gauge_theorem"].__setitem__("every_tested_shear_changes_both_seed_fingerprints", False))
    add("k626-universalize", lambda d: d["k626"]["ownership_reconciliation"].__setitem__("K624_universalized_to_every_K441_embedding", True))
    add("k626-action-owner", lambda d: d["k626"]["ownership_reconciliation"].__setitem__("embedding_gauge_is_source_or_action_selection", True))
    add("k626-orbit", lambda d: d["k626"]["decision"].__setitem__("abstract_K441_pairing_alone_decides_K622_orbit", True))
    add("k626-requirement", lambda d: d["k626"]["decision"].__setitem__("source_or_action_owned_embedding_required_for_broader_verdict", False))
    add("k626-release", lambda d: d["k626"]["decision"].__setitem__("actual_K596_K598_packet_released", True))

    add("k623-domain-defect", lambda d: d["k623"]["pairing_theorem"].__setitem__("domain_orthogonality_defect_rank", 0))
    add("k623-gram-defects", lambda d: d["k623"]["pairing_theorem"].__setitem__("block_pullback_gram_defect_ranks", [0, 0, 0, 0]))
    add("k623-pairing", lambda d: d["k623"]["pairing_theorem"].__setitem__("K622_constructed_orbit_preserves_projector_pairing", True))
    add("k623-scope", lambda d: d["k623"]["pairing_theorem"].__setitem__("arbitrary_domain_map_and_projector_pairing_isometric_orbit_excluded", True))
    add("k623-self-adjoint", lambda d: d["k623"]["pairing_theorem"].__setitem__("projector_pairing_is_action_self_adjoint", False))
    add("k623-k441-identification", lambda d: d["k623"]["pairing_theorem"].__setitem__("projector_pairing_identified_with_K441_factorized_pairing", True))
    add("k623-k441-decision", lambda d: d["k623"]["decision"].__setitem__("K441_pairing_preservation_decided", True))
    add("k623-retract", lambda d: d["k623"]["ownership_reconciliation"].__setitem__("K622_abstract_orbit_equivalence_retracted", True))
    add("k623-release", lambda d: d["k623"]["decision"].__setitem__("actual_K596_K598_packet_released", True))
    add("k624-trace", lambda d: d["k624"]["simultaneous_congruence_theorem"].__setitem__("all_four_first_traces_mismatch_at_both_primes", False))
    add("k624-isometric-orbit", lambda d: d["k624"]["simultaneous_congruence_theorem"].__setitem__("projector_pairing_preserving_commutant_and_domain_orbit_exists", True))
    add("k624-pairing-model", lambda d: d["k624"]["simultaneous_congruence_theorem"].__setitem__("pairing_model", "K441_factorized_pairing"))
    add("k624-k441-identification", lambda d: d["k624"]["simultaneous_congruence_theorem"].__setitem__("K441_factorized_pairing_identification_serialized", True))
    add("k624-abstract-orbit", lambda d: d["k624"]["simultaneous_congruence_theorem"].__setitem__("abstract_nonisometric_K622_orbit_exists", False))
    add("k624-new-data", lambda d: d["k624"]["ownership_reconciliation"].__setitem__("different_action_owned_mixed_hessian_excluded", True))
    add("k624-domain", lambda d: d["k624"]["ownership_reconciliation"].__setitem__("common_BV_Green_domain_constructed", True))
    add("k624-release", lambda d: d["k624"]["decision"].__setitem__("actual_K596_K598_packet_released", True))
    add("k624-k441-decision", lambda d: d["k624"]["decision"].__setitem__("K441_pairing_preservation_decided", True))

    add("k621-dimension", lambda d: d["k621"]["commutant_theorem"].__setitem__("full_commutant_dimension", 4))
    add("k621-fast-solutions", lambda d: d["k621"]["commutant_theorem"].__setitem__("fast_block_solution_affine_dimensions", [0, 0]))
    add("k621-slow-intersection", lambda d: d["k621"]["commutant_theorem"].__setitem__("slow_block_row_space_intersections", [64, 64]))
    add("k621-slow-join", lambda d: d["k621"]["commutant_theorem"].__setitem__("slow_block_row_space_joins", [64, 64]))
    add("k621-adapter", lambda d: d["k621"]["commutant_theorem"].__setitem__("fixed_domain_commuting_adapter_exists", True))
    add("k621-owner", lambda d: d["k621"]["ownership_reconciliation"].__setitem__("full_commutant_is_action_owned_as_a_selected_adapter", True))
    add("k621-domain-tested", lambda d: d["k621"]["ownership_reconciliation"].__setitem__("source_domain_reparameterization_tested", True))
    add("k621-release", lambda d: d["k621"]["decision"].__setitem__("actual_K596_K598_packet_released", True))
    add("k622-slow-pair", lambda d: d["k622"]["orbit_theorem"].__setitem__("zero_seed_slow_row_pair_is_direct_sum", False))
    add("k622-domain-map", lambda d: d["k622"]["orbit_theorem"].__setitem__("one_invertible_domain_reparameterization_matches_both_slow_rows", False))
    add("k622-orbit", lambda d: d["k622"]["orbit_theorem"].__setitem__("invertible_commutant_and_domain_orbit_equivalence_exists", False))
    add("k622-fixed-domain", lambda d: d["k622"]["orbit_theorem"].__setitem__("fixed_domain_commutant_adapter_exists", True))
    add("k622-unique", lambda d: d["k622"]["orbit_theorem"].__setitem__("orbit_equivalence_selects_unique_adapter", True))
    add("k622-source-selected", lambda d: d["k622"]["ownership_reconciliation"].__setitem__("domain_reparameterization_is_source_selected", True))
    add("k622-pairing", lambda d: d["k622"]["ownership_reconciliation"].__setitem__("pairing_or_Green_domain_preservation_proved", True))
    add("k622-release", lambda d: d["k622"]["decision"].__setitem__("actual_K596_K598_packet_released", True))

    add("k617-rank", lambda d: d["k617"]["descent_theorem"].__setitem__("corrected_graph_rank", 127))
    add("k617-collapse", lambda d: d["k617"]["descent_theorem"].__setitem__("pin_candidates_become_identical_after_correction", False))
    add("k617-zero-seed", lambda d: d["k617"]["descent_theorem"].__setitem__("corrected_graph_intersection_K614_zero_seed_rank", 128))
    add("k617-stationary", lambda d: d["k617"]["descent_theorem"].__setitem__("stationary_for_frozen_K438_action", True))
    add("k617-ownership", lambda d: d["k617"]["ownership_reconciliation"].__setitem__("bounded_graph_route_action_owned_by_unrestricted_four_field_action", True))
    add("k617-revival", lambda d: d["k617"]["decision"].__setitem__("moving_graph_revives_bounded_action_owned_route", True))
    add("k618-krylov", lambda d: d["k618"]["action_hull_theorem"].__setitem__("krylov_ranks_A0_through_A4", [128, 256, 512, 512, 512]))
    add("k618-complement", lambda d: d["k618"]["action_hull_theorem"].__setitem__("corrected_carrier_complement_rank", 0))
    add("k618-slow-missing", lambda d: d["k618"]["action_hull_theorem"].__setitem__("slow_incoming_missing_rank", 64))
    add("k618-coupling-owned", lambda d: d["k618"]["ownership_and_typing"].__setitem__("action_derived_vector_split_owns_mixed_hessian_coupling", True))
    add("k618-rank-identity", lambda d: d["k618"]["ownership_and_typing"].__setitem__("equal_rank_identifies_historical_and_current_hulls", True))
    add("k618-route-revived", lambda d: d["k618"]["revival_gate"].__setitem__("corrected_carrier_revives_historical_bounded_graph_as_action_subsystem", True))
    add("k618-k616-retracted", lambda d: d["k618"]["revival_gate"].__setitem__("K616_core_unsplit_packet_obstruction_retracted", True))
    add("k618-packet", lambda d: d["k618"]["decision"].__setitem__("actual_K596_K598_packet_released", True))
    add("k619-seed-intersection", lambda d: d["k619"]["common_module_theorem"].__setitem__("seed_intersection_rank", 128))
    add("k619-depth2", lambda d: d["k619"]["common_module_theorem"].__setitem__("depth_2_intersection_rank", 0))
    add("k619-depth3", lambda d: d["k619"]["common_module_theorem"].__setitem__("depth_3_join_rank", 512))
    add("k619-seed-identity", lambda d: d["k619"]["ownership_reconciliation"].__setitem__("equality_of_generated_subspaces_identifies_seed_maps", True))
    add("k619-stationary", lambda d: d["k619"]["ownership_reconciliation"].__setitem__("common_module_is_stationary_solution_space", True))
    add("k619-packet", lambda d: d["k619"]["decision"].__setitem__("actual_K596_K598_packet_released", True))
    add("k620-fast", lambda d: d["k620"]["module_projector_theorem"].__setitem__("common_module_fast_ranks", [192, 192]))
    add("k620-module-projector", lambda d: d["k620"]["module_projector_theorem"].__setitem__("polynomial_projector_with_image_common_module_exists", True))
    add("k620-complement-projector", lambda d: d["k620"]["module_projector_theorem"].__setitem__("polynomial_projector_with_image_rank128_complement_exists", True))
    add("k620-seed-proportional", lambda d: d["k620"]["seed_adapter_theorem"].__setitem__("corresponding_seed_maps_scalar_proportional_in_any_eigenspace", True))
    add("k620-seed-adapter", lambda d: d["k620"]["seed_adapter_theorem"].__setitem__("scalar_polynomial_p_with_pA_J0_equals_X_exists", True))
    add("k620-commutant-excluded", lambda d: d["k620"]["ownership_reconciliation"].__setitem__("nonpolynomial_action_owned_adapter_excluded", True))
    add("k620-action-selects", lambda d: d["k620"]["decision"].__setitem__("common_module_selected_by_frozen_action", True))

    add("k615-euler-rank", lambda d: d["k615"]["rank_fingerprint"].__setitem__("action_euler_image", 127))
    add("k615-zero-half", lambda d: d["k615"]["rank_fingerprint"].__setitem__("incoming_zero_form", 127))
    add("k615-euler-half", lambda d: d["k615"]["rank_fingerprint"].__setitem__("outgoing_euler", 127))
    add("k615-fast", lambda d: d["k615"]["rank_fingerprint"].__setitem__("fast_euler", 127))
    add("k615-fibre-kernel", lambda d: d["k615"]["fibrewise_stationarity_theorem"].__setitem__("kernel_dimension", 1))
    add("k615-stationary", lambda d: d["k615"]["fibrewise_stationarity_theorem"].__setitem__("nonzero_zero_form_value_is_stationary", True))
    add("k615-domain-kernel", lambda d: d["k615"]["closed_domain_stationarity_theorem"].__setitem__("K440_kernel_dimension", 1))
    add("k615-four-field", lambda d: d["k615"]["closed_domain_stationarity_theorem"].__setitem__("four_source_fermion_slots_direct_sum_kernel_dimension", 1))
    add("k615-scope", lambda d: d["k615"]["closed_domain_stationarity_theorem"].__setitem__("moving_lower_order_or_nonlinear_operator_covered", True))
    add("k615-overclaim", lambda d: d["k615"]["decision"].__setitem__("selected_source_action_rejected", True))
    add("k615-release", lambda d: d["k615"]["decision"].__setitem__("K596_K598_released_by_stationarity", True))

    add("k616-x-rank", lambda d: d["k616"]["input_injectivity"].__setitem__("outgoing_x_rank", 127))
    add("k616-y-rank", lambda d: d["k616"]["input_injectivity"].__setitem__("incoming_y_rank", 127))
    add("k616-components", lambda d: d["k616"]["input_injectivity"].__setitem__("every_nonzero_v_has_all_four_components_nonzero", False))
    add("k616-defect", lambda d: d["k616"]["unsplit_defect_theorem"].__setitem__("rank_for_every_nonzero_v", 1))
    add("k616-pass", lambda d: d["k616"]["unsplit_defect_theorem"].__setitem__("natural_unsplit_packet_satisfies_K596", True))
    add("k616-repair", lambda d: d["k616"]["matching_half_repair"].__setitem__("equals_natural_unsplit_packet", True))
    add("k616-owner", lambda d: d["k616"]["matching_half_repair"].__setitem__("split_is_action_owned", True))
    add("k616-transport", lambda d: d["k616"]["transport_theorem"].__setitem__("rank_preserved", False))
    add("k616-transport-rank", lambda d: d["k616"]["transport_theorem"].__setitem__("rank_at_every_transport_fibre", 0))
    add("k616-scope", lambda d: d["k616"]["transport_theorem"].__setitem__("moving_nonlinear_action_coupling_covered", True))
    add("k616-release", lambda d: d["k616"]["decision"].__setitem__("K596_actual_action_owned_packet_released", True))
    add("k616-action", lambda d: d["k616"]["decision"].__setitem__("selected_source_action_rejected", True))

    add("k614-rank", lambda d: d["k614"]["cross_characteristic_rank_fingerprint"].__setitem__("corrected_image", 127))
    add("k614-fast", lambda d: d["k614"]["cross_characteristic_rank_fingerprint"].__setitem__("fast_projection", 127))
    add("k614-incoming", lambda d: d["k614"]["cross_characteristic_rank_fingerprint"].__setitem__("incoming_projection", 127))
    add("k614-block", lambda d: d["k614"]["cross_characteristic_rank_fingerprint"].__setitem__("slow_incoming_projection", 0))
    add("k614-source", lambda d: d["k614"]["injection_theorem"].__setitem__("source_owned_zero_form_field", False))
    add("k614-carrier", lambda d: d["k614"]["injection_theorem"].__setitem__("image_lies_in_corrected_carrier", False))
    add("k614-half", lambda d: d["k614"]["injection_theorem"].__setitem__("incoming_projection_is_injective", False))
    add("k614-field-value", lambda d: d["k614"]["injection_theorem"].__setitem__("field_space_is_not_a_selected_field_value", False))
    add("k614-background", lambda d: d["k614"]["background_and_riesz_reconciliation"].__setitem__("injection_evaluated_on_active_background_is_zero", False))
    add("k614-current", lambda d: d["k614"]["background_and_riesz_reconciliation"].__setitem__("zero_fermion_current_rank", 1))
    add("k614-stationary", lambda d: d["k614"]["background_and_riesz_reconciliation"].__setitem__("nonzero_fermion_stationary_solution_owned", True))
    add("k614-riesz", lambda d: d["k614"]["background_and_riesz_reconciliation"].__setitem__("K441_action_Riesz_return_for_zero_form_background_owned", True))
    add("k614-release", lambda d: d["k614"]["background_and_riesz_reconciliation"].__setitem__("K596_actual_rank_one_packet_released", True))
    add("k614-decision", lambda d: d["k614"]["decision"].__setitem__("source_owned_zero_form_injection_constructed", False))
    add("k614-overclaim", lambda d: d["k614"]["decision"].__setitem__("actual_action_owned_soldering_constructed", True))

    add("k612-chart", lambda d: d["k612"]["serialized_numeric_custody"].__setitem__("chart_contraction_upper", "1/2"))
    add("k612-inverse", lambda d: d["k612"]["serialized_numeric_custody"].__setitem__("chart_inverse_norm_upper", "2"))
    add("k612-gram", lambda d: d["k612"]["serialized_numeric_custody"].__setitem__("physical_gram_interval", ["1", "1"]))
    add("k612-raw", lambda d: d["k612"]["serialized_numeric_custody"].__setitem__("raw_counterterm_separately_convergent", True))
    for key in ("named_regular_lower_bound_r0", "named_complete_lower_bound_L0", "named_graph_relative_bound_for_complete_cancelled_X", "named_identity_constant_for_complete_cancelled_X", "named_common_domain_for_chart_and_complete_core"):
        add("k612-missing-" + key, lambda d, key=key: d["k612"]["missing_quantitative_custody"].__setitem__(key, True))
    add("k612-distinct", lambda d: d["k612"]["same_interface_countermodels"].__setitem__("floors_are_distinct", False))
    add("k612-uniform", lambda d: d["k612"]["same_interface_countermodels"].__setitem__("no_uniform_floor_follows_from_serialized_interface", False))
    add("k612-row", lambda d: d["k612"]["same_interface_countermodels"]["rows"][0].__setitem__("native_floor", "0"))
    add("k612-family", lambda d: d["k612"]["same_interface_countermodels"].__setitem__("rows", d["k612"]["same_interface_countermodels"]["rows"][:3]))
    for key in ("K139_semiboundedness_retracted", "K462_existential_coercivity_retracted", "K581_noncyclic_inheritance_retracted"):
        add("k612-retract-" + key, lambda d, key=key: d["k612"]["dependency_reconciliation"].__setitem__(key, True))
    add("k612-k611", lambda d: d["k612"]["dependency_reconciliation"].__setitem__("K611_mixed_graph_obstruction_preserved", False))
    add("k612-escape", lambda d: d["k612"]["dependency_reconciliation"].__setitem__("new_cancellation_adapted_estimate_still_live", False))
    add("k612-decision", lambda d: d["k612"]["decision"].__setitem__("K139_constant_extraction_from_current_serialized_custody_rejected", False))
    add("k612-floor", lambda d: d["k612"]["decision"].__setitem__("named_complete_sector_floor_emitted", True))
    add("k612-k473", lambda d: d["k612"]["decision"].__setitem__("K473_released", True))

    add("k613-even", lambda d: d["k613"]["carrier_parity"].__setitem__("all_available_generators_have_even_carrier_parity", False))
    add("k613-contract", lambda d: d["k613"]["carrier_parity"].__setitem__("allowed_contractions_remove_carrier_slots_in_pairs", False))
    add("k613-network", lambda d: d["k613"]["carrier_parity"].__setitem__("homogeneous_tensor_networks_preserve_even_carrier_parity", False))
    add("k613-vector", lambda d: d["k613"]["carrier_parity"].__setitem__("nonzero_natural_vector_or_covector_from_even_inputs", True))
    add("k613-blocks", lambda d: d["k613"]["full_stabilizer_consequence"].__setitem__("spectral_block_ranks", [256, 256]))
    add("k613-minrank", lambda d: d["k613"]["full_stabilizer_consequence"].__setitem__("minimum_nonzero_invariant_endomorphism_rank", 1))
    add("k613-ranks", lambda d: d["k613"]["full_stabilizer_consequence"].__setitem__("possible_invariant_idempotent_ranks", [0, 1, 512]))
    add("k613-rankone", lambda d: d["k613"]["full_stabilizer_consequence"].__setitem__("rank_one_natural_endomorphism_from_current_tensors", True))
    add("k613-scope", lambda d: d["k613"]["full_stabilizer_consequence"].__setitem__("arbitrary_tensor_contraction_stronger_than_K610_factorwise_scope", False))
    add("k613-slot", lambda d: d["k613"]["K594_replay"].__setitem__("one_carrier_slot_component_serialized", True))
    add("k613-background", lambda d: d["k613"]["K594_replay"].__setitem__("odd_carrier_valence_background_contraction_serialized", True))
    add("k613-thirdjet", lambda d: d["k613"]["K594_replay"].__setitem__("existing_third_jet_breaks_central_parity", True))
    add("k613-escape", lambda d: d["k613"]["reopener"].__setitem__("affine_field_dependent_or_odd_action_data_ruled_out", True))
    add("k613-decision-vector", lambda d: d["k613"]["decision"].__setitem__("all_current_homogeneous_tensor_networks_select_vector_or_covector", True))
    add("k613-decision-rank", lambda d: d["k613"]["decision"].__setitem__("all_current_homogeneous_tensor_networks_select_rank_one_packet", True))
    add("k613-release", lambda d: d["k613"]["decision"].__setitem__("K598_released", True))

    caught = 0
    for name, case in mutations:
        failures = audit(case, check_digests=False)
        if failures:
            caught += 1
        else:
            print(f"RED selftest mutation escaped: {name}")
    return caught, len(mutations)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = load_inputs()
    failures = audit(data)
    if failures:
        for failure in failures:
            print(f"RED current_frontier_semantic_currency: {failure}")
        return 1
    print("PASS current_frontier_semantic_currency: live/history/owner facts")
    if args.selftest:
        caught, total = selftest(data)
        print(f"PASS hostile mutations caught: {caught}/{total}")
        return 0 if caught == total else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
