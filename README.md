<img src="https://raw.githubusercontent.com/file-bricks/SoftwareCenter/master/assets/banner.png" width="100%" alt="LaunchBoards Banner">

# LaunchBoards

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/file-bricks/SoftwareCenter/releases"><img src="https://img.shields.io/badge/Release-v1.2.0-blue.svg" alt="Latest Release"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-3776AB.svg?logo=python&logoColor=white" alt="Python 3.10 | 3.11 | 3.12"></a>
  <a href="https://doc.qt.io/qtforpython-6/"><img src="https://img.shields.io/badge/UI-PySide6%20(Qt%206)-41CD52.svg?logo=qt&logoColor=white" alt="PySide6 UI"></a>
  <a href="https://www.microsoft.com/windows"><img src="https://img.shields.io/badge/Platform-Windows%2010%20%7C%2011-0078D6.svg?logo=windows&logoColor=white" alt="Platform: Windows"></a>
  <a href="https://github.com/file-bricks/SoftwareCenter"><img src="https://img.shields.io/badge/Codebase-SoftwareCenter-orange.svg" alt="Sister Product Codebase"></a>
  <a href="https://github.com/file-bricks"><img src="https://img.shields.io/badge/Ecosystem-file--bricks-blue.svg" alt="Ecosystem: file-bricks"></a>
  <a href="https://github.com/open-bricks"><img src="https://img.shields.io/badge/Umbrella-open--bricks-purple.svg" alt="Umbrella: open-bricks"></a>
  <a href="SECURITY.md"><img src="https://img.shields.io/badge/Security-48h%20SLA-brightgreen.svg" alt="Security SLA"></a>
  <a href="llms.txt"><img src="https://img.shields.io/badge/LLM--Ready-llms.txt-success.svg" alt="LLM Context Available"></a>
</p>

---

<p align="center">
  <strong>Organize your app shortcuts into dedicated launch boards and start what you need, when you need it — fast, local-first, and zero telemetry.</strong>
</p>

<p align="center">
  <a href="README.md"><strong>English</strong></a> •
  <a href="README_de.md"><strong>Deutsch</strong></a>
</p>

---

## Quick Navigation

- [What is LaunchBoards?](#what-is-launchboards)
- [Why Two Names for One App?](#why-two-names-for-one-app)
- [Architecture & Profile Isolation](#architecture--profile-isolation)
- [Workspace Launch Lifecycle](#workspace-launch-lifecycle)
- [Core Features](#core-features)
- [Getting Started & How to Run](#getting-started--how-to-run)
- [System Invariants & Governance](#system-invariants--governance)
- [Canonical Repository & Contributing](#canonical-repository--contributing)
- [Ecosystem & Sister Projects](#ecosystem--sister-projects)
- [Security & Vulnerability Reporting](#security--vulnerability-reporting)
- [License](#license)

---

## What is LaunchBoards?

**LaunchBoards is a specialized second branding of [SoftwareCenter](https://github.com/file-bricks/SoftwareCenter)** — running the identical, battle-tested desktop codebase under a distinct application identity, custom app icon, and separate settings profile (`PROFILE_LAUNCHBOARDS`).

While traditional app launchers focus on browsing a flat directory of installed programs, **LaunchBoards** centers the workflow around **thematic workspaces ("Boards")**. You organize your everyday desktop shortcuts, utilities, IDEs, and project folders into tab-based boards (e.g. *Development*, *Design*, *Daily Office*, *Administration*), switching contexts with a single click.

> [!NOTE]
> LaunchBoards is not a fork or detached clone. It is an officially supported product profile of the canonical [SoftwareCenter](https://github.com/file-bricks/SoftwareCenter) codebase. Both brandings run concurrently without mutual interference.

---

## Why Two Names for One App?

SoftwareCenter and LaunchBoards represent two complementary conceptual framings of the exact same utility:

| Perspective | Framing | Primary Use Case | Default Profile |
| :--- | :--- | :--- | :--- |
| **SoftwareCenter** | **Software Catalog** | Organizing, categorizing, and launching installed software packages | `PROFILE_SOFTWARECENTER` |
| **LaunchBoards** | **Workspace Boards** | Organizing shortcuts into tabbed launch boards across active projects | `PROFILE_LAUNCHBOARDS` |

Both apps can run side by side on the same machine without colliding:
- Each profile uses its own independent `QSettings` namespace (`file-bricks/LaunchBoards` vs `file-bricks/SoftwareCenter`).
- Each profile uses an independent single-instance lock (`LaunchBoards.lock` vs `SoftwareCenter.lock`), allowing both to run at the same time.
- Both share 100% interoperability with the versioned profile format (`softwarecenter-profile-v1.json`).

---

## Architecture & Profile Isolation

The diagram below illustrates how LaunchBoards leverages the shared core engine while remaining completely isolated in runtime state, configuration, and process mutex locks:

```mermaid
flowchart TD
    User["Desktop User / Developer"] -->|"Selects Branding"| Choice{"Execution Profile"}
    Choice -->|"Run LaunchBoards"| LB_Entry["LaunchBoards.exe / launchboards.py"]
    Choice -->|"Run SoftwareCenter"| SC_Entry["SoftwareCenter.exe / SoftwareCenter.py"]

    LB_Entry -->|"Initializes Profile"| CoreEngine["SoftwareCenter.py Core Engine"]
    SC_Entry -->|"Initializes Profile"| CoreEngine

    CoreEngine -->|"Dedicated Registry"| LBSettings["QSettings ('file-bricks/LaunchBoards')"]
    CoreEngine -->|"Dedicated Registry"| SCSettings["QSettings ('file-bricks/SoftwareCenter')"]

    CoreEngine -->|"Dedicated Mutex"| LBLock["SingleInstanceLock ('LaunchBoards.lock')"]
    CoreEngine -->|"Dedicated Mutex"| SCLock["SingleInstanceLock ('SoftwareCenter.lock')"]

    LBSettings -->|"Workspace Framing"| LBUi["LaunchBoards UI ('Tabbed Workspace Boards')"]
    SCSettings -->|"Software Framing"| SCUi["SoftwareCenter UI ('Application Catalog')"]
```

---

## Workspace Launch Lifecycle

LaunchBoards provides a responsive, local-first workflow from startup to process invocation:

```mermaid
sequenceDiagram
    autonumber
    actor User as "Desktop User"
    participant App as "LaunchBoards (PySide6)"
    participant Store as "QSettings State"
    participant OS as "Operating System"

    User->>App: "Launch application"
    App->>Store: "Load workspace tabs and shortcuts"
    Store-->>App: "Active boards ('Development', 'Design', 'Tools')"
    App-->>User: "Render tabbed launch boards UI"

    User->>App: "Drag & drop shortcut item (.lnk / .exe)"
    App->>Store: "Persist shortcut item in active board"
    Store-->>App: "State updated"

    User->>App: "Click shortcut / Press hotkey"
    App->>OS: "Spawn target process via QDesktopServices"
    OS-->>User: "Application launched successfully"
```

---

## Core Features

- 📑 **Tabbed Launch Boards:** Create, rename, and rearrange custom workspace boards tailored to specific workflows (e.g. *Code*, *Audio*, *Comms*).
- 🖱️ **Drag & Drop Organization:** Simply drag Windows shortcut files (`.lnk`), executables (`.exe`), scripts, or documents directly into any board.
- ⚡ **Instant Filter Search:** Type to filter shortcuts immediately across all boards without navigating deep menu hierarchies.
- 🔒 **100% Local-First & Zero Telemetry:** No user account, no cloud servers, no telemetry, and zero network traffic.
- 📦 **Portable Profile Migration:** Export and import boards effortlessly using the standard JSON format (`softwarecenter-profile-v1.json`).
- 🔀 **True Side-by-Side Execution:** Run LaunchBoards alongside SoftwareCenter concurrently with dedicated settings and window states.

---

## Getting Started & How to Run

### Option 1: Standalone Windows Executable (Recommended)

Pre-built binaries for LaunchBoards are distributed as standalone, portable Windows executables alongside SoftwareCenter releases:

1. Visit the canonical release page: **[SoftwareCenter Releases](https://github.com/file-bricks/SoftwareCenter/releases)**.
2. Download `LaunchBoards.exe` (or `LaunchBoards-<version>-win64.exe`).
3. Run the executable directly. No installation or administrative privileges required.

### Option 2: Running from Source

Since LaunchBoards shares the canonical codebase, clone and run it via the dedicated runner:

```bash
# Clone the canonical repository
git clone https://github.com/file-bricks/SoftwareCenter.git
cd SoftwareCenter

# Install dependencies (PySide6)
pip install -r requirements.txt

# Launch with the LaunchBoards profile
python launchboards.py
```

### Option 3: Building Standalone Binary Locally

To produce your own portable `LaunchBoards.exe` via PyInstaller, execute the preconfigured build script in the canonical repo:

```cmd
build_exe_launchboards.bat
```

The resulting binary will be located in `dist/LaunchBoards/LaunchBoards.exe` or bundled into root as `LaunchBoards.exe`.

---

## System Invariants & Governance

LaunchBoards adheres to strict operational and architectural invariants:

| ID | Invariant | Description |
| :--- | :--- | :--- |
| `INV-LOCAL-01` | **Zero Network Egress** | No telemetry, phone-home checks, cloud synchronization, or external web requests. |
| `INV-LOCAL-02` | **Unprivileged Run** | Runs strictly in user space (`RunAsInvoker`). Never requests administrative (UAC) elevation. |
| `INV-LOCAL-03` | **Non-Destructive Ops** | Removing a shortcut only detaches the UI reference; target files and executables are never deleted. |
| `INV-LOCAL-04` | **Safe Link Resolution** | Safely extracts target metadata from `.lnk` files without executing shell evaluation scripts. |
| `INV-LOCAL-05` | **Profile Isolation** | QSettings key `file-bricks/LaunchBoards` is strictly isolated from `file-bricks/SoftwareCenter`. |
| `INV-LOCAL-06` | **Mutex Independence** | Single-instance lock `LaunchBoards.lock` permits simultaneous execution with SoftwareCenter. |
| `INV-LOCAL-07` | **Schema Parity** | 100% interoperability with versioned profile schema (`softwarecenter-profile-v1.json`). |
| `INV-LOCAL-08` | **Canonical Authority** | The canonical source of truth for code, tests, and CI is `file-bricks/SoftwareCenter`. |
| `INV-LOCAL-09` | **Bilingual Parity** | All end-user documentation maintains complete German/English alignment (`P-006`). |
| `INV-LOCAL-10` | **Security SLA** | Security disclosures receive a verified response within 48 hours and triage within 5 days. |

---

## Canonical Repository & Contributing

This repository (`file-bricks/LaunchBoards`) is maintained as an official branding pointer and entry point for discoverability.

**All active development, issue tracking, and contributions occur in the canonical repository:**

👉 **[github.com/file-bricks/SoftwareCenter](https://github.com/file-bricks/SoftwareCenter)**

- **Issues & Bug Reports:** Please open issues under SoftwareCenter and tag with `[LaunchBoards]`.
- **Pull Requests:** Submit PRs against `file-bricks/SoftwareCenter`.
- **Translations:** Maintained via `manage_translations.py` and `locales/` in the canonical repository.

---

## Ecosystem & Sister Projects

LaunchBoards is part of the **file-bricks** and **open-bricks** desktop tool ecosystem:

| Project | Focus Area | Canonical Repository |
| :--- | :--- | :--- |
| **SoftwareCenter** | Installed software catalog & desktop launcher | [file-bricks/SoftwareCenter](https://github.com/file-bricks/SoftwareCenter) |
| **LaunchBoards** | Tab-based workspace launch boards | [file-bricks/LaunchBoards](https://github.com/file-bricks/LaunchBoards) |
| **TextCrafter** | Local-first distraction-free text editor & Markdown suite | [file-bricks/TextCrafter](https://github.com/file-bricks/TextCrafter) |
| **TagFolder** | Tag-based file navigation and organization tool | [file-bricks/TagFolder](https://github.com/file-bricks/TagFolder) |
| **lock-master** | Deterministic multi-agent file and directory locking | [dev-bricks/lock-master](https://github.com/dev-bricks/lock-master) |
| **open-bricks** | Umbrella registry for open-source desktop applications | [open-bricks/.github](https://github.com/open-bricks) |

---

## Security & Vulnerability Reporting

Security and user privacy are foundational. LaunchBoards executes completely offline and requires no elevated privileges.

If you identify a security issue or vulnerability, please consult our [SECURITY.md](SECURITY.md) policy. We commit to an initial response within **48 hours** and triage within **5 business days**:

- 📧 Security Team: `security@open-bricks.org`
- 📧 Maintainer: `lukas@open-bricks.org`

---

## License

MIT License — see [LICENSE](LICENSE) for full details.

Copyright (c) 2026 Lukas Geiger.
