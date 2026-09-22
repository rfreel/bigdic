from .common import PlannerBase

class BeamPlanner(PlannerBase):
    name = "beam"
    def __init__(self, estimator, interactions, width=16):
        super().__init__(estimator, interactions); self.width=width
    def plan(self,state):
        required=tuple(dict.fromkeys(state.required_operators))
        beam=[()]
        for _ in range(len(required)):
            cand=[]
            for seq in beam:
                for op in required:
                    if op not in seq:
                        n=seq+(op,)
                        if self.feasible(n,state): cand.append(n)
            beam=sorted(cand,key=lambda s:self.score_sequence(s,state).total_value,reverse=True)[:self.width]
        return max((self.score_sequence(s,state) for s in beam),key=lambda r:r.total_value) if beam else self.infeasible()
