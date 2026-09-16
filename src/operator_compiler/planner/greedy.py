from .common import PlannerBase

class GreedyPlanner(PlannerBase):
    name = "greedy"
    def plan(self, state):
        remaining = list(dict.fromkeys(state.required_operators))
        seq=[]
        while remaining:
            prev = seq[-1] if seq else None
            def key(op):
                base=self.estimator.store.shapley.get(op,0.0)-self.estimator.store.base_cost(op)
                if prev:
                    base += self.interactions.synergy(prev,op,state)
                    base += 0.02*self.estimator.store.macro_edges.get((prev,op),0)
                return base
            chosen=max(remaining,key=key)
            seq.append(chosen); remaining.remove(chosen)
        result=self.score_sequence(tuple(seq),state)
        if result.total_cost > state.budget:
            seq=tuple(op for op in state.required_operators if self.estimator.store.base_cost(op)<=state.budget)
            return self.score_sequence(seq,state)
        return result
