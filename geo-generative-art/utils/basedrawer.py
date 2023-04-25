import numpy as np
from PIL import Image, ImageDraw

from datalayers import DataLayers
from colors import Colors


class BaseDraw:
    def __init__(self, layers):
        assert isinstance(layers, DataLayers)
        self.layers = layers

    def set_colors(self, colors):
        assert isinstance(colors, Colors)
        assert len(colors) == len(self.layers)
        self.colors = colors

    def __transform__(self, p):
        x = np.clip(p.x, self.layers.get_sw().x, self.layers.get_ne().x)
        y = np.clip(p.y, self.layers.get_sw().y, self.layers.get_ne().y)
        x_trans = int(self.width * ((x - self.layers.get_sw().x) / (self.layers.get_ne().x - self.layers.get_sw().x])))
        y_trans = int(self.height * ((y - self.layers.get_sw().y) / (self.layers.get_ne().y - self.layers.get_sw().y)))
        return x_trans, self.height - y_trans

    def draw(self, width, height):
        self.width = width
        self.height = height
        self.img = Image.new('RGB', (width, height))
        self.draw = ImageDraw.Draw(self.img, 'RGBA')

    def save(self, path):
        self.img.save(path, 'PNG')

    def to_base64(self):
        pass
