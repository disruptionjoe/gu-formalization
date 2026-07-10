#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REFEREE (hostile) re-derivation of LEG-A.  Built independently of the leg's data
structures.  I encode ONLY the hard eliminations that a cited GU commitment can
DEFEND at its stated strength, and I refuse to let any soft/evidence tilt remove a
carrier.  Question: does the honest hard intersection force B?  It must NOT if the
leg is honest.

Discipline: a commitment may HARD-eliminate a declaration value ONLY if the cited
line, read at face value, excludes it.  Everything else is logged as a tilt and
CANNOT change survival.  I then adversarially test the p-hack the council fears:
"tilt ABSENT + (ABSENT,CHIRAL) inconsistent  =>  B forced" -- and confirm the leg
does NOT commit it.
"""

FIELD = {"CONSTRAINED", "FULL", "BARE"}
INV   = {"ABSENT", "PRESENT"}
PHASE = {"MASSIVE", "CHIRAL"}
PROV  = {"SUGRA_4D", "GRADED_IG"}   # provenance available to a PRESENT invariance

VERTEX = {
    ("ABSENT",  "MASSIVE"): "B",             # ungauged massive, ker-Gamma cure
    ("PRESENT", "CHIRAL"):  "A",             # gauged massless gravitino
    ("PRESENT", "MASSIVE"): "CTRL40",        # gauged then super-Higgsed
    ("ABSENT",  "CHIRAL"):  "INCONSISTENT",  # ungauged massless charged -> GP bites
}

# ---- HARD eliminations I am willing to defend from a cited line ----
# C1 "We will never find space time Susie" [00:46:02].  Denies GAUGED 4d spacetime
# SUSY => the textbook SUGRA route to a PRESENT invariance is unavailable.  It does
# NOT deny the graded-IG "extend it through supersymmetry" [00:49:16] route (that is
# not spacetime SUSY).  => remove SUGRA_4D only.
prov_out = {"SUGRA_4D"}

# No cited line hard-eliminates a FIELD value: [00:49:16]/[00:32:46] name Omega^1(S)
# which is the shared arena; ker-Gamma vs full is exactly the unstated SG4 gap.
field_out = set()
# No cited line hard-eliminates an INV value: C9 is "no license STATED" (absence of
# statement != statement of absence), C2 keeps PRESENT reachable.  => nothing removed.
inv_out = set()
# No cited line hard-eliminates a PHASE value: C5 "the mass is a variable" [00:46:40]
# makes phase a free modulus.  => nothing removed.
phase_out = set()

allowed_field = FIELD - field_out
allowed_inv   = INV   - inv_out
allowed_phase = PHASE - phase_out
allowed_prov  = PROV  - prov_out

def survives(inv, phase):
    if inv not in allowed_inv or phase not in allowed_phase:
        return False
    carrier = VERTEX[(inv, phase)]
    if carrier in ("A", "CTRL40"):        # both need a PRESENT-invariance provenance
        return "GRADED_IG" in allowed_prov
    return True                            # B (ker-Gamma) and INCONSISTENT corner reachable

survivors = {VERTEX[k] for k in VERTEX if survives(*k)}
print("allowed field :", sorted(allowed_field))
print("allowed inv   :", sorted(allowed_inv))
print("allowed phase :", sorted(allowed_phase))
print("allowed prov  :", sorted(allowed_prov))
print("survivors     :", sorted(survivors))

# ---- INDEPENDENT ASSERTIONS ----
R = []
def ck(c, m): R.append((bool(c), m)); print(("PASS" if c else "FAIL"), m)

ck(allowed_field == {"BARE", "CONSTRAINED", "FULL"}, "no cited line collapses field-space -> not FORCES via field")
ck(allowed_inv == {"ABSENT", "PRESENT"}, "no cited line collapses invariance")
ck(allowed_phase == {"CHIRAL", "MASSIVE"}, "no cited line collapses phase")
ck(allowed_prov == {"GRADED_IG"}, "C1 removes only SUGRA_4D; graded-IG A-door survives (A NOT eliminated)")
ck(survivors == {"A", "B", "CTRL40", "INCONSISTENT"}, "intersection LEAVES A FAMILY (all 4 corners live) -> NOT FORCES-B")
ck("A" in survivors, "carrier A survives (leg does not p-hack A out)")
ck("B" in survivors, "carrier B survives")
ck("CTRL40" in survivors, "-40 survives")

# ---- the p-hack the council fears, tested and REFUSED ----
# If a hostile author FORCED inv=ABSENT (from the C9/C6b tilts) and then demanded
# consistency, (ABSENT,CHIRAL) is inconsistent, so only B remains: a manufactured force.
def collapse(inv_fixed=None):
    return {VERTEX[k] for k in VERTEX if survives(*k) and (inv_fixed is None or k[0]==inv_fixed)}
absent = collapse("ABSENT")
print("inv=ABSENT collapses to:", sorted(absent))
ck(absent == {"B", "INCONSISTENT"}, "ABSENT -> {B, inconsistent}: B would be forced ONLY if inv were hard-forced ABSENT")
ck(inv_out == set(), "inv is NOT hard-forced ABSENT (C9 is a tilt) -> the ABSENT->B force is correctly NOT claimed")

# ---- neither single bit forces a unique carrier (residual is 2-dimensional) ----
def collapse_phase(p): return {VERTEX[k] for k in VERTEX if survives(*k) and k[1]==p}
ck(len(absent) == 2 and len(collapse("PRESENT")) == 2 and len(collapse_phase("MASSIVE")) == 2
   and len(collapse_phase("CHIRAL")) == 2, "no single SG4 bit forces a unique carrier -> genuine 2-bit residual")

nfail = sum(1 for ok,_ in R if not ok)
print(f"\n{sum(1 for ok,_ in R if ok)}/{len(R)} pass, {nfail} fail")
import sys; sys.exit(1 if nfail else 0)
