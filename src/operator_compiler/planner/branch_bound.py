from .common import PlannerBase

class BranchBoundPlanner(PlannerBase):
    name="branch_bound"
    def plan(self,state):
        required=tuple(dict.fromkeys(state.required_operators)); best=None
        def dfs(seq,remaining):
            nonlocal best
            r=self.score_sequence(seq,state)
            if not remaining:
                if best is None or r.total_value>best.total_value: best=r
                return
            for op in remaining:
                n=seq+(op,)
                if self.feasible(n,state): dfs(n,tuple(x for x in remaining if x!=op))
        dfs((),required)
        return best if best is not None else self.infeasible()
