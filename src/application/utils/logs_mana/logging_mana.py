import logging
import logging.config
from yaml import safe_load
from pathlib import Path

class LoggingManager:


    @staticmethod
    def get_logging_conf_from_file(filename: str) -> dict:
        """
        Reads a YAML file and returns its content as a dictionary.
        """
        file_path = Path(__file__).parent / 'logging_conf_files' / filename
        if not file_path.exists():
            raise FileNotFoundError(f"Configuration file {filename} not found in {file_path.parent}")
        with open(file_path, 'r') as file:
            return safe_load(file)
        

    @staticmethod
    def setup_logging(*,home_dir: Path = None) -> None:

        config_dict = {
            'version': 1,
            'disable_existing_loggers': True,
            'formatters': LoggingManager.get_logging_conf_from_file(filename='formatters.yaml'),
            'handlers': LoggingManager.get_logging_conf_from_file(filename='handlers.yaml'),
            'loggers': LoggingManager.get_logging_conf_from_file(filename= 'loggers.yaml'),
            }
        
        config_dict['handlers']['file']['filename'] = Path(home_dir) / 'Logs' / 'application.log'

        logging.config.dictConfig(config_dict)