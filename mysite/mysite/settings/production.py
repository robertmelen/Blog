from .base import *
print("production settings")

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

