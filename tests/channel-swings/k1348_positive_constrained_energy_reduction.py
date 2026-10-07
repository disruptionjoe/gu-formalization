#!/usr/bin/env python3
"""Positive energy and linearized-reduction controls for K1348."""
import hashlib,json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1348-positive-constrained-energy-reduction.json").read_text()); n=0
def check(label,value):
 global n; assert value,label; n+=1; print(f"PASS {n:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
C=D["constrained_reduction"]; Q=D["decision"]
check("energy phase space","H1(T3)" in C["phase_space"] and "L2(T3)" in C["phase_space"])
check("Gauss distribution domain","H-1(T3)" in C["gauss_surface"])
check("zero-mean gauge group","zero-mean H2" in C["gauge_group"])
check("flat zero modes fenced","excludes harmonic" in C["topological_sector"])
check("Hamiltonian has electric energy","||E||2^2" in C["hamiltonian"])
check("Hamiltonian has magnetic energy","||B||2^2" in C["hamiltonian"])
check("Hamiltonian has matter momentum","||Pi||2^2" in C["hamiltonian"])
check("Hamiltonian has covariant gradient","||D phi||2^2" in C["hamiltonian"])
check("Hamiltonian has defocusing potential","lambda/4" in C["hamiltonian"])
samples=[(1,2,3,4,5),(2,0,1,3,2),(0,1,0,2,7)]
for E,B,Pi,Dphi,phi in samples:
 H=Fraction(E*E+B*B+Pi*Pi+Dphi*Dphi,2)+Fraction(3*phi*phi,2)+Fraction(phi**4,4)
 check("sample positive energy",H>0)
check("energy gauge descent","descends to gauge classes" in C["gauge_descent"])
check("nonzero Gauss class","nonzero smooth" in C["nonempty_nonzero_class"])
check("vacuum linearization","free zero-mean Maxwell" in C["vacuum_linearization"])
check("two photon polarizations","two transverse photon" in C["linearized_cohomology"])
check("matter survives cohomology","H_ps matter modes" in C["linearized_cohomology"])
check("positive linearized pairing","strictly positive" in C["linearized_pairing"])
check("positive Hamiltonian decision",Q["positive_interacting_hamiltonian_constructed"])
check("nonempty constraint decision",Q["interacting_gauss_surface_nonempty"])
check("descent decision",Q["classical_energy_descends_to_gauge_classes"])
check("linearized cohomology decision",Q["positive_nonzero_linearized_brst_cohomology_constructed"])
check("zero-mode decision",Q["harmonic_zero_mode_removed_by_declared_sector"])
check("nonlinear Hilbert ceiling",not Q["closed_nonlinear_physical_hilbert_quotient_constructed"])
check("global evolution ceiling",not Q["global_large_data_interacting_evolution_constructed"])
check("quantum ceiling",not Q["quantum_positive_physical_space_constructed"])
check("GU ceiling",not Q["gu_physical_cohomology_constructed"])
assert n==30; print("RESULT: PASS 30/30")
