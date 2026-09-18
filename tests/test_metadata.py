"""Contract tests for LaunchBoards metadata, discoverability, and documentation parity."""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def _clean_anchor(s: str) -> str:
    return re.sub(r"[\s\-?&.:]", "", s)



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
                            msg = (
                                f"Unquoted '{c}' in edge label '{trimmed}' in {doc_name}: "
                                f"line '{line}'"
                            )
                            assert c not in trimmed, msg


def test_banner_guardrails_compliance():
    """Verify exactly one banner reference exists and no duplicate banners were added."""
    for doc_name in ("README.md", "README_de.md"):
        content = (REPO_ROOT / doc_name).read_text(encoding="utf-8")
        banners = re.findall(r'<img\s+[^>]*banner[^>]*>', content, re.IGNORECASE)
        assert len(banners) == 1, (
            f"Expected exactly 1 banner tag in {doc_name}, found {len(banners)}"
        )


def test_llms_txt_integrity():
    llms_path = REPO_ROOT / "llms.txt"
    assert llms_path.is_file(), "llms.txt must exist"
    content = llms_path.read_text(encoding="utf-8")

    assert "https://github.com/file-bricks/SoftwareCenter" in content
    assert "https://github.com/file-bricks/LaunchBoards" in content
    assert "PROFILE_LAUNCHBOARDS" in content
    assert "Search Phrases" in content
    assert ("2026-09-14" in content or "2026-09-18" in content)
    assert ("1.2.0" in content or "1.2.1" in content)
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

    assert len(en_links) == 14, (
        f"Expected 14 quick navigation links in README.md, found {len(en_links)}"
    )
    assert len(de_links) == 14, (
        f"Expected 14 quick navigation links in README_de.md, found {len(de_links)}"
    )

    # Ensure all anchors exist in their respective document
    pattern = re.compile(r"^#+\s+.*", re.MULTILINE)
    headers_en = [_clean_anchor(h.lower()) for h in pattern.findall(content_en)]
    headers_de = [_clean_anchor(h.lower()) for h in pattern.findall(content_de)]

    for _, anchor in en_links:
        clean_a = _clean_anchor(anchor)
        assert any(clean_a in h for h in headers_en), (
            f"Anchor #{anchor} target heading not found in README.md"
        )

    for _, anchor in de_links:
        clean_a = _clean_anchor(anchor)
        assert any(clean_a in h for h in headers_de), (
            f"Anchor #{anchor} target heading not found in README_de.md"
        )


def test_pyproject_pep621_urls_and_version():
    pyproject_path = REPO_ROOT / "pyproject.toml"
    assert pyproject_path.is_file(), "pyproject.toml must exist"
    content = pyproject_path.read_text(encoding="utf-8")

    assert ('version = "1.2.0"' in content or 'version = "1.2.1"' in content)
    assert '"Marketing Log"' in content
    assert '"Third-Party Licenses"' in content
    assert "addopts = \"-ra -v --strict-markers\"" in content


def test_marketing_log_recency():
    ml_path = REPO_ROOT / "MARKETING-LOG.txt"
    assert ml_path.is_file(), "MARKETING-LOG.txt must exist"
    content = ml_path.read_text(encoding="utf-8")

    assert ("2026-09-14" in content or "2026-09-18" in content)
    assert ("1.2.0" in content or "1.2.1" in content)
    assert "Pfad A Repository Hygiene, CI Matrix & Contract Expansion" in content


def test_unprivileged_run_as_invoker_affirmed():
    for filename in ("README.md", "README_de.md", "THIRD_PARTY_LICENSES.md"):
        content = (REPO_ROOT / filename).read_text(encoding="utf-8")
        assert "RunAsInvoker" in content, f"RunAsInvoker affirmation missing in {filename}"


def test_pyside6_lgpl_dynamic_linking_affirmed():
    tpl_content = (REPO_ROOT / "THIRD_PARTY_LICENSES.md").read_text(encoding="utf-8")
    assert "LGPL-3.0" in tpl_content
    assert "Dynamic Linking" in tpl_content
    assert "§ 4 LGPLv3" in tpl_content


def test_github_actions_ci_workflows_present_and_hardened():
    wf_dir = REPO_ROOT / ".github" / "workflows"
    assert wf_dir.is_dir(), ".github/workflows directory must exist"

    ci_file = wf_dir / "ci.yml"
    assert ci_file.is_file(), "ci.yml must exist"
    ci_content = ci_file.read_text(encoding="utf-8")
    assert "timeout-minutes: 15" in ci_content
    assert "contents: read" in ci_content
    assert "cancel-in-progress: true" in ci_content
    assert "ubuntu-latest" in ci_content
    assert "windows-latest" in ci_content
    for py_ver in ("3.10", "3.11", "3.12", "3.13"):
        assert py_ver in ci_content, f"Python {py_ver} missing from CI matrix"

    stale_file = wf_dir / "stale.yml"
    assert stale_file.is_file(), "stale.yml must exist"
    stale_content = stale_file.read_text(encoding="utf-8")
    assert "actions/stale@v9" in stale_content
    assert "timeout-minutes: 10" in stale_content
    assert "issues: write" in stale_content

    welcome_file = wf_dir / "welcome.yml"
    assert welcome_file.is_file(), "welcome.yml must exist"
    welcome_content = welcome_file.read_text(encoding="utf-8")
    assert "actions/first-interaction@v3" in welcome_content
    assert "timeout-minutes: 5" in welcome_content


def test_gitignore_multi_host_and_agent_locks():
    gi_path = REPO_ROOT / ".gitignore"
    assert gi_path.is_file(), ".gitignore must exist"
    content = gi_path.read_text(encoding="utf-8")

    # Multi-host sync patterns
    assert "*conflicted copy*" in content
    assert "*-ASUS*" in content
    assert "*-WORKSTATION*" in content
    assert "*-Mac Studio*" in content

    # Agent coordination locks
    assert "LOCK.permissions.json" in content
    assert "LOCK.user.*" in content
    assert "LOCK.until.*" in content
    assert "LOCK.condition.*" in content
    assert "uv.lock" in content
    assert "!package-lock.json" in content


def test_pep621_pyproject_metadata_and_tools():
    pyproject_path = REPO_ROOT / "pyproject.toml"
    assert pyproject_path.is_file(), "pyproject.toml must exist"
    content = pyproject_path.read_text(encoding="utf-8")

    assert "[build-system]" in content
    assert 'build-backend = "setuptools.build_meta"' in content
    assert 'requires-python = ">=3.10"' in content
    assert "license-files =" in content
    assert "keywords =" in content
    assert "classifiers =" in content
    assert "Programming Language :: Python :: 3.13" in content

    # Standard URLs
    assert "Documentation =" in content
    assert "Security =" in content
    assert '"Parent Organization" =' in content
    assert '"Umbrella Ecosystem" =' in content
    assert '"LLM Ready" =' in content

    # Tooling config
    assert "[tool.ruff]" in content
    assert 'target-version = "py310"' in content
    assert "norecursedirs =" in content


def test_statutory_bgb_521_notice_present():
    content_de = (REPO_ROOT / "README_de.md").read_text(encoding="utf-8")
    content_en = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

    assert "§ 521 BGB" in content_de, "§ 521 BGB notice missing in README_de.md"
    assert "unentgeltliche" in content_de or "Gefälligkeitsrecht" in content_de
    assert "§ 521 BGB" in content_en, "§ 521 BGB notice missing in README.md"
    assert "gratuitous" in content_en or "liability" in content_en


def test_version_synchrony_across_all_manifests():
    version = "1.2.1"
    pyproject = (REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8")
    changelog = (REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    llms = (REPO_ROOT / "llms.txt").read_text(encoding="utf-8")
    tpl = (REPO_ROOT / "THIRD_PARTY_LICENSES.md").read_text(encoding="utf-8")
    marketing = (REPO_ROOT / "MARKETING-LOG.txt").read_text(encoding="utf-8")

    assert f'version = "{version}"' in pyproject, "pyproject.toml version mismatch"
    assert f"[{version}] - 2026-09-18" in changelog, "CHANGELOG.md version mismatch"
    assert f"## Version: {version}" in llms, "llms.txt version mismatch"
    assert f"**Version:** {version}" in tpl, "THIRD_PARTY_LICENSES.md version mismatch"
    assert f"**Version:** {version}" in marketing, "MARKETING-LOG.txt version mismatch"

