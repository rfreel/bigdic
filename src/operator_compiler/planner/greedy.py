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
                    base += self.interactions.order_effect(prev,op,state)
                    base += 0.02*self.estimator.store.macro_edges.get((prev,op),0)
                return base
            available=[op for op in remaining if self.feasible(tuple(seq)+(op,),state)]
            if not available:
                return self.infeasible()
            chosen=max(available,key=key)
            seq.append(chosen); remaining.remove(chosen)
        result=self.score_sequence(tuple(seq),state)
        return result
