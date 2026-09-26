"""Tests for the global application context."""

from pathlib import Path

import pytest

from application.context import ApplicationContext, get_context, init_context, reset_context
from application.utils.system_info.system_info_management import get_project_root


@pytest.fixture(autouse=True)
def _clean_context():
    reset_context()
    yield
    reset_context()


def test_init_context_returns_immutable_context():
    context = init_context()
    assert isinstance(context, ApplicationContext)
    assert context.project_root == get_project_root()
    assert context.system
    assert context.node
    assert context.log_file == get_project_root() / "Logs" / "application.log"


def test_context_is_frozen():
    context = init_context()
    with pytest.raises(AttributeError):
        context.system = "modified"


def test_init_context_is_idempotent():
    first = init_context()
    second = init_context()
    assert first is second


def test_get_context_initializes_on_first_access():
    context = get_context()
    assert context.project_root == get_project_root()


def test_context_log_file_accepts_override(tmp_path: Path):
    custom = ApplicationContext(
        project_root=tmp_path,
        system="Linux",
        node="test-node",
        log_file=tmp_path / "custom.log",
    )
    assert custom.log_file.name == "custom.log"
