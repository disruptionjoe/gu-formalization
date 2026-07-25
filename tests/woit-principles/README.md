# Woit-principles finite kernels

These scripts are positive and negative controls for the Woit-to-GU transfer
notes in `explorations/woit-principles/`. They formalize finite algebraic
geometry, representation-theory, and spectral kernels only. They do not
establish a GU physical sector, a full reflection-positive field theory, a
Penrose transform, or a scientific-status change. The OS reconstruction
stress test requires NumPy; the other Woit-principles kernels use the Python
standard library.

Run:

```bash
python3 tests/woit-principles/test_soldering_palatini_kernel.py
python3 tests/woit-principles/test_os_real_form_kernel.py
python3 tests/woit-principles/test_twistor_grassmannian_kernel.py
python3 tests/woit-principles/test_twistor_real_slice_reconstruction.py
python3 tests/woit-principles/test_os_reconstruction_kernel.py
python3 tests/wave10/H27_soldering_palatini.py
```

| Script | Positive control | Transfer gate |
|---|---|---|
| `test_soldering_palatini_kernel.py` | the nondegenerate four-dimensional Palatini torsion map has exact rank `24/24` | degeneracy drops rank; GU still needs the missing linear-in-curvature/soldering mechanism |
| `test_os_real_form_kernel.py` | a chosen nonzero Euclidean vector gives an invertible `S+ -> S-` Clifford map | the map is not a fixed `Spin(4)` intertwiner, `n` versus `-n` is not a residual bit, and Lorentzian conjugation exchanges Hodge halves |
| `test_twistor_grassmannian_kernel.py` | exact `Gr(2,C^4)`, incidence, tautological quotient, Chern, and stabilizer arithmetic | a purely right-handed tangent and labeled real-form component require extra structure; `c3(Q_3)=1` does not count three generations |
| `test_twistor_real_slice_reconstruction.py` | exact Lorentzian Hermitian big cell, determinant/null-incidence and `O(1)+O(1)` deformation arithmetic, plus Euclidean quaternionic-line geometry | Minkowski and Euclidean spacetime require inequivalent real structures; neither is the GU carrier or full gimmel metric |
| `test_os_reconstruction_kernel.py` | deterministic and seeded positive spectral measures give positive-semidefinite reflected Gram matrices, with quotient rank changing from one to three under fixed time geometry and scale-covariant classification | a planted signed measure fails under the same reflection, so positivity and quotient size come from Schwinger/dynamical data rather than reflection geometry alone |
