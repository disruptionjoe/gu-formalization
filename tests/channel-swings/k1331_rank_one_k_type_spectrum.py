#!/usr/bin/env python3
"""Exact and quadrature controls for K1331's full rank-one K-type spectrum."""
import cmath, hashlib, json, math
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; D=json.loads((ROOT/"lab/process/k1331-rank-one-k-type-spectrum.json").read_text()); ncheck=0
def check(label,value):
 global ncheck; assert value,label; ncheck+=1; print(f"PASS {ncheck:02d}: {label}")
for key,pin in D["pinned_inputs"].items(): check(f"{key} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"])
O=D["rank_one_operator"]; S=D["complete_even_spectrum"]; Q=D["decision"]
check("rank-one group",O["group"]=="SL(2,R) simple-root subgroup")
check("even compact picture",O["compact_picture"]=="K_alpha/M_alpha=SO(2)/{plus_or_minus 1}")
check("common Fourier core","exp(2 i n theta)" in O["common_algebraic_core"])
check("full raw integral",O["raw_standard_integral"].startswith("(J_z f)(g)=integral_R"))
check("spherical normalizer",O["spherical_normalizer"]=="m(z)=sqrt(pi) Gamma(z/2)/Gamma((z+1)/2)")
def a(mode,z):
 out=1
 for k in range(1,abs(mode)+1): out*=((2*k-1)-z)/((2*k-1)+z)
 return out
check("spherical mode",a(0,Fraction(7,3))==1 and S["spherical_mode"]=="a_0(z)=1")
check("weight symmetry",all(a(k,Fraction(2,5))==a(-k,Fraction(2,5)) for k in range(8)))
check("zero identity",all(a(k,Fraction(0))==1 for k in range(12)))
check("first recurrence",a(1,Fraction(2))==Fraction(-1,3))
check("second recurrence",a(2,Fraction(2))==Fraction(-1,15))
check("third recurrence",a(3,Fraction(2))==Fraction(-1,35))
for mode in range(5):
 z=Fraction(4,7)
 ratio=a(mode+1,z)/a(mode,z)
 check(f"mode {mode} recurrence",ratio==((2*mode+1)-z)/((2*mode+1)+z))
def raw_gamma(mode,z):
 q=abs(mode)
 return ((-1)**q*math.pi*math.gamma(z)/(2**(z-1)*math.gamma((z+1)/2+q)*math.gamma((z+1)/2-q)))
check("raw n0 recovers m",abs(raw_gamma(0,2)-2)<1e-12)
check("raw n1 value",abs(raw_gamma(1,2)+Fraction(2,3))<1e-12)
check("raw n2 value",abs(raw_gamma(2,2)+Fraction(2,15))<1e-12)
def quadrature(mode,z,steps=12000):
 left=-math.pi/2; right=math.pi/2; h=(right-left)/steps
 def f(theta): return ((-1)**abs(mode))*math.cos(theta)**(z-1)*math.cos(2*mode*theta)
 total=f(left)+f(right)
 total+=4*sum(f(left+j*h) for j in range(1,steps,2))
 total+=2*sum(f(left+j*h) for j in range(2,steps,2))
 return h*total/3
check("quadrature n1",abs(quadrature(1,2)+2/3)<1e-9)
check("quadrature n2",abs(quadrature(2,2)+2/15)<1e-9)
check("full operator decision",Q["full_rank_one_operator_kernel_constructed"] and Q["all_even_rank_one_k_type_eigenvalues_constructed"])
check("higher-rank scalar ceiling",not Q["higher_rank_irreducible_K_types_claimed_scalar"])
check("physical ceiling",not Q["physical_intertwiner_constructed"] and not Q["protected_status_change"])
assert ncheck==26; print("RESULT: PASS 26/26")
