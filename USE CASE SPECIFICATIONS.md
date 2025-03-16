# Use Case Specifications - Cybersecurity Incident Tracker

## Use Case 1: Log Security Incident

**Actor:** Security Analyst  
**Precondition:** Analyst is logged in and authorized to report incidents.  
**Postcondition:** Incident is logged and assigned a unique ID.

### **Basic Flow:**

1. The analyst selects "Log Incident."
2. The system prompts for incident details (type, severity, description).
3. The analyst enters details and submits.
4. The system assigns a unique incident ID.
5. The system notifies the SOC Manager.

### **Alternative Flow:**

- **Invalid Input:** If required fields are empty, the system prompts the user to complete them.

---

## Use Case 2: Assign Case to Analyst

**Actor:** SOC Manager  
**Precondition:** Incident must be logged in the system.  
**Postcondition:** The case is assigned to an analyst.

### **Basic Flow:**

1. The SOC Manager selects an unassigned incident.
2. The system displays a list of available analysts.
3. The SOC Manager assigns the case.
4. The system sends a notification to the assigned analyst.

### **Alternative Flow:**

- **If no analysts are available,** the system suggests escalation.

---

## Use Case 3: Generate Security Report

**Actor:** Executive  
**Precondition:** The system contains logged incidents.  
**Postcondition:** A report is generated in PDF format.

### **Basic Flow:**

1. The Executive selects "Generate Report."
2. The system retrieves all incidents from the database.
3. The report is formatted and exported as a PDF.
4. The system sends the report via email.

### **Alternative Flow:**

- **If no data is available,** the system notifies the user.

---

## Use Case 4: Update Incident Status

**Actor:** Security Analyst  
**Precondition:** The incident must already be logged.  
**Postcondition:** The incident status is updated.

### **Basic Flow:**

1. The Security Analyst selects an incident.
2. The system displays the current status.
3. The analyst updates the status (e.g., "In Progress," "Resolved").
4. The system saves the new status.
5. The SOC Manager is notified.

### **Alternative Flow:**

- **Unauthorized Access:** If the user does not have permission, an error message is displayed.

---

## Use Case 5: Review Audit Logs

**Actor:** Compliance Officer  
**Precondition:** The system contains security event logs.  
**Postcondition:** The audit logs are displayed.

### **Basic Flow:**

1. The Compliance Officer logs into the system.
2. The officer navigates to "Audit Logs."
3. The system retrieves and displays logs.
4. The officer filters logs based on time and severity.
5. The officer exports the logs if needed.

### **Alternative Flow:**

- **No Logs Available:** If no logs exist, the system displays a message.

---

## Use Case 6: Authenticate User

**Actor:** End User, IT Admin  
**Precondition:** The user must have an account.  
**Postcondition:** The user is granted system access.

### **Basic Flow:**

1. The user enters their username and password.
2. The system verifies the credentials.
3. The system requests multi-factor authentication (MFA).
4. The user enters the MFA code.
5. The system grants access.

### **Alternative Flow:**

- **Incorrect Password:** The system displays an error and allows retry.
- **MFA Failure:** If the user fails MFA, they must reset their authentication method.

---

## Use Case 7: Manage Users

**Actor:** IT Admin  
**Precondition:** The admin must have administrator privileges.  
**Postcondition:** User accounts are updated.

### **Basic Flow:**

1. The IT Admin selects "User Management."
2. The system displays a list of users.
3. The admin selects a user to modify (add, update, delete).
4. The system applies the changes.
5. The system logs the changes for audit purposes.

### **Alternative Flow:**

- **Insufficient Privileges:** If a non-admin attempts this, the system denies access.

---

## Use Case 8: Integrate with SIEM

**Actor:** IT Admin  
**Precondition:** The system must support integration settings.  
**Postcondition:** The SIEM system is linked to the Incident Tracker.

### **Basic Flow:**

1. The IT Admin navigates to "System Settings."
2. The admin selects "SIEM Integration."
3. The system prompts for API credentials.
4. The admin enters SIEM API details and submits.
5. The system tests and establishes a connection.
6. SIEM alerts start syncing with the Incident Tracker.

### **Alternative Flow:**

- **Invalid Credentials:** If API keys are incorrect, the system displays an error.
- **Connection Failure:** If the SIEM system is unreachable, an error is logged.

---
