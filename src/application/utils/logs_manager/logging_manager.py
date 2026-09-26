"""Logging configuration driven by YAML files."""

import logging.config
from pathlib import Path

import yaml

DEFAULT_CONFIG_DIR = Path(__file__).resolve().parent / "logging_conf_files"


def load_config_file(config_dir: Path, filename: str) -> dict:
    """Read a YAML configuration file and return its content as a dict."""
    file_path = config_dir / filename
    if not file_path.is_file():
        raise FileNotFoundError(f"Configuration file {filename} not found in {config_dir}")
    with file_path.open("r", encoding="utf-8") as file:
        content = yaml.safe_load(file)
    if not isinstance(content, dict):
        raise ValueError(f"Configuration file {filename} must contain a mapping")
    return content


def setup_logging(
    config_dir: Path | None = None,
    log_file: Path | None = None,
    project_root: Path | None = None,
) -> None:
    """Configure application logging from YAML files.

    Args:
        config_dir: Directory containing formatters/handlers/loggers YAML files.
        log_file: Target log file path; defaults to <project_root>/Logs/application.log.
        project_root: Project root used to resolve the default log file location.
    """
    conf_dir = config_dir if config_dir is not None else DEFAULT_CONFIG_DIR

    if log_file is None:
        root = project_root if project_root is not None else Path.cwd()
        log_file = root / "Logs" / "application.log"

    log_file.parent.mkdir(parents=True, exist_ok=True)

    config_dict = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": load_config_file(conf_dir, "formatters.yaml"),
        "handlers": load_config_file(conf_dir, "handlers.yaml"),
        "loggers": load_config_file(conf_dir, "loggers.yaml"),
    }
    config_dict["handlers"]["file"]["filename"] = str(log_file)
    logging.config.dictConfig(config_dict)
