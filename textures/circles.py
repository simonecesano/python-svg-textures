import random
import string

from .base import *

class Circles(BaseTexture):
    def __init__(self):
        self.size = 20
        self.background = ''
        self._radius = 2
        self._complement = False
        self._fill = '#343434'
        self._stroke = '#343434'
        self._stroke_width = 0
        self.id = self.random_id()

    def svg(self):
        svg = []
        svg.append(f'<pattern id="{self.id}" patternUnits="userSpaceOnUse" width="{self.size}" height="{self.size}">')

        if self.background:
            svg.append(f'<rect width="{self.size}" height="{self.size}" fill="{self.background}" />')
        svg.append(f'<circle cx="{self.size / 2}" cy="{self.size / 2}" r="{self._radius}" fill="{self._fill}" stroke="{self._stroke}" stroke-width="{self._stroke_width}" />')
        if self.complement:
            for corner in [(0, 0), (0, self.size), (self.size, 0), (self.size, self.size)]:
                svg.append(f'<circle cx="{corner[0]}" cy="{corner[1]}" r="{self._radius}" fill="{self._fill}" stroke="{self._stroke}" stroke-width="{self._stroke_width}" />')

        svg.append('</pattern>')
        return '\n'.join(svg)


    def complement(self, value=True):
        self._complement = value
        return self

    def radius(self, radius):
        self._radius = radius
        return self

    def fill(self, color):
        self._fill = color
        return self

    def heavier(self, factor=2):
        self._radius *= factor
        return self

    def lighter(self, factor=2):
        self._radius /= factor
        return self
