import Mathlib

set_option autoImplicit false

/-!
# Abstract co-flip accounting over the finite `(p,q)` class

This file is the Lean lift requested by H1/H4 after the concrete
`CoflipCore.lean` kernel: it formalizes the sign/accounting theorem over an
abstract finite signature `(p,q)` envelope with `p,q >= 1`.

Scope boundary:

* The fields `sector` and `dir` are the abstract-class outputs of the H1/H4
  rigidity lemmas: `sigma = eps` and `d = mu * eps` on witnessed states.
* This file proves the operation-calculus consequences: no zero-import map
  splits the pair, and a split is equivalent to the one paid `mu` bit.
* It does not formalize the full finite-dimensional spectral decomposition
  proof of Lemma L0 or any BV/cohomological/physical interpretation.
-/

namespace GUFormalization
namespace CoflipAbstract

abbrev Sign := ℤˣ

/-- A finite real signature with both sectors inhabited. The theorem below is
blind to the numerical values of `p` and `q` after these admissibility gates. -/
structure FiniteSignature where
  p : ℕ
  q : ℕ
  hp : 0 < p
  hq : 0 < q

/-- Abstract H1/H4 envelope: `eps` is the payload orientation and `mu` is the
single underived record-law sign slot. `witnessed` means the record trajectory
has strictly positive total nonnegative drive, so its direction is defined. -/
structure System where
  sig : FiniteSignature
  eps : Sign
  mu : Sign
  witnessed : Prop

/-- Sector observable after the H1/H4 sector-rigidity lemma: `sigma = eps`. -/
def sector (X : System) : Sign := X.eps

/-- Record-direction observable after charge positivity on witnessed states:
`d = mu * eps`. -/
def dir (X : System) (_h : X.witnessed) : Sign := X.mu * X.eps

/-- The abstract import counter: the paid bit is exactly `mu = -1`. -/
def importCost (X : System) : ℕ := if X.mu = 1 then 0 else 1

def zeroImport (X : System) : Prop := X.mu = 1

def diagonal (X : System) (h : X.witnessed) : Prop := sector X = dir X h

def antidiagonal (X : System) (h : X.witnessed) : Prop := sector X = -dir X h

theorem units_ne_neg_self (s : Sign) : ¬ s = -s := by
  rcases Int.units_eq_one_or s with h | h <;> subst h <;> intro hs
  · have h2 : (1 : ℤ) = -1 := by simpa using congrArg Units.val hs
    omega
  · have h2 : (-1 : ℤ) = 1 := by simpa using congrArg Units.val hs
    omega

theorem units_one_ne_neg_one : ¬ ((1 : Sign) = -1) := units_ne_neg_self 1

theorem units_neg_one_ne_one : ¬ ((-1 : Sign) = 1) := fun h =>
  units_ne_neg_self 1 h.symm

theorem signs_equal_or_opposite (a b : Sign) : a = b ∨ a = -b := by
  rcases Int.units_eq_one_or a with ha | ha <;>
    rcases Int.units_eq_one_or b with hb | hb <;>
    subst ha <;> subst hb <;> simp

theorem zeroImport_diagonal (X : System) (hX : X.witnessed) (h0 : zeroImport X) :
    diagonal X hX := by
  simp [diagonal, sector, dir, zeroImport] at h0 ⊢
  exact h0

theorem diagonal_iff_mu_one (X : System) (hX : X.witnessed) :
    diagonal X hX ↔ X.mu = 1 := by
  rcases Int.units_eq_one_or X.mu with hm | hm <;>
    rcases Int.units_eq_one_or X.eps with he | he <;>
    simp [diagonal, sector, dir, hm, he, units_one_ne_neg_one, units_neg_one_ne_one]

theorem antidiagonal_iff_mu_neg (X : System) (hX : X.witnessed) :
    antidiagonal X hX ↔ X.mu = -1 := by
  rcases Int.units_eq_one_or X.mu with hm | hm <;>
    rcases Int.units_eq_one_or X.eps with he | he <;>
    simp [antidiagonal, sector, dir, hm, he, units_one_ne_neg_one, units_neg_one_ne_one]

theorem importCost_one_iff_mu_neg (X : System) : importCost X = 1 ↔ X.mu = -1 := by
  rcases Int.units_eq_one_or X.mu with hm | hm <;>
    simp [importCost, hm, units_one_ne_neg_one, units_neg_one_ne_one]

theorem importCost_zero_iff_mu_one (X : System) : importCost X = 0 ↔ X.mu = 1 := by
  rcases Int.units_eq_one_or X.mu with hm | hm <;>
    simp [importCost, hm, units_one_ne_neg_one, units_neg_one_ne_one]

/-- The exact-price theorem in class form: on witnessed states, splitting the
observable pair is equivalent to paying the one record-law bit. -/
theorem exact_price (X : System) (hX : X.witnessed) :
    antidiagonal X hX ↔ importCost X = 1 := by
  rw [antidiagonal_iff_mu_neg, importCost_one_iff_mu_neg]

/-- H1's all-maps form: any map whose source and target are both witnessed and
zero-import lands on the diagonal at both ends, so it fixes both observables or
flips both. No structure on the map is used. -/
theorem arbitrary_zeroImport_map_diagonal (X Y : System)
    (hX : X.witnessed) (hY : Y.witnessed)
    (hX0 : zeroImport X) (hY0 : zeroImport Y) :
    (sector Y = sector X ∧ dir Y hY = dir X hX) ∨
    (sector Y = -sector X ∧ dir Y hY = -dir X hX) := by
  have dX : dir X hX = sector X := by
    have hx := zeroImport_diagonal X hX hX0
    exact hx.symm
  have dY : dir Y hY = sector Y := by
    have hy := zeroImport_diagonal Y hY hY0
    exact hy.symm
  rcases signs_equal_or_opposite (sector Y) (sector X) with hsame | hflip
  · left
    constructor
    · exact hsame
    · rw [dY, dX, hsame]
  · right
    constructor
    · exact hflip
    · rw [dY, dX, hflip]

/-! ## Parameter-map operation calculus -/

/-- The class operation calculus only has two observable sign coordinates:
payload flip `e` and paid record-law flip `m`. Other admissible structure moves
are invisible to this abstract theorem. -/
abbrev Op := Sign × Sign

def Op.e (g : Op) : Sign := g.1

def Op.m (g : Op) : Sign := g.2

def apply (g : Op) (X : System) : System :=
  { X with eps := g.e * X.eps, mu := g.m * X.mu }

def zeroImportOp (g : Op) : Prop := g.m = 1

def flipsSector (g : Op) (X : System) : Prop :=
  sector (apply g X) = -sector X

def flipsDirection (g : Op) (X : System) (hX : X.witnessed) : Prop :=
  dir (apply g X) hX = -dir X hX

def splits (g : Op) (X : System) (hX : X.witnessed) : Prop :=
  Xor (flipsSector g X) (flipsDirection g X hX)

theorem sector_apply (g : Op) (X : System) :
    sector (apply g X) = g.e * sector X := rfl

theorem dir_apply (g : Op) (X : System) (hX : X.witnessed) :
    dir (apply g X) hX = (g.m * g.e) * dir X hX := by
  simp [dir, apply, Op.e, Op.m, mul_left_comm, mul_comm]

theorem flipsSector_iff (g : Op) (X : System) :
    flipsSector g X ↔ g.e = -1 := by
  rcases Int.units_eq_one_or g.e with he | he <;>
    rcases Int.units_eq_one_or X.eps with hx | hx <;>
    simp [flipsSector, sector, apply, Op.e, he, hx, neg_eq_iff_eq_neg,
      units_one_ne_neg_one, units_neg_one_ne_one]

theorem flipsDirection_iff (g : Op) (X : System) (hX : X.witnessed) :
    flipsDirection g X hX ↔ g.m * g.e = -1 := by
  rcases Int.units_eq_one_or (g.m * g.e) with hme | hme <;>
    rcases Int.units_eq_one_or (dir X hX) with hd | hd <;>
    simp [flipsDirection, dir_apply, hme, hd, neg_eq_iff_eq_neg,
      units_one_ne_neg_one, units_neg_one_ne_one]

theorem splits_iff_paid (g : Op) (X : System) (hX : X.witnessed) :
    splits g X hX ↔ g.m = -1 := by
  simp only [splits, Xor, flipsSector_iff, flipsDirection_iff]
  rcases Int.units_eq_one_or g.e with he | he <;>
    rcases Int.units_eq_one_or g.m with hm | hm <;>
    simp [he, hm, units_one_ne_neg_one, units_neg_one_ne_one]

theorem no_zeroImport_split (g : Op) (X : System) (hX : X.witnessed)
    (hg : zeroImportOp g) : ¬ splits g X hX := by
  intro hs
  have hm : g.m = -1 := (splits_iff_paid g X hX).mp hs
  rw [zeroImportOp] at hg
  rw [hg] at hm
  exact units_one_ne_neg_one hm

theorem zeroImportOp_diagonal (g : Op) (X : System) (hX : X.witnessed)
    (hg : zeroImportOp g) :
    (sector (apply g X) = sector X ∧ dir (apply g X) hX = dir X hX) ∨
    (sector (apply g X) = -sector X ∧ dir (apply g X) hX = -dir X hX) := by
  have hm : g.m = 1 := hg
  rcases Int.units_eq_one_or g.e with he | he
  · left
    constructor
    · rw [sector_apply, he, one_mul]
    · rw [dir_apply, hm, he, one_mul, one_mul]
  · right
    constructor
    · rw [sector_apply, he, neg_one_mul]
    · rw [dir_apply, hm, he, one_mul, neg_one_mul]

theorem split_costs_one (g : Op) (X : System) (hX : X.witnessed)
    (h0 : importCost X = 0) (hs : splits g X hX) :
    importCost (apply g X) = 1 := by
  have hm : g.m = -1 := (splits_iff_paid g X hX).mp hs
  have hxmu : X.mu = 1 := (importCost_zero_iff_mu_one X).mp h0
  have htarget : (apply g X).mu = -1 := by
    show g.m * X.mu = -1
    rw [hm, hxmu, mul_one]
  rw [importCost, htarget]
  simp

theorem abstract_accounting (g : Op) (X : System) (hX : X.witnessed) :
    (zeroImportOp g → ¬ splits g X hX) ∧
    (splits g X hX ↔ g.m = -1) ∧
    (importCost X = 0 → splits g X hX → importCost (apply g X) = 1) := by
  exact ⟨fun hg => no_zeroImport_split g X hX hg,
    splits_iff_paid g X hX,
    fun h0 hs => split_costs_one g X hX h0 hs⟩

end CoflipAbstract
end GUFormalization
