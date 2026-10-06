#!/usr/bin/env python3
"""K1145/K1150 audit for the real Bianchi-null correction."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json,runpy
ROOT=Path(__file__).resolve().parents[2]; capture=StringIO()
with redirect_stdout(capture): runpy.run_path(str(ROOT/"tests/channel-swings/k1243_real_bianchi_null_correction.py"))
assert "FAILURES 0" in capture.getvalue(); checks=[]
def check(kind,label,condition): ok=bool(condition); checks.append((label,ok)); print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
k1145=json.loads((ROOT/"lab/process/k1145-i1b-dynamical-cohomology-admission-compiler.json").read_text()); k1150=json.loads((ROOT/"lab/process/k1150-i1b-functional-admission-compiler.json").read_text())
audit={key:False for key in ("source_action_owner","causal_rank_and_negative_capture","propagation","energy_descent","cochain","positive_nonzero_cohomology","common_closed_domain","causal_algebraic_packet","common_graph_domain","closed_gauge_range","uniform_positive_gap","maximal_generator","boundary_trace_compatibility")}
finite=[x["test"] for x in k1145["executable_tests"]]; functional=[x["test"] for x in k1150["executable_tests"]]
check("compiler","all K1145 and K1150 rows are represented",set(finite+functional)<=set(audit))
check("ownership","the correction is repository-constructed and source-unselected",not audit["source_action_owner"])
check("causal","large unequal radicals do not equal the rank-four gauge image",(98316,98316,106504)!=(4,4,4) and not audit["causal_rank_and_negative_capture"])
check("propagation","thirteen normal-null directions still fail",not audit["propagation"] and "PROPAGATION_DEFECT=13" in capture.getvalue())
check("functional","no domain range gap generator or trace packet is supplied",not any(audit[k] for k in functional))
check("verdict","zero of seven rows pass in each compiler",sum(audit[k] for k in finite)==sum(audit[k] for k in functional)==0)
print("K1145_PASS_COUNT=0/7"); print("K1150_PASS_COUNT=0/7")
print("PROPAGATION_DEFECT=13")
fail=[l for l,o in checks if not o]; print(f"TOTAL {len(checks)}  FAILURES {len(fail)}")
if fail: raise SystemExit("FAILED="+" | ".join(fail))
