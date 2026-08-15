#!/usr/bin/env python3
"""IT-C -- typing the positivity-bearing rows of the conditional-physics ledger.

Object: `lab/process/conditional-physics-ledger-v0.258.json`, 84 row records,
sha256 pinned below, plus the proposed versionless delta which is read OUT OF
the artifact
`lab/active-research/joe-directed/indefiniteness-typing/
 itc-positivity-rows-are-five-not-ten-2026-08-15.md`
so that the record and this certificate cannot drift.

This probe does FIVE things and keeps them separate:

  [R] replays BD-D's class-H rule from scratch and checks it returns exactly the
      ten rows BD-D published, BEFORE any positivity claim is made, so nothing
      below can be an artefact of mis-stating BD-D;
  [E] runs the IT-C matching rule (Rule P) over all 84 rows and computes the
      class sizes and the intersection with class H;
  [E] computes an ABSENCE CERTIFICATE for the whole positivity lexicon over all
      84 rows x 9 string fields, per token;
  [E] parses the proposed delta out of the artifact between explicit markers and
      validates every proposed row against the v0.258 taxonomy and freeze rules;
  [C] plants FAILING controls against that same validator -- including a LAUNDER
      control that re-types a row to an unconditional SAME-family kind and an
      ADVANCE control that flips a verdict, both of which MUST be rejected.

Exact integers only. No float is constructed anywhere; `assert_no_float` sweeps
the whole result dict before the certificate prints.

Certificate tags:
  [E] exact result of this route
  [C] control that MUST fire (non-vacuity / discrimination)
  [R] reproduction of a fact already filed by BD-D / the ledger itself

Usage (from the repository root):
  _local/cas-venv/bin/python \
    tests/channel-swings/joe_directed_itc_positivity_rows_are_five_not_ten.py

Failure-path self-test (spawns one subprocess per planted false fact; each must
exit 1; the selftest itself exits 0 on success):
  _local/cas-venv/bin/python \
    tests/channel-swings/joe_directed_itc_positivity_rows_are_five_not_ten.py \
    --selftest

NOT: a ledger edit, a verdict change, a physics derivation, a claim that any GU
object exists, a claim that GU is consistent, or a claim that the proposed
re-typing is canonical. The delta is a PROPOSAL for the canonical owner, and a
re-typing is not an advance.
"""

import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
if os.path.basename(ROOT) == 'tests':
    ROOT = os.path.dirname(ROOT)

LEDGER = os.path.join(ROOT, 'lab', 'process',
                      'conditional-physics-ledger-v0.258.json')
ARTIFACT = os.path.join(
    ROOT, 'lab', 'active-research', 'joe-directed', 'indefiniteness-typing',
    'itc-positivity-rows-are-five-not-ten-2026-08-15.md')

PINNED_LEDGER_SHA = (
    '540b50e386073c0f43da4e8d5a8ffdaf06fd243c6612622d7daf187c0a725047')

MUT = os.environ.get('ITC_MUTATE', '')
if '--mutate' in sys.argv:
    MUT = sys.argv[sys.argv.index('--mutate') + 1]

CERT = []
RESULT = {}


def C(tag, name, ok, detail=''):
    CERT.append((tag, name, bool(ok), str(detail)))
    return bool(ok)


def assert_no_float(obj, path='result'):
    if isinstance(obj, float):
        raise AssertionError('load-bearing float at %s' % path)
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_float(v, '%s[%r]' % (path, k))
    elif isinstance(obj, (list, tuple, set)):
        for i, v in enumerate(obj):
            assert_no_float(v, '%s[%d]' % (path, i))


# ===========================================================================
# 0. BASELINE -- the ledger, pinned by content hash
# ===========================================================================

STRING_FIELDS = ['summary', 'verdict', 'reason_kind', 'distance',
                 'revival_trigger', 'construction_scope', 'mapping_grade',
                 'frontier_grade', 'evidence']
DEMAND_FIELDS = ['reason_kind', 'distance', 'revival_trigger']

# Rule P lexicon, declared before it is run (artifact section 1).
LEXICON = ['positive', 'positivity', 'definite', 'definiteness', 'indefinite',
           'indefiniteness', 'semidefinite', 'coercive', 'krein', 'ghost',
           'ghosts', 'unitary', 'unitarity', 'signature', 'nondegenerate',
           'inertia', 'norm', 'normed', 'psd', 'pseudounitary', 'degenerate']

WORD = re.compile(r'[A-Za-z]+')


def section_0():
    with open(LEDGER, 'rb') as fh:
        raw = fh.read()
    sha = hashlib.sha256(raw).hexdigest()
    if MUT == 'artifact_sha':
        sha = '0' * 64
    RESULT['ledger_sha256'] = sha
    ledger = json.loads(raw)
    RESULT['_ledger'] = ledger
    rows = ledger['rows']
    RESULT['_rows'] = rows
    RESULT['_by_id'] = {r['id']: r for r in rows}

    C('R', 'ledger sha256 matches the value pinned in this probe',
      sha == PINNED_LEDGER_SHA, sha)
    C('R', 'row_record_count is 84 and matches the denominator block',
      len(rows) == 84 == ledger['denominator']['row_record_count'], len(rows))
    C('R', 'canonical_target_count is 82',
      ledger['denominator']['canonical_target_count'] == 82)
    C('R', 'taxonomy is extensible and forbids forced fit',
      ledger['taxonomy']['extensible'] is True and
      ledger['taxonomy']['unknown_kind_rule'] ==
      'NEW_KIND_REQUIRED__FORCED_FIT_FORBIDDEN')
    C('R', 'LT-GR6b is NOT a row of v0.258 (BD-C/LA-11 adjudicated a proposal)',
      'LT-GR6b' not in RESULT['_by_id'] and b'LT-GR6b' not in raw)
    C('R', 'every row carries all five demand-and-identity fields',
      all(all(k in r for k in
              ['id', 'axis', 'source_row', 'summary', 'verdict', 'reason_kind',
               'distance', 'revival_trigger', 'evidence', 'mapping_grade'])
          for r in rows))


# ===========================================================================
# 1. [R] CLASS H -- BD-D's rule, replayed, BEFORE any positivity claim
# ===========================================================================

BDD_PUBLISHED_H = ['RA-A4', 'RA-A5', 'RA-B6', 'RA-D4', 'RA-E4', 'RA-E6',
                   'RA-G1', 'RA-G4', 'LT-SM4', 'LT-SM6']

H_PAT = re.compile(
    r'hessian|mass matrix|eigenvalue|spectrum|spectral|\bpole\b|'
    r'second variation|stabilit', re.I)


def section_1():
    rows = RESULT['_rows']
    h = [r['id'] for r in rows
         if H_PAT.search(' | '.join(str(r.get(k, '')) for k in DEMAND_FIELDS))]
    if MUT == 'class_h_size':
        h = h[:5]
    RESULT['class_H'] = h
    C('R', 'class H replayed from the rule returns exactly 10 rows',
      len(h) == 10, len(h))
    C('R', 'class H is element-for-element BD-D rows_touched_structurally',
      sorted(h) == sorted(BDD_PUBLISHED_H), sorted(h))


# ===========================================================================
# 2. [E] CLASS P -- the IT-C matching rule
# ===========================================================================

def lexicon_hits(row, fields):
    out = {}
    for f in fields:
        v = row.get(f)
        if not isinstance(v, str):
            continue
        for w in WORD.findall(v):
            lw = w.lower()
            if lw in LEXICON:
                out.setdefault(lw, set()).add(f)
    return out


def section_2():
    rows = RESULT['_rows']
    p = [r['id'] for r in rows if lexicon_hits(r, DEMAND_FIELDS)]
    pprime = [r['id'] for r in rows if lexicon_hits(r, STRING_FIELDS)]
    if MUT == 'class_p_size':
        p = list(RESULT['class_H'])
    inter = sorted(set(p) & set(RESULT['class_H']))
    if MUT == 'intersection':
        inter = sorted(set(RESULT['class_H']))
    RESULT['class_P'] = p
    RESULT['class_P_prime'] = pprime
    RESULT['P_intersect_H'] = inter

    C('E', 'class P (positivity lexicon, demand fields) has exactly 5 rows',
      len(p) == 5, p)
    C('E', 'class P is exactly {RA-D4, RA-G2, LT-GR2c, LT-SM8, AC-F1}',
      sorted(p) == sorted(['RA-D4', 'RA-G2', 'LT-GR2c', 'LT-SM8', 'AC-F1']),
      sorted(p))
    C('E', "class P' (all nine string fields) has exactly 7 rows",
      len(pprime) == 7, pprime)
    C('E', "P' \\ P is exactly {LT-GR2, LT-GR5}",
      sorted(set(pprime) - set(p)) == ['LT-GR2', 'LT-GR5'],
      sorted(set(pprime) - set(p)))
    C('E', 'P intersect H has exactly one member, RA-D4',
      inter == ['RA-D4'], inter)
    C('E', 'nine of BD-D ten Hessian rows carry NO lexicon token in ANY field',
      len([i for i in RESULT['class_H'] if i not in pprime]) == 9,
      [i for i in RESULT['class_H'] if i not in pprime])
    C('E', 'LT-GR2 is excluded from P because it is SUPERSEDED',
      RESULT['_by_id']['LT-GR2'].get('row_status') == 'SUPERSEDED')
    C('E', 'LT-GR5 carries its indefiniteness in mapping_grade only, a finding '
           'not a demand',
      set(lexicon_hits(RESULT['_by_id']['LT-GR5'],
                       STRING_FIELDS)) >= {'indefinite', 'nondegenerate'} and
      not lexicon_hits(RESULT['_by_id']['LT-GR5'], DEMAND_FIELDS))


# ===========================================================================
# 3. [E] ABSENCE CERTIFICATE over the whole lexicon
# ===========================================================================

ZERO_TOKENS = ['ghost', 'ghosts', 'definite', 'definiteness', 'indefiniteness',
               'unitarity', 'signature', 'coercive', 'semidefinite', 'norm',
               'normed', 'psd', 'pseudounitary', 'degenerate']


def section_3():
    rows = RESULT['_rows']
    counts = dict((t, 0) for t in LEXICON)
    for r in rows:
        for f in STRING_FIELDS:
            v = r.get(f)
            if not isinstance(v, str):
                continue
            for w in WORD.findall(v):
                lw = w.lower()
                if lw in counts:
                    counts[lw] += 1
    if MUT == 'ghost_token':
        counts['ghost'] = 3
    RESULT['lexicon_counts'] = counts

    C('E', 'token counts: positive 8, positivity 1, krein 1, indefinite 1, '
           'unitary 1, inertia 1, nondegenerate 1',
      counts['positive'] == 8 and counts['positivity'] == 1 and
      counts['krein'] == 1 and counts['indefinite'] == 1 and
      counts['unitary'] == 1 and counts['inertia'] == 1 and
      counts['nondegenerate'] == 1,
      dict((k, v) for k, v in counts.items() if v))
    C('E', 'fourteen lexicon tokens occur ZERO times in all 84 rows',
      all(counts[t] == 0 for t in ZERO_TOKENS) and len(ZERO_TOKENS) == 14,
      [t for t in ZERO_TOKENS if counts[t]])

    # the sole Krein / indefinite occurrences, and where they are NOT
    krein_rows = [r['id'] for r in rows
                  if 'krein' in lexicon_hits(r, STRING_FIELDS)]
    krein_demand = [r['id'] for r in rows
                    if 'krein' in lexicon_hits(r, DEMAND_FIELDS)]
    if MUT == 'krein_demand':
        krein_demand = ['LT-GR2c']
    RESULT['krein_rows'] = krein_rows
    RESULT['krein_demand_rows'] = krein_demand
    C('E', 'the sole Krein occurrence is LT-GR2c.construction_scope',
      krein_rows == ['LT-GR2c'] and
      'construction_scope' in
      lexicon_hits(RESULT['_by_id']['LT-GR2c'], STRING_FIELDS)['krein'])
    C('E', 'ZERO rows demand a Krein structure in a demand field',
      krein_demand == [], krein_demand)
    C('E', 'ZERO rows demand ghost clearance or unitarity in any field',
      counts['ghost'] == 0 and counts['ghosts'] == 0 and
      counts['unitarity'] == 0)

    # D7: the source's own signature data appears in no row
    blob = json.dumps(rows)
    sig_probes = {}
    for pat in [r'6,\s*4', r'7,\s*3', r'Spin\(6', r'Spin\(3',
                r'trace revers', r'Frobenius']:
        sig_probes[pat] = len(re.findall(pat, blob, re.I))
    RESULT['signature_probe'] = sig_probes
    C('E', 'D7: zero rows carry the source signature data (6,4 / 7,3 / Spin(6 '
           '/ Spin(3 / trace reverse / Frobenius) and signature token is 0',
      all(v == 0 for v in sig_probes.values()) and counts['signature'] == 0,
      sig_probes)


# ===========================================================================
# 4. THE PROPOSED DELTA -- read OUT OF the artifact, then validated
# ===========================================================================

BEGIN = '<!-- ITC-DELTA-BEGIN -->'
END = '<!-- ITC-DELTA-END -->'


def load_delta():
    with open(ARTIFACT, 'r', encoding='utf-8') as fh:
        text = fh.read()
    i = text.index(BEGIN) + len(BEGIN)
    j = text.index(END)
    block = text[i:j]
    m = re.search(r'```json\s*(.*?)```', block, re.S)
    if m is None:
        raise AssertionError('no fenced json block between the ITC-DELTA markers')
    return json.loads(m.group(1))


def validate_delta(delta, ledger, relax=()):
    """Return a list of violation strings. Empty list == the delta validates.

    `relax` disables named rules; it exists ONLY so the mutation harness can
    prove each rule is load-bearing.
    """
    v = []
    by_id = {r['id']: r for r in ledger['rows']}
    tax = ledger['taxonomy']['verdict_kinds']
    known = {}
    for fam, kinds in tax.items():
        for k in kinds:
            known[k] = fam
    ext = {}
    for e in delta.get('taxonomy_extension', []):
        ext[e['new_kind']] = e

    if 'base_sha' not in relax:
        if delta.get('ledger_base_sha256') != RESULT['ledger_sha256']:
            v.append('BASE_SHA_DRIFT')
    if delta.get('edit_applied') is not False:
        v.append('CHANNEL_MUST_NOT_EDIT_THE_LEDGER')
    if delta.get('rows_advanced') != 0:
        v.append('RETYPING_IS_NOT_ADVANCING__rows_advanced_must_be_0')
    if delta.get('denominator_move') != 'none':
        v.append('DENOMINATOR_MOVED')

    for e in delta.get('taxonomy_extension', []):
        if e.get('family') not in tax:
            v.append('EXT_FAMILY_UNKNOWN:%s' % e.get('family'))
        if e.get('new_kind') in known:
            v.append('EXT_KIND_ALREADY_EXISTS:%s' % e.get('new_kind'))
        for req in ('definition', 'non_discharge_rule', 'licence',
                    'rejected_alternatives'):
            if not e.get(req):
                v.append('EXT_MISSING_%s' % req.upper())

    for d in delta.get('row_deltas', []):
        rid = d.get('id')
        tag = d.get('delta', '?')
        if rid not in by_id:
            v.append('%s:UNKNOWN_ROW_ID:%s' % (tag, rid))
            continue
        base = by_id[rid]
        # record/certificate may not drift: the "before" must be the ledger
        if 'stale_before' not in relax:
            if d.get('verdict_before') != base['verdict']:
                v.append('%s:VERDICT_BEFORE_DRIFT' % tag)
            if d.get('reason_kind_before') != base['reason_kind']:
                v.append('%s:REASON_KIND_BEFORE_DRIFT' % tag)
        # a re-typing is not an advance: the verdict may not move
        if 'advance' not in relax:
            if d.get('verdict_after') != d.get('verdict_before'):
                v.append('%s:VERDICT_MOVED__THIS_IS_AN_ADVANCE_NOT_A_RETYPING'
                         % tag)
        after = d.get('reason_kind_after')
        if after is None:
            v.append('%s:MISSING_reason_kind_after' % tag)
            continue
        fam_after = known.get(after) or (ext.get(after) or {}).get('family')
        if fam_after is None:
            v.append('%s:UNDECLARED_KIND:%s' % (tag, after))
        # THE LAUNDER RULE: the kind must stay in the same verdict family as
        # the row's verdict. A NEEDS row may not acquire a SAME-family kind.
        if 'launder' not in relax:
            if fam_after is not None and fam_after != d.get('verdict_after'):
                v.append('%s:LAUNDER__kind %s is family %s but the row verdict '
                         'is %s' % (tag, after, fam_after,
                                    d.get('verdict_after')))
        # any delta that changes the kind must carry a non-discharge note and a
        # named condition
        if after != d.get('reason_kind_before'):
            if 'debt_note' not in relax and not d.get('debt_note'):
                v.append('%s:RETYPE_WITHOUT_debt_note' % tag)
            if not d.get('named_condition'):
                v.append('%s:RETYPE_WITHOUT_named_condition' % tag)
            if not d.get('grounds'):
                v.append('%s:RETYPE_WITHOUT_grounds' % tag)
            if d.get('direction') != 'WORSE':
                v.append('%s:RETYPE_DIRECTION_NOT_WORSE' % tag)
        # freeze_rule: id / axis / source_row / summary are immutable
        for frozen in ('id_after', 'axis_after', 'source_row_after',
                       'summary_after'):
            if frozen in d:
                v.append('%s:FREEZE_RULE_VIOLATION:%s' % (tag, frozen))
    return v


def section_4():
    ledger = RESULT['_ledger']
    delta = load_delta()
    RESULT['_delta'] = delta

    C('E', 'the delta parses out of the artifact between the ITC markers',
      isinstance(delta, dict) and 'row_deltas' in delta)
    C('E', 'the artifact pins the same ledger sha256 this probe computed',
      delta.get('ledger_base_sha256') == RESULT['ledger_sha256'])

    viol = validate_delta(delta, ledger)
    RESULT['violations'] = viol
    C('E', 'the proposed delta validates against the v0.258 schema, taxonomy '
           'and freeze rules with ZERO violations', viol == [], viol)

    retypes = [d for d in delta['row_deltas']
               if d.get('reason_kind_after') != d.get('reason_kind_before')]
    RESULT['retype_ids'] = [d['id'] for d in retypes]
    nonvac = len(retypes)
    if MUT == 'nonvacuous':
        nonvac = 0
    C('C', 'CONTROL non-vacuity: at least one proposed delta actually changes a '
           'reason_kind', nonvac >= 1, RESULT['retype_ids'])
    C('E', 'exactly ONE row moves status, and it is LT-SM8',
      RESULT['retype_ids'] == ['LT-SM8'], RESULT['retype_ids'])
    C('E', 'every verdict_after equals verdict_before: rows advanced = 0',
      all(d['verdict_after'] == d['verdict_before']
          for d in delta['row_deltas']))
    C('E', 'the new kind is in family NEEDS and LT-SM8 stays NEEDS',
      delta['taxonomy_extension'][0]['family'] == 'NEEDS' and
      RESULT['_by_id']['LT-SM8']['verdict'] == 'NEEDS' and
      [d for d in delta['row_deltas'] if d['id'] == 'LT-SM8'][0]
      ['verdict_after'] == 'NEEDS')
    C('E', 'the new kind declares itself strictly MORE indebting than '
           'MISSING_CONSTRUCTION',
      delta['taxonomy_extension'][0]['strictly_more_indebting_than'] ==
      'MISSING_CONSTRUCTION')
    C('E', 'the re-typing carries a named withdrawal condition',
      [d for d in delta['row_deltas'] if d['id'] == 'LT-SM8'][0]
      ['named_condition']['name'] == 'INHERITANCE_BRIDGE')
    C('E', 'the artifact counts agree with the counts computed here',
      delta['counts']['class_P_size'] == len(RESULT['class_P']) and
      delta['counts']['class_P_prime_size'] == len(RESULT['class_P_prime']) and
      delta['counts']['class_H_size'] == len(RESULT['class_H']) and
      delta['counts']['P_intersect_H'] == len(RESULT['P_intersect_H']) and
      delta['counts']['rows_advanced'] == 0 and
      delta['counts']['rows_moving_status'] == 1 and
      delta['counts']['bucket_c'] == 0,
      delta['counts'])
    C('E', 'every row named by the delta exists in the base ledger',
      all(d['id'] in RESULT['_by_id'] for d in delta['row_deltas']))
    C('E', 'the delta declares edit_applied false -- the channel does not edit '
           'the ledger', delta['edit_applied'] is False)


# ===========================================================================
# 5. [C] PLANTED FAILING CONTROLS against the same validator
# ===========================================================================

def _clone(delta):
    return json.loads(json.dumps(delta))


def section_5():
    ledger = RESULT['_ledger']
    base = RESULT['_delta']

    # --- LAUNDER CONTROL (required by the brief) ------------------------
    # Re-type LT-SM8 to an unconditional SAME-family kind. MUST be rejected.
    for bad_kind in ('DERIVED_CONDITIONAL', 'DERIVED', 'IMPORTED'):
        d = _clone(base)
        for r in d['row_deltas']:
            if r['id'] == 'LT-SM8':
                r['reason_kind_after'] = bad_kind
        relax = ('launder',) if MUT == 'launder' else ()
        viol = validate_delta(d, ledger, relax=relax)
        C('C', 'LAUNDER CONTROL a NEEDS row re-typed to %s must be REJECTED'
          % bad_kind,
          any(x.startswith('D1:LAUNDER') for x in viol), viol)

    # --- ADVANCE CONTROL ------------------------------------------------
    d = _clone(base)
    for r in d['row_deltas']:
        if r['id'] == 'LT-SM8':
            r['verdict_after'] = 'SAME'
            r['reason_kind_after'] = 'DERIVED_CONDITIONAL'
    relax = ('advance', 'launder') if MUT == 'advance' else ()
    viol = validate_delta(d, ledger, relax=relax)
    C('C', 'ADVANCE CONTROL a verdict flip NEEDS -> SAME must be REJECTED',
      any('VERDICT_MOVED' in x for x in viol), viol)

    # --- DRIFT CONTROL: unknown row id ----------------------------------
    d = _clone(base)
    d['row_deltas'][0] = _clone(d['row_deltas'][0])
    d['row_deltas'][0]['id'] = 'LT-SM99'
    viol = validate_delta(d, ledger)
    C('C', 'DRIFT CONTROL a proposed row id absent from the base ledger must '
           'be REJECTED', any('UNKNOWN_ROW_ID' in x for x in viol), viol)

    # --- STALE-BEFORE CONTROL: record/certificate drift -----------------
    d = _clone(base)
    for r in d['row_deltas']:
        if r['id'] == 'LT-SM8':
            r['reason_kind_before'] = 'EXTERNAL_DATUM'
    relax = ('stale_before',) if MUT == 'stale_before' else ()
    viol = validate_delta(d, ledger, relax=relax)
    C('C', 'STALE CONTROL a reason_kind_before that is not the ledger value '
           'must be REJECTED',
      any('REASON_KIND_BEFORE_DRIFT' in x for x in viol), viol)

    # --- SHA CONTROL ----------------------------------------------------
    d = _clone(base)
    d['ledger_base_sha256'] = 'f' * 64
    viol = validate_delta(d, ledger)
    C('C', 'SHA CONTROL a delta pinned to a different ledger content hash must '
           'be REJECTED', 'BASE_SHA_DRIFT' in viol, viol)

    # --- DEBT-NOTE CONTROL ----------------------------------------------
    d = _clone(base)
    for r in d['row_deltas']:
        if r['id'] == 'LT-SM8':
            r.pop('debt_note', None)
    relax = ('debt_note',) if MUT == 'debt_note' else ()
    viol = validate_delta(d, ledger, relax=relax)
    C('C', 'DEBT CONTROL a re-typing without a non-discharge debt_note must be '
           'REJECTED', any('RETYPE_WITHOUT_debt_note' in x for x in viol), viol)

    # --- DENOMINATOR CONTROL --------------------------------------------
    d = _clone(base)
    d['denominator_move'] = '82 -> 81'
    viol = validate_delta(d, ledger)
    C('C', 'DENOMINATOR CONTROL any denominator move must be REJECTED',
      'DENOMINATOR_MOVED' in viol, viol)

    # --- EDIT CONTROL ---------------------------------------------------
    d = _clone(base)
    d['edit_applied'] = True
    viol = validate_delta(d, ledger)
    C('C', 'EDIT CONTROL a delta claiming the ledger was edited must be '
           'REJECTED', 'CHANNEL_MUST_NOT_EDIT_THE_LEDGER' in viol, viol)

    # --- FREEZE CONTROL -------------------------------------------------
    d = _clone(base)
    d['row_deltas'][0]['summary_after'] = 'something else'
    viol = validate_delta(d, ledger)
    C('C', 'FREEZE CONTROL rewriting a row summary must be REJECTED',
      any('FREEZE_RULE_VIOLATION' in x for x in viol), viol)

    # --- DISCRIMINATION: the validator is not a rubber stamp -------------
    C('C', 'CONTROL the validator distinguishes: the real delta yields 0 '
           'violations while every planted control yields >= 1',
      validate_delta(base, ledger) == [])


# ===========================================================================
# 6. BUCKET SPLIT -- checked against the artifact, not asserted freely
# ===========================================================================

def section_6():
    delta = RESULT['_delta']
    c = delta['counts']
    C('E', 'bucket split is not uniform: 1 wholly (a), 3 mixed (a)+(b), 0 (c)',
      c['bucket_a_wholly'] == 1 and c['bucket_a_b_mixed'] == 3 and
      c['bucket_c'] == 0, c)
    C('E', 'AC-F1 revival_trigger carries NO lexicon token -- its head demand '
           'is bucket (b), which is why the re-typing is declined',
      not lexicon_hits({'revival_trigger':
                        RESULT['_by_id']['AC-F1']['revival_trigger']},
                       ['revival_trigger']),
      RESULT['_by_id']['AC-F1']['revival_trigger'])
    C('E', "LT-GR2c's positivity modifies a normalized global functional -- "
           'homonym, declined',
      'normalized global functional' in
      RESULT['_by_id']['LT-GR2c']['revival_trigger'])
    C('E', 'RA-D2 carries the source-stated VEV conditional and is already '
           'typed at maximum severity, OVER_DETERMINED / GENUINE_FALSIFICATION',
      RESULT['_by_id']['RA-D2']['verdict'] == 'OVER_DETERMINED' and
      RESULT['_by_id']['RA-D2']['reason_kind'] == 'GENUINE_FALSIFICATION')
    C('E', 'RA-D2 is correctly OUTSIDE class P',
      'RA-D2' not in RESULT['class_P'])
    C('E', 'LT-SM8 stays in next_work_queue after the delta (queue position is '
           'binding, see hostile review H1)',
      any('LT-SM8' in q['rows'] for q in RESULT['_ledger']['next_work_queue']))


# ===========================================================================
# FAILURE PATH -- planted FALSE FACTS, each must drive exit 1
# ===========================================================================

MUTATIONS = ['class_p_size', 'class_h_size', 'intersection', 'ghost_token',
             'krein_demand', 'launder', 'advance', 'stale_before', 'debt_note',
             'artifact_sha', 'nonvacuous']


def selftest():
    ok = True
    fired = 0
    for m in MUTATIONS:
        env = dict(os.environ, ITC_MUTATE=m)
        p = subprocess.run([sys.executable, os.path.abspath(__file__)],
                           env=env, capture_output=True, text=True)
        good = p.returncode == 1
        fired += 1 if good else 0
        print('  mutation %-14s exit %d  %s'
              % (m, p.returncode, 'OK' if good else 'FAILED TO FIRE'))
        ok = ok and good
    print('\nFAILURE-PATH SELFTEST: %s (%d/%d planted false facts drove exit 1)'
          % ('PASS' if ok else 'FAIL', fired, len(MUTATIONS)))
    return 0 if ok else 1


def main():
    if '--selftest' in sys.argv:
        return selftest()
    section_0()
    section_1()
    section_2()
    section_3()
    section_4()
    section_5()
    section_6()

    scratch = dict((k, v) for k, v in RESULT.items() if not k.startswith('_'))
    assert_no_float(scratch)

    npass = sum(1 for t, n, ok, d in CERT if ok)
    ntot = len(CERT)
    counts = {}
    for t, n, ok, d in CERT:
        counts[t] = counts.get(t, 0) + 1
    for t, n, ok, d in CERT:
        if not ok:
            print('FAIL [%s] %s   detail=%s' % (t, n, d))
    print()
    print('IT-C  positivity-row typing, base conditional-physics-ledger-v0.258')
    print('  ledger sha256        %s' % RESULT['ledger_sha256'])
    print('  class P              %d  %s'
          % (len(RESULT['class_P']), sorted(RESULT['class_P'])))
    print("  class P'             %d  (adds %s)"
          % (len(RESULT['class_P_prime']),
             sorted(set(RESULT['class_P_prime']) - set(RESULT['class_P']))))
    print('  class H (BD-D)       %d  intersection with P = %d %s'
          % (len(RESULT['class_H']), len(RESULT['P_intersect_H']),
             RESULT['P_intersect_H']))
    print('  zero-count tokens    %d of %d lexicon tokens absent from all 84 '
          'rows' % (len(ZERO_TOKENS), len(LEXICON)))
    print('  Krein in a demand    %d rows' % len(RESULT['krein_demand_rows']))
    print('  rows moving status   %d  %s'
          % (len(RESULT['retype_ids']), RESULT['retype_ids']))
    print('  rows advanced        0     denominator move: none')
    print('  delta violations     %d' % len(RESULT['violations']))
    print('  split                ' +
          '  '.join('[%s] %d' % (k, v) for k, v in sorted(counts.items())))
    print()
    if npass == ntot:
        print('CERTIFICATE: %d/%d checks pass; no load-bearing float (swept). '
              'A re-typing is not an advance.' % (npass, ntot))
        return 0
    print('CERTIFICATE: %d/%d checks pass -- FAILURES ABOVE.' % (npass, ntot))
    return 1


if __name__ == '__main__':
    sys.exit(main())
