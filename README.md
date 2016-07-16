[![Build Status](https://travis-ci.org/Python-Logging-For-Human/ezlogging.svg?branch=master)](https://travis-ci.org/Python-Logging-For-Human/ezlogging)

# lazy_logger

__lazy_logger__ is a tool help you to easily use python's `logging` module by python's print.

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

@logger.patch
def main():
    print('Hello World!')

    print('Hello stdout!', file=sys.stdout)

if __name__ == '__main__':
    main()
```

# test
py.test --capture=sys


# Thanks the contributions

+ Tim(@tim)
+ Wende(@WendellLiu)
+ Jack(@jackklpan)
+ Jason(@chairco)