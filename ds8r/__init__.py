import os

from .ds8r import DS8R

__all__ = ['DS8R']

os.environ['PATH'] += ';' + os.path.dirname(os.path.abspath(__file__))
