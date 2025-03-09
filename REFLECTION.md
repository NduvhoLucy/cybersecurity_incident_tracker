# Reflection: Challenges in Balancing Stakeholder Needs

## 1. Conflicting Priorities
- **Security Analysts** wanted a simple, fast UI, while **Compliance Officers** required detailed documentation, which made the interface complex.
- **Solution:** We added an "Advanced View" for compliance officers while keeping the UI simple for analysts.

## 2. Scalability vs. Performance
- The **Executives** wanted real-time reporting, but **IT Admins** warned about database performance issues.
- **Solution:** We optimized database indexing and caching to speed up queries.

## 3. Security vs. Usability
- **End Users** preferred a quick login, but **SOC Managers** required strict security (MFA, session timeouts).
- **Solution:** We made MFA mandatory only for administrators and optional for regular users.

## 4. Integration with SIEM Tools
- **SOC Managers** needed automatic incident creation, but **IT Admins** feared system overload from false positives.
- **Solution:** We implemented a threshold filter to reduce false alarms.
