import lazy_logger
import sys

logger = lazy_logger.get_logger(__name__)

lazy_logger.log_to_console(logger)

lazy_logger.log_to_rotated_file(logger) # create log file log.out

@logger.patch
def main():
    print('Hello World!')

    print('Hello stdout!', file=sys.stdout)

if __name__ == '__main__':
    main()
