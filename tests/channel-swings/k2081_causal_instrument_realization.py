"""Pinned constants for a conditional written theorem; probe checks finite CAR independently."""
from pathlib import Path
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2]
def build():
 refs=['explorations/conditional-build/k2080-local-car-detector-2026-10-26.md', 'explorations/conditional-build/k2060-positive-energy-localization-2026-10-25.md']
 return dict(id='K2081',constants={'record_error_factor': '1/2', 'channel_signal_factor': '2', 'channel_error_factor': '1', 'example_overlap_squares': ['1/2', '1/2'], 'example_channel_signal': '1/2', 'example_record_error': '1/4', 'mixing_time_factor': '1'},inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs},scope='conditional mathematics; internal verification only; no GU or continuum apparatus certification')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=build();out=ROOT/'lab/process/k2081-causal-instrument-realization.json'
 if a.write:out.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(out.read_text())==d
 print('PASS producer',d['id'])
