import cairo, random
import numpy as np
import geopandas as gpd
from datetime import datetime

from deform import draw_deform


def transform(p, bbox, grid_x, grid_y):
    x, y = np.clip(p.x, bbox[0], bbox[2]), np.clip(p.y, bbox[1], bbox[3])
    x_trans = int(grid_x * ((x - bbox[0]) / (bbox[2] - bbox[0])))
    y_trans = int(grid_y * ((y - bbox[1]) / (bbox[3] - bbox[1])))
    return x_trans, grid_y - y_trans


def main():
    random.seed(0)
    bbox = (-123.14789772033691, 49.27150084847537, -123.1058406829834, 49.29524015790929)
    width, height = 1500, 1000
    shapealpha = 0.02
    side_min = 15
    side_max = 30
    layers_min = 20
    layers_max = 25
    base_deforms = 1
    final_deforms = 3
    base_variance = 120
    final_variance = 50
    colors = [(0.608, 0.365, 0.898), (0.945, 0.357, 0.71), (0.996, 0.894, 0.251), (0, 0.733, 0.976), (0, 0.961, 0.831), (0.608, 0.365, 0.898)]
    random.shuffle(colors)

    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    cr = cairo.Context(ims)
    cr.set_source_rgba(colors[0][0]*1.5, colors[0][1]*1.5, colors[0][2]*1.5, 0.1)
    cr.rectangle(0, 0, width, height)
    cr.fill()

    paths = ['data/cafe.geojson', 'data/starbucks.geojson', 'data/timhortons.geojson', 'data/mcdonalds.geojson', 'data/subway.geojson', 'data/burgerking.geojson']
    for i, path in enumerate(paths):
        color = colors[i] + (shapealpha, )
        df = gpd.read_file(path)
        for p in df.geometry:
            x_orig, y_orig = transform(p, bbox, width, height)
            side = random.randint(side_min, side_max)
            num_layers = random.randint(layers_min, layers_max)
            draw_deform(cr, x_orig, y_orig, side, color, base_deforms, final_deforms, base_variance, final_variance, num_layers)
        shapealpha += 0.005
    ims.write_to_png('img_' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.png')

if __name__ == "__main__":
    main()
