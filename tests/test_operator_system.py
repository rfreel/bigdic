import unittest
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import operator_system as op
import continuation
class OperatorSystemTests(unittest.TestCase):
    def test_catalog_complete_and_reproducible_proxy(self):
        c=op.catalog()
        self.assertEqual((len(c['entries']),sum(x['origin']=='V2' for x in c['entries'])),(803,794))
        self.assertEqual(len({e['name'] for e in c['entries']}),803)
    def test_request_proposes_without_claiming_execution(self):
        x=op.packet('Repair the failing code and verify the result')
        self.assertIn('REPAIR',[c['macro'] for c in x['macro_candidates']])
        self.assertFalse(x['verified'])
        self.assertIsNone(x['receipt'])
        self.assertFalse(x['authority_granted'])
    def test_unknown_cue_remains_open(self):
        self.assertEqual(op.packet('Help with this')['macro_candidates'],[])
    def test_local_terms_are_marked(self):
        terms={x['name']:x for x in op.catalog()['entries']}
        self.assertEqual(terms['DISINHIBITIZE']['origin'],'LOCAL')
        self.assertEqual(terms['PREWALK']['origin'],'LOCAL')
    def test_consequence_role_does_not_claim_source_membership(self):
        roles=op.consequence_lookup('FALSIFIER')
        self.assertEqual(len(roles),1)
        self.assertEqual(roles[0]['role'],'test_or_stop_rule')
        self.assertEqual(roles[0]['term_type'],'defeat_condition')
        self.assertEqual(op.consequence_lookup('KILL-CRITERION')[0]['term_type'],'decision_rule')
        addition=op.consequence_lookup('DECISION-PARTITION')[0]
        self.assertEqual(addition['term_type'],'parametric_extension')
        self.assertIn('acceptable actions',addition['change'])
        self.assertEqual(roles[0]['status'],'PARAMETRIC_WORKING_MODEL')
        self.assertEqual(op.consequence_lookup('not-a-term'),[])
    def test_common_action_does_not_suppress_worthwhile_probe(self):
        result=continuation.choose_continuation(common_action=True,action_authorized=True,
            acceptance_checked=True,effects_bounded=True,probe_available=True,
            probe_can_change_decision=True,probe_worthwhile=True,probe_within_budget=True)
        self.assertEqual(result['choice'],'PROBE')
    def test_unknown_probe_value_defers_even_with_common_action(self):
        result=continuation.choose_continuation(common_action=True,action_authorized=True,
            acceptance_checked=True,effects_bounded=True,probe_available=True,
            probe_can_change_decision=None,probe_worthwhile=None,probe_within_budget=True)
        self.assertEqual(result['choice'],'DEFER')
    def test_act_requires_checked_authority_acceptance_and_bounded_effects(self):
        result=continuation.choose_continuation(common_action=True,action_authorized=False,
            acceptance_checked=True,effects_bounded=True,probe_available=False,
            probe_can_change_decision=None,probe_worthwhile=None,probe_within_budget=None)
        self.assertEqual(result['choice'],'DEFER')
    def test_ready_common_action_can_proceed_when_probe_has_no_decision_value(self):
        result=continuation.choose_continuation(common_action=True,action_authorized=True,
            acceptance_checked=True,effects_bounded=True,probe_available=True,
            probe_can_change_decision=False,probe_worthwhile=None,probe_within_budget=True)
        self.assertEqual(result['choice'],'ACT')
if __name__=='__main__': unittest.main()
