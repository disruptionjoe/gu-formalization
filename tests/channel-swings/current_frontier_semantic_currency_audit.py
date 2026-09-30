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
        "dispositions": json.loads(
            (ROOT / basis["phenomenology_disposition_register"]["path"]).read_text()
        ),
        "b2": json.loads((ROOT / basis["b2_frontier"]["path"]).read_text()),
        "qualification": json.loads(
            (ROOT / basis["w154_w229_qualification"]["path"]).read_text()
        ),
        "b5_artifact": (ROOT / registry["b5_agenda_currency"]["result_ref"]).read_text(),
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
    if isinstance(live, str):
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
              "twelve" in live and "thirty" in live and "alpha,delta" in live,
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
        check("25/9" in live, "live residual target missing")
        check("shifted-form residual or spectral-error bound" in live,
              "live K152 claim ceiling missing")
        for marker in surface["stale_live_markers_forbidden"]:
            check(marker not in live, f"stale marker remains live: {marker}")
    if isinstance(history, str):
        check("25 terminal rows and 66 open rows" in history, "historical 25/66 condition lost")
        check("b2_selectable=false" in history, "historical B2 gate condition lost")
    summary = current.get("current_result", {}).get("summary", "")
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
