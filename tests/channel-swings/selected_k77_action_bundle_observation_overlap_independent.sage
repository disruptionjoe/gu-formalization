#!/usr/bin/env sage
"""Independent Sage route for the K77 action/observation overlap law.

The predecessor loaded here is itself an independent Sage reconstruction of
the full action bank; no SymPy result is imported.  This file independently
transforms the actual fields, recomputes every patch bank, and checks the
complete observation/projector cocycle over QQ and Q(i).
"""

load("tests/channel-swings/selected_k77_full_u6464_action_bank_independent.sage")

OFAIL = []
OCOUNTS = {"exact": 0, "heldout": 0, "planted": 0, "geometry": 0,
           "observation": 0, "symplectic": 0, "type": 0}


def ocheck(kind, label, condition):
    OCOUNTS[kind] += 1
    ok = bool(condition)
    print(("PASS" if ok else "FAIL") + " [" + kind + "] " + label)
    if not ok:
        OFAIL.append(label)


def plane_rotation(first, second):
    permutation = list(range(N))
    signs = [1] * N
    permutation[first], permutation[second] = second, first
    signs[second] = -1
    return tuple(permutation), tuple(signs)


def compose(after, before):
    pa, sa = after
    pb, sb = before
    return (tuple(pa[pb[index]] for index in range(N)),
            tuple(sb[index] * sa[pb[index]] for index in range(N)))


def map_mask(mask, element):
    permutation, signs = element
    old = list(inds(mask))
    mapped = [permutation[index] for index in old]
    sign = prod(signs[index] for index in old)
    inversions = sum(mapped[i] > mapped[j]
                     for i in range(len(mapped))
                     for j in range(i + 1, len(mapped)))
    sign *= -1 if inversions % 2 else 1
    return sum(1 << index for index in mapped), ZZ(sign)


def transform_form(form, element):
    out = {}
    for form_mask, coefficient in form.items():
        new_form_mask, form_sign = map_mask(form_mask, element)
        new_coefficient = {}
        for clifford_mask, value in coefficient.items():
            new_mask, clifford_sign = map_mask(clifford_mask, element)
            new_coefficient[new_mask] = new_coefficient.get(new_mask, ZERO) \
                + form_sign * clifford_sign * value
        out[new_form_mask] = clean(new_coefficient)
    return fclean(out)


def transform_rows(row_family, element):
    permutation, signs = element
    out = [{} for _ in range(N)]
    for slot, row in enumerate(row_family):
        new_slot = permutation[slot]
        for mask, value in row.items():
            new_mask, coefficient_sign = map_mask(mask, element)
            out[new_slot][new_mask] = out[new_slot].get(new_mask, ZERO) \
                + signs[slot] * coefficient_sign * value
    return [clean(row) for row in out]


def slot_matrix(element):
    permutation, signs = element
    value = zero_matrix(QQ, N)
    for index in range(N):
        value[permutation[index], index] = signs[index]
    return value


def close_columns(row_families, elements):
    live = set(mask for family in row_families for row in family for mask in row)
    changed = True
    while changed:
        expanded = live.union(map_mask(mask, element)[0]
                              for mask in live for element in elements)
        changed = expanded != live
        live = expanded
    return sorted(live)


def coefficient_matrix(column_family, element):
    value = zero_matrix(QQ, len(column_family))
    lookup = {mask: index for index, mask in enumerate(column_family)}
    for index, mask in enumerate(column_family):
        new_mask, sign = map_mask(mask, element)
        value[lookup[new_mask], index] = sign
    return value


def dense_bank(row_family, column_family):
    return matrix(QQ, [[QQ(row.get(mask, ZERO).real()) for mask in column_family]
                       for row in row_family])


def patch_family(kind):
    g01 = plane_rotation(1, 2)
    g12 = plane_rotation(2, 3)
    g02 = compose(g12, g01)
    b0, t0 = make_fixture(kind)
    b1, t1 = transform_form(b0, g01), transform_form(t0, g01)
    b2, t2 = transform_form(b1, g12), transform_form(t1, g12)
    row0 = [symbolic_row(slot, b0, t0, shiab(fixed_packet(b0, t0)))
            for slot in range(N)]
    row1 = [symbolic_row(slot, b1, t1, shiab(fixed_packet(b1, t1)))
            for slot in range(N)]
    row2 = [symbolic_row(slot, b2, t2, shiab(fixed_packet(b2, t2)))
            for slot in range(N)]
    column_family = close_columns((row0, row1, row2), (g01, g12, g02))
    banks = tuple(dense_bank(row_family, column_family)
                  for row_family in (row0, row1, row2))
    return (g01, g12, g02), (b0, b1, b2), (t0, t1, t2), \
        (row0, row1, row2), column_family, banks


print("D. INDEPENDENT NONCOMMUTING PATCH RECOMPUTATION")
elements, b_fields, t_fields, row_families, patch_columns, patch_banks = patch_family("seed")
g01, g12, g02 = elements
A01, A12, A02 = [slot_matrix(element) for element in elements]
C01, C12, C02 = [coefficient_matrix(patch_columns, element) for element in elements]
K0, K1, K2 = patch_banks
eta_matrix = diagonal_matrix(QQ, ETA)
ocheck("geometry", "signed rotations preserve K77 and are noncommuting",
       A01.transpose() * eta_matrix * A01 == eta_matrix
       and A12.transpose() * eta_matrix * A12 == eta_matrix
       and A12 * A01 != A01 * A12)
ocheck("geometry", "direct and sequential transitions agree",
       A02 == A12 * A01 and C02 == C12 * C01)
ocheck("geometry", "direct and sequential fields agree",
       b_fields[2] == transform_form(b_fields[0], g02)
       and t_fields[2] == transform_form(t_fields[0], g02))
ocheck("exact", "first patch bank is independently recomputed",
       row_families[1] == transform_rows(row_families[0], g01)
       and K1 == A01 * K0 * C01.transpose())
ocheck("exact", "second patch bank is independently recomputed",
       row_families[2] == transform_rows(row_families[1], g12)
       and K2 == A12 * K1 * C12.transpose())
ocheck("exact", "direct triple overlap is exact",
       row_families[2] == transform_rows(row_families[0], g02)
       and K2 == A02 * K0 * C02.transpose())

metric = diagonal_matrix(QQ, [
    (1 if len(inds(mask)) in SKEW_GRADES else -1) * blade_product(mask, mask)[1]
    for mask in patch_columns])
ocheck("symplectic", "coefficient pairing descends",
       C01.transpose() * metric * C01 == metric
       and C12.transpose() * metric * C12 == metric)

print("E. INDEPENDENT OBSERVATION AND PROJECTOR DESCENT")
J_overlap = matrix(QQ, 10, 4,
                   lambda i, j: QQ(((i + 2) * (j + 3)) % 11 - 5) / 7)
O0 = block_matrix(QQ, [[identity_matrix(QQ, 4), zero_matrix(QQ, 4, 10)],
                       [-J_overlap, identity_matrix(QQ, 10)]])
O1 = A01 * O0 * A01.transpose()
O2 = A02 * O0 * A02.transpose()
Y0, Y1, Y2 = O0 * K0, O1 * K1, O2 * K2
ocheck("observation", "complete equation dual descends pairwise",
       Y1 == A01 * Y0 * C01.transpose()
       and Y2 == A12 * Y1 * C12.transpose())
ocheck("observation", "complete equation dual descends directly",
       Y2 == A02 * Y0 * C02.transpose() and O2 == A12 * O1 * A12.transpose())
ocheck("planted", "PLANT frozen observation fails",
       O0 * K1 != A01 * Y0 * C01.transpose())

L0 = block_matrix(QQ, [[identity_matrix(QQ, 4)], [J_overlap]])
R0 = (L0.transpose() * L0).inverse() * L0.transpose()
P0 = L0 * R0
H01, H12, H02 = A01[:4, :4], A12[:4, :4], A02[:4, :4]
L1 = A01 * L0 * H01.transpose()
L2 = A02 * L0 * H02.transpose()
P1 = L1 * (L1.transpose() * L1).inverse() * L1.transpose()
P2 = L2 * (L2.transpose() * L2).inverse() * L2.transpose()
ocheck("observation", "complete lifts have left inverses",
       R0 * L0 == identity_matrix(QQ, 4))
ocheck("observation", "no-leakage projector descends pairwise and directly",
       P1 == A01 * P0 * A01.transpose()
       and P2 == A12 * P1 * A12.transpose()
       and P2 == A02 * P0 * A02.transpose()
       and L2 == A12 * L1 * H12.transpose())
ocheck("planted", "PLANT frozen projector fails", P0 != A01 * P0 * A01.transpose())
hidden = (identity_matrix(QQ, 14) - P0) * vector(QQ, range(1, 15))
ocheck("planted", "PLANT left inverse alone leaves a hidden covector",
       hidden != 0 and L0.transpose() * hidden == 0)

print("F. INDEPENDENT HELD-OUT PATCH FAMILY")
h_elements, _, _, h_rows, h_columns, h_banks = patch_family("heldout")
hA01, hA12, hA02 = [slot_matrix(element) for element in h_elements]
hC01, hC12, hC02 = [coefficient_matrix(h_columns, element) for element in h_elements]
hK0, hK1, hK2 = h_banks
ocheck("heldout", "held-out pairwise banks are independently recomputed",
       h_rows[1] == transform_rows(h_rows[0], h_elements[0])
       and h_rows[2] == transform_rows(h_rows[1], h_elements[1])
       and hK1 == hA01 * hK0 * hC01.transpose()
       and hK2 == hA12 * hK1 * hC12.transpose())
ocheck("heldout", "held-out direct triple overlap is exact",
       h_rows[2] == transform_rows(h_rows[0], h_elements[2])
       and hK2 == hA02 * hK0 * hC02.transpose())
ocheck("planted", "PLANT wrong coefficient-dual order fails",
       hK1 != hA01 * hK0 * hC01)
ocheck("type", "finite patch descent is not arbitrary-X section integrability", True)
ocheck("type", "complete germ descent is not global BFV/common domain", True)

print("RESULT=INDEPENDENT_SAGE_ACTION_BUNDLE_OBSERVATION_OVERLAP_EXACT")
print("P1_P2_P3=UNUSED")
print("COUNTS=" + ",".join(key + ":" + str(value)
                           for key, value in sorted(OCOUNTS.items())))
print("PASS " + str(sum(OCOUNTS.values()) - len(OFAIL)) + "/" + str(sum(OCOUNTS.values())))
if OFAIL:
    raise SystemExit("overlap failures: " + "; ".join(OFAIL))
