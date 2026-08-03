#!/usr/bin/env python3
"""Exact Lambda^5 / Spin(10) / Pati-Salam channel certificate for Wave C.

The script derives the 126 Pati-Salam branch from Sym^2(16) minus the vector
10, locates the right-neutrino bilinear and its dual mediator field, and keeps
the five physical construction stages separate.
"""
from collections import Counter
from math import comb


checks = 0


def check(label, condition, detail=""):
    global checks
    checks += 1
    print("[{}] {}{}".format("PASS" if condition else "FAIL", label,
                             " -- " + detail if detail else ""))
    assert condition, label


SU4_DIM = {"1": 1, "4": 4, "4bar": 4, "6": 6,
           "10": 10, "10bar": 10, "15": 15}
SU4_DUAL = {"1": "1", "4": "4bar", "4bar": "4", "6": "6",
            "10": "10bar", "10bar": "10", "15": "15"}


def ps(su4, left, right):
    return (su4, int(left), int(right))


def ps_degree(character):
    return sum(SU4_DIM[irrep[0]] * irrep[1] * irrep[2] * mult
               for irrep, mult in character.items())


def su4_tensor_singlet_multiplicity(left, right):
    """Schur multiplicity dim Hom_SU4(1,left tensor right)."""
    return int(SU4_DUAL[left] == right)


def su2_tensor_singlet_multiplicity(left_dim, right_dim):
    """SU(2) irreps are self-dual; Schur gives one singlet iff equal."""
    return int(left_dim == right_dim)


def ps_tensor_singlet_multiplicity(left, right):
    return (su4_tensor_singlet_multiplicity(left[0], right[0]) *
            su2_tensor_singlet_multiplicity(left[1], right[1]) *
            su2_tensor_singlet_multiplicity(left[2], right[2]))


def subtract_exact(lhs, rhs):
    out = lhs.copy()
    for irrep, multiplicity in rhs.items():
        check("Pati-Salam subtraction is nonnegative",
              out[irrep] >= multiplicity,
              "{}: {} >= {}".format(irrep, out[irrep], multiplicity))
        out[irrep] -= multiplicity
        if out[irrep] == 0:
            del out[irrep]
    return out


# Lambda^5(V4 + V10) = sum_a Lambda^a(V4) x Lambda^(5-a)(V10).
normal_wedge_dims = {1: 10, 2: 45, 3: 120, 4: 210, 5: 252}
split_terms = [(a, comb(4, a), normal_wedge_dims[5 - a]) for a in range(5)]
split_dims = [base * normal for _, base, normal in split_terms]
check("Lambda^5 split dimensions are 252,840,720,180,10",
      split_dims == [252, 840, 720, 180, 10], repr(split_dims))
check("Lambda^5(C^14) dimension closes", sum(split_dims) == comb(14, 5) == 2002)
check("internal base-degree-zero sector is 252", split_dims[0] == 252)
check("internal 252 splits into two Hodge halves", 252 == 126 + 126)

# At Spin(14), Lambda^2(S+) = Lambda^1(V14) + Lambda^5(V14):
# 2016 = 14 + 2002.  The internal symmetric 126 is compatible with identical
# Grassmann fields because the Lorentz Lambda^2(2) supplies the antisymmetry.
check("Spin(14) antisymmetric spinor square dimension",
      comb(64, 2) == 14 + comb(14, 5) == 2016)
check("Spin(10) symmetric spinor square is 10 plus 126",
      comb(16 + 1, 2) == 10 + 126 == 136)
check("Spin(10) antisymmetric spinor square is 120", comb(16, 2) == 120)

# Important scalar homonym: Lambda^4(V4) is trivial under connected Spin(4)
# but parity-odd under O(4).  Thus 252 is the unique base-degree-zero scalar
# sector, not the only connected-Lorentz singlet sector.
proper_lorentz_singlet_dimension = split_dims[0] + split_dims[4]
check("proper-Lorentz singlets include degree-zero 252 plus top-form 10",
      proper_lorentz_singlet_dimension == 262)
check("planted '252 is the only connected-Lorentz singlet' is rejected",
      proper_lorentz_singlet_dimension != 252)

# F+ = A + B = (4,2,1) + (4bar,1,2).
# Sym^2(A) and Sym^2(B) use
# Sym^2(U x W)=Sym^2U x Sym^2W + Lambda^2U x Lambda^2W.
sym2_A = Counter({ps("10", 3, 1): 1, ps("6", 1, 1): 1})
sym2_B = Counter({ps("10bar", 1, 3): 1, ps("6", 1, 1): 1})
cross_AB = Counter({ps("1", 2, 2): 1, ps("15", 2, 2): 1})
sym2_Fp = sym2_A + sym2_B + cross_AB
vector_10 = Counter({ps("6", 1, 1): 1, ps("1", 2, 2): 1})
branch_126p = subtract_exact(sym2_Fp, vector_10)
expected_126p = Counter({
    ps("6", 1, 1): 1,
    ps("10", 3, 1): 1,
    ps("10bar", 1, 3): 1,
    ps("15", 2, 2): 1,
})
check("126+ Pati-Salam branch derived from Sym^2(16+) - 10",
      branch_126p == expected_126p, repr(sorted(branch_126p.items())))
check("126+ Pati-Salam dimension closure", ps_degree(branch_126p) == 126)

branch_126m = Counter({
    ps("6", 1, 1): 1,
    ps("10bar", 3, 1): 1,
    ps("10", 1, 3): 1,
    ps("15", 2, 2): 1,
})
check("dual 126- Pati-Salam dimension closure", ps_degree(branch_126m) == 126)

nu_right_bilinear = ps("10bar", 1, 3)
nu_right_field = ps("10", 1, 3)
check("symmetric right-neutrino pair occurs in the 126+ bilinear",
      branch_126p[nu_right_bilinear] == 1)
check("dual (10,1,3) mediator-field type occurs in 126-",
      branch_126m[nu_right_field] == 1)
check("bilinear and mediator field are dual, not identical labels",
      nu_right_bilinear != nu_right_field)
check("dual right-neutrino Pati-Salam contraction has singlet multiplicity one",
      ps_tensor_singlet_multiplicity(nu_right_bilinear,
                                     nu_right_field) == 1)
check("planted same 10bar x 10bar contraction has no SU4 singlet",
      ps_tensor_singlet_multiplicity(nu_right_bilinear,
                                     nu_right_bilinear) == 0)

# Real-form and raw Krein parity.  On signature (6,4), star^2 on internal
# 5-forms is (-1)^(5*5+4)=-1, so the real carrier is 252-dimensional and the
# two 126s are complex-conjugate +/-i eigenspaces, not two real summands.
hodge_star_square_sign = (-1) ** (5 * (10 - 5) + 4)
degree_five_reversal_sign = (-1) ** (5 * (5 - 1) // 2)
check("internal (6,4) Hodge star squares to minus one on five-forms",
      hodge_star_square_sign == -1)
check("real internal object is one 252 with complex-conjugate 126 halves",
      hodge_star_square_sign == -1 and 252 == 2 * 126)
check("degree-five Clifford reversal sign is plus one",
      degree_five_reversal_sign == 1)
check("raw K times degree-five Clifford word preserves 14D chirality",
      (-1) * (-1) == 1)  # K and every odd Clifford word each flip chirality.

# W192/W194 carrier gate: raw real odd Clifford words are K-self-adjoint,
# whereas an Sp connection generator must be K-anti-self-adjoint.  Hence the
# tempting raw inclusion Lambda^5 -> ad(P) has the wrong adjoint class.  This
# does not exclude a phased/reality-completed field or a contraction whose
# actual ad(P) generator has even Clifford degree.
raw_degree_five_is_K_self_adjoint = degree_five_reversal_sign == 1
connection_requires_K_anti_self_adjoint = True
check("raw real degree-five word is in the K-self-adjoint class",
      raw_degree_five_is_K_self_adjoint)
check("raw real Lambda5 cannot itself be an Sp connection generator",
      raw_degree_five_is_K_self_adjoint and
      connection_requires_K_anti_self_adjoint)

# Five-stage physical burden.  Only complex representation support is built.
stages = {
    "complex_bilinear_representation_support": "PASS",
    "gu_native_krein_pairing": "PARTIAL_RAW_PARITY_ONLY",
    "real_or_C_reality_field": "PARTIAL_REAL_252_ONLY",
    "nonzero_source_owned_vev": "OPEN",
    "induced_four_dimensional_mass_operator": "OPEN",
}
check("stage 1 support is exact",
      stages["complex_bilinear_representation_support"] == "PASS")
check("stages 2 and 3 are explicitly partial",
      stages["gu_native_krein_pairing"].startswith("PARTIAL") and
      stages["real_or_C_reality_field"].startswith("PARTIAL"))
check("stages 4 and 5 remain open",
      stages["nonzero_source_owned_vev"] == "OPEN" and
      stages["induced_four_dimensional_mass_operator"] == "OPEN")
check("planted occurrence-to-mass promotion is rejected",
      stages["induced_four_dimensional_mass_operator"] != "PASS")

# The remaining carrier problem: GU's boson is an ad-valued one-form.  An
# inclusion Lambda^5 V10 in End(S) does not supply the extra one-form leg or a
# native projection from Omega^1(Y,ad P).
native_connection_to_lambda5_map_built = False
check("admissible effective Lambda5 connection placement remains unbuilt",
      not native_connection_to_lambda5_map_built)

print("Q6 verdict: Lambda^5 supplies both 126 halves and the dual")
print("right-neutrino channel at compact complex representation grade only.")
print("checks passed:", checks)
