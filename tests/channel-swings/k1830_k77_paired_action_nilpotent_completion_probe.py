#!/usr/bin/env python3
"""Independent finite split-retract controls; does not import full producer."""
from pathlib import Path
import json,copy
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def main():
    count=0
    for n in [2,3,4]:
        # Arbitrary oblique ambient embedding, nonorthogonal splitting.
        dim=4*n;R=s.diag(*([1]*(3*n)+[0]*n));V=s.eye(dim);V[3*n,0]=2;V[1,3*n]=3
        R=V*R*V.inv();Q=s.zeros(n,dim);Q[:,2*n:3*n]=s.eye(n);Q=Q*V.inv()
        for B in [s.zeros(n),s.eye(n),s.ones(n),s.eye(n).elementary_row_op('n->n+km',row=0,row2=1,k=2)]:
            U=s.zeros(dim,n);U[:n,:]=-B;U[n:2*n,:]=s.eye(n);U=V*U
            C=U*Q;assert R*C==C==C*R and C*C==s.zeros(dim) and C.rank()==n
            assert C.T*R.T==C.T==R.T*C.T
            # A supplied, nonorthogonal raw normalization has inverse-transpose dual pullback.
            D=s.eye(dim);D[0,2*n]=2;D[2*n,0]=1;K=D*C
            x=s.Matrix(range(1,dim+1));p=s.Matrix(range(dim,0,-1));bar=D.T.inv()*p
            assert (bar.T*K*x)[0]==(p.T*C*x)[0]
            assert ((D*p).T*K*x)[0] != (p.T*C*x)[0] or B==s.zeros(n) # wrong transform caught where nonzero
            count+=1
        # Symmetric Hessian does not imply symmetric C; all complementary gradients vanish.
        A=s.zeros(dim);A[0,2*n]=1;A=V*A*V.inv();H=s.BlockMatrix([[s.zeros(dim),A.T],[A,s.zeros(dim)]]).as_explicit()
        assert H==H.T and A!=A.T and H*H!=s.zeros(2*dim)
    # Nilpotent Jordan blocks plus free survivors, paired quotient has split signature.
    for n,r in [(4,1),(6,2),(8,2)]:
        C=s.zeros(n)
        for j in range(r):C[j,r+j]=1
        assert C*C==s.zeros(n) and n-2*C.rank()==n-2*r
        h=n-2*r;G=s.BlockMatrix([[s.zeros(h),s.eye(h)],[s.eye(h),s.zeros(h)]]).as_explicit()
        assert G.eigenvals()=={s.Integer(-1):h,s.Integer(1):h}
    d=json.loads((ROOT/'lab/process/k1830-k77-paired-action-nilpotent-completion.json').read_text())
    def report(v):
        return v['results']['homology_dimension']==256 and v['results']['paired_homology_signature']==[256,256] and not v['results']['source_action_selected'] and not v['results']['Hessian_identified_with_differential'] and not v['results']['physical_or_canon_promotion'] and all(v['checks'].values())
    assert report(d);mut=0
    for k,v in [('homology_dimension',512),('paired_homology_signature',[512,0]),('source_action_selected',True),('Hessian_identified_with_differential',True),('physical_or_canon_promotion',True)]:
        m=copy.deepcopy(d);m['results'][k]=v;assert not report(m);mut+=1
    m=copy.deepcopy(d);m['checks'][next(iter(m['checks']))]=False;assert not report(m);mut+=1
    print('PASS independent split-retract cases',count,'homology/form models 3; reporting mutations',mut)
if __name__=='__main__':main()
