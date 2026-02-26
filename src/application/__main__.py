import logging
import pathlib
from application.utils.logs_mana.logging_mana import LoggingManager
from application.utils.system_info.system_info_management import SystemInfo

logger = logging.getLogger('main')

def main() -> None:
    print("Executing application initialization stage")

    SystemInfo.initializing_dot_env_variables()
    LoggingManager.setup_logging()

    logging.info("Application started successfully!")
    logging.info("Application excecuted successfully!")

if __name__ == "__main__":
    main()