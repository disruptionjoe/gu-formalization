"""Exact contact-conditioned certificates for the unrestricted small-spacing frontier."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k2041-exact-small-spacing-frontier.json'
EA,RA=Q(1575,653),Q(729,2612);EB,RB=Q(675,181),Q(81,362)
A,C=Q(1053,2768),Q(2907,69200);DELTA=EB-EA

def certify(delta,bank):
    ka=C*delta/(DELTA+delta);kb=C*delta/(DELTA-delta)
    bad=[]
    for cell in bank:
        contacts=set()
        for row in cell['vertices']:
            e,r=Q(row['energy']),Q(row['value']);g=r+C*e-A
            assert g>=0
            if g==0:contacts.add((e,r));continue
            assert g-ka*(e-EA)>=0,'A contact-conditioned vertex'
            assert g-kb*(EB-e)>=0,'B contact-conditioned vertex'
            bad.append((e,r,g))
        assert len(contacts)<=1
    kap=10*C-A
    assert kap-ka*(10-EA)>0 and kap+kb*(10-EB)>0
    assert (C-ka)*delta==ka*DELTA and (C+kb)*delta==kb*DELTA
    return bad

def produce():
    bank=json.loads((ROOT/'lab/process/k2037-thermal-seven-level-boundary.json').read_text())['banks']['9']
    limits={'A':[],'B':[]};count=0
    for cell in bank:
        for row in cell['vertices']:
            e,r=Q(row['energy']),Q(row['value']);gap=r+C*e-A;count+=1
            if not gap:continue
            for name,den in [('A',C*(e-EA)-gap),('B',C*(EB-e)+gap)]:
                if den>0:limits[name].append((DELTA*gap/den,e,r))
    da,db=min(limits['A']),min(limits['B']);assert da[0]==Q(9,28417) and db[0]==Q(1,23508)
    d=db[0];certify(d,bank);certify(d/2,bank)
    # A changed shape beats the old right branch above its own pairwise threshold.
    # This is larger than the sufficient certificate limit; do not conflate them.
    ep,rp=Q(349,145),Q(81,290);dnext=Q(4,181);e=(EA+3*EB)/4
    t=(EB-e)/(EB-ep-dnext)
    newer=(1-t)*RB+t*rp
    old=RB+(RA-RB)*(EB-e)/(DELTA-dnext)
    assert newer<old
    rival_threshold=Q(2,181)
    assert (RA-RB)/(DELTA-rival_threshold)==(rp-RB)/(EB-ep-rival_threshold)
    inputs=['lab/process/k2037-thermal-seven-level-boundary.json','lab/process/k2039-thermal-component-undercut.json','explorations/conditional-build/k2039-thermal-component-undercut-2026-10-24.md']
    return dict(result_id='K2041',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',endpoint_A=[str(EA),str(RA)],endpoint_B=[str(EB),str(RB)],line=[str(A),str(C)],width=str(DELTA),certified_spacing=str(d),A_certificate_limit=list(map(str,da)),B_certificate_limit=list(map(str,db)),bank_records=count,frontier='L(E)+min(C*delta*(E-EA)/(Delta+delta), C*delta*(EB-E)/(Delta-delta))',switch_energy='(EA+EB+delta)/2',maximum_excess='C*delta/2',dimension=dict(strict_interior=22,endpoints=11,scope='0<delta<1/23508; diagonals classified up to unoccupied extra levels and channel freedom'),second_order=dict(left='-C*(E-EA)/Delta^2',midpoint='-C/(2*Delta)',right='C*(EB-E)/Delta^2',boundary_layer='at E=(EA+EB)/2+theta*delta, normalized second-order defect tends to (C/Delta)*clamp(2*theta-1/2,-1/2,1/2)',uniform_fixed_coefficient=False),successor_witness=dict(pairwise_threshold=str(rival_threshold),delta=str(dnext),energy=str(e),shifted_endpoint_energy=str(ep),shifted_endpoint_return=str(rp),shifted_mass=str(t),return_value=str(newer),old_return=str(old),improvement=str(old-newer),dimension=20),inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},scope='Exact unrestricted finite/countable optimum on the stated small-spacing interval; no larger-spacing phase or GU claim.')
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce()
    if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert r==json.loads(OUT.read_text())
    print('PASS K2041',r['bank_records'],'vertex certificates and explicit next-shape undercut')
