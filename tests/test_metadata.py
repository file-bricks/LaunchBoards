# -*- coding: utf-8 -*-
"""Contract tests for LaunchBoards metadata, discoverability, and documentation parity."""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_readme_files_exist_and_not_empty():
    readme_en = REPO_ROOT / "README.md"
    readme_de = REPO_ROOT / "README_de.md"
    assert readme_en.is_file(), "README.md must exist"
    assert readme_de.is_file(), "README_de.md must exist"
    assert readme_en.stat().st_size > 1500, "README.md should have full documentation"
    assert readme_de.stat().st_size > 1500, "README_de.md should have full documentation"


def test_readme_bilingual_parity():
    content_en = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    content_de = (REPO_ROOT / "README_de.md").read_text(encoding="utf-8")

    # Language switcher checks
    assert 'href="README.md"' in content_en
    assert 'href="README_de.md"' in content_en
    assert 'href="README.md"' in content_de
    assert 'href="README_de.md"' in content_de

    # Key invariant checks in both
    for i in range(1, 11):
        inv = f"INV-LOCAL-{i:02d}"
        assert inv in content_en, f"{inv} missing in README.md"
        assert inv in content_de, f"{inv} missing in README_de.md"

    # Canonical repo links in both
    assert "https://github.com/file-bricks/SoftwareCenter" in content_en
    assert "https://github.com/file-bricks/SoftwareCenter" in content_de


def test_mermaid_diagram_syntax():
    """Verify all Mermaid code blocks comply with GitHub parsing rules and HOOK-BANNER-ASSET-01."""
    illegal_chars = set("()[]{}<>")
    edge_label_re = re.compile(r"((?:--+>|<-+>|-\.-+>|==+>)\|)([^|\r\n]+)(\|)")

    for doc_name in ("README.md", "README_de.md"):
        content = (REPO_ROOT / doc_name).read_text(encoding="utf-8")
        blocks = re.findall(r"```mermaid\s*\n(.*?)\n```", content, re.DOTALL)
        assert len(blocks) == 2, f"{doc_name} should contain exactly 2 Mermaid diagrams"

        for block in blocks:
            for line in block.splitlines():
                stripped = line.strip()
                if not stripped or stripped.startswith("%%"):
                    continue
                # Check edge labels
                for match in edge_label_re.finditer(line):
                    _, label, _ = match.groups()
                    trimmed = label.strip()
                    if not (trimmed.startswith('"') and trimmed.endswith('"')):
                        for c in illegal_chars:
                            assert c not in trimmed, (
                                f"Unquoted '{c}' in edge label '{trimmed}' in {doc_name}: line '{line}'"
                            )


def test_banner_guardrails_compliance():
    """Verify exactly one banner reference exists and no duplicate banners were added."""
    for doc_name in ("README.md", "README_de.md"):
        content = (REPO_ROOT / doc_name).read_text(encoding="utf-8")
        banners = re.findall(r'<img\s+[^>]*banner[^>]*>', content, re.IGNORECASE)
        assert len(banners) == 1, f"Expected exactly 1 banner tag in {doc_name}, found {len(banners)}"


def test_llms_txt_integrity():
    llms_path = REPO_ROOT / "llms.txt"
    assert llms_path.is_file(), "llms.txt must exist"
    content = llms_path.read_text(encoding="utf-8")

    assert "https://github.com/file-bricks/SoftwareCenter" in content
    assert "https://github.com/file-bricks/LaunchBoards" in content
    assert "PROFILE_LAUNCHBOARDS" in content
    assert "Search Phrases" in content
    for i in range(1, 11):
        inv = f"INV-LOCAL-{i:02d}"
        assert inv in content, f"{inv} missing in llms.txt"


def test_security_policy_present_and_sla():
    sec_path = REPO_ROOT / "SECURITY.md"
    assert sec_path.is_file(), "SECURITY.md must exist"
    content = sec_path.read_text(encoding="utf-8")

    assert "48 hours" in content or "48 Stunden" in content
    assert "5 business days" in content or "5 Werktagen" in content
    assert "security@open-bricks.org" in content
    assert "security@file-bricks.org" in content


def test_gitignore_hygiene():
    gi_path = REPO_ROOT / ".gitignore"
    assert gi_path.is_file(), ".gitignore must exist"
    content = gi_path.read_text(encoding="utf-8")

    assert "__pycache__/" in content
    assert "*-conflict-*" in content
    assert "*.sync-conflict-*" in content
    assert "LOCK" in content
    assert "LOCK*" in content
    assert "*.lock" in content


def test_changelog_integrity():
    cl_path = REPO_ROOT / "CHANGELOG.md"
    assert cl_path.is_file(), "CHANGELOG.md must exist"
    content = cl_path.read_text(encoding="utf-8")

    assert "[1.1.0] - 2026-09-10" in content
    assert "Visual Architecture & Lifecycle" in content
