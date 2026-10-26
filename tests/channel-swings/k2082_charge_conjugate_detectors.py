"""Pinned constants for a conditional written theorem; probe checks finite CAR independently."""
from pathlib import Path
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2]
def build():
 refs=['explorations/conditional-build/k2080-local-car-detector-2026-10-26.md', 'explorations/conditional-build/k2056-common-dual-successor-2026-10-25.md', 'explorations/conditional-build/k2058-universal-positive-dynamics-2026-10-25.md', 'explorations/conditional-build/k2060-positive-energy-localization-2026-10-25.md']
 return dict(id='K2082',constants={'real_mode_noise': '1/2', 'paired_vacuum': '2*nu-nu**2', 'paired_signal': '2*nu-nu**2+(1-nu)*a2', 'energy_factor': '8', 'anti_square': -1, 'automorphism_square': 'fermion_parity'},inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs},scope='conditional mathematics; internal verification only; no GU or continuum apparatus certification')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=build();out=ROOT/'lab/process/k2082-charge-conjugate-detectors.json'
 if a.write:out.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(out.read_text())==d
 print('PASS producer',d['id'])
