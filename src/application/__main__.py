import logging
import pathlib
from application.utils.logs_mana.logging_mana import LoggingManager

logger = logging.getLogger('main')

def main() -> None:
    print("Executing logp as a script.")
    HOME_DIR = pathlib.Path(__file__).parent.parent.parent
    print(f"Home directory: {HOME_DIR}")
    LoggingManager.setup_logging(home_dir=HOME_DIR)
    logger.debug("Debug message from __main__")

if __name__ == "__main__":
    main()