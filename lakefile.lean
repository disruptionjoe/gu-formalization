import Lake
open Lake DSL

package gu_formalization where
  -- This package is intentionally small: Lean is used as a proof-carrying
  -- robustness layer for finite kernels, not as a rewrite of the GU program.

require "leanprover-community" / "mathlib"

@[default_target]
lean_lib GUFormalization where
  srcDir := "Lean"
