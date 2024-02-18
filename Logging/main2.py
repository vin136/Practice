import logging.config
import logging.handlers
from pathlib import Path
import json

from config import logger

def set_up_logging():
    config_file = Path('logging_configs/1-stderr-file.json')
    with open(config_file) as f_in:
        config = json.load(f_in)
    logging.config.dictConfig(config)


def main():
    #set_up_logging()
    logger.debug('Debug msg')
    logger.info('Info msg')
    logger.warning('Warning  msg')
    logger.error('Error msg')
    logger.critical('Critical msg')

    try :
        a = 1/0
    except ZeroDivisionError:
        logger.exception('Exception msg')

if __name__ == '__main__':
    main()






