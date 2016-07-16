import ezlogging
import sys

logger = ezlogging.get_logger()

@logger.patch
def main():
    print('Hello World!')

    print('Hello stdout!', file=sys.stdout)

if __name__ == '__main__':
    main()
