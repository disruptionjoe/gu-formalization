import Mathlib

/-! Conditional cores, not a formalization of GU or of the analytic estimates.
The actual solution sequence, its limits, and geometric equal-mass translates
are supplied by the written proofs. Mathlib's graph definition of closability
is used directly; no custom weakened notion replaces it. -/
namespace GUFormalization.ObservationSolutionTrace
open Filter Topology

variable {E F : Type*} [NormedAddCommGroup E] [NormedAddCommGroup F]
  [NormedSpace ℝ E] [NormedSpace ℝ F]

/-- A nonzero vertical graph limit rules out a closable partial linear map. -/
theorem nonclosable_of_graph_limit (T : E →ₗ.[ℝ] F)
    (z : ℕ → E × F) (v : F) (hv : v ≠ 0)
    (hz : ∀ n, z n ∈ T.graph)
    (hlim : Tendsto z atTop (𝓝 (0, v))) : ¬ T.IsClosable := by
  intro h
  obtain ⟨S, hS⟩ := h
  have hm : (0, v) ∈ T.graph.topologicalClosure :=
    mem_closure_of_tendsto hlim (Eventually.of_forall hz)
  rw [hS] at hm
  exact hv (S.graph_fst_eq_zero_snd hm rfl)

/-- Adding more admitted states cannot repair a nonclosable restriction. -/
theorem no_closable_extension (T S : E →ₗ.[ℝ] F)
    (hTS : T ≤ S) (hT : ¬ T.IsClosable) : ¬ S.IsClosable := by
  intro hS
  exact hT (hS.leIsClosable hTS)

/-- Arbitrarily many disjoint pieces of the same positive real mass cannot
fit into a finite total. Countable additivity/invariance are geometric inputs. -/
theorem no_finite_mass_bound (m M : ℝ) (hm : 0 < m)
    (h : ∀ n : ℕ, (n : ℝ) * m ≤ M) : False := by
  obtain ⟨n, hn⟩ := exists_nat_gt (M / m)
  have hn' : M < (n : ℝ) * m := (div_lt_iff₀ hm).mp hn
  exact (not_lt_of_ge (h n)) hn'

/-- The normal (6,4) fixed-frequency coarea tail is r^(7-2s). -/
theorem radial_integrability_threshold (s : ℝ) :
    7 - 2 * s < -1 ↔ 4 < s := by constructor <;> intro h <;> linarith

/-- The data/observation dimensions give the boundedness scaling order9/2. -/
theorem trace_scaling_dimension : (13 : ℚ) / 2 - 4 / 2 = 9 / 2 := by norm_num

end GUFormalization.ObservationSolutionTrace
