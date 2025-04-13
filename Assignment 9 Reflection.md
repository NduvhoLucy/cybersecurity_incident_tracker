## Reflection: Designing Domain and Class Diagrams

### 1. Challenges in Abstraction and Design

Designing the domain model and class diagram for the Cybersecurity Incident Tracker posed a few conceptual challenges. The primary difficulty was in deciding the level of abstraction—especially how many entities to represent explicitly. For example, while SIEM tools, incident escalation, and notification workflows are distinct behaviors, modeling them as separate entities without overcomplicating the system required thoughtful balance.

Another challenge was defining appropriate class methods. Determining what actions should be class-level vs. process-driven (e.g., should `escalateIncident()` be on `Incident`, or part of a service?) required clear thinking about responsibility and cohesion. We focused on encapsulating responsibilities at the object level to maintain modularity.

### 2. Alignment with Previous Assignments

The class diagram aligns closely with earlier user stories and state/activity diagrams. For example, the `Incident` and `Case` objects map directly to workflows from Assignment 8 like "Log Incident" and "Update Status." The `User`, `Notification`, and `AuditLog` classes mirror use cases related to access control, escalation alerts, and auditing. This continuity demonstrates how object behavior (state transitions) and process flows (activity diagrams) inform structural design.

Furthermore, business rules in the domain model stem from functional requirements identified in Assignment 4 (e.g., “Only authorized users can create incidents” translates to method access restrictions in the `Incident` class).

### 3. Trade-offs in Modeling Inheritance vs. Composition

We chose composition over inheritance to maintain clarity and reduce class complexity. For instance, `Case` contains an `Incident` rather than inheriting from it. This reflects real-world ownership and simplifies reuse. Similarly, while roles like Analyst and Manager could be subclasses of `User`, role-based behavior is instead managed through the `role` attribute, simplifying the class structure and aligning with our agile and iterative development model.

### 4. Lessons Learned

This assignment reinforced the importance of clearly understanding system behaviors before modeling data structures. The class diagram is not just technical—it encapsulates the rules, policies, and workflows that stakeholders rely on. We learned that a good class diagram should not only represent code but also reflect real-world processes and responsibilities.

Maintaining alignment across state models, activity workflows, and class responsibilities results in better maintainability and traceability. This exercise solidified our understanding of object-oriented design principles and how they tie into system architecture, stakeholder needs, and agile planning.
