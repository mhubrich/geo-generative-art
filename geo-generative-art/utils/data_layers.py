from shapely.geometry import Point


class DataLayers:
    def __init__(self, bbox, *layers):
        assert isinstance(bbox, (list, tuple))
        assert len(bbox) == 4
        assert len(layers) > 0
        assert all([isinstance(layer, (list, tuple)) for layer in layers])
        assert all([isinstance(p, Point) for layer in layers for p in layer])
        self.bbox = bbox
        self.layers = layers
        self.num_layers = len(layers)

    def __len__(self):
        return self.num_layers

    def __iter__(self):
        yield from self.layers

    def get_sw(self):
        return Point(self.bbox[0:2])

    def get_ne(self):
        return Point(self.bbox[2:4])
