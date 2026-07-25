# Woit-principles finite kernels

These standard-library scripts are positive and negative controls for the
Woit-to-GU transfer notes in `explorations/woit-principles/`. They formalize
finite algebraic geometry and representation-theory kernels only. They do not
establish a GU physical sector, reflection positivity, a Penrose transform, or
a scientific-status change.

Run:

```bash
python3 tests/woit-principles/test_soldering_palatini_kernel.py
python3 tests/woit-principles/test_os_real_form_kernel.py
python3 tests/woit-principles/test_twistor_grassmannian_kernel.py
python3 tests/wave10/H27_soldering_palatini.py
```

| Script | Positive control | Transfer gate |
|---|---|---|
| `test_soldering_palatini_kernel.py` | the nondegenerate four-dimensional Palatini torsion map has exact rank `24/24` | degeneracy drops rank; GU still needs the missing linear-in-curvature/soldering mechanism |
| `test_os_real_form_kernel.py` | a chosen nonzero Euclidean vector gives an invertible `S+ -> S-` Clifford map | the map is not a fixed `Spin(4)` intertwiner, `n` versus `-n` is not a residual bit, and Lorentzian conjugation exchanges Hodge halves |
| `test_twistor_grassmannian_kernel.py` | exact `Gr(2,C^4)`, incidence, tautological quotient, Chern, and stabilizer arithmetic | a purely right-handed tangent and labeled real-form component require extra structure; `c3(Q_3)=1` does not count three generations |
