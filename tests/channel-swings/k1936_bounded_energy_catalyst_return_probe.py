"""Independent one-sided cutoff and common-part reconstruction; baseline before faults."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,importlib.util,json,math
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('producer',HERE/'k1936_bounded_energy_catalyst_return.py');p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
def require(test,label):
    if not test: raise AssertionError(label)
def independent():
    checks=0
    for J in (F(1,2),F(1),F(3)):
        for x in [F(i,2) for i in range(13)]:
            for y in [F(i,2) for i in range(13) if abs(F(i,2)-x)<=J]:
                for L in (F(1,3),F(1),F(7,3),F(8)):
                    a=max(x-L,0)-max(y-L,0)
                    require(a<=J*(x>L),'one-sided remainder');checks+=1
    # Distinct direct marginal reconstruction, including r=0 and r=1.
    for pp,qq in [([F(1),F(0),F(0)],[F(0),F(0),F(1)]),([F(1,4),F(1,2),F(1,4)],[F(1,2),F(1,4),F(1,4)]),([F(1,3)]*3,[F(1,3)]*3)]:
        common=[min(x,y) for x,y in zip(pp,qq)];r=1-sum(common)
        require(sum(abs(x-y) for x,y in zip(pp,qq))==2*r,'TV common part');checks+=1
        if 0<r<1:
            aa=[(x-z)/r for x,z in zip(pp,common)];bb=[(x-z)/r for x,z in zip(qq,common)]
            require(sum(aa)==sum(bb)==1,'residual normalization');checks+=1
    return checks

def main():
    count=independent();report=p.calculate();require(json.loads(p.REPORT.read_text())==report,'report baseline')
    require(report['source_sha256']==hashlib.sha256(Path(p.__file__).read_bytes()).hexdigest(),'pin baseline')
    clean=[[F(1,4),F(1,4)],[F(1,4),F(1,4)]]
    p.transport(clean,[F(0),F(1)],F(1),F(1,2))
    faults=[('jump width',lambda:p.transport(clean,[F(0),F(2)],F(1),F(1,2))),
            ('normalization',lambda:p.transport([[F(1),F(1)],[F(0),F(0)]],[F(0),F(1)],F(1),F(1))),
            ('negative transition',lambda:p.transport([[F(-1),F(1)],[F(1),F(0)]],[F(0),F(1)],F(1),F(1)))]
    for label,run in faults:
        try:run()
        except AssertionError: print('DETECTED mathematical input:',label)
        else:raise AssertionError('missed '+label)
    altered=dict(report);altered['certified_example']=None
    for label,a,b in [('report',altered,report),('pin','0'*64,report['source_sha256'])]:
        try:require(a==b,label)
        except AssertionError:print('DETECTED reporting:',label)
        else:raise AssertionError('missed '+label)
    print('PASS independent exact controls',count,'math faults',len(faults),'report/pin faults 2')
if __name__=='__main__':main()
