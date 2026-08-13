#!/usr/bin/env python3
"""Dependency-hashed nonrecursive consumer for the rank-594 tangent bank."""

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BANK = ROOT / "tests/fixtures/k77_minimal_tangent_bank_v1.json"
Q2_ZERO = (Fraction(0), Fraction(0))


class TangentBankIntegrityError(RuntimeError):
    pass


def canonical(payload: dict) -> bytes:
    return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()


def strict_load(path: Path) -> dict:
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise TangentBankIntegrityError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def payload_hash(payload: dict) -> str:
    unsigned = dict(payload)
    unsigned.pop("construction_hash", None)
    return sha256(canonical(unsigned)).hexdigest()


@dataclass(frozen=True)
class TangentBank:
    payload: dict
    path: Path

    @property
    def signature(self):
        return tuple(self.payload["ambient"]["signature_diagonal"])

    @property
    def offslice_rows(self):
        return tuple(self.payload["ambient"]["offslice_global_rows"])

    @property
    def rank(self):
        return int(self.payload["tangent"]["rank"])

    def vectors(self):
        out = []
        for item in self.payload["tangent"]["vectors"]:
            vector = {}
            for row, rn, rd, sn, sd in item["entries"]:
                value = (Fraction(rn, rd), Fraction(sn, sd))
                if value != Q2_ZERO:
                    vector[int(row)] = value
            out.append(vector)
        return tuple(out)


def load_bank(path: Path = DEFAULT_BANK, verify_dependencies: bool = True) -> TangentBank:
    path = path.resolve()
    payload = strict_load(path)
    if payload.get("schema_version") != "1.0":
        raise TangentBankIntegrityError("unsupported schema")
    if payload_hash(payload) != payload.get("construction_hash"):
        raise TangentBankIntegrityError("construction hash mismatch")
    if verify_dependencies:
        for relative, expected in payload["dependency_hashes"].items():
            dependency = ROOT / relative
            if not dependency.is_file() or sha256(dependency.read_bytes()).hexdigest() != expected:
                raise TangentBankIntegrityError(f"stale dependency: {relative}")
    if payload["coefficient_field"] != "QQ(sqrt(3))":
        raise TangentBankIntegrityError("wrong coefficient field")
    if payload["ambient"]["dimension"] != 1250:
        raise TangentBankIntegrityError("wrong ambient dimension")
    if payload["tangent"]["rank"] != 594 or len(payload["tangent"]["vectors"]) != 594:
        raise TangentBankIntegrityError("wrong tangent rank")
    pivots = [int(item["pivot"]) for item in payload["tangent"]["vectors"]]
    if pivots != sorted(set(pivots)):
        raise TangentBankIntegrityError("pivots are not canonical and unique")
    if sum(len(item["entries"]) for item in payload["tangent"]["vectors"]) != payload["tangent"]["nnz"]:
        raise TangentBankIntegrityError("nnz mismatch")
    return TangentBank(payload, path)
