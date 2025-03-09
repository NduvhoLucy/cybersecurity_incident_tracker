# Functional Requirements - Cybersecurity Incident Tracker

## 1. Incident Management
1. **The system shall allow security analysts to log security incidents with severity levels.**  
   - **Acceptance Criteria:** Analysts can categorize incidents as "Low," "Medium," or "High."

2. **The system shall allow users to attach evidence (logs, screenshots) to incidents.**  
   - **Acceptance Criteria:** Users can upload files up to 10MB.

3. **The system shall provide real-time notifications for new security incidents.**  
   - **Acceptance Criteria:** Alerts are sent via email and system dashboard.

## 2. Case Assignment & Tracking
4. **The system shall allow SOC Managers to assign security incidents to analysts.**  
   - **Acceptance Criteria:** Assigned analysts receive a notification.

5. **The system shall track the progress of security incidents until resolution.**  
   - **Acceptance Criteria:** Incidents have statuses: "Open," "In Progress," "Resolved."

## 3. Reporting & Audit
6. **The system shall generate audit logs for all incident actions.**  
   - **Acceptance Criteria:** Logs contain timestamps, users, and action details.

7. **The system shall provide a dashboard for security metrics (e.g., number of incidents per month).**  
   - **Acceptance Criteria:** Executives can generate reports for any time period.

## 4. SIEM Integration
8. **The system shall integrate with Splunk and Microsoft Sentinel for automatic incident detection.**  
   - **Acceptance Criteria:** SIEM alerts trigger incidents in the tracker.

## 5. User Management & Authentication
9. **The system shall support role-based access control (RBAC).**  
   - **Acceptance Criteria:** Only authorized users can view/edit incidents.

10. **The system shall require multi-factor authentication (MFA) for all logins.**  
   - **Acceptance Criteria:** Users must enter a one-time password (OTP) via email.  
