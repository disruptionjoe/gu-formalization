# CPTt triality comparison gate

This directory contains a bounded comparison between the finite construction in
A. Garrett Lisi, *C, P, T, and Triality*, arXiv:2407.02497v2, and the current GU
generation structures.

Run:

```text
python -u tests/cptt/cptt_triality_gate.py
```

The script uses exact rational arithmetic and has no third-party dependencies.
It checks:

- the 24 Hurwitz units forming the binary tetrahedral group `2T`;
- the order-96 central product `(2T x D4)/Z2` and its order-two center;
- the order-three versus order-six sign subtlety in the paper's quaternion `t`;
- the exact adjoint cycle `i -> j -> k -> i`;
- the ordinary three-cycle as a kinematic comparator for GU's native
  self-dual triplet;
- a repeated-copy vacuity control and a split-operator sensitivity control;
- the Lorentz-Casimir obstruction to cycling GU's current spin-1/2,
  spin-1/2, spin-3/2 typed construction;
- a visible obligation manifest separating kinematic hosting from a physical
  action and positive-quotient lift.

The test does not verify the paper's full semilinear matrix representation. It
does not establish that GU derives three physical generations, selects a
particular finite subgroup, has an interacting CPTt-invariant action, or lifts
the group to a positive physical Hilbert space. Those are separate obligations.

The expected current classification is `KINEMATIC_ONLY` for the native
self-dual carrier, with a scoped `NO_GO` for an order-three cycle on the current
typed 2+1 construction.
