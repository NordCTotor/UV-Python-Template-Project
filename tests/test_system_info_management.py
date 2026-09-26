"""Tests for system information management."""

from application.utils.system_info.system_info_management import get_project_root


def test_get_project_root_contains_pyproject():
    root = get_project_root()
    assert (root / "pyproject.toml").is_file()
    assert (root / "src" / "application").is_dir()
