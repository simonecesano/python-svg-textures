import random
import string

class Lines:
    def __init__(self):
        self.size = 20
        self.stroke = '#343434'
        self.stroke_width = 2
        self.background = ''
        self.id = ''.join(random.choices(string.ascii_lowercase, k=5))
        self.orientation = ['diagonal']
        self.shape_rendering = 'auto'

    def path(self, orientation):
        s = self.size
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
        svg.append(f'<pattern id="{self.id}" patternUnits="userSpaceOnUse" width="{self.size}" height="{self.size}">')

        if self.background:
            svg.append(f'<rect width="{self.size}" height="{self.size}" fill="{self.background}" />')

        for o in self.orientation:
            svg.append(f'<path d="{self.path(o)}" stroke="{self.stroke}" stroke-width="{self.stroke_width}" shape-rendering="{self.shape_rendering}" stroke-linecap="square" />')

        svg.append('</pattern>')
        return '\n'.join(svg)

    # def heavier(self, factor=2):
    #     self.stroke_width *= factor
    #     return self

    # def lighter(self, factor=2):
    #     self.stroke_width /= factor
    #     return self

    # def thinner(self, factor=2):
    #     self.size *= factor
    #     return self

    # def thicker(self, factor=2):
    #     self.size /= factor
    #     return self

    def set_orientation(self, *args):
        if not args:
            return self
        self.orientation = args
        return self

    def set_shape_rendering(self, value):
        self.shape_rendering = value
        return self

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
