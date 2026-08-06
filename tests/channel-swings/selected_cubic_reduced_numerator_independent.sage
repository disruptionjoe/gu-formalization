"""Independent exact reconstruction of the selected-cubic completion fork."""

R.<alpha,b,d> = PolynomialRing(QQ)
F = R.fraction_field()
alpha, b, d = map(F, (alpha, b, d))
m2 = alpha*b

def J(z):
    return matrix(F, [[alpha*z, z], [z, b]])

u0 = vector(F, [1, 0])
um = vector(F, [1, -alpha])
assert J(0)*u0 == 0
assert J(m2)*um == 0

Ehh = matrix(F, [[1, 0], [0, 0]])
Rmap = matrix(F, [[d/(2*alpha), 0], [0, 0]])
z = F['z'].gen() if False else F(1)  # keep the reconstruction over F

def delta_hh(zv):
    return d*zv*Ehh

def delta_redef(zv):
    return Rmap.transpose()*J(zv) + J(zv)*Rmap

assert delta_hh(m2)[0,0] == delta_redef(m2)[0,0] == d*m2
assert delta_hh(m2)[0,1] == 0
assert delta_redef(m2)[0,1] == d*m2/(2*alpha)

def hh_vertex(ui, zi, uj, zj):
    return d*(zi+zj)*ui[0]*uj[0]/2

def redef_vertex(ui, zi, uj, zj):
    Ji, Jj = J(zi), J(zj)
    return (
        (Rmap*ui)*Jj*uj
        + ui*Ji*Rmap*uj
        + (Rmap*uj)*Ji*ui
        + uj*Jj*Rmap*ui
    )/2

assert hh_vertex(u0,0,u0,0) == 0
assert hh_vertex(u0,0,um,m2) == d*m2/2
assert hh_vertex(um,m2,um,m2) == d*m2
assert redef_vertex(u0,0,u0,0) == 0
assert redef_vertex(u0,0,um,m2) == 0
assert redef_vertex(um,m2,um,m2) == 0

print("SAGE_INDEPENDENT_SELECTED_CUBIC_REDUCED_NUMERATOR_PASS")
print("Q0Q0_BULK_NUMERATOR=0")
print("Q0QM_HH_ONLY=d*alpha*b/2")
print("Q0QM_FIELD_REDEFINITION_COMPLETION=0")
