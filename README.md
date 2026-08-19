<img src="https://raw.githubusercontent.com/file-bricks/SoftwareCenter/master/assets/banner.png" width="100%" alt="LaunchBoards Banner">

# LaunchBoards

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Sister product](https://img.shields.io/badge/Sister%20product-SoftwareCenter-blue.svg)](https://github.com/file-bricks/SoftwareCenter)
[![Ecosystem: file-bricks](https://img.shields.io/badge/Ecosystem-file--bricks-blue.svg)](https://github.com/file-bricks)

Organize your app shortcuts into launch boards and start what you need, when you need it.

[Deutsche Dokumentation](README_de.md)

## What is LaunchBoards?

**LaunchBoards is a second branding of [SoftwareCenter](https://github.com/file-bricks/SoftwareCenter)** — the
same desktop app, the same codebase, running under a different name, icon, and settings profile. It is not a
fork and not a separate product line: it is the identical, actively maintained SoftwareCenter code, started with
a `LaunchBoards` product profile instead of the default `SoftwareCenter` profile.

Both apps can run side by side on the same machine with fully separate settings, because each profile gets its
own `QSettings` namespace and single-instance lock. Nothing in the underlying code differs between them.

## Why two names for one app?

SoftwareCenter and LaunchBoards emphasize two framings of the same tool:

- **SoftwareCenter** — organizing and launching your *installed software*.
- **LaunchBoards** — organizing your shortcuts into *launch boards* (tab-based workspaces) you switch between.

The app already speaks in terms of "boards" internally regardless of branding; LaunchBoards simply leads with
that framing.

## Where the actual code lives

This repository is intentionally a pointer, not a duplicate. All source code, tests, issues, and
documentation live in the canonical repository:

**→ [github.com/file-bricks/SoftwareCenter](https://github.com/file-bricks/SoftwareCenter)**

Please file issues, feature requests, and pull requests there — including for anything specific to the
LaunchBoards branding or profile (`PROFILE_LAUNCHBOARDS` in `SoftwareCenter.py`).

## License

MIT License — see [LICENSE](LICENSE). Same license as SoftwareCenter, since it is the same code.

Copyright (c) 2026 Lukas Geiger
