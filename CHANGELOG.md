# Changelog

All notable changes to the LaunchBoards pointer repository and branding documentation will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.1] - 2026-09-18

### Added
- **GitHub Actions CI/CD Workflows:** Implemented complete CI matrix pipeline in `.github/workflows/ci.yml` (multi-OS testing on `ubuntu-latest` and `windows-latest`, Python 3.10 to 3.13 matrix, `timeout-minutes: 15`, concurrency cancellation, and least-privilege `contents: read`), automated stale triage in `.github/workflows/stale.yml` (`actions/stale@v9`, `timeout-minutes: 10`, `issues: write, pull-requests: write`), and contributor welcome automation in `.github/workflows/welcome.yml` (`actions/first-interaction@v3`, `timeout-minutes: 5`).
- **PEP 621 Standard Build & Metadata:** Hardened `pyproject.toml` with standard `[build-system]` (`setuptools>=68.0`, `wheel`), `license-files`, discovery `keywords`, comprehensive `classifiers` (Python 3.10-3.13, Windows, OS Independent), optional dev dependencies (`[project.optional-dependencies]`), and tool configurations (`ruff`, `pytest` with `norecursedirs`).
- **Statutory Legal Notice (§ 521 BGB):** Explicitly documented German statutory liability notice for gratuitous open-source provisions (§ 521 BGB Gefälligkeitsrecht) in `README_de.md` and equivalent international disclaimer in `README.md`.
- **Contract Verification Expansion:** Added new automated contract tests in `tests/test_metadata.py` verifying CI workflow configurations, multi-host and multi-agent lock patterns in `.gitignore`, PEP 621 metadata completeness, and statutory legal notices.

### Changed
- **Multi-Host & Lock Guardrails:** Hardened `.gitignore` with fleet-standard conflict patterns (`*conflicted copy*`, `* (Kopie)*`, `* (Copy)*`, `*-ASUS*`, `*-ASUS-GEI*`, `*-LAPTOP*`, `*-WORKSTATION*`, `*-WORKSTATION-LG*`, `*-Mac Studio*`, `*-MacBook*`) and coordination locks (`LOCK.permissions.json`, `LOCK.user.*`, `LOCK.until.*`, `LOCK.condition.*`, `uv.lock`, `!package-lock.json`).
- **Badge Suite & Manifest Parity:** Updated release badges to `v1.2.1`, added CI passing badge, refreshed contract test count badges, and synchronized version metadata across `pyproject.toml`, `llms.txt`, `THIRD_PARTY_LICENSES.md`, and `MARKETING-LOG.txt`.
- **Code Quality & Linter Compliance:** Resolved f-string warnings in `tests/test_metadata.py` achieving 100% clean `ruff check .` status.

---

## [1.2.0] - 2026-09-14

### Added
- **Target Personas & SEO Discovery:** Formalized 4 concrete target personas (`[PERSONA-01]` Multi-Project Software Engineers & DevOps Practitioners, `[PERSONA-02]` Privacy-First Desktop Power Users & Researchers, `[PERSONA-03]` Creative Directors & Multimedia Producers, and `[PERSONA-04]` System Administrators & Homelab Operators) alongside high-intent search query matrices in `README.md` and `README_de.md`.
- **10-Dimension Comparative Matrix:** Benchmarked LaunchBoards against Windows Start Menu / Taskbar, Microsoft PowerToys Run / Flow Launcher, Stardock Fences, and Cloud Dashboard SaaS (Notion / Start.me) directly mapped to `INV-LOCAL-01` through `INV-LOCAL-10`.
- **Third-Party License Audit (`THIRD_PARTY_LICENSES.md`):** Comprehensive SPDX dependency catalog for Python (`PSF-2.0`), PySide6 / Qt 6 (`LGPL-3.0-only`), pytest (`MIT`), and ruff (`MIT OR Apache-2.0`). Formally verified PySide6 dynamic linking compliance under § 4 LGPLv3, unprivileged `RunAsInvoker` runtime execution, and Zero-Copyleft guarantee for user data.
- **PEP 621 Standard URLs:** Added `Marketing Log` and `Third-Party Licenses` repository links to `pyproject.toml`.
- **Expanded Contract Verification:** Extended automated test suite in `tests/test_metadata.py` from 8 to 16 contract tests covering quick navigation reciprocity, persona declarations, comparative matrix mappings, SPDX audits, and version synchrony.

### Changed
- **Bilingual Navigation Parity:** Expanded Quick Navigation to 14 reciprocal items in both English (`README.md`) and German (`README_de.md`).
- **Badge Suite Modernization:** Updated Shields.io release badge to `v1.2.0`, added `Third-Party Licenses - Audited (MIT/LGPLv3)`, `Tests - 16 passed | 100%`, `Privileges - RunAsInvoker`, and `Network - Zero Egress`.
- **AI Discoverability:** Updated `llms.txt` to version 1.2.0 with persona summaries, comparative matrix reference, and test counts.

---

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
