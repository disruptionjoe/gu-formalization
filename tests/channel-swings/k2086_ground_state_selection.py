"""Reproduce typed constants and pin dependencies; reporting check, not proof."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k2086-ground-state-selection.json').read_text())
 for p,h in d['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'input changed'
 assert d['constants']=={'paired_probability': '2*nu-nu**2', 'covariance_bound': '1/3', 'temperature_exponential': 249999, 'paired_budget': '1/62500'}, 'constant inventory'
 print('PASS dependency pins and constant inventory; mathematical controls in independent probe')
if __name__=='__main__':main()
