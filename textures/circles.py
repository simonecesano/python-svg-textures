import random
import string

from .base import *

class Circles(BaseTexture):
    def __init__(self):
        self.size = 20
        self.background = ''
        self.radius = 2
        self.complement = False
        self.fill = '#343434'
        self.stroke = '#343434'
        self.stroke_width = 0
        self.id = self.random_id()

    def svg(self):
        svg = []
        svg.append(f'<pattern id="{self.id}" patternUnits="userSpaceOnUse" width="{self.size}" height="{self.size}">')

        if self.background:
            svg.append(f'<rect width="{self.size}" height="{self.size}" fill="{self.background}" />')
        svg.append(f'<circle cx="{self.size / 2}" cy="{self.size / 2}" r="{self.radius}" fill="{self.fill}" stroke="{self.stroke}" stroke-width="{self.stroke_width}" />')
        if self.complement:
            for corner in [(0, 0), (0, self.size), (self.size, 0), (self.size, self.size)]:
                svg.append(f'<circle cx="{corner[0]}" cy="{corner[1]}" r="{self.radius}" fill="{self.fill}" stroke="{self.stroke}" stroke-width="{self.stroke_width}" />')

        svg.append('</pattern>')
        return '\n'.join(svg)


    def set_complement(self, value=True):
        self.complement = value
        return self

    def set_radius(self, radius):
        self.radius = radius
        return self

    def set_fill(self, color):
        self.fill = color
        return self

    def heavier(self, factor=2):
        self.radius *= factor
        return self

    def lighter(self, factor=2):
        self.radius /= factor
        return self

    # ----------------------------------------------------------------------

    # def thinner(self, factor=2):
    #     self.size *= factor
    #     return self

    # def thicker(self, factor=2):
    #     self.size /= factor
    #     return self
    
    # def set_stroke(self, color):
    #     self.stroke = color
    #     return self

    # def set_stroke_width(self, width):
    #     self.stroke_width = width
    #     return self

    # def set_id(self, value=None):
    #     if value is None:
    #         return self.id
    #     self.id = value
    #     return self

    # def url(self):
    #     return f"url(#{self.id})"

