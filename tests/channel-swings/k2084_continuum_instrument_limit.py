"""Reproduce typed constants and pin dependencies; reporting check, not proof."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k2084-continuum-instrument-limit.json').read_text())
 for p,h in d['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'input changed'
 assert d['constants']=={'number_bound': 2, 'flagged_bound': 4, 'paired_bound': 4, 'mean_energy_factor': '1/2', 'smooth_projection_fraction': '8/pi**2'}, 'constant inventory'
 print('PASS dependency pins and constant inventory; mathematical controls in independent probe')
if __name__=='__main__':main()
