"""Environment and system information management."""

import platform
from pathlib import Path

from dotenv import dotenv_values, load_dotenv, set_key


def get_project_root() -> Path:
    """Return the project root directory (where pyproject.toml lives)."""
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "pyproject.toml").is_file():
            return parent
    raise FileNotFoundError("Project root not found: no pyproject.toml in parents.")


def ensure_env_file(env_path: Path) -> None:
    """Create the .env file if it does not exist; never delete existing values."""
    if not env_path.exists():
        env_path.touch()
        print(f"Created .env file at: {env_path}")


def load_environment(env_path: Path | None = None) -> dict[str, str | None]:
    """Load environment variables and populate system information keys."""
    root = get_project_root()
    env_file = env_path if env_path is not None else root / ".env"

    ensure_env_file(env_file)
    load_dotenv(env_file)

    set_key(str(env_file), "PROJECT_ROOT_DIRECTORY", str(root))
    system_info = platform.uname()
    set_key(str(env_file), "SYSTEM_INFORMATION", system_info.system)
    set_key(str(env_file), "NODE_INFORMATION", system_info.node)

    load_dotenv(env_file, override=True)
    return dict(dotenv_values(env_file))
