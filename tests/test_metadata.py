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
    assert readme_en.stat().st_size > 2500, "README.md should have full documentation"
    assert readme_de.stat().st_size > 2500, "README_de.md should have full documentation"


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
    assert "2026-09-14" in content
    assert "1.2.0" in content
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

    assert "[1.2.0] - 2026-09-14" in content
    assert "[1.1.0] - 2026-09-10" in content
    assert "Target Personas & SEO Discovery" in content


def test_target_personas_present_in_both_readmes():
    content_en = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    content_de = (REPO_ROOT / "README_de.md").read_text(encoding="utf-8")

    for persona_id in ("PERSONA-01", "PERSONA-02", "PERSONA-03", "PERSONA-04"):
        assert f"[{persona_id}]" in content_en, f"{persona_id} missing in README.md"
        assert f"[{persona_id}]" in content_de, f"{persona_id} missing in README_de.md"


def test_comparative_matrix_present_and_mapped():
    content_en = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    content_de = (REPO_ROOT / "README_de.md").read_text(encoding="utf-8")

    for doc, name in ((content_en, "README.md"), (content_de, "README_de.md")):
        assert "Windows Start" in doc, f"Windows Start missing in matrix of {name}"
        assert "PowerToys Run" in doc, f"PowerToys Run missing in matrix of {name}"
        assert "Stardock Fences" in doc, f"Stardock Fences missing in matrix of {name}"
        for i in range(1, 11):
            inv = f"INV-LOCAL-{i:02d}"
            assert inv in doc, f"{inv} missing from comparative matrix or invariants in {name}"


def test_third_party_licenses_audit_and_spdx():
    tpl_path = REPO_ROOT / "THIRD_PARTY_LICENSES.md"
    assert tpl_path.is_file(), "THIRD_PARTY_LICENSES.md must exist"
    content = tpl_path.read_text(encoding="utf-8")

    assert "PSF-2.0" in content
    assert "LGPL-3.0" in content
    assert "MIT" in content
    assert "Zero-Copyleft" in content
    assert "RunAsInvoker" in content
    for i in range(1, 11):
        inv = f"INV-LOCAL-{i:02d}"
        assert inv in content, f"{inv} missing in THIRD_PARTY_LICENSES.md"


def test_quick_navigation_parity_and_anchors():
    content_en = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    content_de = (REPO_ROOT / "README_de.md").read_text(encoding="utf-8")

    en_links = re.findall(r"\[([^\]]+)\]\(#([^\)]+)\)", content_en.split("---")[2])
    de_links = re.findall(r"\[([^\]]+)\]\(#([^\)]+)\)", content_de.split("---")[2])

    assert len(en_links) == 14, f"Expected 14 quick navigation links in README.md, found {len(en_links)}"
    assert len(de_links) == 14, f"Expected 14 quick navigation links in README_de.md, found {len(de_links)}"

    # Ensure all anchors exist in their respective document
    for _, anchor in en_links:
        pattern = re.compile(rf"^#+\s+.*", re.MULTILINE)
        headers = [h.lower() for h in pattern.findall(content_en)]
        # Normalize anchor test
        found = any(anchor.replace("-", "") in h.replace(" ", "").replace("-", "").replace("?", "").replace("&", "").replace(".", "").replace(":", "") for h in headers)
        assert found, f"Anchor #{anchor} target heading not found in README.md"

    for _, anchor in de_links:
        pattern = re.compile(rf"^#+\s+.*", re.MULTILINE)
        headers = [h.lower() for h in pattern.findall(content_de)]
        found = any(anchor.replace("-", "") in h.replace(" ", "").replace("-", "").replace("?", "").replace("&", "").replace(".", "").replace(":", "") for h in headers)
        assert found, f"Anchor #{anchor} target heading not found in README_de.md"


def test_pyproject_pep621_urls_and_version():
    pyproject_path = REPO_ROOT / "pyproject.toml"
    assert pyproject_path.is_file(), "pyproject.toml must exist"
    content = pyproject_path.read_text(encoding="utf-8")

    assert 'version = "1.2.0"' in content
    assert '"Marketing Log"' in content
    assert '"Third-Party Licenses"' in content
    assert "addopts = \"-ra -v --strict-markers\"" in content


def test_marketing_log_recency():
    ml_path = REPO_ROOT / "MARKETING-LOG.txt"
    assert ml_path.is_file(), "MARKETING-LOG.txt must exist"
    content = ml_path.read_text(encoding="utf-8")

    assert "2026-09-14" in content
    assert "1.2.0" in content
    assert "Pfad B Discoverability, Personas & SEO Audit" in content


def test_unprivileged_run_as_invoker_affirmed():
    for filename in ("README.md", "README_de.md", "THIRD_PARTY_LICENSES.md"):
        content = (REPO_ROOT / filename).read_text(encoding="utf-8")
        assert "RunAsInvoker" in content, f"RunAsInvoker affirmation missing in {filename}"


def test_pyside6_lgpl_dynamic_linking_affirmed():
    tpl_content = (REPO_ROOT / "THIRD_PARTY_LICENSES.md").read_text(encoding="utf-8")
    assert "LGPL-3.0" in tpl_content
    assert "Dynamic Linking" in tpl_content
    assert "§ 4 LGPLv3" in tpl_content
