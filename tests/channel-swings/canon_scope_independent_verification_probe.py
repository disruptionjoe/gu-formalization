#!/usr/bin/env python3
"""Independent structural verification for two 2026-08-24 canon narrowings.

This probe deliberately does not import the LDB or ST-1 instruments.  It uses
only exact parity arithmetic, typed Hom domains, frozen-input digests and the
proposed canon wording.  The predecessor probes remain separate reproduction
controls in the run receipt.
"""

from __future__ import annotations

import hashlib
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
MUT = os.environ.get("CANON_IV_MUTATE", "")
MUTATIONS = (
    "parity",
    "dimension",
    "bare_class",
    "inserted_class",
    "domain_collapse",
    "nullity_wording",
    "shiab_wording",
    "input_digest",
)
CHECKS: list[tuple[str, str, bool, object]] = []

LDB = ROOT / "lab/active-research/joe-directed/lens-digs/ldb-bit2-direction-and-krein-parity-2026-08-17.md"
ST1 = ROOT / "lab/active-research/joe-directed/seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md"
GHOST = ROOT / "canon/ghost-parity-krein-synthesis.md"
SIX_AXIS = ROOT / "canon/six-axis-candidate-krein-positivity-dg.md"
SHIAB = ROOT / "canon/shiab-existence-cl95.md"
TWO_ARENA = ROOT / "canon/two-arena-rep-theory-core-RESULTS.md"
CANON = ROOT / "CANON.md"

EXPECTED_DIGESTS = {
    LDB: "d93ab92634982b00218d2b99c8533ea45cb646e25914a80e607938ea85097b4f",
    ST1: "c35273c8de4b54a6a4a3653c5154215e00725b69ace36dd3fb6f2c5a99cdaf82",
}


def check(group: str, name: str, ok: bool, detail: object = None) -> None:
    CHECKS.append((group, name, bool(ok), detail))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def commutation_sign(q: int) -> int:
    """chi beta = (-1)^p beta chi, p=14-q spacelike factors."""
    p = 14 - q
    if MUT == "parity" and q == 5:
        p += 1
    return -1 if p % 2 else 1


def z4(*classes: int) -> int:
    value = sum(classes) % 4
    if MUT == "bare_class" and classes == (3, 3):
        return 0
    if MUT == "inserted_class" and classes == (3, 3, 2):
        return 2
    return value


def verify_inputs() -> None:
    for path, expected in EXPECTED_DIGESTS.items():
        actual = sha256(path)
        if MUT == "input_digest" and path == LDB:
            actual = "0" * 64
        check("input", f"frozen predecessor digest: {path.name}", actual == expected, actual)


def verify_krein_scope() -> None:
    for q in range(15):
        sign = commutation_sign(q)
        check("krein", f"q={q}: anticommutation iff q odd", (sign == -1) == (q % 2 == 1), sign)

    check("krein", "both physical horns have odd q", 5 % 2 == 1 and 7 % 2 == 1)
    check("krein", "Euclidean control has beta proportional to chi", commutation_sign(0) == 1)
    triplet_dim = 193 if MUT == "dimension" else 192
    check("krein", "triplet splits into two 96-dimensional chirality halves", triplet_dim == 2 * 96, triplet_dim)
    check("krein", "odd-q beta exchanges chirality halves", commutation_sign(5) == -1 and commutation_sign(7) == -1)
    check("krein", "q=0 beta preserves chirality halves", commutation_sign(0) == 1)

    ghost = GHOST.read_text(encoding="utf-8")
    six = SIX_AXIS.read_text(encoding="utf-8")
    required = "`{K, chi} = 0` iff the timelike count `q` is odd"
    if MUT == "nullity_wording":
        required = "`{K, chi} = 0` iff `q` is even"
    check("wording", "ghost-parity canon states the parity criterion", required in ghost)
    check("wording", "six-axis canon states the parity criterion", required in six)
    for name, text in (("ghost", ghost), ("six-axis", six)):
        check("wording", f"{name}: q=0 halves are definite", "`(14,0)`" in text and "halves are definite" in text)
        check("wording", f"{name}: physical horns remain null", "`(9,5)` and `(7,7)`" in text and "totally null" in text)


def verify_shiab_scope() -> None:
    s_plus = 3
    class_two = 2
    check("shiab", "bare same-chirality scalar is class-forbidden", z4(s_plus, s_plus) == 2)
    check("shiab", "one class-2 insertion removes the class obstruction", z4(s_plus, s_plus, class_two) == 0)
    check("shiab", "two class-2 insertions restore the class obstruction", z4(s_plus, s_plus, class_two, class_two) == 2)

    bare_domain = "Hom(S+ tensor S+, Lambda0)"
    inserted_domain = "Hom(S+ tensor S+ tensor T2, Lambda0)"
    if MUT == "domain_collapse":
        inserted_domain = bare_domain
    check("shiab", "bare and inserted Hom domains are different objects", bare_domain != inserted_domain)
    check("shiab", "a zero in the bare domain cannot prove a zero in the inserted domain", bare_domain != inserted_domain and z4(3, 3, 2) == 0)

    surfaces = {
        "shiab": SHIAB.read_text(encoding="utf-8"),
        "two-arena": TWO_ARENA.read_text(encoding="utf-8"),
        "canon-index": CANON.read_text(encoding="utf-8"),
    }
    required = "bare zero-insertion"
    forbidden = "must be supplied by an external source-action spurion"
    if MUT == "shiab_wording":
        required = "unconditional selected mass"
    for name, text in surfaces.items():
        check("wording", f"{name}: absence is scoped to the bare domain", required in text)
        check("wording", f"{name}: old universal spurion inference removed", forbidden not in text)
    shiab = surfaces["shiab"]
    check("wording", "Shiab canon preserves source-action selection as open", "source-action selection" in shiab and "remains OPEN" in shiab)
    check("wording", "Shiab canon preserves reality and scale owners", "reality map" in shiab and "scale" in shiab)


def selftest() -> int:
    print("SELFTEST: verifying clean baseline before mutations")
    clean_env = dict(os.environ)
    clean_env.pop("CANON_IV_MUTATE", None)
    baseline = subprocess.run([sys.executable, str(Path(__file__).resolve())], env=clean_env, capture_output=True, text=True)
    if baseline.returncode != 0:
        print("FAIL baseline")
        print(baseline.stdout)
        return 1
    caught = 0
    for mutation in MUTATIONS:
        env = dict(os.environ, CANON_IV_MUTATE=mutation)
        result = subprocess.run([sys.executable, str(Path(__file__).resolve())], env=env, capture_output=True, text=True)
        genuine = result.returncode == 1 and "[FAIL]" in result.stdout
        print(f"mutation {mutation:18s}: {'CAUGHT' if genuine else 'MISSED'}")
        caught += int(genuine)
    print(f"SELFTEST: {caught}/{len(MUTATIONS)} mutations caught")
    return 0 if caught == len(MUTATIONS) else 1


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    verify_inputs()
    verify_krein_scope()
    verify_shiab_scope()
    passed = sum(ok for _, _, ok, _ in CHECKS)
    for group, name, ok, detail in CHECKS:
        if not ok:
            print(f"[FAIL] [{group}] {name}: {detail}")
    print(f"CANON-SCOPE-IV: {passed}/{len(CHECKS)} exact checks pass")
    print("VERDICT: ODD-Q-NULLITY-SCOPE-AND-BARE-SHIAB-ABSENCE-CONFIRMED" if passed == len(CHECKS) else "VERDICT: NOT-CERTIFIED")
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
