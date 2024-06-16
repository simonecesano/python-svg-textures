import random
import string

class BaseTexture:
    def random_id(self):
        return ''.join(random.choices(string.ascii_lowercase, k=5))
    def __str__(self):
        return self.svg()
        
    def set_background(self, color):
        self.background = color
        return self

    def set_size(self, size):
        self.size = size
        return self
    def set_stroke(self, color):
        self.stroke = color
        return self

    def set_stroke_width(self, width):
        self.stroke_width = width
        return self

    def set_id(self, value=None):
        if value is None:
            return self.id
        self.id = value
        return self

    def heavier(self, factor=2):
        self.stroke_width *= factor
        return self

    def lighter(self, factor=2):
        self.stroke_width /= factor
        return self

    def thinner(self, factor=2):
        self.size *= factor
        return self

    def thicker(self, factor=2):
        self.size /= factor
        return self

    def url(self):
        return f"url(#{self.id})"
    
