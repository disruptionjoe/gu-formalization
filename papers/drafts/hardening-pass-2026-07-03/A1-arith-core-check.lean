/-
Historical mathlib-free subset of the A1 theorem legs.  The authoritative full module is now
`Lean/GUFormalization/LocatedNotForcedLegs.lean`, which is part of the pinned default target
and was reverified on 2026-07-22.  This smaller file remains only as an independent core check.
-/

namespace GUFormalization
namespace TwoPrimaryCore

-- 3c. Rokhlin bulk RS index: 16|sigma => 21*sigma/8 = 42k (exact integer division).
theorem rs_bulk_index_on_rokhlin (k : Int) : 21 * (16 * k) / 8 = 42 * k := by omega

-- 3c'. RS bulk index is even.
theorem rs_bulk_even (k : Int) : ∃ r, 21 * (16 * k) / 8 = r + r := ⟨21 * k, by omega⟩

-- 3d. Adjoint Dirac index 4k divisible by 4.
theorem adjoint_index_div_four (k : Int) : (4 : Int) ∣ 4 * k := ⟨k, rfl⟩

-- 3f. Kramers / mod-2 Witten index.
theorem kramers_mod_two (n : Int) : (2 * n) % 2 = 0 := by omega

-- 3f'. Ghost parity 50/50 net zero.
theorem ghost_parity_net_zero (n : Int) : n - n = 0 := by omega

-- (3e lens numerator oddness needs `ring`/mathlib for the q^2 term; see the full file.)

end TwoPrimaryCore
end GUFormalization
