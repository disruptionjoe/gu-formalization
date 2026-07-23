# GU objects: the geometer's construction vs the physics default (read before attacking any GU object)

Standing reference for every team/agent working GU. Geometric Unity is a GEOMETER'S program (Weinstein):
many of its objects have a geometric construction that DIFFERS from the standard physics version of the
"same-named" object. THE RULE IS NOT "prefer the geometer's version." The rule is: when an object has BOTH a
known standard-field default AND a program-native construction, you must IDENTIFY which one you are using and
WHY -- because we do NOT know a priori on which side the answer lives. The failure mode is defaulting to
EITHER side unconsciously: using the physics version can hit a false wall the geometric object does not have;
using the geometric version can equally make you miss that the answer was on the physics side. The table below
records forks this program has ALREADY identified, and -- where determined -- which construction the answer
lives on and the reason. It is a map of where the two diverge and what we have settled, not a claim that one
side always wins.

Each row: the two constructions, and (in the last column) which side we determined the answer is on for THIS
object and why. Entries are settled forks; for an object NOT in this table, apply the rule below.

| Object | Standard physics construction | Geometer's (program-native) construction | Determined side + why |
|---|---|---|---|
| **Gauge group** | "Sp(64)"; or "non-compact -> non-unitary -> inconsistent" | **Sp(32,32;H)**, the non-compact real form -- and the non-compactness IS the Krein/indefinite form, a feature not a bug (Branch 5: non-compactness == the Krein form, one datum) | Do not reject GU for a "non-unitary non-compact group"; the Krein structure is the point |
| **Ghost clearance** | REMOVE the ghost (SUSY positivity `{Q,Q^dag}=2H>=0`, or project to a positive Hilbert subspace) | **KEEP-AND-GRADE** the ghost via the Krein form `[P,S]=0` (P = Cartan involution of so(9,5)) / Bateman-Turok hidden parity -- an indefinite-metric (PT/Krein) consistency, NOT a positive Hilbert space (Branch 3: GU clears its ghost the anti-SUSY way) | Do not look for SUSY / positive-H positivity; GU's consistency is Krein-graded |
| **Signature (9,5)** | 5 timelike directions -> ghosts, no unitary Hilbert space, inconsistent | The (9,5) ambient IS the geometry; the 5 times force an INDEFINITE (Krein) invariant form `(+64,-64)`, exactly what GU is built on -- positive-definiteness was never claimed (Branch 5: obstructs only Hilbert positivity, which the Krein apparatus absorbs) | Do not kill GU for "multi-time" |
| **Graded / guardian symmetry** | super-Poincare, `{Q,Q} ~ P_mu` (spacetime SUSY) | **super-IG**: a graded extension of the internal gauge group IG, `{Q,Q} ~ Omega^1(ad)` = the SPIN CONNECTION, not `P_mu` (Branch 5, decisive) | A team hunting spacetime SUSY concludes "no guardian"; the geometer's graded object is a distinct (local-Lorentz-graded) thing |
| **Generation count** | an integer index/rank in `Z` | a proposed torsion reading in the 3-primary arena `Z/3 subset pi_3^s = Z/24` | The relation is **unsettled**, not a settled native-side win. `Hom(Z/3,Z)=0` blocks a direct additive identification, so a separately constructed integer observable and bridge would be required. Keep both codomains typed and treat “torsion component -> integer 3” as the open question. |
| **Physical 4+10 carrier split** | Lorentzian `(3,1)+(6,4)` with reality/conjugation closure | compact/complexified `(4,0)+(5,5)` self-dual carrier used by the finite census | Do not transfer the packet silently. One Lorentzian Hodge half is complex dimension `192` but K-null and conjugation-exchanged; the computed stable closure is dimension `384`, signature `(192,192)`. The compact packet remains useful but is not the same physical-real-form object. |
| **Gravity functional** | pick an `R^2 / Weyl^2` Lagrangian (free model-building) | **`|II|^2`**, the full second-fundamental-form norm of the embedding `X^4 -> Y^14`, via the Gauss identity `|II|^2 = |H|^2 - R^X`; Einstein-Hilbert is INDUCED, not added | Do not treat it as free Lagrangian-building; the induced `|II|^2` (with its Einstein term) is what makes GU survive the rotation-curve refutation (H49) -- pure conformal `|H|^2` dies |
| **The scale mu_DW** | a mass parameter to be measured / fixed | the DeWitt/gimmel metric scale -- the scale-covariant geometry fixes only DIMENSIONLESS RATIOS, so the overall scale is STRUCTURALLY free, not merely unmeasured (H24) | Do not expect the geometry to hand you mu_DW; it is a ratio-only structure |
| **The metric** | THE spacetime metric `g` | the gimmel/DeWitt metric on `Y^14 = Met(X^4)`; the vertical block is the TRACE-REVERSED Frobenius fiber `(7,3) -> (6,4)`. There are TWO metrics (base + fiber) and an action relating them | Do not conflate the base spacetime metric with the fiber metric-on-metrics |
| **The RS cure / soldering** | a Porrati-Rahman non-minimal `F`-analytic VERTEX | a KINEMATIC `ker Gamma` PROJECTOR (`g=1` full projection, Spin(9,5)-equivariant) = the gravitino gauge condition realized geometrically (Branch 4: 4/5 axes match de Wit-Freedman; the one differing axis is exactly equivariant-vs-not) | The geometer's equivariant projector is not the physicist's field-strength vertex; the difference IS the guardian axis |

## The rule (the discipline, transferable to any geometric/foundational program)

When a program is built on a NON-STANDARD primitive, an object can have both a standard-field construction and
the program's native construction. The discipline:
1. IDENTIFY the fork. Notice when the object you are manipulating has two possible constructions.
2. NAME which one you are using, and WHY. State it explicitly in the work.
3. STAY OPEN on which side the answer is. We do not know a priori. Some forks resolve native, some standard;
   the table above lists the ones settled so far, each with its reason.
4. A no-go / kill is only as strong as the construction it was derived in. If you reach one, identify the
   construction and check whether it survives in the OTHER -- a physics-version wall may be an artifact, and a
   native-version result may fail to transfer. Do NOT believe a kill until you know which construction it
   lives in and why that is the applicable one.
5. NEVER default silently -- to either side. Defaulting to the physics version hits false walls; defaulting to
   the geometer's version makes you miss cases where the standard object is the right one.
For GU the recurring native features (the ones the table settled toward the geometric side) are:
indefinite/Krein rather than positive Hilbert; torsion (3-primary) rather than integer/index; induced rather
than added; ratio-only rather than scale-fixed; graded-internal (super-IG) rather than graded-spacetime
(super-Poincare); metric-on-metrics rather than a single metric. These are settled results, not a standing
preference -- the next object may go the other way.

## For orchestrators

Include a condensed form of this table AND the rule in the shared context of EVERY GU team/branch brief, so no
team burns a swing by silently defaulting to one construction. Require teams to STATE which construction they
used for each load-bearing object and why. If a team reports a no-go/kill, do not accept it until you know
which construction it was derived in and whether it survives in the other -- the wall may be a physics-version
artifact, or the kill may be real only for one construction while the answer lives on the side they did not
check.
