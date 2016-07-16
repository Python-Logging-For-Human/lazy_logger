import logging
import logging.handlers

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGGER_LEVEL = logging.DEBUG
HANDLER_LEVEL = logging.DEBUG

root_logger = logging.getLogger()


def get_logger(name):
    return logging.getLogger(name)


def log_to_console(logger=root_logger,
                   logger_level=LOGGER_LEVEL,
                   handler_level=HANDLER_LEVEL,
                   logging_format=FORMAT):
    '''
    :param logger: if not set, will apply settings to root logger
    :param logger_level:
    :param handler_level:
    :param logging_format:
    :return:
    '''

    logger.setLevel(logger_level)

    handler = logging.StreamHandler()
    handler.setLevel(handler_level)

    formatter = logging.Formatter(logging_format)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


FILE_NAME = 'log.out'
MAX_BYTE = 10 * 1024 * 1204
BACK_COUNT = 10


def log_to_rotated_file(logger=root_logger,
                        logger_level=LOGGER_LEVEL,
                        handler_level=HANDLER_LEVEL,
                        logging_format=FORMAT,
                        max_byte=MAX_BYTE,
                        file_name=FILE_NAME,
                        back_count=BACK_COUNT):

    # Set up a specific logger with our desired output level
    logger.setLevel(logger_level)

    # Add the log message handler to the logger
    handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=max_byte, backupCount=back_count)
    handler.setLevel(handler_level)

    formatter = logging.Formatter(logging_format)
    handler.setFormatter(formatter)

    logger.addHandler(handler)


def log_to_syslogd(logger): pass


def main():

    logger = get_logger(__name__)
    log_to_console(logger, logger_level=logging.CRITICAL)
    logger.debug('yo')  # should be show up in terminal

    log_to_rotated_file(logger)
    logger.debug('yoyo')  # should be show up in terminal

if __name__ == "__main__":
    main()
