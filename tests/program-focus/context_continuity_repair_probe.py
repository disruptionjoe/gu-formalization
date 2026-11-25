"""Continuity controls: live facts change without rewriting policy or replaying dispatches."""
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('context', ROOT/'scripts/research_context.py')
context = importlib.util.module_from_spec(spec)
spec.loader.exec_module(context)


class Continuity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.state = yaml.safe_load((ROOT/'CURRENT-STATE.yaml').read_text())
        cls.matrix = json.loads((ROOT/context.MATRIX).read_text())

    def render(self, matrix, history=False):
        text = context.render_context(self.state, '', matrix=matrix, history=history)
        return yaml.safe_load(text.split('```yaml\n', 1)[1].split('```', 1)[0])

    def test_counter_changes_without_policy_edit(self):
        for count, due in [(41, False), (43, True), (44, False)]:
            matrix = deepcopy(self.matrix)
            matrix['program_run_counter']['count'] = count
            result = self.render(matrix)
            self.assertEqual(result['live_facts']['counter'], count)
            self.assertEqual(result['live_facts']['ordinary_LC_arithmetic_condition'], due)
            self.assertEqual(result['program_focus'], self.state['program_focus'])

    def test_dispatch_history_is_consumed_not_policy(self):
        selection = self.state['program_focus']['priority_packet_selection']
        self.assertFalse(any(k.startswith('directed_') for k in selection))
        self.assertIn('normal-L2 necessity', selection['localization_promotion'])
        result = self.render(self.matrix)
        records = result['live_facts']['consumed_directions']
        self.assertEqual(len(records), 6)
        self.assertTrue(all(r['status'] == 'consumed' and r['evidence'] for r in records))
        self.assertTrue(all('original_direction' not in r for r in records))
        self.assertIn('original_direction', self.render(self.matrix, True)['history_not_live_selection']['priority_direction_history']['directions'][0])

    def test_completed_benchmark_does_not_complete_native_application(self):
        horizon = json.loads((ROOT/'lab/process/ten-wave-source-falsification-2026-11-24.json').read_text())
        w = next(w for w in horizon['waves'] if w['id'] == 'W08')
        self.assertEqual(w['status'], 'blocked')
        self.assertEqual(len(w['completed_subtests']), 2)
        self.assertIn('physical constraints/quotient', w['remaining_input'])
        self.assertIn('Reuse', w['first_decisive_test'])
        self.assertNotIn('Count39', '\n'.join(horizon['recommended_next_workset']))

    def test_missing_links_and_class_width_stay_visible(self):
        facts = self.render(self.matrix)['live_facts']
        self.assertTrue(facts['class_C_representativeness'])
        self.assertEqual(len(facts['shared_prerequisites']), 5)
        self.assertIn('not permission to block', facts['shared_prerequisites'][-1]['scope'])
        self.assertIn('withdrawn', facts['follow_through']['correction_ranking_check']['correction'])
        for group in facts['shared_prerequisites']:
            self.assertTrue(group['evidence'])


if __name__ == '__main__':
    unittest.main()
