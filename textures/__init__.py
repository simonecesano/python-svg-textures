from .circles import *
from .lines   import *
from .paths   import *

class Texture:
    def lines(self, *args):
        return Lines(*args)
    def circles(self, *args):
        return Circles(*args)
    def paths(self, *args):
        return Paths(*args)
