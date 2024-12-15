import random
import string

class BaseTexture:
    def random_id(self):
        return ''.join(random.choices(string.ascii_lowercase, k=5))

    def __str__(self):
        return self.svg()
        
    def background(self, color):
        self._background = color
        return self
    
    def size(self, size):
        self._size = size
        return self

    def stroke(self, color):
        self._stroke = color
        return self

    def stroke_width(self, width):
        self._stroke_width = width
        return self

    def id(self, value=None):
        if value is None:
            return self.id
        self._id = value
        return self

    def heavier(self, factor=2):
        self._stroke_width *= factor
        return self

    def lighter(self, factor=2):
        self._stroke_width /= factor
        return self

    def thinner(self, factor=2):
        self._size *= factor
        return self

    def thicker(self, factor=2):
        self._size /= factor
        return self

    def url(self):
        return f"url(#{self._id})"
    
