"""Tests for environment and system information management."""

from pathlib import Path

from application.utils.system_info.system_info_management import (
    ensure_env_file,
    get_project_root,
    load_environment,
)


def test_get_project_root_contains_pyproject():
    root = get_project_root()
    assert (root / "pyproject.toml").is_file()
    assert (root / "src" / "application").is_dir()


def test_ensure_env_file_creates_missing_file(tmp_path: Path):
    env_path = tmp_path / ".env"
    ensure_env_file(env_path)
    assert env_path.is_file()


def test_ensure_env_file_preserves_existing_content(tmp_path: Path):
    env_path = tmp_path / ".env"
    env_path.write_text("MY_VAR=keep_me\n")
    ensure_env_file(env_path)
    assert "MY_VAR=keep_me" in env_path.read_text()


def test_load_environment_populates_keys(tmp_path: Path):
    env_path = tmp_path / ".env"
    env_path.write_text("MY_VAR=keep_me\n")
    values = load_environment(env_path)
    assert values["MY_VAR"] == "keep_me"
    assert values["PROJECT_ROOT_DIRECTORY"] == str(get_project_root())
    assert values["SYSTEM_INFORMATION"]
    assert values["NODE_INFORMATION"]
