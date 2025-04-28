# CHANGELOG

All notable changes to the Cybersecurity Incident Tracker project will be documented here.

---

## [1.0.0] - Initial Setup
### Added
- Added core classes: `User`, `Incident`, `Case`, `AuditLog`, `Report`, `Notification`, `SIEMIntegration`.
- Defined class attributes and methods based on UML diagrams.

---

## [1.1.0] - Creational Patterns Implementation
### Added
- Added **Simple Factory** pattern for dynamic creation of `Incident` and `Report` objects.
- Added **Factory Method** pattern for sending notifications via `Email` and `SMS`.
- Added **Abstract Factory** pattern for rendering dashboards based on user roles (Admin, Analyst).
- Added **Builder** pattern for flexible creation of `Report` objects.
- Added **Prototype** pattern for cloning `Case` objects quickly.
- Added **Singleton** pattern to ensure only one `SIEMConnection` instance exists.

---

## [1.2.0] - Unit Testing
### Added
- Wrote unit tests for each design pattern under `/tests/` directory.
- Test cases for object creation, cloning, singleton validation, and building reports.

---

## [1.3.0] - Improvements
### Fixed
- Fix #14: Singleton `SIEMConnection` made thread-safe for multiple accesses.
- Minor improvements to code readability and error handling inside Factory classes.

---

## [1.4.0] - Documentation
### Added
- Created `README.md` with project overview, language choice, and design pattern explanations.
- Created this `CHANGELOG.md` to track progress and project updates.

---

