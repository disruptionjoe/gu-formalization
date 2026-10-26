"""Dependency consistency only; independent mathematical controls are in probe."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/"lab/process/k2088-even-ground-selection.json").read_text())
 for p,h in d['inputs'].items():
  assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'changed dependency '+p
 print('PASS dependency pins; not mathematical proof')
if __name__=='__main__':main()
