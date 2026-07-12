# Path 2: the keep-and-grade loop-positivity theorem -- scope + blind-branch wave design

**Status:** SETUP (not yet deployed). Blockbuster path 2 from the strategy map. GU-INDEPENDENT framing by
design -- the value does not require accepting GU. Serves H59 (GU's terminal UV question) but is written so a
skeptic who rejects GU still has a reason to read it.

## 1. The problem, stated GU-independently

Higher-derivative (4th-order, Stelle-type) gravity is **renormalizable** and **asymptotically free** (established
classically; and, for the GU-specific ker-Gamma Rarita-Schwinger extension, by the UV arc Waves 42-47). The
price is a massive spin-2 **ghost**: a state of negative Krein norm. The textbook verdict is that this ghost
breaks unitarity (negative probabilities) and kills the theory as a fundamental one.

The **keep-and-grade** rescue (Krein / PT-symmetric / indefinite-metric; also the GU `[P,S]=0` Bateman-Turok
hidden parity) proposes NOT to remove the ghost but to equip the state space with an indefinite metric and a
grading/`C`-operator so that (a) the physical inner product is positive on observable states and (b) the
S-matrix is unitary with respect to it. **At TREE level this demonstrably works** (Bender-Mannheim PT quantum
mechanics of the Pais-Uhlenbeck oscillator; Mannheim's conformal-gravity program; Bateman-Turok tree-level
positivity / hidden parity). 

**The open question (the prize):** does the keep-and-grade rescue survive at LOOP level? No general loop-level
proof exists for any theory in this class. This is a decades-old objection to higher-derivative gravity, and our
own UV arc just made it the **single remaining barrier**: with the couplings shown well-behaved (asymptotically
free), loop positivity is now the ONLY thing between "4th-order gravity" and "UV-complete unitary quantum
gravity." A general resolution -- proof OR clean no-go -- is a blockbuster because it decides an entire class of
theories (Stelle gravity, conformal gravity, agravity, GU), not one model.

### The decidable sub-questions (what "survives at loop level" means, precisely)
- **Q-cut:** Do the negative-norm states stay decoupled from the unitarity cuts (Cutkosky / optical theorem) at
  one loop and beyond? (Does the ghost contribute to the imaginary part of physical amplitudes?)
- **Q-pos:** Does the grading/`C`-operator that defines the positive physical inner product survive
  renormalization -- i.e. does a consistent positive-definite physical subspace exist at all loop orders?
- **Q-caus:** Is the loop-consistent construction also Lorentz-invariant and micro-causal, or is unitarity
  bought at the price of causality (the known tension in some rescues)?
A YES on all three for some construction = the theory is a genuine UV-complete unitary QG. A rigorous NO (an
explicit obstruction) = a class-level kill. Either is the blockbuster.

## 2. Why the blind-branch method fits THIS problem exactly

The construction-fork discipline (this repo's standing rule) says: when an object has several possible
constructions, identify which you use, stay open on which side the answer lives, and never default. Here the
**branches ARE the rival constructions** of "make the ghost consistent." They genuinely disagree, they are
pursued by different communities, and no one knows which (if any) works at loops. Running them BLIND to each
other prevents premature convergence onto whichever construction is currently fashionable -- exactly the failure
the guardian wave (Waves 37-41) showed the blind architecture prevents. The wave's job is to find which
construction (if any) achieves loop positivity, and at what cost.

## 3. The five branches (each a rival construction; each blind to the others)

**Branch A -- Cutkosky / unitarity-cut (the most direct test).** Compute the one-loop cuts of the 4th-order
graviton propagator (self-energy, the box/triangle with internal ghost) and check the optical theorem on the
physical subspace: does the negative-norm ghost contribute to `Im M`, or does the largest-time equation /
Veltman cutting confine it? Formalism: Cutkosky rules, largest-time equation, in the indefinite (Krein) metric.
Verdict target: Q-cut at one loop.

**Branch B -- PT / `C`-operator (Bender-Mannheim).** Construct the `C`-operator (the grading that defines the
positive PT inner product) for the *interacting* 4th-order theory and test whether it survives loops /
renormalization -- equivalently, whether the similarity transformation to an isospectral Hermitian Hamiltonian
exists order by order and stays local/relativistic. Formalism: PT-symmetric QFT, similarity transform. Verdict
target: Q-pos (and Q-caus, since the equivalent-Hermitian theory's locality is the crux critics attack).

**Branch C -- Fakeon prescription (Anselmi-Piva).** Adopt the fakeon quantization -- the ghost is neither a
physical particle nor a standard ghost, but a "fake" degree removed by a special average-continuation
prescription at loops. Test whether it delivers loop unitarity, and price it honestly (Anselmi's fakeons are
known to buy unitarity at the cost of micro-causality violation at the fakeon scale). Formalism: fakeon average
continuation, arithmetic of the threshold prescription. Verdict target: Q-cut + Q-caus (this branch is expected
to trade Q-caus for Q-cut -- quantify the trade).

**Branch D -- Lee-Wick / complex-pole (Donoghue-Menezes; Grinstein-O'Connell-Wise).** Treat the ghost as an
unstable resonance with complex-conjugate poles; recover unitarity via Cutkosky rules deformed onto the complex
poles. Test whether the 4th-order gravity (+ RS) ghost can BE a Lee-Wick resonance and whether that preserves
loop unitarity and (perturbative) causality. Formalism: Lee-Wick QFT, complex-pole cutting. Verdict target:
Q-cut + Q-caus via the complex-pole route.

**Branch E -- Adversarial red-team / no-go (the kill attempt).** Do NOT try to make the rescue work; try to
PROVE it FAILS. Construct the explicit obstruction: a physical process where negative probability leaks, a cut
that unavoidably picks up the ghost, a proof the `C`-operator is non-local / the equivalent Hermitian theory is
non-relativistic (the standard critique of PT-QFT), or an inconsistency of the grading under renormalization.
Formalism: whatever breaks it -- locality theorems, spectral positivity bounds, explicit counter-amplitudes.
Verdict target: a rigorous NO, or (by failing to find one) evidence the rescue is robust.

Blindness matters most here: A-D each want their construction to win; E wants everything to lose. If A-D
converge on a construction that survives E's specific attack, that is the proof-of-concept. If E finds an
obstruction that A-D's constructions share, that is the class-level kill.

## 4. Team composition (each branch = one worker running a bespoke 5-persona team INLINE)

Per this program's standing rule (personas always inline, never fanned out per-agent): each branch is a SINGLE
agent that runs its five-persona team sequentially inside one context, then reports the team's converged verdict.
Five agents total (A-E), parallel, mutually blind.

The 5-persona template (specialize persona 1 per branch's formalism; 2-5 are constant):
1. **The formalism specialist** -- the expert in this branch's construction (the Cutkosky/cutting expert for A;
   the PT-QFT / `C`-operator expert for B; the fakeon expert for C; the Lee-Wick expert for D; the
   locality/no-go theorist for E). Does the actual computation/argument.
2. **The mathematical-physics referee** -- demands rigor, not plausibility; grades every claim (proven /
   argued / conjectured); flags where a step is one-loop-only vs all-orders, perturbative vs non-perturbative.
3. **The adversary** -- attacks the branch's OWN emerging claim (intra-team red-team, distinct from Branch E's
   whole-wave red-team): "here is the process that would break what you just argued."
4. **The cross-checker** -- independent second derivation / sanity limit (the two-derivations discipline that
   caught the M^2/r^2 bug in the gravity arc): a decoupling limit, a known QM result the QFT must reduce to, a
   different regulator.
5. **The synthesizer** -- states the branch verdict on {Q-cut, Q-pos, Q-caus}, a confidence grade, the single
   load-bearing assumption, and what one computation would firm it. Also states WHICH construction of the ghost
   the branch used and why (the fork-identification the wider synthesis needs).

Each team must: (a) state the construction it used for the ghost and for "unitarity" (fork discipline); (b) grade
its verdict honestly (proof / one-loop indication / plausibility); (c) name the one obstruction that would kill
its construction -- so the orchestrator can cross-test each branch against Branch E's findings.

## 5. Wave protocol (one wave = every branch swings once, in parallel, blind)

1. **Deploy** A-E in parallel, blind. Each returns a graded verdict on {Q-cut, Q-pos, Q-caus} + its
   construction + its one-killing-obstruction + a durable artifact (exploration + deterministic test where a
   computation was done).
2. **Orchestrator synthesis** (inline, the science-council lens): the high-level picture -- which constructions
   survived, which died, where they agree/disagree, and crucially cross-test: does Branch E's obstruction kill
   any of A-D? does any A-D construction evade it?
3. **Cross-share decision:** identify the learnings worth sharing between teams before a next wave (e.g. if B's
   `C`-operator locality result bears on C's causality trade), and design wave 2 (deeper on the surviving
   construction, or a focused kill on the contested one).
4. **Re-rank + capture:** update the council ranker; if the wave teaches a method move, capture it
   (ai-epistemology observation).

## 6. Honest pre-registration (what each outcome means, fixed BEFORE the wave)
- **A-D find a surviving construction that beats E:** proof-of-concept that keep-and-grade CAN work at (one)
  loop -- a strong, GU-independent, publishable result; NOT yet an all-orders proof.
- **E finds a class-shared obstruction:** a clean no-go killing keep-and-grade at loops for the whole class
  (Stelle/conformal/agravity/GU) -- also a blockbuster, and it would honestly close GU's UV North Star as a NO.
- **Split (some constructions survive, some die, causality-traded):** the most likely realistic outcome -- a
  precise MAP of which rescue costs what (unitarity vs causality vs locality), which is itself a real
  contribution and sets an unambiguous wave-2 target.
- **All inconclusive at one loop:** honest "frontier confirmed hard"; report the specific technical wall, do not
  dress it as progress.

DEPLOYMENT GATE: this is the setup. Deploy on Joe's Go.
