# Test Cases - Cybersecurity Incident Tracker

## **Functional Test Cases**

| Test Case ID | Requirement ID | Description | Steps | Expected Result | Actual Result | Status (Pass/Fail) |
|-------------|---------------|-------------|-------|-----------------|---------------|-------------------|
| TC-001 | FR-001 | Log a security incident | 1. Login as Analyst 2. Click "Log Incident" 3. Enter details 4. Submit | Incident is logged successfully | - | - |
| TC-002 | FR-002 | Assign case to analyst | 1. Login as SOC Manager 2. Select an incident 3. Assign to analyst | Analyst receives a notification | - | - |
| TC-003 | FR-003 | Generate security report | 1. Login as Executive 2. Click "Generate Report" | PDF report is generated | - | - |
| TC-004 | FR-004 | Update incident status | 1. Login as Analyst 2. Select an incident 3. Update status 4. Submit | Status is updated and notification is sent | - | - |
| TC-005 | FR-005 | Review audit logs | 1. Login as Compliance Officer 2. Navigate to "Audit Logs" 3. Filter logs and export | Logs are filtered and exported | - | - |
| TC-006 | FR-006 | Authenticate user | 1. Enter username and password 2. Complete MFA | User is granted system access | - | - |
| TC-007 | FR-007 | Manage users | 1. Login as IT Admin 2. Select "User Management" 3. Modify a user account | User account is updated | - | - |
| TC-008 | FR-008 | Integrate with SIEM | 1. Login as IT Admin 2. Navigate to "System Settings" 3. Enter SIEM credentials 4. Submit | SIEM system is integrated | - | - |

---

## **Non-Functional Test Cases**

| Test Case ID | Requirement ID | Description | Steps | Expected Result | Actual Result | Status (Pass/Fail) |
|-------------|---------------|-------------|-------|-----------------|---------------|-------------------|
| TC-NF-001 | NFR-001 | System must support 1,000 concurrent users | Simulate 1,000 users logging in | System remains stable | - | - |
| TC-NF-002 | NFR-002 | Incident logs must be encrypted | Submit an incident log | Data is encrypted with AES-256 | - | - |
