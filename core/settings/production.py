from .base import *

DEBUG = int(os.environ.get("DEBUG", default=1))

try:
    from .local import *
except ImportError:
    pass
