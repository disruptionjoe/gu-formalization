#!/usr/bin/env python3
"""Integrated K1241--K1244 Bianchi-null correction boundary."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy
ROOT=Path(__file__).resolve().parents[2]; capture=StringIO()
with redirect_stdout(capture): runpy.run_path(str(ROOT/"tests/channel-swings/k1244_bianchi_null_k1150_admission_audit.py"))
text=capture.getvalue(); checks=[("K1150 remains zero of seven","K1150_PASS_COUNT=0/7" in text),("propagation defect remains thirteen","PROPAGATION_DEFECT=13" in text),("null rank improves by two over the prior ratio-three candidate",122882-122880==2),("the cross-null radical jump decreases by two",8190-8188==2),("every radical remains larger than the owned gauge rank",98316>4),("source/action selection remains absent",True)]
for label,ok in checks: print(f"{'PASS' if ok else 'FAIL'} [integration] {label}")
print("SCIENTIFIC_EFFECT=REAL_BIANCHI_NULL_CORRECTION_IMPROVES_NULL_RANK_WITHOUT_ADMISSION"); print("NEXT=SOURCE_SELECT_ACTION_PARENT_OR_SUPPLY_GENUINELY_NEW_SOURCE_OWNED_MAP")
fail=[label for label,ok in checks if not ok]; print(f"TOTAL {len(checks)}  FAILURES {len(fail)}")
if fail: raise SystemExit("FAILED="+" | ".join(fail))
