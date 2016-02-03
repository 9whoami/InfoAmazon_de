# -*- coding: utf-8 -*-

from .base import *
try:
    from .local import *
except ImportError:
    SystemExit("No module named local.py. "
               "Please, create this module from 'local.skeleton'")