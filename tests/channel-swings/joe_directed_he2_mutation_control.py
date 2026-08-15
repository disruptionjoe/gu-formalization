#!/usr/bin/env python3
"""HE-2 mutation control: prove the HE-2 probe's failure path is live.

A probe nobody has seen fail is unverified.  This script takes the HE-2 reality
probe, injects one targeted defect at a time into its MACHINERY (not into its
conclusions), runs the mutant, and requires each mutant to exit NON-ZERO.

Four mutations, each aimed at a different load-bearing organ:

  M1  predeclared reality table          -- proves Part 1 computes the reality
                                            type rather than echoing (p-q) mod 8
  M2  index raising in the gamma-trace   -- proves the (6,4) metric is actually
                                            load-bearing in Leg A's intertwiner
  M3  charge-conjugation-style B word    -- proves the antilinear intertwiner is
                                            solved for, not postulated
  M4  chirality labelling convention     -- proves the mod-4 / weight bookkeeping
                                            is tied to the operator, not to a name

Run from the repository root:
    _local/cas-venv/bin/python tests/channel-swings/joe_directed_he2_mutation_control.py
"""
from __future__ import annotations

import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
TARGET = HERE / "joe_directed_he2_real_form_reality_probe.py"
SRC = TARGET.read_text()

MUTATIONS = [
    (
        "M1 predeclared reality table: assert Cl(6,4) is REAL",
        '{0: "REAL", 2: "COMPLEX", 4: "QUATERNIONIC", 6: "COMPLEX"}[r]',
        '{0: "REAL", 2: "REAL", 4: "QUATERNIONIC", 6: "COMPLEX"}[r]',
    ),
    (
        "M2 gamma-trace: drop the (6,4) index raising eta^{aa}",
        "ga = CL64.gam[a].scaled(CL64.eta[a])",
        "ga = CL64.gam[a].scaled(1)",
    ),
    (
        "M3 antilinear intertwiner: truncate the B word to one gamma",
        "            for a in subset:\n                B = B @ self.gam[a]",
        "            for a in subset[:1]:\n                B = B @ self.gam[a]",
    ),
    (
        "M4 chirality labelling: flip the compact chirality operator's sign",
        "CHI_INT = prod_G.scaled(0, -1)",
        "CHI_INT = prod_G.scaled(0, 1)",
    ),
]

results = []
tmpdir = pathlib.Path(tempfile.mkdtemp(prefix="he2-mutation-"))
for name, old, new in MUTATIONS:
    if old not in SRC:
        print(f"  ERROR  mutation anchor not found for {name}")
        results.append((name, None))
        continue
    mutant = SRC.replace(old, new, 1)
    path = tmpdir / f"mutant_{len(results)}.py"
    path.write_text(mutant)
    proc = subprocess.run([sys.executable, str(path)], capture_output=True, text=True)
    died = proc.returncode != 0
    results.append((name, died))
    print(f"  {'DIED (good)' if died else 'SURVIVED (BAD)'}  {name}   "
          f"exit={proc.returncode}")

print()
alive = [n for n, d in results if d is not True]
if alive:
    print(f"FAILURE PATH NOT VERIFIED: {len(alive)} mutant(s) survived or errored")
    for n in alive:
        print(f"  - {n}")
    raise SystemExit(1)
print(f"failure path verified: {len(results)}/{len(results)} mutants died")
raise SystemExit(0)
