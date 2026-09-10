# Changelog

All notable changes to the LaunchBoards pointer repository and branding documentation will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-09-10

### Added
- **Visual Architecture & Lifecycle:** Integrated dual interactive Mermaid diagrams into `README.md` and `README_de.md` (Architecture & Profile Isolation flowchart + Workspace Launch Lifecycle sequence diagram).
- **Discoverability & Badges:** Added comprehensive Shields.io badge suite covering Python 3.10-3.12, PySide6 (Qt 6), Windows 10/11 platform, SoftwareCenter codebase relation, ecosystem umbrella, and security SLA.
- **System Invariants Matrix:** Documented formal 10-point governance matrix (`INV-LOCAL-01` through `INV-LOCAL-10`) covering zero egress, unprivileged execution, non-destructive shortcut handling, and profile isolation.
- **Bilingual Security Policy:** Added hardened `SECURITY.md` with committed 48-hour response SLA, 5-business-day triage commitment, and official disclosure contacts.
- **Machine-Readable AI Context:** Added `llms.txt` with structured project scope, disambiguation, invariants, and discovery keywords.
- **Repository Hygiene:** Added hardened `.gitignore` filtering out multi-host synchronization conflicts (`*-conflict-*`), multi-agent locks (`LOCK*`), and build artifacts.
- **Automated Verification:** Added contract test suite in `tests/test_metadata.py` ensuring bilingual parity, Mermaid syntax compliance, and link integrity.

### Changed
- **Quick Navigation:** Restructured landing page with standardized 11-point table of contents.
- **Getting Started:** Added clear step-by-step guidance for standalone executable download, running from source via `launchboards.py`, and local PyInstaller builds.

---

## [1.0.0] - 2026-08-01

### Added
- Initial release as canonical pointer repository for the LaunchBoards branding profile.
- Bilingual introduction (`README.md` and `README_de.md`) pointing to `file-bricks/SoftwareCenter`.
- MIT License.
