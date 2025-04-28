from creational_patterns.prototype import CasePrototype

def test_clone_case():
    original_case = CasePrototype(case_id="CASE001", analyst_id="analyst123")
    cloned_case = original_case.clone()

    assert cloned_case.case_id == "CASE001"
    assert cloned_case.analyst_id == "analyst123"
    assert cloned_case.status == "Open"
    assert cloned_case is not original_case  # Should be a different object
