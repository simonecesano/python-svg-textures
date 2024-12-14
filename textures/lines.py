import random
import string

from .base import *

class Lines(BaseTexture):
    def __init__(self):
        self._size = 20
        self._stroke = '#343434'
        self._stroke_width = 2
        self._background = ''
        self._id = ''.join(random.choices(string.ascii_lowercase, k=5))
        self._orientation = ['diagonal']
        self._shape_rendering = 'auto'

    def path(self, orientation):
        s = self._size
        if orientation in ['0/8', 'vertical']:
            return f"M {s / 2}, 0 l 0, {s}"
        elif orientation == '1/8':
            return (f"M {-s / 4},{s} l {s / 2},{-s} "
                    f"M {s / 4},{s} l {s / 2},{-s} "
                    f"M {s * 3 / 4},{s} l {s / 2},{-s}")
        elif orientation in ['2/8', 'diagonal']:
            return (f"M 0,{s} l {s},{-s} "
                    f"M {-s / 4},{s / 4} l {s / 2},{-s / 2} "
                    f"M {3 / 4 * s},{5 / 4 * s} l {s / 2},{-s / 2}")
        elif orientation == '3/8':
            return (f"M 0,{3 / 4 * s} l {s},{-s / 2} "
                    f"M 0,{s / 4} l {s},{-s / 2} "
                    f"M 0,{s * 5 / 4} l {s},{-s / 2}")
        elif orientation in ['4/8', 'horizontal']:
            return f"M 0,{s / 2} l {s},0"
        elif orientation == '5/8':
            return (f"M 0,{-s / 4} l {s},{s / 2} "
                    f"M 0,{s / 4} l {s},{s / 2} "
                    f"M 0,{s * 3 / 4} l {s},{s / 2}")
        elif orientation == '6/8':
            return (f"M 0,0 l {s},{s} "
                    f"M {-s / 4},{3 / 4 * s} l {s / 2},{s / 2} "
                    f"M {s * 3 / 4},{-s / 4} l {s / 2},{s / 2}")
        elif orientation == '7/8':
            return (f"M {-s / 4},0 l {s / 2},{s} "
                    f"M {s / 4},0 l {s / 2},{s} "
                    f"M {s * 3 / 4},0 l {s / 2},{s}")
        else:
            return f"M {s / 2}, 0 l 0, {s}"

    def svg(self):
        svg = []
        svg.append(f'<pattern id="{self._id}" patternUnits="userSpaceOnUse" width="{self._size}" height="{self._size}">')

        if self.background:
            svg.append(f'<rect width="{self._size}" height="{self._size}" fill="{self._background}" />')

        for o in self._orientation:
            svg.append(f'<path d="{self.path(o)}" stroke="{self._stroke}" stroke-width="{self._stroke_width}" shape-rendering="{self._shape_rendering}" stroke-linecap="square" />')

        svg.append('</pattern>')
        return '\n'.join(svg)


    def orientation(self, *args):
        if not args:
            return self
        self._orientation = args
        return self

    def shape_rendering(self, value):
        self.shape_rendering = value
        return self
