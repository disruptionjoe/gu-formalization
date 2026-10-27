---
title: "K2106: Neutral autonomy with unbounded hidden generators"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source selection, relativistic apparatus or physical recovery
scripts:
  - tests/channel-swings/k2106_neutral_unbounded_domains_probe.py
---

# K2106: Neutral autonomy with unbounded hidden generators

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: conditional mathematical construction with explicit domain and approximation limits
carrier: finite visible fermion Fock space tensor a separable infinite hidden Hilbert space LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product ON=declared_positive_Hilbert_space
real_structure: complex adjoint; no source-selected real form
grading: visible U1-neutral algebra, not whole even algebra
action_owner: repository-construction -- supplied selfadjoint generator with its operator domain
target: strong neutral-algebra normalization and domain counterexample MAP-TYPE=intertwiner
```

[Conditional mathematics accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Source and object boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 and SC-META-53 are
UNCERTAIN; SC-META-56 DISAVOWS a mandatory odd-action prerequisite. These
supplied positive Hilbert apparatus/algebra models are not equation9.16.
K2021 supplies local R0/R1; a source-selected positive observed algebra,
state and dynamics still need construction. LT-SM8/LT-GR6b, source-register,
ledger0.263 and canon remain unchanged. Native2+1, total/observed chirality,
full20 and K/C accessibility are distinct debts. This is reverse-scaffold
conditional mathematics, with no GU recovery, novelty or external certification.

## 1. Strong autonomy has a domain-sensitive classification

[K2103](k2103-neutral-algebra-dynamics-2026-10-26.md) is finite-dimensional.
Here V has finite dimension d, F_r=wedge^r V, K is any separable nonzero
Hilbert space, and

    Hspace = direct-sum_(r=0)^d F_r tensor K,
    A = direct-sum_r B(F_r) tensor I_K.               (1)

Use the positive representation and bounded observed algebra as supplied
inputs. Let H be selfadjoint, possibly unbounded, U_t=exp(-itH). Exact
all-state neutral autonomy means U_t* A U_t=A for every real t. It holds
if and only if there are Hermitian finite matrices h_r and selfadjoint k_r
on K such that

    H = direct-sum_r (h_r tensor I + I tensor k_r),
    Dom H = direct-sum_r (F_r tensor Dom k_r).        (2)

The sums over r are FINITE; scalar shifts may be redistributed between
h_r and k_r. This is equality of selfadjoint operators and domains, not
only their differential expressions. A common hidden domain across r is
not required. Each finite-dimensional tensor domain means a finite sum of
K-valued coefficients lying in Dom k_r.

Proof. Automorphisms permute the finite minimal center projections Pi_r.
Strong continuity fixes each Pi_r for all t, so it reduces U_t and H.
The induced continuous automorphism group on each finite matrix algebra is
inner, alpha_t=Ad(exp(it h_r)); finite dimension makes the induced group
norm-continuous and its derivation bounded. Let
W_t=(exp(it h_r) tensor I)U_t on that block. It lies in the commutant
I tensor B(K). Since alpha_t(h_r)=h_r, U_t commutes with exp(is h_r),
so W_t is a strongly continuous GROUP, not an arbitrary cocycle. Stone's
theorem gives W_t=I tensor exp(-it k_r). This proves(2), including its
domain by bounded perturbation. The converse follows by exponentiation.
This avoids applying a formal commutator to an unverified operator core.

## 2. Spectrum and a measurable limit of shielding

The exact lower spectral edge is

    inf spectrum H = min_r [lambda_min(h_r)+inf spectrum k_r].  (3)

It may be minus infinity. Each block is a finite direct sum of shifted k_r;
therefore H is semibounded exactly when every k_r is semibounded. All visible
neutral dynamics depend only on h_r, not on k_r. Sector-dependent hidden
interactions are allowed, and a source bridge cannot replace(2) by a demand
that every hidden coupling vanish.

For an explicit countercontrol set h_r=0 and k_r=N or -N on ell²(N0), where
N|n>=n|n>. Both have domain sum n²|c_n|²<infinity, and both produce identity
dynamics on A. The same initial visible state tensored with |0><0| is a
full-system ground state for +N. For -N, swapping hidden |0> and |m> by a
finite-rank unitary lowers the energy from0 to-m, for arbitrary m. Neutral
observations and their time dependence are identical. Therefore exact neutral
autonomy alone proves neither full-system spectral stability nor passivity
against arbitrary hidden operations. This does NOT say that passivity
restricted to the accessible neutral algebra is undecidable; that restricted
algebra cannot implement these hidden swaps. No inaccessible operation is
claimed as an available experiment.

## 3. Zero formal commutators can miss order-one boundary leakage

Take d=1, K=L²(0,1), P=diag(1,0) and B=X, the swap matrix. On
L²((0,1),C²), let

    H_B=-i partial_x,
    Dom H_B={f in H¹: f(1)=B f(0)}.                 (4)

The unitary boundary condition makes H_B selfadjoint (boundary form cancels,
and diagonalizing B reduces to periodic/antiperiodic scalar momentum).
On D_test=C_c-infinity((0,1),C²), [H_B,P]=0. D_test is dense and
preserved by the formal expressions, but P DOES NOT preserve Dom H_B.
For example boundary value f(0)=e0 requires f(1)=e1; projection breaks it.
D_test is explicitly NOT an operator core of H_B: its graph closure has
zero traces H¹_0, missing the extension's nonzero boundary values.

Using the B-twisted extension f(x+1)=B f(x), U_t f(x)=f(x-t). For0<t<1,

    U_t* P U_t = P on (0,1-t), I-P on (1-t,1).       (5)

The neutral algebra(1) in this d=1 example contains constant diagonal
matrices only. Both spatial regions have positive measure. Hence

    ||U_t* P U_t-P||=1,
    dist(U_t* P U_t,A)=1/2.                          (6)

The second equality is minimax over the two constant diagonal entries;
I/2 attains it. Strong continuity holds: for every fixed L² vector the
norm of the difference applied to that vector tends0 as t->0. The
operator norm remains1 because maximizing vectors concentrate at the seam.
This is an exact counterexample to promoting an interior formal-commutator
calculation into autonomous observed dynamics. It is not a counterexample
to the valid core theorem: bounded observables preserving a genuine H-core
with controlled zero commutator do extend to strong commutation.

Replacing B by a diagonal unitary is the contrary repair: it commutes with
P, preserves the domain, and yields exact neutral autonomy. The location
of the problem is the boundary-domain choice, not the local differential
symbol or the mere fact that H is unbounded.

## 4. Stronger boundary classification and energy repair

For any finite D and B unitary, on the same interval the constant matrix
algebra A0 is normalized by this twisted momentum evolution exactly when
B commutes with EVERY element of A0. Sufficiency is immediate. Necessity:
for0<t<1 the evolved a takes the two values a and B a B* on spatial
sets of positive measure. To belong to a constant algebra they must be
equal. Merely having B normalize A0 is insufficient; the X example
normalizes the diagonal algebra but swaps its center only on part of space.
This tests the exact boundary gluing of a future observed-domain adapter.

This boundary phenomenon is not dependent on negative energy. Define
L_B=H_B², with domain f in H² satisfying f(1)=B f(0) and
f'(1)=B f'(0). It is selfadjoint and nonnegative. Neutral autonomy under
exp(-it L_B) would force the finite center P to be fixed and hence to
reduce L_B. But P does not preserve this domain: choose smooth scalar
eta with eta(0)=0, eta(1)=1, eta'(0)=eta'(1)=0 and set
f=(1-eta)e0+eta e1. It satisfies both B traces; P f does not.
Therefore the nonnegative evolution also fails neutral autonomy. No claim
of the SAME sharp distance(6) for this dispersive evolution is made.
Semiboundedness repairs energy but does not by itself repair observed-domain
closure. This is a second independent prerequisite on the same apparatus.

## 5. Verification and source consequence

The theorem uses strong groups and selfadjoint domains; finite truncations
cannot certify it. Exact controls check charge-block visible commutators,
hidden plus/minus energy and swap controls, explicit mixed boundary traces,
the two-region minimax defect, and a nonnegative squared-extension domain
witness. Faults change a hidden interaction, trace, boundary, or energy sign.
The reusable output is a precise obligation: select the actual observed
algebra AND a strongly compatible physical domain. Neither a positive
symbol nor a formal local operator identity is sufficient. SC-META-53
remains UNCERTAIN; this does not adjudicate the source's unbuilt shielding
mechanism or supply a source-selected realization of(1).
