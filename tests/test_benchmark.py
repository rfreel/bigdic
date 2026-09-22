import json,tempfile,unittest
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1] / 'benchmarks'))
from evaluate import load,analyze
class BenchmarkTests(unittest.TestCase):
 def row(self,task,condition,success):
  return dict(task_id=task,condition=condition,domain='repair',success=success,
              false_completion=False,input_tokens=10,output_tokens=5,tool_calls=1,
              wall_seconds=1.0,provenance='test-fixture')
 def test_paired_result_and_missing_partner(self):
  rows=[self.row('a','baseline',False),self.row('a','candidate',True),
        self.row('b','baseline',True)]
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'runs.jsonl';p.write_text(''.join(json.dumps(x)+'\n' for x in rows))
   x=analyze(load(p))['paired']
  self.assertEqual(x['complete_pairs'],1)
  self.assertEqual(x['missing_partner_task_ids'],['b'])
  self.assertEqual(x['mean_success_difference'],1)
  self.assertIsNone(x['paired_interval'])
 def test_empty_is_not_a_result(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'runs.jsonl';p.write_text('')
   with self.assertRaisesRegex(ValueError,'No observations'):load(p)
 def test_numeric_boolean_and_nonfinite_cost_are_rejected(self):
  for key,value in [('success',1),('false_completion',0),('wall_seconds',float('inf'))]:
   row=self.row('a','baseline',True);row[key]=value
   with self.subTest(key=key):
    with tempfile.TemporaryDirectory() as d:
     p=Path(d)/'runs.jsonl';p.write_text(json.dumps(row)+'\n')
     with self.assertRaisesRegex(ValueError,'invalid'):load(p)
 def test_same_condition_is_not_a_comparison(self):
  with self.assertRaisesRegex(ValueError,'different conditions'):
   analyze({('a','baseline'):self.row('a','baseline',True)},'baseline','baseline')
if __name__=='__main__':unittest.main()
