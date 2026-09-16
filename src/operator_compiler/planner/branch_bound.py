from .common import PlannerBase

class BranchBoundPlanner(PlannerBase):
    name="branch_bound"
    def plan(self,state):
        required=tuple(dict.fromkeys(state.required_operators)); best=self.score_sequence((),state)
        max_remaining={op:max(0,self.estimator.store.shapley.get(op,0)) for op in required}
        def dfs(seq,remaining):
            nonlocal best
            r=self.score_sequence(seq,state)
            if not remaining:
                if r.total_value>best.total_value: best=r
                return
            upper=r.total_value+sum(max_remaining[o] for o in remaining)
            if upper<best.total_value: return
            for op in remaining:
                n=seq+(op,)
                if self.feasible(n,state): dfs(n,tuple(x for x in remaining if x!=op))
        dfs((),required)
        return best
