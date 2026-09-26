"""Environment and system information management."""

from pathlib import Path


def get_project_root() -> Path:
    """Return the project root directory (where pyproject.toml lives)."""
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "pyproject.toml").is_file():
            return parent
    raise FileNotFoundError("Project root not found: no pyproject.toml in parents.")
