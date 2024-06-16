import math
import random
import string

from .base import *

class Paths(BaseTexture):
    def __init__(self):
        self.width = 1
        self.height = 1
        self.size = 20
        self.stroke = '#343434'
        self.stroke_width = 2
        self.background = ''
        self.d = lambda s: f"M {s / 4},{s * 3 / 4}l{s / 4},{-s / 2}l{s / 4},{s / 2}"
        self.id = ''.join(random.choices(string.ascii_lowercase, k=5))
        self.fill = 'transparent'
        self.shape_rendering = 'auto'

    def path(self, pattern_type):
        s = self.size
        if pattern_type == 'squares':
            return f"M {s / 4} {s / 4} l {s / 2} 0 l 0 {s / 2} l {-s / 2} 0 Z"
        elif pattern_type == 'nylon':
            return (f"M 0 {s / 4} l {s / 4} 0 l 0 {-s / 4} "
                    f"M {s * 3 / 4} {s} l 0 {-s / 4} l {s / 4} 0 "
                    f"M {s / 4} {s / 2} l 0 {s / 4} l {s / 4} 0 "
                    f"M {s / 2} {s / 4} l {s / 4} 0 l 0 {s / 4}")
        elif pattern_type == 'waves':
            return (f"M 0 {s / 2} c {s / 8} {-s / 4} , {s * 3 / 8} {-s / 4} , {s / 2} 0 "
                    f"c {s / 8} {s / 4} , {s * 3 / 8} {s / 4} , {s / 2} 0 "
                    f"M {-s / 2} {s / 2} c {s / 8} {s / 4} , {s * 3 / 8} {s / 4} , {s / 2} 0 "
                    f"M {s} {s / 2} c {s / 8} {-s / 4} , {s * 3 / 8} {-s / 4} , {s / 2} 0")
        elif pattern_type == 'woven':
            return (f"M {s / 4},{s / 4}l{s / 2},{s / 2}M{s * 3 / 4},{s / 4}l{s / 2},{-s / 2} "
                    f"M{s / 4},{s * 3 / 4}l{-s / 2},{s / 2}M{s * 3 / 4},{s * 5 / 4}l{s / 2},{-s / 2} "
                    f"M{-s / 4},{s / 4}l{s / 2},{-s / 2}")
        elif pattern_type == 'crosses':
            return f"M {s / 4},{s / 4}l{s / 2},{s / 2}M{s / 4},{s * 3 / 4}l{s / 2},{-s / 2}"
        elif pattern_type == 'caps':
            return f"M {s / 4},{s * 3 / 4}l{s / 4},{-s / 2}l{s / 4},{s / 2}"
        elif pattern_type == 'hexagons':
            self.width = 3
            self.height = math.sqrt(3)
            return (f"M {s},0 l {s},0 l {s / 2},{(s * math.sqrt(3) / 2)} l {(-s / 2)},{(s * math.sqrt(3) / 2)} l {(-s)},0 "
                    f"l {(-s / 2)},{(-s * math.sqrt(3) / 2)} Z "
                    f"M 0,{s * math.sqrt(3) / 2} l {s / 2},0 "
                    f"M {(3 * s)},{s * math.sqrt(3) / 2} l {(-s / 2)},0")
        else:
            return pattern_type(s)

    def svg(self):
        p = self.path(self.d)
        svg = []
        svg.append(f'<pattern id="{self.id}" patternUnits="userSpaceOnUse" width="{self.size * self.width}" height="{self.size * self.height}">')

        if self.background:
            svg.append(f'<rect width="{self.size * self.width}" height="{self.size * self.height}" fill="{self.background}" />')

        svg.append(f'<path d="{p}" fill="{self.fill}" stroke="{self.stroke}" stroke-width="{self.stroke_width}" stroke-linecap="square" shape-rendering="{self.shape_rendering}" />')

        svg.append('</pattern>')
        return '\n'.join(svg)


    def set_shape_rendering(self, value):
        self.shape_rendering = value
        return self

    def set_d(self, d_func):
        self.d = d_func
        return self

    def set_fill(self, color):
        self.fill = color
        return self

    
