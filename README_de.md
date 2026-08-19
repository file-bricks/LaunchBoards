<img src="https://raw.githubusercontent.com/file-bricks/SoftwareCenter/master/assets/banner.png" width="100%" alt="LaunchBoards Banner">

# LaunchBoards

[![Lizenz: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Schwesterprodukt](https://img.shields.io/badge/Schwesterprodukt-SoftwareCenter-blue.svg)](https://github.com/file-bricks/SoftwareCenter)
[![Ecosystem: file-bricks](https://img.shields.io/badge/Ecosystem-file--bricks-blue.svg)](https://github.com/file-bricks)

Organisiere deine App-Verknüpfungen in Launch Boards und starte, was du brauchst, wann du es brauchst.

[English Documentation](README.md)

## Was ist LaunchBoards?

**LaunchBoards ist ein Zweitbranding von [SoftwareCenter](https://github.com/file-bricks/SoftwareCenter)** —
dieselbe Desktop-App, dieselbe Codebasis, unter anderem Namen, Icon und Einstellungsprofil gestartet. Es ist
kein Fork und keine eigene Produktlinie: Es ist exakt der aktiv gepflegte SoftwareCenter-Code, gestartet mit
dem Produktprofil `LaunchBoards` statt dem Standardprofil `SoftwareCenter`.

Beide Apps können parallel auf demselben Rechner laufen, mit vollständig getrennten Einstellungen — jedes
Profil hat einen eigenen `QSettings`-Namespace und eine eigene Single-Instance-Sperre. Am zugrundeliegenden
Code unterscheidet sich nichts.

## Warum zwei Namen für eine App?

SoftwareCenter und LaunchBoards betonen zwei Blickwinkel auf dasselbe Werkzeug:

- **SoftwareCenter** — Organisieren und Starten deiner *installierten Software*.
- **LaunchBoards** — Organisieren deiner Verknüpfungen in *Launch Boards* (tabbasierte Arbeitsbereiche),
  zwischen denen du wechselst.

Die App spricht intern unabhängig vom Branding bereits von "Boards" — LaunchBoards stellt diesen Blickwinkel
nur in den Vordergrund.

## Wo der eigentliche Code liegt

Dieses Repository ist bewusst ein Verweis, kein Duplikat. Sämtlicher Quellcode, Tests, Issues und
Dokumentation liegen im kanonischen Repository:

**→ [github.com/file-bricks/SoftwareCenter](https://github.com/file-bricks/SoftwareCenter)**

Bitte Issues, Feature-Wünsche und Pull Requests dort einreichen — auch für alles, was speziell das
LaunchBoards-Branding oder -Profil betrifft (`PROFILE_LAUNCHBOARDS` in `SoftwareCenter.py`).

## Lizenz

MIT-Lizenz — siehe [LICENSE](LICENSE). Dieselbe Lizenz wie SoftwareCenter, da es derselbe Code ist.

Copyright (c) 2026 Lukas Geiger
