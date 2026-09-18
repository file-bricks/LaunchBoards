# Third-Party Licenses & Runtime Invariants

**Repository:** `file-bricks/LaunchBoards`  
**Stand:** 2026-09-18  
**Version:** 1.2.1  
**SPDX-License-Identifier:** MIT  
**Canonical Codebase:** `file-bricks/SoftwareCenter`  
**Branding Profile:** `PROFILE_LAUNCHBOARDS`  
**Umbrella Ecosystem:** `open-bricks` / `file-bricks`  

---

## 1. Overview & Compliance Architecture

`LaunchBoards` is an open-source, local-first Windows desktop workspace launcher and shortcut management application. It is released under the permissive **MIT License**.

LaunchBoards shares the canonical engine of **[SoftwareCenter](https://github.com/file-bricks/SoftwareCenter)** while executing under an isolated branding identity, dedicated single-instance mutex lock, and independent configuration store (`PROFILE_LAUNCHBOARDS`). All runtime libraries, transitive packages, and development toolchains have been cataloged and audited for license compliance, unprivileged local execution, and zero-copyleft guarantees.

---

## 2. Dependency Inventory & SPDX Audit

### 2.1 Core Runtime Dependencies

| Package / Component | Declared Constraint | License (SPDX) | Type / Purpose | Copyleft Compliance |
|---|---|---|---|---|
| **Python Standard Library** | $\ge$ 3.10 | `PSF-2.0` | Core runtime (json, sys, os, pathlib, subprocess) | Permissive (No copyleft) |
| **PySide6** | $\ge$ 6.5.0 | `LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only` | Official Qt 6 Python desktop UI bindings | **Weak Copyleft / Dynamically Linked**: Dynamic linking under LGPL-3.0 complies with § 4 LGPLv3 without viral license contagion. |
| **shiboken6** | $\ge$ 6.5.0 | `LGPL-3.0-only` | CPython binding generator runtime for Qt 6 | Weak Copyleft (Dynamic link) |

### 2.2 Development, Testing & Quality Assurance

| Package / Component | Version | License (SPDX) | Type / Purpose | Copyleft? |
|---|---|---|---|---|
| **pytest** | $\ge$ 8.0.0 | `MIT` | Automated test suite and metadata contract verification | No |
| **ruff** | $\ge$ 0.4.0 | `MIT OR Apache-2.0` | Static analysis, code formatting, and linting | No |

---

## 3. PySide6 & LGPL-3.0 Dynamic Linking Compliance (§ 4 LGPLv3)

LaunchBoards links to PySide6 and Qt 6 libraries dynamically via standard Python import mechanisms:

1. **No Static Linkage:** PySide6 and the underlying Qt shared libraries (`.dll` on Windows) are never statically compiled into the application logic.
2. **User Replaceability:** End users and system administrators may upgrade, patch, or replace the PySide6 package or Qt runtime binaries independently without modifying LaunchBoards source code.
3. **No Proprietary Lock-In:** Source code of LaunchBoards is 100% open under the MIT License and hosted publicly on GitHub.
4. **License Texts Provided:** The full text of the GNU Lesser General Public License version 3 (LGPL-3.0) and MIT License are referenced and available.

---

## 4. Zero-Copyleft Affirmation & User Data Protection

1. **Permissive Application Licensing:** LaunchBoards is licensed under the MIT License.
2. **Zero Copyleft on User Assets:** User workspace shortcuts (`.lnk`), launched executable targets (`.exe`), scripts, custom board titles, and exported configuration profiles (`softwarecenter-profile-v1.json`) remain the exclusive property of the user and are never tainted by copyleft obligations.
3. **Commercial and Enterprise Friendly:** Permitted for unhindered use in academic, personal, commercial, and enterprise homelab environments.

---

## 5. System Invariants & Governance Compliance

LaunchBoards strictly complies with 10 operational and architectural invariants:

| Invariant ID | Title | Description | Compliance Status |
|---|---|---|---|
| `INV-LOCAL-01` | **Zero Network Egress** | No telemetry, phone-home checks, cloud synchronization, or external web requests. 100% offline. | **VERIFIED** |
| `INV-LOCAL-02` | **Unprivileged Run** | Runs strictly in user space (`RunAsInvoker`). Never requests UAC or administrative elevation. | **VERIFIED** |
| `INV-LOCAL-03` | **Non-Destructive Ops** | Removing shortcuts only removes UI references; target executables and files are never deleted. | **VERIFIED** |
| `INV-LOCAL-04` | **Safe Link Resolution** | Safely extracts target metadata from `.lnk` files without executing shell evaluation scripts. | **VERIFIED** |
| `INV-LOCAL-05` | **Profile Isolation** | QSettings key `file-bricks/LaunchBoards` is strictly isolated from `file-bricks/SoftwareCenter`. | **VERIFIED** |
| `INV-LOCAL-06` | **Mutex Independence** | Single-instance lock `LaunchBoards.lock` permits simultaneous execution with SoftwareCenter. | **VERIFIED** |
| `INV-LOCAL-07` | **Schema Parity** | 100% interoperability with versioned profile schema (`softwarecenter-profile-v1.json`). | **VERIFIED** |
| `INV-LOCAL-08` | **Canonical Authority** | The canonical source of truth for code, tests, and CI is `file-bricks/SoftwareCenter`. | **VERIFIED** |
| `INV-LOCAL-09` | **Bilingual Parity** | All end-user documentation maintains complete German/English alignment (`P-006`). | **VERIFIED** |
| `INV-LOCAL-10` | **Security SLA** | Security disclosures receive a verified response within 48 hours and triage within 5 days. | **VERIFIED** |

---

## 6. Execution Privileges (RunAsInvoker)

LaunchBoards requires **no administrative, root, or elevated privileges**. It operates exclusively in user space (`RunAsInvoker`), reading user-specified shortcut locations and storing workspace configurations in the user's standard application data registry (`QSettings`).
