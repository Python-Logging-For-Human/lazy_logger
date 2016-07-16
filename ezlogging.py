import logging

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGGER_LEVEL = logging.DEBUG
HANDLER_LEVEL = logging.DEBUG


def get_logger(name):
    return logging.getLogger(name)


def log_to_console(logger,
                      logger_level=LOGGER_LEVEL,
                      handler_level=HANDLER_LEVEL,
                      format=FORMAT):

    logger.setLevel(logger_level)

    ch = logging.StreamHandler()
    ch.setLevel(handler_level)

    formatter = logging.Formatter(format)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger


def log_to_rotated_file(logger): pass


def log_to_syslogd(logger): pass


if __name__ == "__main__":

    logger = get_logger(__name__)

    logger = log_to_console(logger)

    logger.debug('yo')  # should be show up in terminal
