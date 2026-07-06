import Mathlib

set_option autoImplicit false

/-!
# K3 / RS Index Arithmetic Kernel

This file formalizes only the integer arithmetic currently used by the Python
audit `tests/rs_k3_symbol_index_formula_audit.py`.

It deliberately does not assert that the physical GU RS complex, symbol class,
background `ch_2`, APS correction, or `Y14 -> K3` bridge has been supplied.
-/

namespace GUFormalization
namespace K3IndexArithmetic

/-- K3 control values used by the current arithmetic audit. -/
def ahatK3 : Int := 2

def chiK3 : Int := 24

def sigmaK3 : Int := -16

def p1K3 : Int := -48

theorem ahat_from_signature : ahatK3 = -sigmaK3 / 8 := by
  norm_num [ahatK3, sigmaK3]

theorem p1_from_signature : p1K3 = 3 * sigmaK3 := by
  norm_num [p1K3, sigmaK3]

/--
The complex index expression from the K3 RS symbol-index arithmetic audit:

`int_K3 Ahat ch((T_C^*K3 + q) tensor F)`.

The parameters are left explicit:

* `rankC` is the complex rank of `F`;
* `ch2F` is `ch_2(F)[K3]`;
* `q` selects the vector-spinor / raw gamma-trace / BRST-style symbolic branch.
-/
def indexComplex (rankC ch2F q : Int) : Int :=
  (4 + q) * rankC * ahatK3 + rankC * p1K3 + (4 + q) * ch2F

/-- Spinor ghost control expression `int_K3 Ahat ch(F)`. -/
def spinorIndexComplex (rankC ch2F : Int) : Int :=
  rankC * ahatK3 + ch2F

theorem spinorIndex_flat_rank16 :
    spinorIndexComplex 16 0 = 32 := by
  norm_num [spinorIndexComplex, ahatK3]

theorem vectorSpinor_q0_flat_rank16 :
    indexComplex 16 0 0 = -640 := by
  norm_num [indexComplex, ahatK3, p1K3]

theorem rawGammaTraceFree_q1_flat_rank16 :
    indexComplex 16 0 1 = -608 := by
  norm_num [indexComplex, ahatK3, p1K3]

theorem brstStyle_qMinus1_flat_rank16 :
    indexComplex 16 0 (-1) = -672 := by
  norm_num [indexComplex, ahatK3, p1K3]

theorem brstStyle_is_raw_minus_two_spinor_ghosts (rankC ch2F : Int) :
    indexComplex rankC ch2F (-1) =
      indexComplex rankC ch2F 1 - 2 * spinorIndexComplex rankC ch2F := by
  unfold indexComplex spinorIndexComplex ahatK3 p1K3
  ring

/--
The current formula is parameter-sensitive: changing `ch_2(F)[K3]` changes the
raw `q = 1` expression. This is the formal boundary behind the prose claim that
the background characteristic class cannot be silently imported or ignored.
-/
theorem raw_q1_depends_on_ch2 :
    Not (indexComplex 16 0 1 = indexComplex 16 1 1) := by
  norm_num [indexComplex, ahatK3, p1K3]

end K3IndexArithmetic
end GUFormalization
