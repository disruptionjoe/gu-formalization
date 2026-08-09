#!/usr/bin/env python3
"""Versioned exact K77 carrier and sparse coefficient-bank consumer API.

Importing this module never executes a predecessor probe.  ``load_bank``
verifies the canonical payload hash and every recorded source/dependency hash
before returning exact ``Fraction`` columns.  The small carrier implementation
supports bounded direct epsilon-cell replay without the historical Run chain.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BANK = ROOT / "tests/fixtures/k77_exact_coefficient_bank_v1.json"
G = tuple[Fraction, Fraction]
ZERO: G = (Fraction(0), Fraction(0))
ONE: G = (Fraction(1), Fraction(0))
I: G = (Fraction(0), Fraction(1))
Element = dict[int, G]
Form = dict[int, Element]


class BankIntegrityError(RuntimeError):
    pass


def strict_load(path: Path) -> dict:
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise BankIntegrityError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def canonical(payload: dict) -> bytes:
    return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()


def payload_hash(payload: dict) -> str:
    unsigned = dict(payload)
    unsigned.pop("construction_hash", None)
    return sha256(canonical(unsigned)).hexdigest()


def file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def q(value) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, (list, tuple)) and len(value) == 2:
        return Fraction(int(value[0]), int(value[1]))
    raise TypeError(value)


def gz(value) -> G:
    return q(value), Fraction(0)


def gadd(left: G, right: G) -> G:
    return left[0] + right[0], left[1] + right[1]


def gmul(left: G, right: G) -> G:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gscale(scalar, value: G) -> G:
    scalar = q(scalar)
    return scalar * value[0], scalar * value[1]


@dataclass(frozen=True)
class ExactBank:
    payload: dict
    path: Path

    @property
    def signature(self) -> tuple[int, ...]:
        return tuple(self.payload["carrier"]["signature_diagonal"])

    @property
    def channels(self) -> tuple[str, str, str]:
        return tuple(self.payload["carrier"]["selected_shiab_channels"])

    @property
    def receiver_labels(self) -> tuple[dict, ...]:
        return tuple(self.payload["receivers"]["labels"])

    def causal_covector(self, name: str) -> tuple[Fraction, ...]:
        return tuple(q(value) for value in self.payload["causal_covectors"][name])

    def column(self, causal: str, kind: str, index: int, component: str) -> dict[int, Fraction]:
        if component not in self.payload["coefficient_basis"]:
            raise KeyError(component)
        matches = [
            item for item in self.payload["columns"][causal]
            if item["kind"] == kind and item["index"] == index
        ]
        if len(matches) != 1:
            raise KeyError((causal, kind, index))
        return {int(row): Fraction(int(num), int(den)) for row, num, den in matches[0][component]}

    def receiver(self, row: int) -> Form:
        label = self.receiver_labels[row]
        real, imag = label["coefficient"]
        return {
            int(label["form_mask"]): {
                int(label["clifford_mask"]): (q(real), q(imag))
            }
        }

    def direct_epsilon_polynomial(self, causal: str, column: int, row: int) -> tuple[Fraction, Fraction, Fraction]:
        core = K77Core(self.signature, self.channels)
        pair = tuple(self.payload["carrier"]["epsilon_generators"][column])
        chi = core.blade(pair)
        u: Form = {}
        for mu, coefficient in enumerate(self.causal_covector(causal)):
            if coefficient:
                u = core.fadd(u, {1 << mu: core.escale(-coefficient, chi)})
        u_b = core.fscale(-1, u)
        u_t = u
        receiver = self.receiver(row)
        z0 = core.fixed_operator_hessian({}, {}, u_b, u_t, receiver)
        zb = core.gsub(core.fixed_operator_hessian(core.phi1, {}, u_b, u_t, receiver), z0)
        zt = core.gsub(core.fixed_operator_hessian({}, core.phi1, u_b, u_t, receiver), z0)
        if any(value[1] for value in (z0, zb, zt)):
            raise BankIntegrityError("real K77 replay acquired imaginary coefficient")
        return z0[0], zb[0], zt[0]


def load_bank(path: Path = DEFAULT_BANK, verify_dependencies: bool = True) -> ExactBank:
    path = path.resolve()
    payload = strict_load(path)
    if payload.get("schema_version") != "1.0":
        raise BankIntegrityError("unsupported schema")
    if payload_hash(payload) != payload.get("construction_hash"):
        raise BankIntegrityError("construction hash mismatch")
    if verify_dependencies:
        for relative, expected in payload["dependency_hashes"].items():
            dependency = ROOT / relative
            if not dependency.is_file() or file_hash(dependency) != expected:
                raise BankIntegrityError(f"stale dependency: {relative}")
    carrier = payload["carrier"]
    receivers = payload["receivers"]
    if carrier["dimension"] != 14 or tuple(carrier["signature_diagonal"]).count(1) != 7:
        raise BankIntegrityError("carrier is not K77")
    if len(carrier["epsilon_generators"]) != 91:
        raise BankIntegrityError("epsilon generator count")
    if receivers["dimension"] != 1274 or len(receivers["labels"]) != 1274:
        raise BankIntegrityError("receiver dimension")
    if len(receivers["horizontal_rows"]) != 24 or len(receivers["offslice_rows"]) != 1250:
        raise BankIntegrityError("receiver split")
    for causal in ("timelike", "spacelike", "null"):
        columns = payload["columns"].get(causal, [])
        if sum(item["kind"] == "metric" for item in columns) != 10:
            raise BankIntegrityError(f"metric count: {causal}")
        if sum(item["kind"] == "epsilon" for item in columns) != 91:
            raise BankIntegrityError(f"epsilon count: {causal}")
        for item in columns:
            for component in payload["coefficient_basis"]:
                if any(int(den) == 0 for _, _, den in item[component]):
                    raise BankIntegrityError("zero denominator")
    return ExactBank(payload, path)


class K77Core:
    """Small exact real-form carrier used only for bounded direct replay."""

    def __init__(self, signature: tuple[int, ...], channels: tuple[str, str, str]):
        if len(signature) != 14 or (signature.count(1), signature.count(-1)) != (7, 7):
            raise BankIntegrityError("expected signature (7,7)")
        self.n = 14
        self.eta = signature
        self.full = (1 << self.n) - 1
        self.channels = channels
        self.phi1 = {1 << index: self.blade(index) for index in range(self.n)}
        self.phi2 = self.fscale(Fraction(1, 2), self.wedge_raw(self.phi1, self.phi1))

    def indices(self, mask: int) -> tuple[int, ...]:
        return tuple(index for index in range(self.n) if mask & (1 << index))

    def eclean(self, value: Element) -> Element:
        return {mask: coefficient for mask, coefficient in value.items() if coefficient != ZERO}

    def eadd(self, *values: Element) -> Element:
        out: Element = {}
        for value in values:
            for mask, coefficient in value.items():
                out[mask] = gadd(out.get(mask, ZERO), coefficient)
        return self.eclean(out)

    def escale(self, scalar, value: Element) -> Element:
        gaussian = scalar if isinstance(scalar, tuple) else gz(scalar)
        return self.eclean({mask: gmul(gaussian, coefficient) for mask, coefficient in value.items()})

    def blade_product(self, left: int, right: int) -> tuple[int, int]:
        inversions = sum(1 for i in self.indices(left) for j in self.indices(right) if i > j)
        sign = -1 if inversions % 2 else 1
        for index in self.indices(left & right):
            sign *= self.eta[index]
        return left ^ right, sign

    def emul(self, left: Element, right: Element) -> Element:
        out: Element = {}
        for lm, lc in left.items():
            for rm, rc in right.items():
                mask, sign = self.blade_product(lm, rm)
                out[mask] = gadd(out.get(mask, ZERO), gscale(sign, gmul(lc, rc)))
        return self.eclean(out)

    def blade(self, item: int | tuple[int, ...], coefficient: G = ONE) -> Element:
        if isinstance(item, int):
            item = (item,)
        return {sum(1 << index for index in item): coefficient}

    def fclean(self, value: Form) -> Form:
        return {mask: self.eclean(coefficient) for mask, coefficient in value.items() if self.eclean(coefficient)}

    def fadd(self, *values: Form) -> Form:
        out: Form = {}
        for value in values:
            for mask, coefficient in value.items():
                out[mask] = self.eadd(out.get(mask, {}), coefficient)
        return self.fclean(out)

    def fscale(self, scalar, value: Form) -> Form:
        return self.fclean({mask: self.escale(scalar, coefficient) for mask, coefficient in value.items()})

    def wedge_sign(self, left: int, right: int) -> int:
        if left & right:
            return 0
        inversions = sum(1 for i in self.indices(left) for j in self.indices(right) if i > j)
        return -1 if inversions % 2 else 1

    def coefficient_product(self, left: Element, right: Element, channel: str) -> Element:
        xy, yx = self.emul(left, right), self.emul(right, left)
        if channel == "comm":
            return self.eadd(xy, self.escale(-1, yx))
        if channel == "symi":
            return self.escale(I, self.eadd(xy, yx))
        raise ValueError(channel)

    def wedge(self, left: Form, right: Form, channel: str) -> Form:
        out: Form = {}
        for lm, lc in left.items():
            for rm, rc in right.items():
                sign = self.wedge_sign(lm, rm)
                if not sign:
                    continue
                out[lm | rm] = self.eadd(
                    out.get(lm | rm, {}),
                    self.escale(sign, self.coefficient_product(lc, rc, channel)),
                )
        return self.fclean(out)

    def wedge_raw(self, left: Form, right: Form) -> Form:
        out: Form = {}
        for lm, lc in left.items():
            for rm, rc in right.items():
                sign = self.wedge_sign(lm, rm)
                if not sign:
                    continue
                out[lm | rm] = self.eadd(
                    out.get(lm | rm, {}), self.escale(sign, self.emul(lc, rc))
                )
        return self.fclean(out)

    def hodge(self, value: Form) -> Form:
        out: Form = {}
        for mask, coefficient in value.items():
            complement = self.full ^ mask
            norm = 1
            for index in self.indices(mask):
                norm *= self.eta[index]
            out[complement] = self.eadd(
                out.get(complement, {}), self.escale(self.wedge_sign(mask, complement) * norm, coefficient)
            )
        return self.fclean(out)

    def shiab(self, curvature: Form) -> Form:
        first_channel, inner_channel, outer_channel = self.channels
        star = self.hodge(curvature)
        first = self.wedge(self.phi1, star, first_channel)
        middle = self.hodge(self.wedge(self.phi2, star, inner_channel))
        second = self.hodge(self.wedge(self.phi1, middle, outer_channel))
        return self.fadd(first, self.fscale(Fraction(-1, 2), second))

    def pair(self, left: Form, right: Form) -> G:
        return self.wedge_raw(left, right).get(self.full, {}).get(0, ZERO)

    def delta_packet(self, b_field: Form, t_field: Form, u_b: Form, u_t: Form) -> Form:
        return self.fadd(
            self.wedge_raw(u_b, b_field), self.wedge_raw(b_field, u_b),
            self.fscale(Fraction(1, 2), self.fadd(
                self.wedge_raw(u_b, t_field), self.wedge_raw(b_field, u_t),
                self.wedge_raw(u_t, b_field), self.wedge_raw(t_field, u_b))),
            self.fscale(Fraction(1, 3), self.fadd(
                self.wedge_raw(u_t, t_field), self.wedge_raw(t_field, u_t))),
        )

    def first_packet_variation(self, b_field: Form, t_field: Form, receiver: Form) -> Form:
        return self.fadd(
            self.fscale(Fraction(1, 2), self.fadd(
                self.wedge_raw(b_field, receiver), self.wedge_raw(receiver, b_field))),
            self.fscale(Fraction(1, 3), self.fadd(
                self.wedge_raw(receiver, t_field), self.wedge_raw(t_field, receiver))),
        )

    def mixed_packet_variation(self, u_b: Form, u_t: Form, receiver: Form) -> Form:
        return self.fadd(
            self.fscale(Fraction(1, 2), self.fadd(
                self.wedge_raw(u_b, receiver), self.wedge_raw(receiver, u_b))),
            self.fscale(Fraction(1, 3), self.fadd(
                self.wedge_raw(receiver, u_t), self.wedge_raw(u_t, receiver))),
        )

    def fixed_operator_hessian(self, b_field: Form, t_field: Form, u_b: Form, u_t: Form, receiver: Form) -> G:
        return gadd(
            gadd(
                self.pair(receiver, self.shiab(self.delta_packet(b_field, t_field, u_b, u_t))),
                self.pair(u_t, self.shiab(self.first_packet_variation(b_field, t_field, receiver))),
            ),
            gadd(
                self.pair(t_field, self.shiab(self.mixed_packet_variation(u_b, u_t, receiver))),
                gscale(Fraction(1, 2), gadd(
                    self.pair(receiver, self.hodge(u_t)),
                    self.pair(u_t, self.hodge(receiver)),
                )),
            ),
        )

    @staticmethod
    def gsub(left: G, right: G) -> G:
        return left[0] - right[0], left[1] - right[1]
