import logging

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

    ch = logging.StreamHandler()
    ch.setLevel(handler_level)

    formatter = logging.Formatter(logging_format)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger


def log_to_rotated_file(logger): pass


def log_to_syslogd(logger): pass


def main():
    logger = get_logger(__name__)
    log_to_console()
    logger.debug('yo')  # should be show up in terminal


if __name__ == "__main__":
    main()
