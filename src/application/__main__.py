"""Application entry point."""

import logging

from application.utils.logs_manager.logging_manager import setup_logging
from application.utils.system_info.system_info_management import load_environment


def main() -> None:
    """Initialize environment and logging, then run the application."""
    print("Executing application initialization stage")

    load_environment()
    setup_logging()

    logging.getLogger("main").info("Application started successfully!")
    logging.getLogger("main").info("Application executed successfully!")


if __name__ == "__main__":
    main()
