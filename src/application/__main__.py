"""Application entry point."""

import logging

from application.context import init_context
from application.utils.logs_manager.logging_manager import setup_logging


def main() -> None:
    """Initialize the global context and logging, then run the application."""
    print("Executing application initialization stage")

    context = init_context()
    setup_logging(log_file=context.log_file)

    logger = logging.getLogger("main")
    logger.info("Application started successfully!")
    logger.info("Application executed successfully!")


if __name__ == "__main__":
    main()
