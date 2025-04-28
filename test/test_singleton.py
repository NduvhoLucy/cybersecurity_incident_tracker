from creational_patterns.singleton import SIEMConnection

def test_singleton_connection():
    conn1 = SIEMConnection("Splunk")
    conn2 = SIEMConnection("Another SIEM")

    assert conn1 is conn2  # Same instance
    assert conn1.tool_name == "Splunk"  # Original value persists
