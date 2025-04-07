## Markdown Explanation – Object State Diagrams

The state diagrams illustrate how each object transitions through various states in the Cybersecurity Incident Tracker system. These models are essential in mapping functional requirements (FRs) to system behavior and ensuring every user interaction and system process is traceable, testable, and aligned with Agile best practices.

### 1. **Incident Object**
The Incident object flows from creation (`New`) to various stages of investigation (`Under Investigation`, `Escalated`) and resolution (`Resolved`, `Closed`, `Archived`). These states help map incident lifecycles and support FR-001 (logging), FR-002 (assignment), and FR-004 (tracking). High-severity incidents move to `Escalated`, enforcing managerial oversight.

### 2. **Case Object**
The Case object transitions from `Open` to `Assigned`, and then into investigative stages like `In Progress` or `Waiting For Input`. Once addressed, it moves through `Resolved`, `Verified`, and `Closed`. These states ensure full visibility over incident case progression and align with FR-003 and FR-004 for managing workloads and updating statuses.

### 3. **User Account Object**
User accounts start as `Pending Approval`, and move to `Active` upon validation. They can be `Suspended` due to policy violations, `Reactivated` by admins, or `Deactivated` permanently. These transitions align with FR-007, supporting secure account lifecycle management.

### 4. **Audit Log Object**
The Audit Log object moves from `Capturing` to `Stored`, then `Reviewed`, and finally `Archived`. This traceable flow meets FR-006, ensuring compliance and proper handling of system logs for auditing purposes.

### 5. **Report Object**
Reports are drafted by users, go through `In Review`, then become `Approved`, `Published`, and ultimately `Archived`. These transitions support FR-005, providing a controlled path for creating and disseminating reports with appropriate review and retention stages.

### 6. **SIEM Integration Object**
This object handles external integration status. It starts at `Configuring`, becomes `Active` when linked successfully, and handles errors with states like `Error`, `Retrying`, or `Disabled`. These transitions directly support FR-008, which addresses real-time integration with third-party SIEM systems.

### 7. **Authentication Token Object**
Authentication tokens are `Issued`, become `Active`, and either `Expire`, get `Renewed`, or are `Revoked` due to inactivity or security triggers. These flows reflect FR-009, which governs session handling and security enforcement.

### 8. **Notification Object**
Notifications go from `Created` to `Delivered`, and are either `Acknowledged` or remain `Unread`. Eventually, all notifications move to `Archived`. These states support FR-010, ensuring users receive timely alerts and the system maintains clean records.

---
