import heapq
from .common import PlannerBase

class AStarPlanner(PlannerBase):
    name="astar"
    def plan(self,state):
        required=tuple(dict.fromkeys(state.required_operators))
        heap=[(0.0,(),frozenset())]
        seen=set()
        while heap:
            neg,seq,used=heapq.heappop(heap)
            if used==frozenset(required): return self.score_sequence(seq,state)
            if (seq,used) in seen: continue
            seen.add((seq,used))
            for op in required:
                if op in used: continue
                n=seq+(op,)
                if not self.feasible(n,state): continue
                score=self.score_sequence(n,state).total_value
                remaining=sum(max(0,self.estimator.store.shapley.get(x,0)) for x in required if x not in used and x!=op)
                heapq.heappush(heap,(-(score+remaining),n,used|{op}))
        return self.score_sequence((),state)
