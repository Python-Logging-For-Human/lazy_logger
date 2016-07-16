import functools
import sys
import logging

_real_print = print


def _fake_print(*args, file=None, **kwargs):
    if file is None:
        _real_print('Logger!__ program.py __: ', *args, **kwargs)
    else:
        _real_print(*args, file=file, **kwargs)


def monkeypatch_method(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator


@monkeypatch_method(logging.Logger)
def patch(self, f):

        @functools.wraps(f)
        def patched(*args, **kwargs):
            import builtins
            builtins.print = _fake_print
            try:
                f(*args, **kwargs)
            finally:
                builtins.print = _real_print

        return patched


def get_logger():
    return logging.getLogger(__name__)

'''
class Logger(logging.Logger):
    
    def __init__(self, *args, **kwargs):
        super(Logger, self).__init__(*args, **kwargs)

    def patch(self, f):

        @functools.wraps(f)
        def patched(*args, **kwargs):
            import builtins
            builtins.print = _fake_print
            try:
                f(*args, **kwargs)
            finally:
                builtins.print = _real_print

        return patched
'''

logger = Logger('name')


logger = get_logger()

@logger.patch
def main():

    print('Hello!')

    print('Hello stdout!', file=sys.stdout)


if __name__ == '__main__':
    main()
