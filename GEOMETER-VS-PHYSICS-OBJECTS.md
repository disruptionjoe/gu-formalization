# GU objects: the geometer's construction vs the physics default (read before attacking any GU object)

Standing reference for every team/agent working GU. Geometric Unity is a GEOMETER'S program (Weinstein):
many of its objects have a geometric construction that DIFFERS from the standard physics version of the
"same-named" object. Using the physics version leads teams into FALSE WALLS -- apparent inconsistencies,
ghosts, or no-gos -- that the geometer's version does not have, because the geometer's object is built
differently. Before you conclude "GU is dead / blocked / inconsistent" on any object below, check that you
used the GEOMETER'S version. This has already saved the program from multiple false kills.

| Object | Physics default (the FALSE WALL) | Geometer's version (how GU actually builds it) | Wall avoided |
|---|---|---|---|
| **Gauge group** | "Sp(64)"; or "non-compact -> non-unitary -> inconsistent" | **Sp(32,32;H)**, the non-compact real form -- and the non-compactness IS the Krein/indefinite form, a feature not a bug (Branch 5: non-compactness == the Krein form, one datum) | Do not reject GU for a "non-unitary non-compact group"; the Krein structure is the point |
| **Ghost clearance** | REMOVE the ghost (SUSY positivity `{Q,Q^dag}=2H>=0`, or project to a positive Hilbert subspace) | **KEEP-AND-GRADE** the ghost via the Krein form `[P,S]=0` (P = Cartan involution of so(9,5)) / Bateman-Turok hidden parity -- an indefinite-metric (PT/Krein) consistency, NOT a positive Hilbert space (Branch 3: GU clears its ghost the anti-SUSY way) | Do not look for SUSY / positive-H positivity; GU's consistency is Krein-graded |
| **Signature (9,5)** | 5 timelike directions -> ghosts, no unitary Hilbert space, inconsistent | The (9,5) ambient IS the geometry; the 5 times force an INDEFINITE (Krein) invariant form `(+64,-64)`, exactly what GU is built on -- positive-definiteness was never claimed (Branch 5: obstructs only Hilbert positivity, which the Krein apparatus absorbs) | Do not kill GU for "multi-time" |
| **Graded / guardian symmetry** | super-Poincare, `{Q,Q} ~ P_mu` (spacetime SUSY) | **super-IG**: a graded extension of the internal gauge group IG, `{Q,Q} ~ Omega^1(ad)` = the SPIN CONNECTION, not `P_mu` (Branch 5, decisive) | A team hunting spacetime SUSY concludes "no guardian"; the geometer's graded object is a distinct (local-Lorentz-graded) thing |
| **Generation count** | an INDEX in Z (Dirac / Atiyah-Singer / a signature) | a TORSION class in the 3-primary arena `Z/3 subset pi_3^s = Z/24`; `Hom(Z/3, Z) = 0`, so a Z-index provably CANNOT reach it (H6) | Do not try to force the count with a Z-valued index; and "odd" (mod-2) != the count (mod-3) |
| **Gravity functional** | pick an `R^2 / Weyl^2` Lagrangian (free model-building) | **`|II|^2`**, the full second-fundamental-form norm of the embedding `X^4 -> Y^14`, via the Gauss identity `|II|^2 = |H|^2 - R^X`; Einstein-Hilbert is INDUCED, not added | Do not treat it as free Lagrangian-building; the induced `|II|^2` (with its Einstein term) is what makes GU survive the rotation-curve refutation (H49) -- pure conformal `|H|^2` dies |
| **The scale mu_DW** | a mass parameter to be measured / fixed | the DeWitt/gimmel metric scale -- the scale-covariant geometry fixes only DIMENSIONLESS RATIOS, so the overall scale is STRUCTURALLY free, not merely unmeasured (H24) | Do not expect the geometry to hand you mu_DW; it is a ratio-only structure |
| **The metric** | THE spacetime metric `g` | the gimmel/DeWitt metric on `Y^14 = Met(X^4)`; the vertical block is the TRACE-REVERSED Frobenius fiber `(7,3) -> (6,4)`. There are TWO metrics (base + fiber) and an action relating them | Do not conflate the base spacetime metric with the fiber metric-on-metrics |
| **The RS cure / soldering** | a Porrati-Rahman non-minimal `F`-analytic VERTEX | a KINEMATIC `ker Gamma` PROJECTOR (`g=1` full projection, Spin(9,5)-equivariant) = the gravitino gauge condition realized geometrically (Branch 4: 4/5 axes match de Wit-Freedman; the one differing axis is exactly equivariant-vs-not) | The geometer's equivariant projector is not the physicist's field-strength vertex; the difference IS the guardian axis |

## The general rule (transferable to any geometric/foundational program)

When a program is built on a NON-STANDARD primitive, each object has the program's NATIVE construction, which
may look like a standard-field object of the same name but is built differently. Using the standard-field
default produces false walls precisely where the native construction diverges. Always ask: what is the
GEOMETER'S (program's-native) version of this object, and does the apparent wall exist in THAT version? For
GU the recurring native features are: indefinite/Krein rather than positive Hilbert; torsion (3-primary)
rather than integer/index; induced rather than added; ratio-only rather than scale-fixed; graded-internal
(super-IG) rather than graded-spacetime (super-Poincare); metric-on-metrics rather than a single metric.

## For orchestrators

Include a condensed form of this table in the shared context of EVERY GU team/branch brief, so no team burns a
swing hitting a physics-version wall the geometer's version does not have. If a team reports a no-go/kill,
check it re-derived the object in the geometer's version before believing it.
