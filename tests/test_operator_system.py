import unittest
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import operator_system as op
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
if __name__=='__main__': unittest.main()
