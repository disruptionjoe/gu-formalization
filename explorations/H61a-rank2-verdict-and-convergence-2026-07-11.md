# The rank-2 Krein Tomita-Takesaki verdict, and the convergence it forces

The make-or-break for the observer conjecture's critical path (does Shulman's Pi_1 indefinite-metric Tomita
theorem extend beyond rank 1?) came back PARTIAL-CONDITIONAL -- and the CONDITION turns out to be a question the
program has ALREADY been asking, which unifies two North Stars.

## 1. The verdict

Shulman's Pi_1 Tomita theorem neither cleanly extends nor cleanly obstructs at rank 2. The full modular skeleton
(J^2=1, J M J = M', Krein-antiisometry, Delta^{it}-covariance, the eta-positive polar decomposition S = J
Delta^{1/2}) **extends to Pi_2 IF AND ONLY IF the Krein modular operator `Delta = S^+ S` has real-positive
spectrum ("modular-PT-unbroken"); it obstructs on the exceptional / non-real (PT-broken) locus.** All four
properties were verified on a genuine rank-2 model in the unbroken regime (W77, residuals <1e-15), so extension
is POSSIBLE -- not a universal no-go.

**Precise obstruction (why rank 2 differs from rank 1):** by Langer's Pontryagin definitizable-operator theory
the non-positive-type defect of `Delta` is bounded by the rank kappa -- Pi_1 caps at one non-real pair, Pi_2
reaches two. Shulman's SINGLE quasivector patches exactly the <=1-dim Pi_1 defect (that is the whole content of
his theorem); Pi_2's 2-dim defect cannot be patched by one quasivector, and there the modular CONJUGATION is the
leading-edge failure. Generalizes to all rank >= 2. No Pi_kappa (kappa>=2) Tomita conjugation theorem exists in
the literature (Shulman 1997 is the state of the art; Gottschalk 2002 = the flow only).

**Key correction over the H61 first swing:** W67/W74 used the HILBERT modular operator (always positive,
grading-independent) -- the decisive object is the KREIN `Delta = S^+ S` built from the Krein adjoint
`a^+ = eta a* eta`, which is eta-selfadjoint and CAN go non-real. The earlier "rank-stability" was the unbroken
interior; it never computed the spectrum that decides the fork.

## 2. The convergence (the important part)

The condition "is `Delta = S^+ S` modular-PT-unbroken (real-positive spectrum)?" is EXACTLY the exceptional /
Jordan-locus question the program already located three times, now seen to be one question:
- **path 2 loop positivity** (the keep-and-grade Krein rescue is consistent iff the grading stays PT-unbroken);
- **Branch E's exceptional-Jordan locus** (W52 -- the positivity-defining grading degenerates on a codim-1
  exceptional locus);
- **W53's AF-flow-vs-locus** (does the asymptotically-free RG trajectory reach the exceptional locus?).

So **the observer conjecture's critical path and GU's UV loop-positivity are the SAME question** -- both reduce to
"does the modular/grading operator's spectrum stay real-positive (PT-unbroken) along the flow, or reach the
exceptional locus?" This unifies the two North Stars: proving GU is loop-positive IS proving the observer
conjecture's Krein-TT leg, and vice versa.

## 3. The partial answer already in hand

W53 (path-2 wave-2) already partially answered this exact question: the spin-2 grading is **PT-unbroken across the
entire interacting regime** (it reaches the exceptional locus `m2^2=0` only at the free UV fixed point, where the
ghost decouples); the sole shadow is the **spin-0 conformal mode** (the negative fixed-ratio `f_0^2/f_2^2<0` --
the classic conformal-factor problem, plausibly a gauge artifact). Carrying this over: **GU is plausibly
modular-PT-unbroken in the spin-2 sector -> Krein-TT extends there -> the observer conjecture's payoff theorem
(H63) holds on the spin-2 sector across the interacting regime**, with the spin-0 conformal-factor mode the
single residual open question -- the SAME residual that has stood since path 2.

## 4. Status and next step

The conjecture is NOT killed (extension is possible and demonstrated in the unbroken regime) and NOT proven
(GU's landing in the unbroken class is the residual open computation). It is CONDITIONALIZED precisely, and the
condition is unified with the loop-positivity North Star, with a partial positive answer (spin-2 unbroken).
For H63: re-found the payoff theorem on the algebraic (flow+conjugation) skeleton IN THE UNBROKEN REGIME, stating
"spectrum(Delta) real-positive" as an explicit postulate, and couple the residual "is GU unbroken?" to the single
open RG computation shared with path 2 / Branch E / W53. The finite type-I toy cannot decide it (J-symmetry of
M_d(C) forces the unbroken interior); the decision lives in the genuinely-indefinite, infinite-rank, type-III /
conformal-mode regime -- the one open computation the whole UV+observer program now shares.

Honest register unchanged: the Curie/genericity caveat stands (a GU-independent theorem about observers +
symmetry-breaking, of which GU is one instance).
