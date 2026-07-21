"""
Aggregation / Condorcet probe over the two boundary-meaning councils
(science 5-member + systems 7-member = 12 personas as voters).

Deterministic, no RNG. Ballots are hard-coded (elicited in-character in the
aggregation artifact). Computes, for STEELMEN (strict ballots) and for the
QUESTION FINALISTS (weak-order ballots, ties = 0.5 pairwise):
  - pairwise majority matrix
  - Condorcet winner if one exists, else Copeland ordering + Smith set
Also computes the confidence-weighted steelman ranking and its agreement /
divergence vs the Condorcet/Copeland ordering.

Run foreground; prints exit note at end.
"""

import itertools

# ----------------------------------------------------------------------
# 12 STEELMEN (author labels)
# ----------------------------------------------------------------------
STEEL = ["ORTH","HET","COM","WILD","PHIL","ZK","NEU","HASH","META","FLP","MMO","INFO"]

# Strict preference ballots over the 12 steelmen, one per persona-voter.
# "which best captures what the missing piece really is." (author ranks own -> noted)
STEEL_BALLOTS = {
 "ORTHODOX":   ["ORTH","INFO","FLP","COM","PHIL","NEU","META","HET","ZK","HASH","MMO","WILD"],
 "HETERODOX":  ["HET","WILD","FLP","PHIL","INFO","ZK","NEU","HASH","META","ORTH","MMO","COM"],
 "COMMERCIAL": ["COM","INFO","ORTH","FLP","PHIL","NEU","ZK","META","HASH","HET","MMO","WILD"],
 "WILD":       ["WILD","HET","PHIL","FLP","INFO","ZK","NEU","HASH","META","ORTH","COM","MMO"],
 "PHILOSOPHER":["PHIL","INFO","FLP","ORTH","COM","HET","NEU","ZK","WILD","META","HASH","MMO"],
 "ZKFHE":      ["ZK","INFO","FLP","HET","PHIL","ORTH","NEU","WILD","HASH","META","COM","MMO"],
 "NEURAL":     ["NEU","INFO","ORTH","FLP","META","PHIL","HET","ZK","HASH","WILD","COM","MMO"],
 "HASHGRAPH":  ["HASH","HET","FLP","INFO","META","ORTH","PHIL","WILD","NEU","ZK","MMO","COM"],
 "METASTABLE": ["META","NEU","INFO","FLP","ORTH","HASH","HET","PHIL","ZK","WILD","MMO","COM"],
 "FLP":        ["FLP","INFO","PHIL","ORTH","HET","ZK","WILD","NEU","COM","META","HASH","MMO"],
 "MMO":        ["MMO","FLP","INFO","HET","ZK","ORTH","PHIL","HASH","META","NEU","WILD","COM"],
 "INFO":       ["INFO","FLP","PHIL","ORTH","NEU","HET","ZK","COM","WILD","META","HASH","MMO"],
}

# author of each steelman (the ballot whose #1 is a self-vote)
STEEL_AUTHOR = {"ORTH":"ORTHODOX","HET":"HETERODOX","COM":"COMMERCIAL","WILD":"WILD",
 "PHIL":"PHILOSOPHER","ZK":"ZKFHE","NEU":"NEURAL","HASH":"HASHGRAPH","META":"METASTABLE",
 "FLP":"FLP","MMO":"MMO","INFO":"INFO"}

# confidence-weighting inputs (author confidence %, MODE)
CONF = {  # (confidence, mode)
 "ORTH":(80,"EXACT"), "HET":(55,"MIXED"), "COM":(70,"EXACT"), "WILD":(40,"MIXED"),
 "PHIL":(62,"MIXED"), "ZK":(55,"MIXED"), "NEU":(60,"MIXED"), "HASH":(45,"ANALOGY"),
 "META":(50,"ANALOGY"), "FLP":(72,"MIXED"), "MMO":(35,"ANALOGY"), "INFO":(80,"EXACT"),
}
MODE_W = {"EXACT":1.0,"MIXED":0.6,"ANALOGY":0.3}

# ----------------------------------------------------------------------
# 36 QUESTIONS: 12 personas x (Q1,Q2,Q3). Scores 1-5 per persona.
# rows = question id; the 12 columns are the personas in PERSONAS order.
# ----------------------------------------------------------------------
PERSONAS = ["ORTHODOX","HETERODOX","COMMERCIAL","WILD","PHILOSOPHER","ZKFHE",
            "NEURAL","HASHGRAPH","METASTABLE","FLP","MMO","INFO"]

# question id -> short label
QLABEL = {
 "O1":"true-end deficiency indices: is limit-point/theta-dissolves a THEOREM not a lean?",
 "O2":"is sigma a genuine DHR superselection charge (statistics/dimension invariants)?",
 "O3":"any observable OTHER than DE-sign riding sigma; can two sectors interfere (Aharonov-Susskind)?",
 "H1":"is the co-flip weld (sigma=record arrow) EXACT at operator grade on the true fiber, not just collar?",
 "H2":"does record direction = Tomita-Takesaki modular flow / thermal time (Connes-Rovelli)?",
 "H3":"is the felt arrow of time literally the alpha-odd lift; opposite-sector observer reversed arrow?",
 "C1":"can priced-separation + 'DE-sign is a free Z/2' be written up TODAY as a finite-dim Krein paper?",
 "C2":"is the internal-audit method portable to other sign/orientation ambiguities (pseudo-Herm, lattice sign)?",
 "C3":"is provable irreducible-input bit-count a measurable property/currency to compare rival unifications?",
 "W1":"does the L1 assembly lemma hold -> sigma-blindness a bona fide Lawvere fixed-point instance not analogy?",
 "W2":"is 'outside' a finality/closure horizon (causal-past retraction), changing missing piece Z/2 -> direction?",
 "W3":"is 'the outside' the SAME outside for all self-encoding worlds; is that what a law of physics secretly is?",
 "P1":"is the Sec-4.2 standpoint dichotomy provably EXHAUSTIVE -> externality upgrades lean->theorem?",
 "P2":"indexical necessity vs disguised selection-effect; what obs distinguishes irreducibly-external?",
 "P3":"first physical demonstrably-undecidable-from-within fact; vindicate/refute complete 3rd-person TOE?",
 "Z1":"does co-flip satisfy the homomorphic-NOT law (involution commuting with encryption)?",
 "Z2":"is there a decryption-KEY object; is the missing bit a withheld KEY (missing-key vs missing-value)?",
 "Z3":"can GU host a ZK proof a valid sector EXISTS without exhibiting which; who is the verifier?",
 "N1":"is the Z/2 an exact disconnected two-minimum (true SSB) or a continuous Hessian-flat direction?",
 "N2":"is there a GU physical-Hessian/curvature measuring sector robustness; distinguishes sigma from tau?",
 "N3":"are sigma,tau,theta the entire UNTRAINABLE parameter set; bit-size a fundamental sloppiness signature?",
 "G1":"is the record arrow a Z/2 orientation of an internal event-DAG, or provably NO internal DAG?",
 "G2":"is the obstruction a 'fault' GU's network has; GU's crash-failure blocking internal consensus?",
 "G3":"sigma-blindness = no node can timestamp its OWN sector-choice (self-referential ordering paradox)?",
 "MS1":"is sigma EXACTLY degenerate or infinitesimally biased; any quantity dynamically breaks the tie?",
 "MS2":"what external perturbation historically selected OUR sector; same 'outside' as other lenses?",
 "MS3":"could decohered branches occupy BOTH sectors; is sigma a superselection ADDRESS not a coin-flip?",
 "F1":"exact oracle CLASS sigma needs: is 1 Z/2 the WEAKEST failure-detector (Chandra-Toueg); tau stronger?",
 "F2":"is the obstruction async-consensus impossibility whose faulty process is the observer's causal FUTURE?",
 "F3":"is first-person-ness the failure-detector reality is FORCED to instantiate to be definite?",
 "MM1":"is there a real third-person authoritative-state object the first person provably can't reach?",
 "MM2":"is sigma a per-observer SHARD assignment or a GLOBAL server choice (one-anchor vs many)?",
 "MM3":"is sigma-blindness an ANTI-CHEAT guarantee; physical law as consistency-preserving netcode?",
 "I1":"is the right quantity a Hartley bit (cardinality) or a Shannon bit (needs a prior)?",
 "I2":"is inward capacity provably 0; does hosting impose a 1-bit CEILING forbidding imports beyond sigma,tau?",
 "I3":"is total external bit-budget (sigma+tau+theta) a conserved fundamental INFORMATION CHARGE?",
}

# 12 scores per question, ordered as PERSONAS
SCORES = {
 "O1":[5,3,4,3,4,2,3,2,2,3,2,4],
 "O2":[5,3,3,2,3,3,3,2,2,3,2,3],
 "O3":[4,4,2,4,3,2,2,2,3,2,2,2],
 "H1":[3,5,2,4,4,3,2,3,2,3,2,3],
 "H2":[4,5,2,4,3,2,2,3,2,3,2,3],
 "H3":[1,5,1,5,3,2,2,3,2,2,2,2],
 "C1":[3,2,5,1,3,2,2,2,2,3,2,3],
 "C2":[3,2,5,2,3,3,3,2,2,3,2,3],
 "C3":[3,3,5,4,3,3,3,3,3,4,3,5],
 "W1":[3,4,2,5,4,3,2,2,2,4,2,3],
 "W2":[2,4,1,5,3,2,2,3,2,4,2,3],
 "W3":[1,4,1,5,3,3,3,3,3,3,3,3],
 "P1":[4,5,4,5,5,4,3,3,3,5,3,4],
 "P2":[2,4,2,4,5,3,2,3,2,4,3,3],
 "P3":[2,4,3,5,5,3,3,3,3,5,3,4],
 "Z1":[2,3,2,2,2,5,2,2,2,2,2,2],
 "Z2":[1,3,2,3,3,5,2,2,2,3,3,3],
 "Z3":[1,3,2,5,3,5,2,3,2,3,3,3],
 "N1":[4,3,3,2,3,2,5,2,5,3,2,3],
 "N2":[3,2,3,2,2,2,5,2,4,2,2,3],
 "N3":[3,3,4,5,3,3,5,3,4,3,3,4],
 "G1":[2,3,2,2,3,2,2,5,2,3,3,2],
 "G2":[1,2,2,2,2,2,2,5,3,4,3,2],
 "G3":[1,4,1,5,3,3,2,5,3,4,3,3],
 "MS1":[4,3,3,2,4,2,5,3,5,3,2,4],
 "MS2":[3,3,2,3,3,2,4,3,5,3,3,3],
 "MS3":[3,3,2,5,3,2,4,3,5,2,3,3],
 "F1":[3,3,4,3,4,4,3,4,3,5,4,5],
 "F2":[2,4,2,5,3,2,2,4,3,5,3,3],
 "F3":[1,5,1,5,4,3,3,3,3,5,4,4],
 "MM1":[2,2,2,1,3,3,2,3,2,3,5,2],
 "MM2":[2,2,2,2,2,2,2,2,3,2,5,2],
 "MM3":[1,2,1,3,2,4,1,2,2,2,5,2],
 "I1":[4,3,4,3,5,4,4,3,3,4,3,5],
 "I2":[4,3,4,3,4,4,4,3,3,5,4,5],
 "I3":[3,3,5,5,3,3,5,3,3,4,3,5],
}

# ----------------------------------------------------------------------
# Weak-order ballots over the finalists are DERIVED from SCORES:
# each persona prefers higher score; equal scores => tie (0.5 pairwise).
# ----------------------------------------------------------------------

def pairwise_strict(ballots, cands):
    """ballots: dict name->ordered list (strict). Returns wins[a][b] = #voters a>b."""
    wins = {a:{b:0.0 for b in cands} for a in cands}
    for order in ballots.values():
        pos = {c:i for i,c in enumerate(order)}
        for a,b in itertools.permutations(cands,2):
            if pos[a] < pos[b]:
                wins[a][b]+=1
    return wins

def pairwise_scored(qids, cands):
    """cands are question ids; each persona scores; tie=0.5."""
    wins = {a:{b:0.0 for b in cands} for a in cands}
    for pi in range(len(PERSONAS)):
        for a,b in itertools.permutations(cands,2):
            sa, sb = SCORES[a][pi], SCORES[b][pi]
            if sa>sb: wins[a][b]+=1
            elif sa==sb: wins[a][b]+=0.5
    return wins

def analyze(wins, cands, nvoters):
    thr = nvoters/2.0
    # Condorcet winner: beats all others in pairwise majority
    condorcet=None
    for a in cands:
        if all(wins[a][b] > wins[b][a] for b in cands if b!=a):
            condorcet=a; break
    # Copeland score: +1 win, +0.5 tie
    cope={}
    for a in cands:
        s=0.0
        for b in cands:
            if b==a: continue
            if wins[a][b] > wins[b][a]: s+=1
            elif wins[a][b]==wins[b][a]: s+=0.5
        cope[a]=s
    order=sorted(cands,key=lambda c:(-cope[c], c))
    # Smith set: smallest dominating set (top cycle)
    def beats_or_ties(a,b): return wins[a][b] >= wins[b][a]
    # compute via iterative: start from Copeland top, close under "someone beats"
    # Smith = minimal set S s.t. every member of S beats every non-member.
    smith=None
    for k in range(1,len(cands)+1):
        top=set(order[:k])
        if all(wins[a][b] > wins[b][a] for a in top for b in cands if b not in top):
            smith=order[:k]; break
    return condorcet, cope, order, smith

def show_matrix(wins, cands, labelmap=None):
    hdr = "        " + " ".join(f"{c[:5]:>6}" for c in cands)
    print(hdr)
    for a in cands:
        row=" ".join(f"{wins[a][b]:>6.1f}" if b!=a else f"{'--':>6}" for b in cands)
        print(f"{a[:6]:>7} {row}")

NV=12
print("="*70)
print("STEELMEN  (12 strict ballots, 12 candidates)")
print("="*70)
sw = pairwise_strict(STEEL_BALLOTS, STEEL)
show_matrix(sw, STEEL)
cw, cope, order, smith = analyze(sw, STEEL, NV)
print("\nCondorcet winner:", cw if cw else "NONE (cycle at top)")
print("Copeland ordering (score):")
for c in order: print(f"   {c:5} {cope[c]:.1f}")
print("Smith set:", smith)

print("\n" + "="*70)
print("CONFIDENCE-WEIGHTED steelman ranking  (conf% x mode_weight)")
print("="*70)
cwt = {s:CONF[s][0]*MODE_W[CONF[s][1]] for s in STEEL}
cwt_order = sorted(STEEL, key=lambda s:(-cwt[s], s))
for s in cwt_order:
    print(f"   {s:5} {cwt[s]:5.1f}   ({CONF[s][0]}% x {CONF[s][1]} {MODE_W[CONF[s][1]]})")

print("\nCONDORCET(Copeland) rank vs CONFIDENCE-WEIGHTED rank:")
cond_rank={c:i+1 for i,c in enumerate(order)}
cwt_rank={c:i+1 for i,c in enumerate(cwt_order)}
print(f"   {'steel':5} {'cond':>5} {'cwt':>5} {'delta':>6}")
for s in STEEL:
    d=cwt_rank[s]-cond_rank[s]
    print(f"   {s:5} {cond_rank[s]:>5} {cwt_rank[s]:>5} {d:>+6}")

print("\n" + "="*70)
print("QUESTION MEANS (all 36) -> pick top-10 finalists")
print("="*70)
means={q:sum(SCORES[q])/NV for q in SCORES}
mean_order=sorted(SCORES,key=lambda q:(-means[q],q))
for q in mean_order:
    tag=" <finalist" if False else ""
    print(f"   {q:4} {means[q]:.2f}")
FINALISTS = mean_order[:10]
print("\nFinalists (top-10 by mean):", FINALISTS)

print("\n" + "="*70)
print("QUESTION FINALISTS  (12 weak-order ballots from scores, ties=0.5)")
print("="*70)
qw = pairwise_scored(FINALISTS, FINALISTS)
show_matrix(qw, FINALISTS)
qc, qcope, qorder, qsmith = analyze(qw, FINALISTS, NV)
print("\nCondorcet winner:", qc if qc else "NONE (cycle at top)")
print("Copeland ordering (score):")
for c in qorder: print(f"   {c:4} {qcope[c]:.1f}   mean={means[c]:.2f}")
print("Smith set:", qsmith)

print("\nEXIT: probe completed OK (deterministic, no RNG).")
