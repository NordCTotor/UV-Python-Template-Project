import logging
import pathlib
from application.utils.logs_mana.logging_mana import LoggingManager
from application.utils.system_info.system_info_management import SystemInfo

logger = logging.getLogger('main')

def main() -> None:
    print("Executing logp as a script.")
    HOME_DIR = pathlib.Path(__file__).parent.parent.parent
    print(f"Home directory: {HOME_DIR}")

    SystemInfo.initializing_dot_env_variables()
    LoggingManager.setup_logging()
    logger.debug("Debug message from __main__")

if __name__ == "__main__":
    main()