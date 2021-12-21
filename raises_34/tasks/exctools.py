import sys
import traceback


def safe(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            print(sys.exc_info())
            traceback.print_exc()
    return wrapper
