# Cybersecurity Incident Tracker – Creational Design Patterns

## Project Overview
The Cybersecurity Incident Tracker is a secure platform designed to help security teams track incidents, manage cases, generate reports, and ensure compliance through audit logging and notifications.  
This project also demonstrates the use of **six creational design patterns** to promote modularity, scalability, and maintainability.

---

## Language Choice: Python 🐍

I selected **Python** for this project because:
- Python allows for rapid development with clean and readable syntax.
- Python is highly suitable for object-oriented design and prototyping.
- Libraries like `pytest` and easy integration with GitHub Actions make it ideal for testing Agile-based projects.

---

## Creational Patterns Used

| Pattern           | Class Name         | Use Case in System                          |
|-------------------|--------------------|--------------------------------------------|
| Simple Factory    | `ObjectFactory`     | Quickly create `Incident` or `Report` objects dynamically. |
| Factory Method    | `NotificationFactory` | Create notifications for users via Email or SMS. |
| Abstract Factory  | `RoleUIFactory`     | Create different user interface components based on user role (Admin or Analyst). |
| Builder           | `ReportBuilder`     | Step-by-step build of complex `Report` objects with optional fields. |
| Prototype         | `CasePrototype`     | Clone existing `Case` objects for faster incident handling. |
| Singleton         | `SIEMConnection`    | Ensure a single integration with external SIEM systems (Splunk, Sentinel). |

---

## Quick Explanation of Each Pattern

### 1. Simple Factory – `ObjectFactory`
- Centralizes object creation for Incidents and Reports.
- Reduces direct dependency on specific classes.

### 2. Factory Method – `NotificationFactory`
- Encapsulates how different types of notifications (Email, SMS) are created.
- Each notification subclass defines its own `send()` method.

### 3. Abstract Factory – `RoleUIFactory`
- Provides a family of related UI components (Admin or Analyst dashboards).
- Makes the system extensible for new user types in the future.

### 4. Builder – `ReportBuilder`
- Separates construction of a `Report` object from its representation.
- Useful when reports have optional or complex configurations.

### 5. Prototype – `CasePrototype`
- Enables cloning of `Case` objects without depending on their concrete class.
- Speeds up case creation for similar incidents.

### 6. Singleton – `SIEMConnection`
- Ensures only one active connection to the external SIEM system.
- Saves resources and avoids redundant integrations.

---

## Folder Structure

