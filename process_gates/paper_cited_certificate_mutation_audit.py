#!/usr/bin/env python3
"""Mutation custody for the three frozen certificates cited by the lead paper.

The manifest stores exact, claim-breaking source substitutions. The gate first
requires every unmodified certificate to pass, then applies each substitution
exactly once in an isolated temporary file and requires the mutant to exit
nonzero. It changes no scientific verdict; it proves only that the named
certificate contracts have live failure paths for these planted faults.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
TIMEOUT_SECONDS = 90


@dataclass(frozen=True)
class Mutation:
    certificate: str
    name: str
    old: str
    new: str


MUTATIONS = (
    Mutation(
        "tests/generation-sector/ghost_parity_krein.py",
        "anti_self_dual_triplet_substitution",
        "SD = [(0, 1, 2, 3, 1), (0, 2, 3, 1, 1), (0, 3, 1, 2, 1)]",
        "SD = [(0, 1, 2, 3, -1), (0, 2, 3, 1, -1), (0, 3, 1, 2, -1)]",
    ),
    Mutation(
        "tests/generation-sector/ghost_parity_krein.py",
        "identity_ambient_metric_substitution",
        "etaV = np.diag(metric_signs).astype(complex)",
        "etaV = I14.copy()",
    ),
    Mutation(
        "tests/generation-sector/ghost_parity_krein.py",
        "positive_definite_full_form_substitution",
        "K = np.kron(etaV, bS)",
        "K = np.eye(N * DIM, dtype=complex)",
    ),
    Mutation(
        "tests/generation-sector/net_chiral_index_invariant.py",
        "cross_form_replaced_by_aligned_form",
        "Kcross = np.block([[np.zeros((n, n)), B], [B.conj().T, np.zeros((n, n))]])",
        "Kcross = np.diag(np.concatenate([np.ones(n), -np.ones(n)])).astype(complex)",
    ),
    Mutation(
        "tests/generation-sector/net_chiral_index_invariant.py",
        "non_isometric_flow_generator",
        "X = np.linalg.solve(K, S)          # X = K^{-1} S  =>  X^dag K + K X = 0",
        "X = S                             # planted non-isometric generator",
    ),
    Mutation(
        "tests/generation-sector/net_chiral_index_invariant.py",
        "aligned_control_replaced_by_cross_form",
        "Kalign = np.diag(np.concatenate([np.ones(n), -np.ones(n)])).astype(complex)",
        "Kalign = Kcross.copy()",
    ),
    Mutation(
        "tests/generation-sector/t1a_kinematic_chirality_kill.py",
        "krein_restriction_replaced_by_identity",
        "Kt = Wt.conj().T @ K @ Wt; Kt = 0.5 * (Kt + Kt.conj().T)",
        "Kt = np.eye(Wt.shape[1], dtype=complex)",
    ),
    Mutation(
        "tests/generation-sector/t1a_kinematic_chirality_kill.py",
        "chirality_restriction_replaced_by_identity",
        "Ct = Wt.conj().T @ chir @ Wt; Ct = 0.5 * (Ct + Ct.conj().T)",
        "Ct = np.eye(Wt.shape[1], dtype=complex)",
    ),
    Mutation(
        "tests/generation-sector/t1a_kinematic_chirality_kill.py",
        "physical_subspace_forced_to_positive_chirality",
        "kev, kU = np.linalg.eigh(Kt); phys = kU[:, kev > 1e-9]",
        "kev, kU = np.linalg.eigh(Kt); phys = Pp",
    ),
)


def run(path: Path) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.run(
        [sys.executable, str(path)],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        timeout=TIMEOUT_SECONDS,
        check=False,
    )


def main() -> int:
    certificates = tuple(dict.fromkeys(m.certificate for m in MUTATIONS))
    for rel in certificates:
        result = run(ROOT / rel)
        if result.returncode != 0:
            print(f"[FAIL] baseline certificate is red: {rel}")
            print((result.stdout + result.stderr)[-2000:])
            return 1
        print(f"[PASS] baseline: {rel}")

    failures = []
    with tempfile.TemporaryDirectory(prefix="gu-paper-mutations-") as tmp:
        tmp_root = Path(tmp)
        for index, mutation in enumerate(MUTATIONS, start=1):
            source = (ROOT / mutation.certificate).read_text(encoding="utf-8")
            count = source.count(mutation.old)
            if count != 1:
                failures.append(
                    f"{mutation.name}: expected one source match, found {count}"
                )
                continue
            mutant = source.replace(mutation.old, mutation.new, 1)
            mutant_path = tmp_root / f"{index:02d}-{Path(mutation.certificate).name}"
            mutant_path.write_text(mutant, encoding="utf-8")
            try:
                result = run(mutant_path)
            except subprocess.TimeoutExpired:
                failures.append(f"{mutation.name}: timed out instead of failing")
                continue
            if result.returncode == 0:
                failures.append(f"{mutation.name}: mutant exited zero")
            else:
                print(f"[PASS] mutant rejected: {mutation.name}")

    if failures:
        for failure in failures:
            print(f"[FAIL] {failure}")
        print(f"RED: {len(failures)}/{len(MUTATIONS)} mutation contracts failed")
        return 1
    print(
        f"GREEN: {len(certificates)}/{len(certificates)} baselines pass; "
        f"{len(MUTATIONS)}/{len(MUTATIONS)} claim-breaking mutants exit nonzero"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
