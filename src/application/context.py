"""Global application context."""

import platform
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

from application.utils.system_info.system_info_management import get_project_root


@dataclass(frozen=True)
class ApplicationContext:
    """Immutable application-wide context."""

    project_root: Path
    system: str
    node: str
    log_file: Path


_context: ApplicationContext | None = None


def init_context() -> ApplicationContext:
    """Build and set the global application context.

    Loads the .env file (read-only, if present) and captures system
    information at runtime. Idempotent: returns the existing context
    if already initialized.
    """
    global _context
    if _context is not None:
        return _context

    root = get_project_root()
    load_dotenv(root / ".env")
    info = platform.uname()
    _context = ApplicationContext(
        project_root=root,
        system=info.system,
        node=info.node,
        log_file=root / "Logs" / "application.log",
    )
    return _context


def get_context() -> ApplicationContext:
    """Return the global context, initializing it on first access."""
    if _context is None:
        return init_context()
    return _context


def reset_context() -> None:
    """Reset the global context (mainly for tests)."""
    global _context
    _context = None
