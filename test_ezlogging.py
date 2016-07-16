import ezlogging as ezlogging
import sys
import time


def test_log_to_console(capsys):
    logger = ezlogging.get_logger('noname')
    ezlogging.log_to_console(logger)
    logger.debug('yo')

    out, err = capsys.readouterr()
    assert err[0:10] == time.strftime("%Y-%m-%d")
    assert err[26:] == 'noname - DEBUG - yo\n'


def test_log_to_rotated_file():
    pass
