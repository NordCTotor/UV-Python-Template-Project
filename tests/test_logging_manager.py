"""Tests for the logging manager."""

import logging
from pathlib import Path

import pytest

from application.utils.logs_manager.logging_manager import (
    DEFAULT_CONFIG_DIR,
    load_config_file,
    setup_logging,
)


def test_load_config_file_returns_dict():
    content = load_config_file(DEFAULT_CONFIG_DIR, "formatters.yaml")
    assert isinstance(content, dict)
    assert "simple" in content


def test_load_config_file_missing_file():
    with pytest.raises(FileNotFoundError):
        load_config_file(DEFAULT_CONFIG_DIR, "does_not_exist.yaml")


def test_setup_logging_configures_main_logger(tmp_path: Path):
    log_file = tmp_path / "Logs" / "application.log"
    setup_logging(log_file=log_file)
    logger = logging.getLogger("main")
    logger.info("test message")
    for handler in logging.getLogger("main").handlers:
        handler.flush()
    assert log_file.is_file()
    assert "test message" in log_file.read_text()


def test_setup_logging_does_not_disable_existing_loggers(tmp_path: Path):
    existing = logging.getLogger("some.custom.logger")
    existing.setLevel(logging.DEBUG)
    setup_logging(log_file=tmp_path / "Logs" / "application.log")
    assert not logging.getLogger("some.custom.logger").disabled
