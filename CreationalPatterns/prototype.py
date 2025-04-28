import copy

class CasePrototype:
    def __init__(self, case_id, analyst_id, status="Open"):
        self.case_id = case_id
        self.analyst_id = analyst_id
        self.status = status

    def clone(self):
        return copy.deepcopy(self)
