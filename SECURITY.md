# Security Policy / Sicherheitsrichtlinie

[English](#english) | [Deutsch](#deutsch)

---

<a name="english"></a>
## English

### Supported Versions

We provide security updates and patches for the following versions and product profiles:

| Product Profile / Version | Supported | Status |
| :--- | :---: | :--- |
| `LaunchBoards` (via SoftwareCenter `1.2.x`) | :white_check_mark: | Active Security Support |
| `LaunchBoards` (via SoftwareCenter `1.1.x`) | :white_check_mark: | Maintenance / Critical Fixes Only |
| `< 1.1.0` | :x: | End of Life (Upgrade Recommended) |

### Reporting a Vulnerability

If you discover a potential security vulnerability in LaunchBoards or its underlying engine, please do NOT open a public issue. We follow coordinated vulnerability disclosure:

1. **GitHub Private Vulnerability Reporting (Preferred):**
   Navigate to **Security > Advisories > Report a vulnerability** in the canonical repository [file-bricks/SoftwareCenter](https://github.com/file-bricks/SoftwareCenter) to open a confidential report.
2. **Direct Contact:**
   Send an email to:
   - `security@open-bricks.org`
   - `security@file-bricks.org`
   - `lukas@open-bricks.org`

Include as much information as possible:
- Steps to reproduce the issue
- Proof of Concept (PoC) or sample data
- Potential impact and affected components (specifying the LaunchBoards profile)
- Application version and operating system environment

### Response SLA

- **Initial Response & Confirmation:** Within **48 hours**.
- **Triage & Severity Assessment:** Within **5 business days**.
- **Remediation & Patch Release:** Coordinated patch published via GitHub release and private advisory disclosure.

### Core Security Invariants

LaunchBoards is designed with a defense-in-depth, local-first architecture:

1. **100% Local-First & Zero Network Egress (`INV-LOCAL-01`):**
   The application operates strictly locally on your machine. It makes zero telemetry calls, contains no trackers, and communicates with no external cloud servers.
2. **Unprivileged Execution (`INV-LOCAL-02`):**
   LaunchBoards runs entirely within standard user space (`RunAsInvoker`). It never requests or requires administrative (UAC) elevation.
3. **Non-Destructive Shortcut Operations (`INV-LOCAL-03`):**
   Removing or re-ordering items inside the UI only alters shortcut metadata in local settings; it never deletes, moves, or alters target application files.
4. **Safe Shell & Path Resolution (`INV-LOCAL-04`):**
   Resolution of `.lnk` shortcuts and executable targets is strictly restricted to filesystem target paths without executing arbitrary script content.
5. **Profile Isolation & Mutual Independence (`INV-LOCAL-05` / `INV-LOCAL-06`):**
   `QSettings` keys and process mutex locks are strictly isolated between LaunchBoards and SoftwareCenter, preventing cross-profile corruption or locking conflicts.

---

<a name="deutsch"></a>
## Deutsch

### Unterstützte Versionen

Sicherheitsupdates und Patches werden für folgende Versionen und Produktprofile bereitgestellt:

| Produktprofil / Version | Unterstützt | Status |
| :--- | :---: | :--- |
| `LaunchBoards` (via SoftwareCenter `1.2.x`) | :white_check_mark: | Aktiver Sicherheits-Support |
| `LaunchBoards` (via SoftwareCenter `1.1.x`) | :white_check_mark: | Wartungsmodus / Nur kritische Fixes |
| `< 1.1.0` | :x: | End of Life (Upgrade empfohlen) |

### Meldung einer Sicherheitslücke

Wenn du eine potenzielle Sicherheitslücke in LaunchBoards oder der zugrundeliegenden Engine entdeckst, eröffne bitte KEIN öffentliches Issue. Wir praktizieren koordinierte Offenlegung:

1. **GitHub Private Vulnerability Reporting (Bevorzugt):**
   Öffne im kanonischen Repository [file-bricks/SoftwareCenter](https://github.com/file-bricks/SoftwareCenter) unter **Security > Advisories > Report a vulnerability** einen vertraulichen Bericht.
2. **Direkter Kontakt:**
   Sende eine E-Mail an:
   - `security@open-bricks.org`
   - `security@file-bricks.org`
   - `lukas@open-bricks.org`

Bitte folgende Angaben beifügen:
- Schritte zur Reproduktion des Problems
- Proof of Concept (PoC) oder Testdaten
- Potenzielle Auswirkungen und betroffene Komponenten (mit Hinweis auf das LaunchBoards-Profil)
- Anwendungsversion und Betriebssystemumgebung

### Antwort-SLA

- **Erstantwort & Bestätigung:** Innerhalb von **48 Stunden**.
- **Triage & Schweregrad-Einstufung:** Innerhalb von **5 Werktagen**.
- **Behebung & Patch-Veröffentlichung:** Koordinierter Release über das Haupt-Repository.

### Zentrale Sicherheitsinvarianten

LaunchBoards basiert auf einer robusten Local-First-Sicherheitsarchitektur:

1. **100% Lokal & Null Netzwerkverkehr (`INV-LOCAL-01`):**
   Die Anwendung arbeitet ausnahmslos lokal. Keine Telemetriedaten, kein Tracking, keine Verbindung zu externen Servern.
2. **Rechtefreier Betrieb (`INV-LOCAL-02`):**
   LaunchBoards läuft vollständig im regulären Benutzerkontext (`RunAsInvoker`). Es werden zu keinem Zeitpunkt Administratorrechte (UAC) angefordert.
3. **Zerstörungsfreie Verknüpfungsverwaltung (`INV-LOCAL-03`):**
   Das Entfernen oder Verschieben von Einträgen betrifft ausschließlich Metadaten in den Einstellungen; Zieldateien oder installierte Programme werden niemals modifiziert oder gelöscht.
4. **Sichere Link-Auflösung (`INV-LOCAL-04`):**
   Die Auflösung von `.lnk`-Dateien und Programmpfaden erfolgt sicher über Pfadabfragen ohne Ausführung beliebiger Shell-Skripte.
5. **Profil-Isolation & Mutex-Unabhängigkeit (`INV-LOCAL-05` / `INV-LOCAL-06`):**
   Einstellungen (`QSettings`) und Prozess-Locks sind vollständig isoliert, sodass LaunchBoards und SoftwareCenter konfliktfrei nebeneinander betrieben werden können.
