[![Build Status](https://travis-ci.org/Python-Logging-For-Human/ezlogging.svg?branch=master)](https://travis-ci.org/Python-Logging-For-Human/ezlogging)

# lazy_logger

__lazy_logger__ is a tool help you to easily use Python's `logging` module by Python's `print` function.

## Quick start

### Requirements

- Git 1.8+
- Python 3.x


### Install

It can installing by pip

```
pip install lazy_logger
```

### Usage

```python
import lazy_logger
import sys

logger = lazy_logger.get_logger()

lazy_logger.log_to_console(logger)

lazy_logger.log_to_rotated_file(logger)

@logger.patch
def main():
    print('Hello World!')

    print('Hello stdout!', file=sys.stdout)

if __name__ == '__main__':
    main()
```

+ `log_to_console()`: Setting logger and auto transfer data to stderr.
+ `log_to_rotated_file()`: Setting logger and can save the data to file (default: log.out), and can rotate at same time.
+ `log_to_syslogd():` Setting logger and can transfer data to sysemd.

# test
py.test --capture=sys


# Thanks the contributions

+ tim(@timtan)
+ WendellLiu(@WendellLiu)
+ jackpan(@jackklpan)
+ Jason(@chairco)