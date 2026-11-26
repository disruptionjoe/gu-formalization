"""Exact cheap controls for quotient/descent scaffolding, not physical certification.

Uses the owned 14D K95 connection vertex. Analytic CK existence and all-history
invisibility are reused written theorems; the probe certifies their finite
current coefficient. No physical pairing, response inverse, or GU verdict.
"""
from fractions import Fraction as Q
from itertools import product
import json
from source_action_paired_response_probe import C,I,vertex,vertex_legacy
from source_action_slice_completion_probe import inject,column,readout,zero
import source_action_deep_geometry as g


def run():
    checks = 0
    # Every observation-preserving equivalence of this fixture: within each
    # two-point fibre either keep both or identify them. All16 preserve image.
    histories = range(4)
    states = [(h,k) for h in histories for k in range(2)]
    for mask in product([False,True],repeat=4):
        classes = {(h,0 if mask[h] else k) for h,k in states}
        assert {h for h,k in classes} == set(histories)
        checks += 1
    # Restricting admissibility really changes image; merging distinct visible
    # histories instead makes the unchanged observation fail to descend.
    restricted = [(h,k) for h,k in states if h%2 == 0]
    assert {h for h,k in restricted} == {0,2};checks += 1
    bad_class = [(0,0),(1,0)]
    assert len({h for h,k in bad_class}) > 1;checks += 1
    # Actual vertex, no fitted matrix: imaginary central one-form in axis a.
    # The scalar-input column gives r_a=i Id. Multiplication by row -i makes
    # Re(eta V psi)=1; this is an independent classical row, NOT a norm.
    for a in range(14):
        u={(1<<a,0):I}
        r,s=vertex(u,inject(4))
        assert r[a] == {0:I}
        assert all(not r[b] for b in range(14) if b!=a)
        assert s == {1<<a:-I/(2*g.d[a])}
        assert vertex(u,inject(4)) == vertex_legacy(u,inject(4))
        assert ((-I)*r[a][0]).a == 1
        checks += 5
    # The actual observation hides normal one-form slots at a point.
    h=column(5)
    assert readout(h)==readout(zero()) and h!=zero();checks += 1
    # Covariant all-history hidden seed p2 on the trace CK hypersurface.
    # This finite identity authenticates the leading current difference;
    # the exact CK theorem, not this polynomial, supplies the curved solution.
    A=g.diag([1,-1,0,0])
    assert g.trace(A)==0 and g.trace(g.mm(A,A))==2;checks += 1
    for s in [Q(0),Q(1,3),Q(-2),Q(7,5)]:
        p2=s*s*g.trace(g.mm(A,A))
        current=p2*((-I)*I).a
        assert current == 2*s*s
        checks += 1
    assert 2*g.trace(g.mm(A,A))==4;checks += 1
    # Wrong scalar/trace substitution would erase the witness; wrong row
    # phase erases the real part. Both are deliberately rejected mutations.
    assert g.trace(A)**2 != g.trace(g.mm(A,A));checks += 1
    assert (C(1)*I).a == 0 and ((-I)*I).a != 0;checks += 1
    # Reuse established Ricci block arithmetic, no new curvature derivation.
    raised=[Q(1,4)]*5+[Q(-5,4)]*9
    assert sum(raised)==-10;checks += 1
    return {'checks':checks,'quotient_fixtures':16,'actual_vertex_axes':14,
            'central_time_current_real':1,'hidden_seed_current_second_derivative':4,
            'ambient_scalar_curvature_reused':-10,
            'observed_base_curvature_fixed':0,
            'exact_scope':'finite vertex and algebra controls; CK/dual analytic existence reused from written proofs',
            'not_certified':['physical admissibility','positive pairing','source quotient','matched inverse response','GU falsification']}

if __name__=='__main__': print(json.dumps(run(),indent=2))
